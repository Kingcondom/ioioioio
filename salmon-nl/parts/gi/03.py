from lib import lecture, sec, mcq, fig

D = "สไลด์ NL2-GI"
OLD = "ตัวอย่างข้อสอบในสไลด์ NL2-GI"

TY = '''<svg viewBox="0 0 720 290">
 <defs><marker id="gi-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="150" height="56" rx="9" class="box"/>
 <text x="85" y="33" text-anchor="middle" class="tb">อาหาร/น้ำปนเปื้อน</text>
 <text x="85" y="53" text-anchor="middle" class="t3">fecal-oral</text>
 <path d="M160 38H196" class="ln" marker-end="url(#gi-03-01-a)"/>
 <rect x="198" y="10" width="170" height="56" rx="9" class="c1soft"/>
 <text x="283" y="33" text-anchor="middle" class="tb">Peyer patches</text>
 <text x="283" y="53" text-anchor="middle" class="t3">distal ileum → macrophage</text>
 <path d="M368 38H404" class="ln" marker-end="url(#gi-03-01-a)"/>
 <rect x="406" y="10" width="304" height="56" rx="9" class="c2soft"/>
 <text x="558" y="33" text-anchor="middle" class="tb">กระจายทั่ว RES</text>
 <text x="558" y="53" text-anchor="middle" class="t3">LN · ตับ · ม้าม · ไขกระดูก · ถุงน้ำดี</text>
 <path d="M20 130H700" class="lna" marker-end="url(#gi-03-01-a)"/>
 <path d="M30 122V138M250 122V138M470 122V138M690 122V138" class="ln"/>
 <text x="140" y="118" text-anchor="middle" class="ta">สัปดาห์ที่ 1</text>
 <text x="360" y="118" text-anchor="middle" class="ta">สัปดาห์ที่ 2</text>
 <text x="580" y="118" text-anchor="middle" class="ta">สัปดาห์ที่ 2–4</text>
 <rect x="30" y="150" width="210" height="104" rx="9" class="misssoft"/>
 <text x="135" y="172" text-anchor="middle" class="tb">ไข้ค่อย ๆ สูง (step-ladder)</text>
 <text x="135" y="194" text-anchor="middle">malaise · anorexia</text>
 <text x="135" y="214" text-anchor="middle">ท้องผูก (constipation)</text>
 <text x="135" y="240" text-anchor="middle" class="t3">Hemoculture ให้ผลบวกสูงสุด</text>
 <rect x="250" y="150" width="210" height="104" rx="9" class="acsoft"/>
 <text x="355" y="172" text-anchor="middle" class="tb">ไข้สูงลอย</text>
 <text x="355" y="194" text-anchor="middle">Relative bradycardia</text>
 <text x="355" y="214" text-anchor="middle">Rose spots · HSM</text>
 <text x="355" y="236" text-anchor="middle">ถ่ายเหลวไม่มีเลือด</text>
 <rect x="470" y="150" width="230" height="104" rx="9" class="badsoft"/>
 <text x="585" y="172" text-anchor="middle" class="tb">Complications</text>
 <text x="585" y="194" text-anchor="middle">Intestinal bleeding</text>
 <text x="585" y="214" text-anchor="middle">Perforation (ileum)</text>
 <text x="585" y="240" text-anchor="middle" class="t3">หายแล้วบางรายเป็น chronic carrier</text>
 <text x="360" y="280" text-anchor="middle" class="t3">Widal test ไม่แนะนำ (sensitivity/specificity ต่ำ)</text>
</svg>'''

GE = '''<svg viewBox="0 0 720 330">
 <rect x="10" y="10" width="345" height="40" rx="9" class="c1"/>
 <text x="182" y="36" text-anchor="middle" class="tw">Watery diarrhea (noninflammatory)</text>
 <rect x="365" y="10" width="345" height="40" rx="9" class="bad"/>
 <text x="537" y="36" text-anchor="middle" class="tw">Bloody diarrhea (inflammatory)</text>
 <rect x="10" y="58" width="345" height="262" rx="9" class="c1soft"/>
 <text x="26" y="82" class="ta">Virus</text>
 <text x="26" y="102">Norovirus · Rotavirus · Adenovirus</text>
 <text x="26" y="132" class="ta">Bacteria</text>
 <text x="26" y="152">ETEC <tspan class="t3">— เดินทาง (traveler)</tspan></text>
 <text x="26" y="172">V. cholerae <tspan class="t3">— อาหารทะเล/น้ำ ถ่ายมาก</tspan></text>
 <text x="26" y="192">C. difficile <tspan class="t3">— เพิ่งได้ ATB</tspan></text>
 <text x="26" y="212">C. perfringens</text>
 <text x="26" y="242" class="ta">Protozoa</text>
 <text x="26" y="262">Giardia lamblia</text>
 <text x="26" y="282">Cryptosporidium <tspan class="t3">— immunocompromised</tspan></text>
 <text x="26" y="308" class="t3">Stool: WBC/RBC น้อย</text>
 <rect x="365" y="58" width="345" height="262" rx="9" class="badsoft"/>
 <text x="381" y="82" class="ta">Bacteria</text>
 <text x="381" y="102">EIEC · EHEC</text>
 <text x="381" y="122">Campylobacter jejuni <tspan class="t3">— สัตว์ปีก</tspan></text>
 <text x="381" y="142">Nontyphoidal Salmonella <tspan class="t3">— ไก่ ไข่</tspan></text>
 <text x="381" y="162">Shigella</text>
 <text x="381" y="182">Yersinia enterocolitica</text>
 <text x="381" y="202">V. parahaemolyticus <tspan class="t3">— หอย</tspan></text>
 <text x="381" y="222">V. vulnificus <tspan class="t3">— หอย</tspan></text>
 <text x="381" y="252" class="ta">Protozoa</text>
 <text x="381" y="272">Entamoeba histolytica</text>
 <text x="381" y="308" class="t3">Stool: WBC/RBC มาก · ห้ามให้ loperamide</text>
</svg>'''

