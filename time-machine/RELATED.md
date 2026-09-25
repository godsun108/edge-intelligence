# Related Memory

TIME MACHINE v0.3 adds deliberate RELATED retrieval.

Selecting RELATED on a capture compares it only with the user's other local SENSE captures. The current method is intentionally inspectable: token overlap plus small same-type and same-route boosts. Results require at least one shared token and return at most five candidates.

The displayed percentage is a retrieval similarity score, not probability, truth, importance, causation, or evidence that two memories are genuinely related. Results are explicitly labeled **MACHINE-DERIVED**.

No embedding service, remote model, or external search receives the capture text in v0.3.
