# MED421 — สรุปสถานะงานทั้งหมด (อัปเดต 16 ต.ค. 2569 · รอบที่ 8)

ไฟล์นี้คือ "จุดกลับมาต่อ" ถ้า context เต็มหรือเปิด session ใหม่ อ่านไฟล์นี้ไฟล์เดียวก็ทำงานต่อได้

---

## 0. กฎสำรองข้อมูล — อ่านก่อนเริ่มงานทุกครั้ง ⚠️

### ทำไมต้องมีกฎนี้
Claude รันอยู่บนเครื่องชั่วคราวในคลาวด์ มี **2 จังหวะที่ข้อมูลหาย** คนละแบบกัน

| อาการ | เกิดอะไร | อะไรหาย |
|---|---|---|
| **Context เต็ม → ย่อบทสนทนา** | ระบบสรุปช่วงเก่าเป็นบทย่อ แล้วคุยต่อ | ข้อความเก่าในแชท · **ไฟล์บนดิสก์ไม่หาย** |
| **Session จบ / ทิ้งไว้นาน** | container ถูกคืน ลบทั้งเครื่อง | **`scratchpad/` หายหมด** |

รอบที่แล้วบทสนทนาถูกย่อไป 1 ครั้ง งานไม่หายเพราะเขียนลงดิสก์ไว้ทุกขั้น

### กฎ 3 ข้อ

**1. ผลงานที่ใช้ token เยอะ → เขียนลงไฟล์ทันที ไม่เก็บไว้ในแชท**
อ่าน PDF/สไลด์มาได้ กี่หน้าก็ตาม เขียนลงไฟล์**ทีละหน้า**เลย อย่ารวบไว้ตอบทีเดียว
ถ้าบทสนทนาถูกย่อกลางคัน งานที่อยู่ในแชทหาย แต่ไฟล์ยังอยู่

**2. จบงานหนึ่งก้อน → commit เข้า repo ทันที ไม่รอจบ session**

```bash
cd /home/claude/ioioioio (หรือ /home/user/ioioioio แล้วแต่ container)
git add -A && git commit -m "<สรุปสั้น ๆ ว่าทำอะไร>"
git push -u origin <branch ที่ session นั้นได้รับมอบหมาย>
```

เกณฑ์ว่า "ก้อนหนึ่ง" คือ — สร้างคาบเรียนเสร็จ 1 คาบ · แกะเอกสารเสร็จ 1 ภาค · เขียนสคริปต์เสร็จ 1 ตัว
**อย่าทำ 3–4 ก้อนแล้วค่อย commit ทีเดียว**

**3. ของสำคัญต้องมีอย่างน้อย 2 ที่**

| ของ | ที่ 1 | ที่ 2 |
|---|---|---|
| เนื้อหาคาบเรียน + พจนานุกรม นล. | artifact (คลาวด์) | repo `artifact/data/` |
| สคริปต์ build ทุกตัว | repo | — |
| ผลแกะเอกสาร (`nl/vis*/`) | repo | — |
| ไฟล์สรุปนี้ | repo | เครื่องผู้ใช้ (ส่งผ่าน SendUserFile) |

**`scratchpad/` = พื้นที่ทำงานชั่วคราวเท่านั้น ห้ามเป็นที่เก็บของสำคัญที่เดียว**

### ของที่ไม่ต้อง commit
ไฟล์ภาพที่เรนเดอร์จาก PDF (`nl/img*/`) — สร้างใหม่ได้ใน 10 วินาที ·
ผล OCR ที่ล้มเหลว · `__pycache__/` · ไฟล์ debug ระหว่างทาง

---

> **เริ่ม session ใหม่:** ถ้า branch ที่ได้รับมอบหมายยังไม่มีงานล่าสุด ให้ `git fetch origin` แล้ว merge
> `origin/claude/lecture-artifact-integration-5plhhc` (ล่าสุด 16 ต.ค. · Version 27) เข้ามาก่อนทำอะไร · ก่อน publish ให้ `Artifact list scope=files` เทียบขนาดไฟล์กับ
> `artifact/data/` เสมอ ถ้าบนเว็บใหม่กว่า **ห้าม publish ทับ** ให้หา branch ที่ตรงกับเว็บแล้ว merge ก่อน
> (รอบ 25 ก.ย. เกือบทับคาบ Extrapulmonary TB เพราะ branch ที่ใช้อยู่เก่ากว่าเว็บ)

> 🧰 **Skill `med421-lecture`** (`.claude/skills/med421-lecture/SKILL.md`) — ขั้นตอนเต็มตั้งแต่รับไฟล์สไลด์จนขึ้นเว็บ ·
> เครื่องมือ: `check_lecture.py` (ตรวจข้อมูล) · `check_render.py` (ไล่กดทุกหัวข้อบนเบราว์เซอร์) · `coverage.py` (คลัง Ward Drill, `--find`) ·
> `compare_live.py` (เทียบเว็บกับ repo ก่อน publish) · `link_bank.py` (ผูกข้อคลัง)
>
> ⚠️ **ปัญหาเก่าที่ `check_lecture.py` พบ (5 ต.ค. · ยังไม่แก้ รอผู้ใช้ตัดสินใจ)**
> - **`**` ค้างบนจอ 127 จุด** — ตัวหนาคร่อมการขึ้นบรรทัดในย่อหน้า: neuro 21/10 (74 · เห็นบนจอใน 9 หัวข้อ) · air 33 (14) · air 08 (12) · nephro 05 (8) · air 23 (7) · cardio 04 (5) · cardio 10 (3) · neuro 07 (2) · chest 26 (1) · endo 14 (1 — `HLA DQB1*02`)
>   แก้ได้โดยไม่กระทบความคืบหน้าของผู้ใช้ (แก้แค่ข้อความ)
> - ✅ (13 ต.ค.) MEQ vignette / OSCE instruction เปลี่ยนเป็น render ด้วย `md()` แล้ว — 25 ข้อที่เคยโชว์ `**` และตารางดิบ แสดงถูกแล้ว
> - **คำตอบกระจุก** — chest 23/9 (B/C เท่านั้น) · neuro 21/10 (A 25/30) · cardio 13 · neuro 23/9, 15/10, 9/10 · air 23
>   การสลับตำแหน่งคำตอบของข้อที่ขึ้นเว็บแล้วจะทำให้คำตอบที่ผู้ใช้เคยทำ (เก็บเป็น index) ผิด → ต้องถามผู้ใช้ก่อน

## 1. ตัวงานหลัก

**artifact:** `MED421 learn` — https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE (ปัจจุบัน **Version 42** · มี **10 ชุดวิชา** · 40 คาบ · capability `db` + `user`)

