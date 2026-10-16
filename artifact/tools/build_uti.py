#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 30 Urinary tract infection (อ.กรทิพย์ · Korntip Phonphok, MD) → data/nephro.json
ต้นฉบับ: Drive 1OeevfDxn_c6H3iLUw6nXIjPOv6DPHawD "Lec5 UTI_4thRSU2026.pdf" · บรรยาย ศ. 18 ก.ย. 2569
โน้ตสไลด์: slides/uti_notes.md — ดึงข้อความได้ครบเฉพาะสไลด์ตัวอักษร · สไลด์ภาพ (urinalysis, culture, Gram stain,
รูป pathogenesis, ภาพ CT/US) อ่านไม่ได้ → เนื้อหาส่วนนั้น กลไกของอาการ และ prostatitis อิงแนวทาง/ตำรา และระบุไว้ในบทเรียน
ผู้ใช้ขอ (13 ต.ค. 2569): อธิบาย pathophysiology ของอาการเด่นแต่ละโรค + ภาพประกอบ → ทุกหัวข้อมี "ทำไมถึงมีอาการนี้" และภาพ SVG
ข้อสอบคลัง Ward Drill คาบ 30 (22 ข้อ) + คาบ 28 สามข้อ (N-OLD-087, N-MCQ-26, N-OLD-074) + Mock M01 ผูกท้ายสคริปต์"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link
from link_mock import link_mock
from svg import *

LEC = "30"
NLN = ["B9.2.2(1)", "B9.2.2(2)", "2.3.14(7)", "2.3.14(14)"]
SRC = "สไลด์ อ.กรทิพย์ — Urinary Tract Infection (4th year RSU 2026)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, figs=None, source=None):
    d = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source or SRC,
         "nl": nl or NLN, "md": md, "pearls": pearls, "items": items}
    if figs: d["figs"] = figs
    S.append(d)
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "NEPH-UTI-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.กรทิพย์ — " + p]

# ───────────────────────────── 1
F1 = {
 "venn": fig("UTI = เชื้อ + การอักเสบ + อาการ",
  "สามวงคือสามสิ่งที่สไลด์ย้ำว่า **ไม่ใช่สิ่งเดียวกัน** · UTI ต้องมีครบทั้งสาม (ตรงกลาง) · **มีเชื้อและ pyuria แต่ไม่มีอาการ = asymptomatic bacteriuria** ซึ่งโดยทั่วไปไม่รักษา · **pyuria ที่ไม่มีเชื้อ = sterile pyuria** (ได้ยามาก่อน TB AIN นิ่ว) · **มีเชื้อและอาการแต่ไม่มี pyuria** ให้นึกถึงผู้ป่วย neutropenia · **อาการอย่างเดียว** ให้นึกถึง vaginitis urethritis painful bladder syndrome",
  svg(420, 340, "แผนภาพเวนน์ของ bacteriuria pyuria และอาการ",
      circ(155, 132, 100, "lac w2"), circ(265, 132, 100, "lms w2"), circ(210, 226, 100, "lbad w2"),
      t(82, 18, "Bacteriuria", "b tac mid"), t(82, 40, "เพาะเชื้อขึ้น", "sm mu mid"),
      t(338, 18, "Pyuria", "b tms mid"), t(338, 40, "WBC ≥ 5/HPF", "sm mu mid"),
      t(210, 336, "อาการของ UTI", "b tbad mid"),
      t(100, 112, "ปนเปื้อน /\ncolonization", "sm mid i2"),
      t(320, 112, "Sterile\npyuria", "sm mid i2"),
      t(210, 68, "ASB", "b mid"), t(210, 90, "มักไม่รักษา", "xs mid mu"),
      t(210, 164, "UTI", "lg b mid"), t(210, 188, "รักษา", "xs mid mu"),
      t(150, 204, "ไม่มี WBC", "xs mid i2"), t(150, 218, "neutropenia", "xs mid mu"),
      t(270, 204, "ได้ยามาก่อน", "xs mid i2"), t(270, 218, "TB · AIN", "xs mid mu"),
      t(210, 290, "vaginitis\nurethritis", "sm mid i2"))),
 "classify": fig("แยกกลุ่มเพื่อเลือกการรักษา",
  "คำถามแรกคือ **มีอาการหรือไม่** (ไม่มี = ASB) · คำถามที่สองคือ **อาการบอกตำแหน่ง** — ไข้ ปวดเอว เคาะ CVA เจ็บ = ลุกลามถึงไต · คำถามสุดท้ายคือ **ผู้ป่วยมีปัจจัยที่ทำลายกลไกป้องกันหรือไม่** ถ้ามี = complicated ต้องใช้ยากว้างขึ้น นานขึ้น และหาสาเหตุ (หัวข้อ 8)",
  svg(420, 440, "แผนผังแยก ASB cystitis pyelonephritis และ complicated UTI",
      box(20, 10, 250, 40, "sk", "Bacteriuria — เพาะเชื้อขึ้น"),
      ar(145, 50, 145, 76, "ln", "ah"),
      box(20, 78, 250, 38, "bx", "มีอาการของ UTI หรือไม่"),
      ar(270, 97, 296, 97, "lms", "ah-ms", "ไม่", "xs i2 mid"),
      box(298, 70, 112, 54, "ms", "ASB\nไม่มีอาการ"),
      t(354, 142, "ไม่รักษา ยกเว้น\nตั้งครรภ์\nก่อนหัตถการ", "xs mid i2"),
      ar(145, 116, 145, 142, "ln", "ah", "มี", "xs i2", dx=14, dy=4),
      box(20, 144, 250, 38, "bx", "อาการบอกตำแหน่ง"),
      ar(82, 182, 82, 208, "ln", "ah"), ar(208, 182, 208, 208, "ln", "ah"),
      box(20, 210, 124, 62, "ac", "Cystitis\nแสบขัด · บ่อย\nปวดท้องน้อย", fs=12),
      box(146, 210, 124, 62, "bad", "Pyelonephritis\nไข้ · ปวดเอว\nCVA tender", fs=12),
      ar(82, 272, 82, 298, "ln", "ah"), ar(208, 272, 208, 298, "ln", "ah"),
      box(20, 300, 250, 38, "bx", "ผู้ป่วยมีปัจจัยเสี่ยงไหม"),
      rect(298, 192, 112, 176, "sk"),
      t(354, 212, "ปัจจัยเสี่ยง", "sm b mid"),
      t(354, 233, "ชาย\nDM · ภูมิต่ำ\nตั้งครรภ์\nปลูกถ่ายไต\nเป็นซ้ำ\nนิ่ว · อุดกั้น\nสายสวน", "sm mid i2", 1.5),
      ar(298, 319, 272, 319, "lmu da", "ah-mu"),
      ar(82, 338, 82, 370, "lok", "ah-ok", "ไม่มี", "xs i2", dx=20, dy=4),
      ar(208, 338, 208, 370, "lbad", "ah-bad", "มี", "xs i2", dx=14, dy=4),
      box(20, 372, 124, 56, "ok", "Uncomplicated\nยามาตรฐาน", fs=12),
      box(146, 372, 124, 56, "bad", "Complicated\nยากว้าง + หาสาเหตุ", fs=12))),
}
sec("neph-uti-01", "UTI คืออะไร — แยกให้ออกจาก bacteriuria และ pyuria",
    "นิยาม · UTI ≠ bacteriuria ≠ pyuria · เพาะเชื้อก่อนให้ยา · ห้ากลุ่มของ UTI · เคสนำสี่รายของอาจารย์", 8,
"""### นิยาม (สไลด์)
**Urinary tract infection (UTI)** คือการมีแบคทีเรียหรือจุลชีพอื่น **ในปัสสาวะหรือเนื้อเยื่อของทางเดินปัสสาวะ** จนก่อโรค — สไลด์ย้ำว่า **UTI ≠ bacteriuria และ UTI ≠ pyuria**
- **Bacteriuria** = มีเชื้อในปัสสาวะ — อาจเป็นแค่ปนเปื้อนตอนเก็บ หรือเชื้อที่อยู่ร่วมโดยไม่ก่อโรค (colonization)
- **Pyuria** = มีเม็ดเลือดขาวในปัสสาวะ — บอกว่า **มีการอักเสบ** แต่ไม่ได้บอกว่าอักเสบจากอะไร
- **UTI** = มีเชื้อ + ร่างกายตอบสนองจน **มีอาการ** ต้องครบทั้งสามองค์ประกอบ

[[fig:venn]]

### ทำไมต้องเพาะเชื้อ และต้องเพาะ "ก่อน" ให้ยา
- การวินิจฉัยและรักษาที่ถูกต้อง **ต้องยืนยันด้วย urine culture** (สไลด์)
- **เก็บปัสสาวะส่งเพาะเชื้อก่อนเริ่มยาเสมอ** — ยาปฏิชีวนะส่วนใหญ่ถูกขับออกทางไตในความเข้มข้นสูงกว่าในเลือดหลายเท่า ให้ยาไปเพียงหนึ่งหรือสองโดส ปัสสาวะก็ปลอดเชื้อแล้ว ทั้งที่เชื้อในเนื้อไตยังไม่ตาย → เพาะไม่ขึ้น เสียโอกาสรู้ว่าเชื้อดื้อยาอะไร
- ผู้หญิงมักมีเชื้อจาก **ช่องคลอดและรอบรูเปิดท่อปัสสาวะ** ปนมาในปัสสาวะที่ถ่ายออกมา → ต้องใช้ **เกณฑ์จำนวนเชื้อ (quantitative criterion)** แยกเชื้อก่อโรคจากการปนเปื้อน (หัวข้อ 5)

### ห้ากลุ่มของ UTI — เป็นโครงของทั้งคาบ
| กลุ่ม | ตำแหน่ง | ใคร | ความหมายต่อการรักษา |
|---|---|---|---|
| **Acute simple cystitis** | กระเพาะปัสสาวะ | หญิงไม่ตั้งครรภ์ ทางเดินปัสสาวะปกติ | ยากินระยะสั้น (หัวข้อ 6) |
| **Acute uncomplicated pyelonephritis** | กรวยไตและเนื้อไต | หญิง ทางเดินปัสสาวะปกติ | ยาที่เข้าเนื้อไตได้ (หัวข้อ 7) |
| **Complicated UTI** | ตำแหน่งใดก็ได้ | ชาย · DM/ภูมิต่ำ · ตั้งครรภ์ · ปลูกถ่ายไต · เป็นซ้ำ | ยากว้างขึ้น นานขึ้น หาสาเหตุ (หัวข้อ 8–9) |
| **Recurrent UTI** | — | ≥ 2 ครั้งใน 6 เดือน หรือ ≥ 3 ครั้งใน 12 เดือน | หาปัจจัยเสี่ยงและป้องกัน (หัวข้อ 10) |
| **Asymptomatic bacteriuria (ASB)** | — | มีเชื้อแต่ไม่มีอาการ | **ไม่รักษา** ยกเว้นบางกลุ่ม (หัวข้อ 13) |

[[fig:classify]]

#### คำว่า "complicated" ไม่ได้แปลว่า "อาการหนัก"
Complicated แปลว่า **ปัจจัยของผู้ป่วยทำให้กลไกป้องกันตามธรรมชาติเสียไป** — ปัสสาวะไหลไม่ดี (อุดกั้น นิ่ว ต่อมลูกหมากโต) มีสิ่งแปลกปลอมให้เชื้อเกาะ (สายสวน นิ่ว) หรือภูมิคุ้มกันต่ำ (เบาหวาน ยากดภูมิ) ผลคือ
- เชื้อหลากหลายกว่า และ **ดื้อยามากกว่า**
- **ยาอย่างเดียวอาจไม่พอ** ถ้าไม่แก้ปัจจัยนั้น (เช่น ไม่ระบายไตที่อุดกั้น)
ผู้ป่วย cystitis ที่เป็นชายก็จัดเป็น complicated แม้จะไม่มีไข้ (สไลด์)

### เคสนำสี่รายของอาจารย์ — ทั้งคาบจะตอบเคสเหล่านี้
| เคส | เรื่องเล่า (สไลด์) | ควรคิดถึง | อ่านต่อ |
|---|---|---|---|
| 1 | หญิง 48 ปี **ไข้** แสบขัด ปัสสาวะบ่อย ปวดท้องน้อย 1 วัน · เป็นแบบนี้ **2 ครั้งใน 6 เดือน** ซื้อยากินเอง | **Recurrent UTI** (อาจารย์เขียนกำกับว่า recurrent) · มีไข้ต้องแยก pyelonephritis | 6, 10 |
| 2 | ชาย 55 ปี **ไข้สูง หนาวสั่น ปวดสีข้างขวา 6 ชั่วโมง** | **Pyelonephritis → septicemia** (อาจารย์เขียนว่า concern septic shock) | 7, 8 |
| 3 | ชาย 45 ปี ไข้กลางคืน เหนื่อย น้ำหนักลด 1 เดือน · **UA WBC 30–50/HPF ได้ยาแล้วไม่ดีขึ้น** | **Sterile pyuria** — GU TB, interstitial nephritis | 5 |
| 4 | ชาย 70 ปี **ปัสสาวะขัดมากขึ้น 1 วัน ไม่มีไข้** | UTI ในชาย = **complicated** · ต่อมลูกหมาก | 9 |
""",
    ["UTI = เชื้อ + การอักเสบ + อาการ — UTI ≠ bacteriuria ≠ pyuria",
     "เก็บ urine culture ก่อนให้ยาเสมอ เพราะยาขับทางปัสสาวะทำให้ปัสสาวะปลอดเชื้อเร็วมาก",
     "Complicated = ปัจจัยของผู้ป่วยทำลายกลไกป้องกัน ไม่ได้แปลว่าอาการหนัก",
     "ชายที่เป็น UTI จัดเป็น complicated เสมอ (สไลด์)",
     "มีเชื้อแต่ไม่มีอาการ = ASB ซึ่งส่วนใหญ่ไม่ต้องรักษา"],
    [mcq(N(1), "A 30-year-old non-pregnant woman has two consecutive clean-catch urine cultures, taken one week apart for a pre-employment check-up, that both grow Escherichia coli at more than 100,000 CFU/mL. She has no urinary symptoms and no fever. Urinalysis shows WBC 10-20/HPF. Which term best describes her condition?",
         ["Acute uncomplicated cystitis", "Asymptomatic bacteriuria", "Sterile pyuria", "Complicated urinary tract infection", "Specimen contamination"], 1,
         "มีเชื้อชนิดเดียวกัน **≥ 10⁵ CFU/mL สองครั้งติดกัน** โดย **ไม่มีอาการ** = **asymptomatic bacteriuria (ASB)** — pyuria ที่พบร่วมไม่ได้เปลี่ยนการวินิจฉัย เพราะ ASB มี pyuria ได้บ่อย\n\n- **Acute cystitis** ต้องมีอาการ (แสบขัด ปัสสาวะบ่อย ปวดท้องน้อย)\n- **Sterile pyuria** คือมี WBC แต่ **เพาะเชื้อไม่ขึ้น** ซึ่งตรงข้ามกับรายนี้\n- **Complicated UTI** ต้องเป็น UTI ที่มีอาการก่อน และรายนี้ไม่มีปัจจัยเสี่ยง\n- **ปนเปื้อน** มักเพาะได้หลายชนิด และไม่ได้เชื้อเดิมซ้ำสองครั้ง",
         "ASB = เชื้อ ≥ 10⁵ (หญิง 2 ครั้ง) ไม่มีอาการ · pyuria ไม่ใช่เหตุให้รักษา", "Definition of UTI vs ASB", R("Definition of UTI · Asymptomatic bacteriuria"), ["B9.2.2(1)", "2.3.14(7)", "B9.3(2)"]),
     mcq(N(2), "According to the classification used in the lecture, which of the following patients has a complicated urinary tract infection?",
         ["A 22-year-old non-pregnant woman with 2 days of dysuria and frequency", "A 35-year-old woman with fever and flank pain who has a normal urinary tract",
          "A 40-year-old man with 1 day of dysuria and frequency without fever", "A 28-year-old woman with asymptomatic bacteriuria found on routine testing",
          "A 25-year-old woman with dysuria, vaginal discharge and itching"], 2,
         "สไลด์จัด **ชาย** เป็น complicated UTI เสมอ แม้ไม่มีไข้ เพราะชายมีท่อปัสสาวะยาวและมีกลไกป้องกันดี การติดเชื้อจึงบ่งว่ามีความผิดปกติแฝง (ต่อมลูกหมาก การอุดกั้น) และต่อมลูกหมากอาจติดเชื้อร่วมด้วย\n\n- หญิงไม่ตั้งครรภ์ แสบขัด ปัสสาวะบ่อย = **acute simple cystitis**\n- หญิงมีไข้ ปวดเอว ทางเดินปัสสาวะปกติ = **acute uncomplicated pyelonephritis** (อาการหนักกว่าแต่ยังไม่ complicated)\n- **ASB** ไม่ใช่ UTI ที่มีอาการ\n- แสบขัด + ตกขาว คัน = นึกถึง **vaginitis** ก่อน",
         "Complicated = ปัจจัยของผู้ป่วย (ชาย DM ภูมิต่ำ ตั้งครรภ์ ปลูกถ่ายไต เป็นซ้ำ) ไม่ใช่ความรุนแรง", "Complicated vs uncomplicated UTI", R("Complicated UTI"), ["B9.2.2(1)", "2.3.14(7)", "2.1.40"]),
    ], nl=NLN + ["B9.3(2)"], figs=F1)

# ───────────────────────────── 2
F2 = {
 "ascend": fig("เชื้อไต่ขึ้นทีละขั้น — แต่ละขั้นให้อาการต่างกัน",
  "ทางหลักคือ **ascending infection** (สไลด์): E. coli จากลำไส้ไปตั้งถิ่นฐานรอบรูเปิดท่อปัสสาวะ → ขึ้นท่อปัสสาวะที่สั้น (หญิงราว 4 ซม.) → เกาะเยื่อบุกระเพาะ = **cystitis** → ไต่ขึ้นท่อไตถึงกรวยไตและเนื้อไต = **pyelonephritis** → ทะลักเข้ากระแสเลือด = **urosepsis** · ทางกระแสเลือด (hematogenous) พบน้อย เช่น S. aureus จากกระแสเลือดไปเป็นฝีในเนื้อไต · อาการบอกได้ว่าเชื้อไปถึงขั้นไหน",
  svg(420, 500, "เส้นทางการติดเชื้อแบบไต่ขึ้นจากลำไส้ถึงไตและกระแสเลือด พร้อมอาการของแต่ละขั้น",
      t(14, 18, "ทางกระแสเลือด (S. aureus)", "xs mu"),
      ar(40, 26, 66, 46, "lmu da", "ah-mu"),
      ell(100, 86, 46, 62, "ac"), ell(134, 92, 14, 22, "wa"),
      t(88, 90, "ไต", "b tac mid"),
      path("M136 114 C150 180 152 240 138 292", "lac w3"),
      path("M168 290 C178 230 176 170 158 116", "lbad w2", "ah-bad"),
      ell(128, 332, 62, 44, "wa"), t(128, 328, "กระเพาะ\nปัสสาวะ", "sm mid"),
      line(128, 376, 128, 420, "lac w3"),
      ar(146, 422, 146, 384, "lbad w2", "ah-bad"),
      t(84, 400, "ท่อสั้น\n~4 ซม.", "xs mid i2"),
      ell(128, 434, 40, 12, "ms"),
      t(128, 466, "รอบรูเปิดท่อปัสสาวะ", "xs mid i2"),
      rect(14, 418, 44, 66, "sk", 14), t(36, 444, "ลำไส้\nใหญ่", "xs mid"),
      ar(58, 440, 86, 436, "lbad w2", "ah-bad"),
      ar(130, 30, 232, 30, "lbad w2", "ah-bad"),
      box(234, 8, 180, 46, "bad", "Urosepsis\nความดันต่ำ ชีพจรเร็ว", fs=12),
      line(146, 96, 234, 100, "lmu dt"),
      box(234, 66, 180, 84, "bad", "Pyelonephritis\nP fimbriae เกาะเนื้อไต\nไข้ หนาวสั่น ปวดเอว\nCVA tender · WBC cast", fs=11.5),
      line(166, 206, 234, 206, "lmu dt"),
      box(234, 174, 180, 66, "sk", "ไต่ขึ้นท่อไต\nendotoxin ลดการบีบตัว\nVUR · ตั้งครรภ์", fs=11.5),
      line(190, 332, 234, 332, "lmu dt"),
      box(234, 290, 180, 84, "ms", "Cystitis\nFimH เกาะ uroplakin\nแสบขัด บ่อย ปวดหน่วง\nท้องน้อย · เลือดปน", fs=11.5),
      line(168, 434, 234, 434, "lmu dt"),
      box(234, 406, 180, 56, "sk", "Colonization\nยังไม่มีอาการ", fs=12))),
 "upec": fig("E. coli เกาะเยื่อบุด้วย fimbriae คนละชนิด",
  "**กระเพาะ**: ปลาย **FimH** ของ type 1 fimbriae จับ **uroplakin ที่มี mannose** บน umbrella cell ① → เชื้อเข้าไปแบ่งตัวในเซลล์เป็น **intracellular bacterial community (IBC)** ② หลบยาและเม็ดเลือดขาว → เซลล์ผิวหลุดลอกพร้อมเชื้อ ③ (ทำให้มีเลือดปนและเผยเยื่อบุชั้นลึก) → เชื้อบางส่วนพักตัวในชั้นลึก ④ เป็นแหล่งของการเป็นซ้ำ · **ไต**: **P fimbriae (PapG)** จับ **globoside** บนเซลล์บุท่อไตและกรวยไต → LPS กระตุ้น TLR4 → IL-8 เรียก neutrophil เข้ามา (pyuria, WBC cast) และ IL-6 ทำให้มีไข้",
  svg(420, 440, "กลไกการเกาะของ E. coli ด้วย type 1 fimbriae ในกระเพาะ และ P fimbriae ในไต",
      t(10, 18, "กระเพาะปัสสาวะ — type 1 fimbriae (FimH)", "b tac"),
      t(10, 36, "ปัสสาวะ", "xs mu"),
      rect(10, 128, 98, 52, "sk", 4), rect(110, 128, 98, 52, "sk", 4), rect(310, 128, 100, 52, "sk", 4),
      rect(14, 124, 90, 5, "acf", 2), rect(114, 124, 90, 5, "acf", 2), rect(314, 124, 92, 5, "acf", 2),
      t(410, 120, "uroplakin", "xs end tac"),
      ell(56, 80, 24, 10, "badf"),
      line(42, 89, 36, 121, "ln"), line(56, 90, 56, 121, "ln"), line(70, 89, 76, 121, "ln"),
      circ(36, 121, 3, "acf"), circ(56, 121, 3, "acf"), circ(76, 121, 3, "acf"),
      t(26, 66, "①", "b"), t(82, 114, "FimH", "xs i2"),
      ell(144, 152, 9, 4, "badf"), ell(160, 146, 9, 4, "badf"), ell(158, 160, 9, 4, "badf"), ell(174, 154, 9, 4, "badf"), ell(146, 166, 9, 4, "badf"),
      t(140, 114, "② IBC", "sm b"),
      g(rect(238, 60, 54, 34, "sk", 4), ell(254, 76, 7, 3, "badf"), ell(272, 80, 7, 3, "badf"), tr="rotate(-14 265 77)"),
      ar(258, 176, 262, 100, "lbad", "ah-bad"),
      t(266, 170, "ชั้นลึกเปิด", "xs tms"),
      t(300, 64, "③ หลุดลอก", "sm b"), t(300, 80, "→ เลือดปน", "xs i2"),
      rect(10, 182, 400, 18, "ms", 3),
      circ(240, 191, 3, "badf"), circ(252, 191, 3, "badf"), circ(345, 191, 3, "badf"),
      t(268, 212, "④ พักตัวในชั้นลึก → เป็นซ้ำ", "xs i2"),
      line(10, 228, 410, 228, "lru da"),
      t(10, 250, "ไต — P fimbriae (PapG)", "b tbad"),
      rect(10, 330, 130, 50, "sk", 4), rect(142, 330, 130, 50, "sk", 4), rect(274, 330, 136, 50, "sk", 4),
      circ(40, 328, 4, "msf"), circ(70, 328, 4, "msf"), circ(100, 328, 4, "msf"), circ(172, 328, 4, "msf"), circ(202, 328, 4, "msf"),
      t(36, 420, "globoside", "xs tms"), line(40, 410, 40, 334, "lmu dt"),
      ell(80, 282, 24, 10, "badf"),
      line(66, 291, 70, 324, "ln"), line(94, 291, 100, 324, "ln"),
      t(10, 306, "P fimbriae", "xs i2"),
      ar(110, 282, 214, 282, "lms", "ah-ms"),
      t(222, 270, "LPS → TLR4 ของเซลล์", "xs i2"),
      t(222, 288, "IL-8 → เรียก neutrophil", "sm b"),
      t(222, 305, "IL-1 · IL-6 → ไข้", "xs i2"),
      t(150, 316, "ท่อไต (lumen)", "xs mu"), t(120, 398, "interstitium", "xs mu"),
      circ(352, 412, 7, "ms"), circ(372, 404, 7, "ms"), circ(392, 414, 7, "ms"),
      ar(372, 396, 372, 320, "lms w2", "ah-ms"),
      circ(392, 318, 6, "ms"), circ(354, 314, 6, "ms"),
      t(410, 436, "neutrophil เข้าท่อไต → pyuria · WBC cast", "xs i2 end"))),
}
sec("neph-uti-02", "กลไกการติดเชื้อ — เชื้อไต่ขึ้นมาได้อย่างไร",
    "กลไกป้องกันของทางเดินปัสสาวะ · ascending vs hematogenous · ทำไมหญิงเป็นบ่อย · เชื้อก่อโรค · virulence ของ E. coli", 9,
"""### ทางเดินปัสสาวะป้องกันตัวเองอย่างไร
สไลด์สรุปกลไกป้องกันไว้สามอย่าง — **การไหลของปัสสาวะ (urine flow), ภูมิคุ้มกันของเยื่อบุ (mucosal immunity) และคุณสมบัติต้านเชื้อของทางเดินปัสสาวะ** — ตารางนี้ขยายความจากตำรา ว่าแต่ละอย่างทำงานอย่างไรและเสียไปเมื่อไร
| กลไก | ทำงานอย่างไร | เสียไปเมื่อไร |
|---|---|---|
| **การชะล้าง (washout)** | ถ่ายปัสสาวะชะเชื้อออกเป็นระยะ เชื้อต้องแบ่งตัวให้ทันก่อนถูกชะ | อุดกั้น นิ่ว ต่อมลูกหมากโต · **ปัสสาวะค้าง (residual urine)** · ดื่มน้ำน้อย |
| **เยื่อบุ** | ชั้น glycosaminoglycan เคลือบผิว · umbrella cell หลุดลอกพร้อมเชื้อ · TLR4 เรียก neutrophil | เบาหวาน ภูมิคุ้มกันต่ำ · เยื่อบุถูกทำลายจากสายสวนหรือหัตถการ |
| **สารในปัสสาวะ** | **Tamm-Horsfall protein (uromodulin)** จับ type 1 fimbriae ให้เชื้อหลุดไปกับปัสสาวะ · ยูเรียสูง osmolality สุดขั้ว | **น้ำตาลในปัสสาวะ** (เบาหวาน ยา SGLT2 inhibitor) กลายเป็นอาหารเชื้อ |
| **ลิ้นกันไหลย้อน** | ท่อไตเข้าผนังกระเพาะแบบเฉียง ถูกบีบปิดขณะถ่าย | vesicoureteral reflux · ตั้งครรภ์ (progesterone คลายท่อไต) |
| **Lactobacilli ในช่องคลอด** | สร้างกรดแลคติก pH ต่ำ E. coli ตั้งถิ่นฐานที่ปากช่องคลอดไม่ได้ | วัยหมดประจำเดือน · spermicide · ยาปฏิชีวนะ |

### สองเส้นทางของเชื้อ (สไลด์)
1. **Ascending infection** — ทางหลัก เชื้อจาก urethra ไต่ขึ้นกระเพาะแล้วขึ้นไต
2. **Hematogenous spread** — พบน้อย มักเป็นส่วนหนึ่งของการติดเชื้อทั้งระบบ เช่น **S. aureus** จากกระแสเลือดไปเป็นฝีในเนื้อไต, Candida, **วัณโรค** (หัวข้อ 5)
> ถ้าเพาะปัสสาวะได้ **S. aureus** ในผู้ที่ไม่ได้คาสายสวน ให้คิดว่าเชื้อมาทางกระแสเลือด → เจาะ hemoculture และมองหา endocarditis หรือฝีที่อื่น

[[fig:ascend]]

### ทำไมผู้หญิงเป็นบ่อยกว่าผู้ชายมาก
- **ท่อปัสสาวะสั้น** (ราว 4 ซม.) และรูเปิดอยู่ใกล้ช่องคลอดและทวารหนัก — แหล่งของ E. coli อยู่ห่างกระเพาะแค่ไม่กี่เซนติเมตร
- **เพศสัมพันธ์** ดันเชื้อจากปากช่องคลอดเข้าท่อปัสสาวะ · **diaphragm กับ spermicide** ฆ่า lactobacilli (สไลด์ recurrent UTI)
- ผู้ชาย: ท่อยาวราว 20 ซม. ผิวรอบรูเปิดแห้ง **น้ำจากต่อมลูกหมากมีสารต้านเชื้อ** → ชายที่เป็น UTI จึงมักมีความผิดปกติแฝง (หัวข้อ 9)

### เชื้อก่อโรค
| เชื้อ | พบในใคร | จุดเด่นที่ใช้ในข้อสอบ |
|---|---|---|
| **E. coli (uropathogenic E. coli, UPEC)** | ทุกกลุ่ม **75–90%** ของ UTI ในชุมชน | Gram-negative bacilli · nitrite บวก · ESBL พบบ่อยขึ้น |
| **Staphylococcus saprophyticus** | หญิงวัยเจริญพันธุ์ที่มีเพศสัมพันธ์ | Gram-positive cocci in clusters · **nitrite ลบ** |
| **Klebsiella pneumoniae** | เบาหวาน ผู้ป่วยใน สายสวน | แคปซูลเมือก · ESBL · emphysematous pyelonephritis |
| **Proteus mirabilis** | นิ่ว สายสวนนาน | **urease** → ปัสสาวะด่าง → นิ่ว struvite |
| **Enterococcus** | สายสวน หัตถการ ผู้สูงอายุ | Gram-positive cocci in chains · nitrite ลบ · **ดื้อ cephalosporin โดยธรรมชาติ** |
| Pseudomonas aeruginosa | โรงพยาบาล หัตถการ | ดื้อยาหลายขนาน |
| Candida | สายสวน ยาปฏิชีวนะกว้าง เบาหวาน | ส่วนใหญ่เป็น colonization (หัวข้อ 11) |

### E. coli ก่อโรคได้อย่างไร (รูป pathogenesis ในสไลด์เป็นภาพ — เรียบเรียงจากตำรา)
[[fig:upec]]
| Virulence factor | ทำอะไร | ผลทางคลินิก |
|---|---|---|
| **Type 1 fimbriae (FimH)** | จับ **uroplakin** ที่มี mannose บนเยื่อบุกระเพาะ → ไม่ถูกชะออก → แทรกเข้าเซลล์เป็น IBC | cystitis · เป็นซ้ำด้วยเชื้อเดิม |
| **P fimbriae (PapG)** | จับ **globoside (Gal-α1,4-Gal)** บนเซลล์บุท่อไตและกรวยไต | สายพันธุ์ที่มี P fimbriae พบมากใน **pyelonephritis และ urosepsis** |
| **LPS (endotoxin)** | ลดการบีบตัวของท่อไต · กระตุ้น TLR4 → cytokine | เชื้อไต่ขึ้นง่าย · ไข้ · septic shock |
| Capsule, hemolysin, siderophore | ต้าน complement · ทำลายเซลล์ · แย่งธาตุเหล็ก | ลุกลามเข้าเนื้อเยื่อและกระแสเลือด |
""",
    ["กลไกป้องกันหลักคือการชะล้างด้วยปัสสาวะ — อะไรที่ทำให้ปัสสาวะค้างจึงเพิ่ม UTI",
     "Ascending เป็นทางหลัก · S. aureus ในปัสสาวะโดยไม่มีสายสวน = คิดถึงทางกระแสเลือด",
     "E. coli 75–90% · S. saprophyticus ในหญิงสาว · Proteus = urease · Enterococcus = ดื้อ cephalosporin",
     "FimH จับ uroplakin (กระเพาะ) · P fimbriae จับ globoside (ไต)"],
    [mcq(N(3), "Uropathogenic Escherichia coli adhere to the bladder urothelium mainly through which interaction?",
         ["P fimbriae (PapG) binding globoside on renal tubular cells", "Type 1 fimbriae (FimH) binding mannosylated uroplakin on umbrella cells",
          "Urease binding urea in the bladder lumen", "Capsular K antigen binding Tamm-Horsfall protein", "Flagella binding collagen in the bladder wall"], 1,
         "เยื่อบุกระเพาะชั้นผิว (umbrella cell) ปกคลุมด้วยแผ่น **uroplakin** ที่มีน้ำตาล mannose — ปลาย **FimH** ของ **type 1 fimbriae** จับ mannose นี้ ทำให้เชื้อไม่ถูกชะออกไปกับปัสสาวะ แล้วแทรกเข้าเซลล์เป็น intracellular bacterial community\n\n- **P fimbriae** จับ globoside บนเซลล์ **ไต** — เป็นเหตุให้สายพันธุ์นี้ก่อ pyelonephritis\n- **Urease** เป็นเอนไซม์ของ Proteus ใช้สลายยูเรีย ไม่ใช่ตัวเกาะ\n- **Tamm-Horsfall protein** เป็นกลไกป้องกัน — จับ type 1 fimbriae ให้เชื้อหลุดไปกับปัสสาวะ\n- flagella ช่วยเคลื่อนที่ขึ้นท่อไต ไม่ใช่ตัวเกาะหลักที่กระเพาะ",
         "FimH–uroplakin = กระเพาะ · PapG–globoside = ไต", "UPEC adhesion", ["ตำรา (Brenner & Rector 11th ed.) — รูป pathogenesis ในสไลด์เป็นภาพ"], ["B9.2.2(1)", "B1.5.2(4)"]),
     mcq(N(4), "A 64-year-old man without a urinary catheter or recent urologic procedure is admitted with fever. Urine culture grows Staphylococcus aureus at 100,000 CFU/mL. Which of the following is the most appropriate next step?",
         ["Treat as uncomplicated cystitis with nitrofurantoin for 5 days", "Repeat the urine culture because Staphylococcus aureus is always a contaminant",
          "Obtain blood cultures and look for a source of bacteraemia such as endocarditis or abscess", "No treatment because this is asymptomatic bacteriuria",
          "Start oral fosfomycin as a single dose"], 2,
         "S. aureus ไม่ใช่เชื้อที่ไต่ขึ้นจากลำไส้ตามปกติ — การพบในปัสสาวะของผู้ที่ **ไม่ได้คาสายสวนหรือทำหัตถการ** บ่งว่าเชื้อมา **ทางกระแสเลือด (hematogenous spread)** ไปฝังที่ไต (สไลด์: hematogenous spread มักเป็นส่วนหนึ่งของการติดเชื้อทั้งระบบ) → ต้อง **เจาะ hemoculture และหาแหล่ง** เช่น endocarditis ฝีในไต กระดูกสันหลังอักเสบ\n\n- รักษาเป็น cystitis หรือให้ยาครั้งเดียว จะพลาด bacteremia ที่อันตรายถึงชีวิต\n- S. aureus ในปัสสาวะ **ไม่ควรสรุปว่าปนเปื้อน** โดยไม่หาแหล่ง\n- ผู้ป่วยมีไข้ จึงไม่ใช่ asymptomatic bacteriuria",
         "S. aureus ในปัสสาวะ (ไม่มีสายสวน) → hemoculture + หาแหล่งในกระแสเลือด", "Hematogenous UTI", R("Pathogenesis — hematogenous spread"), ["B9.2.2(2)", "2.3.14(14)", "2.2.48"]),
    ], nl=NLN + ["B9.1.1(2)", "B1.5.2(4)"], figs=F2,
    source=SRC + " · กลไก UPEC เติมจากตำรา (รูป pathogenesis ในสไลด์เป็นภาพ)")

