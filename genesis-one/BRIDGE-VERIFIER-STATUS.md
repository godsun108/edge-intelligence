# Genesis public-evidence bridge verifier status

`bridge-verify.cjs` is a **read-only local import validator**, not a deployed private/public connection. It parses bounded JSON evidence, checks declared SHA-256 digest, job and commit formats, exact schema and counters, and emits an explicit `verified_provenance:false` / `authorized_for_promotion:false` result. This deliberately does **not** authenticate GitHub Actions provenance, independently verify expected digests, establish origin trust, prevent replay or prove inference correctness. Those require an authenticated private job ledger with expected job IDs, commits, digests and an allowlisted source.

The public controller currently emits a different preliminary summary shape. Before connecting it, add a pinned manifest emitter, private-side allowlisted expected-job verification, adversarial tests and a full verified import. Do not accept evidence merely because a self-declared manifest hash matches its accompanying file: an attacker could replace both. Do not execute artifacts.

The GitHub repository is not the private Command Center. Existing private bridge infrastructure needs direct local inspection before integration. No private state should be uploaded to this repository.
