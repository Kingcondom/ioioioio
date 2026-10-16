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

# ───────────────────────────── 9
TM = ["B1.6.4(2)", "B1.6.4(3)", "3.3.24"]
sec("hon-onc-09", "Staging, grading และ tumour markers",
    "TNM บอกระยะ grade บอกความดุ · tumour marker ใช้ติดตามผลและหาการกลับเป็นซ้ำ ไม่ใช้วินิจฉัยหรือคัดกรอง (ยกเว้นบางตัว) · CEA AFP CA19-9 CA-125 PSA β-hCG LDH", 9,
"""> หัวข้อ 9–13 **ไม่ได้มาจากสไลด์** — สไลด์ประกาศหัวข้อ "Common cancer" แต่ในไฟล์มีรายละเอียดเฉพาะมะเร็งเต้านม จึงเติมจากตำราและแนวทางปัจจุบันให้ครอบคลุมมะเร็งที่ออกสอบบ่อยและข้อ Mock หมวด Oncology

### Staging กับ grading
| | **Stage (ระยะ)** | **Grade (ความดุ)** |
|---|---|---|
| บอกอะไร | **ขนาดและการลุกลาม — TNM** (T ก้อน · N ต่อมน้ำเหลือง · M แพร่กระจาย) | **เซลล์ผิดปกติแค่ไหน** — well / moderately / poorly differentiated · mitosis · Ki-67 |
| ใช้ทำอะไร | **ตัวกำหนดพยากรณ์และการรักษาที่สำคัญที่สุด** | ช่วยทำนายพฤติกรรม และการตอบสนองต่อยาเคมี (หัวข้อ 3) |
- **Clinical stage (cTNM)** จากตรวจร่างกายและภาพถ่าย · **pathological stage (pTNM)** จากชิ้นเนื้อผ่าตัด
- การหา M: **CT ทรวงอก ช่องท้อง เชิงกราน** เป็นพื้นฐานของมะเร็งก้อนตันส่วนใหญ่ · bone scan เมื่อปวดกระดูก/ALP สูง หรือมะเร็งที่ชอบกระดูก · PET-CT ในบางโรค · MRI สมองในมะเร็งปอด

### Tumour markers
| Marker | มะเร็งหลัก | สูงได้จากเหตุอื่น |
|---|---|---|
| **CEA** | **ลำไส้ใหญ่** (ติดตามหลังผ่าตัด) | สูบบุหรี่ ลำไส้อักเสบ ตับแข็ง |
| **AFP** | **HCC · germ cell (non-seminoma, yolk sac)** | ตับอักเสบ ตั้งครรภ์ |
| **CA 19-9** | **ตับอ่อน · ท่อน้ำดี** | **ท่อน้ำดีอุดตัน/อักเสบ** (ลดลงหลังระบาย) · คนที่ไม่มี Lewis antigen ไม่สร้าง |
| **CA-125** | **มะเร็งรังไข่ชนิด epithelial** | **ประจำเดือน endometriosis PID ตั้งครรภ์ น้ำในช่องท้อง/เยื่อหุ้มปอด** |
| **PSA** | **ต่อมลูกหมาก** | ต่อมลูกหมากโต อักเสบ หลังสวนปัสสาวะ |
| **β-hCG** | **choriocarcinoma · germ cell** · gestational trophoblastic disease | ตั้งครรภ์ |
| **LDH** | lymphoma · germ cell · melanoma (พยากรณ์) | เม็ดเลือดแดงแตก เนื้อเยื่อตาย |
| Calcitonin · thyroglobulin | medullary · differentiated thyroid ca (ติดตามหลังผ่าตัด) | |

**หลักใช้**
1. **ไม่ใช้วินิจฉัยแทนชิ้นเนื้อ** — ไวและจำเพาะไม่พอ · **การวินิจฉัยมะเร็งต้องได้ชิ้นเนื้อเสมอ** (ยกเว้น HCC ที่ภาพ CT/MRI เข้าเกณฑ์ LI-RADS 5 ในตับแข็ง)
2. **ไม่ใช้คัดกรองประชากรทั่วไป** (ยกเว้น **AFP + US ในผู้เสี่ยง HCC** และ PSA แบบตัดสินใจร่วมกัน)
3. **ใช้ดีที่สุดเพื่อติดตามการตอบสนองและการกลับเป็นซ้ำ** — ต้องสูงก่อนรักษาจึงจะใช้ติดตามได้
4. Germ cell tumour: **AFP β-hCG LDH** ใช้ทั้งวินิจฉัยร่วม จัดระยะ (S stage) และติดตาม · **seminoma บริสุทธิ์ไม่สร้าง AFP**
""",
    ["Stage (TNM) = พยากรณ์และการรักษาสำคัญที่สุด · grade = ความดุ",
     "วินิจฉัยมะเร็งต้องได้ชิ้นเนื้อ — marker ใช้ติดตาม",
     "CEA ลำไส้ · AFP HCC/non-seminoma · CA19-9 ตับอ่อน · CA-125 รังไข่ · PSA ต่อมลูกหมาก · β-hCG germ cell",
     "CA19-9 สูงเท็จในท่อน้ำดีอุดตัน · CA-125 สูงเท็จใน endometriosis/PID/น้ำในช่องท้อง"],
    [mcq(N(18), "A 64-year-old man had a curative resection for stage III colon cancer. His preoperative CEA was 18 ng/mL and fell to normal after surgery. What is the main role of measuring CEA during follow-up?",
         ["To screen his siblings for colon cancer", "To detect recurrence early during surveillance", "To replace colonoscopy", "To confirm the original diagnosis", "To choose between FOLFOX and CAPOX"], 1,
         "Tumour marker **ใช้ดีที่สุดเพื่อติดตามการตอบสนองและการกลับเป็นซ้ำ** โดยเฉพาะเมื่อ **สูงก่อนรักษาแล้วลดลงหลังผ่าตัด** — CEA ที่กลับขึ้นใหม่ทำให้ต้องหาการกลับเป็นซ้ำด้วย CT\n\nCEA **ไม่ใช้คัดกรองหรือวินิจฉัย** (สูงได้ในคนสูบบุหรี่ ตับแข็ง ลำไส้อักเสบ) และไม่แทนการส่องกล้องตามนัด",
         "Marker ที่สูงก่อนรักษา → ใช้ติดตามการกลับเป็นซ้ำ", "Tumour markers", ["NCCN colon cancer survivorship"], TM + ["B8.2.4-3(1)"]),
     mcq(N(19), "A 30-year-old woman with pelvic pain and fever has a tender adnexal mass and CA-125 of 160 U/mL. Which statement is most accurate?",
         ["CA-125 confirms ovarian cancer", "CA-125 can be raised by pelvic inflammatory disease, endometriosis and menstruation, so it is non-specific in premenopausal women", "CA-125 is a screening test for all women",
          "CA-125 is specific for mucinous tumours", "A raised CA-125 excludes infection"], 1,
         "**CA-125 ไม่จำเพาะ** โดยเฉพาะ **ก่อนหมดประจำเดือน** — สูงได้จาก **PID/ฝีที่ท่อนำไข่และรังไข่ endometriosis ประจำเดือน ตั้งครรภ์ น้ำในช่องท้อง** · หญิงอายุน้อย มีไข้ กดเจ็บ → นึกถึง **tubo-ovarian abscess** ก่อน\n\nCA-125 มีค่ามากในหญิงหลังหมดประจำเดือนที่มีก้อนรังไข่ และใช้ **ติดตาม** มะเร็งรังไข่ชนิด epithelial · ไม่ใช้คัดกรองประชากร",
         "CA-125 สูงเท็จใน PID endometriosis ก่อนหมดประจำเดือน", "Tumour markers", ["Standard gynaecologic oncology practice"], TM + ["B10.2.4-3(4)"]),
    ], TM, "เพิ่มเติม (ไม่ได้มาจากสไลด์) — AJCC 8th · NCCN")

