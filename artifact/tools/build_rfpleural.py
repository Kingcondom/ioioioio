#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Respiratory failure and Pleural disease (อ.สกล เจริญวีระกุล · จ. 28 ก.ย. 2569) → data/chest.json
ต้นฉบับ: สไลด์ "Lec12 Respiratory failure, pleural disease" (Drive 12_uIP-b1TWP-u35yfm90Q9PT5QTNgPvp)
โน้ตอ่านสไลด์อยู่ที่ slides/rf_pleural_notes.md — ข้อความสไลด์ถูกตัดหลังหัวข้อ work up pleural effusion
ส่วนที่ขาด (Light's criteria · parapneumonic · malignant effusion · การรักษา pneumothorax ไม่ tension)
เรียบเรียงจาก BTS Pleural Disease Guideline 2023 ที่อาจารย์ใช้เป็นแกน และระบุใน nlGap
ใช้ข้อในคลังของคาบ 17 (CH-MCQ-17..24 · CH-OLD-23..34 · CH-MEQ-03 · CH-OSCE-02 · CH-OSCE-04)"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # artifact/
REPO = os.path.dirname(BUILD)
NLN = ["2.3.10(7)", "B6.3(1)"]
SRC = "สไลด์ อ.สกล เจริญวีระกุล — Respiratory failure and Pleural disease (2026)"
FIX = {"2.3.4(20)": "2.3.1(20)", "2.3.5-3(1)": None}   # รหัสผิดในคลังเดิม (2.3.5-3(1) = bipolar ไม่เกี่ยว)
S = []

def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})

def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    import random
    order = list(range(5)); random.Random("own-" + iid).shuffle(order)   # กระจายตำแหน่งเฉลยแบบคงที่
    choices, answer = [choices[k] for k in order], order.index(answer)
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}

N = lambda n: "CH-RP-MCQ-%02d" % n

def _fix(codes):
    out = []
    for c in codes:
        c = FIX.get(c, c)
        if c and c not in out: out.append(c)
    return out

_BANK = {}
for f in ["chest_mcq_a", "chest_mcq_b", "chest_old_b", "chest_meq_osce"]:
    for x in json.load(open(os.path.join(REPO, "data", f + ".json"), encoding="utf-8")):
        _BANK[x["id"]] = x

def _shuffle(iid, choices, answer):
    """คลังเดิมเฉลย ก. ทุกข้อ — สลับตัวเลือกแบบคงที่ตาม id (รันซ้ำได้ผลเดิม)"""
    import random
    order = list(range(len(choices)))
    random.Random(iid).shuffle(order)
    return [choices[k] for k in order], order.index(answer)

def bank(iid):
    """ดึงข้อจากคลังคาบ 17 แปลงเป็น item ของบทเรียน"""
    x = _BANK[iid]
    ch, ans = _shuffle(iid, x["choices"], int(x["answer"]))
    if iid.startswith("CH-OLD"):
        return {"id": iid, "kind": "old", "stem": x["q"], "choices": ch, "answer": ans,
                "explain": x["note"], "pearl": "", "topic": "", "src": x.get("src", ""), "ref": [], "nl": _fix(x["nl"])}
    return {"id": iid, "kind": "mcq", "stem": x["stem"], "choices": ch, "answer": ans,
            "explain": x["explain"], "pearl": x.get("pearl", ""), "topic": x.get("topic", ""), "src": "",
            "ref": x.get("ref", []), "nl": _fix(x["nl"])}

def bank_case(iid):
    x = dict(_BANK[iid]); x["nl"] = _fix(x["nl"]); x["_kind"] = "meq"; x["_set"] = "chest"
    return x

# ───────────────────────────── 1
sec("chest-rp-01", "ออกซิเจนเดินทางอย่างไร — DO₂ และ O₂ dissociation curve",
    "ส่งออกซิเจนได้พอหรือไม่ ขึ้นกับ CO · Hb · SaO₂ — PaO₂ แทบไม่มีบทบาทโดยตรง", 8,
"""### สมการที่อาจารย์เปิดคาบ
**DO₂ = CO × [(Hb × SaO₂ × 1.34) + (PaO₂ × 0.003)]**

| ตัวเลข | ความหมาย |
|---|---|
| **1.34** | Hb 1 กรัมจับ O₂ ได้ 1.34 mL (บางตำราใช้ 1.36) = *O₂ carrying capacity* |
| **0.003** | O₂ ที่ **ละลาย** ในเลือด 0.003 mL ต่อ dL ต่อ PaO₂ 1 mmHg |

ลองแทนค่าคนปกติ — Hb 15, SaO₂ 98%, PaO₂ 100
- ส่วนที่จับ Hb = 15 × 0.98 × 1.34 ≈ **19.7 mL/dL**
- ส่วนที่ละลาย = 100 × 0.003 = **0.3 mL/dL**

> **ออกซิเจนเกือบทั้งหมด (> 98%) อยู่บน Hb** — นี่คือเหตุผลที่ผู้ป่วยซีด Hb 6 ที่ SpO₂ 100% ยังขาดออกซิเจนในเนื้อเยื่อได้ และเหตุผลที่ "ดัน PaO₂ จาก 100 เป็น 300" แทบไม่ได้เพิ่ม DO₂ เลย

ตัวแปรที่ **แก้ได้จริง** เมื่อเนื้อเยื่อขาดออกซิเจนจึงมีสามตัว — **CO** (สารน้ำ ยาเพิ่มการบีบตัว) · **Hb** (ให้เลือด) · **SaO₂** (ออกซิเจน การช่วยหายใจ) — สมการเดียวกับที่ใช้ในคาบ Circulatory shock

### O₂ dissociation curve — ตัวเลขที่ต้องจำ
| PaO₂ (mmHg) | 30 | 40 | 55 | 60 |
|---|---|---|---|---|
| **SpO₂ (%)** | 60 | 75 | 88 | 90 |

จุด **PaO₂ 60 ≈ SpO₂ 90%** คือ "ขอบหน้าผา" — เหนือจุดนี้กราฟแบน (PaO₂ ลดมากแต่ sat ลดน้อย) ใต้จุดนี้กราฟชัน (PaO₂ ลดนิดเดียว sat ร่วงเร็ว) นิยาม respiratory failure ที่ใช้ PaO₂ < 60 จึงมาจากจุดนี้

### อะไรทำให้กราฟเลื่อน
| | **Left shift** — Hb จับแน่น ปล่อยยาก | **Right shift** — Hb ปล่อยง่าย |
|---|---|---|
| 2,3-DPG | ↓ | **↑** — hyperthyroidism, ซีดเรื้อรัง, hypoxemia เรื้อรัง |
| อุณหภูมิ | ↓ (hypothermia) | ↑ (ไข้) |
| PaCO₂ | ↓ | ↑ |
| pH | ↑ (alkalosis) | ↓ (acidosis) |
| Hb ผิดชนิด | **HbF, COHb, MetHb** | — |

> จำง่าย ๆ ว่า **กล้ามเนื้อที่ทำงานหนักร้อน เป็นกรด CO₂ สูง** → right shift ช่วยปล่อย O₂ ให้ตรงที่ต้องการ ส่วน **CO และ MetHb** ทำให้ left shift ซ้ำเติม — Hb ที่เหลือก็ยังไม่ยอมปล่อย O₂""",
    ["DO₂ = CO × CaO₂ — O₂ > 98% อยู่บน Hb ส่วนที่ละลายมีแค่ 0.003 × PaO₂",
     "PaO₂ 60 ≈ SpO₂ 90% คือจุดหักของกราฟ — ใต้นี้ sat ร่วงเร็ว",
     "Right shift: 2,3-DPG ↑ ไข้ CO₂ ↑ กรด · Left shift: HbF COHb MetHb alkalosis เย็น"],
    [mcq(N(1), "A 30-year-old woman has Hb 6 g/dL from menorrhagia. SpO2 is 99% on room air and PaO2 is 98 mmHg. Increasing inspired oxygen raises her PaO2 to 300 mmHg. Which statement about her oxygen delivery is correct?",
         ["Her oxygen delivery is normal because SaO2 and PaO2 are normal",
          "Raising PaO2 to 300 mmHg roughly doubles her arterial oxygen content",
          "Her arterial oxygen content is about 40% of normal, and raising PaO2 adds only about 0.6 mL O2/dL",
          "Her oxygen dissociation curve is shifted to the left, so oxygen release is impaired",
          "Dissolved oxygen is the main determinant of her oxygen delivery"], 2,
         "แทนค่า **CaO₂ = (Hb × SaO₂ × 1.34) + (PaO₂ × 0.003)**\n- ปกติ (Hb 15): 15 × 0.99 × 1.34 + 0.3 ≈ **20 mL/dL**\n- ผู้ป่วยรายนี้ (Hb 6): 6 × 0.99 × 1.34 + 0.3 ≈ **8.3 mL/dL** ≈ 40% ของปกติ\n- เพิ่ม PaO₂ จาก 98 → 300 = เพิ่มส่วนที่ละลาย (300 − 98) × 0.003 ≈ **0.6 mL/dL** เท่านั้น\n\nSpO₂ และ PaO₂ บอกแค่ว่า Hb ที่มีอยู่ **อิ่มตัวแค่ไหน** ไม่ได้บอกว่า **มี Hb พอหรือไม่** — นี่คือ *anemic hypoxia* ที่แก้ด้วยการเพิ่ม Hb ไม่ใช่เพิ่มออกซิเจน · ซีดเรื้อรังทำให้ 2,3-DPG สูง กราฟเลื่อน **ขวา** (ไม่ใช่ซ้าย)",
         "ซีดมาก sat 100% ก็ยังขาด O₂ ได้ — O₂ ที่ละลายช่วยน้อยมาก", "Oxygen content and delivery",
         ["สไลด์ อ.สกล — Equation of O2 delivery, Why 1.34, 0.003"], ["B6.1.2(5)", "2.2.9"]),
     mcq(N(2), "Which of the following shifts the oxyhaemoglobin dissociation curve to the RIGHT?",
         ["Carbon monoxide poisoning", "Hypothermia during cardiac surgery", "Chronic hypoxaemia at high altitude",
          "Acute respiratory alkalosis from hyperventilation", "Fetal haemoglobin"], 2,
         "**Hypoxemia เรื้อรัง** (อยู่ที่สูง โรคปอดเรื้อรัง) และ **ซีดเรื้อรัง, hyperthyroidism** เพิ่ม **2,3-DPG** ในเม็ดเลือดแดง → Hb จับ O₂ หลวมลง → **right shift** ปล่อย O₂ ให้เนื้อเยื่อง่ายขึ้น\n\nตัวเลือกอื่นเป็น **left shift** ทั้งหมด — CO (COHb), อุณหภูมิต่ำ, alkalosis (pH สูง CO₂ ต่ำ) และ HbF (จับ 2,3-DPG ได้น้อย)",
         "2,3-DPG ↑ = ขวา: ที่สูง ซีดเรื้อรัง ไทรอยด์เป็นพิษ", "Oxyhaemoglobin dissociation curve",
         ["สไลด์ อ.สกล — O2 affinity table"], ["B6.1.2(5)", "B6.1.2(6)"])],
    ["B6.1.2(5)", "2.2.9"])

