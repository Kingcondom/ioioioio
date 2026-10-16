#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""คาบ 24 Atrial fibrillation (อ.อภิชัย ปกวัฒนา) → data/cardio.json
ต้นฉบับ: Drive 1zK9eofxHl5ldCi-5IqIjyTStGVHYhlRO "AF for medical student 4th yr - update 16-NOV-2025"
โน้ตสไลด์: slides/af_notes.md · ข้อสอบคลัง Ward Drill คาบ 24 (21 ข้อ) ผูกเข้าท้ายสคริปต์"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from link_bank import link

NLN = ["2.3.9(1)", "B7.2.5(5)"]
SRC = "สไลด์ อ.อภิชัย — Atrial fibrillation (update พ.ย. 2025)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "CAR-AF-MCQ-%02d" % n
R = lambda p: ["สไลด์ อ.อภิชัย — " + p]

# ───────────────────────────── 1
sec("cardio-af-01", "AF คืออะไร และทำไมต้องสนใจ",
    "หัวใจเต้นผิดจังหวะที่พบบ่อยที่สุด · เสี่ยงตาย 2 เท่า stroke 5 เท่า", 7,
"""### นิยาม
**Atrial fibrillation (AF)** คือภาวะหัวใจเต้นผิดจังหวะที่ **พบบ่อยที่สุด** หัวใจห้องบนเต้นสั่นพลิ้วอย่างไม่เป็นระเบียบ จน **ห้องบนกับห้องล่างทำงานไม่ประสานกัน** หัวใจห้องล่างจึงเต้นไม่สม่ำเสมอ อาจช้า เร็ว หรือไม่เป็นจังหวะ

### พบบ่อยแค่ไหน (สไลด์)
| กลุ่ม | ความชุก |
|---|---|
| ประชากรทั่วไป | **1–2%** |
| อายุ 40–50 ปี | < 0.5% |
| อายุ > 80 ปี | **5–15%** |
| โอกาสเป็นตลอดชีวิต | **25%** (หนึ่งในสี่) |
ชายพบมากกว่าหญิง · ทั่วโลกมีผู้ป่วยราว 43.6 ล้านคน (2016)

### ผลที่ตามมา — ทำไม AF ไม่ใช่แค่ใจสั่น
| ผลลัพธ์ | ขนาดของปัญหา |
|---|---|
| **การตาย** | เพิ่ม **1.5–3.5 เท่า** (สรุปท้ายสไลด์: ×2) |
| **Stroke** | **20–30% ของ ischemic stroke ทั้งหมด** · เสี่ยงเพิ่ม **5 เท่า** |
| Heart failure | 20–30% ของผู้ป่วย AF |
| Dementia | HR 1.6 |
| ซึมเศร้า | 16–20% |
| คุณภาพชีวิตแย่ลง | > 60% |
| นอนโรงพยาบาล | 10–40% ต่อปี |

### กลไกที่ทำให้เกิด stroke
ห้องบนที่สั่นพลิ้วไม่บีบตัว → เลือดไหลช้าและค้าง โดยเฉพาะใน **left atrial appendage (LAA)** ซึ่งเป็นกระเปาะปลายตัน → **ลิ่มเลือดก่อตัวที่ LAA มากที่สุด** → หลุดไปอุดหลอดเลือดสมอง stroke จาก AF จึงมัก **รุนแรงและเป็นก้อนใหญ่** กว่า stroke จากหลอดเลือดเล็ก

### กรอบของทั้งคาบ: **Dx AF → ? → Rx**
1. **วินิจฉัย** ด้วย ECG
2. **ประเมิน** ระยะ อาการ ความเสี่ยง stroke และโรคร่วม
3. **รักษา** ตาม **ABC pathway** — **A**void stroke · **B**etter symptom control · **C**omorbidities
""",
    ["AF = arrhythmia ที่พบบ่อยที่สุด · ประชากร 1–2% · > 80 ปี 5–15% · lifetime risk 25%",
     "AF เพิ่มการตายราว 2 เท่า และ stroke 5 เท่า (20–30% ของ ischemic stroke)",
     "ลิ่มเลือดเกิดที่ left atrial appendage มากที่สุด",
     "กรอบรักษา: ABC — Avoid stroke · Better symptom · Comorbidities"],
    [mcq(N(1), "Compared with people in sinus rhythm, approximately how much does atrial fibrillation increase the risk of ischaemic stroke?",
         ["No increase", "About 1.2-fold", "About 5-fold", "About 50-fold", "Only if the patient is symptomatic"], 2,
         "สไลด์สรุป: AF เพิ่ม **stroke ราว 5 เท่า** และคิดเป็น **20–30% ของ ischemic stroke ทั้งหมด** ส่วนการตายเพิ่มราว **2 เท่า** (1.5–3.5)\n\nความเสี่ยงนี้ **ไม่ขึ้นกับว่ามีอาการหรือไม่** — AF ที่ไม่มีอาการ (silent) ก็ทำให้เกิด stroke ได้เท่ากัน จึงต้องประเมินความเสี่ยง stroke ทุกราย",
         "AF: stroke ×5 · ตาย ×2", "AF outcomes", R("Overview of AF"), NLN + ["2.2.39"]),
     mcq(N(2), "Where in the heart do thrombi most commonly form in patients with atrial fibrillation?",
         ["Right ventricular apex", "Left atrial appendage", "Aortic root", "Left ventricular outflow tract", "Coronary sinus"], 1,
         "สไลด์ LAA closure: **left atrial appendage เป็นตำแหน่งเกิดลิ่มเลือดบ่อยที่สุด** เพราะเป็นกระเปาะปลายตัน เมื่อห้องบนไม่บีบตัว เลือดในนั้นจะไหลช้าและค้าง\n\nนี่จึงเป็นเหตุผลของการรักษาด้วย **LAA occlusion** ในผู้ป่วยที่กินยาต้านการแข็งตัวของเลือดไม่ได้",
         "ลิ่มเลือดใน AF เกิดที่ LAA มากที่สุด", "Thrombus site in AF", R("LAA closure")),
    ])

# ───────────────────────────── 2
sec("cardio-af-02", "โรคที่สัมพันธ์กับ AF — ต้องหาสาเหตุเสมอ",
    "โรคหัวใจ (HT, HF, ลิ้น, ASD, CAD) และนอกหัวใจ (อ้วน DM COPD CKD ไทรอยด์เป็นพิษ) รวมถึงสุรา", 7,
"""### โรคที่สัมพันธ์กับ AF (สไลด์)
| โรคหัวใจและหลอดเลือด | โรคนอกหัวใจ |
|---|---|
| **Hypertension** (พบบ่อยที่สุด) | **Obesity** |
| **Heart failure** | **Diabetes** |
| **Valvular heart disease** (โดยเฉพาะ mitral stenosis จากรูมาติก) | **COPD** |
| **Congenital heart disease — ASD** | **CKD** |
| **Coronary artery disease** | **Hyperthyroidism** |

### กลไกร่วม
โรคเหล่านี้ทำให้ **ห้องบนซ้ายขยายและเกิดพังผืด (atrial remodeling)** — จากความดันในห้องบนสูง (HT, HF, MS) การอักเสบ หรือฮอร์โมน (ไทรอยด์) → การนำไฟฟ้าในห้องบนแตกเป็นวงเล็ก ๆ หลายวง → AF และ **AF ที่เป็นนานก็ยิ่งทำให้ห้องบนเสื่อม** (AF begets AF)

### สาเหตุที่แก้ได้ ซึ่งออกสอบบ่อย
| ภาวะ | เบาะแส |
|---|---|
| **Hyperthyroidism / thyroid storm** | น้ำหนักลด มือสั่น ขี้ร้อน · ไข้สูง สับสน HF + AF เร็วมาก = storm |
| **สุรา (holiday heart syndrome)** | ใจสั่นหลังดื่มหนักช่วงวันหยุด AF หายเองได้ |
| **Mitral stenosis** | เสียง diastolic rumble · ห้องบนซ้ายโต · ใช้ warfarin ไม่ใช้ NOAC |
| ปอดอักเสบ หลังผ่าตัด PE | AF ที่เกิดจากภาวะเฉียบพลัน |
| Sleep apnea | อ้วน กรน ง่วงกลางวัน |

**การตรวจเบื้องต้นในผู้ป่วยใจสั่น** — **12-lead ECG และ thyroid function test** เสมอ ร่วมกับ echocardiography เพื่อดูลิ้นหัวใจและขนาดห้องหัวใจ
""",
    ["AF สัมพันธ์กับ HT · HF · ลิ้นหัวใจ · ASD · CAD · อ้วน · DM · COPD · CKD · ไทรอยด์เป็นพิษ",
     "ใจสั่น → 12-lead ECG + TFT ก่อนเสมอ",
     "Holiday heart = AF หลังดื่มสุราหนัก",
     "Thyroid storm: ไข้ สับสน HF + AF เร็ว + TSH กด FT4 สูง"],
    [mcq(N(3), "A 34-year-old woman with new-onset atrial fibrillation has had 4 kg weight loss, tremor and heat intolerance. Which blood test must be checked first to identify a reversible cause?",
         ["Serum troponin", "Thyroid function tests (TSH, free T4)", "D-dimer", "Serum lipase", "Antinuclear antibody"], 1,
         "สไลด์จัด **hyperthyroidism** เป็นหนึ่งในโรคนอกหัวใจที่สัมพันธ์กับ AF — ฮอร์โมนไทรอยด์เพิ่มการกระตุ้น β-adrenergic และทำให้ refractory period ของห้องบนสั้นลง\n\nผู้ป่วยมี **น้ำหนักลด มือสั่น ขี้ร้อน** → ตรวจ **TSH และ free T4** การรักษาไทรอยด์ทำให้ AF หายได้ ระหว่างนั้นใช้ **β-blocker** คุมอัตราการเต้นและบรรเทาอาการ",
         "AF ใหม่ทุกราย → ตรวจไทรอยด์", "Hyperthyroidism and AF", R("Diseases related to AF"), NLN + ["2.3.4(9)", "2.1.36"]),
    ])