> 🖼️ **ภาพประกอบ SVG (เพิ่ม 13 ต.ค. · ผู้ใช้ขอ "อธิบาย pathophysiology ของอาการเฉพาะโรค + เน้นภาพ")** — section มีฟิลด์ `figs` และบรรทัด `[[fig:key]]` ใน `md`
> ตัวช่วยวาด `artifact/tools/svg.py` · ดูภาพก่อนใส่ `preview_figs.py` · `check_render.py <set> <lec> --shots <dir>` ถ่ายทุกภาพทั้งสองโหมด · กฎอยู่ใน SKILL §3b
> คาบที่มีภาพแล้ว: nephro 14 (19 ภาพ) · nephro 30 (20) · nephro Imaging (24) · hemonc 12/10 (17) · endo 14/10 (22) — **(16 ต.ค. · Version 27) ครบทุกคาบแล้ว: 31 คาบ 563 ภาพ**
>
> 🖼️ **รอบ 16 ต.ค. — เติมภาพ + กลไก ให้ 26 คาบเก่า** (ผู้ใช้ขอ "อธิบายรูปแทรกข้อความ ของทุกเลคเชอร์ อธิบายพวก pathophysiology")
> - เพิ่ม **461 ภาพ** + **152 ก้อนข้อความกลไก** (`#### ทำไมถึงมีอาการนี้` ตาราง อาการ | กลไก | ใช้แยกโรค หรือรายการลูกศร) — ทุกหัวข้อของ 26 คาบมีภาพอย่างน้อย 1 ภาพ
> - วิธีใส่: **`artifact/tools/apply_figs.py`** อ่านโมดูล `figs_<set>_<ชื่อ>.py` (มี `SET, LEC, INSERTS=[(section id, anchor, "fig:ชื่อฟังก์ชัน" หรือ markdown)]`) แล้วแทรกลง `md` + `figs` ของคาบที่ขึ้นเว็บแล้ว **ไม่ต้องรัน build_*.py ใหม่** · รันซ้ำได้ (ข้ามของที่มีแล้ว) · `--check` ตรวจโดยไม่เขียน · `--all` ทุกโมดูล
> - ⚠️ **ถ้ารัน build_<topic>.py ของคาบเก่าใหม่ ภาพจะหาย** (สคริปต์ลบคาบแล้วสร้างใหม่) → รัน `python3 artifact/tools/apply_figs.py --all` ต่อท้ายทุกครั้ง
> - แตะเฉพาะ `md` และ `figs` · ข้อความเดิมอยู่ครบตามลำดับ · ข้อสอบ/คำตอบ/id ไม่เปลี่ยน → ความคืบหน้าที่ผู้ใช้ทำไว้ไม่เพี้ยน · `check_lecture.py` ได้ 127 รายการเท่าเดิม (ของเก่าทั้งหมด ไม่มีใหม่) · `check_render.py` ทั้ง 26 คาบ ไม่มีปัญหาภาพ · `verify.py` ผ่าน
> - เนื้อหาในภาพ/ตารางกลไกที่ **ไม่ได้มาจากสไลด์** เป็นสรีรวิทยาระดับตำรา (Harrison/Guyton) · กราฟเชิงแนวคิดระบุใน cap ว่า "ภาพแนวคิด/ค่าประมาณ"
> - จุดที่ควรให้ผู้ใช้ตรวจ: ค่า Wilson ALP/TB ในคาบ GI 12/10 (< 2) ไม่ตรงกับคาบ 29/10 (< 4) — เป็นของเดิมในบทเรียน ไม่ได้แก้ · คาบ cardio 27 ภาพ BPG ระบุว่าบางแนวทางให้ทุก 3 สัปดาห์ในผู้เสี่ยงสูง (สไลด์: ทุก 3–4 สัปดาห์ · WHO 2024: ทุก 4 สัปดาห์)
> - **Version 28** (16 ต.ค.): หน้าเว็บแสดง ` · ` เป็นการขึ้นบรรทัดใหม่ (`splitDots()` ใน index.html · ตารางแยกเป็นบรรทัดละรายการ) — ผู้ใช้บอกว่าอ่านยาก · ข้อมูลไม่ได้แก้
> - **Version 30** (ก่อน 19 ต.ค. · session อื่น **publish โดยไม่ push**): เพิ่ม `section.anims` (ภาพเคลื่อนไหวกลไก `[[anim:key]]` เล่นทีละขั้น) และ `section.mnem` (กล่อง "หลักจำ") ให้คาบเดิมเกือบทุกคาบ + โค้ดใน index.html · **19 ต.ค. ดึงไฟล์จากเว็บเข้า repo แล้ว** (commit "Sync artifact with live learn") — สคริปต์ที่ใช้สร้าง anims/mnem ไม่อยู่ใน repo ถ้าต้องแก้ ให้แก้ข้อมูลใน data/*.json ตรง ๆ หรือหา branch ของ session นั้น
> - **Version 31** (19 ต.ค.): cardio 36 Basic ECG (คาบใหม่) · ทับบน Version 30 โดยไม่แตะคาบอื่น
> - **Version 33** (23 ต.ค.): คาบใหม่ chest **37 COPD (GOLD 2026)** · chest **Thoracentesis** (AL กลุ่ม 5) · nephro **22/10 Urethral catheterization** + เติมหัวข้อ/ข้อสอบจาก handout ใหม่ให้ neuro **9/10 LP** (+3 หัวข้อ) และ **21/10 ACS** (+4 หัวข้อ รวม delirium quiz) · แก้ตัวหนาที่ถูกตัดบรรทัดในคาบ 21/10 (check_lecture เหลือ 53 รายการ จาก 127) · ทับบน live 1792427940-73a8 (anims/mnem ของ session dashboard อยู่ครบ — ตรวจทุกหัวข้อก่อน publish)
>   - **Version 39–42** (26 ต.ค. · session อื่น): หมายเหตุขอบเขต GRACE ใต้หัวข้อ cardio-ihd-09 + คำอธิบาย CAR-IHD-MCQ-13 (ตอบคอมเมนต์ผู้ใช้ "For only unstable angina") · index.html บนเว็บมีแพตช์เพิ่ม — ดึง index.html, data/cardio.json และ build_ihd.py เข้า repo แล้ว (ฐานงานถัดไป = v42 `1793000238-7fee`) · มี session อื่นกำลังทำคาบผิวหนัง skin infection (branch `claude/lecture-artifact-integration-5plhhc`) — ถ้าจะแตะ derm.json ให้เช็คก่อน
>   - **Version 36–38** (25 ต.ค. · session Lecture Dashboard `claude/intelligent-brown-xj38me`): hemonc **9/11 Anemia** + **PBS** atlas (รูปจริง `img/pbs/*.jpg` อยู่บนเว็บเท่านั้น ไม่อยู่ใน repo — publish ครั้งต่อไปอย่าส่ง `img/` เป็น null) · `[[img:key]]` + `section.imgs` · ปุ่ม **"ปิดเพื่อทวน"** เหนือทุกตาราง (ตอบคอมเมนต์ผู้ใช้ 25 ต.ค.) — ดึงเข้า repo แล้ว (66fa9d9) · ผมทำโหมดปิดป้ายสำหรับ **ภาพ SVG/ภาพเคลื่อนไหว** ไว้ใน commit 7947979 แต่ไม่ได้ publish (ซ้ำกับของตาราง) — ถ้าผู้ใช้อยากได้กับภาพ ให้ดึงบล็อก `clz*` จาก commit นั้น ตัดส่วนตารางออก
>   - **Version 35** (24 ต.ค.): **ชุดใหม่ Derm** (`data/derm.json` + entry ใน index.json สีเดียวกับ Drill) คาบ **Derm1** Common skin diseases ← อ.ภูริต (Purit Pureesrisak) สไลด์ปี 2566 — ไฟล์ Drive "Lec นศพ ปี 4 (66).pdf" `1PWIdpHHF6dsoLSsPoJhJgsdE9mJWTzH8` (118 MB สแกนจาก iPhone · อ่านจากภาพทุกหน้า) · `build_derm.py` + `figs_derm.py` · โน้ต `slides/derm66_notes.md` (มีลายมือ ✍️)
>   - **Version 34** (23 ต.ค.): nephro **Physio1 / Physio2** สรีรวิทยาไตพื้นฐาน (ผู้ใช้ส่ง "basic physio of nephro" — สไลด์ MDS215 ม.รังสิต Part I/II, Drive `1IHnFaFvZeNbKXeE_RRpnwHLTP6zEEYwO` และ `1-i_hPZrlM-oGSyas0WZCslQRWyJyVtGw`) วางไว้ต้นชุดก่อนคาบ 05 · สคริปต์ `build_renalphys1.py`/`build_renalphys2.py` (แทรกตำแหน่งเอง ไม่ sort — **ต้องรัน Physio1 ก่อน Physio2**) · ⚠️ build_catheter.py และสคริปต์ nephro เก่าบางตัว sort คาบ → รันแล้ว Physio1/2 จะไปอยู่ท้าย ให้รัน build_renalphys1 → 2 ต่อท้าย
>   - ผู้ใช้ขอ COPD "ตามความรู้ที่ NL ต้องการก็พอ ที่เหลือเป็นอ่านเพิ่มเติม" → หัวข้อ 1–11 = ระดับ NL · หัวข้อ 12–14 ชื่อขึ้นต้น "อ่านเพิ่มเติม" · ทำด้วย `build_copd.py` + `figs_copd.py` (โน้ต `slides/copd_notes.md`)
>   - ⚠️ `build_copd.py` เขียน `intro`/`howto` ของชุด chest ทับทั้งก้อน — ข้อความในสคริปต์รวม Thoracentesis ไว้แล้ว ถ้าเพิ่มคาบ chest ใหม่ต้องแก้ INTRO/HOWTO ในสคริปต์นี้ด้วย
>   - neuro 9/10 และ 21/10 อัปเดตด้วย `update_neuro_handouts.py` (รันซ้ำได้ · คง anims/mnem · ต่อบรรทัดที่ตัวหนาคร่อม) ไม่ต้องรัน build_lp/build_acs ใหม่
>   - `check_render` แจ้ง "ข้อความทับ" ใน neuro 9/10 และ 21/10 เฉพาะภาพเคลื่อนไหว (anims ของ session dashboard — ข้อความของทุกขั้นซ้อนกันในไฟล์ แต่แสดงทีละขั้น) ไม่ใช่ภาพนิ่ง
> - **Version 29** (16 ต.ค.): ปุ่ม **"ซ่อนเนื้อหา (โหมดทวน)"** ต่อคาบ (หน้าคาบ + หน้าหัวข้อ) → เหลือแค่หัวข้อ ### / #### เป็นปุ่มกดเปิดทีละส่วน + "จำไปสอบ" พับไว้ · ซ่อน summary · ข้อสอบยังอยู่ · จำค่าใน `state.hide` (localStorage ต่อเครื่อง ไม่ซิงก์บัญชี)
> - `index.html` บนเว็บ v26 มีแพตช์ CSS ปุ่มซ่อนเมนู (จาก `claude/internal-med-learning-web-j9ca6l`) — รวมเข้า repo แล้ว (commit 0ab309b)
>
> 👤 **Version 22–23 มาจาก session dashboard (`claude/intelligent-brown-xj38me`)**: v22 บันทึกความคืบหน้าในบัญชี (`patch_learn_sync.py` · capability `db`+`user` — **ห้าม publish โดยส่ง `capabilities` ที่ไม่มีสองตัวนี้**) · v23 แท็บ "คาบเรียน" (`patch_learn_lectures.py`)
> repo ซิงก์ `artifact/index.html` กับหน้าเว็บ v23 แล้ว (commit 53491e2) — แก้หน้าเว็บต่อจากไฟล์นี้ได้เลย
>
> 🔗 **index.html บนเว็บมีโค้ด deep link** (`#<ชุด>-<คาบ>` จาก Lecture Dashboard · `patch_deeplinks.py` ใน branch `claude/intelligent-brown-xj38me`) — รวมเข้า repo แล้ว (Version 21)
> `compare_live.py` เทียบ index.html ด้วยแล้ว (ถอด wrapper ของบริการ) → **ต้อง read `index.html` มาเทียบทุกครั้งก่อน publish index.html**
เป็นเว็บเรียนเนื้อหา + คลังข้อสอบ MCQ/MEQ/OSCE สำหรับรอบ Internal Medicine
(MED421/422 · 14 ก.ย. – 22 พ.ย. 2569 · รพ.ราชวิถี · สอบลงกอง 17–18 พ.ย.)

**ผู้ใช้:** นักศึกษาแพทย์ปี 4 (nutt.spider@gmail.com)

**ตารางเรียนจริง** (จาก Google Calendar): 44 Lecture · 13 Bedside · 8 Teaching Round

---

## 2. ที่อยู่ไฟล์

```
/home/user/ioioioio/          ← repo · ฉบับล่าสุดอยู่ที่ claude/add-today-blougl = claude/keen-brahmagupta-nqy0my (commit เดียวกัน)
├── artifact/                  ← ต้นฉบับ artifact (publish จากที่นี่)
│   ├── index.html             ← หน้าเว็บ (43 KB)
│   ├── README.md              ← วิธีเพิ่มคาบใหม่ + schema ย่อ
│   ├── data/
│   │   ├── index.json         ← รายชื่อชุดวิชา + ชื่อไฟล์ + จำนวนคาบ
│   │   ├── nl.json            ← พจนานุกรม นล. 1,389 รหัส (472 KB)
│   │   ├── air.json (3 คาบ)   cardio.json (3)  chest.json (4)
│   │   ├── nephro.json (1)    neuro.json (5)
│   │   ├── endo.json (2)
│   │   └── id.json (1)        ← ชุดใหม่ 2 ต.ค. (build_sepsis.py สร้าง entry ใน index.json ให้เองถ้ายังไม่มี)
│   └── tools/                 ← (14 ต.ค.) build_diabetes.py + figs_diabetes.py · (13 ต.ค.) build_glomerular.py + figs_glomerular.py · build_uti.py · build_renalimg.py · build_wbc.py ·
│                                 svg.py (ตัวช่วยวาดภาพ) · preview_figs.py (ดูภาพก่อนใส่) ·
│                                 build_acs.py · build_cns.py · build_epilepsy.py · build_eptb.py ·
│                                 build_ihd.py · build_lp.py · build_mets.py · build_rfpleural.py ·
│                                 build_thyroid.py · build_sepsis.py · map_nl.py · refactor.py ·
│                                 verify.py (ทดสอบด้วย Playwright — ต้องผ่านก่อน publish · นับแท็บจาก index.json เอง)
├── nl/                        ← งานแกะเกณฑ์ นล. (เสร็จแล้ว ไม่ต้องทำซ้ำ)
│   ├── vis/056.txt–074.txt    ← ผลอ่านภาค ข. ด้วยสายตา
│   ├── visA/010.txt–047.txt   ← ผลอ่านภาค ก. ด้วยสายตา + _scheme.md (โครงรหัส)
│   ├── nl_partB.json (511)  ·  nl_partA.json (698)
│   ├── build_vis.py · build_visA.py   ← vis*/ → nl_part*.json
│   └── merge_full.py          ← รวมทั้งสองภาคเข้า artifact/data/nl.json + แก้รหัสผิด
├── refs/curriculum-topics-2569.md  ← หัวข้อตามหลักสูตรทางการ
├── slides/SOURCES.md          ← รายการไฟล์สไลด์ที่ได้รับและ Drive file id
├── slides/eptb_notes.md       ← โน้ตอ่านสไลด์ Extrapulmonary TB ทีละหน้า (16 หน้า + ลายมือ)
├── slides/rf_pleural_notes.md · thyroid_notes.md · sepsis_notes.md  ← โน้ตรอบ 2 ต.ค.
└── (ของเดิมคนละสาย: drill.html · learn.html · build.py · data/ · export/)
```

> ⚠️ **ไฟล์ทั้งหมดอยู่ใน repo แล้ว ไม่ได้อยู่ใน `scratchpad/` อีกต่อไป**
> รอบที่แล้ว container ถูกคืนไปจริงและ `scratchpad/` หายทั้งหมด — งานไม่หายเพราะ commit ไว้ครบ
> `NL_syllabus.pdf` และ `nl/img*/` ไม่ได้ commit (โหลด/เรนเดอร์ใหม่ได้)

**แผนรายสัปดาห์เต็ม:** `/root/.claude/plans/google-calendar-humming-dijkstra.md`

---

## 3. โครงสร้างข้อมูล (schema — ต้องทำตามเป๊ะ)

```
lecture: { lec, title, subtitle, objectives[], sections[], meq[], osce[],
           nlGap?, guidelines?[] }