# ───────────────────────────── 2
sec("chest-rp-02", "Hypoxia ไม่เท่ากับ hypoxemia — สี่แบบ และเมื่อไร SpO₂ โกหก",
    "hypoxemic · anemic · circulatory · histotoxic · saturation gap > 5% · PaO₂ ที่ยอมรับได้ตามอายุ", 8,
"""### คำสองคำที่มักใช้ปนกัน
- **Hypoxemia** = ออกซิเจนใน **เลือดแดง** ต่ำ (PaO₂ หรือ SaO₂ ต่ำ)
- **Hypoxia** = ออกซิเจนที่ **เนื้อเยื่อ** ได้รับไม่พอ — hypoxemia เป็นแค่หนึ่งในสี่สาเหตุ

| ชนิด hypoxia | ปัญหาอยู่ที่ | ตัวอย่าง | PaO₂ |
|---|---|---|---|
| **Hypoxemic** | ปอด/การหายใจ | pneumonia, hypoventilation | **ต่ำ** |
| **Anemic** | ตัวขน — Hb น้อยหรือผิดปกติ | ซีด, CO poisoning, methemoglobinemia | ปกติ |
| **Circulatory** | การไหลเวียน | shock ทั้งสี่ชนิด, ischemia | ปกติ |
| **Histotoxic** | เซลล์ใช้ O₂ ไม่ได้ | cyanide (mitochondrial poisoning), left shift รุนแรง | ปกติ |

> ลายมือในสไลด์ — **lactate สูง = shock** · เมื่อ PaO₂ ปกติแต่ lactate สูง ให้มองหาสามแบบหลัง

### ความรุนแรงของ hypoxemia
| ระดับ | PaO₂ (mmHg) |
|---|---|
| Mild | 60–79 |
| Moderate | 40–59 |
| Severe | < 40 |

### PaO₂ ปกติลดลงตามอายุ — อย่าเรียกผู้สูงอายุว่า hypoxemia ง่ายเกินไป
| อายุ (ปี) | ≤ 60 | 70 | 80 | 90 |
|---|---|---|---|---|
| PaO₂ ที่ยอมรับได้ | > 80 | > 70 | > 60 | > 50 |

### True hypoxemia — เทียบ SpO₂ กับ SaO₂ ก่อนเชื่อ
pulse oximeter ใช้แสงสองความยาวคลื่น แยกได้แค่ oxy-Hb กับ deoxy-Hb จึง **อ่านผิดเมื่อมี Hb ผิดชนิด**
- **Saturation gap > 5%** (SpO₂ ต่างจาก SaO₂ ที่วัดจริงด้วย co-oximetry) → คิดถึง **Hb ผิดปกติ**
- **Carboxyhemoglobin (CO poisoning)** — COHb ดูดแสงคล้าย oxy-Hb → **SpO₂ ปกติหลอกตา** ทั้งที่ขาดออกซิเจนรุนแรง
- **Methemoglobinemia** — SpO₂ ค้างราว **85%** ไม่ว่า PaO₂ จะเท่าไร ให้ O₂ แล้วไม่ดีขึ้น เลือดสีน้ำตาลช็อกโกแลต (ยา dapsone, nitrite, local anesthetic)
- **Sulfhemoglobinemia** และ Hb โครงสร้างผิดปกติอื่น ๆ
- ปัจจัยทั่วไป: มือเย็น/ช็อก (สัญญาณอ่อน), ยาทาเล็บ, ผิวคล้ำ (อ่านสูงกว่าจริง)""",
    ["Hypoxia 4 แบบ: hypoxemic · anemic · circulatory · histotoxic — 3 แบบหลัง PaO₂ ปกติ",
     "CO poisoning: SpO₂ ปกติหลอกตา · MetHb: SpO₂ ค้าง ~85% ให้ O₂ ไม่ขึ้น",
     "PaO₂ ปกติลดตามอายุ: ≤60 ปี > 80 · 80 ปี > 60"],
    [mcq(N(3), "A family of four is brought from a closed room heated by a charcoal stove. All have headache and confusion. The father's SpO2 is 99% on room air, but arterial blood gas shows a measured SaO2 of 72% by co-oximetry. What is the most likely explanation?",
         ["Methaemoglobinaemia", "Carbon monoxide poisoning", "Cyanide poisoning", "Pulse oximeter malfunction from cold extremities", "Hypoventilation from sedation"], 1,
         "**Saturation gap 99 − 72 = 27% (> 5%)** = Hb ผิดชนิด · บริบทเตาถ่านในห้องปิด → **CO poisoning**\n\n**COHb ดูดแสงคล้าย oxy-Hb** เครื่องวัดปลายนิ้วจึงอ่านว่าอิ่มตัวดี ทั้งที่ Hb ส่วนหนึ่งถูก CO ยึดไปแล้วและกราฟยัง **left shift** ซ้ำ → anemic hypoxia\n\nMetHb จะทำให้ SpO₂ ค้างราว 85% ไม่ใช่ 99% · cyanide เป็น histotoxic hypoxia ที่ SaO₂ ปกติ\n\nรักษา: **100% O₂ ผ่าน non-rebreather** (ลดครึ่งชีวิต COHb จาก ~5 ชม. เหลือ ~1 ชม.) พิจารณา hyperbaric O₂ ในรายรุนแรง",
         "SpO₂ ปกติ + อาการขาด O₂ + ห้องปิด → CO · ต้องวัด SaO₂ ด้วย co-oximetry", "True hypoxemia – saturation gap",
         ["สไลด์ อ.สกล — True hypoxemia, saturation gap > 5%"], ["B6.1.2(5)", "2.2.9", "3.3.17"]),
     mcq(N(4), "An 82-year-old man with no lung disease has a routine arterial blood gas on room air: PaO2 65 mmHg, PaCO2 38 mmHg. Which interpretation is most appropriate?",
         ["Moderate hypoxaemia requiring long-term oxygen therapy", "Type 1 respiratory failure",
          "Within the acceptable range for his age", "Severe hypoxaemia", "Hypoventilation"], 2,
         "ตารางในสไลด์ — **PaO₂ ที่ยอมรับได้ลดลงตามอายุ**: ≤ 60 ปี > 80 · 70 ปี > 70 · **80 ปี > 60** · 90 ปี > 50\n\nที่อายุ 82 ปี PaO₂ 65 จึงอยู่ในเกณฑ์ ไม่ใช่ respiratory failure (ต้อง < 60) และ PaCO₂ ปกติ ไม่มี hypoventilation\n\nถ้าคิด A-a gradient: PAO₂ = 150 − 38/0.8 ≈ 102.5 → A-a ≈ 37.5 · ค่าปกติ = อายุ/4 + 4 = **24.5** จึงกว้างเล็กน้อยตามความเสื่อมของปอดผู้สูงอายุ",
         "PaO₂ ปกติลดตามอายุ — 80 ปี > 60 ก็ยอมรับได้", "Age-adjusted PaO2",
         ["สไลด์ อ.สกล — Acceptable PaO2 by age group"], ["B6.1.2(4)", "3.3.17"])],
    ["B6.1.2(5)", "2.2.9", "2.1.37"])

# ───────────────────────────── 3
sec("chest-rp-03", "A-a gradient — เครื่องมือแยกปอดเสียกับหายใจไม่พอ",
    "PAO₂ = 150 − PaCO₂/0.8 · ปกติ = อายุ/4 + 4 · A-a ปกติ = low PiO₂ หรือ hypoventilation", 9,
"""### สูตร (ที่ room air ระดับน้ำทะเล)
**PAO₂ = [FiO₂ × (Pb − PH₂O)] − PaCO₂/RQ**
= [0.21 × (760 − 47)] − PaCO₂/0.8
= **150 − PaCO₂/0.8**

**P(A−a)O₂ = PAO₂ − PaO₂** · ค่าปกติ ≈ **อายุ/4 + 4**

| ตัวแปร | ค่า |
|---|---|
| FiO₂ | 0.21 ที่ room air |
| Pb | 760 mmHg ที่ระดับน้ำทะเล |
| PH₂O | 47 mmHg ที่ 37 °C |
| RQ | ~0.8 ในภาวะคงที่ อาหารปกติ |

### ตัวอย่างคิดเร็ว
ชาย 40 ปี PaO₂ 60 PaCO₂ 40 → PAO₂ = 150 − 50 = 100 → **A-a = 40** (ปกติ ≤ 14) → **กว้าง = ปัญหาในปอด**

### A-a ปกติแต่ hypoxemia — ปอดดี ปัญหาอยู่นอกปอด
| กลุ่ม | ตัวอย่างในสไลด์ |
|---|---|
| **Low PiO₂** | ขึ้นที่สูง เครื่องบิน |
| **Central hypoventilation** | brainstem lesion, **ยากดการหายใจ** (opioid, benzodiazepine), **obesity hypoventilation syndrome**, primary alveolar hypoventilation |
| **Spinal cord** | **ALS**, C-spine injury |
| **Peripheral nerve** | **Guillain–Barré syndrome** |
| **Neuromuscular junction** | **Myasthenia gravis**, Lambert–Eaton |
| **กล้ามเนื้อ** | myopathy |
| **ผนังทรวงอก** | kyphoscoliosis, thoracoplasty, fibrothorax |

> ลักษณะร่วมของ hypoventilation คือ **PaCO₂ สูง** — และเพราะ A-a ปกติ **ให้ออกซิเจนแล้ว PaO₂ ดีขึ้น** แต่ **ไม่ได้แก้ CO₂** ต้องเพิ่ม ventilation (NIV/ใส่ท่อ) หรือแก้สาเหตุ

### A-a กว้าง — ปัญหาในเนื้อปอด
**V/Q mismatch · shunt · dead space · diffusion limitation** (รายละเอียดหัวข้อถัดไป)

### กับดักของสูตร
- ใช้ได้ดีเฉพาะ **room air** · ที่ FiO₂ สูงค่าปกติกว้างขึ้นมาก ใช้ **P/F ratio** แทน
- ผู้ป่วยที่ทั้ง hypoventilation และมีโรคปอด (COPD exacerbation) → PaCO₂ สูง **และ** A-a กว้าง""",
    ["PAO₂ = 150 − PaCO₂/0.8 · A-a ปกติ ≈ อายุ/4 + 4",
     "A-a ปกติ + PaCO₂ สูง = hypoventilation: ยา OHS GBS MG ALS kyphoscoliosis",
     "Hypoventilation: ให้ O₂ แก้ PaO₂ ได้ แต่ CO₂ ต้องแก้ด้วย ventilation"],
    [mcq(N(5), "A 25-year-old man is found drowsy after taking an unknown amount of his mother's morphine tablets. Room-air arterial blood gas: pH 7.22, PaCO2 70 mmHg, PaO2 55 mmHg. What is his alveolar-arterial oxygen gradient and what does it indicate?",
         ["About 8 mmHg; hypoxaemia is fully explained by hypoventilation", "About 37 mmHg; aspiration pneumonia must be present",
          "About 58 mmHg; there is a large shunt", "About 95 mmHg; severe V/Q mismatch", "It cannot be calculated without FiO2 above 0.21"], 0,
         "PAO₂ = 150 − 70/0.8 = 150 − 87.5 = **62.5** → A-a = 62.5 − 55 = **7.5 mmHg** (ปกติที่อายุ 25 ≈ 10)\n\n**A-a ปกติ + PaCO₂ สูง = pure alveolar hypoventilation** จาก opioid กดศูนย์หายใจ — ปอดปกติ\n\nถ้า A-a กว้างขึ้นในรายเดียวกัน แปลว่ามีปัญหาในปอดซ้อน เช่น **aspiration pneumonia** ที่พบบ่อยในผู้ป่วยซึม\n\nรักษา: **naloxone** + ช่วยหายใจ (bag-valve-mask) ไม่ใช่แค่เพิ่มออกซิเจน",
         "PaCO₂ สูง + A-a ปกติ = hypoventilation ล้วน → แก้ที่ ventilation", "A-a gradient in hypoventilation",
         ["สไลด์ อ.สกล — A-a gradient formula, Normal A-a gradient hypoxemia"], ["B6.1.2(3)", "B6.2.5(1)", "3.3.17"]),
     mcq(N(6), "Which patient's hypoxaemia is expected to have a NORMAL alveolar-arterial oxygen gradient?",
         ["A 50-year-old man with right lower lobe pneumonia", "A 45-year-old woman with acute pulmonary embolism",
          "A 30-year-old woman with myasthenic crisis and no aspiration", "A 60-year-old man with idiopathic pulmonary fibrosis",
          "A 35-year-old man with ARDS after pancreatitis"], 2,
         "**Myasthenic crisis** = กล้ามเนื้อหายใจอ่อนแรงที่ neuromuscular junction → **alveolar hypoventilation** → PaCO₂ สูง, PaO₂ ต่ำ แต่ **A-a ปกติ** ตราบที่ยังไม่มีปอดอักเสบหรือปอดแฟบซ้อน\n\nตัวเลือกอื่นเป็นโรคในเนื้อปอด/หลอดเลือดปอด → A-a กว้าง: pneumonia และ ARDS (shunt), PE (V/Q mismatch, dead space), IPF (diffusion limitation + V/Q)\n\nติดตาม MG crisis ด้วย **FVC/NIF** ไม่ใช่ SpO₂ เพราะ sat ตกช้ากว่าการล้าของกล้ามเนื้อ",
         "Neuromuscular → hypoventilation → A-a ปกติ · ติดตามด้วย FVC/NIF", "Causes of normal A-a gradient hypoxaemia",
         ["สไลด์ อ.สกล — Normal A-a gradient hypoxemia"], ["B6.2.5(1)", "B6.1.2(3)"])],
    ["B6.2.5(1)", "3.3.17", "B6.1.2(3)"])

