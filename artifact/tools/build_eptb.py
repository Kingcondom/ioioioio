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


# ───────────────────────────── 5
sec("chest-eptb-05", "Case 01 — วัณโรคเยื่อหุ้มปอด (TB pleuritis)",
    "ไข้กึ่งเฉียบพลัน เจ็บหน้าอกเวลาหายใจ ไม่ตอบสนองยา CAP → น้ำ lymphocyte เด่น + ADA > 40", 8,
"""### เคสจากสไลด์
| | |
|---|---|
| **อาการสำคัญ** | ไข้กึ่งเฉียบพลัน ไอต่อเนื่อง **เจ็บหน้าอกเวลาหายใจ (pleuritic chest pain)** น้ำหนักลดโดยไม่ทราบสาเหตุ |
| **ประวัติ** | อาการทางเดินหายใจแย่ลงเรื่อย ๆ หลายสัปดาห์ **ไม่ตอบสนองต่อยารักษาปอดอักเสบชุมชน (CAP) มาตรฐาน** |
| **ภาพรังสี** | **น้ำในเยื่อหุ้มปอดข้างเดียว** (ด้านซ้าย) |
| **สารน้ำ** | **exudate สีฟาง** · **lymphocyte 50–90%** · **eosinophil < 5%** · mesothelial cell น้อย |
| **การวินิจฉัย** | **TB pleurisy** ยืนยันด้วย **ADA > 40 IU/L** |

**คำถามแรกที่อาจารย์ให้ถามตัวเอง** (โน้ตในห้อง) — ไข้ ไอ น้ำหนักลด และน้ำในเยื่อหุ้มปอดข้างเดียว เป็น **การติดเชื้อ หรือ มะเร็งปอด**? สองโรคนี้ให้ exudate ที่ lymphocyte เด่นเหมือนกัน สิ่งที่ช่วยแยกคือ **อายุ ADA cytology และ mesothelial cell**

### กลไก
จุดวัณโรคเล็ก ๆ ใต้เยื่อหุ้มปอดแตกเข้าช่องเยื่อหุ้ม → โปรตีนของเชื้อกระตุ้น **ปฏิกิริยาภูมิไวเกินชนิดล่าช้า (CD4 T-cell)** → lymphocyte เข้ามาจำนวนมาก + ความซึมผ่านของหลอดเลือดเพิ่ม + การระบายน้ำเหลืองถูกอุด
ผลคือ **exudate ที่ lymphocyte เด่นและ ADA สูง แต่แทบไม่มีเชื้อในน้ำ**

### การวินิจฉัย
| การตรวจ | ผลที่คาด |
|---|---|
| Light's criteria | **exudate** |
| Cell | **lymphocyte เด่น** · mesothelial cell น้อย (มากกว่า 5% ทำให้วัณโรคมีโอกาสน้อยลง) |
| **ADA** | **> 40 U/L** → sens 92% / spec 89% |
| AFB smear | บวก **< 10%** |
| Xpert จากน้ำ | ไวเพียง **0.34** |
| Culture จากน้ำ | 12–70% |
| **Pleural biopsy** | พบ **caseating granuloma** และเพาะเชื้อได้ดีที่สุด → ใช้เมื่อผลยังไม่ชัด |

### การรักษา
- **สูตร 2IRZE/4IR รวม 6 เดือน**
- **ไม่ให้ corticosteroid เป็นกิจวัตร** (สไลด์หน้า 14 จัดอยู่ในกลุ่ม not recommended)
- เจาะระบายน้ำเพื่อบรรเทาอาการเหนื่อยได้ ไม่จำเป็นต้องใส่สายระบายทุกราย
- น้ำอาจหายเองได้แม้ไม่รักษา แต่ผู้ป่วยจำนวนมากจะ **กลับมาเป็นวัณโรคปอดภายหลัง** จึงต้องรักษาทุกราย
""",
    ["Pleuritic chest pain + ไม่ตอบสนองยา CAP + น้ำข้างเดียว → คิดถึง TB pleuritis",
     "DDx หลักของ lymphocytic exudate คือ วัณโรค กับ มะเร็ง",
     "ADA > 40 IU/L ยืนยันในบริบทที่ชุก · pleural biopsy ไวที่สุด",
     "รักษา 2IRZE/4IR · ไม่ให้ steroid เป็นกิจวัตร"],
    [mcq(N(14), "A 34-year-old man has 4 weeks of low-grade fever, dry cough, left pleuritic chest pain and 5 kg weight loss. He did not improve after 7 days of amoxicillin-clavulanate plus azithromycin. Chest radiograph shows a moderate left pleural effusion without parenchymal infiltrate. What is the most appropriate next step?",
         ["Switch to intravenous carbapenem", "Diagnostic thoracentesis with cell count, protein, LDH, glucose, ADA, cytology, AFB smear, NAAT and mycobacterial culture",
          "CT pulmonary angiography", "Start empirical prednisolone", "Chest tube insertion and pleurodesis"], 1,
         "นี่คือเคส 01 ในสไลด์ — **ไข้กึ่งเฉียบพลัน เจ็บหน้าอกเวลาหายใจ น้ำหนักลด ไม่ตอบสนองยา CAP และน้ำในเยื่อหุ้มปอดข้างเดียว** ต้อง **เจาะน้ำส่งตรวจให้ครบในครั้งเดียว** เพื่อแยก **วัณโรค มะเร็ง และ parapneumonic effusion**\n\nทำไมข้ออื่นผิด: เปลี่ยนยาปฏิชีวนะโดยยังไม่รู้ชนิดของน้ำเป็นการรักษาแบบเดา · steroid เดี่ยวกดภูมิคุ้มกันโดยไม่ฆ่าเชื้อ · pleurodesis ปิดโอกาสวินิจฉัย",
         "น้ำในเยื่อหุ้มปอดที่ยังไม่รู้สาเหตุ → เจาะส่งตรวจให้ครบรวม ADA", "Approach to TB pleural effusion", ["สไลด์ อ.ภาณุวัฒน์ หน้า 5", "MED31 MCQ ข้อ 27 – Light criteria exudative, ADA > 40 ต้อง treat ยังไงต่อ"], NLN + ["2.3.10(7)", "2.1.35"]),
     mcq(N(15), "A 29-year-old woman has a lymphocytic exudative pleural effusion with ADA 74 U/L, negative AFB smear, negative Xpert MTB/RIF on pleural fluid and negative cytology. What is the best management?",
         ["Observe, because negative Xpert excludes TB", "Start anti-tuberculous therapy (2IRZE/4IR) while awaiting mycobacterial culture",
          "Start 2IRZE/10IR because pleural TB needs 12 months", "Add prednisolone to anti-tuberculous therapy", "Refer for pleurectomy"], 1,
         "**Xpert จากน้ำเยื่อหุ้มปอดไวเพียง 0.34** ผลลบจึงตัดโรคไม่ได้ ภาพรวม **lymphocytic exudate + ADA 74 + cytology ลบ ในผู้ป่วยอายุน้อยในพื้นที่ชุก** เพียงพอที่จะ **เริ่มยาวัณโรค** พร้อมรอ culture\n\n**ระยะเวลา**: TB pleura อยู่ในกลุ่ม **6 เดือน (2IRZE/4IR)** ร่วมกับต่อมน้ำเหลือง เยื่อหุ้มหัวใจ และระบบทางเดินปัสสาวะ\n\n**Steroid ไม่แนะนำเป็นกิจวัตรใน TB pleura** (สไลด์หน้า 14)",
         "TB pleura: เริ่มยาได้จาก ADA + lymphocyte · 6 เดือน · ไม่ให้ steroid", "Treatment of TB pleuritis", ["สไลด์ อ.ภาณุวัฒน์ หน้า 10–14", "MED34 MCQ ครั้งที่ 2 (RS ข้อ 5) – Pleural ADA 70 AFB negative → TB"], NLN + ["2.3.10(7)"]),
    ], NLN + ["2.3.10(7)", "B6.2.2(10)", "2.1.35"])

