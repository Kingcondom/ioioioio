# -*- coding: utf-8 -*-
"""ข้อสอบที่เป็นรูปจากโพย MED35 (Google Doc "MED Y4 | Pastpapers and review from MD35 (RJ)")

แต่ละข้อมี `img` = รายการภาพ (ไฟล์อยู่ใน pic35/img/ และ publish ไว้ที่ pic/ ข้างหน้าเว็บ)
MCQ เขียนคำตอบที่ถูกไว้ choices[0] เสมอ — patch_drill.py สลับตำแหน่งให้แบบ deterministic (seed ตาม id)
`set` = ชุดใน Ward Drill ที่ข้อนี้ไปอยู่
"""

SRC = "โพย MED35"

ITEMS = [
# ───────────────────────────── CARDIO ─────────────────────────────
dict(
 id="PIC35-01", set="cardio", part="MCQ", lec="13",
 lecture="Ischemic heart diseases (AL) (อ.สุรพันธ์)",
 topic="ECG spot diagnosis – anterior STEMI and the culprit artery",
 img=[dict(src="pic/med35-01.jpg", cap="12-lead ECG ของผู้ป่วย")],
 stem="A 65-year-old man with diabetes and hypertension presents with crushing retrosternal chest pain radiating to the left arm for 2 hours, with sweating. BP 136/84 mmHg, PR 98/min, lungs clear, no murmur. His 12-lead ECG is shown. Which coronary artery is most likely occluded?",
 choices=["Left anterior descending artery","Right coronary artery","Left circumflex artery","Posterior descending artery","Left main coronary artery"],
 explain="""**อ่าน ECG ทีละขั้น**
- Sinus rhythm, rate ~90/min, QRS แคบ
- **ST elevation ใน V1–V4 (ถึง V5)** ร่วมกับ **Q wave / QS ใน V1–V3** = กล้ามเนื้อหัวใจผนัง **anteroseptal ถึง anterior** กำลังตาย
- lead ที่ยกตรงกับพื้นที่เลี้ยงของ **LAD** (septum + ผนังหน้า LV) → culprit คือ **LAD**

**จับคู่ lead กับหลอดเลือด (ต้องจำ)**

| ST elevation | ผนัง | หลอดเลือดที่มักอุดตัน |
|---|---|---|
| V1–V2 | Septal | LAD (septal branch) |
| V3–V4 | Anterior | LAD |
| I, aVL, V5–V6 | Lateral | LCx หรือ diagonal ของ LAD |
| II, III, aVF | Inferior | RCA (~80%) หรือ LCx |
| ST depression V1–V3 + R สูง | Posterior | LCx / RCA |

**ทำไมข้ออื่นผิด**
- **RCA / posterior descending**: ให้ ST elevation ที่ II, III, aVF (inferior) — ECG นี้ inferior lead ไม่ยก
- **LCx**: ให้ lateral (I, aVL, V5–V6) หรือ posterior pattern — ไม่ใช่ V1–V4 เด่น
- **Left main**: ภาพที่พบบ่อยคือ **ST depression กระจาย ≥6 lead + ST elevation ที่ aVR** (diffuse subendocardial ischemia) และผู้ป่วยมักช็อก

ข้อสอบ FA ปีนี้ให้ EKG แล้วถามต่อเป็น MEQ: อ่าน EKG → problem list → definitive diagnosis (acute anterolateral STEMI, คิดว่า LAD) → acute management""",
 pearl="ST elevation V1–V4 = LAD · I, aVL, V5–V6 = lateral · II, III, aVF = inferior (RCA) — เห็น inferior STEMI ให้ติด V3R–V4R ทุกครั้ง",
 ref=["MED35 FA MEQ หน้า 4–5 – ให้รูป EKG ให้ interpret แล้วบอก definitive diagnosis → acute anterolateral wall STEMI (LAD)",
      "MED35 FA – โพย MEQ ที่บอกว่า 'MEQ คล้าย ๆ โพยอันนี้' (AC MEQ NL step 3 ข้อสอบชุดที่ 2: EKG ST elevation V1–V5) — ภาพ EKG ในข้อนี้มาจากโพยชุดนั้น"],
 nl=["2.2.1","B7.2.6(1)","B7.3(3)c"]),

dict(
 id="PIC35-02", set="cardio", part="MCQ", lec="13",
 lecture="Ischemic heart diseases (AL) (อ.สุรพันธ์)",
 topic="STEMI at a non-PCI hospital – choosing reperfusion",
 img=[dict(src="pic/med35-02.jpg", cap="12-lead ECG (ภาพจากโพย มีวงสีกำกับ lead ที่ผิดปกติไว้)")],
 stem="A man in his early 80s with diabetes, hypertension and known ischaemic heart disease develops chest tightness while watching television. Previous episodes settled with rest, but this one has persisted for 2 hours. He is at a community hospital without a catheterisation laboratory; transfer for primary PCI would take about 3 hours. BP 142/86 mmHg, PR 63/min, lungs clear, no murmur. His ECG (shown) has ST elevation in I, aVL and V2–V6 with ST depression in III and aVF. He has received aspirin and clopidogrel. Which is the most appropriate next treatment?",
 choices=["Intravenous streptokinase 1.5 million units over 30–60 minutes",
          "Transfer for primary PCI without giving fibrinolysis",
          "Observe and repeat high-sensitivity troponin in 3 hours before deciding",
          "Oral nifedipine plus sublingual isosorbide dinitrate",
          "Intravenous unfractionated heparin alone and admit to the ward"],
 explain="""**กลไก**: STEMI = thrombus อุดหลอดเลือดหัวใจทั้งเส้น ทุกนาทีที่ช้า = กล้ามเนื้อตายเพิ่ม (time is muscle) เป้าหมายคือ **reperfusion ให้เร็วที่สุดภายใน 12 ชั่วโมงหลังเริ่มเจ็บ**

**เลือกวิธี reperfusion**
- Primary PCI ดีที่สุด **ถ้าทำได้ภายใน 120 นาทีนับจากวินิจฉัย**
- ถ้า **คาดว่าเกิน 120 นาที** (เคสนี้ส่งต่อ 3 ชั่วโมง) และไม่มีข้อห้าม → **fibrinolysis ภายใน 10 นาทีหลังวินิจฉัย** (ESC 2023) แล้วส่งต่อทำ CAG ภายใน 2–24 ชม. (pharmaco-invasive)
- ยาในไทยที่ใช้บ่อยคือ **streptokinase 1.5 ล้านยูนิต ใน NSS 100 mL หยดใน 30–60 นาที**
- อายุ >75 ปี: clopidogrel ให้ 75 mg **ไม่ loading** เมื่อใช้ร่วมกับ fibrinolysis

**ทำไมข้ออื่นผิด**
- **ส่งไป primary PCI เลย**: เกินกรอบ 120 นาที → เสียกล้ามเนื้อมากกว่าให้ยาละลายลิ่มเลือดก่อน
- **รอ troponin**: ST elevation ที่เข้าเกณฑ์ + อาการเข้าได้ = วินิจฉัย STEMI ได้ทันที ห้ามรอผลเลือด
- **Nifedipine**: short-acting dihydropyridine ทำให้ reflex tachycardia และเพิ่มการตายใน ACS — **ไม่ใช่การรักษามาตรฐาน** (โพยปีนี้จดว่าอาจารย์เฉลยมี CCB ด้วย — ให้ตอบเป็นยาลดการใช้ออกซิเจน เช่น beta-blocker แทน)
- **Heparin อย่างเดียว**: เป็นแค่ adjunct ไม่เปิดหลอดเลือด

**แนวเฉลยอาจารย์ (FA MEQ หน้า 6)**: reperfusion therapy ด้วย fibrinolytic (streptokinase) + aspirin + clopidogrel + statin · ไม่ต้องบอกชื่อยาก็ได้คะแนน (เช่น antiplatelet, ACEI) · **ไม่ให้คะแนน CAG เพราะโจทย์ไม่ใช่โรงพยาบาลที่ทำ intervention ได้**""",
 pearl="Primary PCI ได้ภายใน 120 นาที → PCI · เกิน 120 นาที → fibrinolysis ภายใน 10 นาที แล้วส่ง CAG 2–24 ชม.",
 ref=["MED35 FA MEQ หน้า 1–6 – ชาย 80+ ปี แน่นหน้าอกขณะดูทีวี U/D DM HT IHD → EKG ST elevation I, aVL, V2–V6 / ST depression II, III, aVF → acute anterolateral STEMI → acute management (เฉลย: fibrinolytic + aspirin + clopidogrel + statin, ไม่ตอบ CAG)"],
 nl=["2.2.1","B7.2.6(1)","2.3.9(6)"]),

dict(
 id="PIC35-03", set="cardio", part="MCQ", lec="36",
 lecture="Common cardiac arrhythmia and basic EKG (AL) (อ.สุรชาติ)",
 topic="ECG spot diagnosis – high-grade (Mobitz II) second-degree AV block",
 img=[dict(src="pic/med35-03.jpg", cap="12-lead ECG พร้อม rhythm strip (V1, II, V5)")],
 stem="A 74-year-old woman presents with fatigue and two episodes of near-syncope over the past week. BP 104/62 mmHg, pulse 32/min and regular. Her ECG is shown. Which statement best describes the conduction abnormality?",
 choices=["Intermittent failure of AV conduction: some P waves are not conducted while the PR interval of conducted beats stays constant",
          "Delayed AV conduction: every P wave is conducted with a fixed PR interval longer than 200 ms",
          "Progressive lengthening of the PR interval until one P wave is not conducted",
          "Complete failure of AV conduction: P waves and QRS complexes are fully dissociated",
          "Sinus arrest: long pauses in which no P waves are generated"],
 explain="""**อ่าน rhythm strip (lead II ด้านล่าง)**
- P wave มาสม่ำเสมอ (atrial rate ~85–90/min) แต่ **QRS ตามมาเพียงทุก ๆ 3 P wave** (3:1) → ventricular rate ~30/min
- **PR ของ beat ที่ conduct ยาวเท่ากันทุกครั้ง** ไม่ค่อย ๆ ยาวขึ้น
- P ที่ไม่ conduct ไม่มีสาเหตุนำ = **intermittent (all-or-none) failure ของ AV conduction** → **second-degree AV block แบบ Mobitz II / high-grade (advanced) AV block**

**ทำไมสำคัญ**: Mobitz II มักเป็นรอยโรคต่ำกว่า AV node (His–Purkinje) → **เสี่ยงกลายเป็น complete heart block และ asystole ทันที** · atropine มักไม่ได้ผล → เตรียม **transcutaneous pacing** / dopamine หรือ adrenaline infusion ถ้าไม่ stable และ **ใส่ permanent pacemaker** เป็นการรักษาหลัก (ตรวจ hyperkalemia, ยา beta-blocker/CCB/digoxin, inferior MI ก่อนเสมอ)

**ทำไมข้ออื่นผิด**
- **Delayed AV conduction (PR >200 ms ทุก beat)** = first-degree AV block — ทุก P ต้อง conduct แต่ ECG นี้มี P ที่ไม่มี QRS ตาม (โพย MED35 จดว่าตอบ "Delayed conduction AV" ซึ่ง **ไม่ตรงกับภาพ** — คำว่า intermittent conduction ตรงกับ Mobitz II มากกว่า)
- **PR ยาวขึ้นเรื่อย ๆ จนหลุด** = Mobitz I (Wenckebach) — ระดับ AV node, มักไม่อันตราย
- **P กับ QRS ไม่สัมพันธ์กันเลย** = third-degree — PR จะเปลี่ยนไปเรื่อย ๆ แต่ภาพนี้ PR ก่อน QRS คงที่
- **Sinus arrest** = ไม่มี P wave ในช่วงหยุด — ภาพนี้ P ยังมาสม่ำเสมอ""",
 pearl="PR คงที่ + มี P หลุด = Mobitz II → pacemaker · PR ค่อย ๆ ยาวแล้วหลุด = Wenckebach · PR ไม่สัมพันธ์ = complete heart block",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 5 – ให้ภาพ EKG type II AV block (Mobitz) ตัวเลือก: Delayed conduction AV / Intermittent conduction AV / Complete conduction AV"],
 nl=["2.3.9(1)","B7.2.5(5)","3.1.12"]),

# ───────────────────────────── INFECTIOUS ─────────────────────────────
dict(
 id="PIC35-04", set="infect", part="OSCE/SAQ", lec="I03",
 lecture="โรคติดเชื้อ: เอชไอวีและโรคติดเชื้อฉวยโอกาส (ยังไม่ระบุคาบ)",
 topic="SAQ – CSF ในผู้ป่วย HIV: India ink และ cryptococcal meningitis",
 station="SAQ (เขียนตอบ) 5 นาที",
 img=[dict(src="pic/med35-04.jpg", cap="ภาพจากการตรวจ CSF (สเกลบาร์ 10 µm)")],
 vignette="ผู้ป่วยชายไทยอายุ 34 ปี ติดเชื้อเอชไอวี ไม่ได้กินยาต้านไวรัส CD4 45 cells/mm3 มาด้วยปวดศีรษะมากขึ้นเรื่อย ๆ 2 สัปดาห์ ไข้ต่ำ ๆ คลื่นไส้อาเจียน\nPE: stiff neck เล็กน้อย ไม่มี focal neurological deficit\nLP: opening pressure 32 cmH2O · นำ CSF ไปตรวจทางห้องปฏิบัติการได้ผลดังภาพ",
 questions=[
  dict(q="1. ภาพนี้เป็นการส่งตรวจทางห้องปฏิบัติการด้วยวิธีใด",
       a="**India ink preparation ของ CSF** (negative staining — หมึกย้อมพื้นหลังให้ดำ แคปซูลของเชื้อไม่ติดสีจึงเห็นเป็นวงใส)\n\nควรส่งคู่กับ **cryptococcal antigen (CrAg) ใน CSF และ serum** ซึ่งไวกว่า India ink มาก (India ink ไวเพียง ~70–80%)"),
  dict(q="2. จงอธิบายสิ่งที่เห็นในภาพ",
       a="- **Yeast cell รูปกลม ขนาดประมาณ 5–10 µm** (เทียบสเกล 10 µm)\n- ล้อมรอบด้วย **วงใสหนา (clear halo) = polysaccharide capsule** บนพื้นหลังดำ\n- บางเซลล์มี **narrow-based budding**"),
  dict(q="3. เชื้อที่เป็นไปได้มากที่สุด 1 ตัว",
       a="***Cryptococcus neoformans*** → cryptococcal meningitis ในผู้ป่วย advanced HIV (CD4 <100)"),
  dict(q="4. ยาที่ใช้รักษา บอกมา 2 ชนิด",
       a="**Induction (≥2 สัปดาห์)**\n- **Amphotericin B deoxycholate 0.7–1.0 mg/kg/day IV** + **flucytosine 100 mg/kg/day** (ถ้าไม่มี flucytosine ใช้ **fluconazole 800–1200 mg/day** แทน)\n- WHO 2022 แนะนำ single high-dose liposomal AmB 10 mg/kg + flucytosine + fluconazole 14 วัน (ถ้ามียา)\n\n**Consolidation**: fluconazole 400–800 mg/day 8 สัปดาห์ → **Maintenance**: fluconazole 200 mg/day จน CD4 >100 และ viral load กดได้ ≥1 ปี\n\n**สิ่งที่ต้องทำร่วม**: เจาะ LP ซ้ำระบายน้ำเมื่อ opening pressure ≥25 cmH2O · **เริ่ม ART หลังเริ่มยาต้านเชื้อรา 4–6 สัปดาห์** (เริ่มเร็วกว่านี้เพิ่มการตายจาก IRIS)")],
 ref=["MED35 FA SAQ ข้อ 1 – คนไข้ HIV เอา CSF มาตรวจพบดังรูป → ส่งตรวจวิธีอะไร (India ink) / อธิบายรูป (encapsulated, halo) / เชื้อ (Cryptococcus neoformans) / ยารักษา 2 ยา",
      "MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 70 – Cryptococcus meningitis (ให้รูป)"],
 nl=["2.3.1-3(7)","B3.2.2(1)","3.1.7"]),

dict(
 id="PIC35-05", set="infect", part="MCQ", lec="I03",
 lecture="โรคติดเชื้อ: เอชไอวีและโรคติดเชื้อฉวยโอกาส (ยังไม่ระบุคาบ)",
 topic="Cryptococcal meningitis – induction therapy and dose",
 img=[dict(src="pic/med35-05.jpg", cap="ภาพจากการตรวจ CSF")],
 stem="A 29-year-old man with untreated HIV infection (CD4 38 cells/mm3) has had progressive headache and fever for 3 weeks. Lumbar puncture: opening pressure 30 cmH2O, CSF WBC 20 cells/mm3 (lymphocytes 90%), protein 80 mg/dL, glucose 35 mg/dL (blood glucose 100 mg/dL). The CSF preparation is shown. Which is the most appropriate initial treatment?",
 choices=["Amphotericin B deoxycholate 0.7–1.0 mg/kg/day IV plus flucytosine",
          "Amphotericin B deoxycholate 0.3 mg/kg/day IV alone",
          "Oral fluconazole 200 mg once daily alone",
          "Start antiretroviral therapy today and add antifungal therapy after 2 weeks",
          "Ceftriaxone 2 g IV every 12 hours plus vancomycin"],
 explain="""**ภาพ**: India ink ของ CSF พบ yeast กลมจำนวนมากล้อมด้วยวงใส (capsule) → ***Cryptococcus neoformans***

**Induction ที่ถูกต้อง** = ยาที่ฆ่าเชื้อเร็ว (fungicidal) ให้ CSF ปลอดเชื้อเร็วที่สุด: **AmB deoxycholate 0.7–1.0 mg/kg/day + flucytosine 100 mg/kg/day อย่างน้อย 2 สัปดาห์** (ไม่มี flucytosine → AmB + fluconazole 800 mg/day) แล้วต่อ consolidation fluconazole

**ทำไมข้ออื่นผิด**
- **AmB 0.3 mg/kg/day**: ขนาดต่ำเกินไป ฆ่าเชื้อไม่พอ (ตัวเลือกนี้ออกในข้อสอบจริงเพื่อดูว่าจำ dose ได้ไหม — ข้อสอบ FA ให้ 0.7 vs 0.3)
- **Fluconazole 200 mg เดี่ยว ๆ**: เป็นยา fungistatic ขนาด maintenance — ใช้เป็น induction เดี่ยวแล้วการตายสูง
- **เริ่ม ART ทันที**: ใน cryptococcal meningitis การเริ่ม ART เร็ว (<2 สัปดาห์) **เพิ่มการตายจาก IRIS** (COAT trial) → เริ่มหลัง antifungal 4–6 สัปดาห์
- **Ceftriaxone + vancomycin**: เป็นสูตร bacterial meningitis — CSF lymphocyte เด่น glucose ต่ำปานกลาง + India ink บวก ไม่ใช่แบคทีเรีย

อย่าลืม **therapeutic LP ซ้ำ** เมื่อ opening pressure ≥25 cmH2O — ความดันในกะโหลกสูงเป็นสาเหตุตายหลักในสัปดาห์แรก""",
 pearl="Crypto meningitis: AmB 0.7–1 mg/kg/d + 5-FC 2 สัปดาห์ → fluconazole 400–800 × 8 สัปดาห์ → 200/d · ART หลัง 4–6 สัปดาห์ · LP ระบายถ้า OP ≥25",
 ref=["MED35 FA MCQ – บอกอาการคนไข้ cryptococcosis ให้ยาอะไร *จำ dose* (Amphotericin B 0.7 / fluconazole IV / Amphotericin B 0.3)",
      "MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 70 – Cryptococcus meningitis (ให้รูป India ink)"],
 nl=["2.3.1-3(7)","B3.2.2(1)"]),

dict(
 id="PIC35-06", set="infect", part="MCQ", lec="I02",
 lecture="โรคติดเชื้อ: ไข้เฉียบพลันในเขตร้อน (ยังไม่ระบุคาบ)",
 topic="Spot diagnosis – eschar of scrub typhus",
 img=[dict(src="pic/med35-06.jpg", cap="รอยโรคที่พบเมื่อแหวกผมดูบริเวณคอหลังหู")],
 stem="A 9-year-old girl from a rural village in northern Thailand has had high fever, headache and myalgia for 6 days. On examination she has tender cervical lymph nodes, and the painless lesion shown is found on her neck behind the ear. Platelets 110,000/mm3, AST 85 U/L, ALT 70 U/L. Which is the most likely diagnosis?",
 choices=["Scrub typhus","Leptospirosis","Dengue infection","Cutaneous anthrax","Murine typhus"],
 explain="""**ภาพ**: แผลกลมขนาดเล็ก **ตรงกลางเป็นสะเก็ดดำ ขอบแดง ไม่เจ็บ = eschar** ตรงตำแหน่งที่ตัวไรอ่อน (chigger) กัด — ไรชอบกัดบริเวณอับชื้นและเสื้อผ้ารัด (ขาหนีบ รักแร้ ขอบกางเกง ใต้ราวนม **หลังหู คอ**) จึงต้องแหวกผมและถอดเสื้อผ้าหาเสมอ

**Scrub typhus** (*Orientia tsutsugamushi*): ไข้สูง ปวดศีรษะ ปวดเมื่อย + **eschar** + ต่อมน้ำเหลืองโตใกล้แผล ± ผื่น maculopapular, เกล็ดเลือดต่ำ, transaminase สูง → รักษา **doxycycline** (ใช้ได้ในเด็กเป็นระยะสั้น) หรือ azithromycin (หญิงตั้งครรภ์)

**ทำไมข้ออื่นผิด**
- **Leptospirosis**: ปวดน่อง conjunctival suffusion ประวัติลุยน้ำ — **ไม่มี eschar**
- **Dengue**: ไข้ เกล็ดเลือดต่ำ ได้ แต่ไม่มี eschar และไม่มีต่อมน้ำเหลืองกดเจ็บเฉพาะที่
- **Cutaneous anthrax**: eschar ดำไม่เจ็บเหมือนกัน แต่มี **บวมน้ำรอบแผลมาก (massive non-pitting edema)** และประวัติสัมผัสสัตว์/หนังสัตว์
- **Murine typhus**: อาการคล้าย scrub แต่ติดจากหมัดหนู **ไม่มี eschar**""",
 pearl="ไข้ไม่ทราบสาเหตุในไทย → ถอดเสื้อผ้าหา eschar ทุกจุดอับ · เจอ eschar = scrub typhus จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ → doxycycline",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 64 – แผลดำเล็กที่คอ (ให้รูป) ตอบ scrub typhus",
      "MED35 สอบลงกองครั้งที่ 2 MCQ ข้อ 44 – low-grade fever, painless black eschar at neck → scrub typhus"],
 nl=["2.3.1","2.1.1"]),

