# HANDOFF — สถานะโปรเจกต์ MED421 study kit

อัปเดตล่าสุด: 2026-09-19 · branch `claude/lecture-artifact-integration-5plhhc` · commit ล่าสุด `0c5dde0`

---

## 1. โปรเจกต์นี้คืออะไร

ชุดเครื่องมืออ่านหนังสือสำหรับ **MED421/422 อายุรศาสตร์** ประกอบด้วยสองเว็บที่ build จาก JSON ไฟล์เดียวจบ เปิดออฟไลน์ได้

```
config.json  +  data/*.json   --build.py-------->  bank_merged.json  +  drill.html
learn/<set>.json              --build_learn.py-->  learn.html  +  export/learn_<set>.md
```

- **`drill.html`** — คลังข้อสอบ ฝนคำตอบ มีแท็บ "MEQ/OSCE ตามปี" และ "ออกบ่อย"
- **`learn.html`** — เว็บเรียนเนื้อหา บทเรียนภาษาไทย + ข้อสอบเช็คความเข้าใจท้ายทุกหัวข้อ (ผูกกับข้อในคลังด้วย id)
- **`COVERAGE.md`** — ตารางรายสัปดาห์: เรียน lecture อะไรไปแล้ว และคาบไหนยังไม่มีข้อในคลัง (routine อัปเดตทุกเสาร์)
- **`SPEC.md`** — สัญญาของโปรเจกต์ อ่านก่อนแก้อะไรก็ตาม (schema, ข้อตกลง, ตารางความคืบหน้า, open items)
- **`check_numbers.py`** — ตรวจเลขคณิต ABG / Winter's / Light's criteria ในข้อสอบ

### Artifact ที่ publish แล้ว
| หน้า | ลิงก์ |
|---|---|
| **drill.html** (Version 9) | https://claude.ai/artifact/Fdi5gcNXKqFLAXg4fQBV7X |
| **learn.html** (Version 1) | https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE |

> อัปเดต artifact เดิมด้วยการส่ง `url` นั้นเข้าไป — ถ้า publish เฉย ๆ จะได้ artifact ใหม่คนละอัน

> **หน้าหลัก (ตั้งไว้ 25 ก.ย. 2569): drill.html = `Fdi5gcNXKqFLAXg4fQBV7X`** — build ใหม่ทุกครั้งให้ republish ด้วย `url` นี้เท่านั้น
> - ลิงก์เก่า `https://claude.ai/code/artifact/69931ac7-6ac2-4b0a-b4f3-41b7f4aff86d` (คิท 5 ระบบจาก main / `claude/med-exam-pipeline-kit-g3zgv1`) **เลิกใช้แล้ว** อย่า publish ทับหรือต่อยอดจากตัวนั้น
> - โค้ดต้นทางของหน้าหลักคือ branch นี้ (`claude/lecture-artifact-integration-5plhhc` และ `claude/adoring-babbage-zkg8ih` ที่ต่อจากมัน) ไม่ใช่ main

---

## 2. สถานะคลังข้อสอบ — 1,318 ข้อ

| ระบบ | MCQ ใหม่ | MEQ/OSCE | ข้อสอบเก่า | รวม |
|---|---|---|---|---|
| cardio | 40 | 10 | 130 | **180** |
| nephro | 40 | 10 | 124 | **174** |
| chest | 40 | 10 | 58 | **108** |
| neuro | 40 | 10 | 78 | **128** |
| air (ภูมิ/รูมาโต) | 50 | 10 | 56 | **116** |
| infect | 24 | 6 | 42 | **72** |
| gi | 21 | 4 | 43 | **68** |
| endo | 21 | 4 | 53 | **78** |
| heme | 21 | 4 | 47 | **72** |
| derm | 14 | 2 | 48 | **64** |
| onco | 12 | 2 | 44 | **58** |
| mock | 200 | — | — | **200** |

**ข้อสอบเก่าแยกตามรุ่น** (จาก tag ใน `src`): MED28 23 · MED29 16 · MED30 80 · MED31 247 · MED32 152 · MED33 86 · MED34 152 · MED35 112

---

## 3. สถานะบทเรียน — 9 คาบ / 91 หัวข้อ / ข้อเช็คความเข้าใจ 253 ข้อ

| ไฟล์ | คาบ | หัวข้อ | หัวข้อย่อย |
|---|---|---|---|
| `learn/air.json` | 08 | Allergy and clinical immunology | 9 |
| | 23 | Approach to arthritis / crystal and infective arthropathy | 9 |
| | 33 | Connective tissue disease, vasculitis and inflammatory arthritis | 16 |
| `learn/cardio.json` | 04 | Inflammatory MyoPericardial Syndrome (IMPS) | 12 |
| | **10** | **Circulatory Shock** | 8 |
| `learn/chest.json` | 03 | Pulmonary tuberculosis | 9 |
| | 26 | Arterial blood gas analysis | 6 |
| `learn/nephro.json` | 05 | Fluid electrolyte: Divalent (Ca, PO4, Mg) | 12 |
| `learn/neuro.json` | **07** | **Acute ischemic stroke** | 10 |