# ───────────────────────────── 3
sec("cardio-af-03", "อาการของ AF — stable หรือ unstable",
    "ไม่มีอาการ · มีอาการแต่ hemodynamics คงที่ · หรือ unstable ที่ต้องช็อกไฟฟ้าทันที", 7,
"""### สามกลุ่มอาการ (สไลด์)
| กลุ่ม | ลักษณะ |
|---|---|
| **1. Asymptomatic** | ไม่มีอาการ hemodynamics คงที่ — พบโดยบังเอิญ |
| **2. Symptomatic, stable** | **แน่น/เจ็บหน้าอก ทนออกแรงไม่ได้ เวียนศีรษะ เป็นลม นอนไม่หลับ** |
| **3. Symptomatic, unstable** | **syncope · hypotension · acute HF/pulmonary edema · เจ็บหน้าอกต่อเนื่อง · cardiogenic shock** |

**ทำไมมีอาการ** — AF ทำให้ **เสีย atrial kick** (ห้องบนไม่บีบเติมเลือดช่วงท้าย diastole ซึ่งเติมได้ราว 20–30%) ร่วมกับ **หัวใจเต้นเร็วจน diastole สั้น** → ห้องล่างเติมเลือดไม่พอ → **cardiac output ลด** ผู้ป่วยที่หัวใจแข็ง (LVH, HFpEF, MS) จึงทรุดเร็วที่สุด

### ตรวจร่างกาย
- **ชีพจรไม่สม่ำเสมอแบบไม่มีรูปแบบ (irregularly irregular)**
- **Pulse deficit** — อัตราที่ฟังหัวใจ **มากกว่า** ชีพจรที่คลำได้ เพราะบางจังหวะเติมเลือดไม่พอจนแรงดันไม่ถึงข้อมือ
- ไม่มี a wave ใน JVP · ความดังของ S1 ไม่เท่ากัน

### กับดักบนจอ monitor
ผู้ป่วยรู้สึกตัวดี พูดได้ แต่ **คลำชีพจรไม่ได้** ขณะที่ monitor เป็น AF เร็ว → **ตรวจชีพจรและสาย monitor ใหม่ก่อน** ไม่ใช่ทำ CPR เพราะคนที่ cardiac arrest พูดไม่ได้

**Unstable → synchronized electrical cardioversion ทันที** (หัวข้อ 10)
""",
    ["AF stable: แน่นหน้าอก ทนออกแรงไม่ได้ เวียนศีรษะ · unstable: syncope, hypotension, pulmonary edema, chest pain, shock",
     "อาการเกิดจากเสีย atrial kick + diastole สั้น → CO ลด",
     "Irregularly irregular pulse + pulse deficit",
     "Unstable AF → synchronized cardioversion"],
    [mcq(N(4), "A 68-year-old man has AF at 170/min. He is confused, BP 76/44 mmHg, with cold extremities and crackles to the mid-zones. Which features make this AF 'haemodynamically unstable'?",
         ["Age over 65 alone", "Hypotension, altered mental status and acute pulmonary oedema",
          "An irregularly irregular pulse", "Absent P waves on the ECG", "A ventricular rate above 100/min alone"], 1,
         "สไลด์แบ่ง **unstable** เป็น **syncope, hypotension, acute HF/pulmonary edema, ongoing chest pain และ cardiogenic shock** ผู้ป่วยรายนี้มี **ความดันต่ำ สับสน มือเท้าเย็น และ pulmonary edema** → ต้อง **synchronized electrical cardioversion ทันที**\n\nชีพจรไม่สม่ำเสมอ ไม่มี P wave และอัตราเร็วเกิน 100 เป็นลักษณะของ AF ทั่วไป ไม่ได้ทำให้เป็น unstable",
         "Unstable = hypotension · ซึม · pulmonary edema · chest pain · shock", "Unstable AF", R("Symptom of AF"), NLN + ["2.1.36", "2.1.5"]),
    ])

# ───────────────────────────── 4
sec("cardio-af-04", "วินิจฉัยด้วย ECG — สามเกณฑ์ และอุปกรณ์คัดกรอง",
    "\"ECG must be done!!!\" — R-R ไม่สม่ำเสมอ · ไม่มี P wave ชัด · atrial rate > 300", 8,
"""### หลักของอาจารย์: **ECG must be done!!!**
การวินิจฉัย AF ต้องเห็นจาก ECG เสมอ ชีพจรไม่สม่ำเสมออย่างเดียวยังไม่พอ เพราะ PAC/PVC บ่อย ๆ หรือ multifocal atrial tachycardia ก็ทำให้ชีพจรไม่สม่ำเสมอได้

### สามเกณฑ์
| เกณฑ์ | เหตุผล |
|---|---|
| **1. Irregular R-R interval** (irregularly irregular) | AV node รับสัญญาณจากห้องบนแบบสุ่ม |
| **2. No distinct P wave** | ห้องบนไม่ได้ depolarize พร้อมกันเป็นก้อนเดียว จึงเห็นเป็น **f wave** ที่ฐานแทน |
| **3. Atrial rate > 300 bpm** | วงไฟฟ้าเล็ก ๆ หลายวงในห้องบน (มักเป็น 350–600) |

- **Coarse AF** — f wave ใหญ่ ชัด (มักพบในห้องบนโต เช่น MS)
- **Fine AF** — f wave เล็กจนแทบเป็นเส้นเรียบ
- QRS มักแคบ (ถ้ากว้างให้คิดถึง bundle branch block หรือ **pre-excitation**)

### เครื่องมือคัดกรอง
| ชนิด | เกณฑ์วินิจฉัย |
|---|---|
| **12-lead ECG** | เห็น AF → **วินิจฉัยได้เลย** |
| **ECG 1–2 lead** (เช่น นาฬิกาหรืออุปกรณ์พกพาที่บันทึก ECG) | AF ต่อเนื่อง **> 30 วินาที** → วินิจฉัย |
| **อุปกรณ์ที่ไม่ใช่ ECG** (เช่น PPG ในนาฬิกา) | **ต้องยืนยันด้วยอุปกรณ์ที่เป็น ECG** |

### แยกจาก atrial flutter และ sick sinus
- **Atrial flutter** — คลื่น **sawtooth** สม่ำเสมอราว 300/นาที มักนำลง 2:1 → ชีพจร **150 สม่ำเสมอ** · ความเสี่ยง stroke และการให้ยาต้านการแข็งตัวคิดเหมือน AF
- **Tachy-brady syndrome** — ผู้สูงอายุที่ AF เร็วสลับกับหยุดเต้นนาน = **sick sinus syndrome** ร่วมกับ paroxysmal AF → ยาคุมอัตราอาจทำให้ช้าจนเป็นลม ต้องใส่ pacemaker ก่อน
""",
    ["ECG must be done — วินิจฉัย AF ด้วย ECG เสมอ",
     "สามเกณฑ์: irregular R-R · no distinct P · atrial rate > 300",
     "12-lead เห็น AF = dx · ECG 1–2 lead ต้อง > 30 วินาที · PPG ต้องยืนยันด้วย ECG",
     "Flutter: sawtooth · 2:1 → ชีพจร 150 สม่ำเสมอ"],
    [mcq(N(5), "Which combination of ECG findings fulfils the lecture's three criteria for atrial fibrillation?",
         ["Regular R-R, sawtooth flutter waves, atrial rate 300/min", "Irregular R-R, no distinct P waves, atrial rate above 300/min",
          "Regular R-R, inverted P waves, rate 150/min", "Irregular R-R, three or more P-wave morphologies, atrial rate 110/min", "Wide QRS, AV dissociation, rate 180/min"], 1,
         "สามเกณฑ์ของสไลด์: **(1) irregular R-R interval (2) no distinct P wave (3) atrial rate > 300 bpm**\n\nข้ออื่น: regular + sawtooth = **atrial flutter** · P wave สามรูปแบบขึ้นไปและ rate ราว 100–130 = **multifocal atrial tachycardia** (ผู้ป่วย COPD) · wide QRS + AV dissociation = **ventricular tachycardia**",
         "AF: R-R ไม่สม่ำเสมอ + ไม่มี P + atrial rate > 300", "ECG criteria of AF", R("How to diagnosis"), NLN + ["3.1.12", "B7.3(3)b"]),
     mcq(N(6), "A 63-year-old man's smartwatch (photoplethysmography only, no ECG function) alerts him to 'possible AF'. He feels well. What is the next step?",
         ["Start anticoagulation immediately based on the alert", "Ignore the alert because smartwatches are not validated",
          "Confirm with an ECG-based recording (12-lead ECG or ambulatory ECG)", "Start amiodarone", "Arrange electrical cardioversion"], 2,
         "สไลด์ screening tool: **อุปกรณ์ที่ไม่ใช่ ECG ต้องยืนยันด้วยอุปกรณ์ที่เป็น ECG** ก่อนวินิจฉัย\n\n**12-lead ECG** ที่เห็น AF วินิจฉัยได้ทันที ส่วน **ECG 1–2 lead ต้องเห็น AF นานกว่า 30 วินาที** · การเริ่มยาต้านการแข็งตัวของเลือดโดยไม่มีการยืนยันเสี่ยงเลือดออกโดยไม่จำเป็น",
         "PPG/smartwatch → ยืนยันด้วย ECG ก่อนเสมอ", "AF screening", R("Screening tool (update 2024)"), NLN + ["3.1.12"]),
    ], NLN + ["3.1.12", "B7.3(3)b"])

