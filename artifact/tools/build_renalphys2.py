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
- **ภาวะปกติ**: autoregulation ตรึง GFR ไว้เมื่อ MAP อยู่ราว **80–170 mmHg** → filtered load ของ Na และน้ำแทบไม่เปลี่ยน (กลไก myogenic/TGF, Starling ที่ glomerulus และ clearance/FENa สอนละเอียดในคาบ **Physio1**)
- **เมื่อร่างกายขาดน้ำมาก**: sympathetic + Ang II → renal arteriole หดตัว → RBF ↓ → GFR ↓ → filtered load ↓

### 2) ทางการดูดกลับ — ตัวคุมหลัก
| ดูด Na กลับ | ดูดน้ำกลับ |
|---|---|
| glomerulotubular balance | glomerulotubular balance |
| sympathetic: ↑ ดูด Na ที่ PT, TAL, DT, CD | gradient ใน medulla (countercurrent และ CH2O ดูคาบ Physio1) |
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
- ผลรวม **↑ ขับ NaCl และน้ำ** (✍️ ลายมือ: ANP เป็นตัวเดียวที่ตอบสนองต่อภาวะน้ำเกิน)

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
**กระเพาะที่ยืดจากการดื่ม ยับยั้งความกระหายก่อนที่น้ำจะถูกดูดซึม** (สไลด์ Thirst center) — ป้องกันการดื่มเกิน

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
↓ Posm → **ADH ถูกกด** + ไม่กระหาย · ↑ ANP · ↓ sympathetic → ↓ renin/Ang II/aldo · ↑ GFR · ↓ FF → **water diuresis**: ปัสสาวะมาก จาง **Uosm/Posm < 1** CH2O เป็นบวก · สไลด์: osmolar clearance เพิ่มเล็กน้อย (ขับ Na เพิ่มนิดหน่อย)
### Hyperosmotic volume expansion — กินเค็ม (สไลด์ Salty diet)
↑ Posm → ↑ ADH + ดื่มน้ำ → Posm กลับปกติ **อย่างรวดเร็ว** · แต่ BV ที่เพิ่ม → ↑ ANP ↓ RAAS ↓ sympathetic → **ขับ NaCl และน้ำ (ช้า)** จนปริมาตรกลับ — หลังกินเค็มจึงคอแห้งก่อน แล้วค่อยปัสสาวะมาก
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

# ═════════════════════════════════════════════ 8
sec("nephro-phy2-08", "Potassium I — K กำหนด RMP · ผลต่อกล้ามเนื้อและหัวใจ · การย้าย K เข้า-ออกเซลล์",
    "98% ของ K อยู่ในเซลล์ · K สูง/ต่ำทำให้อ่อนแรงต่างกลไก · ECG · insulin β2 aldosterone acid-base และ osmolality", 9,
"""### ทำไม K สำคัญ (สไลด์ Potassium)
[K]ECF และกระแส K ที่รั่วออกทาง **leak K channel** เป็นตัวกำหนด **resting membrane potential (RMP)** ของเซลล์ที่กระตุ้นได้ โดยเฉพาะกล้ามเนื้อลายและหัวใจ · K ในเลือดเปลี่ยน → RMP เปลี่ยน → การทำงานของกล้ามเนื้อและหัวใจเปลี่ยน
- ค่าปกติ **3.5–5.0 mEq/L** · ECF มี K ทั้งหมดเพียง ~65 mmol ขณะที่กล้ามเนื้อมี ~2,600 mmol (✍️ ส่วนใหญ่อยู่ในเซลล์) · กินวันละ ~100 mmol
- กลไกคุม K มี 2 ชั้น: **(1) shift เข้า-ออกเซลล์ (นาที)** **(2) ไตดูดกลับ/ขับ (ชั่วโมง)** — หัวข้อ 9

### กล้ามเนื้อ (สไลด์ Neuromuscular function)
[[fig:k_rmp]]
| | กลไก | อาการ |
|---|---|---|
| **K สูง ระยะแรก** | ↓ K efflux → ประจุบวกค้างในเซลล์ → RMP ดีโพลาไรซ์เข้าใกล้ threshold → ไวขึ้น | กล้ามเนื้อกระตุก ตะคริว |
| **K สูง ระยะหลัง** | ดีโพลาไรซ์ค้าง → **voltage-gated Na channel ถูก inactivate** | อ่อนแรงปวกเปียก |
| **K ต่ำ** | ↑ K efflux → RMP hyperpolarize ห่างจาก threshold | อ่อนแรงปวกเปียก (ตะคริว ileus ด้วย) |

### หัวใจ (สไลด์ Cardiac function · ECG)
| ระดับ K | กลไก | ECG / อาการ |
|---|---|---|
| K สูง: mild 5.5–6.5 · moderate 6.5–8 · severe > 8 | ↑ K channel เปิดใน phase 3 → repolarize เร็ว | **T สูงแหลม** → VT/VF |
| | RMP ดีโพลาไรซ์ → Na channel inactivate → phase 0 ช้า | P กว้างแบน · **PR ยาว · QRS กว้าง · sine wave** → bradycardia, sinus arrest |
| K ต่ำ | ↓ K channel ใน phase 3 → repolarize ช้า | **T แบน · U เด่น · ST depression** · P สูงเล็กน้อย → arrhythmia |
ตัวอย่างในสไลด์: K 7.0 → T สูงแหลมสมมาตร · K 9.0 (rhabdomyolysis) → T ใหญ่มาก sine wave · K 1.7 → ST depression T กลับหัว U เด่น QU ยาว

### Shift — ใครดึง K เข้าเซลล์ (สไลด์ K shift · Table 5.4)
[[fig:k_shift]]
- **aldosterone, insulin, epinephrine (β2)** → ↑ Na/K-ATPase ในกล้ามเนื้อ กระดูก ตับ RBC → K เข้าเซลล์ → **↓ PK** · หลังกินอาหาร insulin ช่วย "เก็บ" K ไว้ในเซลล์ก่อนที่ไตจะขับทัน
- **α-adrenergic** → ↓ Na/K-ATPase → ↑ PK
- **acid-base**: metabolic acidosis → ยับยั้ง Na/K-ATPase + H เข้าเซลล์แลก K ออก → ↑ PK · alkalosis ตรงข้าม
- ⚠️ **สไลด์ย้ำ**: การแลก H/K **ไม่เกิดใน respiratory acid-base disorder หรือ metabolic acidosis จากกรดอินทรีย์** (lactate ketone เข้าเซลล์ไปพร้อม H) — K สูงใน DKA จึงมาจาก **ขาด insulin + Posm สูง** มากกว่า
- ออกนอกเซลล์อื่น ๆ: Posm สูง (น้ำออก K ตาม — solvent drag) · digitalis (ยับยั้ง pump) · ออกกำลังกาย (ATP ↓ → ATP-sensitive K channel เปิด) · เซลล์แตก (hemolysis rhabdomyolysis) · β-blocker

#### ทำไมถึงมีอาการนี้ — และทำไมรักษาแบบนั้น
| สถานการณ์ | กลไก |
|---|---|
| ให้ **Ca gluconate** ทันทีเมื่อ ECG เปลี่ยนใน K สูง | Ca ยก threshold ขึ้น (หัวข้อ 10) → คืนระยะห่าง RMP–threshold ให้ Na channel ใช้งานได้ — ไม่ได้ลด K |
| ให้ **insulin + glucose**, **salbutamol** | ดึง K เข้าเซลล์ภายใน 15–30 นาที (ชั่วคราว) |
| เจาะเลือดรัดแขนนาน/กำมือ หรือเลือด hemolysis | K หลุดจากเซลล์ในหลอด → **pseudohyperkalemia** ECG ปกติ |
| ผู้ป่วยหอบหืดพ่นยาถี่ | β2 → K เข้าเซลล์ → K ต่ำ อ่อนแรง |
> แถวการรักษาเติมจากตำรา (Boron · KDIGO/UK Kidney Association hyperkalaemia guideline) — สไลด์สอนกลไก shift
""",
    ["K อยู่ในเซลล์ ~98% — shift เพียงเล็กน้อยเปลี่ยน K เลือดมาก",
     "K สูง: ไวขึ้นก่อน แล้ว Na channel inactivate → อ่อนแรง · T แหลม → QRS กว้าง → sine wave",
     "K ต่ำ: hyperpolarize → อ่อนแรง · T แบน U เด่น ST กด",
     "Insulin β2 aldosterone ดึง K เข้าเซลล์ · acidosis จากกรดแร่ดัน K ออก (กรดอินทรีย์ไม่ค่อย)",
     "Ca gluconate ใน K สูง = ป้องกันหัวใจ ไม่ได้ลด K"],
    [mcq(N(15), "A 62-year-old man on hemodialysis misses two sessions. Serum K is 7.8 mEq/L and the ECG shows peaked T waves, a prolonged PR interval and a widened QRS complex. Which mechanism best explains the widened QRS?",
         ["Sustained depolarization of the resting membrane potential inactivates voltage-gated Na channels, slowing phase 0 and conduction",
          "Increased K efflux during phase 3 shortens repolarization and widens the QRS",
          "Hyperpolarization of the resting membrane potential moves it away from threshold",
          "Increased Ca influx during phase 2 prolongs ventricular depolarization",
          "Hyperkalemia blocks the Na/K-ATPase, increasing intracellular Na and conduction velocity"], 0,
         "K สูงมาก → RMP ดีโพลาไรซ์ค้าง → **Na channel ถูก inactivate** → phase 0 ขึ้นช้าและเล็ก → นำไฟฟ้าช้า → **PR ยาว QRS กว้าง** จนเป็น sine wave (สไลด์ Cardiac function)\n\n"
         "- **K efflux ใน phase 3 เพิ่ม** → อธิบาย **T สูงแหลม** ไม่ใช่ QRS กว้าง\n- **hyperpolarization** = K ต่ำ\n"
         "- **Ca influx phase 2** = กลไกของ QT ที่เปลี่ยนใน Ca ผิดปกติ\n- **ยับยั้ง Na/K-ATPase แล้วนำไฟฟ้าเร็วขึ้น** — ผิดทั้งสองส่วน",
         "QRS กว้างใน K สูง = Na channel inactivation", "Hyperkalemia ECG mechanism", R("Cardiac function"), [HYPERK, ECG, ECG_B, HANDLE_B]),
     mcq(N(16), "A 24-year-old woman with severe asthma receives continuous nebulized salbutamol for 6 hours. Her serum K falls from 4.1 to 2.9 mEq/L; urine K excretion is low. What is the mechanism?",
         ["β2-adrenergic stimulation increases Na/K-ATPase activity in skeletal muscle, shifting K into cells",
          "β2 stimulation increases K secretion by principal cells",
          "Respiratory alkalosis from hyperventilation drives K into cells via H/K exchange",
          "Salbutamol stimulates aldosterone secretion from the adrenal cortex",
          "Salbutamol blocks ATP-sensitive K channels, trapping K in muscle"], 0,
         "β2-agonist → cAMP → **Na/K-ATPase ในกล้ามเนื้อทำงานเพิ่ม** → K ย้ายเข้าเซลล์ (shift) · UK ต่ำยืนยันว่าไม่ได้เสียทางไต (สไลด์ K shift: epinephrine β2 · Table 5.4 salbutamol)\n\n"
         "- **ขับทางไต** — UK ต่ำ ขัดกัน\n- **respiratory alkalosis + H/K exchange** — สไลด์ย้ำว่าการแลก H/K **ไม่เกิดใน respiratory disorder** (และผลน้อย)\n"
         "- **aldosterone** — ไม่ใช่ผลของ β2 และจะทำให้ UK สูง\n- **บล็อก KATP** — ไม่ใช่กลไกของ salbutamol",
         "β2-agonist → K เข้าเซลล์ (ใช้รักษา K สูงได้)", "K shift by β2 agonist", R("K shift into/out cell · Table 5.4"), [HANDLE_B, LYTE, WEAK])],
    [HANDLE_B, HYPERK, LYTE, LYTE_B, WEAK, ECG], {"k_rmp": F.k_rmp(), "k_shift": F.k_shift()})

