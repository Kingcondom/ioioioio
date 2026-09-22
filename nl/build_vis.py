#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ประกอบพจนานุกรม นล. ภาค ข. จากผลอ่านหน้าด้วยสายตา (nl/vis/*.txt)"""
import json, os, re, collections

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "vis")
PART_B = "ข. ความรู้ความสามารถทางวิชาชีพและทักษะทางคลินิก"

rec = {}
section = ""          # หัวข้อระดับ 2.1 / 2.2 / 3.1 …
table = ""            # หัวข้อตาราง 2.3.x
for fn in sorted(os.listdir(SRC)):
    page = int(fn[:3])
    for ln in open(os.path.join(SRC, fn), encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip():
            continue
        if ln.startswith("@SEC "):
            section = ln[5:].split("|")[0].strip(); table = ""; continue
        if ln.startswith("@TBL "):
            table = ln[5:].strip(); continue
        code, _, title = ln.partition("\t")
        code, title = code.strip(), title.strip()
        if not title:
            raise SystemExit("บรรทัดไม่มีชื่อรายการ: %s (%s)" % (ln, fn))
        if code in rec:
            raise SystemExit("รหัสซ้ำ %s (%s)" % (code, fn))
        istbl = code.startswith("2.3.")
        rec[code] = {"code": code, "part": PART_B,
                     "section": table if istbl else section,
                     "system": "", "group": "3" if "-3(" in code else ("2" if istbl else ""),
                     "title": title, "page": page}

out = os.path.join(BASE, "nl_partB.json")
json.dump(rec, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)

c = collections.Counter(re.sub(r"[-(].*$", "", k) for k in rec)
print("รวม %d รหัส → %s" % (len(rec), out))
for k, n in sorted(c.items(), key=lambda x: [int(i) for i in x[0].split(".")]):
    print("  %-8s %3d" % (k, n))