# ───────────────────────────── 3
def _row(y, mech, sym, sc):
    return (box(100, y, 176, 44, "sk", mech, fs=11.5) + ar(276, y + 22, 296, y + 22, "ln", "ah")
            + box(298, y, 112, 44, sc, sym, fs=11.5))
F3 = {
 "symmap": fig("อาการแต่ละอย่างเกิดจากกลไกอะไร",
  "**บน (ไต)**: เนื้อไตอักเสบบวมใน **แคปซูลที่ยืดไม่ได้** → แคปซูลถูกยืด → ประสาทอัตโนมัติที่เข้าไขสันหลังระดับ **T10–L1** → ปวดเอวและเคาะ CVA เจ็บ · เชื้อในเนื้อไตที่มีเลือดมากปล่อย **LPS → IL-1, IL-6, TNF-α** → ไข้สูงหนาวสั่น · **ล่าง (กระเพาะ)**: การอักเสบอยู่ที่ผิวเยื่อบุ → แสบขัด ปัสสาวะบ่อย ปวดหน่วงท้องน้อย เลือดปน แต่ **ไม่มีไข้สูง** เพราะ cytokine เข้ากระแสเลือดน้อย",
  svg(420, 494, "กลไกของอาการ upper UTI และ lower UTI",
      rect(10, 8, 400, 24, "bad", 6), t(20, 25, "UPPER UTI — pyelonephritis", "sm b tbad"),
      ell(50, 120, 36, 54, "lbad da"), ell(50, 120, 27, 44, "ac"),
      ar(77, 120, 85, 120, "lbad", "ah-bad"), ar(23, 120, 15, 120, "lbad", "ah-bad"),
      ar(50, 164, 50, 172, "lbad", "ah-bad"), ar(50, 76, 50, 68, "lbad", "ah-bad"),
      t(50, 124, "ไต", "b mid tac"), t(50, 194, "แคปซูลตึง", "xs mid tbad"),
      _row(42, "เนื้อไตบวม ดันแคปซูล\nประสาท T10–L1", "ปวดเอว\nเคาะ CVA เจ็บ", "bad"),
      _row(96, "LPS → IL-1, IL-6, TNF\n→ hypothalamus", "ไข้สูง\nหนาวสั่น", "bad"),
      _row(150, "cytokine + ประสาท\nช่องท้องที่ใช้ร่วมกับไต", "คลื่นไส้\nอาเจียน", "bad"),
      rect(10, 210, 400, 24, "ms", 6), t(20, 227, "LOWER UTI — cystitis", "sm b tms"),
      ell(50, 318, 34, 42, "wa"), ell(50, 318, 26, 33, "lms w3"),
      poly([(38, 340), (62, 340), (50, 356)], "ms", True),
      line(50, 360, 50, 404, "lac w3"),
      t(50, 314, "กระเพาะ", "xs mid"),
      t(50, 424, "ผนัง + trigone", "xs mid tms"), t(50, 438, "อักเสบ", "xs mid tms"),
      _row(244, "trigone/urethra อักเสบ\nปัสสาวะไหลผ่านเยื่อบุ", "แสบขัด", "ms"),
      _row(298, "stretch receptor ไวขึ้น\ndetrusor บีบเอง", "ปัสสาวะบ่อย\nกลั้นไม่อยู่", "ms"),
      _row(352, "ผนังกระเพาะอักเสบ\nS2–S4 · T11–L2", "ปวดหน่วง\nเหนือหัวหน่าว", "ms"),
      _row(406, "หลอดเลือดใต้เยื่อบุ\nเปราะ · เยื่อบุลอก", "ปัสสาวะ\nมีเลือดปน", "ms"),
      t(10, 482, "ไม่มีไข้สูงใน cystitis: อักเสบแค่ผิวเยื่อบุ cytokine เข้ากระแสเลือดน้อย", "xs mu"))),
 "urge": fig("ทำไม cystitis ปวดถ่ายบ่อย ทีละน้อย",
  "ปกติ stretch receptor ในผนังกระเพาะส่งสัญญาณปวดถ่ายเมื่อปัสสาวะใกล้เต็ม (เส้นเขียว) · เมื่อเยื่อบุอักเสบ prostaglandin และ cytokine ทำให้ **ประสาทรับความรู้สึกไวขึ้น (threshold ต่ำลง)** และ **detrusor บีบตัวเองเป็นพัก ๆ** → ความรู้สึกปวดถึงระดับ \"ต้องไปถ่าย\" ตั้งแต่ปัสสาวะยังน้อย (เส้นแดง) → **ถ่ายบ่อย ครั้งละน้อย กลั้นไม่อยู่** ต่างจาก polyuria (เบาหวาน เบาจืด) ที่ถ่ายบ่อยแต่ปริมาณมากทุกครั้ง",
  svg(420, 344, "กราฟความรู้สึกปวดถ่ายกับปริมาตรปัสสาวะ ปกติเทียบกับกระเพาะอักเสบ",
      ar(56, 250, 404, 250, "ln", "ah"), ar(56, 250, 56, 28, "ln", "ah"),
      t(64, 34, "ความรู้สึกปวดอยากถ่าย", "xs i2"), t(404, 270, "ปริมาตรปัสสาวะในกระเพาะ →", "xs end i2"),
      line(56, 110, 396, 110, "lmu da"), t(62, 102, "ต้องไปถ่าย", "xs mu"),
      path("M56 246 C200 240 280 200 340 110 L356 76", "lok w3"),
      path("M56 242 C90 200 118 150 140 110 L154 76", "lbad w3"),
      line(140, 110, 140, 250, "lbad dt"), line(340, 110, 340, 250, "lok dt"),
      circ(140, 110, 5, "badf"), circ(340, 110, 5, "okf"),
      t(150, 150, "อักเสบ: ปวดตั้งแต่", "xs b tbad"), t(150, 164, "ปัสสาวะยังน้อย", "xs tbad"),
      t(334, 228, "ปกติ: ปวดเมื่อ", "xs b tok end"), t(334, 242, "กระเพาะเกือบเต็ม", "xs tok end"),
      t(10, 296, "ปกติ", "xs i2"), circ(120, 292, 10, "wa"), circ(190, 292, 10, "wa"), circ(260, 292, 10, "wa"),
      t(404, 296, "ทีละมาก", "xs end mu"),
      t(10, 328, "cystitis", "xs b tbad"),
      *[circ(84 + 23 * k, 324, 4, "wa") for k in range(11)],
      t(404, 328, "ทีละน้อย บ่อย", "xs end mu"))),
}
sec("neph-uti-03", "ทำไมถึงมีอาการนี้ — อาการบอกว่าเชื้ออยู่ตรงไหน",
    "กลไกของแสบขัด ปัสสาวะบ่อย ปวดท้องน้อย เลือดปน ไข้ ปวดเอว CVA tenderness อาเจียน · ทำไมผู้สูงอายุ เบาหวาน คาสายสวน มาไม่เป็นแบบ · DDx ของสไลด์", 11,
"""อาการของ UTI ไม่ได้มีไว้ท่องจำเป็นรายการ — **แต่ละอาการบอกว่าการอักเสบอยู่ที่ชั้นไหนและลึกแค่ไหน** ถ้าเข้าใจกลไก จะแยก cystitis จาก pyelonephritis และแยก UTI จากโรคอื่นได้จากประวัติและตรวจร่างกายเกือบทั้งหมด
> หัวข้อนี้เรียบเรียงจากตำรา (Brenner & Rector, Comprehensive Clinical Nephrology) เพื่ออธิบายอาการที่สไลด์ใช้ในเคสนำ — สไลด์ไม่มีหน้ากลไกของอาการโดยตรง

[[fig:symmap]]

#### ทำไมถึงมีอาการนี้ — Lower UTI (cystitis)
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปัสสาวะแสบขัด (dysuria)** | เยื่อบุ **trigone และ urethra** อักเสบ บวม · prostaglandin และ bradykinin ทำให้ปลายประสาทรับความเจ็บไวขึ้น → ปัสสาวะที่ไหลผ่านเยื่อบุที่อักเสบกระตุ้นความแสบ | แสบ **ในท่อ** ตลอดหรือท้ายการถ่าย = cystitis/urethritis · แสบ **ที่ผิวนอก** เมื่อปัสสาวะโดนปากช่องคลอด + ตกขาว คัน = **vaginitis** |
| **ปัสสาวะบ่อย ปวดกลั้นไม่อยู่ (frequency, urgency)** | การอักเสบลด **threshold ของ stretch receptor** ในผนังกระเพาะ + **detrusor บีบตัวเองเป็นพัก ๆ (irritability)** → ปวดถ่ายตั้งแต่ปัสสาวะยังน้อย | บ่อยแต่ **ครั้งละน้อย** = cystitis · บ่อยและ **ครั้งละมาก** = polyuria (เบาหวาน เบาจืด) |
| **ปวดหน่วงเหนือหัวหน่าว (suprapubic pain)** | ผนังกระเพาะอักเสบ ส่งสัญญาณผ่านประสาทอัตโนมัติ (pelvic nerve S2–S4 · hypogastric T11–L2) → ปวดตื้อ ๆ ตรงกลางเหนือหัวหน่าว ระบุตำแหน่งไม่ชัด | กดเจ็บเหนือหัวหน่าวแต่ **ไม่ปวดเอว** = ยังจำกัดอยู่ในกระเพาะ |
| **ปัสสาวะเป็นเลือด (hemorrhagic cystitis)** | หลอดเลือดฝอยใต้เยื่อบุขยายและเปราะ · umbrella cell หลุดลอกพร้อมเชื้อ (หัวข้อ 2) → เลือดซึม | ไม่ได้บอกความรุนแรง · ถ้าเลือดปนโดย **ไม่มีอาการอักเสบ** ให้คิดถึงนิ่ว มะเร็ง · ยา cyclophosphamide ทำให้เลือดออกจาก acrolein |
| **ปัสสาวะขุ่น กลิ่นแรง** | WBC และแบคทีเรียจำนวนมาก · urease ของบางเชื้อสร้าง ammonia | ไม่จำเพาะ — ขุ่นจากผลึกฟอสเฟตก็ได้ **ไม่ใช่ข้อบ่งชี้ให้ยา** |
| **ไม่มีไข้สูง** | การอักเสบอยู่แค่ผิวเยื่อบุ cytokine เข้ากระแสเลือดน้อย | ไข้ > 38 °C หรือหนาวสั่น = **ลุกลามเกินกระเพาะ** (ไต ต่อมลูกหมาก) |

[[fig:urge]]

#### ทำไมถึงมีอาการนี้ — Upper UTI (pyelonephritis)
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้สูง หนาวสั่น (fever, rigors)** | เชื้อเข้าเนื้อไตซึ่งมีเลือดไหลผ่านมาก (ราว 20% ของ cardiac output) → **LPS** กระตุ้น macrophage หลั่ง **IL-1, IL-6, TNF-α** → PGE₂ ที่ hypothalamus ตั้ง set point สูงขึ้น → กล้ามเนื้อสั่นเพื่อผลิตความร้อน (rigors) | ไข้ + อาการปัสสาวะ = upper UTI (ในชายคิดถึง prostatitis ด้วย) · หนาวสั่นมาก = เชื้อเข้ากระแสเลือดบ่อย |
| **ปวดเอว (flank pain)** | เนื้อไตอักเสบ **บวมในแคปซูลที่ยืดไม่ได้** → แคปซูลถูกยืด → ประสาทอัตโนมัติวิ่งตาม sympathetic เข้าไขสันหลังระดับ **T10–L1** → ปวดตื้อ ๆ ที่เอวและสีข้าง อาจร้าวมาด้านหน้า | ปวดบิดเป็นพัก ๆ ร้าวลงขาหนีบ = **นิ่วในท่อไต** (ท่อไตบีบตัวต้านการอุดกั้น) · ปวดเอว + ไข้ + นิ่ว = **อุดกั้นติดเชื้อ** (หัวข้อ 8) |
| **เคาะเจ็บที่มุมซี่โครงกับกระดูกสันหลัง (CVA tenderness)** | แรงสั่นสะเทือนจากการเคาะส่งถึงไตที่บวมและแคปซูลที่ตึงอยู่แล้ว → กระตุ้นความเจ็บ | มีข้างเดียว = ไตข้างนั้น · **เป็นอาการแสดงที่แยก pyelonephritis ออกจาก cystitis** |
| **คลื่นไส้ อาเจียน** | cytokine กระตุ้น chemoreceptor trigger zone · ไตใช้ปมประสาทช่องท้อง (celiac/aorticorenal) ร่วมกับลำไส้ → reflex อาเจียนและลำไส้เคลื่อนไหวน้อยลง | **กินยาหรือน้ำไม่ได้ = ข้อบ่งชี้ให้นอนโรงพยาบาล** (สไลด์) |
| **อาการ cystitis นำมาก่อน** | เชื้อไต่ขึ้นจากกระเพาะ | ไม่มีอาการ lower tract ก็ **ไม่ได้ตัด** pyelonephritis |
| **WBC cast ในปัสสาวะ** | เม็ดเลือดขาวในท่อไตถูก Tamm-Horsfall protein ห่อเป็นแท่ง | ยืนยันว่าอักเสบในเนื้อไต (หัวข้อ 4) |
| **ความดันต่ำ ชีพจรเร็ว สับสน** | เชื้อและ endotoxin เข้ากระแสเลือด → หลอดเลือดขยาย รั่ว | = **urosepsis** ต้องมองหาการอุดกั้นทันที (เคส 2) |

#### ทำไมบางกลุ่มมาแบบไม่เป็นแบบ (atypical presentation)
| กลุ่ม | กลไกที่ทำให้อาการไม่ชัด | สิ่งที่มาแทน |
|---|---|---|
| **ผู้สูงอายุ** | การตอบสนองต่อ pyrogen ลดลง ไข้ต่ำกว่าคนหนุ่มสาว · สมองสำรองน้อย cytokine ทำให้สับสนง่าย · มีปัสสาวะบ่อยหรือกลั้นไม่อยู่เป็นพื้นเดิม | **สับสน (delirium)** ล้ม กินไม่ได้ ความดันต่ำ — แต่ **ASB พบบ่อยมากในวัยนี้** อย่าสรุปว่าสับสนเพราะ UTI ก่อนหาสาเหตุอื่น |
| **เบาหวาน** | **autonomic neuropathy** → กระเพาะรับความรู้สึกน้อย (ไม่ปวดถ่าย ไม่แสบ) และบีบไม่หมด → ปัสสาวะค้าง · neutrophil ทำงานบกพร่องเมื่อน้ำตาลสูง | มาด้วย **pyelonephritis ฝีในไต emphysematous** หรือ sepsis โดยไม่มีอาการ lower tract นำ |
| **คาสายสวน** | สายเปิดค้าง กระเพาะไม่ต้องบีบและไม่ต้องกลั้น — ไม่มี dysuria/frequency ให้บอก | ไข้ที่ไม่มีสาเหตุอื่น หนาวสั่น ปวดท้องน้อยหรือ CVA สับสน |
| **บาดเจ็บไขสันหลัง** | ไม่มีความรู้สึกจากกระเพาะ | เกร็งมากขึ้น autonomic dysreflexia ไข้ |
| **Neutropenia** | ไม่มี neutrophil — ไม่มี pyuria และการอักเสบน้อย | มีไข้อย่างเดียว · UA อาจไม่มี WBC (สไลด์: caution in neutropenic patients) |

#### อาการคล้าย cystitis แต่ไม่ใช่ — DDx ในสไลด์
| โรค | กลไกที่ต่าง | เบาะแส |
|---|---|---|
| **Vaginitis** | อักเสบที่ผิวช่องคลอดและปากช่องคลอด ไม่ใช่กระเพาะ | แสบที่ผิวนอก ตกขาว คัน กลิ่น · **ไม่มี** ปัสสาวะบ่อยหรือปวดกลั้น |
| **Urethritis** (chlamydia, gonorrhea) | อักเสบเฉพาะท่อปัสสาวะ | ค่อย ๆ เริ่ม คู่นอนใหม่ มีหนองจากท่อ · **pyuria แต่เพาะเชื้อธรรมดาไม่ขึ้น** |
| **Painful bladder syndrome** | ชั้นป้องกันของเยื่อบุเสีย + ประสาทไวเกิน **ไม่มีเชื้อ** | ปวดเมื่อกระเพาะเต็ม ดีขึ้นหลังถ่าย เป็นเรื้อรัง · **เพาะเชื้อลบซ้ำ ๆ** |
| **PID** | อักเสบที่มดลูกและปีกมดลูก | ปวดท้องน้อยสองข้าง ไข้ ตกขาว โยกปากมดลูกเจ็บ |
""",
    ["ไข้ + ปวดเอว + CVA tenderness = เชื้อถึงเนื้อไต · cystitis ไม่ควรมีไข้สูง",
     "ปวดเอวเกิดจากแคปซูลไตถูกยืด (T10–L1) · ปวดบิดร้าวลงขาหนีบ = นิ่วในท่อไต",
     "Frequency ของ cystitis = บ่อยทีละน้อย (threshold ต่ำลง) ต่างจาก polyuria",
     "แสบที่ผิวนอก + ตกขาว = vaginitis · pyuria แต่เพาะไม่ขึ้น + คู่นอนใหม่ = urethritis",
     "ผู้สูงอายุ เบาหวาน คาสายสวน neutropenia มาไม่เป็นแบบ — แต่ ASB ก็พบบ่อยในกลุ่มนี้"],
    [mcq(N(5), "A 29-year-old woman has 2 days of fever 39.1 C, chills, nausea and right flank pain. Percussion over the right costovertebral angle reproduces severe pain. Which mechanism best explains the flank pain and costovertebral angle tenderness?",
         ["Spasm of the ureteral smooth muscle against an obstructing stone", "Distension of the bladder wall stimulating pelvic splanchnic nerves",
          "Inflammatory oedema of the renal parenchyma stretching the renal capsule, with pain carried by afferents entering T10–L1", "Irritation of the parietal peritoneum over the kidney",
          "Inflammation of the psoas muscle adjacent to the kidney"], 2,
         "ใน pyelonephritis เนื้อไตอักเสบและบวม แต่ถูกห่อด้วย **แคปซูลไตที่ยืดไม่ได้** → แคปซูลถูกยืด → ความเจ็บวิ่งตามประสาทอัตโนมัติเข้าไขสันหลังระดับ **T10–L1** → ปวดตื้อ ๆ ที่เอว และการเคาะ CVA ส่งแรงสั่นสะเทือนถึงไตที่ตึงอยู่จึงเจ็บมาก\n\n- **ท่อไตบีบตัวต้านนิ่ว** ทำให้ปวดบิดเป็นพัก ๆ ร้าวลงขาหนีบ (renal colic) ไม่ใช่ปวดตื้อร่วมกับไข้แบบนี้\n- **กระเพาะโป่ง** ทำให้ปวดเหนือหัวหน่าว\n- ไตอยู่ **หลังเยื่อบุช่องท้อง** จึงไม่ได้ปวดจาก peritoneum เป็นกลไกหลัก\n- psoas abscess ปวดเมื่อเหยียดสะโพก (psoas sign) ไม่ใช่กลไกของ pyelonephritis",
         "ปวดเอวใน pyelo = แคปซูลไตถูกยืด (T10–L1)", "Mechanism of flank pain", ["ตำรา Brenner & Rector 11th ed. — กลไกอาการ (สไลด์ไม่มีหน้ากลไก)"], ["B9.2.2(2)", "2.3.14(14)", "B9.1.1(3)"]),
     mcq(N(6), "A 66-year-old woman with long-standing type 2 diabetes and peripheral neuropathy presents with fever and confusion. She denies dysuria or urgency. Her post-void residual volume is 350 mL and urine culture grows Klebsiella pneumoniae. Why did she lack lower urinary tract symptoms?",
         ["Hyperglycaemia blocks the action of bacterial endotoxin on the bladder", "Klebsiella pneumoniae never causes cystitis",
          "Glycosuria sterilises the bladder urine", "Diabetic autonomic neuropathy reduces bladder sensation and impairs emptying, so inflammation is not perceived and urine stagnates",
          "Fever suppresses the micturition reflex"], 3,
         "**Diabetic autonomic neuropathy** ทำให้ประสาทรับความรู้สึกจากผนังกระเพาะเสีย — ผู้ป่วยไม่รู้สึกปวดถ่ายหรือแสบ และกระเพาะ **บีบไม่หมด** (residual 350 mL) → ปัสสาวะค้างเป็นแหล่งเพาะเชื้อ → มาด้วยไข้และสับสน (atypical) แทน\n\n- น้ำตาลในปัสสาวะ **เลี้ยงเชื้อ** ไม่ได้ฆ่าเชื้อ\n- Klebsiella ก่อ cystitis ได้ และพบบ่อยในเบาหวาน\n- น้ำตาลสูงไม่ได้ยับยั้งฤทธิ์ endotoxin — ตรงข้าม neutrophil ทำงานแย่ลง\n- ไข้ไม่ได้ยับยั้ง micturition reflex",
         "เบาหวาน: กระเพาะชา + ปัสสาวะค้าง → UTI ที่ไม่มีอาการ lower tract", "Atypical UTI in diabetes", ["ตำรา — atypical presentation · สไลด์: Comorbidities DM = complicated UTI"], ["B9.2.2(2)", "2.3.4(1)", "B9.1.2(7)"]),
     mcq(N(7), "A 24-year-old sexually active woman complains of burning when urine touches the vulva, with a thick white vaginal discharge and itching. She has no urinary frequency or urgency and no suprapubic pain. Which diagnosis is most likely?",
         ["Acute uncomplicated cystitis", "Acute pyelonephritis", "Vaginitis", "Painful bladder syndrome", "Asymptomatic bacteriuria"], 2,
         "อาการแสบ **ที่ผิวนอก (external dysuria)** เมื่อปัสสาวะโดนปากช่องคลอดที่อักเสบ ร่วมกับ **ตกขาว คัน** และ **ไม่มีปัสสาวะบ่อยหรือปวดกลั้น** = **vaginitis** (ตกขาวข้นขาวคัน เข้าได้กับ candida) — สไลด์ระบุ vaginitis เป็น DDx แรกของ acute simple cystitis\n\n- **Cystitis** แสบในท่อ มี frequency/urgency และปวดหน่วงท้องน้อย เพราะการอักเสบอยู่ที่ trigone และผนังกระเพาะ\n- **Pyelonephritis** ต้องมีไข้ ปวดเอว\n- **Painful bladder syndrome** ปวดสัมพันธ์กับกระเพาะเต็ม ไม่มีตกขาว\n- **ASB** ไม่มีอาการ",
         "External dysuria + ตกขาว ไม่มี frequency = vaginitis", "DDx of dysuria", R("Acute simple cystitis — DDx"), ["2.1.40", "2.3.14(17)", "2.3.14(7)"]),
    ], nl=NLN + ["2.1.40", "2.1.41", "2.1.43", "2.1.1"], figs=F3,
    source=SRC + " · กลไกของอาการเรียบเรียงจากตำรา (Brenner & Rector 11th · Comprehensive Clinical Nephrology 6th)")

