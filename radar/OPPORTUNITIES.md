# Opportunity Radar

EDGE's first opportunity watcher uses the official Grants.gov public search API. It ingests posted/forecasted opportunities, preserves agency, opportunity number, dates and source identity, then passes observations through the same memory/change/relevance pipeline.

Planned official-source adapters: SAM.gov contract opportunities (requires an API key for the documented API), public surplus/auction sources where a stable machine-readable interface is available, and selected official open-data catalogs.

No credentials belong in this public repository. API-key sources must use repository/environment secrets in deployment.

## v0.5 hardening
The Grants.gov adapter now maps the documented search2 response fields (including agencyName), and its keyword can be configured without changing ingestion code. The default remains broad so the relevance layer—not the source adapter—controls what reaches the briefing.
