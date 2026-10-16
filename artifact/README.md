# ต้นฉบับ artifact "MED421 learn"

เว็บเรียน https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE

```
index.html          หน้าเว็บ (โหลด data/*.json แบบ lazy ตอนกดแท็บ)
data/index.json     รายชื่อชุดวิชา + ชื่อไฟล์ + จำนวนคาบ
data/nl.json        พจนานุกรมเกณฑ์ นล. 2567 ฉบับเต็ม 1,389 รหัส
data/<set>.json     เนื้อหาคาบเรียนแยกตามชุดวิชา
tools/              สคริปต์สร้างคาบ + ตัวตรวจ
```

## เพิ่มคาบใหม่

1. เขียน `tools/build_<ชื่อ>.py` ตามแบบ `build_ihd.py`
2. รันเพื่อ merge เข้า `data/<set>.json` แล้วอัปเดต `lectureCount` ใน `data/index.json`
3. `python3 tools/verify.py` — ต้องผ่านก่อนเสมอ
4. publish ด้วย `Artifact` action publish พร้อม `url` เดิม + `root` + `files`

## schema

```
lecture: { lec, title, subtitle, objectives[], sections[], meq[], osce[],
           nlGap?, guidelines?[] }
section: { id, title, summary, minutes, nl[], md, pearls[], items[] }
item:    { id, kind:"mcq"|"old", stem, choices[5], answer(0-4), explain,
           pearl, topic, src, ref[], nl[] }
```

**ข้อควรระวัง** — markdown parser ในหน้าเว็บไม่รองรับ code fence (```) ห้ามใช้ ใช้ตารางแทน ·
`answer` นับจาก 0 · `id` ห้ามชนกัน
