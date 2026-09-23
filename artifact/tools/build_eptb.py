#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrapulmonary tuberculosis (อ.ภาณุวัฒน์ · Panuwat Wongkulab) → data/chest.json
ต้นฉบับ: สไลด์ "Extrapulmonary Tuberculosis: The Hidden Pathogen" (Apr 2026) 16 หน้า + โน้ตลายมือ
โน้ตอ่านสไลด์ทีละหน้าอยู่ที่ slides/eptb_notes.md"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
NLN = ["2.3.1(20)", "B6.2.2(8)"]
SRC = "สไลด์ อ.ภาณุวัฒน์ — Extrapulmonary TB: The Hidden Pathogen (2026)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "CH-EP-MCQ-%02d" % n

# ───────────────────────────── 1
sec("chest-eptb-01", "ภูเขาน้ำแข็งที่ซ่อนอยู่ — ภาระโรคและใครเสี่ยง",
    "EPTB คือส่วนใต้น้ำของวัณโรค: หาเชื้อยาก วินิจฉัยช้า และมักอยู่คู่กับวัณโรคปอด", 7,
"""### ตัวเชื้อเดียวกัน แต่ไปอยู่ผิดที่
**Extrapulmonary TB (EPTB)** คือวัณโรคที่เกิดนอกเนื้อปอด เชื้อยังเป็น *Mycobacterium tuberculosis* ตัวเดิม เพียงแต่ **แพร่ไปทางกระแสเลือดและน้ำเหลือง (lymphohematogenous spread)** ตั้งแต่ช่วงติดเชื้อครั้งแรก แล้วไปฝังตัวเงียบ ๆ ในอวัยวะที่มีออกซิเจนและเลือดไปเลี้ยงดี

สไลด์แบ่งกลไกไว้สองแบบ (โน้ตในห้องเขียนกำกับไว้)
- **Primary infection** → พบใน **เด็กเล็ก** ที่ภูมิคุ้มกันยังคุมเชื้อไม่อยู่ตั้งแต่แรก
- **Reactivation** → พบใน **ผู้ใหญ่** เชื้อที่ฝังตัวไว้นานกลับมาแบ่งตัวเมื่อภูมิคุ้มกันลดลง

กลุ่มเสี่ยงตามสไลด์คือ **ผู้ที่ภูมิคุ้มกันบกพร่อง** และ **ผู้ที่ได้รับเชื้อปริมาณมากตั้งแต่แรก**

### ภาพของประเทศไทย (Suksont Jit, IJID 2009)
| ตัวเลข | ความหมาย |
|---|---|
| **94 ต่อแสนประชากร** | incidence density ของวัณโรค |
| **12–13%** | สัดส่วน EPTB ในรายงานผู้ป่วยวัณโรคทั้งหมด (ที่เหลือราว 80% เป็นวัณโรคปอด) |
| **13–17%** | ผู้ป่วยวัณโรคที่ติดเชื้อ HIV ร่วมด้วย |
| **1% → 1.7%** | วัณโรคดื้อยาเพิ่มจากปี 2002 ถึง 2006 |

**ทำไมเรียกว่าภูเขาน้ำแข็ง** — ยอดที่มองเห็นคือ **smear-positive pulmonary TB** ซึ่งย้อมเจอเชื้อง่ายและรายงานง่าย ส่วนใต้น้ำคือ **EPTB และวัณโรคปอดที่ smear เป็นลบ** ซึ่งหาเชื้อยาก วินิจฉัยช้า และรักษาซับซ้อนกว่า

### เป็นทั้งปอดและนอกปอดพร้อมกันได้
อาจารย์เน้นในห้องว่า **EPTB กับวัณโรคปอดอยู่ร่วมกันได้** และบางอวัยวะเกิดจากการลุกลามต่อเนื่อง (extension) จากปอดหรือต่อมน้ำเหลืองข้างเคียง ผู้ป่วย EPTB ทุกรายจึงต้อง **ถ่ายภาพรังสีทรวงอกและส่งเสมหะ** เสมอ เพราะผลต่อการแพร่เชื้อและการแยกห้องต่างกันมาก

### ปัจจัยเสี่ยง (BMJ Best Practice)
| ปัจจัย | เหตุผล |
|---|---|
| **มาจากพื้นที่ชุก** — เอเชีย ละตินอเมริกา แอฟริกา | โอกาสติดเชื้อแฝงสูง |
| **HIV** | CD4 ต่ำ → คุมเชื้อไม่อยู่ เชื้อกระจายทั่วตัว |
| **ไตวายระยะสุดท้าย (ESRD)** | ภูมิคุ้มกันระดับเซลล์บกพร่องจาก uremia |
| **ยาเคมีบำบัด** | กดภูมิคุ้มกัน |
| **มะเร็ง** | กดภูมิคุ้มกันทั้งจากโรคและจากการรักษา |
""",
    ["EPTB ราว 12–13% ของผู้ป่วยวัณโรคในไทย ที่เหลือราว 80% เป็นวัณโรคปอด",
     "Primary infection พบในเด็ก · reactivation พบในผู้ใหญ่",
     "EPTB อยู่ร่วมกับวัณโรคปอดได้ → ต้อง CXR และส่งเสมหะทุกราย",
     "ปัจจัยเสี่ยง: มาจากพื้นที่ชุก · HIV · ESRD · ยาเคมีบำบัด · มะเร็ง"],
    [mcq(N(1), "A 38-year-old man on maintenance haemodialysis for end-stage renal disease is diagnosed with tuberculous cervical lymphadenitis. He has no cough. Which additional step is essential before deciding on infection-control measures?",
         ["No further test is needed because lymph node TB is never infectious",
          "Chest radiograph and sputum examination to look for concurrent pulmonary TB",
          "Tuberculin skin test to confirm active disease",
          "Serum adenosine deaminase level",
          "Repeat lymph node biopsy for drug-susceptibility testing"], 1,
         "**EPTB อยู่ร่วมกับวัณโรคปอดได้** และสิ่งที่ตัดสินว่าผู้ป่วย **แพร่เชื้อหรือไม่** คือมีรอยโรคที่ปอดหรือกล่องเสียงหรือไม่ ไม่ใช่ตัวต่อมน้ำเหลือง → ต้อง **CXR + เสมหะ AFB/Xpert** เสมอ\n\nผู้ป่วยรายนี้มี **ESRD** ซึ่งเป็นปัจจัยเสี่ยงของ EPTB ตามสไลด์ การไม่มีอาการไอก็ **ตัดวัณโรคปอดไม่ได้**\n\nทำไมข้ออื่นผิด: TST ไม่ใช้วินิจฉัย active TB · ADA ในเลือดไม่มีที่ใช้ · การตรวจความไวต่อยาไม่ได้ตอบคำถามเรื่องการแพร่เชื้อ",
         "EPTB ทุกราย → CXR + เสมหะ เพื่อหาวัณโรคปอดที่ซ่อนอยู่",
         "EPTB coexisting with pulmonary TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 2–3", "MED32 MCQ ข้อ 32 – ให้อาการ extrapulmonary TB ทำยังไงดี"]),
     mcq(N(2), "According to Thai surveillance data presented in the lecture, approximately what proportion of all notified TB cases are extrapulmonary?",
         ["1–2%", "12–13%", "35–40%", "50%", "80%"], 1,
         "สไลด์อ้าง **Suksont Jit, IJID 2009** — **EPTB ราว 12–13%** ของผู้ป่วยวัณโรคที่รายงานทั้งหมด ส่วน **ราว 80% เป็นวัณโรคปอด** (โน้ตในห้อง)\n\nตัวเลขอื่นในสไลด์เดียวกัน: incidence density 94/100,000 · HIV ร่วม 13–17% · วัณโรคดื้อยา 1% → 1.7%",
         "EPTB ≈ 12–13% · วัณโรคปอด ≈ 80%", "Epidemiology of EPTB in Thailand", ["สไลด์ อ.ภาณุวัฒน์ หน้า 2"]),
    ])

