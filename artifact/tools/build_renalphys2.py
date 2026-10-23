#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สรีรวิทยาไตพื้นฐาน II (Watchara Chongsa, PhD · Physiology Unit, Rangsit · MDS215 ปรีคลินิก) → data/nephro.json
ต้นฉบับ: Drive 1-i_hPZrlM-oGSyas0WZCslQRWyJyVtGw "Lec 8-12 Renal Physiology_Part II.pdf" (102 หน้า)
โน้ตสไลด์: slides/renal_physio2_notes.md · ภาพประกอบ: figs_renalphys2.py
lec = "Physio2" (ไม่มีคาบนี้ในคลัง Ward Drill) · แทรกต่อท้าย "Physio1" ถ้ามี ไม่งั้นไว้ลำดับแรก
สไลด์มี: ปริมาตร/osmolality (Darrow–Yannet, GT balance, sympathetic, RAAS, ADH, ANP, thirst, integrated responses) ·
Na K Ca Pi Mg · acid-base control (buffer, ปอด, ไต, TA/NH4, NAE) · disorders + compensation · ABG/AG · micturition
เติมจากตำรา/แนวทาง (ระบุในบทเรียน): SIADH/hyponatremia/ODS (European guideline 2014) · urine volume = osmole load/Uosm ·
Winter's formula และสูตรชดเชย · delta ratio · osmolal gap · urine AG · RTA ละเอียด · vomiting phases/urine Cl · DKA K ·
รูปแบบ incontinence ตามระดับรอยโรค
คลัง Ward Drill: ผูก MOCK-135 MOCK-180 MOCK-198 MOCK-200 (ไม่แตะคลังคาบ 19/22/28/42)"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
import figs_renalphys2 as F

SET, LEC = "nephro", "Physio2"
SRC = "สไลด์ Renal Physiology Part II (Watchara Chongsa, PhD)"
SRC_ADD = "สไลด์ Renal Physiology Part II + ตำรา/แนวทาง (บางส่วนไม่อยู่ในสไลด์)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl, figs=None, source=SRC):
    d = {"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": source,
         "nl": nl, "md": md, "pearls": pearls, "items": items}
    if figs: d["figs"] = figs
    S.append(d)
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl):
    assert len(choices) == 5 and 0 <= answer <= 4 and len(set(choices)) == 5, iid
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl}
N = lambda n: "NEPH-PHY2-MCQ-%02d" % n
R = lambda p, *g: ["สไลด์ Renal Physiology II — " + p] + list(g)
GH = "Guyton & Hall 14th ed"
BB = "Boron & Boulpaep 3rd ed"

# รหัส นล.
FLUID_B, GFR_B, TUB_B, HANDLE_B, AB_B, MICT_B, HORM_B = ("B9.1.2(1)", "B9.1.2(2)", "B9.1.2(3)", "B9.1.2(4)",
                                                         "B9.1.2(6)", "B9.1.2(7)", "B9.1.2(8)")
LYTE, LYTE_B = "2.3.4(2)", "B9.2.5(2)"
SIADH, SIADH_B = "2.3.4-3(5)", "B11.2.5-3(11)"
HORMDIS, DI_B, ADDISON_B, CONN_B = "2.3.4-3(4)", "B11.2.5-3(6)", "B11.2.5-3(8)", "B11.2.5-3(10)"
RAAS_B, CAPTH_B = "B11.1.2(3)c", "B11.1.2(2)e"
HYPERK, RTA = "2.2.15", "2.3.14-3(12)"
INCONT, STRESS, STRESS_B, AUR, RET, AUR_B = "2.1.46", "2.3.14(16)", "B10.2.3(2)", "2.2.29", "2.1.45", "B9.2.3(1)"
INNV, OAB_D, BPH = "B9.1.1(3)", "B9.4(3)", "2.3.14(8)"
EDEMA, POLY, OLIG, OLIG_B = "2.1.39", "2.1.42", "2.1.44", "B9.2.5(1)"
SHOCK, VOMIT, DIARR = "2.2.7", "2.1.15", "2.1.18"
DM, DM_B = "2.3.4(1)", "B11.2.5(4)"
OSM_B, ELYTE_B, ABG, ABG_B = "B9.3(3)", "B9.3(5)", "3.3.17", "B6.3(2)"
RESPCTRL_B, RESPFAIL_B, COPD, HYPERVENT = "B6.1.2(3)", "B6.2.5(1)", "2.3.10(3)", "2.2.22"
BUFFER_B, DIUR_B, FLUIDDRUG_B = "B1.1.1(1)", "B9.4(1)", "B9.4(2)"
POISON, WEAK, SEIZ, CONF = "2.2.46", "2.1.22", "2.1.23", "2.1.78"
ECG, ECG_B = "3.1.12", "B7.3(3)"
CKD, BP_B, HYPOVOL_B = "2.3.14(3)", "B7.1.2(4)", "B7.1.2(5)"
SCI, SCI_B, PULMED = "2.3.18-3(10)", "B3.2.3(3)", "2.2.5"