dict(
 id="PIC35-07", set="infect", part="MCQ", lec="I02",
 lecture="โรคติดเชื้อ: ไข้เฉียบพลันในเขตร้อน (ยังไม่ระบุคาบ)",
 topic="Malaria blood film – Plasmodium vivax and radical cure",
 img=[dict(src="pic/med35-07.jpg", cap="Thin blood film (Giemsa)")],
 stem="A 32-year-old soldier returned from the Thai–Myanmar border 2 weeks ago and has had fever with chills every other day for 5 days. He is alert, with no jaundice, bleeding or hypotension. Hct 38%, platelets 98,000/mm3, creatinine 0.9 mg/dL. His thin blood film is shown. G6PD activity is normal. Which is the most appropriate treatment?",
 choices=["Chloroquine for 3 days plus primaquine for 14 days",
          "Chloroquine for 3 days alone",
          "Intravenous artesunate",
          "Single low-dose primaquine 0.25 mg/kg alone",
          "Oral doxycycline for 7 days"],
 explain="""**ภาพ**: เม็ดเลือดแดงที่ติดเชื้อ **ขยายใหญ่กว่าเม็ดข้างเคียง** มี trophozoite รูปร่างไม่แน่นอน (amoeboid) และ **จุดแดงละเอียดทั่วเซลล์ (Schüffner's dots)** → ***P. vivax*** (หรือ *P. ovale*) — ทั้งสองตัวชอบเม็ดเลือดแดงตัวอ่อน (reticulocyte) เซลล์จึงใหญ่

**รักษา 2 เป้าหมาย**
1. **Blood stage**: **chloroquine** 3 วัน (รวม 25 mg base/kg) — vivax ในไทยยังไวต่อ chloroquine
2. **Liver stage (hypnozoite) → radical cure**: **primaquine 0.25 mg/kg/day × 14 วัน** (หรือ 0.5 mg/kg/day × 7 วัน) ป้องกันการกลับเป็นซ้ำ — **ต้องตรวจ G6PD ก่อน** (G6PD พร่องเสี่ยง hemolysis)

**ทำไมข้ออื่นผิด**
- **Chloroquine อย่างเดียว**: หายรอบนี้แต่ hypnozoite ในตับยังอยู่ → relapse ภายในไม่กี่สัปดาห์–เดือน
- **IV artesunate**: สำหรับ **severe malaria** (ซึม ชัก ตัวเหลือง ไตวาย ช็อก parasitemia สูง) — เคสนี้ไม่มีอาการรุนแรง
- **Primaquine single low dose**: ใช้ฆ่า gametocyte ของ ***P. falciparum*** เพื่อตัดการแพร่เชื้อ — ไม่ใช่ radical cure ของ vivax
- **Doxycycline เดี่ยว**: ออกฤทธิ์ช้า ใช้เป็นยาเสริมหรือป้องกัน ไม่ใช่การรักษาหลัก

**เทียบ falciparum**: RBC ขนาดปกติ หลาย ring ในเซลล์เดียว headphone ring, gametocyte รูปกล้วย → ACT (เช่น artemether–lumefantrine) + single low-dose primaquine""",
 pearl="RBC โต + Schüffner's dots = vivax/ovale → chloroquine 3 วัน + primaquine 14 วัน (ตรวจ G6PD ก่อน)",
 ref=["MED35 สอบลงกองครั้งที่ 2 MCQ – ให้รูป PBS: RBC ใหญ่กว่าปกติ P. vivax/ovale treatment → Chloroquine + Primaquine"],
 nl=["2.3.1","2.1.1"]),

