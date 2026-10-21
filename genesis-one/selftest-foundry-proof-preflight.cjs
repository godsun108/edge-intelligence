#!/usr/bin/env node
'use strict';
// Dependency-free regression checks for Foundry proof preflight.
// Run: node genesis-one/selftest-foundry-proof-preflight.cjs
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const dir=fs.mkdtempSync(path.join(os.tmpdir(),'genesis-proof-'));
try{
 const audit=path.join(dir,'audit.json'),registry=path.join(dir,'NORTH_STARS.json');
 fs.writeFileSync(audit,JSON.stringify({version:35}));
 const run=(entries)=>{fs.writeFileSync(registry,JSON.stringify({schema:'turbo.north-stars.v1',entries}));return cp.spawnSync(process.execPath,[path.join(__dirname,'foundry-proof-preflight.cjs'),registry,audit],{encoding:'utf8'});};
 let r=run([{id:'edge-value',owner:'edge'}]);
 assert.equal(r.status,3,'missing Genesis owner must fail closed');
 assert.equal(JSON.parse(r.stdout).status,'BLOCKED_INVALID_CANONICAL_REGISTRY_ENTRY');
 for(const entries of [
  [{id:'genesis-one',owner:'wrong'}],
  [{id:'genesis-one',owner:''}],
  [{id:'genesis-one',owner:'genesis-one'},{id:'genesis-one',owner:'genesis-one'}]
 ]){
  r=run(entries);
  assert.equal(r.status,3,'incorrect, empty or duplicate owner must fail closed');
  assert.equal(JSON.parse(r.stdout).canonicalOwnerVerified,false);
 }
 r=run([{id:'genesis-one',owner:'genesis-one'}]);
 assert.equal(r.status,0,'canonical owner allows review preflight');
 assert.equal(JSON.parse(r.stdout).canonicalProducer,'genesis-one');
 console.log('Foundry proof preflight selftests passed: missing/wrong/empty/duplicate-owner blocked, registered-owner review ready');
}finally{fs.rmSync(dir,{recursive:true,force:true});}
