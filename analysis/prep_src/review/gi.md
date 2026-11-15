# Medical accuracy review: GI

ตรวจแล้ว: one_per_theme 36 แก่น (related + fix), synth 11 ข้อ, reps 36 ข้อ, pics 1 ข้อ (เปิดดูรูปแล้ว)
ผล `python3 check2.py gi` = OK

## รายการแก้

1. **synth SYN-GI-03 explain** | ผิดเล็กน้อย
   - ก่อน: คิดคะแนน Child–Pugh ให้ ascites ปานกลาง 2 คะแนน รวมได้ Child–Pugh 10 ("ผู้ป่วย Child C 10 คะแนน")
   - หลัง: ascites ปานกลาง (moderate) ได้ 3 คะแนน รวมได้ **Child–Pugh 11 = Child C** และยังอยู่ในเกณฑ์ pre-emptive TIPS (10–13) คำตอบไม่เปลี่ยน

2. **one_per_theme "Esophageal varices: NSBB primary/secondary prophylaxis" related** | ปรับให้ชัด
   - ก่อน: "varices ขนาดใหญ่ มี red wale signs หรือเป็น Child C → NSBB หรือ EVL" (อ่านเหมือนต้องมีครบทุกข้อ)
   - หลัง: "varices ขนาดกลาง–ใหญ่ **หรือ** varices ขนาดเล็กที่มี red wale signs หรือเป็น Child C" ตาม Baveno

3. **one_per_theme "Upper GI bleeding: เดาสาเหตุ (varices, Mallory-Weiss tear)" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ใน note ของ rep)
   - ก่อน: note เขียนว่า "platelet และ AST/ALT/INR ปกติหมด" แต่โจทย์ไม่มีค่า INR และเขียน "Gastric vascular ectasia (GAVE/portal hypertensive gastropathy)" เหมือนเป็นโรคเดียวกัน
   - หลัง: fix บอกว่าสรุปเรื่อง INR ไม่ได้ (ใช้ platelet, AST/ALT และการไม่มีปัจจัยเสี่ยงแทน) และ GAVE กับ PHG เป็นคนละภาวะ คำตอบ Mallory–Weiss ถูกอยู่แล้ว

4. **one_per_theme "Dysentery (invasive diarrhea): กลไก, เดาเชื้อ (Shigella, Campylobacter), stool exam" fix (เพิ่มใหม่)** | ปรับให้ชัด
   - ก่อน: note ของ rep เขียนว่า "คำตอบจึงเป็นตัวเลือก a" แต่ในหน้าที่แสดง Campylobacter jejuni อยู่ลำดับที่ 4 ผู้อ่านอาจเข้าใจผิด
   - หลัง: fix ระบุว่าคำตอบคือ Campylobacter jejuni และ "ตัวเลือก a" หมายถึงลำดับในโพยเดิม

## ข้อรูป
- PIC35-14 (Gram stain, cholera): รูปเป็นแบคทีเรีย Gram-negative รูปแท่งโค้งสั้นจำนวนมากรอบเซลล์ ตรงกับ comma-shaped GNB และเฉลย Vibrio cholerae ตรงกับภาพทางคลินิก ขนาดยา (doxycycline 300 mg หรือ azithromycin 1 g ครั้งเดียว) ถูกต้อง → ไม่มีปัญหา (`review/gi_pics_fix.json` = [])

## จุดที่ตรวจแล้วไม่ต้องแก้ (ตัวอย่าง)
- ค่าที่คำนวณซ้ำ: SAAG 2.6−0.8 = 1.8, PMN 620×0.7 = 434 (SYN-GI-04); paracetamol 15 g/50 kg = 300 mg/kg, King's criteria ยังไม่ครบ (SYN-GI-05); lipase 920/60 ≈ 15 เท่า, Tokyo grade II (WBC >12,000 + ไข้ ≥39 °C, bilirubin ≥5) (SYN-GI-07)
- ขนาดยาและเกณฑ์: albumin ใน SBP (1.5/1 g/kg; Cr >1, BUN >30, bilirubin >4), albumin 6–8 g/L หลังเจาะเกิน 5 L, spironolactone:furosemide 100:40, CDI (fidaxomicin/vancomycin 125 mg qid, fulminant vanc 500 mg + IV metronidazole, severe = WBC ≥15,000 หรือ Cr >1.5), NAC 150/50/100 mg/kg, King's College criteria, cholera WHO 100 mL/kg ใน 3 ชม., melioidosis ceftazidime ≥10–14 วัน + co-trimoxazole 3–6 เดือน, Baveno VII (<20 kPa + plt >150,000)
- fix เดิมของแก่น transaminase pattern (anti-HAV vs HBsAg + anti-HCV) และ C. septicum (colonoscopy) ถูกต้องอยู่แล้ว คงไว้
