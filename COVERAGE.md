# เรียนไปแล้ว vs อยู่ในคลังแล้ว — รายสัปดาห์

ดึงคาบ lecture จาก Google Calendar (event ที่ขึ้นต้นว่า `Lecture:`) แล้วเทียบกับ `bank_merged.json` ของหน้าหลัก
https://claude.ai/artifact/Fdi5gcNXKqFLAXg4fQBV7X (อัปเดตอัตโนมัติทุกวันเสาร์เช้า)

สถานะ
- ✅ **มีแล้ว** — มีกลุ่ม `lec` ของคาบนี้โดยตรง และมี MCQ ใหม่อย่างน้อย 5 ข้อ
- 🟡 **บางส่วน** — มีข้อที่เกี่ยวข้อง แต่อยู่ในกลุ่มหัวข้อกว้าง ๆ หรือมีแต่ข้อเก่า หรือมี MCQ ใหม่ไม่ถึง 5 ข้อ
- ❌ **ยังไม่มี** — ไม่มีข้อใหม่ของเรื่องนี้เลย

ตัวเลขในวงเล็บคือ MCQ ใหม่ / MEQ-OSCE / ข้อเก่า ที่ตรงเรื่องนั้น

---

## สัปดาห์ที่ 2 · 21–25 ก.ย. 2569

| วัน | Lecture (อาจารย์) | อยู่ในคลังที่ไหน | สถานะ |
|---|---|---|---|
| จ. 21 | Impetigo, Cellulitis, Herpes, Viral exanthem, Superficial mycoses (อ.วรณิสร์) | derm `D02` ผื่นเรื้อรังและผื่นจากการติดเชื้อ (3 / 0 / 34) | 🟡 ข้อใหม่มีแค่ 3 ข้อ ไม่มี MEQ ของการติดเชื้อที่ผิวหนัง |
| อ. 22 | SLE and systemic autoimmune diseases (อ.ปัญนิภา) | air `33` Connective tissue diseases and vasculitis (10 / 1 / 10) | ✅ แต่วันที่ของคาบ 33 ใน config ยังเป็น TBD |
| พ. 23 | Epilepsy (อ.พิมลพรรณ) | neuro `N02` หัวข้ออื่นของระบบประสาท (3 / 1 / 16) | 🟡 ไม่มีกลุ่มคาบของตัวเอง ข้อใหม่มีแค่ 3 ข้อ |
| พ. 23 | Extrapulmonary TB (อ.ภาณุวัฒน์) | chest `TB2` (10 / 1 / 0) — เพิ่ม 25 ก.ย. | ✅ |
| พฤ. 24 | Ischemic heart diseases (AL) (อ.สุรพันธ์) | cardio `13` (7 / 2 / 23) | ✅ |
| พฤ. 24 | Nephrotic / Nephritic syndrome (อ.ฉันทิศา) | nephro `14` (6 / 3 / 18) | ✅ |
| ศ. 25 | Dyslipidemia, obesity and metabolic syndrome (อ.นวพร) | endo `E04` (12 / 2 / 6) — เพิ่ม 25 ก.ย. | ✅ |
| ศ. 25 | หัตถการ Blood transfusion (อ.ชัชวาล) | heme `H02` (2 / 0 / 8) | 🟡 ยังไม่มีเรื่องหมู่เลือด ABO/Rh, crossmatch, ขั้นตอนหัตถการ |
| ศ. 25 | Septicemia and antibiotic usage (อ.พจน์) | infect `I01` (7 / 1 / 6) | ✅ ข้อเก่าอย่าง qSOFA (MED32) ยังพักอยู่ใน `_held_unverified_papers.json` |

**ต้องเพิ่ม (เรียงตามลำดับความสำคัญ)**
1. ~~Dyslipidemia / Obesity / MetS~~ ✅ เพิ่มแล้ว (`E04`)
2. ~~Extrapulmonary TB~~ ✅ เพิ่มแล้ว (`TB2`)
3. Blood transfusion: เพิ่มเรื่อง ABO/Rh compatibility, crossmatch, AHTR ต้อง stop transfusion ก่อน (MED28), ABO ของ FFP/cryo/platelet (MED31)
4. Epilepsy: แยกออกจาก `N02` เป็นกลุ่มคาบของตัวเอง แล้วเพิ่ม MCQ
5. Derm infection: เพิ่ม MCQ/MEQ เรื่อง impetigo, cellulitis, herpes, exanthem, tinea