section: { id, title, summary, minutes, nl[], md, pearls[], items[] }
item:    { id, kind:"mcq"|"old", stem, choices[5], answer(0-4), explain,
           pearl, topic, src, ref[], nl[] }
```

**ข้อควรระวัง:**
- markdown parser ในหน้าเว็บ **ไม่รองรับ code fence** (```) — ห้ามใช้ ใช้ตารางแทน
- `answer` เป็น index เริ่มที่ 0
- `id` ห้ามชนกัน รูปแบบ `<SET>-MCQ-nn` และ `<set>-<lec>-nn`

**สูตรเพิ่ม 1 คาบ:** เขียน `build_<ชื่อ>.py` → merge เข้าไฟล์ set → อัปเดต `lectureCount`
ใน `index.json` → `python3 verify.py` → `Artifact publish` ด้วย `url` + `root` + `files`

**ต้นทุน:** 1 คาบเต็มรูปแบบ (10 sections + ~28 MCQ + MEQ + OSCE) ≈ **41k tokens**

---

## 4. คาบที่ทำเสร็จแล้ว 26 คาบ

| set | lec | เรื่อง |
|---|---|---|
| air | 08 | Allergy and clinical immunology |
| air | 23 | Approach to arthritis / crystal and infective |
| air | 33 | Connective tissue disease, vasculitis (18 หัวข้อ — เติมส่วนที่ขาดจากสไลด์ อ.พรรณนิภา ครบแล้ว) |
| cardio | 04 | Inflammatory MyoPericardial Syndrome (IMPS) |
| cardio | 10 | Circulatory Shock |
| cardio | 13 | Ischemic heart disease (CCS→STEMI) ← อ.สุรพันธ์ · พฤ. 24 ก.ย. (เดิมใช้เลข 24/9 — เปลี่ยนเป็นเลขคาบจริงจากคลัง Ward Drill แล้ว · ผูกคลังคาบ 13 ครบ 32 ข้อ ด้วย `tools/link_ihd_bank.py`) |
| cardio | 24 | Atrial fibrillation ← อ.อภิชัย · จ. 5 ต.ค. (11 หัวข้อ · 20 MCQ ใหม่ + คลังคาบ 24 ครบ 21 ข้อ · MEQ AF RVR + warfarin · OSCE counselling warfarin) |
| cardio | 27 | Valvular heart disease + Acute rheumatic fever ← พ.ญ.ชนัญญา · อ. 6 ต.ค. (13 หัวข้อ · 18 MCQ ใหม่ + คลังคาบ 27 ครบ 31 ข้อ · MEQ ARF ใหม่ + C-MEQ-02 · OSCE C-OSCE-04) — **ผู้ใช้ขอให้อัปเดตตามแนวทางล่าสุด**: ESC/EACTS 2025 (VHD) · WHO 2024 + Jones 2015 (ARF) · ESC 2023 + Duke-ISCVID 2023 (IE — ไม่อยู่ในสไลด์ แต่มีในคลัง 7 ข้อ) · ลายมือบนสไลด์อ่านไม่ได้ |
| cardio | 36 | Basic ECG และ arrhythmia ที่พบบ่อย ← อ.สุรชาติ · จ. 19 ต.ค. (14 หัวข้อ · 28 MCQ ใหม่ + คลังคาบ 36 ครบ 23 ข้อ · MEQ inferior STEMI + CHB · OSCE บันทึก 12-lead + Brugada leads + C-OSCE-02/03 · **28 ภาพ ECG วาดจริงบนกระดาษกราฟ** จาก `figs_ecg.py`) — PDF 37.8 MB อ่านได้เฉพาะข้อความ (ภาพ ECG ในสไลด์มองไม่เห็น · ลายมือ OCR เป็นเศษคำ ใช้เฉพาะที่ตีความได้) · **หัวข้อ 7 (ACLS) และการรักษา AV block/hyperK ไม่อยู่ในสไลด์** → AHA ACLS 2020 + 2023 · ESC SVT 2019 · ACC/AHA/HRS 2018 · 4th UDMI · ESC ACS 2023 |
| chest | 03 | Pulmonary tuberculosis |
| chest | 26 | Arterial blood gas analysis |
| chest | 23/9 | Extrapulmonary TB ← อ.ภาณุวัฒน์ (12 หัวข้อ · 33 MCQ · MEQ TB peritonitis · SAQ body fluid) |
| chest | 17 | Respiratory failure + Pleural disease ← อ.สกล (12 หัวข้อ · 36 ข้อ รวมคลังคาบ 17 ครบ · CH-MEQ-03 · CH-OSCE-02/04) |
| chest | Thoracentesis | Thoracentesis และการแปลผลน้ำ ← Active learning กลุ่ม 5 (12 หัวข้อ · 26 MCQ + MOCK-137/138/142 · MEQ · OSCE หัตถการ · **21 ภาพ**) — BTS 2023 · สไลด์นักศึกษามีจุดผิดบางจุด แก้ตามแนวทางและระบุในบทเรียน |
| chest | 37 | COPD ← อ. 20 ต.ค. · เรียบเรียงจาก **GOLD 2026** (14 หัวข้อ = NL 11 + อ่านเพิ่มเติม 3 · 30 MCQ + คลังคาบ 37 อีก 8 · MEQ AECOPD + CH-MEQ-02 · OSCE inhaler · **20 ภาพ**) — บางหน้าของ GOLD PDF อ่านไม่ได้ (ภาพ) · ส่วน pneumonia/asthma ของคาบ 37 ในคลังยังไม่มีบทเรียน |
| nephro | Physio1 | สรีรวิทยาไตพื้นฐาน I — การทำงานของไต RBF/GFR clearance การขนส่งในท่อไต concentrating (14 หัวข้อ · 29 MCQ + MOCK-147/165/169/179/181 · MEQ NSAID+ACEi+thiazide · OSCE คำนวณ clearance/FENa/CH2O · **23 ภาพ**) — PDF อ่านได้แค่ข้อความ ภาพในสไลด์ (สมการ eGFR, แผนภาพเซลล์ท่อไต, countercurrent) วาดใหม่จาก Guyton/Boron · ส่วนจากตำราติด "(ตำรา)" ในเนื้อหา · จุดที่สไลด์ดูคลาดเคลื่อนมีหมายเหตุแก้ |
| nephro | Physio2 | สรีรวิทยาไตพื้นฐาน II — tonicity, Darrow–Yannet, Na/ADH/RAAS/ANP, SIADH, K, Ca/Pi/Mg, กรด-ด่าง + วิเคราะห์ ABG, micturition (15 หัวข้อ · 30 MCQ + MOCK-135/170/173/180/198 · MEQ อาเจียน/gastric outlet · OSCE วิเคราะห์ ABG 3 ราย · **25 ภาพ**) — หัวข้อ 7 (SIADH/ODS, European 2014) และสูตร compensation/delta/osmolal gap เติมเอง · เฉลยแบบฝึก ABG 10 ข้อในสไลด์เขียนเอง (ข้อ 7 ค่าไม่เข้า H–H พอดี) |
| nephro | 05 | Fluid electrolyte: Divalent |
| neuro | 07 | Acute ischemic stroke |
| neuro | 23/9 | Epilepsy ← อ.พิมลพรรณ |
| neuro | 15/10 | CNS infection + CSF ← อ.พิมลพรรณ |
| neuro | 9/10 | หัตถการ LP + eye exam ← อ.พิมลพรรณ · **+ handout ใหม่ อ.ปองปวีณ์ (23 ต.ค.)** → 9 หัวข้อ · 19 MCQ · 17 ภาพ |
| neuro | 21/10 | Acute confusional state + alteration of consciousness ← อ.พิมลพรรณ · **+ handout ACS 2026 อ.เพชรรัตน์ + Delirium quiz (23 ต.ค.)** → 19 หัวข้อ · 45 MCQ · 29 ภาพ (เฉลย quiz ข้อ 1/3 อนุมานจากเนื้อหา — handout ไม่มีเฉลย) |
| derm | Derm1 | Common skin diseases for internists ← อ.ภูริต · สไลด์ปี 2566 (18 หัวข้อ: รอยโรค · eczema ทุกชนิด · contact · miliaria · urticaria · STD/syphilis · chancroid/GC/LGV · leprosy · EM/SJS/TEN · erythema nodosum · 45 MCQ + MOCK-008/016/058/059/060 · MEQ allopurinol SJS-TEN · OSCE บรรยายผื่น secondary syphilis + counselling · **32 ภาพ**) — สไลด์เก่ากว่าแนวทาง: GC ceftriaxone 125 mg → CDC 2021 500 mg · leprosy MDT เก่า → WHO 2018 สามตัวทุกราย · chronic urticaria → EAACI 2022 · แสดงทั้งสองแบบในบทเรียน |
| endo | 01 | Metabolic syndrome, Obesity, Dyslipidemia ← อ.นวพร (13 หัวข้อ · 35 MCQ · MEQ · OSCE ให้คำปรึกษาลดน้ำหนัก) |
| endo | 14/10 | Diabetes mellitus (Inc. DKA) ← ศ.นพ.ชัยชาญ · พ. 14 ต.ค. (15 หัวข้อ · 31 MCQ + MOCK-124/188–192 · MEQ DKA รายแรกของ T1 · OSCE ตรวจเท้าเบาหวาน · **22 ภาพ**) — **สไลด์ไม่มี DKA/HHS/hypoglycemia** → หัวข้อ 7–9 อิง ADA 2024 consensus + ADA 2009 + ADA SoC · KDIGO 2022 DM-CKD · IWGDF 2023 · ไม่มีคลัง Ward Drill (ชุด Endo) |
| endo | 14 | Thyroid disorders ← อ.ศิวกร (13 หัวข้อ · 26 MCQ · MEQ Graves · OSCE ตรวจคอ + counselling MMI) |
| id | 25/9 | Septicemia and antibiotic usage ← อ.พจน์ (11 หัวข้อ · 20 MCQ · MEQ obstructive pyelonephritis · OSCE ชั่วโมงแรก) — **อิง SSC 2026 เพราะสไลด์เป็นภาพล้วน** |
| id | 5/10 | AIDS and HIV infection ← พ.ญ.มนัสวี · จ. 5 ต.ค. (13 หัวข้อ · 27 MCQ · MEQ PCP/advanced HIV · OSCE pre-test counselling) — สไลด์ส่วนตาราง (WHO staging, สูตรยา, OI prophylaxis, crypto Rx) เป็นภาพ → อิงแนวทางไทย 2025/WHO และระบุในบทเรียน · ไม่มีข้อในคลัง Ward Drill |
| gi | 12/10 | Acute and chronic hepatitis ← อ.เฉลิมรัฐ · จ. 12 ต.ค. (11 หัวข้อ · 14 MCQ + MOCK-149/153 · MEQ acute HBV · SAQ HBV serology) — WHO 2024/EASL 2025 HBV · AASLD–IDSA HCV · EASL 2024 MASLD |
| gi | 27/10 | Approach to abdominal pain ← นพ.กิตติ · อ. 27 ต.ค. (11 หัวข้อ · 16 MCQ + MOCK-152/154–157/160/161 · MEQ gallstone pancreatitis · SAQ ปวดท้อง 6 ราย) — ACG 2024 AP · TG18 · ACG/CAG 2017 · Maastricht VI |
| gi | 29/10 | Liver function tests ← นพ.กิตติ · พฤ. 29 ต.ค. (8 หัวข้อ · 15 MCQ + MOCK-035/150 · MEQ paracetamol · SAQ แปล LFT 5 ราย) — ACG 2017 · EASL 2024 PBC · AASLD 2022 Wilson |
| hemonc | 12/10 | Approach to WBC disorder and lymphadenopathy ← อ.เบญจมาภรณ์ · จ. 12 ต.ค. (13 หัวข้อ · 32 MCQ + MOCK-044/056 · MEQ · SAQ อ่าน CBC · **17 ภาพ**) — สไลด์ 66 หน้าอ่านเป็นภาพรวมลายมือ · หัวข้อ 7 (acute leukemia/APL) แทบทั้งหมดเติมจาก Williams/WHO 2022/ELN 2022 · CML ELN 2020 · CLL iwCLL 2018 · Lugano 2014 |
| nephro | 14 | Approach to glomerular disease ← พญ.ฉันทิศา · พฤ. 1 ต.ค. (13 หัวข้อ · 24 MCQ + คลังคาบ 14 ครบ 27 + คาบ 28 อีก 8 (proteinuria/lipiduria/LN) + Mock 166–168/172/176/177 · MEQ MN+RVT · SAQ แปล UA 5 ราย · **19 ภาพ**) — ภาพพยาธิ/KDIGO 2021 MN algorithm/LN class ในสไลด์เป็นภาพ → KDIGO 2021 · KDIGO 2025 IgAN · KDIGO 2024 LN/AAV |
| nephro | 22/10 | Urethral catheterization ← พฤ. 22 ต.ค. (11 หัวข้อ · 24 MCQ · MEQ · OSCE ใส่สาย Foley ในผู้ชาย · **13 ภาพ**) — EAUN 2024 · BAUS-BAUN 2021 · CDC/IDSA 2009 CAUTI · EAU trauma/LUTS · การระบายปัสสาวะคั่งอ้าง Nyman 2010 (ยังไม่ได้ตรวจกับต้นฉบับ) |
| nephro | 30 | Urinary tract infection ← อ.กรทิพย์ · ศ. 18 ก.ย. (13 หัวข้อ · 31 MCQ + คลังคาบ 30 ครบ 22 + N-OLD-087/N-MCQ-26/N-OLD-074 + MOCK-011/019/020 · MEQ · SAQ · **20 ภาพ**) — สไลด์ภาพล้วนบางหน้าอ่านไม่ได้ · กลไกอาการ/CFU/prostatitis/recurrent/EPN เติมจาก IDSA 2011/2019/2025, EAU 2025, AUA 2019 · CAUTI ≥10² (สไลด์) เทียบ ≥10³ (IDSA) แสดงทั้งคู่ |
| nephro | Imaging | Essential renal imaging ← อ.ธนิศร (ไม่มีวันในปฏิทิน · ไม่ใช้เลข 19 เพราะคลังคาบ 19 = CKD) (14 หัวข้อ · 33 MCQ + คาบ 28: N-OLD-080–084, N-MCQ-27/28, N-OSCE-03 + MOCK-171/174/175/182 · MEQ · SAQ · **24 ภาพ**) — handout ไม่มีหน้าภาพ → หัวข้อ 5 (contrast/NSF), 7 (nuclear), 14 (ADPKD/mass) เติมทั้งหมดจาก ACR–NKF 2020/2021, ESUR 2018, KDIGO 2025 ADPKD, Bosniak |
| hemonc | 2/11 | General oncology ← พญ.ปิยวรรณ · จ. 2 พ.ย. (13 หัวข้อ · 29 MCQ + Mock 16 ข้อ (MOCK-021–029, 031–034, 036–038) · MEQ breast cancer + oncologic emergencies · SAQ ยาต้านมะเร็ง + ภาวะฉุกเฉิน) — **หัวข้อ 9–13 (markers คัดกรอง มะเร็งที่พบบ่อย ภาวะฉุกเฉิน) เพิ่มเองตามคำขอผู้ใช้ "ทำไม่ครบ" เพราะไฟล์มี Common cancer แค่เต้านม** · MOCK-030 myeloma เก็บไว้ให้คาบโลหิตวิทยา — GLOBOCAN 2022 · ASCO irAE 2021 · USPSTF 2024 · CDK4/6 · สไลด์ระบาดวิทยาเป็นภาพ |

