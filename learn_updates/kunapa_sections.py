# -*- coding: utf-8 -*-
"""หัวข้อใหม่จากสไลด์ อ.Kunapa Lam-arunthai — Approach to anemia (ไฟล์ใน Drive: "Approach to anemia (2).pdf", อัปโหลด 9 พ.ย. 2569)
แทรกเข้าคาบ 9/11 ของ data/hemonc.json ในอาร์ติแฟกต์ MED421 learn"""

SRC = "สไลด์ อ.Kunapa Lam-arunthai — Approach to anemia (คาบ 9 พ.ย. 2569) + โน้ตลายมือในสไลด์ (✍️)"
REF_SLIDE = "สไลด์ อ.Kunapa Lam-arunthai — Approach to anemia (MED421 · 9 พ.ย. 2569)"

def q(id, topic, stem, choices, answer, explain, pearl, ref, nl):
    return {"id": id, "kind": "mcq", "topic": topic, "stem": stem, "choices": choices,
            "answer": answer, "explain": explain, "pearl": pearl, "src": "", "ref": ref, "nl": nl}

# ---------------------------------------------------------------- K1
K1_MD = r"""### สไลด์คาบจริง — อ่านคู่กับหัวข้อ Approach ด้านบน
หัวข้อนี้สรุปจาก **สไลด์ Approach to anemia ของ อ.Kunapa Lam-arunthai** ที่ใช้สอนในคาบ 9 พ.ย. — ส่วนที่ขึ้นต้นด้วย ✍️ คือโน้ตลายมือในสไลด์ ส่วนที่ระบุว่า **(เสริม)** เป็นของบทเรียนนี้ · ตรงไหนที่สไลด์ใช้ตัวเลขต่างจากหัวข้อ Approach ด้านบน มีกล่องบอกไว้

### นิยาม — red cell mass ลดลง
| ค่า (WHO) | หญิง | ชาย |
|---|---|---|
| Hemoglobin (g/dL) | **< 12** | **< 13** |
| Hematocrit (%) | **< 36** | **< 39** |
| RBC (×10⁶/µL) ช่วงปกติ | 4.0–5.4 | 4.5–6.0 |
| MCV (fL) ช่วงปกติ | 80–100 | 80–100 |

**ซีดในหญิงตั้งครรภ์**
- เกณฑ์: **Hb < 11.0 g/dL ไตรมาสแรก** · **< 10.5 (หรือ 11.0) ไตรมาส 2–3**
- เป็นความผิดปกติทางโลหิตวิทยาที่ **พบบ่อยที่สุดในการตั้งครรภ์** และสาเหตุอันดับหนึ่งคือ **ขาดเหล็ก**
- **ต้องสืบค้นเพิ่ม** เมื่อ: ซีดเล็กน้อยแต่ **MCV ต่ำมาก** (คิดถึง thal trait) · **macrocytic** · ซีดปานกลาง **Hb 7.0–9.9** · ซีดรุนแรง **Hb 4.0–6.9**

### อาการและอาการแสดงแยกตามระบบ
| ระบบ | อาการ/อาการแสดง |
|---|---|
| ผิวหนัง | ซีดที่ผิวและเยื่อบุ · ตัวเย็น · เหลือง · **glossitis** · เล็บเปราะ · ผมหงอกก่อนวัย |
| หายใจ | หอบเหนื่อย |
| กล้ามเนื้อ | อ่อนแรง |
| ประสาท | เพลีย · มึนงง · เป็นลม · vertigo |
| หัวใจหลอดเลือด | ใจสั่น · angina/เจ็บหน้าอก · heart attack · **congestive heart failure** · postural hypotension · **systolic ejection murmur** |
| ทางเดินอาหาร | กลืนลำบาก · สีอุจจาระเปลี่ยน · ขับถ่ายเปลี่ยน · ปวดใต้ลิ้นปี่ |
- อาการแสดงที่สไลด์ย้ำใน diagnostic approach: **pale conjunctiva/buccal mucosa · wide pulse pressure · systolic murmur at apex**

### ตั้งต้นด้วย 3 แกน — onset · pathogenesis · MCV
**1. Onset**
| Acute (≤ 2–3 สัปดาห์) | Subacute | Chronic (> 3 เดือน) |
|---|---|---|
| **blood loss · hemolysis · hemodilution** | **stem cell disease**: aplastic anemia · acute leukemia · PRCA · myelophthisis | **nutritional deficiency · ACD · thalassemia · MDS · endocrine · CKD** |

> **Kunapa · ต่างจากหัวข้อ Approach** — สไลด์นับ acute ถึง **2–3 สัปดาห์** และ chronic **> 3 เดือน** (หัวข้อด้านบนใช้ acute < 1 สัปดาห์ · chronic > 2–3 เดือน) · และสไลด์เพิ่ม **hemodilution** ในกลุ่ม acute — ตอบข้อสอบในคาบให้ยึดตัวเลขของสไลด์

**2. Pathogenesis — 4 กลไก**
1. **Hypoproliferative anemia** — พบ **~75%** ของทั้งหมด · ไขกระดูกเพิ่มการสร้างไม่สมกับความซีด
2. **Ineffective erythropoiesis (maturation defect)** — เซลล์ตัวอ่อนตายในไขกระดูก
3. **Hemolytic anemia**
4. **Acute blood loss**

**3. MCV** — < 80 · 80–100 · > 100 fL (ตารางท้ายหัวข้อ)

### Acute blood loss — ประเมินจากอาการ
| % เสียเลือด | ปริมาตร (mL) | อาการ | อาการแสดง |
|---|---|---|---|
| < 20 | < 1,000 | กระสับกระส่าย | ± vasovagal reaction |
| 20–30 | 1,000–1,500 | เหนื่อยเมื่อออกแรง | **orthostatic hypotension** · ชีพจรเร็วเมื่อออกแรง |
| 30–40 | 1,500–2,000 | **เป็นลม (syncope)** | orthostatic hypotension · **ชีพจรเร็วขณะพัก** |
| > 40 | > 2,000 | **สับสน** | **shock** |
- (เสริม) ชั่วโมงแรกของเสียเลือด Hb ยังไม่ลด — ใช้ **vital signs และ orthostatic change** ประเมิน ไม่ใช่ Hb

### Hemolytic anemia
- อายุ RBC สั้นลง (ปกติ **90–120 วัน**) · reticulocyte เพิ่มตามความสามารถของไขกระดูกที่ชดเชย
- ✍️ smear เห็น **polychromasia** · แล็บ **LDH ↑ · haptoglobin ↓**
- แบ่งเป็น **intravascular** และ **extravascular** — (เสริม) intravascular: hemoglobinemia · **hemoglobinuria · urine hemosiderin** · haptoglobin ต่ำมาก · extravascular: ม้าม/ตับเก็บ → เหลือง **ม้ามโต**

| Congenital (ความผิดปกติในตัวเม็ดเลือด) | Acquired |
|---|---|
| **Membrane** — hereditary spherocytosis | **PNH** |
| **Enzyme** — G-6-PD deficiency | **Immune** — AIHA · hemolytic transfusion reaction |
| **Globin** — thalassemia · hemoglobinopathy | **Infection** — malaria · clostridial infection |
| | **Microangiopathy** — TTP/HUS |
| | **Drug/chemical** — lead poisoning |
- ✍️ **PNH = pancytopenia + intravascular hemolysis + thrombosis in unusual site** (หลอดเลือดดำในช่องท้อง ตับ สมอง)

### Hypoproliferative anemia (75%)
ไขกระดูกฝั่งเม็ดเลือดแดงไม่เพิ่มการสร้างให้สมกับความซีด — สาเหตุ:
- **Iron deficiency anemia · anemia of chronic disease**
- **Anemia of CKD · hypothyroidism**
- **Infiltrative marrow disease** — leukemia · lymphoma · solid tumor · infection · myelofibrosis
- **ยา สารเคมี รังสี**
- **Stem cell disease** — aplastic anemia · MDS · PRCA

### Ineffective erythropoiesis — 2 แบบ
| Nuclear maturation defect | Cytoplasmic maturation defect |
|---|---|
| **macrocytosis** + ไขกระดูกผิดปกติ | **microcytosis + hypochromia** |
| folate/B12 deficiency · ยา (**MTX**, alkylating agents) · MDS · alcohol | **thalassemia · sideroblastic anemia** |
- (เสริม) จำง่าย: **นิวเคลียสช้า → เซลล์ใหญ่** (DNA สร้างไม่ทัน แต่ไซโทพลาสซึมโตต่อ) · **ไซโทพลาสซึมช้า → เซลล์เล็ก** (Hb ไม่พอ เซลล์แบ่งตัวเพิ่มอีกรอบ)

### Morphologic approach — MCV
| MCV < 80 fL | MCV 80–100 fL | MCV > 100 fL |
|---|---|---|
| Iron deficiency anemia | Iron deficiency anemia (**ระยะแรก**) | **Megaloblastic anemia** |
| Thalassemia | Hemolysis | Non-megaloblastic — **โรคตับ สุรา hypothyroidism** |
| Anemia of chronic disease | Anemia of CKD | Primary marrow disorder — **AA · MDS** |
| Sideroblastic anemia | Acute blood loss | ยา — **AZT · hydroxyurea · chemotherapy** |
| ซีดจากเหตุอื่น + มี thal ซ่อนอยู่ | Bone marrow disease | |
| **Copper deficiency** · **zinc poisoning** (พบน้อย) | Endocrine disorder · ACD | |
- (เสริม) **zinc เกิน → ขัดการดูดซึม copper** จึงอยู่กลุ่มเดียวกัน — ผู้ป่วยกินแร่ธาตุเสริมหรือผ่าตัดกระเพาะ เจอ anemia + neutropenia + ไขสันหลังเสื่อมคล้าย B12

### อาการร่วมที่ชี้ทาง (สไลด์ diagnostic approach)
| สิ่งที่พบ | นึกถึง |
|---|---|
| **ตัวเหลืองตาเหลือง** | hemolysis |
| **Hemodynamics ไม่คงที่** | acute blood loss |
| **ตับม้ามโต** → สนับสนุนเหตุทางโลหิตวิทยา | lymphoma · acute leukemia · thalassemia · HS · AIHA |
| **Glossitis + koilonychia** | iron deficiency |
| **เสีย position + vibration sense** | B12 deficiency |
| **มีเลือดออกผิดปกติ** | bone marrow disease |
| **ปวดกระดูก** | multiple myeloma |
"""

