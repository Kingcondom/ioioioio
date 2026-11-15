# Medical accuracy review: CHEST

ตรวจแล้ว: one_per_theme 30 แก่น (related + fix), synth 9 ข้อ, reps 30 ข้อ, pics 2 ข้อ (เปิดดูรูปทั้ง 2 รูปแล้ว)
ผล `python3 check2.py chest` = OK

## รายการแก้

1. **one_per_theme "Hypoxemia physiology: shunt, A-a gradient, ARDS" related** | ผิดเล็กน้อย
   - ก่อน: "Dead space (V/Q สูง): PE, emphysema → CO2 คั่งเป็นหลัก"
   - หลัง: dead space ทำให้ต้องเพิ่ม minute ventilation; **PE ส่วนใหญ่ PaCO2 ต่ำ** (hypoxaemia จาก V/Q mismatch) CO2 คั่งเฉพาะเมื่อชดเชยไม่ได้ (COPD/emphysema รุนแรง, PE ก้อนใหญ่มาก)

2. **one_per_theme "Hypoxemia physiology: shunt, A-a gradient, ARDS" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ใน note ของ rep CH-OLD-17)
   - ก่อน: note "dead space ... PE, emphysema — ทำให้ CO2 คั่งเป็นหลัก"
   - หลัง: fix อธิบายว่า PE มักมี respiratory alkalosis/PaCO2 ต่ำ คำตอบ shunt ถูกแล้ว

3. **one_per_theme "Salicylate poisoning: HAGMA + respiratory alkalosis" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ใน note ของ rep PP34-CHE-001)
   - ก่อน: "AG = 142-108-14 = 30"
   - หลัง: AG = 142 − (108 + 14) = **20** ยังเป็น HAGMA; Winter 29 ± 2 vs 20 = respiratory alkalosis ซ้อน คำตอบ salicylate ไม่เปลี่ยน

4. **one_per_theme "CAP ใน รพ.: empirical ceftriaxone + macrolide, เกณฑ์เปลี่ยน IV → oral" fix (เพิ่มใหม่)** | ปรับให้ชัด
   - ก่อน: โจทย์ rep PP32-CHE-063 ไม่ได้บอกว่า admit แต่เฉลย ceftriaxone IV + azithromycin
   - หลัง: fix ระบุว่าเฉลยนี้ใช้กับ CAP ที่ต้อง admit (non-ICU) ไม่มีปัจจัยเสี่ยงเชื้อดื้อ; OPD ไม่มีโรคร่วม = amoxicillin ขนาดสูงเดี่ยว; มีโรคร่วม = amox-clav **ร่วม** macrolide/doxy หรือ FQ เดี่ยว

5. **synth SYN-CHEST-02 explain** | ปรับให้ชัด
   - ก่อน: "อาการเกือบทุกวันและตื่นกลางคืนมากกว่าสัปดาห์ละครั้ง = GINA step 3" (ไม่ตรงกับ stem ที่บอกอาการ 3-4 วัน/สัปดาห์)
   - หลัง: "อาการหลายวันต่อสัปดาห์ (3-4 วัน ใช้ SABA เกือบทุกวัน) และตื่นกลางคืน ≥ 1 ครั้ง/สัปดาห์ = เริ่มที่ GINA step 3"

6. **synth SYN-CHEST-04 explain** | ปรับให้ชัด
   - ก่อน: P/F 110 บน HFNC = ARDS moderate (Berlin ต้องวัดบน PEEP ≥ 5)
   - หลัง: เพิ่มว่าใช้ได้ตามนิยาม global ARDS 2023 (HFNC ≥ 30 L/min) และควรยืนยันซ้ำบน PEEP หลังใส่ท่อ

7. **synth SYN-CHEST-05 explain (ตัวลวง 1)** | ปรับให้ชัด
   - ก่อน: "tension pneumothorax ต้องมี BP ตก"
   - หลัง: "มักมี BP ตก/JVP สูง trachea ถูกดัน เคาะโปร่ง และเห็นลม + เส้น pleura"

8. **synth SYN-CHEST-09 fullcover** | ผิดเล็กน้อย
   - ก่อน: "Dead space (PE, emphysema) เพิ่ม CO2"
   - หลัง: "PE มักมี PaCO2 ต่ำ; CO2 คั่งเมื่อชดเชยไม่ได้ (COPD/emphysema รุนแรง)"

## ข้อรูป (`review/chest_pics_fix.json`)
- **PIC35-22** (CXR, TB สงสัย) | ปรับให้ชัด: รูปเป็นทึบหนาแน่นเกือบทั้ง RUL ต่อถึง hilum (air-space consolidation) ไม่ใช่แค่ patchy/reticulonodular; คำตอบ (sputum AFB + Xpert + culture) ยังถูก เพิ่มให้คิดถึงมะเร็งปอดอุดหลอดลมในผู้สูบบุหรี่ ถ้าเสมหะลบ → CT/bronchoscopy
- **PIC35-23** (CXR, CAP + effusion) | ผิดเล็กน้อย: เฉลยอ่าน "ปอดซ้ายค่อนข้างใส" แต่รูปมี patchy opacity ที่ perihilar/กลางปอดซ้าย = multilobar pneumonia (IDSA/ATS minor criterion) ส่วน right lower/middle consolidation + right effusion (CP angle ขวาทื่อ, diaphragm ขวาหาย) ตรงกับรูป

## จุดที่ตรวจแล้วไม่ต้องแก้ (ตัวอย่าง)
- คำนวณซ้ำด้วย python: SYN-01 pH = 7.26 (HCO3 31, PaCO2 72; acute คาด 27, chronic คาด ~35); SYN-03 AG 22, Winter 32 ± 2 vs 22, delta 1.25, calc osm 291 (gap ~1), pH 7.48; SYN-04 PBW 70.6 kg → 6 mL/kg ≈ 420 mL; SYN-05 Light protein 0.69 / LDH 1.9 / 420 > 167; SYN-06 Posm 255 สอดคล้อง Na 121; SYN-09 PAO2 112, A-a 50, pH 7.49; rep CH-OLD-16 AG 47, delta 3.9, Winter 28.5-32.5 vs 20, pH 7.50
- เกณฑ์/ขนาดยา: NIV (pH ≤ 7.35 + PaCO2 > 45), LTOT, GOLD A/B/E, GINA track 1, PCP steroid (PaO2 < 70 หรือ A-a ≥ 35; pred 40 bid ×5 → 40 ×5 → 20 ×11), TMP 15-20 mg/kg/d, ART ภายใน 2 สัปดาห์, WHO 2021 pre-XDR/XDR, ARDSnet (Vt 6 mL/kg PBW, Pplat ≤ 30, prone P/F < 150), CURB-65 และ IDSA/ATS 2019 major/minor, Light's criteria, chylothorax TG > 110, re-expansion ≤ 1-1.5 L, needle decompression ICS 4-5 AAL/MAL, USPSTF LDCT 50-80 ปี ≥ 20 pack-years
- rifampicin-AIN (SYN-CHEST-07) คำตอบหยุด RIF ถาวรเป็นคำตอบที่ดีที่สุดเพียงข้อเดียว (ตัวลวง "หยุดทุกตัวแล้วใส่กลับทีละตัว" จะ rechallenge rifampicin)
