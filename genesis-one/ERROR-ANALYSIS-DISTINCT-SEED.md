# Genesis ONE — distinct-seed accepted-error investigation

Evidence: GitHub Actions run 39489317960, artifact `genesis-distinct-seed-evidence` (4,000 tasks; seed=900001, count=200, seedCount=4). Frozen source SHA256: `d63c1b8e4fc0666165064c046519eccd4702fed22ab9daeb46da7901289dfb6a`.

## Observed wrong accepted decisions

1. Seed 907920; scenario `combined_stress`; task 99; expected `L:2:4`; accepted `L:2:5`; stage 4; 2 observed probes, 0 bad probes; chosenXs `[8,7,-8]`; requested 7; comparisons 678.
2. Seed 907920; scenario `unseen_K_test_only`; task 75; expected `U:-1`; accepted `U:-2`; stage 4; 2 observed probes, 0 bad probes; chosenXs `[-8,-2]`; requested 6; comparisons 1326.

## Hypothesis (not established)

The stage-4 acceptance gate may permit acceptance with only two observed probes when nearby candidates are not distinguishable. This is not proof that raising `minObs` or changing the gate improves generalization; those changes could increase abstention or introduce new failures.

## Next experiments

- Inspect candidate ambiguity and evidence state for both tasks without modifying frozen v35.
- Evaluate any proposed gate change on separate training/development seeds and a fresh preregistered test distribution; report acceptance coverage and wrong-acceptance count together.
- Keep existing v35 regression and distinct-seed baselines immutable for comparison.

**Interpretation boundary:** The two observed errors were obtained from a reused synthetic generator, not independent real-world validation.