# ───────────────────────────── 4
sec("chest-rp-04", "V/Q mismatch · shunt · dead space · diffusion — ให้ O₂ แล้วดีขึ้นไหม",
    "shunt ไม่ตอบสนองต่อ O₂ · dead space ทำให้ CO₂ คั่ง · diffusion ตกตอนออกแรง · PE กับ HPV", 10,
"""### สี่กลไกของ A-a กว้าง
**V/Q ปกติทั้งปอด ≈ 0.8** — ปลายบนปอด V/Q สูง ฐานปอด V/Q ต่ำ

| กลไก | V/Q | ตัวอย่าง | PaCO₂ | ตอบสนองต่อ O₂ |
|---|---|---|---|---|
| **V/Q mismatch (low V/Q)** | ต่ำ | asthma, COPD, pneumonia บางส่วน | ปกติ/ต่ำ | **ดี** — สาเหตุที่พบบ่อยที่สุด |
| **Shunt** | **0** (มีเลือดไม่มีลม) | pneumonia เต็ม alveoli, **ARDS, pulmonary edema, atelectasis**, intracardiac R→L | ปกติ/ต่ำ | **น้อยมาก** |
| **Dead space** | **∞** (มีลมไม่มีเลือด) | **PE**, emphysema, ช็อก, PEEP สูงเกิน | **↑** | ดีขึ้นบ้าง |
| **Diffusion limitation** | — | **ILD**, emphysema, ออกกำลังกาย | ปกติ/ต่ำ | **ดี** · A-a กว้าง **ตอนออกแรง** |

ลายมือในสไลด์ — ILD **sat ปกติตอนพัก แต่ตกตอนออกแรง** เพราะ transit time สั้นลงจนก๊าซซึมผ่านเยื่อหนาไม่ทัน → **6-minute walk test** เผยได้

### ทำไม shunt ไม่ตอบสนองต่อออกซิเจน
เลือดที่ผ่าน alveoli ที่เต็มน้ำ/หนอง **ไม่เคยสัมผัสก๊าซที่เราให้เลย** แล้วมาผสมกับเลือดดี — เพิ่ม FiO₂ แค่ไหน ส่วนที่ดีก็อิ่มตัวอยู่แล้ว

**Shunt fraction** Qs/Qt = (CcO₂ − CaO₂)/(CcO₂ − CvO₂) · **ปกติ ≤ 5%** (bronchial และ thebesian veins)

| PaO₂ บน 100% O₂ (mmHg) | 550 | 450 | 350 | 250 |
|---|---|---|---|---|
| **Shunt (%)** | 5 | 10 | 15 | 20 |

การแก้ shunt คือ **เปิด alveoli กลับ** — **PEEP**, recruitment, รักษาสาเหตุ (ขับน้ำ ยาปฏิชีวนะ) ไม่ใช่เพิ่ม O₂ อย่างเดียว

### Pulmonary embolism — dead space หรือ shunt?
คำตอบในสไลด์คือ **ทั้งสองแบบ**
- บริเวณที่ลิ่มเลือดอุด = **dead space** (มีลม ไม่มีเลือด)
- เลือดถูก **เบนไปปอดส่วนที่เหลือมากเกิน** → ปอดส่วนนั้น V ปกติ Q เพิ่ม → **V/Q ต่ำ → hypoxemia แบบคล้าย shunt**
- จึงมักเห็น **PaO₂ ต่ำ + PaCO₂ ต่ำ** (หายใจเร็วชดเชย) ใน PE

### Hypoxic pulmonary vasoconstriction (HPV) และ COPD กับออกซิเจน
- ปอดส่วนที่ O₂ ต่ำ หลอดเลือดจะ **หดตัว** เพื่อเบนเลือดไปส่วนที่ระบายอากาศดี = กลไกป้องกันตัวเอง
- **ให้ O₂ มากเกินใน COPD** → ปลด HPV (O₂ เป็น vasodilator) → เลือดกลับไปเลี้ยงส่วนที่ระบายลมไม่ดี → V/Q แย่ลง + Haldane effect + ศูนย์หายใจถูกกด → **CO₂ คั่ง** (ลายมือในสไลด์)
- นี่คือเหตุผลของเป้า **SpO₂ 88–92%** ใน COPD และผู้มีความเสี่ยง CO₂ คั่ง

### PaCO₂ บอกอะไร
**PaCO₂ = 0.863 × VCO₂ / [(VT − VD) × RR]** · anatomical dead space ≈ 150 mL
| PaCO₂ | ภาวะ | การระบายอากาศ |
|---|---|---|
| > 45 | Hypercapnia | Hypoventilation |
| 35–45 | Eucapnia | ปกติ |
| < 35 | Hypocapnia | Hyperventilation |

> ผู้ป่วยหายใจ **เร็วแต่ตื้น** (VT ต่ำ) — สัดส่วน dead space ต่อ VT สูงขึ้น ระบายอากาศจริงลดลง PaCO₂ จึงขึ้นได้แม้ RR 35""",
    ["Shunt (V/Q = 0) ไม่ตอบสนองต่อ O₂ — แก้ด้วย PEEP เปิด alveoli",
     "Dead space (V/Q = ∞) ทำให้ CO₂ คั่ง · PE มีทั้ง dead space และ low V/Q",
     "ILD: sat ปกติตอนพัก ตกตอนออกแรง (diffusion limitation)",
     "COPD ให้ O₂ มากไป → ปลด HPV → CO₂ คั่ง → เป้า SpO₂ 88–92%"],
    [mcq(N(7), "A 40-year-old man with ARDS from severe pneumonia is intubated. On FiO2 1.0 his PaO2 is only 70 mmHg. Increasing FiO2 further is not possible. Which intervention addresses the main mechanism of his hypoxaemia?",
         ["Increase the respiratory rate to lower PaCO2", "Increase positive end-expiratory pressure (PEEP) to recruit collapsed alveoli",
          "Start inhaled bronchodilators", "Transfuse red cells to Hb 14 g/dL", "Give intravenous sodium bicarbonate"], 1,
         "PaO₂ 70 บน FiO₂ 1.0 = **shunt ขนาดใหญ่** (ตารางสไลด์: PaO₂ 250 บน 100% O₂ ≈ shunt 20% — รายนี้มากกว่านั้นมาก)\n\nกลไกหลักของ ARDS คือ alveoli เต็มน้ำและแฟบ → เลือดผ่านโดยไม่ได้แลกก๊าซ · **เพิ่ม O₂ ไม่ช่วย** สิ่งที่ช่วยคือ **เปิด alveoli กลับมา** ด้วย **PEEP** (และ prone position ในรายรุนแรง) ร่วมกับ lung-protective ventilation\n\nเพิ่ม RR แก้ CO₂ ไม่แก้ shunt · bronchodilator แก้ low V/Q จากหลอดลมตีบ · ให้เลือดเพิ่ม DO₂ แต่ไม่แก้ PaO₂",
         "Shunt ไม่ตอบ O₂ → แก้ด้วย PEEP/prone", "Shunt and refractory hypoxaemia",
         ["สไลด์ อ.สกล — Shunt fraction table, Parameters in hypoxemia"], ["B6.2.5(1)", "2.3.10-3(1)", "B6.1.2(2)"]),
     mcq(N(8), "A 58-year-old man with interstitial lung disease has SpO2 96% at rest, which falls to 84% after walking for 3 minutes. Which mechanism best explains the exercise-induced desaturation?",
         ["Right-to-left intracardiac shunt", "Alveolar hypoventilation", "Diffusion limitation from shortened capillary transit time",
          "Increased dead space from pulmonary embolism", "Left shift of the oxygen dissociation curve"], 2,
         "สไลด์อธิบาย diffusion limitation ว่าเกิดจาก **พื้นที่ลด · การอักเสบ · พังผืดที่ alveolocapillary membrane · transit time สั้นเกิน** — ตัวอย่างคือ **emphysema, ILD และการออกกำลัง**\n\nตอนพัก เม็ดเลือดแดงอยู่ในเส้นเลือดฝอยราว 0.75 วินาที นานพอให้ O₂ ซึมผ่านเยื่อที่หนาขึ้นได้ทัน · เมื่อออกแรง CO เพิ่ม **transit time สั้นลง** จนซึมไม่ทัน → sat ตก (ลายมือ: *sat ปกติตอนพัก ตกตอน stress*)\n\nตรวจที่เผยภาวะนี้: **6-minute walk test** และ DLCO",
         "ILD: sat ตกตอนออกแรง = diffusion limitation", "Diffusion limitation",
         ["สไลด์ อ.สกล — Diffusion limitation"], ["B6.1.2(4)", "B6.2.5(1)"])],
    ["B6.1.2(2)", "B6.1.2(4)", "B6.2.5(1)"])

