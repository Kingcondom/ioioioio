const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 860 } }); const errs=[];p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8766/index.html#hemonc-9.11'); await p.waitForTimeout(1500);
  await p.locator('#main .tile[data-sec]').nth(5).click(); await p.waitForTimeout(800);
  const r = {};
  r.tqbar = await p.locator('#main .tqbar [data-tq="on"]').count();
  await p.locator('#main .tqbar [data-tq="on"]').first().click(); await p.waitForTimeout(200);
  r.covered = await p.evaluate(() => document.querySelectorAll('#main table.tq td.cv').length);
  r.mnemPin = await p.locator('#main a[data-mnpin]').count();
  r.secPin = await p.locator('#main a.chip.acc').count();
  r.figCover = await p.evaluate(() => document.querySelectorAll('#main .figq').length);
  await p.locator('#main [data-act="hidelec"]').first().click(); await p.waitForTimeout(300);
  r.recall = await p.evaluate(() => document.querySelectorAll('#main .rv').length);
  await p.locator('#main [data-act="hidelec"]').first().click(); await p.waitForTimeout(300);
  await p.locator('#main [data-act="markread"]').count().then(n=>r.markreadBtns=n);
  r.errs=errs; console.log(JSON.stringify(r));
  await b.close();
})();