# ───────────────────────────── 2
sec("chest-eptb-02", "HIV เปลี่ยนแผนที่ของโรค",
    "ผู้ป่วย HIV เป็นแบบกระจายทั่วตัวและสมอง ผู้ป่วยไม่ติด HIV เป็นเฉพาะที่ — เยื่อหุ้มปอดและกระดูกสันหลัง", 7,
"""### ข้อมูลจากสไลด์ (Tawatcai W, SEATROPH 2008)
ร้อยละของผู้ป่วยในแต่ละกลุ่มที่มีรอยโรคตำแหน่งนั้น

| ตำแหน่ง | HIV บวก | HIV ลบ |
|---|---|---|
| Lymph node | 21.2 | 48.3 |
| **Pleura** | 4.6 | **74.3** |
| **Bone, spine** | 1.0 | **74.0** |
| Meninges and brain | 38.9 | 50.0 |
| Pericardium | 7.1 | 71.4 |
| Gastrointestinal | 25.0 | 75.0 |
| **Disseminated** | **87.5** | 12.5 |
| Genitourinary | 0 | 100 |
| Skin | 0 | 50 |

### อ่านตารางให้เป็นกลไก
- **HIV บวก → disseminated TB สูงถึง 87.5% (OR 41.51)** เพราะเมื่อ CD4 ต่ำ granuloma สร้างไม่ได้ เชื้อจึงไม่ถูกขังไว้ในจุดเดียว แต่กระจายไปทางกระแสเลือด (miliary)
- **เยื่อหุ้มสมองและสมอง** เป็นอีกตำแหน่งที่สไลด์ชี้ว่าต้องระวังในผู้ป่วย HIV (OR 4.47)
- **HIV ลบ → รอยโรคเฉพาะที่เด่น** โดยเฉพาะ **pleura (74.3%)** และ **bone/spine (74.0%)** ซึ่งพบน้อยมากในผู้ป่วย HIV

**ทำไมเยื่อหุ้มปอดจึงพบน้อยในผู้ป่วย HIV** — น้ำในเยื่อหุ้มปอดจากวัณโรคเกิดจาก **ปฏิกิริยาภูมิไวเกินชนิดล่าช้าของ CD4 T-cell** ต่อโปรตีนของเชื้อ ผู้ป่วยที่ไม่มี CD4 จึงสร้างปฏิกิริยานี้ได้น้อย

### กฎสองข้อที่อาจารย์ย้ำในห้อง
| กฎ | เหตุผล |
|---|---|
| **ผู้ป่วย HIV ทุกราย ต้อง CXR หาวัณโรค** | วัณโรคเป็นโรคติดเชื้อฉวยโอกาสที่พบบ่อยที่สุดและเป็นสาเหตุการตายอันดับต้นของผู้ป่วย HIV |
| **ผู้ป่วยวัณโรคทุกราย ต้องตรวจ HIV** | **มีผลกับการรักษา** — ต้องวางแผนยาต้านไวรัส (ART) จังหวะเริ่มยา ยาตีกันกับ rifampicin และการป้องกัน IRIS |

### ภาวะ disseminated (miliary) TB
เชื้อกระจายไปทั่วตัวทางกระแสเลือด ภาพรังสีทรวงอกเป็น **จุดเล็กขนาดเท่ากันราว 1–3 มม. กระจายทั่วปอด** ผู้ป่วยมีไข้เรื้อรัง น้ำหนักลด อาจมีตับม้ามโต ไขกระดูกกดตัว และ **ต้องหาวัณโรคเยื่อหุ้มสมองร่วมด้วยเสมอ** การยืนยันมักใช้เนื้อเยื่อ เช่น ไขกระดูกหรือตับ ร่วมกับเพาะเชื้อจากเลือดในผู้ป่วย HIV
""",
    ["HIV บวก → disseminated TB 87.5% (OR 41.51) และเยื่อหุ้มสมองต้องระวัง",
     "HIV ลบ → pleura 74.3% และ bone/spine 74.0% เด่น",
     "ผู้ป่วย HIV ทุกราย CXR หาวัณโรค · ผู้ป่วยวัณโรคทุกรายตรวจ HIV",
     "TB pleuritis ต้องอาศัย CD4 → จึงพบน้อยในผู้ป่วย HIV ที่ CD4 ต่ำ"],
    [mcq(N(3), "A 31-year-old man with newly diagnosed HIV infection (CD4 count 42 cells/µL) has 6 weeks of fever and weight loss. Chest radiograph shows innumerable 2-mm nodules throughout both lungs. Based on the pattern of EPTB by HIV status, which form of tuberculosis is he most likely to have?",
         ["Isolated tuberculous pleuritis", "Tuberculous spondylitis", "Disseminated (miliary) tuberculosis", "Genitourinary tuberculosis", "Tuberculous lymphadenitis without systemic spread"], 2,
         "**HIV บวกร่วมกับ CD4 ต่ำมาก** → granuloma สร้างไม่ได้ เชื้อจึงกระจายทางกระแสเลือด ข้อมูลในสไลด์พบ **disseminated TB 87.5% ในผู้ป่วย HIV เทียบกับ 12.5% ในผู้ป่วย HIV ลบ (OR 41.51)** และ CXR เป็น **miliary pattern**\n\nทำไมข้ออื่นผิด: **pleura (4.6%) และ bone/spine (1.0%) พบน้อยมากในผู้ป่วย HIV** เพราะต้องอาศัยปฏิกิริยาภูมิคุ้มกันระดับเซลล์ · GU TB ในข้อมูลชุดนี้พบเฉพาะผู้ป่วย HIV ลบ\n\nขั้นต่อไปที่ต้องคิดเสมอ: **ตรวจหาวัณโรคเยื่อหุ้มสมอง** เพราะเปลี่ยนระยะเวลารักษาและจังหวะเริ่ม ART",
         "HIV + CD4 ต่ำ + miliary → disseminated TB · อย่าลืมหา TB meningitis",
         "Disseminated TB in HIV", ["สไลด์ อ.ภาณุวัฒน์ หน้า 4"], NLN + ["2.3.1(9)"]),
     mcq(N(4), "Which EPTB site was most characteristic of HIV-negative rather than HIV-positive patients in the Thai series presented?",
         ["Disseminated disease", "Meninges and brain", "Pleura", "No difference between groups at any site", "Skin only"], 2,
         "ในผู้ป่วย **HIV ลบ** รอยโรคเฉพาะที่เด่น — **pleura 74.3% และ bone/spine 74.0%** เทียบกับเพียง 4.6% และ 1.0% ในผู้ป่วย HIV บวก\n\n**กลไก**: TB pleuritis เป็น **ปฏิกิริยาภูมิไวเกินชนิดล่าช้าที่อาศัย CD4 T-cell** ผู้ป่วยที่มี CD4 ปกติจึงสร้างน้ำในเยื่อหุ้มปอดที่มี lymphocyte เด่นได้ ส่วนผู้ป่วย HIV ที่ CD4 ต่ำจะเป็นแบบ disseminated แทน",
         "HIV ลบ → pleura และ bone/spine · HIV บวก → disseminated",
         "EPTB pattern by HIV status", ["สไลด์ อ.ภาณุวัฒน์ หน้า 4"]),
     mcq(N(5), "A 27-year-old woman is newly diagnosed with tuberculous lymphadenitis. Which test must be offered to every patient with tuberculosis because its result changes management?",
         ["Serum ADA", "HIV testing", "Tuberculin skin test", "Serum IgG for M. tuberculosis", "Chest CT scan"], 1,
         "อาจารย์ย้ำในห้อง: **ผู้ป่วยวัณโรคทุกรายต้องตรวจ HIV เพราะมีผลกับการรักษา** — ถ้าผลบวกต้องวางแผน **เริ่ม ART** (โดยทั่วไปภายใน 2–8 สัปดาห์หลังเริ่มยาวัณโรค) ระวัง **ยาตีกันกับ rifampicin** ให้ **co-trimoxazole prophylaxis** และเฝ้าระวัง **IRIS**\n\nกลับกัน **ผู้ป่วย HIV ทุกรายต้อง CXR หาวัณโรค**\n\nทำไมข้ออื่นผิด: TST ไม่ใช้วินิจฉัย active TB · serology ไม่แนะนำให้ใช้ · ADA ในเลือดไม่มีที่ใช้",
         "ผู้ป่วยวัณโรคทุกราย → ตรวจ HIV", "HIV testing in TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 4 (โน้ตในห้อง)"], NLN + ["3.3.15"]),
    ])