# ───────────────────────────── 4
F4 = {
 "nitrite": fig("Nitrite บวกได้ต้องผ่านครบทุกขั้น",
  "Nitrate (NO₃⁻) มาจาก **อาหาร** ถูกกรองลงปัสสาวะ แล้ว **เชื้อที่มี nitrate reductase** (E. coli, Klebsiella, Proteus — กลุ่ม Enterobacterales) เปลี่ยนเป็น nitrite (NO₂⁻) ซึ่งต้องใช้เวลา **ค้างในกระเพาะราว 4 ชั่วโมง** · ขาดขั้นไหนก็ลบลวงได้ (กล่องเทาด้านขวา) — **nitrite บวกจึงเชื่อถือได้ แต่ nitrite ลบไม่ตัด UTI** (สไลด์) · ปัสสาวะแรกตอนเช้าให้ผลดีที่สุด",
  svg(420, 396, "ขั้นตอนการเกิด nitrite ในปัสสาวะและสาเหตุของผลลบลวง",
      box(10, 10, 210, 44, "ok", "อาหาร (ผัก) มี nitrate\nNO₃⁻", fs=12),
      ar(115, 54, 115, 78, "ln", "ah"),
      box(10, 80, 210, 44, "wa", "ไตกรอง NO₃⁻\nลงสู่ปัสสาวะ", fs=12),
      ar(115, 124, 115, 148, "ln", "ah"),
      box(10, 150, 210, 64, "ac", "ในกระเพาะ: เชื้อที่มี\nnitrate reductase\nเปลี่ยน NO₃⁻ → NO₂⁻", fs=12),
      ar(115, 214, 115, 238, "ln", "ah"),
      box(10, 240, 210, 44, "ms", "ต้องค้างในกระเพาะ\n≥ 4 ชั่วโมง", fs=12),
      ar(115, 284, 115, 308, "ln", "ah"),
      box(10, 310, 210, 44, "bad", "แถบตรวจเป็นสีชมพู\n= nitrite บวก", fs=12),
      t(332, 30, "ทำไมลบลวง", "sm b mid tbad"),
      box(250, 48, 164, 50, "sk", "ไม่กินผัก · ดื่มน้ำมาก\nปัสสาวะเจือจาง", fs=11),
      line(250, 82, 222, 102, "lbad da"), t(236, 98, "✕", "b tbad mid"),
      box(250, 132, 164, 76, "sk", "เชื้อไม่สร้าง nitrite\nEnterococcus\nS. saprophyticus\nPseudomonas · Candida", fs=11),
      line(250, 176, 222, 182, "lbad da"), t(236, 175, "✕", "b tbad mid"),
      box(250, 234, 164, 52, "sk", "ปัสสาวะบ่อย ค้างไม่ถึง\n4 ชม. (อาการ cystitis เอง)", fs=11),
      line(250, 260, 222, 262, "lbad da"), t(236, 257, "✕", "b tbad mid"),
      box(250, 314, 164, 36, "sk", "วิตามินซีสูงรบกวนสี", fs=11),
      line(250, 332, 222, 332, "lbad da"), t(236, 328, "✕", "b tbad mid"),
      t(10, 384, "บวก = เชื่อถือได้ · ลบ ≠ ไม่มี UTI", "sm b i2"))),
 "casts": fig("WBC cast เกิดได้ในท่อไตเท่านั้น",
  "**ซ้าย**: ในเนื้อไตที่อักเสบ (pyelonephritis หรือ AIN) เม็ดเลือดขาวจาก interstitium เคลื่อนเข้า **ท่อไต** ซึ่งมี **Tamm-Horsfall protein (uromodulin)** ที่หลั่งจาก thick ascending limb ตกเป็นเจล → ห่อเม็ดเลือดขาวไว้เป็นแท่งตามรูปท่อ → หลุดออกมาเป็น **WBC cast** · **ขวา**: กระเพาะปัสสาวะไม่มีท่อให้หล่อและไม่มี Tamm-Horsfall protein → cystitis มี WBC มากแต่ **ลอยอิสระ ไม่มี cast** — WBC cast จึงยืนยันว่าการอักเสบอยู่ในไต",
  svg(420, 362, "การเกิด WBC cast ในท่อไตเทียบกับ WBC อิสระในกระเพาะปัสสาวะ",
      t(105, 18, "ไต — pyelonephritis / AIN", "sm b tbad mid"), t(318, 18, "กระเพาะ — cystitis", "sm b tms mid"),
      line(80, 40, 80, 190, "ln w2"), line(130, 40, 130, 190, "ln w2"),
      t(105, 58, "ท่อไต", "xs mid mu"),
      rect(84, 100, 42, 78, "ac", 6),
      t(74, 112, "Tamm-\nHorsfall", "xs end tac"),
      circ(98, 120, 5, "ms"), circ(113, 136, 5, "ms"), circ(97, 152, 5, "ms"), circ(114, 166, 5, "ms"),
      circ(158, 112, 5, "ms"), ar(152, 115, 134, 124, "lms", "ah-ms"),
      circ(54, 160, 5, "ms"), ar(60, 160, 78, 158, "lms", "ah-ms"),
      t(140, 80, "WBC จาก\ninterstitium", "xs i2"),
      ar(105, 192, 105, 226, "ln", "ah"),
      circ(105, 282, 50, "bx"),
      rect(68, 269, 74, 26, "ac", 12),
      circ(83, 282, 5, "ms"), circ(99, 278, 5, "ms"), circ(115, 285, 5, "ms"), circ(130, 279, 4.5, "ms"),
      t(105, 350, "WBC cast = อักเสบในเนื้อไต", "xs b mid tbad"),
      ell(318, 104, 82, 58, "wa"),
      circ(290, 96, 5, "ms"), circ(312, 120, 5, "ms"), circ(336, 90, 5, "ms"), circ(348, 122, 5, "ms"),
      circ(296, 134, 5, "ms"), circ(326, 106, 5, "ms"), circ(270, 116, 5, "ms"), circ(362, 104, 5, "ms"),
      t(318, 182, "ไม่มีท่อให้หล่อ", "xs mid i2"), t(318, 196, "ไม่มี Tamm-Horsfall", "xs mid i2"),
      ar(318, 204, 318, 226, "ln", "ah"),
      circ(318, 282, 50, "bx"),
      circ(296, 264, 5, "ms"), circ(330, 270, 5, "ms"), circ(306, 296, 5, "ms"), circ(342, 296, 5, "ms"), circ(318, 282, 5, "ms"), circ(288, 288, 5, "ms"),
      t(318, 350, "WBC อิสระ ไม่มี cast", "xs b mid tms"))),
}
sec("neph-uti-04", "Urinalysis — dipstick และกล้องจุลทรรศน์บอกอะไร",
    "ตัวอย่างดีต้องมี epithelial < 5/HPF · leukocyte esterase · nitrite ต้องมีเชื้อที่มีเอนไซม์และค้าง 4 ชม. · pyuria · WBC cast บอกว่าอยู่ที่ไต", 10,
"""### เก็บปัสสาวะให้ถูกก่อน
- **Clean-catch midstream** — ทำความสะอาด แหวกแคมหรือรูดหนังหุ้มปลาย **ทิ้งปัสสาวะช่วงแรก** (ชะเชื้อในท่อปัสสาวะส่วนปลายออก) แล้วเก็บช่วงกลาง
- ส่งตรวจเร็ว (ภายในราว 2 ชั่วโมง หรือแช่เย็น) — ปล่อยไว้ที่อุณหภูมิห้องเชื้อจะแบ่งตัวในหลอด นับได้มากเกินจริง
- **Epithelial cells < 5/HPF = ตัวอย่างดี** (สไลด์) — squamous epithelial cell มาจากผิวช่องคลอดและปลายท่อปัสสาวะ ถ้ามีมาก แปลว่าปนเปื้อน WBC และเชื้อที่เห็นอาจมาจากช่องคลอด → **เก็บใหม่** ก่อนแปลผล

### Dipstick
#### Leukocyte esterase (LE)
- **กลไก**: esterase ในแกรนูลของ neutrophil ย่อยสารบนแถบให้เปลี่ยนสี — ตรวจได้แม้เม็ดเลือดขาวแตกไปแล้ว
- ตรวจพบเมื่อ **WBC ≥ 10 cells/HPF** · **sensitivity 75–96% · specificity 94–98%** (สไลด์)
- LE บวก = มี **pyuria (การอักเสบ)** ไม่ได้แปลว่ามีเชื้อ

#### Nitrite
[[fig:nitrite]]
- **กลไก** (สไลด์): E. coli, Proteus mirabilis และ Klebsiella มีเอนไซม์ **nitrate reductase** เปลี่ยน **nitrate ที่มาจากอาหาร** ในปัสสาวะเป็น **nitrite**
- **Nitrite บวก = ดัชนีที่เชื่อถือได้ของ significant bacteriuria** · **Nitrite ลบไม่ได้ตัด bacteriuria** (สไลด์)

#### ทำไม nitrite ลบทั้งที่ติดเชื้อ
| สาเหตุ | กลไก |
|---|---|
| **เชื้อไม่มี nitrate reductase** | **Enterococcus, Staphylococcus saprophyticus**, Candida · Pseudomonas เปลี่ยน nitrite ต่อเป็นก๊าซไนโตรเจน |
| **ปัสสาวะค้างในกระเพาะไม่ถึงราว 4 ชั่วโมง** | ปฏิกิริยาต้องใช้เวลา — คนที่เป็น cystitis ปัสสาวะบ่อย (อาการของโรคเอง) จึงลบบ่อย · ปัสสาวะแรกตอนเช้าดีที่สุด |
| **สารตั้งต้นน้อย** | ไม่กินผัก ดื่มน้ำมาก ยาขับปัสสาวะ → nitrate เจือจาง |
| **สารรบกวน** | วิตามินซีขนาดสูงรบกวนปฏิกิริยาสี |
ผลบวกลวง: ตัวอย่างวางทิ้งไว้นาน (เชื้อปนเปื้อนสร้าง nitrite ในหลอด) · ยาที่ทำให้ปัสสาวะมีสี เช่น phenazopyridine

#### อ่าน LE กับ nitrite ร่วมกัน
| LE | Nitrite | แปลว่า |
|---|---|---|
| + | + | ในคนมีอาการ = UTI แทบแน่นอน |
| + | − | UTI จากเชื้อที่ไม่สร้าง nitrite หรือค้างไม่นาน · หรือ **sterile pyuria** (หัวข้อ 5) |
| − | + | มีเชื้อแต่ไม่มี pyuria — neutropenia · ปนเปื้อน · ASB ระยะแรก |
| − | − | โอกาส UTI ต่ำ แต่ถ้าอาการชัด **ยังต้องส่งเพาะเชื้อ** |

### Microscopy (สไลด์)
- **Pyuria = WBC ≥ 5 cells/HPF ในตัวอย่างที่ปั่น (≥ 10 cells/HPF ถ้าไม่ปั่น)**
- **ระวังในผู้ป่วย neutropenia!!** — ไม่มีเม็ดเลือดขาวมาให้เห็น แม้ติดเชื้อรุนแรง (อาจารย์เขียนกำกับว่า infection ยังเกิดได้)
- **WBC cast** — บอกตำแหน่ง (ด้านล่าง)
- **Hematuria** — พบใน hemorrhagic cystitis ได้ เม็ดเลือดแดงรูปร่างปกติ (มาจากเยื่อบุ ไม่ใช่ glomerulus)
- **เห็นแบคทีเรีย** — ใน Gram stain ปัสสาวะที่ไม่ปั่น เห็นเชื้อ 1 ตัวต่อ oil-immersion field เทียบได้ราว 10⁵ CFU/mL (ตำรา)

[[fig:casts]]

#### ทำไม WBC cast บอกว่าการอักเสบอยู่ที่ไต
- cast ทุกชนิดก่อตัวได้ **เฉพาะในท่อไต** — Tamm-Horsfall protein (uromodulin) ที่หลั่งจาก thick ascending limb ตกเป็นเจลในท่อที่ปัสสาวะไหลช้าและเข้มข้น แล้วห่อเซลล์ที่อยู่ในท่อขณะนั้น
- **WBC cast = มีเม็ดเลือดขาวอยู่ในท่อไต** → การอักเสบอยู่ใน tubulointerstitium: **acute pyelonephritis** (มีไข้ CVA tenderness เชื้อขึ้น) หรือ **acute interstitial nephritis** (ได้ยา ผื่น eosinophil เพาะไม่ขึ้น)
- cystitis มี WBC จำนวนมากแต่ **ไม่มี cast**
""",
    ["Epithelial cells < 5/HPF = ตัวอย่างดี · มากกว่านั้น = ปนเปื้อน เก็บใหม่",
     "LE ตรวจ WBC ≥ 10/HPF · sens 75–96% spec 94–98%",
     "Nitrite ต้องมีเชื้อที่มี nitrate reductase + ค้าง ~4 ชม. · ลบไม่ตัด UTI (Enterococcus, S. saprophyticus)",
     "Pyuria = WBC ≥ 5/HPF (ปั่น) · ระวัง neutropenia ไม่มี pyuria",
     "WBC cast = อักเสบในเนื้อไต (pyelonephritis หรือ AIN) · cystitis ไม่มี cast"],
    [mcq(N(8), "A 27-year-old woman with dysuria and frequency has been voiding every 30 to 45 minutes all day. Dipstick of a random urine sample shows leucocyte esterase 3+ and nitrite negative. Culture later grows Escherichia coli at 100,000 CFU/mL. Which is the most likely explanation for the negative nitrite?",
         ["Escherichia coli lacks nitrate reductase", "The urine did not remain in the bladder long enough for nitrate to be reduced to nitrite",
          "Leucocyte esterase inactivates nitrite on the dipstick", "The infection is in the kidney rather than the bladder", "Nitrite is only positive in Gram-positive infections"], 1,
         "E. coli **มี nitrate reductase** แต่การเปลี่ยน nitrate เป็น nitrite ต้องใช้เวลา — ปัสสาวะต้อง **ค้างในกระเพาะราว 4 ชั่วโมง** ผู้ป่วยรายนี้ปัสสาวะทุก 30–45 นาที (ซึ่งก็คืออาการของ cystitis เอง) จึงลบลวง → สไลด์: **negative test does not exclude bacteriuria**\n\n- E. coli เป็นตัวอย่างคลาสสิกของเชื้อที่สร้าง nitrite\n- LE ไม่ได้ทำลาย nitrite\n- ตำแหน่งการติดเชื้อไม่ได้กำหนดผล nitrite\n- เชื้อ Gram-positive (Enterococcus, S. saprophyticus) ส่วนใหญ่ **ไม่มี** nitrate reductase จึงให้ nitrite ลบ",
         "Nitrite ลบลวง: ปัสสาวะบ่อย ค้าง < 4 ชม. หรือเชื้อไม่มีเอนไซม์", "Nitrite test limitations", R("Urinalysis: Dipstick — nitrite"), ["B9.3(2)", "3.1.6", "B9.2.2(1)"]),
     mcq(N(9), "A 52-year-old man receiving chemotherapy for lymphoma has fever 38.8 C. Absolute neutrophil count is 200/µL. Urinalysis shows WBC 0-1/HPF and leucocyte esterase negative, but urine and blood cultures both grow Escherichia coli. Which statement best explains the urinalysis?",
         ["The cultures must be contaminated", "Leucocyte esterase is inactivated by chemotherapy drugs", "Without circulating neutrophils there are no cells to form pyuria, so a urinary source cannot be excluded by a normal urinalysis",
          "Escherichia coli does not provoke an inflammatory response", "Pyuria only occurs in upper urinary tract infection"], 2,
         "สไลด์เตือน **\"Caution in neutropenic patients!!\"** — pyuria คือ neutrophil ที่เคลื่อนเข้ามาในทางเดินปัสสาวะ ถ้าร่างกายแทบไม่มี neutrophil ก็ไม่มีเซลล์มาให้เห็น ทั้งที่ติดเชื้ออยู่ → **UA ปกติไม่ได้ตัด UTI ในผู้ป่วย neutropenia** ต้องส่งเพาะเชื้อเสมอ\n\n- เพาะได้เชื้อเดียวกันทั้งเลือดและปัสสาวะ ไม่ใช่ปนเปื้อน\n- ยาเคมีบำบัดไม่ได้ทำลายเอนไซม์บนแถบตรวจ — ไม่มี WBC จึงไม่มี esterase\n- E. coli กระตุ้นการอักเสบชัดเจนในคนปกติ\n- pyuria พบทั้ง cystitis และ pyelonephritis",
         "Neutropenia: ไม่มี pyuria ไม่ได้แปลว่าไม่มี UTI", "Pyuria in neutropenia", R("Urinalysis: Microscopy — caution in neutropenic patients"), ["B9.3(2)", "3.1.6", "2.1.1"]),
     mcq(N(10), "A 35-year-old woman with dysuria provides a urine sample. Microscopy shows squamous epithelial cells 20-30/HPF, WBC 10-15/HPF and mixed bacteria. Which of the following is the most appropriate next step?",
         ["Start intravenous ceftriaxone for pyelonephritis", "Diagnose sterile pyuria and send urine for acid-fast bacilli", "Repeat the urinalysis on a properly collected clean-catch midstream specimen",
          "Diagnose asymptomatic bacteriuria and give no further evaluation", "Order a renal ultrasound"], 2,
         "สไลด์: **epithelial cells < 5/HPF = good urine sample** — รายนี้มี squamous epithelial 20–30/HPF แสดงว่าปัสสาวะ **ปนเปื้อนจากผิวช่องคลอด** ทั้ง WBC และเชื้อหลายชนิดที่เห็นอาจมาจากช่องคลอด จึงแปลผลไม่ได้ → **เก็บใหม่แบบ clean-catch midstream** (ทิ้งช่วงแรก เก็บช่วงกลาง)\n\n- ยังไม่มีหลักฐานของ pyelonephritis (ไม่มีไข้หรือปวดเอว)\n- จะเรียก sterile pyuria ต้องได้ตัวอย่างที่ดีและเพาะไม่ขึ้นก่อน\n- ผู้ป่วยมีอาการ จึงไม่ใช่ ASB\n- ยังไม่มีข้อบ่งชี้ทำภาพทางรังสี",
         "Squamous epithelium มาก = ปนเปื้อน → เก็บใหม่", "Specimen quality", R("Urinalysis — epithelial cells < 5/HPF"), ["B9.3(1)", "B9.3(2)", "3.1.6"]),
    ], nl=NLN + ["B9.3(1)", "B9.3(2)", "3.1.6"], figs=F4,
    source=SRC + " · ตารางและภาพ urinalysis ในสไลด์เป็นภาพ — การแปลผลร่วมและสาเหตุลบลวงเติมจากตำรา")

# ───────────────────────────── 5
LX = lambda e: 160 + (e - 1) * 50   # ตำแหน่ง x ของ 10^e บนแกน log
def _bar(y, lab1, lab2, e0, cls, note, e_alt=None):
    out = t(10, y + 16, lab1, "sm b") + t(10, y + 31, lab2, "xs mu")
    if e_alt:
        out += rect(LX(e_alt), y + 12, LX(e0) - LX(e_alt), 16, "lmu da", 8)
    out += rect(LX(e0), y + 12, 410 - LX(e0), 16, cls, 8) + circ(LX(e0), y + 20, 5, cls + "f" if cls in ("ac", "ok", "bad", "ms") else "inkf")
    out += t(min(LX(e0) + 10, 300), y + 44, note, "xs i2")
    return out
F5 = {
 "cfu": fig("เกณฑ์จำนวนเชื้อขึ้นกับชนิดสิ่งส่งตรวจและอาการ",
  "แถบเริ่มที่จำนวนเชื้อ (CFU/mL) ที่ถือว่ามีนัยสำคัญ · **ยิ่งสิ่งส่งตรวจปนเปื้อนยาก หรือผู้ป่วยมีอาการชัด เกณฑ์ยิ่งต่ำ** — suprapubic aspiration ปกติต้องปลอดเชื้อ เชื้อขึ้นเท่าไรก็มีความหมาย · ปัสสาวะที่ถ่ายเองปนเชื้อจากช่องคลอดได้ จึงใช้ **≥ 10⁵** (สไลด์) · คนมีอาการ cystitis ปัสสาวะบ่อยจนเชื้อแบ่งตัวไม่ทัน จึงใช้ 10²–10³ (IDSA) · คาสายสวนมีอาการ สไลด์ใช้ **≥ 10²** (IDSA 2009 ใช้ ≥ 10³ — เส้นประ) · **เพาะขึ้น ≥ 3 ชนิด = ปนเปื้อน** ไม่ว่าจะนับได้เท่าไร",
  svg(420, 366, "แผนภูมิเกณฑ์ CFU ต่อมิลลิลิตรของสิ่งส่งตรวจแต่ละชนิด",
      t(285, 14, "CFU/mL (log)", "xs mid mu"),
      *[t(LX(e), 32, "10" + "¹²³⁴⁵⁶"[e - 1], "xs mid i2") for e in range(1, 7)],
      *[line(LX(e), 38, LX(e), 344, "lru dt") for e in range(1, 7)],
      _bar(42, "Suprapubic aspirate", "ปกติต้องปลอดเชื้อ", 1, "ok", "ขึ้นเท่าไรก็มีความหมาย"),
      _bar(94, "คาสายสวน มีอาการ", "CA-UTI", 2, "ac", "สไลด์ ≥ 10² · IDSA ≥ 10³"),
      line(LX(3), 104, LX(3), 132, "lbad w2 da"),
      _bar(146, "Clean-catch มีอาการ", "หญิง cystitis (IDSA)", 3, "ac", "10²–10³ ก็มีนัยสำคัญ", e_alt=2),
      _bar(198, "Clean-catch มาตรฐาน", "voided (สไลด์)", 5, "ms", "≥ 10⁵ uropathogen"),
      _bar(250, "ไม่มีอาการ (ASB)", "หรือคาสายไม่มีอาการ", 5, "ms", "หญิงต้อง 2 ครั้ง"),
      t(10, 318, "เพาะขึ้น ≥ 3 ชนิด", "sm b tbad"), t(10, 333, "(สไลด์)", "xs mu"),
      rect(LX(1), 310, 410 - LX(1), 22, "bad", 11), t(285, 326, "ปนเปื้อน — เก็บใหม่", "sm b mid tbad"))),
 "gutb": fig("Genitourinary TB ลุกลามลงมาทีละขั้น",
  "วัณโรคทางเดินปัสสาวะเกิดจาก **เชื้อในปอดที่แฝงอยู่กระจายทางกระแสเลือด** ไปฝังที่ cortex ของไต (สไลด์) แล้วค่อย ๆ ลามลงตามทางเดินปัสสาวะเป็นปีหรือหลายปี · ทุกขั้นเกิด **granuloma → เนื้อตาย → พังผืด** ซึ่งอธิบายภาพที่อาจารย์ให้ดู (calyx ผิดรูป ureter ตีบยาว ไตเล็กมีหินปูน) และอาการ (sterile pyuria เลือดปน ปัสสาวะบ่อยจากกระเพาะหดเล็ก) · ในชายลามต่อไปที่ต่อมลูกหมากและ epididymis ได้",
  svg(420, 428, "ขั้นตอนการลุกลามของวัณโรคทางเดินปัสสาวะและสิ่งที่ตรวจพบในแต่ละขั้น",
      t(105, 14, "เกิดอะไรขึ้น", "xs b mid mu"), t(322, 14, "ตรวจพบอะไร", "xs b mid mu"),
      *[box(10, y, 190, 46, c, a, fs=11.5) + line(200, y + 23, 228, y + 23, "lmu dt") + box(228, y, 186, 46, "sk", b, fs=11.5)
        + (ar(105, y + 46, 105, y + 58, "ln", "ah") if y < 360 else "")
        for y, c, a, b in [
          (22, "sk", "TB ในปอด (latent)", "อาจไม่มีประวัติ · CXR ปกติได้"),
          (80, "ms", "กระจายทางกระแสเลือด\nฝังที่ cortex ทั้งสองไต", "ไม่มีอาการนานหลายปี"),
          (138, "bad", "granuloma → caseous\nnecrosis ที่ papilla", "sterile pyuria · เลือดปน\nไข้ต่ำ ๆ กลางคืน"),
          (196, "bad", "แผลแตกเข้า calyx\nเชื้อหลุดลงปัสสาวะ", "calyx ผิดรูป (caliectasis)\nurine AFB/Xpert บวก"),
          (254, "ms", "พังผืดที่ ureter", "ureter ตีบยาว\n→ hydronephrosis"),
          (312, "ms", "พังผืดที่ผนังกระเพาะ", "กระเพาะหดเล็ก\n→ ปัสสาวะบ่อยมาก"),
          (370, "sk", "ไตทั้งก้อนกลายเป็น\nหินปูน", "ไตเล็ก ไม่ทำงาน\n(autonephrectomy)")]])),
}
sec("neph-uti-05", "Urine culture, Gram stain และ sterile pyuria — เคส 3",
    "เกณฑ์ CFU ตามชนิดสิ่งส่งตรวจ · ≥ 3 ชนิด = ปนเปื้อน · Gram stain บอกยา · sterile pyuria · วัณโรคทางเดินปัสสาวะ", 10,
"""### Urine culture — เกณฑ์ significant bacteriuria
สไลด์: เกณฑ์มาตรฐานของปัสสาวะที่ถ่ายเอง (voided) คือ **≥ 10⁵ CFU/mL ของเชื้อที่ก่อโรคได้ (uropathogen)** และอาจารย์เขียนกำกับว่า **เพาะขึ้น ≥ 3 ชนิด = สงสัยปนเปื้อน** · หน้าตารางเกณฑ์ตามชนิดสิ่งส่งตรวจในสไลด์เป็นภาพ → ตารางนี้ใช้เกณฑ์ IDSA ประกอบ

[[fig:cfu]]

| สิ่งส่งตรวจ / สถานการณ์ | เกณฑ์ | ที่มา |
|---|---|---|
| Voided clean-catch (มาตรฐาน) | **≥ 10⁵ CFU/mL** ของ uropathogen | สไลด์ (Brenner & Rector) |
| หญิงที่มีอาการ cystitis | **10²–10³ CFU/mL** ก็มีนัยสำคัญ | IDSA / ตำรา |
| ASB (ไม่มีอาการ) | ≥ 10⁵ CFU/mL · **หญิงต้องได้เชื้อเดิม 2 ครั้งติดกัน** · ชาย 1 ครั้ง | สไลด์ · IDSA 2019 |
| คาสายสวน **มีอาการ** (CA-UTI) | **≥ 10² CFU/mL** (สไลด์) · IDSA 2009 ใช้ ≥ 10³ | สไลด์ · IDSA 2009 |
| คาสายสวน ไม่มีอาการ | ≥ 10⁵ CFU/mL | สไลด์ |
| Suprapubic aspiration | เชื้อขึ้นเท่าไรก็มีนัยสำคัญ | ตำรา |
| **เพาะขึ้น ≥ 3 ชนิด** | **ปนเปื้อน → เก็บใหม่** | สไลด์ (ลายมืออาจารย์) |

#### ทำไมคนที่มีอาการใช้เกณฑ์ต่ำกว่า
เกณฑ์ 10⁵ ถูกออกแบบมาแยก **การปนเปื้อน** ในคนที่ไม่มีอาการ — แต่คนที่เป็น cystitis **ปัสสาวะบ่อย** ปัสสาวะค้างในกระเพาะสั้น เชื้อจึงแบ่งตัวไม่ทันถึง 10⁵ ก่อนถูกชะออก ประกอบกับ **อาการและ pyuria ยืนยันอยู่แล้วว่าเชื้อนั้นก่อโรคจริง** — ถ้ายึด 10⁵ อย่างเดียวจะพลาดผู้ป่วย cystitis จริงได้ราวหนึ่งในสาม

### Urine Gram stain — รู้เชื้อก่อนผลเพาะ (หน้าสไลด์เป็นภาพ — สรุปจากตำรา)
| เห็น | คิดถึง | ผลต่อการเลือกยา |
|---|---|---|
| **Gram-negative bacilli** | Enterobacterales (E. coli, Klebsiella, Proteus) · Pseudomonas | ceftriaxone หรือ aminoglycoside ครอบคลุม · ระวัง ESBL |
| **Gram-positive cocci in chains** | **Enterococcus** | **ดื้อ cephalosporin โดยธรรมชาติ** → ampicillin/amoxicillin |
| Gram-positive cocci in clusters | S. saprophyticus (หญิงสาว) · **S. aureus → หาแหล่งในกระแสเลือด** | |
| Yeast | Candida | มักเป็น colonization (หัวข้อ 11) |
| WBC มากแต่ไม่เห็นเชื้อ | sterile pyuria | ดูตารางถัดไป |

### Sterile pyuria — มี pyuria แต่เพาะเชื้อไม่ขึ้น (สไลด์)
| กลุ่ม | ตัวอย่าง | กลไก / เบาะแส |
|---|---|---|
| **ได้ยาปฏิชีวนะไม่ครบ** | ซื้อยากินเองก่อนมา | ยาฆ่าเชื้อในปัสสาวะแล้ว แต่การอักเสบยังเหลือ — อาจารย์เขียนว่า **"AIN ~ partial treat"** |
| **เชื้อที่เพาะธรรมดาไม่ขึ้น** | **TB**, anaerobe, mycoplasma, **chlamydia**, virus, fungus, schistosomiasis | ต้องใช้อาหารเลี้ยงเชื้อหรือวิธีตรวจเฉพาะ |
| **ไตอักเสบที่ไม่ใช่เชื้อ** | **interstitial nephritis**, cystitis จากสาเหตุอื่น, allergic | AIN: ได้ยา (NSAID, β-lactam, PPI) ไข้ ผื่น eosinophilia · มี WBC cast ได้ |
| **เยื่อบุถูกระคาย** | **นิ่ว** สิ่งแปลกปลอม (สายสวน stent) | ปวดบิด เลือดปน |
| **ปนเปื้อนจากช่องคลอด** | | squamous epithelial cell มาก |
| **มะเร็งทางเดินปัสสาวะ** | | ผู้สูงอายุ สูบบุหรี่ เลือดปนไม่เจ็บ |

### Genitourinary TB — คำตอบของเคส 3
ชาย 45 ปี ไข้กลางคืน น้ำหนักลด 1 เดือน · **UA WBC 30–50/HPF ได้ยาปฏิชีวนะแล้วไม่ดีขึ้น** = sterile pyuria ในประเทศที่วัณโรคชุก → **ต้องคิดถึง GU TB** (และ interstitial nephritis ตามที่อาจารย์เขียนไว้)
- เกิดจาก **hematogenous spread ของวัณโรคปอดที่แฝงอยู่** (สไลด์)
- **วินิจฉัยช้า** เพราะอาการถูกบังหรือเข้าใจผิดว่าเป็น UTI ธรรมดา (สไลด์)
- ภาพที่อาจารย์ให้ดู: **calyx ทื่อผิดรูป (caliectasis)** · **ureter ตีบยาวหลายตำแหน่ง** · หินปูนในไต · **ไตเล็กไม่ทำงานมีหินปูน** · ฝีต่อมลูกหมากในผู้ป่วย HIV · ต่อมหมวกไตโต (Addison)
- ตรวจ: **ปัสสาวะตอนเช้า 3 วัน ส่ง AFB + molecular test (Xpert MTB/RIF) + TB culture** · CXR · ตรวจ HIV

[[fig:gutb]]

#### ทำไมถึงมีอาการนี้ (GU TB)
| อาการ / สิ่งที่พบ | กลไก |
|---|---|
| **Sterile pyuria** | granuloma ปล่อยเม็ดเลือดขาวลงปัสสาวะ แต่ M. tuberculosis โตช้าและไม่ขึ้นในอาหารเลี้ยงเชื้อธรรมดา |
| เลือดปน | แผลเนื้อตายที่ papilla และเยื่อบุ |
| ปัสสาวะบ่อยมาก (ระยะหลัง) | ผนังกระเพาะเป็นพังผืด หดเล็ก ความจุลดลง (thimble bladder) |
| ไตข้างหนึ่งบวมน้ำ | ureter เป็นพังผืดตีบ → อุดกั้น |
| ไข้ต่ำ ๆ กลางคืน น้ำหนักลด | cytokine จาก granuloma (TNF-α) |
| ยาปฏิชีวนะทั่วไปไม่ได้ผล | เชื้อไม่ไวต่อยา UTI ทั่วไป · fluoroquinolone อาจทำให้ดีขึ้นชั่วคราวและบังการวินิจฉัย |
""",
    ["Voided ≥ 10⁵ CFU/mL (สไลด์) · หญิงมีอาการ 10²–10³ ก็พอ · CA-UTI ≥ 10² (สไลด์) หรือ ≥ 10³ (IDSA)",
     "เพาะขึ้น ≥ 3 ชนิด = ปนเปื้อน เก็บใหม่",
     "GPC in chains = Enterococcus ดื้อ cephalosporin โดยธรรมชาติ",
     "Sterile pyuria: ได้ยามาก่อน · TB · chlamydia · AIN · นิ่ว · มะเร็ง",
     "Sterile pyuria เรื้อรัง + ไข้กลางคืน น้ำหนักลด = GU TB → urine AFB/Xpert ตอนเช้า 3 วัน"],
    [mcq(N(11), "A 72-year-old man with a long-term urinary catheter has fever on day 3 of intravenous ceftriaxone for a catheter-associated urinary tract infection. The urine Gram stain shows Gram-positive cocci in chains. Which of the following is the most appropriate change in therapy?",
         ["Increase the ceftriaxone dose", "Switch to cefepime", "Add metronidazole", "Switch to ampicillin, because enterococci are intrinsically resistant to cephalosporins", "Add fluconazole"], 3,
         "Gram-positive cocci in chains ในปัสสาวะของผู้คาสายสวน = **Enterococcus** ซึ่ง **ดื้อ cephalosporin ทุกรุ่นโดยธรรมชาติ** (penicillin-binding protein จับ cephalosporin ได้น้อย) — ceftriaxone จึงไม่ได้ผล ต้องเปลี่ยนเป็น **ampicillin/amoxicillin** (ถ้าไว) หรือ vancomycin ถ้าดื้อ และเปลี่ยนสายสวนด้วย\n\n- เพิ่มขนาด ceftriaxone หรือเปลี่ยนเป็น cefepime ก็ยังเป็น cephalosporin\n- metronidazole ครอบคลุม anaerobe ไม่ใช่ Enterococcus\n- fluconazole ใช้กับ Candida (เห็นเป็น yeast ไม่ใช่ cocci)",
         "GPC in chains = Enterococcus → ampicillin (ดื้อ cephalosporin)", "Gram stain-guided therapy", ["ตำรา — หน้า Urine Gram stain ในสไลด์เป็นภาพ"], ["3.1.9", "B1.5.2(5)", "B9.2.2(1)"]),
     mcq(N(12), "A 45-year-old man has 1 month of night fevers, fatigue and weight loss. Urinalysis repeatedly shows WBC 30-50/HPF and RBC 10-20/HPF, but routine urine cultures show no growth, and two courses of antibiotics have not helped. CT urography shows blunted, irregular calyces and a long stricture of the right ureter with hydronephrosis. Which diagnosis is most likely?",
         ["Recurrent Escherichia coli cystitis", "Genitourinary tuberculosis", "Acute interstitial nephritis from antibiotics", "Xanthogranulomatous pyelonephritis", "Emphysematous pyelonephritis"], 1,
         "นี่คือ **เคส 3 ของอาจารย์**: ไข้กลางคืน น้ำหนักลด + **sterile pyuria ที่ยาปฏิชีวนะไม่ช่วย** + ภาพ **calyx ทื่อผิดรูปและ ureter ตีบยาว** = **genitourinary TB** (สไลด์: hematogenous spread ของวัณโรคปอดแฝง วินิจฉัยช้าเพราะถูกบังด้วย UTI) → ส่ง urine AFB, Xpert MTB/RIF และ TB culture จากปัสสาวะตอนเช้า 3 วัน\n\n- **E. coli cystitis** ต้องเพาะเชื้อขึ้น\n- **AIN** ทำให้เกิด sterile pyuria ได้ แต่ไม่ทำให้ ureter ตีบหรือ calyx ผิดรูป\n- **XPN** เพาะไม่ขึ้นได้ 25–40% แต่เป็นก้อนในไตข้างเดียวร่วมกับนิ่ว (bear's paw)\n- **Emphysematous** มีก๊าซใน CT และอาการรุนแรงเฉียบพลัน",
         "Sterile pyuria + calyx ผิดรูป + ureter ตีบ = GU TB", "Genitourinary tuberculosis", R("Genitourinary TB · Case 3"), ["2.3.1(20)", "B9.3(2)", "2.1.43"]),
     mcq(N(13), "A urine culture from a woman with dysuria reports three different organisms, each at 10,000 CFU/mL, including lactobacilli. Which interpretation is most appropriate?",
         ["Polymicrobial cystitis requiring broad-spectrum antibiotics", "Contamination of the specimen; a properly collected specimen should be repeated",
          "Emphysematous cystitis", "Asymptomatic bacteriuria", "Fungal urinary tract infection"], 1,
         "อาจารย์เขียนกำกับในสไลด์ว่า **เพาะขึ้น ≥ 3 ชนิด = สงสัยปนเปื้อน** — UTI ในชุมชนแทบทั้งหมดเกิดจากเชื้อชนิดเดียว เชื้อหลายชนิดรวมถึง **lactobacilli** (เชื้อประจำถิ่นของช่องคลอด) บ่งว่าตัวอย่างปนเชื้อจากช่องคลอดและผิวหนัง → เก็บใหม่แบบ clean-catch midstream หรือสวนเก็บถ้าเก็บเองไม่ได้\n\n- ไม่ควรให้ยากว้างตามผลที่ปนเปื้อน\n- emphysematous cystitis วินิจฉัยด้วยก๊าซในผนังกระเพาะจากภาพ\n- ผู้ป่วยมีอาการ จึงไม่ใช่ ASB\n- ไม่มี yeast ในผล",
         "≥ 3 ชนิด (โดยเฉพาะมี lactobacilli) = ปนเปื้อน → เก็บใหม่", "Culture interpretation", R("Significant bacteriuria"), ["3.3.9", "B9.3(1)", "B9.2.2(1)"]),
    ], nl=NLN + ["3.3.9", "3.1.9", "B9.3(1)", "2.3.1(20)"], figs=F5,
    source=SRC + " · หน้าตาราง culture และ Gram stain ในสไลด์เป็นภาพ — เกณฑ์ตามชนิดสิ่งส่งตรวจอิง IDSA (ระบุในตาราง)")

