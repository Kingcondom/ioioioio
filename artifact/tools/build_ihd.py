#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ischemic heart diseases (24 ก.ย. · อ.สุรพันธ์ พงศ์สุธนะ · Active learning) → data/cardio.json"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
NL = ["2.3.9-3(1)"]
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes,
              "nl": nl or NL, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NL}

sec("cardio-ihd-01", "CAD เป็นโรคเรื้อรังที่วนเข้าออกหลายระยะ",
    "atherosclerosis timeline · สี่ระยะทางคลินิก · การแตกของ plaque", 8,
"""สไลด์เปิดด้วยแนวคิดที่ใช้เป็นโครงทั้งคาบ — **Coronary artery disease เป็นโรคเรื้อรัง (a chronic disorder)** ที่ **วนเข้าออกระหว่างระยะต่าง ๆ ตลอดชีวิต** ไม่ใช่เหตุการณ์ครั้งเดียว

| ระยะทางคลินิก | ลักษณะ |
|---|---|
| **Asymptomatic** | มีคราบไขมันแล้วแต่ยังไม่มีอาการ |
| **Stable angina** | เจ็บหน้าอกเวลาออกแรง คงที่ ทำนายได้ |
| **Progressive angina** | เจ็บถี่ขึ้น นานขึ้น หรือเกิดที่ระดับกิจกรรมต่ำลง |
| **Acute coronary syndrome** | **unstable angina · NSTEMI · STEMI** |

### Atherosclerosis timeline
สไลด์ไล่ลำดับการเกิดรอยโรคไว้ตามช่วงอายุ

**Endothelial dysfunction → Fatty streak → Foam cells → Intermediate lesion → Atheroma → Fibrous plaque → Complicated lesion / Rupture**

- เริ่มตั้งแต่ **ทศวรรษแรกของชีวิต** (endothelial dysfunction, fatty streak)
- **ทศวรรษที่สาม** — atheroma และ intermediate lesion
- **ทศวรรษที่สี่เป็นต้นไป** — fibrous plaque และ **complicated lesion / rupture**

### จุดเปลี่ยนที่สำคัญที่สุด — plaque rupture
> คราบที่ **ตีบมากที่สุด ไม่ใช่คราบที่อันตรายที่สุดเสมอไป** — คราบที่มี **ไขมันมาก ผนังบาง และมีการอักเสบสูง (vulnerable plaque)** อาจตีบไม่มากแต่ **แตกง่าย** เมื่อแตกแล้วเกิดลิ่มเลือดอุดทันที กลายเป็น **ACS**
>
> นี่คือเหตุผลที่ **ผู้ป่วยจำนวนมากเกิด MI โดยไม่เคยมีอาการ angina มาก่อน** และเป็นเหตุผลที่การรักษาด้วยยา (statin, antiplatelet) มีความสำคัญไม่แพ้การขยายหลอดเลือด

### ความต่างเชิงกลไกที่กำหนดการรักษา

| | **Chronic coronary syndrome** | **Acute coronary syndrome** |
|---|---|---|
| กลไก | **ตีบแบบคงที่ → เลือดไม่พอเมื่อต้องการมากขึ้น** | **plaque แตก → ลิ่มเลือดอุดเฉียบพลัน** |
| อาการ | เจ็บเวลาออกแรง พักแล้วหาย | **เจ็บขณะพัก นานกว่า 20 นาที** |
| เป้าหมายการรักษา | ลดอาการ + ป้องกันเหตุการณ์ในอนาคต | **เปิดหลอดเลือดให้เร็วที่สุด** |
""",
    ["CAD เป็นโรคเรื้อรังที่วนเข้าออกสี่ระยะ ไม่ใช่เหตุการณ์ครั้งเดียว",
     "คราบที่ตีบมากที่สุดไม่ใช่คราบที่อันตรายที่สุด — vulnerable plaque ตีบน้อยแต่แตกง่าย",
     "CCS = ตีบคงที่ ขาดเลือดเมื่อออกแรง · ACS = plaque แตก ลิ่มเลือดอุดเฉียบพลัน",
     "ผู้ป่วยจำนวนมากเกิด MI โดยไม่เคยมี angina มาก่อน"],
    [
    mcq("CAR-IHD-MCQ-01",
        "A 54-year-old man with no prior cardiac symptoms suddenly develops crushing chest pain at rest. Angiography during the event shows an occluded vessel at a site that had only 40% stenosis on a CT angiogram performed two years earlier. Which mechanism best explains this?",
        ["Progressive narrowing of a fixed stenosis to complete occlusion",
         "Rupture of a lipid-rich, thin-capped plaque with superimposed thrombosis",
         "Coronary vasospasm without any underlying plaque",
         "Embolisation from a left atrial thrombus",
         "Increased myocardial oxygen demand alone"],
        1,
        """**Plaque rupture ตามด้วยลิ่มเลือด คือกลไกของ ACS ส่วนใหญ่**

สไลด์วาง atherosclerosis timeline ไว้จบที่ **complicated lesion / rupture** และแยกกลไกของ CCS ออกจาก ACS อย่างชัดเจน

**ทำไมรอยโรคที่ตีบเพียง 40% จึงอุดตันสนิทได้**

| | **Stable plaque** | **Vulnerable plaque** |
|---|---|---|
| ผนังเส้นใย | **หนา** | **บาง (thin cap)** |
| แกนไขมัน | เล็ก | **ใหญ่ ไขมันมาก** |
| การอักเสบ | น้อย | **มาก มี macrophage แทรก** |
| ระดับการตีบ | มักมาก | **มักน้อยถึงปานกลาง** |
| ผลลัพธ์ | **stable angina** | **แตกแล้วเกิด ACS ทันที** |

**นัยทางคลินิกที่สำคัญที่สุด** — เพราะรอยโรคที่จะแตกมักตีบไม่มาก **การขยายหลอดเลือดเฉพาะจุดที่ตีบมากจึงไม่ได้ป้องกัน MI ในอนาคต** การรักษาที่ลดเหตุการณ์ได้คือ **statin, antiplatelet, การคุมความดันและเบาหวาน และการเลิกบุหรี่** ซึ่งทำให้คราบทั้งระบบเสถียรขึ้น

**ทำไมข้ออื่นผิด** — การตีบแบบค่อยเป็นค่อยไปมักทำให้เกิด **หลอดเลือดข้างเคียง (collateral)** และอาการ angina ที่แย่ลงทีละน้อย ไม่ใช่อุดตันฉับพลัน · **vasospasm ล้วน ๆ** พบได้แต่น้อยกว่ามาก · **ลิ่มเลือดจากหัวใจห้องบนซ้าย** ทำให้เกิด stroke มากกว่า MI และต้องมี AF · **ความต้องการออกซิเจนที่เพิ่มขึ้นอย่างเดียว** ทำให้เกิด type 2 MI ซึ่งต้องมีตัวกระตุ้น เช่น ซีดรุนแรง ติดเชื้อ หรือหัวใจเต้นเร็วมาก""",
        "รอยโรคตีบน้อยก็ทำให้เกิด MI ได้ — จึงต้องรักษาทั้งระบบด้วยยา ไม่ใช่แค่ขยายจุดที่ตีบมาก",
        "Plaque rupture",
        ["สไลด์ อ.สุรพันธ์ — CAD / Atherosclerosis Timeline", "ESC 2019 Chronic Coronary Syndromes"]),
    ])

sec("cardio-ihd-02", "Chronic coronary syndrome — step approach และ pretest probability",
    "หกขั้นของ ESC 2019 · การประเมินความน่าจะเป็นก่อนตรวจ", 10,
"""ESC 2019 เปลี่ยนชื่อจาก *stable CAD* เป็น **chronic coronary syndrome (CCS)** เพื่อเน้นว่าโรคดำเนินต่อเนื่องตลอด และวาง **step approach** ไว้เป็นลำดับ

| ขั้น | สิ่งที่ทำ |
|---|---|
| **1** | **ประเมินอาการและสัญญาณชีพ** — เป็น angina แบบใด |
| **2** | **ประเมินโรคร่วม คุณภาพชีวิต และสุขภาพโดยรวม** — ถ้าการเปิดหลอดเลือดไม่ใช่ทางเลือกที่ยอมรับได้ตั้งแต่ต้น ก็ไม่ต้องไล่ตรวจต่อ |
| **3** | **Basic testing** — resting ECG, เลือด, echocardiography, chest X-ray |
| **4** | **ประเมิน pretest probability (PTP) และความน่าจะเป็นทางคลินิก** |
| **5** | **เลือกการตรวจวินิจฉัย** ตาม PTP |
| **6** | **ประเมินความเสี่ยงของเหตุการณ์ (event risk)** เพื่อวางแผนการรักษา |

### การแบ่งชนิดของอาการเจ็บหน้าอก

| ชนิด | เกณฑ์ |
|---|---|
| **Typical angina** | ครบ 3 ข้อ — **เจ็บแน่นกลางอกหรือใต้กระดูกอก** · **ถูกกระตุ้นด้วยการออกแรงหรืออารมณ์** · **หายเมื่อพักหรืออมยาไนเตรตภายในไม่กี่นาที** |
| **Atypical angina** | ครบ 2 ข้อ |
| **Non-anginal** | ครบ 0–1 ข้อ |

> **ขั้นที่ 2 คือขั้นที่คนมองข้ามมากที่สุด** — สไลด์ระบุว่าถ้าผู้ป่วยมีอาการที่ **ไม่ใช่ angina อย่างชัดเจน** หรือ **สภาพโดยรวมทำให้การเปิดหลอดเลือดไม่ใช่ทางเลือก** ก็ **ไม่ควรไล่ตรวจไปเรื่อย ๆ** เพราะผลตรวจจะไม่เปลี่ยนการรักษา

### Basic testing ที่ต้องทำทุกราย
- **Resting ECG** — ปกติได้ในผู้ป่วย CCS จำนวนมาก **ECG ปกติไม่ตัดโรคออก** · มองหา Q wave เก่า, ST-T เปลี่ยนแปลง, LVH, AF
- **Ambulatory ECG** — มีที่ใช้เมื่อสงสัย **arrhythmia** หรือ **vasospastic angina**
- **Chest X-ray** — ใช้เมื่อสงสัยหัวใจล้มเหลวหรือโรคปอด ไม่ได้ใช้วินิจฉัย CAD
- **Echocardiography** — ประเมินการบีบตัว ความผิดปกติของการเคลื่อนไหวผนัง และตัดสาเหตุอื่น เช่น ลิ้นหัวใจตีบ

### Pretest probability — ทำไมสำคัญ
PTP คำนวณจาก **อายุ เพศ และลักษณะของอาการเจ็บหน้าอก**

- **PTP ต่ำมาก** → การตรวจเพิ่มให้ผล **บวกลวง** มากกว่าประโยชน์
- **PTP สูงมาก** → ผลลบก็ยังไม่ตัดโรค ควรไป **ตรวจสวนหลอดเลือดหัวใจ** เลยในรายที่มีอาการมาก
- **PTP ปานกลาง** → เป็นกลุ่มที่ **ได้ประโยชน์สูงสุดจากการตรวจแบบไม่รุกล้ำ**

**การตรวจที่เลือกได้** — **CCTA** (ดีเมื่อ PTP ต่ำถึงปานกลาง เพราะ negative predictive value สูงมาก) หรือ **functional imaging** เช่น stress echo, SPECT, stress CMR (ดีเมื่อ PTP สูงขึ้นหรือมีรอยโรคแล้วอยากรู้ว่าขาดเลือดจริงไหม)

> **Exercise ECG เพียงอย่างเดียวมีบทบาทลดลงมากใน ESC 2019** เพราะความไวและความจำเพาะต่ำกว่าการตรวจที่มีภาพ แต่ยังมีประโยชน์ในการ **ประเมินความสามารถในการออกกำลัง อาการ การตอบสนองของความดัน และการเต้นผิดจังหวะ**
""",
    ["Typical angina = ครบ 3 ข้อ · atypical = 2 ข้อ · non-anginal = 0–1 ข้อ",
     "ขั้นที่ 2 ของ ESC: ถ้าเปิดหลอดเลือดไม่ใช่ทางเลือก ก็ไม่ต้องไล่ตรวจต่อ",
     "Resting ECG ปกติไม่ตัด CCS ออก",
     "PTP ต่ำ → ตรวจแล้วบวกลวงเยอะ · PTP ปานกลาง → ได้ประโยชน์สูงสุดจากการตรวจแบบไม่รุกล้ำ",
     "Exercise ECG อย่างเดียวมีบทบาทลดลง แต่ยังบอกสมรรถภาพและการตอบสนองของความดันได้"],
    [
    mcq("CAR-IHD-MCQ-02",
        "A 38-year-old woman describes sharp left-sided chest pain lasting seconds, unrelated to exertion and reproducible by pressing on the chest wall. Resting ECG and echocardiography are normal. According to the ESC stepwise approach, what is the most appropriate next step?",
        ["Proceed directly to invasive coronary angiography",
         "Conclude the pain is non-anginal with very low pretest probability and avoid further ischaemia testing",
         "Order a stress myocardial perfusion scan to be safe",
         "Start dual antiplatelet therapy empirically",
         "Order CT coronary angiography in all such patients"],
        1,
        """**เจ็บแหลม เป็นวินาที ไม่สัมพันธ์กับการออกแรง และกดเจ็บที่ผนังทรวงอก = non-anginal chest pain** เมื่อรวมกับ **อายุน้อยและเพศหญิง** ทำให้ **pretest probability ต่ำมาก**

สไลด์ระบุไว้ในขั้นที่ 2 ของ step approach ว่า **"Clear non-anginal"** เป็นเหตุผลให้ **ไม่ไล่ตรวจต่อ** ร่วมกับการประเมินสุขภาพโดยรวม โรคร่วม และคุณภาพชีวิต

**เหตุผลเชิงสถิติที่ต้องเข้าใจ** — เมื่อ **ความชุกของโรคในกลุ่มที่ตรวจต่ำมาก** แม้การตรวจจะมีความจำเพาะดี **ค่าพยากรณ์ผลบวก (PPV) ก็ยังต่ำ** ผลบวกส่วนใหญ่จึงเป็น **บวกลวง** ซึ่งนำไปสู่
- การตรวจเพิ่มที่รุกล้ำโดยไม่จำเป็น
- ความเสี่ยงจากรังสีและสารทึบรังสี
- ความวิตกกังวลและการติดฉลากว่าเป็นโรคหัวใจ

**สิ่งที่ควรทำแทน** — หาสาเหตุอื่นของอาการ (**musculoskeletal, GERD, ความวิตกกังวล**) และ **ประเมินปัจจัยเสี่ยงหลอดเลือดหัวใจเพื่อป้องกันระยะยาว**

**ทำไมข้ออื่นผิด** — การสวนหลอดเลือดในผู้ป่วย PTP ต่ำมากมีความเสี่ยงโดยไม่มีประโยชน์ · **stress test และ CCTA ในทุกราย** ขัดกับหลัก PTP โดยตรง · **DAPT** ไม่มีข้อบ่งชี้เลยเมื่อยังไม่มีหลักฐานว่าเป็นโรค""",
        "PTP ต่ำมาก อย่าตรวจ — ผลบวกส่วนใหญ่จะเป็นบวกลวงและพาไปสู่การตรวจที่รุกล้ำโดยเปล่าประโยชน์",
        "Pretest probability",
        ["สไลด์ อ.สุรพันธ์ — ESC 2019 CCS step approach", "ESC 2019 Guidelines on Chronic Coronary Syndromes"]),
    mcq("CAR-IHD-MCQ-03",
        "Which combination defines TYPICAL angina?",
        ["Sharp pain, worse on inspiration, relieved by leaning forward",
         "Substernal discomfort, provoked by exertion or emotional stress, relieved by rest or nitrates within minutes",
         "Burning epigastric pain after meals relieved by antacids",
         "Pain reproducible by chest wall palpation lasting seconds",
         "Pain radiating to the back, maximal at onset, with unequal pulses"],
        1,
        """**Typical angina ต้องครบทั้งสามข้อ**
1. **เจ็บแน่นบริเวณกลางอกหรือใต้กระดูกอก** (อาจร้าวไปคอ กราม ไหล่ แขน)
2. **ถูกกระตุ้นด้วยการออกแรงหรือความเครียดทางอารมณ์**
3. **หายเมื่อพักหรืออมยาไนเตรตภายในไม่กี่นาที**

| ครบกี่ข้อ | จัดเป็น |
|---|---|
| **3 ข้อ** | **Typical angina** |
| **2 ข้อ** | **Atypical angina** |
| **0–1 ข้อ** | **Non-anginal** |

ชนิดของอาการเป็น **หนึ่งในสามตัวแปรของ pretest probability** ร่วมกับ **อายุและเพศ** จึงมีผลโดยตรงต่อการตัดสินใจว่าจะตรวจอะไรต่อ

**ตัวเลือกอื่นคือกลุ่มอาการที่ต้องแยก**

| อาการ | คิดถึง |
|---|---|
| เจ็บแหลม แย่ลงเมื่อหายใจเข้า ดีขึ้นเมื่อโน้มตัวไปข้างหน้า | **Pericarditis** |
| แสบร้อนลิ้นปี่หลังอาหาร ดีขึ้นด้วยยาลดกรด | **GERD** |
| กดเจ็บผนังทรวงอก เป็นวินาที | **Musculoskeletal** |
| ร้าวไปหลัง ปวดมากที่สุดทันทีที่เริ่ม ชีพจรสองข้างไม่เท่ากัน | **Aortic dissection** |""",
        "สามข้อของ typical angina: ตำแหน่ง · ถูกกระตุ้นด้วยการออกแรง · หายเมื่อพักหรือไนเตรต",
        "Angina classification",
        ["สไลด์ อ.สุรพันธ์ — ESC 2019 CCS Angina", "ESC 2019 CCS"]),
    ])