# ═════════════════════════════════════════════ 9
sec("nephro-phy2-09", "Potassium II — ไตขับ K ที่ principal cell และ 6 ปัจจัยที่ทำให้ขับมากขึ้น",
    "PT 65% · TAL 25% · ส่วนปลายดูดหรือขับตามความต้องการ · aldosterone · flow/Na · anion · Mg · alkalosis · ยาขับปัสสาวะ", 9,
"""### K ถูกจัดการตลอด nephron (สไลด์ Renal K regulation)
| ส่วน | การจัดการ |
|---|---|
| PT | ดูดกลับ ~65% ตาม Na และน้ำ |
| TAL | ดูดกลับ ~25% ตาม Na (NKCC2) |
| DT และ CD | **ดูดกลับหรือขับ ตามระดับ K ในเลือด** ผ่าน **P cell (ขับ)** และ **type A-IC (ดูดกลับด้วย H/K-ATPase)** |
- **กิน K ปกติ/มาก**: DT ขับ 8–50% · CCD ขับ 5–30% → ขับทิ้ง **15–80%** ของที่กรอง
- **กิน K น้อย**: DT ดูดกลับ 2% · CCD ดูดกลับ 7% → ขับทิ้งเพียง **~1%**
→ ไตคุม K ที่ "ส่วนปลาย" เป็นหลัก ส่วนต้นทำงานเกือบคงที่

### Principal cell และปัจจัยที่เพิ่มการขับ K (สไลด์ Factors affecting tubular K secretion)
[[fig:pcell]]
| ปัจจัย | กลไก | ตัวอย่างคลินิก |
|---|---|---|
| 1 **K ในเลือดสูง** | Na/K-ATPase ดึง K เข้าเซลล์มาก → gradient ออกสู่ lumen สูง · กระตุ้น aldosterone | กินอาหาร K สูง rhabdomyolysis |
| 2 **Mg ในเลือดต่ำ** | Mg ในเซลล์อุด ROMK จากด้านใน — Mg ต่ำ ROMK เปิดตลอด | K ต่ำที่ "แก้ไม่ขึ้น" |
| 3 **aldosterone สูง** | ↑ ENaC ROMK และ pump | JG cell tumor, adrenal tumor (Conn) |
| 4 **Na/flow ส่วนปลายสูง** (ตำแหน่งออกฤทธิ์ของยาขับปัสสาวะ/Bartter/Gitelman/Liddle ดู Physio1) | Na มาก → ENaC ดูดมาก lumen ลบ · flow มาก → ดัด primary cilia → Ca เข้า → **BK channel** เปิด + K ในท่อถูกพาไปไม่สะสม | **loop/thiazide** อาหารเค็ม volume expansion |
| 5 **anion ในท่อที่ดูดกลับไม่ได้** | HCO3 SO4 หรือยา (penicillin) ทำให้ lumen ลบยิ่งขึ้น | CA inhibitor · **อาเจียน** (HCO3 กรองเกินกำลังดูด) |
| 6 **metabolic alkalosis (เฉียบพลัน)** | P cell: ↑ pump ↑ K channel เปิด · B-IC: ↑ H/K-ATPase แลก | ✍️ alkalosis เฉียบพลัน → ขับ K มาก → K ต่ำ · acidosis เฉียบพลัน → ขับ K น้อย → K สูง |

**Table 5.5 (สไลด์)** — เพิ่มการขับ: อาหาร K สูง · hyperaldosteronism · alkalosis · thiazide · loop · luminal anion | ลดการขับ: อาหาร K ต่ำ · hypoaldosteronism · acidosis · **K-sparing diuretic** (✍️ ออกฤทธิ์ที่ late DT/CD ซึ่งเป็นจุดขับ K พอดี จึงไม่เสีย K)
> สไลด์ Acute vs chronic metabolic acidosis (Berne & Levy fig 36.10): acidosis **เรื้อรัง** กลับเพิ่มการขับ K ได้ เพราะ PT ดูดน้ำและ NaCl น้อยลง → flow ส่วนปลายเพิ่ม + ปริมาตรลด → aldosterone ↑ (✍️ อาจารย์บอกว่าไม่ออกสอบ)

#### ทำไมถึงมีอาการนี้
| ภาวะ | ห่วงโซ่เหตุ→ผล |
|---|---|
| **K ต่ำจาก furosemide/thiazide** | บล็อก NKCC2/NCC → Na และน้ำล้นไปส่วนปลาย (ปัจจัย 4) + ปริมาตรลด → aldosterone (ปัจจัย 3) + contraction alkalosis (ปัจจัย 6) |
| **K ต่ำแก้ไม่ขึ้นเพราะ Mg ต่ำ** | ให้ KCl แต่ ROMK ไม่ถูก Mg อุด K รั่วทิ้งทางไต → ต้องให้ Mg ก่อน/พร้อมกัน |
| **K ต่ำหลังอาเจียน** | K ในน้ำย่อยมีน้อย — ที่หายส่วนใหญ่คือ **ทางไต**: HCO3 ในท่อ (anion) + aldosterone + alkalosis (หัวข้อ 13) |
| **K สูงจาก ACEi + spironolactone ใน CKD** | ตัด aldosterone สองชั้น + nephron เหลือน้อย flow ส่วนปลายต่ำ |
| **K สูงใน type 4 RTA** | hypoaldosteronism → ขับ K ไม่ได้ · K สูงยังกด ammoniagenesis → acidosis (หัวข้อ 12) |
""",
    ["ส่วนปลาย (P cell) คือจุดคุมการขับ K · PT/TAL ดูดกลับคงที่ ~90%",
     "6 ปัจจัยเพิ่มการขับ: K สูง · Mg ต่ำ · aldosterone · Na/flow ส่วนปลาย · luminal anion · alkalosis",
     "Loop/thiazide → K ต่ำ · K-sparing ทำงานที่จุดขับ K จึงไม่เสีย K",
     "Mg ต่ำ → ROMK ไม่ถูกอุด → K ต่ำแก้ไม่ขึ้น",
     "Acidosis เฉียบพลันลดการขับ K · alkalosis เฉียบพลันเพิ่ม"],
    [mcq(N(17), "A 70-year-old woman with heart failure starts furosemide 80 mg/day. Two weeks later her K is 2.9 mEq/L and HCO3 is 31 mEq/L. Which mechanism contributes most directly to her hypokalemia?",
         ["Increased Na delivery and flow to the principal cells, plus volume-contraction–induced aldosterone, enhance K secretion",
          "Furosemide directly inhibits ROMK in the collecting duct, trapping K inside cells",
          "Furosemide stimulates H/K-ATPase in type A intercalated cells, increasing K reabsorption",
          "Furosemide causes K to shift into skeletal muscle via β2 receptors",
          "Furosemide blocks K secretion in the proximal tubule"], 0,
         "furosemide บล็อก NKCC2 ที่ TAL → Na และน้ำล้นไปส่วนปลาย → **ENaC ดูด Na มาก (lumen ลบ) + flow สูงเปิด BK และพา K ในท่อออกไป** · ปริมาตรลด → **aldosterone** · HCO3 31 = contraction alkalosis ซึ่งเพิ่มการขับ K อีก (สไลด์ factors 3, 4, 6 · Table 5.5)\n\n"
         "- **บล็อก ROMK ที่ CD** — ผิด ถ้าบล็อก ROMK จะขับ K น้อยลง\n- **H/K-ATPase ดูด K กลับ** — จะทำให้ K สูงขึ้นไม่ใช่ต่ำ\n"
         "- **shift ผ่าน β2** — furosemide ไม่มีฤทธิ์นี้\n- **PT ขับ K** — PT ดูด K กลับ ไม่ได้ขับ",
         "Loop/thiazide → Na/flow ส่วนปลาย + aldosterone → K ต่ำ", "Diuretic-induced hypokalemia", R("Factors affecting tubular K secretion · Table 5.5"), [HANDLE_B, DIUR_B, LYTE]),
     mcq(N(18), "A 55-year-old man with chronic alcohol use has K 2.6 mEq/L and Mg 1.0 mg/dL. Despite 120 mEq of IV KCl over 24 hours, his K remains 2.8 mEq/L with ongoing urinary K loss. What is the best explanation?",
         ["Low intracellular Mg removes the normal block of ROMK channels, so principal cells keep secreting K until Mg is replaced",
          "Hypomagnesemia increases insulin secretion, shifting all infused K into cells",
          "Hypomagnesemia inhibits aldosterone, causing K wasting",
          "Magnesium competes with K for reabsorption in the proximal tubule",
          "Hypomagnesemia causes metabolic acidosis, which increases distal K secretion acutely"], 0,
         "Mg ในเซลล์อุด **ROMK** จากด้านใน · Mg ต่ำ → ROMK เปิดตลอด → K ถูกขับทิ้งทางไตไม่หยุด แม้ให้ K มาก → **ต้องแก้ Mg ก่อนหรือพร้อม K** (สไลด์ factor 2: ↓ plasma Mg2+)\n\n"
         "- **insulin ดึง K เข้าเซลล์** — ไม่ใช่ผลของ Mg ต่ำ และไม่อธิบาย UK สูง\n- **Mg ต่ำยับยั้ง aldosterone** — ถ้า aldosterone ต่ำจะเสีย K **น้อยลง**\n"
         "- **แย่งดูดที่ PT** — ไม่มีกลไกนี้\n- **acidosis เฉียบพลันเพิ่มการขับ K** — ตรงข้าม acidosis เฉียบพลันลดการขับ K",
         "K ต่ำ + Mg ต่ำ → ให้ Mg ด้วย", "Hypomagnesemia and refractory hypokalemia", R("Factors affecting tubular K secretion"), [HANDLE_B, LYTE, LYTE_B])],
    [HANDLE_B, TUB_B, DIUR_B, CONN_B, HYPERK, LYTE], {"pcell": F.pcell()})

