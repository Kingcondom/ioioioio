# -*- coding: utf-8 -*-
# หัวข้อ 6–8: Child-Pugh + พยากรณ์ · portal hypertension · hepatic encephalopathy  (สไลด์หน้า 17–28)

sec("gi-cir-06", "Child-Pugh และพยากรณ์โรค",
    "5 ตัวแปร ABCDE · A 5–6 · B 7–9 · C 10–15 · รอด 1 ปี A 100% B 80% C 45% · MELD ≥ 15 ส่งพิจารณาเปลี่ยนตับ",
    8, r"""
### Child-Turcotte-Pugh (สไลด์)
| ตัวแปร | 1 คะแนน | 2 คะแนน | 3 คะแนน |
|---|---|---|---|
| **Ascites** | ไม่มี | เล็กน้อย | ปานกลาง (ขึ้นไป) |
| **Bilirubin** | **< 2** mg/dL | **2–3** | **> 3** |
| **Albumin** | **> 3.5** g/dL | **2.8–3.5** | **< 2.8** |
| **PT** (วินาทีเกิน control) | < 4 | 4–6 | > 6 |
| หรือ **INR** | **< 1.7** | **1.7–2.3** | **> 2.3** |
| **Encephalopathy** | ไม่มี | grade 1–2 | grade 3–4 |

| Class | คะแนน |
|---|---|
| **A** | **5–6** |
| **B** | **7–9** |
| **C** | **10–15** |

### พยากรณ์ (สไลด์ — 2 ตารางจากต่างแหล่ง)
| Class | รอด 1 ปี | รอด 2 ปี |
|---|---|---|
| **A** | 100% | 85% |
| **B** | 80% | 60% |
| **C** | **45%** | **35%** |

| Class | รอด 1 ปี | 5 ปี | 10 ปี |
|---|---|---|---|
| A | 82% | 45% | 25% |
| B | 62% | 20% | 7% |
| C | 42% | 20% | 0% |

> ตัวเลขสองชุดไม่ตรงกันเพราะต่างประชากร — **จำทิศทาง**: class C รอด 1 ปีราว **ครึ่งเดียว**

### MELD (สไลด์หน้า 51 + เพิ่มเติม)
สไลด์ใช้ **MELD ≥ 15** เป็นเกณฑ์ส่งพิจารณา **ผ่าตัดเปลี่ยนตับ**
- MELD คำนวณจาก **bilirubin · INR · creatinine** (MELD-Na เพิ่ม **Na**) — **ไม่มีตัวแปรตามความเห็นแพทย์** (ascites, HE) จึงเป็นกลางกว่า Child-Pugh
- ใช้จัดลำดับผู้รอตับ และทำนายอัตราตายใน 3 เดือน (เพิ่มเติม — ไม่ได้มาจากสไลด์)
""",
    ["Child-Pugh = Albumin · Bilirubin · Coagulation (INR) · Distension (ascites) · Encephalopathy",
     "A 5–6 · B 7–9 · C 10–15",
     "Class C รอด 1 ปีราวครึ่งเดียว",
     "MELD = bilirubin · INR · Cr (+Na) · ≥ 15 → พิจารณาเปลี่ยนตับ"],
    [mcq("GI-CIR-MCQ-14",
         "A patient with cirrhosis has no ascites, no encephalopathy, bilirubin 2.4 mg/dL, albumin 3.0 g/dL and INR 1.5. What is the Child-Pugh class?",
         ["Class A (5 points)", "Class A (6 points)", "Class B (7 points)", "Class B (8 points)", "Class C (10 points)"],
         2,
         "คิดคะแนน: ascites ไม่มี **1** · HE ไม่มี **1** · bilirubin 2–3 = **2** · albumin 2.8–3.5 = **2** · INR < 1.7 = **1** → รวม **7 = Child B**\n\nA = 5–6 · B = 7–9 · C = 10–15",
         "1+1+2+2+1 = 7 → B", "Child-Pugh"),
     mcq("GI-CIR-MCQ-15",
         "Which variables make up the MELD score?",
         ["Bilirubin, albumin, INR, ascites and encephalopathy", "Bilirubin, INR and creatinine (with sodium in MELD-Na)",
          "AST, platelet count and age", "Albumin, creatinine and platelet count", "INR, lactate and pH"],
         1,
         "MELD ใช้ **bilirubin · INR · creatinine** และ **MELD-Na** เพิ่ม Na — เป็นค่าแล็บทั้งหมด\n\nข้อ A คือ **Child-Pugh** · ข้อ C คือส่วนประกอบของ **FIB-4/APRI** (ประเมินพังผืด) · สไลด์ใช้ **MELD ≥ 15** เป็นข้อบ่งชี้ส่งพิจารณาเปลี่ยนตับ",
         "MELD = bili · INR · Cr (+Na)", "Prognosis")],
    nl=["2.3.11(4)", "B8.2.5(4)", "B8.3(1)"],
    mnem=[{"name": "ABCDE", "what": "5 ตัวแปรของ Child-Pugh",
           "lines": [["A", "**Albumin** > 3.5 / 2.8–3.5 / < 2.8"], ["B", "**Bilirubin** < 2 / 2–3 / > 3"],
                     ["C", "**Coagulation** — INR < 1.7 / 1.7–2.3 / > 2.3"], ["D", "**Distension** — ascites ไม่มี / น้อย / ปานกลาง"],
                     ["E", "**Encephalopathy** ไม่มี / 1–2 / 3–4"]],
           "note": "รวม 5–6 = A · 7–9 = B · 10–15 = C (นึกถึง “5-7-10”)",
           "src": "หลักจำที่ใช้ทั่วไป · ค่าตัดจากสไลด์หน้า 17"}])


