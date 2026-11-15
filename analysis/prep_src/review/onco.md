# Medical accuracy review: onco

ตรวจแล้ว: one_per_theme 15 แก่น (related + fix), synth 6 ข้อ, reps 15 ข้อ, pics 1 ข้อ (เปิดดูรูปแล้ว)
ผล `python3 check2.py onco` = OK

## รายการแก้

1. **synth SYN-ONCO-06 choices[0]** | ปรับให้ชัด
   - ก่อน: "...whereas chest radiograph screening shows no benefit because its interval includes 1"
   - หลัง: "...shows **no evidence of** benefit because its interval includes 1" เพราะ CI คร่อม 1 แปลว่าไม่มีหลักฐานว่าได้ประโยชน์ ไม่ได้พิสูจน์ว่าไม่มีผล ซึ่งเป็นหลักเดียวกับที่ข้อนี้สอน (ไม่มีนัยสำคัญ ≠ เท่ากัน) คำตอบไม่เปลี่ยน

2. **one_per_theme "มะเร็งที่หายขาดด้วยเคมีบำบัด: testicular germ cell, lymphoma, chemosensitivity" related** | ปรับให้ชัด
   - ก่อน: จัด APL (ATRA + arsenic trioxide) เป็นมะเร็งที่หายด้วยเคมีบำบัดโดยไม่มีคำอธิบาย
   - หลัง: ระบุว่า APL หายขาดด้วย ATRA + ATO ซึ่งเป็น differentiation therapy ไม่ใช่ cytotoxic chemotherapy แท้

3. **one_per_theme "Performance status (ECOG) และ treatment intent" fix (ต่อท้าย fix เดิม)** | ปรับให้ชัด
   - ก่อน: note ของ rep อ้าง "คำตอบที่บันทึกคือข้อ A", "ข้อ B ผิด... ECOG 1", "ข้อ C, D, E ผิด" แต่ในหน้าที่แสดงคำตอบอยู่ลำดับที่ 4 (D) และ ECOG 1 อยู่ลำดับที่ 3 ผู้อ่านอาจคิดว่าข้อ D ผิด
   - หลัง: fix บอกว่าตัวอักษรใน note อ้างลำดับในโพยเดิม และคำตอบคือ "ECOG 0; curative intent with neoadjuvant therapy"

## ข้อรูป
- PIC35-19 (มือ ชายสูบบุหรี่): รูปเป็นปลายนิ้วโป่ง เล็บโค้งนูนทุกนิ้ว = digital clubbing ตรงกับคำบรรยายและเฉลย lung cancer; คำอธิบาย (Lovibond angle >180°, Schamroth sign, COPD อย่างเดียวไม่ทำให้ clubbing) ถูกต้อง → ไม่มีปัญหา (`review/onco_pics_fix.json` = [])

## จุดที่ตรวจแล้วไม่ต้องแก้ (ตัวอย่าง)
- SYN-ONCO-03: ค่า SIADH สอดคล้องกัน (Na 124 → คำนวณ osmolality ได้ราว 258, urine osm 480, urine Na 52, euvolemic, thyroid/adrenal ปกติ); limited-stage SCLC → concurrent platinum–etoposide + early thoracic RT (+ durvalumab ตาม ADRIATIC) ถูก
- SYN-ONCO-05: ครอบครัวเข้าเกณฑ์ Amsterdam II จริง (พ่อ CRC 46, อา endometrium, ปู่ ureter; ปู่เป็นญาติสายตรงของอีกสองคน, 2 รุ่น, 1 คน <50); MSH2 → colonoscopy ทุก 1–2 ปี + TAH-BSO ราว 40 ปี ถูก
- SYN-ONCO-06: RR 0.80 (0.73–0.93) และ 0.99 (0.87–1.13) ตรงกับ NLST/PLCO; คำตอบเดียวชัดเจน
- SYN-ONCO-01/02/04: HER2+ ER+ cT2N1 (chemo + trastuzumab 1 ปี ไม่ให้พร้อม anthracycline, T-DM1 เมื่อมี residual disease), FN (≥38.3 หรือ ≥38.0 นาน 1 ชม. + ANC <500, antipseudomonal β-lactam ภายใน 60 นาที, MASCC ≥21), mediastinal choriocarcinoma (hCG สูงมาก/AFP ปกติ, scrotal US, cisplatin-based BEP/VIP, marker half-life) ถูกต้อง
- fix เดิมของแก่น ECOG (neoadjuvant vs adjuvant ขึ้นกับชนิดมะเร็ง) ถูกต้อง คงไว้
