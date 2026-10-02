#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thyroid disorders (อ.ศิวกร อินทร์คง · พ. 30 ก.ย. 2569) → data/endo.json
ต้นฉบับ: สไลด์ "Lec14 Thyroid disorder_2026" (Drive 1iq1YOO-vf-JF3vL40p1ppCmu-1eHnII5) — โน้ตที่ slides/thyroid_notes.md
ข้อความสไลด์ถูกตัดหลัง algorithm ของ thyroid nodule → ส่วน hypothyroidism, amiodarone, US pattern, Bethesda
เทียบจาก artifact บทเรียน Thyroid ของผู้ใช้ที่ทำจากสไลด์ชุดเดียวกัน + ATA 2014/2015/2016, ETA 2018, Bethesda 2023
Thyroid storm ไม่อยู่ในสไลด์ส่วนที่ดึงได้ → ใช้ ATA 2016 + JTA 2016 และระบุใน nlGap"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # artifact/
NLN = ["2.3.4(9)", "B11.2.5(2)"]
SRC = "สไลด์ อ.ศิวกร อินทร์คง — Thyroid disorders (2026)"
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

N = lambda n: "END-TH-MCQ-%02d" % n
R = lambda s: "สไลด์ อ.ศิวกร — " + s

# ───────────────────────────── 1
sec("endo-th-01", "ผู้จัดการกับโรงงาน — แกน HPT, deiodinase และทำไม TSH ไวที่สุด",
    "T4 คือ prohormone · T3 ออกฤทธิ์ · TSH วิ่งสวน FT4 แบบ log-linear · euthyroid sick syndrome", 7,
"""### แกน hypothalamus–pituitary–thyroid
**TRH → TSH (thyrotroph) → ต่อมไทรอยด์** สร้างฮอร์โมนส่วนใหญ่เป็น **T4** แล้วเนื้อเยื่อปลายทางเปลี่ยนเป็น **T3 ตัวออกฤทธิ์** ฮอร์โมนที่สูงขึ้นจะ **กดกลับ** TRH และ TSH (negative feedback)

ขั้นตอนในต่อม — **NIS ดูดไอโอดีน → TPO ทำ oxidation/organification → coupling บน thyroglobulin** → เก็บใน colloid → หลั่ง (ยา MMI/PTU ตัดที่ TPO)

| เอนไซม์ | หน้าที่ |
|---|---|
| **D1, D2** | T4 → **T3** (ออกฤทธิ์) |
| **D3** | T4 → **reverse T3** (ไม่ออกฤทธิ์ — ทางทิ้ง) |

### TSH คือเทอร์โมมิเตอร์ที่ไวที่สุด
TSH เปลี่ยนแบบ **log-linear** — FT4 ขยับนิดเดียว TSH เปลี่ยนเป็นสิบเท่า ถ้าต่อมใต้สมองปกติ **TSH วิ่งสวน FT4 เสมอ** จึงใช้ TSH คัดกรองโรคที่ตัวต่อม (primary)

**เมื่อไร TSH "โกหก"**
- **Central** (ต่อมใต้สมอง/hypothalamus เสีย) — FT4 ต่ำแต่ TSH ไม่สูงตาม
- **ช่วงรักษา hyperthyroidism** — TSH ถูกกดค้างหลายเดือนหลัง FT4 กลับปกติ → ปรับยาตาม FT4/T3
- **ป่วยหนัก** (euthyroid sick) และ **ยา** (steroid, dopamine กด TSH)

### Euthyroid sick syndrome (non-thyroidal illness)
ป่วยหนัก/อดอาหาร → **D1 ถูกกด** → **T3 ต่ำก่อน, rT3 สูง** → ป่วยหนักมาก T4 ต่ำตาม · TSH ปกติหรือต่ำเล็กน้อย และ **สูงชั่วคราวช่วงฟื้น**
> ไม่ส่ง TFT ใน ICU ถ้าไม่ได้สงสัยโรคไทรอยด์จริง และ **ไม่ให้ฮอร์โมนรักษาตัวเลข**

### โรคต่อมไร้ท่อมีแค่สี่แบบ (สไลด์เปิดคาบ)
ฮอร์โมน **สร้างเกิน** · **สร้างขาด** · **เนื้อเยื่อตอบสนองผิด** (เช่น insulin resistance ใน DM2) · **เนื้องอก**ของต่อม""",
    ["T4 = prohormone · D1/D2 → T3 · D3 → rT3",
     "TSH วิ่งสวน FT4 แบบ log-linear — แต่โกหกใน central, ช่วงรักษา hyperthyroid และป่วยหนัก",
     "Euthyroid sick: T3 ต่ำก่อน rT3 สูง — ไม่ให้ฮอร์โมน"],
    [mcq(N(1), "A 68-year-old man in the ICU with septic shock has a TSH of 0.4 mIU/L (0.3–4.1), FT4 0.9 ng/dL (0.8–1.8) and a low total T3 with high reverse T3. He has no goitre and no history of thyroid disease. What is the most appropriate interpretation and action?",
         ["Central hypothyroidism; start levothyroxine", "Non-thyroidal illness (euthyroid sick syndrome); do not treat, recheck after recovery",
          "Subclinical hyperthyroidism; start methimazole", "Primary hypothyroidism; start liothyronine (T3)", "T3 thyrotoxicosis; give propranolol"], 1,
         "ลายมือในสไลด์ — **ป่วยหนัก → deiodinase เปลี่ยน** → **D1 ถูกกด** ทำให้ T4 เปลี่ยนเป็น T3 น้อยลง และไปเป็น **reverse T3** แทน → **T3 ต่ำ rT3 สูง** TSH ปกติหรือต่ำเล็กน้อย\n\nนี่คือการปรับตัวลดการเผาผลาญ ไม่ใช่โรคต่อม — **ไม่ให้ฮอร์โมน** และตรวจซ้ำหลังหายป่วย (ช่วงฟื้น TSH อาจสูงขึ้นชั่วคราว อย่าเข้าใจผิดว่าเป็น hypothyroid)",
         "ICU + T3 ต่ำ rT3 สูง TSH ไม่สูง = euthyroid sick → ไม่รักษา", "Non-thyroidal illness syndrome",
         [R("TFT interpretation, deiodinase (Nat Rev Endocrinol 2019;15:479)")], ["B11.1.2(2)d", "B11.3(3)", "3.3.12"]),
     mcq(N(2), "A 30-year-old woman with Graves' disease has been taking methimazole for 6 weeks. She feels much better. FT4 is now 1.2 ng/dL (0.8–1.8) and FT3 is normal, but TSH remains < 0.01 mIU/L. What should be done with her methimazole dose?",
         ["Increase the dose because TSH is still suppressed", "Stop methimazole immediately",
          "Adjust the dose according to FT4 and T3, recognising that TSH may remain suppressed for months", "Add levothyroxine", "Switch to PTU"], 2,
         "สไลด์ส่วน Monitor — **วัด FT4 และ T3 ที่ 4–6 สัปดาห์** ลายมือกำกับว่า **TSH ฟื้นช้า** เพราะ thyrotroph ถูกกดมานาน ต้องใช้เวลาหลายเดือนกว่าจะกลับมาหลั่ง\n\nถ้าเพิ่มยาตาม TSH จะทำให้ผู้ป่วยกลายเป็น hypothyroid · FT4 ปกติแล้วจึง **คงหรือลดขนาด** แล้วค่อยใช้ TSH เมื่อ euthyroid ต่อเนื่อง",
         "ช่วงรักษา Graves: ปรับยาตาม FT4/T3 ไม่ใช่ TSH", "Monitoring antithyroid therapy",
         [R("Antithyroid drug – Monitor")], ["B11.4(2)", "B11.3(3)"])],
    ["B11.1.2(2)d", "B11.1.1(4)", "B11.3(3)"])

# ───────────────────────────── 2
sec("endo-th-02", "ถอดรหัส TFT ในห้านาที",
    "primary · T3 · T4 · subclinical thyrotoxicosis · inappropriate TSH · ตาราง TSH เมื่อ FT4 ต่ำ", 8,
"""### Thyrotoxicosis patterns (ตารางในสไลด์)
| FT3 | FT4 | TSH | แปลว่า | ลายมือ/ตัวอย่าง |
|---|---|---|---|---|
| ↑ | ↑ | ↓ | **Primary thyrotoxicosis** | Graves, thyroiditis |
| ↑ | ปกติ | ↓ | **T3 thyrotoxicosis** | **Graves ระยะแรก, Graves กำเริบ, toxic nodule** |
| ปกติ | ↑ | ↓ | **T4 thyrotoxicosis** | thyrotoxic **ร่วมกับป่วยหนัก** (D1 ถูกกด) · ได้ไอโอดีน/amiodarone |
| ปกติ | ปกติ | ↓ | **Subclinical thyrotoxicosis** | ระยะเริ่ม · ได้ฮอร์โมนเกิน |
| ↑ | ↑ | **ปกติหรือ ↑** | **Inappropriate TSH** | ตัด **assay interference** → **TSH-producing pituitary adenoma** → **resistance to thyroid hormone β** |

### Hypothyroid patterns — ตาราง TSH เมื่อ FT4 ต่ำ *(Williams 15th — ส่วน hypothyroid ของสไลด์ดึงข้อความไม่ได้)*
| TSH (mIU/L) | คิดถึง |
|---|---|
| **> 10** | **Primary hypothyroidism** |
| 5–10 | Primary ระยะเล็กน้อย หรือ central (TSH ที่ทำงานไม่เต็มที่) |
| **0.5–5** | **Central hypothyroidism** |
| < 0.5 | Central หรือ **หลังรักษา hyperthyroidism** (TSH ยังถูกกด) |

**Subclinical hypothyroidism** = TSH สูง FT4 ปกติ

### ลำดับการอ่าน
1. **TSH ก่อน** — ต่ำ / ปกติ / สูง
2. **FT4** — ไปทางเดียวกันหรือสวนกับ TSH
3. ถ้าสวนกันถูกทาง = **primary** · ถ้าไปทางเดียวกัน = **central** หรือ inappropriate TSH
4. **FT3** ช่วยแยก T3 toxicosis และ euthyroid sick""",
    ["TSH ต่ำ + FT3 สูง + FT4 ปกติ = T3 toxicosis (Graves ระยะแรก/กำเริบ, toxic nodule)",
     "FT4 สูง แต่ TSH ไม่ต่ำ: assay interference → TSH-oma → RTHβ",
     "FT4 ต่ำ + TSH ไม่สูง (0.5–5) = central — ตรวจแกนอื่นของต่อมใต้สมอง"],
    [mcq(N(3), "A 34-year-old woman has palpitations and tremor. FT4 2.6 ng/dL (0.8–1.8), FT3 7.0 pg/mL (1.6–4), TSH 3.8 mIU/L (0.3–4.1). She has headaches and bitemporal visual field loss. After excluding assay interference, what is the most likely diagnosis?",
         ["Graves' disease", "Subacute thyroiditis", "TSH-secreting pituitary adenoma", "Euthyroid sick syndrome", "Factitious thyrotoxicosis"], 2,
         "สไลด์ — **FT4/FT3 สูงแต่ TSH ไม่ต่ำ (inappropriate TSH)** → ตัด **assay interference** ก่อน แล้วคิดถึง **TSH-producing pituitary tumor** หรือ **resistance to thyroid hormone β**\n\nปวดศีรษะ + ลานสายตาด้านข้างเสียสองข้าง (bitemporal hemianopia จากก้อนกด optic chiasm) ชี้ไปที่ **TSH-oma** ชัดเจน → MRI pituitary, α-subunit\n\nGraves, thyroiditis และ factitious จะ **กด TSH จนต่ำ** เสมอ",
         "FT4 สูง + TSH ไม่ต่ำ + bitemporal hemianopia = TSH-oma", "Inappropriate TSH secretion",
         [R("TFT interpretation – Exclude assay interference, TSH-producing pituitary tumor, RTHβ")], ["B11.3(3)", "2.3.4-3(4)", "B11.2.4-3(1)"]),
     mcq(N(4), "A 29-year-old woman had severe postpartum haemorrhage 1 year ago and has not menstruated since. She is fatigued and cold-intolerant. FT4 0.5 ng/dL (0.8–1.8), TSH 1.2 mIU/L (0.3–4.1). Before starting levothyroxine, what must be assessed?",
         ["Thyroid peroxidase antibodies", "Thyroid ultrasound", "Morning cortisol (adrenal axis)", "Radioactive iodine uptake", "Serum thyroglobulin"], 2,
         "FT4 ต่ำแต่ **TSH ไม่สูงตาม (0.5–5)** = **central hypothyroidism** · ประวัติตกเลือดหลังคลอดแล้วไม่มีประจำเดือน = **Sheehan syndrome**\n\nต่อมใต้สมองเสียมักขาดหลายแกนพร้อมกัน **ต้องประเมินและแก้ cortisol ก่อน** — ถ้าให้ levothyroxine ก่อน การเผาผลาญเพิ่มจะเร่งการใช้ cortisol จน **adrenal crisis** ได้\n\nติดตามด้วย **FT4 (ครึ่งบนของค่าปกติ) ไม่ใช่ TSH**",
         "Central hypothyroid → เช็ค cortisol ก่อนให้ LT4", "Central hypothyroidism",
         ["Williams Textbook of Endocrinology 15th — TSH when FT4 is low", "ATA Hypothyroidism Guideline 2014"], ["2.3.4(4)", "B11.2.5(3)", "2.3.4-3(4)"])],
    ["B11.3(3)", "3.3.12"])

