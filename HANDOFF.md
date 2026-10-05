# MED421 — สรุปสถานะงานทั้งหมด (อัปเดต 2 ต.ค. 2569 · รอบที่ 5)

ไฟล์นี้คือ "จุดกลับมาต่อ" ถ้า context เต็มหรือเปิด session ใหม่ อ่านไฟล์นี้ไฟล์เดียวก็ทำงานต่อได้

---

## 0. กฎสำรองข้อมูล — อ่านก่อนเริ่มงานทุกครั้ง ⚠️

### ทำไมต้องมีกฎนี้
Claude รันอยู่บนเครื่องชั่วคราวในคลาวด์ มี **2 จังหวะที่ข้อมูลหาย** คนละแบบกัน

| อาการ | เกิดอะไร | อะไรหาย |
|---|---|---|
| **Context เต็ม → ย่อบทสนทนา** | ระบบสรุปช่วงเก่าเป็นบทย่อ แล้วคุยต่อ | ข้อความเก่าในแชท · **ไฟล์บนดิสก์ไม่หาย** |
| **Session จบ / ทิ้งไว้นาน** | container ถูกคืน ลบทั้งเครื่อง | **`scratchpad/` หายหมด** |

รอบที่แล้วบทสนทนาถูกย่อไป 1 ครั้ง งานไม่หายเพราะเขียนลงดิสก์ไว้ทุกขั้น

### กฎ 3 ข้อ

**1. ผลงานที่ใช้ token เยอะ → เขียนลงไฟล์ทันที ไม่เก็บไว้ในแชท**
อ่าน PDF/สไลด์มาได้ กี่หน้าก็ตาม เขียนลงไฟล์**ทีละหน้า**เลย อย่ารวบไว้ตอบทีเดียว
ถ้าบทสนทนาถูกย่อกลางคัน งานที่อยู่ในแชทหาย แต่ไฟล์ยังอยู่

**2. จบงานหนึ่งก้อน → commit เข้า repo ทันที ไม่รอจบ session**

```bash
cd /home/claude/ioioioio (หรือ /home/user/ioioioio แล้วแต่ container)
git add -A && git commit -m "<สรุปสั้น ๆ ว่าทำอะไร>"
git push -u origin <branch ที่ session นั้นได้รับมอบหมาย>
```

เกณฑ์ว่า "ก้อนหนึ่ง" คือ — สร้างคาบเรียนเสร็จ 1 คาบ · แกะเอกสารเสร็จ 1 ภาค · เขียนสคริปต์เสร็จ 1 ตัว
**อย่าทำ 3–4 ก้อนแล้วค่อย commit ทีเดียว**

**3. ของสำคัญต้องมีอย่างน้อย 2 ที่**

| ของ | ที่ 1 | ที่ 2 |
|---|---|---|
| เนื้อหาคาบเรียน + พจนานุกรม นล. | artifact (คลาวด์) | repo `artifact/data/` |
| สคริปต์ build ทุกตัว | repo | — |
| ผลแกะเอกสาร (`nl/vis*/`) | repo | — |
| ไฟล์สรุปนี้ | repo | เครื่องผู้ใช้ (ส่งผ่าน SendUserFile) |

**`scratchpad/` = พื้นที่ทำงานชั่วคราวเท่านั้น ห้ามเป็นที่เก็บของสำคัญที่เดียว**

### ของที่ไม่ต้อง commit
ไฟล์ภาพที่เรนเดอร์จาก PDF (`nl/img*/`) — สร้างใหม่ได้ใน 10 วินาที ·
ผล OCR ที่ล้มเหลว · `__pycache__/` · ไฟล์ debug ระหว่างทาง

---

> **เริ่ม session ใหม่:** ถ้า branch ที่ได้รับมอบหมายยังไม่มีงานล่าสุด ให้ `git fetch origin` แล้ว merge
> `origin/claude/add-today-blougl` เข้ามาก่อนทำอะไร · ก่อน publish ให้ `Artifact list scope=files` เทียบขนาดไฟล์กับ
> `artifact/data/` เสมอ ถ้าบนเว็บใหม่กว่า **ห้าม publish ทับ** ให้หา branch ที่ตรงกับเว็บแล้ว merge ก่อน
> (รอบ 25 ก.ย. เกือบทับคาบ Extrapulmonary TB เพราะ branch ที่ใช้อยู่เก่ากว่าเว็บ)

