# Genesis ONE — exact-median noise-consensus shadow evaluation

Status: negative result; **do not promote**. Frozen v35 unchanged. Both suites reuse the synthetic generator and have been inspected during development; not sealed holdouts.

Verified CI: [original replay 39495335938](https://github.com/godsun108/edge-intelligence/actions/runs/39495335938), artifact `genesis-task-replay`; [distinct-seed 39495335936](https://github.com/godsun108/edge-intelligence/actions/runs/39495335936), artifact `genesis-distinct-seed-evidence`; commit `da1f43b08c44d1735b934b863672ba030ae12357`.

| Suite | Policy | Correct accepted | Wrong accepted | Accepted total |
|---|---|---:|---:|---:|
| Original 4,000 tasks | v35 | 2141 | 4 | 2145 |
| Original 4,000 tasks | Exact median residual zero | 1699 | 0 | 1699 |
| Distinct-seed 4,000 tasks | v35 | 2152 | 2 | 2154 |
| Distinct-seed 4,000 tasks | Exact median residual zero | 1699 | 0 | 1699 |
| Combined 8,000 tasks | v35 | 4293 | 6 | 4299 |
| Combined 8,000 tasks | Exact median residual zero | 3398 | 0 | 3398 |

The filter vetoed all 6 wrong accepted decisions but also vetoed **895 correct accepted decisions** (442 original + 453 distinct). It is too aggressive to justify promotion. Exact median zero is a brittle equality test under noisy synthetic observations; no inference changes were made.

Next: evaluate a graded robust residual/margin score on **fresh development seeds**, reporting correct-acceptance coverage, wrong accepts, and observation cost. Pre-register independent evaluation before claiming generalization; do not optimize solely against the two exposed suites.
