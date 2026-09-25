# SAVANT Portability v0.8

SAVANT research can now be exported from the browser as human-readable JSON using schema `edge.savant.export.v1`.

The export preserves the local claim collection, including:
- claims and creation timestamps
- evidence and provenance fields
- evidence stance and source class
- unresolved questions
- RADAR candidate origin/import identifiers where present

A compatible export can be imported later. Import validates the top-level schema, requires claim IDs and text, normalizes missing evidence/question arrays, and deduplicates by claim ID.

## Limits

This is explicit file portability, not cloud synchronization, backup guarantees, encryption, account identity, or conflict-free multi-device merging. The browser remains the active local store. Users should treat exported files according to the sensitivity of the research they contain.