# ───────────────────────────── 3
sec("endo-th-03", "Thyrotoxicosis ≠ hyperthyroidism — โรงงานเร่ง หรือ โกดังแตก",
    "RAIU ปกติ 15–25% · สูงใน Graves · ใกล้ศูนย์ใน thyroiditis/factitious · ATD ช่วยเฉพาะโรงงานเร่ง", 8,
"""### นิยาม
- **Thyrotoxicosis** = ฮอร์โมนในเลือดเกิน **ไม่ว่ามาจากไหน**
- **Hyperthyroidism** = กรณีย่อยที่ **ต่อมผลิตเกินจริง**

### แยกด้วย radioactive iodine uptake (RAIU)
| RAIU | กลุ่ม | สาเหตุ |
|---|---|---|
| **ปกติหรือสูง** (ปกติ 15–25%) | **Hyperthyroidism** — โรงงานเร่ง | **Graves** (สูง > 30%) · **toxic multinodular goiter** · **toxic adenoma** · TSH-producing adenoma · **hCG**: hyperemesis gravidarum, trophoblastic disease |
| **เกือบศูนย์** (< 10%) | **Thyrotoxicosis without hyperthyroidism** — โกดังแตก/ของนอก | **thyroiditis** (painless, postpartum, subacute) · **factitious** (กิน levothyroxine — ลายมือ "TP") · struma ovarii · **ได้ไอโอดีนมากเมื่อเร็ว ๆ นี้** |

> **หลักจำ** — ยาต้านไทรอยด์ (ATD) ยับยั้ง **การสร้างใหม่** ถ้าฮอร์โมนมาจากของเก่าที่รั่วออกจาก follicle ที่แตก ให้ยาไปก็ไม่มีอะไรให้ยับยั้ง → thyroiditis รักษาด้วย **β-blocker ± ยาแก้อักเสบ** แล้วรอ

### ทริกแยก factitious
**ต่อมเล็ก ไม่โต · RAIU ต่ำ · thyroglobulin ในเลือดต่ำ** (ฮอร์โมนกินเข้าไปไม่มี Tg ตามมา ต่างจาก thyroiditis ที่ Tg สูงเพราะต่อมแตก)

### hCG กับ TSH receptor
hCG มี α-subunit เหมือน TSH กระตุ้น receptor ได้อ่อน ๆ → **ไตรมาสแรก/hyperemesis/ครรภ์ไข่ปลาอุก** ทำให้ TSH ต่ำ FT4 สูงเล็กน้อยได้ (gestational transient thyrotoxicosis — มักไม่ต้องใช้ ATD)""",
    ["RAIU สูง = โรงงานเร่ง (Graves, toxic nodule, hCG) · RAIU ~0 = thyroiditis, factitious, iodine",
     "ATD ไม่ช่วย thyroiditis — ใช้ β-blocker",
     "Factitious: ต่อมเล็ก + RAIU ต่ำ + Tg ต่ำ"],
    [mcq(N(5), "A 26-year-old nurse has weight loss, palpitations and tremor. Her thyroid is not palpable. FT4 is high, TSH is suppressed, 24-hour radioiodine uptake is 1%, and serum thyroglobulin is undetectable. What is the most likely diagnosis?",
         ["Graves' disease", "Painless (silent) thyroiditis", "Factitious ingestion of thyroid hormone", "Toxic adenoma", "Struma ovarii"], 2,
         "RAIU ใกล้ศูนย์ = **thyrotoxicosis without hyperthyroidism** (โกดังแตก หรือของจากนอก)\n\nแยกต่อ: **thyroiditis** — follicle แตกปล่อยทั้งฮอร์โมนและ **thyroglobulin** ออกมา → Tg **สูง** · **กินฮอร์โมนเอง** — ฮอร์โมนมาจากนอกต่อม ต่อมถูกกดจนเล็ก → Tg **ต่ำ/วัดไม่ได้**\n\nบุคลากรทางการแพทย์ที่เข้าถึงยาได้ + ต่อมคลำไม่ได้ + Tg ต่ำ = **factitious thyrotoxicosis**",
         "RAIU ~0 + Tg ต่ำ + ต่อมเล็ก = กินฮอร์โมนเอง", "Factitious thyrotoxicosis",
         [R("Etiology of thyrotoxicosis – factitious ingestion"), R("Radioactive iodine uptake")], ["2.3.4(9)", "B11.3(3)"]),
     mcq(N(6), "Which cause of thyrotoxicosis is associated with an INCREASED radioactive iodine uptake?",
         ["Postpartum thyroiditis", "Subacute (de Quervain) thyroiditis", "Recent iodinated contrast exposure", "Hydatidiform mole", "Factitious ingestion of levothyroxine"], 3,
         "สไลด์จัด **trophoblastic disease** และ **hyperemesis gravidarum** อยู่ฝั่ง **hyperthyroidism (RAIU ปกติหรือสูง)** เพราะ **hCG กระตุ้น TSH receptor** ให้ต่อมสร้างฮอร์โมนจริง\n\nตัวเลือกอื่น RAIU **เกือบศูนย์** — thyroiditis ทุกชนิด (เซลล์ถูกทำลาย), ไอโอดีนเกิน (เจือจางสารรังสี + กด uptake), factitious (ต่อมถูกกด)",
         "hCG (molar pregnancy, hyperemesis) = hyperthyroidism จริง RAIU ไม่ต่ำ", "Radioactive iodine uptake",
         [R("Etiology of thyrotoxicosis – normal/elevated RAIU vs nearly absent RAIU")], ["2.3.4(9)", "B11.3(3)"])],
    ["2.3.4(9)", "B11.2.5(2)", "B11.3(3)"])

# ───────────────────────────── 4
sec("endo-th-04", "อาการไทรอยด์เป็นพิษ — ทุกข้อไล่กลับไปหากลไกได้",
    "β-receptor · BMR · ลำไส้ · กล้าม · SHBG · ไต · apathetic thyrotoxicosis · gynecomastia", 7,
"""### Case เปิดคาบ
หญิง 35 ปี **น้ำหนักลด 1 เดือน** ใจสั่น มือสั่น ชีพจร **120 สม่ำเสมอ** · **lid lag, lid retraction**
FT4 **2** (0.8–1.8 ng/dL) · FT3 **6.5** (1.6–4 pg/mL) · TSH **< 0.001** (0.3–4.1) → **primary thyrotoxicosis**

> lid lag/retraction เกิดจาก adrenergic กระตุ้นกล้ามเนื้อ Müller — **พบได้ทุกสาเหตุ** ยังไม่ใช่หลักฐานของ Graves

### อาการตามกลไก
| กลไก | อาการ | อาการแสดง |
|---|---|---|
| **T3 เพิ่ม β-receptor** (ไวต่อ adrenaline) | ใจสั่น หงุดหงิด กระวนกระวาย dysphoria | **sinus tachycardia, AF**, tremor, lid retraction/lag |
| **BMR/การสร้างความร้อนเพิ่ม** | **ขี้ร้อน น้ำหนักลดทั้งที่กินมากขึ้น** | ผิวอุ่นชื้น |
| **ลำไส้บีบตัวเร็ว** | ถ่ายบ่อย ท้องเสีย | — |
| **สลายโปรตีนกล้ามเนื้อ** | เพลีย อ่อนแรง | **proximal myopathy** |
| **SHBG เพิ่ม + aromatization เพิ่ม** | ประจำเดือนน้อย libido ลด | **gynecomastia** ในชาย |
| **เลือดผ่านไตเพิ่ม** | ปัสสาวะบ่อย | — |
| ต่อมเอง | — | **goiter** |

### Apathetic thyrotoxicosis
**ผู้สูงอายุ** มาด้วย **ซึม เฉยเมย ซึมเศร้า น้ำหนักลด** หรือ **AF/หัวใจล้มเหลว** โดย **ไม่มีอาการ adrenergic** ให้เห็น (CMAJ 1974) → ผู้สูงอายุที่มี AF ใหม่ **ต้องส่ง TSH ทุกราย**""",
    ["Lid lag/retraction = adrenergic เกิดได้ทุกสาเหตุ ไม่ใช่ Graves โดยเฉพาะ",
     "ผู้สูงอายุ: apathetic thyrotoxicosis — ซึม + AF โดยไม่ใจสั่น → ส่ง TSH",
     "Gynecomastia จาก SHBG ↑ + aromatization ↑"],
    [mcq(N(7), "A 78-year-old man is brought in for 3 months of apathy, poor appetite and 6 kg weight loss. He has no tremor or sweating. ECG shows new atrial fibrillation at 110/min. His family thinks he is depressed. Which investigation is most important?",
         ["Mini-mental state examination", "Serum TSH", "Holter monitoring", "CT brain", "Serum vitamin B12"], 1,
         "สไลด์ — **apathetic thyrotoxicosis**: อาการผิดแบบของไทรอยด์เป็นพิษใน **ผู้สูงอายุ** — **ซึม เฉยเมย ซึมเศร้า** ไม่มีอาการ adrenergic ที่คุ้นเคย\n\nเบาะแสคือ **น้ำหนักลด + AF ใหม่** → ส่ง **TSH** ก่อนวินิจฉัยว่าซึมเศร้าหรือสมองเสื่อม\n\nผู้สูงอายุที่ thyrotoxic มักเป็น **toxic multinodular goiter** และเสี่ยง AF, หัวใจล้มเหลว, กระดูกพรุน",
         "ผู้สูงอายุ ซึม + ผอม + AF ใหม่ → TSH", "Apathetic thyrotoxicosis",
         [R("Symptoms – Apathetic thyrotoxicosis (CMAJ 1974;111:957)")], ["2.3.4(9)", "2.1.9", "B11.1.3(2)"]),
     mcq(N(8), "A 32-year-old man with untreated Graves' disease develops bilateral tender breast enlargement. What is the mechanism?",
         ["Prolactin secretion from a pituitary adenoma", "Increased sex hormone-binding globulin and peripheral aromatisation of androgens to oestrogen",
          "Direct stimulation of breast tissue by TSH receptor antibodies", "Testicular failure from autoimmune orchitis", "Side effect of methimazole"], 1,
         "สไลด์ \"Underlying mechanisms of gynecomastia in Graves' disease\" — ฮอร์โมนไทรอยด์ **เพิ่ม SHBG** ซึ่งจับ testosterone แน่นกว่า estradiol → **free testosterone ลด** สัดส่วน estrogen/androgen เพิ่ม ร่วมกับ **aromatization androgen → estrogen ที่เนื้อเยื่อเพิ่มขึ้น**\n\nหายได้เมื่อคุมไทรอยด์ได้",
         "Gynecomastia ใน thyrotoxicosis = SHBG ↑ + aromatization ↑", "Gynaecomastia in thyrotoxicosis",
         [R("Gynecomastia in Graves' disease (EDM Case Rep 2021)")], ["2.3.4(9)", "B11.2.5(2)"])],
    ["2.3.4(9)", "2.1.36", "2.1.9", "2.1.24"])

