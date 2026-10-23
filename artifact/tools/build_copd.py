#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 37 (ส่วน COPD) Pneumonia / Asthma / COPD (Basic) (AL) — อ.เกรียงศักดิ์ → data/chest.json
ต้นฉบับ: Drive 1b3Tr9ooby8N1NYRB3pRiCznHns6LayaE "GOLD-REPORT-2026-v1.3-8Dec2025_WMV2.pdf" (GOLD 2026 Report)
โน้ต: slides/copd_notes.md · ภาพประกอบ: figs_copd.py
ข้อความที่ดึงได้ถูกตัดที่หน้า 127 (กลางบท 5) และรูป/ตารางทั้งหมดเป็นภาพที่อ่านไม่ได้ →
ส่วนที่อยู่ในรูป (ตัวเลข mMRC/CAT ในรูป ABE, เป้า SpO2 88–92%, ข้อบ่งชี้ NIV/IMV, admission criteria, ยาเลิกบุหรี่, รายละเอียดยาใน Appendix)
อิงความรู้ GOLD 2025/2026 และระบุไว้ในบทเรียน
โครงสร้างตามที่ผู้ใช้ขอ: หัวข้อ 1–11 = ระดับ NL (COPD กลุ่ม 2 ดูแลเองได้) · หัวข้อ 12–14 = "อ่านเพิ่มเติม (เกินระดับ NL)"
คลัง Ward Drill คาบ 37: ผูกเฉพาะข้อ COPD (CH-MCQ-37/38/39 · CH-OLD-48…51 · CH-MEQ-02) — ข้อ pneumonia/asthma ปล่อยไว้ให้บทเรียนถัดไป"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link
from svg import fig
import figs_copd as F

SET, LEC = "chest", "37"
SRC = "GOLD 2026 Report (Global Strategy for the Diagnosis, Management, and Prevention of COPD)"
SRC_FIG = "GOLD 2026 Report + GOLD 2025 (ส่วนที่เป็นรูป/ตารางซึ่งอ่านจากไฟล์ไม่ได้)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
              "nl": nl, "md": md, "pearls": pearls, "items": items, "figs": figs or {}})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "CH-COPD-MCQ-%02d" % n
R = lambda p: ["GOLD 2026 — " + p]

# รหัส นล. (เกณฑ์แพทยสภา 2567)
COPD, COPDB, AE, ARF, RF = "2.3.10(3)", "B6.2.2(5)", "2.2.11", "2.2.9", "B6.2.5(1)"
SPIRO, SPIROB, BD, ICS, TOB = "3.3.18", "B6.3(3)", "B6.4(4)", "B6.4(5)", "2.3.19(6)"
ABG, ABGB, MECH, GAS, O2T, CTRL = "3.3.17", "B6.3(2)", "B6.1.2(2)", "B6.1.2(4)", "B6.1.2(5)", "B6.1.2(3)"
DYS, COUGH, CYAN, WL, CXR = "2.1.34", "2.1.32", "2.1.37", "2.1.9", "3.2.1"
FLU, IMM, CORT, ASTHMA, LRTI = "2.3.1(11)", "B1.4.8", "B11.4(3)", "2.3.10(1)", "2.3.10(5)"
PTX, ASTHMAB, LRTIB = "2.3.10(6)", "B6.2.2(2)", "B6.2.2(4)"

RM = ("> **อ่านเพิ่มเติม — เกินระดับที่ NL ต้องการ** · หัวข้อนี้สรุปรายละเอียดจาก GOLD 2026 สำหรับคนที่อยากรู้ลึกหรือเตรียมขึ้น ward อายุรกรรม "
      "ข้ามได้ถ้าเป้าหมายคือสอบ NL · ข้อสอบท้ายหัวข้อเป็นระดับ \"อ่านเพิ่มเติม\"")

# ───────────────────────────── 1
sec("chest-copd-01", "COPD คืออะไร ใครเสี่ยง — นิยาม GOLD 2026 และปัจจัยเสี่ยงในบริบทไทย",
    "นิยามใหม่ · บุหรี่/ยาเส้น · ควันชีวมวล · PM2.5 · อาชีพ · วัณโรคเก่า · ปอดโตไม่เต็มที่ · pack-year", 9,
"""> **บทเรียนนี้แบ่งเป็น 2 ชั้นตามที่ขอ** · หัวข้อ 1–11 = **ความรู้ระดับที่ NL ต้องการ** (COPD อยู่ใน `นล. 2.3.10(3)` กลุ่ม 2 = ต้องวินิจฉัยและดูแลเบื้องต้นได้เอง รวมถึง acute exacerbation ใน `นล. 2.2.11`) · หัวข้อ 12–14 ขึ้นต้นว่า **"อ่านเพิ่มเติม (เกินระดับ NL)"** เป็นรายละเอียดจาก GOLD 2026 ที่อ่านเสริมได้ ข้ามได้ถ้าเตรียมสอบ NL
> คาบนี้ไม่มีสไลด์จากอาจารย์ เนื้อหาเรียบเรียงจาก **GOLD 2026 Report** · ข้อความที่ดึงจากไฟล์ถูกตัดที่หน้า 127 และรูป/ตารางในรายงานเป็นภาพที่อ่านไม่ได้ ส่วนนั้นอิง GOLD 2025 และจะระบุไว้ตรงจุดที่ใช้

### นิยาม (GOLD 2026)
**COPD** = โรคปอดที่ **ต่างกันในแต่ละคน (heterogeneous)** มีอาการทางเดินหายใจเรื้อรัง (เหนื่อย ไอ มีเสมหะ และ/หรือ exacerbation) จากความผิดปกติของ **ทางเดินหายใจ** (bronchitis, bronchiolitis) และ/หรือ **ถุงลม** (emphysema) ทำให้เกิด **airflow obstruction ที่คงอยู่ (persistent) และมักแย่ลงเรื่อย ๆ**

- วินิจฉัยด้วย **spirometry: post-bronchodilator FEV1/FVC < 0.7** ในบริบททางคลินิกที่เข้ากัน (อาการ + ปัจจัยเสี่ยง) — หัวข้อ 4
- COPD เป็นสาเหตุการตาย **อันดับ 3 ของโลก** (3.7 ล้านคนในปี 2021 · ราว 90% อยู่ในประเทศรายได้ต่ำ–ปานกลาง) และ **กว่า 80% ของผู้ป่วยยังไม่ได้รับการวินิจฉัย**
- คำว่า "chronic bronchitis" (ไอมีเสมหะ ≥ 3 เดือน/ปี ติดกัน 2 ปี) และ "emphysema" (ถุงลมถูกทำลาย) เป็นคำบรรยายลักษณะ ไม่ใช่เกณฑ์วินิจฉัย — ผู้ป่วยส่วนใหญ่มีทั้งสองแบบในสัดส่วนต่างกัน

### สาเหตุ: ยีน × สิ่งแวดล้อม × ช่วงเวลาของชีวิต (GETomics)
[[fig:trajectory]]

| ปัจจัยเสี่ยง | กลไก / ข้อมูลจาก GOLD 2026 | ในเวชปฏิบัติไทย |
|---|---|---|
| **บุหรี่** (รวมยาเส้น มวนเอง ไปป์ บารากู่ กัญชา) | ควันมีสารออกซิแดนท์และอนุภาค กระตุ้น macrophage/neutrophil หลั่ง protease ทำลายเนื้อปอด · เริ่มสูบก่อนอายุ 15 เสี่ยงมากขึ้นโดยไม่ขึ้นกับ pack-year · **แต่ < 50% ของคนสูบหนักเป็น COPD** | ผู้ชายสูงอายุในชนบทสูบ **ยาเส้นมวนใบตอง/ใบจาก** ซึ่งเผาไม่สมบูรณ์ ควันเข้มข้น ต้องถามทุกครั้ง |
| **ควันบุหรี่มือสอง** · แม่สูบขณะตั้งครรภ์ | ปอดทารกโตผิดปกติ (epigenetic) | ถามคนในบ้าน |
| **ควันชีวมวล (biomass)** — ฟืน ถ่าน แกลบ มูลสัตว์ | ในประเทศรายได้ต่ำ–ปานกลาง บุหรี่อธิบายได้แค่ **30–40%** ของภาระโรค · ปัจจัยที่ไม่ใช่บุหรี่รวมกันเกิน 50% ของ COPD ทั่วโลก | **ผู้หญิงที่ไม่เคยสูบบุหรี่แต่หุงต้มด้วยฟืน/ถ่านในครัวปิดมาหลายสิบปี** คือผู้ป่วย COPD ที่ถูกมองข้ามบ่อยที่สุด |
| **มลพิษอากาศภายนอก** (PM2.5, NO2, โอโซน) | ราว 50% ของ attributable risk ใน LMIC · ในคนไม่สูบบุหรี่เป็นปัจจัยอันดับ 1 · ไม่มีระดับที่ปลอดภัย · กระตุ้น exacerbation | หมอกควันภาคเหนือ การเผาในที่โล่ง |
| **ฝุ่น/สารเคมีจากอาชีพ** | 10–20% ของ COPD · 31% ในคนไม่สูบบุหรี่ · ยาฆ่าแมลงขนาดสูง | เกษตรกรพ่นยา โรงสี เหมือง ก่อสร้าง |
| **วัณโรคปอดเก่า** | ทำลายหลอดลมและเนื้อปอด (fibrosis, traction bronchiectasis) → obstruction ถาวร · COPD เสี่ยงเป็น TB 3 เท่า | พบบ่อยมากในไทย — ประวัติ TB ต้องถามทุกราย |
| **ปอดโตไม่เต็มที่** | คลอดก่อนกำหนด น้ำหนักแรกเกิดน้อย ติดเชื้อรุนแรงในวัยเด็ก หอบหืดในเด็ก → peak lung function ต่ำ | — |
| **Alpha-1 antitrypsin deficiency** (SERPINA1) | ขาดตัวยับยั้ง neutrophil elastase → panlobular emphysema ตั้งแต่อายุน้อย | พบน้อยมากในเอเชีย (รายละเอียดหัวข้อ 13) |
| อื่น ๆ | HIV · ฐานะยากจน · อายุ (สะสม exposure) · asthma ในผู้ใหญ่เสี่ยง COPD 12 เท่า | — |

### การคำนวณ pack-year
**pack-year = (จำนวนมวนต่อวัน ÷ 20) × จำนวนปีที่สูบ** · เช่น 10 มวน/วัน นาน 30 ปี = 0.5 × 30 = **15 pack-year** · การศึกษาส่วนใหญ่ใช้ ≥ 10 pack-year เป็นเกณฑ์ แต่ GOLD 2026 ชี้ว่าแม้ < 10 pack-year ก็เพิ่มความเสี่ยงได้

> ใครควรได้ spirometry (GOLD 2026 สนับสนุน **active case-finding** ไม่ใช่ screening คนทั่วไป): ผู้ที่มี **อาการทางเดินหายใจเรื้อรังที่ไม่มีคำอธิบาย** หรือมี **ปัจจัยเสี่ยงชัด** (สูบ > 20 pack-year, ติดเชื้อทางเดินหายใจส่วนล่างซ้ำ, ปัจจัยวัยเด็ก) — การตรวจ spirometry ในคนที่ไม่มีอาการและไม่มีปัจจัยเสี่ยงไม่แนะนำ""",
    ["COPD = อาการเรื้อรัง + airflow obstruction ที่คงอยู่ · ยืนยันด้วย post-BD FEV1/FVC < 0.7",
     "ครึ่งหนึ่งของ COPD ทั่วโลกไม่ได้มาจากบุหรี่ — ถามควันฟืน/ถ่าน ฝุ่นอาชีพ PM2.5 และประวัติวัณโรคทุกครั้ง",
     "pack-year = (มวน/วัน ÷ 20) × ปี",
     "COPD เกิดได้ทั้งจากปอดเสื่อมเร็ว และจากปอดโตไม่เต็มที่ตั้งแต่เด็ก",
     "> 80% ของผู้ป่วยยังไม่ได้รับการวินิจฉัย — ให้ทำ spirometry ในคนที่มีอาการหรือปัจจัยเสี่ยง"],
    [mcq(N(1), "A 62-year-old Thai woman from a rural village has had progressive exertional breathlessness and morning cough for 3 years. She has never smoked; her husband smokes outdoors. For 35 years she has cooked over a wood and charcoal stove in a poorly ventilated kitchen. Post-bronchodilator FEV1/FVC is 0.61. Which exposure is most likely to be the principal cause of her disease?",
         ["Alpha-1 antitrypsin deficiency", "Household biomass smoke from cooking", "Undiagnosed childhood asthma", "Outdoor second-hand smoke from her husband", "Obesity-related small airway closure"], 1,
         "ผู้หญิงไม่สูบบุหรี่ที่ **หุงต้มด้วยฟืน/ถ่านในครัวปิดมานาน** ได้รับอนุภาคและก๊าซพิษขนาดสูงทุกวัน ซึ่งกระตุ้นการอักเสบแบบเดียวกับควันบุหรี่ · GOLD 2026 ระบุว่าในประเทศรายได้ต่ำ–ปานกลาง บุหรี่อธิบายได้แค่ 30–40% และ **ปัจจัยที่ไม่ใช่บุหรี่รวมกันเกินครึ่งของ COPD ทั่วโลก**\n\n"
         "- *AATD* — พบน้อยมากในเอเชีย และมักเกิด emphysema ตั้งแต่อายุ < 45 ปี\n- *asthma ในเด็ก* — เป็นปัจจัยเสี่ยงได้ แต่ไม่มีประวัติชี้นำ\n"
         "- *ควันบุหรี่มือสองนอกบ้าน* — ขนาด exposure น้อยกว่าควันในครัวทุกวันหลายสิบปีมาก\n- *อ้วน* — ทำให้ปริมาตรปอดลด (restrictive) ไม่ทำให้ FEV1/FVC ต่ำ",
         "ผู้หญิงไม่สูบบุหรี่ + ครัวฟืน/ถ่าน = นึกถึง biomass COPD", "Risk factors", R("Chapter 1 Causes and risk factors (biomass exposure)"), [COPD, COPDB]),
     mcq(N(2), "A 72-year-old man smoked 15 hand-rolled cigarettes per day from the age of 30 until he stopped at the age of 70. How many pack-years has he smoked?",
         ["15 pack-years", "30 pack-years", "40 pack-years", "60 pack-years", "600 pack-years"], 1,
         "สูบ 40 ปี (อายุ 30–70) · 15 มวน/วัน = 15 ÷ 20 = **0.75 ซอง/วัน** · **0.75 × 40 = 30 pack-year**\n\n"
         "- *15* — คูณด้วย 20 ปีแทน 40 ปี\n- *40* — เอาจำนวนปีมาตอบตรง ๆ\n- *60* — คิดว่า 1 ซองมี 10 มวน (15 ÷ 10 × 40)\n- *600* — ลืมหารด้วย 20 (15 × 40)",
         "pack-year = (มวน/วัน ÷ 20) × ปี · ยาเส้นมวนเองนับเป็นมวนได้", "Pack-year", ["หลักการคำนวณ pack-year (ไม่อยู่ใน GOLD โดยตรง)"], [TOB, COPD])],
    [COPD, COPDB, TOB],
    {"trajectory": F.trajectory()})

# ───────────────────────────── 2
sec("chest-copd-02", "พยาธิสรีรวิทยา — จากควันถึงลมค้าง ปอดพอง และออกซิเจนต่ำ",
    "อักเสบ neutrophil/macrophage/CD8 · protease–antiprotease · small airway disease + emphysema · air trapping · dynamic hyperinflation · V/Q · PH", 11,
"""### 1. การอักเสบและการทำลาย
- ควันและอนุภาคกระตุ้น **macrophage และเซลล์เยื่อบุ** หลั่ง chemokine ดึง **neutrophil** และ **CD8 T cell** เข้ามา (ต่างจาก asthma ที่เป็น eosinophil/Th2) — บางคนมี eosinophil สูง (T2) ซึ่งตอบสนองต่อ ICS
- เซลล์อักเสบหลั่ง **protease** (neutrophil elastase, MMP-12) ทำลาย **elastin** เกินกว่าที่ **antiprotease** (α1-antitrypsin) จะต้านไหว + **oxidative stress** จากควันเองและจากเซลล์อักเสบ
- การอักเสบ **ยังดำเนินต่อแม้เลิกบุหรี่แล้ว** (autoantigen, dysbiosis) — แต่เลิกบุหรี่ยังชะลอการเสื่อมได้มากที่สุด

### 2. สองตำแหน่งที่เสีย — airway และ alveoli
| ตำแหน่ง | สิ่งที่เกิด | ผล |
|---|---|---|
| **หลอดลมใหญ่** (chronic bronchitis) | goblet cell และต่อมเมือกโตเพิ่ม cilia เสีย | ไอมีเสมหะเรื้อรัง ติดเชื้อง่าย |
| **small airway** (< 2 mm) | ผนังอักเสบหนา พังผืดรอบหลอดลม เมือกอุด จำนวนหลอดลมเล็กลดลง | **แรงต้านทาน ↑** = ตำแหน่งหลักของ obstruction |
| **ถุงลม** (emphysema) | ผนังถุงลมถูกย่อย ถุงลมรวมเป็นโพรง · **centrilobular** (บุหรี่ กลีบบน) · **panlobular** (AATD กลีบล่าง) | **elastic recoil ↓** · เสียพื้นที่แลกเปลี่ยนก๊าซ (DLco ↓) |
| **หลอดเลือดปอด** | intimal hyperplasia ตั้งแต่ระยะแรก · capillary bed หาย | pulmonary hypertension ระยะท้าย |

[[fig:tethering]]

### 3. ลมค้างและปอดพอง (air trapping → hyperinflation)
- ลมออกได้ช้าเพราะ **แรงต้านสูง + แรงดีดกลับต่ำ + หลอดลมแฟบ** → ลมค้างเมื่อหมดลมหายใจออก (**RV ↑ ตั้งแต่ระยะแรก**) → ปริมาตรปอดที่พักสูงขึ้น (**static hyperinflation**, FRC/TLC ↑)
- ตอนออกแรงหายใจเร็ว เวลาหายใจออกไม่พอ ลมสะสมเพิ่มทีละครั้ง = **dynamic hyperinflation** — GOLD 2026 ระบุว่าสัมพันธ์กับความเหนื่อย ความทนต่อการออกกำลังลดลง การ admit การหายใจล้มเหลว และการตาย มากกว่าค่า FEV1

[[fig:dyn_hyper]]

### 4. ก๊าซในเลือดผิดปกติ — V/Q mismatch เป็นกลไกหลัก
- ถุงลมที่หลอดลมตีบ/เสมหะอุดได้ลมน้อยแต่ยังมีเลือดไหล (**low V/Q**) → เลือดออกจากปอดมี O2 ต่ำ = **hypoxemia** (แก้ได้ด้วย O2 ไม่มากเพราะไม่ใช่ shunt แท้)
- emphysema ทำลายทั้งถุงลมและหลอดเลือด → พื้นที่ระบายอากาศที่ไม่มีเลือด (**high V/Q, dead space ↑**) → ต้องหายใจมากขึ้นเพื่อขับ CO2 เท่าเดิม
- ระยะท้าย หรือช่วง exacerbation กล้ามเนื้อหายใจล้า (ภาระสูง กะบังลมแบนเสียเปรียบ) → **alveolar ventilation ไม่พอ → CO2 คั่ง (hypercapnia)** · ร่างกายชดเชยด้วยการเก็บ HCO3 ที่ไต (chronic respiratory acidosis)
- ยานอนหลับ/opioid ที่กดศูนย์หายใจ ทำให้ hypercapnic respiratory failure ได้ง่าย

### 5. ผลนอกปอด
[[fig:cor_chain]]

- **systemic inflammation** + ไม่ได้ขยับร่างกาย + hypoxemia → กล้ามเนื้อลีบ น้ำหนักลด (cachexia) กระดูกพรุน ซีดจากโรคเรื้อรัง ซึมเศร้า
- ปอดพองกดหลอดเลือดดำใหญ่และหัวใจ ลด venous return และ cardiac output · COPD เพิ่มโรคหัวใจหลอดเลือดทุกชนิด โดยเฉพาะหลัง exacerbation""",
    ["Obstruction ใน COPD = small airway disease (แรงต้าน ↑) + emphysema (elastic recoil ↓) ในสัดส่วนต่างกันแต่ละคน",
     "หลอดลมเล็กเปิดอยู่ได้เพราะผนังถุงลมยึดดึง — emphysema ทำลายแรงดึงนี้ หลอดลมจึงแฟบตอนหายใจออก",
     "Dynamic hyperinflation: ออกแรง → เวลาหายใจออกสั้น → ลมสะสม → IC แคบ = เหนื่อย",
     "Hypoxemia ใน COPD มาจาก V/Q mismatch เป็นหลัก · hypercapnia มาจาก alveolar hypoventilation เมื่อกล้ามเนื้อหายใจล้า",
     "HPV + capillary bed ถูกทำลาย → pulmonary hypertension → cor pulmonale"],
    [mcq(N(3), "Which mechanism best explains the reduced FEV1 in a patient with predominantly emphysematous COPD?",
         ["Reversible contraction of bronchial smooth muscle in response to allergens",
          "Loss of elastic recoil and of alveolar attachments, so small airways collapse early during forced expiration",
          "Stiff chest wall that limits the volume that can be inhaled",
          "Fixed narrowing of the trachea that limits both inspiratory and expiratory flow equally",
          "Increased surfactant production that lowers alveolar surface tension"], 1,
         "emphysema ทำลาย elastin ในผนังถุงลม → **แรงดีดกลับที่ขับลมออกลดลง** และ **ผนังถุงลมที่เคยยึดดึงหลอดลมเล็กให้เปิดหายไป** · ตอนเป่าแรง แรงดันในช่องอกบวกบีบหลอดลมเล็กที่ไม่มีกระดูกอ่อนให้แฟบก่อนลมออกหมด FEV1 จึงลดมาก\n\n"
         "- *กล้ามเนื้อเรียบหดตัวจาก allergen* — กลไกของ asthma ซึ่งกลับคืนได้\n- *ผนังทรวงอกแข็ง* — restrictive ทำให้ FVC ลดพอ ๆ กับ FEV1 อัตราส่วนปกติ\n"
         "- *หลอดลมใหญ่ตีบคงที่* — upper airway obstruction flow-volume loop แบนทั้งบนและล่าง\n- *surfactant เพิ่ม* — ทำให้ถุงลมเปิดง่ายขึ้น ไม่ใช่สาเหตุ obstruction",
         "Emphysema = recoil หาย + tethering หาย → dynamic airway collapse", "Pathophysiology", R("Chapter 1 Pathophysiology — airflow obstruction and gas trapping"), [COPDB, MECH]),
     mcq(N(4), "A 67-year-old man with COPD (FEV1 48% predicted) says that his breathlessness becomes intolerable after climbing one flight of stairs, although he feels comfortable at rest. Which change during exercise best explains his symptom?",
         ["A fall in end-expiratory lung volume that increases inspiratory capacity",
          "Development of a right-to-left intracardiac shunt",
          "Progressive rise in end-expiratory lung volume because expiratory time shortens, reducing inspiratory capacity",
          "Sudden bronchospasm triggered by cold air in every patient with COPD",
          "Reduced production of carbon dioxide by exercising muscles"], 2,
         "ออกแรง → หายใจเร็ว → **เวลาหายใจออกสั้นลง** ขณะที่ COPD ต้องใช้เวลาหายใจออกนาน ลมจึงออกไม่หมด **EELV สูงขึ้นทีละจังหวะ (dynamic hyperinflation)** · inspiratory capacity แคบ ปริมาตรหายใจเข้าชนเพดาน TLC กล้ามเนื้อหายใจทำงานในช่วงที่เสียเปรียบ = เหนื่อยหายใจเข้าไม่อิ่ม\n\n"
         "- *EELV ลดลง* — ตรงข้าม เกิดในคนปกติตอนออกกำลัง\n- *right-to-left shunt* — ไม่ใช่กลไกปกติของ COPD\n"
         "- *bronchospasm จากอากาศเย็นทุกคน* — เป็น exercise-induced bronchoconstriction ใน asthma\n- *CO2 ลดลง* — ออกกำลังผลิต CO2 มากขึ้น ยิ่งต้องระบายมากขึ้น",
         "เหนื่อยตอนออกแรงใน COPD = dynamic hyperinflation · ยาขยายหลอดลมและ pursed-lip ช่วยลดตรงนี้", "Dynamic hyperinflation", R("Chapter 1 Pathophysiology — hyperinflation"), [COPDB, MECH, DYS])],
    [COPDB, MECH, GAS, O2T, RF],
    {"tethering": F.tethering(), "dyn_hyper": F.dyn_hyper(), "cor_chain": F.cor_chain()})

