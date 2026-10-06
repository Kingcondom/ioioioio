#!/usr/bin/env python3
"""ไล่เปิดทุกหัวข้อของทุกชุดที่ 390px โหมดมืด: page error · ล้นจอแนวนอน · ** ค้าง · ภาพ SVG ไม่ขึ้น"""
import json, os, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
idx = json.load(open(os.path.join(ROOT, "data", "index.json")))
bad = 0; n = 0
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 390, "height": 800}, color_scheme="dark")
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.set_default_timeout(8000)
    pg.goto(f"http://127.0.0.1:{port}/index.html"); pg.wait_for_timeout(500)
    for c in (idx if not os.environ.get("EXAM_ONLY") else idx[:1]):
        pg.click(f"button[data-course='{c['set']}']"); pg.wait_for_timeout(300)
        for l in json.load(open(os.path.join(ROOT, c["file"]))):
            for s in (l["sections"] if not os.environ.get("EXAM_ONLY") else []):
                n += 1
                if n % 50 == 0: print("..", n, flush=True)
                pg.evaluate(f"document.querySelector(\"button.tile[data-sec='{s['id']}']\")||0")
                pg.click(f"button[data-tab='home']"); pg.wait_for_timeout(60)
                pg.click(f"button.tile[data-sec='{s['id']}']"); pg.wait_for_timeout(80)
                r = pg.evaluate("""()=>({ov:document.documentElement.scrollWidth>window.innerWidth,
                  raw:document.querySelector('main').innerText.includes('**'),
                  figs:document.querySelectorAll('main figure.fig svg').length,
                  title:(document.querySelector('main h2')||{}).textContent})""")
                prob = []
                if r["ov"]: prob.append("ล้นจอ")
                if r["raw"]: prob.append("** ค้าง")
                if r["figs"] != len(s.get("figs", [])): prob.append(f"ภาพ {r['figs']}/{len(s.get('figs',[]))}")
                if r["title"] != s["title"]: prob.append("เปิดผิดหัวข้อ")
                if errs: prob.append("error " + errs.pop())
                if prob: bad += 1; print("✗", c["set"], s["id"], prob, flush=True)
    pg.click("button[data-tab='review']"); pg.wait_for_timeout(150)
    pg.click("button[data-tab='exam']"); pg.wait_for_timeout(150)
    pg.click("button[data-act='newexam']"); pg.wait_for_timeout(200)
    pg.click("button[data-xq]"); pg.wait_for_timeout(150)
    ok = pg.evaluate("document.querySelectorAll('.verdict').length")
    print("สุ่มข้อสอบ:", "ทำงาน" if ok else "✗ ไม่เฉลย", "| errors:", errs)
    b.close()
print(f"ตรวจ {n} หัวข้อ · มีปัญหา {bad}")