# ═════════════════════════════════════════════ 10
sec("nephro-phy2-10", "Ca, Pi และ Mg — รูปแบบในพลาสมา ความไวของเส้นประสาท และการจัดการของไต",
    "Ionized Ca กำหนด threshold · albumin/pH/phosphate เปลี่ยน ionized Ca · Chvostek/Trousseau · QT · PTH calcitriol FGF-23 · segment ที่ดูดกลับ", 9,
"""> หัวข้อนี้คือ **ฐานสรีรวิทยา** — สาเหตุ อาการ การวินิจฉัยและการรักษา Ca P Mg ผิดปกติอยู่ใน **คาบ 05 Fluid electrolyte: Divalent** (อ.ใน รพ.ราชวิถี)

### Calcium (สไลด์ Calcium)
- ร่างกายมี Ca ~1,300 g — **99% ในกระดูกและฟัน** · 1% ในเซลล์ · **0.1% ใน ECF** · ค่าปกติ total **9–10 mg/dL** (< 8.5 ต่ำ · > 10.5 สูง)
- ในพลาสมา: **ionized 50% (ตัวที่ออกฤทธิ์)** · complexed กับ Pi HCO3 citrate SO4 10% · จับโปรตีน 40% (albumin ~90%)
| สิ่งที่เปลี่ยน | กลไก | ionized Ca |
|---|---|---|
| **phosphate สูง** | Ca จับ phosphate เป็น complex มากขึ้น | ↓ |
| **albumin ต่ำ** (ตับแข็ง nephrotic) | Ca จับ albumin น้อยลง → total Ca ลด แต่สัดส่วน ionized สูงขึ้น | ionized มักปกติ — **total หลอกว่าต่ำ** |
| **acidemia** | H แย่งที่บน albumin/anion → Ca หลุดออก | ↑ |
| **alkalemia** (หายใจเร็ว) | albumin ปล่อย H → จับ Ca มากขึ้น | ↓ → ชา เกร็ง |

### ทำไม Ca ต่ำจึงชาและเกร็ง (สไลด์ Neuromuscular function)
[[fig:ca_thr]]
ionized Ca นอกเซลล์คุมการเปิดของ **voltage-gated Na channel** (ปกติเปิดที่ ~−55 mV) — Ca ต่ำ → threshold ต่ำลง → เส้นประสาทยิงง่าย
- sensory: ชาปลายนิ้ว รอบปาก reflex ไว · motor: ตะคริว **tetany carpopedal spasm** (พบบ่อยหลังผ่าตัดต่อมไทรอยด์)
- **Chvostek's sign**: เคาะหน้าติ่งหู 2 ซม. ใต้ zygoma 0.5–1 ซม. → กล้ามเนื้อหน้าข้างเดียวกันกระตุก (grade 1 มุมปาก → 4 ครึ่งหน้า) — พบเพียง ~25% ของ Ca ต่ำ
- **Trousseau's sign**: พันผ้ารัดแขนสูงกว่า SBP 20 mmHg นาน 3 นาที → มือจีบ (ข้อมืองอ MCP งอ IP เหยียด นิ้วโป้งหุบ) — ไวกว่า (94%)
- **Ca สูง** → threshold สูง → อ่อนแรง
- หัวใจ: Ca เข้าเซลล์ใน phase 2 · **Ca ต่ำ → ST และ QT ยาว** (ตัวอย่างสไลด์ QT 0.44 s หลังตัดไทรอยด์) · **Ca สูง → ST/QT สั้น** (Ca 12.2 mg/dL QT 0.28 s)
- สไลด์ Mg: **Mg ต่ำ** ก็ทำให้ tetany และ Chvostek/Trousseau บวกได้

### ฮอร์โมนที่คุม Ca และ Pi (สไลด์ Plasma Ca2+ regulation · Phosphate)
| ฮอร์โมน | Ca เลือด | Pi เลือด | ทำที่ |
|---|---|---|---|
| **PTH** (Ca ต่ำ → CaSR) | ↑ | ↓ | กระดูก (resorption) · ไต ↑ ดูด Ca ที่ DT · ↓ ดูด Pi ที่ PT · ↑ 1α-hydroxylase |
| **1,25(OH)2D3** | ↑ | ↑ | ลำไส้ดูด Ca และ Pi · กระดูก |
| **FGF-23** (osteocyte/osteoblast · Pi สูง) | — | ↓ | ดึง NaPi-IIa ออกจาก PT · **กด 1α-hydroxylase** |
| **Calcitonin** (parafollicular cell) | ↓ | — | ไม่มีบทบาททุกนาทีในคน อาจลด bone resorption เมื่อ Ca สูงมาก |
Ca balance ต่อวัน (สไลด์): กิน 1,000 mg · ดูดซึมสุทธิ ~100 mg = ขับทางปัสสาวะ ~100 mg · กรอง 9,980 ดูดกลับ 9,880 mg

### ไตดูดกลับที่ไหน
[[fig:div_segments]]
| | PT | TAL | DT | ปัจจัยเพิ่มการดูดกลับ / ลด |
|---|---|---|---|---|
| **Ca** | 65% (ตาม Na น้ำ) | 25% | **8% (PTH, calcitriol)** · CCD 1% | ↑: PTH calcitriol **thiazide** phosphate/albumin สูง volume contraction alkalemia |
| **Pi** | **80% NaPi-IIa/IIc** | — | 10% | ↓ ดูด: PTH FGF-23 Pi สูง Ca ต่ำ volume expansion **metabolic acidosis** (Pi เป็น buffer ในปัสสาวะ) |
| **Mg** | 30% | **60% paracellular** | 5% (TRPM6) | ↑: PTH EGF volume contraction alkalosis · ↓: furosemide thiazide |
- Pi: body 600 g (85% กระดูก 14% ในเซลล์ — ATP DNA 2,3-DPG) · ในพลาสมา ionized 45% (HPO4:H2PO4 = 80:20) · ค่าปกติ 3–4 mg/dL (< 2.5 ต่ำ > 4.5 สูง) · **Pi ~10% ที่หลุดไปปัสสาวะคือ titratable acid** (หัวข้อ 12)
- Mg: body 25 g (54% กระดูก 45% ในเซลล์) · ในพลาสมา ionized 60% · ค่าปกติ 1.5–2.3 mg/dL · ลดความไวของประสาท ยับยั้งการหลั่ง ACh NE catecholamine

#### ทำไมถึงมีอาการนี้
- **thiazide ใช้ป้องกันนิ่ว Ca** — บล็อก NCC → Na ในเซลล์ DT ต่ำ → basolateral Na/Ca exchanger ขน Ca ออกได้มาก → ดูด Ca กลับเพิ่ม (+ ปริมาตรลด → PT ดูดตาม) · ตรงข้ามกับ **loop** ที่ทำลาย lumen-positive voltage ใน TAL → ขับ Ca และ Mg ทิ้ง
- **หายใจหอบตื่นเต้นแล้วมือจีบ** — respiratory alkalosis → ionized Ca ลดทั้งที่ total Ca ปกติ
- **CKD: Pi สูง Ca ต่ำ** — GFR ลด ขับ Pi ไม่ได้ → Pi จับ Ca + FGF-23 สูงกด calcitriol → PTH สูง (secondary hyperparathyroidism)
> กลไก thiazide และ CKD เติมจาก Boron — สไลด์ระบุเพียง "thiazide ↑ Ca reabsorption"
""",
    ["Ionized Ca 50% เป็นตัวออกฤทธิ์ · alkalemia และ phosphate สูงลด ionized Ca",
     "Ca ต่ำ → threshold ของ Na channel ต่ำ → ชา tetany · Trousseau ไว 94% Chvostek ~25%",
     "Ca ต่ำ QT ยาว · Ca สูง QT สั้น",
     "DT คือจุดที่ PTH/calcitriol/thiazide เพิ่มดูด Ca · PTH และ FGF-23 ลดดูด Pi ที่ PT",
     "Mg ดูดมากสุดที่ TAL (60% paracellular) → loop diuretic ทำ Mg ต่ำ"],
    [mcq(N(19), "A 22-year-old woman becomes anxious during an examination and breathes rapidly. She develops perioral numbness and carpopedal spasm. Total Ca 9.4 mg/dL, albumin 4.2 g/dL. ABG: pH 7.56, PaCO2 24 mmHg, HCO3 21 mEq/L. What explains her tetany?",
         ["Alkalemia causes albumin to release H+ and bind more Ca, lowering ionized Ca and the threshold for nerve firing",
          "Hypocapnia directly depolarizes the resting membrane potential of motor neurons",
          "Alkalemia shifts K into cells, causing hyperpolarization and spasm",
          "Hyperventilation increases PTH secretion, lowering total Ca",
          "Low total Ca from hypoalbuminemia reduces nerve excitability"], 0,
         "respiratory alkalosis (pH 7.56 PaCO2 24) → albumin ปล่อย H+ → ตำแหน่งว่างจับ Ca → **ionized Ca ลด** ทั้งที่ total ปกติ → threshold ของ voltage-gated Na channel ลด → เส้นประสาทไวเกิน → ชาและเกร็ง (สไลด์ Calcium: H+ กับ albumin) · HCO3 21 เข้ากับ acute respiratory alkalosis (คาด 24 − 2×1.6 ≈ 20.8)\n\n"
         "- **CO2 ต่ำดีโพลาไรซ์ RMP โดยตรง** — ไม่ใช่กลไกหลัก\n- **K เข้าเซลล์ → hyperpolarization** — จะทำให้อ่อนแรง ไม่ใช่เกร็ง (และ H/K exchange ไม่เกิดใน respiratory disorder)\n"
         "- **PTH เพิ่มแล้ว Ca ลด** — PTH เพิ่ม Ca\n- **albumin ต่ำ** — albumin ปกติ และ Ca ต่ำทำให้ไว **เพิ่ม** ไม่ใช่ลด",
         "หายใจเร็ว → alkalemia → ionized Ca ↓ → tetany", "Ionized Ca and pH", R("Calcium · Neuromuscular function"), [CAPTH_B, HANDLE_B, HYPERVENT, LYTE]),
     mcq(N(20), "A 45-year-old man has recurrent calcium oxalate stones with 24-hour urine Ca of 380 mg. Which drug lowers urinary Ca, and by what mechanism?",
         ["Hydrochlorothiazide, by blocking NaCl entry in the distal convoluted tubule, which enhances Ca reabsorption there (plus proximal reabsorption from mild volume contraction)",
          "Furosemide, by blocking NKCC2 and increasing paracellular Ca reabsorption in the thick ascending limb",
          "Acetazolamide, by inhibiting carbonic anhydrase and increasing Ca reabsorption in the proximal tubule",
          "Mannitol, by raising tubular osmolality and trapping Ca in the lumen",
          "Spironolactone, by blocking ENaC in the collecting duct where most Ca is reabsorbed"], 0,
         "**thiazide** บล็อก NCC ที่ DT → Na ในเซลล์ต่ำ → Na/Ca exchanger ด้าน basolateral ขน Ca ออกได้มาก → **ดูด Ca กลับเพิ่ม** + ปริมาตรลดเล็กน้อยทำให้ PT ดูดตาม Na → urine Ca ลด (สไลด์: thiazide ↑ Ca reabsorption · DT 8% เป็นจุดปรับละเอียด)\n\n"
         "- **furosemide** — ทำลาย lumen-positive voltage ใน TAL → **ลด** การดูด Ca (เพิ่ม urine Ca ใช้แก้ Ca สูง)\n- **acetazolamide** — ทำให้ปัสสาวะด่าง citrate ต่ำ **เพิ่มนิ่ว** Ca phosphate\n"
         "- **mannitol** — ไม่ใช่ยาลด urine Ca\n- **spironolactone** — CD ดูด Ca เพียง ~1% และ spironolactone ไม่ได้บล็อก ENaC (บล็อก MR)",
         "Thiazide ลด urine Ca · loop เพิ่ม urine Ca", "Diuretics and renal Ca handling", R("Renal Ca2+ reabsorption", BB), [HANDLE_B, DIUR_B, CAPTH_B])],
    [HANDLE_B, CAPTH_B, ELYTE_B, LYTE, DIUR_B], {"ca_thr": F.ca_thr(), "div_segments": F.div_segments()})

# ═════════════════════════════════════════════ 11
sec("nephro-phy2-11", "กรดมาจากไหน และสามแนวป้องกัน pH — buffer · ปอด · ไต",
    "CO2 15,000 mmol/วัน กับ fixed acid 70 mEq/วัน · buffer ในเลือด เซลล์ กระดูก ปัสสาวะ · H/K exchange · Henderson–Hasselbalch", 8,
"""### แหล่งกรด–ด่าง (สไลด์ Control of acid-base balance)
pH ปกติ **7.35–7.45** (ในคลินิกใช้ 7.40)
| แหล่ง | ปริมาณ/วัน | ใครกำจัด |
|---|---|---|
| อาหาร | 20 mEq H+ | ไต |
| ทางเดินอาหารหลั่ง OH−/HCO3 ทิ้งในอุจจาระ → เหลือ H ในร่างกาย | 10 mEq H+ | ไต |
| เมตาบอลิซึม: **volatile acid (CO2)** | **~15,000 mmol** | **ปอด** |
| เมตาบอลิซึม: **fixed (non-volatile) acid** เช่น lactic sulfuric phosphoric keto acid | 40 mEq H+ | ไต |
| **รวม fixed acid ที่ไตต้องขับ** | **~70 mEq/วัน** | ไต (ไม่มีทางอื่น) |
**ด่าง**: HCO3 จากการเผาผลาญ organic anion (citrate) · NH3 จากกรดอะมิโน (ตับเปลี่ยนเป็น urea)

### แนวที่ 1 — Buffer (สไลด์ Buffers system)
ทำงาน **ทันที** แต่แค่ "จับ" H ไว้ **ไม่ได้กำจัดกรดออกจากร่างกาย**
| ที่ | buffer |
|---|---|
| พลาสมา | **HCO3 (80%)** · โปรตีน (15%) · inorganic phosphate (5%) |
| RBC | **hemoglobin** (สำคัญกับ CO2) · HCO3 · organic phosphate (ATP 2,3-DPG) |
| ICF | โปรตีน · inorganic/organic phosphate (ATP ADP creatine phosphate) |
| กระดูก | mineral phosphate และ carbonate — acidosis เรื้อรัง (CKD) จึงสลายกระดูก |
| ปัสสาวะ | phosphate (HPO4 → H2PO4) · ammonia (NH3 → NH4) |
**ICF buffer**: H เข้าเซลล์ (จับโปรตีนและ phosphate) แลกกับ K ออก → acidemia ทำให้ PK สูง — ⚠️ **ไม่เกิดใน respiratory disorder และ organic acidosis** (lactate ketone เข้าเซลล์พร้อม H) · โปรตีนเป็น **amphoteric** — มีทั้งหมู่กรด (COOH) และหมู่ด่าง (NH2)

### แนวที่ 2 — ปอด (สไลด์ Respiratory system)
H+ ↑/PCO2 ↑ → chemoreceptor (carotid/aortic และ central) → ศูนย์หายใจใน medulla → ↑ ventilation → เป่า CO2 ทิ้ง · ตอบสนองใน **นาที–ชั่วโมง เต็มที่ 12–24 ชม.** · แก้ pH ได้ **~50–60%**
### แนวที่ 3 — ไต (สไลด์ Renal system)
ตอบสนองใน **ชั่วโมง–หลายวัน** แต่ **แรงที่สุด** — ทำ 3 อย่าง: ดูด HCO3 ที่กรองกลับ · สร้าง HCO3 ใหม่ · ขับ H (หัวข้อ 12)

[[fig:defense]]

### Henderson–Hasselbalch (สไลด์ Acid–base disorder)
**pH = 6.1 + log ( [HCO3] ÷ 0.03 × PaCO2 )** — ค่าปกติ 24 ÷ (0.03 × 40 = 1.2) = 20 → log 20 = 1.3 → pH 7.4
- pH ขึ้นกับ **อัตราส่วน** ไม่ใช่ค่าใดค่าหนึ่ง → ไตคุม "ตัวเศษ" ปอดคุม "ตัวส่วน" → เป็นพื้นฐานของการชดเชย (หัวข้อ 13)

#### ทำไม HCO3 เป็น buffer ที่สำคัญที่สุดทั้งที่ pKa 6.1 ห่างจาก 7.4
buffer ทั่วไปทำงานดีเมื่อ pH ใกล้ pKa แต่ระบบ HCO3/CO2 เป็น **ระบบเปิด** — CO2 ที่เกิดจากการจับ H ถูก **ปอดเป่าทิ้งทันที** (PaCO2 ไม่สะสม) และ **ไตเติม HCO3 ใหม่** ได้ · buffer อื่นเป็นระบบปิด จับ H ได้จนหมดแล้วก็จบ (เติมจาก Boron — ไม่อยู่ในสไลด์)
""",
    ["Fixed acid ~70 mEq/วัน ต้องขับทางไตเท่านั้น · CO2 15,000 mmol/วัน ออกทางปอด",
     "Buffer ทันทีแต่ไม่กำจัดกรด · ปอด นาที–ชม. แก้ ~50–60% · ไต ชม.–วัน แรงสุด",
     "พลาสมา: HCO3 80% · โปรตีน 15% · Pi 5% · RBC: hemoglobin",
     "H/K exchange ไม่เกิดใน respiratory disorder และ organic acidosis",
     "pH = 6.1 + log(HCO3 ÷ 0.03 × PaCO2) — ขึ้นกับอัตราส่วน"],
    [mcq(N(21), "Use the Henderson–Hasselbalch equation. A patient has PaCO2 40 mmHg and HCO3 12 mEq/L. What is the arterial pH?",
         ["7.00", "7.10", "7.20", "7.30", "7.40"], 1,
         "pH = 6.1 + log (12 ÷ (0.03 × 40)) = 6.1 + log (12 ÷ 1.2) = 6.1 + log 10 = 6.1 + 1 = **7.10** · ภาวะนี้ HCO3 ลดครึ่งหนึ่งโดยที่ PaCO2 ยังไม่ชดเชย — ถ้าปอดชดเชยตาม Winter (PaCO2 ~26) pH จะกลับมาเป็น ~7.29 (6.1 + log (12 ÷ 0.78) = 6.1 + 1.19)\n\n"
         "- **7.40** — ต้องมีอัตราส่วน 20:1 (เช่น 24/1.2)\n- **7.00 / 7.20 / 7.30** — คำนวณ log ผิด (log 10 = 1)",
         "pH = 6.1 + log(HCO3/0.03PaCO2) — HCO3 ครึ่ง ไม่ชดเชย → pH 7.10", "Henderson–Hasselbalch", R("Henderson–Hasselbalch equation"), [AB_B, BUFFER_B, ABG_B]),
     mcq(N(22), "The pKa of the bicarbonate buffer system (6.1) is far from normal plasma pH (7.4), yet it is the most important extracellular buffer. Why?",
         ["It is an open system: CO2 generated by buffering is exhaled by the lungs and HCO3 is regenerated by the kidneys",
          "Bicarbonate has the highest pKa of all body buffers",
          "Hemoglobin cannot buffer H+ inside red blood cells",
          "Bicarbonate buffering removes H+ from the body without any renal involvement",
          "Phosphate is absent from plasma, so bicarbonate is the only available buffer"], 0,
         "buffer ที่ pKa ห่างจาก pH ควรทำงานไม่ดี แต่ระบบ HCO3/CO2 **เปิด** — H + HCO3 → CO2 + H2O แล้ว **ปอดเป่า CO2 ทิ้ง** ทำให้ PaCO2 ไม่สะสมและปฏิกิริยาเดินหน้าได้ต่อ · **ไตสร้าง HCO3 ใหม่** มาแทนที่ที่ใช้ไป · ปริมาณ HCO3 ในพลาสมายังสูง (24 mEq/L = 80% ของการ buffer ในพลาสมา ตามสไลด์)\n\n"
         "- **pKa สูงสุด** — ผิด 6.1 ต่ำกว่า phosphate (6.8)\n- **Hb buffer ไม่ได้** — Hb เป็น buffer สำคัญใน RBC (สไลด์)\n"
         "- **กำจัด H ได้โดยไม่ต้องใช้ไต** — buffer ใด ๆ ไม่กำจัด fixed acid ต้องอาศัยไตเติม HCO3\n- **ไม่มี phosphate ในพลาสมา** — มี (5%)",
         "HCO3/CO2 = ระบบเปิด (ปอด + ไต)", "Bicarbonate buffer as an open system", R("Buffers system", BB), [AB_B, BUFFER_B, RESPCTRL_B])],
    [AB_B, BUFFER_B, RESPCTRL_B, ABG_B], {"defense": F.defense()})

