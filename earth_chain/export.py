"""Generate a safe, versioned Earth Chain handoff for MINT and Command Center.
Run from repository root: python earth_chain/export.py
"""
import json
from pathlib import Path
from datetime import datetime, timezone
from engine import report, validate
ROOT=Path(__file__).resolve().parent
def build(rows):
    summary=report(rows)
    valid,_=validate(rows)
    # Only actionable candidates with explicit counterparty consent; no assumed economics.
    opportunities=[{"external_id":"earth-chain:"+str(x["id"]),"source_system":"earth-chain",
        "commodity":x["commodity"],"region":x["region"],"quote_kind":x["kind"],
        "status":"discovered_unreviewed","expected_cash_usd":0,"settled_cash_usd":0,
        "requires_human_review":True,"evidence_url":x["evidence_url"]}
        for x in valid if x["kind"] in ("ask","bid") and x.get("counterparty_contact_consent") is True]
    telemetry={"schema":"earth-chain.telemetry.v0.1","generated_at":datetime.now(timezone.utc).isoformat(),
        "status":"LOCAL_ONLY","observations":summary["observations"],"rejected_count":len(summary["rejected"]),
        "opportunity_candidates":len(opportunities),"prices_published":False,
        "source_digest_sha256":summary["digest_sha256"],
        "note":"Generated locally; not evidence of deployed connectivity or verified market liquidity."}
    return summary,opportunities,telemetry
def main():
    rows=json.loads((ROOT/"observations.json").read_text())
    if not isinstance(rows,list): raise ValueError("Expected JSON array")
    summary,opportunities,telemetry=build(rows)
    out=ROOT/"outputs";out.mkdir(exist_ok=True)
    for name,data in (("market_report.json",summary),("mint_candidates.json",{"schema":"earth-chain.mint.v0.1","items":opportunities}),("command_telemetry.json",telemetry)):
        (out/name).write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({"observations":summary["observations"],"candidates":len(opportunities),"rejected":len(summary["rejected"])}))
if __name__=="__main__": main()