# ───────────────────────────── 6
def _organ_panel(x, kd, bd, bl, ttl, ok_k, ok_b):
    cx = x + 98
    out = t(cx, 18, ttl, "sm b mid")
    out += ell(cx - 30, 80, 34, 44, "ac") + t(cx - 68, 84, "ไต", "xs b end tac")
    out += line(cx + 40, 36, cx + 40, 180, "lbad w2") + t(cx + 48, 50, "เลือด", "xs tbad")
    out += path("M%d 124 C%d 160 %d 180 %d 200" % (cx - 22, cx - 18, cx - 10, cx - 6), "lac w2")
    out += ell(cx - 4, 226, 56, 34, "wa") + t(cx - 4, 252, "ปัสสาวะ", "xs mid i2")
    import random
    rnd = random.Random(len(ttl))
    for _ in range(kd): out += circ(cx - 30 + rnd.uniform(-20, 20), 80 + rnd.uniform(-28, 28), 3, "acf")
    for _ in range(bl): out += circ(cx + 40, rnd.uniform(60, 172), 3, "acf")
    for _ in range(bd): out += circ(cx - 4 + rnd.uniform(-40, 40), 220 + rnd.uniform(-16, 10), 3, "acf")
    out += t(cx - 30, 146, ok_k, "xs mid " + ("tok" if "✓" in ok_k else "tbad"))
    out += t(cx - 4, 278, ok_b, "xs mid tok")
    return out
F6 = {
 "drugsite": fig("ยาไปอยู่ที่ไหน — ทำไม nitrofurantoin รักษา pyelonephritis ไม่ได้",
  "จุดสีคือความเข้มข้นของยา · **Nitrofurantoin และ fosfomycin** ถูกขับออกทางไตเร็วมาก ระดับในเลือดและเนื้อไตต่ำ แต่ในปัสสาวะสูงมาก → ฆ่าเชื้อที่ผิวเยื่อบุกระเพาะได้ดี (cystitis) แต่ **ไม่ถึงเชื้อในเนื้อไตหรือกระแสเลือด** · **Ceftriaxone, fluoroquinolone, aminoglycoside, TMP/SMX** มีระดับในเลือดและเนื้อไตดี จึงใช้กับ pyelonephritis ได้ — การเลือกยาจึงขึ้นกับ **ตำแหน่ง** ของการติดเชื้อ ไม่ใช่แค่ชนิดเชื้อ",
  svg(420, 318, "เปรียบเทียบความเข้มข้นของยาในเนื้อไต เลือด และปัสสาวะ",
      _organ_panel(6, 2, 30, 1, "Nitrofurantoin · Fosfomycin", "เนื้อไต ✕", "ปัสสาวะ ✓ → cystitis"),
      line(210, 10, 210, 300, "lru da"),
      _organ_panel(214, 22, 26, 14, "Ceftriaxone · FQ · AG", "เนื้อไต ✓", "ไต ✓ ปัสสาวะ ✓ → pyelo"),
      t(210, 308, "จุด = ความเข้มข้นของยา", "xs mid mu"))),
}
sec("neph-uti-06", "Acute simple cystitis — รักษาอย่างไร และทำไมใช้ยานี้",
    "ใครคือ simple cystitis · DDx · nitrofurantoin 5 วัน เป็นยาแรก · fosfomycin/aminoglycoside ครั้งเดียว · β-lactam 7 วัน · FQ/TMP-SMX 3 วันระวังดื้อ · ดีขึ้นใน 48 ชม.", 9,
"""### ใครคือ acute simple cystitis
**หญิงไม่ตั้งครรภ์ ทางเดินปัสสาวะปกติ** มีแสบขัด ปัสสาวะบ่อย ปวดกลั้น ปวดหน่วงท้องน้อย **ไม่มีไข้ ไม่ปวดเอว ไม่มีตกขาว**
- อาการครบแบบนี้ โอกาสเป็น UTI สูงพอให้ **เริ่มยาได้เลยโดยไม่ต้องรอผลเพาะเชื้อ**
- **ส่งเพาะเชื้อเมื่อ**: เป็นซ้ำ · ไม่ดีขึ้นใน 48 ชม. · สงสัย pyelonephritis · ตั้งครรภ์ · ชาย · เพิ่งได้ยาปฏิชีวนะ (เสี่ยงเชื้อดื้อ)
- **DDx ในสไลด์**: vaginitis · urethritis · painful bladder syndrome · PID (ตารางในหัวข้อ 3)

### ยา (สไลด์ อ.กรทิพย์ — Females)
| ลำดับ | ยา | ระยะเวลา | เหตุผลของการเลือก |
|---|---|---|---|
| **First-line** | **Nitrofurantoin** | **5 วัน** | เข้มข้นสูงในปัสสาวะ เชื้อดื้อน้อย กระทบเชื้อในลำไส้น้อย ไม่ใช้รักษาโรคอื่นจึงไม่เร่งเชื้อดื้อ |
| Alternative | **Fosfomycin** | **ครั้งเดียว** | ระดับในปัสสาวะสูงอยู่หลายวันหลังกินครั้งเดียว |
| Alternative | **Aminoglycoside** | **ครั้งเดียว** (ฉีด) | ขับทางไตในรูปเดิม เข้มข้นในปัสสาวะสูง ฆ่าเชื้อแบบขึ้นกับความเข้มข้น · ครอบคลุม ESBL บางส่วน |
| Alternative | **Amox/clav, cefixime** (β-lactam) | **7 วัน** | ได้ผลด้อยกว่าเล็กน้อยและกลับเป็นซ้ำมากกว่า จึงต้องให้นานกว่า |
| **ใช้ด้วยความระวัง — เชื้อดื้อสูง** | **Ciprofloxacin, levofloxacin** | **3 วัน** | ควรเก็บไว้ใช้กับการติดเชื้อที่รุนแรงกว่า · ผลข้างเคียงเอ็นอักเสบ QT ยาว C. difficile |
| **ใช้ด้วยความระวัง — เชื้อดื้อสูง** | **TMP/SMX** | **3 วัน** | อัตราดื้อของ E. coli ในไทยสูง |

[[fig:drugsite]]

#### ทำไม nitrofurantoin และ fosfomycin ห้ามใช้กับ pyelonephritis
ยาทั้งสองถูกดูดซึมแล้ว **ขับออกทางไตอย่างรวดเร็ว ระดับในเลือดและในเนื้อไตต่ำมาก** แต่ในปัสสาวะสูงมาก → ฆ่าเชื้อที่ผิวเยื่อบุกระเพาะได้ดี แต่ **ไปไม่ถึงเชื้อในเนื้อไตหรือกระแสเลือด** · นอกจากนี้ nitrofurantoin ต้องอาศัยการกรองของไต — ในไตเสื่อมมาก ระดับในปัสสาวะไม่พอ และยาสะสมเป็นพิษ (ปลายประสาทอักเสบ ปอดอักเสบ) จึงเลี่ยงเมื่อ CrCl < 30 mL/min (Beers criteria)

#### ทำไม β-lactam ต้องให้นานกว่า
β-lactam ฆ่าเชื้อแบบขึ้นกับเวลา และถูกขับออกจากปัสสาวะเร็ว · การศึกษาเปรียบเทียบพบว่าหายและไม่กลับเป็นซ้ำน้อยกว่ายาอื่น ส่วนหนึ่งเพราะกำจัด E. coli ที่อาศัยอยู่ในช่องคลอดและลำไส้ได้ไม่ดี → เชื้อกลับมาเกาะใหม่ได้

### ติดตาม
- **ควรดีขึ้นภายใน 48 ชั่วโมง** (สไลด์) → ถ้าไม่ดีขึ้น ส่งเพาะเชื้อ คิดถึงเชื้อดื้อยา การวินิจฉัยผิด หรือลุกลามเป็น pyelonephritis
- หายแล้ว **ไม่ต้องเพาะเชื้อซ้ำ** (ยกเว้นหญิงตั้งครรภ์)

### กลับไปที่เคส 1 — มีไข้ด้วย
หญิง 48 ปี แสบขัด ปัสสาวะบ่อย ปวดท้องน้อย **และมีไข้**
1. **ไข้ไม่เข้ากับ simple cystitis** → ต้องวัดไข้จริงและ **เคาะ CVA** ถ้ามีไข้ > 38 °C หรือเคาะเจ็บ = pyelonephritis ซึ่งใช้ยาคนละแบบ (**ห้าม nitrofurantoin**)
2. เป็น **2 ครั้งใน 6 เดือน** = เข้าเกณฑ์ **recurrent UTI** → **ต้องส่ง urine culture** (ซื้อยากินเองทำให้เชื้อดื้อ) แล้วหาปัจจัยเสี่ยงและป้องกัน (หัวข้อ 10)
3. อายุ 48 ปี อาจใกล้วัยหมดประจำเดือน → estrogen ลด lactobacilli ลด เป็นปัจจัยของการเป็นซ้ำ
""",
    ["Simple cystitis (หญิง): nitrofurantoin 5 วัน เป็นยาแรก (สไลด์)",
     "ทางเลือก: fosfomycin ครั้งเดียว · aminoglycoside ครั้งเดียว · amox/clav หรือ cefixime 7 วัน",
     "Cipro/levo 3 วัน และ TMP/SMX 3 วัน — ใช้ด้วยความระวังเพราะเชื้อดื้อสูง",
     "Nitrofurantoin และ fosfomycin ไม่ถึงเนื้อไต → ห้ามใช้ใน pyelonephritis",
     "Cystitis ควรดีขึ้นใน 48 ชม. — ไม่ดีขึ้นให้เพาะเชื้อ"],
    [mcq(N(14), "A 26-year-old non-pregnant woman has 2 days of dysuria, frequency and suprapubic pain. She has no fever, no flank pain and no vaginal discharge. She has no drug allergies and normal renal function. According to the lecture, which regimen is the first-line treatment?",
         ["Ciprofloxacin for 3 days", "Nitrofurantoin for 5 days", "Intravenous ceftriaxone for 7 days", "Amoxicillin-clavulanate for 3 days", "Trimethoprim-sulfamethoxazole for 14 days"], 1,
         "สไลด์ acute simple cystitis (Females): **first-line = nitrofurantoin 5 วัน** — เข้มข้นสูงในปัสสาวะ เชื้อดื้อน้อย กระทบเชื้อในลำไส้น้อย\n\n- **Ciprofloxacin 3 วัน** และ **TMP/SMX 3 วัน** อยู่ในกลุ่ม \"use with caution, resistance concerns\" (และ TMP/SMX 14 วันนานเกินจำเป็น)\n- **Ceftriaxone IV** ใช้กับ pyelonephritis ไม่จำเป็นในหญิงที่ไม่มีไข้\n- **Amox/clav** เป็นทางเลือกแต่ต้องให้ **7 วัน** ไม่ใช่ 3 วัน",
         "Simple cystitis: nitrofurantoin 5 วัน", "First-line therapy of acute simple cystitis", R("1. Acute simple cystitis (Females)"), ["B9.2.2(1)", "2.3.14(7)", "B1.7.2"]),
     mcq(N(15), "A 31-year-old woman has fever 38.9 C, rigors and left costovertebral angle tenderness. A colleague suggests oral nitrofurantoin because her last cystitis responded well to it. Why is nitrofurantoin inappropriate?",
         ["Nitrofurantoin does not cover Escherichia coli", "Nitrofurantoin achieves therapeutic concentrations in urine but not in renal tissue or blood",
          "Nitrofurantoin is only available intravenously", "Nitrofurantoin causes immediate acute kidney injury in all patients with fever", "Nitrofurantoin must always be given as a single dose"], 1,
         "ผู้ป่วยมีไข้ หนาวสั่น เคาะ CVA เจ็บ = **acute pyelonephritis** — เชื้ออยู่ใน **เนื้อไต** และอาจอยู่ในกระแสเลือด · nitrofurantoin ถูกขับออกทางไตเร็วมาก **ระดับในเลือดและเนื้อไตต่ำ** แม้ในปัสสาวะจะสูง → ใช้ได้กับ cystitis เท่านั้น (fosfomycin ก็เช่นกัน)\n\n- nitrofurantoin ครอบคลุม E. coli ได้ดี ปัญหาคือตำแหน่ง ไม่ใช่ชนิดเชื้อ\n- เป็นยากิน ไม่ใช่ยาฉีด\n- ไม่ได้ทำให้ไตวายทันทีในทุกคน (แต่ควรเลี่ยงเมื่อไตเสื่อมมาก)\n- ให้เป็นคอร์ส 5 วัน ไม่ใช่ครั้งเดียว (ยาครั้งเดียวคือ fosfomycin)",
         "Nitrofurantoin/fosfomycin = ยาของกระเพาะ ไม่ถึงไต", "Drug choice by site of infection", R("Acute simple cystitis vs acute pyelonephritis — treatment"), ["B9.2.2(2)", "B1.7.1(1)", "B1.7.2"]),
    ], nl=NLN + ["B1.7.2", "2.1.40", "2.1.41"], figs=F6)

# ───────────────────────────── 7
F7 = {
 "pyelorx": fig("เลือกยา pyelonephritis ตามสไลด์",
  "เก็บ urine culture (และ hemoculture เมื่อไข้สูงหรือ sepsis) **ก่อนให้ยา** · ไม่มี SIRS/ช็อก → **ceftriaxone** · มี septicemia/septic shock → **meropenem หรือ imipenem** เพราะ E. coli สร้าง ESBL ได้บ่อย (อาจารย์เขียนกำกับว่า β-lactamase) และพลาดยาตัวแรกในคนช็อกมีราคาแพง · ทางเลือกทั้งสองกลุ่มคือ gentamicin หรือ amikacin · ดีขึ้นใน 48–72 ชม. → เปลี่ยนเป็นยากินตามผลเพาะเชื้อ รวม **7 วัน** (ถ้าใช้ **oral cephalosporin 10–14 วัน**) · ไม่ดีขึ้น → หาที่ซ่อนเชื้อ (หัวข้อ 8)",
  svg(420, 512, "แผนผังการเลือกยาปฏิชีวนะสำหรับ acute pyelonephritis",
      box(10, 10, 400, 40, "sk", "เก็บ urine culture ± hemoculture ก่อนให้ยา", fs=12),
      ar(210, 50, 210, 72, "ln", "ah"),
      box(110, 74, 200, 38, "bx", "SIRS / septic shock ?"),
      poly([(110, 93), (80, 93), (80, 126)], "lok", False, "ah-ok"), t(95, 86, "ไม่", "xs mid i2"),
      poly([(310, 93), (340, 93), (340, 126)], "lbad", False, "ah-bad"), t(325, 86, "ใช่", "xs mid i2"),
      box(10, 128, 190, 70, "ok", "Ceftriaxone\nalt: gentamicin · amikacin", fs=12),
      box(220, 128, 190, 70, "bad", "Meropenem / imipenem\nalt: gentamicin · amikacin\n(กลัว ESBL E. coli)", fs=12),
      poly([(105, 198), (105, 222), (210, 222)], "ln"), poly([(315, 198), (315, 222), (210, 222)], "ln"),
      ar(210, 222, 210, 244, "ln", "ah"),
      box(110, 246, 200, 38, "bx", "ดีขึ้นใน 48–72 ชม. ?"),
      poly([(110, 265), (80, 265), (80, 298)], "lok", False, "ah-ok"), t(95, 258, "ใช่", "xs mid i2"),
      poly([(310, 265), (340, 265), (340, 298)], "lbad", False, "ah-bad"), t(325, 258, "ไม่", "xs mid i2"),
      box(10, 300, 190, 84, "ok", "Step-down ยากิน\nตามผลเพาะเชื้อ\ncipro · levo · TMP/SMX\ncefixime · amox/clav", fs=11.5),
      box(220, 300, 190, 84, "bad", "Imaging (US/CT)\nหา obstruction · abscess\nemphysematous\n→ หัวข้อ 8", fs=11.5),
      ar(105, 384, 105, 406, "ln", "ah"),
      box(10, 408, 190, 52, "ac", "รวม 7 วัน\n(oral cephalosporin 10–14 วัน)", fs=11.5),
      box(220, 408, 190, 96, "sk", "นอนโรงพยาบาลถ้า\nไข้หรือปวดไม่ลด\nอ่อนเพลียมาก\nกินน้ำหรือยาไม่ได้\nสงสัยอุดกั้น · กังวลการกินยา", fs=11))),
}
sec("neph-uti-07", "Acute uncomplicated pyelonephritis — เคส 2",
    "อาการและการตรวจ · ข้อบ่งชี้ให้นอนโรงพยาบาล · ceftriaxone vs carbapenem ตาม SIRS/ช็อก · step-down ยากิน 7 วัน (oral cephalosporin 10–14 วัน) · ดีขึ้นใน 48–72 ชม.", 10,
"""### อาการและการตรวจ
ไข้ หนาวสั่น ปวดเอว **เคาะ CVA เจ็บ** ± อาการ cystitis · คลื่นไส้อาเจียน (กลไกในหัวข้อ 3)
- **Urine culture ทุกราย ก่อนให้ยา** · hemoculture เมื่อไข้สูงหรือ sepsis · CBC, Cr
- UA: pyuria · nitrite · **WBC cast** (ยืนยันว่าอยู่ในไต)
- **ไม่ต้องทำภาพทุกราย** — สไลด์ให้ทำเมื่อ อาการหนักมาก · ไม่ดีขึ้นทั้งที่ยาถูก · **สงสัยอุดกั้น** (ไตแย่ลงจาก baseline หรือปัสสาวะลดลงฉับพลัน) · กลับเป็นซ้ำภายในไม่กี่สัปดาห์

### เคส 2 ของอาจารย์
ชาย 55 ปี รับจ้างก่อสร้าง **ไข้สูง หนาวสั่น ปวดสีข้างขวา 6 ชั่วโมง** — อาจารย์เขียนกำกับว่า **"Septicemia · concern septic shock"**
- ชาย = **complicated** ตั้งแต่ต้น (หัวข้อ 8) → ต้องถามอาการต่อมลูกหมาก นิ่ว เบาหวาน
- ปวดสีข้างเฉียบพลัน 6 ชม. + ไข้สูง → ต้องแยก **นิ่วอุดท่อไตร่วมกับติดเชื้อ** ซึ่งเป็นภาวะฉุกเฉินทางยูโรวิทยา
- ประเมิน **qSOFA/SIRS ความดัน lactate** ทันที → ถ้ามี septic shock ใช้ carbapenem + ทำ US ไตเร็ว

### ใครต้องนอนโรงพยาบาล (สไลด์ — indications for hospitalization)
- **ไข้สูงหรือปวดมากไม่ลด**
- **อ่อนเพลียมาก (marked debility)**
- **กินน้ำหรือกินยาไม่ได้** — อาเจียนจาก cytokine และ reflex จากไต (หัวข้อ 3)
- **สงสัยทางเดินปัสสาวะอุดกั้น**
- **กังวลว่าผู้ป่วยจะกินยาไม่ต่อเนื่อง**
และแน่นอน — มี SIRS หรือ septic shock

### ยาเริ่มต้น (สไลด์ — Females)
[[fig:pyelorx]]
| สถานการณ์ | First-line | Alternative |
|---|---|---|
| **ไม่มี SIRS/septic shock** | **Ceftriaxone** | Gentamicin, amikacin |
| **Septicemia / septic shock** | **Meropenem / imipenem-cilastatin** | Gentamicin, amikacin |

#### ทำไมรายที่ช็อกต้องเริ่มด้วย carbapenem
อาจารย์เขียนกำกับว่า **"E. coli → β-lactamase"** — E. coli ในชุมชนไทยสร้าง **ESBL (extended-spectrum β-lactamase)** ได้บ่อย ซึ่งทำลาย ceftriaxone · ในคนที่ช็อก การได้ยาที่เชื้อดื้อเพิ่มอัตราตายชัดเจน → เริ่ม **carbapenem ที่ทน ESBL** ก่อน แล้ว **ลดระดับยา (de-escalate)** เมื่อรู้ผลความไว

#### ทำไม aminoglycoside เป็นทางเลือกที่ดีใน pyelonephritis
ขับทางไตในรูปเดิม **เข้มข้นสูงทั้งในเนื้อไตและปัสสาวะ** ครอบคลุม ESBL ได้บางส่วน · แต่ **เป็นพิษต่อไตและหู** — ให้วันละครั้ง ระยะสั้น ระวังในผู้สูงอายุ ไตเสื่อม หรือใช้ร่วมกับยาที่เป็นพิษต่อไต

### เปลี่ยนเป็นยากิน (สไลด์ — step-down)
เมื่อไข้ลง กินได้ และรู้ผลความไวของเชื้อ:
- **Ciprofloxacin, levofloxacin, TMP/SMX** หรือ **cefixime, amox/clav** (ตามผลเพาะเชื้อ)
- **รวมระยะเวลา 7 วัน** · **ถ้าใช้ oral cephalosporin ให้ 10–14 วัน** — β-lactam ชนิดกินดูดซึมได้น้อยกว่าและระดับในเนื้อไตต่ำกว่า จึงต้องให้นานกว่า

### ควรดีขึ้นเมื่อไร (สไลด์)
- acute simple cystitis: **ภายใน 48 ชั่วโมง** · acute uncomplicated pyelonephritis: **48–72 ชั่วโมง**
#### ทำไมไข้ไม่ลงทันทีแม้ยาถูก
เนื้อไตที่อักเสบยังบวม cytokine ยังค้าง และเชื้อที่ตายปล่อย endotoxin ออกมา → ไข้ลงค่อยเป็นค่อยไปใน 2–3 วัน · **อย่ารีบเปลี่ยนยาในวันที่ 1–2** ถ้าอาการโดยรวมดีขึ้น · แต่ถ้าครบ 72 ชม. ยังไม่ดีขึ้น = มีปัญหาเชิงโครงสร้าง (หัวข้อ 8)
""",
    ["Pyelo ไม่มี SIRS/ช็อก: ceftriaxone · มี septic shock: meropenem/imipenem (ESBL) · alt: gentamicin/amikacin",
     "Admit: ไข้/ปวดไม่ลด · อ่อนเพลียมาก · กินไม่ได้ · สงสัยอุดกั้น · กังวลการกินยา",
     "Step-down ตามผลเพาะเชื้อ รวม 7 วัน — oral cephalosporin 10–14 วัน",
     "Pyelonephritis ควรดีขึ้นใน 48–72 ชม. · cystitis ใน 48 ชม.",
     "ห้ามใช้ nitrofurantoin/fosfomycin ใน pyelonephritis"],
    [mcq(N(16), "A 47-year-old woman with acute pyelonephritis has BP 82/48 mmHg despite 30 mL/kg of crystalloid, HR 124/min and lactate 4.6 mmol/L. Urine and blood cultures have been taken. According to the lecture, which empirical antibiotic is most appropriate?",
         ["Oral ciprofloxacin", "Intravenous ceftriaxone", "Oral nitrofurantoin", "Intravenous meropenem", "Single-dose oral fosfomycin"], 3,
         "ผู้ป่วยมี **septic shock** (ความดันต่ำหลังให้สารน้ำ lactate สูง) — สไลด์ pyelonephritis **with septicemia/septic shock: first-line = meropenem หรือ imipenem/cilastatin** (alternative gentamicin/amikacin) เพราะ E. coli สร้าง **ESBL** ได้บ่อย และการได้ยาที่เชื้อดื้อในคนที่ช็อกเพิ่มอัตราตาย → เริ่มกว้างก่อนแล้วค่อยลดระดับตามผลเพาะเชื้อ\n\n- **Ceftriaxone** เป็นยาแรกของ pyelonephritis **ที่ไม่มี** SIRS/ช็อก\n- **ยากิน** ไม่เหมาะกับคนช็อก (การดูดซึมไม่แน่นอน)\n- **Nitrofurantoin และ fosfomycin** ไม่ถึงเนื้อไตและเลือด",
         "Pyelo + septic shock → carbapenem (ESBL)", "Empirical therapy of pyelonephritis with shock", R("2. Acute uncomplicated pyelonephritis — with septicemia/septic shock"), ["B9.2.2(2)", "2.3.14(14)", "2.2.7", "2.2.48"]),
     mcq(N(17), "A 33-year-old woman with acute uncomplicated pyelonephritis improved on intravenous ceftriaxone. On day 3 she is afebrile and eating. The Escherichia coli isolate is susceptible to cefixime but resistant to fluoroquinolones and trimethoprim-sulfamethoxazole. She is switched to oral cefixime. According to the lecture, what should the total duration of therapy be?",
         ["3 days", "5 days", "7 days", "10–14 days", "4–6 weeks"], 3,
         "สไลด์: step-down เป็นยากินตามผลความไว **total duration 7 วัน — แต่ถ้าใช้ oral cephalosporin ให้ 10–14 วัน** เพราะ β-lactam ชนิดกินดูดซึมน้อยกว่าและระดับในเนื้อไตต่ำกว่า fluoroquinolone หรือ TMP/SMX\n\n- 3 หรือ 5 วัน เป็นระยะของ cystitis\n- 7 วัน ใช้เมื่อ step-down ด้วย fluoroquinolone หรือ TMP/SMX\n- 4–6 สัปดาห์ เป็นระยะของ kidney cyst infection ใน ADPKD (หัวข้อ 12)",
         "Pyelo step-down: 7 วัน · oral cephalosporin 10–14 วัน", "Duration of pyelonephritis therapy", R("2. Acute uncomplicated pyelonephritis — step-down, total duration"), ["B9.2.2(2)", "2.3.14(14)", "B1.7.2"]),
    ], nl=NLN + ["2.1.1", "2.2.48", "B1.7.2"], figs=F7)

