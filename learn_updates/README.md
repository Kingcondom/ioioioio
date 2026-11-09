# อัปเดตอาร์ติแฟกต์ MED421 learn

## 2026-11-09 — คาบ Anemia (9/11): สไลด์ อ.Kunapa Lam-arunthai

ต้นทาง: `Approach to anemia (2).pdf` ใน Google Drive (สไลด์คาบจริง + โน้ตลายมือ)

- `kunapa_sections.py` — 5 หัวข้อใหม่ (`hon-anm-k1`…`k5`) พร้อมข้อสอบท้ายหัวข้อ 15 ข้อ (`HON-ANM-MCQ-K01`…`K15`)
- `apply_kunapa.py` — แทรกหัวข้อหลัง `hon-anm-00` ใน `data/hemonc.json`, อัปเดต title/subtitle/objectives/guidelines ของคาบ, เพิ่มกล่อง "Kunapa ·" ใน `hon-anm-00` และอัปเดต intro/howto ของชุด hemonc ใน `data/index.json`
  - ตรวจว่า id ไม่ซ้ำ ตัวเลือก 5 ข้อไม่ซ้ำ และรหัส NL มีอยู่ใน `data/nl.json`
  - รันซ้ำได้ (ลบ `hon-anm-k*` เดิมก่อนแทรก)

อาร์ติแฟกต์: https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE (เปลี่ยนเฉพาะ `data/hemonc.json` และ `data/index.json`)

## 2026-11-09 — ปรับหน้าตาตาม study-page-design

- `restyle.py <artifact-read.html> <out.html>` — แปลง CSS ของหน้า: สเกลตัวอักษร 12/14/16/18/20/24 · spacing 4–48 · radius 6/10/16 · น้ำหนักสูงสุด 600 · palette → ชื่อตามหน้าที่ · ปุ่มสูง ≥ 44px พร้อม state disabled/loading · ตัด animation ตอนแสดงการ์ด · ปุ่ม primary หนึ่งปุ่มต่อการ์ด (markread และ MEQ reveal เป็นปุ่มรอง)
- ไม่แตะขนาดตัวอักษรในแผนภาพ SVG (`.fig svg text`, `.lg/.sm/.xs`) และอนิเมชันกลไกในภาพ

## 2026-11-09 — โหมดพรีเซนต์ทั้งคาบ

- `present_mode.py <in.html> <out.html>` — เพิ่มปุ่ม "▶ พรีเซนต์คาบนี้" (การ์ดคาบ) และ "▶ พรีเซนต์จากหัวข้อนี้" (หน้าหัวข้อ)
- สไลด์สร้างจากข้อมูลคาบอัตโนมัติ: ปก → ต่อหัวข้อ (เปิดหัวข้อจาก summary → หัวข้อย่อย ### ละสไลด์ → ปิดหัวข้อด้วยหลักจำ) → สรุปจุดที่ติด
- keyword = คำตัวหนาในบทเรียน (ไม่มีพอใช้หัวแถวของตาราง) สูงสุด 10 คำ · ภาพกลไกปิดป้ายอัตโนมัติ · โน้ตเต็มซ่อนไว้ (ปุ่ม N)
- ประเมินตัวเองต่อสไลด์เก็บใน `state.rate` คีย์ `pv|<ชุด>|<หัวข้อ>#<ลำดับ>` จึงซิงก์บัญชี · ตำแหน่งสไลด์ล่าสุดจำใน localStorage `med421-pres`
- แก้พร้อมกัน: ลิงก์ยาวในกล่อง นล./แนวทาง ทำหน้าคาบล้นจอบนมือถือ
- ลำดับการรัน: `restyle.py` → `present_mode.py`