IBS = '''<svg viewBox="0 0 720 360">
 <defs><marker id="gi-03-04-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="170" y="8" width="380" height="40" rx="9" class="acsoft"/>
 <text x="360" y="33" text-anchor="middle" class="tb">เข้าเกณฑ์ Rome IV + ไม่มี alarm features</text>
 <path d="M360 48V68" class="ln" marker-end="url(#gi-03-04-a)"/>
 <rect x="120" y="70" width="480" height="44" rx="9" class="box"/>
 <text x="360" y="89" text-anchor="middle" class="tb">อธิบายโรค · LSM ทุกราย</text>
 <text x="360" y="106" text-anchor="middle" class="t3">Low FODMAP · high fiber low fat · exercise · จัดการความเครียด</text>
 <path d="M360 114V132M120 132H600M120 132V150M360 132V150M600 132V150" class="ln"/>
 <path d="M120 146V152" class="ln" marker-end="url(#gi-03-04-a)"/><path d="M360 146V152" class="ln" marker-end="url(#gi-03-04-a)"/><path d="M600 146V152" class="ln" marker-end="url(#gi-03-04-a)"/>
 <rect x="10" y="154" width="220" height="36" rx="8" class="c1soft"/>
 <text x="120" y="177" text-anchor="middle" class="tb">อาการปวดท้องเด่น</text>
 <rect x="250" y="154" width="220" height="36" rx="8" class="c2soft"/>
 <text x="360" y="177" text-anchor="middle" class="tb">ท้องผูกเด่น (IBS-C)</text>
 <rect x="490" y="154" width="220" height="36" rx="8" class="misssoft"/>
 <text x="600" y="177" text-anchor="middle" class="tb">ท้องเสียเด่น (IBS-D)</text>
 <path d="M120 190V208" class="ln" marker-end="url(#gi-03-04-a)"/><path d="M360 190V208" class="ln" marker-end="url(#gi-03-04-a)"/><path d="M600 190V208" class="ln" marker-end="url(#gi-03-04-a)"/>
 <rect x="10" y="210" width="220" height="56" rx="8" class="box"/>
 <text x="120" y="232" text-anchor="middle">Antispasmodic</text>
 <text x="120" y="252" text-anchor="middle" class="t3">Buscopan · peppermint oil</text>
 <rect x="250" y="210" width="220" height="56" rx="8" class="box"/>
 <text x="360" y="232" text-anchor="middle">Fiber / laxative</text>
 <text x="360" y="252" text-anchor="middle" class="t3">PEG · MOM · lactulose</text>
 <rect x="490" y="210" width="220" height="56" rx="8" class="box"/>
 <text x="600" y="232" text-anchor="middle">Loperamide · ondansetron</text>
 <text x="600" y="252" text-anchor="middle" class="t3">ไม่ดี → rifaximin, bile acid binder</text>
 <path d="M120 266V290M360 266V290M600 266V290" class="ln"/>
 <text x="128" y="282" class="t3">ไม่ตอบสนอง</text>
 <path d="M120 290H600M360 290V304" class="ln"/>
 <path d="M360 300V306" class="ln" marker-end="url(#gi-03-04-a)"/>
 <rect x="200" y="308" width="320" height="44" rx="9" class="oksoft"/>
 <text x="360" y="327" text-anchor="middle" class="tb">TCA ขนาดต่ำ (neuromodulator)</text>
 <text x="360" y="344" text-anchor="middle" class="t3">ยังไม่ดี → ส่งต่อแพทย์ทางเดินอาหาร</text>
</svg>'''