# ───────────────────────────── 8
F8 = {
 "obstruct": fig("ทำไมไตอุดกั้นที่ติดเชื้อกลายเป็น urosepsis เร็ว และยาอย่างเดียวไม่พอ",
  "นิ่วอุดท่อไต → ปัสสาวะติดเชื้อค้างในกรวยไตที่ขยาย กลายเป็น **หนองในถุงปิด (pyonephrosis)** ไม่มีการชะล้าง · แรงดันในกรวยไตสูงจนปัสสาวะ **ย้อนเข้าหลอดเลือดดำและน้ำเหลือง (pyelovenous/pyelolymphatic backflow)** → เชื้อและ endotoxin เข้ากระแสเลือดโดยตรง → septic shock · ไตข้างที่อุดกรองได้น้อย ยาจึงไม่ถูกขับเข้าปัสสาวะข้างนั้น และหนองไม่มีเลือดไปเลี้ยง → **ต้องระบาย (PCN หรือ DJ stent) ภายในไม่กี่ชั่วโมง** ร่วมกับยา",
  svg(420, 414, "กลไกที่ไตอุดกั้นและติดเชื้อนำไปสู่ urosepsis",
      t(14, 22, "ไตข้างที่อุดกั้น", "sm b"),
      ell(96, 124, 58, 82, "ac"), ell(116, 132, 32, 44, "ms"),
      t(116, 128, "หนอง", "sm b mid tms"), t(116, 143, "ในกรวยไต", "xs mid tms"),
      line(186, 60, 186, 190, "lbad w3"), t(182, 52, "หลอดเลือด", "xs end tbad"),
      ar(146, 112, 182, 98, "lbad", "ah-bad"), ar(146, 150, 182, 168, "lbad", "ah-bad"),
      t(168, 208, "ย้อนเข้าเลือด", "xs mid tbad"),
      path("M122 176 C128 200 134 220 138 238", "lwa w5"),
      ell(140, 250, 10, 8, "inkf"), t(156, 262, "นิ่ว", "xs b"),
      path("M142 260 C146 290 148 312 150 330", "lac w2"),
      ell(150, 362, 46, 30, "wa"), t(150, 366, "กระเพาะ", "xs mid"),
      t(84, 290, "ใต้นิ่ว: ปัสสาวะ", "xs mid mu"), t(84, 304, "อาจปกติ", "xs mid mu"),
      box(230, 10, 184, 44, "sk", "1 นิ่ว/ก้อนอุดท่อไต", fs=11.5),
      ar(322, 54, 322, 70, "ln", "ah"),
      box(230, 72, 184, 58, "ms", "2 ปัสสาวะติดเชื้อค้าง\n= หนองในถุงปิด\nไม่มีการชะล้าง", fs=11.5),
      ar(322, 130, 322, 146, "ln", "ah"),
      box(230, 148, 184, 58, "ms", "3 แรงดันในกรวยไตสูง\n→ ย้อนเข้าหลอดเลือด\nและน้ำเหลือง", fs=11.5),
      ar(322, 206, 322, 222, "ln", "ah"),
      box(230, 224, 184, 44, "bad", "4 เชื้อ + endotoxin เข้าเลือด\n→ septic shock", fs=11.5),
      box(230, 284, 184, 58, "sk", "ยาเข้าไม่ถึง: ไตข้างนั้น\nกรองน้อย · หนองไม่มี\nเลือดไปเลี้ยง", fs=11.5),
      box(230, 356, 184, 46, "ok", "แก้: ระบายด่วน\nPCN / DJ stent + ยา", fs=11.5))),
 "fever72": fig("กฎ 72 ชั่วโมง — ไข้ไม่ลงทั้งที่ยาถูก = หาที่ซ่อนเชื้อ",
  "ถ้าเชื้อไวต่อยาที่ให้แต่ไข้ยังไม่ลงใน 72 ชม. ปัญหามักไม่ใช่ \"ยาผิด\" แต่เป็น **ที่ซ่อนเชื้อที่ยาเข้าไม่ถึง** — สไลด์: no response within 72 hrs หรือสงสัย obstruction → **imaging** และพิจารณาให้ยานานขึ้น · US ดูไตบวมน้ำได้เร็ว ข้างเตียง · CT with contrast ดูฝี ก๊าซ และนิ่ว · การรักษาคือ **source control** (ระบาย) ไม่ใช่การเปลี่ยนยาไปเรื่อย ๆ",
  svg(420, 414, "แผนผังเมื่อไข้ไม่ลงใน 72 ชั่วโมงของการรักษา UTI",
      box(10, 10, 400, 40, "sk", "Pyelonephritis / complicated UTI ได้ยาที่เชื้อไว", fs=12),
      ar(210, 50, 210, 72, "ln", "ah"),
      box(110, 74, 200, 38, "bx", "ไข้ลงใน 72 ชม. ?"),
      poly([(110, 93), (80, 93), (80, 130)], "lok", False, "ah-ok"), t(95, 86, "ลง", "xs mid i2"),
      poly([(310, 93), (330, 93), (330, 130)], "lbad", False, "ah-bad"), t(320, 86, "ไม่ลง", "xs mid i2"),
      box(10, 132, 150, 50, "ok", "ทำต่อ: step-down\nให้ครบระยะ", fs=12),
      box(230, 132, 180, 50, "bad", "ไม่ใช่ยาผิด\nแต่มีที่ซ่อนเชื้อ", fs=12),
      ar(320, 182, 320, 204, "ln", "ah"),
      box(140, 206, 270, 56, "ms", "Imaging\nUS → ไตบวมน้ำ · CT → ฝี ก๊าซ นิ่ว", fs=12),
      *[ar(275, 262, x + 47, 298, "ln", "ah") for x in (10, 112, 214, 316)],
      box(10, 300, 94, 70, "bad", "อุดกั้น\n→ PCN /\nDJ stent", fs=11),
      box(112, 300, 94, 70, "bad", "ฝีในไต\n→ เจาะ\nระบาย", fs=11),
      box(214, 300, 94, 70, "bad", "ก๊าซในไต\n→ ระบาย\n± ตัดไต", fs=11),
      box(316, 300, 94, 70, "sk", "ไม่พบ\n→ เชื้อดื้อ?\nไข้ที่อื่น?", fs=11),
      t(10, 398, "Source control สำคัญกว่าการเปลี่ยนยา", "sm b tok"))),
}
sec("neph-uti-08", "Complicated UTI — ใคร ยาอะไร และเมื่อไรต้องทำภาพ",
    "ชาย DM ภูมิต่ำ ตั้งครรภ์ ปลูกถ่ายไต เป็นซ้ำ · ceftriaxone / aminoglycoside / pip-tazo-cefepime-ceftazidime เมื่อเสี่ยงเชื้อดื้อ · 10–14 วัน · กฎ 72 ชม. · อุดกั้น ฝี นิ่ว struvite", 12,
"""### ใครคือ complicated UTI (สไลด์)
| ปัจจัย | ทำไมทำให้ "ซับซ้อน" |
|---|---|
| **ชาย** | ท่อปัสสาวะยาวและมีสารต้านเชื้อจากต่อมลูกหมาก การติดเชื้อจึงบ่งความผิดปกติแฝง · ต่อมลูกหมากอาจติดเชื้อร่วม (หัวข้อ 9) |
| **เบาหวาน, ภูมิคุ้มกันต่ำ** | น้ำตาลเลี้ยงเชื้อ neutrophil บกพร่อง กระเพาะชาบีบไม่หมด · เสี่ยงฝี papillary necrosis และ emphysematous pyelonephritis (หัวข้อ 12) |
| **ตั้งครรภ์** | progesterone คลายท่อไต + มดลูกกดท่อไต → ปัสสาวะคั่ง · pyelonephritis ทำให้คลอดก่อนกำหนด · ยาที่ใช้ได้จำกัด |
| **ผู้รับการปลูกถ่ายไต** | ยากดภูมิ · ไตใหม่ไม่มีเส้นประสาท จึงไม่ปวดเตือน · รอยต่อท่อไตกับกระเพาะมีการไหลย้อน |
| **Recurrent uncomplicated UTI** | สงสัยปัจจัยแฝง และเชื้อดื้อยาจากการได้ยาซ้ำ ๆ |
| (ตำรา) อุดกั้น นิ่ว สายสวน หัตถการ ไตเสื่อม | ปัสสาวะค้าง หรือมีสิ่งแปลกปลอมให้เชื้อสร้าง biofilm |

### ยา (สไลด์)
| | ยา |
|---|---|
| **Empirical first-line** | **Ceftriaxone** |
| Alternative | Gentamicin, amikacin |
| **เสี่ยงเชื้อดื้อ/ติดเชื้อในโรงพยาบาล (nosocomial/MDR risk)** | **Piperacillin/tazobactam, ceftazidime, cefepime** — ครอบคลุม Pseudomonas |
| Definitive | **Step-down เป็นยากินตามผลความไว**: ciprofloxacin, levofloxacin, TMP/SMX, β-lactam |
| **ระยะเวลา** | **10–14 วัน** หรือนานกว่าในข้อบ่งชี้เฉพาะ |
ถ้ามี septic shock ใช้หลักเดียวกับหัวข้อ 7 — เริ่ม carbapenem ก่อนแล้วลดระดับ

### กฎ 72 ชั่วโมง (สไลด์)
**ไม่ตอบสนองภายใน 72 ชม. หรือสงสัยการอุดกั้น → imaging และพิจารณาให้ยานานขึ้น**
[[fig:fever72]]

#### ทำไมไข้ไม่ลงทั้งที่เชื้อไวต่อยา
| สาเหตุ | กลไก | ภาพที่เห็น | แก้อย่างไร |
|---|---|---|---|
| **อุดกั้น → pyonephrosis** | ปัสสาวะติดเชื้อค้างในกรวยไตที่ขยาย = หนองในถุงปิด · ไตข้างนั้นกรองน้อย ยาไม่ถูกขับลงปัสสาวะข้างนั้น | ไตบวมน้ำ (US) · นิ่ว (CT) | **ระบายด่วน**: percutaneous nephrostomy (PCN) หรือ DJ stent |
| **ฝีในไตหรือรอบไต** | หนองไม่มีหลอดเลือด pH ต่ำ เชื้อหนาแน่น ยาเข้าไม่ถึงและออกฤทธิ์ได้ไม่ดี | US ก้อน hypoechoic · CT ก้อน hypodense ขนาดใหญ่ | ฝีขนาดใหญ่ (เกินราว 3–5 ซม.) → เจาะระบาย + ยานานขึ้น |
| **Emphysematous pyelonephritis** | เนื้อตายและก๊าซ (หัวข้อ 12) | ก๊าซใน CT | ระบาย ± ตัดไต |
| **เชื้อดื้อ หรือไม่ใช่ UTI** | ESBL, Pseudomonas, Enterococcus · ไข้จากที่อื่น | — | ดูผลเพาะเชื้อ หาแหล่งอื่น |

[[fig:obstruct]]

#### ทำไมอุดกั้นแล้วกลายเป็น urosepsis เร็ว
- แรงดันในกรวยไตสูง → **ปัสสาวะย้อนเข้าหลอดเลือดดำและน้ำเหลือง** (และ fornix ของ calyx อาจฉีก) → เชื้อและ endotoxin ทะลักเข้ากระแสเลือดโดยตรง
- ไม่มีการชะล้าง เชื้อเพิ่มจำนวนในถุงปิด
- ปัสสาวะที่เก็บได้อาจ **ปกติ** เพราะไตข้างที่อุดไม่ส่งปัสสาวะลงมา — UA ปกติจึงไม่ตัด pyonephrosis
→ **pyelonephritis + ไตบวมน้ำ = ภาวะฉุกเฉินทางยูโรวิทยา** ต้อง source control ภายในไม่กี่ชั่วโมง ยาอย่างเดียวไม่พอ

### ภาพทางรังสีที่อาจารย์ให้ดู (สไลด์เป็นภาพ — สรุปจากคำอธิบายในสไลด์)
| ภาพ | สิ่งที่เห็น | แปลว่า |
|---|---|---|
| US ไต | **ก้อน hypoechoic** | pyelonephritis เฉพาะที่ หรือฝีระยะแรก |
| CT ฉีดสารทึบรังสี | **ริ้วสีจางรูปสามเหลี่ยม แผ่จากกรวยไตไปถึง cortex** | **acute pyelonephritis** |
| CT ฉีดสารทึบรังสี | **บริเวณสีจางขนาดใหญ่** | **renal abscess** |
| US หรือ CT | กรวยไตและ calyx ขยาย | hydronephrosis — หาจุดอุดกั้น |
| CT KUB | นิ่ว | อาจารย์เขียนว่า **"Radio = Ca"** — นิ่วแคลเซียมทึบรังสี เห็นใน KUB · **นิ่วกรดยูริกโปร่งรังสี** เห็นใน CT |
#### ทำไม pyelonephritis เห็นเป็นลิ่มสามเหลี่ยม
ไตแบ่งเป็น lobe รูปพีระมิด ฐานอยู่ที่ cortex ยอดอยู่ที่ papilla — เชื้อที่ขึ้นจากกรวยไตเข้าทาง papilla แล้วลามตามท่อไตในแนวรัศมี → การอักเสบ บวม และหลอดเลือดหดตัวเกิดเป็นแนวนั้น สารทึบรังสีเข้าน้อย → **ลิ่มสีจาง ปลายชี้กรวยไต ฐานอยู่ผิวไต** · ถ้าเนื้อตายรวมเป็นหนองจะกลายเป็นก้อนสีจางขนาดใหญ่ = ฝี

### นิ่ว struvite — เชื้อกับนิ่วเลี้ยงกันเอง
- เชื้อที่สร้าง **urease** (Proteus mirabilis, Klebsiella) สลายยูเรียเป็น **ammonia → ปัสสาวะเป็นด่าง (pH > 7)** → magnesium ammonium phosphate (struvite) ตกตะกอน → **นิ่ว staghorn** เต็มกรวยไต
- เชื้ออยู่ในเนื้อนิ่วและ biofilm ยาเข้าไม่ถึง → ติดเชื้อซ้ำ (สไลด์: stones = failure to eradicate) จนกว่า **เอานิ่วออกหมด** (มักใช้ PCNL) ร่วมกับยา
""",
    ["Complicated (สไลด์): ชาย · DM/ภูมิต่ำ · ตั้งครรภ์ · ปลูกถ่ายไต · recurrent",
     "Empirical ceftriaxone · alt aminoglycoside · MDR/nosocomial: pip/tazo, ceftazidime, cefepime · 10–14 วัน",
     "ไข้ไม่ลงใน 72 ชม. = หาที่ซ่อนเชื้อ (อุดกั้น ฝี ก๊าซ) → imaging",
     "Pyelo + hydronephrosis = urologic emergency → PCN/DJ stent + ยา",
     "CT: ลิ่มสามเหลี่ยมสีจาง = pyelonephritis · ก้อนสีจางใหญ่ = abscess"],
    [mcq(N(18), "A 58-year-old woman with diabetes has fever 39.5 C, right flank pain and BP 84/50 mmHg after fluid resuscitation. Intravenous meropenem has been started. Bedside ultrasound shows moderate right hydronephrosis, and CT shows an 8-mm stone in the right proximal ureter. Which is the most important next step?",
         ["Continue antibiotics alone and repeat imaging in 1 week", "Urgent decompression of the right kidney by percutaneous nephrostomy or ureteric stent",
          "Extracorporeal shock wave lithotripsy today", "Add oral potassium citrate to dissolve the stone", "Start corticosteroids to reduce ureteric oedema"], 1,
         "นี่คือ **obstructive pyelonephritis with septic shock** — ปัสสาวะติดเชื้อค้างเหนือนิ่วเป็นหนองในถุงปิด แรงดันสูงดันเชื้อและ endotoxin เข้ากระแสเลือด และยาเข้าไม่ถึง → ต้อง **source control ด่วน: percutaneous nephrostomy (PCN) หรือ DJ stent** ร่วมกับยาปฏิชีวนะ (สไลด์: suspected urologic obstruction → imaging)\n\n- ยาอย่างเดียวไม่พอในไตที่อุดกั้นและติดเชื้อ\n- **ห้ามสลายนิ่ว (ESWL) ขณะติดเชื้อ** — ดันเชื้อเข้ากระแสเลือดมากขึ้น · เอานิ่วออกหลังติดเชื้อหายแล้ว\n- potassium citrate ใช้ละลายนิ่วกรดยูริก ช้าเป็นสัปดาห์\n- steroid ไม่มีบทบาท",
         "Pyelo + อุดกั้น + ช็อก → ระบายด่วน (PCN/DJ stent)", "Obstructive pyelonephritis", R("Complicated UTI — suspected urologic obstruction → imaging"), ["B9.2.2(2)", "2.3.14-3(9)", "2.3.14-3(15)", "2.2.48"]),
     mcq(N(19), "A 67-year-old man was discharged 10 days ago after a 2-week admission with an indwelling urinary catheter. He now has fever, suprapubic pain and pyuria. According to the lecture, which empirical regimen is most appropriate while awaiting culture results?",
         ["Oral nitrofurantoin", "Oral amoxicillin", "Intravenous piperacillin-tazobactam", "Single-dose oral fosfomycin", "No antibiotics until culture results return"], 2,
         "ชายที่เพิ่งนอนโรงพยาบาลนานและคาสายสวน = **complicated UTI ที่เสี่ยงเชื้อดื้อ/เชื้อในโรงพยาบาล (nosocomial/MDR risk)** — สไลด์ให้ใช้ **piperacillin/tazobactam, ceftazidime หรือ cefepime** ซึ่งครอบคลุม Pseudomonas และเชื้อในโรงพยาบาล แล้วลดระดับตามผลเพาะเชื้อ รวม 10–14 วัน\n\n- **nitrofurantoin และ fosfomycin** ไม่ถึงเนื้อเยื่อ และไม่เหมาะกับผู้ป่วยมีไข้ (อาจมี prostatitis/pyelonephritis)\n- **amoxicillin** เชื้อแกรมลบดื้อสูงมาก\n- ผู้ป่วยมีไข้และอาการ **ไม่ควรรอผลเพาะเชื้อ** ก่อนให้ยา",
         "Complicated + nosocomial/MDR risk → pip/tazo, ceftazidime, cefepime", "Empirical therapy of complicated UTI", R("3. Complicated UTI — empiric treatment"), ["B9.2.2(2)", "2.3.14(14)", "B1.7.2", "2.3.19(5)"]),
     mcq(N(20), "A 36-year-old woman has fever, left flank pain and pyuria with white blood cell casts. Contrast-enhanced CT shows several wedge-shaped, hypodense striations extending from the renal papillae to the cortex of the left kidney, without gas, hydronephrosis or a focal fluid collection. Which interpretation is most appropriate?",
         ["Renal abscess requiring percutaneous drainage", "Emphysematous pyelonephritis", "Acute pyelonephritis, managed with antibiotics alone", "Xanthogranulomatous pyelonephritis requiring nephrectomy", "Renal cell carcinoma"], 2,
         "สไลด์: CT ฉีดสารทึบรังสีที่เห็น **ริ้วสีจางรูปสามเหลี่ยม แผ่จากกรวยไตถึง cortex** = **acute pyelonephritis** — เชื้อลามจาก papilla ตามท่อไตในแนวรัศมี การอักเสบและหลอดเลือดหดตัวทำให้สารทึบรังสีเข้าน้อยเป็นลิ่ม → รักษาด้วยยาปฏิชีวนะ ไม่ต้องระบาย\n\n- **Renal abscess** เห็นเป็น **บริเวณสีจางขนาดใหญ่** (ก้อนหนอง) ไม่ใช่ริ้ว\n- **Emphysematous** ต้องมีก๊าซ\n- **XPN** เป็นไตโตหลายช่องร่วมกับนิ่ว (bear's paw)\n- มะเร็งไตเป็นก้อนเนื้อ ไม่ใช่ริ้วรูปลิ่มร่วมกับอาการติดเชื้อ",
         "CT: ลิ่มสามเหลี่ยมสีจาง = pyelo · ก้อนสีจางใหญ่ = ฝี", "CT findings of pyelonephritis", R("Renal and perinephric abscess — CT images"), ["B9.2.2(2)", "2.3.14(14)"]),
    ], nl=NLN + ["2.3.14-3(9)", "2.3.14-3(15)", "B9.2.3-3(1)", "2.2.48"], figs=F8)

# ───────────────────────────── 9
F9 = {
 "prostate": fig("Acute bacterial prostatitis — อาการแต่ละอย่างมาจากไหน",
  "ต่อมลูกหมากล้อมรอบ **prostatic urethra** และอยู่ชิดผนังหน้าของไส้ตรง · เมื่อติดเชื้อ ต่อมบวมในแคปซูล → **บีบท่อปัสสาวะ** (ลำเล็ก เบ่ง ปัสสาวะไม่ออก) · ต่อมมีหลอดเลือดมาก → **เชื้อเข้ากระแสเลือดง่าย** (ไข้สูง หนาวสั่น) — การ **นวดต่อมขณะอักเสบ** จึงดันเชื้อเข้าเลือด ห้ามทำ · ปวดฝีเย็บและทวารหนักผ่าน pelvic plexus (S2–S4) · ยาที่จะเข้าต่อมได้ต้อง **ละลายในไขมัน** (fluoroquinolone, TMP/SMX) เพราะมี blood–prostate barrier (เรียบเรียงจาก EAU 2025 — สไลด์ไม่มีหน้านี้)",
  svg(420, 396, "กลไกของอาการ acute bacterial prostatitis",
      ell(96, 74, 70, 48, "wa"), t(96, 70, "กระเพาะ", "sm mid"), t(96, 86, "ปัสสาวะ", "sm mid"),
      ell(96, 182, 58, 44, "lbad da"), ell(96, 182, 50, 38, "ms"),
      line(96, 122, 96, 300, "lac w3"),
      ar(58, 182, 88, 182, "lbad w2", "ah-bad"), ar(134, 182, 104, 182, "lbad w2", "ah-bad"),
      t(10, 244, "ท่อปัสสาวะถูกบีบ", "xs tbad"),
      ar(46, 166, 16, 140, "lbad", "ah-bad"), t(14, 128, "เลือด", "xs tbad"),
      rect(164, 112, 30, 200, "sk", 14), t(179, 330, "ไส้ตรง", "xs mid mu"),
      ar(182, 290, 156, 204, "lmu w3", "ah-mu"), t(150, 296, "DRE", "xs b end"),
      t(96, 318, "ต่อมบวมในแคปซูล", "xs mid tms"),
      line(136, 160, 214, 46, "lmu dt"),
      box(214, 12, 200, 62, "bad", "หลอดเลือดมาก\n→ เชื้อเข้าเลือด\n→ ไข้สูง หนาวสั่น", fs=11.5),
      line(106, 176, 214, 118, "lmu dt"),
      box(214, 86, 200, 62, "ms", "ต่อมบวมกด prostatic urethra\n→ ลำเล็ก เบ่ง\nปัสสาวะไม่ออก", fs=11.5),
      line(146, 196, 214, 186, "lmu dt"),
      box(214, 160, 200, 50, "sk", "pelvic plexus S2–S4\n→ ปวดฝีเย็บ ทวารหนัก", fs=11.5),
      line(176, 252, 214, 252, "lmu dt"),
      box(214, 222, 200, 62, "bad", "DRE: บวม นุ่ม ร้อน กดเจ็บมาก\nห้ามนวดต่อม\n(ดันเชื้อเข้ากระแสเลือด)", fs=11.5),
      box(214, 298, 200, 62, "ok", "blood–prostate barrier\nยาละลายไขมันผ่านได้\nFQ · TMP/SMX", fs=11.5),
      t(10, 384, "ชาย + ไข้ + LUTS = prostatitis จนกว่าจะพิสูจน์ได้ว่าไม่ใช่", "xs b i2"))),
}
sec("neph-uti-09", "UTI ในผู้ชายและต่อมลูกหมาก — เคส 4",
    "ทำไมชายเป็น UTI ต้องหาสาเหตุ · ซักประวัติและตรวจเคส 4 (DRE, post-void residual) · acute bacterial prostatitis · chronic bacterial prostatitis เป็นแหล่งของ relapse", 9,
"""> หัวข้อนี้ **ส่วนใหญ่ไม่ได้มาจากสไลด์** — สไลด์มีเพียง "Males = complicated UTI" · "prostatitis = failure to eradicate infection" และเคส 4 · เนื้อหา prostatitis เรียบเรียงจาก **EAU Guidelines on Urological Infections 2025** และตำรา เพราะคลังข้อสอบ Ward Drill ถามเรื่องนี้

### ทำไมชายเป็น UTI น้อย และเมื่อเป็นต้องหาสาเหตุเสมอ
- ท่อปัสสาวะยาวราว 20 ซม. ห่างทวารหนัก ผิวรอบรูเปิดแห้ง · **น้ำจากต่อมลูกหมากมีสังกะสีและสารต้านเชื้อ**
- ชายที่เป็น UTI จึงมักมีความผิดปกติแฝง: **ต่อมลูกหมากโต (BPH) → ปัสสาวะค้าง** · นิ่ว · ท่อปัสสาวะตีบ · สายสวน · neurogenic bladder · **ต่อมลูกหมากติดเชื้อ**
- ทุกรายจึงเป็น **complicated UTI** (สไลด์) — ส่ง urine culture ทุกราย

### เคส 4 — ชาย 70 ปี ปัสสาวะขัดมากขึ้น 1 วัน ไม่มีไข้
| ขั้น | ทำอะไร | ทำไม |
|---|---|---|
| ประวัติ | LUTS แบบอุดกั้น (ลำเล็ก เบ่ง ถ่ายไม่สุด ตื่นกลางคืน) · ไข้ หนาวสั่น ปวดฝีเย็บ · เคยเป็นซ้ำ · สายสวน หัตถการ · เบาหวาน | หาสาเหตุที่ทำให้ปัสสาวะค้าง และแยก prostatitis |
| ตรวจร่างกาย | คลำกระเพาะปัสสาวะโป่ง · เคาะ CVA · **DRE** (ขนาด ความนุ่ม กดเจ็บ ก้อนแข็ง) | ต่อมโตเรียบ = BPH · บวมนุ่มกดเจ็บ = prostatitis · แข็งเป็นก้อน = มะเร็ง |
| ส่งตรวจ | UA + **urine culture** · Cr · **post-void residual (PVR)** ด้วย US · US KUB ถ้าเป็นซ้ำ มีไข้ หรือไม่ดีขึ้น | PVR สูง = ปัสสาวะค้าง เป็นแหล่งเพาะเชื้อ |
| รักษา | ยาตาม complicated UTI (หัวข้อ 8) · แก้ปัจจัย เช่น α-blocker สำหรับ BPH · สวนปัสสาวะถ้าปัสสาวะไม่ออก | ยาอย่างเดียวไม่พอถ้าปัสสาวะยังค้าง |
PSA **ไม่ควรตรวจขณะติดเชื้อ** — การอักเสบทำให้ PSA สูงขึ้นชั่วคราว

### Acute bacterial prostatitis
[[fig:prostate]]
#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้สูง หนาวสั่น** | ต่อมมีหลอดเลือดมาก เชื้อเข้ากระแสเลือดง่าย | ชาย + ไข้ + อาการปัสสาวะ = prostatitis จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ |
| **ปวดฝีเย็บ ทวารหนัก ปวดเวลาเบ่งอุจจาระ** | ต่อมบวมในแคปซูล ส่งความรู้สึกผ่าน pelvic plexus (S2–S4) | ต่างจาก pyelonephritis ที่ปวดเอว |
| **ลำเล็ก เบ่ง ปัสสาวะไม่ออก** | ต่อมบวมกด prostatic urethra ที่วิ่งผ่านกลางต่อม | อาจเกิด acute urinary retention |
| **DRE: ต่อมบวม นุ่ม ร้อน กดเจ็บมาก (boggy, tender)** | บวมน้ำและหนองในต่อม | **ห้ามนวดต่อมลูกหมาก** — ดันเชื้อเข้ากระแสเลือด |
| แสบขัด ปัสสาวะบ่อย | cystitis และท่อปัสสาวะอักเสบร่วม | |
#### รักษา (EAU 2025)
- ยาที่ **เข้าต่อมลูกหมากได้** — ต่อมมี **blood–prostate barrier** ยาต้องละลายในไขมันและไม่แตกตัวมาก เช่น **fluoroquinolone, TMP/SMX** · ระยะเฉียบพลันการอักเสบเปิด barrier จึงเริ่มด้วยยาฉีดกลุ่ม β-lactam ได้ แล้วเปลี่ยนเป็นยากิน
- ระยะเวลา **2–4 สัปดาห์**
- ปัสสาวะไม่ออก → ใส่สายสวน (หรือ suprapubic catheter) · ไม่ดีขึ้น → TRUS หรือ CT หา **prostatic abscess** แล้วระบาย

### Chronic bacterial prostatitis — แหล่งของ relapse
ต่อมลูกหมากเก็บเชื้อไว้ (สไลด์: **prostatitis = failure to eradicate infection**) → UTI ซ้ำด้วย **เชื้อตัวเดิม** เป็นพัก ๆ ระหว่างนั้นอาจไม่มีอาการ · วินิจฉัยด้วยการเพาะปัสสาวะก่อนและหลังนวดต่อม (ทำในระยะที่ไม่อักเสบเฉียบพลัน) · รักษาด้วย **fluoroquinolone 4–6 สัปดาห์** (EAU 2025)
""",
    ["ชาย = complicated เสมอ → urine culture ทุกราย และหาสาเหตุ (BPH, PVR, นิ่ว)",
     "ชาย + ไข้ + LUTS + ปวดฝีเย็บ = acute bacterial prostatitis",
     "DRE: ต่อมบวมนุ่มกดเจ็บ — ห้ามนวดต่อม (bacteremia)",
     "Blood–prostate barrier → FQ/TMP-SMX · acute 2–4 สัปดาห์ · chronic 4–6 สัปดาห์ (EAU)",
     "Chronic bacterial prostatitis = relapse ด้วยเชื้อเดิม"],
    [mcq(N(21), "A 64-year-old man has fever 39.4 C, chills, dysuria, perineal pain and difficulty voiding. Digital rectal examination reveals an exquisitely tender, warm, boggy prostate. Which action should be avoided?",
         ["Obtaining blood and urine cultures", "Starting antibiotics that penetrate the prostate", "Vigorous prostatic massage to obtain expressed prostatic secretions",
          "Measuring post-void residual volume", "Placing a catheter if he develops urinary retention"], 2,
         "ภาพนี้คือ **acute bacterial prostatitis** — ต่อมที่บวม ร้อน กดเจ็บ มีเชื้อจำนวนมากและหลอดเลือดมาก **การนวดต่อมอย่างแรงจะดันเชื้อเข้ากระแสเลือด (bacteremia/sepsis)** และเจ็บมาก จึงห้ามทำ (การเพาะสารคัดหลั่งจากการนวดต่อมใช้ในระยะเรื้อรังเท่านั้น)\n\n- **เพาะเชื้อเลือดและปัสสาวะ** ควรทำก่อนให้ยา\n- **ยาที่เข้าต่อมได้** (fluoroquinolone, TMP/SMX หรือยาฉีดในระยะแรก) คือการรักษาหลัก\n- **PVR** และ **ใส่สายสวนเมื่อปัสสาวะไม่ออก** เป็นสิ่งที่ควรทำ เพราะต่อมบวมกดท่อปัสสาวะ",
         "Acute prostatitis: ห้ามนวดต่อม", "Acute bacterial prostatitis", ["EAU Guidelines on Urological Infections 2025 — ไม่อยู่ในสไลด์"], ["B9.2.2(2)", "2.3.14(8)", "2.1.45", "2.1.40"]),
     mcq(N(22), "A 58-year-old man has had four episodes of Escherichia coli cystitis in 18 months, each with the same susceptibility pattern, and is asymptomatic between episodes. Urine culture after prostatic massage grows the same organism. Which treatment is most appropriate?",
         ["Nitrofurantoin for 5 days", "Amoxicillin for 7 days", "A fluoroquinolone such as levofloxacin for 4–6 weeks", "Single-dose fosfomycin", "Intravenous ceftriaxone for 3 days"], 2,
         "UTI ซ้ำด้วย **เชื้อตัวเดิม** ในชาย และเพาะได้เชื้อเดิมจากสารคัดหลั่งหลังนวดต่อม = **chronic bacterial prostatitis** (สไลด์: prostatitis = failure to eradicate infection) · ต่อมมี **blood–prostate barrier** ยาที่ผ่านได้ต้องละลายในไขมัน → **fluoroquinolone 4–6 สัปดาห์** (EAU 2025) หรือ TMP/SMX ถ้าไว\n\n- **Nitrofurantoin และ fosfomycin** อยู่แต่ในปัสสาวะ ไม่เข้าต่อม\n- **Amoxicillin** และ **ceftriaxone** ผ่าน barrier ได้น้อย และระยะเวลาสั้นเกินไปที่จะกำจัดเชื้อในต่อม",
         "Chronic bacterial prostatitis → FQ 4–6 สัปดาห์", "Chronic bacterial prostatitis", ["EAU Guidelines on Urological Infections 2025 · สไลด์ — failure to eradicate: prostatitis"], ["B9.2.2(2)", "2.3.14(8)", "B1.7.1(1)"]),
    ], nl=NLN + ["2.3.14(8)", "B10.2.4(2)", "B9.2.3(1)", "2.1.45"], figs=F9,
    source="เรียบเรียงจาก EAU Guidelines on Urological Infections 2025 และตำรา (ไม่อยู่ในสไลด์) · เคส 4 และ \"Males = complicated\" จากสไลด์ อ.กรทิพย์")