# ───────────────────────────── DERM ─────────────────────────────
dict(
 id="PIC35-08", set="derm", part="OSCE/SAQ", lec="D02",
 lecture="ผิวหนัง: ผื่นเรื้อรังและผื่นจากการติดเชื้อที่พบบ่อย (ยังไม่ระบุคาบ)",
 topic="SAQ – ผื่นด่างขาวที่หลังและผล KOH: pityriasis versicolor",
 station="SAQ (เขียนตอบ) 5 นาที",
 img=[dict(src="pic/med35-08a.jpg", cap="ภาพที่ 1 — ผื่นที่หลังของผู้ป่วย"),
      dict(src="pic/med35-08b.jpg", cap="ภาพที่ 2 — ผลตรวจขูดผิวหนังที่ส่งตรวจในข้อ 2")],
 vignette="ผู้ป่วยชายไทยอายุ 24 ปี อาชีพพนักงานส่งของ มีผื่นที่หลังมา 3 เดือน คันเล็กน้อยเวลาเหงื่อออก เป็นมากขึ้นช่วงหน้าร้อน ผื่นมีลักษณะดังภาพที่ 1",
 questions=[
  dict(q="1. จงอธิบายลักษณะผื่นผิวหนัง",
       a="- **Multiple well-defined hypopigmented macules and patches** หลายขนาด บางส่วนรวมกันเป็นปื้นใหญ่\n- ผิวมี **fine (furfuraceous) scale** — ขูดหรือดึงผิวให้ตึงแล้ว scale ชัดขึ้น (evoked scale sign)\n- กระจายที่ **หลังส่วนบนและไหล่** (บริเวณที่มีต่อมไขมันมาก)"),
  dict(q="2. จะส่งตรวจทางห้องปฏิบัติการอะไร",
       a="**KOH preparation** (10–20% KOH) ของสะเก็ดที่ขูดจากผื่น · อาจใช้ Wood's lamp เสริม (เรืองแสงสีเหลืองอมเขียว)"),
  dict(q="3. จงอธิบายลักษณะเชื้อราในภาพที่ 2",
       a="พบ **เส้นใยราสั้น ๆ (short hyphae) ปนกับกลุ่มสปอร์กลม (clusters of round yeast cells)** = ลักษณะ **\"spaghetti and meatballs\"**"),
  dict(q="4. เชื้อราที่เป็นไปได้มากที่สุด 1 ตัว",
       a="***Malassezia furfur*** (กลุ่ม *Malassezia* spp. เช่น *M. globosa*) → **Pityriasis (tinea) versicolor**"),
  dict(q="5. (ฝึกเพิ่ม) การรักษาและคำแนะนำ",
       a="- ยาทา/สระ: **ketoconazole 2% shampoo** หรือ **selenium sulfide 2.5%** ทิ้งไว้ 5–10 นาทีแล้วล้าง วันละครั้ง 1–2 สัปดาห์\n- ผื่นกว้างหรือเป็นซ้ำ: **itraconazole 200 mg/day 5–7 วัน** หรือ **fluconazole 300 mg สัปดาห์ละครั้ง × 2**\n- **Oral terbinafine และ griseofulvin ไม่ได้ผล** กับ pityriasis versicolor\n- บอกผู้ป่วยว่า **สีผิวจะกลับมาเป็นปกติช้าเป็นเดือน** แม้เชื้อหายแล้ว และกลับเป็นซ้ำได้บ่อยในหน้าร้อน")],
 ref=["MED35 FA SAQ ข้อ 2 – ผู้ชาย แผ่นหลังมีลักษณะดังรูป → อธิบายลักษณะผิว / ส่ง lab อะไร (KOH) / ให้รูป KOH อธิบายลักษณะรา / Diag ราที่เป็นไปได้มากสุด (Malassezia furfur)"],
 nl=["2.3.12(11)"]),

dict(
 id="PIC35-09", set="derm", part="MCQ", lec="D02",
 lecture="ผิวหนัง: ผื่นเรื้อรังและผื่นจากการติดเชื้อที่พบบ่อย (ยังไม่ระบุคาบ)",
 topic="KOH preparation – 'spaghetti and meatballs'",
 img=[dict(src="pic/med35-09.jpg", cap="KOH preparation ของสะเก็ดผิวหนัง")],
 stem="A 20-year-old man has asymptomatic, finely scaling hypopigmented macules over his upper back and chest that become more extensive every hot season. A potassium hydroxide (KOH) preparation of skin scrapings is shown. Which is the most likely causative organism?",
 choices=["Malassezia furfur","Trichophyton rubrum","Candida albicans","Microsporum canis","Corynebacterium minutissimum"],
 explain="""**ภาพ**: เส้นใยราสั้น ๆ ขาดเป็นท่อน ปนกับ **กลุ่มของ yeast กลม** = **spaghetti (hyphae) and meatballs (spores)** → ***Malassezia furfur*** = pityriasis versicolor

*Malassezia* เป็นยีสต์ประจำถิ่นบนผิวที่มีไขมัน เมื่ออากาศร้อนชื้น/เหงื่อมาก จะเปลี่ยนเป็นรูปเส้นใย สร้าง **azelaic acid ยับยั้ง tyrosinase** → ผิวสีจางลง (hypopigmented) — ในคนผิวขาวอาจเห็นเป็นสีชมพูหรือน้ำตาลได้ จึงเรียก "versicolor"

**ทำไมข้ออื่นผิด**
- ***Trichophyton rubrum***: dermatophyte → KOH เห็น **เส้นใยยาว แตกกิ่ง มีผนังกั้น (long branching septate hyphae)** ไม่มีกลุ่มสปอร์ · ผื่น tinea เป็นวงขอบนูนแดง active border
- ***Candida albicans***: budding yeast + pseudohyphae ได้เหมือนกัน แต่ผื่นอยู่ **ซอกพับเปียกชื้น** สีแดงสด มี **satellite pustules** — ไม่ใช่ด่างขาวที่หลัง
- ***Microsporum canis***: dermatophyte จากแมว → tinea capitis/corporis, Wood's lamp สีเขียวที่เส้นผม
- ***Corynebacterium minutissimum***: แบคทีเรีย → erythrasma ที่ซอกพับ สีน้ำตาลแดง Wood's lamp **coral-red** — KOH ไม่พบเชื้อรา""",
 pearl="Spaghetti and meatballs = Malassezia (pityriasis versicolor) · รักษาด้วย azole/selenium — terbinafine กินไม่ได้ผล",
 ref=["MED35 FA SAQ ข้อ 2 – ให้รูป KOH อธิบายลักษณะรา และ Diag ราที่เป็นไปได้มากสุด → Malassezia furfur"],
 nl=["2.3.12(11)"]),