# ───────────────────────────── 5
sec("endo-th-05", "Graves' disease — แอนติบอดีปลอมตัวเป็น TSH",
    "สาเหตุ hyperthyroidism อันดับหนึ่ง · ตา หน้าแข้ง นิ้ว · Graves vs silent thyroiditis · ตารางแอนติบอดี", 9,
"""### ดูที่คอก่อนส่งแล็บ (จากสไลด์ อ.ชัยชาญ)
| สาเหตุ | ต่อมที่คลำได้ |
|---|---|
| **Graves' disease** | โตทั่วต่อม (diffuse) |
| **Silent/painless thyroiditis** (chronic lymphocytic) | โตทั่วต่อม |
| **Toxic multinodular goiter** | หลายก้อน |
| **Toxic adenoma** | ก้อนเดียว |
| **Subacute thyroiditis** | โตทั่ว/เป็นก้อน **กดเจ็บ + ไข้** |

### กลไก
autoantibody ต่อ **TSH receptor (TRAb)** กระตุ้นเหมือน TSH แต่ **feedback ปิดไม่ได้** → สร้างและหลั่งฮอร์โมนเพิ่ม · **สาเหตุ hyperthyroidism ที่พบบ่อยที่สุด** · พบมากอายุ **30–50 ปี** (JAMA 2023)

### ป้ายชื่อของ Graves — มีแต่ Graves
**TSH receptor อยู่บน fibroblast** หลังลูกตาและที่ผิวหนังด้วย → TRAb + cytokine → **สะสม glycosaminoglycan**
- **Exophthalmos** — เนื้อเยื่อหลังลูกตาบวม
- **Pretibial myxedema** — ผิวหน้าแข้งหนา แดง **กดไม่บุ๋ม**
- **Acropachy** — นิ้วปุ้ม
- ร่วมกับ **diffuse goiter + thyroid bruit** (หลอดเลือดเพิ่ม)

> เห็น **ตาโปนจริง, pretibial myxedema หรือ acropachy** ในผู้ป่วย thyrotoxic = วินิจฉัย Graves ได้เลย

### Graves vs silent thyroiditis
| | **Graves** | **Silent thyroiditis** |
|---|---|---|
| ระยะเวลาเป็นพิษ | นานเรื่อย ๆ | **< 6–8 สัปดาห์** |
| ตาโปน | ~10% | ไม่มี |
| เนื้อต่อม | นุ่มหรือแน่น | แน่น |
| Thyroid bruit | ~20% | ไม่มี |
| **RAIU** | **สูง (> 30%)** | **ต่ำ (< 10%)** |
| **TRAb** | **บวก** | **ลบ** |

### แอนติบอดี (%) — Williams 14th
| | TRAb | Anti-Tg | Anti-TPO |
|---|---|---|---|
| ประชากรทั่วไป | **0** | 5–20 | 8–27 |
| Graves | **80–95** | 50–70 | 50–80 |
| Autoimmune thyroiditis | 10–20 | 80–90 | **90–100** |

> **TRAb** แทบไม่พบในคนปกติ → ตัวชี้ Graves ที่ดี · **anti-TPO** บวกได้ทั้งสองโรคและคนปกติถึงหนึ่งในสี่ → ยืนยัน autoimmune แต่แยก Graves ไม่ได้""",
    ["Graves มีป้ายชื่อ 3 จุด: ตาโปน · pretibial myxedema · acropachy (+ bruit)",
     "Graves vs silent: ระยะเวลา > 6–8 wk · RAIU สูง · TRAb บวก",
     "TRAb ชี้ Graves · anti-TPO ชี้ autoimmune แต่แยกไม่ได้"],
    [mcq(N(9), "A 33-year-old woman has had thyrotoxic symptoms for 5 weeks. Her thyroid is diffusely enlarged, firm and non-tender, without bruit. There is no proptosis. TSH is suppressed and FT4 is high. Which pair of results would best distinguish painless thyroiditis from Graves' disease?",
         ["Anti-TPO positive and anti-Tg positive", "Low radioactive iodine uptake and negative TSH receptor antibody",
          "High radioactive iodine uptake and positive TSH receptor antibody", "High ESR and multinucleated giant cells", "High FT3 to FT4 ratio and low thyroglobulin"], 1,
         "ตาราง **Graves vs silent thyroiditis** — แยกด้วย **RAIU** (Graves สูง > 30% · silent ต่ำ < 10%) และ **TRAb** (Graves บวก · silent ลบ) ร่วมกับระยะเวลา (silent < 6–8 สัปดาห์) และไม่มีตาโปน/bruit\n\nAnti-TPO บวกได้ทั้งสองโรคจึงแยกไม่ได้ · ESR สูงและ giant cell เป็นของ **subacute** (เจ็บ มีไข้) ซึ่งรายนี้ไม่เจ็บ\n\nสำคัญเพราะ **silent thyroiditis ไม่ใช้ ATD** ให้แค่ β-blocker",
         "แยก Graves กับ silent: RAIU + TRAb", "Graves' disease vs painless thyroiditis",
         [R("Graves' disease vs Silent thyroiditis (adapted from Prof. Chaicharn)"), R("Thyroid autoantibody table")], ["2.3.4(9)", "2.3.4-3(2)", "B11.3(3)"]),
     mcq(N(10), "In a patient with thyrotoxicosis, which physical finding is specific for Graves' disease rather than other causes?",
         ["Lid lag", "Fine tremor", "Pretibial myxoedema", "Sinus tachycardia", "Warm moist skin"], 2,
         "สไลด์ — **pretibial myxedema** (ผิวหนังหน้าแข้งหนา แดง กดไม่บุ๋ม) เกิดจาก **TRAb + cytokines กระตุ้น dermal fibroblast ให้สะสม glycosaminoglycan** จึงพบ **เฉพาะ Graves** (ลายมือ: specific) เช่นเดียวกับ exophthalmos และ acropachy\n\nLid lag, tremor, tachycardia และผิวอุ่นชื้นเป็นผลของฮอร์โมนเกิน **เกิดได้ทุกสาเหตุ**",
         "Specific for Graves: ตาโปน · pretibial myxedema · acropachy", "Extrathyroidal manifestations of Graves' disease",
         [R("Graves' disease – pretibial myxedema, exophthalmos, acropachy (JAMA 2023;330:1472)")], ["2.3.4(9)", "B11.2.5(2)"])],
    ["2.3.4(9)", "B11.2.5(2)", "2.3.4(3)"])

# ───────────────────────────── 6
sec("endo-th-06", "Thyroiditis สามแบบ — และ subacute thyroiditis สามระยะ",
    "acute = แบคทีเรีย · subacute = ไวรัส เจ็บ ESR สูง · chronic = Hashimoto · NSAID → prednisolone 40", 9,
"""### ตารางสามชนิด
| | **Acute** | **Subacute** (de Quervain) | **Chronic** (Hashimoto/silent) |
|---|---|---|---|
| สาเหตุ | **แบคทีเรีย** | **ไวรัส** | **Autoimmune** |
| สถานะ | ปกติ | **เป็นพิษ → ขาด → ปกติ** | เป็นพิษ ปกติ หรือขาด |
| ไข้ เจ็บที่ต่อม | **มี** | **มี** | **ไม่มี** |
| วินิจฉัย | **FNA ย้อม Gram + เพาะเชื้อ** | **ESR สูง** · cyto **multinucleated giant cell** | **anti-TPO, anti-Tg** · cyto lymphocytic |
| รักษา | **ยาปฏิชีวนะ + ระบายหนอง** | **NSAID (steroid)** | ไม่ต้องรักษาจำเพาะ |

### Acute infectious thyroiditis
ปวดเด่นที่กลีบเดียว **กลืนเจ็บ** ร้าวไปคอหอยหรือหู ผิวแดง ไข้ ต่อมน้ำเหลืองโต · **TFT มักปกติ** · เด็กที่เป็นซ้ำซ้าย ให้คิดถึง **pyriform sinus fistula**

### Subacute (granulomatous, giant cell, de Quervain) thyroiditis
- ไวรัส — **mumps, coxsackie, influenza, echo, adenovirus**
- นำด้วยไข้ต่ำ เจ็บคอ อ่อนเพลีย แล้ว **ปวดต่อมมาก ร้าวไปหู ขากรรไกร** อาจ **ย้ายข้าง** ภายในหลายสัปดาห์
- ต่อมโตเล็กน้อย แข็ง **กดเจ็บ** · **ESR > 50 mm/h** · RAIU ต่ำ

**สามระยะ**
| ระยะ | นาน | กลไก |
|---|---|---|
| 1 · Thyrotoxic | **3–6 สัปดาห์** | follicle ถูกทำลาย ปล่อยฮอร์โมนที่สร้างไว้ |
| 2 · Hypothyroid | **ได้ถึง 6 เดือน** | คลังว่าง |
| 3 · Recovery | — | **5–15% ขาดถาวร** |

**รักษา**
- **NSAID ขนาดสูง** — ibuprofen **1,200–3,200 mg/วัน** หรือ aspirin **2,600 mg/วัน**
- ไม่ดีขึ้นใน **2–3 วัน** → หยุด NSAID ให้ **prednisolone 40 mg/วัน 1–2 สัปดาห์** แล้วค่อย ๆ ลดใน 2–4 สัปดาห์หรือนานกว่า
- **β-blocker** ตามอาการ · **ไม่ใช้ ATD**

### Hashimoto's thyroiditis
diffuse goiter · lymphocyte แทรกทั่วต่อม · ปกติ → subclinical → overt hypothyroid · **4.3%/ปี** กลายเป็น overt · anti-TPO/anti-Tg บวกเกือบทุกราย
**Postpartum thyroiditis** — 2–6 เดือนหลังคลอด ต่อมไม่เจ็บ TRAb ลบ (ช่วยแยกจาก Graves กำเริบหลังคลอด)""",
    ["Subacute: ไข้ + คอเจ็บร้าวหู + ESR > 50 + RAIU ต่ำ → NSAID ไม่ใช่ ATD",
     "NSAID ไม่ดีใน 2–3 วัน → prednisolone 40 mg/วัน 1–2 wk แล้ว taper",
     "สามระยะ: เป็นพิษ 3–6 wk → ขาดถึง 6 เดือน → หาย (5–15% ถาวร)"],
    [mcq(N(11), "A 42-year-old woman had a sore throat 2 weeks ago. She now has fever, palpitations and severe anterior neck pain radiating to both ears. The thyroid is firm and exquisitely tender. TSH < 0.01, FT4 high, ESR 85 mm/h, radioiodine uptake 2%. Ibuprofen 2,400 mg/day for 3 days has not relieved the pain. What is the next step?",
         ["Start methimazole 30 mg/day", "Radioactive iodine ablation", "Stop NSAID and start prednisolone 40 mg/day, with propranolol for palpitations",
          "Fine-needle aspiration for Gram stain and culture", "Urgent total thyroidectomy"], 2,
         "ไข้ + คอเจ็บร้าวหู + ต่อมกดเจ็บ + **ESR สูง** + **RAIU ต่ำ** หลังติดเชื้อทางเดินหายใจ = **subacute (de Quervain) thyroiditis**\n\nสไลด์ — เริ่ม **NSAID ขนาดสูง** (ibuprofen 1,200–3,200 mg/วัน) · **ไม่ดีขึ้นใน 2–3 วัน → หยุด NSAID ให้ prednisolone 40 mg/วัน 1–2 สัปดาห์** แล้ว taper 2–4 สัปดาห์ · **β-blocker** คุมใจสั่น\n\n**ATD ไม่ช่วย** (ไม่มีการสร้างใหม่) · RAI ใช้ไม่ได้เพราะต่อมไม่ดูดไอโอดีน · FNA Gram stain ใช้กับ **acute** thyroiditis ที่ TFT ปกติและเจ็บกลีบเดียว",
         "Subacute thyroiditis: NSAID → ไม่ดีใน 2–3 วัน → prednisolone 40", "Treatment of subacute thyroiditis",
         [R("Painful subacute thyroiditis – treatment (NEJM 2003;348:2646)")], ["2.3.4-3(2)", "2.3.4(9)"]),
     mcq(N(12), "A woman recovering from subacute thyroiditis asks how her thyroid function will change. Which sequence is expected?",
         ["Hypothyroid for 3–6 weeks, then thyrotoxic for 6 months", "Thyrotoxic for 3–6 weeks, then hypothyroid for up to 6 months, then recovery in most patients",
          "Permanent hypothyroidism in all patients", "Persistent thyrotoxicosis requiring radioiodine", "Euthyroid throughout because only pain occurs"], 1,
         "สไลด์ — **thyrotoxic phase 3–6 สัปดาห์** (หลั่งฮอร์โมนที่สร้างไว้จาก follicle ที่ถูกทำลาย) → **hypothyroid phase นานได้ถึง 6 เดือน** (คลังว่าง เซลล์กำลังซ่อม) → **recovery** โดย **5–15% เป็น hypothyroidism ถาวร**\n\nจึงต้องตรวจ TFT ซ้ำเป็นระยะหลังหายปวด และให้ levothyroxine ชั่วคราวถ้ามีอาการขาดฮอร์โมน",
         "Subacute: พิษ 3–6 wk → ขาด ≤ 6 เดือน → หาย (5–15% ถาวร)", "Natural history of subacute thyroiditis",
         [R("Painful subacute thyroiditis – laboratory finding")], ["2.3.4-3(2)", "2.3.4(4)"])],
    ["2.3.4-3(2)", "2.3.4(9)", "2.3.4(4)"])