## 1. ตัวงานหลัก

**artifact:** `MED421 learn` — https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE (ปัจจุบัน **Version 16** · มี **7 ชุดวิชา** · 21 คาบ)
เป็นเว็บเรียนเนื้อหา + คลังข้อสอบ MCQ/MEQ/OSCE สำหรับรอบ Internal Medicine
(MED421/422 · 14 ก.ย. – 22 พ.ย. 2569 · รพ.ราชวิถี · สอบลงกอง 17–18 พ.ย.)

**ผู้ใช้:** นักศึกษาแพทย์ปี 4 (nutt.spider@gmail.com)

**ตารางเรียนจริง** (จาก Google Calendar): 44 Lecture · 13 Bedside · 8 Teaching Round

---

## 2. ที่อยู่ไฟล์

```
/home/user/ioioioio/          ← repo · ฉบับล่าสุดอยู่ที่ claude/add-today-blougl = claude/keen-brahmagupta-nqy0my (commit เดียวกัน)
├── artifact/                  ← ต้นฉบับ artifact (publish จากที่นี่)
│   ├── index.html             ← หน้าเว็บ (43 KB)
│   ├── README.md              ← วิธีเพิ่มคาบใหม่ + schema ย่อ
│   ├── data/
│   │   ├── index.json         ← รายชื่อชุดวิชา + ชื่อไฟล์ + จำนวนคาบ
│   │   ├── nl.json            ← พจนานุกรม นล. 1,389 รหัส (472 KB)
│   │   ├── air.json (3 คาบ)   cardio.json (3)  chest.json (4)
│   │   ├── nephro.json (1)    neuro.json (5)
│   │   ├── endo.json (2)
│   │   └── id.json (1)        ← ชุดใหม่ 2 ต.ค. (build_sepsis.py สร้าง entry ใน index.json ให้เองถ้ายังไม่มี)
│   └── tools/                 ← build_acs.py · build_cns.py · build_epilepsy.py · build_eptb.py ·
│                                 build_ihd.py · build_lp.py · build_mets.py · build_rfpleural.py ·
│                                 build_thyroid.py · build_sepsis.py · map_nl.py · refactor.py ·
│                                 verify.py (ทดสอบด้วย Playwright — ต้องผ่านก่อน publish · นับแท็บจาก index.json เอง)
├── nl/                        ← งานแกะเกณฑ์ นล. (เสร็จแล้ว ไม่ต้องทำซ้ำ)
│   ├── vis/056.txt–074.txt    ← ผลอ่านภาค ข. ด้วยสายตา
│   ├── visA/010.txt–047.txt   ← ผลอ่านภาค ก. ด้วยสายตา + _scheme.md (โครงรหัส)
│   ├── nl_partB.json (511)  ·  nl_partA.json (698)
│   ├── build_vis.py · build_visA.py   ← vis*/ → nl_part*.json
│   └── merge_full.py          ← รวมทั้งสองภาคเข้า artifact/data/nl.json + แก้รหัสผิด
├── refs/curriculum-topics-2569.md  ← หัวข้อตามหลักสูตรทางการ
├── slides/SOURCES.md          ← รายการไฟล์สไลด์ที่ได้รับและ Drive file id
├── slides/eptb_notes.md       ← โน้ตอ่านสไลด์ Extrapulmonary TB ทีละหน้า (16 หน้า + ลายมือ)
├── slides/rf_pleural_notes.md · thyroid_notes.md · sepsis_notes.md  ← โน้ตรอบ 2 ต.ค.
└── (ของเดิมคนละสาย: drill.html · learn.html · build.py · data/ · export/)
```

> ⚠️ **ไฟล์ทั้งหมดอยู่ใน repo แล้ว ไม่ได้อยู่ใน `scratchpad/` อีกต่อไป**
> รอบที่แล้ว container ถูกคืนไปจริงและ `scratchpad/` หายทั้งหมด — งานไม่หายเพราะ commit ไว้ครบ
> `NL_syllabus.pdf` และ `nl/img*/` ไม่ได้ commit (โหลด/เรนเดอร์ใหม่ได้)

