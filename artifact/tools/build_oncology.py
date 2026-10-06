#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""General oncology (พญ.ปิยวรรณ เทียนชัยอนันต์) → data/hemonc.json (ชุดใหม่ Heme/Onc)
ต้นฉบับ: Drive 1nzh5iBJ_uJ5uP9_q2zDlAxQ-Opw5xRJg · บรรยาย จ. 2 พ.ย. 2569 · โน้ต slides/oncology_notes.md
ผูกข้อ Mock หมวด M02 Oncology ที่ตรงเรื่อง · อัปเดต: GLOBOCAN 2022 · Hallmarks 2011/2022 · ECOG ·
ASCO/ESMO irAE · NCCN/ESMO breast cancer (CDK4/6, KEYNOTE-522) · USPSTF 2024"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_mock import link_mock

SET, LEC = "hemonc", "2/11"
NLN = ["B1.6.4"]
SRC = "สไลด์ พญ.ปิยวรรณ — General oncology"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None, src=SRC):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": src,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "HON-ONC-MCQ-%02d" % n
R = lambda p: ["สไลด์ พญ.ปิยวรรณ — " + p]

# ───────────────────────────── 1
EPI = ["B1.6.4(4)"]
sec("hon-onc-01", "ระบาดวิทยาของมะเร็ง — โลกและประเทศไทย",
    "GLOBOCAN: ปอดและเต้านมพบบ่อยที่สุดในโลก · ไทย: ชายมะเร็งตับและท่อน้ำดีนำ หญิงมะเร็งเต้านมนำ · HBV และพยาธิใบไม้ตับ", 7,
"""### ภาพรวมในสไลด์
สไลด์ใช้กราฟ **GLOBOCAN 2012** (อุบัติการณ์แยกชายหญิง แนวโน้มมะเร็งเต้านมและลำไส้ใหญ่เพิ่มขึ้น) และ **มะเร็งที่พบบ่อยในไทย 2544–2546** ซึ่งเป็นภาพ — ตัวเลขด้านล่างจึงเป็น **ข้อมูลล่าสุดที่ไม่ได้มาจากสไลด์**

### GLOBOCAN 2022 (IARC 2024 — ไม่ได้มาจากสไลด์)
| อันดับ (ทั้งโลก ทั้งสองเพศ) | อุบัติการณ์ | การตาย |
|---|---|---|
| 1 | **มะเร็งปอด** (~12%) | **มะเร็งปอด** (~19%) |
| 2 | **มะเร็งเต้านมหญิง** (~12%) | มะเร็งลำไส้ใหญ่และทวารหนัก |
| 3 | มะเร็งลำไส้ใหญ่และทวารหนัก | มะเร็งตับ |
| 4 | มะเร็งต่อมลูกหมาก | มะเร็งเต้านม |
| 5 | มะเร็งกระเพาะ | มะเร็งกระเพาะ |
- ปี 2022 มีผู้ป่วยใหม่ราว **20 ล้านราย** ตาย **9.7 ล้านราย** · ราว 1 ใน 5 คนจะเป็นมะเร็งในช่วงชีวิต

### ประเทศไทย (ทะเบียนมะเร็ง — ไม่ได้มาจากสไลด์)
| **ชาย** | **หญิง** |
|---|---|
| **มะเร็งตับและท่อน้ำดีในตับ** · ปอด · ลำไส้ใหญ่ · ต่อมลูกหมาก | **มะเร็งเต้านม** · ลำไส้ใหญ่ · ตับและท่อน้ำดี · ปอด · **ปากมดลูก** |
- **มะเร็งตับ (HCC)** สัมพันธ์กับ **ไวรัสตับอักเสบบี** — สาเหตุนำของมะเร็งตับในเอเชียและทั่วโลก
- **มะเร็งท่อน้ำดี (cholangiocarcinoma)** สูงที่สุดในโลกที่ **ภาคตะวันออกเฉียงเหนือ** — จาก **พยาธิใบไม้ตับ (Opisthorchis viverrini)** จากการกินปลาดิบ (ปลาร้า ก้อยปลา)
- มะเร็งปากมดลูกลดลงจากการคัดกรองและวัคซีน HPV

### ป้องกันได้ (ภาพรวม)
บุหรี่ (ปอด ศีรษะและคอ หลอดอาหาร กระเพาะปัสสาวะ) · **วัคซีน HBV และ HPV** · เหล้า · อ้วน · ไม่กินปลาดิบ · คัดกรองเต้านม ปากมดลูก ลำไส้ใหญ่
""",
    ["โลก: ปอดและเต้านมพบบ่อยสุด · ปอดตายมากสุด",
     "ไทย: ชายมะเร็งตับ/ท่อน้ำดีนำ · หญิงมะเร็งเต้านมนำ",
     "HBV = สาเหตุนำของ HCC · พยาธิใบไม้ตับ = cholangiocarcinoma ภาคอีสาน"],
    [mcq(N(1), "A 52-year-old farmer from north-eastern Thailand who regularly eats raw fermented fish presents with painless jaundice and a hilar biliary mass. Which aetiological factor is most strongly associated with this cancer in this region?",
         ["Hepatitis C virus", "Opisthorchis viverrini infection", "Aflatoxin only", "Human papillomavirus", "Epstein–Barr virus"], 1,
         "ภาคอีสานของไทยมีอุบัติการณ์ **cholangiocarcinoma สูงที่สุดในโลก** สาเหตุหลักคือ **พยาธิใบไม้ตับ Opisthorchis viverrini** ที่ติดจาก **การกินปลาน้ำจืดดิบหรือสุกไม่ทั่ว** (ก้อยปลา ปลาร้า) — พยาธิอยู่ในท่อน้ำดีทำให้อักเสบเรื้อรังและเกิดสาร N-nitroso\n\nHBV และ aflatoxin สัมพันธ์กับ **HCC** มากกว่า\n\n*(ข้อมูลระบาดวิทยาไทย ไม่ได้มาจากสไลด์)*",
         "ปลาดิบ + อีสาน + ก้อนที่ขั้วตับ = cholangiocarcinoma จากพยาธิใบไม้ตับ", "Cancer epidemiology in Thailand", ["Thai Cancer Registry · IARC"], EPI + ["B8.2.4-3(2)"]),
    ], EPI, SRC + " · GLOBOCAN 2022")

# ───────────────────────────── 2
AIM = ["B1.7.3", "B1.6.4(2)"]
sec("hon-onc-02", "เป้าหมายการรักษา — หายขาดหรือประคับประคอง",
    "ระยะแรก: หายขาด ผ่าตัด · neoadjuvant ลดขนาด · adjuvant กำจัด micrometastasis · ระยะลุกลาม: ยืดชีวิตพร้อมคุณภาพชีวิต · ตัวอย่างมะเร็งลำไส้ใหญ่", 8,
"""### ชั่งประโยชน์กับความเสี่ยง (สไลด์)
การรักษามะเร็งทุกครั้งต้องดู **ทั้งผู้ป่วยและตัวมะเร็ง** แล้วตั้ง **เป้าหมาย (aim of treatment)** ก่อนเลือกวิธี

| | **ระยะแรก (early stage)** | **ระยะลุกลาม (advanced/metastatic)** |
|---|---|---|
| เป้าหมายสูงสุด | **หายขาด (cure)** | **ยืดชีวิตพร้อมคุณภาพชีวิตที่ดี** |
| การรักษาหลัก | **ผ่าตัดเพื่อหายขาด (definitive)** | **เคมีบำบัด/รังสีรักษาแบบประคับประคอง (palliative)** |
| เสริม | **Neoadjuvant** (ก่อนผ่าตัด) — **ลดขนาดก้อน** · **Adjuvant** (หลังผ่าตัด) — **ยืด DFS/OS** | ควบคุมอาการ · ยืด PFS/OS · **เลือกยาที่ผลข้างเคียงยอมรับได้** |

**Adjuvant ทำงานอย่างไร** — หลังผ่าตัดหมดที่ตาเห็น อาจยังมี **micrometastasis** ที่ตรวจไม่พบ → ยาเคมีกำจัดเพื่อ **ลดการกลับเป็นซ้ำ** และเพิ่มโอกาสหายขาด

### ตัวอย่าง: มะเร็งลำไส้ใหญ่ระยะแรก (สไลด์)
| ระยะ | ผ่าตัดอย่างเดียว — รอด 5 ปี |
|---|---|
| **I–II** | **~85%** |
| **III (มีต่อมน้ำเหลือง)** | **30–50%** |
- **Adjuvant chemotherapy ใน stage III** — สูตรที่มี **5-FU** เพิ่มการรอด 5 ปี **10–20%** · **เพิ่ม oxaliplatin (FOLFOX/CAPOX)** เพิ่มอีก **~5%** (รอด 6 ปี)
- ระยะลุกลาม (สไลด์): ยาเคมีและยามุ่งเป้าหลายสายต่อกัน ยืดการรอดจากไม่กี่เดือนเป็น **มากกว่า 2–3 ปี** แต่ส่วนใหญ่ไม่หายขาด *(ยกเว้นบางรายที่แพร่ไปตับ/ปอดจำนวนน้อยและผ่าตัดออกได้)*

### คำศัพท์
**DFS** = disease-free survival · **PFS** = progression-free survival · **OS** = overall survival · **Response rate** = ก้อนยุบตามเกณฑ์ — **ตอบสนองดีไม่จำเป็นต้องอยู่นานขึ้นเสมอ**
""",
    ["ระยะแรก: cure ด้วยผ่าตัด · ระยะลุกลาม: ยืดชีวิต + คุณภาพชีวิต",
     "Neoadjuvant ลดขนาดก่อนผ่าตัด · adjuvant กำจัด micrometastasis",
     "มะเร็งลำไส้ stage III: 5-FU +10–20% · + oxaliplatin +5%",
     "Response rate ไม่เท่ากับ OS"],
    [mcq(N(2), "A 58-year-old man has a completely resected stage III colon adenocarcinoma (3 of 14 nodes positive). What is the main purpose of offering him oxaliplatin plus fluoropyrimidine chemotherapy now?",
         ["To shrink the primary tumour before surgery", "To eradicate micrometastatic disease and improve disease-free and overall survival", "Palliation of symptoms",
          "To treat known liver metastases", "To reduce surgical complications"], 1,
         "นี่คือ **adjuvant chemotherapy** — หลังผ่าตัดหมด แต่มะเร็งที่มีต่อมน้ำเหลืองบวกมีโอกาสเหลือ **micrometastasis** สูง (ผ่าตัดอย่างเดียวรอด 5 ปีเพียง 30–50%)\n\nสไลด์: 5-FU เพิ่มการรอด **10–20%** และ **oxaliplatin เพิ่มอีก ~5%** · การลดขนาดก่อนผ่าตัดคือ **neoadjuvant**",
         "Adjuvant = กำจัด micrometastasis หลังผ่าตัด", "Aims of treatment", R("Example: early stage colon cancer"), AIM + ["B8.2.4-3(1)"]),
    ], AIM)