dict(
 id="PIC35-10", set="derm", part="MCQ", lec="D02",
 lecture="ผิวหนัง: ผื่นเรื้อรังและผื่นจากการติดเชื้อที่พบบ่อย (ยังไม่ระบุคาบ)",
 topic="Spot diagnosis – thickened yellow toenails",
 img=[dict(src="pic/med35-10.jpg", cap="เล็บเท้าของผู้ป่วย")],
 stem="A 58-year-old man with type 2 diabetes has had thickened, yellow-brown, crumbly toenails for 2 years. The change began at the free edge of the great toenail and has spread towards the cuticle, as shown. The nail folds are not swollen or tender, and he has no skin plaques elsewhere. Which is the most likely diagnosis?",
 choices=["Tinea unguium (dermatophyte onychomycosis)","Psoriatic nail disease","Chronic candidal paronychia","Subungual melanoma","Green nail syndrome (Pseudomonas)"],
 explain="""**ภาพ**: เล็บนิ้วโป้งเท้า **หนา สีเหลืองน้ำตาล ขุ่น เปราะ ร่อนเป็นผง** เริ่มจากปลายเล็บและขอบข้างแล้วลามเข้าหาโคน มี **subungual hyperkeratosis** = **distal lateral subungual onychomycosis** ซึ่งเป็นแบบที่พบบ่อยที่สุดของ **tinea unguium** (เชื้อหลัก ***Trichophyton rubrum***)

**ยืนยันก่อนให้ยากิน**: KOH / เพาะเชื้อ / PAS ของเศษเล็บ (โรคเล็บอื่นหน้าตาคล้ายกันได้)

**รักษา**: **terbinafine 250 mg/day 12 สัปดาห์** (เล็บเท้า; เล็บมือ 6 สัปดาห์) ตรวจ LFT ก่อน · ทางเลือก itraconazole pulse · ยาทา (ciclopirox, efinaconazole) เมื่อเป็นน้อย ไม่ลามถึงโคนเล็บ · ในผู้ป่วยเบาหวานควรรักษาเพราะเป็นทางเข้าของ cellulitis

**ทำไมข้ออื่นผิด**
- **Psoriatic nail**: nail pitting, oil-drop sign, onycholysis มักหลายเล็บ **โดยเฉพาะเล็บมือ** และมีผื่นสะเก็ดเงินที่อื่น
- **Candidal paronychia**: **รอบเล็บบวมแดง กดเจ็บ cuticle หาย** พบในคนที่มือเปียกบ่อย — ภาพนี้รอบเล็บปกติ
- **Subungual melanoma**: **แถบสีดำ/น้ำตาลตามยาวเล็บ** กว้างขึ้น หรือสีลามออกมาที่ผิวรอบเล็บ (Hutchinson sign)
- **Green nail**: เล็บมีสี **เขียวดำ** จาก pyocyanin มักร่วมกับ onycholysis""",
 pearl="เล็บเท้าหนาเหลืองเปราะเริ่มจากปลายเล็บ = tinea unguium (T. rubrum) → ยืนยันด้วย KOH/culture แล้ว terbinafine 12 สัปดาห์",
 ref=["MED35 สอบลงกองครั้งที่ 2 MCQ – ให้รูปเล็บเท้า ถามเชื้อ/โรค ตอบ Tinea unguium"],
 nl=["2.3.12(11)"]),

dict(
 id="PIC35-11", set="derm", part="MCQ", lec="D02",
 lecture="ผิวหนัง: ผื่นเรื้อรังและผื่นจากการติดเชื้อที่พบบ่อย (ยังไม่ระบุคาบ)",
 topic="Spot diagnosis – unilateral dermatomal vesicular rash on the back",
 img=[dict(src="pic/med35-11.jpg", cap="ผื่นของผู้ป่วย")],
 stem="A 64-year-old man had burning pain over the right side of his back and flank for 3 days, followed 1 day ago by the eruption shown. The rash does not cross the midline. Which is the most likely diagnosis?",
 choices=["Herpes zoster","Herpes simplex infection","Allergic contact dermatitis","Bullous impetigo","Dermatitis herpetiformis"],
 explain="""**ภาพ**: กลุ่มตุ่มน้ำใสและตุ่มหนองเล็ก ๆ บนพื้นแดง (grouped vesicles on an erythematous base) เรียงเป็นแถบ **ตาม dermatome ด้านเดียว ไม่ข้ามแนวกลางลำตัว** → **herpes zoster (shingles)**

**กลไก**: varicella-zoster virus แฝงใน dorsal root ganglion หลังเป็นอีสุกอีใส เมื่อภูมิคุ้มกันชนิดเซลล์ลดลง (อายุมาก, ยากดภูมิ, HIV) ไวรัส reactivate วิ่งตามเส้นประสาทออกมาที่ผิว → **ปวดแสบร้อนนำมาก่อนผื่น 1–5 วัน** (prodrome) แล้วจึงเกิดผื่นใน dermatome เดียวกัน

**รักษา**: เริ่มยาต้านไวรัส **ภายใน 72 ชั่วโมง** — **valacyclovir 1 g tid × 7 วัน** หรือ **acyclovir 800 mg 5 ครั้ง/วัน × 7 วัน** ลดระยะเวลาผื่นและความเสี่ยง **postherpetic neuralgia** · ป้องกันด้วย recombinant zoster vaccine ในอายุ ≥50 ปี

**ทำไมข้ออื่นผิด**
- **Herpes simplex**: ตุ่มน้ำกลุ่มเดียวเล็ก ๆ ที่ริมฝีปาก/อวัยวะเพศ เป็นซ้ำที่เดิม — ไม่เรียงยาวตาม dermatome
- **Contact dermatitis**: คัน ผื่นมีขอบตามรูปสิ่งที่สัมผัส (เส้นตรง รูปเข็มขัด) ไม่มีปวดแสบนำ
- **Bullous impetigo**: ตุ่มพองเหลวขนาดใหญ่ แตกเป็นแผลตื้นขอบสะเก็ด ไม่ตาม dermatome
- **Dermatitis herpetiformis**: ตุ่มคันมาก **สมมาตร** ที่ศอก เข่า ก้น สัมพันธ์กับ celiac disease""",
 pearl="ปวดแสบนำ 2–3 วัน + ตุ่มน้ำเป็นกลุ่มตาม dermatome ข้างเดียว = zoster → antiviral ภายใน 72 ชม.",
 ref=["MED35 สอบลงกองครั้งที่ 2 MCQ – ให้รูปผื่นตาม dermatome ข้างหลัง → herpes zoster"],
 nl=["2.3.12","2.3.1"]),

dict(
 id="PIC35-12", set="derm", part="MCQ", lec="D01",
 lecture="ผิวหนัง: ผื่นเฉียบพลันและภาวะฉุกเฉินทางผิวหนัง (ยังไม่ระบุคาบ)",
 topic="Spot diagnosis – vesicular rash that starts on the face then spreads to the trunk",
 img=[dict(src="pic/med35-12.jpg", cap="ใบหน้าของผู้ป่วยวันที่ 2 ของผื่น")],
 stem="A 16-year-old boy has had low-grade fever and malaise for 2 days. An itchy rash began on his face and scalp and spread to his trunk over the following day. His face is shown. He has no history of eczema. Which is the most likely diagnosis?",
 choices=["Varicella (chickenpox)","Bullous impetigo","Mpox","Hand, foot and mouth disease","Eczema herpeticum"],
 explain="""**ภาพ**: ผื่นหลายระยะ **อยู่พร้อมกันในบริเวณเดียว** — papule, vesicle ใสบนฐานแดง ("dew drop on a rose petal"), ตุ่มหนองบุ๋มกลาง และสะเก็ด → ลักษณะ **"lesions in different stages"**

ร่วมกับประวัติ **ผื่นเริ่มที่หน้าและหนังศีรษะแล้วลามลงลำตัว** + ไข้ต่ำ คัน → **varicella (chickenpox)** ผื่นจะหนาแน่นที่ลำตัว (centripetal)

**การดูแล**: วัยรุ่นและผู้ใหญ่มักเป็นรุนแรงกว่าเด็ก (pneumonitis) → ให้ **acyclovir 800 mg 5 ครั้ง/วัน × 5–7 วัน หรือ valacyclovir 1 g tid** ถ้าเริ่มภายใน 24 ชม.หลังผื่นขึ้น · ห้ามให้ aspirin (Reye syndrome) · แยกผู้ป่วยแบบ airborne + contact **จนทุกตุ่มตกสะเก็ด**

**ทำไมข้ออื่นผิด**
- **Bullous impetigo** (โพย MED35 ลังเลว่าเป็นข้อนี้): ตุ่มพองเหลว **ขนาดใหญ่** แตกเป็นแผลตื้นขอบสะเก็ด เฉพาะที่ ไม่มีไข้ และ **ไม่ลามจากหน้าลงตัวตามลำดับ** — ผื่นไม่ได้มีหลายระยะพร้อมกัน
- **Mpox**: ผื่น **ระยะเดียวกันทั้งหมด** หนาแน่นที่หน้า มือ เท้า (centrifugal) และ **ต่อมน้ำเหลืองโตเด่น**
- **Hand, foot and mouth disease**: ตุ่มน้ำรูปรีที่ฝ่ามือ ฝ่าเท้า แผลในปาก ส่วนใหญ่เด็กเล็ก
- **Eczema herpeticum**: HSV บนผิวที่เป็น atopic dermatitis อยู่เดิม — ตุ่มบุ๋มกลาง monomorphic เป็นกลุ่ม ผู้ป่วยไม่มีประวัติ eczema""",
 pearl="ผื่นเริ่มหน้า→ลำตัว + ผื่นหลายระยะพร้อมกัน = varicella · ผื่นระยะเดียวกัน + ต่อมน้ำเหลืองโต = mpox/smallpox",
 ref=["MED35 สอบลงกองครั้งที่ 2 MCQ ข้อ 83 – ผื่นแบบนี้ขึ้นหน้าก่อนตัว (ให้รูป) — โพยจดว่า 'คล้าย ๆ รูปนี้ bullous impetigo??' (ไม่แน่ใจ; ลักษณะในโจทย์เข้าได้กับ varicella มากกว่า)"],
 nl=["2.3.12","2.3.1"]),