# ═════════════════════════════════════════════ 1
sec("nephro-phy2-01", "น้ำเคลื่อนตาม tonicity — osmolarity ที่ \"ดึงน้ำได้จริง\"",
    "ECF/ICF แลกน้ำกันด้วยแรง osmotic · Posm เทียบ tonicity · ทำไม urea ไม่ดึงน้ำ แต่ glucose ดึง", 8,
"""### Part II เรียนอะไร (สไลด์หน้า 2)
อ.วัชระแบ่ง Part II เป็น 6 เรื่อง: **(1)** การคุมปริมาตรและ osmolality ของน้ำในร่างกาย **(2)** สมดุล Na K Ca Pi Mg **(3)** การคุมกรด-ด่าง **(4)** ความผิดปกติกรด-ด่างและการชดเชย **(5)** การแปลผลกรด-ด่างทางคลินิก **(6)** การควบคุมการถ่ายปัสสาวะ
บทเรียนนี้เป็น **ฐานสรีรวิทยา** ของคาบคลินิกในชุด nephro: คาบ 05 Divalent (Ca P Mg) · คาบ 22 Dysnatremia/Dyskalemia (ยังไม่มีบทเรียน) · chest 26 ABG · 22/10 Urethral catheterization — เรื่อง GFR/RBF และการขนส่งในแต่ละ segment อยู่ใน **Part I**

> ส่วนที่ **ไม่อยู่ในสไลด์** (เติมจาก Guyton & Hall 14th · Boron & Boulpaep 3rd · แนวทาง hyponatremia ยุโรป 2014 · Berend NEJM 2014) จะบอกไว้ในหัวข้อนั้น ๆ เสมอ

### น้ำเข้าออกเท่ากันวันละ ~2.5 ลิตร — ร่างกายคุมสองชั้น
1. **การย้ายน้ำระหว่าง compartment** (ICF ↔ ECF) — เกิดเองตามแรง osmotic ภายในไม่กี่นาที
2. **ไตปรับการขับ Na และน้ำ** ผ่าน sympathetic และฮอร์โมน (RAAS ADH ANP) — ช้ากว่าแต่แก้ที่ต้นเหตุ

### กลไก: น้ำวิ่งตาม "ตัวถูกละลายที่ผ่านเยื่อไม่ได้"
เยื่อหุ้มเซลล์มี aquaporin น้ำผ่านได้อิสระ แต่ **Na ถูกปั๊มออก (Na/K-ATPase) และ glucose เข้าเซลล์ได้ช้า** จึงเป็นตัวถูกละลายที่ "ติดอยู่" ใน ECF · น้ำจะไหลไปฝั่งที่มีตัวถูกละลายพวกนี้เข้มข้นกว่าจนสองฝั่งเท่ากัน
- **ECF osmolarity ↑** → น้ำออกจากเซลล์ → ICF volume ↓ ICF osmolarity ↑ → **เซลล์เหี่ยว (cell dehydration)**
- **ECF osmolarity ↓** → น้ำเข้าเซลล์ → ICF volume ↑ ICF osmolarity ↓ → **เซลล์บวม (cell edema)**

[[fig:osm]]

### สูตรที่ต้องแยกให้ออก (สไลด์ Water shift)
| ค่า | สูตร | ใช้บอกอะไร |
|---|---|---|
| **Plasma osmolarity** | 2[Na] + glucose/18 + BUN/2.8 | ตัวถูกละลาย "ทั้งหมด" — เทียบกับค่าที่วัดได้ (osmolal gap หัวข้อ 14) |
| **Effective osmolarity (tonicity)** | 2[Na] + glucose/18 | ตัวที่ **ดึงน้ำได้จริง** — กำหนดขนาดเซลล์และกระตุ้น ADH |
- คูณ Na ด้วย 2 เพราะ Na มาพร้อม anion (Cl, HCO3) เสมอ · หาร glucose ด้วย 18 และ BUN ด้วย 2.8 เพื่อเปลี่ยน mg/dL เป็น mmol/L
- **urea ผ่านเยื่อหุ้มเซลล์ได้ง่าย** → ความเข้มข้นในและนอกเซลล์เท่ากันเสมอ → ไม่สร้างแรงดึงน้ำ = **ineffective osmole** (✍️ ลายมือในสไลด์: urea ไม่กระตุ้น ADH)
- ค่าปกติ Posm **285–295 mOsm/L** (สไลด์ ADH)

#### ทำไมถึงมีอาการนี้
| สถานการณ์ | กลไก | ผลที่เห็น |
|---|---|---|
| ไตวาย BUN 112 mg/dL | Posm ที่คำนวณสูงขึ้น ~40 แต่ urea อยู่ทั้งในและนอกเซลล์ | **ไม่มีเซลล์เหี่ยว ไม่กระหายน้ำจาก urea** — สับสนในไตวายมาจาก uremic toxin ไม่ใช่ osmolality |
| น้ำตาลสูงมาก (HHS) | glucose ค้างใน ECF (ขาด insulin) → ดึงน้ำออกจากเซลล์ | Na ในเลือด **ต่ำลงจากการเจือจาง** ทั้งที่ tonicity สูง (hypertonic hyponatremia) · สมองเหี่ยว → ซึม |
| ให้ mannitol | ผ่านเยื่อไม่ได้ → ดึงน้ำออกจากเซลล์สมอง | ใช้ลด ICP ได้ |
""",
    ["Tonicity = 2[Na] + glucose/18 — ไม่นับ urea เพราะผ่านเยื่อได้",
     "ECF hypertonic → เซลล์เหี่ยว · ECF hypotonic → เซลล์บวม (สมองทนบวมได้น้อยสุด)",
     "Glucose สูง → Na ต่ำจากการเจือจางทั้งที่ tonicity สูง (translocational)",
     "Posm ปกติ 285–295 mOsm/L"],
    [mcq(N(1), "A 66-year-old man with advanced chronic kidney disease has the following laboratory values: Na 138 mEq/L, glucose 90 mg/dL, BUN 112 mg/dL. He is alert and not thirsty. Which statement best explains why his brain cells are not shrinking despite the elevated calculated plasma osmolality?",
         ["Urea crosses cell membranes freely, so his effective osmolality (tonicity) is about 281 mOsm/L",
          "His calculated plasma osmolality of 321 mOsm/L proves that his cells are dehydrated but compensated by thirst",
          "Urea is confined to the extracellular fluid and therefore balances intracellular potassium",
          "Glucose is the main contributor to tonicity in this patient",
          "Each mEq of sodium contributes one osmole, so his tonicity is 143 mOsm/L"], 0,
         "คำนวณ: Posm = 2(138) + 90/18 + 112/2.8 = 276 + 5 + 40 = **321 mOsm/L** แต่ **tonicity = 276 + 5 = 281 mOsm/L** (ปกติ) — urea ผ่านเยื่อหุ้มเซลล์ได้ ความเข้มข้นในเซลล์จึงเท่านอกเซลล์ ไม่ดึงน้ำ ไม่กระตุ้น osmoreceptor\n\n"
         "- **321 = cell dehydration** — ผิด ค่าที่สูงมาจาก urea ซึ่งเป็น ineffective osmole\n- **urea อยู่แต่ใน ECF** — ผิด urea กระจายทั่ว total body water\n"
         "- **glucose เป็นตัวหลัก** — glucose 90 mg/dL ให้เพียง 5 mOsm\n- **Na 1 osmole** — Na ต้องคูณ 2 เพราะมี anion มาด้วย",
         "Urea เพิ่ม Posm แต่ไม่เพิ่ม tonicity", "Effective osmolality and urea", R("Water shift between compartment"), [FLUID_B, OSM_B, CKD]),
     mcq(N(2), "A 58-year-old woman with poorly controlled type 2 diabetes is brought in confused. Serum Na 128 mEq/L, glucose 900 mg/dL, BUN 28 mg/dL. Which best describes her sodium disorder?",
         ["Hypertonic hyponatremia because glucose draws water out of cells and dilutes sodium",
          "Hypotonic hyponatremia requiring 3% saline",
          "Pseudohyponatremia caused by a laboratory artifact from hyperlipidemia",
          "Euvolemic hyponatremia from inappropriate ADH secretion",
          "Isotonic hyponatremia because urea balances the sodium deficit"], 0,
         "Tonicity = 2(128) + 900/18 = 256 + 50 = **306 mOsm/L** (สูง) · glucose ค้างใน ECF ดึงน้ำออกจากเซลล์มาเจือจาง Na → **hypertonic (translocational) hyponatremia** — เซลล์สมองเหี่ยว ไม่ใช่บวม จึงห้ามให้ 3% NaCl · แก้ด้วยสารน้ำและ insulin (Na จะสูงขึ้นเองเมื่อ glucose ลด)\n\n"
         "- **hypotonic + 3% NaCl** — ผิด tonicity สูงอยู่แล้ว\n- **pseudohyponatremia** — เป็นความผิดพลาดของการวัด (ไขมัน/โปรตีนสูงมาก) tonicity ปกติ\n"
         "- **SIADH** — ต้องเป็น hypotonic\n- **urea ชดเชย** — urea ไม่ใช่ effective osmole",
         "Na ต่ำ + glucose สูง → คำนวณ tonicity ก่อนเสมอ", "Hyperglycemia and sodium", R("Water shift between compartment", GH), [LYTE, LYTE_B, DM, OSM_B])],
    [FLUID_B, OSM_B, LYTE], {"osm": F.osm()})