sec("cardio-ihd-03", "CCS — การรักษาด้วยยาและการป้องกันเหตุการณ์",
    "แยกยาลดอาการออกจากยาที่ลดการตาย", 10,
"""หัวใจของการรักษา CCS คือการ **แยกสองเป้าหมายออกจากกัน**

| เป้าหมาย | ยา |
|---|---|
| **ลดอาการ (anti-ischemic)** | beta-blocker, calcium channel blocker, ไนเตรต, ivabradine, ranolazine, trimetazidine, nicorandil |
| **ลดเหตุการณ์และการตาย (event prevention)** | **antiplatelet · statin · ACEI/ARB ในกลุ่มที่มีข้อบ่งชี้** |

> **ยาลดอาการไม่ได้ลดการตาย และยาที่ลดการตายบางตัวไม่ได้ลดอาการ** — ผู้ป่วยที่ไม่มีอาการแล้วยังต้องกิน statin และ aspirin ต่อ เป็นประเด็นที่ต้องอธิบายให้ผู้ป่วยเข้าใจ ไม่งั้นจะหยุดยาเอง

### Anti-ischemic drug — ลำดับตาม ESC 2019
- **ยาตัวแรก** — **beta-blocker และ/หรือ calcium channel blocker** เลือกตามอัตราการเต้นหัวใจ ความดัน และโรคร่วม
- **ไนเตรตออกฤทธิ์สั้น** — ให้ทุกรายเพื่อบรรเทาอาการเฉียบพลัน
- **ขั้นถัดไป** — เพิ่มไนเตรตออกฤทธิ์ยาว, ivabradine, ranolazine, trimetazidine หรือ nicorandil ตามโปรไฟล์ผู้ป่วย

**การเลือกตามสถานการณ์**

| สถานการณ์ | เลือก |
|---|---|
| **หัวใจเต้นเร็ว** | beta-blocker หรือ non-dihydropyridine CCB (verapamil, diltiazem) |
| **หัวใจเต้นช้า** | **หลีกเลี่ยง beta-blocker และ non-DHP CCB** → ใช้ dihydropyridine CCB หรือไนเตรต |
| **หัวใจล้มเหลว (HFrEF)** | **beta-blocker** เป็นตัวหลัก **ห้ามใช้ verapamil และ diltiazem** |
| **สงสัย vasospastic angina** | **CCB และไนเตรต — หลีกเลี่ยง beta-blocker** |

### Event prevention
- **Antiplatelet** — **aspirin 75–100 mg/วัน** เป็นมาตรฐาน · ใช้ **clopidogrel** เมื่อแพ้หรือทนแอสไพรินไม่ได้
- **Statin** — ให้ทุกรายโดยไม่ขึ้นกับระดับไขมันเริ่มต้น
- **ACEI/ARB** — เมื่อมี **หัวใจล้มเหลว เบาหวาน ความดันโลหิตสูง หรือโรคไตเรื้อรัง** ร่วมด้วย
- **Double antiplatelet (เพิ่มยาตัวที่สองบน aspirin)** — พิจารณาใน **ผู้ที่เสี่ยงเหตุการณ์ขาดเลือดสูงและเสี่ยงเลือดออกไม่สูง**

### Lifestyle modification — สไลด์ให้น้ำหนักเท่ากับยา
- **เลิกบุหรี่** — มาตรการที่คุ้มค่าที่สุด
- **อาหารเพื่อสุขภาพ** แบบเมดิเตอร์เรเนียน
- ออกกำลังกาย คุมน้ำหนัก คุมความดันและเบาหวาน

### สองรูปแบบพิเศษที่ต้องรู้จัก
- **Microvascular angina** — มีอาการและหลักฐานขาดเลือด **แต่หลอดเลือดหัวใจใหญ่ไม่ตีบ**
- **Vasospastic angina** — เจ็บ **ขณะพัก โดยเฉพาะกลางดึกถึงเช้ามืด** ECG ขณะเจ็บพบ **ST ยกชั่วคราว** ตอบสนองดีต่อ **CCB และไนเตรต** และ **beta-blocker ทำให้แย่ลง**
""",
    ["แยกให้ชัด: ยาลดอาการ vs ยาที่ลดการตาย — ผู้ป่วยไม่มีอาการก็ยังต้องกิน statin และ aspirin",
     "HFrEF ห้ามใช้ verapamil และ diltiazem",
     "Vasospastic angina ให้ CCB และไนเตรต หลีกเลี่ยง beta-blocker",
     "Microvascular angina = มีอาการขาดเลือดแต่หลอดเลือดใหญ่ไม่ตีบ"],
    [
    mcq("CAR-IHD-MCQ-04",
        "A 60-year-old man with chronic coronary syndrome has been symptom-free for a year on aspirin, atorvastatin and bisoprolol. He asks to stop all medication because he feels well. Which explanation is most accurate?",
        ["He may stop all three because absence of symptoms indicates cure",
         "Aspirin and statin reduce future events and death independently of symptoms, so they should continue",
         "Only the beta-blocker prevents death and must be continued",
         "Statins may be stopped once LDL is normal",
         "Aspirin may be stopped because he has no stent"],
        1,
        """**ต้องแยกยาสองกลุ่มให้ชัด** ตามที่สไลด์แบ่งไว้เป็น **anti-ischemic drug** กับ **event prevention**

| กลุ่ม | ยา | ทำอะไร |
|---|---|---|
| **ลดอาการ** | **beta-blocker**, CCB, ไนเตรต, ivabradine, ranolazine | บรรเทา angina — **ไม่ได้ลดการตายใน CCS** |
| **ลดเหตุการณ์และการตาย** | **antiplatelet · statin · ACEI/ARB (เมื่อมีข้อบ่งชี้)** | **ลด MI และการตาย ไม่ว่าจะมีอาการหรือไม่** |

**การไม่มีอาการไม่ได้แปลว่าโรคหาย** — สไลด์ย้ำตั้งแต่ต้นว่า CAD เป็น **โรคเรื้อรังที่วนเข้าออกหลายระยะ** และ **คราบที่จะแตกมักตีบไม่มาก** ผู้ป่วยที่สบายดีจึงยังมีความเสี่ยงต่อ ACS อยู่

**ประเด็นเรื่อง statin** — ให้ต่อแม้ LDL ถึงเป้า เพราะ
- ประโยชน์มาจากการ **ทำให้คราบเสถียรและลดการอักเสบ** ไม่ใช่แค่ตัวเลข LDL
- **หยุดยาแล้ว LDL จะกลับขึ้นและความเสี่ยงกลับมา**

**beta-blocker** ในผู้ป่วยรายนี้ใช้ **ลดอาการ** เป็นหลัก จึงเป็นตัวเดียวที่อาจพิจารณาปรับหรือลดได้หากไม่มีข้อบ่งชี้อื่น (เช่น หัวใจล้มเหลว หรือเพิ่งเกิด MI) — แต่ต้องปรึกษาแพทย์ ไม่ใช่หยุดเอง""",
        "ไม่มีอาการ ≠ หายจากโรค — statin และ antiplatelet ป้องกันเหตุการณ์ในอนาคต ต้องกินต่อ",
        "CCS medical therapy",
        ["สไลด์ อ.สุรพันธ์ — ESC 2019 CCS Anti-ischemic drug / Event prevention"]),
    mcq("CAR-IHD-MCQ-05",
        "A 46-year-old smoker has recurrent chest pain at rest between 2 and 5 a.m. ECG during an episode shows transient ST elevation that resolves completely with sublingual nitrate. Coronary angiography shows no significant fixed stenosis. Which treatment should be AVOIDED?",
        ["Calcium channel blocker", "Long-acting nitrate", "Smoking cessation advice", "Beta-blocker", "Statin"],
        3,
        """**Vasospastic (Prinzmetal) angina** — เจ็บขณะพักโดยเฉพาะ **กลางดึกถึงเช้ามืด**, **ST ยกชั่วคราวขณะเจ็บแล้วหายสนิท**, หลอดเลือดไม่ตีบถาวร

สไลด์ระบุไว้ในหัวข้อของ ESC 2019 CCS ว่า *"In patients with suspected/confirmed vasospastic angina, **calcium channel blockers and nitrates should be considered and beta-blockers avoided**"*

**เหตุผลเชิงกลไก** — beta-blocker ปิดตัวรับ **β2** ที่ทำหน้าที่ขยายหลอดเลือด ทำให้ฤทธิ์ของ **α-adrenergic ที่หดหลอดเลือดเด่นขึ้น** → **การหดเกร็งรุนแรงขึ้น** โดยเฉพาะ non-selective beta-blocker

**การรักษาที่ถูกต้อง**
- **Calcium channel blocker เป็นยาหลัก** (diltiazem, verapamil หรือ amlodipine) ขนาดสูงพอ
- **ไนเตรตออกฤทธิ์ยาว** เสริม และไนเตรตอมใต้ลิ้นสำหรับอาการเฉียบพลัน
- **เลิกบุหรี่เป็นสิ่งสำคัญที่สุด** — บุหรี่เป็นตัวกระตุ้นการหดเกร็งที่แรงที่สุด
- **Statin** ให้ได้และมีประโยชน์
- หลีกเลี่ยง **ยาที่กระตุ้นการหดเกร็ง** เช่น triptan, ergot, โคเคน และยาแก้หวัดที่มี pseudoephedrine

**ทำไมข้ออื่นถูกต้องหมด** — CCB, ไนเตรต, การเลิกบุหรี่ และ statin ล้วนเป็นการรักษาที่เหมาะสมในภาวะนี้""",
        "ST ยกชั่วคราวตอนกลางดึกแล้วหายสนิท + หลอดเลือดไม่ตีบ = vasospastic angina → ห้าม beta-blocker",
        "Vasospastic angina",
        ["สไลด์ อ.สุรพันธ์ — ESC 2019 CCS Vasospastic angina / Anti-ischemic in acute phase"]),
    ])

