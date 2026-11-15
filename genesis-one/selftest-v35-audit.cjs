#!/usr/bin/env node
'use strict';
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const assert=require('node:assert/strict');
const {spawnSync}=require('node:child_process');
const scenarios=['reference','high_noise','combined_stress','novel_families','unseen_K_test_only'];
const seed=31071, count=10, reps=3, seedCount=2;
const runs=Array.from({length:seedCount},(_,i)=>({seed:(seed+i*7919)>>>0,byScenario:scenarios.map(s=>({scenario:s,tasks:count,mismatches:0,correct:4,wrong:1,accepted:5}))}));
const timing=(ms)=>runs.flatMap(r=>Array.from({length:reps},()=>({seed:r.seed,ms,checksum:20})));
const total={correct:40,wrong:10,accepted:50,requests:100};
const a={version:35,settings:{seed,count,reps,seedCount},gate:{fit:'mae',pool:8,tolerance:1,minObs:2,cap:4,mode:'efficient'},taskCount:100,mismatchCount:0,mismatches:[],runs,totals:{v29:total,v30:total,v35:total},timingsMs:{v29:timing(20),v30:timing(25),v35:timing(15)},medianMs:{v29:20,v30:25,v35:15},speedupPct:25,criteria:{zeroBehaviorMismatches:true,medianFasterThanV29:true,passed:true}};
const dir=fs.mkdtempSync(path.join(os.tmpdir(),'genesis-audit-'));
const validator=path.join(__dirname,'validate-v35-audit.cjs');
try{
 const fixture=path.join(dir,'audit.json');
 const check=(obj)=>{fs.writeFileSync(fixture,JSON.stringify(obj));return spawnSync(process.execPath,[validator,fixture],{encoding:'utf8'});};
 let result=check(a);assert.equal(result.status,0,result.stderr);
 result=check({...a,mismatchCount:1});assert.notEqual(result.status,0,'tampered mismatch count should fail');
 result=check({...a,medianMs:{...a.medianMs,v35:99}});assert.notEqual(result.status,0,'tampered median should fail');
 result=check({...a,taskCount:101});assert.notEqual(result.status,0,'tampered task count should fail');
 console.log('PASS: valid synthetic fixture accepted; three tampered fixtures rejected.');
} finally {fs.rmSync(dir,{recursive:true,force:true});}
