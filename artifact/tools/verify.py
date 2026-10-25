#!/usr/bin/env python3
"""เปิด build/index.html ด้วย Chromium จริง ตรวจว่า loader ทำงานและสลับ set ได้"""
import subprocess, sys, time, os, re
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

        pg.wait_for_selector("aside .olec", timeout=10000)
        n = pg.eval_on_selector_all("aside .olec", "els=>els.length")
        print("%s outline: %d คาบ" % (_first["label"], n))
        if n != len(_flec):
            fail.append("%s ควรมี %d คาบ ได้ %d" % (_first["label"], len(_flec), n))

        ring = pg.inner_text("#ring")
        print("แถบความคืบหน้า:", ring.replace("\n", " "))
        if "/%d" % _fsec not in ring:   # แถบนี้นับเฉพาะชุดที่เปิดอยู่
            fail.append("ความคืบหน้าของ %s ควรเป็น %d หัวข้อ ได้: %r" % (_first["label"], _fsec, ring))

        # ปิดตารางเพื่อทวน: หาหัวข้อแรกของชุดแรกที่มีตารางอย่างน้อย 2 แถวข้อมูล แล้วลองปิด/เปิด
        _target = None
        for _l in _flec:
            for _s in _l["sections"]:
                _rows = [x for x in str(_s.get("md", "")).split("\n") if x.strip().startswith("|")]
                _body = [x for x in _rows if not set(x.replace("|", "").replace(" ", "")) <= set(":-")]
                if len(_body) >= 3:          # หัวตาราง + แถวข้อมูล 2 แถว
                    _target = (_l["lec"], _s["id"])
                    break
            if _target:
                break
        if not _target:
            fail.append("ไม่พบหัวข้อที่มีตารางในชุดแรก — ตรวจโหมดปิดตารางไม่ได้")
        else:
            _lec, _sid = _target
            pg.click('[data-lec="%s"]' % _lec)
            pg.wait_for_selector('[data-sec="%s"]' % _sid, state="visible", timeout=5000)
            pg.click('[data-sec="%s"]' % _sid)
            pg.wait_for_selector("main .card h2", timeout=5000)
            if not pg.query_selector("main .tqbar"):
                fail.append("หัวข้อ %s มีตารางแต่ไม่มีแถบปิดเพื่อทวน" % _sid)
            else:
                # ยึดตารางจากแถบของมันเอง — ตอบข้อสอบแล้วจะมีตารางในคำอธิบายเพิ่มเข้ามา
                _tbl = "()=>{var b=document.querySelector('main .tqbar');if(!b)return null;return [].map.call(b.nextElementSibling.querySelectorAll('tbody tr'),function(r){return [].map.call(r.children,function(c){return c.textContent.trim();});});}"
                _t0 = pg.evaluate(_tbl)
                pg.eval_on_selector_all("main .tqbar button[data-tq='on']", "e=>e[0].click()")
                pg.wait_for_selector("main table.tq td.cv", timeout=5000)
                _n = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.length")
                _hints = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.map(x=>x.getAttribute('data-hint'))")
                print("ปิดตารางเพื่อทวน (%s): %d ช่อง · คำใบ้ %r" % (_sid, _n, _hints[:4]))
                if _n < 1:
                    fail.append("กดปิดเพื่อทวนแล้วไม่มีช่องถูกปิด")
                # คอลัมน์แรกคือคำถาม ต้องไม่ถูกปิด
                if pg.eval_on_selector_all("main table.tq tbody tr", "rs=>rs.filter(r=>r.children[0].classList.contains('cv')).length"):
                    fail.append("คอลัมน์แรกถูกปิดด้วย ควรเปิดไว้เป็นคำถาม")
                # ข้อความต้องมองไม่เห็นจริง
                if "rgba(0, 0, 0, 0)" not in pg.eval_on_selector("main table.tq td.cv:not(.op)", "e=>getComputedStyle(e).color"):
                    fail.append("ข้อความของช่องที่ปิดยังมองเห็นได้")
                # คำใบ้ต้องสั้นและไม่ขึ้นต้นด้วยสระหรือวรรณยุกต์ลอย
                if any(x and len(x) > 10 for x in _hints):
                    fail.append("คำใบ้ยาวเกินไป: %r" % [x for x in _hints if x and len(x) > 10][:3])
                if any(x and x[0] in "ิีึืุูั่้๊๋็์ํ" for x in _hints):
                    fail.append("คำใบ้ขึ้นต้นด้วยสระหรือวรรณยุกต์ลอย")
                # เข้าถึงด้วยคีย์บอร์ดได้
                _kb = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.filter(x=>x.getAttribute('tabindex')!==null).length")
                if _kb != _n:
                    fail.append("ช่องที่ปิดเข้าถึงด้วยคีย์บอร์ดไม่ได้ (%d/%d)" % (_kb, _n))
                # แตะทีละช่อง แล้วสถานะต้องรอด render ใหม่
                pg.eval_on_selector_all("main table.tq td.cv", "e=>e[0].click()")
                if pg.eval_on_selector_all("main table.tq td.cv.op", "e=>e.length") != 1:
                    fail.append("แตะช่องเดียวแต่เปิดไม่ใช่ 1 ช่อง")
                if pg.query_selector("main .ch"):
                    pg.eval_on_selector_all("main .ch", "e=>e[0].click()")
                    pg.wait_for_selector(".verdict", timeout=5000)
                    pg.wait_for_timeout(400)
                    _n2 = pg.eval_on_selector_all("main table.tq td.cv", "e=>e.length")
                    _op2 = pg.eval_on_selector_all("main table.tq td.cv.op", "e=>e.length")
                    print("หลัง render ใหม่: ยังปิด %d ช่อง · ช่องที่เปิดไว้คงอยู่ %d" % (_n2, _op2))
                    if _n2 != _n:
                        fail.append("render ใหม่แล้วสถานะปิดตารางหาย (%d → %d)" % (_n, _n2))
                    if _op2 != 1:
                        fail.append("render ใหม่แล้วช่องที่เปิดไว้ถูกปิดกลับ")
                # เลิกทวน → ตารางกลับเป็นปกติ
                pg.eval_on_selector_all("main .tqbar button[data-tq='off']", "e=>e[0].click()")
                pg.wait_for_function("!document.querySelector('main table.tq td.cv')", timeout=5000)
                _t1 = pg.evaluate(_tbl)
                if _t1 != _t0:
                    fail.append("ตารางไม่กลับมาเหมือนเดิมหลังเลิกทวน")
                else:
                    print("เลิกทวน → ตารางกลับมาเหมือนเดิม ✓")

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

        # ปุ่มซ่อนแถบด้านบน: กดแล้วแถบต้องเตี้ยลงและซ่อนแท็บ แล้วคงสถานะหลังรีโหลด
        if pg.query_selector("#mastBtn"):
            _h0 = pg.eval_on_selector(".mast", "e=>Math.round(e.getBoundingClientRect().height)")
            pg.click("#mastBtn")
            pg.wait_for_function("document.querySelector('.mast').classList.contains('min')", timeout=3000)
            _h1 = pg.eval_on_selector(".mast", "e=>Math.round(e.getBoundingClientRect().height)")
            print("ปุ่มซ่อนแถบ: %dpx → %dpx" % (_h0, _h1))
            if _h1 >= _h0:
                fail.append("กดซ่อนแถบแล้วความสูงไม่ลดลง (%d → %d)" % (_h0, _h1))
            if pg.eval_on_selector("#courseTabs", "e=>e.getClientRects().length>0"):
                fail.append("ซ่อนแถบแล้วแท็บชุดวิชายังแสดงอยู่")
            pg.reload(wait_until="networkidle")
            pg.wait_for_selector("#mastBtn", timeout=10000)
            if not pg.eval_on_selector(".mast", "e=>e.classList.contains('min')"):
                fail.append("สถานะซ่อนแถบไม่ถูกจำไว้หลังรีโหลด")
            pg.click("#mastBtn")   # กางกลับก่อนตรวจการล้นแนวนอน
            pg.wait_for_function("!document.querySelector('.mast').classList.contains('min')", timeout=3000)
        else:
            fail.append("ไม่พบปุ่ม #mastBtn")

        # ไม่มี horizontal scroll ที่ความกว้างมือถือ
        ov = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
        print("ล้นแนวนอนที่ 390px:", ov, "px")
        if ov > 1:
            fail.append("หน้าล้นแนวนอน %dpx" % ov)

        pg.screenshot(path=os.path.join(os.path.dirname(BUILD), "check-mobile.png"), full_page=False)

        # ---- ปุ่มซ่อนเมนูแถบด้านบน ----
        cost = []
        HH = lambda: pg.evaluate(
            "()=>Math.round(document.querySelector('header.mast').getBoundingClientRect().height)")
        VIS = lambda sel: pg.evaluate(
            "s=>{const e=document.querySelector(s);return !!e&&getComputedStyle(e).display!=='none'}", sel)
        # เนื้อหาที่มองเห็นจริงต้องไม่ทับปุ่ม (ไล่ถึง text node ไม่ใช่กล่อง)
        OVER = """()=>{const b=document.getElementById('mastBtn').getBoundingClientRect();const o=[];
          const walk=e=>{if(e.id==='mastBtn'||getComputedStyle(e).display==='none')return;
            for(const n of e.childNodes){
              if(n.nodeType===3&&n.textContent.trim()){const r=document.createRange();r.selectNode(n);
                /* ตัดตามบรรพบุรุษที่ clip อยู่ ไม่งั้นข้อความที่ถูกย่อด้วย ... จะวัดกว้างเกินจริง */
                let cl=null;for(let a=e;a&&a!==document.body;a=a.parentElement){
                  const ov=getComputedStyle(a);
                  if(ov.overflowX!=='visible'||ov.overflowY!=='visible'){cl=a.getBoundingClientRect();break;}}
                for(const q0 of r.getClientRects()){
                  const q=cl?{left:Math.max(q0.left,cl.left),right:Math.min(q0.right,cl.right),
                              top:Math.max(q0.top,cl.top),bottom:Math.min(q0.bottom,cl.bottom)}:q0;
                  if(q.right>q.left&&q.bottom>q.top)o.push([e.id||e.className,q]);}}
              else if(n.nodeType===1)walk(n);}};
          document.querySelectorAll('.mast .wrap > *').forEach(walk);
          return o.filter(([n,r])=>!(r.right<=b.left||r.left>=b.right||r.bottom<=b.top||r.top>=b.bottom))
                  .map(([n])=>n);}"""

        for w in (320, 360, 390, 560, 768, 1024, 1280):
            pg.set_viewport_size({"width": w, "height": 900})
            pg.wait_for_timeout(120)
            open_h = HH()
            # ปุ่มลอยอยู่นอก flex จึงต้องไม่ทำให้แถบสูงขึ้นเลย
            base = pg.evaluate("""()=>{const b=document.getElementById('mastBtn'),p=b.parentNode;
                b.remove();const h=Math.round(document.querySelector('header.mast').getBoundingClientRect().height);
                p.appendChild(b);return h;}""")
            # ปุ่มสูงกว่าตัวหนังสือในแถวชื่อ จึงดันแถบขึ้นราว 10px เป็นเรื่องปกติ
            # แต่ถ้าเกินนั้นแปลว่าปุ่มเบียดจนมีแถวใหม่โผล่ — อันนั้นคือของเสีย
            cost.append((w, open_h - base))
            if open_h - base >= 20:
                fail.append("ที่ %dpx ปุ่มซ่อนเมนูเบียดจนแถบงอกอีกแถว (+%dpx)" % (w, open_h - base))
            hit = pg.evaluate(OVER)
            if hit:
                fail.append("ที่ %dpx ปุ่มซ่อนเมนูทับ %s" % (w, hit))
            pg.click("#mastBtn"); pg.wait_for_timeout(130)
            min_h = HH()
            if min_h > open_h * 0.6:
                fail.append("ที่ %dpx ย่อแล้วยังสูง %dpx (จาก %dpx)" % (w, min_h, open_h))
            if pg.evaluate(OVER):
                fail.append("ที่ %dpx ตอนย่อ ปุ่มทับเนื้อหา" % w)
            if not VIS("#mastBtn"):
                fail.append("ที่ %dpx ปุ่มหายตอนย่อ กดขยายกลับไม่ได้" % w)
            pg.click("#mastBtn"); pg.wait_for_timeout(130)
            if HH() != open_h:
                fail.append("ที่ %dpx ขยายกลับแล้วความสูงไม่เท่าเดิม" % w)
        print("ปุ่มซ่อนเมนูแถบ: ตรวจ %d ความกว้าง ✓ · ต้นทุนความสูงตอนกาง %s"
              % (len(cost), " ".join("%d:+%d" % c for c in cost)))

        # จำสถานะย่อข้ามรีโหลด
        pg.set_viewport_size({"width": 390, "height": 844})
        pg.click("#mastBtn"); pg.wait_for_timeout(130)
        was = HH()
        pg.reload(wait_until="networkidle"); pg.wait_for_timeout(250)
        if HH() != was:
            fail.append("รีโหลดแล้วไม่จำสถานะซ่อนเมนู")
        if not VIS("#mastBtn") or "\u25be" not in pg.inner_text("#mastBtn"):
            fail.append("หลังรีโหลด ปุ่มไม่ได้อยู่ในสถานะ 'ขยาย'")
        # สลับชุดวิชาแล้วต้องยังย่ออยู่ (render() เรียก applyHdr)
        pg.evaluate("()=>document.getElementById('mastBtn').click()"); pg.wait_for_timeout(130)
        pg.click("#courseTabs button:has-text('Chest')"); pg.wait_for_timeout(700)
        pg.click("#mastBtn"); pg.wait_for_timeout(130)
        pg.click("#courseTabs button:has-text('AIR')") if VIS("#courseTabs") else None
        pg.wait_for_timeout(500)
        if HH() > was * 1.3:
            fail.append("สลับชุดวิชาแล้วแถบเด้งกลับมากางเอง")
        print("จำสถานะย่อ + ไม่เด้งกลับตอนสลับชุดวิชา ✓")
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