# ───────────────────────────── 7
sec("endo-th-07", "ยาต้านไทรอยด์ — MMI คือยาแรก, PTU แค่ P-T-U",
    "กลไก · half-life · MMI 1 mg = PTU 20 mg · ขนาดเริ่มตาม FT4 · ติดตาม · หยุดยาเมื่อ TSH และ TRAb ปกติ", 9,
"""### กลไกและเภสัช
ทั้งสองตัวยับยั้ง **TPO ในต่อม** — iodine oxidation/organification · iodotyrosine coupling · การสร้าง thyroglobulin · การเติบโตของ follicular cell
**PTU** ยับยั้งการเปลี่ยน **T4 → T3 นอกต่อม** เพิ่มอีกทาง

| | **Methimazole (MMI)** | **PTU** |
|---|---|---|
| Half-life | **6–8 ชม.** | **90 นาที** |
| ออกฤทธิ์นาน | **24 ชม. (วันละครั้ง)** | 8–12 ชม. (วันละ 2–3 ครั้ง) |
| ผ่านรก / น้ำนม | ผ่าน / ผ่าน | ผ่าน / ผ่าน |
| ขนาดเทียบ | **MMI 1 mg ≈ PTU 20 mg** | |
| พิษเด่น | cholestasis · **embryopathy** | **ตับวายเฉียบพลัน** · ANCA vasculitis |

### P-T-U — สามสถานการณ์ที่ใช้ PTU
- **P**regnancy **ไตรมาสแรก** (ลายมือ: เปลี่ยนเป็น MMI **หลัง 16 สัปดาห์**)
- **T**hyroid storm (ยับยั้ง T4 → T3 ได้ด้วย)
- **U**nable to take MMI — แพ้ MMI แบบ **ไม่รุนแรง**

นอกจากนี้ **MMI เป็นยาแรกเสมอ** (ATA 2016)

### ขนาดเริ่ม MMI ตาม FT4
| FT4 | MMI เริ่มต้น |
|---|---|
| 1–1.5 × ULN | **5–10 mg/วัน** |
| 1.5–2 × ULN | **10–20 mg/วัน** |
| 2–3 × ULN | **30–40 mg/วัน** |
ปรับตามอาการ ขนาดต่อม และระดับ T3 ด้วย

### ติดตาม
- **FT4 + T3** ที่ **4–6 สัปดาห์** → ทุก 4–8 สัปดาห์จน euthyroid → ทุก 2–3 เดือน
- ลดเหลือขนาดต่ำสุดที่คุมได้ (มัก **2.5–5 mg/วัน**)
- **TSH ฟื้นช้า** — ใช้ปรับยาเมื่อ euthyroid ต่อเนื่องแล้วเท่านั้น

### หยุดยาเมื่อไร
- ให้ **12–18 เดือน** → หยุดได้ถ้า **TSH และ TRAb ปกติ**
- **TRAb ยังสูง** → ต่ออีก 12 เดือนแล้วประเมินใหม่ หรือ **RAI/ผ่าตัด**
- ใช้ MMI ระยะยาว → วัด TRAb ปีละครั้ง หยุดเมื่อกลับปกติ
- **หลังหยุด** — TFT ที่ 1–3 เดือน แล้วทุก 3 เดือนใน 1 ปี · กำเริบ → RAI/ผ่าตัด หรือ MMI ขนาดต่ำระยะยาว · หายแล้วตรวจอย่างน้อยปีละครั้ง""",
    ["MMI เป็นยาแรก · PTU = Pregnancy ไตรมาสแรก, Thyroid storm, Unable (แพ้ MMI เล็กน้อย)",
     "MMI 1 mg ≈ PTU 20 mg · MMI ออกฤทธิ์ 24 ชม. กินวันละครั้ง",
     "เริ่ม MMI ตาม FT4: 1–1.5× → 5–10 · 1.5–2× → 10–20 · 2–3× → 30–40 mg/วัน",
     "ให้ 12–18 เดือน หยุดเมื่อ TSH และ TRAb ปกติ"],
    [mcq(N(13), "A 35-year-old woman with newly diagnosed Graves' disease has FT4 3.4 ng/dL (ULN 1.8) and FT3 9.0 pg/mL (ULN 4). She is not pregnant and has no liver disease. What is the most appropriate initial antithyroid regimen?",
         ["PTU 100 mg three times daily", "Methimazole 5 mg once daily", "Methimazole 20 mg once daily", "Methimazole 30 mg once daily", "Levothyroxine plus methimazole (block-and-replace)"], 2,
         "FT4 3.4/1.8 = **1.9 × ULN** → ตารางสไลด์ **1.5–2 × ULN → MMI 10–20 mg/วัน** · FT3 สูงมากเป็นเหตุผลให้เลือก **ขอบบน (20 mg)** ตามที่สไลด์ให้พิจารณา T3 ด้วย\n\nMMI ออกฤทธิ์ 24 ชั่วโมงจึง **กินวันละครั้ง** · PTU ไม่ใช่ยาแรกเพราะพิษต่อตับ และใช้เฉพาะ P-T-U · 30–40 mg สงวนไว้สำหรับ FT4 2–3 × ULN · block-and-replace ไม่แนะนำ",
         "FT4 1.5–2× ULN → MMI 10–20 mg วันละครั้ง", "Initial methimazole dosing",
         [R("Antithyroid drug – Start (FT4-guided)"), "Ross DS et al. ATA 2016 (Thyroid 2016;26:1343)"], ["B11.4(2)", "2.3.4(9)"]),
     mcq(N(14), "A woman with Graves' disease has taken methimazole for 18 months. She is clinically euthyroid on 2.5 mg/day. TSH is normal but TSH receptor antibody remains elevated. What is the most appropriate plan?",
         ["Stop methimazole now because TSH is normal", "Continue methimazole for another 12 months and reassess, or consider radioiodine or thyroidectomy",
          "Double the methimazole dose", "Switch to PTU", "Add levothyroxine and stop methimazole"], 1,
         "สไลด์ \"When to stop\" — ให้ MMI **12–18 เดือน** แล้ว **หยุดได้ถ้าทั้ง TSH และ TRAb ปกติ** · **ถ้า TRAb ยังสูง ให้ MMI ต่ออีก 12 เดือนแล้วประเมินใหม่ หรือพิจารณา RAI/ผ่าตัด**\n\nTRAb ที่ยังบวกตอนหยุดยาคือ **ตัวทำนายการกำเริบที่แรงที่สุด** (สไลด์: กลุ่มที่ TRAb ยังบวก relapse สูงถึง 53–85%)",
         "TRAb ยังบวกที่ 18 เดือน → ต่อยาอีก 12 เดือน หรือ RAI/ผ่าตัด", "Stopping antithyroid drugs",
         [R("Antithyroid drug – When to stop"), R("Thyroid 2006;16:295")], ["B11.4(2)", "2.3.4(9)"])],
    ["B11.4(2)", "2.3.4(9)"])

# ───────────────────────────── 8
sec("endo-th-08", "ผลข้างเคียงของ ATD, การตั้งครรภ์ และ β-blocker",
    "agranulocytosis → หยุดยาเจาะ CBC · แพ้รุนแรงห้ามสลับ · MMI embryopathy · propranolol คุมอาการ", 8,
"""*(ตารางผลข้างเคียงอยู่ในสไลด์ช่วงที่ดึงข้อความไม่ได้ — เทียบจาก ATA 2016)*

| ผลข้างเคียง | ความถี่ | ลักษณะ |
|---|---|---|
| ผื่น ลมพิษ ปวดข้อ | 1–5% | ผื่นเล็กน้อยให้ antihistamine ต่อยาได้ |
| **Agranulocytosis** | **0.2–0.5%** | มักใน 3 เดือนแรก · MMI ขึ้นกับขนาด · PTU ไม่ขึ้นกับขนาด |
| **Hepatotoxicity** | < 0.1% | **PTU → fulminant hepatitis/ตับวาย** · MMI → cholestasis |
| **ANCA vasculitis** | พบน้อย | **PTU** มากกว่า |
| Hypoglycemia | พบน้อย | insulin autoimmune syndrome (กลุ่ม sulfhydryl) |

### กฎเหล็กสองข้อ
1. **ไข้ เจ็บคอ แผลในปาก → หยุดยาและเจาะ CBC ทันที** (สอนผู้ป่วยทุกคนตั้งแต่วันแรก) · ตัวเหลือง ปัสสาวะเข้ม → หยุดยาตรวจตับ
2. **แพ้รุนแรงตัวหนึ่ง ห้ามสลับไปอีกตัว** — cross-reactivity → ไปทาง **RAI หรือผ่าตัด**

### การตั้งครรภ์
| | ความพิการแต่กำเนิด |
|---|---|
| **MMI** | **2–4%** รุนแรง — **aplasia cutis** (หนังศีรษะขาด), **choanal atresia**, esophageal atresia, omphalocele |
| **PTU** | ~2.3% รุนแรงน้อยกว่า — preauricular sinus, ทางเดินปัสสาวะ |

**ก่อนจ่ายยา** — ถาม LMP ทุกครั้ง แนะนำคุมกำเนิด · ตั้งครรภ์ → **PTU ไตรมาสแรก** แล้วเปลี่ยน MMI · ตรวจ **CBC และ LFT พื้นฐาน**

### β-blocker — คุมอาการระหว่างรอยาหรือรอ thyroiditis หาย
| ยา | ขนาด | ข้อควรรู้ |
|---|---|---|
| **Propranolol** | 10–40 mg วันละ 3–4 ครั้ง | non-selective · **ขนาดสูงลด T4 → T3** · ใช้ในครรภ์/ให้นมได้ · ห้ามในหอบหืด |
| Atenolol | 25–100 mg วันละ 1–2 ครั้ง | β1 · กินง่าย · เลี่ยงในครรภ์ |
| Metoprolol | 25–50 mg วันละ 2–3 ครั้ง | β1 |""",
    ["ไข้ เจ็บคอหลังเริ่ม ATD → หยุดยา + CBC ทันที",
     "แพ้รุนแรง (agranulocytosis, ตับ, vasculitis) ห้ามสลับไปอีกตัว → RAI/ผ่าตัด",
     "MMI embryopathy: aplasia cutis, choanal atresia → PTU ไตรมาสแรก",
     "Propranolol คุมอาการได้ทันทีทุกสาเหตุ"],
    [mcq(N(15), "A 28-year-old woman started methimazole 20 mg/day 6 weeks ago for Graves' disease. She now has fever 39 °C and a painful sore throat with oral ulcers. What is the most appropriate immediate action?",
         ["Continue methimazole and prescribe amoxicillin", "Halve the methimazole dose", "Stop methimazole and obtain an urgent complete blood count with differential",
          "Switch to PTU immediately", "Add prednisolone and continue methimazole"], 2,
         "ไข้ + เจ็บคอ + แผลในปากในช่วง 3 เดือนแรกของ ATD = ต้องคิดถึง **agranulocytosis** (0.2–0.5%) จนกว่าจะพิสูจน์ได้ว่าไม่ใช่\n\n**หยุดยาทันทีและเจาะ CBC** · ถ้า ANC < 500 → รับไว้ ให้ยาปฏิชีวนะครอบคลุมกว้าง ± G-CSF\n\n**ห้ามสลับไป PTU** เพราะ cross-reactivity → รักษาไทรอยด์ต่อด้วย β-blocker แล้ววาง RAI หรือผ่าตัด",
         "ATD + ไข้เจ็บคอ → หยุดยา เจาะ CBC · ห้ามสลับยา", "Agranulocytosis from antithyroid drugs",
         ["ATA 2016 (Thyroid 2016;26:1343) – side effects", R("Antithyroid drug")], ["B11.4(2)", "2.3.4(9)"]),
     mcq(N(16), "A 30-year-old woman with Graves' disease controlled on methimazole 10 mg/day finds she is 6 weeks pregnant. What is the most appropriate change?",
         ["Continue methimazole throughout pregnancy", "Stop all antithyroid drugs and give radioiodine",
          "Switch to PTU for the first trimester, then consider switching back to methimazole after about 16 weeks", "Switch to propranolol alone", "Perform urgent thyroidectomy in the first trimester"], 2,
         "สไลด์ — **PTU ในไตรมาสแรก** (P ของ P-T-U) ลายมือกำกับ **\"after 16 weeks\"** เปลี่ยนกลับเป็น MMI\n\nเหตุผล: **MMI embryopathy** (aplasia cutis, choanal/esophageal atresia) เกิดช่วงสร้างอวัยวะ · ส่วน PTU มีพิษต่อตับ จึงไม่ใช้ยาวตลอดครรภ์\n\nขนาดเทียบ MMI 10 mg ≈ **PTU 200 mg/วัน** แบ่งให้ · **RAI ห้ามในครรภ์** · ผ่าตัดถ้าจำเป็นทำช่วงไตรมาสสอง",
         "ตั้งครรภ์ไตรมาสแรก → PTU แล้วกลับ MMI หลัง ~16 wk", "Antithyroid drugs in pregnancy",
         [R("Antithyroid drug – 1st trimester (handwritten: after 16 weeks)"), "ATA 2017 Thyroid and Pregnancy Guideline"], ["B11.4(2)", "2.3.4(9)"])],
    ["B11.4(2)", "2.3.4(9)"])

