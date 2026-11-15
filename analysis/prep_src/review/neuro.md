# Medical accuracy review: NEURO

ตรวจแล้ว: one_per_theme 40 แก่น (related + fix), synth 15 ข้อ, reps 40 ข้อ, pics 0 ข้อ (`review/in/neuro_pics.json` ว่าง)
ผล `python3 check2.py neuro` = OK

สรุป: ผิดร้ายแรง 0 / ผิดเล็กน้อย 4 / ปรับให้ชัด 5 (รวม 9 จุด)

## รายการแก้

1. **one_per_theme "Eosinophilic meningitis: กินหอยโข่งดิบ → Angiostrongylus" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ในโจทย์และ note ของ rep)
   - ก่อน: CSF ในโจทย์มี PMN 35% + lymphocyte 45% + eosinophil 25% (รวม 105%) และ glucose 20/100 (ratio 0.2) โดย note อ่านว่า "glucose ต่ำกว่าครึ่ง" เหมือนเป็นลักษณะของโรค
   - หลัง: fix บอกว่า differential รวมเกิน 100% และ Angiostrongylus มัก glucose ปกติหรือต่ำเล็กน้อย ถ้า glucose ต่ำมากต้องคิดถึง TB, bacterial หรือเชื้อราร่วมด้วย สิ่งที่ใช้ตอบคือ eosinophil ≥ 10% + หอยโข่งดิบ (คำตอบไม่เปลี่ยน)

2. **one_per_theme "Alcohol withdrawal / delirium tremens → benzodiazepine" fix (เพิ่มใหม่)** | ผิดเล็กน้อย (ใน note ของ rep)
   - ก่อน: note ว่า lorazepam ถูกกำจัดด้วย glucuronidation "ที่ไม่พึ่งตับมาก"
   - หลัง: lorazepam ยังเผาผลาญที่ตับ แต่ผ่าน glucuronidation (phase II) ที่ยังทำงานได้ในโรคตับ และไม่มี active metabolite (คำตอบไม่เปลี่ยน)

3. **one_per_theme "Vertigo: central vs peripheral, CPA tumor" related** | ผิดเล็กน้อย
   - ก่อน: "Vestibular suppressant (dimenhydrinate, betahistine) ใช้ระยะสั้นเท่านั้น"
   - หลัง: vestibular suppressant คือ dimenhydrinate, meclizine, benzodiazepine (ใช้ระยะสั้นเพราะชะลอการชดเชยของสมอง ไม่ใช้รักษา BPPV ซึ่งใช้ Epley) ส่วน betahistine ไม่ใช่ vestibular suppressant ใช้ใน Meniere

4. **one_per_theme "Movement disorders: Parkinson (SNc), focal dystonia, tardive dyskinesia" related** | ผิดเล็กน้อย
   - ก่อน: "...dopamine agonist ... MAO-B inhibitor ระยะยาวมี motor fluctuation/dyskinesia" (อ่านเหมือน MAO-B inhibitor ทำให้เกิด fluctuation) และ VMAT2 inhibitor ระบุแค่ tetrabenazine
   - หลัง: ระบุว่า **levodopa** ใช้ระยะยาวทำให้เกิด motor fluctuation (wearing-off) และ dyskinesia; VMAT2 inhibitor สำหรับ TD = valbenazine, deutetrabenazine (tetrabenazine)

5. **one_per_theme "Facial palsy: UMN vs LMN pattern, Bell palsy, Ramsay Hunt" related** | ปรับให้ชัด
   - ก่อน: "น้ำตาลดลง (greater petrosal)" (อ่านได้เป็น "น้ำตาล" คือ sugar)
   - หลัง: "น้ำตาไหลน้อยลง/ตาแห้ง (greater petrosal)"

6. **one_per_theme "Aphasia: Broca vs Wernicke" related** | ปรับให้ชัด
   - ก่อน: "มักไม่มีอ่อนแรง อาจมี superior quadrantanopia จึงถูกเข้าใจผิดว่าเป็นโรคจิต" (อ่านเหมือน quadrantanopia เป็นเหตุให้ถูกเข้าใจผิด)
   - หลัง: "มักไม่มีอ่อนแรง (อาจมีเพียง superior quadrantanopia) ผู้ป่วยจึงถูกเข้าใจผิดว่าเป็นโรคจิตหรือ delirium"