# ═════════════════════════════════════════════ 12
sec("nephro-phy2-12", "ไตกับกรด — เก็บ HCO3 คืน สร้าง HCO3 ใหม่ และขับ H ด้วย phosphate กับ ammonium",
    "Reclamation ที่ PT · titratable acid 40% · NH4 60% · NAE · ปัจจัยที่เพิ่มการขับ H · contraction alkalosis · RTA type 1/2/4", 10,
"""### 3.1 ดูด HCO3 ที่กรองกลับ (reclamation)
- กรองวันละ ~4,320 mmol (สไลด์) ต้องเก็บคืนเกือบหมด · ภาพในสไลด์: **PT ~80% · TAL ~10% · DT ~6% · CD ~4%**
- กลไกที่ PT: H ออกทาง **NHE3** → จับ HCO3 ในท่อ → CO2 + H2O (carbonic anhydrase) → แพร่เข้าเซลล์ → H + HCO3 → HCO3 กลับเลือดทาง NBCe1
- **ไม่มีการขับ H สุทธิ** — แค่ได้ HCO3 ตัวเดิมคืน
- HCO3 ในพลาสมา **> ~25 mEq/L** → เกินกำลังดูดกลับ → ออกในปัสสาวะ (สไลด์ titration curve) = วิธีที่ไตแก้ alkalosis

[[fig:pt_hco3]]

### 3.2–3.3 ขับ H และสร้าง HCO3 ใหม่
- ขับ H ได้ทั่วท่อไต แต่ตัวหลักคือ **late DT และ cortical CD (type A-IC)**
- ปัสสาวะเป็นกรดได้ต่ำสุด **pH 4.5** = H อิสระ 0.03 mEq/L → ถ้าขับ 70 mEq เป็น H อิสระต้องใช้ปัสสาวะ **~2,667 L/วัน** (สไลด์) → จึงต้องผูก H กับ buffer · ปัสสาวะปกติ pH 6–6.5
| รูปแบบ | สัดส่วน | กลไก |
|---|---|---|
| **Titratable acid** (NaH2PO4) | ~40% | Na2HPO4 ที่กรองมาและไม่ถูกดูดกลับ รับ H → H2PO4 · **ปริมาณจำกัด** ตาม phosphate ที่กรอง |
| **Ammonium** (NH4Cl) | ~60% | **ammoniagenesis** ที่ PT: glutamine → NH4 + HCO3 ใหม่ · NH4 ถูกดูดกลับที่ TAL (แทน K บน NKCC2) สะสมใน medulla → NH3 แพร่เข้า CD → จับ H เป็น NH4 **ติดอยู่ในท่อ** · **เพิ่มได้หลายเท่าเมื่อ acidosis เรื้อรัง และเมื่อ K ต่ำ** |
**1 H ที่ขับ = 1 HCO3 ใหม่เข้าเลือด**
**Net acid excretion (NAE) = (TA + NH4) − HCO3 ในปัสสาวะ = [(U_TA × V) + (U_NH4 × V)] − (U_HCO3 × V)** ≈ 70 mEq/วัน = fixed acid ที่สร้าง

[[fig:nae]]

### ปัจจัยที่เพิ่มการดูด HCO3 กลับ/สร้าง HCO3/ขับ H (สไลด์ Factors affecting)
| ปัจจัย | กลไก |
|---|---|
| ↑ PaCO2 (ปัญหาการหายใจ) | CO2 เข้าเซลล์มาก → H ในเซลล์มาก → ขับ H มาก (การชดเชย respiratory acidosis) |
| ↑ [H] จาก fixed acid | กระตุ้นทุกขั้น + ammoniagenesis |
| ↑ lumen ลบ (ดูด Na ที่ P cell มาก) | H ถูกดึงออกง่าย |
| **K ต่ำ** | ↑ ammoniagenesis ที่ PT · ↑ H/K-ATPase ที่ A-IC (แลก K กลับ ขับ H ออก) |
| **↑ Ang II** | ↑ NHE3 ที่ PT |
| **↑ aldosterone** | ↑ ดูด Na ที่ P cell (lumen ลบ) + ↑ H+-ATPase ที่ A-IC |
**↓ ECF volume → ↑ Ang II + aldosterone → ↑ ขับ H ↑ ดูด HCO3 → metabolic alkalosis = contraction alkalosis** (✍️ ลายมือ: เช่น ระบาย ascites ยาขับปัสสาวะ)

### Renal tubular acidosis — เมื่อขั้นใดขั้นหนึ่งเสีย (สไลด์ตาราง metabolic acidosis · รายละเอียดเติมจาก Boron)
| | Type 1 (distal) | Type 2 (proximal) | Type 4 (hypoaldosteronism) |
|---|---|---|---|
| ขั้นที่เสีย | A-IC **ขับ H ไม่ได้** ("acidify urine ไม่ได้") | PT **ดูด HCO3 กลับไม่ได้** (threshold ต่ำ) | ขาด/ดื้อ aldosterone → **ขับ K และ H ไม่ได้** · K สูงกด ammoniagenesis → **NH4 ↓** |
| urine pH | **> 5.5 เสมอ** | > 5.5 ช่วงแรก · **< 5.5 เมื่อ HCO3 ต่ำกว่า threshold** | **< 5.5** (ขับ H ได้แต่ไม่มี NH3 มารับ) |
| K | **ต่ำ** | **ต่ำ** (HCO3 ล้นไปส่วนปลาย = anion + aldosterone) | **สูง** |
| อื่น ๆ | นิ่ว/nephrocalcinosis (ปัสสาวะด่าง citrate ต่ำ) | Fanconi (glucose PO4 กรดอะมิโนรั่ว) · ภาวะกระดูกอ่อน | เบาหวาน CKD · ยา ACEi spironolactone |
ทั้งสามแบบเป็น **normal anion gap (hyperchloremic)** เพราะไม่มี anion ใหม่ · ตัวขนส่งที่เสียในแต่ละแบบ (และ Fanconi) ทบทวนในคาบ **Physio1** — ที่นี่เน้นว่า "ทำไม K ต่างกัน"

#### ทำไม RTA แต่ละแบบ K ต่างกัน
- **type 1**: H-ATPase เสีย → การขับ Na ที่ปลายท่ออาศัยแลกกับ K แทน H + ปริมาตรลดเล็กน้อย → aldosterone → **K ต่ำ**
- **type 2**: HCO3 ที่ PT ดูดไม่ได้ล้นไปส่วนปลาย → anion ในท่อ + Na/flow สูง + aldosterone → **K ต่ำ** (แย่ลงเมื่อให้ NaHCO3)
- **type 4**: aldosterone ไม่มีผล → P cell ไม่ขับ K → **K สูง** → K สูงยังกด ammoniagenesis → ขับกรดเป็น NH4 ไม่ได้ → acidosis
""",
    ["Reclamation: PT ~80% ผ่าน NHE3 + CA — ไม่มีการขับ H สุทธิ",
     "Titratable acid 40% (phosphate, จำกัด) · NH4 60% (เพิ่มได้มาก) · 1 H ขับ = 1 HCO3 ใหม่",
     "NAE = TA + NH4 − HCO3 ≈ 70 mEq/วัน · urine pH ต่ำสุด 4.5",
     "ปริมาตรลด → Ang II + aldosterone → contraction alkalosis · K ต่ำ ↑ ammoniagenesis",
     "RTA: type 1 urine pH > 5.5 K ต่ำ · type 2 bicarbonaturia K ต่ำ · type 4 K สูง NH4 ต่ำ"],
    [mcq(N(23), "A 64-year-old man with diabetic nephropathy (eGFR 40 mL/min/1.73 m²) has Na 138, K 6.0, Cl 112, HCO3 18 mEq/L; urine pH 5.2. Plasma renin and aldosterone are low. What is the main reason he cannot excrete his daily acid load normally?",
         ["Hypoaldosteronism with hyperkalemia suppresses proximal ammoniagenesis, so NH4 excretion falls (type 4 RTA)",
          "Type A intercalated cells cannot secrete H, so urine pH cannot fall below 5.5 (type 1 RTA)",
          "The proximal tubule has a low threshold for HCO3 reabsorption (type 2 RTA)",
          "Accumulation of unmeasured organic anions from reduced GFR (uremic acidosis)",
          "Gastrointestinal HCO3 loss with an appropriately increased urinary NH4"], 0,
         "normal AG (138 − 130 = 8) · **K สูง** · urine pH < 5.5 (ยังขับ H ได้) · renin/aldosterone ต่ำ (hyporeninemic hypoaldosteronism พบบ่อยในเบาหวาน) → **type 4 RTA**: ขาด aldosterone → ขับ K/H ลด · **K สูงกด ammoniagenesis** → NH4 ซึ่งเป็นทางขับกรดหลัก (60%) ลด → NAE ลด (สไลด์: type 4 RTA hyperkalemia inhibits NH3 synthesis)\n\n"
         "- **type 1** — urine pH จะ > 5.5 และ K ต่ำ\n- **type 2** — K ต่ำ และมักมี Fanconi\n"
         "- **uremic acidosis** — มัก AG กว้างเมื่อ GFR < ~15–20 · ผู้ป่วยนี้ AG ปกติ\n- **GI loss** — NH4 จะ **เพิ่ม** (urine AG ลบ) และ K มักต่ำ",
         "NAG acidosis + K สูง + urine pH < 5.5 → type 4 RTA", "Type 4 RTA", R("Metabolic acidosis table · Ammonium salt excretion", BB), [RTA, AB_B, HYPERK, CKD]),
     mcq(N(24), "A healthy volunteer on a typical diet collects 24-hour urine: volume 1.5 L, titratable acid 20 mEq/L, NH4 30 mEq/L, HCO3 2 mEq/L. What is the net acid excretion?",
         ["45 mEq/day", "48 mEq/day", "72 mEq/day", "75 mEq/day", "78 mEq/day"], 2,
         "NAE = (U_TA × V) + (U_NH4 × V) − (U_HCO3 × V) = (20 × 1.5) + (30 × 1.5) − (2 × 1.5) = 30 + 45 − 3 = **72 mEq/วัน** — ใกล้ fixed acid ~70 mEq ที่สไลด์ระบุ = สมดุล\n\n"
         "- **45** = NH4 อย่างเดียว\n- **48** = (20 + 30 − 2) ลืมคูณปริมาตร\n- **75** = ลืมหัก HCO3 · **78** = บวก HCO3 แทนที่จะลบ (HCO3 ที่หลุดในปัสสาวะเท่ากับเสียด่าง)",
         "NAE = TA + NH4 − HCO3 (คูณปริมาตร)", "Net acid excretion", R("Net acid excretion (NAE)"), [AB_B, TUB_B])],
    [AB_B, TUB_B, RTA, HYPERK], {"pt_hco3": F.pt_hco3(), "nae": F.nae()})

