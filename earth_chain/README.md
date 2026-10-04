# Earth Chain Market Intelligence — EDGE adapter v0.1

An internal, local-first, dependency-free evidence validator. This is **not** a futures exchange, broker, index publisher, or cannabis trading platform.

## Canonical system ownership
- EDGE owns supplier/price intelligence and provenance.
- MINT owns reviewed opportunities and confirmed settlement (not inferred revenue).
- Turbo Foundry owns engineering and reproducible tests.
- Command Center may read a generated report, but must display NOT CONNECTED until actually wired.
- Portal may eventually display approved public information, never private counterparty records.
- EARTH NOW remains the environmental observation owner.
- Sovereign Core may later supply shared contracts; no dependency is asserted today.

## Run
```sh
python earth_chain/engine.py earth_chain/observations.json
python -m unittest discover -s earth_chain -p 'test_*.py'
```

The initial observations file is empty. No market prices are invented. Fields are USD/metric ton, ISO-8601 timestamp, evidence URL, commodity, quote kind, region and source. Executed transactions require an explicit evidence-verification flag. The digest helps identify report-input changes; it does not establish authenticity or tamper-proof storage.

## Next gates
1. Obtain supplier permission and lawful publicly shareable observations.
2. Review and verify five suppliers and five buyers.
3. Record one genuine procurement introduction with human authorization.
4. Connect report export to EDGE and Command Center after contract review.
5. Only consider a published benchmark after methodology, sampling, quality grades, auditability and legal review.

No automatic contract execution, token issuance, price index, or derivatives trading.
