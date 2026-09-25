# RADAR CONTRACT

RADAR converts sources into observations, compares them with remembered observations, applies explicit rules, and emits a briefing.

Pipeline: SOURCE → NORMALIZE → OBSERVATION → FINGERPRINT → CHANGE → RULES → RELEVANCE → BRIEFING.

Every observation must retain source identity, observed/retrieved timestamps, stable ID where available, URL/provenance, structured data and tags. A score is a prioritization aid, never a decision or truth claim. Public-repo rules must never contain credentials or sensitive personal information.
