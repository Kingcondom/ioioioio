#!/usr/bin/env python3
"""เปิด build/index.html ด้วย Chromium จริง ตรวจว่า loader ทำงานและสลับ set ได้"""
import subprocess, sys, time, os
from playwright.sync_api import sync_playwright

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
PORT = 8931

srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", BUILD],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
fail = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 390, "height": 844})  # ขนาดมือถือ
        errs, bad = [], []
        def on_resp(r):
            if r.status >= 400:
                bad.append("%d %s" % (r.status, r.url))
        
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        pg.on("response", on_resp)
        pg.on("requestfailed", lambda r: bad.append("failed %s (%s)" % (r.url, r.failure)))
        pg.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="networkidle")

        pg.wait_for_selector("#courseTabs button", timeout=10000)
        tabs = pg.eval_on_selector_all("#courseTabs button", "els=>els.map(e=>e.textContent)")
        print("แท็บชุดวิชา:", tabs)
        if len(tabs) != 5:
            fail.append("แท็บควรมี 5 ชุด แต่ได้ %d" % len(tabs))

        pg.wait_for_selector("aside .olec", timeout=10000)
        n = pg.eval_on_selector_all("aside .olec", "els=>els.length")
        print("AIR outline: %d คาบ" % n)
        if n != 3:
            fail.append("AIR ควรมี 3 คาบ ได้ %d" % n)

        ring = pg.inner_text("#ring")
        print("แถบความคืบหน้า:", ring.replace("\n", " "))
        if "/36" not in ring:   # AIR = 9+9+18 หัวข้อ (แถบนี้นับเฉพาะชุดที่เปิดอยู่)
            fail.append("ความคืบหน้าของ AIR ควรเป็น 36 หัวข้อ ได้: %r" % ring)

        # สลับไป Cardio → ต้องโหลดไฟล์ใหม่แล้วแสดงคาบครบตามไฟล์ data
        import json as _j
        ncar = len(_j.load(open(os.path.join(BUILD, "data", "cardio.json"), encoding="utf-8")))
        pg.click("#courseTabs button:has-text('Cardio')")
        pg.wait_for_function("document.querySelectorAll('aside .olec').length===%d" % ncar, timeout=10000)
        print("Cardio outline: %d คาบ ✓" % ncar)

        # เปิดคาบแรก → หัวข้อย่อย → ตอบข้อสอบ 1 ข้อ
        pg.click("aside .olec > button")
        pg.wait_for_selector("aside .osec li button", timeout=5000)
        pg.click("aside .osec li button")
        pg.wait_for_selector("main .card", timeout=5000)
        title = pg.inner_text("main .card h2")
        print("เปิดหัวข้อ:", title[:60])

        if pg.query_selector(".ch"):
            pg.click(".ch")
            pg.wait_for_selector(".verdict", timeout=5000)
            print("ตอบข้อสอบ → เฉลยขึ้น:", pg.inner_text(".verdict")[:40])
        else:
            fail.append("ไม่พบตัวเลือกข้อสอบในหัวข้อแรก")

        # รีโหลด → progress ต้องยังอยู่ (localStorage)
        pg.reload(wait_until="networkidle")
        pg.wait_for_selector("aside .olec", timeout=10000)
        kept = pg.evaluate("localStorage.getItem('med421-learn-v1')!==null")
        cur = pg.eval_on_selector_all("#courseTabs button.on", "e=>e.map(x=>x.textContent)")
        print("หลังรีโหลด: localStorage คงอยู่ =", kept, "| แท็บปัจจุบัน =", cur)
        if not kept:
            fail.append("localStorage ไม่ถูกบันทึก")
        if cur != ["Cardio"]:
            fail.append("ไม่ได้กลับมาที่ Cardio หลังรีโหลด ได้ %r" % cur)

        # ไม่มี horizontal scroll ที่ความกว้างมือถือ
        ov = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
        print("ล้นแนวนอนที่ 390px:", ov, "px")
        if ov > 1:
            fail.append("หน้าล้นแนวนอน %dpx" % ov)

        pg.screenshot(path=os.path.join(os.path.dirname(BUILD), "check-mobile.png"), full_page=False)

        # กรอง Google Fonts / favicon ที่ container บล็อกอยู่แล้ว ไม่เกี่ยวกับ refactor
        ours = [x for x in bad if "fonts.googleapis" not in x and "fonts.gstatic" not in x
                and not x.endswith("favicon.ico") and "favicon.ico" not in x]
        print("คำขอที่ล้มเหลวทั้งหมด:", bad)
        if ours:
            fail.append("คำขอของหน้าเราล้มเหลว: %r" % ours)
        real = [e for e in errs if "ERR_CERT" not in e and "404" not in e]
        if real:
            fail.append("console error: %r" % real[:5])
        b.close()
finally:
    srv.terminate()

print()
if fail:
    print("❌ ไม่ผ่าน:")
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("✅ ผ่านทุกข้อ")