# ───────────────────────────── 10
SCR = ["B1.6.4(4)", "B1.3.4(1)"]
sec("hon-onc-10", "คัดกรองและป้องกันมะเร็ง",
    "เต้านม mammogram · ปากมดลูก HPV DNA · ลำไส้ใหญ่ FIT/colonoscopy · ปอด LDCT ในผู้สูบบุหรี่ · HCC US + AFP ทุก 6 เดือนในผู้เสี่ยง · วัคซีน HBV HPV", 9,
"""### เกณฑ์ของโปรแกรมคัดกรองที่ดี
โรคพบบ่อยและรุนแรง · มีระยะก่อนอาการที่ตรวจพบได้ · การตรวจแม่นและยอมรับได้ · **รักษาเร็วแล้วลดการตายได้จริง**
> ระวัง **lead-time bias** (เจอเร็วขึ้นดูเหมือนรอดนานขึ้น) และ **overdiagnosis** (เจอโรคที่ไม่เคยทำอันตราย เช่น มะเร็งต่อมลูกหมากบางส่วน มะเร็งไทรอยด์ขนาดเล็ก)

### ตารางคัดกรองหลัก (ไม่ได้มาจากสไลด์)
| มะเร็ง | ใคร | วิธี |
|---|---|---|
| **เต้านม** | หญิง **40–74 ปี** (USPSTF 2024) | **Mammogram ทุก 2 ปี** (สไลด์: ปีละครั้งช่วง 40–50) · BRCA: MRI ปีละครั้งตั้งแต่ 25–30 |
| **ปากมดลูก** | หญิง **25/30–65 ปี** | **HPV DNA ทุก 5 ปี** (โครงการ สปสช. 30–60 ปี · เก็บเองได้) หรือ Pap smear ทุก 3 ปี |
| **ลำไส้ใหญ่** | **45/50–75 ปี** (ไทย 50–70 ปี) | **FIT ทุกปี** → บวก → **colonoscopy** · หรือ colonoscopy ทุก 10 ปี · ญาติสายตรงเป็นก่อน 60 → เริ่ม 40 หรือก่อนอายุญาติ 10 ปี |
| **ปอด** | **50–80 ปี สูบ ≥ 20 pack-year** ยังสูบหรือเลิก < 15 ปี (USPSTF 2021) | **Low-dose CT ปีละครั้ง** — CXR ไม่ลดการตาย |
| **ตับ (HCC)** | **ตับแข็งทุกสาเหตุ · HBV เรื้อรังกลุ่มเสี่ยง** (ชาย > 40 หญิง > 50 ปี ประวัติครอบครัว) | **อัลตราซาวนด์ ± AFP ทุก 6 เดือน** |
| **ต่อมลูกหมาก** | ชาย 55–69 ปี | **PSA แบบตัดสินใจร่วมกัน (shared decision)** — ไม่คัดกรองทุกคน |
| **ท่อน้ำดี** | ภาคอีสาน กินปลาดิบ | ตรวจอุจจาระหาพยาธิ · US ในโครงการ CASCAP |

### การป้องกัน
- **เลิกบุหรี่** — ลดมะเร็งปอด ศีรษะและคอ หลอดอาหาร กระเพาะปัสสาวะ ตับอ่อน
- **วัคซีน HBV** (แรกเกิด) → ลด HCC · **วัคซีน HPV** (หญิงและชาย 9–26 ปี · ไทยให้นักเรียนหญิง ป.5) → ลดมะเร็งปากมดลูก ทวารหนัก ช่องปากและคอ
- **รักษา HBV/HCV** · **กำจัดพยาธิใบไม้ตับ งดปลาดิบ** · ลดเหล้า น้ำหนัก เนื้อแดง/เนื้อแปรรูป
- **ยาป้องกัน**: tamoxifen/AI ในหญิงเสี่ยงสูงต่อมะเร็งเต้านม · aspirin ใน Lynch syndrome
""",
    ["Mammogram 40–74 ทุก 2 ปี · HPV DNA ทุก 5 ปี · FIT ทุกปี 50–70 (ไทย)",
     "ปอด: LDCT ปีละครั้ง 50–80 ปี ≥ 20 pack-year — CXR ไม่ช่วย",
     "HCC: US ± AFP ทุก 6 เดือนในตับแข็ง/HBV เสี่ยง",
     "PSA = shared decision · ระวัง overdiagnosis และ lead-time bias"],
    [mcq(N(20), "A 52-year-old woman asks about colorectal cancer screening. She has no symptoms and no family history. Which approach is appropriate in the Thai national programme?",
         ["Serum CEA every year", "Annual faecal immunochemical test (FIT), with colonoscopy if positive", "Barium enema every year", "CT abdomen every 2 years", "No screening until age 70"], 1,
         "โครงการคัดกรองมะเร็งลำไส้ใหญ่ของไทย: **อายุ 50–70 ปี ตรวจ FIT** → **ผลบวกส่ง colonoscopy** · ทางเลือกอื่นคือ colonoscopy ทุก 10 ปี (แนวทางสหรัฐฯ เริ่มที่ 45 ปี)\n\n**CEA ไม่ใช้คัดกรอง** (ไวต่ำ ไม่จำเพาะ)\n\n*(ไม่ได้มาจากสไลด์)*",
         "คัดกรองลำไส้ใหญ่ไทย: FIT 50–70 → บวก → colonoscopy", "Cancer screening", ["Thai national CRC screening programme · USPSTF 2021"], SCR + ["B8.2.4-3(1)"]),
    ], SCR, "เพิ่มเติม (ไม่ได้มาจากสไลด์) — USPSTF · สปสช.")