# ───────────────────────────── 5
sec("chest-rp-05", "Respiratory failure สี่ชนิด และเลือกออกซิเจนให้ตรงกลไก",
    "Type I hypoxic · II ventilatory · III perioperative · IV shock · HFNC/ROX · NIV · เกณฑ์ใส่ท่อช่วยหายใจ", 10,
"""### นิยามตามก๊าซเลือด
- **Type I (hypoxemic)** — PaO₂ < 60 mmHg, PaCO₂ ปกติหรือต่ำ
- **Type II (hypercapnic)** — PaCO₂ > 45–50 mmHg ร่วมกับ pH < 7.35 (เฉียบพลัน)

### ตารางสี่ชนิดของ อ.สกล
| | **Type I – Hypoxic** | **Type II – Ventilatory** | **Type III – Perioperative** | **Type IV – Shock** |
|---|---|---|---|---|
| กลไก | V/Q mismatch, **shunt**, diffusion, low PiO₂ | **hypoventilation**, dead space | **atelectasis** (FRC ลด) | **hypoperfusion** |
| ตัวอย่าง | pneumonia, **ARDS**, pulmonary edema | **CNS injury, MG crisis**, airway exacerbation, obesity | **obesity, ascites**, bronchospasm, เสมหะ, ยาสลบ/ยาระงับประสาท | hemorrhage, **sepsis**, MI, pneumothorax |

**Type II = load > capacity** — ภาระงานการหายใจ (หลอดลมตีบ ปอดแข็ง ท้องโต) มากกว่าที่ศูนย์หายใจ เส้นประสาท และกล้ามเนื้อจะรับไหว
**Type III** — หลังดมยาสลบ FRC ลดลงจนต่ำกว่า closing volume → airway ปิดตัว → ปอดแฟบฐานปอด → แก้ด้วย **ลุกนั่ง, incentive spirometry, คุมปวด, recruitment**
**Type IV** — กล้ามเนื้อหายใจใช้ CO ถึง 40% ในช็อก การใส่ท่อช่วยหายใจ "ปลดภาระ" ให้เลือดไปเลี้ยงอวัยวะสำคัญ

### เลือกอุปกรณ์ออกซิเจน *(แนวทาง BTS Oxygen 2017 — ไม่อยู่ในสไลด์ส่วนที่ดึงได้)*
| อุปกรณ์ | อัตราไหล | FiO₂ โดยประมาณ |
|---|---|---|
| Nasal cannula | 1–6 L/min | 0.24–0.44 (+~4% ต่อ L) |
| Simple face mask | 5–10 L/min | 0.35–0.55 |
| **Venturi mask** | ตามสี | **คงที่** 0.24–0.60 — เหมาะกับ COPD |
| Non-rebreather mask | 10–15 L/min | 0.60–0.90 |
| **High-flow nasal cannula (HFNC)** | สูงถึง 60 L/min | ถึง 1.0 + PEEP เล็กน้อย + ล้าง dead space |

**เป้า SpO₂** — ทั่วไป **94–98%** · มีความเสี่ยง CO₂ คั่ง (COPD, OHS, neuromuscular) **88–92%**

**ROX index = (SpO₂/FiO₂) ÷ RR** — ประเมิน HFNC · **≥ 4.88** ที่ 2, 6, 12 ชม. ทำนายว่าไม่ต้องใส่ท่อ · ต่ำลงเรื่อย ๆ = อย่ารอใส่ท่อ

### NIV (BiPAP) ใช้ได้ผลชัดในสองกลุ่ม
1. **AECOPD ที่ pH < 7.35 และ PaCO₂ > 45** ยังรู้สึกตัว ไอขับเสมหะได้
2. **Cardiogenic pulmonary edema** (CPAP หรือ BiPAP)
ข้อห้าม: ซึมมาก ปกป้องทางเดินหายใจไม่ได้ อาเจียน/เลือดออกทางเดินอาหารส่วนบน ช็อก ใบหน้าบาดเจ็บ ไม่ร่วมมือ

### เกณฑ์ใส่ท่อช่วยหายใจ — คิดเป็นสี่ข้อ
| ข้อบ่งชี้ | ตัวอย่าง |
|---|---|
| **Oxygenation ล้มเหลว** | SpO₂ ไม่ถึงเป้าแม้ HFNC/NIV, ROX ต่ำลง |
| **Ventilation ล้มเหลว** | pH ลดลงเรื่อย ๆ, PaCO₂ สูงขึ้นแม้ใช้ NIV, ล้า หายใจ paradoxical |
| **ปกป้องทางเดินหายใจไม่ได้** | GCS ≤ 8, ไม่มี gag/ไอ, อาเจียนสำลัก |
| **คาดการณ์ว่าจะแย่ลง** | angioedema/แผลไหม้ทางเดินหายใจ, ช็อก, ต้องย้ายไปทำหัตถการ |

> การตัดสินใจเป็น **ทางคลินิก** — ไม่ต้องรอผลก๊าซเลือดถ้าผู้ป่วยล้าชัดเจน""",
    ["Type I hypoxic · II ventilatory (load > capacity) · III perioperative (atelectasis) · IV shock",
     "เป้า SpO₂ 94–98% ทั่วไป · 88–92% ถ้าเสี่ยง CO₂ คั่ง",
     "NIV ได้ผลชัด: AECOPD pH < 7.35 และ cardiogenic pulmonary edema",
     "ใส่ท่อ = oxygenation · ventilation · airway protection · anticipated course"],
    [bank("CH-MCQ-22"), bank("CH-OLD-32"),
     mcq(N(9), "A 62-year-old obese woman becomes hypoxaemic on postoperative day 1 after an upper abdominal operation. She is alert, temperature 37.4 °C, and has decreased breath sounds at both lung bases. Chest radiograph shows bibasal plate-like opacities. Which type of respiratory failure is this and what is the most appropriate initial management?",
         ["Type 1 from ARDS; intubate and apply high PEEP", "Type 2 from opioid overdose; give naloxone",
          "Type 3 (perioperative) from atelectasis; sit upright, provide analgesia, incentive spirometry and early mobilisation",
          "Type 4 from septic shock; give broad-spectrum antibiotics and fluid boluses", "Type 1 from pulmonary embolism; start thrombolysis"], 2,
         "ตารางของ อ.สกล — **Type III perioperative** เกิดจาก **atelectasis** เพราะ FRC ลดลงหลังดมยาสลบ ร่วมกับปวดแผลจนหายใจตื้น ท้องอืด อ้วน\n\nวันแรกหลังผ่าตัดช่องท้องส่วนบน ไข้ต่ำ ๆ ปอดฐานเสียงเบา และภาพ plate-like atelectasis เข้ากันทั้งหมด\n\nรักษาด้วย **การเปิดปอดคืน** — นั่งตัวตรง คุมปวดให้หายใจลึกได้ incentive spirometry ไอขับเสมหะ ลุกเดินเร็ว ± CPAP · ไม่ใช่ยาปฏิชีวนะหรือละลายลิ่มเลือดโดยไม่มีหลักฐาน",
         "หลังผ่าตัดวันแรก ปอดฐานแฟบ = Type III → เปิดปอดคืน", "Type 3 (perioperative) respiratory failure",
         ["สไลด์ อ.สกล — Respiratory failure type 3, Lung volume in general anesthesia"], ["2.2.9", "2.3.10(2)", "B6.2.5(1)"])],
    ["2.2.9", "B6.2.5(1)", "2.2.11"])

# ───────────────────────────── 6
sec("chest-rp-06", "เจ็บหน้าอกจากปอด — ประสาทของเยื่อหุ้มปอด และตรวจร่างกายแยก ลม น้ำ เนื้อ",
    "visceral pleura ไม่รู้สึกเจ็บ · parietal → intercostal/phrenic · ตารางตรวจร่างกายห้าแบบ", 8,
"""### ทำไมเจ็บตรงนั้น — ประสาทของเยื่อหุ้มปอด
| ส่วน | เส้นประสาท | รับรู้ | ความหมายทางคลินิก |
|---|---|---|---|
| **Parietal – costal** | **Intercostal nerves** (somatic) | ปวด แรงกด อุณหภูมิ สัมผัส | เจ็บตรงจุด ชี้ได้ ร้าวตามแนวซี่โครง |
| **Parietal – mediastinal และ central diaphragm** | **Phrenic nerve** (C3–5) | ปวด | **ปวดร้าวไหล่ข้างเดียวกัน** |
| **Visceral pleura** | Vagus + sympathetic (pulmonary plexus) | **แค่การยืด** | **ไม่เจ็บ** — ปอดอักเสบเจ็บก็ต่อเมื่อลามถึง parietal pleura |

### ชนิดของเจ็บหน้าอกจากระบบหายใจ
- **Pleuritic pain (พบบ่อยที่สุด)** — แหลม แทง ใกล้ผนังอก **หายใจลึก/ไอ/ขยับแล้วเจ็บมากขึ้น** ข้างเดียวตามฝั่งที่เป็นโรค ± **pleural rub**
- **Pulmonary pain** (tracheitis, tracheobronchitis) — แสบร้อนกลางอก ไอแล้วเจ็บ
- **แน่นหน้าอก (chest tightness)** — asthma/COPD exacerbation, massive PE
- **Pulmonary hypertension** — เจ็บเหมือน **angina** (หลังกระดูกอก ออกแรงแล้วเจ็บ พักแล้วหาย) เพราะ RV ขาดเลือดจากภาระที่เพิ่ม
- เจ็บหน้าอก **ร่วมกับความดันตก** → คิดภาวะฉุกเฉินทางปอดก่อน: **tension pneumothorax, massive PE**
- เจ็บหน้าอกจากระบบหายใจคิดเป็นราว **10%** ของผู้ป่วยที่รับไว้จากห้องฉุกเฉิน

### ตารางตรวจร่างกาย — ข้อสอบชอบถามมาก
| ภาวะ | Expansion | Tactile fremitus | Percussion | Breath sound | อื่น ๆ |
|---|---|---|---|---|---|
| **ลม** (pneumothorax, emphysema) | ↓ | ↓ | **Hyperresonance** | ↓ | — |
| **น้ำ** (pleural effusion) | ↓ | ↓ | **Dullness** (stony) | ↓ | trachea ดันไปฝั่งตรงข้ามถ้ามาก |
| **Consolidation** | ↓/ปกติ | **↑** | Dull | **Bronchial** | crackles, **egophony**, whispered pectoriloquy |
| **Fibrosis** | ↓ | ↑/ปกติ | ปกติ/dull | ↓ | **late inspiratory (velcro) crackles** |
| **Asthma/COPD** | ↓ สองข้าง | ↓ สองข้าง | ปกติ/hyperresonance | ↓ สองข้าง | wheeze, poor air entry |

> จุดแยกที่สำคัญที่สุด: **น้ำ vs เนื้อปอดแน่น** — dull เหมือนกัน แต่ **fremitus ลดในน้ำ เพิ่มใน consolidation** (เสียงเดินผ่านเนื้อแน่นได้ดี แต่ถูกน้ำกั้น)""",
    ["Visceral pleura ไม่เจ็บ · parietal costal → intercostal · central diaphragm → phrenic ร้าวไหล่",
     "น้ำ: dull + fremitus ↓ · consolidation: dull + fremitus ↑ + bronchial BS",
     "ลม: hyperresonance + BS ↓ · เจ็บอก + BP ตก = tension PTX / massive PE"],
    [bank("CH-OLD-33"),
     mcq(N(10), "A 35-year-old man with right lower lobe pneumonia complains of sharp pain at the tip of his right shoulder that worsens with deep breathing. Shoulder examination is normal. Which nerve carries this pain?",
         ["Right intercostal nerves T7–T9", "Vagus nerve", "Phrenic nerve", "Long thoracic nerve", "Suprascapular nerve"], 2,
         "ตารางประสาทในสไลด์ — **parietal pleura ส่วน mediastinal และ central diaphragm** รับความรู้สึกผ่าน **phrenic nerve (C3–C5)** ซึ่งมาจากระดับไขสันหลังเดียวกับผิวหนังบริเวณไหล่ → สมองแปลว่า **ปวดที่ไหล่** (referred pain)\n\nส่วน costal pleura ใช้ intercostal nerves → เจ็บตรงผนังอก · visceral pleura (vagus/sympathetic) รับรู้แค่การยืด **ไม่เจ็บ**",
         "ปวดร้าวไหล่จากปอด = central diaphragmatic pleura → phrenic", "Pleural innervation",
         ["สไลด์ อ.สกล — Pleura and nerve supply"], ["B6.1.1(4)", "2.1.35"])],
    ["2.1.35", "2.1.34", "B6.1.1(4)"])

