---
name: med421-lecture
description: Turn a MED421 lecture file (Google Drive link, uploaded PDF/PPTX, or slide images) into a full lesson in the "MED421 learn" artifact — read the slides, write notes, build sections + MCQ/MEQ/OSCE, link the matching Ward Drill (bank_merged.json) questions, run every check, publish safely and update HANDOFF.md. Use whenever the user sends lecture slides or a Drive link for MED421/Internal Medicine, says "ทำคาบนี้", "ทำ lecture", "ลง drill/learn", "อัปเดต artifact", or asks whether Ward Drill questions are covered by lessons ("มี lecture ครบไหม", coverage).
---

# MED421 lecture → MED421 learn

ผู้ใช้เป็นนักศึกษาแพทย์ปี 4 (รอบ Internal Medicine รพ.ราชวิถี) ส่งไฟล์สไลด์มา → สร้างเป็นคาบเรียนเต็มรูปแบบใน artifact
**MED421 learn** https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE แล้วตรวจทุกอย่างก่อนขึ้นเว็บ
ตอบผู้ใช้เป็นภาษาไทย · repo `Kingcondom/ioioioio` · ทำงานใน `artifact/` · สคริปต์อยู่ใน `artifact/tools/`

## 0. เริ่มงาน — ห้ามข้าม
1. อ่าน `HANDOFF.md` ทั้งไฟล์ (สถานะล่าสุด กฎสำรองข้อมูล ข้อตกลงกับผู้ใช้ §8)
2. `git fetch origin` แล้วดูว่า branch ไหนมีงานล่าสุด (`git log -1 --date=short --format='%ad %s' origin/<branch>`) — ถ้า branch ที่ได้รับมอบหมายเก่ากว่า ให้ **merge branch ที่ใหม่กว่าเข้ามาก่อน**
3. ตรวจว่าเว็บตรงกับ repo: `Artifact list` (scope files) → `Artifact read` ด้วย `paths` ของไฟล์ data → `python3 artifact/tools/compare_live.py <โฟลเดอร์ที่ read บันทึก>`
   ถ้า "ต่าง" ในไฟล์ที่เราไม่ได้แก้ = มี session อื่น publish ไปแล้ว → หา branch ที่ตรงกับเว็บแล้ว merge **ห้าม publish ทับ**
4. `pip install -q playwright pymupdf` (ห้ามรัน `playwright install` — มี Chromium อยู่แล้ว)

## 1. ระบุคาบ
- ไฟล์ Drive: `get_file_metadata` (ชื่อไฟล์ อาจารย์ ขนาด) · ปฏิทิน: `search_events` ด้วยชื่อเรื่องหรือชื่ออาจารย์ → วันที่บรรยาย
- `python3 artifact/tools/coverage.py --find "<คำค้น>"` → ถ้าคลัง Ward Drill มีคาบนี้ ได้ **เลขคาบจริง** และรายชื่อข้อที่ต้องผูก
  - มีในคลัง → `lec` = เลขคาบในคลัง (เช่น "24") + `date` = วันที่จริง
  - ไม่มีในคลัง → `lec` = วัน/เดือน (เช่น "5/10") ตามที่ทำมา
- เลือกชุดวิชาจาก `artifact/data/index.json` (air · cardio · chest · nephro · neuro · endo · id) — ชุดใหม่ต้องเพิ่ม entry ใน index พร้อม accent สองโหมด
- **ประเมิน token บอกผู้ใช้ก่อนเริ่ม** (คาบเต็ม ~40–50k) ตามข้อตกลง ถ้าผู้ใช้สั่ง "ทำเลย" มาแล้วไม่ต้องถามซ้ำ

## 2. อ่านสไลด์ → เขียนโน้ตลงไฟล์ทันที
- ลอง `read_file_content` ก่อน (PDF/PPTX ที่มีข้อความดึงได้ครบ ประหยัดที่สุด)
- สไลด์ภาพล้วนหรือไฟล์ที่อัปโหลดในแชท → render ด้วย pymupdf (poppler ไม่มีในเครื่อง)
  `python3 -c "import pymupdf;d=pymupdf.open('<pdf>');[p.get_pixmap(dpi=130).save(f'nl/img_<topic>/p{i+1:02d}.png') for i,p in enumerate(d)]"`
  แล้ว `Read` ภาพทีละ 4 หน้า · **ลายมือของผู้ใช้ (✍️) = สิ่งที่อาจารย์เน้นในห้อง** ต้องจดและใส่ในบทเรียน
