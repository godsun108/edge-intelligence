# SAVANT Tamper-Evident History v1.0

New SAVANT research-history events are now SHA-256 hash chained in the browser using Web Crypto.

Each event records:
- timestamp
- event type
- factual detail
- previous event hash
- its own SHA-256 hash

The selected claim verifies its local chain before displaying a VERIFIED LOCAL CHAIN indicator. A broken previous-hash link, changed event payload, or unsigned legacy event is surfaced as a check failure.

## Security boundary

This is **tamper-evident**, not tamper-proof and not an external timestamp authority.

Because both the data and verifier live in the user's browser, a sufficiently capable party who can rewrite the whole local record can recompute the chain. The chain is useful for detecting accidental edits, partial manipulation, corruption, and broken history continuity. Stronger assurance would require signed checkpoints or hashes anchored outside the mutable local store.

Legacy history entries created before v1.0 are not silently blessed; they appear as unsigned legacy events until a future explicit migration strategy is implemented.
