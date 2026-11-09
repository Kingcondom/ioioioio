const { chromium } = require('playwright');
const U='http://localhost:8766/index.html', OUT=process.argv[2];
(async()=>{const b=await chromium.launch();const R=[];
for(const [w,h,mob] of [[390,844,true],[1440,900,false]]){
  const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:mob,hasTouch:mob});const p=await ctx.newPage();const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.goto(U+'#cardio-ihd'); await p.waitForTimeout(400);
  await p.goto(U+'#hemonc'); await p.waitForTimeout(1500);
  R.push([w+' home bar',await p.evaluate(()=>document.querySelectorAll('#main>.tr-fz').length)]);
  const sid=await p.evaluate(()=>{location.hash='#hemonc-12.10';return 1}); await p.waitForTimeout(1000);
  const lecBar=await p.evaluate(()=>document.querySelectorAll('#main>.tr-fz').length+' '+document.body.dataset.view);
  await p.locator('main [data-sec]').first().click(); await p.waitForTimeout(900);
  const W0=await p.evaluate(()=>{const c=document.querySelector('#main>.card');return [document.body.dataset.view,Math.round(c.getBoundingClientRect().height),getComputedStyle(c).zoom]});
  await p.locator('#main .tr-fz [data-trfz="1"]').click(); await p.locator('#main .tr-fz [data-trfz="1"]').click(); await p.waitForTimeout(300);
  const W1=await p.evaluate(()=>{const c=document.querySelector('#main>.card');return [Math.round(c.getBoundingClientRect().height),getComputedStyle(c).zoom,document.querySelector('#main .tr-fz output').textContent,localStorage.getItem('med421-learn-fz'),document.documentElement.scrollWidth]});
  await p.screenshot({path:`${OUT}/fz-${w}-big.png`});
  await p.reload(); await p.waitForTimeout(1500);
  const W2=await p.evaluate(()=>[document.querySelector('#main .tr-fz output').textContent,getComputedStyle(document.querySelector('#main>.card')).zoom]);
  for(let i=0;i<6;i++){const d=p.locator('#main .tr-fz [data-trfz="-1"]');if(await d.isDisabled())break;await d.click()}
  const W3=await p.evaluate(()=>[document.querySelector('#main .tr-fz output').textContent,document.documentElement.scrollWidth,!document.querySelector('#main .tr-fz [data-trfz="0"]').hidden]);
  await p.screenshot({path:`${OUT}/fz-${w}-small.png`});
  await p.locator('#main .tr-fz [data-trfz="0"]').click();
  let W4=null; if(!mob){await p.keyboard.press('=');await p.waitForTimeout(100);W4=await p.evaluate(()=>[document.querySelector('#main .tr-fz output').textContent,document.querySelector('.tr-side .tr-fz output').textContent]);await p.keyboard.press('-')}
  R.push([w+' lecture bar/view',lecBar],[w+' before',W0],[w+' after 2x A+',W1],[w+' after reload',W2],[w+' min',W3],[w+' key = (main/side)',W4],[w+' errs',errs]);
  await ctx.close()}
console.log(R.map(x=>x[0]+': '+JSON.stringify(x[1])).join('\n'));await b.close()})();