# ───────────────────────────── 3
sec("chest-copd-03", "อาการและการตรวจร่างกาย — ทำไมถึงมีอาการนี้",
    "เหนื่อยตอนออกแรง · ไอเรื้อรัง · barrel chest · pursed-lip · Hoover sign · หายใจออกยาว · เขียว · cor pulmonale · CO2 คั่ง · น้ำหนักลด", 11,
"""### อาการที่พบ (GOLD 2026)
- **เหนื่อยเรื้อรัง (dyspnea)** = อาการหลัก ค่อยเป็นค่อยไป เกิดตอนออกแรงก่อน ผู้ป่วยบรรยายว่า "ต้องออกแรงหายใจ แน่นหนัก หายใจไม่อิ่ม" — มักปรับชีวิตหลบอาการจนมาหาแพทย์ช้า
- **ไอเรื้อรัง** มักเป็นอาการแรก ผู้ป่วยคิดว่า "ไอเพราะสูบบุหรี่" · มีเสมหะเหนียวปริมาณน้อย ~30% · **เสมหะปริมาณมากทุกวัน** ให้นึกถึง bronchiectasis ร่วม
- หวีด แน่นหน้าอก (ไม่มีก็ไม่ตัด COPD มีก็ไม่ได้แปลว่าเป็น asthma) · อ่อนเพลีย · "หวัดลงคอนานทุกหน้าหนาว"
- ระยะรุนแรง: **น้ำหนักลด กล้ามเนื้อลีบ เบื่ออาหาร** (ต้องแยกวัณโรคและมะเร็งปอดเสมอ) · ขาบวม (cor pulmonale) · ซึมเศร้า วิตกกังวล
- ไอแรงจนหมดสติ (cough syncope) หรือซี่โครงหักได้

### การตรวจร่างกาย
GOLD 2026 ย้ำว่า **การตรวจร่างกายแทบไม่เคยใช้วินิจฉัย COPD** — อาการแสดงจะชัดเมื่อการทำงานปอดเสียไปมากแล้ว ระยะแรกอาจตรวจปกติทั้งหมด

[[fig:diaphragm]]

#### ทำไมถึงมีอาการนี้
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **เหนื่อยเวลาออกแรง** ค่อย ๆ มากขึ้น | dynamic hyperinflation (หัวข้อ 2) + กล้ามเนื้อขาเสื่อมจากไม่ได้ใช้ + hypoxemia ตอนออกแรง | asthma เหนื่อยเป็นพัก ๆ มีช่วงปกติ · HF มี orthopnea/PND · ILD เหนื่อยแบบหายใจตื้นเร็ว |
| **ไอมีเสมหะเรื้อรัง** ตอนเช้า | goblet cell/ต่อมเมือกโต + cilia เสีย เสมหะค้างทั้งคืน ไอออกตอนตื่น | เสมหะมากเป็นถ้วย มีกลิ่น ไอเป็นเลือด = bronchiectasis · ไข้ น้ำหนักลด = TB |
| **หายใจออกยาว (prolonged expiration) + wheeze** | ลมผ่านหลอดลมที่ตีบ/แฟบช้า ใช้เวลานาน ลมไหลเร็วผ่านช่องแคบทำให้ผนังสั่นเกิดเสียง · forced expiratory time > 6 วินาทีบ่งชี้ obstruction | wheeze ใน COPD มักเบาและไม่หายหมดหลังพ่นยา · asthma หวีดดังและหายได้ |
| **เสียงหายใจเบา เคาะโปร่ง (hyperresonance) ตับต่ำลง เสียงหัวใจเบา** | ปอดพองมีลมมาก เนื้อปอดที่นำเสียงน้อย ปอดดันกะบังลมและตับลง คลุมหัวใจ | pneumothorax ก็เคาะโปร่งแต่เป็นข้างเดียว |
| **อกถังเบียร์ (barrel chest)** AP diameter ≈ lateral | hyperinflation ทำให้ทรวงอกค้างในท่าหายใจเข้า | — |
| **Hoover sign** — ขอบซี่โครงล่างหุบเข้าตอนหายใจเข้า | กะบังลมแบน หดตัวแล้วดึงขอบซี่โครงเข้าแทนการกดอวัยวะช่องท้องลง | บ่งว่ามี hyperinflation รุนแรง |
| **ใช้กล้ามเนื้อช่วยหายใจ นั่งโน้มตัวเท้าแขน (tripod)** | กะบังลมแบนออกแรงไม่ได้ ต้องใช้ sternocleidomastoid/scalene ยกทรวงอก การเท้าแขนยึดไหล่ให้ pectoralis ช่วยได้ | ทุกภาวะเหนื่อยรุนแรง |
| **เป่าปากหายใจออก (pursed-lip)** | เพิ่มแรงดันย้อนในหลอดลม ดัน equal pressure point ไปหลอดลมใหญ่ หลอดลมเล็กไม่แฟบ + หายใจช้าลง | จำเพาะต่อ obstruction รุนแรง (ดูภาพด้านล่าง) |
| **เขียว (central cyanosis)** | V/Q mismatch → SaO2 ต่ำ · deoxy-Hb > 5 g/dL เห็นที่ลิ้นและริมฝีปาก · ยิ่งเห็นง่ายถ้ามี polycythemia | peripheral cyanosis (ลิ้นปกติ) = เลือดไหลช้า ไม่ใช่ปอด |
| **ขาบวม JVP สูง ตับโต P2 ดัง RV heave** = **cor pulmonale** | hypoxic vasoconstriction + capillary bed หาย → pulmonary hypertension → RV ล้ม · hypercapnia ทำให้ไตเก็บเกลือและน้ำเพิ่ม | ต้องแยก left HF (crepitation, S3, orthopnea, BNP สูงมาก) — มีร่วมกันได้บ่อย |
| **CO2 คั่ง**: ปวดหัวตอนเช้า ง่วงซึม สับสน มือสั่นกระตุก (**flapping tremor/asterixis**) มือเท้าอุ่น ชีพจรแรง | CO2 ขยายหลอดเลือด (สมอง → ปวดหัว, ปลายมือ → อุ่น) · CO2 ข้ามเข้าสมองทำให้ pH ใน CSF ต่ำ = CO2 narcosis | ซึมใน COPD ต้องเจาะ ABG เสมอ ไม่ใช่แค่ดู SpO2 |
| **น้ำหนักลด กล้ามเนื้อลีบ** | งานการหายใจสูงใช้พลังงานมาก + systemic inflammation (TNF-α) สลายกล้ามเนื้อ + กินได้น้อยเพราะเหนื่อยเวลากิน | GOLD 2026: **ต้องแยกวัณโรคและมะเร็งปอดเสมอ** · BMI < 21 พยากรณ์โรคแย่ |
| **นิ้วปุ้ม (clubbing)** | **COPD เองไม่ทำให้เกิด clubbing** | ถ้าพบ ให้หา **มะเร็งปอด bronchiectasis ILD หรือ lung abscess** |

[[fig:pursed_lip]]

> ภาพจำแบบเดิม "**pink puffer** (emphysema ผอม หายใจเร็ว เป่าปาก ออกซิเจนพอ) vs **blue bloater** (chronic bronchitis อ้วน เขียว บวม CO2 คั่ง)" เป็นปลายสุดสองขั้วที่ช่วยจำกลไก แต่ผู้ป่วยจริงส่วนใหญ่อยู่ระหว่างกลาง — GOLD ไม่ใช้จัดประเภทการรักษา""",
    ["การตรวจร่างกายไม่ใช้วินิจฉัย COPD — อาการแสดงปรากฏเมื่อโรคเป็นมากแล้ว ต้องใช้ spirometry",
     "Barrel chest · Hoover sign · ใช้กล้ามเนื้อช่วยหายใจ · tripod = ผลของ hyperinflation และกะบังลมแบน",
     "Pursed-lip ดัน equal pressure point ไปหลอดลมใหญ่ที่มีกระดูกอ่อน หลอดลมเล็กจึงไม่แฟบ",
     "Cor pulmonale = PH จาก hypoxic vasoconstriction + capillary bed หาย → RV ล้ม (ขาบวม JVP สูง P2 ดัง)",
     "COPD ไม่ทำให้นิ้วปุ้ม · น้ำหนักลด → แยกวัณโรคและมะเร็งปอด"],
    [mcq(N(5), "During inspiration, the lower lateral rib margins of a patient with severe COPD move inward instead of outward. What is the mechanism of this sign?",
         ["Paralysis of the phrenic nerve", "A flattened diaphragm whose contraction pulls the lower ribs inward",
          "Paradoxical movement of a flail segment after rib fractures", "Contraction of the abdominal muscles during inspiration to assist ventilation",
          "Pleural effusion pushing the lower ribs medially"], 1,
         "นี่คือ **Hoover sign** · ปกติกะบังลมเป็นโดม ส่วนที่แนบผนังทรวงอก (zone of apposition) ทำให้การหดตัวดันซี่โครงล่างออก · ใน hyperinflation **กะบังลมแบนราบ** เส้นแรงของใยกล้ามเนื้อวิ่งเข้าหาแนวกลาง การหดตัวจึง **ดึงขอบซี่โครงล่างเข้า**\n\n"
         "- *phrenic nerve palsy* — กะบังลมข้างนั้นไม่หดตัว ท้องบุ๋มตอนหายใจเข้า (paradoxical abdomen) ไม่ใช่ซี่โครงหุบ\n- *flail chest* — ต้องมีกระดูกซี่โครงหักหลายจุด ส่วนที่หักบุ๋มเฉพาะที่\n"
         "- *กล้ามเนื้อท้องหดตอนหายใจเข้า* — กล้ามเนื้อท้องช่วยตอนหายใจออก\n- *pleural effusion* — ไม่ทำให้ซี่โครงเคลื่อนเข้าตอนหายใจเข้า",
         "Hoover sign = กะบังลมแบนจาก hyperinflation", "Physical signs", R("Chapter 1 Hyperinflation; Chapter 2 Physical examination"), [COPD, MECH]),
     mcq(N(6), "A 66-year-old man with long-standing COPD (GOLD 3) attends clinic for routine follow-up. You notice new finger clubbing that was not present one year ago. He has lost 4 kg. What is the most appropriate next step?",
         ["Reassure him that clubbing is a typical feature of advanced COPD", "Increase his inhaled corticosteroid dose",
          "Investigate for lung cancer with chest imaging", "Start long-term oxygen therapy", "Test for alpha-1 antitrypsin deficiency"], 2,
         "**COPD เองไม่ทำให้นิ้วปุ้ม** · clubbing ที่เกิดใหม่ร่วมกับน้ำหนักลดในผู้สูบบุหรี่ต้องคิดถึง **มะเร็งปอด** ก่อน (รวมถึง bronchiectasis, lung abscess, ILD) · GOLD 2026: COPD (โดยเฉพาะ emphysema) เป็นปัจจัยเสี่ยงอิสระของมะเร็งปอด และน้ำหนักลด **ต้องสืบค้นวัณโรคและมะเร็งปอดเสมอ**\n\n"
         "- *ปลอบว่าเป็นธรรมดาของ COPD* — ผิด ทำให้พลาดมะเร็ง\n- *เพิ่ม ICS* — ไม่แก้สาเหตุ\n- *LTOT* — ต้องมีหลักฐาน hypoxemia ก่อน\n- *ตรวจ AATD* — ไม่เกี่ยวกับ clubbing",
         "COPD + clubbing = หามะเร็งปอด/bronchiectasis", "Physical signs", R("Chapter 2 Additional clinical features; Chapter 5 Lung cancer"), [COPD, WL, CXR])],
    [COPD, DYS, COUGH, CYAN, WL, MECH],
    {"diaphragm": F.diaphragm(), "pursed_lip": F.pursed_lip()})

# ───────────────────────────── 4
sec("chest-copd-04", "วินิจฉัยด้วย spirometry — อ่านค่า FEV1/FVC เกรด GOLD 1–4 และการตรวจอื่นที่ต้องรู้",
    "post-BD FEV1/FVC < 0.7 · pre-BD ใช้ exclude · reversibility ไม่ใช้แยก asthma · PEF ใช้วินิจฉัยไม่ได้ · CXR · SpO2 ≤ 92% → ABG · AATD", 11,
"""### Spirometry คือการตรวจที่ขาดไม่ได้
GOLD 2026: สงสัย COPD ในคนที่มี **เหนื่อย ไอเรื้อรัง มีเสมหะ ติดเชื้อทางเดินหายใจส่วนล่างซ้ำ และ/หรือมีปัจจัยเสี่ยง** แต่ **การวินิจฉัยต้องใช้ forced spirometry ที่ได้ post-bronchodilator FEV1/FVC < 0.7 เสมอ (mandatory)**

[[fig:spiro_vt]]

| ค่า | ความหมาย | ใน COPD |
|---|---|---|
| **FVC** | ปริมาตรที่เป่าออกได้ทั้งหมดจากหายใจเข้าสุด | ลดเล็กน้อย (ลมค้าง) |
| **FEV1** | ปริมาตรที่เป่าออกในวินาทีแรก | **ลดมาก** (ลมออกช้า) |
| **FEV1/FVC** | สัดส่วนที่ออกในวินาทีแรก ปกติ ≥ 0.7–0.8 | **< 0.7** = obstruction |
| **FEV1 % predicted** | เทียบค่าอ้างอิงตามอายุ เพศ ส่วนสูง (GOLD 2026 แนะนำสมการ GLI-Global ซึ่งไม่แยกเชื้อชาติ) | ใช้แบ่ง **เกรด** ความรุนแรงของการอุดกั้น |

#### ขั้นตอนตามแนวทาง GOLD 2026
1. ทำ **pre-bronchodilator** ก่อนได้ — ถ้า **ไม่มี obstruction ก็ตัด COPD ออกได้** ไม่ต้องทำ post-BD (ยกเว้นสงสัยมาก)
2. ถ้า pre-BD มี obstruction → ให้ยาขยายหลอดลม (เช่น salbutamol 400 µg) แล้ววัดซ้ำ → **post-BD FEV1/FVC < 0.7 = ยืนยัน COPD**
3. pre-BD obstruction แต่ post-BD ไม่ obstruction → ยังไม่ใช่ COPD แต่เสี่ยงในอนาคต ติดตามใกล้ชิด
4. ค่า post-BD อยู่ระหว่าง **0.6–0.8 ควรตรวจซ้ำอีกครั้ง** (ค่าแกว่งตามชีววิทยา) · ถ้า < 0.6 แทบไม่กลับขึ้นเกิน 0.7
- **ไม่ใช้ระดับ reversibility (ΔFEV1) แยก asthma กับ COPD และไม่ใช้ทำนายการตอบสนองต่อยา** · ไม่ต้องหยุดยาพ่นก่อนทำ spirometry ตอนติดตามผล
- fixed ratio 0.7 อาจวินิจฉัยเกินในผู้สูงอายุ (อัตราส่วนลดตามวัย) และวินิจฉัยขาดในคนอายุน้อย — GOLD ยังเลือก fixed ratio เพราะง่ายและใช้ในงานวิจัยทั้งหมด

#### เกรดความรุนแรงของการอุดกั้น (ใช้เมื่อ FEV1/FVC < 0.7)
| เกรด | post-BD FEV1 % predicted |
|---|---|
| GOLD 1 mild | ≥ 80% |
| GOLD 2 moderate | 50–79% |
| GOLD 3 severe | 30–49% |
| GOLD 4 very severe | < 30% |

> เกรด GOLD 1–4 บอก "ความรุนแรงของการอุดกั้น" ซึ่ง **ไม่เท่ากับความรุนแรงของโรค** — อาการและ exacerbation สัมพันธ์กับ FEV1 อย่างอ่อน การเลือกยาจึงใช้กลุ่ม ABE (หัวข้อ 5)

[[fig:flow_vol]]

### การตรวจอื่นที่ควรรู้
| การตรวจ | ใช้ทำอะไร |
|---|---|
| **Peak expiratory flow (PEF)** | **ใช้วินิจฉัย COPD อย่างเดียวไม่ได้** — ไวแต่ไม่จำเพาะ แยก obstructive/restrictive ไม่ได้ · ใช้ร่วมแบบสอบถามเพื่อคัดกรองเมื่อไม่มี spirometry |
| **Chest X-ray** | **ไม่ใช้วินิจฉัย** แต่ใช้แยกโรคอื่นและหาโรคร่วม (มะเร็ง TB HF bronchiectasis) · ลักษณะของ hyperinflation: **กะบังลมแบนราบ ช่องลมหลังกระดูกอกกว้าง (lateral film) ปอดดำโปร่ง หลอดเลือดเรียวลงเร็ว** หัวใจเรียวยาว · อาจเห็น bulla |
| **Pulse oximetry → ABG** | **SpO2 ≤ 92% ให้เจาะ ABG** (SpO2 ไม่ตรงกับ SaO2 เสมอ และไม่บอก PaCO2/pH) · ใช้ประเมิน LTOT |
| **CBC** | eosinophil (เลือก ICS) · Hct สูง (polycythemia) · ซีด |
| **ECG / echo / NT-proBNP** | หาโรคหัวใจร่วมและ cor pulmonale (P pulmonale, right axis, RVH) |
| **Alpha-1 antitrypsin** | GOLD แนะนำตรวจทุกคนที่วินิจฉัย COPD (ทำได้จำกัดในไทย — สำคัญมากถ้าอายุ < 45 ปี emphysema กลีบล่าง ไม่สูบบุหรี่ หรือมีประวัติครอบครัว) |
| **DLco, lung volume, CT** | เมื่ออาการไม่สมกับ FEV1 หรือวางแผนรักษาเฉพาะ (หัวข้อ 13) |""",
    ["วินิจฉัย COPD = post-bronchodilator FEV1/FVC < 0.7 · pre-BD ปกติใช้ตัด COPD ออกได้",
     "เกรด GOLD 1–4 ใช้ FEV1 %pred: ≥ 80 · 50–79 · 30–49 · < 30 — บอกความรุนแรงของการอุดกั้น ไม่ใช่ใช้เลือกยา",
     "Reversibility ไม่ใช้แยก asthma/COPD · PEF ใช้วินิจฉัยอย่างเดียวไม่ได้",
     "CXR ไม่ใช้วินิจฉัย แต่ใช้แยกโรค · hyperinflation = กะบังลมแบน retrosternal space กว้าง",
     "SpO2 ≤ 92% → เจาะ ABG"],
    [mcq(N(7), "A 64-year-old ex-smoker with exertional dyspnea has post-bronchodilator spirometry: FEV1 1.50 L (52% predicted), FVC 2.90 L (80% predicted), FEV1/FVC 0.52. How should this result be classified?",
         ["Airflow obstruction, GOLD grade 1 (mild)", "Airflow obstruction, GOLD grade 2 (moderate)", "Airflow obstruction, GOLD grade 3 (severe)",
          "Airflow obstruction, GOLD grade 4 (very severe)", "Restrictive ventilatory defect"], 1,
         "ขั้นแรก **FEV1/FVC 0.52 < 0.7** = มี airflow obstruction (FVC 80% ไม่ได้บ่ง restriction) · ขั้นที่สองแบ่งเกรดด้วย **post-BD FEV1 52% → อยู่ช่วง 50–79% = GOLD 2 (moderate)**\n\n"
         "- *GOLD 1* — ต้อง FEV1 ≥ 80%\n- *GOLD 3* — 30–49%\n- *GOLD 4* — < 30%\n- *Restrictive* — FEV1 และ FVC ลดพอกัน อัตราส่วนปกติหรือสูง (ยืนยันด้วย TLC)",
         "อ่าน ratio ก่อน แล้วจึงดู FEV1 %pred เพื่อแบ่งเกรด", "Spirometry", R("Chapter 2 Spirometry; Assessing severity of airflow obstruction"), [SPIRO, SPIROB, COPD]),
     mcq(N(8), "A 58-year-old smoker with chronic cough and exertional breathlessness is seen at a district hospital that has only a peak flow meter. His peak expiratory flow is 62% of predicted. What is the most appropriate next step?",
         ["Diagnose COPD and start a long-acting antimuscarinic agent today", "Arrange forced spirometry with a bronchodilator to confirm airflow obstruction",
          "Give oral prednisolone for 2 weeks; improvement confirms COPD", "Order a chest radiograph, which is diagnostic if it shows hyperinflation",
          "Measure arterial blood gas to diagnose COPD"], 1,
         "GOLD 2026: **spirometry ที่ได้ post-BD FEV1/FVC < 0.7 เป็นสิ่งที่ต้องมีเพื่อวินิจฉัย** · PEF แม้ไว แต่ **ไม่จำเพาะ** และแยก obstructive กับ restrictive ไม่ได้ จึงใช้วินิจฉัยเพียงอย่างเดียวไม่ได้ · ระหว่างรอ ให้ยาบรรเทาอาการ (SABA) และแนะนำเลิกบุหรี่ได้\n\n"
         "- *วินิจฉัยและเริ่ม LAMA เลย* — เสี่ยงวินิจฉัยผิด (HF, ILD, โรคอ้วนก็ทำให้ PEF ต่ำได้)\n- *ทดลอง steroid* — การตอบสนองต่อ steroid ไม่ใช้วินิจฉัยหรือแยก asthma กับ COPD\n"
         "- *CXR* — ไม่ไวและไม่จำเพาะ ใช้แยกโรคอื่น\n- *ABG* — บอกการแลกเปลี่ยนก๊าซ ไม่ได้บอก obstruction",
         "ไม่มี spirometry = ยังวินิจฉัย COPD ไม่ได้ · PEF ใช้คัดกรองเท่านั้น", "Diagnosis", R("Chapter 2 Diagnosis; Spirometry"), [SPIRO, SPIROB, COPD]),
     mcq(N(9), "Which chest radiograph finding is most consistent with lung hyperinflation in COPD?",
         ["Bilateral upper-lobe cavities with fibrosis", "Kerley B lines and upper-lobe venous diversion",
          "Flattened hemidiaphragms with an enlarged retrosternal air space on the lateral film", "Diffuse reticulonodular shadowing in the lower zones",
          "Unilateral absence of lung markings with a visible pleural line"], 2,
         "ปอดพองดัน **กะบังลมลงจนแบนราบ** (โดมสูงจากเส้นที่ลากระหว่างมุมทั้งสอง < 1.5 cm) และ **ช่องลมหลังกระดูกอกกว้าง** ใน lateral film · อาจเห็นปอดโปร่งดำ หลอดเลือดเรียวลงเร็ว หัวใจแคบยาว — GOLD 2026 ระบุว่าใช้แยกโรค ไม่ใช่วินิจฉัย\n\n"
         "- *cavity + fibrosis กลีบบน* — วัณโรค (ทั้งโรคเก่าและโรคใหม่)\n- *Kerley B + upper lobe diversion* — หัวใจล้มซีกซ้าย\n- *reticulonodular กลีบล่าง* — ILD\n- *pleural line ไม่มี lung markings* — pneumothorax (ภาวะแทรกซ้อนของ bulla)",
         "CXR ใน COPD: กะบังลมแบน + retrosternal air space กว้าง", "Chest radiograph", R("Chapter 2 Additional investigations — imaging"), [CXR, COPD])],
    [SPIRO, SPIROB, CXR, ABG, COPD],
    {"spiro_vt": F.spiro_vt(), "flow_vol": F.flow_vol()})