# ───────────────────────────── 7
sec("chest-rp-07", "Pneumothorax — ชนิด สาเหตุ และวินิจฉัยด้วยตา ฟิล์ม อัลตราซาวด์",
    "primary · secondary · traumatic/iatrogenic · tension = วินิจฉัยทางคลินิก · lung sliding และ lung point", 10,
"""### สามรูปแบบตามกลไก
| ชนิด | กลไก |
|---|---|
| **Open** | ผนังทรวงอกเปิด อากาศจาก **ภายนอก** เข้า (visceral pleura ยังดี) — แผลดูดลม |
| **Closed** | visceral pleura ฉีก แล้ว **ปิดผนึกเองได้** |
| **Tension** | รอยฉีกทำหน้าที่เป็น **ลิ้นทางเดียว** ลมเข้าแต่ไม่ออก → ความดันในช่องอกสูง → **กด mediastinum และ IVC** → เลือดกลับหัวใจลด → **obstructive shock** |

### สาเหตุ
**Spontaneous**
- **Primary** — ไม่มีโรคปอด ชายผอมสูง สูบบุหรี่ มี **bleb/bullae** ที่ยอดปอด · กรรมพันธุ์ **Marfan, Ehlers–Danlos** · กลายเป็น tension 1–2%
- **Secondary** — มีโรคปอดเดิม: **COPD** (พบบ่อยที่สุด), cystic lung disease, มะเร็งปอด, **pneumonia/วัณโรค** — อาการหนักกว่าเพราะปอดสำรองน้อย

**Traumatic**
- **Iatrogenic** — **ใส่ central line (subclavian), barotrauma จากเครื่องช่วยหายใจ, เจาะปอด**, CPR, bronchoscopy, ใส่ pacemaker, intercostal nerve block
- **Non-iatrogenic** — บาดเจ็บทรวงอก (ทั้งแทงทะลุและกระแทก) **ซี่โครงหัก** ดำน้ำ/บิน (ความดันเปลี่ยนเร็ว)
- Traumatic pneumothorax กลายเป็น **tension ราว 20%** และมากกว่านั้นใน **ผู้ป่วยที่ใช้เครื่องช่วยหายใจ** (แรงดันบวกอัดลมเข้าทุกครั้ง)

### อาการและอาการแสดง
- เจ็บหน้าอก **ฉับพลัน** ข้างเดียว แหลม pleuritic **ไม่ร้าว ไม่สัมพันธ์การออกแรง** · หอบตั้งแต่เล็กน้อยถึงหายใจล้มเหลว
- ตรวจ: expansion ↓ · breath sound ↓/หาย · **hyperresonance** · subcutaneous emphysema
- **Tension** เพิ่ม: **trachea เบี่ยงไปฝั่งตรงข้าม · ความดันต่ำ · หลอดเลือดดำที่คอโป่ง · เขียว**

> **Tension pneumothorax วินิจฉัยทางคลินิก — ห้ามรอเอกซเรย์** (ข้อที่ออกสอบทุกรุ่น)

### เอกซเรย์ทรวงอก
- เส้น **visceral pleural line** บาง คม สีขาว · **ไม่มี lung marking** นอกเส้นนี้
- ช่องซี่โครงกว้าง ปริมาตรข้างนั้นเพิ่ม
- **Mediastinum/trachea ถูกดันไปฝั่งตรงข้าม** → สงสัย tension
- อาจเห็น subcutaneous emphysema และ pneumomediastinum
- ท่านอนหงาย: **deep sulcus sign** (ลมลอยไปด้านหน้าและล่าง)

### อัลตราซาวด์ (E-FAST) — เร็วและทำข้างเตียงได้
| สัญญาณ | ความหมาย |
|---|---|
| **มี lung sliding** | **ตัด pneumothorax ได้ 100%** ณ จุดที่วาง probe |
| Loss of lung sliding | เยื่อหุ้มปอดสองชั้นแยกกัน — **ไม่จำเพาะ**: pneumothorax, effusion, emphysema, pleurodesis, ใส่ท่อลงหลอดลมข้างเดียว |
| **Barcode / stratosphere sign** (M-mode) | ไม่มีการเคลื่อน |
| Loss of lung pulse | — |
| **Lung point** | จุดเปลี่ยนระหว่างมีกับไม่มี sliding = **จำเพาะ ~100%** ยืนยัน pneumothorax |

### Case ในสไลด์
ชาย 47 ปี หลังติด COVID 1 เดือน ไอแห้งตลอด 1 สัปดาห์ก่อนมาไอแล้วเจ็บอกขวา · PR 113 RR 22 **SpO₂ 92%** · **trachea อยู่กลาง ไม่มีคอโป่ง** · ขวา expansion ↓ BS ↓ **hyperresonance** fremitus ↓ → **pneumothorax ขวา ไม่ใช่ tension** (post-COVID ทำให้เกิด cyst/bulla และ secondary pneumothorax ได้)""",
    ["Tension PTX วินิจฉัยทางคลินิก — trachea เบี่ยง + BP ตก + JVP โป่ง → ห้ามรอฟิล์ม",
     "US: มี lung sliding = ตัด PTX ได้ · lung point = ยืนยัน",
     "Iatrogenic: subclavian line, barotrauma, thoracentesis · บนเครื่องช่วยหายใจกลายเป็น tension ง่าย"],
    [bank("CH-OLD-28"),
     mcq(N(11), "A 70-year-old man on mechanical ventilation suddenly becomes hypotensive (BP 70/40 mmHg) with rising peak airway pressures. Bedside ultrasound of the right anterior chest shows absent lung sliding and a 'barcode' pattern on M-mode; a lung point is seen in the right lateral chest. Which statement is correct?",
         ["Absent lung sliding alone confirms pneumothorax", "The lung point confirms pneumothorax; decompress immediately without waiting for a chest radiograph",
          "Lung point indicates a pleural effusion", "Ultrasound cannot diagnose pneumothorax in ventilated patients", "Obtain a CT chest before any intervention"], 1,
         "สไลด์ — **loss of lung sliding ไม่จำเพาะ** (เกิดได้จาก effusion, emphysema, pleurodesis) แต่ **lung point** คือจุดที่ปอดยังแตะผนังสลับกับส่วนที่มีลม = **ยืนยัน pneumothorax** · ส่วน **มี lung sliding = ตัดได้ 100%**\n\nผู้ป่วยใช้เครื่องช่วยหายใจ ความดันในทางเดินหายใจพุ่ง ความดันต่ำ = **tension pneumothorax** → **needle decompression แล้วตามด้วย chest drain ทันที** · การส่ง CT หรือรอฟิล์มอาจทำให้หัวใจหยุดเต้น",
         "Lung point = ยืนยัน · บนเครื่องช่วยหายใจ + BP ตก = decompress เลย", "Ultrasound in pneumothorax",
         ["สไลด์ อ.สกล — Ultrasound, Absent of lung sliding, Lung point sign"], ["2.2.14", "2.3.10(6)", "3.1.19"]),
     mcq(N(12), "Which of the following patients has a SECONDARY spontaneous pneumothorax?",
         ["A 20-year-old tall smoker with no lung disease", "A 45-year-old man after subclavian central venous catheter insertion",
          "A 66-year-old man with severe COPD", "A 30-year-old man after a motorcycle crash with rib fractures", "A 28-year-old scuba diver after a rapid ascent"], 2,
         "สไลด์แบ่ง — **Primary**: ไม่มีโรคปอด (bleb/bullae, Marfan) · **Secondary**: **มีโรคปอดเดิม** — **COPD**, cystic lung disease, มะเร็งปอด, pneumonia/TB · **Traumatic**: iatrogenic (central line, barotrauma, thoracentesis) หรือบาดเจ็บ/ความดันเปลี่ยน (อุบัติเหตุ ดำน้ำ)\n\nการแยกนี้สำคัญเพราะ secondary pneumothorax **อาการหนักกว่า และต้องรับไว้ใส่สายระบายเกือบทุกราย** แม้ขนาดเล็ก",
         "Secondary = มีโรคปอดเดิม (COPD พบบ่อยสุด) → admit", "Classification of pneumothorax",
         ["สไลด์ อ.สกล — Spontaneous pneumothorax, Traumatic pneumothorax"], ["2.3.10(6)", "B6.2.3(4)"])],
    ["2.3.10(6)", "2.2.14", "B6.2.3(4)", "3.2.1"])

