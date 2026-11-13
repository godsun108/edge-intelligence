# Genesis ONE — graded residual development protocol

Frozen inference source: `genesis-one/regression-v35.html`; never edit as part of this experiment. Diagnostic policies only veto a frozen-v35 acceptance; they cannot correct a wrong prediction.

## Predeclared candidate thresholds

For each accepted v35 decision, gather the nonmissing initial observations, all nonmissing followups, and only probes actually selected by v35. Compute residuals `observed y - proposed candidate prediction` and their median. Compare three rules: `|median| == 0` (previous baseline), `|median| <= 0.5`, and `|median| <= 1`. Do not tune thresholds based on outcome labels.

## Fresh development sample

Run `node genesis-one/replay-v35-tasks.cjs seed=1300001 count=200 seedCount=4`. Five scenarios x four seeds x 200 tasks = 4,000 synthetic tasks. Report correct accepted, wrong accepted, accepted total, abstentions, and request counts for baseline and shadow policies. Explicitly report how many correct answers are rejected per prevented wrong answer.

## Limitations

The same scenario generator and original v35 algorithm are reused, so this is *development evaluation*, not independent or sealed validation. Previously inspected suites must not be described as untouched holdouts. No policy is approved for promotion without better evaluation of error/coverage tradeoffs and an independent test distribution.
