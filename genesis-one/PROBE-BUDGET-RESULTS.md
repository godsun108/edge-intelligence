# Genesis ONE — budgeted additional probe development results

**Decision: no promotion.** Frozen v35 source unchanged. This was a counterfactual probe-acquisition experiment over pre-generated synthetic observations, not a live measurement service.

Source: [GitHub Actions run 39517570787](https://github.com/godsun108/edge-intelligence/actions/runs/39517570787), branch `genesis-v36-audit-infrastructure`, commit `2ba0a3db7a5d4ca438797e9597cdd2a816475555`. Parameters `seed=2100001 count=200 seedCount=4`, 4,000 tasks. CI success verifies execution and accounting assertions, not model improvement.

| Metric | Frozen v35 | Budgeted extra-probe policy |
|---|---:|---:|
| Correct accepted | 2140 | 2140 |
| Wrong accepted | 2 | 2 |
| Total accepted | 2142 | 2142 |
| Requests | 27091 | 27310 |

- Eligible accepted tasks: **73**.
- Additional requests: **219** (3 per eligible task).
- Additional nonmissing observations: **142**.
- Decisions vetoed: **0**; wrong accepts prevented: **0**; correct accepts rejected: **0**.
- Request increase: **219 / 27091 = 0.808%**.

## Interpretation and limitations

The acquisition policy requests up to three unselected, pre-generated probes only for sparse-evidence accepts with a candidate offset competitor. It does not peek at unrequested probe values before choosing the extra probes. The counterfactual decision ranks candidates by absolute-error sum on augmented observations and **only vetoes** the original accepted decision when a different candidate ranks first; it does not revise or correct the prediction. Therefore zero changed decisions does not prove that extra evidence cannot help a different inference policy. The selection rule and reranking method may be inadequate, and the two wrong accepts might not even have been eligible. This remains a synthetic development test, not an independent holdout.

Next: instrument per-error eligibility and extra-probe outcomes, and design an independent noise-aware inference policy with an explicit request budget. Avoid repeating additional requests without evidence of decision benefit.
