# Review: endo

ตรวจครบ: one_per_theme 26 แก่น (related + fix + ข้อตัวแทนพร้อม note), synth 9 ข้อ, ข้อรูป 1 ข้อ (PIC35-13 เปิดดูรูปแล้ว)

คำนวณตรวจด้วย python: SYN-ENDO-01 Friedewald LDL = 290 − 38 − 210/5 = 210 ✔, metabolic syndrome ครบ 5/5 ✔; SYN-ENDO-02 eGFR (CKD-EPI 2021, หญิง 56 ปี Cr 1.2) ≈ 53 ✔; SYN-ENDO-04 AG = 27 ✔, Winter 1.5×8+8 = 20 = PaCO2 ✔, effective osmolality 289 ✔, corrected Na ≈ 137 ✔. คำตอบ choices[0] เป็นคำตอบที่ดีที่สุดเพียงข้อเดียวทุกข้อ ไม่มีข้อที่ต้องเปลี่ยนคำตอบ

## รายการแก้
1. synth SYN-ENDO-04 choices[0] — ผิดเล็กน้อย: "delay insulin until K is at least 3.3 mEq/L" → "delay the insulin infusion until potassium has been corrected" (เกณฑ์ 3.3 เป็นของ ADA เดิม; consensus ADA/EASD 2024 ใช้ 3.5 จึงไม่ผูกตัวเลือกกับตัวเลขเดียว คำตอบยังเป็นข้อเดิม)
2. synth SYN-ENDO-04 explain — ผิดเล็กน้อย: "ให้ K ก่อนจน ≥3.3" → ระบุทั้ง ≥3.3 (ADA เดิม) และ ≥3.5 (consensus 2024) และว่า K 3.1 ต่ำกว่าทั้งสองเกณฑ์; ปรับบรรทัดตัวลวง "ถูกเมื่อ K ≥3.3" ให้ตรงกัน
3. synth SYN-ENDO-04 fullcover — ผิดเล็กน้อย: บรรทัด K เพิ่ม "consensus 2024 ใช้ <3.5 / 3.5–5.0 / >5.0"
4. synth SYN-ENDO-04 pearl — ปรับให้ชัด: "(K <3.3 ให้ K ก่อน)" → "(K <3.3 หรือ <3.5 ตามแนวทาง 2024 ให้ K ก่อน)"
5. one_per_theme "DKA: ลำดับการรักษา (NSS ก่อน → IV insulin drip, K ต่ำให้ K ก่อน)" related — ผิดเล็กน้อย: เกณฑ์ K 3.3/5.2 → เพิ่มเกณฑ์ consensus 2024 (<3.5 งด insulin ให้ K 10–20 mEq/ชม., 3.5–5.0 ใส่ K, >5.0 ไม่ให้)
6. one_per_theme เดียวกัน related — ผิดเล็กน้อย: เกณฑ์ DKA หาย "pH ≥7.3 หรือ HCO3 ≥18 ร่วมกับ ketone ลดลง" → "pH ≥7.3 และ HCO3 ≥18 และ β-OHB <0.6 mmol/L" (consensus 2024)
7. one_per_theme เดียวกัน fix (เพิ่มใหม่) — ผิดเล็กน้อย: note ของข้อตัวแทนใช้ตัวเลข ADA เดิม (K 3.3/5.2, bicarbonate pH <6.9) → ระบุเกณฑ์ 2024 (K 3.5/5.0, bicarbonate pH <7.0); คำตอบของข้อตัวแทนยังถูก
8. one_per_theme "Subacute (de Quervain) thyroiditis หลัง URI" fix (เพิ่มใหม่) — ปรับให้ชัด: ข้อตัวแทนให้ต่อมเจ็บ 2 สัปดาห์หลัง URI พร้อม TSH 20 ซึ่งไม่ตรงลำดับโรคทั่วไป (ช่วงเจ็บมักเป็นระยะ thyrotoxic TSH ต่ำ; ระยะ hypothyroid มาทีหลังเมื่อปวดทุเลา) → อธิบายลำดับและบอกว่า TSH ต่ำ + ต่อมเจ็บหลัง URI ก็ตอบ subacute thyroiditis

## ข้อรูป
- PIC35-13 (thyroid scan): ภาพผู้ป่วยเห็นจุดจับสารเข้มจุดเดียว เนื้อต่อมที่เหลือแทบไม่จับสาร เทียบภาพปกติที่เห็นสองกลีบ ตำแหน่งอยู่ด้านซ้ายของภาพ (anterior view = กลีบขวาของผู้ป่วย) ตรงกับ stem/cap/เฉลย toxic adenoma → review/endo_pics_fix.json = []

## ข้อสังเกต (ไม่แก้)
- SYN-ENDO-08: high-dose DST ไม่กด + MRI pituitary ปกติ ทำให้ ectopic ACTH เป็นคำตอบที่ "most likely" ได้ (ACTH 310, K 2.6, อาการเร็ว, สูบบุหรี่) explain ระบุ IPSS ไว้แล้วสำหรับรายที่ยังไม่แน่ใจ
- note ข้อตัวแทน Thyrotoxicosis มีคำพิมพ์ผิด "อยู่ใต้ต่อใต้ pituitary" (อ่านอย่างเดียว ไม่กระทบความหมาย)
