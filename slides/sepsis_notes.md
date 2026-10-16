# โน้ต — Septicemia and antibiotic usage (อ.พจน์ · ศ. 25 ก.ย. 2569 16:00–18:00)

ไฟล์สไลด์ใน Drive: "Sepsis _ Principle ATB medical student.pdf" `10qgsfnxQl7wacVkNBSAF5SXe8Bx4vPDc` (**175 MB · ภาพล้วน**)
- `read_file_content` คืนข้อความว่างเปล่า (ไม่มี text layer) · ดาวน์โหลดเข้า workspace ไม่ได้ (proxy) และไฟล์ใหญ่เกินจะส่งเป็น base64
- **ยังไม่ได้อ่านเนื้อหาสไลด์จริงแม้แต่หน้าเดียว** → ถ้าผู้ใช้ส่งภาพสไลด์ (ภาพหน้าจอ/PDF ไฟล์เล็ก) มา ให้อ่านด้วยสายตาแล้วแก้ `build_sepsis.py`

## แหล่งที่ใช้แทน
1. **Surviving Sepsis Campaign 2026** (Prescott HC, Antonelli M et al., CCM/ICM มี.ค. 2026) — ตรวจกับหน้า SCCM แล้ว:
   - 4 ระดับ definite/probable/possible/unlikely · ช็อก หรือ probable/definite → ยา ≤ 1 ชม. · possible ไม่ช็อก → สืบค้นเร็วแล้วให้ภายใน 3 ชม. · unlikely → ชะลอยา เฝ้าดู
   - คัดกรอง NEWS/NEWS2/MEWS/SIRS แทน qSOFA · crystalloid ≥ 30 mL/kg ใน 3 ชม. · balanced > NSS · ห้าม starch, gelatin · albumin เฉพาะได้น้ำมาก/ตับแข็ง
   - NE ตัวแรก เริ่มทางหลอดเลือดส่วนปลายได้ · MAP 65 · อายุ ≥ 65 ใช้ 60–65 · NE ขึ้นเรื่อย ๆ เติม vasopressin → epinephrine · ห้าม terlipressin, dopamine ตัวแรก
   - steroid ใน septic shock · lactate ซ้ำ · PCT ไม่ใช้ตัดสินเริ่มยา ใช้ช่วยหยุดได้ · anaerobe เฉพาะช่องท้อง อุ้งเชิงกรานลึก necrotizing soft tissue หัว-คอ CNS · ไม่ให้ antifungal เป็นกิจวัตร · beta-lactam prolonged infusion · source control ≤ 6 ชม.
2. **บทเรียน Sepsis SSC 2026 ของผู้ใช้** (claude.ai/artifact/DB59ZbY5ize8MhxXiHkZJZ · ทำคู่กับ lecture นี้) — กลไก "ท่อรั่ว ท่อขยาย ท่อตัน โรงงานดับ", นาฬิกา "1·1·3·รอ", 4 เคสจัดระดับ, โรคเลียนแบบ sepsis, NL1–3
3. **หลักการใช้ยาปฏิชีวนะ** (ส่วน "Principle ATB" ของชื่อไฟล์) — Harrison's 21e, Sanford Guide, แนวทาง melioidosis/leptospirosis/scrub typhus ของไทย
