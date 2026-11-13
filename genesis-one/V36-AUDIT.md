# Genesis ONE — v36 audit infrastructure (phase 1)

This branch preserves the v29 reference and v35 inference implementations unchanged.

## Audit validator

Run with Node.js (no dependencies):

```sh
node genesis-one/validate-v35-audit.cjs genesis-regression-v35.json
```

Checks frozen gate, version, seed sequence, scenario coverage, task accounting, per-version totals, timing array sizes and medians, and recorded pass/fail criteria. Nonzero exit means invalid or inconsistent input.

**Boundary:** this validator checks internal consistency of the exported JSON; it does not independently rerun the inference, prove task-level equivalence, authenticate the browser build, or certify benchmark speedups across devices. The v35 export omits source SHA and per-task decision traces. A future phase must capture these explicitly and run independent replay before making stronger claims.

**Existing evidence:** 4,000 synthetic tasks, zero recorded mismatches, 4 incorrect accepted answers, 62 ms v29 median versus 57 ms v35 median. Development-visible, device-specific.