# ───────────────────────────── 3
sec("chest-eptb-03", "ทำไม EPTB วินิจฉัยยาก — smear, culture, NAAT และ TST",
    "EPTB มีเชื้อน้อย (paucibacillary) การย้อมจึงมักลบ culture ช้าแต่แม่น NAAT เร็วแต่ความไวขึ้นกับสิ่งส่งตรวจ", 9,
"""### ปัญหาหลักคือเชื้อน้อย
EPTB ส่วนใหญ่เป็น **paucibacillary** คือมีเชื้อในสิ่งส่งตรวจน้อยมาก ต่างจากวัณโรคปอดชนิดมีโพรงที่มีเชื้อนับล้านตัว ผลคือ
- **ต้องได้การวินิจฉัยทางจุลชีววิทยาจากเนื้อเยื่อหรือสารน้ำ** จากอวัยวะที่เป็นโรคโดยตรง
- **โอกาสเจอเชื้อในสิ่งส่งตรวจต่ำ** จึงต้องใช้หลายวิธีร่วมกัน

### ผลตอบรับของการย้อมและการเพาะเชื้อ (สไลด์หน้า 8)
| สิ่งส่งตรวจ | AFB smear | Culture |
|---|---|---|
| **Pleural fluid** | **< 10%** | 12–70% |
| **CSF** | 5–37% | 40–80% |

**ข้อสรุป** — **smear ลบไม่ได้ตัดวัณโรค** และ culture ให้ผลดีกว่ามาก แต่ต้องรอหลายสัปดาห์

### Culture (มาตรฐานทองคำ) กับ NAAT (สไลด์หน้า 11)
| | **TB culture (MGIT)** | **NAAT เช่น GeneXpert** |
|---|---|---|
| จุดแข็ง | ยืนยันว่าเชื้อ **ยังมีชีวิต** · ไวมาก (ตรวจพบได้ที่ **10–100 ตัว/มล.**) · **แยก MTB จาก NTM** ได้ · ทำ **DST ครบทุกตัวยา** | **เร็ว** ได้ผลภายในวันเดียว · บอก **rifampicin resistance** ได้ทันที |
| ความไวใน EPTB | สูงที่สุด | **ต่อมน้ำเหลือง 0.96** (ดีมาก) · **น้ำในเยื่อหุ้มปอด 0.34** (แย่) |
| ข้อจำกัด | **ช้า 2–8 สัปดาห์** | **แยกเชื้อเป็นหรือตายไม่ได้** · ครอบคลุม mutation ไม่ครบ · จำกัดจำนวนเป้าหมายต่อการตรวจ (ราว 4 สี) |

**ใช้อย่างไร** — ส่ง **ทั้ง NAAT และ culture** จากสิ่งส่งตรวจเดียวกันเสมอ NAAT ให้คำตอบเร็วเพื่อเริ่มยา ส่วน culture ใช้ยืนยันและทำ DST ถ้า NAAT จากน้ำในเยื่อหุ้มปอดเป็นลบ **อย่าเพิ่งตัดวัณโรค** เพราะความไวเพียงราวหนึ่งในสาม

### Tuberculin skin test (TST)
**TST ไม่ใช้วินิจฉัยวัณโรคระยะแสดงอาการ** ใช้ช่วยวินิจฉัย **การติดเชื้อวัณโรค (TB infection / latent)** เท่านั้น เพราะ
- ผลบวกบอกเพียงว่า **เคยสัมผัสเชื้อ** ซึ่งในไทยพบในคนจำนวนมากอยู่แล้ว
- ผลลบก็ **ตัดโรคไม่ได้** โดยเฉพาะในผู้ป่วยที่เป็นโรครุนแรงหรือภูมิคุ้มกันต่ำ (anergy)

### ลำดับคิดเมื่อสงสัย EPTB
1. เก็บสิ่งส่งตรวจจาก **อวัยวะที่เป็นโรคโดยตรง** — เจาะน้ำ เจาะดูดด้วยเข็ม หรือตัดชิ้นเนื้อ
2. ส่ง **AFB smear + NAAT + culture/DST** และ **พยาธิวิทยา** (หา caseating granuloma)
3. ส่ง **ตัวบ่งชี้ทางชีวเคมี** ของสารน้ำ เช่น ADA (หัวข้อถัดไป)
4. **CXR + เสมหะ** หาวัณโรคปอดร่วม และ **ตรวจ HIV**
""",
    ["EPTB = paucibacillary → smear ลบไม่ตัดโรค",
     "AFB smear: pleural < 10% · CSF 5–37% · culture: pleural 12–70% · CSF 40–80%",
     "Culture = gold standard: เชื้อเป็น/ตาย · แยก NTM · DST ครบ",
     "GeneXpert: LN ไว 0.96 · pleural fluid ไวเพียง 0.34",
     "TST ไม่ใช้วินิจฉัย active TB — ใช้กับ TB infection"],
    [mcq(N(6), "A 45-year-old man has a lymphocytic exudative pleural effusion. Pleural fluid AFB smear is negative. Which statement about this result is most accurate?",
         ["It excludes tuberculous pleuritis",
          "It is expected, because AFB smear of pleural fluid is positive in fewer than 10% of tuberculous pleuritis cases",
          "It indicates non-tuberculous mycobacterial infection",
          "It means the effusion is a transudate",
          "It should be repeated daily until positive before starting treatment"], 1,
         "TB pleuritis เป็น **paucibacillary** และเกิดจากปฏิกิริยาภูมิไวเกิน ไม่ใช่เชื้อจำนวนมากในน้ำ สไลด์ระบุ **AFB smear จากน้ำเยื่อหุ้มปอดบวก < 10%** และ culture บวก 12–70%\n\nดังนั้นผล smear ลบ **เป็นเรื่องที่คาดไว้แล้ว ไม่ใช่เหตุผลให้ตัดโรคหรือรอ** การวินิจฉัยอาศัย **ADA, สัดส่วน lymphocyte, culture และ pleural biopsy**",
         "Pleural fluid AFB smear บวก < 10% → ลบไม่ได้ตัดโรค", "AFB smear yield in EPTB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 8"], NLN + ["3.1.9"]),
     mcq(N(7), "Which advantage belongs to mycobacterial culture rather than to a nucleic acid amplification test such as GeneXpert?",
         ["Results within 2 hours", "Detection of rifampicin resistance by rpoB mutation",
          "Distinguishing live from dead bacilli and allowing full drug-susceptibility testing",
          "Higher sensitivity in pleural fluid than in lymph node tissue", "No need for a clinical specimen"], 2,
         "สไลด์หน้า 11 — **culture เป็นมาตรฐานทองคำ** เพราะ **ยืนยันว่าเชื้อยังมีชีวิต**, **ไวมาก (10–100 ตัว/มล.)**, **แยก MTB จาก NTM** และ **ทำ DST ได้ครบทุกตัวยา**\n\n**NAAT** จุดแข็งคือ **เร็ว** และบอก **rifampicin resistance** ได้ แต่ **แยกเชื้อเป็นหรือตายไม่ได้** (จึงไม่ใช้ติดตามผลการรักษา) และครอบคลุม mutation ไม่ครบ",
         "Culture = เชื้อเป็น/ตาย + NTM + DST ครบ · NAAT = เร็ว + RIF resistance", "Culture vs NAAT", ["สไลด์ อ.ภาณุวัฒน์ หน้า 11"]),
     mcq(N(8), "In which specimen does GeneXpert (NAAT) have the highest pooled sensitivity for EPTB according to the lecture?",
         ["Pleural fluid", "Lymph node tissue or aspirate", "Urine", "Serum", "Ascitic fluid"], 1,
         "สไลด์หน้า 11 — **ต่อมน้ำเหลือง pooled sensitivity 0.96** เทียบกับ **น้ำในเยื่อหุ้มปอดเพียง 0.34**\n\n**เหตุผล**: ต่อมน้ำเหลืองมีเชื้ออยู่ในเนื้อเยื่อจำนวนมากกว่า ส่วนน้ำในเยื่อหุ้มปอดเกิดจากปฏิกิริยาภูมิคุ้มกันต่อเชื้อจำนวนน้อยที่อยู่ในเยื่อหุ้ม ไม่ได้ลอยอยู่ในน้ำ → **NAAT จากน้ำเยื่อหุ้มปอดที่เป็นลบจึงตัดโรคไม่ได้**",
         "Xpert ไว: LN 0.96 >> pleural fluid 0.34", "NAAT sensitivity by site", ["สไลด์ อ.ภาณุวัฒน์ หน้า 11"]),
     mcq(N(9), "A 40-year-old woman with suspected tuberculous meningitis has a tuberculin skin test of 0 mm. What is the correct interpretation?",
         ["Tuberculous meningitis is excluded", "She must have non-tuberculous mycobacterial infection",
          "A negative TST does not exclude active TB; TST is not a diagnostic test for active disease",
          "She should receive BCG vaccination", "The test should be read at 2 hours instead"], 2,
         "สไลด์หน้า 8 — **TST ไม่ใช้วินิจฉัย active TB** ใช้ช่วยวินิจฉัย **TB infection** เท่านั้น\n\nผลลบพบได้บ่อยในผู้ป่วยวัณโรครุนแรง ภาวะทุพโภชนาการ หรือภูมิคุ้มกันต่ำ (**anergy**) และผลบวกก็บอกเพียงว่าเคยสัมผัสเชื้อ การวินิจฉัย TB meningitis อาศัย **CSF profile, ADA, NAAT, culture และภาพสมอง**",
         "TST ไม่ใช้วินิจฉัย active TB — ลบก็ตัดโรคไม่ได้", "Role of TST", ["สไลด์ อ.ภาณุวัฒน์ หน้า 8"], NLN + ["3.1.11"]),
    ], NLN + ["3.1.9", "3.1.11", "B1.5.2(5)"])

