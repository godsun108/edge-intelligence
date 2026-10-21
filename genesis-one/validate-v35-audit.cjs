#!/usr/bin/env node
'use strict';
// Genesis ONE v36: structural validation of v35 audit exports.
// This is NOT an independent re-execution of the browser inference code.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const file = process.argv[2];
if (!file) { console.error('Usage: node genesis-one/validate-v35-audit.cjs <audit.json>'); process.exit(2); }
const a = JSON.parse(fs.readFileSync(file, 'utf8'));
const eq = (actual, expected, label) => assert.deepEqual(actual, expected, label);
eq(a.version, 35, 'version');
const s = a.settings;
for (const k of ['seed','count','reps','seedCount']) assert.ok(Number.isSafeInteger(s[k]) && s[k] > 0, k);
eq(a.gate, {fit:'mae',pool:8,tolerance:1,minObs:2,cap:4,mode:'efficient'}, 'frozen policy');
const scenarios = ['reference','high_noise','combined_stress','novel_families','unseen_K_test_only'];
eq(a.runs.length, s.seedCount, 'seed batches');
eq(a.taskCount, s.seedCount * s.count * scenarios.length, 'task count');
let mismatches=0, correct=0, wrong=0, accepted=0;
a.runs.forEach((run,i)=>{
 eq(run.seed,(s.seed+i*7919)>>>0,'seed sequence');
 eq(run.byScenario.map(x=>x.scenario),scenarios,'scenario names');
 for(const sc of run.byScenario){
  eq(sc.tasks,s.count,'scenario task count');
  for(const k of ['mismatches','correct','wrong','accepted']) assert.ok(Number.isSafeInteger(sc[k])&&sc[k]>=0,k);
  assert.ok(sc.correct+sc.wrong===sc.accepted && sc.accepted<=sc.tasks,'acceptance accounting');
  mismatches+=sc.mismatches;correct+=sc.correct;wrong+=sc.wrong;accepted+=sc.accepted;
 }
});
eq(a.mismatchCount,mismatches,'mismatch total');
if(mismatches===0)eq(a.mismatches.length,0,'mismatch examples');
for(const version of ['v29','v30','v35']){
 const t=a.totals[version];
 eq([t.correct,t.wrong,t.accepted],[correct,wrong,accepted],version+' totals');
 assert.ok(Number.isSafeInteger(t.requests)&&t.requests>=0,'requests');
 const times=a.timingsMs[version];
 eq(times.length,s.seedCount*s.reps,version+' timing count');
 times.forEach((x,i)=>{
  eq(x.seed,a.runs[Math.floor(i/s.reps)].seed,'timing seed');
  assert.ok(Number.isFinite(x.ms)&&x.ms>=0,'timing');
  assert.ok(Number.isFinite(x.checksum),'checksum');
 });
 const sorted=times.map(x=>x.ms).sort((x,y)=>x-y);
 const median=sorted[Math.floor(sorted.length/2)];
 assert.ok(Math.abs(median-a.medianMs[version])<1e-7,version+' median');
}
eq(a.totals.v29,a.totals.v30,'v29/v30 aggregate totals');
eq(a.totals.v29,a.totals.v35,'v29/v35 aggregate totals');
const faster=a.medianMs.v35<a.medianMs.v29;
const zero=mismatches===0;
eq(a.criteria,{zeroBehaviorMismatches:zero,medianFasterThanV29:faster,passed:zero&&faster},'criteria');
assert.ok(Math.abs(a.speedupPct-100*(a.medianMs.v29-a.medianMs.v35)/a.medianMs.v29)<1e-7,'speedup');
console.log(JSON.stringify({valid:true,version:35,taskCount:a.taskCount,mismatches,correct,wrong,accepted,medianMs:a.medianMs,criteria:a.criteria,scope:'structural audit consistency only'},null,2));
