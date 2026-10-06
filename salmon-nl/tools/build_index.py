#!/usr/bin/env python3
"""สร้าง data/index.json จาก tools/sets.json — ใส่เฉพาะชุดที่มีไฟล์ data/<set>.json แล้ว

ข้อความ intro ของแต่ละชุดอ่านจาก notes/<set>_intro.txt ถ้ามี
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sets = json.load(open(os.path.join(ROOT, "tools", "sets.json")))
HOWTO = ("**วิธีใช้** — เลือกหัวข้อย่อยจากแถบซ้าย อ่านสรุปแล้วตอบข้อสอบท้ายหัวข้อ เฉลยขึ้นทันทีพร้อมเหตุผลของทุกตัวเลือก · "
         "ตอบครบแล้วหัวข้อจะถูกติ๊กว่าเรียนจบ · แท็บ **สุ่มข้อสอบ** คละโจทย์ทั้งชุดแบบสนามจริง · "
         "ข้อที่ผิดทั้งหมดรวมอยู่ใน **ทบทวนข้อที่ผิด**")
out = []
for s in sets:
    f = os.path.join(ROOT, "data", s["set"] + ".json")
    if not os.path.exists(f):
        continue
    lecs = json.load(open(f))
    if not lecs:
        continue
    n_sec = sum(len(l["sections"]) for l in lecs)
    n_it = sum(len(x["items"]) for l in lecs for x in l["sections"])
    intro_f = os.path.join(ROOT, "notes", s["set"] + "_intro.txt")
    intro = open(intro_f).read().strip() if os.path.exists(intro_f) else (
        f"สรุปจากสไลด์ {s['deck']} (MedSalmon ติว NL by พี่ซี) แบ่งเป็น {len(lecs)} หมวด {n_sec} หัวข้อย่อย "
        f"แต่ละหัวข้อมีข้อสอบสไตล์ NL step 2 รวม {n_it} ข้อ")
    out.append({"set": s["set"], "label": s["label"], "thai": s["thai"],
                "title": f"{s['label']} · {s['thai']}", "source": "สไลด์ " + s["deck"],
                "intro": intro, "howto": HOWTO, "accent": s["accent"],
                "file": f"data/{s['set']}.json", "lectureCount": len(lecs)})
json.dump(out, open(os.path.join(ROOT, "data", "index.json"), "w"), ensure_ascii=False, indent=1)
print("index.json:", ", ".join(f"{o['set']}({o['lectureCount']})" for o in out))