# ───────────────────────────── 6
sec("chest-eptb-06", "Case 02 — วัณโรคต่อมน้ำเหลือง (TB lymphadenitis)",
    "ก้อนที่คอ โตช้า ไม่เจ็บ แข็ง ไม่มีการอักเสบเฉียบพลัน → FNA หรือตัดชิ้นเนื้อ พบ caseating granuloma", 8,
"""### เคสจากสไลด์
| | |
|---|---|
| **อาการสำคัญ** | คลำได้ **ก้อนแข็งที่คอ** |
| **ประวัติ** | ต่อมน้ำเหลืองที่คอ **โตช้า ๆ ไม่เจ็บ ทั้งสองข้าง** เป็นสัปดาห์ **ไม่มีอาการอักเสบเฉียบพลัน** (ไม่แดง ไม่ร้อน) |
| **หัตถการ** | **excisional biopsy หรือ fine needle aspiration (FNA)** |
| **พยาธิวิทยา** | **caseous (cheese-like) granulomatous inflammation** · ให้ผลวินิจฉัยทางพยาธิวิทยา **100%** ใน LN EPTB |
| **การวินิจฉัย** | **TB lymphadenitis** — พบ **AFB รูปร่างเป็นเม็ดลูกปัด (bead-like)** |

### ลักษณะทางคลินิก (สไลด์หน้า 3)
- **ไม่เจ็บ โตช้าเป็นสัปดาห์ แข็ง** เป็นข้างเดียวหรือสองข้างก็ได้
- เป็น EPTB ที่พบบ่อยตำแหน่งหนึ่ง โดยเฉพาะต่อมที่คอ
- ถ้าปล่อยไว้ ต่อมจะติดกันเป็นกลุ่ม (matted) นิ่มลงเป็นหนอง **cold abscess** และอาจแตกเป็นรูเปิดเรื้อรัง (scrofuloderma)

### การวินิจฉัยแยกโรคที่ต้องคิดคู่เสมอ
อาจารย์เน้นในห้องว่า **ก้อนที่คอต้องคิดถึงมะเร็งเสมอ** แล้วถามต่อว่าเป็น **primary หรือ secondary**
| กลุ่ม | สิ่งที่ต้องทำ |
|---|---|
| **มะเร็งแพร่กระจายมาที่ต่อม** | **ตรวจศีรษะและลำคอ** หา primary เช่น มะเร็งหลังโพรงจมูก |
| **Lymphoma** | ตัดทั้งต่อมเพื่อดูโครงสร้าง |
| **ร่วมกับน้ำในเยื่อหุ้มปอด** | **ตรวจเยื่อหุ้มปอด** — วัณโรคหรือมะเร็งที่ลามมา |
| NTM · cat-scratch · reactive | พบในบางบริบท โดยเฉพาะเด็ก |

### การรักษา
- **2IRZE/4IR รวม 6 เดือน**
- **ไม่ให้ steroid เป็นกิจวัตร**
- **Paradoxical reaction** — ต่อมอาจโตขึ้นหรือเกิดต่อมใหม่ระหว่างรักษาได้ในช่วงแรก (โดยเฉพาะผู้ป่วย HIV ที่เริ่ม ART = IRIS) **ไม่ได้แปลว่ายาล้มเหลว** ถ้าเชื้อไวต่อยา ให้ยาเดิมต่อ อาจเจาะระบายหนองได้
""",
    ["LN TB: ไม่เจ็บ โตช้าเป็นสัปดาห์ แข็ง ไม่มีการอักเสบเฉียบพลัน",
     "FNA/excision → caseating granuloma + AFB bead-like · histology ให้ผล 100%",
     "Xpert จากต่อมน้ำเหลืองไว 0.96",
     "ก้อนที่คอ → คิดถึงมะเร็งเสมอ ตรวจศีรษะลำคอหา primary",
     "Paradoxical enlargement ระหว่างรักษา ≠ ยาล้มเหลว"],
    [mcq(N(16), "A 26-year-old man has 6 weeks of painless, firm, bilateral posterior cervical lymph node enlargement without redness or warmth. He has low-grade evening fever. Which investigation gives the highest diagnostic yield?",
         ["Serum ADA", "Tuberculin skin test", "Fine needle aspiration or excisional biopsy of the node for histology, AFB, NAAT and culture",
          "Ultrasound of the neck alone", "Trial of amoxicillin for 2 weeks"], 2,
         "เคส 02 ในสไลด์ — **ต่อมน้ำเหลืองที่คอโตช้า ไม่เจ็บ แข็ง ไม่มีการอักเสบเฉียบพลัน** → ต้องได้ **เนื้อเยื่อ**\n\n**Excisional biopsy หรือ FNA** ให้ผลทางพยาธิวิทยาสูงถึง **100%** พบ **caseating granuloma** และ **Xpert จากต่อมน้ำเหลืองไว 0.96** ร่วมกับ culture เพื่อทำ DST\n\nทำไมข้ออื่นผิด: ADA ในเลือดและ TST ไม่ใช้วินิจฉัย · อัลตราซาวนด์อย่างเดียวไม่ให้การวินิจฉัย · ลองยาปฏิชีวนะทำให้ล่าช้า",
         "ต่อมน้ำเหลืองโตเรื้อรัง → ต้องได้เนื้อเยื่อ (FNA/excision)", "Diagnosis of TB lymphadenitis", ["สไลด์ อ.ภาณุวัฒน์ หน้า 6, 11"], NLN + ["2.1.57"]),
     mcq(N(17), "A 58-year-old heavy smoker has a 3-cm hard, painless, fixed upper cervical lymph node for 2 months. FNA shows no granuloma. According to the lecture's approach, what must be done next?",
         ["Treat empirically for TB for 2 months and reassess", "Search for a primary head and neck malignancy (e.g., nasopharynx) and obtain tissue diagnosis",
          "Reassure and observe", "Start prednisolone", "Repeat the tuberculin skin test"], 1,
         "โน้ตในห้อง: **ก้อนที่คอ → คิดถึงมะเร็งเสมอ และต้องแยก primary หรือ secondary → ตรวจศีรษะและลำคอ**\n\nผู้ป่วยสูงอายุ สูบบุหรี่ ต่อม **แข็งและยึดติด** และ FNA ไม่พบ granuloma → ต้อง **หามะเร็งปฐมภูมิบริเวณศีรษะลำคอ** (เช่น nasopharyngoscopy) และได้เนื้อเยื่อยืนยัน\n\nการให้ยาวัณโรคเชิงประจักษ์โดยไม่มีหลักฐานทำให้มะเร็งถูกวินิจฉัยช้า",
         "ก้อนที่คอแข็งยึดติดในผู้สูงอายุ → หามะเร็งศีรษะลำคอก่อน", "Differential of cervical lymphadenopathy", ["สไลด์ อ.ภาณุวัฒน์ หน้า 3 (โน้ตในห้อง)"], NLN + ["2.1.57"]),
     mcq(N(18), "A woman with culture-confirmed, drug-susceptible TB lymphadenitis develops enlargement of the treated node and a new adjacent node 5 weeks into standard therapy. She is otherwise improving. What is the most appropriate management?",
         ["Switch to a second-line MDR-TB regimen", "Stop all drugs and re-culture",
          "Recognise a paradoxical reaction and continue the same regimen, aspirating the node if fluctuant",
          "Add routine long-term corticosteroid for the full treatment course", "Diagnose treatment failure and refer for surgery"], 2,
         "**Paradoxical reaction** พบบ่อยใน TB lymphadenitis — ต่อมโตขึ้นหรือมีต่อมใหม่ในช่วงแรกของการรักษา เพราะ **ภูมิคุ้มกันฟื้นตัวและตอบสนองต่อซากเชื้อ** ไม่ใช่เชื้อดื้อยา\n\nเมื่อ **เชื้อไวต่อยาและอาการโดยรวมดีขึ้น** → **ให้ยาเดิมต่อ** เจาะระบายหนองถ้านิ่ม\n\n**Steroid ไม่แนะนำเป็นกิจวัตรใน TB lymphadenitis** (สไลด์หน้า 14)",
         "LN โตขึ้นระหว่างรักษาเชื้อไวต่อยา = paradoxical reaction → ยาเดิมต่อ", "Paradoxical reaction", ["สไลด์ อ.ภาณุวัฒน์ หน้า 14"], NLN + ["2.1.57"]),
    ], NLN + ["2.1.57"])

# ───────────────────────────── 7
sec("chest-eptb-07", "Case 03 — วัณโรคกระดูกสันหลัง (Pott's disease)",
    "ปวดหลังเฉพาะจุดเป็นเดือน กดเจ็บ cold abscess → MRI → ผ่าตัดเมื่อมี cord compression หรือกระดูกไม่มั่นคง", 9,
"""### เคสจากสไลด์
| | |
|---|---|
| **อาการสำคัญ** | **ปวดหลังเฉพาะจุด แย่ลงเรื่อย ๆ เป็นเดือน** |
| **ประวัติ** | **กดเจ็บเฉพาะที่** มากขึ้น · ในผู้ป่วย HIV มักมี **cold abscess** (ฝีที่ไม่มีลักษณะร้อนแดงของการอักเสบเฉียบพลัน) |
| **ภาพ** | **MRI/CT: ตัวกระดูกสันหลังถูกทำลาย + รอยโรครอบกระดูกสันหลัง (paraspinal)** |
| **ประเมินระบบประสาท** | เฝ้าระวัง **การกดไขสันหลัง** และความผิดปกติทางระบบประสาทที่แย่ลง |
| **การวินิจฉัย** | **TB spondylitis (Pott's disease)** |

### กลไกและลักษณะภาพ
เชื้อมาทางกระแสเลือดไปฝังที่ **ส่วนหน้าของตัวกระดูกสันหลังใกล้ endplate** (มักเป็น **ทรวงอกส่วนล่างถึงเอวส่วนบน**) แล้วลามใต้ anterior longitudinal ligament ไปยังข้อถัดไป
| ลักษณะ | TB spondylitis | Pyogenic spondylodiscitis |
|---|---|---|
| ระยะเวลา | **ช้า เป็นเดือน** | เร็ว เป็นวันถึงสัปดาห์ |
| หมอนรองกระดูก | **ค่อนข้างคงอยู่ในระยะแรก** | ถูกทำลายเร็ว |
| ฝี | **paraspinal/psoas cold abscess ขนาดใหญ่** ผนังบางเรียบ | ฝีเล็กกว่า |
| ผลที่ตามมา | ตัวกระดูกยุบด้านหน้า → **หลังค่อมเป็นมุม (gibbus)** | — |

**การยืนยัน** — **CT-guided biopsy** ของกระดูกหรือฝี ส่งพยาธิวิทยา AFB NAAT และ culture

### การรักษา
- ยาวัณโรค **นานกว่าตำแหน่งอื่น** — สไลด์แสดงแถบ bone and spine ยาวราว **9–12 เดือน** (2IRZE ตามด้วย IR)
- **ไม่ให้ steroid เป็นกิจวัตร**
- **ข้อบ่งชี้ผ่าตัด (absolute)**
  1. **Cord compression ที่มีความผิดปกติทางระบบประสาท คงอยู่หรือกลับเป็นซ้ำแม้ได้ยาแล้ว**
  2. **กระดูกสันหลังไม่มั่นคง (spinal instability)**
""",
    ["Pott's: ปวดหลังเฉพาะจุดเป็นเดือน + กดเจ็บ + cold abscess",
     "MRI: ตัวกระดูกถูกทำลาย + paraspinal/psoas abscess · หมอนรองกระดูกคงอยู่ในระยะแรก",
     "ยืนยันด้วย CT-guided biopsy",
     "รักษานานกว่าตำแหน่งอื่น (ราว 9–12 เดือน) · ไม่ให้ steroid",
     "ผ่าตัดเมื่อ cord compression + neuro deficit คงอยู่/กลับเป็นซ้ำ หรือ spinal instability"],
    [mcq(N(19), "A 47-year-old man has 4 months of progressive thoracolumbar back pain with focal tenderness over T12, night sweats and weight loss. MRI shows destruction of the anterior T11–T12 vertebral bodies with a large bilateral paraspinal abscess extending into the psoas; the intervening disc is relatively preserved. What is the most likely diagnosis?",
         ["Osteoporotic compression fracture", "Pyogenic spondylodiscitis due to Staphylococcus aureus", "Tuberculous spondylitis (Pott's disease)", "Multiple myeloma", "Ankylosing spondylitis"], 2,
         "เคส 03 ในสไลด์ — **ปวดหลังเฉพาะจุดเป็นเดือน กดเจ็บ มีอาการทั่วตัว** และ MRI เป็น **การทำลายตัวกระดูกด้านหน้า + ฝี paraspinal/psoas ขนาดใหญ่ + หมอนรองกระดูกค่อนข้างคงอยู่**\n\nจุดแยกจาก **pyogenic spondylodiscitis** คือ **ดำเนินโรคช้า** และ **หมอนรองกระดูกถูกทำลายช้า** ส่วนฝีของวัณโรคเป็น **cold abscess** ขนาดใหญ่ ไม่มีลักษณะร้อนแดง\n\nขั้นต่อไป: **CT-guided biopsy** และตรวจระบบประสาทเป็นระยะ",
         "ปวดหลังเป็นเดือน + ทำลายตัวกระดูกด้านหน้า + psoas abscess = Pott's", "Diagnosis of spinal TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 3, 7"], NLN + ["2.3.13-3(9)", "B5.2.2-3(7)"]),
     mcq(N(20), "A patient with TB spondylitis on standard therapy for 6 weeks has persistent lower-limb weakness from cord compression that has not improved. Which is the most appropriate step?",
         ["Continue medical therapy alone for a further 6 months", "Add high-dose corticosteroid and avoid surgery",
          "Refer for urgent surgical decompression and stabilisation", "Switch to an MDR-TB regimen", "Stop anti-tuberculous drugs before surgery"], 2,
         "สไลด์หน้า 7 และ 15 — **ข้อบ่งชี้ผ่าตัดที่ชัดเจนของ TB spondylitis**\n1. **Cord compression ที่มีความผิดปกติทางระบบประสาทคงอยู่หรือกลับเป็นซ้ำแม้ได้ยา**\n2. **Spinal instability**\n\nผู้ป่วยรายนี้เข้าข้อ 1 → **ผ่าตัดลดการกดทับและยึดกระดูก** โดย **ให้ยาวัณโรคต่อ** ไม่หยุดยา\n\nSteroid ไม่แนะนำเป็นกิจวัตรใน bone/spine TB และไม่ใช่ทางเลือกแทนการผ่าตัด",
         "Pott's + neuro deficit ไม่ดีขึ้นแม้ได้ยา หรือ spinal instability → ผ่าตัด", "Surgery in spinal TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 7, 15"], NLN + ["2.3.13-3(9)"]),
    ], NLN + ["2.3.13-3(9)", "B5.2.2-3(7)"])