# ───────────────────────────── 5
sec("chest-copd-05", "ประเมินผู้ป่วยหลังวินิจฉัย — mMRC, CAT และกลุ่ม ABE แบบ GOLD 2026",
    "ประเมิน 5 ด้าน · mMRC 0–4 · CAT 0–40 · exacerbation moderate/severe · E = ≥ 1 ครั้ง (ใหม่ 2026) · eosinophil · โรคร่วม", 9,
"""### ประเมิน 5 ด้านเพื่อเลือกการรักษา (GOLD 2026)
1. **ความรุนแรงของการอุดกั้น** — เกรด GOLD 1–4
2. **อาการ** — mMRC หรือ CAT
3. **ประวัติ exacerbation ระดับ moderate และ severe ในปีที่ผ่านมา**
4. **Blood eosinophil count** — ใช้เลือก ICS
5. **โรคร่วม (multimorbidity)** — หัวใจ เบาหวาน กระดูกพรุน ซึมเศร้า มะเร็งปอด

### เครื่องมือวัดอาการ
| mMRC | เหนื่อยเมื่อ |
|---|---|
| 0 | ออกกำลังหนักเท่านั้น |
| 1 | เดินเร็วบนพื้นราบหรือขึ้นเนินเล็กน้อย |
| 2 | เดินช้ากว่าคนวัยเดียวกันบนพื้นราบ หรือต้องหยุดหายใจเมื่อเดินตามจังหวะตัวเอง |
| 3 | ต้องหยุดหายใจหลังเดินราว 100 เมตร หรือไม่กี่นาที |
| 4 | เหนื่อยจนออกจากบ้านไม่ได้ หรือเหนื่อยตอนแต่งตัว |

- **mMRC** วัดเฉพาะความเหนื่อย · **≥ 2 = เหนื่อยมาก** (ตารางเป็นคำแปลมาตรฐานของ mMRC ซึ่งในรายงานเป็นรูป)
- **CAT (COPD Assessment Test, ปัจจุบันเรียก CAAT)** 8 ข้อ ข้อละ 0–5 (ไอ เสมหะ แน่นหน้าอก เหนื่อยขึ้นบันได กิจกรรมในบ้าน ความมั่นใจออกนอกบ้าน การนอน พลังงาน) รวม 0–40 · **≥ 10 = อาการมาก** (เทียบ SGRQ ≥ 25) · GOLD แนะนำแบบวัดหลายมิติมากกว่า mMRC เพราะ COPD กระทบมากกว่าแค่เหนื่อย

### Exacerbation — ระดับที่นับ
- **moderate** = ต้องใช้ **systemic steroid และ/หรือ antibiotic** (รักษานอก รพ.) · **severe** = ต้อง **admit หรือมาห้องฉุกเฉิน**
- ตัวทำนาย exacerbation ครั้งหน้าที่ดีที่สุด = **ประวัติ exacerbation ในปีก่อน** — GOLD 2026 ย้ำว่า **แม้ครั้งเดียวก็เพิ่มความเสี่ยง** ทำให้ปอดเสื่อมเร็วและเพิ่มการตาย

[[fig:abe]]

### กลุ่ม ABE (ใช้กับผู้ป่วยที่ยังไม่เคยได้ยา maintenance)
| กลุ่ม | เกณฑ์ |
|---|---|
| **E** | **exacerbation moderate หรือ severe ≥ 1 ครั้งในปีที่ผ่านมา** (ไม่สนใจระดับอาการ) |
| **A** | ไม่มี exacerbation · mMRC 0–1 หรือ CAT < 10 |
| **B** | ไม่มี exacerbation · mMRC ≥ 2 หรือ CAT ≥ 10 |

> **สิ่งที่เปลี่ยนใน GOLD 2026**: ฉบับ 2023–2025 กำหนดกลุ่ม E = moderate ≥ 2 ครั้ง หรือ admit ≥ 1 ครั้ง · ฉบับ 2026 **ปรับให้ moderate exacerbation ครั้งเดียวก็เข้ากลุ่ม E** เพราะข้อมูล observational ใหม่พบว่าครั้งเดียวก่อนเริ่มยาก็เพิ่มความเสี่ยงครั้งต่อไป · กลุ่ม C/D เดิมรวมเป็น E ตั้งแต่ 2023 แล้ว
> ข้อสอบเก่าและตำราที่อ้าง GOLD ฉบับก่อนยังใช้เกณฑ์ ≥ 2 — อ่านโจทย์ให้ดีว่าอ้างฉบับไหน

- เกรด spirometry **ไม่ได้ใช้จัดกลุ่ม** แล้ว (ทำนายรายบุคคลได้ไม่แม่น) แต่ยังบันทึกคู่กัน เช่น "COPD GOLD 3, group E"
- เป้าหมายใหม่ของ GOLD 2026 = **low disease activity**: ไม่มี exacerbation · อาการไม่แย่ลง · FEV1 ไม่ลดเร็วกว่าวัย""",
    ["ประเมิน 5 ด้าน: เกรด spirometry · อาการ · exacerbation · eosinophil · โรคร่วม",
     "mMRC ≥ 2 หรือ CAT ≥ 10 = อาการมาก",
     "GOLD 2026: exacerbation moderate (steroid/antibiotic) หรือ severe (admit) แม้ 1 ครั้ง = กลุ่ม E",
     "เกรด GOLD 1–4 ไม่ใช้จัดกลุ่ม ABE — ใช้บอกความรุนแรงของการอุดกั้น",
     "ประวัติ exacerbation ในปีก่อน = ตัวทำนาย exacerbation ครั้งหน้าที่ดีที่สุด"],
    [mcq(N(10), "A 63-year-old man with newly confirmed COPD (post-bronchodilator FEV1 72% predicted) has an mMRC score of 1 and a CAT score of 8. Six months ago he was treated by his general practitioner with oral prednisolone and amoxicillin-clavulanate for a flare of cough and breathlessness; he was not admitted. According to GOLD 2026, which group is he in?",
         ["Group A", "Group B", "Group E", "Group C", "Group D"], 2,
         "การรักษาด้วย **steroid และ antibiotic = exacerbation ระดับ moderate** · GOLD 2026 ปรับเกณฑ์ให้ **moderate เพียง 1 ครั้งในปีที่ผ่านมาก็เป็นกลุ่ม E** ไม่ว่าอาการจะน้อย (mMRC 1, CAT 8)\n\n"
         "- *A* — จะถูกต้องถ้าไม่มี exacerbation (และเป็นคำตอบตามเกณฑ์ GOLD 2023–2025 ที่ต้อง ≥ 2 ครั้ง)\n- *B* — ต้องไม่มี exacerbation และอาการมาก\n- *C, D* — ระบบ ABCD เดิม ยกเลิกตั้งแต่ GOLD 2023",
         "GOLD 2026: 1 moderate exacerbation ก็เป็น E", "ABE assessment", R("Chapter 2 Combined initial COPD assessment; Report highlights iv"), [COPD]),
     mcq(N(11), "A 70-year-old woman with COPD has a CAT score of 18 and mMRC 2. Post-bronchodilator FEV1 is 38% predicted. She has had no exacerbations and no hospital admissions in the past two years. Which statement about her assessment is correct?",
         ["She is in group E because FEV1 is below 50% predicted", "She is in group B; the spirometric grade (GOLD 3) is recorded but does not determine the group",
          "She is in group A because she has had no exacerbations", "She cannot be grouped until her blood eosinophil count is known",
          "She is in group D because both symptoms and airflow obstruction are severe"], 1,
         "การจัดกลุ่มใช้ **ประวัติ exacerbation** ก่อน (ไม่มี) แล้วดู **อาการ** (CAT 18 ≥ 10, mMRC 2) → **กลุ่ม B** · FEV1 38% = **GOLD 3** บันทึกแยก (\"GOLD 3, group B\") แต่ **ไม่ได้ใช้จัดกลุ่ม** เพราะทำนายรายบุคคลได้ไม่แม่น\n\n"
         "- *E เพราะ FEV1 < 50%* — FEV1 ถูกถอดออกจากเกณฑ์ความเสี่ยงตั้งแต่ GOLD 2017\n- *A* — อาการมากจึงไม่ใช่ A\n- *ต้องรู้ eos ก่อน* — eos ใช้เลือก ICS ไม่ได้ใช้จัดกลุ่ม\n- *D* — ไม่มีในระบบ ABE",
         "จัดกลุ่ม = exacerbation + อาการ · เกรด spirometry บันทึกแยก", "ABE assessment", R("Chapter 2 Initial assessment; Combined initial COPD assessment"), [COPD, SPIRO])],
    [COPD, SPIRO],
    {"abe": F.abe()})

# ───────────────────────────── 6
sec("chest-copd-06", "แยกโรค — asthma, หัวใจล้ม, bronchiectasis, วัณโรคเก่า และอื่น ๆ",
    "asthma vs COPD · HF · bronchiectasis · post-TB · obliterative bronchiolitis · ไม่ใช้คำ asthma–COPD overlap แล้ว", 8,
"""### หลักคิด
airflow obstruction ที่ไม่กลับคืนเต็มที่ **ไม่จำเพาะต่อ COPD** (GOLD 2026) — asthma ที่เป็นมานาน วัณโรคเก่า bronchiectasis ก็ทำได้ · ต้องดูภาพรวม: อายุที่เริ่ม ปัจจัยเสี่ยง รูปแบบอาการ และภาพรังสี

[[fig:asthma_copd]]

| โรค | ลักษณะที่ชี้นำ | กลไกที่ทำให้แยกได้ |
|---|---|---|
| **COPD** | เริ่มวัยกลางคน (> 40 ปี) · สูบบุหรี่/ควันชีวมวล · เหนื่อยตอนออกแรงค่อย ๆ มากขึ้น | โครงสร้างถูกทำลาย → obstruction คงอยู่ |
| **Asthma** | เริ่มในวัยเด็ก · อาการแปรปรวนวันต่อวัน กลางคืน/เช้ามืด · ภูมิแพ้ จมูกอักเสบ eczema · ประวัติครอบครัว | การอักเสบ T2 + กล้ามเนื้อเรียบหดตัว → กลับคืนได้ |
| **Heart failure** | orthopnea, PND · crepitation ที่ฐานปอด · S3 · CXR หัวใจโต น้ำในปอด · NT-proBNP สูง · spirometry มักเป็นแบบ restrictive ไม่ใช่ obstructive | น้ำในถุงลม/ผนังหลอดลม ลด compliance |
| **Bronchiectasis** | **เสมหะปริมาณมาก** เป็นหนองทุกวัน ไอเป็นเลือด ติดเชื้อซ้ำ · crackles หยาบ · CT หลอดลมโตกว่าหลอดเลือดคู่กัน ผนังหนา | วงจรติดเชื้อ–อักเสบ–ทำลายผนัง · พบร่วมกับ COPD ได้ 20–69% |
| **วัณโรคปอด/TB sequelae** | อาศัยในพื้นที่ระบาด เคยรักษา TB · CXR แผลเป็น fibrocalcific กลีบบน · ไข้ น้ำหนักลด (ถ้า active) | แผลเป็นและ traction bronchiectasis → obstruction ถาวร · GOLD นับเป็นทั้งปัจจัยเสี่ยง โรคแยก และโรคร่วม |
| **Obliterative bronchiolitis** | อายุน้อย ไม่สูบบุหรี่ · หลังปลูกถ่ายปอด/ไขกระดูก สูดสารพิษ rheumatoid arthritis · CT หายใจออกเห็นลมค้างเป็นหย่อม (mosaic) | หลอดลมเล็กมีพังผืดอุด |
| **Diffuse panbronchiolitis** | ชาวเอเชียตะวันออก เพศชาย ไม่สูบบุหรี่ · ไซนัสอักเสบเรื้อรัง · CT จุดเล็ก ๆ กระจาย (tree-in-bud) | ตอบสนองต่อ macrolide |

ตารางนี้เป็นเนื้อหาของรูป Differential diagnosis ใน GOLD (รูปอ่านจากไฟล์ 2026 ไม่ได้ ใช้ตามฉบับ 2025 ซึ่งเนื้อหาเดียวกัน) · โรคที่ทำให้เหนื่อยแบบไม่มี obstruction: ซีด อ้วน กล้ามเนื้อเสื่อม ILD pulmonary embolism เรื้อรัง ต้องคิดเสมอเมื่ออาการไม่สมกับ FEV1

### Asthma ร่วมกับ COPD
- GOLD 2026 **เลิกใช้คำ "asthma–COPD overlap"** — ถือว่าเป็น 2 โรคที่อาจเกิดร่วมกันในคนเดียว
- นึกถึง asthma ร่วมเมื่อมี: ประวัติ asthma ในวัยเด็ก ภูมิแพ้ ประวัติครอบครัว หวีดแปรปรวน eosinophil สูง · ค่า BD reversibility และ eosinophil **แยกสองโรคไม่ได้แน่นอน**
- **ถ้ามี asthma ร่วม ต้องรักษาตามแนวทาง asthma — ICS จำเป็น** (ห้ามใช้ LABA เดี่ยว ๆ ใน asthma เพราะเพิ่มการตาย)""",
    ["Obstruction ไม่กลับคืนไม่จำเพาะต่อ COPD — asthma นาน วัณโรคเก่า bronchiectasis ก็ทำได้",
     "Asthma: เริ่มเด็ก แปรปรวน ภูมิแพ้ · COPD: > 40 ปี มี exposure ค่อย ๆ แย่ลง",
     "HF: orthopnea PND crepitation BNP สูง · spirometry มักไม่ obstructive",
     "Bronchiectasis: เสมหะมากทุกวัน ไอเป็นเลือด CT หลอดลมโต",
     "มี asthma ร่วม → รักษาแบบ asthma ต้องมี ICS"],
    [mcq(N(12), "A 68-year-old ex-smoker (20 pack-years) presents with 3 months of breathlessness. He now sleeps on three pillows and wakes at night gasping. Examination shows bibasal fine crackles, a raised jugular venous pressure and pitting ankle edema. Post-bronchodilator FEV1/FVC is 0.78 with a reduced FVC. What is the most likely explanation of his breathlessness?",
         ["Moderate COPD with cor pulmonale", "Left-sided heart failure", "Asthma with fixed airflow obstruction",
          "Bronchiectasis", "Pre-COPD"], 1,
         "**orthopnea + PND + crepitation ที่ฐานปอด + JVP สูง + ขาบวม** = หัวใจล้ม · **FEV1/FVC 0.78 ≥ 0.7** จึงไม่มี airflow obstruction ไม่ใช่ COPD · FVC ลดเพราะน้ำในปอดทำให้ปอดแข็ง (restrictive) — ส่ง NT-proBNP และ echocardiography\n\n"
         "- *COPD with cor pulmonale* — ต้องมี ratio < 0.7 และ cor pulmonale ไม่ทำให้ crepitation/orthopnea แบบนี้\n- *asthma with fixed obstruction* — ต้องมี obstruction\n"
         "- *bronchiectasis* — เสมหะมากทุกวัน crackles หยาบ\n- *pre-COPD* — มีอาการ/ภาพผิดปกติแต่ ratio ปกติ ใช้เมื่อไม่มีคำอธิบายอื่น ที่นี่อธิบายได้ด้วย HF",
         "Ratio ≥ 0.7 = ไม่ใช่ COPD · orthopnea/PND/crepitation → หัวใจ", "Differential diagnosis", R("Chapter 2 Differential diagnosis; Chapter 5 Heart failure"), [COPD, DYS]),
     mcq(N(13), "A 55-year-old Thai farmer who has never smoked completed treatment for smear-positive pulmonary tuberculosis 8 years ago. He now has exertional breathlessness. Sputum AFB and GeneXpert are negative. Chest radiograph shows bilateral upper-zone fibrocalcific scarring unchanged from 2 years ago. Post-bronchodilator FEV1/FVC is 0.60. Which statement is most appropriate?",
         ["This is relapsed tuberculosis and anti-tuberculosis treatment should be restarted", "Spirometry is invalid in patients with previous tuberculosis",
          "Chronic airflow obstruction after tuberculosis is recognised; treat with bronchodilators, and use inhaled corticosteroids only with caution after excluding active TB",
          "He should receive high-dose inhaled corticosteroid as first-line therapy", "His obstruction must be asthma because he has never smoked"], 2,
         "GOLD 2026: **วัณโรคปอดทำให้เกิด chronic airflow obstruction ได้** (แผลเป็น traction bronchiectasis การอักเสบของ small airway) เรียกว่า TB-associated COPD · รักษาด้วย **ยาขยายหลอดลม** ตามหลัก COPD · **ICS โดยเฉพาะขนาดสูงเพิ่มความเสี่ยงวัณโรคกำเริบ** ในพื้นที่ระบาดและในคนที่มีแผลเป็น TB — ต้องแยก active TB ก่อนเริ่มและติดตาม\n\n"
         "- *TB กลับเป็นซ้ำ* — เสมหะลบและภาพไม่เปลี่ยน ไม่มีหลักฐาน\n- *spirometry ใช้ไม่ได้* — ใช้ได้ตามปกติ\n- *ICS ขนาดสูงเป็นยาแรก* — ไม่ใช่ยาแรกของ COPD และเสี่ยง TB\n- *ต้องเป็น asthma* — COPD ไม่ได้เกิดจากบุหรี่อย่างเดียว",
         "ประวัติ TB + obstruction = TB-associated COPD · ICS ระวัง TB", "Post-TB airflow obstruction", R("Chapter 1 Infections; Chapter 5 Pulmonary tuberculosis"), [COPD, "B6.2.2(8)"])],
    [COPD, ASTHMA, ASTHMAB, LRTI, "B6.2.2(8)"],
    {"asthma_copd": F.asthma_copd()})

