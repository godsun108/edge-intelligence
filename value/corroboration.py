"""Deterministic explicit-identifier corroboration graph.

v0.1 links only identifiers literally present in normalized observations.
It does not infer semantic equivalence and does not modify VALUE scores.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

CVE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)


def identifiers(observation):
    text = " ".join([
        str(observation.get("id", "")),
        str(observation.get("title", "")),
        json.dumps(observation.get("data", {}), sort_keys=True),
    ])
    return sorted({m.upper() for m in CVE.findall(text)})


def build(snapshot):
    groups = defaultdict(list)
    for o in snapshot.get("observations", []):
        for ident in identifiers(o):
            groups[ident].append({
                "source": o.get("source"),
                "source_id": o.get("id"),
                "title": o.get("title"),
                "url": o.get("url"),
            })
    edges = []
    for ident, records in sorted(groups.items()):
        sources = sorted({r["source"] for r in records if r["source"]})
        edges.append({
            "identifier": ident,
            "records": records,
            "record_count": len(records),
            "independent_source_count": len(sources),
            "sources": sources,
            "corroborated": len(sources) >= 2,
        })
    return {
        "schema": "edge.corroboration.v0.1",
        "semantics": "explicit-identifier linkage only; no semantic equivalence inference",
        "groups": edges,
    }


def main():
    snapshot = json.loads(Path("radar/data/latest.json").read_text())
    out = Path("value/data/corroboration.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(snapshot), indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
