# ศัลย์ masterfucker

เว็บบทเรียนศัลยศาสตร์ภาษาไทย (สรุปใหม่จาก Schwartz's Principles of Surgery 11e) ใช้ engine เดียวกับ NL1 learn
แยก 3 กลุ่มเรียน: **NL1-2** (`n12`) · **NL3** (`n3`) · **Resident** (`res`)

หน้าเว็บที่เผยแพร่: https://claude.ai/artifact/KD4pmvTRdHGB59YptvHPZm

```
index.html          หน้าเว็บ (engine) — โหลด data/index.json แล้วโหลดไฟล์ของกลุ่มที่เปิด
parts/<กลุ่ม>_<คาบ>.json   ต้นฉบับรายคาบ (คำตอบถูกอยู่ choices[0] เสมอ)
build.py            รวม parts → data/<กลุ่ม>.json + data/index.json (สลับตำแหน่งคำตอบแบบ seed คงที่)
validate.py         ตรวจรูปแบบไฟล์คาบ: python3 validate.py parts/*.json
CONTENT_SPEC.md     สเปกการเขียนเนื้อหา/ข้อสอบ
```

แก้เนื้อหา → `python3 validate.py parts/*.json && python3 build.py` → publish `index.html` พร้อม `data/*.json` ไปที่ URL เดิม
สี ชื่อแบบฝึก (MEQ/OSCE/Mock oral) และบทบาทของ AI tutor ของแต่ละกลุ่มตั้งไว้ใน `COURSES` ใน build.py

## แผนภาพ pathophysiology
ทุกหัวข้อมีแผนภาพ SVG (298 ภาพ) เก็บใน `figs` ของแต่ละ section และวางในเนื้อหาด้วยบรรทัด `[[fig:key]]` — สเปกอยู่ใน FIG_SPEC.md
ตรวจ: `python3 tools/figlint.py parts/*.json` และ `node tools/figrender.js parts/*.json` (ต้องได้ 0 ทั้งคู่)
