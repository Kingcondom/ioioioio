#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ประกอบพจนานุกรม นล. ภาค ก. จากผลอ่านหน้าด้วยสายตา (nl/visA/*.txt)"""
import json, os, re, collections

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "visA")
PART_A = "ก. วิทยาศาสตร์การแพทย์พื้นฐาน"

rec, sysname = {}, {}
sysnow, table, section = "", "", ""
for fn in sorted(f for f in os.listdir(SRC) if f.endswith(".txt")):
    page = int(fn[:3])
    for ln in open(os.path.join(SRC, fn), encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip():
            continue
        if ln.startswith("@SYS "):
            code, _, name = ln[5:].partition("\t")
            sysnow = code.strip(); sysname[sysnow] = name.strip(); continue
        if ln.startswith("@TBL "):
            body = ln[5:]
            table, _, section = body.partition("|")
            table, section = table.strip(), section.strip()
            continue
        code, _, title = ln.partition("\t")
        code, title = code.strip(), title.strip()
        if not title:
            raise SystemExit("บรรทัดไม่มีชื่อรายการ: %r (%s)" % (ln, fn))
        if code in rec:
            raise SystemExit("รหัสซ้ำ %s (%s)" % (code, fn))
        root = re.match(r"^B\d{1,2}", code).group(0)
        rec[code] = {"code": code, "part": PART_A, "section": table or section,
                     "system": sysname.get(root, ""),
                     "group": "3" if "-3(" in code else "1-2",
                     "title": title, "page": page}

out = os.path.join(BASE, "nl_partA.json")
json.dump(rec, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
c = collections.Counter(re.match(r"^B\d{1,2}", k).group(0) for k in rec)
print("รวม %d รหัส → %s" % (len(rec), out))
print(" · ".join("%s=%d" % (k, c[k]) for k in sorted(c, key=lambda x: int(x[1:]))))
print("กลุ่ม:", dict(collections.Counter(v["group"] for v in rec.values())))
