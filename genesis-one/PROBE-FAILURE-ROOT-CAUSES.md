# Genesis ONE — exact probe-budget failure analysis

Source: [successful GitHub Actions run 39519755704](https://github.com/godsun108/edge-intelligence/actions/runs/39519755704), artifact `genesis-probe-budget-development`, wrongDiagnostics entries. Development-only, post-hoc diagnosis; frozen v35 unchanged.

## Wrong acceptance 1: trigger exclusion

Seed `2100001`, `combined_stress`, task `119`. Truth `L:-2:3`; accepted `L:-2:2`. Initial nonmissing count 3; followup nonmissing count 3; five unselected probes; offset competitor exists. Acquisition rule required both counts <=2, so **ineligible**. Candidate absolute-error totals before acquisition: wrong `L:-2:2`=2; true `L:-2:3`=6. We did not request extra probes for this task. Cannot claim extra probing would correct it.

## Wrong acceptance 2: extra observations reinforce error

Seed `2115839`, `combined_stress`, task `76`. Truth `V:-5`; accepted `V:-4`. Initial nonmissing count 1; followup nonmissing count 1; four unselected probes; offset competitor exists. **Eligible**. Original absolute-error totals: wrong `V:-4`=1; true `V:-5`=3. Additional probes selected *before reading values*: x=3,y=11; x=8,y=null; x=4,y=null. Two of three requests were missing. Augmented totals: wrong `V:-4`=1; true `V:-5`=4. Wrong answer remained preferred, so no veto.

## Interpretation

Two separate failure mechanisms: (1) eligibility trigger too narrow for some wrong accepts, (2) noisy or missing added evidence can preserve or even strengthen a wrong winner. These observations **do not prove** that a broader trigger or more requests would improve overall performance. In particular, widening eligibility could raise cost and reject correct predictions.

Next experiment: preregister comparison of selective repeat measurements and a probabilistic uncertainty-based abstention decision on fresh development seeds. Require explicit additional request accounting and guard against selection on ground-truth labels. Do not promote a candidate based on these two exposed examples.
