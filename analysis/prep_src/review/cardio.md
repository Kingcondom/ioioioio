# Medical accuracy review: cardio

ขอบเขตที่ตรวจ: one_per_theme 49 แก่น (related + fix) พร้อมข้อตัวแทน 49 ข้อ (โจทย์ ตัวเลือก คำตอบ note), synth 18 ข้อ (stem, choices, explain, fullcover, pearl) และข้อรูป 3 ข้อ (เปิดดูรูปครบทุกรูป)
คำนวณตัวเลขใน stem ซ้ำแล้ว: Friedewald LDL (SYN-08 = 265 ตรง), BUN:Cr (SYN-03 ≈ 27), pulse pressure (SYN-18 = 26), pulse deficit (SYN-06 = 22), CHA2DS2-VASc (SYN-06 = 5 / CHA2DS2-VA = 4), Wells DVT (SYN-16 = 4), MAP, BP ต่างกันสองแขน (SYN-12 = 44) ทุกค่าสอดคล้องกัน

## รายการแก้

1. synth SYN-CARDIO-17 explain (ตัวลวง apixaban) — ผิดเล็กน้อย
   ก่อน: "apixaban และ DOAC อื่นไม่ได้ผลและอันตรายกว่า warfarin ใน rheumatic MS (INVICTUS)"
   หลัง: INVICTUS ทดสอบ rivaroxaban (ไม่ใช่ apixaban) เทียบ warfarin พบ cardiovascular event และอัตราตายสูงกว่า จึงไม่ใช้ DOAC ใน AF ที่มี rheumatic MS ปานกลาง–รุนแรง ต้องใช้ warfarin

2. synth SYN-CARDIO-14 explain (ตัวลวง masked HT/methyldopa) — ปรับให้ชัด
   ก่อน: "methyldopa เป็นยาสำหรับ HT ในครรภ์เท่านั้น"
   หลัง: "methyldopa ใช้เป็นหลักใน HT ระหว่างตั้งครรภ์ และรายนี้ยังไม่ได้เป็น HT ที่ต้องให้ยา" (คำว่า "เท่านั้น" เกินจริง)

3. one_per_theme "วินิจฉัย HT: white coat / resistant / secondary / lifestyle" fix — ปรับให้ชัด
   ก่อน: fix อธิบายว่าแนวทางปัจจุบัน (ESC 2024, AHA/ACC 2025) ให้เริ่มยาเมื่อยืนยัน BP ≥ 140/90 แต่ไม่ได้บอกผู้อ่านว่าคำตอบของข้อตัวแทนควรเป็นอะไร
   หลัง: เพิ่มว่าข้อสอบเก่าที่อิงแนวทางเดิม (รวมแนวทางไทย 2562) เฉลย D (lifestyle 3–6 เดือน) ส่วนถ้าตอบตามแนวทางปัจจุบันให้เริ่มยาร่วมกับปรับพฤติกรรม (เนื้อหาเดิมใน fix ถูกต้อง เก็บไว้)

## ตรวจแล้วไม่ต้องแก้ (บันทึกไว้)
- ข้อตัวแทน 49 ข้อ: คำตอบและ note ถูกต้องตามแนวทางปัจจุบัน; ข้อที่โพยเก่าเฉลยผิด (AF rate control = digoxin, IE = ASO, ECG ใน PP35-CAR-031) note แก้ไว้แล้ว ข้อ HT grade 1 มี fix อยู่แล้ว (ปรับตามข้อ 3)
- related ทั้ง 49 แก่น: ค่าตัดและขนาดยาที่ตรวจตรงแนวทาง เช่น เกณฑ์ STEMI V2–V3 ตามเพศ/อายุ, ESC 2023 fibrinolysis ≤ 10 นาที/CAG 2–24 ชม., CHA2DS2-VA (ESC 2024), cardioversion > 24 ชม. (ESC 2024), PH mPAP > 20 (ESC/ERS 2022), Jones 2015, prophylaxis IE ไม่ใช้ clindamycin, adrenaline 0.01 mg/kg IM สูงสุด 0.5 mg, colchicine ตามน้ำหนัก, atropine 1 mg สูงสุด 3 mg, ICD/CRT, MR/AR/AS surgical thresholds, Marfan root ≥ 50 mm
- synth 18 ข้อ: ทุกข้อมีคำตอบที่ดีที่สุดข้อเดียว คำตอบตรงกับ explain ไม่มีตัวลวงที่ถูกพอๆ กัน
- ข้อรูป (review/cardio_pics_fix.json = []):
  - PIC35-01: รูปเห็น sinus rhythm ราว 95/นาที, QS + ST ยกใน V1–V4 และ ST ยกเล็กน้อยใน V5, inferior lead ไม่ยก ตรงกับเฉลย LAD
  - PIC35-02: ST ยกใน I, aVL, V2–V6 และ ST กดใน III, aVF, HR ราว 60 ตรงกับ stem; การเลือก fibrinolysis เมื่อส่งต่อ PCI ต้องใช้ 3 ชม. ถูกต้อง
  - PIC35-03: วัดจาก rhythm strip lead II ได้ P ราว 86/นาที (บางตัวซ่อนใน T wave), QRS แคบราว 29/นาที, conduction 3:1 และ PR ของ beat ที่นำผ่านคงที่ = high-grade (Mobitz II-type) AV block ตรงกับเฉลย
