#!/usr/bin/env node
'use strict';
// Independent task-level replay from checked-in v35 source, not an audit JSON parser.
// Uses Node VM to evaluate the original browser algorithm in an isolated sandbox.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const html=fs.readFileSync(path.join(__dirname,'regression-v35.html'),'utf8');
const match=html.match(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/i);
assert.ok(match,'browser script missing');
const nodes=new Map();
const element=id=>{if(!nodes.has(id))nodes.set(id,{value:'',textContent:'',onclick:null});return nodes.get(id)};
const sandbox={document:{getElementById:element},localStorage:{getItem:()=>null,setItem:()=>{}},setTimeout:()=>{},console};
vm.createContext(sandbox);

// Insert a replay entry point INSIDE the browser's lexical closure.
const marker="$('run').onclick=";
assert.ok(match[1].includes(marker),'browser run hook missing');
const injected=`globalThis.__genesisReplay=function(opts){const seed=opts.seed,count=opts.count,seedCount=opts.seedCount;
const byScenario=[],failures=[];let tasks=0,mismatches=0,correct=0,wrong=0,accepted=0,requests=0;
 for(let z=0;z<seedCount;z++){const runSeed=(seed+z*7919)>>>0;
  for(let i=0;i<scenarios.length;i++){const sc=scenarios[i],rows=make((runSeed+i*100003)>>>0,count,sc);
   let sm=0,sw=0,sa=0,sbad=0;
   for(const row of rows){const a=decide29(row,gate),b=decide30(row,gate),c=decide32(row,gate);tasks++;
    const ok=signature(a)===signature(b)&&signature(a)===signature(c);
    if(!ok){mismatches++;sm++;if(failures.length<20)failures.push({seed:runSeed,scenario:sc.name,task:row.task,target:row.target,v29:a,v30:b,v35:c})}
    correct+=Number(c.correct);wrong+=Number(c.wrong);accepted+=Number(c.decision==='accept');requests+=c.requested;
    sw+=Number(c.correct);sbad+=Number(c.wrong);sa+=Number(c.decision==='accept');
   }
   byScenario.push({seed:runSeed,scenario:sc.name,tasks:rows.length,mismatches:sm,correct:sw,wrong:sbad,accepted:sa});
  }
 }
 return {tasks,mismatches,correct,wrong,accepted,requests,byScenario,failures};
})()`,sandbox,{timeout:120000});
`;
vm.runInContext(match[1].replace(marker,injected+marker),sandbox,{filename:'regression-v35.browser.js',timeout:30000});
const opts={seed:31071,count:800,seedCount:1};
for(const a of process.argv.slice(2)){const [k,v]=a.split('=');if(!(k in opts)||!Number.isSafeInteger(Number(v))||Number(v)<1)throw Error('Invalid argument: '+a);opts[k]=Number(v)}
assert.ok(opts.count<=3000&&opts.seedCount<=12,'bounded replay');
const run=sandbox.__genesisReplay(opts);
const output={schema:'genesis.task-replay.v1',source:'genesis-one/regression-v35.html',sourceSha256:crypto.createHash('sha256').update(html).digest('hex'),settings:opts,scope:'Node VM re-execution of checked-in browser v35 algorithms; no independent implementation or browser timing',...run};
console.log(JSON.stringify(output,null,2));
if(run.mismatches)process.exitCode=1;
