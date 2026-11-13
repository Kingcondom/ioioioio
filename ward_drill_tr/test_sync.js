/* ซิงก์บัญชี: เอกสาร data/users/u1/drill มีคำตอบ + log ของอีกเครื่อง · เครื่องนี้มีคำตอบใน localStorage
   → รวมกันถูก (คำตอบเดิมไม่หาย) และเขียนกลับขึ้นบัญชีพร้อม log — node test_sync.js <url index.html> */
const { chromium } = require('playwright');
const U = process.argv[2] || 'http://localhost:8767/index.html';
const STUB = `(function(){
  var DB={"data/users/u1/drill":{answers:{"C-MCQ-02":{pick:4,ok:true},"N-MCQ-01":{pick:0,ok:false}},shown:{"C-MEQ-01#0":1},log:{"2026-11-08":["C-MCQ-02","N-MCQ-01"]},v:1}};
  window.__DB=DB;window.__W=0;
  function snap(p){var d=DB[p];return{exists:!!d,data:function(){return JSON.parse(JSON.stringify(d||{}))},metadata:{hasPendingWrites:false}}}
  function doc(p){return{onSnapshot:function(cb){setTimeout(function(){cb(snap(p))},60);return function(){}},
    set:function(v){DB[p]=JSON.parse(JSON.stringify(v));window.__W++;return Promise.resolve()}}}
  var smp=function(m,o){var t="ตัวอย่างคำตอบ";o&&o.onText&&o.onText({text:t});return Promise.resolve({text:t})};
  window.claude={use:function(n){return n==="db"?Promise.resolve({doc:doc}):n==="user"?Promise.resolve({id:function(){return Promise.resolve("u1")}}):n==="sample"?Promise.resolve(smp):Promise.reject(new Error("no"))}};
})();`;
const R = []; let bad = 0;
function ok(name, cond, info) { R.push((cond ? 'PASS ' : 'FAIL ') + name + (info !== undefined ? ' : ' + JSON.stringify(info) : '')); if (!cond) bad++; }
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.addInitScript(STUB);
  /* เครื่องนี้เคยตอบไว้ 1 ข้อแบบยังไม่ได้ซิงก์ (เก็บด้วยคีย์เดิม med421-drill-v1 รูปแบบเดิมที่ไม่มี log) */
  await p.addInitScript(() => { if (!sessionStorage.getItem('seeded')) { sessionStorage.setItem('seeded', '1'); localStorage.setItem('med421-drill-v1', JSON.stringify({ answers: { 'C-MCQ-01': { pick: 3, ok: true } }, shown: {}, set: 'cardio', mode: 'new' })); localStorage.setItem('med421-drill-v1:sync', JSON.stringify({ cloud: true, pend: true, uid: 'u1' })); } });
  await p.goto(U); await p.waitForTimeout(2200);
  const s1 = await p.evaluate(() => { const l = JSON.parse(localStorage.getItem('med421-drill-v1')); return { answers: Object.keys(l.answers).sort(), log: l.log, shown: Object.keys(l.shown), sync: document.getElementById('lsync').textContent.trim(), side: document.querySelector('.tr-side .tr-syncm span').textContent }; });
  ok('merge keeps both devices answers', JSON.stringify(s1.answers) === JSON.stringify(['C-MCQ-01', 'C-MCQ-02', 'N-MCQ-01']), s1.answers);
  ok('log from account adopted', s1.log && s1.log['2026-11-08'] && s1.log['2026-11-08'].length === 2, s1.log);
  ok('shown kept', s1.shown[0] === 'C-MEQ-01#0', s1.shown);
  ok('sync label mirrored', s1.sync === 'บันทึกในบัญชี' && s1.side === s1.sync, [s1.sync, s1.side]);
  const acc = await p.evaluate(() => window.__DB['data/users/u1/drill']);
  ok('merged state written back', Object.keys(acc.answers).length === 3 && acc.log['2026-11-08'].length === 2, acc);
  /* ตอบข้อใหม่วันนี้ → log วันนี้ขึ้นบัญชี */
  await p.evaluate(() => { location.hash = '#cardio-10'; }); await p.waitForTimeout(800);
  await p.locator('#stream .item').first().locator('.choice').nth(1).click(); await p.waitForTimeout(1600);
  const acc2 = await p.evaluate(() => { const d = window.__DB['data/users/u1/drill'], t = new Date(), k = t.getFullYear() + '-' + String(t.getMonth() + 1).padStart(2, '0') + '-' + String(t.getDate()).padStart(2, '0'); return { today: d.log[k], prev: d.log['2026-11-08'], n: Object.keys(d.answers).length, ring: null }; });
  ok('today log synced to account', acc2.today && acc2.today.length === 1 && acc2.prev.length === 2 && acc2.n === 4, acc2);
  /* "เฉลยทั้งหมด" ไม่นับเป็นข้อที่ทำเอง */
  await p.click('#btn-reveal'); await p.waitForTimeout(1200);
  const acc3 = await p.evaluate(() => { const d = window.__DB['data/users/u1/drill'], k = Object.keys(d.log).sort().pop(); return d.log[k].length; });
  ok('reveal-all not counted as done', acc3 === 1, acc3);
  await p.click('.tr-sd-nav [data-trpage=home]'); await p.waitForTimeout(500);
  ok('home ring reads account log', await p.evaluate(() => document.querySelector('.tr-ring-in b').textContent === '1/20'));
  ok('7-day bars show yesterday', await p.evaluate(() => [...document.querySelectorAll('.tr-bars b')].map(x => +x.textContent).reduce((a, x) => a + x, 0) >= 1));
  ok('no page errors', errs.length === 0, errs);
  console.log(R.join('\n')); console.log(bad ? bad + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(bad ? 1 : 0);
})();
