# MED421 — สรุปสถานะงานทั้งหมด (อัปเดต 28 ต.ค. 2569)

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
cd /home/user/ioioioio
git add -A && git commit -m "<สรุปสั้น ๆ ว่าทำอะไร>"
git push -u origin claude/internal-med-learning-web-j9ca6l
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

## 1. ตัวงานหลัก

**artifact:** `MED421 learn` — https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE (ปัจจุบัน — ดูเลขล่าสุดจาก Artifact action:list เสมอ)

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
/home/user/ioioioio/          ← repo · branch claude/internal-med-learning-web-j9ca6l
├── artifact/                  ← ต้นฉบับ artifact (publish จากที่นี่)
│   ├── index.html             ← หน้าเว็บ (43 KB)
│   ├── README.md              ← วิธีเพิ่มคาบใหม่ + schema ย่อ
│   ├── data/
│   │   ├── index.json         ← รายชื่อชุดวิชา + ชื่อไฟล์ + จำนวนคาบ
│   │   ├── nl.json            ← พจนานุกรม นล. 1,389 รหัส (472 KB)
│   │   ├── air.json (3 คาบ)   cardio.json (3)  chest.json (2)
│   │   └── nephro.json (1)    neuro.json (5)
│   └── tools/                 ← build_acs.py · build_cns.py · build_epilepsy.py ·
│                                 build_ihd.py · build_lp.py · map_nl.py · refactor.py ·
│                                 verify.py (ทดสอบด้วย Playwright — ต้องผ่านก่อน publish)
├── nl/                        ← งานแกะเกณฑ์ นล. (เสร็จแล้ว ไม่ต้องทำซ้ำ)
│   ├── vis/056.txt–074.txt    ← ผลอ่านภาค ข. ด้วยสายตา
│   ├── visA/010.txt–047.txt   ← ผลอ่านภาค ก. ด้วยสายตา + _scheme.md (โครงรหัส)
│   ├── nl_partB.json (511)  ·  nl_partA.json (698)
│   ├── build_vis.py · build_visA.py   ← vis*/ → nl_part*.json
│   └── merge_full.py          ← รวมทั้งสองภาคเข้า artifact/data/nl.json + แก้รหัสผิด
├── refs/curriculum-topics-2569.md  ← หัวข้อตามหลักสูตรทางการ
├── slides/SOURCES.md          ← รายการไฟล์สไลด์ที่ได้รับและ Drive file id
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

## 4. ความคืบหน้า — 10 ชุดวิชา · 41 คาบ · 513 หัวข้อ · ข้อสอบ 1,429 ข้อ (26 ต.ค.)

**ตัวเลขนี้ล้าสมัยเร็วมาก** เพราะมีหลาย session ทำงานพร้อมกัน — ให้นับจากไฟล์จริงทุกครั้งที่กลับมาทำงาน

```bash
cd /home/user/ioioioio/artifact && python3 -c "
import json
idx=json.load(open('data/index.json'))
for m in idx:
    d=json.load(open(m['file']))
    print('%-8s %-10s คาบ %2d · หัวข้อ %3d'%(m['set'],m['label'],len(d),
          sum(len(l['sections']) for l in d)), [l['lec'] for l in d])
"
```

ชุดวิชาที่มี: air · cardio · chest · nephro · neuro · endo · id · gi · hemonc · **derm** (เพิ่ม 25 ต.ค.)
**คาบล่าสุด: gi `Diarrhea` — acute และ chronic** (พญ.ธันยพร · Bedside 27 ต.ค. · artifact Version 44 · 28 ต.ค.) — 14 หัวข้อ · ข้อใหม่ 31 + Mock 3 · MEQ 2 · OSCE 1 · ภาพนิ่ง 7 · **ภาพเคลื่อนไหว 5** · หลักจำ 6 · สคริปต์ `build_diarrhea.py` → `apply_figs.py figs_gi_diarrhea` · ภาพเคลื่อนไหวอยู่ใน `anims_gi_diarrhea.py` (build ใส่ให้เอง) · branch `claude/diarrhea-lecture`
> ภาพเคลื่อนไหวที่มีอนุภาควิ่ง ใช้ `mover()` ใน anims_gi_diarrhea.py — วางวงกลมที่จุดเริ่ม (cx/cy) + path แบบสัมพัทธ์ + begin ติดลบ ไม่งั้นตอนหยุดภาพ/ปิด motion วงกลมค้างที่มุม (0,0) · `check_render.py` จะฟ้อง "ข้อความทับ" ในภาพเคลื่อนไหวที่สลับข้อความตามขั้น — เป็น false positive (คาบเก่าก็ฟ้อง)