# ───────────────────────────── 10
F10 = {
 "recur": fig("Relapse กับ reinfection — แยกด้วยเวลาและสายพันธุ์",
  "**Relapse** (บน): เชื้อสายพันธุ์เดิมกลับมา **ภายใน 2 สัปดาห์** หลังรักษา เพราะเชื้อไม่เคยหมด — ซ่อนอยู่ในแหล่งที่ยาเข้าไม่ถึง (สไลด์: นิ่ว ไตเป็นแผลเป็น PKD prostatitis) → ต้อง **หาแหล่งด้วยภาพ แล้วเอาออก** · **Reinfection** (ล่าง): ปัสสาวะปลอดเชื้อแล้ว **เกิน 2 สัปดาห์** จึงติดใหม่จากเชื้อในลำไส้หรือช่องคลอด (ตัวเดิมหรือตัวใหม่ก็ได้) → ป้องกันที่พฤติกรรมและปัจจัยเสี่ยง",
  svg(420, 312, "เส้นเวลาเปรียบเทียบ relapse และ reinfection หลังรักษา UTI",
      t(10, 20, "Relapse — เชื้อตัวเดิม ภายใน 2 สัปดาห์", "sm b tbad"),
      line(30, 70, 410, 70, "lmu"),
      circ(30, 70, 8, "badf"), t(30, 98, "UTI\n+ ยาครบ", "xs mid i2"),
      path("M38 78 C58 122 86 122 104 80", "lbad da", "ah-bad"), t(72, 136, "ซ่อนในแหล่ง", "xs mid tbad"),
      circ(110, 70, 8, "badf"), t(110, 54, "ซ้ำ", "xs b mid tbad"),
      box(150, 84, 260, 58, "bad", "แหล่งซ่อน: นิ่ว · ต่อมลูกหมาก\nไตแผลเป็น · PKD → หาและเอาออก", fs=11.5),
      line(130, 40, 130, 156, "lmu da"), line(130, 198, 130, 238, "lmu da"),
      t(136, 44, "2 สัปดาห์", "xs mu"),
      t(10, 186, "Reinfection — หลัง 2 สัปดาห์ เชื้อใหม่หรือเดิม", "sm b tms"),
      circ(30, 226, 8, "badf"), line(40, 226, 296, 226, "lok w3"),
      t(214, 218, "ปัสสาวะปลอดเชื้อ", "xs mid tok"),
      circ(306, 226, 8, "msf"), t(306, 208, "ซ้ำ", "xs b mid tms"), line(316, 226, 410, 226, "lmu"),
      box(250, 254, 160, 32, "sk", "เชื้อจากลำไส้ / ช่องคลอด", fs=11),
      ar(330, 254, 312, 236, "lms", "ah-ms"),
      box(10, 254, 230, 32, "ok", "ป้องกัน: พฤติกรรม · estrogen", fs=11),
      t(10, 304, "แยกไม่ได้ด้วยอาการ — ต้องดูเวลาและผลเพาะเชื้อ", "xs mu"))),
}
sec("neph-uti-10", "Recurrent UTI — relapse หรือ reinfection — เคส 1",
    "≥ 2 ครั้งใน 6 เดือน หรือ ≥ 3 ครั้งใน 12 เดือน · relapse ≤ 2 สัปดาห์เชื้อเดิม · reinfection > 2 สัปดาห์ · failure to eradicate · ปัจจัยเสี่ยงและการป้องกันพร้อมกลไก", 9,
"""### นิยาม (สไลด์)
**Recurrent UTI = ≥ 2 ครั้งใน 6 เดือน หรือ ≥ 3 ครั้งใน 12 เดือน** — เคส 1 (2 ครั้งใน 6 เดือน) เข้าเกณฑ์
| ชนิด | นิยาม (สไลด์) | ต้นเหตุ | แนวทาง |
|---|---|---|---|
| **Reinfection** | กลับเป็นด้วยเชื้อเดิมหรือเชื้อใหม่ **หลัง 2 สัปดาห์** | เชื้อจากลำไส้หรือช่องคลอดขึ้นมาใหม่ | ป้องกันที่พฤติกรรมและปัจจัยเสี่ยง |
| **Relapse** | กลับเป็นด้วย **เชื้อสายพันธุ์เดิมภายใน 2 สัปดาห์** | เชื้อไม่เคยหมด มีแหล่งซ่อน | หาแหล่งด้วยภาพ |
| **Failure to eradicate** | — | **นิ่ว · ไตเป็นแผลเป็น · PKD · prostatitis** | เอาแหล่งออก (เช่นนิ่ว struvite ต้องเอาออกหมด) |

[[fig:recur]]

### ปัจจัยเสี่ยง (สไลด์) — และทำไมจึงเสี่ยง
| ปัจจัย | กลไก |
|---|---|
| **เพศสัมพันธ์** | ดันเชื้อจากปากช่องคลอดเข้าท่อปัสสาวะ |
| **Diaphragm + spermicide** | spermicide (nonoxynol-9) ฆ่า lactobacilli แต่ E. coli ทนได้ → E. coli ครองปากช่องคลอด · diaphragm กดท่อปัสสาวะ ถ่ายไม่หมด |
| **ปัสสาวะเล็ด, cystocele** | กระเพาะหย่อน ถ่ายไม่หมด · ความชื้นรอบรูเปิด |
| **ปัสสาวะค้างหลังถ่าย (post-voiding residual)** | ไม่มีการชะล้าง เชื้อแบ่งตัวได้เต็มที่ |
| **ปัจจัยทางชีวภาพ/พันธุกรรม** | วัยหมดประจำเดือน (estrogen ลด) · ประวัติ UTI ในแม่ · เยื่อบุบางคนมีตัวรับให้ E. coli เกาะมากกว่า (เช่น non-secretor ของหมู่เลือด) |

### การป้องกันและจัดการ (สไลด์)
| วิธี | ทำงานอย่างไร |
|---|---|
| **ปรับพฤติกรรม · สุขอนามัย** | ลดการนำเชื้อเข้าท่อปัสสาวะ |
| **ดื่มน้ำมาก (liberal fluid intake)** | ถ่ายบ่อยขึ้น ชะเชื้อออกก่อนเกาะ — RCT ปี 2018 ในหญิงที่ดื่มน้ำน้อย การดื่มเพิ่มวันละ 1.5 ลิตรลดการเป็นซ้ำราวครึ่งหนึ่ง |
| **ปัสสาวะหลังมีเพศสัมพันธ์ (postcoital voiding)** | ชะเชื้อที่ถูกดันเข้าท่อก่อนจะเกาะเยื่อบุ |
| **เปลี่ยนวิธีคุมกำเนิด** | เลิก spermicide และ diaphragm |
| **Topical (vaginal) estrogen ในวัยหมดประจำเดือน** | estrogen เพิ่ม glycogen ในเยื่อบุช่องคลอด → lactobacilli กลับมา → สร้างกรดแลคติก **pH ช่องคลอดต่ำ** → E. coli ตั้งถิ่นฐานที่ปากช่องคลอดไม่ได้ |
| **Ultrasound หรือ cystoscopy (บางราย)** | หาแหล่งของ relapse หรือความผิดปกติทางกายวิภาค |
ทางเลือกเพิ่มเติม (ไม่อยู่ในสไลด์ — AUA/CUA/SUFU 2019 และ EAU 2025): ยาปฏิชีวนะป้องกันขนาดต่ำต่อเนื่อง หรือกินครั้งเดียวหลังมีเพศสัมพันธ์ · ให้ผู้ป่วยเริ่มยาเองเมื่อมีอาการ (self-start) หลังเพาะเชื้อ · methenamine hippurate · ผลิตภัณฑ์ cranberry (หลักฐานจำกัด)

### กลับไปที่เคส 1
หญิง 48 ปี เป็น 2 ครั้งใน 6 เดือน ซื้อยากินเอง → **เพาะเชื้อก่อนให้ยาครั้งนี้** (ซื้อยาบ่อยเสี่ยงเชื้อดื้อ) · ซักเรื่องเพศสัมพันธ์ วิธีคุมกำเนิด การดื่มน้ำ ประจำเดือน (ใกล้วัยหมดประจำเดือน) ปัสสาวะเล็ด · ตรวจหา cystocele · ถ้าเป็นซ้ำเร็วด้วยเชื้อเดิมหรือมีไข้ → US ไตหาแหล่งซ่อน
""",
    ["Recurrent UTI = ≥ 2 ครั้ง/6 เดือน หรือ ≥ 3 ครั้ง/12 เดือน",
     "Relapse = เชื้อเดิมภายใน 2 สัปดาห์ (มีแหล่งซ่อน → imaging) · Reinfection = หลัง 2 สัปดาห์",
     "Failure to eradicate: นิ่ว ไตแผลเป็น PKD prostatitis",
     "Spermicide ฆ่า lactobacilli · vaginal estrogen ทำให้ lactobacilli และ pH ต่ำกลับมา",
     "ดื่มน้ำมาก + ปัสสาวะหลังเพศสัมพันธ์ = เพิ่มการชะล้าง"],
    [mcq(N(23), "A 41-year-old woman completed 7 days of ciprofloxacin for Escherichia coli pyelonephritis. Ten days after finishing therapy she again has fever and flank pain, and the urine grows Escherichia coli with an identical susceptibility pattern. How should this episode be classified, and what should be done?",
         ["Reinfection; advise postcoital voiding only", "Relapse; image the urinary tract to look for a persistent focus such as a stone, abscess or obstruction",
          "Asymptomatic bacteriuria; no treatment needed", "Reinfection; start long-term prophylaxis without further evaluation", "Contamination; repeat the culture next month"], 1,
         "สไลด์: **relapse = กลับเป็นด้วยเชื้อสายพันธุ์เดิมภายใน 2 สัปดาห์** — แปลว่าเชื้อไม่เคยหมดไป มี **แหล่งซ่อนที่ยาเข้าไม่ถึง** (นิ่ว ฝี การอุดกั้น ไตแผลเป็น) → ต้อง **ทำภาพทางเดินปัสสาวะ** (สไลด์: imaging reserved for … relapse within a few weeks of treatment) แล้วรักษาแหล่งนั้น\n\n- **Reinfection** คือหลัง 2 สัปดาห์ (เชื้อใหม่หรือเดิมจากลำไส้/ช่องคลอด) จึงเน้นป้องกัน\n- ผู้ป่วยมีไข้และปวดเอว ไม่ใช่ ASB\n- การให้ยาป้องกันระยะยาวโดยไม่หาแหล่งจะพลาดสาเหตุที่แก้ได้\n- เชื้อเดิมรูปแบบความไวเดิมพร้อมอาการ ไม่ใช่การปนเปื้อน",
         "Relapse (≤ 2 สัปดาห์ เชื้อเดิม) → หาแหล่งด้วยภาพ", "Relapse vs reinfection", R("Recurrent UTIs · Clinical response — imaging"), ["B9.2.2(2)", "2.3.14(14)", "2.3.14-3(9)"]),
     mcq(N(24), "A 62-year-old postmenopausal woman has had three episodes of culture-proven cystitis in the past year. She has vaginal atrophy and no urinary tract abnormality on ultrasound. Vaginal oestrogen is prescribed. What is the mechanism by which it reduces recurrence?",
         ["It increases urine output and dilutes bacteria", "It acidifies the urine directly and kills Escherichia coli in the bladder",
          "It restores glycogen-rich vaginal epithelium so lactobacilli recolonise and lower the vaginal pH, preventing Escherichia coli colonisation of the introitus", "It blocks FimH binding to uroplakin", "It has a direct antibacterial effect against Gram-negative bacilli"], 2,
         "สไลด์แนะนำ **topical estrogen ในหญิงวัยหมดประจำเดือน** — estrogen ทำให้เยื่อบุช่องคลอดหนาและมี **glycogen** ซึ่ง lactobacilli ใช้สร้างกรดแลคติก → **pH ช่องคลอดต่ำ** → E. coli จากลำไส้ตั้งถิ่นฐานที่ปากช่องคลอดไม่ได้ จึงไต่ขึ้นท่อปัสสาวะไม่ได้\n\n- estrogen ไม่ได้เพิ่มปริมาณปัสสาวะ\n- ไม่ได้ทำให้ปัสสาวะในกระเพาะเป็นกรดหรือฆ่าเชื้อโดยตรง\n- ไม่ได้ยับยั้ง FimH (กลไกนี้เป็นเป้าของ D-mannose ที่ยังอยู่ระหว่างศึกษา)",
         "Vaginal estrogen → lactobacilli กลับมา → pH ต่ำ → E. coli เกาะไม่ได้", "Prevention of recurrent UTI", R("Recurrent UTIs — management: topical estrogen"), ["B9.2.2(1)", "2.3.14(7)", "2.3.14(11)"]),
    ], nl=NLN + ["2.3.14-3(15)", "2.3.14-3(10)"], figs=F10)

# ───────────────────────────── 11
F11 = {
 "biofilm": fig("สายสวนกับ biofilm — ทำไมคาสายแล้วมีเชื้อแทบทุกราย",
  "เชื้อเข้าได้สองทาง: **นอกสาย (extraluminal)** ไต่จากฝีเย็บตามผิวนอกของสาย (ช่วงแรก พบมากในหญิง) และ **ในสาย (intraluminal)** จากถุงหรือข้อต่อที่ถูกเปิด · เมื่อเกาะผิวสายเชื้อสร้าง **biofilm** ห่อตัวเอง แบ่งตัวช้า ยาและเม็ดเลือดขาวเข้าไม่ถึง · Proteus สร้าง urease → ปัสสาวะด่าง → ผลึก struvite ใน biofilm → **สายอุดตัน** · ปัสสาวะที่ไหลผ่านสายเก่าจึงมีเชื้อจาก biofilm ไม่ใช่เชื้อในกระเพาะ → **ถอดหรือเปลี่ยนสายก่อนเก็บปัสสาวะส่งเพาะ**",
  svg(420, 380, "เส้นทางที่เชื้อเข้าตามสายสวนปัสสาวะและโครงสร้าง biofilm",
      ell(112, 80, 84, 56, "wa"), t(112, 52, "กระเพาะปัสสาวะ", "xs mid"),
      circ(112, 106, 12, "bx"),
      line(106, 118, 106, 322, "ln w2"), line(118, 118, 118, 322, "ln w2"),
      line(96, 136, 96, 262, "lac"), line(128, 136, 128, 262, "lac"),
      ar(100, 256, 100, 150, "lbad w2", "ah-bad"),
      t(90, 200, "นอกสาย\n(ช่วงแรก)", "xs b end tbad"),
      ar(112, 318, 112, 170, "lbad da", "ah-bad"),
      t(124, 296, "ในสาย\n(ถุง/ข้อต่อเปิด)", "xs b tbad"),
      rect(82, 324, 60, 44, "sk", 6), t(112, 350, "ถุง", "xs mid"),
      t(322, 22, "ซูมผิวสายสวน", "sm b mid"),
      circ(254, 46, 4, "acf"), circ(292, 40, 4, "acf"), circ(330, 48, 4, "acf"),
      ar(292, 48, 292, 84, "lac", "ah-ac"), t(300, 70, "ยาเข้าน้อย", "xs tac"),
      rect(236, 90, 168, 60, "ms", 16),
      ell(256, 120, 7, 3, "badf"), ell(280, 106, 7, 3, "badf"), ell(300, 128, 7, 3, "badf"),
      ell(330, 112, 7, 3, "badf"), ell(352, 128, 7, 3, "badf"), ell(378, 108, 7, 3, "badf"),
      poly([(316, 132), (322, 138), (316, 144), (310, 138)], "inkf", True), poly([(366, 132), (372, 138), (366, 144), (360, 138)], "inkf", True),
      line(230, 152, 410, 152, "ln w3"), t(410, 168, "ผิวสายสวน", "xs end mu"),
      t(236, 186, "biofilm: เมือกห่อเชื้อ เชื้อโตช้า", "xs i2"), t(236, 200, "ยาและเม็ดเลือดขาวเข้าไม่ถึง", "xs i2"),
      t(236, 220, "Proteus: urease → ด่าง →", "xs i2"), t(236, 234, "ผลึก struvite → สายอุดตัน", "xs i2"),
      box(230, 252, 184, 54, "ok", "ถอด/เปลี่ยนสายก่อน\nเก็บปัสสาวะส่งเพาะ", fs=11.5),
      box(230, 318, 184, 50, "sk", "มีเชื้อเพิ่ม 3–7% ต่อวัน\nที่คาสาย (IDSA 2009)", fs=11))),
}
sec("neph-uti-11", "Catheter-associated UTI และ funguria",
    "เกณฑ์ CA-UTI (สไลด์ ≥ 10² มีอาการ · ≥ 10⁵ ไม่มีอาการ) · biofilm · เปลี่ยนสายก่อนเพาะเชื้อ · ป้องกัน: CIC เปลี่ยนสายทุก 4 สัปดาห์ · purple urine bag · candiduria รักษาเมื่อไร", 9,
"""### เกณฑ์ (สไลด์)
| | เกณฑ์ | ทำอะไร |
|---|---|---|
| คาสายสวน **ไม่มีอาการ** (CA-ASB) | **≥ 10⁵ CFU/mL** | **ไม่รักษา** |
| คาสายสวน **มีอาการ** (CA-UTI) | **≥ 10² CFU/mL** (สไลด์) · IDSA 2009 ใช้ ≥ 10³ | รักษา + เปลี่ยนสาย |
อาการของ CA-UTI ที่ใช้ได้: **ไข้ที่ไม่มีสาเหตุอื่น หนาวสั่น สับสนใหม่ ปวดท้องน้อยหรือ CVA ปัสสาวะเป็นเลือด** · ส่วน **ปัสสาวะขุ่น มีกลิ่น หรือตะกอน ไม่ใช่ข้อบ่งชี้ให้ยา**

### ทำไมคาสายแล้วมีเชื้อแทบทุกราย — biofilm (อาจารย์เขียนกำกับว่า "biofilm")
[[fig:biofilm]]
- สายสวน **ข้ามกลไกป้องกันทุกอย่าง** — เปิดทางจากภายนอกเข้ากระเพาะตลอดเวลา และกระเพาะไม่ได้บีบถ่ายจนหมด (มีปัสสาวะค้างใต้ balloon)
- เชื้อเกาะผิวสาย สร้าง **biofilm** (เมือก polysaccharide) → เชื้อในนั้นแบ่งตัวช้า ยาที่ฆ่าเชื้อที่กำลังแบ่งตัวได้ผลน้อย ยาและเม็ดเลือดขาวแทรกเข้าไปยาก
- **Proteus (urease)** ทำให้ปัสสาวะด่าง ผลึก struvite ฝังใน biofilm → สายอุดตัน
- โอกาสมีเชื้อเพิ่มขึ้น **3–7% ต่อวัน** ที่คาสาย (IDSA 2009) → คาเกินหนึ่งเดือนแทบทุกรายมี bacteriuria — นี่คือเหตุผลที่ **ไม่รักษา CA-ASB** (รักษาแล้วก็กลับมาใหม่ และเลือกเชื้อดื้อ)

#### ผลต่อการปฏิบัติ
- **ถอดหรือเปลี่ยนสายก่อนเก็บปัสสาวะส่งเพาะ** ถ้าคามานานเกิน 2 สัปดาห์ (IDSA 2009) — ปัสสาวะที่ผ่านสายเก่าพาเชื้อจาก biofilm มาด้วย
- เก็บจาก **sampling port ด้วยเทคนิคปลอดเชื้อ** ห้ามเก็บจากถุง
- เชื้อหลากหลายกว่า: E. coli, Klebsiella, Proteus, Pseudomonas, **Enterococcus**, Candida — เลือกยาแบบ complicated UTI (หัวข้อ 8)

### การป้องกัน (สไลด์)
| วิธี | เหตุผล |
|---|---|
| **ถอดสายเร็วที่สุด → clean intermittent catheterization (CIC)** | ไม่มีสายค้าง ไม่มี biofilm กระเพาะได้ระบายหมดเป็นระยะ |
| เทคนิคใส่สายปลอดเชื้อ · ระบบปิด · ถุงต่ำกว่ากระเพาะ | ลดทั้งทางนอกสายและทางในสาย (ปัสสาวะไหลย้อน) |
| **เปลี่ยนสายทุก 4 สัปดาห์** | ก่อน biofilm และผลึกหนาจนอุดตัน |
| วัสดุและสารเคลือบ (silver, antimicrobial) | ชะลอการเกาะของเชื้อในระยะสั้น |
| ยาปฏิชีวนะป้องกัน (?), probiotics | **ไม่แนะนำเป็นประจำ** — เลือกเชื้อดื้อ |

### Purple urine bag syndrome
tryptophan ในอาหาร → แบคทีเรียในลำไส้เปลี่ยนเป็น indole → ตับเปลี่ยนเป็น **indoxyl sulfate** ขับออกทางปัสสาวะ → แบคทีเรียในปัสสาวะที่เป็นด่างย่อยต่อเป็น **indigo (น้ำเงิน) + indirubin (แดง)** ติดผนังถุงพลาสติก → ถุงเป็นสีม่วง · พบในผู้สูงอายุติดเตียง ท้องผูก คาสายนาน · **ตัวมันเองไม่อันตราย** แต่บอกว่ามีเชื้อมากและปัสสาวะด่าง → ประเมินอาการ เปลี่ยนสาย แก้ท้องผูก

### Funguria (สไลด์)
- พบบ่อยในผู้ป่วยในและ **ส่วนใหญ่ไม่อันตราย** · เชื้อหลัก **Candida albicans** และ Candida ชนิดอื่น
- คำถามสำคัญคือ **infection หรือ colonization** · ปัจจัย: **คาสายสวนนาน** ยาปฏิชีวนะกว้าง เบาหวาน steroid
| สถานการณ์ | ทำอะไร (สไลด์) |
|---|---|
| **Asymptomatic candiduria** | **ไม่รักษา** — ถอดหรือเปลี่ยนสาย หยุดยาปฏิชีวนะที่ไม่จำเป็น |
| **เสี่ยงแพร่กระจาย: neutropenia · ทารกน้ำหนักน้อยมาก (< 1500 g) · จะทำหัตถการทางเดินปัสสาวะ** | รักษา |
| **มีอาการ** (แสบขัด ปัสสาวะบ่อย ปวดท้องน้อย) | **Fluconazole** |
| เสี่ยงดื้อ fluconazole (เช่น C. glabrata, C. krusei) | **Amphotericin B** |
#### ทำไม fluconazole ใช้ได้ แต่ echinocandin และ voriconazole ใช้ไม่ได้
fluconazole ละลายน้ำ ขับทางไตในรูปเดิม **ความเข้มข้นในปัสสาวะสูง** · echinocandin และ voriconazole **แทบไม่ออกมาในปัสสาวะ** จึงไม่เหมาะกับ cystitis จาก Candida (IDSA 2016)
""",
    ["CA-UTI (สไลด์): มีอาการ ≥ 10² · ไม่มีอาการ ≥ 10⁵ (ไม่รักษา) · IDSA ≥ 10³",
     "ปัสสาวะขุ่น/มีกลิ่นในผู้คาสาย ไม่ใช่ข้อบ่งชี้ให้ยา",
     "เปลี่ยนสายก่อนเก็บปัสสาวะส่งเพาะ (biofilm) · เก็บจาก sampling port",
     "ป้องกัน: ถอดสาย → CIC · ระบบปิด · เปลี่ยนสายทุก 4 สัปดาห์",
     "Candiduria ไม่มีอาการ = ไม่รักษา ยกเว้น neutropenia ทารก < 1500 g ก่อนหัตถการ · มีอาการ = fluconazole"],
    [mcq(N(25), "A 79-year-old bedridden man has had an indwelling urethral catheter for 2 months. He develops fever 38.7 C without another source. Before starting antibiotics, how should the urine specimen for culture be obtained?",
         ["Aspirate urine from the drainage bag", "Send the tip of the old catheter for culture", "Replace the catheter and collect urine from the newly inserted catheter",
          "Wait until the fever has resolved before collecting urine", "Collect a clean-catch midstream specimen around the catheter"], 2,
         "สายที่คามานานเกิน 2 สัปดาห์ถูกปกคลุมด้วย **biofilm** — ปัสสาวะที่ไหลผ่านสายเก่าจะพาเชื้อจาก biofilm มาด้วย ซึ่งอาจไม่ใช่เชื้อที่ก่อโรคในกระเพาะ → **เปลี่ยนสายใหม่แล้วเก็บจากสายใหม่** (IDSA 2009) จะได้ผลที่สะท้อนเชื้อจริง และการเปลี่ยนสายยังช่วยกำจัดแหล่งเชื้อ\n\n- **ปัสสาวะในถุง** ค้างที่อุณหภูมิห้อง เชื้อแบ่งตัวและปนเปื้อน\n- **ปลายสาย** ปนเชื้อจากท่อปัสสาวะเสมอ แปลผลไม่ได้\n- **ไม่ควรรอ** — ผู้ป่วยมีไข้ต้องเก็บแล้วเริ่มยาทันที\n- เก็บ clean-catch รอบสายไม่ได้ในผู้ที่คาสาย",
         "CA-UTI: เปลี่ยนสายก่อนเก็บปัสสาวะส่งเพาะ", "Urine collection in catheterised patients", R("Catheter-associated UTI — biofilm"), ["B9.3(1)", "2.3.19(5)", "B9.2.2(1)"]),
     mcq(N(26), "A 68-year-old woman in the intensive care unit with an indwelling catheter and receiving broad-spectrum antibiotics has Candida albicans at more than 100,000 CFU/mL in the urine. She is afebrile, has no urinary symptoms, and her neutrophil count is normal. No urologic procedure is planned. What is the most appropriate management?",
         ["Oral fluconazole for 14 days", "Intravenous amphotericin B", "Remove or replace the catheter and stop unnecessary antibiotics, without antifungal therapy",
          "Intravenous micafungin", "Daily bladder irrigation with amphotericin B"], 2,
         "สไลด์: **asymptomatic candiduria — usually no treatment** · รักษาเฉพาะผู้ที่ **เสี่ยงแพร่กระจาย (neutropenia, ทารกน้ำหนักน้อยกว่า 1500 g, จะทำหัตถการทางเดินปัสสาวะ)** หรือมีอาการ · ผู้ป่วยรายนี้ไม่เข้าข้อใด → แก้ปัจจัยเสี่ยง คือ **ถอดหรือเปลี่ยนสายและหยุดยาปฏิชีวนะที่ไม่จำเป็น** ซึ่งทำให้ candiduria หายเองได้บ่อย\n\n- **Fluconazole** ใช้เมื่อมีอาการหรือเสี่ยงแพร่กระจาย\n- **Amphotericin B** ใช้เมื่อเสี่ยงดื้อ fluconazole และมีข้อบ่งชี้รักษา · การล้างกระเพาะด้วย amphotericin B ไม่แนะนำเป็นประจำ\n- **Micafungin** แทบไม่ออกมาในปัสสาวะ",
         "Asymptomatic candiduria → ถอด/เปลี่ยนสาย ไม่ต้องให้ยาต้านเชื้อรา", "Funguria", R("Funguria"), ["2.3.1-3(7)", "2.3.19(5)", "B9.2.2(1)"]),
    ], nl=NLN + ["2.3.19(5)", "2.3.1-3(7)", "B1.5.2(3)"], figs=F11)

