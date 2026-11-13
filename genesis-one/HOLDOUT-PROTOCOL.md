# Genesis ONE — exploratory distinct-seed evaluation

Evaluate frozen v35 on new synthetic instances, without changing inference logic or gates. This is NOT a sealed independent holdout or evidence of general intelligence.

- Keep original regression gate: `seed=31071 count=200 seedCount=4`.
- Distinct-seed evaluation: `seed=900001 count=200 seedCount=4` (4,000 tasks, five existing scenarios).
- Record source SHA-256, settings, correct, wrong, accepted, abstained, requests, per-scenario totals, and mismatches.
- Do not tune thresholds to these results and then call this an untouched holdout.
- A wrong accepted answer matters even if implementation mismatch count is zero.

**Limits:** The generator, scenarios, and browser implementation are reused through a Node VM. New seeds do not establish independent generation, a novel distribution, or a separately implemented reference. A genuinely sealed, preregistered external holdout remains future work.