sec("cardio-ihd-04", "ACS — นิยามและการแบ่งสามกลุ่ม",
    "universal definition ของ MI · unstable angina สามรูปแบบ", 8,
"""### นิยามของ acute MI
สไลด์ยกนิยามไว้ตรง ๆ ว่า **AMI ใช้เมื่อมีหลักฐานของ myocardial injury**
- **มีค่า cardiac troponin สูงกว่า 99th percentile upper reference limit อย่างน้อยหนึ่งค่า**
- **ร่วมกับบริบททางคลินิกที่เข้าได้กับภาวะกล้ามเนื้อหัวใจขาดเลือด**

> จุดสำคัญ — **troponin สูงอย่างเดียวไม่ใช่ MI** เพราะ troponin สูงได้ในหลายภาวะ (ไตวาย, หัวใจล้มเหลว, pulmonary embolism, sepsis, myocarditis) **ต้องมีหลักฐานว่าเป็นการขาดเลือดด้วย**

### หลักฐานสนับสนุนที่ใช้ได้ (ข้อใดข้อหนึ่ง)
1. **อาการของ myocardial ischaemia**
2. **การเปลี่ยนแปลงของ ECG ที่เข้าได้กับการขาดเลือด**
3. **เกิด pathological Q wave**
4. **ภาพแสดงการสูญเสียกล้ามเนื้อหัวใจที่มีชีวิตใหม่ หรือความผิดปกติของการเคลื่อนไหวผนังใหม่**
5. **พบลิ่มเลือดในหลอดเลือดหัวใจจากการสวนหรือการชันสูตร**

### การแบ่ง ACS

**Acute coronary syndrome**
- **STEMI** — ST ยกตามเกณฑ์ → **ต้องเปิดหลอดเลือดทันที**
- **NSTE-ACS**
  - **NSTEMI** — troponin ขึ้น
  - **Unstable angina** — **troponin ไม่ขึ้น**

> ในยุคของ **high-sensitivity troponin** สัดส่วนของ **unstable angina ลดลงมาก** เพราะผู้ป่วยที่เดิมเรียก UA จำนวนมากตรวจพบ troponin ขึ้นเล็กน้อยและถูกจัดเป็น NSTEMI

### Unstable angina — สามรูปแบบที่ต้องจำ
สไลด์ยกตารางมาไว้ชัดเจน

| รูปแบบ | นิยาม |
|---|---|
| **Rest angina** | **เจ็บขณะพัก มักนานเกิน 20 นาที เกิดภายใน 1 สัปดาห์ก่อนมาพบแพทย์** |
| **New onset angina** | **angina ที่รุนแรงระดับ CCS class III ขึ้นไป โดยเพิ่งเริ่มภายใน 2 เดือน** |
| **Increasing angina** | **angina เดิมที่ถี่ขึ้น นานขึ้น หรือเกิดที่ระดับกิจกรรมต่ำลง — เพิ่มขึ้นอย่างน้อย 1 CCS class ภายใน 2 เดือน จนถึงระดับ CCS III** |

### MINOCA
**Myocardial infarction with non-obstructive coronary arteries** — เข้าเกณฑ์ AMI ทุกข้อ **แต่การสวนหลอดเลือดไม่พบการตีบที่มีนัยสำคัญ** ต้องทบทวนภาพการสวนซ้ำเพื่อยืนยันว่าไม่มีการอุดกั้นจริง แล้วหาสาเหตุอื่น เช่น **plaque erosion, การหดเกร็ง, spontaneous coronary artery dissection (SCAD), myocarditis, embolism**
""",
    ["Troponin สูงอย่างเดียวไม่ใช่ MI — ต้องมีบริบทของการขาดเลือดร่วมด้วย",
     "Unstable angina สามรูปแบบ: rest · new onset (CCS III ภายใน 2 เดือน) · increasing (เพิ่ม ≥1 class)",
     "ยุค hs-troponin ทำให้ unstable angina ลดลง เพราะถูกจัดเป็น NSTEMI แทน",
     "MINOCA = เข้าเกณฑ์ MI แต่หลอดเลือดไม่ตีบ — ต้องหาสาเหตุอื่น"],
    [
    mcq("CAR-IHD-MCQ-06",
        "A 70-year-old woman with sepsis and acute kidney injury has a high-sensitivity troponin of 80 ng/L (99th percentile 14 ng/L) on a routine panel. She has no chest pain, her ECG is unchanged from baseline, and echocardiography shows no new wall motion abnormality. What is the most appropriate interpretation?",
        ["This confirms acute myocardial infarction; start dual antiplatelet therapy",
         "Myocardial injury without evidence of ischaemia; this does not meet the definition of acute MI",
         "This is unstable angina by definition",
         "Troponin elevation in renal failure is always artefactual and can be ignored",
         "Immediate coronary angiography is mandatory"],
        1,
        """**นิยามของ AMI ต้องมีสองส่วน** ตามที่สไลด์ระบุ — **troponin สูงกว่า 99th percentile** **ร่วมกับ** **บริบททางคลินิกที่เข้าได้กับการขาดเลือด**

ผู้ป่วยรายนี้มีเพียงส่วนแรก จึงเป็น **myocardial injury** ไม่ใช่ **myocardial infarction**

**หลักฐานสนับสนุนที่ต้องมีอย่างน้อยหนึ่งข้อ** — และผู้ป่วยรายนี้ไม่มีเลย
- อาการของการขาดเลือด ✗ (ไม่มีเจ็บหน้าอก)
- ECG เปลี่ยนแปลงแบบขาดเลือด ✗ (เหมือนเดิม)
- เกิด pathological Q wave ✗
- ภาพพบการเคลื่อนไหวผนังผิดปกติใหม่ ✗
- พบลิ่มเลือดจากการสวนหรือชันสูตร ✗

**สาเหตุของ troponin สูงที่ไม่ใช่ ACS** — **sepsis, ไตวาย, หัวใจล้มเหลว, ภาวะหัวใจเต้นเร็วมาก, pulmonary embolism, myocarditis, ช็อก, ออกกำลังหนักมาก**

**สิ่งที่ควรทำ** — **รักษาสาเหตุหลัก (sepsis และ AKI)** และ **ตรวจ troponin ซ้ำเพื่อดูแนวโน้ม** เพราะ **รูปแบบขึ้นแล้วลง (rise and fall)** ช่วยแยกการบาดเจ็บเฉียบพลันจากการสูงแบบเรื้อรัง

**ทำไมข้ออื่นผิด** — การให้ **DAPT** โดยไม่มีหลักฐาน ACS เพิ่มความเสี่ยงเลือดออกโดยไม่จำเป็น · **unstable angina ต้องมีอาการ** และ **troponin ไม่ขึ้น** ซึ่งตรงข้ามกับรายนี้ · **troponin ในผู้ป่วยไตวายไม่ใช่ของปลอม** แต่สะท้อนการบาดเจ็บจริงและสัมพันธ์กับพยากรณ์โรคที่แย่ลง · การสวนหลอดเลือดไม่มีข้อบ่งชี้""",
        "Troponin ขึ้น + ไม่มีหลักฐานขาดเลือด = myocardial injury ไม่ใช่ MI — รักษาสาเหตุหลักและดูแนวโน้ม",
        "Universal definition of MI",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, Definition of acute MI", "Fourth Universal Definition of MI"]),
    ])

sec("cardio-ihd-05", "STEMI — เกณฑ์ ECG ที่ต้องจำตัวเลขให้แม่น",
    "จุด J · สองลีดต่อเนื่อง · ตัวเลขที่ต่างกันตามเพศและอายุ", 9,
"""สไลด์ให้เกณฑ์ไว้ละเอียด และ **ตัวเลขต่างกันตามลีด เพศ และอายุ** ซึ่งเป็นจุดที่ออกสอบบ่อย

### เกณฑ์ ST-segment elevation
**วัดที่จุด J และต้องพบใน ลีดที่ต่อเนื่องกันอย่างน้อยสองลีด**

| ลีด | เกณฑ์ |
|---|---|
| **V2–V3 ในผู้ชายอายุน้อยกว่า 40 ปี** | **≥ 2.5 mm** |
| **V2–V3 ในผู้ชายอายุ 40 ปีขึ้นไป** | **≥ 2 mm** |
| **V2–V3 ในผู้หญิง** | **≥ 1.5 mm** |
| **ลีดอื่นทั้งหมด** | **≥ 1 mm** |

**เงื่อนไขสำคัญ** — เกณฑ์เหล่านี้ใช้เมื่อ **ไม่มี LVH และไม่มี LBBB** เพราะทั้งสองภาวะทำให้ ST เปลี่ยนแปลงอยู่แล้วตามธรรมชาติ

### ST-segment elevation equivalent — กลุ่มที่พลาดบ่อยที่สุด

**Posterior MI**
- **ST depression ใน V1–V3 บ่งชี้การขาดเลือด โดยเฉพาะเมื่อ T wave ส่วนปลายเป็นบวก**
- **ยืนยันด้วย ST elevation ≥ 0.5 mm ในลีด V7–V9**
- ผู้ป่วยกลุ่มนี้ **เป็น STEMI และต้องได้ reperfusion** แต่ถ้าดูแค่ 12 ลีดมาตรฐานจะเห็นเป็น ST depression แล้วเข้าใจผิดว่าเป็น NSTEMI

### ECG ที่ยังไม่เข้าเกณฑ์ (non-diagnostic ECG)
สไลด์ระบุว่าให้ทำสามอย่าง
1. **นึกถึงว่าอาจมาเร็วมากหลังเริ่มอาการ**
2. **มองหา hyper-acute T wave** ซึ่ง **มาก่อน ST elevation**
3. **ทำ ECG ซ้ำ หรือ monitor ดูการเปลี่ยนแปลงของ ST**
4. **เพิ่มลีด V7–V9** เพื่อจับ posterior MI

### ลีดที่ควรเพิ่มเมื่อสงสัย
- **V7–V9** — posterior
- **V3R, V4R** — right ventricular infarction (สำคัญมากใน inferior MI เพราะ **ห้ามให้ไนเตรต** เมื่อมี RV infarction)

> **หลักที่ต้องทำให้ได้ภายใน 10 นาที** — ESC ระบุว่า **ต้องได้ ECG 12 ลีดภายใน 10 นาทีหลัง first medical contact และให้แพทย์ที่มีประสบการณ์แปลผลทันที**
""",
    ["V2–V3 ผู้ชาย < 40 ปี ≥ 2.5 mm · ผู้ชาย ≥ 40 ปี ≥ 2 mm · ผู้หญิง ≥ 1.5 mm · ลีดอื่น ≥ 1 mm",
     "ต้องพบในสองลีดที่ต่อเนื่องกัน และวัดที่จุด J",
     "ST depression V1–V3 + T ปลายเป็นบวก = สงสัย posterior MI → ทำ V7–V9",
     "Hyper-acute T wave มาก่อน ST elevation — ECG ไม่ชัดให้ทำซ้ำ",
     "Inferior MI ต้องทำ V3R, V4R เสมอ เพราะถ้ามี RV infarction ห้ามให้ไนเตรต"],
    [
    mcq("CAR-IHD-MCQ-07",
        "A 35-year-old man has 40 minutes of crushing chest pain. ECG shows 2 mm ST elevation in V2 and V3, with no LVH or LBBB. Which statement is correct?",
        ["This meets STEMI criteria because any ST elevation of 2 mm in V2-V3 qualifies",
         "This does not meet the V2-V3 threshold for men under 40 years, which is 2.5 mm; repeat the ECG and consider additional leads",
         "STEMI is excluded and he can be discharged",
         "The criteria apply only if LBBB is present",
         "Posterior leads are never useful in this situation"],
        1,
        """**เกณฑ์ V2–V3 ต่างกันตามเพศและอายุ** และผู้ชายอายุน้อยกว่า 40 ปีมีเกณฑ์ **สูงที่สุดคือ ≥ 2.5 mm** เพราะกลุ่มนี้มี **early repolarization** ที่ทำให้ ST ยกขึ้นเล็กน้อยได้ตามปกติ

| ลีด | เกณฑ์ |
|---|---|
| **V2–V3 ชาย < 40 ปี** | **≥ 2.5 mm** ← รายนี้ได้ 2 mm จึงยังไม่ถึง |
| V2–V3 ชาย ≥ 40 ปี | ≥ 2 mm |
| V2–V3 หญิง | ≥ 1.5 mm |
| ลีดอื่น | ≥ 1 mm |

**แต่ห้ามสรุปว่าไม่ใช่ ACS** — สไลด์ระบุสิ่งที่ต้องทำเมื่อ ECG ยังไม่เข้าเกณฑ์
1. นึกถึงว่า **อาจมาเร็วมากหลังเริ่มอาการ**
2. **มองหา hyper-acute T wave** ซึ่งมาก่อน ST elevation
3. **ทำ ECG ซ้ำหรือ monitor ดู dynamic ST change**
4. **เพิ่มลีด V7–V9** เพื่อจับ posterior MI

**สิ่งที่ต้องทำต่อ** — ส่ง **hs-troponin ตาม algorithm 0/1 ชั่วโมง**, ทำ ECG ซ้ำทุก 15–30 นาที, ให้ **แอสไพริน**, monitor จังหวะการเต้น และ **เตรียมพร้อมสำหรับการเปิดหลอดเลือดทันทีถ้า ST ยกขึ้นถึงเกณฑ์**

**ทำไมข้ออื่นผิด** — การ **ให้กลับบ้าน** ในผู้ป่วยเจ็บหน้าอก 40 นาทีโดยไม่ตรวจต่อเป็นความผิดพลาดร้ายแรง · เกณฑ์ใช้ **เมื่อไม่มี LBBB** ไม่ใช่เมื่อมี · **posterior lead มีประโยชน์มาก** โดยเฉพาะเมื่อ ECG มาตรฐานไม่ชัด""",
        "ชาย < 40 ปี ต้อง ≥ 2.5 mm ใน V2–V3 — ไม่ถึงเกณฑ์ไม่ได้แปลว่าไม่ใช่ ACS ให้ทำ ECG ซ้ำและเพิ่มลีด",
        "STEMI ECG criteria",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, ECG criteria"]),
    mcq("CAR-IHD-MCQ-08",
        "A 62-year-old man with ongoing chest pain has ECG showing 2 mm ST depression in V1-V3 with tall, upright terminal T waves. Which is the most appropriate next step?",
        ["Diagnose NSTEMI and plan invasive angiography within 24 hours",
         "Record posterior leads V7-V9 looking for ST elevation of at least 0.5 mm",
         "Give fibrinolysis immediately based on the ST depression",
         "Discharge if troponin is normal at presentation",
         "Record right-sided leads V3R and V4R only"],
        1,
        """**ST depression ใน V1–V3 ร่วมกับ T wave ส่วนปลายเป็นบวก = สัญญาณของ posterior MI** ซึ่งสไลด์ระบุไว้ตรง ๆ ว่า *"ST-segment depression in leads V1–V3 suggests myocardial ischaemia, especially when the terminal T-wave is positive"*

**ต้องยืนยันด้วย V7–V9** — สไลด์ระบุว่า **ST elevation ≥ 0.5 mm ใน V7–V9** เป็น **ST-segment elevation equivalent** และ **ใช้ระบุ posterior MI**

**ทำไมเรื่องนี้สำคัญมาก** — ถ้าดูแค่ 12 ลีดมาตรฐาน จะเห็นเป็น **ST depression** แล้วจัดเป็น NSTEMI ซึ่งนำไปสู่ **การรอสวนหลอดเลือดภายใน 24 ชั่วโมง** ทั้งที่ผู้ป่วยเป็น **STEMI ที่ต้องเปิดหลอดเลือดทันที** — ความล่าช้านี้ทำให้กล้ามเนื้อหัวใจตายเพิ่มโดยไม่จำเป็น

**กลไก** — ผนังด้านหลังของหัวใจไม่มีลีดมาตรฐานมองตรง ๆ ลีด V1–V3 จึงเห็นภาพ **กลับด้าน (reciprocal)** ของ ST elevation ด้านหลัง กลายเป็น ST depression และ Q wave ด้านหลังกลายเป็น R wave สูงใน V1–V2

**ทำไมข้ออื่นผิด** — จัดเป็น **NSTEMI แล้วรอ 24 ชั่วโมง** คือกับดักของข้อนี้ · **ให้ยาละลายลิ่มเลือดจาก ST depression เพียงอย่างเดียว** ไม่มีข้อบ่งชี้และอันตราย ต้องยืนยันด้วย V7–V9 ก่อน · **troponin ปกติตอนแรกไม่ตัด MI** เพราะยังไม่ถึงเวลาที่จะขึ้น · **V3R/V4R อย่างเดียว** ใช้ดู right ventricle ซึ่งคนละเรื่องกับ posterior""",
        "ST depression V1–V3 + T ปลายบวก = ทำ V7–V9 ทันที — อย่าเรียกเป็น NSTEMI แล้วรอ",
        "Posterior MI",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, ECG criteria / Atypical ECG presentation"]),
    ])

sec("cardio-ihd-06", "STEMI — การเปิดหลอดเลือดและเวลาเป้าหมาย",
    "primary PCI เป็นตัวเลือกแรก · ตัวเลขเวลาที่ต้องจำ", 10,
"""### หลักการ
**Primary PCI เป็นวิธีเปิดหลอดเลือดที่ดีที่สุด** ถ้าทำได้ภายในเวลาที่กำหนด มิฉะนั้นให้ **ยาละลายลิ่มเลือด**

### ตัวเลขเวลาที่ต้องจำ

| ตัวชี้วัด | เป้าหมาย |
|---|---|
| **ECG 12 ลีดหลัง first medical contact (FMC)** | **ภายใน 10 นาที** |
| **FMC ถึง wire crossing เมื่อไป PCI โดยตรง** | **ภายใน 120 นาที** |
| **ถ้าอยู่ในโรงพยาบาลที่ทำ PCI ได้** | **ภายใน 60 นาที** |
| **ถ้าต้องส่งต่อ** | **ภายใน 90 นาที** |
| **เริ่มยาละลายลิ่มเลือดหลังวินิจฉัย STEMI** | **ภายใน 10 นาที** |
| **Door-in to door-out ที่โรงพยาบาลที่ทำ PCI ไม่ได้** | **≤ 30 นาที** |

> **กฎการตัดสินใจ** — ถ้าคาดว่า **FMC ถึง wire crossing เกิน 120 นาที** ให้ **ยาละลายลิ่มเลือดทันที** แล้วส่งต่อไปโรงพยาบาลที่ทำ PCI ได้

### สิ่งที่ลดเวลาได้จริงตามสไลด์
- **วินิจฉัย STEMI ตั้งแต่ก่อนถึงโรงพยาบาล (pre-hospital / EMS)** แล้ว **เปิดห้องสวนหัวใจทันที** — ลดทั้งเวลาและอัตราตาย
- **ข้ามห้องฉุกเฉิน พาผู้ป่วยเข้าห้องสวนหัวใจโดยตรง** — **ประหยัดเวลาได้ 20 นาที** จาก FMC ถึง wire crossing

### Procedural aspects
- **Radial access เป็นทางเลือกมาตรฐาน** เพราะลดเลือดออกและลดอัตราตาย
- **Drug-eluting stent (DES) ดีกว่า bare-metal stent** ในทุกสถานการณ์
- **Intra-aortic balloon pump (IABP)** — สไลด์ระบุชัดว่า
  - **ไม่มีประโยชน์จากการใช้เป็นกิจวัตรใน anterior MI ที่ไม่มีช็อก**
  - **ไม่ได้ทำให้ผลลัพธ์ดีขึ้นใน MI ที่มี cardiogenic shock**
  - ใช้ได้ในบทบาท **haemodynamic support** ในผู้ป่วยช็อกเป็นราย ๆ

### CABG ฉุกเฉิน — เมื่อไร
- **กายวิภาคไม่เหมาะกับ PCI**
- **กล้ามเนื้อหัวใจที่เสี่ยงมีขนาดใหญ่ หรือมี cardiogenic shock**
- **มีภาวะแทรกซ้อนเชิงกลของ MI ที่ต้องผ่าตัดซ่อม** — ให้ทำ CABG พร้อมกับการซ่อม
- **PCI ล้มเหลวหรือหลอดเลือดอุดในตำแหน่งที่ทำ PCI ไม่ได้**

**เรื่องเวลาของ CABG ที่ไม่ฉุกเฉิน** — ผู้ป่วยที่ผ่า CABG เร็วเกินไปมี **อัตราตายสูงกว่า และสูงที่สุดเมื่อผ่าในวันเดียวกับที่เกิด MI** จึงควรกำหนดเวลาเป็นราย ๆ
- ผู้ที่ **อาการทรุดหรือเสี่ยงเกิดเหตุการณ์ซ้ำสูง** → **ผ่าโดยเร็วที่สุด ไม่ต้องรอให้เกล็ดเลือดฟื้น**
- ผู้ป่วยอื่น → **หยุด ticagrelor 3 วัน · clopidogrel 5 วัน · prasugrel 7 วัน** · **ให้แอสไพรินต่อ** และ **เริ่มแอสไพรินหลังผ่าตัดที่ 6–24 ชั่วโมงถ้าไม่มีเลือดออก**
""",
    ["ECG ภายใน 10 นาทีหลัง FMC · PCI ภายใน 120 นาที มิฉะนั้นให้ยาละลายลิ่มเลือด",
     "ในโรงพยาบาลที่ทำ PCI ได้เป้าคือ 60 นาที · ต้องส่งต่อคือ 90 นาที",
     "ข้ามห้องฉุกเฉินเข้าห้องสวนหัวใจโดยตรงประหยัด 20 นาที",
     "IABP ไม่มีประโยชน์เป็นกิจวัตร แม้ใน cardiogenic shock",
     "หยุดยาก่อน CABG: ticagrelor 3 วัน · clopidogrel 5 วัน · prasugrel 7 วัน"],
    [
    mcq("CAR-IHD-MCQ-09",
        "A patient is diagnosed with STEMI at a rural hospital without a catheterisation laboratory. The nearest PCI centre is 3 hours away by road, so expected first-medical-contact-to-wire time is about 200 minutes. What is the most appropriate management?",
        ["Transfer for primary PCI regardless of the delay",
         "Give fibrinolysis within 10 minutes of STEMI diagnosis, then transfer to a PCI centre",
         "Give aspirin only and observe locally",
         "Wait for troponin results before any reperfusion decision",
         "Insert an intra-aortic balloon pump before transfer"],
        1,
        """**เวลาที่คาดไว้ 200 นาที เกิน 120 นาที** จึง **ไม่ควรส่งไปทำ primary PCI เป็นทางเลือกแรก** แต่ต้อง **ให้ยาละลายลิ่มเลือดทันที**

**ตัวเลขเวลาที่ต้องจำ**

| ตัวชี้วัด | เป้าหมาย |
|---|---|
| ECG หลัง FMC | **10 นาที** |
| FMC ถึง wire crossing (เลือก PCI ได้) | **≤ 120 นาที** |
| **เริ่มยาละลายลิ่มเลือดหลังวินิจฉัย STEMI** | **≤ 10 นาที** |
| Door-in to door-out ที่ รพ. ที่ทำ PCI ไม่ได้ | **≤ 30 นาที** |

**สิ่งที่ต้องทำต่อหลังให้ยาละลายลิ่มเลือด** — **ส่งต่อไปโรงพยาบาลที่ทำ PCI ได้ทันที** ไม่ใช่รอดูอาการ เพราะต้องประเมินว่า **reperfusion สำเร็จหรือไม่** และทำ **rescue PCI** ถ้าล้มเหลว หรือ **routine early PCI** ถ้าสำเร็จ

**หลักฐานที่สไลด์ยกมา** — **pre-hospital fibrinolysis ลดอัตราตายระยะแรกได้ 17% เมื่อเทียบกับการให้ในโรงพยาบาล** หากให้ภายใน 2 ชั่วโมงแรกหลังเริ่มอาการ และ **pre-hospital fibrinolysis ตามด้วย early PCI ให้ผลใกล้เคียงกับการส่งไปทำ primary PCI** ในผู้ที่มาภายใน 3 ชั่วโมงและไม่สามารถทำ PCI ได้ภายใน 1 ชั่วโมงหลัง FMC

**ทำไมข้ออื่นผิด** — **ส่งไปทำ PCI โดยไม่สนเวลา** ทำให้กล้ามเนื้อหัวใจตายเพิ่มระหว่างเดินทาง · **ให้แอสไพรินแล้วสังเกตอาการ** คือไม่ได้ทำ reperfusion เลย · **รอผล troponin** เป็นความผิดพลาดร้ายแรง เพราะ **STEMI วินิจฉัยจาก ECG ไม่ต้องรอ troponin** · **IABP** สไลด์ระบุว่าไม่มีประโยชน์เป็นกิจวัตร""",
        "คาดว่าเกิน 120 นาทีถึง wire = ให้ยาละลายลิ่มเลือดภายใน 10 นาที แล้วส่งต่อ — STEMI ไม่ต้องรอ troponin",
        "Reperfusion strategy and timing",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, Reperfusion therapy / Summary of time target"]),
    ])

sec("cardio-ihd-07", "STEMI — ยาละลายลิ่มเลือด",
    "เลือกยา fibrin-specific · ข้อห้าม · การประเมินหลังให้", 8,
"""### การเลือกยา
สไลด์ระบุว่า **ควรเลือกยากลุ่ม fibrin-specific** และยกตัวอย่าง **tenecteplase (TNK-tPA) แบบ single-bolus ปรับตามน้ำหนัก**

**ข้อดีของ tenecteplase**
- **ลดอัตราตายที่ 30 วันได้เทียบเท่า accelerated tPA**
- **ปลอดภัยกว่าในแง่การลดเลือดออกนอกสมองและการให้เลือด**
- **ใช้ง่ายกว่าในภาวะนอกโรงพยาบาล** เพราะฉีดครั้งเดียว

### ข้อห้ามที่ต้องคัดกรองก่อนให้ทุกครั้ง

**ข้อห้ามสัมบูรณ์**
- **เคยมีเลือดออกในสมอง หรือ stroke ที่ไม่ทราบสาเหตุเมื่อใดก็ตาม**
- **Ischemic stroke ภายใน 6 เดือน**
- **เนื้องอกหรือความผิดปกติของหลอดเลือดในระบบประสาทกลาง (AVM)**
- **บาดเจ็บรุนแรง ผ่าตัดใหญ่ หรือบาดเจ็บที่ศีรษะภายใน 1 เดือน**
- **เลือดออกในทางเดินอาหารภายใน 1 เดือน**
- **ภาวะเลือดออกผิดปกติที่ทราบอยู่แล้ว** (ไม่รวมประจำเดือน)
- **สงสัย aortic dissection**
- **การเจาะที่กดห้ามเลือดไม่ได้ภายใน 24 ชั่วโมง** เช่น เจาะตับ หรือเจาะหลัง

**ข้อห้ามสัมพัทธ์**
- **TIA ภายใน 6 เดือน**
- **ได้ยาต้านการแข็งตัวของเลือดอยู่**
- **ตั้งครรภ์ หรือภายใน 1 สัปดาห์หลังคลอด**
- **ความดันโลหิตสูงที่คุมไม่ได้ (SBP > 180 mmHg)**
- **โรคตับระยะท้าย · เยื่อบุหัวใจอักเสบติดเชื้อ · แผลในทางเดินอาหารที่ยังไม่หาย**
- **การกู้ชีพที่ใช้เวลานานหรือมีการบาดเจ็บ**

### หลังให้ยาละลายลิ่มเลือดต้องทำอะไรต่อ
**ส่งต่อไปโรงพยาบาลที่ทำ PCI ได้เสมอ** แล้วประเมินว่า reperfusion สำเร็จหรือไม่

| ผล | การจัดการ |
|---|---|
| **ล้มเหลว** — อาการไม่ดีขึ้น หรือ **ST ลดลงน้อยกว่า 50% ที่ 60–90 นาที** | **Rescue PCI ทันที** |
| **สำเร็จ** | **สวนหลอดเลือดภายใน 2–24 ชั่วโมง** (routine early PCI) |

> **ห้ามให้ยาละลายลิ่มเลือดใน NSTE-ACS** — ไม่มีประโยชน์และเพิ่มอันตราย เป็นข้อที่ออกสอบบ่อย
""",
    ["เลือก fibrin-specific agent — tenecteplase ฉีดครั้งเดียว ใช้ง่ายที่สุดนอกโรงพยาบาล",
     "คัดกรองข้อห้ามทุกครั้ง โดยเฉพาะประวัติเลือดออกในสมองและ stroke",
     "ST ลดลงน้อยกว่า 50% ที่ 60–90 นาที = ล้มเหลว → rescue PCI",
     "ให้ยาละลายลิ่มเลือดสำเร็จก็ยังต้องสวนหลอดเลือดภายใน 2–24 ชั่วโมง",
     "ห้ามให้ยาละลายลิ่มเลือดใน NSTE-ACS"],
    [
    mcq("CAR-IHD-MCQ-10",
        "Ninety minutes after fibrinolysis for an inferior STEMI, the patient still has chest pain and the ST elevation has decreased by only 20%. What is the most appropriate management?",
        ["Repeat the same fibrinolytic agent",
         "Immediate transfer for rescue percutaneous coronary intervention",
         "Start an intra-aortic balloon pump and observe",
         "Give a second antiplatelet and reassess in 6 hours",
         "Schedule elective angiography in 1 week"],
        1,
        """**ST ลดลงน้อยกว่า 50% ที่ 60–90 นาที ร่วมกับยังเจ็บหน้าอกอยู่ = reperfusion ล้มเหลว → ต้องทำ rescue PCI ทันที**

**เกณฑ์ประเมินความสำเร็จของยาละลายลิ่มเลือด**

| ตัวชี้วัด | สำเร็จ |
|---|---|
| **การลดลงของ ST ที่ 60–90 นาที** | **≥ 50%** |
| อาการเจ็บหน้าอก | ดีขึ้นชัดเจน |
| จังหวะการเต้น | อาจมี **reperfusion arrhythmia** เช่น accelerated idioventricular rhythm |

**ทำไมต้องรีบ** — กล้ามเนื้อหัวใจยังขาดเลือดต่อเนื่อง ทุกนาทีที่ผ่านไปคือกล้ามเนื้อที่ตายเพิ่ม และ **rescue PCI ลดทั้งการเกิดหัวใจล้มเหลวและการเกิดเหตุการณ์ซ้ำ** เมื่อเทียบกับการรักษาต่อด้วยยา

**ทำไมข้ออื่นผิด**
- **ให้ยาละลายลิ่มเลือดซ้ำ** ไม่แนะนำ — เพิ่มความเสี่ยงเลือดออกโดยเฉพาะในสมอง โดยไม่เพิ่มอัตราการเปิดหลอดเลือด
- **IABP** สไลด์ระบุว่า **ไม่ได้ทำให้ผลลัพธ์ดีขึ้น** แม้ในผู้ป่วยช็อก และไม่ใช่ทางเลือกแทนการเปิดหลอดเลือด
- **รอประเมินอีก 6 ชั่วโมง** คือการปล่อยให้กล้ามเนื้อตายต่อ
- **นัดสวนหลอดเลือดในอีก 1 สัปดาห์** ช้าเกินไปอย่างสิ้นเชิง

> เทียบกับกรณีที่ **สำเร็จ** — ก็ยัง **ต้องสวนหลอดเลือดภายใน 2–24 ชั่วโมง** อยู่ดี ไม่ใช่จบที่ยา""",
        "ST ลดน้อยกว่า 50% ที่ 60–90 นาที = ล้มเหลว → rescue PCI ทันที ห้ามให้ยาละลายลิ่มเลือดซ้ำ",
        "Failed fibrinolysis",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, Fibrinolytic therapy"]),
    ])

sec("cardio-ihd-08", "NSTE-ACS — การวินิจฉัยด้วย hs-troponin",
    "algorithm 0/1 ชั่วโมง · สิ่งที่ไม่ควรส่ง · การแยกโรค", 9,
"""### หลักการวินิจฉัยตาม ESC 2020
สไลด์ยก recommendation มาไว้ชัดเจน

| คำแนะนำ | Class |
|---|---|
| **วินิจฉัยและประเมินความเสี่ยงระยะสั้นจาก ประวัติ อาการ สัญญาณชีพ การตรวจร่างกาย ECG และผลแล็บรวม hs-cTn** | **I B** |
| **ตรวจ troponin ด้วย high-sensitivity assay ทันทีที่รับไว้ และได้ผลภายใน 60 นาที** | **I B** |
| **ทำ ECG 12 ลีดภายใน 10 นาทีหลัง FMC และให้แพทย์ที่มีประสบการณ์แปลทันที** | **I B** |
| **ทำ ECG ซ้ำเมื่อมีอาการกลับมาหรือยังไม่แน่ใจ** | **I C** |
| **เพิ่มลีด V3R, V4R, V7–V9 เมื่อสงสัยการขาดเลือดต่อเนื่องแต่ลีดมาตรฐานไม่ชัด** | **I C** |

### Algorithm 0 ชั่วโมง / 1 ชั่วโมง
- **ESC 0h/1h algorithm เป็นตัวเลือกแรก (Class I B)** เมื่อมี assay ที่ validate แล้ว
- **0h/2h algorithm ใช้แทนได้ (Class I B)**
- **0h/3h ใช้ได้เมื่อมีเฉพาะ assay ที่ validate กับ 3 ชั่วโมง (Class IIa B)**
- **ถ้าสองค่าแรกยังไม่สรุปและอาการยังเข้าได้กับ ACS → ตรวจเพิ่มที่ 3 ชั่วโมง (Class I B)**

**ค่าที่ใช้ต่างกันตามยี่ห้อของ assay** เช่น hs-cTn T (Roche): very low < 5, low < 12, no 1h∆ < 3, high ≥ 52, 1h∆ ≥ 5 ng/L — **ต้องดูค่าของ assay ที่โรงพยาบาลตัวเองใช้ ไม่มีตัวเลขเดียวที่ใช้ได้ทุกที่**

### สิ่งที่ ESC 2020 บอกว่า "ไม่ต้องส่ง"
> **ไม่แนะนำให้ส่ง biomarker อื่นเป็นกิจวัตรร่วมกับ hs-cTn** ได้แก่ **CK, CK-MB, h-FABP และ copeptin (Class III B)**
>
> เป็นการเปลี่ยนแปลงที่สำคัญจากอดีตที่เคยส่ง CK-MB คู่กันเสมอ — ปัจจุบัน **hs-cTn เหนือกว่าในทุกด้าน** การส่งเพิ่มเพียงเพิ่มค่าใช้จ่ายและความสับสน
>
> ข้อยกเว้น — **copeptin ใช้ได้เมื่อไม่มี hs-cTn assay (Class IIa B)**

### การตรวจภาพ
- **Echocardiography** — แนะนำในผู้ป่วยที่มี **หัวใจหยุดเต้นหรือระบบไหลเวียนไม่เสถียร** ให้ทำทันทีหลัง ECG (Class I C) และใช้ประเมินการทำงานของหัวใจห้องล่างซ้ายและแยกโรคอื่น
- **CCTA แนะนำแทนการสวนหลอดเลือด (Class I A)** เพื่อ **ตัด ACS ออก** เมื่อ **ความน่าจะเป็นของ CAD ต่ำถึงปานกลาง และ troponin กับ ECG ปกติหรือไม่สรุป**
- ผู้ป่วยที่ **ไม่มีอาการเจ็บซ้ำ ECG ปกติ troponin ปกติ แต่ยังสงสัย ACS** → ทำ **stress test ที่มีภาพ หรือ CCTA ก่อนตัดสินใจสวนหลอดเลือด (Class I B)**

### การเฝ้าระวังจังหวะการเต้น
- **Monitor ต่อเนื่องจนกว่าจะวินิจฉัยหรือตัด NSTEMI ออก (I C)** และ **รับไว้ในหน่วยที่มี monitor (I C)**
- **เสี่ยงต่ำ — monitor ถึง 24 ชั่วโมงหรือจนทำ PCI แล้วแต่อย่างใดถึงก่อน (I C)**
- **เสี่ยงสูงขึ้น — monitor เกิน 24 ชั่วโมง (I C)**
""",
    ["hs-cTn ทันทีที่รับไว้ ผลภายใน 60 นาที · ECG ภายใน 10 นาที",
     "0h/1h เป็น algorithm แรก · 0h/2h ใช้แทนได้ · ยังไม่สรุปให้ตรวจซ้ำที่ 3 ชั่วโมง",
     "ห้ามส่ง CK, CK-MB, h-FABP, copeptin เป็นกิจวัตรร่วมกับ hs-cTn (Class III)",
     "ค่าจุดตัดต่างกันตามยี่ห้อ assay — ต้องรู้ค่าของโรงพยาบาลตัวเอง",
     "CCTA ใช้ตัด ACS ออกได้เมื่อความน่าจะเป็นต่ำถึงปานกลางและผลอื่นไม่สรุป"],
    [
    mcq("CAR-IHD-MCQ-11",
        "According to the 2020 ESC NSTE-ACS guideline as presented, which statement about biomarkers is correct?",
        ["CK-MB should always be measured alongside high-sensitivity troponin",
         "Routine measurement of CK, CK-MB, h-FABP or copeptin in addition to hs-cTn is NOT recommended",
         "Copeptin is recommended for all patients in addition to hs-cTn",
         "BNP should replace troponin for diagnosis",
         "Troponin should be measured only after 6 hours of symptoms"],
        1,
        """สไลด์ยก **"What is new"** ของ ESC 2020 มาโดยตรงว่า *"For diagnostic purposes, it is **not recommended** to routinely measure additional biomarkers such as **CK, CK-MB, h-FABP, or copeptin**, in addition to hs-cTn"* — เป็นคำแนะนำ **Class III B**

**เหตุผล** — **hs-cTn มีความไวและความจำเพาะเหนือกว่า marker เดิมทั้งหมด** การส่งเพิ่มจึง
- **ไม่เพิ่มความแม่นยำ**
- **เพิ่มค่าใช้จ่าย**
- **อาจทำให้สับสน** เมื่อผลไม่สอดคล้องกัน เช่น CK-MB ปกติแต่ hs-cTn ขึ้น

**ข้อยกเว้นเดียว** — **copeptin ใช้ได้เมื่อไม่มี hs-cTn assay** เพื่อช่วย rule out เร็ว (Class IIa B)

**BNP/NT-proBNP มีที่ใช้จริงแต่คนละบทบาท** — สไลด์ระบุว่า *"Measuring BNP or NT-proBNP plasma concentrations **should be considered to gain prognostic information**"* (Class IIa B) คือใช้ **บอกพยากรณ์โรค ไม่ใช่วินิจฉัย**

**ทำไมข้ออื่นผิด** — **ส่ง CK-MB เสมอ** เป็นแนวทางเก่า · **copeptin ทุกราย** ไม่ใช่ · **BNP แทน troponin** ผิดบทบาทโดยสิ้นเชิง · **รอ 6 ชั่วโมง** ขัดกับคำแนะนำที่ให้ **ตรวจทันทีที่รับไว้และได้ผลภายใน 60 นาที** แล้วใช้ algorithm 0h/1h""",
        "ยุค hs-troponin: เลิกส่ง CK-MB เป็นกิจวัตร · BNP ใช้บอกพยากรณ์ ไม่ใช่วินิจฉัย",
        "Biomarkers in NSTE-ACS",
        ["สไลด์ อ.สุรพันธ์ — 2020 ESC NSTEACS guideline, What is new"]),
    ])

sec("cardio-ihd-09", "NSTE-ACS — แบ่งความเสี่ยงและเวลาที่ต้องสวนหลอดเลือด",
    "สี่ระดับความเร่งด่วน · GRACE > 140 · เกณฑ์ very high risk", 10,
"""นี่คือหัวข้อที่ออกสอบมากที่สุดของ NSTE-ACS — **ความเร่งด่วนของการสวนหลอดเลือดขึ้นกับความเสี่ยง**

### Immediate invasive strategy — ภายใน 2 ชั่วโมง (Class I C)
เมื่อมี **very-high-risk criteria ข้อใดข้อหนึ่ง**
- **ระบบไหลเวียนไม่เสถียร หรือ cardiogenic shock**
- **เจ็บหน้าอกซ้ำหรือดื้อต่อการรักษาด้วยยา**
- **หัวใจเต้นผิดจังหวะที่คุกคามชีวิต**
- **ภาวะแทรกซ้อนเชิงกลของ MI**
- **หัวใจล้มเหลวที่สัมพันธ์กับ NSTE-ACS ชัดเจน**
- **ST depression มากกว่า 1 mm ใน ≥ 6 ลีด ร่วมกับ ST elevation ใน aVR และ/หรือ V1**

> ข้อสุดท้ายคือรูปแบบของ **left main หรือ proximal LAD occlusion หรือ three-vessel disease** — จำให้ได้เพราะดูเผิน ๆ เหมือน NSTEMI ธรรมดาแต่อันตรายมาก

### Early invasive strategy — ภายใน 24 ชั่วโมง (Class I A)
เมื่อมี **high-risk criteria ข้อใดข้อหนึ่ง**
- **วินิจฉัยเป็น NSTEMI** ตาม algorithm
- **ST/T เปลี่ยนแปลงแบบ dynamic หรือน่าจะใหม่ ในลีดที่ต่อเนื่องกัน ซึ่งบ่งชี้การขาดเลือดต่อเนื่อง**
- **ST elevation ชั่วคราว**
- **GRACE risk score มากกว่า 140**

### Selective invasive strategy (Class I A)
ผู้ป่วย **ความเสี่ยงต่ำ** — ให้ทำ **การทดสอบภาวะขาดเลือดที่เหมาะสม หรือ CCTA** ก่อน แล้วค่อยตัดสินใจ

### กรณีพิเศษ
**ผู้ป่วยที่รอดจากภาวะหัวใจหยุดเต้นนอกโรงพยาบาล ระบบไหลเวียนเสถียร และไม่มี ST elevation** → **ควรพิจารณาสวนหลอดเลือดแบบชะลอ (delayed) มากกว่าทันที (Class IIa B)**

### การเปิดหลอดเลือดหลายเส้น
- **Radial access เป็นมาตรฐาน (Class I A)**
- **DES ดีกว่า bare-metal stent ในทุกกรณี (Class I A)**
- **Complete revascularization ควรพิจารณาในผู้ป่วยที่ไม่มีช็อกและมีโรคหลายเส้น (Class IIa C)**
- **FFR-guided revascularization ของรอยโรคที่ไม่ใช่ culprit ใช้ได้ระหว่าง index PCI (Class IIb B)**

### GRACE risk score
ใช้ **บอกพยากรณ์โรค (Class IIa B)** โดยคำนวณจาก **อายุ อัตราการเต้นหัวใจ ความดันซิสโตลิก ระดับครีแอตินิน Killip class ภาวะหัวใจหยุดเต้นแรกรับ ST deviation และ troponin ที่สูง**
""",
    ["Very high risk → สวนภายใน 2 ชั่วโมง · high risk → ภายใน 24 ชั่วโมง · low risk → ตรวจก่อนค่อยตัดสินใจ",
     "ST depression > 1 mm ใน ≥ 6 ลีด + ST elevation ใน aVR = left main จนกว่าจะพิสูจน์เป็นอื่น → สวนภายใน 2 ชั่วโมง",
     "GRACE > 140 = high risk ต้องสวนภายใน 24 ชั่วโมง",
     "หัวใจหยุดเต้นนอกโรงพยาบาลที่เสถียรและไม่มี ST elevation ให้ชะลอการสวน ไม่ใช่รีบ"],
    [
    mcq("CAR-IHD-MCQ-12",
        "A 68-year-old man with NSTE-ACS has ongoing chest pain despite nitrates and morphine, blood pressure 82/50 mmHg, and ECG showing 2 mm ST depression in leads I, II, aVL, V4-V6 with ST elevation in aVR. What is the recommended timing of invasive strategy?",
        ["Selective invasive strategy after stress testing",
         "Immediate invasive strategy within 2 hours",
         "Early invasive strategy within 24 hours",
         "Invasive strategy within 72 hours",
         "Conservative management with fibrinolysis"],
        1,
        """ผู้ป่วยรายนี้เข้าเกณฑ์ **very-high-risk ถึงสามข้อ** ซึ่งต้อง **สวนหลอดเลือดทันทีภายใน 2 ชั่วโมง (Class I C)**

| เกณฑ์ very high risk | ผู้ป่วยรายนี้ |
|---|---|
| ระบบไหลเวียนไม่เสถียรหรือช็อก | ✓ **BP 82/50** |
| **เจ็บหน้าอกซ้ำหรือดื้อต่อการรักษาด้วยยา** | ✓ **ยังเจ็บแม้ได้ไนเตรตและมอร์ฟีน** |
| หัวใจเต้นผิดจังหวะที่คุกคามชีวิต | ✗ |
| ภาวะแทรกซ้อนเชิงกล | ✗ |
| หัวใจล้มเหลวจาก NSTE-ACS | ✗ |
| **ST depression > 1 mm ใน ≥ 6 ลีด + ST elevation ใน aVR** | ✓ **I, II, aVL, V4–V6 = 6 ลีด + aVR ยก** |

**รูปแบบ ECG นี้สำคัญมาก** — **ST depression กระจายหลายลีดร่วมกับ ST elevation ใน aVR** บ่งชี้ **การขาดเลือดทั่วทั้งชั้น subendocardium** ซึ่งมักมาจาก **left main disease, proximal LAD occlusion หรือ three-vessel disease** ผู้ป่วยกลุ่มนี้มีอัตราตายสูงมากและ **ไม่ควรรอ 24 ชั่วโมง**

**ทำไมข้ออื่นผิด**
- **Selective strategy** สงวนไว้สำหรับผู้ป่วยความเสี่ยงต่ำเท่านั้น
- **ภายใน 24 ชั่วโมง** คือเกณฑ์ของ **high risk** (NSTEMI, dynamic ST/T, transient ST elevation, GRACE > 140) ซึ่งช้าเกินไปสำหรับผู้ป่วยที่ช็อกและเจ็บไม่หยุด
- **72 ชั่วโมง** ไม่มีในคำแนะนำปัจจุบัน
- **ยาละลายลิ่มเลือด** — **ห้ามใช้ใน NSTE-ACS** ไม่มีประโยชน์และเพิ่มอันตราย""",
        "ช็อก หรือเจ็บไม่หยุดแม้ให้ยา หรือ ST depression ≥ 6 ลีด + aVR ยก = สวนภายใน 2 ชั่วโมง",
        "Timing of invasive strategy",
        ["สไลด์ อ.สุรพันธ์ — 2020 ESC NSTEACS, Coronary revascularization"]),
    mcq("CAR-IHD-MCQ-13",
        "A haemodynamically stable 55-year-old man with NSTEMI has no recurrent pain after treatment and a GRACE risk score of 165. When should invasive angiography be performed?",
        ["Within 2 hours", "Within 24 hours", "Within 7 days", "Only if a stress test is positive", "Never; medical therapy alone is sufficient"],
        1,
        """**GRACE risk score > 140 และการวินิจฉัย NSTEMI** ต่างก็เป็น **high-risk criteria** ซึ่งสไลด์ระบุว่าต้องใช้ **early invasive strategy ภายใน 24 ชั่วโมง (Class I A)**

**High-risk criteria ทั้งสี่ข้อ**
1. **วินิจฉัยเป็น NSTEMI** ✓ (รายนี้มี)
2. **ST/T เปลี่ยนแปลงแบบ dynamic หรือน่าจะใหม่ ในลีดต่อเนื่อง**
3. **ST elevation ชั่วคราว**
4. **GRACE risk score > 140** ✓ (รายนี้ 165)

**ทำไมไม่ใช่ 2 ชั่วโมง** — เกณฑ์ **very high risk** ต้องมี **ช็อก เจ็บดื้อยา arrhythmia คุกคามชีวิต ภาวะแทรกซ้อนเชิงกล หัวใจล้มเหลว หรือรูปแบบ ST depression ≥ 6 ลีด + aVR ยก** ซึ่งผู้ป่วยรายนี้ไม่มีเลย — **เสถียรและไม่เจ็บซ้ำ**

**ทำไมไม่ใช่ selective strategy** — การทำ stress test ก่อนสงวนไว้สำหรับ **ผู้ป่วยความเสี่ยงต่ำ** เท่านั้น การทำในผู้ป่วย NSTEMI ที่ GRACE 165 เป็นการหน่วงเวลาโดยไม่จำเป็นและอาจอันตราย

**GRACE คำนวณจาก** — อายุ, อัตราการเต้นหัวใจ, ความดันซิสโตลิก, ครีแอตินิน, Killip class, ภาวะหัวใจหยุดเต้นแรกรับ, ST deviation และ troponin ที่สูง

> จำคู่ตัวเลข — **GRACE > 140 = 24 ชั่วโมง** เทียบกับ **ST depression ≥ 6 ลีด + aVR = 2 ชั่วโมง**""",
        "NSTEMI หรือ GRACE > 140 = สวนภายใน 24 ชั่วโมง — stress test ก่อนใช้เฉพาะกลุ่มเสี่ยงต่ำ",
        "GRACE risk score",
        ["สไลด์ อ.สุรพันธ์ — 2020 ESC NSTEACS, Risk assessment"]),
    ])

sec("cardio-ihd-10", "ยาต้านเกล็ดเลือดและยาต้านการแข็งตัวของเลือดใน ACS",
    "DAPT 12 เดือน · ห้าม pre-treatment · ผู้ป่วยที่ต้องกิน OAC ด้วย", 10,
"""### DAPT — มาตรฐาน
**แอสไพริน + P2Y12 inhibitor นาน 12 เดือน** เว้นแต่มีข้อห้ามหรือเสี่ยงเลือดออกมากเกินไป (Class I A)

**ขนาดยาตามสไลด์**

| ยา | Loading dose | Maintenance |
|---|---|---|
| **Aspirin** | **150–300 mg กิน** (หรือ 75–250 mg IV) | **75–100 mg วันละครั้ง** |
| **Clopidogrel** | **300–600 mg** | **75 mg วันละครั้ง** |
| **Prasugrel** | **60 mg** | **10 mg วันละครั้ง** (5 mg ถ้าน้ำหนัก < 60 กก. หรืออายุ ≥ 75 ปี) |
| **Ticagrelor** | **180 mg** | **90 mg วันละสองครั้ง** |

### ข้อห้ามและข้อควรระวังที่ต้องจำ
> **Prasugrel ห้ามใช้ในผู้ที่เคยเป็น stroke หรือ TIA** — สไลด์ระบุว่า *"Prior stroke is a contraindication for prasugrel"*
> **Prasugrel ใช้ด้วยความระมัดระวังในผู้ที่อายุ ≥ 75 ปี** และถ้าจำเป็นให้ใช้ขนาด **5 mg**

### การเปลี่ยนแปลงที่สำคัญของ ESC 2020
1. **Prasugrel ควรพิจารณาก่อน ticagrelor** ในผู้ป่วย NSTE-ACS ที่จะไปทำ PCI (Class IIa B)
2. **ไม่แนะนำให้ pre-treatment ด้วย P2Y12 inhibitor** เมื่อ **ยังไม่ทราบกายวิภาคของหลอดเลือด และวางแผนทำ early invasive (Class III A)**
3. **De-escalation** — เปลี่ยนจาก prasugrel หรือ ticagrelor ไปเป็น **clopidogrel** อาจพิจารณาเป็นทางเลือก โดยทำตามดุลยพินิจ หรือใช้ **platelet function test หรือ CYP2C19 genotyping** นำทาง (Class IIb A)

### ยาต้านการแข็งตัวของเลือดระหว่างทำ PCI
- **ต้องให้ทุกราย ร่วมกับยาต้านเกล็ดเลือด (Class I A)**
- **UFH 70–100 IU/kg** (หรือ **50–70 IU/kg เมื่อใช้ร่วมกับ GP IIb/IIIa inhibitor**) เป็นมาตรฐาน (Class I A)
- **ห้ามสลับไปมาระหว่าง UFH กับ LMWH (Class III B)**
- **หยุดยาต้านการแข็งตัวของเลือดทันทีหลังทำหัตถการ** (Class IIa C)

### ผู้ป่วยที่ต้องกิน oral anticoagulant ด้วย (เช่น AF)
นี่คือสถานการณ์ที่ซับซ้อนที่สุดและออกสอบบ่อย

| ระยะ | การรักษา |
|---|---|
| **สัปดาห์แรกหลังเหตุการณ์** | **TAT (triple therapy)** — OAC + แอสไพริน + clopidogrel |
| **หลังจากนั้นถึง 12 เดือน** | **DAT เป็นค่าตั้งต้น** — **NOAC ขนาดป้องกัน stroke + ยาต้านเกล็ดเลือดตัวเดียว (ควรเป็น clopidogrel)** (Class I A) |
| **หลัง 12 เดือน** | **หยุดยาต้านเกล็ดเลือด เหลือ OAC อย่างเดียว** (Class I B) |

**ข้อห้ามสำคัญ** — **ห้ามใช้ ticagrelor หรือ prasugrel เป็นส่วนหนึ่งของ triple therapy (Class III C)**

### การลดความเสี่ยงเลือดออกระหว่าง PCI
- **ปรับขนาดยาตามน้ำหนักและการทำงานของไต** โดยเฉพาะในผู้หญิงและผู้สูงอายุ
- **ใช้ radial artery เป็นทางเข้าหลัก**
- **ให้ PPI ในผู้ที่ได้ DAPT และเสี่ยงเลือดออกทางเดินอาหารสูงกว่าเฉลี่ย**
""",
    ["DAPT 12 เดือนเป็นมาตรฐาน · aspirin maintenance 75–100 mg",
     "Prasugrel ห้ามใช้ในผู้ที่เคยเป็น stroke หรือ TIA และระวังในผู้สูงอายุ ≥ 75 ปี",
     "ห้าม pre-treatment ด้วย P2Y12 เมื่อยังไม่รู้กายวิภาคและจะทำ early invasive",
     "ผู้ป่วย AF: TAT 1 สัปดาห์ → DAT (NOAC + clopidogrel) ถึง 12 เดือน → OAC อย่างเดียว",
     "ห้ามใช้ ticagrelor หรือ prasugrel ใน triple therapy"],
    [
    mcq("CAR-IHD-MCQ-14",
        "A 72-year-old man with atrial fibrillation on apixaban presents with NSTEMI and undergoes PCI with a drug-eluting stent. Which antithrombotic regimen best matches the guideline presented?",
        ["Triple therapy with apixaban, aspirin and ticagrelor for 12 months",
         "Apixaban, aspirin and clopidogrel for up to 1 week, then apixaban plus clopidogrel until 12 months, then apixaban alone",
         "Stop apixaban and give aspirin plus ticagrelor for 12 months",
         "Apixaban alone with no antiplatelet therapy",
         "Aspirin plus prasugrel plus apixaban for 6 months"],
        1,
        """สไลด์ระบุกลยุทธ์ไว้ชัดเจนสำหรับผู้ป่วย AF ที่ต้องทำ PCI

| ระยะ | การรักษา | Class |
|---|---|---|
| **สัปดาห์แรก** | **TAT** — OAC + แอสไพริน + clopidogrel | **I A** |
| **ถึง 12 เดือน** | **DAT** — **NOAC ขนาดป้องกัน stroke + ยาต้านเกล็ดเลือดตัวเดียว (ควรเป็น clopidogrel)** | **I A** |
| **หลัง 12 เดือน** | **หยุดยาต้านเกล็ดเลือด เหลือ OAC อย่างเดียว** | **I B** |

**หลักการเบื้องหลัง** — ผู้ป่วยกลุ่มนี้ต้องการทั้ง **การป้องกัน stroke จาก AF** และ **การป้องกัน stent thrombosis** แต่การใช้ยาสามตัวพร้อมกันนาน ๆ **เพิ่มความเสี่ยงเลือดออกอย่างมาก** แนวทางจึงลดระยะเวลาของ triple therapy ให้สั้นที่สุด

**ข้อห้ามที่ต้องจำ** — **ห้ามใช้ ticagrelor หรือ prasugrel เป็นส่วนหนึ่งของ TAT (Class III C)** เพราะฤทธิ์ต้านเกล็ดเลือดแรงเกินไปเมื่อรวมกับ OAC

**ทำไมข้ออื่นผิด**
- **TAT ด้วย ticagrelor 12 เดือน** ผิดสองชั้น — ทั้งใช้ยาผิดตัวและนานเกินไป
- **หยุด apixaban** ทำให้ผู้ป่วยเสี่ยง stroke จาก AF ซึ่งเป็นข้อบ่งชี้เดิม
- **ให้ OAC อย่างเดียวทันทีหลังใส่ขดลวด** เสี่ยง **stent thrombosis** สูง
- **aspirin + prasugrel + apixaban** ขัดกับข้อห้ามโดยตรง

> ถ้าเสี่ยงเลือดออกสูง — สไลด์ระบุว่าให้พิจารณา **rivaroxaban 15 mg แทน 20 mg** หรือ **dabigatran 110 mg แทน 150 mg** ระหว่างที่ยังให้ยาต้านเกล็ดเลือดร่วม""",
        "AF + PCI: TAT 1 สัปดาห์ → NOAC + clopidogrel ถึง 12 เดือน → NOAC เดี่ยว — ห้าม ticagrelor/prasugrel ใน TAT",
        "Antithrombotic therapy with oral anticoagulation",
        ["สไลด์ อ.สุรพันธ์ — 2020 ESC NSTEACS, In patient need (N)OAC"]),
    mcq("CAR-IHD-MCQ-15",
        "A 58-year-old man with NSTE-ACS and a history of ischaemic stroke 3 years ago is scheduled for PCI. Which P2Y12 inhibitor is CONTRAINDICATED?",
        ["Clopidogrel", "Ticagrelor", "Prasugrel", "Cangrelor", "All are equally acceptable"],
        2,
        """สไลด์ระบุไว้ในตารางขนาดยาว่า **"Prior stroke is a contraindication for prasugrel"**

**เหตุผล** — ในการศึกษา TRITON-TIMI 38 ผู้ป่วยที่เคยเป็น **stroke หรือ TIA** และได้ prasugrel มี **อัตราการเกิดเลือดออกในสมองสูงขึ้นอย่างมีนัยสำคัญ** จนประโยชน์โดยรวมกลายเป็นโทษ

**ข้อควรระวังอื่นของ prasugrel ตามสไลด์**
- **อายุ ≥ 75 ปี** — ใช้ด้วยความระมัดระวัง ถ้าจำเป็นให้ใช้ **5 mg**
- **น้ำหนักตัว < 60 กก.** — ใช้ **5 mg**
- **ไม่ต้องปรับขนาดในผู้ป่วยโรคไต**

**ทางเลือกสำหรับผู้ป่วยรายนี้** — **ticagrelor** (LD 180 mg, MD 90 mg วันละสองครั้ง) หรือ **clopidogrel** (LD 300–600 mg, MD 75 mg) เมื่อ ticagrelor ใช้ไม่ได้

**เปรียบเทียบคุณสมบัติ**

| | **Clopidogrel** | **Prasugrel** | **Ticagrelor** |
|---|---|---|---|
| การย้อนกลับ | ไม่ย้อนกลับ | ไม่ย้อนกลับ | **ย้อนกลับได้** |
| ต้องเปลี่ยนเป็นรูปออกฤทธิ์ | **ใช่ 2 ขั้น** | ใช่ 1 ขั้น | **ไม่ต้อง** |
| เริ่มออกฤทธิ์ | **ช้า 2–6 ชม.** | เร็ว 0.5–4 ชม. | เร็ว 0.5–2 ชม. |
| หยุดก่อนผ่าตัด | **5 วัน** | **7 วัน** | **5 วัน** |""",
        "เคยเป็น stroke หรือ TIA = ห้าม prasugrel เด็ดขาด — เลือก ticagrelor หรือ clopidogrel แทน",
        "P2Y12 inhibitors",
        ["สไลด์ อ.สุรพันธ์ — 2020 ESC NSTEACS, Table 6-7 Medication"]),
    ])

sec("cardio-ihd-11", "หลังรอดจาก MI — ยาและการปรับวิถีชีวิต",
    "การเลิกบุหรี่ · อาหาร · cardiac rehabilitation · การกลับไปใช้ชีวิต", 9,
"""สไลด์ให้พื้นที่กับหัวข้อนี้มาก เพราะเป็นส่วนที่ **ลดอัตราตายได้มากที่สุดต่อบาทที่ลงทุน**

### เลิกบุหรี่ — มาตรการที่คุ้มค่าที่สุด
- **บุหรี่มีฤทธิ์กระตุ้นการเกิดลิ่มเลือดอย่างแรง**
- **การเลิกบุหรี่เป็นการป้องกันทุติยภูมิที่คุ้มค่าที่สุดในบรรดาทั้งหมด**
- **ผู้ที่เลิกได้มีอัตราตายลดลง 36%**
- **ควรเริ่มตั้งแต่ขณะนอนโรงพยาบาล** ซึ่งเป็นช่วงที่ห้ามสูบอยู่แล้ว และ **ทำต่อเนื่องหลังจำหน่าย**
- ใช้ **การสนับสนุนทางพฤติกรรมร่วมกับยา** — **nicotine replacement, bupropion, varenicline**

### อาหาร แอลกอฮอล์ และน้ำหนัก
- **อาหารแบบเมดิเตอร์เรเนียน**
- **ไขมันอิ่มตัวไม่เกิน 10% ของพลังงานทั้งหมด** แทนที่ด้วย **polyunsaturated fatty acid**
- **ไขมันทรานส์ให้น้อยที่สุด**
- **เกลือน้อยกว่า 5 กรัมต่อวัน**
- **ใยอาหาร 30–45 กรัมต่อวัน**
- **ผลไม้ 200 กรัม และผัก 200 กรัมต่อวัน**
- **ปลา 1–2 ครั้งต่อสัปดาห์** โดยเฉพาะปลาที่มีไขมันสูง
- **ถั่วไม่ใส่เกลือ 30 กรัมต่อวัน**
- **แอลกอฮอล์จำกัด** — ชายไม่เกิน 2 แก้ว (20 กรัมแอลกอฮอล์) หญิงที่ไม่ตั้งครรภ์ไม่เกิน 1 แก้วต่อวัน **และไม่แนะนำให้ผู้ที่ไม่ดื่มอยู่แล้วเริ่มดื่ม**
- **หลีกเลี่ยงเครื่องดื่มที่เติมน้ำตาล**
- **ไขมันหน้าท้องเป็นอันตรายเป็นพิเศษ** — การลดน้ำหนักมีผลดีต่อปัจจัยเสี่ยง แม้ **ยังไม่มีข้อพิสูจน์ว่าการลดน้ำหนักเองลดอัตราตาย**

### Cardiac rehabilitation
- **ผู้ป่วย AMI ทุกรายควรเข้าโปรแกรมฟื้นฟูหัวใจที่มีการออกกำลังกาย** โดยพิจารณา **อายุ ระดับกิจกรรมก่อนเกิดโรค และข้อจำกัดทางร่างกาย**
- โปรแกรมควรมี **การฝึกออกกำลังกาย การปรับปัจจัยเสี่ยง การให้ความรู้ การจัดการความเครียด และการสนับสนุนทางจิตใจ**
- **ลดอัตราตายจากโรคหัวใจได้ 22%**
- ปัจจุบันส่วนใหญ่เป็นโปรแกรมผู้ป่วยนอก **8–24 สัปดาห์**

### การกลับไปใช้ชีวิต
- **การกลับไปทำงานเป็นตัวชี้วัดการฟื้นตัวที่สำคัญ** — ตัดสินเป็นราย ๆ ตาม **การทำงานของหัวใจห้องล่างซ้าย ความสมบูรณ์ของการเปิดหลอดเลือด การคุมจังหวะการเต้น และลักษณะงาน**
- **การลาป่วยยาวมักไม่เกิดประโยชน์**
- **กิจกรรมเบาถึงปานกลางหลังจำหน่ายควรได้รับการสนับสนุน**
- **กิจกรรมทางเพศกลับมาได้เร็ว** โดยปรับตามความสามารถทางกาย
- **การเดินทางโดยเครื่องบิน**
  - **MI ที่ไม่มีภาวะแทรกซ้อน เปิดหลอดเลือดครบ และ LVEF > 40%** → **ความเสี่ยงต่ำ เดินทางได้ตั้งแต่วันที่ 3 หลังจำหน่าย**
  - **STEMI ที่มีภาวะแทรกซ้อน หัวใจล้มเหลว LVEF < 40% ยังมีการขาดเลือดเหลือ หรือมีการเต้นผิดจังหวะ** → **เลื่อนออกไปจนกว่าจะคงที่**

### ความดันโลหิตและความร่วมมือในการรักษา
- **เป้าหมาย SBP < 140 mmHg** · ผู้สูงอายุที่เปราะบางตั้งเป้าหลวมกว่าได้ · ผู้ที่เสี่ยงสูงมากและทนยาได้หลายตัวอาจพิจารณา **< 120 mmHg**
- **ความร่วมมือในการกินยาต่ำเป็นอุปสรรคสำคัญ** และ **การนัดติดตามช้าหลัง AMI ทำให้ความร่วมมือแย่ลงทั้งระยะสั้นและระยะยาว**
- **กลยุทธ์ที่ช่วยได้** — **ยารวมเม็ด (fixed-dose combination หรือ polypill)** ซึ่งในการศึกษา FOCUS พบว่า **เพิ่มความร่วมมือได้ที่ 9 เดือน**
""",
    ["เลิกบุหรี่ลดอัตราตาย 36% และเป็นการป้องกันทุติยภูมิที่คุ้มค่าที่สุด",
     "Cardiac rehabilitation ลดอัตราตายจากโรคหัวใจ 22% — ควรส่งทุกราย",
     "MI ไม่มีภาวะแทรกซ้อน + LVEF > 40% บินได้ตั้งแต่วันที่ 3 หลังจำหน่าย",
     "เป้าความดัน SBP < 140 mmHg · นัดติดตามเร็วช่วยเพิ่มความร่วมมือในการกินยา"],
    [
    mcq("CAR-IHD-MCQ-16",
        "Which secondary prevention measure after myocardial infarction is described in the lecture as potentially the most cost-effective of all, with a 36% reduction in mortality among those who succeed?",
        ["Exercise-based cardiac rehabilitation", "Smoking cessation", "Mediterranean diet", "Blood pressure control below 120 mmHg", "Use of a polypill"],
        1,
        """สไลด์ระบุไว้ตรง ๆ ว่า **"Smoking cessation is potentially the most (cost) effective of all secondary prevention"** และ **"36% reduction of mortality in quitters"**

**เหตุผล** — **บุหรี่มีฤทธิ์กระตุ้นการเกิดลิ่มเลือดอย่างแรง (strong prothrombotic effect)** การเลิกจึงลดความเสี่ยงได้เร็วและมาก โดยไม่มีค่ายา

**วิธีที่ได้ผลตามสไลด์**
- **เริ่มตั้งแต่ขณะนอนโรงพยาบาล** ซึ่งเป็นช่วงที่ห้ามสูบอยู่แล้ว จึงเป็นโอกาสทอง แล้ว **ทำต่อเนื่องหลังจำหน่าย**
- **ใช้การสนับสนุนทางพฤติกรรมร่วมกับยา** — **nicotine replacement therapy, bupropion, varenicline**
- **บุหรี่ไฟฟ้าอาจช่วยได้** — สไลด์ระบุว่าบุหรี่ไฟฟ้าที่มีนิโคตินมีอัตราการเลิกหรือลดการสูบสูงกว่ายาหลอก

**เทียบกับมาตรการอื่นที่สไลด์ให้ตัวเลขไว้**

| มาตรการ | ผล |
|---|---|
| **เลิกบุหรี่** | **ลดอัตราตาย 36%** |
| **Exercise-based cardiac rehabilitation** | **ลดอัตราตายจากโรคหัวใจ 22%** |
| เป้าความดัน | **SBP < 140 mmHg** (ไม่ใช่ < 120 ในทุกราย — สงวนไว้สำหรับผู้เสี่ยงสูงมากที่ทนยาได้) |
| **Polypill** | เพิ่ม **ความร่วมมือในการกินยา** ยังต้องการการศึกษาใหญ่กว่านี้เพื่อยืนยันประโยชน์ทางคลินิก |""",
        "เลิกบุหรี่ = ลดตาย 36% · cardiac rehab = ลดตายจากหัวใจ 22% — สองตัวเลขนี้จำให้แม่น",
        "Secondary prevention",
        ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI, Lifestyle and risk factor control"]),
    ])

MEQ = [{
 "id": "CAR-IHD-MEQ-01", "part": "MEQ", "lec": "24/9", "lecture": "Ischemic heart diseases",
 "topic": "Acute STEMI at a non-PCI hospital — diagnosis, reperfusion decision and complications",
 "vignette": """ชายไทยอายุ 58 ปี มาห้องฉุกเฉินโรงพยาบาลชุมชนด้วยเจ็บแน่นหน้าอก 50 นาที
PI: 50 นาทีก่อนมาโรงพยาบาล ขณะเดินขึ้นบันได มีอาการแน่นกลางอกเหมือนถูกกดทับ ร้าวไปกรามและแขนซ้าย เหงื่อแตกท่วมตัว คลื่นไส้ อาเจียน 1 ครั้ง นั่งพักแล้วไม่ดีขึ้น
U/D: ความดันโลหิตสูง 8 ปี กิน amlodipine ไม่สม่ำเสมอ · สูบบุหรี่วันละ 1 ซอง มา 30 ปี · บิดาเสียชีวิตด้วยโรคหัวใจตอนอายุ 55 ปี · ปฏิเสธประวัติ stroke เลือดออกผิดปกติ หรือผ่าตัดใหญ่
PE: GA: กระสับกระส่าย เหงื่อแตก
V/S: BT 36.8 C, PR 52/min, RR 22/min, BP 96/60 mmHg (วัดสองแขนเท่ากัน), SpO2 96% room air
Heart: จังหวะสม่ำเสมอ ไม่มี murmur · Lung: ไม่มี crepitation · JVP ไม่โป่ง · ปลายมือเย็นเล็กน้อย
ECG 12 ลีด (ทำที่นาทีที่ 8 หลังถึงโรงพยาบาล): ST elevation 3 mm ใน lead II, III, aVF และ ST depression ใน I, aVL
ข้อมูลโรงพยาบาล: ไม่มีห้องสวนหัวใจ · โรงพยาบาลที่ทำ PCI ได้อยู่ห่างออกไป โดยรถพยาบาลใช้เวลาเดินทางประมาณ 2 ชั่วโมง 40 นาที""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยพร้อมระบุตำแหน่งของกล้ามเนื้อหัวใจที่ขาดเลือด และบอกว่าต้องทำ ECG เพิ่มเติมอะไรและเพราะอะไร",
   "a": """**การวินิจฉัย — Acute inferior ST-elevation myocardial infarction (STEMI)**

**เหตุผล**
- **อาการเข้าได้กับ typical angina ที่เกิดขณะพักและไม่ดีขึ้น** นานเกิน 20 นาที
- **ST elevation 3 mm ใน lead II, III, aVF** ซึ่งเป็น **ลีดที่ต่อเนื่องกันของผนังด้านล่าง (inferior wall)** และ **เกิน 1 mm ตามเกณฑ์ของลีดอื่นที่ไม่ใช่ V2–V3**
- **ST depression ใน I, aVL เป็น reciprocal change** ซึ่งสนับสนุนการวินิจฉัยอย่างมาก

**หลอดเลือดที่น่าจะเป็นต้นเหตุ** — **right coronary artery (RCA)** ในผู้ป่วยส่วนใหญ่ (หรือ left circumflex ในบางราย)

**ECG เพิ่มเติมที่ต้องทำทันที — ลีดด้านขวา V3R และ V4R**

**เหตุผลที่สำคัญที่สุด** — เพื่อตรวจหา **right ventricular (RV) infarction** ซึ่งพบร่วมกับ inferior MI ได้บ่อย เพราะ RCA เลี้ยงทั้งผนังด้านล่างและหัวใจห้องล่างขวา

**ทำไมต้องรู้ให้ได้ก่อนให้ยา**
> **ถ้ามี RV infarction ห้ามให้ไนเตรต** และต้องระวังยาที่ลด preload ทุกชนิด (รวมมอร์ฟีนขนาดสูงและยาขับปัสสาวะ) เพราะหัวใจห้องล่างขวาที่ขาดเลือด **พึ่งพา preload อย่างมาก** การลด preload จะทำให้ **ความดันตกรุนแรงทันที**
> การรักษาความดันต่ำจาก RV infarction คือ **ให้สารน้ำ** ไม่ใช่ยาขับปัสสาวะ

**เบาะแสที่ทำให้ต้องสงสัย RV infarction ในผู้ป่วยรายนี้** — **BP 96/60 ซึ่งค่อนข้างต่ำ** และ **PR 52/min (bradycardia)** ซึ่งพบบ่อยใน inferior MI จากการที่ RCA เลี้ยง SA และ AV node

**และควรทำ V7–V9** เพื่อดู posterior extension ซึ่งพบร่วมกับ inferior MI ได้บ่อยเช่นกัน"""},
  {"q": "2. จงตัดสินใจเรื่องการเปิดหลอดเลือด พร้อมแสดงเหตุผลเชิงตัวเลข และระบุสิ่งที่ต้องทำก่อนให้ยา",
   "a": """**การตัดสินใจ — ให้ยาละลายลิ่มเลือด (fibrinolysis) ทันที แล้วส่งต่อไปโรงพยาบาลที่ทำ PCI ได้**

**เหตุผลเชิงตัวเลข**

| ตัวชี้วัด | เป้าหมาย | ผู้ป่วยรายนี้ |
|---|---|---|
| ECG หลัง FMC | **≤ 10 นาที** | ✓ ทำที่นาทีที่ 8 |
| **FMC ถึง wire crossing ถ้าจะเลือก primary PCI** | **≤ 120 นาที** | ✗ **เดินทาง 160 นาที ยังไม่รวมเวลาเตรียมและเวลาในห้องสวน** |
| **เริ่มยาละลายลิ่มเลือดหลังวินิจฉัย STEMI** | **≤ 10 นาที** | เป้าหมายที่ต้องทำให้ได้ |
| **Door-in to door-out** | **≤ 30 นาที** | เป้าหมายที่ต้องทำให้ได้ |

เมื่อ **คาดว่าเวลาถึง wire crossing เกิน 120 นาที** แนวทางระบุให้ **ให้ยาละลายลิ่มเลือดเป็นทางเลือกแรก**

**หลักฐานสนับสนุน** — สไลด์ระบุว่า **pre-hospital fibrinolysis ลดอัตราตายระยะแรกได้ 17%** เมื่อให้ภายใน 2 ชั่วโมงแรกหลังเริ่มอาการ และ **การให้ยาละลายลิ่มเลือดตามด้วย early PCI ให้ผลใกล้เคียงกับการส่งไปทำ primary PCI** ในผู้ที่มาภายใน 3 ชั่วโมงและทำ PCI ภายใน 1 ชั่วโมงหลัง FMC ไม่ได้ — ผู้ป่วยรายนี้มาที่ 50 นาทีจึงอยู่ในกลุ่มที่ได้ประโยชน์สูง

**ยาที่เลือก** — **fibrin-specific agent** โดยเฉพาะ **tenecteplase (TNK-tPA) แบบ single bolus ปรับตามน้ำหนัก** เพราะ **ลดอัตราตายที่ 30 วันเทียบเท่า accelerated tPA, ปลอดภัยกว่าในแง่เลือดออกนอกสมอง และใช้ง่ายที่สุด**

**สิ่งที่ต้องทำก่อนให้ยา**

1. **คัดกรองข้อห้ามให้ครบ** — ผู้ป่วยรายนี้ปฏิเสธประวัติ stroke, เลือดออกผิดปกติ และผ่าตัดใหญ่ · **วัดความดันสองแขนเท่ากันและไม่มีอาการร้าวไปหลัง** ช่วยลดความน่าจะเป็นของ **aortic dissection** ซึ่งเป็นข้อห้ามสัมบูรณ์ · **BP 96/60 ไม่ใช่ข้อห้าม** (ข้อห้ามสัมพัทธ์คือ SBP > 180)
2. **ทำ V3R, V4R ก่อนให้ไนเตรต** — ถ้ามี RV infarction **ห้ามให้ไนเตรต**
3. **ให้แอสไพริน loading 150–300 mg เคี้ยว** และ **clopidogrel** (ในบริบทของ fibrinolysis ใช้ clopidogrel ไม่ใช่ prasugrel หรือ ticagrelor)
4. **ให้ยาต้านการแข็งตัวของเลือดร่วม** ตามสูตรที่ใช้กับ fibrinolysis
5. **เปิดเส้นเลือดสองเส้น ติด monitor เตรียมเครื่องกระตุกหัวใจ** เพราะเสี่ยงต่อ **VF และ bradyarrhythmia**
6. **แจ้งโรงพยาบาลปลายทางและเปิดห้องสวนหัวใจล่วงหน้า** — สไลด์ระบุว่าการเปิดห้องสวนตั้งแต่ก่อนถึงช่วยลดเวลาและอัตราตาย"""},
  {"q": "3. หลังให้ยาละลายลิ่มเลือด 75 นาที ผู้ป่วยยังเจ็บหน้าอกอยู่ ECG พบว่า ST ใน lead III ลดลงจาก 3 mm เหลือ 2.5 mm จงประเมินและวางแผนต่อ",
   "a": """**การประเมิน — reperfusion ล้มเหลว (failed fibrinolysis)**

**เกณฑ์ที่ใช้**

| ตัวชี้วัด | เกณฑ์สำเร็จ | ผู้ป่วยรายนี้ |
|---|---|---|
| **การลดลงของ ST ที่ 60–90 นาที** | **≥ 50%** | ✗ **ลดลงเพียง 0.5 จาก 3 mm = 17%** |
| **อาการเจ็บหน้าอก** | ดีขึ้นชัดเจน | ✗ **ยังเจ็บอยู่** |
| Reperfusion arrhythmia | อาจพบ accelerated idioventricular rhythm | ไม่ได้ระบุ |

**แผนการรักษา — ส่งต่อทำ rescue PCI ทันที**

1. **ติดต่อโรงพยาบาลที่ทำ PCI ได้ทันที** แจ้งว่าเป็น failed fibrinolysis เพื่อให้เตรียมห้องสวนหัวใจรอ
2. **ส่งตัวโดยรถพยาบาลที่มีทีมและอุปกรณ์กู้ชีพครบ** ติด monitor ตลอดทาง
3. **ให้ยาต้านเกล็ดเลือดและยาต้านการแข็งตัวของเลือดต่อเนื่อง**
4. **เฝ้าระวังภาวะแทรกซ้อนระหว่างทาง** — arrhythmia, ความดันตก, หัวใจล้มเหลว

**สิ่งที่ห้ามทำ**
> **ห้ามให้ยาละลายลิ่มเลือดซ้ำ** — เพิ่มความเสี่ยงเลือดออกโดยเฉพาะในสมองอย่างมาก โดยไม่เพิ่มอัตราการเปิดหลอดเลือด
> **ห้ามรอดูอาการต่อ** — กล้ามเนื้อหัวใจยังตายเพิ่มทุกนาที
> **IABP ไม่ใช่ทางเลือกแทนการเปิดหลอดเลือด** — สไลด์ระบุว่า **ไม่ได้ทำให้ผลลัพธ์ดีขึ้นแม้ในผู้ป่วยที่มี cardiogenic shock**

**เปรียบเทียบกับกรณีที่สำเร็จ** — แม้ reperfusion จะสำเร็จ **ก็ยังต้องส่งไปสวนหลอดเลือดภายใน 2–24 ชั่วโมง** (routine early PCI) ไม่ใช่จบการรักษาที่ยา"""},
  {"q": "4. จงวางแผนการดูแลระยะยาวหลังผู้ป่วยรอดชีวิตและออกจากโรงพยาบาล",
   "a": """**1) ยาที่ต้องได้ทุกราย (event prevention)**
- **DAPT — แอสไพริน 75–100 mg/วัน + P2Y12 inhibitor นาน 12 เดือน** (ผู้ป่วยรายนี้ไม่มีประวัติ stroke จึงใช้ prasugrel หรือ ticagrelor ได้ตามบริบทของการทำ PCI)
- **Statin ขนาดสูง** ให้โดยไม่ขึ้นกับระดับไขมันเริ่มต้น
- **Beta-blocker** — มีข้อบ่งชี้ชัดเจนหลัง MI
- **ACEI/ARB** — ผู้ป่วยรายนี้มีความดันโลหิตสูงร่วม จึงมีข้อบ่งชี้
- **พิจารณา PPI** เพราะได้ DAPT และมีความเสี่ยงเลือดออกทางเดินอาหาร

**ต้องอธิบายให้ผู้ป่วยเข้าใจว่า** — **ยาที่ลดการตายกับยาที่ลดอาการเป็นคนละกลุ่ม** การที่ไม่มีอาการแล้วไม่ใช่เหตุผลให้หยุด statin หรือ antiplatelet

**2) เลิกบุหรี่ — สำคัญที่สุดในผู้ป่วยรายนี้**
- ผู้ป่วยสูบวันละซอง 30 ปี และ **บุหรี่มีฤทธิ์กระตุ้นการเกิดลิ่มเลือดอย่างแรง**
- **การเลิกบุหรี่ลดอัตราตายได้ 36%** และเป็น **การป้องกันทุติยภูมิที่คุ้มค่าที่สุด**
- **เริ่มตั้งแต่ขณะนอนโรงพยาบาล** แล้วติดตามต่อเนื่องหลังจำหน่าย
- **ใช้การสนับสนุนทางพฤติกรรมร่วมกับยา** — nicotine replacement, bupropion หรือ varenicline

**3) Cardiac rehabilitation**
- **ส่งเข้าโปรแกรมฟื้นฟูหัวใจที่มีการออกกำลังกายทุกราย** — **ลดอัตราตายจากโรคหัวใจ 22%**
- โปรแกรมผู้ป่วยนอก **8–24 สัปดาห์** ประกอบด้วย **การฝึกออกกำลังกาย การปรับปัจจัยเสี่ยง การให้ความรู้ การจัดการความเครียด และการสนับสนุนทางจิตใจ**

**4) อาหารและน้ำหนัก**
- **อาหารแบบเมดิเตอร์เรเนียน** — ไขมันอิ่มตัวไม่เกิน 10% ของพลังงาน, ไขมันทรานส์น้อยที่สุด, **เกลือน้อยกว่า 5 กรัม/วัน**, ใยอาหาร 30–45 กรัม/วัน, **ผัก 200 กรัม + ผลไม้ 200 กรัม/วัน**, ปลา 1–2 ครั้ง/สัปดาห์, ถั่วไม่ใส่เกลือ 30 กรัม/วัน
- **จำกัดแอลกอฮอล์** ไม่เกิน 2 แก้ว/วันสำหรับชาย และ **หลีกเลี่ยงเครื่องดื่มเติมน้ำตาล**

**5) ควบคุมความดันโลหิต**
- **เป้าหมาย SBP < 140 mmHg** ร่วมกับ **ลดเกลือ เพิ่มกิจกรรมทางกาย และลดน้ำหนัก**
- ผู้ป่วยรายนี้กิน amlodipine ไม่สม่ำเสมอมาก่อน จึงต้อง **แก้ปัญหาความร่วมมือในการกินยา** เป็นพิเศษ

**6) ความร่วมมือในการรักษาและการติดตาม**
- **นัดติดตามเร็วหลังจำหน่าย** — สไลด์ระบุว่า **การนัดช้าทำให้ความร่วมมือแย่ลงทั้งระยะสั้นและระยะยาว**
- พิจารณา **ยารวมเม็ด (polypill)** ซึ่งการศึกษา FOCUS พบว่า **เพิ่มความร่วมมือที่ 9 เดือน**

**7) การกลับไปใช้ชีวิต**
- **กลับไปทำงาน** — ตัดสินเป็นรายตาม **LVEF ความสมบูรณ์ของการเปิดหลอดเลือด การคุมจังหวะการเต้น และลักษณะงาน** · **การลาป่วยยานานมักไม่เกิดประโยชน์**
- **กิจกรรมเบาถึงปานกลางควรสนับสนุน** · **กิจกรรมทางเพศกลับมาได้เร็ว**
- **การเดินทางโดยเครื่องบิน** — ถ้า **ไม่มีภาวะแทรกซ้อน เปิดหลอดเลือดครบ และ LVEF > 40%** เดินทางได้ **ตั้งแต่วันที่ 3 หลังจำหน่าย**

**8) ประเมินการทำงานของหัวใจห้องล่างซ้ายก่อนจำหน่าย** ด้วย echocardiography เพื่อวางแผนยาและประเมินความจำเป็นของ ICD ในภายหลัง"""}],
 "ref": ["สไลด์ อ.สุรพันธ์ พงศ์สุธนะ — STEMI 2017 / NSTEMI 2020 / Chronic coronary syndrome",
         "2017 ESC Guidelines for the management of AMI in patients presenting with ST-segment elevation"],
 "nl": ["2.3.9-3(1)"], "years": [], "_kind": "meq", "_set": "cardio"}]

OSCE = [{
 "id": "CAR-IHD-OSCE-01", "part": "OSCE/SAQ", "lec": "24/9", "lecture": "Ischemic heart diseases",
 "topic": "SAQ – แปลผล ECG และตัดสินใจเปิดหลอดเลือดสี่สถานการณ์",
 "station": "SAQ (เขียนตอบ) 10 นาที",
 "instruction": """ผู้ป่วยสี่รายมาด้วยเจ็บแน่นหน้าอก จงตอบคำถามท้ายตาราง

