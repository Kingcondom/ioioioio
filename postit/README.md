# Post-it ห้ามลืม

หน้าเปิดค้างไว้บน iPad หรือจอข้างโต๊ะ วนการ์ดจากหัวข้อที่ผู้ใช้ปักไว้ (pearls · mnemonics · โจทย์ท้ายหัวข้อ)

- artifact: https://claude.ai/artifact/BRsYSzd35CARo2m6Jw6ANY (slug `54746283-c801-4fa6-8e93-34755d68812d`, private)
- capabilities: `db` + `user` (หัวข้อที่ปักเก็บที่ `data/users/<id>/postit` ซิงก์ข้ามเครื่อง)
- ไฟล์ที่ publish: `index.html` · `data/sec.json` · `data/q.json`

## ลิงก์ปัก (hash แบบ plain `#name` เท่านั้น)

| hash | ปักอะไร | ปุ่มอยู่ที่ |
|---|---|---|
| `#l-<section id>` | หัวข้อใน MED421 learn | แถวชิปใต้ชื่อหัวข้อ (`artifact/index.html`) |
| `#s-<section id>` | หัวข้อใน Salmon NL | แถวชิปใต้ชื่อหัวข้อ (แก้บน artifact สด) |
| `#q-<item id>` | ข้อสอบ MCQ รายข้อ | ป้ายในหัวข้อของข้อ ใน Ward Drill (`pinTag()` ใน drill.html สด) |

ข้อใน Ward Drill ที่ id ไม่อยู่ใน `data/q.json` (เช่น MEQ/OSCE หรือข้อที่มีเฉพาะใน drill) จะแสดงเป็นการ์ดลิงก์กลับไป Ward Drill
Ward Drill ใส่ปุ่มเฉพาะ MCQ ใหม่และข้อสอบเก่า ไม่ใส่ใน MEQ/OSCE

## อัปเดตเนื้อหาการ์ด

Post-it เก็บสำเนาเนื้อหาไว้เอง ถ้าเพิ่มหรือแก้หัวข้อใน learn หรือ Salmon ต้อง build ใหม่

```bash
# Salmon: ดึง data/*.json ล่าสุดจาก artifact Salmon NL มาไว้ใน postit/salmon/ ก่อน
python3 postit/build_cards.py      # อ่าน ../artifact/data + salmon/ → data/sec.json, data/q.json
```

แล้ว publish เฉพาะ `data/sec.json` และ `data/q.json` ขึ้น Post-it (patch mode) ห้ามส่ง capabilities ว่าง

## แพตช์ Ward Drill (ใช้ซ้ำถ้า build drill ใหม่จาก pipeline)

`drill_pin_edits.json` = คู่ old/new สำหรับ `edit_version` (เพิ่ม `pinTag()` แล้วต่อท้าย `qno` ใน renderMCQ และข้อสอบเก่า)

## โพสต์อิทที่เขียนเอง (3 พ.ย. 2569 · v5 `1793713925-b6dd`)

ปุ่ม **+ เขียนเอง** แถบบน → ช่องเขียนบนสุดของหน้าจัดการ · เก็บใน `state.own[id] = {f, b, t, u}` (ลบ = `{del:1, u}` tombstone)
ซิงก์ไปกับเอกสารเดียวกัน `data/users/<id>/postit` · รวมข้ามเครื่องด้วย `mergeOwn` (ใบไหน `u` ใหม่กว่าชนะ)
การ์ดมี `pid = "o-<id>"` · ไม่มีเฉลย + มี " = " / " → " ใช้ `cloze()` เดียวกับ pearl · ซูมแล้วมีปุ่มแก้/ลบแทนลิงก์บทเรียน

## เมนูแก้ไข/ลบ บนการ์ด (3 พ.ย. 2569 · v6 `1793714166-18e8`)

คลิกขวา · ดับเบิลคลิก · กดค้าง 550 ms (touch/pen) · ปุ่ม ContextMenu/Shift+F10 → `#cmenu` (`openMenu`)
คลิกเดียวถูกหน่วง 260 ms เพื่อแยกจากดับเบิลคลิก · ใบบทเรียน "แก้ไข" = `editCard` → บันทึกเป็น own note แล้ว `state.done[replaceK]` ซ่อนใบเดิม
"ลบ" ใบบทเรียน = `removeCard` (เหมือน "จำได้แล้ว") · ข้อจำกัดความยาวใบเขียนเอง 600/1200 ตัวอักษร

## ภาพหน้าจอ → คำถาม (3 พ.ย. 2569 · v7 `1793729619-79d3`)

**capabilities เปลี่ยนเป็น `{db:{}, user:{}, sample:{images:true}}`** — publish ครั้งต่อไปให้ละ `capabilities` (ระบบคงไว้เอง) ห้ามส่ง `{}`
กล่อง `#shot` ในส่วนเขียนเอง (ซ่อนถ้า `claude.use("sample")` เป็น null หรือ `limits()` ไม่มี `images`) · เลือก/วาง Ctrl+V (ทั้งหน้า)/ลากภาพ
`sample.json(prompt, {images, signal})` → `[{q,a}]` → ติ๊กเลือก → เป็น `state.own` · ภาพไม่ถูกเก็บ · error ถาวร (not_granted ฯลฯ) ซ่อนกล่อง
ทดสอบด้วย mock `window.claude` ผ่าน `add_init_script` (สคริปต์ทดสอบอยู่ใน scratchpad ของ session นั้น ไม่ได้ commit)