- เขียน `slides/<topic>_notes.md` **ทีละหน้า/ทีละช่วง** แล้ว commit + push ทันที (context อาจถูกย่อ container อาจถูกคืน)
- จดไว้ชัด ๆ ว่าสไลด์หน้าไหนเป็นภาพ/ตารางที่อ่านไม่ได้ → ส่วนนั้นต้องอิงแนวทางและระบุในบทเรียน
- เพิ่มรายการไฟล์ใน HANDOFF §6

## 3. สร้างคาบ — `artifact/tools/build_<topic>.py`
ใช้ `build_hiv.py` (คาบไม่มีคลัง) หรือ `build_af.py` (มีคลัง ผูกข้อท้ายสคริปต์) เป็นแม่แบบ — helper `sec()` `mcq()` เหมือนกัน
- **schema** (HANDOFF §3): lecture `{lec, date, title, subtitle, objectives[], sections[], meq[], osce[], nlGap?, guidelines?[]}` · section `{id, title, summary, minutes, source, nl[], md, pearls[], items[]}` · item `{id, kind:"mcq"|"old", stem, choices[5], answer 0–4, explain, pearl, topic, src, ref[], nl[]}`
- **เนื้อหาเต็มรูปแบบ** 10–13 หัวข้อ เรียงตามโครงสไลด์ · แต่ละหัวข้อ: อธิบาย **กลไก** ไม่ใช่แค่ข้อเท็จจริง · ตาราง · pearls 3–5 ข้อ · MCQ ใหม่ 1–3 ข้อ (โจทย์อังกฤษสไตล์ข้อสอบ คำอธิบายไทย บอกเหตุผลข้อผิดด้วย)
- MEQ 1 ชุด (vignette ไทยแบบโจทย์จริง + คำถามย่อยพร้อมคะแนน) · OSCE/SAQ 1 สถานี (เกณฑ์ให้คะแนนเป็นตาราง)
- id: section `<set>-<topic>-NN` · ข้อใหม่ `<SET>-<TOPIC>-MCQ-NN` · `<SET>-<TOPIC>-MEQ-01` · `<SET>-<TOPIC>-OSCE-01`
- **รหัส นล.**: ค้นใน `artifact/data/nl.json` ด้วย regex ชื่อโรค/อาการ ใส่ทั้งระดับหัวข้อและระดับข้อ · ส่วนที่ไม่มีรหัส → เขียน `nlGap` + `guidelines[]` (แนวทางที่อาจารย์อ้าง + แนวทางปัจจุบัน)
- **เนื้อหาที่ไม่ได้มาจากสไลด์** (เติมจากแนวทาง/ความรู้) ต้องบอกในบทเรียนว่าอิงอะไร และแจ้งผู้ใช้ตอนจบ
- **ผูกข้อคลัง Ward Drill**: `BANK_MAP = {section_id: [bank ids]}` แล้ว `link(set, lec, BANK_MAP, meq=[...], osce=[...])` จาก `link_bank.py` — ทุกข้อของคาบในคลังต้องลงหัวข้อที่ตรงเรื่อง (อ่านโจทย์จาก `coverage.py --find`)
- **กระจายตำแหน่งคำตอบ** ของข้อใหม่ด้วยบล็อก spread ใน `build_hiv.py` (ยกเว้นข้อที่ตัวเลือกเรียงตามธรรมชาติ เช่น stage, ตัวเลข) — **ทำก่อน publish ครั้งแรกเท่านั้น** ห้ามสลับคำตอบของข้อที่ขึ้นเว็บแล้ว (คำตอบที่ผู้ใช้เคยทำเก็บเป็น index ใน localStorage)
- ท้ายสคริปต์: ลบคาบเดิมที่ `lec` เดียวกัน → append → ตรวจ id ซ้ำ/นล./code fence → เขียนไฟล์ → อัปเดต `lectureCount`
- เขียนทีละ 4–6 หัวข้อ แล้ว `python3 artifact/tools/build_<topic>.py` + commit "WIP: ..." + push ทุกก้อน
- อัปเดต `intro`/`howto` ของชุดใน `index.json` (บอกคาบใหม่ ลำดับที่แนะนำ ตัดชื่อคาบนี้ออกจาก "ยังไม่ได้ทำ")

