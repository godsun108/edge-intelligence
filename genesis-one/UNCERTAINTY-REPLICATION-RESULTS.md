# Genesis ONE — uncertainty replication results

**Green CI does not mean policy promotion.** Frozen v35 unchanged. Source: [GitHub Actions run 39520297772](https://github.com/godsun108/edge-intelligence/actions/runs/39520297772), successful. Three preregistered synthetic development suites, each 4,000 tasks, no replay mismatches. Same task generator as previous experiments, not independent holdout.

| Seed | v35 correct | v35 wrong | Gap2 correct | Gap2 wrong | Gap4 correct | Gap4 wrong | Requests |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2900001 | 2129 | 3 | 2129 | 2 | 2108 | 1 | 27096 |
| 3300001 | 2139 | 3 | 2139 | 3 | 2108 | 2 | 27195 |
| 3700001 | 2123 | 6 | 2122 | 5 | 2097 | 2 | 27084 |
| **Total** | **6391** | **12** | **6390** | **10** | **6313** | **5** | **81375** |

Margin >=2: **2 wrong accepts prevented, 1 correct accept rejected** across 12,000 tasks. Margin >=4: **7 wrong accepts prevented, 78 correct accepts rejected**. No extra measurement requests; these are shadow-only abstention filters. Seed 3300001 had no improvement from margin >=2; seed 3700001 had a correct-accept cost.

Including earlier 4,000-task development suite seed 2500001: baseline 8564 correct/15 wrong, margin >=2 8563 correct/12 wrong, margin >=4 8458 correct/6 wrong across 16,000 tasks. These pooled counts are descriptive only, not an independent holdout or proof of generalization.

**Decision:** retain margin >=2 as an experimental candidate only. No change to frozen v35 or production status. Further work should inspect per-scenario performance and develop truly independent holdout regimes before considering promotion.
