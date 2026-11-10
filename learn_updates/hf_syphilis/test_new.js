const { chromium } = require('playwright');
const U='http://localhost:8767/index.html', OUT=process.argv[2];
(async()=>{const b=await chromium.launch();const R=[];
for(const [w,h,mob] of [[390,844,true],[1440,900,false]]){
 const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:mob,hasTouch:mob});const p=await ctx.newPage();const errs=[];
 p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource/.test(m.text()))errs.push(m.text())});
 for(const [set,lec] of [['cardio','HF'],['id','10.11']]){
  await p.goto(U+'#'+set);await p.waitForTimeout(1200);
  await p.evaluate(h=>{location.hash=h},'#'+set+'-'+lec);await p.waitForTimeout(1200);
  const lv=await p.evaluate(()=>({view:document.body.dataset.view,h2:(document.querySelector('#main h2')||{}).textContent,tiles:document.querySelectorAll('main [data-sec]').length}));
  R.push([w+' '+set+' lecture',lv]);
  await p.screenshot({path:`${OUT}/${set}-${w}-lec.png`});
  const n=lv.tiles;let bad=[];
  for(let i=0;i<n;i++){
   await p.evaluate(h=>{location.hash='#zz';location.hash=h},'#'+set+'-'+lec);await p.waitForTimeout(600);
   await p.locator('main [data-sec]').nth(i).click();await p.waitForTimeout(500);
   const r=await p.evaluate(()=>{const m=document.getElementById('main');const t=m.innerText;
     return {h2:(m.querySelector('h2')||{}).textContent,raw:/\*\*|\[\[(fig|anim|img):|^#{1,2} /m.test(t),figs:m.querySelectorAll('.fig svg').length,sw:document.documentElement.scrollWidth,
       tbl:[...m.querySelectorAll('table')].length,gate:!!m.querySelector('.tr-gate')}});
   if(r.raw||r.sw>w)bad.push([i,r]);
   if(i===0||r.figs) await p.screenshot({path:`${OUT}/${set}-${w}-s${i+1}.png`,fullPage:false});
   if(r.figs){await p.evaluate(()=>document.querySelector('#main .fig').scrollIntoView({block:'start'}));await p.waitForTimeout(200);await p.screenshot({path:`${OUT}/${set}-${w}-fig${i+1}.png`})}
  }
  R.push([w+' '+set+' sections checked',n,'bad',bad]);
  // answer a quiz in last section
  await p.locator('.tr-gate .btn').click().catch(()=>{});await p.waitForTimeout(300);
  const qa=await p.evaluate(()=>{const q=document.querySelector("#main div.q[id^='q-']");if(!q)return 'noq';q.querySelector('.ch').click();return document.querySelectorAll('#main .verdict').length});
  R.push([w+' '+set+' quiz',qa]);
  // MEQ list includes new
  await p.evaluate(()=>{const x=document.querySelector('[data-trview="meq"]')||document.querySelectorAll('.tr-bn')[3];x.click()});await p.waitForTimeout(600);
  R.push([w+' '+set+' meq tiles',await p.evaluate(()=>document.querySelectorAll('#main [data-pid]').length)]);
 }
 R.push([w+' errs',errs]);await ctx.close()}
console.log(R.map(x=>x.map(y=>typeof y==='string'?y:JSON.stringify(y)).join(' : ')).join('\n'));await b.close()})();
