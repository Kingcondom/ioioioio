# ข้อสอบที่เป็นรูป — โพย MED35

ที่มา: Google Doc "MED Y4 | Pastpapers and review from MD35 (RJ)" (ภาพ 77 รูป · ส่วนใหญ่เป็นสกรีนช็อตข้อความ LMS ที่มีในคลังอยู่แล้ว)
คัดเฉพาะข้อที่ **ภาพเป็นส่วนหนึ่งของโจทย์** ได้ 24 ข้อ (MCQ 18 + SAQ 6) — Ward Drill Version 25

| ไฟล์ | หน้าที่ |
|---|---|
| `items_med35.py` | เนื้อข้อสอบ (MCQ เขียนคำตอบถูกไว้ choices[0]) |
| `patch_drill.py` | ย่อ/ครอปรูป → `img/` แล้วแพตช์หน้าเว็บที่ publish อยู่ (ใส่ข้อ + รองรับฟิลด์ `img` + แท็บ "ข้อสอบมีรูป") — รันซ้ำได้ |
| `img/` | รูปที่ publish ไว้ที่ `pic/` ข้างหน้าเว็บ |

อัปเดตรอบหน้า: `Artifact read` หน้าเว็บ → `python3 pic35/patch_drill.py <live.html> ward_drill/index.html <โฟลเดอร์รูปจาก Doc>`
→ publish `ward_drill/index.html` ไปที่ https://claude.ai/artifact/Fdi5gcNXKqFLAXg4fQBV7X พร้อม `files` = `pic/*.jpg` ← `pic35/img/*.jpg`

ข้อที่ไม่ได้ใส่: สไลด์ ABG ข้อ 32 (เป็นข้อความในรูป และตัวเลข pH ไม่สอดคล้องกับ Henderson–Hasselbalch) ·
EKG hyperK และ PBS thrombocytopenia ใน FA SAQ (ในโพยไม่มีรูป)

## แท็บ "ข้อสอบแยกปี" (Version 26)
`python3 ward_drill/patch_years.py ward_drill/index.html` — รวมข้อทุกระบบที่มีฟิลด์ `years` ตามปี MED28–MED35 (ไม่เพิ่มข้อใหม่)
กรองได้ตาม Part และที่มา (คลังข้อสอบเก่า / ข้อใหม่ที่อิงปีนั้น) · แสดงทีละ 60 ข้อ · ลิงก์ตรง `#year-35`
ถ้า republish จากหน้าเว็บสดใหม่ ให้รัน `pic35/patch_drill.py` ก่อน แล้วค่อย `patch_years.py`

## สุ่มทำข้อสอบ "ระบบละ 5 ข้อ" (Version 30)
`python3 ward_drill/patch_quiz5.py ward_drill/index.html` — เพิ่มขอบเขตในโหมดสุ่ม: สุ่ม 5 ข้อจากทุกระบบ ยกเว้น Mock NL (11 ระบบ = 55 ข้อ) เรียงตามระบบ
หมายเหตุ: Version 30 แพตช์ต่อจากหน้าเว็บสด 1793895436-5a3e (มีข้อ AIR-ART จาก session อื่น) — `ward_drill/index.html` ใน repo ตรงกับเว็บแล้ว

## สุ่ม: "คลังข้อสอบเก่าก่อน" (Version 31)
`python3 ward_drill/patch_quiz_prio.py ward_drill/index.html` (รันหลัง patch_quiz5.py) — แถบ "เลือกข้อจาก" ในโหมดสุ่ม:
คลังข้อสอบเก่าก่อน (ค่าเริ่มต้น) = สุ่มจากข้อสอบเก่าให้ครบก่อน ไม่พอจึงเติมข้อใหม่ · คละเก่ากับใหม่ = แบบเดิม · ข้อใหม่ในชุดสุ่มติดป้าย "ข้อใหม่"

## คาบที่ทวนแล้ว: สุ่มข้อสอบของแต่ละวัน (Version 35)
`python3 ward_drill/patch_rvquiz.py ward_drill/index.html` — ปุ่ม "สุ่มข้อสอบ" ในหัวของแต่ละวัน · ตั้งปีที่ออก (ทุกปี/3/5 ปีล่าสุด/เลือกเอง + ข้อฝึกเพิ่ม), Part, จำนวนข้อต่อคาบ
ข้อสอบเก่าก่อนข้อฝึกเพิ่ม · ชุดและคำตอบในชุดเก็บใน localStorage `med421-drill-rvquiz` · ฐานคือเว็บสด 1794212683-65c3 (มีปุ่ม "ถาม AI" + capability sample จาก session อื่น)

## ปุ่มโหมดสี (Version 36)
`python3 ward_drill/patch_theme.py ward_drill/index.html` — อัตโนมัติ / สว่าง / มืด ที่หัวหน้า · ตั้ง `data-theme` บน `<html>` (CSS มีชุดสีมืดอยู่แล้ว) · เก็บใน localStorage `med421-drill-theme`
