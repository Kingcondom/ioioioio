const { chromium } = require('playwright');
const OUT = process.argv[2];
const U = 'http://localhost:8766/index.html';
(async () => {
  const b = await chromium.launch();
  const R = [];
  for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: scheme });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push('pageerror ' + e.message)); p.on('console', m => { if (m.type() === 'error' && !/fonts|ERR_|404/.test(m.text())) errs.push('console ' + m.text()); });
    await p.goto(U + '#hemonc'); await p.waitForTimeout(1500);
    const T = scheme;
    await p.screenshot({ path: `${OUT}/m-${T}-home.png` });
    R.push([T + ' home', await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, hero: !!document.querySelector('.tr-hero'), cards: document.querySelectorAll('.tr-card').length, bnav: getComputedStyle(document.querySelector('.tr-bnav')).display, side: getComputedStyle(document.querySelector('.tr-side')).display, view: document.body.dataset.view }))]);
    // radial
    await p.click('.tr-main'); await p.waitForTimeout(700);
    await p.screenshot({ path: `${OUT}/m-${T}-radial.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(300);
    // sheet
    await p.locator('.tr-card').nth(2).click(); await p.waitForTimeout(700);
    await p.screenshot({ path: `${OUT}/m-${T}-sheet.png` });
    R.push([T + ' sheet open', await p.evaluate(() => document.querySelector('.tr-sheet').open)]);
    // open first topic from sheet
    await p.locator('.tr-sh-list button').first().click(); await p.waitForTimeout(900);
    R.push([T + ' section', await p.evaluate(() => ({ view: document.body.dataset.view, gate: !!document.querySelector('.tr-gate'), qHidden: [...document.querySelectorAll('#main div.q[id^=q-]')].every(q => q.offsetParent === null), nav: !!document.querySelector('#main .quiz .nav') && document.querySelector('#main .quiz .nav').offsetParent !== null }))]);
    await p.evaluate(() => document.querySelector('.tr-gate').scrollIntoView({ block: 'center' })); await p.waitForTimeout(300);
    await p.screenshot({ path: `${OUT}/m-${T}-gate.png` });
    await p.locator('.tr-gate .btn').click(); await p.waitForTimeout(700);
    // answer all questions of this section (first choice)
    for (let i = 0; i < 12; i++) {
      const left = await p.evaluate(() => { const q = [...document.querySelectorAll('#main div.q[id^=q-]')].find(x => !x.querySelector('.ch:disabled')); if (!q) return 0; q.querySelector('.ch').click(); return 1; });
      if (!left) break; await p.waitForTimeout(150);
    }
    R.push([T + ' after answers', await p.evaluate(() => ({ log: JSON.parse(localStorage.getItem('med421-learn-v1')).log }))]);
    await p.screenshot({ path: `${OUT}/m-${T}-answered.png` });
    // swipe → next section
    const before = await p.evaluate(() => document.querySelector('#main h2') && document.querySelector('#main h2').textContent);
    const cdp = await ctx.newCDPSession(p);
    await p.evaluate(() => window.scrollTo(0, 0));
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 330, y: 140 }] });
    for (const x of [280, 200, 120]) { await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: 145 }] }); await p.waitForTimeout(20); }
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await p.waitForTimeout(700);
    const afterT = await p.evaluate(() => document.querySelector('#main h2') && document.querySelector('#main h2').textContent);
    R.push([T + ' swipe next section', before !== afterT, afterT && afterT.slice(0, 40)]);
    // home ring
    await p.locator('.tr-bn').first().click(); await p.waitForTimeout(700);
    R.push([T + ' ring', await p.evaluate(() => document.querySelector('.tr-ring-in b').textContent)]);
    await p.screenshot({ path: `${OUT}/m-${T}-home2.png` });
    // long press → wheel
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 200, y: 560 }] });
    await p.waitForTimeout(2300);
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await p.waitForTimeout(700);
    R.push([T + ' wheel', await p.evaluate(() => !!document.querySelector('.tr-wheel.on'))]);
    await p.screenshot({ path: `${OUT}/m-${T}-wheel.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(400);
    // MEQ page
    await p.locator('.tr-bn').nth(3).click(); await p.waitForTimeout(700);
    R.push([T + ' meq seg', await p.evaluate(() => !!document.querySelector('.tr-seg') && document.body.dataset.view)]);
    await p.locator('.tr-seg button').nth(1).click(); await p.waitForTimeout(500);
    R.push([T + ' osce', await p.evaluate(() => document.body.dataset.view)]);
    // review
    await p.locator('.tr-bn').nth(4).click(); await p.waitForTimeout(500);
    R.push([T + ' review', await p.evaluate(() => document.body.dataset.view)]);
    R.push([T + ' sw final', await p.evaluate(() => document.documentElement.scrollWidth)]);
    R.push([T + ' errs', errs]);
    await ctx.close();
  }
  console.log(R.map(x => x.map(y => typeof y === 'string' ? y : JSON.stringify(y)).join(' : ')).join('\n'));
  await b.close();
})();
