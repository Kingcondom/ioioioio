#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ดูภาพประกอบก่อนใส่ในบทเรียน — วาดภาพจากโมดูล figs_*.py ลงหน้าเปล่าที่ใช้ CSS เดียวกับเว็บ แล้วถ่ายภาพโหมดสว่าง/มืด

    python3 artifact/tools/preview_figs.py figs_glomerular barrier twomech --out /tmp/prev
    python3 artifact/tools/preview_figs.py figs_glomerular --out /tmp/prev        # ทุกฟังก์ชันในโมดูล

ตรวจด้วย: ข้อความ/รูปทรงหลุดกรอบ · ข้อความทับกัน (เหมือน check_render.py) แล้วเปิดดูภาพด้วย Read"""
import importlib, inspect, os, re, sys
from playwright.sync_api import sync_playwright

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
args = [a for a in sys.argv[1:]]
out = args[args.index("--out") + 1] if "--out" in args else "/tmp/figprev"
if "--out" in args:
    i = args.index("--out"); del args[i:i + 2]
mod = importlib.import_module(args[0])
names = args[1:] or [n for n, f in inspect.getmembers(mod, inspect.isfunction)
                     if f.__module__ == mod.__name__ and not n.startswith("_")]
html = open(os.path.join(os.path.dirname(TOOLS), "index.html"), encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
defs = re.search(r'(<svg width="0" height="0".*?</svg>)', html, re.S).group(1)
body = []
for n in names:
    s = getattr(mod, n)()
    if isinstance(s, dict):  # โมดูลแบบ apply_figs คืน fig(title, cap, svg)
        s = s["svg"]
    w = float(re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+)', s).group(1))
    body.append("<figure class='fig' id='f-%s'><div class='figt'>%s</div><div class='figsv'><div class='figin' style='max-width:%dpx'>%s</div></div></figure>"
                % (n, n, round(w * 1.25), s))
page = "<!doctype html><html><meta charset='utf-8'><style>%s body{padding:16px;max-width:860px}</style><body>%s%s</body></html>" % (css, defs, "".join(body))
os.makedirs(out, exist_ok=True)
pf = os.path.join(out, "_preview.html")
open(pf, "w", encoding="utf-8").write(page)
CHROME = next((p for p in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "/opt/pw-browsers/chromium"] if os.path.exists(p)), None)
CHECK = open(os.path.join(TOOLS, "check_render.py"), encoding="utf-8").read()
FIGJS = re.search(r'FIGJS = """(.*?)"""', CHECK, re.S).group(1).replace("main .fig svg", ".fig svg")
bad = 0
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"]) if CHROME else p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 900, "height": 1000})
    pg.goto("file://" + pf)
    pg.wait_for_timeout(300)
    for k, fb in enumerate(pg.evaluate(FIGJS)):
        print("%-14s %s" % (names[k], "✓" if not fb else "✗ " + " · ".join(fb[:6])))
        bad += bool(fb)
    for theme in ("light", "dark"):
        pg.evaluate("t => document.documentElement.setAttribute('data-theme', t)", theme)
        for n in names:
            pg.query_selector("#f-" + n).screenshot(path=os.path.join(out, "%s-%s.png" % (n, theme)))
    b.close()
print("ภาพอยู่ที่", out, "· ไม่มีสีประจำชุด (ใช้สี accent ตั้งต้นของหน้า)")
sys.exit(1 if bad else 0)