K1 = {
  "id": "hon-anm-k1",
  "title": "สไลด์ อ.Kunapa ① — นิยาม onset 4 กลไก และ MCV",
  "minutes": 14,
  "summary": "WHO: Hb < 12 หญิง · < 13 ชาย · ตั้งครรภ์ < 11 (ไตรมาสแรก) · onset acute ≤ 2–3 สัปดาห์ / chronic > 3 เดือน · 4 กลไก: hypoproliferative (75%) · ineffective · hemolysis · blood loss · ตารางเสียเลือด 4 ระดับ · hemolysis congenital vs acquired · MCV 3 กลุ่ม",
  "source": SRC,
  "nl": ["2.1.56", "3.3.1", "B2.3(2)", "2.3.3(4)", "2.2.44", "2.3.3(7)", "2.3.3(8)"],
  "md": K1_MD,
  "pearls": [
    "สไลด์ อ.Kunapa: acute ≤ 2–3 สัปดาห์ (blood loss · hemolysis · hemodilution) · subacute = stem cell disease · chronic > 3 เดือน",
    "Hypoproliferative anemia พบ ~75% — IDA ACD CKD hypothyroid infiltration ยา stem cell disease",
    "Ineffective erythropoiesis: nuclear defect = macrocytic (B12 folate MTX MDS alcohol) · cytoplasmic defect = microcytic (thal sideroblastic)",
    "เสียเลือด 30–40% = syncope + ชีพจรเร็วขณะพัก · > 40% = สับสน + shock",
    "PNH = pancytopenia + intravascular hemolysis + thrombosis ในตำแหน่งแปลก",
    "ตั้งครรภ์: ซีดเล็กน้อยแต่ MCV ต่ำมาก · macrocytic · Hb < 10 → ต้องสืบค้นเพิ่ม",
  ],
  "items": [
    q("HON-ANM-MCQ-K01", "Acute blood loss — class by clinical signs",
      "A 45-year-old man is brought in after vomiting a large amount of fresh blood. He fainted at home. He is alert and oriented. Supine HR 122/min and BP 104/68 mmHg; sitting up makes him dizzy with a further fall in BP. Hb 12.1 g/dL. Approximately how much of his blood volume has he lost?",
      ["Less than 20% (under 1,000 mL), because the Hb is still above 12 g/dL",
       "20–30% (1,000–1,500 mL), because he only has orthostatic symptoms",
       "30–40% (1,500–2,000 mL)",
       "More than 40% (over 2,000 mL), because he fainted",
       "It cannot be estimated until the Hb is repeated in 24 hours"],
      2,
      "ใช้ตาราง acute blood loss ในสไลด์ อ.Kunapa ซึ่งประเมินจาก **อาการและ vital signs** ไม่ใช่ Hb\n\n- **Syncope + ชีพจรเร็วขณะพัก (122/min) + orthostatic hypotension** = ระดับ **30–40% (1,500–2,000 mL)**\n- ระดับ > 40% ต้องมี **สับสนและ shock** — ผู้ป่วยยังรู้สึกตัวดี ความดันขณะนอนยังพอ\n- 20–30% มีแค่เหนื่อยเมื่อออกแรง orthostatic และชีพจรเร็ว **เมื่อออกแรง** ไม่ใช่ขณะพัก\n- **Hb 12.1 ยังไม่ลด** เพราะชั่วโมงแรกเสียทั้ง RBC และพลาสมาในสัดส่วนเดียวกัน — Hb ลดลงเมื่อร่างกายดึงน้ำเข้าหลอดเลือดหรือได้น้ำเกลือ (หลายชั่วโมงถึง 1–2 วัน) จึงห้ามใช้ Hb แรกรับบอกปริมาณเสียเลือด\n- ไม่ต้องรอ Hb ซ้ำ — ประเมินได้ทันทีจากอาการและต้อง resuscitate ตอนนี้",
      "เสียเลือด 30–40% = syncope + ชีพจรเร็วขณะพัก · > 40% = สับสน + shock · Hb ชั่วโมงแรกยังไม่ลด",
      [REF_SLIDE, "ATLS 10th ed. — classes of hemorrhage"],
      ["2.2.44", "2.1.56", "B2.4(1)"]),
    q("HON-ANM-MCQ-K02", "Ineffective erythropoiesis — nuclear vs cytoplasmic defect",
      "Which pairing correctly matches the type of ineffective erythropoiesis with its red cell size and an example?",
      ["Nuclear maturation defect — microcytic, hypochromic cells — β-thalassemia",
       "Cytoplasmic maturation defect — macrocytic cells — methotrexate therapy",
       "Nuclear maturation defect — macrocytic cells — myelodysplastic syndrome",
       "Cytoplasmic maturation defect — normocytic cells — anemia of chronic kidney disease",
       "Nuclear maturation defect — normocytic cells — sideroblastic anemia"],
      2,
      "สไลด์แบ่ง ineffective erythropoiesis (เซลล์ตัวอ่อนตายในไขกระดูก) เป็น 2 แบบ\n\n- **Nuclear maturation defect → macrocytosis** — DNA สร้างไม่ทัน นิวเคลียสแบ่งช้าแต่ไซโทพลาสซึมโตต่อ เซลล์จึงใหญ่ · ตัวอย่าง: **folate/B12 deficiency · MTX · alkylating agents · MDS · alcohol** → **MDS ถูก**\n- **Cytoplasmic maturation defect → microcytosis + hypochromia** — Hb (heme หรือ globin) ไม่พอ เซลล์แบ่งเพิ่มอีกรอบจึงเล็ก · ตัวอย่าง: **thalassemia · sideroblastic anemia**\n\nตัวลวง: β-thal เป็น cytoplasmic ไม่ใช่ nuclear · MTX เป็น nuclear (ยับยั้ง DHFR) · CKD เป็น hypoproliferative (EPO ไม่พอ) ไม่ใช่ ineffective · sideroblastic เป็น cytoplasmic และ microcytic",
      "นิวเคลียสช้า → เซลล์ใหญ่ (B12 folate MTX MDS สุรา) · ไซโทพลาสซึมช้า → เซลล์เล็ก (thal sideroblastic)",
      [REF_SLIDE, "Harrison's Principles of Internal Medicine 21st ed. — Anemia and polycythemia"],
      ["2.1.56", "B2.3(2)", "2.3.3(8)"]),
    q("HON-ANM-MCQ-K03", "Anemia in pregnancy — when to investigate further",
      "A 27-year-old woman at 10 weeks of gestation has a routine CBC: Hb 10.6 g/dL, MCV 62 fL, RDW 13.2%, RBC 5.6 × 10⁶/µL, WBC and platelets normal. She feels well. What is the most appropriate interpretation?",
      ["Physiologic hemodilution of pregnancy; no further work-up is needed",
       "Typical iron deficiency of pregnancy; start oral iron and recheck only if Hb falls below 9 g/dL",
       "Mild anemia with a very low MCV and a high RBC count; send Hb typing/thalassemia screening (and ferritin) and offer partner screening",
       "Severe anemia; transfuse packed red cells before the second trimester",
       "Macrocytic anemia; check vitamin B12 and folate levels"],
      2,
      "Hb 10.6 ในไตรมาสแรก **< 11 = ซีด** (เกณฑ์ในสไลด์) แต่เป็นระดับเล็กน้อย\n\nสไลด์ระบุให้ **สืบค้นเพิ่ม** เมื่อ **ซีดเล็กน้อยแต่ MCV ต่ำมาก** — ผู้ป่วยรายนี้ MCV 62 ทั้งที่ Hb แค่ 10.6 · **RBC สูง 5.6 ล้าน + RDW ปกติ** เป็นลักษณะของ **thalassemia trait** มากกว่าขาดเหล็ก (ขาดเหล็กระดับนี้ MCV ไม่ควรต่ำขนาดนี้และ RDW มักกว้าง) → ส่ง **Hb typing/DNA สำหรับ α-thal 1 และ ferritin** · ในไทยต้อง **ตรวจคู่สมรส** เพื่อประเมินความเสี่ยง Hb Bart's hydrops / β-thal major ของทารก\n\n- Hemodilution ไม่ทำให้ MCV ต่ำ\n- ให้เหล็กเฉย ๆ จะพลาดการคัดกรอง thalassemia ซึ่งเวลามีจำกัดในการตั้งครรภ์\n- Hb 10.6 ไม่ใช่ severe (severe = 4.0–6.9) และไม่มีข้อบ่งชี้ให้เลือด\n- MCV 62 คือ microcytic ไม่ใช่ macrocytic",
      "ตั้งครรภ์ซีดเล็กน้อยแต่ MCV ต่ำมาก + RBC สูง → คัดกรอง thalassemia ทั้งแม่และคู่สมรส",
      [REF_SLIDE, "WHO 2024 — Guideline on haemoglobin cutoffs to define anaemia"],
      ["2.3.3(8)", "3.3.5", "2.3.3(7)", "2.1.56"]),
  ],
  "figs": {},
  "mnem": [
    {"name": "4 กลไก = 'ไม่สร้าง · สร้างเสีย · แตก · หาย'",
     "what": "pathogenesis ของภาวะซีดตามสไลด์ อ.Kunapa",
     "lines": [["ไม่สร้าง", "**Hypoproliferative** (~75%) — IDA ACD CKD hypothyroid infiltration stem cell"],
               ["สร้างเสีย", "**Ineffective erythropoiesis** — nuclear (ใหญ่) / cytoplasmic (เล็ก)"],
               ["แตก", "**Hemolysis** — congenital (membrane enzyme globin) / acquired"],
               ["หาย", "**Acute blood loss** — ประเมินจากอาการ 4 ระดับ"]],
     "note": "retic ต่ำ = ไม่สร้างหรือสร้างเสีย · retic สูง = แตกหรือหาย",
     "src": "เรียบเรียงจากสไลด์ อ.Kunapa"}
  ],
}