# ═════════════════════════════════════════════ 2
sec("nephro-phy2-02", "Darrow–Yannet — หกแบบของปริมาตรที่ผิดปกติ และเลือกสารน้ำให้ตรง",
    "Iso/hyper/hyposmotic × contraction/expansion · Hct และโปรตีนในพลาสมาบอกอะไร · สารน้ำที่ใช้แก้", 9,
"""### หลักคิด (สไลด์ Types of volume deficit/excess)
ถามสองคำถามเสมอ: **ECF เพิ่มหรือลด** และ **สิ่งที่เสีย/ได้มา เข้มกว่า เท่ากับ หรือจางกว่าพลาสมา**
- เสีย/ได้ของเหลวที่ **เข้มเท่าพลาสมา** → ECF osmolarity ไม่เปลี่ยน → น้ำไม่ย้าย → ICF คงเดิม
- เสีย **น้ำมากกว่า** solute หรือได้ **solute มากกว่า** น้ำ → ECF เข้มขึ้น → น้ำออกจากเซลล์
- เสีย **solute มากกว่า** น้ำ หรือได้ **น้ำมากกว่า** solute → ECF จางลง → น้ำเข้าเซลล์

[[fig:darrow]]

| ชนิด | ตัวอย่าง (สไลด์) | ECF | Posm | ICF | สารน้ำ (สไลด์) |
|---|---|---|---|---|---|
| Isosmotic contraction | diarrhea, vomiting, burn, hemorrhage | ↓ | คงเดิม | คงเดิม | **isotonic: 0.9% NaCl** |
| Hyperosmotic contraction | เหงื่อ ขาดน้ำ ไข้ alcoholism **DI** | ↓ | ↑ | ↓ | **hypotonic: 0.45% NaCl, D5W** |
| Hyposmotic contraction | **adrenal insufficiency/hypoaldosteronism** | ↓↓ | ↓ | ↑ | สไลด์: hypertonic 3% NaCl |
| Isosmotic expansion | ให้ 0.9% NaCl มาก | ↑ | คงเดิม | คงเดิม | — |
| Hyperosmotic expansion | กินเกลือมาก ให้ 3% NaCl | ↑ | ↑ | ↓ | — |
| Hyposmotic expansion | ดื่มน้ำมาก **SIADH** | ↑ | ↓ | ↑ | — |

> ✍️ ลายมือในสไลด์: hyposmotic contraction = "adrenal ไม่หลั่ง aldosterone → เสีย Na มากกว่าน้ำ" · ในทางปฏิบัติ adrenal crisis ส่วนใหญ่แก้ด้วย **0.9% NaCl + hydrocortisone** ส่วน 3% NaCl สงวนไว้เมื่อ Na ต่ำรุนแรงมีอาการทางสมอง (หมายเหตุจากแนวทาง ไม่อยู่ในสไลด์)

### อ่าน Hct และโปรตีนในพลาสมา (สไลด์ Table 6.2 · Costanzo)
Hct = RBC volume ÷ blood volume — RBC เป็น "เซลล์" จึงบวม/เหี่ยวตาม ICF ส่วนโปรตีนในพลาสมาบอกว่าน้ำในหลอดเลือดถูกดึงออกหรือเติมเข้า
| ชนิด | Blood volume | Posm | RBC volume | Hct | Plasma protein |
|---|---|---|---|---|---|
| Iso contraction | ↓ | — | — | ↑ | ↑ |
| Hyperosmotic contraction | ↓ | ↑ | ↓ | **—** | ↑ |
| Hyposmotic contraction | ↓ | ↓ | ↑ | **↑↑** | ↑ |
| Iso expansion | ↑ | — | — | ↓ | ↓ |
| Hyperosmotic expansion | ↑ | ↑ | ↓ | **↓↓** | ↓ |
| Hyposmotic expansion (SIADH) | ↑ | ↓ | ↑ | **—** | ↓ |

#### ทำไมถึงมีอาการนี้
- **ขาดน้ำแบบ hyperosmotic แต่ Hct ไม่สูง** — plasma ลดทำให้ Hct ควรสูง แต่ RBC เหี่ยวลงพร้อมกัน สองแรงหักล้างกัน → ใช้ **โปรตีนในพลาสมา** ดีกว่า
- **SIADH Hct ไม่เปลี่ยน** — plasma เจือจาง (Hct ควรลด) แต่ RBC บวม (Hct ควรเพิ่ม) หักล้างกัน
- **Addison: ขาดน้ำรุนแรงทั้งที่ Na ต่ำ** — เสีย Na ทางไต ECF จางลง → น้ำส่วนหนึ่งย้ายเข้าเซลล์ ECF จึงหดมากกว่าที่ปริมาตรที่เสียบอก → ความดันตก ช็อกง่าย
""",
    ["ถามสองข้อ: ECF ↑ หรือ ↓ · สิ่งที่เสีย/ได้เข้มกว่าหรือจางกว่าพลาสมา",
     "Isosmotic: น้ำไม่ย้าย ICF คงเดิม — เช่น ท้องเสีย เลือดออก ให้ NSS",
     "Hyperosmotic contraction (เหงื่อ ขาดน้ำ DI) → hypotonic fluid · Hyposmotic contraction = adrenal insufficiency",
     "Hct หลอกได้เมื่อ RBC เปลี่ยนขนาด — plasma protein บอกปริมาตรพลาสมาตรงกว่า"],
    [mcq(N(3), "A 30-year-old marathon runner collapses on a hot day after 4 hours of running with little fluid intake. Sweat is hypotonic to plasma. Compared with before the race, which set of changes is expected?",
         ["ECF volume decreased, ICF volume decreased, body fluid osmolarity increased",
          "ECF volume decreased, ICF volume unchanged, body fluid osmolarity unchanged",
          "ECF volume decreased, ICF volume increased, body fluid osmolarity decreased",
          "ECF volume increased, ICF volume decreased, body fluid osmolarity increased",
          "ECF volume unchanged, ICF volume decreased, body fluid osmolarity increased"], 0,
         "เหงื่อจางกว่าพลาสมา = เสีย **น้ำมากกว่า solute** → **hyperosmotic volume contraction**: ECF ลด และเข้มขึ้น → น้ำออกจากเซลล์ → ICF ลดด้วย (ร่างกายแบ่งการขาดน้ำให้ทั้งสอง compartment)\n\n"
         "- **ICF คงเดิม** = isosmotic contraction (ท้องเสีย เลือดออก)\n- **ICF เพิ่ม osmolarity ลด** = hyposmotic contraction (adrenal insufficiency)\n"
         "- **ECF เพิ่ม** = hyperosmotic expansion (กินเกลือมาก)\n- **ECF คงเดิม** — เป็นไปไม่ได้เมื่อเสียน้ำจาก ECF",
         "เหงื่อ = เสียน้ำ > เกลือ → hyperosmotic contraction", "Darrow–Yannet: sweating", R("Types of volume deficit"), [FLUID_B, LYTE_B]),
     mcq(N(4), "A 42-year-old woman with primary adrenal insufficiency presents with fatigue and postural hypotension. Serum Na is 124 mEq/L. Which combination of changes is expected (compared with normal)?",
         ["Blood volume ↓, plasma osmolarity ↓, RBC volume ↑, hematocrit ↑, plasma protein ↑",
          "Blood volume ↓, plasma osmolarity ↑, RBC volume ↓, hematocrit unchanged, plasma protein ↑",
          "Blood volume ↑, plasma osmolarity ↓, RBC volume ↑, hematocrit unchanged, plasma protein ↓",
          "Blood volume ↓, plasma osmolarity unchanged, RBC volume unchanged, hematocrit ↓, plasma protein ↓",
          "Blood volume ↑, plasma osmolarity unchanged, RBC volume unchanged, hematocrit ↓, plasma protein ↓"], 0,
         "ขาด aldosterone → ไตเสีย Na มากกว่าน้ำ = **hyposmotic volume contraction**: ECF ลดและจางลง → น้ำเข้าเซลล์ (RBC บวม) · Hct ขึ้นจากสองแรงที่ไปทางเดียวกัน (plasma ลด + RBC ใหญ่ขึ้น) · โปรตีนเข้มข้นขึ้นเพราะ plasma ลด (สไลด์ Table 6.2)\n\n"
         "- **Posm ↑ RBC ↓ Hct คงเดิม** = hyperosmotic contraction (เหงื่อ DI)\n- **blood volume ↑ Hct คงเดิม** = SIADH\n"
         "- **Posm คงเดิม Hct ↓** — ไม่ใช่ภาวะขาดน้ำแบบใด (ขาดน้ำ Hct ไม่ลด)\n- **iso expansion** = ให้ NSS มาก",
         "Addison = hyposmotic contraction: Hct ↑↑", "Darrow–Yannet: adrenal insufficiency", R("Types of volume deficit · Table 6.2"), [FLUID_B, ADDISON_B, HORMDIS])],
    [FLUID_B, LYTE, LYTE_B, FLUIDDRUG_B, ADDISON_B, SIADH], {"darrow": F.darrow()})

