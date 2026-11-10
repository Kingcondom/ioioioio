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

## 2026-11-09 — โครงหน้าแบบ Teaching Round (learn Version 67 · `1794200490-ba64`)

ฐาน = live v66 `1794196963-003d` (= `learn_updates/tr/index_v66_base.html`, sha256 d3d5a834…) → `python3 learn_updates/tr/apply_tr.py <base> <out>` → `index_v67.html`
ข้อมูล `data/*.json` ไม่ได้แตะ publish แค่ `index.html`

ลำดับทั้งหมดถ้าต้องสร้างใหม่จากหน้าเก่า: `restyle.py` → `present_mode.py` → `tr/apply_tr.py`

สิ่งที่ `apply_tr.py` ทำ
1. ต่อท้าย CSS `tr/tr.css` — โทเคนสี lime ทับของเดิม (light/dark), การ์ดมุม 24, ปุ่ม pill, แถบล่าง, วงล้อ, sheet, แถบซ้าย/ขวา (≥1100 / ≥1400), `.cols{zoom:1.1/1.2}` บนคอม
2. `state.log` = ประวัติการทวนรายวัน `{yyyy-mm-dd:[section id]}` เก็บ 60 วัน — เพิ่มใน `normP` (จึงซิงก์ขึ้นบัญชีใน doc `data/users/<id>/learn`), `adopt`, `merge` (`mergeLog` รวมแบบ union)
3. `applyAccent` เลิกตั้งสีประจำชุดเป็น inline (ใช้ lime ทั้งเว็บ)
4. JS `tr/tr.js` ก่อน `boot()` — `viewHome` ถูกแทนด้วย `TR.home` และ `render` ถูกห่อให้เรียก `TR.after()` หลังทุกครั้ง
   - นับ "ทวนวันนี้" เมื่อหัวข้อในหน้า section ตอบครบทุกข้อ หรือกด "ทำเครื่องหมายว่าเรียนแล้ว"
   - ข้อสอบซ่อนหลังแถบ "ทำข้อสอบท้ายหัวข้อ" จนกว่าจะกด (ถ้าเคยตอบแล้ว/โหมดทวน ไม่ซ่อน) — ปุ่มไปหัวข้อถัดไปยังเห็นเสมอ
   - ปัด: หน้าแรก/คาบเรียน = เปลี่ยนชุด · หน้าคาบ = คาบก่อน/ถัดไป · หน้าหัวข้อ = หัวข้อก่อน/ถัดไป (Alt ← → เหมือนกัน)
   - วงล้อสลับคาบ: ดับเบิลคลิก/กดค้าง 2 วิ ที่ไม่ใช่เนื้อหา (`.prose .q table .fig` ฯลฯ ถูกเว้นเพื่อไม่แย่งการเลือกข้อความไปถาม AI)
   - วงล้อทางลัด 11 ช่อง: เรียนต่อ พรีเซนต์ ถาม AI ข้อที่ผิด MEQ OSCE โหมดทวน Post-it สลับคาบ สารบัญ โหมดสี
   - Ctrl K / `/` ค้นหาหัวข้อทุกชุด (โหลดทุกชุดตอนเปิดครั้งแรก) · 1–5 ตอบข้อสอบ · + เปิดทางลัด
   - ≥1400: ถาม AI (กล่องเดิม) ติดมุมขวาบนอัตโนมัติ (ปิดแล้วไม่เปิดเองอีกใน session) + แถบ ข้อที่ผิด / ปักจากหน้านี้ล่าสุด (localStorage `med421-learn-pins`) / คีย์ลัด
   - แก้บั๊กเดิม: ชิปอ้างอิงที่มีลิงก์ยาวทำหน้าล้นจอบนมือถือ
5. ค่าคงที่: เป้า 5 หัวข้อ/วัน · วันสอบ `EXAM="2026-11-17"` ใน `tr.js`

