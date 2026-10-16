#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ผูกข้อสอบจากคลัง bank_merged.json (คลังเดียวกับ Ward Drill) เข้าหัวข้อของคาบที่มีบทเรียนแล้ว

ใช้จากสคริปต์อื่น:
    from link_bank import link
    link("cardio", "24/9", {"cardio-ihd-01": ["C-MCQ-14", "C-OLD-35"], ...}, meq=["C-MEQ-01"], osce=["C-OSCE-01"])

- แปลงรูปแบบข้อในคลังเป็น item ของ learn (old: q→stem, note→explain)
- รันซ้ำได้ — ข้อที่ผูกไว้แล้วจะไม่ถูกเพิ่มซ้ำ
- ตรวจว่า id ในคลังมีจริง และไม่ถูกใช้ในคาบอื่นแล้ว"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
BANK = os.path.join(os.path.dirname(BUILD), "bank_merged.json")


def bank_index(setkey):
    s = json.load(open(BANK, encoding="utf-8"))[setkey]
    idx = {}
    for it in s.get("mcq", []):
        idx[it["id"]] = {"id": it["id"], "kind": "mcq", "stem": it["stem"], "choices": it["choices"],
                         "answer": it["answer"], "explain": it.get("explain", ""), "pearl": it.get("pearl", ""),
                         "topic": it.get("topic", ""), "src": "", "ref": it.get("ref", []), "nl": it.get("nl", [])}
    for g in s.get("old", []):
        for it in g.get("items", []):
            if "choices" in it:
                idx[it["id"]] = {"id": it["id"], "kind": "old", "stem": it["q"], "choices": it["choices"],
                                 "answer": it["answer"], "explain": it.get("note", ""), "pearl": it.get("pearl", ""),
                                 "topic": it.get("topic", ""), "src": it.get("src", ""), "ref": it.get("ref", []),
                                 "nl": it.get("nl", [])}
    for it in s.get("meq", []):
        idx[it["id"]] = dict(it, years=it.get("years", []), _kind="meq", _set=setkey)
    return idx


def link(setkey, lec, sections, meq=(), osce=()):
    path = os.path.join(BUILD, "data", setkey + ".json")
    data = json.load(open(path, encoding="utf-8"))
    L = [l for l in data if l["lec"] == lec][0]
    idx = bank_index(setkey)
    used_elsewhere = set()
    for l in data:
        if l is L:
            continue
        for s in l["sections"]:
            used_elsewhere |= {i["id"] for i in s["items"]}
        used_elsewhere |= {x["id"] for x in l["meq"] + l["osce"]}
    here = {i["id"] for s in L["sections"] for i in s["items"]} | {x["id"] for x in L["meq"] + L["osce"]}
    secs = {s["id"]: s for s in L["sections"]}
    added = 0
    for sid, ids in sections.items():
        assert sid in secs, "ไม่มีหัวข้อ " + sid
        for i in ids:
            assert i in idx, "ไม่มีในคลัง " + i
            assert i not in used_elsewhere, "ใช้ในคาบอื่นแล้ว " + i
            if i in here:
                continue
            assert len(idx[i]["choices"]) == 5, i
            secs[sid]["items"].append(idx[i]); here.add(i); added += 1
    for key, ids in (("meq", meq), ("osce", osce)):
        for i in ids:
            assert i in idx and i not in used_elsewhere, i
            if i not in here:
                L[key].append(idx[i]); here.add(i); added += 1
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return added