| ราย | อายุ/เพศ | ระยะเวลาอาการ | ECG | ข้อมูลเพิ่มเติม |
|---|---|---|---|---|
| **A** | ชาย 45 ปี | 90 นาที | ST elevation 2.5 mm ใน V2–V4 | อยู่ใน รพ. ที่มีห้องสวนหัวใจ |
| **B** | ชาย 36 ปี | 60 นาที | ST elevation 2 mm ใน V2–V3 ไม่มี LVH/LBBB | — |
| **C** | ชาย 60 ปี | 3 ชม. | ST depression 2 mm ใน V1–V3, T ส่วนปลายเป็นบวก, R สูงใน V1–V2 | — |
| **D** | หญิง 66 ปี | 5 ชม. | ST depression 1.5 mm ใน I, II, aVL, V4–V6 และ ST elevation ใน aVR | BP 84/52 mmHg, ยังเจ็บแม้ได้ไนเตรต |

1.1 แต่ละรายเข้าเกณฑ์ STEMI หรือไม่ เพราะเหตุใด (8 คะแนน)
1.2 ราย A ควรเปิดหลอดเลือดด้วยวิธีใด ภายในเวลาเท่าใด (3 คะแนน)
1.3 ราย C ต้องทำ ECG เพิ่มอะไร และถ้าผลเป็นบวกจะจัดการอย่างไร (4 คะแนน)
1.4 ราย D จัดอยู่ในความเสี่ยงระดับใด ต้องสวนหลอดเลือดภายในกี่ชั่วโมง และรูปแบบ ECG นี้บ่งชี้อะไร (5 คะแนน)""",
 "answer": """**1.1 เข้าเกณฑ์ STEMI หรือไม่ (8 คะแนน — รายละ 2 คะแนน)**

