#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nephro คาบ 30 (UTI) หัวข้อ neph-uti-01: เพิ่ม "หลักจำ" ให้ภาพแยกกลุ่ม UTI

ผู้ใช้คอมเมนต์ 5 พ.ย. 2569 บนกล่องปัจจัยเสี่ยงในภาพ "แยกกลุ่มเพื่อเลือกการรักษา": "มี trick จำมั้ย"
เพิ่ม section.mnem 2 ชุด (แต่งเพิ่ม ไม่ได้มาจากสไลด์ — ระบุใน src):
  1) COMP-IR = ปัจจัยที่ทำให้เป็น complicated UTI (ครบทุกช่องในกล่องของภาพ)
  2) "มีไหม → ที่ไหน → ใคร" = สามคำถามของภาพ

ใช้: python3 patch_uti_mnem.py <nephro.json ต้นทาง> <ปลายทาง> · รันซ้ำได้
"""
import json, sys

SEC = "neph-uti-01"
MNEM = [
    {"name": "COMP-IR",
     "what": "ปัจจัยที่ทำให้ UTI เป็น complicated — คำว่า **COMP**licated สะกดให้เองสี่ตัวแรก",
     "lines": [
         ["C", "**C**atheter — สายสวน (ของให้เชื้อเกาะ)"],
         ["O", "**O**bstruction / st**O**ne — อุดกั้น · นิ่ว (ปัสสาวะไหลไม่ดี)"],
         ["M", "**M**ale — ผู้ชายทุกราย (ต่อมลูกหมาก)"],
         ["P", "**P**regnancy — ตั้งครรภ์"],
         ["I", "**I**mmunocompromised — DM · ยากดภูมิ · ปลูกถ่ายไต"],
         ["R", "**R**ecurrent — เป็นซ้ำ (บอกว่ามีปัจจัยซ่อนอยู่)"]],
     "note": "ทั้งหกตัวมาจากกลไกเดียวกัน คือกลไกป้องกันตามธรรมชาติเสีย — **ไหลไม่ดี · มีของให้เกาะ · ภูมิตก** · มีข้อใดข้อหนึ่ง = complicated แม้อาการจะเบา",
     "src": "หลักจำที่แต่งเพิ่มให้ตรงกับกล่องปัจจัยเสี่ยงในภาพ ไม่ได้มาจากสไลด์"},
    {"name": "มีไหม → ที่ไหน → ใคร",
     "what": "สามคำถามของภาพ เรียงตามลำดับที่ต้องถาม",
     "lines": [
         ["มีไหม", "มี**อาการ**ไหม — ไม่มี = **ASB** ไม่รักษา (ยกเว้นตั้งครรภ์ · ก่อนหัตถการ)"],
         ["ที่ไหน", "อาการบอก**ตำแหน่ง** — แสบขัด ปวดท้องน้อย = cystitis · ไข้ ปวดเอว CVA เจ็บ = pyelonephritis"],
         ["ใคร", "**ผู้ป่วย**คือใคร — เข้า COMP-IR = complicated (ยากว้าง นาน หาสาเหตุ) · ไม่เข้า = uncomplicated"]],
     "src": "หลักจำที่แต่งเพิ่ม ไม่ได้มาจากสไลด์"},
]

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
hit = [s for l in data for s in l["sections"] if s["id"] == SEC]
assert len(hit) == 1, "ไม่พบหัวข้อ " + SEC
s = hit[0]
have = [m.get("name") for m in (s.get("mnem") or [])]
add = [m for m in MNEM if m["name"] not in have]
if add:
    s["mnem"] = (s.get("mnem") or []) + add
    print("เพิ่มหลักจำ:", [m["name"] for m in add])
else:
    print("มีหลักจำอยู่แล้ว ไม่ได้แก้")
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