> ⚠️ เลข `lec` แบบวันที่ (เช่น "23/9") เป็นตัวแทนชั่วคราว — **เลขคาบจริงดูได้จากฟิลด์ `lec` ใน `bank_merged.json`** (คลังเดียวกับ Ward Drill)
> ถ้าคาบนั้นมีข้อในคลัง ให้ใช้เลขนั้นและผูกข้อด้วย `artifact/tools/link_bank.py` (ดูตัวอย่าง `link_ihd_bank.py` และท้าย `build_af.py`)

**ส่งข้อจากบทเรียนเข้า Ward Drill** (14 ต.ค.) — `artifact/tools/drill_sync.py <checkout ของ claude/adoring-babbage-zkg8ih>` แล้ว `python3 build.py --no-pdf` ในนั้น
- ข้อใหม่ 151 MCQ + 10 MEQ/OSCE: nephro 14 (24) · 30 (31) · **IMG** (33) · heme **H04** (32) · endo **E05** (31) — คงลำดับตัวเลือกของบทเรียน (`mcq_late` ใน config ไม่สลับ ไม่ดึงเลขสุ่ม → ข้อเดิมทุกข้อในคลังเหมือน live 100%)
- แพตช์ template: ลิงก์ตรง `applyHash` (ของ live v11 จาก Lecture Dashboard) + โจทย์ MEQ/OSCE ที่มีตารางเรนเดอร์เป็นตาราง · เติม NL 67 รหัสใน refs ของ drill
- ✅ **Drill Version 18** (24 ต.ค.) — เพิ่ม derm **D03** (DERM-D1 45 + MEQ/OSCE 2) ต่อจาก D02 · ข้อเดิม 1294 ข้อไม่เปลี่ยน
- ✅ **Drill Version 17** (23 ต.ค.) — เพิ่ม nephro **PHY1** (29 + MEQ/OSCE 2) และ **PHY2** (30 + 2) ไว้ต้นชุด Nephro · ข้อเดิม 1231 ข้อไม่เปลี่ยน
- ✅ **Drill Version 16** (23 ต.ค.) — เพิ่ม chest **37** (CH-COPD 30 + MEQ/OSCE 2) · chest **THO** Thoracentesis (26 + 2 · แทรกหลังคาบ 17) · nephro **CATH** (24 + 2 · หลัง IMG) · neuro **LP** (19) และ **ACS** (45) (หลังคาบ 07 · MEQ/OSCE ของสองคาบนี้มีใน drill อยู่แล้ว) · ข้อเดิม 1081 ข้อไม่เปลี่ยน (0 removed / 0 changed) · blurb chest/nephro/neuro อัปเดต
  - **ขั้นตอน publish Drill ตอนนี้มี 3 ขั้น** (เพราะ session dashboard เพิ่มชุดรายคาบใน `dashboard/drill_sets/*.json`): `drill_sync.py /path/drillwt` → `build.py --no-pdf` ในนั้น → `python3 dashboard/drill_tool.py merge <drillwt>/drill.html dashboard/drill_sets <out.html>` → publish `<out.html>` (ไม่ส่ง capabilities) · `LEC_FIX` ใน drill_sync.py คงวันที่ที่ dashboard แก้ไว้