**ราย A — เข้าเกณฑ์ STEMI** ✓
ST elevation **2.5 mm ใน V2–V4** · ผู้ชายอายุ 45 ปี (≥ 40 ปี) เกณฑ์ V2–V3 คือ **≥ 2 mm** และ V4 ใช้เกณฑ์ลีดอื่นคือ **≥ 1 mm** — เกินทั้งคู่ และอยู่ใน **ลีดต่อเนื่องกัน** → **anterior STEMI**

**ราย B — ยังไม่เข้าเกณฑ์** ✗
ผู้ชาย **อายุ 36 ปี (< 40 ปี)** เกณฑ์ V2–V3 คือ **≥ 2.5 mm** แต่ได้เพียง **2 mm**
**แต่ห้ามสรุปว่าไม่ใช่ ACS** — ต้อง **ทำ ECG ซ้ำหรือ monitor ดู dynamic change**, **มองหา hyper-acute T wave** ซึ่งมาก่อน ST elevation, **เพิ่มลีด V7–V9**, และ **ส่ง hs-troponin ตาม algorithm 0h/1h**

**ราย C — เข้าเกณฑ์ STEMI (posterior MI) เมื่อยืนยันด้วยลีดหลัง** ✓
**ST depression ใน V1–V3 ร่วมกับ T ส่วนปลายเป็นบวก บ่งชี้การขาดเลือด** และ **R wave สูงใน V1–V2** คือภาพกลับด้านของ Q wave ด้านหลัง — เป็น **ST-segment elevation equivalent** ต้องยืนยันด้วย V7–V9