7. **one_per_theme "Wernicke encephalopathy: confusion, ophthalmoplegia, ataxia" fix (เพิ่มใหม่)** | ปรับให้ชัด (ใน note ของ rep)
   - ก่อน: note ย่อหน้า "ข้อควรระวัง" อ้าง "ข้อ A กับ C" ตามลำดับในโพยเดิม ซึ่งไม่ตรงกับตัวเลือกที่แสดง (caloric test อยู่ลำดับที่ 4, mamillary hypertrophy อยู่ลำดับที่ 2)
   - หลัง: fix ใช้ชื่อตัวเลือกแทนตัวอักษร: คำตอบคือ abnormal caloric test ตัวลวง "hypertrophy of mamillary bodies" ผิด (ระยะเฉียบพลัน = T2/FLAIR สูง, ระยะเรื้อรัง = atrophy)

8. **synth SYN-NEURO-13 explain** | ปรับให้ชัด
   - ก่อน: "เริ่มที่ cortex ส่วนมือซ้าย (contralateral ต่อมือขวา) ... = focal aware motor seizure evolving to bilateral tonic–clonic" (ผู้อ่านเข้าใจผิดได้ว่าเป็นมือซ้าย และโจทย์ไม่ได้บอกว่ารู้ตัวตอนเริ่มชักหรือไม่)
   - หลัง: "เริ่มที่บริเวณมือของ motor cortex ซีกซ้าย (ตรงข้ามกับมือขวา) ... = focal motor onset ที่กลายเป็น focal to bilateral tonic–clonic seizure" (คำตอบไม่เปลี่ยน)

9. **one_per_theme "Restless legs syndrome" fix (เดิม)** | ตรวจแล้วถูก คงไว้
   - หมายเหตุ: ตัวเลือก "Dopaminergic agents are first line" ในข้อ rep ผิดตามแนวทาง AASM 2024/2025 ด้วย (ข้อนี้จึงมีสองตัวเลือกที่ "NOT correct" ตามแนวทางปัจจุบัน) fix เดิมอธิบายไว้แล้ว ไม่นับเป็นจุดแก้

## ข้อรูป
- ไม่มีข้อรูปของระบบนี้ (`review/in/neuro_pics.json` = []) → `review/neuro_pics_fix.json` = []

## จุดที่ตรวจแล้วไม่ต้องแก้ (ตัวอย่าง)
- ค่าที่คำนวณซ้ำ: SYN-NEURO-07 FVC 1.6 L/70 kg = 22.9 mL/kg ลดลง 43% ใน 12 ชม., CSF glucose ratio 70/105 = 0.67 (GBS ปกติ); SYN-NEURO-12 ratio 32/118 = 0.27; SYN-NEURO-03 GCS E3V4M6 = 13; SYN-NEURO-10 E2V2M4 = 8; SYN-NEURO-13 diazepam 10 mg ≈ 0.18 mg/kg, levetiracetam 60 mg/kg × 55 kg = 3,300 mg; SYN-NEURO-01 LKW 07:00 → 09:15 = 2 ชม. 15 นาที, BP 178/96 < 185/110
- เกณฑ์และขนาดยา: alteplase 0.9 mg/kg (max 90), INR > 1.7/platelet < 100,000/DOAC 48 ชม., BP หลังให้ยา < 180/105, thrombectomy 6–24 ชม., DAPT 21 วัน, CEA 70–99% ภายใน 2 สัปดาห์, ICH SBP ~140 + PCC/vit K, cerebellar ICH > 3 ซม./hydrocephalus → suboccipital decompression, nimodipine + vasospasm วันที่ 3–14, IVIG 0.4 g/kg × 5 วัน, FVC 20 mL/kg, ceftriaxone 2 g q12h + ampicillin เมื่ออายุ > 50/DM, dexamethasone 0.15 mg/kg q6h × 4 วัน, cipro 500 mg ครั้งเดียว, acyclovir 10 mg/kg q8h 14–21 วัน, 2HRZE/10HR + dexamethasone, SE second line (LEV 60, fosPHT 20, VPA 40 mg/kg), atropine doubling q5 นาทีจนหลอดลมแห้ง, ห้าม succinylcholine ใน OP, ferritin ≤ 75 ใน RLS, HLA-B*15:02 ก่อน carbamazepine
- fix เดิมของแก่น lumbar spinal stenosis (มีสัญญาณ PAD ร่วม ควรตรวจ ABI) และ RLS ถูกต้องอยู่แล้ว คงไว้
- คำตอบของ rep ทั้ง 40 ข้อถูกตามแนวทางปัจจุบัน (ข้อ stroke on warfarin INR 1.8 → thrombectomy, TOAST, lacune, Bell, Broca, PCA, PCom CN III, cerebellar ICH, SAH, CVST, ฯลฯ)
