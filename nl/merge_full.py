#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""รวมพจนานุกรม นล. ฉบับเต็ม 2567 ทั้งภาค ก. และ ภาค ข. → build/data/nl.json"""
import json, os, re, collections

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(B, "artifact", "data")
NLD = os.path.join(B, "nl")
PART_A = "ก. วิทยาศาสตร์การแพทย์พื้นฐาน"
PART_B = "ข. ความรู้ความสามารถทางวิชาชีพและทักษะทางคลินิก"

A = json.load(open(os.path.join(NLD, "nl_partA.json"), encoding="utf-8"))
Bp = json.load(open(os.path.join(NLD, "nl_partB.json"), encoding="utf-8"))

SECTH = {
 "2.3.1":"โรคติดเชื้อและโรคปรสิต","2.3.2":"เนื้องอกและมะเร็ง",
 "2.3.3":"โรคเลือดและความผิดปกติของระบบภูมิคุ้มกัน","2.3.4":"โรคต่อมไร้ท่อ โภชนาการ และเมตาบอลิก",
 "2.3.5":"โรคทางจิตเวชและพฤติกรรม","2.3.6":"โรคระบบประสาท",
 "2.3.7":"โรคตาและอวัยวะเคียงลูกตา","2.3.8":"โรคหูและกระดูกมาสตอยด์",
 "2.3.9":"โรคระบบไหลเวียนโลหิต","2.3.10":"โรคระบบการหายใจ",
 "2.3.11":"โรคระบบทางเดินอาหาร","2.3.12":"โรคผิวหนังและเนื้อเยื่อใต้ผิวหนัง",
 "2.3.13":"โรคระบบกล้ามเนื้อ กระดูก และเนื้อเยื่อเกี่ยวพัน","2.3.14":"โรคระบบสืบพันธุ์และทางเดินปัสสาวะ",
 "2.3.15":"การตั้งครรภ์ การคลอด และระยะหลังคลอด","2.3.16":"ภาวะที่เกิดในระยะปริกำเนิด",
 "2.3.17":"ความพิการแต่กำเนิดและความผิดปกติของโครโมโซม",
 "2.3.18":"การบาดเจ็บ พิษ และผลจากสาเหตุภายนอก","2.3.19":"สาเหตุภายนอกของการเจ็บป่วยและการตาย",
 "2.1":"อาการ / ปัญหาสำคัญ","2.2":"โรค/ภาวะ/กลุ่มอาการฉุกเฉิน",
 "3.1":"การตรวจทางห้องปฏิบัติการและการตรวจพิเศษ","3.2":"การตรวจทางรังสีวิทยา","3.3":"การตรวจอื่น ๆ",
}

merged = {}
for src, part in ((A, PART_A), (Bp, PART_B)):
    for k, v in src.items():
        v = dict(v); v["part"] = part; v["source"] = "full-2567"
        merged[k] = v

# หัวข้อระดับหมวดของภาค ข.
for k, th in SECTH.items():
    n = sum(1 for x in Bp if x.startswith(k + ".") or x.startswith(k + "(") or x.startswith(k + "-3("))
    merged[k] = {"code": k, "part": PART_B, "section": "", "system": "", "group": "",
                 "title": "%s (ทั้งหมวด %d รายการ)" % (th, n), "page": 0, "source": "full-2567"}

# หัวข้อระดับหมวดของภาค ก. (B2 · B2.1 · B2.1.1 …) เพื่อให้รหัสย่อที่คาบอ้างถึงยังใช้ได้
prefixes = collections.Counter()
for k in A:
    base = re.sub(r"[-(].*$", "", k)          # B5.2.2-3(6) → B5.2.2
    parts = base.split(".")
    for i in range(1, len(parts) + 1):
        prefixes[".".join(parts[:i])] += 1
for p, n in prefixes.items():
    if p in merged:
        continue
    root = re.match(r"^B\d{1,2}", p).group(0)
    sample = next((v for v in A.values() if re.sub(r"[-(].*$", "", v["code"]).startswith(p)), None)
    merged[p] = {"code": p, "part": PART_A,
                 "section": sample["section"] if p.count(".") >= 2 and sample else "",
                 "system": sample["system"] if sample else "", "group": "",
                 "title": (sample["section"] if p.count(".") >= 2 and sample else
                           (sample["system"] if sample else p)) + " (ทั้งหมวด %d รายการ)" % n,
                 "page": sample["page"] if sample else 0, "source": "full-2567"}

json.dump(merged, open(os.path.join(D, "nl.json"), "w", encoding="utf-8"),
          ensure_ascii=False, separators=(",", ":"), sort_keys=True)

# แก้รหัสที่ไฟล์เดิมใช้แทนเลขซ้ำในเอกสาร
FIX = {"B5.2.2-3(2b)": "B5.2.2-3(6)", "B5.2.2-3(3b)": "B5.2.2-3(7)",
       "B5.2.2-3(4b)": "B5.2.2-3(8)"}
n = collections.Counter()
for fn in sorted(os.listdir(D)):
    if fn in ("index.json", "nl.json"):
        continue
    p = os.path.join(D, fn)
    data = json.load(open(p, encoding="utf-8"))
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("nl"), list):
                o["nl"] = sorted({FIX.get(c, c) for c in o["nl"]})
                for c in o["nl"]:
                    if c in FIX.values(): n[c] += 1
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(data)
    json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

ka = sum(1 for k in merged if k.startswith("B"))
print("พจนานุกรมรวม %d รหัส (ก. %d · ข. %d)" % (len(merged), ka, len(merged) - ka))
print("แก้รหัสในคาบเรียน:", dict(n))
