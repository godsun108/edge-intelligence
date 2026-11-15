# Genesis ONE — uncertainty abstention results

**Development-only result; no policy promotion.** Frozen v35 source unchanged.

Source: [successful GitHub Actions run 39519931475](https://github.com/godsun108/edge-intelligence/actions/runs/39519931475). Preregistered settings: `seed=2500001 count=200 seedCount=4`, 4,000 synthetic tasks, 0 replay mismatches, 27,076 measurement requests. Margin rules are shadow-only abstention filters on existing observations.

| Policy | Correct accepts | Wrong accepts | Total accepts | Wrong prevented | Correct rejected |
|---|---:|---:|---:|---:|---:|
| Frozen v35 | 2173 | 3 | 2176 | 0 | 0 |
| Discrete-noise lead >=2 | 2173 | 2 | 2175 | 1 | 0 |
| Discrete-noise lead >=4 | 2145 | 1 | 2146 | 2 | 28 |

Margin >=2 is a promising observation on this particular development suite: one wrong acceptance vetoed at zero observed correct-accept cost. The stricter margin >=4 has a measurable coverage penalty. These are *not* independent holdout results, statistical guarantees, calibrated probabilities, or proof of real-world reliability. The same synthetic generator was used in earlier experiments; candidate policies must be tested across multiple predeclared fresh suites and noise regimes before any promotion discussion. No extra requests were made by the shadow filters.

Next: verify margin >=2 on predeclared additional synthetic development seeds, report per-scenario differences and inspect all wrong accepts, including those the filter retains. Keep v35 frozen and explicitly label any tuning as development work.