# ───────────────────────────── 7
sec("chest-copd-07", "ยาที่ใช้ใน COPD — กลไกที่ receptor ผลข้างเคียง และการใช้ inhaler ให้ถูก",
    "SABA/SAMA · LABA/LAMA · ICS · theophylline · mucolytic · pMDI สูดช้า · DPI สูดแรง · spacer · teach-back", 12,
"""[[fig:receptors]]

### กลุ่มยาหลัก
| กลุ่ม | ตัวอย่าง | ออกฤทธิ์ | ใช้เมื่อ | ผลข้างเคียงและกลไก |
|---|---|---|---|---|
| **SABA** | salbutamol, terbutaline | เริ่มในไม่กี่นาที อยู่ 4–6 ชม. | บรรเทาอาการ (reliever) ทุกกลุ่ม · ยาแรกใน exacerbation | ใจสั่น tachycardia (β1 ข้ามมาบ้าง + reflex จากหลอดเลือดขยาย) · มือสั่น (β2 ที่กล้ามเนื้อลาย) · **K ต่ำ** (β2 กระตุ้น Na/K-ATPase ดึง K เข้าเซลล์) · ระวังกระตุ้น AF |
| **SAMA** | ipratropium | 6–8 ชม. | reliever · คู่กับ SABA ใน exacerbation | ปากแห้ง |
| **LABA** | salmeterol, formoterol (12 ชม.) · indacaterol, olodaterol, vilanterol (24 ชม.) | ยาวนาน | maintenance | เหมือน SABA แต่น้อยกว่า |
| **LAMA** | tiotropium, umeclidinium, glycopyrronium (24 ชม.) | ยาวนาน · ลด exacerbation ได้ดีกว่า LABA เดี่ยว | maintenance | ปากแห้ง · **ปัสสาวะคั่งในต่อมลูกหมากโต** · ต้อหินมุมปิดเฉียบพลันถ้าพ่นละอองผ่าน mask เข้าตา |
| **ICS** (ใช้ร่วมกับ LABA/LAMA เท่านั้นใน COPD) | budesonide, fluticasone, beclometasone | ลดการอักเสบแบบ T2 | ผู้ที่มี exacerbation + eosinophil สูง | เชื้อราในปาก เสียงแหบ (ยาตกค้างในคอ — บ้วนปาก ใช้ spacer) · **pneumonia** (พบมากกว่าใน COPD) · TB/NTM · น้ำตาลขึ้น ต้อกระจก กระดูกพรุน (ขนาดสูง) |
| **Methylxanthine** | theophylline, doxofylline | ขยายหลอดลมน้อย | ทางเลือกเมื่อไม่มียาพ่น | **therapeutic index แคบ**: คลื่นไส้ ใจสั่น arrhythmia ชัก · ระดับยาเพิ่มเมื่อใช้ ciprofloxacin, macrolide, ตับแข็ง HF · ลดลงเมื่อสูบบุหรี่ · **ไม่ใช้ IV aminophylline ใน exacerbation** |
| **Mucolytic/antioxidant** | N-acetylcysteine, carbocysteine, erdosteine | ลดความหนืดเสมหะ ต้านออกซิแดนท์ | บางรายที่มีเสมหะมาก (ลด exacerbation ได้บ้าง) | น้อย |

#### ทำไมยาขยายหลอดลมช่วยเหนื่อยแม้ FEV1 เพิ่มน้อย
ยาคลายกล้ามเนื้อเรียบทำให้ลมออกได้เร็วขึ้นในแต่ละการหายใจ **ลม trapped ลดลง EELV ลด IC กว้างขึ้น** (deflation) — ผลต่ออาการจึงมากกว่าที่ตัวเลข FEV1 บอก · ใน COPD **vagal (cholinergic) tone สูง** antimuscarinic จึงได้ผลดี และ LABA + LAMA เสริมกันเพราะออกฤทธิ์คนละทาง

#### ทำไม ICS ไม่ได้ผลกับทุกคน
การอักเสบหลักของ COPD เป็นแบบ **neutrophil** ซึ่งตอบสนองต่อ steroid น้อย (oxidative stress จากควันลดการทำงานของ HDAC2 ที่ steroid ใช้ปิดยีนอักเสบ) · ผู้ที่ **eosinophil สูง** มีการอักเสบแบบ T2 ที่ steroid ระงับได้ จึงได้ประโยชน์ (หัวข้อ 8)

### Inhaler — ยาดีแค่ไหนก็ไม่ได้ผลถ้าสูดผิด
[[fig:inhaler]]

| อุปกรณ์ | วิธีสูดที่ถูก | ข้อผิดพลาดที่พบบ่อย |
|---|---|---|
| **pMDI** (ยาพ่นแบบกด) | เขย่า → หายใจออกให้สุด (ห่างจากหลอด) → อมปากหลอดให้สนิท → **กดพ่น 1 ครั้งพร้อมเริ่มสูดช้า ๆ ลึก ๆ 3–5 วินาที** → กลั้นหายใจ 5–10 วินาที → รอ 30–60 วินาทีก่อนพ่นซ้ำ | กดกับสูดไม่พร้อมกัน · สูดแรงเร็วเกิน · ไม่กลั้นหายใจ |
| **pMDI + spacer/VHC** | พ่นเข้ากระบอก แล้วสูดช้า ๆ ลึก ๆ หรือหายใจปกติ 4–5 ครั้ง | ช่วยคนที่จังหวะไม่ตรง · ลดยาตกค้างในคอ ลดเชื้อราจาก ICS |
| **DPI** (ผงแห้ง) | เปิด/บรรจุยา (เจาะแคปซูล) → หายใจออกให้สุด **ไม่เป่าใส่เครื่อง** (ผงจะชื้นจับก้อน) → **สูดแรงและเร็วตั้งแต่ต้น** → กลั้นหายใจ | สูดแรงไม่พอ (ผู้สูงอายุ/เหนื่อยมาก) · เป่าลมเข้าเครื่อง |
| **SMI** (Respimat) | ละอองช้า อยู่นาน สูดช้าและลึกแบบ pMDI | ประกอบตลับยาผิด |
| **Nebulizer** | หายใจปกติผ่าน mouthpiece/mask | ไม่ดีกว่า inhaler ถ้าผู้ป่วยใช้เป็น · ใช้ใน exacerbation หรือคนที่ใช้ inhaler ไม่ได้ |

- GOLD 2026: **มากกว่า 2 ใน 3 ใช้ผิดอย่างน้อย 1 ขั้น** · ต้อง **สาธิตให้ดูและให้ผู้ป่วยทำกลับ (teach-back)** ตรวจทุกครั้งที่นัด ให้นำยามาเอง
- เลือก device ตามแรงสูด มือ สายตา ความจำ และราคา · ถ้าใช้ device เดิมได้ ให้ยาใหม่ใน device เดิม · **อย่าเปลี่ยน device โดยไม่สอนใหม่** (เพิ่ม exacerbation)
- ICS ทุกชนิด: **บ้วนปาก กลั้วคอหลังพ่น** ลดเชื้อราและเสียงแหบ""",
    ["β2 agonist → cAMP ↑ → กล้ามเนื้อเรียบคลาย · antimuscarinic บล็อก M3 ที่ vagus กระตุ้น",
     "SABA ขนาดสูง: K ต่ำ มือสั่น ใจสั่น · antimuscarinic: ปากแห้ง ปัสสาวะคั่ง ต้อหินมุมปิด",
     "ICS ใน COPD ใช้ร่วมกับยาขยายหลอดลมเท่านั้น · ผลข้างเคียงสำคัญ = pneumonia, เชื้อราในปาก, TB",
     "pMDI/SMI สูดช้าลึก · DPI สูดแรงเร็ว ห้ามเป่าใส่เครื่อง · กลั้นหายใจ 5–10 วินาที",
     "ตรวจท่าพ่นยาด้วย teach-back ทุก visit — ก่อนเพิ่มยาทุกครั้ง"],
    [mcq(N(14), "Tiotropium improves airflow in COPD mainly by which mechanism?",
         ["Stimulating beta-2 receptors to increase intracellular cAMP", "Blocking M3 muscarinic receptors on airway smooth muscle, preventing acetylcholine-induced rises in intracellular calcium",
          "Inhibiting phosphodiesterase-4 in neutrophils", "Binding the glucocorticoid receptor and suppressing inflammatory gene transcription",
          "Antagonising leukotriene D4 receptors"], 1,
         "tiotropium = **LAMA** จับและบล็อก **M3 receptor** · acetylcholine จาก vagus ใช้ M3 → Gq → IP3 → Ca2+ ↑ ทำให้กล้ามเนื้อเรียบหดและต่อมเมือกหลั่ง · ใน COPD cholinergic tone สูง การบล็อกจึงขยายหลอดลมได้ดี และลด exacerbation\n\n"
         "- *กระตุ้น β2 → cAMP* — กลไกของ salbutamol/LABA\n- *ยับยั้ง PDE4* — roflumilast\n- *glucocorticoid receptor* — ICS\n- *leukotriene receptor* — montelukast ใช้ใน asthma",
         "LAMA = บล็อก M3 · LABA = กระตุ้น β2 · ใช้คู่กันเสริมฤทธิ์", "Bronchodilator pharmacology", R("Chapter 3 Pharmacological treatment (Appendix 3 อ่านไม่ได้ — หลักเภสัชวิทยา)"), [BD]),
     mcq(N(15), "A 74-year-old woman admitted with an exacerbation of COPD has received nebulised salbutamol every 1–2 hours for 12 hours. She has a fine tremor and a heart rate of 118/min. Serum potassium has fallen from 4.1 to 2.9 mmol/L. What is the mechanism of the hypokalaemia?",
         ["Renal potassium wasting caused by salbutamol", "Beta-2-mediated stimulation of Na+/K+-ATPase that shifts potassium into cells",
          "Gastrointestinal loss due to nausea and vomiting", "Respiratory alkalosis caused by hyperventilation alone", "Mineralocorticoid effect of ipratropium"], 1,
         "β2 agonist กระตุ้น **Na+/K+-ATPase** ที่กล้ามเนื้อลาย (ผ่าน cAMP) → **K ถูกดึงเข้าเซลล์ (transcellular shift)** ระดับในเลือดลดโดยปริมาณ K ในร่างกายไม่ได้ลด · มือสั่นเกิดจาก β2 ที่กล้ามเนื้อลายเช่นกัน · tachycardia จาก β1 ที่ข้ามมาบ้างและ reflex · ระวัง arrhythmia ถ้ามี hypoxemia/โรคหัวใจ — GOLD แนะนำไม่ให้ SABA ขนาดสูงเกิน\n\n"
         "- *ไตขับ K* — ไม่ใช่กลไกหลักของ salbutamol (steroid ที่ได้ร่วมเสริมได้บ้าง)\n- *สูญเสียทางเดินอาหาร* — ไม่มีประวัติ\n"
         "- *respiratory alkalosis* — ทำให้ K ต่ำได้เล็กน้อย ไม่อธิบายการลดลงมากแบบนี้\n- *ipratropium* — ไม่มีฤทธิ์ mineralocorticoid",
         "SABA ถี่ → K ต่ำจาก shift เข้าเซลล์ · ตรวจ K ใน exacerbation", "Bronchodilator adverse effects", R("Chapter 4 Bronchodilators"), [BD, AE]),
     mcq(N(16), "A 69-year-old man is prescribed a dry powder inhaler (DPI) containing LABA+LAMA. Which instruction is correct for this device?",
         ["Shake the inhaler and press the canister at the same time as a slow, deep breath", "Breathe out fully into the mouthpiece before inhaling so that the powder is loosened",
          "Breathe out away from the device, then inhale quickly and forcefully from the start, then hold the breath", "Use a large-volume spacer with the DPI to improve deposition",
          "Take several normal tidal breaths through the device over 1 minute"], 2,
         "DPI ไม่มีแรงขับในตัว ผงยาจะแตกเป็นอนุภาคเล็กพอลงปอดได้เมื่อ **ผู้ป่วยสูดแรงและเร็วจนเกิดลมหมุน (turbulence) ในเครื่อง** · ต้อง **หายใจออกห่างจากเครื่อง** ก่อน แล้วสูดแรงตั้งแต่ต้น กลั้นหายใจ 5–10 วินาที · ถ้าผู้ป่วยสูดแรงไม่พอ GOLD 2026 แนะนำเปลี่ยนเป็น pMDI + spacer หรือ SMI\n\n"
         "- *เขย่าและกดพ่นพร้อมสูดช้า* — วิธีของ pMDI\n- *เป่าลมเข้าเครื่อง* — ความชื้นทำให้ผงจับก้อน ยาเสีย\n- *ใช้ spacer กับ DPI* — spacer ใช้กับ pMDI เท่านั้น\n- *หายใจปกติหลายครั้ง* — วิธีของ spacer/nebulizer",
         "DPI = สูดแรงเร็ว · pMDI = สูดช้าลึก · ทั้งสองแบบไม่เป่าใส่เครื่อง", "Inhaler technique", R("Chapter 3 Managing inhaled therapy"), [BD, COPD])],
    [BD, ICS, "B6.4(3)", COPD],
    {"receptors": F.receptors(), "inhaler": F.inhaler()})

# ───────────────────────────── 8
sec("chest-copd-08", "ยาระยะคงที่ — เริ่มยาตามกลุ่ม ABE, เมื่อไรใช้ ICS และการปรับยาเบื้องต้น",
    "A = bronchodilator · B = LABA+LAMA · E = LABA+LAMA (eos ≥ 300 → triple) · ไม่ใช้ LABA+ICS · SABA ทุกคน · ปรับยาตาม dyspnea/exacerbation", 10,
"""### เป้าหมายของการรักษา
**ลดอาการ** (เหนื่อย ทนออกกำลังได้ คุณภาพชีวิต) และ **ลดความเสี่ยงในอนาคต** (exacerbation ปอดเสื่อม ตาย) · GOLD 2026 เพิ่มเป้า **low disease activity** = ไม่มี exacerbation อาการไม่แย่ลง FEV1 ไม่ลดเร็ว

[[fig:initial_rx]]

### ยาเริ่มต้น (ผู้ที่ยังไม่เคยได้ยา — GOLD 2026)
| กลุ่ม | ยาเริ่มต้น | เหตุผล |
|---|---|---|
| **A** | ยาขยายหลอดลม 1 ตัว (short หรือ long-acting · **long-acting ดีกว่าถ้ามีและจ่ายได้** ยกเว้นเหนื่อยนาน ๆ ครั้ง) | อาการน้อย ความเสี่ยงต่ำ · ใช้ต่อถ้าได้ผล |
| **B** | **LABA + LAMA** | RCT: ในคน CAT ≥ 10 ดีกว่า LAMA เดี่ยวหลายด้าน · ถ้าใช้ combination ไม่ได้ เลือก LABA หรือ LAMA ตามที่ผู้ป่วยรู้สึกดีขึ้น · **หาโรคร่วม** ที่เพิ่มความเหนื่อย |
| **E** | **LABA + LAMA** · พิจารณา **LABA + LAMA + ICS ถ้า eosinophil ≥ 300 cells/µL** | LABA+LAMA ลด exacerbation ดีที่สุดในกลุ่มยาขยายหลอดลม · ICS ได้ประโยชน์ชัดเมื่อ eos สูง |
| ทุกกลุ่ม | **SABA (หรือ SAMA) สำหรับบรรเทาอาการ** | — |

- **LABA + ICS ไม่แนะนำใน COPD** — ถ้ามีข้อบ่งชี้ ICS ให้ใช้ **triple (LABA+LAMA+ICS)** ซึ่งดีกว่า · triple ในอุปกรณ์เดียว (single-inhaler) ดีกว่าหลายอุปกรณ์
- **มี asthma ร่วม → รักษาแบบ asthma ICS จำเป็น**
- ในสิทธิการรักษาของไทย LABA+LAMA บางชนิดอาจเข้าถึงยาก — หลักการยังเหมือนเดิม: เริ่มจาก long-acting bronchodilator ที่มี

### ICS — ใช้ eosinophil ร่วมกับประวัติ exacerbation
[[fig:eos_ics]]

- **eos ≥ 300**: ได้ประโยชน์มากสุด · เริ่ม triple ได้ตั้งแต่แรกในกลุ่ม E
- **eos ≥ 100** และยังมี exacerbation บน LABA+LAMA: เพิ่ม ICS เป็น triple (ยิ่ง eos สูงยิ่งได้ผล)
- **eos < 100**: ICS ได้ประโยชน์น้อย เสี่ยง pneumonia มากกว่า
- **ระวัง/ไม่ใช้ ICS**: pneumonia ซ้ำ · ประวัติ TB/NTM หรือ TB sequelae (GOLD 2026: ICS ขนาดสูงเพิ่มความเสี่ยง TB ในพื้นที่ระบาด) · ค่าระดับเหล่านี้มาจากข้อความ GOLD 2026 ส่วนรายการ "against" มาจากรูปของ GOLD 2025

### ติดตามและปรับยา (หลักการระดับ NL)
วงจร **Review → Assess → Adjust**
1. **Review**: อาการ (CAT/mMRC) exacerbation eosinophil
2. **Assess**: **ท่าพ่นยา adherence** การสูบบุหรี่ โรคร่วม — แก้สิ่งเหล่านี้ก่อนเพิ่มยาเสมอ
3. **Adjust**: ดู "ปัญหาหลัก" (ไม่ต้องจัดกลุ่ม ABE ใหม่)
   - **ยังเหนื่อย** บนยาเดี่ยว → **LABA + LAMA** · ยังเหนื่อยต่อ → เปลี่ยนอุปกรณ์/ตัวยา ส่ง pulmonary rehab หาสาเหตุอื่น
   - **ยังมี exacerbation** บนยาเดี่ยว → **LABA + LAMA** · บน LABA+LAMA และ **eos ≥ 100 → เพิ่ม ICS (triple)**
   - มีทั้งสองปัญหา → ใช้เส้นทาง exacerbation
- ทำ spirometry อย่างน้อยปีละครั้ง ไม่ต้องหยุดยาก่อนตรวจ · รายละเอียดขั้นถัดไป (azithromycin, roflumilast, biologics) อยู่ในหัวข้อ 12 อ่านเพิ่มเติม""",
    ["A: bronchodilator 1 ตัว · B: LABA+LAMA · E: LABA+LAMA (+ICS ถ้า eos ≥ 300)",
     "ไม่ใช้ LABA+ICS ใน COPD — ถ้าต้องมี ICS ให้ triple",
     "ICS: ประโยชน์เพิ่มตาม eosinophil · ≥ 100 เพิ่มได้เมื่อยัง exacerbate · ระวัง pneumonia และ TB",
     "ก่อนเพิ่มยาทุกครั้ง: ตรวจท่าพ่นยา adherence การสูบบุหรี่",
     "ปรับยาตามปัญหาหลัก: เหนื่อย → LABA+LAMA + rehab · exacerbation → LABA+LAMA → triple"],
    [mcq(N(17), "A 61-year-old woman with newly diagnosed COPD (post-bronchodilator FEV1 58% predicted) has a CAT score of 17 and no exacerbations in the past year. Blood eosinophil count is 150 cells/µL. Which initial maintenance treatment is recommended by GOLD 2026, provided there are no issues of cost or availability?",
         ["As-needed salbutamol only", "LABA + inhaled corticosteroid", "LABA + LAMA", "LABA + LAMA + inhaled corticosteroid", "Oral theophylline"], 2,
         "ไม่มี exacerbation + CAT ≥ 10 = **กลุ่ม B** → **LABA + LAMA** เป็นยาเริ่มต้นที่แนะนำ (RCT ดีกว่า LAMA เดี่ยว) · พร้อม SABA สำหรับบรรเทาอาการ\n\n"
         "- *SABA อย่างเดียว* — ใช้ได้เฉพาะกลุ่ม A ที่เหนื่อยนาน ๆ ครั้ง\n- *LABA + ICS* — GOLD ไม่แนะนำใน COPD\n- *triple* — ใช้ในกลุ่ม E ที่ eos ≥ 300 ไม่ใช่กลุ่ม B ที่ eos 150\n- *theophylline* — ผลน้อย ผลข้างเคียงมาก ไม่ใช่ยาแรก",
         "กลุ่ม B = LABA+LAMA", "Initial pharmacotherapy", R("Chapter 3 Initial pharmacological management (Figure 3.8)"), [COPD, BD]),
     mcq(N(18), "A 66-year-old man with newly diagnosed COPD (FEV1 46% predicted, CAT 14) was admitted once last year for an exacerbation. He has never received maintenance inhalers. Blood eosinophils are 380 cells/µL. Which initial maintenance regimen is most appropriate?",
         ["LAMA alone", "LABA + ICS", "LABA + LAMA + ICS", "Oral prednisolone 5 mg daily", "Azithromycin 250 mg daily"], 2,
         "admit 1 ครั้ง = **กลุ่ม E** · ยาเริ่มต้นของกลุ่ม E คือ LABA+LAMA แต่ **ถ้า eosinophil ≥ 300 ให้พิจารณา triple (LABA+LAMA+ICS) ตั้งแต่แรก** เพราะการอักเสบแบบ T2 ตอบสนองต่อ ICS และ triple ลด exacerbation (และลดตายในกลุ่มที่ exacerbate บ่อย/รุนแรง)\n\n"
         "- *LAMA เดี่ยว* — ไม่พอสำหรับกลุ่ม E\n- *LABA + ICS* — ไม่แนะนำ triple ดีกว่า\n- *prednisolone ระยะยาว* — ไม่มีประโยชน์ มีผลเสียมาก\n- *azithromycin* — เป็นยาเสริมขั้นถัดไปในคนที่ยัง exacerbate บนยาพ่นเต็มที่",
         "กลุ่ม E + eos ≥ 300 → เริ่ม triple ได้", "Initial pharmacotherapy", R("Chapter 3 Initial pharmacological management — Group E"), [COPD, BD, ICS]),
     mcq(N(19), "A 70-year-old man with COPD has used a LABA+LAMA inhaler correctly and regularly for 1 year. He has had two exacerbations treated with prednisolone in the past 12 months. He stopped smoking 5 years ago. Blood eosinophil count is 240 cells/µL. What is the most appropriate change?",
         ["Switch to LABA + ICS", "Add an inhaled corticosteroid (triple therapy)", "Stop the LAMA and add theophylline",
          "Add regular nebulised salbutamol four times daily", "No change; exacerbations are expected"], 1,
         "ใช้ยาถูกวิธีและสม่ำเสมอแล้ว ยังมี exacerbation บน **LABA+LAMA** และ **eos ≥ 100 (240)** → GOLD 2026 แนะนำ **เพิ่ม ICS เป็น LABA+LAMA+ICS** · ประโยชน์จะมากขึ้นตาม eos\n\n"
         "- *เปลี่ยนเป็น LABA + ICS* — เสีย LAMA ไป และไม่แนะนำใน COPD\n- *หยุด LAMA เพิ่ม theophylline* — ลดประสิทธิภาพ เพิ่มพิษ\n"
         "- *nebulised SABA ประจำ* — ไม่ลด exacerbation\n- *ไม่เปลี่ยน* — เป้าหมาย GOLD 2026 คือไม่มี exacerbation",
         "LABA+LAMA ยัง exacerbate + eos ≥ 100 → triple", "Follow-up pharmacotherapy", R("Chapter 3 Follow-up pharmacological management (Figure 3.9)"), [COPD, ICS])],
    [COPD, BD, ICS],
    {"initial_rx": F.initial_rx(), "eos_ics": F.eos_ics()})