# ───────────────────────────── 8
sec("chest-rp-08", "รักษา pneumothorax ตาม BTS 2023 — ดูอาการ ไม่ใช่ขนาด",
    "tension → decompress + drain · primary ไม่มีอาการ → สังเกต · secondary → admit + drain · ป้องกันซ้ำ", 9,
"""### Tension pneumothorax
1. **Needle decompression ทันที** (ช่องซี่โครงที่ 4–5 แนว anterior axillary line ในผู้ใหญ่ หรือช่องที่ 2 mid-clavicular line)
2. ตามด้วย **intercostal chest drain ต้องใส่เสมอ** (สไลด์: *chest drain ต้องเข้า!*)
3. **Suction ไม่จำเป็นทุกราย**
4. ใส่สายใน **safety triangle** — ขอบหน้า pectoralis major · ขอบหน้า latissimus dorsi · แนวช่องซี่โครงที่ 5 (ระดับหัวนม) · ยอดอยู่ใต้รักแร้

### Non-tension — หลักใหม่ของ BTS 2023 *(สไลด์ส่วนนี้ดึงไม่ได้ เรียบเรียงจากแนวทาง)*
ลายมือในสไลด์ — **ประเมินตามอาการ (subjective/clinical) ไม่ใช่ขนาดบนฟิล์ม**

| สถานการณ์ | แนวทาง |
|---|---|
| **Primary · อาการน้อย/ไม่มี · ไม่มี high-risk** | **Conservative** — ไม่ต้องเจาะ นัดติดตามด้วย CXR ได้แม้ขนาดใหญ่ |
| **Primary · มีอาการ** | **Needle aspiration** หรือ ambulatory device หรือ chest drain ขนาดเล็ก |
| **Secondary** (มีโรคปอด) | **รับไว้ในโรงพยาบาล** · ส่วนใหญ่ **ใส่ chest drain** แม้ขนาดเล็ก |
| **High-risk features** | **chest drain** — hemodynamic ไม่คงที่, hypoxia รุนแรง, สองข้าง, มีโรคปอด, อายุ ≥ 50 ปีที่สูบบุหรี่, มีเลือดร่วม (hemopneumothorax) |
| **บนเครื่องช่วยหายใจ** | **ใส่ tube thoracostomy** เพราะแรงดันบวกเปลี่ยนเป็น tension ได้ |

### ป้องกันการเป็นซ้ำ
**ข้อบ่งชี้ผ่าตัด (VATS bullectomy + pleurodesis/pleurectomy)**
- เป็นซ้ำ **ข้างเดิมครั้งที่ 2** หรือเป็น **อีกข้าง**
- เป็นสองข้างพร้อมกัน
- **ลมรั่วไม่หยุด (persistent air leak) > 3–5 วัน**
- **อาชีพเสี่ยง** — นักบิน **นักดำน้ำ** หรือเคยเป็น tension

**คำแนะนำผู้ป่วย**
- **เลิกบุหรี่** (รวมกัญชา) — ลดการเป็นซ้ำมากที่สุดที่ทำได้เอง
- **ดำน้ำ scuba ห้ามตลอดชีวิต** เว้นแต่ผ่าตัด pleurectomy สองข้าง
- **ขึ้นเครื่องบิน** — รอจนเอกซเรย์ยืนยันว่าหายสนิท (แนวทางเดิมแนะนำอย่างน้อย 1 สัปดาห์หลังหาย)
- กลับมาพบแพทย์ทันทีถ้าหอบหรือเจ็บอกซ้ำ""",
    ["Tension: needle decompression → chest drain ต้องใส่เสมอ (suction ไม่จำเป็นทุกราย)",
     "BTS 2023: primary อาการน้อย → สังเกตได้แม้ขนาดใหญ่ · secondary → admit + drain",
     "ผ่าตัดเมื่อ: ซ้ำข้างเดิม/อีกข้าง · air leak > 3–5 วัน · อาชีพนักบิน/นักดำน้ำ",
     "เลิกบุหรี่ · scuba ห้ามถาวร"],
    [bank("CH-MCQ-18"), bank("CH-MCQ-24"), bank("CH-OLD-29"),
     mcq(N(13), "A 21-year-old man has had mild right chest discomfort for 2 days. He is not breathless, SpO2 98% on room air, BP 118/70 mmHg. He has no lung disease and does not smoke. Chest radiograph shows a 3-cm apical-to-cupola right primary spontaneous pneumothorax without mediastinal shift. According to the BTS 2023 guideline, what is the most appropriate management?",
         ["Immediate needle decompression", "Large-bore chest drain with suction",
          "Conservative management with outpatient follow-up and clear advice to return if symptoms worsen",
          "Video-assisted thoracoscopic surgery with pleurodesis now", "Admit for high-flow oxygen for 72 hours in all cases"], 2,
         "BTS 2023 เปลี่ยนแกนการตัดสินใจจาก **ขนาด** เป็น **อาการ** (ลายมือในสไลด์: ประเมินตามอาการ) — **primary spontaneous pneumothorax ที่อาการน้อยและไม่มี high-risk feature** ดูแลแบบ **conservative** ได้ แม้ขนาดใหญ่ โดยนัดตรวจซ้ำและให้คำแนะนำชัดเจน\n\nHigh-risk features ที่ต้องเปลี่ยนแผน: hemodynamic ไม่คงที่ · hypoxia รุนแรง · สองข้าง · มีโรคปอดเดิม · อายุ ≥ 50 ที่สูบบุหรี่ · hemopneumothorax\n\nผ่าตัดยังไม่ข้อบ่งชี้ในครั้งแรก เว้นแต่อาชีพเสี่ยง",
         "Primary PTX อาการน้อย ไม่มี high-risk → conservative ได้ (BTS 2023)", "BTS 2023 – primary spontaneous pneumothorax",
         ["BTS Guideline for Pleural Disease 2023 (Thorax 2023;78:s1–s42)", "สไลด์ อ.สกล — Management (ลายมือ subjective/clinical)"], ["2.3.10(6)", "B6.2.3(4)"])],
    ["2.3.10(6)", "2.2.14"])

# ───────────────────────────── 9
sec("chest-rp-09", "Pleural effusion — น้ำมาจากไหน และเห็นได้เมื่อมีเท่าไร",
    "น้ำปกติ ~10 mL · Starling กับ permeability · ปริมาณที่เห็นในแต่ละท่า · สัญญาณอัลตราซาวด์", 8,
"""### น้ำในช่องเยื่อหุ้มปอดปกติ
ใส **0.1–0.2 mL/kg (≈ 10 mL)** · เซลล์ < 1,700/µL — **macrophage 75%** · lymphocyte 23% · mesothelial, neutrophil, eosinophil อย่างละ < 2%
สร้างจากหลอดเลือด parietal pleura และ **ดูดกลับทาง lymphatic ของ parietal pleura** — ระบบนี้รับได้มากกว่าที่สร้างปกติถึง 20 เท่า น้ำจึงสะสมเมื่อสร้างเกินมาก หรือทางระบายอุดตัน

### สาเหตุตามกลไก
| กลไก | ชนิด | ตัวอย่าง |
|---|---|---|
| **Hydrostatic ↑** | Transudate | **หัวใจล้มเหลว** |
| **Oncotic ↓** | Transudate | **albumin ต่ำ** (ตับแข็ง nephrotic) |
| **Permeability ↑** | Exudate | **parapneumonic**, วัณโรค, **มะเร็ง**, autoimmune |
| **รั่วจากอวัยวะข้างเคียง** | ได้ทั้งสองแบบ | หลอดอาหารแตก, **thoracic duct** (chylothorax), **ascites** (hepatic hydrothorax), pancreatic pseudocyst, urinothorax |
| **ดูดกลับลด** | Exudate | lymphatic อุด (มะเร็ง), venous ↑ |

### ต้องมีน้ำเท่าไรถึงเห็น
| ท่า/ภาพ | ปริมาณขั้นต่ำ |
|---|---|
| **Lateral decubitus** | **2–10 mL** — ไวที่สุดในฟิล์มธรรมดา |
| Lateral | 25–75 mL (posterior costophrenic sulcus > 75) |
| **PA upright** | **150–500 mL** (lateral costophrenic angle ทื่อ > 150) |
| Supine/AP | ~500 mL (อาจต้อง 175–500 mL) — ดูเป็นฝ้าทั้งข้าง |

**ลักษณะบนฟิล์ม** — **meniscus sign** (ขอบโค้งเว้าขึ้นที่ปอดล่าง) · น้ำมากดัน mediastinum ไปฝั่งตรงข้าม · **lamellar effusion** แถบบางใต้ visceral pleura (CHF, lymphangitic carcinomatosis) · **loculated** ทำมุมป้านกับผนังอก ขอบเรียบ ไม่ไหลตามท่า · **subpulmonic** ดูเหมือนกะบังลมยกสูง

> ถ้าฝ้าทั้งข้าง: **mediastinum ถูกดันไปฝั่งตรงข้าม = น้ำมาก** · **ดึงเข้าหา = ปอดแฟบ (เช่นเนื้องอกอุดหลอดลม)** · อยู่กลาง = น้ำร่วมกับปอดแฟบ หรือ trapped lung

### อัลตราซาวด์ — ไวกว่าฟิล์มและใช้นำทางเจาะ
| สัญญาณ | ความหมาย |
|---|---|
| **Spine sign** | เห็นกระดูกสันหลังเลยกะบังลมขึ้นไป = มีน้ำ (ปกติลมบัง) |
| **Jellyfish sign** | ปอดแฟบลอยไปมาในน้ำ |
| **Sinusoid sign** (M-mode) · **Quad sign** | ยืนยันน้ำอิสระ |
| **Plankton / swirling sign** | มีเศษลอย = exudate, เลือด, หนอง |
| **Hematocrit sign** | ชั้นตะกอนแยก = เลือด |
| **Septation/loculation** | **exudate** (parapneumonic, TB) |

**ปริมาตรโดยประมาณ (mL) ≈ ระยะห่างสูงสุดของเยื่อสองชั้น (mm) × 20**""",
    ["Transudate = Starling (CHF, albumin ต่ำ) · exudate = permeability หรือ lymphatic อุด",
     "Lateral decubitus เห็นน้ำ 2–10 mL · PA ต้อง 150–500 mL",
     "US: septation = exudate · ปริมาตร ≈ ระยะ (mm) × 20"],
    [mcq(N(14), "A chest radiograph shows complete opacification of the left hemithorax. Which finding most strongly suggests that the opacity is caused by a massive pleural effusion rather than collapse of the left lung?",
         ["Air bronchograms within the opacity", "The trachea and mediastinum are shifted to the RIGHT",
          "The trachea and mediastinum are shifted to the LEFT", "Elevation of the left hemidiaphragm", "Narrowing of the left intercostal spaces"], 1,
         "สไลด์ — น้ำมากทำให้ **ปริมาตรข้างนั้นเพิ่ม (volume gain)** → **ดัน mediastinum ไปฝั่งตรงข้าม** · ปอดแฟบทำให้ **ปริมาตรลด** → **ดึง** mediastinum เข้าหา กะบังลมยก ช่องซี่โครงแคบ\n\nถ้าฝ้าทั้งข้างแต่ mediastinum อยู่กลาง ให้คิดถึง **น้ำร่วมกับปอดแฟบจากก้อนอุดหลอดลม** หรือ mesothelioma ที่ตรึงทรวงอก\n\nAir bronchogram บอก consolidation ไม่ใช่น้ำ",
         "ฝ้าทั้งข้าง: ดันออก = น้ำ · ดึงเข้า = ปอดแฟบ", "Complete white-out hemithorax",
         ["สไลด์ อ.สกล — Meniscus sign, volume gain"], ["2.3.10(7)", "3.2.1"]),
     mcq(N(15), "Thoracic ultrasound in a patient with pneumonia and a pleural effusion shows multiple septations with swirling echogenic particles. What does this indicate?",
         ["A transudate due to heart failure", "The effusion is an exudate, likely a complicated parapneumonic effusion or empyema",
          "Pneumothorax", "Hepatic hydrothorax", "Lamellar effusion from lymphangitic carcinomatosis"], 1,
         "สไลด์ — **septation และ loculation บนอัลตราซาวด์ → exudate** · **plankton/swirling sign** = มีอนุภาคลอย (เซลล์ โปรตีน หนอง เลือด)\n\nในบริบท pneumonia คือ **complicated parapneumonic effusion/empyema** — fibrin จากการอักเสบสร้างผนังกั้นเป็นช่อง → ต้องเจาะตรวจและมักต้องใส่สายระบาย ± ยาละลายลิ่มเลือดในช่องเยื่อหุ้มปอด\n\nTransudate มักเป็นน้ำใสไม่มีเสียงสะท้อน (anechoic) ไม่มีผนังกั้น",
         "Septation บน US = exudate · ใน pneumonia คิดถึง empyema", "Thoracic ultrasound signs",
         ["สไลด์ อ.สกล — Ultrasound: exudate, plankton sign, loculation"], ["2.3.10(7)", "2.3.10-3(2)"])],
    ["2.3.10(7)", "B6.2.2(10)", "3.2.1"])

