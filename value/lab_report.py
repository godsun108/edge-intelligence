"""Descriptive VALUE laboratory report card."""
from collections import defaultdict


def report(freeze, outcomes):
    outcomes=list(outcomes)
    assessed={o["signal_id"]:o for o in outcomes}
    result={
      "schema":"edge.value.lab.report.v0.1",
      "frozen_candidates":freeze.get("candidate_count",0),
      "assessed_outcomes":len(outcomes),
      "status":"INSUFFICIENT_OUTCOMES" if not outcomes else "DESCRIPTIVE_ONLY",
      "warning":"No method is declared superior; causal decision value is not established.",
      "methods":{},
    }
    value_ids=freeze.get("value_selected",[])
    methods={"value_top_budget":value_ids,**freeze.get("baselines",{})}
    for name,ids in methods.items():
        labeled=[assessed[i] for i in ids if i in assessed]
        result["methods"][name]={
          "selected":len(ids),
          "assessed":len(labeled),
          "consequence_hits":sum(bool(x.get("consequence_observed")) for x in labeled),
          "timely_hits":sum(bool(x.get("timely")) for x in labeled),
        }
    return result
