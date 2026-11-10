#!/usr/bin/env python3
"""ตรวจการส่งตารางจาก MED421 learn ไปเป็นใบ post-it (ฟีเจอร์ 5 พ.ย.)

ฟีเจอร์นี้พาดสองหน้าและคั่นด้วย URL hash ที่เข้ารหัส base64 — ถ้าพังจะพังเงียบ
(ปุ่มกดได้ หน้าเปิดได้ แต่ไม่มีใบขึ้น หรือขึ้นเป็นภาษาต่างดาว) จึงต้องวิ่งจริงทั้งเส้น

    python3.13 artifact/tools/verify_pin.py

ตรวจพฤติกรรม ไม่ตรวจชื่อคลาส: หา "ปุ่มที่พาไปหน้า post-it" จากข้อความบนปุ่ม
ไม่ใช่จาก data-* เพราะฟีเจอร์นี้เพิ่งเขียนและถูกเขียนใหม่ได้ทุกวัน
"""
import base64
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
POSTIT = os.path.join(ROOT, "postit")
P_LEARN, P_POSTIT = 8941, 8942
PIN_LABEL = re.compile(r"ปัก.*ตาราง|ตาราง.*post")

fail = []

LKEY = "postit-v1"   # คีย์ที่หน้า post-it ใช้เก็บของจริง


def own_notes(pg):
    """ใบที่ผู้ใช้เขียนเอง อ่านจาก localStorage — เป็นสิ่งที่คงอยู่จริงหลังรีโหลด"""
    raw = pg.evaluate("(k)=>localStorage.getItem(k)", LKEY)
    if not raw:
        return []
    own = (json.loads(raw).get("own") or {})
    return [{"f": v.get("f", ""), "b": v.get("b", "")}
            for v in own.values() if v and not v.get("del")]




def chromium():
    c = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    if not c:
        raise SystemExit("ไม่พบ Chromium ใน /opt/pw-browsers — ห้ามรัน playwright install")
    return sorted(c, key=lambda p: int(re.search(r"chromium-(\d+)", p).group(1)))[-1]