**ยังไม่มีบทเรียนเลย**: infect · gi · endo · heme · derm · onco

---

## 4. งานที่ค้างอยู่ตอนนี้ (สำคัญที่สุดสำหรับแชทถัดไป)

### บทเรียน Neuro กลุ่ม N02 — เขียนไป 9 จาก 13 หัวข้อ

Neuro มีข้อสอบ 128 ข้อ แต่มีบทเรียนแค่คาบ 07 (stroke) เท่านั้น อีก **78 ข้อในกลุ่ม `N02`** ยังไม่มีบทเรียนรองรับ

**งานที่เขียนไว้แล้วเก็บอยู่ที่ `attic/wip_neuro_n02_sections.json`** (9 หัวข้อ ผูกข้อสอบไป 53 ข้อ) — ยังไม่ได้ผนวกเข้า `learn/neuro.json` และยังไม่ผ่าน build

หัวข้อที่เขียนเสร็จแล้ว:
1. `neuro-n02-01` ผู้ป่วยไม่รู้สึกตัว — GCS, ม่านตา, สาเหตุ (7 ข้อ)
2. `neuro-n02-02` ระบุตำแหน่งรอยโรคจากข้างเตียง — ลานสายตา, aphasia, facial palsy (4 ข้อ)
3. `neuro-n02-03` ปวดศีรษะ — tension/migraine/cluster + red flags (4 ข้อ)
4. `neuro-n02-04` เลือดออกในสมองและใต้เยื่อหุ้มสมอง — SAH/ICH (5 ข้อ)
5. `neuro-n02-05` ชักและภาวะชักต่อเนื่อง (9 ข้อ)
6. `neuro-n02-06` เยื่อหุ้มสมองอักเสบจากแบคทีเรีย (6 ข้อ)
7. `neuro-n02-07` น้ำไขสันหลัง — อ่านผลและข้อห้ามเจาะหลัง (9 ข้อ)
8. `neuro-n02-08` สมองอักเสบจากเริม (5 ข้อ)
9. `neuro-n02-09` เวียนศีรษะ — ส่วนกลาง vs ส่วนปลาย (4 ข้อ)

**อีก 4 หัวข้อที่ยังไม่ได้เขียน** (25 ข้อที่เหลือ):

| id | หัวข้อ | ข้อสอบที่ต้องผูก |
|---|---|---|
| `neuro-n02-10` | เพ้อ สมองเสื่อม และภาวะที่รักษาได้ (delirium, Alzheimer, NPH, Wernicke, alcohol withdrawal) | NEU-MCQ-38, NEU-OLDP-064, 069, 070, 071, 072, 022, 057, 060 |
| `neuro-n02-11` | โรคระบบประสาทส่วนปลายและรอยต่อประสาทกล้ามเนื้อ (GBS, MG, myopathy, neuropathy, Morton neuroma) | NEU-MCQ-31, NEU-MCQ-32, NEU-OLDP-045, 019, 031, 052, 046, 025, 062, 021 |
| `neuro-n02-12` | ไขสันหลังและรากประสาทถูกกด (cord compression, cauda equina) | NEU-MCQ-33, NEU-MCQ-34, NEU-OLDP-020 |
| `neuro-n02-13` | การเคลื่อนไหวผิดปกติ (dystonia, tardive dyskinesia, restless legs) | NEU-OLDP-024, 026, 023 |

**ขั้นตอนปิดงาน**: เขียน 4 หัวข้อที่เหลือ → รวมทั้ง 13 หัวข้อเป็น lecture entry `N02` ใน `learn/neuro.json` (ใส่ `meq: [NEU-MEQ-02..05]`, `osce: [NEU-OSCE-02..05]`) → `python3 build_learn.py` → publish ทับ artifact `5jjGrfPjyBgP7wzxcu8TcE` → commit + push

---

## 5. กฎที่ห้ามผิด

### Schema ข้อสอบใหม่ (SPEC §3.1)
- `"answer": 0` **เสมอ** และวางตัวเลือกที่ถูกไว้ที่ `choices[0]` — `build.py` สลับตำแหน่งให้เองแบบ deterministic ต่อ set
- ตัวเลือก **5 ตัว ไม่ซ้ำกัน** และทุกตัวต้องน่าเชื่อพอที่นักเรียนเก่งจะเลือกผิดได้จริง
- `note`/`explain` เป็นภาษาไทย เดินกลไกก่อน แล้วค่อยบอกว่าทำไมตัวลวงแต่ละตัวผิด
- `nl` ต้องเป็นรหัสที่มีจริงใน `refs/nl_2567.json` เท่านั้น

### Schema คลังข้อสอบเก่า (SPEC §3.3)
`{id, lec, lecture, q, choices, answer, note, src}` — `src` ต้องขึ้นต้นด้วย tag รุ่น (`MED31 · MED34`) แล้วตามด้วยข้อความโพยดิบ โดยแต่ละท่อนนำหน้าด้วย `[MEDxx]` เพราะ `build.py` ขุด tag พวกนี้ไปทำแท็บ "ตามปี" และ "ออกบ่อย" (HOT_MIN=2)

