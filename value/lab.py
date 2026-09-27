"""EDGE // VALUE prospective laboratory.

Produces frozen candidate evaluations and deliberately simple baselines.
This artifact is for measurement, not human attention.
"""
import json
from pathlib import Path
from value.bridge import derive
from value.engine import evaluate, DEFAULT_THRESHOLD


def baselines(observations, budget=10):
    rows=list(observations)
    newest=sorted(rows,key=lambda o:str(o.get("observed_at") or ""),reverse=True)[:budget]
    source=sorted(rows,key=lambda o:(str(o.get("source") or ""),str(o.get("id") or "")))[:budget]
    deterministic=sorted(rows,key=lambda o:str(o.get("source",""))+":"+str(o.get("id","")))[:budget]
    def ids(xs): return [str(x.get("source",""))+":"+str(x.get("id","")) for x in xs]
    return {
        "newest_first":ids(newest),
        "source_order":ids(source),
        "deterministic_control":ids(deterministic),
    }


def freeze(snapshot, generated_at=None, budget=10):
    observations=snapshot.get("observations",[])
    candidates=[derive(o)[0] for o in observations]
    scored=evaluate(candidates)
    value_selected=[x["id"] for x in scored if x["value_score"] >= DEFAULT_THRESHOLD][:budget]
    return {
        "schema":"edge.value.lab.freeze.v0.1",
        "generated_at":generated_at or snapshot.get("generated_at"),
        "input_schema":snapshot.get("schema"),
        "value_version":"edge.value.v0.1",
        "attention_budget":budget,
        "candidate_count":len(scored),
        "candidates":scored,
        "value_selected":value_selected,
        "value_threshold":DEFAULT_THRESHOLD,
        "baselines":baselines(observations,budget),
        "semantics":"prospective measurement artifact; not an attention queue or instruction",
        "rules":{
            "prospective_only":True,
            "no_retroactive_score_rewrite":True,
            "no_final_test_tuning":True,
            "silence_is_measured":True,
        },
    }


def main():
    snapshot=json.loads(Path("radar/data/latest.json").read_text())
    out=Path("value/data/lab-latest.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(freeze(snapshot),indent=2,sort_keys=True)+"\n")


if __name__=="__main__": main()