# ---------------------------------------------------------------- K2
K2_MD = r"""### แล็บที่สไลด์ไล่ให้ส่ง (เลือกตามสมมติฐาน)
- **CBC** — red cell parameters · WBC + differential · platelet · **เทียบกับ CBC เก่าเสมอ**
- **Peripheral blood smear** · **reticulocyte count** · **direct Coombs test**
- **Blood chemistry** — bilirubin · LDH · BUN/Cr · LFT
- **Iron profile** — serum iron · TIBC · transferrin saturation · **serum ferritin**
- **Stool occult blood + parasite**
- **Hemoglobin analysis** · **G-6-PD level** (✍️ screening: **methemoglobin reduction test**)
- **Osmotic fragility test** (HS) · **urine hemosiderin · Ham's test** (PNH)
- **Bone marrow study**

### Red cell parameters — ตัวไหนวัดตรง ตัวไหนคำนวณ
| วัดโดยตรง | คำนวณ |
|---|---|
| **RBC** (×10⁶/µL) | **Hct (%) = RBC × MCV ÷ 10** |
| **MCV** (fL) | **MCH (pg) = Hb × 10 ÷ RBC** |
| **Hb** (g/dL) | **MCHC (g/dL) = Hb ÷ Hct × 100** |
| | **RDW (%)** — ความกว้างของการกระจายขนาด |

**ค่าปกติ CBC ในสไลด์**: MCV **80–100 fL** · MCH **> 27 pg** · MCHC **32–36 g/dL** · RDW **11.5–14.5%** · WBC 3.8–10.6 (ชาย) / 3.6–11.0 (หญิง) ×10⁹/L · platelet **150–440 ×10⁹/L**
- (เสริม) เครื่องนับวัด MCV ตรงแล้วคำนวณ Hct — ภาวะที่รบกวน MCV (cold agglutinin เซลล์จับกลุ่ม) จึงทำ Hct และ **MCHC ผิดไปด้วย** · **MCHC > 36** ให้นึกถึง **spherocyte** (HS, AIHA) หรือค่าเทียมจาก agglutination/lipemia

### Reticulocyte — 3 วิธีอ่านในสไลด์
**1. Corrected retic และ RPI**
- **Corrected retic = % retic × Hct ผู้ป่วย ÷ 45**
- **RPI = corrected retic ÷ 2** (สไลด์ใช้ตัวหาร 2 แบบง่าย)
- **RPI < 2 → hypoproliferative หรือ ineffective erythropoiesis** · **RPI ≥ 2 → hemolysis หรือ acute blood loss**

**2. Absolute reticulocyte count = % retic × RBC**
| Absolute retic (/µL) | ความหมาย |
|---|---|
| 25,000–75,000 | ช่วงปกติ |
| **> 100,000** | **regenerative** (ไขกระดูกตอบสนอง) |
| **< 50,000** | **hypoproliferative** |
| 50,000–100,000 | สาเหตุผสม |

**3. Reticulocyte index (RI) = corrected retic ÷ maturation time**
| Hct ผู้ป่วย | maturation time (วัน) |
|---|---|
| **≥ 40%** | 1 |
| **30–40%** | 1.5 |
| **20–30%** | 2 |
| **< 20%** | 2.5 |
- RI คนปกติ **1–2%** · **RI < 1% ร่วมกับซีด = สร้างลดลง** · **RI > 2% ร่วมกับซีด = เสีย RBC** (แตกหรือเลือดออก)

> **Kunapa · ตัวเลขต่างจากหัวข้อ Approach** — สไลด์แบ่ง maturation time ที่ Hct **40 / 30 / 20** (หัวข้อด้านบนใช้ 36–45 / 26–35 / 16–25) และสอนสูตร RPI แบบหาร 2 ตรง ๆ ด้วย — หลักเดียวกันคือ **Hct ยิ่งต่ำ retic ยิ่งถูกปล่อยออกเร็วและอยู่ในเลือดนาน ต้องหารมากขึ้น** · สอบในคาบให้ใช้ตารางของสไลด์

**ตัวอย่างคำนวณ** — Hct 24% · retic 6% · RBC 2.7 ×10⁶/µL
- Corrected = 6 × 24/45 = **3.2%** · RI = 3.2 ÷ 2 (Hct 20–30) = **1.6**
- Absolute = 0.06 × 2,700,000 = **162,000/µL** → regenerative
- (เสริม) เกณฑ์แต่ละแบบอาจให้คำตอบก้ำกึ่งไม่ตรงกัน — ใช้ร่วมกับบริบท: เหลือง LDH haptoglobin หรือแหล่งเสียเลือด

### Smear — รูปร่างเซลล์และโรคที่ต้องนึกถึง (ตามสไลด์)
| รูปร่าง | นึกถึง |
|---|---|
| **Autoagglutination** | AIHA (cold) |
| **Spherocyte** | **AIHA · HS** · thalassemia · hemolytic transfusion reaction · MAHA · hypersplenism · หลังให้เลือด · **clostridial sepsis** · **severe hypophosphatemia** · G-6-PD deficiency ขณะ hemolytic crisis |
| **Schistocyte** | **MAHA** — TTP/HUS · DIC · traumatic hemolysis · malignant hypertension · vasculitis · GN · preeclampsia · **macrovascular**: prosthetic valve · chordae ขาด · **severe burn · march hemoglobinuria** |
| **Target cell** | **thalassemia** · obstructive liver disease · IDA · sideroblastic · หลังตัดม้าม · hemoglobinopathy (HbE) |
| **Spur cell (acanthocyte)** | **ตับวายรุนแรง (spur cell anemia)** · abetalipoproteinemia · หลังตัดม้าม · hypothyroidism · malabsorption |
| **Burr cell (echinocyte)** | **uremia** · pyruvate kinase deficiency · RBC ที่ K ต่ำ |
| **Teardrop** | **myelofibrosis · myelophthisis** · thalassemia · megaloblastic |
| **Basophilic stippling** | **lead poisoning** · megaloblastic · MDS · thalassemia · sideroblastic · unstable Hb |
| **Stomatocyte** | hereditary stomatocytosis · โรคตับ (โดยเฉพาะ **สุราเฉียบพลัน**) |
| **Howell-Jolly body** | **หลังตัดม้าม · ม้ามทำงานลดลง** |
| **Rouleaux** | multiple myeloma (✍️ ข้างภาพ plasma cell — นิวเคลียสเยื้องข้าง → multiple myeloma) |

ภาพ smear ในสไลด์ (ดูภาพจริงในบท **อ่าน Peripheral Blood Smear**): autoagglutination · β-thal/HbE disease · IDA · megaloblastic + **hypersegmented neutrophil** (✍️ **> 5 lobes หรือ 5 lobes > 5%**) · APL hypergranular/microgranular variant + **faggot cell** · hand-mirror lymphoblast · **hairy cell leukemia** · splenic marginal zone lymphoma with villous lymphocyte · **plasma cell leukemia** · CLL · myelophthisis (✍️ leukoerythroblastic — มะเร็งแทรกไขกระดูก หรือ infection) · G-6-PD deficiency with acute hemolysis
"""

K2 = {
  "id": "hon-anm-k2",
  "title": "สไลด์ อ.Kunapa ② — แล็บ red cell indices reticulocyte 3 แบบ และ smear",
  "minutes": 14,
  "summary": "Hct = RBC × MCV/10 · MCH = Hb × 10/RBC · MCHC = Hb/Hct × 100 · corrected retic = %retic × Hct/45 · RPI = corrected/2 (< 2 hypo/ineffective · ≥ 2 แตก/เสีย) · absolute retic > 100,000 regenerative · < 50,000 hypo · RI maturation Hct ≥ 40/30–40/20–30/< 20 = 1/1.5/2/2.5 · smear 11 รูปร่าง",
  "source": SRC,
  "nl": ["3.3.1", "3.1.2", "3.3.3", "B2.3(2)", "B2.3(3)", "2.1.56", "3.3.27"],
  "md": K2_MD,
  "pearls": [
    "Hct = RBC × MCV ÷ 10 · MCH = Hb × 10 ÷ RBC · MCHC = Hb ÷ Hct × 100",
    "RPI = (%retic × Hct/45) ÷ 2 · < 2 = hypoproliferative/ineffective · ≥ 2 = hemolysis/blood loss",
    "Absolute retic > 100,000/µL = regenerative · < 50,000 = hypoproliferative · 50,000–100,000 = ผสม",
    "Maturation time ตามสไลด์: Hct ≥ 40 → 1 · 30–40 → 1.5 · 20–30 → 2 · < 20 → 2.5",
    "Spherocyte เจอได้ใน clostridial sepsis และ severe hypophosphatemia ด้วย · burr cell = uremia/PK def · spur cell = ตับวายรุนแรง",
    "Hypersegmented neutrophil = มี 6 lobes ขึ้นไป หรือ 5 lobes > 5%",
  ],
  "items": [
    q("HON-ANM-MCQ-K04", "Reticulocyte production index",
      "A 30-year-old woman has Hb 8.0 g/dL, Hct 24%, MCV 88 fL and a reticulocyte count of 7.5%. Using the simplified method taught in the lecture (corrected reticulocyte count = % reticulocytes × patient Hct ÷ 45; RPI = corrected count ÷ 2), what is the RPI and its interpretation?",
      ["RPI about 7.5 — hypoproliferative anemia",
       "RPI about 4.0 — the marrow response is adequate; consider hemolysis or acute blood loss",
       "RPI about 1.0 — ineffective erythropoiesis",
       "RPI about 2.0 — hemolysis or acute blood loss",
       "RPI about 14.1 — regenerative anemia"],
      3,
      "คำนวณตามสไลด์\n- **Corrected retic = 7.5 × 24/45 = 4.0%**\n- **RPI = 4.0 ÷ 2 = 2.0**\n- เกณฑ์: **RPI ≥ 2 → hemolysis หรือ acute blood loss** · RPI < 2 → hypoproliferative หรือ ineffective erythropoiesis\n\nตัวลวง:\n- 4.0 คือ corrected retic ยังไม่ได้หาร maturation time\n- 7.5 คือ % retic ดิบที่ยังไม่แก้ และค่าสูงไม่ได้แปลว่า hypoproliferative\n- 1.0 มาจากการหารซ้ำสองรอบ\n- 14.1 คือคูณกลับด้าน (7.5 × 45/24) — การแก้ต้อง **ลด** ค่าลงเมื่อ Hct ต่ำ\n\n(เสริม) ค่าที่ชนเกณฑ์พอดีต้องใช้บริบทช่วย — ดู bilirubin LDH haptoglobin smear และหาแหล่งเสียเลือด",
      "RPI = %retic × Hct/45 ÷ 2 · ≥ 2 = แตก/เสีย · < 2 = ผลิตไม่พอ",
      [REF_SLIDE],
      ["3.3.1", "2.1.56", "B2.3(2)"]),
    q("HON-ANM-MCQ-K05", "Red cell indices — calculation",
      "A CBC reports RBC 4.0 × 10⁶/µL, MCV 75 fL and Hb 9.0 g/dL. Which set of calculated indices is correct?",
      ["Hct 30%, MCH 22.5 pg, MCHC 30 g/dL",
       "Hct 18.8%, MCH 44 pg, MCHC 48 g/dL",
       "Hct 30%, MCH 36 pg, MCHC 30 g/dL",
       "Hct 3.0%, MCH 2.25 pg, MCHC 300 g/dL",
       "Hct 33%, MCH 22.5 pg, MCHC 27 g/dL"],
      0,
      "สูตรในสไลด์ (RBC MCV Hb วัดตรง ที่เหลือคำนวณ)\n- **Hct = RBC × MCV ÷ 10 = 4.0 × 75 ÷ 10 = 30%**\n- **MCH = Hb × 10 ÷ RBC = 9 × 10 ÷ 4.0 = 22.5 pg** (ปกติ > 27 → hypochromic)\n- **MCHC = Hb ÷ Hct × 100 = 9 ÷ 30 × 100 = 30 g/dL** (ปกติ 32–36 → hypochromic)\n\nภาพรวม = **microcytic hypochromic** → นึกถึง IDA / thalassemia ก่อน\n\nตัวลวงเกิดจากหารผิดตัวหรือผิดหลักทศนิยม · MCHC > 36 ในชีวิตจริงต้องคิดถึง spherocyte หรือค่าเทียม",
      "Hct = RBC × MCV/10 · MCH = Hb × 10/RBC · MCHC = Hb/Hct × 100",
      [REF_SLIDE, "Williams Hematology — red cell indices"],
      ["3.3.1", "2.1.56"]),
    q("HON-ANM-MCQ-K06", "Smear morphology — matching",
      "Which red cell morphology–condition pairing is correct?",
      ["Burr cells (echinocytes) — postsplenectomy state",
       "Howell-Jolly bodies — uremia",
       "Spur cells (acanthocytes) — severe acute hepatic necrosis",
       "Teardrop cells — hereditary spherocytosis",
       "Autoagglutination — lead poisoning"],
      2,
      "จากตาราง smear ในสไลด์\n- **Spur cell (acanthocyte)** — **acute hepatic necrosis (spur cell anemia)** · abetalipoproteinemia · หลังตัดม้าม · hypothyroidism · malabsorption → **ถูก**\n- Burr cell (echinocyte) = **uremia** · PK deficiency · RBC ที่ K ต่ำ (ไม่ใช่หลังตัดม้าม)\n- Howell-Jolly body = **หลังตัดม้าม/ม้ามทำงานลดลง** (ไม่ใช่ uremia) — ตัวลวงสองข้อแรกสลับคู่กัน\n- Teardrop = **myelofibrosis/myelophthisis** · thal · megaloblastic\n- Autoagglutination = **AIHA (cold agglutinin)** · lead poisoning ให้ **basophilic stippling**",
      "Burr = uremia · Spur = ตับวาย · Howell-Jolly = ไม่มีม้าม · Teardrop = ไขกระดูกถูกแทรก · Stippling = ตะกั่ว",
      [REF_SLIDE, "Atlas of Blood Smears in Common Hematologic Diseases (อ.Chaicharoen Tantanate, v.01.2025)"],
      ["3.1.2", "3.3.27", "2.1.56"]),
  ],
  "figs": {},
  "mnem": [
    {"name": "Retic: 45 · 2 · 100,000",
     "what": "ตัวเลขสามตัวที่ต้องจำเวลาแปลผล reticulocyte",
     "lines": [["45", "Hct ปกติที่ใช้แก้: corrected = %retic × Hct/**45**"],
               ["2", "หารด้วย **2** ได้ RPI · และเกณฑ์ตัดคือ **2** เหมือนกัน (< 2 ผลิตไม่พอ · ≥ 2 แตก/เสีย)"],
               ["100,000", "absolute retic > **100,000**/µL = regenerative · < 50,000 = hypoproliferative"]],
     "note": "สไลด์ใช้ RPI = corrected ÷ 2 แบบง่าย · ถ้าจะละเอียดใช้ maturation time ตาม Hct",
     "src": "เรียบเรียงจากสไลด์ อ.Kunapa"}
  ],
}