# ───────────────────────────── 9
sec("endo-th-09", "เลือกทางรักษา Graves — ATD · RAI · ผ่าตัด และใครจะกลับเป็นซ้ำ",
    "RAI หาย > 90% แต่ตาอาจแย่ลง · ผ่าตัดเมื่อคอพอกใหญ่/สงสัยมะเร็ง/ตารุนแรง · GREAT score · MMI ระยะยาว", 9,
"""### Radioactive iodine (I-131)
- **หาย > 90%** ใน Graves และ autonomous nodule
- ก่อนทำ: **β-blocker ± MMI ล่วงหน้า**
- **อาจทำให้ตาโปน (Graves' orbitopathy) แย่ลง** — ระวังโดยเฉพาะผู้สูบบุหรี่ ± steroid ป้องกัน
- **ห้าม** ในการตั้งครรภ์/ให้นม และเมื่อสงสัยมะเร็ง · คุมกำเนิดหลังทำ 4–6 เดือน
- ผลระยะยาวส่วนใหญ่คือ **hypothyroidism → ต้องกิน levothyroxine**

### ผ่าตัด
**ข้อบ่งชี้** — **คอพอกใหญ่กดเบียด** · **ก้อนสงสัย/เป็นมะเร็ง** · **ตาโปนปานกลาง–รุนแรง**
| โรค | ผ่าตัด |
|---|---|
| Graves | **total** > subtotal thyroidectomy |
| Toxic adenoma | **lobectomy** |
| Toxic MNG | **total thyroidectomy** |
ภาวะแทรกซ้อน — **recurrent laryngeal nerve** (เสียงแหบ) · hematoma · **hypoparathyroidism** (Ca ต่ำ) · ต้องกิน LT4 ตลอดชีวิต

### เลือกตามสถานการณ์ (ATA 2016)
| สถานการณ์ | ทางที่เหมาะ |
|---|---|
| ตั้งครรภ์ | ATD (PTU→MMI) · ผ่าตัดไตรมาสสองถ้าจำเป็น · **ห้าม RAI** |
| ตาโปน active ปานกลาง–รุนแรง | **ATD หรือผ่าตัด** |
| โรคตับ / แพ้ ATD รุนแรง | **RAI หรือผ่าตัด** |
| โอกาส remission สูง (หญิง อาการน้อย ต่อมเล็ก TRAb ต่ำ) | **ATD** |
| สงสัยมะเร็ง | **ผ่าตัด** |
| เสี่ยงผ่าตัดสูง | **RAI** |

### ใครจะกลับเป็นซ้ำหลังหยุด ATD
ปัจจัย — ขนาดต่อม · **TRAb (ทำนายแรงที่สุด)** · FT4 · อายุ เพศ ประวัติครอบครัว · ตาโปน · **สูบบุหรี่** · หลังคลอด
แต่ไม่มีตัวแปรเดียวพอ — TRAb ลบยัง relapse **39%** · TRAb บวก **53%** (JCEM 2024)

**GREAT score** (JCEM 2016) — ประเมินก่อนเริ่มยา
| ตัวแปร | คะแนน |
|---|---|
| อายุ < 40 ปี | +1 |
| FT4 ก่อนรักษา ≥ 40 pmol/L (≈ 3.1 ng/dL) | +1 |
| TRAb 6–19.9 IU/L / ≥ 20 | +1 / +2 |
| คอพอก grade II–III | +2 |

| Class | คะแนน | กลับเป็นซ้ำ |
|---|---|---|
| I | 0–1 | **16%** |
| II | 2–3 | **44%** |
| III | 4–6 | **68%** |
GREAT+ เพิ่ม HLA (DQB1\\*02, DQA1\\*05, DRB1\\*03)

### MMI ระยะยาว
RCT (Thyroid 2019) — MMI **60–120 เดือน** กลับเป็นซ้ำน้อยกว่า 18–24 เดือน ขนาดคงที่ราว **3.5–5.5 mg/วัน** · เป็นทางเลือกเมื่อไม่ต้องการ RAI/ผ่าตัด""",
    ["RAI หาย > 90% · ห้ามในครรภ์และสงสัยมะเร็ง · ตาอาจแย่ลง",
     "ผ่าตัดเมื่อ: คอพอกกดเบียด · สงสัยมะเร็ง · ตาโปนปานกลาง–รุนแรง",
     "TRAb คือตัวทำนาย relapse ที่แรงที่สุด · GREAT class III กลับเป็นซ้ำ 68%"],
    [mcq(N(17), "A 38-year-old woman who smokes has Graves' disease with active moderate-to-severe orbitopathy (proptosis, diplopia, eyelid swelling). Which definitive treatment should be AVOIDED?",
         ["Continued methimazole", "Total thyroidectomy", "Radioactive iodine without glucocorticoid cover", "Smoking cessation counselling", "Selenium supplementation for mild disease"], 2,
         "สไลด์ — **radioactive iodine may cause or exacerbate eye disease** ในผู้ป่วย Graves โดยเฉพาะ **ผู้สูบบุหรี่** และตาที่กำลัง active\n\nATA 2016 — ตาโปน **active ปานกลาง–รุนแรง** → เลือก **ATD หรือผ่าตัด** · ถ้าจำเป็นต้องใช้ RAI ในตาโปนเล็กน้อยต้องมี **steroid คลุม**\n\nสไลด์ระบุ **moderate to severe Graves' ophthalmopathy เป็นข้อบ่งชี้ของการผ่าตัด** · เลิกบุหรี่สำคัญทุกราย",
         "Graves + ตาโปน active → ATD หรือผ่าตัด ไม่ใช่ RAI", "Choice of therapy in Graves' orbitopathy",
         [R("Radioactive iodine therapy; Surgery – indications"), "ATA 2016"], ["2.3.4(9)", "B11.2.5(2)"]),
     mcq(N(18), "A 25-year-old woman with newly diagnosed Graves' disease has a grade III goitre, FT4 55 pmol/L, and TRAb 24 IU/L. Using the GREAT score, what is her predicted risk of relapse after a standard course of antithyroid drugs?",
         ["About 5%", "About 16%", "About 44%", "About 68%", "Relapse cannot occur if she completes 18 months"], 3,
         "GREAT score: **อายุ < 40 = +1** · **FT4 ≥ 40 pmol/L = +1** · **TRAb ≥ 20 IU/L = +2** · **goiter grade II–III = +2** → รวม **6 คะแนน = Class III (4–6)** → **กลับเป็นซ้ำราว 68%**\n\nข้อมูลนี้ช่วยตัดสินใจตั้งแต่ต้นว่าอาจเลือก **RAI หรือผ่าตัด** หรือวางแผน **MMI ระยะยาว** แทนการให้ยา 18 เดือนแล้วหยุด",
         "GREAT: อายุ < 40, FT4 ≥ 40, TRAb, goiter → class III = 68%", "GREAT score",
         [R("GREAT score (JCEM 2016;101:1381)")], ["2.3.4(9)", "B11.4(2)"])],
    ["2.3.4(9)", "B11.4(2)", "2.3.4(3)"])

# ───────────────────────────── 10
sec("endo-th-10", "Toxic adenoma, toxic multinodular goiter และ thyroid storm",
    "hot nodule ไม่ใช่มะเร็ง · ก้อนไม่หายเอง → RAI/ผ่าตัด · storm: β-blocker → PTU → iodine 1 ชม.หลัง → steroid", 9,
"""### Toxic adenoma
**ก้อนเดียวที่ทำงานเอง (autonomous)** · thyroid scan เห็น **จุดดูดสารสูง (hot nodule)** เนื้อต่อมที่เหลือถูกกดจาง
- ลายมือ: **hot nodule แทบไม่เป็นมะเร็ง** → มักไม่ต้อง FNA
- แต่ถ้าเป็น **Graves ร่วมกับ cold nodule** → ต้อง work up มะเร็งแบบก้อนทั่วไป
- รักษา **RAI หรือ lobectomy** — ATD คุมได้ชั่วคราวแต่ก้อนไม่หายเอง

### Toxic multinodular goiter
hyperthyroidism ที่เกิดใน **คอพอกหลายก้อนที่เป็นมานาน** · มักเป็นผู้สูงอายุ · **subclinical หรือเป็นพิษเล็กน้อย** · รักษา **RAI หรือ total thyroidectomy**

### Case ในสไลด์
หญิง 40 ปี น้ำหนักลด ใจสั่น **12 เดือน** · FT4 2 FT3 6.5 TSH < 0.001 → ลายมือ: **thyroid scan** → toxic adenoma หรือ Graves + cold nodule

### Thyroid storm *(ไม่อยู่ในสไลด์ส่วนที่ดึงได้ — ATA 2016 / JTA 2016)*
ไทรอยด์เป็นพิษที่ **อวัยวะเริ่มล้มเหลว** — ไข้สูง หัวใจเต้นเร็วมาก/AF หัวใจล้มเหลว **สับสน ชัก โคม่า** อาเจียน ท้องเสีย ตัวเหลือง
ตัวกระตุ้น — **หยุดยาเอง**, ติดเชื้อ, ผ่าตัด, คลอด, RAI, สารทึบรังสีไอโอดีน
**Burch–Wartofsky ≥ 45** = เข้าได้มาก (25–44 = ใกล้เป็น)

**รักษาเรียงตามลำดับ (ใน ICU)**
| ขั้น | ยา | เหตุผล |
|---|---|---|
| 1 | **Propranolol** 60–80 mg ทุก 4 ชม. (หรือ esmolol) | คุมหัวใจ + ลด T4 → T3 |
| 2 | **PTU** 500–1,000 mg loading แล้ว 250 mg ทุก 4 ชม. (หรือ MMI 60–80 mg/วัน) | หยุดการสร้าง + ลด T4 → T3 |
| 3 | **Iodine** (SSKI/Lugol) **ให้หลัง thionamide อย่างน้อย 1 ชม.** | หยุดการหลั่ง — ให้ก่อนจะกลายเป็นวัตถุดิบ |
| 4 | **Hydrocortisone** 300 mg แล้ว 100 mg ทุก 8 ชม. | ลด T4 → T3 + adrenal reserve ไม่พอ |
| 5 | ลดไข้ด้วย **paracetamol** + cooling · **ห้าม aspirin** | aspirin แย่ง T4 ออกจาก TBG |
| 6 | รักษาตัวกระตุ้น · สารน้ำ · cholestyramine เสริม | |""",
    ["Hot nodule แทบไม่เป็นมะเร็ง · Graves + cold nodule → work up",
     "Toxic adenoma → RAI/lobectomy · TMNG → RAI/total",
     "Storm: β-blocker → PTU → iodine ≥ 1 ชม.หลัง → hydrocortisone · ห้าม aspirin"],
    [mcq(N(19), "A 60-year-old woman has subclinical hyperthyroidism and a single 3-cm palpable thyroid nodule. Thyroid scintigraphy shows intense uptake in the nodule with suppressed uptake in the rest of the gland. What is the next step?",
         ["Fine-needle aspiration of the nodule", "Radioactive iodine or lobectomy as definitive therapy", "Long-term PTU", "Observation only because hot nodules resolve spontaneously", "Total thyroidectomy with neck dissection for presumed cancer"], 1,
         "Scan เป็น **hot nodule** ที่กดเนื้อรอบข้าง = **toxic adenoma** (autonomously functioning nodule)\n\nลายมือในสไลด์ — **hot nodule แทบไม่เป็นมะเร็ง** จึง **ไม่ต้อง FNA** · ก้อนไม่หายเองและ ATD แค่คุมชั่วคราว → **definitive: RAI หรือ thyroid lobectomy**\n\nผู้หญิงอายุ 60 ที่ TSH ถูกกดเสี่ยง **AF และกระดูกพรุน** จึงควรรักษาแม้ subclinical",
         "Hot nodule → ไม่ต้อง FNA → RAI หรือ lobectomy", "Toxic adenoma",
         [R("Toxic adenoma – thyroid scan, Tx RAI or thyroidectomy")], ["2.3.4(9)", "B11.2.4-3(1)", "2.1.53"]),
     mcq(N(20), "A 40-year-old woman with Graves' disease stopped methimazole 2 weeks ago. She now has temperature 40 °C, AF at 160/min, agitation and vomiting. Burch–Wartofsky score is 70. Propranolol and PTU have been given. Which statement about the next medication is correct?",
         ["Give Lugol's iodine before PTU to block hormone release faster", "Give iodine at least 1 hour after the thionamide",
          "Use aspirin to control the fever", "Avoid glucocorticoids because they worsen thyrotoxicosis", "Start levothyroxine to suppress TSH"], 1,
         "**Thyroid storm** (BWPS ≥ 45) จากการหยุดยาเอง\n\nลำดับ: **β-blocker → thionamide (PTU) → iodine อย่างน้อย 1 ชั่วโมงหลัง → hydrocortisone** · ถ้าให้ iodine ก่อน thionamide ต่อมจะใช้ไอโอดีนเป็น **วัตถุดิบสร้างฮอร์โมนเพิ่ม** (Jod–Basedow)\n\nลดไข้ด้วย paracetamol — **ห้าม aspirin** เพราะแย่ง T4 ออกจาก TBG ทำให้ free hormone เพิ่ม · hydrocortisone **ช่วย** ลด T4 → T3",
         "Storm: iodine ให้หลัง thionamide ≥ 1 ชม. · ห้าม aspirin", "Thyroid storm management",
         ["ATA 2016 (Thyroid 2016;26:1343) – thyroid storm", "Japan Thyroid Association 2016 – thyroid storm guideline"], ["2.3.4-3(3)", "B11.2.5-3(4)", "B11.4(2)"])],
    ["2.3.4(9)", "2.3.4-3(3)", "B11.2.4-3(1)"])

