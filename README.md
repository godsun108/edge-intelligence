# EDGE

**Know what matters.**

EDGE is a private intelligence-console architecture for turning changing information into a short, provenance-aware queue for human judgment.

## Modules
- RADAR — discovery, monitoring, rules, change detection
- SAVANT — evidence-oriented research
- LEDGER / ASSETS — resources and obligations
- TIME MACHINE / MEMORY — deliberate searchable history
- SENSE — physical-world and phone capability layer

## Principle
**EDGE does not decide for you. It makes sure you do not decide blind.**

V0.1 is intentionally static and local-first. No sensitive information belongs in this public repository. Future source adapters should normalize observations, preserve provenance and timestamps, deduplicate previously seen items, evaluate explicit user rules, and surface meaningful changes.

## v1.0
EDGE v1.0 establishes the operational loop: official/public sources → normalized observations → persistent source memory → change detection → explicit relevance rules → inspectable reasons → opportunity intelligence → local-first human triage → Morning Brief.

The browser caches the last successful briefing so a temporary feed failure does not erase the user's working context. Source truth and human decisions remain separate.


## v1.2 — Integrated local intelligence loop

EDGE v1.2 consolidates RADAR, SENSE and TIME MACHINE into coherent operational surfaces.

- RADAR: feed ingestion, cached fallback, relevance briefing and human triage.
- SENSE: explicit/heuristic capture, local persistence, import/export and deliberate promotion.
- TIME MACHINE: search, age-based resurfacing, related retrieval, threads, factual compare, retrieval map, activity pulse and 7-day review queue.
- Safety/trust: user text is HTML-escaped before rendering; machine-derived relationships are labeled; capture is not commitment; age is not importance; similarity is not truth.
- ASK EDGE currently behaves as deliberate local capture, not a fake conversational intelligence layer.

The current deployment is intentionally local-first. Cross-device sync, native iOS sensors, authenticated private storage, semantic embeddings and additional data adapters remain future work and must not be implied by the web prototype.


## v1.3 — SAVANT begins
SAVANT v0.1 adds a local-first evidence map: claims/questions plus explicitly labeled SUPPORTS, CONTRADICTS and CONTEXT records. It intentionally has no truth score or automatic verdict.

SAVANT v0.2 adds PRIMARY/SECONDARY/UNKNOWN source classification and explicit unresolved research questions while preserving the no-auto-verdict boundary.

SAVANT v0.3 adds reconstructable provenance records: title, publisher/author, publication date, retrieval timestamp, excerpt, URL/citation note and research context.

SAVANT v0.4 adds descriptive evidence-state analysis so missing primary evidence, recorded contradictions, unknown source classes and unresolved questions are visible without generating a truth/confidence score.

SAVANT v0.5 adds an extractive evidence brief that reorganizes recorded SUPPORTS, CONTRADICTS, CONTEXT and unresolved questions without generating a verdict or claiming completeness.

SAVANT v0.6 adds the first machine-assisted research bridge: RADAR emits provenance-preserving research candidates from relevant changed public-source observations. Candidates remain CONTEXT/CANDIDATE_ONLY until deliberately reviewed; automation does not silently convert observations into conclusions.

SAVANT v0.7 adds the human review gate: RADAR candidates appear in a research inbox and can be deliberately imported as CONTEXT with their provenance and machine-attention reasons preserved. Automatic SUPPORTS/CONTRADICTS promotion remains prohibited.

SAVANT v0.8 adds explicit research portability: human-readable JSON export/import preserves claims, evidence provenance, unresolved questions and RADAR-origin metadata, with schema validation and claim-ID deduplication.

SAVANT v0.9 adds per-claim research history for claim creation, evidence attachment, questions and RADAR imports. The event view is an audit aid, explicitly not a cryptographic/tamper-proof log.

SAVANT v1.0 hash-chains new research-history events with browser SHA-256 and verifies chain continuity locally. This is tamper-evident, not tamper-proof or externally timestamped; legacy unsigned events are surfaced rather than silently trusted.

SAVANT v1.1 adds portable integrity checkpoints for verified research histories. A checkpoint preserves claim identity, event count and chain-tip hash and can be exported independently; it is not a signature, notarization or external timestamp.

SAVANT v1.2 adds independent checkpoint-file verification and, when the matching claim exists locally, comparison of the exported chain tip with local research history. Self-hash verification still does not prove authorship or trusted time.


## EDGE v2.5 — CAPITAL + Quantum Intelligence
CAPITAL v0.1 adds a local-first lawful liquidity ledger that strictly separates pipeline capital from user-confirmed available cash. EDGE also establishes a quantum-intelligence contract: quantum simulation, quantum-inspired, hybrid and real-hardware methods must be labeled accurately and benchmarked against classical baselines; no mystical certainty or guaranteed financial advantage claims.