# ═════════════════════════════════════════════ 3
sec("nephro-phy2-03", "ไตคุมปริมาตรด้วยการขับ Na — การกรอง การดูดกลับ และ sympathetic",
    "Autoregulation ตรึง GFR · glomerulotubular balance · FF กับแรง Starling ที่ peritubular capillary · pressure natriuresis", 9,
"""### หลักใหญ่: ปริมาตร ECF = ปริมาณ Na ในร่างกาย
Na เป็นตัวถูกละลายหลักของ ECF และน้ำตาม Na เสมอ (ผ่าน ADH/thirst) — **ไตคุมปริมาตรด้วยการคุมการขับ Na** (✍️ ลายมือ: สมดุล Na = สมดุลน้ำ) · ทำได้สองทาง (สไลด์ Renal regulates body fluid volume)

### 1) ทางการกรอง
- **ภาวะปกติ**: autoregulation ตรึง GFR ไว้เมื่อ MAP อยู่ราว **80–170 mmHg** → filtered load ของ Na และน้ำแทบไม่เปลี่ยน (รายละเอียดกลไก myogenic/TGF ใน Part I)
- **เมื่อร่างกายขาดน้ำมาก**: sympathetic + Ang II → renal arteriole หดตัว → RBF ↓ → GFR ↓ → filtered load ↓

### 2) ทางการดูดกลับ — ตัวคุมหลัก
| ดูด Na กลับ | ดูดน้ำกลับ |
|---|---|
| glomerulotubular balance | glomerulotubular balance |
| sympathetic: ↑ ดูด Na ที่ PT, TAL, DT, CD | gradient ใน medulla (ทบทวน countercurrent ใน Part I) |
| ฮอร์โมน: Ang II, epinephrine, aldosterone, ADH (↑) · ANP (↓) | ADH |

[[fig:na_segments]]

### Glomerulotubular balance และ filtration fraction
**Glomerulotubular balance** = PT ดูดกลับเป็น **สัดส่วนคงที่ (~65%)** ของที่กรองมา แม้ GFR จะเปลี่ยน — ป้องกันไม่ให้ GFR ที่แกว่งเล็กน้อยทำให้ Na หลุดออกมาก
กลไกสำคัญคือ **แรง Starling ที่ peritubular capillary** ซึ่งขึ้นกับ filtration fraction (FF = GFR/RPF):
- **↓ BV → ↓ BP → ↑ sympathetic & Ang II** → efferent หด → GFR ลดเล็กน้อยแต่ RPF ลดมาก → **↑ FF** → เลือดที่ออกจาก glomerulus มี **Pc ↓ และ πc ↑** → ดูดน้ำและ Na จาก interstitium รอบ PT กลับเข้าหลอดเลือดได้ดี → **↓ ขับ Na**
- **↑ BV → ↑ BP** → ทำตรงข้าม → ↓ FF → Pc ↑ πc ↓ → PT ดูดกลับน้อยลง → **↑ ขับ Na = pressure natriuresis**

[[fig:ff]]

### Sympathetic — ระบบตอบสนองเร็ว (สไลด์ Sympathetic activity)
↓ blood volume/BP → cardiovascular center → ↑ sympathetic ไปที่ไต 4 จุดพร้อมกัน:
1. renal artery/arteriole หดตัว → ↓ RBF
2. **mesangial cell หดตัว** → พื้นที่กรองลด → ↓ GFR
3. **JG cell (β1) → ↑ renin** → RAAS (หัวข้อ 4)
4. **ท่อไตดูด Na กลับมากขึ้นโดยตรง**
→ ผลรวม **↓ ขับ NaCl และน้ำ** · ถูกยับยั้งด้วยปริมาตร/ความดันสูงและ ANP

#### ทำไมถึงมีอาการนี้
| ภาวะ | กลไก | ผลที่ตรวจพบ |
|---|---|---|
| Prerenal (ขาดน้ำ หัวใจวาย) | sympathetic + Ang II + FF สูง → PT ดูด Na และ urea กลับมาก | **FENa < 1%** · UNa < 20 · BUN/Cr > 20 |
| ความดันโลหิตสูงในคนกินเค็ม | ไตต้องใช้ความดันที่สูงขึ้นเพื่อขับ Na เท่าที่กินเข้าไป (pressure natriuresis เลื่อนไปทางขวา) | BP ขึ้นตามปริมาณเกลือ (salt-sensitive) |
| ยา NSAID ในผู้ที่ปริมาตรต่ำ | ตัด prostaglandin ที่ขยาย afferent ซึ่งเป็นตัวถ่วง sympathetic/Ang II | GFR ตกเฉียบพลัน |
> ส่วน "ทำไม" ในตารางเชื่อมกับคลินิกจาก Guyton & Hall — สไลด์สอนเฉพาะกลไก
""",
    ["Autoregulation (MAP 80–170) ตรึง GFR → ไตคุม Na ด้วยการดูดกลับเป็นหลัก",
     "FF ↑ → Pc ↓ πc ↑ ที่ peritubular capillary → PT ดูด Na กลับมาก",
     "ความดันสูง → PT ดูดเหลือ ~50% → ขับ Na 6% = pressure natriuresis (สไลด์)",
     "Sympathetic ต่อไต: หลอดเลือดหด · mesangial หด · renin (β1) · ดูด Na โดยตรง"],
    [mcq(N(5), "A 25-year-old man loses 1.5 L of blood after a motorcycle accident. Renal sympathetic activity and angiotensin II rise, constricting the efferent arteriole more than the afferent arteriole. Which change in the peritubular capillary best explains the increased proximal tubular Na reabsorption?",
         ["Lower hydrostatic pressure and higher oncotic pressure in the peritubular capillary because filtration fraction rises",
          "Higher hydrostatic pressure and lower oncotic pressure in the peritubular capillary because filtration fraction falls",
          "Increased delivery of NaCl to the macula densa that stimulates renin",
          "Direct inhibition of the Na/K-ATPase in proximal tubular cells by angiotensin II",
          "Increased atrial natriuretic peptide acting on the proximal tubule"], 0,
         "efferent หด → GFR ลดน้อยแต่ RPF ลดมาก → **FF สูงขึ้น** → เลือดที่ไหลต่อไปเป็น peritubular capillary **โปรตีนเข้มข้น (πc ↑) และความดันต่ำ (Pc ↓)** → ดึงของเหลวจาก interstitium รอบ PT กลับเข้าหลอดเลือดได้มาก → PT ดูด Na กลับมากขึ้น (สไลด์ Glomerulotubular balance)\n\n"
         "- **Pc ↑ πc ↓** = ภาวะปริมาตรเกิน\n- **NaCl ถึง macula densa มากขึ้น** — ตรงข้าม ในภาวะเสียเลือด NaCl ที่ไปถึงลดลง\n"
         "- **Ang II ยับยั้ง Na/K-ATPase** — ผิด Ang II **เพิ่ม** NHE3 และการดูด Na\n- **ANP** — ลดลงเมื่อปริมาตรลด และ ANP ลดการดูด Na",
         "Hypovolemia → ↑FF → ↓Pc ↑πc → ↑ PT reabsorption", "Peritubular Starling forces", R("Glomerulotubular balance"), [GFR_B, HANDLE_B, SHOCK, HYPOVOL_B]),
     mcq(N(6), "Which statement best defines glomerulotubular balance?",
         ["The proximal tubule reabsorbs a nearly constant fraction of the filtered Na load when GFR changes",
          "The macula densa senses NaCl delivery and adjusts afferent arteriolar tone to keep GFR constant",
          "Aldosterone increases Na reabsorption in the collecting duct when GFR falls",
          "The afferent arteriole constricts in response to increased stretch to keep renal blood flow constant",
          "Filtered Na load always equals urinary Na excretion"], 0,
         "**Glomerulotubular balance** = การดูดกลับที่ PT **ปรับตามสัดส่วน** ของ filtered load (~65%) — GFR เพิ่ม PT ก็ดูดเพิ่ม (ส่วนหนึ่งผ่าน FF และ Starling force ที่ peritubular capillary) Na ที่หลุดไปส่วนปลายจึงแทบไม่เปลี่ยน\n\n"
         "- **macula densa ปรับ afferent** = tubuloglomerular feedback (ส่วนหนึ่งของ autoregulation — คนละกลไก)\n- **aldosterone** — เป็นการคุมด้วยฮอร์โมนที่ CD ไม่ใช่ GT balance\n"
         "- **afferent หดเมื่อถูกยืด** = myogenic mechanism\n- **filtered = excreted** — ผิด ปกติขับทิ้ง < 1% ของที่กรอง",
         "GT balance = PT ดูดเป็นสัดส่วนคงที่ · TGF = macula densa ปรับ GFR", "Glomerulotubular balance vs TGF", R("Renal regulating Na and water reabsorption"), [GFR_B, TUB_B, HANDLE_B])],
    [HANDLE_B, GFR_B, TUB_B, BP_B, HYPOVOL_B], {"na_segments": F.na_segments(), "ff": F.ff()})

