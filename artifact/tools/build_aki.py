#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Acute kidney injury (พญ.วรรณิยา มีนุ่น · Wanniya Meenune, MD · งานโรคไต รพ.ราชวิถี) → data/nephro.json คาบ "42"
(คาบ Ward Drill 42 "Acute kidney injury") · ศ. 30 ต.ค. 2569
ต้นฉบับ: "AKI year 4 update 2569.pdf" (73 หน้า · ลายมือผู้ใช้จดในห้อง) · โน้ต slides/aki_notes.md
ภาพจริงจากสไลด์: extract_aki.py → artifact/img/nephro/aki-*.jpg (section.imgs + [[img:key]])
ภาพนิ่ง SVG: figs_nephro_aki.py (section.figs) · ภาพเคลื่อนไหว + หลักจำ: anims_nephro_aki.py
สไลด์ใช้ RIFLE ไม่มี KDIGO, ไม่มีการป้องกัน contrast AKI, HRS/cardiorenal, FEurea, ระยะของ ATN, การรักษา AIN/TTP/rhabdo
→ อิงแนวทาง: KDIGO AKI 2012 · ACR–NKF contrast 2020 · EASL 2018 (HRS) · ISTH 2020 (TTP) และตำรา (ระบุในบทเรียน)"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(REPO, "dashboard"))
from link_bank import link
from patch_learn_anim import _insert_marker
import figs_nephro_aki as F
import anims_nephro_aki as AN
from extract_aki import SPEC as IMGSPEC

SET, LEC = "nephro", "42"
LECNAME = "Acute kidney injury (อ.วรรณิยา)"
SRC = "สไลด์ อ.วรรณิยา — Acute kidney injury (73 หน้า)"
SRC_ADD = "สไลด์ อ.วรรณิยา + แนวทาง/ตำรา (บางส่วนไม่อยู่ในสไลด์)"
CREDIT = "ภาพจากสไลด์ AKI — พญ.วรรณิยา มีนุ่น · รพ.ราชวิถี"
FILES = {int(n[4:6]): n for n, _, _ in IMGSPEC}
S = []

# รหัส นล.
AKI, AKI_B, ANUR, OLIG, OLIG_B, POLY = "2.3.14(3)", "B9.2.7(1)", "2.2.28", "2.1.44", "B9.2.5(1)", "2.1.42"
HEMAT, UA, UA_B, RFT, OSM = "2.1.43", "3.1.6", "B9.3(2)", "B9.3(4)", "B9.3(3)"
LYTE, LYTE_B, HYPERK, ABG, DRUGFL = "2.3.4(2)", "B9.2.5(2)", "2.2.15", "3.3.17", "B9.4(2)"
GFRH, RENH = "B9.1.2(2)", "B9.1.2(4)"
SHOCK, SEPSIS, HF, CIRR = "2.2.7", "2.2.48", "2.3.9(5)", "2.3.11(4)"
ADR, PK = "2.3.19(2)", "B1.7.1(3)"
AGN, AIN, OBST, BPH, STONE = "2.3.14(2)", "2.3.14-3(8)", "2.3.14-3(9)", "2.3.14(8)", "2.3.14-3(15)"
MHT, SSC, HEMO, HEMO_B, HCRISIS, LEPTO = "2.2.4", "2.3.12-3(13)", "2.3.3-3(6)", "B2.2.5-3(1)", "2.2.18", "2.3.1(13)"
ECG, ECG_B, MYO = "3.1.12", "B7.3(3)", "2.3.13-3(7)"
BASE = [AKI, AKI_B]


def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, imgs=None, src=SRC):
    s = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
         "nl": nl, "md": md, "pearls": pearls, "items": items}
    if figs:
        s["figs"] = figs
    if imgs:
        s["imgs"] = imgs
    S.append(s)


