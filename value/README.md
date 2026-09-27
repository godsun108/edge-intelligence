# EDGE // VALUE v0.1

**Mission: find what matters before it becomes obvious.**

VALUE ranks candidate information by expected decision value before that value decays. It is an attention-allocation layer, not a truth engine, recommendation engine, trading signal, or claim that an item is objectively important.

Pipeline:

```
RADAR observation/change
        ↓
SAVANT evidence/provenance context
        ↓
VALUE inspectable factors + penalties
        ↓
short ranked attention queue or NO_SIGNAL
        ↓
human judgment
        ↓
later outcome/calibration record
```

## Core score

Each input factor is explicit and bounded to 0–1:

- relevance — connection to a declared objective or decision
- consequence — magnitude if the information is materially true
- actionability — whether a lawful, realistic action exists
- novelty — how much this changes the prior information state
- reliability — provenance/evidence quality, not metaphysical truth
- time_advantage — value of learning it now rather than later

Penalties are also 0–1:

- uncertainty
- noise
- duplication
- manipulation_risk

v0.1 uses a transparent weighted arithmetic score. The weights are provisional and must be changed only through versioned code/tests, never silently tuned to make past examples look better.

`value_score = 100 × positive_signal × penalty_multiplier`

The score is an **attention priority**, not probability, truth, expected profit, moral importance, or instruction to act.

## NO_SIGNAL is success

VALUE must be allowed to say that nothing currently clears the attention threshold. It must not manufacture significance to keep a feed busy.

## Anti-hype rules

1. Popularity and engagement are not value inputs.
2. Repetition does not create evidence and is penalized as duplication.
3. Urgency alone cannot create a high score.
4. Low reliability cannot be rescued by high consequence.
5. Every surfaced score must expose its factors and penalties.
6. Human decisions remain separate from machine prioritization.
7. Sensitive personal objectives do not belong in this public repository.
8. Financial, medical, legal, political, or safety-sensitive items require domain-appropriate verification before consequential action.
9. VALUE may prioritize political/public-policy information descriptively, but must not rank candidates, parties, voting choices, or persuasion targets.
10. Outcomes must be appended later; prior scores are never rewritten to flatter performance.

## Calibration path

v0.1 establishes deterministic scoring and invariants. Future versions may preserve:
- surfaced_at
- decision_window
- whether a human inspected it
- whether it changed a decision
- later observed consequence
- whether the information arrived before broad dissemination
- score/version/factor snapshot

Those records can test whether VALUE actually improves attention allocation. Until then, VALUE is a hypothesis expressed as inspectable software.


## v0.2 — eyes, corroboration, calibration

v0.2 adds the first authoritative source expansion through CISA's Known Exploited Vulnerabilities catalog, explicit-identifier corroboration, append-only outcome/calibration primitives, source-baseline semantics and a hard attention budget.

A newly introduced source is a **baseline**, not a burst of new events. Only subsequent records or changed fingerprints may claim RADAR novelty. VALUE treats baseline records as non-novel and duplicate-like for attention purposes.

The attention queue surfaces at most 10 items by default. Additional above-threshold candidates are counted as suppressed rather than turning VALUE into a firehose.

Corroboration v0.1 links only literal stable identifiers (currently CVE IDs) and counts independent sources. It does not infer semantic equivalence and does not yet boost VALUE scores.

Outcome records preserve the original score and VALUE version. Calibration is descriptive and does not prove that a surfaced item caused a better decision.