# ───────────────────────────── 5
sec("cardio-af-05", "ระยะของ AF และการประเมินแรกรับ",
    "silent · paroxysmal · persistent · long-standing · permanent — แล้วประเมิน EHRA onset HF stroke และโรคพื้นฐาน", 7,
"""### ระยะของ AF (สไลด์)
| ระยะ | นิยาม |
|---|---|
| **Silent** | **ไม่มีอาการ** พบโดยบังเอิญ |
| **Paroxysmal** | **เป็น ๆ หาย ๆ** หายเองหรือรักษาจนหาย มักน้อยกว่า 48 ชม. **ไม่เกิน 7 วัน** |
| **Persistent** | เป็นต่อเนื่อง **นานกว่า 7 วัน** |
| **Long-standing persistent** | เป็นต่อเนื่อง **นานกว่า 1 ปี** แต่ยังตั้งใจจะทำ rhythm control |
| **Permanent** | ตกลงร่วมกันว่า **จะไม่พยายามทำให้กลับเป็นจังหวะปกติอีก** — เน้นคุมอัตราอย่างเดียว |

**ข้อสำคัญ** — ระยะไม่ได้เปลี่ยนความเสี่ยง stroke · paroxysmal AF ก็ต้องประเมิน CHA₂DS₂-VASc และให้ยาต้านการแข็งตัวเหมือนกัน

### ประเมินแรกรับ
| สิ่งที่ประเมิน | เพื่ออะไร |
|---|---|
| **EHRA score** | ระดับอาการ → ตัดสินใจเรื่อง rhythm control |
| **ความเสี่ยง stroke** | ตัดสินใจเรื่องยาต้านการแข็งตัวของเลือด |
| **Onset > 48 ชม. หรือไม่** | ถ้าเกินหรือไม่ทราบ → ห้าม cardioversion ทันทีโดยไม่ได้ยาต้านการแข็งตัวก่อน (เสี่ยงลิ่มเลือดหลุด) |
| **Heart failure** | เลือกยาคุมอัตรา |
| **Stroke หรือ TIA เดิม** | ได้ 2 คะแนน = เสี่ยงสูง |
| **โรคพื้นฐาน** | หาสาเหตุที่แก้ได้ (หัวข้อ 2) |

### EHRA score
| Class | ความหมาย |
|---|---|
| **I** | ไม่มีอาการ |
| **II** | อาการเล็กน้อย **ไม่กระทบกิจวัตร** |
| **III** | อาการรุนแรง **กระทบกิจวัตร** |
| **IV** | อาการ **รุนแรงจนต้องหยุดกิจวัตร** |
""",
    ["Paroxysmal ≤ 7 วัน (มัก < 48 ชม.) · persistent > 7 วัน · long-standing > 1 ปี · permanent = ไม่พยายามกลับ sinus แล้ว",
     "ระยะไม่เปลี่ยนความเสี่ยง stroke",
     "EHRA I ไม่มีอาการ · II ไม่กระทบกิจวัตร · III กระทบกิจวัตร · IV หยุดกิจวัตร",
     "Onset > 48 ชม./ไม่ทราบ → ต้อง anticoagulate ก่อน cardioversion"],
    [mcq(N(7), "A patient has had continuous atrial fibrillation for 3 weeks. Which stage is this?",
         ["Paroxysmal", "Persistent", "Long-standing persistent", "Permanent", "Silent"], 1,
         "สไลด์: **paroxysmal = เป็น ๆ หาย ๆ ไม่เกิน 7 วัน** · **persistent = นานกว่า 7 วัน** · **long-standing persistent = นานกว่า 1 ปี** · **permanent = ตัดสินใจไม่ทำให้กลับเป็นจังหวะปกติแล้ว**\n\n3 สัปดาห์ต่อเนื่อง → **persistent AF**",
         "> 7 วัน = persistent · > 1 ปี = long-standing", "Stages of AF", R("Stage of AF")),
     mcq(N(8), "A woman with AF reports palpitations and fatigue that stop her from doing her usual housework. What is her EHRA symptom class?",
         ["EHRA I", "EHRA II", "EHRA III", "EHRA IV", "EHRA cannot be assessed without Holter"], 2,
         "EHRA score: **I ไม่มีอาการ · II mild ไม่กระทบกิจวัตร · III severe กระทบกิจวัตร · IV disabling หยุดกิจวัตร**\n\nอาการ **กระทบงานบ้านตามปกติ** = **EHRA III** · ถ้าทำกิจวัตรไม่ได้เลยจะเป็น IV",
         "EHRA III = กระทบกิจวัตร · IV = หยุดกิจวัตร", "EHRA score", R("Initial evaluation of AF")),
    ])

# ───────────────────────────── 6
sec("cardio-af-06", "A — ประเมินความเสี่ยง stroke: CHA₂DS₂-VASc และ CHA₂DS₂-VA",
    "หาคนเสี่ยงต่ำก่อน แล้วให้ยาต้านการแข็งตัวคนที่เหลือ · ESC 2024 ตัดคะแนนเพศออก", 10,
"""### CHA₂DS₂-VASc (สไลด์)
| ตัวอักษร | ปัจจัย | คะแนน |
|---|---|---|
| **C** | Congestive heart failure | 1 |
| **H** | Hypertension | 1 |
| **A₂** | Age **≥ 75** | **2** |
| **D** | Diabetes | 1 |
| **S₂** | Stroke / TIA / thromboembolism | **2** |
| **V** | Vascular disease (MI, PAD, aortic plaque) | 1 |
| **A** | Age **65–74** | 1 |
| **Sc** | Sex category — **หญิง** | 1 |
คะแนนเต็ม 9 · ความเสี่ยง stroke ต่อปีเพิ่มตามคะแนน เช่น 0 = 0% · 1 = 1.3% · 2 = 2.2% · 4 = 4.0% · 9 = 15.2%

### ขั้นตอน A ใน ABC pathway (ESC 2020)
1. **หาคนเสี่ยงต่ำ** — **CHA₂DS₂-VASc 0 ในชาย หรือ 1 ในหญิง** → ไม่ต้องให้ยา
2. **ให้การป้องกัน stroke** เมื่อ **≥ 1 ในชาย หรือ ≥ 2 ในหญิง** พร้อม **ประเมินความเสี่ยงเลือดออกและแก้ปัจจัยที่แก้ได้** (ความดันสูงที่คุมไม่ได้ ยา NSAID/aspirin ที่ไม่จำเป็น สุรา INR แกว่ง)
3. **เลือกยา** — NOAC หรือ warfarin ที่คุม INR ได้ดี (TTR สูง)

**ความเสี่ยงเลือดออกสูงไม่ใช่เหตุผลให้งดยา** แต่เป็นสัญญาณให้แก้ปัจจัยเสี่ยงและติดตามใกล้ชิด

### ESC 2024 — CHA₂DS₂-VA
แนวทางใหม่ **ตัดคะแนนเพศหญิงออก** เพราะเพศหญิงเพิ่มความเสี่ยงเฉพาะเมื่อมีปัจจัยอื่นร่วม → เกณฑ์เดียวกันทั้งสองเพศ
- **CHA₂DS₂-VA ≥ 2** → แนะนำให้ยาต้านการแข็งตัวของเลือด
- **= 1** → ควรพิจารณา

### ไม่ต้องคิดคะแนนก็รู้ว่าเสี่ยงสูง
- **เคยเป็น stroke หรือ TIA**
- **อายุ ≥ 75 ปี**
คะแนนเป็นเพียงเครื่องมือจากข้อมูลประชากร (CHADS₂, CHA₂DS₂-VASc, mCHA₂DS₂-VASc, CHA₂DS₂-VA, ATRIA) — **คะแนนสูง = เสี่ยงสูงกว่าคนทั่วไป → พิจารณาป้องกัน stroke**

**Aspirin ไม่ใช่ยาป้องกัน stroke ใน AF** — ได้ผลน้อยแต่เลือดออกใกล้เคียงยาต้านการแข็งตัว
""",
    ["CHA₂DS₂-VASc: C1 H1 A₂2 D1 S₂2 V1 A1 Sc1 (หญิง) · เต็ม 9",
     "เสี่ยงต่ำ: 0 ชาย / 1 หญิง · ให้ OAC: ≥ 1 ชาย / ≥ 2 หญิง",
     "ESC 2024 CHA₂DS₂-VA ตัดเพศ · ≥ 2 แนะนำ OAC",
     "เคย stroke/TIA หรืออายุ ≥ 75 = เสี่ยงสูงทันที",
     "Bleeding risk สูง → แก้ปัจจัย ไม่ใช่เหตุผลงดยา · aspirin ไม่ใช่ยาป้องกัน stroke ใน AF"],
    [mcq(N(9), "A 72-year-old woman with hypertension and type 2 diabetes has non-valvular AF. What is her CHA2DS2-VASc score?",
         ["2", "3", "4", "5", "6"], 2,
         "คิดทีละตัว: **H** hypertension 1 · **D** diabetes 1 · **A** อายุ 65–74 = 1 · **Sc** เพศหญิง 1 → **รวม 4**\n\nอายุ 72 ยังไม่ถึง 75 จึงได้ 1 ไม่ใช่ 2 · ความเสี่ยง stroke ราว **4% ต่อปี** → ให้ยาต้านการแข็งตัวของเลือด\n\nถ้าใช้ **CHA₂DS₂-VA (ESC 2024)** จะได้ 3 ซึ่งก็ยังเกิน 2 → ให้ยาเหมือนกัน",
         "อายุ 65–74 = 1 · ≥ 75 = 2 · หญิง +1 ใน VASc", "CHA2DS2-VASc calculation", R("CHA2DS2-VASc table")),
     mcq(N(10), "A 55-year-old man with paroxysmal AF has no hypertension, diabetes, heart failure, vascular disease or prior stroke. What is the recommendation for stroke prevention?",
         ["Warfarin INR 2–3", "Apixaban 5 mg twice daily", "Aspirin 81 mg daily", "No antithrombotic therapy; reassess risk factors periodically", "Dual antiplatelet therapy"], 3,
         "CHA₂DS₂-VASc = **0 ในชาย = กลุ่มเสี่ยงต่ำ** (ขั้นที่ 1 ของ ABC pathway) → **ไม่ต้องให้ยาต้านลิ่มเลือด**\n\n**Aspirin ไม่ใช้ป้องกัน stroke ใน AF** · ต้อง **ประเมินซ้ำเป็นระยะ** เพราะเมื่ออายุ 65 หรือเกิดความดันสูง คะแนนจะเปลี่ยน\n\nระยะ paroxysmal ไม่ได้ทำให้ความเสี่ยงต่างจาก persistent",
         "CHA₂DS₂-VASc 0 ชาย/1 หญิง → ไม่ต้องให้ยา · ประเมินซ้ำ", "Low-risk AF", R("ABC pathway — A")),
     mcq(N(11), "Under the ESC 2024 approach (CHA2DS2-VA), what is the main change from CHA2DS2-VASc?",
         ["Age is no longer counted", "Female sex is no longer scored", "Prior stroke now scores 3", "Heart failure is removed", "Diabetes scores 2"], 1,
         "สไลด์ ESC 2024 — **new definition of stroke risk evaluation: CHA₂DS₂-VA** ตัด **Sc (sex category)** ออก เพราะเพศหญิงเพิ่มความเสี่ยงเมื่อมีปัจจัยอื่นอยู่แล้วเท่านั้น\n\nเกณฑ์จึงเหมือนกันทั้งสองเพศ: **≥ 2 แนะนำให้ OAC**, **1 ควรพิจารณา**",
         "CHA₂DS₂-VA = ตัดคะแนนเพศ", "ESC 2024 CHA2DS2-VA", R("ESC 2024")),
    ], NLN + ["2.2.39", "B3.2.6(1)"])

