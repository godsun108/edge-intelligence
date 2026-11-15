# Genesis ONE — shadow-policy experiment results

Status: diagnostic, **not** a promoted inference change. Two deterministic, reused synthetic-generator seed suites; not an independent holdout.

## Verified CI evidence

- Original frozen suite: [run 39492685630](https://github.com/godsun108/edge-intelligence/actions/runs/39492685630), artifact `genesis-task-replay`, seed 31071, count 200, seedCount 4.
- Distinct-seed suite: [run 39492685620](https://github.com/godsun108/edge-intelligence/actions/runs/39492685620), artifact `genesis-distinct-seed-evidence`, seed 900001, count 200, seedCount 4.
- Both completed successfully on commit `d339bfda049e6b14f2aaa309ad62ba9eedc4dc53`.

| Policy | Original correct | Original wrong | Distinct correct | Distinct wrong | Combined correct | Combined wrong |
|---|---:|---:|---:|---:|---:|---:|
| Frozen v35 | 2141 | 4 | 2152 | 2 | 4293 | 6 |
| Candidate stable with final-stage answer | 2135 | 4 | 2143 | 1 | 4278 | 5 |
| Final-stage >=4 observations | 2091 | 4 | 2110 | 1 | 4201 | 5 |
| Both filters | 2089 | 4 | 2107 | 1 | 4196 | 5 |

The stability filter prevents one wrong acceptance but rejects 15 correct accepts relative to v35; >=4 observations rejects 92 correct accepts for the same one prevented error; both rejects 97 correct accepts. No tested filter fixes the four original-seed wrong accepts. Do not promote any of these filters based on this evidence.

**Interpretation limits:** Shadow filtering can only veto existing v35 accepted decisions, not recover mistakes or evaluate a changed search strategy. The suites use the same generator and have been inspected during development. These are diagnostics, not sealed holdout evidence or production performance claims.

## Next experiment

Investigate whether selected probes are discriminative against the nearest competing hypothesis and whether noise-aware ambiguity scoring can improve the error/coverage frontier. Use a separate candidate implementation and fresh development seeds, preserve v35 unchanged, and pre-register an untouched final evaluation before any promotion.