# ───────────────────────────── ENDO ─────────────────────────────
dict(
 id="PIC35-13", set="endo", part="MCQ", lec="E06",
 lecture="Thyroid disorders (อ.ศิวกร)",
 topic="Thyroid scan – single hot nodule",
 img=[dict(src="pic/med35-13.jpg", cap="Thyroid scan ของผู้ป่วย (ขวา) เทียบกับภาพปกติ (ซ้าย)")],
 stem="A 45-year-old woman with hypertension has had heat intolerance, sweating and weight loss for 4 months. There is no exophthalmos and no thyroid bruit. A firm, mobile 3-cm nodule is palpable in the right thyroid lobe. TSH <0.01 mIU/L (0.4–4.0), free T4 2.6 ng/dL (0.9–1.7), free T3 7.8 pg/mL (2.3–4.2). Her thyroid scan is shown next to a normal scan. Which is the most compatible diagnosis?",
 choices=["Toxic adenoma","Graves disease","Toxic multinodular goiter","Thyroiditis","Sick euthyroid syndrome"],
 explain="""**ภาพ**: scan ของผู้ป่วยมี **จุดจับสารรังสีเข้มจุดเดียว (single hot nodule)** ตรงตำแหน่งก้อน ขณะที่ **เนื้อต่อมส่วนที่เหลือแทบไม่จับสารเลย** (เทียบกับภาพปกติที่เห็นทั้งสองกลีบ)

**กลไก**: ก้อนทำงานอิสระ (autonomous — มักมี activating mutation ของ TSH receptor) สร้างฮอร์โมนเกิน → **TSH ถูกกด** → เนื้อต่อมปกติที่ต้องพึ่ง TSH หยุดจับสาร = ภาพ hot nodule + suppressed background = **toxic adenoma**

**ทำไมข้ออื่นผิด**
- **Graves disease**: จับสาร **เพิ่มทั่วทั้งต่อมสม่ำเสมอ (diffuse homogeneous)** มักมี exophthalmos, bruit, pretibial myxedema, TRAb บวก
- **Toxic multinodular goiter**: **หลายจุดร้อนสลับจุดเย็น (patchy)** ในต่อมที่โตเป็นปุ่ม ผู้สูงอายุ
- **Thyroiditis** (subacute/painless/postpartum): ฮอร์โมนรั่วจากต่อมที่ถูกทำลาย → **uptake ต่ำหรือไม่จับเลย**
- **Sick euthyroid**: คนป่วยหนัก **T3 ต่ำ** TSH ปกติหรือต่ำเล็กน้อย — ไม่ใช่ภาวะ hyperthyroid

**ต่อ**: hot nodule แทบไม่เป็นมะเร็ง (<1%) จึง **ไม่ต้อง FNA** · รักษาหายขาดด้วย **radioactive iodine หรือ lobectomy** (ยาต้านไทรอยด์คุมได้แต่ไม่หาย)""",
 pearl="Hyperthyroid + ก้อนเดียว → thyroid scan: hot nodule กดเนื้อรอบข้าง = toxic adenoma (ไม่ต้อง FNA) · diffuse = Graves · patchy = TMNG · uptake ต่ำ = thyroiditis",
 ref=["MED35 FA SAQ ข้อ 3 – หญิง HT ขี้ร้อน เหงื่อออกมาก no exophthalmos no bruit ก้อน thyroid 3 cm ขยับได้ TSH ต่ำ FT3 FT4 สูง → แปลผล / ส่งตรวจเพิ่ม (thyroid scan 20 คะแนน, RAI uptake 10 คะแนน) / Diag → toxic adenoma",
      "MED35 LMS – ภาพ thyroid scan เทียบ normal (hot nodule ก้อนใหญ่ดำ) เฉลย Toxic adenoma — ภาพในข้อนี้มาจาก LMS ข้อนั้น"],
 nl=["2.3.4","2.1.53"]),

# ───────────────────────────── GI ─────────────────────────────
dict(
 id="PIC35-14", set="gi", part="MCQ", lec="G03",
 lecture="ระบบทางเดินอาหาร: ลำไส้ ตับอ่อน และอาการท้องเสีย (ยังไม่ระบุคาบ)",
 topic="Gram stain of stool – acute watery diarrhoea",
 img=[dict(src="pic/med35-14.jpg", cap="Gram stain จากสิ่งส่งตรวจของผู้ป่วย")],
 stem="A 30-year-old man has had profuse, painless watery diarrhoea for 1 day — more than 15 episodes of pale 'rice-water' stool — with vomiting but no fever. He is lethargic, with sunken eyes and poor skin turgor. BP 84/50 mmHg, PR 124/min. A Gram stain of the stool is shown. Which is the most likely causative organism?",
 choices=["Vibrio cholerae","Campylobacter jejuni","Shigella dysenteriae","Enterotoxigenic Escherichia coli","Clostridioides difficile"],
 explain="""**ภาพ**: แบคทีเรีย **ติดสีแดง (Gram-negative) รูปแท่งโค้งเหมือนเครื่องหมายจุลภาค (comma-shaped)** กระจายอยู่รอบเซลล์เยื่อบุ → ***Vibrio cholerae***

**กลไก**: cholera toxin จับ GM1 ที่เยื่อบุลำไส้เล็ก → กระตุ้น Gs → **cAMP สูง** → CFTR หลั่ง Cl⁻ และน้ำออกมาในลำไส้ **โดยเซลล์ไม่ถูกทำลาย** → ถ่ายน้ำปริมาณมหาศาล **ไม่มีไข้ ไม่มีเลือด ไม่ปวดท้องมาก** อุจจาระเหมือนน้ำซาวข้าว → ขาดน้ำรุนแรง ช็อก hypokalemia และ metabolic acidosis ภายในไม่กี่ชั่วโมง

**รักษา**: สิ่งที่ช่วยชีวิตคือ **สารน้ำ** — IV **Ringer's lactate** อย่างรวดเร็วในรายช็อก แล้วต่อ ORS · ยาปฏิชีวนะช่วยลดปริมาณอุจจาระและระยะแพร่เชื้อ: **doxycycline 300 mg ครั้งเดียว** หรือ **azithromycin 1 g ครั้งเดียว** · ยืนยันด้วยเพาะเชื้อบน **TCBS agar** (โคโลนีสีเหลือง)

**ทำไมข้ออื่นผิด**
- ***Campylobacter jejuni***: Gram-negative โค้งเหมือนกัน (รูป **ปีกนกนางนวล / S-shape**) แต่ให้ **ไข้ ปวดท้อง ถ่ายเป็นมูกเลือด** และสัมพันธ์กับ Guillain–Barré
- ***Shigella***: Gram-negative **แท่งตรง** ทำลายเยื่อบุ → **dysentery** ไข้สูง ปวดเบ่ง
- **ETEC**: ถ่ายเป็นน้ำได้ (traveler's diarrhea) แต่เป็น **แท่งตรง** และมักไม่รุนแรงถึงช็อกในผู้ใหญ่
- ***C. difficile***: **Gram-positive** แท่งใหญ่มีสปอร์ สัมพันธ์กับยาปฏิชีวนะ/นอนโรงพยาบาล""",
 pearl="Rice-water stool + ไม่มีไข้ + ช็อกเร็ว + Gram-negative comma-shaped = Vibrio cholerae → fluid ก่อน แล้ว doxycycline/azithromycin ครั้งเดียว",
 ref=["MED35 FA SAQ ข้อ 4 – คนไข้ watery diarrhea ท้องเสีย 1 วัน ส่งตรวจพบดังรูป → อธิบายภาพ (gram negative comma shape bacilli) → บอกเชื้อที่เป็นไปได้ 2 ชื่อ เขียนตัวเต็ม (Vibrio cholerae, …)"],
 nl=["2.3.1","2.3.11"]),

# ───────────────────────────── AIR ─────────────────────────────
dict(
 id="PIC35-15", set="air", part="MCQ", lec="08",
 lecture="Allergy and clinical immunology",
 topic="Urticaria with hypotension after a meal – initial management",
 img=[dict(src="pic/med35-15.jpg", cap="ผื่นที่ต้นแขนของผู้ป่วย")],
 stem="A 27-year-old woman develops the rash shown 20 minutes after eating seafood at a dinner party, followed by wheezing and dizziness. BP 80/50 mmHg, PR 128/min, RR 28/min, SpO2 91% on room air, with diffuse expiratory wheeze. Which is the most appropriate initial management?",
 choices=["Adrenaline (1 mg/mL) 0.5 mg intramuscularly into the anterolateral thigh",
          "Chlorpheniramine 10 mg intravenously",
          "Famotidine 20 mg intravenously",
          "Hydrocortisone 200 mg intravenously",
          "Adrenaline (1 mg/mL) 1 mg as an intravenous push"],
 explain="""**ภาพ**: ผื่นนูนแดง **ขอบชัด รูปร่างไม่แน่นอน บวมน้ำ (wheals)** หลายวงรวมกัน = **urticaria**

ผื่นลมพิษ + **ระบบหายใจ (wheeze, SpO2 ต่ำ) + ความดันตก** หลังสัมผัสสารก่อภูมิแพ้ภายในนาที = **anaphylaxis** (distributive shock)

**ทำไม adrenaline IM**: ยาตัวเดียวที่แก้ทุกกลไก — α1 หดหลอดเลือดและลดบวมทางเดินหายใจ, β1 เพิ่มแรงบีบหัวใจ, β2 ขยายหลอดลมและ **ยับยั้งการหลั่ง mediator จาก mast cell** · ฉีดที่ **กล้ามเนื้อต้นขาด้านนอก** ดูดซึมเร็วที่สุด · ผู้ใหญ่ **0.01 mg/kg สูงสุด 0.5 mg** ซ้ำได้ทุก 5–15 นาที · ร่วมกับนอนราบยกขา, O2, **IV crystalloid 1–2 L เร็ว ๆ**

**ทำไมข้ออื่นผิด**
- **Antihistamine H1 / H2**: แก้แค่ผื่นคัน **ไม่แก้ความดันตกและทางเดินหายใจบวม** — การให้ยากลุ่มนี้แทน adrenaline เป็นสาเหตุการตายที่ป้องกันได้
- **Hydrocortisone**: ออกฤทธิ์ช้าหลายชั่วโมง ไม่ช่วยระยะเฉียบพลัน
- **Adrenaline 1 mg IV push**: ขนาดของ cardiac arrest — ในคนที่ยังมีชีพจรเสี่ยง VT/VF, MI, hypertensive crisis · ถ้า IM 2–3 ครั้งไม่ดีขึ้นจึงใช้ **IV infusion ขนาดต่ำ** ในที่ที่ monitor ได้""",
 pearl="Anaphylaxis = adrenaline 0.5 mg IM ที่ต้นขาทันที · antihistamine/steroid เป็นแค่ยาเสริม · สังเกตอาการ ≥4–6 ชม. (biphasic) และสั่ง adrenaline autoinjector ก่อนกลับ",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 28 – หญิงไปกิน dinner แล้วเกิดผื่นนี้ (ให้รูป urticaria) ใบ้ asthma attack BP 80/50 initial management (anti-H1 / H2 blocker / Adrenaline)"],
 nl=["B4.2.2(12)","2.2.7","B1.4.11(1)"]),