# ═════════════════════════════════════════════ 13
sec("nephro-phy2-13", "ความผิดปกติกรด-ด่างและการชดเชย — กลไกเบื้องหลังอาการ",
    "4 primary disorders · buffer + ปอด + ไต · K และ ionized Ca เปลี่ยนตาม · DKA/Kussmaul · อาเจียน/paradoxical aciduria · mixed", 11,
"""### แบ่งตามตัวที่ผิดก่อน (สไลด์ Acid–base disorder)
**simple** = สาเหตุเดียว · **mixed** = ≥ 2 สาเหตุ (✍️ ลายมือ: พบเป็นส่วนมาก)
| ตัวหลัก | ภาวะ | สาเหตุกลุ่มใหญ่ |
|---|---|---|
| ↓ HCO3 → ↓ pH | **metabolic acidosis** | เมตาบอลิซึมหรือไต |
| ↑ HCO3 → ↑ pH | **metabolic alkalosis** | เมตาบอลิซึมหรือไต |
| ↑ PaCO2 → ↓ pH | **respiratory acidosis** | ระบบหายใจ |
| ↓ PaCO2 → ↑ pH | **respiratory alkalosis** | ระบบหายใจ |

[[fig:comp]]

### การชดเชยของแต่ละภาวะ (สไลด์ Compensatory mechanisms)
| ภาวะ | 1 Buffer | 2 ปอด | 3 ไต |
|---|---|---|---|
| **Metabolic acidosis** | HCO3 ถูกใช้ · H ไล่ Ca จาก albumin → **ionized Ca ↑** · H เข้าเซลล์แลก K → **K ↑** | ↑ VT และ RR (**Kussmaul**) → ↓ PaCO2 | ↑ ดูด/สร้าง HCO3 · ↑ ammoniagenesis · ↑ NAE → ปัสสาวะเป็นกรด |
| **Metabolic alkalosis** | albumin ปล่อย H จับ Ca → **ionized Ca ↓** · H ออกจากเซลล์ K เข้า → **K ↓** | หายใจช้า-ตื้น → ↑ PaCO2 (จำกัดด้วย hypoxemia) | ↓ ดูด HCO3 · ↓ NAE → ปัสสาวะด่าง |
| **Respiratory acidosis** | **acute**: ICF buffer — CO2 เข้าเซลล์ → H จับโปรตีน/phosphate (HCO3 ขึ้นนิดเดียว) | — | **chronic**: ↑ ดูด/สร้าง HCO3 ↑ ammoniagenesis → HCO3 ↑ ชัด |
| **Respiratory alkalosis** | **acute**: ICF buffer | — | **chronic**: ↓ ดูด HCO3 ↓ ammoniagenesis → HCO3 ↓ |

### สาเหตุตามสไลด์
- **Metabolic acidosis** — กรดเกิน: DKA · lactic (hypoxemia หรือ hypoperfusion) · salicylate (ระยะหลัง) · methanol · ethylene glycol | เสีย HCO3: diarrhea · type 2 RTA | ขับ H ไม่ได้: CKD · type 1 RTA · type 4 RTA
- **Metabolic alkalosis** — เสีย H: **อาเจียน** · hyperaldosteronism | ได้ HCO3: NaHCO3 · milk-alkali | **contraction alkalosis**: loop/thiazide
- **Respiratory acidosis** — กดศูนย์หายใจ (opiate barbiturate ยาสลบ รอยโรค CNS central sleep apnea · ให้ O2 ในผู้ป่วยกักเก็บ CO2) · กล้ามเนื้อหายใจ (GBS polio ALS MS) · ทางเดินหายใจอุด (สำลัก OSA laryngospasm) · แลกเปลี่ยนก๊าซ (ARDS COPD pneumonia pulmonary edema)
- **Respiratory alkalosis** — กระตุ้นศูนย์หายใจ (hysterical hyperventilation · gram-negative sepsis · salicylate ระยะแรก · โรค CNS) · hypoxemia (ที่สูง pneumonia PE) · เครื่องช่วยหายใจ

### Mixed disorders (สไลด์ Table 9.12)
| สถานการณ์ | ความผิดปกติ |
|---|---|
| หัวใจหยุดเต้น | respiratory acidosis + lactic acidosis |
| อาเจียนหลังผ่าตัด + หายใจเร็วจากปวด | metabolic alkalosis + respiratory alkalosis |
| ✍️ ไตวาย + อาเจียน | metabolic acidosis + metabolic alkalosis |
| ตับวาย | respiratory alkalosis + metabolic acidosis |
| DKA + อาเจียน / DKA + lactic | met. acidosis + met. alkalosis / high AG สองชนิด |
| COPD + ยาขับปัสสาวะ | respiratory acidosis + metabolic alkalosis |
| septic shock + ARDS | metabolic acidosis + respiratory acidosis |
| **salicylate** | **respiratory alkalosis + metabolic acidosis** |

#### ทำไมถึงมีอาการนี้ — DKA หายใจหอบลึก (Kussmaul)
[[fig:dka]]
#### ทำไมถึงมีอาการนี้ — อาเจียนแล้ว K ต่ำ และปัสสาวะเป็นกรดทั้งที่เลือดด่าง
[[fig:vomit]]
- **salicylate ทำไมเป็นสองภาวะ** — ช่วงแรกกระตุ้นศูนย์หายใจโดยตรง (resp. alkalosis) ต่อมาขัดขวาง oxidative phosphorylation → lactic + ketoacid สะสม (met. acidosis)
- **COPD ได้ O2 สูงแล้วซึม** — สไลด์จัดเป็นสาเหตุ resp. acidosis: hypoxic drive ลด + V/Q แย่ลง (Haldane) → CO2 คั่ง
> กลไก K ใน DKA, ระยะของการอาเจียน urine Cl และ salicylate/O2 เติมจากตำรา (Boron · Guyton · ADA hyperglycemic crises consensus 2024)
""",
    ["ชดเชยไปทางเดียวกับตัวหลักเสมอ ไม่เคยเกิน",
     "Metabolic acidosis: Kussmaul (VT ↑ มากกว่า RR) · ionized Ca ↑ · K ↑ (กรดแร่)",
     "Metabolic alkalosis: hypoventilation · ionized Ca ↓ · K ↓",
     "Respiratory: acute = ICF buffer (HCO3 เปลี่ยนนิด) · chronic = ไตชดเชย 3–5 วัน",
     "อาเจียน: generation (เสีย HCl) + maintenance (volume/Cl/K ต่ำ + aldosterone) → paradoxical aciduria"],
    [mcq(N(25), "A 19-year-old woman with type 1 diabetes has had vomiting for 2 days and now seems drowsy. Glucose 480 mg/dL, Na 134, Cl 98, HCO3 8 mEq/L. ABG: pH 7.11, PaCO2 26 mmHg. What is the acid–base diagnosis?",
         ["High anion gap metabolic acidosis with a concomitant respiratory acidosis",
          "High anion gap metabolic acidosis with appropriate respiratory compensation",
          "High anion gap metabolic acidosis with a concomitant respiratory alkalosis",
          "Normal anion gap metabolic acidosis with appropriate respiratory compensation",
          "Acute respiratory acidosis with metabolic compensation"], 0,
         "AG = 134 − (98 + 8) = **28** → high AG (DKA) · Winter: PaCO2 คาด = 1.5 × 8 + 8 = **20 ± 2 (18–22)** · วัดได้ **26 > 22** → ปอดชดเชยไม่พอ = **respiratory acidosis ร่วม** (ง่วงซึม กล้ามเนื้อหายใจล้า ปอดอักเสบ/สำลัก) — เป็นสัญญาณอันตรายว่ากำลังจะหายใจล้มเหลว · ตรวจสอบ pH: 6.1 + log (8 ÷ 0.78) = 6.1 + 1.01 = 7.11 ✓\n\n"
         "- **ชดเชยเหมาะสม** — ต้อง 18–22\n- **resp. alkalosis ร่วม** — PaCO2 ต้อง < 18\n"
         "- **normal AG** — AG 28 กว้าง\n- **resp. acidosis ปฐมภูมิ** — PaCO2 26 ต่ำกว่าปกติ ไม่ใช่สูง",
         "Winter: PaCO2 = 1.5 × HCO3 + 8 ± 2 — สูงกว่าช่วง = resp. acidosis ร่วม", "Winter's formula in DKA", R("Metabolic acidosis · compensatory mechanisms", "Berend NEJM 2014"), [AB_B, DM, ABG, LYTE]),
     mcq(N(26), "A 46-year-old man with gastric outlet obstruction has vomited for 5 days. Na 132, K 2.8, Cl 82, HCO3 38 mEq/L; ABG pH 7.53, PaCO2 47 mmHg. Urine pH 5.5, urine Na 15 mEq/L, urine Cl 8 mEq/L. Why is his urine acidic despite alkalemia?",
         ["Volume and Cl depletion, hypokalemia and high aldosterone drive H+ secretion and HCO3 reabsorption, maintaining the alkalosis",
          "Gastric H+ is absorbed in the small intestine and excreted in urine",
          "Respiratory compensation raises PaCO2, which is the only stimulus for renal H+ secretion",
          "Alkalemia directly stimulates H+-ATPase in type B intercalated cells",
          "He has a coexisting distal renal tubular acidosis"], 0,
         "**paradoxical aciduria**: ไตต้องเลือกระหว่าง \"รักษาปริมาตร\" กับ \"แก้ pH\" — ปริมาตรลด + Cl ต่ำ → Ang II (↑ NHE3 ดูด HCO3) + aldosterone (↑ H+-ATPase) · **K ต่ำ** → ↑ H/K-ATPase และ ammoniagenesis → ขับ H ออกต่อ ทั้งที่เลือดด่าง (สไลด์ Factors affecting HCO3 reabsorption · contraction alkalosis) · urine Cl 8 = saline-responsive → แก้ด้วย NSS + KCl · PaCO2 คาด 0.7 × 38 + 20 = 46.6 ✓ ชดเชยเหมาะสม\n\n"
         "- **H จากกระเพาะถูกดูดซึมแล้วขับ** — H ถูกอาเจียนทิ้งไปแล้ว\n- **PaCO2 เป็นตัวกระตุ้นเดียว** — PaCO2 47 มีผลน้อย ตัวหลักคือ volume/Cl/K/aldosterone\n"
         "- **B-IC** — เซลล์ชนิด B ขับ **HCO3** ไม่ใช่ H (ทำงานเมื่อ alkalosis)\n- **distal RTA** — จะเป็น acidosis ไม่ใช่ alkalosis",
         "อาเจียน + urine pH ต่ำ + UCl ต่ำ = maintenance ด้วยปริมาตร/K → ให้ NSS + KCl", "Vomiting and paradoxical aciduria", R("Metabolic alkalosis · Factors affecting HCO3 reabsorption"), [AB_B, VOMIT, LYTE, HYPOVOL_B])],
    [AB_B, LYTE, LYTE_B, DM, VOMIT, COPD, RESPFAIL_B, POISON], {"comp": F.comp(), "dka": F.dka(), "vomit": F.vomit()}, source=SRC_ADD)

