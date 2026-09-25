#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เติมส่วนที่ยังขาดจากสไลด์ อ.พรรณนิภา (SLE and systemic autoimmune diseases 2567)
ลงในคาบ AIR 33 ของ data/air.json — รันซ้ำได้ ไม่สร้างของซ้ำ"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
SRC = ("สไลด์ อ.พรรณนิภา บุปผาเรณู (หน่วยโรคข้อและรูมาติสซั่ม รพ.ราชวิถี) "
       "— SLE and systemic autoimmune diseases 2567")

def sec(sid, title, summary, minutes, nl, md, pearls, items):
    return {"id": sid, "title": title, "summary": summary, "minutes": minutes,
            "nl": nl, "md": md, "pearls": pearls, "source": SRC, "items": items}

def own(iid, stem, choices, answer, explain, pearl, topic, nl):
    return {"id": iid, "kind": "own", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": [], "nl": nl}

NL_SLE = ["2.3.13-3(15)", "B5.2.2-3(5)"]
NL_PLEURA = ["2.3.13-3(15)", "2.3.10(7)", "B6.3(1)", "B5.2.2-3(5)"]
NL_SSC = ["2.3.12-3(13)", "B4.2.2-3(9)", "2.3.13"]
NL_IIM = ["2.3.13-3(10)", "B5.2.2-3(2)"]

# ─────────────────────────── หัวข้อใหม่ 1: น้ำในเยื่อหุ้มปอดของลูปัส ───────────────────────────
PLEURA = sec(
 "air-33-02d",
 "เจาะน้ำในเยื่อหุ้มปอดของลูปัส — อ่านผลให้เป็น",
 "ลักษณะน้ำเจาะที่บอกว่าเป็น lupus pleuritis และตัวเลขที่บอกว่าไม่ใช่", 8, NL_PLEURA,
"""**เยื่อหุ้มปอดอักเสบคืออาการทางปอดที่พบบ่อยที่สุดของ SLE** สไลด์สรุปลักษณะไว้สี่ข้อ — **มักเป็นสองข้างมากกว่าข้างเดียว · ปริมาณน้ำน้อยถึงปานกลาง · เป็นแบบ “dry” pleuritis ที่เจ็บแต่ไม่มีน้ำก็ได้ · และมักมีเยื่อหุ้มหัวใจอักเสบร่วมด้วย**

> **เจาะเพื่อ “ตัดโรคอื่น” ไม่ใช่เพื่อ “ยืนยันลูปัส”** — ผู้ป่วย SLE เกือบทุกรายได้ยากดภูมิคุ้มกันอยู่ น้ำในเยื่อหุ้มปอดที่เพิ่งเกิดจึงต้องตัด **การติดเชื้อ (รวมวัณโรค) · หัวใจล้มเหลว · ลิ่มเลือดอุดกั้นปอด (นึกถึง APS ร่วมเสมอ) · และมะเร็ง** ออกก่อน

### ลักษณะน้ำเจาะของ lupus pleuritis (จากสไลด์)

| สิ่งที่ตรวจ | ค่าที่พบ |
|---|---|
| **ปริมาณ** | น้อยถึงปานกลาง **400–1,000 มล.** |
| **ลักษณะ** | เหลืองใส (serous) หรือ **ปนเลือดเล็กน้อย (serosanguineous)** |
| **เม็ดเลือดขาว** | สูงขึ้น แต่ **มักน้อยกว่า 15,000/ลบ.มม.** |
| **ชนิดเซลล์เด่น** | **neutrophil ในระยะเฉียบพลัน · lymphocyte ในระยะเรื้อรัง** |
| **น้ำตาล** | **ปกติหรือต่ำลงเล็กน้อย** |
| **โปรตีน** | **สูง > 3 g/dL · อัตราส่วนน้ำเจาะต่อซีรัม > 0.5** |
| **LDH** | **สูง · อัตราส่วน > 0.6 หรือ > 200 IU/L** |
| **pH** | **ปกติ** |
| **C3 และ C4 ในน้ำเจาะ** | **ต่ำ** (immune complex ถูกใช้ไป) |
| **ANA ในน้ำเจาะ** | **บวก · อัตราส่วนน้ำเจาะต่อซีรัม ≥ 1** |
| **LE cell** | **มักพบ** — คือ neutrophil ที่กลืน immune complex เข้าไป |

**โปรตีนและ LDH ที่เข้าเกณฑ์ข้างบนคือ Light's criteria** — เข้าข้อใดข้อหนึ่งก็เป็น **exudate** ดังนั้น **น้ำในเยื่อหุ้มปอดของลูปัสเป็น exudate เสมอ** ถ้าผลออกมาเป็น transudate ให้กลับไปคิดถึง **หัวใจล้มเหลว · ตับแข็ง · หรือ nephrotic syndrome จาก lupus nephritis** แทน

### ตัวเลขที่ใช้แยกจากโรคอื่น — จุดที่ออกสอบจริง

| วินิจฉัย | น้ำตาลในน้ำเจาะ | pH | เบาะแสอื่น |
|---|---|---|---|
| **Lupus pleuritis** | **ปกติหรือต่ำเล็กน้อย** | **ปกติ (~7.4)** | **ANA บวก อัตราส่วน ≥ 1 · complement ต่ำ · LE cell** |
| **Rheumatoid pleuritis** | **ต่ำมาก (มักน้อยกว่า 30–60 mg/dL)** | **ต่ำ** | RF ในน้ำเจาะสูง · พบในชายที่เป็น RA มานาน |
| **Empyema / complicated parapneumonic** | **ต่ำมาก** | **< 7.20** | ขุ่นเป็นหนอง ย้อมกรัมหรือเพาะเชื้อขึ้น — **ต้องใส่สายระบาย** |
| **วัณโรคเยื่อหุ้มปอด** | ปกติถึงต่ำ | ปกติถึงต่ำ | **lymphocyte เด่น · ADA สูง** · มักข้างเดียว |
| **มะเร็ง** | ปกติหรือต่ำ | ปกติหรือต่ำ | lymphocyte เด่น · มักปนเลือด · เซลล์วิทยาบวก |

> **จำสั้น ๆ — ลูปัสทำให้ pH และน้ำตาล “เกือบปกติ” ถ้าเจอน้ำตาลต่ำมากคู่กับ pH ต่ำ ให้คิดถึง RA หรือหนองในช่องเยื่อหุ้มปอดก่อน ไม่ใช่ลูปัส**

### เมื่อเจาะแล้วเข้าได้กับลูปัสจริง
- **รักษาที่ตัวโรค** — NSAIDs สำหรับรายที่อาการน้อย · **สเตียรอยด์ขนาดต่ำถึงปานกลางเมื่อไม่ตอบสนอง NSAIDs** ตามตารางความรุนแรงในหัวข้อการรักษา · hydroxychloroquine ให้ทุกราย
- **ไม่ต้องใส่สายระบายในน้ำเยื่อหุ้มปอดจากลูปัสที่ไม่ติดเชื้อ** — น้ำมักน้อยถึงปานกลางและยุบตามการรักษาโรค
- **อาการหอบในผู้ป่วย SLE ที่ภาพถ่ายไม่มีน้ำ** ให้คิดถึง **shrinking lung syndrome** (ปอดเล็กลงแบบ restrictive กะบังลมทำงานลดลง) และ **diffuse alveolar hemorrhage ซึ่งราวสองในสามไม่ไอเป็นเลือด** — สองภาวะนี้เจาะน้ำไม่ได้คำตอบ
""",
 ["Lupus pleuritis เป็น exudate เสมอ มักสองข้าง ปริมาณน้อยถึงปานกลาง และมักมี pericarditis ร่วม",
  "น้ำเจาะของลูปัส: pH ปกติ น้ำตาลปกติหรือต่ำเล็กน้อย ANA บวกอัตราส่วน ≥ 1 complement ต่ำ และพบ LE cell",
  "น้ำตาลต่ำมากคู่กับ pH < 7.2 = คิดถึง RA pleuritis หรือ empyema ไม่ใช่ลูปัส",
  "เจาะน้ำในผู้ป่วย SLE เพื่อตัดการติดเชื้อ วัณโรค และมะเร็งออก ไม่ใช่เพื่อยืนยันลูปัส"],
 [
  own("AIR-33-02D-Q1",
   "A 27-year-old woman with SLE on prednisolone 10 mg/day presents with pleuritic chest pain and dyspnoea for 5 days. Chest radiograph shows small bilateral pleural effusions. Thoracentesis yields clear yellow fluid: protein 4.2 g/dL (serum 6.8), LDH 260 IU/L (serum 340), glucose 82 mg/dL, pH 7.41, WBC 2,800/mm3 with lymphocyte predominance, ADA 15 U/L, Gram stain and AFB smear negative, cytology negative, pleural fluid ANA positive with a fluid-to-serum ratio of 1.4 and low pleural C4. Which interpretation best fits this fluid?",
   ["Lupus pleuritis — an exudate with near-normal pH and glucose, positive fluid ANA and low complement",
    "Tuberculous pleuritis — lymphocytic exudates in an immunosuppressed host are diagnostic of tuberculosis",
    "Complicated parapneumonic effusion requiring immediate chest tube drainage",
    "Transudate from nephrotic syndrome due to membranous lupus nephritis",
    "Malignant effusion — negative cytology on a single specimen excludes nothing and is the most likely cause"],
   0,
   "**คิดเป็นสองขั้น — exudate หรือ transudate ก่อน แล้วค่อยหาว่าเป็น exudate จากอะไร**\n\n**ขั้นที่ 1** อัตราส่วนโปรตีน 4.2/6.8 = **0.62 (> 0.5)** และอัตราส่วน LDH 260/340 = **0.76 (> 0.6)** → เข้า **Light's criteria เป็น exudate** จึง **ตัด transudate จาก nephrotic syndrome ออก**\n\n**ขั้นที่ 2** ลักษณะที่เหลือเข้ากับ **lupus pleuritis** ทุกข้อ — **pH 7.41 ปกติ · น้ำตาล 82 ปกติ · เม็ดเลือดขาวน้อยกว่า 15,000 · ANA ในน้ำเจาะบวกโดยอัตราส่วนต่อซีรัม ≥ 1 · complement ในน้ำเจาะต่ำ**\n\n**ทำไมข้ออื่นผิด**\n- **วัณโรค** — lymphocyte เด่นจริง แต่ **ADA 15 ถือว่าต่ำ** (จุดตัดที่ใช้กันคือราว 40 U/L) และวัณโรคเยื่อหุ้มปอดมัก **ข้างเดียว** ไม่ใช่สองข้าง · ลักษณะ lymphocyte เด่นอย่างเดียวไม่เคยวินิจฉัยวัณโรคได้\n- **Complicated parapneumonic / empyema** — ต้องมี **pH < 7.20 และน้ำตาลต่ำมาก** รายนี้ทั้งสองค่าปกติ จึงไม่มีข้อบ่งชี้ใส่สายระบาย\n- **มะเร็ง** — เป็นไปได้เสมอในทางทฤษฎี แต่ไม่มีข้อมูลใดชี้ไปทางนั้น ส่วน ANA ที่บวกในน้ำเจาะร่วมกับ complement ต่ำเป็นภาพของลูปัสโดยตรง",
   "Exudate + pH และน้ำตาลเกือบปกติ + ANA ในน้ำเจาะบวก (ratio ≥ 1) + complement ต่ำ = lupus pleuritis",
   "เจาะน้ำในเยื่อหุ้มปอดของลูปัส", NL_PLEURA),
  own("AIR-33-02D-Q2",
   "A 34-year-old woman with a 6-year history of SLE develops a unilateral pleural effusion. Pleural fluid shows protein 5.1 g/dL (serum 7.0), LDH 890 IU/L (serum 300), glucose 22 mg/dL, pH 7.08, WBC 9,400/mm3 with 85% neutrophils. Which is the most appropriate next step?",
   ["Send Gram stain and culture and arrange drainage, because very low glucose with pH below 7.2 points away from lupus pleuritis",
    "Increase prednisolone to 1 mg/kg/day and observe, since this is a typical lupus flare of serositis",
    "Start pulse methylprednisolone because pleural involvement at this severity is an organ-threatening manifestation",
    "Measure pleural fluid ANA and complement; a positive ANA would confirm lupus pleuritis regardless of the glucose",
    "Repeat the chest radiograph in two weeks, as small effusions in SLE resolve without intervention"],
   0,
   "**น้ำตาล 22 mg/dL ร่วมกับ pH 7.08 ไม่ใช่ภาพของลูปัส** — ลูปัสทำให้ **pH ปกติและน้ำตาลปกติหรือต่ำเพียงเล็กน้อย** ค่าที่ต่ำขนาดนี้บอกว่า **มีการใช้กลูโคสและสร้างกรดในช่องเยื่อหุ้มปอดมาก** ซึ่งพบใน **empyema/complicated parapneumonic effusion และ rheumatoid pleuritis** เป็นหลัก\n\nในผู้ป่วยที่ได้ยากดภูมิคุ้มกัน ต้องถือว่า **ติดเชื้อไว้ก่อน** จึงต้อง **ย้อมกรัม เพาะเชื้อ และระบายหนอง** — **pH < 7.20 คือจุดตัดคลาสสิกของ complicated parapneumonic effusion ที่ต้องใส่สายระบาย** ไม่ใช่รอดูอาการ\n\n**ทำไมข้ออื่นผิด**\n- **เพิ่มสเตียรอยด์หรือให้ pulse methylprednisolone** — คือความผิดพลาดที่อันตรายที่สุดในผู้ป่วย SLE ที่กำลังติดเชื้อ กฎคือ **ตัดการติดเชื้อและพิษยาออกก่อนเสมอ ก่อนจะบอกว่าโรคกำเริบ** · serositis ก็ไม่ใช่ข้อบ่งชี้ของ pulse steroid\n- **ANA ในน้ำเจาะบวก** พบได้ในน้ำเจาะจากสาเหตุอื่นของผู้ป่วยที่มี ANA ในเลือดสูงอยู่แล้ว **จึงยืนยันไม่ได้** และไม่ลบล้างค่าที่ผิดปกติชัดเจนอย่างน้ำตาลกับ pH\n- **รอสองสัปดาห์** — ปล่อยหนองไว้ในช่องเยื่อหุ้มปอดของผู้ป่วยที่ภูมิคุ้มกันถูกกด",
   "pH < 7.2 และน้ำตาลต่ำมากในผู้ป่วย SLE = ติดเชื้อจนกว่าจะพิสูจน์ได้ว่าไม่ใช่ ต้องเพาะเชื้อและระบาย ไม่ใช่เพิ่มยากดภูมิคุ้มกัน",
   "เจาะน้ำในเยื่อหุ้มปอดของลูปัส", NL_PLEURA),
 ])

# ─────────────────────── หัวข้อใหม่ 2: เกณฑ์จำแนก SSc ปี 2013 ทีละข้อ ───────────────────────
SSC = sec(
 "air-33-06b",
 "เกณฑ์จำแนก systemic sclerosis ปี 2013 ทีละข้อ",
 "ตารางให้คะแนน ACR/EULAR 2013 · ข้อที่พอข้อเดียว · และกติกาที่ทำให้บวกเลขผิด", 7, NL_SSC,
"""หัวข้อที่แล้วบอกว่า **เกณฑ์ ACR/EULAR 2013 ใช้จุดตัดที่ ≥ 9 คะแนน** หัวข้อนี้คือตัวตารางที่ต้องบวกเลขเป็น เพราะข้อสอบชอบให้เคสมาแล้วถามว่า **เข้าเกณฑ์หรือยัง**

### ตารางให้คะแนน

| ข้อ | คะแนน |
|---|---|
| **ผิวแข็งที่นิ้วมือทั้งสองข้าง ลามเหนือข้อ MCP** | **9 — ข้อนี้ข้อเดียวพอ (sufficient criterion)** |
| **ผิวแข็งที่นิ้ว (นับข้อที่คะแนนสูงกว่าข้อเดียว)** — มือบวมตึง (puffy fingers) | **2** |
| ↳ sclerodactyly (ตั้งแต่ใต้ MCP ลงไป แต่ไม่เลย PIP) | **4** |
| **รอยโรคที่ปลายนิ้ว (นับข้อที่คะแนนสูงกว่าข้อเดียว)** — แผลที่ปลายนิ้ว (digital tip ulcer) | **2** |
| ↳ **แผลเป็นบุ๋มที่ปลายนิ้ว (fingertip pitting scar)** | **3** |
| **Telangiectasia** | **2** |
| **Nailfold capillary ผิดปกติ** | **2** |
| **PAH และ/หรือ ILD** (อย่างละ 2 · **รวมสูงสุด 2**) | **2** |
| **Raynaud's phenomenon** | **3** |
| **แอนติบอดีจำเพาะของ SSc** — anti-centromere, anti-topoisomerase I (Scl-70), anti-RNA polymerase III (**รวมสูงสุด 3**) | **3** |

**≥ 9 คะแนน = จัดเป็น systemic sclerosis**

### กติกาสามข้อที่ทำให้บวกเลขผิดบ่อยที่สุด
1. **ผิวแข็งเหนือ MCP ทั้งสองมือคือ sufficient criterion** — เจอข้อนี้ **จัดเป็น SSc ได้ทันทีโดยไม่ต้องบวกข้ออื่น**
2. **กลุ่มที่มีวงเล็บว่า “นับข้อที่สูงกว่า” ห้ามบวกซ้ำ** — ผู้ป่วยที่มีทั้ง puffy fingers และ sclerodactyly ได้ **4 ไม่ใช่ 6** · มีทั้งแผลและแผลเป็นบุ๋มได้ **3 ไม่ใช่ 5** · มีทั้ง PAH และ ILD ได้ **2 ไม่ใช่ 4** · มีแอนติบอดีสามตัวก็ยังได้ **3**
3. **แอนติบอดีที่นับได้มีแค่สามตัว** — **anti-U1RNP, ANA เปล่า ๆ หรือ RF ไม่นับแม้แต่คะแนนเดียว**

### ลองบวกดูหนึ่งเคส
หญิงอายุ 45 ปี **Raynaud (3) + มือบวมตึงโดยยังไม่ sclerodactyly (2) + nailfold capillary ผิดปกติ (2) + anti-centromere บวก (3)** = **10 คะแนน → เข้าเกณฑ์ SSc** ทั้งที่ยังไม่มีผิวแข็งชัดเจนเลย
ถ้าเคสเดียวกันนี้ **แอนติบอดีที่บวกเป็น anti-U1RNP แทน** จะเหลือ **7 คะแนน → ไม่เข้าเกณฑ์** และต้องกลับไปคิดถึง **MCTD หรือ UCTD**

### สองข้อที่เกณฑ์นี้ใช้ไม่ได้
- **ผู้ป่วยที่ผิวแข็งแต่ไม่แข็งที่นิ้วเลย**
- **ผู้ป่วยที่มีโรคกลุ่ม scleroderma-like ซึ่งอธิบายอาการได้ดีกว่า** — **NSF · eosinophilic fasciitis · scleredema diabeticorum · scleromyxedema · porphyria · lichen sclerosus · GVHD · diabetic cheiroarthropathy**

> และเหมือนกับ SLE — **นี่คือ classification criteria ไม่ใช่ diagnostic criteria** คนไข้ที่ยังไม่ถึง 9 คะแนนแต่มี Raynaud ทุติยภูมิร่วมกับ capillaroscopy ผิดปกติ **คือผู้ป่วยที่ต้องตามดู ไม่ใช่ผู้ป่วยที่ถูกตัดโรคทิ้ง**
""",
 ["ผิวแข็งที่นิ้วทั้งสองข้างลามเหนือ MCP = 9 คะแนน จัดเป็น SSc ได้ทันทีโดยไม่ต้องดูข้ออื่น",
  "กลุ่มที่บอกว่า “นับข้อที่สูงกว่า” ห้ามบวกซ้ำ — puffy + sclerodactyly ได้ 4 · PAH + ILD ได้ 2 · แอนติบอดีสามตัวได้ 3",
  "แอนติบอดีที่นับคะแนนมีแค่ anti-centromere, anti-Scl-70 และ anti-RNA pol III — anti-U1RNP ไม่นับ",
  "Raynaud 3 + puffy fingers 2 + nailfold ผิดปกติ 2 + anti-centromere 3 = 10 เข้าเกณฑ์แล้วแม้ผิวยังไม่แข็ง"],
 [
  own("AIR-33-06B-Q1",
   "A 45-year-old woman has Raynaud's phenomenon for 3 years, puffy fingers with sclerodactyly limited to the fingers (skin thickening does not extend proximal to the MCP joints), fingertip pitting scars, facial telangiectasia, abnormal nailfold capillaries and a positive anti-centromere antibody. Echocardiography shows pulmonary arterial hypertension and HRCT shows mild interstitial lung disease. What is her total 2013 ACR/EULAR score?",
   ["19", "21", "23", "16", "25"],
   0,
   "**บวกทีละกลุ่ม โดยจำกฎ \u201cนับข้อที่สูงกว่าข้อเดียว\u201d ให้ได้**\n\n| กลุ่ม | ผู้ป่วยรายนี้ | คะแนน |\n|---|---|---|\n| **ผิวแข็งที่นิ้ว** | มีทั้ง puffy fingers (2) และ sclerodactyly (4) → **นับเฉพาะข้อที่สูงกว่า** | **4** |\n| **รอยโรคปลายนิ้ว** | แผลเป็นบุ๋ม (3) | **3** |\n| Telangiectasia | มี | **2** |\n| Nailfold capillary ผิดปกติ | มี | **2** |\n| **PAH และ/หรือ ILD** | มีทั้งคู่ แต่ **รวมสูงสุด 2** | **2** |\n| Raynaud\u2019s phenomenon | มี | **3** |\n| แอนติบอดีจำเพาะ | anti-centromere (**รวมสูงสุด 3**) | **3** |\n| **รวม** | | **19** |\n\n**19 ≥ 9 จึงจัดเป็น systemic sclerosis** และรูปแบบของเธอ (ผิวแข็งไม่เลย MCP + anti-centromere + PAH) คือ **limited cutaneous SSc**\n\n**ตัวลวงแต่ละตัวมาจากการบวกผิดแบบใด**\n- **21** — บวก puffy fingers ซ้ำกับ sclerodactyly (2+4) หรือบวก PAH กับ ILD เป็น 4\n- **23** — บวกผิดทั้งสองแบบพร้อมกัน\n- **25** — บวกผิดทั้งสองแบบ แล้วยังบวกแผลปลายนิ้วซ้ำกับแผลเป็นบุ๋มอีก\n- **16** — ลืมคะแนนแอนติบอดี\n\n> **ข้อผิวแข็งเหนือ MCP ทั้งสองมือ (9 คะแนน) ใช้ไม่ได้กับรายนี้** เพราะโจทย์ระบุชัดว่าผิวแข็งไม่ลามเหนือ MCP — ถ้าลามเหนือ MCP เมื่อไร **ข้อนั้นข้อเดียวก็จัดเป็น SSc ได้โดยไม่ต้องบวกอะไรอีก**",
   "puffy fingers + sclerodactyly นับ 4 ไม่ใช่ 6 · PAH + ILD นับ 2 ไม่ใช่ 4 · แอนติบอดีรวมสูงสุด 3 → เคสนี้ได้ 19 คะแนน",
   "เกณฑ์จำแนก SSc ปี 2013", NL_SSC),
  own("AIR-33-06B-Q2",
   "A 52-year-old woman is referred with Raynaud's phenomenon, abnormal nailfold capillaries and a positive anti-U1RNP antibody at 1:320. She has puffy hands but no sclerodactyly, no telangiectasia, no digital ulcers or pitting scars, and normal PFT and echocardiography. Which statement is correct?",
   ["She scores 7 points and is not classified as systemic sclerosis, because anti-U1RNP is not one of the three SSc-related antibodies that score",
    "She scores 10 points and is classified as systemic sclerosis, because any positive antibody in a patient with Raynaud's scores 3",
    "She cannot be assessed with the 2013 criteria because she has no skin thickening at all",
    "The criteria classify her as limited cutaneous systemic sclerosis on the strength of Raynaud's phenomenon and abnormal capillaries alone",
    "A positive anti-U1RNP is a sufficient criterion and classifies her regardless of her total score"],
   0,
   "**คะแนนของเธอคือ Raynaud 3 + puffy fingers 2 + nailfold capillary ผิดปกติ 2 = 7 คะแนน** ซึ่ง **ไม่ถึง 9 จึงยังไม่จัดเป็น SSc**\n\n**หัวใจของข้อนี้** — เกณฑ์ปี 2013 ให้คะแนนแอนติบอดีเฉพาะ **สามตัวคือ anti-centromere, anti-topoisomerase I (Scl-70) และ anti-RNA polymerase III** เท่านั้น **anti-U1RNP ไม่อยู่ในรายการ** จึงไม่ได้คะแนนแม้แต่คะแนนเดียว\n\nภาพของเธอ — **Raynaud + มือบวม + anti-U1RNP** — คือภาพที่ต้องคิดถึง **MCTD (ถ้าไทเตอร์สูงถึงระดับที่เกณฑ์ Alarcón-Segovia กำหนด และมีอาการครบ 3 ใน 5) หรือ UCTD (ถ้ายังไม่ครบ)** และเป็นผู้ป่วยที่ **ต้องนัดตามดูเป็นระยะ**\n\n**ทำไมข้ออื่นผิด**\n- **ไม่มีข้อไหนของเกณฑ์นี้ที่เป็น sufficient criterion นอกจากผิวแข็งเหนือ MCP ทั้งสองมือ (9 คะแนน)**\n- **ไม่จำเป็นต้องมีผิวแข็งจึงจะใช้เกณฑ์ได้** — เกณฑ์ใช้ไม่ได้เฉพาะกับผู้ที่ **ผิวแข็งแต่เว้นนิ้ว** หรือมีโรค scleroderma-like ที่อธิบายได้ดีกว่า\n- **เกณฑ์นี้ไม่ได้แบ่ง limited กับ diffuse** — การแบ่งสองกลุ่มนั้นดูจากขอบเขตของผิวที่แข็ง",
   "anti-U1RNP ไม่ได้คะแนนในเกณฑ์ SSc 2013 — Raynaud + puffy fingers + nailfold ผิดปกติ ได้แค่ 7 ให้คิดถึง MCTD/UCTD แทน",
   "เกณฑ์จำแนก SSc ปี 2013", NL_SSC),
 ])

# ─────────────────── ส่วนที่ "ต่อท้าย" หัวข้อเดิม (มาร์กเกอร์กันเขียนซ้ำ) ───────────────────
APPEND = {
 # lupus anticoagulant — ชื่อการตรวจที่สไลด์วาดไว้เป็นแผนภาพ
 "air-33-04": ("dRVVT",
"""
**ชื่อการตรวจที่สไลด์วาดเป็นแผนภาพไว้** — การตรวจ lupus anticoagulant ที่ใช้จริงคือ **dRVVT (dilute Russell viper venom time)** ร่วมกับ aPTT ที่ไวต่อ lupus anticoagulant · พิษงู Russell ไปกระตุ้น factor X โดยตรงโดยต้องอาศัย phospholipid เป็นฐาน **แอนติบอดีที่จับ phospholipid จึงทำให้เวลาแข็งตัวยาวออก** และ **การเติม phospholipid เข้มข้นกลับเข้าไปจะแก้ความผิดปกติได้ (confirmatory step)** ซึ่งเป็นขั้นที่ยืนยันว่าเป็น lupus anticoagulant ไม่ใช่การขาดปัจจัยการแข็งตัว
> **ห้ามเจาะตรวจ lupus anticoagulant ขณะได้ยาต้านการแข็งตัวของเลือด** เพราะ warfarin, heparin และ DOAC รบกวนผลทั้งหมด — ให้ตรวจก่อนเริ่มยาหรือเว้นระยะตามคำแนะนำของห้องแล็บ
"""),
 # MSA รายตัว — สไลด์หน้า MSA in DM
 "air-33-07": ("ตารางแอนติบอดีจำเพาะของ myositis รายตัว",
"""
### ตารางแอนติบอดีจำเพาะของ myositis รายตัว (MSA)

| แอนติบอดี | ภาพทางคลินิกที่ผูกกับตัวมัน |
|---|---|
| **Anti-Mi-2** | เลือดออกเป็นจุดที่ perionychium · **cuticular overgrowth** · **CK สูง** · **ตอบสนองการรักษาดี** |
| **Anti-SAE1/2** | ผื่นสีแดงคล้ำอมม่วง · **PAH (รายงานมากในผู้ป่วยชาวจีน)** · **ILD น้อย** |
| **Anti-MDA-5** | **ตุ่มเจ็บที่ฝ่ามือ** · heliotrope · ผมร่วง · **pneumomediastinum และลมใต้ผิวหนัง** · **clinically amyopathic (ผื่นเด่น กล้ามเนื้อแทบไม่อ่อนแรง)** · **aldolase สูงเดี่ยว ๆ โดย CK เกือบปกติ** · **ferritin สูง** — สไลด์กำกับว่า **เสียชีวิตราวครึ่งหนึ่งภายใน 6 เดือน** จาก ILD ที่ลุกลามเร็ว |
| **Anti-TIF-1γ** | ผื่นคล้ายสะเก็ดเงิน · **red-on-white** · **ovoid palatal patch** · ปวดข้อน้อย · **CK สูงไม่มาก** · **สัมพันธ์กับมะเร็งมากที่สุด** |
| **Anti-NXP-2** | **บวมตามปลายแขนขา** · **อ่อนแรงส่วนปลาย** · ปวดและตะคริวกล้ามเนื้อ · **หลอดเลือดในลำไส้ผิดปกติ** · **calcinosis** |
| **กลุ่ม Mi-2/SAE/MDA5/TIF1γ/NXP2 ร่วมกัน** | ผื่นตามบริเวณที่ถูกแสง (heliotrope, V-sign, shawl sign, Gottron's sign) · **แผลที่ผิวหนัง** · **กลืนลำบาก** |
| **Antisynthetase (ASAs) เช่น anti-Jo-1** | **mechanic's hands · ไข้ · ข้ออักเสบ · ILD · Raynaud** = anti-synthetase syndrome |

> **สองตัวที่เปลี่ยนการดูแลทันทีที่ผลออก** — **anti-MDA-5 ให้รีบประเมิน ILD และรักษาเชิงรุก** เพราะ ILD ลุกลามเร็วมาก · **anti-TIF-1γ ให้เร่งคัดกรองมะเร็งให้ครบ รวมการตรวจ ENT หามะเร็งโพรงหลังจมูก**
"""),
 # Sjögren — ตัวเลขอาการนอกต่อมจาก NEJM 2018 ที่สไลด์ยกมา
 "air-33-07b": ("อาการนอกต่อมรายระบบพร้อมความถี่",
"""
### อาการนอกต่อมรายระบบพร้อมความถี่ (ตัวเลขที่สไลด์ยกมาจาก NEJM 2018)

| ระบบ | พบราว | ลักษณะ |
|---|---|---|
| **ข้อ** | **38%** | ปวดข้อร่วมกับข้อฝืดตอนเช้า หรือ synovitis |
| **ต่อม** | **22%** | **ต่อมพาโรติด ต่อมใต้ขากรรไกร หรือต่อมน้ำตาโตที่คลำได้** |
| ปอด | 11% | หลอดลมอักเสบเรื้อรัง · bronchiolitis · **ILD** |
| **ผิวหนัง** | **10%** | **purpura · vasculitis · subacute cutaneous lupus** |
| อาการทั่วกาย | 9% | ไข้ น้ำหนักลดโดยไม่ตั้งใจ เหงื่อออกกลางคืน |
| **ต่อมน้ำเหลือง** | **9%** | โตแบบไม่ร้าย **หรือมะเร็งต่อมน้ำเหลือง** |
| **เส้นประสาทส่วนปลาย** | **6%** | **pure sensory axonal polyneuropathy · ataxic ganglionopathy · mononeuritis multiplex จาก vasculitis** |
| ไต | 5% | **interstitial nephritis** · glomerulonephritis จาก cryoglobulin |
| ระบบประสาทส่วนกลาง | 2% | cerebral vasculitis · **transverse myelitis** · รอยโรค demyelinating |
| กล้ามเนื้อ | 2% | myositis ที่ปวดหรืออ่อนแรง |

**อ่านตารางนี้ให้เป็นสองบรรทัด** — **อาการนอกต่อมที่พบบ่อยคือข้อและต่อม** ส่วน **อาการที่พบน้อยแต่เปลี่ยนการรักษาทันทีคือ ไต ระบบประสาท และต่อมน้ำเหลืองที่โตผิดปกติ** เพราะสามกลุ่มหลังคือข้อบ่งชี้ของยากดภูมิคุ้มกันหรือการตัดชิ้นเนื้อหามะเร็งต่อมน้ำเหลือง ไม่ใช่แค่ให้น้ำตาเทียม
"""),
}

# ─────────────────────────── ข้อสอบที่เติมเข้าหัวข้อเดิม ───────────────────────────
EXTRA_ITEMS = {
 "air-33-07": [
  own("AIR-33-07-Q1",
   "A 48-year-old woman has a 6-week history of heliotrope rash, Gottron's papules, painful papules on the palms and skin ulcers over the elbows, but her muscle strength is normal and CK is 120 U/L. She now has progressive dyspnoea; HRCT shows rapidly progressive interstitial changes and a small pneumomediastinum, and serum ferritin is markedly raised. Which myositis-specific antibody is most likely, and what does it imply?",
   ["Anti-MDA-5 — clinically amyopathic dermatomyositis with rapidly progressive ILD and high early mortality",
    "Anti-Mi-2 — classic dermatomyositis that usually responds well to corticosteroids",
    "Anti-TIF-1γ — dermatomyositis strongly associated with underlying malignancy",
    "Anti-HMGCR — statin-associated immune-mediated necrotizing myopathy",
    "Anti-cN-1A — inclusion body myositis presenting with finger flexor weakness"],
   0,
   "**ภาพนี้เป็น anti-MDA-5 แทบทุกจุด** — **ผื่นของ dermatomyositis เต็มรูปแบบแต่กล้ามเนื้อแทบไม่อ่อนแรงและ CK เกือบปกติ (clinically amyopathic)** · **ตุ่มเจ็บที่ฝ่ามือและแผลที่ผิวหนัง** · **ILD ที่ลุกลามเร็วพร้อม pneumomediastinum** · **ferritin สูงมาก** ซึ่งเป็นตัวบอกความรุนแรง\n\n**ความหมายทางคลินิกคือรีบ** — สไลด์กำกับว่ากลุ่มนี้ **เสียชีวิตราวครึ่งหนึ่งภายใน 6 เดือน** จาก ILD จึงต้อง **ประเมินปอดทันทีและรักษาเชิงรุกด้วยสเตียรอยด์ร่วมกับยากดภูมิคุ้มกัน (calcineurin inhibitor หรือ cyclophosphamide)** ไม่ใช่รอดูอาการกล้ามเนื้อ\n\n**ทำไมข้ออื่นผิด**\n- **Anti-Mi-2** — ผื่นเด่นเหมือนกันแต่ **CK สูง** และ **ตอบสนองการรักษาดี** ไม่ใช่ภาพ amyopathic ที่มี ILD รุนแรง\n- **Anti-TIF-1γ** — สัมพันธ์กับมะเร็ง ผื่นเป็นแบบคล้ายสะเก็ดเงินและ **ovoid palatal patch** ยังต้องคัดกรองมะเร็งในรายนี้ด้วย แต่ไม่ใช่ตัวที่อธิบาย ILD ที่ลุกลามเร็ว\n- **Anti-HMGCR** — **CK สูงมากและอ่อนแรงชัดเจน** หลังได้สแตติน ไม่มีผื่นของ DM\n- **Anti-cN-1A** — IBM ซึ่งดำเนินโรคเป็นเดือนถึงปี อ่อนแรงงอนิ้วและ quadriceps ไม่สมมาตร และไม่มีผื่น",
   "ผื่น DM เต็มรูปแบบ + กล้ามเนื้อปกติ + ILD ลุกลามเร็ว + ferritin สูง = anti-MDA-5 ต้องรักษาเชิงรุกทันที",
   "กล้ามเนื้ออักเสบ และแอนติบอดีจำเพาะ", NL_IIM),
 ],
 "air-33-07c": [
  own("AIR-33-07C-Q3",
   "A 30-year-old woman presents with polyarthritis for 3 weeks together with Raynaud's phenomenon and sclerodactyly. ANA is positive at 1:160 with a speckled pattern, anti-RNP is positive and anti-Sm is negative. Hand radiographs are normal. What is the most likely diagnosis?",
   ["Undifferentiated connective tissue disease (UCTD)",
    "Mixed connective tissue disease (MCTD)",
    "Systemic sclerosis (SSc)",
    "Systemic lupus erythematosus (SLE)",
    "Overlap syndrome"],
   0,
   "**ข้อนี้คือคำถามท้ายสไลด์ของอาจารย์ และคำตอบคือ UCTD** — ผู้ป่วยมีทั้งอาการและแอนติบอดีของโรคเนื้อเยื่อเกี่ยวพัน **แต่ยังไม่เข้าเกณฑ์ของโรคใดเลย**\n\n**ไล่ทีละโรค**\n- **MCTD** — เกณฑ์ Alarcón-Segovia ต้องการ **anti-U1RNP ไทเตอร์สูงระดับ > 1:1,000** ส่วนรายนี้ **ANA เพียง 1:160** ซึ่งต่ำเกินไป และอาการที่มี (synovitis, Raynaud, sclerodactyly) **ยังไม่ครบตามที่เกณฑ์กำหนดร่วมกับไทเตอร์ที่ต้องการ** จึงยังเรียก MCTD ไม่ได้\n- **SSc** — ลองบวกเกณฑ์ ACR/EULAR 2013 ดู: **sclerodactyly 4 + Raynaud 3 = 7 คะแนน** และ **anti-RNP ไม่ใช่แอนติบอดีจำเพาะของ SSc จึงไม่ได้คะแนน** → **ไม่ถึง 9 ไม่เข้าเกณฑ์**\n- **SLE** — ไม่มีเกณฑ์ทางคลินิกของ EULAR/ACR 2019 ที่ชัดเจนเลย (ไม่มีผื่น ไม่มีแผลในปาก ไม่มีเม็ดเลือดต่ำ ไม่มีไตอักเสบ) และ **anti-Sm ลบ** · ข้ออักเสบอย่างเดียวได้ 6 คะแนน ยังไม่ถึง 10\n- **Overlap syndrome** — นิยามคือ **เข้าเกณฑ์ของโรคหนึ่งครบแล้วมีอาการของอีกโรคที่อธิบายด้วยโรคแรกไม่ได้** รายนี้ยัง **ไม่เข้าเกณฑ์โรคใดสักโรค** จึงเรียก overlap ไม่ได้\n\n**สิ่งที่ต้องทำต่อคือนัดตามดูเป็นระยะ** — UCTD ราวร้อยละ 30 จะกลายเป็นโรคที่ชัดเจนภายหลัง (RA มากที่สุด รองลงมาคือ Sjögren, SLE, MCTD) ที่เหลือคงสภาพอยู่ได้นานหลายปี",
   "มีอาการและแอนติบอดีของ CTD แต่ไม่เข้าเกณฑ์โรคใดเลย = UCTD · anti-RNP ไทเตอร์ไม่สูงพอและอาการไม่ครบ จึงยังไม่ใช่ MCTD",
   "MCTD และ UCTD", ["2.3.13", "B5.2.2-3(5)"]),
 ],
}

# ─────────────────────────────────── ประกอบร่าง ───────────────────────────────────
path = os.path.join(BUILD, "data", "air.json")
data = json.load(open(path, encoding="utf-8"))
lec = next(l for l in data if l["lec"] == "33")

# 1) หัวข้อใหม่ — ลบของเดิมถ้ามี แล้วแทรกต่อจากหัวข้อที่เกี่ยวข้อง
def put_after(after_id, section):
    secs = [s for s in lec["sections"] if s["id"] != section["id"]]
    at = next(i for i, s in enumerate(secs) if s["id"] == after_id) + 1
    secs.insert(at, section)
    lec["sections"] = secs

put_after("air-33-02c", PLEURA)
put_after("air-33-06", SSC)

# 2) ต่อท้าย md ของหัวข้อเดิม
for sid, (marker, block) in APPEND.items():
    s = next(x for x in lec["sections"] if x["id"] == sid)
    if marker not in s["md"]:
        s["md"] = s["md"].rstrip() + "\n" + block

# 3) ข้อสอบที่เติมเข้าหัวข้อเดิม
for sid, items in EXTRA_ITEMS.items():
    s = next(x for x in lec["sections"] if x["id"] == sid)
    have = {i["id"] for i in s["items"]}
    s["items"] += [i for i in items if i["id"] not in have]

# 4) subtitle และ objectives ให้ตรงกับของที่เพิ่ม
if "น้ำในเยื่อหุ้มปอด" not in lec["subtitle"]:
    lec["subtitle"] += " · น้ำในเยื่อหุ้มปอดของลูปัส · เกณฑ์ SSc 2013"
obj = "อ่านผลน้ำเจาะเยื่อหุ้มปอดของผู้ป่วย SLE และแยกออกจากการติดเชื้อและ rheumatoid pleuritis ได้"
if obj not in lec["objectives"]:
    lec["objectives"].append(obj)
obj2 = "บวกคะแนนเกณฑ์ ACR/EULAR 2013 ของ systemic sclerosis ได้ถูกต้องตามกติกานับข้อที่สูงกว่า"
if obj2 not in lec["objectives"]:
    lec["objectives"].append(obj2)

json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

nsec = len(lec["sections"])
nitem = sum(len(s["items"]) for s in lec["sections"])
print("คาบ 33: %d หัวข้อ · %d ข้อสอบ" % (nsec, nitem))
print("AIR ทั้งชุด: %d หัวข้อ" % sum(len(s["sections"]) for s in data))
print("air.json %d bytes" % os.path.getsize(path))