# ───────────────────────────── 8
sec("chest-eptb-08", "วัณโรคเยื่อหุ้มสมองและระบบประสาท (TB meningitis, tuberculoma)",
    "รูปแบบที่อันตรายที่สุดของ EPTB — CSF lymphocyte โปรตีนสูง น้ำตาลต่ำ · รักษา 12 เดือน · steroid เป็นข้อบ่งชี้ absolute", 10,
"""### ทำไมเป็นรูปแบบที่อันตรายที่สุด
เชื้อที่ฝังตัวใกล้ผิวสมองหรือเยื่อหุ้มสมอง (Rich focus) แตกเข้าช่อง subarachnoid → เกิด **exudate เหนียวข้นที่ฐานสมอง (basal meningitis)** ซึ่งก่อปัญหาสามอย่าง
| กลไก | ผลทางคลินิก |
|---|---|
| exudate หุ้มเส้นประสาทสมองที่ฐานสมอง | **cranial nerve palsy** โดยเฉพาะ **CN VI** |
| อุดทางไหลของน้ำไขสันหลัง | **hydrocephalus** → ซึมลง ความดันในกะโหลกสูง |
| หลอดเลือดที่ผ่าน exudate อักเสบ (vasculitis) | **สมองขาดเลือด** มักที่ basal ganglia และ internal capsule |

ร่วมกับ **hyponatremia จาก SIADH** ได้บ่อย

### ภาพทางคลินิก
**กึ่งเฉียบพลันเป็นสัปดาห์** — ไข้ต่ำ ปวดศีรษะ อาเจียน แล้วค่อย ๆ ซึมลง มี **คอแข็ง** และ **เส้นประสาทสมองผิดปกติ** ต่างจากแบคทีเรียที่เป็นเร็วเป็นชั่วโมงถึงวัน
**ข้อมูลในสไลด์** — ในผู้ป่วย HIV พบรอยโรคที่เยื่อหุ้มสมองและสมองได้บ่อย (OR 4.47) ส่วน **tuberculoma** คือก้อน granuloma ในเนื้อสมองที่อาจทำให้ชักหรือแขนขาอ่อนแรง

### CSF (ตารางที่อาจารย์ติดดาว ★★★)
| | TB meningitis |
|---|---|
| ลักษณะ | **ใสในระยะแรก ขุ่นเมื่อเรื้อรัง** (อาจมีใยคล้ายใยแมงมุมเมื่อตั้งทิ้งไว้) |
| Cell | **100–500** · **ระยะแรก PMN เด่น ต่อมา mononuclear ถึง 95%** |
| Protein | **สูง 100–500 mg/dL** |
| Glucose | **40–50 mg/dL (ราว 50% ของน้ำตาลในเลือด)** → ต้องเจาะน้ำตาลในเลือดพร้อมกันเสมอ |
| ADA | จุดตัด **ราว 20 U/L** แต่ผันแปรมาก |
| AFB smear / culture | **5–37% / 40–80%** → ส่งปริมาณมากและส่ง NAAT ร่วม |

### การรักษา
- **2IRZE ตามด้วย IR รวม 12 เดือน (2IRZE/10IR)** — สไลด์ระบุว่าเป็นกลุ่มที่ต้อง **รักษานานและติดตามใกล้ชิด**
- **Corticosteroid = ข้อบ่งชี้ absolute** — ลดการตาย **ราว 25%** (Cochrane review) และช่วยภาวะ **paradoxical worsening** หลังเริ่มยา โดยทั่วไปใช้ **dexamethasone** แล้วค่อย ๆ ลดขนาดใน 6–8 สัปดาห์
- ข้อมูลใหม่ที่ควรรู้: การศึกษา **ACT HIV (NEJM 2023)** พบว่า dexamethasone **ไม่ลดการตาย** ในผู้ป่วย TB meningitis ที่ติด HIV
- **ผู้ป่วย HIV** — ไม่เริ่ม ART ทันที ให้รอราว **4–8 สัปดาห์** หลังเริ่มยาวัณโรค เพราะ IRIS ในสมองอันตรายถึงชีวิต
- Hydrocephalus → ปรึกษาประสาทศัลยแพทย์เพื่อระบายน้ำไขสันหลัง
""",
    ["TBM = basal meningitis → CN VI palsy · hydrocephalus · vasculitic infarct · SIADH",
     "CSF: clear → turbid · cell 100–500 (PMN ระยะแรก → mononuclear) · protein 100–500 · glucose 40–50 (≈50%)",
     "รักษา 2IRZE/10IR รวม 12 เดือน",
     "Steroid ใน TBM = absolute indication · ลดตายราว 25%",
     "HIV + TBM → เลื่อน ART ราว 4–8 สัปดาห์ กัน IRIS"],
    [mcq(N(21), "A 36-year-old man has 3 weeks of headache, low-grade fever and increasing drowsiness, with a new right sixth cranial nerve palsy. CSF: opening pressure raised, clear fluid, WBC 280/µL (80% lymphocytes), protein 240 mg/dL, glucose 32 mg/dL (blood glucose 110 mg/dL). What is the most appropriate treatment?",
         ["Ceftriaxone and vancomycin for 14 days", "Intravenous acyclovir alone",
          "Anti-tuberculous therapy 2IRZE/10IR plus adjunctive dexamethasone",
          "Amphotericin B plus flucytosine", "Anti-tuberculous therapy 2IRZE/4IR without corticosteroid"], 2,
         "ภาพคลาสสิกของ **TB meningitis** — **กึ่งเฉียบพลันเป็นสัปดาห์ + CN VI palsy (basal meningitis)** และ CSF เข้าตารางในสไลด์: **cell 100–500 lymphocyte เด่น, protein 100–500 mg/dL, glucose ต่ำราว 30% ของเลือด**\n\n**การรักษา**: **2IRZE/10IR (12 เดือน)** + **corticosteroid ซึ่งเป็นข้อบ่งชี้ absolute** (ลดตายราว 25%)\n\nทำไมข้ออื่นผิด: สูตร 6 เดือนสั้นเกินไปสำหรับ CNS · ceftriaxone/vancomycin ใช้กับแบคทีเรีย · amphotericin ใช้กับ cryptococcus (ต้องส่ง India ink/CrAg ร่วมด้วยในผู้ป่วย HIV)",
         "TBM: 2IRZE/10IR + dexamethasone", "Treatment of TB meningitis", ["สไลด์ อ.ภาณุวัฒน์ หน้า 9, 12, 14"], NLN + ["2.3.6(5)", "B3.2.2(1)"]),
     mcq(N(22), "Which CSF finding is characteristic of early tuberculous meningitis and may mislead the clinician?",
         ["Xanthochromia", "A neutrophil-predominant pleocytosis that later shifts to mononuclear cells", "Normal protein", "Glucose higher than blood glucose", "Eosinophil count above 50%"], 1,
         "ตารางในสไลด์หน้า 9 — CSF ของวัณโรค **ระยะแรก PMN เด่น ต่อมาเปลี่ยนเป็น mononuclear ถึง 95%**\n\nถ้าเจาะเร็วจึงอาจ **หลอกว่าเป็น bacterial meningitis** ต้องดูบริบท (ดำเนินโรคช้า เส้นประสาทสมองผิดปกติ โปรตีนสูงมาก) และ **เจาะซ้ำ** ถ้ายังไม่ชัด\n\nลักษณะอื่น: ใสระยะแรก ขุ่นเมื่อเรื้อรัง · protein สูง · glucose ราว 50% ของเลือด",
         "CSF TB ระยะแรก PMN เด่นได้ แล้วเปลี่ยนเป็น mononuclear", "Early CSF in TBM", ["สไลด์ อ.ภาณุวัฒน์ หน้า 9"], NLN + ["2.3.6(5)", "B3.3(2)"]),
     mcq(N(23), "A patient with advanced HIV (CD4 25 cells/µL) not yet on antiretroviral therapy is diagnosed with tuberculous meningitis. When should ART generally be started?",
         ["Immediately, on the same day as anti-tuberculous therapy", "After about 4–8 weeks of anti-tuberculous therapy",
          "Only after completing 12 months of anti-tuberculous therapy", "Never, because rifampicin makes ART impossible", "Before starting anti-tuberculous therapy"], 1,
         "ใน **TB meningitis** การเริ่ม ART เร็วเพิ่มความเสี่ยง **IRIS ในสมอง** ซึ่งอันตรายถึงชีวิต แนวทางจึงแนะนำให้ **เลื่อน ART ไปราว 4–8 สัปดาห์** หลังเริ่มยาวัณโรค\n\nต่างจาก **วัณโรคตำแหน่งอื่นที่ CD4 < 50** ซึ่งแนะนำให้เริ่ม ART **ภายใน 2 สัปดาห์**\n\nสไลด์เน้นว่า **ผู้ป่วยวัณโรคทุกรายต้องตรวจ HIV เพราะมีผลกับการรักษา** — นี่คือตัวอย่างที่ชัดที่สุด",
         "TBM + HIV → เริ่ม ART หลังยาวัณโรคราว 4–8 สัปดาห์", "ART timing in TBM", ["สไลด์ อ.ภาณุวัฒน์ หน้า 4, 14"], NLN + ["2.3.1(9)", "2.3.6(5)"]),
    ], NLN + ["2.3.6(5)", "B3.2.2(1)", "B3.3(2)"])