# ───────────────────────────── 7
sec("cardio-af-07", "เลือกยาต้านการแข็งตัว: warfarin หรือ NOAC",
    "NOAC สะดวกกว่าแต่ต้องสั่งขนาดให้ถูก · mitral stenosis และลิ้นเทียมใช้ warfarin เท่านั้น · ยาแก้ฤทธิ์และ LAA occlusion", 9,
"""### ยาที่มีให้เลือก
| กลุ่ม | ยา | กลไก |
|---|---|---|
| **VKA** | **Warfarin** — เป้า **INR 2.0–3.0** | ยับยั้งการกระตุ้น vitamin K → ลดการสร้าง **factor II, VII, IX, X** |
| **NOAC** | **Dabigatran** | **direct thrombin inhibitor** |
| | **Rivaroxaban · Apixaban · Edoxaban** | **anti-factor Xa** (ชื่อลงท้าย -xaban) |

### Warfarin กับ NOAC (สไลด์)
| | **Warfarin** | **NOAC** |
|---|---|---|
| การติดตาม | **ต้องเจาะ INR** | ไม่ต้อง |
| อาหาร | **ผักใบเขียวและอาหารรบกวน** | ไม่รบกวน |
| ราคา | **ถูก** | แพง |
| ยาแก้ฤทธิ์ | **vitamin K, FFP** | ยาจำเพาะ (แพง) · **ส่วนประกอบของเลือดไม่ได้ผล** |

### ใครต้องใช้ warfarin เท่านั้น
- **Moderate–severe mitral stenosis** (มักจากรูมาติก) — ที่ไทยพบบ่อย
- **ลิ้นหัวใจเทียมชนิดโลหะ (mechanical valve)**
NOAC ไม่มีหลักฐานหรือเกิดลิ่มเลือดมากกว่าในสองกลุ่มนี้ จึงเรียก AF อื่นทั้งหมดว่า "non-valvular AF" ที่ใช้ NOAC ได้

### Key ของอาจารย์: **NOAC ต้องสั่งขนาดให้เหมาะสม**
ขนาดที่มีในโรงพยาบาล — dabigatran 75/110/150 มก. · rivaroxaban 2.5/10/15/20 มก. · apixaban 2.5/5 มก. · edoxaban 30/60 มก.
ตัวอย่างเกณฑ์ลดขนาด (ตามฉลากยา)
| ยา | ขนาดปกติ | ลดขนาดเมื่อ |
|---|---|---|
| Apixaban | 5 มก. วันละ 2 ครั้ง | **2.5 มก. วันละ 2 ครั้ง** ถ้ามี 2 ใน 3: อายุ ≥ 80 · น้ำหนัก ≤ 60 กก. · Cr ≥ 1.5 |
| Rivaroxaban | 20 มก. วันละครั้งพร้อมอาหาร | **15 มก.** ถ้า CrCl 15–49 |
| Edoxaban | 60 มก. วันละครั้ง | **30 มก.** ถ้า CrCl 15–50 หรือ น้ำหนัก ≤ 60 กก. |
| Dabigatran | 150 มก. วันละ 2 ครั้ง | **110 มก. วันละ 2 ครั้ง** ในผู้สูงอายุมาก หรือเสี่ยงเลือดออก · ขับทางไตมาก ระวังไตเสื่อม |
**การให้ขนาดต่ำโดยไม่เข้าเกณฑ์ = ป้องกัน stroke ไม่ได้**

### ยาแก้ฤทธิ์ (สไลด์)
| ยา | ยาแก้ฤทธิ์ |
|---|---|
| Warfarin | **vitamin K, FFP** (หรือ PCC) |
| Dabigatran | **Idarucizumab** |
| -xaban | **PCC** (หรือ andexanet alfa ถ้ามี) |

### ทางเลือกที่ไม่ใช่ยา
**LAA occlusion/closure** — ปิดกระเปาะที่เกิดลิ่มเลือดบ่อยที่สุด สำหรับผู้ป่วยที่ใช้ยาต้านการแข็งตัวระยะยาวไม่ได้
""",
    ["Warfarin INR 2–3 · dabigatran = thrombin inhibitor · -xaban = anti-Xa",
     "MS ปานกลาง–รุนแรง หรือ mechanical valve → warfarin เท่านั้น",
     "NOAC ต้องสั่งขนาดให้ถูก — ขนาดต่ำเกินเกณฑ์ป้องกัน stroke ไม่ได้",
     "Antidote: warfarin → vit K/FFP · dabigatran → idarucizumab · -xaban → PCC",
     "ใช้ OAC ไม่ได้ → LAA occlusion"],
    [mcq(N(12), "Which anticoagulant's effect is reversed specifically by idarucizumab?",
         ["Warfarin", "Apixaban", "Rivaroxaban", "Dabigatran", "Enoxaparin"], 3,
         "สไลด์ antidote: **dabigatran → idarucizumab** (monoclonal antibody fragment ที่จับ dabigatran โดยตรง) · **-xaban → PCC** · **warfarin → vitamin K หรือ FFP**\n\nเหตุผลที่ส่วนประกอบของเลือดใช้ไม่ได้กับ NOAC: ยายังอยู่ในเลือดและยับยั้ง factor ที่เติมเข้าไปใหม่ได้ทันที",
         "Dabigatran → idarucizumab", "NOAC reversal", R("Antidote for OAC"), NLN + ["B2.4(3)"]),
     mcq(N(13), "A 78-year-old woman weighing 55 kg with non-valvular AF has serum creatinine 1.2 mg/dL. Which apixaban dose is appropriate?",
         ["2.5 mg twice daily", "5 mg twice daily", "5 mg once daily", "10 mg twice daily", "Apixaban is contraindicated"], 1,
         "เกณฑ์ลดขนาด apixaban เป็น 2.5 มก. วันละ 2 ครั้ง ต้องมี **2 ใน 3**: **อายุ ≥ 80 · น้ำหนัก ≤ 60 กก. · Cr ≥ 1.5 มก./ดล.**\n\nผู้ป่วยมีเพียง **ข้อเดียว (น้ำหนัก 55)** → ใช้ **ขนาดปกติ 5 มก. วันละ 2 ครั้ง**\n\nKey ของอาจารย์: **NOAC ต้องสั่งขนาดให้เหมาะสม** — การลดขนาดโดยไม่เข้าเกณฑ์ทำให้ป้องกัน stroke ไม่ได้",
         "Apixaban ลดขนาดเมื่อเข้า 2 ใน 3 (≥ 80 ปี · ≤ 60 กก. · Cr ≥ 1.5)", "NOAC dosing", R("Key – NOAC must prescribed with appropriate dose"), NLN + ["B2.4(3)"]),
    ], NLN + ["B2.4(3)"])

