#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เปิดคาบหนึ่งในเบราว์เซอร์จริง (จอมือถือ 390px) แล้วไล่กดทุกหัวข้อ

    python3 artifact/tools/check_render.py id 5/10

ตรวจทุกหัวข้อ: โหลดได้ · ไม่มี ** ค้างบนจอ · ไม่ล้นแนวนอน · ไม่มี page error · แท็บ MEQ/OSCE เปิดได้
ต้อง `pip install playwright` ก่อน (ห้ามรัน playwright install — ใช้ Chromium ที่มีอยู่)"""
import os, subprocess, sys, time
from playwright.sync_api import sync_playwright
import json

ART = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SET, LEC = sys.argv[1], sys.argv[2]
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
            if raw: flag.append("มี ** ค้าง")
            if ov > 1: flag.append("ล้น %dpx" % ov)
            if q == 0: flag.append("ไม่มีข้อสอบ")
            if flag: bad.append("หัวข้อ %d: %s" % (i + 1, ", ".join(flag)))
            print("%2d %-45s ข้อ %2d ตาราง %d %s" % (i + 1, pg.inner_text("main .card h2")[:45], q,
                  len(pg.query_selector_all("main table")), "✗ " + ", ".join(flag) if flag else "✓"))
        for tab in ("MEQ", "OSCE"):
            pg.click("#tabs button:has-text('%s')" % tab); pg.wait_for_timeout(300)
            print("%s: %d รายการในชุดนี้" % (tab, len(pg.query_selector_all(".tile"))))
        b.close()
finally:
    srv.terminate()
if errs: bad.append("page error: %r" % errs[:3])
print("\n" + ("✅ แสดงผลถูกทุกหัวข้อ" if not bad else "❌ " + " · ".join(bad)))
sys.exit(1 if bad else 0)
