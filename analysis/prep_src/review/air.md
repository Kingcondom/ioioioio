# Medical accuracy review: AIR (allergy, immunology, rheumatology)

ตรวจแล้ว: one_per_theme 19 แก่น (related + fix), synth 6 ข้อ, reps 19 ข้อ, pics 4 ข้อ (เปิดดูรูปทั้ง 4 รูปแล้ว)
ผล `python3 check2.py air` = OK

## รายการแก้

1. **one_per_theme "Rheumatoid arthritis: ข้อเล็กสมมาตร, morning stiffness, RF, nodule" related** | ผิดเล็กน้อย
   - ก่อน: "rheumatoid nodule (จำเพาะสุด)"
   - หลัง: "rheumatoid nodule (อาการนอกข้อที่พบบ่อยสุด สัมพันธ์ RF/anti-CCP บวก)"

2. **synth SYN-AIR-02 fullcover** | ผิดเล็กน้อย
   - ก่อน: "nodule จำเพาะสุดนอกข้อ"
   - หลัง: "nodule = อาการนอกข้อที่พบบ่อยสุด"

3. **one_per_theme "จำแนก arthritis (OA/RA/SpA/AOSD/chikungunya)" fix (เพิ่มใหม่)** | ปรับให้ชัด (rep AIR-OLD-13)
   - ก่อน: เฉลย chikungunya ทั้งที่เกล็ดเลือด 45,000 + leukopenia + atypical lymphocyte เข้าได้กับ dengue มากกว่า โดยไม่บอกให้แยก dengue
   - หลัง: fix ว่า chikungunya ถูกเมื่อเทียบตัวเลือก (มีข้ออักเสบจริง) แต่ต้องตรวจ NS1/IgM แยก dengue และเลี่ยง NSAID/aspirin จนกว่าจะตัด dengue

4. **one_per_theme "Chronic urticaria: นิยาม ≥6 สัปดาห์" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ใน note ของ rep AIR-OLDP-005)
   - ก่อน: "12 สัปดาห์เป็นเกณฑ์ ... persistent ITP/chronic ITP"
   - หลัง: ITP newly diagnosed < 3 เดือน, persistent 3-12 เดือน, chronic > 12 เดือน (12 สัปดาห์ = persistent เท่านั้น)

5. **synth SYN-AIR-05 explain** | ปรับให้ชัด
   - ก่อน: "ถ้าไตแย่ลง/nephrotic → biopsy"
   - หลัง: ผู้ใหญ่ควรวัด UPCR ตั้งแต่แรก; biopsy ถ้า proteinuria คงอยู่ > 0.5-1 g/วัน, creatinine ขึ้น หรือ nephrotic

6. **synth SYN-AIR-06 explain (ตัวลวง 1)** | ปรับให้ชัด
   - ก่อน: "GCA ซึ่งต้องมีอาการทางศีรษะ"
   - หลัง: "cranial GCA ซึ่งมักมีอาการทางศีรษะ; ถ้าไข้/ESR ไม่ลดหลัง pred ขนาดต่ำ ให้คิด large-vessel GCA และส่ง imaging"

## ข้อรูป (`review/air_pics_fix.json`)
- **PIC35-15** (urticaria + anaphylaxis): รูปเป็น wheals ขอบชัดรวมกันเป็นแผ่น ตรงกับ urticaria; เฉลย adrenaline 0.5 mg IM ต้นขาถูก → ไม่มีปัญหา
- **PIC35-16** (synovial fluid): เห็นผลึกรูปเข็มยาวปลายแหลมจำนวนมากใต้กล้องธรรมดา ตรงกับ MSU/gout; "yellow when parallel = urate" ถูก → ไม่มีปัญหา
- **PIC35-18** (ใบหน้า, MCTD) | ผิดเล็กน้อย: รูปเห็นเพียงผื่นแดงจางที่แก้ม/จมูก (ตาถูกปิด) ไม่ใช่ "รอบตา" ชัดเจน; pearl "nucleolar = diffuse SSc" ไม่ถูก (anti-Scl-70 ให้ speckled/homogeneous; nucleolar = anti-PM/Scl, Th/To, fibrillarin, RNA pol I) คำตอบ MCTD ถูก
- **PIC35-17** (น้ำไขข้อขุ่น + GNB) | ผิดเล็กน้อย: รูปมีน้ำราว 15 mL (โพยเขียน 50 mL); ถ้าเป็น melioidosis ต้อง ceftazidime/meropenem ≥ 4 สัปดาห์แล้วต่อ TMP-SMX 3-6 เดือน (เฉลยเดิมไม่มี eradication phase)

## จุดที่ตรวจแล้วไม่ต้องแก้ (ตัวอย่าง)
- SYN-AIR-01: eGFR 22 = CKD 4 → allopurinol เริ่ม ≤ 50 mg (ACR 2020), NSAID ห้าม (CKD + PUD), prophylaxis 3-6 เดือน, ข้อบ่งชี้ ULT (tophus, ≥ 2 flare/ปี)
- SYN-AIR-02: ACR/EULAR 2010 = 3 (4-10 ข้อเล็ก) + 3 (anti-CCP สูง) + 1 (ESR/CRP) + 1 (≥ 6 สัปดาห์) = 8; MTX สัปดาห์ละครั้ง + folic acid
- SYN-AIR-04: HCQ 200 mg/60 kg = 3.3 mg/kg (≤ 5); MMF หยุด ≥ 6 สัปดาห์ก่อนตั้งครรภ์ → AZA; โรคสงบ ≥ 6 เดือน; Z-score −2.2 ≤ −2.0 = ต่ำกว่าเกณฑ์อายุ; GIOP (≥ 2.5 mg ≥ 3 เดือน) Ca/vit D และเลี่ยง bisphosphonate ในผู้วางแผนตั้งครรภ์ (ACR 2022)
- SYN-AIR-06: PMR pred 12.5-25 mg (EULAR/ACR 2015), CK ปกติ
- เกณฑ์อื่น: live vaccine ห้ามเมื่อ pred ≥ 20 mg ≥ 14 วัน, HCQ ≤ 5 mg/kg น้ำหนักจริง + ตรวจตาทุกปีหลัง 5 ปี, EULAR/ACR 2019 SLE (ANA ≥ 1:80, ≥ 10 คะแนน), SRC (pred ≥ 15 mg, captopril), GCA (pred 40-60 mg, IV MP 500-1,000 mg × 3), IgAV criteria (EULAR/PRINTO/PRES), DGI ceftriaxone 1 g/วัน ≥ 7 วัน (CDC 2021), urticaria H1 รุ่น 2 ถึง 4 เท่า → omalizumab, adrenaline 0.5 mg IM
