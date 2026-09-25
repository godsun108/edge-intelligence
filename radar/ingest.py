import json, urllib.request, datetime, pathlib, hashlib
UA={"User-Agent":"edge-radar/0.2"}
def get(url):
 req=urllib.request.Request(url,headers=UA)
 with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
def fp(o): return hashlib.sha256(json.dumps([o["source"],o["id"],o["title"],o.get("url",""),o.get("data",{})],sort_keys=True).encode()).hexdigest()
def main():
 now=datetime.datetime.now(datetime.timezone.utc).isoformat(); obs=[]
 # Real public source #1: USGS significant earthquakes
 q=get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson")
 for f in q.get("features",[]):
  p=f.get("properties",{}); o={"id":f.get("id"),"source":"USGS","title":p.get("title") or p.get("place") or "Earthquake","url":p.get("url") or "","observed_at":p.get("time"),"retrieved_at":now,"tags":["earth","earthquake"],"data":{"magnitude":p.get("mag"),"place":p.get("place")}};o["fingerprint"]=fp(o);obs.append(o)
 # Real public source #2: NASA EONET open natural-event catalog
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
 payload={"schema":"edge.radar.snapshot.v1","generated_at":now,"sources":["USGS","NASA EONET"],"observations":obs,"changes":changed}
 p.write_text(json.dumps(payload,separators=(",",":")))
 (root/"briefing.json").write_text(json.dumps({"generated_at":now,"items":changed[:40]},separators=(",",":")))
if __name__=="__main__":main()