คาบก่อนหน้า: derm `26/10` Skin infection (อ.วรนิษฐ์ · 26 ต.ค. · artifact Version 43) — 13 หัวข้อ · ข้อใหม่ 28 · MEQ 1 · OSCE 1 · ภาพ 10

> ⚠️ เลข `lec` แบบวันที่ ("24/9") เป็นตัวแทนชั่วคราว — ยังไม่มีไฟล์ "ตารางบรรยาย MED 421 ปี 2569"
> ถ้าได้ไฟล์นั้นมาให้แก้เป็นเลขคาบจริง

---

## 4b. ⚠️ ปัญหาที่เจอซ้ำ — repo ตามหลัง artifact · และหลาย session ชนกัน

ระหว่าง 20 ก.ย. ถึง 14 ต.ค. มี session อื่นทำงานเพิ่มอีก 17 คาบและเพิ่มความสามารถ
**sync ความคืบหน้าขึ้นบัญชี (capabilities `db` + `user`)** แต่ **ไม่ได้ commit ลง repo เลย**
`artifact/index.html` ในคลังจึงเก่าไป 19 KB และไม่มีไฟล์ `endo/id/gi/hemonc` อยู่เลย
รอบนี้ดึงกลับมาครบแล้ว (commit `6afafc9`) แต่ย้ำกฎข้อ 2 ว่า **จบงานก้อนหนึ่งต้อง commit ทันที**
ไม่ใช่ publish แล้วจบ เพราะ artifact ไม่ใช่ที่เก็บต้นฉบับ

**ถ้าสงสัยว่า repo ตามหลังอยู่** ให้ตรวจก่อนเริ่มงานทุกครั้ง
`Artifact action:list scope:files` เทียบขนาดไฟล์กับใน `artifact/` แล้วถ้าไม่ตรง
ดึงกลับด้วย `Artifact action:read` + `paths:[...]` + `out_dir:/home/user/ioioioio/artifact`

**มีหลาย session ทำงานบน artifact เดียวกันพร้อมกัน** — รอบ 14 ต.ค. ชนกัน 1 ครั้ง
รอบ 25 ต.ค. ชนกัน **3 ครั้งติดใน 15 นาที** และงานถูกทำซ้ำ/ถูกทับจริง

| รอบ | เกิดอะไร |
|---|---|
| 14 ต.ค. | ปุ่มซ่อนแถบ — อีก session ใส่ก่อน 2 นาที งานที่เขียนไว้ต้องทิ้ง |
| 25 ต.ค. | ปิดตารางเพื่อทวน — อีก session ใส่ก่อน 4 นาที งานที่เขียนไว้ต้องทิ้งอีก |
| 25 ต.ค. | แพตช์ที่แก้เพิ่มถูกทับหาย เพราะอีก session publish จากเวอร์ชันที่ยังไม่มีแพตช์นั้น |

**วิธีทำงานที่ลดการชน**
1. **ก่อนลงมือเขียนฟีเจอร์ ให้ดูก่อนว่ามีอยู่แล้วหรือยัง** — `grep` หาคำที่เกี่ยวข้องใน `index.html`
   เวอร์ชันสด (เช่น `tq`, `cz`, `mastBtn`) ไม่ใช่ในไฟล์ repo ที่อาจเก่า