**แผนรายสัปดาห์เต็ม:** `/root/.claude/plans/google-calendar-humming-dijkstra.md`

---

## 3. โครงสร้างข้อมูล (schema — ต้องทำตามเป๊ะ)

```
lecture: { lec, title, subtitle, objectives[], sections[], meq[], osce[],
           nlGap?, guidelines?[] }
section: { id, title, summary, minutes, nl[], md, pearls[], items[] }
item:    { id, kind:"mcq"|"old", stem, choices[5], answer(0-4), explain,
           pearl, topic, src, ref[], nl[] }
```

**ข้อควรระวัง:**
- markdown parser ในหน้าเว็บ **ไม่รองรับ code fence** (```) — ห้ามใช้ ใช้ตารางแทน
- `answer` เป็น index เริ่มที่ 0
- `id` ห้ามชนกัน รูปแบบ `<SET>-MCQ-nn` และ `<set>-<lec>-nn`

**สูตรเพิ่ม 1 คาบ:** เขียน `build_<ชื่อ>.py` → merge เข้าไฟล์ set → อัปเดต `lectureCount`
ใน `index.json` → `python3 verify.py` → `Artifact publish` ด้วย `url` + `root` + `files`

**ต้นทุน:** 1 คาบเต็มรูปแบบ (10 sections + ~28 MCQ + MEQ + OSCE) ≈ **41k tokens**

---

## 4. คาบที่ทำเสร็จแล้ว 21 คาบ

| set | lec | เรื่อง |
|---|---|---|
| air | 08 | Allergy and clinical immunology |
| air | 23 | Approach to arthritis / crystal and infective |
| air | 33 | Connective tissue disease, vasculitis (18 หัวข้อ — เติมส่วนที่ขาดจากสไลด์ อ.พรรณนิภา ครบแล้ว) |
| cardio | 04 | Inflammatory MyoPericardial Syndrome (IMPS) |
| cardio | 10 | Circulatory Shock |
| cardio | 13 | Ischemic heart disease (CCS→STEMI) ← อ.สุรพันธ์ · พฤ. 24 ก.ย. (เดิมใช้เลข 24/9 — เปลี่ยนเป็นเลขคาบจริงจากคลัง Ward Drill แล้ว · ผูกคลังคาบ 13 ครบ 32 ข้อ ด้วย `tools/link_ihd_bank.py`) |
| cardio | 24 | Atrial fibrillation ← อ.อภิชัย · จ. 5 ต.ค. (11 หัวข้อ · 20 MCQ ใหม่ + คลังคาบ 24 ครบ 21 ข้อ · MEQ AF RVR + warfarin · OSCE counselling warfarin) |
| chest | 03 | Pulmonary tuberculosis |
| chest | 26 | Arterial blood gas analysis |
| chest | 23/9 | Extrapulmonary TB ← อ.ภาณุวัฒน์ (12 หัวข้อ · 33 MCQ · MEQ TB peritonitis · SAQ body fluid) |
| chest | 17 | Respiratory failure + Pleural disease ← อ.สกล (12 หัวข้อ · 36 ข้อ รวมคลังคาบ 17 ครบ · CH-MEQ-03 · CH-OSCE-02/04) |
| nephro | 05 | Fluid electrolyte: Divalent |
| neuro | 07 | Acute ischemic stroke |
| neuro | 23/9 | Epilepsy ← อ.พิมลพรรณ |
| neuro | 15/10 | CNS infection + CSF ← อ.พิมลพรรณ |
| neuro | 9/10 | หัตถการ LP + eye exam ← อ.พิมลพรรณ |
| neuro | 21/10 | Acute confusional state + alteration of consciousness ← อ.พิมลพรรณ |
| endo | 01 | Metabolic syndrome, Obesity, Dyslipidemia ← อ.นวพร (13 หัวข้อ · 35 MCQ · MEQ · OSCE ให้คำปรึกษาลดน้ำหนัก) |
| endo | 14 | Thyroid disorders ← อ.ศิวกร (13 หัวข้อ · 26 MCQ · MEQ Graves · OSCE ตรวจคอ + counselling MMI) |
| id | 25/9 | Septicemia and antibiotic usage ← อ.พจน์ (11 หัวข้อ · 20 MCQ · MEQ obstructive pyelonephritis · OSCE ชั่วโมงแรก) — **อิง SSC 2026 เพราะสไลด์เป็นภาพล้วน** |
| id | 5/10 | AIDS and HIV infection ← พ.ญ.มนัสวี · จ. 5 ต.ค. (13 หัวข้อ · 27 MCQ · MEQ PCP/advanced HIV · OSCE pre-test counselling) — สไลด์ส่วนตาราง (WHO staging, สูตรยา, OI prophylaxis, crypto Rx) เป็นภาพ → อิงแนวทางไทย 2025/WHO และระบุในบทเรียน · ไม่มีข้อในคลัง Ward Drill |

> ⚠️ เลข `lec` แบบวันที่ (เช่น "23/9") เป็นตัวแทนชั่วคราว — **เลขคาบจริงดูได้จากฟิลด์ `lec` ใน `bank_merged.json`** (คลังเดียวกับ Ward Drill)
> ถ้าคาบนั้นมีข้อในคลัง ให้ใช้เลขนั้นและผูกข้อด้วย `artifact/tools/link_bank.py` (ดูตัวอย่าง `link_ihd_bank.py` และท้าย `build_af.py`)

**ความครอบคลุมคลัง Ward Drill (5 ต.ค.)** — ผูกเข้าบทเรียนแล้ว **293/570 ข้อ**: AIR 110/110 · Cardio 97/180 · Chest 64/106 · Nephro 22/174 (Mock 200 ข้อไม่ผูกคาบ) ·
คาบในคลังที่ยังไม่มีบทเรียน: Cardio 27 Rheumatic/Valvular · 36 Arrhythmia/EKG · 39 HT/HF · Chest 21 CXR/Occupational · 37 Pneumonia/Asthma/COPD · Nephro 14, 19, 22, 28, 30, 42

---

## 5. พจนานุกรม นล. (สถานะปัจจุบัน)

`build/data/nl.json` = **1,389 รหัส · 472 KB** — ✅ **ครบทั้งเล่ม ฉบับ พ.ศ. 2567**

| ภาค | รหัส | ที่มา |
|---|---|---|
| ก. วิทยาศาสตร์การแพทย์พื้นฐาน (B1–B11) | 854 (รายการจริง 698 + หัวข้อหมวด 156) | หน้า 6–47 |
| ข. ความรู้ความสามารถทางวิชาชีพฯ | 535 (511 + หัวข้อหมวด 24) | หน้า 56–74 |

จำนวนรายการจริงภาค ก. แยกตามระบบ:
B1=143 · B2=53 · B3=93 · B4=54 · B5=40 · B6=46 · B7=47 · B8=52 · B9=35 · B10=68 · B11=67

ทุกรายการมี `code`, `part`, `section`, `system`, `group`, `title`, `page`, `source`

**ระบบรหัส:**
- ภาค ก.: `BX.1` โครงสร้าง/หน้าที่ (`.1.1` Structures · `.1.2` Functions · `.1.3` การเปลี่ยนแปลงตามช่วงชีวิต)
  `BX.2` สาเหตุ/พยาธิ/การวินิจฉัย → `.2.1` hereditary/congenital · `.2.2` infectious/inflammatory/immunologic ·
  `.2.3` traumatic/mechanical · `.2.4` neoplastic · `.2.5` metabolic/regulatory · `.2.6` vascular ·
  `BX.3` การสืบค้นโรค · `BX.4` ยาสมเหตุผล — ตารางแยก **ซ้าย = กลุ่มที่ 1 และ 2** / **ขวา = กลุ่มที่ 3** (`-3(n)`)
  (รายละเอียดเต็มที่ `nl/visA/_scheme.md`)
- ภาค ข.: `2.1.x` อาการสำคัญ (84) · `2.2.x` ภาวะฉุกเฉิน (50) ·
  `2.3.<ระบบ>(n)` โรคตามระบบ **กลุ่ม 2 = ดูแลเองได้** · `2.3.<ระบบ>-3(n)` **กลุ่ม 3 = วินิจฉัยแล้วส่งต่อ** ·
  `3.1/3.2/3.3` การตรวจ (52)

**วิธีแกะที่ใช้ได้จริง:** เรนเดอร์หน้าเป็น PNG 200 dpi แล้ว **อ่านด้วยสายตา** (Read tool)
→ แม่น 100% · ต้นทุน ~3.8k tokens/หน้า
**วิธีที่ล้มเหลว (อย่าทำซ้ำ):** tesseract OCR — ลอง 3 แบบ ได้ดีสุด 71% แย่สุด 37% ใช้ไม่ได้

### รหัสที่ไฟล์เดิมใส่ผิดและแก้ไปแล้ว
| รหัสเดิม | ควรเป็น | แก้กี่จุด |
|---|---|---|
| `2.3.4(20)` Tuberculosis | `2.3.1(20)` | 38 |
| `2.3.12(12)` Urticaria | `2.3.12(14)` | 5 |
| `2.3.12(13)` SJS/TEN | `2.2.49` | 5 |
| `B5.2.2-3(2b)` Vasculitis | `B5.2.2-3(6)` | 10 |
| `B5.2.2-3(3b)` Osteomyelitis | `B5.2.2-3(7)` | 5 |

### ข้อผิดพลาดในตัวเอกสารแพทยสภาที่พบ (บันทึกไว้ใน title)
- `B1.6.4` ถูกใช้ซ้ำสองหัวข้อ (Neoplasm และ Adaptation to environmental extremes) → เก็บอันหลังเป็น `B1.6.5`
- `B5.2.2` กลุ่ม 3 นับ (1)–(5) จบหน้า 27 แล้วขึ้นหน้า 28 **เริ่มนับใหม่ที่ (2)** → เรียงต่อเป็น (6)(7)(8)
  (ตรวจซ้ำด้วยการ crop ภาพที่ 400 dpi แล้ว ยืนยันว่าเอกสารพิมพ์แบบนั้นจริง)
- `B11.2.6` พิมพ์เป็น `11.2.6` ขาด B
- หัวข้อ 2.2 เขียนว่า "49 รายการ" แต่เลขไล่ถึง 2.2.50

ตรวจแล้ว: รหัสที่ 13 คาบอ้างถึง 136 รหัส → พบในพจนานุกรมครบ 136 ไม่มีรหัสลอย · ทุก build_*.py assert รหัสกับ nl.json ก่อนเขียน
(รอบ 2 ต.ค. พบรหัสผิดในคลัง: `2.3.5-3(1)` = bipolar ถูกใส่ในข้อมะเร็งปอด → build_rfpleural.py ตัดทิ้ง)

---

## 6. ไฟล์สไลด์ที่ได้รับแล้ว

**พ.ญ.มนัสวี** — AIDS and HIV infection ✅ Drive `13PhGovTDoDXERCeB2zfMC1_1nZq2mAlJ` (25 MB) · ข้อความดึงได้เฉพาะสไลด์ตัวอักษร · โน้ต `slides/hiv_notes.md`

**อ.อภิชัย ปกวัฒนา** — Atrial fibrillation (update 16 Nov 2025) ✅ Drive `1zK9eofxHl5ldCi-5IqIjyTStGVHYhlRO` · ดึงข้อความด้วย `read_file_content` ได้ครบ · โน้ต `slides/af_notes.md`

**อ.ภาณุวัฒน์ (Panuwat Wongkulab)** — Extrapulmonary TB: The Hidden Pathogen (Apr 2026) ✅
- ผู้ใช้อัปโหลดในแชทเป็น PDF ภาพล้วน 16 หน้า (ไม่อยู่ใน Drive) → อ่านด้วยสายตา โน้ตเต็มที่ `slides/eptb_notes.md`
- ⚠️ ไฟล์ bank `CH-MCQ-20` และ `CH-OSCE-04` (pleural/ADA) ของคาบ 17 อ.สกล ยังว่าง — ตั้งใจไม่ใช้ในคาบ EPTB เพื่อเก็บไว้ให้คาบเยื่อหุ้มปอด

**อ.พิมลพรรณ** (เจ้าของ paranee.k@rsu.ac.th) — ✅ **ใช้ครบทั้ง 4 ไฟล์แล้ว**
- Epilepsy `1tWDtfQ-ZA-tDDR1_YgGkYgyS-4md6hQ5` ✅
- CNS infection `1dnFAWEZRkkzF7MgbJ487vU1Jv9pNZHjp` ✅
- LP + eye exam `13UzOj8-vMSv_P3cQqg06033ws9NV9w2l` ✅
- Acute Confusional State `1JtJeNHGY-Fls5CiGvIpwx2lp8FfUIi8g` ✅ (W6 · 21 ต.ค.)

**อ.สุรพันธ์ พงศ์สุธนะ** (Cardiology) — รวมเป็นคาบเดียวแล้ว ✅
- CAD complete2019 `1Pcst0l92BATWKClV00umsyNQXgdFvD4k` (ยังไม่ได้อ่าน — สำรองไว้)
- Chronic coronary syndrome 2019 `1BqP50Nbbuw2BszsHKNoDnLeFlA4eoPWJ`
- NSTEMI 2020 `17iNJA1PvpedUAz8wyM4CzZBU1MAy1EdI`
- STEMI2017 `1j-EtRG61awYlCMKRx-q9MKymdhYF2BAA`

**อ.นวพร นภาทิวาอำนวย** (Diabetes & Metabolism) — ✅ ใช้แล้ว (ชุด Endo คาบ 01)
- Lec 1 2026 MS, obesity, DLP Handout `1ttUNtkD5EXmVXVIhKuScn4Y6wOV9-yQe` (15 MB · อยู่ใน Drive ผู้ใช้เอง)
  ⚠️ `read_file_content` ได้ข้อความถึงสไลด์ DLCN แล้วหยุด — ส่วนรักษา dyslipidemia ดึงไม่ได้
  ดาวน์โหลดตรงก็ไม่ได้ (proxy 403) → หัวข้อ 11–13 ของคาบนี้ใช้ ESC/EAS 2019 แทนและระบุไว้ใน `nlGap`
  ถ้าผู้ใช้ส่งภาพสไลด์ส่วนนั้นมา ให้เทียบแล้วแก้ `build_mets.py`

**รอบ 2 ต.ค. (โฟลเดอร์ Drive "Claude" `1mft-8EhUVLSAXIwVX7zV6JmHoiaBPzsM` ของผู้ใช้)** — ✅ v14
- Lec12 Respiratory failure, pleural disease `12_uIP-b1TWP-u35yfm90Q9PT5QTNgPvp` → chest คาบ **17** (ใช้เลขคาบตามคลังข้อสอบ ไม่ใช่ "Lec12")
  ⚠️ ข้อความถูกตัดหลัง work up pleural effusion → Light's/empyema/malignant/การรักษา PTX ไม่ tension ใช้ BTS 2023
- Lec14 Thyroid disorder_2026 `1iq1YOO-vf-JF3vL40p1ppCmu-1eHnII5` → endo คาบ **14**
  ⚠️ ข้อความถูกตัดหลัง nodule algorithm → hypothyroid/amiodarone/Bethesda เทียบจาก artifact บทเรียน Thyroid ของผู้ใช้
  (claude.ai/artifact/S9FmtzVewjtqtWxnuNQxRu — ทำจากสไลด์ชุดเดียวกันใน session อื่น) · thyroid storm ใช้ ATA/JTA 2016
- Sepsis _ Principle ATB `10qgsfnxQl7wacVkNBSAF5SXe8Bx4vPDc` (175 MB **ภาพล้วน** · read_file_content ว่าง) → id คาบ 25/9
  ใช้ SSC 2026 (ตรวจกับ sccm.org แล้ว) + artifact Sepsis ของผู้ใช้ (claude.ai/artifact/DB59ZbY5ize8MhxXiHkZJZ) · **ถ้าได้ภาพสไลด์มาให้แก้ build_sepsis.py**
- Lec7 Epilepsy `1stF_hQlkx8nCxnE07W3lKHCBsT5alFhW` = สไลด์ชุดเดียวกับคาบ Epilepsy ที่ทำแล้ว (มีลายมือ) → ไม่สร้างซ้ำ
- ผู้ใช้มี artifact บทเรียนแยกต่อหัวข้อใน "ห้องสมุดท่าอาจารย์" (claude.ai/artifact/QebhLmV2eKyzj3mkqstnjR) — ใช้เป็นแหล่งเทียบได้เมื่อสไลด์ดึงไม่ครบ
- ตำแหน่งเฉลย: build ใหม่ทั้งสามสลับตัวเลือกแบบคงที่ด้วย random.Random(id) — คลังเดิม (CH-MCQ/CH-OLD) เฉลย ก. ทุกข้อ

**เข้าไม่ถึง (น่าจะอยู่บัญชี @rsu.ac.th):**
- UTI `1GG55VJ6ddTMQ2IETf1IqUpU_tMDizEH7`
- Tropical disease `1ax8FzPhmAZ4iFSSsXGQcb5TGobcG4nn9` (ผู้ใช้สั่งข้าม Malaria ไปก่อน)

**NL Syllabus** `143DRB8wSwIfDvji6OfC--FRIUitv7kbm` → โหลดมาแล้วที่ `nl/NL_syllabus.pdf`

---

## 7. งานที่ค้าง (เรียงตามลำดับที่ตกลงกันไว้)

1. W1: UTI (รอไฟล์) · Malaria (ผู้ใช้สั่งพัก)
2. W2 เหลือ: Skin infections · Nephrotic/Nephritis — ✅ Extrapulmonary TB (v12) · ✅ Dyslipidemia/MetS/Obesity (v13) ·
   ✅ Septicemia (v14 · อิง SSC 2026 รอภาพสไลด์จริง) · ✅ Pleural/Resp failure (v14) · ✅ Thyroid (v14)
3. W10 แท็บ "ทบทวนก่อนสอบ" (~50k tokens)

> ✅ **งานเกณฑ์ นล. เสร็จสมบูรณ์แล้ว** ไม่ต้องอ่าน PDF ซ้ำอีก
> ✅ **สไลด์ของ อ.พิมลพรรณ ใช้ครบทุกไฟล์แล้ว** — คาบที่เหลือรอสไลด์จากอาจารย์ท่านอื่น

**เสนอไว้แต่ยังไม่ได้ทำ:** อ่าน CAD complete2019 เพิ่มรายละเอียด · ใส่ `guidelines` ให้ 9 คาบแรก ·
เพิ่มหัวข้อ status epilepticus ในคาบ Epilepsy

---

## 8. คำสั่ง/ข้อตกลงจากผู้ใช้ที่ยังมีผล

- **ประเมิน token ทุกครั้ง** ที่จะสร้างของใหม่
- เนื้อหา **เต็มรูปแบบทุกคาบ** (ไม่ย่อ)
- **ไม่ยุบรวม** artifact เก่า 5 อัน ปล่อยแยกไว้
- ทุกคาบต้องมีป้ายว่า **ครอบคลุมจุดประสงค์ นล.** · ถ้าหัวข้อไหนไม่มีรหัส นล.
  ให้หา **guideline ปัจจุบัน** มาทำเป็นสื่อการสอนแทน (ใส่ใน `nlGap` + `guidelines[]`)
- ใช้ `MED421 learn` เป็น artifact หลักเสมอ

---

## 9. รายละเอียดทางเทคนิคที่เคยติดปัญหา

- **Playwright:** container ใหม่ยังไม่มีโมดูลติดตั้ง — ต้อง `pip install --break-system-packages playwright` ก่อน (เบราว์เซอร์มีอยู่แล้ว
  ห้ามรัน `playwright install`) · ต้องระบุ `executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"`
  และ `args=["--no-sandbox"]` · Google Fonts โดน proxy บล็อก (ERR_CERT_AUTHORITY_INVALID หรือ ERR_TUNNEL_CONNECTION_FAILED — verify.py กรองทั้งสองแบบแล้ว)
  เป็นเรื่องปกติของ container ไม่ใช่บั๊ก
- **อย่าใช้ `pgrep -f <script>` ในลูปรอ** — มันแมตช์ตัว bash command เองแล้วค้างตลอดกาล
- แถบความคืบหน้านับเฉพาะ set ที่เปิดอยู่ (AIR = 34 ไม่ใช่ 91) — เคยเข้าใจผิดว่าเป็นบั๊ก
- `.nav .btn` เคยล้นจอที่ 390px เพราะ `white-space:nowrap` → แก้แล้วด้วย
  `white-space:normal;text-align:left;max-width:100%`
- สีป้ายกลุ่ม 2/3 ใช้ตัวแปร `--ok/--ok-soft` และ `--miss/--miss-soft` ที่มีอยู่แล้ว
  จึงถูกต้องทั้งโหมดสว่างและมืดโดยอัตโนมัติ
