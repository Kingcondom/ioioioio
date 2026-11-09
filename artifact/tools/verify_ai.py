#!/usr/bin/env python3
"""ตรวจกล่อง "ถาม AI" ของหน้า learn (capability sample · ผู้ใช้ขอ 7 พ.ย.)

หน้าจริงเรียกโมเดลผ่าน window.claude ซึ่งมีแค่ตอนเปิดใน claude.ai — รันในเครื่องเรียกไม่ได้
จึง **ปลอม window.claude.use** ก่อนหน้าโหลด แล้วตรวจทุกอย่างรอบ ๆ การเรียกนั้น:
สิ่งที่ส่งไปถูกไหม · สตรีมแล้วข้อความไม่ซ้ำ · กดหยุดได้จริง · error แต่ละรหัสทำตัวถูก ·
ไม่มี capability แล้วปุ่มต้องไม่โผล่

    python3.13 artifact/tools/verify_ai.py

ข้อที่คุมแน่น ๆ สองข้อ เพราะเป็นบั๊กที่เกิดง่ายและเงียบ:
- `onText` ส่ง **คำตอบทั้งก้อน** ไม่ใช่ส่วนต่อท้าย ถ้าโค้ดเผลอ `+=` ข้อความจะซ้ำทวีคูณ
- `cache` ต้องเป็น false ไม่งั้นถามซ้ำจะได้คำตอบเก่าย้อนมา (replay 5 นาที)
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEARN = os.path.join(ROOT, "artifact")
PORT = 8961
SONNET = re.compile(r"sonnet")

fail = []


def chromium():
    c = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    if not c:
        raise SystemExit("ไม่พบ Chromium ใน /opt/pw-browsers")
    return sorted(c, key=lambda p: int(re.search(r"chromium-(\d+)", p).group(1)))[-1]


# ปลอม window.claude: sample คืนค่าตามสคริปต์ที่เทสต์กำหนด และบันทึกทุกอย่างที่หน้าส่งมา
STUB = """
window.__aiCalls = [];
window.__aiPlan = window.__aiPlan || {mode: "ok"};
window.claude = {
  use: function (name) {
    if (name === "sample") {
      if (window.__aiPlan.noSample) return Promise.resolve(null);
      var fn = function (input, opts) {
        var rec = {input: input, opts: {}, aborted: false};
        for (var k in (opts || {})) if (k !== "onText" && k !== "signal") rec.opts[k] = opts[k];
        rec.hasSignal = !!(opts && opts.signal);
        window.__aiCalls.push(rec);
        var plan = window.__aiPlan;
        if (plan.mode === "err") {
          return Promise.reject({code: plan.code, message: "stub"});
        }
        return new Promise(function (resolve, reject) {
          /* สตรีมแบบของจริง: ส่งคำตอบทั้งก้อนที่ยาวขึ้นเรื่อย ๆ */
          var parts = ["คำตอบ ท่อนแรก", "คำตอบ ท่อนแรก และท่อนสอง"];
          if (opts && opts.signal) {
            opts.signal.addEventListener("abort", function () {
              rec.aborted = true;
              reject({code: "cancelled", text: parts[0]});
            });
          }
          setTimeout(function () { opts && opts.onText && opts.onText({text: parts[0]}); }, 40);
          if (plan.mode === "hang") return;      /* ค้างไว้ให้เทสต์กดหยุด */
          setTimeout(function () {
            opts && opts.onText && opts.onText({text: parts[1]});
            resolve({text: parts[1], truncated: false});
          }, 120);
        });
      };
      fn.limits = function () { return Promise.resolve({images: false}); };
      fn.json = function () { return Promise.resolve({}); };
      return Promise.resolve(fn);
    }
    return Promise.resolve(null);   /* db/user ไม่ต้องมีในเทสต์นี้ */
  }
};
"""


def pick_section():
    """หาหัวข้อที่มีเนื้อหาร้อยแก้วยาวพอให้ลากคลุมได้"""
    for f in sorted(glob.glob(os.path.join(LEARN, "data", "*.json"))):
        name = os.path.splitext(os.path.basename(f))[0]
        if name in ("index", "nl"):
            continue
        for lec in json.load(open(f, encoding="utf-8")):
            for sec in lec.get("sections", []):
                for line in str(sec.get("md", "")).split("\n"):
                    t = line.strip()
                    if len(t) > 120 and not t.startswith(("|", "#", ">", "-", "[[")):
                        return name, lec["lec"], sec["id"]
    return None


srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", LEARN],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.5)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chromium(), args=["--no-sandbox"])

        def fresh(plan=None):
            ctx = b.new_context(viewport={"width": 1280, "height": 900})
            ctx.add_init_script("window.__aiPlan=%s;" % json.dumps(plan or {"mode": "ok"}))
            ctx.add_init_script(STUB)
            pg = ctx.new_page()
            pg.on("pageerror", lambda e: fail.append("pageerror: %s" % e))
            pg.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="networkidle")
            return ctx, pg

        target = pick_section()
        if not target:
            fail.append("ไม่พบหัวข้อที่มีร้อยแก้วยาวพอให้ลากคลุม")
        setname, lec, sid = target or (None, None, None)

        def open_section(pg):
            """ไปหัวข้อด้วย hash เหมือน verify.py — แท็บชุดวิชาอยู่ในแผงข้างที่พับได้
            แล้วจึงกดจากแท็บไม่ได้ทุกความกว้าง"""
            slug = re.sub(r"[^A-Za-z0-9._~-]", ".", str(lec))
            pg.evaluate("h=>{location.hash=h}", "#%s-%s" % (setname, slug))
            pg.wait_for_selector('main [data-sec="%s"]' % sid, state="visible", timeout=10000)
            pg.click('main [data-sec="%s"]' % sid)
            pg.wait_for_selector("main .card h2", timeout=8000)
            pg.wait_for_timeout(250)

        def entry(pg):
            """ทางเข้ากล่องแชทที่ผู้ใช้กดจริง — ปุ่มในแถบนำทาง (ล่างบนมือถือ ซ้ายบนจอกว้าง)
            ปุ่มลอย .ai-fab ถูกซ่อนด้วย CSS ในเลย์เอาต์ที่มีแถบนำทาง จึงไม่ใช้เป็นตัววัด"""
            nav = pg.locator("[data-trai]")
            if nav.count() and nav.first.is_visible():
                return nav.first
            fab = pg.locator(".ai-fab")
            if fab.count() and fab.first.is_visible():
                return fab.first
            return None

        def open_chat(pg, who="กล่องแชท"):
            if not pg.locator(".ai-panel").is_hidden():
                return True                      # จอกว้างเปิดให้เองรอบแรก
            e = entry(pg)
            if e is None:
                fail.append("%s: ไม่พบทางเข้ากล่องถาม AI เลย (ทั้งปุ่มแถบนำทางและปุ่มลอย)" % who)
                return False
            e.click()
            pg.wait_for_timeout(300)
            if pg.locator(".ai-panel").is_hidden():
                fail.append("%s: กดปุ่มถาม AI แล้วกล่องไม่เปิด" % who)
                return False
            return True

        def select_prose(pg):
            """ลากคลุมย่อหน้าแรกที่ยาวพอในเนื้อหา แล้วคืนข้อความที่เลือก"""
            return pg.evaluate("""()=>{
              const p=[...document.querySelectorAll('#main .prose p,#main .prose li')]
                      .find(x=>x.textContent.trim().length>80);
              if(!p) return null;
              const r=document.createRange();r.selectNodeContents(p);
              const s=window.getSelection();s.removeAllRanges();s.addRange(r);
              document.dispatchEvent(new Event('selectionchange'));
              return s.toString().trim();
            }""")

        # ---------- 1. ปุ่มลอยขึ้นเมื่อมี capability ----------
        ctx, pg = fresh()
        open_section(pg)
        if open_chat(pg, "มี capability"):
            print("ทางเข้ากล่องถาม AI: เปิดได้เมื่อ capability ใช้ได้ ✓")
        pg.click('.ai-panel [data-ai="close"]')
        pg.wait_for_timeout(150)

        # ---------- 2. ลากคลุม → ปุ่มถามโผล่ → เปิดกล่องพร้อมข้อความที่เลือก ----------
        picked = select_prose(pg)
        if not picked:
            fail.append("หาย่อหน้าให้ลากคลุมในหัวข้อ %s ไม่ได้" % sid)
        else:
            pg.wait_for_timeout(400)
            sel = pg.locator(".ai-sel")
            if sel.is_hidden():
                fail.append("ลากคลุมข้อความแล้วปุ่ม 'ถาม AI ↗' ไม่โผล่")
            else:
                sel.click()
                pg.wait_for_timeout(250)
                if pg.locator(".ai-panel").is_hidden():
                    fail.append("กดปุ่มถามแล้วกล่องแชทไม่เปิด")
                quote = pg.inner_text(".ai-panel") if not pg.locator(".ai-panel").is_hidden() else ""
                head = picked[:30]
                if head and head not in quote:
                    fail.append("กล่องแชทไม่แสดงข้อความที่ลากคลุมไว้เป็นบริบท (%r)" % head)
                print("ลากคลุม → ปุ่มถามโผล่ → กล่องเปิดพร้อมบริบท ✓ (%d ตัวอักษร)" % len(picked))

        # ---------- 3. ส่งคำถาม: สิ่งที่ส่งไปต้องถูก และสตรีมต้องไม่ซ้ำ ----------
        pg.fill(".ai-panel textarea", "อันนี้หมายความว่าอะไร")
        pg.click('.ai-panel [data-ai="send"]')
        pg.wait_for_timeout(700)
        calls = pg.evaluate("()=>window.__aiCalls")
        if not calls:
            fail.append("กดส่งแล้วไม่มีการเรียก sample เลย")
        else:
            c = calls[-1]
            opts, inp = c["opts"], c["input"]
            if opts.get("cache") is not False:
                fail.append("cache ต้องเป็น false สำหรับแชท (ได้ %r) — ถามซ้ำจะได้คำตอบเก่า"
                            % opts.get("cache"))
            if not SONNET.search(str(opts.get("model") or "")):
                fail.append("ผู้ใช้ขอระดับ sonnet แต่ model ที่ส่งคือ %r" % opts.get("model"))
            if not c.get("hasSignal"):
                fail.append("ไม่ได้ส่ง signal ไปด้วย — กดหยุดกลางคันจะยกเลิกไม่ได้")
            if not isinstance(inp, list) or not inp:
                fail.append("input ที่ส่งไม่ใช่รายการบทสนทนา (ได้ %s)" % type(inp).__name__)
            else:
                if inp[-1].get("role") != "user":
                    fail.append("บทสนทนาต้องจบด้วย role user (ได้ %r)" % inp[-1].get("role"))
                last = str(inp[-1].get("content") or "")
                if picked and picked[:25] not in last:
                    fail.append("ข้อความที่ลากคลุมไม่ถูกส่งไปเป็นบริบท")
                if "อันนี้หมายความว่าอะไร" not in last:
                    fail.append("คำถามที่พิมพ์ไม่ถูกส่งไป")
            print("ส่งคำถาม: model=%s · cache=%r · ส่ง signal=%s · %d ท่อนบทสนทนา ✓"
                  % (opts.get("model"), opts.get("cache"), c.get("hasSignal"), len(inp)))

            body = pg.inner_text(".ai-panel")
            if body.count("ท่อนแรก") > 2:
                fail.append("คำตอบซ้ำในหน้า (%d ครั้ง) — onText ให้คำตอบทั้งก้อน ต้อง assign ไม่ใช่ +="
                            % body.count("ท่อนแรก"))
            if "ท่อนสอง" not in body:
                fail.append("ไม่เห็นคำตอบท่อนสุดท้ายในกล่องแชท")
            print("สตรีมคำตอบ: ไม่ซ้ำ · เห็นคำตอบสุดท้ายครบ ✓")

        # ---------- 4. กดหยุดกลางคัน ----------
        ctx.close()
        ctx, pg = fresh({"mode": "hang"})
        open_section(pg)
        open_chat(pg, "กดหยุด")
        pg.fill(".ai-panel textarea", "ถามยาว ๆ")
        pg.click('.ai-panel [data-ai="send"]')
        pg.wait_for_timeout(300)
        pg.click('.ai-panel [data-ai="send"]')      # ปุ่มเดิมกลายเป็น "หยุด"
        pg.wait_for_timeout(400)
        aborted = pg.evaluate("()=>(window.__aiCalls.slice(-1)[0]||{}).aborted")
        body = pg.inner_text(".ai-panel")
        if not aborted:
            fail.append("กดหยุดแล้วไม่ได้ abort การเรียกจริง")
        if "หยุด" not in body:
            fail.append("กดหยุดแล้วไม่บอกผู้ใช้ว่าหยุดแล้ว")
        print("กดหยุดกลางคัน: abort ถึง stub จริง · แจ้งผู้ใช้ ✓")

        # ---------- 5. error ชั่วคราวต้องไม่ปิดฟีเจอร์ / error ถาวรต้องปิด ----------
        ctx.close()
        ctx, pg = fresh({"mode": "err", "code": "rate_limited"})
        open_section(pg)
        open_chat(pg, "rate_limited")
        pg.fill(".ai-panel textarea", "ถาม")
        pg.click('.ai-panel [data-ai="send"]')
        pg.wait_for_timeout(500)
        body = pg.inner_text(".ai-panel")
        if "ถี่" not in body and "โควตา" not in body:
            fail.append("rate_limited ควรบอกผู้ใช้ว่าถามถี่เกินไป (ได้ %r)" % body[-120:])
        pg.click('.ai-panel [data-ai="close"]')
        pg.wait_for_timeout(200)
        if entry(pg) is None:
            fail.append("rate_limited เป็นเรื่องชั่วคราว แต่ทางเข้ากล่องถามหายไปเลย")
        print("error ชั่วคราว (rate_limited): แจ้งผู้ใช้ · ทางเข้ายังอยู่ ✓")

        ctx.close()
        ctx, pg = fresh({"mode": "err", "code": "not_granted"})
        open_section(pg)
        open_chat(pg, "not_granted")
        pg.fill(".ai-panel textarea", "ถาม")
        pg.click('.ai-panel [data-ai="send"]')
        pg.wait_for_timeout(500)
        pg.click('.ai-panel [data-ai="close"]')
        pg.wait_for_timeout(200)
        picked = select_prose(pg)
        pg.wait_for_timeout(400)
        if pg.locator(".ai-sel").count() and pg.locator(".ai-sel").is_visible():
            fail.append("not_granted = ใช้ไม่ได้ถาวร แต่ลากคลุมแล้วยังโชว์ปุ่ม 'ถาม AI ↗'")
        print("error ถาวร (not_granted): เลิกโชว์ปุ่มถามตอนลากคลุม ✓")

        # ---------- 6. ไม่มี capability เลย → ปุ่มต้องไม่โผล่ ----------
        ctx.close()
        ctx, pg = fresh({"noSample": True})
        open_section(pg)
        e = entry(pg)
        if e is not None:
            e.click()
            pg.wait_for_timeout(300)
            if not pg.locator(".ai-panel").is_hidden():
                fail.append("ไม่มี capability แต่กดปุ่มถามแล้วกล่องยังเปิด — ถามไปก็ไม่มีใครตอบ")
        picked = select_prose(pg)
        pg.wait_for_timeout(400)
        if pg.locator(".ai-sel").count() and pg.locator(".ai-sel").is_visible():
            fail.append("ไม่มี capability แต่ลากคลุมแล้วยังโชว์ปุ่ม 'ถาม AI ↗'")
        print("ไม่มี capability: ไม่โชว์ปุ่มทั้งสองแบบ ✓")
        ctx.close()
        b.close()
finally:
    srv.terminate()

print()
if fail:
    print("❌ ไม่ผ่าน")
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("✅ ผ่านทุกข้อ — กล่องถาม AI ส่งบริบทถูก สตรีมไม่ซ้ำ หยุดได้ และถอยอย่างสุภาพเมื่อใช้ไม่ได้")
