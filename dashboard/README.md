# MED421 Lectures — dashboard รวมทุกคาบบรรยาย

**artifact:** https://claude.ai/artifact/8ir2xCgMKC7Fn4MiE2a5AV (ต้นฉบับคือ `index.html` ในโฟลเดอร์นี้)

หน้าเดียวรวมคาบบรรยายของกลุ่มเรา 45 คาบ (14 ก.ย. – 22 พ.ย. 2569) เรียงตามวันจริงจาก Google Calendar
แต่ละคาบมีปุ่มเปิด **MED421 learn** และ **MED421 Ward Drill** ตรงคาบนั้น + ลิงก์ "อ่านคู่" ไปบทข้างเตียงในห้องสมุดท่าอาจารย์

| เว็บ | URL |
|---|---|
| MED421 learn | https://claude.ai/artifact/5jjGrfPjyBgP7wzxcu8TcE |
| MED421 Ward Drill | https://claude.ai/artifact/Fdi5gcNXKqFLAXg4fQBV7X |
| ห้องสมุดท่าอาจารย์ | https://claude.ai/artifact/QebhLmV2eKyzj3mkqstnjR |

## ลิงก์ตรงเข้าคาบ (deep link)

artifact ส่งต่อเฉพาะ `#token` ธรรมดา (ตัวอักษร ตัวเลข `.` `_` `~` `-`) เข้าไปถึงหน้าเว็บ จึงใช้รูปแบบ

```
<learn>#<ชุด>-<คาบ>     เช่น #cardio-13 · #gi-27.10 (คาบ "27/10" ใช้ . แทน /) · #endo (ทั้งชุด)
<drill>#<ชุด>-<lec>     เช่น #nephro-14 · #neuro-N02 · #chest-TB2 · #mock-M07 · #derm (ทั้งชุด)
```

- **learn** → เลือกชุด เปิดหน้าภาพรวม กางคาบนั้นในแถบซ้าย แล้วเลื่อนไปที่การ์ดของคาบ
- **drill** → เลือกชุด โหมด "ข้อสอบใหม่" กรองเฉพาะ lecture นั้น (ถ้ามีแต่ในคลังเก่าจะสลับเป็นโหมดคลังเก่า)

โค้ดที่เพิ่มอยู่ใน `patch_deeplinks.py` (เพิ่มเมื่อ 13 ต.ค. 2569 · learn Version 20 · drill Version 11)
**ถ้า publish learn หรือ drill ใหม่จาก branch อื่น ต้องมีโค้ดส่วนนี้ด้วย** ไม่อย่างนั้นปุ่มใน dashboard จะเปิดแค่หน้าแรก
(ไม่พัง แต่ไม่กระโดดไปคาบ) — `readHash()/landHash()` + `id='lec-…'` ในการ์ดคาบของ learn และ `applyHash()` ท้ายสคริปต์ของ drill

## แก้ข้อมูล

ข้อมูลทั้งหมดอยู่ในอาร์เรย์ `LECS` / `EXTRAS` ในสคริปต์ของ `index.html`

```
learn: [ลิงก์คาบ, จำนวนหัวข้อ, ข้อเช็คความเข้าใจ]
drill: [ลิงก์ lec, MCQ, MEQ+OSCE/SAQ, คลังเก่า, 1 = ชุดรวม (คลังยังไม่แยกรายคาบ)]
more:  [[ชื่อบทข้างเตียง, artifact id], ...]
```

เมื่อ learn มีคาบใหม่ ให้ใส่ `learn:[...]` ให้คาบนั้นแล้ว publish `index.html` ทับ URL เดิม
ตัวเลขจำนวนข้อเป็นภาพ ณ 13 ต.ค. 2569