**ราย D — ไม่เข้าเกณฑ์ STEMI แต่เป็น NSTE-ACS ที่เสี่ยงสูงมาก** ✗ (ในแง่เกณฑ์ ST elevation)
**ST depression กระจายหลายลีด ร่วมกับ ST elevation ใน aVR** ไม่ใช่เกณฑ์ STEMI แต่เป็น **very-high-risk criterion ของ NSTE-ACS**

**1.2 ราย A — วิธีและเวลา (3 คะแนน)**
- **Primary PCI เป็นวิธีที่ดีที่สุด**
- **อยู่ในโรงพยาบาลที่ทำ PCI ได้ → เป้าหมาย FMC ถึง wire crossing ภายใน 60 นาที**
- (ถ้าต้องส่งต่อ เป้าหมายคือ **90 นาที** และถ้าคาดว่าเกิน **120 นาที** ให้ **ยาละลายลิ่มเลือดภายใน 10 นาทีหลังวินิจฉัย** แทน)
- **ข้ามห้องฉุกเฉินพาเข้าห้องสวนหัวใจโดยตรง ประหยัดเวลาได้ 20 นาที**

**1.3 ราย C — ECG เพิ่มเติมและการจัดการ (4 คะแนน)**
- **ต้องทำลีด V7–V9** (posterior leads)
- **เกณฑ์ที่ใช้ยืนยัน — ST elevation ≥ 0.5 mm ใน V7–V9**
- **ถ้าเป็นบวก ให้ถือว่าเป็น STEMI และเปิดหลอดเลือดทันที** ตามเวลาเป้าหมายเดียวกับ STEMI ทั่วไป — **ห้ามจัดเป็น NSTEMI แล้วรอ 24 ชั่วโมง** ซึ่งเป็นความผิดพลาดที่พบบ่อยที่สุดของผู้ป่วยกลุ่มนี้
- **ควรทำ V3R, V4R ด้วย** เพราะ posterior MI มักมาจาก RCA หรือ LCx และอาจมี RV infarction ร่วม

