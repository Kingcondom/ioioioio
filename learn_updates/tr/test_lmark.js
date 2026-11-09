const { chromium } = require('playwright');
const U='http://localhost:8766/index.html', OUT=process.argv[2];
(async()=>{const b=await chromium.launch();const R=[];
for(const [w,h,mob] of [[390,844,true],[1440,900,false]]){
  const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:mob,hasTouch:mob});const p=await ctx.newPage();const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.goto(U+'#hemonc');await p.waitForTimeout(1500);
  // lectures list view
  await p.evaluate(()=>{document.querySelector('[data-trview="lectures"],.tr-bn:nth-child(2)').click()});await p.waitForTimeout(800);
  R.push([w+' list',await p.evaluate(()=>({view:document.body.dataset.view,wraps:document.querySelectorAll('.tr-lw').length,btn:document.querySelector('.tr-lw .tr-lmark')&&document.querySelector('.tr-lw .tr-lmark').textContent}))]);
  await p.locator('.tr-lw .tr-lmark').first().click();await p.waitForTimeout(800);
  R.push([w+' after mark',await p.evaluate(()=>{const st=JSON.parse(localStorage.getItem('med421-learn-v1'));return {btn:document.querySelector('.tr-lw .tr-lmark').textContent,on:document.querySelector('.tr-lw .tr-lmark').classList.contains('on'),chip:document.querySelector('.tr-lw .lchips .chip.acc')&&document.querySelector('.tr-lw .lchips .chip.acc').textContent,done:Object.keys(st.done).length,log:Object.values(st.log||{}).flat().length,toast:(document.querySelector('.tr-toast')||{}).textContent,sw:document.documentElement.scrollWidth}})]);
  await p.screenshot({path:`${OUT}/lm-${w}-list.png`});
  // home tag
  await p.evaluate(()=>{const x=document.querySelector('.tr-side [data-trview="home"]')||document.querySelector('.tr-bn');x.click()});await p.waitForTimeout(800);
  R.push([w+' home tag',await p.evaluate(()=>document.querySelector('.tr-card .tr-c-foot .tr-tag').textContent)]);
  await p.screenshot({path:`${OUT}/lm-${w}-home.png`});
  // sheet: unmark
  await p.locator('.tr-card').first().click();await p.waitForTimeout(700);
  R.push([w+' sheet btn',await p.evaluate(()=>document.querySelector('.tr-sheet [data-trlmark]').textContent)]);
  await p.screenshot({path:`${OUT}/lm-${w}-sheet.png`});
  await p.locator('.tr-sheet [data-trlmark]').click();await p.waitForTimeout(900);
  R.push([w+' after unmark',await p.evaluate(()=>({tag:document.querySelector('.tr-card .tr-c-foot .tr-tag').textContent,done:Object.keys(JSON.parse(localStorage.getItem('med421-learn-v1')).done).length,sheet:document.querySelector('.tr-sheet').open}))]);
  // lecture page
  await p.evaluate(()=>{location.hash='#hemonc-12.10'});await p.waitForTimeout(900);
  R.push([w+' lecture page',await p.evaluate(()=>({view:document.body.dataset.view,btn:document.querySelector('#main .meta [data-trlmark]')&&document.querySelector('#main .meta [data-trlmark]').textContent}))]);
  R.push([w+' errs',errs]);await ctx.close()}
console.log(R.map(x=>x[0]+': '+JSON.stringify(x[1])).join('\n'));await b.close()})();