- ✅ **Drill Version 14** (19 ต.ค.) — เพิ่ม cardio 36 (CAR-ECG-MCQ 28 ข้อ + MEQ/OSCE 2) ผ่าน `drill_sync.py` (JOBS แถว cardio 36) · ข้อเดิมไม่เปลี่ยน
- ✅ **Drill Version 13** (17 ต.ค.) — บันทึกคำตอบในบัญชี `data/users/<id>/drill` (capabilities `{db:{}, user:{}}` · ใช้งานจริงแล้ว) + แท็บ "สุ่มทำข้อสอบ" (ระบบนี้/ทุกระบบ · 10–100 ข้อ · ทุกข้อ/ยังไม่เคยทำ/เคยตอบผิด) + แก้ป้ายยาวล้นจอมือถือ — ทั้งหมดอยู่ใน `drill_sync.py` · **publish drill ครั้งต่อไปต้องไม่ส่ง capabilities ว่าง** (ละไว้ = คงเดิม)
- ✅ **publish แล้ว Drill Version 12** (14 ต.ค. ผู้ใช้ยืนยัน) ที่ `Fdi5gcNXKqFLAXg4fQBV7X` · ไฟล์ข้อมูล drill ไม่ได้ commit ใน branch `adoring-babbage` → **ใครจะ build drill ใหม่จาก branch นั้น ต้องรัน `drill_sync.py` ก่อน publish** ไม่งั้นข้อพวกนี้และ applyHash จะหาย

