# Genesis ONE — failure case 1707920 / combined_stress / task 100

Evidence: [likelihood evaluation run 39500520677](https://github.com/godsun108/edge-intelligence/actions/runs/39500520677), artifact ID `12300400647`, JSON `wrongAcceptedExamples[0]`. This is a post-hoc case study, not an independent validation result.

- Ground truth `L:-2:-4`, frozen v35 accepted `L:-2:-5` at stage 4.
- All six initial observations missing.
- Followups: x=-9,y=13 and x=1,y=-7; x=-7 and x=-4 missing. Both observed followups agree with the *wrong* offset -5.
- Selected probes x=8 (missing), x=7 (missing), x=4 (y=-13, supports wrong offset -5), x=3 (y=-10, supports true offset -4).
- **Unselected, pre-generated** probes x=-8,y=12; x=-2,y=0; x=1,y=-6 all support the true offset -4. These are counterfactual observations, **not** measurements the algorithm actually requested. Acquiring them would incur extra request cost.
- Wrong candidate and true candidate differ by a constant one-unit offset at every x, so moving probes farther away cannot increase their separation. Probe *availability*, repeated independent measurements, and noise aggregation are plausible research directions.
- Reported v35 requested count 8; this example has 2 observed selected probes and zero bad probes according to the decision record. The 8 requested count is the harness metric; do not equate it to eight observed measurements.

## Follow-up experiment proposal

Predeclare a **budgeted probe-acquisition** policy before evaluation: request additional pre-generated probes only when evidence is sparse and leading candidates are within a one-unit prediction gap. Count every additional probe request, including missing results. Compare wrong accepts, correct accepts, abstentions, and total request cost across a new synthetic development suite. Do not peek at unselected probe values when deciding whether to request them. Keep frozen v35 as the comparator, not an edited source.