def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl, keep=False):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5, iid
    d = {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
         "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
    if keep:
        d["_keep"] = True
    return d


def IM(n, title, alt, cap=None, q=None, quiz=None):
    """ภาพจริงจากสไลด์ · key = i<NN> · cap = คำอธิบาย หรือ q + quiz = ให้ลองอ่านก่อนแล้วกดดูเฉลย (ทุกภาพ quiz ต้องมี q ของตัวเอง)"""
    d = {"src": "img/nephro/%s.jpg" % FILES[n], "title": title, "alt": alt, "credit": CREDIT}
    if quiz:
        assert q, n
        d["q"] = q
        d["quiz"] = quiz
    else:
        d["cap"] = cap
    return "i%02d" % n, d


def IMGS(*xs):
    return dict(xs)


N = lambda n: "NEPH-AKI-MCQ-%02d" % n
R = lambda p, *g: ["สไลด์ อ.วรรณิยา — " + p] + list(g)
KDIGO = "KDIGO Clinical Practice Guideline for Acute Kidney Injury 2012"

# ═════════════════════════════════════════════ 1
sec("nephro-aki-01", "AKI คืออะไร — ไตทำอะไร และทำไม AKI ถึงอันตราย",
    "ไต 4 หน้าที่: ขับของเสีย · รักษาสมดุลน้ำ เกลือแร่ กรด-ด่าง · คุมความดัน · สร้างฮอร์โมน · AKI พบ 0.75–5% ของผู้ป่วยใน 7–15% ของ ICU ตาย 30–80%", 6,
"""### โครงของคาบ (สไลด์)
อ.วรรณิยาเปิดด้วยคำถามง่าย ๆ ว่า **ไตทำอะไร** แล้วไล่ว่าเมื่อไตวายจะเสียอะไร → นิยามและระดับความรุนแรง (RIFLE) → **สาเหตุ 3 กลุ่ม** pre-renal · intrinsic (vascular, GN, AIN, ATN) · post-renal โดยถามทุกกลุ่มว่า **\"UA หน้าตาแบบใด\"** → **4 ขั้นของการวินิจฉัย** (ไตวายจริงไหม · AKI หรือ CKD · ตัด post-renal · ประเมิน intrinsic ด้วยดัชนีปัสสาวะ) → ภาพรังสี → **ภาวะแทรกซ้อน** (hyperkalemia เป็นหลัก) → **ข้อบ่งชี้ dialysis**

> สไลด์ใช้เกณฑ์ **RIFLE** และไม่ได้สอน KDIGO, การป้องกัน contrast AKI, hepatorenal/cardiorenal, FEurea, ระยะของ ATN และการรักษาเฉพาะโรค (TTP, AIN, rhabdomyolysis) — บทเรียนเติมจาก **KDIGO 2012** และแนวทางที่ระบุไว้ในแต่ละหัวข้อ เพื่อให้ตอบข้อสอบ Ward Drill ของคาบนี้ได้ครบ

### ไตทำอะไร (สไลด์ p3)
| หน้าที่ | รายละเอียด |
|---|---|
| **Homeostasis** | สมดุลน้ำและเกลือแร่ · กรด-ด่าง |
| **Excrete waste product** | urea, creatinine, กรดที่ไม่ระเหย, ยา |
| **Control BP** | renin–angiotensin, การขับ Na และน้ำ |
| **Synthesis** | erythropoietin · vitamin D (1α-hydroxylation) |

### เมื่อไตวาย (สไลด์ p4)
- **Waste products secretion abnormality** → Scr สูง GFR ต่ำ
- **Regulation failure** → น้ำ และ electrolyte ผิดปกติ
- **Synthesis failure** → ซีด และ osteodystrophy

[[fig:func]]

#### ทำไมถึงมีอาการนี้
| สิ่งที่พบใน AKI | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **BUN/Cr สูง** | GFR ลด สารที่ขับทางการกรองคั่ง | Cr ขึ้นช้ากว่าการบาดเจ็บ (หัวข้อ 2) · BUN ขึ้นจากเหตุนอกไตได้ (หัวข้อ 14) |
| **บวม น้ำท่วมปอด** | ขับ Na และน้ำไม่ได้ ขณะที่ยังได้น้ำเกลือ/อาหาร | น้ำเกินที่ไม่ตอบสนองต่อ diuretic = ข้อบ่งชี้ dialysis |
| **K สูง** | ไตขับ K ราว 90% ของที่กินเข้าไป · กรดดัน K ออกจากเซลล์ · เซลล์ตาย (rhabdo, TLS) | อันตรายถึงชีวิตเร็วที่สุด → ตรวจ ECG ทุกราย |
| **Metabolic acidosis (AG สูง)** | ขับกรดที่ไม่ระเหยไม่ได้ (sulfate, phosphate, urate) และสร้าง HCO3 ใหม่ไม่ได้ | AG สูงจาก uremia มักไม่เกิน ~20 ถ้าสูงมากหาสาเหตุอื่น (lactate, ketone, สารพิษ) |
| **ซีด กระดูกผิดปกติ** | ขาด EPO และ calcitriol — ใช้เวลาเป็นเดือน | ถ้าเจอตั้งแต่แรก ชวนคิด **CKD** มากกว่า AKI |

### Impact of AKI (สไลด์ p5)
- พบ **0.75–5% ของผู้ป่วยใน** และ **7–15% ของผู้ป่วย ICU**
- **อัตราตาย ~30–80%** (สูงสุดใน ICU ที่ต้องฟอกเลือด) — ผู้รอดชีวิตเสี่ยงเป็น CKD และกลับมา AKI ซ้ำ
- เหตุผลที่ KDIGO นับแม้ **Cr ขึ้นเพียง 0.3 mg/dL**: การศึกษาพบว่าการเพิ่มขึ้นเล็กน้อยก็สัมพันธ์กับอัตราตายที่สูงขึ้นแล้ว (ข้อมูลจากแนวทาง ไม่อยู่ในสไลด์)
""",
    ["ไต 4 หน้าที่: ขับของเสีย · รักษาสมดุล (น้ำ เกลือแร่ กรด-ด่าง) · คุมความดัน · สร้าง EPO/vitamin D",
     "AKI ฆ่าผู้ป่วยผ่าน regulation failure: น้ำเกิน K สูง และกรด — ไม่ใช่ BUN ที่สูง",
     "ซีด/กระดูกผิดปกติตั้งแต่แรก = เบาะแสของ CKD",
     "AKI พบ 7–15% ของผู้ป่วย ICU อัตราตาย 30–80%"],
    [mcq(N(1), "A 66-year-old man is admitted with septic shock. On day 3 his creatinine has risen from 1.0 to 3.4 mg/dL and his urine output is 200 mL/day. Which of the following abnormalities is the most immediate threat to his life and reflects failure of the kidney's regulatory (homeostatic) function?",
         ["Serum potassium 7.1 mEq/L with peaked T waves", "Blood urea nitrogen 68 mg/dL", "Haemoglobin 10.8 g/dL", "Serum 25-hydroxyvitamin D at the lower limit of normal", "Serum creatinine 3.4 mg/dL"], 0,
         "สไลด์ p4 แบ่งผลของไตวายเป็น **waste product abnormality** (BUN, Cr) · **regulation failure** (น้ำ, electrolyte) · **synthesis failure** (ซีด, osteodystrophy)\n\n**K 7.1 + peaked T** เป็น regulation failure ที่ทำให้หัวใจหยุดเต้นได้ภายในนาที → ต้องรักษาก่อนสิ่งอื่น\n\n- **BUN และ Cr** เป็นตัวบอกการขับของเสีย ตัวมันเองไม่ได้ฆ่าผู้ป่วยในระยะสั้น\n- **Hb 10.8** ใน sepsis 3 วันมาจากการอักเสบ/เจาะเลือด — การขาด EPO ต้องใช้เวลานาน\n- **25-OH vitamin D** สร้างที่ตับ ไม่ใช่ไต (ไตทำ 1α-hydroxylation) และไม่ใช่ภาวะเร่งด่วน",
         "ใน AKI ภัยเร่งด่วน = K สูง น้ำเกิน กรด", "Kidney functions", R("Kidney function, Renal failure"), BASE + [HYPERK]),
     mcq(N(2), "A 58-year-old woman is found to have a creatinine of 4.6 mg/dL during an emergency visit for vomiting. She has no prior laboratory results. Which additional finding would most strongly suggest that her kidney disease has been present for months rather than days?",
         ["Normocytic anaemia with haemoglobin 8.2 g/dL and high parathyroid hormone", "Serum potassium 5.6 mEq/L", "Urine output of 300 mL/day", "Anion gap metabolic acidosis with bicarbonate 17 mEq/L", "Blood urea nitrogen to creatinine ratio of 15"], 0,
         "หน้าที่ **สร้างฮอร์โมน** (EPO, calcitriol) เสียแล้วต้องใช้เวลาเป็นเดือนกว่าจะเห็นผล → **ซีด normocytic + PTH สูง** (secondary hyperparathyroidism จาก calcitriol ต่ำ/PO4 คั่ง) เป็นเบาะแสของ **CKD**\n\n- K สูง, oliguria, acidosis และ BUN/Cr ratio เกิดได้ทั้ง AKI และ CKD ไม่ช่วยบอกระยะเวลา\n\nหลักฐานที่ดีกว่านี้อีกคือ **Cr เดิม** และ **ultrasound ไตเล็ก** (หัวข้อ 14)",
         "ซีด + PTH สูง + ไตเล็ก → เรื้อรัง", "AKI vs CKD clue", R("Renal failure"), BASE + ["B9.2.7(2)"]),
    ], BASE + [LYTE], figs={"func": F.func_fail()})

# ═════════════════════════════════════════════ 2
sec("nephro-aki-02", "นิยามและระดับความรุนแรง — RIFLE (สไลด์) และ KDIGO 2012",
    "RIFLE: Risk Cr×1.5 · Injury ×2 · Failure ×3 · Loss > 4 สัปดาห์ · ESKD > 3 เดือน · KDIGO: Cr ↑ ≥0.3 ใน 48 ชม. หรือ ×1.5 ใน 7 วัน หรือ UO < 0.5 × 6 ชม. · Cr มาช้า · ✍️ UO คิดต่อ ideal weight", 9,
"""### RIFLE criteria (สไลด์ p6)
| Category | GFR criteria | Urine output criteria |
|---|---|---|
| **Risk** | Cr ×1.5 หรือ GFR ลด > 25% | UO < 0.5 mL/kg/h × 6 ชม. |
| **Injury** | Cr ×2 หรือ GFR ลด > 50% | UO < 0.5 mL/kg/h × 12 ชม. |
| **Failure** | Cr ×3 หรือ GFR ลด > 75% | UO < 0.3 mL/kg/h × 24 ชม. หรือ anuria × 12 ชม. |
| **Loss** | persistent ARF = complete loss of kidney function > 4 สัปดาห์ | |
| **ESRD** | end-stage kidney disease > 3 เดือน | |

สไลด์บอกว่าระดับ **Risk = high sensitivity** (จับได้เร็วแต่ผลบวกลวงมาก) · **Failure = high specificity** (ถ้าถึงระดับนี้ AKI จริงแน่)

### KDIGO 2012 — นิยามที่ใช้ปัจจุบัน (ไม่อยู่ในสไลด์)
AKI คือมีข้อใดข้อหนึ่ง
- **Cr เพิ่ม ≥ 0.3 mg/dL ภายใน 48 ชม.** หรือ
- **Cr ≥ 1.5 เท่าของ baseline** ที่รู้หรือสันนิษฐานว่าเกิดภายใน 7 วัน หรือ
- **ปัสสาวะ < 0.5 mL/kg/h นาน 6 ชม.**

| Stage | Creatinine | Urine output |
|---|---|---|
| **1** | 1.5–1.9 เท่า หรือเพิ่ม ≥ 0.3 mg/dL | < 0.5 mL/kg/h 6–12 ชม. |
| **2** | 2.0–2.9 เท่า | < 0.5 mL/kg/h ≥ 12 ชม. |
| **3** | ≥ 3 เท่า หรือ Cr ≥ 4.0 mg/dL หรือเริ่ม RRT | < 0.3 mL/kg/h ≥ 24 ชม. หรือ anuria ≥ 12 ชม. |

- จัด stage ตาม **เกณฑ์ที่รุนแรงกว่า** ระหว่าง Cr กับ UO และใช้ **ค่าที่แย่ที่สุด**
- ภาวะที่เกิน 7 วันแต่ไม่ถึง 90 วัน KDIGO เรียก **acute kidney disease (AKD)** · เกิน 90 วัน = CKD (สไลด์ใช้ Loss > 4 สัปดาห์ และ ESRD > 3 เดือน)

[[fig:rifle]]

### ข้อจำกัดของ creatinine
✍️ ลายมือในสไลด์ RIFLE บอก 3 เรื่องที่อาจารย์พูดในห้อง
- **Cr ต่ำในผู้สูงอายุ** เพราะกล้ามเนื้อน้อย (↓ muscle mass) และใน **ผู้ขาดอาหาร** → Cr \"ปกติ\" อาจซ่อน GFR ที่ต่ำ → ✍️ ใช้ **serum cystatin C + Cr** ช่วยประเมิน
- ✍️ **urine biomarker** ช่วยวินิจฉัย AKI ได้เร็วกว่า Cr (เช่น NGAL, TIMP-2·IGFBP7 — ชื่อสารอิงตำรา)
- ✍️ คิด urine output ต่อ **ideal body weight ≈ ส่วนสูง (ซม.) − 100** ไม่ใช่น้ำหนักจริงที่อาจบวมน้ำหรืออ้วน
- Cr เป็นสัญญาณที่ **มาช้า**: GFR ตกทันทีที่ไตบาดเจ็บ แต่ Cr ต้องสะสมหลายวันกว่าจะถึงค่าคงที่ใหม่ (✍️ วงที่ GFR พร้อมเขียน \"4 hr\" — ปัสสาวะเปลี่ยนเร็วระดับชั่วโมง ส่วน Cr ช้าระดับวัน)

#### ทำไมถึงมีอาการนี้
| สิ่งที่เห็น | กลไก | ใช้อย่างไร |
|---|---|---|
| **วันแรกที่ความดันตก Cr ยังปกติ** | creatinine สะสมทีละวัน ยังไม่ถึง steady state | ติดตาม Cr ทุกวัน · อย่าบอกว่า \"ไตยังดี\" จาก Cr ค่าเดียว |
| **Cr ขึ้นจาก 0.4 เป็น 0.8 ในหญิงชราผอม** | ฐานต่ำเพราะสร้างน้อย การเพิ่ม 2 เท่าคือ GFR หายไปครึ่งหนึ่ง | ตีความเป็น **stage 2** ไม่ใช่ \"Cr ยังปกติ\" |
| **ผู้ป่วยบวมน้ำ 20 กก. ปัสสาวะ \"พอ\" ต่อ kg** | หารด้วยน้ำหนักจริงที่รวมน้ำ ทำให้ mL/kg/h ต่ำเกินจริงหรือหลอก | ใช้ ideal body weight |
""",
    ["KDIGO: Cr ↑ ≥ 0.3 mg/dL ใน 48 ชม. · ≥ 1.5 เท่าใน 7 วัน · UO < 0.5 mL/kg/h × 6 ชม.",
     "Stage 1 = 1.5–1.9× · Stage 2 = 2.0–2.9× · Stage 3 = ≥ 3×, Cr ≥ 4.0 หรือเริ่ม RRT",
     "RIFLE (สไลด์): Risk sensitive · Failure specific · Loss > 4 สัปดาห์ · ESRD > 3 เดือน",
     "Cr มาช้าและต่ำหลอกในผู้สูงอายุ/ขาดอาหาร → ✍️ cystatin C, biomarker",
     "✍️ UO คิดต่อ ideal body weight ≈ ส่วนสูง − 100"],
    [mcq(N(3), "A 70-year-old man, height 165 cm, undergoes emergency laparotomy. His baseline creatinine 1 month ago was 0.9 mg/dL. Thirty-six hours after surgery his creatinine is 2.0 mg/dL, and his urine output has been 30 mL/h for the past 8 hours. Using KDIGO criteria (urine output calculated on ideal body weight of about 65 kg), what is his AKI stage?",
         ["Stage 1", "Stage 2", "Stage 3", "No AKI, because urine output is above 0.3 mL/kg/h", "RIFLE Loss"], 1,
         "**Creatinine:** 2.0 ÷ 0.9 = **2.2 เท่า** → อยู่ในช่วง 2.0–2.9 = **stage 2**\n\n**Urine output:** ✍️ ideal body weight ≈ 165 − 100 = 65 kg · 30 ÷ 65 = **0.46 mL/kg/h** นาน 8 ชม. → < 0.5 นาน 6–12 ชม. = เกณฑ์ stage 1\n\n**ใช้เกณฑ์ที่รุนแรงกว่า → stage 2**\n\n- \"No AKI\" ผิด: เกณฑ์ < 0.3 เป็นของ stage 3 เท่านั้น ส่วน < 0.5 × 6 ชม. ก็เป็น AKI แล้ว\n- Loss ต้องเป็น > 4 สัปดาห์",
         "จัด stage ด้วยเกณฑ์ที่แย่กว่าระหว่าง Cr กับ UO", "KDIGO staging", R("RIFLE criteria", KDIGO), BASE + [OLIG], keep=True),
     mcq(N(4), "An 84-year-old bedridden woman weighing 36 kg is treated with intravenous vancomycin for MRSA osteomyelitis. Her serum creatinine is 0.7 mg/dL and her creatinine-based eGFR is reported as 78 mL/min/1.73 m². Which statement best explains why this result may be misleading?",
         ["Low muscle mass reduces creatinine generation, so creatinine-based eGFR overestimates her true GFR; cystatin C or measured clearance is more reliable", "Vancomycin interferes with the laboratory assay and falsely lowers creatinine", "Elderly patients secrete less creatinine in the tubules, so serum creatinine is falsely high", "Creatinine-based eGFR underestimates GFR in all patients over 80 years", "Creatinine is extensively reabsorbed in the tubule when muscle mass is low"], 0,
         "✍️ อาจารย์: **Cr ต่ำในผู้สูงอายุเพราะกล้ามเนื้อน้อย** และในผู้ขาดอาหาร → Cr 0.7 ไม่ได้แปลว่าไตดี เพราะ **สร้าง creatinine น้อย** · สมการ eGFR สมมติมวลกล้ามเนื้อเฉลี่ย จึง **ประเมิน GFR สูงเกินจริง** → ยาที่ขับทางไต (vancomycin) อาจเกินขนาด\n\n✍️ ใช้ **serum cystatin C ร่วมกับ Cr** (cystatin C สร้างจากทุกเซลล์ ไม่ขึ้นกับกล้ามเนื้อ) หรือวัด creatinine clearance จากปัสสาวะ 24 ชม. และติดตามระดับยา\n\n- vancomycin ไม่รบกวนการวัด Cr\n- การหลั่ง Cr ที่ท่อไตลดจะทำให้ Cr **สูง** ไม่ใช่ต่ำ และ Cr แทบไม่ถูกดูดกลับ",
         "ผอม แก่ ขาดอาหาร: Cr ต่ำหลอก → cystatin C", "Creatinine limitation", R("RIFLE criteria (ลายมือ)", KDIGO), BASE + [RFT, PK]),
    ], BASE + [RFT, OLIG], figs={"rifle": F.rifle_kdigo()})

# ═════════════════════════════════════════════ 3
sec("nephro-aki-03", "สาเหตุ 3 กลุ่ม — pre-renal · intrinsic · post-renal",
    "Pre-renal = เลือดไปไตไม่พอ (กลับคืนได้) · Intrinsic 4 กลุ่ม: vascular · GN · AIN · ATN · Post-renal = อุดทั้งสองข้าง · ตัด pre/post ที่แก้ง่ายก่อน", 6,
"""### สามตำแหน่งที่ทำให้ปัสสาวะไม่ออก
การทำปัสสาวะต้องมี **เลือดไปไตพอ → เนื้อไตทำงาน → ทางระบายไม่อุด** ความผิดปกติที่จุดใดจุดหนึ่งคือกลุ่มสาเหตุหนึ่ง

| กลุ่ม | ปัญหา | ตัวอย่าง (สไลด์) | UA ทั่วไป |
|---|---|---|---|
| **Pre-renal** (p7) | renal blood flow ลด → GFR ลด · เนื้อไตปกติ | ขาดน้ำ HF sepsis NSAID hepatorenal | **bland** |
| **Intrinsic** (p12) | เนื้อไตเสีย 4 กลุ่ม | **vascular · acute GN · AIN · ATN** | ตามกลุ่ม |
| **Post-renal** (p35, p41) | ทางเดินปัสสาวะอุด | BPH stricture นิ่ว มะเร็ง · ผลึกในท่อไต | **bland** |

- **Pre-renal**: \"if identified and treated, usually reversible\" — ถ้าปล่อยนานกลายเป็น **ischemic ATN** (สไลด์ p28: renal ischemia = prolonged pre-renal)
- **Post-renal**: ต้องอุด **ทั้งสองข้าง** (หรือข้างเดียวในคนที่มีไตทำงานข้างเดียว) เพราะไตอีกข้างชดเชยได้
- อ.วรรณิยาจัด **การตกผลึกในท่อไต** (uric acid, ยา) ไว้ในหัวข้อ \"intrinsic renal: intrarenal obstruction (post-renal AKI)\" — บทเรียนแยกเป็นหัวข้อ 12

[[fig:sediment]]

#### ทำไมถึงมีอาการนี้
| ลักษณะ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Cr ลดลงเร็วหลังให้น้ำ (24–72 ชม.)** | เนื้อไตยังดี เมื่อเลือดกลับมา GFR กลับทันที | ยืนยัน pre-renal ย้อนหลัง |
| **Cr ไม่ลดแม้ให้น้ำพอ + granular cast** | เซลล์ท่อไตตายแล้ว ต้องรอสร้างใหม่ | pre-renal กลายเป็น ATN |
| **ปัสสาวะไม่ออกเลย (anuria)** | มักเกิดจากอุดตันทั้งหมด หรือหลอดเลือดอุดสองข้าง/cortical necrosis/RPGN รุนแรง | anuria → คิด **post-renal ก่อน** ใส่สาย/ultrasound ทันที |
| **UA bland ทั้งที่ GFR ตกมาก** | ไม่มีการอักเสบหรือเลือดออกในเนื้อไต | pre-renal, post-renal, vascular, crystal (ไม่ใช่ GN/AIN) |
""",
    ["Pre-renal = เลือดไปไตไม่พอ · intrinsic = vascular / GN / AIN / ATN · post-renal = อุดทั้งสองข้าง",
     "Pre-renal ที่ปล่อยนาน → ischemic ATN",
     "Anuria → คิด post-renal ก่อน ใส่สาย/ultrasound ทันที",
     "UA bland: pre-renal, post-renal, vascular, crystal"],
    [mcq(N(5), "A 79-year-old woman is admitted with 3 days of vomiting. Her creatinine is 2.6 mg/dL (baseline 0.9). She receives intravenous isotonic saline and her blood pressure and jugular venous pressure normalise within 12 hours. After 72 hours of adequate volume repletion, her creatinine is 3.4 mg/dL, urine output is 400 mL/day and the urine sediment shows many muddy brown granular casts. Which of the following best explains the course?",
         ["Prolonged renal hypoperfusion has progressed to ischaemic acute tubular necrosis", "She still has pre-renal azotaemia and needs another 3 litres of saline", "She has developed acute interstitial nephritis from the saline", "A post-renal cause is excluded because she is passing urine", "Creatinine rise after fluids indicates rapidly progressive glomerulonephritis"], 0,
         "pre-renal ที่แท้จริงต้อง **ดีขึ้นภายใน 24–72 ชม.** หลังแก้ volume เพราะเนื้อไตยังดี · ในรายนี้ Cr ยังขึ้นและมี **muddy brown granular cast** = เซลล์ท่อไตตายแล้ว → **ischemic ATN** (สไลด์ p28: renal ischemia = prolonged pre-renal)\n\n- ให้น้ำเพิ่มเมื่อ volume ปกติแล้วจะทำให้ **น้ำเกิน** (ATN ขับน้ำไม่ได้)\n- น้ำเกลือไม่ทำให้เกิด AIN\n- ปัสสาวะยังออกไม่ได้ตัด post-renal (อุดบางส่วนก็มีปัสสาวะได้) แต่ cast บอก ATN แล้ว\n- RPGN ต้องมี dysmorphic RBC/RBC cast",
         "ให้น้ำพอแล้ว Cr ไม่ลง + granular cast = ATN", "Pre-renal to ATN", R("Cause of ARF, ATN"), BASE + [UA]),
     mcq(N(6), "A 35-year-old man with two normally functioning kidneys presents with left renal colic. CT shows an 8-mm stone in the left mid-ureter with moderate left hydronephrosis. His creatinine is 0.9 mg/dL (baseline 0.8). Why is his creatinine nearly normal?",
         ["The unobstructed right kidney maintains total GFR; post-renal AKI requires bilateral obstruction or obstruction of a single functioning kidney", "Ureteric stones never reduce glomerular filtration in the affected kidney", "Creatinine is secreted into the ureter above the stone", "Hydronephrosis increases renal blood flow and filtration", "Pain-induced catecholamine release increases GFR in the obstructed kidney"], 0,
         "ไตข้างที่อุด GFR ลดจริง แต่ **ไตขวาที่ปกติชดเชย** (hyperfiltration) ทำให้ GFR รวมแทบไม่เปลี่ยน → Cr เกือบปกติ\n\n**post-renal AKI ต้องอุดทั้งสองข้าง** (bladder outlet, urethra, ท่อไตสองข้าง เช่น มะเร็งปากมดลูก) หรืออุดข้างเดียวในคนที่มี **ไตทำงานข้างเดียว**\n\n- นิ่วในท่อไตลด GFR ข้างนั้นจริง (แรงดันย้อน)\n- creatinine ไม่ได้ถูกหลั่งเข้าท่อไตเหนือนิ่ว\n- hydronephrosis ทำให้ RBF ลดในระยะหลัง ไม่ใช่เพิ่ม",
         "Post-renal AKI = อุดสองข้าง หรือไตข้างเดียว", "Post-renal principle", R("Post-renal AKI"), BASE + [OBST, STONE]),
    ], BASE + [UA, UA_B], figs={"sediment": F.sediment()})

# ═════════════════════════════════════════════ 4
sec("nephro-aki-04", "Pre-renal azotemia — สาเหตุ กลไก และ NSAID/ACEi",
    "ECV ลด · CO ลด · vasodilatation (✍️ sepsis พบบ่อยสุด) · renal vasoconstriction (✍️ NSAIDs) · UA bland · BUN/Cr > 20 · U Na < 20 · FENa < 1% · ✍️ HCO3 สูงขึ้นเร็ว · triple whammy", 10,
"""### สาเหตุ (สไลด์ p8–10)
| กลไก | สาเหตุ |
|---|---|
| **Effective ECV ลด** | fluid loss: **burn, diarrhea, diuretics** · fluid sequestration: **pancreatitis, burn**, crush, malnutrition, liver disease |
| **Cardiac output ลด** | heart failure · ✍️ **amphetamine, alcohol** (cardiomyopathy) |
| **Peripheral vasodilatation** | ยาลดความดัน · **sepsis (✍️ common สุด)** · adrenal insufficiency, hypermagnesemia, hypercapnia, hypoxemia |
| **Severe renal vasoconstriction** | sepsis · **NSAIDs (✍️ วงไว้)** · α-adrenergic agonists · **hepatorenal syndrome** |
| **Mechanical occlusion** | thrombosis, emboli ของหลอดเลือดแดงไต |

[[fig:prerenal]]

### กลไก: ไตพยุง GFR อย่างไร และยาไปทำลายตรงไหน
เมื่อความดันเลือดไปไตลด ไตมีกลไกพยุง GFR (autoregulation — ดูคาบ **Physio1**)
1. **Myogenic reflex + prostaglandin** → afferent arteriole ขยาย ให้เลือดเข้า glomerulus มากขึ้น
2. **Angiotensin II** → efferent arteriole หด ให้แรงดันใน glomerulus (P_GC) ค้างอยู่
3. **Aldosterone + ADH + sympathetic** → ดูด Na และน้ำกลับให้มากที่สุด

ยาที่ \"ตัด\" กลไกเหล่านี้ทำให้ GFR ตกทันทีในคนที่เลือดไปไตน้อยอยู่แล้ว: **NSAID** ตัดข้อ 1 · **ACEi/ARB** ตัดข้อ 2 · **diuretic** ลด volume เพิ่ม = **triple whammy**

### UA และแล็บใน pre-renal (สไลด์ p11)
- **Typical: bland sediment** (✍️ ดาว) — อาจมี hyaline cast · proteinuria 1+–2+ ได้แต่ส่วนใหญ่ < 500 mg/วัน
- BUN/Cr > 20 · U Na < 20 · FENa < 1% · Uosm > 400 · SpGr > 1.020 (รายละเอียดหัวข้อ 15)
- ✍️ ข้าง \"decreased effective ECV\": **HCO3 เริ่มสูงแล้ว (detect ได้ไวสุด)** — contraction alkalosis

#### ทำไมถึงมีอาการนี้
| สิ่งที่พบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **BUN/Cr > 20** | น้ำไหลช้าในท่อไต proximal → urea ถูกดูดกลับตามน้ำและ Na · ADH ยังเปิดทาง urea ที่ collecting duct · creatinine ไม่ถูกดูดกลับ | pre-renal (และ GI bleed, steroid ที่เพิ่ม urea) |
| **U Na < 20, FENa < 1%** | angiotensin II + aldosterone สั่งดูด Na คืนเกือบหมด | ท่อไตยังทำงาน — ATN จะสูง |
| **Uosm > 400–500, SpGr สูง** | ADH หลั่งเพราะ volume ลด → ดูดน้ำคืน ปัสสาวะเข้มข้น | ATN ทำเข้มข้นไม่ได้ (~300) |
| **HCO3 สูง (✍️)** | angiotensin II กระตุ้น NHE3 ที่ proximal ดูด HCO3 คืน · aldosterone หลั่ง H+ · Cl ต่ำ (อาเจียน/diuretic) | สัญญาณ volume ลดที่มาเร็ว |
| **ความดันท่ายืนตก ชีพจรเร็ว เยื่อบุแห้ง** | intravascular volume ลด | แยก \"ขาดน้ำ\" ออกจาก \"น้ำเกินแต่ ECV ต่ำ\" (HF, cirrhosis) |

### การดูแล
- **ขาดน้ำ/เสียเลือด**: ให้ isotonic crystalloid (และเลือดถ้าเสียเลือด) พร้อมหยุดเลือด/แก้สาเหตุ แล้วประเมินซ้ำบ่อย ๆ
- **หยุด/งดยา**: NSAID · ACEi/ARB · diuretic · metformin (เสี่ยง lactic acidosis เมื่อ GFR ต่ำ)
- **ปรับขนาดยา** ที่ขับทางไต
""",
    ["Pre-renal: ECV ลด · CO ลด · vasodilatation (✍️ sepsis) · renal vasoconstriction (✍️ NSAID, HRS) · occlusion",
     "PG ขยาย afferent + AngII หด efferent = พยุง GFR → NSAID/ACEi ตัดกลไกนี้",
     "Triple whammy: diuretic + NSAID + ACEi/ARB",
     "Pre-renal: UA bland · BUN/Cr > 20 · U Na < 20 · FENa < 1% · Uosm > 400",
     "✍️ HCO3 สูง (contraction alkalosis) เป็นสัญญาณ volume ลดที่มาเร็ว"],
    [mcq(N(7), "A 74-year-old man with hypertension takes lisinopril 20 mg and hydrochlorothiazide 25 mg daily. He started ibuprofen 400 mg three times daily for knee osteoarthritis 1 week ago, and has had watery diarrhoea for 2 days. BP 98/60 mmHg, PR 104/min, dry mucous membranes. Creatinine 2.6 mg/dL (baseline 1.0), BUN 64 mg/dL, K 5.7 mEq/L, urine sodium 11 mEq/L, bland urine sediment. Which is the most appropriate management?",
         ["Stop ibuprofen, hold lisinopril and hydrochlorothiazide, give intravenous isotonic crystalloid and monitor creatinine and potassium", "Continue lisinopril to protect the kidney and add furosemide to increase urine output", "Start prednisolone for presumed NSAID-induced interstitial nephritis", "Arrange urgent haemodialysis because creatinine has more than doubled", "Switch ibuprofen to celecoxib, which spares renal prostaglandins"], 0,
         "ภาพนี้คือ **triple whammy**: **diuretic + ท้องเสีย** (volume ลด) · **NSAID** ตัด prostaglandin ที่ขยาย afferent · **ACEi** ตัด angiotensin II ที่หด efferent → P_GC ตก → GFR ตก · UA bland, U Na 11 = pre-renal (hemodynamic)\n\nจัดการ: **หยุด NSAID · งด ACEi และ diuretic ชั่วคราว · ให้ isotonic fluid** แล้วติดตาม Cr/K\n\n- furosemide ทำให้ขาดน้ำมากขึ้น และ ACEi ทำให้ GFR/K แย่ลงตอนนี้\n- AIN ต้องมี pyuria/WBC cast ไม่ใช่ bland\n- K 5.7 และไม่มีน้ำเกิน → ยังไม่มีข้อบ่งชี้ dialysis\n- **COX-2 inhibitor ก็ลด prostaglandin ในไต** (COX-2 แสดงออกที่ macula densa) เสี่ยงเท่ากัน",
         "Triple whammy → หยุดยาทั้งสามกลุ่ม + ให้น้ำ", "Triple whammy", R("Cause of pre-renal azotemia (3)"), BASE + [ADR, GFRH]),
     mcq(N(8), "A 69-year-old woman with poor oral intake for 5 days has BUN 60 mg/dL, creatinine 2.0 mg/dL, Na 140, K 4.0, Cl 96 and HCO3 31 mEq/L. Urine sodium is 10 mEq/L and urine osmolality 650 mOsm/kg. Which mechanism best explains her BUN-to-creatinine ratio of 30?",
         ["Low tubular flow and ADH increase urea reabsorption, while creatinine is not reabsorbed", "Tubular cell necrosis releases urea into the urine", "Increased hepatic urea synthesis from hypercatabolism", "Reduced tubular secretion of creatinine by angiotensin II", "Glomerular protein leak raises plasma urea"], 0,
         "pre-renal: เลือดไปไตน้อย → **น้ำไหลช้าใน proximal tubule** urea ถูกดูดกลับตาม Na และน้ำมากขึ้น · **ADH** เปิด urea transporter ที่ inner medullary collecting duct ให้ urea กลับเพิ่ม · ส่วน **creatinine ถูกกรองแต่แทบไม่ถูกดูดกลับ** → BUN ขึ้นมากกว่า Cr → ratio > 20\n\nHCO3 31 = **contraction alkalosis** (✍️ \"HCO3 เริ่มสูงละ detect ได้ไวสุด\") · U Na 10, Uosm 650 = ท่อไตยังทำงาน\n\n- ATN ทำให้ ratio ~10 (ไม่ใช่สูง)\n- hypercatabolism ทำให้ BUN สูงได้ แต่โจทย์เป็นภาพขาดน้ำชัดเจน\n- angiotensin II ไม่ได้ลดการหลั่ง creatinine",
         "BUN/Cr > 20 = urea ถูกดูดกลับตามน้ำ", "Pre-renal BUN/Cr", R("Diagnostic indices", "UA in prerenal"), BASE + [RENH, OSM]),
    ], BASE + [SHOCK, GFRH, LYTE], figs={"prerenal": F.prerenal_causes()})

# ═════════════════════════════════════════════ 5
sec("nephro-aki-05", "Pre-renal ที่ไม่ใช่ \"ขาดน้ำ\" — sepsis · hepatorenal · cardiorenal",
    "Sepsis: vasodilatation + vasoconstriction ในไต + อักเสบ → MAP ≥ 65 ด้วย norepinephrine · HRS: splanchnic vasodilation → ไตหดตัว FENa ต่ำมาก · Cardiorenal type 1: venous congestion → decongest ด้วย diuretic", 8,
"""สไลด์ให้ **sepsis** อยู่ทั้งใน peripheral vasodilatation (p9) และ severe renal vasoconstriction (p10) และให้ **hepatorenal syndrome** เป็น renal vasoconstriction · ✍️ อาจารย์ขีดเส้นใต้ hepatorenal · ส่วน cardiorenal อยู่ใต้ \"decrease cardiac output\" (p8) — รายละเอียดกลไกและการรักษาในหัวข้อนี้ **อิงตำราและแนวทาง ไม่อยู่ในสไลด์**

### Sepsis-associated AKI
- ✍️ **sepsis เป็นสาเหตุที่พบบ่อยที่สุด** ของ AKI ในโรงพยาบาล (โดยเฉพาะ ICU)
- กลไกไม่ใช่แค่ความดันต่ำ: หลอดเลือดทั่วตัวขยาย (warm shock, pulse pressure กว้าง) แต่ **หลอดเลือดในไตหด** · **microcirculation ผิดปกติ** · cytokine ทำร้ายเซลล์ท่อไตโดยตรง — AKI จึงเกิดได้แม้ renal blood flow ไม่ต่ำ
- สไลด์ p50: sepsis เป็น ATN ที่ **FENa อาจต่ำ** (มีส่วนของหลอดเลือดหด)
- รักษา: แก้การติดเชื้อ · ให้ fluid ตามการตอบสนอง · **vasopressor (norepinephrine) ให้ MAP ≥ 65** · ไม่ใช้ dopamine \"renal dose\" (KDIGO 2012 ไม่แนะนำ) · หลีกเลี่ยงยาที่ทำร้ายไต

### Hepatorenal syndrome (HRS-AKI)
1. Cirrhosis + portal hypertension → **splanchnic vasodilatation** (NO) → arterial underfilling
2. ร่างกายรับรู้ว่า \"เลือดไม่พอ\" → **RAAS + sympathetic + ADH** ทำงานเต็มที่
3. **หลอดเลือดไตหดอย่างรุนแรง** → GFR ตก ทั้งที่เนื้อไตปกติ (ไตจาก HRS เคยใช้ปลูกถ่ายได้ผลดี)
- ลักษณะ: **U Na ต่ำมาก FENa < 0.2%** · UA bland · protein < 500 mg/วัน · ultrasound ปกติ · มักมี hyponatremia
- วินิจฉัย (EASL 2018 / ICA): ไม่มี shock ไม่ได้ยา nephrotoxic ไม่มีโรคเนื้อไต และ **ไม่ดีขึ้นหลังหยุด diuretic + ให้ albumin 1 g/kg/วัน นาน 2 วัน**
- รักษา: **terlipressin + albumin** (ทางเลือก norepinephrine) · รักษาขาดคือปลูกถ่ายตับ

### Cardiorenal syndrome
- **Type 1** (acute cardiorenal): หัวใจล้มเหลวเฉียบพลัน → AKI
- ตัวขับสำคัญคือ **venous congestion** (CVP สูง → แรงดันหลอดเลือดดำไตและในเนื้อไตสูง → แรงดันกรองสุทธิลด) มากกว่า low output อย่างเดียว
- ผู้ป่วย **บวม JVP สูง U Na ต่ำ** — ไม่ใช่ขาดน้ำ → รักษาด้วย **decongestion: IV loop diuretic** · Cr ขึ้นเล็กน้อยระหว่างขับน้ำมักยอมรับได้ถ้าอาการคั่งดีขึ้น

#### ทำไมถึงมีอาการนี้
| ลักษณะ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **มือเท้าอุ่น pulse pressure กว้าง Cr ขึ้น** | vasodilated high-output state (sepsis, cirrhosis) → effective arterial volume ต่ำ | ไม่ใช่ cardiogenic shock (มือเท้าเย็น) |
| **HRS: U Na < 10, FENa < 0.2%** | renal vasoconstriction สุดขีด แต่ท่อไตดี | ATN ใน cirrhosis จะมี FENa สูงและ granular cast |
| **HF: บวม JVP สูง แต่ U Na ต่ำ** | ไตรับรู้ low effective flow + congestion → เก็บ Na | ต้องขับน้ำ ไม่ใช่ให้น้ำ |
""",
    ["✍️ Sepsis = สาเหตุ AKI ที่พบบ่อยที่สุด · ไตเสียได้แม้ RBF ไม่ต่ำ · MAP ≥ 65 ด้วย norepinephrine",
     "HRS: splanchnic vasodilation → ไตหดสุด · FENa < 0.2% · albumin 1 g/kg × 2 วันก่อนวินิจฉัย · terlipressin + albumin",
     "Cardiorenal type 1: venous congestion เป็นตัวขับ → decongest ด้วย loop diuretic",
     "Dopamine renal dose ไม่ช่วย (KDIGO 2012)"],
    [mcq(N(9), "A 56-year-old man with alcohol-related cirrhosis and tense ascites is admitted with confusion. He takes spironolactone and furosemide. BP 102/64 mmHg. Creatinine has risen from 0.9 to 2.1 mg/dL over 4 days. Urine sodium 6 mEq/L, FENa 0.1%, no proteinuria or haematuria, and renal ultrasound is normal. There is no shock and no nephrotoxic drug exposure. What is the most appropriate next step?",
         ["Stop diuretics and give intravenous albumin 1 g/kg/day for 2 days, then reassess", "Start terlipressin immediately without albumin", "Give 3 litres of normal saline over 6 hours", "Start low-dose dopamine to improve renal blood flow", "Perform a kidney biopsy to exclude glomerulonephritis"], 0,
         "ภาพเข้าได้กับ **pre-renal/HRS-AKI ใน cirrhosis**: FENa ต่ำมาก UA bland ultrasound ปกติ\n\nขั้นแรก (EASL 2018 / ICA): **หยุด diuretic + ให้ albumin 1 g/kg/วัน นาน 2 วัน** → ถ้าดีขึ้นคือ pre-renal จาก volume · ถ้าไม่ดีขึ้นและเข้าเกณฑ์ = **HRS-AKI → terlipressin + albumin**\n\n- terlipressin ใช้หลัง albumin challenge และต้องให้ร่วมกับ albumin\n- normal saline ปริมาณมากทำให้ ascites/hyponatremia แย่ลง\n- dopamine ไม่มีประโยชน์\n- ไม่มีข้อบ่งชี้เจาะไต (UA bland ultrasound ปกติ) และเสี่ยงเลือดออก\n\n(หัวข้อนี้อิงแนวทาง ไม่อยู่ในสไลด์ — สไลด์ระบุ hepatorenal syndrome เป็น severe renal vasoconstriction)",
         "HRS: หยุด diuretic + albumin 1 g/kg × 2 วัน ก่อน", "Hepatorenal syndrome", R("Cause of pre-renal azotemia (3)", "EASL Clinical Practice Guidelines for decompensated cirrhosis 2018"), BASE + [CIRR]),
     mcq(N(10), "A 67-year-old woman with acute pyelonephritis is in septic shock. After 30 mL/kg of intravenous crystalloid her mean arterial pressure is 58 mmHg, lactate 4.1 mmol/L, and urine output 15 mL/h. Her lungs now have bibasal crackles. Which intervention is most likely to protect her kidney function?",
         ["Start norepinephrine to achieve a mean arterial pressure of at least 65 mmHg", "Start low-dose dopamine at 2 µg/kg/min for renal vasodilatation", "Give furosemide to convert oliguric to non-oliguric AKI", "Continue large fluid boluses until the central venous pressure exceeds 20 mmHg", "Start haemodialysis immediately to remove cytokines"], 0,
         "หลังให้ fluid เพียงพอแล้ว MAP ยังต่ำ = **vasodilatory (septic) shock** → **norepinephrine ให้ MAP ≥ 65 mmHg** เพื่อคืนแรงดันเลือดไปไต (สไลด์: sepsis = peripheral vasodilatation)\n\n- **dopamine renal dose** ไม่ป้องกันหรือรักษา AKI (KDIGO 2012 แนะนำไม่ใช้)\n- **furosemide** เปลี่ยน oliguric เป็น non-oliguric ไม่ได้ช่วยผลลัพธ์ ใช้เฉพาะเมื่อน้ำเกิน\n- เริ่มมี crackles แล้ว การให้น้ำต่อจน CVP สูงทำให้ไตบวม/congest และปอดแย่ลง\n- ยังไม่มีข้อบ่งชี้ dialysis",
         "Septic shock + AKI: norepinephrine ให้ MAP ≥ 65 ไม่ใช่ dopamine", "Sepsis-associated AKI", R("Cause of pre-renal azotemia (2)", KDIGO), BASE + [SEPSIS, SHOCK]),
    ], BASE + [SEPSIS, HF, CIRR], src=SRC_ADD)

# ═════════════════════════════════════════════ 6
sec("nephro-aki-06", "Intrinsic (1) — renal vascular disorders: TMA · scleroderma crisis · malignant HT · RVT",
    "✍️ ลำดับพบบ่อย: TTP/HUS > scleroderma renal crisis > renal vein thrombosis > malignant HT · UA bland/hematuria ได้ แต่ไม่มี RBC cast · TTP → plasma exchange · SRC → ACEi", 9,
"""### Intrinsic AKI แบ่ง 4 กลุ่ม (สไลด์ p12)
**Renal vascular disorder · acute glomerulonephritis (AGN) · acute interstitial nephritis (AIN) · acute tubular necrosis (ATN)** — หัวข้อ 6–11 ไล่ทีละกลุ่ม

### Renal vascular disorders (สไลด์ p13)
- **Malignant hypertension** (malignant nephrosclerosis)
- **Scleroderma renal crisis** — ✍️ \"Prednisolone\" (ยาที่กระตุ้น) · ✍️ \"thrombotic angiopathy\"
- **TTP/HUS (TMA)** — ✍️ highlight · ✍️ \"neurological (specific)\" · ✍️ common: AKI ที่มา present
- **Renal vein thrombosis** — ✍️ case: U/D membranous nephropathy (MN) → CC: hematuria · ✍️ ⇒ antiphospholipid
- **Antiphospholipid syndrome (APS)**

✍️ อาจารย์ใส่ลำดับความถี่ **① TTP/HUS ② scleroderma renal crisis ③ renal vein thrombosis ④ malignant HT** และเล่าเคส \"**common ⇒ หญิงอายุ 26 ปี AKI → MAHA → TTP ⇒ หาสาเหตุรอง (SLE) → ต้องรีบทำ plasma exchange**\"

[[fig:vascular]]

### Thrombotic microangiopathy (TTP/HUS)
- **TTP**: ขาด ADAMTS13 (ส่วนใหญ่เป็น autoantibody) → vWF multimer ยาวจับเกล็ดเลือด → ลิ่มทั่วร่าง · เด่น **สมอง** · AKI มักไม่รุนแรงเท่า HUS · ADAMTS13 < 10%
- **HUS**: Shiga toxin (STEC, เด็ก ท้องเสียเป็นเลือด) · **aHUS**: complement ผิดปกติ · ไตเด่น
- สาเหตุรองของ TMA: SLE/APS, มะเร็ง, ยา (calcineurin inhibitor, gemcitabine, quinine), ตั้งครรภ์ (HELLP), HIV, malignant HT, scleroderma
- การรักษา TTP (ISTH 2020 — ไม่อยู่ในสไลด์): **plasma exchange ด่วน** + corticosteroid (± caplacizumab, rituximab) · **เลี่ยงการให้เกล็ดเลือด** ถ้าไม่มีเลือดออกรุนแรง

### Scleroderma renal crisis
- systemic sclerosis (มัก diffuse, ระยะแรก, anti-RNA polymerase III) · ✍️ **prednisolone ขนาดสูง (≥ 15 mg/วัน) เป็นตัวกระตุ้น**
- intimal proliferation ของ interlobular artery (onion skin) → ไตขาดเลือด → **renin พุ่ง → BP สูงมาก** → วงจร
- รักษา: **ACE inhibitor (captopril) ไต่ขนาดเร็ว** แม้ Cr ขึ้น — ข้อยกเว้นที่ ACEi ใช้ใน AKI

### Malignant hypertension · RVT · APS
- **Malignant HT**: BP มัก≥ 180/120 + จอตาเลือดออก/papilledema · fibrinoid necrosis · ลด BP แบบควบคุม (≤ 25% ในชั่วโมงแรก)
- **Renal vein thrombosis**: membranous nephropathy (hypercoagulable จาก nephrotic) · APS · ปวดสีข้าง hematuria ไตโต · ยืนยันด้วย CT/MR venography · anticoagulant

### UA ใน vascular disorder (สไลด์ p14)
- **Typical: bland sediment**
- บางโรคมี **microscopic hematuria** เช่น renal vein thrombosis, TMA, scleroderma renal crisis
- บางโรคมี proteinuria, RBC, **dysmorphic RBC** ได้ **แต่จะไม่มี RBC cast** เช่น malignant HT

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Schistocyte, LDH สูง, haptoglobin ต่ำ** | RBC ถูกเฉือนผ่านลิ่มเกล็ดเลือด/ไฟบรินในหลอดเลือดเล็ก | MAHA = TMA (TTP/HUS/SRC/malignant HT) · Coombs ลบ |
| **เกล็ดเลือดต่ำ** | ถูกใช้ในลิ่ม | DIC จะมี PT/aPTT ยาว fibrinogen ต่ำ · TTP ปกติ |
| **สับสน ชัก อาการเฉพาะที่ (✍️)** | ลิ่มในหลอดเลือดสมอง | เด่นใน TTP |
| **BP พุ่ง + Cr ขึ้นในผู้ป่วย SSc** | หลอดเลือดไตตีบ → renin สูง | SRC — ตอบสนองต่อ ACEi |
| **ปวดสีข้าง + hematuria ในผู้ป่วย nephrotic** | ลิ่มในหลอดเลือดดำไต ไตบวม | RVT — คิดถึงใน MN |
""",
    ["✍️ vascular ที่พบบ่อย: ① TTP/HUS ② SRC ③ RVT ④ malignant HT",
     "UA vascular: bland หรือ hematuria/dysmorphic RBC ได้ แต่ไม่มี RBC cast",
     "TTP: MAHA + PLT ต่ำ + อาการสมอง → plasma exchange ด่วน · เลี่ยงให้เกล็ดเลือด",
     "Scleroderma renal crisis: ✍️ prednisolone ขนาดสูงกระตุ้น · รักษาด้วย ACEi",
     "RVT: คิดถึงใน membranous nephropathy และ APS"],
    [mcq(N(11), "A 26-year-old woman presents with 3 days of fever, headache and intermittent confusion. Hb 7.8 g/dL with many schistocytes, platelets 18,000/mm³, LDH 1,450 U/L, haptoglobin undetectable, direct Coombs test negative, PT and aPTT normal. Creatinine 2.1 mg/dL, urine shows protein 2+ and 5–10 RBC/HPF without casts. ANA is positive at 1:640. What is the most appropriate immediate management?",
         ["Send ADAMTS13 activity and start urgent plasma exchange with corticosteroids", "Transfuse platelets to raise the count above 50,000/mm³", "Start haemodialysis and wait for the ADAMTS13 result", "Perform an urgent kidney biopsy to confirm lupus nephritis", "Start intravenous immunoglobulin alone"], 0,
         "MAHA (schistocyte LDH สูง haptoglobin ต่ำ Coombs ลบ) + เกล็ดเลือดต่ำ + อาการทางสมอง + AKI ในหญิงอายุน้อย = **TTP** (✍️ อาจารย์: \"26 ปี AKI female → MAHA → TTP ⇒ 2° cause (SLE) → ต้องรีบทำ plasma\") · ANA บวกชวนคิด SLE เป็นสาเหตุรอง\n\n**เจาะ ADAMTS13 ก่อนแล้วเริ่ม plasma exchange ทันที** ไม่ต้องรอผล (TTP ที่ไม่รักษาตาย ~90%) + corticosteroid\n\n- **การให้เกล็ดเลือด** อาจเพิ่มลิ่ม — ให้เฉพาะเลือดออกรุนแรง\n- dialysis ไม่ได้รักษาสาเหตุ\n- เจาะไตใน PLT 18,000 อันตรายมาก และ UA ไม่มี RBC cast\n- IVIG ไม่ใช่การรักษาหลัก",
         "MAHA + PLT ต่ำ + สมอง → plasma exchange ด่วน", "TTP", R("Renal vascular disorder (ลายมือ)", "ISTH guideline for treatment of TTP 2020"), BASE + [HEMO, HEMO_B]),
     mcq(N(12), "A 45-year-old woman with diffuse cutaneous systemic sclerosis diagnosed 1 year ago was started on prednisolone 40 mg/day for myositis 3 weeks ago. She now has headache and blurred vision. BP 196/112 mmHg (previously 118/74). Creatinine 2.4 mg/dL (baseline 0.8), platelets 96,000/mm³ with occasional schistocytes, urine protein 1+ with no casts. What is the most appropriate treatment?",
         ["Start an ACE inhibitor such as captopril and titrate rapidly", "Increase prednisolone to 1 mg/kg/day", "Start a beta-blocker as monotherapy", "Give intravenous cyclophosphamide pulses", "Avoid all antihypertensive drugs until creatinine stabilises"], 0,
         "**Scleroderma renal crisis**: SSc ชนิด diffuse ระยะแรก + **prednisolone ขนาดสูง (✍️ ตัวกระตุ้น)** + BP พุ่ง + AKI + MAHA เล็กน้อย · UA เกือบ bland (สไลด์ p14: vascular ไม่มี RBC cast)\n\nกลไก: หลอดเลือดไตตีบ → ไตขาดเลือด → **renin สูง** → BP สูง → หลอดเลือดเสียต่อ\n\nรักษา: **ACE inhibitor (captopril) ไต่ขนาดเร็ว** แม้ Cr ขึ้น เพราะตัดวงจร renin โดยตรง (อิงตำรา)\n\n- steroid ขนาดสูงคือตัวกระตุ้น ต้องลดลง\n- β-blocker เดี่ยว ไม่แก้ renin และอาจทำให้หลอดเลือดหด\n- cyclophosphamide ไม่ใช่การรักษา SRC\n- การไม่ลด BP ทำให้ไตเสียมากขึ้น",
         "SRC: steroid ขนาดสูงกระตุ้น · ACEi รักษา", "Scleroderma renal crisis", R("Renal vascular disorder (ลายมือ)"), BASE + [SSC, MHT]),
    ], BASE + [MHT, SSC, HEMO], figs={"vascular": F.vascular()})

# ═════════════════════════════════════════════ 7
sec("nephro-aki-07", "Intrinsic (2) — glomerulonephritis ที่มาเป็น AKI",
    "Post-infectious GN · MPGN · RPGN · lupus nephritis · IgA nephropathy · vasculitis · FSGS · UA: proteinuria (มัก nephrotic range) + dysmorphic RBC + RBC cast · AKI + RBC cast = RPGN จนกว่าจะพิสูจน์ได้ว่าไม่ใช่", 8,
"""### GN ที่ทำให้ AKI (สไลด์ p15)
| โรค | ลายมือ/เบาะแส |
|---|---|
| **Post-infectious GN** | ✍️ \"เด็ก\" · หลังคออักเสบ/ผิวหนังติดเชื้อ 1–3 สัปดาห์ · ✍️ ASO titer |
| **MPGN** | ✍️ สาเหตุรอง: **HCV พบบ่อยที่สุด** · ✍️ \"HBV ⇒ MN common\" |
| **RPGN** | Cr ขึ้นเร็วในวัน–สัปดาห์ · crescent (ภาพด้านล่าง) |
| **Lupus nephritis** | หญิงอายุน้อย · complement ต่ำ · ANA/anti-dsDNA |
| **IgA nephropathy** | ✍️ \"syn-pharyngitic\" — เป็นหวัดแล้วปัสสาวะเป็นเลือด **ในวันเดียวกัน** |
| **Renal vasculitis** | ANCA (GPA, MPA) · ไอเป็นเลือด ไซนัส |
| **FSGS** | nephrotic เด่น (ภาพ histology ในสไลด์ p18) |

✍️ เคสที่อาจารย์เล่า: U/D **DM** (poor controlled → **diabetic nephropathy**) และ **thalassemia** มีเม็ดเลือดแดงในปัสสาวะ → ส่ง **ASO titer** — ตัวอย่างว่าผู้ป่วยมีโรคไตเดิมได้แต่ต้องหา GN ซ้อน

> รายละเอียดโรค GN แต่ละชนิดอยู่ในคาบ **14 Approach to glomerular disease** — หัวข้อนี้เน้นมุม \"GN ที่มาเป็น AKI\" และการอ่าน UA

### UA ใน acute GN
สไลด์ p21
- proteinuria (มักเป็น **nephrotic range**) · WBC · RBC
- เจอ **oval fat bodies, waxy cast, fatty cast** ได้
- เจอ **dysmorphic RBC, RBC cast** ได้ (✍️ highlight ทั้งหมด)

[[img:i01]]

[[img:i02]]

### RPGN — เมื่อไรต้องรีบ
- AKI + **dysmorphic RBC/RBC cast** + proteinuria = **RPGN จนกว่าจะพิสูจน์ได้ว่าไม่ใช่** — ไตเสียถาวรได้ในไม่กี่วัน
- ส่งด่วน: **anti-GBM, ANCA, C3/C4, ANA/anti-dsDNA** (± ASO, hepatitis B/C) และ **เจาะไต** เร็ว
- รุนแรง/รอผลไม่ได้: เริ่ม **IV methylprednisolone** ได้ก่อน (± plasma exchange ใน anti-GBM) — การรักษาอิงตำรา/KDIGO GN 2021 ไม่อยู่ในสไลด์

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปัสสาวะสีโค้ก/น้ำล้างเนื้อ** | RBC ผ่าน GBM ที่ฉีก hemoglobin ถูกเปลี่ยนเป็น methemoglobin ในปัสสาวะกรด | สีน้ำตาลจาก glomerulus vs สีแดงสด + ลิ่มเลือดจากทางเดินปัสสาวะ |
| **Dysmorphic RBC** | RBC เบียดผ่านรูเล็กและเจอ osmotic stress ตลอดท่อไต | > 80% dysmorphic หรือ acanthocyte > 5% ชวน GN |
| **RBC cast** | RBC ติดในแม่พิมพ์ Tamm–Horsfall ในท่อไต | จำเพาะต่อ GN · malignant HT ไม่มี (p14) |
| **บวม ความดันสูง ปัสสาวะน้อย** | GFR ตก + ไตดูด Na คืนมาก (primary Na retention) | nephritic syndrome |
| **ไอเป็นเลือด + AKI** | anti-GBM หรือ ANCA ทำลาย capillary ทั้งปอดและไต | pulmonary–renal syndrome ต้องรักษาด่วน |
""",
    ["GN ที่มาเป็น AKI: PIGN (✍️ เด็ก) · MPGN (✍️ HCV) · RPGN · lupus · IgA (✍️ syn-pharyngitic) · vasculitis · FSGS",
     "UA ใน GN: dysmorphic RBC + RBC cast + proteinuria (มัก nephrotic range)",
     "AKI + RBC cast = RPGN จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → serology + เจาะไตด่วน",
     "Crescent = proliferation ใน Bowman's space จาก capillary ที่แตก"],
    [mcq(N(13), "A 62-year-old man has 3 weeks of malaise, arthralgia and intermittent haemoptysis. Creatinine has risen from 1.0 to 4.5 mg/dL over 3 weeks. Urinalysis shows protein 2+, 30–50 RBC/HPF that are mostly dysmorphic, and RBC casts. Chest radiograph shows bilateral patchy alveolar opacities. What is the most appropriate next step?",
         ["Urgent ANCA, anti-GBM antibody and complement levels with early kidney biopsy, considering empirical pulse methylprednisolone", "Repeat creatinine in 4 weeks to confirm chronicity", "Start an ACE inhibitor and recheck proteinuria in 3 months", "Treat as community-acquired pneumonia and prerenal AKI with fluids", "Cystoscopy to exclude bladder cancer"], 0,
         "AKI ที่ Cr ขึ้นในไม่กี่สัปดาห์ + **dysmorphic RBC + RBC cast** = **RPGN** · ร่วมกับไอเป็นเลือดและปอดมีเงา = **pulmonary–renal syndrome** (ANCA vasculitis หรือ anti-GBM)\n\nต้อง **ส่ง ANCA, anti-GBM, C3/C4 ด่วน + เจาะไตเร็ว** และพิจารณา **pulse methylprednisolone** ทันทีถ้ารุนแรง (± plasma exchange ใน anti-GBM)\n\n- รอ 4 สัปดาห์ = ไตเสียถาวร\n- ACEi เป็นการรักษาระยะยาวของ proteinuria ไม่ใช่ RPGN\n- RBC cast ไม่ใช่ pre-renal\n- cystoscopy ใช้กับเลือดออกจากทางเดินปัสสาวะ (RBC รูปร่างปกติ ไม่มี cast)",
         "AKI + RBC cast + ไอเป็นเลือด → ANCA/anti-GBM + biopsy ด่วน", "RPGN", R("Glomerulonephritis, UA in acute GN"), BASE + [AGN, UA_B]),
     mcq(N(14), "A 54-year-old man with longstanding uncontrolled hypertension presents with BP 230/140 mmHg, retinal haemorrhages and papilloedema. Creatinine is 3.0 mg/dL. Which urine sediment finding would most strongly suggest a primary glomerulonephritis rather than malignant hypertension as the cause of his AKI?",
         ["Red blood cell casts", "Proteinuria 2+", "Dysmorphic red blood cells", "Microscopic haematuria 5–10 RBC/HPF", "Hyaline casts"], 0,
         "สไลด์ p14: ใน vascular disorder เช่น **malignant HT** พบ **proteinuria, RBC และ dysmorphic RBC ได้ แต่ไม่มี RBC cast** · ส่วน p21: **RBC cast** พบใน acute GN\n\nดังนั้นสิ่งที่ชี้ไป GN มากที่สุดคือ **RBC cast**\n\n- proteinuria, hematuria และ dysmorphic RBC เกิดได้ทั้งสองแบบ\n- hyaline cast ไม่จำเพาะ พบในคนปกติ/ขาดน้ำ",
         "Malignant HT มี dysmorphic RBC ได้ แต่ไม่มี RBC cast", "UA: vascular vs GN", R("UA in intrinsic AKI: vascular, UA in acute GN"), BASE + [MHT, UA_B]),
    ], BASE + [AGN, UA_B, HEMAT],
    imgs=IMGS(
        IM(1, "Normal glomerulus (สไลด์ p16)", "ภาพชิ้นเนื้อไตย้อม PAS glomerulus ปกติ มีลูกศรยาวชี้ผนัง capillary ลูกศรสั้นชี้ tubular basement membrane และลูกศรคู่ชี้ mesangium ใต้ภาพมีคำอธิบายภาษาอังกฤษ",
           cap="**Glomerulus ปกติ** (courtesy Helmut G Rennke) — capillary lumen เปิดโล่ง มีเซลล์ 1–2 ตัวต่อ capillary tuft · ผนัง capillary (ลูกศรยาว) หนาเท่า tubular basement membrane (ลูกศรสั้น) · mesangial cell อยู่ตรงก้าน (ลูกศรคู่) — ใช้เทียบกับภาพ RPGN ถัดไป"),
        IM(2, "RPGN — glomerulus มี crescent (สไลด์ p20)", "ภาพชิ้นเนื้อไตย้อมสีชมพูแดง เห็น glomerulus สามวง วงบนมีลูกศรดำชี้เซลล์ที่เพิ่มจำนวนเป็นรูปจันทร์เสี้ยวใน Bowman's space กด capillary tuft",
           q="ภาพนี้มาจากผู้ป่วยที่ Cr ขึ้นเร็วในไม่กี่สัปดาห์ — ลูกศรชี้อะไร และบอกโรคกลุ่มไหน",
           quiz="**คำตอบ:** **crescent** ใน Bowman's space = **RPGN (crescentic GN)** · **กลไก:** capillary ของ glomerulus แตก fibrin และ cytokine รั่วเข้า Bowman's space กระตุ้น parietal epithelial cell + macrophage เพิ่มจำนวนเป็นรูปจันทร์เสี้ยว กด tuft จน GFR ตก · **ทำต่อ:** anti-GBM, ANCA, complement และรักษาด่วน — crescent ที่กลายเป็นพังผืดแล้วไม่กลับคืน")))

# ═════════════════════════════════════════════ 8
sec("nephro-aki-08", "Intrinsic (3) — acute interstitial nephritis (AIN)",
    "ยา: β-lactam (✍️ penicillin) · sulfonamide · rifampicin · cimetidine (+ NSAID, PPI) · ติดเชื้อ: ✍️ leptospirosis, hantavirus · UA: WBC + WBC cast ไม่มี RBC cast · eosinophiluria > 5% ชวน AIN จากยา · หยุดยา", 9,
"""### สาเหตุ (สไลด์ p22)
| กลุ่ม | ตัวอย่าง | ลายมือ |
|---|---|---|
| **Drugs** | **β-lactam** (✍️ penicillin) · sulfonamide · rifampicin · cimetidine | ✍️ **\"จำ\"** |
| **Infections** | **leptospirosis** (✍️ acute febrile illness ⇒ ต้องมี liver failure ร่วม) · **Hantavirus** (✍️ หนูเป็นพาหะ) | ✍️ **\"จำ\"** |
| Infiltration | sarcoidosis, leukemia, lymphoma | ✍️ \"ไม่ต้องจำ\" |
| Connective tissue diseases | Sjögren, SLE | ✍️ \"ไม่ต้องจำ\" |

ยาที่พบบ่อยในเวชปฏิบัติปัจจุบันเพิ่มเติม (ตำรา): **NSAIDs, proton pump inhibitors**, allopurinol, diuretics, ciprofloxacin

### กลไก AIN
- ยาเป็น **hapten** จับโปรตีนท่อไต (หรือเลียนแบบแอนติเจน) → **ภูมิแพ้ชนิด T cell (type IV)** + eosinophil แทรกใน interstitium
- เริ่ม **7–10 วันหลังได้ยา** (1–3 วันถ้าเคยได้) · ไม่ขึ้นกับขนาดยา
- interstitium บวม + tubulitis → GFR ลด · WBC หลุดลงท่อ → WBC cast
- อาการทั้งระบบ: ไข้ ผื่น eosinophilia — **ครบทั้ง 3 ข้อน้อยกว่า 10–15%** (NSAID มักไม่มี)

[[img:i03]]

### UA ใน AIN (สไลด์ p25–27)
- proteinuria แบบ **subnephrotic** · **WBC, WBC cast** ได้
- เจอ RBC ได้แต่ไม่ค่อยเด่น · **ไม่เจอ RBC cast**
- drug-induced **penicillin**: WBC เด่น + **Hansel's stain positive** (eosinophiluria)
- drug-induced **NSAIDs**: proteinuria แบบ **nephrotic syndrome** ได้ (AIN + minimal change disease)
- **Eosinophiluria** (eosinophil ≥ 1–3% ของ WBC ในปัสสาวะ) พบใน AIN · UTI · transplant rejection · GN/RPGN · atheroembolic disease · prostatitis → **ถ้า > 5% ชวนคิด AIN จากยา** (✍️ ดาว)

[[img:i04]]

> ข้อมูลปัจจุบันพบว่า urine eosinophil มีความไวและความจำเพาะต่ำ (ไม่มีก็ไม่ตัด AIN) — การวินิจฉัยแน่นอนคือ **เจาะไต** (ตำรา)

### การรักษา (ตำรา — ไม่อยู่ในสไลด์)
1. **หยุดยาที่สงสัยทันที** — สำคัญที่สุด · เปลี่ยนเป็นยาคนละกลุ่ม
2. ไม่ดีขึ้นใน 3–7 วัน หรือรุนแรง → **corticosteroid** (prednisolone ~1 mg/kg/วัน แล้วลดขนาดใน 4–6 สัปดาห์) — ได้ผลดีถ้าเริ่มเร็ว ก่อนเกิดพังผืด
3. leptospirosis: penicillin G/ceftriaxone/doxycycline + ดูแลประคับประคอง

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ไข้ ผื่น maculopapular** | ปฏิกิริยาภูมิไวเกินต่อยาทั้งระบบ | ไม่มีก็ไม่ตัด AIN |
| **Eosinophilia/eosinophiluria** | Th2 cytokine (IL-5) ดึง eosinophil | > 5% ชวน AIN จากยา (สไลด์) |
| **Sterile pyuria + WBC cast** | WBC ใน interstitium หลุดลงท่อแล้วอัดในแม่พิมพ์ Tamm–Horsfall | WBC cast = AIN หรือ pyelonephritis (culture แยก) |
| **ไม่มี RBC cast** | glomerulus ไม่ได้อักเสบ | แยกจาก GN |
| **Leptospirosis: AKI ไม่ปัสสาวะน้อย + K ต่ำ** | เชื้อทำ tubulointerstitial nephritis ที่ proximal tubule → ดูด Na ลดลง Na ไปถึง distal มาก → ขับ K | ✍️ febrile illness + ตับผิดปกติ + ไตวาย ในเกษตรกร |
""",
    ["AIN จากยา: ✍️ penicillin/β-lactam · sulfonamide · rifampicin · cimetidine (+ NSAID, PPI)",
     "AIN จากเชื้อ: ✍️ leptospirosis (ไข้ + ตับ + ไต) · hantavirus (หนู)",
     "UA: sterile pyuria + WBC cast · ไม่มี RBC cast · NSAID → nephrotic ได้",
     "Eosinophiluria > 5% ชวน AIN จากยา แต่ไม่ไวและไม่จำเพาะ",
     "รักษา: หยุดยาทันที ± steroid ถ้าไม่ดีขึ้น"],
    [mcq(N(15), "A 58-year-old man is receiving intravenous cloxacillin for cellulitis. On day 10 he develops fever and a diffuse maculopapular rash. Creatinine has risen from 0.9 to 2.8 mg/dL. Blood eosinophils 12%. Urinalysis: protein 1+, WBC 20–30/HPF, WBC casts, RBC 2–3/HPF, no RBC casts; urine culture negative; Hansel's stain shows 8% eosinophils. What is the most appropriate management?",
         ["Stop cloxacillin and switch to a non-beta-lactam antibiotic, adding corticosteroid if kidney function does not improve", "Continue cloxacillin and add an antihistamine for the rash", "Switch to cefazolin because cephalosporins do not cause interstitial nephritis", "Start empirical treatment for pyelonephritis with ceftriaxone", "Start plasma exchange for presumed vasculitis"], 0,
         "ยา β-lactam วันที่ 10 + ไข้ ผื่น eosinophilia + **sterile pyuria + WBC cast** ไม่มี RBC cast + **eosinophiluria 8% (> 5% ชวน AIN จากยา)** = **drug-induced AIN** (สไลด์ p25: penicillin group WBC เด่น Hansel stain บวก)\n\nจัดการ: **หยุดยาทันที เปลี่ยนเป็นยาคนละกลุ่ม** (เช่น clindamycin ตามเชื้อ) · ไม่ดีขึ้นใน 3–7 วัน → corticosteroid\n\n- ให้ยาต่อทำให้เกิดพังผืดถาวร\n- **cephalosporin เป็น β-lactam** อาจแพ้ข้ามกลุ่ม\n- culture ลบ ไม่ใช่ pyelonephritis\n- ไม่มี RBC cast/ANCA ไม่ใช่ vasculitis",
         "AIN จากยา: หยุดยา ± steroid", "Drug-induced AIN", R("Interstitial nephritis, UA in AIN, Eosinophiluria"), BASE + [AIN, ADR]),
     mcq(N(16), "A 42-year-old rice farmer in north-eastern Thailand presents after 5 days of high fever, severe calf pain and conjunctival suffusion. Total bilirubin 6.8 mg/dL with mildly raised transaminases, platelets 62,000/mm³, creatinine 3.2 mg/dL, potassium 3.0 mEq/L. Urine output is 1.8 L/day. Which description best fits the renal involvement?",
         ["Non-oliguric AKI from tubulointerstitial nephritis with renal potassium wasting", "Oliguric AKI from post-streptococcal glomerulonephritis with hyperkalaemia", "Post-renal AKI from bilateral ureteric obstruction", "Hepatorenal syndrome with a fractional excretion of sodium below 0.2%", "Thrombotic thrombocytopenic purpura with ADAMTS13 deficiency"], 0,
         "ไข้สูง ปวดน่อง ตาแดง (conjunctival suffusion) ตัวเหลือง เกล็ดเลือดต่ำในเกษตรกร = **leptospirosis (Weil's disease)** — ✍️ \"acute febrile illness ⇒ ต้องมี liver failure\" สไลด์ p22 จัดเป็นสาเหตุ **AIN**\n\nไตใน leptospirosis: **tubulointerstitial nephritis** ที่ proximal tubule → ดูด Na ลดลง Na ไปถึง distal มาก → **ขับ K มาก (K ต่ำ)** และมัก **non-oliguric**\n\n- PSGN ไม่มีไข้สูง/ตัวเหลือง\n- ไม่มีหลักฐานการอุดตัน\n- HRS ต้องมี cirrhosis และ U Na ต่ำมาก\n- TTP ต้องมี MAHA/schistocyte\n\nรักษา: penicillin G หรือ ceftriaxone + ดูแลน้ำ/เกลือแร่ (อิงตำรา)",
         "Leptospirosis: non-oliguric AKI + K ต่ำ + ตับ", "Leptospirosis AKI", R("Interstitial nephritis (ลายมือ)"), BASE + [AIN, LEPTO]),
    ], BASE + [AIN, ADR, LEPTO],
    imgs=IMGS(
        IM(3, "AIN — interstitial infiltrate (สไลด์ p24)", "ภาพชิ้นเนื้อไตย้อม H&E มี glomerulus อยู่ซ้ายล่าง ด้านขวามีเซลล์อักเสบจำนวนมากแทรกระหว่างท่อไต เส้นดำลากชี้กลุ่มเซลล์ที่มีแกรนูลสีแดงส้ม",
           q="ชิ้นเนื้อไตของผู้ป่วยที่ Cr ขึ้นหลังเริ่มยาปฏิชีวนะ 10 วัน — เซลล์ที่เส้นดำชี้คืออะไร และบอกอะไร",
           quiz="**คำตอบ:** **eosinophil** ใน interstitium ร่วมกับ lymphocyte จำนวนมาก = **acute interstitial nephritis** · ✍️ อาจารย์: \"eosinophil → จาก drug\" · **จุดที่ต้องเห็น:** เซลล์อักเสบอยู่ **ระหว่างท่อไต** ไม่ใช่ในกระจุก glomerulus (glomerulus ซ้ายล่างดูปกติ) · **ทำต่อ:** หยุดยาที่สงสัย ± steroid"),
        IM(4, "WBC cast และ eosinophiluria (สไลด์ p26)", "ภาพสองภาพจากสไลด์ ภาพ a ตะกอนปัสสาวะมี cast ยาวสองอันที่ภายในเต็มไปด้วยเม็ดเลือดขาว ลูกศรชี้ cast หัวลูกศรชี้เม็ดเลือดขาวเดี่ยว ภาพ b ย้อมสีเห็นกลุ่มเซลล์ที่มีแกรนูลสีชมพูแดง ลูกศรชี้",
           q="ตะกอนปัสสาวะของผู้ป่วย AKI หลังได้ penicillin — ภาพ a และ b คืออะไร",
           quiz="**คำตอบ:** **(a) WBC cast** — เม็ดเลือดขาวอัดในแม่พิมพ์ Tamm–Horsfall = การอักเสบเกิด **ในเนื้อไต** (AIN หรือ pyelonephritis) ไม่ใช่ในกระเพาะปัสสาวะ · **(b) eosinophiluria** — ย้อม Hansel's stain เห็น eosinophil แกรนูลแดง · **ใช้อย่างไร:** WBC cast + eosinophiluria > 5% + ไม่มี RBC cast ชวน **AIN จากยา** (สไลด์ p25–27) · culture แยก pyelonephritis")))

# ═════════════════════════════════════════════ 9
sec("nephro-aki-09", "Intrinsic (4) — acute tubular necrosis (ATN)",
    "ATN: ischemia (pre-renal นาน) · nephrotoxin (✍️ gentamicin, contrast, acyclovir) · pigment · GFR ตก 3 ทาง: cast อุด · backleak · TGF · UA: สไลด์ bland / ตำรา muddy brown granular cast · 3 ระยะ: initiation · maintenance · recovery (polyuria)", 10,
"""### สาเหตุ (สไลด์ p28)
- **Renal ischemia** (prolonged pre-renal) — ผ่าตัดใหญ่ ช็อก เสียเลือด sepsis
- **Nephrotoxins** — **aminoglycosides** (✍️ gentamicin) · **radiocontrast** · ✍️ **acyclovir**
- **Pigmenturia** — **myoglobinuria** (✍️ rhabdo) · **hemoglobinuria** (✍️ PNH)
- รายละเอียด nephrotoxin อยู่หัวข้อ 10 · pigment หัวข้อ 11

[[img:i05]]

### ทำไม GFR ตกใน ATN
เซลล์ **proximal tubule (S3)** และ **medullary thick ascending limb** ใช้ออกซิเจนมาก แต่อยู่ในบริเวณที่ออกซิเจนต่ำ (outer medulla) จึงเสียหายก่อน
1. **Cast obstruction** — เซลล์ที่หลุด + Tamm–Horsfall = granular cast อุดท่อ → แรงดันในท่อสูงต้านการกรอง
2. **Backleak** — ผนังท่อที่ไม่มีเซลล์ปกคลุม น้ำกรองรั่วกลับเข้าเลือด
3. **Tubuloglomerular feedback** — Na ที่ดูดกลับไม่ได้ไปถึง macula densa มาก → afferent หด
4. เซลล์เสีย polarity (Na-K ATPase ย้ายไปด้านข้าง) → ดูด Na/น้ำไม่ได้ → **FENa สูง Uosm ~300**

### UA ใน ATN (สไลด์ p32)
- สไลด์: **typical bland sediment** · บาง case proteinuria 1+–2+ (< 500 mg/วัน)
- ถ้าเป็น **rhabdomyolysis หรือ intravascular hemolysis** → **disproportion of RBC vs strip for heme** เช่น protein 1+, RBC 2–3/HPF, WBC 1–2/HPF, **blood 3+** (✍️ วงไว้ → myoglobin/hemoglobin)
- ⚠️ **ความต่างจากตำรา**: ตำราและข้อสอบส่วนใหญ่ใช้ **muddy brown granular cast + renal tubular epithelial cell (RTE) / RTE cast** เป็นลักษณะเด่นของ ATN (พบ ~70–80% ของ ATN) — ถ้าโจทย์ถาม \"cast ที่พบใน ATN\" ให้ตอบ muddy brown granular cast

### ระยะของ ATN และ non-oliguric ATN
[[fig:phases]]

- **non-oliguric ATN** (ปัสสาวะ > 400 mL/วัน) พบบ่อยใน nephrotoxin (aminoglycoside, contrast) · พยากรณ์ดีกว่า · สไลด์ p50 จัดเป็น ATN ที่ FENa อาจต่ำ
- **ระยะฟื้นตัว**: ปัสสาวะมาก เสีย Na K Mg PO4 — ให้น้ำ/เกลือแร่ตาม balance และค่อย ๆ ลดลง (การให้ตามปัสสาวะทุก mL ไปเรื่อย ๆ ทำให้ diuresis ไม่หยุด)

#### ทำไมถึงมีอาการนี้
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Muddy brown granular cast + RTE cell** | เซลล์ท่อไตตายหลุดลงท่อ ปนกับ Tamm–Horsfall | ATN (pre-renal มีแค่ hyaline cast) |
| **FENa > 2%, U Na > 40** | เซลล์ดูด Na กลับไม่ได้ | pre-renal < 1% |
| **Uosm ~300, SpGr 1.010–1.015** | ทำ medullary gradient และตอบ ADH ไม่ได้ (isosthenuria) | pre-renal > 400–500 |
| **ให้น้ำแล้ว Cr ไม่ลง** | ต้องรอเซลล์ใหม่ 1–3 สัปดาห์ | การให้น้ำต่อทำให้น้ำเกิน |
| **Polyuria ช่วงฟื้น** | เซลล์ใหม่ยังดูดกลับไม่เก่ง + urea ที่คั่งเป็น osmotic diuresis | ต้องดูแล K Mg PO4 |
""",
    ["ATN: ischemia (pre-renal นาน) · nephrotoxin (✍️ gentamicin, contrast, acyclovir) · pigment",
     "GFR ตก 3 ทาง: cast อุดท่อ · backleak · TGF หด afferent",
     "UA: สไลด์เขียน bland · ข้อสอบ/ตำรา: muddy brown granular cast + RTE cell",
     "FENa > 2% · Uosm ~300 · BUN/Cr ~10",
     "ระยะฟื้นตัว = polyuria เสีย K Mg PO4"],
    [mcq(N(17), "A 71-year-old man had a prolonged episode of hypotension (BP 70/40 mmHg for about 2 hours) during emergency repair of a ruptured abdominal aortic aneurysm. On day 2 his blood pressure is normal, but urine output is 250 mL/day and creatinine has risen from 1.1 to 3.9 mg/dL. Urine shows numerous muddy brown granular casts and renal tubular epithelial cells. Which mechanism best explains the persistently low GFR despite restored blood pressure?",
         ["Tubular obstruction by casts, backleak of filtrate across denuded tubules and tubuloglomerular feedback-mediated afferent vasoconstriction", "Immune complex deposition in the glomerular basement membrane", "Persistent pre-renal hypoperfusion that will resolve with more intravenous fluid", "Eosinophilic infiltration of the interstitium", "Bilateral ureteric obstruction from the aortic graft"], 0,
         "หลังความดันกลับมาแล้ว GFR ยังต่ำเพราะ **เซลล์ท่อไตตายแล้ว** (ischemic ATN — สไลด์ p28 renal ischemia) · GFR ตกจาก **3 กลไก**: **cast อุดท่อ** (muddy brown granular cast) · **backleak** น้ำกรองรั่วผ่านผนังที่ไม่มีเซลล์ · **TGF** Na ไปถึง macula densa มาก → afferent หด\n\n- immune complex = GN (ต้องมี RBC cast)\n- ความดันปกติแล้วและมี granular cast ไม่ใช่ pre-renal — ให้น้ำต่อจะน้ำเกิน\n- eosinophil = AIN\n- ควรตรวจ ultrasound ตัดการอุดตันด้วย แต่ภาพ UA บอก ATN",
         "ความดันกลับแล้ว GFR ยังต่ำ = cast + backleak + TGF", "ATN mechanism", R("Acute tubular necrosis"), BASE + [OLIG]),
     mcq(N(18), "A 60-year-old woman with ischaemic ATN after septic shock was oliguric for 10 days. On day 12 her urine output increases to 4.5 L/day. Creatinine has started to fall (5.2 to 4.6 mg/dL). Serum K 3.1 mEq/L, Mg 1.4 mg/dL, phosphate 2.0 mg/dL, Na 141 mEq/L. She is euvolaemic. What is the most appropriate management?",
         ["Replace potassium, magnesium and phosphate and give maintenance fluid guided by daily balance and weight, tapering as urine output falls", "Start haemodialysis because the creatinine is still above 4 mg/dL", "Give desmopressin to reduce urine output", "Restrict all fluids to 1 L/day to stop the diuresis", "Give furosemide to accelerate recovery"], 0,
         "นี่คือ **ระยะฟื้นตัว (polyuric phase) ของ ATN**: เซลล์ใหม่ปกคลุมท่อแต่ยังดูดน้ำ/เกลือกลับไม่เก่ง + urea ที่คั่งเป็น osmotic diuresis → ปัสสาวะมาก **เสีย K Mg PO4**\n\nจัดการ: **ทดแทนเกลือแร่** และให้น้ำตาม balance/น้ำหนัก แล้วค่อย ๆ ลด (ถ้าให้ตามปัสสาวะทุก mL ไปเรื่อย ๆ diuresis จะไม่หยุด)\n\n- Cr กำลังลดและไม่มีข้อบ่งชี้ dialysis (AEIOU)\n- ไม่ใช่ diabetes insipidus — desmopressin ไม่ช่วยและอาจทำ Na ต่ำ\n- จำกัดน้ำจะทำให้ขาดน้ำและไตบาดเจ็บซ้ำ\n- furosemide ไม่ได้เร่งการฟื้น",
         "ATN ระยะฟื้น: polyuria → ทดแทน K Mg PO4 และน้ำตาม balance", "ATN recovery phase", R("Acute tubular necrosis", "ตำรา — phases of ATN"), BASE + [POLY, LYTE]),
    ], BASE + [OLIG, OLIG_B], figs={"phases": F.atn_phases()},
    imgs=IMGS(IM(5, "ATN — ชิ้นเนื้อไต (สไลด์ p29)", "ภาพชิ้นเนื้อไตย้อม PAS เห็นท่อไตหลายท่อที่เซลล์บุผิวแบนบาง ขอบ brush border หายไป มีเศษเซลล์หลุดอยู่ในโพรงท่อ และบางท่อโพรงกว้าง",
                    q="ชิ้นเนื้อไตของผู้ป่วยที่ความดันตกนานระหว่างผ่าตัด — ลองหาความผิดปกติของท่อไต",
                    quiz="**คำตอบ:** **acute tubular necrosis** · **จุดที่ต้องเห็น:** เซลล์บุท่อ **แบนบาง ไม่มี brush border** · **เศษเซลล์ที่หลุดลอยในโพรงท่อ** (ต้นกำเนิดของ granular cast) · โพรงท่อกว้างผิดปกติ · interstitium แทบไม่มีเซลล์อักเสบ (ต่างจาก AIN) · **กลไก:** ขาดออกซิเจน → เซลล์เสีย polarity หลุดจาก basement membrane → cast อุดและ backleak")))

# ═════════════════════════════════════════════ 10
sec("nephro-aki-10", "Nephrotoxins — aminoglycoside · contrast · acyclovir · lithium และยาอื่น",
    "Aminoglycoside: non-oliguric ATN หลัง 5–10 วัน + Mg/K ต่ำ · Contrast: หลอดเลือดหด + พิษตรง · เสี่ยงจริงเมื่อ eGFR < 30 · ป้องกันด้วย IV isotonic fluid (ACR–NKF 2020) · NAC/bicarbonate ไม่ช่วย · Lithium → nephrogenic DI", 9,
"""สไลด์ p28 ระบุ nephrotoxin ของ ATN: **aminoglycosides (✍️ gentamicin), radiocontrast** และ ✍️ **acyclovir** · หัวข้อนี้รวบรวมกลไกและการป้องกัน — ส่วนที่เกินสไลด์อิง **KDIGO 2012** และ **ACR–NKF 2020**

[[fig:toxmap]]

### Aminoglycoside (gentamicin, amikacin)
- ถูกกรองแล้วจับ **megalin** ที่ proximal tubule → สะสมใน lysosome (phospholipidosis) → เซลล์ตาย
- ลักษณะ: **non-oliguric** · Cr ขึ้นหลังได้ยา **5–10 วัน** · **Mg และ K ต่ำ** (เสียทางท่อไต) · หูเสื่อมร่วม
- ลดเสี่ยง: ให้ **วันละครั้ง** (uptake อิ่มตัว) · ระยะสั้นที่สุด · วัดระดับยา · เลี่ยงการใช้ร่วม vancomycin/contrast/NSAID

### Contrast-associated AKI
- กลไก: **หลอดเลือดในไตหด → outer medulla ขาด O2** + **พิษตรงต่อเซลล์ท่อไต** + ความหนืด
- Cr ขึ้นใน **24–72 ชม.** หลังฉีด ส่วนใหญ่กลับคืนใน 1–2 สัปดาห์ · สไลด์ p50 จัดเป็น ATN ที่ FENa อาจต่ำ
- **ACR–NKF 2020** (IV contrast): เสี่ยงจริงเมื่อ **eGFR < 30** หรือมี **AKI** อยู่ → ให้ **IV isotonic fluid (normal saline) ก่อน–หลัง** ถ้าไม่มีข้อห้าม · eGFR 30–44 พิจารณาเป็นราย · ≥ 45 ไม่ต้อง
- ใช้ contrast ชนิด low/iso-osmolar **ขนาดน้อยที่สุด** · งด NSAID และยาที่ทำร้ายไต
- **ไม่แนะนำ**: N-acetylcysteine · sodium bicarbonate แทนน้ำเกลือ (PRESERVE trial ไม่ต่าง) · ฟอกเลือดป้องกัน
- **Metformin**: งดเมื่อ **eGFR < 30 หรือมี AKI** ตั้งแต่ก่อน/ขณะฉีด และ 48 ชม. หลัง แล้วตรวจ Cr ซ้ำก่อนเริ่มใหม่ (ACR Manual on Contrast Media) — เหตุผลคือกลัว lactic acidosis ถ้าไตวาย ไม่ใช่ metformin ทำร้ายไต
- ไม่ควรเลื่อน CT ที่จำเป็นต่อชีวิตเพราะกลัวไต · ดูเรื่อง contrast เพิ่มในคาบ **Imaging**

### ยาอื่นที่ควรรู้
| ยา | กลไก/ลักษณะ |
|---|---|
| **Acyclovir IV** (✍️) | ตกผลึกในท่อไต (หัวข้อ 12) ± ATN |
| **Amphotericin B** | หลอดเลือดหด + พิษต่อเยื่อหุ้มเซลล์ · K Mg ต่ำ · distal RTA |
| **Cisplatin** | ATN · Mg ต่ำมาก |
| **Vancomycin** (โดยเฉพาะร่วม piperacillin-tazobactam) | ATN/cast nephropathy · ติดตามระดับยา |
| **Calcineurin inhibitor** | หด afferent (คล้าย NSAID) · TMA |
| **Lithium** | เข้าเซลล์ collecting duct ทาง ENaC → ไม่ตอบ ADH = **nephrogenic DI** (ปัสสาวะมาก Uosm ต่ำ ไม่ขึ้นหลัง desmopressin) · ใช้นานเกิด CKD |

#### ทำไมถึงมีอาการนี้
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Aminoglycoside: AKI ไม่ปัสสาวะน้อย + Mg ต่ำ** | เซลล์ PT/thick ascending limb เสีย → ดูด Mg/K กลับไม่ได้ ส่วนการทำเข้มข้นเสียด้วย | ATN จากยาต่างจาก ischemic ที่มักปัสสาวะน้อย |
| **Contrast: Cr ขึ้นวันที่ 1–3 แล้วลง** | vasoconstriction + พิษชั่วคราว | Cr ขึ้นหลัง 5 วันหรือมีผื่น/eosinophil → คิด atheroembolic disease |
| **Lithium: ปัสสาวะมาก Na สูงเล็กน้อย** | collecting duct ไม่ตอบ ADH | ไม่ตอบ desmopressin = nephrogenic DI |
""",
    ["Aminoglycoside: non-oliguric ATN หลัง 5–10 วัน · Mg/K ต่ำ · ให้วันละครั้ง",
     "Contrast AKI: ACR–NKF 2020 เสี่ยงจริงเมื่อ eGFR < 30 หรือมี AKI → IV isotonic fluid ก่อน–หลัง",
     "NAC, NaHCO3 และฟอกเลือดป้องกัน ไม่แนะนำ",
     "Metformin: งดเมื่อ eGFR < 30 หรือ AKI จนตรวจ Cr ซ้ำ 48 ชม.",
     "Lithium → nephrogenic DI (ไม่ตอบ desmopressin)"],
    [mcq(N(19), "A 72-year-old woman receives intravenous gentamicin 5 mg/kg once daily with ampicillin for enterococcal pyelonephritis. On day 8 her creatinine rises from 0.8 to 2.1 mg/dL. Urine output is 1.6 L/day. Serum magnesium 1.2 mg/dL and potassium 3.2 mEq/L. Which feature is most characteristic of this type of kidney injury?",
         ["Non-oliguric acute tubular necrosis appearing after several days of therapy, with renal magnesium and potassium wasting", "Immediate oliguric AKI within hours of the first dose", "Glomerular injury with RBC casts and nephrotic-range proteinuria", "Crystal deposition causing bilateral hydronephrosis", "Allergic interstitial nephritis with rash and eosinophilia"], 0,
         "**Aminoglycoside nephrotoxicity** (สไลด์ p28 ✍️ gentamicin): ยาจับ **megalin** แล้วสะสมใน proximal tubule → ATN แบบ **non-oliguric** ที่ปรากฏหลังได้ยา **5–10 วัน** ร่วมกับ **Mg และ K ต่ำ** จากท่อไตรั่ว\n\n- ไม่เกิดทันทีหลังเข็มแรก\n- ไม่ทำร้าย glomerulus (ไม่มี RBC cast)\n- ไม่ตกผลึก\n- ไม่ใช่ปฏิกิริยาแพ้\n\nจัดการ: หยุด/เปลี่ยนยา ทดแทน Mg K ติดตามการได้ยิน",
         "Aminoglycoside: non-oliguric ATN วันที่ 5–10 + Mg/K ต่ำ", "Aminoglycoside", R("Acute tubular necrosis (ลายมือ)"), BASE + [ADR]),
     mcq(N(20), "A 64-year-old man with type 2 diabetes and CKD (eGFR 26 mL/min/1.73 m²) needs a contrast-enhanced CT for suspected pancreatic cancer. He takes metformin 500 mg twice daily. Which is the most appropriate plan for his metformin?",
         ["Withhold metformin at the time of the contrast scan and for 48 hours afterwards, restarting only after kidney function is rechecked and stable", "Continue metformin unchanged because iodinated contrast does not interact with it", "Stop metformin 7 days before the scan and restart the next day without checking creatinine", "Give intravenous sodium bicarbonate so metformin can be continued", "Cancel the CT scan because contrast is absolutely contraindicated with metformin"], 0,
         "ACR Manual on Contrast Media: ผู้ที่ **eGFR < 30 หรือมี AKI** ให้ **งด metformin ตั้งแต่เวลาฉีด และ 48 ชม. หลัง** แล้ว **ตรวจไตซ้ำ** ก่อนเริ่มใหม่ — เหตุผลคือถ้าเกิด contrast-associated AKI metformin จะคั่งและเสี่ยง **lactic acidosis** (metformin ไม่ได้ทำร้ายไตเอง)\n\nเขาควรได้ **IV isotonic fluid ก่อน–หลัง** และ contrast ขนาดน้อยที่สุดด้วย (ACR–NKF 2020, eGFR < 30)\n\n- ให้ต่อไม่ได้ในคนที่ eGFR < 30\n- หยุด 7 วันไม่จำเป็น และต้องตรวจ Cr ก่อนเริ่มใหม่\n- bicarbonate ไม่ป้องกันและไม่เกี่ยวกับ metformin\n- ไม่ควรยกเลิก CT ที่จำเป็นต่อการวินิจฉัย\n\n(เนื้อหานี้อิงแนวทาง ไม่อยู่ในสไลด์ — eGFR < 30 เป็นข้อห้ามใช้ metformin ทั่วไปอยู่แล้ว)",
         "Metformin + contrast: งดเมื่อ eGFR < 30/AKI ตรวจไตซ้ำ 48 ชม.", "Contrast and metformin", ["ACR Manual on Contrast Media", "ACR–NKF consensus on IV iodinated contrast in kidney disease 2020"], BASE + [ADR, PK]),
    ], BASE + [ADR, PK], figs={"toxmap": F.nephrotox_map()}, src=SRC_ADD)

# ═════════════════════════════════════════════ 11
sec("nephro-aki-11", "Pigment nephropathy — rhabdomyolysis · hemoglobinuria · ปัสสาวะแดง/น้ำตาล",
    "Dipstick blood 3+ แต่ RBC 0–3/HPF = myoglobin/hemoglobin · plasma ใส = myoglobin · แดง = hemoglobin · ✍️ amphetamine, PNH · CK ยืนยัน rhabdo · ให้ isotonic fluid เร็ว · heme-negative red urine: rifampicin, beet, porphyria · ✍️ ส่ง UA ใน 2 ชม.", 10,
"""### Rhabdomyolysis — กลไก 3 ทาง
- สาเหตุ: crush/บาดเจ็บ · ออกกำลังหนัก · ชัก · **ยา: statin + fibrate (gemfibrozil)** · ✍️ **amphetamine** (\"ถ้า BP สูง 220 สงสัยไว้ก่อน\") · แอลกอฮอล์ · heat stroke · K/PO4 ต่ำ · ติดเชื้อ
- กล้ามเนื้อสลายปล่อย **myoglobin, K, PO4, urate, CK, AST** · Ca ไปเกาะเนื้อตาย → **Ca ต่ำช่วงแรก**
- heme ทำร้ายไต: **① จับ NO → หลอดเลือดไตหด** (+ น้ำไปอยู่ในกล้ามเนื้อที่บวม) · **② เหล็กทำ oxidative injury ต่อ proximal tubule** · **③ myoglobin + Tamm–Horsfall เป็น cast อุดท่อ** (ตกตะกอนง่ายในปัสสาวะกรด)

[[img:i06]]

### Hemoglobinuria
- ✍️ **PNH** — ปัสสาวะดำช่วงเช้า (hemolysis ตอนกลางคืน) · G6PD deficiency (primaquine, dapsone, ถั่วปากอ้า, ติดเชื้อ) · มาลาเรีย · เลือดผิดหมู่ · งูแมวเซา (Russell's viper) · TMA
- hemoglobin อิสระเกินกำลังจับของ haptoglobin → ถูกกรอง → ATN · เหล็กสะสมเป็น **hemosiderin** ในเซลล์ท่อไต

[[img:i07]]

### UA ใน pigment ATN (สไลด์ p32)
**Disproportion of RBC vs strip for heme**: ตัวอย่างในสไลด์ — protein 1+, **RBC 2–3/HPF**, WBC 1–2/HPF, **blood 3+** (✍️ วงสองค่านี้ → myoglobin / hemoglobin)
- dipstick ใช้ **peroxidase activity ของ heme** จึงบวกทั้ง RBC, hemoglobin และ myoglobin แต่กล้องเห็นเฉพาะ RBC ที่ยังเป็นเซลล์

### Approach to red or brown urine (สไลด์ p33)
[[img:i08]]

**Heme-negative red urine (สไลด์ p34)**
| กลุ่ม | ตัวอย่าง |
|---|---|
| **ยา** | doxorubicin · chloroquine · deferoxamine · ibuprofen · nitrofurantoin · **rifampin/rifampicin** · phenothiazine · levodopa · methyldopa · primaquine · phenytoin |
| **อาหาร/สี** | beets (บางคน) · blackberries · food coloring |
| **Metabolites** | bile pigments · methemoglobin · porphyria · *Serratia marcescens* infection |

### การดูแล rhabdomyolysis (ตำรา — ไม่อยู่ในสไลด์)
- ยืนยันด้วย **CK** (มัก > 5 เท่าของค่าปกติ · เสี่ยง AKI สูงเมื่อ > 5,000–15,000 U/L) · ตรวจ K, PO4, Ca, urate, HCO3, ECG
- **หยุดสาเหตุ** (statin/fibrate) · **isotonic fluid เร็วและมาก** ตั้งแต่แรก เป้าปัสสาวะ ~200–300 mL/ชม. (ระวังน้ำเกินถ้า oliguric แล้ว)
- **แก้ K สูง** ตามหัวข้อ 16 · **ไม่ให้ Ca แก้ Ca ต่ำ** ถ้าไม่มีอาการ/ไม่มี K สูงที่ ECG ผิด (Ca จะไปเกาะกล้ามเนื้อเพิ่มและ Ca สูงช่วงฟื้น)
- bicarbonate/mannitol ไม่มีหลักฐานว่าดีกว่าน้ำเกลือ · **dialysis** เมื่อ K สูง กรด หรือน้ำเกินที่ดื้อต่อยา

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **ปัสสาวะสีน้ำตาลโค้ก** | myoglobin/hemoglobin ในปัสสาวะ | dipstick heme บวก |
| **Blood 3+ แต่ RBC 0–3** | dipstick ตรวจ heme ไม่ได้นับเซลล์ | pigment vs hematuria จริง |
| **พลาสมาใส vs ชมพู** | myoglobin 17 kDa ถูกกรองเร็ว ไม่ค้างในพลาสมา · hemoglobin จับ haptoglobin ค้างในเลือด | ใส = myoglobin · แดง = hemoglobin |
| **AST > ALT, LDH สูง** | AST อยู่ในกล้ามเนื้อมาก | อย่าหลงไปคิดโรคตับ |
| **Ca ต่ำ → ภายหลัง Ca สูง** | Ca ไปเกาะเนื้อตาย แล้วปล่อยกลับช่วงฟื้น + calcitriol เพิ่ม | ไม่ให้ Ca ถ้าไม่จำเป็น |
| **K สูงเร็วมาก** | K ในกล้ามเนื้อทะลักออก + ไตขับไม่ได้ + กรด | ECG ทันที |
""",
    ["Dipstick blood 3+ แต่ RBC น้อย = pigment (myoglobin/hemoglobin)",
     "พลาสมาใส = myoglobin · พลาสมาแดง = hemoglobin",
     "Heme ทำร้ายไต 3 ทาง: หลอดเลือดหด · เหล็ก oxidative · cast",
     "Rhabdo: CK ยืนยัน · หยุดสาเหตุ (statin+gemfibrozil, ✍️ amphetamine) · isotonic fluid เร็ว · ไม่ให้ Ca ถ้าไม่จำเป็น",
     "Heme-negative red urine: rifampicin, beet, porphyria, phenazopyridine · ✍️ ส่ง UA ใน 2 ชม."],
    [mcq(N(21), "A 24-year-old man is brought in after a prolonged generalised seizure. His urine is reddish-brown. Dipstick: blood 3+; microscopy: 0–2 RBC/HPF. After centrifugation the urine supernatant remains red-brown and the patient's plasma is clear (not pink). Which pigment is most likely present and why?",
         ["Myoglobin, because it is small and rapidly filtered so it does not accumulate in plasma", "Haemoglobin, because it binds haptoglobin and is cleared rapidly into urine", "Bilirubin, because it gives a positive dipstick blood reaction", "Porphyrins, because they cause a positive heme dipstick", "Intact red blood cells that settled in the sediment"], 0,
         "ใช้แผนผังสไลด์ p33: ส่วนใสยังแดง → **dipstick heme บวก** → myoglobin หรือ hemoglobin → ดู **สีพลาสมา**: **ใส = myoglobinuria**\n\nmyoglobin โมเลกุลเล็ก (~17 kDa) จับโปรตีนในพลาสมาน้อย → **ถูกกรองออกเร็ว** พลาสมาจึงไม่เปลี่ยนสี · ส่วน **hemoglobin** จับ haptoglobin ซึ่งใหญ่ ค้างในเลือดจนพลาสมาเป็นสีชมพู ก่อนจะล้นมาในปัสสาวะเมื่อ haptoglobin อิ่มตัว\n\n- bilirubin และ porphyrin ไม่ทำให้ dipstick heme บวก (porphyria อยู่ในกลุ่ม heme-negative)\n- RBC ที่ตกตะกอนจะทำให้ **ตะกอน** แดง ส่วนใสใส · และกล้องจะเห็น RBC มาก\n\nหลังชัก → rhabdomyolysis → ส่ง CK",
         "พลาสมาใส + heme บวก = myoglobin", "Red/brown urine approach", R("Approach to the patient with red or brown urine"), BASE + [HEMAT, UA]),
     mcq(N(22), "A 30-year-old man is extracted after his legs were trapped under rubble for 6 hours. CK is 48,000 U/L, creatinine 2.4 mg/dL, K 5.4 mEq/L, phosphate 7.6 mg/dL and corrected calcium 6.9 mg/dL. He has no tetany or seizures, and ECG shows a normal QT interval without peaked T waves. Which of the following is the most appropriate management of his hypocalcaemia?",
         ["Do not give intravenous calcium now; treat the rhabdomyolysis with aggressive isotonic fluid and monitor calcium", "Give intravenous calcium gluconate infusion to normalise serum calcium", "Give oral calcium carbonate 1 g three times daily with meals", "Give calcitriol to increase intestinal calcium absorption", "Give intravenous sodium bicarbonate to raise ionised calcium"], 0,
         "Ca ต่ำใน rhabdomyolysis เกิดจาก **Ca ไปจับกับ phosphate และเกาะในกล้ามเนื้อที่ตาย** · การให้ Ca เมื่อ **ไม่มีอาการ** จะไปเกาะเนื้อตายเพิ่ม และเสี่ยง **Ca สูงช่วงฟื้น** (Ca ถูกปล่อยกลับ + calcitriol เพิ่ม)\n\n→ **ไม่ให้ Ca** เว้นแต่มีอาการ (tetany ชัก) หรือมี **K สูงที่ ECG ผิด** (ให้ Ca gluconate เพื่อปกป้องหัวใจ)\n\nจัดการหลัก: **isotonic fluid เร็วและมาก** ติดตาม K PO4 Ca และ ECG\n\n- calcitriol ทำให้ Ca-PO4 product สูงและเกาะเนื้อเยื่อมากขึ้น\n- bicarbonate ทำให้ ionized Ca **ลดลง** (Ca จับ albumin มากขึ้นในภาวะด่าง)\n\n(อิงตำรา ไม่อยู่ในสไลด์)",
         "Rhabdo + Ca ต่ำไม่มีอาการ → ไม่ให้ Ca", "Rhabdomyolysis calcium", R("ATN from rhabdomyolysis", "Bosch X, et al. Rhabdomyolysis and acute kidney injury. N Engl J Med 2009"), BASE + [LYTE, MYO]),
    ], BASE + [HEMAT, UA, MYO, HCRISIS],
    imgs=IMGS(
        IM(6, "ATN from rhabdomyolysis — myoglobin cast (สไลด์ p30)", "ภาพชิ้นเนื้อไตย้อม H&E ท่อไตหลายท่อมีก้อนตะกอนสีส้มแดงเป็นเม็ดอยู่ในโพรง มีกล่องข้อความ Myoglobin deposit in renal tubule มุมขวาล่าง",
           cap="**Myoglobin deposit (pigment cast) ในท่อไต** — ก้อนสีส้มแดงเป็นเม็ดอุดโพรงท่อ คือกลไกที่ ③ (cast อุดท่อ) · เซลล์ท่อไตรอบ ๆ แบนบาง (ATN) · ในผู้ป่วยจะเห็น dipstick blood บวกแต่ RBC น้อย"),
        IM(7, "ATN จาก PNH — hemosiderin ในท่อไต (สไลด์ p31)", "ภาพชิ้นเนื้อไตย้อม H&E ท่อไตจำนวนมากมีเม็ดสีน้ำตาลเข้มเกือบดำสะสมในเซลล์บุท่อ มี glomerulus อยู่มุมซ้ายล่าง กล่องข้อความ Hemosiderin deposit in renal tubule",
           q="ชิ้นเนื้อไตของผู้ป่วยหญิงที่ปัสสาวะสีดำตอนเช้าเป็นช่วง ๆ — เม็ดสีน้ำตาลดำในท่อไตคืออะไร และมาจากไหน",
           quiz="**คำตอบ:** **hemosiderin** ในเซลล์ท่อไต จาก **paroxysmal nocturnal hemoglobinuria (PNH)** · **กลไก:** RBC ขาด CD55/CD59 จึงถูก complement ทำลายในหลอดเลือด (เด่นช่วงกลางคืน → ✍️ ปัสสาวะดำตอนเช้า) → hemoglobin อิสระถูกกรอง → เซลล์ proximal tubule ดูดกลับและเก็บเหล็กเป็น hemosiderin → oxidative injury = ATN · ปัสสาวะมี hemosiderin ได้แม้ไม่มี hemolysis ช่วงนั้น"),
        IM(8, "Approach to red or brown urine (สไลด์ p33)", "แผนผังสีส้มจากสไลด์ ปั่นปัสสาวะ ถ้าตะกอนแดงคือ hematuria ถ้าส่วนใสแดงให้ตรวจ dipstick heme ผลลบคือ beeturia phenazopyridine porphyria ผลบวกคือ myoglobin หรือ hemoglobin แล้วดูสีพลาสมา ใสคือ myoglobinuria แดงคือ hemoglobinuria",
           cap="แผนผังที่อาจารย์ดัดแปลงจาก UpToDate: **ปั่นปัสสาวะก่อน** — ตะกอนแดง = **hematuria** (มี RBC) · ส่วนใสแดง → **dipstick heme** · ลบ = beeturia, phenazopyridine, porphyria และยาในตาราง p34 · บวก = myoglobin หรือ hemoglobin → **สีพลาสมา: ใส = myoglobinuria · แดง = hemoglobinuria** · ✍️ \"ต้องเอา UA ภายใน 2 ชม.\" — ปัสสาวะที่ตั้งทิ้ง RBC แตกเป็น hemoglobin และ cast สลาย ทำให้แปลผลผิด")))

# ═════════════════════════════════════════════ 12
sec("nephro-aki-12", "Intrarenal obstruction — crystal nephropathy (uric acid · oxalate · ยา)",
    "Crystal: uric (TLS) · oxalate (✍️ ethylene glycol, มะเฟือง, ตะลิงปลิง, Vit C) · MTX · acyclovir · triamterene · sulfonamide · ✍️ ciprofloxacin · indinavir (✍️ HIV → นิ่ว) · ปัสสาวะน้อย + pH เหมาะ · UA bland + ผลึก · ให้น้ำ ปรับขนาดยา", 9,
"""### Intrinsic renal: intrarenal obstruction (สไลด์ p35)
อ.วรรณิยาจัดหัวข้อนี้ว่า **\"Intrinsic renal : intrarenal obstruction (Post-renal AKI)\"** — ผลึกอุดท่อไตจาก **ภายใน** ไต
- **Crystal deposition**: **uric · oxalate · methotrexate · acyclovir · triamterene · sulfonamides**
- ✍️ oxalate ⇒ \"**common สุดของ drug → ATB ⇒ ciprofloxacin**\" · ผลไม้: **มะเฟือง (star fruit)** · ผัก: **ตะลิงปลิง** · **Vit C เยอะ**
- ✍️ calcium oxalate: **ethylene glycol** common · รูป **envelope** และ **dumbbell**
- ✍️ indinavir → **HIV ⇒ renal stone**

### ทำไมผลึกถึงตกในท่อไต
1. **ความเข้มข้นสูง** — ปัสสาวะน้อย/ขาดน้ำ ยาขนาดสูง ฉีดเร็ว
2. **pH ปัสสาวะ** — **uric acid, methotrexate ตกในปัสสาวะกรด** · **ciprofloxacin, indinavir, calcium phosphate ตกในปัสสาวะด่าง**
3. สารตั้งต้นมาก — tumor lysis (urate, phosphate) · ethylene glycol → oxalate · มะเฟือง/ตะลิงปลิง (oxalate สูง โดยเฉพาะกินน้ำคั้นมากหรือมี CKD อยู่เดิม)

[[img:i09]]

[[img:i10]]

[[img:i11]]

### UA (สไลด์ p40)
- **Typical: bland sediment** · protein 1+–2+ (< 500 mg/วัน) · **เห็นผลึก** ในปัสสาวะสด

### ตัวอย่างที่ออกข้อสอบบ่อย (ตำรา)
| ภาวะ | ลักษณะ | ป้องกัน/รักษา |
|---|---|---|
| **Tumor lysis syndrome** | lymphoma/leukemia เริ่มเคมีบำบัด 1–3 วัน · **K PO4 urate สูง Ca ต่ำ** · uric acid + CaPO4 ตกผลึก | ให้น้ำมาก · allopurinol ก่อนเริ่มยา · **rasburicase** ถ้าเสี่ยงสูง/urate สูง |
| **Acyclovir IV** | Cr ขึ้นใน 24–48 ชม. · ผลึกรูปเข็ม birefringent | ให้น้ำ · หยดช้า 1–2 ชม. · ปรับขนาดตาม GFR |
| **Methotrexate ขนาดสูง** | ตกในปัสสาวะกรด | ให้น้ำ + ทำปัสสาวะด่าง · glucarpidase |
| **Ethylene glycol** | AG + osmolar gap สูง · CaOx (envelope) · Ca ต่ำ | fomepizole/ethanol · hemodialysis |
| **มะเฟือง/ตะลิงปลิง** | acute oxalate nephropathy · ผู้ป่วย CKD อาจมีสะอึก/ชัก (neurotoxin ในมะเฟือง) | หยุดกิน · dialysis ถ้ารุนแรง |

#### ทำไมถึงมีอาการนี้
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **AKI ใน 1–3 วันหลังเริ่มยา/เคมีบำบัด** | ผลึกเกิดทันทีเมื่อเกินจุดอิ่มตัว | ต่างจาก AIN (7–10 วัน) |
| **ปวดสีข้าง/ปัสสาวะเป็นเลือดเล็กน้อย** | ผลึกครูดท่อ หรือเป็นนิ่ว (indinavir, sulfadiazine) | UA เห็นผลึก |
| **Ca ต่ำใน TLS / ethylene glycol** | phosphate หรือ oxalate จับ Ca | ใช้ร่วมกับ K/PO4/urate (TLS) หรือ osmolar gap (EG) |
""",
    ["Crystal: uric · oxalate · MTX · acyclovir · triamterene · sulfonamide (+ ✍️ cipro, indinavir)",
     "Uric acid/MTX ตกในปัสสาวะกรด · cipro/indinavir/CaPO4 ตกในปัสสาวะด่าง",
     "✍️ Oxalate: ethylene glycol · มะเฟือง · ตะลิงปลิง · Vit C ขนาดสูง · CaOx = envelope/dumbbell",
     "TLS: K PO4 urate สูง Ca ต่ำ → น้ำ + allopurinol/rasburicase",
     "UA: bland + ผลึก · ป้องกันด้วยน้ำและปรับขนาดยา"],
    [mcq(N(23), "A 46-year-old woman with HSV encephalitis receives intravenous acyclovir 10 mg/kg every 8 hours as a rapid infusion. Her oral intake is poor. On day 3 creatinine rises from 0.8 to 2.3 mg/dL. Urine microscopy shows needle-shaped birefringent crystals and a few WBC. What is the most appropriate management?",
         ["Give intravenous isotonic fluid, infuse acyclovir slowly over 1–2 hours and reduce the dose according to kidney function", "Stop acyclovir permanently and observe the encephalitis", "Start prednisolone for acute interstitial nephritis", "Alkalinise the urine with sodium bicarbonate and continue the same dose", "Perform an urgent kidney biopsy before any change in treatment"], 0,
         "**Acyclovir crystal nephropathy** (สไลด์ p35, p38 ✍️ acyclovir): ยาละลายน้ำต่ำ เมื่อ **ฉีดเร็ว + ขาดน้ำ** ความเข้มข้นในท่อไตเกินจุดอิ่มตัว → **ผลึกรูปเข็ม birefringent** อุดท่อ · มักเกิดใน 24–72 ชม.\n\nจัดการ: **ให้น้ำ · หยดช้า 1–2 ชม. · ปรับขนาดตาม GFR** — HSV encephalitis ยังต้องได้ยาต่อ\n\n- หยุดยาถาวรเสี่ยงต่อสมอง\n- ภาพผลึกไม่ใช่ AIN\n- acyclovir ไม่ได้ขึ้นกับ pH มาก การทำด่างไม่ใช่การรักษามาตรฐาน\n- ไม่จำเป็นต้องเจาะไต",
         "Acyclovir AKI: ให้น้ำ หยดช้า ปรับขนาด — ไม่หยุดยาที่จำเป็น", "Acyclovir crystal", R("Intrarenal obstruction, Drugs induce crystal"), BASE + [ADR, PK]),
     mcq(N(24), "A 55-year-old woman with CKD stage 3 (baseline creatinine 1.6 mg/dL) drank about 1 litre of fresh star fruit juice daily for 3 days as a herbal remedy. She now has nausea, persistent hiccups and oliguria; creatinine is 5.8 mg/dL. Urine microscopy shows many envelope-shaped crystals. What is the most likely mechanism of her AKI?",
         ["Acute oxalate nephropathy from calcium oxalate crystal deposition in the tubules", "Uric acid nephropathy from tumour lysis", "Myoglobin cast nephropathy from rhabdomyolysis", "Drug-induced acute interstitial nephritis", "Pre-renal azotaemia from fruit-induced diarrhoea"], 0,
         "✍️ อาจารย์: oxalate จาก **มะเฟือง (star fruit)** และ **ตะลิงปลิง** · ผลึก **envelope-shaped = calcium oxalate** (✍️ envelope/dumbbell)\n\nมะเฟืองมี oxalate สูง → ถูกขับทางไต ตกผลึกเป็น CaOx ในท่อไต = **acute oxalate nephropathy** · ผู้ป่วย **CKD** เสี่ยงมาก และยังได้ **neurotoxin (caramboxin)** ทำให้สะอึก สับสน ชัก\n\n- uric acid ผลึกเป็นรูปเพชร/สี่เหลี่ยม (ภาพ uric crystal) และต้องมีมะเร็ง/TLS\n- ไม่มีประวัติกล้ามเนื้อ/CK\n- ไม่มี WBC cast/ผื่น\n- ผลึกจำนวนมากอธิบายได้ดีกว่า pre-renal\n\nรักษา: หยุดกิน ให้น้ำถ้าไม่เกิน · dialysis ถ้าอาการทางสมองหรือ AKI รุนแรง",
         "มะเฟือง/ตะลิงปลิง → CaOx crystal (envelope)", "Oxalate nephropathy", R("Intrarenal obstruction (ลายมือ)", "Calcium oxalate crystal (ลายมือ)"), BASE + [ADR]),
    ], BASE + [STONE, ADR],
    imgs=IMGS(
        IM(9, "Crystal จาก ciprofloxacin ในชิ้นเนื้อไต (สไลด์ p36)", "ภาพชิ้นเนื้อไตสองภาพเคียงกัน ภาพซ้ายย้อม H&E เห็นผลึกสีน้ำตาลม่วงในท่อไต ภาพขวาใต้แสงโพลาไรซ์เห็นผลึกเรืองแสงสีขาวแดง",
           cap="**Ciprofloxacin crystal** — สไลด์ p36: ชิ้นเนื้อไต 3 รายพบ **ผลึกรูปเข็ม birefringent ในท่อไต โดยไม่มี AIN** (ซ้าย H&E · ขวาใต้ polarized light ผลึกเรืองแสง) · ✍️ อาจารย์: ciprofloxacin เป็นยาปฏิชีวนะที่ทำ crystal บ่อยที่สุด · ตกผลึกง่ายใน **ปัสสาวะด่าง** และขนาดยาสูง"),
        IM(10, "Drugs induce crystal (สไลด์ p38)", "สไลด์สี่ภาพผลึกจากยา ซ้ายบน acyclovir เป็นผลึกรูปเข็มจำนวนมาก ขวาบน sulphadiazine เป็นผลึกรูปพัดคล้ายฟ่อนข้าวบนพื้นดำ ซ้ายล่าง indinavir เป็นผลึกรูปกากบาทและแท่ง ขวาล่าง amoxycillin เป็นผลึกรูปเข็มเป็นกระจุก กลางภาพมีป้ายเหลือง Drugs induce crystal",
           q="ผลึกจากยา 4 ชนิดในปัสสาวะ — แต่ละรูปทรงคือยาอะไร และยาไหนตกง่ายในปัสสาวะด่าง",
           quiz="**คำตอบ:** **acyclovir** = ผลึกรูปเข็ม (ซ้ายบน) · **sulphadiazine** = รูปพัด/ฟ่อนข้าว \"sheaf of wheat\" (ขวาบน — ใช้รักษา toxoplasmosis ใน HIV) · **indinavir** = แท่ง/รูปดาวกากบาท (ซ้ายล่าง ✍️ HIV → นิ่ว) · **amoxicillin** = เข็มเป็นกระจุก (ขวาล่าง ขนาดสูง) · **ปัสสาวะด่าง:** indinavir (และ ciprofloxacin) · **ปัสสาวะกรด:** sulfonamide, methotrexate, uric acid · ป้องกันทุกตัวด้วยน้ำและปรับขนาดยา"),
        IM(11, "Uric · calcium phosphate · calcium oxalate (สไลด์ p39)", "สไลด์สามภาพผลึกในปัสสาวะ ซ้ายบน uric crystal เป็นผลึกรูปเพชรและสี่เหลี่ยมขนมเปียกปูนจำนวนมาก ขวาบน calcium phosphate เป็นผลึกแท่งเรียงเป็นรูปดาว ล่าง calcium oxalate มีเลข 1 ชี้ผลึกรูปซองจดหมาย และเลข 2 ชี้ผลึกรูปดัมเบล",
           q="ผลึกในปัสสาวะ 3 ชนิด — ภาพล่าง ผลึกหมายเลข 1 และ 2 คืออะไร และนึกถึงภาวะอะไร",
           quiz="**คำตอบ:** ภาพล่างคือ **calcium oxalate** — **① รูปซองจดหมาย (envelope, dihydrate)** และ **② รูปดัมเบล/ไข่ (monohydrate)** (✍️ envelope shape, dumbbell) · **นึกถึง:** ✍️ **ethylene glycol** (AG + osmolar gap สูง) · มะเฟือง/ตะลิงปลิง · Vit C ขนาดสูง · enteric hyperoxaluria · **ภาพบนซ้าย uric acid** = รูปเพชร/สี่เหลี่ยมขนมเปียกปูน (TLS, ปัสสาวะกรด) · **บนขวา calcium phosphate** = แท่งเรียงเป็นดาว (ปัสสาวะด่าง)")))

# ═════════════════════════════════════════════ 13
sec("nephro-aki-13", "Post-renal AKI — ทางเดินปัสสาวะอุดตัน",
    "ระดับท่อไต: นิ่ว ลิ่มเลือด หนอง fungal ball ก้อน · กดจากนอก: มะเร็ง fibrosis ผูกท่อไต · กระเพาะ: BPH neurogenic นิ่ว ก้อน · ท่อปัสสาวะ: stricture (✍️ ฉีด paraffin/ฝังมุก) · UA bland · ultrasound หา hydronephrosis · ระบายแล้วระวัง post-obstructive diuresis", 8,
"""### สาเหตุ — extra-renal (สไลด์ p41)
| ระดับ | สาเหตุ |
|---|---|
| **Ureter / pelvis** — intrinsic | tumor · stone · clot · pus · fungal ball |
| **Ureter / pelvis** — extrinsic | malignancy (มะเร็งปากมดลูก ต่อมลูกหมาก ลำไส้ ต่อมน้ำเหลือง) · retroperitoneal fibrosis · ligation (ผูกท่อไตระหว่างผ่าตัดอุ้งเชิงกราน) |
| **Bladder** | stone · tumor · **neurogenic bladder** · **BPH** · malignancy |
| **Urethra** | **urethral stricture** — ✍️ \"น่าสนใจ\" → **ฉีด paraffin / ฝังมุก** ที่อวัยวะเพศ |

- อุดที่ **ท่อไต** ต้องเป็น **สองข้าง** (หรือไตทำงานข้างเดียว) จึงเกิด AKI · อุดที่ **กระเพาะ/ท่อปัสสาวะ** กระทบทั้งสองไตพร้อมกัน
- **Intrarenal obstruction** (ผลึกในท่อไต) อาจารย์จัดเป็น post-renal ด้วย (หัวข้อ 12)

### UA (สไลด์ p42)
- **Typical: bland sediment** · protein 1+–2+ (< 500 mg/วัน) · อาจมี hematuria จากนิ่ว/ก้อน หรือ pyuria จากการติดเชื้อร่วม

### กลไก: แรงดันย้อน
- แรงดันในท่อไตและ Bowman's space สูง → **ต้านแรงดันกรอง** → GFR ลด
- ระยะแรกหลอดเลือดไตขยายชั่วคราว แล้วตามด้วย **หลอดเลือดหด** (angiotensin II, thromboxane) → RBF ลด
- ระยะแรกท่อไตยังดี (**FENa ต่ำ** — สไลด์ p50 \"acute urinary tract obstruction early stage\") · อุดนานท่อไตเสีย (**FENa สูง** — p51 \"late stage\") และเกิดพังผืดถาวร
- **ระบายเร็ว ไตมักกลับคืน** · อุดนานเกิน 1–2 สัปดาห์ฟื้นไม่เต็มที่ (ตำรา)

### การวินิจฉัยและรักษา (ตำรา + คาบ 22/10 catheter)
- คลำ/เคาะกระเพาะ · **bladder scan** · ใส่สายสวนปัสสาวะ (วินิจฉัยและรักษาพร้อมกัน)
- **Ultrasound** หา hydronephrosis — อาจ **ไม่เห็น** ในชั่วโมงแรก ๆ ขาดน้ำมาก หรือมะเร็ง/fibrosis หุ้มท่อไตไว้ → ถ้าสงสัยมากตรวจซ้ำหรือทำ CT ไม่ฉีดสี
- ระบายตามระดับ: **Foley** (bladder outlet) · **suprapubic catheter** (ใส่ทางท่อปัสสาวะไม่ได้ เช่น stricture) · **percutaneous nephrostomy หรือ DJ stent** (ระดับท่อไต)
- หลังระบาย: **post-obstructive diuresis** — ปัสสาวะ > 200 mL/ชม. เสียน้ำ Na K Mg → วัดทุกชั่วโมง ทดแทนบางส่วน (รายละเอียดคาบ 22/10)

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Anuria ทันที** | อุดสมบูรณ์ที่ทางออกร่วม | ปัสสาวะ 0 mL = คิดอุดตันก่อนเสมอ |
| **ปัสสาวะออกบ้าง ไม่ออกบ้าง (fluctuating)** | อุดไม่สมบูรณ์/ลิ่มขยับ | ไม่ตัด post-renal เพราะยังมีปัสสาวะ |
| **ปัสสาวะออกมาก (polyuria) ใน partial obstruction** | ท่อไตเสียจากแรงดันนาน ทำเข้มข้นไม่ได้ (nephrogenic DI ชั่วคราว) | เคสชายสูงอายุ BPH ที่ปัสสาวะบ่อยปริมาณมาก |
| **K สูง + กรดเกินสัดส่วน GFR** | แรงดันสูงทำ distal tubule หลั่ง K/H ไม่ได้ (type 4 RTA) | ชวนคิดอุดตัน |
""",
    ["Post-renal: อุดสองข้าง หรือที่กระเพาะ/ท่อปัสสาวะ หรือไตข้างเดียว",
     "UA bland · ultrasound หา hydronephrosis (อาจไม่เห็นในระยะแรก/retroperitoneal fibrosis)",
     "ระบายตามระดับ: Foley · suprapubic · nephrostomy/DJ stent",
     "✍️ urethral stricture จากฉีด paraffin/ฝังมุก",
     "หลังระบาย: ระวัง post-obstructive diuresis"],
    [mcq(N(25), "A 52-year-old woman with stage IIIB carcinoma of the cervix presents with 2 days of very low urine output. Creatinine 6.1 mg/dL (baseline 0.8), K 6.0 mEq/L. Bladder scan shows 40 mL residual urine. Ultrasound shows bilateral moderate hydronephrosis with dilated ureters down to the pelvis. After initial treatment of hyperkalaemia, what is the most appropriate intervention to relieve the obstruction?",
         ["Bilateral percutaneous nephrostomy or ureteric stenting", "Insertion of an indwelling urethral (Foley) catheter alone", "Intravenous furosemide to flush the ureters", "Suprapubic catheterisation", "Immediate radical hysterectomy"], 0,
         "ปัสสาวะค้างในกระเพาะเพียง 40 mL แต่ **ท่อไตและไตโป่งทั้งสองข้าง** = อุดที่ **ระดับท่อไตส่วนล่าง** จากมะเร็งปากมดลูกกดเบียด (extrinsic — สไลด์ p41 malignancy) → ต้องระบาย **เหนือจุดอุด** ด้วย **percutaneous nephrostomy** หรือ **ureteric (DJ) stent**\n\n- Foley/suprapubic ระบายเฉพาะกระเพาะ ซึ่งไม่ได้อุด\n- furosemide ไม่แก้การอุดและทำให้ขาดน้ำ\n- ระยะ IIIB ไม่ใช่ข้อบ่งชี้ผ่าตัด\n\nหลังระบายติดตาม post-obstructive diuresis",
         "อุดที่ท่อไต → ระบายเหนือจุดอุด (nephrostomy/stent)", "Ureteric obstruction", R("Post-renal AKI (2)"), BASE + [OBST, ANUR]),
     mcq(N(26), "A 48-year-old man had liquid paraffin injected into his penis several years ago. He now presents with 18 hours of inability to pass urine, a tender palpable bladder and creatinine 2.4 mg/dL (baseline 1.0). Two attempts to pass a 14 Fr Foley catheter meet firm resistance in the penile urethra. What is the most appropriate next step?",
         ["Insert a suprapubic catheter (or ask urology for urgent drainage) rather than forcing a urethral catheter", "Force a larger 22 Fr Foley catheter through the resistance", "Give intravenous furosemide and wait for spontaneous voiding", "Start tamsulosin and discharge with follow-up", "Order a contrast-enhanced CT before any drainage"], 0,
         "✍️ อาจารย์ชี้ว่า **urethral stricture** จาก **การฉีด paraffin/ฝังมุก** เป็นสาเหตุ post-renal ที่ \"น่าสนใจ\" ในไทย · ผู้ป่วยมี **acute urinary retention + AKI** และ **ใส่สายผ่านท่อปัสสาวะไม่ได้** → ต้อง **ระบายทาง suprapubic** (หรือให้ urology ใส่ด้วย guidewire/cystoscope)\n\n- ดันสายใหญ่แรง ๆ ทำ urethra ฉีก (false passage) และทำ stricture แย่ลง\n- furosemide ไม่แก้การอุด\n- tamsulosin ใช้ใน BPH และไม่แก้ stricture\n- ไม่ต้องรอ CT และ contrast ทำร้ายไตเพิ่ม",
         "ใส่สายผ่าน stricture ไม่ได้ → suprapubic", "Urethral stricture", R("Post-renal AKI (2) (ลายมือ)"), BASE + [OBST, ANUR, "2.1.45"]),
    ], BASE + [OBST, BPH, ANUR])

# ═════════════════════════════════════════════ 14
sec("nephro-aki-14", "Step 1–2: ไตวายจริงไหม และ AKI หรือ CKD — พร้อมภาพรังสี",
    "Step 1: BUN ขึ้นจากนอกไต (GI bleed, steroid, catabolism) · Cr ขึ้นโดย GFR ไม่เปลี่ยน (cimetidine, trimethoprim) · Step 2: Cr เดิม ซีด Ca/PO4 ultrasound (ไตเล็ก ขาว cortex บาง) · KUB/IVP มีข้อจำกัด · U/S คือ first-line", 9,
"""### Steps to diagnosis AKI (สไลด์ p43–47)
เมื่อ **BUN/Cr สูงขึ้น ± ปัสสาวะน้อย**
1. **Step 1** — ประเมินสาเหตุที่ BUN/Cr สูง: **ไตวายจริงไหม?**
2. **Step 2** — **AKI หรือ CKD?** (history · physical examination · lab)
3. **Step 3** — **ตัด post-renal** (หัวข้อ 13)
4. **Step 4** — **ประเมิน intrinsic renal** (UA + ดัชนีปัสสาวะ หัวข้อ 15)

### Step 1 — BUN/Cr ขึ้นได้โดยไม่ใช่ไตวาย
| ค่าที่สูง | สาเหตุ (สไลด์ p44–45) | กลไก |
|---|---|---|
| **BUN** | **hypercatabolic stage** (sepsis, burn, ไข้) · โปรตีนสูง · amino acid infusion · **GI bleeding** (✍️ \"blood หรือ bleed เลย\") · **corticosteroid** · tetracycline (หมดอายุ/anti-anabolic) | ผลิต urea มากขึ้น — เลือดในลำไส้ถูกย่อยเป็นโปรตีน |
| **Creatinine** | **rhabdomyolysis** (ปล่อยจากกล้ามเนื้อ) · ยา **ยับยั้งการหลั่ง Cr ที่ท่อไต: cimetidine, trimethoprim** | creatinine ราว 10–20% ถูกหลั่งทาง OCT2/MATE ที่ proximal tubule — ยาแย่งทางนี้ทำ Cr ขึ้น 0.2–0.4 mg/dL โดย GFR เท่าเดิม |

- ยาอื่นที่ยับยั้งการหลั่ง Cr (ตำรา): dolutegravir, cobicistat, ritonavir — Cr ขึ้นเล็กน้อยแล้วคงที่ BUN และปัสสาวะปกติ
- **Trimethoprim** ยังปิด ENaC (คล้าย amiloride) → **K สูง** ได้ด้วย

### Step 2 — AKI หรือ CKD
[[fig:akickd]]

### ภาพรังสีในสไลด์ (p52–58)
[[img:i12]]

[[img:i13]]

**Order ultrasound KUB เพื่อดู (สไลด์ p58)**: 1 kidney size · 2 echogenicity · 3 cortical thickness · 4 corticomedullary junction · 5 complex renal cyst · 6 renal mass
- ✍️ เจอ **renal mass สงสัย RCC** → **ห้ามส่งเจาะไต** → ทำ **CT/MRI** แล้ว **nephrectomy**
- ✍️ ไตสองข้างขนาด **ต่างกันเกิน 1.5 ซม.** → คิด renovascular disease หรือไตข้างหนึ่งฝ่อ

[[img:i14]]

[[img:i15]]

#### ทำไมถึงมีอาการนี้
| สิ่งตรวจพบ | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **BUN 80 Cr 1.1 ในเลือดออกทางเดินอาหาร** | เลือดเป็นโปรตีนถูกย่อยดูดซึม + volume ลด | BUN/Cr สูงมาก ไม่ใช่ไตวายเสมอ |
| **Cr ขึ้น 0.3 หลังได้ co-trimoxazole BUN ไม่ขึ้น** | trimethoprim แย่งการหลั่ง creatinine | ไม่ใช่ AKI จริง — ดู BUN, UO, cystatin C |
| **ไตเล็ก ขาว cortex บาง** | พังผืดแทนเนื้อไต (nephron หาย) | CKD |
| **Cortex ขาวกว่าตับ แต่ไตขนาดปกติ** | เนื้อไตอักเสบ/บวม หรือ CKD ที่ไตไม่เล็ก | ใช้ร่วมกับประวัติและ Cr เดิม |
""",
    ["4 ขั้น: ไตวายจริงไหม → AKI หรือ CKD → ตัด post-renal → ประเมิน intrinsic",
     "BUN สูงจากนอกไต: GI bleed · steroid · catabolism · โปรตีน/amino acid · tetracycline",
     "Cr สูงโดย GFR ไม่เปลี่ยน: cimetidine · trimethoprim (ยับยั้งการหลั่ง) · rhabdo",
     "CKD: ไตเล็ก ขาว cortex บาง ซีด PTH สูง — ยกเว้น DM amyloid HIVAN ADPKD myeloma ไตไม่เล็ก",
     "KUB/IVP มีข้อจำกัด (เงาลำไส้ · ต้องฉีด contrast) → ultrasound เป็นตัวแรก · ✍️ ก้อนสงสัย RCC ห้ามเจาะไต"],
    [mcq(N(27), "A 38-year-old man with HIV infection is started on high-dose trimethoprim-sulfamethoxazole for Pneumocystis pneumonia. On day 3 his creatinine has risen from 1.0 to 1.3 mg/dL. BUN is unchanged at 12 mg/dL, urine output is 1.8 L/day, urinalysis is bland, and potassium is 5.6 mEq/L. What is the best explanation for the change in creatinine?",
         ["Trimethoprim inhibits tubular secretion of creatinine, raising serum creatinine without a true fall in GFR", "Sulfamethoxazole crystal nephropathy causing obstructive AKI", "Pre-renal AKI from Pneumocystis-related dehydration", "Acute interstitial nephritis from sulfonamide hypersensitivity", "Rhabdomyolysis from pneumonia"], 0,
         "สไลด์ p45: **decrease tubular secretion — cimetidine, trimethoprim** → Cr สูงขึ้นโดย **GFR ไม่เปลี่ยน** (Step 1: \"is it really renal failure?\") · เบาะแส: Cr ขึ้นเล็กน้อย (0.3) **BUN คงที่ ปัสสาวะดี UA bland**\n\nK 5.6 อธิบายได้จาก trimethoprim **ปิด ENaC** ที่ collecting duct (เหมือน amiloride) ไม่ใช่จาก GFR ตก\n\n- crystal/AIN จาก sulfonamide เกิดได้จริง แต่จะมีผลึกหรือ pyuria/WBC cast และ BUN ขึ้นตาม\n- pre-renal ทำ BUN/Cr ratio สูงและปัสสาวะเข้มข้น\n- ไม่มีหลักฐาน rhabdomyolysis\n\nจัดการ: ให้ยาต่อ ติดตาม K และ Cr (ถ้าต้องการวัด GFR จริงใช้ cystatin C)",
         "Cr ขึ้นเล็กน้อย BUN คงที่ หลัง trimethoprim = แย่งการหลั่ง", "Creatinine secretion", R("Increased serum creatinine"), BASE + [RFT, ADR]),
     mcq(N(28), "A 58-year-old woman presents with fatigue and is found to have creatinine 4.8 mg/dL; no previous results are available. Hb 8.5 g/dL (normocytic), phosphate 6.8 mg/dL, calcium 7.8 mg/dL and intact PTH 480 pg/mL. Ultrasound shows a right kidney of 8.1 cm and left kidney of 8.4 cm, both with increased cortical echogenicity, thin cortex and poor corticomedullary differentiation. Which finding most strongly indicates chronic rather than acute kidney disease?",
         ["Bilateral small echogenic kidneys with thin cortex", "Serum phosphate of 6.8 mg/dL", "Creatinine of 4.8 mg/dL", "Hypocalcaemia", "Fatigue"], 0,
         "**ไตเล็กสองข้าง (< 9 ซม.) + echogenicity สูง + cortex บาง + corticomedullary junction ไม่ชัด** = nephron ถูกแทนด้วยพังผืดซึ่งต้องใช้เวลาเป็นเดือน–ปี → **CKD** (สไลด์ p58 สิ่งที่ต้องดูใน ultrasound)\n\nซีดและ PTH สูงก็สนับสนุน CKD แต่ **PO4 สูง Ca ต่ำ** เกิดใน AKI ได้ภายในไม่กี่วัน · ค่า Cr เดี่ยว ๆ บอกเวลาไม่ได้ · อาการเหนื่อยไม่จำเพาะ\n\nข้อยกเว้นที่ไตไม่เล็กแม้เป็น CKD: DM, amyloidosis, HIVAN, ADPKD, myeloma (อิงตำรา)",
         "ไตเล็ก ขาว cortex บาง = CKD", "AKI vs CKD ultrasound", R("Order investigation for U/S KUB, Step 2"), BASE + ["B9.2.7(2)", RFT]),
    ], BASE + [RFT, "B9.2.7(2)"], figs={"akickd": F.aki_ckd()},
    imgs=IMGS(
        IM(12, "Film KUB (สไลด์ p53)", "ภาพถ่ายรังสีช่องท้องแนวหน้า เห็นกระดูกสันหลังส่วนเอวตรงกลาง เงาไตสองข้างจาง ๆ ซ้อนกับเงาลมในลำไส้และอุจจาระ",
           q="สไลด์ถามว่า \"limitation in investigation due to ???\" — ฟิล์ม KUB นี้ใช้ประเมินไตใน AKI ได้จำกัดเพราะอะไร",
           quiz="**คำตอบ:** เงาไตถูก **ลมและอุจจาระในลำไส้บัง** เห็นขอบไตไม่ชัด · เห็นได้เฉพาะ **นิ่วที่ทึบรังสี** (calcium) — uric acid stone และ hydronephrosis มองไม่เห็น · ไม่บอกเนื้อไตหรือการอุดตัน · **ใช้ทำอะไร:** ดูนิ่วทึบรังสี และติดตามนิ่ว · AKI ให้เริ่มที่ **ultrasound**"),
        IM(13, "Film IVP (สไลด์ p55)", "ภาพถ่ายรังสี intravenous pyelogram เห็นกรวยไตและท่อไตสองข้างมีสารทึบรังสีเป็นสีขาว เงาลำไส้ซ้อนอยู่บางส่วน",
           q="สไลด์ถามว่า IVP \"limitation in investigation due to ???\" — ทำไมไม่ใช้ IVP ในผู้ป่วย AKI",
           quiz="**คำตอบ:** IVP ต้อง **ฉีด iodinated contrast** และอาศัย **ไตกรองสารทึบรังสีออกมา** · ใน AKI GFR ต่ำ → ภาพจาง/ไม่เห็น และ contrast **ทำร้ายไตซ้ำ** (contrast-associated AKI — หัวข้อ 10) · ยังมีปัญหาเงาลำไส้บังเหมือน KUB · ปัจจุบันแทนด้วย **ultrasound** (ดูการอุดตัน) และ **CT ไม่ฉีดสี** (นิ่ว)"),
        IM(14, "Ultrasound ไต (สไลด์ p56)", "ภาพอัลตราซาวด์แนวยาวของไตขวาใต้ตับ เห็นเนื้อไตรอบนอกสีเทาและไขมันในกรวยไตตรงกลางสีขาว",
           cap="**Ultrasound KUB** — ตรวจตัวแรกใน AKI: ไม่ใช้รังสี/contrast ทำข้างเตียงได้ · ดู **ขนาด · echogenicity (เทียบกับตับ) · ความหนา cortex · corticomedullary junction · hydronephrosis · ก้อน/ถุงน้ำ** · ✍️ อาจารย์: ถ้าไตสองข้างขนาด **ต่างกันเกิน 1.5 ซม.** ให้คิดถึงโรคหลอดเลือดแดงไตตีบหรือไตข้างหนึ่งฝ่อ"),
        IM(15, "Ultrasound วัดขนาดไต (สไลด์ p57)", "ภาพอัลตราซาวด์ไตสองภาพเคียงกัน มีเครื่องหมายวัดความยาวไตและความหนาของ cortex ตัวเลข distance มุมขวาบน",
           cap="การ **วัดขนาดไตและความหนา cortex** — ไตผู้ใหญ่ปกติยาว **~10–12 ซม.** cortex หนาพอสมควร · ไต **< 9 ซม. ขาวกว่าตับ cortex บาง** ชวน CKD · ข้อยกเว้นที่ไตไม่เล็กแม้เป็น CKD: DM, amyloidosis, HIVAN, ADPKD, myeloma (ตัวเลขอิงตำรา)")))

# ═════════════════════════════════════════════ 15
sec("nephro-aki-15", "Step 4: ดัชนีปัสสาวะ — FENa, FEurea และกับดัก",
    "Pre-renal: SpGr > 1.024 · Uosm > 400 · U/P osm > 1.5 · U Na < 20 · FENa < 1% · BUN/Cr > 20 · U/P Cr > 40 · ATN: Uosm > 300 (~300) · U Na > 30 · FENa > 1% · U/P Cr < 20 · low FENa ATN และ high FENa pre-renal (DMARD) · ได้ diuretic ใช้ FEurea", 10,
"""### Diagnostic indices (สไลด์ p48)
| | **Pre-renal** | **ATN** | **Obstructive uropathy** |
|---|---|---|---|
| SpGr | > 1.024 | 1.015 | 1.015 |
| U osmole | > 400 | > 300 | > 300 |
| U/P osmole | > 1.5 | 1 | 1 |
| U Na | < 20 | > 30 | < 30 |
| **FENa** | **< 1%** | **> 1%** | variable |
| **BUN/Cr** | **> 20** | 10 | 10–20 |
| U/P Cr | > 40 | < 20 | < 20 |

ตำราส่วนใหญ่ใช้ตัวเลขที่ห่างกันกว่านี้ (pre-renal Uosm > 500 · ATN Uosm < 350 · U Na > 40 · FENa > 2%) — เพื่อให้ชัดว่า **ATN ทำปัสสาวะเข้มข้นไม่ได้** (Uosm ใกล้ plasma ~300)

### FENa (สไลด์ p49)
**FENa = (U Na / P Na) ÷ (U Cr / P Cr) × 100%** — สัดส่วนของ Na ที่ถูกกรองแล้วหลุดออกมาในปัสสาวะ

[[fig:fena]]

### ข้อยกเว้น — FENa หลอก (สไลด์ p50–51)
| | สาเหตุ |
|---|---|
| **AKI ที่ FENa ต่ำ (< 1%) แต่ไม่ใช่ pre-renal ธรรมดา** | non-renal loss · **hepatorenal syndrome** · acute glomerular injury · HUS/TTP · acute allograft rejection · **acute urinary tract obstruction (early)** · ATN บางแบบ: non-oliguric, **contrast**, **ACEI/ARB/NSAID**, ARF in pregnancy, **sepsis**, extensive burn, **rhabdomyolysis**, **hemolysis**, uric acid nephropathy |
| **AKI ที่ FENa สูง (> 2%) แต่เป็น pre-renal** | **\"DMARD\"**: **D**iuretic use · **M**ineralocorticoid deficiency · **A**lkalosis (metabolic) · **R**enal salt wasting · **D**M (glycosuria) |
| **FENa สูงอื่น ๆ** | AIN · acute renal artery occlusion · acute urinary tract obstruction (late) · classical ATN (ischemic, toxic) |

### FEurea — ใช้เมื่อได้ diuretic (ตำรา ไม่อยู่ในสไลด์)
- **FEurea = (U urea / P urea) ÷ (U Cr / P Cr) × 100%** (ใช้ urea nitrogen ทั้งคู่)
- urea ถูกดูดกลับส่วนใหญ่ที่ **proximal tubule** ซึ่ง loop/thiazide ไม่ได้ออกฤทธิ์ → ไม่ถูก diuretic หลอก
- **< 35% = pre-renal** · **> 50% = ATN**

#### ทำไมถึงมีอาการนี้
| ค่าที่ได้ | กลไก | กับดัก |
|---|---|---|
| **FENa < 1% ใน contrast/rhabdo/sepsis** | มีส่วนของหลอดเลือดไตหดตัวรุนแรง ท่อไตบางส่วนยังดูด Na | อย่าสรุป pre-renal จาก FENa อย่างเดียว ดู UA |
| **FENa สูงในผู้ได้ furosemide** | ยาบล็อก NKCC2 Na หลุด | ใช้ FEurea |
| **FENa สูงใน metabolic alkalosis (อาเจียน)** | HCO3 ที่เกินถูกขับพร้อม Na (bicarbonaturia) | ดู **U Cl** แทน (< 20 = ขาด volume) |
| **FENa ต่ำในคนปกติที่กินเค็มน้อย** | GFR ปกติ ไตดูด Na เกือบหมด | แปลผลเฉพาะใน AKI ที่ปัสสาวะน้อย |
""",
    ["FENa = (U Na/P Na) ÷ (U Cr/P Cr) × 100 · < 1% pre-renal · > 1–2% ATN",
     "Pre-renal: Uosm > 400 · U/P osm > 1.5 · BUN/Cr > 20 · U/P Cr > 40",
     "ATN ที่ FENa ต่ำ: contrast · rhabdo · hemolysis · sepsis · burn · non-oliguric",
     "Pre-renal ที่ FENa สูง: DMARD (diuretic, mineralocorticoid deficiency, alkalosis, renal salt wasting, DM)",
     "ได้ diuretic → FEurea (< 35% pre-renal · > 50% ATN)"],
    [mcq(N(29), "A 66-year-old man becomes oliguric after cardiac surgery complicated by 3 hours of hypotension. He has received no diuretics. Plasma Na 136 mEq/L, plasma creatinine 4.0 mg/dL; urine Na 68 mEq/L, urine creatinine 40 mg/dL, urine osmolality 310 mOsm/kg. Urine sediment shows granular casts. What is his fractional excretion of sodium (FENa) and its interpretation?",
         ["0.05% — pre-renal azotaemia", "0.5% — pre-renal azotaemia", "2% — indeterminate", "5% — acute tubular necrosis", "20% — post-renal obstruction"], 3,
         "**FENa = (U Na / P Na) ÷ (U Cr / P Cr) × 100** (สไลด์ p49)\n\n- U Na / P Na = 68 / 136 = **0.5**\n- U Cr / P Cr = 40 / 4.0 = **10**\n- 0.5 ÷ 10 = 0.05 → × 100 = **5%**\n\nFENa 5% (> 1–2%) + Uosm 310 (ทำเข้มข้นไม่ได้) + granular cast + ไม่ได้ diuretic = **ATN** หลังความดันต่ำนาน\n\n- **0.05%** = ลืมคูณ 100\n- 0.5% ได้จากการสลับเศษส่วน\n- FENa ไม่ได้ใช้วินิจฉัย post-renal (variable)",
         "FENa = (UNa×PCr)/(PNa×UCr) × 100", "FENa calculation", R("Fractional excretion of sodium, Diagnostic indices"), BASE + [UA_B, OSM], keep=True),
     mcq(N(30), "A 78-year-old woman with heart failure on furosemide 80 mg/day presents with poor intake and vomiting. Creatinine 2.0 mg/dL (baseline 1.0), BUN 60 mg/dL. Urine: Na 45 mEq/L, creatinine 100 mg/dL, urea nitrogen 300 mg/dL; FENa is 3%. Urine sediment shows only hyaline casts. Calculate her fractional excretion of urea (FEurea) and interpret it.",
         ["FEurea 10% — supports pre-renal azotaemia despite the high FENa", "FEurea 10% — supports acute tubular necrosis", "FEurea 50% — supports acute tubular necrosis", "FEurea 50% — supports pre-renal azotaemia", "FEurea cannot be interpreted in patients taking loop diuretics"], 0,
         "**FEurea = (U urea / P urea) ÷ (U Cr / P Cr) × 100**\n\n- U urea / BUN = 300 / 60 = **5**\n- U Cr / P Cr = 100 / 2.0 = **50**\n- 5 ÷ 50 = 0.1 → × 100 = **10%**\n\nFEurea **< 35% = pre-renal** · FENa 3% สูงหลอกเพราะ **furosemide** (D ของ \"DMARD\" สไลด์ p51) · urea ถูกดูดกลับส่วนใหญ่ที่ proximal tubule ซึ่ง loop diuretic ไม่ได้ออกฤทธิ์ จึงใช้ได้ในผู้ได้ diuretic\n\nBUN/Cr 30 และ hyaline cast ก็สนับสนุน pre-renal\n\n- ATN จะมี FEurea > 50% และ granular cast\n\n(FEurea อิงตำรา ไม่อยู่ในสไลด์)",
         "ได้ diuretic: FEurea < 35% = pre-renal", "FEurea", R("ARF with high FENa (DMARD)"), BASE + [UA_B, DRUGFL]),
    ], BASE + [UA_B, OSM, RFT], figs={"fena": F.fena()})

# ═════════════════════════════════════════════ 16
sec("nephro-aki-16", "ภาวะแทรกซ้อน — hyperkalemia และ ECG · น้ำเกิน · Na ต่ำ · กรด · PO4/Ca/urate",
    "ECG: peaked T → P หาย PR ยาว → QRS กว้าง bradycardia → sine wave · Ca gluconate 1 g · RI 10 U + 50% glucose 50 mL (✍️ glucose > 250 ให้ RI อย่างเดียว) · β-agonist · binder (Kalimate/Dekales, Lokelma) · loop diuretic · dialysis · acidosis: NaHCO3 ให้ HCO3 > 15 หรือ pH > 7.2", 12,
"""### Prevention and treatment of complications (สไลด์ p66, p70)
[[img:i19]]

[[img:i20]]

| ภาวะ | การป้องกัน/รักษาในสไลด์ |
|---|---|
| **Volume overload** | จำกัดเกลือและน้ำ · diuretics |
| **Hyponatremia** | จำกัด free water ทางปาก · เลี่ยงสารน้ำ hypotonic ทางหลอดเลือด |
| **Hyperkalemia** | จำกัด K ในอาหาร · หยุด K supplement และ K-sparing diuretic · loop diuretic · K binder · insulin + glucose · β-agonist · calcium · dialysis |
| **Metabolic acidosis** | **NaHCO3 (รักษา HCO3 > 15 mmol/L หรือ pH > 7.2)** · dialysis (สไลด์ใช้สายฟ้าเน้น) · ✍️ \"มี case ถ้า CO2 สูงอยู่แล้วในเลือด\" — ระวัง |
| Hyperphosphatemia | จำกัด phosphate · phosphate binder (CaCO3, Al(OH)3) — อาจารย์กากบาท (ไม่ใช่ประเด็นหลักใน AKI) |
| Hypocalcemia | Ca carbonate/gluconate **ถ้ามีอาการ** |
| Hypermagnesemia | หยุด antacid ที่มี Mg |
| Hyperuricemia | รักษาเมื่อ > 15 mg/dL · allopurinol, forced alkaline diuresis — อาจารย์กากบาท |

### Hyperkalemia — กลไกและ ECG
- ไตขับ K ส่วนใหญ่ → AKI ทำ K คั่ง · กรดดัน K ออกจากเซลล์ · เซลล์ตาย (rhabdo, TLS, hemolysis) · ยา (ACEi/ARB, spironolactone, NSAID, trimethoprim)
- ✍️ **ดู K จาก blood gas ได้เลย** — ได้ผลเร็วกว่ารอผลแล็บ
- ECG (สไลด์ p60–65): **peaked T/tall peaked T → loss of P wave · prolonged PR → QRS กว้าง · bradycardia → sine wave** → VF/asystole

[[img:i16]]

[[img:i17]]

[[img:i18]]

### รักษา hyperkalemia 3 ขั้น
[[fig:hyperk]]

| ขั้น | ยา (สไลด์ + ✍️) | หมายเหตุ (ตำรา) |
|---|---|---|
| **1 ปกป้องหัวใจ** | **calcium gluconate หรือ calcium chloride 1 g** | 10% Ca gluconate 10 mL IV 2–3 นาที · ออกฤทธิ์ 1–3 นาที อยู่ 30–60 นาที · ทำซ้ำได้ถ้า ECG ยังผิด · CaCl2 มี Ca มากกว่า ~3 เท่าแต่ระคายเส้น |
| **2 ย้ายเข้าเซลล์** | **insulin 10 units regular + glucose 50 mL of 50% dextrose** · ✍️ insulin **IV** · ✍️ **ถ้าน้ำตาลสูงเกิน 250 ให้ RI อย่างเดียว** · inhaled β-agonist | insulin กระตุ้น Na-K ATPase ลด K ~0.6–1 mEq/L ใน 15–30 นาที อยู่ 4–6 ชม. · AKI กำจัด insulin ช้า **เสี่ยงน้ำตาลต่ำ** → ตรวจ DTX ทุกชั่วโมง |
| **3 เอาออก** | loop diuretic · **K binder** · **dialysis** | binder ใช้เวลา · dialysis เมื่อดื้อยา (AEIOU) |

### K binder ในไทย (สไลด์ p66–69)
| | **Kalimate / Dekales** (รุ่นเดิม) | **Lokelma** (รุ่นใหม่) |
|---|---|---|
| ชื่อสาร | **calcium polystyrene sulfonate** (✍️ แลก K เอา Ca) | **sodium zirconium cyclosilicate** |
| กลไก | แลกเปลี่ยน K กับ Ca | ดักจับ K อย่างจำเพาะตลอดทางเดินอาหาร |
| ความเร็ว | ช้า (หลายชั่วโมงถึงวัน) | เริ่มเห็นผลใน **1 ชม.** |
| รส/สัมผัส | สากเหมือนทราย ละลายยาก | ไม่มีรส เนียนเหมือนแป้ง |
| ผลข้างเคียง | **ท้องผูกรุนแรง ลำไส้อุดตัน/ทะลุ** (บางราย) | ต่ำกว่า · บวมน้ำเล็กน้อย (มี Na) |
| การเตรียม | ผสมน้ำพอสมควร | ผสมน้ำน้อย ดื่มได้ทันที |
| ราคา | ถูก | **300–400 บาท/ซอง** |
- Kayexalate (ชื่อในตาราง) = **sodium** polystyrene sulfonate — ในไทยใช้รุ่น calcium (Kalimate)

#### ทำไมถึงมีอาการนี้
| อาการ/สิ่งตรวจพบ | กลไก | ใช้อย่างไร |
|---|---|---|
| **กล้ามเนื้ออ่อนแรง ชา** | RMP ยกขึ้นนาน Na channel inactivate → กล้ามเนื้อกระตุ้นไม่ขึ้น | K สูงมากแม้ ECG ยังไม่เปลี่ยน |
| **Peaked T** | K conductance เพิ่ม → repolarize เร็ว | สัญญาณแรก |
| **QRS กว้าง sine wave** | นำไฟฟ้าช้าใน ventricle | ภาวะก่อนหัวใจหยุดเต้น → Ca ทันที |
| **ตัวบวม เหนื่อยนอนราบไม่ได้** | ขับ Na/น้ำไม่ได้ + ได้น้ำเกลือ | ดื้อ diuretic = ข้อบ่งชี้ dialysis |
| **หายใจหอบลึก (Kussmaul)** | ชดเชย metabolic acidosis | HCO3 < 15 หรือ pH < 7.2 → NaHCO3 / dialysis |
""",
    ["✍️ ดู K จาก blood gas ได้เร็ว · ECG ผิด = รักษาด่วนไม่ว่า K เท่าไร",
     "ECG: peaked T → P หาย PR ยาว → QRS กว้าง bradycardia → sine wave",
     "Ca gluconate 1 g ปกป้องหัวใจ แต่ไม่ลด K",
     "RI 10 U IV + 50% glucose 50 mL · ✍️ น้ำตาล > 250 ให้ RI อย่างเดียว · เฝ้าน้ำตาลต่ำ",
     "Kalimate/Dekales (Ca polystyrene sulfonate) ช้า ท้องผูก · Lokelma เร็ว ~1 ชม. แพง",
     "Acidosis: NaHCO3 ให้ HCO3 > 15 หรือ pH > 7.2 · ✍️ ระวังถ้า CO2 สูง"],
    [mcq(N(31), "A 70-year-old man with oliguric AKI has a serum potassium of 7.2 mEq/L. ECG shows peaked T waves, absent P waves and a QRS duration of 160 ms. Blood pressure is 128/70 mmHg. Which should be given first?",
         ["Intravenous 10% calcium gluconate 10 mL over 2–3 minutes", "Oral calcium polystyrene sulfonate (Kalimate) 30 g", "Intravenous furosemide 80 mg", "Intravenous sodium bicarbonate 100 mL of 7.5% solution", "Arrange haemodialysis and give nothing until it starts"], 0,
         "K 7.2 + **QRS กว้าง P หาย** = หัวใจใกล้หยุดเต้น (สไลด์ p60–61) → ต้อง **ปกป้อง myocardium ก่อน** ด้วย **calcium gluconate (หรือ chloride) 1 g** (= 10% Ca gluconate 10 mL) IV 2–3 นาที · ออกฤทธิ์ใน 1–3 นาที ทำซ้ำได้ถ้า ECG ยังผิด\n\nจากนั้น **insulin + glucose · β-agonist** แล้วเอา K ออก (binder, diuretic, dialysis)\n\n- binder ช้าเป็นชั่วโมง–วัน\n- furosemide ใช้ได้น้อยใน oliguric AKI และช้า\n- NaHCO3 ลด K ได้น้อย ใช้เมื่อมี acidosis\n- ระหว่างรอ dialysis ต้องรักษาด้วยยาก่อนเสมอ",
         "ECG เปลี่ยน → Ca gluconate ก่อนทุกอย่าง", "Hyperkalaemia first step", R("Pattern of EKG in hyperkalemia, Prevention and treatment of complications"), BASE + [HYPERK, ECG]),
     mcq(N(32), "A 61-year-old man with type 2 diabetes and AKI has potassium 6.6 mEq/L with peaked T waves. Calcium gluconate has been given. His capillary blood glucose is 320 mg/dL. What is the most appropriate way to shift potassium into cells?",
         ["Regular insulin 10 units intravenously without dextrose, with hourly glucose monitoring", "Regular insulin 10 units intravenously with 50 mL of 50% dextrose", "Regular insulin 10 units subcutaneously", "50 mL of 50% dextrose alone to stimulate endogenous insulin", "Withhold insulin because hyperglycaemia will drive potassium out of cells"], 0,
         "สไลด์: **insulin 10 units regular + glucose 50 mL of 50% dextrose** · ✍️ อาจารย์: insulin ให้ **IV** และ **ถ้าน้ำตาลสูงเกิน 250 ให้ RI อย่างเดียว** — น้ำตาล 320 อยู่แล้ว ไม่ต้องให้ glucose เพิ่ม\n\ninsulin กระตุ้น **Na-K ATPase** ดึง K เข้าเซลล์ ลด K ~0.6–1 mEq/L ใน 15–30 นาที · AKI กำจัด insulin ช้า จึงต้อง **ตรวจน้ำตาลทุกชั่วโมง** (เสี่ยงน้ำตาลต่ำหลายชั่วโมง)\n\n- การให้ dextrose เพิ่มทำให้น้ำตาลสูงขึ้นอีก (hyperosmolality ดึง K ออกจากเซลล์)\n- SC ดูดซึมไม่แน่นอนและช้า\n- dextrose อย่างเดียวพึ่ง insulin ของตัวเองซึ่งไม่พอในเบาหวาน\n- การไม่ให้ insulin ไม่ถูก",
         "✍️ น้ำตาล > 250: ให้ RI IV อย่างเดียว", "Insulin for hyperkalaemia", R("Prevention and treatment of complications (ลายมือ)"), BASE + [HYPERK, DRUGFL]),
    ], BASE + [HYPERK, LYTE, ECG, ECG_B, ABG], figs={"hyperk": F.hyperk_tx()},
    imgs=IMGS(
        IM(16, "Pattern of EKG in hyperkalemia (1) (สไลด์ p60)", "สไลด์ ECG สี่ภาพ ซ้ายบน lead V5 คลื่น T สูงแหลม ขวาบน lead II คลื่น P หายไป ซ้ายล่างแถบ PR segment ยาว ขวาล่าง lead II หัวใจเต้นช้ามาก แต่ละภาพมีป้ายสีฟ้ากำกับ",
           cap="สไลด์ p60: **peaked T wave/tall peak T** (V5) · **loss of P wave** · **prolonged PR segment** · **bradycardia** — เรียงตามความรุนแรงโดยประมาณ: T เปลี่ยนก่อน (repolarization เร็วขึ้น) แล้ว atrium นำไฟฟ้าช้า (P แบน/หาย PR ยาว) ตามด้วย ventricle (QRS กว้าง) · ECG สัมพันธ์กับระดับ K ไม่ดี บางรายหัวใจหยุดโดยไม่มี peaked T มาก่อน"),
        IM(17, "Sine wave (สไลด์ p61)", "แถบ ECG rhythm strip lead II เห็นคลื่นกว้างโค้งต่อเนื่องคล้ายคลื่นไซน์ ไม่เห็น P wave และ QRS แยกจาก T",
           q="Rhythm strip ของผู้ป่วยไตวายที่ซึมลง — รูปคลื่นนี้เรียกว่าอะไร และต้องทำอะไรทันที",
           quiz="**คำตอบ:** **sine wave pattern** — QRS กว้างมากจนรวมกับ T เป็นคลื่นโค้งต่อเนื่อง ไม่มี P = **hyperkalemia รุนแรงมาก** ใกล้ VF/asystole · **ทำทันที:** **calcium gluconate 10% 10 mL IV** (ซ้ำได้) → insulin + glucose · β-agonist → เตรียม **dialysis ด่วน** · ✍️ อาจารย์: \"ดู blood gas ได้เลย\" ได้ค่า K ภายในไม่กี่นาที"),
        IM(18, "12-lead ECG ใน hyperkalemia (สไลด์ p62)", "ECG 12 lead ใน chest leads V2 ถึง V4 คลื่น T สูงแหลมมากและ QRS กว้าง limb leads เห็นคลื่นกว้าง ไม่เห็น P wave ชัดเจน",
           q="ECG 12 lead ของผู้ป่วย AKI ที่ K ยังไม่ออกผล — ลองอ่านสิ่งผิดปกติหลัก 3 อย่าง",
           quiz="**คำตอบ:** **T สูงแหลมฐานแคบ** (เด่นที่ V2–V4) · **QRS กว้าง** · **ไม่เห็น P wave ชัด** = **hyperkalemia ระดับรุนแรง** (สไลด์ pattern 3) · **กลไก:** K นอกเซลล์สูง → repolarize เร็ว (peaked T) และ Na channel inactivate → นำไฟฟ้าช้า (QRS กว้าง P หาย) · **ทำ:** ให้ Ca gluconate ก่อนรอผล K · ระวังสับสนกับ hyperacute T ของ STEMI (STEMI ฐาน T กว้าง ไม่มี QRS กว้างทั่วทุก lead)"),
        IM(19, "Prevention and treatment of complications (สไลด์ p66)", "ตารางสีส้มอ่อนจากสไลด์ แถว volume overload hyponatremia และ hyperkalemia พร้อมวิธีรักษา มีกล่องเหลืองเขียน Kalimate Dekales calcium polystyrene sulfonate และ Kalimate ข้าง potassium binding resin",
           cap="ตารางของอาจารย์ (p66): **volume overload** — จำกัดเกลือ/น้ำ diuretics · **hyponatremia** — จำกัด free water เลี่ยงสารน้ำ hypotonic · **hyperkalemia** — จำกัด K หยุด K supplement/K-sparing diuretic loop diuretic **K binder (ในไทย = Kalimate/Dekales)** insulin 10 U + 50% glucose 50 mL β-agonist **Ca gluconate/chloride 1 g** dialysis · ✍️ insulin ทาง IV · ✍️ น้ำตาล > 250 ให้ RI อย่างเดียว"),
        IM(20, "Prevention and treatment of complications (ต่อ) (สไลด์ p70)", "ตารางต่อจากสไลด์ แถว hyperphosphatemia hypocalcemia hypermagnesemia hyperuricemia และ metabolic acidosis มีกากบาทแดงที่ phosphate binder และ allopurinol และสายฟ้าแดงชี้ metabolic acidosis",
           cap="ตารางต่อ (p70): อาจารย์ **กากบาท** phosphate binder และ allopurinol/forced alkaline diuresis (ไม่ใช่ประเด็นหลักใน AKI) และ **สายฟ้าชี้ metabolic acidosis** — **NaHCO3 ให้ HCO3 > 15 mmol/L หรือ pH > 7.2 · dialysis** · ✍️ \"มี case ถ้า CO2 สูงอยู่แล้วในเลือด\" → NaHCO3 ถูกเปลี่ยนเป็น CO2 ผู้ป่วยที่หายใจออกไม่ทัน (CO2 คั่ง) อาจเป็นกรดมากขึ้น · Ca ต่ำให้เมื่อมีอาการ")))

# ═════════════════════════════════════════════ 17
sec("nephro-aki-17", "ข้อบ่งชี้ dialysis ใน AKI — เริ่มก่อน \"too late\"",
    "สไลด์: K สูง/น้ำเกิน/กรด ที่ไม่ตอบสนองต่อยาเต็มที่ · uremic symptom · uremic pericarditis · BUN > 100 หรือ Cr > 10 (non-catabolic) · BUN > 70 หรือ Cr > 7 (hypercatabolic) · อาการ uremia = too late · AEIOU", 8,
"""### ข้อบ่งชี้ในสไลด์
**Dialysis (สไลด์ p71)**
- **Hyperkalemia** ที่ไม่ตอบสนองต่อยาเต็มที่
- **Volume overload** ที่ไม่ตอบสนองต่อยาเต็มที่
- **Uremic symptom**
- **Uremic pericarditis**
- **Severe metabolic acidosis** ที่ไม่ตอบสนองต่อยาเต็มที่
- **BUN > 100 หรือ Cr > 10** (non-catabolic)
- **BUN > 70 หรือ Cr > 7** (hypercatabolic)

**Indication of RRT in AKI (HD / acute PD) — สไลด์ p72**
- early signs: anorexia, nausea, vomiting, pruritus · uremic encephalopathy · uremic pericarditis (late complication) → อาจารย์กากบาททั้งหมดว่า **\"Too late\"** ✍️ \"End stage\"
- **Key for initiating RRT in AKI**: **1. control volume overload** ที่ไม่ตอบสนองต่อยาเต็มที่ · **2. acid–base disturbance** ที่ไม่ตอบสนองต่อยาเต็มที่ (อาจารย์วาดหัวใจไว้)

[[fig:rrt]]

### เชื่อมกับแนวทางปัจจุบัน (ไม่อยู่ในสไลด์)
- **KDIGO 2012**: เริ่ม RRT **เร่งด่วน** เมื่อมีความผิดปกติของน้ำ เกลือแร่ กรด-ด่างที่คุกคามชีวิต · การตัดสินใจอื่นให้ดู **ภาพรวมทางคลินิกและแนวโน้ม** มากกว่าค่า BUN/Cr เพียงอย่างเดียว
- การศึกษา **STARRT-AKI (2020)** และ AKIKI: การเริ่มฟอกเร็ว \"ล่วงหน้า\" ในผู้ป่วยที่ยังไม่มีข้อบ่งชี้ ไม่ลดอัตราตาย และทำให้ต้องฟอกต่อนานขึ้น → ผู้ป่วยที่คุมได้ด้วยยา **รอได้** และหลายรายไตฟื้นโดยไม่ต้องฟอก
- เลือกวิธี: **intermittent HD** (เร็ว แก้ K ได้ดีสุด) · **CRRT** (ผู้ป่วยความดันไม่คงที่ใน ICU หรือสมองบวม) · **acute PD** (สไลด์ระบุ — ใช้ได้เมื่อไม่มีเครื่อง HD/หลอดเลือดไม่ดี)
- **I — intoxication** (methanol, ethylene glycol, lithium, salicylate) เป็นข้อบ่งชี้ dialysis ที่ไม่ขึ้นกับไต

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ความหมาย |
|---|---|---|
| **เบื่ออาหาร คลื่นไส้ อาเจียน คัน** | uremic toxin (guanidine, middle molecules) ระคายทางเดินอาหาร ผิวหนัง | early uremia — สไลด์ว่าสายแล้ว |
| **สับสน asterixis ชัก** | uremic encephalopathy | ต้องฟอกทันที |
| **เจ็บอกเสียดสี pericardial rub** | uremic pericarditis — เยื่อหุ้มหัวใจอักเสบจากสารพิษ (มักไม่มี ST elevation แบบ viral) | ✍️ \"End stage\" · เสี่ยง tamponade |
| **เลือดออกง่าย** | uremic platelet dysfunction | desmopressin ช่วยชั่วคราว · dialysis แก้ |
""",
    ["Dialysis ใน AKI: K สูง · น้ำเกิน · กรด ที่ไม่ตอบสนองต่อยาเต็มที่ (สไลด์ p71–72)",
     "อาการ uremia (encephalopathy, pericarditis) = too late — อย่ารอถึงจุดนั้น",
     "BUN > 100/Cr > 10 (non-catabolic) · BUN > 70/Cr > 7 (hypercatabolic)",
     "AEIOU: Acidosis · Electrolyte · Intoxication · Overload · Uremia",
     "คุมได้ด้วยยา → รอได้ (STARRT-AKI) · ไม่ความดันคงที่ → CRRT"],
    [mcq(N(33), "A 68-year-old man with ischaemic ATN is on day 4 of oliguria (urine output 300 mL/day). He has received furosemide 200 mg intravenously without any increase in urine output. He is now dyspnoeic with bibasal crackles to the mid-zones and SpO₂ 88% on 6 L/min oxygen. BP 160/90 mmHg. K 5.4 mEq/L, HCO3 19 mEq/L, BUN 86 mg/dL, creatinine 6.4 mg/dL. What is the most appropriate next step?",
         ["Urgent dialysis (ultrafiltration) for diuretic-resistant volume overload", "Continue furosemide and wait until BUN exceeds 100 mg/dL", "Give a further 1 L of saline to improve renal perfusion", "Start sodium bicarbonate infusion", "Give oral calcium polystyrene sulfonate and reassess tomorrow"], 0,
         "**Volume overload ที่ไม่ตอบสนองต่อยาเต็มที่** (furosemide 200 mg IV แล้วไม่มีปัสสาวะ) + น้ำท่วมปอด SpO₂ 88% = ข้อบ่งชี้ **dialysis เร่งด่วน** (สไลด์ p71 และ key ข้อ 1 ใน p72 · O ใน AEIOU) → **ultrafiltration** ดึงน้ำออก\n\n- รอให้ BUN > 100 = \"too late\" — เขากำลังหายใจล้มเหลวจากน้ำ\n- ให้น้ำเกลือเพิ่มทำให้แย่ลง\n- HCO3 19 ไม่ใช่ acidosis รุนแรง และ NaHCO3 เพิ่ม Na/น้ำ\n- K 5.4 ไม่ใช่ปัญหาหลัก",
         "น้ำเกินที่ดื้อ diuretic = dialysis ด่วน", "Dialysis indication", R("Dialysis, Indication of RRT in AKI"), BASE + [OLIG, ANUR]),
     mcq(N(34), "A 65-year-old man has AKI stage 3 from contrast and sepsis. On day 4 he is alert and comfortable, BP 132/76 mmHg, lungs clear, no oedema. Urine output has increased from 400 to 1,000 mL/day. K 5.2 mEq/L, HCO3 20 mEq/L, BUN 92 mg/dL, creatinine 7.4 mg/dL (non-catabolic). There is no pericardial rub or confusion. What is the most appropriate plan?",
         ["Continue conservative management with daily monitoring because there is currently no indication for dialysis", "Start haemodialysis now because creatinine exceeds 7 mg/dL", "Start haemodialysis now because AKI stage 3 always requires dialysis", "Insert a peritoneal dialysis catheter and start acute PD to prevent uraemia", "Start continuous renal replacement therapy to remove contrast"], 0,
         "เทียบกับเกณฑ์สไลด์ p71: K ไม่ดื้อยา · ไม่มีน้ำเกิน · HCO3 20 ไม่ใช่กรดรุนแรง · ไม่มีอาการ uremia/pericarditis · **non-catabolic** ต้อง **BUN > 100 หรือ Cr > 10** (เขา 92 และ 7.4) → **ยังไม่มีข้อบ่งชี้** และ **ปัสสาวะเริ่มเพิ่ม** (เข้าสู่ระยะฟื้น)\n\n**ดูแลแบบประคับประคอง** ติดตามน้ำ K กรด และ Cr ทุกวัน — STARRT-AKI แสดงว่าการเริ่มล่วงหน้าไม่ช่วยและอาจไม่จำเป็นเลย\n\n- Cr > 7 เป็นเกณฑ์ของ **hypercatabolic** เท่านั้น\n- stage 3 ไม่ได้แปลว่าต้องฟอก\n- contrast ถูกขับเองไม่ต้องใช้ CRRT",
         "ไม่มี AEIOU + ปัสสาวะเพิ่ม → รอได้", "Timing of RRT", R("Dialysis", KDIGO), BASE + [RFT]),
    ], BASE + [LYTE, HYPERK], figs={"rrt": F.rrt_timing()})


# ───────────────────────────── MEQ / OSCE
MEQ = [{"id": "NEPH-AKI-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Triple whammy (ACEi + diuretic + NSAID) with diarrhoea → pre-renal progressing to ATN, hyperkalaemia and refractory volume overload — staging, urine indices, emergency treatment and RRT",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 72 ปี ส่วนสูง 155 ซม. น้ำหนัก 50 กก.
CC: ถ่ายเหลว 3 วัน ปัสสาวะออกน้อย 1 วัน
PI: 3 วันก่อนถ่ายเหลวเป็นน้ำวันละ 6–8 ครั้ง กินได้น้อย · 1 สัปดาห์ก่อนซื้อ ibuprofen 400 mg วันละ 3 ครั้งกินเองเพราะปวดเข่า · 12 ชม. ที่ผ่านมาปัสสาวะ 150 mL อ่อนเพลีย ใจสั่น
U/D: hypertension, heart failure (LVEF 45%) — enalapril 10 mg bid, furosemide 40 mg/วัน, spironolactone 25 mg/วัน · Cr 1.0 mg/dL เมื่อ 3 เดือนก่อน
PE: BT 37.4 °C · PR 112/min · BP 92/56 mmHg (ลุกนั่งแล้วหน้ามืด) · RR 22/min · เยื่อบุแห้ง JVP ไม่เห็น ปอดใส ไม่บวม
Lab: BUN 54 mg/dL · Cr 3.6 mg/dL · Na 131 · K 6.8 · Cl 100 · HCO3 14 mEq/L · glucose 110 mg/dL
UA: SpGr 1.012 · protein trace · blood negative · WBC 0–1/HPF · **muddy brown granular casts และ renal tubular epithelial cells**
Urine: Na 52 mEq/L · creatinine 40 mg/dL · urea nitrogen 330 mg/dL · osmolality 320 mOsm/kg
ECG: sinus tachycardia · T สูงแหลม V2–V5 · PR 240 ms · QRS 120 ms""",
 "questions": [
  {"q": "1. จงเขียน problem list และบอก KDIGO stage พร้อมเหตุผล (3 คะแนน)",
   "a": """**Problem list**
1. **AKI KDIGO stage 3** — Cr 3.6 จาก baseline 1.0 = **3.6 เท่า** (≥ 3 เท่า) · UO 150 mL/12 ชม. = 12.5 mL/ชม. ÷ ideal body weight (155 − 100 = 55 กก.) = **0.23 mL/kg/h × 12 ชม.** (เกณฑ์ UO ระดับ stage 2 — ใช้เกณฑ์ที่รุนแรงกว่าคือ Cr → stage 3)
2. **Severe hyperkalemia (K 6.8) with ECG changes** (peaked T, PR ยาว, QRS กว้าง) — ต้องรักษาก่อน
3. **High anion gap metabolic acidosis** — AG = 131 − (100 + 14) = **17**
4. **Hypovolemia / volume depletion** จากถ่ายเหลว + diuretic (BP ต่ำ ชีพจรเร็ว postural)
5. **Hyponatremia (131)**
6. ได้ยา **\"triple whammy\"** — enalapril + furosemide + ibuprofen และ **spironolactone** (เพิ่ม K)
7. U/D hypertension, heart failure (LVEF 45%)"""},
  {"q": "2. AKI นี้เป็น pre-renal หรือ ATN — จงคำนวณดัชนีที่เหมาะสมและแปลผล (4 คะแนน)",
   "a": """**FENa** = (U Na × P Cr) ÷ (P Na × U Cr) × 100 = (52 × 3.6) ÷ (131 × 40) × 100 = 187.2 ÷ 5,240 × 100 ≈ **3.6%**
แต่ผู้ป่วย **ได้ furosemide** → FENa สูงหลอกได้ (D ใน **DMARD**) → ใช้ **FEurea**
**FEurea** = (U urea × P Cr) ÷ (BUN × U Cr) × 100 = (330 × 3.6) ÷ (54 × 40) × 100 = 1,188 ÷ 2,160 × 100 = **55%** (> 50% = ATN)
**สนับสนุน ATN:** Uosm 320 / SpGr 1.012 (ทำเข้มข้นไม่ได้) · BUN/Cr = 15 (ไม่ถึง 20) · **muddy brown granular cast + RTE cells**
**สรุป:** เริ่มจาก **pre-renal** (ถ่ายเหลว + diuretic + NSAID ตัด prostaglandin ที่ afferent + ACEi ตัด angiotensin II ที่ efferent) ที่ปล่อยไว้จนเกิด **ischemic ATN**"""},
  {"q": "3. จงสั่งการรักษาภาวะ hyperkalemia ทันที พร้อมขนาดยาและเหตุผล (4 คะแนน)",
   "a": """1. **10% calcium gluconate 10 mL (1 g) IV ใน 2–3 นาที** — ECG เปลี่ยน (QRS กว้าง) ต้องปกป้องหัวใจก่อน · ซ้ำได้ถ้า ECG ยังผิดหลัง 5–10 นาที
2. **Regular insulin 10 units IV + 50% glucose 50 mL** (น้ำตาล 110 จึงต้องให้ glucose — ✍️ ถ้า > 250 ให้ RI อย่างเดียว) · ตรวจ DTX ทุกชั่วโมง 4–6 ชม. (AKI กำจัด insulin ช้า)
3. **Salbutamol พ่น 10–20 mg** เสริมการย้าย K เข้าเซลล์
4. **NaHCO3** พิจารณาได้เพราะ HCO3 14 (ร่วมกับ volume ที่ขาด) — เป้า HCO3 > 15 หรือ pH > 7.2 (สไลด์)
5. **หยุด enalapril, spironolactone, ibuprofen, furosemide** · งดอาหาร K สูง · ให้ **isotonic fluid** แก้ volume ที่ขาด (เพิ่มการขับ K) · **K binder** (Lokelma ออกฤทธิ์เร็วกว่า Kalimate)
6. ตรวจ K ซ้ำใน 1–2 ชม. (blood gas เร็ว ✍️) · ติด monitor · **เตรียม dialysis ถ้าไม่ตอบสนอง**"""},
  {"q": "4. ผ่านไป 36 ชม. หลังได้ isotonic fluid 3 ลิตร: ปัสสาวะ 100 mL/24 ชม. แม้ได้ furosemide 200 mg IV · น้ำหนักเพิ่ม 3 กก. · crackles ถึงกลางปอด SpO₂ 89% (O₂ 6 L/min) · K 6.4 ทั้งที่ได้ยาข้อ 3 ซ้ำ · pH 7.14 HCO3 10 · ผู้ป่วยรู้สึกตัวดี BP 150/88 — จงบอกการจัดการและเหตุผล (3 คะแนน)",
   "a": """มีข้อบ่งชี้ **dialysis เร่งด่วน 3 ข้อ** ตามสไลด์ p71–72 (AEIOU):
- **O — volume overload ที่ไม่ตอบสนองต่อ diuretic** (น้ำท่วมปอด)
- **E — hyperkalemia ที่ไม่ตอบสนองต่อยาเต็มที่**
- **A — severe metabolic acidosis** (pH 7.14 HCO3 10) — การให้ NaHCO3 เพิ่มจะเติม Na/น้ำในคนที่น้ำเกินอยู่แล้ว
→ ใส่ **double-lumen catheter** และทำ **hemodialysis + ultrafiltration** ทันที (ความดันคงที่ → intermittent HD ได้ · ถ้าไม่คงที่ → CRRT) · ไม่ต้องรอให้มี uremic symptom (\"too late\")"""},
  {"q": "5. ก่อนกลับบ้าน จงบอกการป้องกันไม่ให้เกิดซ้ำ และการติดตามระยะยาว (2 คะแนน)",
   "a": """- **เลี่ยง NSAID** (รวม COX-2 inhibitor) — ใช้ paracetamol/ยาทาเฉพาะที่แทน
- **Sick day rules**: เมื่อท้องเสีย อาเจียน หรือกินไม่ได้ ให้ **หยุด ACEi/ARB, diuretic, spironolactone (และ metformin/SGLT2i ถ้ามี)** ชั่วคราวและมาพบแพทย์
- เริ่ม ACEi/diuretic ใหม่ทีละตัวเมื่อไตฟื้นและ volume คงที่ ตรวจ Cr/K หลังเริ่ม 1–2 สัปดาห์
- ติดตาม Cr และ urine albumin ที่ **~3 เดือน** — AKI เพิ่มความเสี่ยง CKD และ AKI ซ้ำ (KDIGO)
- ทบทวนขนาดยาที่ขับทางไตทุกครั้ง"""}],
 "ref": ["สไลด์ อ.วรรณิยา — Cause of pre-renal azotemia, Diagnostic indices, FENa, ARF with high FENa (DMARD), Prevention and treatment of complications, Dialysis", KDIGO],
 "nl": [AKI, AKI_B, HYPERK, LYTE, ADR, OLIG], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "NEPH-AKI-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "OSCE/SAQ – Hyperkalaemia in oliguric AKI: read the ECG, give emergency orders and decide on dialysis",
 "station": "OSCE (อ่าน ECG + เขียนคำสั่งการรักษา) 6 นาที · ผู้คุมสอบ 1 คน · ECG 12 lead หนึ่งแผ่น + ใบสั่งยา",
 "instruction": """ผู้ป่วยชายอายุ 64 ปี เบาหวาน ได้ enalapril มา admit ด้วย pneumonia และ septic shock วันที่ 3 ปัสสาวะ 200 mL/วัน
ผล blood gas ล่าสุด: pH 7.22 · HCO3 13 · K 7.0 mEq/L · glucose 180 mg/dL · Cr 4.9 mg/dL (baseline 1.1)
ท่านได้รับ ECG 12 lead (ลักษณะเหมือนภาพ **12-lead ECG ใน hyperkalemia** ในหัวข้อ 16 — T สูงแหลม QRS กว้าง ไม่เห็น P)

**จงทำสิ่งต่อไปนี้**
1. อ่าน ECG และบอกความหมายให้ผู้คุมสอบฟัง
2. เขียนคำสั่งการรักษาเร่งด่วนพร้อมขนาดยา
3. บอกการติดตามและเกณฑ์ที่จะส่งฟอกเลือด""",
 "answer": """| หัวข้อ | สิ่งที่ต้องทำ/พูด | คะแนน |
|---|---|---|
| **อ่าน ECG** | T สูงแหลมฐานแคบ · **QRS กว้าง** · P หาย/แบน · (bradycardia ถ้ามี) → **hyperkalemia รุนแรง เสี่ยง sine wave/VF** | 2 |
| **ความเร่งด่วน** | บอกว่า **ECG ผิด = รักษาทันที** ไม่รอผลซ้ำ · ติด cardiac monitor · ✍️ ใช้ K จาก blood gas ได้ | 1 |
| **ขั้น 1 ปกป้องหัวใจ** | **10% Ca gluconate 10 mL (1 g) IV 2–3 นาที** (หรือ CaCl2 ทาง central line) · ซ้ำได้ถ้า ECG ไม่ดีขึ้น | 2 |
| **ขั้น 2 ย้าย K** | **RI 10 U IV + 50% glucose 50 mL** (glucose 180 < 250 จึงให้ glucose — ✍️ ถ้า > 250 ให้ RI อย่างเดียว) · salbutamol พ่น 10–20 mg · **NaHCO3** พิจารณาเพราะ pH 7.22 HCO3 13 (ระวังน้ำเกิน/CO2) | 3 |
| **ขั้น 3 เอาออก** | หยุด **enalapril** และ K ทุกแหล่ง · K binder (Lokelma เร็ว / Kalimate ช้า) · loop diuretic ถ้ามีปัสสาวะและไม่ขาดน้ำ | 2 |
| **ติดตาม** | K ซ้ำ 1–2 ชม. · DTX ทุก 1 ชม. (น้ำตาลต่ำหลัง insulin ใน AKI) · ECG ซ้ำ · I/O | 2 |
| **เกณฑ์ dialysis** | **K ที่ไม่ตอบสนองต่อยาเต็มที่ · กรดรุนแรงที่ไม่ตอบสนอง · น้ำเกินที่ไม่ตอบสนอง** · อาการ uremia (\"too late\") · ใน septic shock ความดันไม่คงที่ → **CRRT** | 2 |
| **การสื่อสาร** | ลำดับชัดเจน บอกขนาดยาและทางให้ยาครบ | 1 |

**รวม 15 คะแนน** · **ข้อผิดพลาดร้ายแรง:** ให้ K binder หรือ furosemide เป็นยาแรกโดยไม่ให้ calcium · ให้ insulin โดยไม่ติดตามน้ำตาล · ให้ insulin ทาง SC""",
 "ref": ["สไลด์ อ.วรรณิยา — Pattern of EKG in hyperkalemia, Prevention and treatment of complications, Dialysis"],
 "nl": [HYPERK, ECG, AKI, ABG], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "ศ. 30 ต.ค.",
 "title": "Acute kidney injury — นิยาม KDIGO แยก pre/intra/post-renal และการดูแล",
 "subtitle": "หน้าที่ไตและนิยาม (RIFLE → KDIGO) · pre-renal (NSAID/ACEi, sepsis, HRS, cardiorenal) · intrinsic 4 กลุ่ม (vascular · GN · AIN · ATN) · nephrotoxin · pigment · crystal · post-renal · 4 ขั้นของการวินิจฉัย · ดัชนีปัสสาวะ FENa/FEurea · hyperkalemia และ ECG · ข้อบ่งชี้ dialysis — พร้อมภาพจริงจากสไลด์ 20 ภาพ",
 "objectives": [
   "บอกหน้าที่ของไต และอธิบายว่าทำไม AKI ทำให้เกิดน้ำเกิน K สูง และกรด",
   "จัดระดับ AKI ตาม RIFLE (สไลด์) และ KDIGO 2012 และบอกข้อจำกัดของ creatinine",
   "แยกสาเหตุ pre-renal, intrinsic (vascular, GN, AIN, ATN) และ post-renal จากประวัติ ตรวจร่างกาย และ UA \"หน้าตาแบบใด\"",
   "อธิบายกลไกของ pre-renal (autoregulation, NSAID/ACEi, sepsis, hepatorenal, cardiorenal) และการดูแล",
   "อธิบายกลไกของ ATN, AIN, pigment nephropathy และ crystal nephropathy และสิ่งตรวจพบที่ใช้แยก",
   "ใช้ 4 ขั้นของการวินิจฉัย AKI รวมถึงการแยก AKI กับ CKD และการเลือกภาพรังสี",
   "คำนวณและแปลผล FENa และ FEurea พร้อมรู้ข้อยกเว้น",
   "อ่าน ECG ของ hyperkalemia และสั่งการรักษาภาวะแทรกซ้อนของ AKI ได้ถูกลำดับ",
   "บอกข้อบ่งชี้ของการบำบัดทดแทนไตใน AKI และหลัก \"อย่ารอจนสายเกินไป\""],
 "nlGap": "เกณฑ์ฯ มีรหัส `นล. 2.3.14(3)` Acute kidney injury และ `B9.2.7(1)` เป็นแกนของคาบ รวมถึง `2.2.15` hyperkalemia, `2.3.14-3(8)` interstitial nephritis, `2.3.14-3(9)` obstructive uropathy แต่ **ไม่มีรหัสเฉพาะ** สำหรับ rhabdomyolysis, contrast-associated AKI, crystal nephropathy, hepatorenal/cardiorenal syndrome และการบำบัดทดแทนไต (dialysis) · **สไลด์ใช้เกณฑ์ RIFLE** และไม่ได้สอน KDIGO, การป้องกัน contrast AKI, FEurea, ระยะของ ATN, การรักษา TTP/AIN/rhabdomyolysis, HRS และ cardiorenal — ส่วนเหล่านี้อิงแนวทางด้านล่างและระบุในบทเรียน",
 "guidelines": [
   "**KDIGO Clinical Practice Guideline for Acute Kidney Injury 2012** — นิยาม/staging · ไม่ใช้ dopamine/diuretic ป้องกัน · contrast-induced AKI · การเริ่ม RRT (Kidney Int Suppl 2012;2:1–138)",
   "**ACR–NKF Consensus 2020** — use of intravenous iodinated contrast media in patients with kidney disease (Davenport MS, et al. Radiology 2020) + ACR Manual on Contrast Media (metformin)",
   "**EASL Clinical Practice Guidelines for decompensated cirrhosis 2018** — albumin challenge และ terlipressin ใน HRS-AKI",
   "**ISTH guideline for treatment of TTP 2020** — plasma exchange + corticosteroid",
   "**STARRT-AKI (N Engl J Med 2020)** — accelerated vs standard initiation of RRT",
   "ตำรา: Bosch X, et al. Rhabdomyolysis and acute kidney injury. N Engl J Med 2009"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── ประกอบ
secs = {s_["id"]: s_ for s_ in S}
for it in AN.ITEMS:
    s_ = secs[it["sec"]]
    a = it["anim"]
    s_.setdefault("anims", {})[a["key"]] = {k: a[k] for k in ("title", "svg", "steps")}
    s_["md"], ok = _insert_marker(s_["md"], it.get("after", ""), "[[anim:%s]]" % a["key"])
    assert ok, ("ไม่พบหัวข้อ", it["sec"], it.get("after"))
for m in AN.MNEM:
    secs[m["sec"]].setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})

# กระจายตำแหน่งคำตอบ (คำตอบถูกเขียนไว้ที่ choices[0] · ข้อที่ตัวเลือกเรียงตามลำดับ keep ไว้)
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it.pop("_keep", False):
            continue
        assert it["answer"] == 0, it["id"]
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        ch = it["choices"]; ch[0], ch[tgt] = ch[tgt], ch[0]; it["answer"] = tgt

# ตรวจภาพจริง / figs / anims: ทุก marker มีของ และทุกของถูกใช้
for s_ in S:
    for kind, field in (("img", "imgs"), ("fig", "figs"), ("anim", "anims")):
        used = re.findall(r"^\s*\[\[%s:([\w-]+)\]\]\s*$" % kind, s_["md"], re.M)
        have = s_.get(field, {})
        assert set(used) == set(have), (s_["id"], kind, set(used) ^ set(have))
        assert len(used) == len(set(used)), (s_["id"], kind)
    for k, g in s_.get("imgs", {}).items():
        assert re.match(r"^img/[\w/.-]+\.(jpg|png|webp)$", g["src"]), g["src"]
        assert os.path.exists(os.path.join(BUILD, g["src"])), g["src"]
        assert g.get("alt") and g.get("credit") and (g.get("cap") or (g.get("quiz") and g.get("q"))), (s_["id"], k)
    assert "```" not in s_["md"], s_["id"]
allimg = [k for s_ in S for k in s_.get("imgs", {})]
assert len(allimg) == len(set(allimg)), "key ภาพซ้ำ"

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8"))
data = [l for l in data if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

BANK_MAP = {
    "nephro-aki-04": ["N-MCQ-35", "N-MCQ-38", "N-OLD-105", "N-OLD-107", "N-OLD-108", "N-OLD-113", "N-OLD-115"],
    "nephro-aki-05": ["N-MCQ-39", "N-OLD-116", "N-OLD-117", "N-OLD-118"],
    "nephro-aki-08": ["N-OLD-114", "N-OLD-120"],
    "nephro-aki-09": ["N-OLD-106"],
    "nephro-aki-10": ["N-MCQ-37", "N-OLD-112", "N-OLD-122"],
    "nephro-aki-11": ["N-MCQ-36", "N-OLD-109", "N-OLD-110", "N-OLD-123"],
    "nephro-aki-12": ["N-OLD-111"],
    "nephro-aki-13": ["N-MCQ-40", "N-OLD-121"],
    "nephro-aki-15": ["N-OLD-119"],
    "nephro-aki-17": ["N-OLD-124"],
}
added = link(SET, LEC, BANK_MAP, meq=["N-MEQ-02"])

d = json.load(open(path, encoding="utf-8"))
assert d[-1]["lec"] == LEC
L = d[-1]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m["nl"]})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
ids = [i["id"] for l in d for s_ in l["sections"] for i in s_["items"]] + [m["id"] for l in d for m in l["meq"] + l["osce"]]
dup = {x for x in ids if ids.count(x) > 1}
assert not dup, dup