# ───────────────────────────── 9
sec("chest-eptb-09", "วัณโรคเยื่อหุ้มหัวใจ (TB pericarditis)",
    "น้ำในเยื่อหุ้มหัวใจเรื้อรัง ADA > 40 เสี่ยง tamponade และ constriction · steroid เป็นข้อบ่งชี้แบบมีเงื่อนไข", 7,
"""### ภาพรวม
วัณโรคเป็น **สาเหตุสำคัญของน้ำในเยื่อหุ้มหัวใจปริมาณมากในประเทศที่วัณโรคชุก** เชื้อมักลามมาจาก **ต่อมน้ำเหลืองในช่องอกข้างหลอดลม** หรือมาทางกระแสเลือด
ข้อมูลในสไลด์หน้า 4 พบรอยโรคที่เยื่อหุ้มหัวใจ **71.4% ในผู้ป่วย HIV ลบ เทียบกับ 7.1% ในผู้ป่วย HIV บวก**

### ระยะของโรคและผลที่ตามมา
| ระยะ | สิ่งที่เกิด |
|---|---|
| **Effusive** | น้ำสีฟางหรือปนเลือด (serosanguinous) สะสมช้า ๆ → **cardiac tamponade** ได้ |
| **Effusive-constrictive** | น้ำยังอยู่ แต่เยื่อหุ้มเริ่มหนา |
| **Constrictive** | เยื่อหุ้มหนาเป็นพังผืดและหินปูน → **constrictive pericarditis** (JVP สูง Kussmaul sign บวมและท้องมาน) |

### สารน้ำ (ตารางสไลด์หน้า 9 ★)
- **straw colored หรือ serosanguinous**
- **lymphocyte เพิ่ม** · ระยะแรก PMN เด่น ต่อมา mononuclear
- **protein สูง · glucose ต่ำ** · ไม่พบเซลล์มะเร็ง
- **ADA ≥ 40–45 U/L** สนับสนุนวัณโรค และช่วยแยกจากมะเร็งที่เยื่อหุ้มหัวใจ

### การรักษา
- **2IRZE/4IR รวม 6 เดือน**
- **เจาะระบายน้ำ (pericardiocentesis)** เมื่อมี tamponade หรือเพื่อวินิจฉัย
- **Corticosteroid = ข้อบ่งชี้แบบมีเงื่อนไข (conditional)** — ช่วยลดการตาย และลดการต้องเจาะระบายหรือผ่าตัดลอกเยื่อหุ้มหัวใจ แนะนำ **เฉพาะผู้ป่วย HIV ลบ** (ESC 2015) หรือใช้เชิงประจักษ์
  - เหตุผลที่เลี่ยงในผู้ป่วย HIV: การศึกษา **IMPI (NEJM 2014)** พบว่า prednisolone **ลดการเกิด constriction** แต่ **ไม่ลดการตายโดยรวม** และ **เพิ่มมะเร็งที่สัมพันธ์กับ HIV**
- **Pericardiectomy** เมื่อ constriction ไม่ดีขึ้นหลังได้ยาวัณโรคไปแล้ว
""",
    ["TB pericarditis: effusive → effusive-constrictive → constrictive",
     "Pericardial fluid: serosanguinous · lymphocyte · protein สูง · ADA ≥ 40",
     "รักษา 6 เดือน (2IRZE/4IR)",
     "Steroid = conditional: เฉพาะ HIV ลบ (ESC 2015) · ลด constriction",
     "Constriction ที่ไม่ดีขึ้นหลังยา → pericardiectomy"],
    [mcq(N(24), "A 44-year-old HIV-negative man has a large pericardial effusion. Pericardiocentesis yields serosanguinous fluid with lymphocyte predominance, high protein, ADA 62 U/L and no malignant cells. He is started on 2IRZE/4IR. Regarding adjunctive corticosteroid, which statement best matches the lecture?",
         ["Contraindicated in all patients with TB pericarditis", "Absolute indication identical to TB meningitis",
          "Conditional indication: may be used in HIV-negative patients because it reduces constriction and the need for pericardiocentesis or pericardiectomy",
          "Required only if the patient is HIV-positive", "Should replace anti-tuberculous therapy"], 2,
         "สไลด์หน้า 14 จัด **TB pericarditis เป็น conditional indication** — steroid **สัมพันธ์กับการตายที่ลดลงและลดการต้องเจาะระบายหรือผ่าตัดลอกเยื่อหุ้มหัวใจ** แนะนำ **เฉพาะผู้ป่วย HIV ลบ (ESC 2015)** หรือใช้เชิงประจักษ์\n\nหลักฐานประกอบ: **IMPI (NEJM 2014)** — ลด constriction แต่ไม่ลดการตายโดยรวม และ **เพิ่มมะเร็งที่สัมพันธ์กับ HIV** จึงเลี่ยงในผู้ป่วย HIV\n\nเทียบ: **TB meningitis = absolute** · **LN, pleura, bone/spine, GU = not recommended**",
         "Steroid: meningitis = absolute · pericarditis = conditional (HIV ลบ) · ที่เหลือ = ไม่แนะนำ", "Corticosteroid in TB pericarditis", ["สไลด์ อ.ภาณุวัฒน์ หน้า 14", "MED ข้อสอบเก่า – pericardial fluid tuberculous vs malignant"], NLN + ["2.3.9-3(6)", "B7.2.2-3(3)", "B1.7.4"]),
    ], NLN + ["2.3.9-3(6)", "B7.2.2-3(3)"])