# ───────────────────────────── 8
sec("cardio-af-08", "Warfarin ในชีวิตจริง — ปรับขนาดตาม INR และจัดการ INR สูง",
    "ถามวิธีกินยาก่อนเปลี่ยนขนาด · คิดเป็นขนาดต่อสัปดาห์ · INR ±0.5 → ปรับ ±10–20%", 10,
"""### ช่วงเป้าแคบ (narrow therapeutic range)
กราฟในสไลด์: INR **ต่ำกว่า 2 → stroke เพิ่ม** · INR **สูงกว่า 3–4 → เลือดออกในสมองเพิ่มชัด** · เป้า **2.0–3.0**

### หลักการปรับขนาด (สไลด์)
1. **ถามก่อนเสมอ** — กินยาตรงไหม ลืมหรือกินเกิน **อาหารเปลี่ยน** (ผักใบเขียว อาหารเสริม สมุนไพร สุรา) หรือ **ได้ยาใหม่** (ยาปฏิชีวนะ amiodarone fluconazole ยาเพิ่ม INR · rifampicin ยาลด INR)
2. **คิดเป็นขนาดต่อสัปดาห์**
3. **INR ห่างจากเป้า ±0.5 → ปรับขนาด ±10–20% ต่อสัปดาห์**

### เม็ดยาที่มี
warfarin **2 มก.** (Maforan) · **3 มก.** และ **5 มก.** (Orfarin)
- 4 มก./วัน = 2 มก. × 2 เม็ด
- 4.5 มก./วัน = 2 มก. + ½ ของ 5 มก.

### โจทย์ในสไลด์
**เคส 1** — กิน warfarin 2 มก./วัน วันนี้ **INR 1.0**
→ ค่าต่ำจนเหมือนไม่ได้กินยาเลย ขั้นแรกคือ **สอบถามวิธีการกินยาก่อนตัดสินใจ** ไม่ใช่เพิ่มขนาดทันที

**เคส 2** — กิน warfarin 5 มก./วัน (**35 มก./สัปดาห์**) วันนี้ **INR 3.5** (เป้า 2–3)
| ตัวเลือก | ขนาดต่อสัปดาห์ | ลดลง |
|---|---|---|
| 3 มก. จ–ศ + 4 มก. ส–อา | 23 | 34% (มากไป) |
| **4.5 มก. ทุกวัน** | **31.5** | **10%** |
| 4 มก. ทุกวัน | 28 | 20% |
→ **ถามเรื่องอาหารหรือยาที่เปลี่ยนก่อน** แล้วถ้าต้องปรับ INR 3.5 อยู่ในช่วง 3–5 → **งดยา 1 วัน แล้วลดราว 10% ต่อสัปดาห์** = 31.5 มก./สัปดาห์

### INR สูงเกินไป (สไลด์)
| สถานการณ์ | การจัดการ |
|---|---|
| **INR 3–5 ไม่มีเลือดออก** | **งดยา 1 วัน** ลดขนาด **10%/สัปดาห์** |
| **INR 5–9 ไม่มีเลือดออก** | **งดยา 2 วัน** ลดขนาด **20%/สัปดาห์** |
| **INR > 9 ไม่มีเลือดออก** | **หยุดยา + vitamin K 2.5–5 มก. กิน** · ติดตาม 24–48 ชม. ถ้ายังสูงให้ vitamin K 1–2 มก. กินซ้ำ |
| **เลือดออกมาก + INR ยาว** | **หยุดยา + vitamin K 10 มก. ทางหลอดเลือด** · พิจารณา **FFP** หรือ recombinant factor VIIa (หรือ PCC) |

**ทำไมต้องให้ FFP/PCC ด้วยเมื่อเลือดออก** — vitamin K ต้องรอตับสร้าง factor ใหม่ 12–24 ชม. ส่วน FFP/PCC เติม factor ที่สร้างเสร็จแล้วทันที
""",
    ["Warfarin INR ต่ำผิดคาด → ถามวิธีกินยา อาหาร ยาใหม่ ก่อนปรับขนาด",
     "คิดเป็นขนาดต่อสัปดาห์ · INR ±0.5 → ปรับ ±10–20%",
     "INR 3–5: งด 1 วัน ลด 10% · 5–9: งด 2 วัน ลด 20% · > 9: หยุด + vit K 2.5–5 มก. กิน",
     "เลือดออกมาก: vit K 10 มก. IV + FFP/PCC"],
    [mcq(N(14), "A patient taking warfarin 2 mg daily for AF has an INR of 1.0 today (previous INRs were 2.3–2.6). What should be done first?",
         ["Increase to 4 mg daily", "Increase to 3 mg daily except Sunday", "Ask how the patient has been taking the medication before changing the dose",
          "Switch to a NOAC immediately", "Give vitamin K"], 2,
         "โจทย์ในสไลด์ — INR 1.0 ในผู้ที่เคยคุมได้ดี เท่ากับ **แทบไม่มีฤทธิ์ยาเลย** สาเหตุที่พบบ่อยที่สุดคือ **ไม่ได้กินยา** หรือกินผิดวิธี\n\nคำตอบของอาจารย์: **สอบถามวิธีการกินยาก่อนตัดสินใจวางแผนการรักษา** — ถ้าเพิ่มขนาดทั้งที่ผู้ป่วยแค่ลืมกิน เมื่อกลับมากินครบจะได้ยาเกินจน INR สูงและเลือดออก",
         "INR ต่ำผิดคาด → ถามการกินยาก่อน", "Warfarin low INR", R("โจทย์ warfarin 2 mg INR 1.0"), NLN + ["B2.4(3)"]),
     mcq(N(15), "A patient on warfarin 5 mg daily (35 mg/week) has INR 3.5 with no bleeding. Diet and medicines are unchanged. Which adjustment matches the lecture's rule?",
         ["Stop warfarin permanently", "Give vitamin K 10 mg intravenously", "Hold one dose, then reduce to about 31.5 mg/week (4.5 mg daily)",
          "Increase to 6 mg daily", "Reduce to 23 mg/week"], 2,
         "สไลด์: **INR 3–5 ไม่มีเลือดออก → งดยา 1 วัน และลดขนาดลง 10% ต่อสัปดาห์** และหลักทั่วไป INR เกิน 0.5 → ปรับ 10–20%\n\n35 × 0.9 = **31.5 มก./สัปดาห์ = 4.5 มก./วัน** (2 มก. + ½ ของ 5 มก.)\n\n23 มก./สัปดาห์ ลดถึง 34% มากเกินไปจน INR อาจต่ำกว่าเป้า · vitamin K ใช้เมื่อ INR > 9 หรือมีเลือดออก",
         "INR 3–5 ไม่มีเลือดออก: งด 1 วัน + ลด 10%/สัปดาห์", "Warfarin high INR", R("โจทย์ warfarin 5 mg INR 3.5"), NLN + ["2.3.3(1)"]),
     mcq(N(16), "A patient on warfarin presents with melaena, BP 84/50 mmHg and INR 6.8. Which management is most appropriate in addition to resuscitation?",
         ["Hold warfarin only and recheck INR in a week", "Oral vitamin K 1 mg", "Stop warfarin, give vitamin K 10 mg intravenously and replace clotting factors with FFP or PCC",
          "Give idarucizumab", "Continue warfarin at half dose"], 2,
         "สไลด์: **เลือดออกมากร่วมกับ INR ยาว → หยุดยา ให้ vitamin K 10 มก. ทางหลอดเลือด และพิจารณา FFP หรือ recombinant factor VIIa**\n\nVitamin K ต้องรอตับสร้าง factor ใหม่ 12–24 ชม. จึงต้องให้ **FFP หรือ PCC** เพื่อเติม factor II, VII, IX, X ทันที · idarucizumab ใช้กับ dabigatran เท่านั้น",
         "Warfarin + major bleed: vit K 10 มก. IV + FFP/PCC", "Warfarin-associated bleeding", R("INR สูงเกินไป"), NLN + ["2.3.3(1)", "2.2.44"]),
    ], NLN + ["2.3.3(1)", "B2.4(3)", "B2.2.5(2)"])

