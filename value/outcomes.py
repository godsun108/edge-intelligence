"""EDGE // VALUE outcome/calibration primitives.

Outcome records are append-only observations about prior frozen signals.
They never modify the original VALUE score.
"""
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Outcome:
    signal_id: str
    value_version: str
    original_score: float
    surfaced_at: str
    assessed_at: str
    inspected: bool
    decision_changed: bool
    consequence_observed: bool
    timely: bool
    notes: str = ""

    def record(self):
        if not self.signal_id or not self.value_version:
            raise ValueError("signal_id and value_version are required")
        if not 0 <= float(self.original_score) <= 100:
            raise ValueError("original_score must be between 0 and 100")
        data = asdict(self)
        data["schema"] = "edge.value.outcome.v0.1"
        data["semantics"] = "append-only assessment; original signal remains immutable"
        return data


def summarize(records):
    rows = list(records)
    n = len(rows)
    if not n:
        return {"schema":"edge.value.calibration.v0.1","assessed":0}
    def rate(key):
        return round(sum(bool(r[key]) for r in rows) / n, 4)
    return {
        "schema": "edge.value.calibration.v0.1",
        "assessed": n,
        "inspection_rate": rate("inspected"),
        "decision_change_rate": rate("decision_changed"),
        "observed_consequence_rate": rate("consequence_observed"),
        "timely_rate": rate("timely"),
        "warning": "descriptive calibration only; does not prove causal decision value",
    }
