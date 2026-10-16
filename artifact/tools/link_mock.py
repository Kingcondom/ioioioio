#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ผูกข้อจาก Mock exam (คลัง bank_merged.json ชุด 'mock' — ไม่ผูกคาบ) เข้าหัวข้อของคาบในชุดใดก็ได้

    from link_mock import link_mock
    link_mock("gi", "12/10", {"gi-hep-03": ["MOCK-149"]})

ข้อ mock ลงเป็น kind "old" · ตรวจว่าไม่ถูกใช้ในคาบอื่นทั้งเว็บ · รันซ้ำได้"""
import json, os
from link_bank import bank_index, BUILD


def link_mock(setkey, lec, sections):
    idxm = bank_index("mock")
    path = os.path.join(BUILD, "data", setkey + ".json")
    d = json.load(open(path, encoding="utf-8"))
    L = [l for l in d if l["lec"] == lec][0]
    have = {i["id"] for s in L["sections"] for i in s["items"]}
    used = set()
    for f in os.listdir(os.path.join(BUILD, "data")):
        if f.endswith(".json") and f not in ("nl.json", "index.json"):
            for l in json.load(open(os.path.join(BUILD, "data", f), encoding="utf-8")):
                if f == setkey + ".json" and l["lec"] == lec:
                    continue
                used |= {i["id"] for s in l["sections"] for i in s["items"]}
    secs = {s["id"]: s for s in L["sections"]}
    n = 0
    for sid, ids in sections.items():
        assert sid in secs, "ไม่มีหัวข้อ " + sid
        for i in ids:
            assert i in idxm, "ไม่มีใน mock " + i
            assert i not in used, "ใช้ในคาบอื่นแล้ว " + i
            if i in have:
                continue
            it = dict(idxm[i]); it["kind"] = "old"
            it["topic"] = (it.get("topic") or "").split("·", 1)[-1].strip()
            it["ref"] = ["Mock exam MED421 — " + i] + list(it.get("ref", []))
            secs[sid]["items"].append(it); have.add(i); n += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return n