# ═════════════════════════════════════════════ 14
sec("nephro-phy2-14", "แปลผลกรด-ด่างทีละขั้น — ABG, anion gap, delta ratio, osmolal gap และแบบฝึกจากสไลด์",
    "ค่าปกติ · HCO3 จาก ABG เทียบ TCO2 · สูตรการชดเชย · AG และ albumin · wide vs normal AG · ฝึก 10 ข้อของสไลด์", 12,
"""### ค่าปกติ (สไลด์ Analysis and clinical evaluation)
| | ค่าเฉลี่ย | ช่วง |
|---|---|---|
| pH | 7.40 | 7.35–7.45 ([H] 40 nmol/L) |
| PaCO2 | 40 mmHg | 35–45 |
| HCO3 | 24 mEq/L | 22–26 |
- HCO3 ใน ABG **คำนวณ** จาก pH และ PaCO2 ด้วย Henderson–Hasselbalch — สไลด์: ใช้วิเคราะห์ได้ดีเมื่อร่างกายอยู่ในสมดุล (chronic) · **ถ้ากำลังเปลี่ยนแปลง หรือจะคำนวณ compensation/AG ให้ใช้ HCO3 จาก electrolyte (TCO2) ที่เจาะเวลาเดียวกัน** · สองค่านี้ควรต่างกันไม่เกิน 10%
- ตัวอย่างใบผลในสไลด์: pH 7.326 · pCO2 33.4 · HCO3 17.1 · BE −8.9 · TCO2 18.1 → ✍️ **metabolic acidosis** · Winter: 1.5 × 17.1 + 8 = 33.7 ± 2 → PaCO2 33.4 = **ชดเชยเหมาะสม** (การคำนวณนี้เติมโดยบทเรียน)

### ขั้นตอน (สไลด์ Stepwise approach + ส่วนเติม)
[[fig:steps]]
| ขั้น | ทำอะไร |
|---|---|
| 1 | pH < 7.4 = acidosis · > 7.4 = alkalosis |
| 2 | ตัวไหนอธิบายทิศ pH — HCO3 < 24 กับ acidosis = metabolic · PaCO2 > 40 กับ acidosis = respiratory (กลับกันสำหรับ alkalosis) |
| 3 | มีการชดเชยไหม (uncompensated vs compensated) และ **พอดีไหม** |
| 4 | metabolic acidosis → **anion gap** |

### สูตรการชดเชยที่คาดไว้ (เติมจากตำรา — ชุดเดียวกับคาบ chest 26)
| ภาวะหลัก | ค่าที่คาด |
|---|---|
| Metabolic acidosis | **PaCO2 = 1.5 × HCO3 + 8 ± 2** (Winter) |
| Metabolic alkalosis | **PaCO2 ≈ 0.7 × HCO3 + 20 ± 2** |
| Respiratory acidosis | HCO3 ↑ **1** (acute) หรือ **4** (chronic) ต่อ PaCO2 ↑ 10 |
| Respiratory alkalosis | HCO3 ↓ **2** (acute) หรือ **5** (chronic) ต่อ PaCO2 ↓ 10 |
นอกช่วง = มีความผิดปกติที่สอง · สไลด์: acute respiratory = HCO3 เปลี่ยนนิดเดียว (buffer) · chronic = เปลี่ยนมาก (ไต)

### Anion gap (สไลด์ Differential diagnosis cause of metabolic acidosis)
**AG = Na − (Cl + HCO3)** · ปกติ **10 ± 2** · ส่วนใหญ่คือ **albumin** (+ phosphate citrate sulfate)
- albumin ลดทุก 1 g/dL จาก 4 → AG แคบลง ~2.5 → **corrected AG = AG + 2.5 × (4 − albumin)** (ตับแข็ง ขาดอาหาร nephrotic)
[[fig:gamble]]
| AG กว้าง (> 12) · Cl ปกติ — **กรดเติมเข้า** | AG ปกติ · **Cl > 110** — **เสีย HCO3 หรือขับ H ไม่ได้** |
|---|---|
| ketoacidosis (DM อดอาหาร สุรา): acetoacetate β-OHB | **diarrhea**: เสีย HCO3 จากน้ำย่อยตับอ่อนและน้ำดี |
| lactic acidosis: lactate | **carbonic anhydrase inhibitor**: เสีย HCO3 ทางปัสสาวะ |
| CKD: ขับ anion ไม่ได้ | **spironolactone, hypoaldosteronism**: ขับ H ที่ไตลดลง (+ RTA) |
| aspirin: salicylate · methanol: formate | |
| ethylene glycol: glycolate oxalate · toluene: hippurate benzoate | |

### ขั้นต่อ (เติมจาก Berend NEJM 2014 · Boron)
- **Delta ratio = (AG − 12) ÷ (24 − HCO3)** · < 1 = มี normal AG acidosis ร่วม · 1–2 = high AG อย่างเดียว · **> 2 = มี metabolic alkalosis ร่วม** (เช่น DKA ที่อาเจียน)
- **Osmolal gap = Posm ที่วัด − (2Na + glucose/18 + BUN/2.8)** · > 10 → มี osmole ที่ไม่ได้วัด: **methanol ethylene glycol** (ethanol ก็เพิ่มแต่ไม่ทำ AG กว้าง)
- **Urine AG = UNa + UK − UCl** ใน normal AG acidosis · **ลบ** = ไตขับ NH4 (มากับ Cl) ได้ดี → สาเหตุนอกไต (ท้องเสีย) · **บวก** = ไตขับ NH4 ไม่ได้ → RTA type 1/4

### แบบฝึกในสไลด์ — 10 ABG (เฉลยโดยบทเรียน)
| # | pH | PaCO2 | HCO3 | คำตอบ |
|---|---|---|---|---|
| 1 | 7.49 | 44 | 32 | **metabolic alkalosis** ชดเชยพอดี (คาด 0.7 × 32 + 20 = 42.4 ± 2) — ✍️ ตรงกับลายมือ |
| 2 | 7.30 | 55 | 26 | **acute respiratory acidosis** (คาด HCO3 24 + 1.5 = 25.5) |
| 3 | 7.29 | 30 | 14 | **metabolic acidosis** ชดเชยพอดี (Winter 29 ± 2) |
| 4 | 7.68 | 27 | 30 | **mixed: respiratory alkalosis + metabolic alkalosis** (ทั้งสองตัวไปทางด่าง) |
| 5 | 7.27 | 58 | 26 | **acute respiratory acidosis** (คาด 25.8) |
| 6 | 7.40 | 25 | 15 | **mixed: metabolic acidosis + respiratory alkalosis** (Winter 30.5 ± 2 แต่ PaCO2 25 · pH ปกติพอดี) — ✍️ ตรงกับลายมือ · เช่น salicylate sepsis ตับวาย |
| 7 | 7.48 | 25 | 17 | **chronic respiratory alkalosis** (คาด acute 21 · chronic 16.5) · ตาม HH ค่าชุดนี้ให้ pH ~7.46 |
| 8 | 7.43 | 75 | 48 | **chronic respiratory acidosis + metabolic alkalosis** (คาด HCO3 24 + 4 × 3.5 = 38 แต่วัดได้ 48) — เช่น COPD ที่ได้ยาขับปัสสาวะ/steroid |
| 9 | 7.31 | 80 | 39 | **chronic respiratory acidosis** ชดเชยพอดี (คาด 24 + 16 = 40) |
| 10 | 7.52 | 23 | 18 | **respiratory alkalosis** HCO3 อยู่ระหว่าง acute (20.6) กับ chronic (15.5) → กำลังชดเชย หรือมี metabolic acidosis เล็กน้อยร่วม |
""",
    ["ใช้ TCO2 จาก electrolyte คำนวณ AG/compensation · ABG HCO3 เป็นค่าคำนวณ",
     "AG = Na − (Cl + HCO3) ปกติ 10 ± 2 · แก้ albumin +2.5 ต่อ 1 g/dL ที่ลด",
     "AG กว้าง = กรดเติม · AG ปกติ Cl สูง = เสีย HCO3/ขับ H ไม่ได้",
     "Delta ratio > 2 → met. alkalosis ร่วม · < 1 → NAG ร่วม",
     "Osmolal gap > 10 + AG กว้าง → methanol/ethylene glycol"],
    [mcq(N(27), "A 35-year-old man with type 1 diabetes has vomited repeatedly for 3 days. Na 136, Cl 88, HCO3 16 mEq/L, glucose 520 mg/dL, albumin 4.0 g/dL. ABG: pH 7.34, PaCO2 31 mmHg. What is the most complete acid–base diagnosis?",
         ["High anion gap metabolic acidosis with a coexisting metabolic alkalosis",
          "High anion gap metabolic acidosis alone with appropriate respiratory compensation",
          "Combined high anion gap and normal anion gap metabolic acidosis",
          "Metabolic alkalosis with respiratory compensation",
          "Normal anion gap metabolic acidosis with respiratory alkalosis"], 0,
         "AG = 136 − (88 + 16) = **32** · ΔAG = 32 − 12 = **20** · ΔHCO3 = 24 − 16 = **8** · delta ratio = 20 ÷ 8 = **2.5 (> 2)** → HCO3 ลดน้อยกว่าที่กรดที่เติมเข้ามาควรทำ = มี **metabolic alkalosis จากการอาเจียน** ซ่อนอยู่ (ถ้าไม่มี HCO3 ควรเหลือ ~4) · Winter: 1.5 × 16 + 8 = 32 ± 2 → PaCO2 31 ชดเชยพอดี · pH: 6.1 + log (16 ÷ 0.93) = 7.34 ✓\n\n"
         "- **HAGMA อย่างเดียว** — delta ratio จะอยู่ราว 1–2\n- **HAGMA + NAGMA** — delta ratio < 1\n"
         "- **metabolic alkalosis หลัก** — pH 7.34 เป็นกรด\n- **NAGMA** — AG 32 กว้าง",
         "Delta ratio > 2 ใน DKA = มีอาเจียน/alkalosis ร่วม", "Delta–delta", R("Anion gap measurement", "Berend NEJM 2014"), [AB_B, DM, VOMIT, ABG]),
     mcq(N(28), "A 40-year-old man is brought in 18 hours after drinking homemade liquor; he now complains of blurred vision. Na 138, Cl 100, HCO3 10 mEq/L, glucose 90 mg/dL, BUN 14 mg/dL, measured serum osmolality 330 mOsm/kg; serum ethanol undetectable. ABG: pH 7.26, PaCO2 23 mmHg. What is the most likely cause?",
         ["Methanol poisoning (formate accumulation)", "Isolated ethanol intoxication", "Diabetic ketoacidosis",
          "Lactic acidosis from septic shock", "Diarrhea-induced bicarbonate loss"], 0,
         "AG = 138 − (100 + 10) = **28** (กว้าง) · Posm คำนวณ = 2(138) + 90/18 + 14/2.8 = 276 + 5 + 5 = **286** · osmolal gap = 330 − 286 = **44 (> 10)** · ไม่มี ethanol → มี osmole แปลกปลอม = **toxic alcohol** · ตามัว = **methanol → formate** ทำลาย optic nerve (สไลด์: methanol → formate · wide AG) · Winter: 1.5 × 10 + 8 = 23 ✓ ชดเชยพอดี\n\n"
         "- **ethanol อย่างเดียว** — ไม่พบ ethanol และ ethanol ไม่ทำให้ AG กว้างขนาดนี้\n- **DKA** — glucose 90\n"
         "- **lactic acidosis** — ไม่ทำให้ osmolal gap กว้าง 44 และไม่มี sepsis\n- **diarrhea** — AG ปกติ",
         "AG กว้าง + osmolal gap กว้าง + ตามัว → methanol", "Osmolal gap", R("Wide AG metabolic acidosis", "Berend NEJM 2014"), [AB_B, POISON, OSM_B, ABG])],
    [AB_B, ABG, ABG_B, OSM_B, ELYTE_B, RTA, POISON], {"steps": F.steps(), "gamble": F.gamble()}, source=SRC_ADD)