FIG_LAPLACE = {
 "title": "ทำไม varices ใหญ่จึงแตกง่าย — กฎของ Laplace",
 "cap": "สไลด์หน้า 31 · แรงตึงผนัง **T = tp × r / w** (tp = transmural pressure = portal pressure ที่ส่งถึง varix · r = รัศมี · w = ความหนาผนัง) · varix **ใหญ่ (r ↑)** ผนัง **บาง (w ↓ — red wale sign)** และ portal pressure **สูง** → T สูงเกินที่ผนังทนได้ → แตก · ยาลด portal pressure (NSBB) ลด tp · EVL กำจัด varix",
 "svg": """<svg viewBox="0 0 440 210" role="img" aria-label="กฎของ Laplace แรงตึงผนังเท่ากับความดันคูณรัศมีหารความหนาผนัง varix เล็กผนังหนาแรงตึงต่ำ varix ใหญ่ผนังบางแรงตึงสูงแตกง่าย" xmlns="http://www.w3.org/2000/svg">
<rect x="110" y="8" width="220" height="40" rx="10" class="ac"/><text x="220" y="34" class="lg b mid tac">T = tp × r / w</text>
<circle cx="110" cy="122" r="26" class="ok"/><circle cx="110" cy="122" r="16" class="paf"/><text x="110" y="126" class="xs mid">r เล็ก</text>
<text x="110" y="168" class="sm b mid tok">Small varix · ผนังหนา</text><text x="110" y="186" class="xs mid">เลือดออกใน 2 ปี ~7%</text>
<circle cx="330" cy="122" r="48" class="bad"/><circle cx="330" cy="122" r="44" class="paf"/><text x="330" y="118" class="xs mid">r ใหญ่</text><text x="330" y="132" class="xs mid tbad">ผนังบาง</text>
<text x="330" y="190" class="sm b mid tbad">Large varix · ~30% ใน 2 ปี</text>
<line x1="170" y1="122" x2="262" y2="122" class="lac w2" marker-end="url(#ah-ac)"/><text x="216" y="112" class="xs mid tac">portal pressure ↑</text><text x="216" y="140" class="xs mid tac">→ โตขึ้น 7–8%/ปี</text>
</svg>"""}