dict(
 id="PIC35-16", set="air", part="MCQ", lec="23",
 lecture="Approach to arthritis / crystal and infective arthropathy",
 topic="Synovial fluid microscopy – needle-shaped crystals",
 img=[dict(src="pic/med35-16.jpg", cap="กล้องจุลทรรศน์ของน้ำไขข้อ")],
 stem="A 48-year-old man who drinks beer daily and smokes presents with severe pain, swelling and redness of the right first metatarsophalangeal joint that began overnight. Synovial fluid aspirated from the joint is examined under the microscope, as shown. Which is the most likely diagnosis?",
 choices=["Acute gouty arthritis","Pseudogout (calcium pyrophosphate crystal arthritis)","Septic arthritis","Reactive arthritis","Acute flare of osteoarthritis"],
 explain="""**ภาพ**: ผลึก **รูปเข็มยาวปลายแหลม (needle-shaped)** จำนวนมาก บางอันอยู่ใกล้/ในเซลล์เม็ดเลือดขาว → **monosodium urate (MSU) crystal** = **gout**

ใต้ compensated polarized light ผลึก MSU เป็น **strongly negatively birefringent** — **สีเหลืองเมื่อวางขนานกับแกน** compensator (จำ: **"Yellow-Parallel = urate"**)

**กลไก**: uric acid สูงนาน → ผลึก MSU สะสมในข้อ เมื่อผลึกหลุดออกมา (ดื่มเหล้า/เบียร์ซึ่งมี purine และเพิ่ม lactate ที่แย่งขับ urate, อาหาร purine สูง, ขาดน้ำ, ยาขับปัสสาวะ) จะถูก neutrophil/macrophage กิน → กระตุ้น **NLRP3 inflammasome → IL-1β** → ข้ออักเสบเฉียบพลันรุนแรง มักเป็นที่ **MTP ที่ 1 (podagra)** ตอนกลางคืน

**ทำไมข้ออื่นผิด**
- **Pseudogout (CPPD)**: ผลึก **รูปสี่เหลี่ยมขนมเปียกปูน/แท่งสั้น (rhomboid)** **weakly positive** birefringent (สีฟ้าเมื่อขนาน) มักเป็นที่เข่า ข้อมือ ผู้สูงอายุ
- **Septic arthritis**: น้ำขุ่นมาก WBC >50,000 Gram stain/culture พบเชื้อ — **แต่ต้องจำว่าเจอผลึกไม่ได้ตัด septic arthritis** ควรส่ง Gram/culture เสมอ
- **Reactive arthritis**: oligoarthritis ข้อใหญ่ขา หลังติดเชื้อทางเดินอาหาร/ปัสสาวะ ไม่มีผลึก
- **OA**: น้ำไขข้อใส WBC <2,000 ไม่มีผลึก

**รักษาระยะเฉียบพลัน**: NSAID / colchicine (ภายใน 36 ชม.) / corticosteroid · **ไม่เริ่มหรือหยุด allopurinol ช่วงกำลังอักเสบ** (ถ้ากินอยู่แล้วให้กินต่อ)""",
 pearl="Needle + negative birefringence (เหลืองเมื่อขนาน) = gout · Rhomboid + positive (ฟ้าเมื่อขนาน) = CPPD · เจอผลึกแล้วก็ยังต้องส่ง Gram/culture",
 ref=["MED35 FA SAQ ข้อ 7 – ผู้ชาย ปวดข้อ ชอบดื่มเหล้า สูบบุหรี่ เจาะน้ำไขข้อพบดังรูป → อธิบายผล (needle shape crystal) → Diag (gouty arthritis)"],
 nl=["B5.2.5(1)","2.3.13(2)","B5.3(3)"]),

dict(
 id="PIC35-17", set="air", part="OSCE/SAQ", lec="23",
 lecture="Approach to arthritis / crystal and infective arthropathy",
 topic="SAQ – น้ำไขข้อขุ่น + Gram-negative bacilli: non-gonococcal septic arthritis",
 station="SAQ (เขียนตอบ) 5 นาที",
 img=[dict(src="pic/med35-17.jpg", cap="น้ำไขข้อที่เจาะได้จากเข่าขวา")],
 vignette="ผู้ป่วยชายไทยอายุ 62 ปี เป็นเบาหวาน มาด้วยปวด บวม แดง ร้อน ข้อเข่าขวา 2 วัน มีไข้\nV/S: BT 38.8 °C, PR 104/min, BP 128/78 mmHg\nเข่าขวาบวม แดง ร้อน กดเจ็บ ขยับแทบไม่ได้ ข้ออื่นปกติ\nเจาะข้อเข่าได้น้ำไขข้อลักษณะดังภาพ ย้อม Gram พบ **Gram-negative bacilli**",
 questions=[
  dict(q="1. จงแปลผลน้ำไขข้อนี้",
       a="- **สีเหลือง ขุ่น (turbid / opaque)** มองทะลุไม่เห็นตัวหนังสือ = **inflammatory ถึง septic fluid** (ปกติใส ไม่มีสี)\n- **Gram stain พบ Gram-negative bacilli** = มีเชื้อแบคทีเรียในข้อ\n- ผลที่คาดว่าจะพบเพิ่ม: WBC **>50,000/mm³** neutrophil **>90%**, glucose ในน้ำไขข้อต่ำ\n- ควรตรวจผลึกด้วยเสมอ (gout/CPPD เกิดร่วมกับ septic ได้)\n\n(เฉลยในโพย: Turbid with approximately 50 mL of fluid. Gram negative bacilli are found.)"),
  dict(q="2. จงให้การวินิจฉัย",
       a="**Acute non-gonococcal septic arthritis** ของข้อเข่าขวา (เชื้อ Gram-negative bacilli — ในผู้ป่วยเบาหวานของไทยต้องนึกถึง Enterobacterales, *Pseudomonas* และ ***Burkholderia pseudomallei* (melioidosis)** ด้วย)"),
  dict(q="3. (ฝึกเพิ่ม) การรักษาเบื้องต้น",
       a="- ส่ง **เพาะเชื้อน้ำไขข้อ + hemoculture 2 ขวด** ก่อนให้ยา\n- **ยาปฏิชีวนะทางหลอดเลือดดำทันที** ครอบคลุม Gram-negative: **ceftriaxone 2 g/day** หรือ **ceftazidime 2 g q8h** ถ้าเสี่ยง *Pseudomonas*/melioidosis (เบาหวาน ภาคอีสาน) แล้วปรับตามผลเพาะเชื้อ รวมประมาณ 4 สัปดาห์\n- **ระบายหนองออกจากข้อ** — เจาะดูดซ้ำทุกวัน หรือ arthroscopic/open drainage ถ้าไม่ดีขึ้น\n- ประเมินแหล่งติดเชื้อต้นทาง (ทางเดินปัสสาวะ ผิวหนัง ปอด)")],
 ref=["MED35 สอบลงกองครั้งที่ 1 OSCE/SAQ ข้อ 9 – ปวด บวม แดง ข้อเข่าขวา เจาะ synovial fluid (ให้รูป) G/S พบ Gram negative bacilli → 9.1 แปลผล (turbid, GNB) → 9.2 วินิจฉัย (non-GC septic arthritis)"],
 nl=["2.3.13-3(6)","B5.3(3)","3.1.7"]),

dict(
 id="PIC35-18", set="air", part="MCQ", lec="33",
 lecture="Connective tissue diseases and vasculitis",
 topic="Facial rash, proximal weakness and coarse speckled ANA",
 img=[dict(src="pic/med35-18.jpg", cap="ใบหน้าของผู้ป่วย")],
 stem="A 32-year-old woman has had progressive proximal muscle weakness for 2 months, with difficulty climbing stairs and combing her hair. Her fingers turn white then blue in the cold, and her hands look puffy. Her face is shown. CK 2,400 U/L. ANA is positive at 1:1280 with a coarse speckled pattern; anti-U1 RNP antibody is strongly positive, while anti-dsDNA, anti-Sm and anti-Jo-1 are negative. Which is the most likely diagnosis?",
 choices=["Mixed connective tissue disease","Dermatomyositis","Systemic lupus erythematosus","Overlap syndrome","Systemic sclerosis"],
 explain="""**ภาพ**: ผื่นแดงบริเวณแก้ม จมูก และรอบตา — ผื่นที่หน้าเพียงอย่างเดียว **แยก SLE, dermatomyositis และ MCTD ออกจากกันไม่ได้** ต้องใช้ข้อมูลอื่น

**กุญแจของข้อนี้คือ ANA pattern**: **coarse speckled = anti-U1 RNP** และ **anti-U1 RNP titer สูงเพียงตัวเดียว** ร่วมกับลักษณะของหลายโรคปนกัน — Raynaud's phenomenon (พบ >90%), **มือบวม (puffy hands)**, myositis, ข้ออักเสบ, ผื่นแบบ SLE → **Mixed connective tissue disease (MCTD)**

**ทำไมข้ออื่นผิด**
- **Dermatomyositis**: กล้ามเนื้ออ่อนแรงต้นแขนขาเหมือนกัน แต่ผื่นจำเพาะคือ **heliotrope rash (เปลือกตาม่วง) + Gottron papules** ที่ข้อนิ้ว · antibody คือ anti-Mi-2, anti-MDA5, anti-TIF1γ, anti-Jo-1 (antisynthetase) — ไม่ใช่ U1 RNP เดี่ยว ๆ · ถ้าโจทย์ไม่ให้ ANA pattern มา ข้อนี้คือคำตอบที่น่าเลือกที่สุด
- **SLE**: มี anti-U1 RNP ได้ แต่ควรมี **anti-dsDNA / anti-Sm** (จำเพาะ) ซึ่งเป็นลบ
- **Overlap syndrome**: ผู้ป่วยเข้าเกณฑ์ ≥2 โรคพร้อมกัน (เช่น scleroderma–polymyositis กับ anti-PM/Scl) — MCTD ถูกแยกเป็นกลุ่มเฉพาะที่นิยามด้วย anti-U1 RNP
- **Systemic sclerosis**: ผิวหนังหนาแข็ง, anti-Scl-70 หรือ anti-centromere

หมายเหตุ: โพย MED35 จดตัวเลือกไว้ 4 ข้อ (Dermatomyositis, Overlapping syndrome, SLE, MCTD) แต่ไม่ได้จดเฉลย — ข้อนี้เติมรายละเอียดให้คำตอบชัดตามเบาะแส "coarse speckle pattern" ที่จำมาได้""",
 pearl="ANA pattern → antibody: homogeneous = dsDNA/histone · coarse speckled = U1 RNP (MCTD) · fine speckled = Ro/La · centromere = limited SSc · nucleolar = diffuse SSc",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 1 – หญิง proximal muscle weakness 2 เดือน มี skin lesion (ให้รูปหน้า) ANA positive coarse speckle pattern → ตัวเลือก Dermatomyositis / Overlapping syndrome / SLE / Mixed connective tissue disease"],
 nl=["2.3.13-3(10)","2.3.13-3(15)","B5.2.2-3(2)"]),

