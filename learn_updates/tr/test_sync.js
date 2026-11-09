const { chromium } = require('playwright');
const U = 'http://localhost:8766/index.html';
/* stub: บัญชีมีความคืบหน้าเดิม (ไม่มี log) + log ของอีกเครื่อง แล้วดูว่ารวมกันถูกและเขียนกลับพร้อม log */
const STUB = `(function(){
  var DB={"data/users/u1/learn":{done:{"hon-wbc-01":true},ans:{},rate:{},log:{"2026-11-08":["hon-wbc-01"]},v:1}};
  window.__DB=DB;window.__W=[];
  function snap(p){var d=DB[p];return{exists:!!d,data:function(){return JSON.parse(JSON.stringify(d||{}))},metadata:{hasPendingWrites:false}}}
  function doc(p){return{onSnapshot:function(cb){setTimeout(function(){cb(snap(p))},50);return function(){}},
    set:function(v){DB[p]=JSON.parse(JSON.stringify(v));window.__W.push(p);return Promise.resolve()}}}
  var smp=function(m,o){var t="ตัวอย่างคำตอบ";o&&o.onText&&o.onText({text:t});return Promise.resolve({text:t})};
  window.claude={use:function(n){return n==="db"?Promise.resolve({doc:doc}):n==="user"?Promise.resolve({id:function(){return Promise.resolve("u1")}}):n==="sample"?Promise.resolve(smp):Promise.reject(new Error("no"))}};
})();`;
(async () => {
  const b = await chromium.launch(); const R = [];
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.addInitScript(STUB);
  await p.goto(U + '#hemonc'); await p.waitForTimeout(2000);
  R.push(['merged log from account', await p.evaluate(() => JSON.parse(localStorage.getItem('med421-learn-v1')).log)]);
  R.push(['sync label', await p.evaluate(() => document.getElementById('lsync').textContent)]);
  R.push(['ai docked', await p.evaluate(() => ({ panel: !document.querySelector('.ai-panel').hidden, html: document.documentElement.classList.contains('tr-ai'), focus: document.activeElement.tagName, rect: (r=>[Math.round(r.top),Math.round(r.right),Math.round(r.width),Math.round(r.height)])(document.querySelector('.ai-panel').getBoundingClientRect()), dockTop: getComputedStyle(document.querySelector('.tr-dock')).top }))]);
  await p.screenshot({ path: process.argv[2] + '/d-ai-dock.png' });
  await p.keyboard.press('Control+k'); await p.waitForTimeout(300); R.push(['ctrl k with ai open', await p.evaluate(()=>!!document.querySelector('.tr-pal'))]); await p.keyboard.press('Escape');
  // answer a full section → log today → written back to account with log
  await p.evaluate(() => { location.hash = '#hemonc-12.10' }); await p.waitForTimeout(800);
  await p.locator('#main .tile[data-sec]').nth(1).click(); await p.waitForTimeout(800);
  await p.locator('.tr-gate .btn').click(); await p.waitForTimeout(300);
  for (let i = 0; i < 12; i++) { const l = await p.evaluate(() => { const q = [...document.querySelectorAll("#main div.q[id^='q-']")].find(x => !x.querySelector('.ch:disabled')); if (!q) return 0; q.querySelector('.ch').click(); return 1 }); if (!l) break; await p.waitForTimeout(120) }
  await p.waitForTimeout(1500);
  R.push(['account doc after', await p.evaluate(() => window.__DB['data/users/u1/learn'].log)]);
  R.push(['done kept', await p.evaluate(() => Object.keys(window.__DB['data/users/u1/learn'].done))]);
  R.push(['errs', errs]);
  console.log(R.map(x => x[0] + ': ' + JSON.stringify(x[1])).join('\n'));
  await b.close();
})();