sec("gi-cir-07", "Portal hypertension — กลไก ทางลัด และภาวะแทรกซ้อนสองกลุ่ม",
    "ต้านการไหลในตับ + เลือดไหลเข้าเพิ่ม (splanchnic vasodilation) · collateral · varices โตขึ้น 7–8%/ปี · T = tp × r/w · HVPG",
    8, r"""
### กลไก (สไลด์หน้า 21, 31)
1. **ความดันในหลอดเลือดดำพอร์ทัลสูงขึ้น** จากการ **ต้านการไหลผ่านตับ** (resistance to portal flow) — พังผืดและ nodule กด sinusoid
2. เลือดหาทางอ้อม = **collateral circulation** → **หลอดเลือดดำโป่งทั่วทางเดินอาหาร**
3. **Portal blood inflow เพิ่ม** จาก **splanchnic arteriolar resistance ลดลง** (หลอดเลือดแดงในช่องท้องขยาย — NO) → ความดันพอร์ทัล **ยิ่งสูง**
4. ความดันสูงต่อเนื่อง → **varices โต (variceal growth)** → **แตก (variceal rupture)**

[[fig:cir_laplace]]

### ทางลัด portal–systemic ที่สำคัญ (เพิ่มเติม — ไม่ได้มาจากสไลด์)
| ตำแหน่ง | เชื่อมระหว่าง | ผล |
|---|---|---|
| **หลอดอาหารส่วนล่าง/กระเพาะ** | left gastric (coronary) vein ↔ azygos | **Esophageal/gastric varices** |
| **สะดือ** | paraumbilical vein ↔ epigastric vein | **Caput medusae** |
| **ทวารหนัก** | superior rectal ↔ middle/inferior rectal | Rectal varices (ไม่ใช่ริดสีดวงธรรมดา) |
| ช่องท้องด้านหลัง | splenorenal | spontaneous shunt → ส่งเสริม HE |

### HVPG — ตัววัด portal pressure (สไลด์ + เพิ่มเติม)
- HVPG = wedged − free hepatic venous pressure · ปกติ **1–5 mmHg**
- **≥ 10 mmHg = clinically significant portal hypertension** (เริ่มเกิด varices และ decompensation) · **≥ 12** varices แตกได้ (เพิ่มเติม)
- สไลด์: **HVPG > 20 mmHg ขณะเลือดออกเฉียบพลัน ทำนายผลแย่** และ **ผู้ที่ HVPG ลดลงด้วยยา (HVPG responder) รอดชีวิตดีกว่า**

### ภาวะแทรกซ้อนของตับแข็ง (สไลด์หน้า 22)
| จาก portal hypertension | จาก liver insufficiency |
|---|---|
| **Variceal hemorrhage** · **Ascites** · SBP · HRS | **Jaundice** · **Encephalopathy** · coagulopathy |

ตารางสรุปท้ายสไลด์เพิ่ม: **hepatopulmonary syndrome** · **HCC** · ติดเชื้อแทรกซ้อนในโรงพยาบาล (หัวข้อสุดท้าย)
""",
    ["Portal HT = resistance ↑ (ในตับ) + inflow ↑ (splanchnic vasodilation)",
     "Varices โตขึ้น 7–8%/ปี",
     "T = tp × r / w — ใหญ่ + ผนังบาง + ความดันสูง = แตก",
     "HVPG ≥ 10 = CSPH · > 20 ขณะเลือดออก = ผลแย่"],
    [mcq("GI-CIR-MCQ-16",
         "According to Laplace's law as applied to oesophageal varices (T = tp × r / w), which combination carries the highest risk of rupture?",
         ["Small varix, thick wall, low portal pressure", "Large varix, thin wall, high portal pressure",
          "Small varix, thin wall, low portal pressure", "Large varix, thick wall, low portal pressure",
          "Any varix once portal pressure falls below 12 mmHg"],
         1,
         "สไลด์: **variceal wall tension** เป็นตัวกำหนดหลักว่า varix จะแตกหรือไม่ · **T = transmural pressure × radius / wall thickness**\n\nvarix **ใหญ่ (r ↑) · ผนังบาง (w ↓)** · **ความดันสูง (tp ↑)** → T สูงสุด · ใน endoscopy ผนังบางเห็นเป็น **red wale sign** · เพิ่มเติม: HVPG < 12 mmHg varices แทบไม่แตก",
         "ใหญ่ · บาง · ความดันสูง = แตก", "Portal hypertension"),
     mcq("GI-CIR-MCQ-17",
         "Which haemodynamic change increases portal venous inflow and sustains portal hypertension in cirrhosis?",
         ["Splanchnic arteriolar vasoconstriction", "Splanchnic arteriolar vasodilation",
          "Reduced cardiac output", "Increased hepatic arterial resistance", "Portal vein thrombosis in all patients"],
         1,
         "สไลด์หน้า 31: portal pressure ขึ้นกับ **resistance to portal flow** และ **portal blood inflow** ซึ่งเพิ่มเมื่อ **splanchnic arteriolar resistance ลดลง** (หลอดเลือดขยายจาก NO)\n\nนี่เป็นเหตุผลที่ยา **ทำให้หลอดเลือดช่องท้องหดตัว** ได้ผล — **NSBB** (β2 block ทำให้ splanchnic vasoconstriction + β1 ลด CO) · **terlipressin/octreotide** ในเลือดออกเฉียบพลัน",
         "Inflow ↑ จาก splanchnic vasodilation", "Portal hypertension")],
    nl=["2.3.11(4)", "B8.2.5(4)", "B8.2.2-3(7)"],
    figs={"cir_laplace": FIG_LAPLACE})