### ด่านตรวจ 4 ข้อของข้อสอบเก่า (SPEC §6.1)
ทุกข้อที่จะเข้าคลังต้องผ่านครบทั้งสี่ — **faithful** (เฉลยตรงกับที่โพยบันทึกจริง โจทย์ไม่งอกรายละเอียดทางคลินิกที่โพยไม่ได้บันทึก) · **provenance_ok** (ทุก tag `MEDxx` มีหลักฐาน `[MEDxx]` จริง) · **schema_ok** · **medically_sound** (ถ้าเฉลยโพยล้าสมัย ต้องเขียนกำกับใน note)

> **ไม่แน่ใจ = ตก** ข้อผิดในคลังอันตรายกว่าข้อที่หายไป

### ห้ามเด็ดขาด
- **ห้ามเดาเลขคาบ** ถ้าไม่มี `MED421-422_Lecture_List.txt` — ใช้ placeholder ไปก่อน
- **ห้ามแต่งรหัส NL หรือเลขหน้าอ้างอิง**
- **ห้ามเอาข้อที่ยังไม่ผ่านด่านตรวจเข้าคลัง** แม้จะอยากให้งานคืบ

---

## 6. ของที่ parked ไว้ (ยังไม่เข้าคลัง)

- **`data/_held_unverified_papers.json` — 456 ข้อ** ที่ reconstruct แล้วแต่ไม่ผ่านด่านตรวจ ไฟล์นี้ **ไม่ได้ถูกอ้างใน `config.json` และ `build.py` ไม่อ่าน** มี `_warning` กำกับไว้ในไฟล์
- ยังไม่ได้ทำ: slice s4 (Nephro + Chest + AIR, 240 ข้อ) และกลุ่มที่ระบุระบบไม่ได้ (43 ข้อ) — ยังไม่เคย reconstruct
- 98 ข้อที่ parked ในระบบที่ข้อเยอะอยู่แล้ว (cardio 70, chest 10, nephro 6, derm 5, air 5, onco 2) — คุ้มค่าน้อย
- onco มีข้อซ้ำ 2 ข้อ (เก็บ 46 แต่ unique 44) ยังไม่ได้แก้

---

## 7. Open items ใน SPEC.md

1. ยืนยันเลขคาบของ Neuro (ตอนนี้ใช้ `07` ยังไม่ได้ยืนยัน) และวันที่จริงของ AIR 08/23/33 กับ Neuro 07
2. แทนที่ placeholder เลขคาบของ 6 ระบบใหม่ (infect/gi/endo/heme/derm/onco) เมื่อได้ `MED421-422_Lecture_List.txt`
3. เติมรหัส NL ของระบบประสาทที่ขาดจากประกาศแพทยสภาฉบับจริง — ตอนนี้ `refs/nl_2567.json` มีแค่ `2.3.6` (ทั้งหมวด) กับ `2.3.9-3(3)` ไม่มีรหัสย่อยของชัก ปวดศีรษะ สมองเสื่อม
4. ข้อสอบเก่าไม่มีรหัส `nl` เลย — `build.py` เตือนอยู่
5. แท็บ "ตามปี" และ "ออกบ่อย" ยังว่างสำหรับ Neuro/ID/GI/Endo/Heme/Derm/Onco/Mock

---

## 8. ข้อตกลงเรื่อง git

- พัฒนาและ push บน **`claude/lecture-artifact-integration-5plhhc`** เท่านั้น
- `git push -u origin claude/lecture-artifact-integration-5plhhc` — ถ้าพังเพราะเน็ต retry 4 ครั้ง (2s, 4s, 8s, 16s)
- **ห้ามเปิด pull request** เว้นแต่สั่งชัดเจน
- ทุก commit ปิดท้ายด้วย
  ```
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0124sY9c9oECUaV1Pi3xE74h
  ```
- ห้ามใส่ชื่อ/รหัสโมเดลใน commit message, PR, code comment หรือไฟล์ใด ๆ ในรีโป

---

## 9. ประวัติ commit ของรอบนี้

| commit | เนื้อหา |
|---|---|
| `c0119be` | ข้อสอบเก่าชุดแรกที่ผ่านการตรวจ 31 ข้อ |
| `6f4fc68` | บันทึกการ ingest โพย MED28–MED35 ลง SPEC §6.1 |
| `eb922ed` | Derm/Onco 102 ข้อ |
| `e297bb6` | park 456 ข้อที่ไม่ผ่านการตรวจไว้นอก build |
| `6d8645f` | Neuro 78 ข้อ (ผ่าน 78 จาก 88) |
| `50ed434` | อีก 5 ระบบ 263 ข้อ (ผ่าน 263 จาก 358 = 73%) |
| `0c5dde0` | ปรับ `learn.html` ให้ใช้ design system เดียวกับ `drill.html` + publish artifact |
