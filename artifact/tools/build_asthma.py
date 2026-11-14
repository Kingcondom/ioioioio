#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ chest "AST" Asthma — การวินิจฉัยและการรักษาโรคหืด (GINA) · อ. 3 พ.ย. 2569 → data/chest.json
ต้นฉบับ: เสียงบันทึก Plaud of_91d6b4bd2505e94aa563a62daced04ed "11-03 การบรรยาย: การวินิจฉัยและการจัดการโรคหืด" (85 นาที)
  — เป็นคาบ active learning: นักศึกษานำเสนอ อาจารย์แทรกแก้/เน้น · โน้ต slides/asthma_plaud_notes.md
ไม่มีไฟล์สไลด์ asthma ใน Drive โฟลเดอร์ lecture → ส่วนที่ไม่ได้พูดในคาบ/ตัวเลขในตาราง อิง GINA 2024/2025 (ระบุในบทเรียน)
ภาพนิ่ง + ภาพเคลื่อนไหว + หลักจำ: anims_chest_ast.py
หัวข้อ 1–12 = ระดับ NL (asthma กลุ่ม 2) · หัวข้อ 13 = "อ่านเพิ่มเติม (เกินระดับ NL)"
คลัง Ward Drill คาบ 37: ผูกข้อ asthma (CH-MCQ-36, CH-OLD-52..55, CH-MEQ-05) — ข้อ COPD อยู่ในคาบ 37 แล้ว ข้อ pneumonia ยังว่าง"""
import json, os, re, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
REPO = os.path.dirname(BUILD)
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(REPO, "dashboard"))
from link_bank import link
from patch_learn_anim import _insert_marker
import anims_chest_ast as AN

SET, LEC = "chest", "AST"
LECNAME = "Asthma — วินิจฉัยและรักษาโรคหืด (GINA)"
SRC = "คาบ active learning อ. 3 พ.ย. (เสียงบันทึก Plaud) + GINA 2024/2025"
SRC_G = "GINA 2024/2025 (ส่วนนี้ไม่ได้พูดละเอียดในคาบ)"
S = []

# รหัส นล. (เกณฑ์แพทยสภา 2567)
AST, ASTB, AE, ARF, RF = "2.3.10(1)", "B6.2.2(2)", "2.2.11", "2.2.9", "B6.2.5(1)"
SPIRO, SPIROB, ABG, ABGB = "3.3.18", "B6.3(3)", "3.3.17", "B6.3(2)"
BD, ICS, LTRA, CORT, IMMOD = "B6.4(4)", "B6.4(5)", "B6.4(6)", "B11.4(3)", "B1.7.4"
HYP, ANA, ANTIG = "B1.4.11", "B1.4.11(1)", "B1.4.5"
DYS, COUGH, RHIN, RHINB, POLYP = "2.1.34", "2.1.32", "2.3.10(8)", "B6.2.2(1)", "2.3.10-3(3)"
TOB, ADR, PK, IMM, OSA, PREG = "2.3.19(6)", "B1.7.1(4)", "B1.7.1(3)", "B1.4.8", "2.3.10-3(5)", "2.3.15-3(11)"
MECH, AIRC, EXER, GAS, CTRL, SHOCK = "B6.1.2(2)", "B6.1.2(1)", "B6.1.2(6)", "B6.1.2(4)", "B6.1.2(3)", "2.2.7"
BASE = [AST, ASTB]

RM = ("> **อ่านเพิ่มเติม — เกินระดับที่ NL ต้องการ** · หัวข้อนี้สรุปจาก GINA 2024 (severe asthma) สำหรับคนที่อยากรู้ลึก "
      "ข้ามได้ถ้าเป้าหมายคือสอบ NL · อาจารย์พูดถึงแผนภาพ T2-high/T2-low กับเป้ายาในคาบ แต่ไม่ได้สอนรายละเอียดยา")


def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, src=SRC):
    s = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
         "nl": nl, "md": md, "pearls": pearls, "items": items}
    if figs:
        s["figs"] = figs
    S.append(s)


def mcq(n, stem, choices, explain, pearl, topic, ref, nl, keep=False):
    """คำตอบถูกเขียนไว้ที่ choices[0] เสมอ · บล็อก spread ท้ายสคริปต์จะกระจายตำแหน่งให้"""
    assert len(choices) == 5 and len(set(choices)) == 5, n
    d = {"id": "CH-AST-MCQ-%02d" % n, "kind": "mcq", "stem": stem, "choices": choices, "answer": 0,
         "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
    if keep:
        d["_keep"] = True
    return d


G = lambda p: ["GINA 2024 — " + p]
CLS = "คาบ AST (อ. 3 พ.ย.) — "

# ═════════════════════════════════════════════ 1
sec("chest-ast-01", "Asthma คืออะไร — นิยาม GINA อาการแปรปรวน และ phenotype",
    "นิยามสองขา: อาการแปรปรวน + variable expiratory airflow limitation · ไอ → แน่นอก → เหนื่อย · phenotype กับ endotype", 8,
"""> **บทเรียนนี้มาจากไหน** · เรียบเรียงจาก **คาบ active learning วันอังคาร 3 พ.ย.** (เสียงบันทึก Plaud 85 นาที — นักศึกษาแต่ละกลุ่มนำเสนอ อาจารย์แทรกแก้และย้ำ) · **ไม่มีไฟล์สไลด์ asthma ใน Drive** จึงไม่มีภาพสไลด์จริง — ตัวเลขในตาราง ขนาดยา และหัวข้อที่ไม่ได้พูดในคาบ (MgSO4, AERD, ตั้งครรภ์, exercise-induced, biologics) อิง **GINA 2024/2025** และระบุไว้ตรงจุด
> จุดที่อาจารย์แก้หรือย้ำในห้อง ติดป้าย **อาจารย์เน้น** — ให้ถือเป็นจุดที่น่าจะออกสอบ
> หัวข้อ 1–12 = ความรู้ระดับ NL (asthma อยู่ใน `นล. 2.3.10(1)` **กลุ่ม 2 ต้องวินิจฉัยและดูแลได้เอง** · exacerbation อยู่ใน `นล. 2.2.11`) · หัวข้อ 13 = **อ่านเพิ่มเติม (เกินระดับ NL)**

### นิยาม (GINA)
**Asthma** = โรคที่ต่างกันในแต่ละคน มักมี **การอักเสบเรื้อรังของทางเดินหายใจ** นิยามด้วย 2 ขา
1. **อาการทางเดินหายใจ** — wheeze · หายใจลำบาก · แน่นหน้าอก · ไอ — ที่ **แปรปรวนทั้งเวลาและความรุนแรง**
2. **variable expiratory airflow limitation** ที่ตรวจยืนยันได้ (spirometry/PEF — หัวข้อ 4)

**อาจารย์เน้น**: นิยามปัจจุบัน **ไม่มีคำว่า obstruction และไม่มีเกณฑ์ FEV1/FVC < 0.70** — ถ้าเจอคำตอบแบบนั้นแปลว่าใช้ข้อมูลเก่า (อาจารย์เตือนว่า AI ที่ใช้ database เดิมมักตอบผิดตรงนี้ ถ้าจะใช้ให้ระบุว่า "ตาม GINA ฉบับปี…")

### อาการแบบไหนชวนคิดถึง asthma
| ลักษณะ | เหตุผล |
|---|---|
| มีมากกว่า 1 อาการ (wheeze, เหนื่อย, แน่นอก, ไอ) | การอักเสบ + หลอดลมหดเกร็งทำให้เกิดหลายอาการพร้อมกัน |
| **เป็น ๆ หาย ๆ** แย่ช่วงกลางคืน/เช้ามืด | อาจารย์: "มีช่วงเป็น มีช่วงหาย — ถ้าเป็นตลอดไม่เหมือน asthma" |
| มีตัวกระตุ้น: ไวรัส · allergen (ไรฝุ่น แมว เกสร) · ออกกำลัง · หัวเราะ · อากาศเย็น ความชื้น ฝน แอร์ · ควันบุหรี่ PM2.5 | หลอดลมไวเกิน (AHR) ตอบสนองต่อสิ่งที่คนปกติไม่ตอบสนอง |
| เริ่มวัยเด็ก มีภูมิแพ้จมูก eczema ประวัติครอบครัว | atopy — แต่ adult-onset ก็พบได้ |

**อาจารย์ถาม "อาการที่น้อยที่สุดคืออะไร"** → **ไอ** · มากขึ้นเป็น **แน่นอก** · มากที่สุดคือ **เหนื่อย** จนต้องรีบมาโรงพยาบาล

ลักษณะที่ทำให้ **ไม่น่าเป็น asthma** (GINA): ไอเดี่ยว ๆ ไม่มีอาการอื่น · **มีเสมหะเรื้อรัง** · เวียนหัว มึน ชาปลายมือ (hyperventilation) · เจ็บหน้าอก · เสียงหวีดช่วง **หายใจเข้า** (stridor)

### Phenotype กับ endotype (อาจารย์เน้น)
- **phenotype** = ลักษณะที่ผู้ป่วยแสดงออก · **endotype** = กลไกการอักเสบเบื้องหลัง
- phenotype ที่นักศึกษานำเสนอ (GINA): **allergic** (พบบ่อยที่สุด เริ่มวัยเด็ก eosinophilic) · **non-allergic** · **adult-onset** (ไม่มีภูมิแพ้ → ถามอาชีพ) · **persistent airflow limitation** (เป็นนานจน remodeling) · **obesity** · **cough-variant** (ไอเด่น ไม่มี wheeze)
- อาจารย์จัดให้ง่ายกว่าด้วย "การอักเสบ" 3 กลุ่ม: **allergic eosinophilic** · **non-allergic eosinophilic** (สองกลุ่มนี้ = **T2-high**) · **non-eosinophilic** (neutrophilic หรือ paucigranulocytic = **T2-low**) — รายละเอียดหัวข้อ 2
- อาจารย์: แบ่งได้อีกหลายแบบ — classic (ไอ + หลอดลมตีบ) vs **cough-variant** (ไออย่างเดียว) · ตามโรคร่วม (asthma + chronic rhinosinusitis, + chronic bronchitis)

### ทำไมต้องจริงจัง
- ผู้ป่วยทั่วโลกราว 300 ล้านคน · การเสียชีวิตส่วนใหญ่ **ป้องกันได้** — สัมพันธ์กับการไม่ได้ ICS, ใช้ SABA มากเกิน และประเมินความรุนแรงต่ำไป (หัวข้อ 6, 10)""",
    ["Asthma = อาการแปรปรวน + variable expiratory airflow limitation — ไม่มีเกณฑ์ FEV1/FVC < 0.70",
     "อาการน้อยสุดคือไอ → แน่นอก → เหนื่อย · เป็น ๆ หาย ๆ แย่กลางคืน/เช้ามืด",
     "เสมหะเรื้อรัง ชาปลายมือ stridor ตอนหายใจเข้า = คิดโรคอื่นก่อน",
     "phenotype = สิ่งที่เห็น · endotype = กลไก · T2-high = allergic และ non-allergic eosinophilic",
     "ตรวจปอดปกติช่วงไม่มีอาการ ไม่ตัด asthma"],
    [mcq(1, "Which of the following best reflects the current GINA definition of asthma?",
         ["Variable respiratory symptoms with variable expiratory airflow limitation",
          "Persistent airflow obstruction with a post-bronchodilator FEV1/FVC below 0.70",
          "Chronic productive cough for 3 months in each of 2 consecutive years",
          "Airway eosinophilia confirmed by induced sputum or bronchial biopsy",
          "Raised total serum IgE together with a positive skin prick test"],
         "GINA นิยาม asthma ด้วย **2 ขา**: ประวัติอาการทางเดินหายใจที่ **แปรปรวน** (wheeze เหนื่อย แน่นอก ไอ) และ **variable expiratory airflow limitation** ที่ยืนยันได้ — กลไกคือหลอดลมหดเกร็งและบวมจากการอักเสบที่ \"มาแล้วไป\" ค่าการไหลของลมจึงเปลี่ยนไปตามเวลาและตามยา\n\n"
         "- \"FEV1/FVC below 0.70 คงอยู่\" — เป็นเกณฑ์ของ COPD · **อาจารย์เน้น** ว่า asthma ไม่มีเกณฑ์ ratio\n"
         "- \"ไอมีเสมหะ 3 เดือน 2 ปีติดกัน\" — นิยาม chronic bronchitis\n"
         "- \"eosinophil ในเสมหะ/ชิ้นเนื้อ\" — บอก endotype T2 ไม่ใช่นิยามโรค และ asthma แบบ T2-low ไม่มี\n"
         "- \"IgE สูง + skin test บวก\" — บอกแค่ภาวะภูมิแพ้ (sensitisation) ไม่ใช่ asthma",
         "นิยาม = อาการแปรปรวน + ลมหายใจออกแปรปรวน", "Definition", G("Chapter 1 Definition of asthma") + [CLS + "อาจารย์แก้เรื่อง ratio"], BASE)],
    BASE + [DYS, COUGH])

# ═════════════════════════════════════════════ 2
sec("chest-ast-02", "พยาธิสรีรวิทยา — T2-high, T2-low และ airway remodeling",
    "dendritic cell → Th2 → IL-4/IL-5/IL-13 · IgE-mast cell (early phase) · eosinophil (late phase) · alarmin–ILC2 · remodeling", 11,
"""### การอักเสบแบบ T2 ทีละขั้น
1. **Sensitization** — dendritic cell ในเยื่อบุจับ allergen นำเสนอให้ naive T cell · **TSLP** ที่เซลล์เยื่อบุหลั่งช่วยดันให้กลายเป็น **Th2**
2. Th2 หลั่ง **IL-4** → B cell เปลี่ยนชนิดเป็น plasma cell สร้าง **IgE** → IgE ไปเกาะ FcεRI บน **mast cell**
3. **Early phase (นาที)** — สัมผัส allergen ซ้ำ จับ IgE บน mast cell → degranulation: **histamine, cysteinyl leukotriene (LTC4/D4/E4), PGD2, PAF** → กล้ามเนื้อเรียบหดตัว · หลอดเลือดขยายและรั่ว (บวม) · mucociliary clearance เสีย
4. **Late phase (4–8 ชั่วโมง)** — **IL-5** เรียกและยืดอายุ **eosinophil** ซึ่งหลั่ง **major basic protein** ทำลายเยื่อบุ · **IL-13** เพิ่ม goblet cell เมือกเหนียว และทำให้หลอดลม **ไวเกิน (airway hyperresponsiveness)**
5. **Remodeling** — อักเสบซ้ำนานปี: กล้ามเนื้อเรียบหนา (hypertrophy/hyperplasia) · collagen สะสมใต้ basement membrane · goblet cell metaplasia · หลอดเลือดใหม่ → lumen แคบถาวร

**อาจารย์เน้น**: "ที่ต้องจำคือ **IL-4, IL-5, IL-13**" · IgE อยู่ "ปลายทาง" — ปัจจุบันการคุมการอักเสบมุ่งที่ **ต้นทาง** มากกว่าบล็อก IgE อย่างเดียว

| ตัวกลาง | มาจาก | ทำอะไร | ยาที่ไปตัด |
|---|---|---|---|
| TSLP, IL-33, IL-25 (alarmin) | เยื่อบุที่ถูกไวรัส/มลพิษ/allergen กระทบ | ปลุก dendritic cell และ **ILC2** | tezepelumab (anti-TSLP) |
| IL-4 | Th2 | B cell สร้าง IgE · ดัน Th2 ต่อ | dupilumab (anti-IL-4Rα) |
| IL-5 | Th2, ILC2 | สร้าง เรียก ยืดอายุ eosinophil | mepolizumab, benralizumab |
| IL-13 | Th2, ILC2 | เมือก · AHR · กระตุ้น iNOS → **FeNO สูง** | dupilumab |
| IgE | plasma cell | ติด mast cell → degranulation | omalizumab |
| Histamine, CysLT, PGD2 | mast cell | หลอดลมหดเกร็ง บวม เมือก | SABA (แก้ผล) · montelukast (CysLT1) |

### สามเส้นทาง (แผนภาพที่อาจารย์ให้จด)
[[fig:endotype]]

- **Allergic eosinophilic** — allergen → Th2 → IL-4/5/13 + IgE
- **Non-allergic eosinophilic** — ไวรัส มลพิษ ควันบุหรี่ ทำร้ายเยื่อบุ → alarmin → **ILC2** หลั่ง IL-5/IL-13 โดยไม่ผ่าน allergen · ยังเป็น T2 (eosinophil เด่น) แต่ **IgE ไม่เด่น** · มักเริ่มวัยผู้ใหญ่ ร่วมกับ chronic rhinosinusitis/nasal polyp
- **T2-low** — ไม่ยุ่งกับ IL-4/5/13 แต่ไปทาง Th1/Th17 → **neutrophil** หรือไม่มีเซลล์อักเสบเด่น (paucigranulocytic) · **อาจารย์**: ใช้คำว่า "T2-low" ไม่ใช้ "non-T2" เพราะ T2 น้อยแต่ไม่ใช่ศูนย์
- **อาจารย์เน้น**: การอักเสบ "**เหมือนน้ำ**" — บล็อกทาง IgE มันจะวิ่งไปทาง IL-5 บล็อก IL-5 มันจะหาทาง IL-4 → คนไข้จริงจึงไม่แยกขาด 100%

