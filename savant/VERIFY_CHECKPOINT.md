# SAVANT Independent Checkpoint Verification v1.2

SAVANT can now verify an exported `edge.savant.checkpoint.v1` JSON file supplied by the user.

Verification has two distinct levels:

1. **Checkpoint file integrity** — recompute the checkpoint SHA-256 from its canonical recorded fields and compare it with `checkpoint_hash`.
2. **Local-history correspondence** — if the browser currently contains the matching claim ID, verify that the checkpoint chain tip corresponds to the event at the checkpoint's recorded event count.

The UI distinguishes:
- CHECKPOINT FILE HASH VERIFIED
- LOCAL HISTORY MATCHES CHECKPOINT
- LOCAL HISTORY DOES NOT MATCH CHECKPOINT
- NO MATCHING LOCAL CLAIM · FILE INTEGRITY ONLY
- explicit verification failures

## Important limitation

Self-hash verification can detect accidental corruption or modification that was not followed by recomputing the hash. It does not establish authorship or a trusted time because an attacker able to rewrite a checkpoint can also recompute an unsigned hash.

The next trust tier is asymmetric digital signatures and/or an independently anchored checkpoint hash.
