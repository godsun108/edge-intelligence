# Genesis ONE — probe-level error evidence (seed 907920)

Source: GitHub Actions run `39490419523`, uploaded `genesis-distinct-seed-evidence` JSON; frozen v35 source SHA256 `d63c1b8e4fc0666165064c046519eccd4702fed22ab9daeb46da7901289dfb6a`. These are observed failures on reused synthetic scenarios, not independently generated holdout tasks.

## combined_stress, task 99

- Truth: `L:2:4` (2x+4); final accepted: `L:2:5` (2x+5).
- Initial nonmissing observations: (-3,-1), (5,14). The frozen initial stage reports `L:2:4` (loss 0.5) at all five stages; all four followups are missing.
- Selected probes: x=8 observed y=21, x=7 missing, x=-8 observed y=-11. Both nonmissing selected probes exactly fit the **wrong** candidate `L:2:5`; the true candidate predicts 20 and -12. Another available, unselected probe at x=3 has y=10, which exactly fits the true candidate.
- The accepted answer changed relative to the initial stage; this supports investigating noisy probe-driven re-ranking and candidate stability.

## unseen_K_test_only, task 75

- Truth: `U:-1` (x^4-1); accepted: `U:-2` (x^4-2).
- Initial nonmissing observations: (-6,1294), (-3,80), (-1,0), (0,-2), (2,14). The initial stage already proposes `U:-2` (loss 0.4). Followup (-7,2399) preserves the proposed answer.
- Selected probes: (-8,4094) and (-2,14), both exactly fitting the wrong `U:-2`; true formula predicts 4095 and 15. Available unselected probe at x=3 has y=79, which fits the true `U:-1`.
- This supports investigating near-neighbor ambiguity and the risk of validating a wrong candidate with noisy agreeing probes.

## Boundaries and next test

The examples do not establish that a different gate would improve aggregate outcomes. Before altering inference, run a **separate experimental policy** that records candidate stability, competitor margins, and selected-versus-unselected probe evidence, then compare incorrect accepts, correct accepts, abstentions, and computational cost across both frozen evaluations and fresh development seeds. Never tune on the frozen evaluations and call them independent holdouts.