# ---------------------------------------------------------------- K3
K3_MD = r"""### Case 1 ในสไลด์ — ชาย 33 ปี เพลีย ซีด จ้ำเลือด 4 สัปดาห์
- **PE**: ซีดมาก · **ไม่เหลือง** · petechiae ที่ขาทั้งสองข้างและผนังอก · (ไม่มีตับม้ามโต ต่อมน้ำเหลืองโต)
- **CBC**: Hb **5 g/dL** · Hct 16% · MCV **100 fL** · WBC **1.2 ×10⁹/L** (PMN 10% · L 85% · M 5%) · platelet **10 ×10⁹/L**
- คำถาม: most likely diagnosis — A. aplastic anemia · B. megaloblastic anemia · C. acute leukemia · D. MDS · E. CLL

**ไล่คิด** (✍️ "pancytopenia + subacute · lymphocyte predominate (relative)")
1. **Pancytopenia** + onset **subacute** (4 สัปดาห์) → กลุ่ม **stem cell disease**
2. ANC = 1.2 × 0.10 = **0.12 ×10⁹/L** · lymphocyte 85% แต่ absolute ≈ 1.0 = **relative lymphocytosis** (สายอื่นหายไป ไม่ใช่ lymphocyte เพิ่ม)
3. **ไม่มีตับม้ามโต ไม่เหลือง** → ไม่เข้ากับ hemolysis หรือ infiltration
4. → **A. Aplastic anemia** (ต้องยืนยันด้วย bone marrow)

ตัวลวงในเคส
- **Megaloblastic** — pancytopenia ได้ แต่มัก MCV > 100 ชัด มี hypersegmented neutrophil เหลืองเล็กน้อย LDH สูงมาก และไม่ได้มี lymphocyte เด่น
- **Acute leukemia** — subacute เหมือนกัน แต่มักเห็น **blast** ใน smear และอาจมีตับม้าม/ต่อมโต ปวดกระดูก
- **MDS** — พบในผู้สูงอายุมากกว่า มี dysplasia (pseudo-Pelger, ringed sideroblast) ต้องตรวจโครโมโซม
- **CLL** — absolute lymphocytosis (> 5 ×10⁹/L) ผู้สูงอายุ ต่อมน้ำเหลืองโต · ที่นี่ WBC รวมแค่ 1.2

### Aplastic anemia — สาเหตุ
| Inherited | Acquired |
|---|---|
| **Fanconi anemia** | **Idiopathic** (ส่วนใหญ่ — autoimmune T cell) |
| **Dyskeratosis congenita** | **ยาและสารพิษ** — alcohol · **chloramphenicol** · **benzene** · ticlopidine · penicillamine · gold salt · sulfonamides · diuretics |
| **Shwachman-Diamond syndrome** | **ติดเชื้อ** — EBV · **non-A non-B non-C hepatitis** · HIV · CMV |
| | **SLE · RA** |
| | **ตั้งครรภ์** |
- ✍️ จำกลุ่ม acquired: **chemical · infection · autoimmune · idiopathic** (+ ตั้งครรภ์)

### อาการและการดำเนินโรค
- **ซีด** · **เลือดออก** จากเกล็ดเลือดต่ำ · **ไข้/ติดเชื้อ** จากเม็ดเลือดขาวต่ำ
- **ไม่มี organomegaly** — ถ้าตับม้ามต่อมโตต้องคิดโรคอื่น
- **~20% ของ severe AA มี PNH clone**
- ดำเนินโรคต่อเป็น **PNH · MDS · AML** ได้

### Laboratory investigation
- **Pancytopenia with relative lymphocytosis**
- **Hypocellular bone marrow** (ไขกระดูกถูกแทนด้วยไขมัน)
- **Chromosome study ปกติ** — เพื่อตัด **hypoplastic MDS**
- คัดกรอง PNH — **urine hemosiderin · Ham's test · flow cytometry CD55/CD59**
- เด็ก/ผู้ใหญ่ตอนต้น: ตัด **Fanconi anemia** — เลี้ยง lymphocyte หรือ fibroblast กับ **DEB (diepoxybutane) หรือ mitomycin C** → **โครโมโซมแตกมากผิดปกติ**

### ความรุนแรง (Camitta criteria — เสริม เพราะในสไลด์เป็นภาพตาราง)
| ระดับ | เกณฑ์ |
|---|---|
| **Severe AA** | BM cellularity **< 25%** (หรือ 25–50% แต่เซลล์สร้างเลือดเหลือ < 30%) **+ อย่างน้อย 2 ใน 3**: ANC **< 0.5 ×10⁹/L** · platelet **< 20 ×10⁹/L** · retic **< 20 ×10⁹/L** (เครื่องอัตโนมัติ < 60) |
| **Very severe AA** | เข้า severe **+ ANC < 0.2 ×10⁹/L** |
| **Non-severe AA** | ไม่ถึงเกณฑ์ severe |
- เคสในสไลด์: ANC 0.12 + platelet 10 → ถ้าไขกระดูก hypocellular = **very severe AA**
- ✍️ ข้างตาราง: **G-CSF** ใช้ช่วยกรณี WBC ต่ำ — ผลข้างเคียงคือ **ปวดกระดูก ปวดกล้ามเนื้อ**

### การรักษา (เสริม — ไม่อยู่ในสไลด์)
- **อายุน้อย + มีพี่น้อง HLA ตรง → allogeneic HSCT**
- ไม่มี donor/อายุมาก → **immunosuppression: horse ATG + cyclosporine + eltrombopag**
- Supportive: ให้เลือดแบบ **leukoreduced** (ลดการกระตุ้นภูมิก่อนปลูกถ่าย) · ยาปฏิชีวนะเร็วเมื่อมีไข้ · หลีกเลี่ยงยาที่เป็นเหตุ
"""

