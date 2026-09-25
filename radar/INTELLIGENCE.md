# Opportunity Intelligence

EDGE enriches grant observations after ingestion rather than confusing source facts with EDGE interpretation.

For Grants.gov items it derives:
- agency and opportunity number
- closing date and days remaining when parseable
- urgency: OPEN (>30 days), SOON (8–30), URGENT (0–7), CLOSED, or UNKNOWN
- relevance reasons such as matched interest terms and deadline proximity

Urgency boosts attention priority; it does not assert eligibility, quality, award probability, or recommend applying. Those require reading the full opportunity and making a human decision.

The UI exposes **WHY** so a relevance score is inspectable rather than mysterious.
