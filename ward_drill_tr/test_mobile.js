/* มือถือ 390 px · สว่าง/มืด — node test_mobile.js <url index.html> <โฟลเดอร์ภาพ> */
const { chromium } = require('playwright');
const U = process.argv[2] || 'http://localhost:8767/index.html', OUT = process.argv[3] || '.';
const R = []; let bad = 0;
function ok(name, cond, info) { R.push((cond ? 'PASS ' : 'FAIL ') + name + (info !== undefined ? ' : ' + JSON.stringify(info) : '')); if (!cond) bad++; }
(async () => {
  const b = await chromium.launch();
  for (const T of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: T });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push('pageerror ' + e.message));
    p.on('console', m => { if (m.type() === 'error' && !/fonts|ERR_|404|Failed to load/.test(m.text())) errs.push('console ' + m.text()); });
    const sw = () => p.evaluate(() => document.documentElement.scrollWidth);
    await p.goto(U); await p.waitForTimeout(1200);
    const h = await p.evaluate(() => ({ view: document.body.dataset.view, hero: !!document.querySelector('.tr-hero'), cards: document.querySelectorAll('.tr-card').length, bnav: getComputedStyle(document.querySelector('.tr-bnav')).display, side: getComputedStyle(document.querySelector('.tr-side')).display, fab: getComputedStyle(document.querySelector('.aiw-fab')).display }));
    ok(T + ' home layout', h.view === 'home' && h.hero && h.cards === 12 && h.bnav !== 'none' && h.side === 'none' && h.fab === 'none', h);
    ok(T + ' home no overflow', (await sw()) <= 390, await sw());
    await p.screenshot({ path: `${OUT}/m-${T}-home.png` });
    // วงล้อทางลัด
    await p.click('.tr-main'); await p.waitForTimeout(700);
    ok(T + ' radial open', await p.evaluate(() => document.querySelectorAll('.tr-rm.on .tr-rm-it').length === 12));
    await p.screenshot({ path: `${OUT}/m-${T}-radial.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(300);
    ok(T + ' radial closed', await p.evaluate(() => !document.querySelector('.tr-rm')));
    // หน้าต่างระบบ → เลือกคาบ
    await p.locator('.tr-card').nth(0).click(); await p.waitForTimeout(600);
    ok(T + ' set sheet', await p.evaluate(() => document.querySelector('.tr-sheet').open && document.querySelectorAll('.tr-sh-list button').length > 3));
    await p.screenshot({ path: `${OUT}/m-${T}-sheet.png` });
    await p.locator('.tr-sh-list button').first().click(); await p.waitForTimeout(800);
    const d = await p.evaluate(() => ({ view: document.body.dataset.view, items: document.querySelectorAll('#stream .item').length, mcq: [...document.querySelectorAll('#stream .item')].filter(x => x.querySelector('.choice')).length, filt: document.querySelector('.tr-filt span').textContent, pins: [...document.querySelectorAll('#stream .item a[href*="BRsYSzd35"]')].filter(a => /#q-[A-Z]/.test(a.href) && a.target === '_blank').length }));
    ok(T + ' drill view from sheet', d.view === 'drill' && d.items > 0 && /^Lec 04/.test(d.filt), d);
    ok(T + ' pin buttons on every MCQ (as before)', d.mcq > 0 && d.pins === d.mcq, d);
    ok(T + ' drill no overflow', (await sw()) <= 390, await sw());
    // ตัวกรอง = แถบ rail เดิมย้ายเข้า sheet แล้วคืนที่เดิม
    await p.click('.tr-filt'); await p.waitForTimeout(600);
    ok(T + ' filter sheet has rail', await p.evaluate(() => !!document.querySelector('.tr-sheet[open] #lecbar .lec') && !!document.querySelector('.tr-sheet[open] #btn-reveal')));
    await p.screenshot({ path: `${OUT}/m-${T}-filter.png` });
    await p.locator('.tr-sheet #lecbar .lec').nth(2).click(); await p.waitForTimeout(800);
    ok(T + ' filter picks lecture + rail restored', await p.evaluate(() => !document.querySelector('.tr-sheet').open && !!document.querySelector('.shell>.rail #lecbar') && /^Lec 10/.test(document.querySelector('.tr-filt span').textContent)), await p.evaluate(() => document.querySelector('.tr-filt span').textContent));
    // ตอบข้อแรก
    await p.locator('#stream .item').first().locator('.choice').first().click(); await p.waitForTimeout(500);
    const a = await p.evaluate(() => { const s = JSON.parse(localStorage.getItem('med421-drill-v1')); const k = Object.keys(s.log || {}); return { verdict: !!document.querySelector('#stream .item .verdict'), panel: !!document.querySelector('#stream .item .panel'), answers: Object.keys(s.answers).length, log: k.length ? s.log[k[0]].length : 0 }; });
    ok(T + ' answer works + logged today', a.verdict && a.panel && a.answers === 1 && a.log === 1, a);
    await p.screenshot({ path: `${OUT}/m-${T}-answered.png` });
    // ปัดซ้าย → คาบถัดไป
    const cdp = await ctx.newCDPSession(p);
    async function swipe(x0, x1, y) { await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: x0, y }] }); for (const x of [x0 + (x1 - x0) / 3, x0 + 2 * (x1 - x0) / 3, x1]) { await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: y + 4 }] }); await p.waitForTimeout(20); } await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await p.waitForTimeout(700); }
    await p.evaluate(() => window.scrollTo(0, 0));
    const before = await p.evaluate(() => document.querySelector('.tr-filt span').textContent);
    await swipe(340, 120, 300);
    const after = await p.evaluate(() => document.querySelector('.tr-filt span').textContent);
    ok(T + ' swipe next lecture', before !== after && /^Lec 13/.test(after), [before, after]);
    // หน้าแรก: วงแหวนนับ 1
    await p.locator('.tr-bn').first().click(); await p.waitForTimeout(600);
    ok(T + ' ring counts today', await p.evaluate(() => document.querySelector('.tr-ring-in b').textContent === '1/20'), await p.evaluate(() => document.querySelector('.tr-ring-in b').textContent));
    // ปัดบนหน้าแรก = เปลี่ยนระบบ
    await swipe(340, 120, 420);
    ok(T + ' home swipe → next set', await p.evaluate(() => document.querySelector('.tr-card.cur .tr-c-no').textContent === 'Nephro'));
    await swipe(120, 340, 420);
    // กดค้าง 2 วิ → วงล้อสลับคาบ
    await p.evaluate(() => window.scrollTo(0, 0));
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 300, y: 60 }] });
    await p.waitForTimeout(2300);
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await p.waitForTimeout(700);
    ok(T + ' long press wheel', await p.evaluate(() => !!document.querySelector('.tr-wheel.on')));
    await p.screenshot({ path: `${OUT}/m-${T}-wheel.png` });
    await p.locator('.tr-wh-it.on .tr-wh-chip').click(); await p.waitForTimeout(900);
    ok(T + ' wheel opens lecture', await p.evaluate(() => document.body.dataset.view === 'drill' && !document.querySelector('.tr-wheel')));
    // สุ่มสอบ
    await p.locator('.tr-bn').nth(3).click(); await p.waitForTimeout(600);
    await p.click('.qzgo'); await p.waitForTimeout(700);
    const q = await p.evaluate(() => ({ n: document.querySelectorAll('#stream .item').length, pins: document.querySelectorAll('#stream .item a[href*="BRsYSzd35"]').length }));
    await p.locator('#stream .item').first().locator('.choice').first().click(); await p.waitForTimeout(500);
    const q2 = await p.evaluate(() => ({ verdict: !!document.querySelector('#stream .item .verdict'), quizAns: Object.keys(JSON.parse(localStorage.getItem('med421-drill-quiz')).ans).length }));
    ok(T + ' quiz draws + answers', q.n === 20 && q.pins === 20 && q2.verdict && q2.quizAns === 1, [q, q2]);
    await p.screenshot({ path: `${OUT}/m-${T}-quiz.png` });
    // ข้อที่ผิดจากวงล้อทางลัด
    await p.click('.tr-main'); await p.waitForTimeout(600);
    await p.locator('.tr-rm-it').nth(6).click({ force: true }); await p.waitForTimeout(900);
    ok(T + ' radial → wrong quiz', await p.evaluate(() => { const q = JSON.parse(localStorage.getItem('med421-drill-quiz')); return q.pool === 'wrong' || document.querySelector('.tr-toast.on') !== null; }));
    // คลังเก่าจากทางลัด (ข้อเก่ามีปุ่มปัก)
    await p.click('.tr-main'); await p.waitForTimeout(600);
    await p.locator('.tr-rm-it').nth(1).click({ force: true }); await p.waitForTimeout(900);
    ok(T + ' radial → old bank with pins', await p.evaluate(() => JSON.parse(localStorage.getItem('med421-drill-v1')).mode === 'old' && document.querySelectorAll('#stream .olditem-mcq a[href*="BRsYSzd35"]').length > 0));
    // ทวนแล้ว
    await p.locator('.tr-bn').nth(4).click(); await p.waitForTimeout(600);
    ok(T + ' review tab', await p.evaluate(() => JSON.parse(localStorage.getItem('med421-drill-v1')).mode === 'review' && document.querySelector('.tr-bn[aria-current=page] .tr-bn-t').textContent === 'ทวนแล้ว'));
    // ขนาดเนื้อหา
    await p.locator('.tr-bn').nth(1).click(); await p.waitForTimeout(500);
    await p.click('.tr-tools [data-trfz="1"]'); await p.waitForTimeout(300);
    ok(T + ' content size +', await p.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--fz').trim() === '1.1' && localStorage.getItem('med421-drill-fz') === '1.1'));
    ok(T + ' final no overflow', (await sw()) <= 390, await sw());
    ok(T + ' no page errors', errs.length === 0, errs);
    await ctx.close();
  }
  console.log(R.join('\n')); console.log(bad ? bad + ' FAILED' : 'ALL PASS');
  await b.close(); process.exit(bad ? 1 : 0);
})();
