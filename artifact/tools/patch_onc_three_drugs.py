#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hem/Onc คาบ 2/11 (General oncology) หัวข้อ hon-onc-06: เน้นว่าจำยามุ่งเป้าแค่ 3 ตัว

ผู้ใช้คอมเมนต์ 2 พ.ย. 2569 ที่ตาราง "HER family (EGFR) — ยาในสไลด์":
  "เน้นให้หน่อยว่าจำแค่ transumab and imatinib and erlotinib พอ"  (= trastuzumab)
เพิ่มกล่องเน้นใต้หัวข้อ + pearl ข้อแรก · ไม่แตะข้อสอบ

ใช้: python3 patch_onc_three_drugs.py <hemonc.json ต้นทาง> <ปลายทาง> · รันซ้ำได้
"""
import json, sys

SEC = "hon-onc-06"
HEAD = "### HER family (EGFR) — ยาในสไลด์\n"
MARK = "จำแค่ 3 ตัวพอ"
NOTE = ("> **จำแค่ 3 ตัวพอ** — ยาอื่นในตารางอ่านผ่านได้\n"
        "> - **Trastuzumab** → antibody ต่อ **HER2** · มะเร็งเต้านม/กระเพาะ **HER2 บวก** (IHC 3+ หรือ FISH บวก) · พิษหัวใจ **ผันกลับได้**\n"
        "> - **Imatinib** → TKI ต่อ **BCR-ABL** · **CML** (Philadelphia chromosome) · ต่อ KIT ด้วย → GIST\n"
        "> - **Erlotinib** → TKI ต่อ **EGFR** · **NSCLC (adenocarcinoma) ที่มี EGFR mutation** · ผื่นแบบสิว ท้องเสีย\n\n")
PEARL = "จำแค่ 3 ตัว: trastuzumab = HER2 (เต้านม/กระเพาะ) · imatinib = BCR-ABL (CML) · erlotinib = EGFR mutation (NSCLC)"

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
hit = [s for l in data for s in l["sections"] if s["id"] == SEC]
assert len(hit) == 1, "ไม่พบหัวข้อ " + SEC
s = hit[0]
if MARK in s["md"]:
    print("มีกล่องเน้นอยู่แล้ว ไม่ได้แก้")
else:
    assert s["md"].count(HEAD) == 1, "ไม่พบหัวข้อ HER family แบบไม่ซ้ำ"
    s["md"] = s["md"].replace(HEAD, HEAD + NOTE)
    s["pearls"] = [PEARL] + [p for p in s["pearls"] if p != PEARL]
    print("แก้แล้ว:", SEC)
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