**ความครอบคลุมคลัง Ward Drill** — ผูกเข้าบทเรียนแล้ว **423/570 ข้อ = 74% (23 ต.ค.)**: AIR 110/110 · Cardio 151/180 · Chest 72/106 · Nephro 90/174 (Mock 200 ข้อไม่ผูกคาบ — ผูกแล้ว 51 ข้อ) ·
คาบในคลังที่ยังไม่มีบทเรียน: Cardio 39 HT/HF · Chest 21 CXR/Occupational · 37 ส่วน Pneumonia/Asthma (COPD ทำแล้ว) · Nephro 19 CKD · 22 Dysnatremia/kalemia · 42 AKI ·
คาบ 28 (UA) เหลือ 4 ข้อ: N-MCQ-25, N-OLD-072, N-OLD-073 (cast/AKI) และ N-OLD-077 (Fanconi) — เก็บไว้ให้คาบ AKI/UA

---

## 5. พจนานุกรม นล. (สถานะปัจจุบัน)

`build/data/nl.json` = **1,389 รหัส · 472 KB** — ✅ **ครบทั้งเล่ม ฉบับ พ.ศ. 2567**

| ภาค | รหัส | ที่มา |
|---|---|---|
| ก. วิทยาศาสตร์การแพทย์พื้นฐาน (B1–B11) | 854 (รายการจริง 698 + หัวข้อหมวด 156) | หน้า 6–47 |
| ข. ความรู้ความสามารถทางวิชาชีพฯ | 535 (511 + หัวข้อหมวด 24) | หน้า 56–74 |

จำนวนรายการจริงภาค ก. แยกตามระบบ:
B1=143 · B2=53 · B3=93 · B4=54 · B5=40 · B6=46 · B7=47 · B8=52 · B9=35 · B10=68 · B11=67

ทุกรายการมี `code`, `part`, `section`, `system`, `group`, `title`, `page`, `source`

**ระบบรหัส:**
- ภาค ก.: `BX.1` โครงสร้าง/หน้าที่ (`.1.1` Structures · `.1.2` Functions · `.1.3` การเปลี่ยนแปลงตามช่วงชีวิต)
  `BX.2` สาเหตุ/พยาธิ/การวินิจฉัย → `.2.1` hereditary/congenital · `.2.2` infectious/inflammatory/immunologic ·
  `.2.3` traumatic/mechanical · `.2.4` neoplastic · `.2.5` metabolic/regulatory · `.2.6` vascular ·
  `BX.3` การสืบค้นโรค · `BX.4` ยาสมเหตุผล — ตารางแยก **ซ้าย = กลุ่มที่ 1 และ 2** / **ขวา = กลุ่มที่ 3** (`-3(n)`)
  (รายละเอียดเต็มที่ `nl/visA/_scheme.md`)
- ภาค ข.: `2.1.x` อาการสำคัญ (84) · `2.2.x` ภาวะฉุกเฉิน (50) ·
  `2.3.<ระบบ>(n)` โรคตามระบบ **กลุ่ม 2 = ดูแลเองได้** · `2.3.<ระบบ>-3(n)` **กลุ่ม 3 = วินิจฉัยแล้วส่งต่อ** ·
  `3.1/3.2/3.3` การตรวจ (52)

**วิธีแกะที่ใช้ได้จริง:** เรนเดอร์หน้าเป็น PNG 200 dpi แล้ว **อ่านด้วยสายตา** (Read tool)
→ แม่น 100% · ต้นทุน ~3.8k tokens/หน้า
**วิธีที่ล้มเหลว (อย่าทำซ้ำ):** tesseract OCR — ลอง 3 แบบ ได้ดีสุด 71% แย่สุด 37% ใช้ไม่ได้

### รหัสที่ไฟล์เดิมใส่ผิดและแก้ไปแล้ว
| รหัสเดิม | ควรเป็น | แก้กี่จุด |
|---|---|---|
| `2.3.4(20)` Tuberculosis | `2.3.1(20)` | 38 |
| `2.3.12(12)` Urticaria | `2.3.12(14)` | 5 |
| `2.3.12(13)` SJS/TEN | `2.2.49` | 5 |
| `B5.2.2-3(2b)` Vasculitis | `B5.2.2-3(6)` | 10 |
| `B5.2.2-3(3b)` Osteomyelitis | `B5.2.2-3(7)` | 5 |