# ───────────────────────────── 11
sec("endo-th-11", "Hypothyroidism — ทุกอย่างช้าลง และมีเมือกพอกผิว",
    "อาการตามกลไก · primary vs central · levothyroxine 1.6 mcg/kg · start low go slow · เป้า TSH vs FT4", 9,
"""*(ส่วนนี้ของสไลด์ดึงข้อความไม่ได้ — เทียบจากบทเรียนที่ทำจากสไลด์ชุดเดียวกัน + ATA 2014)*

### อาการตามกลไก
| กลไก | อาการและอาการแสดง |
|---|---|
| **BMR และความร้อนลด** | เหนื่อย เพลีย **ขี้หนาว** น้ำหนักขึ้นทั้งที่เบื่ออาหาร |
| หัวใจ/adrenergic ช้า | **bradycardia** เหนื่อยง่าย |
| **Glycosaminoglycan สะสม ดูดน้ำ** | หน้า มือ เท้าบวมกดไม่บุ๋ม (**myxedema**) · **เสียงแหบ** · **carpal tunnel** · น้ำในเยื่อหุ้มหัวใจ/ปอด · หูตึง |
| กล้ามเนื้อคลายตัวช้า | **delayed relaxation ของ ankle reflex** |
| ผิวและต่อมเหงื่อ | ผิวแห้งหยาบ ผมร่วง |
| ลำไส้ | **ท้องผูก** |
| สมอง | ความจำไม่ดี สมาธิลด ซึมเศร้า |
| ฮอร์โมนเพศ | **menorrhagia** ระยะหลังขาดประจำเดือน |
| แล็บ | **hyponatremia, LDL สูง, CK สูง**, ซีด |

### Primary vs central
| **Primary** — โรงงานเสีย · TSH สูง | **Central** — ผู้จัดการเสีย · TSH ไม่สูงตาม |
|---|---|
| **Hashimoto** (พบบ่อยที่สุด) · หลัง **I-131/ผ่าตัด/ฉายแสงที่คอ** · **ขาดไอโอดีน** · ยา **amiodarone, lithium** · thyroiditis · infiltrative | hypopituitarism (เนื้องอก **Sheehan** หลังผ่าตัด/ฉายแสง) · โรค hypothalamus — **ตรวจ cortisol ก่อนเริ่ม LT4** |

### Levothyroxine
- ขนาดเต็ม **1.6 mcg/kg/วัน** (น้ำหนักอุดมคติ)
- กิน **ก่อนอาหารเช้า 60 นาที** (หรือก่อนนอน ≥ 3 ชม.หลังอาหารเย็น) · **แยกจากแคลเซียม เหล็ก ยาลดกรด ≥ 4 ชม.**
- **อายุ > 50–60 ปี หรือโรคหัวใจ → "start low, go slow"** 12.5–25 mcg/วัน
- ปรับครั้งละ 12.5–25 mcg · **TSH ซ้ำ 4–6 สัปดาห์** หลังเปลี่ยนขนาดทุกครั้ง
- **เป้า primary = TSH ปกติ** · **เป้า central = FT4 ครึ่งบนของค่าปกติ** (TSH ใช้ไม่ได้)
- ตั้งครรภ์ → เพิ่มขนาด ~25–30% ทันทีที่รู้

### Myxedema coma *(ATA 2014)*
ผู้สูงอายุ hypothyroid รุนแรง + ตัวกระตุ้น (ติดเชื้อ หนาว ยากดประสาท) → **ซึม อุณหภูมิต่ำ หายใจช้า (CO₂ คั่ง) Na ต่ำ น้ำตาลต่ำ หัวใจช้า**
รักษา: **hydrocortisone ก่อน/พร้อมกัน** + **levothyroxine IV 200–400 mcg loading** + ประคับประคอง (อุ่นช้า ๆ ช่วยหายใจ)""",
    ["Hypothyroid: ช้า เย็น บวม ง่วง · ankle reflex คลายช้า · carpal tunnel · Na ต่ำ LDL สูง CK สูง",
     "LT4 1.6 mcg/kg ก่อนอาหารเช้า 60 นาที · สูงอายุ/โรคหัวใจ เริ่ม 12.5–25",
     "เป้า primary = TSH ปกติ · central = FT4 ครึ่งบน"],
    [mcq(N(21), "A 72-year-old man with stable angina is newly diagnosed with primary hypothyroidism (TSH 38 mIU/L, FT4 0.4 ng/dL). Weight 70 kg. What is the most appropriate levothyroxine regimen?",
         ["112 mcg/day (full replacement 1.6 mcg/kg) immediately", "12.5–25 mcg/day, increased gradually every 4–6 weeks according to TSH and symptoms",
          "IV levothyroxine 400 mcg loading", "Liothyronine (T3) 25 mcg three times daily", "No treatment until TSH exceeds 50 mIU/L"], 1,
         "ขนาดเต็มคือ **1.6 mcg/kg** (≈ 112 mcg) แต่ใน **ผู้สูงอายุหรือมีโรคหลอดเลือดหัวใจ** ต้อง **\"start low, go slow\"** เริ่ม **12.5–25 mcg/วัน** เพราะการเพิ่มการเผาผลาญเร็วเพิ่มความต้องการออกซิเจนของหัวใจ → angina/MI\n\nปรับครั้งละ 12.5–25 mcg ตรวจ **TSH ซ้ำทุก 4–6 สัปดาห์** · IV loading สงวนไว้สำหรับ **myxedema coma** · T3 ไม่ใช่ยาหลัก",
         "สูงอายุ/โรคหัวใจ: LT4 เริ่ม 12.5–25 mcg", "Levothyroxine initiation",
         ["ATA Hypothyroidism Guideline 2014 (Thyroid 2014;24:1670)"], ["2.3.4(4)", "B11.4(2)", "B11.2.5(3)"]),
     mcq(N(22), "A 45-year-old woman on levothyroxine 100 mcg/day for Hashimoto's thyroiditis has a TSH that rose from 2.0 to 9.5 mIU/L after she started iron and calcium supplements, which she takes with her levothyroxine at breakfast. What is the best next step?",
         ["Double the levothyroxine dose", "Advise taking levothyroxine on an empty stomach 30–60 minutes before breakfast, separated from iron and calcium by at least 4 hours, and recheck TSH in 6 weeks",
          "Switch to liothyronine", "Stop iron and calcium permanently", "Check TSH receptor antibody"], 1,
         "**เหล็ก แคลเซียม และยาลดกรด จับ levothyroxine ในลำไส้** ทำให้ดูดซึมลด → TSH สูงขึ้นโดยที่โรคไม่ได้แย่ลง\n\nแก้ที่ **วิธีกิน** ก่อนเพิ่มขนาด: กินตอนท้องว่าง **ก่อนอาหารเช้า 30–60 นาที** · **แยกจากเหล็ก/แคลเซียม ≥ 4 ชั่วโมง** · **ตรวจ TSH ซ้ำ 4–6 สัปดาห์** — เป็นเนื้อหา counselling levothyroxine ที่ออก OSCE บ่อย",
         "LT4 ท้องว่าง แยกจากเหล็ก/แคลเซียม ≥ 4 ชม.", "Levothyroxine absorption",
         ["ATA Hypothyroidism Guideline 2014"], ["2.3.4(4)", "B11.4(2)"])],
    ["2.3.4(4)", "B11.2.5(3)", "B11.4(2)"])

# ───────────────────────────── 12
sec("endo-th-12", "Amiodarone และไอโอดีน — Wolff–Chaikoff กับ Jod–Basedow",
    "200 mg มีไอโอดีน 75 mg · hypo จากต่อม Hashimoto · AIT 1 = ของเกิน → MMI · AIT 2 = ไฟไหม้ → prednisone", 7,
"""*(ส่วนนี้ของสไลด์ดึงข้อความไม่ได้ — เทียบจากบทเรียนที่ทำจากสไลด์ชุดเดียวกัน + ETA 2018)*

**Amiodarone 200 mg มีไอโอดีน 75 mg** ปล่อยไอโอดีนอิสระราว **7 mg/วัน** ขณะที่ร่างกายต้องการ **0.15–0.30 mg/วัน** (เกินหลายสิบเท่า) และยายัง **กด D1** (T4 → T3 ลด)

### สามทางที่ต่อมตอบสนอง
| | **Hypothyroidism** (10–20%) | **AIT type 1** | **AIT type 2** |
|---|---|---|---|
| กลไก | **Wolff–Chaikoff ที่ไม่หลุด** — ไอโอดีนเกินกด organification ต่อมปกติหนีได้ แต่ **ต่อม Hashimoto หนีไม่ได้** | **Jod–Basedow** — ต่อมที่มีโรคเดิม (Graves แฝง, nodular goiter) ได้วัตถุดิบเพิ่มแล้วผลิตไม่ยั้ง | **Destructive thyroiditis** — ยาทำลายเซลล์ตรง ของเก่ารั่ว |
| ต่อมเดิม | Hashimoto | **มีโรค** | **มักปกติ** |
| Color Doppler | — | **เลือดมาเลี้ยงมาก** | ไม่เพิ่ม |
| RAIU | — | ต่ำ/ปกติ/สูง | **ถูกกด** |
| เริ่มหลังได้ยา | — | ~3 เดือน | **~30 เดือน** |
| รักษา | **levothyroxine ให้ amiodarone ต่อได้** | **methimazole 40–60 mg/วัน** | **prednisone 40 mg/วัน** (หายเองได้) |

> **หลักจำ** — **Type 1 = ของเกิน ให้ยาหยุดผลิต · Type 2 = ไฟไหม้ ให้ยาดับไฟ** · แยกไม่ได้ เป็นแบบผสม หรือหัวใจไม่เสถียร → **ให้ MMI + prednisone ร่วมกันตั้งแต่แรก** (ETA 2018)

### ช่วง 3 เดือนแรกในคนไทรอยด์ปกติ
TSH สูงเล็กน้อย · T4 สูง · T3 ต่ำ · rT3 สูง — เป็นผลของยา **อย่ารีบวินิจฉัยโรค** · ควรตรวจ TFT ก่อนเริ่มยาและทุก 6 เดือน""",
    ["Amiodarone 200 mg = iodine 75 mg · ตรวจ TFT ก่อนเริ่มและทุก 6 เดือน",
     "Hypothyroid จาก amiodarone → LT4 ไม่ต้องหยุดยา",
     "AIT 1 (ต่อมมีโรค, Doppler เลือดมาก) → MMI · AIT 2 (ต่อมปกติ, ทำลาย) → prednisone"],
    [mcq(N(23), "A 70-year-old man has taken amiodarone for 2.5 years for ventricular tachycardia. He develops weight loss and palpitations. TSH < 0.01, FT4 high. He has no goitre and no prior thyroid disease. Colour-flow Doppler shows absent vascularity and radioiodine uptake is suppressed. What is the most appropriate treatment?",
         ["Methimazole 40–60 mg/day", "Prednisone 40 mg/day", "Radioactive iodine", "Levothyroxine", "Potassium iodide"], 1,
         "ต่อมเดิม **ปกติ** · เริ่มหลังได้ยา **นาน (~30 เดือน)** · **Doppler ไม่มี hypervascularity** · **RAIU ถูกกด** = **AIT type 2** (destructive thyroiditis — ยาทำลายเซลล์ ฮอร์โมนเก่ารั่ว)\n\nรักษา **glucocorticoid — prednisone 40 mg/วัน** · ATD ไม่ช่วยเพราะไม่มีการสร้างใหม่ · RAI ใช้ไม่ได้เพราะต่อมไม่ดูด (และร่างกายเต็มไปด้วยไอโอดีน)\n\nถ้าแยกไม่ได้หรือหัวใจไม่เสถียร ให้ MMI + prednisone ร่วมกัน",
         "AIT 2: ต่อมปกติ Doppler ไม่เพิ่ม onset ช้า → prednisone", "Amiodarone-induced thyrotoxicosis",
         ["ETA 2018 Guidelines for amiodarone-associated thyroid dysfunction (Eur Thyroid J 2018;7:55)"], ["2.3.4(9)", "B11.4(2)"]),
     mcq(N(24), "A 66-year-old woman with Hashimoto's thyroiditis (positive anti-TPO) develops fatigue and a TSH of 18 mIU/L 4 months after starting amiodarone for atrial fibrillation. Amiodarone is controlling her arrhythmia well. What is the best management?",
         ["Stop amiodarone permanently", "Start methimazole", "Start levothyroxine and continue amiodarone", "Give prednisone 40 mg/day", "Radioactive iodine ablation"], 2,
         "ไอโอดีนเกินจาก amiodarone ทำให้เกิด **Wolff–Chaikoff effect** (กด organification) ต่อมปกติ **หนีออก (escape)** ได้ใน 1–2 สัปดาห์ แต่ **ต่อมที่มี Hashimoto หนีไม่ได้** → **amiodarone-induced hypothyroidism**\n\nรักษาด้วย **levothyroxine** และ **ให้ amiodarone ต่อได้** เมื่อยาจำเป็นต่อการคุมหัวใจ",
         "Hypothyroid จาก amiodarone → LT4 + ใช้ amiodarone ต่อ", "Amiodarone-induced hypothyroidism",
         ["ETA 2018 (Eur Thyroid J 2018;7:55)"], ["2.3.4(4)", "B11.4(2)"])],
    ["2.3.4(9)", "2.3.4(4)", "2.3.4(5)", "B11.4(2)"])

