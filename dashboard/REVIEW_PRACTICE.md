# ฝึกข้อสอบคาบที่ทวนแล้ว (Dashboard → Ward Drill)

31 ต.ค. 2569 · Ward Drill v23 (`1793452738-b44b`) · MED421 Lectures (`1793452766-8161`)

## ใช้ยังไง
- กด ✓ คาบที่ทวนใน **MED421 Lectures** ตามปกติ
- เปิด **Ward Drill → โหมด "คาบที่ทวนแล้ว"** ได้เลย: แยกตาม **วันที่ทวน** (ใหม่สุดก่อน) → การ์ดต่อคาบ
  ตาราง ปีที่ออก (MED35 → MED28, ข้อฝึกเพิ่ม) × MCQ / MEQ / SAQ·OSCE (ทำแล้ว/ทั้งหมด กดเพื่อทำเฉพาะช่องนั้น)
- ปุ่ม **"ทำข้อสอบของวันที่ …"** รวมข้อสอบทุกคาบที่ทวนวันนั้นไว้ที่เดียว · แถบซ้าย: วันที่ทวน / คาบ / Part / ปี
- อยากได้ทันทีหลังกดทวน: ปุ่ม **ฝึกข้อสอบคาบที่ทวนแล้ว** ในแผงข้างของ Dashboard

## การซิงก์ (artifact แต่ละตัวมี db ของตัวเอง อ่านข้ามกันไม่ได้)
1. **งานตั้งเวลา** "MED421 ซิงก์การทวน Dashboard → Ward Drill" (`trig_017kVBLiXnwEKoUvNPaT1gwb`)
   07:23 09:23 11:23 13:23 15:23 17:23 19:23 23:23 (เวลาไทย) — อ่าน `data/users/<id>/slides` ของ dashboard
   แล้วเขียนทับบรรทัด `var RV_SEED={u, at, reviews}` ในหน้า drill (edit_version) เฉพาะเมื่อมีการทวนใหม่
   - เขียน db ของ drill ตรง ๆ ไม่ได้ เพราะ drill เป็น public (เครื่องมือ db_write ปฏิเสธ `public_audience`)
   - หน้า drill ใช้ RV_SEED เฉพาะเมื่อผู้ดูคือเจ้าของ (`u` ตรงกับ user.id()) แล้วเก็บลง `data/users/<id>/drill-reviewed`
   - หลัง 18 พ.ย. 2569 งานจะไม่ทำอะไร ลบได้
2. **ลิงก์จากปุ่มใน dashboard** `#review~y2026~<MMDDHHMM>.<MMDD>.<MMDD>~…` (id คาบ + วันที่ทวน)
- ใช้ชุดที่ `at` ใหม่กว่า (seed: at = updatedAt ของ dashboard · ลิงก์: เวลาที่กด)

## ข้อมูลข้อสอบ
- ข้อของคาบ = คลังข้อสอบเก่า + MCQ ใหม่ + MEQ/OSCE ที่ `lec` ตรงกัน · ปีจาก `years`
- Part ของปีนั้นอ่านจาก `src` / `ref` ช่วงข้อความหลัง `MEDxx` (ไม่ระบุ = MCQ) · MEQ/OSCE ใหม่ใช้ `part` ของข้อ
- `DLECS` (id คาบ dashboard → hash drill, ชื่อ, อาจารย์) ฝังจาก LECS ของ dashboard ตอนแพตช์ — ถ้า dashboard เพิ่มคาบ ต้องแพตช์ drill ใหม่

## ถ้า build drill / dashboard ใหม่จาก pipeline
```bash
python3 dashboard/patch_drill_review.py <drill.html> <dashboard index.html> <out.html>   # หลัง drill_tool.py merge
python3 dashboard/patch_dash_review.py <dashboard index.html> <out.html>
```
หลัง publish drill ใหม่ บรรทัด `var RV_SEED=null;` จะว่าง — งานตั้งเวลาเติมให้รอบถัดไป
`--edits edits.json` เขียนคู่ old/new สำหรับ `edit_version` (แก้เฉพาะโค้ด ไม่แตะข้อมูลข้อสอบ)