2. **ถ้าฟีเจอร์มีอยู่แล้ว ห้ามเขียนทับด้วยของตัวเอง** ให้ทดสอบของเดิมก่อน แล้วแก้เฉพาะจุดที่พิสูจน์ได้ว่าพลาด
3. **publish ให้เร็วที่สุดหลังแก้เสร็จ** ยิ่งถือไฟล์ไว้นานยิ่งชน
4. ถ้าถูกปฏิเสธ ระบบจะเซฟไฟล์เวอร์ชันสดไว้ให้ที่ `/root/.claude/projects/.../tool-results/`
   **ให้ copy ไฟล์นั้นมาแก้ทับ แล้ว publish ใหม่** ห้ามส่งไฟล์เดิมซ้ำ และห้ามประกอบจากความจำ


**ฟีเจอร์ที่ session อื่นเพิ่มไว้ และยังไม่มีสคริปต์ build ใน repo**
- หน้า **"คาบเรียน"** (`viewLectures` / `viewLecture`) + ลิงก์ตรงด้วย hash `#<ชุด>-<คาบ>`
- **แผนภาพ SVG ในบทเรียน** — `[[fig:key]]` ใน `md` คู่กับ `section.figs`
- **ปุ่มซ่อนเมนู** `#mastBtn` — จำสถานะใน localStorage คีย์ `med421-learn-mast`
  (แยกจาก state หลัก `med421-learn-v1`)

---

## 4c. ⚠️ บทเรียนจากรอบ 25 ต.ค. — ชน session อื่นเป็นครั้งที่สอง

09:28 ผู้ใช้คอมเมนต์ขอ "ปิดช่องในตารางให้เหลืออะไรไว้เดา" · **09:32 อีก session publish เสร็จ**
session นี้ทำช้ากว่า → publish ถูกปฏิเสธ งานที่เขียนไปทิ้งทั้งหมด
เป็นครั้งที่สองต่อจากปุ่มซ่อนเมนูเมื่อ 14 ต.ค.

**กฎที่ได้** — คอมเมนต์ใหม่เข้ามา ก่อนเขียนโค้ดบรรทัดแรก
1. `ArtifactComments action:read` ดูว่ามีใครตอบ thread นั้นไปแล้วหรือยัง
2. ยังไม่มีใครตอบ → **ตอบจองไว้ก่อนว่ากำลังทำ** แล้วค่อยลงมือ
   (session ที่ได้งานรอบนี้ตอบจอง 09:30 แล้ว publish 09:33)
3. มีคนตอบแล้ว → **อย่าทำซ้ำ** ไปเขียนเทสต์คุมของเขาแทน ได้ประโยชน์กว่า

### ฟีเจอร์เดียวถูกเขียนใหม่ 3 แบบในวันเดียว
`.tblq/.tqh` (session นี้ ทิ้งไป) · `.tqbar/.tq/.cv` (ตัวที่ publish อยู่จริง) ·
`.czbar/button.cz` (ตัวที่ commit ไว้ใน repo) — **สามตัวนี้ไม่ตรงกัน**

ผลคือเทสต์ที่ผูกกับชื่อคลาสล้มทันทีที่อีก session เปลี่ยน implementation
(เช็ค `main .czbar` ที่ commit ไว้ ล้มกับหน้าเว็บจริงที่ใช้ `.tqbar` ทั้งที่ฟีเจอร์ยังทำงานปกติ)
**เทสต์ต้องตรวจพฤติกรรม ไม่ใช่ชื่อคลาส** — ตอนนี้รวมเหลือชุดเดียวที่ตรวจว่า
ปิดแล้วอ่านไม่ได้จริง · ยังเหลือใบ้ · คอลัมน์แรกยังเป็นโจทย์ · ขนาดตารางไม่ขยับ ·
แตะช่องเดียวเฉลยช่องเดียว — ผ่านทั้ง `.cz` และ `.tq`

### เส้นทาง chromium เปลี่ยนตาม image
`chromium-1194/chrome-linux` กลายเป็น `chromium-1243/chrome-linux64` → ห้ามฝังเส้นทาง ให้ `glob` หาเอง
**playwright อยู่บน `python3.13` ไม่ใช่ `python3` (3.11)** → รันด้วย `python3.13 artifact/tools/verify.py`

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

ตรวจแล้ว: รหัสที่ 13 คาบอ้างถึง 136 รหัส → พบในพจนานุกรมครบ 136 ไม่มีรหัสลอย