# ───────────────────────────── 10
sec("chest-rp-10", "เมื่อไรต้องเจาะ และ work up ตาม BTS 2023",
    "ข้างเดียว/สองข้างไม่เท่ากัน/ไม่รู้สาเหตุ · ทำใต้อัลตราซาวด์เสมอ · สงสัยมะเร็ง → CT ก่อนเจาะ · ภาวะแทรกซ้อน", 9,
"""### ข้อบ่งชี้ของ thoracentesis
- น้ำ **ข้างเดียว** — โดยเฉพาะ **ข้างซ้าย** (ไม่ใช่รูปแบบของหัวใจล้มเหลว)
- **สองข้างแต่ไม่เท่ากัน** (discordant)
- **ไม่รู้สาเหตุ** · หรือ **ไม่ตอบสนอง** ต่อการรักษาสาเหตุ (เช่นให้ยาขับปัสสาวะแล้วไม่ลด) · มีไข้หรือเจ็บอกแบบ pleuritic
- **Therapeutic** เพื่อลดอาการหอบ
- ต้อง **ปลอดภัย** และ **ทำใต้อัลตราซาวด์เสมอ** (ลด pneumothorax และเลือดออก)

> หัวใจล้มเหลว **น้ำสองข้าง ขวามากกว่าซ้าย** ไม่มีไข้ — ไม่ต้องเจาะ ให้ยาขับปัสสาวะแล้วดู

### ลำดับตาม BTS 2023 (สรุปของ อ.สกล: **สงสัยมะเร็งไหม → เจาะได้ไหม**)
**1. ประวัติ ตรวจร่างกาย CXR + อัลตราซาวด์ทรวงอก**

**2. สงสัยมะเร็ง?**
- **ใช่** → **CT thorax/abdomen/pelvis ฉีดสี ก่อน เจาะระบายหมด** (ภาพชัดกว่าตอนยังมีน้ำ) → เจาะใต้ US ส่ง cytology, protein, LDH, glucose, pH, MC&S · ถ้าเห็นตำแหน่งชัด **ทำ US-guided cutting needle biopsy ในคราวเดียว** · เคยสัมผัส **asbestos สงสัย mesothelioma → thoracoscopy เลย**
- **ไม่** → เจาะใต้ US ส่งตรวจชุดเดียวกัน + เลือด **CRP, CBC, renal, LFT, albumin** → CT thorax ถ้าไม่ใช่การติดเชื้อชัด

**3. ยังไม่พบสาเหตุ** → image-guided pleural biopsy หรือ **thoracoscopy** · PET บางราย · คิดถึงโรคที่รักษาได้ซ้ำอีกครั้ง — **PE, TB, หัวใจล้มเหลว, lymphoma**

### Box 1 — ส่งตรวจเพิ่มตามโรคที่สงสัย
| สงสัย | ส่งตรวจ |
|---|---|
| Chylothorax | **triglyceride, cholesterol** ในน้ำ |
| Hemothorax | **Hematocrit** ในน้ำ |
| Empyema | **glucose, pH** |
| Rheumatoid | glucose |
| Pancreatitis | **amylase/lipase** |
| หัวใจล้มเหลว | **NT-proBNP** ในเลือด |
| Lymphoma | lymphocyte subsets (flow cytometry) |
| Autoimmune | autoimmune screen · IgG4 disease → pleural biopsy + IgG4 · amyloid → Congo red |

### ภาวะแทรกซ้อนของการเจาะที่ออกสอบ
| ภาวะ | ลักษณะ | ทำอย่างไร |
|---|---|---|
| **Vasovagal** | หน้ามืด เหงื่อ **ชีพจรช้า** ความดันต่ำ ฟังปอดเท่ากัน | หยุด นอนยกขา ± atropine |
| **Pneumothorax** | หอบขึ้น เสียงหายใจหาย | CXR, ระบายถ้ามาก |
| **Re-expansion pulmonary edema** | ไอ แน่นอก hypoxia ฝ้าใหม่ **ข้างที่เจาะ** หลังระบายเร็ว/มาก | O₂ ประคับประคอง |
| **Hemothorax** | ถูก intercostal artery | แทงชิดขอบบนซี่โครงล่าง |

**ป้องกัน re-expansion edema** — **หยุดเมื่อแน่นอก ไอ หรือเจ็บ** และไม่ระบายเกิน **~1.5 L ต่อครั้ง**""",
    ["เจาะเมื่อ: ข้างเดียว (โดยเฉพาะซ้าย) · สองข้างไม่เท่ากัน · ไม่รู้สาเหตุ · ใต้ US เสมอ",
     "BTS 2023: สงสัยมะเร็ง → CT ฉีดสีก่อนระบายหมด · asbestos → thoracoscopy",
     "Vasovagal: ชีพจรช้า ปอดเท่ากัน · re-expansion edema: ฝ้าข้างที่เจาะ → หยุดที่ ~1.5 L หรือเมื่อแน่นอก"],
    [bank("CH-MCQ-21"), bank("CH-OLD-30"), bank("CH-OLD-31")],
    ["2.3.10(7)", "B6.3(1)", "3.1.7"])

# ───────────────────────────── 11
sec("chest-rp-11", "Light's criteria และอ่านน้ำให้ออกว่าคืออะไร",
    "exudate ถ้าเข้าเกณฑ์ข้อใดข้อหนึ่ง · ได้ยาขับปัสสาวะใช้ albumin gradient · chylothorax · TB · amylase · glucose ต่ำ", 11,
"""*(ตารางส่วนนี้อยู่ในสไลด์ช่วงที่ดึงข้อความไม่ได้ — เรียบเรียงจาก BTS 2023 และคลังข้อสอบคาบ 17)*

### Light's criteria — **exudate ถ้าเข้าข้อใดข้อหนึ่ง**
| เกณฑ์ | จุดตัด |
|---|---|
| Pleural protein / serum protein | **> 0.5** |
| Pleural LDH / serum LDH | **> 0.6** |
| Pleural LDH | **> 2/3 ของค่าสูงสุดปกติของ LDH ในเลือด** |

> ข้อสอบชอบให้ **คำนวณให้เห็นตัวเลขในคำตอบ** — เขียนอัตราส่วนทุกข้อแล้วสรุป

**จุดอ่อน** — ไวมาก จึงเรียก transudate เป็น exudate ได้ราว 25% โดยเฉพาะ **หัวใจล้มเหลวที่ได้ยาขับปัสสาวะ** → ใช้ตัวช่วย
- **Serum − pleural albumin gradient > 1.2 g/dL** → transudate
- Serum − pleural protein gradient > 3.1 g/dL
- **NT-proBNP ในเลือดสูง** สนับสนุนหัวใจล้มเหลว

### Transudate — สาเหตุที่พบบ่อย
**หัวใจล้มเหลว** (สองข้าง ขวามากกว่า) · **ตับแข็ง (hepatic hydrothorax ขวา ~85%)** · nephrotic syndrome · hypoalbuminemia · peritoneal dialysis

### Exudate — อ่านตามลักษณะเฉพาะ
| ลักษณะ | คิดถึง |
|---|---|
| **Lymphocyte เด่น > 50%** | **วัณโรค**, มะเร็ง, lymphoma, หลังผ่าตัดหัวใจ |
| Lymphocyte เด่น + **ADA > 40 U/L** + mesothelial น้อย | **วัณโรคเยื่อหุ้มปอด** — เริ่มยาได้เลยในพื้นที่ชุก (ดูคาบ EPTB) |
| **Neutrophil เด่น** | **parapneumonic**, PE, pancreatitis |
| **Eosinophil > 10%** | ลมหรือเลือดในช่องอก (หลังเจาะ), ยา, parasite, Churg–Strauss |
| **ขุ่นขาวเหมือนนม** + **TG > 110 mg/dL** | **Chylothorax** (thoracic duct ฉีก — มะเร็ง lymphoma, ผ่าตัด, บาดเจ็บ) |
| ขุ่นขาว + **cholesterol > 200** + ผลึก cholesterol, TG ต่ำ | **Pseudochylothorax** — น้ำค้างนาน (RA, TB เก่า) |
| **Hct น้ำ ≥ 50% ของเลือด** | **Hemothorax** → ใส่สายระบาย |
| **Glucose ต่ำ < 60 mg/dL** | **empyema, rheumatoid (ต่ำมาก < 30), TB, มะเร็ง**, lupus, หลอดอาหารแตก |
| **Amylase สูง** | **pancreatitis/pseudocyst, หลอดอาหารแตก** (salivary amylase, pH ~6), มะเร็ง |
| Cytology บวก | malignant effusion (ไวราว 60% ในการเจาะครั้งแรก) |

### Hepatic hydrothorax — ข้อควรระวัง
น้ำในท้องรั่วผ่านรูเล็กของกะบังลม (ขวา) → **transudate** · รักษาที่ ascites: **จำกัดเกลือ + ยาขับปัสสาวะ** ± TIPS · **ห้ามใส่ chest drain** (เสียโปรตีน ติดเชื้อ ไตวาย)""",
    ["Light: protein ratio > 0.5 · LDH ratio > 0.6 · LDH > 2/3 ULN → ข้อเดียวก็ exudate",
     "ได้ยาขับปัสสาวะแล้วเป็น exudate → albumin gradient > 1.2 = จริง ๆ เป็น transudate",
     "TG > 110 = chylothorax · Hct ≥ 50% ของเลือด = hemothorax · glucose ต่ำมาก = RA/empyema",
     "Hepatic hydrothorax: ห้ามใส่ chest drain"],
    [bank("CH-OLD-27"), bank("CH-OLD-23"), bank("CH-MCQ-20"), bank("CH-OLD-25"), bank("CH-OLD-34"), bank("CH-MCQ-19"),
     mcq(N(16), "A 74-year-old man with heart failure has been on furosemide 80 mg/day for 5 days. Pleural fluid: protein 3.2 g/dL (serum 6.0), LDH 150 U/L (serum 240; upper limit of normal 250), albumin 1.4 g/dL (serum 2.9 g/dL). Serum NT-proBNP is 6,800 pg/mL. How should this effusion be interpreted?",
         ["Exudate; perform thoracoscopic pleural biopsy", "Exudate from tuberculosis; start anti-tuberculous therapy",
          "A transudate due to heart failure, misclassified by Light's criteria because of diuretic therapy",
          "Malignant effusion until proven otherwise", "Chylothorax"], 2,
         "Light's criteria: protein ratio 3.2/6.0 = **0.53 (> 0.5 → exudate)** · LDH ratio 150/240 = 0.63 (> 0.6) · LDH 150 < 2/3 × 250 (167) → เข้าเกณฑ์ exudate สองข้อแบบหมิ่นเหม่\n\nแต่ผู้ป่วย **ได้ยาขับปัสสาวะ** ซึ่งดึงน้ำออกมากกว่าโปรตีน ทำให้น้ำในช่องอกเข้มข้นขึ้น → **Light's criteria เรียก transudate เป็น exudate** ราว 25%\n\nตัวช่วย: **serum − pleural albumin gradient = 2.9 − 1.4 = 1.5 g/dL (> 1.2) → transudate** และ **NT-proBNP สูงมาก** สนับสนุนหัวใจล้มเหลว → ปรับยารักษาหัวใจ ไม่ต้องทำหัตถการเพิ่ม",
         "ได้ diuretic + exudate หมิ่นเหม่ → albumin gradient > 1.2 = transudate", "Pseudo-exudate in diuresed heart failure",
         ["BTS Guideline for Pleural Disease 2023", "สไลด์ อ.สกล — Box 1 (NT-proBNP)"], ["B6.3(1)", "3.1.7", "2.3.10(7)"])],
    ["B6.3(1)", "3.1.7", "2.3.10(7)", "B6.2.2(10)"])