**1.4 ราย D — ระดับความเสี่ยง เวลา และความหมาย (5 คะแนน)**

**ระดับความเสี่ยง — very high risk** เข้าเกณฑ์ **สองข้อ**
1. **ระบบไหลเวียนไม่เสถียร** — BP 84/52 mmHg
2. **เจ็บหน้าอกดื้อต่อการรักษาด้วยยา** — ยังเจ็บแม้ได้ไนเตรต
3. และรูปแบบ ECG เองก็เป็นเกณฑ์ข้อที่สาม — **ST depression > 1 mm ใน ≥ 6 ลีด ร่วมกับ ST elevation ใน aVR**

**เวลา — Immediate invasive strategy ภายใน 2 ชั่วโมง (Class I C)**

**ความหมายของรูปแบบ ECG นี้** — **ST depression กระจายหลายลีดร่วมกับ ST elevation ใน aVR** สะท้อน **การขาดเลือดทั่วทั้งชั้น subendocardium** ซึ่งมักเกิดจาก
- **Left main coronary artery disease**
- **Proximal LAD occlusion**
- **Three-vessel disease**

ผู้ป่วยกลุ่มนี้ **มีอัตราตายสูงมาก** และมักต้อง **ผ่าตัด CABG มากกว่าทำ PCI** จึงต้องรีบสวนหลอดเลือดเพื่อทราบกายวิภาคและให้ทีม heart team ตัดสินใจ