# ═════════════════════════════════════════════ 15
sec("nephro-phy2-15", "การถ่ายปัสสาวะ — ศูนย์ควบคุม เส้นประสาท micturition reflex และชนิดของการกลั้นไม่ได้",
    "Cortex · pons (PMC/PSC) · sacral S2–S4 · hypogastric/pelvic/pudendal · β3 α1 M3 nicotinic · reflex ที่ > 150 mL · urge vs overflow vs stress", 9,
"""### ศูนย์ควบคุม 3 ระดับ (สไลด์ CNS control of micturition)
| ศูนย์ | หน้าที่ |
|---|---|
| **1 Cerebral micturition center** (prefrontal cortex) | ศูนย์บัญชาการ — รับรู้ว่าเต็ม และ **อนุญาตหรือยับยั้ง** voiding reflex |
| **2 Pontine micturition center (PMC) / pontine storage center (PSC)** | สถานีถ่ายทอดระหว่างสมองกับไขสันหลัง · **สวิตช์สลับช่วงเก็บ/ช่วงขับ** · **ประสานให้หูรูดคลายพร้อม detrusor บีบ** (✍️ ประสานกล้ามเนื้อหลายส่วนพร้อมกัน) |
| **3 Sacral micturition center** (S2–S4) | ศูนย์ของ **micturition reflex** · ทางเชื่อมก้านสมองกับกระเพาะ |

### เส้นประสาท (สไลด์ Innervation)
[[fig:mict]]
| เส้นประสาท | สารสื่อ / receptor | ผล | ช่วง |
|---|---|---|---|
| **Hypogastric** (sympathetic T10–L2) | NE · **β3** ที่ detrusor · **α1** ที่คอกระเพาะ หูรูดชั้นใน ท่อปัสสาวะ | detrusor **คลาย** · หูรูดชั้นใน **บีบ** | **เก็บ** |
| **Pelvic** (parasympathetic S2–S4) | ACh · **M3** | detrusor **บีบ** · หูรูดชั้นในคลาย | **ขับ** |
| **Pudendal** (somatic S2–S4) | ACh · **nicotinic (N)** | หูรูด **ชั้นนอก** (กล้ามเนื้อลาย) บีบ = กลั้นได้ตามใจ | เก็บ (ตั้งใจ) |
| **Aδ afferent** ใน pelvic nerve | — | ส่งสัญญาณการยืด/ความเต็ม | ทั้งสองช่วง |
สไลด์สรุป: ช่วงเก็บ — parasympathetic **ถูกยับยั้ง** · sympathetic และ somatic **ถูกกระตุ้น** | ช่วงขับ — กลับกันทั้งหมด

### Micturition reflex (สไลด์ Bladder at rest · Micturition reflex)
- **ขณะพัก**: detrusor คลาย หูรูดชั้นในหดแบบ passive หูรูดชั้นนอกหดค้าง (tonic discharge ของ pudendal)
- **ปัสสาวะ > ~150 mL** → stretch receptor → Aδ afferent → ไขสันหลัง sacral (และขึ้นไป pons/cortex) → **parasympathetic ↑** (detrusor บีบ หูรูดในเปิด) **sympathetic ↓** · **somatic ↓** (หูรูดนอกคลาย) → ปัสสาวะ
- **cortex** ตัดสินว่าจะปล่อยหรือไม่ — ถ้ายังไม่สะดวก PSC สั่ง ↑ sympathetic ↑ somatic ↓ parasympathetic → reflex ถูกกด แล้วจะกลับมาใหม่เมื่อเต็มขึ้นอีก
- ถ้าไม่ปล่อย ความรู้สึกปวดจะมาเป็นระลอกตามรอบของ reflex

### สะพานสู่คลินิก — ทำนายอาการจากตำแหน่งรอยโรค (เติมจากตำรา · ICS terminology)
[[fig:lesion]]
| ชนิด | กลไก | ตัวอย่าง |
|---|---|---|
| **Urge** (overactive) | detrusor บีบเองโดย cortex ห้ามไม่ได้ (รอยโรคเหนือ pons หรือ detrusor ไวเอง) · หูรูดยังประสานดี → ถ่ายหมด | stroke dementia NPH (wet wobbly wacky) · OAB |
| **Reflex + DSD** | ไขสันหลังเหนือ S2 ขาด → reflex ที่ sacral ยังอยู่แต่ไม่มี pons ประสาน → detrusor บีบขณะหูรูดบีบสวน | spinal cord injury หลัง spinal shock · MS |
| **Overflow** | detrusor ไม่บีบ (sacral/peripheral ขาด) หรือทางออกอุด → ค้างจนล้น | cauda equina · DM neuropathy · **BPH** · ยา anticholinergic |
| **Stress** | แรงปิดของหูรูด/อุ้งเชิงกราน < แรงดันช่องท้อง | หลังคลอด · หลังผ่าตัด prostate |

#### ทำไมถึงมีอาการนี้
- **ยาแก้หวัด (pseudoephedrine + chlorpheniramine) แล้วปัสสาวะไม่ออกในชายสูงอายุ** — α1-agonist บีบคอกระเพาะ/prostate + anticholinergic ปิด M3 ของ detrusor → overflow (ดูคาบ 22/10 Urethral catheterization)
- **ยารักษา OAB สอดคล้องกับวงจร** — oxybutynin/solifenacin (บล็อก M3) · **mirabegron (β3-agonist เลียนแบบ sympathetic ช่วงเก็บ)** · tamsulosin (บล็อก α1A ช่วยผู้ชาย BPH ถ่ายง่ายขึ้น)
- **SCI: ความดันในกระเพาะสูงทำลายไต** — DSD ทำให้ detrusor บีบกับทางออกที่ปิด → ความดันสูง → vesicoureteral reflux hydronephrosis ติดเชื้อซ้ำ
""",
    ["Cortex อนุญาต/ห้าม · pons สลับเก็บ/ขับและประสานหูรูด · S2–S4 = ศูนย์ reflex",
     "Hypogastric (T10–L2, NE): β3 คลาย detrusor · α1 บีบหูรูดใน → เก็บ",
     "Pelvic (S2–S4, ACh M3): detrusor บีบ → ขับ · Pudendal (ACh N): หูรูดนอก",
     "Reflex เริ่มที่ ~150 mL ผ่าน Aδ afferent",
     "เหนือ pons → urge · ไขสันหลัง → DSD · sacral/ทางออกอุด → overflow"],
    [mcq(N(29), "A 30-year-old man had a complete T6 spinal cord injury 4 months ago. Urodynamics show involuntary detrusor contractions while the external urethral sphincter contracts simultaneously; he has recurrent UTIs and bilateral hydronephrosis. Which best explains this pattern?",
         ["Interruption of pathways to the pontine micturition center leaves the sacral reflex intact but uncoordinated, causing detrusor–sphincter dyssynergia",
          "Destruction of the sacral micturition center produces an atonic, areflexic bladder",
          "Loss of cortical inhibition with intact pontine coordination produces urge incontinence with complete emptying",
          "Weakness of the pelvic floor allows urine leakage when abdominal pressure rises",
          "Prostatic enlargement obstructs outflow and causes overflow incontinence"], 0,
         "รอยโรคไขสันหลัง **เหนือ S2 แต่ใต้ pons** (หลังพ้น spinal shock): **sacral reflex ยังอยู่** → detrusor บีบเองเมื่อกระเพาะยืด แต่ **ขาดสวิตช์และการประสานจาก pons** → หูรูดนอกไม่คลายตาม (บีบสวน) = **detrusor–sphincter dyssynergia** → ความดันในกระเพาะสูง ปัสสาวะค้าง reflux hydronephrosis UTI (สไลด์: pons = coordinating center ของหูรูดและกระเพาะ)\n\n"
         "- **sacral ถูกทำลาย** → atonic overflow ไม่มี detrusor contraction\n- **เหนือ pons** → urge แต่ถ่ายหมด หูรูดประสานดี\n"
         "- **อุ้งเชิงกรานหย่อน** = stress incontinence\n- **BPH** — ไม่มี involuntary detrusor contraction ร่วมกับหูรูดบีบแบบนี้",
         "SCI เหนือ sacral → reflex bladder + DSD", "Neurogenic bladder by lesion level", R("CNS control of micturition · Micturition reflex"), [MICT_B, INCONT, SCI, SCI_B, RET]),
     mcq(N(30), "Which receptor–effect pairing correctly describes bladder physiology?",
         ["Sympathetic hypogastric fibers relax the detrusor via β3 receptors and contract the internal sphincter via α1 receptors during filling",
          "Parasympathetic pelvic fibers contract the detrusor via nicotinic receptors during voiding",
          "Somatic pudendal fibers contract the internal (smooth muscle) urethral sphincter via M3 receptors",
          "M3 receptor stimulation relaxes the detrusor during the storage phase",
          "Aδ afferent fibers in the pudendal nerve carry bladder-stretch signals to T10–L2"], 0,
         "ช่วง **เก็บ**: hypogastric (T10–L2) ปล่อย NE → **β3 คลาย detrusor** + **α1 บีบคอกระเพาะ/หูรูดใน** (สไลด์ Innervation)\n\n"
         "- **pelvic → nicotinic** — ผิด pelvic (parasympathetic) ใช้ **M3** บีบ detrusor · nicotinic อยู่ที่หูรูดนอก (pudendal)\n- **pudendal → หูรูดใน M3** — pudendal คุม **หูรูดนอก (กล้ามเนื้อลาย)** ผ่าน nicotinic\n"
         "- **M3 คลาย detrusor** — M3 ทำให้ **บีบ**\n- **Aδ ใน pudendal ไป T10–L2** — Aδ afferent อยู่ใน **pelvic nerve** เข้า **S2–S4**",
         "β3 คลาย · α1 บีบหูรูดใน · M3 บีบ detrusor · N หูรูดนอก", "Bladder innervation", R("Innervation of the urinary bladder and urethral sphincter"), [MICT_B, INNV, OAB_D])],
    [MICT_B, INNV, INCONT, STRESS, STRESS_B, AUR, AUR_B, OAB_D, BPH, SCI_B], {"mict": F.mict(), "lesion": F.lesion()})

# ── END SECTIONS


# ═════════════════════════════════════════════ ประกอบคาบ
LECNAME = "สรีรวิทยาไตพื้นฐาน II (Watchara Chongsa, PhD)"
MEQ = [{"id": "NEPH-PHY2-MEQ-01", "part": "MEQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Vomiting — hyposmotic volume contraction, metabolic alkalosis, hypokalemia, paradoxical aciduria and safe correction",
 "vignette": """ผู้ป่วยชายไทยอายุ 58 ปี อาเจียนทุกครั้งหลังกินอาหารมา 7 วัน (ส่องกล้องภายหลังพบ gastric outlet obstruction จากแผลเรื้อรังที่ pylorus) ช่วงนี้ดื่มได้แต่น้ำเปล่าเล็กน้อย
PE: น้ำหนัก 58 kg (เดิม 62 kg) · BP นอน 92/58 mmHg ลุกนั่ง 76/50 mmHg · PR 118/min · ปากแห้ง skin turgor ไม่ดี · JVP แฟบ · ได้ยิน succussion splash
Lab: Na 128 · K 2.6 · Cl 76 · TCO2 40 mEq/L · BUN 48 · Cr 1.6 mg/dL · glucose 110 mg/dL · albumin 4.0 g/dL
ABG: pH 7.54 · PaCO2 48 mmHg
Urine: pH 5.5 · Na 12 · K 35 · Cl 6 mEq/L · osmolality 640 mOsm/kg""",
 "questions": [
  {"q": "1. จงแปลผลกรด-ด่างทีละขั้น (ตัวหลัก การชดเชย anion gap) และบอกกลไก generation กับ maintenance (4 คะแนน)",
   "a": """**pH 7.54 = alkalemia** · HCO3 40 สูง → **metabolic alkalosis** เป็นตัวหลัก
**การชดเชย**: PaCO2 คาด = 0.7 × 40 + 20 = **48 ± 2** → วัดได้ 48 = ชดเชยทางการหายใจเหมาะสม (ตรวจ HH: 6.1 + log (40 ÷ 1.44) = 7.54)
**AG** = 128 − (76 + 40) = **12** → ปกติ ไม่มี high AG acidosis ซ่อน
**Generation**: อาเจียนเสีย HCl — parietal cell สร้าง H ออกไป HCO3 จึงเข้าเลือด
**Maintenance**: ไตไม่ยอมขับ HCO3 ส่วนเกินเพราะ (1) ปริมาตรลด → Ang II ↑ NHE3 · aldosterone ↑ H+-ATPase (2) **Cl ต่ำ** (3) **K ต่ำ** → ↑ H/K-ATPase และ ammoniagenesis (สไลด์ Factors affecting HCO3 reabsorption · contraction alkalosis)"""},
  {"q": "2. จัดภาวะสารน้ำตาม Darrow–Yannet และอธิบายกลไกของ postural hypotension, skin turgor ไม่ดี, BUN/Cr ≈ 30, UNa 12 และ Uosm 640 (4 คะแนน)",
   "a": """น้ำหนักลด 4/62 = **~6.5%** (ปานกลางถึงรุนแรง) · tonicity = 2(128) + 110/18 ≈ **262 mOsm/L** (ต่ำ) → **ECF ลด + จางลง = hyposmotic volume contraction** (เสียน้ำย่อยที่มีเกลือ แล้วดื่มน้ำเปล่าทดแทนขณะที่ ADH สูงจากปริมาตรลด → เก็บน้ำเปล่า) · น้ำบางส่วนย้ายเข้าเซลล์ ECF จึงหดมากขึ้นอีก
- **postural hypotension/ชีพจรเร็ว**: preload ต่ำ baroreflex ชดเชยไม่พอเมื่อลุกนั่ง
- **skin turgor ไม่ดี ปากแห้ง**: interstitial fluid ลด
- **BUN/Cr 30**: ADH สูง + flow ช้า → urea ถูกดูดกลับมาก (prerenal)
- **UNa 12**: sympathetic + Ang II + aldosterone + FF สูง → ดูด Na กลับเต็มที่
- **Uosm 640 ทั้งที่ Na 128**: ADH ถูกกระตุ้นแบบ **non-osmotic** จากปริมาตรลด (volume receptor/baroreceptor ชนะ osmoreceptor) — นี่คือสาเหตุของ hyponatremia"""},
  {"q": "3. ทำไม K ต่ำ ทั้งที่อาเจียนน้ำย่อยซึ่งมี K น้อย · ทำไมปัสสาวะ pH 5.5 ทั้งที่เลือดด่าง · ทำไม UCl ต่ำกว่า UNa (4 คะแนน)",
   "a": """**K ต่ำส่วนใหญ่หายทางไต** (UK 35 > 20 ทั้งที่ K 2.6): ช่วงแรก HCO3 ที่กรองเกินกำลังดูดกลับเป็น **luminal anion** ที่ทำให้ lumen ลบ + **aldosterone สูง** จากปริมาตรลด + **alkalosis** เพิ่มการเปิด ROMK/pump → P cell ขับ K มาก (สไลด์ factors 3, 5, 6) · alkalosis ยังดัน K เข้าเซลล์
**Paradoxical aciduria**: ปริมาตรลด + K ต่ำ + aldosterone → A-IC และ PT ขับ H/ดูด HCO3 เต็มที่ — ไตเลือกรักษาปริมาตรก่อน pH
**UCl 6 < UNa 12**: ร่างกายขาด Cl มาก ดูด Cl กลับเกือบหมด · Na บางส่วนถูกขับไปพร้อม HCO3 ที่ล้น → **urine Cl** จึงบอกภาวะปริมาตรได้ตรงกว่า UNa ใน metabolic alkalosis (UCl < 20 = saline-responsive)"""},
  {"q": "4. วางแผนการรักษาพร้อมเหตุผลทางสรีรวิทยา และบอกสิ่งที่ต้องเฝ้าระวังเรื่อง Na (4 คะแนน)",
   "a": """**0.9% NaCl** คืนปริมาตรและ Cl → Ang II/aldosterone ลด และมี Cl ให้ดูดกลับแทน HCO3 → ไตขับ HCO3 ออกเอง (ปัสสาวะกลายเป็นด่าง) · **KCl** ทดแทน (K ต่ำทำให้ alkalosis คงอยู่) · ใส่ NG decompress + **PPI** ลดการเสีย H · หาและแก้สาเหตุอุดตัน
**ระวัง Na ขึ้นเร็วเกิน**: เมื่อปริมาตรกลับ ADH ที่ถูกกระตุ้นจากปริมาตรจะ **ดับทันที** → ปัสสาวะจางจำนวนมาก (water diuresis) → Na พุ่ง · KCl ที่ให้ก็เพิ่ม Na (K เข้าเซลล์แลก Na ออก) · ผู้ป่วยมี K ต่ำ ขาดอาหาร = **เสี่ยง ODS สูง** → เป้าเพิ่ม Na ≤ 8 (ไม่เกิน 10) mmol/L ใน 24 ชม. (European 2014 / US 2013) · ตรวจ Na ทุก 4–6 ชม. วัดปัสสาวะทุกชั่วโมง ถ้าปัสสาวะจางออกมากและ Na ขึ้นเร็ว → ให้ D5W ทดแทน ± desmopressin"""},
  {"q": "5. ระหว่างให้สารน้ำวันที่ 2 ผู้ป่วยชารอบปาก มือจีบเมื่อวัดความดัน · total Ca 8.9 mg/dL · albumin 4.0 · Mg 1.1 mg/dL · K 2.9 แม้ได้ KCl ไปมาก — อธิบายกลไกทั้งหมด (4 คะแนน)",
   "a": """**Trousseau sign บวก** = เส้นประสาทไวเกิน
- **alkalemia** → albumin ปล่อย H แล้วจับ Ca มากขึ้น → **ionized Ca ลด** ทั้งที่ total Ca เกือบปกติ → threshold ของ voltage-gated Na channel ต่ำลง → tetany (สไลด์ Calcium)
- **Mg ต่ำ** (ขาดอาหาร อาเจียน) → ทำให้ tetany ได้เอง และกดการหลั่ง/ฤทธิ์ PTH
- **K ไม่ขึ้นเพราะ Mg ต่ำ**: Mg ในเซลล์ปกติอุด ROMK — Mg ต่ำ ROMK เปิดตลอด → K รั่วทางไตต่อเนื่อง (สไลด์ factor 2)
→ ให้ **MgSO4** ก่อน/พร้อม KCl · แก้ alkalosis · ถ้า ionized Ca ต่ำจริงและมีอาการ ให้ Ca gluconate"""}],
 "ref": ["สไลด์ Renal Physiology II — Types of volume deficit · ADH · Factors affecting tubular K secretion · Factors affecting HCO3 reabsorption · Metabolic alkalosis · Calcium",
         "European hyponatraemia guideline 2014 · Verbalis Am J Med 2013 · Guyton & Hall 14th ed · Boron & Boulpaep 3rd ed"],
 "nl": [AB_B, LYTE, LYTE_B, VOMIT, HANDLE_B, FLUID_B, HYPOVOL_B, FLUIDDRUG_B],
 "years": [], "_kind": "meq", "_set": "nephro"}]