# index.json: lectureCount + intro/howto ของชุด nephro
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
nfig_all = sum(len(s_.get("figs") or {}) for l in d for s_ in l["sections"])  # ตัวเลขเดิมใน intro (144) นับเฉพาะ figs
AKI_INTRO = (" · และคาบ 42 **Acute kidney injury** ของ พญ.วรรณิยา ตั้งแต่นิยาม RIFLE/KDIGO และข้อจำกัดของ creatinine "
             "ไล่สาเหตุ pre-renal (NSAID/ACEi, sepsis, hepatorenal, cardiorenal) · intrinsic 4 กลุ่ม (vascular, GN, AIN, ATN) "
             "รวม nephrotoxin, pigment และ crystal · post-renal · 4 ขั้นของการวินิจฉัยและดัชนีปัสสาวะ FENa/FEurea "
             "จนถึง hyperkalemia กับ ECG และข้อบ่งชี้ dialysis พร้อมภาพจริงจากสไลด์ (urine sediment, histology, ultrasound, ECG)")
AKI_HOWTO = (" · คาบ 42 (AKI): หัวข้อ 2–3 (นิยามและสามกลุ่มสาเหตุ) → 4 (กลไก afferent/efferent) → 14–15 (4 ขั้นและดัชนีปัสสาวะ) "
             "แล้วไล่ intrinsic ในหัวข้อ 6–12 · ปิดด้วย 16–17 (hyperkalemia และ dialysis) ซึ่งเป็นเรื่องที่ต้องทำได้ในวอร์ด")
