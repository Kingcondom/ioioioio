# Ward Drill — หน้าตาแบบ MED421 learn + สีประจำระบบ

เผยแพร่แล้วเป็น **Version 40** ของ MED421 Ward Drill `Fdi5gcNXKqFLAXg4fQBV7X` (13 พ.ย. 2569)

- `tr_drill.css` `tr_drill.js` — โครงหน้าแบบ Teaching Round เหมือนหน้า learn (ต่อยอดจากร่างใน branch `claude/pensive-volta-ki8ie1`)
- `make_sys_css.py` → `sys_colors.css` — สีประจำระบบ 12 ระบบ ทั้งโหมดสว่างและมืด
  (ทั้งหน้าใช้สีของระบบที่เลือก การ์ด แถบระบบ แถบซ้าย และป้ายในโหมดรวมหลายระบบใช้สีของระบบตัวเอง)
- `apply_tr_drill.py <live.html> <out.html>` — ใส่ทั้งหมดลงไฟล์ที่ Artifact `action:read` บันทึกไว้
- `test_mobile.js` `test_desk.js` `test_sync.js` — Playwright (`node test_mobile.js http://localhost:8767/index.html <โฟลเดอร์ภาพ>`)

เปลี่ยนสีระบบไหน: แก้ hue ใน `SYS` ของ `make_sys_css.py` แล้วรัน `python3 make_sys_css.py` ก่อน apply
