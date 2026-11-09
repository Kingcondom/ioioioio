const { chromium } = require('playwright');
const OUT = process.argv[2], U = 'http://localhost:8766/index.html';
(async () => {
  const b = await chromium.launch(); const R = [];
  for (const [w, h, sc] of [[1440, 900, 'light'], [1920, 1080, 'dark'], [1200, 800, 'light']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: sc });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errs.push(m.text()) });
    await p.goto(U + '#hemonc'); await p.waitForTimeout(1500);
    await p.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto' });
    const T = w + '-' + sc;
    await p.screenshot({ path: `${OUT}/d-${T}-home.png` });
    R.push([T + ' layout', await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, side: getComputedStyle(document.querySelector('.tr-side')).display, dock: getComputedStyle(document.querySelector('.tr-dock')).display, mast: getComputedStyle(document.querySelector('.mast')).display, bnav: getComputedStyle(document.querySelector('.tr-bnav')).display, week: getComputedStyle(document.querySelector('.tr-week')).display, aside: getComputedStyle(document.getElementById('outline')).display }))]);
    if (w === 1440) {
      // Ctrl K search
      await p.keyboard.press('Control+k'); await p.waitForTimeout(400); await p.keyboard.type('gout'); await p.waitForTimeout(1500);
      await p.screenshot({ path: `${OUT}/d-${T}-search.png` });
      R.push(['search', await p.evaluate(() => ({ n: document.querySelectorAll('.tr-pal-list li button').length, first: document.querySelector('.tr-pal-list .pt') && document.querySelector('.tr-pal-list .pt').textContent.slice(0, 50), ld: document.querySelector('.tr-pal-foot .ld').textContent }))]);
      await p.keyboard.press('Enter'); await p.waitForTimeout(1500);
      R.push(['search → section', await p.evaluate(() => ({ view: document.body.dataset.view, course: document.querySelector('.tr-sd-c[aria-current=true] b') && document.querySelector('.tr-sd-c[aria-current=true] b').firstChild.textContent, h2: document.querySelector('#main h2').textContent.slice(0, 40) }))]);
      await p.screenshot({ path: `${OUT}/d-${T}-section.png` });
      // gate + keyboard
      await p.locator('.tr-gate .btn').click(); await p.waitForTimeout(500);
      await p.keyboard.press('2'); await p.waitForTimeout(400);
      R.push(['key 2 answered', await p.evaluate(() => document.querySelectorAll('#main .verdict').length)]);
      // toc toggle
      await p.locator('.tr-side [data-trtoc]').click(); await p.waitForTimeout(300);
      R.push(['toc drawer', await p.evaluate(() => getComputedStyle(document.getElementById('outline')).display + '/' + getComputedStyle(document.getElementById('outline')).position)]);
      await p.screenshot({ path: `${OUT}/d-${T}-toc.png` });
      await p.locator('.tr-side [data-trtoc]').click(); await p.waitForTimeout(200);
      // pin table capture
      const pin = p.locator('#main a[data-tqpin]').first();
      if (await pin.count()) { await pin.evaluate(a => { a.addEventListener('click', e => e.preventDefault(), { once: true }); a.click() }); await p.waitForTimeout(300); }
      R.push(['dock pins', await p.evaluate(() => document.querySelectorAll('.tr-pn').length)]);
      // present mode still works
      await p.locator('#main [data-act="present"]').first().click(); await p.waitForTimeout(500);
      R.push(['present', await p.evaluate(() => !!document.querySelector('.pv'))]);
      await p.keyboard.press('Escape'); await p.waitForTimeout(300);
      // radial on desktop
      await p.locator('.tr-sd-plus').click(); await p.waitForTimeout(600);
      await p.screenshot({ path: `${OUT}/d-${T}-radial.png` });
      await p.keyboard.press('Escape'); await p.waitForTimeout(300);
      // home + dblclick wheel
      await p.locator('.tr-side [data-trview="home"]').click(); await p.waitForTimeout(600);
      const hb = await p.locator('.tr-whead').boundingBox();
      await p.mouse.dblclick(hb.x + hb.width / 2, hb.y + hb.height / 2); await p.waitForTimeout(700);
      R.push(['dblclick wheel', await p.evaluate(() => !!document.querySelector('.tr-wheel.on'))]);
      await p.screenshot({ path: `${OUT}/d-${T}-wheel.png` });
      await p.keyboard.press('Escape'); await p.waitForTimeout(400);
      // dblclick on prose must not open wheel
      await p.evaluate(() => window.scrollTo(0, 0));
      // course switch from sidebar
      await p.locator('.tr-sd-c').first().click(); await p.waitForTimeout(1200);
      R.push(['switch AIR', await p.evaluate(() => document.querySelector('.tr-top h1').textContent)]);
      // Alt+→ course
      await p.keyboard.press('Alt+ArrowRight'); await p.waitForTimeout(1200);
      R.push(['alt→', await p.evaluate(() => document.querySelector('.tr-top h1').textContent)]);
      // lecture page view (hide mode, NL box) still renders
      await p.locator('.tr-card').first().click(); await p.waitForTimeout(500);
      await p.locator('.tr-sheet .tr-sh-acts .btn').nth(2).click(); await p.waitForTimeout(700);
      R.push(['lecture page', await p.evaluate(() => ({ view: document.body.dataset.view, nl: !!document.querySelector('#main .nlbox'), pres: !!document.querySelector('#main [data-act=present]') }))]);
    }
    R.push([T + ' sw end', await p.evaluate(() => document.documentElement.scrollWidth)]);
    R.push([T + ' errs', errs]);
    await p.close();
  }
  console.log(R.map(x => x.map(y => typeof y === 'string' ? y : JSON.stringify(y)).join(' : ')).join('\n'));
  await b.close();
})();
