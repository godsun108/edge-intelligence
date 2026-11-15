#!/usr/bin/env node
'use strict';
// Local-side verifier for public experimental evidence. Never executes downloaded code.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
function sha(b){return crypto.createHash('sha256').update(b).digest('hex')}
function verify(manifestPath,summaryPath){
 const mb=fs.readFileSync(manifestPath),sb=fs.readFileSync(summaryPath);
 assert.ok(mb.length<65536&&sb.length<1048576,'evidence size limit');
 const m=JSON.parse(mb),s=JSON.parse(sb);
 assert.equal(m.schema,'genesis.public-evidence.v1');
 assert.match(m.job_id,/^[a-zA-Z0-9._-]{1,128}$/);
 assert.match(m.source_commit,/^[a-f0-9]{40}$/);
 assert.match(m.summary_sha256,/^[a-f0-9]{64}$/);
 assert.equal(sha(sb),m.summary_sha256,'summary digest mismatch');
 assert.equal(s.schema,'genesis.research-summary.v1');
 assert.equal(s.job_id,m.job_id);assert.equal(s.source_commit,m.source_commit);
 assert.equal(s.status,'experimental');assert.equal(s.promotion,'forbidden');
 assert.ok(Array.isArray(s.runs)&&s.runs.length>=1&&s.runs.length<=12);
 for(const run of s.runs){assert.equal(run.tasks,4000);assert.equal(run.mismatches,0);assert.ok(Number.isSafeInteger(run.requests)&&run.requests>=0);for(const key of ['baseline','uncertaintyGap2','uncertaintyGap4']){const p=run.policies[key];assert.ok(Number.isSafeInteger(p.correct)&&p.correct>=0);assert.ok(Number.isSafeInteger(p.wrong)&&p.wrong>=0);assert.equal(p.accepted,p.correct+p.wrong)}}
 return {job_id:m.job_id,source_commit:m.source_commit,summary_sha256:m.summary_sha256,verified_structure:true,verified_digest:true,verified_provenance:false,authorized_for_promotion:false};
}
if(require.main===module){try{if(process.argv.length!==4)throw Error('usage: node bridge-verify.cjs manifest.json summary.json');console.log(JSON.stringify(verify(process.argv[2],process.argv[3])))}catch(e){console.error('REJECTED:',e.message);process.exitCode=1}}
module.exports={verify};