# ───────────────────────────── 12
F12 = {
 "gas": fig("Emphysematous pyelonephritis — ก๊าซมาจากไหน",
  "สามปัจจัยมาบรรจบกัน: **น้ำตาลในเนื้อเยื่อสูง** (เบาหวานคุมไม่ได้) เป็นสารตั้งต้น · **เลือดไปเลี้ยงน้อย** (microangiopathy ของเบาหวาน ไตบวมในแคปซูล) ทำให้เนื้อเยื่อขาดออกซิเจนและพาก๊าซออกไม่ทัน · **การอุดกั้น** (นิ่ว papillary necrosis — สไลด์) เพิ่มแรงดันและการคั่ง → E. coli และ Klebsiella (65–100% — สไลด์) ซึ่งเป็น facultative anaerobe **หมักน้ำตาลแบบ mixed-acid fermentation** ได้ CO₂ และ H₂ สะสมในเนื้อไต → เนื้อตายลาม (AKI 60%) และ toxin เข้ากระแสเลือด (septic shock 19%) · ฟองในปัสสาวะและคลำได้กรอบแกรบพบไม่ถึง 10%",
  svg(420, 334, "กลไกการเกิดก๊าซใน emphysematous pyelonephritis",
      box(10, 10, 128, 56, "ms", "น้ำตาลในเนื้อเยื่อสูง\n(DM คุมไม่ได้)", fs=11),
      box(146, 10, 128, 56, "bad", "เลือดไปเลี้ยงน้อย\n(microangiopathy)", fs=11),
      box(282, 10, 128, 56, "sk", "อุดกั้น\n(นิ่ว · papillary\nnecrosis)", fs=11),
      ar(74, 66, 150, 96, "ln", "ah"), ar(210, 66, 210, 96, "ln", "ah"), ar(346, 66, 270, 96, "ln", "ah"),
      box(70, 98, 280, 58, "ac", "E. coli / Klebsiella หมักน้ำตาล\n(mixed-acid fermentation)", fs=12),
      ar(210, 156, 210, 182, "ln", "ah"),
      box(70, 184, 280, 46, "bad", "CO₂ + H₂ สะสมในเนื้อไต — ระบายไม่ทัน", fs=12),
      circ(34, 200, 7, "lmu"), circ(46, 220, 5, "lmu"), circ(28, 226, 4, "lmu"),
      circ(384, 198, 6, "lmu"), circ(396, 220, 4, "lmu"), circ(376, 222, 5, "lmu"),
      ar(130, 230, 74, 260, "ln", "ah"), ar(210, 230, 210, 260, "ln", "ah"), ar(290, 230, 346, 260, "ln", "ah"),
      box(10, 262, 128, 58, "bad", "เนื้อไตตาย\n→ AKI (60%)", fs=11),
      box(146, 262, 128, 58, "bad", "toxin เข้าเลือด\n→ shock (19%)", fs=11),
      box(282, 262, 128, 58, "sk", "ฟองในปัสสาวะ ·\nกรอบแกรบ (< 10%)", fs=11))),
 "epnclass": fig("แบ่ง class ตามตำแหน่งของก๊าซใน CT (Huang & Tseng)",
  "ก๊าซยิ่งลามออกไปนอกไตมาก การพยากรณ์โรคยิ่งแย่ · **I** อยู่ใน collecting system · **II** อยู่ในเนื้อไต · **IIIA** ลามเข้า **perinephric space** (ระหว่างแคปซูลไตกับ Gerota fascia) · **IIIB** ลามเลย **Gerota fascia** ออกไป pararenal space · **IV** ไตทั้งสองข้าง หรือไตข้างเดียวที่เหลืออยู่ — **CT KUB เป็นวิธีวินิจฉัยที่ดีที่สุด** (สไลด์) เพราะบอกได้ทั้งตำแหน่งของก๊าซ การอุดกั้น และฝีในคราวเดียว",
  svg(420, 352, "ตำแหน่งของก๊าซในแต่ละ class ของ emphysematous pyelonephritis",
      ell(140, 180, 125, 158, "lmu da"), t(140, 14, "Gerota fascia", "xs mid mu"),
      ell(140, 180, 72, 112, "ac"),
      ell(166, 182, 24, 38, "wa"),
      circ(160, 170, 4, "bx"), circ(171, 184, 4, "bx"), circ(161, 196, 4, "bx"), t(192, 160, "I", "b"),
      circ(118, 108, 4, "bx"), circ(130, 96, 4, "bx"), circ(110, 122, 4, "bx"), circ(124, 118, 3, "bx"), t(98, 98, "II", "b"),
      circ(42, 196, 4, "bx"), circ(50, 210, 4, "bx"), circ(38, 214, 3, "bx"), t(46, 240, "IIIA", "b"),
      circ(26, 54, 4, "bx"), circ(36, 66, 4, "bx"), circ(20, 72, 3, "bx"), t(46, 48, "IIIB", "b"),
      t(140, 300, "แคปซูลไต", "xs mid tac"),
      t(290, 60, "I", "b"), t(316, 60, "collecting system", "xs i2"),
      t(290, 92, "II", "b"), t(316, 92, "เนื้อไต", "xs i2"),
      t(290, 124, "IIIA", "b"), t(326, 124, "perinephric", "xs i2"), t(326, 138, "(ใน Gerota)", "xs mu"),
      t(290, 170, "IIIB", "b"), t(326, 170, "pararenal", "xs i2"), t(326, 184, "(เลย fascia)", "xs mu"),
      t(290, 216, "IV", "b"), t(316, 216, "สองข้าง / ไตเดียว", "xs i2"),
      ell(320, 262, 14, 24, "ac"), ell(370, 262, 14, 24, "ac"),
      circ(318, 256, 3, "bx"), circ(324, 268, 3, "bx"), circ(368, 258, 3, "bx"), circ(374, 270, 3, "bx"),
      t(345, 306, "CT KUB = ดีที่สุด", "xs b mid tac"))),
}
sec("neph-uti-12", "การติดเชื้อไตชนิดพิเศษ — emphysematous, XPN และถุงน้ำติดเชื้อใน ADPKD",
    "Emphysematous pyelonephritis ในเบาหวาน (กลไกก๊าซ class I–IV CT KUB) · XPN (ก้อนในไตข้างเดียว นิ่ว bear's paw) · kidney cyst infection ใน ADPKD (KDIGO 2025 · ยาละลายไขมัน 4–6 สัปดาห์)", 12,
"""### Emphysematous cystitis และ pyelonephritis (สไลด์)
- การติดเชื้อของทางเดินปัสสาวะส่วนล่างหรือบน **ที่มีการสร้างก๊าซ** — เป็น **gas-forming และ necrotizing infection**
- ปัจจัยเสี่ยง: **เบาหวาน** · **ทางเดินปัสสาวะอุดกั้น** (นิ่วในไตหรือท่อไต, papillary necrosis)
- เชื้อ: **E. coli หรือ K. pneumoniae (65–100%)**
- อาการ: เหมือน **pyelonephritis รุนแรง** · **ปัสสาวะมีฟองลม (pneumaturia) และคลำได้กรอบแกรบ < 10%** · **AKI 60%** · **septic shock 19%**
- **CT KUB เป็นวิธีวินิจฉัยที่ดีที่สุด**

[[fig:gas]]

#### ทำไมถึงมีอาการนี้
| อาการ / สิ่งที่พบ | กลไก |
|---|---|
| ไข้สูง ปวดเอว อาการหนักเร็ว | เนื้อไตตายเป็นวงกว้าง ปล่อย toxin และ cytokine |
| **Pneumaturia** (< 10%) | ก๊าซใน collecting system หรือผนังกระเพาะออกมากับปัสสาวะ |
| **คลำได้กรอบแกรบ (crepitus)** ที่สีข้าง (< 10%) | ก๊าซลามออกนอกไตเข้าเนื้อเยื่อรอบไตและผนังลำตัว |
| **AKI (60%)** | เนื้อไตตาย + sepsis + อุดกั้น + เบาหวานที่มีโรคไตเดิม |
| **Septic shock (19%)** | necrotizing infection ปล่อย endotoxin |
| เกล็ดเลือดต่ำ ซึม | sepsis รุนแรง — เป็นปัจจัยพยากรณ์ไม่ดี |

#### Class และการรักษา
[[fig:epnclass]]
| Class (สไลด์) | ก๊าซอยู่ที่ | รักษาโดยทั่วไป (Huang & Tseng 2000 — ไม่อยู่ในสไลด์) |
|---|---|---|
| **I** | collecting system เท่านั้น | ยา + ระบาย/แก้การอุดกั้น |
| **II** | เนื้อไต | ยา + **percutaneous drainage (PCD)** |
| **IIIA** | ลามเข้า **perinephric space** (ระหว่างแคปซูลกับ Gerota fascia) | ยา + PCD · ถ้ามีปัจจัยเสี่ยง **≥ 2 ข้อ** (เกล็ดเลือดต่ำ AKI ซึม ช็อก) PCD มักล้มเหลว → **nephrectomy** |
| **IIIB** | ลามเลย Gerota fascia เข้า **pararenal space** | เหมือน IIIA |
| **IV** | ไตทั้งสองข้าง หรือไตข้างเดียวที่เหลือ | ยา + PCD พยายามเก็บไต |
ทุก class: ยาปฏิชีวนะครอบคลุม E. coli/Klebsiella (มักเริ่ม carbapenem) · **คุมน้ำตาลด้วย insulin** · แก้การอุดกั้น

### Xanthogranulomatous pyelonephritis (XPN) (สไลด์)
- **chronic pyelonephritis ชนิดพิเศษ** · **ข้างเดียวเกือบเสมอ** · ทำลายไตเกือบทั้งหมด · **แยกยากจากมะเร็งไต** ทั้งอาการและภาพ
- พยาธิ: neutrophil + mononuclear cell + **lipid-laden macrophage** (foam cell) เป็นลักษณะเด่น
- ใคร: **หญิงวัยกลางคน มีประวัติ UTI ซ้ำ** · **อุดกั้นจากนิ่วที่ติดเชื้อ** (อาจารย์เขียนว่า calcium stone · chronic infection)
- อาการ: ปวดเอว ไข้ อ่อนเพลีย เบื่ออาหาร **น้ำหนักลด** · **คลำได้ก้อนที่ไตข้างเดียว** · ซีด ESR สูง · UA มี pyuria และ bacteriuria
- เชื้อ: E. coli, **Proteus mirabilis**, Pseudomonas, Enterococcus faecalis, Klebsiella · **เพาะปัสสาวะไม่ขึ้น 25–40%**
- CT: ไตโต (ในสไลด์ 12.2 × 9.1 ซม.) กรวยไตและ calyx ขยายเป็นหลายช่อง ร่วมกับนิ่ว = **"bear's paw" sign**
- รักษา: ยา + **nephrectomy** เพราะไตข้างนั้นเสียแล้ว (ตำรา)
#### ทำไมถึงมีอาการนี้ (XPN)
| อาการ / สิ่งที่พบ | กลไก |
|---|---|
| ก้อนที่ไต น้ำหนักลด เหมือนมะเร็ง | การอักเสบเรื้อรังแทนที่เนื้อไตด้วยก้อน granuloma ของ foam cell |
| Foam cell | macrophage กินไขมันจากเนื้อไตที่ตายและเศษเยื่อบุ แต่ย่อยไม่หมด |
| **เพาะเชื้อไม่ขึ้น 25–40%** | ไตข้างที่ติดเชื้ออุดกั้นสนิท ปัสสาวะจากข้างนั้นไม่ลงมากระเพาะ (ที่เก็บได้มาจากไตข้างดี) · ได้ยามาก่อน |
| ซีด ESR สูง | การอักเสบเรื้อรัง (IL-6 → hepcidin → anemia of inflammation) |

### UTI และ kidney cyst infection ใน ADPKD (สไลด์ · KDIGO ADPKD 2025)
| | Cystitis/pyelonephritis ใน ADPKD | **Kidney cyst infection** |
|---|---|---|
| อาการ | แสบขัด ปัสสาวะบ่อย | **ไข้ ปวดเอว** · DDx **cyst hemorrhage, นิ่ว** |
| UA / urine culture | ผิดปกติ | **อาจปกติ** — ถุงน้ำส่วนใหญ่ไม่ต่อกับท่อไต |
- เชื้อ: **E. coli (75%)**, K. pneumoniae, Enterococcus · **เพาะปัสสาวะก่อนให้ยา**
- **ภาพ**: **US ไม่มีประโยชน์** (ถุงน้ำจำนวนมากแยกไม่ได้) · CT/MRI บอกตำแหน่งได้แต่ไม่จำเพาะ · WBC-labeled scan ผลบวก/ลบลวงได้ · **FDG-PET/CT ดีที่สุด** แต่หายาก · **เจาะดูดถุงน้ำ** เมื่อคลินิกและภาพเข้าได้แต่เพาะเลือดและปัสสาวะลบ — ยืนยันการติดเชื้อและระบายไปพร้อมกัน
- **KDIGO 2025 algorithm**: สงสัยเมื่อ **ไข้ > 38 °C + ปวดท้องเฉียบพลัน + CRP สูง (≥ 50 mg/L) หรือ WBC > 11 × 10⁹/L** → ใช้ภาพตัดแหล่งอื่น → ถ้ามีลักษณะวินิจฉัย **≥ 2 ข้อ จาก ≥ 2 หมวด** (อาการ · จุลชีววิทยา · ภาพ · การตอบสนองต่อยา) = likely cyst infection → ถ้าต้องยืนยัน ใช้ FDG PET-CT
  (ค่า CRP ในข้อความที่ดึงจากสไลด์อ่านได้เป็น "250 mg/l" — ตีความว่าเป็น ≥ 50 mg/L)
- **ยา**: ต้อง **ละลายในไขมัน (lipophilic)** — **fluoroquinolone (levofloxacin ดีกว่า ciprofloxacin), TMP/SMX** · **4–6 สัปดาห์** · ไข้ไม่ลง → **ระบายผ่านผิวหนังหรือผ่าตัด** · บางรายต้องตัดไต
#### ทำไมต้องยาละลายไขมัน และนานถึง 4–6 สัปดาห์
ถุงน้ำใน ADPKD ส่วนใหญ่ **หลุดออกจาก nephron เป็นถุงปิด** ผนังบุด้วยเซลล์ที่มี tight junction แน่น → ยาต้อง **แพร่ผ่านเยื่อหุ้มเซลล์** เข้าไป จึงต้องละลายในไขมัน · ยาที่อาศัยการกรองลงปัสสาวะ (β-lactam, aminoglycoside) ไปไม่ถึงในถุง · เชื้อในถุงปิดจำนวนมากและไม่มีการชะล้าง จึงต้องให้นาน
""",
    ["Emphysematous: DM + อุดกั้น · E. coli/Klebsiella · AKI 60% shock 19% · crepitus < 10% · CT KUB",
     "ก๊าซ = หมักน้ำตาลในเนื้อเยื่อที่น้ำตาลสูงและเลือดไปเลี้ยงน้อย",
     "Class I collecting · II เนื้อไต · IIIA perinephric · IIIB เลย fascia · IV สองข้าง/ไตเดียว",
     "XPN: หญิงวัยกลางคน UTI ซ้ำ + นิ่ว · ก้อนไตข้างเดียว · foam cell · bear's paw · เพาะไม่ขึ้น 25–40%",
     "ADPKD cyst infection: US ไม่ช่วย · FDG-PET ดีที่สุด · levofloxacin/TMP-SMX 4–6 สัปดาห์"],
    [mcq(N(27), "A 61-year-old woman with poorly controlled diabetes has severe right pyelonephritis. Non-contrast CT shows gas within the right renal parenchyma extending into the perinephric space, confined within Gerota's fascia. The left kidney is normal. According to the classification shown in the lecture, which class is this?",
         ["Class I", "Class II", "Class IIIA", "Class IIIB", "Class IV"], 2,
         "การแบ่ง class ตามตำแหน่งของก๊าซ (สไลด์ — Huang & Tseng): ก๊าซในเนื้อไตที่ **ลามเข้า perinephric space ซึ่งอยู่ระหว่างแคปซูลไตกับ Gerota fascia** = **Class IIIA**\n\n- **Class I** ก๊าซอยู่ใน collecting system เท่านั้น\n- **Class II** ก๊าซอยู่ในเนื้อไตแต่ยังไม่ออกนอกแคปซูล\n- **Class IIIB** ลามเลย Gerota fascia เข้า pararenal space\n- **Class IV** ไตทั้งสองข้างหรือไตข้างเดียวที่เหลือ — ไตซ้ายรายนี้ปกติ",
         "IIIA = perinephric (ใน Gerota) · IIIB = เลย fascia", "Emphysematous pyelonephritis classification", R("Emphysematous pyelonephritis — prognostic classification"), ["B9.2.2(2)", "2.3.14(14)", "2.3.4(1)"]),
     mcq(N(28), "A 48-year-old woman with autosomal dominant polycystic kidney disease has fever 38.9 C and left flank pain. CRP is 160 mg/L. Urine culture is negative, and MRI suggests an infected cyst in the left kidney. Which antibiotic regimen is most appropriate?",
         ["Oral amoxicillin for 7 days", "Intravenous gentamicin for 5 days", "Oral nitrofurantoin for 5 days", "Levofloxacin for 4–6 weeks", "Intravenous cefazolin for 3 days"], 3,
         "สไลด์ (KDIGO ADPKD 2025): kidney cyst infection ใช้ **ยาละลายในไขมัน — fluoroquinolone (levofloxacin ดีกว่า ciprofloxacin) หรือ TMP/SMX นาน 4–6 สัปดาห์** เพราะถุงน้ำเป็นถุงปิดที่ไม่ต่อกับท่อไต ยาต้องแพร่ผ่านผนังเซลล์เข้าไป และเชื้อในถุงไม่มีการชะล้าง · ไข้ไม่ลง → ระบายถุงน้ำ\n\n- **Amoxicillin, gentamicin, cefazolin** ละลายน้ำ ผ่านผนังถุงน้ำได้น้อย และระยะเวลาสั้นเกินไป\n- **Nitrofurantoin** อยู่แต่ในปัสสาวะ ไม่ถึงถุงน้ำ\n- urine culture ลบไม่ได้ตัด cyst infection เพราะถุงไม่ต่อกับระบบปัสสาวะ",
         "ADPKD cyst infection → levofloxacin/TMP-SMX 4–6 สัปดาห์", "Kidney cyst infection in ADPKD", R("Kidney cyst infection in ADPKD — treatment"), ["B9.2.1-3(1)", "B9.2.2(2)", "B1.7.1(1)"]),
     mcq(N(29), "A 46-year-old woman with recurrent urinary tract infections has 3 months of left flank pain, low-grade fever and 6 kg weight loss. A firm left flank mass is palpable. Haemoglobin is 9.8 g/dL and ESR 98 mm/h. CT shows an enlarged non-functioning left kidney with a central staghorn calculus and multiple dilated low-attenuation spaces arranged like a bear's paw. Nephrectomy shows sheets of lipid-laden macrophages. Which diagnosis is most likely?",
         ["Renal cell carcinoma", "Xanthogranulomatous pyelonephritis", "Genitourinary tuberculosis", "Emphysematous pyelonephritis", "Infected renal cyst in ADPKD"], 1,
         "ครบทุกข้อของ **xanthogranulomatous pyelonephritis (XPN)** ในสไลด์: หญิงวัยกลางคน **UTI ซ้ำ** · **อุดกั้นจากนิ่วติดเชื้อ** (staghorn) · ปวดเอว ไข้ **น้ำหนักลด** · **ก้อนที่ไตข้างเดียว** · ซีด ESR สูง · CT **bear's paw** · พยาธิ **lipid-laden macrophages**\n\n- **มะเร็งไต** เป็นโรคที่ต้องแยก (อาการและภาพคล้ายกัน) แต่พยาธิจะเป็นเซลล์มะเร็ง ไม่ใช่ foam cell ทั้งแผ่น\n- **GU TB** มี caseating granuloma, calyx ผิดรูป ureter ตีบ ไม่ใช่ foam cell\n- **Emphysematous** มีก๊าซและอาการเฉียบพลันรุนแรง\n- ผู้ป่วยไม่มีประวัติ ADPKD และภาพไม่ใช่ถุงน้ำหลายใบทั้งสองไต",
         "XPN: นิ่ว + ก้อนไตข้างเดียว + bear's paw + foam cell", "Xanthogranulomatous pyelonephritis", R("Xanthogranulomatous pyelonephritis"), ["B9.2.2(2)", "2.3.14(14)", "2.3.14-3(15)"]),
    ], nl=NLN + ["2.3.4(1)", "B9.2.1-3(1)", "2.3.14-3(15)", "2.2.48"], figs=F12)

# ───────────────────────────── 13
F13 = {
 "asb": fig("Asymptomatic bacteriuria — ใครรักษา ใครไม่รักษา และเพราะอะไร",
  "ASB ส่วนใหญ่ **ไม่เกิดผลเสียและไม่ได้ประโยชน์จากยา** (สไลด์) — ไม่คัดกรอง ไม่รักษา · ยกเว้น **หญิงตั้งครรภ์** (ฮอร์โมนและมดลูกทำให้ปัสสาวะคั่งในท่อไต ASB จึงกลายเป็น pyelonephritis ได้ง่าย) และ **ก่อนหัตถการทางเดินปัสสาวะที่ทำให้เยื่อบุมีเลือดออก** (เชื้อเข้ากระแสเลือดตรงจากแผล) · **ผู้รับไต**: สไลด์ให้รักษา แต่ IDSA 2019 แนะนำไม่คัดกรอง/ไม่รักษาเมื่อผ่าตัดเกิน 1 เดือน",
  svg(420, 404, "แผนผังการตัดสินใจรักษา asymptomatic bacteriuria",
      box(10, 10, 400, 40, "sk", "เชื้อ ≥ 10⁵ CFU/mL แต่ไม่มีอาการ = ASB", fs=12),
      ar(210, 50, 210, 72, "ln", "ah"),
      box(110, 74, 200, 36, "bx", "อยู่ในกลุ่มใด", fs=12),
      ar(150, 110, 73, 138, "ln", "ah"), ar(210, 110, 210, 138, "ln", "ah"), ar(270, 110, 347, 138, "ln", "ah"),
      box(10, 140, 126, 44, "ms", "ตั้งครรภ์", fs=12),
      box(147, 140, 126, 44, "ms", "ก่อนหัตถการ\nที่มีเลือดออก", fs=11.5),
      box(284, 140, 126, 44, "sk", "กลุ่มอื่นทั้งหมด", fs=12),
      ar(73, 184, 73, 204, "ln", "ah"), ar(210, 184, 210, 204, "ln", "ah"), ar(347, 184, 347, 204, "ln", "ah"),
      box(10, 206, 126, 98, "sk", "progesterone\nคลายท่อไต +\nมดลูกกด → คั่ง\n→ pyelo · คลอด\nก่อนกำหนด", fs=11),
      box(147, 206, 126, 98, "sk", "เยื่อบุฉีกขาด\n(TURP ส่องกล้อง)\n→ เชื้อเข้าเลือด\n→ sepsis\nหลังหัตถการ", fs=11),
      box(284, 206, 126, 98, "sk", "DM สูงอายุ\nคาสาย ไขสันหลัง\nยาไม่ลด pyelo\nเพิ่มเชื้อดื้อ\nC. difficile", fs=11),
      ar(73, 304, 73, 324, "ln", "ah"), ar(210, 304, 210, 324, "ln", "ah"), ar(347, 304, 347, 324, "ln", "ah"),
      box(10, 326, 126, 48, "bad", "คัดกรอง + รักษา\nเพาะซ้ำหลังรักษา", fs=11),
      box(147, 326, 126, 48, "bad", "รักษาก่อน\nหัตถการระยะสั้น", fs=11),
      box(284, 326, 126, 48, "ok", "ไม่คัดกรอง\nไม่รักษา", fs=11.5),
      t(10, 394, "ผู้รับไต: สไลด์ = รักษา · IDSA 2019 = ไม่รักษาหลัง 1 เดือน", "xs mu"))),
}
sec("neph-uti-13", "Asymptomatic bacteriuria — เมื่อไรไม่ควรให้ยา",
    "นิยาม ≥ 10⁵ ไม่มีอาการ · ไม่คัดกรอง ไม่รักษา · ยกเว้นตั้งครรภ์และก่อนหัตถการ · ผู้รับไต (สไลด์ vs IDSA 2019) · ยาในหญิงตั้งครรภ์ · pyuria ไม่ใช่ข้อบ่งชี้", 9,
"""### นิยาม (สไลด์)
**พบเชื้อ ≥ 10⁵ CFU/mL ในปัสสาวะ clean-catch โดยไม่มีอาการของ UTI** (IDSA: หญิงต้องได้เชื้อเดิม 2 ครั้งติดกัน)
- ผู้ป่วยส่วนใหญ่ **ไม่เกิดผลเสีย และไม่ได้ประโยชน์จากยาปฏิชีวนะ** (สไลด์)
- **ไม่คัดกรอง และไม่รักษาเป็นประจำ** (สไลด์)
- **Pyuria ใน ASB ไม่ใช่ข้อบ่งชี้ให้รักษา** — พบได้บ่อย เพราะร่างกายตอบสนองต่อเชื้อในปัสสาวะ แต่เชื้อไม่ได้บุกรุกเนื้อเยื่อ
- ปัสสาวะขุ่นหรือมีกลิ่น **ไม่ใช่อาการ**

[[fig:asb]]

### รักษาเฉพาะใคร
| กลุ่ม | ทำไมต้องรักษา | ที่มา |
|---|---|---|
| **หญิงตั้งครรภ์** — คัดกรองช่วงต้นของการตั้งครรภ์และรักษา | **progesterone คลายกล้ามเนื้อเรียบของท่อไต** + **มดลูกที่โตกดท่อไต** (ขวามากกว่า) → **ท่อไตขยาย ปัสสาวะคั่ง** → ASB ไต่ขึ้นเป็น pyelonephritis ได้ง่าย → คลอดก่อนกำหนด ทารกน้ำหนักน้อย · การรักษาลด pyelonephritis ได้ชัด | สไลด์ · IDSA 2019 |
| **ผู้ที่จะทำหัตถการทางเดินปัสสาวะ** ที่ทำให้เยื่อบุมีเลือดออก (TURP ส่องกล้องตัดนิ่ว) | เยื่อบุฉีกขาด → เชื้อในปัสสาวะเข้ากระแสเลือดโดยตรง → bacteremia/sepsis หลังหัตถการ · ให้ยาตามผลเพาะเชื้อ **ก่อนหัตถการระยะสั้น** | สไลด์ · IDSA 2019 |
| **ผู้รับการปลูกถ่ายไต** | สไลด์ (อ้าง Brenner & Rector 2020) ระบุว่าได้ประโยชน์ — แต่ **IDSA 2019 แนะนำไม่คัดกรองและไม่รักษา ASB ในผู้ที่ผ่าตัดมาเกิน 1 เดือน** (การศึกษาแบบสุ่มไม่พบประโยชน์) · ช่วงเดือนแรกหลังผ่าตัดยังไม่มีข้อสรุป | สไลด์ vs IDSA 2019 |
> ตอบข้อสอบในคาบนี้ตามสไลด์ แต่รู้ไว้ว่าแนวทาง IDSA 2019 ไม่แนะนำให้รักษา ASB ในผู้รับไตที่ผ่าตัดมาเกิน 1 เดือน

### ไม่รักษา
| กลุ่ม | ทำไมไม่รักษา |
|---|---|
| **เบาหวาน** | การศึกษาแบบสุ่มพบว่ายาไม่ลด symptomatic UTI pyelonephritis หรือการนอนโรงพยาบาล |
| **ผู้สูงอายุ / บ้านพักคนชรา** | ASB พบบ่อยมาก ให้ยาแล้วกลับมามีเชื้อใหม่ที่ดื้อกว่า |
| **คาสายสวน** | biofilm ทำให้กำจัดไม่ได้ ยาเลือกเชื้อดื้อ (หัวข้อ 11) |
| **บาดเจ็บไขสันหลัง** | เหมือนกัน |
| **ผู้สูงอายุที่สับสนหรือล้ม โดยไม่มีไข้หรืออาการทั้งระบบ** | หาสาเหตุอื่นของ delirium ก่อน อย่าโทษ bacteriuria (IDSA 2019) |
#### ทำไมการรักษา ASB ทำร้ายมากกว่าช่วย
- ยาคัดเลือก **เชื้อดื้อยา** และเพิ่ม **C. difficile colitis**
- เชื้อใน ASB หลายสายพันธุ์ **ก่อโรคต่ำ** (มี virulence factor น้อย) และครองพื้นที่กันไม่ให้เชื้อที่รุนแรงกว่าเข้ามา (bacterial interference) — กำจัดออกเท่ากับเปิดทางให้เชื้อใหม่

### ยาสำหรับ ASB/UTI ในหญิงตั้งครรภ์ (ไม่อยู่ในสไลด์ — แนวทางสากล)
| ใช้ได้ | เลี่ยง |
|---|---|
| amoxicillin (ถ้าไว) · amox/clav · cephalexin · cefixime · fosfomycin · nitrofurantoin (เลี่ยงช่วงใกล้คลอด) | **fluoroquinolone** · **tetracycline** (ฟันและกระดูกทารก) · **TMP/SMX ไตรมาสแรก** (ต้าน folate) **และใกล้คลอด** (kernicterus) |
ระยะเวลา **4–7 วัน** (IDSA 2019) · **เพาะเชื้อซ้ำหลังรักษา** และติดตามตลอดการตั้งครรภ์
""",
    ["ASB = ≥ 10⁵ ไม่มีอาการ → ไม่คัดกรอง ไม่รักษา",
     "รักษาเฉพาะ: หญิงตั้งครรภ์ · ก่อนหัตถการที่ทำให้เยื่อบุมีเลือดออก (สไลด์เพิ่มผู้รับไต — IDSA 2019 ไม่แนะนำหลัง 1 เดือน)",
     "Pyuria ปัสสาวะขุ่น หรือมีกลิ่น ไม่ใช่ข้อบ่งชี้รักษา ASB",
     "เบาหวาน ผู้สูงอายุ คาสายสวน ไม่รักษา ASB",
     "ตั้งครรภ์: เลี่ยง FQ tetracycline TMP/SMX (ไตรมาสแรกและใกล้คลอด) · เพาะซ้ำหลังรักษา"],
    [mcq(N(30), "A 72-year-old man is scheduled for transurethral resection of the prostate next week. He has no urinary symptoms or fever. Pre-operative urine culture grows Escherichia coli at more than 100,000 CFU/mL. What is the most appropriate management?",
         ["No treatment, because he is asymptomatic", "Culture-directed antibiotic therapy started shortly before the procedure",
          "Long-term nitrofurantoin prophylaxis for 6 months", "Cancel the procedure permanently", "Repeat the culture after surgery and treat only if fever develops"], 1,
         "สไลด์: ASB รักษาเฉพาะ **หญิงตั้งครรภ์** และ **ผู้ที่จะทำหัตถการทางเดินปัสสาวะ** — TURP ทำให้เยื่อบุฉีกขาดและมีเลือดออก เชื้อในปัสสาวะจะเข้ากระแสเลือดโดยตรงจนเกิด bacteremia/sepsis หลังผ่าตัด → ให้ **ยาตามผลเพาะเชื้อก่อนหัตถการเป็นระยะสั้น** (IDSA 2019)\n\n- \"ไม่มีอาการจึงไม่รักษา\" ใช้กับ ASB ทั่วไป แต่ไม่ใช่ก่อนหัตถการที่มีเลือดออก\n- ยาป้องกันระยะยาวไม่จำเป็น\n- ไม่ต้องยกเลิกหัตถการ เพียงรักษาก่อน\n- รอให้มีไข้หลังผ่าตัดคือปล่อยให้เกิด sepsis",
         "ASB ก่อนหัตถการที่มีเลือดออก (TURP) → รักษาก่อนหัตถการ", "ASB before urologic procedures", R("Asymptomatic bacteriuria — patients undergoing urologic intervention"), ["B9.2.2(1)", "2.3.14(7)", "2.3.14(8)"]),
     mcq(N(31), "An 84-year-old nursing-home resident with dementia has cloudy, foul-smelling urine noticed by staff. She is afebrile, eating normally, and her mental status is at baseline. Dipstick shows leucocyte esterase 2+ and nitrite positive. What is the most appropriate management?",
         ["Start oral ciprofloxacin for 7 days", "Start intravenous ceftriaxone", "No antibiotic treatment; ensure hydration and observe for genuine symptoms",
          "Single-dose fosfomycin for every positive dipstick", "Insert an indwelling urinary catheter to monitor output"], 2,
         "ไม่มีไข้ ไม่มีอาการทางปัสสาวะ ไม่มีอาการทั้งระบบ สติเท่าเดิม = **asymptomatic bacteriuria** (ร่วมกับ pyuria) ซึ่งพบบ่อยมากในผู้สูงอายุในสถานดูแล — สไลด์: **NOT routinely screening or treating ASB** · **ปัสสาวะขุ่นหรือมีกลิ่นไม่ใช่ข้อบ่งชี้** · LE และ nitrite บวกบอกแค่ว่ามี pyuria และเชื้อ ไม่ได้บอกว่าเป็น UTI\n\n- ยาปฏิชีวนะ (ciprofloxacin, ceftriaxone, fosfomycin) ไม่ลดภาวะแทรกซ้อน แต่เพิ่มเชื้อดื้อและ C. difficile\n- การใส่สายสวนเพิ่มความเสี่ยงติดเชื้อโดยไม่จำเป็น",
         "ปัสสาวะขุ่น/มีกลิ่น + dipstick บวก ไม่มีอาการ = ASB ไม่ให้ยา", "ASB in the elderly", R("Asymptomatic bacteriuria"), ["B9.2.2(1)", "2.3.14(7)", "B9.3(2)"]),
    ], nl=NLN + ["2.3.15-3(11)", "B10.1.3(3)"], figs=F13)