# ───────────────────────────── 9
sec("chest-copd-09", "การรักษาที่ไม่ใช่ยา — เลิกบุหรี่ วัคซีน pulmonary rehab LTOT โภชนาการ และเมื่อไรส่งต่อ",
    "5A/5R · NRT varenicline · วัคซีน influenza pneumococcal RSV · rehab 6–8 สัปดาห์ · LTOT PaO2 ≤ 55 · BMI · โรคร่วม · referral", 13,
"""### 1. เลิกบุหรี่ — การรักษาที่เปลี่ยนการดำเนินโรคได้มากที่สุด
- ราว **40% ของผู้ป่วย COPD ยังสูบอยู่** · เลิกได้แล้วอาการดีขึ้น exacerbation ลด FEV1 ลดช้าลง และ **ลดการตาย** (Lung Health Study)
- คนที่เป็น COPD เลิกยากกว่า (ติดนิโคตินมากกว่า ซึมเศร้าบ่อย) · **counseling + ยา ได้ผลดีที่สุด** (อัตราเลิก 1 ปี: ไม่ทำอะไร 1.4% · แนะนำสั้น 2.6% · counseling เข้มข้น 6% · counseling + ยา 12.3%) · แม้แนะนำ **3 นาที** ก็เพิ่มอัตราเลิก
- ติดนิโคตินมาก: สูบภายใน 30 นาทีหลังตื่น · สูบกลางคืน · ≥ 20 มวน/วัน · Fagerström 7–10

| 5A (พร้อมเลิก) | 5R (ยังไม่พร้อม — สร้างแรงจูงใจ) |
|---|---|
| **Ask** ถามการสูบทุกครั้ง | **Relevance** โยงกับตัวผู้ป่วย (ลูกหลาน อาการตัวเอง) |
| **Advise** แนะนำชัดเจนให้เลิก | **Risks** ผลเสียระยะสั้น/ยาว ควันมือสอง |
| **Assess** ความพร้อม ระดับการติด | **Rewards** ประโยชน์ที่ได้ (เหนื่อยน้อยลง ประหยัดเงิน) |
| **Assist** วันเลิก ยา counseling สายเลิกบุหรี่ **1600** | **Roadblocks** อุปสรรค (อยาก น้ำหนักขึ้น ความเครียด) |
| **Arrange** นัดติดตาม (สัปดาห์แรก) | **Repetition** ย้ำทุกครั้งที่พบ |

- **ยา** (ตารางยาใน GOLD Appendix อ่านไม่ได้ — ใช้ตามแนวทางทั่วไป): **nicotine replacement** (แผ่นแปะ หมากฝรั่ง อม — ให้นิโคตินโดยไม่มีสารพิษอื่น) · **varenicline** (partial agonist ที่ α4β2 nicotinic receptor ลดอาการอยากและลดความพอใจเมื่อสูบ — ได้ผลดีที่สุดตัวเดียว) · **bupropion** (ยับยั้งการเก็บกลับ dopamine/noradrenaline · ห้ามในผู้ที่ชักง่าย) · nortriptyline · cytisine
- **ไม่มีหลักฐานว่า e-cigarette ช่วยเลิกได้และปลอดภัย** (GOLD 2026) · การกลับไปสูบซ้ำพบบ่อย เป็นธรรมชาติของการติด ไม่ใช่ความล้มเหลว
- ลด exposure อื่น: **เตาหุงต้มไร้ควัน/ใช้ก๊าซแทนฟืน เปิดครัวให้อากาศถ่ายเท** · อุปกรณ์ป้องกันในงาน · หลีกเลี่ยงออกนอกบ้านวัน PM2.5 สูง

### 2. วัคซีน (GOLD 2026 — อัปเดต RSV และ influenza)
| วัคซีน | คำแนะนำ | กลไกประโยชน์ |
|---|---|---|
| **Influenza** ทุกปี | ทุกคน (ชนิดเชื้อตาย/inactivated) | ลด LRTI ที่ต้อง admit ลดการตาย ลด exacerbation · ลดโรคหัวใจขาดเลือด |
| **Pneumococcal** | ทุกคนอายุ ≥ 50 ปี และอายุ 19–49 ปีที่มีโรคปอดเรื้อรัง · **GOLD แนะนำ PCV20 หรือ PCV21** (หรือ PCV13/15 แล้วตาม PPSV23) | ลด pneumonia และ exacerbation |
| **RSV** | อายุ ≥ 75 ปีทุกคน · 50–74 ปีที่มีโรคปอด/หัวใจเรื้อรัง | RSV ทำให้ราว 9% ของ exacerbation และกระตุ้นหัวใจล้ม |
| **Tdap** | ผู้ที่ไม่เคยได้ตอนวัยรุ่น (COPD เสี่ยงไอกรน) | — |
| **Zoster, COVID-19** | ตามคำแนะนำของประเทศ | — |

### 3. Pulmonary rehabilitation
- = **ฝึกออกกำลังกาย (แกนหลัก) + ความรู้ + การจัดการตนเอง** · ดีขึ้นทุกระดับความรุนแรง: เหนื่อยน้อยลง ทนออกกำลังได้มากขึ้น คุณภาพชีวิตดีขึ้น ลดวิตกกังวล
- ข้อบ่งชี้: **กลุ่ม B และ E** (อาการมาก/เสี่ยง exacerbation) · **หลัง admit ด้วย exacerbation ภายใน 4 สัปดาห์ ลดการ admit ซ้ำและลดการตาย**
- **6–8 สัปดาห์** (12 สัปดาห์ไม่ดีกว่า) · ฝึกมีผู้ดูแลอย่างน้อย 2 ครั้ง/สัปดาห์ · endurance + resistance แขนขา เดิน · ประเมินด้วย 6-minute walk test
- กลไก: กล้ามเนื้อขาที่ฝึกแล้วใช้ออกซิเจนเก่งขึ้น ผลิตกรด lactic ช้าลง → ต้องหายใจน้อยลงที่งานเท่าเดิม → hyperinflation น้อยลง · ลดความกลัวเหนื่อย (วงจร เหนื่อย → ไม่ขยับ → กล้ามเนื้อเสื่อม → ยิ่งเหนื่อย)

### 4. Long-term oxygen therapy (LTOT)
[[fig:ltot]]

- **ข้อบ่งชี้ (ตอน stable)**: **PaO2 ≤ 55 mmHg หรือ SaO2 ≤ 88%** (ยืนยัน 2 ครั้งในช่วง 3 สัปดาห์) · หรือ **PaO2 55–60 mmHg/SaO2 88% + pulmonary hypertension, ขาบวมจาก cor pulmonale หรือ Hct > 55%** → ให้ **> 15 ชั่วโมงต่อวัน**
- **ยืดชีวิตได้** (NOTT, MRC) เพราะแก้ hypoxic pulmonary vasoconstriction ชะลอ PH และ polycythemia · คนที่ออกซิเจนต่ำปานกลางไม่ได้ประโยชน์ (LOTT) · 24 ชม. ไม่ดีกว่า 15 ชม.
- ประเมินซ้ำที่ 60–90 วัน · **ห้ามสูบบุหรี่/จุดไฟใกล้ออกซิเจน** · เดินทางโดยเครื่องบินได้เกือบทุกคน (อาจต้องเพิ่ม O2)

### 5. โภชนาการ การออกกำลังกาย และสุขภาพจิต
- **BMI < 21 kg/m2 พยากรณ์โรคแย่** (ตายมากขึ้น) · อ้วน > 30 เสี่ยง OSA และโรคหัวใจ · เสริมอาหารในคนผอม/ขาดสารอาหาร เพิ่มน้ำหนักและกำลังกล้ามเนื้อหายใจ
- คัดกรองซึมเศร้า/วิตกกังวล (PHQ-2, GAD-2) — พบราว 1 ใน 3 · rehab และ CBT ช่วย · **benzodiazepine ไม่ช่วยเหนื่อย** และกดการหายใจ

### 6. โรคร่วมและภาวะแทรกซ้อนที่ต้องหา
| ภาวะ | สิ่งที่ต้องรู้ (GOLD 2026) |
|---|---|
| **โรคหัวใจ** (HT ~50%, HF 20–30%, CAD, AF) | เสี่ยง MI/stroke สูงสุดช่วง 30 วันหลัง exacerbation · **β1-selective blocker (bisoprolol, metoprolol) ใช้ได้และควรใช้เมื่อมีข้อบ่งชี้ทางหัวใจ** · ระวัง SABA และ theophylline กระตุ้น AF |
| **Cor pulmonale / PH** | echo · LTOT ถ้า hypoxemic |
| **Secondary polycythemia** (6–10%) | หา hypoxemia ที่ยังไม่แก้ · CO จากบุหรี่ |
| **มะเร็งปอด** | LDCT ปีละครั้งในคนอายุ 50–80 ปี สูบ ≥ 20 pack-year (ยังสูบ/เลิก < 15 ปี) |
| **Pneumothorax** | bulla แตก → เหนื่อยเฉียบพลัน เจ็บอก — secondary spontaneous PTX ใน COPD มักต้องใส่สายระบาย |
| **กระดูกพรุน กล้ามเนื้อลีบ ซีด เบาหวาน GERD OSA** | รักษาตามแนวทางของแต่ละโรค ไม่เปลี่ยนการรักษา COPD |

### 7. เมื่อไรส่งต่อแพทย์เฉพาะทาง
วินิจฉัยไม่ชัด (สงสัย asthma, ILD, HF) · **อายุ < 40–45 ปีหรือไม่มีปัจจัยเสี่ยง** (หา AATD) · exacerbation ซ้ำแม้รักษาเต็มที่ · อาการไม่สมกับ FEV1 · ต้องประเมิน LTOT/home NIV · cor pulmonale · ไอเป็นเลือด น้ำหนักลด ก้อนในปอด · พิจารณาผ่าตัด/ส่องกล้องลดปริมาตรปอด หรือปลูกถ่ายปอด (หัวข้อ 14)""",
    ["เลิกบุหรี่ = counseling + ยา (NRT, varenicline, bupropion) · ใช้ 5A/5R · e-cigarette ไม่แนะนำ",
     "วัคซีน: influenza ทุกปี · pneumococcal (PCV20/PCV21) · RSV (≥ 75 ปี หรือ 50–74 ปีที่มีโรคปอด) · Tdap · zoster",
     "Pulmonary rehab 6–8 สัปดาห์ สำหรับกลุ่ม B/E · เริ่มภายใน 4 สัปดาห์หลัง admit ลดการตาย",
     "LTOT > 15 ชม./วัน เมื่อ PaO2 ≤ 55 (หรือ 55–60 + PH/ขาบวม/Hct > 55%) ตอน stable — ยืดชีวิต",
     "β1-selective blocker ใช้ได้ใน COPD เมื่อมีข้อบ่งชี้ทางหัวใจ"],
    [mcq(N(20), "A 59-year-old man with COPD smokes 25 cigarettes a day, lights his first cigarette within 10 minutes of waking, and says he wants to stop within the next month. Which approach is most likely to achieve long-term abstinence?",
         ["Advise him to switch to electronic cigarettes", "Advise gradual reduction by 1 cigarette per week without other support",
          "Behavioural counselling combined with pharmacotherapy such as varenicline or nicotine replacement", "Prescribe a benzodiazepine to control withdrawal anxiety",
          "Defer cessation until his COPD is stable on triple therapy"], 2,
         "ผู้ป่วยพร้อมเลิก (ขั้น **Assist** ของ 5A) และติดนิโคตินสูง (สูบภายใน 30 นาทีหลังตื่น, ≥ 20 มวน/วัน) · GOLD 2026: **counseling ร่วมกับยา** ได้ผลดีที่สุดใน COPD · varenicline (partial agonist α4β2) และ NRT ช่วยลดอาการขาดนิโคติน · ตั้งวันเลิก นัดติดตามในสัปดาห์แรก\n\n"
         "- *e-cigarette* — GOLD 2026: ไม่มีหลักฐานเรื่องประสิทธิภาพและความปลอดภัย\n- *ลดทีละมวนโดยไม่มีตัวช่วย* — อัตราเลิกต่ำ\n"
         "- *benzodiazepine* — ไม่ใช่ยาเลิกบุหรี่ และกดการหายใจ\n- *รอให้โรคคงที่ก่อน* — ทุกการพบแพทย์คือโอกาส ยิ่งเลิกเร็วยิ่งดี",
         "Counseling + ยา = วิธีเลิกบุหรี่ที่ดีที่สุด", "Smoking cessation", R("Chapter 3 Risk reduction — smoking cessation"), [TOB, COPD]),
     mcq(N(21), "A 72-year-old woman with COPD has been stable for 3 months. On two occasions 3 weeks apart, arterial blood gas on room air at rest shows PaO2 58 mmHg. She has bilateral pitting ankle edema, a loud P2, and haematocrit 57%. What is the most appropriate management of her hypoxaemia?",
         ["No oxygen, because PaO2 is above 55 mmHg", "Oxygen only during exertion", "Long-term oxygen therapy for more than 15 hours per day",
          "Venesection alone to reduce haematocrit", "Oxygen only at night"], 2,
         "PaO2 **55–60 mmHg ร่วมกับหลักฐานว่า hypoxemia ทำร้ายอวัยวะแล้ว** (ขาบวมจาก cor pulmonale, P2 ดัง = pulmonary hypertension, **Hct > 55%** = polycythemia) เข้าเกณฑ์ **LTOT > 15 ชั่วโมง/วัน** ซึ่งยืดชีวิตได้ เพราะแก้ hypoxic vasoconstriction และลดการกระตุ้น EPO\n\n"
         "- *ไม่ให้เพราะ > 55* — ลืมเกณฑ์ข้อที่สอง\n- *ให้เฉพาะออกแรง/กลางคืน* — ไม่มีหลักฐานยืดชีวิต (NOTT: ใช้ต่อเนื่องดีกว่ากลางคืน)\n- *เจาะเลือดออกอย่างเดียว* — ไม่แก้สาเหตุ (hypoxemia)",
         "PaO2 55–60 + cor pulmonale/PH/Hct > 55% = ให้ LTOT", "LTOT", R("Chapter 3 Oxygen therapy"), [COPD, O2T, ABG]),
     mcq(N(22), "A 68-year-old man with COPD asks which vaccines he should receive. He has had no vaccinations since childhood. According to GOLD 2026, which recommendation is most appropriate?",
         ["Influenza vaccine only during an exacerbation", "BCG revaccination and annual influenza vaccine",
          "Annual inactivated influenza vaccine, a pneumococcal conjugate vaccine (e.g., PCV20 or PCV21) and RSV vaccine, plus Tdap and zoster vaccines",
          "Pneumococcal vaccine only if FEV1 is below 40% predicted", "Avoid all vaccines because they can trigger exacerbations"], 2,
         "GOLD 2026: ผู้ป่วย COPD ควรได้วัคซีนตามคำแนะนำ — **influenza ทุกปี** · **pneumococcal** (GOLD แนะนำ PCV20 หรือ PCV21 ในอายุ ≥ 50) · **RSV** (อายุ 50–74 ปีที่มีโรคปอดเรื้อรัง และทุกคน ≥ 75) · **Tdap** ถ้าไม่เคยได้ตอนวัยรุ่น · **zoster** · COVID-19 ตามคำแนะนำประเทศ — ลด LRTI, admit และ exacerbation\n\n"
         "- *ให้ตอน exacerbation* — วัคซีนเป็นการป้องกัน ให้ตามฤดูกาล/ตอน stable\n- *BCG ซ้ำ* — ไม่มีข้อบ่งชี้ในผู้ใหญ่\n"
         "- *pneumococcal เฉพาะ FEV1 < 40%* — เป็นข้อมูลเก่าเรื่อง PPSV23 ปัจจุบันให้ทุกคนตามอายุ/โรค\n- *เลี่ยงวัคซีน* — ผิด ผลข้างเคียงส่วนใหญ่เล็กน้อยชั่วคราว",
         "COPD: influenza ทุกปี + pneumococcal + RSV + Tdap + zoster", "Vaccination", R("Chapter 3 Vaccinations"), [COPD, IMM, FLU])],
    [COPD, TOB, IMM, FLU, O2T, ABG, PTX],
    {"ltot": F.ltot()})

# ───────────────────────────── 10
sec("chest-copd-10", "Acute exacerbation (1) — วินิจฉัย ความรุนแรง และยา 3 กลุ่ม",
    "นิยาม ≤ 14 วัน · ไวรัสพบบ่อยสุด · แยก pneumonia/PE/HF/PTX · Rome mild/moderate/severe · SABA ± SAMA · prednisolone 40 mg × 5 วัน · antibiotic เมื่อเสมหะเป็นหนอง", 12,
"""### นิยาม (GOLD 2026)
**Exacerbation** = เหตุการณ์เฉียบพลันที่อาการแย่ลงภายใน **≤ 14 วัน** มี **เหนื่อยมากขึ้น และ/หรือ ไอและเสมหะเพิ่ม** อาจมีหายใจเร็ว ชีพจรเร็ว ร่วมกับการอักเสบที่หลอดลมและทั่วร่างกายเพิ่มขึ้น

#### ทำไมถึงเหนื่อยมากขึ้น
สิ่งกระตุ้น → หลอดลมอักเสบบวม เสมหะมาก → แรงต้านเพิ่ม ลมค้างมากขึ้น (**hyperinflation แย่ลงอย่างเฉียบพลัน**) → กล้ามเนื้อหายใจทำงานหนักในท่าที่เสียเปรียบ + V/Q mismatch แย่ลง → hypoxemia ± hypercapnia

### สาเหตุกระตุ้น
- **ติดเชื้อทางเดินหายใจ — ไวรัสพบบ่อยที่สุด** (rhinovirus, influenza, parainfluenza, metapneumovirus, RSV) และแบคทีเรีย (*H. influenzae, S. pneumoniae, M. catarrhalis* · *Pseudomonas* ในรายรุนแรง/ได้ยาบ่อย)
- มลพิษ PM2.5/NO2 · อากาศร้อนจัด/หนาวจัด · หมอกควันไฟป่า · ราวหนึ่งในสามหาสาเหตุไม่พบ
- **ภาวะที่เลียนแบบหรือทำให้แย่ลง ต้องแยกทุกราย**: **pneumonia** (CXR) · **pulmonary embolism** (เจ็บอกแบบ pleuritic, ชีพจรเร็ว, ขาบวมข้างเดียว — admit ด้วย exacerbation พบ PE ถึง 5.9%) · **หัวใจล้ม/MI/arrhythmia** (ECG, troponin, NT-proBNP) · **pneumothorax** · pleural effusion

### ความรุนแรง — Rome classification (ใหม่ใน GOLD 2026)
| | Mild | Moderate (≥ 3 ใน 5 ข้อ) | Severe |
|---|---|---|---|
| ความเหนื่อย (VAS 0–10) | < 5 | ≥ 5 | เหมือน moderate |
| อัตราการหายใจ | < 24 | ≥ 24 | " |
| ชีพจร | < 95 | ≥ 95 | " |
| SaO2 ขณะพัก | ≥ 92% (ลด ≤ 3%) | < 92% และ/หรือลด > 3% | " |
| CRP | < 10 mg/L | ≥ 10 mg/L | " |
| ABG | — | อาจมี hypoxemia | **PaO2 ≤ 60 และ/หรือ PaCO2 > 45 + pH < 7.35** |

- ระบบเดิม (mild = SABA อย่างเดียว · moderate = steroid/antibiotic · severe = admit) ยังใช้ในการนับประวัติเพื่อจัดกลุ่ม ABE
- **ข้อบ่งชี้ admit** (รูปในรายงานอ่านไม่ได้ — ตาม GOLD 2025): อาการรุนแรง (เหนื่อยขณะพักแย่ลงเฉียบพลัน หายใจเร็ว SpO2 ลด **สับสน ง่วงซึม**) · acute respiratory failure · อาการแสดงใหม่ (**เขียว ขาบวม**) · ไม่ตอบสนองการรักษาเบื้องต้น · โรคร่วมรุนแรง (HF, arrhythmia ใหม่) · ดูแลที่บ้านไม่ได้ · **มากกว่า 80% ของ exacerbation รักษาแบบผู้ป่วยนอกได้**

[[fig:ae_flow]]

### ยา 3 กลุ่ม
| ยา | ขนาด/วิธีให้ | กลไกที่ช่วย | ข้อควรระวัง |
|---|---|---|---|
| **SABA ± SAMA** (salbutamol ± ipratropium) | MDI 1–2 puff หรือ nebulize ทุก 1 ชม. 2–3 ครั้ง แล้วทุก 2–4 ชม. ตามอาการ · MDI+spacer ได้ผลเท่า nebulizer | คลายกล้ามเนื้อเรียบ ลด hyperinflation | **nebulizer ให้ขับด้วยลมอัด (air-driven) ไม่ใช่ออกซิเจน** ในผู้ที่เสี่ยง CO2 คั่ง (ถ้าจำเป็นใช้ O2 ทาง nasal cannula ร่วม) · ไม่ใช้ขนาดสูงเกิน (K ต่ำ, arrhythmia) |
| **Systemic corticosteroid** | **prednisolone 40 mg/วัน 5 วัน** · กินได้ผลเท่าฉีด | ลดบวมอักเสบในหลอดลม → ฟื้นเร็ว FEV1 ดีขึ้น ออกซิเจนดีขึ้น ลด treatment failure ลดวันนอน | course ยาวเพิ่ม pneumonia และการตาย · น้ำตาลขึ้น (เบาหวาน) · eos สูงได้ผลมากกว่า |
| **Antibiotic** | ให้เมื่อ: **(1) มี ≥ 2 ใน 4 อาการ — เหนื่อยเพิ่ม ไข้ เสมหะเพิ่ม เสมหะเป็นหนอง — โดยต้องมี "เสมหะเป็นหนอง"** · (2) เคยเพาะเชื้อขึ้นใน exacerbation ก่อน · (3) **ต้องใช้ NIV หรือเครื่องช่วยหายใจ** · empirical: **amoxicillin-clavulanate, macrolide, doxycycline** (quinolone ในบางราย) **5 วัน** (≤ 5 วันในผู้ป่วยนอก, 5–7 วันโดยรวม) | เสมหะเหลือง/เขียว = myeloperoxidase จาก neutrophil · ไว 94% ต่อการมีแบคทีเรียมาก | exacerbation บ่อย FEV1 ต่ำมาก หรือใช้เครื่องช่วยหายใจ → **เพาะเชื้อเสมหะ** (Pseudomonas, เชื้อดื้อยา) · CRP ช่วยลดการใช้ยา · **ไม่แนะนำใช้ procalcitonin ตัดสิน** |

- **ไม่ใช้ IV aminophylline/theophylline** (ผลข้างเคียงมาก) · **respiratory stimulant (doxapram) ไม่แนะนำ**
- เสริม: **ป้องกัน DVT** · สารน้ำ/ยาขับปัสสาวะตามภาวะ · N-acetylcysteine ช่วยขับเสมหะได้ · **ให้ยาพ่น long-acting ต่อหรือเริ่มก่อนกลับบ้าน** · เน้นเลิกบุหรี่""",
    ["Exacerbation = อาการแย่ลงภายใน ≤ 14 วัน · ไวรัสเป็นสาเหตุที่พบบ่อยที่สุด",
     "แยก pneumonia · PE · หัวใจล้ม/MI · pneumothorax ทุกราย",
     "ยาขยายหลอดลมตัวแรก = SABA ± SAMA · nebulizer ใช้ลมอัด ไม่ใช่ O2",
     "Prednisolone 40 mg/วัน × 5 วัน",
     "Antibiotic เมื่อเสมหะเป็นหนอง + อีก ≥ 1 อาการ หรือใช้ NIV/ventilator · 5 วัน"],
    [mcq(N(23), "A 66-year-old man is admitted with an exacerbation of COPD. He is not acidotic and has no pneumonia on chest radiograph. Which systemic corticosteroid regimen is recommended?",
         ["Hydrocortisone 100 mg IV every 6 hours for 14 days", "Prednisolone 40 mg orally once daily for 5 days",
          "Prednisolone 60 mg daily tapered over 6 weeks", "Dexamethasone 6 mg daily for 10 days", "No systemic corticosteroid; inhaled budesonide is mandatory instead"], 1,
         "GOLD 2026: **prednisone/prednisolone 40 mg/วัน 5 วัน** (ให้ทางปากได้ผลเท่าทางหลอดเลือด) ลดเวลาฟื้นตัว เพิ่ม FEV1 และออกซิเจน ลด relapse/treatment failure และวันนอน · course ยาวกว่านี้เพิ่ม pneumonia และการตาย\n\n"
         "- *hydrocortisone 14 วัน* — ขนาด/ระยะเวลาเกินจำเป็น\n- *taper 6 สัปดาห์* — ไม่มีประโยชน์เพิ่ม ผลเสียมาก\n- *dexamethasone 10 วัน* — สูตรสำหรับ COVID-19\n- *budesonide พ่นแทนบังคับ* — nebulized budesonide เป็นทางเลือกในบางราย ไม่ใช่ข้อบังคับ",
         "AECOPD: prednisolone 40 mg × 5 วัน", "Exacerbation — corticosteroids", R("Chapter 4 Glucocorticoids"), [AE, CORT]),
     mcq(N(24), "A 71-year-old woman with COPD presents with 1 day of sudden breathlessness and right-sided pleuritic chest pain. She has no change in sputum and no fever. Pulse 118/min, RR 28/min, SpO2 86% on room air. Her right calf has been swollen since a hip operation 2 weeks ago. Chest radiograph shows hyperinflation only. Which investigation is most important next?",
         ["Sputum culture", "CT pulmonary angiography", "Repeat spirometry", "Serum procalcitonin", "High-resolution CT for bronchiectasis"], 1,
         "อาการแย่ลงเฉียบพลันที่ **ไม่มีเสมหะเปลี่ยน ไม่มีไข้** แต่ **เจ็บอกแบบ pleuritic ชีพจรเร็ว ขาบวมข้างเดียวหลังผ่าตัด** = นึกถึง **pulmonary embolism** ซึ่ง GOLD 2026 ระบุเป็นภาวะเลียนแบบ exacerbation ที่ต้องแยก (พบได้ถึง 5.9% ของผู้ป่วยที่ admit) → **CTPA**\n\n"
         "- *เพาะเชื้อเสมหะ* — ไม่มีอาการติดเชื้อ\n- *spirometry ซ้ำ* — ไม่ทำช่วงเฉียบพลัน\n- *procalcitonin* — GOLD ไม่แนะนำใช้ตัดสิน antibiotic และไม่ช่วยหา PE\n- *HRCT* — ไม่ใช่ปัญหาเฉียบพลัน",
         "Exacerbation ที่ไม่มีเสมหะเปลี่ยน + pleuritic pain + DVT → หา PE", "Exacerbation — differential diagnosis", R("Chapter 4 Conditions to be considered"), [AE, COPD])],
    [AE, COPD, BD, CORT, LRTI],
    {"ae_flow": F.ae_flow()})