K3 = {
  "id": "hon-anm-k3",
  "title": "สไลด์ อ.Kunapa ③ — Case 1: pancytopenia ชาย 33 ปี → aplastic anemia",
  "minutes": 12,
  "summary": "Pancytopenia + subacute + relative lymphocytosis + ไม่มีตับม้ามโต = aplastic anemia · inherited (Fanconi DKC Shwachman-Diamond) vs acquired (idiopathic ยา chloramphenicol benzene ติดเชื้อ hepatitis EBV HIV SLE ตั้งครรภ์) · BM hypocellular · chromosome ปกติ (ตัด MDS) · CD55/CD59 (ตัด PNH) · DEB/mitomycin C (Fanconi) · severe/very severe",
  "source": SRC,
  "nl": ["2.3.3-3(1)", "B2.2.2-3(1)", "B2.1.1(1)", "2.1.56", "3.3.1", "B2.4(1)", "B2.4(4)"],
  "md": K3_MD,
  "pearls": [
    "Pancytopenia + subacute + relative lymphocytosis + ไม่มีตับม้ามโต → aplastic anemia",
    "AA ต้องไม่มี organomegaly · ~20% ของ severe AA มี PNH clone · ดำเนินเป็น PNH MDS AML ได้",
    "Work-up AA: BM hypocellular · chromosome ปกติ (ตัด hypoplastic MDS) · CD55/CD59 (ตัด PNH) · DEB/mitomycin C ในคนอายุน้อย (Fanconi)",
    "ยาที่ทำ AA: chloramphenicol · benzene · ticlopidine · penicillamine · gold · sulfonamides · diuretics",
    "Very severe AA = ANC < 0.2 ×10⁹/L",
  ],
  "items": [
    q("HON-ANM-MCQ-K07", "Pancytopenia — aplastic anemia (slide case 1)",
      "A 33-year-old man has had fatigue and easy bruising for 4 weeks. He is markedly pale with petechiae on both legs and the chest wall; there is no jaundice, lymphadenopathy or hepatosplenomegaly. Hb 5 g/dL, Hct 16%, MCV 100 fL, WBC 1.2 × 10⁹/L (neutrophils 10%, lymphocytes 85%, monocytes 5%), platelets 10 × 10⁹/L. No blasts are seen on the smear. What is the most likely diagnosis?",
      ["Megaloblastic anemia", "Acute leukemia", "Chronic lymphocytic leukemia", "Aplastic anemia", "Myelodysplastic syndrome"],
      3,
      "เคสนี้คือ **Case 1 ในสไลด์ อ.Kunapa**\n\n- **Pancytopenia + onset subacute (4 สัปดาห์)** → กลุ่ม stem cell disease\n- Lymphocyte 85% ของ WBC 1.2 = absolute ~1.0 → **relative lymphocytosis** เพราะ neutrophil หายไป (ANC 0.12)\n- **ไม่มีตับม้ามโต ต่อมน้ำเหลืองโต ไม่เหลือง** และไม่มี blast → **aplastic anemia** (ยืนยันด้วย BM hypocellular)\n\nตัวลวง\n- Megaloblastic: pancytopenia ได้ แต่ MCV มัก > 110 มี hypersegmented neutrophil เหลืองเล็กน้อย LDH สูง\n- Acute leukemia: มักเห็น blast และมี organomegaly/ปวดกระดูกได้\n- CLL: absolute lymphocytosis สูง ผู้สูงอายุ ต่อมโต\n- MDS: ผู้สูงอายุ มี dysplasia — hypoplastic MDS แยกด้วย chromosome study\n\n(เสริม) ANC 0.12 + platelet 10 → ถ้า BM ยืนยัน = **very severe AA** → รีบส่งต่อเพื่อ HSCT/ATG",
      "Pancytopenia + relative lymphocytosis + ไม่มี organomegaly = aplastic anemia",
      [REF_SLIDE, "BSH Guideline for the diagnosis and management of adult aplastic anaemia (2024)"],
      ["2.3.3-3(1)", "B2.2.2-3(1)", "2.1.56"]),
    q("HON-ANM-MCQ-K08", "Aplastic anemia — what the work-up is excluding",
      "In a young adult with pancytopenia and a hypocellular bone marrow, flow cytometry for CD55/CD59 on red cells and granulocytes is sent. What is the main purpose of this test?",
      ["To exclude hypoplastic myelodysplastic syndrome",
       "To detect a paroxysmal nocturnal hemoglobinuria (PNH) clone",
       "To diagnose Fanconi anemia",
       "To confirm autoimmune hemolytic anemia",
       "To identify hairy cell leukemia"],
      1,
      "สไลด์ให้ work-up aplastic anemia เพื่อ **ตัดโรคที่เลียนแบบหรือเกิดร่วม**\n- **CD55/CD59 flow cytometry** (+ urine hemosiderin, Ham's test) → หา **PNH clone** — พบใน **~20% ของ severe AA** และ AA ดำเนินเป็น PNH ได้ (ทั้งสองโรคเกิดจาก stem cell ที่ถูกทำลาย; clone ที่ขาด GPI-anchor รอดจาก T cell)\n- **Chromosome study ปกติ** → ใช้ตัด **hypoplastic MDS**\n- **DEB/mitomycin C chromosome breakage** → ใช้หา **Fanconi anemia** ในเด็ก/ผู้ใหญ่ตอนต้น\n- AIHA ใช้ **DAT** · hairy cell leukemia ใช้ CD11c/CD25/CD103/annexin A1 (และมักม้ามโต)",
      "CD55/CD59 = หา PNH clone · chromosome ปกติ = ตัด MDS · DEB/MMC = Fanconi",
      [REF_SLIDE, "BSH Guideline for the diagnosis and management of adult aplastic anaemia (2024)"],
      ["2.3.3-3(1)", "2.3.3-3(6)", "B2.2.2-3(1)"]),
    q("HON-ANM-MCQ-K09", "Aplastic anemia — drug causes",
      "Which drug or chemical listed in the lecture is a classic cause of acquired aplastic anemia?",
      ["Chloramphenicol", "Amoxicillin", "Ferrous sulfate", "Omeprazole", "Allopurinol"],
      0,
      "สาเหตุ acquired AA จากยาและสารพิษในสไลด์: **alcohol · chloramphenicol · benzene · ticlopidine · penicillamine · gold salt · sulfonamides · diuretics**\n\n- **Chloramphenicol** มีพิษต่อไขกระดูก 2 แบบ — (1) กดไขกระดูกตามขนาดยา หายได้เมื่อหยุด (2) **aplastic anemia แบบ idiosyncratic** ไม่ขึ้นกับขนาด เกิดหลังหยุดยาหลายสัปดาห์ถึงเดือนและมักไม่หาย\n- ยาอื่นในตัวเลือกไม่ได้เป็นสาเหตุคลาสสิกของ AA (allopurinol เด่นเรื่อง SJS/TEN/DRESS)",
      "ยาทำ AA: chloramphenicol · benzene · ticlopidine · penicillamine · gold · sulfonamide · diuretics",
      [REF_SLIDE],
      ["2.3.3-3(1)", "B2.2.2-3(1)"]),
  ],
  "figs": {},
}

# ---------------------------------------------------------------- K4
K4_MD = r"""### Case 2 — หญิง 18 ปี ประจำเดือนมามาก 7 เดือน
- PE ปกติ ยกเว้น **conjunctiva ซีดปานกลาง** · ไม่มีโรคประจำตัว
- **CBC**: Hb **5 g/dL** · Hct 16% · MCV **60 fL** · RDW **21%** · WBC 5.5 ×10⁹/L (PMN 80% L 20%) · platelet **800 ×10⁹/L**
- คำถาม: most appropriate action — A. iron supplement · B. packed red cell transfusion · C. Hb electrophoresis · D. bone marrow · E. abdominal ultrasound

**อ่าน CBC**: microcytic + **RDW กว้าง** + **reactive thrombocytosis** + ประวัติเสียเลือดเรื้อรัง → **iron deficiency anemia**

**เลือกการรักษา** — ใช้เกณฑ์ให้เลือดในสไลด์: **RBC transfusion เมื่อ (1) CVS ไม่คงที่ (2) มีอาการจากซีด หรือ (3) ยังเสียเลือดต่อเนื่องและมาก** · ถ้าไม่เข้าเกณฑ์ → **ให้เหล็ก**
- ✍️ โน้ตในสไลด์ทำเครื่องหมายไว้ที่ทั้ง **A** และ **B** — ข้อนี้ตัดสินจากสถานะคนไข้: ประวัติยัง **มีประจำเดือนมามากต่อเนื่อง** และ Hb 5 → เอียงไปทาง **B (ให้ PRC)** ตามเกณฑ์ข้อ 3 · ถ้าโจทย์บอกว่าคงที่ ไม่มีอาการ เลือดหยุดแล้ว → **A (ให้เหล็ก)** — อ่านโจทย์ให้ดีว่าให้ข้อมูลอะไร แล้วถามอาจารย์ยืนยันเฉลย
- **Hb electrophoresis ตอนนี้ไม่ได้** — ขาดเหล็กทำ **HbA2 ต่ำลง** ซ่อน β-thal trait → ตรวจหลังเติมเหล็ก
- ไม่ต้องเจาะไขกระดูก · US ช่องท้องไม่ได้ตอบปัญหาเร่งด่วน (หาสาเหตุ menorrhagia ทาง gyne ทีหลัง)

### Iron deficiency anemia — สาเหตุ 3 กลุ่ม
| ความต้องการเพิ่ม | เสียเหล็กเพิ่ม | ได้รับ/ดูดซึมลดลง |
|---|---|---|
| วัยทารก · **วัยรุ่น** · **ตั้งครรภ์** | เสียเลือดเฉียบพลัน/เรื้อรัง · **บริจาคเลือด** · **ประจำเดือน** | อาหารไม่พอ · **malabsorption** · **หลังตัดกระเพาะ** · การอักเสบเฉียบพลัน/เรื้อรัง |
- ✍️ **Crohn disease → duodenum/jejunum** ดูดซึมเหล็กไม่ได้

### Investigations
- **CBC**: Hct ↓ Hb ↓ · **MCV ↓ (เมื่อ Hb < 10 g/dL)** · MCH ↓ · MCHC ↓ · **RDW ↑ = early sign**
- **Reticulocyte ↓**
- **Iron profile**: serum iron ↓ · **TIBC ↑** · **ferritin ↓** · **Tsat = serum iron ÷ TIBC × 100**
- **Bone marrow iron stain = gold standard** (แต่ invasive) — IDA ไม่มีเหล็กย้อมติด

### สามระยะของการพร่องเหล็ก (ตารางในสไลด์)
| | ปกติ | Negative iron balance | Iron-deficient erythropoiesis | **IDA** |
|---|---|---|---|---|
| BM iron stores | 1–3+ | 0–1+ | 0 | 0 |
| Serum ferritin (µg/L) | 50–200 | **< 20** | < 15 | < 15 |
| Serum iron (µg/dL) | 50–150 | ปกติ | **< 50** | < 30 |
| TIBC (µg/dL) | 300–360 | > 360 | > 380 | > 400 |
| Iron saturation (%) | 30–50 | ปกติ | **< 20** | < 16 |
| RBC morphology | ปกติ | ปกติ | ปกติ | **hypochromic microcytic** |
- **Ferritin ลดก่อนเพื่อน** (คลังหมด) → serum iron/Tsat ตก (การสร้างเริ่มขาด) → สุดท้าย **เซลล์เล็กซีด**
- (เสริม) หน่วยของ serum iron/TIBC ในสไลด์พิมพ์เป็น µg/L — ค่ามาตรฐานใช้ **µg/dL**

### Treatment
- **ให้ RBC** เมื่อ CVS ไม่คงที่ · มีอาการจากซีด · หรือยังเสียเลือดต่อเนื่องมาก
- **ให้เหล็ก**: **oral elemental iron 50–100 mg วันละ 1–3 ครั้ง** · **IV iron ~1,000 mg/course**
- **รักษาต้นเหตุ** · **ผู้สูงอายุต้องคัดกรองมะเร็งทางเดินอาหาร**
- (เสริม) BSH 2021: เหล็กกิน **วันละครั้งหรือวันเว้นวัน** ดูดซึมดีกว่าแบ่งหลายมื้อ (hepcidin ขึ้นหลังกินแต่ละครั้ง) · Hb ควรขึ้น ~2 g/dL ใน 3–4 สัปดาห์ · ให้ต่อ **3 เดือนหลัง Hb ปกติ** เพื่อเติมคลัง

### Case 3 — หญิง 80 ปี เพลีย อ่อนแรง เคยผ่าตัดกระเพาะ
- U/D: DM type 2 · dyslipidemia · CAD · **SH: เคยตัดกระเพาะ (gastrectomy)**
- PE: ซีดปานกลาง · ไม่เหลือง · ไม่มีต่อมน้ำเหลืองโต · ไม่มีตับม้ามโต
- **CBC**: Hb **7 g/dL** · Hct 22% · MCV **120 fL** · WBC **2,500/µL** · platelet **100,000/µL** → ✍️ **pancytopenia with macrocytic**
- ตัวเลือก: AIHA · IDA · ACD · **megaloblastic anemia** · multiple myeloma → ตอบ **D. Megaloblastic anemia** (B12 deficiency จากไม่มี intrinsic factor หลังตัดกระเพาะ)
- (เสริม) metformin ใช้นานก็ลดการดูดซึม B12 — ผู้ป่วยเบาหวานรายนี้มีสองปัจจัย

### Megaloblastic anemia
- ขาด **B12 หรือ folate** → สร้าง **DNA** บกพร่อง (B12 เกี่ยวกับ RNA ด้วยในสไลด์)
- ดูดซึม: **B12 ที่ terminal ileum** · **folate ที่ jejunum**
- ความต้องการต่อวัน — (เสริม) ในไฟล์สไลด์ตัวเลขดูสลับกัน (B12 50 · folate 2.5 µg/วัน) · ค่าตามตำรา: **B12 ~2–3 µg/วัน** (คลังในตับพอ **3–5 ปี**) · **folate ~100–400 µg/วัน** (คลังพอ **3–4 เดือน**) → ขาด folate เกิดเร็วกว่ามาก

| สาเหตุ B12 deficiency | สาเหตุ folate deficiency |
|---|---|
| **มังสวิรัติเคร่ง (vegan)** | กินไม่พอ |
| **Pernicious anemia** (antibody ต่อ parietal cell / intrinsic factor) | เสียเพิ่ม — **dialysis** |
| **ตัดกระเพาะทั้งหมด/บางส่วน** | ยา — **methotrexate · ยากันชัก** |
| Malabsorption (โรคของ terminal ileum) | **สุรา** |
| ยา — 6-MP · Ara-C · hydroxyurea | Malabsorption |
| | **ความต้องการเพิ่ม** — ตั้งครรภ์ · hemolytic anemia |
- (เสริม) 6-MP · Ara-C · hydroxyurea ทำ megaloblastosis โดย **ยับยั้งการสร้าง DNA ตรง ๆ** ไม่ได้ทำให้ B12 ต่ำ — วัดระดับ B12 จะปกติ

**อาการ**: ซีด · **เหลือง** (ineffective erythropoiesis — เซลล์ตายในไขกระดูก) · **glossitis (beefy tongue)** · **ระบบประสาท (เฉพาะ B12)**: peripheral neuropathy · **เสีย position + vibration** · dementia

**Lab**
- CBC + smear: **macro-ovalocyte · basophilic stippling · NRC · hypersegmented neutrophil**
- **Indirect bilirubin ↑ · LDH ↑**
- **Serum B12 · serum หรือ red cell folate**
- **Antibody ต่อ gastric parietal cell และ intrinsic factor** (pernicious anemia)

**Treatment**
- **Vitamin B12 1,000 µg ฉีดทุกวัน 1–2 สัปดาห์ → ทุกสัปดาห์ 1 เดือน → ทุกเดือนตลอดชีวิต**
- Oral B12 (ขนาดสูงใช้ได้แม้ไม่มี IF — ดูดซึมแบบ passive ~1%)
- **Oral folate 1–5 mg/วัน**
- (เสริม) **ห้ามให้ folate เดี่ยวก่อนตัด B12** — เลือดดีขึ้นแต่ประสาทแย่ลง · ช่วงแรกของการรักษาเฝ้าระวัง **K ต่ำ** (เซลล์ใหม่ดึง K เข้า)
"""

