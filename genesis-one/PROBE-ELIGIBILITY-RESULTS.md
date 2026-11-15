# Genesis ONE — probe-budget eligibility diagnosis

**Decision: no promotion.** Frozen v35 remains unchanged. This is a post-hoc diagnosis of an exposed synthetic development suite, not independent validation.

Verified [GitHub Actions run 39518350105](https://github.com/godsun108/edge-intelligence/actions/runs/39518350105), commit `d3794ec6a6b21a19dbd2ff6f78b2c1e32519452a`. Settings: `seed=2100001 count=200 seedCount=4`; 4,000 tasks; successful CI accounting assertions.

| Metric | Result |
|---|---:|
| Frozen v35 correct accepts | 2140 |
| Frozen v35 wrong accepts | 2 |
| Total probe-eligible accepts | 73 |
| Eligible correct accepts | 72 |
| Eligible wrong accepts | 1 |
| Ineligible wrong accepts | 1 |
| Additional probe requests | 219 |
| Additional nonmissing measurements | 142 |
| Wrong accepts vetoed | 0 |
| Correct accepts vetoed | 0 |
| Changed decisions | 0 |

**Interpretation:** One wrong accepted task was excluded by the acquisition trigger; the other qualified but the augmented-evidence ranking did not veto it. This separates a **trigger coverage** failure from an **evidence interpretation** failure. The eligible wrong task's exact observations and candidate ranking are not yet reported by these aggregate counters, so do not claim why the reranker retained it. These additional observations are pre-generated counterfactual data; their request costs are explicitly counted.

Next: instrument each wrong acceptance with trigger conditions, extra-probe outcomes, original and augmented candidate scores, and veto decision. Only then evaluate a revised acquisition/inference policy. Preserve the v35 baseline and account for all extra requests.
