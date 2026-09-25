# SAVANT Source Semantics

SAVANT v0.2 adds two research primitives.

## Source class
Evidence may be labeled **PRIMARY**, **SECONDARY**, or **UNKNOWN**. This is user-supplied metadata. PRIMARY does not mean correct; SECONDARY does not mean weak. The label describes the source's relationship to the underlying event or claim, not its reliability.

## Unresolved questions
Each claim can carry open research questions. They are preserved separately from evidence so absence of evidence is not silently converted into an answer.

SAVANT still performs no automatic truth scoring or source-quality ranking. A future retrieval layer may help populate metadata, quotations, dates, and provenance, but should preserve source text and clearly distinguish extracted facts from machine analysis.