# ───────────────────────────── 3
PS = ["B1.7.3", "B1.6.4(2)"]
sec("hon-onc-03", "ปัจจัยของผู้ป่วยและของมะเร็ง — performance status",
    "Karnofsky 100–0 · ECOG 0–4 · อายุตามการทำงานสำคัญกว่าอายุจริง · ระยะ grade Ki-67 · มะเร็งที่ไวรังสี seminoma lymphoma SCC · predictive marker HER2 KRAS EGFR", 9,
"""### ปัจจัยของผู้ป่วย (สไลด์)
- **Performance status** — ตัวทำนายสำคัญที่สุดว่าทนยาเคมีได้และได้ประโยชน์หรือไม่
- โรคร่วม (ความดัน เบาหวาน) · สภาพทั่วไป (เบื่ออาหาร น้ำหนักลด ปวด)
- **อายุตามการทำงาน (functional age) สำคัญกว่าอายุตามปฏิทิน**
- เศรษฐานะ · ความตั้งใจของผู้ป่วยและผู้ดูแล · สภาพจิตใจ · ระบบช่วยเหลือ

### Karnofsky Performance Status (สไลด์)
| KPS | ความสามารถ | กลุ่ม |
|---|---|---|
| **100** | ปกติ ไม่มีอาการ | **ทำกิจวัตรและทำงานได้ ไม่ต้องดูแลพิเศษ** |
| 90 | ทำกิจวัตรปกติได้ อาการเล็กน้อย | |
| 80 | ทำได้แต่ต้องออกแรง | |
| **70** | ดูแลตัวเองได้ ทำงานไม่ได้ | **ทำงานไม่ได้ อยู่บ้านดูแลตัวเองได้เป็นส่วนใหญ่** |
| 60 | ต้องมีคนช่วยบางครั้ง | |
| 50 | ต้องมีคนช่วยมาก พบแพทย์บ่อย | |
| **40** | พิการ ต้องดูแลพิเศษ | **ดูแลตัวเองไม่ได้ ต้องดูแลแบบโรงพยาบาล** |
| 30 | พิการรุนแรง ควรนอนโรงพยาบาล | |
| 20 | ป่วยหนักมาก ต้องรักษาประคับประคองเต็มที่ | |
| 10 | ใกล้ตาย | |
| 0 | เสียชีวิต | |

### ECOG (เพิ่มเติม — ไม่ได้มาจากสไลด์ ใช้บ่อยกว่าในเวชปฏิบัติ)
| ECOG | | ≈ KPS |
|---|---|---|
| **0** | ปกติเต็มที่ | 90–100 |
| **1** | ทำงานเบาได้ จำกัดเฉพาะงานหนัก | 70–80 |
| **2** | ดูแลตัวเองได้ ทำงานไม่ได้ **ลุกจากเตียง > 50% ของเวลาตื่น** | 50–60 |
| **3** | ดูแลตัวเองได้จำกัด **อยู่บนเตียง/เก้าอี้ > 50%** | 30–40 |
| **4** | ติดเตียง ดูแลตัวเองไม่ได้ | 10–20 |
ยาเคมีบำบัดส่วนใหญ่ให้ใน **ECOG 0–2** · **ECOG 3–4 มักได้ประโยชน์น้อยและเสี่ยงสูง** → เน้นประคับประคอง (ยกเว้นมะเร็งที่ตอบสนองยาดีมาก เช่น lymphoma, germ cell, SCLC)

### ปัจจัยของมะเร็ง (สไลด์)
- **ระยะ (staging)** — TNM
- **ชนิดที่ตอบสนองต่อยาเคมี** — **grade สูง · mitosis มาก · Ki-67 สูง · poorly differentiated**
- **ไวต่อรังสี**: **seminoma · lymphoma · squamous cell carcinoma**
- **Predictive marker สำหรับยามุ่งเป้า**: **HER2** (trastuzumab) · **KRAS** (anti-EGFR antibody ใช้ได้เฉพาะ RAS wild-type) · **EGFR mutation** (EGFR-TKI ในมะเร็งปอด)
> **Prognostic** = บอกพยากรณ์โรค (เช่น ต่อมน้ำเหลืองบวก) · **Predictive** = บอกว่ายาตัวใดจะได้ผล (เช่น HER2, EGFR mutation)
""",
    ["Performance status = ตัวทำนายการทนยาที่สำคัญที่สุด · ใช้อายุตามการทำงาน",
     "KPS ≥ 80 ทำงานได้ · 50–70 อยู่บ้าน · ≤ 40 ดูแลตัวเองไม่ได้",
     "ECOG 0–2 ให้ยาเคมี · 3–4 เน้นประคับประคอง",
     "ไวรังสี: seminoma lymphoma SCC · predictive: HER2 KRAS EGFR"],
    [mcq(N(3), "A 70-year-old woman with metastatic gastric cancer cares for herself but cannot work, and is up and about for more than half of her waking hours. What is her approximate ECOG performance status?",
         ["ECOG 0", "ECOG 1", "ECOG 2", "ECOG 3", "ECOG 4"], 2,
         "**ECOG 2** = ดูแลตัวเองได้ **ทำงานไม่ได้** และ **ลุกจากเตียงมากกว่าครึ่งหนึ่งของเวลาตื่น** (≈ KPS 50–60)\n\nECOG 1 ยังทำงานเบาได้ · ECOG 3 อยู่บนเตียงหรือเก้าอี้ > 50% · ผู้ป่วย ECOG 0–2 ยังพิจารณาเคมีบำบัดแบบประคับประคองได้\n\n*(ECOG ไม่ได้มาจากสไลด์ — สไลด์ใช้ Karnofsky)*",
         "ECOG 2: ดูแลตัวเองได้ ทำงานไม่ได้ ลุก > 50%", "Performance status", ["ECOG performance status (Oken 1982)"] + R("Karnofsky performance status scale"), PS),
     mcq(N(4), "Which of the following tumours is classically highly radiosensitive?",
         ["Melanoma", "Seminoma", "Renal cell carcinoma", "Osteosarcoma", "Glioblastoma"], 1,
         "สไลด์ cancer's factors: มะเร็งที่ **ไวต่อรังสี** ได้แก่ **seminoma · lymphoma · squamous cell carcinoma**\n\nMelanoma, RCC, sarcoma และ glioblastoma ค่อนข้าง **ดื้อรังสี** (ต้องใช้ขนาดสูง)",
         "ไวรังสี: seminoma lymphoma SCC", "Radiosensitivity", R("Cancer's factors"), PS + ["B10.2.4-3(2)"]),
    ], PS)