# ───────────────────────────── 9
sec("cardio-af-09", "B — Rate control: เป้า < 110 และเลือกยาตามโรคร่วม",
    "ยังเป็น AF แต่ไม่เร็ว · β-blocker · diltiazem/verapamil · digoxin · amiodarone เมื่อ unstable", 9,
"""### Rate control คืออะไร
**ยังเป็น AF อยู่ แต่ไม่ให้เต้นเร็ว** — เป้า **อัตราขณะพัก < 110 ครั้ง/นาที** (lenient rate control) ถ้ายังมีอาการจึงค่อยลดลงอีก

### ยาคุมอัตรา (สไลด์)
| สถานการณ์ | ยา |
|---|---|
| **Acute · stable** | ยากิน — **β-blocker** · **non-DHP CCB (diltiazem, verapamil)** · **digoxin** |
| **Acute · unstable** | ยาทางหลอดเลือด (**amiodarone**) หรือ **cardioversion** |
| **ระยะยาว** | ยาเดิม คุมให้ **< 110** |

**กลไก** — ทุกตัว **ชะลอการนำไฟฟ้าผ่าน AV node** ห้องบนยังสั่นเหมือนเดิม แต่สัญญาณผ่านลงห้องล่างน้อยลง

### เลือกยาตามโรคร่วม (ESC 2020)
| โรคร่วม | ยาลำดับแรก | เหตุผล |
|---|---|---|
| ไม่มี · ความดันสูง · **HFpEF** | **β-blocker หรือ NDCC** | |
| **HFrEF** | **β-blocker** (ลำดับสอง: digoxin, amiodarone) | **ห้าม NDCC** — กดการบีบตัว ทำให้ HF แย่ลง |
| **COPD/asthma รุนแรง** | **NDCC** | β-blocker อาจทำให้หลอดลมตีบ |
| **Pre-excited AF (WPW)** | **ablation** | **ห้ามยาที่กด AV node** (β-blocker, CCB, digoxin, adenosine) — สัญญาณจะลงทาง accessory pathway จนเป็น VF |
ยังคุมไม่ได้ → ใช้ยาร่วมกันสองตัว → สามตัว หรือ **ใส่ pacemaker แล้วจี้ AV node (pace-and-ablate)**

### HFrEF ที่ทรุดและความดันต่ำ
β-blocker และ NDCC ลดการบีบตัวจนความดันตกอีก → ใช้ **digoxin ทางหลอดเลือด** (เพิ่มแรงบีบเล็กน้อยและชะลอ AV node) หรือ **amiodarone** หรือ cardioversion ถ้า unstable
""",
    ["Rate control เป้า < 110 ขณะพัก",
     "Stable: β-blocker · diltiazem/verapamil · digoxin · unstable: IV amiodarone หรือ cardioversion",
     "HFrEF: β-blocker · ห้าม NDCC · ทรุด/ความดันต่ำ → IV digoxin หรือ amiodarone",
     "COPD/asthma รุนแรง → NDCC",
     "Pre-excited AF → ห้ามยากด AV node"],
    [mcq(N(17), "A 66-year-old man with severe COPD (frequent bronchospasm) has persistent AF at 128/min, BP 138/84 mmHg and normal LVEF. Which first-line rate-control drug is most suitable?",
         ["Propranolol", "Diltiazem", "Adenosine", "Ivabradine", "Flecainide"], 1,
         "แผนผังเลือกยาในสไลด์ (ESC 2020): **severe COPD หรือ asthma → NDCC (diltiazem, verapamil) เป็นลำดับแรก** เพราะ β-blocker (โดยเฉพาะ non-selective อย่าง propranolol) อาจทำให้หลอดลมตีบ\n\nAdenosine ใช้วินิจฉัย/หยุด SVT ไม่ได้คุมอัตรา AF · flecainide เป็นยาคุมจังหวะ ไม่ใช่ยาคุมอัตรา",
         "Severe COPD/asthma → NDCC", "Rate control in COPD", R("Choice of drugs for rate control"), NLN + ["B7.4(7)"]),
     mcq(N(18), "A 25-year-old man has an irregular, very rapid, wide-complex tachycardia at 240/min with varying QRS width; his resting ECG shows a short PR and delta wave. BP is 118/72 mmHg. Which drug must be AVOIDED?",
         ["Procainamide", "Ibutilide", "Verapamil", "Synchronised cardioversion", "Referral for accessory-pathway ablation"], 2,
         "นี่คือ **pre-excited AF (AF ใน WPW)** — QRS กว้างและแปรผัน อัตราเร็วมาก ไม่สม่ำเสมอ\n\nยาที่ **กด AV node (verapamil, diltiazem, β-blocker, digoxin, adenosine)** ทำให้สัญญาณลงทาง **accessory pathway** มากขึ้น → อัตราเร็วขึ้นจนเกิด **VF** ได้\n\nสไลด์จัด **pre-excited AF → ablation** เป็นการรักษาหลัก ระยะเฉียบพลันใช้ **procainamide/ibutilide** หรือ **cardioversion**",
         "Pre-excited AF: ห้าม AV nodal blocker", "Pre-excited AF", R("Choice of drugs for rate control"), NLN + ["3.1.12", "B7.4(7)"]),
    ], NLN + ["B7.4(7)"])

# ───────────────────────────── 10
sec("cardio-af-10", "B — Rhythm control: cardioversion และการคงจังหวะปกติ",
    "Emergency ช็อกไฟฟ้า · elective ต้อง anticoagulate 3 สัปดาห์ก่อนและ 4 สัปดาห์หลัง หรือ TEE · ยาคงจังหวะและ ablation", 9,
"""### Rhythm control คืออะไร
**กลับเป็นจังหวะปกติ (sinus rhythm)** — เป็นการรักษาที่ **เข้มข้นกว่า** rate control มีสองขั้น
1. **Cardioversion** — เปลี่ยนจาก AF เป็น sinus ด้วย **ไฟฟ้า** หรือ **ยา**
2. **คงจังหวะปกติระยะยาว** — ด้วย **ยาต้านหัวใจเต้นผิดจังหวะ** หรือ **AF ablation**

### Cardioversion สองแบบ (สไลด์)
| | **Emergency** | **Elective** |
|---|---|---|
| ข้อบ่งชี้ | **hemodynamics ไม่คงที่** — ความดันต่ำ **สติเปลี่ยน HF เจ็บหน้าอก** | hemodynamics คงที่ |
| วิธี | **ช็อกไฟฟ้า (synchronized)** | ไฟฟ้า หรือ ยา |
| ยาต้านการแข็งตัว | เริ่มให้ทันทีพร้อมกัน ไม่ต้องรอ | **ต้องให้** — **3 สัปดาห์ก่อน และ 4 สัปดาห์หลัง** หรือ **ใช้ TEE ตรวจว่าไม่มีลิ่มเลือดแล้วทำได้เลย** |

**ทำไมต้อง 4 สัปดาห์หลัง แม้กลับเป็น sinus แล้ว** — ห้องบนยัง **"ชา" (atrial stunning)** บีบตัวไม่ได้เต็มที่หลายสัปดาห์ ลิ่มเลือดยังก่อตัวได้ และผู้ป่วยที่มีความเสี่ยง stroke ต้องกินยาต่อระยะยาวตามคะแนน ไม่ใช่หยุดหลัง 4 สัปดาห์

**ทำไมต้อง synchronized** — ช็อกตรงกับ R wave เพื่อเลี่ยงการช็อกบน T wave (vulnerable period) ซึ่งทำให้เกิด VF

### คงจังหวะปกติระยะยาว
- **ยา** — amiodarone · dronedarone · flecainide · propafenone · dofetilide · sotalol
  - flecainide/propafenone ใช้ได้เฉพาะ **หัวใจโครงสร้างปกติ** (ห้ามใน CAD หรือ HFrEF)
  - amiodarone ได้ผลดีสุดแต่มีพิษต่อไทรอยด์ ปอด ตับ
- **AF ablation** (pulmonary vein isolation) — จุดเริ่มของ AF มักอยู่ที่รูเปิดของ pulmonary vein
""",
    ["Rhythm control = cardioversion (ไฟฟ้า/ยา) + คงจังหวะระยะยาว (ยา/ablation)",
     "Unstable → synchronized electrical cardioversion ทันที",
     "Elective cardioversion: OAC 3 สัปดาห์ก่อน + 4 สัปดาห์หลัง หรือ TEE",
     "ยาคงจังหวะ: amiodarone · dronedarone · flecainide · propafenone · dofetilide · sotalol"],
    [mcq(N(19), "A 60-year-old man has had AF for an unknown duration with palpitations; he is haemodynamically stable. Elective cardioversion is planned. Which approach is correct?",
         ["Cardiovert today without anticoagulation", "Anticoagulate for 3 weeks before and at least 4 weeks after cardioversion, or perform TEE to exclude thrombus first",
          "Give aspirin for 1 week before cardioversion", "Anticoagulate only after cardioversion if AF recurs", "Cardioversion is contraindicated in AF"], 1,
         "สไลด์ elective cardioversion: **ต้องให้ยาต้านการแข็งตัว 3 สัปดาห์ก่อนและ 4 สัปดาห์หลัง หรือใช้ TEE strategy**\n\nAF ที่ **ไม่ทราบระยะเวลา** ถือว่าอาจนานกว่า 48 ชม. → อาจมีลิ่มเลือดใน LAA แล้ว ถ้าช็อกทันทีลิ่มเลือดจะหลุดเมื่อห้องบนกลับมาบีบ · หลัง cardioversion ห้องบนยัง **stunned** จึงต้องให้ยาต่ออย่างน้อย 4 สัปดาห์",
         "Elective CV: OAC 3 สัปดาห์ก่อน + 4 สัปดาห์หลัง หรือ TEE", "Anticoagulation around cardioversion", R("Cardioversion")),
    ])

