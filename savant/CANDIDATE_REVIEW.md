# SAVANT Candidate Review v0.7

The browser now consumes `radar/data/savant_candidates.json` and presents unreviewed RADAR observations in a **RESEARCH CANDIDATES** inbox.

A candidate changes SAVANT only when the user selects **IMPORT AS CONTEXT**.

Import creates:
- a new local claim seeded from the observed title;
- one CONTEXT evidence record;
- the original URL/title/publisher;
- observed and retrieval timestamps;
- source class supplied by the bridge;
- RADAR relevance reasons;
- an origin record containing candidate ID, change state and relevance.

Imported candidate IDs are retained on the claim so the same candidate is not offered repeatedly in that browser.

## Boundary

Import does not mean the proposition is true. It means the user chose to preserve the public observation as research context. Automated promotion to SUPPORTS or CONTRADICTS is intentionally not implemented.
