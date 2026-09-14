# SPEC — โครงสร้างข้อมูลและมาตรฐานการเขียนข้อ (med421-kit)

## 1. ไฟล์ในชุด

| ไฟล์ | หน้าที่ |
|---|---|
| `config.json` | **ไฟล์เดียวที่ต้องแก้เวลาเพิ่มระบบ** — ปฏิทิน lecture, สีของระบบ, seed, รายชื่อไฟล์ข้อสอบ |
| `data/<system>.json` | คลังข้อสอบของแต่ละระบบ |
| `refs/nl_2567.json` | ดัชนีเกณฑ์แพทยสภา พ.ศ. 2567 (NL Syllabus) ใช้ผูกรายข้อ |
| `build.py` | รวม → ตรวจ → สลับเฉลย → เว็บ → PDF |
| `check_numbers.py` | ตรวจ ABG ทุกข้อด้วย Henderson–Hasselbalch + Winter's + anion gap |
| `site/` | ผลลัพธ์ (ไม่ต้องแก้มือ) |

## 2. config.json

```jsonc
{
  "course": "...", "build": { "out_dir": "site", "pdf": true,
                              "nl_reference_file": "refs/nl_2567.json" },
  "systems": [{
    "key": "air",                    // ใช้เป็นชื่อไฟล์ผลลัพธ์ air.html / air.pdf
    "name_th": "ระบบการหายใจ",
    "name_en": "AIR — Airway & Respiratory System",
    "file": "data/air.json",
    "color": "#0ea5a4",              // สีประจำระบบ (ใช้ทั้งเว็บและ PDF)
    "seed": 4210,                    // seed สลับตัวเลือก — คงที่ต่อระบบ ห้ามเปลี่ยนหลังแจกโพย
    "lectures": [ { "lec": "AIR-01", "title": "...", "date": "" } ]
  }]
}
```

`lec` ของทุกข้อต้องมีอยู่ใน `lectures` ของระบบนั้น มิฉะนั้น build จะหยุด

## 3. schema ของข้อสอบ

### 3.1 MCQ

```jsonc
{
  "id": "AIR-MCQ-07",          // <SYSTEM>-MCQ-<nn> ห้ามซ้ำทั้งคลัง
  "type": "mcq",
  "lec": "AIR-03",
  "topic": "Acute asthma exacerbation",
  "stem": "A 30-year-old asthmatic woman ...",
  "choices": ["คำตอบที่ถูก", "ตัวลวง 1", "ตัวลวง 2", "ตัวลวง 3", "ตัวลวง 4"],
  "answer": 0,                  // เขียน 0 เสมอ — build สลับให้เอง
  "ref": "GINA 2024 Chapter 4",
  "pearl": "ประโยคเดียวที่อยากให้จำ",
  "nl": ["2.2.11", "B6.4(4)"],  // รหัสจาก refs/nl_2567.json
  "abg": { "ph": 7.28, "paco2": 48, "hco3": 22 },   // ใส่เมื่อโจทย์มี ABG
  "source_note": "ระบุเมื่อดัดแปลงตัวเลขจากต้นฉบับ"  // ไม่บังคับ
}
```

### 3.2 MEQ

```jsonc
{
  "id": "AIR-MEQ-01", "type": "meq", "lec": "AIR-05", "topic": "...",
  "scenario": "โจทย์ยาว 1 ย่อหน้า",
  "questions": [ { "q": "คำถามย่อย", "a": "แนวตอบ", "points": 2 } ],
  "ref": "...", "pearl": "...", "nl": ["2.3.10(5)"]
}
```

## 4. มาตรฐานการเขียนข้อ

1. **คำตอบถูกไว้ตัวแรกเสมอ (`answer: 0`)** แล้วให้ build สลับ — คนเขียนจะได้ไม่เผลอทำ key หาย
2. ตัวเลือก **5 ตัว ห้ามซ้ำ** ความยาวใกล้เคียงกัน หลีกเลี่ยง "ถูกทุกข้อ / ไม่มีข้อถูก"
3. stem เป็น clinical vignette: อายุ–เพศ–อาการ–ระยะเวลา → PE (T, PR, RR, BP, SpO2) → lab → คำถาม
4. คำถามเน้นคำเดียว: MOST likely diagnosis / MOST appropriate initial management / BEST explains
5. ตัวลวงต้องเป็นโรคหรือการรักษาที่ "เกือบใช่" ในบริบทเดียวกัน ไม่ใช่ของหลุดระบบ
6. ทุกข้อต้องมี `ref` (guideline + ปี หรือแหล่งโพยต้นฉบับ) และ `pearl` 1 ประโยค
7. ทุกข้อควรผูก `nl` อย่างน้อย 1 รหัส — เพื่อเช็คว่าคลังครอบคลุมเกณฑ์แพทยสภาแค่ไหน
8. หลีกเลี่ยงเครื่องหมาย `"` `<` `>` ในข้อความ (ใช้เครื่องหมายคำพูดเดี่ยวหรือเว้น) เพื่อให้ JSON และ HTML สะอาด

## 5. สูตรตรวจตัวเลข (`check_numbers.py`)

| สูตร | ใช้ตรวจ |
|---|---|
| Henderson–Hasselbalch: `pH = 6.1 + log10(HCO3 / (0.03 × PaCO2))` | pH ที่เขียนต้องตรงกับ PaCO2/HCO3 ±0.03 มิฉะนั้นถือว่า **ผิด** (exit 1) |
| Winter's: `PaCO2 คาด = 1.5 × HCO3 + 8 ± 2` | ถ้า HCO3 < 22 แล้ว PaCO2 หลุดช่วง → เตือน (INFO) ว่าเป็น mixed disorder หรือเขียนผิด |
| Anion gap: `AG = Na − Cl − HCO3` | รายงานค่าให้ตรวจกับเฉลย (ใส่ `na`, `cl` ใน `abg`) |
| Delta ratio: `ΔAG / ΔHCO3` | ใช้ตีความ triple disorder — ตรวจด้วยมือจากค่า AG ที่สคริปต์พิมพ์ |
| A–a gradient: `PAO2 = FiO2 × (760 − 47) − PaCO2/0.8` | ใช้ตอนเขียน pearl ของข้อ gas exchange |

## 6. สิ่งที่ build ตรวจให้ (หยุดทันทีถ้าเจอ)

- `id` ซ้ำ
- ตัวเลือกไม่ครบ 5 / ตัวเลือกซ้ำ
- `answer` ไม่เท่ากับ 0
- `lec` ไม่มีในปฏิทินของระบบ
- MEQ ไม่มี `questions` หรือ `scenario` / ข้อย่อยไม่มีคำตอบ
- type ไม่ใช่ mcq/meq

**เตือน (ไม่หยุด build):** ลืม `ref`, ลืม `pearl`, ไม่ผูก `nl`, หรืออ้าง NL code ที่ไม่มีในดัชนี

## 7. การสลับเฉลย

`random.Random(seed ของระบบ)` เรียงข้อตาม `id` แล้วสลับทีละข้อ → build ใหม่จากศูนย์ได้ไฟล์ **byte-identical**
ถ้าอยากได้ชุดสลับใหม่ (เช่นแจกคนละ version) ให้เปลี่ยน `seed` ใน `config.json` เท่านั้น