# ───────────────────────────── 10
sec("chest-eptb-10", "วัณโรคช่องท้องและระบบทางเดินปัสสาวะ",
    "เยื่อบุช่องท้อง: ท้องโต + ปวดทั่วท้อง · ลำไส้: ปวดท้องขวาล่าง 80–90% · ไต: sterile pyuria และผ่าตัดไตที่ไม่ทำงาน", 9,
"""### วัณโรคเยื่อบุช่องท้อง (TB peritonitis)
**อาการ** (สไลด์หน้า 3) — **ท้องโตร่วมกับปวดท้องทั่ว ๆ** ร่วมกับไข้ น้ำหนักลด อาจคลำได้หน้าท้องหนืดคล้ายแป้งนวด (doughy abdomen)

**น้ำในช่องท้อง**
| ค่า | TB peritonitis | เทียบกับ cirrhosis |
|---|---|---|
| **SAAG** | **< 1.1 g/dL** (ไม่ใช่ portal hypertension) | ≥ 1.1 g/dL |
| Protein | **สูง (มักมากกว่า 2.5–3 g/dL)** | ต่ำ |
| Cell | **lymphocyte เด่น** | PMN ต่ำถ้าไม่ติดเชื้อ |
| **ADA** | **> 36–40 U/L** → sens 100% / spec 97% (สไลด์หน้า 10) | ต่ำ |

**การยืนยัน** — AFB smear ของน้ำในช่องท้องแทบไม่เคยบวก การตรวจที่ให้ผลดีที่สุดคือ **ส่องกล้องช่องท้องตัดชิ้นเนื้อเยื่อบุช่องท้อง (laparoscopic peritoneal biopsy)** เห็นตุ่มเล็กขาวกระจายทั่ว และพยาธิวิทยาเป็น caseating granuloma
**ข้อควรระวัง** — ผู้ป่วยตับแข็งก็เป็น TB peritonitis ซ้อนได้ ทำให้ SAAG สูงหลอกได้

### วัณโรคลำไส้ (TB enteritis)
- **ปวดท้องขวาล่าง (RLQ) พบ 80–90%** เพราะตำแหน่งที่พบบ่อยที่สุดคือ **ileocecal region** — มีเนื้อเยื่อน้ำเหลืองมาก และเนื้อหาในลำไส้ค้างอยู่นาน
- ภาพ CT: **ผนัง terminal ileum และ cecum หนา + ต่อมน้ำเหลืองในช่องท้องโต**
- **การวินิจฉัยแยกโรคสำคัญคือ Crohn's disease** — ต้องได้ชิ้นเนื้อจากการส่องกล้องลำไส้ ส่งพยาธิวิทยา (granuloma มี caseation) AFB NAAT และ culture
- ภาวะแทรกซ้อน: ลำไส้ตีบ อุดตัน ทะลุ

### วัณโรคระบบทางเดินปัสสาวะและอวัยวะสืบพันธุ์ (GU TB)
- ในข้อมูลของสไลด์พบ **เฉพาะในผู้ป่วย HIV ลบ** — เป็นโรคของ reactivation ที่ใช้เวลานานหลายปี
- เบาะแสสำคัญ: **sterile pyuria** (มีเม็ดเลือดขาวในปัสสาวะแต่เพาะเชื้อธรรมดาไม่ขึ้น) และ **ปัสสาวะเป็นเลือด**
- ตรวจ **ปัสสาวะตอนเช้า 3 วันติดกัน** ส่ง AFB NAAT และ culture
- ระยะหลัง: ท่อไตตีบ ไตบวมน้ำ หินปูนในไต จนไตไม่ทำงาน ในชายอาจมี epididymitis ในหญิงอาจเป็นหมัน
- **รักษา 6 เดือน (2IRZE/4IR)** · **ไม่ให้ steroid**
- **ข้อบ่งชี้ผ่าตัดไตออก (nephrectomy)** (สไลด์หน้า 15) — **ไตที่ไม่ทำงานแล้ว** ร่วมกับ **ความดันโลหิตสูงที่คุมไม่ได้ หรือปวดสีข้างรุนแรงต่อเนื่อง**
""",
    ["TB peritonitis: ท้องโต + ปวดทั่วท้อง · SAAG < 1.1 · protein สูง · lymphocyte · ADA > 36–40",
     "ยืนยัน TB peritonitis ด้วย laparoscopic peritoneal biopsy",
     "TB enteritis: ปวด RLQ 80–90% · ileocecal · DDx Crohn",
     "GU TB: sterile pyuria + hematuria · ปัสสาวะเช้า 3 วัน",
     "Nephrectomy: ไตไม่ทำงาน + HT คุมไม่ได้ หรือปวดสีข้างรุนแรงต่อเนื่อง"],
    [mcq(N(25), "A 32-year-old woman has 2 months of abdominal distension, diffuse abdominal pain, evening fever and weight loss. Ascitic fluid: SAAG 0.6 g/dL, total protein 4.8 g/dL, WBC 1,100/µL (88% lymphocytes), ADA 58 U/L, cytology negative. What is the most likely diagnosis?",
         ["Cirrhotic ascites", "Spontaneous bacterial peritonitis", "Tuberculous peritonitis", "Nephrotic syndrome", "Congestive heart failure"], 2,
         "สไลด์หน้า 3 — **TB peritoneum: ท้องโตร่วมกับปวดทั่วท้อง**\n\nน้ำในช่องท้องเป็น **SAAG ต่ำ (< 1.1) = ไม่ใช่ portal hypertension** · **protein สูง** · **lymphocyte เด่น** · **ADA 58 > 36–40 U/L** (sens 100% / spec 97%) และไม่พบเซลล์มะเร็ง → **TB peritonitis**\n\nทำไมข้ออื่นผิด: cirrhosis และ heart failure มี SAAG สูง · SBP มี PMN เด่น · nephrotic syndrome มี SAAG ต่ำแต่ protein ต่ำ\n\nยืนยันด้วย **laparoscopic peritoneal biopsy**",
         "Ascites SAAG ต่ำ + protein สูง + lymphocyte + ADA > 36–40 = TB peritonitis", "TB peritonitis", ["สไลด์ อ.ภาณุวัฒน์ หน้า 3, 10", "MED34 MCQ ครั้งที่ 2 (GI ข้อ 2) – ascites low SAAG high protein → TB peritoneal"], NLN + ["2.1.12"]),
     mcq(N(26), "A 40-year-old man has 3 months of right lower quadrant pain, fever and weight loss. CT shows thickening of the terminal ileum and caecum with enlarged mesenteric lymph nodes. Colonoscopic ileal biopsy shows caseating granulomas. What is the diagnosis and the key differential that the biopsy has helped exclude?",
         ["Acute appendicitis; mesenteric adenitis", "Intestinal tuberculosis; Crohn's disease", "Amoebic colitis; ulcerative colitis", "Colon cancer; diverticulitis", "Typhoid fever; yersiniosis"], 1,
         "สไลด์หน้า 3 — **TB enteritis: ปวดท้องขวาล่าง 80–90%** เพราะรอยโรคอยู่ที่ **ileocecal region** เป็นหลัก\n\n**Caseating granuloma** ชี้ว่าเป็นวัณโรค และช่วยแยกจาก **Crohn's disease** ซึ่งให้ภาพ ileocecal thickening เหมือนกันแต่ granuloma **ไม่มี caseation** — การแยกนี้สำคัญมาก เพราะถ้าให้ steroid หรือยากดภูมิแก่ผู้ป่วยวัณโรคที่ถูกวินิจฉัยผิดว่าเป็น Crohn's โรคจะลุกลาม",
         "Ileocecal thickening + caseating granuloma = intestinal TB (แยกจาก Crohn)", "Intestinal TB vs Crohn", ["สไลด์ อ.ภาณุวัฒน์ หน้า 3", "MED35 ลงกองครั้งที่ 2 MCQ ข้อ 53 – ตัด ileum biopsy เจอ granulomatous inflammation → TB", "MED34 MCQ ครั้งที่ 4 ข้อ 76 – Terminal ileum thickening + lymphadenopathy → TB"], NLN + ["2.1.11"]),
     mcq(N(27), "A 52-year-old man with a history of treated pulmonary TB has recurrent dysuria and microscopic haematuria. Urinalysis repeatedly shows pyuria, but routine urine cultures are negative. Which test is most appropriate next?",
         ["Repeat routine urine culture", "Three consecutive early-morning urine samples for AFB, NAAT and mycobacterial culture",
          "Serum ADA", "Prostate-specific antigen", "Empirical 3-day ciprofloxacin"], 1,
         "**Sterile pyuria** (มีเม็ดเลือดขาวในปัสสาวะแต่เพาะเชื้อธรรมดาไม่ขึ้น) + ปัสสาวะเป็นเลือด ในผู้ที่เคยเป็นวัณโรค → คิดถึง **GU TB**\n\nตรวจ **ปัสสาวะตอนเช้า 3 วันติดกัน** ส่ง AFB NAAT และ culture เพราะเชื้อออกมาในปัสสาวะเป็นช่วง ๆ และจำนวนน้อย\n\nสไลด์หน้า 4 พบ GU TB **เฉพาะในผู้ป่วย HIV ลบ** — เป็น reactivation ที่ใช้เวลานาน",
         "Sterile pyuria + hematuria → คิด GU TB → urine AFB/culture เช้า 3 วัน", "Genitourinary TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 4, 15"], NLN + ["2.1.43"]),
     mcq(N(28), "In genitourinary tuberculosis, which situation is an indication for nephrectomy according to the lecture?",
         ["Any positive urine mycobacterial culture", "Sterile pyuria at diagnosis",
          "A non-functioning kidney associated with intractable hypertension or continuous severe flank pain",
          "Bilateral renal involvement with normal function", "Drug-susceptible disease responding to therapy"], 2,
         "สไลด์หน้า 15 — **nephrectomy ทำเมื่อไตไม่ทำงานแล้ว (non-functioning kidney)** และต้อง **มีความดันโลหิตสูงที่คุมไม่ได้ หรือปวดสีข้างรุนแรงต่อเนื่อง** ร่วมด้วย\n\nกลไกของความดันสูง: ไตที่ขาดเลือดจากพังผืดหลั่ง **renin** มากเกิน\n\nข้อบ่งชี้ผ่าตัดโดยรวม: **ไม่ตอบสนองต่อยา หรือยังมีการติดเชื้อที่ทำลายเนื้อเยื่ออยู่**",
         "GU TB: ผ่าตัดไตเมื่อไม่ทำงาน + HT คุมไม่ได้/ปวดสีข้างต่อเนื่อง", "Surgery in GU TB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 15"]),
    ], NLN + ["2.1.12", "2.1.11", "2.1.43"])

