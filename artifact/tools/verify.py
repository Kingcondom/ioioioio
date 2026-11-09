#!/usr/bin/env python3
"""เปิด build/index.html ด้วย Chromium จริง ตรวจว่า loader ทำงานและสลับ set ได้"""
import re, subprocess, sys, time, os
from playwright.sync_api import sync_playwright

def chromium_path():
    """หา Chromium ใน container — เลข build และชื่อโฟลเดอร์ย่อยเปลี่ยนไปตามรุ่น จึงห้ามฝังไว้"""
    import glob
    cands = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    if not cands:
        raise SystemExit("ไม่พบ Chromium ใน /opt/pw-browsers — ห้ามรัน playwright install ให้ตรวจ container")
    def build(p):
        m = re.search(r"chromium-(\d+)", p)
        return int(m.group(1)) if m else 0
    return sorted(cands, key=build)[-1]

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
PORT = 8931

srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", BUILD],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
fail = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chromium_path(), args=["--no-sandbox"])
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

        # จำนวนที่คาดหวังอ่านจากไฟล์ data เอง ไม่ฝังเลขไว้ในสคริปต์
        import json as _j0
        _idx = _j0.load(open(os.path.join(BUILD, "data", "index.json"), encoding="utf-8"))
        _first = _idx[0]
        _flec = _j0.load(open(os.path.join(BUILD, _first["file"]), encoding="utf-8"))
        _fsec = sum(len(l["sections"]) for l in _flec)

        pg.wait_for_selector("#courseTabs button", timeout=10000)
        tabs = pg.eval_on_selector_all("#courseTabs button", "els=>els.map(e=>e.textContent)")
        import json as _j
        _NSET = len(_j.load(open(os.path.join(BUILD, "data", "index.json"), encoding="utf-8")))
        print("แท็บชุดวิชา:", tabs)
        if len(tabs) != len(_idx):
            fail.append("แท็บควรมี %d ชุดตาม index.json แต่ได้ %d" % (len(_idx), len(tabs)))

        # ---- โครงหน้าแบบ Teaching Round (9 พ.ย.): หน้าแรก = การ์ดคาบ ไม่ใช่สารบัญ ----
        pg.wait_for_selector(".tr-card", timeout=10000)
        n = pg.eval_on_selector_all(".tr-card", "els=>els.length")
        print("%s หน้าแรก: %d การ์ดคาบ" % (_first["label"], n))
        if n != len(_flec):
            fail.append("%s ควรมี %d คาบ ได้ %d" % (_first["label"], len(_flec), n))
        ring = pg.inner_text(".tr-tile[data-trview='lectures']")
        print("ไทล์ความคืบหน้า:", ring.replace("\n", " "))
        if "/%d" % _fsec not in ring:   # นับเฉพาะชุดที่เปิดอยู่
            fail.append("ความคืบหน้าของ %s ควรเป็น %d หัวข้อ ได้: %r" % (_first["label"], _fsec, ring))
        if pg.eval_on_selector_all(".tr-bnav .tr-bn", "e=>e.filter(b=>b.getBoundingClientRect().height>=44).length") != 5:
            fail.append("แถบล่างควรมี 5 ปุ่ม สูงอย่างน้อย 44px")

        def slug(x):
            return re.sub(r"[^A-Za-z0-9._~-]", ".", str(x))

        def open_sec(setk, lec, sid):
            pg.evaluate("h=>{location.hash=h}", "#%s-%s" % (setk, slug(lec)))
            pg.wait_for_selector('main [data-sec="%s"]' % sid, state="visible", timeout=10000)
            pg.click('main [data-sec="%s"]' % sid)
            pg.wait_for_selector("main .card h2", timeout=5000)

        def open_quiz():
            # ข้อสอบซ่อนหลังแถบ "ทำข้อสอบท้ายหัวข้อ" จนกว่าจะอ่านจบ
            if pg.query_selector("main .tr-gate button"):
                pg.click("main .tr-gate button"); pg.wait_for_timeout(200)

        # ปิดตารางเพื่อทวน: หาหัวข้อแรกของชุดแรกที่มีตารางอย่างน้อย 2 แถวข้อมูล แล้วลองปิด/เปิด
        _target = None
        for _l in _flec:
            for _s in _l["sections"]:
                _rows = [x for x in str(_s.get("md", "")).split("\n") if x.strip().startswith("|")]
                _body = [x for x in _rows if not set(x.replace("|", "").replace(" ", "")) <= set(":-")]
                if len(_body) >= 3:
                    _target = (_l["lec"], _s["id"])
                    break
            if _target:
                break
        if not _target:
            fail.append("ไม่พบหัวข้อที่มีตารางในชุดแรก — ตรวจโหมดปิดตารางไม่ได้")
        else:
            _lec, _sid = _target
            open_sec(_first["set"], _lec, _sid)
            if pg.query_selector("main .tr-gate") and pg.eval_on_selector_all("main div.q[id^='q-']", "e=>e.filter(x=>x.offsetParent!==null).length"):
                fail.append("ยังไม่ได้กดทำข้อสอบ แต่ข้อสอบโผล่แล้ว")
            if not pg.query_selector("main .tqbar"):
                fail.append("หัวข้อ %s มีตารางแต่ไม่มีแถบปิดเพื่อทวน" % _sid)
            else:
                _tbl = "()=>{var b=document.querySelector('main .tqbar');if(!b)return null;return [].map.call(b.nextElementSibling.querySelectorAll('tbody tr'),function(r){return [].map.call(r.children,function(c){return c.textContent.trim();});});}"
                _t0 = pg.evaluate(_tbl)
                pg.eval_on_selector_all("main .tqbar button[data-tq='on']", "e=>e[0].click()")
                pg.wait_for_selector("main table.tq td.cv", timeout=5000)
                _n = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.length")
                _hints = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.map(x=>x.getAttribute('data-hint'))")
                print("ปิดตารางเพื่อทวน (%s): %d ช่อง · คำใบ้ %r" % (_sid, _n, _hints[:4]))
                if _n < 1:
                    fail.append("กดปิดเพื่อทวนแล้วไม่มีช่องถูกปิด")
                if pg.eval_on_selector_all("main table.tq tbody tr", "rs=>rs.filter(r=>r.children[0].classList.contains('cv')).length"):
                    fail.append("คอลัมน์แรกถูกปิดด้วย ควรเปิดไว้เป็นคำถาม")
                if "rgba(0, 0, 0, 0)" not in pg.eval_on_selector("main table.tq td.cv:not(.op)", "e=>getComputedStyle(e).color"):
                    fail.append("ข้อความของช่องที่ปิดยังมองเห็นได้")
                if any(x and len(x) > 10 for x in _hints):
                    fail.append("คำใบ้ยาวเกินไป: %r" % [x for x in _hints if x and len(x) > 10][:3])
                if any(x and x[0] in "ิีึืุูั่้๊๋็์ํ" for x in _hints):
                    fail.append("คำใบ้ขึ้นต้นด้วยสระหรือวรรณยุกต์ลอย")
                _kb = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.filter(x=>x.getAttribute('tabindex')!==null).length")
                if _kb != _n:
                    fail.append("ช่องที่ปิดเข้าถึงด้วยคีย์บอร์ดไม่ได้ (%d/%d)" % (_kb, _n))
                pg.eval_on_selector_all("main table.tq td.cv", "e=>e[0].click()")
                if pg.eval_on_selector_all("main table.tq td.cv.op", "e=>e.length") != 1:
                    fail.append("แตะช่องเดียวแต่เปิดไม่ใช่ 1 ช่อง")
                open_quiz()
                if pg.query_selector("main div.q[id^='q-'] .ch"):
                    pg.eval_on_selector_all("main div.q[id^='q-'] .ch", "e=>e[0].click()")
                    pg.wait_for_selector(".verdict", timeout=5000)
                    pg.wait_for_timeout(400)
                    _n2 = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.length")
                    _op2 = pg.eval_on_selector_all("main table.tq td.cv.op", "e=>e.length")
                    print("หลัง render ใหม่: ยังปิด %d ช่อง · ช่องที่เปิดไว้คงอยู่ %d" % (_n2, _op2))
                    if _n2 != _n:
                        fail.append("render ใหม่แล้วสถานะปิดตารางหาย (%d → %d)" % (_n, _n2))
                    if _op2 != 1:
                        fail.append("render ใหม่แล้วช่องที่เปิดไว้ถูกปิดกลับ")
                pg.eval_on_selector_all("main .tqbar button[data-tq='off']", "e=>e[0].click()")
                pg.wait_for_function("!document.querySelector('main table.tq td.cv')", timeout=5000)
                if pg.evaluate(_tbl) != _t0:
                    fail.append("ตารางไม่กลับมาเหมือนเดิมหลังเลิกทวน")
                else:
                    print("เลิกทวน → ตารางกลับมาเหมือนเดิม ✓")

        # สลับไป Cardio → ต้องโหลดไฟล์ใหม่แล้วแสดงการ์ดคาบครบตามไฟล์ data
        ncar = len(_j.load(open(os.path.join(BUILD, "data", "cardio.json"), encoding="utf-8")))
        # ล้าง hash ที่ใช้เปิดหัวข้อด้านบน ไม่งั้นรีโหลดแล้วหน้าจะกลับไปชุดตาม hash (พฤติกรรมลิงก์ตรงเดิม)
        pg.evaluate("()=>history.replaceState(null,'',location.pathname)")
        pg.click("#courseTabs button:has-text('Cardio')")
        pg.wait_for_function("document.querySelectorAll('.tr-card').length===%d" % ncar, timeout=10000)
        print("Cardio หน้าแรก: %d การ์ดคาบ ✓" % ncar)

        # เปิดคาบแรกจากการ์ด → หน้าต่างคาบ → หัวข้อแรก → ทำข้อสอบ 1 ข้อ
        pg.click(".tr-card")
        pg.wait_for_selector(".tr-sheet[open] .tr-sh-list button", timeout=5000)
        pg.click(".tr-sheet .tr-sh-list button")
        pg.wait_for_selector("main .card h2", timeout=5000)
        print("เปิดหัวข้อ:", pg.inner_text("main .card h2")[:60])
        open_quiz()
        if pg.query_selector("main div.q[id^='q-'] .ch"):
            pg.click("main div.q[id^='q-'] .ch")
            pg.wait_for_selector(".verdict", timeout=5000)
            print("ตอบข้อสอบ → เฉลยขึ้น:", pg.inner_text(".verdict")[:40])
        else:
            fail.append("ไม่พบตัวเลือกข้อสอบในหัวข้อแรก")

        # รีโหลด → progress ต้องยังอยู่ (localStorage)
        pg.reload(wait_until="networkidle")
        pg.wait_for_selector("main .card", timeout=10000)
        kept = pg.evaluate("localStorage.getItem('med421-learn-v1')!==null")
        cur = pg.eval_on_selector_all("#courseTabs button.on", "e=>e.map(x=>x.textContent)")
        print("หลังรีโหลด: localStorage คงอยู่ =", kept, "| แท็บปัจจุบัน =", cur)
        if not kept:
            fail.append("localStorage ไม่ถูกบันทึก")
        if cur != ["Cardio"]:
            fail.append("ไม่ได้กลับมาที่ Cardio หลังรีโหลด ได้ %r" % cur)

        # ---- ทุกความกว้าง: ไม่ล้นแนวนอน · มือถือใช้แถบล่าง · คอมใช้แถบซ้าย · คอมขยายเนื้อหาใหญ่ขึ้น ----
        pg.evaluate("()=>{location.hash='#cardio'}"); pg.wait_for_timeout(500)
        FS = """()=>{const p=[...document.querySelectorAll('main .lede,main p,main .tr-hero p')].find(x=>x.textContent.trim().length>20)||document.querySelector('main');
          const z=parseFloat(getComputedStyle(document.querySelector('.cols')).zoom)||1;
          return {fs:+(parseFloat(getComputedStyle(p).fontSize)*z).toFixed(1),
                  bnav:getComputedStyle(document.querySelector('.tr-bnav')).display!=='none',
                  side:getComputedStyle(document.querySelector('.tr-side')).display!=='none',
                  ovf:Math.max(0,document.documentElement.scrollWidth-innerWidth)};}"""
        rows = []
        for zw, zh in ((320, 700), (390, 844), (768, 1000), (1024, 900), (1280, 900), (1600, 1000), (1920, 1080), (2560, 1440)):
            pg.set_viewport_size({"width": zw, "height": zh}); pg.wait_for_timeout(300)
            d = pg.evaluate(FS); rows.append((zw, d))
            if d["ovf"]:
                fail.append("ที่ %dpx ล้นแนวนอน %dpx" % (zw, d["ovf"]))
            if zw < 1100 and not d["bnav"]:
                fail.append("ที่ %dpx ไม่มีแถบล่าง" % zw)
            if zw >= 1100 and (d["bnav"] or not d["side"]):
                fail.append("ที่ %dpx ควรใช้แถบซ้ายแทนแถบล่าง" % zw)
        small = [d["fs"] for w, d in rows if w < 1100]
        big = [d["fs"] for w, d in rows if w >= 1100]
        if small and big and min(big) <= max(small):
            fail.append("บนคอมเนื้อหาไม่ได้ใหญ่ขึ้น (%s → %s)" % (max(small), min(big)))
        print("ทุกความกว้าง: " + " · ".join("%d→%.1fpx%s" % (w, d["fs"], "/ซ้าย" if d["side"] else "/ล่าง") for w, d in rows))
        pg.set_viewport_size({"width": 390, "height": 844})

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
