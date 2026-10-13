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
        lv = open(p, "rb").read()
        if rel == "index.html":
            # บริการ artifact ห่อหน้าเว็บด้วยบรรทัดแรก <!doctype html><html><head>…<body> และปิดท้าย </body></html> เพิ่ม — ถอดออกก่อนเทียบ
            # (13 ต.ค. 2569: หน้าเว็บมีแพตช์ deep link จาก session dashboard ที่ repo ไม่มี — ถ้าไม่เทียบไฟล์นี้จะ publish ทับ)
            t = lv.decode("utf-8").split("\n")
            if t and t[0].startswith("<!doctype html><html><head><meta charset=utf8>"):
                body = "\n".join(t[1:]).rstrip()
                if body.endswith("</body></html>"):
                    body = body[:-len("</body></html>")]
                lv = (body.rstrip() + "\n").encode("utf-8")
        try:
            rp = (subprocess.run(["git", "-C", ROOT, "show", "%s:artifact/%s" % (base, rel)], capture_output=True, check=True).stdout
                  if base else open(os.path.join(ART, rel), "rb").read())
        except Exception:
            rp = None
        if rel == "index.html" and rp is not None:
            rp = (rp.decode("utf-8").rstrip() + "\n").encode("utf-8")
        same = rp is not None and h(lv) == h(rp)
        diff += not same
        print("%-22s เว็บ %s  repo %s  %s" % (rel, h(lv), h(rp) if rp else "—ไม่มี—", "ตรงกัน" if same else "ต่าง"))
print("\n" + ("✅ เว็บตรงกับ repo — publish ได้" if not diff else "⚠️ ต่างกัน %d ไฟล์ — ตรวจก่อนว่าเป็นไฟล์ที่เราตั้งใจแก้หรือมีคนอื่นแก้" % diff))
