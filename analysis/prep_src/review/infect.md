# Medical accuracy review: infect

ตรวจ: one_per_theme 30 แก่น (related + fix), synth 11 ข้อ, reps 30 ข้อ, pics 4 ข้อ (เปิดดูรูปครบ 4 รูป)
ภาพรวม: ไม่พบข้อผิดร้ายแรง synth ทุกข้อมีคำตอบที่ดีที่สุดข้อเดียว lab/vital สอดคล้อง (เช่น FVC 1.5 L/70 kg = 21 mL/kg, CSF/serum glucose 0.36, AKI non-oliguric + K 3.1)

## รายการแก้
1. one_per_theme "Tetanus: การรักษาครบ…" related — ปรับให้ชัด — ก่อน: "แผลสกปรกให้ Td เมื่อเข็มสุดท้าย >5 ปี และให้ TIG เพิ่มเมื่อเคยได้ <3 เข็ม" (อ่านได้ว่าได้ TIG อย่างเดียว) → หลัง: แผลสกปรก เคยได้ <3 เข็ม/ไม่ทราบ → Td + TIG; ครบ ≥3 เข็มแต่ >5 ปี → Td อย่างเดียว
2. synth SYN-INFECT-11 fullcover — ปรับให้ชัด — ข้อความเดียวกับข้อ 1
3. one_per_theme "Leptospirosis: การตรวจยืนยัน…" related — ผิดเล็กน้อย — ก่อน: "ไม่ได้ติดจากการถูกหนูกัด" (เด็ดขาดเกินจริง) → หลัง: การถูกหนูกัดเป็นทางที่พบน้อยมาก หนูกัดแล้วมีไข้ให้นึกถึง rat-bite fever
4. synth SYN-INFECT-01 explain — ผิดเล็กน้อย — ก่อน: อ้าง "heart failure จาก AR" ซึ่งโจทย์ไม่ได้ให้ → หลัง: ลิ้นเทียมรั่วใหม่ (diastolic murmur ใหม่ เสี่ยง heart failure)
5. synth SYN-INFECT-03 explain ตัวลวง (4) — ผิดเล็กน้อย — ก่อน: "S. pneumoniae พบบ่อยที่สุดใน HIV ที่ CD4 ยังสูง" (ขัดกับ fullcover ที่ว่าทุกระดับ CD4) → หลัง: พบบ่อยที่สุดทุกระดับ CD4 แต่ภาพไม่เข้า (GP lancet diplococci ไม่แตกแขนง ไม่ทำฝีสมอง)
6. synth SYN-INFECT-04 choices[0] — ปรับให้ชัด — ก่อน: "start ART 4–6 weeks after antifungal therapy" (อ่านได้ว่าหลังจบยา) → หลัง: "…after starting antifungal therapy"
7. synth SYN-INFECT-05 fullcover (Taenia) — ผิดเล็กน้อย — ก่อน: "Taenia solium จากหมูดิบ; ไข่ทำให้ neurocysticercosis" (ชวนเข้าใจว่ากินหมูดิบแล้วเป็น cysticercosis) → หลัง: กินหมูดิบ → taeniasis (praziquantel/niclosamide); กลืนไข่ปนเปื้อนอุจจาระคน → neurocysticercosis; T. saginata ไม่ทำ cysticercosis
8. one_per_theme "HIV กับ pneumonia…" fix (ใหม่) — ผิดเล็กน้อย — note ของข้อตัวแทนเขียน "เฉลย: C. Streptococcus pneumoniae" แต่ตัวเลือก C ในข้อคือ M. tuberculosis → เพิ่ม fix ระบุว่าคำตอบคือ S. pneumoniae (ตัวเลือกสุดท้าย)
9. one_per_theme "Leptospirosis: วินิจฉัยจาก…" fix (ใหม่) — ผิดเล็กน้อย — note ของข้อตัวแทนว่า dengue "ไม่ใช่ไข้กลับขึ้นใหม่" และ jaundice ของ falciparum เป็น indirect อย่างเดียว → fix: dengue มี saddleback fever ได้ จุดแยกคือตัวเหลือง; severe falciparum มีทั้ง indirect และ direct bilirubin

## ตรวจแล้วไม่ต้องแก้ (สาระสำคัญ)
- fix เดิมของ Sepsis (Sepsis-3 → bacteremic pyelonephritis ไม่ใช่ sepsis) และ COVID (หน้ากากผ้า, airborne, ไม่กักตัว 14 วัน) ถูกต้อง
- ขนาดยา/สูตร: GC ceftriaxone 500 mg, chancroid azithro 1 g/ceftriaxone 250 mg, syphilis early vs late vs neuro, DGI ceftriaxone 1 g, M. genitalium doxy → moxi, PVE MSSA (ESC 2023), crypto WHO 2022, PCP steroid เกณฑ์ PaO2 <70, DTG bid กับ rifampicin, melioidosis ceftazidime/meropenem → TMP-SMX 3–6 เดือน, vivax CQ + PQ 14 วัน, doxy prophylaxis ต่อ 4 สัปดาห์ ถูกต้อง
- pics: PIC35-06 (eschar ที่คอใต้หู ตรงกับคำบรรยาย), PIC35-07 (RBC โต + Schüffner's dots + amoeboid trophozoite = vivax), PIC35-05 และ PIC35-04 (India ink เห็นยีสต์มีแคปซูลวงใส บางตัวแตกหน่อ ขนาดเทียบสเกล 10 µm สอดคล้อง) ไม่มีปัญหา → infect_pics_fix.json = []