# ───────────────────────────── 4
BIO = ["B1.6.4(1)"]
sec("hon-onc-04", "เซลล์ปกติกับเซลล์มะเร็ง — วงจรเซลล์และ hallmarks",
    "เซลล์ส่วนใหญ่อยู่ G0 ต้องมีสัญญาณการเติบโต · checkpoint G1 G2 metaphase · 6 hallmarks + ใหม่ · หลายขั้นตอน dysplasia → CIS → มะเร็ง", 10,
"""### การควบคุมการเติบโตของเซลล์ปกติ (สไลด์)
- **เซลล์ร่างกายส่วนใหญ่อยู่ในระยะพัก (G0)** — ต้องได้ **สัญญาณการเติบโต** จึงเข้าสู่ G1
- ห่วงโซ่สัญญาณ: **growth ligand (เช่น EGF) → growth receptor (เช่น EGFR ในตระกูล HER) → downstream pathway (RAS–RAF–MEK–ERK, PI3K–AKT–mTOR) → นิวเคลียส**
- **Cell cycle checkpoint** ตรวจ **DNA เสียหาย** → **หยุดวงจรเพื่อซ่อม** → ถ้าซ่อมไม่ได้ → **apoptosis**
| Checkpoint | ตำแหน่ง | ตัวควบคุมหลัก (เพิ่มเติม) |
|---|---|---|
| **G1 (restriction point)** | ก่อนเข้า S phase | **p53 → p21** · **Rb**–cyclin D/CDK4/6 |
| **G2** | ก่อนเข้า M phase | ATM/ATR–CHK |
| **Metaphase (spindle)** | ก่อนแยกโครโมโซม | spindle assembly checkpoint |

### Hallmarks of cancer (Hanahan & Weinberg — สไลด์)
1. **พึ่งตนเองด้านสัญญาณการเติบโต** (self-sufficiency in growth signals)
2. **ไม่ตอบสนองต่อสัญญาณยับยั้ง** (insensitivity to antigrowth signals)
3. **หลบเลี่ยง apoptosis**
4. **แบ่งตัวได้ไม่จำกัด** (telomerase)
5. **สร้างหลอดเลือดใหม่ต่อเนื่อง** (angiogenesis)
6. **รุกรานเนื้อเยื่อและแพร่กระจาย**
**Hallmarks ใหม่ (Cell 2011 — สไลด์)**: **ปรับเมตาบอลิซึมพลังงาน (Warburg)** · **หลบเลี่ยงระบบภูมิคุ้มกัน** · ปัจจัยเอื้อ: **genome ไม่เสถียร** และ **การอักเสบที่ส่งเสริมเนื้องอก** *(ฉบับ 2022 เพิ่ม phenotypic plasticity, epigenetic reprogramming, microbiome, senescent cells)*

**การแพร่กระจาย — seed and soil** (สไลด์): เซลล์มะเร็ง (seed) ไปเติบโตได้เฉพาะในอวัยวะที่สภาพแวดล้อมเหมาะ (soil) — เช่น มะเร็งเต้านม/ต่อมลูกหมากชอบกระดูก

### กลไกก่อมะเร็ง (สไลด์)
- **ทางการเติบโต**: หลั่งสัญญาณเอง · **เพิ่มจำนวน receptor** (HER2 amplification) · **receptor กลายพันธุ์ทำงานเองไม่ต้องมี ligand** (EGFR mutation) · **downstream ทำงานเอง** (KRAS, BRAF)
- **Angiogenesis** (VEGF) · **apoptosis** · **metastasis**
- **หลายปัจจัย**: พันธุกรรม (germline เช่น BRCA, Lynch · หรือ sporadic) + สิ่งแวดล้อม (บุหรี่ UV ไวรัส)
- **หลายขั้นตอน (multistep)**: ปกติ → **dysplasia (intraepithelial neoplasia) เล็กน้อย → ปานกลาง → รุนแรง → carcinoma in situ → มะเร็งรุกราน** — เช่น **CIN** ของปากมดลูก, adenoma–carcinoma sequence ของลำไส้ใหญ่ (APC → KRAS → p53)
""",
    ["เซลล์ส่วนใหญ่อยู่ G0 · checkpoint: G1 (p53, Rb) · G2 · metaphase",
     "6 hallmarks + เมตาบอลิซึม + หลบภูมิคุ้มกัน",
     "Seed and soil — มะเร็งไปอวัยวะที่เหมาะ",
     "Multistep: dysplasia → CIS → invasive · CIN · adenoma–carcinoma"],
    [mcq(N(5), "A tumour carries a loss-of-function mutation in TP53. Which normal cellular response to DNA damage is most directly lost?",
         ["Secretion of VEGF", "Arrest at the G1 checkpoint to allow DNA repair, or apoptosis if repair fails", "Telomerase activation", "EGFR dimerisation", "Microtubule assembly in M phase"], 1,
         "สไลด์: checkpoint ทำหน้าที่ **ตรวจ DNA เสียหาย → หยุดวงจรให้ซ่อม → ถ้าซ่อมไม่ได้ส่งเซลล์ไป apoptosis**\n\n**p53** เป็นตัวหลักของ **G1 checkpoint** (กระตุ้น p21 ยับยั้ง CDK) และกระตุ้น apoptosis — เมื่อเสียไป เซลล์ที่ DNA เสียหายแบ่งตัวต่อได้ สะสมการกลายพันธุ์ (**genome ไม่เสถียร**) · TP53 กลายพันธุ์พบบ่อยที่สุดในมะเร็งมนุษย์",
         "p53 = ผู้พิทักษ์ genome ที่ G1 checkpoint", "Cell cycle checkpoints", R("Cell cycle check point"), BIO),
     mcq(N(6), "Which of the following is an original hallmark of cancer described by Hanahan and Weinberg?",
         ["Dependence on exogenous growth factors", "Sustained angiogenesis", "Increased sensitivity to apoptosis", "Limited replicative potential", "Contact inhibition"], 1,
         "Hallmarks 6 ข้อแรก (สไลด์): **พึ่งตนเองด้านสัญญาณการเติบโต · ไม่ตอบสนองสัญญาณยับยั้ง · หลบเลี่ยง apoptosis · แบ่งตัวไม่จำกัด · สร้างหลอดเลือดใหม่ต่อเนื่อง · รุกรานและแพร่กระจาย**\n\nตัวเลือกอื่นเป็นคุณสมบัติของ **เซลล์ปกติ** (ต้องพึ่งสัญญาณจากภายนอก แบ่งตัวได้จำกัด มี contact inhibition)",
         "Sustained angiogenesis = hallmark", "Hallmarks of cancer", R("What is cancer cell?"), BIO),
    ], BIO + ["B1.6.4(4)"])