K4 = {
  "id": "hon-anm-k4",
  "title": "สไลด์ อ.Kunapa ④ — Case 2 IDA จากประจำเดือนมามาก · Case 3 megaloblastic หลังตัดกระเพาะ",
  "minutes": 15,
  "summary": "IDA: microcytic + RDW กว้าง + reactive thrombocytosis · สามระยะ ferritin < 20 → iron/Tsat ตก → hypochromic microcytic · ให้เลือดเมื่อ CVS ไม่คงที่/มีอาการ/ยังเสียเลือดมาก · elemental iron 50–100 mg 1–3 ครั้ง/วัน · IV 1,000 mg · ผู้สูงอายุคัดกรองมะเร็ง GI · Megaloblastic: pancytopenia + MCV > 100 หลัง gastrectomy · B12 1,000 µg ทุกวัน → ทุกสัปดาห์ → ทุกเดือนตลอดชีวิต · folate 1–5 mg/วัน",
  "source": SRC,
  "nl": ["2.3.3(7)", "B2.2.5(1)", "3.3.26", "B2.4(2)", "B2.4(1)", "2.3.6-3(9)", "B1.1.5(2)", "2.1.56"],
  "md": K4_MD,
  "pearls": [
    "IDA: RDW ↑ เป็น early sign · MCV ลดเมื่อ Hb < 10 · ferritin ลดก่อน · BM iron stain = gold standard",
    "ให้ RBC ใน IDA เมื่อ CVS ไม่คงที่ · มีอาการจากซีด · ยังเสียเลือดต่อเนื่องมาก — นอกนั้นให้เหล็ก",
    "เหล็กกิน elemental 50–100 mg วันละ 1–3 ครั้ง · IV ~1,000 mg/course · ผู้สูงอายุคัดกรองมะเร็ง GI",
    "ห้ามส่ง Hb typing ขณะขาดเหล็ก — HbA2 ต่ำลง ซ่อน β-thal trait",
    "Pancytopenia + MCV 120 + เคยตัดกระเพาะ = megaloblastic (B12) · B12 1,000 µg ทุกวัน → สัปดาห์ → เดือน ตลอดชีวิต",
    "B12 ดูดซึมที่ terminal ileum · folate ที่ jejunum · อาการประสาทเฉพาะ B12",
  ],
  "items": [
    q("HON-ANM-MCQ-K10", "Iron deficiency anemia — indication for transfusion",
      "An 18-year-old woman has had heavy menstrual bleeding for 7 months and is currently menstruating heavily. She has palpitations and dyspnea when climbing one flight of stairs. HR 112/min, BP 108/70 mmHg. Hb 5 g/dL, MCV 60 fL, RDW 21%, platelets 800 × 10⁹/L. What is the most appropriate immediate management?",
      ["Oral ferrous sulfate and review in 4 weeks",
       "Hemoglobin electrophoresis before any treatment",
       "Bone marrow aspiration with iron stain",
       "Packed red cell transfusion, then iron replacement and control of the bleeding",
       "Abdominal ultrasonography to look for a hidden source of blood loss"],
      3,
      "เคสดัดแปลงจาก **Case 2 ในสไลด์** — microcytic + **RDW 21%** + **platelet 800 (reactive thrombocytosis)** + เสียเลือดเรื้อรัง = **IDA**\n\nเกณฑ์ให้ RBC ในสไลด์: **CVS ไม่คงที่ · มีอาการจากซีด · หรือยังเสียเลือดต่อเนื่องมาก** — ผู้ป่วยรายนี้ **มีอาการ** (ใจสั่น เหนื่อย ชีพจร 112) และ **กำลังมีประจำเดือนมาก** → **ให้ PRC ก่อน** แล้วตามด้วยเหล็กและควบคุมเลือดออก (ส่งเลือดตรวจ ferritin ก่อนให้เลือด)\n\n- เหล็กกินอย่างเดียวเหมาะเมื่อ **คงที่ ไม่มีอาการ** — โจทย์ต้นฉบับในสไลด์ไม่ได้ให้อาการชัด จึงมีให้เลือกระหว่าง A กับ B (โน้ตลายมือทำเครื่องหมายทั้งสองข้อ)\n- Hb electrophoresis ขณะขาดเหล็กแปลผลผิด (HbA2 ต่ำลง)\n- ไม่ต้องเจาะไขกระดูกเมื่อเหตุชัด\n- แหล่งเสียเลือดรู้แล้ว (ประจำเดือน) — ประเมินทาง gyne ต่อภายหลัง",
      "IDA + มีอาการ/ยังเสียเลือดมาก → PRC · คงที่ไม่มีอาการ → เหล็ก",
      [REF_SLIDE, "BSH Guideline for the laboratory diagnosis of iron deficiency in adults (2021)"],
      ["2.3.3(7)", "B2.4(1)", "B2.4(2)", "3.3.26"]),
    q("HON-ANM-MCQ-K11", "Stages of iron deficiency",
      "A regular blood donor has serum ferritin 14 µg/L, serum iron 42 µg/dL, TIBC 390 µg/dL and transferrin saturation 11%. Hb is 12.9 g/dL (male reference ≥ 13), MCV 84 fL and the smear shows normocytic normochromic red cells. Which stage of iron deficiency best fits?",
      ["Normal iron status",
       "Negative iron balance (iron depletion) only",
       "Iron-deficient erythropoiesis, before microcytic hypochromic anemia develops",
       "Established iron deficiency anemia with hypochromic microcytic cells",
       "Anemia of chronic disease"],
      2,
      "ใช้ตาราง **สามระยะของการพร่องเหล็ก** ในสไลด์\n\n| ระยะ | ferritin | serum iron / Tsat | morphology |\n|---|---|---|---|\n| Negative iron balance | **< 20** | ปกติ | ปกติ |\n| **Iron-deficient erythropoiesis** | < 15 | **iron < 50 · Tsat < 20** | **ยังปกติ** |\n| IDA | < 15 | iron < 30 · Tsat < 16 | **hypochromic microcytic** |\n\nผู้ป่วย: ferritin 14 · iron 42 · Tsat 11% · TIBC 390 แต่ **เซลล์ยังปกติ (MCV 84)** และ Hb เพิ่งต่ำกว่าเกณฑ์เล็กน้อย → **iron-deficient erythropoiesis** — เหล็กไม่พอสร้างเม็ดเลือดแล้วแต่ยังไม่ทันเห็นเซลล์เล็ก (สไลด์: MCV จะลดเมื่อ Hb < 10)\n\n- Negative balance ยังมี serum iron/Tsat ปกติ\n- ACD ferritin ปกติหรือสูง TIBC ต่ำ\n- (เสริม) ผู้บริจาคเลือดประจำเป็นกลุ่มเสี่ยงที่สไลด์ระบุในหมวด 'เสียเหล็กเพิ่ม'",
      "Ferritin ลดก่อน → iron/Tsat ตก (เซลล์ยังปกติ) → สุดท้าย hypochromic microcytic",
      [REF_SLIDE],
      ["2.3.3(7)", "3.3.26", "B2.2.5(1)"]),
    q("HON-ANM-MCQ-K12", "Megaloblastic anemia after gastrectomy (slide case 3)",
      "An 80-year-old woman with type 2 diabetes treated with metformin and a remote history of total gastrectomy presents with malaise. She is moderately pale, not jaundiced, with no lymphadenopathy or organomegaly. Hb 7 g/dL, MCV 120 fL, WBC 2,500/µL, platelets 100,000/µL. Which treatment regimen is most appropriate once the diagnosis is confirmed?",
      ["Oral folic acid 5 mg/day alone",
       "Vitamin B12 1,000 µg injections daily for 1–2 weeks, then weekly for a month, then monthly for life",
       "Intravenous iron 1,000 mg",
       "Prednisolone 1 mg/kg/day",
       "Erythropoietin-stimulating agent"],
      1,
      "เคสนี้คือ **Case 3 ในสไลด์** — **pancytopenia + MCV 120** + **เคยตัดกระเพาะ** (ไม่มี parietal cell → ไม่มี intrinsic factor) → **megaloblastic anemia จาก B12 deficiency** (metformin เป็นปัจจัยเสริม)\n\nการรักษาตามสไลด์: **B12 1,000 µg ฉีดทุกวัน 1–2 สัปดาห์ → ทุกสัปดาห์ 1 เดือน → ทุกเดือนตลอดชีวิต** (เหตุไม่หายไป จึงต้องให้ตลอด)\n\n- **Folate เดี่ยวห้ามให้** ใน B12 deficiency — เลือดดีขึ้นบางส่วนแต่ subacute combined degeneration แย่ลง\n- IV iron ไม่ตรงกับ MCV 120\n- Prednisolone ใช้ใน AIHA (ไม่มีเหลือง ไม่มีหลักฐานแตก)\n- ESA ใช้ในซีดจาก CKD",
      "หลังตัดกระเพาะ = ไม่มี IF → B12 ฉีด 1,000 µg ทุกวัน → สัปดาห์ → เดือน ตลอดชีวิต",
      [REF_SLIDE, "BSH Guidelines for the diagnosis and treatment of cobalamin and folate disorders (2014)"],
      ["2.3.3(7)", "B2.2.5(1)", "2.3.6-3(9)", "B2.4(2)"]),
  ],
  "figs": {},
}