# ───────────────────────────── 13
sec("endo-th-13", "ก้อนที่คอ — ทำงานไหม แล้วร้ายไหม",
    "TSH ก่อน · ต่ำ → scan · ปกติ → US pattern + FNA ตามขนาด · Bethesda 2023 I–VI", 9,
"""### นิยาม (สไลด์)
**Goiter** = ต่อมโต · **Nodule** = รอยโรคที่ **แยกจากเนื้อต่อมรอบข้างได้ชัดในภาพรังสี**
Goiter แบ่งตามสถานะเป็น euthyroid, thyrotoxic, hypothyroid · ก้อนส่วนใหญ่ (~95%) ไม่ใช่มะเร็ง ที่เหลือส่วนใหญ่เป็น papillary

### Case ในสไลด์
ชาย 45 ปี **ก้อนคอขวา 8 เดือน** ไม่ใจสั่น น้ำหนักไม่ลด PR 80 **FT3 FT4 TSH ปกติ** → euthyroid single nodule — คำถามเดียวที่เหลือคือ **ร้ายไหม**

### Algorithm (สไลด์)
**ประวัติ ตรวจร่างกาย + TSH + อัลตราซาวด์**
| TSH | ทำต่อ |
|---|---|
| **ต่ำ** | FT4/FT3, TRAb, **thyroid scintigraphy** → **hot = ไม่ต้อง FNA** · cold → ประเมินแบบก้อนทั่วไป |
| **ปกติ** | **US risk stratification ± FNA ± molecular test** |
| **สูง** | FT4, **anti-TPO/Tg** — อาจเป็น pseudonodule ของ Hashimoto |

ซักเพิ่มเรื่องความเสี่ยง — **ฉายแสงที่คอตอนเด็ก**, ประวัติครอบครัวมะเร็งไทรอยด์/MEN2, **เสียงแหบ กลืนลำบาก ก้อนโตเร็ว ต่อมน้ำเหลืองคอโต**

### ATA ultrasound pattern และเกณฑ์ FNA *(ATA 2015 — สไลด์ส่วนนี้ดึงข้อความไม่ได้)*
| Pattern | เสี่ยงมะเร็ง | FNA เมื่อ | ลักษณะ |
|---|---|---|---|
| **High** | > 70–90% | **≥ 1 cm** | solid hypoechoic + **microcalcification, ขอบไม่เรียบ, taller-than-wide**, ลามนอกต่อม |
| Intermediate | 10–20% | **≥ 1 cm** | solid hypoechoic ขอบเรียบ |
| Low | 5–10% | **≥ 1.5 cm** | iso/hyperechoic solid หรือ partially cystic มีส่วน solid เยื้อง |
| Very low | < 3% | **≥ 2 cm** (หรือติดตาม) | spongiform |
| Benign | < 1% | ไม่ต้อง | **pure cyst** |

### Bethesda 2023
| | ผล | เสี่ยงมะเร็ง | ทำต่อ |
|---|---|---|---|
| I | Nondiagnostic | 13% | **เจาะซ้ำ** ใต้ US |
| II | **Benign** | 4% | ติดตาม |
| III | AUS | 22% | เจาะซ้ำ / molecular / ผ่าตัด |
| IV | **Follicular neoplasm** | 30% | **lobectomy** หรือ molecular |
| V | Suspicious for malignancy | 74% | total/near-total หรือ molecular |
| VI | **Malignant** | 97% | **total/near-total thyroidectomy** |

> **Follicular บอกไม่ได้จากเข็ม** — carcinoma ต่างจาก adenoma ที่ **การทะลุ capsule/หลอดเลือด** ต้องเห็นทั้งก้อน → Bethesda IV จบที่ lobectomy""",
    ["ก้อนไทรอยด์: TSH ก่อน — ต่ำ → scan (hot ไม่ต้อง FNA) · ปกติ → US + FNA",
     "FNA: high/intermediate ≥ 1 cm · low ≥ 1.5 · very low ≥ 2 · pure cyst ไม่ต้อง",
     "Bethesda II benign → ติดตาม · IV follicular → lobectomy · VI → total thyroidectomy"],
    [mcq(N(25), "A 45-year-old man has an 8-month right neck mass with normal TSH, FT4 and FT3. Ultrasound shows a 1.3-cm solid hypoechoic nodule with irregular margins, microcalcifications and a taller-than-wide shape. What is the next step?",
         ["Thyroid scintigraphy", "Repeat ultrasound in 12 months", "Ultrasound-guided fine-needle aspiration", "Start levothyroxine suppression", "Radioactive iodine therapy"], 2,
         "TSH ปกติ → algorithm ในสไลด์ไปที่ **US risk stratification ± FNA** (scan ใช้เมื่อ **TSH ต่ำ** เท่านั้น)\n\nลักษณะ **solid hypoechoic + microcalcification + ขอบไม่เรียบ + taller-than-wide** = **ATA high suspicion** (เสี่ยงมะเร็ง > 70–90%) → **FNA เมื่อ ≥ 1 cm** — ก้อน 1.3 cm จึง **ต้องเจาะ**\n\nLevothyroxine suppression ไม่แนะนำแล้ว · RAI ไม่มีบทบาทก่อนวินิจฉัย",
         "TSH ปกติ + high-suspicion pattern ≥ 1 cm → FNA", "Thyroid nodule evaluation",
         [R("Euthyroid single or multiple nodule – algorithm"), "ATA 2015 Thyroid Nodule Guideline"], ["2.1.53", "B11.2.4-3(1)", "B11.2.4-3(2)"]),
     mcq(N(26), "FNA of a 2.5-cm thyroid nodule is reported as Bethesda category IV (follicular neoplasm). Why can FNA not distinguish follicular adenoma from follicular carcinoma, and what is the usual next step?",
         ["Because follicular cells do not stain; repeat FNA", "Because carcinoma is defined by capsular or vascular invasion, which requires histology of the whole nodule; diagnostic lobectomy (or molecular testing)",
          "Because follicular carcinoma secretes calcitonin; measure calcitonin", "Because the nodule is too large; observe", "Because follicular lesions are always benign; discharge"], 1,
         "**Follicular carcinoma** ต่างจาก **adenoma** ที่ **การรุกทะลุ capsule หรือหลอดเลือด** ไม่ใช่ลักษณะของเซลล์ — FNA ดูได้แค่เซลล์ จึงต้องได้ **ทั้งก้อน** มาตรวจ\n\nBethesda IV (เสี่ยงมะเร็งราว 30%) → **lobectomy เพื่อวินิจฉัย** หรือใช้ **molecular testing** ช่วยคัด · calcitonin ใช้กับ **medullary carcinoma** (C cell)",
         "Bethesda IV → lobectomy เพราะต้องดูการทะลุ capsule", "Bethesda category IV",
         ["Bethesda System for Reporting Thyroid Cytopathology 2023"], ["B11.2.4-3(2)", "3.3.11", "2.1.53"])],
    ["2.3.4(3)", "2.1.53", "B11.2.4-3(1)", "B11.2.4-3(2)"])


