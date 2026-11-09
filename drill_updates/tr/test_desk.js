/* คอม 1200 / 1440 / 1920 · สว่าง/มืด — node test_desk.js <url index.html> <โฟลเดอร์ภาพ>
   แถบซ้าย/แถบขวา · Ctrl K · ซ่อนแถบ [ ] (จำค่าหลังรีโหลด) · ขนาดเนื้อหา - = · ดับเบิลคลิก = วงล้อ · ตอบข้อ · ปุ่มปัก */
const { chromium } = require('playwright');
const U = process.argv[2] || 'http://localhost:8767/index.html', OUT = process.argv[3] || '.';
const R = []; let bad = 0;
function ok(name, cond, info) { R.push((cond ? 'PASS ' : 'FAIL ') + name + (info !== undefined ? ' : ' + JSON.stringify(info) : '')); if (!cond) bad++; }
(async () => {
  const b = await chromium.launch();
  for (const W of [1200, 1440, 1920]) for (const T of ['light', 'dark']) {
    const N = W + ' ' + T;
    const ctx = await b.newContext({ viewport: { width: W, height: 900 }, colorScheme: T });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push('pageerror ' + e.message));
    p.on('console', m => { if (m.type() === 'error' && !/fonts|ERR_|404|Failed to load/.test(m.text())) errs.push('console ' + m.text()); });
    const sw = () => p.evaluate(() => document.documentElement.scrollWidth);
    await p.goto(U); await p.waitForTimeout(1200);
    const L = await p.evaluate(() => ({ side: getComputedStyle(document.querySelector('.tr-side')).display, dock: getComputedStyle(document.querySelector('.tr-dock')).display, bnav: getComputedStyle(document.querySelector('.tr-bnav')).display, sets: document.querySelectorAll('.tr-sd-c').length, week: getComputedStyle(document.querySelector('.tr-week')).display }));
    ok(N + ' layout', L.side === 'flex' && L.bnav === 'none' && L.sets === 12 && L.week !== 'none' && (W >= 1400 ? L.dock === 'flex' : L.dock === 'none'), L);
    ok(N + ' home no overflow', (await sw()) <= W, await sw());
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-home.png` });
    // Ctrl K → ค้นหา → เปิดข้อ
    await p.keyboard.press('Control+k'); await p.waitForTimeout(300);
    await p.keyboard.type('tamponade'); await p.waitForTimeout(300);
    const nres = await p.evaluate(() => document.querySelectorAll('.tr-pal-list li button').length);
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-search.png` });
    await p.keyboard.press('Enter'); await p.waitForTimeout(900);
    const j = await p.evaluate(() => { const f = document.querySelector('#stream .tr-flash'); return { view: document.body.dataset.view, flash: f ? f.id : '', pal: !!document.querySelector('.tr-pal') }; });
    ok(N + ' Ctrl K search → item', nres > 0 && j.view === 'drill' && /^it-/.test(j.flash) && !j.pal, [nres, j]);
    // ตอบข้อที่ค้นเจอ (ถ้าเป็น MCQ) + ปุ่มปัก
    const it = await p.evaluate(() => { const a = document.querySelector('#stream .tr-flash'); return { mcq: !!(a && a.querySelector('.choice')), pin: !!(a && a.querySelector('a[href*="BRsYSzd35"]')) }; });
    if (it.mcq) { await p.locator('#stream .tr-flash .choice').first().click(); await p.waitForTimeout(500); }
    ok(N + ' answer + pin on found item', it.mcq && it.pin && await p.evaluate(() => !!document.querySelector('#stream .verdict')), it);
    // ปุ่มปัก → แถบขวาจำไว้ (กดแล้วเปิดแท็บใหม่ ปิดทิ้ง)
    if (W >= 1400) {
      const [pop] = await Promise.all([ctx.waitForEvent('page').catch(() => null), p.locator('#stream .item a[href*="BRsYSzd35"]').first().click()]);
      if (pop) await pop.close(); await p.waitForTimeout(300);
      ok(N + ' pin recorded in dock', await p.evaluate(() => document.querySelectorAll('.tr-dock .tr-pn').length === 1));
    }
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-drill.png` });
    ok(N + ' drill no overflow', (await sw()) <= W, await sw());
    // ขนาดเนื้อหา
    await p.locator('body').press('=');
    ok(N + ' content size =', await p.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--fz').trim() === '1.1'));
    await p.locator('body').press('-');
    // ซ่อนแถบซ้าย/ขวา
    const w0 = await p.evaluate(() => document.getElementById('stream').getBoundingClientRect().width);
    await p.locator('body').press('['); if (W >= 1400) await p.locator('body').press(']'); await p.waitForTimeout(500);
    const w1 = await p.evaluate(() => document.getElementById('stream').getBoundingClientRect().width);
    const hid = await p.evaluate(() => ({ s: document.documentElement.classList.contains('tr-noside'), d: document.documentElement.classList.contains('tr-nodock'), rail: getComputedStyle(document.querySelector('.tr-rail-l')).display }));
    ok(N + ' hide panels widens content', hid.s && hid.rail === 'flex' && (W < 1400 || hid.d) && w1 > w0 + 100, [w0, w1, hid]);
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-nopanes.png` });
    ok(N + ' no overflow (panes hidden)', (await sw()) <= W, await sw());
    await p.reload(); await p.waitForTimeout(1000);
    ok(N + ' panes remembered', await p.evaluate(() => document.documentElement.classList.contains('tr-noside')));
    await p.click('.tr-rail-l'); if (W >= 1400) await p.click('.tr-rail-r'); await p.waitForTimeout(400);
    ok(N + ' panes restored', await p.evaluate(() => !document.documentElement.classList.contains('tr-noside') && !document.documentElement.classList.contains('tr-nodock')));
    // ดับเบิลคลิกพื้นที่ว่าง → วงล้อคาบ
    await p.goto(U); await p.waitForTimeout(900);
    ok(N + ' view remembered after reload', await p.evaluate(() => document.body.dataset.view === 'drill'));
    await p.click('.tr-sd-nav [data-trpage=home]'); await p.waitForTimeout(500);
    const hb = await p.locator('.tr-whead').boundingBox();
    await p.mouse.dblclick(hb.x + hb.width / 2, hb.y + hb.height / 2); await p.waitForTimeout(700);
    ok(N + ' dblclick wheel', await p.evaluate(() => !!document.querySelector('.tr-wheel.on')));
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-wheel.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(400);
    // ทางลัดจากแถบซ้าย
    await p.click('.tr-sd-plus'); await p.waitForTimeout(600);
    ok(N + ' radial from sidebar', await p.evaluate(() => document.querySelectorAll('.tr-rm.on .tr-rm-it').length === 12));
    await p.screenshot({ path: `${OUT}/d-${W}-${T}-radial.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(300);
    // เลือกระบบจากแถบซ้าย
    await p.locator('.tr-sd-c').nth(4).click(); await p.waitForTimeout(500);
    ok(N + ' sidebar set', await p.evaluate(() => JSON.parse(localStorage.getItem('med421-drill-v1')).set === 'air'));
    ok(N + ' no page errors', errs.length === 0, errs);
    await ctx.close();
  }
  console.log(R.join('\n')); console.log(bad ? bad + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(bad ? 1 : 0);
})();