# ═════════════════════════════════════════════ 4
sec("nephro-phy2-04", "RAAS, aldosterone และ ANP — คันเร่งกับเบรกของการเก็บ Na",
    "ตัวกระตุ้น renin · Ang II ทำอะไรบ้าง · aldosterone ที่ P cell และ A-IC · ANP ยับยั้งทุกจุด", 9,
"""### Renin–angiotensin–aldosterone (สไลด์ RAA system · Sherwood)
**ตัวกระตุ้น renin จาก JG cell** — ↓ ความดันที่ afferent arteriole (baroreceptor ในผนัง) · ↓ NaCl ที่ไปถึง **macula densa** · ↑ **sympathetic (β1)**
angiotensinogen (ตับ) → **renin** → Ang I → **ACE** (endothelium โดยเฉพาะปอด) → **Ang II**

| Ang II ทำที่ | ผล |
|---|---|
| หลอดเลือดแดงทั่วตัว | หดตัว → ↑ BP |
| efferent arteriole (มากกว่า afferent) | รักษา GFR · ↑ FF → ↑ ดูดกลับที่ PT |
| PT | ↑ **NHE3** → ดูด Na และ HCO3 กลับ (ที่มาของ contraction alkalosis) |
| adrenal cortex (zona glomerulosa) | ↑ **aldosterone** |
| hypothalamus | ↑ ADH และกระหายน้ำ |
| cardiovascular center | ↑ sympathetic |

[[fig:raas]]

### Aldosterone (สไลด์ Aldosterone)
- **กระตุ้น**: ↓ Na ในพลาสมา · ↓ ปริมาตร/ความดัน (ผ่าน sympathetic → renin → Ang II) · **↑ K ในพลาสมา (กระตุ้นโดยตรง)**
- **ยับยั้ง**: osmolality สูงมาก · **ANP** · อาหารเค็ม
- **ทำที่ late DT และ CD**: **P cell** ↑ ดูด Na (ENaC + Na/K-ATPase) ↑ ขับ K · **type A-IC** ↑ ขับ H (H+-ATPase)
- ✍️ ลายมือ: ↑K ในเลือดกระตุ้น aldosterone เพื่อขับ K ออก — ฮอร์โมนตัวเดียวคุมทั้งปริมาตรและ K

### ANP — เบรกของระบบ (สไลด์ Atrial natriuretic peptide)
↑ blood volume → atrial myocyte ถูกยืด → ANP →
- CVS center: ↓ sympathetic → ↓ BP · hypothalamus: **↓ ADH** · adrenal: **↓ aldosterone**
- ไต: **↓ renin** (→ ↓ Ang II) · **afferent arteriole ขยาย** → ↑ RBF · **mesangial (GMC) คลาย** → ↑ GFR · **↓ ดูด Na ที่ P cell**
- ผลรวม **↑ ขับ NaCl และน้ำ** (✍️ ANP เป็นตัวเดียวในกลุ่มที่ "ขับ" Na)

#### ทำไมถึงมีอาการนี้
| ภาวะ | กลไก | ผลที่เห็น |
|---|---|---|
| **Primary aldosteronism** | aldosterone สูงเองไม่ขึ้นกับ renin → ENaC ทำงานตลอด | ความดันสูง · **K ต่ำ** · metabolic alkalosis · renin ถูกกดต่ำ · บวมน้อยเพราะ "aldosterone escape" (pressure natriuresis + ANP) |
| **Addison disease** | ขาด aldosterone → ไม่ดูด Na ที่ P cell → lumen ไม่เป็นลบ → ไม่ขับ K/H | Na ต่ำ · **K สูง** · normal AG acidosis · ความดันตก |
| **ACEi/ARB, spironolactone** | ตัดทาง Ang II/aldosterone | K สูงขึ้น โดยเฉพาะใน CKD หรือใช้ร่วมกัน |
| หัวใจวาย ตับแข็ง | effective circulating volume ต่ำ ทั้งที่น้ำทั้งตัวเกิน → RAAS + sympathetic + ADH ทำงานเต็มที่ | บวม · Na ต่ำ · UNa ต่ำ |
> แถว primary aldosteronism/aldosterone escape และหัวใจวายเติมจาก Guyton & Hall — สไลด์สอนกลไกพื้นฐาน
""",
    ["Renin: ↓ ความดัน afferent · ↓ NaCl ที่ macula densa · ↑ sympathetic β1",
     "Ang II: หลอดเลือดหด · efferent หด · NHE3 ที่ PT · aldosterone · ADH/thirst",
     "Aldosterone ถูกกระตุ้นโดยตรงจาก K สูง → P cell ดูด Na ขับ K · A-IC ขับ H",
     "ANP: ↓ renin/aldo/ADH · ขยาย afferent · คลาย mesangial · ↓ ดูด Na ที่ P cell"],
    [mcq(N(7), "A 38-year-old woman with Addison disease presents with Na 126 mEq/L and K 6.2 mEq/L. Which mechanism best explains her hyperkalemia?",
         ["Lack of aldosterone reduces ENaC-mediated Na entry in principal cells, so the lumen is less negative and K secretion falls",
          "Cortisol deficiency inhibits Na/K-ATPase in skeletal muscle, shifting K out of cells",
          "Excess ADH increases K reabsorption in the medullary collecting duct",
          "Renin deficiency reduces angiotensin II–stimulated K secretion in the proximal tubule",
          "Hyponatremia directly opens ROMK channels in the thick ascending limb, causing K reabsorption"], 0,
         "aldosterone ทำให้ P cell เพิ่ม **ENaC, ROMK และ Na/K-ATPase** · เมื่อขาด aldosterone Na เข้าเซลล์ทาง ENaC น้อย → lumen ไม่เป็นลบ และ K ในเซลล์ไม่ถูกปั๊มเข้ามา → **ขับ K ลดลง** → K สูง (สไลด์ Aldosterone · Factors affecting K secretion)\n\n"
         "- **cortisol กับ Na/K-ATPase** — ปัจจัย shift หลักคือ insulin β2 aldosterone ไม่ใช่ cortisol\n- **ADH เพิ่มการดูด K** — ผิด ADH ไม่ใช่ตัวคุม K หลัก\n"
         "- **renin deficiency** — Addison มี renin **สูง** (ปฐมภูมิที่ adrenal) และการขับ K ไม่ได้เกิดที่ PT\n- **ROMK ใน TAL** — ROMK ใน TAL ใช้ recycle K ไม่ใช่กลไกนี้",
         "ขาด aldosterone → ไม่ดูด Na ที่ P cell → ไม่ขับ K", "Aldosterone and K secretion", R("Aldosterone · Factors affecting tubular K secretion"), [ADDISON_B, HYPERK, HANDLE_B, HORMDIS]),
     mcq(N(8), "In a patient with acute volume overload, atrial stretch releases atrial natriuretic peptide (ANP). Which effect of ANP contributes to natriuresis?",
         ["Dilation of the afferent arteriole and relaxation of mesangial cells, increasing GFR",
          "Stimulation of aldosterone secretion from the zona glomerulosa",
          "Increased ENaC activity in principal cells of the collecting duct",
          "Increased ADH secretion from the posterior pituitary",
          "Stimulation of renin release from juxtaglomerular cells"], 0,
         "ANP ทำให้ **afferent ขยาย + mesangial คลาย** → GFR และ filtered load เพิ่ม และ **ยับยั้ง renin, aldosterone, ADH และ ENaC/การดูด Na ที่ P cell** → ขับ NaCl และน้ำ (สไลด์ ANP)\n\n"
         "ตัวเลือกที่เหลือเป็นผลที่ **ตรงข้าม** กับ ANP ทั้งหมด: ANP **ลด** aldosterone · **ลด** การดูด Na ที่ P cell · **ลด** ADH · **ลด** renin",
         "ANP = เบรกของ RAAS/ADH + เพิ่ม GFR", "ANP actions", R("Atrial natriuretic peptide (ANP)"), [HORM_B, HANDLE_B, RAAS_B])],
    [RAAS_B, HORM_B, HANDLE_B, CONN_B, ADDISON_B, HYPERK], {"raas": F.raas()})

# ═════════════════════════════════════════════ 5
sec("nephro-phy2-05", "ADH และการกระหายน้ำ — ตัวคุม osmolality",
    "Osmoreceptor เทียบ baroreceptor/volume receptor · V2R → AQP2 · ADH ทำ 3 อย่างที่ท่อไต · เกณฑ์ 275–295 · DI กับ SIADH", 9,
"""### ใครสั่งให้หลั่ง ADH (สไลด์ Antidiuretic hormone)
| ตัวกระตุ้น | ตัวรับ | หมายเหตุ |
|---|---|---|
| **↑ effective plasma osmolality (tonicity)** | **osmoreceptor** ใน hypothalamus | ไวที่สุด — เปลี่ยน 1–2% ก็ตอบ · ✍️ urea ไม่นับ |
| ↓ effective circulating volume | volume receptor (atrium และปอด) | ต้องลดราว 5–10% แต่เมื่อลดมาก "ชนะ" osmolality |
| ↓ BP | baroreceptor (aortic arch, carotid sinus) | |
| ยา | **morphine, nicotine กระตุ้น** · **alcohol, ANP ยับยั้ง** | ดื่มเหล้าแล้วปัสสาวะบ่อย = ADH ถูกกด |

osmoreceptor รับรู้การเปลี่ยนแปลงความเข้มข้นของ ECF **ผ่านการที่น้ำเคลื่อนเข้า-ออกตัวเซลล์เอง**: ECF เข้มขึ้น → เซลล์ osmoreceptor เหี่ยว → ยิงสัญญาณ → ↑ ADH · ECF จาง → เซลล์บวม → ↓ ADH
- ADH สร้างที่ supraoptic/paraventricular nucleus เก็บและหลั่งที่ **posterior pituitary**
- **Posm ปกติ 285–295 · ต่ำกว่า 275 mOsm/L ไม่มีการหลั่ง ADH** (สไลด์)
- ADH ขนาดสูง → **V1R** ที่หลอดเลือด → หดตัว (จึงชื่อ vasopressin)

[[fig:adh_curve]]

### ADH ทำ 3 อย่างที่ท่อไต (สไลด์ ADH affecting on renal tubule)
1. ↑ water permeability ที่ **late DT และ collecting duct** → ดูดน้ำกลับ — ผ่าน **V2R → Gs → cAMP → PKA → แทรก AQP2**
2. ↑ ดูด NaCl ที่ **TAL** → ↑ gradient ใน medulla
3. ↑ ดูด **urea** ที่ inner medullary CD → ↑ osmolality ของ inner medulla
→ 2 และ 3 คือการ "สร้างแรงดูด" ส่วน 1 คือ "เปิดประตู"

[[fig:adh]]

### Thirst center (สไลด์ Thirst center)
กระตุ้นด้วย ↑ osmolality (สำคัญที่สุด) · ↓ ปริมาตร atrium · ↓ BP · **↑ Ang II** · ปากแห้ง
✍️ **กระเพาะที่ยืดจากการดื่ม ยับยั้งความกระหายก่อนที่น้ำจะถูกดูดซึม** — ป้องกันการดื่มเกิน

#### ทำไมถึงมีอาการนี้
| ภาวะ | กลไก | ผลที่ตรวจพบ |
|---|---|---|
| **Central DI** (หลังผ่าตัด/บาดเจ็บ pituitary) | ไม่มี ADH → AQP2 ไม่ถูกแทรก → CD ไม่ให้น้ำผ่าน | ปัสสาวะจางมาก (Uosm < 300 บางครั้ง < 100) หลายลิตร · Na สูงถ้าดื่มไม่ทัน · **ให้ desmopressin แล้ว Uosm ขึ้น** |
| **Nephrogenic DI** (lithium, Ca สูง, K ต่ำ) | มี ADH แต่ V2R/AQP2 ไม่ตอบ (lithium เข้า principal cell ทาง ENaC แล้วกด AQP2) | เหมือนข้างบน แต่ **desmopressin ไม่ช่วย** |
| **SIADH** | ADH หลั่งทั้งที่ Posm ต่ำ | Na ต่ำ · Uosm สูงเกินกว่าที่ควร (หัวข้อ 7) |
| ปริมาตรลดมาก (หัวใจวาย ตับแข็ง อาเจียน) | volume/baroreceptor กระตุ้น ADH ชนะ osmoreceptor | Na ต่ำ แม้ Posm ต่ำ |
> แถว DI/lithium เติมจากตำรา (Boron · Guyton) — สไลด์กล่าวถึง DI ในตัวอย่าง hyperosmotic contraction
""",
    ["ADH: osmoreceptor ไวสุด · volume/baroreceptor แรงสุดเมื่อปริมาตรลดมาก",
     "Posm < 275 → ไม่มี ADH · ปกติ 285–295",
     "V2R → cAMP → PKA → AQP2 แทรกที่ apical membrane ของ principal cell",
     "ADH ยัง ↑ NaCl ที่ TAL และ urea ที่ IMCD เพื่อสร้าง gradient",
     "Alcohol และ ANP กด ADH · morphine nicotine กระตุ้น"],
    [mcq(N(9), "Two days after transsphenoidal pituitary surgery, a 45-year-old man passes 6 L of urine per day. Serum Na 149 mEq/L, plasma osmolality 302 mOsm/kg, urine osmolality 90 mOsm/kg. After subcutaneous desmopressin, urine osmolality rises to 450 mOsm/kg. What is the most likely diagnosis?",
         ["Central diabetes insipidus", "Nephrogenic diabetes insipidus", "Primary polydipsia",
          "Osmotic diuresis from hyperglycemia", "Syndrome of inappropriate ADH secretion"], 0,
         "ปัสสาวะจางมาก (90) ทั้งที่ Posm สูง (302) = ไตไม่ได้รับสัญญาณ ADH · ให้ desmopressin แล้ว Uosm เพิ่ม 5 เท่า = **ท่อไตตอบสนองได้ แต่ร่างกายไม่สร้าง ADH** → **central DI** (เข้ากับการผ่าตัด pituitary)\n\n"
         "- **nephrogenic DI** — desmopressin จะไม่ทำให้ Uosm เพิ่มชัด\n- **primary polydipsia** — Posm และ Na จะ **ต่ำ/ปกติต่ำ** ไม่ใช่ 149/302\n"
         "- **osmotic diuresis** — Uosm มักอยู่ราว 300 ขึ้นไป ไม่ใช่ 90\n- **SIADH** — Na ต่ำ ปัสสาวะเข้มข้น",
         "Posm สูง + Uosm ต่ำ → DI · ตอบ desmopressin = central", "Central DI physiology", R("Antidiuretic hormone", BB), [DI_B, HORMDIS, POLY, OSM_B]),
     mcq(N(10), "Which sequence correctly describes how ADH increases water reabsorption in the collecting duct?",
         ["V2 receptor → Gs → cAMP → protein kinase A → insertion of aquaporin-2 into the apical membrane of principal cells",
          "V1 receptor → Gq → IP3 → insertion of aquaporin-1 into the basolateral membrane of intercalated cells",
          "V2 receptor → Gi → decreased cAMP → removal of aquaporin-2 from the apical membrane",
          "Nuclear mineralocorticoid receptor → transcription of ENaC → water follows Na through ENaC",
          "V2 receptor → opening of aquaporin-3 in the apical membrane of the thick ascending limb"], 0,
         "ADH จับ **V2R ด้าน basolateral** ของ **principal cell** → Gs → adenylyl cyclase → cAMP → PKA → ถุงที่มี **AQP2 ถูกส่งไปแทรกที่ apical membrane** (ระยะยาวเพิ่มการสร้าง AQP2) → น้ำออกทาง **AQP3/4 ด้าน basolateral**\n\n"
         "- **V1/Gq** — เป็นทางหดหลอดเลือด · AQP1 อยู่ที่ PT และ thin descending limb ไม่ถูก ADH คุม\n- **Gi ลด cAMP** — ตรงข้าม\n"
         "- **MR → ENaC** = กลไก aldosterone ไม่ใช่ ADH และน้ำไม่ผ่าน ENaC\n- **TAL** — ไม่ให้น้ำผ่านเลยแม้มี ADH (ADH เพิ่มแค่ NaCl)",
         "V2R → cAMP → AQP2 (apical) · AQP3/4 (basolateral)", "ADH signaling", R("ADH affecting on renal tubule", BB), [HORM_B, TUB_B, DI_B])],
    [HORM_B, TUB_B, OSM_B, DI_B, SIADH_B, POLY], {"adh_curve": F.adh_curve(), "adh": F.adh()})

