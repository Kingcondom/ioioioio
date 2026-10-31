# ฝึกข้อสอบคาบที่ทวนแล้ว (Dashboard → Ward Drill)

เพิ่มเมื่อ 31 ต.ค. 2569 · Ward Drill v21 (`1793451624-bf76`) · MED421 Lectures (`1793451666-fded`)

## ใช้ยังไง
1. ใน **MED421 Lectures** กด ✓ คาบที่ทวนแล้วตามปกติ
2. แผง "การทวนของฉัน" มีปุ่ม **ฝึกข้อสอบคาบที่ทวนแล้ว · N คาบ** → เปิด Ward Drill โหมด **คาบที่ทวนแล้ว**
3. หน้าแรกเป็นการ์ดต่อคาบ: ตาราง ปีที่ออก (MED35 → MED28, ข้อฝึกเพิ่ม) × MCQ / MEQ / SAQ·OSCE
   ตัวเลขคือ ทำแล้ว/ทั้งหมด กดเพื่อทำเฉพาะช่องนั้น · แถบซ้ายเลือกคาบ / Part / ปี

## ทำงานยังไง
- dashboard ส่งรายการผ่านลิงก์ `DRILL#review~<drill[0] ของคาบ>_<จำนวนรอบที่ทวน>~…` เรียงจากที่ทวนล่าสุด
  (db ของแต่ละ artifact แยกกัน อ่านข้ามกันไม่ได้ จึงส่งทาง hash) — `#review` เฉย ๆ = เปิดโหมดด้วยรายการเดิม
- drill เก็บรายการไว้ที่ localStorage `med421-drill-reviewed` และบัญชี `data/users/<id>/drill-reviewed` = `{keys:[{k,n}], at}`
- ข้อของคาบ = คลังข้อสอบเก่า + MCQ ใหม่ + MEQ/OSCE ที่ `lec` ตรงกัน · ปีจาก `years`
- Part ของปีนั้นอ่านจาก `src` (คลังเก่า) / `ref` (MCQ ใหม่) ช่วงข้อความหลัง `MEDxx` — ไม่ระบุ = MCQ
  MEQ/OSCE ใหม่ใช้ `part` ของข้อเอง · ข้อจาก MEQ/SAQ ที่เรียบเรียงเป็นตัวเลือกมีป้าย "เรียบเรียงเป็นตัวเลือก"
- ข้อที่ออกหลายปีอยู่ทุกปีที่ออก (id ใน DOM ต่อท้าย `--<ปี>`) · คำตอบใช้ `state.answers` เดิม ซิงก์ตามปกติ

## ถ้า build drill / dashboard ใหม่จาก pipeline
แพตช์จะหาย ต้องรันซ้ำก่อน publish (แต่ละสคริปต์รันได้กับหน้าที่ยังไม่แพตช์เท่านั้น):
```bash
python3 dashboard/patch_drill_review.py <drill.html> <out.html>      # หลัง drill_tool.py merge
python3 dashboard/patch_dash_review.py <dashboard index.html> <out.html>
```
`--edits edits.json` เขียนคู่ old/new สำหรับ `edit_version` (แก้เฉพาะโค้ด ไม่แตะข้อมูลข้อสอบ)