# ───────────────────────────── 11
sec("chest-copd-11", "Acute exacerbation (2) — ออกซิเจนแบบควบคุม, CO2 คั่ง, NIV, ใส่ท่อช่วยหายใจ และก่อนกลับบ้าน",
    "เป้า SpO2 88–92% · Venturi · ทำไม O2 มากทำให้ CO2 คั่ง · ABG ซ้ำ · NIV เมื่อ pH ≤ 7.35 + PaCO2 ≥ 45 · ข้อบ่งชี้ใส่ท่อ · discharge bundle · ติดตาม 1 เดือน/3 เดือน", 12,
"""### ออกซิเจนแบบควบคุม
- ผู้ป่วยที่ hypoxemic ให้ O2 **ไตเตรตให้ SpO2 88–92%** (ค่าเป้าอยู่ในรูปของ GOLD ที่อ่านจากไฟล์ 2026 ไม่ได้ — ตาม GOLD 2023–2025 และ BTS oxygen guideline) · **Venturi mask 24–28%** ให้ FiO2 แน่นอนกว่า nasal cannula
- **เจาะ ABG ก่อนหรือหลังเริ่ม O2 และซ้ำใน 30–60 นาที** ดู PaCO2/pH (SpO2 ไม่บอก CO2) · VBG ใช้ได้ในรายไม่รุนแรง · SpO2 อ่านค่าสูงเกินจริงในผิวสีเข้ม
- ถ้า CO2 ขึ้นหลังให้ O2 **อย่าหยุด O2 ทันที** (PaO2 จะดิ่งต่ำกว่าเดิม) ให้ลด FiO2 กลับสู่เป้าและพิจารณา NIV

[[fig:o2_co2]]

#### ทำไม O2 มากเกินทำให้ CO2 คั่ง (ลำดับความสำคัญ)
1. **V/Q mismatch แย่ลง** — O2 ปลด hypoxic vasoconstriction ในถุงลมที่ระบายไม่ดี เลือดไหลกลับไปที่ที่ขับ CO2 ไม่ได้ (dead space ของถุงลมดีเพิ่มขึ้น)
2. **Haldane effect** — Hb ที่จับ O2 มากขึ้นปล่อย CO2 ที่จับไว้ออกสู่พลาสมา
3. **hypoxic drive ลดลง** — มีส่วนน้อยกว่าที่เคยเชื่อ (minute ventilation ลดเล็กน้อย)
- ผล: CO2 คั่ง → **respiratory acidosis** → ซึม สับสน (CO2 narcosis) → หยุดหายใจ · ข้อมูลจริง: ผู้ป่วย AECOPD ที่ได้ O2 แบบไตเตรตตายน้อยกว่าที่ได้ O2 ความเข้มข้นสูง

### Ventilatory support
[[fig:niv]]

| วิธี | ข้อบ่งชี้/ข้อเท็จจริง (GOLD 2026) |
|---|---|
| **NIV (BiPAP)** — วิธีแรก | ≥ 1 ข้อ: **respiratory acidosis: PaCO2 ≥ 45 mmHg และ pH ≤ 7.35** · เหนื่อยรุนแรงมีอาการแสดงกล้ามเนื้อหายใจล้า/ใช้แรงมาก (accessory muscle, ท้องบุ๋มสวนทางทรวงอก, intercostal retraction) · hypoxemia ไม่ดีขึ้นแม้ให้ O2 (รายการตาม GOLD 2025 Fig 4.8) · **สำเร็จ 80–85% เพิ่ม pH ลด PaCO2 ลดงานหายใจ ลด VAP ลดวันนอน ลดการใส่ท่อและลดการตาย** · หายใจเองได้ ≥ 4 ชม. หยุดได้เลยไม่ต้อง wean |
| **High-flow nasal oxygen (HFNT)** | ใช้เมื่อทน NIV ไม่ได้ · บางการศึกษาไม่ด้อยกว่า NIV แต่ราว 30% ต้องเปลี่ยนเป็น NIV · **ERS แนะนำ NIV ก่อน HFNT ใน hypercapnic respiratory failure** |
| **Invasive ventilation** | NIV ล้มเหลวหรือทนไม่ได้ · หยุดหายใจ/หัวใจหยุดเต้น · ซึมลง/กระสับกระส่ายคุมไม่ได้ · สำลักมาก อาเจียนต่อเนื่อง · ขับเสมหะไม่ได้ · ความดันต่ำรุนแรงไม่ตอบสนอง · arrhythmia รุนแรง · hypoxemia คุกคามชีวิตในคนที่ทน NIV ไม่ได้ (ตาม GOLD 2025 Fig 4.9) · ตายในโรงพยาบาล 17–49% แต่ **อย่าปฏิเสธ ICU เพราะมองพยากรณ์แง่ร้ายเกินจริง** — คุยความประสงค์ของผู้ป่วย (advance directive) ล่วงหน้า |

#### ทำไม NIV ได้ผลใน COPD
- **IPAP** (แรงดันช่วยหายใจเข้า) ช่วยกล้ามเนื้อที่ล้า ให้ tidal volume ใหญ่ขึ้น alveolar ventilation เพิ่ม **ขับ CO2 ได้ pH ขึ้น**
- **EPAP** ต้าน **intrinsic PEEP (auto-PEEP)** จากลมค้าง — ผู้ป่วยไม่ต้องออกแรงลบล้างแรงดันค้างในถุงลมก่อนลมจะเริ่มไหลเข้า งานหายใจจึงลดลง

### การจำแนกผู้ป่วยในตามสภาพ (GOLD 2026)
- **ไม่มี respiratory failure**: RR ≤ 24, HR ≤ 95, ไม่ใช้ accessory muscle, สติปกติ, O2 Venturi 24–35% แก้ได้, PaCO2 ไม่เพิ่ม
- **Respiratory failure (ไม่คุกคามชีวิต)**: RR > 24, HR > 95, ใช้ accessory muscle, สติปกติ, ต้อง Venturi > 35%, PaCO2 เพิ่มจากเดิมหรือ 50–60
- **Ventilatory failure (คุกคามชีวิต)**: สติเปลี่ยนเฉียบพลัน, ต้อง FiO2 > 40% หรือแก้ไม่ได้, **PaCO2 > 60 + pH ≤ 7.25**

### ก่อนกลับบ้านและการติดตาม (GOLD 2026)
- **admit ซ้ำใน 30 วันถึง 30–50%** · ตาย 5 ปีหลัง admit ราว 50% · ฟื้นตัว 4–6 สัปดาห์ บางคนไม่กลับเท่าเดิม
- **discharge bundle**: ทบทวนและ **เริ่ม/ปรับยา long-acting** (เริ่ม triple เร็วภายใน 30 วันหลัง exacerbation ลด exacerbation ครั้งต่อไป 20–30% — มีเพียง 17.5% ที่ได้ triple ตอนกลับบ้าน) · **ตรวจท่าพ่นยา** · เลิกบุหรี่ · วัคซีน · **pulmonary rehab ภายใน 4 สัปดาห์** · action plan เขียนเป็นลายลักษณ์อักษร · จัดการโรคร่วม
- **นัดติดตามภายใน 1 เดือน** (ลดการ admit ซ้ำ) และที่ **3 เดือน**: spirometry, ประเมินความต้องการ LTOT ตอน stable (ประเมินวันกลับบ้านไม่แม่น)
- exacerbation ซ้ำ → CT หา bronchiectasis/emphysema · ตรวจ vitamin D ใน admit (ขาดรุนแรง < 10 ng/mL → เสริม)""",
    ["AECOPD: O2 เป้า SpO2 88–92% (Venturi) · ABG ซ้ำใน 30–60 นาที",
     "O2 มากเกิน → CO2 คั่ง จาก V/Q แย่ลง (ปลด HPV) + Haldane + drive ลดเล็กน้อย — แก้โดยไตเตรต ไม่ใช่หยุด O2",
     "NIV เมื่อ pH ≤ 7.35 + PaCO2 ≥ 45 หรือกล้ามเนื้อหายใจล้า — ลดการใส่ท่อและลดตาย",
     "ใส่ท่อเมื่อ NIV ล้มเหลว ซึม/กระสับกระส่าย สำลัก ขับเสมหะไม่ได้ shock arrest",
     "ก่อนกลับบ้าน: ยา long-acting + ท่าพ่นยา + rehab ใน 4 สัปดาห์ + นัด 1 เดือน · ประเมิน LTOT ที่ 3 เดือน"],
    [mcq(N(25), "A 70-year-old man with severe COPD is brought to the emergency department with an exacerbation. Paramedics gave 15 L/min oxygen via a non-rebreather mask. He is now drowsy. ABG: pH 7.21, PaCO2 88 mmHg, PaO2 210 mmHg, HCO3 34 mmol/L. Which mechanism contributes most to the rise in PaCO2?",
         ["Increased CO2 production from fever", "Release of hypoxic pulmonary vasoconstriction, worsening ventilation–perfusion mismatch",
          "Metabolic alkalosis suppressing ventilation", "Absorption atelectasis causing a pure shunt", "Oxygen toxicity damaging the alveolar membrane within minutes"], 1,
         "ให้ O2 ความเข้มข้นสูง → PAO2 ในถุงลมที่ระบายไม่ดีสูงขึ้น **hypoxic vasoconstriction ถูกปลด** เลือดไหลกลับไปถุงลมที่ระบายอากาศไม่ได้ จึงขับ CO2 ไม่ได้ (**V/Q mismatch แย่ลง**) — เป็นกลไกหลัก ร่วมกับ **Haldane effect** และ hypoxic drive ที่ลดลงเล็กน้อย · PaO2 210 = ได้ O2 เกินเป้า (88–92%) มาก · แก้: ลด FiO2 ด้วย Venturi ให้ SpO2 88–92% และเริ่ม **NIV** (pH < 7.35, PaCO2 ≥ 45)\n\n"
         "- *ไข้เพิ่ม CO2* — มีส่วนน้อย และไม่มีไข้ในโจทย์\n- *metabolic alkalosis* — HCO3 34 คือการชดเชย chronic respiratory acidosis ไม่ใช่ต้นเหตุ\n"
         "- *absorption atelectasis* — ทำให้ PaO2 ต่ำ ไม่ใช่ PaCO2 สูง และ PaO2 ที่นี่สูงมาก\n- *O2 toxicity* — ใช้เวลาหลายวัน",
         "CO2 คั่งจาก O2 = V/Q แย่ลง + Haldane → ไตเตรต SpO2 88–92%", "Oxygen-induced hypercapnia", R("Chapter 4 Management of respiratory failure — oxygen therapy"), [AE, RF, ABG, O2T]),
     mcq(N(26), "A 64-year-old woman with COPD is admitted with an exacerbation. After 1 hour of nebulised bronchodilators, prednisolone and oxygen titrated to SpO2 90%, she is alert but using accessory muscles. RR 30/min. ABG: pH 7.29, PaCO2 64 mmHg, PaO2 62 mmHg. What is the most appropriate next step?",
         ["Immediate endotracheal intubation", "Start non-invasive ventilation (BiPAP)", "Increase oxygen to achieve SpO2 above 96%",
          "Give intravenous aminophylline", "Give intravenous doxapram"], 1,
         "**pH 7.29 (≤ 7.35) + PaCO2 64 (≥ 45)** = acute-on-chronic hypercapnic respiratory failure ที่ยังรู้สึกตัวดีและไม่มีข้อห้าม → **NIV เป็นวิธีแรก** (GOLD 2026: สำเร็จ 80–85% ลดการใส่ท่อและลดตาย) · ติดตาม ABG ซ้ำใน 1–2 ชม.\n\n"
         "- *ใส่ท่อทันที* — สงวนไว้เมื่อ NIV ล้มเหลว/มีข้อห้าม (ซึม สำลัก หยุดหายใจ shock)\n- *เพิ่ม SpO2 > 96%* — ทำให้ CO2 คั่งมากขึ้น\n"
         "- *IV aminophylline* — GOLD ไม่แนะนำ ผลข้างเคียงมาก\n- *doxapram* — respiratory stimulant ไม่แนะนำ",
         "pH ≤ 7.35 + PaCO2 ≥ 45 ที่ยังตื่นดี = NIV", "NIV indications", R("Chapter 4 Noninvasive mechanical ventilation"), [AE, ARF, RF, ABG, ABGB]),
     mcq(N(27), "A 67-year-old man is ready for discharge after 5 days in hospital for an exacerbation of COPD. Before admission he used only as-needed salbutamol. Which discharge plan best follows GOLD 2026?",
         ["Continue prednisolone 20 mg daily for 1 month and review in 6 months",
          "Start maintenance long-acting bronchodilator therapy, check inhaler technique, refer for pulmonary rehabilitation within 4 weeks and arrange follow-up within 1 month",
          "Prescribe home nebulised salbutamol only, because inhalers failed",
          "Prescribe long-term oxygen based on the ABG taken on the day of discharge",
          "Stop all inhalers once FEV1 returns to baseline"], 1,
         "admit 1 ครั้ง = กลุ่ม E → ต้องเริ่ม **ยา long-acting** (LABA+LAMA หรือ triple ตาม eos) **ก่อนกลับบ้าน** · ตรวจท่าพ่นยา · **pulmonary rehab ภายใน 4 สัปดาห์** (ลด admit ซ้ำและลดตาย) · **นัดภายใน 1 เดือน** และ 3 เดือน · เลิกบุหรี่ วัคซีน action plan\n\n"
         "- *prednisolone 1 เดือน* — ไม่มีประโยชน์ เพิ่ม pneumonia กระดูกพรุน\n- *nebulizer อย่างเดียว* — ไม่ใช่ maintenance ไม่ลด exacerbation\n"
         "- *LTOT จาก ABG วันกลับบ้าน* — ต้องประเมินตอน stable (ราว 3 เดือน) เพราะ hypoxemia หลัง exacerbation มักดีขึ้น\n- *หยุดยาเมื่อดีขึ้น* — COPD ต้องใช้ยาต่อเนื่อง",
         "ก่อนกลับบ้าน: long-acting + ท่าพ่นยา + rehab ≤ 4 สัปดาห์ + นัด ≤ 1 เดือน", "Discharge and follow-up", R("Chapter 4 Hospital discharge and follow-up"), [AE, COPD])],
    [AE, ARF, RF, ABG, ABGB, O2T, CTRL],
    {"o2_co2": F.o2_co2(), "niv": F.niv()})

INTRO = 'สองคาบแรกของ อ.ศิวพร — วัณโรคปอด และการแปลผลก๊าซในเลือดแดง — ต่อด้วยคาบ **Extrapulmonary TB ของ อ.ภาณุวัฒน์ (23 ก.ย.)** ที่ไล่วัณโรคนอกปอดทีละอวัยวะ ตั้งแต่เยื่อหุ้มปอด ต่อมน้ำเหลือง กระดูกสันหลัง สมอง เยื่อหุ้มหัวใจ ไปจนถึงช่องท้องและทางเดินปัสสาวะ และคาบ 17 **Respiratory failure and Pleural disease ของ อ.สกล (28 ก.ย.)** ที่เริ่มจากการส่งออกซิเจนและ A-a gradient ไปจนถึง pneumothorax และการอ่านน้ำในช่องเยื่อหุ้มปอดตาม BTS 2023 ต่อด้วยคาบ **Thoracentesis (Active learning กลุ่ม 5)** ที่สอนหัตถการเจาะน้ำทีละขั้น ตั้งแต่ข้อบ่งชี้ consent อัลตราซาวด์ การแทงเหนือขอบบนซี่โครง ขีดระบายและ re-expansion edema การส่ง pH ไปจนถึงการอ่านผลน้ำห้าขั้น และคาบ 37 **COPD (20 ต.ค.)** ที่เรียบเรียงจาก **GOLD 2026** — หัวข้อ 1–11 เป็นความรู้ระดับ NL ส่วนหัวข้อ 12–14 เป็น "อ่านเพิ่มเติม" เนื้อหาเรียบเรียงจากสไลด์บรรยายจริง ร่วมกับคลังข้อสอบ MED28–MED35 และข้อใหม่ของชุด Chest จบแต่ละหัวข้อมีข้อสอบเช็คความเข้าใจทันที'
HOWTO = '**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายกลไกทันทีที่ตอบ · ตอบครบทุกข้อแล้วหัวข้อจะถูกทำเครื่องหมายว่าเรียนจบ · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบวัณโรคแล้วไปฝึก **MEQ** และ **OSCE/SAQ** ต่อได้เลย\n\n**ลำดับที่แนะนำ** — เรียนคาบ 03 วัณโรคปอดก่อนคาบ Extrapulmonary TB เพราะสูตรยา พิษยา และการป้องกันการแพร่เชื้อปูพื้นไว้ในคาบ 03 แล้ว · ในคาบ EPTB ตาราง **body fluid** และ **ADA** (หัวข้อ 4) คือส่วนที่อาจารย์เน้นมากที่สุด · คาบ 17 เรียนต่อจากคาบ 26 (ABG) ได้เลย เพราะ A-a gradient และ hypoxemia ต่อยอดกันตรง ๆ — ข้อที่ออกทุกรุ่นคือ **คำนวณ Light\'s criteria ให้เห็นตัวเลข** และ **tension pneumothorax วินิจฉัยทางคลินิก ห้ามรอฟิล์ม** · คาบ **Thoracentesis** เรียนต่อจากคาบ 17 ได้ทันที (คาบ 17 สอนกลไกและสาเหตุของน้ำ คาบนี้สอนหัตถการ การส่งตรวจ และการอ่านผลเป็นขั้น) — จุดที่ออก OSCE คือ **consent + แทงเหนือขอบบนซี่โครง + ปิด 3-way + เก็บ pH ใน syringe blood gas** · คาบ 37 COPD เรียนต่อจากคาบ 26 และ 17 ได้เลย (ใช้ ABG และ hypercapnic respiratory failure ต่อ) — เน้น **กลุ่ม ABE แบบ GOLD 2026 (exacerbation 1 ครั้งก็เป็น E)**, **เกณฑ์ LTOT** และ **O2 เป้า 88–92% กับข้อบ่งชี้ NIV** · หัวข้อ "อ่านเพิ่มเติม" ข้ามได้ถ้าเตรียมสอบ NL\n\nคาบที่เหลือของชุด Chest (CXR และโรคจากการทำงาน · ส่วน pneumonia/asthma ของคาบ 37) ยังไม่ได้ทำบทเรียน แต่ข้อสอบมีอยู่ครบใน drill.html แล้ว'