# ───────────────────────────── 12
sec("chest-rp-12", "Parapneumonic effusion · empyema · malignant effusion — เมื่อไรต้องใส่สาย",
    "pH < 7.2 หรือหนอง หรือเชื้อบวก = ระบาย · tPA + DNase · VATS · ซ้ำในมะเร็ง → IPC หรือ talc", 10,
"""*(สไลด์ส่วนนี้ดึงข้อความไม่ได้ — เรียบเรียงจาก BTS 2023 ที่อาจารย์ใช้เป็นแกน)*

### Parapneumonic effusion สามระยะ
| ระยะ | ลักษณะน้ำ | การรักษา |
|---|---|---|
| **Uncomplicated** (exudative) | ใส pH > 7.2 glucose ปกติ ไม่พบเชื้อ | **ยาปฏิชีวนะอย่างเดียว** |
| **Complicated** (fibrinopurulent) | **pH < 7.2**, glucose < 40–60 mg/dL, LDH > 1,000, **เชื้อบวกจาก Gram/culture**, มีผนังกั้น | **ยาปฏิชีวนะ + chest drain** |
| **Empyema** (organizing) | **หนองชัด** | **chest drain** ± ยาละลาย ± ผ่าตัด |

**ข้อบ่งชี้ใส่ chest drain** — **หนองหรือขุ่นมาก · Gram stain/culture บวก · pH < 7.2** (ถ้าไม่มีเครื่องวัด pH ใช้ glucose < 72 mg/dL)
- ใช้ **สายขนาดเล็ก (12–14 F)** ใต้อัลตราซาวด์ได้ผลไม่ด้อยกว่าสายใหญ่
- ระบายไม่ออก/ยังเป็นช่อง → **intrapleural tPA 10 mg + DNase 5 mg วันละ 2 ครั้ง 3 วัน** (MIST-2) หรือ **VATS decortication**
- ยาปฏิชีวนะต้อง **ครอบคลุม anaerobe** (เช่น amoxicillin-clavulanate หรือ ceftriaxone + metronidazole) · **หลีกเลี่ยง aminoglycoside** (ซึมเข้าหนองไม่ดี และไม่ทำงานในกรด) · ให้นานราว **2–6 สัปดาห์**
- ประเมินความเสี่ยงด้วย **RAPID score** (renal, age, purulence, infection source, dietary albumin)

### Malignant pleural effusion
- สาเหตุบ่อย: **มะเร็งปอด เต้านม** lymphoma · mesothelioma (asbestos)
- น้ำมักเป็นเลือดปน lymphocyte/mononuclear เด่น glucose อาจต่ำ · cytology ครั้งแรกไวราว 60% ไม่พบอย่าตัดทิ้ง → biopsy
- **น้ำกลับมาซ้ำและมีอาการ** → เลือกตาม **ปอดขยายได้หรือไม่**
  - ปอดขยายได้ → **talc pleurodesis** (slurry ทางสาย หรือ poudrage ทาง thoracoscopy) **หรือ indwelling pleural catheter (IPC)**
  - **ปอดขยายไม่ได้ (trapped lung)** → **IPC** (pleurodesis จะไม่ติด)
- ไม่เจาะระบายซ้ำ ๆ ไปเรื่อย ๆ — ทุกครั้งเสี่ยง และน้ำกลับมาใน 1–2 สัปดาห์

### ภาวะอื่นที่ต้องระบายทันที
**Hemothorax** (Hct น้ำ ≥ 50% ของเลือด) · **empyema** · **pneumothorax** ที่มีอาการหรือบนเครื่องช่วยหายใจ""",
    ["ใส่ chest drain เมื่อ: หนอง/ขุ่น · Gram/culture บวก · pH < 7.2",
     "ระบายไม่ออก → tPA + DNase หรือ VATS · ยาครอบคลุม anaerobe ไม่ใช้ aminoglycoside",
     "Malignant effusion ซ้ำ: ปอดขยายได้ → talc หรือ IPC · trapped lung → IPC"],
    [bank("CH-OLD-24"), bank("CH-MCQ-17"), bank("CH-OLD-26"), bank("CH-MCQ-23")],
    ["2.3.10-3(2)", "2.3.10(7)", "B6.3(1)", "B6.2.4-3(2)"])


LECNAME = "Pleural disease / Respiratory failure (อ.สกล)"
MEQ = [bank_case("CH-MEQ-03")]
OSCE = [bank_case("CH-OSCE-02"), bank_case("CH-OSCE-04")]
for m in MEQ + OSCE:
    m["lecture"] = LECNAME

LECTURE = {
 "lec": "17",
 "date": "จ. 28 ก.ย.",
 "title": "Respiratory failure and Pleural disease",
 "subtitle": "DO₂ และ O₂ curve · hypoxia สี่แบบ · A-a gradient · shunt dead space diffusion · respiratory failure สี่ชนิด ออกซิเจน NIV และเกณฑ์ใส่ท่อ · เจ็บอกจากปอดและตรวจร่างกาย · pneumothorax วินิจฉัยและรักษาตาม BTS 2023 · effusion เจาะเมื่อไร Light's criteria อ่านน้ำ · empyema และ malignant effusion",
 "objectives": [
   "คำนวณ oxygen content และอธิบายว่าทำไม Hb และ CO สำคัญกว่า PaO₂ ในการส่งออกซิเจน รวมถึงปัจจัยที่เลื่อน O₂ dissociation curve",
   "แยก hypoxia สี่แบบ และรู้ว่าเมื่อไร SpO₂ เชื่อไม่ได้ (saturation gap, CO, MetHb)",
   "คำนวณ A-a gradient และใช้แยก hypoventilation ออกจากโรคในเนื้อปอด",
   "อธิบาย V/Q mismatch, shunt, dead space และ diffusion limitation พร้อมการตอบสนองต่อออกซิเจน",
   "จำแนก respiratory failure สี่ชนิด เลือกอุปกรณ์ออกซิเจน/HFNC/NIV และบอกเกณฑ์ใส่ท่อช่วยหายใจ",
   "วินิจฉัย pneumothorax และ tension pneumothorax ทางคลินิก เอกซเรย์ และอัลตราซาวด์ แล้วรักษาตาม BTS 2023",
   "บอกข้อบ่งชี้และภาวะแทรกซ้อนของ thoracentesis แปลผลน้ำด้วย Light's criteria และตรวจพิเศษ และวางแผนรักษา empyema และ malignant effusion"],
 "nlGap": "**ข้อความในสไลด์ถูกตัดหลังหัวข้อ work up pleural effusion** (เครื่องมือดึงข้อความได้ไม่ครบ) — ส่วนท้ายของคาบได้แก่ **Light's criteria · การอ่านน้ำชนิดต่าง ๆ · parapneumonic/empyema · malignant effusion · การรักษา pneumothorax ที่ไม่ใช่ tension** เรียบเรียงจาก **BTS Guideline for Pleural Disease 2023** ที่อาจารย์ระบุเป็นแกนของคาบ ร่วมกับคลังข้อสอบคาบ 17 · เกณฑ์ฯ **ไม่มีรหัสของ HFNC, NIV หรือเกณฑ์ใส่ท่อช่วยหายใจ** โดยตรง (อยู่ใต้ `นล. 2.2.9`) และไม่มีรหัสของอัลตราซาวด์ทรวงอกนอกจาก FAST ในผู้บาดเจ็บ (`นล. 3.1.19`) จึงอิงแนวทางด้านล่าง ถ้าได้ภาพสไลด์ส่วนท้ายมา ให้เทียบแล้วแก้ `build_rfpleural.py`",
 "guidelines": [
   "**BTS Guideline for Pleural Disease 2023** (Thorax 2023;78:s1–s42 · doi 10.1136/thorax-2023-220304) — algorithm work up effusion, pneumothorax ตามอาการ, parapneumonic/empyema, malignant effusion (อาจารย์อ้างในสไลด์)",
   "**Light RW et al. Ann Intern Med 1972** — Light's criteria · serum–pleural albumin gradient สำหรับผู้ได้ยาขับปัสสาวะ",
   "**BTS Guideline for Oxygen Use in Adults 2017** — เป้า SpO₂ 94–98% / 88–92% และการเลือกอุปกรณ์",
   "**ERS/ATS 2017 — Noninvasive mechanical ventilation for acute respiratory failure** · **ERS 2022 — High-flow nasal cannula** (ROX index)",
   "**MIST-2 (NEJM 2011)** — intrapleural tPA + DNase ใน pleural infection"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ── ตรวจก่อนเขียน
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
    for i in s["items"]:
        assert len(i["choices"]) == 5 and 0 <= i["answer"] <= 4, i["id"]

data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "chest": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d | nl codes %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE), len(codes)))
print("chest.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