# ───────────────────────────── 11
GI_LUNG = ["B6.2.4-3(2)", "B8.2.4-3(1)", "B8.2.4-3(2)", "2.3.2-3(1)"]
sec("hon-onc-11", "มะเร็งที่พบบ่อย 1 — ปอด ลำไส้ใหญ่ ตับ และทางเดินอาหารส่วนบน",
    "NSCLC vs SCLC · paraneoplastic · ตรวจ driver mutation · CRC ระยะลุกลาม FOLFOX/FOLFIRI + ยามุ่งเป้า · HCC จาก HBV · กระเพาะ Virchow node · หลอดอาหาร กลืนลำบากต้องส่องกล้อง", 13,
"""### มะเร็งปอด
| | **Non-small cell (85%)** | **Small cell (15%)** |
|---|---|---|
| ชนิด | **Adenocarcinoma** (พบบ่อยสุด อยู่รอบนอก ไม่สูบบุหรี่ก็เป็น) · **squamous** (กลางปอด สูบบุหรี่ hypercalcemia จาก PTHrP) · large cell | สัมพันธ์บุหรี่มาก อยู่กลางปอด โตเร็ว **แพร่กระจายเร็ว** |
| Paraneoplastic | **Hypercalcemia (PTHrP — squamous)** · hypertrophic osteoarthropathy | **SIADH · Cushing (ACTH) · Lambert–Eaton** |
| รักษา | ระยะ I–II: **ผ่าตัด** · III: เคมี-ฉายแสง + immunotherapy · IV: **ตรวจ driver mutation (EGFR ALK ROS1 …) + PD-L1** → ยามุ่งเป้า หรือ immunotherapy ± เคมี | **ไวต่อเคมีและรังสีมาก** — **etoposide + platinum** (+ atezolizumab/durvalumab) · ไม่ผ่าตัด · **กลับเป็นซ้ำเร็ว** |
- อาการ: ไอเรื้อรัง ไอเป็นเลือด น้ำหนักลด · **Pancoast tumour** (ยอดปอด → Horner, ปวดแขน) · **SVC syndrome** · เสียงแหบ (recurrent laryngeal nerve)
- **Mesothelioma** — สัมผัส **แร่ใยหิน (asbestos)** · เยื่อหุ้มปอดหนาเป็นปุ่ม + น้ำในเยื่อหุ้มปอด · latency 20–40 ปี

### มะเร็งลำไส้ใหญ่และทวารหนัก
- **Adenoma → carcinoma** (APC → KRAS → TP53) · ปัจจัยเสี่ยง: อายุ ประวัติครอบครัว **Lynch (MSI-H) · FAP** · IBD · เนื้อแดง อ้วน
- **ซ้าย**: ถ่ายเปลี่ยน อุจจาระเล็กลง ถ่ายเป็นเลือด ลำไส้อุดตัน · **ขวา**: **ซีดจากขาดเหล็ก** ก้อนท้องขวาล่าง · **ชายสูงอายุ/หญิงหมดประจำเดือนที่ขาดเหล็ก → ส่องกล้องทั้งบนและล่าง**
- วินิจฉัย: **colonoscopy + ชิ้นเนื้อ** · จัดระยะ: **CT ทรวงอก ช่องท้อง เชิงกราน + CEA** · มะเร็งทวารหนัก: MRI เชิงกราน
- **ระยะแพร่กระจาย (สไลด์ advanced colon เป็นภาพ — สรุปจากแนวทาง)**: **FOLFOX หรือ FOLFIRI** (หรือ CAPOX) + **bevacizumab** หรือ **cetuximab/panitumumab (RAS wild-type และก้อนข้างซ้าย)** · **MSI-H/dMMR → pembrolizumab ทางเลือกแรก** · BRAF V600E → encorafenib + cetuximab · แพร่ไปตับ/ปอดจำนวนน้อย → **ผ่าตัดออกอาจหายขาด** · การรอดชีวิตเฉลี่ยราว **30 เดือน** ด้วยยาหลายสาย

### ตับและท่อน้ำดี
- **HCC**: **HBV (สาเหตุนำในไทยและทั่วโลก)** HCV เหล้า MASLD aflatoxin · มักมีตับแข็ง · **วินิจฉัยด้วย CT/MRI หลายระยะ: arterial enhancement + washout** ได้โดยไม่ต้องเจาะ · รักษาตาม BCLC: ผ่าตัด/จี้/ปลูกถ่ายตับ → TACE → **atezolizumab + bevacizumab** หรือ durvalumab + tremelimumab
- **Cholangiocarcinoma**: พยาธิใบไม้ตับ (อีสาน) · PSC · เหลืองไม่ปวด · CA 19-9

### ทางเดินอาหารส่วนบนและตับอ่อน
- **หลอดอาหาร**: **squamous** (บุหรี่ เหล้า ส่วนกลาง) vs **adenocarcinoma** (GERD/Barrett ส่วนปลาย) · **กลืนลำบากที่ค่อย ๆ เป็นจากของแข็งไปของเหลว + น้ำหนักลด → ส่องกล้องตัดชิ้นเนื้อ**
- **กระเพาะ**: H. pylori · อิ่มเร็ว ปวดใต้ลิ้นปี่ น้ำหนักลด ซีด · **Virchow node (ไหปลาร้าซ้าย)** · Sister Mary Joseph (สะดือ) · Krukenberg (รังไข่) · **ส่องกล้องตัดชิ้นเนื้อ** · HER2 บวก → trastuzumab
- **ตับอ่อน**: หัวตับอ่อน → **เหลืองไม่ปวด + Courvoisier** · ปวดร้าวหลัง น้ำหนักลด เบาหวานเกิดใหม่ · Trousseau (ลิ่มเลือดดำย้ายที่) · CA 19-9 · ผ่าตัดได้เพียง 15–20%
""",
    ["SCLC: กลางปอด SIADH Cushing Lambert–Eaton · ไวยา etoposide + platinum · ไม่ผ่าตัด",
     "NSCLC ระยะ IV: ตรวจ EGFR ALK ROS1 … + PD-L1 ก่อนเลือกยา",
     "CRC ขวา: ซีดจากขาดเหล็ก · ซ้าย: ถ่ายเปลี่ยน/อุดตัน · ระยะ: CT C/A/P + CEA",
     "mCRC: FOLFOX/FOLFIRI + bevacizumab หรือ anti-EGFR (RAS wt ซ้าย) · MSI-H → pembrolizumab",
     "กลืนลำบาก + น้ำหนักลด → ส่องกล้อง · Virchow node = มะเร็งกระเพาะ"],
    [mcq(N(21), "A 63-year-old smoker has a central lung mass, confusion and serum sodium 118 mmol/L with euvolaemia and inappropriately concentrated urine. Biopsy is pending. Which histology is most likely?",
         ["Adenocarcinoma", "Squamous cell carcinoma", "Small cell lung carcinoma", "Bronchial carcinoid", "Mesothelioma"], 2,
         "**ก้อนกลางปอด + ผู้สูบบุหรี่ + SIADH (Na ต่ำ euvolemia ปัสสาวะเข้มข้น)** = **small cell lung cancer** — เซลล์ neuroendocrine หลั่ง ADH (และ ACTH) · ร่วมกับ Lambert–Eaton ได้\n\nSquamous สัมพันธ์กับ **hypercalcemia จาก PTHrP** · adenocarcinoma อยู่รอบนอกปอด\n\nSCLC **ไวต่อเคมีและรังสี** → etoposide + platinum ± immunotherapy\n\n*(ไม่ได้มาจากสไลด์)*",
         "SCLC = กลางปอด + SIADH/ACTH/LEMS", "Lung cancer", ["NCCN SCLC guideline"], GI_LUNG + ["2.3.4-3(5)"]),
     mcq(N(22), "A 66-year-old man presents with fatigue and iron-deficiency anaemia (Hb 8.9 g/dL, ferritin 6 ng/mL). He denies GI symptoms. Which investigation is most important?",
         ["Iron supplements and recheck in 3 months", "Bidirectional endoscopy (upper endoscopy and colonoscopy)", "Serum CEA", "Bone marrow biopsy", "Stool culture"], 1,
         "**ชายสูงอายุที่ขาดเหล็กโดยไม่มีสาเหตุชัด = เลือดออกจากทางเดินอาหารจนกว่าพิสูจน์เป็นอื่น** โดยเฉพาะ **มะเร็งลำไส้ใหญ่ซีกขวา** (มักไม่มีอาการลำไส้ มาด้วยซีด) และมะเร็งกระเพาะ\n\n→ **ส่องกล้องทั้งบนและล่าง** · ให้เหล็กได้แต่ห้ามแทนการสืบค้น · CEA ไม่ใช้วินิจฉัย",
         "ชายสูงอายุขาดเหล็ก → ส่องกล้องบน + ล่าง", "Colorectal cancer", ["BSG guideline for iron deficiency anaemia (2021)"], GI_LUNG),
     mcq(N(23), "A patient has newly diagnosed metastatic colorectal cancer with multiple liver metastases. Tumour testing shows mismatch-repair deficiency (dMMR/MSI-high). What is the preferred first-line systemic therapy?",
         ["Cetuximab alone", "Pembrolizumab (immune checkpoint inhibitor)", "Tamoxifen", "Imatinib", "Best supportive care only"], 1,
         "มะเร็ง **MSI-H/dMMR** มีการกลายพันธุ์จำนวนมาก → **neoantigen มาก** ระบบภูมิคุ้มกันมองเห็นได้ดี → ตอบสนองต่อ **immune checkpoint inhibitor** สูงและนาน (KEYNOTE-177: pembrolizumab ดีกว่าเคมีบำบัด) — สอดคล้องกับสไลด์ที่ระบุ **MSI-high CRC และ dMMR solid tumours** ในข้อบ่งใช้ ICI\n\nกรณีที่ไม่ใช่ MSI-H ใช้ FOLFOX/FOLFIRI + bevacizumab หรือ anti-EGFR (RAS wild-type)",
         "mCRC MSI-H/dMMR → pembrolizumab ก่อน", "Metastatic colorectal cancer", ["KEYNOTE-177 (NEJM 2020) · NCCN colon"] + R("Approved treatment for immune checkpoint inhibitors"), GI_LUNG + ["B1.4.14"]),
    ], GI_LUNG, "เพิ่มเติม (ไม่ได้มาจากสไลด์) — NCCN/ESMO · BCLC 2022")

