# MED421 Question Bank Kit — สเปกและวิธีใช้

ชุดนี้ทำให้การเพิ่มระบบใหม่เหลือแค่ **เขียนไฟล์ JSON** แล้วสั่ง build อย่างเดียว
โค้ดเรนเดอร์เว็บ สลับเฉลย ตรวจ schema และออก PDF ทำให้หมดแล้ว

---

## 1. โครงสร้างไฟล์

```
kit/
├── config.json        ← แก้ไฟล์นี้เวลาเพิ่มระบบใหม่ (ไม่ต้องแตะโค้ด)
├── build.py           ← สั่งไฟล์เดียวจบ: รวม → ตรวจ → สลับเฉลย → เว็บ → PDF
├── render_pdf.py      ← build.py เรียกให้เอง ไม่ต้องรันตรง
├── template.html      ← หน้าเว็บทำข้อสอบ (มี placeholder __DATA__ ฯลฯ)
├── data/              ← ไฟล์ข้อสอบทั้งหมด (JSON)
│   ├── cardio_mcq_a.json   cardio_mcq_b.json   cardio_meq_osce.json   cardio_old.json
│   ├── nephro_*.json
│   └── chest_*.json
└── ผลลัพธ์ที่ build ออกมา: drill.html · bank_merged.json · MED421_<ระบบ>.pdf
```

## 2. คำสั่ง

```bash
python3 build.py                 # สร้างทุกระบบใน config.json
python3 build.py neuro           # สร้างเฉพาะระบบเดียว (ระบบอื่นคงไว้ใน bank_merged.json)
python3 build.py neuro --no-pdf  # เฉพาะเว็บ — ใช้ตอนกำลังเขียนข้อ เร็วกว่ามาก
```

build จะ **หยุดพร้อมบอกจุดผิด** ถ้าเจอ: id ซ้ำ · ตัวเลือกไม่ครบ 5 · ตัวเลือกซ้ำกัน · `answer` ผิดช่วง ·
`lec` ที่ไม่มีในปฏิทิน · MEQ ที่ไม่มี `questions` · OSCE ที่ไม่มี `answer`
และจะ **เตือน** (ไม่หยุด) ถ้าข้อไหนไม่มี `ref` หรือ `pearl`

---

## 3. Schema (สำคัญที่สุด — เขียนตามนี้เป๊ะ ๆ)

### 3.1 MCQ ใหม่ — `data/<ระบบ>_mcq_a.json` (array)

```json
{
  "id": "CH-MCQ-01",
  "lec": "03",
  "lecture": "Pulmonary tuberculosis / ABG (อ.ศิวพร)",
  "topic": "Latent tuberculosis infection in a household contact",
  "stem": "A 28-year-old healthy woman is the household contact of ... Which of the following is the most appropriate management?",
  "choices": [
    "ตัวเลือกที่ถูก — เขียนไว้ตำแหน่งแรกเสมอ",
    "ตัวลวง 1", "ตัวลวง 2", "ตัวลวง 3", "ตัวลวง 4"
  ],
  "answer": 0,
  "explain": "**คำอธิบายภาษาไทย** รองรับ markdown: **ตัวหนา**, ตาราง |...|, - bullet, 1. เลข, > quote",
  "pearl": "ประโยคเดียวที่จำไปสอบได้เลย",
  "ref": ["MED31 past paper loop C&D", "MED35 สอบลงกองครั้งที่ 1 ข้อ 7"],
  "part": "MCQ",
  "nl": ["2.3.13(2)", "B5.2.5(1)"]
}
```

**ฟิลด์ `nl` — อ้างอิงเกณฑ์แพทยสภา พ.ศ. 2567**
ใส่รหัสหัวข้อจาก `refs/nl_2567.json` ได้หลายรหัสต่อข้อ ใช้ได้กับ **ทั้ง MCQ, MEQ/OSCE และคลังข้อสอบเก่า**
`build.py` จะเรนเดอร์เป็นชิป `NL …` พร้อมชื่อเต็ม ส่วน และเลขหน้า ทั้งในเว็บและ PDF
ถ้าอ้างรหัสที่ยังไม่มีในดัชนี build จะ **เตือน** (ไม่หยุด) ให้ไปเพิ่มรหัสนั้นใน `refs/nl_2567.json` ก่อน