# ---------------------------------------------------------------- K5
K5_MD = r"""### Hemoglobin ปกติของผู้ใหญ่
| ชนิด | โครงสร้าง | สัดส่วน |
|---|---|---|
| **HbA** | α₂β₂ | **97%** |
| **HbA2** | α₂δ₂ | **2–3%** |
| **HbF** | α₂γ₂ | **< 1%** |
Thalassemia = โรคกรรมพันธุ์ที่สร้าง globin chain ได้ลดลงบางส่วนหรือไม่ได้เลย

### Pathophysiology ในสไลด์
- **β-thalassemia** — β-chain ขาด → **α-chain เกิน ตกตะกอนในเซลล์ตัวอ่อน** → ineffective erythropoiesis + hemolysis
- **α-thalassemia** — α-chain ขาด → chain ที่เหลือจับกันเอง
  - ทารก: **γ₄ = Hb Bart's** — **O₂ affinity สูงมาก ปล่อย O₂ ไม่ได้** ("physiologically useless") → tissue hypoxia
  - ผู้ใหญ่: **β₄ = Hb H** — ไม่มีประโยชน์ทางสรีระ **ตกตะกอนใน RBC** → hemolytic anemia

### Genotype–phenotype ของ α-thalassemia (ตารางในสไลด์)
| ชนิด | Genotype | ความรุนแรง | Hb typing |
|---|---|---|---|
| ปกติ | αα/αα | ปกติ | A2A (HbA ~97.5% · A2 2.5–3.5%) |
| **α-thal 2 trait** (α⁺) | -α/αα | ปกติ · **MCV > 80** | A2A ปกติ |
| **α-thal 1 trait** (α⁰) | --/αα | ไม่มีอาการ · **MCV < 80** | cord blood: **Hb Bart's 2–10%** · ผู้ใหญ่ A2A ปกติ |
| Homozygous Hb CS | αᶜˢα/αᶜˢα | เล็กน้อย | A A2 CS (Hb CS ~5%) |
| **Hb H–Constant Spring** | --/αᶜˢα | **รุนแรงกว่า Hb H** | A A2 H CS (CS 2–3% · H 10–15%) |
| **Hb H disease** | --/-α | ปานกลาง (NTDT) | cord blood: Bart's 10–30% · ผู้ใหญ่ **A A2 H** |
| **Hb Bart's hydrops** | --/-- | **เสียชีวิตในครรภ์/แรกคลอด** | Hb Bart's > 80% + Hb Portland |
- **α-thal 1 trait และ α-thal 2 trait ตรวจ Hb typing ผู้ใหญ่ได้ปกติ** → ต้องใช้ **DNA analysis** (โดยเฉพาะคัดกรองคู่สมรส)

### แบ่งตามความต้องการเลือด — TDT vs NTDT
- **TDT (transfusion-dependent)**: β-thal major · β-thal/HbE ชนิดรุนแรง · Hb H hydrops
- **NTDT (non-transfusion-dependent)**: β-thal/HbE ส่วนใหญ่ · **Hb H disease · Hb H-CS** · β-thal intermedia — ให้เลือดเป็นครั้งคราว (ติดเชื้อ ตั้งครรภ์ ผ่าตัด)
- (เสริม) **NTDT ก็เหล็กเกินได้แม้ไม่ค่อยได้เลือด** — ineffective erythropoiesis → **erythroferrone ↑ → hepcidin ↓ → ดูดซึมเหล็กจากลำไส้มาก**
- ภาวะแทรกซ้อนที่พบบ่อย (Viprakasit, Vox Sang 2015): TDT — เหล็กเกินที่หัวใจ ตับ ต่อมไร้ท่อ · NTDT — extramedullary hematopoiesis · pulmonary hypertension · thrombosis · แผลที่ขา · นิ่วในถุงน้ำดี · เหล็กเกินที่ตับ

### ประเมินเหล็กเกิน
| วิธี | เกณฑ์ |
|---|---|
| **Liver iron concentration (LIC)** (mg Fe/g dry wt) | **< 2** ปกติ · **2–7** เล็กน้อย ยอมรับได้ · **7–15** ปานกลาง เสี่ยง **ตับพังผืดและเบาหวาน** · **> 15** รุนแรง |
| **Serum ferritin** | **> 2,500 ng/mL** → เสี่ยงภาวะแทรกซ้อนทางหัวใจ |
| **Cardiac MRI T2∗** | **> 20 ms** ปกติ · **10–20** ปานกลาง · **< 10 ms** รุนแรง เสี่ยงหัวใจล้มเหลว |
- T2∗ **ยิ่งสั้นยิ่งมีเหล็กมาก** (เหล็กทำให้สัญญาณ MRI จางเร็ว)

### ข้อบ่งชี้เริ่มยาขับเหล็กใน TDT
- ได้เลือด **> 1 ปี** หรือ **> 10 ครั้ง/ปี**
- **Serum ferritin > 1,000 ng/mL** (ตรวจ 2 ครั้งห่างกัน 1–3 เดือน)
- **LIC > 7 mg/g dry weight** (biopsy หรือ MRI)

### ยาขับเหล็ก 3 ตัว (ตารางในสไลด์)
| | **Desferrioxamine (DFO)** | **Deferasirox (DFX)** | **Deferiprone (DFP)** |
|---|---|---|---|
| Chelator : iron | **1 : 1** | **2 : 1** | **3 : 1** |
| ขนาด (mg/kg/วัน) | 20–60 | 20–40 | 75–100 |
| วิธีให้ | **SC 8–12 ชม. 5–7 คืน/สัปดาห์** หรือ IV | **กิน วันละครั้ง** | **กิน วันละ 3 ครั้ง** |
| Half-life | **20–30 นาที** | 8–16 ชม. | 3–4 ชม. |
| ขับออก | ปัสสาวะ + อุจจาระ | **อุจจาระ** | **ปัสสาวะเป็นหลัก** |
| ขับเหล็กที่ตับ | +++ | +++ | ++ |
| ขับเหล็กที่หัวใจ | ++ | ++ | **+++** |
| ผลข้างเคียงหลัก | **ก้อนตรงที่ฉีด** · **กระดูกผิดปกติ (เด็ก)** · **ototoxicity · ophthalmic** · **ติดเชื้อ Yersinia/Klebsiella** | ผื่น · คลื่นไส้ ท้องเสีย · **Cr ขึ้น (กลับคืนได้ ไม่ลุกลาม)** · LFT ผิดปกติ | ทางเดินอาหาร · **ปวดข้อ/ข้ออักเสบ** · LFT ผิดปกติ · **neutropenia · agranulocytosis** |
| อายุ | ไม่แนะนำ < 3 ปี (เหล็กยังต่ำ) | ศึกษาในเด็กตั้งแต่ 2 ปี | ข้อมูลน้อยในเด็ก < 6–10 ปี |
- ✍️ ข้างตาราง DFO: **ติดตาม infection** (เหล็กที่จับกับ DFO = siderophore ที่ Yersinia ใช้โต)
- (เสริม) Deferiprone ขับเหล็กหัวใจดีที่สุด → ใช้เมื่อ **T2∗ < 10 ms** (มักใช้ร่วมกับ DFO) · ปัสสาวะสีน้ำตาลแดงได้

### การติดตามระหว่างใช้ยา — จุดเน้นจากตาราง
| ยา | ต้องเฝ้าระวังเป็นพิเศษ |
|---|---|
| **DFO** | **audiogram + ตรวจตา ทุกปี** · CBC ทุก 3–4 สัปดาห์ · ferritin LFT BUN/Cr ทุก 3 เดือน |
| **DFP** | **CBC ทุกสัปดาห์ช่วง 2 เดือนแรก** (agranulocytosis) แล้วทุก 3–4 สัปดาห์ · LFT · **Zn (optional)** |
| **DFX** | **BUN/Cr และ U/A ทุก 3–4 สัปดาห์** (ไต) · LFT ทุก 3–4 สัปดาห์ช่วงแรก · audiogram/ตา ทุกปี |
- ทุกตัว: **serum ferritin ทุก 3 เดือน** · ผู้ใหญ่ตรวจตามรอบทุก 3 เดือน · เด็กบางรายการทุก 6–8 สัปดาห์
"""

