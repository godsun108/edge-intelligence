# SAVANT Research History v0.9

New and modified SAVANT claims now maintain a local event history.

Recorded event types currently include:
- CLAIM_CREATED
- EVIDENCE_ATTACHED
- QUESTION_ADDED
- RADAR_CANDIDATE_IMPORTED

Each event has an EDGE-generated timestamp and a compact factual detail. The selected claim displays events newest-first.

## Semantics

The history is an audit aid, not a cryptographic audit log. Browser localStorage can be edited or cleared, imports can contain pre-existing records, and the current implementation does not hash-chain or digitally sign events.

For legacy claims without a history array, the UI derives a clearly labeled legacy creation event from the existing claim timestamp rather than pretending earlier events were captured.

A future private backend can make this tamper-evident and synchronize it across authorized devices.