**กฎเหล็ก**
- **เขียน `"answer": 0` เสมอ และวางคำตอบที่ถูกไว้ `choices[0]`** — `build.py` สลับตำแหน่งให้เองแบบ deterministic
  (seed แยกต่อระบบ → build ใหม่กี่ครั้งก็ได้ตำแหน่งเดิม แต่ไม่ใช่ A ทุกข้อ)
- `choices` ต้องมี **5 ข้อ ห้ามซ้ำกัน** และทุกข้อต้องมีเหตุผลให้คนเลือก
- `id` ใช้ pattern `<2 ตัวอักษรของระบบ>-MCQ-<เลข 2 หลัก>` เช่น `NE-MCQ-01`

### 3.2 MEQ + OSCE/SAQ — `data/<ระบบ>_meq_osce.json` (array เดียว รวมกัน)

**MEQ**
```json
{
  "id": "CH-MEQ-01", "part": "MEQ", "lec": "03",
  "lecture": "Pulmonary tuberculosis / ABG (อ.ศิวพร)",
  "topic": "Active pulmonary tuberculosis",
  "vignette": "ผู้ป่วยชายไทยอายุ 46 ปี ...\nU/D: ...\nPE: ...\nV/S: ...\nLab: ...\nCXR: ...",
  "questions": [
    {"q": "1. จงให้การวินิจฉัยที่น่าจะเป็นมากที่สุด พร้อมข้อมูลสนับสนุน", "a": "แนวคำตอบ markdown ภาษาไทย"},
    {"q": "2. ...", "a": "..."}
  ],
  "ref": ["MED33 MEQ วัณโรคปอด"]
}
```

**OSCE / SAQ** (ใช้ `station` + `instruction` + `answer` แทน `vignette` + `questions`)
```json
{
  "id": "CH-OSCE-02", "part": "OSCE/SAQ", "lec": "17",
  "lecture": "Pleural disease / Respiratory failure (อ.สกล)",
  "topic": "SAQ – Chest radiograph: tension pneumothorax",
  "station": "SAQ (เขียนตอบ) 5 นาที",
  "instruction": "โจทย์ + คำถามย่อย 2.1–2.5 พร้อมคะแนน",
  "answer": "เฉลยและเกณฑ์ให้คะแนน markdown ภาษาไทย",
  "ref": ["MED32 SAQ CXR pneumothorax"]
}
```

### 3.3 คลังข้อสอบเก่า — `data/<ระบบ>_old_a.json` (array)

**รูปแบบที่ใช้ตั้งแต่ Chest เป็นต้นไป — เรียบเรียงเป็นตัวเลือก เหมือนข้อใหม่**
```json
{
  "id": "CH-OLD-01", "lec": "03",
  "lecture": "Pulmonary tuberculosis / ABG (อ.ศิวพร)",
  "q": "โจทย์ภาษาอังกฤษ เรียบเรียงจากที่โพยจดไว้",
  "choices": ["ตัวที่ถูก", "ตัวลวง 1", "ตัวลวง 2", "ตัวลวง 3", "ตัวลวง 4"],
  "answer": 0,
  "note": "เฉลย + กลไกภาษาไทย — ถ้าโพยตอบผิดตามหลักปัจจุบัน ให้เขียนบอกตรงนี้",
  "src": "MED31 past paper loop C&D – ข้อความต้นฉบับที่โพยจดไว้"
}
```
`build.py` จะจัดกลุ่มตาม `lec` ให้เอง ตามลำดับใน `config.sets[].lecture_order`