### ทำไม T2 สำคัญในทางปฏิบัติ
- T2 ตอบสนอง **ICS** ดี — เหตุผลที่ ICS เป็นแกนกลางของการรักษาทุกขั้น
- ตัวบ่งชี้ T2: **blood eosinophil สูง · FeNO สูง · ภูมิแพ้ชัด** (หัวข้อ 5) และใช้เลือก biologic ใน severe asthma (หัวข้อ 13)
- T2-low ตอบสนองต่อ ICS น้อยกว่า และหา biomarker ไม่ได้ — ต้องคิดถึงการวินิจฉัยผิด/โรคร่วมก่อน""",
    ["IL-4 → IgE · IL-5 → eosinophil · IL-13 → เมือก AHR และ FeNO",
     "Early phase (นาที) = mast cell · late phase (4–8 ชม.) = eosinophil",
     "Non-allergic eosinophilic: ไวรัส/มลพิษ → alarmin (TSLP, IL-33) → ILC2 — T2 แต่ IgE ไม่เด่น",
     "T2-low ไม่ใช่ \"non-T2\" — neutrophilic/paucigranulocytic ตอบสนอง ICS น้อย",
     "อักเสบซ้ำโดยไม่ได้ ICS → remodeling → persistent airflow limitation"],
    [mcq(2, "A 46-year-old woman develops asthma for the first time. She has chronic rhinosinusitis with nasal polyps but no hay fever or eczema, and skin prick tests to common aeroallergens are negative. Blood eosinophils are 720 cells/µL. Which mechanism best explains her airway inflammation?",
         ["Epithelial alarmins activating group 2 innate lymphoid cells to release IL-5 and IL-13",
          "Allergen-specific IgE cross-linking on sensitised mast cells after each exposure",
          "Th1 and Th17 lymphocytes recruiting neutrophils into the bronchial wall",
          "Paucigranulocytic smooth muscle hyperresponsiveness without airway inflammation",
          "Immune complex deposition along the bronchial epithelial basement membrane"],
         "ภาพนี้คือ **non-allergic eosinophilic asthma** (adult-onset + nasal polyp + eosinophil สูง + ไม่มี sensitisation) — เยื่อบุที่ถูกไวรัส/มลพิษกระทบหลั่ง **alarmin (TSLP, IL-33, IL-25)** ปลุก **ILC2** ให้หลั่ง IL-5 (eosinophil) และ IL-13 (เมือก AHR) โดยไม่ต้องผ่าน allergen และ IgE · ยังเป็น **T2-high** จึงตอบสนอง ICS\n\n"
         "- \"IgE cross-linking บน mast cell\" — คือ allergic asthma แต่ skin test ลบ ไม่มี sensitisation\n"
         "- \"Th1/Th17 → neutrophil\" — T2-low ซึ่ง eosinophil ไม่ควรสูงขนาดนี้\n"
         "- \"paucigranulocytic\" — ไม่มีเซลล์อักเสบเด่น ขัดกับ eosinophil 720\n"
         "- \"immune complex\" — กลไก type III ไม่ใช่ของ asthma",
         "Adult-onset + polyp + eos สูง + ไม่แพ้อะไร = non-allergic eosinophilic (alarmin–ILC2)", "Endotype",
         G("Severe asthma guide — type 2 inflammation") + [CLS + "แผนภาพ T2-high/T2-low (Plaud highlight 11:06)"], BASE + [HYP, ANTIG]),
     mcq(3, "During a laboratory allergen challenge, a man with allergic asthma inhales cat allergen. His FEV1 falls by 30% within 15 minutes, recovers after an hour, and then falls again 6 hours later. Which cell is chiefly responsible for the second fall?",
         ["Eosinophil", "Mast cell", "Neutrophil", "Basophil", "Alveolar macrophage"],
         "นี่คือ **dual response**: ช่วงแรก (early phase, นาที) มาจาก **mast cell** ที่มี IgE หลั่ง histamine/leukotriene ทันที · ช่วงหลัง 4–8 ชั่วโมง (**late phase**) มาจากเซลล์อักเสบที่ถูกเรียกเข้ามา โดยเฉพาะ **eosinophil** (ผ่าน IL-5) ร่วมกับ Th2 — หลั่ง major basic protein, cysteinyl leukotriene ทำให้เยื่อบุบวม เมือกมาก หลอดลมไวเกิน · late phase ตอบสนองต่อ **corticosteroid** ไม่ใช่ SABA อย่างเดียว\n\n"
         "- \"Mast cell\" — ตัวหลักของ early phase (ช่วงแรก)\n- \"Neutrophil\" — เด่นใน T2-low และ exacerbation จากเชื้อบางชนิด ไม่ใช่ late phase ของ allergen\n"
         "- \"Basophil\" — มีบทบาทร่วมแต่ไม่ใช่ตัวหลัก\n- \"Alveolar macrophage\" — ไม่ใช่ effector หลักของ late phase",
         "Early phase = mast cell · late phase = eosinophil", "Early/late phase", ["ตำราอิมมูโนวิทยา — allergen challenge dual response"], BASE + [HYP])],
    BASE + [HYP, ANTIG],
    AN.FIGS["chest-ast-02"])

# ═════════════════════════════════════════════ 3
sec("chest-ast-03", "อาการเกิดได้อย่างไร — wheeze ไอกลางคืน silent chest และ pulsus paradoxus",
    "แรงต้านแปรผกผันกับ r⁴ · wheeze ตอนหายใจออก · circadian · V/Q mismatch · hyperinflation · silent chest = อันตราย", 9,
"""#### ทำไมถึงมีอาการนี้
| อาการ/อาการแสดง | กลไก | ใช้แยกโรคอย่างไร |
|---|---|---|
| **Wheeze ตอนหายใจออก** (หลายเสียง polyphonic ทั้งสองข้าง) | หายใจออก ความดันในช่องอกบวก กดหลอดลมที่แคบอยู่แล้ว → ลมเร็วผ่านช่องแคบ ผนังสั่น | wheeze เสียงเดียวที่เดิม = ก้อน/สิ่งแปลกปลอม · เสียงหายใจเข้าที่คอ (stridor) = ทางเดินหายใจส่วนบน |
| **ไอ** โดยเฉพาะกลางคืน · cough-variant | mediator กระตุ้น cough receptor · เมือกเหนียว · cough-variant ไอเด่นโดยไม่มีหลอดลมตีบชัด | ไอเดี่ยว ๆ ต้องแยก ACE inhibitor, postnasal drip, GERD, วัณโรค |
| **อาการกลางคืน/เช้ามืด** | จังหวะชีวภาพ: **cortisol และ adrenaline ต่ำสุดราวตี 4** · **vagal tone สูง** · หลอดลมเย็นลง · ไรฝุ่นที่นอน · นอนราบ | ต่างจาก PND ของหัวใจล้มเหลว (มี orthopnea ขาบวม JVP สูง crepitation) |
| **แน่นหน้าอก** | หายใจที่ปริมาตรปอดสูง (air trapping) กล้ามเนื้อหายใจทำงานหนัก | — |
| **หายใจออกยาว · ทรวงอกพอง** | ลมออกไม่ทันก่อนหายใจครั้งใหม่ → dynamic hyperinflation | COPD ก็มีได้ แต่ asthma กลับปกติระหว่าง attack |
| **SpO2 ต่ำ** | ถุงลมหลังหลอดลมตีบได้ลมน้อยแต่เลือดยังผ่าน (**low V/Q**) | แก้ด้วย O2 ไม่ยาก (ไม่ใช่ shunt) |
| **Pulsus paradoxus** > 10 mmHg | หายใจเข้าแรงมาก ความดันในช่องอกติดลบมาก → เลือดเข้าหัวใจขวามาก ผนังกั้นห้องดันหัวใจซ้าย + afterload ซ้ายเพิ่ม → SBP ตกตอนหายใจเข้า | บอกความรุนแรง · อาจหายไปเมื่อผู้ป่วยหมดแรง (ไม่ใช่ดีขึ้น) |
| **Silent chest** | ตีบมากจนลมแทบไม่ผ่าน → ไม่มีลมพอทำให้เกิดเสียง | **life-threatening** — wheeze ที่เบาลงพร้อมอาการแย่ลง = อันตราย |
| จมูก: เยื่อบุซีดบวม น้ำมูกใส · ผิวหนัง: eczema | atopy — \"united airway\": ผู้ป่วย asthma ส่วนใหญ่มี rhinitis ร่วม | สนับสนุน allergic phenotype |

> **ทำไมตีบนิดเดียวเหนื่อยมาก** — แรงต้านทานของท่อแปรผกผันกับ **รัศมียกกำลังสี่** (Poiseuille) · รัศมีลดลงครึ่งหนึ่ง แรงต้านเพิ่ม 16 เท่า

### ตัวกระตุ้นที่ต้องถาม
ไวรัส (rhinovirus, influenza, RSV) · allergen (ไรฝุ่น แมลงสาบ ขนสัตว์ เกสร สปอร์รา) · ควันบุหรี่และบุหรี่ไฟฟ้า · PM2.5 · อากาศเย็น/เปลี่ยนฤดู · ออกกำลัง · อารมณ์ หัวเราะ · ยา (**NSAID/aspirin, beta-blocker**) · สารในที่ทำงาน (occupational asthma — ดูคาบ 21 Image in chest หัวข้อ 18) · GERD · ใช้ยาควบคุมไม่สม่ำเสมอ""",
    ["Wheeze เกิดตอนหายใจออกเพราะความดันในช่องอกกดหลอดลมที่แคบอยู่แล้ว",
     "อาการกลางคืน: cortisol/adrenaline ต่ำสุดตอนเช้ามืด + vagal tone สูง",
     "Silent chest และ pulsus paradoxus ที่หายไปตอนผู้ป่วยหมดแรง = แย่ลง ไม่ใช่ดีขึ้น",
     "รัศมีหลอดลมลดครึ่ง → แรงต้าน × 16",
     "Hypoxemia ใน asthma มาจาก V/Q mismatch — แก้ด้วย O2 ได้ไม่ยาก"],
    [mcq(5, "A 23-year-old woman with asthma reports that her wheeze and cough are worst at about 4 a.m., often waking her from sleep. She has no orthopnoea or ankle swelling. Which mechanism best explains the timing of her symptoms?",
         ["Circadian fall in cortisol and adrenaline with a rise in vagal tone",
          "Supine posture causing pulmonary venous congestion and interstitial oedema",
          "Accumulation of carbon dioxide during REM sleep depressing ventilation",
          "Aspiration of gastric acid caused by obesity hypoventilation syndrome",
          "Loss of mucociliary clearance from obstructive sleep apnoea episodes"],
         "ในคนปกติ calibre ของหลอดลมแกว่งตามวันเล็กน้อย แต่ในผู้ป่วย asthma การแกว่งนี้ขยายมาก — **cortisol และ adrenaline ในเลือดต่ำสุดช่วงเช้ามืด** (การอักเสบและการหดตัวไม่ถูกต้าน) และ **vagal tone สูงตอนนอน** (acetylcholine ผ่าน M3 ทำให้หลอดลมหดตัว) + หลอดลมเย็นลง + allergen จากที่นอน → **airway calibre แคบที่สุดราวตี 4** · การตื่นกลางคืนจึงเป็นหนึ่งใน 4 คำถามของ symptom control\n\n"
         "- \"นอนราบ → pulmonary venous congestion\" — กลไกของ PND ในหัวใจล้มเหลว ซึ่งผู้ป่วยไม่มี orthopnea/ขาบวม\n"
         "- \"CO2 สะสมช่วง REM\" — ไม่ทำให้หลอดลมหดตัว และไม่ใช่สาเหตุของ wheeze\n"
         "- \"กรดไหลย้อนจาก obesity hypoventilation\" — GERD กระตุ้นได้ แต่โจทย์ไม่มีข้อมูลอ้วน/แสบร้อน และไม่อธิบายจังหวะเวลาที่สม่ำเสมอ\n"
         "- \"OSA\" — เป็นโรคร่วมที่ทำให้คุมยาก แต่ไม่ใช่กลไกหลักของอาการเช้ามืด",
         "Asthma แย่ตอนเช้ามืด = cortisol/adrenaline ต่ำสุด + vagal สูง", "Nocturnal asthma", ["ตำราสรีรวิทยา — circadian variation of airway calibre"], BASE + [MECH, AIRC])],
    BASE + [MECH, AIRC, GAS, DYS, COUGH, RHIN])

# ═════════════════════════════════════════════ 4
sec("chest-ast-04", "วินิจฉัย — spirometry, PEF diary, challenge test และ ICS trial",
    "ก่อน–หลัง salbutamol: > 12% และ > 200 mL (FEV1 หรือ FVC) · ไม่มีเกณฑ์ ratio · PEF variability · methacholine · exercise · ICS 4 สัปดาห์", 13,
"""### หลักการ
**วินิจฉัย = อาการแปรปรวน + หลักฐาน variable expiratory airflow limitation** · ตรวจก่อนเริ่ม ICS ถ้าทำได้ (หลังเริ่ม ICS ผลมักเป็นลบ) · งด SABA ≥ 4 ชม. และ LABA 24–48 ชม. ก่อนตรวจ (GINA)

### Spirometry และ bronchodilator responsiveness
- เป่า spirometry → พ่น **salbutamol 200–400 mcg (2–4 puffs)** → รอ **10–15 นาที** → เป่าซ้ำ
- คำนวณ: **% ที่เพิ่ม = (หลัง − ก่อน) ÷ ก่อน × 100**
- **บวก (ผู้ใหญ่)** = FEV1 (หรือ FVC) เพิ่ม **> 12% และ > 200 mL** จากค่าก่อนยา

**อาจารย์เน้น (ใช้เวลาในคาบนานที่สุด)**
- ต้องผ่าน **ทั้งสองข้อ** — 12% อย่างเดียวหรือ 200 mL อย่างเดียวไม่พอ
- ดูได้ทั้ง **FEV1 หรือ FVC**
- **ไม่ต้องดู FEV1/FVC** — "ratio จะ 80 จะ 90 จะ 100% ก็ต้องทำซ้ำ" · ratio < 0.70 ใช้บอกว่ามี obstruction (เกณฑ์ COPD) ไม่ใช่เกณฑ์ของ asthma
- ผลบวกสนับสนุน asthma แต่ **ใช้แยก asthma กับ COPD ไม่ได้แน่นอน** (COPD ก็ตอบสนองต่อยาได้ — คาบ 37 หัวข้อ 6)

