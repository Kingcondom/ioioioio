#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nephro คาบ 30 หัวข้อ neph-uti-06: เน้นใจความของ "ใครคือ acute simple cystitis"

ผู้ใช้คอมเมนต์ 5 พ.ย. 2569 (ที่ตัวหนา "ไม่มีไข้ ไม่ปวดเอว ไม่มีตกขาว"): "เน้นให้มันถูกใจความหน่อย"
ย่อหน้าเดิมเป็นประโยคยาว ตัวหนาไม่ได้บอกว่าแต่ละข้อมีไว้ทำไม → แยกเป็นสูตรสามส่วน
(คนปกติ + อาการอยู่แค่กระเพาะ + ไม่ใช่โรคอื่น/ยังไม่ขึ้นไต) และให้ตัวหนาตกที่ความหมายของแต่ละข้อ

ใช้: python3 patch_cystitis_who.py <nephro.json ต้นทาง> <nephro.json ปลายทาง> · รันซ้ำได้
"""
import json, sys

SEC = "neph-uti-06"
OLD = ("### ใครคือ acute simple cystitis\n"
       "**หญิงไม่ตั้งครรภ์ ทางเดินปัสสาวะปกติ** มีแสบขัด ปัสสาวะบ่อย ปวดกลั้น ปวดหน่วงท้องน้อย **ไม่มีไข้ ไม่ปวดเอว ไม่มีตกขาว**\n")
NEW = ("### ใครคือ acute simple cystitis\n"
       "> **simple cystitis = คนปกติ + อาการอยู่แค่กระเพาะ + ไม่มีอะไรบอกว่าเป็นอย่างอื่น**\n"
       "\n"
       "- **คนปกติ** — หญิงไม่ตั้งครรภ์ ทางเดินปัสสาวะปกติ (ไม่เข้า COMP-IR)\n"
       "- **อาการอยู่แค่กระเพาะ** — แสบขัด, ปัสสาวะบ่อย, ปวดกลั้น, ปวดหน่วงท้องน้อย\n"
       "- **ไม่มีไข้ ไม่ปวดเอว** → เชื้อ **ยังไม่ขึ้นไต** (มีเมื่อไร = pyelonephritis เปลี่ยนยา)\n"
       "- **ไม่มีตกขาว** → **ไม่ใช่ vaginitis / STI** ที่อาการแสบขัดคล้ายกัน\n"
       "\n")

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
hit = [s for l in data for s in l["sections"] if s["id"] == SEC]
assert len(hit) == 1, "ไม่พบหัวข้อ %s" % SEC
s = hit[0]
if NEW in s["md"]:
    print("แก้ไว้แล้ว")
else:
    assert s["md"].count(OLD) == 1, "ข้อความเดิมเปลี่ยนไปแล้ว ตรวจด้วยมือ"
    s["md"] = s["md"].replace(OLD, NEW)
    print("แก้แล้ว:", SEC)
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
