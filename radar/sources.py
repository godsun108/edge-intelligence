"""Authoritative public RADAR source adapters."""
import datetime as dt

CISA_KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def normalize_cisa_kev(payload, retrieved_at, limit=100):
    rows = payload.get("vulnerabilities", [])
    out = []
    for v in rows[:limit]:
        cve = v.get("cveID")
        if not cve:
            continue
        vendor = v.get("vendorProject") or ""
        product = v.get("product") or ""
        name = v.get("vulnerabilityName") or f"{cve} known exploited vulnerability"
        out.append({
            "id": cve,
            "source": "CISA KEV",
            "title": f"{cve} — {name}",
            "url": f"https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext={cve}",
            "observed_at": v.get("dateAdded"),
            "retrieved_at": retrieved_at,
            "tags": ["cybersecurity", "known exploited vulnerability", vendor, product],
            "data": {
                "cve": cve,
                "vendor": vendor,
                "product": product,
                "dateAdded": v.get("dateAdded"),
                "dueDate": v.get("dueDate"),
                "knownRansomwareCampaignUse": v.get("knownRansomwareCampaignUse"),
                "requiredAction": v.get("requiredAction"),
            },
        })
    return out