# ───────────────────────────── 5
CHE = ["B1.7.3"]
sec("hon-onc-05", "ยาเคมีบำบัดและวงจรเซลล์",
    "Non-phase specific: platinum alkylating · S phase: antimetabolite topoisomerase inhibitor · G2: bleomycin · M: taxane vinca · มะเร็งโตเร็วตอบสนองดี · ให้นาน รุ่นใหม่ ให้ร่วมกัน · พิษเฉพาะยา", 11,
"""### กลุ่มยาต้านมะเร็ง (สไลด์)
| กลุ่ม | ตัวอย่าง |
|---|---|
| **ไม่ขึ้นกับวงจรเซลล์** | steroid |
| **ขึ้นกับวงจรเซลล์ แต่ไม่จำเพาะระยะ** | **Platinum** (cisplatin carboplatin oxaliplatin) · **Alkylating** (cyclophosphamide ifosfamide) |
| **จำเพาะ S phase** | **Antimetabolite** (5-FU methotrexate gemcitabine) · **topoisomerase inhibitor** (anthracycline เช่น doxorubicin · irinotecan etoposide) |
| **จำเพาะ G2** | **Bleomycin** |
| **จำเพาะ M phase** | **Antimicrotubule** — **taxane** (paclitaxel docetaxel) · **vinca alkaloid** (vincristine) |
| **Targeted therapy** | ยับยั้งโมเลกุลเป้าหมายของการก่อมะเร็ง |

### ทำไมยาเคมีไม่ฆ่ามะเร็งหมดในครั้งเดียว (สไลด์)
- **ยาเคมีออกฤทธิ์เฉพาะเซลล์ที่กำลังแบ่งตัว**
- มะเร็งส่วนใหญ่ **ผลัดเซลล์เป็นวันถึงสัปดาห์** แต่ **ยาอยู่ในร่างกายเป็นชั่วโมง** → ต้องให้ซ้ำเป็นรอบ (cycles)

**ปัจจัยของเซลล์มะเร็ง** — โตเร็วตอบสนองดี: **poorly differentiated · proliferation สูง · mitosis มาก · growth fraction (S phase) สูง · Ki-67 สูง** — เช่น **germ cell tumour, small cell lung cancer** (ไวต่อยามาก)
**ปัจจัยของยา**
- **ระยะเวลาสัมผัสยา** — **5-FU หยดต่อเนื่องดีกว่าฉีดครั้งเดียว** ในมะเร็งลำไส้ใหญ่ (ยาจำเพาะ S phase ต้องอยู่นานให้ทันเซลล์เข้าระยะ)
- **รุ่นของยา** — ยารุ่นที่ 3 ดีกว่ารุ่นที่ 2 ใน NSCLC stage IIIB/IV
- **ให้ร่วมกัน (combination)** — ฆ่าเซลล์ได้มากที่สุดภายใต้พิษที่ทนได้ ครอบคลุมเซลล์หลายกลุ่ม · **อัตราตอบสนองเพิ่มแต่ไม่แปลเป็นการรอดชีวิตเสมอ** · platinum doublet ดีกว่ายาเดี่ยวใน NSCLC

### พิษเฉพาะยาที่ต้องจำ (ไม่ได้มาจากสไลด์)
| ยา | พิษเด่น |
|---|---|
| **Doxorubicin (anthracycline)** | **หัวใจล้มเหลว** ตามขนาดสะสม → ตรวจ echo/LVEF |
| **Cisplatin** | **ไตวาย** Mg ต่ำ **หูตึง** คลื่นไส้รุนแรง ปลายประสาท |
| **Bleomycin** | **ปอดเป็นพังผืด** (ไม่กดไขกระดูก) |
| **Vincristine** | **ปลายประสาทอักเสบ** ท้องผูก (ไม่กดไขกระดูก) |
| **Cyclophosphamide/ifosfamide** | **กระเพาะปัสสาวะอักเสบมีเลือดออก** → mesna |
| **Oxaliplatin** | ปลายประสาทชาเมื่อโดนความเย็น |
| **5-FU/capecitabine** | เยื่อบุปากอักเสบ ท้องเสีย hand–foot syndrome · DPD deficiency พิษรุนแรง |
| **Methotrexate** | กดไขกระดูก เยื่อบุอักเสบ → leucovorin rescue |
| ทั่วไป | **กดไขกระดูก (nadir 7–14 วัน) → febrile neutropenia = ภาวะฉุกเฉิน** ผมร่วง คลื่นไส้ |
""",
    ["Non-phase specific: platinum alkylating · S: antimetabolite · G2: bleomycin · M: taxane vinca",
     "ยาเคมีฆ่าเฉพาะเซลล์ที่แบ่งตัว → ให้เป็นรอบ",
     "ไวยามาก: germ cell tumour · SCLC",
     "Anthracycline หัวใจ · cisplatin ไต หู · bleomycin ปอด · vincristine ประสาท"],
    [mcq(N(7), "Which chemotherapeutic agent acts specifically in the M phase by disrupting microtubules?",
         ["Cisplatin", "Cyclophosphamide", "5-fluorouracil", "Vincristine", "Bleomycin"], 3,
         "สไลด์: **M phase — antimicrotubule: taxane และ vinca alkaloid (vincristine)** · vinca ยับยั้งการประกอบ microtubule · taxane ทำให้ microtubule เสถียรจนแยกตัวไม่ได้\n\n**Cisplatin, cyclophosphamide** = ไม่จำเพาะระยะ · **5-FU** = S phase · **bleomycin** = G2",
         "M phase: taxane + vinca", "Cell-cycle specificity", R("Classic cytotoxic drug"), CHE),
     mcq(N(8), "A 28-year-old man receiving bleomycin, etoposide and cisplatin (BEP) for testicular germ cell tumour develops progressive dyspnoea and dry cough with bibasal crackles and a restrictive defect. Which drug is most likely responsible?",
         ["Etoposide", "Cisplatin", "Bleomycin", "Vincristine", "Doxorubicin"], 2,
         "**Bleomycin** ทำให้ **ปอดอักเสบและพังผืด (pulmonary fibrosis)** ตามขนาดสะสม — หยุดยาทันที ให้ steroid หลีกเลี่ยงออกซิเจนความเข้มข้นสูงเกินจำเป็น\n\nCisplatin = ไต หู ปลายประสาท · doxorubicin = หัวใจ · vincristine = ปลายประสาท\n\nGerm cell tumour เป็นตัวอย่างมะเร็งที่ **ไวต่อยาเคมีมาก** (สไลด์) แม้แพร่กระจายก็หายขาดได้\n\n*(พิษของยาไม่ได้มาจากสไลด์)*",
         "Bleomycin → pulmonary fibrosis", "Chemotherapy toxicity", ["Standard pharmacology — chemotherapy toxicity"], CHE + ["B10.2.4-3(2)"]),
    ], CHE)

# ───────────────────────────── 6
TGT = ["B1.7.3", "B1.6.4(1)"]
sec("hon-onc-06", "Targeted therapy — HER family, tyrosine kinase และ angiogenesis",
    "-mab จับนอกเซลล์ · -nib TKI ในเซลล์ · cetuximab ใช้เฉพาะ RAS wild-type · trastuzumab HER2 · EGFR-TKI ในมะเร็งปอด EGFR mutation · imatinib BCR-ABL · bevacizumab VEGF", 11,
"""### Targeted therapy คืออะไร (สไลด์)
ยาที่ **ยับยั้งโมเลกุลเป้าหมายจำเพาะ** ในการก่อมะเร็งและการโตของก้อน — **ไม่ใช่การฆ่าเซลล์ที่แบ่งตัวเร็วทั่วไป** แบบยาเคมี
| | **Monoclonal antibody (-mab)** | **Small molecule (-nib)** |
|---|---|---|
| ตำแหน่ง | **นอกเซลล์ — จับ ligand หรือ receptor** (upstream) | **ในเซลล์ — ยับยั้ง tyrosine kinase** (downstream) |
| การให้ | ทางหลอดเลือด | **กิน** |
| ตัวอย่าง | trastuzumab cetuximab bevacizumab | imatinib erlotinib gefitinib lapatinib sorafenib |

### Tyrosine kinase (สไลด์)
ย้ายฟอสเฟตจาก ATP ไปยัง tyrosine ของโปรตีน → ควบคุม **การแบ่งตัว การอยู่รอด angiogenesis การรุกรานและแพร่กระจาย**
- **Receptor TK**: **EGFR · VEGFR · PDGFR**
- **Non-receptor TK**: **JAK2 · c-ABL**

### HER family (EGFR) — ยาในสไลด์
| เป้า | ยา | ใช้ใน | Predictive marker |
|---|---|---|---|
| **EGFR (HER1) — antibody** | **cetuximab · panitumumab** | มะเร็งลำไส้ใหญ่ระยะแพร่กระจาย · ศีรษะและคอ | **ใช้ได้เฉพาะ RAS (KRAS/NRAS) wild-type** — RAS กลายพันธุ์ทำให้ downstream ทำงานเองจึงดื้อ |
| **HER2 — antibody** | **trastuzumab · pertuzumab** | **มะเร็งเต้านม/กระเพาะ HER2 บวก** | IHC 3+ หรือ FISH บวก · พิษ: **หัวใจ (ผันกลับได้)** |
| **EGFR — TKI** | **erlotinib · gefitinib** (osimertinib รุ่นที่ 3 ปัจจุบันเป็นมาตรฐาน) | **NSCLC (adenocarcinoma) ที่มี EGFR mutation** | exon 19 deletion/L858R · พบบ่อยในเอเชีย หญิง ไม่สูบบุหรี่ |
| **HER2/EGFR — TKI** | **lapatinib** | มะเร็งเต้านม HER2 บวก | |
| **BCR-ABL (+ KIT)** | **imatinib** | **CML** (Philadelphia) · GIST (KIT) | |
> ผลข้างเคียงเด่นของยากลุ่ม anti-EGFR: **ผื่นแบบสิว (acneiform rash)** — ผื่นมากสัมพันธ์กับการตอบสนองดี · ท้องเสีย

### Angiogenesis (สไลด์)
- ก้อน **< 1–2 มม.** ไม่มีหลอดเลือด อยู่นิ่ง (dormant) → **angiogenic switch: VEGF เพิ่ม** → ก้อนโตและแพร่กระจายได้
- หลอดเลือดของก้อน **รั่ว ขาดเซลล์ค้ำจุน ไม่เป็นระเบียบ**
- ยา: **bevacizumab** (antibody ต่อ VEGF-A) · **VEGF-trap (aflibercept)** · **TKI ต่อ VEGFR**: sorafenib pazopanib (ใช้ใน RCC HCC)
- **พิษของยาต้าน VEGF (ไม่ได้มาจากสไลด์)**: **ความดันสูง · โปรตีนรั่วในปัสสาวะ · เลือดออก · ลิ่มเลือดแดง · ลำไส้ทะลุ · แผลหายช้า** → หยุดยาก่อนและหลังผ่าตัด
""",
    ["-mab นอกเซลล์ ทางหลอดเลือด · -nib TKI ในเซลล์ กิน",
     "Cetuximab/panitumumab ใช้เฉพาะ RAS wild-type",
     "Trastuzumab: HER2 3+/FISH+ · พิษหัวใจผันกลับได้",
     "EGFR-TKI ใน NSCLC EGFR mutation · imatinib BCR-ABL",
     "Bevacizumab: ความดันสูง โปรตีนรั่ว เลือดออก ลำไส้ทะลุ แผลหายช้า"],
    [mcq(N(9), "A patient with metastatic colorectal adenocarcinoma is being considered for cetuximab. Which biomarker result is required before using it?",
         ["HER2 amplification", "RAS (KRAS/NRAS) wild-type", "EGFR exon 19 deletion", "BCR-ABL fusion", "PD-L1 expression ≥ 50%"], 1,
         "สไลด์ predictive marker: **KRAS** — cetuximab/panitumumab จับ **EGFR นอกเซลล์** แต่ถ้า **RAS กลายพันธุ์** สัญญาณ downstream ทำงานเองโดยไม่ต้องผ่าน EGFR → **ยาไม่ได้ผล**\n\nจึงใช้ได้เฉพาะ **RAS wild-type** (ปัจจุบันตรวจ BRAF ด้วย) · EGFR exon 19 deletion ใช้เลือก EGFR-TKI ใน **มะเร็งปอด**",
         "Anti-EGFR mAb ใช้เฉพาะ RAS wild-type", "Predictive markers", R("Cancer's factors · EGFR antagonist"), TGT + ["B8.2.4-3(1)"]),
     mcq(N(10), "A 62-year-old woman on bevacizumab for metastatic colon cancer is reviewed before her next cycle. Which adverse effect should be routinely monitored for this drug?",
         ["Pulmonary fibrosis", "Hypertension and proteinuria", "Haemorrhagic cystitis", "Ototoxicity", "Acneiform rash"], 1,
         "**Bevacizumab** ยับยั้ง **VEGF** — ผลข้างเคียงประจำกลุ่ม: **ความดันสูง และโปรตีนรั่วในปัสสาวะ** (วัดความดันและตรวจปัสสาวะทุกรอบ) · ร้ายแรงแต่พบน้อย: เลือดออก ลิ่มเลือดแดง **ลำไส้ทะลุ แผลหายช้า**\n\nAcneiform rash = anti-EGFR · hemorrhagic cystitis = cyclophosphamide · หูตึง = cisplatin\n\n*(พิษของยาไม่ได้มาจากสไลด์)*",
         "Anti-VEGF → ความดันสูง + proteinuria", "Anti-angiogenic therapy", ["Bevacizumab prescribing information"] + R("VEGF antagonist in cancer treatment"), TGT),
     mcq(N(11), "A 55-year-old non-smoking Thai woman has metastatic lung adenocarcinoma with an EGFR exon 19 deletion. Which class of first-line therapy is most appropriate?",
         ["Anti-VEGF antibody alone", "EGFR tyrosine kinase inhibitor", "Anti-HER2 antibody", "Imatinib", "Single-agent bleomycin"], 1,
         "**EGFR mutation (exon 19 deletion หรือ L858R)** ทำให้ receptor ทำงานเองโดยไม่ต้องมี ligand (สไลด์: mutation of receptor) → ตอบสนองดีมากต่อ **EGFR-TKI** — สไลด์ยกตัวอย่าง **erlotinib, gefitinib** · ปัจจุบันใช้ **osimertinib** เป็นทางเลือกแรก\n\nพบบ่อยใน **คนเอเชีย ผู้หญิง ไม่สูบบุหรี่ adenocarcinoma**",
         "EGFR mutation NSCLC → EGFR-TKI", "EGFR-TKI", R("HER family · EGFR antagonist") + ["NCCN/ESMO NSCLC guidelines"], TGT + ["B6.2.4-3(2)"]),
    ], TGT)

