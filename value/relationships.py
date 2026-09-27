"""EDGE // VALUE explicit relationship graph.

Builds only relationships literally present in normalized observations.
No embeddings, inferred causality, or semantic similarity.
"""
import json
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

CVE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)


def entities(observation):
    found=set()
    data=observation.get("data") or {}
    text=" ".join([str(observation.get("id","")),str(observation.get("title","")),json.dumps(data,sort_keys=True)])
    for x in CVE.findall(text): found.add(("cve",x.upper()))
    for key,kind in (("vendor","vendor"),("product","product")):
        value=data.get(key)
        if isinstance(value,str) and value.strip(): found.add((kind,value.strip()))
    return sorted(found)


def build(snapshot):
    nodes={}
    edges=defaultdict(lambda:{"observations":[],"sources":set()})
    for o in snapshot.get("observations",[]):
        es=entities(o)
        for kind,value in es:
            nid=f"{kind}:{value}"
            nodes[nid]={"id":nid,"kind":kind,"value":value}
        for a,b in combinations(es,2):
            left=f"{a[0]}:{a[1]}";right=f"{b[0]}:{b[1]}"
            key=tuple(sorted((left,right)))
            edges[key]["observations"].append({"source":o.get("source"),"source_id":o.get("id")})
            if o.get("source"): edges[key]["sources"].add(o["source"])
    return {
        "schema":"edge.value.relationships.v0.1",
        "semantics":"explicit co-occurrence only; association is not causation",
        "nodes":sorted(nodes.values(),key=lambda x:x["id"]),
        "edges":[{
            "left":k[0],"right":k[1],
            "observation_count":len(v["observations"]),
            "independent_source_count":len(v["sources"]),
            "sources":sorted(v["sources"]),
            "observations":v["observations"],
        } for k,v in sorted(edges.items())],
    }


def main():
    snapshot=json.loads(Path("radar/data/latest.json").read_text())
    out=Path("value/data/relationships.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(build(snapshot),indent=2,sort_keys=True)+"\n")


if __name__=="__main__": main()
