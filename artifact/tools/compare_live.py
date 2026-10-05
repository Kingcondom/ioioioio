#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เทียบไฟล์บนเว็บ (ที่โหลดด้วย Artifact read แบบ paths) กับไฟล์ใน repo ก่อน publish

    python3 artifact/tools/compare_live.py <โฟลเดอร์ที่ Artifact read บันทึกไว้> [commit ฐาน]

- ไม่ใส่ commit: เทียบกับ HEAD ของไฟล์ data/ ใน repo ตอนนี้
- ใส่ commit: เทียบกับไฟล์ ณ commit นั้น (ใช้ตอนแก้ไฟล์ไปแล้ว อยากรู้ว่าเว็บยังเป็นฐานเดิมไหม)
ถ้ามีไฟล์ "ต่าง" ที่เราไม่ได้แก้ = มี session อื่น publish ทับมา → ห้าม publish ทับ ต้องหา branch แล้ว merge ก่อน"""
import hashlib, os, subprocess, sys

ART = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(ART)
live = sys.argv[1]
base = sys.argv[2] if len(sys.argv) > 2 else None
h = lambda b: hashlib.sha256(b).hexdigest()[:12]
diff = 0
for dp, _, fs in os.walk(live):
    for f in sorted(fs):
        p = os.path.join(dp, f); rel = os.path.relpath(p, live)
        if rel == "index.html":
            continue  # บริการ artifact ห่อหน้าเว็บเพิ่ม เทียบตรง ๆ ไม่ได้
        lv = open(p, "rb").read()
        try:
            rp = (subprocess.run(["git", "-C", ROOT, "show", "%s:artifact/%s" % (base, rel)], capture_output=True, check=True).stdout
                  if base else open(os.path.join(ART, rel), "rb").read())
        except Exception:
            rp = None
        same = rp is not None and h(lv) == h(rp)
        diff += not same
        print("%-22s เว็บ %s  repo %s  %s" % (rel, h(lv), h(rp) if rp else "—ไม่มี—", "ตรงกัน" if same else "ต่าง"))
print("\n" + ("✅ เว็บตรงกับ repo — publish ได้" if not diff else "⚠️ ต่างกัน %d ไฟล์ — ตรวจก่อนว่าเป็นไฟล์ที่เราตั้งใจแก้หรือมีคนอื่นแก้" % diff))