K5 = {
  "id": "hon-anm-k5",
  "title": "สไลด์ อ.Kunapa ⑤ — Thalassemia: genotype–phenotype, TDT/NTDT, เหล็กเกิน และยาขับเหล็ก 3 ตัว",
  "minutes": 15,
  "summary": "HbA 97% · A2 2–3% · F < 1% · Hb Bart's (γ₄) O₂ affinity สูง · Hb H (β₄) ตกตะกอน → hemolysis · α-thal 1 trait --/αα MCV < 80 Hb typing ผู้ใหญ่ปกติ · LIC > 7 · ferritin > 2,500 · T2∗ < 10 ms · เริ่มขับเหล็ก: ได้เลือด > 1 ปี/> 10 ครั้งต่อปี · ferritin > 1,000 · LIC > 7 · DFO 1:1 SC (หู ตา Yersinia) · DFX 2:1 กินวันละครั้ง (ไต) · DFP 3:1 กินวันละ 3 ครั้ง (agranulocytosis, หัวใจดีสุด)",
  "source": SRC,
  "nl": ["2.3.3(8)", "B2.2.1(1)", "B2.2.1(2)", "3.3.5", "B2.3(4)", "B2.4(1)", "B2.4(2)"],
  "md": K5_MD,
  "pearls": [
    "Hb Bart's (γ₄) จับ O₂ แน่นจนปล่อยไม่ได้ · Hb H (β₄) ตกตะกอนใน RBC → hemolysis",
    "α-thal 1 trait (--/αα) MCV < 80 แต่ Hb typing ผู้ใหญ่ปกติ → ต้อง DNA",
    "เหล็กเกิน: LIC > 7 ปานกลาง (> 15 รุนแรง) · ferritin > 2,500 เสี่ยงหัวใจ · T2∗ < 10 ms รุนแรง",
    "เริ่มขับเหล็กใน TDT: ได้เลือด > 1 ปี หรือ > 10 ครั้ง/ปี · ferritin > 1,000 สองครั้ง · LIC > 7",
    "DFO 1:1 SC (หู ตา กระดูก Yersinia) · DFX 2:1 กินวันละครั้ง (ไต ตับ) · DFP 3:1 กินวันละ 3 ครั้ง (agranulocytosis · หัวใจดีสุด)",
    "NTDT ก็เหล็กเกินได้จาก hepcidin ต่ำ แม้ไม่ค่อยได้เลือด",
  ],
  "items": [
    q("HON-ANM-MCQ-K13", "Iron chelators — adverse effects",
      "A 24-year-old man with transfusion-dependent β-thalassemia/HbE starts an oral iron chelator taken three times a day. Six weeks later he develops fever and sore throat; his absolute neutrophil count is 0.3 × 10⁹/L. Which drug is he most likely taking, and what monitoring should have been in place?",
      ["Deferasirox — monthly serum creatinine",
       "Desferrioxamine — annual audiogram",
       "Deferiprone — weekly CBC during the first months of therapy",
       "Deferasirox — weekly CBC",
       "Desferrioxamine — monthly urinalysis"],
      2,
      "**กินวันละ 3 ครั้ง = Deferiprone (DFP)** (half-life สั้น 3–4 ชม.) · ผลข้างเคียงสำคัญ = **neutropenia/agranulocytosis** → สไลด์ให้ตรวจ **CBC ทุกสัปดาห์ช่วง 2 เดือนแรก** แล้วทุก 3–4 สัปดาห์ · มีไข้ + ANC ต่ำ → **หยุดยาทันที** รักษาแบบ febrile neutropenia\n\n- Deferasirox **กินวันละครั้ง** — เด่นเรื่อง **ไต (Cr ขึ้น)** ตับ ผื่น ทางเดินอาหาร → ตรวจ BUN/Cr U/A บ่อย\n- Desferrioxamine **ฉีด SC/IV** — เด่นเรื่อง **ototoxicity ตา กระดูก ติดเชื้อ Yersinia** → audiogram/ตรวจตาทุกปี\n- (เสริม) DFP ขับเหล็กที่ **หัวใจ** ได้ดีที่สุด (+++)",
      "DFP กินวันละ 3 ครั้ง → agranulocytosis → CBC ทุกสัปดาห์ · DFX วันละครั้ง → ไต · DFO ฉีด → หู ตา Yersinia",
      [REF_SLIDE, "TIF Guidelines for the management of transfusion dependent thalassaemia, 4th ed. (2021)"],
      ["2.3.3(8)", "B2.4(2)", "B2.2.1(2)"]),
    q("HON-ANM-MCQ-K14", "Iron overload — assessment and when to chelate",
      "A 12-year-old boy with β-thalassemia major has received monthly transfusions for 3 years without chelation. Serum ferritin is 2,800 ng/mL on two occasions, liver iron concentration (MRI) is 16 mg Fe/g dry weight, and cardiac MRI T2∗ is 8 ms. Which interpretation is correct?",
      ["Iron overload is mild; recheck in a year before starting chelation",
       "Severe hepatic and severe cardiac iron loading; start intensive chelation that includes an agent effective at removing cardiac iron",
       "Severe hepatic iron loading only; cardiac T2∗ of 8 ms is normal",
       "Cardiac T2∗ of 8 ms is normal because a lower T2∗ means less iron",
       "Chelation is not indicated because the liver iron is below 20 mg/g"],
      1,
      "เกณฑ์ในสไลด์\n- **LIC > 15 mg/g = severe** (7–15 ปานกลาง เสี่ยงตับพังผืดและเบาหวาน)\n- **Ferritin > 2,500 ng/mL** = เสี่ยงภาวะแทรกซ้อนทางหัวใจ\n- **T2∗ < 10 ms = severe cardiac iron** (> 20 ปกติ · 10–20 ปานกลาง) — **T2∗ ยิ่งสั้นยิ่งเหล็กมาก**\n\nข้อบ่งชี้ขับเหล็กครบทุกข้อ (ได้เลือด > 1 ปี · > 10 ครั้ง/ปี · ferritin > 1,000 สองครั้ง · LIC > 7) → ต้อง **chelation เข้มข้น** และเพราะหัวใจรุนแรงต้องใช้ยาที่ขับเหล็กหัวใจได้ดี — (เสริม) มักใช้ **DFO ร่วมกับ deferiprone** (DFP หัวใจ +++)\n\nตัวลวงเข้าใจทิศทางของ T2∗ กลับด้าน หรือใช้เกณฑ์ LIC ผิด",
      "LIC > 15 · ferritin > 2,500 · T2∗ < 10 ms = เหล็กเกินรุนแรง (หัวใจ) — T2∗ ยิ่งต่ำยิ่งแย่",
      [REF_SLIDE, "TIF Guidelines for the management of transfusion dependent thalassaemia, 4th ed. (2021)"],
      ["2.3.3(8)", "B2.2.1(1)", "B2.4(2)"]),
    q("HON-ANM-MCQ-K15", "α-thalassemia genotype–phenotype",
      "A couple is screened before pregnancy. Both have MCV around 70 fL, normal ferritin, and adult Hb typing showing only HbA2A with normal HbA2. Which genotype best explains these findings, and what is the main risk to their fetus?",
      ["α-thal 2 trait (-α/αα) in both; risk of Hb H disease only",
       "β-thal trait in both; risk of β-thalassemia major",
       "α-thal 1 trait (--/αα) in both; 25% risk of Hb Bart's hydrops fetalis",
       "Homozygous Hb Constant Spring in both; risk of Hb H–Constant Spring",
       "Normal genotypes; microcytosis is due to anemia of chronic disease"],
      2,
      "จากตาราง genotype–phenotype ในสไลด์\n- **α-thal 1 trait (--/αα)** → **MCV < 80** แต่ **Hb typing ผู้ใหญ่ปกติ (A2A)** — เข้ากับทั้งคู่\n- α-thal 2 trait (-α/αα) มัก **MCV > 80**\n- β-thal trait ต้องเห็น **HbA2 สูง (> 3.5%)** — ที่นี่ HbA2 ปกติ\n- Homozygous Hb CS จะเห็น **Hb CS ~5%** ใน Hb typing\n- ferritin ปกติ ตัดขาดเหล็ก\n\nพ่อแม่เป็น --/αα ทั้งคู่ → ลูกมีโอกาส **--/-- = Hb Bart's hydrops fetalis 25%** (Hb Bart's > 80% จับ O₂ ไม่ปล่อย) → ยืนยันด้วย **DNA analysis** และให้คำปรึกษาก่อนคลอด",
      "MCV < 80 + Hb typing ปกติ + ferritin ปกติ = นึกถึง α-thal 1 trait → DNA · คู่สมรสเป็นทั้งคู่ = Bart's hydrops 25%",
      [REF_SLIDE, "TIF Guidelines for the management of non-transfusion dependent thalassaemia, 2nd ed. (2017)"],
      ["2.3.3(8)", "3.3.5", "B2.2.1(1)", "B2.3(4)"]),
  ],
  "figs": {},
  "mnem": [
    {"name": "O · X · P = 1 · 2 · 3",
     "what": "ยาขับเหล็กเรียงตามสัดส่วน chelator : iron และจำนวนมื้อ",
     "lines": [["1", "DF**O** — 1:1 · **ฉีด** SC 8–12 ชม. · พิษ **หู ตา กระดูก · Yersinia**"],
               ["2", "DF**X** (deferasirox) — 2:1 · กิน **วันละ 1 ครั้ง** · พิษ **ไต ตับ** ผื่น"],
               ["3", "DF**P** (deferiprone) — 3:1 · กิน **วันละ 3 ครั้ง** · พิษ **agranulocytosis** ปวดข้อ · **หัวใจ +++**"]],
     "note": "P = PMN หาย (agranulocytosis) และ P = Pump (หัวใจ) — DFP ขับเหล็กหัวใจดีที่สุด",
     "src": "เรียบเรียงจากตารางในสไลด์ อ.Kunapa"}
  ],
}

NEW_SECTIONS = [K1, K2, K3, K4, K5]