ANIM_HE = {
 "title": "Hepatic encephalopathy — แอมโมเนียจากลำไส้หลุดถึงสมอง",
 "svg": """<svg viewBox="0 0 440 300" role="img" aria-label="ภาพเคลื่อนไหว แอมโมเนียจากลำไส้ผ่าน portal vein เข้าตับเปลี่ยนเป็นยูเรีย ในตับแข็งตับเปลี่ยนไม่ได้และมี shunt แอมโมเนียถึงสมอง astrocyte สร้าง glutamine บวม ตัวกระตุ้นเพิ่มแอมโมเนีย lactulose ทำให้ลำไส้เป็นกรดเปลี่ยนเป็น ammonium" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="200" width="150" height="80" rx="20" class="sk"/><text x="85" y="222" class="sm b mid">ลำไส้ใหญ่</text><text x="85" y="242" class="xs mid">แบคทีเรีย + โปรตีน</text><text x="85" y="260" class="xs b mid">→ NH₃</text>
<rect x="250" y="190" width="170" height="90" rx="30" class="ac"/><text x="335" y="214" class="sm b mid tac">ตับ</text>
<text x="335" y="238" class="xs mid" data-x="2">urea cycle: NH₃ → urea</text>
<g data-s="2"><text x="335" y="238" class="xs b mid tbad">เซลล์ตับเหลือน้อย</text><text x="335" y="256" class="xs mid tbad">กำจัด NH₃ ไม่ได้</text></g>
<path d="M160,240 L248,240" class="ln w2 fl" marker-end="url(#ah)"/><text x="204" y="232" class="xs mid mu">portal vein</text>
<rect x="250" y="20" width="170" height="80" rx="30" class="wa"/><text x="335" y="44" class="sm b mid twa">สมอง</text>
<text x="335" y="66" class="xs mid" data-x="2">ปกติ NH₃ ต่ำ</text>
<g data-s="2"><path d="M160,214 C170,120 210,70 248,60" class="lbad w2 fl" marker-end="url(#ah-bad)"/><text x="150" y="120" class="xs b tbad">shunt อ้อมตับ</text></g>
<g data-s="3"><text x="335" y="66" class="xs b mid">astrocyte: NH₃ + glutamate</text><text x="335" y="82" class="xs b mid tbad">→ glutamine → บวม</text>
<text x="335" y="128" class="xs mid">+ GABA ↑ · false neurotransmitter</text><text x="335" y="144" class="xs mid">(octopamine) · mercaptan · SCFA</text></g>
<g data-s="4"><rect x="10" y="20" width="200" height="74" rx="10" class="ms"/><text x="22" y="40" class="xs b tms">ตัวเร่ง</text><text x="22" y="58" class="xs">GI bleed · ท้องผูก · โปรตีนมาก · ติดเชื้อ</text><text x="22" y="76" class="xs">K ต่ำ/alkalosis · ยานอนหลับ · ขาดน้ำ</text></g>
<g data-s="5"><rect x="10" y="150" width="150" height="40" rx="8" class="ok"/><text x="85" y="166" class="xs b mid tok">Lactulose: ลำไส้เป็นกรด</text><text x="85" y="182" class="xs mid">NH₃ → NH₄⁺ ดูดซึมไม่ได้</text></g>
</svg>""",
 "steps": [
  {"t": "ปกติ", "cap": "แบคทีเรียในลำไส้ย่อยโปรตีนได้ **แอมโมเนีย (NH₃)** ซึ่งไปกับเลือด **portal vein** เข้าตับ · ตับเปลี่ยนเป็น **urea** ผ่าน urea cycle → สมองแทบไม่เจอ NH₃"},
  {"t": "ตับแข็ง — สองรากพร้อมกัน", "cap": "สไลด์: HE เกิดใน **severe hepatocellular dysfunction** (โรงงานพัง) ร่วมกับ **intrahepatic และ extrahepatic shunting** (ถนนตันจนเลือดอ้อมตับ) → สารพิษที่ดูดซึมจากลำไส้ **ไม่ถูกกำจัด** ถึงสมองโดยตรง"},
  {"t": "ในสมอง", "cap": "**Ammonia** เป็นสารที่ถูกกล่าวหามากที่สุด · astrocyte กำจัด NH₃ โดยรวมกับ glutamate เป็น **glutamine** ซึ่งดึงน้ำเข้าเซลล์ → **astrocyte บวม** (stage IV = cerebral edema) · สไลด์เพิ่ม **mercaptan** (จาก methionine) **short-chain fatty acid · phenol · false neurotransmitter (octopamine)** · aromatic/branched-chain amino acid เสียสมดุล · **GABA** ซึ่งเป็น inhibitory neurotransmitter"},
  {"t": "ตัวเร่ง", "cap": "สไลด์: **nitrogen load เพิ่ม** (GI bleeding · โปรตีนมาก · azotemia · **ท้องผูก**) · **electrolyte** (**K ต่ำ · alkalosis** — ไตสร้าง NH₃ มากขึ้นและ NH₃ ผ่านเข้าสมองง่ายขึ้น · hypoxia · Na ต่ำ · ขาดน้ำ) · **ยา** (narcotic · sedative · **diuretic**) · **ติดเชื้อ** · ผ่าตัด · ตับอักเสบซ้อน · shunt"},
  {"t": "รักษา", "cap": "สไลด์: **กำจัดตัวเร่ง + ลด NH₃** · **Lactulose** เป็น nonabsorbable disaccharide → แบคทีเรียหมักเป็นกรด **pH ในลำไส้ต่ำ เปลี่ยน NH₃ เป็น NH₄⁺** ซึ่งดูดซึมไม่ได้ + เป็นยาระบาย · ยาปฏิชีวนะที่ไม่ดูดซึม (**neomycin · metronidazole** ในสไลด์ — ปัจจุบันใช้ **rifaximin**) ลดแบคทีเรียที่สร้าง NH₃"}
 ]}