**config ต้องแก้**
- คาบ `33` ใส่วันที่ "อ. 22 ก.ย."
- คาบ `10` Shock (AL) ใน config เป็น "อ. 22 ก.ย." แต่ย้ายไปแล้ว → "พ. 21 ต.ค. 15:00"

---

## สัปดาห์ที่ 3 · 28 ก.ย.–2 ต.ค. 2569

| วัน | Lecture (อาจารย์) | อยู่ในคลังที่ไหน | สถานะ |
|---|---|---|---|
| จ. 28 | Pleurisy, pleural effusion, empyema, Respiratory failure (อ.สกล) | chest `17` (8 / 3 / 14) | ✅ แต่เรื่อง empyema และ respiratory failure มี MCQ ใหม่แค่ 2 ข้อ (ที่เหลือเป็นเรื่อง effusion/PTX) |
| อ. 29 | Acute arthritis, crystal arthropathy, septic arthritis (อ.สูงชัย) | air `23` (17 / 2 / 15) — gout/CPPD/septic 9 ข้อใหม่ | ✅ |
| พ. 30 | Chronic kidney disease (อ.วรางคณา) | nephro `19` (6 / 1 / 16) | ✅ |
| พ. 30 | Thyroid diseases (อ.ศิวกร) | endo `E02` โรคของต่อมไทรอยด์ (7 / 1 / 18) | ✅ แต่ `E02` ยังเป็นกลุ่มหัวข้อ "ยังไม่ระบุคาบ" |
| พฤ. 1 | Chest X-ray interpretation / Occupational lung diseases (อ.พจนี) | chest `21` (7 / 0 / 8) | ✅ แต่ยังไม่มี MEQ/SAQ อ่านฟิล์ม |
| พฤ. 1 | Fluid electrolytes: Dysnatremia, dyskalemia (อ.ชุมพล) | nephro `22` (6 / 2 / 22) | ✅ |
| ศ. 2 | Approach to Arthritis (AL) (อ.กิตติวรรณ) | air `23` (ใช้กลุ่มเดียวกับคาบวันอังคาร) | ✅ |

ข้อเก่าที่ยังพักอยู่ใน `_held_unverified_papers.json` (ยังไม่ผ่านการตรวจ จึงไม่อยู่ในคลัง): ไทรอยด์ ~44 · Na/K ~31 · เยื่อหุ้มปอด/หายใจล้มเหลว ~15 · CXR/โรคปอดจากการทำงาน ~15 · gout/septic arthritis ~13 · CKD ~12

**ต้องเพิ่ม (เรียงตามลำดับความสำคัญ)**
1. Chest `17`: MCQ เรื่อง empyema (เกณฑ์ใส่ ICD, fibrinolytic/VATS) และ respiratory failure type 1/2
2. Chest `21`: SAQ อ่าน CXR (silicosis, asbestosis, pneumothorax ฯลฯ)
3. ตรวจข้อเก่าที่พักไว้ของไทรอยด์และ Na/K แล้วเอาเข้าคลัง (จำนวนมากที่สุด)
4. ค้างจากสัปดาห์ที่ 2: Blood transfusion, Epilepsy, Derm infection (ยัง 🟡)

**config ต้องแก้**
- คาบ `23` ยังเป็น TBD → "อ. 29 ก.ย." (และ AL ศ. 2 ต.ค.)
- `E02` → "พ. 30 ก.ย." (เป็นคาบ Thyroid diseases ของ อ.ศิวกร)
- ค้างจากสัปดาห์ที่ 2: คาบ `33` → "อ. 22 ก.ย." · คาบ `10` Shock → "พ. 21 ต.ค."

สัปดาห์ที่ 2: ไม่มีคาบไหนเปลี่ยนสถานะ (ไม่มีการเพิ่มข้อในคลังตั้งแต่ 25 ก.ย.)