# ───────────────────────────── 4
sec("chest-eptb-04", "ถอดรหัสสารน้ำ: pleural, pericardial และ CSF + ADA",
    "ตารางที่อาจารย์ติดดาวมากที่สุด: lymphocyte เด่น โปรตีนสูง น้ำตาลต่ำ และ ADA เป็นตัวแทนของภูมิคุ้มกันระดับเซลล์", 10,
"""### ตาราง body fluid (แนวทางวัณโรคประเทศไทย 2561) ⭐
อาจารย์ติดดาว **pleural ★★★★** และ **CSF ★★★** — สองคอลัมน์นี้คือส่วนที่ต้องจำให้ได้

| | **Pleural effusion** | Pericardial effusion | **CSF** |
|---|---|---|---|
| ลักษณะ | **usually straw colored** | straw colored หรือ serosanguinous | **clear early, turbid with chronicity** |
| pH | rarely < 7.3, never > 7.4 | ไม่มีข้อมูลชัด | ไม่มีข้อมูลชัด |
| Cell count | **1,000–5,000** | ไม่มีข้อมูลชัด | **100–500** |
| Differential | **lymphocyte 50–90%, eosinophil < 5%, mesothelial cell น้อย** | lymphocyte เพิ่ม · ระยะแรก PMN เด่น ต่อมา mononuclear | **ระยะแรก PMN เด่น ต่อมา mononuclear ถึง 95%** |
| Protein | **usually > 2.5 g/dL** | usually high | **usually high (100–500 mg/dL)** |
| Glucose | **usually < serum** | low | **40–50 mg/dL (ราว 50% ของน้ำตาลในเลือด)** |
| Cytology | no malignant cell | no malignant cell | no malignant cell |

**ความหมายของบางช่อง** (โน้ตในห้อง)
- **Eosinophil < 5%** บอกว่า **ไม่ใช่ภาวะภูมิแพ้** หรือภาวะที่ทำให้ eosinophil สูง เช่น มีเลือดหรืออากาศในช่องเยื่อหุ้มปอด
- **Mesothelial cell น้อย** เพราะ fibrin และการอักเสบคลุมผิวเยื่อหุ้มจนเซลล์ mesothelial หลุดลงมาไม่ได้
- **ช่วงแรก PMN เด่น** ทั้งใน CSF และ pericardial fluid → ถ้าเจาะเร็วอาจหลอกว่าเป็นแบคทีเรียได้ ต้องดูบริบทและเจาะซ้ำ

### ADA — ตัวแทนของภูมิคุ้มกันระดับเซลล์
**กลไก**: T-cell แบ่งตัว → เพิ่ม **purine metabolism** → เอนไซม์ **adenosine deaminase** สูงขึ้น
ADA สูงจึงสะท้อน **การตอบสนองของภูมิคุ้มกันระดับเซลล์ที่กำลังทำงาน** โดยเฉพาะการแบ่งตัวของ lymphocyte ซึ่งเป็นแก่นของการอักเสบจากวัณโรค

| สารน้ำ | จุดตัด | ความแม่น |
|---|---|---|
| **Pleural และ pericardial** | **40–45 U/L** | pleural ที่ 40 IU/L: **sens 92% / spec 89%** |
| **Peritoneum** | **36–40 U/L** | sens 100% / spec 97% |
| **CSF** | **20 U/L** (ผันแปรมาก) | ที่ 8 IU/L: sens 59% / spec 96% |

### ผลบวกลวง — ADA สูงไม่ได้แปลว่าวัณโรคเสมอ
- **Empyema** และ **parapneumonic effusion** (แต่ neutrophil เด่น)
- **Lymphoma** (lymphocyte เด่นเหมือนกัน → กับดักที่สำคัญที่สุด)
- **Malignant pleural effusion**
- **Collagen vascular disease** เช่น rheumatoid pleuritis, SLE

**กฎการใช้** — อ่าน ADA **คู่กับชนิดเซลล์เสมอ**: ADA สูง + lymphocyte เด่น + ไม่พบเซลล์มะเร็ง ในพื้นที่ที่วัณโรคชุกอย่างไทย → **เริ่มยาวัณโรคได้** พร้อมส่ง culture ไว้ ส่วน ADA สูง + neutrophil เด่น → คิดถึง empyema ก่อน
""",
    ["Pleural TB: straw colored · lymph 50–90% · eos < 5% · mesothelial น้อย · protein > 2.5 · glucose < serum",
     "CSF TB: clear → turbid · cell 100–500 · protein 100–500 mg/dL · glucose 40–50 (≈50% ของเลือด)",
     "ADA cut-off: pleural/pericardial 40–45 · peritoneum 36–40 · CSF 20",
     "ADA บวกลวง: empyema · lymphoma · malignancy · parapneumonic · collagen vascular disease",
     "อ่าน ADA คู่กับชนิดเซลล์เสมอ"],
    [mcq(N(10), "Pleural fluid from a 30-year-old man shows: straw-coloured exudate, WBC 2,400/µL with 85% lymphocytes, 2% eosinophils, rare mesothelial cells, protein 5.1 g/dL, glucose lower than serum, ADA 68 U/L, cytology negative. What is the most likely diagnosis?",
         ["Congestive heart failure", "Tuberculous pleuritis", "Parapneumonic effusion", "Chylothorax", "Pulmonary embolism"], 1,
         "ครบทุกช่องของตาราง TB pleural effusion ตามแนวทางไทย 2561\n- **straw colored** · **cell 1,000–5,000** · **lymphocyte 50–90%** · **eosinophil < 5%** · **mesothelial cell น้อย** · **protein > 2.5 g/dL** · **glucose < serum** · ไม่มีเซลล์มะเร็ง\n- **ADA 68 > 40 U/L** (sens 92% / spec 89%)\n\nทำไมข้ออื่นผิด: heart failure เป็น transudate · parapneumonic effusion มี **neutrophil เด่น** · chylothorax เป็นน้ำขาวขุ่น triglyceride สูง",
         "Lymphocytic exudate + ADA > 40 + mesothelial น้อย = TB pleuritis", "Pleural fluid profile in TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 9–10", "MED31 MCQ ข้อ 72 – Yellow color exudate ADA 50 ถามว่า fluid มาจากไหน"], NLN + ["2.3.10(7)", "B6.2.2(10)"]),
     mcq(N(11), "A 55-year-old man has a lymphocyte-predominant pleural effusion with ADA 52 U/L. Pleural fluid cytology is negative, but he has generalised lymphadenopathy and splenomegaly. Which condition is the most important cause of a false-positive ADA to exclude?",
         ["Congestive heart failure", "Nephrotic syndrome", "Lymphoma", "Hypothyroidism", "Cirrhosis"], 2,
         "สไลด์หน้า 10 — ADA สูงไม่ได้จำเพาะกับวัณโรค **ผลบวกลวงพบใน empyema, lymphoma, malignant pleural effusion, parapneumonic effusion และ collagen vascular disease**\n\n**Lymphoma เป็นกับดักที่สำคัญที่สุด** เพราะให้ทั้ง **ADA สูง และ lymphocyte เด่น** เหมือนวัณโรคทุกประการ ผู้ป่วยรายนี้มี **ต่อมน้ำเหลืองโตทั่วตัวและม้ามโต** จึงต้องตัดชิ้นเนื้อต่อมน้ำเหลืองหรือทำ pleural biopsy\n\nข้ออื่นเป็นสาเหตุของ transudate ซึ่ง ADA ไม่สูง",
         "ADA สูง + lymphocyte เด่น → วัณโรค หรือ lymphoma", "False-positive ADA", ["สไลด์ อ.ภาณุวัฒน์ หน้า 10"], NLN + ["2.3.10(7)"]),
     mcq(N(12), "Why is adenosine deaminase elevated in tuberculous serositis?",
         ["It is secreted by the mycobacteria themselves",
          "It reflects T-lymphocyte proliferation and purine metabolism during an active cell-mediated immune response",
          "It leaks from damaged hepatocytes",
          "It is produced by mesothelial cells in response to fibrin",
          "It is a marker of neutrophil degranulation"], 1,
         "สไลด์หน้า 10 วางกลไกเป็นลูกศรสามขั้น: **T-cell proliferation → purine metabolism → ADA elevation**\n\nADA จึงเป็น **surrogate marker ของภูมิคุ้มกันระดับเซลล์** — สะท้อนการแบ่งตัวของ lymphocyte ซึ่งเป็นแก่นของการอักเสบแบบ granulomatous ในวัณโรค ไม่ได้มาจากตัวเชื้อ\n\nนี่คือเหตุผลที่ **โรคอื่นที่มี lymphocyte แบ่งตัวมาก (เช่น lymphoma)** ก็ทำให้ ADA สูงได้",
         "ADA = ตัวแทนของ T-cell ที่แบ่งตัว ไม่ใช่ของตัวเชื้อ", "Mechanism of ADA", ["สไลด์ อ.ภาณุวัฒน์ หน้า 10"]),
     mcq(N(13), "Which ADA cut-off is used for tuberculous peritonitis in ascitic fluid, according to the lecture?",
         ["8 U/L", "20 U/L", "36–40 U/L", "70–80 U/L", "ADA is not useful in ascites"], 2,
         "สไลด์หน้า 10 — จุดตัดของ ADA แยกตามสารน้ำ\n- **Pleural และ pericardial 40–45 U/L**\n- **Peritoneum 36–40 U/L** (sens 100% / spec 97%)\n- **CSF 20 U/L** (ผันแปรมาก ที่ 8 IU/L sens 59% / spec 96%)",
         "ADA: pleural/pericardial 40–45 · ascites 36–40 · CSF 20", "ADA cut-offs by fluid", ["สไลด์ อ.ภาณุวัฒน์ หน้า 10"]),
    ], NLN + ["2.3.10(7)", "B6.2.2(10)"])

# ═══ ต่อส่วนที่ 2 ด้านล่าง ═══