sec("gi-cir-08", "Hepatic encephalopathy — กลไก ตัวเร่ง วินิจฉัย และรักษา",
    "NH₃ + shunt · ตัวเร่ง เลือด ผูก ติดเชื้อ K ต่ำ ยา · วินิจฉัยโดยตัดโรคอื่น ammonia ไม่จำเพาะ · lactulose 30–60 mL ทุกชั่วโมงจนถ่าย แล้วปรับให้ถ่ายนิ่ม 2–4 ครั้ง",
    12, r"""
### นิยาม (สไลด์)
กลุ่มอาการทาง **ประสาทจิตเวชที่ซับซ้อน** — ระดับความรู้สึกตัวและพฤติกรรมผิดปกติ **บุคลิกเปลี่ยน** · อาการทางประสาท **ขึ้นลง (fluctuating)** · **asterixis (flapping tremor)** · **EEG เปลี่ยนแบบเฉพาะ** · เป็นได้ทั้ง **เฉียบพลันกลับคืนได้** หรือ **เรื้อรังลุกลาม**

[[anim:cir-he]]

### ตัวเร่งที่พบบ่อย (สไลด์)
| กลุ่ม | ตัวอย่าง |
|---|---|
| **Nitrogen load ↑** | **GI bleeding** · กินโปรตีนมาก · azotemia · **ท้องผูก** |
| **Electrolyte/metabolic** | **Hypokalemia · alkalosis** · hypoxia · hyponatremia · **hypovolemia** |
| **ยา** | **narcotic · tranquilizer · sedative** · **diuretic** |
| **อื่น ๆ** | **ติดเชื้อ** · ผ่าตัด · ตับอักเสบเฉียบพลันซ้อน · โรคตับลุกลาม · portal-systemic shunt (รวม TIPS) |

### วินิจฉัย (สไลด์)
- **วินิจฉัยโดยตัดโรคอื่นออก (exclusion)** + LFT ผิดปกติ
- **Ammonia ในเลือดสูง แต่ไม่จำเพาะ** (ค่าปกติก็ไม่ตัด HE · ค่าสูงก็ไม่ยืนยัน)
- **น้ำไขสันหลังปกติ** · **CT สมองไม่มีลักษณะเฉพาะ** ยกเว้น **stage IV มี cerebral edema**

**ระดับความรุนแรง — West Haven (เพิ่มเติม · สไลด์มีเป็นภาพ)**
| Grade | อาการ |
|---|---|
| **1** | สมาธิสั้น นอนกลางวันตื่นกลางคืน อารมณ์เปลี่ยน |
| **2** | ซึม **สับสนเวลา** พฤติกรรมไม่เหมาะสม · **asterixis ชัด** |
| **3** | ง่วงมากแต่ปลุกตื่น **สับสนสถานที่** |
| **4** | **โคม่า** |

### วินิจฉัยแยกโรค (สไลด์)
**เมาสุรา · ยานอนหลับเกินขนาด · delirium tremens · Wernicke · Korsakoff · subdural hematoma** (ล้มบ่อย เลือดออกง่าย) · **meningitis** · **น้ำตาลต่ำ** หรือ metabolic encephalopathy อื่น

> ผู้ป่วยตับแข็งซึมทุกราย → **เจาะน้ำตาลปลายนิ้วก่อน** · ล้ม/อาการไม่สมมาตร → CT สมอง · ไข้ → หาการติดเชื้อรวมถึง **เจาะน้ำในช่องท้องหา SBP**

### รักษา (สไลด์)
1. **รู้เร็ว รักษาเร็ว**
2. **กำจัดตัวเร่ง** — สำคัญที่สุด
3. **ลด ammonia** — ลดการดูดซึมโปรตีนและสาร nitrogen จากลำไส้

| ยา | ขนาด/หลัก (สไลด์) |
|---|---|
| **Lactulose** | nonabsorbable disaccharide · osmotic laxative · **ลำไส้เป็นกรด NH₃ → NH₄⁺** · มีผลต่อเมแทบอลิซึมของแบคทีเรีย · **30–60 mL ทุก 1 ชม. จนถ่าย** แล้วปรับ (มัก **15–30 mL วันละ 3 ครั้ง**) ให้ **ถ่ายนิ่ม 2–4 ครั้ง/วัน** |
| **Neomycin** | 0.5–1.0 g ทุก 6 ชม. (nonabsorbable antibiotic · ระวังพิษต่อไตและหู) |
| **Metronidazole** | ทางเลือก (ระวัง neuropathy เมื่อใช้นาน) |
| **Flumazenil** | เฉพาะ HE ที่ **เร่งโดย benzodiazepine** |
| Extracorporeal liver assist | **ยังไม่พิสูจน์ประโยชน์** |

**อัปเดตจาก guideline (ไม่ได้มาจากสไลด์ — AASLD/EASL 2014 · EASL 2022)**
- **Rifaximin 550 mg วันละ 2 ครั้ง** ร่วมกับ lactulose — **ป้องกัน HE ซ้ำ** หลังเป็นครั้งที่สอง · แทน neomycin/metronidazole
- **ไม่จำกัดโปรตีนแล้ว** — แนะนำ **โปรตีน 1.2–1.5 g/kg/วัน** + มื้อว่างก่อนนอน (การจำกัดโปรตีนทำให้ sarcopenia และแย่ลง) · ต่างจากสไลด์ที่ยังเขียน protein restriction
""",
    ["HE = เซลล์ตับเหลือน้อย + shunt → NH₃ ถึงสมอง",
     "ตัวเร่ง: เลือด · ผูก · ติดเชื้อ · K ต่ำ/alkalosis · ยานอนหลับ · diuretic",
     "Ammonia ไม่จำเพาะ — วินิจฉัยโดยตัดโรคอื่น · เจาะน้ำตาลก่อน",
     "Lactulose 30–60 mL q1h จนถ่าย → ถ่ายนิ่ม 2–4 ครั้ง/วัน",
     "ปัจจุบัน: + rifaximin ป้องกันซ้ำ · ไม่จำกัดโปรตีน"],
    [mcq("GI-CIR-MCQ-18",
         "A cirrhotic man becomes confused 2 days after starting furosemide 80 mg and spironolactone 200 mg daily. Serum K 2.9 mmol/L, HCO3 32 mmol/L. How do these abnormalities precipitate hepatic encephalopathy?",
         ["They directly damage hepatocytes", "Hypokalaemia increases renal ammonia production and alkalosis favours NH3 entry into the brain",
          "They cause cerebral vasoconstriction", "They raise GABA synthesis in the liver", "They increase intestinal protein absorption"],
         1,
         "สไลด์จัด **hypokalemia · alkalosis** (และ diuretic) เป็นตัวเร่ง HE\n\nกลไก: **K ต่ำ** → H⁺ เข้าเซลล์ท่อไต → **ไตสร้าง NH₃ มากขึ้น** · **alkalosis** → NH₄⁺ เปลี่ยนเป็น **NH₃** ซึ่งไม่มีประจุ **ผ่าน blood–brain barrier ได้ง่าย** · รักษา: หยุด diuretic แก้ K และน้ำ + lactulose",
         "K ต่ำ + alkalosis = NH₃ เข้าสมอง", "Hepatic encephalopathy",
         nl=["2.3.6(6)", "B3.2.5(2)", "2.3.11(4)"]),
     mcq("GI-CIR-MCQ-19",
         "A drowsy patient with cirrhosis has asterixis and a serum ammonia of 45 µmol/L (normal). What is the correct interpretation?",
         ["A normal ammonia excludes hepatic encephalopathy", "Ammonia is not specific; HE is a clinical diagnosis after excluding other causes",
          "Lumbar puncture is required to confirm HE", "MRI brain showing typical lesions is diagnostic",
          "Treatment should wait until ammonia rises"],
         1,
         "สไลด์: วินิจฉัย HE โดย **ตัดสาเหตุอื่นออก** · ammonia สูง **แต่ไม่จำเพาะ** · CSF ปกติ · CT ไม่มีลักษณะเฉพาะ (ยกเว้น stage IV สมองบวม)\n\nผู้ป่วยมี asterixis + ซึม ในตับแข็ง → **ให้ lactulose และหาตัวเร่งเลย** ไม่ต้องรอผล ammonia · เพิ่มเติม: guideline ปัจจุบันบอกว่าค่า ammonia ปกติช่วยให้ทบทวนการวินิจฉัย แต่ไม่ใช้ปรับการรักษา",
         "HE = clinical diagnosis · ammonia ไม่ใช่ตัวตัดสิน", "Hepatic encephalopathy",
         nl=["2.3.6(6)", "B3.2.5(2)", "2.3.11(4)"]),
     mcq("GI-CIR-MCQ-20",
         "Lactulose is started for overt hepatic encephalopathy. What is the recommended titration target?",
         ["One hard stool every 2 days", "Two to four soft stools per day", "At least ten watery stools per day",
          "Stool pH above 8", "Normalisation of serum ammonia before stopping"],
         1,
         "สไลด์: **30–60 mL ทุก 1 ชั่วโมงจนกว่าจะถ่าย** แล้วปรับเป็น **15–30 mL วันละ 3 ครั้ง** ให้ **ถ่ายนิ่ม 2–4 ครั้งต่อวัน**\n\nถ่ายมากเกินไป → **ขาดน้ำ Na สูง K ต่ำ ไตวาย** ซึ่งกลับเป็นตัวเร่ง HE เอง · lactulose ทำให้ลำไส้ **เป็นกรด** (pH ต่ำ) ไม่ใช่ด่าง",
         "Lactulose: ถ่ายนิ่ม 2–4 ครั้ง/วัน", "Hepatic encephalopathy",
         nl=["2.3.6(6)", "2.3.11(4)"]),
     old("MOCK-151", nl=["2.3.6(6)", "B3.2.5(2)", "2.3.11(4)"], pearl="HE = NH₃ ค้าง + portosystemic shunt"),
     old("MOCK-096", nl=["2.3.6(6)", "B3.2.5(2)"], pearl="Asterixis สองข้าง = metabolic encephalopathy แบบกระจาย")],
    nl=["2.3.11(4)", "2.3.6(6)", "B3.2.5(2)", "B8.2.5-3(1)"],
    anims={"cir-he": ANIM_HE},
    mnem=[{"name": "HEPATICS", "what": "ตัวเร่ง hepatic encephalopathy ที่ต้องหาทุกครั้ง",
           "lines": [["H", "**Hemorrhage** (GI bleed) · Hypovolemia"], ["E", "**Electrolytes** — K ต่ำ · Na ต่ำ · alkalosis"],
                     ["P", "**Protein** มาก · **P**oor bowel (ท้องผูก)"], ["A", "**Azotemia** (ไตวาย)"],
                     ["T", "**Tranquilizers** — benzodiazepine · opioid"], ["I", "**Infection** — รวม SBP"],
                     ["C", "**Constipation**"], ["S", "**Shunt** (TIPS) · Surgery"]],
           "note": "รักษา HE = หาตัวเร่งก่อน แล้ว lactulose",
           "src": "หลักจำที่ใช้ทั่วไป (ไม่ได้มาจากสไลด์) · รายการตรงกับสไลด์หน้า 24–25"}])