# ───────────────────────────── 12
OTH = ["B10.2.4-3(4)", "B9.2.4-3(2)", "B11.2.4-3(2)", "B4.2.4-3(1)", "B3.2.4-3(2)", "B5.2.4-3(2)"]
sec("hon-onc-12", "มะเร็งที่พบบ่อย 2 — ต่อมลูกหมาก ปากมดลูก รังไข่ ไต ไทรอยด์ ผิวหนัง และสมอง",
    "PSA + ต้านฮอร์โมนเพศชาย · HPV 16/18 · รังไข่ CA-125 ผ่าตัด + platinum · RCC triad + polycythemia · papillary psammoma · BCC pearly · แพร่กระจายไปสมองพบบ่อยกว่าเนื้องอกปฐมภูมิ", 11,
"""### ระบบสืบพันธุ์และทางเดินปัสสาวะ
| มะเร็ง | จุดสำคัญ |
|---|---|
| **ต่อมลูกหมาก** | ชายสูงอายุ · มักไม่มีอาการ หรือปัสสาวะลำบาก ปวดกระดูก · **PSA + MRI → ชิ้นเนื้อ (Gleason/ISUP grade)** · ชอบแพร่ไป **กระดูกแบบ osteoblastic** · เฉพาะที่: เฝ้าติดตาม/ผ่าตัด/ฉายแสง · แพร่กระจาย: **ยาต้านฮอร์โมนเพศชาย (ADT)** + ARPI (abiraterone enzalutamide) ± docetaxel · กระดูก: **zoledronic acid/denosumab** |
| **ปากมดลูก** | **HPV 16/18** · เลือดออกหลังมีเพศสัมพันธ์ · squamous ส่วนใหญ่ · ระยะแรกผ่าตัด · ลุกลามเฉพาะที่: **เคมี-ฉายแสง (cisplatin)** · ป้องกันด้วยวัคซีนและคัดกรอง |
| **รังไข่** | อาการไม่ชัด **ท้องอืด อิ่มเร็ว** ก้อนในเชิงกราน น้ำในช่องท้อง · **CA-125** · BRCA · มักพบระยะ III · **ผ่าตัดลดก้อนให้มากที่สุด + carboplatin/paclitaxel** · BRCA/HRD → **PARP inhibitor (olaparib)** |
| **เยื่อบุโพรงมดลูก** | **เลือดออกหลังหมดประจำเดือน** · estrogen ไม่มี progesterone ต้าน (อ้วน PCOS **tamoxifen**) · Lynch |
| **ไต (RCC — clear cell)** | **ปัสสาวะเป็นเลือด + ปวดสีข้าง + ก้อน** (triad พบน้อย) · paraneoplastic: **polycythemia (EPO)** hypercalcemia · ส่วนใหญ่พบโดยบังเอิญจาก CT · VHL · **ผ่าตัด** · แพร่กระจาย: **IO + VEGFR-TKI** (ดื้อเคมีและรังสี) |
| **กระเพาะปัสสาวะ** | **ปัสสาวะเป็นเลือดไม่ปวด** ผู้สูบบุหรี่ สีย้อม · **cystoscopy** |
| **อัณฑะ (germ cell)** | ชายหนุ่ม ก้อนอัณฑะไม่เจ็บ · **AFP β-hCG LDH** · **ตัดอัณฑะทางขาหนีบ (ห้ามเจาะผ่านถุงอัณฑะ)** · **หายขาดได้แม้แพร่กระจาย (BEP)** |

### ไทรอยด์
| ชนิด | ลักษณะ |
|---|---|
| **Papillary (~80%)** | **psammoma bodies · ground-glass (Orphan Annie) nuclei · nuclear grooves** · แพร่ทางน้ำเหลือง · รังสีบริเวณคอ · พยากรณ์ดีมาก |
| Follicular | แพร่ทางเลือด (กระดูก ปอด) · ต้องดูการรุกแคปซูล/หลอดเลือด (FNA บอกไม่ได้) |
| **Medullary** | C cell → **calcitonin** · **MEN2 (RET)** |
| Anaplastic | ผู้สูงอายุ โตเร็วมาก พยากรณ์แย่ |

### ผิวหนัง
- **Basal cell carcinoma** — พบบ่อยที่สุด ใบหน้า (แสงแดด) **ตุ่มมันวาวขอบนูน (pearly) เส้นเลือดฝอย แผลตรงกลาง** · **แพร่กระจายน้อยมาก รุกเฉพาะที่** → **ผ่าตัดให้ขอบปลอดมะเร็ง** (Mohs บริเวณใบหน้า)
- **Squamous cell carcinoma** — แผลเรื้อรัง (Marjolin ulcer) actinic keratosis · แพร่กระจายได้มากกว่า BCC
- **Melanoma** — ABCDE · ความหนา (Breslow) คือพยากรณ์สำคัญ · ไทยพบ **acral lentiginous** (ฝ่าเท้า ใต้เล็บ) · ระยะลุกลาม: **anti-PD-1 ± anti-CTLA-4** · BRAF V600E → BRAF + MEK inhibitor

### สมอง
- **ก้อนในสมองของผู้ใหญ่ที่พบบ่อยที่สุดคือมะเร็งแพร่กระจายมา** — จาก **ปอด เต้านม melanoma ไต ลำไส้** · มักหลายก้อนที่รอยต่อเนื้อสมองขาว-เทา
- ปฐมภูมิ: **glioblastoma** (ผู้สูงอายุ ขอบ ring-enhancing เนื้อตาย ข้ามซีกผ่าน corpus callosum) · meningioma (ไม่ร้าย)
- รักษาก้อนแพร่กระจาย: **dexamethasone ลดสมองบวม** · ก้อนเดียว → ผ่าตัด/SRS · หลายก้อน → SRS หรือ whole-brain RT · ยามุ่งเป้าที่ผ่านสมองได้ (osimertinib, alectinib)
""",
    ["Prostate: PSA → MRI → biopsy · กระดูก osteoblastic · ADT",
     "รังไข่: ท้องอืด อิ่มเร็ว CA-125 · ผ่าตัด + carboplatin/paclitaxel · BRCA → PARPi",
     "RCC: hematuria flank pain mass + polycythemia · ดื้อเคมี/รังสี",
     "Papillary: psammoma + Orphan Annie nuclei · medullary: calcitonin MEN2",
     "BCC: pearly + telangiectasia ไม่ค่อยแพร่กระจาย → ผ่าตัดขอบปลอด",
     "ก้อนในสมองผู้ใหญ่ส่วนใหญ่ = แพร่กระจายมา (ปอด เต้านม melanoma)"],
    [mcq(N(24), "A 24-year-old man has a painless, firm right testicular mass. AFP and β-hCG are raised. What is the correct first step after scrotal ultrasound?",
         ["Fine-needle aspiration through the scrotum", "Radical inguinal orchiectomy", "Observation for 3 months", "Antibiotics for epididymitis", "Scrotal biopsy"], 1,
         "ก้อนอัณฑะแข็งไม่เจ็บในชายหนุ่ม + **AFP/β-hCG สูง** = **germ cell tumour (non-seminoma)** → **ตัดอัณฑะผ่านทางขาหนีบ (radical inguinal orchiectomy)** ซึ่งได้ทั้งวินิจฉัยและรักษา\n\n**ห้ามเจาะหรือตัดผ่านถุงอัณฑะ** เพราะเปลี่ยนทางระบายน้ำเหลืองและเพิ่มการกระจายเฉพาะที่ · แม้แพร่กระจายก็ **หายขาดได้สูงด้วย BEP** (ไวต่อเคมีมาก — หัวข้อ 5)",
         "ก้อนอัณฑะ → inguinal orchiectomy ห้ามผ่านถุงอัณฑะ", "Testicular cancer", ["EAU testicular cancer guideline"], ["B10.2.4-3(2)", "3.3.24", "2.1.49"]),
     mcq(N(25), "A 72-year-old man has worsening low back pain, PSA 210 ng/mL and multiple sclerotic (osteoblastic) lesions on bone scan. What is the backbone of systemic treatment?",
         ["Anthracycline chemotherapy", "Androgen deprivation therapy (with an androgen-receptor pathway inhibitor)", "Trastuzumab", "Tamoxifen", "Radical prostatectomy alone"], 1,
         "มะเร็งต่อมลูกหมากแพร่ไปกระดูก (**osteoblastic**) อาศัยฮอร์โมนเพศชาย → แกนหลักคือ **androgen deprivation therapy (GnRH agonist/antagonist หรือตัดอัณฑะ)** ปัจจุบันให้ร่วมกับ **abiraterone/enzalutamide/apalutamide** ± docetaxel\n\nร่วมกับ **bisphosphonate/denosumab** เมื่อดื้อต่อการตัดฮอร์โมน และเฝ้าระวัง **spinal cord compression** (ปวดหลังที่แย่ลง)",
         "Prostate แพร่กระจาย → ADT + ARPI", "Prostate cancer", ["NCCN/EAU prostate cancer"], ["B10.2.4-3(4)", "B5.2.4-3(2)"]),
    ], OTH, "เพิ่มเติม (ไม่ได้มาจากสไลด์) — NCCN/ESMO/EAU")