### ข้อผิดพลาดในตัวเอกสารแพทยสภาที่พบ (บันทึกไว้ใน title)
- `B1.6.4` ถูกใช้ซ้ำสองหัวข้อ (Neoplasm และ Adaptation to environmental extremes) → เก็บอันหลังเป็น `B1.6.5`
- `B5.2.2` กลุ่ม 3 นับ (1)–(5) จบหน้า 27 แล้วขึ้นหน้า 28 **เริ่มนับใหม่ที่ (2)** → เรียงต่อเป็น (6)(7)(8)
  (ตรวจซ้ำด้วยการ crop ภาพที่ 400 dpi แล้ว ยืนยันว่าเอกสารพิมพ์แบบนั้นจริง)
- `B11.2.6` พิมพ์เป็น `11.2.6` ขาด B
- หัวข้อ 2.2 เขียนว่า "49 รายการ" แต่เลขไล่ถึง 2.2.50

ตรวจแล้ว: รหัสที่ 13 คาบอ้างถึง 136 รหัส → พบในพจนานุกรมครบ 136 ไม่มีรหัสลอย · ทุก build_*.py assert รหัสกับ nl.json ก่อนเขียน
(รอบ 2 ต.ค. พบรหัสผิดในคลัง: `2.3.5-3(1)` = bipolar ถูกใส่ในข้อมะเร็งปอด → build_rfpleural.py ตัดทิ้ง)

---

## 6. ไฟล์สไลด์ที่ได้รับแล้ว

**รอบ 14 ต.ค. (โฟลเดอร์เดิม)** — ✅ v24 · 2026 Diabetes lecture Student (ศ.นพ.ชัยชาญ) `1FB1Oe9v_DWc46H1Y37gi7Gu1ZbPcWdtH` → endo 14/10 · โน้ต `slides/diabetes_notes.md` · ข้อความครบ ภาพ/กราฟอ่านไม่ได้

**รอบ 13 ต.ค. (โฟลเดอร์เดิม `17s6Doub5Ez41F8q69KQa4lf-pWAzfFDj` · ผู้ใช้เพิ่ม 4 ไฟล์)** — ✅ v21 · ทำพร้อมกันด้วย subagent 3 ตัวใน git worktree แล้ว merge
- Lec11 Approach to glomerular disease (พญ.ฉันทิศา) `1R5f1MtTJIlwCUeomxvcBD10MKpDzYob4` → nephro 14 · โน้ต `slides/glomerular_notes.md` · ข้อความครบ ภาพอ่านไม่ได้
- Lec5 UTI_4thRSU2026 (อ.กรทิพย์) `1OeevfDxn_c6H3iLUw6nXIjPOv6DPHawD` → nephro 30 · โน้ต `slides/uti_notes.md`
- Lec19 Essential Renal Imaging handout (อ.ธนิศร) `1NHjoGyLcAer6GbmfEp9FEXBw4F_8xmAN` → nephro Imaging · โน้ต `slides/renalimg_notes.md`
- Basic electrocardiography outline (อ.สุรชาติ) `13UUiw9BU7zag_JNHWBmidA5gPoVhjTiu` (37.8 MB · 113 หน้า) → cardio 36 · โน้ต `slides/ecg_notes.md`
- Lec22 Approach to WBC disorder and lymphadenopathy (อ.เบญจมาภรณ์) `1VtpxDAfvwYkpJPIrqs19s7JoLJU-hA6V` → hemonc 12/10 · โน้ต `slides/wbc_notes.md` (ไฟล์นี้ดาวน์โหลดผ่าน public link ได้ → เรนเดอร์อ่านได้ครบ 66 หน้า)

**รอบ 6 ต.ค. (โฟลเดอร์ Drive `17s6Doub5Ez41F8q69KQa4lf-pWAzfFDj`)** — ✅ v18 · ทั้ง 4 ไฟล์ดึงข้อความด้วย `read_file_content` ได้
- Acute and chronic hepatitis (อ.เฉลิมรัฐ) `1X6QMVuq2GWT3SLbV9VactnQ11MVtml98` → gi 12/10 · โน้ต `slides/hepatitis_notes.md`
- Approach to abdominal pain 65 (นพ.กิตติ) `10g5J-s6Zv5JZB3RbHs6dh2QWUR5Xzr5V` → gi 27/10 · โน้ต `slides/abdpain_notes.md`
- Liver Function Tests 63 (นพ.กิตติ) `1HWt4TMmRmpgSw8lT_NIjt74YQ5LC-zJ3` → gi 29/10 · โน้ต `slides/lft_notes.md`
- Lec 1 General Oncology (พญ.ปิยวรรณ) `1nzh5iBJ_uJ5uP9_q2zDlAxQ-Opw5xRJg` (19.5 MB) → hemonc 2/11 · โน้ต `slides/oncology_notes.md` · กราฟ GLOBOCAN 2012/มะเร็งไทยเป็นภาพ → ใช้ GLOBOCAN 2022 และระบุไว้

**พ.ญ.ชนัญญา** — VHD + ARF ✅ Drive `1IVsvzRiGSfwCrfi6wcJt49fkwP4Zfzq2` · ข้อความครบ ลายมืออ่านไม่ได้ · โน้ต `slides/vhd_arf_notes.md`

**พ.ญ.มนัสวี** — AIDS and HIV infection ✅ Drive `13PhGovTDoDXERCeB2zfMC1_1nZq2mAlJ` (25 MB) · ข้อความดึงได้เฉพาะสไลด์ตัวอักษร · โน้ต `slides/hiv_notes.md`

**อ.อภิชัย ปกวัฒนา** — Atrial fibrillation (update 16 Nov 2025) ✅ Drive `1zK9eofxHl5ldCi-5IqIjyTStGVHYhlRO` · ดึงข้อความด้วย `read_file_content` ได้ครบ · โน้ต `slides/af_notes.md`

**อ.ภาณุวัฒน์ (Panuwat Wongkulab)** — Extrapulmonary TB: The Hidden Pathogen (Apr 2026) ✅
- ผู้ใช้อัปโหลดในแชทเป็น PDF ภาพล้วน 16 หน้า (ไม่อยู่ใน Drive) → อ่านด้วยสายตา โน้ตเต็มที่ `slides/eptb_notes.md`
- ⚠️ ไฟล์ bank `CH-MCQ-20` และ `CH-OSCE-04` (pleural/ADA) ของคาบ 17 อ.สกล ยังว่าง — ตั้งใจไม่ใช้ในคาบ EPTB เพื่อเก็บไว้ให้คาบเยื่อหุ้มปอด

**อ.พิมลพรรณ** (เจ้าของ paranee.k@rsu.ac.th) — ✅ **ใช้ครบทั้ง 4 ไฟล์แล้ว**
- Epilepsy `1tWDtfQ-ZA-tDDR1_YgGkYgyS-4md6hQ5` ✅
- CNS infection `1dnFAWEZRkkzF7MgbJ487vU1Jv9pNZHjp` ✅
- LP + eye exam `13UzOj8-vMSv_P3cQqg06033ws9NV9w2l` ✅
- Acute Confusional State `1JtJeNHGY-Fls5CiGvIpwx2lp8FfUIi8g` ✅ (W6 · 21 ต.ค.)

**อ.สุรพันธ์ พงศ์สุธนะ** (Cardiology) — รวมเป็นคาบเดียวแล้ว ✅
- CAD complete2019 `1Pcst0l92BATWKClV00umsyNQXgdFvD4k` (ยังไม่ได้อ่าน — สำรองไว้)
- Chronic coronary syndrome 2019 `1BqP50Nbbuw2BszsHKNoDnLeFlA4eoPWJ`
- NSTEMI 2020 `17iNJA1PvpedUAz8wyM4CzZBU1MAy1EdI`
- STEMI2017 `1j-EtRG61awYlCMKRx-q9MKymdhYF2BAA`