*(รูปแบบเก่าแบบข้อความล้วน `{part, q, a, src}` ยังใช้ได้ — Cardio/Nephro ยังเป็นแบบนี้อยู่ ระบบจะเรนเดอร์ให้ถูกแบบอัตโนมัติ)*

### 3.4 เพิ่มระบบใหม่ใน `config.json`

```json
{
  "key": "neuro",
  "label": "Neuro",
  "thai": "ระบบประสาท",
  "blurb": "4 คาบบรรยาย · ...",
  "accent": {"light": "#6b3f8c", "soft": "#efe8f5", "ink": "#542f70",
             "dark": "#b998d8", "darkSoft": "#1d1526", "darkInk": "#cdb6e3"},
  "lecture_order": ["07", "16", "25", "34"],
  "mcq": ["data/neuro_mcq_a.json", "data/neuro_mcq_b.json"],
  "meq": ["data/neuro_meq_osce.json"],
  "old": ["data/neuro_old_a.json"]
}
```
ถ้า lecture ใหม่ยังไม่มีในปฏิทิน ต้องเพิ่มใน `config.lectures` ด้วย:
`"07": {"date": "พ. 17 ก.ย.", "week": 1, "al": 0}` (`al: 1` = คาบ Active Learning)

---

## 4. มาตรฐานการเขียนข้อ (สิ่งที่ทำให้ชุดนี้ต่างจาก quiz ทั่วไป)

1. **โจทย์ภาษาอังกฤษ** แบบ clinical vignette · **เฉลยและคำอธิบายภาษาไทย**
2. **5 ตัวเลือกที่มีเหตุผลรองรับทุกข้อ แต่ถูกข้อเดียว** — ตัวลวงต้องเป็นสิ่งที่นักเรียนเก่งพลาดจริง
   ไม่ใช่ตัวเลือกที่ผิดชัดจนไม่มีใครเลือก
3. **คำอธิบายต้องไล่กลไกก่อน** (pathophysiology / mechanism) แล้วจึงโยงคลินิก
   และต้อง **บอกทีละข้อว่าตัวลวงแต่ละตัวผิดเพราะอะไร**
4. มี **ตารางเปรียบเทียบ** เมื่อเป็นหัวข้อที่มีโรคคล้ายกันหลายโรค
5. ทุกข้อมี **`ref`** ระบุรุ่น/ครั้งที่สอบ/loop/เลขข้อของข้อสอบเก่าที่เป็นต้นแบบ
6. **ตัวเลขทุกตัวต้องสอดคล้องกันเอง** — ABG ต้องผ่าน Henderson–Hasselbalch,
   การชดเชยต้องผ่าน Winter's formula, Light's criteria ต้องคำนวณแล้วตรงกับข้อสรุป
   (ดู `check_numbers.py` ใน §5)
7. **ถ้าคำเฉลยในโพยไม่ตรงกับแนวทางปัจจุบัน ให้เขียนบอกไว้ในคำอธิบาย** อย่าลอกตาม

---

## 5. ตรวจตัวเลขก่อน build

```bash
python3 check_numbers.py          # ไล่ ABG ทุกข้อใน data/ ว่าผ่าน Henderson–Hasselbalch ไหม
```

สูตรที่ใช้บ่อย
| สิ่งที่ตรวจ | สูตร |
|---|---|
| ความสอดคล้องของ ABG | pH = 6.1 + log( HCO3 ÷ (0.03 × PaCO2) ) |
| Metabolic acidosis ชดเชยพอไหม | Winter's: PaCO2 ที่คาด = 1.5 × HCO3 + 8 ± 2 |
| Resp acidosis เฉียบพลัน | HCO3 เพิ่ม **1** ต่อ PaCO2 ที่สูงขึ้นทุก 10 |
| Resp acidosis เรื้อรัง | HCO3 เพิ่ม **3.5–4** ต่อ PaCO2 ที่สูงขึ้นทุก 10 |
| A-a gradient | PAO2 = FiO2 × 713 − PaCO2/0.8 ; ค่าปกติ = อายุ/4 + 4 |
| Anion gap | Na − (Cl + HCO3) ; corrected = AG + 2.5 × (4.0 − albumin) |
| Delta ratio | (AG − 12) ÷ (24 − HCO3) |
| Light's criteria (exudate ถ้าเข้าข้อใดข้อหนึ่ง) | โปรตีน ratio > 0.5 · LDH ratio > 0.6 · LDH น้ำ > ⅔ ULN ของ serum |