# ───────────────────────────── 11
sec("chest-eptb-11", "สรุปการรักษา: ระยะเวลา steroid และการผ่าตัด",
    "ส่วนใหญ่ 6 เดือน · กระดูกสันหลังนานขึ้น · สมอง 12 เดือน · steroid แบ่งสามระดับ · ผ่าตัดเมื่อยาไม่พอ", 8,
"""### สูตรมาตรฐาน (แนวทางวัณโรคประเทศไทย 2561)
| ระยะ | ยา | เป้าหมาย |
|---|---|---|
| **Initial phase 2 เดือน** | **I**soniazid · **R**ifampicin · **Z** (pyrazinamide) · **E**thambutol | **ฆ่าเชื้อให้มากที่สุดและหยุดการแพร่** |
| **Continuation phase ≥ 4 เดือน** | **I**soniazid · **R**ifampicin | **ป้องกันการกลับเป็นซ้ำ** |

### ระยะเวลาตามอวัยวะ
| อวัยวะ | ระยะเวลา |
|---|---|
| **ต่อมน้ำเหลือง · เยื่อหุ้มปอด · เยื่อหุ้มหัวใจ · ทางเดินปัสสาวะ** | **6 เดือน — 2IRZE/4IR** |
| **กระดูกและกระดูกสันหลัง** | **นานขึ้น ราว 9–12 เดือน** |
| **เยื่อหุ้มสมองและสมอง (tuberculoma)** | **12 เดือน — 2IRZE/10IR** รักษานานและติดตามใกล้ชิด |

**หลักจำ** — อวัยวะที่ **ยาเข้าได้ยาก** (กระดูก สมองที่ผ่าน blood–brain barrier) หรือที่ **ผลเสียจากการกลับเป็นซ้ำร้ายแรง** จะรักษานานขึ้น

### Corticosteroid สามระดับ (สไลด์หน้า 14)
| ระดับ | ตำแหน่ง | เหตุผล |
|---|---|---|
| **Absolute** | **TB meningitis** | **ลดการตายราว 25%** (Cochrane) · ช่วย paradoxical worsening |
| **Conditional** | **TB pericarditis** | ลดการตาย ลดการเจาะระบายและผ่าตัด · **เฉพาะ HIV ลบ (ESC 2015)** หรือเชิงประจักษ์ |
| **Not recommended** | **LN · pleura · bone/spine · GU** | ไม่มีประโยชน์ชัดเจน · เพิ่มผลข้างเคียง |

**ข้อควรรู้** — rifampicin **เหนี่ยวนำเอนไซม์ตับ** ทำให้ระดับ steroid ในเลือดลดลง ขนาดยาที่ใช้ร่วมกับยาวัณโรคจึงสูงกว่าปกติ

### ผ่าตัดเมื่อไร (สไลด์หน้า 15)
**หลักใหญ่** — **ไม่ตอบสนองต่อยา หรือยังมีการติดเชื้อที่ทำลายเนื้อเยื่ออยู่**
| ตำแหน่ง | ข้อบ่งชี้ |
|---|---|
| **TB spondylitis** | cord compression + neuro deficit **คงอยู่หรือกลับเป็นซ้ำแม้ได้ยา** · **spinal instability** |
| **TB kidney** | **ไตไม่ทำงาน** + **HT คุมไม่ได้** หรือ **ปวดสีข้างรุนแรงต่อเนื่อง** → nephrectomy |
| (เพิ่มเติม) TB pericarditis | constriction ที่ไม่ดีขึ้นหลังได้ยา → pericardiectomy |
""",
    ["LN · pleura · pericardium · GU = 6 เดือน (2IRZE/4IR)",
     "Bone/spine ราว 9–12 เดือน · CNS 12 เดือน (2IRZE/10IR)",
     "Steroid: meningitis absolute · pericarditis conditional · LN/pleura/bone/GU ไม่แนะนำ",
     "ผ่าตัดเมื่อยาไม่พอ: Pott's + neuro deficit/instability · ไตไม่ทำงาน + HT/ปวด"],
    [mcq(N(29), "Which extrapulmonary TB site requires the longest standard duration of treatment according to the Thai guideline shown in the lecture?",
         ["Cervical lymph node", "Pleura", "Pericardium", "Meninges and brain (tuberculoma)", "Genitourinary tract"], 3,
         "สไลด์หน้า 12 — **LN, pleura, pericardium, GU = 6 เดือน (2IRZE/4IR)** · **bone and spine นานขึ้น** · **meningitis และ CNS (tuberculoma) = รักษานานที่สุดและต้องติดตามใกล้ชิด** โดยใช้ **2IRZE/10IR รวม 12 เดือน**\n\nเหตุผล: ยาหลายตัวผ่าน blood–brain barrier ได้จำกัด โดยเฉพาะเมื่อการอักเสบลดลง และผลเสียจากการกลับเป็นซ้ำในสมองร้ายแรงมาก",
         "CNS TB = 12 เดือน (2IRZE/10IR) — นานที่สุด", "Duration by organ", ["สไลด์ อ.ภาณุวัฒน์ หน้า 12"]),
     mcq(N(30), "For which form of tuberculosis is adjunctive corticosteroid NOT recommended as routine therapy?",
         ["Tuberculous meningitis", "Tuberculous pericarditis in an HIV-negative patient", "Tuberculous pleuritis", "Tuberculous meningitis with paradoxical worsening", "None; corticosteroid is recommended for all EPTB"], 2,
         "สไลด์หน้า 14 แบ่ง steroid เป็นสามระดับ\n- **Absolute — TB meningitis** (ลดตายราว 25%)\n- **Conditional — TB pericarditis** (HIV ลบ)\n- **Not recommended — TB lymphadenitis, TB pleura, TB bone/spine, GU TB**\n\nTB pleuritis จึงไม่ควรได้ steroid เป็นกิจวัตร แม้จะมีน้ำมากก็ตาม",
         "ไม่ให้ steroid: LN · pleura · bone/spine · GU", "Corticosteroid indications", ["สไลด์ อ.ภาณุวัฒน์ หน้า 14"], NLN + ["B1.7.4"]),
    ], NLN + ["B1.7.4"])

# ───────────────────────────── 12
sec("chest-eptb-12", "พิษของยาแนวแรก และการตัดวงจรการแพร่เชื้อ",
    "แผนที่พิษยาทีละอวัยวะ · มาตรการสามชั้น administrative–environmental–personal · การตามผู้สัมผัส", 8,
"""### แผนที่พิษของยาแนวแรก (สไลด์หน้า 13)
| อวัยวะ | ยา | พิษ |
|---|---|---|
| **ตา** | **E — ethambutol** | **optic neuropathy** — ตามัว เห็นสีผิด (แดง–เขียว) อาจสูญเสียการมองเห็นถาวร |
| **หู** | **S — streptomycin** | **ototoxicity** — หูหนวก เวียนศีรษะ ตากระตุก |
| **ตับ** | **H, R, Z** | **ตับอักเสบรุนแรง** — ทั้งสามตัวเป็นพิษต่อตับ · **R ทำให้ bilirubin (TB/DB) สูงแบบ cholestatic** · **Z ทำให้กรดยูริกสูงและปวดข้อ** |
| **ไต** | **S — streptomycin** | ปัสสาวะออกน้อย **ไตวายเฉียบพลัน** |
| **ระบบเลือดและทั่วร่างกาย** | **R — rifampicin** | **จ้ำเลือด เกล็ดเลือดต่ำ ช็อกเฉียบพลัน อาการคล้ายไข้หวัดใหญ่รุนแรง** (มักเกิดเมื่อกินยาไม่สม่ำเสมอหรือกลับมากินใหม่) |
| **เส้นประสาท** | **H — isoniazid** | **peripheral neuropathy** → ป้องกันและรักษาด้วย **pyridoxine (vitamin B6) 50–100 มก./วัน** |

รายละเอียดการจัดการตับอักเสบจากยา (เกณฑ์หยุดยาและการกลับมาให้ยาทีละตัว) อยู่ในคาบ **03 Pulmonary tuberculosis**

### ตัดวงจรการแพร่เชื้อ (แนวทางควบคุมวัณโรคประเทศไทย 2554)
| ชั้น | มาตรการ |
|---|---|
| **1. Administrative** | จัดระบบบริการและ **แยกผู้ป่วย** · ผู้ป่วยหยุดงานหรือแยกตัว **อย่างน้อย 2 สัปดาห์ หรือจนเพาะเชื้อเป็นลบ** (โดยเฉพาะเชื้อดื้อยา) |
| **2. Environmental** | **จัดการระบายอากาศ** ในพื้นที่ให้บริการอย่างเข้มงวด |
| **3. Personal** | ป้องกันทางเดินหายใจด้วย **หน้ากาก N95 หรือหน้ากากอนามัย** |

**EPTB แพร่เชื้อหรือไม่** — EPTB **ที่ไม่มีรอยโรคที่ปอดหรือกล่องเสียง โดยทั่วไปไม่แพร่ทางอากาศ** จึงไม่ต้องแยกห้องแบบ airborne หลังจาก **ตัดวัณโรคปอดด้วย CXR และเสมหะแล้ว** ข้อยกเว้นคือแผลที่มีหนองไหลหรือหัตถการที่ทำให้เกิดละอองจากรอยโรค

### การตามผู้สัมผัสใกล้ชิด
- คัดกรองด้วย **TST (≥ 10 มม. = บวก)** หรือ **IGRA**
- ตรวจคัดกรอง **ทุก 6 เดือนเป็นเวลา 2 ปี แล้วปีละครั้ง**

### บทสรุปของอาจารย์
**EPTB คือเชื้อที่เปลี่ยนรูปได้และมีจำนวนน้อย (shape-shifting, paucibacillary)** การเอาชนะต้องอาศัย
1. **ความสงสัยทางคลินิกสูง**
2. **การวินิจฉัยหลายวิธีร่วมกัน (NAAT และ culture)**
3. **การรักษาที่ยาวขึ้นและเฉพาะตามอวัยวะ**
""",
    ["E → ตา (optic neuropathy) · S → หูและไต · H/R/Z → ตับ",
     "R → จ้ำเลือด เกล็ดเลือดต่ำ ช็อก flu-like · Z → กรดยูริกสูง",
     "H → peripheral neuropathy → pyridoxine 50–100 มก./วัน",
     "แยกตัว ≥ 2 สัปดาห์หรือจน culture ลบ · ระบายอากาศ · N95",
     "ผู้สัมผัส: TST ≥ 10 มม. หรือ IGRA ทุก 6 เดือน × 2 ปี แล้วปีละครั้ง",
     "EPTB ล้วนที่ตัดวัณโรคปอดแล้ว โดยทั่วไปไม่ต้องแยกห้องแบบ airborne"],
    [mcq(N(31), "A patient on 2IRZE for TB lymphadenitis develops purpura, thrombocytopenia and hypotension shortly after restarting his medication following a 2-week interruption. Which drug is most likely responsible?",
         ["Isoniazid", "Rifampicin", "Pyrazinamide", "Ethambutol", "Pyridoxine"], 1,
         "สไลด์หน้า 13 — **Rifampicin: purpura, thrombocytopenia, acute shock, severe flu-like syndrome**\n\nกลไกเป็น **ปฏิกิริยาทางภูมิคุ้มกัน (แอนติบอดีต่อ rifampicin)** ซึ่งมักเกิด **เมื่อกินยาไม่สม่ำเสมอหรือกลับมากินใหม่หลังหยุดไป** → ต้อง **หยุด rifampicin ถาวร**\n\nเทียบ: E → ตา · S → หูและไต · H → เส้นประสาทส่วนปลาย · H/R/Z → ตับ",
         "R: จ้ำเลือด เกล็ดเลือดต่ำ ช็อก flu-like — มักเกิดเมื่อกินยาไม่สม่ำเสมอ", "Rifampicin hypersensitivity", ["สไลด์ อ.ภาณุวัฒน์ หน้า 13"]),
     mcq(N(32), "A 50-year-old man with diabetes and tuberculous pleuritis is starting 2IRZE/4IR. Which supplement should be given to prevent a nerve toxicity of this regimen?",
         ["Folic acid 5 mg/day", "Pyridoxine 50–100 mg/day", "Vitamin B12 injection monthly", "Thiamine 100 mg/day", "Vitamin D 1,000 IU/day"], 1,
         "สไลด์หน้า 13 — **Isoniazid → peripheral neuropathy** รักษาและป้องกันด้วย **pyridoxine 50–100 มก./วัน**\n\nกลไก: isoniazid จับกับ pyridoxine และเพิ่มการขับออก ทำให้ขาด vitamin B6 ซึ่งจำเป็นต่อการทำงานของเส้นประสาท กลุ่มเสี่ยง ได้แก่ **เบาหวาน สุรา ทุพโภชนาการ ไตวาย HIV และหญิงตั้งครรภ์**",
         "H → neuropathy → pyridoxine 50–100 มก./วัน", "Isoniazid neuropathy", ["สไลด์ อ.ภาณุวัฒน์ หน้า 13", "MED ข้อสอบเก่า – ยาวัณโรคตัวไหนทำให้ peripheral neuropathy"]),
     mcq(N(33), "A 30-year-old woman is diagnosed with tuberculous cervical lymphadenitis. Chest radiograph is normal and three sputum samples are negative by smear and Xpert. She asks whether she must be admitted to an isolation room. What is the most appropriate advice?",
         ["She must be admitted to a negative-pressure room for 2 months", "She must wear an N95 respirator at home for 6 months",
          "She does not need airborne isolation, because extrapulmonary TB without pulmonary or laryngeal involvement is generally not transmissible by air",
          "She should stop working for 12 months", "All household contacts must start 2IRZE"], 2,
         "EPTB ที่ **ไม่มีรอยโรคที่ปอดหรือกล่องเสียง** โดยทั่วไป **ไม่แพร่ทางอากาศ** เพราะเชื้อไม่ได้ถูกไอออกมาเป็นละออง เมื่อ **ตัดวัณโรคปอดด้วย CXR และเสมหะแล้ว** จึงไม่ต้องแยกห้องแบบ airborne ดูแลแบบผู้ป่วยนอกได้\n\nมาตรการสามชั้นในสไลด์หน้า 16 (แยกตัว ≥ 2 สัปดาห์ ระบายอากาศ N95) ใช้กับผู้ป่วย **ที่แพร่เชื้อได้** คือวัณโรคปอดหรือกล่องเสียง\n\nผู้สัมผัสในบ้านยังควรได้รับการคัดกรองตามแนวทาง แต่ **ไม่ได้ให้ยาสูตรรักษาโรคทุกคน**",
         "EPTB ล้วนที่ตัดวัณโรคปอดแล้ว → ไม่ต้องแยกห้อง airborne", "Infection control in EPTB", ["สไลด์ อ.ภาณุวัฒน์ หน้า 16", "MED32 MCQ ข้อ 32 – ให้อาการ extrapulmonary TB ทำยังไงดี (ไม่ต้อง admit, admit ห้องแยก, face mask)"]),
    ], NLN + ["B1.5.1(3)"])


