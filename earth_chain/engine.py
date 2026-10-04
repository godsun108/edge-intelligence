"""Earth Chain: local-first, standard-library hemp market evidence engine.
No trading, financial execution, scraping, or fabricated pricing.
Usage: python earth_chain/engine.py earth_chain/observations.json
"""
import json, sys, hashlib, datetime
from pathlib import Path
GRADES={"hurd","bast_fiber","grain","biomass","biochar"}
KINDS={"ask","bid","executed_transaction"}
REQUIRED={"id","timestamp","commodity","kind","price_usd_per_metric_ton","source","region","evidence_url"}
def validate(rows):
    seen=set(); valid=[]; errors=[]
    for n,row in enumerate(rows,1):
        problems=[]
        missing=REQUIRED-set(row)
        if missing: problems.append("missing "+",".join(sorted(missing)))
        if row.get("id") in seen: problems.append("duplicate id")
        if row.get("commodity") not in GRADES: problems.append("invalid commodity")
        if row.get("kind") not in KINDS: problems.append("invalid kind")
        p=row.get("price_usd_per_metric_ton")
        if isinstance(p,bool) or not isinstance(p,(int,float)) or not 0<p<10000000: problems.append("invalid price")
        for key in ("source","region","evidence_url"):
            if not isinstance(row.get(key),str) or not row[key].strip(): problems.append("missing "+key)
        try: datetime.datetime.fromisoformat(row.get("timestamp","").replace("Z","+00:00"))
        except (ValueError,AttributeError): problems.append("invalid timestamp")
        if row.get("kind")=="executed_transaction" and not row.get("transaction_evidence_verified",False):
            problems.append("transaction evidence not verified")
        if problems: errors.append({"row":n,"issues":problems})
        else: valid.append(row); seen.add(row["id"])
    return valid,errors
def report(rows):
    valid,errors=validate(rows)
    counts={g:{k:0 for k in sorted(KINDS)} for g in sorted(GRADES)}
    for row in valid: counts[row["commodity"]][row["kind"]]+=1
    payload={"schema":"earth-chain.market.v0.1","observations":len(valid),"rejected":errors,"counts":counts,"prices_published":False,"note":"No benchmark or index is published; quotes and verified transactions remain separate."}
    payload["digest_sha256"]=hashlib.sha256(json.dumps(valid,sort_keys=True).encode()).hexdigest()
    return payload
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: python earth_chain/engine.py observations.json")
    data=json.loads(Path(sys.argv[1]).read_text())
    if not isinstance(data,list): raise SystemExit("Expected JSON array")
    print(json.dumps(report(data),indent=2))
