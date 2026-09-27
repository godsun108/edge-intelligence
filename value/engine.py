"""EDGE // VALUE deterministic attention-priority engine.

A VALUE score prioritizes inspection. It is not truth, probability, profit,
importance in an objective sense, or an instruction to act.
"""
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List

WEIGHTS = {
    "relevance": 0.22,
    "consequence": 0.20,
    "actionability": 0.18,
    "novelty": 0.15,
    "reliability": 0.15,
    "time_advantage": 0.10,
}
PENALTY_WEIGHTS = {
    "uncertainty": 0.35,
    "noise": 0.20,
    "duplication": 0.25,
    "manipulation_risk": 0.20,
}
DEFAULT_THRESHOLD = 45.0
DEFAULT_ATTENTION_BUDGET = 10


def _unit(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be between 0 and 1")
    return value


@dataclass(frozen=True)
class Candidate:
    id: str
    relevance: float
    consequence: float
    actionability: float
    novelty: float
    reliability: float
    time_advantage: float
    uncertainty: float = 0.0
    noise: float = 0.0
    duplication: float = 0.0
    manipulation_risk: float = 0.0

    def validated(self) -> "Candidate":
        if not self.id:
            raise ValueError("candidate id is required")
        for name, value in asdict(self).items():
            if name != "id":
                _unit(name, value)
        return self


def score(candidate: Candidate) -> Dict:
    c = candidate.validated()
    raw = sum(getattr(c, name) * weight for name, weight in WEIGHTS.items())

    # Reliability is a gate as well as a positive factor: spectacular but
    # poorly supported claims must not dominate attention merely by consequence.
    reliability_gate = 0.25 + 0.75 * c.reliability

    penalty_load = sum(
        getattr(c, name) * weight for name, weight in PENALTY_WEIGHTS.items()
    )
    penalty_multiplier = max(0.0, 1.0 - penalty_load)
    value = 100.0 * raw * reliability_gate * penalty_multiplier

    return {
        "id": c.id,
        "value_score": round(value, 2),
        "positive_signal": round(raw, 4),
        "reliability_gate": round(reliability_gate, 4),
        "penalty_multiplier": round(penalty_multiplier, 4),
        "factors": {name: getattr(c, name) for name in WEIGHTS},
        "penalties": {name: getattr(c, name) for name in PENALTY_WEIGHTS},
        "meaning": "attention_priority_only",
        "version": "edge.value.v0.1",
    }


def evaluate(candidates: Iterable[Candidate]) -> List[Dict]:
    return sorted(
        (score(candidate) for candidate in candidates),
        key=lambda item: (-item["value_score"], item["id"]),
    )


def rank(candidates: Iterable[Candidate], threshold: float = DEFAULT_THRESHOLD, max_items: int = DEFAULT_ATTENTION_BUDGET) -> Dict:
    threshold = float(threshold)
    if not 0.0 <= threshold <= 100.0:
        raise ValueError("threshold must be between 0 and 100")
    if max_items < 1:
        raise ValueError("max_items must be at least 1")
    ranked: List[Dict] = evaluate(candidates)
    eligible = [item for item in ranked if item["value_score"] >= threshold]
    surfaced = eligible[:max_items]
    return {
        "schema": "edge.value.queue.v0.1",
        "threshold": threshold,
        "state": "SIGNAL" if surfaced else "NO_SIGNAL",
        "items": surfaced,
        "evaluated": len(ranked),
        "eligible": len(eligible),
        "suppressed_above_threshold": max(0, len(eligible) - len(surfaced)),
        "attention_budget": max_items,
    }
