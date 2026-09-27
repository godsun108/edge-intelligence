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

NVD_CVE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=100"


def _english_description(cve):
    for d in cve.get("descriptions", []):
        if d.get("lang") == "en":
            return d.get("value") or ""
    return ""


def _cvss(cve):
    metrics = cve.get("metrics") or {}
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        rows = metrics.get(key) or []
        if rows:
            data = rows[0].get("cvssData") or {}
            return {"version": data.get("version"), "baseScore": data.get("baseScore"), "baseSeverity": data.get("baseSeverity") or rows[0].get("baseSeverity")}
    return {}


def normalize_nvd(payload, retrieved_at, limit=100):
    out=[]
    for wrapper in (payload.get("vulnerabilities") or [])[:limit]:
        cve=wrapper.get("cve") or {}
        cid=cve.get("id")
        if not cid:
            continue
        desc=_english_description(cve)
        out.append({
            "id":cid,
            "source":"NIST NVD",
            "title":f"{cid} — {desc[:180]}" if desc else cid,
            "url":f"https://nvd.nist.gov/vuln/detail/{cid}",
            "observed_at":cve.get("published"),
            "retrieved_at":retrieved_at,
            "tags":["cybersecurity","cve","nvd"],
            "data":{
                "cve":cid,
                "published":cve.get("published"),
                "lastModified":cve.get("lastModified"),
                "vulnStatus":cve.get("vulnStatus"),
                "cvss":_cvss(cve),
            },
        })
    return out

FEDERAL_REGISTER_URL = "https://www.federalregister.gov/api/v1/documents.json?per_page=100&order=newest"


def normalize_federal_register(payload, retrieved_at, limit=100):
    out=[]
    for d in (payload.get("results") or [])[:limit]:
        number=d.get("document_number")
        title=d.get("title")
        if not number or not title:
            continue
        agencies=[a.get("name") for a in (d.get("agencies") or []) if a.get("name")]
        out.append({
            "id":number,
            "source":"Federal Register",
            "title":title,
            "url":d.get("html_url") or d.get("pdf_url") or "",
            "observed_at":d.get("publication_date"),
            "retrieved_at":retrieved_at,
            "tags":["regulation","public policy",*(agencies[:4])],
            "data":{
                "document_number":number,
                "type":d.get("type"),
                "publication_date":d.get("publication_date"),
                "agencies":agencies,
                "abstract":d.get("abstract"),
            },
        })
    return out