# ───────────────────────────── ONCO ─────────────────────────────
dict(
 id="PIC35-19", set="onco", part="MCQ", lec="O02",
 lecture="General oncology (พญ.ปิยวรรณ)",
 topic="Spot diagnosis – digital clubbing in an older smoker",
 img=[dict(src="pic/med35-19.jpg", cap="มือทั้งสองข้างของผู้ป่วย")],
 stem="A 60-year-old man who has smoked 40 pack-years presents with chronic cough and 6 kg weight loss over 3 months. His hands are shown. Which underlying malignancy is most strongly associated with this physical finding?",
 choices=["Lung cancer","Basal cell carcinoma of the skin","Colorectal cancer","Male breast cancer","Prostate cancer"],
 explain="""**ภาพ**: ปลายนิ้วโป่งเป็นกระเปาะ เล็บโค้งนูน **มุมระหว่างโคนเล็บกับผิวหนังหายไป (Lovibond angle >180°)** ทุกนิ้ว = **digital clubbing** (ทดสอบเพิ่ม: Schamroth window sign หายไป)

**กลไก (สมมติฐานหลัก)**: megakaryocyte/platelet clump ที่ปกติถูกกรองในปอด หลุดผ่านเข้าระบบไหลเวียนส่วนปลาย (จาก shunt หรือเนื้องอก) ไปติดที่ปลายนิ้ว ปล่อย **PDGF และ VEGF** → เนื้อเยื่อเกี่ยวพันและหลอดเลือดปลายนิ้วเจริญมากขึ้น

**สาเหตุที่ต้องนึก** — ชายสูงอายุสูบบุหรี่หนัก ไอเรื้อรัง น้ำหนักลด + clubbing → **lung cancer (โดยเฉพาะ NSCLC/adenocarcinoma)** อาจร่วมกับ hypertrophic pulmonary osteoarthropathy · สาเหตุอื่น: bronchiectasis, lung abscess/empyema, interstitial lung disease, cyanotic congenital heart disease, infective endocarditis, IBD, cirrhosis

**จุดหลอกที่ออกบ่อย**: **COPD อย่างเดียวไม่ทำให้นิ้วปุ้ม** — ผู้ป่วย COPD ที่มี clubbing ต้องหามะเร็งปอดหรือโรคอื่นเสมอ

**ทำไมข้ออื่นผิด**: basal cell carcinoma, colorectal, male breast และ prostate cancer ไม่สัมพันธ์กับ clubbing (ตัวเลือกในข้อสอบจริงคือ basal cell / colon / male breast cancer / lung CA)""",
 pearl="Clubbing + สูบบุหรี่ + น้ำหนักลด = lung cancer จนกว่าจะพิสูจน์ได้ว่าไม่ใช่ · COPD ไม่ทำให้ clubbing",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 10 – รูปนิ้วมือ ชาย 60 ปี (ข้อนี้เลย) → Lung CA (ตัวเลือก Basal cell / Colon / Male breast cancer)"],
 nl=["B6.2.4-3(2)"]),

# ───────────────────────────── NEPHRO ─────────────────────────────
dict(
 id="PIC35-20", set="nephro", part="MCQ", lec="30",
 lecture="Urinary tract infection (อ.กรทิพย์)",
 topic="Nitrite-positive cystitis – reading the urine Gram stain",
 img=[dict(src="pic/med35-20.jpg", cap="Gram stain ของปัสสาวะ")],
 stem="A 28-year-old woman has had dysuria, frequency and suprapubic pain for 2 days, without fever or flank pain. Urine dipstick: leukocyte esterase 2+, nitrite positive. A Gram stain of the urine is shown. Which organism is most likely?",
 choices=["Escherichia coli","Staphylococcus saprophyticus","Enterococcus faecalis","Neisseria gonorrhoeae","Candida albicans"],
 explain="""**ภาพ**: แบคทีเรีย **ติดสีแดง/ชมพู (Gram-negative) รูปแท่ง (bacilli)** → กลุ่ม **Enterobacterales** ซึ่งพบมากที่สุดคือ ***E. coli*** (75–95% ของ uncomplicated cystitis) รองลงมา *Klebsiella*, *Proteus*

**ทำไม nitrite บวกช่วย**: Enterobacterales มีเอนไซม์ **เปลี่ยน nitrate ในปัสสาวะเป็น nitrite** (ต้องค้างในกระเพาะปัสสาวะ ≥4 ชม.) → nitrite บวก **จำเพาะสูง** ต่อเชื้อกลุ่มนี้ · Gram-positive cocci ส่วนใหญ่ทำไม่ได้

**ทำไมข้ออื่นผิด**
- ***S. saprophyticus***, ***Enterococcus***: **Gram-positive cocci** (สีม่วง) และ **nitrite มักลบ**
- ***N. gonorrhoeae***: **Gram-negative diplococci** อยู่ในเซลล์ neutrophil → urethritis/cervicitis มีหนองไหล
- ***Candida***: ยีสต์ติดสี Gram-positive มีหน่อ (budding) พบในผู้ป่วยใส่สายสวน/ได้ยาปฏิชีวนะนาน

**รักษา uncomplicated cystitis**: **nitrofurantoin 100 mg bid × 5 วัน** หรือ **fosfomycin 3 g ครั้งเดียว** · หลีกเลี่ยง fluoroquinolone เป็นยาแรก

หมายเหตุ: ภาพในโพย MED35 เป็นภาพ *K. pneumoniae* (เห็น capsule) — Gram stain แยก *E. coli* กับ *Klebsiella* ไม่ได้ สิ่งที่ข้อสอบต้องการคือ "Gram-negative bacilli ของกลุ่ม Enterobacterales" ซึ่งตัวที่พบบ่อยที่สุดคือ *E. coli*""",
 pearl="Nitrite บวก = Enterobacterales (E. coli มากสุด) · Gram-positive cocci (Enterococcus, S. saprophyticus) มัก nitrite ลบ",
 ref=["MED35 สอบลงกองครั้งที่ 1 MCQ ข้อ 52 – หญิงเป็น UTI เชื้อพบ nitrite+ ให้รูปเป็น gram neg (ภาพ K. pneumoniae)"],
 nl=["B9.2.2(1)","2.3.14(7)"]),

dict(
 id="PIC35-21", set="nephro", part="OSCE/SAQ", lec="28",
 lecture="Urine analysis / Common abdominal pain in nephro (อ.ธนิศร)",
 topic="SAQ – KUB: staghorn calculi และผลึกที่จำเพาะใน UA",
 station="SAQ (เขียนตอบ) 5 นาที",
 img=[dict(src="pic/med35-21.jpg", cap="Plain KUB ของผู้ป่วย")],
 vignette="ผู้ป่วยหญิงไทยอายุ 55 ปี เป็นกรวยไตอักเสบซ้ำ ๆ หลายครั้งในปีที่ผ่านมา ปวดหลังทั้งสองข้างตื้อ ๆ เรื้อรัง ครั้งนี้มาด้วยไข้ ปัสสาวะขุ่น มีกลิ่นแอมโมเนีย\nUA: pH 8.0, WBC numerous/HPF\nถ่ายภาพรังสี KUB ได้ดังภาพ",
 questions=[
  dict(q="1. จงแปลผล KUB นี้",
       a="- Plain KUB (supine) คุณภาพพอใช้\n- พบ **radiopaque calculi ขนาดใหญ่ รูปแตกกิ่งตามรูปร่างกรวยไตและ calyx (branching / staghorn calculus)** ที่ไตขวา และมี **นิ่วในกรวยไตซ้ายด้วย** → **bilateral renal calculi (staghorn)**\n- ไม่เห็นนิ่วชัดในแนวท่อไตหรือกระเพาะปัสสาวะ · ลมในลำไส้และกระดูกไม่มีความผิดปกติชัดเจน\n\n(เฉลยในโพย: KUB staghorn — kidney stone at both renal pelvis)"),
  dict(q="2. ถ้าตรวจ UA จะพบผลึกอะไรที่จำเพาะที่สุด",
       a="**Triple phosphate (struvite = magnesium ammonium phosphate) crystal** — รูป **\"coffin-lid\"** (ฝาโลงศพ) ในปัสสาวะที่ **pH เป็นด่าง (>7)**"),
  dict(q="3. (ฝึกเพิ่ม) เชื้อที่เกี่ยวข้องและกลไก",
       a="เชื้อที่สร้าง **urease** โดยเฉพาะ ***Proteus mirabilis*** (รวมถึง *Klebsiella*, *Pseudomonas*, *Providencia*)\n\nurease ย่อย urea → **NH₃ + CO₂** → ปัสสาวะเป็นด่างและมี ammonium สูง → magnesium ammonium phosphate ตกตะกอนรอบเชื้อ → นิ่วโตเร็วเต็มกรวยไต และเชื้ออยู่ในเนื้อนิ่ว ยาปฏิชีวนะเข้าไม่ถึง"),
  dict(q="4. (ฝึกเพิ่ม) หลักการรักษา",
       a="- รักษาการติดเชื้อตามผลเพาะเชื้อ\n- **เอานิ่วออกให้หมด** — staghorn ใช้ **percutaneous nephrolithotomy (PCNL)** เป็นหลัก เพราะเศษนิ่วที่เหลือเป็นแหล่งเชื้อและโตใหม่\n- ติดตาม UA/เพาะเชื้อ ป้องกันการติดเชื้อซ้ำ (acetohydroxamic acid ใช้น้อย)")],
 ref=["MED35 สอบลงกองครั้งที่ 1 OSCE/SAQ – KUB staghorn (kidney stone at both renal pelvis) ให้รูป → interpret KUB → UA จะเจออะไรที่ specific (triple phosphate crystal)"],
 nl=["B9.2.3-3(1)","2.3.14-3(15)"]),