ORDERED_IDS = [N(17), N(27)]

# ───────────────────────────── ข้อคลัง Ward Drill (คาบ 30 ครบ 22 ข้อ + คาบ 28 สามข้อ) และ Mock
BANK_MAP = {
    "neph-uti-02": ["N-OLD-091"],
    "neph-uti-03": ["N-OLD-098", "N-OLD-100"],
    "neph-uti-04": ["N-MCQ-26", "N-OLD-074", "N-OLD-093"],
    "neph-uti-05": ["N-MCQ-34", "N-OLD-090", "N-OLD-102"],
    "neph-uti-06": ["N-OLD-104"],
    "neph-uti-07": ["N-OLD-096"],
    "neph-uti-08": ["N-MCQ-33", "N-OLD-095", "N-OLD-087"],
    "neph-uti-09": ["N-MCQ-32", "N-OLD-094"],
    "neph-uti-10": ["N-OLD-103"],
    "neph-uti-11": ["N-OLD-099", "N-OLD-101"],
    "neph-uti-12": ["N-OLD-092", "N-OLD-097"],
    "neph-uti-13": ["N-MCQ-30", "N-MCQ-31", "N-OLD-088", "N-OLD-089"],
}
MOCK_MAP = {
    "neph-uti-07": ["MOCK-019"],
    "neph-uti-11": ["MOCK-020"],
    "neph-uti-13": ["MOCK-011"],
}
NL_FIX = {   # รหัสในคลังที่ไม่มีในพจนานุกรม/เป็นรหัสหมวด → รหัสเฉพาะ
    "N-OLD-102": ["B9.2.2(2)", "2.3.1(20)", "B9.3(2)"],
    "N-OLD-092": ["B9.2.2(2)", "2.3.4(1)", "2.3.14(14)"],
    "N-OLD-097": ["2.3.14(7)", "2.3.4(1)", "B9.2.2(1)", "B1.7.1(4)"],
    "N-OLD-098": ["2.3.14(7)", "2.1.43", "B1.7.1(4)", "2.3.19(2)"],
    "N-OLD-099": ["B9.2.2(1)", "3.1.9", "2.3.14(7)", "2.3.19(5)"],
    "N-OLD-101": ["B9.2.2(1)", "2.1.43", "2.3.19(5)"],
    "N-MCQ-31": ["B9.2.2(1)", "2.3.14(7)", "2.3.4(1)"],
    "N-OLD-089": ["B9.2.2(1)", "2.3.14(7)", "2.3.4(1)"],
    "N-MCQ-30": ["B9.2.2(1)", "2.3.14(7)", "2.3.15-3(11)"],
    "N-OLD-088": ["B9.2.2(1)", "2.3.14(7)", "2.3.15-3(11)"],
    "MOCK-011": ["B9.2.2(1)", "2.3.14(7)", "2.3.15-3(11)", "2.3.1"],
    "MOCK-019": ["B9.2.2(2)", "2.3.14(14)", "B1.7.2", "2.3.1"],
    "MOCK-020": ["B9.2.2(1)", "2.3.14(7)", "2.3.19(5)", "3.1.9", "2.3.1"],
}

# ───────────────────────────── MEQ · OSCE/SAQ
LECNAME = "Urinary tract infection (อ.กรทิพย์)"
MEQ = [{"id": "NEPH-UTI-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Urosepsis from right pyelonephritis in a diabetic man progressing to emphysematous pyelonephritis",
 "vignette": """ผู้ป่วยชายไทยคู่ อายุ 55 ปี อาชีพรับจ้างก่อสร้าง ภูมิลำเนา จ.ร้อยเอ็ด (เคส 2 ของอาจารย์ — ขยายต่อ)
CC: ไข้สูง หนาวสั่น ปวดสีข้างด้านขวา 6 ชั่วโมงก่อนมาโรงพยาบาล
PI: 2 วันก่อนปัสสาวะแสบขัด ปัสสาวะบ่อย · 6 ชั่วโมงก่อนมามีไข้สูง หนาวสั่น ปวดตื้อ ๆ ที่เอวขวาตลอดเวลา คลื่นไส้ อาเจียน 3 ครั้ง กินอะไรไม่ได้ ญาติสังเกตว่าซึมลง
U/D: เบาหวานชนิดที่ 2 มา 10 ปี คุมไม่ดี (HbA1c 11%) กิน metformin และ empagliflozin · เคยเป็นนิ่วในไตขวา
PE: BT 39.6 C, PR 122/min, BP 86/50 mmHg, RR 26/min, SpO2 96% · ซึมแต่ปลุกตื่น · right CVA tenderness ชัดเจน · ไม่มี crepitus · ท้องนุ่ม
Lab: WBC 21,800/µL (N 90%), Hb 12.1 g/dL, platelet 88,000/µL · BUN 42, Cr 2.6 mg/dL (baseline 1.0) · glucose 412 mg/dL · HCO₃⁻ 16 mmol/L · lactate 4.4 mmol/L
UA: sp.gr. 1.020, glucose 4+, leukocyte esterase 3+, nitrite positive, WBC numerous/HPF, RBC 10–20/HPF, WBC cast present · Urine Gram stain: Gram-negative bacilli""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัย และบอกว่าเป็น UTI กลุ่มใดตามสไลด์ พร้อมเหตุผล (2 คะแนน)",
   "a": """**Acute pyelonephritis ข้างขวา ร่วมกับ sepsis/septic shock (urosepsis)** — ไข้สูง หนาวสั่น ปวดเอวขวา CVA tenderness · UA มี pyuria nitrite บวก **WBC cast** · ความดันต่ำ lactate 4.4 ซึม เกล็ดเลือดต่ำ ไตวายเฉียบพลัน
เป็น **complicated UTI** เพราะ **เป็นชาย + เบาหวานคุมไม่ดี** (สไลด์) และมีประวัตินิ่วในไต (เสี่ยงอุดกั้น)"""},
  {"q": "2. จงอธิบายกลไกของ (ก) ไข้สูงหนาวสั่น (ข) ปวดเอวและ CVA tenderness (ค) เหตุใด WBC cast บอกว่าการติดเชื้ออยู่ที่ไต ไม่ใช่แค่กระเพาะปัสสาวะ (3 คะแนน)",
   "a": """(ก) เชื้อเข้าเนื้อไตที่มีเลือดไหลผ่านมาก → **LPS กระตุ้น macrophage หลั่ง IL-1, IL-6, TNF-α → PGE₂ ที่ hypothalamus ตั้ง set point สูง** → กล้ามเนื้อสั่นผลิตความร้อน (rigors)
(ข) เนื้อไตอักเสบ **บวมในแคปซูลที่ยืดไม่ได้ → แคปซูลถูกยืด** → ประสาทอัตโนมัติเข้าไขสันหลังระดับ **T10–L1** → ปวดตื้อที่เอว · การเคาะส่งแรงสั่นถึงไตที่ตึงอยู่ → เจ็บ
(ค) **cast ก่อตัวได้เฉพาะในท่อไต** — Tamm-Horsfall protein จาก thick ascending limb ห่อเม็ดเลือดขาวที่อยู่ในท่อเป็นแท่ง · กระเพาะปัสสาวะไม่มีท่อและไม่มี Tamm-Horsfall จึงไม่มี cast"""},
  {"q": "3. ก่อนให้ยาปฏิชีวนะ ต้องส่งตรวจอะไร และต้องทำภาพทางรังสีอะไรเร่งด่วน เพราะเหตุใด (3 คะแนน)",
   "a": """- **Urine culture** (และ Gram stain) **ก่อนให้ยา** — ยาขับทางปัสสาวะทำให้ปัสสาวะปลอดเชื้อเร็ว · **hemoculture 2 ชุด** — ไม่ให้การเก็บตัวอย่างทำให้ยาช้าเกิน 1 ชั่วโมง
- **Ultrasound ไตข้างเตียงโดยเร็ว** — ผู้ป่วยมี **ประวัตินิ่ว + ช็อก + ไตวายเฉียบพลัน** ต้องตัด **การอุดกั้น (pyonephrosis)** ซึ่งต้องระบายด่วน ยาอย่างเดียวไม่พอ (สไลด์: suspected obstruction / renal function ลดลงจาก baseline → imaging)
- ถ้า US ไม่ชัดหรือสงสัยก๊าซ/ฝี → **CT KUB** (ไม่ฉีดสีเพราะไตวาย) — CT เป็นวิธีวินิจฉัย emphysematous pyelonephritis ที่ดีที่สุด"""},
  {"q": "4. จงเลือกยาปฏิชีวนะเริ่มต้นตามสไลด์ พร้อมเหตุผล และการรักษาประคับประคองที่สำคัญ (3 คะแนน)",
   "a": """- **Meropenem (หรือ imipenem/cilastatin) ทางหลอดเลือดดำ** — pyelonephritis **with septic shock** ตามสไลด์ · E. coli/Klebsiella สร้าง **ESBL** ได้บ่อย และการได้ยาที่เชื้อดื้อในคนช็อกเพิ่มอัตราตาย · ปรับขนาดตามการทำงานของไต
- ทางเลือกในสไลด์คือ gentamicin/amikacin แต่ **ผู้ป่วยไตวายเฉียบพลัน — เลี่ยง aminoglycoside** ถ้าเลือกได้
- **IV crystalloid 30 mL/kg** · **norepinephrine** ถ้า MAP < 65 หลังให้สารน้ำ · ติดตาม lactate และปัสสาวะ
- **หยุด metformin และ empagliflozin** (sepsis, AKI, เสี่ยง lactic acidosis และ ketoacidosis) → **คุมน้ำตาลด้วย insulin**"""},
  {"q": "5. วันที่ 3 ผู้ป่วยยังมีไข้ 39 C ทั้งที่เชื้อ Klebsiella pneumoniae ไวต่อ meropenem · CT KUB พบก๊าซในเนื้อไตขวาลามเข้า perinephric space แต่ยังอยู่ภายใน Gerota fascia ไม่มีนิ่วอุดกั้น · จงวินิจฉัย บอก class อธิบายว่าก๊าซเกิดได้อย่างไร และวางแผนการรักษา (3 คะแนน)",
   "a": """**Emphysematous pyelonephritis — Class IIIA** (ก๊าซลามเข้า perinephric space ระหว่างแคปซูลกับ Gerota fascia)
**กลไกก๊าซ**: น้ำตาลในเนื้อเยื่อสูง (เบาหวานคุมไม่ดี) + เลือดไปเลี้ยงน้อย (microangiopathy ไตบวม) → Klebsiella/E. coli **หมักน้ำตาลแบบ mixed-acid fermentation ได้ CO₂ และ H₂** ซึ่งระบายออกไม่ทัน → เนื้อไตตาย
**แผนการรักษา**: ไข้ไม่ลงใน 72 ชม. ทั้งที่เชื้อไวต่อยา = มีที่ซ่อนเชื้อ → **ยาต่อ + percutaneous drainage** · ผู้ป่วยมีปัจจัยเสี่ยง ≥ 2 ข้อ (**เกล็ดเลือดต่ำ AKI ซึม ช็อก**) → การระบายมักไม่พอ → **ปรึกษาศัลยแพทย์ยูโรวิทยาเพื่อ nephrectomy** ถ้าไม่ดีขึ้น · คุมน้ำตาลด้วย insulin · ให้ยารวมนานกว่า 10–14 วันตามการตอบสนอง"""}],
 "ref": ["สไลด์ อ.กรทิพย์ — Case 2, acute pyelonephritis with septic shock, clinical response/imaging, emphysematous pyelonephritis",
         "Huang JJ, Tseng CC. Arch Intern Med 2000;160:797–805 (การรักษาตาม class — ไม่อยู่ในสไลด์)"],
 "nl": ["B9.2.2(2)", "2.3.14(14)", "2.2.48", "2.2.7", "2.3.4(1)", "3.1.6", "B9.3(2)"],
 "years": [], "_kind": "meq", "_set": "nephro"}]

OSCE = [{"id": "NEPH-UTI-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Interpretation of urinalysis in four patients with suspected urinary tract infection",
 "station": "SAQ (แปลผลปัสสาวะ) 10 นาที",
 "instruction": """จงแปลผลปัสสาวะของผู้ป่วย 4 ราย และบอกสิ่งที่ต้องทำต่อ (รายละ 2.5 คะแนน)

A. หญิง 24 ปี แสบขัด ปัสสาวะบ่อย 2 วัน ไม่มีไข้
   LE 2+ · nitrite positive · WBC 20–30/HPF · RBC 5–10/HPF
   squamous epithelial 0–1/HPF · cast: none · bacteria: many

B. หญิง 30 ปี ไข้ 39 C ปวดเอวซ้าย เคาะ CVA เจ็บ
   LE 3+ · nitrite positive · WBC numerous/HPF · RBC 10–20/HPF
   squamous epithelial 0–1/HPF · WBC cast 2–3/LPF · bacteria: many

C. หญิง 35 ปี ตรวจสุขภาพประจำปี ไม่มีอาการ
   LE 1+ · nitrite negative · WBC 5–10/HPF · RBC 0–2/HPF
   squamous epithelial 20–30/HPF · cast: none · bacteria: mixed

D. ชาย 45 ปี ไข้กลางคืน น้ำหนักลด 1 เดือน ได้ยาปฏิชีวนะ 2 คอร์สไม่ดีขึ้น
   LE 2+ · nitrite negative · WBC 30–50/HPF · RBC 10–20/HPF
   squamous epithelial 0–1/HPF · cast: none · bacteria: not seen
   urine culture: no growth × 2""",
 "answer": """**เกณฑ์ให้คะแนน (10 คะแนน)**

| ราย | การแปลผล | สิ่งที่ต้องทำต่อ | คะแนน |
|---|---|---|---|
| **A** | **Acute simple cystitis** — pyuria (WBC ≥ 5/HPF) + LE บวก + **nitrite บวก** (เชื้อ Enterobacterales ที่มี nitrate reductase) · ตัวอย่างดี (epithelial < 5/HPF) · ไม่มี cast ไม่มีไข้ = จำกัดที่กระเพาะ | **Nitrofurantoin 5 วัน** (สไลด์) · ครั้งแรกไม่จำเป็นต้องเพาะเชื้อ · ควรดีขึ้นใน 48 ชม. | 2.5 |
| **B** | **Acute pyelonephritis** — ไข้ ปวดเอว CVA tenderness + pyuria nitrite บวก + **WBC cast = การอักเสบอยู่ในท่อไต (เนื้อไต)** | **Urine culture ก่อนยา** · ไม่มี SIRS/ช็อก → **ceftriaxone** · step-down ตามผลเพาะเชื้อ รวม 7 วัน (oral cephalosporin 10–14 วัน) · **ห้าม nitrofurantoin** | 2.5 |
| **C** | **ตัวอย่างปนเปื้อน** — squamous epithelial 20–30/HPF (เกณฑ์ตัวอย่างดี < 5/HPF) เชื้อหลายชนิด · ผู้ป่วยไม่มีอาการ | **ไม่ให้ยา** · ถ้าจำเป็นต้องตรวจ ให้เก็บใหม่แบบ clean-catch midstream (ทิ้งช่วงแรก เก็บช่วงกลาง) · แม้เพาะขึ้นก็เป็น ASB ที่ไม่ต้องรักษา | 2.5 |
| **D** | **Sterile pyuria** — WBC 30–50 แต่ไม่เห็นเชื้อ เพาะไม่ขึ้นสองครั้ง + ไข้กลางคืน น้ำหนักลด ยาไม่ช่วย → คิดถึง **genitourinary TB** ก่อน (DDx: interstitial nephritis, ได้ยามาไม่ครบ, นิ่ว, มะเร็ง) | **ปัสสาวะตอนเช้า 3 วัน ส่ง AFB + Xpert MTB/RIF + TB culture** · CXR · anti-HIV · CT urography ดู calyx และ ureter | 2.5 |

**ข้อที่ทำให้เสียคะแนน**: ให้ยาผู้ป่วย C · ใช้ nitrofurantoin ใน B · สรุปว่า D เป็น UTI ธรรมดาแล้วเปลี่ยนยาปฏิชีวนะอีก · ไม่บอกว่า WBC cast หมายถึงเนื้อไต""",
 "ref": ["สไลด์ อ.กรทิพย์ — Urinalysis (dipstick, microscopy), sterile pyuria, management of cystitis/pyelonephritis, Case 3"],
 "nl": ["3.1.6", "B9.3(1)", "B9.3(2)", "B9.2.2(1)", "B9.2.2(2)", "2.3.1(20)"],
 "years": [], "_kind": "meq", "_set": "nephro"}]

LECMETA = {
 "objectives": [
   "แยก UTI ออกจาก bacteriuria, pyuria และ asymptomatic bacteriuria และจัดผู้ป่วยเข้ากลุ่ม simple cystitis, uncomplicated pyelonephritis, complicated และ recurrent UTI",
   "อธิบายกลไกการติดเชื้อแบบไต่ขึ้น กลไกป้องกันของทางเดินปัสสาวะ และ virulence factor ของ E. coli",
   "อธิบายกลไกของอาการเด่นแต่ละอย่าง (แสบขัด ปัสสาวะบ่อย ปวดท้องน้อย ไข้ ปวดเอว CVA tenderness) และใช้แยก cystitis, pyelonephritis และโรคที่คล้ายกัน",
   "แปลผล urinalysis, urine culture และ Gram stain รวมถึงสาเหตุของ nitrite ลบลวงและ sterile pyuria",
   "เลือกยาและระยะเวลารักษา acute simple cystitis และ acute uncomplicated pyelonephritis ตามสไลด์ พร้อมเหตุผลทางเภสัชวิทยา",
   "ระบุ complicated UTI ใช้กฎ 72 ชั่วโมง และรู้ว่าเมื่อใดต้องทำภาพและระบาย",
   "ดูแล UTI ในผู้ชายและ prostatitis, recurrent UTI, catheter-associated UTI และ funguria",
   "วินิจฉัยและจัดการ emphysematous pyelonephritis, XPN, kidney cyst infection ใน ADPKD และวัณโรคทางเดินปัสสาวะ",
   "ตัดสินใจคัดกรองและรักษา asymptomatic bacteriuria ได้ถูกต้อง"],
 "nlGap": "เกณฑ์ฯ มีรหัส acute cystitis (`นล. B9.2.2(1)`, `2.3.14(7)`) acute pyelonephritis (`B9.2.2(2)`, `2.3.14(14)`) และการเก็บ/ตรวจปัสสาวะ (`B9.3(1)`, `B9.3(2)`, `3.1.6`) แต่ **ไม่มีรหัสของ asymptomatic bacteriuria, catheter-associated UTI, prostatitis, emphysematous หรือ xanthogranulomatous pyelonephritis, renal abscess และ funguria โดยตรง** (ใช้รหัสใกล้เคียง เช่น `2.3.14-3(9)` obstructive uropathy, `2.3.19(5)` อุปกรณ์การแพทย์, `2.3.1-3(7)` systemic mycoses) · สไลด์ส่วนที่เป็นภาพ (ตาราง urinalysis, urine culture, Gram stain, รูป pathogenesis, ภาพ CT/US) อ่านไม่ได้ — เนื้อหาส่วนนั้น กลไกของอาการ และหัวข้อ prostatitis จึงอิงแนวทางด้านล่างและระบุไว้ในแต่ละหัวข้อ",
 "guidelines": [
   "**แนวทางเวชปฏิบัติการรักษาโรคติดเชื้อทางเดินปัสสาวะ พ.ศ. 2568** (อาจารย์อ้างในสไลด์)",
   "**Brenner and Rector's The Kidney, 11th ed. (2020) — Chapter 36 Urinary Tract Infection in Adults** (อาจารย์อ้าง) — เกณฑ์ significant bacteriuria, กลไกของอาการ",
   "**Comprehensive Clinical Nephrology, 6th ed. (2019) — Section X Infectious Disease and Kidney** (อาจารย์อ้าง)",
   "**KDIGO 2025 Clinical Practice Guideline for Autosomal Dominant Polycystic Kidney Disease** — kidney cyst infection (อาจารย์อ้าง)",
   "**IDSA/ESCMID International Clinical Practice Guidelines for Acute Uncomplicated Cystitis and Pyelonephritis in Women (Clin Infect Dis 2011)** — เกณฑ์ culture ในหญิงที่มีอาการ ยาตามตำแหน่งการติดเชื้อ",
   "**IDSA 2019 Clinical Practice Guideline for the Management of Asymptomatic Bacteriuria** — กลุ่มที่คัดกรอง/รักษา ผู้รับไต หญิงตั้งครรภ์ 4–7 วัน",
   "**IDSA 2009 International Clinical Practice Guidelines for Catheter-Associated Urinary Tract Infection (Clin Infect Dis 2010)** — เกณฑ์ ≥ 10³ CFU/mL เปลี่ยนสายก่อนเก็บปัสสาวะ bacteriuria 3–7% ต่อวัน",
   "**IDSA 2016 Clinical Practice Guideline for the Management of Candidiasis** — candiduria",
   "**IDSA 2025 Guidelines on the Management of Complicated Urinary Tract Infections** — ประกอบหลักการเลือกยาตามความรุนแรงและความเสี่ยงเชื้อดื้อ",
   "**EAU Guidelines on Urological Infections 2025** — acute/chronic bacterial prostatitis, recurrent UTI",
   "**AUA/CUA/SUFU Guideline on Recurrent Uncomplicated UTI in Women (2019, amended 2022)** — การป้องกันด้วยยา",
   "**Huang JJ, Tseng CC. Emphysematous pyelonephritis: clinicoradiological classification, management, prognosis, and pathogenesis. Arch Intern Med 2000;160:797–805**",
   "**American Geriatrics Society Beers Criteria 2023** — เลี่ยง nitrofurantoin เมื่อ CrCl < 30 mL/min"],
}

# ═══════════════════════════════════════════ TAIL (MEQ/OSCE · เขียนไฟล์ · ผูกคลัง)
MEQ = globals().get("MEQ", [])
OSCE = globals().get("OSCE", [])
LECTURE = {
 "lec": LEC, "date": "ศ. 18 ก.ย.",
 "title": "Urinary tract infection",
 "subtitle": "นิยามและการแบ่งกลุ่ม · เชื้อไต่ขึ้นและ virulence ของ E. coli · ทำไมแต่ละอาการเกิด · urinalysis · culture และ sterile pyuria · cystitis · pyelonephritis · complicated UTI และกฎ 72 ชั่วโมง · ชายและต่อมลูกหมาก · recurrent UTI · CAUTI และ funguria · emphysematous, XPN, ถุงน้ำติดเชื้อใน ADPKD · asymptomatic bacteriuria",
 "objectives": [],
 "sections": S, "meq": MEQ, "osce": OSCE,
}
LECTURE.update(globals().get("LECMETA", {}))

# กระจายตำแหน่งคำตอบของข้อใหม่ (ข้อที่ตัวเลือกเรียงตามธรรมชาติไม่สลับ) — ทำก่อน publish ครั้งแรกเท่านั้น
ORDERED = set(globals().get("ORDERED_IDS", []))
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED or not it["id"].startswith("NEPH-UTI-MCQ"):
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "nephro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

secids = {s["id"] for s in S}
BANK_MAP = {k: v for k, v in globals().get("BANK_MAP", {}).items() if k in secids}
MOCK_MAP = {k: v for k, v in globals().get("MOCK_MAP", {}).items() if k in secids}
added = link("nephro", LEC, BANK_MAP, meq=globals().get("BANK_MEQ", []), osce=globals().get("BANK_OSCE", []))
addm = link_mock("nephro", LEC, MOCK_MAP)

# ปรับรหัส นล. ของข้อคลังในคาบนี้ (คลังมีรหัสเก่าที่ไม่มีในพจนานุกรม · mock มีแค่รหัสหมวด)
data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
NL_FIX = globals().get("NL_FIX", {})
for s in L["sections"]:
    for it in s["items"]:
        if it["id"] in NL_FIX:
            it["nl"] = NL_FIX[it["id"]]

seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s in L["sections"] for c in s["nl"]} | {c for s in L["sections"] for i in s["items"] for c in i["nl"]}
         | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in L["sections"]:
    assert "```" not in s["md"], s["id"]

data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "nephro": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
nnew = sum(1 for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-UTI-MCQ"))
print("sections %d | ข้อใหม่ %d + คลัง %d + mock %d = %d | meq %d | osce %d | nl %d | figs %d" % (
    len(S), nnew, added, addm, sum(len(s["items"]) for s in L["sections"]), len(L["meq"]), len(L["osce"]), len(codes),
    sum(len(s.get("figs") or {}) for s in S)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for s in S for i in s["items"] if i["id"].startswith("NEPH-UTI-MCQ")).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
