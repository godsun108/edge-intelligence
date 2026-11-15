# Genesis ONE v36 — existing Foundry proof integration

Status: **preflight implemented; receipt issuance blocked pending canonical registry ownership**.

## Existing interfaces inspected
- `godsun108/turbo-foundry/proof/PROOF_RECEIPT.schema.json`: `turbo.proof-receipt.v1`.
- `godsun108/turbo-foundry/proof_receipts.py`: receipt `producer.system` must equal the canonical `NORTH_STARS.json` entry's `owner`; directory and filename must match IDs.
- `godsun108/turbo-foundry/proof/README.md`: structural validation is not proof review; producer cannot self-promote maturity.
- `godsun108/turbo-foundry/docs/autopilot/foundry-genesis-integration-contract.md`: separate architectural language inference contract, **not** a deployed Genesis endpoint.

## Current blocker
As inspected October 20, 2026, Foundry `NORTH_STARS.json` contains no `genesis-one` entry. Existing `edge-value` and `sovereign-core` entries are different systems. Do not issue a receipt against either to bypass ownership.

## Local preflight
```sh
node genesis-one/validate-v35-audit.cjs path/to/genesis-regression-v35.json
node genesis-one/foundry-proof-preflight.cjs path/to/turbo-foundry/NORTH_STARS.json path/to/genesis-regression-v35.json
```
The second command intentionally exits 3 while the registry entry is absent. It does not perform inference replay or hash evidence. No third-party runner is required.

## Next safe steps
1. Obtain reviewed decision for a distinct Genesis ONE North Star entry and canonical producer owner in Foundry. This is a cross-repository governance change, **not** done here.
2. Preserve the original v35 export and its SHA-256 fingerprint; verify source provenance.
3. Independently replay deterministic task-level inference; existing v35 structural audit alone cannot substantiate parity.
4. Produce `turbo.proof-receipt.v1` only after validation, with `environment: synthetic`, an exact bounded claim, limitations, and fingerprints.
5. Have Foundry reviewer validate evidence, then separately consider registry proof status and Command Center regeneration.

No production integration, spending, or merge authorized. GitHub Actions is optional; local/own verification is primary.