# ───────────────────────────── CHEST ─────────────────────────────
dict(
 id="PIC35-22", set="chest", part="MCQ", lec="03",
 lecture="Pulmonary tuberculosis / ABG (อ.ศิวพร)",
 topic="Upper-lobe opacity with haemoptysis – first investigation",
 img=[dict(src="pic/med35-22.jpg", cap="Chest radiograph (PA upright)")],
 stem="A 45-year-old construction worker has had low-grade fever and dry cough for 3 weeks, and since yesterday has coughed up blood-streaked sputum. He bought antibiotics from a pharmacy, which helped only briefly. He has smoked 20 cigarettes a day for 20 years. Fine crepitations and decreased breath sounds are heard over the right upper chest. His chest radiograph is shown. Which is the most appropriate next investigation?",
 choices=["Sputum AFB smear and Xpert MTB/RIF, with mycobacterial culture",
          "CT-guided transthoracic needle biopsy of the lesion",
          "Tuberculin skin test",
          "Serum galactomannan",
          "Empirical levofloxacin for 2 weeks, then repeat the chest radiograph"],
 explain="""**ภาพ**: ฟิล์ม PA upright หลอดลมอยู่กลาง มี **ทึบแบบ patchy/consolidation ปน reticulonodular ที่ปอดขวาส่วนบน (right upper zone)** ปอดซ้ายค่อนข้างใส — ตำแหน่ง **upper lobe (apical/posterior segment)** เป็นตำแหน่งคลาสสิกของ **post-primary (reactivation) TB** เพราะ O₂ สูงและ lymphatic drainage น้อย

ไอเรื้อรัง >2 สัปดาห์ + ไข้ต่ำ + **ไอเป็นเลือด** + ฝ้าปอดกลีบบน → **ต้องพิสูจน์ TB ก่อน** ด้วย **เสมหะ AFB smear 2–3 ครั้ง + molecular test (Xpert MTB/RIF ซึ่งบอก rifampicin resistance ด้วย) + เพาะเชื้อ** (เฉลยโพย: AFB stain / PCR for TB / culture for TB)

**ทำไมข้ออื่นผิด**
- **CT-guided biopsy**: สูบบุหรี่ 20 pack-years ต้องนึกถึงมะเร็งปอดด้วยก็จริง แต่ **ขั้นแรกต้องตรวจเสมหะก่อน** เพราะ TB พบบ่อยกว่า ตรวจง่ายกว่า และผู้ป่วยแพร่เชื้อได้ — ถ้าเสมหะลบและไม่ดีขึ้นจึงพิจารณา CT/bronchoscopy
- **Tuberculin skin test / IGRA**: ใช้วินิจฉัย **latent TB** — บวกได้ในคนไทยส่วนใหญ่ แยก active จาก latent ไม่ได้
- **Galactomannan**: สำหรับ invasive aspergillosis ในผู้ป่วยภูมิคุ้มกันต่ำมาก
- **Levofloxacin ลองรักษา**: fluoroquinolone **ฆ่า TB บางส่วน → อาการดีขึ้นชั่วคราว ทำให้วินิจฉัยช้าและเสี่ยงดื้อยา** (ห้ามใช้ FQ ลองรักษาเมื่อสงสัย TB)

**ต่อ (MEQ ปีนี้)**: ระหว่างรอผลแยกห้อง airborne · ยืนยันแล้วให้ **2HRZE/4HR** · ให้ความรู้การแพร่เชื้อทาง **airborne** และคัดกรองผู้สัมผัส""",
 pearl="ไอ ≥2 สัปดาห์ + ฝ้ากลีบบน = ตรวจเสมหะ AFB + Xpert + culture ก่อนทุกอย่าง · อย่าลอง fluoroquinolone ในผู้ที่อาจเป็น TB",
 ref=["MED35 สอบลงกองครั้งที่ 1 Summative MEQ ข้อ 1 – ชาย 45 ปี ก่อสร้าง ไข้ต่ำ ไอแห้ง ซื้อยาฆ่าเชื้อกิน แล้วไอเสมหะเป็นเลือด สูบบุหรี่ 20 มวน 20 ปี → อ่าน CXR (ให้รูป: PA upright, trachea midline, reticulonodular opacity) → ส่งแลป 3 อย่าง (AFB stain, PCR for TB, culture) → 2IRZE/4IR → airborne"],
 nl=["B6.2.2(8)","2.3.4(20)","3.1.7"]),

dict(
 id="PIC35-23", set="chest", part="OSCE/SAQ", lec="37",
 lecture="Pneumonia / Asthma / COPD (Basic) (AL) (อ.เกรียงศักดิ์)",
 topic="SAQ – อ่าน CXR: community-acquired pneumonia กับ parapneumonic effusion",
 station="SAQ (เขียนตอบ) 5 นาที · ต่อจาก OSCE ซักประวัติ",
 img=[dict(src="pic/med35-23.jpg", cap="Chest radiograph (AP erect, mobile)")],
 vignette="(ต่อจาก OSCE ซักประวัติ) ผู้ป่วยหญิงไทยอายุ 54 ปี มาด้วยไข้ ไอมีเสมหะสีเขียว เหนื่อย 3 วันก่อนมาโรงพยาบาล\nV/S: BT 38.6 °C, PR 108/min, RR 26/min, BP 118/70 mmHg, SpO2 93% room air\nPE: decreased breath sounds และ dullness on percussion ที่ปอดขวาส่วนล่าง ได้ยิน crepitation ที่ปอดขวาส่วนกลาง\nCXR ดังภาพ",
 questions=[
  dict(q="1. จงอ่าน CXR นี้ตามลำดับ (ABCDE)",
       a="- **ชนิดฟิล์ม**: AP erect (mobile) — ขนาดหัวใจประเมินไม่แม่น · หายใจเข้าและ exposure พอใช้\n- **A (airway)**: trachea อยู่แนวกลาง\n- **B (breathing)**: **ทึบแบบ alveolar/air-space opacity ที่ปอดขวาส่วนกลางถึงล่าง** และ **ทึบเนื้อเดียวกันที่ฐานปอดขวา ขอบบนโค้งเว้าขึ้นไปทางผนังทรวงอก (meniscus sign)** · ปอดซ้ายค่อนข้างใส\n- **C (circulation/cardiac)**: เงาหัวใจด้านขวาและ mediastinum ไม่ชัดบางส่วน\n- **D (diaphragm)**: **มองไม่เห็น dome ของ diaphragm ขวาและ costophrenic angle ขวาทื่อ** · ด้านซ้าย dome และ CP angle คม\n- **E (everything else)**: กระดูกและ soft tissue ปกติ มีสาย ECG electrode\n\n**สรุป**: right lower/middle zone consolidation ร่วมกับ **right pleural effusion**"),
  dict(q="2. จงให้การวินิจฉัย",
       a="**Community-acquired pneumonia (ปอดขวาส่วนล่าง) with right parapneumonic effusion**"),
  dict(q="3. (ฝึกเพิ่ม) ส่งตรวจอะไรต่อสำหรับน้ำในช่องเยื่อหุ้มปอด และเกณฑ์ที่ต้องใส่สายระบาย",
       a="- **Diagnostic thoracentesis (ใช้ ultrasound นำ)** ส่ง pH, glucose, LDH, protein (คู่กับ serum ตาม Light's criteria), cell count, Gram stain, culture ± AFB\n- **Complicated parapneumonic effusion / empyema → ใส่ chest drain** เมื่อ: **หนอง**, **Gram stain/culture บวก**, **pH <7.20**, **glucose <60 mg/dL**, (LDH >1,000 U/L) หรือ loculated\n- ร่วมกับ sputum Gram stain/culture, hemoculture 2 ขวด และให้ยาปฏิชีวนะ CAP เช่น **ceftriaxone + azithromycin**")],
 ref=["MED35 สอบลงกองครั้งที่ 1 OSCE-1 – ซักประวัติหญิง ไข้ ไอ เหนื่อย 3 วัน และส่ง investigation (sputum Gram, CXR)",
      "MED35 สอบลงกองครั้งที่ 1 SAQ-P1 – Given CXR (ให้รูป) → interpret ABCDE → Community acquired pneumonia with parapneumonic effusion"],
 nl=["2.3.10(5)","2.3.10(7)","B6.2.2(10)"]),

# ───────────────────────────── HEME ─────────────────────────────
dict(
 id="PIC35-24", set="heme", part="OSCE/SAQ", lec="H01",
 lecture="โลหิตวิทยา: โลหิตจางและธาลัสซีเมีย (ยังไม่ระบุคาบ)",
 topic="SAQ – PBS ของหญิงประจำเดือนมามาก: iron deficiency anemia",
 station="SAQ (เขียนตอบ) 5 นาที · ต่อจาก OSCE ซักประวัติ",
 img=[dict(src="pic/med35-24.jpg", cap="Peripheral blood smear ของผู้ป่วย")],
 vignette="(ต่อจาก OSCE ซักประวัติ) ผู้ป่วยหญิงไทยอายุ 30 ปี อ่อนเพลีย มีคนทักว่าซีดมา 1 สัปดาห์ ประจำเดือนมามากขึ้นมา 6 เดือน ช่วงมีประจำเดือนต้องเปลี่ยนผ้าอนามัยวันละ 6–8 แผ่นและชุ่มทุกแผ่น มีหน้ามืดเวลาลุกยืน\nPE: pale conjunctivae, ไม่มีตัวเหลือง ตับม้ามไม่โต\nPBS ดังภาพ",
 questions=[
  dict(q="1. จงอธิบาย PBS ให้ครบทั้ง 3 series",
       a="- **RBC**: **hypochromic microcytic** (เม็ดเล็กกว่านิวเคลียสของ small lymphocyte, ตรงกลางซีดกว้าง >1/3 ของเซลล์) · **anisopoikilocytosis** มี **pencil cell (elongated cell)** · ไม่พบ spherocyte, schistocyte หรือ nucleated RBC\n- **WBC**: พบ small lymphocyte ลักษณะปกติ ไม่มี blast\n- **Platelet**: จำนวนพอเพียง (อาจสูงเล็กน้อยจาก reactive thrombocytosis ในภาวะขาดเหล็ก)"),
  dict(q="2. Definitive diagnosis และการตรวจยืนยัน",
       a="**Iron deficiency anemia จาก chronic blood loss (menorrhagia)**\n\nยืนยัน: **serum ferritin ต่ำ (<30 ng/mL)** — ตัวที่จำเพาะที่สุด · serum iron ต่ำ · **TIBC สูง** · transferrin saturation <16–20% · RDW สูง (แยกจาก thalassemia trait ที่ RDW มักปกติ, Mentzer index MCV/RBC >13 เข้าได้กับขาดเหล็ก)"),
  dict(q="3. (ฝึกเพิ่ม) คำแนะนำและการรักษา",
       a="- อธิบายเป็นภาษาไทยว่า **ซีดจากการขาดธาตุเหล็ก เพราะเสียเลือดทางประจำเดือนมาก**\n- **ferrous sulfate (เหล็ก elemental ~65 mg) วันละ 1 ครั้งหรือวันเว้นวัน** ตอนท้องว่าง กินกับ **วิตามินซี/น้ำส้ม** ช่วยดูดซึม · **ห้ามกินพร้อมนม ชา กาแฟ ยาลดกรด** · อุจจาระอาจดำ ท้องผูกได้\n- กินต่อ **อีก 3 เดือนหลัง Hb ปกติ** เพื่อเติมเหล็กสะสม · คาดว่า reticulocyte ขึ้นใน 5–10 วัน Hb ขึ้น 1–2 g/dL ใน 2–4 สัปดาห์\n- อาหารเหล็กสูง (เนื้อแดง ตับ เลือด ผักใบเขียว) · **ส่งตรวจหาสาเหตุของประจำเดือนมามาก** (เช่น myoma) — แก้ที่ต้นเหตุ")],
 ref=["MED35 สอบลงกองครั้งที่ 1 OSCE-3 – ซักประวัติหญิง 30 ปี อ่อนเพลีย ซีด 1 สัปดาห์ (ประจำเดือนมามาก) → วินิจฉัย IDA และให้คำแนะนำ",
      "MED35 สอบลงกองครั้งที่ 1 SAQ-P3 – Given PBS (ให้รูป) → อธิบาย PBS ของ iron deficiency anemia → definitive diagnosis"],
 nl=["2.3.3"]),
]
