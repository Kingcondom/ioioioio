#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cardio คาบ 13 (IHD) หัวข้อ cardio-ihd-09: GRACE ใช้ตัดสินใจเฉพาะ unstable angina

ผู้ใช้คอมเมนต์ 26 ต.ค. 2569 ที่หัวข้อ GRACE risk score: "For only unstable angina นะ"
เหตุผล: NSTEMI เป็น high-risk criterion อยู่แล้ว (สวนภายใน 24 ชม. โดยไม่ต้องคิดคะแนน)
GRACE > 140 จึงเปลี่ยนการตัดสินใจจริงเฉพาะในผู้ป่วย UA ที่ troponin ไม่ขึ้น

ใช้: python3 patch_grace_ua.py <cardio.json ต้นทาง> <cardio.json ปลายทาง> · รันซ้ำได้
"""
import json, sys

SEC = "cardio-ihd-09"
HEAD = "### GRACE risk score\n"
MARK = "ใช้ตัดสินใจเฉพาะ unstable angina"
NOTE = ("\n> **GRACE ใช้ตัดสินใจเฉพาะ unstable angina** (troponin ไม่ขึ้น)\n"
        "> ผู้ป่วยที่วินิจฉัยเป็น **NSTEMI** เข้าเกณฑ์ high risk อยู่แล้ว ต้องสวนภายใน 24 ชั่วโมงโดยไม่ต้องคิดคะแนน\n"
        "> คะแนน **GRACE > 140** จึงเป็นตัวที่ยกผู้ป่วย UA ขึ้นเป็น high risk → early invasive · ถ้าคะแนนต่ำ → selective invasive (ตรวจก่อน)\n")
OLD_PEARL = "GRACE > 140 = high risk ต้องสวนภายใน 24 ชั่วโมง"
NEW_PEARL = "GRACE ใช้ตัดสินใจเฉพาะ UA (troponin ไม่ขึ้น) — NSTEMI เป็น high risk อยู่แล้ว · UA ที่ GRACE > 140 = high risk ต้องสวนภายใน 24 ชั่วโมง"

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
hit = [s for l in data for s in l["sections"] if s["id"] == SEC]
assert len(hit) == 1, "ไม่พบหัวข้อ %s" % SEC
s = hit[0]
if MARK in s["md"]:
    print("มีหมายเหตุอยู่แล้ว ไม่ได้แก้")
else:
    i = s["md"].find(HEAD)
    assert i >= 0 and s["md"].count(HEAD) == 1, "ไม่พบหัวข้อ GRACE แบบไม่ซ้ำ"
    j = s["md"].find("\n\n", i + len(HEAD))  # จบย่อหน้าแรกใต้หัวข้อ
    j = len(s["md"].rstrip("\n")) if j < 0 else j
    s["md"] = s["md"][:j] + "\n" + NOTE + s["md"][j:]
    s["pearls"] = [NEW_PEARL if p == OLD_PEARL else p for p in s["pearls"]]
    assert NEW_PEARL in s["pearls"], "ไม่พบ pearl เดิมเรื่อง GRACE"
    print("แก้แล้ว:", SEC)
# ข้อ CAR-IHD-MCQ-13 (NSTEMI + GRACE 165) คำตอบเดิมถูกอยู่แล้ว เติมหนึ่งบรรทัดให้สอดคล้องกับหมายเหตุ
QID = "CAR-IHD-MCQ-13"
QNOTE = ("\n\n> รายนี้แค่ **วินิจฉัย NSTEMI** ก็เข้าเกณฑ์ 24 ชั่วโมงแล้ว — **GRACE ใช้ตัดสินใจจริงเฉพาะ unstable angina** "
         "(troponin ไม่ขึ้น) ที่ต้องอาศัยคะแนน > 140 ยกขึ้นเป็น high risk")
q = [i for l in data for x in l["sections"] for i in x["items"] if i["id"] == QID]
assert len(q) == 1, "ไม่พบ " + QID
if "GRACE ใช้ตัดสินใจจริงเฉพาะ unstable angina" not in q[0]["explain"]:
    q[0]["explain"] = q[0]["explain"].rstrip("\n") + QNOTE
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