# ═════════════════════════════════════════════ 6
sec("nephro-phy2-06", "ร่างกายตอบสนองแบบบูรณาการ — ขาดน้ำ ดื่มน้ำมาก กินเค็ม ออกกำลังกาย",
    "Flowchart ของสไลด์ทีละขั้น · Uosm/Posm · free water clearance · BUN/Cr · อาการแสดงของปริมาตรลด/เกิน", 10,
"""### Hyperosmotic volume contraction — ขาดน้ำ/เหงื่อออก (สไลด์ flowchart)
**ด้าน osmolality**: ↑ Posm → osmoreceptor → **↑ ADH** + **กระหายน้ำ** → ดูดน้ำที่ late DT/CD · ↑ NaCl ที่ TAL · ↑ urea ที่ IMCD → **antidiuresis**: ปัสสาวะน้อย Uosm สูง **Uosm/Posm > 1** · free water clearance (CH2O) ติดลบ
**ด้านปริมาตร**: ↓ BV/BP → baroreceptor + volume receptor → ↓ ANP · ↑ sympathetic → afferent หด (↓ GFR) efferent หด (↑ FF → ↓ Pc ↑ πc → ↑ ดูดที่ PT) · ↑ renin → Ang II → aldosterone → ↑ ดูด Na ที่ P cell → **FENa ต่ำ**
**ผลพลอยได้ที่สไลด์ชี้**:
- Ang II ↑ NHE3 + aldosterone ↑ H+-ATPase → ↑ ขับ H ↑ ดูด HCO3 → **contraction alkalosis**
- ADH ↑ urea reabsorption + flow ช้า → **↑ BUN และ BUN/Cr ratio** (prerenal)
- flow ช้า → solute wash-out ลดลง ไตเข้มข้นได้มากขึ้น

### Hyposmotic volume expansion — ดื่มน้ำมาก
↓ Posm → **ADH ถูกกด** + ไม่กระหาย · ↑ ANP · ↓ sympathetic → ↓ renin/Ang II/aldo · ↑ GFR · ↓ FF → **water diuresis**: ปัสสาวะมาก จาง **Uosm/Posm < 1** CH2O เป็นบวก · ✍️ ไตขับ Na เพิ่มเล็กน้อยด้วย
### Hyperosmotic volume expansion — กินเค็ม (สไลด์ Salty diet)
↑ Posm → ↑ ADH + ดื่มน้ำ → Posm กลับปกติ **อย่างรวดเร็ว** · แต่ BV ที่เพิ่ม → ↑ ANP ↓ RAAS ↓ sympathetic → **ขับ NaCl และน้ำ (ช้า)** จนปริมาตรกลับ — ✍️ หลังกินเค็มจึงคอแห้งก่อน แล้วค่อยปัสสาวะมาก
### ออกกำลังกาย (สไลด์ Exercise)
เหงื่อ + หายใจทางปาก (insensible loss เพิ่มเพราะ VT และ RR สูง) → เสียน้ำ > solute → ↑ ADH + กระหาย · sympathetic จาก central command → afferent หด ↓ RBF/GFR · RAAS ↑ → **antidiuresis**

[[fig:urine_vol]]

> **ปริมาณปัสสาวะ = ภาระ osmole ÷ Uosm** และค่า Uosm ต่ำสุด ~50 สูงสุด ~1,200 mOsm/kg เติมจาก Guyton & Hall — ใช้อธิบายว่าทำไมไตขับน้ำได้ "ไม่จำกัด" ไม่จริง

### อาการแสดง (สไลด์ Volume contraction/expansion)
| | ปริมาตรลด | ปริมาตรเกิน |
|---|---|---|
| น้ำหนักเปลี่ยนเฉียบพลัน | mild 2% · moderate 2–5% · severe ≥ 8% | mild 2% · moderate 5% · severe ≥ 8% |
| ในหลอดเลือด | postural hypotension · ชีพจรเร็วเบา · **neck vein แฟบ** | ชีพจรแรง · **JVD** · pulmonary edema (หอบ crackles ไอ) |
| interstitial | ตาโหล ลูกตานิ่ม · กระหม่อมบุ๋มในทารก | บวมตามที่ต่ำ/ทั้งตัว |
| osmolality สูง | กระหาย ปากแห้ง น้ำลายน้อย **skin turgor ไม่ดี** | — |
| ADH ชดเชย | ปัสสาวะน้อย Uosm สูง | — |
| อื่น ๆ | ไข้ในช่วงแรก (คุมอุณหภูมิได้ไม่ดี) | — |
**สาเหตุปริมาตรลด (สไลด์)**: กินน้ำไม่ได้ (บาดเจ็บช่องปาก กลืนไม่ได้ ไม่รู้สึกกระหาย หมดสติ) · ทางเดินอาหาร (อาเจียน ท้องเสีย) · ไต (ยาขับปัสสาวะ osmotic diuresis Addison) · ผิวหนัง (ไข้ เหงื่อ แผลไฟไหม้) · เสียเลือด · third space (บวม ascites)
**สาเหตุปริมาตรเกิน (สไลด์)**: ขับ Na/น้ำไม่ได้ (หัวใจวาย ไตวาย corticosteroid สูง — hyperaldosteronism Cushing — ตับแข็ง) · ได้ Na มาก (อาหาร ยา สารน้ำที่มี Na) · ได้น้ำมาก (ดื่ม/ให้สารน้ำหรือเลือดเร็วเกิน)

#### ทำไมถึงมีอาการนี้
- **skin turgor ไม่ดี** — interstitial fluid ใต้ผิวหนังลดและ ECF เข้มข้น ผิวที่ถูกดึงจึงคืนตัวช้า
- **orthostatic hypotension + ชีพจรเร็ว** — preload ต่ำ เมื่อยืนเลือดไปกองที่ขา baroreflex เร่งหัวใจแต่ชดเชยไม่พอ
- **BUN/Cr > 20 ในขาดน้ำ** — creatinine ถูกกรองอย่างเดียว ส่วน urea ถูกดูดกลับตามน้ำมากขึ้นเมื่อ flow ช้าและ ADH สูง
""",
    ["ขาดน้ำ: ADH + RAAS + sympathetic → Uosm/Posm > 1 · FENa ต่ำ · BUN/Cr สูง · contraction alkalosis",
     "ดื่มน้ำมาก: ADH ถูกกด → water diuresis Uosm/Posm < 1",
     "กินเค็ม: osmolality กลับเร็วด้วย ADH+ดื่ม ปริมาตรกลับช้าด้วย ANP/ลด RAAS",
     "ปัสสาวะต่อวัน = osmole load ÷ Uosm (min ~0.5 L ที่ Uosm 1,200)",
     "Weight loss ≥ 8% = ขาดน้ำรุนแรง"],
    [mcq(N(11), "An 84-year-old bedridden woman with dementia has had poor oral intake for 4 days during a heat wave. BP 96/60 mmHg lying, HR 112/min. Serum Na 151 mEq/L, BUN 64 mg/dL, Cr 1.9 mg/dL. Which urine findings are most consistent with her physiological response?",
         ["Urine osmolality 820 mOsm/kg, urine Na 10 mEq/L, FENa 0.3%",
          "Urine osmolality 120 mOsm/kg, urine Na 10 mEq/L, FENa 0.3%",
          "Urine osmolality 300 mOsm/kg, urine Na 60 mEq/L, FENa 3%",
          "Urine osmolality 820 mOsm/kg, urine Na 80 mEq/L, FENa 4%",
          "Urine osmolality 90 mOsm/kg, urine Na 60 mEq/L, FENa 2.5%"], 0,
         "**hyperosmotic volume contraction**: Posm สูง → **ADH สูง** → ปัสสาวะเข้มข้น (Uosm >> Posm) · ปริมาตรลด → sympathetic + RAAS + FF สูง → ดูด Na กลับเกือบหมด → **UNa < 20, FENa < 1%** · BUN/Cr = 64/1.9 ≈ 34 (> 20) เข้ากับ prerenal\n\n"
         "- **Uosm 120** — ปัสสาวะจางทั้งที่ Na 151 = DI ไม่ใช่การตอบสนองปกติ\n- **Uosm 300 UNa 60 FENa 3%** = ท่อไตเสีย (ATN) หรือได้ยาขับปัสสาวะ\n"
         "- **Uosm 820 UNa 80** — ผสมกัน: ADH ทำงานแต่ไตไม่เก็บ Na (เช่น ได้ diuretic, adrenal insufficiency) ไม่ใช่ขาดน้ำธรรมดา\n- **Uosm 90** = water diuresis",
         "ขาดน้ำ + ไตปกติ → Uosm สูง UNa ต่ำ FENa < 1%", "Integrated response to dehydration", R("Hyperosmotic volume contraction flowchart · Volume contraction"), [FLUID_B, OLIG, OLIG_B, OSM_B, HYPOVOL_B]),
     mcq(N(12), "A 52-year-old man drinks about 6 L of beer daily and eats almost nothing; his daily solute intake is about 300 mOsm. His kidneys can dilute urine to a minimum of 60 mOsm/kg. What is the maximum volume of water he can excrete per day before plasma Na starts to fall?",
         ["0.25 L", "2.5 L", "5 L", "10 L", "20 L"], 2,
         "ปริมาณปัสสาวะ = **ภาระ osmole ÷ Uosm** = 300 ÷ 60 = **5 L/วัน** · ดื่มเบียร์ 6 L (น้ำเกือบทั้งหมด solute น้อย) จึงเกินกำลังขับ → น้ำค้าง → Na ตก = **beer potomania** แม้ ADH จะถูกกดเต็มที่\n\n"
         "- **0.25 L** = เอา 300 ÷ 1,200 (ใช้ค่า Uosm สูงสุด) แล้วผิดหลัก\n- **2.5 L** = ใช้ Uosm 120\n- **10/20 L** — เป็นไปได้เฉพาะเมื่อ solute สูงกว่านี้มาก (Guyton: ~20 L เมื่อกินปกติและ ADH เป็นศูนย์)",
         "ไตขับน้ำได้ = solute load ÷ Uosm ต่ำสุด", "Solute load and water excretion", R("Hyposmotic volume expansion", GH), [FLUID_B, LYTE, OSM_B])],
    [FLUID_B, OSM_B, HYPOVOL_B, EDEMA, OLIG, PULMED], {"urine_vol": F.urine_vol()}, source=SRC_ADD)