# ───────────────────────────── 7
IO = ["B1.4.12", "B1.4.14"]
sec("hon-onc-07", "Immuno-oncology — immune checkpoint inhibitors และ irAEs",
    "CTLA-4 กดช่วงกระตุ้น T cell ในต่อมน้ำเหลือง · PD-1 กด T cell ในเนื้อเยื่อ · ใช้ในมะเร็งหลายชนิดรวม MSI-H/dMMR · irAE ผิวหนังมาก่อน ลำไส้ ตับ ต่อมไร้ท่อ · รักษาด้วย steroid ตามระดับ", 10,
"""### การควบคุมระบบภูมิคุ้มกัน (สไลด์)
- T cell ถูกกระตุ้นเมื่อ **APC แสดง antigen (หรือ neoantigen ของมะเร็ง) บน MHC** + **สัญญาณกระตุ้นร่วม (co-stimulation)**
- สมดุลกับ **สัญญาณยับยั้ง (co-inhibitory = immune checkpoint)** — น้อยไป = autoimmune · มากไป = ภูมิคุ้มกันบกพร่อง/**ทนต่อมะเร็ง (immune tolerance)**
- **มะเร็งใช้ checkpoint หลบภูมิคุ้มกัน** (hallmark ใหม่)

| | **CTLA-4** | **PD-1 / PD-L1** |
|---|---|---|
| ช่วงที่ออกฤทธิ์ | **ช่วงแรกของการกระตุ้น T cell (priming) ในต่อมน้ำเหลือง** | **ช่วง effector — T cell ในเนื้อเยื่อ/ก้อนมะเร็ง** |
| กลไก | แย่งจับ B7 (CD80/86) จาก CD28 | PD-L1 บนเซลล์มะเร็งจับ PD-1 ทำให้ T cell หมดแรง |
| ยา | **ipilimumab** | **anti-PD-1: nivolumab pembrolizumab** · **anti-PD-L1: atezolizumab durvalumab** |
| พิษ | **มากกว่า** (colitis, hypophysitis) | น้อยกว่า (thyroiditis, pneumonitis) |

### ข้อบ่งใช้ที่ได้รับอนุมัติ (สไลด์)
Melanoma · **NSCLC** · SCLC · **RCC** · urothelial · **ศีรษะและคอ** · **Hodgkin lymphoma** · PMBCL · **HCC** · กระเพาะ/GEJ · **ปากมดลูก** · **TNBC** · Merkel cell · cutaneous SCC · **MSI-high CRC** และ **มะเร็งก้อนตันใดก็ได้ที่ dMMR** (อนุมัติตาม biomarker ไม่ขึ้นกับอวัยวะ)

### Immune-related adverse events (irAEs)
- เกิดได้ **ทุกอวัยวะ** — **ผิวหนัง (ผื่น คัน) เกิดเร็วที่สุด** · **ลำไส้ใหญ่อักเสบ** · **ตับอักเสบ** · **ต่อมไร้ท่อ** (ไทรอยด์ ต่อมใต้สมอง ต่อมหมวกไต **เบาหวานชนิด 1**) · **ปอดอักเสบ** · กล้ามเนื้อหัวใจอักเสบ (พบน้อยแต่ตายสูง)
- **การให้ยาร่วม (CTLA-4 + PD-1) เกิดเร็วกว่าและรุนแรงกว่า** (สไลด์ kinetics)
- อาจเกิด **หลังหยุดยาแล้วหลายเดือน**

**การดูแล (ASCO/ESMO — ไม่ได้มาจากสไลด์)**
| ระดับ | ทำอะไร |
|---|---|
| **1** | ให้ยาต่อ เฝ้าระวัง |
| **2** | **พักยา** · **prednisolone 0.5–1 มก./กก./วัน** |
| **3–4** | **หยุดยา** · **methylprednisolone 1–2 มก./กก./วัน** · ไม่ดีขึ้น 48–72 ชม. → **infliximab** (colitis) หรือ mycophenolate (ตับอักเสบ — ห้าม infliximab) |
| ต่อมไร้ท่อ | **ให้ฮอร์โมนทดแทน** (levothyroxine hydrocortisone insulin) มักไม่ต้อง steroid ขนาดสูง และมักให้ ICI ต่อได้ |
""",
    ["CTLA-4: priming ในต่อมน้ำเหลือง · PD-1: effector ในเนื้อเยื่อ",
     "ICI ใช้ในมะเร็ง MSI-H/dMMR ทุกอวัยวะ",
     "irAE: ผิวหนังเร็วสุด · colitis · hepatitis · endocrine · pneumonitis · myocarditis",
     "Grade 2 พักยา + pred 0.5–1 · grade 3–4 หยุด + methylpred 1–2 · endocrine ให้ฮอร์โมนทดแทน"],
    [mcq(N(12), "A 60-year-old man receiving pembrolizumab for NSCLC develops 7 watery stools per day above baseline with abdominal cramps (grade 3 colitis). Infection has been excluded. What is the most appropriate management?",
         ["Continue pembrolizumab and give loperamide", "Withhold pembrolizumab and start IV methylprednisolone 1–2 mg/kg/day", "Start oral vancomycin", "Reduce the pembrolizumab dose by half", "Start infliximab alone without steroids"], 1,
         "**Immune-related colitis grade 3** (≥ 7 ครั้งเหนือปกติ) → **หยุด ICI** และให้ **methylprednisolone 1–2 มก./กก./วัน** · ถ้าไม่ดีขึ้นใน 48–72 ชม. เพิ่ม **infliximab** หรือ vedolizumab\n\nICI **ไม่ลดขนาด** — ให้ต่อ พัก หรือหยุดเท่านั้น · loperamide อย่างเดียวอาจบังอาการและเสี่ยงทะลุ\n\n*(การจัดการ irAE ไม่ได้มาจากสไลด์ — ASCO 2021/ESMO 2022)*",
         "irAE grade 3 → หยุด ICI + methylpred 1–2 มก./กก.", "Immune-related adverse events", ["ASCO guideline: Management of irAEs (2021)", "ESMO irAE guideline (2022)"] + R("Immune related adverse events"), IO),
     mcq(N(13), "Which statement correctly contrasts CTLA-4 and PD-1?",
         ["CTLA-4 acts mainly in the effector phase within tumour tissue", "CTLA-4 regulates early T-cell activation (priming) in lymphoid tissue, whereas PD-1 inhibits effector T-cell activity in peripheral tissues and tumours",
          "PD-1 is expressed only on tumour cells", "Both act only on B cells", "Blocking CTLA-4 causes fewer immune adverse events than blocking PD-1"], 1,
         "สไลด์ (J Clin Oncol 2015): **CTLA-4 ควบคุมช่วงแรกของการกระตุ้น T cell** (ในต่อมน้ำเหลือง แย่งจับ B7 จาก CD28) · **PD-1 ยับยั้ง T cell ในช่วง effector** ในเนื้อเยื่อ เมื่อจับ PD-L1 บนเซลล์มะเร็ง\n\nการยับยั้ง CTLA-4 ทำให้ T cell ถูกกระตุ้นกว้างกว่า → **irAE มากกว่า** anti-PD-1",
         "CTLA-4 = priming · PD-1 = effector", "Immune checkpoints", R("CTLA4 · PD1"), IO),
    ], IO + ["B1.7.3"])