ทดสอบ (Playwright, เสิร์ฟหน้า+data ทุกชุดในเครื่อง): `test_mobile.js` (390 light/dark) · `test_desk.js` (1200/1440/1920) · `test_sync.js` (stub `window.claude` — log รวมกับของบัญชีและเขียนกลับ, AI ติดข้างจอ) · `feat_reg.js` (ปิดตาราง/ปัก/โหมดทวน) — ผ่านหมด 0 error

⚠️ ยังไม่ได้ทำ (ต้องได้รับอนุญาตก่อน เพราะอยู่คนละ branch/artifact)
- สำเนา `artifact/` ใน branch `claude/internal-med-learning-web-j9ca6l` ยังเป็นของก่อนวันที่ 9 พ.ย. (ไม่มีคาบ Kunapa, restyle, present, TR shell) — ห้าม publish จากสำเนานั้น
- Post-it `postit/build_cards.py` ยังไม่ได้รันใหม่ → หัวข้อ `hon-anm-k1..k5` ยังค้นใน Post-it ไม่เจอ

## 9 พ.ย. — ปิดงาน
- branch หลัก `claude/internal-med-learning-web-j9ca6l` commit 7235b71: สำเนา `artifact/index.html` + data + `postit/` ตรงของสด (learn v67, Post-it v11)
- `verify.py` / `verify_pin.py` ปรับตาม UI ใหม่ · ผ่านพร้อม `checkdata.py` · รายละเอียดใน HANDOFF.md หัวข้อ 🟢 9 พ.ย.

- 9 พ.ย. v68: ปุ่มย่อ/ขยายขนาดเนื้อหา (`.tr-fz`, 80–150%, คีย์ - / =, localStorage `med421-learn-fz`) ตามคอมเมนต์ใน artifact · ทดสอบ `tr/test_fz.js`
- 9 พ.ย. v69: ปุ่มซ่อนแถบซ้าย/ขวาบนคอม (`html.tr-noside/.tr-nodock`, ปุ่มคืนเป็นแถบแคบขอบจอ, คีย์ [ ], localStorage `med421-learn-panes`) · ทดสอบ `tr/test_pane.js`
- 9 พ.ย. v71: ปุ่ม "กดว่าเรียนจบคาบนี้" (`markLec`, ใช้ state.done เดิม) — สร้างต่อจาก v70 ของอีก session (วงล้อไล่หัวข้อในคาบ) · tr.js/tr.css ในโฟลเดอร์นี้ยังเป็นของ v69 ให้ใช้ index_v71.html เป็นฐาน

## 10 พ.ย. — คาบ Heart failure (Cardio · lec "HF") + Genital ulcer/syphilis (ID · lec "10/11") · learn `1794327696-f219`
- ที่มา: สไลด์ `Intro to HF for MD 4th yr 11_2026.pdf` (Drive, อ.Chatchai Pitakrattanachai) · บันทึกเสียง Plaud 10 พ.ย. (ไม่ได้ระบุชื่ออาจารย์)
- ตรวจกับแนวทางปัจจุบัน: 2026 ESC HF guideline (28 ส.ค. 2026) · AHA/ACC/HFSA 2022 · HFCT · CDC STI 2021/2024 · WHO 2024 · คู่มือกรมควบคุมโรค — จุดที่ต่างจากสไลด์/คำบรรยายอยู่ในกล่อง "อัปเดตแนวทาง ·"
- `hf_syphilis/build_hf.py` → `cardio_hf.json` · `gus_a/b/c.py` → `id_gus.json` · `validate.py <set> <json>` · `merge.py <live data dir> <out>` (แทน/เพิ่มคาบ + แก้ intro/howto ใน index.json)
- publish เฉพาะ `data/cardio.json` `data/id.json` `data/index.json` ทับ live `1794326333-1056` (ข้อมูลรูป imgs ของอีก session ยังอยู่ครบ)
- ⚠️ สำเนา `artifact/data` ใน branch หลักยังไม่ได้ sync: live มี imgs ที่อีก session เพิ่ม (ไฟล์ img/ ยังไม่อยู่ใน repo) ถ้าคัดลอกแค่ json จะทำให้ checkdata ฟ้องรูปหาย