# ───────────────────────────── 11
sec("cardio-af-11", "C — โรคร่วมและวิถีชีวิต และบทสรุปทั้งคาบ",
    "รักษาสาเหตุ · ลดน้ำหนัก ออกกำลัง ลดสุรา คุมความดัน เบาหวาน OSA → AF กลับเป็นน้อยลง", 7,
"""### C ใน ABC pathway
**รักษาโรคที่เป็นเหตุของ AF** ทั้งเพื่อ **ป้องกันไม่ให้เกิด (primary)** และ **ป้องกันการกลับเป็นซ้ำใน paroxysmal AF (secondary)**
ยาที่เคยมีการศึกษา: **ACEI/ARB** · **statin** · **PUFA**

### เป้าหมายเฉพาะ (สไลด์ ESC 2020 และ update 2024)
| ปัจจัย | เป้าหมาย |
|---|---|
| **ความดันสูง** | คุมให้เหมาะ · **ACEI หรือ ARB เป็นยาแรก** |
| **Heart failure** | **GDMT สำหรับ HFrEF** |
| **น้ำหนัก** | ลด **≥ 10%** · เป้า **BMI 20–25** (สไลด์ 2020: < 27) |
| **ออกกำลังกาย** | ปานกลาง **150–300 นาที/สัปดาห์** หรือหนัก **75–150 นาที/สัปดาห์** |
| **สุรา** | เลี่ยงการดื่มหนัก หรือเลิกในคนที่ดื่มประจำ |
| **เบาหวาน** | HbA1c ลด > 10% เป้า < 6.5% · **metformin หรือ SGLT2 inhibitor** |
| บุหรี่ | เลิก |
| **OSA** | วินิจฉัยและรักษา |
| ไขมัน | ตามแนวทาง |
การคุมปัจจัยเหล่านี้ทำให้ **AF กลับเป็นซ้ำน้อยลง** และทำให้ **ablation ได้ผลดีขึ้น**

### บทสรุปของอาจารย์
| ขั้น | สาระ |
|---|---|
| **Dx** | **ECG**: R-R ไม่สม่ำเสมอ · ไม่มี P wave · atrial rate > 300 |
| ทำไมต้องรักษา | **ตาย ×2 · stroke ×5** · พบ 1–2% ของประชากร |
| **A** | ประเมินความเสี่ยง stroke — **เคย stroke · อายุ ≥ 75 · คะแนนสูง** → ป้องกันด้วย **warfarin · NOAC · LAA occluder** |
| **B** | **Rate** (< 110) หรือ **rhythm** control |
| **C** | **รักษาโรคร่วม** |

**ESC 2024** เรียกกรอบใหม่ว่า **AF-CARE** — **C**omorbidity · **A**void stroke · **R**educe symptoms (rate & rhythm) · **E**valuation ต่อเนื่อง โดยย้ายการคุมโรคร่วมขึ้นมาเป็นข้อแรก
""",
    ["C: ACEI/ARB สำหรับความดัน · GDMT สำหรับ HFrEF · BMI 20–25 · ออกกำลัง 150–300 นาที/สัปดาห์",
     "เลี่ยงดื่มหนัก · DM ใช้ metformin หรือ SGLT2i · รักษา OSA",
     "คุมปัจจัยเสี่ยง → AF กลับเป็นน้อยลง และ ablation ได้ผลดีขึ้น",
     "ESC 2024 = AF-CARE (Comorbidity · Avoid stroke · Reduce symptoms · Evaluation)"],
    [mcq(N(20), "A 52-year-old man with paroxysmal AF has BMI 33 kg/m², untreated hypertension, snoring with daytime sleepiness and drinks heavily at weekends. Which intervention is MOST likely to reduce his AF burden over the long term?",
         ["Aspirin 81 mg daily", "Comprehensive risk-factor management: weight loss, BP control with ACEI/ARB, treatment of sleep apnoea and alcohol reduction",
          "Digoxin alone", "Avoiding all exercise", "Routine annual Holter monitoring only"], 1,
         "สไลด์ **C — comorbidities/cardiovascular risk factor management**: **ลดน้ำหนัก ≥ 10% · คุมความดันด้วย ACEI/ARB · วินิจฉัยและรักษา OSA · ลดหรือเลิกสุรา · ออกกำลัง 150–300 นาที/สัปดาห์**\n\nการคุมปัจจัยเหล่านี้ลดการ remodel ของห้องบน → **AF กลับเป็นน้อยลง** · aspirin และ digoxin ไม่ได้ลดภาระ AF",
         "C: ลดน้ำหนัก คุมความดัน รักษา OSA ลดสุรา → AF ลดลง", "Risk-factor management", R("Comorbidities and CV risk factors"), NLN + ["2.3.9(4)"]),
    ], NLN + ["2.3.9(4)", "2.3.9(5)"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "Atrial fibrillation (อ.อภิชัย)"
MEQ = [{"id": "CAR-AF-MEQ-01", "part": "MEQ", "lec": "24", "lecture": LECNAME,
 "topic": "New AF with rapid ventricular response — diagnosis, rate control, stroke prevention and warfarin follow-up",
 "vignette": """ผู้ป่วยหญิงไทยอายุ 76 ปี มาห้องฉุกเฉินด้วยอาการใจสั่น เหนื่อยง่าย 3 วัน
PI: 3 วันก่อนมีใจสั่นตลอดเวลา เหนื่อยเวลาเดินในบ้าน นอนราบได้ ไม่มีเจ็บหน้าอก ไม่เป็นลม ไม่ทราบว่าเริ่มใจสั่นวันไหนแน่
U/D: ความดันโลหิตสูง 10 ปี (amlodipine 10 มก.) · เบาหวานชนิดที่ 2 (metformin) · ไม่เคยเป็น stroke
PE: BT 36.8 C, PR 132/min irregularly irregular, apical rate 150/min, BP 142/86 mmHg, RR 20/min, SpO2 97%
JVP ไม่สูง · Heart: irregular rhythm, no murmur · Lungs: clear · ไม่มีขาบวม
Lab: Cr 0.9 mg/dL, น้ำหนัก 58 กก., TSH ปกติ · Echo: LVEF 60%, ไม่มี mitral stenosis""",
 "questions": [
  {"q": "1. จงบอกการตรวจที่ใช้ยืนยันการวินิจฉัย และเกณฑ์ที่ใช้ (2 คะแนน)",
   "a": """**12-lead ECG** — "ECG must be done!!!"
เกณฑ์ AF สามข้อ: **(1) irregular R-R interval (2) no distinct P wave (มี f wave แทน) (3) atrial rate > 300 bpm**
ผู้ป่วยรายนี้มี **pulse deficit** (apical 150 vs ชีพจร 132) สนับสนุน AF with rapid ventricular response"""},
  {"q": "2. ผู้ป่วยรายนี้ stable หรือ unstable และจะคุมอัตราการเต้นของหัวใจอย่างไร เป้าหมายเท่าใด (3 คะแนน)",
   "a": """**Stable** — ไม่มี hypotension, สติเปลี่ยน, pulmonary edema, เจ็บหน้าอก หรือ shock
**Rate control**: LVEF ปกติ + ความดันสูง → **β-blocker (เช่น metoprolol) หรือ non-DHP CCB (diltiazem)** เป็นลำดับแรก · **เป้า < 110 ครั้ง/นาทีขณะพัก**
**ไม่ทำ cardioversion ทันที** เพราะ **ไม่ทราบระยะเวลาที่เป็น** (อาจ > 48 ชม.) → เสี่ยงลิ่มเลือดหลุด"""},
  {"q": "3. จงคำนวณ CHA₂DS₂-VASc และบอกแนวทางป้องกัน stroke พร้อมเลือกยาและขนาด (4 คะแนน)",
   "a": """**CHA₂DS₂-VASc = 5** — H 1 · D 1 · **A₂ (≥ 75) 2** · Sc หญิง 1 (CHA₂DS₂-VA = 4)
→ เสี่ยงสูง (ราว 6.7%/ปี) → **ให้ยาต้านการแข็งตัวของเลือด** (อายุ ≥ 75 ก็เสี่ยงสูงอยู่แล้ว)
ไม่มี mitral stenosis/ลิ้นเทียม = **non-valvular AF → เลือก NOAC** ได้ เช่น **apixaban 5 มก. วันละ 2 ครั้ง** — ผู้ป่วยเข้าเกณฑ์ลดขนาดเพียงข้อเดียว (น้ำหนัก ≤ 60) จึงยังเป็นขนาดปกติ
หรือ **warfarin เป้า INR 2–3** ถ้าค่าใช้จ่ายเป็นข้อจำกัด
**ไม่ใช้ aspirin** · ประเมิน bleeding risk และแก้ปัจจัยที่แก้ได้"""},
  {"q": "4. ผู้ป่วยเลือกใช้ warfarin 5 มก./วัน หนึ่งเดือนต่อมา INR 3.5 ไม่มีเลือดออก จะทำอย่างไร (3 คะแนน)",
   "a": """1. **ถามก่อน** — กินยาถูกไหม อาหารเปลี่ยน ได้ยาใหม่ (ยาปฏิชีวนะ amiodarone fluconazole) หรือไม่
2. **INR 3–5 ไม่มีเลือดออก → งดยา 1 วัน และลดขนาด 10% ต่อสัปดาห์**
3. 35 มก./สัปดาห์ → **31.5 มก./สัปดาห์ = 4.5 มก./วัน** (2 มก. + ½ ของ 5 มก.)
4. นัดตรวจ INR ซ้ำ"""},
  {"q": "5. จงบอกการดูแลโรคร่วม (C) ที่ควรแนะนำ (2 คะแนน)",
   "a": """- คุมความดัน — **ACEI หรือ ARB เป็นลำดับแรก**
- เบาหวาน — **metformin หรือ SGLT2 inhibitor**
- **BMI 20–25** · ออกกำลังกายปานกลาง **150–300 นาที/สัปดาห์** · เลี่ยงสุรา
- คัดกรอง sleep apnea ถ้ามีอาการ"""}],
 "ref": ["สไลด์ อ.อภิชัย — ECG, ABC pathway, warfarin cases"], "nl": ["2.3.9(1)", "2.1.36", "3.1.12", "B2.4(3)", "2.3.9(4)"],
 "years": [], "_kind": "meq", "_set": "cardio"}]

OSCE = [{"id": "CAR-AF-OSCE-01", "part": "OSCE/SAQ", "lec": "24", "lecture": LECNAME,
 "topic": "OSCE – Counselling a patient starting warfarin for atrial fibrillation",
 "station": "OSCE (ให้คำแนะนำผู้ป่วยมาตรฐาน) 5 นาที",
 "instruction": """ผู้ป่วยชายอายุ 70 ปี เพิ่งได้รับการวินิจฉัย AF ร่วมกับ moderate mitral stenosis แพทย์ตัดสินใจเริ่ม **warfarin 3 มก./วัน** เป้า INR 2.0–3.0

ผู้ป่วยถามว่า "ยานี้คือยาอะไร ทำไมต้องกิน แล้วทำไมไม่ใช้ยาใหม่ที่ไม่ต้องเจาะเลือด"

**จงให้คำแนะนำผู้ป่วยเรื่องการใช้ยา warfarin ภายใน 5 นาที**""",
 "answer": """**เกณฑ์ให้คะแนน (10 คะแนน)**

| ข้อ | สิ่งที่ต้องทำ | คะแนน |
|---|---|---|
| 1 | แนะนำตัว ยืนยันตัวผู้ป่วย ถามความเข้าใจเดิม | 1 |
| 2 | อธิบาย **ทำไมต้องกิน** — หัวใจห้องบนเต้นสั่น เลือดค้างจนเป็นลิ่ม หลุดไปอุดสมอง (stroke เพิ่มราว 5 เท่า) ยานี้ช่วยป้องกัน | 1 |
| 3 | ตอบ **ทำไมไม่ใช้ NOAC** — ผู้ป่วยมี **ลิ้นหัวใจไมทรัลตีบปานกลาง** ยาใหม่ไม่มีหลักฐานและไม่แนะนำ ต้องใช้ warfarin | 1 |
| 4 | **วิธีกิน** — วันละครั้ง เวลาเดียวกันทุกวัน · ลืมกินให้กินทันทีที่นึกได้ในวันเดียวกัน **ห้ามกินเพิ่มเป็นสองเท่าวันถัดไป** · ดูสีและขนาดเม็ดยา (2/3/5 มก. สีต่างกัน) | 2 |
| 5 | **ต้องเจาะ INR สม่ำเสมอ** เป้า 2–3 · ต่ำไปป้องกันไม่ได้ สูงไปเลือดออก | 1 |
| 6 | **อาหารและยาอื่น** — กินผักใบเขียวสม่ำเสมอ ไม่เปลี่ยนมาก · **ห้ามซื้อยาเอง** โดยเฉพาะยาแก้ปวด NSAID aspirin สมุนไพร อาหารเสริม · แจ้งแพทย์และทันตแพทย์ทุกครั้งว่ากิน warfarin · เลี่ยงสุรา | 2 |
| 7 | **อาการเลือดออกที่ต้องมาโรงพยาบาล** — เลือดออกตามไรฟัน จ้ำเลือด ปัสสาวะสีแดง อุจจาระดำ อาเจียนเป็นเลือด ปวดศีรษะรุนแรง แขนขาอ่อนแรง | 1 |
| 8 | ทวนความเข้าใจ (teach-back) และเปิดโอกาสถาม | 1 |

**ข้อที่ทำให้เสียคะแนน**: บอกให้กินยาสองเท่าเมื่อลืม · ไม่ห้าม NSAID · บอกให้งดผักใบเขียวทั้งหมด (ควรกินสม่ำเสมอ ไม่ใช่งด) · ไม่อธิบายเหตุผลที่ใช้ NOAC ไม่ได้""",
 "ref": ["สไลด์ อ.อภิชัย — VKA vs NOACs, warfarin tablets, INR adjustment"], "nl": ["2.3.9(1)", "B2.4(3)", "2.3.3(1)"],
 "years": [], "_kind": "meq", "_set": "cardio"}]

LECTURE = {
 "lec": "24", "date": "จ. 5 ต.ค.",
 "title": "Atrial fibrillation",
 "subtitle": "ความชุกและผลลัพธ์ · โรคที่สัมพันธ์ · stable/unstable · ECG สามเกณฑ์ · ระยะและ EHRA · CHA₂DS₂-VASc/VA · warfarin กับ NOAC · ปรับ warfarin ตาม INR · rate และ rhythm control · โรคร่วมและวิถีชีวิต",
 "objectives": [
   "อธิบายความสำคัญของ AF ทั้งความชุก การตาย และ stroke และกลไกการเกิดลิ่มเลือดที่ LAA",
   "ระบุโรคที่สัมพันธ์กับ AF และสาเหตุที่แก้ได้ที่ต้องหาเสมอ",
   "แยก AF ที่ stable กับ unstable และรู้ว่าเมื่อใดต้อง cardioversion ทันที",
   "วินิจฉัย AF จาก ECG ด้วยสามเกณฑ์ และแปลผลอุปกรณ์คัดกรอง",
   "จำแนกระยะของ AF และประเมินอาการด้วย EHRA score",
   "คำนวณ CHA₂DS₂-VASc/CHA₂DS₂-VA และเลือกยาต้านการแข็งตัวของเลือดพร้อมขนาดที่ถูกต้อง",
   "ปรับขนาด warfarin ตาม INR และจัดการ INR สูงหรือเลือดออก",
   "เลือกยา rate control ตามโรคร่วม และวางแผน rhythm control อย่างปลอดภัย"],
 "nlGap": "เกณฑ์ฯ มีรหัส AF ใน `นล. 2.3.9(1)` และยาต้านการแข็งตัวใน `B2.4(3)` แต่ **ไม่มีรหัสของ NOAC แต่ละตัว คะแนน CHA₂DS₂-VASc AF ablation หรือ LAA occlusion** เนื้อหาส่วนนั้นอิงแนวทางที่อาจารย์ใช้และแนวทางปัจจุบันด้านล่าง",
 "guidelines": [
   "**ESC 2020 Guidelines for the diagnosis and management of atrial fibrillation** — ABC pathway, EHRA score, แผนผังเลือกยา rate control (อาจารย์อ้างในสไลด์)",
   "**ESC 2024 Guidelines for the management of atrial fibrillation** — AF-CARE และ CHA₂DS₂-VA",
   "**2023 ACC/AHA/ACCP/HRS Guideline for the Diagnosis and Management of Atrial Fibrillation**",
   "**Fuster V, et al. ACC/AHA/ESC Guidelines for AF. Europace 2006;8:651–745** — ความชุกตามอายุ และกราฟ INR กับ stroke/เลือดออก (อาจารย์อ้างในสไลด์)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# ── เขียนลงไฟล์ แล้วผูกข้อสอบคลัง Ward Drill คาบ 24
path = os.path.join(BUILD, "data", "cardio.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

BANK_MAP = {
    "cardio-af-02": ["C-MCQ-21", "C-OLD-61", "C-OLD-62", "C-OLD-63", "C-OLD-64", "C-OLD-69"],
    "cardio-af-03": ["C-OLD-59", "C-OLD-67", "C-OLD-68", "C-OLD-70"],
    "cardio-af-04": ["C-OLD-71", "C-OLD-60"],
    "cardio-af-06": ["C-MCQ-18", "C-OLD-56", "C-OLD-66"],
    "cardio-af-07": ["C-MCQ-22", "C-OLD-65"],
    "cardio-af-09": ["C-OLD-57", "C-OLD-58", "C-MCQ-19"],
    "cardio-af-10": ["C-MCQ-20"],
}
added = link("cardio", "24", BANK_MAP)

data = json.load(open(path, encoding="utf-8"))
L = [l for l in data if l["lec"] == "24"][0]
seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s in L["sections"] for c in s["nl"]} | {c for s in L["sections"] for i in s["items"] for c in i["nl"]} | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in L["sections"]:
    assert "```" not in s["md"], s["id"]

# เรียงคาบตามลำดับเลขคาบจริง (คาบที่เป็นวันที่ไว้ท้าย)
data.sort(key=lambda l: (0, int(l["lec"])) if l["lec"].isdigit() else (1, l["lec"]))
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "cardio": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("sections %d | ข้อใหม่ %d + คลัง %d = %d | meq %d | osce %d | nl %d" % (
    len(S), sum(1 for s in S for i in s["items"] if i["kind"] == "mcq" and i["id"].startswith("CAR-AF")), added,
    sum(len(s["items"]) for s in L["sections"]), len(L["meq"]), len(L["osce"]), len(codes)))
print("cardio.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