# ───────────────────────────── 8
BR = ["B10.2.4-3(4)", "2.1.55"]
sec("hon-onc-08", "มะเร็งเต้านม — คัดกรอง ชนิดย่อย และการรักษา",
    "Mammogram ปีละครั้ง/ทุก 2 ปีตั้งแต่ 40 · HBOC BRCA → MRI ตั้งแต่ 30 · ER/PR HER2 TNBC · ต่อมน้ำเหลืองคือพยากรณ์สำคัญที่สุด · endocrine 5 ปี TAM/AI · trastuzumab 1 ปี · metastatic HR+ เริ่มด้วยฮอร์โมน", 14,
"""### คัดกรอง (สไลด์)
- **คนทั่วไป: mammogram ปีละครั้งช่วงอายุ 40–50 ปี**
- **มะเร็งเต้านม–รังไข่ทางพันธุกรรม (HBOC, autosomal dominant)** สงสัยเมื่อ: **มะเร็งเต้านมอายุ < 45 ปี · ทั้งสองข้าง · ในผู้ชาย · ร่วมกับมะเร็งรังไข่อายุใดก็ได้** → ตรวจ **BRCA1/BRCA2** · ผู้มียีน: **mammogram/MRI เต้านมตั้งแต่อายุ 30 ปี**
> **อัปเดต (ไม่ได้มาจากสไลด์)** — **USPSTF 2024: mammogram ทุก 2 ปี อายุ 40–74 ปี** · ACR/NCCN: ปีละครั้งตั้งแต่ 40 ปี · ผู้มียีน BRCA: MRI ปีละครั้งตั้งแต่ 25–30 ปี และพิจารณาผ่าตัดรังไข่และท่อนำไข่ป้องกันเมื่ออายุ 35–45 ปี

### ชนิดย่อยและพยากรณ์ (สไลด์)
พยาธิ: **invasive ductal (พบบ่อยสุด) / lobular carcinoma**
| ชนิดย่อย | ลักษณะ | ยาหลัก |
|---|---|---|
| **Hormone receptor บวก (ER/PgR+)** | พบบ่อยสุด โตช้า | **ยาต้านฮอร์โมน** |
| **HER2 บวก** | **IHC 3+ หรือ FISH บวก** | **trastuzumab ± pertuzumab** + ยาเคมี |
| **Triple negative (TNBC)** | ER PgR HER2 ลบ · อายุน้อย · BRCA1 · ดุ | ยาเคมี (± immunotherapy) |
- **พยากรณ์ที่สำคัญที่สุด = จำนวนต่อมน้ำเหลืองรักแร้ที่มีมะเร็ง**
- อายุมาก/หมดประจำเดือนพยากรณ์ดีกว่า

### ระยะแรก — ผ่าตัดเป็นหลัก (สไลด์)
**เต้านม**: **ตัดเต้านมแบบ modified radical (MRM)** หรือ **ผ่าตัดสงวนเต้า (BCS) + ฉายแสงเสมอ**
**รักแร้**: คลำต่อมน้ำเหลืองไม่ได้ → **sentinel lymph node biopsy (SLNB)** · บวกชัด → axillary dissection (ALND)
**การรักษาเสริม (adjuvant)**
| การรักษา | ให้เมื่อ |
|---|---|
| **ยาต้านฮอร์โมน 5 ปี** | **ER/PgR บวกทุกราย (ไม่ว่ากี่ %)** · **ก่อนหมดประจำเดือน: tamoxifen** · **หลังหมดประจำเดือน: aromatase inhibitor (AI) ± tamoxifen** |
| **ยาเคมี (anthracycline-based)** | **ต่อมน้ำเหลืองบวก** หรือ **ก้อน > 1–2 ซม.** (โดยเฉพาะ HER2+/TNBC) |
| **Trastuzumab 1 ปี** | **HER2 บวก (3+ หรือ FISH+)** |
| **ฉายแสงหลัง MRM** | **ต่อมน้ำเหลืองบวก > 4 ต่อม · ก้อน > 5 ซม. · ขอบใกล้** |
> **อัปเดต (ไม่ได้มาจากสไลด์)** — ER+ HER2− ต่อมน้ำเหลือง 0–3: ใช้ **genomic assay (Oncotype DX)** ตัดสินว่าต้องให้ยาเคมีหรือไม่ · เสี่ยงสูงพิจารณา **ยาต้านฮอร์โมน 7–10 ปี** และ **abemaciclib/ribociclib** หรือ **olaparib (BRCA)** · **TNBC/HER2+ ระยะ II–III มักให้ยาก่อนผ่าตัด (neoadjuvant)** — TNBC ใช้ **pembrolizumab + ยาเคมี (KEYNOTE-522)** · เหลือก้อนหลังยา: HER2+ → T-DM1 · TNBC → capecitabine
> **ผลข้างเคียงยาต้านฮอร์โมน** — tamoxifen: **มะเร็งเยื่อบุโพรงมดลูก ลิ่มเลือด** (แต่ช่วยกระดูก) · AI: **กระดูกพรุน ปวดข้อ** → ตรวจ BMD

### ระยะลุกลามเฉพาะที่/inflammatory (สไลด์)
**ยาเคมี (anthracycline) ก่อน → MRM → ฉายแสง** (inflammatory ห้ามผ่าตัดสงวนเต้า)

### ระยะแพร่กระจาย (สไลด์)
| | ทำอะไร |
|---|---|
| **HR บวก + กระดูก/เนื้อเยื่ออ่อน หรืออวัยวะภายในเล็กน้อยไม่มีอาการ** | **ยาต้านฮอร์โมนแบบประคับประคอง** — ก่อนหมดประจำเดือน tamoxifen · หลังหมด AI หรือ tamoxifen |
| **HR บวก + แพร่ไปอวัยวะภายในมาก มีอาการ (visceral crisis)** | **ยาเคมี** — ยังไม่เคยได้ anthracycline → anthracycline · เคยได้แล้ว → **taxane ± trastuzumab (HER2+)** |
| **HR ลบ** | **ยาเคมีแบบประคับประคอง** |
> **อัปเดต (ไม่ได้มาจากสไลด์)** — HR+ HER2− แพร่กระจาย มาตรฐานปัจจุบัน: **AI + CDK4/6 inhibitor (palbociclib ribociclib abemaciclib)** เป็นทางเลือกแรก (ก่อนหมดประจำเดือนต้องกดรังไข่ร่วม) · HER2+: **trastuzumab + pertuzumab + taxane** แล้ว **trastuzumab deruxtecan** · กระดูก: **bisphosphonate/denosumab** ลดกระดูกหัก
""",
    ["คัดกรอง mammogram ตั้งแต่ 40 · BRCA → MRI ตั้งแต่ 25–30",
     "HBOC: < 45 ปี · สองข้าง · ผู้ชาย · + มะเร็งรังไข่",
     "พยากรณ์สำคัญที่สุด = ต่อมน้ำเหลือง",
     "ER/PgR+ ทุก % → ยาต้านฮอร์โมน 5 ปี (pre TAM · post AI)",
     "HER2+ → trastuzumab 1 ปี · HR+ แพร่กระจายไม่มี visceral crisis → ยาต้านฮอร์โมน (+ CDK4/6i)"],
    [mcq(N(14), "A 62-year-old postmenopausal woman has a 1.5 cm invasive ductal carcinoma, ER 90%, PgR 60%, HER2 negative, sentinel nodes negative, treated with breast-conserving surgery and radiotherapy. What is the most appropriate adjuvant systemic therapy?",
         ["Tamoxifen for 1 year", "Aromatase inhibitor for 5 years", "Trastuzumab for 1 year", "No further therapy", "Bevacizumab"], 1,
         "สไลด์: **ER/PgR บวก (ไม่ว่ากี่ %) → ยาต้านฮอร์โมน 5 ปี** · **หลังหมดประจำเดือน → aromatase inhibitor** (± tamoxifen สลับ) · ก่อนหมดประจำเดือน → tamoxifen\n\nHER2 ลบ จึงไม่ใช้ trastuzumab · ยาเคมีพิจารณาตามความเสี่ยง (ปัจจุบันใช้ genomic assay ช่วยตัดสิน) · AI ต้องติดตาม **มวลกระดูก**",
         "Postmenopausal ER+ → AI 5 ปี", "Adjuvant endocrine therapy", R("Breast cancer — early stage"), BR),
     mcq(N(15), "A 38-year-old woman has invasive breast cancer, HER2 IHC 3+, with 2 positive axillary nodes. In addition to chemotherapy, which adjuvant targeted therapy is indicated and for how long?",
         ["Cetuximab for 6 months", "Trastuzumab for 1 year", "Imatinib for 3 years", "Bevacizumab for 1 year", "Tamoxifen for 5 years only"], 1,
         "สไลด์: **HER2 บวก (IHC 3+ หรือ FISH บวก) → adjuvant trastuzumab 1 ปี** ร่วมกับยาเคมี · ปัจจุบันระยะ II–III มักให้ก่อนผ่าตัด (trastuzumab + pertuzumab + ยาเคมี)\n\n**ต้องตรวจ LVEF ก่อนและระหว่างให้ยา** — trastuzumab ทำให้หัวใจบีบตัวลด (ส่วนใหญ่ผันกลับได้) โดยเฉพาะหลัง anthracycline · ถ้า ER บวกด้วยให้ยาต้านฮอร์โมนร่วม",
         "HER2 3+/FISH+ → trastuzumab 1 ปี + เฝ้า LVEF", "HER2-positive breast cancer", R("Breast cancer — adjuvant trastuzumab"), BR + ["B1.7.3"]),
     mcq(N(16), "A 35-year-old woman's mother had breast cancer at 40 and her maternal aunt had ovarian cancer. Which is the most appropriate next step?",
         ["Start mammography at age 50", "Refer for genetic counselling and BRCA1/2 testing", "Prophylactic tamoxifen without assessment", "Annual CA-125 only", "No action is needed"], 1,
         "สไลด์: **HBOC** สงสัยเมื่อ **มะเร็งเต้านมอายุ < 45 ปี** และ **มะเร็งรังไข่ในครอบครัว** → ส่ง **ให้คำปรึกษาทางพันธุกรรมและตรวจ BRCA1/2**\n\nผู้มียีน: **mammogram/MRI เต้านมตั้งแต่ 30 ปี (หรือ 25)** และพิจารณาผ่าตัดป้องกัน · CA-125 อย่างเดียวไม่มีประโยชน์ในการคัดกรอง",
         "เต้านม < 45 + รังไข่ในครอบครัว → BRCA testing", "Hereditary breast–ovarian cancer", R("Breast cancer — hereditary breast-ovarian cancer"), BR),
     mcq(N(17), "A 58-year-old postmenopausal woman, 4 years after treatment for ER-positive, HER2-negative breast cancer, presents with back pain. Imaging shows multiple bone metastases only; liver and lungs are clear. She is well. What is the preferred first-line systemic approach?",
         ["Anthracycline chemotherapy", "Endocrine therapy (an aromatase inhibitor, currently combined with a CDK4/6 inhibitor) plus a bone-modifying agent", "Trastuzumab", "Best supportive care only", "Radical mastectomy"], 1,
         "สไลด์: **HR บวก + แพร่ไปกระดูก/เนื้อเยื่ออ่อน หรืออวัยวะภายในเล็กน้อยไม่มีอาการ → ยาต้านฮอร์โมนแบบประคับประคอง** · ยาเคมีสงวนไว้สำหรับ **visceral crisis** หรือ HR ลบ\n\nมาตรฐานปัจจุบัน (ไม่ได้มาจากสไลด์): **AI + CDK4/6 inhibitor** · ร่วมกับ **bisphosphonate/denosumab** ลดภาวะแทรกซ้อนของกระดูก · ฉายแสงจุดที่ปวด",
         "HR+ แพร่ไปกระดูก ไม่มี visceral crisis → endocrine (+ CDK4/6i)", "Metastatic breast cancer", R("Breast cancer — metastatic") + ["ESMO/NCCN metastatic breast cancer"], BR + ["B5.2.4-3(2)"]),
    ], BR + ["B1.7.3"], SRC + " · USPSTF 2024 · NCCN/ESMO breast")