**สิ่งที่ห้ามทำในราย D** — **ห้ามให้ยาละลายลิ่มเลือด** เพราะเป็น NSTE-ACS ซึ่งยาละลายลิ่มเลือดไม่มีประโยชน์และเพิ่มอันตราย""",
 "ref": ["สไลด์ อ.สุรพันธ์ — ESC 2017 STEMI ECG criteria / 2020 ESC NSTEACS Coronary revascularization"],
 "nl": ["2.3.9-3(1)"], "years": [], "_kind": "meq", "_set": "cardio"}]

LECTURE = {
 "lec": "24/9",
 "title": "Ischemic heart disease — ตั้งแต่ CCS ถึง STEMI",
 "subtitle": "atherosclerosis timeline และ plaque rupture · step approach และ pretest probability ของ CCS · ยาลดอาการกับยาที่ลดการตาย · นิยาม MI · เกณฑ์ ECG ของ STEMI และ posterior MI · เวลาเป้าหมายของการเปิดหลอดเลือด · ยาละลายลิ่มเลือด · hs-troponin 0h/1h · GRACE และความเร่งด่วนของการสวน · DAPT และผู้ป่วยที่ต้องกิน OAC · การป้องกันทุติยภูมิ",
 "objectives": [
   "อธิบายว่า CAD เป็นโรคเรื้อรังที่วนเข้าออกหลายระยะ และบอกได้ว่าทำไมคราบที่ตีบน้อยจึงทำให้เกิด MI",
   "ใช้ step approach และ pretest probability ตัดสินใจว่าจะตรวจอะไรในผู้ป่วย CCS",
   "แยกยาที่ลดอาการออกจากยาที่ลดเหตุการณ์และการตาย และเลือกยาให้ตรงกับโรคร่วม",
   "ใช้นิยาม universal definition แยก myocardial injury ออกจาก myocardial infarction",
   "จำเกณฑ์ ST elevation ที่ต่างกันตามลีด เพศ และอายุ และจับ posterior MI ด้วย V7–V9 ได้",
   "ตัดสินใจระหว่าง primary PCI กับยาละลายลิ่มเลือดจากเวลาเป้าหมาย และประเมินว่า reperfusion สำเร็จหรือไม่",
   "ใช้ hs-troponin algorithm 0h/1h และรู้ว่า biomarker ใดไม่ควรส่งแล้ว",
   "แบ่งความเสี่ยง NSTE-ACS และเลือกเวลาสวนหลอดเลือดภายใน 2 หรือ 24 ชั่วโมงได้ถูกต้อง",
   "วางแผนยาต้านเกล็ดเลือดในผู้ป่วยทั่วไปและในผู้ที่ต้องกินยาต้านการแข็งตัวของเลือดร่วม",
   "วางแผนการป้องกันทุติยภูมิหลัง MI รวมถึงการเลิกบุหรี่และ cardiac rehabilitation"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

path = os.path.join(BUILD, "data", "cardio.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "cardio": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | items %d | meq %d | osce %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE)))
print("cardio.json มี %d คาบ · %d bytes" % (len(data), os.path.getsize(path)))