# ═════════════════════════════════════════════ 7
sec("nephro-phy2-07", "สะพานสู่คลินิก — SIADH, hyponatremia และ osmotic demyelination",
    "อ่าน hyponatremia ด้วยสรีรวิทยา: tonicity → ADH → ปริมาตร · ทำไม SIADH ปัสสาวะยังมี Na · สมองปรับตัวและขีดจำกัดการแก้", 9,
"""> หัวข้อนี้ **ต่อยอดจากสไลด์** (SIADH = hyposmotic volume expansion) ด้วยตำราและ **European clinical practice guideline on hyponatraemia (Spasovski et al. 2014)** · การรักษาเต็มรูปแบบอยู่ในคาบ 22 Dysnatremia & Dyskalemia (อ.ชุมพล — ยังไม่มีบทเรียน)

### Hyponatremia คือปัญหา "น้ำ" ไม่ใช่ปัญหา "Na"
Na ในเลือดต่ำเกือบทุกรายเกิดจาก **น้ำเกินเมื่อเทียบกับ Na** และน้ำจะค้างได้ก็ต่อเมื่อ **ไตขับน้ำไม่ได้** — ส่วนใหญ่เพราะ **ADH ยังหลั่งอยู่** ทั้งที่ Posm ต่ำ
ไล่ตามสรีรวิทยา 3 ขั้น:
1. **tonicity** — ต่ำจริงไหม (ตัด hyperglycemia/pseudohyponatremia — หัวข้อ 1)
2. **ไตขับน้ำได้ไหม** — Uosm < 100 = ADH ถูกกดแล้ว (ดื่มมาก/solute น้อย) · Uosm > 100 = ADH ทำงาน
3. **ทำไม ADH ยังทำงาน** — ดูปริมาตร: ลด (อาเจียน ท้องเสีย ยาขับปัสสาวะ) · เกินแบบบวม (หัวใจวาย ตับแข็ง — effective volume ต่ำ) · ปกติ (**SIADH**, hypothyroid, ขาด cortisol)

[[fig:siadh]]

| | ปริมาตรลด (อาเจียน) | SIADH | หัวใจวาย/ตับแข็ง |
|---|---|---|---|
| ADH | สูง (volume) | สูง (inappropriate) | สูง (effective volume ต่ำ) |
| RAAS | สูง | **ต่ำ** | สูง |
| UNa | **< 20–30** | **> 30** | < 20 (ถ้าไม่ได้ยาขับปัสสาวะ) |
| ตอบสนองต่อ 0.9% NaCl | Na ขึ้น | มักไม่ขึ้น/ต่ำลง | บวมมากขึ้น |

#### ทำไมถึงมีอาการนี้
- **SIADH ไม่บวม** — น้ำที่เก็บไว้ 2/3 กระจายเข้าเซลล์ และ ECF ที่เกินเล็กน้อยกระตุ้น natriuresis (ANP ↑ RAAS ↓ GFR ↑) จนปริมาตรกลับใกล้ปกติ
- **SIADH ปัสสาวะมี Na สูง** — ไตไม่ได้ "รั่ว" Na แต่กำลังทำหน้าที่ปกติคือขับ Na ที่เกินออกเพื่อรักษาปริมาตร
- **SIADH ให้ NSS แล้ว Na ต่ำลง** — NSS มี osmole 308 mOsm ถ้าปัสสาวะเข้มข้น ~600 Na ทั้งหมดถูกขับออกในปัสสาวะเพียงครึ่งลิตร อีกครึ่งลิตรเป็นน้ำเปล่าที่ถูกเก็บไว้
- **ปวดหัว อาเจียน ชัก ใน Na ที่ตกเร็ว** — น้ำเข้าเซลล์สมองในกะโหลกที่ขยายไม่ได้ → ความดันในกะโหลกสูง

### สมองปรับตัว และทำไมแก้เร็วเกินไปจึงอันตราย
[[fig:ods]]
- ภายใน ~48 ชม. เซลล์สมองขับ K Cl และ **organic osmolyte** ออกเพื่อหดกลับ → hyponatremia เรื้อรังจึงอาการน้อย
- การสร้าง osmolyte กลับใช้เวลาหลายวัน → ถ้า Na ขึ้นเร็ว เซลล์ที่ "ปรับลด" แล้วจะเสียน้ำ → **osmotic demyelination syndrome** (central pontine myelinolysis) — พูดไม่ชัด กลืนลำบาก อ่อนแรงทั้งตัว locked-in · มักเกิด 2–6 วันหลังแก้
- **ขีดจำกัด (European 2014)**: เพิ่ม Na **≤ 10 mmol/L ใน 24 ชม.แรก** และ **≤ 8 mmol/L ในแต่ละ 24 ชม.ถัดไป** · กลุ่มเสี่ยงสูง (สุรา ขาดอาหาร K ต่ำ ตับแข็ง Na ≤ 105) แนวทางสหรัฐ 2013 แนะนำเป้า 4–8 และไม่เกิน 8
- อาการรุนแรง (ชัก ซึมมาก): **3% NaCl 150 mL ใน 20 นาที** ซ้ำได้ จนเพิ่ม ~5 mmol/L — แค่นี้พอลดสมองบวม
- ระวัง **แก้เกินเอง**: เมื่อสาเหตุของ ADH หายไป (ให้สารน้ำในผู้ที่ขาดน้ำ หยุด thiazide แก้ cortisol) ADH จะดับทันที → ปัสสาวะจางออกมาก (water diuresis) → Na พุ่ง
""",
    ["Hyponatremia = น้ำเกินเทียบกับ Na + ไตขับน้ำไม่ได้ (ADH ทำงาน)",
     "SIADH: euvolemic · Uosm > 100 · UNa > 30 · RAAS ต่ำ — UNa สูงเพราะไตรักษาปริมาตร",
     "ปริมาตรลด → UNa < 20–30 และ Na ขึ้นเมื่อได้ NSS",
     "European 2014: เพิ่ม Na ≤ 10 ใน 24 ชม.แรก · ≤ 8 ต่อ 24 ชม.ถัดไป",
     "Water diuresis หลังแก้สาเหตุ = เสี่ยงแก้เร็วเกิน (ODS)"],
    [mcq(N(13), "A 70-year-old woman with pneumonia has serum Na 124 mEq/L, plasma osmolality 258 mOsm/kg, urine osmolality 480 mOsm/kg, and urine Na 52 mEq/L. She is clinically euvolemic and not taking diuretics; TSH and cortisol are normal. Why is her urine Na high?",
         ["Water retention mildly expands the ECF, suppressing renin–aldosterone and increasing ANP and GFR, so the kidney excretes Na",
          "ADH directly blocks ENaC in principal cells, causing renal Na wasting",
          "Aldosterone excess from pneumonia causes inappropriate natriuresis",
          "Cerebral release of brain natriuretic peptide causes primary salt wasting with hypovolemia",
          "Hyponatremia inhibits proximal NHE3, preventing Na reabsorption"], 0,
         "นี่คือ **SIADH** (hypotonic · Uosm > 100 · euvolemic · UNa > 30 · ตัด thyroid/adrenal แล้ว) · ADH ทำให้เก็บน้ำ → ECF ขยายเล็กน้อย → ตัวรับปริมาตรตอบสนองตามปกติ: **↓ renin/aldosterone ↑ ANP ↑ GFR → ขับ Na** เพื่อรักษาปริมาตร → UNa สูง (กลไกเติมจากตำรา เชื่อมกับสไลด์ ANP/RAAS)\n\n"
         "- **ADH บล็อก ENaC** — ผิด ADH ไม่ได้ทำให้เสีย Na โดยตรง\n- **aldosterone สูง** — ใน SIADH aldosterone **ต่ำ** และ aldosterone ทำให้เก็บ Na ไม่ใช่ขับ\n"
         "- **cerebral salt wasting** — ผู้ป่วยต้องมี hypovolemia และโรคสมอง ผู้ป่วยรายนี้ euvolemic\n- **Na ต่ำยับยั้ง NHE3** — ไม่มีกลไกนี้",
         "SIADH: UNa สูงเพราะไตตอบสนองต่อปริมาตรที่เกินเล็กน้อย", "SIADH physiology", R("Types of volume excess", "European hyponatraemia guideline 2014"), [SIADH, SIADH_B, LYTE]),
     mcq(N(14), "A 48-year-old man with alcohol use disorder and poor intake is admitted with serum Na 112 mEq/L and K 2.9 mEq/L; he is mildly confused but has no seizures. He receives 0.9% saline and KCl, and 24 hours later his Na is 128 mEq/L. Three days later he develops dysarthria, dysphagia and quadriparesis. Which mechanism best explains this complication?",
         ["The rapid rise in ECF tonicity drew water out of brain cells that had lost organic osmolytes during adaptation, injuring oligodendrocytes",
          "Excess saline caused cerebral edema because water moved into brain cells",
          "Hypokalemia directly caused demyelination of peripheral nerves",
          "Thiamine deficiency caused hemorrhagic lesions in the mammillary bodies",
          "Hyponatremia that persisted for 3 days caused delayed cerebral edema"], 0,
         "Na เพิ่ม **16 mmol/L ใน 24 ชม.** (เกินขีด 10 ของ European 2014 และเกิน 8 ที่แนะนำในกลุ่มเสี่ยงสูง — สุรา K ต่ำ ขาดอาหาร) · สมองที่ปรับตัวต่อ hyponatremia เรื้อรังได้ขับ osmolyte ออกไปแล้ว เมื่อ ECF เข้มขึ้นเร็ว **น้ำจึงออกจากเซลล์** → oligodendrocyte ใน pons บาดเจ็บ → **osmotic demyelination syndrome** (อาการช้า 2–6 วัน: dysarthria dysphagia quadriparesis) · K ต่ำเพิ่มความเสี่ยงเพราะการให้ K ก็ทำให้ Na สูงขึ้นด้วย (K เข้าเซลล์แลก Na ออก)\n\n"
         "- **cerebral edema จาก saline** — ทิศตรงข้าม การแก้ Na ทำให้เซลล์ **เหี่ยว**\n- **K ต่ำทำลาย myelin ส่วนปลาย** — ไม่ใช่กลไก และอาการเป็นของก้านสมอง\n"
         "- **thiamine (Wernicke)** — สับสน ตากระตุก ataxia ไม่ใช่ quadriparesis + dysphagia หลังแก้ Na\n- **hyponatremia ค้าง** — Na ถูกแก้ไปแล้ว",
         "Na ขึ้นเร็วใน hyponatremia เรื้อรัง → น้ำออกจากเซลล์สมอง → ODS", "Osmotic demyelination", R("Water shift between compartment", "European hyponatraemia guideline 2014", "Verbalis Am J Med 2013"), [LYTE, LYTE_B, CONF, WEAK])],
    [LYTE, LYTE_B, SIADH, SIADH_B, CONF, SEIZ], {"siadh": F.siadh(), "ods": F.ods()}, source=SRC_ADD)

