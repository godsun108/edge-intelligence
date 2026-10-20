#!/usr/bin/env node
'use strict';
// Genesis v36: local, dependency-free preflight for Turbo Foundry proof receipts.
// This does not mint a receipt, replay inference, or promote maturity.
const fs=require('node:fs');
const assert=require('node:assert/strict');
const [registryPath,auditPath]=process.argv.slice(2);
if(!registryPath||!auditPath){
 console.error('Usage: node genesis-one/foundry-proof-preflight.cjs <NORTH_STARS.json> <v35-audit.json>');
 process.exit(2);
}
const registry=JSON.parse(fs.readFileSync(registryPath,'utf8'));
const audit=JSON.parse(fs.readFileSync(auditPath,'utf8'));
assert.equal(registry.schema,'turbo.north-stars.v1');
assert.ok(Array.isArray(registry.entries));
assert.equal(audit.version,35);
const genesis=registry.entries.filter(e=>e.id==='genesis-one');
const report={
 schema:'genesis.foundry-proof-preflight.v1',
 compatibleReceiptSchema:'turbo.proof-receipt.v1',
 genesisRegistryEntryPresent:genesis.length===1,
 canonicalProducer:genesis.length===1?genesis[0].owner:null,
 auditVersion:audit.version,
 auditClaimsStructuralOnly:true,
 status:genesis.length===1?'READY_FOR_EVIDENCE_REVIEW':'BLOCKED_MISSING_CANONICAL_REGISTRY_ENTRY',
 nextAction:genesis.length===1?
  'Independently validate source audit and SHA-256 fingerprint evidence before issuing a reviewed receipt':
  'Request reviewed Genesis ONE North Star registry entry with canonical owner; do not misattribute to EDGE or Sovereign Core'
};
console.log(JSON.stringify(report,null,2));
if(!report.genesisRegistryEntryPresent)process.exitCode=3;
