# Genesis ONE audit fixtures

The original `genesis-regression-v35.json` export is retained in the user's file library, not checked into this public repository. This prevents treating a user-supplied browser export as an independently reproduced CI result.

For local verification, run:

```sh
node genesis-one/validate-v35-audit.cjs /path/to/genesis-regression-v35.json
```

A negative test that changes `mismatchCount` from 0 to 1 is expected to fail. The validator checks internal consistency, not provenance or independent behavior.