LECTURE = lecture("03", "GI infection & IBS",
    subtitle="Typhoid · food poisoning · infectious gastroenteritis · irritable bowel syndrome",
    objectives=[
        "วินิจฉัย typhoid fever จากอาการตามสัปดาห์ เลือก hemoculture และยาฆ่าเชื้อได้",
        "จัดการ chronic Salmonella carrier ด้วยการหา gallstone และให้ยาที่เหมาะสม",
        "แยก food poisoning (preformed toxin) จาก infectious diarrhea และแยกเชื้อ watery vs bloody ได้",
        "รู้ข้อบ่งชี้ stool culture/ATB และข้อห้าม loperamide ใน inflammatory diarrhea",
        "วินิจฉัย IBS ด้วย Rome IV และเลือกการรักษาตามอาการเด่น",
    ],
    sections=[
    sec("gi-03-01", "Typhoid & paratyphoid fever (enteric fever)",
        "ไข้นาน + ท้องผูกแล้วท้องเสีย + relative bradycardia + rose spots → hemoculture → ceftriaxone/azithromycin", minutes=6,
        source=f"{D} หน้า 55–63", nl=["2.3.1(21)"],
        md='''
### เชื้อและกลไก
- *Salmonella* Typhi → typhoid fever · *Salmonella* Paratyphi → paratyphoid fever
- ติดต่อ **fecal-oral** (อาหาร/น้ำปนเปื้อน)
- เชื้อบุกเข้า **macrophage** แล้วกระจายไป lymph nodes, ตับ, ม้าม, ไขกระดูก, **Peyer patches ของ distal ileum** และ **ถุงน้ำดี**

[[fig:gi-03-01-tl]]

### อาการ
- ไข้ อ่อนเพลีย เบื่ออาหาร
- **ท้องผูกช่วงแรก** แล้วจึง **ถ่ายเหลวไม่มีเลือด** ภายหลัง
- ปวดท้อง กดเจ็บทั่วท้อง hepatosplenomegaly
- **Relative bradycardia** (ไข้สูงแต่ชีพจรไม่เร็วตาม)
- **Rose spots** = ผื่น erythematous macular จาง ๆ ที่ลำตัว/ท้อง
- ภาวะแทรกซ้อน (สัปดาห์ที่ 2–4): **intestinal bleeding, perforation**

### การตรวจ
- **Hemoculture** (หลัก) · stool C/S (bone marrow culture ไวที่สุด แม้ได้ยาแล้ว — เสริม)
- **Widal test ไม่แนะนำ** เพราะ sensitivity และ specificity ต่ำ

### การรักษา
- **Ceftriaxone, Azithromycin**, TMP/SMX
- Fluoroquinolone (ciprofloxacin, ofloxacin, levofloxacin) — **ระยะหลังพบเชื้อดื้อ FQ มากขึ้น**

### Chronic Salmonella carriage
- Stool culture **ยังบวกนาน 12 เดือน** หลังหายป่วย
- เชื้อ *S.* Typhi อยู่ใน **ถุงน้ำดี** (มักพบร่วมกับ gallstone) ไม่มีอาการ
- **Ix: U/S gallbladder** (หานิ่ว)
- **Tx: ciprofloxacin หรือ TMP/SMX 2–4 สัปดาห์**; ถ้ามี gallstone → **cholecystectomy**
- ภาวะแทรกซ้อน: เพิ่มความเสี่ยง **มะเร็งถุงน้ำดี**

> โจทย์ "แม่ครัว/คนทำอาหาร สบายดี ตรวจประจำปีเจอ *S.* Typhi ในอุจจาระ" → **U/S liver & gallbladder** เพื่อหา gallstone
''',
        figs=[fig("gi-03-01-tl", "Typhoid: เส้นทางเชื้อและอาการตามสัปดาห์", TY,
                  "แถวบนคือเส้นทางเชื้อ แถวล่างคืออาการที่เด่นในแต่ละสัปดาห์ ภาวะแทรกซ้อนลำไส้ทะลุ/เลือดออกเกิดสัปดาห์ที่ 2–4")],
        pearls=[
            "Typhoid: ท้องผูกก่อนแล้วถ่ายเหลว + relative bradycardia + rose spots",
            "ส่ง hemoculture; Widal ไม่แนะนำ",
            "Tx: ceftriaxone หรือ azithromycin (FQ ดื้อมากขึ้น)",
            "Chronic carrier: stool + นาน 12 เดือน → U/S GB; cipro/TMP-SMX 2–4 wk ± cholecystectomy",
        ],
        items=[
            mcq("GI-03-01-1", "A 14-year-old girl has fever, chills, abdominal pain and profuse non-bloody diarrhea. Her illness began 2 weeks ago with several days of low-grade fever and constipation. Temperature 39.3 °C. She has diffuse abdominal tenderness, mild hepatosplenomegaly and a pink maculopapular rash on the trunk and abdomen. Which is the most likely causative organism?",
                "Salmonella Typhi", ["Vibrio cholerae", "Escherichia coli", "Shigella dysenteriae", "Entamoeba histolytica"],
                explain='''ไข้ที่ค่อย ๆ เป็นนาน 2 สัปดาห์ เริ่มด้วย **ท้องผูกแล้วตามด้วยถ่ายเหลวไม่มีเลือด** + **hepatosplenomegaly** + **rose spots** ที่ลำตัว = typhoid fever จาก *S.* Typhi
- *V. cholerae* ถ่ายเป็นน้ำมากเฉียบพลัน ไม่มีไข้สูงนาน ไม่มีตับม้ามโต
- *E. coli* (ETEC) ท้องเสียเฉียบพลันสั้น ๆ ไม่มีไข้สูงหรือผื่น
- *Shigella* ถ่ายเป็นมูกเลือด ปวดเบ่ง
- *E. histolytica* ถ่ายมูกเลือดเรื้อรัง ไม่มีผื่นหรือ HSM แบบนี้''',
                pearl="ไข้นาน + ท้องผูกแล้วถ่ายเหลว + rose spots + HSM = typhoid", topic="Typhoid diagnosis",
                ref=[f"{D} หน้า 60–61"], nl=["2.3.1(21)"], kind="old", src=OLD),
            mcq("GI-03-01-2", "A healthy cook has a routine annual stool examination that grows Salmonella Typhi. She has no symptoms. Which is the most appropriate investigation?",
                "Ultrasound of the liver and gallbladder", ["Hand and nail swab culture", "Hemoculture", "Nasal swab culture", "Widal test"],
                explain='''คนไม่มีอาการแต่ stool พบ *S.* Typhi = **chronic carrier** ซึ่งเชื้ออาศัยใน **ถุงน้ำดี** โดยเฉพาะเมื่อมี gallstone ต้องทำ **U/S liver & gallbladder** เพื่อหานิ่ว เพราะถ้ามีนิ่วต้องตัดถุงน้ำดีร่วมด้วย
- Hand/nail swab และ nasal swab ไม่ใช่แหล่งเก็บเชื้อของ typhoid carrier (nasal swab ใช้หา *S. aureus* carrier)
- Hemoculture มักลบในคนไม่มีอาการ ไม่ช่วยวางแผน
- Widal test ไม่แนะนำเพราะ sensitivity/specificity ต่ำ''',
                pearl="Typhoid carrier → U/S หา gallstone", topic="Chronic carrier",
                ref=[f"{D} หน้า 59, 62–63"], nl=["2.3.1(21)"], kind="old", src=OLD),
            mcq("GI-03-01-3", "A 25-year-old man has had fever for 9 days with headache, malaise and constipation. Temperature 39.5 °C with pulse 84/min. He has faint salmon-colored macules on the abdomen and a palpable spleen. Which test is most appropriate to confirm the diagnosis?",
                "Blood culture", ["Widal test", "Stool occult blood", "Weil-Felix test", "Abdominal ultrasound"],
                explain='''ไข้สูงแต่ชีพจรช้า (**relative bradycardia**) + rose spots + ม้ามโต → สงสัย typhoid ยืนยันด้วย **hemoculture** ซึ่งบวกสูงในสัปดาห์แรก–สอง
- Widal test ไม่แนะนำ ผลบวกลวง/ลบลวงสูง
- Stool occult blood ไม่จำเพาะ
- Weil-Felix ใช้กับ rickettsia (scrub typhus/murine typhus) และไม่แนะนำแล้วเช่นกัน
- Abdominal U/S ไม่ได้ยืนยันเชื้อ''',
                pearl="Typhoid ยืนยันด้วย hemoculture ไม่ใช่ Widal", topic="Typhoid investigation",
                ref=[f"{D} หน้า 57"], nl=["2.3.1(21)"]),
            mcq("GI-03-01-4", "A 30-year-old woman with blood culture-proven typhoid fever is admitted. She has persistent fever 39 °C but no signs of perforation. Local surveillance reports high fluoroquinolone resistance among Salmonella Typhi isolates. Which is the most appropriate antibiotic?",
                "IV ceftriaxone", ["Oral ciprofloxacin", "Oral metronidazole", "Oral amoxicillin-clavulanate", "IV vancomycin"],
                explain='''Typhoid ในพื้นที่ที่ **ดื้อ fluoroquinolone** ให้ **ceftriaxone** (หรือ azithromycin ถ้าเป็นผู้ป่วยนอก) ตามสไลด์
- Ciprofloxacin เป็นยาที่ใช้ได้ แต่สไลด์ระบุว่าเชื้อดื้อ FQ มากขึ้นเรื่อย ๆ และโจทย์บอกว่าดื้อสูง
- Metronidazole ไม่ครอบคลุม *Salmonella*
- Amoxicillin-clavulanate ไม่ใช่ยาที่แนะนำและเจาะเข้า intracellular ได้ไม่ดี
- Vancomycin ไม่ครอบคลุม gram-negative''',
                pearl="Typhoid: ceftriaxone/azithromycin; FQ ดื้อมากขึ้น", topic="Typhoid treatment",
                ref=[f"{D} หน้า 58"], nl=["2.3.1(21)"]),
        ]),

    sec("gi-03-02", "Food poisoning",
        "อาเจียนเด่น เกิดเป็นกลุ่มหลังกินอาหารเดียวกัน จาก preformed toxin → clinical dx + supportive", minutes=3,
        source=f"{D} หน้า 64", nl=["2.3.1(7)"],
        md='''
### นิยาม
Food poisoning (food-borne intoxication) เกิดจาก **กินสารพิษของแบคทีเรียที่สร้างไว้ในอาหาร** (preformed toxin) จึงมีอาการเร็วหลังกิน (1–6 ชม. — เสริม)

### ลักษณะ
- **อาเจียนเด่น** (ยกเว้น *C. perfringens* ที่ **ท้องเสียเด่น**)
- ถ่ายเหลวเป็นน้ำ ปวดเกร็งท้อง ไม่ค่อยมีไข้
- **คนที่กินอาหารชนิดเดียวกันมีอาการเหมือนกัน**
- วินิจฉัยทางคลินิก
- **Tx: supportive** (ORS, antiemetic) — ไม่ต้องให้ยาฆ่าเชื้อ

| เชื้อ | อาหารที่เกี่ยวข้อง (ตามสไลด์) | จุดเด่น |
|---|---|---|
| *Staphylococcus aureus* | อาหารที่ทิ้งไว้ให้เย็นที่อุณหภูมิห้อง (สลัด มายองเนส — เสริม) | อาเจียนมาก เริ่มเร็ว 1–6 ชม. |
| *Bacillus cereus* | **ข้าวผัด** (ข้าวสุกค้าง), เนื้อสัตว์ ผัก | emetic type อาเจียน |
| *Clostridium perfringens* | อาหารกระป๋อง เนื้อสัตว์ (อุ่นซ้ำ) | **ท้องเสียเด่น** 8–16 ชม. (เสริม) |

> ระยะฟักตัวสั้นมาก + อาเจียนเด่น + หลายคนเป็นพร้อมกัน → toxin ไม่ใช่การติดเชื้อ — ไม่ต้อง stool culture ไม่ต้อง ATB
''',
        pearls=[
            "Food poisoning = preformed toxin → อาเจียนเด่น เกิดเร็ว เป็นกลุ่ม",
            "ข้าวผัดค้าง = B. cereus · อาหารทิ้งไว้ที่อุณหภูมิห้อง = S. aureus",
            "C. perfringens ท้องเสียเด่นกว่าอาเจียน",
            "รักษา supportive: ORS, antiemetic — ไม่ให้ ATB",
        ],
        items=[
            mcq("GI-03-02-1", "Four office workers develop severe nausea and repeated vomiting 2 hours after sharing leftover fried rice that had been kept at room temperature overnight. They are afebrile. Which organism is most likely responsible?",
                "Bacillus cereus", ["Clostridium perfringens", "Vibrio parahaemolyticus", "Campylobacter jejuni", "Salmonella Typhi"],
                explain='''อาการอาเจียนเด่นภายในไม่กี่ชั่วโมงหลังกิน **ข้าวผัด/ข้าวสุกค้าง** หลายคนเป็นพร้อมกัน = food poisoning จาก preformed emetic toxin ของ ***B. cereus***
- *C. perfringens* ทำให้ท้องเสียเด่น ระยะฟักนานกว่า (8–16 ชม.) จากเนื้อสัตว์อุ่นซ้ำ
- *V. parahaemolyticus* มาจากอาหารทะเล/หอยดิบ และเป็นการติดเชื้อที่มีระยะฟักนานกว่า
- *Campylobacter* มาจากสัตว์ปีก ทำให้ท้องเสียมีไข้ มักมีเลือด
- *S.* Typhi ทำให้ไข้นานเป็นสัปดาห์ ไม่ใช่อาเจียนเฉียบพลัน''',
                pearl="ข้าวผัดค้าง + อาเจียนเร็ว = B. cereus", topic="Food poisoning organisms",
                ref=[f"{D} หน้า 64"], nl=["2.3.1(7)"]),
            mcq("GI-03-02-2", "Several guests vomit repeatedly 3 hours after eating cream-filled pastries that were left at room temperature during a wedding party. One guest, a 40-year-old man, has mild abdominal cramps, no fever, pulse 92/min and BP 118/74 mmHg, and tolerates fluids. Which is the most appropriate management?",
                "Oral rehydration solution and an antiemetic", ["Ciprofloxacin for 3 days", "Stool culture before any treatment", "IV metronidazole", "Loperamide plus azithromycin"],
                explain='''Food poisoning จาก *S. aureus* enterotoxin (อาหารทิ้งไว้อุณหภูมิห้อง อาการเร็ว อาเจียนเด่น เป็นกลุ่ม) วินิจฉัยทางคลินิกและรักษา **supportive ด้วย ORS และ antiemetic**
- Ciprofloxacin ไม่มีประโยชน์เพราะโรคเกิดจาก toxin ไม่ใช่เชื้อที่กำลังแบ่งตัว
- Stool culture ไม่จำเป็นในอาการไม่รุนแรงและเป็นเพียงไม่กี่ชั่วโมง
- Metronidazole ใช้กับ anaerobe/protozoa ไม่เกี่ยว
- Loperamide + azithromycin ใช้ใน traveler's diarrhea ที่รุนแรง ไม่ใช่ toxin-mediated vomiting''',
                pearl="Food poisoning: ORS + antiemetic ไม่ต้อง ATB", topic="Food poisoning management",
                ref=[f"{D} หน้า 64"], nl=["2.3.1(7)", "B8.4(4)"]),
        ]),

    sec("gi-03-03", "Infectious gastroenteritis",
        "แยก watery vs bloody → ส่ง stool เมื่อรุนแรง/เลือด/> 1 wk → ORS ± cipro/azithro 3 วัน; ห้าม loperamide ใน inflammatory", minutes=7,
        source=f"{D} หน้า 65–76", nl=["2.3.1(7)", "2.1.18", "B8.4(4)"],
        md='''
### แบ่งตามลักษณะอุจจาระ
[[fig:gi-03-03-ge]]

### Clue จากประวัติ (ตามสไลด์)
| Clue | เชื้อ |
|---|---|
| เพิ่งเดินทาง (traveler's diarrhea) | ETEC |
| อาหารทะเลไม่สุก น้ำปนเปื้อน + **ถ่ายเป็นน้ำปริมาณมาก** | *Vibrio cholerae* |
| เพิ่งได้ยาฆ่าเชื้อ | *Clostridioides difficile* |
| ภูมิคุ้มกันบกพร่อง | *Cryptosporidium* |
| สัตว์ปีก (poultry) | *Campylobacter jejuni* |
| หอย/สัตว์มีเปลือก | *V. parahaemolyticus*, *V. vulnificus* |
| สัตว์ปีกและไข่ | Nontyphoidal *Salmonella* |

### Cholera (ข้อสอบชอบ)
ถ่ายเหลวเป็นน้ำซาวข้าว ปริมาณมาก **ไม่ปวดท้อง ไม่มีไข้** → ขาดน้ำรุนแรง: sunken eyeball, hypotension, Hct สูง (hemoconcentration), **pre-renal AKI** (BUN/Cr > 20), **hypokalemia**, **normal anion gap metabolic acidosis** (เสีย HCO3 ทางอุจจาระ) — กลไก: cholera toxin → ↑cAMP → Cl⁻ secretion (เสริม)

### ข้อบ่งชี้ส่ง stool exam & culture
- Severe dehydration
- อาการ > 1 สัปดาห์
- ไข้สูง หรือ **bloody diarrhea**
- ผู้สูงอายุ / immunocompromised

### การรักษา
| ความรุนแรง | การรักษา |
|---|---|
| Mild watery diarrhea | Supportive: **ORS** |
| Severe watery หรือ bloody diarrhea | ORS หรือ **IV fluid** (กรณี severe) + **ATB: ciprofloxacin, levofloxacin, azithromycin 3 วัน** |

**Antidiarrheal**: bismuth subsalicylate, racecadotril, loperamide
> **Loperamide ห้ามให้ใน inflammatory diarrhea** (ไข้, ถ่ายเป็นเลือด) เพราะอาจทำให้เกิด **toxic megacolon**

> Watery diarrhea ที่มีภาวะขาดน้ำ (BP ต่ำ ปากแห้ง) แต่ไม่มีไข้ stool ไม่มี WBC/RBC → คำตอบคือ **IV fluid** ไม่ใช่ยาฆ่าเชื้อ
''',
        figs=[fig("gi-03-03-ge", "เชื้อก่อ infectious diarrhea แยกตามลักษณะอุจจาระ", GE,
                  "ซ้ายคือกลุ่มถ่ายเป็นน้ำ (toxin/ไม่ทำลาย mucosa) ขวาคือกลุ่มถ่ายเป็นเลือด (invasive) พร้อม clue ประวัติอาหาร")],
        pearls=[
            "Cholera: ถ่ายน้ำมาก ไม่ปวด ไม่มีไข้ → hypokalemia + NAGMA + prerenal AKI",
            "Campylobacter = สัตว์ปีก, bloody diarrhea; V. parahaemolyticus = อาหารทะเล/หอย",
            "Watery diarrhea + dehydration ไม่มีไข้ → IV fluid/ORS เป็นหลัก",
            "ATB (cipro/levo/azithro 3 วัน) เมื่อ severe watery หรือ bloody diarrhea",
            "ห้าม loperamide ในไข้/ถ่ายเป็นเลือด → toxic megacolon",
        ],
        items=[
            mcq("GI-03-03-1", "A previously healthy 45-year-old man has nausea, vomiting and watery diarrhea for 12 hours. Temperature 36.7 °C, pulse 80/min, BP 90/60 mmHg. Lips are dry; abdomen is soft and non-tender with hyperactive bowel sounds. Stool examination shows watery stool with RBC 0–1 and WBC 0–1 cells/HPF. What is the most appropriate management?",
                "IV fluid", ["Norfloxacin", "Ciprofloxacin", "Metronidazole", "Ceftriaxone"],
                explain='''Acute **noninflammatory watery diarrhea** (ไม่มีไข้ stool ไม่มี WBC/RBC) ที่ขาดน้ำจน BP 90/60 → การรักษาหลักคือ **แก้ภาวะขาดน้ำด้วย IV fluid** ส่วนใหญ่เกิดจากไวรัส/toxin และหายเอง
- Norfloxacin/ciprofloxacin ใช้เมื่อ severe watery หรือ bloody diarrhea หรือมีไข้สูง ซึ่งผู้ป่วยนี้ไม่มี
- Metronidazole ใช้กับ amoebiasis, giardiasis, C. difficile
- Ceftriaxone ใช้ใน invasive diarrhea/typhoid ที่รุนแรง''',
                pearl="Watery diarrhea + dehydration ไม่มีไข้ → fluid ไม่ใช่ ATB", topic="Acute watery diarrhea",
                ref=[f"{D} หน้า 68–70"], nl=["2.1.18", "B8.4(4)"], kind="old", src=OLD),
            mcq("GI-03-03-2", "A 20-year-old man has had watery diarrhea 12 times in 1 day, described as rice-water with mucus but no blood. He has no abdominal pain. BP 90/50 mmHg, pulse 120/min. He has sunken eyes and dry lips; abdomen is not distended and non-tender. What is the most likely causative organism?",
                "Vibrio cholerae", ["Shigella", "Nontyphoidal Salmonella", "Enterohemorrhagic E. coli (EHEC)", "Entamoeba histolytica"],
                explain='''ถ่ายเหลวเป็นน้ำปริมาณมาก (12 ครั้ง/วัน) ไม่ปวดท้อง ไม่มีเลือด และขาดน้ำรุนแรงอย่างรวดเร็ว = **cholera**
- *Shigella* ถ่ายมูกเลือด ปวดเบ่ง มีไข้
- Nontyphoidal *Salmonella* มักมีไข้ ปวดท้อง และอาจมีเลือดปน
- EHEC ถ่ายเป็นเลือดมาก เสี่ยง HUS
- *E. histolytica* ถ่ายมูกเลือดแบบ dysentery''',
                pearl="ถ่ายน้ำซาวข้าวมาก ไม่ปวดท้อง ช็อกเร็ว = cholera", topic="Cholera",
                ref=[f"{D} หน้า 71–72"], nl=["2.3.1(7)"], kind="old", src=OLD),
            mcq("GI-03-03-3", "A 25-year-old man has had watery diarrhea 10 times/day for 2 days with vomiting 2–3 times/day and no abdominal pain. Temperature 37 °C, pulse 110/min, BP 90/60 mmHg. Hct 48%, WBC 13,000/mm³ (N 80%), platelets 120,000/mm³. BUN 60 mg/dL, Cr 2 mg/dL, Na 142, K 2.8, HCO3 14, Cl 90 mmol/L. What is the most likely diagnosis?",
                "Cholera", ["Amoebiasis", "Capillariasis", "Salmonellosis", "Cystoisosporiasis"],
                explain='''ถ่ายเป็นน้ำปริมาณมาก ไม่ปวดท้อง ไม่มีไข้ ร่วมกับผลจากการเสียน้ำ/เกลือแร่ทางอุจจาระ: **hemoconcentration (Hct 48%)**, **prerenal AKI (BUN/Cr = 30)**, **hypokalemia** และ **metabolic acidosis จากเสีย HCO3** = cholera
- Amoebiasis ทำให้ dysentery มูกเลือด ปวดเบ่ง
- Capillariasis เป็นพยาธิทำให้ท้องเสียเรื้อรัง protein-losing enteropathy บวม ไม่ใช่เฉียบพลัน 2 วัน
- Salmonellosis มักมีไข้ ปวดท้อง
- Cystoisosporiasis ท้องเสียเรื้อรังในผู้ป่วย HIV''',
                pearl="Cholera labs: Hct สูง, prerenal AKI, ↓K, metabolic acidosis", topic="Cholera complications",
                ref=[f"{D} หน้า 73–74"], nl=["2.3.1(7)", "2.3.4(2)"], kind="old", src=OLD),
            mcq("GI-03-03-4", "A 32-year-old man develops fever, crampy abdominal pain and diarrhea with mucus and blood 2 days after eating undercooked chicken at a barbecue. Stool examination shows numerous RBCs and WBCs. What is the most likely causative pathogen?",
                "Campylobacter jejuni", ["Vibrio cholerae", "Giardia lamblia", "Cryptosporidium spp.", "Norovirus"],
                explain='''Inflammatory (bloody) diarrhea หลังกิน **สัตว์ปีกที่ปรุงไม่สุก** = ***Campylobacter jejuni*** (เชื้อก่อ bacterial diarrhea ที่พบบ่อย สัมพันธ์กับ Guillain-Barré syndrome — เสริม) — สไลด์ใช้โจทย์ "ถ่ายเหลวพุ่งมีมูกเลือด กินอาหารสุก ๆ ดิบ ๆ stool RBC/WBC มาก" และเฉลย Campylobacter
- *V. cholerae*, *Giardia*, *Cryptosporidium* และ norovirus ทำให้ **watery** diarrhea ไม่มี RBC/WBC จำนวนมากในอุจจาระ''',
                pearl="Bloody diarrhea + ไก่ไม่สุก = Campylobacter", topic="Bloody diarrhea pathogen",
                ref=[f"{D} หน้า 66, 75–76"], nl=["2.3.1(7)"]),
            mcq("GI-03-03-5", "A 28-year-old woman has fever 39 °C, tenesmus and frequent small-volume bloody stools for 2 days. She asks for something to stop the diarrhea before a long bus trip. Which medication should be avoided?",
                "Loperamide", ["Oral rehydration solution", "Azithromycin", "Ciprofloxacin", "Bismuth subsalicylate"],
                explain='''ผู้ป่วยมี **inflammatory diarrhea** (ไข้สูง ถ่ายเป็นเลือด ปวดเบ่ง) ห้ามให้ **loperamide** เพราะลด motility ทำให้เชื้อ/toxin ค้างในลำไส้ เสี่ยง **toxic megacolon** และ HUS ใน EHEC (เสริม)
- ORS เป็นพื้นฐานของทุกรายเพื่อทดแทนน้ำ
- Azithromycin และ ciprofloxacin เป็น ATB ที่สไลด์แนะนำ 3 วันใน bloody diarrhea
- Bismuth subsalicylate เป็น antidiarrheal ที่ใช้ได้ตามสไลด์ (ไม่ได้ยับยั้ง motility แบบ opioid)''',
                pearl="Bloody diarrhea/ไข้ → ห้าม loperamide (toxic megacolon)", topic="Loperamide contraindication",
                ref=[f"{D} หน้า 68"], nl=["B8.4(4)", "2.1.18"]),
        ]),

    sec("gi-03-04", "Irritable bowel syndrome (IBS)",
        "ปวดท้องสัมพันธ์กับการถ่าย ≥ 1 วัน/สัปดาห์ใน 3 เดือน + 2 ใน 3 ข้อ (Rome IV) ไม่มี alarm → LSM + ยาตามอาการเด่น", minutes=6,
        source=f"{D} หน้า 77–88", nl=["2.3.11(6)", "B8.2.5(2)"],
        md='''
### ใครเป็น
- Idiopathic (gut-brain axis, visceral hypersensitivity — เสริม)
- **หญิง > ชาย, peak age 20–39 ปี**
- สัมพันธ์กับ psychiatric disorders, fibromyalgia

### อาการ
- **ปวดท้องเรื้อรัง สัมพันธ์กับการถ่ายอุจจาระ** (มักดีขึ้นหลังถ่าย)
- Trigger: **ความเครียด**, มื้ออาหาร
- ท้องเสีย / ท้องผูก / สลับกัน
- **ตรวจร่างกายปกติ**

### Rome IV criteria for IBS
**ปวดท้องเป็นซ้ำ ≥ 1 วัน/สัปดาห์ในช่วง 3 เดือนที่ผ่านมา** ร่วมกับ **≥ 2 ข้อ**
1. ปวดท้องสัมพันธ์กับการถ่ายอุจจาระ
2. ความถี่ของการถ่ายเปลี่ยน
3. ลักษณะอุจจาระเปลี่ยน

และ **เริ่มมีอาการ ≥ 6 เดือน** โดย active ใน 3 เดือนล่าสุด

### การตรวจ
- **Alarm feature → colonoscopy** (เช่น อายุ ≥ 50 ปีเริ่มเป็นใหม่, ถ่ายเป็นเลือด, น้ำหนักลด, อาการตอนกลางคืน, ซีด, FHx มะเร็งลำไส้ใหญ่/IBD — เสริม)
- Fecal calprotectin, CRP เมื่อสงสัย IBD
- Stool culture (เมื่อท้องเสียเด่น)
- ไม่มี alarm → วินิจฉัยจากเกณฑ์ ไม่ต้องส่องทุกราย

### การรักษา
**Lifestyle & dietary modification** (ทุกราย)
- **Low FODMAP diet**
- **High fiber & low fat diet**
- Regular exercise

**Medication ตามอาการเด่น**
- Anti-spasmodics: **Buscopan (hyoscine), dicyclomine** — ปวดเด่น
- Anti-diarrheal: **loperamide, ondansetron** — ท้องเสียเด่น
- Laxatives: **PEG, milk of magnesia (MOM), lactulose** — ท้องผูกเด่น

[[fig:gi-03-04-ibs]]

> ข้อสอบ: หญิงสาว ปวดท้องเรื้อรัง ดีขึ้นหลังถ่าย แย่ลงตอนเครียด/สอบ ท้องผูกสลับท้องเสีย ไม่มี alarm ตรวจปกติ → **IBS** และการรักษาแรกตามเฉลยในสไลด์คือ **high-fiber diet**

| แยกโรค | ต่างจาก IBS อย่างไร |
|---|---|
| Functional dyspepsia | ปวดลิ้นปี่ **ไม่สัมพันธ์กับการถ่าย** |
| Functional diarrhea | ถ่ายเหลว **ไม่มีอาการปวดท้อง** เด่น |
| IBD | มีเลือด, ไข้, น้ำหนักลด, calprotectin สูง |
''',
        figs=[fig("gi-03-04-ibs", "การรักษา IBS ตามอาการเด่น", IBS,
                  "ทุกรายเริ่มด้วยการอธิบายโรคและปรับอาหาร แล้วเลือกยาตามอาการเด่น ถ้าไม่ตอบสนองจึงใช้ TCA ขนาดต่ำ (ดัดแปลงจากแผนภาพในสไลด์หน้า 82)")],
        pearls=[
            "Rome IV: ปวด ≥ 1 วัน/wk ใน 3 เดือน + ≥ 2 ใน 3 (สัมพันธ์กับถ่าย, ความถี่เปลี่ยน, ลักษณะเปลี่ยน), onset ≥ 6 เดือน",
            "IBS ตรวจร่างกายปกติ; มี alarm → colonoscopy",
            "สงสัย IBD → fecal calprotectin, CRP",
            "IBS-C → fiber/PEG; IBS-D → loperamide; ปวดเด่น → antispasmodic; ดื้อยา → TCA",
        ],
        items=[
            mcq("GI-03-04-1", "A 20-year-old woman has had intermittent abdominal pain for as long as she can remember. The pain improves after defecation or when she relaxes, and is worse now because she is stressed about final examinations. Physical examination and colonoscopy are normal. What is the most likely diagnosis?",
                "Irritable bowel syndrome", ["Inflammatory bowel disease", "Functional dyspepsia", "Lactose intolerance", "Somatic symptom disorder"],
                explain='''ปวดท้องเรื้อรังที่ **ดีขึ้นหลังถ่ายอุจจาระ** กำเริบเมื่อ **เครียด** หญิงอายุน้อย ตรวจร่างกายและ colonoscopy ปกติ = **IBS**
- IBD จะพบรอยโรคใน colonoscopy และมีเลือด/น้ำหนักลด
- Functional dyspepsia ปวดลิ้นปี่ ไม่สัมพันธ์กับการถ่าย
- Lactose intolerance สัมพันธ์กับการดื่มนม ท้องอืดท้องเสีย
- Somatic symptom disorder เป็นการวินิจฉัยทางจิตเวชที่ต้องมีความคิด/พฤติกรรมกังวลเกินเหตุต่ออาการ ไม่ใช่คำอธิบายที่ดีที่สุดเมื่อเข้า Rome IV''',
                pearl="ปวดท้องดีขึ้นหลังถ่าย + เครียดกำเริบ + ตรวจปกติ = IBS", topic="IBS diagnosis",
                ref=[f"{D} หน้า 83–84"], nl=["2.3.11(6)"], kind="old", src=OLD),
            mcq("GI-03-04-2", "A 35-year-old woman has had abdominal pain, burping, bloating and loose stools for 2 years, starting after she changed workplaces. She has no weight loss or other red-flag signs. Physical examination and EGD are normal. What is the most likely diagnosis?",
                "Irritable bowel syndrome", ["Functional dyspepsia", "Functional diarrhea", "Inflammatory bowel disease", "Somatic symptom disorder"],
                explain='''ปวดท้องร่วมกับ **การเปลี่ยนแปลงของอุจจาระ (ถ่ายเหลว)** เรื้อรัง 2 ปี สัมพันธ์กับความเครียด ไม่มี red flag = **IBS**
- Functional dyspepsia เด่นอาการลิ้นปี่/อิ่มเร็ว ไม่มีการเปลี่ยนแปลงของอุจจาระ — EGD ปกติไม่ได้ทำให้เป็น functional dyspepsia เสมอไป
- Functional diarrhea คือถ่ายเหลวเรื้อรัง **โดยไม่มีปวดท้องเด่น**
- IBD จะมีเลือด น้ำหนักลด หรือ inflammatory markers สูง
- Somatic symptom disorder ไม่ใช่คำตอบที่ดีที่สุดเมื่อเข้าเกณฑ์ IBS''',
                pearl="ปวดท้อง + อุจจาระเปลี่ยน = IBS; ถ่ายเหลวไม่ปวด = functional diarrhea", topic="IBS vs functional disorders",
                ref=[f"{D} หน้า 85–86"], nl=["2.3.11(6)", "B8.2.5(2)"], kind="old", src=OLD),
            mcq("GI-03-04-3", "A 26-year-old woman has intermittent lower abdominal pain for 4 months with alternating constipation and diarrhea. She has no bloody stool, no nocturnal symptoms and no family history of colorectal cancer. Physical examination is normal. What is the most appropriate initial management?",
                "High-fiber diet", ["Prokinetic agent", "Colonoscopy", "Stool occult blood", "Long-term loperamide"],
                explain='''หญิงอายุน้อยเข้าได้กับ IBS (mixed type) **ไม่มี alarm feature** จึงไม่ต้องส่องกล้อง เริ่มด้วย **lifestyle & dietary modification** — เฉลยในสไลด์คือ **high-fiber diet**
- Prokinetic ไม่ใช่ยาหลักของ IBS
- Colonoscopy ทำเมื่อมี alarm feature เท่านั้น
- Stool occult blood ไม่ช่วยและไม่ใช่ screening ในคนอายุ 26 ไม่มีความเสี่ยง
- Loperamide ระยะยาวใช้เฉพาะ IBS-D และจะทำให้ช่วงท้องผูกแย่ลง
> สไลด์เฉลย high fibre diet; บางแหล่งเลือก antispasmodic สำหรับอาการปวด — ข้อสอบตามสไลด์ให้เริ่มที่อาหาร''',
                pearl="IBS ไม่มี alarm → เริ่ม diet (high fiber/low FODMAP) ไม่ต้องส่อง", topic="IBS initial management",
                ref=[f"{D} หน้า 81, 87–88"], nl=["2.3.11(6)"], kind="old", src=OLD),
            mcq("GI-03-04-4", "A 55-year-old man has had alternating diarrhea and constipation with crampy lower abdominal pain for 3 months. He has lost 5 kg and noticed dark blood mixed with stool twice. Hb is 10.2 g/dL with microcytosis. What is the most appropriate next step?",
                "Colonoscopy", ["Diagnose IBS and start a low-FODMAP diet", "Start an antispasmodic and review in 3 months", "Low-dose amitriptyline", "Reassurance and stress management"],
                explain='''อาการคล้าย IBS แต่มี **alarm features** หลายข้อ: อายุ > 50 เริ่มเป็นใหม่, **น้ำหนักลด, ถ่ายมีเลือด, iron deficiency anemia** → ต้อง **colonoscopy** เพื่อ R/O colorectal cancer/IBD ก่อนวินิจฉัย IBS
- การวินิจฉัย IBS และให้ low FODMAP, antispasmodic, amitriptyline หรือ reassurance ทำได้เมื่อไม่มี alarm เท่านั้น การให้ยาก่อนจะทำให้วินิจฉัยมะเร็งช้า''',
                pearl="IBS-like + alarm (อายุมาก, เลือด, wt loss, IDA) → colonoscopy", topic="IBS alarm features",
                ref=[f"{D} หน้า 79–80"], nl=["2.3.11(6)", "2.3.11-3(2)"]),
        ]),
    ])