LECNAME = "Thyroid disorders (อ.ศิวกร)"
MEQ = [{"id": "END-MEQ-02", "part": "MEQ", "lec": "14", "lecture": LECNAME,
 "topic": "Graves' disease — diagnosis, initial therapy, drug toxicity and definitive options",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 35 ปี อาชีพพนักงานบัญชี มาโรงพยาบาลด้วยอาการน้ำหนักลด 6 กิโลกรัมใน 6 เดือน
PI: 6 เดือนก่อน ใจสั่น มือสั่น ขี้ร้อน เหงื่อออกมาก กินเก่งขึ้นแต่น้ำหนักลด ถ่ายวันละ 3 ครั้ง ประจำเดือนมาน้อยลง 2 เดือนก่อนเพื่อนทักว่าตาโปน
PH: ไม่มีโรคประจำตัว สูบบุหรี่วันละ 5 มวน ใช้ถุงยางอนามัยคุมกำเนิด LMP 2 สัปดาห์ก่อน
PE: BT 37.4 C, PR 120/min regular, BP 138/62 mmHg, RR 18/min
Eyes: lid retraction, lid lag, proptosis ทั้งสองข้าง ไม่มี diplopia
Neck: diffuse goiter grade II, soft, non-tender, **thyroid bruit** ได้ยินทั้งสองข้าง
Skin: warm, moist · fine tremor · ไม่มี pretibial myxedema
Lab: FT4 3.0 ng/dL (0.8–1.8), FT3 8.4 pg/mL (1.6–4), TSH < 0.001 mIU/L (0.3–4.1)""",
 "questions": [
  {"q": "1. จงบอกการวินิจฉัย พร้อมเหตุผลที่สนับสนุนจากประวัติและตรวจร่างกาย และการตรวจเพิ่มที่ควรส่งก่อนเริ่มยา (4 คะแนน)",
   "a": """**การวินิจฉัย: Graves' disease (primary hyperthyroidism)**
- TFT: **FT4 และ FT3 สูง TSH ถูกกด** = primary thyrotoxicosis
- เป็นมา **6 เดือน** (thyroiditis มักไม่เกิน 6–8 สัปดาห์)
- **ป้ายชื่อของ Graves** — **proptosis** (TRAb กระตุ้น fibroblast หลังลูกตา) + **diffuse goiter + thyroid bruit**
- อายุ 30–50 ปี เพศหญิง

**ส่งเพิ่มก่อนเริ่มยา**
| ตรวจ | เหตุผล |
|---|---|
| **TRAb** | ยืนยัน Graves + เป็นค่าตั้งต้นใช้ตัดสินหยุดยา/ทำนาย relapse |
| **CBC with differential** | ค่าพื้นฐานก่อนยาที่อาจทำ agranulocytosis |
| **LFT** | ค่าพื้นฐาน (hepatotoxicity) · thyrotoxicosis เองก็ทำ LFT ผิดปกติได้ |
| **Urine pregnancy test** | เลือก MMI หรือ PTU |
| (RAIU ไม่จำเป็นเมื่ออาการเข้าได้ชัดและ TRAb บวก) | |"""},
  {"q": "2. จงเขียนการรักษาเริ่มต้น พร้อมขนาดยา (3 คะแนน)",
   "a": """**1. β-blocker คุมอาการทันที** — propranolol 20–40 mg วันละ 3–4 ครั้ง (ไม่มีหอบหืด) · ขนาดสูงลด T4 → T3
**2. Methimazole เป็นยาแรก** — FT4 3.0/1.8 = **1.7 × ULN → 10–20 mg/วัน** · FT3 สูงมากและคอพอก grade II → เลือก **20 mg วันละครั้ง**
**3. ติดตาม FT4 + T3 ที่ 4–6 สัปดาห์** ปรับยาตาม FT4/T3 (TSH ฟื้นช้า) ลดถึงขนาดต่ำสุด 2.5–5 mg/วัน
**4. แนะนำเลิกบุหรี่** — ลดความเสี่ยงตาแย่ลงและ relapse · คุมกำเนิดต่อเนื่อง"""},
  {"q": "3. หลังเริ่มยา 5 สัปดาห์ ผู้ป่วยมีไข้ 39 องศา เจ็บคอมาก CBC: WBC 1,200/mm³ ANC 200/mm³ จงบอกภาวะ การจัดการ และแผนรักษาไทรอยด์ต่อ (3 คะแนน)",
   "a": """**ภาวะ: Methimazole-induced agranulocytosis (febrile neutropenia)** — ANC < 500 · พบ 0.2–0.5% มักใน 3 เดือนแรก
**จัดการ**
- **หยุด methimazole ทันทีและถาวร**
- รับไว้ เพาะเชื้อ ให้ **ยาปฏิชีวนะครอบคลุมกว้าง (anti-pseudomonal)** ± **G-CSF**
**แผนไทรอยด์ต่อ**
- **ห้ามสลับเป็น PTU** — cross-reactivity
- คุมอาการด้วย **propranolol** (± iodine/cholestyramine ระยะสั้น)
- Definitive: **total thyroidectomy** (เหมาะที่สุดในรายนี้เพราะมีตาโปน) หรือ RAI เมื่อพร้อม"""},
  {"q": "4. ถ้าผู้ป่วยไม่ได้แพ้ยา และรักษาครบ 18 เดือน ปัจจัยใดทำนายการกลับเป็นซ้ำ และจะตัดสินใจหยุดยาอย่างไร (2 คะแนน)",
   "a": """**ปัจจัยทำนาย relapse** — **TRAb (แรงที่สุด)** · คอพอกใหญ่ · FT4 แรกเริ่มสูง · อายุน้อย · ตาโปน · **สูบบุหรี่** · ช่วงหลังคลอด
GREAT score ของรายนี้: อายุ < 40 (+1) · FT4 3.0 ng/dL ≈ 39 pmol/L (0) · goiter grade II (+2) · TRAb (ตามค่าจริง) → อย่างน้อย class II (relapse ~44%)
**หยุดยาได้เมื่อ TSH และ TRAb ปกติ** · TRAb ยังสูง → ต่ออีก 12 เดือน หรือ RAI/ผ่าตัด หรือ MMI ขนาดต่ำระยะยาว"""},
  {"q": "5. ผู้ป่วยถามว่าทำไมไม่ใช้ \"น้ำแร่รังสี (RAI)\" เพราะเพื่อนหายด้วยวิธีนี้ จงตอบ (2 คะแนน)",
   "a": """- RAI ทำให้หายได้ **> 90%** แต่ **อาจทำให้ตาโปนแย่ลง** โดยเฉพาะ **ผู้สูบบุหรี่** — รายนี้มี proptosis และสูบบุหรี่ จึงควรเลือก **ATD หรือผ่าตัด** ก่อน หรือถ้าใช้ RAI ต้องมี **steroid คลุม**
- RAI **ห้ามในการตั้งครรภ์/ให้นม** และต้องคุมกำเนิดหลังทำ 4–6 เดือน
- ผลระยะยาวส่วนใหญ่คือ **hypothyroidism ต้องกิน levothyroxine ตลอดชีวิต**"""}],
 "ref": [R("Case 35 yr woman, Graves' disease, ATD start/monitor/stop, RAI, surgery, GREAT score"), "ATA 2016 (Thyroid 2016;26:1343)"],
 "nl": ["2.3.4(9)", "B11.2.5(2)", "B11.4(2)", "B11.3(3)", "2.1.9", "2.1.36"], "years": [], "_kind": "meq", "_set": "endo"}]

OSCE = [{"id": "END-OSCE-02", "part": "OSCE/SAQ", "lec": "14", "lecture": LECNAME,
 "topic": "OSCE – Thyroid examination and methimazole counselling",
 "station": "สถานีตรวจร่างกาย + สื่อสารกับผู้ป่วยจำลอง 8 นาที",
 "instruction": """หญิงอายุ 30 ปี ใจสั่น น้ำหนักลด 3 เดือน แพทย์สงสัย Graves' disease

**ส่วนที่ 1 (5 นาที)** จงตรวจต่อมไทรอยด์และอาการแสดงของไทรอยด์เป็นพิษให้ผู้คุมสอบดู พร้อมบอกสิ่งที่กำลังตรวจ
**ส่วนที่ 2 (3 นาที)** ผลยืนยันเป็น Graves' disease แพทย์จะเริ่ม methimazole 15 mg/วัน จงให้คำแนะนำการใช้ยาแก่ผู้ป่วย

หมายเหตุสำหรับผู้ป่วยจำลอง: แต่งงานแล้ว ยังไม่มีบุตร "อยากมีลูกปีหน้า" · ถ้าไม่ถูกถามจะไม่บอกว่าอาจตั้งครรภ์""",
 "answer": """**ส่วนที่ 1 — ตรวจร่างกาย (ลำดับที่ได้คะแนน)**
| ขั้น | สิ่งที่ทำ | สิ่งที่มองหา |
|---|---|---|
| แนะนำตัว ขออนุญาต ล้างมือ | ให้ผู้ป่วยนั่ง เปิดคอ | — |
| **มือ** | ยื่นมือ วางกระดาษบนหลังมือ · จับชีพจร | **fine tremor**, palmar erythema, เหงื่อ, **ชีพจรเร็ว/AF**, acropachy |
| **ตา** | มองจากด้านหน้าและ **จากด้านบนศีรษะ** · ให้มองตามนิ้วลงล่าง · ตรวจ EOM | **lid retraction, lid lag, proptosis**, chemosis, diplopia |
| **คอ — ดูจากด้านหน้า** | ให้ **กลืนน้ำ** (ต่อมเลื่อนขึ้น) · **แลบลิ้น** (thyroglossal cyst เลื่อน ต่อมไม่เลื่อน) | ขนาด สมมาตร แผลเป็น |
| **คอ — คลำจากด้านหลัง** | คลำทีละกลีบ ให้กลืนขณะคลำ · คลำต่อมน้ำเหลือง | diffuse/nodular, นุ่ม/แข็ง, **กดเจ็บ** |
| เคาะ | กระดูก sternum | retrosternal extension |
| **ฟัง** | stethoscope บนต่อมทั้งสองกลีบ (กลั้นหายใจ) | **thyroid bruit** (Graves) |
| อื่น ๆ | **proximal myopathy** (ลุกจากเก้าอี้กอดอก) · **pretibial myxedema** · reflex | |
| สรุป | รายงานผลและขอบคุณผู้ป่วย | |

**ส่วนที่ 2 — Counselling methimazole**
- ชื่อยา จุดประสงค์ (ลดการสร้างฮอร์โมน) **กินวันละครั้ง** ใช้เวลา 4–6 สัปดาห์กว่าจะดีขึ้น ระยะรักษา **12–18 เดือน** ห้ามหยุดยาเอง
- **อาการเตือนที่ต้องหยุดยาและมาโรงพยาบาลทันที** — **ไข้ เจ็บคอ แผลในปาก** (เจาะ CBC) · **ตัวเหลือง ปัสสาวะสีเข้ม ปวดท้องขวาบน** (ตรวจตับ) · ผื่นมาก ปวดข้อ
- **ถามเรื่องการตั้งครรภ์** — LMP · วางแผนมีบุตร → **คุมกำเนิดระหว่างใช้ MMI** · ถ้าตั้งครรภ์ให้มาพบแพทย์ทันทีเพื่อเปลี่ยนเป็น **PTU ในไตรมาสแรก** (MMI ทำให้ทารกพิการได้) · ปรึกษาวางแผนก่อนมีบุตร
- เลิกบุหรี่ (ถ้าสูบ) · นัดเจาะเลือดตามนัด · ใช้ propranolol คุมใจสั่นระหว่างรอ
- ตรวจสอบความเข้าใจ (teach-back) และเปิดโอกาสให้ถาม

**ข้อที่ทำให้เสียคะแนน**: ไม่ให้กลืนน้ำ/แลบลิ้น · ไม่ฟัง bruit · ลืมบอกอาการ agranulocytosis · ไม่ถามเรื่องตั้งครรภ์""",
 "ref": [R("Graves' disease signs; Antithyroid drug"), "ATA 2016 – counselling before ATD"],
 "nl": ["2.3.4(9)", "B11.4(2)", "2.1.53", "B11.2.5(2)"], "years": [], "_kind": "meq", "_set": "endo"}]

LECTURE = {
 "lec": "14",
 "date": "พ. 30 ก.ย.",
 "title": "Thyroid disorders",
 "subtitle": "แกน HPT และ deiodinase · ถอดรหัส TFT · thyrotoxicosis vs hyperthyroidism และ RAIU · อาการตามกลไก · Graves vs thyroiditis · ATD (MMI/PTU) ผลข้างเคียงและการตั้งครรภ์ · RAI ผ่าตัด GREAT score · toxic nodule และ thyroid storm · hypothyroidism และ levothyroxine · amiodarone · thyroid nodule และ Bethesda",
 "objectives": [
   "อธิบายแกน HPT การทำงานของ deiodinase และข้อจำกัดของ TSH (central, ช่วงรักษา, ป่วยหนัก)",
   "แปลผล TFT ทุกรูปแบบ รวมถึง T3/T4 toxicosis, inappropriate TSH และ central hypothyroidism",
   "แยก hyperthyroidism ออกจาก thyrotoxicosis without hyperthyroidism ด้วย RAIU, TRAb และลักษณะต่อม",
   "วินิจฉัยและรักษา Graves' disease ด้วย ATD ตามขนาด FT4 รวมถึงการติดตาม หยุดยา ผลข้างเคียง และการตั้งครรภ์",
   "เลือกระหว่าง ATD, RAI และผ่าตัด และใช้ GREAT score ทำนายการกลับเป็นซ้ำ",
   "จำแนก thyroiditis สามชนิดและรักษา subacute thyroiditis ได้ถูกต้อง",
   "วินิจฉัยและรักษา hypothyroidism, amiodarone-associated thyroid dysfunction และภาวะฉุกเฉิน (thyroid storm, myxedema coma)",
   "ประเมิน thyroid nodule ด้วย TSH, scan, US pattern, FNA และ Bethesda 2023"],
 "nlGap": "**ข้อความในสไลด์ถูกตัดหลัง algorithm ของ thyroid nodule** (เครื่องมือดึงข้อความได้ไม่ครบ) — ส่วน **hypothyroidism, amiodarone, ultrasound pattern และ Bethesda, ตารางผลข้างเคียงของ ATD** เทียบจาก **บทเรียน Thyroid ที่ผู้ใช้ทำไว้จากสไลด์ชุดเดียวกัน** และแนวทางด้านล่าง · **Thyroid storm และ myxedema coma** ไม่อยู่ในส่วนที่ดึงได้ (เกณฑ์ฯ จัด `นล. 2.3.4-3(3)` เป็น **กลุ่ม 3 วินิจฉัยแล้วส่งต่อ**) จึงเรียบเรียงจาก ATA 2016/JTA 2016 และ ATA 2014 · เกณฑ์ฯ **ไม่มีรหัสของ amiodarone-induced thyroid dysfunction และ Bethesda** โดยตรง (อยู่ใต้ `B11.4(2)` และ `B11.2.4-3`) ถ้าได้ภาพสไลด์ส่วนท้ายมา ให้เทียบแล้วแก้ `build_thyroid.py`",
 "guidelines": [
   "**ATA 2016 — Guidelines for the Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis** (Thyroid 2016;26:1343) — อาจารย์อ้างในสไลด์ (ATD, RAI, surgery, thyroid storm)",
   "**ETA 2018** — Graves' hyperthyroidism (Eur Thyroid J 2018;7:167) และ amiodarone-associated thyroid dysfunction (Eur Thyroid J 2018;7:55)",
   "**ATA 2014 — Guidelines for the Treatment of Hypothyroidism** (Thyroid 2014;24:1670)",
   "**ATA 2015 — Thyroid Nodules and Differentiated Thyroid Cancer** · **Bethesda System 2023**",
   "**ATA 2017 — Thyroid Disease During Pregnancy and the Postpartum**",
   "**GREAT score** (JCEM 2016;101:1381) · **long-term MMI RCT** (Thyroid 2019;29:1192) · **JCEM 2024;109:e1881**",
   "**แนวทางเวชปฏิบัติโรคต่อมไร้ท่อและเมตะบอลิสม พ.ศ. 2563** (อาจารย์อ้างเรื่อง destructive thyroiditis)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ── ตรวจก่อนเขียน
path = os.path.join(BUILD, "data", "endo.json")
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
    if m["set"] == "endo": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d | nl codes %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE), len(codes)))
print("endo.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
