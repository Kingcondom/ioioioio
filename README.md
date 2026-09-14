# med421-kit — ชุด pipeline ข้อสอบอายุรศาสตร์ (MED35)

เขียนข้อสอบเป็น JSON ไฟล์เดียวต่อระบบ แล้วสั่ง build ออกมาเป็นเว็บ + PDF พร้อมผูกเกณฑ์แพทยสภา (NL 2567) รายข้อ

```bash
python3 build.py                 # ทุกระบบ -> site/
python3 build.py air --no-pdf    # ระบบเดียว ไม่ทำ PDF
python3 check_numbers.py         # ตรวจ ABG ทุกข้อ
```

| ไฟล์ | ใช้ทำอะไร |
|---|---|
| `PROMPT.md` | พรอมป์สำเร็จรูป 3 แบบ — ทำระบบใหม่ / แปลงคลังเก่า / ติวสด |
| `SPEC.md` | schema ครบทุกแบบ + มาตรฐานการเขียนข้อ + สูตรตรวจตัวเลข |
| `config.json` | ไฟล์เดียวที่ต้องแก้เวลาเพิ่มระบบ |
| `build.py` | รวม → ตรวจ → สลับเฉลย → เว็บ → PDF |
| `check_numbers.py` | Henderson–Hasselbalch + Winter's + anion gap |
| `data/` | คลังข้อสอบ (ตอนนี้: `air.json` — ระบบการหายใจ 41 MCQ + 3 MEQ) |
| `refs/nl_2567.json` | ดัชนีเกณฑ์ NL พ.ศ. 2567 เฉพาะหัวข้อระบบหายใจ 70 รายการ |
| `site/` | ผลลัพธ์: `index.html`, `air.html`, `air.pdf` |

## กันพลาดไว้ตรงไหนบ้าง

- build **หยุดพร้อมบอกจุดผิด** ถ้า id ซ้ำ / ตัวเลือกไม่ครบ 5 / ตัวเลือกซ้ำ / `lec` ไม่มีในปฏิทิน / MEQ ไม่มี `questions` — และเตือนถ้าลืม `ref`, `pearl` หรือ `nl`
- คนเขียนข้อ **เขียน `answer: 0` เสมอ** วางคำตอบถูกไว้ตัวแรก แล้ว build สลับให้ — seed แยกต่อระบบ build ใหม่จากศูนย์ได้ไฟล์ byte-identical
- `check_numbers.py` ไล่ ABG ทุกข้อ ถ้า pH ไม่ตรงกับ PaCO2/HCO3 จะ exit 1 พร้อมบอกค่าที่ควรเป็น
