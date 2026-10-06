from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Hemato"

F_SNAKE = fig("hemato-10-01-f1", "งูพิษในไทย: neurotoxin vs hematotoxin และการติดตาม", '''<svg viewBox="0 0 740 400">
 <rect x="20" y="10" width="340" height="44" rx="10" class="c1"/>
 <text x="190" y="30" text-anchor="middle" class="tw">Neurotoxin</text>
 <text x="190" y="46" text-anchor="middle" class="tw">"จง เห่า สาม ครา"</text>
 <rect x="380" y="10" width="340" height="44" rx="10" class="bad"/>
 <text x="550" y="30" text-anchor="middle" class="tw">Hematotoxin</text>
 <text x="550" y="46" text-anchor="middle" class="tw">"แมว เขียว กะ หายเลือด"</text>
 <rect x="20" y="62" width="340" height="96" rx="10" class="c1soft"/>
 <text x="36" y="84" class="t2">งูจงอาง (King cobra)</text>
 <text x="36" y="104" class="t2">งูเห่า (Thai cobra) — เฉพาะที่บวมได้</text>
 <text x="36" y="124" class="t2">งูสามเหลี่ยม (Banded krait)</text>
 <text x="36" y="144" class="t2">งูทับสมิงคลา (Malayan krait)</text>
 <rect x="380" y="62" width="340" height="96" rx="10" class="badsoft"/>
 <text x="396" y="84" class="t2">งูแมวเซา (Russell's viper) → DIC, AKI</text>
 <text x="396" y="104" class="t2">งูเขียวหางไหม้ (Green pit viper)</text>
 <text x="396" y="124" class="t2">งูกะปะ (Malayan pit viper)</text>
 <text x="396" y="144" class="t3">บวมเฉพาะที่มาก → compartment syndrome</text>
 <rect x="20" y="166" width="340" height="96" rx="10" class="box"/>
 <text x="36" y="188" class="tb">อาการ</text>
 <text x="36" y="208" class="t2">Ptosis, กลืนลำบาก, พูดไม่ชัด</text>
 <text x="36" y="228" class="t2">กล้ามเนื้ออ่อนแรง → หายใจล้มเหลว</text>
 <text x="36" y="250" class="ta">ติดตาม: peak flow</text>
 <rect x="380" y="166" width="340" height="96" rx="10" class="box"/>
 <text x="396" y="188" class="tb">อาการ</text>
 <text x="396" y="208" class="t2">เลือดออกจากรอยเขี้ยว, ecchymosis</text>
 <text x="396" y="228" class="t2">mucosal bleeding, hematuria</text>
 <text x="396" y="250" class="ta">ติดตาม: 20-min WBCT / VCT</text>
 <rect x="20" y="270" width="340" height="120" rx="10" class="acsoft"/>
 <text x="36" y="292" class="tb">ให้ antivenom เมื่อ</text>
 <text x="36" y="314" class="t2">• ptosis หรือกล้ามเนื้ออ่อนแรงใด ๆ</text>
 <text x="36" y="342" class="tb">ใส่ท่อช่วยหายใจเมื่อ</text>
 <text x="36" y="362" class="t2">• กลืนลำบาก, PEF &lt; 200 L/min</text>
 <text x="36" y="380" class="t2">• ptosis, respiratory distress</text>
 <rect x="380" y="270" width="340" height="120" rx="10" class="acsoft"/>
 <text x="396" y="292" class="tb">ให้ antivenom เมื่อ</text>
 <text x="396" y="312" class="t2">• Systemic bleed (ยกเว้น micro hematuria)</text>
 <text x="396" y="330" class="t2">• 20WBCT ไม่แข็ง / VCT &gt; 20 นาที</text>
 <text x="396" y="348" class="t2">• Plt &lt; 50,000 · INR &gt; 1.2</text>
 <text x="396" y="366" class="t2">• Compartment syndrome</text>
 <text x="396" y="384" class="t3">ไม่ต้องทำ skin test · เฝ้าระวัง anaphylaxis</text>
</svg>''', "แยกงูตามพิษก่อน แล้วติดตามด้วยตัวชี้วัดของแต่ละกลุ่ม (peak flow vs clotting time) และให้ antivenom ตามเกณฑ์ในกล่องล่าง")

