# SAVANT Integrity Checkpoints v1.1

A claim with a verified hash-chained history can now create a portable integrity checkpoint.

A checkpoint records:
- schema
- claim ID and claim text at checkpoint time
- checkpoint creation time
- event count
- history chain-tip SHA-256
- SHA-256 of the checkpoint record itself

The browser can verify that the checkpoint record has not changed and that its chain tip still matches the corresponding event in the current local history. Checkpoints can be exported as human-readable JSON.

## What this improves

If a checkpoint file is copied somewhere independent of the active browser store, it becomes a useful comparison artifact: later research history can be checked against the earlier chain tip.

## What this does not prove

The checkpoint is not digitally signed, notarized, externally timestamped, or automatically published. A checkpoint retained only beside the mutable local database does not create independent trust. Stronger assurance requires deliberately storing its hash or signed record in an independent system.
