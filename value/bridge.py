"""RADAR -> EDGE // VALUE bridge.

Derivations are intentionally conservative. Unknown user-specific relevance or
actionability is not invented. Every derived factor carries inspectable reasons.
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from value.engine import Candidate, rank

PRIMARY_SOURCES = {"USGS", "Grants.gov", "NASA EONET", "CISA KEV"}


def clamp(x):
    return max(0.0, min(1.0, float(x)))


def derive(observation, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    source = observation.get("source", "")
    tags = {str(x).lower() for x in observation.get("tags", [])}
    data = observation.get("data") or {}
    change = observation.get("change", "same")
    radar_relevance = max(0.0, float(observation.get("relevance", 0) or 0))

    reasons = {}
    # RADAR rule scores are unbounded attention points, so map conservatively.
    relevance = clamp(radar_relevance / 50.0)
    reasons["relevance"] = ["mapped from explicit RADAR rule score"] if radar_relevance else ["no explicit RADAR relevance rule matched"]

    novelty = {"new": 1.0, "changed": 0.75, "same": 0.05}.get(change, 0.25)
    reasons["novelty"] = [f"RADAR change={change}"]

    reliability = 0.85 if source in PRIMARY_SOURCES else 0.35
    reasons["reliability"] = [f"known primary/public source: {source}"] if source in PRIMARY_SOURCES else ["source class not established by VALUE"]

    consequence = 0.15
    if "earthquake" in tags:
        mag = data.get("magnitude")
        if isinstance(mag, (int, float)):
            consequence = clamp((float(mag) - 4.0) / 4.0)
            reasons["consequence"] = [f"earthquake magnitude={mag}; bounded heuristic, not impact estimate"]
        else:
            reasons["consequence"] = ["earthquake magnitude unavailable"]
    elif source == "CISA KEV":
        consequence = 0.75
        reasons["consequence"] = ["CISA catalog states exploitation in the wild; local applicability not inferred"]
    else:
        reasons["consequence"] = ["no domain consequence adapter; conservative default"]

    actionability = 0.10
    time_advantage = 0.15
    if source == "Grants.gov":
        close = data.get("closeDate")
        days = None
        if close:
            for fmt in ("%m/%d/%Y", "%Y-%m-%d"):
                try:
                    days = (dt.datetime.strptime(close, fmt).date() - now.date()).days
                    break
                except ValueError:
                    pass
        if days is not None and days >= 0:
            actionability = 0.35
            time_advantage = 0.9 if days <= 7 else (0.65 if days <= 30 else 0.35)
            reasons["actionability"] = ["public opportunity has a future close date; eligibility not inferred"]
            reasons["time_advantage"] = [f"{days} days until listed close date"]
        else:
            reasons["actionability"] = ["eligibility/action unknown"]
            reasons["time_advantage"] = ["usable close-date window unavailable"]
    elif source == "CISA KEV":
        due = data.get("dueDate")
        days = None
        if due:
            try:
                days = (dt.datetime.strptime(due, "%Y-%m-%d").date() - now.date()).days
            except ValueError:
                pass
        actionability = 0.30
        time_advantage = 0.85 if days is not None and 0 <= days <= 7 else (0.60 if days is not None and days <= 30 else 0.35)
        reasons["actionability"] = ["CISA publishes required remediation action; asset applicability not inferred"]
        reasons["time_advantage"] = [f"{days} days until CISA due date"] if days is not None else ["CISA due-date window unavailable"]
    else:
        reasons["actionability"] = ["no lawful user action inferred from observation alone"]
        reasons["time_advantage"] = ["no domain-specific decision window established"]

    uncertainty = 0.10 if source in PRIMARY_SOURCES else 0.50
    noise = 0.10
    duplication = 0.75 if change == "same" else 0.0
    manipulation_risk = 0.05 if source in PRIMARY_SOURCES else 0.40

    candidate = Candidate(
        id=f"{source}:{observation.get('id')}",
        relevance=relevance,
        consequence=consequence,
        actionability=actionability,
        novelty=novelty,
        reliability=reliability,
        time_advantage=time_advantage,
        uncertainty=uncertainty,
        noise=noise,
        duplication=duplication,
        manipulation_risk=manipulation_risk,
    )
    return candidate, reasons


def build(snapshot, threshold=45.0, now=None):
    observations = snapshot.get("observations", [])
    derived = []
    reason_map = {}
    source_map = {}
    for observation in observations:
        candidate, reasons = derive(observation, now=now)
        derived.append(candidate)
        reason_map[candidate.id] = reasons
        source_map[candidate.id] = {
            "source": observation.get("source"),
            "source_id": observation.get("id"),
            "title": observation.get("title"),
            "url": observation.get("url"),
            "observed_at": observation.get("observed_at"),
            "retrieved_at": observation.get("retrieved_at"),
            "radar_change": observation.get("change"),
        }

    queue = rank(derived, threshold=threshold)
    for item in queue["items"]:
        item["observation"] = source_map[item["id"]]
        item["derivation_reasons"] = reason_map[item["id"]]
    queue["input_schema"] = snapshot.get("schema")
    queue["input_generated_at"] = snapshot.get("generated_at")
    queue["semantics"] = "machine-derived attention queue; human verification required"
    return queue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="radar/data/latest.json")
    parser.add_argument("--output", default="value/data/latest.json")
    parser.add_argument("--threshold", type=float, default=45.0)
    args = parser.parse_args()
    snapshot = json.loads(Path(args.input).read_text())
    result = build(snapshot, threshold=args.threshold)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
