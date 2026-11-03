#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liver cirrhosis and complications (อ. 3 พ.ย. 2569 · ผศ.สยาม ศิรินธรปัญญา · GI unit รพ.ราชวิถี)
→ data/gi.json (คาบ "3/11")

ต้นฉบับ: Google Drive "Lec Cirrhosis and complication Rx.pdf" (51 หน้า)
fileId 146DmuSy-7gIZ_aZaTJNI94ZSdn-DrjDF · เนื้อหาแบ่งเขียนใน tools/cir/part*.py
"""
import json, os, glob

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
SRC = "สไลด์ ผศ.สยาม — Cirrhosis and complication Rx"
NL = ["2.3.11(4)", "B8.2.5(4)"]
S = []


def sec(sid, title, summary, minutes, md, pearls, items, nl=None, figs=None, anims=None, mnem=None, source=SRC):
    s = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
         "nl": nl or NL, "md": md.strip() + "\n", "pearls": pearls, "items": items}
    if figs:
        s["figs"] = figs
    if anims:
        s["anims"] = anims
    if mnem:
        s["mnem"] = mnem
    S.append(s)


def mcq(iid, stem, choices, answer, explain, pearl, topic, ref=None, nl=None):
    assert len(choices) == 5 and 0 <= answer < 5, iid
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "",
            "ref": ref or [SRC], "nl": nl or NL}


BANK = {i["id"]: i for i in json.load(open(os.path.join(os.path.dirname(BUILD), "bank_merged.json"),
                                            encoding="utf-8"))["mock"]["mcq"]}


def old(mid, nl=None, pearl=""):
    """ข้อจาก Mock exam MED421 (NL Part 1 Mock Assessment) — รูปแบบเดียวกับ MOCK-149 ในคาบ hepatitis"""
    q = BANK[mid]
    n = int(mid.split("-")[1])
    sect = q["ref"][0].split("·")[-1].strip() if q.get("ref") else "Gastroenterology"
    return {"id": mid, "kind": "old", "stem": q["stem"], "choices": q["choices"], "answer": q["answer"],
            "explain": q["explain"], "pearl": pearl, "topic": q["topic"].split("·", 1)[-1].strip(),
            "src": "", "ref": ["Mock exam MED421 — " + mid,
                               "NL Part 1 Mock Assessment (200 ข้อ) — ข้อ %d · %s" % (n, sect)],
            "nl": nl or q.get("nl") or NL}


HERE = os.path.dirname(os.path.abspath(__file__))
G = {"sec": sec, "mcq": mcq, "old": old, "NL": NL, "SRC": SRC}
for f in sorted(glob.glob(os.path.join(HERE, "cir", "part*.py"))):
    exec(compile(open(f, encoding="utf-8").read(), f, "exec"), G)

LEC = G["LECTURE"]
LEC["sections"] = S

# ---- ตรวจความถูกต้องก่อนเขียนไฟล์ ----
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
ids = set()
for s in S:
    for c in s["nl"]:
        assert c in nl, (s["id"], c)
    for k in (s.get("figs") or {}):
        assert "[[fig:%s]]" % k in s["md"], (s["id"], k)
    for k in (s.get("anims") or {}):
        assert "[[anim:%s]]" % k in s["md"], (s["id"], k)
    assert "```" not in s["md"], s["id"]
    for it in s["items"]:
        assert it["id"] not in ids, it["id"]
        ids.add(it["id"])
        for c in it["nl"]:
            assert c in nl or c.count(".") == 2, (it["id"], c)
for q in LEC["meq"] + LEC["osce"]:
    assert q["id"] not in ids
    ids.add(q["id"])

path = os.path.join(BUILD, "data", "gi.json")
d = json.load(open(path, encoding="utf-8"))
d = [l for l in d if l["lec"] != LEC["lec"]] + [LEC]
open(path, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))

ip = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ip, encoding="utf-8"))
for m in idx:
    if m["set"] == "gi":
        m["lectureCount"] = len(d)
        m["intro"] = G["GI_INTRO"]
        m["howto"] = G["GI_HOWTO"]
open(ip, "w", encoding="utf-8").write(json.dumps(idx, ensure_ascii=False, indent=1))

print("คาบ %s: %d หัวข้อ · %d ข้อ · MEQ %d · OSCE %d · gi รวม %d คาบ" % (
    LEC["lec"], len(S), sum(len(s["items"]) for s in S), len(LEC["meq"]), len(LEC["osce"]), len(d)))