OSCE = [{"id": "NEPH-PHY2-OSCE-01", "part": "OSCE/SAQ", "lec": LEC, "lecture": LECNAME,
 "topic": "Data interpretation station – Stepwise acid–base interpretation (3 cases)",
 "station": "สถานีแปลผล 8 นาที (ผู้คุมสอบให้ผลทีละชุด นักศึกษาอธิบายด้วยวาจา)",
 "instruction": """**งานของนักศึกษา**: แปลผลกรด-ด่างทีละขั้นทั้ง 3 ชุด — บอก primary disorder · คำนวณการชดเชยที่คาดและบอกว่าเหมาะสมหรือไม่ · คำนวณ anion gap (และค่าอื่นที่จำเป็น) · บอกสาเหตุที่เข้ากับข้อมูลและกลไก 1 ประโยค

**ชุด A** — หญิง 20 ปี เบาหวานชนิดที่ 1 หายใจหอบลึก: pH 7.23 · PaCO2 22 mmHg · HCO3 9 · Na 134 · Cl 98 mEq/L · albumin 4.0 g/dL · glucose 450 mg/dL
**ชุด B** — ชาย 45 ปี ท้องเสียเป็นน้ำ 5 วัน: pH 7.29 · PaCO2 30 mmHg · HCO3 14 · Na 138 · Cl 114 mEq/L · albumin 4.0 g/dL · ปัสสาวะ Na 30 · K 25 · Cl 80 mEq/L
**ชุด C** — ชาย 70 ปี COPD ใช้ O2 ที่บ้าน อาการคงที่: pH 7.34 · PaCO2 62 mmHg · HCO3 32 · Na 140 · Cl 96 mEq/L""",
 "answer": """**เกณฑ์ให้คะแนน (20 คะแนน)**

| ชุด | สิ่งที่ต้องพูด/คำนวณ | คะแนน |
|---|---|---|
| ทุกชุด | เริ่มจาก pH → ตัวหลัก → การชดเชย → AG อย่างเป็นระบบ (บอกค่าปกติ pH 7.40 · PaCO2 40 · HCO3 24) | 2 |
| A | acidemia + HCO3 ต่ำ = **metabolic acidosis** | 1 |
| A | Winter: 1.5 × 9 + 8 = **21.5 ± 2** → PaCO2 22 = ชดเชยเหมาะสม | 2 |
| A | AG = 134 − (98 + 9) = **27** → high AG · delta ratio = (27 − 12) ÷ (24 − 9) = **1.0** → HAGMA อย่างเดียว | 2 |
| A | สาเหตุ **DKA** · หายใจหอบลึก = Kussmaul (H กระตุ้น chemoreceptor → VT ↑) | 1 |
| B | **metabolic acidosis** · Winter 1.5 × 14 + 8 = **29 ± 2** → PaCO2 30 เหมาะสม | 2 |
| B | AG = 138 − (114 + 14) = **10** → normal AG (hyperchloremic) | 2 |
| B | urine AG = 30 + 25 − 80 = **−25 (ลบ)** → ไตขับ NH4 ได้ดี = เสีย HCO3 ทางลำไส้ ไม่ใช่ RTA | 2 |
| C | acidemia + PaCO2 สูง = **respiratory acidosis** | 1 |
| C | ΔPaCO2 22 → HCO3 คาด acute ~26 · chronic 24 + 4 × 2.2 = **~33** → 32 = **chronic ชดเชยโดยไต** | 2 |
| C | AG = 140 − (96 + 32) = 12 ปกติ · ไม่ต้องให้ bicarbonate | 1 |
| สื่อสาร | ใช้ HCO3 จาก electrolyte (TCO2) · สรุปเป็นประโยคเดียวต่อชุด · เป็นระบบ ไม่เดา | 2 |

**Critical errors**: ใช้สูตรการชดเชยผิดภาวะ · สรุปว่าชุด C เป็น "acute respiratory failure ต้องใส่ท่อทันที" โดยไม่ประเมินว่าเรื้อรัง · บอกว่าชุด B เป็น RTA ทั้งที่ urine AG ลบ

**คำถามต่อจากผู้คุมสอบ**: "ถ้าชุด B มี albumin 2.0 g/dL" → corrected AG = 10 + 2.5 × 2 = **15** → มี high AG acidosis ซ่อน (เช่น lactic จากขาดน้ำ) · "ชุด A ถ้า PaCO2 เป็น 30" → สูงกว่า 23.5 = **respiratory acidosis ร่วม** (เหนื่อยล้า/ปอดอักเสบ) อันตราย · "ทำไมชุด C ห้ามให้ O2 ความเข้มข้นสูงเกิน" → hypoxic drive และ V/Q แย่ลง → CO2 คั่ง (สไลด์: O2 therapy เป็นสาเหตุ respiratory acidosis)""",
 "ref": ["สไลด์ Renal Physiology II — Stepwise approach · Anion gap · Wide/Normal AG metabolic acidosis · Primary disturbance and compensatory response",
         "Berend K et al. NEJM 2014;371:1434–45 · ชุดสูตรเดียวกับคาบ chest 26 ABG"],
 "nl": [AB_B, ABG, ABG_B, DM, DIARR, COPD, RTA],
 "years": [], "_kind": "meq", "_set": "nephro"}]
LECTURE = {
 "lec": LEC, "date": "พื้นฐานสรีรวิทยา (ปรีคลินิก)",
 "title": "สรีรวิทยาไตพื้นฐาน II — สมดุลน้ำ อิเล็กโทรไลต์ กรด-ด่าง และการถ่ายปัสสาวะ",
 "subtitle": "Darrow–Yannet · glomerulotubular balance · RAAS/ADH/ANP · K shift และการขับ K · Ca Pi Mg · buffer ปอด ไต · HCO3 reclamation, TA, NH4 · การชดเชย · anion gap · micturition reflex — พร้อมสะพานสู่คลินิก (SIADH, ODS, DKA, อาเจียน, RTA, incontinence)",
 "objectives": [
   "อธิบายการเคลื่อนของน้ำระหว่าง ICF/ECF ด้วย tonicity และแยก plasma osmolality กับ effective osmolality",
   "จัดภาวะปริมาตรผิดปกติ 6 แบบด้วย Darrow–Yannet และเลือกสารน้ำที่สอดคล้อง",
   "อธิบายว่าไตคุมการขับ Na ด้วย glomerulotubular balance, sympathetic, RAAS และ ANP อย่างไร",
   "อธิบายการหลั่งและกลไกของ ADH (V2R–AQP2) การกระหายน้ำ และใช้อธิบาย DI, SIADH และ osmotic demyelination",
   "อธิบายการคุม K ทั้ง shift และการขับที่ principal cell พร้อมผลต่อกล้ามเนื้อและ ECG",
   "อธิบายรูปแบบของ Ca Pi Mg ในพลาสมา ผลต่อ threshold ของเส้นประสาท และการดูดกลับในแต่ละส่วนของ nephron",
   "อธิบายแหล่งกรด buffer การชดเชยทางปอด และการเก็บ/สร้าง HCO3 การขับ titratable acid และ NH4 ของไต",
   "แปลผลกรด-ด่างทีละขั้น (การชดเชย anion gap delta ratio osmolal gap urine AG) และอธิบายกลไกของ Kussmaul, paradoxical aciduria และ RTA",
   "อธิบายวงจรควบคุมการถ่ายปัสสาวะ และทำนายชนิดของ incontinence จากตำแหน่งรอยโรค"],
 "nlGap": "เกณฑ์ฯ มีรหัสสรีรวิทยาไตครบ (`B9.1.2(1)` body fluid · `B9.1.2(4)` renal handling of Na K Ca Mg Pi · `B9.1.2(6)` acid-base · `B9.1.2(7)` micturition) และรหัสโรค (`2.3.4(2)` fluid/electrolyte/acid-base · SIADH `2.3.4-3(5)` · RTA `2.3.14-3(12)` · hyperkalemia `2.2.15` · incontinence `2.1.46`) แต่ **ไม่มีรหัสเฉพาะของ osmotic demyelination, contraction alkalosis, toxic alcohol/osmolal gap และ detrusor–sphincter dyssynergia** → ใช้รหัสกลุ่มที่ใกล้ที่สุด และอิงตำรา/แนวทางในรายการด้านล่าง",
 "guidelines": [
   "**สไลด์ Lec 8–12 Renal Physiology Part II (Watchara Chongsa, PhD · MDS215)** — เนื้อหาหลักทุกหัวข้อ (สไลด์อ้าง Berne & Levy Physiology 7th ed 2018 · Boron & Boulpaep Medical Physiology 3rd ed · Costanzo Table 6.2 · Sherwood)",
   "**Guyton & Hall Textbook of Medical Physiology 14th ed (2021)** — urine volume กับ solute load, การตอบสนองแบบบูรณาการ, aldosterone escape (เติมในหัวข้อ 3–6)",
   "**Boron & Boulpaep Medical Physiology 3rd ed** — ระบบ HCO3 แบบเปิด, ammoniagenesis, RTA, thiazide กับ Ca (หัวข้อ 10–12)",
   "**Spasovski G et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol 2014;170:G1–G47** — ขีดจำกัดการแก้ Na และ 3% NaCl 150 mL (หัวข้อ 7, MEQ)",
   "**Verbalis JG et al. Diagnosis, evaluation, and treatment of hyponatremia: expert panel recommendations. Am J Med 2013;126(10 Suppl 1):S1–S42** — กลุ่มเสี่ยง ODS สูง",
   "**Berend K, de Vries APJ, Gans ROB. Physiological approach to assessment of acid–base disturbances. N Engl J Med 2014;371:1434–45** — สูตรการชดเชย delta ratio osmolal gap urine AG (หัวข้อ 14, OSCE)",
   "**ADA consensus report: Hyperglycemic crises in adults with diabetes (Diabetes Care 2024)** — K ใน DKA (หัวข้อ 13)",
   "**International Continence Society (ICS) standardisation of terminology** — ชนิดของ incontinence (หัวข้อ 15)"],
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
MOCK_MAP = {"nephro-phy2-07": ["MOCK-170"], "nephro-phy2-08": ["MOCK-173"], "nephro-phy2-10": ["MOCK-198"], "nephro-phy2-12": ["MOCK-180"], "nephro-phy2-13": ["MOCK-135"]}
nmock = link_mock(SET, LEC, MOCK_MAP) if MOCK_MAP else 0

from collections import Counter
newi = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-PHY2")]
print("sections %d | ข้อใหม่ %d | mock %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), len(newi), nmock, len(L["meq"]), len(L["osce"]), sum(len(s.get("figs") or {}) for s in S), len(codes)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for i in newi).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