def serve(d, port):
    s = subprocess.Popen([sys.executable, "-m", "http.server", str(port), "-d", d],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return s


def plain(t):
    """ตัด ** และยุบช่องว่าง ให้เทียบข้อความได้โดยไม่ติดมาร์กดาวน์"""
    return re.sub(r"\s+", " ", str("" if t is None else t)
                  .replace("**", "").replace("`", "")).strip()


def decode(payload):
    x = payload.replace("-", "+").replace("_", "/")
    x += "=" * (-len(x) % 4)
    return json.loads(base64.b64decode(x).decode("utf-8"))


# หาคาบ/หัวข้อที่มีตารางหลายคอลัมน์ จากไฟล์ data เอง ไม่ฝัง id ไว้
def pick_targets(nmax=3):
    out = []
    for f in sorted(glob.glob(os.path.join(LEARN, "data", "*.json"))):
        name = os.path.splitext(os.path.basename(f))[0]
        if name in ("index", "nl"):
            continue
        for lec in json.load(open(f, encoding="utf-8")):
            for sec in lec.get("sections", []):
                rows = [r.strip() for r in str(sec.get("md", "")).split("\n")
                        if r.strip().startswith("|")]
                body = [r for r in rows
                        if not set(r.replace("|", "").replace(" ", "")) <= set(":-")]
                if len(body) < 3:
                    continue
                cols = len(body[0].strip("|").split("|"))
                out.append((name, lec["lec"], sec["id"], cols, len(body) - 1))
    # เอาตาราง 2 คอลัมน์หนึ่งอัน และ >2 คอลัมน์หนึ่งอัน เพื่อคุมทั้งสองเส้นทางของโค้ด
    two = next((t for t in out if t[3] == 2), None)
    many = next((t for t in out if t[3] > 2), None)
    big = max(out, key=lambda t: t[3] * t[4]) if out else None
    return [t for t in (two, many, big) if t][:nmax]


MNEM_LABEL = re.compile(r"ปัก.*หลักจำ|หลักจำ.*post")


def pick_mnem():
    """หาหัวข้อที่มีกล่องหลักจำมากกว่าหนึ่งกล่อง เพื่อคุมว่าปักครบทุกกล่อง ไม่ใช่กล่องแรก"""
    best = None
    for f in sorted(glob.glob(os.path.join(LEARN, "data", "*.json"))):
        name = os.path.splitext(os.path.basename(f))[0]
        if name in ("index", "nl"):
            continue
        for lec in json.load(open(f, encoding="utf-8")):
            for sec in lec.get("sections", []):
                mn = sec.get("mnem") or []
                if len(mn) < 2:
                    continue
                if best is None or len(mn) > len(best[3]):
                    best = (name, lec["lec"], sec["id"], mn)
    return best



srv = [serve(LEARN, P_LEARN), serve(POSTIT, P_POSTIT)]
time.sleep(1.5)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chromium(), args=["--no-sandbox"])
        ctx = b.new_context(viewport={"width": 1280, "height": 900})
        learn = ctx.new_page()
        errs = []
        learn.on("pageerror", lambda e: errs.append("learn pageerror: %s" % e))
        learn.on("console", lambda m: errs.append("learn console: " + m.text)
                 if m.type == "error" else None)
        learn.on("response", lambda r: errs.append("learn %d %s" % (r.status, r.url))
                 if r.status >= 400 else None)
        learn.goto("http://127.0.0.1:%d/index.html" % P_LEARN, wait_until="networkidle")

        # กันเบราว์เซอร์เปิดลิงก์ออกไปข้างนอก แต่ยังให้ handler ของแอปตั้ง href ได้
        learn.add_init_script("")
        learn.evaluate("""()=>{document.addEventListener('click',function(e){
            var a=e.target.closest&&e.target.closest('a[href]');
            if(a&&/claude\\.ai\\/artifact/.test(a.getAttribute('href')||''))e.preventDefault();
        },false);}""")

        targets = pick_targets()
        if not targets:
            fail.append("ไม่พบตารางในชุดข้อมูลเลย — ตรวจไม่ได้")
        print("ตารางที่จะตรวจ:", [(t[0], t[2], "%dคอลัมน์ %dแถว" % (t[3], t[4]))
                                  for t in targets])

        payloads = []
        for setname, lec, sid, cols, rows in targets:
            label = next(e["label"] for e in json.load(
                open(os.path.join(LEARN, "data", "index.json"), encoding="utf-8"))
                if e["set"] == setname)
            # โครงหน้าใหม่ (9 พ.ย.): ไปหน้าคาบด้วยลิงก์ตรง #<ชุด>-<คาบ> แล้วกดการ์ดหัวข้อ (สารบัญซ่อนบนคอม)
            learn.evaluate("h=>{location.hash=h}", "#%s-%s" % (setname, re.sub(r"[^A-Za-z0-9._~-]", ".", str(lec))))
            learn.wait_for_selector('main [data-sec="%s"]' % sid, state="visible", timeout=8000)
            learn.click('main [data-sec="%s"]' % sid)
            learn.wait_for_timeout(300)

            links = learn.locator("main a").filter(has_text=PIN_LABEL)
            if links.count() == 0:
                fail.append("%s: ไม่พบปุ่มส่งตารางไป post-it เหนือตาราง" % sid)
                continue
            link = links.first
            link.click()
            learn.wait_for_timeout(120)
            href = link.get_attribute("href") or ""
            if "#t=" not in href:
                fail.append("%s: กดปุ่มแล้ว href ไม่มี #t= (ได้ %r)" % (sid, href[:90]))
                continue
            data = decode(href.split("#t=", 1)[1])

            # เทียบกับตารางที่อยู่บนหน้าจริง ไม่ใช่กับ markdown
            dom = learn.evaluate("""(sel)=>{
              var a=[...document.querySelectorAll('main .prose .tablewrap')];
              var tw=a.find(x=>x.querySelector('table'));
              var tb=tw.querySelector('table');
              var hd=[...tb.querySelectorAll('thead th')].map(t=>t.innerText.trim());
              var rows=[...tb.querySelectorAll('tbody tr')].map(
                  tr=>[...tr.children].map(td=>td.innerText.trim()));
              return {hd:hd, rows:rows};
            }""", None)
            usable = [r for r in dom["rows"]
                      if r and r[0] and any(c and c != "—" for c in r[1:])]
            if len(data.get("c") or []) != len(usable):
                fail.append("%s: ตารางบนหน้ามีแถวใช้ได้ %d แต่ส่งไป %d ใบ"
                            % (sid, len(usable), len(data.get("c") or [])))
            for (front, back), row in zip(data.get("c") or [], usable):
                key = row[0].replace("*", "")
                if key.split("\n")[0][:18] not in front:
                    fail.append("%s: หน้าใบไม่มีคอลัมน์แรกของแถว (%r ไม่อยู่ใน %r)"
                                % (sid, key[:18], front[:60]))
                    break
                for c in row[1:]:
                    if c and c != "—" and c.split("\n")[0][:18] not in back:
                        fail.append("%s: หลังใบตกเนื้อหาคอลัมน์ถัดไป (%r)" % (sid, c[:30]))
                        break
            nbytes = len(href)
            print("  %-18s %d ใบ · URL %d ตัวอักษร%s"
                  % (sid, len(data.get("c") or []), nbytes,
                     "  ⚠ ยาวเกิน 8000 เสี่ยงเบราว์เซอร์ตัด" if nbytes > 8000 else ""))
            if nbytes > 8000:
                fail.append("%s: URL ยาว %d ตัวอักษร — เสี่ยงถูกตัดในเบราว์เซอร์บางตัว"
                            % (sid, nbytes))
            payloads.append((sid, href.split("#t=", 1)[1], data))

        # ---- ฝั่ง post-it: เปิดด้วย hash จริงแล้วต้องได้ใบครบ ----
        pin = ctx.new_page()
        pin.on("pageerror", lambda e: errs.append("postit pageerror: %s" % e))
        pin.on("console", lambda m: errs.append("postit console: " + m.text)
               if m.type == "error" else None)
        pin.on("response", lambda r: errs.append("postit %d %s" % (r.status, r.url))
               if r.status >= 400 else None)
        for round_i, (sid, payload, data) in enumerate(payloads):
            pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT,
                     wait_until="domcontentloaded")
            pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)
            pin.goto("http://127.0.0.1:%d/index.html?r=%d#t=%s"
                     % (P_POSTIT, round_i, payload), wait_until="networkidle")
            pin.wait_for_timeout(600)
            own = own_notes(pin)
            want = [(f, b) for f, b in data["c"]]
            if len(own) != len(want):
                fail.append("%s: ส่งไป %d ใบ แต่หน้า post-it สร้าง %d ใบ"
                            % (sid, len(want), len(own)))
            got = {(o["f"], o["b"]) for o in own}
            missing = [w for w in want if w not in got]
            if missing:
                fail.append("%s: %d ใบเนื้อหาไม่ตรงหลังถอดรหัส เช่น %r"
                            % (sid, len(missing), missing[0][0][:60]))
            # ใบที่ปักต้องขึ้นบนกระดานจริง ไม่ใช่แค่ถูกบันทึก — ตั้งแต่ 7 พ.ย.
            # กระดานเลื่อนได้ ใบเกินหนึ่งจอต้องวางต่อลงไป ไม่ใช่หายไป
            shown = pin.evaluate("()=>document.querySelectorAll('#grid > *').length")
            if shown < len(own):
                fail.append("%s: บันทึก %d ใบ แต่ขึ้นบนกระดานแค่ %d ใบ"
                            % (sid, len(own), shown))
            print("  %-18s ขึ้นบนกระดาน %d ใบ" % (sid, shown))

            thai = [o for o in own if re.search(r"[฀-๿]", o["f"] + o["b"])]
            print("  %-18s post-it สร้าง %d ใบ · มีภาษาไทยอ่านออก %d ใบ"
                  % (sid, len(own), len(thai)))
            if want and not thai:
                fail.append("%s: ไม่มีใบไหนมีอักษรไทยเลย — น่าจะเพี้ยนตอนถอด base64" % sid)

            # ปักซ้ำต้องไม่ได้ใบเพิ่ม (pinTable คีย์ด้วย hash ของเนื้อหา)
            before = len(own)
            pin.goto("http://127.0.0.1:%d/index.html?r=%db#t=%s"
                     % (P_POSTIT, round_i, payload), wait_until="networkidle")
            pin.wait_for_timeout(600)
            after = len(own_notes(pin))
            if after != before:
                fail.append("%s: ปักซ้ำแล้วใบเพิ่มจาก %d เป็น %d — ควรกันซ้ำด้วยเนื้อหา"
                            % (sid, before, after))
        pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT,
                 wait_until="domcontentloaded")
        pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)
        # ---- แท็บ post-it ที่เปิดอยู่แล้ว แล้วเปลี่ยนแค่ hash ----
        # production อาจส่ง payload มาทางนี้ (แท็บเปิดอยู่ แอปเปลี่ยน hash ให้) ไม่ใช่โหลดหน้าใหม่
        # เส้นทางนี้วิ่งผ่าน readHash() ของ hashchange ซึ่งไม่มีอะไรคุมมาก่อน
        if payloads:
            sid0, payload0, data0 = payloads[0]
            pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT, wait_until="networkidle")
            pin.wait_for_timeout(600)
            pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)
            pin.evaluate("(p)=>{location.hash='t='+p;}", payload0)
            pin.wait_for_timeout(900)
            got = own_notes(pin)
            print("  %-18s แท็บเปิดอยู่แล้วเปลี่ยนแค่ hash → %d ใบ" % (sid0, len(got)))
            if len(got) != len(data0.get("c") or []):
                fail.append("%s: เปลี่ยนแค่ hash (แท็บเปิดอยู่แล้ว) ได้ %d ใบ ควรได้ %d "
                            "— เส้นทาง hashchange พัง" % (sid0, len(got), len(data0.get("c") or [])))
            pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT, wait_until="domcontentloaded")
            pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)

        # ---- ปักกล่อง "หลักจำ" (ผู้ใช้ขอ 7 พ.ย.) ----
        mn = pick_mnem()
        if not mn:
            fail.append("ไม่พบหัวข้อที่มีกล่องหลักจำสองกล่องขึ้นไป — ตรวจปุ่มปักหลักจำไม่ได้")
        else:
            mset, mlec, msid, boxes = mn
            label = next(e["label"] for e in json.load(
                open(os.path.join(LEARN, "data", "index.json"), encoding="utf-8"))
                if e["set"] == mset)
            # โครงหน้าใหม่ (9 พ.ย.): ไปหน้าคาบด้วยลิงก์ตรง #<ชุด>-<คาบ> แล้วกดการ์ดหัวข้อ (สารบัญซ่อนบนคอม)
            learn.evaluate("h=>{location.hash=h}", "#%s-%s" % (mset, re.sub(r"[^A-Za-z0-9._~-]", ".", str(mlec))))
            learn.wait_for_selector('main [data-sec="%s"]' % msid, state="visible", timeout=8000)
            learn.click('main [data-sec="%s"]' % msid)
            learn.wait_for_timeout(300)

            links = learn.locator("main a").filter(has_text=MNEM_LABEL)
            if links.count() == 0:
                fail.append("%s: ไม่พบปุ่มปักหลักจำในกล่องหลักจำ" % msid)
            else:
                link = links.first
                link.click()
                learn.wait_for_timeout(120)
                href = link.get_attribute("href") or ""
                if "#t=" not in href:
                    fail.append("%s: กดปุ่มปักหลักจำแล้ว href ไม่มี #t= (ได้ %r)"
                                % (msid, href[:90]))
                else:
                    d = decode(href.split("#t=", 1)[1])
                    cards = d.get("c") or []
                    want = [b for b in boxes if plain(b.get("name"))]
                    if len(cards) != len(want):
                        fail.append("%s: หัวข้อนี้มีหลักจำ %d กล่อง แต่ส่งไป %d ใบ"
                                    % (msid, len(want), len(cards)))
                    for box, (front, back) in zip(want, cards):
                        nm = plain(box.get("name"))
                        if nm not in plain(front):
                            fail.append("%s: หน้าใบไม่มีชื่อหลักจำ %r (ได้ %r)"
                                        % (msid, nm, front[:60]))
                            continue
                        if box.get("note") and plain(box["note"])[:25] not in plain(back):
                            fail.append("%s: ใบของ %s ตก note ของกล่อง" % (msid, nm))
                        lines = [l for l in (box.get("lines") or [])
                                 if isinstance(l, (list, tuple)) and len(l) == 2]
                        for key, val in (lines[:1] + lines[-1:]):
                            probe = plain(val)[:22] or plain(key)
                            if probe and probe not in plain(back):
                                fail.append("%s: ใบของ %s ตกบรรทัด %r"
                                            % (msid, nm, probe))
                                break
                    print("  %-18s หลักจำ %d กล่อง → %d ใบ · URL %d ตัวอักษร"
                          % (msid, len(want), len(cards), len(href)))
                    if len(href) > 8000:
                        fail.append("%s: URL ปักหลักจำยาว %d ตัวอักษร" % (msid, len(href)))

                    pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT,
                             wait_until="domcontentloaded")
                    pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)
                    pin.goto("http://127.0.0.1:%d/index.html?mn=1#t=%s"
                             % (P_POSTIT, href.split("#t=", 1)[1]),
                             wait_until="networkidle")
                    pin.wait_for_timeout(700)
                    got = own_notes(pin)
                    shown = pin.evaluate(
                        "()=>document.querySelectorAll('#grid > *').length")
                    print("  %-18s post-it สร้าง %d ใบ · ขึ้นบนกระดาน %d ใบ"
                          % (msid, len(got), shown))
                    if len(got) != len(cards):
                        fail.append("%s: ส่งหลักจำ %d ใบ แต่หน้า post-it สร้าง %d ใบ"
                                    % (msid, len(cards), len(got)))
                    if shown < len(got):
                        fail.append("%s: หลักจำบันทึก %d ใบ แต่ขึ้นบนกระดานแค่ %d"
                                    % (msid, len(got), shown))

        # กระดานเลื่อนได้ (7 พ.ย.) — ใบเกินหนึ่งจอต้องวางต่อลงไปครบ ไม่ใช่โดนตัด
        # ตารางจริงในชุดยังสั้นเกินกว่าจะกินเกินหนึ่งจอ จึงสร้าง payload ขึ้นมาทดสอบเอง
        MANY = 30
        synth = {"s": "ทดสอบกระดานเลื่อน",
                 "c": [["**แถวที่ %d**\nคำถามทดสอบ" % i, "คำตอบทดสอบ %d" % i]
                       for i in range(1, MANY + 1)]}
        sp = base64.urlsafe_b64encode(
            json.dumps(synth, ensure_ascii=False).encode("utf-8")).decode().rstrip("=")
        pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT,
                 wait_until="domcontentloaded")
        pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)
        pin.goto("http://127.0.0.1:%d/index.html?many=1#t=%s" % (P_POSTIT, sp),
                 wait_until="networkidle")
        pin.wait_for_timeout(800)
        saved = len(own_notes(pin))
        shown = pin.evaluate("()=>document.querySelectorAll('#grid > *').length")
        geo = pin.evaluate("""()=>{var b=document.getElementById('board'),
            g=document.getElementById('grid');
            return {scrollable:b.scrollHeight>b.clientHeight+4,
                    gridH:Math.round(g.getBoundingClientRect().height),
                    boardH:Math.round(b.getBoundingClientRect().height),
                    ovfX:Math.max(0,document.documentElement.scrollWidth-innerWidth)};}""")
        print("  ปัก %d ใบ: บันทึก %d · ขึ้นบนกระดาน %d · เลื่อนได้ %s · ล้นแนวนอน %d px"
              % (MANY, saved, shown, geo["scrollable"], geo["ovfX"]))
        if saved != MANY:
            fail.append("ปัก %d ใบรวดเดียว บันทึกได้ %d" % (MANY, saved))
        if shown != MANY:
            fail.append("ปัก %d ใบ แต่ขึ้นบนกระดานแค่ %d — ใบเกินหนึ่งจอหาย"
                        % (MANY, shown))
        if not geo["scrollable"]:
            fail.append("ใบ %d ใบไม่ทำให้กระดานเลื่อนได้ (gridH %d · boardH %d) "
                        "— ถ้าใบล้นออกนอกจอแล้วเลื่อนไม่ได้ จะมองไม่เห็น"
                        % (MANY, geo["gridH"], geo["boardH"]))
        if geo["ovfX"]:
            fail.append("ใบเยอะแล้วล้นแนวนอน %d px" % geo["ovfX"])
        pin.goto("http://127.0.0.1:%d/index.html" % P_POSTIT,
                 wait_until="domcontentloaded")
        pin.evaluate("(k)=>localStorage.removeItem(k)", LKEY)

        bad_hash = "t=%s" % base64.urlsafe_b64encode(b"not json").decode().rstrip("=")
        pin.goto("http://127.0.0.1:%d/index.html#%s" % (P_POSTIT, bad_hash),
                 wait_until="networkidle")
        pin.wait_for_timeout(500)
        n = len(own_notes(pin))
        if n:
            fail.append("ส่ง payload เสียไปแล้วยังสร้าง %d ใบ — ควรแจ้งเตือนแล้วไม่สร้าง" % n)
        print("  payload เสีย → สร้าง %d ใบ (ควรเป็น 0)" % n)

        hard = [e for e in errs
                if "favicon" not in e and "Failed to load resource" not in e]
        if hard:
            fail.append("มี error ในคอนโซล: %s" % hard[:3])
        b.close()
finally:
    for s in srv:
        s.terminate()

print()
if fail:
    print("❌ ไม่ผ่าน")
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("✅ ผ่านทุกข้อ — ตารางจาก learn ไปขึ้นเป็นใบ post-it ได้ครบและอ่านออก")