**อ.นวพร นภาทิวาอำนวย** (Diabetes & Metabolism) — ✅ ใช้แล้ว (ชุด Endo คาบ 01)
- Lec 1 2026 MS, obesity, DLP Handout `1ttUNtkD5EXmVXVIhKuScn4Y6wOV9-yQe` (15 MB · อยู่ใน Drive ผู้ใช้เอง)
  ⚠️ `read_file_content` ได้ข้อความถึงสไลด์ DLCN แล้วหยุด — ส่วนรักษา dyslipidemia ดึงไม่ได้
  ดาวน์โหลดตรงก็ไม่ได้ (proxy 403) → หัวข้อ 11–13 ของคาบนี้ใช้ ESC/EAS 2019 แทนและระบุไว้ใน `nlGap`
  ถ้าผู้ใช้ส่งภาพสไลด์ส่วนนั้นมา ให้เทียบแล้วแก้ `build_mets.py`

**รอบ 2 ต.ค. (โฟลเดอร์ Drive "Claude" `1mft-8EhUVLSAXIwVX7zV6JmHoiaBPzsM` ของผู้ใช้)** — ✅ v14
- Lec12 Respiratory failure, pleural disease `12_uIP-b1TWP-u35yfm90Q9PT5QTNgPvp` → chest คาบ **17** (ใช้เลขคาบตามคลังข้อสอบ ไม่ใช่ "Lec12")
  ⚠️ ข้อความถูกตัดหลัง work up pleural effusion → Light's/empyema/malignant/การรักษา PTX ไม่ tension ใช้ BTS 2023
- Lec14 Thyroid disorder_2026 `1iq1YOO-vf-JF3vL40p1ppCmu-1eHnII5` → endo คาบ **14**
  ⚠️ ข้อความถูกตัดหลัง nodule algorithm → hypothyroid/amiodarone/Bethesda เทียบจาก artifact บทเรียน Thyroid ของผู้ใช้
  (claude.ai/artifact/S9FmtzVewjtqtWxnuNQxRu — ทำจากสไลด์ชุดเดียวกันใน session อื่น) · thyroid storm ใช้ ATA/JTA 2016
- Sepsis _ Principle ATB `10qgsfnxQl7wacVkNBSAF5SXe8Bx4vPDc` (175 MB **ภาพล้วน** · read_file_content ว่าง) → id คาบ 25/9
  ใช้ SSC 2026 (ตรวจกับ sccm.org แล้ว) + artifact Sepsis ของผู้ใช้ (claude.ai/artifact/DB59ZbY5ize8MhxXiHkZJZ) · **ถ้าได้ภาพสไลด์มาให้แก้ build_sepsis.py**
- Lec7 Epilepsy `1stF_hQlkx8nCxnE07W3lKHCBsT5alFhW` = สไลด์ชุดเดียวกับคาบ Epilepsy ที่ทำแล้ว (มีลายมือ) → ไม่สร้างซ้ำ
- ผู้ใช้มี artifact บทเรียนแยกต่อหัวข้อใน "ห้องสมุดท่าอาจารย์" (claude.ai/artifact/QebhLmV2eKyzj3mkqstnjR) — ใช้เป็นแหล่งเทียบได้เมื่อสไลด์ดึงไม่ครบ
- ตำแหน่งเฉลย: build ใหม่ทั้งสามสลับตัวเลือกแบบคงที่ด้วย random.Random(id) — คลังเดิม (CH-MCQ/CH-OLD) เฉลย ก. ทุกข้อ

**เข้าไม่ถึง (น่าจะอยู่บัญชี @rsu.ac.th):**
- UTI `1GG55VJ6ddTMQ2IETf1IqUpU_tMDizEH7`
- Tropical disease `1ax8FzPhmAZ4iFSSsXGQcb5TGobcG4nn9` (ผู้ใช้สั่งข้าม Malaria ไปก่อน)

**NL Syllabus** `143DRB8wSwIfDvji6OfC--FRIUitv7kbm` → โหลดมาแล้วที่ `nl/NL_syllabus.pdf`

---

## 7. งานที่ค้าง (เรียงตามลำดับที่ตกลงกันไว้)

1. W1: ✅ UTI (v21) · Malaria (ผู้ใช้สั่งพัก)
2. W2 เหลือ: Skin infections · Nephrotic/Nephritis — ✅ Extrapulmonary TB (v12) · ✅ Dyslipidemia/MetS/Obesity (v13) ·
   ✅ Septicemia (v14 · อิง SSC 2026 รอภาพสไลด์จริง) · ✅ Pleural/Resp failure (v14) · ✅ Thyroid (v14)
3. W10 แท็บ "ทบทวนก่อนสอบ" (~50k tokens)

> ✅ **งานเกณฑ์ นล. เสร็จสมบูรณ์แล้ว** ไม่ต้องอ่าน PDF ซ้ำอีก
> ✅ **สไลด์ของ อ.พิมลพรรณ ใช้ครบทุกไฟล์แล้ว** — คาบที่เหลือรอสไลด์จากอาจารย์ท่านอื่น

**เสนอไว้แต่ยังไม่ได้ทำ:** อ่าน CAD complete2019 เพิ่มรายละเอียด · ใส่ `guidelines` ให้ 9 คาบแรก ·
เพิ่มหัวข้อ status epilepticus ในคาบ Epilepsy

---

## 8. คำสั่ง/ข้อตกลงจากผู้ใช้ที่ยังมีผล

- **ประเมิน token ทุกครั้ง** ที่จะสร้างของใหม่
- เนื้อหา **เต็มรูปแบบทุกคาบ** (ไม่ย่อ)
- **ไม่ยุบรวม** artifact เก่า 5 อัน ปล่อยแยกไว้
- ทุกคาบต้องมีป้ายว่า **ครอบคลุมจุดประสงค์ นล.** · ถ้าหัวข้อไหนไม่มีรหัส นล.
  ให้หา **guideline ปัจจุบัน** มาทำเป็นสื่อการสอนแทน (ใส่ใน `nlGap` + `guidelines[]`)
- ใช้ `MED421 learn` เป็น artifact หลักเสมอ

---

## 9. รายละเอียดทางเทคนิคที่เคยติดปัญหา

- **Playwright:** container ใหม่ยังไม่มีโมดูลติดตั้ง — ต้อง `pip install --break-system-packages playwright` ก่อน (เบราว์เซอร์มีอยู่แล้ว
  ห้ามรัน `playwright install`) · ต้องระบุ `executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"`
  และ `args=["--no-sandbox"]` · Google Fonts โดน proxy บล็อก (ERR_CERT_AUTHORITY_INVALID หรือ ERR_TUNNEL_CONNECTION_FAILED — verify.py กรองทั้งสองแบบแล้ว)
  เป็นเรื่องปกติของ container ไม่ใช่บั๊ก
- **`check_render.py` / `verify.py` ใช้พอร์ตตายตัว** (8934 ฯลฯ) — ถ้ารันหลาย agent พร้อมกันจะชนกัน ให้รันทีละตัวหลัง merge
- **subagent ใน worktree** (`.claude/worktrees/` ใส่ไว้ใน `.git/info/exclude`) — ให้แต่ละตัว commit ใน worktree แล้ว `git checkout <branch> -- build_x.py notes.md` มารันใน tree หลัก ตาม build ทีละตัว
- **อย่าใช้ `pgrep -f <script>` ในลูปรอ** — มันแมตช์ตัว bash command เองแล้วค้างตลอดกาล
- แถบความคืบหน้านับเฉพาะ set ที่เปิดอยู่ (AIR = 34 ไม่ใช่ 91) — เคยเข้าใจผิดว่าเป็นบั๊ก
- `.nav .btn` เคยล้นจอที่ 390px เพราะ `white-space:nowrap` → แก้แล้วด้วย
  `white-space:normal;text-align:left;max-width:100%`
- สีป้ายกลุ่ม 2/3 ใช้ตัวแปร `--ok/--ok-soft` และ `--miss/--miss-soft` ที่มีอยู่แล้ว
  จึงถูกต้องทั้งโหมดสว่างและมืดโดยอัตโนมัติ
