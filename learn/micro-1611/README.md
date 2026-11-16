# MED421 learn — คาบ 16/11 ทบทวน Microorganism

เนื้อหาคาบใหม่ของชุด **ID** ในเว็บ MED421 learn (https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE)

ที่มา
1. สไลด์ "Microorganism 2026.pdf" (Google Drive, 96 หน้า, Quiz 1–16)
2. บันทึกเสียง Plaud "11-16 การบรรยาย: ทบทวนจุลชีววิทยาคลินิก ปรสิต และแนวทางรักษา" (48 นาที)

ไฟล์
- `lec_a.py` หัวข้อ 1–7 (แบคทีเรีย) · `lec_b.py` หัวข้อ 8–14 (รา ผื่น mycobacteria ปรสิต มาลาเรีย)
- `build.py` รวมเป็นคาบ 16/11 + MEQ/OSCE ตรวจรหัส นล. ตรวจภาพ สลับตำแหน่งเฉลย แล้วเขียน `data/id.json` และ `data/index.json`
- `data/` ไฟล์ที่เผยแพร่อยู่ (`nl.json` ใช้ตรวจรหัส นล. เท่านั้น) · `img/id/mic-*.jpg` ภาพจากสไลด์ 35 ภาพ

แก้เนื้อหา: แก้ `lec_a.py` / `lec_b.py` แล้วรัน `python3 build.py` (ลบคาบ 16/11 เดิมแล้วใส่ใหม่ รันซ้ำได้ ผลเหมือนเดิม)
แล้วเผยแพร่ด้วยเครื่องมือ Artifact ไปที่ URL ข้างบน โดยส่ง `data/id.json`, `data/index.json` และ `img/id/*.jpg` เป็นไฟล์ประกอบ
