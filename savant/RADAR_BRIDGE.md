# RADAR → SAVANT Candidate Bridge

RADAR can now emit `radar/data/savant_candidates.json`.

This file contains **research candidates**, not evidence automatically accepted into SAVANT.

For each relevant changed observation, the bridge preserves:
- RADAR/source identity
- source URL and source title
- publisher/source system
- observed and retrieval timestamps
- relevance and explicit match reasons
- RADAR change state
- a conservative source-class label for the official public feeds currently wired
- `stance: CONTEXT`
- `import_semantics: CANDIDATE_ONLY`

## Trust boundary

A RADAR observation is not automatically a verified claim, and a candidate is not automatically evidence for or against a user claim. The bridge deliberately defaults to CONTEXT and requires a later deliberate import/review step before local SAVANT evidence is changed.

This prevents automation from silently turning “the system observed a public record” into “the system concluded the proposition is true.”