for m in idx:
    if m["set"] != SET:
        continue
    m["lectureCount"] = len(d)
    it = m["intro"]
    if "คาบ 42 **Acute kidney injury**" not in it:
        it = it.replace("เจ็ดคาบของชุด Nephro", "แปดคาบของชุด Nephro")
        it = it.replace(" · และคาบ 22/10 **Urethral catheterization**", " · คาบ 22/10 **Urethral catheterization**")
        anchor = "จนถึง CAUTI การแก้ปัญหาใส่ไม่เข้า และ post-obstructive diuresis"
        assert anchor in it
        it = it.replace(anchor, anchor + AKI_INTRO)
    it = re.sub(r"\*\*ภาพกลไกรวม \d+ ภาพ\*\*", "**ภาพกลไกรวม %d ภาพ**" % nfig_all, it)
    m["intro"] = it
    hw = m["howto"]
    if "คาบ 42 (AKI)" not in hw:
        anchor = "· ฝึก OSCE หัตถการใส่สายในหุ่นท้ายคาบ"
        assert anchor in hw
        hw = hw.replace(anchor, anchor + AKI_HOWTO)
        old = "(CKD · dysnatremia & dyskalemia · urine analysis · AKI)"
        assert old in hw
        hw = hw.replace(old, "(CKD · dysnatremia & dyskalemia · urine analysis)")
    m["howto"] = hw
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

nimg_kb = sum(os.path.getsize(os.path.join(BUILD, g["src"])) for s_ in S for g in s_.get("imgs", {}).values()) / 1048576
print("sections %d | ข้อใหม่ %d + คลัง %d | meq %d | osce %d | figs %d | anims %d | mnem %d | imgs %d (%.2f MB) | nl %d | nephro figs %d" % (
    len(S), sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("NEPH-AKI")), added, len(L["meq"]), len(L["osce"]),
    sum(len(s_.get("figs") or {}) for s_ in S), len(AN.ITEMS), len(AN.MNEM), len(allimg), nimg_kb, len(codes), nfig_all))