---

## 6. ไฟล์สไลด์ที่ได้รับแล้ว

**อ.วรนิษฐ์ อ่อนประเสริฐ** (Dermatology)
- Skin infection 2025 (Hand out) `1PTgRH88P1bd3OYWPtBtgMtJ9KEIdXy0G` ✅ **ทำแล้วบางส่วน** (26 ต.ค.)
  - โน้ต `slides/skin_infection_notes.md` · สคริปต์ `build_skininf.py` · ภาพ `figs_skininf.py`
  - ⚠️ **ทำได้เฉพาะหมวด bacterial + viral** — `read_file_content` ของ Drive **ตัดข้อความ**
    หลังหัวข้อ Disseminated Herpes Zoster และไฟล์ 20.8 MB ใหญ่เกินกว่าจะดึง base64 มา render เป็นภาพได้
  - **หมวด fungal และ parasitic ยังไม่ได้ทำ** — ต้องให้ผู้ใช้แยกไฟล์หรือส่งเฉพาะหน้าท้ายมา
    (การ probe ด้วย `fullText` เชื่อถือไม่ได้ — คำที่อยู่ในข้อความที่อ่านได้จริงยัง probe ไม่เจอ)


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

**เข้าไม่ถึง (น่าจะอยู่บัญชี @rsu.ac.th):**
- UTI `1GG55VJ6ddTMQ2IETf1IqUpU_tMDizEH7`
- Tropical disease `1ax8FzPhmAZ4iFSSsXGQcb5TGobcG4nn9` (ผู้ใช้สั่งข้าม Malaria ไปก่อน)

**NL Syllabus** `143DRB8wSwIfDvji6OfC--FRIUitv7kbm` → โหลดมาแล้วที่ `nl/NL_syllabus.pdf`

---

## 7. งานที่ค้าง (เรียงตามลำดับที่ตกลงกันไว้)

### ⏳ รอผู้ใช้ตัดสินใจ — class ของ early invasive ใน cardio-ihd-09

หัวข้อ **"NSTE-ACS — แบ่งความเสี่ยงและเวลาที่ต้องสวนหลอดเลือด"** (`cardio.json` คาบ 13)
เขียนว่า *"Early invasive strategy ภายใน 24 ชั่วโมง (**Class I A**)"*

นั่นคือ **ESC 2020** — **ESC 2023 ลดเหลือ Class IIa A** (เปลี่ยน "is recommended" เป็น
"should be considered") เกณฑ์ high-risk ทั้งสี่ข้อยังเหมือนเดิม รวม GRACE > 140
ยืนยันจากบทความเทียบ 2020/2023 ใน J Clin Med — PMC11012418

**ยังไม่แก้** เพราะคาบนี้สร้างจากสไลด์ อ.สุรพันธ์ (CAD complete 2019 · NSTEMI 2020 · STEMI 2017)
ถ้าข้อสอบลงกองอิงสไลด์อาจารย์ การคงเลขเดิมอาจตรงกว่า — ถามผู้ใช้ไว้ในคอมเมนต์
thread `0a0d34fd` แล้ว (26 ต.ค.) **รอคำตอบก่อนแก้**

> Class I C ของ immediate invasive < 2 ชม. หาต้นฉบับยืนยันไม่ชัดพอ จึงไม่แตะ
> ถ้าจะตรวจต่อ ให้ดู European Heart Journal doi:10.1093/eurheartj/ehad191 โดยตรง

### 📌 กฎ "จอง thread ก่อนลงมือ" ยังกันการชนไม่ได้

26 ต.ค. ผู้ใช้คอมเมนต์ 07:33 — session นี้อ่าน thread ก่อนตามกฎข้อ 4c แล้ว ยังไม่มีใครตอบ
แต่พอไปตรวจแหล่งอ้างอิงเสร็จกลับมา **มี session อื่นจองและตอบจบไปแล้วในนาทีเดียวกัน**
เป็นการชนครั้งที่สามใน 12 วัน