LECNAME = "Extrapulmonary tuberculosis (อ.ภาณุวัฒน์)"
MEQ = [{"id": "CH-MEQ-EP-01", "part": "MEQ", "lec": "23/9", "lecture": LECNAME,
 "topic": "Tuberculous peritonitis in a patient newly found to have HIV — diagnosis, treatment and ART timing",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 34 ปี อาชีพพนักงานโรงงาน มาโรงพยาบาลด้วยอาการท้องโตขึ้นเรื่อย ๆ 6 สัปดาห์
PI: 2 เดือนก่อนมาโรงพยาบาล มีไข้ต่ำ ๆ ตอนเย็น เหงื่อออกกลางคืน เบื่ออาหาร น้ำหนักลด 7 กิโลกรัม 6 สัปดาห์ก่อนสังเกตว่าท้องโตขึ้น ปวดท้องตื้อ ๆ ทั่วท้อง ไม่มีตัวเหลือง ไม่มีขาบวม ไม่มีไอ
U/D: ไม่มีโรคประจำตัว ไม่ดื่มสุรา ไม่เคยตรวจ HIV
PE: V/S: BT 37.9 C, PR 96/min, BP 112/70 mmHg, RR 18/min
GA: ผอม ไม่ซีด ไม่เหลือง · ไม่มี spider nevi ไม่มี palmar erythema
Abdomen: distended, shifting dullness positive, diffuse mild tenderness, doughy feeling, ไม่คลำได้ตับม้าม
Lymph node: ไม่โต · Lungs: clear
Lab: CBC Hb 10.8 g/dL, WBC 6,200 /mm3 (L 18%), Plt 310,000 /mm3 · albumin 2.9 g/dL · LFT ปกติ · Anti-HIV positive, CD4 180 cells/µL""",
 "questions": [
  {"q": "1. จงบอกการตรวจน้ำในช่องท้องที่ต้องส่ง และผลที่คาดว่าจะพบถ้าเป็นโรคที่สงสัยมากที่สุด (4 คะแนน)",
   "a": """**การวินิจฉัยที่สงสัยมากที่สุด: tuberculous peritonitis** — ไข้ต่ำเรื้อรัง เหงื่อออกกลางคืน น้ำหนักลด **ท้องโตร่วมกับปวดทั่วท้อง** (สไลด์หน้า 3) หน้าท้องหนืด ไม่มีลักษณะตับแข็ง และมี **HIV** เป็นปัจจัยเสี่ยง

**ส่งตรวจน้ำในช่องท้อง (diagnostic paracentesis)**
| การตรวจ | ผลที่คาดใน TB peritonitis |
|---|---|
| ลักษณะ | ใสสีฟาง อาจขุ่นเล็กน้อย |
| **Albumin ในน้ำ → คำนวณ SAAG** | **SAAG < 1.1 g/dL** (ไม่ใช่ portal hypertension) |
| **Total protein** | **สูง (มากกว่า 2.5–3 g/dL)** |
| **Cell count และ differential** | เม็ดเลือดขาวราว 500–2,000 **lymphocyte เด่น** |
| **ADA** | **> 36–40 U/L** (sens 100% / spec 97%) |
| Glucose, LDH | glucose ต่ำกว่าเลือด LDH สูง |
| **AFB smear, Xpert MTB/RIF, mycobacterial culture** | smear แทบไม่บวก · culture ให้ผลบวกมากกว่า |
| **Cytology** | ไม่พบเซลล์มะเร็ง (แยก peritoneal carcinomatosis) |
| Gram stain และ culture ธรรมดา | ลบ |"""},
  {"q": "2. ผลน้ำในช่องท้อง: SAAG 0.7, protein 4.6 g/dL, WBC 1,200 (lymphocyte 90%), ADA 64 U/L, AFB smear negative, Xpert negative, cytology negative — จะวินิจฉัยอย่างไร และถ้าต้องการยืนยันด้วยเนื้อเยื่อ ควรทำหัตถการใด (3 คะแนน)",
   "a": """**การวินิจฉัย: tuberculous peritonitis** — **SAAG ต่ำ + protein สูง + lymphocyte เด่น + ADA 64 > 36–40 U/L** และไม่พบเซลล์มะเร็ง

**AFB smear และ Xpert เป็นลบไม่ได้ตัดโรค** เพราะ EPTB เป็น **paucibacillary** (สไลด์หน้า 8 และ 11)

**การยืนยันด้วยเนื้อเยื่อ: laparoscopy with peritoneal biopsy** — เห็นตุ่มขาวเล็กกระจายบนเยื่อบุช่องท้อง พยาธิวิทยาเป็น **caseating granuloma** และส่ง AFB NAAT culture จากชิ้นเนื้อ ในบริบทที่ ADA สูงชัดเจนและตัดมะเร็งได้ สามารถ **เริ่มยาวัณโรคได้เลย** ระหว่างรอผล culture"""},
  {"q": "3. จงเขียนสูตรยาและระยะเวลาการรักษา พร้อมระบุยาเสริมที่ควรให้ (3 คะแนน)",
   "a": """**สูตรยา: 2IRZE/4IR** (สไลด์หน้า 12 — วัณโรคช่องท้องใช้ระยะเวลามาตรฐาน 6 เดือน)
- **Initial phase 2 เดือน**: isoniazid + rifampicin + pyrazinamide + ethambutol — ฆ่าเชื้อและหยุดการแพร่
- **Continuation phase 4 เดือน**: isoniazid + rifampicin — กันการกลับเป็นซ้ำ
- **ยาเสริม: pyridoxine 50–100 มก./วัน** ป้องกัน peripheral neuropathy จาก isoniazid (ผู้ป่วย HIV และทุพโภชนาการเป็นกลุ่มเสี่ยง)
- **Co-trimoxazole prophylaxis** เพราะเป็นผู้ป่วย HIV ที่มีวัณโรค
- **ไม่ให้ corticosteroid เป็นกิจวัตร**
- ติดตาม **LFT** (H, R, Z เป็นพิษต่อตับ) และ **สายตา** (ethambutol)"""},
  {"q": "4. ผู้ป่วยรายนี้ควรเริ่มยาต้านไวรัส (ART) เมื่อใด และต้องระวังอะไร (3 คะแนน)",
   "a": """**เริ่ม ART ภายในราว 2–8 สัปดาห์หลังเริ่มยาวัณโรค** — CD4 180 ไม่ต่ำกว่า 50 จึงเริ่มได้ภายใน 8 สัปดาห์ (ถ้า CD4 < 50 ให้เริ่มภายใน 2 สัปดาห์) · **ไม่ใช่วัณโรคเยื่อหุ้มสมอง** จึงไม่ต้องเลื่อนนานเป็นพิเศษ

**ข้อควรระวัง**
- **ยาตีกัน** — rifampicin เหนี่ยวนำเอนไซม์ตับ ลดระดับยาต้านไวรัสหลายตัว เช่น **dolutegravir ต้องเพิ่มเป็นวันละสองครั้ง** และห้ามใช้ร่วมกับ protease inhibitor ส่วนใหญ่
- **IRIS** — หลังเริ่ม ART อาจมีไข้ ต่อมน้ำเหลืองโต หรือน้ำในช่องท้องเพิ่มขึ้นชั่วคราว ไม่ได้แปลว่ายาล้มเหลว
- **พิษต่อตับซ้อนกัน** ระหว่างยาวัณโรคกับยาต้านไวรัส"""},
  {"q": "5. ญาติถามว่าผู้ป่วยต้องแยกห้องหรือไม่ และคนในบ้านต้องทำอย่างไร จงตอบ (2 คะแนน)",
   "a": """- **ต้องตัดวัณโรคปอดก่อน** ด้วย **CXR และเสมหะ AFB/Xpert** — ถ้าไม่มีรอยโรคที่ปอดหรือกล่องเสียง **วัณโรคช่องท้องโดยทั่วไปไม่แพร่ทางอากาศ** ไม่ต้องแยกห้องแบบ airborne
- ถ้าพบวัณโรคปอดร่วมด้วย → มาตรการสามชั้น: **แยกตัวอย่างน้อย 2 สัปดาห์หรือจน culture ลบ · ระบายอากาศ · N95/หน้ากากอนามัย**
- **ผู้สัมผัสใกล้ชิด** คัดกรองด้วย **TST (≥ 10 มม.) หรือ IGRA** และอาการ ตรวจ **ทุก 6 เดือนเป็นเวลา 2 ปี แล้วปีละครั้ง** (สไลด์หน้า 16)"""}],
 "ref": ["สไลด์ อ.ภาณุวัฒน์ หน้า 3, 8, 10–13, 16", "MED34 ข้อสอบ MED ครั้งที่ 2 MCQ (GI ข้อ 2) – ascites low SAAG high protein → TB peritoneal"],
 "nl": ["2.3.1(20)", "2.1.12", "2.3.1(9)", "3.3.15", "B6.2.2(8)"], "years": ["34"], "_kind": "meq", "_set": "chest"}]

OSCE = [{"id": "CH-OSCE-EP-01", "part": "OSCE/SAQ", "lec": "23/9", "lecture": LECNAME,
 "topic": "SAQ – Body fluid interpretation in extrapulmonary TB (pleural, CSF, ascites)",
 "station": "SAQ (เขียนตอบ) 5 นาที",
 "instruction": """จงแปลผลสารน้ำจากผู้ป่วย 3 รายต่อไปนี้

**ผู้ป่วย A** — ชายอายุ 28 ปี ไข้ต่ำ เจ็บหน้าอกซ้ายเวลาหายใจ 4 สัปดาห์ · pleural fluid: straw colored, WBC 2,600 (lymphocyte 88%, eosinophil 1%), mesothelial cell rare, protein 5.0 g/dL (serum 7.2), LDH 520 (serum 260; ULN 250), glucose ต่ำกว่า serum, ADA 71 U/L, cytology negative

**ผู้ป่วย B** — หญิงอายุ 41 ปี ปวดศีรษะ ไข้ 3 สัปดาห์ ซึมลง ตาเข (CN VI palsy) · CSF: clear, WBC 240 (mononuclear 85%), protein 260 mg/dL, glucose 34 mg/dL (blood 118)

**ผู้ป่วย C** — ชายอายุ 60 ปี ติดสุรา ตาเหลือง ท้องมาน · ascitic fluid: SAAG 1.9 g/dL, protein 1.0 g/dL, WBC 180 (PMN 20%), ADA 8 U/L

จงตอบ
1. ผู้ป่วย A — จำแนกตาม Light's criteria และการวินิจฉัยที่น่าจะเป็นที่สุด (3 คะแนน)
2. ผู้ป่วย B — การวินิจฉัยที่น่าจะเป็นที่สุด และการรักษาที่ต้องให้ร่วมกับยาวัณโรค (3 คะแนน)
3. ผู้ป่วย C — เป็นวัณโรคเยื่อบุช่องท้องหรือไม่ เพราะอะไร (2 คะแนน)
4. ระบุภาวะที่ทำให้ ADA ในน้ำเยื่อหุ้มปอดสูงได้โดยไม่ใช่วัณโรค อย่างน้อย 3 ภาวะ (2 คะแนน)""",
 "answer": """**1. ผู้ป่วย A**
| เกณฑ์ Light | คำนวณ | ผล |
|---|---|---|
| protein ratio > 0.5 | 5.0/7.2 = **0.69** | ✔ |
| LDH ratio > 0.6 | 520/260 = **2.0** | ✔ |
| LDH > 2/3 ULN | 520 > 167 | ✔ |
→ **Exudate** · **lymphocyte เด่น + eosinophil < 5% + mesothelial น้อย + ADA 71 > 40** → **Tuberculous pleuritis**
(ตารางแนวทางไทย 2561: straw colored · cell 1,000–5,000 · lymphocyte 50–90% · protein > 2.5 · glucose < serum)

**2. ผู้ป่วย B — Tuberculous meningitis**
- กึ่งเฉียบพลัน + **CN VI palsy (basal meningitis)** · CSF **cell 100–500 mononuclear เด่น · protein 100–500 mg/dL · glucose ราว 30% ของเลือด**
- รักษา **2IRZE/10IR (12 เดือน)** + **dexamethasone** (absolute indication ลดตายราว 25%)
- ส่งเพิ่ม: CSF Xpert, AFB culture, cryptococcal antigen · ตรวจ HIV · CT/MRI หา hydrocephalus

**3. ผู้ป่วย C — ไม่ใช่วัณโรคเยื่อบุช่องท้อง**
- **SAAG 1.9 ≥ 1.1 = portal hypertension** จากตับแข็ง · **protein ต่ำ** · **ADA 8** ต่ำกว่าจุดตัด 36–40 U/L · PMN 36 เซลล์ ไม่ถึงเกณฑ์ SBP (≥ 250)

**4. ADA สูงโดยไม่ใช่วัณโรค** (สไลด์หน้า 10)
**empyema · lymphoma · malignant pleural effusion · parapneumonic effusion · collagen vascular disease (เช่น rheumatoid, SLE)**

**ข้อที่ทำให้เสียคะแนน**: บอกว่า AFB smear ลบจึงไม่ใช่วัณโรค · ให้สูตร 6 เดือนกับ TB meningitis · ลืม steroid ใน TB meningitis · อ่าน ADA โดยไม่ดูชนิดเซลล์""",
 "ref": ["สไลด์ อ.ภาณุวัฒน์ หน้า 9–10, 12, 14", "MED31 OSCE ข้อ 4 – แปลผล pleural fluid lymph เด่น Light criteria exudative", "MED30 SAQ ข้อ 1 – สงสัย TB pleural effusion"],
 "nl": ["2.3.1(20)", "2.3.10(7)", "2.3.6(5)", "B3.3(2)", "2.1.12"], "years": ["30", "31"], "_kind": "meq", "_set": "chest"}]

LECTURE = {
 "lec": "23/9",
 "date": "พ. 23 ก.ย.",
 "title": "Extrapulmonary tuberculosis",
 "subtitle": "ภาระโรคและผลของ HIV · ทำไมวินิจฉัยยาก · ถอดรหัสสารน้ำและ ADA · เยื่อหุ้มปอด ต่อมน้ำเหลือง กระดูกสันหลัง สมอง เยื่อหุ้มหัวใจ ช่องท้อง และทางเดินปัสสาวะ · ระยะเวลายา steroid ผ่าตัด · พิษยาและการตัดวงจรการแพร่เชื้อ",
 "objectives": [
   "อธิบายว่าทำไม EPTB เป็นส่วนใต้น้ำของวัณโรค และระบุกลุ่มเสี่ยงได้",
   "เปรียบเทียบรูปแบบ EPTB ระหว่างผู้ป่วยที่ติดและไม่ติด HIV และบอกเหตุผลที่ต้องตรวจ HIV ในผู้ป่วยวัณโรคทุกราย",
   "เลือกการตรวจทางจุลชีววิทยาที่เหมาะสม — smear, culture, NAAT — และรู้ข้อจำกัดของแต่ละวิธีรวมถึง TST",
   "แปลผลน้ำในเยื่อหุ้มปอด เยื่อหุ้มหัวใจ น้ำไขสันหลัง และน้ำในช่องท้อง รวมถึงจุดตัดและผลบวกลวงของ ADA",
   "จดจำอาการและการวินิจฉัยของวัณโรคเยื่อหุ้มปอด ต่อมน้ำเหลือง กระดูกสันหลัง เยื่อหุ้มสมอง เยื่อหุ้มหัวใจ ช่องท้อง และทางเดินปัสสาวะ",
   "กำหนดระยะเวลาการรักษาตามอวัยวะ ข้อบ่งชี้ของ corticosteroid สามระดับ และข้อบ่งชี้ของการผ่าตัด",
   "ระบุพิษของยาแนวแรกทีละอวัยวะ และวางมาตรการป้องกันการแพร่เชื้อและการตามผู้สัมผัส"],
 "nlGap": "**เกณฑ์ฯ รวมวัณโรคทุกตำแหน่งไว้ในรหัสเดียว** (`นล. 2.3.1(20)` และ `B6.2.2(8)`) ไม่แยกรหัสสำหรับวัณโรคต่อมน้ำเหลือง ช่องท้อง กระดูกสันหลัง หรือทางเดินปัสสาวะ และไม่มีรหัสของ **ADA** หรือ **NAAT (GeneXpert)** เนื้อหาส่วนนั้นจึงอิงแนวทางที่อาจารย์อ้างและแนวทางปัจจุบันด้านล่าง",
 "guidelines": [
   "**แนวทางการวินิจฉัยและดูแลรักษาผู้ป่วยวัณโรคในประเทศไทย 2561** — ตาราง body fluid, ADA, ระยะเวลาตามอวัยวะ, พิษยา, steroid และข้อบ่งชี้ผ่าตัด (อาจารย์อ้างในสไลด์)",
   "**แนวทางการควบคุมวัณโรคประเทศไทย 2564** — สูตร 2HRZE/4HR และ 2HRZE/10HR สำหรับวัณโรคเยื่อหุ้มสมองและกระดูกข้อ",
   "**WHO Consolidated Guidelines on Tuberculosis — Module 3: Diagnosis (2024)** — การใช้ Xpert MTB/RIF Ultra กับสิ่งส่งตรวจนอกปอด",
   "**ATS/CDC/ERS/IDSA 2016 — Treatment of Drug-Susceptible Tuberculosis** — ระยะเวลาตามอวัยวะและ corticosteroid ใน TB meningitis และ pericarditis",
   "**ESC 2015 — Guidelines for the Diagnosis and Management of Pericardial Diseases** — steroid เฉพาะผู้ป่วย HIV ลบ",
   "**Cochrane 2016 — Corticosteroids for managing tuberculous meningitis** · **IMPI (NEJM 2014)** · **ACT HIV (NEJM 2023)**"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ── ตรวจ id ซ้ำทั้งชุดวิชาก่อนเขียน
path = os.path.join(BUILD, "data", "chest.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
seen = set()
for l in data + [LECTURE]:
    for x in [i for s in l["sections"] for i in s["items"]] + l.get("meq", []) + l.get("osce", []) + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s in S for c in s["nl"]} | {c for s in S for i in s["items"] for c in i["nl"]} | {c for m in MEQ + OSCE for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบในพจนานุกรม: %s" % missing
for s in S:
    assert "```" not in s["md"], s["id"]

data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "chest": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d | nl codes %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE), len(codes)))
print("chest.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
