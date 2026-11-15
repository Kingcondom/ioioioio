# nephro: บันทึกการแก้ไข (medical accuracy review)

ตรวจแล้ว: one_per_theme 43 แก่น (related + ข้อตัวแทน/note), synth 16 ข้อ (คำนวณ AG, osmolal gap, Winter, pH, corrected Ca, free water deficit, FENa/อัตราปัสสาวะ, Cockcroft-Gault ด้วย python ตรงทุกข้อ) และข้อรูป 2 ข้อ (เปิดดูรูปแล้ว)
ข้อตัวแทนทั้ง 43 ข้อมีเฉลยและ note ถูกต้อง จึงไม่ต้องเขียน `fix`

## รายการแก้

1. **one_per_theme "Uremia และข้อบ่งชี้ dialysis" related** · ผิดเล็กน้อย
   ก่อน: uremic pericarditis "(เสียงเสียดสี, ST ยกทั่วไป, ไม่มี PR depression ชัดได้)" ซึ่งทำให้เข้าใจว่า ECG มักมี ST ยกทั่วไป
   หลัง: ECG มักไม่มี ST ยกทั่วไปแบบ viral pericarditis เพราะกล้ามเนื้อหัวใจใต้เยื่อหุ้มมักไม่อักเสบ จึงใช้ ECG ปกติตัดโรคออกไม่ได้ (ตรงกับ fullcover ของ SYN-NEPHRO-02)

2. **one_per_theme "Pyelonephritis ซับซ้อน (abscess, de-escalate, sepsis AKI)" related** · ผิดเล็กน้อย (ล้าสมัย)
   ก่อน: "fluoroquinolone 5-7 วัน, beta-lactam ราว 10-14 วัน"
   หลัง: IDSA 2025 (complicated UTI) แนะนำราว 7 วันเมื่ออาการดีขึ้น ใช้ได้ทั้ง beta-lactam และ FQ (FQ 5-7 วัน) และให้นานขึ้นเมื่อมีฝี การอุดกั้นที่ยังไม่แก้ หรือตอบสนองช้า

3. **synth SYN-NEPHRO-06 explain** · ปรับให้ชัด
   ก่อน: "proteinuria ระดับ nephrotic" ทั้งที่ UPCR 3.4 g/g ยังไม่ถึงเกณฑ์ > 3.5
   หลัง: "proteinuria เกือบถึงระดับ nephrotic (UPCR 3.4 g/g, albumin 2.6)"

4. **synth SYN-NEPHRO-14 stem** · ปรับให้ชัด
   ก่อน: ไม่มีค่า creatinine แต่ explain ตัดตัวลวง AIN ด้วยเหตุผลว่า "AIN มี creatinine ขึ้น"
   หลัง: เพิ่ม "Creatinine is 0.8 mg/dL." ในโจทย์ ให้เหตุผลตัดตัวลวงมีข้อมูลรองรับ

## ข้อรูป (review/nephro_pics_fix.json)

5. **PIC35-20 (Gram stain ปัสสาวะ)** · ปรับให้ชัด
   รูปตรงกับโจทย์และเฉลย (GNB สีชมพูท่ามกลาง neutrophil เข้ากับ E. coli) แต่หมายเหตุอ้างว่า "เห็น capsule" (K. pneumoniae) ซึ่งในรูปไม่เห็น จึงเขียนข้อความแก้ว่าไม่เห็น capsule และ Gram stain แยก E. coli กับ Klebsiella ไม่ได้
- **PIC35-21 (KUB staghorn)**: รูปตรงกับเฉลย คือมี staghorn calculus ชัดที่ไตขวา และมีนิ่วแตกกิ่งในตำแหน่งไตซ้าย จึงไม่ต้องแก้

## สรุป
ผิดร้ายแรง 0 · ผิดเล็กน้อย 2 · ปรับให้ชัด 3 (รวมข้อรูป 1)