# ───────────────────────────── 13
EM = ["2.3.3(2)", "2.2.13", "2.2.38", "2.3.4(2)"]
sec("hon-onc-13", "ภาวะฉุกเฉินทางมะเร็งและการดูแลประคับประคอง",
    "Febrile neutropenia: antibiotic ภายใน 1 ชม. · TLS: สารน้ำ allopurinol/rasburicase · hypercalcemia: NSS + bisphosphonate · SVC syndrome · spinal cord compression: dexamethasone + MRI ด่วน · malignant effusion", 12,
"""### Febrile neutropenia
- **ไข้ ≥ 38.3 °C ครั้งเดียว หรือ ≥ 38.0 °C นาน 1 ชม.** + **ANC < 500** (หรือคาดว่าจะ < 500 ใน 48 ชม.) · มักช่วง **nadir 7–14 วันหลังยา**
- อาการอักเสบอาจไม่ชัดเพราะไม่มีเม็ดเลือดขาว
- **เพาะเชื้อแล้วให้ยาปฏิชีวนะครอบคลุม Pseudomonas ภายใน 1 ชม.** — **cefepime / piperacillin–tazobactam / meropenem** · เพิ่ม vancomycin เมื่อสงสัยติดเชื้อสายสวน ผิวหนัง ปอดอักเสบ MRSA หรือช็อก
- ความเสี่ยงต่ำ (MASCC ≥ 21) อาจกินยาที่บ้านได้ · ป้องกันด้วย G-CSF ในสูตรยาที่เสี่ยงสูง

### Tumour lysis syndrome
- เซลล์มะเร็งแตกจำนวนมากหลังเริ่มยา — **lymphoma/leukaemia ที่โตเร็ว (Burkitt ALL) ก้อนใหญ่ LDH สูง**
- **K สูง · phosphate สูง · uric acid สูง · Ca ต่ำ** (จับกับ phosphate) → **ไตวายเฉียบพลัน** หัวใจเต้นผิดจังหวะ ชัก
- ป้องกัน/รักษา: **สารน้ำมาก (ปัสสาวะ 80–100 มล./ชม.)** · **allopurinol** (ป้องกัน) · **rasburicase** (เสี่ยงสูงหรือ uric acid สูงแล้ว — ห้ามใน G6PD deficiency) · แก้ K · ฟอกไตเมื่อจำเป็น

### Hypercalcemia of malignancy
- กลไก: **PTHrP** (squamous cell — ปอด ศีรษะและคอ · ไต · เต้านม) · **ก้อนในกระดูกสลายกระดูก** (myeloma เต้านม) · **calcitriol** (lymphoma)
- **ซึม สับสน กระหายน้ำ ปัสสาวะมาก ท้องผูก ไตวาย** · PTH ต่ำ
- รักษา: **NSS ทางหลอดเลือด** (ขาดน้ำจาก nephrogenic DI) → **zoledronic acid** (ออกฤทธิ์ 2–4 วัน) · **calcitonin** (เร็วแต่สั้น) · denosumab เมื่อไตวาย · steroid ใน lymphoma · ไม่ใช้ furosemide เป็นหลัก

### SVC syndrome
- ก้อนในทรวงอกกดหลอดเลือดดำใหญ่ — **มะเร็งปอด (SCLC) · lymphoma** · สายสวนหลอดเลือด
- **หน้าบวม แดง เส้นเลือดที่คอและอกโป่ง แขนบวม** อาการแย่ลงเมื่อก้มหรือนอน
- **ต้องได้ชิ้นเนื้อก่อนให้ steroid/ฉายแสง** (ยกเว้นทางเดินหายใจหรือสมองบวมคุกคามชีวิต) · **stent หลอดเลือดดำ** ช่วยเร็ว · รักษาตามชนิดมะเร็ง

### Malignant spinal cord compression
- **ปวดหลังที่แย่ลงตอนกลางคืน/นอนราบ** ในผู้ป่วยมะเร็ง (ปอด เต้านม ต่อมลูกหมาก myeloma) → ขาอ่อนแรง ชา ปัสสาวะ/อุจจาระผิดปกติ (สายเกินไป)
- **Dexamethasone ทันที** → **MRI ทั้งกระดูกสันหลังภายใน 24 ชม.** → **ฉายแสง** หรือ **ผ่าตัดลดแรงกด + ฉายแสง** (ก้อนเดียว ยังเดินได้ไม่นาน กระดูกไม่มั่นคง)
- **ผลลัพธ์ขึ้นกับการเดินได้ก่อนรักษา** — ยังเดินได้มักเดินต่อได้

### Malignant pleural effusion
- กลไกหลัก: **เซลล์มะเร็งอุดท่อน้ำเหลืองของเยื่อหุ้มปอด ระบายน้ำไม่ได้** + เยื่อหุ้มปอดรั่ว
- **Exudate** · cytology บวก ~60% · เกิดซ้ำบ่อย → **pleurodesis (talc)** หรือ **สายระบายฝังใต้ผิวหนัง (IPC)** · ปอดไม่ขยาย (trapped lung) → IPC

### อาการอื่นที่ต้องดูแล
- **คลื่นไส้อาเจียนจากยาเคมี**: 5-HT3 antagonist (ondansetron) + **NK1 antagonist (aprepitant)** + dexamethasone ± olanzapine สำหรับยาก่ออาเจียนสูง (cisplatin)
- **ปวดจากมะเร็ง**: บันไดยา WHO · opioid ให้ยาตามเวลา + ยาระบายป้องกันท้องผูก
- **การดูแลแบบประคับประคองควบคู่ตั้งแต่เริ่ม** ในมะเร็งระยะลุกลาม — เพิ่มคุณภาพชีวิต (และอาจยืดชีวิต) · การแจ้งข่าวร้าย (SPIKES)
""",
    ["Febrile neutropenia: เพาะเชื้อ + cefepime/pip-tazo/meropenem ภายใน 1 ชม.",
     "TLS: K↑ PO4↑ urate↑ Ca↓ → สารน้ำ allopurinol rasburicase (ห้ามใน G6PD)",
     "Hypercalcemia: NSS → zoledronic acid · PTHrP ใน squamous",
     "SVC: ชิ้นเนื้อก่อน steroid/RT ถ้าไม่คุกคามชีวิต",
     "Cord compression: dexamethasone → MRI ทั้งแนวภายใน 24 ชม. → RT/ผ่าตัด"],
    [mcq(N(26), "Ten days after chemotherapy for breast cancer, a woman has a temperature of 38.6 °C, BP 118/70 mmHg and ANC 200/µL. No focus is found. After blood cultures, what is the most appropriate next step?",
         ["Wait for culture results before giving antibiotics", "Start IV anti-pseudomonal beta-lactam (e.g. cefepime or piperacillin–tazobactam) within 1 hour", "Oral amoxicillin at home", "G-CSF alone", "Start antifungal therapy only"], 1,
         "**Febrile neutropenia** (ไข้ ≥ 38.3 + ANC < 500 ช่วง nadir) เป็น **ภาวะฉุกเฉิน** — ติดเชื้อแกรมลบลุกลามเร็ว → **เพาะเชื้อแล้วให้ยาปฏิชีวนะต้าน Pseudomonas ทางหลอดเลือดภายใน 1 ชม.** (cefepime pip-tazo meropenem)\n\nไม่รอผลเพาะเชื้อ · ยาต้านเชื้อราพิจารณาเมื่อไข้ไม่ลง 4–7 วัน · G-CSF ไม่แทนยาปฏิชีวนะ\n\n*(ไม่ได้มาจากสไลด์ — IDSA/ASCO)*",
         "FN → antipseudomonal β-lactam ภายใน 1 ชม.", "Febrile neutropenia", ["IDSA/ASCO febrile neutropenia guideline (2018)"], ["2.3.3(2)", "2.3.3-3(5)"]),
     mcq(N(27), "Two days after starting chemotherapy for bulky Burkitt lymphoma, a patient has K 6.4 mmol/L, phosphate 8.2 mg/dL, uric acid 14 mg/dL, Ca 6.8 mg/dL and rising creatinine. G6PD status is normal. What is the best management?",
         ["Stop IV fluids", "Aggressive IV hydration, rasburicase, treatment of hyperkalaemia and early nephrology input", "Calcium gluconate infusion to normalise calcium as the main therapy", "Allopurinol alone and repeat labs in a week", "Thiazide diuretic"], 1,
         "**Tumour lysis syndrome** (K↑ PO4↑ urate↑ Ca↓ + ไตวาย) หลังเริ่มยาในมะเร็งโตเร็วก้อนใหญ่ → **สารน้ำมาก · rasburicase** (ย่อย uric acid ที่มีอยู่แล้ว — allopurinol แค่กันการสร้างใหม่) · **แก้ K สูงแบบเร่งด่วน** · ปรึกษาฟอกไตถ้าปัสสาวะไม่ออกหรือเกลือแร่ไม่ลง\n\n**ไม่ให้แคลเซียมแก้ Ca ต่ำที่ไม่มีอาการ** เพราะตกตะกอน calcium-phosphate ในไต · rasburicase **ห้ามใน G6PD deficiency** (เม็ดเลือดแดงแตก)",
         "TLS ที่เกิดแล้ว → สารน้ำ + rasburicase + แก้ K", "Tumour lysis syndrome", ["Cairo–Bishop TLS criteria · BSH TLS guideline"], ["2.3.4(2)", "B9.2.5(2)"]),
     mcq(N(28), "A 66-year-old man with metastatic prostate cancer has 2 weeks of worsening thoracic back pain, worse lying down, and today new leg weakness and numbness below the umbilicus. What should be done first?",
         ["NSAIDs and review in clinic next week", "High-dose dexamethasone immediately, then urgent whole-spine MRI", "Plain X-ray of the spine and physiotherapy", "Start chemotherapy", "Lumbar puncture"], 1,
         "ปวดหลังแย่ลงเมื่อนอนราบในผู้ป่วยมะเร็ง + **ขาอ่อนแรงและระดับการรับความรู้สึก** = **malignant spinal cord compression** → **dexamethasone ทันที** แล้ว **MRI ทั้งแนวกระดูกสันหลังด่วน (ภายใน 24 ชม.)** → **ฉายแสง หรือผ่าตัดลดแรงกด + ฉายแสง**\n\nผลการเดินหลังรักษาขึ้นกับการเดินได้ก่อนรักษา — ทุกชั่วโมงสำคัญ",
         "Cord compression: dexamethasone → MRI ทั้งแนวด่วน", "Spinal cord compression", ["NICE NG234 metastatic spinal cord compression (2023)"], ["2.2.38", "B3.2.3(3)", "B5.2.4-3(2)"]),
     mcq(N(29), "A 70-year-old woman with lung squamous cell carcinoma is confused and dehydrated. Calcium is 14.2 mg/dL, PTH is suppressed and PTHrP is raised. Which initial treatment is most appropriate?",
         ["Oral calcium restriction only", "IV normal saline followed by IV zoledronic acid", "Thiazide diuretic", "Furosemide alone without fluids", "Vitamin D supplementation"], 1,
         "**Humoral hypercalcemia of malignancy (PTHrP)** จาก squamous cell carcinoma · Ca > 14 มีอาการ → **NSS ทางหลอดเลือด** แก้การขาดน้ำ (แคลเซียมสูงทำให้ไตเข้มข้นปัสสาวะไม่ได้) **แล้วให้ zoledronic acid** ยับยั้ง osteoclast (ออกฤทธิ์ 2–4 วัน) ± calcitonin ระหว่างรอ\n\nThiazide **เพิ่ม** แคลเซียม · furosemide ใช้เฉพาะเมื่อน้ำเกินหลังให้สารน้ำแล้ว",
         "Hypercalcemia of malignancy: NSS → zoledronic acid", "Hypercalcaemia of malignancy", ["Endocrine Society hypercalcemia of malignancy guideline (2022)"], ["2.3.4(2)", "B6.2.4-3(2)"]),
    ], EM, "เพิ่มเติม (ไม่ได้มาจากสไลด์) — IDSA/ASCO · NICE NG234 · Endocrine Society 2022")

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
 "nl": ["B10.2.4-3(4)", "2.1.55", "B1.7.3"], "years": [], "_kind": "meq", "_set": SET},
 {"id": "HON-ONC-MEQ-02", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Oncologic emergencies after first chemotherapy — febrile neutropenia and tumour lysis",
 "vignette": """ผู้ป่วยชายไทยอายุ 45 ปี เพิ่งได้รับการวินิจฉัย diffuse large B-cell lymphoma ก้อนใหญ่ในช่องท้อง 12 ซม. LDH 1,850 U/L ได้ยาเคมีบำบัด R-CHOP รอบแรกเมื่อ 3 วันก่อน
PI: ปัสสาวะออกน้อยลง 1 วัน คลื่นไส้ อ่อนเพลีย ใจสั่น
PE: BT 37.0 C · BP 132/84 · HR 104 · ไม่มีไข้ · บวมขาเล็กน้อย
Lab: BUN 48 · Cr 3.1 (เดิม 0.9) · K 6.6 · phosphate 9.1 mg/dL · Ca 6.9 mg/dL · uric acid 15.2 mg/dL · EKG: T wave สูงแหลม
10 วันต่อมาหลังไตฟื้นตัว ผู้ป่วยกลับมาด้วยไข้ 38.7 C หนาวสั่น BP 96/60 · ANC 180/µL""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยในครั้งแรก พร้อมปัจจัยเสี่ยงของผู้ป่วย (3 คะแนน)",
   "a": """**Tumour lysis syndrome (laboratory + clinical)** — K, phosphate, uric acid สูง · Ca ต่ำ · **ไตวายเฉียบพลัน** · EKG เปลี่ยน
ปัจจัยเสี่ยง: **lymphoma โตเร็ว · ก้อนใหญ่ (bulky > 10 ซม.) · LDH สูงมาก** · เริ่มยาที่ได้ผลแรง · (ไม่ได้ป้องกันด้วยสารน้ำ/allopurinol หรือ rasburicase เพียงพอ)"""},
  {"q": "2. จงบอกการรักษาเร่งด่วน (4 คะแนน)",
   "a": """- **K สูงที่มี EKG เปลี่ยน**: **calcium gluconate IV** ปกป้องหัวใจ (ข้อยกเว้นที่ให้แคลเซียม) · **insulin + glucose** · salbutamol พ่น · ยาขับ K/ resin
- **สารน้ำทางหลอดเลือดมาก** ให้ปัสสาวะ 80–100 มล./ชม. (ระวังน้ำเกินเมื่อไตวาย)
- **Rasburicase** (ตรวจ G6PD ก่อนถ้าทำได้) — allopurinol ไม่ลด uric acid ที่มีอยู่แล้ว
- **ปรึกษาฟอกไต** เมื่อ K/phosphate ไม่ลง น้ำเกิน หรือปัสสาวะไม่ออก
- ไม่แก้ Ca ต่ำที่ไม่มีอาการ · ติดตามเกลือแร่ทุก 6–8 ชม."""},
  {"q": "3. ครั้งที่สอง ผู้ป่วยเป็นอะไร และต้องทำอะไรภายในชั่วโมงแรก (4 คะแนน)",
   "a": """**Febrile neutropenia + ความดันต่ำ (สงสัย septic shock)** ช่วง nadir (วันที่ 7–14)
- **เพาะเชื้อเลือด 2 ขวด** (รวมจากสายสวน ถ้ามี) ปัสสาวะ CXR
- **ยาปฏิชีวนะต้าน Pseudomonas ภายใน 1 ชม.** — รายนี้ความดันต่ำ → **meropenem + vancomycin** (± aminoglycoside)
- **สารน้ำ crystalloid 30 มล./กก.** → norepinephrine ถ้า MAP < 65 · lactate · ย้าย ICU
- พิจารณา G-CSF ในรายที่เสี่ยงสูงมาก · รอบต่อไปให้ **G-CSF ป้องกัน**"""},
  {"q": "4. รอบต่อไปจะป้องกันภาวะทั้งสองอย่างไร (2 คะแนน)",
   "a": """- TLS: ประเมินความเสี่ยงก่อนทุกรอบแรก — **สารน้ำล่วงหน้า + allopurinol** (เสี่ยงปานกลาง) หรือ **rasburicase** (เสี่ยงสูง) · ให้ prednisolone นำก่อนในก้อนใหญ่มาก
- FN: **G-CSF (pegfilgrastim) ป้องกันหลังยา** เมื่อเคยมี FN · สอนผู้ป่วยให้วัดไข้และมาโรงพยาบาลทันทีเมื่อไข้ ≥ 38"""}],
 "ref": ["IDSA/ASCO febrile neutropenia (2018)", "Cairo–Bishop TLS criteria · BSH TLS guideline"],
 "nl": ["2.3.3(2)", "2.3.4(2)", "2.3.3-3(5)"], "years": [], "_kind": "meq", "_set": SET}]

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
 "nl": ["B1.7.3", "B1.4.14", "B1.6.4(1)"], "years": [], "_kind": "meq", "_set": SET},
 {"id": "HON-ONC-OSCE-02", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "SAQ – Oncologic emergencies and tumour markers",
 "station": "SAQ (เขียนตอบ) 6 นาที",
 "instruction": """จงให้การวินิจฉัยและการจัดการเร่งด่วน 1–2 ข้อ สำหรับผู้ป่วยมะเร็ง 5 รายต่อไปนี้

| ราย | ข้อมูล |
|---|---|
| A | หญิง 50 ปี มะเร็งเต้านม 9 วันหลังยาเคมี ไข้ 38.5 °C ANC 300 |
| B | ชาย 60 ปี มะเร็งปอด หน้าบวมแดง เส้นเลือดดำที่คอและอกโป่ง หายใจปกติ ยังไม่มีชิ้นเนื้อ |
| C | ชาย 68 ปี มะเร็งต่อมลูกหมาก ปวดหลังกลางคืน 3 สัปดาห์ วันนี้ขาอ่อนแรง |
| D | หญิง 72 ปี มะเร็งปอด squamous ซึม Ca 14.5 mg/dL PTH ต่ำ |
| E | ชาย 25 ปี ก้อนอัณฑะแข็งไม่เจ็บ — ควรตรวจเลือดอะไร และผ่าตัดแบบใด |""",
 "answer": """| ราย | วินิจฉัย | จัดการ | คะแนน |
|---|---|---|---|
| **A** | **Febrile neutropenia** | เพาะเชื้อ + **cefepime/pip-tazo ภายใน 1 ชม.** | 2 |
| **B** | **SVC syndrome** | **หาชิ้นเนื้อก่อน** steroid/ฉายแสง (ไม่คุกคามชีวิต) · ยกหัวสูง · stent ถ้าอาการมาก | 2 |
| **C** | **Malignant spinal cord compression** | **dexamethasone ทันที → MRI ทั้งแนวภายใน 24 ชม.** → ฉายแสง/ผ่าตัด | 2 |
| **D** | **Hypercalcemia of malignancy (PTHrP)** | **NSS → zoledronic acid** ± calcitonin | 2 |
| **E** | **Testicular germ cell tumour** | **AFP β-hCG LDH** · **radical inguinal orchiectomy** (ห้ามผ่านถุงอัณฑะ) | 2 |""",
 "ref": ["IDSA/ASCO · NICE NG234 · Endocrine Society 2022 · EAU testicular cancer"],
 "nl": ["2.3.3(2)", "2.2.13", "2.2.38", "3.3.24"], "years": [], "_kind": "meq", "_set": SET}]

LECTURE = {
 "lec": LEC, "date": "จ. 2 พ.ย.",
 "title": "General oncology",
 "subtitle": "ระบาดวิทยา · เป้าหมายการรักษาและ performance status · วงจรเซลล์และ hallmarks · ยาเคมีตามระยะของวงจรเซลล์ · targeted therapy และ immunotherapy · มะเร็งเต้านม · tumour markers คัดกรอง มะเร็งที่พบบ่อย และภาวะฉุกเฉินทางมะเร็ง",
 "objectives": [
   "บอกมะเร็งที่พบบ่อยของโลกและประเทศไทย และปัจจัยเสี่ยงที่ป้องกันได้",
   "แยกเป้าหมายการรักษาระยะแรกกับระยะลุกลาม และความหมายของ neoadjuvant/adjuvant",
   "ประเมิน performance status และปัจจัยของมะเร็งที่มีผลต่อการเลือกการรักษา",
   "อธิบายการควบคุมวงจรเซลล์ hallmarks of cancer และการก่อมะเร็งหลายขั้นตอน",
   "จัดกลุ่มยาเคมีตามระยะของวงจรเซลล์ และบอกพิษเฉพาะของยาหลัก",
   "อธิบายกลไก biomarker และพิษของยามุ่งเป้าและ immune checkpoint inhibitor",
   "วางแผนคัดกรอง วินิจฉัยชนิดย่อย และรักษามะเร็งเต้านมตามระยะ",
   "ใช้ staging และ tumour markers อย่างถูกต้อง และเลือกวิธีคัดกรองมะเร็งที่มีหลักฐาน",
   "จดจำลักษณะเด่นและหลักการรักษาของมะเร็งที่พบบ่อย (ปอด ลำไส้ใหญ่ ตับ กระเพาะ ต่อมลูกหมาก นรีเวช ไต ไทรอยด์ ผิวหนัง สมอง)",
   "วินิจฉัยและจัดการภาวะฉุกเฉินทางมะเร็ง: febrile neutropenia, TLS, hypercalcemia, SVC syndrome, spinal cord compression"],
 "nlGap": "เกณฑ์ฯ มีรหัสวิทยาศาสตร์พื้นฐาน `นล. B1.6.4` Neoplasm · `B1.7.3` General principles of antineoplastic agents · `B1.4.12` Tumor immunology · `B10.2.4-3(4)` Malignant neoplasm of reproductive system (breast) · `2.1.55` Breast mass แต่ **ไม่มีรหัสของ immune checkpoint inhibitor, irAE หรือ performance status** โดยตรง และสไลด์ใช้ข้อมูล GLOBOCAN 2012 และการรักษามะเร็งเต้านมก่อนยุค CDK4/6 inhibitor จึงอ้างอิงแนวทางด้านล่าง · **หัวข้อ 9–13 เพิ่มเองทั้งหมด** เพราะไฟล์สไลด์มีส่วน Common cancer เฉพาะมะเร็งเต้านม — ครอบคลุมรหัส `3.3.24` Tumor markers · `2.3.3(2)` Febrile neutropenia · `2.2.13` SVC obstruction · `2.2.38` Spinal cord compression",
 "guidelines": [
   "**GLOBOCAN 2022 (IARC, CA Cancer J Clin 2024)** — อุบัติการณ์และการตายจากมะเร็งทั่วโลก",
   "**Hanahan D. Hallmarks of cancer: new dimensions (Cancer Discovery 2022)** — ต่อจากฉบับ 2000 และ 2011 ที่อยู่ในสไลด์",
   "**ASCO Guideline: Management of immune-related adverse events (2021)** และ **ESMO irAE guideline (2022)**",
   "**USPSTF Breast cancer screening (2024)** — mammogram ทุก 2 ปี อายุ 40–74",
   "**NCCN/ESMO Breast cancer guidelines** — CDK4/6 inhibitor ใน HR+ แพร่กระจาย · KEYNOTE-522 ใน TNBC · neoadjuvant ใน HER2+",
   "**NCCN/ESMO Colon cancer** — adjuvant FOLFOX/CAPOX ใน stage III · anti-EGFR เฉพาะ RAS wild-type · KEYNOTE-177 (MSI-H)",
   "**USPSTF Lung (2021) และ Colorectal (2021) cancer screening** · โครงการคัดกรองมะเร็งลำไส้ใหญ่และปากมดลูก (HPV DNA) ของ สปสช.",
   "**IDSA/ASCO Outpatient management of fever and neutropenia (2018)** · **Endocrine Society Hypercalcemia of malignancy (2022)** · **NICE NG234 Spinal metastases and MSCC (2023)**"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

HEMONC_META = {"set": "hemonc", "title": "Heme/Onc · โลหิตวิทยาและมะเร็งวิทยา",
 "intro": "ชุดใหม่ของโลหิตวิทยาและมะเร็งวิทยา เริ่มจากคาบ **General oncology ของ พญ.ปิยวรรณ (2 พ.ย.)** — ระบาดวิทยา เป้าหมายการรักษา performance status วงจรเซลล์และ hallmarks of cancer ยาเคมีตามระยะของวงจรเซลล์ ยามุ่งเป้า immunotherapy มะเร็งเต้านม ต่อด้วย tumour markers การคัดกรอง มะเร็งที่พบบ่อย และภาวะฉุกเฉินทางมะเร็ง พร้อมอัปเดตแนวทางที่เปลี่ยนไปหลังสไลด์",
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
                             "hon-onc-08": ["MOCK-025", "MOCK-038"],
                             "hon-onc-10": ["MOCK-033"], "hon-onc-11": ["MOCK-022", "MOCK-023", "MOCK-032", "MOCK-029"],
                             "hon-onc-12": ["MOCK-034", "MOCK-036", "MOCK-037", "MOCK-021", "MOCK-028"], "hon-onc-13": ["MOCK-031"]})

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
