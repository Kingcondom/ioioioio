#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ความครอบคลุมของคลัง Ward Drill (bank_merged.json) เทียบกับบทเรียนใน artifact/data

    python3 artifact/tools/coverage.py              # สรุปทุกชุด + คาบที่ยังไม่มีบทเรียน
    python3 artifact/tools/coverage.py --find AF     # หาเลขคาบจริงและข้อในคลังของหัวข้อ (ค้นจากชื่อคาบ/หัวข้อ/โจทย์)

ใช้ก่อนเริ่มคาบใหม่: ถ้าคลังมีคาบนั้น → ใช้เลข lec ของคลัง และผูกข้อด้วย link_bank.py"""
import json, os, re, sys, glob
from collections import OrderedDict

ART = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(ART)
bank = json.load(open(os.path.join(ROOT, "bank_merged.json"), encoding="utf-8"))

used = {}
for f in glob.glob(os.path.join(ART, "data", "*.json")):
    if f.endswith(("nl.json", "index.json")):
        continue
    st = os.path.basename(f)[:-5]
    for L in json.load(open(f, encoding="utf-8")):
        for s in L["sections"]:
            for i in s["items"]: used[i["id"]] = (st, L["lec"], s["id"])
        for x in L["meq"] + L["osce"]: used[x["id"]] = (st, L["lec"], "meq/osce")

def bank_items(v):
    for k, g in v.items():
        if k == "hot":
            continue
        for x in g:
            for y in (x["items"] if isinstance(x, dict) and "items" in x else [x]):
                if isinstance(y, dict) and y.get("id"):
                    yield k, dict(y, lec=str(y.get("lec", x.get("lec") if isinstance(x, dict) else "")),
                                  lecture=y.get("lecture", x.get("lecture") if isinstance(x, dict) else ""))

if "--find" in sys.argv:
    q = re.compile(sys.argv[sys.argv.index("--find") + 1], re.I)
    for st, v in bank.items():
        for k, y in bank_items(v):
            txt = " ".join(str(y.get(f, "")) for f in ("lecture", "topic", "stem", "q"))
            if q.search(txt):
                print("%-7s lec %-4s %-6s %-11s %-8s | %s | %s" % (st, y["lec"], k, y["id"],
                      "ผูกแล้ว" if y["id"] in used else "ว่าง", str(y.get("lecture"))[:40], str(y.get("topic") or y.get("stem") or y.get("q"))[:60]))
    sys.exit(0)

T = U = 0
todo = []
for st, v in bank.items():
    lecs = OrderedDict()
    for k, y in bank_items(v):
        d = lecs.setdefault(y["lec"], {"name": y["lecture"], "n": 0, "u": 0})
        d["n"] += 1; d["u"] += y["id"] in used
    n = sum(d["n"] for d in lecs.values()); u = sum(d["u"] for d in lecs.values())
    if st != "mock":
        T += n; U += u
    print("%-7s %3d/%-3d %s" % (st, u, n, "(ไม่ผูกคาบ)" if st == "mock" else ""))
    for lec, d in lecs.items():
        if st != "mock" and d["u"] < d["n"]:
            todo.append("  %-7s คาบ %-4s %3d/%-3d %s" % (st, lec, d["u"], d["n"], str(d["name"])[:60]))
print("รวม (ไม่นับ mock) %d/%d ข้อ = %d%%\n\nคาบในคลังที่ยังผูกไม่ครบ:" % (U, T, round(100 * U / T)))
print("\n".join(todo) or "  — ครบทุกคาบ")
