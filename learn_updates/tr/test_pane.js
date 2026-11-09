const { chromium } = require('playwright');
const U='http://localhost:8766/index.html', OUT=process.argv[2];
(async()=>{const b=await chromium.launch();const R=[];
for(const [w,h] of [[1440,1000],[1200,850]]){
  const p=await b.newPage({viewport:{width:w,height:h}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
  await p.goto(U+'#hemonc-12.10');await p.waitForTimeout(1500);
  await p.locator('main [data-sec]').first().click();await p.waitForTimeout(800);
  const box=()=>p.evaluate(()=>{const c=document.querySelector('#main>.card').getBoundingClientRect();return {x:Math.round(c.x),w:Math.round(c.width),sw:document.documentElement.scrollWidth,cls:document.documentElement.className}});
  R.push([w+' both shown',await box()]);
  await p.screenshot({path:`${OUT}/p-${w}-0.png`});
  await p.locator('.tr-side [data-trpane="s"]').click();await p.waitForTimeout(500);
  if(w>=1400){await p.locator('.tr-dock [data-trpane="d"]').click();await p.waitForTimeout(500)}
  R.push([w+' both hidden',await box()]);
  await p.screenshot({path:`${OUT}/p-${w}-1.png`});
  await p.reload();await p.waitForTimeout(1500);
  R.push([w+' after reload',await p.evaluate(()=>[document.documentElement.className,getComputedStyle(document.querySelector('.tr-rail-l')).display])]);
  await p.locator('.tr-rail-l').click();await p.waitForTimeout(400);
  await p.keyboard.press(']');await p.waitForTimeout(400);
  R.push([w+' restored',await box()]);
  await p.keyboard.press('[');await p.waitForTimeout(400);
  // AI panel when dock hidden
  if(w>=1400){await p.keyboard.press(']');await p.waitForTimeout(300);await p.locator('.tr-side [data-trai]').count();
    await p.keyboard.press('[');await p.waitForTimeout(300);
    await p.locator('.tr-side [data-trai]').click();await p.waitForTimeout(500);
    R.push(['ai w/ dock',await p.evaluate(()=>{const r=document.querySelector('.ai-panel').getBoundingClientRect();return [Math.round(r.right),Math.round(r.width)]})]);
    await p.keyboard.press('Escape');}
  R.push([w+' errs',errs]);await p.close()}
console.log(R.map(x=>x[0]+': '+JSON.stringify(x[1])).join('\n'));await b.close()})();