# ── END SECTIONS


# ═════════════════════════════════════════════ ประกอบคาบ
LECNAME = "สรีรวิทยาไตพื้นฐาน II (Watchara Chongsa, PhD)"
MEQ = []
OSCE = []
LECTURE = {
 "lec": LEC, "date": "พื้นฐานสรีรวิทยา (ปรีคลินิก)",
 "title": "สรีรวิทยาไตพื้นฐาน II — สมดุลน้ำ อิเล็กโทรไลต์ กรด-ด่าง และการถ่ายปัสสาวะ",
 "subtitle": "Darrow–Yannet · glomerulotubular balance · RAAS/ADH/ANP · K shift และการขับ K · Ca Pi Mg · buffer ปอด ไต · HCO3 reclamation, TA, NH4 · การชดเชย · anion gap · micturition reflex — พร้อมสะพานสู่คลินิก (SIADH, ODS, DKA, อาเจียน, RTA, incontinence)",
 "objectives": [],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ทำก่อน publish ครั้งแรกเท่านั้น) — ข้อที่ตัวเลือกเรียงตามตัวเลขไม่สลับ
ORDERED = {N(12), N(21), N(24)}
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED or not it["id"].startswith("NEPH-PHY2-MCQ"):
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "nephro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
pos = next((i + 1 for i, l in enumerate(data) if l.get("lec") == "Physio1"), 0)
data.insert(pos, LECTURE)

seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
L = LECTURE
codes = {c for s in L["sections"] for c in s["nl"]} | {c for s in L["sections"] for i in s["items"] for c in i["nl"]} | {c for m in L["meq"] + L["osce"] for c in m.get("nl", [])}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in L["sections"]:
    assert "```" not in s["md"], s["id"]
    for k in (s.get("figs") or {}):
        assert "[[fig:%s]]" % k in s["md"], (s["id"], k)

json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "nephro": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ผูกข้อ Mock exam (ไม่ผูกคาบ) ที่ตรงเรื่อง
from link_mock import link_mock
MOCK_MAP = {}
nmock = link_mock(SET, LEC, MOCK_MAP) if MOCK_MAP else 0

from collections import Counter
newi = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-PHY2")]
print("sections %d | ข้อใหม่ %d | mock %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), len(newi), nmock, len(L["meq"]), len(L["osce"]), sum(len(s.get("figs") or {}) for s in S), len(codes)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for i in newi).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