S1 = sec("hemato-10-01", "Snake bite",
    "Neurotoxin: จงอาง เห่า สามเหลี่ยม ทับสมิงคลา → peak flow, ptosis = antivenom · hematotoxin: แมวเซา เขียวหางไหม้ กะปะ → 20WBCT/VCT, ไม่แข็ง = antivenom", minutes=9,
    source=f"{D} หน้า 372–387", nl=["2.2.45", "2.3.18(8)", "B3.2.5(5)"],
    md='''
### ชนิดงูพิษ (ท่องจำ)

| กลุ่ม | ท่องจำ | งู |
|---|---|---|
| **Neurotoxin** | **"จง เห่า สาม ครา"** | งูจงอาง (King cobra), งูเห่า (Thai cobra), **งูสามเหลี่ยม (Banded krait — ลายปล้องดำสลับเหลือง)**, งูทับสมิงคลา (Malayan krait — ปล้องดำสลับขาว) |
| **Hematotoxin** | **"แมว เขียว กระ หายเลือด"** | **งูแมวเซา (Russell's viper)**, **งูเขียวหางไหม้ (Green pit viper)**, **งูกะปะ (Malayan pit viper)** |

(เสริม: งูแมวเซาเด่น DIC + **AKI**, งูกะปะ/เขียวหางไหม้เด่นเลือดออกและบวมเฉพาะที่มาก; งูเห่ามี local necrosis)

### อาการ

- **Local**: ปวด, รอยเขี้ยว, บวม, ecchymosis, necrosis, hemorrhagic bleb
- **Neurotoxin**: **ptosis**, dysphagia, dysarthria, dyspnea, กล้ามเนื้ออ่อนแรง → respiratory failure
- **Hematotoxin**: เลือดออกจากรอยเขี้ยว, generalized ecchymosis, mucosal bleeding

### การตรวจ

- **Hematotoxin: 20-min whole blood clotting time (20WBCT) หรือ VCT** + CBC, PT, PTT, INR, **UA, BUN, Cr (ดู AKI)**
- **Neurotoxin: peak flow**

[[fig:hemato-10-01-f1]]

### การรักษา

- **Initial: ABC**
- **Neurotoxin – ใส่ ETT เมื่อ**: dysphagia, **peak flow < 200 L/min**, ptosis, respiratory distress
- **Hematotoxin**: FFP, platelet transfusion เมื่อมี **systemic bleeding** (ร่วมกับ antivenom)
- **Wound care**, **rest & immobilization**, pain control **paracetamol** (เลี่ยง NSAIDs — เสริม)
- **ATB prophylaxis: amoxicillin/clavulanate เมื่อสงสัย infection**
- **Tetanus prophylaxis (หลัง VCT ปกติแล้ว)** — ฉีดเข้ากล้ามขณะเลือดไม่แข็งจะเกิด hematoma

### ข้อบ่งชี้ให้ antivenom

| Neurotoxin | Hematotoxin |
|---|---|
| **มี muscle weakness ใด ๆ หรือ ptosis** | **Systemic bleeding** (ยกเว้น microscopic hematuria) |
| | **20WBCT ไม่แข็ง หรือ VCT > 20 นาที** |
| | **Platelet < 50,000** |
| | **PT prolonged หรือ INR > 1.2** |
| | **Compartment syndrome** |

- **ไม่จำเป็นต้องทำ skin test** ก่อนให้เซรุ่ม · **เฝ้าระวัง anaphylaxis** หลังให้

### การติดตาม

- Neurotoxin: V/S, อาการหายใจลำบาก, neuro signs, compartment syndrome, urine output, **peak flow ซ้ำ**
- Hematotoxin: V/S, เลือดออก, compartment syndrome, urine output, **lab ซ้ำ (20WBCT/VCT, CBC, PT, PTT, INR)** — ถึงแรกรับปกติก็ต้อง **serial VCT** (เสริม: ทุก 6 ชม. อย่างน้อย 24 ชม.)

> ถูกงูกัด มีแค่บวม/รอยเขี้ยว ไม่มีอาการระบบ → **ยังไม่ให้ antivenom** แต่ติดตาม **serial VCT/20WBCT** · ถ้า 20WBCT ไม่แข็ง → **antivenom** (FFP ไม่ใช่การรักษาแรก)
''',
    figs=[F_SNAKE],
    pearls=[
        "Neurotoxin = จง เห่า สาม ครา · hematotoxin = แมว เขียว กะ",
        "Neurotoxin → peak flow · ETT เมื่อ PEF < 200, กลืนลำบาก, ptosis, distress",
        "Hematotoxin → 20WBCT/VCT · ไม่แข็ง/INR > 1.2/plt < 50k → antivenom",
        "ไม่ต้อง skin test ก่อนเซรุ่ม · tetanus หลัง VCT ปกติ",
    ],
    items=[
        mcq("HEMATO-10-01-1",
            "A patient is bitten by a snake with alternating black and bright yellow bands and a triangular body cross-section. He has no symptoms 30 minutes after the bite. What is the most appropriate investigation to monitor this patient?",
            "Serial peak expiratory flow",
            ["20-minute whole blood clotting time", "Pulmonary function test with spirometry", "Platelet count", "Serum creatine kinase"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ภาพงูเขียนเป็นข้อความ)",
            explain='''ลายปล้องดำสลับเหลือง ตัวเป็นสามเหลี่ยม = **งูสามเหลี่ยม (banded krait)** ซึ่งเป็น **neurotoxin** → ติดตามด้วย **peak flow** (PEF < 200 L/min ต้องใส่ท่อช่วยหายใจ)
- 20WBCT ใช้กับงู hematotoxin (แมวเซา เขียวหางไหม้ กะปะ)
- PFT/spirometry เต็มรูปแบบไม่เหมาะกับห้องฉุกเฉิน
- Platelet count ใช้ติดตาม hematotoxin
- CK ใช้กับ sea snake (myotoxin — เสริม)''',
            pearl="งูสามเหลี่ยม = neurotoxin → peak flow", topic="Neurotoxic snake monitoring",
            ref=[f"{D} หน้า 372, 374, 380–381"], nl=["2.2.45", "B3.2.5(5)"]),
        mcq("HEMATO-10-01-2",
            "A 50-year-old female farmer was bitten by an unidentified snake 1 hour ago. PE: swelling and redness with 2 fang marks on the dorsum of the right foot; no ptosis, no bleeding, otherwise unremarkable. Initial 20-minute whole blood clotting test shows a clot. What is the most appropriate management?",
            "Serial venous clotting time and clinical observation",
            ["Give antivenom immediately", "Discharge with oral antibiotics", "Give tetanus toxoid IM and discharge", "Give FFP prophylactically"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''มีรอยเขี้ยว + บวมเฉพาะที่ แต่**ยังไม่มีอาการระบบ**และการแข็งตัวปกติ → ยังไม่มีข้อบ่งชี้ antivenom แต่พิษ hematotoxin อาจออกฤทธิ์ช้า → **serial VCT/20WBCT** ร่วมกับติดตามอาการ (และ peak flow ถ้าไม่ทราบชนิดงู)
- Antivenom ให้เมื่อมีข้อบ่งชี้ (systemic bleed, WBCT ไม่แข็ง, INR > 1.2, plt < 50,000, weakness/ptosis)
- กลับบ้านเลยไม่ปลอดภัย
- Tetanus ให้หลังยืนยันว่า VCT ปกติต่อเนื่อง และไม่ควรเป็นสิ่งเดียวที่ทำ
- FFP ป้องกันไม่มีประโยชน์''',
            pearl="รอยเขี้ยวไม่มีอาการระบบ → serial VCT", topic="Observation after snake bite",
            ref=[f"{D} หน้า 379, 382–383"], nl=["2.2.45", "2.3.18(8)"]),
        mcq("HEMATO-10-01-3",
            "A patient comes to the emergency room 30 minutes after a snake bite. He has swelling of the right foot with fang marks. The 20-minute whole blood clotting test shows unclotted blood. There is no active bleeding. What is the most appropriate initial management?",
            "Antivenom",
            ["Fresh frozen plasma", "Cryoprecipitate", "Tetanus toxoid", "Dexamethasone"],
            kind="old", src="ข้อสอบเก่าในสไลด์",
            explain='''**20WBCT ไม่แข็ง** = venom-induced consumption coagulopathy → **ข้อบ่งชี้ให้ antivenom** (ไม่ต้อง skin test เฝ้าระวัง anaphylaxis)
- FFP/cryoprecipitate ไม่แก้พิษที่ยังทำลาย factor อยู่ ใช้เสริมเมื่อมี systemic bleeding
- Tetanus toxoid ให้หลัง VCT ปกติ (ฉีดตอนนี้เสี่ยง hematoma)
- Dexamethasone ไม่มีบทบาท''',
            pearl="20WBCT ไม่แข็ง → antivenom", topic="Hematotoxic antivenom",
            ref=[f"{D} หน้า 378, 384–385"], nl=["2.2.45", "2.3.18(8)"]),
        mcq("HEMATO-10-01-4",
            "A rubber tapper is bitten by a snake identified as a Malayan pit viper. Six hours later the foot and entire leg are tensely swollen with hemorrhagic blebs. The 20-minute whole blood clotting test is unclotted. Which complication is most characteristic of this snake?",
            "Compartment syndrome",
            ["Respiratory failure", "Ptosis and descending paralysis", "Rhabdomyolysis with myoglobinuria", "Hypoglycemia"],
            kind="old", src="ข้อสอบเก่าในสไลด์ (ภาพงูเขียนเป็นข้อความ; เฉลยในสไลด์เป็นภาพ — ตอบตามลักษณะงูกะปะ)",
            explain='''**งูกะปะ (Malayan pit viper) = hematotoxin** ทำให้ coagulopathy และ**บวมเฉพาะที่รุนแรง** (bleb, necrosis) จนอาจเกิด **compartment syndrome** (ซึ่งเป็นข้อบ่งชี้ antivenom ในสไลด์) — DIC-like coagulopathy ก็พบได้
- Respiratory failure และ ptosis/paralysis เป็นของงู neurotoxin (จงอาง เห่า สามเหลี่ยม ทับสมิงคลา)
- Rhabdomyolysis เด่นใน sea snake (myotoxin) และพบได้ในงูแมวเซา
- Hypoglycemia ไม่ใช่ภาวะแทรกซ้อนเด่น
(ถ้าตัวเลือกมี DIC ก็เป็นคำตอบที่ถูกได้ — สไลด์เดิมมีทั้ง compartment syndrome และ DIC ในตัวเลือก)''',
            pearl="งูกะปะ = hematotoxin + บวมมาก → compartment syndrome", topic="Malayan pit viper",
            ref=[f"{D} หน้า 372, 378, 386–387"], nl=["2.2.45", "2.3.18(8)"]),
        mcq("HEMATO-10-01-5",
            "A 30-year-old man bitten by a cobra 2 hours ago develops bilateral ptosis and difficulty swallowing. Peak expiratory flow is 180 L/min and falling. What is the most appropriate management?",
            "Endotracheal intubation with ventilatory support and antivenom",
            ["Antivenom only after a skin test", "Observe and repeat peak flow in 6 hours", "Neostigmine alone without airway support", "FFP and platelet transfusion"],
            explain='''Neurotoxic envenomation: **ptosis/อ่อนแรง → ข้อบ่งชี้ antivenom** และ **dysphagia + PEF < 200 L/min → ใส่ ETT** ตามสไลด์
- ไม่ต้องทำ skin test ก่อนให้เซรุ่ม (ไม่ช่วยทำนายและเสียเวลา)
- รอ 6 ชั่วโมงเสี่ยงหยุดหายใจ
- Neostigmine อาจช่วยในงูเห่า (postsynaptic) เป็นส่วนเสริม แต่ห้ามใช้แทนการดูแลทางเดินหายใจ
- FFP/platelet เป็นการรักษา hematotoxin''',
            pearl="Neurotoxin + PEF < 200/กลืนลำบาก → ETT + antivenom", topic="Neurotoxic management",
            ref=[f"{D} หน้า 376, 378"], nl=["2.2.45", "B3.2.5(5)", "2.2.9"]),
    ])

LECTURE = lecture("10", "Snake bite",
    "Neurotoxin vs hematotoxin · 20WBCT · peak flow · antivenom",
    objectives=[
        "จำแนกงูพิษในไทยเป็น neurotoxin และ hematotoxin ได้",
        "เลือกการติดตาม (peak flow vs 20WBCT/VCT) ตามชนิดงู",
        "ระบุข้อบ่งชี้ antivenom และการใส่ท่อช่วยหายใจได้",
        "ดูแลแผล ยาแก้ปวด ยาปฏิชีวนะ และ tetanus อย่างเหมาะสม",
    ],
    sections=[S1])
