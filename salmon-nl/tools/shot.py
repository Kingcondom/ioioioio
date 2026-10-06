#!/usr/bin/env python3
"""เปิดเว็บด้วย Playwright แล้วถ่ายภาพหัวข้อหนึ่ง — python3 tools/shot.py <set> <section-id> <out.png> [width] [dark]"""
import sys, os, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key, sid, out = sys.argv[1:4]; w = int(sys.argv[4]) if len(sys.argv) > 4 else 1200; dark = len(sys.argv) > 5
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
H = functools.partial(Q, directory=ROOT)
srv = socketserver.TCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": w, "height": 900}, color_scheme="dark" if dark else "light")
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(f"http://127.0.0.1:{port}/index.html"); pg.wait_for_timeout(600)
    pg.click(f"button[data-course='{key}']") if pg.query_selector(f"button[data-course='{key}']") else None
    pg.wait_for_timeout(400)
    pg.click(f"button.tile[data-sec='{sid}']"); pg.wait_for_timeout(400)
    for b2 in pg.query_selector_all("button[data-q]")[:1]: b2.click()
    pg.wait_for_timeout(300)
    ov = pg.evaluate("document.documentElement.scrollWidth>window.innerWidth")
    raw = pg.evaluate("document.querySelector('main').innerText.includes('**')")
    pg.screenshot(path=out, full_page=True)
    print("page errors:", errs, "| h-overflow:", ov, "| raw **:", raw)
    b.close()
