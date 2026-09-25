import json, urllib.request, datetime, pathlib, hashlib\nUA={"User-Agent":"edge-radar/0.2"}
def get(url):
 req=urllib.request.Request(url,headers=UA)
 with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
def fp(o): return hashlib.sha256(json.dumps([o["source"],o["id"],o["title"],o.get("url",""),o.get("data",{})],sort_keys=True).encode()).hexdigest()
def days_until(value):
 if not value:return None
 for fmt in ("%m/%d/%Y","%Y-%m-%d"):
  try:return (datetime.datetime.strptime(value,fmt).date()-datetime.datetime.now(datetime.timezone.utc).date()).days
  except ValueError:pass
 return None

def enrich_opportunity(o):
 if o.get("source")!="Grants.gov":return o
 d=o.get("data",{}); days=days_until(d.get("closeDate")); urgency="UNKNOWN"
 if days is not None:
  urgency="CLOSED" if days<0 else ("URGENT" if days<=7 else ("SOON" if days<=30 else "OPEN"))
 o["opportunity"]={"agency":d.get("agency"),"number":d.get("number"),"close_date":d.get("closeDate"),"days_until_close":days,"urgency":urgency}
 return o

def score(o,rules):
 text=(o.get("title","")+" "+" ".join(o.get("tags",[]))).lower(); best=0; reasons=[]
 for r in rules:
  pts=0; why=[]
  for term in r.get("terms",[]):
   if term.lower() in text: pts+=r.get("term_weight",10);why.append("matched "+term)
  if o.get("change")=="new": pts+=r.get("new_weight",5)
  if o.get("change")=="changed": pts+=r.get("change_weight",7)
  if pts>best: best=pts;reasons=why
 return best,reasons

def load_config():
 try: return json.loads(pathlib.Path("radar/config.json").read_text())
 except Exception: return {}

def savant_candidates(observations, now):
 out=[]
 for o in observations:
  if o.get("change")=="same" or o.get("relevance",0)<=0: continue
  out.append({
   "id":o.get("source","source")+":"+str(o.get("id")),
   "claim_seed":o.get("title") or "Untitled observation",
   "source":o.get("url") or "",
   "source_title":o.get("title") or "",
   "publisher":o.get("source") or "",
   "observed_at":o.get("observed_at"),
   "retrieved_at":o.get("retrieved_at") or now,
   "source_class":"PRIMARY" if o.get("source") in ("USGS","Grants.gov","NASA EONET") else "UNKNOWN",
   "stance":"CONTEXT",
   "relevance":o.get("relevance",0),
   "reasons":o.get("reasons",[]),
   "radar_change":o.get("change"),
   "import_semantics":"CANDIDATE_ONLY"
  })
 return sorted(out,key=lambda x:x.get("relevance",0),reverse=True)[:40]

def main():
 cfg=load_config()
 now=datetime.datetime.now(datetime.timezone.utc).isoformat(); obs=[]
 # Real public source #1: USGS significant earthquakes
 q=get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson")
 for f in q.get("features",[]):
  p=f.get("properties",{}); o={"id":f.get("id"),"source":"USGS","title":p.get("title") or p.get("place") or "Earthquake","url":p.get("url") or "","observed_at":p.get("time"),"retrieved_at":now,"tags":["earth","earthquake"],"data":{"magnitude":p.get("mag"),"place":p.get("place")}};o["fingerprint"]=fp(o);obs.append(o)
 # Real public source #2: Grants.gov public opportunity search
 try:
  payload=json.dumps({"keyword":cfg.get("grants_keyword",""),"oppStatuses":"forecasted|posted","rows":100,"startRecordNum":0}).encode()
  req=urllib.request.Request("https://api.grants.gov/v1/api/search2",data=payload,headers={**UA,"Content-Type":"application/json"},method="POST")
  with urllib.request.urlopen(req,timeout=30) as r: grants=json.load(r)
  for g in grants.get("data",{}).get("oppHits",[]):
   oid=str(g.get("id") or g.get("number") or g.get("title")); title=g.get("title") or "Grant opportunity"
   o={"id":oid,"source":"Grants.gov","title":title,"url":"https://www.grants.gov/search-results-detail/"+oid,"observed_at":g.get("openDate"),"retrieved_at":now,"tags":["grant","funding opportunity",str(g.get("agencyName","")),str(g.get("oppStatus",""))],"data":{"agency":g.get("agencyName"),"agencyCode":g.get("agencyCode"),"closeDate":g.get("closeDate"),"openDate":g.get("openDate"),"number":g.get("number"),"status":g.get("oppStatus"),"aln":g.get("alnist",[])}};o["fingerprint"]=fp(o);obs.append(o)
 except Exception as ex: print("Grants.gov:",ex)
 # Real public source #3: NASA EONET open natural-event catalog
 e=get("https://eonet.gsfc.nasa.gov/api/v3/events?status=open&limit=100")
 for x in e.get("events",[]):
  cats=[c.get("title","") for c in x.get("categories",[])];o={"id":x.get("id"),"source":"NASA EONET","title":x.get("title") or "Natural event","url":x.get("link") or "","observed_at":(x.get("geometry") or [{}])[-1].get("date"),"retrieved_at":now,"tags":["earth"]+cats,"data":{"categories":cats}};o["fingerprint"]=fp(o);obs.append(o)
 root=pathlib.Path("radar/data");root.mkdir(parents=True,exist_ok=True); prev={}
 p=root/"latest.json"
 if p.exists():
  try: prev={o["source"]+":"+str(o["id"]):o.get("fingerprint") for o in json.loads(p.read_text()).get("observations",[])}
  except Exception: pass
 for o in obs:
  k=o["source"]+":"+str(o["id"]);o["change"]="new" if k not in prev else ("changed" if prev[k]!=o["fingerprint"] else "same")
 changed=[o for o in obs if o["change"]!="same"]
 rules=[]
 try: rules=json.loads(pathlib.Path("radar/rules.json").read_text()).get("rules",[])
 except Exception: pass
 for o in changed:
  o["relevance"],o["reasons"]=score(o,rules)
 changed.sort(key=lambda o:o.get("relevance",0),reverse=True)
 payload={"schema":"edge.radar.snapshot.v1","generated_at":now,"sources":["USGS","Grants.gov","NASA EONET"],"observations":obs,"changes":changed}
 p.write_text(json.dumps(payload,separators=(",",":")))
 brief=[o for o in changed if o.get("relevance",0)>0][:40]
 (root/"briefing.json").write_text(json.dumps({"generated_at":now,"items":brief},separators=(",",":")))
 (root/"savant_candidates.json").write_text(json.dumps({"schema":"edge.savant.candidates.v1","generated_at":now,"items":savant_candidates(changed,now)},separators=(",",":")))
if __name__=="__main__":main()
