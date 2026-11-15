# Genesis ONE — Private/Public Research Bridge

Status: **architecture contract; not a verified deployed connection**. Private/local systems remain authoritative. Public GitHub is a secondary, untrusted compute and evidence surface. This design should integrate with the existing Command Center registry, evidence intake, portable runners and verification gates, not replace them.

## Outbound job (private -> public)

Only export explicitly allowlisted synthetic fixtures, nonsecret algorithm test bundles and reproducible run configuration. A job manifest should contain `schema`, `job_id`, `source_commit`, `source_sha256`, `fixture_sha256`, `policy_ids`, `seed`, `task_count`, `expected_outputs`, and a privacy classification. Never export local VictoryChain state, identity or signing material, tokens, proprietary/private prompts, customer information, private strategies, or unreviewed files. Refuse ambiguous classification. Require a human approval step before the first export of any new data category.

## Public worker

Run a pinned, bounded, no-secrets workflow with read-only repository permissions, no untrusted PR execution with secrets, explicit timeouts and uploaded machine-readable evidence. The public worker must not mint private approval receipts or promote policies. Its result is an untrusted claim even if CI is green.

## Inbound evidence (public -> private)

Download via an authenticated, explicitly allowlisted channel; verify expected job ID, exact source commit and input digests, expected schema, size bounds, replay determinism, workflow provenance, and artifact SHA-256. Reject missing, stale, replayed, mismatched or malformed results. Quarantine artifacts until validation. Record accepted/rejected receipts in the private Command Center ledger. Do not execute downloaded scripts or merge code automatically. An artifact hash proves integrity relative to a trusted expected hash, not correctness or trustworthy authorship by itself.

## Authority and promotion

Only private-side policy may authorize further use. Genesis frozen v35 remains immutable. Shadow policies stay experimental; real-world orders and other privileged actions remain disabled. No autonomous self-modification, publishing local-only assets, or syncing local VictoryChain to GitHub. No new spending.

## Integration milestones

1. Inspect the actual private Command Center evidence intake and public Oracle-Q relay contract before implementation; reconcile schemas rather than invent parallel APIs.
2. Publish a synthetic, harmless outbound job and verify a full public-run -> private-import round trip with digest and provenance checks.
3. Test negative cases: tampered artifact, wrong commit, stale receipt, duplicate job, missing provenance, private-data leakage.
4. Only after verified round trip, let the Genesis controller submit allowlisted experimental tasks; keep policy promotion manual.

## Current verified limits

The GitHub Genesis workflows and local Command Center/Oracle-Q pieces have been developed separately; a live Genesis public-to-private round trip has **not** been established by this document. GitHub workflow scheduling on a nondefault branch is not proof of unattended execution. Preserve the existing local-first architecture and do not infer access to private computer files from a GitHub checkout.
