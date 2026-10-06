from lib import lecture, sec, mcq, fig

D = "สไลด์ Update ข้อสอบ 2025"
SRC = "NL2 2025 (update)"

def R(*p):
    return [f"{D} หน้า " + ", ".join(str(x) for x in p)]

S1 = sec("exam25-09-01", "Crystal arthritis & drug-induced lupus",
    "Rhomboid weakly positive = CPPD · needle negative = gout · hydralazine/procainamide/isoniazid = drug-induced SLE", minutes=4,
    source=f"{D} หน้า 184–187", nl=["2.3.13(2)", "2.3.13-3(15)"],
    md='''
### ข้อสอบกลุ่มนี้ถามอะไร

**Crystal arthropathy — polarized microscopy**

| | Gout (MSU) | **CPPD (pseudogout)** |
|---|---|---|
| รูปร่าง | **needle-shaped** | **rhomboid** |
| Birefringence | **strongly negative** | **weakly positive** |
| ข้อที่พบบ่อย | MTP1, ข้อเท้า | **เข่า**, ข้อมือ |
| Uric acid | มักสูง (ช่วงกำเริบอาจปกติ) | ปกติ |
| X-ray | punched-out erosion | **chondrocalcinosis** |
| ปัจจัยเสี่ยง | ชาย, ไตเสื่อม, ดื่มเหล้า | **ผู้สูงอายุ**, hyperparathyroid, hemochromatosis, Mg ต่ำ (เสริม) |

- ต้องตัด **septic arthritis** เสมอด้วย Gram stain/culture ของน้ำข้อ

**Drug-induced lupus (DIL)**
- ยา: **hydralazine, procainamide**, isoniazid, minocycline, anti-TNF (เสริม)
- อาการ: ไข้ ปวดข้อ **serositis** (pericarditis, pleuritis) · ไตและ CNS พบน้อย · **anti-histone Ab บวก** · หายเมื่อหยุดยา
- ผู้ป่วย HT สูงอายุที่ใช้ hydralazine (พบใน slow acetylator) แล้วมีอาการแบบ SLE = DIL
''',
    pearls=[
        "Rhomboid + weakly positive = CPPD · needle + strongly negative = gout",
        "ผู้สูงอายุ ข้อเข่าอักเสบเฉียบพลัน uric acid ปกติ = นึกถึง CPPD",
        "Hydralazine/procainamide/isoniazid → drug-induced lupus (anti-histone)",
    ],
    items=[
        mcq("EXAM25-09-01-1",
            "A 70-year-old man presents with acute swelling and pain of the right knee. Synovial fluid examination under polarized light microscopy shows weakly positively birefringent rhomboid crystals. Gram stain is negative. Serum uric acid is normal. What is the most likely diagnosis?",
            "Calcium pyrophosphate deposition disease (pseudogout)",
            ["Gouty arthritis", "Septic arthritis", "Rheumatoid arthritis", "Osteoarthritis"],
            kind="old", src=SRC,
            explain='''ผลึก **rhomboid + weakly positive birefringence** = **calcium pyrophosphate (CPPD, pseudogout)** · เข้ากับผู้สูงอายุ ข้อเข่า และ uric acid ปกติ (สไลด์แสดงภาพผลึก)
- Gout เห็นผลึก **needle-shaped, strongly negative**
- Septic arthritis ต้องมีเชื้อ (Gram stain/culture บวก) และ WBC ในน้ำข้อสูงมาก — ตัดได้ด้วย Gram stain ลบ (เติมในโจทย์)
- RA เป็น polyarthritis สมมาตรเรื้อรัง ไม่มีผลึก
- OA เป็นเรื้อรัง ไม่อักเสบเฉียบพลัน และไม่มีผลึก''',
            pearl="Rhomboid weakly positive = CPPD", topic="CPPD",
            ref=R(184, 185), nl=["2.3.13(2)"]),
        mcq("EXAM25-09-01-2",
            "A 75-year-old woman with hypertension, controlled on medication for 10 years, presents with 2 weeks of fever, malaise, arthralgia, malar rash, oral ulcers and a pericardial friction rub. Hct 27%, WBC 2,800/µL, platelets 88,000/µL. Which medication is most likely responsible for this presentation?",
            "Hydralazine",
            ["Enalapril", "Amlodipine", "Losartan", "Hydrochlorothiazide"],
            kind="old", src=SRC,
            explain='''อาการแบบ SLE (ไข้ ปวดข้อ ผื่น serositis/pericarditis cytopenia) ในหญิงสูงอายุที่ใช้ยาลดความดันมานาน = **drug-induced lupus จาก hydralazine** (ยาที่เป็นสาเหตุคลาสสิกคู่กับ procainamide) → หยุดยา ตรวจ anti-histone
- Enalapril (ACEI) ทำให้ไอและ angioedema ไม่ใช่ DIL
- Amlodipine ทำให้ขาบวม เหงือกโต
- Losartan ทำให้ K สูง ไม่ใช่ DIL
- HCTZ ทำให้ photosensitivity และเกี่ยวกับ subacute cutaneous lupus ได้บ้าง แต่ไม่ใช่ systemic DIL แบบคลาสสิก''',
            pearl="HT + อาการ SLE ในผู้สูงอายุ → hydralazine-induced lupus", topic="Drug-induced lupus",
            ref=R(186, 187), nl=["2.3.13-3(15)", "2.3.19(2)"]),
    ])

LECTURE = lecture("09", "Rheumato", "CPPD · drug-induced lupus",
    objectives=[
        "แยก CPPD กับ gout จากผลึกในน้ำข้อ",
        "จำยาที่ทำให้เกิด drug-induced lupus",
    ],
    sections=[S1])