# ───────────────────────────── 12 (อ่านเพิ่มเติม)
sec("chest-copd-12", "อ่านเพิ่มเติม (เกินระดับ NL) — ปรับยาขั้นสูง: azithromycin, roflumilast, biologics, ensifentrine และยาที่ลดการตาย",
    "Figure 3.9 ฉบับเต็ม · LABA+ICS เดิม · ถอน ICS · dupilumab/mepolizumab · disease activity · IMPACT/ETHOS", 8,
RM + """

[[fig:followup_rx]]

### Follow-up algorithm ฉบับเต็ม (GOLD 2026 Figure 3.9)
- ใช้กับทุกคนที่ได้ยา maintenance แล้ว **ไม่ว่าตอนเริ่มอยู่กลุ่มไหน** · เลือก "treatable trait" หลัก: **dyspnea** หรือ **exacerbation** (มีทั้งสองใช้เส้นทาง exacerbation)
- **เส้นทาง dyspnea**: ยาเดี่ยว → LABA+LAMA → ยังเหนื่อย: เปลี่ยน device/ตัวยา · pulmonary rehab · **ensifentrine** (ยับยั้ง PDE3 และ PDE4 ในรูปพ่นละออง — ขยายหลอดลมและต้านอักเสบ) ถ้ามี · หาสาเหตุอื่น
- **เส้นทาง exacerbation**:
  - LABA+LAMA ยัง exacerbate → **eos ≥ 100: เพิ่ม ICS** · **eos < 100**: **azithromycin** (ผู้ที่ไม่สูบบุหรี่ — ระวังเชื้อดื้อยา QT ยาว สูญเสียการได้ยิน) หรือ **roflumilast** (FEV1 < 50% + chronic bronchitis + เคย admit)
  - Triple ยัง exacerbate → **eos ≥ 300: dupilumab** (anti-IL-4Rα — ถ้ามี chronic bronchitis) หรือ **mepolizumab** (anti-IL-5 — มีหรือไม่มี chronic bronchitis) (Figure 3.11 ใหม่ใน 2026) · หรือ azithromycin · roflumilast
- **ถอน ICS** จาก triple เฉพาะเมื่อเริ่มโดยไม่มีข้อบ่งชี้ ไม่ตอบสนอง ผลข้างเคียงมาก หรือ **pneumonia รุนแรง/ซ้ำ** · eos ≥ 300 ถอนแล้วเสี่ยง exacerbation
- **ผู้ที่ได้ LABA+ICS อยู่เดิม** (ไม่มี asthma): คุมได้ดีใช้ต่อได้ · ยัง exacerbate → eos ≥ 100 เป็น triple / eos < 100 เปลี่ยนเป็น LABA+LAMA · อาการเด่น → LABA+LAMA หรือ triple

### ยาเสริมที่ควรรู้กลไก
| ยา | กลไก | ใช้เมื่อ | ระวัง |
|---|---|---|---|
| **Azithromycin** (250 mg/วัน หรือ 500 mg 3 ครั้ง/สัปดาห์ นาน 1 ปีในการศึกษา) | ต้านอักเสบ ลด neutrophil ลด biofilm ต้านไวรัส | exacerbation ซ้ำ โดยเฉพาะผู้ที่ **ไม่สูบบุหรี่** | QT ยาว การได้ยินลด เชื้อดื้อยา · ตรวจ NTM ก่อน |
| **Roflumilast** (PDE4 inhibitor ชนิดกิน) | cAMP ในเซลล์อักเสบ ↑ → ลดการอักเสบ (ไม่ใช่ยาขยายหลอดลม) | FEV1 < 50% + chronic bronchitis + เคย admit | ท้องเสีย คลื่นไส้ **น้ำหนักลด** นอนไม่หลับ ซึมเศร้า · ห้ามคู่ theophylline |
| **Dupilumab / mepolizumab** | บล็อก T2 cytokine (IL-4/IL-13 · IL-5) | eos ≥ 300 ยัง exacerbate บน triple | ราคาแพงมาก · ไม่ใช่ยาบัญชีหลักสำหรับ COPD ในไทย |
| **Mucolytic** (NAC, carbocysteine, erdosteine) | ลดความหนืดเสมหะ ต้านออกซิแดนท์ | บางรายที่ไม่ได้ ICS | — |

### ยาที่ลดการตาย (Figure 3.19)
- **Triple therapy แบบ fixed-dose (IMPACT, ETHOS)** ลด all-cause mortality เทียบกับ LABA+LAMA ในผู้ที่มีอาการ (CAT ≥ 10) และ **exacerbation บ่อย (≥ 2 moderate) หรือรุนแรง (≥ 1 admit)**
- LABA+ICS (TORCH, SUMMIT) และ LAMA (UPLIFT) **ไม่ลดการตาย** ในการศึกษาที่ไม่ได้คัดคนที่ exacerbate
- ร่วมกับมาตรการที่ไม่ใช่ยา: เลิกบุหรี่ · rehab หลัง admit · LTOT · home NIV ในผู้ที่ hypercapnia มาก · LVRS ในคนที่เลือกแล้ว · ปลูกถ่ายปอด

### Disease activity (ส่วนใหม่ GOLD 2026)
- "disease activity" = กระบวนการทางชีววิทยาที่ทำให้โรคลุกลามและยังแก้ไขได้ · ตัวบ่งชี้: exacerbation อาการแย่ลงเรื้อรัง FEV1 ลดเร็ว emphysema ลุกลาม · biomarker ที่ใช้ได้ตอนนี้มีแค่ eosinophil
- **disease stability** = ไม่มี exacerbation + อาการไม่แย่ลง + FEV1 ไม่ลดเร็ว · **disease control** = stability + อาการต่ำกว่าเกณฑ์""",
    ["Follow-up algorithm ใช้ treatable trait (dyspnea/exacerbation) ไม่ใช้กลุ่ม ABE ซ้ำ",
     "LABA+LAMA ยัง exacerbate: eos ≥ 100 → ICS · eos < 100 → azithromycin หรือ roflumilast",
     "Triple ยัง exacerbate + eos ≥ 300 → dupilumab (chronic bronchitis) หรือ mepolizumab",
     "Triple fixed-dose ลดการตายในผู้ที่ exacerbate บ่อย/รุนแรง (IMPACT, ETHOS)"],
    [mcq(N(28), "[Read-more level] A 64-year-old ex-smoker with COPD (FEV1 42% predicted) has had three moderate exacerbations in the past year despite correct use of single-inhaler LABA+LAMA+ICS. He has chronic cough with sputum most days. Blood eosinophils have been 420 and 380 cells/µL. Which add-on therapy is supported by GOLD 2026?",
         ["Dupilumab", "Long-term oral prednisolone", "Switch to LABA + ICS", "Add a second LAMA", "Montelukast"], 0,
         "บน triple แล้วยัง exacerbate + **eos ≥ 300 + มี chronic bronchitis** → GOLD 2026 (Figure 3.11) แนะนำพิจารณา **dupilumab** (anti-IL-4Rα บล็อกสัญญาณ IL-4/IL-13 ของการอักเสบ T2 ลดการสร้างเมือก) — mepolizumab (anti-IL-5) เป็นอีกทางเลือก · azithromycin/roflumilast ก็พิจารณาได้\n\n"
         "- *prednisolone ระยะยาว* — ผลเสียมาก ไม่ลด exacerbation\n- *LABA + ICS* — ลดยาลง\n- *LAMA ซ้ำ 2 ตัว* — ไม่มีประโยชน์เพิ่ม เพิ่มผลข้างเคียง\n- *montelukast* — ไม่มีหลักฐานใน COPD",
         "Triple + eos ≥ 300 + chronic bronchitis → dupilumab", "Biologics", R("Chapter 3 Follow-up pharmacological management (Figure 3.11)"), [COPD])],
    [COPD, ICS],
    {"followup_rx": F.followup_rx()}, source=SRC)

# ───────────────────────────── 13 (อ่านเพิ่มเติม)
sec("chest-copd-13", "อ่านเพิ่มเติม (เกินระดับ NL) — pre-COPD, PRISm, AATD, CT/DLco, case-finding และ treatable traits",
    "pre-COPD · PRISm (ratio ≥ 0.7 แต่ FEV1 < 80%) · young COPD · LLN/z-score · GLI-Global · AATD · DLco · CT · HFNT", 7,
RM + """

### คำศัพท์ใหม่ (GOLD 2026)
| คำ | ความหมาย | ความสำคัญ |
|---|---|---|
| **pre-COPD** | มีอาการ และ/หรือ ความผิดปกติเชิงโครงสร้าง/การทำงาน (emphysema, ลมค้าง, DLco ต่ำ, FEV1 ลดเร็ว) แต่ **FEV1/FVC ≥ 0.7** | บางคนกลายเป็น COPD · ยังไม่มีหลักฐานการรักษานอกจากเลิกบุหรี่ |
| **PRISm** (preserved ratio impaired spirometry) | post-BD **FEV1/FVC ≥ 0.7 แต่ FEV1 < 80%** | พบ 7–11% ของประชากร · 20–30% กลายเป็น obstruction · เพิ่มโรคหัวใจและการตาย · สัมพันธ์อ้วน/ผอม |
| **young COPD** | อายุ 20–50 ปี | มักไม่ถูกวินิจฉัย · ประวัติวัยเด็ก/ครอบครัวสำคัญ |
| early / mild COPD | early ใช้กับงานวิจัยชีววิทยา · mild ใช้บอกความรุนแรงของ spirometry เท่านั้น | — |

### Spirometry เชิงลึก
- **LLN และ z-score** (−1.645 = 5th percentile) แม่นกว่าในคนอายุน้อยและผู้สูงอายุ · ถ้าสงสัย COPD ในคนอายุ < 50 ที่ ratio ≥ 0.7 ซ้ำ ให้ดู LLN · GOLD ยังใช้ fixed ratio
- GOLD 2026 แนะนำสมการ **GLI-Global** (ไม่แยกเชื้อชาติ) แต่ยังใช้ **FEV1 % predicted** แบ่งเกรด (ERS/ATS เสนอ z-score)
- **Lung volume** (body plethysmography): RV ↑ ตั้งแต่แรก TLC ↑ เมื่อรุนแรง · **DLco** ควรตรวจเมื่อเหนื่อยไม่สมกับ FEV1 — **DLco < 60%** สัมพันธ์อาการมากและการตาย · ในคนสูบบุหรี่ที่ spirometry ปกติ DLco < 80% เสี่ยงเป็น COPD
- 6-minute walk test และ **BODE index** (BMI, Obstruction, Dyspnea, Exercise) ทำนายการตายดีกว่าค่าเดี่ยว

### Imaging
- **CT** ไม่จำเป็นต่อการวินิจฉัย · ข้อบ่งชี้ (Figure 2.14): exacerbation ต่อเนื่อง · อาการไม่สมกับ PFT · **FEV1 15–45% + hyperinflation มาก** (ประเมินการลดปริมาตรปอด) · เข้าเกณฑ์คัดกรองมะเร็งปอด
- สิ่งที่ CT บอก: emphysema (พื้นที่ ≤ −950 HU) และการกระจาย · fissure สมบูรณ์หรือไม่ · **bronchiectasis ~30%** · mucus plug · ILA 4–9% · หลอดเลือดแดงปอดโต (PA:Ao > 1 เสี่ยง exacerbation) · หินปูนหลอดเลือดหัวใจ กระดูกบาง

### Alpha-1 antitrypsin deficiency
- ยีน **SERPINA1** · α1-AT สร้างที่ตับ ยับยั้ง **neutrophil elastase** ในปอด · ชนิด **PiZZ** โปรตีนพับผิดติดค้างในตับ (ตับแข็งได้) ระดับในเลือด < 20% ของปกติ → elastase ทำลายถุงลมไม่ยั้ง → **panlobular emphysema กลีบล่าง อายุน้อย** (บุหรี่เร่งมาก)
- GOLD แนะนำ **ตรวจระดับ AAT ในผู้ป่วย COPD ทุกราย** · ตรวจครอบครัว · augmentation therapy (ให้ AAT ทางหลอดเลือด) ในผู้ที่ขาดรุนแรง · heterozygote MZ/SZ ไม่ใช่ข้อบ่งชี้

### Case-finding และ treatable traits
- GOLD 2026 สนับสนุน **active case-finding** (แบบสอบถาม CDQ/CAPTURE, micro-spirometer, ทำ spirometry ในคนที่ทำ LDCT คัดกรองมะเร็งปอด) — UCAP trial: การค้นหาแล้วรักษาลด healthcare utilization · ไม่แนะนำ screening คนไม่มีอาการ/ความเสี่ยง
- **treatable traits** = ลักษณะที่วัดได้และมีการรักษาเฉพาะ (eos สูง → ICS · hyperinflation → LVR · hypoxemia → O2 · กล้ามเนื้อลีบ → rehab/โภชนาการ · ซึมเศร้า · OSA → CPAP)""",
    ["PRISm = FEV1/FVC ≥ 0.7 แต่ FEV1 < 80% · pre-COPD = มีความผิดปกติแต่ ratio ปกติ",
     "DLco < 60% = อาการมาก พยากรณ์แย่ · ตรวจเมื่อเหนื่อยไม่สมกับ FEV1",
     "AATD: panlobular emphysema กลีบล่าง อายุน้อย · GOLD แนะนำตรวจทุกราย",
     "CT เมื่อ: exacerbation ต่อเนื่อง · อาการไม่สมกับ PFT · ประเมินลดปริมาตรปอด · คัดกรองมะเร็ง"],
    [mcq(N(29), "[Read-more level] A 52-year-old current smoker has exertional breathlessness. Post-bronchodilator spirometry: FEV1 68% predicted, FVC 70% predicted, FEV1/FVC 0.76. Which term describes this result according to GOLD 2026?",
         ["COPD, GOLD grade 2", "Preserved ratio impaired spirometry (PRISm)", "Normal spirometry", "Asthma–COPD overlap", "Pure restrictive lung disease proven"], 1,
         "**FEV1/FVC 0.76 ≥ 0.7** จึงยังไม่ใช่ COPD แต่ **FEV1 68% < 80%** = **PRISm** · GOLD 2026: 20–30% ของ PRISm กลายเป็น obstruction · เพิ่มความเสี่ยงโรคหัวใจและการตาย · ต้องเลิกบุหรี่และติดตาม spirometry\n\n"
         "- *COPD GOLD 2* — ต้องมี ratio < 0.7 ก่อนจึงแบ่งเกรด\n- *ปกติ* — FEV1 ต่ำกว่าเกณฑ์\n- *asthma–COPD overlap* — GOLD 2026 เลิกใช้คำนี้\n- *restrictive พิสูจน์แล้ว* — ต้องวัด TLC จึงยืนยันได้ PRISm เกิดจากหลายสาเหตุ (อ้วน, ลมค้าง, ILD)",
         "Ratio ≥ 0.7 + FEV1 < 80% = PRISm", "PRISm", R("Chapter 1 PRISm"), [SPIRO, SPIROB])],
    [SPIRO, SPIROB, COPDB],
    {}, source=SRC)

# ───────────────────────────── 14 (อ่านเพิ่มเติม)
sec("chest-copd-14", "อ่านเพิ่มเติม (เกินระดับ NL) — ลดปริมาตรปอด ปลูกถ่ายปอด home NIV palliative care และโรคร่วมเชิงลึก",
    "LVRS (NETT) · endobronchial valve · bullectomy · เกณฑ์ปลูกถ่ายปอด · home NIV PaCO2 > 53 · palliative dyspnea · มะเร็งปอด · OSA overlap · MOLT", 8,
RM + """

### ลดปริมาตรปอด (lung volume reduction)
[[fig:ebv]]

| วิธี | ผู้ที่เหมาะ | ข้อควรรู้ |
|---|---|---|
| **LVRS** (ผ่าตัดเอาส่วน emphysema มากสุดออก) | emphysema รุนแรง **กลีบบนเด่น + exercise capacity ต่ำหลัง rehab** | NETT: **ยืดชีวิต** ในกลุ่มนี้ · ตายมากขึ้นถ้า FEV1 ≤ 20% + emphysema กระจายสม่ำเสมอ หรือ DLco ≤ 20% |
| **Endobronchial one-way valve (EBV)** | FEV1 15–45% + hyperinflation มาก + **fissure สมบูรณ์/ไม่มี collateral ventilation** | FEV1, 6MWD, คุณภาพชีวิตดีขึ้น · **pneumothorax ~27%** ส่วนใหญ่ใน 72 ชม. · กลีบยุบหลังทำ = รอดชีวิตดีขึ้น |
| Coil, vapor ablation | ไม่ต้องการ fissure สมบูรณ์ | หาได้น้อย |
| **Bullectomy** | bulla ใหญ่ > 1/3 ของทรวงอกกดปอดดี | เหนื่อยลด ปอด/หัวใจทำงานดีขึ้น |
| **ปลูกถ่ายปอด** | **ส่งปรึกษา**: โรคลุกลามแม้รักษาเต็มที่ ไม่เหมาะ LVRS, BODE 5–6, PaCO2 > 50 และ/หรือ PaO2 < 60, FEV1 < 25% · **ขึ้นทะเบียน**: BODE ≥ 7, FEV1 < 15–20%, severe exacerbation ≥ 3 ครั้ง/ปี, 1 ครั้งที่มี hypercapnic respiratory failure, PH ปานกลาง–รุนแรง | median survival 5.9 ปี · ปลูกถ่ายสองข้างดีกว่าในอายุ < 60 ปี |

กลไกร่วม: ตัด/ยุบส่วนที่พองโดยไม่ทำหน้าที่ → ปอดส่วนดีขยาย elastic recoil ดีขึ้น กะบังลมกลับเป็นโดม กล้ามเนื้อหายใจและหัวใจทำงานดีขึ้น

### Home NIV และ HFNT ระยะยาว
- ผู้ที่ **PaCO2 > 53 mmHg ค้างอยู่ 2–4 สัปดาห์หลัง discharge** — home NIV + O2 ยืดเวลาก่อน admit ซ้ำ/ตาย (RCT) · ใช้แรงดัน IPAP สูงพอจะลด CO2 จึงลดการตาย
- **COPD + OSA (overlap)**: **CPAP ลดการตายและการ admit** ชัดเจน — ถามกรน ง่วงกลางวัน อ้วน
- home HFNT อาจลด exacerbation ในผู้ที่ hypercapnia เรื้อรัง (กำลังศึกษา)

### Palliative และ end-of-life care
- อาการเหนื่อยดื้อต่อยา: ยาขยายหลอดลมเต็มที่ · rehab · **opioid** (morphine ขนาดต่ำบางการศึกษาช่วย) · **พัดลมเป่าหน้า** (กระตุ้น trigeminal ลดการรับรู้เหนื่อย) · chest wall vibration · NMES · O2 อาจช่วยแม้ไม่ hypoxemic · **benzodiazepine ไม่ช่วย**
- คุยเรื่อง advance care planning ตั้งแต่เนิ่น ๆ (การ admit เป็นจังหวะที่ดี) · การทำนายชีวิต 6 เดือนใน COPD ไม่แม่น · hospice สำหรับผู้ที่เหนื่อยขณะพักแม้ได้ยาเต็มที่และ admit บ่อย

### โรคร่วมเชิงลึก (บท 5 ที่เขียนใหม่ใน 2026)
- แนวทาง **4Ms**: Mentation · Mobility · Medications (> 90% ใช้ยาหลายตัว) · Morbidities · frailty พบบ่อยและทำนายผลแย่
- **มะเร็งปอด**: emphysema เพิ่มความเสี่ยงมากกว่าระดับ obstruction · LDCT ปีละครั้ง อายุ 50–80, ≥ 20 pack-year, ยังสูบหรือเลิก < 15 ปี · **ไม่แนะนำคัดกรองใน COPD ที่ไม่เคยสูบบุหรี่** · ICS ไม่เพิ่ม/ลดมะเร็ง
- **Pulmonary hypertension**: mPAP > 20 mmHg (25–30% ของ COPD มี PH เล็กน้อย · 5% รุนแรง PVR > 5 WU มักมี DLco < 45% และ obstruction ไม่มาก — "pulmonary vascular phenotype") → ส่งศูนย์ PH · ยา PAH ไม่แนะนำในรายไม่รุนแรง
- **MOLT** (multiple organ loss of tissue) = emphysema + BMI ต่ำ + กระดูกพรุน + sarcopenia → พยากรณ์แย่ · **CKD** อาจซ่อนเพราะ creatinine ต่ำจากกล้ามเนื้อน้อย · **secondary polycythemia** (Hb ≥ 17 ชาย/≥ 15 หญิง)
- **เบาหวาน**: steroid ทำน้ำตาลขึ้น ICS ขนาดสูงคุมเบาหวานแย่ลง · **GERD** เพิ่ม exacerbation (PPI ช่วยได้) · **BMI ที่ดีที่สุด 21–30**
- **ผ่าตัด**: เสี่ยงภาวะแทรกซ้อนทางปอดมากขึ้นเมื่อแผลใกล้กะบังลม · regional anesthesia เสี่ยงน้อยกว่า GA · เตรียมผู้ป่วยให้ดีที่สุดก่อนผ่าตัด
- **ข้อมูลส่วนท้ายบท 5 และบท 6 (AI/telehealth) อ่านจากไฟล์ไม่ได้** — ไม่ได้ใส่ในบทเรียน""",
    ["LVRS ยืดชีวิตใน emphysema กลีบบน + exercise capacity ต่ำ (NETT)",
     "EBV ต้องการ fissure สมบูรณ์ · ภาวะแทรกซ้อนหลัก pneumothorax",
     "Home NIV เมื่อ PaCO2 > 53 ค้าง 2–4 สัปดาห์หลัง admit · COPD + OSA → CPAP ลดตาย",
     "เหนื่อยระยะท้าย: opioid ขนาดต่ำ พัดลมเป่าหน้า rehab — ไม่ใช้ benzodiazepine"],
    [mcq(N(30), "[Read-more level] A 63-year-old ex-smoker has severe upper-lobe-predominant emphysema with marked hyperinflation (FEV1 28% predicted, RV 240% predicted) despite optimal therapy and pulmonary rehabilitation. CT shows intact fissures in the right upper lobe. Which statement about endobronchial one-way valve therapy is correct?",
         ["Valves work by allowing air to enter but not leave the treated lobe", "The most common serious early complication is pneumothorax",
          "Collateral ventilation across fissures improves the result", "It is contraindicated because the emphysema is upper-lobe predominant", "It permanently cures COPD"], 1,
         "valve ทางเดียวให้ **ลมออกได้แต่เข้าไม่ได้** กลีบที่พองจึงยุบ (ต้องมี **fissure สมบูรณ์/ไม่มี collateral ventilation**) · เมื่อกลีบเป้าหมายยุบเร็ว กลีบข้างเคียงขยายตัวทันที ทำให้เนื้อปอดที่เปราะฉีกขาด **pneumothorax พบ ~27% ส่วนใหญ่ใน 72 ชม.** — ต้องทำในศูนย์ที่จัดการได้\n\n"
         "- *ลมเข้าได้ออกไม่ได้* — กลับกัน จะทำให้พองยิ่งขึ้น\n- *collateral ventilation ช่วย* — ทำให้กลีบไม่ยุบ ล้มเหลว\n- *ห้ามใน upper lobe* — ใช้ได้ทั้งกลีบบนและล่าง\n- *รักษาหาย* — ช่วยอาการ ไม่ได้หยุดโรค",
         "EBV: ลมออกทางเดียว · ต้อง fissure สมบูรณ์ · pneumothorax", "Lung volume reduction", R("Chapter 3 Interventional and surgical treatments"), [COPD])],
    [COPD, ARF, PTX],
    {"ebv": F.ebv()}, source=SRC)

