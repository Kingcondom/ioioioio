#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เปิดคาบหนึ่งในเบราว์เซอร์จริง (จอมือถือ 390px) แล้วไล่กดทุกหัวข้อ

    python3 artifact/tools/check_render.py id 5/10

ตรวจทุกหัวข้อ: โหลดได้ · ไม่มี ** ค้างบนจอ · ไม่ล้นแนวนอน · ไม่มี page error · แท็บ MEQ/OSCE เปิดได้ ·
ภาพประกอบ (SVG): ข้อความ/รูปทรงไม่หลุดกรอบภาพ · ข้อความไม่ทับกัน

    python3 artifact/tools/check_render.py nephro 14 --shots /tmp/x   # + ถ่ายภาพประกอบทุกภาพ (โหมดสว่างและมืด กว้าง 860px) ไว้ดูด้วยตา
ต้อง `pip install playwright` ก่อน (ห้ามรัน playwright install — ใช้ Chromium ที่มีอยู่)"""
import os, subprocess, sys, time
from playwright.sync_api import sync_playwright
import json

ART = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SET, LEC = sys.argv[1], sys.argv[2]
SHOTS = sys.argv[sys.argv.index("--shots") + 1] if "--shots" in sys.argv else None
FIGJS = """() => Array.from(document.querySelectorAll('main .fig svg')).map((s, k) => {
  const R = s.getBoundingClientRect(), sc = R.width / s.viewBox.baseVal.width, out = [];
  const T = Array.from(s.querySelectorAll('text')).map(e => [e, e.getBoundingClientRect()]);
  s.querySelectorAll('text,rect,circle,ellipse,path,line,polyline,polygon').forEach(e => {
    const b = e.getBoundingClientRect(), tol = 2 * sc + 1;
    if (b.width + b.height === 0) return;
    if (b.left < R.left - tol || b.top < R.top - tol || b.right > R.right + tol || b.bottom > R.bottom + tol)
      out.push('หลุดกรอบ ' + e.tagName + ' ' + (e.textContent || '').trim().slice(0, 24));
  });
  for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) {
    const a = T[i][1], b = T[j][1], ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
    if (ox > 3 * sc && oy > 0.4 * Math.min(a.height, b.height)) out.push('ข้อความทับ: ' + T[i][0].textContent.trim().slice(0, 18) + ' × ' + T[j][0].textContent.trim().slice(0, 18));
  }
  return out;
})"""
idx = json.load(open(os.path.join(ART, "data", "index.json"), encoding="utf-8"))
meta = [m for m in idx if m["set"] == SET][0]
lecs = [l["lec"] for l in json.load(open(os.path.join(ART, meta["file"]), encoding="utf-8"))]
I = lecs.index(LEC)
CHROME = next((p for p in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "/opt/pw-browsers/chromium"] if os.path.exists(p)), None)
PORT = 8934
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", ART], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
errs, bad = [], []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"]) if CHROME else p.chromium.launch(args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 390, "height": 844})
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="networkidle")
        pg.click("#courseTabs button:has-text('%s')" % meta["label"])
        pg.wait_for_function("document.querySelectorAll('aside .olec').length===%d" % len(lecs), timeout=10000)
        pg.query_selector_all("aside .olec > button")[I].click(); pg.wait_for_timeout(400)
        n = len(pg.query_selector_all("aside .olec")[I].query_selector_all(".osec li button"))
        for i in range(n):
            pg.query_selector_all("aside .olec")[I].query_selector_all(".osec li button")[i].click()
            pg.wait_for_selector("main .card h2")
            raw = pg.evaluate("document.querySelector('main').innerText.includes('**')")
            ov = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
            q = len(pg.query_selector_all(".q"))
            flag = []
            figs = pg.evaluate(FIGJS)
            for k, fb in enumerate(figs):
                for x in fb[:4]: flag.append("ภาพ %d %s" % (k + 1, x))
            if raw: flag.append("มี ** ค้าง")
            if ov > 1: flag.append("ล้น %dpx" % ov)
            if q == 0: flag.append("ไม่มีข้อสอบ")
            if flag: bad.append("หัวข้อ %d: %s" % (i + 1, ", ".join(flag)))
            print("%2d %-45s ข้อ %2d ตาราง %d ภาพ %d %s" % (i + 1, pg.inner_text("main .card h2")[:45], q,
                  len(pg.query_selector_all("main table")), len(figs), "✗ " + ", ".join(flag) if flag else "✓"))
        if SHOTS:
            os.makedirs(SHOTS, exist_ok=True)
            pg.set_viewport_size({"width": 860, "height": 1000})
            for i in range(n):
                pg.query_selector_all("aside .olec")[I].query_selector_all(".osec li button")[i].click()
                pg.wait_for_selector("main .card h2")
                for theme in ("light", "dark"):
                    for _ in range(3):  # กดปุ่มโหมดสีจริง (ปุ่มเรียก applyAccent ให้สีประจำชุดเปลี่ยนตาม)
                        if pg.evaluate("document.documentElement.getAttribute('data-theme')") == theme: break
                        pg.click("#themeBtn")
                    for k, el in enumerate(pg.query_selector_all("main .fig")):
                        el.screenshot(path=os.path.join(SHOTS, "s%02d-f%d-%s.png" % (i + 1, k + 1, theme)))
            while pg.evaluate("document.documentElement.getAttribute('data-theme')"):
                pg.click("#themeBtn")
            pg.set_viewport_size({"width": 390, "height": 844})
            print("ภาพประกอบถ่ายไว้ที่", SHOTS)
        for tab in ("MEQ", "OSCE"):
            pg.click("#tabs button:has-text('%s')" % tab); pg.wait_for_timeout(300)
            print("%s: %d รายการในชุดนี้" % (tab, len(pg.query_selector_all(".tile"))))
        b.close()
finally:
    srv.terminate()
if errs: bad.append("page error: %r" % errs[:3])
print("\n" + ("✅ แสดงผลถูกทุกหัวข้อ" if not bad else "❌ " + " · ".join(bad)))
sys.exit(1 if bad else 0)