## 4. ตรวจ — ต้องผ่านทุกข้อก่อน publish
| คำสั่ง | ตรวจอะไร |
|---|---|
| `python3 artifact/tools/check_lecture.py <set> <lec>` | schema · id ซ้ำทั้งเว็บ · รหัส นล. · code fence · ตัวเลือก 5 · **`**` ไม่ครบคู่ (จะโชว์ดิบบนจอ)** · คำตอบกระจุก · lectureCount · สถิติคาบ — **คาบใหม่ต้องไม่มี ✗** (ข้อผิดพลาดเก่าของคาบอื่นดูใน HANDOFF) |
| `python3 artifact/tools/verify.py` | เปิดเว็บจริง สลับทุกชุด ตอบข้อสอบ localStorage ไม่ล้นจอมือถือ |
| `python3 artifact/tools/check_render.py <set> <lec>` | ไล่กดทุกหัวข้อของคาบใหม่ที่ 390px · `**` ค้าง · ล้นจอ · page error · แท็บ MEQ/OSCE |
| `python3 artifact/tools/coverage.py` | ความครอบคลุมคลัง Ward Drill หลังผูกข้อ |
ตรวจเนื้อหาซ้ำด้วยตัวเอง: ตัวเลขทุกตัวตรงกับโน้ตสไลด์ · คำนวณในโจทย์ (คะแนน ขนาดยา) ถูก · ข้อที่ถูกมีข้อเดียว

## 5. Publish อย่างปลอดภัย
1. commit + push ก่อน
2. `Artifact read` ด้วย `paths` ของไฟล์ที่จะส่ง → `compare_live.py <dir> <commit ก่อนเริ่มงาน>` ต้อง "ตรงกัน" (เว็บยังเป็นฐานเดียวกับที่เราเริ่ม)
3. `Artifact read` url เปล่าหนึ่งครั้ง (นับเป็นการดูเวอร์ชันล่าสุด) แล้ว publish:
   `url` = artifact เดิม · `file_path` = `artifact/index.html` · `root` = `artifact` · `files` = **เฉพาะไฟล์ที่แก้** (เช่น `data/id.json`, `data/index.json`) · `label` สั้น ๆ
4. `Artifact list` scope files → ขนาดไฟล์ต้องตรงกับ `wc -c artifact/data/*.json`
- index.html บนเว็บใหญ่กว่าใน repo เสมอ (บริการห่อ `<html>` เพิ่ม) — เป็นเรื่องปกติ

## 6. ปิดงาน
- อัปเดต `HANDOFF.md`: เวอร์ชัน · จำนวนคาบ · แถวในตาราง §4 (หัวข้อ/ข้อ/MEQ/OSCE + ส่วนที่อิงแนวทาง) · §6 ไฟล์สไลด์ · ตัวเลข coverage → commit + push
- รายงานผู้ใช้ (ไทย กระชับ): ลิงก์ + เวอร์ชัน · คาบมีอะไร (หัวข้อ ข้อใหม่ + ข้อคลัง MEQ OSCE) · **ส่วนที่ไม่ได้มาจากสไลด์** · ผลตรวจ · coverage ใหม่ · ถ้าพบงานของ session อื่นบนเว็บ บอกว่า merge แล้วไม่ทับ

## กับดักที่เคยเจอ
- markdown ในหน้าเว็บ: **ไม่มี code fence** · ย่อหน้าถูก render ทีละบรรทัด → **ตัวหนาห้ามคร่อมการขึ้นบรรทัดใหม่** (รายการ `-` คร่อมได้) · ห้ามมี `*` ติดตัวเลขกลางคำ (เช่น HLA-B*57 → เขียน HLA-B5701)
- `**` ในคำอธิบายข้อสอบมองไม่เห็นตอนยังไม่ตอบ — `check_lecture.py` จับได้ `check_render.py` จับไม่ได้ ต้องใช้ทั้งคู่
- ห้ามแก้ไฟล์ data ของชุดอื่นโดยไม่จำเป็น และห้าม publish ไฟล์ที่ไม่ได้แก้ (ป้องกันทับงานคนอื่น)
- Google Fonts ใน Playwright ขึ้น ERR_CERT — ปกติของ container · อย่าใช้ `pgrep -f` รอสคริปต์
- `nl/img*/` (ภาพเรนเดอร์) อยู่ใน .gitignore — ไม่ต้อง commit