# ───────────────────────────── MEQ / OSCE
LECNAME = "Pneumonia / Asthma / COPD (Basic) (AL) (อ.เกรียงศักดิ์) — ส่วน COPD"
MEQ = [{"id": "CH-COPD-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
        "topic": "Newly diagnosed biomass-related COPD — assessment, initial treatment and later hypercapnic exacerbation",
        "nl": [COPD, COPDB, SPIRO, BD, ICS, AE, ABG, TOB], "ref": R("Chapter 2–4") + ["BTS/ERS — controlled oxygen and NIV (เป้า SpO2 88–92%)"],
        "vignette": "หญิงไทยอายุ 62 ปี อาชีพทำนา อ.แม่แจ่ม จ.เชียงใหม่ มา OPD ด้วยเหนื่อยเวลาเดินขึ้นเนิน/ขึ้นบันไดมา 2 ปี ค่อย ๆ มากขึ้น ตอนนี้ต้องหยุดพักเมื่อเดินบนพื้นราบตามจังหวะตัวเอง ไอมีเสมหะขาวทุกเช้า\n"
                    "ประวัติ: ไม่เคยสูบบุหรี่ สามีสูบยาเส้นในบ้านวันละ 10 มวน · **หุงข้าวด้วยฟืนและถ่านในครัวปิดตั้งแต่อายุ 20 ปี** · ไม่เคยเป็นวัณโรค ไม่มีโรคภูมิแพ้ในวัยเด็ก\n"
                    "ปีที่แล้วเคยไปสถานีอนามัยด้วยไอเสมหะเขียวและเหนื่อยมากขึ้น 1 ครั้ง ได้ amoxicillin-clavulanate และ prednisolone 5 วัน ไม่ได้นอนโรงพยาบาล\n"
                    "PE: BMI 19 kg/m2 · RR 20/min · SpO2 94% room air · ทรวงอก AP diameter เพิ่ม เคาะโปร่ง เสียงหายใจเบาทั้งสองข้าง หายใจออกยาว มี end-expiratory wheeze เล็กน้อย · ไม่มีนิ้วปุ้ม ไม่มีขาบวม JVP ไม่สูง\n"
                    "Spirometry (post-bronchodilator): FEV1 1.10 L (58% predicted) · FVC 2.05 L (82% predicted) · FEV1/FVC 0.54 · FEV1 เพิ่มหลังยาขยายหลอดลม 90 mL (6%)\n"
                    "CBC: Hb 13.2 g/dL · eosinophil 380 cells/µL · CXR: ปอดพอง กะบังลมแบน ไม่มีก้อนหรือแผลเป็นวัณโรค · CAT score 16 · mMRC 2",
        "questions": [
            {"q": "1. จงแปลผล spirometry และให้การวินิจฉัยพร้อมเกรดความรุนแรง (3 คะแนน)",
             "a": "- **post-BD FEV1/FVC 0.54 < 0.7** = มี **persistent airflow obstruction** (1)\n- FVC 82% ไม่บ่ง restriction · BD response 90 mL/6% ไม่มีนัย — และ GOLD 2026 **ไม่ใช้ reversibility แยก asthma กับ COPD** (0.5)\n"
                  "- FEV1 58% predicted = **GOLD 2 (moderate, 50–79%)** (1)\n- วินิจฉัย: **COPD จากควันชีวมวล (biomass-related COPD) + ควันบุหรี่มือสอง** — อาการ + ปัจจัยเสี่ยงเข้ากันในบริบททางคลินิก ไม่มีลักษณะ asthma/TB/HF (0.5)"},
            {"q": "2. จงอธิบายกลไกที่ทำให้ผู้ป่วยเหนื่อยเวลาออกแรง และกลไกของอาการแสดงที่ตรวจพบในทรวงอก (3 คะแนน)",
             "a": "- ควันชีวมวลกระตุ้น macrophage/neutrophil → protease ทำลายผนังถุงลม (emphysema) + small airway อักเสบหนา เสมหะอุด → **แรงต้านเพิ่ม elastic recoil ลด หลอดลมเล็กแฟบตอนหายใจออก** → ลมออกช้า FEV1 ลด (1)\n"
                  "- **dynamic hyperinflation**: ออกแรงหายใจเร็ว เวลาหายใจออกสั้น ลมค้างสะสม EELV สูง IC แคบ ปริมาตรหายใจเข้าชนเพดาน กล้ามเนื้อหายใจเสียเปรียบ = เหนื่อย · กล้ามเนื้อขาเสื่อมจากไม่ได้ใช้ร่วมด้วย (1)\n"
                  "- AP diameter เพิ่ม/เคาะโปร่ง/เสียงหายใจเบา = ปอดพองมีลมมาก เนื้อปอดนำเสียงน้อย · หายใจออกยาว + wheeze = ลมผ่านหลอดลมแคบช้าและทำให้ผนังสั่น (1)"},
            {"q": "3. จงจัดกลุ่มผู้ป่วยตาม GOLD 2026 พร้อมเหตุผล (2 คะแนน)",
             "a": "- exacerbation ที่รักษาด้วย antibiotic + prednisolone 1 ครั้ง = **moderate exacerbation 1 ครั้งในปีที่ผ่านมา** → **กลุ่ม E** (GOLD 2026 ปรับให้ 1 moderate ก็เข้า E) (1.5)\n"
                  "- บันทึกเป็น **COPD GOLD 2, group E** · CAT 16/mMRC 2 บอกว่าอาการมากด้วย แต่ไม่เปลี่ยนกลุ่ม (ถ้าตอบกลุ่ม B ตามเกณฑ์ GOLD ฉบับก่อน ≥ 2 ครั้ง ได้ 0.5) (0.5)"},
            {"q": "4. จงให้การรักษาด้วยยาเริ่มต้น พร้อมเหตุผลเรื่องการใช้ ICS (3 คะแนน)",
             "a": "- กลุ่ม E → **LABA + LAMA** เป็นหลัก (1)\n- **eosinophil 380 ≥ 300** → **พิจารณา LABA + LAMA + ICS (triple) ตั้งแต่แรก** เพราะการอักเสบแบบ T2 ตอบสนองต่อ ICS ลด exacerbation ได้มาก · ใช้ single-inhaler ถ้าได้ (1)\n"
                  "- ไม่ใช้ LABA + ICS · ไม่มีประวัติ TB/pneumonia ซ้ำที่เป็นข้อห้าม ICS · **SABA สำหรับบรรเทาอาการ** · เลือก device ตามแรงสูด สอนและให้ทำกลับ (teach-back) แนะนำบ้วนปากหลังพ่น ICS (1)"},
            {"q": "5. จงบอกการดูแลที่ไม่ใช่ยาที่สำคัญสำหรับผู้ป่วยรายนี้ (3 คะแนน)",
             "a": "- **ลด exposure**: เปลี่ยนเป็นเตาแก๊ส/เตาไร้ควัน ย้ายครัวหรือเพิ่มการระบายอากาศ · **ให้สามีเลิกบุหรี่/ไม่สูบในบ้าน** (5A แก่สามี) · หลีกเลี่ยงหมอกควันช่วง PM2.5 สูง ใส่หน้ากาก (1)\n"
                  "- **วัคซีน**: influenza ทุกปี · pneumococcal (PCV20/PCV21) · RSV (อายุ 50–74 ปีที่มีโรคปอดเรื้อรัง) · Tdap · zoster (1)\n"
                  "- **pulmonary rehabilitation** (กลุ่ม E) · **โภชนาการ** (BMI 19 < 21 พยากรณ์แย่) · written action plan สอนสังเกตอาการ exacerbation · นัดติดตามประเมินอาการ ท่าพ่นยา · spirometry ปีละครั้ง (1)"},
            {"q": "6. หนึ่งปีต่อมา ผู้ป่วยมาห้องฉุกเฉินด้วยไข้ ไอเสมหะเขียวมากขึ้น เหนื่อยมาก 3 วัน ญาติให้ O2 ถังที่บ้าน 10 L/min ทาง mask ระหว่างทาง ตอนนี้ง่วงซึมแต่ปลุกตื่น RR 28/min · ABG: pH 7.27 · PaCO2 70 mmHg · PaO2 140 mmHg · HCO3 32 mmol/L · CXR ไม่มี consolidation จงแปลผลและให้การรักษาตามลำดับ (4 คะแนน)",
             "a": "- **ABG**: acidemia + PaCO2 สูง = **acute-on-chronic respiratory acidosis** (HCO3 32 สูงจากการชดเชยเดิม แต่ pH ยังต่ำ = มีส่วนเฉียบพลันซ้อน) · PaO2 140 = **ได้ O2 มากเกิน** ทำให้ CO2 คั่งเพิ่มจาก V/Q mismatch ที่แย่ลง (ปลด hypoxic vasoconstriction) + Haldane effect (1)\n"
                  "- **ลด O2 ไม่ใช่หยุด**: Venturi 24–28% ไตเตรต **SpO2 88–92%** · ABG ซ้ำใน 30–60 นาที (0.5)\n"
                  "- **NIV (BiPAP)** ทันที เพราะ pH ≤ 7.35 + PaCO2 ≥ 45 และยังปลุกตื่น ไม่มีข้อห้าม · เตรียมใส่ท่อถ้าแย่ลง/ซึมลง/ไม่ดีขึ้นใน 1–2 ชม. (1)\n"
                  "- **SABA + SAMA** พ่น (nebulizer ขับด้วยลมอัด) · **prednisolone 40 mg × 5 วัน** · **antibiotic** (เสมหะเป็นหนอง + ไข้ + ใช้ NIV → ข้อบ่งชี้ชัด) เช่น amoxicillin-clavulanate 5 วัน · ป้องกัน DVT · หา PE/HF/pneumonia ร่วม (1)\n"
                  "- ก่อนกลับบ้าน: ทบทวนท่าพ่นยาและ adherence · pulmonary rehab ภายใน 4 สัปดาห์ · นัด 1 เดือน · ประเมิน LTOT/home NIV ตอน stable (PaCO2 > 53 ค้างหลัง 2–4 สัปดาห์ → พิจารณา home NIV) · สอนญาติเรื่องการให้ O2 เกิน (0.5)"}]}]

OSCE = [{"id": "CH-COPD-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
         "topic": "OSCE – Teaching a patient with COPD to use a pMDI with spacer, and checking DPI technique",
         "station": "OSCE (สอนผู้ป่วย) 7 นาที",
         "nl": [COPD, BD, ICS], "ref": R("Chapter 3 Managing inhaled therapy"),
         "instruction": "ชายอายุ 70 ปี เป็น COPD (GOLD 3, group E) แพทย์สั่งยาพ่นชนิด pMDI (LABA+LAMA+ICS) พร้อม spacer ผู้ป่วยเคยใช้ยาผงแห้ง (DPI) มาก่อนแต่ \"พ่นแล้วไม่รู้สึกว่ายาเข้า\" และยังมี exacerbation\n\n"
                        "**จงสอนผู้ป่วย (ผู้ป่วยมาตรฐาน) ใช้ pMDI ร่วมกับ spacer ให้ถูกต้อง ตรวจว่าผู้ป่วยทำได้ และอธิบายว่าทำไม DPI เดิมอาจไม่ได้ผล ภายใน 7 นาที** · มี pMDI หลอดฝึก spacer และ DPI ตัวอย่างวางไว้ให้",
         "answer": "**เกณฑ์ให้คะแนน (16 คะแนน)**\n\n| ข้อ | สิ่งที่ต้องทำ | คะแนน |\n|---|---|---|\n"
                   "| 1 | แนะนำตัว ยืนยันตัวผู้ป่วย ถามความเข้าใจเดิมเรื่องยาพ่นและปัญหาที่เจอ ใช้ภาษาง่าย | 1 |\n"
                   "| 2 | ขอให้ผู้ป่วย **สาธิต DPI แบบเดิม** ก่อน และสังเกตข้อผิดพลาด (เป่าลมเข้าเครื่อง · สูดเบา/ช้า · ไม่กลั้นหายใจ) | 2 |\n"
                   "| 3 | อธิบาย **ทำไม DPI ไม่ได้ผล**: ผงยาต้องใช้แรงสูดเร็วและแรงจึงแตกเป็นอนุภาคเล็กลงปอด ถ้าแรงสูดไม่พอยาค้างในเครื่อง/คอ — จึงเปลี่ยนเป็น pMDI + spacer | 2 |\n"
                   "| 4 | เตรียม pMDI: เปิดฝา ตรวจปากกระบอก **เขย่า** · หลอดใหม่/ไม่ได้ใช้นานให้พ่นทิ้งตามเอกสารกำกับ · เสียบเข้า spacer | 2 |\n"
                   "| 5 | **หายใจออกให้สุด (ไม่เป่าเข้า spacer)** → อมปากกระบอก spacer ให้สนิท | 1 |\n"
                   "| 6 | **กด 1 ครั้ง แล้วสูดช้า ๆ ลึก ๆ** (3–5 วินาที — ถ้า spacer มีเสียงหวีดแปลว่าสูดเร็วเกิน) หรือหายใจเข้าออกปกติ 4–5 ครั้งผ่าน spacer | 2 |\n"
                   "| 7 | **กลั้นหายใจ 5–10 วินาที** · ถ้าต้องพ่นซ้ำรอ 30–60 วินาทีแล้วเขย่าใหม่ · กด 1 ครั้งต่อการสูด 1 ชุด | 1 |\n"
                   "| 8 | **บ้วนปาก กลั้วคอ** หลังพ่น (มี ICS → ลดเชื้อราในปากและเสียงแหบ) · ล้าง spacer สัปดาห์ละครั้ง ผึ่งให้แห้งไม่เช็ด (ลดไฟฟ้าสถิต) | 2 |\n"
                   "| 9 | **ให้ผู้ป่วยสาธิตกลับ (teach-back)** แก้ข้อผิดพลาดจนถูกต้อง · นัดให้นำยามาทุกครั้ง · บอกวิธีดูยาที่เหลือ/ตัวนับ | 2 |\n"
                   "| 10 | สรุป เปิดโอกาสถาม แยกยาควบคุม (ทุกวัน) กับยาบรรเทาอาการ (SABA) | 1 |\n\n"
                   "**จุดตาย**: ไม่ให้ผู้ป่วยสาธิตกลับ · สอนให้สูดแรงเร็วกับ pMDI (สับสนกับ DPI) · กดพ่นหลายครั้งเข้า spacer ในครั้งเดียว · ไม่แนะนำบ้วนปากหลังยาที่มี ICS\n\n"
                   "**เหตุผลตาม GOLD 2026**: ผู้ป่วยมากกว่า 2 ใน 3 ใช้ยาพ่นผิดอย่างน้อย 1 ขั้น · teach-back ได้ผลดีที่สุด · การเปลี่ยน device โดยไม่สอนใหม่เพิ่ม exacerbation"}]

LECTURE = {
 "lec": LEC, "date": "อ. 20 ต.ค.", "title": "COPD — โรคปอดอุดกั้นเรื้อรัง (GOLD 2026)",
 "subtitle": "หัวข้อ 1–11 = ความรู้ระดับ NL (นิยาม ปัจจัยเสี่ยง กลไกอาการ spirometry ABE แยกโรค ยา inhaler การรักษาระยะคงที่ LTOT exacerbation O2 NIV) · หัวข้อ 12–14 = อ่านเพิ่มเติม เกินระดับ NL",
 "objectives": [
   "บอกนิยาม COPD ตาม GOLD 2026 และปัจจัยเสี่ยงในบริบทไทย (บุหรี่/ยาเส้น ควันชีวมวล PM2.5 อาชีพ วัณโรคเก่า) คำนวณ pack-year ได้",
   "อธิบายกลไก airflow obstruction, air trapping, dynamic hyperinflation, V/Q mismatch และ cor pulmonale แล้วใช้อธิบายอาการและอาการแสดง",
   "แปลผล spirometry (post-BD FEV1/FVC < 0.7) แบ่งเกรด GOLD 1–4 และรู้ข้อจำกัดของ PEF และ CXR",
   "จัดกลุ่ม ABE ตาม GOLD 2026 (1 moderate exacerbation = E) ด้วย mMRC/CAT และประวัติ exacerbation",
   "แยก COPD จาก asthma หัวใจล้ม bronchiectasis และโรคปอดหลังวัณโรค",
   "อธิบายกลไกและผลข้างเคียงของ SABA/SAMA/LABA/LAMA/ICS เลือกยาเริ่มต้นตามกลุ่ม และใช้ eosinophil ตัดสินใจเรื่อง ICS",
   "สอนการใช้ pMDI + spacer และ DPI ได้ถูกต้อง",
   "ให้คำแนะนำเลิกบุหรี่ (5A/5R + ยา) วัคซีน pulmonary rehab และบอกข้อบ่งชี้ LTOT",
   "ประเมินและรักษา acute exacerbation: แยกโรคเลียนแบบ ยา 3 กลุ่ม ข้อบ่งชี้ antibiotic O2 แบบควบคุม และข้อบ่งชี้ NIV/ใส่ท่อช่วยหายใจ วางแผนก่อนกลับบ้าน"],
 "nlGap": "หัวข้อ 1–11 ตรงกับเกณฑ์ฯ แพทยสภา: COPD (`นล. 2.3.10(3)` กลุ่ม 2 — ดูแลเองได้, `B6.2.2(5)`) · exacerbation (`นล. 2.2.11`) · respiratory failure (`2.2.9`, `B6.2.5(1)`) · spirometry (`3.3.18`, `B6.3(3)`) · ABG (`3.3.17`) · ยาขยายหลอดลม/ICS (`B6.4(4)`, `B6.4(5)`) · บุหรี่ (`2.3.19(6)`) · "
          "**หัวข้อ 12–14 เกินระดับที่ NL ต้องการ** (biologics, roflumilast, LVRS/valve, ปลูกถ่ายปอด, PRISm, AATD) ใส่ไว้เป็นความรู้อ่านเพิ่มเติม · "
          "คาบนี้ไม่มีสไลด์อาจารย์ — เนื้อหาเรียบเรียงจาก **GOLD 2026 Report** ซึ่งข้อความที่ดึงได้ถูกตัดที่หน้า 127 (ท้ายบท 5, บท 6 และ Appendix อ่านไม่ได้) และรูป/ตารางทั้งหมดเป็นภาพ — ส่วนที่อยู่ในรูป (ตาราง mMRC, ตัวเลข ABE, เป้า SpO2 88–92%, ข้อบ่งชี้ admit/NIV/ใส่ท่อ, ยาเลิกบุหรี่) อิง GOLD 2025 และแนวทางด้านล่าง และระบุไว้ในบทเรียนตรงจุดที่ใช้",
 "guidelines": [
   "**GOLD 2026 Report** — Global Strategy for the Diagnosis, Management, and Prevention of COPD (v1.3, 8 Dec 2025) · แหล่งหลัก",
   "**GOLD 2025 Report** — รูปและตารางที่อ่านจากไฟล์ 2026 ไม่ได้ (mMRC, ABE, differential diagnosis, admission/NIV/IMV indications, ICS against)",
   "**BTS Guideline for oxygen use in healthcare and emergency settings (2017)** — เป้า SpO2 88–92% ในผู้เสี่ยง hypercapnic respiratory failure",
   "**ERS/ATS Clinical Practice Guidelines: noninvasive ventilation for acute respiratory failure (2017)** — NIV ใน AECOPD ที่มี acidosis",
   "**ERS Clinical Practice Guideline on high-flow nasal cannula (2022)** — NIV ก่อน HFNT ใน hypercapnic AECOPD (อ้างใน GOLD 2026)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ───────────────────────────── กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ตัวเลือกเรียงตามธรรมชาติไม่สลับ
ORDERED = {N(2), N(7)}
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

# ───────────────────────────── เขียนลงไฟล์ แล้วผูกข้อคลัง Ward Drill คาบ 37 (เฉพาะข้อ COPD)
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
BANK_MAP = {
    "chest-copd-04": ["CH-OLD-48"],
    "chest-copd-08": ["CH-OLD-49"],
    "chest-copd-09": ["CH-MCQ-37", "CH-OLD-50", "CH-MCQ-39"],
    "chest-copd-10": ["CH-MCQ-38", "CH-OLD-51"],
}
added = link(SET, LEC, BANK_MAP, meq=["CH-MEQ-02"], osce=[])

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == LEC][0]
seen = set()
for f in os.listdir(os.path.join(BUILD, "data")):
    if f.endswith(".json") and f not in ("nl.json", "index.json"):
        for l in json.load(open(os.path.join(BUILD, "data", f), encoding="utf-8")):
            for x in [i for s_ in l["sections"] for i in s_["items"]] + l["meq"] + l["osce"] + [{"id": s_["id"]} for s_ in l["sections"]]:
                assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
                seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = ({c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])}
         | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])})
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s_ in L["sections"]:
    assert "```" not in s_["md"], s_["id"]
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET:
        m["lectureCount"] = len(data)
        m["intro"] = INTRO
        m["howto"] = HOWTO
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d (NL %d + อ่านเพิ่มเติม %d) | ข้อใหม่ %d + คลัง %d = %d | meq %d | osce %d | ภาพ %d | nl %d" % (
    len(S), sum(1 for s_ in S if not s_["title"].startswith("อ่านเพิ่มเติม")), sum(1 for s_ in S if s_["title"].startswith("อ่านเพิ่มเติม")),
    sum(1 for s_ in S for i in s_["items"] if i["id"].startswith("CH-COPD")), added,
    sum(len(s_["items"]) for s_ in L["sections"]), len(L["meq"]), len(L["osce"]), sum(len(s_["figs"]) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for s_ in S for i in s_["items"] if i["id"].startswith("CH-COPD")).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