---

## 6. ความคืบหน้า

| ระบบ | ข้อใหม่ | คลังเก่า | สถานะ |
|---|---|---|---|
| Cardio | 50 | 130 | ✅ เสร็จ (คลังเก่ายังเป็นข้อความ) |
| Nephro | 50 | 124 | ✅ เสร็จ (คลังเก่ายังเป็นข้อความ) |
| Chest | 50 | 56 | ✅ เสร็จ (คลังเก่าเป็นตัวเลือกแล้ว) |
| **AIR** (Allergy/Immunology/Rheumatology) | **60** (MCQ 50 + MEQ 4 + OSCE/SAQ 6) | **50** | ✅ เสร็จ (คลังเก่าเป็นตัวเลือก + **ผูกรหัส NL 2567 ครบทุกข้อ**) |
| **Mock NL** (ชุดจำลอง NL Part 1) | **200** | — | ✅ นำเข้าแล้ว — แยกตามระบบ 11 สาขา (`lec` = M01–M11) เฉลย + คำอธิบายไทยรายข้อ จาก PDF ต้นฉบับ ผูก NL ระดับหมวด |
| Infectious (5 คาบ) · Neuro (4) · GI (4) · Endocrine (3) · Hemato (3) · Skin (2) · Onco (1) | — | — | ยังไม่ทำ |

**งานค้าง**
1. แปลงคลังเก่า Cardio 130 + Nephro 124 ข้อ ให้เป็นตัวเลือก 5 ข้อ เหมือน Chest/AIR
2. ผูกรหัส NL 2567 ย้อนหลังให้ Cardio, Nephro, Chest (build เตือนไว้ให้แล้วว่าข้อไหนยังไม่มี) — ต้องเพิ่มรหัสของระบบนั้น ๆ ใน `refs/nl_2567.json` ก่อน (ตอนนี้มีเฉพาะหัวข้อระบบหายใจและ AIR)
3. ใส่วันที่จริงของ lecture AIR (08, 23, 33) ใน `config.lectures` — ตอนนี้เป็น TBD
4. ชุด Mock ยังไม่มี `pearl` รายข้อ (build เตือนไว้) และผูก NL ไว้ระดับหมวด (2.3.x ทั้งหมวด) ถ้าต้องการละเอียดถึงระดับโรค ต้องไล่ใส่รายข้อเพิ่ม

## 7. ไฟล์อ้างอิงเกณฑ์แพทยสภา `refs/nl_2567.json`

```jsonc
{
  "source": "ประกาศแพทยสภาที่ 4/2567 ...",
  "entries": {
    "B5.2.5(1)": { "part": "ก. วิทยาศาสตร์การแพทย์พื้นฐาน",
                   "section": "B5.2.5 Metabolic and regulatory disorders",
                   "page": 27, "group": "1-2",
                   "title": "Crystal arthropathy (gout, pseudogout)" }
  }
}
```

- `group` `"1-2"` = ต้องวินิจฉัยและดูแลรักษาเบื้องต้นได้เอง, `"3"` = รู้จัก วินิจฉัยแยกโรค และส่งต่อได้ (ละไว้ได้ถ้าหัวข้อนั้นไม่ได้แบ่งกลุ่ม)
- ชี้ path ของไฟล์นี้ได้ที่ `config.nl_reference_file`
- เพิ่มรหัสใหม่ได้อิสระ ขอให้ `title`, `section`, `page` ตรงกับต้นฉบับประกาศ
