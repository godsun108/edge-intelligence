# SENSE v0.1

SENSE is EDGE's deliberate physical-world capture layer. v0.1 implements local-first captures for IDEA, OBJECT, OBSERVATION and TASK. Entries remain in browser localStorage and are not committed to the public repository.

This is intentionally permission-minimal. Native phone sensors, NFC, Action Button, location and camera integrations come later through explicit device permissions and platform APIs; EDGE must never imply access it does not have.

Architecture: PHONE / HUMAN → SENSE → deliberate capture → private context → EDGE.