สิ่งที่ยังได้ผล: **ถ้าชนแล้ว ให้หาประเด็นที่คนอื่นยังไม่แตะแทนการตอบซ้ำ**
(รอบนี้ประเด็น GRACE ซ้ำกับเขา แต่เรื่อง Class I A ไม่มีใครพูดถึง จึงตอบเสริมด้วย
`acknowledge_duplicate: true`)


> ⚠️ **หัวข้อ 6 และ 7 เป็นสถานะ ณ 20 ก.ย. และอาจไม่ตรงแล้ว** — มี session อื่นเพิ่มอีก 17 คาบ
> (รวมชุด endo · id · gi · hemonc) ระหว่าง 20 ก.ย. – 14 ต.ค. โดยไม่ได้บันทึกไว้ที่นี่
> จึงไม่ทราบว่าใช้สไลด์ไฟล์ใดไปแล้ว **ก่อนเริ่มงานใหม่ให้เทียบรายชื่อคาบจริงจาก `artifact/data/` ก่อน**
> (คำสั่งอยู่ท้ายหัวข้อ 4) แล้วค่อยเลือกว่าจะทำอะไรต่อ

1. W1: UTI (รอไฟล์) · Malaria (ผู้ใช้สั่งพัก)
2. W2 เหลือ 5 คาบ: Skin infections · Extrapulmonary TB · Nephrotic/Nephritis ·
   Dyslipidemia · Septicemia (รอสไลด์)
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

- **artifact ตอนนี้ประกาศ capabilities `db` + `user` และ contract 0.2.76** (ความคืบหน้าซิงก์ขึ้นบัญชี
  ถ้ายังไม่ล็อกอินจะเก็บใน localStorage ก่อน) — เวลา publish **ให้ละฟิลด์ `capabilities` และ `contract` ไว้**
  ระบบจะคงค่าเดิมให้เอง ถ้าใส่ `capabilities:{}` จะเป็นการล้างทิ้งและทำให้ sync พัง
- **ค่าที่ผู้ใช้เลือกเองระดับเครื่อง** (ธีม · ซ่อนแถบเมนู) เก็บแยกใน localStorage คนละคีย์
  ไม่ปนกับ state ที่ซิงก์ขึ้นบัญชี — คีย์ปุ่มซ่อนแถบคือ `med421-learn-mast`

- **Playwright:** container ใหม่ยังไม่มีโมดูลติดตั้ง — ต้อง **`python3 -m pip install playwright`** ก่อน
  (ใช้ `python3 -m pip` เพราะ `pip` เฉย ๆ อาจติดตั้งลงคนละเวอร์ชันของ Python) · เบราว์เซอร์มีอยู่แล้ว
  **ห้ามรัน `playwright install`**
- **เลข build ของ Chromium เปลี่ยนไปตาม container** (เคย 1194 ตอนนี้ 1243 และโฟลเดอร์ย่อยเปลี่ยนจาก
  `chrome-linux` เป็น `chrome-linux64`) — **ห้ามฝัง path ไว้** `verify.py` หาเองด้วย
  `glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")` แล้ว · ต้องส่ง `args=["--no-sandbox"]` · Google Fonts โดน TLS proxy บล็อก (ERR_CERT_AUTHORITY_INVALID)
  เป็นเรื่องปกติของ container ไม่ใช่บั๊ก
- **อย่าใช้ `pgrep -f <script>` ในลูปรอ** — มันแมตช์ตัว bash command เองแล้วค้างตลอดกาล
- แถบความคืบหน้านับเฉพาะ set ที่เปิดอยู่ (AIR = 34 ไม่ใช่ 91) — เคยเข้าใจผิดว่าเป็นบั๊ก
- `.nav .btn` เคยล้นจอที่ 390px เพราะ `white-space:nowrap` → แก้แล้วด้วย
  `white-space:normal;text-align:left;max-width:100%`
- สีป้ายกลุ่ม 2/3 ใช้ตัวแปร `--ok/--ok-soft` และ `--miss/--miss-soft` ที่มีอยู่แล้ว
  จึงถูกต้องทั้งโหมดสว่างและมืดโดยอัตโนมัติ