# ───────────────────────────── MEQ / OSCE
LECNAME = "General oncology (พญ.ปิยวรรณ)"
MEQ = [{"id": "HON-ONC-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Breast mass — diagnosis, subtype-based adjuvant therapy and survivorship",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 44 ปี ยังมีประจำเดือน คลำพบก้อนที่เต้านมซ้าย 2 เดือน ไม่เจ็บ
ประวัติครอบครัว: มารดาเป็นมะเร็งรังไข่อายุ 52 ปี
PE: ก้อนแข็ง ขอบไม่เรียบ ขนาด 2.5 ซม. ที่ upper outer quadrant ไม่ติดผิวหนัง · คลำต่อมน้ำเหลืองรักแร้ซ้ายได้ 1 ต่อม ขนาด 1 ซม. เคลื่อนได้
Mammogram/US: BI-RADS 5 · core biopsy: invasive ductal carcinoma grade 2 · ER 80% · PgR 50% · HER2 IHC 3+ · Ki-67 30%
CT chest/abdomen และ bone scan: ไม่พบการแพร่กระจาย · ECOG 0""",
 "questions": [
  {"q": "1. จงบอกชนิดย่อยของมะเร็งเต้านมรายนี้ และปัจจัยพยากรณ์ที่สำคัญที่สุด (2 คะแนน)",
   "a": """- ชนิดย่อย: **Hormone receptor บวก และ HER2 บวก** (ER/PgR+ · HER2 IHC 3+)
- ปัจจัยพยากรณ์ที่สำคัญที่สุด: **สถานะต่อมน้ำเหลืองรักแร้** (รายนี้สงสัยบวก → ยืนยันด้วย FNA/core biopsy)"""},
  {"q": "2. เป้าหมายการรักษาคืออะไร และวางแผนการรักษาเฉพาะที่และการรักษาทั้งระบบ (5 คะแนน)",
   "a": """- **เป้าหมาย: หายขาด (curative)** — ระยะแรก ไม่แพร่กระจาย ECOG 0
- เฉพาะที่: **ผ่าตัดสงวนเต้า + ฉายแสง** หรือ **MRM** · รักแร้: ต่อมน้ำเหลืองบวกยืนยันแล้ว → ALND (หรือ SLNB หลัง neoadjuvant ในรายที่ตอบสนองตามแนวทางปัจจุบัน)
- ทั้งระบบ (สไลด์):
  - **ยาเคมี** (anthracycline-based ± taxane) — ต่อมน้ำเหลืองบวก ก้อน > 2 ซม. HER2+
  - **Trastuzumab 1 ปี** — HER2 3+
  - **ยาต้านฮอร์โมน 5 ปี — tamoxifen** เพราะยังไม่หมดประจำเดือน
  - ฉายแสงหลังผ่าตัด
- *ปัจจุบัน (ไม่ได้มาจากสไลด์)*: HER2+ ระยะ II ขึ้นไป มักให้ **ยาก่อนผ่าตัด (trastuzumab + pertuzumab + ยาเคมี)** — ถ้ายังเหลือก้อนหลังผ่าตัด เปลี่ยนเป็น **T-DM1**"""},
  {"q": "3. ต้องตรวจหรือเฝ้าระวังอะไรระหว่างได้ trastuzumab และ tamoxifen (3 คะแนน)",
   "a": """- **Trastuzumab**: **echocardiogram/LVEF ก่อนเริ่มและทุก 3 เดือน** — หัวใจบีบตัวลด (มักผันกลับได้) เสี่ยงมากขึ้นเมื่อได้ anthracycline ร่วม
- **Tamoxifen**: **เลือดออกทางช่องคลอดผิดปกติ** (มะเร็งเยื่อบุโพรงมดลูก) · **ลิ่มเลือดดำ** · อาการร้อนวูบวาบ · ยาที่ยับยั้ง CYP2D6 แรง (paroxetine fluoxetine) ลดฤทธิ์
- ยาเคมี: **ไข้ระหว่างเม็ดเลือดขาวต่ำ = ภาวะฉุกเฉิน** · anthracycline พิษหัวใจสะสม"""},
  {"q": "4. ประวัติครอบครัวมีความสำคัญอย่างไร และจะแนะนำอะไร (2 คะแนน)",
   "a": """- มะเร็งเต้านมก่อน 45 ปี + มารดาเป็นมะเร็งรังไข่ → สงสัย **HBOC** → **ให้คำปรึกษาทางพันธุกรรมและตรวจ BRCA1/2**
- ถ้ายีนบวก: มีผลต่อการผ่าตัด (พิจารณาตัดเต้านมสองข้าง/ผ่าตัดรังไข่และท่อนำไข่ป้องกัน) และ **ตรวจคัดกรองญาติสายตรง** (เริ่มคัดกรองตั้งแต่อายุ 25–30 ปีด้วย MRI/mammogram)"""}],
 "ref": ["สไลด์ พญ.ปิยวรรณ — breast cancer", "NCCN/ESMO early breast cancer guidelines"],
 "nl": ["B10.2.4-3(4)", "2.1.55", "B1.7.3"], "years": [], "_kind": "meq", "_set": SET}]

OSCE = [{"id": "HON-ONC-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Anticancer drugs: mechanism, biomarker and key toxicity",
 "station": "SAQ (เขียนตอบ) 6 นาที",
 "instruction": """จงบอก **กลไก/ระยะของวงจรเซลล์หรือเป้าหมาย** และ **ผลข้างเคียงสำคัญ 1 อย่างที่ต้องเฝ้าระวัง** ของยาต่อไปนี้ และบอก **biomarker ที่ต้องตรวจก่อนใช้** ถ้ามี

| ยา | ใช้ใน |
|---|---|
| A. Doxorubicin | มะเร็งเต้านม lymphoma |
| B. Vincristine | lymphoma ALL |
| C. Cisplatin | มะเร็งอัณฑะ ปอด ปากมดลูก |
| D. Trastuzumab | มะเร็งเต้านม |
| E. Cetuximab | มะเร็งลำไส้ใหญ่ระยะแพร่กระจาย |
| F. Pembrolizumab | NSCLC melanoma MSI-H tumours |""",
 "answer": """| ยา | กลไก/ระยะ | Biomarker | พิษที่ต้องเฝ้าระวัง | คะแนน |
|---|---|---|---|---|
| **A. Doxorubicin** | Anthracycline — **topoisomerase II inhibitor** แทรก DNA (S phase ตามสไลด์) | — | **หัวใจล้มเหลว ตามขนาดสะสม** → LVEF | 2 |
| **B. Vincristine** | **M phase — ยับยั้ง microtubule** | — | **ปลายประสาทอักเสบ ท้องผูก** (ไม่กดไขกระดูก) | 2 |
| **C. Cisplatin** | Platinum — **เชื่อม DNA ไม่จำเพาะระยะ** | — | **ไตวาย Mg ต่ำ หูตึง** คลื่นไส้รุนแรง → ให้สารน้ำ | 2 |
| **D. Trastuzumab** | **Monoclonal antibody ต่อ HER2** | **HER2 IHC 3+ หรือ FISH+** | **หัวใจบีบตัวลด (ผันกลับได้)** → LVEF | 2 |
| **E. Cetuximab** | **Monoclonal antibody ต่อ EGFR** | **RAS (KRAS/NRAS) wild-type** | **ผื่นแบบสิว** Mg ต่ำ แพ้ระหว่างหยด | 2 |
| **F. Pembrolizumab** | **Anti-PD-1 immune checkpoint inhibitor** | PD-L1 (NSCLC) · **MSI-H/dMMR** | **irAE** — colitis hepatitis pneumonitis ไทรอยด์ | 2 |""",
 "ref": ["สไลด์ พญ.ปิยวรรณ — chemotherapy and cancer cell, targeted therapy, immuno-oncology"],
 "nl": ["B1.7.3", "B1.4.14", "B1.6.4(1)"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "จ. 2 พ.ย.",
 "title": "General oncology",
 "subtitle": "ระบาดวิทยา · เป้าหมายการรักษาและ performance status · วงจรเซลล์และ hallmarks · ยาเคมีตามระยะของวงจรเซลล์ · targeted therapy และ immunotherapy · มะเร็งเต้านม",
 "objectives": [
   "บอกมะเร็งที่พบบ่อยของโลกและประเทศไทย และปัจจัยเสี่ยงที่ป้องกันได้",
   "แยกเป้าหมายการรักษาระยะแรกกับระยะลุกลาม และความหมายของ neoadjuvant/adjuvant",
   "ประเมิน performance status และปัจจัยของมะเร็งที่มีผลต่อการเลือกการรักษา",
   "อธิบายการควบคุมวงจรเซลล์ hallmarks of cancer และการก่อมะเร็งหลายขั้นตอน",
   "จัดกลุ่มยาเคมีตามระยะของวงจรเซลล์ และบอกพิษเฉพาะของยาหลัก",
   "อธิบายกลไก biomarker และพิษของยามุ่งเป้าและ immune checkpoint inhibitor",
   "วางแผนคัดกรอง วินิจฉัยชนิดย่อย และรักษามะเร็งเต้านมตามระยะ"],
 "nlGap": "เกณฑ์ฯ มีรหัสวิทยาศาสตร์พื้นฐาน `นล. B1.6.4` Neoplasm · `B1.7.3` General principles of antineoplastic agents · `B1.4.12` Tumor immunology · `B10.2.4-3(4)` Malignant neoplasm of reproductive system (breast) · `2.1.55` Breast mass แต่ **ไม่มีรหัสของ immune checkpoint inhibitor, irAE หรือ performance status** โดยตรง และสไลด์ใช้ข้อมูล GLOBOCAN 2012 และการรักษามะเร็งเต้านมก่อนยุค CDK4/6 inhibitor จึงอ้างอิงแนวทางด้านล่าง",
 "guidelines": [
   "**GLOBOCAN 2022 (IARC, CA Cancer J Clin 2024)** — อุบัติการณ์และการตายจากมะเร็งทั่วโลก",
   "**Hanahan D. Hallmarks of cancer: new dimensions (Cancer Discovery 2022)** — ต่อจากฉบับ 2000 และ 2011 ที่อยู่ในสไลด์",
   "**ASCO Guideline: Management of immune-related adverse events (2021)** และ **ESMO irAE guideline (2022)**",
   "**USPSTF Breast cancer screening (2024)** — mammogram ทุก 2 ปี อายุ 40–74",
   "**NCCN/ESMO Breast cancer guidelines** — CDK4/6 inhibitor ใน HR+ แพร่กระจาย · KEYNOTE-522 ใน TNBC · neoadjuvant ใน HER2+",
   "**NCCN/ESMO Colon cancer** — adjuvant FOLFOX/CAPOX ใน stage III · anti-EGFR เฉพาะ RAS wild-type"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

HEMONC_META = {"set": "hemonc", "title": "Heme/Onc · โลหิตวิทยาและมะเร็งวิทยา",
 "intro": "ชุดใหม่ของโลหิตวิทยาและมะเร็งวิทยา เริ่มจากคาบ **General oncology ของ พญ.ปิยวรรณ (2 พ.ย.)** — ระบาดวิทยา เป้าหมายการรักษา performance status วงจรเซลล์และ hallmarks of cancer ยาเคมีตามระยะของวงจรเซลล์ ยามุ่งเป้า immunotherapy และมะเร็งเต้านม พร้อมอัปเดตแนวทางที่เปลี่ยนไปหลังสไลด์",
 "howto": "**วิธีใช้** — อ่านเนื้อหาให้จบแล้วตอบข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมคำอธิบายทันที · ข้อที่ตอบผิดรวมอยู่ในแท็บ **ทบทวนข้อที่ผิด** · จบคาบแล้วฝึก **MEQ** และ **OSCE/SAQ**\n\n**ลำดับที่แนะนำ** — หัวข้อ 5 (ยาเคมีตามระยะของวงจรเซลล์และพิษเฉพาะยา) และหัวข้อ 8 (มะเร็งเต้านม) ออกสอบบ่อยที่สุด ฝึกทำตาราง SAQ ยาต้านมะเร็งให้ได้เอง\n\n**หมายเหตุ** — ชุดนี้ยังไม่มีคลังข้อสอบเก่ารายคาบใน Ward Drill จึงผูกข้อจาก Mock exam หมวด Oncology ที่ตรงเรื่องแทน · ข้อความที่ไม่ได้มาจากสไลด์มีระบุไว้ทุกจุด",
 "label": "Heme/Onc", "thai": "โลหิตวิทยาและมะเร็งวิทยา",
 "accent": {"light": "#8a2a63", "soft": "#f5e6ef", "ink": "#6c1f4d", "dark": "#f59ac9", "darkSoft": "#26141e", "darkInk": "#f8bddb"},
 "file": "data/hemonc.json", "lectureCount": 1}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ก่อนขึ้นเว็บครั้งแรกเท่านั้น) · ข้อ 3 เรียง ECOG 0–4 คงไว้
_slot = 0
for s_ in S:
    for it in s_["items"]:
        if it["id"] in {N(3)}:
            continue
        tgt = [0, 3, 1, 4, 2][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", SET + ".json")
data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
data = [l for l in data if l.get("lec") != LEC] + [LECTURE]
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
if not any(m["set"] == SET for m in idx):
    idx.append(HEMONC_META)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

added = link_mock(SET, LEC, {"hon-onc-01": ["MOCK-027"], "hon-onc-02": ["MOCK-026", "MOCK-024"],
                             "hon-onc-08": ["MOCK-025", "MOCK-038"]})

d = json.load(open(path, encoding="utf-8"))
L = [l for l in d if l["lec"] == LEC][0]
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s_ in L["sections"] for c in s_["nl"]} | {c for s_ in L["sections"] for i in s_["items"] for c in i.get("nl", [])} | {c for m in L["meq"] + L["osce"] for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == SET: m["lectureCount"] = len(d)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + mock %d | meq %d | osce %d | nl %d" % (len(S), sum(len(s_["items"]) for s_ in S), added, len(MEQ), len(OSCE), len(codes)))
