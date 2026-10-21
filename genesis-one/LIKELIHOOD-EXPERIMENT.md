# Genesis ONE — discrete-noise likelihood shadow experiment

**Status:** development-only diagnostic; no v35 algorithm modification or promotion.

For each frozen-v35 accepted decision, score every candidate against the observations available to v35 (nonmissing initial observations, all followups, and selected probes). The discrete residual penalty is 0 for |error|=0, 1 for |error|=1, and `8+4*(|error|-2)` for |error|>=2. This is a heuristic negative log-likelihood approximation, not calibrated probabilities. Ties sort by candidate ID. Accept in shadow only if v35's accepted candidate equals the best noise-ranked candidate and the runner-up penalty gap is at least 0.5 or at least 1 (with integer penalties these thresholds are effectively identical; this intentionally checks threshold sensitivity and should be revised for a noninteger score in a later iteration).

Run a fresh 4,000-task synthetic development suite with `seed=1700001 count=200 seedCount=4`. Record correct accepted, wrong accepted, abstentions, correct rejected, wrong prevented, and requests; preserve source SHA. Existing suites are exposed and not independent holdouts. No deployment or baseline change is authorized from this experiment alone.
