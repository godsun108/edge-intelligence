# Genesis ONE — probe discrimination diagnostics

Evidence: distinct-seed GitHub Actions [run 39493990924](https://github.com/godsun108/edge-intelligence/actions/runs/39493990924), artifact `genesis-distinct-seed-evidence`; diagnostic instrumentation at commit `72092a116f9f7f774a6c06b1ea6da239128897c9`. Same synthetic generator and frozen v35 inference; not an independent holdout.

## Error 1: combined_stress, task 99, seed 907920

Truth `L:2:4`; accepted `L:2:5`. Top alternatives by initial/followup fit include `L:2:4` (loss 0.5), `L:2:3` (loss 1.5), `L:2:2` (loss 2.5). The accepted candidate differs from the true alternative by **1 unit at every x**, so simply choosing a more distant x cannot amplify separation. Selected probes x=8 and x=-8 both happened to agree exactly with the wrong candidate; an unselected x=3 agreed with truth. This is a noise/replication problem rather than a lack of spatial separation.

## Error 2: unseen_K_test_only, task 75, seed 907920

Truth `U:-1`; accepted `U:-2`. Top alternatives include `U:-1` (loss 0.6), `U:-3` (loss 1.4), `U:0` (loss 1.6). Again the true alternative differs by **1 unit at every x**. Selected x=-8 and x=-2 agree exactly with the wrong candidate; unselected x=3 agrees with truth. Probe location alone cannot increase separation between these offset-only candidates.

## Implication

A maximum-prediction-separation probe heuristic cannot solve these specific constant-offset confusions: the separation is invariant in x. Test noise-aware aggregation, repeated observations at multiple x, or an abstention rule calibrated on the candidate margin, but quantify correct-acceptance loss and additional observation cost on fresh development seeds. Do not modify frozen v35 based solely on these two selected cases.