### ถ้ายังไม่ยืนยัน — ทำอะไรต่อ
| วิธี | ทำอย่างไร | ผลบวก |
|---|---|---|
| ตรวจซ้ำตอนมีอาการ | อาจารย์: "ติดตามและลองทำซ้ำ มันอาจ positive ทีหลัง" | เกณฑ์เดิม |
| **PEF ก่อน–หลังยา** | เหมือน spirometry แต่ใช้ peak flow meter | PEF เพิ่ม **> 20%** |
| **PEF diary** | เป่าเช้า–เย็น 1–2 สัปดาห์ | GINA: ค่าเฉลี่ย diurnal variability **> 10%** (เด็ก > 13%) · ERS 2022 และ BTS/NICE ใช้ **≥ 20%** |
| **ICS trial 4 สัปดาห์** | ให้ ICS แล้ววัดซ้ำ | FEV1 > 12% และ > 200 mL หรือ PEF > 20% |
| **Methacholine/histamine challenge** | สูดสารกระตุ้นขนาดเพิ่มทีละขั้น | FEV1 ลด **≥ 20%** ที่ขนาดต่ำ (คนปกติต้องใช้ขนาดสูง — คน asthma \"ไวเกิน\") |
| **Exercise challenge** | วิ่ง/ปั่น 6–8 นาที แล้ววัดซ้ำ | FEV1 ลด **> 10% และ > 200 mL** — อาจารย์: "exercise ใช้แค่ 10% ตัวเลขไม่เหมือนอันอื่น" |
| ระหว่าง visit | FEV1 แปรปรวนระหว่างนัด | > 12% และ > 200 mL (นอกช่วงติดเชื้อ) |

[[fig:pefvar]]

> **ผลลบไม่ได้ตัดโรค** โดยเฉพาะถ้าตรวจตอนไม่มีอาการหรือได้ ICS มาแล้ว · challenge test ที่ **ลบ** ช่วยตัด asthma ได้ดี (negative predictive value สูง) ในคนที่ไม่ได้ใช้ ICS

### Spirometry ทำไม่ได้ (เช่น รพ.ชุมชน)
ใช้ PEF แทนได้ · ถ้าอาการชัดและไม่มีเครื่องเลย GINA ให้เริ่ม ICS-containing treatment และ **บันทึกเหตุผล** แล้วยืนยันภายหลัง — อย่าเริ่มด้วย SABA เดี่ยว""",
    ["BD responsiveness ผู้ใหญ่: FEV1 หรือ FVC เพิ่ม > 12% และ > 200 mL — ต้องทั้งคู่",
     "อาจารย์: asthma ไม่มีเกณฑ์ FEV1/FVC < 0.70 — ratio เป็นเรื่อง obstruction/COPD",
     "PEF ก่อน–หลังยา > 20% · PEF diary: GINA > 10% · ERS 2022/BTS-NICE ≥ 20% — บอกที่มาของเกณฑ์เสมอ",
     "Exercise challenge ใช้ FEV1 ลด > 10% (และ > 200 mL) · methacholine ใช้ลด ≥ 20%",
     "ผลลบครั้งแรกไม่ตัดโรค — ตรวจซ้ำตอนมีอาการ หรือทำ challenge/ICS trial"],
    [mcq(7, "A 28-year-old man has episodic wheeze. Spirometry before and 15 minutes after 400 µg of inhaled salbutamol shows: FEV1 2.10 L → 2.40 L; FVC 3.60 L → 3.70 L; FEV1/FVC 0.58 → 0.65. Which interpretation is correct?",
         ["Positive — FEV1 rose by 300 mL and 14%",
          "Negative — FEV1 rose by under 15%",
          "Negative — FVC rose by only 100 mL",
          "Positive — FEV1/FVC rose by 0.07",
          "Indeterminate — FEV1/FVC is still below 0.70"],
         "คำนวณ: FEV1 เพิ่ม **2.40 − 2.10 = 0.30 L = 300 mL** · **0.30 ÷ 2.10 × 100 = 14.3%** → เกิน **12% และ 200 mL** ทั้งคู่ = **bronchodilator responsiveness บวก** สนับสนุน asthma (กล้ามเนื้อเรียบที่หดตัวคลายด้วย β2 agonist ทำให้ลมไหลเร็วขึ้น)\n\n"
         "- \"น้อยกว่า 15%\" — เกณฑ์คือ 12% ไม่ใช่ 15%\n"
         "- \"FVC เพิ่มแค่ 100 mL\" — ใช้ FEV1 **หรือ** FVC ข้อใดข้อหนึ่งผ่านก็พอ\n"
         "- \"ratio เพิ่ม 0.07\" — การเปลี่ยนของ ratio ไม่ใช่เกณฑ์\n"
         "- \"ratio ยัง < 0.70 จึงสรุปไม่ได้\" — **อาจารย์เน้น** ว่า ratio ไม่เกี่ยวกับการวินิจฉัย asthma",
         "(หลัง − ก่อน) ÷ ก่อน × 100 · > 12% และ > 200 mL", "BD responsiveness", G("Box 1-2 Diagnostic criteria") + [CLS + "อาจารย์สอนสูตรและย้ำเรื่อง ratio"], BASE + [SPIRO, SPIROB, BD]),
     mcq(8, "A woman keeps a twice-daily peak flow diary. On one typical day her morning PEF is 340 L/min and her evening PEF is 400 L/min. Using the GINA method, what is the diurnal variability for that day?",
         ["16%", "15%", "18%", "8%", "60%"],
         "GINA: **diurnal variability = (ค่าสูงสุดของวัน − ค่าต่ำสุดของวัน) ÷ ค่าเฉลี่ยของสองค่านั้น × 100** → (400 − 340) ÷ 370 × 100 = **16.2%** · นำค่ารายวันมาเฉลี่ย 1–2 สัปดาห์ ถ้า **> 10%** (ผู้ใหญ่) = แปรปรวนเกิน (ERS 2022 และ BTS/NICE ใช้ ≥ 20%) · ค่าเช้าต่ำกว่าเย็นเพราะหลอดลมแคบที่สุดช่วงเช้ามืด\n\n"
         "- \"15%\" — หารด้วยค่าสูงสุด (60 ÷ 400)\n- \"18%\" — หารด้วยค่าต่ำสุด (60 ÷ 340)\n"
         "- \"8%\" — หารด้วยผลรวม (60 ÷ 740) แทนค่าเฉลี่ย\n- \"60%\" — เอาผลต่าง L/min มาตอบเป็นเปอร์เซ็นต์",
         "Diurnal PEF variability = (สูง − ต่ำ) ÷ เฉลี่ย × 100", "PEF variability", G("Box 1-2 — excessive variability in twice-daily PEF"), BASE + [SPIRO, SPIROB], keep=True),
     mcq(9, "A 30-year-old teacher has had intermittent cough and wheeze for a year, worse with colds. Today she is symptom-free; her chest is clear and spirometry is normal with no bronchodilator responsiveness. She is not using any inhaler. What is the most appropriate next step?",
         ["Repeat spirometry when symptomatic or keep a PEF diary",
          "Exclude asthma because bronchodilator testing was negative",
          "Start regular salbutamol and review in three months",
          "Request high-resolution CT of the chest before any other test",
          "Measure total IgE to confirm or refute allergic asthma"],
         "Asthma เป็นโรค **แปรปรวน** — ตรวจตอนไม่มีอาการ หลอดลมอาจปกติ ผลจึงลบได้ · ขั้นต่อไปตาม GINA (และที่อาจารย์วงไว้): **ตรวจซ้ำตอนมีอาการ** หรือ **PEF เช้า–เย็น 1–2 สัปดาห์** · ถ้ายังไม่ได้ → bronchial challenge (methacholine/exercise) หรือ ICS trial\n\n"
         "- \"ตัด asthma\" — ผลลบครั้งเดียวไม่ตัดโรค\n"
         "- \"salbutamol ประจำ\" — **ไม่แนะนำ SABA เดี่ยว** (หัวข้อ 6) และยังไม่ได้วินิจฉัย\n"
         "- \"HRCT ก่อน\" — ใช้เมื่อสงสัยโรคอื่น (bronchiectasis, ILD) ไม่ใช่ขั้นแรก\n"
         "- \"total IgE\" — บอกภูมิแพ้ ไม่ยืนยันหรือตัด asthma (หัวข้อ 5)",
         "ผลปกติตอนไม่มีอาการ → ตรวจซ้ำตอนมีอาการ / PEF diary", "Diagnostic pathway", G("Box 1-1 Diagnostic flowchart") + [CLS + "ขั้นตอนเมื่อผลยังไม่ยืนยัน"], BASE + [SPIRO])],
    BASE + [SPIRO, SPIROB, BD, MECH],
    AN.FIGS["chest-ast-04"])

# ═════════════════════════════════════════════ 5
sec("chest-ast-05", "Biomarker และการวินิจฉัยแยกโรค — FeNO, eosinophil, IgE และโรคที่เลียนแบบ asthma",
    "FeNO/eos สูง = \"น่าจะ\" ไม่ใช่ยืนยัน · IgE/skin test บอกแค่ภูมิแพ้ · แยกตามอายุ · COPD (อ้างอิงคาบ 37) · ILO · HF · TB · ACE inhibitor", 9,
"""### Biomarker — อาจารย์ให้แปลว่า \"น่าจะ\" ไม่ใช่ \"ยืนยัน\"
| การตรวจ | บอกอะไร | ข้อควรระวัง |
|---|---|---|
| **FeNO** (เป่าวัด nitric oxide) | IL-13 กระตุ้น iNOS ในเยื่อบุ → **eosinophilic (T2) inflammation** · ผู้ใหญ่ > 50 ppb = สูง · < 25 ppb = ต่ำ (ATS 2011) | ลดลงหลังใช้ ICS และในคนสูบบุหรี่ · สูงได้ใน allergic rhinitis |
| **Blood eosinophil** | ≥ 300 cells/µL สนับสนุน T2 | อาจารย์: **พยาธิ** ก็ทำให้ eos สูง · ลดลงหลังใช้ steroid |
| **Specific IgE / skin prick test** | ภาวะไวต่อสารก่อภูมิแพ้ (sensitisation) | บวกไม่ได้แปลว่าเป็น allergic asthma · ลบไม่ได้ตัด asthma ชนิดอื่น |
| **CXR** | ปกติใน asthma ส่วนใหญ่ | ใช้ **หาโรคอื่น** (pneumothorax, pneumonia, หัวใจโต) ไม่ใช่วินิจฉัย asthma |

**อาจารย์เน้น**: อาการเข้าได้ + eos/FeNO สูง → "**น่าจะ**เป็น asthma" (ยังต้องยืนยัน airflow) · อาการเข้าได้แต่ eos/FeNO ปกติ → ถ้าเป็นต้องเป็น non-eosinophilic ซึ่งพบน้อย → "**ไม่น่าจะ**" แต่ **ไม่ได้ exclude**

### แยกโรคตามอายุ (ที่นำเสนอในคาบ — GINA)
| อายุ | คิดถึง |
|---|---|
| 6–11 ปี | สิ่งแปลกปลอม (inhaled foreign body) · โรคแต่กำเนิด · bronchiectasis · primary ciliary dyskinesia |
| 12–39 ปี | chronic upper airway cough syndrome · **inducible laryngeal obstruction (vocal cord dysfunction)** · hyperventilation/dysfunctional breathing · bronchiectasis · alpha-1 antitrypsin deficiency |
| ≥ 40 ปี | ข้างบน + **COPD** · **heart failure** · ไอจาก **ACE inhibitor** · lung cancer · pulmonary embolism · ILD |
| ทุกอายุ | **วัณโรค** (ไอเรื้อรัง ไอเป็นเลือด ไข้ เหงื่อออกกลางคืน น้ำหนักลด) · central airway obstruction (stridor) |

### แยกจาก COPD
- ตารางเทียบเต็มอยู่ใน **คาบ 37 COPD หัวข้อ 6** (ภาพ asthma vs COPD) — ไม่ซ้ำที่นี่
- **อาจารย์**: COPD ก็มี wheeze มีหลอดลมตีบ ถูกกระตุ้นด้วยมลพิษ อุณหภูมิ การติดเชื้อได้ แต่ allergen ไม่ค่อยเป็นตัวกระตุ้น · ใช้ **อายุ + ประวัติสูบบุหรี่** และ **เสมหะเรื้อรัง (chronic sputum production) ซึ่งเป็นลักษณะเด่นของ COPD** — asthma ไม่มีเสมหะเด่น
- **BD reversibility และ eosinophil แยกสองโรคไม่ได้แน่นอน** · obstruction ที่ไม่กลับคืนเต็มที่ก็ **ไม่จำเพาะกับ COPD** (asthma ที่ remodeling แล้วก็เป็นได้)
- GOLD 2026 **ไม่ใช้คำว่า "asthma–COPD overlap"** — ถ้ามี **asthma และ COPD ร่วมกัน** ให้รักษาตามแนวทาง asthma: **ต้องมี ICS เสมอ ห้าม LABA หรือ LAMA เดี่ยว**

### โรคที่มาเหมือน "หอบหืดที่ไม่ตอบสนองต่อยา"
- **Inducible laryngeal obstruction** — เสียงหวีดช่วง **หายใจเข้า** ที่คอ แน่นคอ เสียงเปลี่ยน · เกิด-หายเร็ว · SpO2 มักปกติ · ไม่ตอบสนอง salbutamol · flow-volume loop ช่วงหายใจเข้าแบนระหว่างมีอาการ · ยืนยันด้วยส่องกล่องเสียงขณะมีอาการ
- **Heart failure (cardiac asthma)** — orthopnea, PND, ขาบวม, JVP สูง, crepitation, S3, หัวใจโต · NT-proBNP สูง
- **ACE inhibitor** — ไอแห้งจาก bradykinin สะสม · หายภายในสัปดาห์–เดือนหลังหยุดยา
- **Occupational asthma** — อาการดีขึ้นวันหยุด · ดูคาบ 21 หัวข้อ 18""",
    ["FeNO/eos สูง = สนับสนุน T2 (\"น่าจะ\") ไม่ใช่ยืนยัน · ปกติก็ไม่ได้ exclude",
     "IgE/skin test บอกแค่ sensitisation · CXR ใช้หาโรคอื่น",
     "COPD: อายุ > 40 · สูบบุหรี่ · เสมหะเรื้อรังเด่น · reversibility/eos แยกสองโรคไม่ได้แน่นอน",
     "ไม่มีคำว่า ACO ใน GOLD 2026 — มี asthma ร่วมด้วยต้องได้ ICS",
     "หวีดตอนหายใจเข้า + ไม่ตอบสนอง salbutamol + SpO2 ปกติ = inducible laryngeal obstruction"],
    [mcq(10, "A 34-year-old man has 6 months of episodic wheeze and night cough. Spirometry today is normal. FeNO is 62 ppb and blood eosinophils are 480 cells/µL; he has no travel history. How should these biomarker results be interpreted?",
         ["They support type 2 airway inflammation likely to respond to ICS",
          "They confirm asthma, so lung function testing is no longer needed",
          "They indicate neutrophilic asthma that will need a macrolide",
          "They exclude COPD because COPD never causes eosinophilia",
          "They suggest heart failure with congestion of the bronchial wall"],
         "FeNO มาจาก **IL-13 กระตุ้น iNOS ในเยื่อบุหลอดลม** และ eosinophil มาจาก **IL-5** — ทั้งสองค่าสูงบ่งว่ามี **T2 (eosinophilic) inflammation** ซึ่งตอบสนอง **ICS** ดี · อาจารย์ให้แปลว่า \"**น่าจะ**\" เป็น asthma ยังต้องหาหลักฐาน variable airflow (ตรวจซ้ำตอนมีอาการ/PEF diary/challenge)\n\n"
         "- \"ยืนยัน asthma ไม่ต้องตรวจปอด\" — biomarker ไม่ใช่เกณฑ์วินิจฉัย (rhinitis, eosinophilic bronchitis ก็ FeNO สูงได้)\n"
         "- \"neutrophilic\" — ตรงข้าม ค่าที่สูงคือ eosinophilic\n"
         "- \"ตัด COPD\" — COPD บางรายมี eos สูงได้ (เป็นตัวเลือกใช้ ICS ใน COPD)\n"
         "- \"heart failure\" — ไม่ทำให้ FeNO/eos สูง",
         "FeNO/eos สูง = T2 → ICS ได้ผล แต่ยังต้องยืนยัน airflow", "FeNO", G("Box 1-2, Chapter 3 — FeNO") + [CLS + "อาจารย์: \"น่าจะ\" ไม่ใช่ \"ยืนยัน\""], BASE + [SPIRO]),
     mcq(11, "A 26-year-old nurse has repeated emergency visits for 'asthma attacks' with throat tightness, voice change and a noisy breath heard loudest over the neck during inspiration. SpO2 stays at 98%, salbutamol gives no relief, and a flow–volume loop recorded during an episode shows a flattened inspiratory limb. What is the most likely diagnosis?",
         ["Inducible laryngeal obstruction", "Life-threatening asthma", "Allergic bronchopulmonary aspergillosis",
          "Exercise-induced bronchoconstriction", "Eosinophilic granulomatosis with polyangiitis"],
         "เสียงหวีดช่วง **หายใจเข้า** ดังที่คอ + เสียงเปลี่ยน + **SpO2 ปกติ** + **ไม่ตอบสนองต่อ β2 agonist** + **inspiratory limb แบน** = ทางเดินหายใจส่วนบนที่อยู่นอกช่องอกตีบ (สายเสียงหุบเข้าหากันผิดจังหวะตอนหายใจเข้า) = **inducible laryngeal obstruction** (vocal cord dysfunction) · ยืนยันด้วยการส่องกล่องเสียงขณะมีอาการ · รักษาด้วยการฝึกหายใจ/speech therapy ไม่ใช่เพิ่ม steroid\n\n"
         "- \"life-threatening asthma\" — ต้องมี SpO2 ต่ำ หรือ silent chest และ wheeze ตอนหายใจออก ไม่ใช่ inspiratory noise\n"
         "- \"ABPA\" — asthma + IgE สูงมาก + bronchiectasis/ปอดเป็นหย่อม ๆ ไม่ใช่อาการที่คอ\n"
         "- \"exercise-induced bronchoconstriction\" — หลอดลมส่วนล่างตีบหลังออกกำลัง ตอบสนองต่อ SABA และ expiratory limb ผิดปกติ\n"
         "- \"EGPA\" — asthma + eos สูง + vasculitis (เส้นประสาท ผิวหนัง ไต) ไม่ใช่ภาพนี้",
         "Inspiratory noise + SpO2 ปกติ + ไม่ตอบสนอง salbutamol = ILO", "Differential diagnosis", G("Box 1-3 Differential diagnosis by age"), BASE + [DYS])],
    BASE + [SPIRO, DYS, COUGH, RHIN, HYP])

# ═════════════════════════════════════════════ 6
sec("chest-ast-06", "ยา — controller, reliever, add-on: กลไกและผลข้างเคียง",
    "ICS = แกนกลาง · SABA/formoterol/salmeterol · ห้าม SABA เดี่ยว ห้าม LABA เดี่ยว · LAMA · LTRA · OCS · ขนาด ICS ต่ำ/กลาง/สูง", 11,
"""### 3 กลุ่มยา (ที่นำเสนอในคาบ)
- **Controller** — ใช้ต่อเนื่อง ต้องมี **ICS** เพื่อลดการอักเสบ อาการ และความเสี่ยง (exacerbation, lung function ลด)
- **Reliever** — ใช้เมื่อมีอาการ: **ICS-formoterol** (แนะนำ) · ICS-SABA · SABA
- **Add-on** — สำหรับ difficult-to-treat/severe asthma: LAMA · biologic · (LTRA)

| ยา | กลไก | ใช้เมื่อ | ผลข้างเคียงที่ต้องรู้ |
|---|---|---|---|
| **ICS** — budesonide, beclometasone, fluticasone, ciclesonide | จับ glucocorticoid receptor → ปิดยีนอักเสบ (ยับยั้ง NF-κB/AP-1) → cytokine Th2 ลด · eosinophil ตาย · mast cell ในเยื่อบุลด · **เพิ่มจำนวน β2 receptor** | ทุกขั้น ทุกคน | เฉพาะที่: **เชื้อราในปาก เสียงแหบ** (บ้วนปาก ใช้ spacer) · ขนาดสูงนาน: กระดูกพรุน ต้อกระจก adrenal suppression |
| **SABA** — salbutamol | β2 → Gs → **cAMP ↑** → PKA → myosin light chain kinase ทำงานลด + Ca2+ ในเซลล์ลด → กล้ามเนื้อเรียบคลาย ใน 5 นาที อยู่ 4–6 ชม. | reliever (Track 2) · acute attack | มือสั่น ใจสั่น tachycardia · **hypokalemia** (Na-K-ATPase ดึง K เข้าเซลล์) · hyperglycemia · lactic acidosis |
| **Formoterol** (LABA เร็ว) | β2 agonist ชอบไขมัน เข้าเยื่อหุ้มเซลล์เร็วและค้างนาน → **ออกฤทธิ์ 1–3 นาที อยู่ ~12 ชม.** | ICS-formoterol: AIR/MART (Track 1) | เหมือน SABA · สูงสุด 72 mcg/วัน (12 สูดของ 200/6) |
| **Salmeterol** (LABA ช้า) | ออกฤทธิ์ 10–20 นาที อยู่ 12 ชม. | ICS-salmeterol เป็น controller (Track 2) — **ใช้บรรเทาอาการไม่ได้** | — |
| **SAMA/LAMA** — ipratropium / tiotropium | ต้าน **M3** → ลดการหดตัวจาก vagal tone และเมือก | ipratropium: exacerbation รุนแรง · tiotropium: add-on step 5 | ปากแห้ง ปัสสาวะคั่ง ระวัง glaucoma มุมปิด |
| **LTRA** — montelukast | ต้าน CysLT1 receptor | ทางเลือกที่ได้ผลน้อยกว่า ICS · AERD · EIB | **คำเตือน neuropsychiatric** (ฝันร้าย ซึมเศร้า คิดฆ่าตัวตาย — US FDA boxed warning 2020) |
| **OCS** — prednisolone | เหมือน ICS แต่ทั้งตัว | exacerbation 5–7 วัน · step 5 เมื่อจำเป็นที่สุด | สะสม: เบาหวาน กระดูกพรุน ต้อ ติดเชื้อ · แม้เป็นคอร์สสั้น ๆ รวมกัน 4–5 คอร์สก็เพิ่มความเสี่ยง |
| Theophylline | ยับยั้ง phosphodiesterase | **ไม่แนะนำ** แล้ว | ช่วงรักษาแคบ ชัก arrhythmia ปฏิกิริยากับยามาก |

### ห้าม SABA เดี่ยว — อาจารย์เน้นมาก
- "การสั่ง beta-2 แล้วให้คนไข้พ่นบ่อย ๆ **เป็นการรักษาที่ผิด**" — salbutamol แค่ **ปิดบังอาการ** การอักเสบยังอยู่และเพิ่มขึ้นเรื่อย ๆ "สุดท้ายคนไข้ก็จะตาย"
- พ่นซ้ำ dose ที่ 3–4 เริ่มไม่ได้ผลแต่ผู้ป่วยยิ่งพ่น → "**ไม่ตายจาก asthma ก็อาจตายจาก cardiac**" (tachyarrhythmia, hypokalemia)
- ใช้ SABA บ่อยยังทำให้ **β2 receptor ลดจำนวน (downregulation)** ตอบสนองยาแย่ลง
- ข้อมูลประกอบ: ใช้ SABA **≥ 3 กระบอก/ปี** เพิ่มความเสี่ยง exacerbation รุนแรง · **≥ 12 กระบอก/ปี** เพิ่มความเสี่ยงตาย (GINA) · ในคาบ: **> 1 กระบอก/เดือน** หรือพ่น nebulized SABA ประจำ = ธงแดง
- → ทุกครั้งที่หอบต้องได้ **ICS คู่เสมอ** (หัวข้อ 7)

### ห้าม LABA เดี่ยว
LABA คลายกล้ามเนื้อนาน ทำให้ผู้ป่วยรู้สึกดีขึ้นทั้งที่การอักเสบยังเดินหน้า → exacerbation รุนแรงและ **การตายเพิ่ม** (การศึกษา SMART ของ salmeterol) → LABA ต้องอยู่ในหลอดเดียวกับ ICS เสมอ (ข้อนี้ใช้กับคนที่มี asthma ร่วมกับ COPD ด้วย)

### formoterol ต่างจาก salmeterol อย่างไร
[[fig:formo]]

### ขนาด ICS ต่อวันในผู้ใหญ่ (GINA)
| ยา | ต่ำ | กลาง | สูง |
|---|---|---|---|
| Budesonide (DPI) | 200–400 mcg | > 400–800 | > 800 |
| Fluticasone propionate (DPI/pMDI) | 100–250 | > 250–500 | > 500 |
| Beclometasone dipropionate (pMDI อนุภาคมาตรฐาน) | 200–500 | > 500–1000 | > 1000 |

- ประโยชน์ส่วนใหญ่ได้ตั้งแต่ **ขนาดต่ำ** (dose–response แบน) แต่ผลข้างเคียงเพิ่มตามขนาด · **อาจารย์เน้น**: ขนาดสูงสงวนไว้ที่ step 5 เท่านั้น
- ICS + **ยายับยั้ง CYP3A4** (ritonavir, ketoconazole, itraconazole) → ระดับ steroid สูง เกิด Cushing/adrenal suppression ได้ (ที่นำเสนอในคาบ)""",
    ["ICS คือแกนกลางทุกขั้น — ลดการอักเสบ และเพิ่ม β2 receptor",
     "อาจารย์: SABA เดี่ยวซ้ำ ๆ = รักษาผิด ปิดบังอาการ ตายจาก asthma หรือ cardiac",
     "LABA เดี่ยวเพิ่มการตาย — ต้องอยู่หลอดเดียวกับ ICS เสมอ",
     "Formoterol เร็ว (1–3 นาที) + นาน จึงเป็นทั้ง controller และ reliever · salmeterol ช้า ใช้บรรเทาไม่ได้",
     "SABA ทำ hypokalemia ผ่าน Na-K-ATPase · montelukast มีคำเตือน neuropsychiatric"],
    [mcq(13, "A patient asks why her new budesonide–formoterol inhaler can be used for sudden symptoms, whereas her previous fluticasone–salmeterol inhaler could not. Which property of formoterol explains this?",
         ["Its onset of bronchodilation occurs within a few minutes",
          "Its duration of action is far longer than that of salmeterol",
          "Its selectivity for β2 receptors is higher than salbutamol",
          "Its own anti-inflammatory effect suppresses airway eosinophils",
          "Its use does not cause tachycardia or a fall in potassium"],
         "formoterol เป็น LABA ที่ชอบไขมันปานกลาง เข้าถึง β2 receptor ได้ทันทีและค้างในเยื่อหุ้มเซลล์ → **เริ่มออกฤทธิ์ใน 1–3 นาที** (เร็วพอ ๆ กับ salbutamol) และอยู่ราว 12 ชม. · จึงใช้เป็น **reliever** ได้ และเมื่ออยู่หลอดเดียวกับ ICS ผู้ป่วยได้ยาต้านการอักเสบทุกครั้งที่พ่นบรรเทาอาการ (AIR/MART) · **อาจารย์**: \"LABA ใน Track 1 บังคับต้องเป็น formoterol\"\n\n"
         "- \"นานกว่า salmeterol มาก\" — ทั้งคู่อยู่ราว 12 ชม. เท่ากัน\n"
         "- \"β2 selective กว่า salbutamol\" — ไม่ใช่เหตุผลของการใช้เป็น reliever\n"
         "- \"ต้านการอักเสบเอง\" — β2 agonist ไม่ลดการอักเสบ ฤทธิ์ต้านการอักเสบมาจาก budesonide\n"
         "- \"ไม่ทำใจสั่น K ต่ำ\" — formoterol ก็มีผลข้างเคียงของ β2 agonist เหมือนกัน",
         "Formoterol = เร็ว + นาน → MART/AIR · salmeterol ช้า", "Formoterol", G("Chapter 4 — ICS-formoterol reliever") + [CLS + "อาจารย์: Track 1 ต้องเป็น formoterol"], BASE + [BD]),
     mcq(14, "A 38-year-old man with asthma has been prescribed salmeterol 50 µg twice daily on its own by another clinic, with salbutamol as needed. He still wakes at night twice a week. What is the most appropriate change?",
         ["Switch to budesonide–formoterol maintenance and reliever",
          "Continue salmeterol and add montelukast at bedtime",
          "Replace salmeterol with tiotropium given once daily",
          "Add oral theophylline to the salmeterol twice daily",
          "Stop salmeterol and use salbutamol only when needed"],
         "**LABA เดี่ยวโดยไม่มี ICS ห้ามใช้ใน asthma** — คลายกล้ามเนื้อนานจนผู้ป่วยไม่รู้ตัวว่าการอักเสบกำลังแย่ลง → exacerbation รุนแรงและการตายเพิ่ม · ผู้ป่วยตื่นกลางคืน 2 ครั้ง/สัปดาห์ = คุมไม่ได้ → เปลี่ยนเป็นยาที่มี **ICS** ทันที — ทางที่แนะนำคือ **budesonide-formoterol MART** (Track 1 step 3)\n\n"
         "- \"salmeterol + montelukast\" — ยังไม่มี ICS ความเสี่ยงเดิมไม่หายไป\n"
         "- \"tiotropium แทน\" — LAMA เดี่ยวใน asthma ก็ไม่มี ICS ใช้เป็น add-on step 5 เท่านั้น\n"
         "- \"เพิ่ม theophylline\" — ไม่แนะนำ ผลข้างเคียงมากและยังไม่มี ICS\n"
         "- \"SABA อย่างเดียว\" — **อาจารย์เน้น** ว่าเป็นการรักษาที่ผิด เสี่ยงตาย",
         "Asthma ทุกคนต้องมี ICS — ห้าม LABA เดี่ยว ห้าม SABA เดี่ยว", "LABA monotherapy", G("Chapter 4 — LABA safety"), BASE + [BD, ICS, ADR]),
     mcq(15, "A 25-year-old woman with acute asthma receives continuous nebulised salbutamol for 2 hours. She develops a fine tremor, and a repeat potassium is 2.9 mmol/L (initially 4.0). What is the mechanism of the fall in potassium?",
         ["β2 stimulation of Na-K-ATPase shifting potassium into cells",
          "Aldosterone excess causing renal potassium wasting in urine",
          "Gastrointestinal potassium loss from drug-induced diarrhoea",
          "Dilution from the intravenous fluid given with the nebuliser",
          "Magnesium deficiency causing potassium loss in distal tubules"],
         "β2 agonist กระตุ้น β2 receptor บนเซลล์กล้ามเนื้อลาย → cAMP → **Na-K-ATPase ทำงานมากขึ้น** → K เคลื่อนจากเลือดเข้าเซลล์ (transcellular shift) ไม่ใช่สูญเสียออกนอกร่างกาย · พ่นต่อเนื่องขนาดสูงจึงต้องติดตาม K (และน้ำตาล lactate) · กลไกเดียวกับที่ใช้ salbutamol รักษา hyperkalemia\n\n"
         "- \"aldosterone\" — ไม่มีเหตุให้ aldosterone สูงในเวลา 2 ชม.\n- \"ท้องเสีย\" — ไม่ใช่ผลของยาพ่น\n"
         "- \"เจือจางจากน้ำเกลือ\" — nebuliser ไม่ได้ให้น้ำเกลือเข้าหลอดเลือด และเจือจางไม่ทำให้ K ลดเกือบ 30%\n"
         "- \"ขาด magnesium\" — ทำให้ K ต่ำดื้อต่อการแก้ได้ แต่ไม่ใช่สาเหตุที่เกิดเฉียบพลันจาก salbutamol",
         "SABA ขนาดสูง → K เข้าเซลล์ → hypokalemia · ติดตาม K", "SABA adverse effects", ["ตำราเภสัชวิทยา — β2 agonist and potassium"], BASE + [BD, ADR])],
    BASE + [BD, ICS, LTRA, CORT, IMMOD, ADR],
    AN.FIGS["chest-ast-06"])

# ═════════════════════════════════════════════ 7
sec("chest-ast-07", "GINA Track 1 / Track 2 — เลือกขั้นเริ่มต้น และสอน MART",
    "Track 1 (preferred): ICS-formoterol ทุกขั้น · step 1–2 AIR · step 3 MART ต่ำ · step 4 MART กลาง · step 5 add-on · Track 2 ในไทยต้องใช้ 3 หลอด", 12,
"""### Track 1 — ทางที่แนะนำ
**อาจารย์เน้น (Plaud highlight 49:38 และ 52:02 — สองแผนผังที่อาจารย์ให้จด)**
- ใช้ **ICS-formoterol หลอดเดียว** ตลอดบันได — ICS จะเป็นตัวไหนก็ได้ แต่ **LABA ต้องเป็น formoterol** เพราะออกฤทธิ์เร็ว
- "**ทุกครั้งที่คนไข้หอบ ต้องได้ ICS low dose คู่เสมอ**" → ไม่เรียกว่า reliever เฉย ๆ แต่เรียก **AIR (anti-inflammatory reliever)**
- step 3–4 ใช้หลอดเดียวกันเป็นทั้งยาเช้า–เย็นและยาเวลามีอาการ = **MART** (maintenance and reliever therapy)
- เหตุผลที่ Track 1 preferred: **หลอดเดียวง่ายที่สุด** ผู้ป่วยใช้จริง และลด severe exacerbation ได้มากกว่าแบบที่ใช้ SABA เป็น reliever

| Step | Track 1 (preferred) | Track 2 (ทางเลือก) |
|---|---|---|
| 1–2 | **AIR**: ICS-formoterol ขนาดต่ำ **เมื่อมีอาการ** | step 1: พ่น ICS ทุกครั้งที่ใช้ SABA · step 2: ICS ขนาดต่ำทุกวัน + SABA เมื่อมีอาการ |
| 3 | **MART ขนาดต่ำ** | ICS-LABA ขนาดต่ำทุกวัน + reliever แยก |
| 4 | **MART ขนาดกลาง** | ICS-LABA ขนาดกลางทุกวัน + reliever แยก |
| 5 | + **LAMA** · ส่งประเมิน phenotype ± **biologic** · พิจารณา ICS-formoterol ขนาดสูง | + LAMA · biologic · ICS-LABA ขนาดสูง |

**อาจารย์เน้นเรื่อง Track 2 ในประเทศไทย**: reliever ของ Track 2 ควรเป็น ICS-SABA แต่ **ไทยไม่มี ICS-SABA ในหลอดเดียว** มีแต่ SABA กับ ICS แยก → คนไข้หนึ่งคนต้องใช้ **3 หลอด** (ICS-LABA + SABA + ICS) "เป็นไปได้ยากในทางปฏิบัติที่คนไข้จะยอมใช้จริง" · step down ใน Track 2 = ตัด LABA ออก เหลือ ICS ขนาดต่ำ

### เริ่มที่ขั้นไหน (ผู้ใหญ่และวัยรุ่น ≥ 12 ปี)
| อาการตอนมาครั้งแรก | เริ่ม Track 1 |
|---|---|
| อาการ **< 3–5 วัน/สัปดาห์** lung function ปกติหรือลดเล็กน้อย | step 1–2: AIR ICS-formoterol เมื่อมีอาการ |
| อาการ **เกือบทุกวัน** หรือ **ตื่นกลางคืน ≥ 1 ครั้ง/สัปดาห์** หรือ **lung function ต่ำ** | step 3: MART ขนาดต่ำ |
| อาการทุกวัน + ตื่นกลางคืน ≥ 1/สัปดาห์ + lung function ต่ำ | step 4: MART ขนาดกลาง |
| มาครั้งแรกด้วย **คุมไม่ได้รุนแรง หรือ exacerbation** | step 4 + **OCS ระยะสั้น** |

นักศึกษาสรุปในคาบ (อาจารย์ใช้ด้วย): **มีแต่อาการกลางวัน → step 1–2 · มีอาการกลางคืนหรือ lung function ต่ำ → step 3 · มี exacerbation → step 4** · อาจารย์ชี้ว่าในชีวิตจริง lung function ต่ำมักมาพร้อมอาการเสมอ

### สอนผู้ป่วยใช้ MART (budesonide-formoterol 200/6 mcg ชนิด DPI · delivered 160/4.5)
| ขั้น | ยาประจำ | เมื่อมีอาการ |
|---|---|---|
| Step 1–2 (AIR) | ไม่มี | 1 สูด · ซ้ำได้ถ้ายังมีอาการหลังไม่กี่นาที |
| Step 3 | 1 สูด เช้า–เย็น | 1 สูด |
| Step 4 | 2 สูด เช้า–เย็น | 1 สูด |

- รวมทั้งหมด **ไม่เกิน 12 สูด/วัน** (formoterol 72 mcg) · ถ้าต้องใช้เพิ่มหลายครั้งติดกัน 2–3 วัน → ทำตาม action plan/มาพบแพทย์
- **ไม่ต้องมี salbutamol แยก** · ใช้แบบ MART ได้เฉพาะ ICS-formoterol (budesonide-formoterol, beclometasone-formoterol) — **ห้ามทำ MART ด้วย ICS-salmeterol**
- ข้อมูลในคาบ: exacerbation เล็กน้อยในคลินิกใช้ **budesonide-formoterol 160/4.5 ครั้งละ 1–2 สูด** ได้แทน salbutamol (หัวข้อ 11)""",
    ["Track 1 ใช้ ICS-formoterol หลอดเดียวทุกขั้น — preferred เพราะง่ายและลด severe exacerbation",
     "อาจารย์: ทุกครั้งที่หอบต้องได้ ICS คู่เสมอ = AIR · ไม่ใช่ SABA เดี่ยว",
     "Step 3 = MART ขนาดต่ำ · step 4 = MART ขนาดกลาง (ไม่ใช่ high dose) · step 5 = + LAMA/biologic",
     "เริ่มขั้น: กลางวันอย่างเดียว 1–2 · กลางคืน/FEV1 ต่ำ 3 · มาด้วย exacerbation 4 + OCS สั้น",
     "MART สูงสุด 12 สูด/วัน · ใช้ได้เฉพาะ formoterol · ไทยไม่มี ICS-SABA หลอดเดียว"],
    [mcq(16, "A 31-year-old woman newly diagnosed with asthma has symptoms on most days and wakes with cough and wheeze about once a week. FEV1 is 72% predicted. She has never had an exacerbation. According to GINA Track 1, what is the most appropriate initial treatment?",
         ["Low-dose budesonide–formoterol as maintenance and reliever",
          "Low-dose budesonide–formoterol taken only when needed",
          "High-dose fluticasone daily with salbutamol when needed",
          "Low-dose fluticasone–salmeterol with salmeterol when needed",
          "Montelukast at night with salbutamol taken when needed"],
         "อาการ **เกือบทุกวัน** + **ตื่นกลางคืน ≥ 1 ครั้ง/สัปดาห์** + **FEV1 ต่ำ** แต่ยังไม่มี exacerbation = เริ่ม **Track 1 step 3: MART ขนาดต่ำ** (budesonide-formoterol 1 สูดเช้า–เย็น + 1 สูดเมื่อมีอาการ) · ICS คุมการอักเสบทุกวัน และทุกครั้งที่พ่นบรรเทาอาการได้ ICS เพิ่มตามความรุนแรงของวันนั้น\n\n"
         "- \"เฉพาะเมื่อมีอาการ\" — step 1–2 สำหรับอาการ < 3–5 วัน/สัปดาห์ น้อยเกินไปสำหรับรายนี้\n"
         "- \"high-dose fluticasone\" — **อาจารย์เน้น** ว่าขนาดสูงสงวนไว้ step 5 ผลข้างเคียงมาก ประโยชน์เพิ่มน้อย\n"
         "- \"salmeterol เป็นยาบรรเทา\" — salmeterol ออกฤทธิ์ช้า ใช้บรรเทาไม่ได้ และห้ามพ่นเพิ่มเกินขนาด\n"
         "- \"montelukast + SABA\" — ไม่มี ICS ได้ผลน้อยกว่าและยังพึ่ง SABA",
         "เกือบทุกวัน/ตื่นกลางคืน/FEV1 ต่ำ → MART ขนาดต่ำ (step 3)", "Initial treatment", G("Box 4-4 Initial asthma treatment, Track 1") + [CLS + "แผนผัง step (highlight 52:02)"], BASE + [ICS, BD]),
     mcq(17, "A 27-year-old man presents to clinic with his first asthma diagnosis. He has had daily wheeze, waking every night and needed emergency nebulisation 2 days ago; FEV1 today is 58% predicted. He is now able to speak in sentences with SpO2 96%. What is the most appropriate treatment to start?",
         ["Medium-dose budesonide–formoterol MART with a short course of prednisolone",
          "Low-dose budesonide–formoterol taken only when needed for symptoms",
          "Low-dose budesonide–formoterol MART without any oral corticosteroid",
          "High-dose fluticasone–salmeterol with salbutamol taken when needed",
          "Regular salbutamol four times daily with a short course of prednisolone"],
         "ผู้ป่วยใหม่ที่มาด้วย **คุมไม่ได้รุนแรง (อาการทุกวัน ตื่นทุกคืน FEV1 58%) และเพิ่งมี exacerbation** → GINA ให้เริ่ม **step 4: MART ขนาดกลาง** ร่วมกับ **OCS ระยะสั้น** (prednisolone 40–50 mg 5–7 วัน) เพื่อดับการอักเสบที่กำลังลุก แล้วนัดติดตามใน 1–2 สัปดาห์\n\n"
         "- \"เฉพาะเมื่อมีอาการ\" — step 1–2 ต่ำเกินไปมาก\n"
         "- \"MART ขนาดต่ำโดยไม่มี OCS\" — ต่ำกว่าที่แนะนำสำหรับคนที่มาด้วย exacerbation\n"
         "- \"high-dose fluticasone-salmeterol\" — high dose สงวนไว้ step 5 และไม่ใช่ทางที่แนะนำ\n"
         "- \"salbutamol ประจำ\" — ไม่มี ICS เป็นการรักษาที่ผิด",
         "มาครั้งแรกด้วย exacerbation/คุมไม่ได้รุนแรง → MART ขนาดกลาง + OCS สั้น", "Initial treatment", G("Box 4-4 Initial asthma treatment"), BASE + [ICS, BD, CORT, AE]),
     mcq(18, "A 40-year-old woman has been started on budesonide–formoterol 200/6 µg, one inhalation twice daily as maintenance and reliever therapy. She asks what to do when she feels wheezy during the day. What is the correct advice?",
         ["Take one extra inhalation of the same inhaler as needed",
          "Take two puffs of a separate salbutamol inhaler as needed",
          "Wait until symptoms have lasted a day before any extra dose",
          "Double tomorrow's morning maintenance dose instead",
          "Start prednisolone 40 mg from a supply kept at home"],
         "MART = ใช้ **หลอดเดียวกัน** ทั้งเป็นยาประจำและยาบรรเทา — มีอาการให้สูด **1 สูดเพิ่ม** (ซ้ำได้ถ้ายังไม่ดีขึ้นในไม่กี่นาที) รวมทั้งวันไม่เกิน 12 สูด · ได้ทั้ง formoterol (คลายเร็ว) และ budesonide (ต้านการอักเสบ) ตามความรุนแรงของวันนั้น ทำให้ exacerbation ลดลง\n\n"
         "- \"salbutamol แยก\" — ทำให้เสียข้อดีของ AIR และไม่ได้ ICS เพิ่มเวลามีอาการ\n"
         "- \"รอให้ครบวัน\" — การรอทำให้การอักเสบลุกลาม\n"
         "- \"เพิ่มขนาดพรุ่งนี้เช้า\" — ช้าเกินไป ไม่ช่วยอาการตอนนี้\n"
         "- \"prednisolone เอง\" — ใช้ตาม action plan เมื่อแย่ลงรุนแรงเท่านั้น ไม่ใช่ทุกครั้งที่หวีด",
         "MART: มีอาการ → 1 สูดของหลอดเดิม · ≤ 12 สูด/วัน", "MART", G("Box 4-8 MART dosing") + [CLS + "อาจารย์อธิบาย MART"], BASE + [ICS, BD])],
    BASE + [ICS, BD, CORT])

# ═════════════════════════════════════════════ 8
sec("chest-ast-08", "ติดตามผล — symptom control, ความเสี่ยงในอนาคต, step up/down, difficult-to-treat vs severe, remission",
    "4 คำถาม (จำแค่ 4 ข้อ) · well controlled = ขั้นต่ำ · ตรวจท่าพ่น/adherence ก่อน step up · step down หลังคุมดี 3 เดือน · remission 4 ข้อ", 11,
"""### ประเมิน symptom control
[[fig:control]]

- ถามย้อนหลัง **4 สัปดาห์**: อาการกลางวัน > 2 ครั้ง/สัปดาห์ · ตื่นกลางคืน · ใช้ยาบรรเทา > 2 ครั้ง/สัปดาห์ · กิจกรรมถูกจำกัด → **0 ข้อ well · 1–2 partly · 3–4 uncontrolled**
- **อาจารย์เน้น**: "จำแค่ 4 ข้อ" — ACQ/ACT ไม่ต้องจำ (ที่นำเสนอ: ACQ-5 เฉลี่ย ≤ 0.75 คุมได้ · 0.75–1.5 ก้ำกึ่ง · ≥ 1.5 คุมไม่ได้)
- **อาจารย์เน้น**: well controlled คือ **เกณฑ์ขั้นต่ำ** (ยังยอมให้มีอาการธรรมดา ≤ 2 ครั้ง/สัปดาห์) · เป้าปัจจุบันสูงกว่านั้น — **total control** คือไม่มีเลยสักข้อ และมุ่งสู่ remission

### ประเมินความเสี่ยงในอนาคต (แยกจาก symptom control)
| ความเสี่ยง | ปัจจัย |
|---|---|
| **Exacerbation** | อาการคุมไม่ได้ · **ไม่ได้ ICS/ใช้ไม่สม่ำเสมอ/ท่าผิด** · **SABA มาก** (≥ 3 กระบอก/ปี) · FEV1 ต่ำ (< 60%) · BD responsiveness สูง · สูบบุหรี่ allergen มลพิษ · โรคร่วม (อ้วน ไซนัส GERD food allergy ซึมเศร้า) · **เคยนอน ICU/ใส่ท่อ** · exacerbation รุนแรงใน 12 เดือน · eosinophil/FeNO สูง · ตั้งครรภ์ |
| **Persistent airflow limitation** | คลอดก่อนกำหนด น้ำหนักแรกเกิดน้อย น้ำหนักขึ้นเร็วในวัยทารก · ไอมีเสมหะเรื้อรัง · **exacerbation รุนแรงโดยไม่ได้ ICS** · ควัน สารเคมี งาน · FEV1 ต่ำตั้งแต่แรก · eosinophil ในเลือด/เสมหะสูง |
| **ผลข้างเคียงยา** | OCS บ่อย · ICS ขนาดสูงนาน · ใช้ร่วมกับยายับยั้ง CYP3A4 · ท่าพ่นผิด (เชื้อราในปาก) |

### Assess → Adjust → Review
- **ติดตาม** 1–3 เดือนหลังเริ่มยา แล้วทุก 3–12 เดือน · **ตั้งครรภ์ทุก 4–6 สัปดาห์** · หลัง exacerbation ภายใน 1 สัปดาห์
- **ก่อน step up ทุกครั้ง** ตรวจ: **ท่าพ่นยา · adherence · ยังสัมผัสตัวกระตุ้นไหม · โรคร่วม · วินิจฉัยถูกไหม** (ที่นำเสนอและอาจารย์ย้ำ)
- step up แบบ: ต่อเนื่อง ≥ 2–3 เดือน · ระยะสั้น 1–2 สัปดาห์ (เช่น ช่วงติดเชื้อไวรัส) · ปรับรายวัน (MART ทำให้อยู่แล้ว)
- **step down** เมื่อคุมได้ดีต่อเนื่อง **2–3 เดือน (GINA: 3 เดือน)** ลดทีละขั้น (ICS ลด 25–50%) เลือกช่วงไม่มีไข้หวัด ไม่เดินทาง ไม่ตั้งครรภ์ · **ผู้ใหญ่ไม่หยุด ICS ทั้งหมด**

### Difficult-to-treat กับ severe asthma (อาจารย์เน้น)
- ทั้งสองอยู่ใต้หัวใหญ่ **uncontrolled** = ใช้ยา **step 4–5** แล้วยังคุมไม่ได้ (หรือต้องใช้ขนาดสูงเพื่อคุม)
- **Difficult-to-treat** = ยังมี **ปัจจัยที่แก้ได้แต่ยังไม่ได้แก้**: ใช้ยาไม่ตามฉลาก ท่าพ่นผิด สูตรผิด ยังสูบบุหรี่ ยังใช้ beta-blocker/NSAID ยังเจอ allergen
- **Severe** = แก้ทุกอย่างที่แก้ได้แล้ว **รวมโรคร่วม** (OSA, GERD, อ้วน, rhinosinusitis, laryngeal obstruction, ซึมเศร้า วิตกกังวล) ก็ยังคุมไม่ได้ → ส่งผู้เชี่ยวชาญ (หัวข้อ 13)
- ประมาณการ: ผู้ป่วย asthma ราว 17% เป็น difficult-to-treat แต่เป็น severe จริงเพียงราว 3–4%

### Remission — เป้าหมายใหม่ (อาจารย์เน้น)
- **ไม่ใช่หายขาด** — clinical remission ต้องครบ **4 ข้อ** (ต่อเนื่อง ≥ 12 เดือน ตามแนวทางส่วนใหญ่)
  1. **ไม่มีอาการ** — "ไม่ใช่มีนิดหน่อย ต้องไม่มี"
  2. **ไม่มี exacerbation**
  3. **lung function ปกติ/คงที่**
  4. **ไม่ต้องใช้ OCS** — ทั้งแบบกินทุกวันและแบบเป็นคอร์ส
- **Complete remission** = 4 ข้อ + **biomarker** ที่เคยสูง (FeNO, eosinophil) กลับปกติ + **หลอดลมไม่ไวเกินแล้ว**""",
    ["4 คำถาม (4 สัปดาห์): กลางวัน > 2/สัปดาห์ · ตื่นกลางคืน · reliever > 2/สัปดาห์ · กิจกรรมจำกัด",
     "Well controlled = เกณฑ์ขั้นต่ำ · เป้าคือ total control → remission",
     "ก่อน step up: ท่าพ่น · adherence · ตัวกระตุ้น · โรคร่วม · วินิจฉัยถูกไหม",
     "Difficult-to-treat = ยังมีปัจจัยแก้ได้ · severe = แก้หมดแล้วยังคุมไม่ได้",
     "Clinical remission: ไม่มีอาการ ไม่กำเริบ ปอดปกติ/คงที่ ไม่ใช้ OCS"],
    [mcq(19, "A 29-year-old man on low-dose budesonide–formoterol maintenance and reliever therapy reports daytime symptoms three times a week and uses extra inhalations about three times a week, but no night waking or activity limitation. What should be done first?",
         ["Check his inhaler technique and adherence",
          "Step up to medium-dose maintenance therapy",
          "Add a long-acting muscarinic antagonist",
          "Prescribe a five-day course of prednisolone",
          "Refer him for assessment for a biologic"],
         "มี 2 ใน 4 ข้อ (อาการกลางวันและใช้ยาบรรเทา > 2 ครั้ง/สัปดาห์) = **partly controlled** · ก่อน step up ทุกครั้ง GINA และอาจารย์ให้หา **สาเหตุที่แก้ได้ก่อน** — ท่าพ่นผิดพบได้ในผู้ป่วยส่วนใหญ่ และการไม่ใช้ยาประจำทำให้ ICS ไม่ถึงหลอดลม · ถ้าท่าพ่น/adherence/ตัวกระตุ้น/โรคร่วมดีแล้วจึงค่อยเพิ่มเป็นขนาดกลาง\n\n"
         "- \"step up ทันที\" — ถ้าปัญหาคือท่าพ่น การเพิ่มยาไม่ช่วยและเพิ่มผลข้างเคียง\n"
         "- \"เพิ่ม LAMA\" — เป็น add-on step 5\n"
         "- \"prednisolone\" — ไม่มี exacerbation ไม่ใช่ข้อบ่งชี้\n"
         "- \"biologic\" — สำหรับ severe asthma หลังแก้ทุกปัจจัยแล้วที่ step 4–5",
         "ก่อน step up: ท่าพ่น + adherence ก่อนเสมอ", "Step up", G("Box 4-2 Assess-Adjust-Review") + [CLS + "ที่นำเสนอและอาจารย์ย้ำ"], BASE + [ICS]),
     mcq(20, "A 52-year-old woman remains uncontrolled despite medium-dose budesonide–formoterol MART for 6 months. At review she cannot generate a fast inhalation through her dry-powder inhaler and admits she often forgets the evening dose. How should her asthma currently be classified?",
         ["Difficult-to-treat asthma", "Severe asthma", "Well-controlled asthma",
          "Partly controlled mild asthma", "Corticosteroid-resistant asthma"],
         "ใช้ยา **step 4** แล้วยังคุมไม่ได้ = uncontrolled · แต่ยังมี **ปัจจัยที่แก้ได้** (ท่าพ่น DPI ผิด — สูดไม่แรงพอให้ผงยาแตกตัว และลืมยา) → เป็น **difficult-to-treat** · **อาจารย์เน้น**: จะเรียก severe ได้ก็ต่อเมื่อแก้ทุกอย่างที่แก้ได้แล้ว รวมโรคร่วม ก็ยังคุมไม่ได้\n\n"
         "- \"severe asthma\" — ยังเรียกไม่ได้จนกว่าจะแก้ท่าพ่นและ adherence\n- \"well-controlled\" — ขัดกับข้อมูล\n"
         "- \"partly controlled mild\" — ผู้ป่วยอยู่ step 4 ไม่ใช่ mild\n- \"steroid-resistant\" — สรุปไม่ได้เมื่อยาเข้าไม่ถึงหลอดลม",
         "Step 4–5 คุมไม่ได้ + ยังมีปัจจัยแก้ได้ = difficult-to-treat", "Difficult vs severe", G("Severe asthma guide — definitions") + [CLS + "อาจารย์อธิบาย difficult vs severe"], BASE + [ICS])],
    BASE + [ICS, CORT, ADR],
    AN.FIGS["chest-ast-08"])

# ═════════════════════════════════════════════ 9
sec("chest-ast-09", "เทคนิคพ่นยา action plan และการดูแลที่ไม่ใช้ยา",
    "pMDI + spacer: สูดช้า · DPI: สูดแรงเร็ว · บ้วนปากหลัง ICS · teach-back · written action plan · เลิกบุหรี่ วัคซีน ลดน้ำหนัก ออกกำลัง", 8,
"""### pMDI กับ spacer
- ผู้ป่วยส่วนใหญ่ (กว่า 2 ใน 3 ในหลายการศึกษา) พ่นผิดอย่างน้อย 1 ขั้น — ยาไม่ถึงหลอดลมเล็ก ดูเหมือน "ยาไม่ได้ผล"
- **pMDI ต้องสูดช้า ลึก** (ละอองพุ่งเร็วอยู่แล้ว ถ้าสูดเร็วยาจะกระแทกคอ) · **DPI ต้องสูดแรงเร็ว** (แรงสูดทำให้ผงยาแตกเป็นอนุภาคเล็ก)
- spacer ลดการพึ่งการประสานมือ ลดยาค้างในคอ → ลด oral candidiasis และเสียงแหบ

### เทียบ pMDI กับ DPI (เช่น Turbuhaler ของ budesonide-formoterol)
| ขั้น | pMDI (+ spacer) | DPI (Turbuhaler) |
|---|---|---|
| เตรียม | เขย่า เปิดฝา ต่อ spacer | ตั้งตรง บิดฐานไปจนสุดแล้วบิดกลับจนได้ยิน "คลิก" — **ไม่เขย่า** |
| ก่อนสูด | หายใจออกนอกอุปกรณ์ | หายใจออกนอกอุปกรณ์ — **ห้ามเป่าเข้า** (ผงชื้นจับก้อน) |
| สูด | กด 1 ครั้ง สูด **ช้า ลึก 3–5 วินาที** | สูด **แรง เร็ว ลึก** |
| หลังสูด | กลั้นหายใจ ~10 วินาที | กลั้นหายใจ ~10 วินาที |
| ปิดท้าย | ยาที่มี ICS → บ้วนปาก กลั้วคอ | บ้วนปาก กลั้วคอ |

- ให้ผู้ป่วย **ทำให้ดู (teach-back)** ทุกครั้งที่นัด โดยเฉพาะก่อน step up · เลือก device ตามแรงสูดและความถนัด (ผู้สูงอายุ/หอบมากอาจสูดแรงไม่พอสำหรับ DPI)

### Written asthma action plan
บอก 3 อย่าง: ยาประจำและยาบรรเทาคืออะไร · **อาการ/PEF แบบไหนคือแย่ลง** และต้องเพิ่มยาอย่างไร (MART: เพิ่มสูดตามอาการ · Track 2: เพิ่ม ICS) · **เมื่อไหร่ต้องเริ่ม OCS และมาโรงพยาบาลทันที** (พูดเป็นคำ ๆ, PEF < 50%, ยาไม่ช่วย) — ลด exacerbation และการตาย

### การดูแลที่ไม่ใช้ยา (ที่นำเสนอในคาบ + GINA)
- **เลิกบุหรี่และบุหรี่ไฟฟ้า** ทั้งผู้ป่วยและคนในบ้าน — ควันทำให้ตอบสนองต่อ ICS น้อยลง
- หลีกเลี่ยง allergen และมลพิษในบ้าน/ที่ทำงาน · PM2.5 สูงให้อยู่ในอาคาร/ใส่หน้ากาก (การกำจัดไรฝุ่นอย่างเดียวได้ผลจำกัด)
- **วัคซีน**: influenza ทุกปี · COVID-19 · RSV ในผู้สูงอายุตามเกณฑ์ของแต่ละประเทศ (ในคาบพูดถึงอายุ ≥ 50 ปี) · pneumococcal ตามเกณฑ์อายุ/โรคร่วม
- ออกกำลังกายสม่ำเสมอ · breathing exercise · **ลดน้ำหนัก** ในคนอ้วน
- ทบทวนยา: **NSAID/aspirin** (ถ้าเคยแพ้ — หัวข้อ 12) · **beta-blocker ชนิดไม่จำเพาะ** (รวมยาหยอดตา timolol) ห้าม · ชนิด cardioselective ใช้ได้เมื่อมีข้อบ่งชี้ชัด (เช่น หลัง MI) โดยติดตามใกล้ชิด""",
    ["pMDI สูดช้า ลึก · DPI สูดแรง เร็ว — ห้ามเป่าเข้า DPI",
     "ยาที่มี ICS → บ้วนปากกลั้วคอ · ใช้ spacer ลดยาค้างในคอ",
     "Teach-back ทุกนัด — ท่าพ่นผิดพบในผู้ป่วยส่วนใหญ่",
     "Action plan: ยาอะไร · แย่ลงแค่ไหนเพิ่มยาอย่างไร · เมื่อไหร่ OCS/มาโรงพยาบาล",
     "เลิกบุหรี่ วัคซีนไข้หวัดใหญ่ ลดน้ำหนัก · ห้าม non-selective beta-blocker"],
    [mcq(21, "A 19-year-old student demonstrates her salbutamol pMDI with a spacer. She shakes the inhaler, attaches it, breathes out away from the device, seals her lips, presses once and inhales as fast and hard as she can so that the spacer whistles, then holds her breath for 10 seconds. Which step should be corrected?",
         ["Inhaling as fast and hard as possible after pressing",
          "Shaking the canister before attaching it to the spacer",
          "Breathing out fully away from the spacer before the dose",
          "Pressing the canister only once for each inhalation",
          "Holding her breath for about 10 seconds afterwards"],
         "pMDI ปล่อยละอองที่พุ่งเร็วอยู่แล้ว ต้อง **สูดช้าและลึก 3–5 วินาที** ให้ละอองลอยเข้าไปถึงหลอดลมเล็ก · การสูดแรงเร็ว (spacer มีเสียงหวีดเตือน) ทำให้ยากระแทกคอและผนัง spacer — นั่นคือท่าของ **DPI** ซึ่งต้องใช้แรงสูดทำให้ผงแตกตัว\n\n"
         "- \"เขย่า\" — ถูก pMDI เป็นยาแขวนตะกอน\n- \"หายใจออกนอกอุปกรณ์\" — ถูก\n"
         "- \"กดครั้งเดียวต่อการสูด\" — ถูก กดหลายครั้งทำให้ละอองจับกันติดผนัง\n- \"กลั้นหายใจ 10 วินาที\" — ถูก ให้ละอองตกตะกอน",
         "pMDI = สูดช้า · DPI = สูดแรงเร็ว", "Inhaler technique", G("Chapter 5 — inhaler skills"), BASE + [BD])],
    BASE + [BD, ICS, TOB, IMM])

# ═════════════════════════════════════════════ 10
sec("chest-ast-10", "Acute exacerbation — ตัวกระตุ้น ใครเสี่ยงตาย และแบ่งความรุนแรง",
    "ไวรัส allergen PM2.5 ใช้ยาไม่สม่ำเสมอ · ความเสี่ยงตาย 4 กลุ่ม · พูด/RR/SpO2/PEF · silent chest · PaCO2 ปกติ = อันตราย", 10,
"""### Exacerbation คืออะไร
อาการ (เหนื่อย ไอ wheeze แน่นอก) **แย่ลงอย่างต่อเนื่อง** ร่วมกับ lung function ลดลง จนต้องเปลี่ยนการรักษา · อาจเป็นอาการแรกที่ทำให้วินิจฉัย asthma

### ตัวกระตุ้น (ที่นำเสนอในคาบ)
- **ไวรัส** — rhinovirus (พบบ่อยที่สุด), influenza, RSV · ไวรัสทำลายเยื่อบุ → alarmin → การอักเสบ T2 ลุก
- **allergen** — เกสร ไรฝุ่น สปอร์รา · **food allergy** ไม่ใช่สาเหตุหลัก แต่ถ้ามี **ลมพิษ ปาก/หน้าบวม ความดันต่ำ** หลังกินอาหาร = **anaphylaxis** → adrenaline IM ก่อน
- **PM2.5** · อากาศเย็น เปลี่ยนฤดู · **ใช้ ICS ไม่สม่ำเสมอ** (สาเหตุที่แก้ได้บ่อยที่สุด) · NSAID ในคนที่แพ้

### ใครเสี่ยงตายจาก asthma (4 กลุ่ม — ที่นำเสนอในคาบ ตาม GINA)
| กลุ่ม | ปัจจัย |
|---|---|
| **เคยรุนแรงมาก่อน** | **เคยใส่ท่อ/ใช้เครื่องช่วยหายใจ** · นอนโรงพยาบาล/มา ER ใน 12 เดือน · กำลังใช้หรือเพิ่งหยุด OCS |
| **คุมโรคไม่ดี** | **ไม่ได้ ICS** หรือใช้ไม่สม่ำเสมอ · ไม่มี/ไม่ทำตาม action plan · **SABA > 1 กระบอก/เดือน** หรือพ่น nebulized SABA ประจำ |
| **ปัจจัยผู้ป่วย** | โรคจิตเวช/ปัญหาสังคม · food allergy/เคย anaphylaxis · **รับรู้อาการได้ไม่ดี** (หลอดลมตีบมากแต่ไม่รู้สึก) · หลอดลมไวเกินรุนแรง |
| **โรคร่วม** | pneumonia · เบาหวาน · arrhythmia |

→ บันทึกความเสี่ยงให้ชัด สอนสัญญาณเตือน และให้มาพบแพทย์ตั้งแต่เริ่มแย่ลง

### แบ่งความรุนแรงที่ข้างเตียง
[[fig:severity]]

- ประเมิน **อาการ การหายใจ SpO2 และ PEF** (ถ้าวัดได้) — **อย่ารอ ABG** ก่อนเริ่มรักษา
- **PEF % = PEF ที่วัดได้ ÷ ค่าดีที่สุดของผู้ป่วย (หรือค่าคาดการณ์) × 100** — เช่น 130 ÷ 420 = 31% = life-threatening ตามเกณฑ์ BTS (< 33%)
- ตรวจเพิ่มในรายรุนแรง: **ABG** เมื่อ SpO2 < 92% หรือมีลักษณะ life-threatening · K (ได้ SABA มาก) · **CXR ไม่ต้องทำทุกราย** — ทำเมื่อสงสัย pneumothorax, pneumonia, หรือไม่ตอบสนองต่อการรักษา

### PaCO2 ปกติ = อันตราย
- ระหว่างหอบ ผู้ป่วยหายใจเร็ว PaCO2 **ควรต่ำ** · ถ้า PaCO2 กลับมา "ปกติ" (≈ 40 mmHg) แปลว่ากล้ามเนื้อหายใจเริ่มล้า และกำลังจะเป็น type 2 respiratory failure
- ข้อนี้ข้อสอบ Ward Drill ออก (ข้อ CH-MCQ-36 ท้ายหัวข้อ)""",
    ["Rhinovirus เป็นตัวกระตุ้นที่พบบ่อยที่สุด · ใช้ ICS ไม่สม่ำเสมอคือสาเหตุที่แก้ได้",
     "เคยใส่ท่อ/ICU คือปัจจัยเสี่ยงตายที่แรงที่สุด · SABA > 1 กระบอก/เดือนเป็นธงแดง",
     "Severe: พูดเป็นคำ RR > 30 SpO2 < 92% PEF ≤ 50% · life-threatening: silent chest ซึม เขียว PEF < 33%",
     "PaCO2 ปกติในคนหอบหนัก = กำลังจะหยุดหายใจ",
     "อย่ารอ ABG/CXR ก่อนเริ่มรักษา — CXR ทำเมื่อสงสัย pneumothorax/pneumonia"],
    [mcq(22, "Which of the following features in the history of a patient with asthma most strongly increases the risk of a fatal attack?",
         ["Previous intubation for an asthma attack",
          "Childhood eczema that has now resolved",
          "Allergic rhinitis treated with a nasal steroid",
          "Symptoms triggered mainly by cold air",
          "A sibling who also has asthma"],
         "การเคย **ใส่ท่อช่วยหายใจหรือเข้า ICU จาก asthma** บอกว่าผู้ป่วยรายนี้เคยหลอดลมตีบจนการหายใจล้มเหลวมาแล้ว — มักมีหลอดลมไวเกินรุนแรงและ **รับรู้ความรุนแรงได้ไม่ดี** มาโรงพยาบาลช้า · เป็นปัจจัยเสี่ยงตายที่แรงที่สุดในรายการของ GINA (กลุ่ม \"เคยรุนแรงมาก่อน\")\n\n"
         "- \"eczema ในวัยเด็ก\" — บอก atopy ไม่ใช่ความเสี่ยงตาย\n- \"allergic rhinitis ที่รักษาอยู่\" — การรักษาจมูกช่วยคุมหืดด้วยซ้ำ\n"
         "- \"กระตุ้นด้วยอากาศเย็น\" — เป็นตัวกระตุ้นทั่วไป\n- \"พี่น้องเป็น asthma\" — บอกความเสี่ยงเป็นโรค ไม่ใช่ความเสี่ยงตาย",
         "เคยใส่ท่อ/ICU จาก asthma = เสี่ยงตายสูงสุด", "Risk of asthma death", G("Box 9-1 Risk factors for asthma-related death") + [CLS + "ที่นำเสนอ 4 กลุ่ม"], BASE + [AE])],
    BASE + [AE, ARF, RF, ABG, ABGB, SPIRO, CTRL, SHOCK],
    AN.FIGS["chest-ast-10"])

# ═════════════════════════════════════════════ 11
sec("chest-ast-11", "รักษา exacerbation — คลินิก ห้องฉุกเฉิน ICU และการจำหน่าย",
    "SABA ซ้ำ · ipratropium ในรายรุนแรง · OCS ภายใน 1 ชม. · O2 เป้า 93–95% · MgSO4 2 g IV · ข้อบ่งชี้ ICU · เกณฑ์จำหน่าย · นัด 2–7 วัน", 13,
"""### ขนาดยาตามความรุนแรง (ที่นำเสนอในคาบ — GINA primary care)
| ระดับ | ยาขยายหลอดลม | อื่น ๆ |
|---|---|---|
| **Mild** | **salbutamol 4 puffs** pMDI + spacer หรือ **budesonide-formoterol 160/4.5 1–2 สูด** · ประเมินซ้ำ แล้วให้ซ้ำตามการตอบสนอง | ปรับยาควบคุม |
| **Moderate** | salbutamol **4–6 puffs** หรือ **2.5 mg nebulizer** · ซ้ำได้ **3 ครั้ง ห่าง 20–30 นาที** | **ipratropium 4 puffs** ร่วมได้ ≤ 3 ครั้ง · **prednisolone** |
| **Severe/life-threatening** | ส่งต่อสถานที่ดูแลวิกฤตได้ · salbutamol **6–10 puffs** หรือ **5 mg nebulizer** ซ้ำทุก 20–30 นาที (หรือพ่นต่อเนื่อง) + ipratropium | **O2** · **systemic corticosteroid** · monitor ตลอด · มี anaphylaxis ร่วม → **adrenaline IM ก่อน** |

ประเมินซ้ำทุก **30–60 นาที** (หรือเร็วกว่านั้นถ้าแย่ลง): อาการ RR การใช้กล้ามเนื้อช่วยหายใจ air entry SpO2 PEF

### ยาแต่ละตัว — ทำไมต้องให้ และให้อย่างไร (GINA ED)
- **Oxygen** — titrate เป้า **SpO2 93–95%** ในผู้ใหญ่ (เด็ก 94–98%) · ในคาบนำเสนอ 92–95% · **ไม่ให้จนสูงเกิน** (O2 สูงเกินทำให้ PaCO2 เพิ่มได้แม้ใน asthma)
- **SABA** — คลายกล้ามเนื้อเรียบเร็ว · pMDI + spacer ได้ผลเท่า nebulizer ในรายที่ไม่ถึงขั้น life-threatening
- **Ipratropium** — เพิ่มในรายรุนแรง ลดการ admit (ใช้เฉพาะช่วงเฉียบพลัน)
- **Systemic corticosteroid ภายใน 1 ชั่วโมง** — prednisolone **40–50 mg/วัน 5–7 วัน** (ไม่ต้อง taper) หรือ hydrocortisone 100 mg IV ทุก 6 ชม. ถ้ากินไม่ได้ · ออกฤทธิ์หลัง 4–6 ชม. จึงต้องให้เร็ว · กินได้ผลเท่าฉีด
- **Magnesium sulfate 2 g IV ใน 20 นาที (ครั้งเดียว)** — ในรายรุนแรงที่ไม่ตอบสนองการรักษาเริ่มต้น หรือ FEV1/PEF < 25–30% หลัง 1 ชม. · กลไก: ต้าน Ca2+ เข้าเซลล์กล้ามเนื้อเรียบ ลด acetylcholine และ histamine release
- **ไม่แนะนำ**: aminophylline/theophylline (ผลข้างเคียงมาก) · ยานอนหลับ/ยากล่อมประสาท (กดการหายใจ) · antibiotic ถ้าไม่มีหลักฐานติดเชื้อแบคทีเรีย · CXR ทุกราย

### ข้อบ่งชี้ ICU / ใส่ท่อช่วยหายใจ
- ลักษณะ **life-threatening** (silent chest, ซึม สับสน, เขียว, หมดแรง) · ไม่ตอบสนองแม้รักษาเต็มที่ · PEF แย่ลง · hypoxemia ไม่ดีขึ้น · **PaCO2 ปกติหรือสูงขึ้น** · acidosis · หยุดหายใจ
- ถ้าต้องใส่ท่อ: แพทย์ที่ชำนาญ · ตั้ง **RR ต่ำ tidal volume ต่ำ expiratory time ยาว** ยอมให้ CO2 สูง (**permissive hypercapnia**) เพื่อกัน air trapping/auto-PEEP ที่ทำให้ความดันตกและ pneumothorax

### เกณฑ์จำหน่าย (ที่นำเสนอในคาบ)
- อาการดีขึ้นและคงที่ **อย่างน้อย 1–2 ชม. หลัง salbutamol ครั้งสุดท้าย** · **SpO2 ห้องธรรมดา ≥ 92%** (GINA ED: > 94%) · **PEF ดีขึ้นและ > 70% ของค่าดีที่สุด/คาดการณ์** (GINA: 60–80%) · ผู้ป่วยพร้อมดูแลตัวเองที่บ้าน — ขึ้นกับดุลยพินิจของทีม

### ก่อนกลับบ้าน — ช่วงเวลาที่ป้องกันครั้งต่อไปได้ดีที่สุด
1. บันทึกการวินิจฉัยและ **ตัวกระตุ้น**
2. **เริ่มหรือเพิ่ม ICS-containing treatment** — ผู้ที่อายุ ≥ 12 ปีแนะนำ **ICS-formoterol (MART)** · ให้ prednisolone ต่อจนครบ 5–7 วัน
3. **ตรวจท่าพ่นยา** และ adherence
4. ให้ **written asthma action plan** · ยาพอใช้
5. **นัดภายใน 2–7 วัน (ผู้ใหญ่)** · เด็ก 2–5 วัน (ในคาบ)
- ถ้าไม่ดีขึ้นในคลินิก: เพิ่ม ipratropium ถ้ายังไม่ได้ให้ · step up · **ส่งต่อด่วน**""",
    ["ทุกระดับเริ่ม SABA (หรือ ICS-formoterol ใน mild) · ประเมินซ้ำทุก 30–60 นาที",
     "Systemic steroid ภายใน 1 ชม. — prednisolone 40–50 mg 5–7 วัน ไม่ต้อง taper",
     "O2 เป้า 93–95% (GINA) — ไม่ใช่ 88–92% แบบ COPD และไม่ใช่ 100%",
     "MgSO4 2 g IV ใน 20 นาที เมื่อรุนแรงและไม่ตอบสนอง · aminophylline/ยากล่อมประสาทไม่แนะนำ",
     "ก่อนกลับ: เริ่ม/เพิ่ม ICS (MART) · ท่าพ่น · action plan · นัด 2–7 วัน"],
    [mcq(24, "A 33-year-old woman with severe acute asthma has received oxygen, three doses of nebulised salbutamol with ipratropium, and oral prednisolone 50 mg. After 1 hour she still speaks in short phrases and her PEF is 28% of her best. SpO2 is 94% on oxygen. Which additional drug is most appropriate now?",
         ["IV magnesium sulfate 2 g over 20 minutes",
          "Oral montelukast 10 mg once at bedtime",
          "IV ceftriaxone 2 g once daily",
          "IV furosemide 40 mg as a single bolus",
          "Oral midazolam 7.5 mg as a single dose"],
         "หอบรุนแรงที่ **ไม่ตอบสนองหลังรักษาเริ่มต้น 1 ชั่วโมง** และ PEF < 30% → เพิ่ม **magnesium sulfate 2 g IV ใน 20 นาที** ครั้งเดียว (GINA) · Mg ต้านการไหลเข้าของ Ca2+ ในกล้ามเนื้อเรียบหลอดลม และลดการหลั่ง acetylcholine/histamine → คลายหลอดลมเพิ่ม ลดการ admit ในบางกลุ่ม · ระหว่างนี้แจ้งแพทย์อาวุโส/ICU\n\n"
         "- \"montelukast\" — ไม่มีบทบาทในการรักษาเฉียบพลัน\n- \"ceftriaxone\" — ไม่มีหลักฐานติดเชื้อแบคทีเรีย\n"
         "- \"furosemide\" — สำหรับน้ำท่วมปอดจากหัวใจ ไม่ใช่ asthma\n- \"midazolam\" — ยากล่อมประสาทกดการหายใจ ห้ามในหอบรุนแรง",
         "Severe ไม่ตอบสนองใน 1 ชม. → MgSO4 2 g IV", "Magnesium", G("Box 9-6 Management in acute care facility"), BASE + [AE, BD, CORT]),
     mcq(26, "A 24-year-old man is ready for discharge after a moderate asthma exacerbation treated in the emergency department. Before the attack he used only salbutamol as needed. Which discharge plan is most appropriate?",
         ["Start budesonide–formoterol MART, check technique and review in 2–7 days",
          "Continue salbutamol as needed because his symptoms have now resolved",
          "Prescribe prednisolone tapered over 4 weeks with salbutamol as needed",
          "Arrange spirometry in 6 months as the only follow-up for this attack",
          "Give oral amoxicillin for 5 days to prevent an early relapse of the attack"],
         "exacerbation คือ **สัญญาณว่าการอักเสบไม่ถูกคุม** · ผู้ป่วยใช้ SABA เดี่ยว (ปัจจัยเสี่ยงตาย) → ต้อง **เริ่มยาที่มี ICS** (อายุ ≥ 12 แนะนำ ICS-formoterol MART) + prednisolone ให้ครบ 5–7 วัน + **ตรวจท่าพ่น** + **action plan** + **นัดภายใน 2–7 วัน** — ทั้งหมดคือรายการก่อนจำหน่ายที่นำเสนอในคาบ\n\n"
         "- \"salbutamol ต่อ\" — **อาจารย์เน้น** ว่า SABA เดี่ยวคือการรักษาที่ผิด\n"
         "- \"prednisolone taper 4 สัปดาห์\" — คอร์ส 5–7 วันพอและไม่ต้อง taper · ยาวไปเพิ่มผลข้างเคียง\n"
         "- \"spirometry 6 เดือน\" — นัดช้าเกินไป ช่วง 1–2 สัปดาห์แรกเสี่ยงกลับเป็นซ้ำ\n"
         "- \"amoxicillin\" — exacerbation ส่วนใหญ่มาจากไวรัส antibiotic ไม่ช่วย",
         "ก่อนกลับ: ICS (MART) + ท่าพ่น + action plan + นัด 2–7 วัน", "Discharge", G("Box 9-7 Discharge management") + [CLS + "เกณฑ์จำหน่ายที่นำเสนอ"], BASE + [AE, ICS])],
    BASE + [AE, ARF, BD, CORT, ABG, ANA, SHOCK],
    src=SRC)

# ═════════════════════════════════════════════ 12
sec("chest-ast-12", "สถานการณ์พิเศษ — AERD, ตั้งครรภ์, exercise-induced bronchoconstriction",
    "Samter's triad: COX-1 → leukotriene · ตั้งครรภ์: ยาปลอดภัยกว่าหอบ ห้ามหยุด ICS · EIB: น้ำระเหยจากเยื่อบุ → osmolarity → mast cell", 9,
"""> หัวข้อนี้ **ไม่ได้พูดในคาบ** — เรียบเรียงจาก GINA 2024 เพราะอยู่ในขอบเขตที่ NL ถามบ่อย

### Aspirin-exacerbated respiratory disease (AERD/N-ERD)
- **Samter's triad**: asthma (มักเริ่มวัยผู้ใหญ่ รุนแรง) + **chronic rhinosinusitis with nasal polyps** (ได้กลิ่นลดลง) + หอบ คัดจมูก หน้าแดง **30–120 นาที หลัง aspirin/NSAID**
- พบราว 7% ของผู้ใหญ่ที่เป็น asthma และราว 15% ของ severe asthma
- **กลไก**: aspirin/NSAID ยับยั้ง **COX-1** → PGE2 (ตัวเบรก mast cell) ลดลง และ arachidonic acid ถูกเบนไปทาง **5-lipoxygenase** → **cysteinyl leukotriene** ล้น → หลอดลมหดตัว จมูกบวม · **ไม่ใช่ IgE**
- ดูแล: เลี่ยง aspirin/NSAID ที่ยับยั้ง COX-1 ทุกตัว · **paracetamol ขนาดต่ำ** และ **COX-2 selective (celecoxib)** มักใช้ได้ · ICS เป็นหลัก · **montelukast** ช่วยได้ · aspirin desensitization/biologic ในบางราย (ผู้เชี่ยวชาญ)

### Asthma ในหญิงตั้งครรภ์
- ราว 1/3 ดีขึ้น 1/3 เท่าเดิม 1/3 แย่ลง (มักช่วงไตรมาส 2–3)
- **หอบที่คุมไม่ได้อันตรายต่อทารกกว่ายา** (hypoxemia → ทารกโตช้า คลอดก่อนกำหนด preeclampsia)
- **ห้ามหยุด ICS** — budesonide มีข้อมูลมากที่สุด · ICS-formoterol, SABA ใช้ได้ · ข้อมูล biologic ยังน้อย
- ติดตามทุก **4–6 สัปดาห์** (ในคาบ) · exacerbation รักษาเต็มที่เหมือนคนไม่ตั้งครรภ์ (OCS ใช้ได้) · เป้า SpO2 ≥ 95% · ติดตามทารก
- ช่วงคลอด: ใช้ยาประจำต่อ · ผู้ที่ได้ OCS ขนาดสูงก่อนคลอดระวัง adrenal insufficiency และน้ำตาลต่ำในทารก

### Exercise-induced bronchoconstriction (EIB)
- อาการ **ระหว่างหรือหลังออกกำลัง** สูงสุดราว 5–10 นาทีหลังหยุด หายเองใน 30–60 นาที · พบบ่อยในนักกีฬาที่หายใจแรงในอากาศเย็น/แห้ง
- **กลไก**: หายใจเร็วแรง → น้ำระเหยจากผิวเยื่อบุ → **osmolarity สูง** + เยื่อบุเย็นลง → mast cell หลั่ง histamine/leukotriene → หลอดลมหดตัว
- วินิจฉัย: exercise challenge — **FEV1 ลด > 10% และ > 200 mL** (อาจารย์ย้ำว่าตัวเลขนี้ต่างจากเกณฑ์อื่น)
- ป้องกัน: warm-up · **ICS-formoterol ขนาดต่ำก่อนออกกำลัง** (หรือ SABA ก่อนออกกำลังใน Track 2) · ถ้าเป็นบ่อยแปลว่าคุมโรคไม่ดี → ICS ประจำ · LTRA เป็นทางเลือก
- แยก **inducible laryngeal obstruction** (เสียงหวีดตอนหายใจเข้าระหว่างออกกำลัง หายทันทีเมื่อหยุด — หัวข้อ 5)

### ยาที่ทำให้ asthma แย่ลง
NSAID/aspirin (ในคน AERD) · **non-selective beta-blocker** รวมยาหยอดตา · ACE inhibitor (ทำให้ไอ ไม่ทำให้หลอดลมตีบโดยตรง)""",
    ["Samter's triad = asthma + nasal polyp + แพ้ aspirin/NSAID · กลไก COX-1 → leukotriene ล้น ไม่ใช่ IgE",
     "AERD: paracetamol ขนาดต่ำ/celecoxib มักใช้ได้ · montelukast ช่วย",
     "ตั้งครรภ์: หอบที่คุมไม่ได้อันตรายกว่ายา — ห้ามหยุด ICS · budesonide ข้อมูลมากที่สุด",
     "EIB: น้ำระเหย → osmolarity สูง → mast cell · exercise challenge FEV1 ลด > 10%",
     "ห้าม non-selective beta-blocker รวมยาหยอดตา timolol"],
    [mcq(27, "A 44-year-old woman with adult-onset asthma, nasal polyps and loss of smell develops wheeze, nasal congestion and facial flushing 45 minutes after taking ibuprofen for back pain. What is the underlying mechanism of this reaction?",
         ["Shunting of arachidonic acid towards cysteinyl leukotriene production",
          "IgE antibodies directed against ibuprofen bound to airway mast cells",
          "Direct histamine release from basophils by the propionic acid group",
          "Accumulation of bradykinin from reduced angiotensin-converting enzyme",
          "Complement activation by immune complexes formed with ibuprofen"],
         "นี่คือ **AERD (Samter's triad)** · ibuprofen ยับยั้ง **COX-1** → PGE2 ซึ่งปกติ \"เบรก\" mast cell และการสร้าง leukotriene ลดลง · arachidonic acid ถูกเบนไปทาง **5-lipoxygenase** → **cysteinyl leukotriene (LTC4/D4/E4)** สูงมาก → หลอดลมหดตัว จมูกบวม หน้าแดง · เป็นปฏิกิริยาทางเภสัชวิทยา **ไม่ใช่ IgE** จึงเกิดกับ NSAID ที่ยับยั้ง COX-1 ทุกตัว\n\n"
         "- \"IgE ต่อ ibuprofen\" — ถ้าเป็น IgE จะแพ้เฉพาะยาตัวนั้น แต่ AERD ข้ามกลุ่มทุก COX-1 inhibitor\n"
         "- \"histamine จาก basophil โดยตรง\" — ไม่ใช่กลไกหลัก\n- \"bradykinin\" — กลไกของไอ/angioedema จาก ACE inhibitor\n"
         "- \"complement จาก immune complex\" — type III ไม่เกี่ยว",
         "AERD = COX-1 ถูกบล็อก → leukotriene ล้น", "AERD", G("Chapter 6 — aspirin-exacerbated respiratory disease"), BASE + [ADR, POLYP, LTRA]),
     mcq(28, "A 29-year-old woman who is 24 weeks pregnant has well-controlled asthma on low-dose budesonide–formoterol maintenance and reliever therapy. She asks whether she should stop the inhaler to protect her baby. What is the best advice?",
         ["Continue her current ICS-containing inhaler throughout pregnancy",
          "Stop the inhaler and use salbutamol only when she is wheezy",
          "Switch to oral montelukast alone until after the delivery",
          "Stop all inhalers until delivery unless she needs admission",
          "Change to oral theophylline as a safer option for pregnancy"],
         "**หอบที่คุมไม่ได้อันตรายต่อทารกมากกว่ายา** — hypoxemia ของแม่ทำให้ทารกโตช้า คลอดก่อนกำหนด preeclampsia · ICS (โดยเฉพาะ **budesonide** ซึ่งมีข้อมูลมากที่สุด) และ formoterol ปลอดภัยในการตั้งครรภ์ · การหยุด ICS เพิ่มความเสี่ยง exacerbation · ติดตามทุก 4–6 สัปดาห์\n\n"
         "- \"salbutamol เดี่ยว\" — เสียการต้านการอักเสบ เสี่ยงกำเริบ และเป็นการรักษาที่ผิด\n"
         "- \"montelukast เดี่ยว\" — ได้ผลน้อยกว่า ICS\n- \"หยุดทุกอย่าง\" — อันตรายที่สุด\n"
         "- \"theophylline\" — ไม่แนะนำ ช่วงรักษาแคบ และไม่ปลอดภัยกว่า ICS",
         "ตั้งครรภ์: ห้ามหยุด ICS — คุมหืดดีคือปกป้องทารก", "Pregnancy", G("Chapter 6 — asthma in pregnancy"), BASE + [ICS, PK, PREG]),
     mcq(29, "A 20-year-old runner develops cough, chest tightness and wheeze about 5–10 minutes after finishing races on cold mornings; symptoms settle within an hour. Which mechanism best explains the bronchoconstriction?",
         ["Evaporative water loss raising airway surface osmolarity",
          "IgE-mediated reaction to pollen inhaled during running",
          "Lactic acid from muscle directly constricting the airways",
          "Vagal surge triggered by the post-exercise rise in heart rate",
          "Pulmonary venous congestion from exercise-induced ischaemia"],
         "หายใจเร็วแรงในอากาศเย็น/แห้ง → **น้ำระเหยจากของเหลวบนผิวเยื่อบุ** → **osmolarity สูงขึ้น** และเยื่อบุเย็นลง → mast cell และ eosinophil หลั่ง histamine/leukotriene → หลอดลมหดตัว สูงสุดหลังหยุดออกกำลัง 5–10 นาที · วินิจฉัยด้วย exercise challenge (FEV1 ลด > 10% และ > 200 mL) · ป้องกันด้วย warm-up และ ICS-formoterol (หรือ SABA) ก่อนออกกำลัง\n\n"
         "- \"IgE ต่อเกสร\" — เกิดได้ตามฤดู แต่จังหวะเวลาที่ผูกกับการวิ่งในอากาศเย็นบ่งกลไก osmotic\n"
         "- \"lactic acid\" — ไม่ทำให้หลอดลมหดตัวโดยตรง\n- \"vagal surge จากหัวใจเต้นเร็ว\" — ไม่ใช่กลไก\n"
         "- \"pulmonary venous congestion จากหัวใจขาดเลือด\" — ไม่เข้ากับวัยรุ่นสุขภาพดี",
         "EIB = osmotic/thermal trigger ของ mast cell", "Exercise-induced bronchoconstriction", G("Chapter 6 — exercise-induced bronchoconstriction"), BASE + [EXER, HYP])],
    BASE + [ADR, POLYP, PREG, PK, EXER, LTRA],
    src=SRC_G)

# ═════════════════════════════════════════════ 13
sec("chest-ast-13", "อ่านเพิ่มเติม (เกินระดับ NL) — severe asthma และ biologics",
    "ส่งต่อเมื่อคุมไม่ได้ที่ step 4–5 หลังแก้ทุกปัจจัย · T2 biomarker · omalizumab · mepolizumab/benralizumab · dupilumab · tezepelumab", 6,
RM + """

### เมื่อไหร่ควรนึกถึง severe asthma
คุมไม่ได้แม้ใช้ **ICS-LABA ขนาดสูง** (หรือ OCS ประจำ) หลังแก้ **ท่าพ่น adherence ตัวกระตุ้น และโรคร่วม** ครบแล้ว (หัวข้อ 8) → ส่งผู้เชี่ยวชาญประเมิน phenotype

### ประเมิน T2 (GINA severe asthma)
ถือว่ามี T2 ถ้ามีอย่างใดอย่างหนึ่ง (ขณะใช้ ICS ขนาดสูง): **blood eos ≥ 150/µL** · **FeNO ≥ 20 ppb** · sputum eos ≥ 2% · อาการผูกกับ allergen · ต้องใช้ OCS ประจำ · ตรวจซ้ำได้ถึง 3 ครั้ง (ก่อนลด OCS)

### Biologic — ไล่จากต้นทางไปปลายทาง (ตรงกับแผนภาพที่อาจารย์ให้จด หัวข้อ 2)
| ยา | เป้า | เหมาะกับ | หมายเหตุ |
|---|---|---|---|
| **Tezepelumab** | **TSLP** (alarmin ต้นทาง) | severe asthma ทั้ง T2-high และบางส่วนของ T2-low | ตัวเดียวที่ได้ผลแม้ biomarker ต่ำ |
| **Dupilumab** | **IL-4Rα** (บล็อกทั้ง IL-4 และ IL-13) | eos/FeNO สูง · ต้องใช้ OCS · มี CRSwNP หรือ atopic dermatitis ร่วม | eos ในเลือดอาจสูงขึ้นชั่วคราว |
| **Mepolizumab · Reslizumab** | **IL-5** | severe eosinophilic | ใช้ใน EGPA/CRSwNP ด้วย (mepolizumab) |
| **Benralizumab** | **IL-5Rα** → NK cell ทำลาย eosinophil (ADCC) | severe eosinophilic | eos ในเลือดแทบเป็นศูนย์ |
| **Omalizumab** | **IgE** ในเลือด (กันไม่ให้จับ FcεRI) | severe allergic asthma ที่มี sensitisation ชัด | ขนาดตาม IgE และน้ำหนักตัว · ระวัง anaphylaxis |

- อาจารย์: ปัจจุบันเน้นบล็อก "**ต้นทาง**" (TSLP, IL-4R) มากกว่า IgE อย่างเดียว · และระวังว่าการบล็อกทางหนึ่ง การอักเสบอาจหาทางอื่น
- ประเมินผลหลังใช้ ≥ 4 เดือน · เป้าคือลด exacerbation ลด/เลิก OCS และมุ่งสู่ remission
- ทางเลือกอื่นใน step 5 (ผู้เชี่ยวชาญ): azithromycin ระยะยาว (ผู้ใหญ่ ระวัง QT/ดื้อยา) · bronchial thermoplasty (หลักฐานจำกัด) · OCS ขนาดต่ำสุดเป็นทางสุดท้าย""",
    ["Severe asthma วินิจฉัยได้หลังแก้ท่าพ่น adherence ตัวกระตุ้น และโรคร่วมแล้วเท่านั้น",
     "T2 biomarker ใน severe asthma: eos ≥ 150 · FeNO ≥ 20 · allergen · ต้องใช้ OCS",
     "Omalizumab = IgE · mepolizumab/reslizumab = IL-5 · benralizumab = IL-5Rα · dupilumab = IL-4Rα · tezepelumab = TSLP",
     "Tezepelumab บล็อก alarmin ต้นทาง — ใช้ได้แม้ biomarker ต่ำ"],
    [mcq(30, "A 50-year-old man has severe eosinophilic asthma (blood eosinophils 900 cells/µL) requiring frequent oral corticosteroid courses despite optimised high-dose ICS–LABA, good technique and treated comorbidities. His specialist chooses a monoclonal antibody that binds interleukin-5 itself. Which drug is this?",
         ["Mepolizumab", "Omalizumab", "Dupilumab", "Tezepelumab", "Benralizumab"],
         "**Mepolizumab** (และ reslizumab) จับ **IL-5** โดยตรง → eosinophil ถูกสร้างและอยู่รอดน้อยลง → exacerbation และความต้องการ OCS ลดลงใน severe eosinophilic asthma\n\n"
         "- \"Omalizumab\" — จับ **IgE**\n- \"Dupilumab\" — บล็อก **IL-4 receptor α** (IL-4 และ IL-13)\n"
         "- \"Tezepelumab\" — จับ **TSLP**\n- \"Benralizumab\" — จับ **IL-5 receptor α** บน eosinophil (ไม่ใช่ตัว IL-5) แล้วให้ NK cell ทำลาย",
         "IL-5 ตัวยา = mepolizumab/reslizumab · IL-5R = benralizumab", "Biologics", G("Severe asthma guide — biologic therapy"), BASE + [IMMOD])],
    BASE + [IMMOD, HYP],
    src=SRC_G)


# ═════════════════════════════════════════════ MEQ / OSCE
MEQ = [{"id": "CH-AST-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
        "topic": "Uncontrolled asthma on SABA alone — diagnosis, mechanism, control assessment and GINA Track 1 treatment",
        "nl": [AST, ASTB, SPIRO, SPIROB, BD, ICS, AE, RHIN], "ref": G("Chapters 1–5") + [CLS + "ประเด็นที่อาจารย์เน้น"],
        "vignette": "หญิงไทยอายุ 24 ปี พนักงานออฟฟิศ มา OPD ด้วยไอและหายใจมีเสียงหวีดเป็น ๆ หาย ๆ มา 8 เดือน มักเป็นช่วงตี 3–5 ต้องตื่นมาพ่นยา 2–3 คืนต่อสัปดาห์ เป็นมากขึ้นเวลาเป็นหวัดหรือทำความสะอาดห้องที่มีฝุ่น ช่วงกลางวันมีอาการ 4 วันต่อสัปดาห์ เดินขึ้นบันไดที่ทำงานต้องหยุดพัก\n"
                    "ซื้อ salbutamol MDI พ่นเองจากร้านยา ใช้หมดเดือนละ 1 หลอด ไม่เคยใช้ยาอื่น · 3 เดือนก่อนไป ER พ่นยา 3 ครั้งแล้วกลับบ้าน\n"
                    "ประวัติ: จามคัดจมูกน้ำมูกใสทุกเช้าตั้งแต่เด็ก มารดาเป็นโรคหืด · ไม่สูบบุหรี่ เลี้ยงแมว 1 ตัวในห้องนอน\n"
                    "PE: BMI 22 · RR 18/min · SpO2 98% room air · เยื่อบุจมูกซีดบวม · ปอดได้ยิน end-expiratory wheeze เล็กน้อยทั้งสองข้าง ไม่มี crepitation · หัวใจปกติ ไม่มีขาบวม\n"
                    "Spirometry (ก่อน → 15 นาทีหลัง salbutamol 400 mcg): FEV1 2.30 → 2.65 L (FEV1 ก่อนยา 74% predicted) · FVC 3.40 → 3.55 L · FEV1/FVC 0.68 → 0.75\n"
                    "CBC: eosinophil 520 cells/µL · FeNO 58 ppb",
        "questions": [
            {"q": "1. จงแปลผล spirometry พร้อมแสดงการคำนวณ และให้การวินิจฉัย (3 คะแนน)",
             "a": "- FEV1 เพิ่ม **2.65 − 2.30 = 0.35 L = 350 mL** · **0.35 ÷ 2.30 × 100 = 15.2%** → เกิน **12% และ 200 mL** = bronchodilator responsiveness บวก = **variable expiratory airflow limitation** (1.5)\n"
                  "- **ไม่ต้องใช้** FEV1/FVC < 0.70 เป็นเกณฑ์ (อาจารย์เน้น) — ratio หลังยา 0.75 ก็ไม่ได้ตัดโรค (0.5)\n"
                  "- วินิจฉัย **asthma, allergic (T2-high) phenotype** ร่วมกับ **allergic rhinitis** — อาการแปรปรวน กลางคืน ตัวกระตุ้นไวรัส/ฝุ่น/แมว ประวัติครอบครัว eos 520 FeNO 58 สนับสนุน (1)"},
            {"q": "2. จงอธิบายกลไกที่ทำให้ผู้ป่วยมีอาการช่วงเช้ามืด และกลไกการเกิดเสียง wheeze (3 คะแนน)",
             "a": "- **เช้ามืด**: cortisol และ adrenaline ต่ำสุดราวตี 4 · vagal tone สูงตอนนอน (acetylcholine → M3 → หลอดลมหดตัว) · หลอดลมเย็นลง · สัมผัสแมว/ไรฝุ่นในห้องนอนตลอดคืน → late-phase inflammation (1.5)\n"
                  "- **wheeze**: Th2 → IL-4 (IgE บน mast cell) IL-5 (eosinophil) IL-13 (เมือก AHR) → กล้ามเนื้อเรียบหดตัว เยื่อบุบวม เมือก → หลอดลมแคบ · ตอนหายใจออกความดันในช่องอกกดหลอดลมที่แคบอยู่แล้ว ลมเร็วผ่านช่องแคบทำให้ผนังสั่น (1.5)"},
            {"q": "3. จงประเมิน symptom control และปัจจัยเสี่ยงต่อ exacerbation ของผู้ป่วยรายนี้ (3 คะแนน)",
             "a": "- 4 คำถามใน 4 สัปดาห์: อาการกลางวัน > 2/สัปดาห์ ✓ · ตื่นกลางคืน ✓ · ใช้ยาบรรเทา > 2/สัปดาห์ ✓ · กิจกรรมจำกัด ✓ = **4/4 = uncontrolled** (1.5)\n"
                  "- ปัจจัยเสี่ยง: **ไม่ได้ ICS** · **ใช้ SABA เดี่ยว ~1 หลอด/เดือน** (≥ 12 หลอด/ปี — สัมพันธ์กับการตาย) · **เคยไป ER ใน 12 เดือน** · FEV1 74% · eos/FeNO สูง · สัมผัส allergen ต่อเนื่อง (แมวในห้องนอน) (1.5)"},
            {"q": "4. จงให้การรักษาด้วยยาตาม GINA Track 1 ระบุชื่อยา ขนาด วิธีใช้ และเหตุผลที่ไม่ให้ salbutamol ต่อเดี่ยว ๆ (4 คะแนน)",
             "a": "- อาการเกือบทุกวัน + ตื่นกลางคืน ≥ 1/สัปดาห์ + FEV1 ต่ำ → เริ่ม **step 3: budesonide-formoterol 200/6 MART ขนาดต่ำ** — 1 สูดเช้า–เย็น + 1 สูดเมื่อมีอาการ (ยังไม่ถึง step 4 เพราะอาการ 4 วัน/สัปดาห์ ไม่ใช่ทุกวัน และครั้งนี้ไม่ได้มาด้วย exacerbation) · รวมไม่เกิน 12 สูด/วัน · **หยุด salbutamol แยก** (1.5)\n"
                  "- เหตุผล: SABA แค่คลายกล้ามเนื้อ **ปิดบังอาการ** การอักเสบยังเดินหน้า · β2 receptor downregulation · ใช้มากสัมพันธ์กับ exacerbation และการตาย — **อาจารย์เน้น** \"ทุกครั้งที่หอบต้องได้ ICS คู่เสมอ\" (AIR) · formoterol ออกฤทธิ์เร็วจึงใช้บรรเทาได้ (1.5)\n"
                  "- สอนท่าพ่น DPI (สูดแรงเร็ว ห้ามเป่าเข้า) + บ้วนปาก · action plan · รักษา allergic rhinitis ด้วย intranasal steroid · นัด 1–3 เดือน (1)"},
            {"q": "5. จงบอกการดูแลที่ไม่ใช้ยาและการติดตามผล รวมถึงเมื่อไหร่จึงลดยาได้ (2 คะแนน)",
             "a": "- เอาแมวออกจากห้องนอน ลดฝุ่น · หลีกเลี่ยงควันบุหรี่/PM2.5 · วัคซีน influenza ทุกปี · ออกกำลังสม่ำเสมอ (1)\n"
                  "- นัด 1–3 เดือน ประเมิน 4 คำถาม ท่าพ่น adherence · ถ้าคุมได้ดีต่อเนื่อง **3 เดือน** จึง step down ทีละขั้น **ไม่หยุด ICS** · ถ้าตั้งครรภ์ห้ามหยุดยา นัดทุก 4–6 สัปดาห์ (1)"}]}]

OSCE = [{"id": "CH-AST-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
         "topic": "OSCE – Counselling a patient to start budesonide–formoterol MART with a dry-powder inhaler and a written action plan",
         "station": "OSCE (สอนผู้ป่วย) 7 นาที",
         "nl": [AST, ASTB, ICS, BD], "ref": G("Box 4-8 MART · Chapter 5 inhaler skills"),
         "instruction": "หญิงอายุ 24 ปี (ผู้ป่วยมาตรฐาน) เพิ่งได้รับการวินิจฉัย asthma ที่คุมไม่ได้ เดิมใช้ salbutamol MDI ซื้อเองเดือนละ 1 หลอด แพทย์สั่ง **budesonide-formoterol 200/6 mcg ชนิด Turbuhaler แบบ MART (1 สูดเช้า–เย็น + 1 สูดเมื่อมีอาการ)**\n\n"
                        "**จงอธิบายยาใหม่ สอนวิธีใช้ Turbuhaler ให้ถูกต้อง และให้คำแนะนำเมื่ออาการแย่ลง ภายใน 7 นาที** · มีอุปกรณ์ฝึก (placebo Turbuhaler) วางไว้ให้",
         "answer": "**เกณฑ์ให้คะแนน (18 คะแนน)**\n\n| ข้อ | สิ่งที่ต้องทำ | คะแนน |\n|---|---|---|\n"
                   "| 1 | แนะนำตัว ยืนยันตัวผู้ป่วย ถามความเข้าใจเดิมเรื่องโรคและยาพ่น | 1 |\n"
                   "| 2 | อธิบายโรคด้วยภาษาง่าย: หลอดลม **อักเสบเรื้อรัง** ไวต่อสิ่งกระตุ้น — salbutamol แค่ขยายหลอดลมชั่วคราว ไม่รักษาการอักเสบ ใช้เดี่ยว ๆ บ่อยอันตราย | 2 |\n"
                   "| 3 | อธิบายยาใหม่: มี **ยาลดการอักเสบ (budesonide) + ยาขยายหลอดลมที่ออกฤทธิ์เร็วและนาน (formoterol)** ในหลอดเดียว → ใช้ทั้งเป็นยาประจำและยาเวลามีอาการ | 2 |\n"
                   "| 4 | บอกวิธีใช้แบบ MART: **1 สูดเช้า–เย็นทุกวันแม้ไม่มีอาการ** + **1 สูดเมื่อมีอาการ** (ซ้ำได้ถ้ายังไม่ดีขึ้นในไม่กี่นาที) · **รวมไม่เกิน 12 สูด/วัน** · ไม่ต้องใช้ salbutamol แยกอีก | 2 |\n"
                   "| 5 | เตรียมยา: เปิดฝา **ถือตั้งตรง บิดฐานไปจนสุดแล้วบิดกลับจนได้ยินคลิก** · **ไม่เขย่า** | 2 |\n"
                   "| 6 | หายใจออกให้สุด **นอกอุปกรณ์ (ห้ามเป่าเข้า)** → อมปากกระบอกให้สนิท **สูดแรง เร็ว และลึก** → กลั้นหายใจ ~10 วินาที | 2 |\n"
                   "| 7 | ปิดฝา **บ้วนปาก กลั้วคอ** (ลดเชื้อราในปาก เสียงแหบ) · ดูตัวนับยา | 1 |\n"
                   "| 8 | **ให้ผู้ป่วยสาธิตกลับ (teach-back)** และแก้จุดผิดจนถูก | 2 |\n"
                   "| 9 | **Action plan**: ถ้าต้องสูดเพิ่มหลายครั้งติดกัน 2–3 วัน หรือตื่นกลางคืนบ่อยขึ้น → ติดต่อแพทย์ · **พูดได้เป็นคำ ๆ เหนื่อยมาก ยาไม่ช่วย ปากเขียว → มาโรงพยาบาลทันที** | 2 |\n"
                   "| 10 | ลดตัวกระตุ้น (แมวนอกห้องนอน ฝุ่น ควัน) · นัด 1–3 เดือน นำยามาด้วย · เปิดโอกาสถาม | 2 |\n\n"
                   "**จุดตาย**: สอนให้เขย่า/เป่าลมเข้า Turbuhaler · สอนให้ใช้ salbutamol เดี่ยวต่อเป็นยาบรรเทา · บอกให้ใช้ยาเฉพาะตอนมีอาการทั้งที่สั่ง MART · ไม่ให้ผู้ป่วยสาธิตกลับ\n\n"
                   "**เหตุผล**: DPI ต้องใช้แรงสูดทำให้ผงยาแตกเป็นอนุภาคเล็กพอจะลงหลอดลม — ต่างจาก pMDI ที่ต้องสูดช้า · MART ลด severe exacerbation เมื่อเทียบกับการใช้ SABA เป็น reliever (GINA)"}]

LECTURE = {
 "lec": LEC, "date": "อ. 3 พ.ย.", "title": "Asthma — วินิจฉัยและรักษาโรคหืด (GINA)",
 "subtitle": "คาบ active learning (เสียงบันทึก Plaud · ไม่มีไฟล์สไลด์) — หัวข้อ 1–12 ระดับ NL: นิยาม กลไก T2 อาการ วินิจฉัย (12% + 200 mL ไม่มีเกณฑ์ ratio) biomarker แยกโรค ยา Track 1/MART ติดตามผล ท่าพ่น exacerbation AERD ตั้งครรภ์ EIB · หัวข้อ 13 อ่านเพิ่มเติม (biologics)",
 "objectives": [
   "บอกนิยาม asthma ตาม GINA (อาการแปรปรวน + variable expiratory airflow limitation) และแยก phenotype กับ endotype (T2-high/T2-low)",
   "อธิบายการอักเสบ T2 (IL-4/IL-5/IL-13, IgE–mast cell, eosinophil, alarmin–ILC2) และ remodeling แล้วใช้อธิบาย wheeze อาการกลางคืน silent chest และ pulsus paradoxus",
   "แปลผล bronchodilator responsiveness (> 12% และ > 200 mL) PEF variability challenge test และ ICS trial — โดยไม่ใช้เกณฑ์ FEV1/FVC < 0.70",
   "แปลผล FeNO/eosinophil/IgE อย่างถูกต้อง และแยก asthma จาก COPD, inducible laryngeal obstruction, heart failure, วัณโรค",
   "อธิบายกลไกและผลข้างเคียงของ ICS, SABA, formoterol, salmeterol, LAMA, LTRA, OCS และเหตุผลที่ห้าม SABA เดี่ยว/LABA เดี่ยว",
   "เลือกขั้นการรักษาเริ่มต้นตาม GINA Track 1 และสอน MART/AIR ได้",
   "ประเมิน symptom control 4 ข้อ ความเสี่ยงในอนาคต step up/down แยก difficult-to-treat กับ severe asthma และรู้เกณฑ์ remission",
   "สอนการใช้ pMDI + spacer และ DPI ได้ถูกต้อง พร้อม action plan",
   "ประเมินความรุนแรงของ exacerbation รักษาตามระดับ (O2, SABA, ipratropium, steroid, MgSO4) บอกข้อบ่งชี้ ICU และเกณฑ์จำหน่าย",
   "ดูแล AERD, asthma ในหญิงตั้งครรภ์ และ exercise-induced bronchoconstriction"],
 "nlGap": "ตรงกับเกณฑ์ฯ แพทยสภา: asthma (`นล. 2.3.10(1)` **กลุ่ม 2 — ดูแลเองได้**, `B6.2.2(2)`) · asthma exacerbation (`นล. 2.2.11`) · acute respiratory failure (`2.2.9`, `B6.2.5(1)`) · spirometry/PEF (`3.3.18`, `B6.3(3)`) · ABG (`3.3.17`) · ยาขยายหลอดลม/ICS/LTRA (`B6.4(4)`, `B6.4(5)`, `B6.4(6)`) · hypersensitivity (`B1.4.11`) · allergic rhinitis (`2.3.10(8)`) · "
          "**ไม่มีรหัสเฉพาะ** สำหรับ AERD, exercise-induced bronchoconstriction, inducible laryngeal obstruction, biologics และ severe asthma (หัวข้อ 13 เกินระดับ NL) — อิงแนวทางด้านล่าง · "
          "**คาบนี้ไม่มีไฟล์สไลด์** (ค้น Drive โฟลเดอร์ lecture แล้วไม่พบ) — เนื้อหาเรียบเรียงจากเสียงบันทึก Plaud ของคาบ active learning (นักศึกษานำเสนอ อาจารย์แทรกแก้) ร่วมกับ GINA 2024/2025 · ตัวเลขในตาราง ขนาดยา และหัวข้อ MgSO4/ICU/AERD/ตั้งครรภ์/EIB/biologics อิง GINA และระบุไว้ในบทเรียน",
 "guidelines": [
   "**GINA 2024 / 2025 — Global Strategy for Asthma Management and Prevention** · แหล่งหลัก (Track 1/2, เกณฑ์วินิจฉัย, การรักษา exacerbation)",
   "**GINA Difficult-to-treat & Severe Asthma Guide (2024)** — นิยาม difficult/severe, T2 biomarker, biologics",
   "**BTS/SIGN British guideline on the management of asthma (2019)** — เกณฑ์ life-threatening (PEF < 33%, SpO2 < 92%, PaCO2 ปกติ) ที่ข้อสอบ Ward Drill ใช้",
   "**ERS 2022 guideline on the diagnosis of asthma in adults** และ **BTS/NICE/SIGN 2024** — เกณฑ์ PEF variability ≥ 20%",
   "**ATS 2011 Clinical Practice Guideline: interpretation of FeNO** — จุดตัด < 25 / > 50 ppb",
   "**GOLD 2026** — ไม่ใช้คำ asthma–COPD overlap (ดูคาบ 37 หัวข้อ 6)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ═════════════════════════════════════════════ ประกอบ: ภาพเคลื่อนไหว + หลักจำ
secs = {s_["id"]: s_ for s_ in S}
for it in AN.ITEMS:
    s_ = secs[it["sec"]]
    a = it["anim"]
    s_.setdefault("anims", {})[a["key"]] = {k: a[k] for k in ("title", "svg", "steps")}
    s_["md"], ok = _insert_marker(s_["md"], it.get("after", ""), "[[anim:%s]]" % a["key"])
    assert ok, ("ไม่พบหัวข้อ", it["sec"], it.get("after"))
for m in AN.MNEM:
    secs[m["sec"]].setdefault("mnem", []).append({x: m[x] for x in ("name", "what", "lines", "note", "src") if m.get(x)})

# ═════════════════════════════════════════════ กระจายตำแหน่งคำตอบ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ข้อที่ตัวเลือกเป็นตัวเลขคงไว้
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it.pop("_keep", False):
            continue
        assert it["answer"] == 0, it["id"]
        tgt = [2, 4, 1, 3, 0][_slot % 5]; _slot += 1
        ch = it["choices"]; ch[0], ch[tgt] = ch[tgt], ch[0]; it["answer"] = tgt
# ข้อ 8 (ตัวเลข): คำตอบที่ถูก 16% อยู่ index 0 → ย้ายไป index 3 แบบเรียงตัวเลขใหม่
for s_ in S:
    for it in s_["items"]:
        if it["id"] == "CH-AST-MCQ-08":
            it["choices"] = ["8%", "15%", "16%", "18%", "60%"]
            it["answer"] = 2

# ═════════════════════════════════════════════ ตรวจ marker ↔ ของ
for s_ in S:
    for kind, field in (("fig", "figs"), ("anim", "anims")):
        used = re.findall(r"^\s*\[\[%s:([\w-]+)\]\]\s*$" % kind, s_["md"], re.M)
        have = s_.get(field, {})
        assert set(used) == set(have), (s_["id"], kind, set(used) ^ set(have))
        assert len(used) == len(set(used)), (s_["id"], kind)
    assert "```" not in s_["md"], s_["id"]

# ═════════════════════════════════════════════ เขียน chest.json (ต่อท้าย ไม่แตะคาบอื่น) แล้วผูกข้อคลัง Ward Drill คาบ 37 (เฉพาะ asthma)
path = os.path.join(BUILD, "data", SET + ".json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
BANK_MAP = {
    "chest-ast-03": ["CH-OLD-53"],
    "chest-ast-04": ["CH-OLD-55"],
    "chest-ast-07": ["CH-OLD-54"],
    "chest-ast-10": ["CH-MCQ-36"],
    "chest-ast-11": ["CH-OLD-52"],
}
added = link(SET, LEC, BANK_MAP, meq=["CH-MEQ-05"], osce=[])

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

# ═════════════════════════════════════════════ index.json: lectureCount + intro/howto ของชุด chest (แทรกต่อท้าย · รันซ้ำได้)
AST_INTRO = (" · ต่อด้วยคาบ **Asthma (อ. 3 พ.ย. · active learning)** เรียบเรียงจากเสียงบันทึกในห้องร่วมกับ **GINA 2024/2025** — "
             "กลไก T2 · การวินิจฉัย (> 12% และ > 200 mL ไม่มีเกณฑ์ ratio) · Track 1 ICS-formoterol/MART · exacerbation · AERD ตั้งครรภ์ EIB พร้อมภาพเคลื่อนไหวและหลักจำ")
AST_HOWTO = (" · คาบ **Asthma** เรียนต่อจากคาบ 37 COPD ได้ทันที — เน้นที่อาจารย์ย้ำ: **ไม่มีเกณฑ์ FEV1/FVC < 0.70 ใน asthma**, "
             "**12% และ 200 mL ต้องทั้งคู่**, **ห้าม SABA เดี่ยว (ทุกครั้งที่หอบต้องได้ ICS)**, **Track 1 ต้องเป็น formoterol**, difficult-to-treat vs severe และ remission 4 ข้อ")
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] != SET:
        continue
    m["lectureCount"] = len(data)
    if "คาบ **Asthma (อ. 3 พ.ย." not in m["intro"]:
        anchor = "หัวข้อ 12–14 เป็น \"อ่านเพิ่มเติม\""
        assert anchor in m["intro"], "intro ของ chest เปลี่ยนไปจากที่สคริปต์รู้จัก"
        m["intro"] = m["intro"].replace(anchor, anchor + AST_INTRO, 1)
    if "คาบ **Asthma** เรียนต่อจากคาบ 37" not in m["howto"]:
        anchor = "· หัวข้อ \"อ่านเพิ่มเติม\" ข้ามได้ถ้าเตรียมสอบ NL"
        assert anchor in m["howto"], "howto ของ chest เปลี่ยนไปจากที่สคริปต์รู้จัก"
        m["howto"] = m["howto"].replace(anchor, anchor + AST_HOWTO, 1)
        old = "คาบที่เหลือของชุด Chest (ส่วน pneumonia/asthma ของคาบ 37) ยังไม่ได้ทำบทเรียน"
        if old in m["howto"]:
            m["howto"] = m["howto"].replace(old, "คาบที่เหลือของชุด Chest (ส่วน pneumonia ของคาบ 37) ยังไม่ได้ทำบทเรียน")
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

from collections import Counter
new = [i for s_ in S for i in s_["items"] if i["id"].startswith("CH-AST")]
print("sections %d (NL %d + อ่านเพิ่มเติม %d) | ข้อใหม่ %d + คลัง %d | meq %d | osce %d | figs %d | anims %d | mnem %d | nl %d" % (
    len(S), sum(1 for s_ in S if not s_["title"].startswith("อ่านเพิ่มเติม")), sum(1 for s_ in S if s_["title"].startswith("อ่านเพิ่มเติม")),
    len(new), added, len(L["meq"]), len(L["osce"]), sum(len(s_.get("figs") or {}) for s_ in S),
    sum(len(s_.get("anims") or {}) for s_ in S), sum(len(s_.get("mnem") or []) for s_ in S), len(codes)))
print("ตำแหน่งคำตอบข้อใหม่:", dict(sorted(Counter(i["answer"] for i in new).items())))
print("%s.json มี %d คาบ: %s" % (SET, len(data), [l["lec"] for l in data]))
