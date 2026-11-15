# Genesis ONE — graded residual development evaluation

**Decision: no promotion.** Frozen v35 remains unchanged.

Source: [GitHub Actions run 39496298065](https://github.com/godsun108/edge-intelligence/actions/runs/39496298065), commit `a0ca8bd66308186994d86ac4b4d0fcb16946c32a`, artifact `genesis-graded-noise-development`. Parameters `seed=1300001 count=200 seedCount=4`, five scenarios × four seeds × 200 = 4,000 synthetic tasks. CI assertions passed, zero v29/v30/v35 behavioral mismatches.

| Shadow acceptance policy | Correct accepted | Wrong accepted | Total accepted | Abstained | Correct rejected vs v35 | Wrong prevented vs v35 |
|---|---:|---:|---:|---:|---:|---:|
| Frozen v35 | 2201 | 4 | 2205 | 1795 | 0 | 0 |
| Median residual exactly zero | 2185 | 4 | 2189 | 1811 | 16 | 0 |
| Absolute median residual <= 0.5 | 2193 | 4 | 2197 | 1803 | 8 | 0 |
| Absolute median residual <= 1 | 2201 | 4 | 2205 | 1795 | 0 | 0 |

All candidate filters fail to prevent any incorrect accepts on these seeds; the stricter two reduce coverage. The apparent difference between this run and prior inspected suites reinforces the risk of tuning on exposed failures. These are *development* results on the same synthetic generator, not independent validation.

Next: instrument all wrong accepted decisions for error taxonomy; consider a separate generative noise-likelihood model and alternative inference candidate on development seeds. Pre-register genuinely independent evaluation cases before claiming generalization. Preserve baseline and costs.
