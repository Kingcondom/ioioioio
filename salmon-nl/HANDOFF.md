# Salmon NL — สถานะงาน (อัปเดต 7 ต.ค. 2569)

เว็บเรียน NL2 Medicine จากสไลด์ **MedSalmon ติว NL by พี่ซี** (โฟลเดอร์ Drive "Medicine - ณัฐพัชร์ พัฒนพงษ์กวิน", เจ้าของ medsalmon2021@gmail.com — ผู้ใช้มีสิทธิ์ดูอย่างเดียว)

- **artifact:** Salmon NL — https://claude.ai/artifact/EL8HrvUJawWYs1rr25qzGK
- **repo:** `Kingcondom/ioioioio` branch `claude/salmon-nl` โฟลเดอร์ `salmon-nl/`
- หน้าตาและเอนจินดัดแปลงจาก MED421 learn (`artifact/index.html` ของ branch learn) + เพิ่ม **ภาพ SVG ในหัวข้อ** (`figs` + บรรทัด `[[fig:id]]`) และแท็บ **สุ่มข้อสอบ**
- ความคืบหน้าผู้ใช้เก็บใน localStorage key `salmon-nl-v1` (คำตอบเก็บเป็น index → **ห้ามสลับตำแหน่งคำตอบของข้อที่ขึ้นเว็บแล้ว**)

## ชุดที่เสร็จแล้ว (11 ชุด · 340 หัวข้อ · 1,306 ข้อ · 210 ภาพ)

| set | deck | หมวด | หัวข้อ | ข้อ | ภาพ |
|---|---|---|---|---|---|
| cardio | NL2-Cardio | 6 | 28 | 108 | 21 |
| resp | NL2-Respiratory | 7 | 26 | 113 | 16 |
| gi | NL2-GI | 8 | 29 | 104 | 23 |
| nephro | NL2-Nephro | 9 | 34 | 127 | 24 |
| endo | NL2-Endocrine | 7 | 26 | 118 | 18 |
| hemato | NL2-Hemato | 10 | 37 | 144 | 20 |
| id | NL2-Infectious (Completed) | 9 | 31 | 115 | 18 |
| neuro | NL2-Neuro | 11 | 38 | 162 | 19 |
| rheum | NL2-Rheumato | 6 | 22 | 87 | 15 |
| derm | NL2-Dermato | 10 | 41 | 151 | 29 |
| exam25 | Update ข้อสอบ 2025 NL2-Medicine | 10 ระบบ | 28 | 77 | 7 |

ข้อที่ `kind="old"` = ข้อสอบตัวอย่างในสไลด์ที่เรียบเรียงใหม่ · ข้อสงสัย/จุดที่แก้ตัวเลข/สไลด์ที่เป็นภาพ อยู่ใน `notes/<set>_notes.md` และในคำอธิบายข้อนั้น ๆ

## วิธีแก้/เพิ่มเนื้อหา

1. แก้ `parts/<set>/<lec>.py` (เขียนด้วย helper ใน `tools/lib.py`) — สเปกเต็มใน `SPEC.md`
2. `python3 tools/assemble.py <set>` → รวม + สลับคำตอบ + ตรวจ (ต้อง ✗ 0) + สร้าง `data/index.json`
3. `python3 tools/sweep.py` → เปิดทุกหัวข้อที่ 390px โหมดมืด (ใช้เวลา ~15 นาที)
4. commit + push แล้ว publish: `Artifact` publish ด้วย `url` ข้างบน · `file_path` = `salmon-nl/index.html` · `root` = `salmon-nl` · `files` = เฉพาะไฟล์ data ที่แก้

**การสลับคำตอบ** (`tools/spread.py`): ชุด gi/cardio/resp/nephro ใช้แบบ hash ต่อ id (LEGACY) ชุดอื่นใช้แบบกระจายสมดุลต่อชุด
แก้ข้อเดิมได้ แต่ถ้าเพิ่ม/ลบข้อในชุดที่ไม่ใช่ LEGACY ตำแหน่งคำตอบของข้อถัดไปจะเลื่อน → ถ้าผู้ใช้ทำไปแล้วให้เพิ่มข้อใหม่ด้วย `mcq_ordered` (กำหนดตำแหน่งเอง) แทน

## ที่ยังทำต่อได้
- เทียบเนื้อหากับสไลด์ที่เป็นภาพ (export PDF ของ deck ใหญ่ผ่าน connector ไม่ได้ — ต้องให้ผู้ใช้ส่ง PDF มา) เพื่อยืนยันเฉลยข้อเก่าที่ "ตอบตามหลักฐาน"
- ผูกข้อจาก exam25 เข้าหัวข้อของแต่ละระบบ (ตอนนี้แยกเป็นชุดของตัวเอง)
