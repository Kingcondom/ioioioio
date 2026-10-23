#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สรีรวิทยาไตพื้นฐาน I (Watchara Chongsa, PhD · Physiology Unit, Rangsit University · MDS215 ปรีคลินิก) → data/nephro.json
ต้นฉบับ: Drive 1IHnFaFvZeNbKXeE_RRpnwHLTP6zEEYwO "Lec 4-7 Renal Physiology_Part I.pdf" (24.9 MB · อ่านเฉพาะข้อความ — ภาพในสไลด์อ่านไม่ได้)
โน้ตสไลด์: slides/renal_physio1_notes.md · ภาพประกอบ: figs_renalphys1.py (21 ภาพ)
lec = "Physio1" (คาบพื้นฐาน ไม่มีในคลัง Ward Drill) · แทรกที่ index 0 ของ nephro.json (ก่อนคาบ 05) — ไม่ sort คาบอื่น
สไลด์มี: หน้าที่ของไต · RBF + การควบคุม · clearance/PAH · renal nerve · filtration barrier · Starling/GFR · eGFR (สมการเป็นภาพ) ·
autoregulation · FF · glomerulotubular balance · PT/loop/DT/CD transport + ยาขับปัสสาวะ + tubular defect · organic secretion · FE ·
concentrating/diluting · Cosm/CH2O
สไลด์ไม่มี (เติมจาก Guyton & Hall 14th / Boron & Boulpaep 3rd / KDIGO และระบุในบทเรียน): กลไกโมเลกุลของ TGF · SGLT2 inhibitor ·
splay · triple whammy · creatinine secretion/trimethoprim · sCr–GFR hyperbola · CKD-EPI 2021 · FEurea · hypoK–alkalosis · Bartter types
Part II (body fluid, volume/osmolality balance, K Ca Mg Pi balance, acid–base, micturition) ทำโดย session อื่น — อ้างถึงสั้น ๆ เท่านั้น
คลัง Ward Drill: ไม่มีคาบนี้ในคลัง · ผูกเฉพาะข้อ Mock ที่ยังว่างและตรงเรื่อง (MOCK-179 165 169 181 147) ·
ไม่ผูกข้อของคาบ 19/22/28/42 · MOCK-170/173/180 (Na K กรด–ด่าง) เว้นไว้ให้ Part II"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
import figs_renalphys1 as F

SET, LEC = "nephro", "Physio1"
SRC = "สไลด์ Watchara Chongsa PhD — Renal Physiology Part I (MDS215)"
SRC_ADD = "สไลด์ + ตำรา Guyton & Hall 14th / Boron & Boulpaep 3rd (ส่วนที่เติมระบุในเนื้อหา)"
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
N = lambda n: "NEPH-PHY1-MCQ-%02d" % n
R = lambda p, *g: ["สไลด์ Renal Physiology I — " + p] + list(g)
GH = "Guyton & Hall Textbook of Medical Physiology 14th ed"
BB = "Boron & Boulpaep Medical Physiology 3rd ed"

# รหัส นล.
STRUCT, INNV, CIRC = "B9.1.1(1)", "B9.1.1(3)", "B7.1.1(5)"
FLUID, GFRH, TUB, HANDL, CONC, ACIDB, HORM, METAB = ("B9.1.2(1)", "B9.1.2(2)", "B9.1.2(3)", "B9.1.2(4)",
                                                    "B9.1.2(5)", "B9.1.2(6)", "B9.1.2(8)", "B9.1.2(9)")
RFT, OSM, LYTE_LAB, UAS, UA = "B9.3(4)", "B9.3(3)", "B9.3(5)", "B9.3(2)", "3.1.6"
DIUR, FLUIDRX = "B9.4(1)", "B9.4(2)"
AKI, AKI_B, CKD_B = "2.3.14(3)", "B9.2.7(1)", "B9.2.7(2)"
LYTE, LYTE_B, HYPERK = "2.3.4(2)", "B9.2.5(2)", "2.2.15"
OLIG, POLY, OLIG_B, ANURIA = "2.1.44", "2.1.42", "B9.2.5(1)", "2.2.28"
EDEMA, HEMAT = "2.1.39", "2.1.43"
NEPHROTIC, NEPHROTIC_B = "2.3.14(12)", "B9.2.2(4)"
RAS, RAS_B, RTA = "2.3.14-3(13)", "B9.2.6-3(1)", "2.3.14-3(12)"
DM, DM_B, DMDRUG = "2.3.4(1)", "B11.2.5(4)", "B11.4(1)"
HT, HT_B, HF = "2.3.9(4)", "B7.2.5(1)", "2.3.9(5)"
SHOCK, SHOCK_B, HYPOVOL = "2.2.7", "B7.2.5(4)", "B7.1.2(5)"
NSAID, RAASD, AUTON = "B5.4(1)", "B7.4(2)", "B1.7.5"
PK, PKSP, ADR, ADRDRUG = "B1.7.1(1)", "B1.7.1(3)", "B1.7.1(4)", "2.3.19(2)"
GOUT, URIC = "2.3.13(2)", "B5.3(4)"
EPO, CAPTH = "B2.4(4)", "B11.1.2(2)e"
DI, DI_B, SIADH, SIADH_B = "2.3.4-3(4)", "B11.2.5-3(6)", "2.3.4-3(5)", "B11.2.5-3(11)"
CIRRH = "2.3.11(4)"

# ═════════════════════════════════════════════ 1
sec("nephro-phy1-01", "หน้าที่ 7 ข้อของไต — และอาการที่เกิดเมื่อหน้าที่นั้นหายไป",
    "ขับของเสีย/ยา · เกลือแร่ · น้ำ · ต่อมไร้ท่อ (renin EPO calcitriol PG) · กรด–ด่าง · gluconeogenesis", 9,
"""### คาบนี้คืออะไร
คาบปรีคลินิกของ อ. Watchara Chongsa (MDS215) — **Part I: หน้าที่ของไตและกระบวนการพื้นฐานของการสร้างปัสสาวะ** ปูพื้นให้ทุกคาบ nephro ที่ตามมา (AKI, CKD, glomerular disease, electrolyte) เพราะอาการทางคลินิกเกือบทั้งหมดอธิบายได้ด้วยกลไกในคาบนี้
- Part I (คาบนี้): หน้าที่ของไต · RBF · GFR · autoregulation · FF · การขนส่งในท่อไตแต่ละส่วน + ยาขับปัสสาวะ + โรคของท่อไต · organic secretion · FE · การทำปัสสาวะเข้มข้น/เจือจาง
- Part II (อีกบทเรียน): การกระจายน้ำในร่างกาย การคุมปริมาตรและ osmolality การคุม K Ca Mg Pi กรด–ด่าง และ micturition

> เนื้อหาหลักมาจากข้อความในสไลด์ · ภาพในสไลด์ (แผนภาพเซลล์ ภาพ countercurrent สมการ eGFR) อ่านไม่ได้ จึงวาดใหม่ตามป้ายในสไลด์และตำรา **Guyton & Hall 14th / Boron & Boulpaep 3rd** · ทุกจุดที่เติมจากตำราจะเขียนว่า "(ตำรา)" กำกับ

### หน้าที่ 7 ข้อ — สไลด์สอนคู่กับ "Decreased renal function"
[[fig:functions]]
| หน้าที่ | รายละเอียดในสไลด์ | เมื่อไตเสีย → อาการ |
|---|---|---|
| 1. ขับของเสียไนโตรเจน | **creatinine** (จาก creatine ในกล้ามเนื้อ) · **urea** (จาก amino acid) · **uric acid** (จาก purine) | sCr และ BUN สูง (**azotemia**) → คลื่นไส้ อาเจียน อ่อนเพลีย ตะคริว (uremic symptoms) · uric acid สูง → ผลึกในข้อ → **gout** |
| 2. ขับสารแปลกปลอมและยา | กรอง + หลั่งที่ท่อไต (หัวข้อ 13) | renal drug clearance ลด → ระดับยาสูง → **พิษจากยา** |
| 3. สมดุลเกลือแร่ | ขับ Na K Mg Pi ส่วนเกินจากอาหาร · **เก็บ Ca** ที่มักเสียไปทุกวัน | Na คั่ง → น้ำคั่ง → **ความดันสูง บวม** · K สูง → **หัวใจเต้นผิดจังหวะ** · Pi สูง |
| 4. สมดุลน้ำและ osmolality | ขับน้ำเมื่อเกิน เก็บน้ำเมื่อขาด | ขับน้ำเกินไม่ได้ → บวม ความดันสูง |
| 5. ต่อมไร้ท่อ | **renin** (RAAS → คุมความดัน) · **erythropoietin** · **1α-hydroxylase** · PGI₂/PGE₂ และ kinin (ขยายหลอดเลือดเฉพาะที่) | ดูตารางถัดไป |
| 6. สมดุลกรด–ด่าง | หลั่ง H⁺ · ดูดกลับและสร้าง HCO₃⁻ | กรดคั่ง → **metabolic acidosis** |
| 7. Gluconeogenesis | จาก glutamine ในเซลล์ PT (ขั้นตอนเดียวกับการสร้าง NH₄⁺/HCO₃⁻ ใหม่) | — |

#### ทำไมถึงมีอาการนี้ — ต่อมไร้ท่อของไต
| ฮอร์โมน | สร้างที่ / ตัวกระตุ้น | ไตเสีย → กลไก → อาการ |
|---|---|---|
| **Erythropoietin** | **interstitial fibroblast** ใน peritubular capillary bed ของ cortex และ outer medulla · กระตุ้นด้วย **PaO₂ ในเนื้อไตต่ำ** (hypoxemia หรือเลือดเข้าไตน้อย) | fibroblast ถูกแทนด้วยพังผืด → EPO ↓ → ไขกระดูกสร้าง RBC ↓ → Hct ↓ → **ซีด เหนื่อยง่าย** (normocytic anemia ของ CKD) |
| **1α-hydroxylase** | ในเซลล์ **proximal tubule**: 25(OH)D₃ → **1,25(OH)₂D₃ (calcitriol)** | calcitriol ↓ → ดูดซึม Ca จากลำไส้ ↓ + ไตดูดกลับ Ca ↓ → **Ca ต่ำ** → **PTH ↑** → สลายกระดูก → **renal osteodystrophy** (บวกกับ Pi คั่ง) |
| **Renin** | JG cell (หัวข้อ 2) | ไตที่ขาดเลือดหลั่ง renin มาก → ความดันสูง (renovascular) |
| **PGI₂ · PGE₂ · kinin** | ในไตเอง ขยาย afferent | เป็นตัวพยุงเลือดเข้าไตเมื่อขาดเลือด — NSAID ตัดออก (หัวข้อ 6) |

### เส้นทางของปัสสาวะ (Overview)
เลือด → renal artery → **nephron** (พลาสมา → ปัสสาวะ) → renal pelvis → ureter → bladder → urethra → ออกนอกร่างกาย
- ทุกขั้นที่ nephron ทำมี 3 อย่าง: **กรอง (filtration) · ดูดกลับ (reabsorption) · หลั่ง (secretion)** — หัวข้อ 3–14 ไล่ทีละขั้น
""",
    ["จำหน้าที่ของไตคู่กับ \"ไตเสียแล้วเป็นอะไร\" — อาการ CKD เดาได้ทั้งหมด",
     "EPO สร้างจาก interstitial fibroblast (ไม่ใช่ tubular cell) ตอบสนองต่อ PaO₂ ในเนื้อไตต่ำ",
     "1α-hydroxylase อยู่ใน PT → CKD: calcitriol ↓ → Ca ↓ → PTH ↑ → renal osteodystrophy",
     "ไตเก็บ Ca แต่ขับ Na K Mg Pi ส่วนเกิน — ไตเสียจึงได้ K สูง Pi สูง Ca ต่ำ",
     "ไตสร้างกลูโคสจาก glutamine ใน PT ได้ (gluconeogenesis)"],
    [mcq(N(1), "A 58-year-old man with CKD stage 4 (eGFR 22 mL/min/1.73 m²) has fatigue and pallor. Hb is 8.6 g/dL with normal MCV, ferritin and transferrin saturation are adequate, and reticulocytes are low. Loss of which renal cell population best explains his anaemia?",
         ["Juxtaglomerular cells of the afferent arteriole", "Proximal tubular epithelial cells that express 1α-hydroxylase",
          "Peritubular interstitial fibroblasts of the cortex and outer medulla", "Macula densa cells of the thick ascending limb", "Glomerular podocytes"], 2,
         "anemia ของ CKD เป็น normocytic · reticulocyte ต่ำ (ไขกระดูกไม่ถูกกระตุ้น) · เหล็กพอ → ขาด **erythropoietin** ซึ่งสไลด์บอกว่าสร้างโดย **interstitial fibroblast ใน peritubular capillary bed ของ cortex และ outer medulla** เมื่อ PaO₂ ในเนื้อไตต่ำ · CKD → fibroblast กลายเป็น myofibroblast/พังผืด → EPO ไม่พอ\n\n"
         "- **JG cell** — สร้าง renin ไม่เกี่ยวกับ RBC\n- **PT cell (1α-hydroxylase)** — สร้าง calcitriol → ผลคือ Ca ต่ำ/PTH สูง ไม่ใช่ซีด\n"
         "- **Macula densa** — รับรู้ NaCl เพื่อ TGF และ renin\n- **Podocyte** — ชั้นกรอง เสียแล้วเกิด proteinuria",
         "EPO = peritubular interstitial fibroblast ตอบ PaO₂ ต่ำ", "Renal endocrine function — erythropoietin", R("Renal function 5.2 Erythropoietin"), [HORM, EPO, CKD_B, AKI]),
     mcq(N(2), "A 66-year-old woman with long-standing diabetic kidney disease (eGFR 12 mL/min/1.73 m²) is reviewed before starting dialysis. Which set of plasma findings is most consistent with loss of the kidney's excretory and endocrine functions?",
         ["K⁺ low, phosphate low, Ca²⁺ high, HCO₃⁻ high", "K⁺ high, phosphate high, Ca²⁺ low, HCO₃⁻ low",
          "K⁺ high, phosphate low, Ca²⁺ high, HCO₃⁻ high", "K⁺ normal, phosphate normal, Ca²⁺ normal, HCO₃⁻ normal because of adaptation",
          "K⁺ low, phosphate high, Ca²⁺ high, HCO₃⁻ low"], 1,
         "ไล่หน้าที่ทีละข้อตามสไลด์: ขับ K ไม่ได้ → **K สูง** · ขับ Pi ไม่ได้ → **Pi สูง** · 1α-hydroxylase ↓ → calcitriol ↓ → **Ca ต่ำ** (→ PTH สูง) · หลั่ง H⁺/สร้าง HCO₃⁻ ไม่ได้ → **HCO₃⁻ ต่ำ** (metabolic acidosis)\n\n"
         "- **K ต่ำ Pi ต่ำ Ca สูง HCO₃⁻ สูง** — กลับด้านทั้งหมด\n- **K สูง Pi ต่ำ Ca สูง** — Pi และ Ca ผิดทาง\n"
         "- **ปกติทั้งหมดจากการปรับตัว** — การปรับตัว (nephron ที่เหลือทำงานหนักขึ้น) ช่วยได้ในระยะต้น แต่ที่ eGFR 12 ไม่พอแล้ว\n- **K ต่ำ** — ไม่ใช่ลักษณะของไตวายระยะท้าย",
         "ไตวาย: K ↑ Pi ↑ Ca ↓ HCO₃⁻ ↓", "Consequences of loss of renal function", R("Renal function 1–6 · Decreased renal function"), [HORM, HANDL, CKD_B, LYTE, HYPERK])],
    [HORM, HANDL, METAB, STRUCT, CKD_B, AKI, GOUT, EPO, CAPTH], {"functions": F.functions()})

# ═════════════════════════════════════════════ 2
sec("nephro-phy1-02", "เลือดไปเลี้ยงไต (RBF) — afferent vs efferent, sympathetic และ renin",
    "RBF 20% ของ CO · ความต้านทานที่ arteriole · สารหด/ขยายแต่ละเส้น · RAAS 3 ทางกระตุ้น renin · renal nerve", 11,
"""### ตัวเลขที่ต้องจำ
- ไตหนักราว 0.5% ของน้ำหนักตัว แต่รับเลือด **20% ของ cardio output** ขณะพัก → **RBF ~1–1.2 L/min** (สไลด์ช่วงหลังใช้ 1.2–1.3 L/min)
- เลือดมากขนาดนี้ไม่ใช่เพื่อออกซิเจน แต่เพื่อ **กรอง** — ไตใช้ O₂ ไปกับการขนส่ง Na⁺ เป็นหลัก (ตำรา)
- **RBF = ความดัน ÷ ความต้านทาน** ความต้านทานส่วนใหญ่อยู่ที่ **afferent และ efferent arteriole** → ขนาดของสองเส้นนี้คุมทั้ง RBF และ GFR

### สารที่ทำให้ arteriole หด/ขยาย (สไลด์ Vasoactive substances)
[[fig:arterioles]]
| สาร | ทำอะไร | RBF |
|---|---|---|
| NE, E (α1-AR) · ATP (P2X) · adenosine (A1R) | **afferent หด** (major site) | ↓ |
| endothelin · thromboxane A₂ · ADH · dopamine ขนาดสูง | afferent + efferent หด | ↓ |
| **angiotensin II** | **efferent หด** — efferent ไวกว่า afferent | ↓ |
| nitric oxide · dopamine ขนาดต่ำ | afferent + efferent ขยาย | ↑ |
| **PGI₂ · PGE₂** · ANP · bradykinin · kinin | **afferent ขยาย** (major site) | ↑ |

### 1. Sympathetic — ยิ่งกระตุ้นแรง ยิ่งยอม "ตัดไต"
- เส้นประสาทจาก celiac plexus เลี้ยงตั้งแต่ interlobar artery จนถึง efferent แต่ **afferent มีเส้นประสาทและ α1-receptor มากที่สุด**
- ปริมาตร/ความดันลด ออกกำลัง กลัว สู้ → sympathetic ↑ → **afferent หด** → RBF ↓ (เลือดไปอวัยวะอื่นแทน)
- ความแรงของผล (สไลด์): ปกติ → แทบไม่มีผล · กระตุ้นเล็กน้อย–ปานกลาง → ผลน้อยเพราะ autoregulation ชดเชย · **กระตุ้นรุนแรงเฉียบพลัน** (shock, เสียเลือด) → RBF ลดเหลือ **10–30%** ของปกติ

#### NE ทำอะไรกับไตบ้าง (สไลด์ Renal nerve supply)
| ตำแหน่ง | receptor | ผล |
|---|---|---|
| กล้ามเนื้อเรียบหลอดเลือด | α1 | afferent หด → RBF ↓ GFR ↓ |
| endothelium และ mesangial cell | α1 | ปล่อย **PGE₂/PGI₂** → ขยาย (ถ่วงดุลไม่ให้หดเกิน) |
| JG cell | **β1** | **renin ↑** → AII → efferent หด |
| mesangial cell | α1 | หดตัว → พื้นที่กรองลด → Kf ↓ GFR ↓ |
| เซลล์ท่อไต (PT, TAL, DT, CD) | α1 | **ดูดกลับ Na⁺ ↑** |
- เส้นประสาทเดียวกันปล่อย dopamine ร่วมด้วย ถ่วงดุลผลของ NE

### 2. Renin–angiotensin–aldosterone
angiotensinogen (ตับ) → **renin (ไต)** → AI → **ACE (ปอด)** → **AII** → หลอดเลือดหด RBF ↓
[[fig:renin]]
| ทางกระตุ้น renin | สัญญาณ | ตัวอย่างในสไลด์ |
|---|---|---|
| ① sympathetic (β1-AR ที่ JG cell) | baroreceptor/volume receptor รับรู้ว่าปริมาตรลด | hypovolemia, hypotension, ออกกำลัง กลัว |
| ② renal baroreceptor | ความดันใน afferent ลด → **JG cell ถูกยืดน้อยลง** | hypovolemia, **renal artery stenosis** |
| ③ macula densa | **NaCl ที่ไหลมาถึงลดลง** | GFR ลด (glomerular disease, hypovolemia) · ถูกดูดกลับไปก่อนที่ PT/loop มาก (**กลูโคสหรือกรดอะมิโนในเลือดสูง** — Na⁺ ถูกดูดคู่กับมันที่ PT) |
| ยับยั้ง | **ANP** | หัวใจห้องบนถูกยืด (ปริมาตรเกิน) |

#### ทำไมถึงมีอาการนี้ — renal artery stenosis ทำให้ความดันสูง
หลอดเลือดแดงไตตีบ → ความดันหลังจุดตีบต่ำ → JG cell ถูกยืดน้อย (ทาง ②) → renin ↑ → AII ↑ → หลอดเลือดทั้งตัวหด + aldosterone เก็บ Na → **ความดันสูงที่คุมยาก** · ในไตข้างนั้น AII ที่หด efferent คือสิ่งที่พยุง GFR ไว้ → ให้ ACEi/ARB แล้ว GFR ตก (หัวข้อ 6)
""",
    ["RBF ~20% CO (~1–1.2 L/min) · ความต้านทานหลักอยู่ที่ afferent/efferent",
     "Afferent: หดด้วย NE/adenosine · ขยายด้วย PG/ANP — efferent: หดด้วย AII (ไวกว่า afferent)",
     "Sympathetic รุนแรงเฉียบพลัน → RBF เหลือ 10–30% · β1 ที่ JG cell → renin",
     "Renin 3 ทาง: sympathetic β1 · ความดัน afferent ต่ำ · NaCl ถึง macula densa ต่ำ — ANP ยับยั้ง",
     "Renal artery stenosis: JG cell ยืดน้อย → renin ↑ → ความดันสูง"],
    [mcq(N(3), "A 24-year-old man is brought in after a motorcycle crash with BP 72/40 mmHg and heart rate 140/min. His urine output over the first 2 hours is 8 mL. Which mechanism contributes most to the abrupt fall in his renal blood flow?",
         ["Norepinephrine acting on α1-adrenergic receptors causing afferent arteriolar constriction",
          "Angiotensin II acting mainly on the afferent arteriole", "Prostaglandin E₂ release causing efferent arteriolar constriction",
          "Atrial natriuretic peptide causing afferent constriction", "Low-dose dopamine release causing generalized renal vasoconstriction"], 0,
         "เสียเลือดมาก (shock) → **sympathetic กระตุ้นรุนแรงเฉียบพลัน** → NE จับ **α1 ที่ afferent** (ตำแหน่งที่มีเส้นประสาทและ α1 มากที่สุด) → afferent หด → RBF ลดได้ถึง **10–30%** ของปกติ (สไลด์) → GFR ตก ปัสสาวะออกน้อย · ไตยอมเสียเลือดให้หัวใจและสมอง\n\n"
         "- **AII ที่ afferent** — AII หด **efferent** เป็นหลัก (efferent ไวกว่า)\n- **PGE₂** — ขยาย afferent ถ่วงดุล NE ไม่ได้ทำให้หด\n"
         "- **ANP** — ขยาย afferent และยับยั้ง renin\n- **dopamine ขนาดต่ำ** — ขยายทั้งสองเส้น",
         "Shock: NE → α1 afferent หด → RBF เหลือ 10–30%", "Sympathetic control of RBF", R("Factors affecting RBF · Renal nerve supply"), [GFRH, CIRC, SHOCK, SHOCK_B, AUTON, OLIG]),
     mcq(N(4), "A 70-year-old smoker has resistant hypertension, a left renal artery stenosis of 85% on CT angiography and an elevated plasma renin activity. Which signal at the juxtaglomerular apparatus of the left kidney is primarily responsible for the increased renin secretion?",
         ["Increased NaCl delivery to the macula densa", "Decreased stretch of the juxtaglomerular cells due to low afferent arteriolar pressure",
          "Increased atrial natriuretic peptide", "β1-adrenergic blockade by the patient's medication", "Increased glomerular filtration rate in the stenotic kidney"], 1,
         "หลังจุดตีบความดันใน afferent ต่ำ → **JG cell ถูกยืดน้อยลง** (intrarenal/renal baroreceptor) → หลั่ง renin มาก — สไลด์ยก **renal artery stenosis** เป็นตัวอย่างของทางนี้ · AII ที่เพิ่มขึ้นทำให้ความดันทั้งตัวสูง\n\n"
         "- **NaCl ถึง macula densa เพิ่ม** — จะ **ลด** renin (ไตข้างตีบ GFR ลด NaCl ถึงน้อยลงต่างหาก)\n- **ANP** — ยับยั้ง renin\n"
         "- **β1 blockade** — ลด renin\n- **GFR เพิ่ม** — ไตข้างตีบ GFR ไม่เพิ่ม",
         "RAS: ความดัน afferent ต่ำ → JG cell ยืดน้อย → renin ↑", "Renin secretion — renal baroreceptor", R("RAA system · Mechanisms activating renin secretion"), [GFRH, HORM, RAS, RAS_B, HT, HT_B])],
    [GFRH, CIRC, INNV, HORM, SHOCK, RAS, HT], {"arterioles": F.arterioles(), "renin": F.renin()})

# ═════════════════════════════════════════════ 3
sec("nephro-phy1-03", "Clearance — วัด RPF, RBF และ GFR ด้วยสารตัวเดียว",
    "C = UV/P · PAH → ERPF 630 · RPF 700 · RBF · inulin = gold standard · creatinine clearance · sCr–GFR hyperbola · eGFR", 11,
"""### Clearance คืออะไร
**Clearance ของสาร A** = ปริมาตรพลาสมาที่ถูก \"ล้าง\" สาร A ออกจนหมดต่อหน่วยเวลา (mL/min)
- หลัก: ปริมาณสารในปัสสาวะต่อนาที (U × V) ต้องถูก \"ขน\" มาด้วยพลาสมาจำนวนหนึ่ง — หารด้วยความเข้มข้นในพลาสมา (P) ก็ได้ปริมาตรพลาสมานั้น
- ตัวอย่างในสไลด์: ถ้าพลาสมา 1 mL มีสาร A 1 หน่วย และพบในปัสสาวะ 5 หน่วย → ใช้พลาสมา 5 mL ขนมา → clearance = 5 mL/min

| สัญลักษณ์ | ความหมาย |
|---|---|
| **C_A = (U_A × V) / P_A** | mL/min |
| U_A | ความเข้มข้นในปัสสาวะ (mg/mL หรือ mg/dL) |
| V | อัตราการไหลของปัสสาวะ (mL/min) |
| P_A | ความเข้มข้นในพลาสมา (หน่วยเดียวกับ U) |

### วัดเลือดเข้าไตด้วย PAH (para-aminohippuric acid)
สารที่จะใช้วัด RPF ต้อง **กรองได้เสรีและถูกหลั่งออกเกือบหมดในรอบเดียว**
[[fig:pah]]
| ขั้น | ค่า (สไลด์) |
|---|---|
| PAH ถูกกรอง | 20% |
| หลั่งที่ท่อไตส่วนต้น | 70% |
| กลับเข้าหลอดเลือดดำ | 10% → **extraction ratio 0.9** |
| C_PAH = **effective RPF (ERPF)** | ~**630 mL/min** |
| **Actual RPF** = ERPF ÷ 0.9 | ~**700 mL/min** |
| **RBF** = RPF ÷ (1 − Hct) | ~**1.2–1.3 L/min** |
- **Hct** = สัดส่วนปริมาตร RBC ในเลือด เช่น Hct 40% = เลือด 100 mL มี RBC 40 mL และพลาสมา 60 mL → RBF = RPF ÷ 0.6 (แปลง % เป็นทศนิยมก่อน)

### วัด GFR
- สารที่ใช้วัด GFR ต้อง **กรองได้เสรี ไม่ถูกดูดกลับ ไม่ถูกหลั่ง ไม่ถูกเผาผลาญ** → clearance = GFR พอดี
- **Inulin** = **gold standard** (ต้องหยดเข้าเส้นตลอด จึงใช้ในงานวิจัย)
- **Creatinine clearance (CCr)** = ที่ใช้ทางคลินิก: creatinine มาจากการสลาย creatine ในกล้ามเนื้อ ~1–2% ของ creatine pool ต่อวัน ระดับในเลือดคงที่ในคนปกติ
  - **24-h CCr = (U_Cr × V) / P_Cr** · sCr ปกติ **0.6–1.2 mg/dL** · GFR ปกติ **125 mL/min (180 L/วัน)**
  - (ตำรา) creatinine ถูก **หลั่ง** ที่ PT ด้วยราว 10–20% → CCr **สูงกว่า GFR จริง** และยิ่งเห็นชัดเมื่อ GFR ต่ำ · ยาที่บล็อกการหลั่ง (trimethoprim, cimetidine) ทำให้ sCr ขึ้นโดย GFR ไม่เปลี่ยน — หัวข้อ 13

### sCr ไม่ใช่เส้นตรงกับ GFR (ตำรา)
[[fig:scr_curve]]
- สร้าง creatinine คงที่ → ที่สมดุล **GFR × sCr ≈ คงที่** → กราฟ hyperbola
- ช่วงต้น GFR หายไปครึ่งหนึ่ง sCr ขยับแค่ราว 1 → 2 mg/dL · ช่วงท้าย GFR ลดนิดเดียว sCr พุ่ง
- sCr ขึ้นกับ **มวลกล้ามเนื้อ** ด้วย: ผู้สูงอายุตัวเล็ก/ขาดอาหาร sCr \"ปกติ\" อาจซ่อน GFR ที่ต่ำมาก · นักกล้าม sCr สูงทั้งที่ไตปกติ

### eGFR — ใช้แบ่งระยะ CKD
สไลด์แสดงสามสมการ (ภาพ อ่านรายละเอียดไม่ได้ · อ้าง Comprehensive Clinical Nephrology 5th ed): **Cockcroft–Gault (1976)** · **MDRD (1999)** · **CKD-EPI (2012)** — ทุกสมการใช้ sCr ร่วมกับอายุ เพศ (และน้ำหนักใน CG)
| สมการ | ให้ค่าอะไร | ข้อสังเกต (ตำรา/แนวทาง) |
|---|---|---|
| Cockcroft–Gault | **CCr (mL/min)** = (140 − อายุ) × น้ำหนัก ÷ (72 × sCr) × 0.85 ถ้าหญิง | ไม่ปรับพื้นที่ผิว · ยังใช้ปรับขนาดยาบางตัว |
| MDRD | eGFR mL/min/1.73 m² | ต่ำกว่าจริงเมื่อ GFR > 60 |
| CKD-EPI | eGFR mL/min/1.73 m² | แม่นกว่าที่ GFR สูง · **KDIGO 2024 แนะนำ CKD-EPI 2021 ที่ไม่ใช้เชื้อชาติ** และใช้ cystatin C ร่วมเมื่อมวลกล้ามเนื้อผิดปกติ |
- ปัจจัยที่ทำให้ GFR ต่างกันตามสรีระ (สไลด์): อายุ > 30 ปี GFR ลดลงเรื่อย ๆ และ > 80 ปีเหลือ ~50% · lean body mass มาก GFR สูง · ชาย > หญิง ~10% · African-American สูงกว่า · อาหารโปรตีน/คาร์โบไฮเดรตสูง GFR ↑ · ตั้งครรภ์ GFR ↑
""",
    ["Clearance = UV/P — ปริมาตรพลาสมาที่ถูกล้างสารนั้นต่อนาที",
     "PAH: กรอง 20% + หลั่ง 70% → C_PAH = ERPF ~630 · ÷0.9 = RPF ~700 · ÷(1−Hct) = RBF",
     "Inulin = gold standard ของ GFR · ทางคลินิกใช้ creatinine (CCr สูงกว่า GFR จริงเพราะมีการหลั่ง)",
     "GFR × sCr ≈ คงที่ → sCr ขึ้นเล็กน้อยในคนที่ sCr เดิมต่ำ = GFR หายไปมาก",
     "eGFR (CG 1976 · MDRD 1999 · CKD-EPI 2012/2021) ใช้แบ่งระยะ CKD"],
    [mcq(N(5), "During a research study, a healthy volunteer receives a para-aminohippuric acid (PAH) infusion. Urine PAH is 12 mg/mL, urine flow 1.0 mL/min, plasma PAH 0.02 mg/mL and haematocrit 40%. Assuming a PAH extraction ratio of 0.9, what is the renal blood flow?",
         ["600 mL/min", "667 mL/min", "1,000 mL/min", "1,111 mL/min", "1,500 mL/min"], 3,
         "1) **C_PAH = ERPF** = (12 × 1.0) / 0.02 = **600 mL/min**\n2) **Actual RPF** = ERPF ÷ 0.9 = **667 mL/min**\n3) **RBF** = RPF ÷ (1 − Hct) = 667 ÷ 0.6 = **1,111 mL/min**\n\n"
         "- **600** — คือ ERPF (หยุดที่ขั้นแรก)\n- **667** — คือ RPF จริง ยังไม่แปลงเป็นเลือดทั้งหมด\n"
         "- **1,000** — = 600 ÷ 0.6 ลืมหารด้วย extraction ratio\n- **1,500** — = 600 ÷ 0.4 ใช้ Hct แทน (1 − Hct)",
         "ERPF = C_PAH → ÷0.9 = RPF → ÷(1−Hct) = RBF", "PAH clearance and renal blood flow", R("Clinical assessment of RBF"), [GFRH, RFT, CIRC]),
     mcq(N(6), "An 84-year-old bedridden woman weighing 38 kg is admitted with pneumonia. Her serum creatinine is 0.8 mg/dL. The team plans to give a renally excreted antibiotic at full dose because her 'creatinine is normal'. Which statement is most accurate?",
         ["Her GFR must be normal because serum creatinine is within 0.6–1.2 mg/dL",
          "Her GFR is likely much lower than suggested because low muscle mass reduces creatinine production",
          "Serum creatinine overestimates GFR in the elderly because tubular reabsorption of creatinine increases",
          "A normal creatinine excludes drug accumulation regardless of age",
          "Creatinine clearance is unaffected by body weight, so no adjustment is needed"], 1,
         "sCr ขึ้นกับ **การสร้าง** (มวลกล้ามเนื้อ — creatinine มาจาก creatine ในกล้ามเนื้อ) และ **การขับ** (GFR) · หญิงอายุ 84 ปี 38 กิโลกรัม นอนติดเตียง → สร้าง creatinine น้อยมาก → sCr 0.8 อาจตรงกับ GFR ต่ำมาก · Cockcroft–Gault: (140 − 84) × 38 ÷ (72 × 0.8) × 0.85 ≈ **31 mL/min** → ต้องปรับขนาดยา (สไลด์: GFR ลดตามอายุ เหลือ ~50% เมื่อ > 80 ปี)\n\n"
         "- **sCr ปกติ = GFR ปกติ** — ผิดเพราะไม่คิดมวลกล้ามเนื้อ\n- **ท่อไตดูดกลับ creatinine** — creatinine ไม่ถูกดูดกลับ (ถูกหลั่งเล็กน้อยต่างหาก)\n"
         "- **ไม่มียาสะสมแน่นอน** — ผิด ยาที่ขับทางไตสะสมได้\n- **CCr ไม่ขึ้นกับน้ำหนัก** — สูตร CG ใช้น้ำหนักโดยตรง",
         "ผู้สูงอายุตัวเล็ก: sCr \"ปกติ\" ≠ GFR ปกติ", "Limitations of serum creatinine", R("Clinical assessment of GFR · Physical variations of GFR", "Cockcroft & Gault 1976"), [RFT, PKSP, PK, GFRH])],
    [GFRH, RFT, CIRC, PK, CKD_B], {"pah": F.pah(), "scr_curve": F.scr_curve()}, source=SRC_ADD)

# ═════════════════════════════════════════════ 4
sec("nephro-phy1-04", "Filtration barrier — ทำไมน้ำผ่าน แต่ albumin ไม่ผ่าน",
    "endothelium 70 nm · GBM (collagen IV, ประจุลบ) · slit diaphragm 4–14 nm (nephrin podocin) · ขนาด < 3.6 nm ผ่านเสรี · ประจุลบกั้น albumin", 9,
"""### สามชั้นของ filtration barrier (สไลด์)
[[fig:barrier]]
| ชั้น | โครงสร้าง | กั้นอะไร |
|---|---|---|
| 1. **Endothelium** ของ glomerular capillary | มีรู (fenestra) ~**70 nm** · ผิวเคลือบ glycoprotein ประจุลบ | size barrier → กั้น **RBC WBC platelet** |
| 2. **Glomerular basement membrane** | ตาข่ายโปรตีนประจุลบ (**collagen IV**) | size barrier + **charge barrier หลัก** → กั้น **โปรตีนใหญ่** |
| 3. **Slit diaphragm** ระหว่าง foot process ของ podocyte | รู **4–14 nm** · glycoprotein ประจุลบ: **nephrin, NEPH-1, podocin** | size + charge → กั้น **โปรตีนเล็ก เช่น albumin** |
- ในคนปกติการซึมผ่านของกระจุกค่อนข้างคงที่

### คุณสมบัติของสาร: ขนาดและประจุ
| ขนาด | การกรอง |
|---|---|
| เส้นผ่านศูนย์กลาง < 3.6 nm หรือ MW < 5.5 kDa | **กรองเสรี** (เท่าน้ำ) |
| 3.6–8.4 nm หรือ 5.5–70 kDa | ผ่านน้อยลงเรื่อย ๆ |
| > 8.4 nm หรือ > 70 kDa | **ไม่ผ่าน** (รวมเซลล์เม็ดเลือด) |

| สาร (Boron & Boulpaep ในสไลด์) | MW (kDa) | ผ่าน (% เทียบน้ำ) |
|---|---|---|
| Na⁺ · urea · glucose · creatinine | < 0.2 | 100 |
| **myoglobin** | 17 | **75** |
| **hemoglobin** | 68 | **3** |
| **albumin** | 69 | **0.5** |
- **ประจุ** มีผลเฉพาะกับ **โมเลกุลใหญ่**: ประจุลบของ barrier ผลัก **albumin (ประจุลบ)** · ไอออนเล็กทั้งบวกและลบ (Na⁺ Cl⁻ K⁺ HCO₃⁻) ผ่านได้หมด
- จึงได้ **filtrate ที่เหมือนพลาสมาทุกอย่างยกเว้นโปรตีนและเซลล์**: glucose 100 mg/dL · amino acid · urea · uric acid · creatinine เท่าพลาสมา · osmolality ~300 · albumin แทบเป็นศูนย์

#### ทำไมถึงมีอาการนี้
| อาการ/ภาวะ | กลไก (สไลด์ + ตำรา) | ใช้แยกโรคอย่างไร |
|---|---|---|
| **albuminuria ในเบาหวาน** | foot process กว้าง (inflammation) + เสียประจุลบ → albumin ลอดได้ | albuminuria (UACR) = สัญญาณแรกของ diabetic kidney disease |
| **nephrotic syndrome** | podocyte บาดเจ็บจากภูมิคุ้มกัน หรือ **ยีน nephrin/podocin กลายพันธุ์** → slit diaphragm เสีย → โปรตีนรั่วมาก | proteinuria > 3.5 g/วัน · ปัสสาวะเป็นฟอง (รายละเอียดในคาบ 14) |
| **hematuria + proteinuria** | ชั้นกรองถูกทำลาย (nephritic) → แม้แต่ RBC ก็ลอดได้ | ร่วมกับ dysmorphic RBC/RBC cast = glomerular |
| **ปัสสาวะสีโคล่าใน rhabdomyolysis** | myoglobin เล็ก (17 kDa) กรองได้ 75% | dipstick heme บวกแต่ไม่เห็น RBC |
| **hemolysis ปัสสาวะไม่แดงทันที** | Hb tetramer 68 kDa ผ่านแค่ 3% และ (ตำรา) Hb อิสระถูก **haptoglobin** จับไว้ก่อน — เห็น hemoglobinuria เมื่อ haptoglobin อิ่ม | intravascular hemolysis รุนแรง |
- Hb กับ albumin หนักเกือบเท่ากัน แต่ albumin ผ่านน้อยกว่าราว 6 เท่า = หลักฐานว่า **ประจุลบ** ของ barrier ทำงานจริง
""",
    ["Endothelium กั้นเซลล์ · GBM กั้นโปรตีนใหญ่ · slit diaphragm กั้น albumin",
     "< 3.6 nm (< 5.5 kDa) ผ่านเสรี · > 8.4 nm (> 70 kDa) ไม่ผ่าน",
     "ประจุลบมีผลเฉพาะโมเลกุลใหญ่ — ผลัก albumin แต่ไอออนเล็กผ่านหมด",
     "Myoglobin 17 kDa ผ่าน 75% · Hb 3% · albumin 0.5%",
     "Nephrin/podocin กลายพันธุ์ หรือ podocyte บาดเจ็บ → nephrotic"],
    [mcq(N(7), "A 5-year-old boy has generalized oedema and frothy urine. Urine protein is 4+ and the proteinuria is highly selective (mostly albumin, very little IgG). Electron microscopy shows effacement of podocyte foot processes. Which change in the filtration barrier best explains why albumin (69 kDa) is lost while larger IgG (150 kDa) is retained?",
         ["Enlargement of endothelial fenestrae to more than 1 µm", "Loss of the negative charge and slit-diaphragm integrity of the podocyte layer",
          "Increased glomerular capillary hydrostatic pressure from afferent dilation", "Active tubular secretion of albumin into the urine",
          "Complete destruction of the glomerular basement membrane"], 1,
         "albumin มีขนาด (7.1 nm) ใกล้ขอบบนของสิ่งที่ผ่านได้ และ **ประจุลบ** — ปกติถูกกั้นด้วย **ประจุลบ + slit diaphragm** · เมื่อ podocyte เสีย (foot process effacement) ประจุลบและ slit diaphragm หายไป → albumin ลอดได้ แต่ IgG ใหญ่กว่ามากจึงยังติดขนาดของ GBM = **selective proteinuria** (minimal change disease)\n\n"
         "- **fenestra > 1 µm** — ถ้าใหญ่ขนาดนั้นเซลล์เม็ดเลือดจะลอดได้\n- **P_GC สูง** — เพิ่มการกรองทั้งหมด ไม่ได้เลือกเฉพาะ albumin\n"
         "- **ท่อไตหลั่ง albumin** — ไม่มีกลไกนี้ ท่อไตดูดกลับโปรตีนต่างหาก\n- **GBM ถูกทำลายทั้งหมด** — จะรั่วทั้ง IgG และ RBC (non-selective + hematuria)",
         "Selective albuminuria = เสียประจุลบ/slit diaphragm ของ podocyte", "Charge and size selectivity", R("Filtration membrane permeability · Solute charge"), [GFRH, NEPHROTIC, NEPHROTIC_B, EDEMA]),
     mcq(N(8), "A 22-year-old man develops severe muscle pain and cola-coloured urine after an extreme gym session. Urine dipstick is strongly positive for blood, but microscopy shows no red cells. CK is 85,000 U/L. Why does myoglobin appear in the urine so readily?",
         ["It is bound to haptoglobin, which carries it across the glomerulus", "It is actively secreted by organic cation transporters in the proximal tubule",
          "Its small size (about 17 kDa, 3.8 nm) allows it to be filtered about 75% as freely as water",
          "It is positively charged and therefore attracted by the basement membrane", "It is filtered only after the glomerular basement membrane is destroyed"], 2,
         "สไลด์ (ตาราง Boron & Boulpaep): **myoglobin 17 kDa, 3.76 nm → filterability 75%** เพราะเล็กกว่าเกณฑ์ 70 kDa มาก · กล้ามเนื้อสลาย → myoglobin ในเลือดสูง → กรองออกมาในปัสสาวะ → dipstick heme บวก (ทดสอบ peroxidase ของ heme) แต่ไม่มี RBC · heme เป็นพิษต่อท่อไต → AKI ได้\n\n"
         "- **haptoglobin** — จับ hemoglobin ไม่ใช่ myoglobin และทำให้กรอง **ไม่ได้**\n- **OCT หลั่ง** — myoglobin ไม่ใช่ organic cation ขนาดเล็ก\n"
         "- **ประจุบวกถูกดึงดูด** — ไม่ใช่เหตุผลหลัก ขนาดคือตัวกำหนด\n- **GBM ถูกทำลายก่อน** — ไม่จำเป็น กรองได้ผ่าน barrier ปกติ",
         "Myoglobin เล็ก (17 kDa) → กรองได้ 75% → ปัสสาวะสีโคล่า", "Solute size and filterability", R("Solute property — molecular size"), [GFRH, HEMAT, UAS, AKI])],
    [GFRH, STRUCT, NEPHROTIC, NEPHROTIC_B, HEMAT, UAS, EDEMA], {"barrier": F.barrier()})

# ═════════════════════════════════════════════ 5
sec("nephro-phy1-05", "Starling forces และ GFR = Kf × NFP — ทุกอย่างที่เปลี่ยน GFR ผ่านสี่ช่องนี้",
    "NFP = 60 − (18 + 32) = 10 mmHg · GFR 125 mL/min · Kf (mesangial, GBM) · P_GC (afferent/efferent) · P_BC (อุดตัน) · π_GC (albumin)", 12,
"""### แรงที่ขับการกรอง
**Net filtration pressure (NFP)** = แรงดันออก − แรงดึงกลับ
[[fig:starling]]
| แรง | ค่า (mmHg) | ทิศ | ขึ้นกับ |
|---|---|---|---|
| **P_GC** ความดันน้ำในกระจุก | 60 | ดันออก | ปริมาณเลือดที่อยู่ในกระจุก (afferent/efferent) |
| **P_BC** ความดันใน Bowman's space | 18 | ดันกลับ | การไหลของปัสสาวะข้างหน้า |
| **π_GC** oncotic pressure ของพลาสมา | 32 | ดึงกลับ | ความเข้มข้นโปรตีน โดยเฉพาะ **albumin** |
| π_BC oncotic ใน Bowman | ≈ 0 | — | ไม่มีโปรตีนใน filtrate |
- **NFP = 60 − (18 + 32) = 10 mmHg**
- **GFR = Kf × NFP** โดย **Kf = การซึมผ่าน × พื้นที่กรอง** = 12.5 × 10 = **125 mL/min ≈ 180 L/วัน** (พลาสมาทั้งตัว ~3 L ถูกกรองราว 60 รอบต่อวัน)

### 1. Kf — พื้นที่และการซึมผ่าน
| ปัจจัย | ผล |
|---|---|
| sympathetic, NE, E, **AII** (รวม adenosine/ATP) → **mesangial cell หดตัว** | พื้นที่กรอง ↓ → Kf ↓ → GFR ↓ |
| dopamine, ANP, NO, PGE₂ → mesangial คลายตัว | Kf ↑ → GFR ↑ |
| mesangial โต (เบาหวาน, nephropathy) | Kf ↓ → GFR ↓ |
| **GBM หนา** (เบาหวาน, ความดันสูง) | การซึมผ่าน ↓ → GFR ↓ |
| hypoxia/สารพิษ → endothelium หด tight junction เสีย | สไลด์เขียนว่าการซึมผ่าน ↑ → Kf ↑ → GFR ↑ (ทางคลินิกพิษเหล่านี้มักทำให้ GFR รวมลดจากกลไกอื่น — ตำรา) |

### 2. P_GC — ขึ้นกับว่าแคบ \"ก่อน\" หรือ \"หลัง\" กระจุก
[[fig:arterioles4]]
| การเปลี่ยนแปลง | ตัวอย่าง | RBF | P_GC | GFR |
|---|---|---|---|---|
| afferent หด | sympathetic, NE · NSAID (ตัด PG) | ↓ | ↓ | ↓ |
| **efferent หด** | **angiotensin II** | ↓ | ↑ | ↑ (คงไว้) |
| afferent ขยาย | PGI₂, PGE₂, ANP | ↑ | ↑ | ↑ |
| afferent + efferent ขยาย | NO, dopamine ขนาดต่ำ | ↑ | ↔ | ↔ |
| **efferent ขยาย** | **ACEi / ARB** | ↑ | ↓ | ↓ |
- สไลด์เน้นสามจุด: **AII ช่วยคง GFR เมื่อความดันเข้าไตต่ำ** · **PG ช่วยคง RBF ใน hemorrhage/shock — ให้ NSAID ช่วงนั้นทำให้เกิด AKI** · **ACEi/ARB ใช้ลด hyperfiltration ในเบาหวานระยะแรก** (รายละเอียดทางคลินิกหัวข้อ 6)

### 3. P_BC — ทางเดินปัสสาวะอุด
- **นิ่วอุด pelvis/ureter** → ปัสสาวะค้างในท่อไต → Bowman's space ดันกลับ ↑ → GFR ↓
- **ต่อมลูกหมากโต** → ท่อปัสสาวะอุด → ค้างในกระเพาะ → ย้อนขึ้น ureter ถึงไต → P_BC ↑ → GFR ↓ (= **post-renal AKI** — ต้องอุดทั้งสองข้างหรือไตข้างเดียว creatinine จึงขึ้น)

### 4. π_GC — albumin
| ภาวะ | π_GC | GFR (ปัจจัยอื่นคงที่) |
|---|---|---|
| albumin สูง (โปรตีนในอาหารสูง ปริมาตรหดตัว/ขาดน้ำ) | ↑ | ↓ |
| albumin ต่ำ (ตับแข็ง ขาดอาหาร nephrotic syndrome) | ↓ | ↑ |
- (ตำรา) π_GC เพิ่มขึ้นตามความยาวกระจุก เพราะน้ำออกไป ~20% แล้วโปรตีนเข้มข้นขึ้น — เลือดที่ออกทาง efferent จึงมี oncotic สูง ซึ่งคือแรงดูดกลับที่ peritubular capillary (หัวข้อ 8)
""",
    ["NFP = P_GC − (P_BC + π_GC) = 60 − (18 + 32) = 10 mmHg",
     "GFR = Kf × NFP = 12.5 × 10 = 125 mL/min = 180 L/วัน",
     "หด afferent → GFR ↓ · หด efferent → GFR ↑ (RBF ↓ ทั้งคู่)",
     "นิ่ว/BPH → P_BC ↑ → GFR ↓ · albumin ต่ำ → π_GC ↓ → GFR ↑",
     "Mesangial หดตัว (AII, NE) หรือ GBM หนา (DM) → Kf ↓"],
    [mcq(N(9), "A 76-year-old man with benign prostatic hyperplasia presents with a palpable bladder, 1,400 mL drained on catheterisation, bilateral hydronephrosis and creatinine rising from 1.1 to 3.4 mg/dL. Which change in glomerular Starling forces primarily explains the fall in his GFR?",
         ["Decreased glomerular capillary oncotic pressure", "Increased Bowman's capsule hydrostatic pressure",
          "Decreased filtration coefficient from mesangial contraction", "Increased glomerular capillary hydrostatic pressure", "Decreased Bowman's space oncotic pressure"], 1,
         "ตรงตามสไลด์: ต่อมลูกหมากโต → ท่อปัสสาวะอุด → ปัสสาวะค้างในกระเพาะและ **ย้อนขึ้น ureter ถึงไต** → ของเหลวค้างในท่อไต → **P_BC ↑** → NFP ลด → GFR ↓ (post-renal AKI) · ปลดการอุดแล้ว P_BC ลด GFR กลับ\n\n"
         "- **π_GC ลด** — จะทำให้ GFR **เพิ่ม**\n- **Kf ลดจาก mesangial หด** — ไม่ใช่กลไกหลักของการอุดตัน\n"
         "- **P_GC เพิ่ม** — จะเพิ่ม GFR\n- **π_BC** — ปกติเป็นศูนย์อยู่แล้ว",
         "ทางเดินปัสสาวะอุด → P_BC ↑ → GFR ↓", "Bowman's capsule pressure and obstruction", R("Factors: Bowman's capsule hydrostatic pressure"), [GFRH, AKI, AKI_B, OLIG]),
     mcq(N(10), "In an experimental animal, plasma albumin is acutely lowered from 4.0 to 2.0 g/dL while renal plasma flow, arteriolar resistances and Kf are held constant. What is the expected immediate effect on GFR and filtration fraction?",
         ["GFR decreases; filtration fraction decreases", "GFR increases; filtration fraction increases", "GFR unchanged; filtration fraction unchanged",
          "GFR decreases; filtration fraction increases", "GFR increases; filtration fraction decreases"], 1,
         "albumin ลด → **π_GC ลด** → แรงดึงกลับลดลง → NFP ↑ → **GFR ↑** · RPF คงที่ → **FF = GFR/RPF ↑** — ตรงกับแถว \"Decreased plasma protein: RPF ↔ · π_GC ↓ · GFR ↑ · FF ↑\" ในตาราง FF ของสไลด์\n\n"
         "- **GFR ลด** — ทิศผิด π_GC เป็นแรงต้านการกรอง\n- **ไม่เปลี่ยน** — π_GC เป็นหนึ่งในสี่ตัวแปรของ NFP\n"
         "- **GFR ลด FF เพิ่ม** — GFR ผิดทาง\n- **GFR เพิ่ม FF ลด** — RPF คงที่ FF ต้องเพิ่มตาม GFR\n\nหมายเหตุ: ในผู้ป่วย nephrotic จริง GFR มักไม่สูงเพราะ Kf ลดและปริมาตรเปลี่ยน — โจทย์นี้ถามผลของแรงเดียว",
         "Albumin ↓ → π_GC ↓ → GFR ↑ FF ↑", "Glomerular oncotic pressure", R("Glomerular colloid osmotic pressure · Filtration fraction table"), [GFRH, NEPHROTIC_B, CIRRH])],
    [GFRH, AKI, AKI_B, NEPHROTIC_B, DM, RAASD, NSAID], {"starling": F.starling(), "arterioles4": F.arterioles4()})

# ═════════════════════════════════════════════ 6
sec("nephro-phy1-06", "ยาที่ \"บีบ\" หรือ \"คลาย\" arteriole — NSAID, ACEi/ARB, SGLT2i และ hemodynamic AKI",
    "ไตขาดเลือดพยุง GFR ด้วย PG (afferent) + AII (efferent) · NSAID / ACEi ตัดคนละมือ · triple whammy · hyperfiltration ในเบาหวาน", 10,
"""### หลักเดียว ใช้ได้กับทุกยา
ไตปกติที่ปริมาตรปกติแทบไม่ต้องพึ่ง PG หรือ AII ในการคุม GFR · แต่เมื่อ **เลือดเข้าไตน้อย** (shock เสียเลือด ขาดน้ำ ท้องเสีย HF ตับแข็ง renal artery stenosis) ไตต้องใช้ **สองมือ** พยุง P_GC:
1. **Prostaglandin (PGI₂/PGE₂) ขยาย afferent** → เลือดยังเข้ากระจุกได้ (สไลด์: PG ช่วยคง RBF ใน hemorrhage และ circulatory shock)
2. **Angiotensin II หด efferent** → เลือดที่เข้ามาค้างในกระจุก ความดันไม่ตก (สไลด์: AII ช่วยคง GFR เมื่อความดันเข้าไตต่ำ)
[[fig:lowflow]]

#### ทำไมถึงมีอาการนี้ — AKI จากยาในภาวะเลือดเข้าไตน้อย
| ยา | ตัดมือไหน | ผลต่อกระจุก | ภาพทางคลินิก |
|---|---|---|---|
| **NSAID** (ibuprofen, aspirin ขนาดสูง, diclofenac) | ยับยั้ง COX → PG ↓ → **afferent หด** | เลือดเข้าน้อยลงอีก P_GC ตก | AKI แบบ pre-renal (FENa ต่ำ ปัสสาวะใส) · สไลด์: **ให้ NSAID ระหว่าง hemorrhagic shock → AKI** · ยังทำให้ K สูง (renin ↓) และบวม (ตำรา) |
| **ACEi / ARB** | AII ↓ → **efferent คลาย** | เลือดไหลผ่านออกเร็ว P_GC ตก | Cr ขึ้นหลังเริ่มยา โดยเฉพาะ **bilateral renal artery stenosis**, ไตข้างเดียวที่ตีบ, ขาดน้ำ, HF รุนแรง |
| NSAID + ACEi/ARB + **diuretic** (\"triple whammy\" — ตำรา) | ตัดทั้งสองมือ + ลดปริมาตร | P_GC ไม่มีอะไรพยุง | AKI รุนแรงในผู้สูงอายุ — เป็นสาเหตุ AKI จากยาที่ป้องกันได้บ่อยที่สุด |

### Cr ขึ้นหลังเริ่ม ACEi/ARB — ดีหรือร้าย (ตำรา/แนวทาง KDIGO)
- ในคนที่ปริมาตรปกติ Cr ขึ้นได้เล็กน้อยช่วงแรก (**ไม่เกินราว 30%**) = ผลทางสรีรวิทยาที่ตั้งใจ: P_GC ลด → ลดภาระกระจุก → ชะลอการเสื่อมระยะยาว → **ไม่ต้องหยุดยา**
- Cr ขึ้นมากกว่านั้น → หาสาเหตุ: ขาดน้ำ ได้ NSAID/diuretic ร่วม หรือ **renal artery stenosis** (ไตข้างนั้นพึ่ง AII ทั้งหมด)

### เบาหวาน: hyperfiltration และยาสองกลุ่มที่ปกป้องไต
[[fig:tgf]]
- สไลด์: \"hyperglycemia in DM activates tubuloglomerular feedback → glomerular hyperfiltration → diabetic nephropathy\" และ \"ARB/ACEi ใช้รักษา hyperfiltration ในเบาหวานระยะแรก\"
- (ตำรา) กลไก: น้ำตาลสูง → **SGLT2 ใน PT ดูด Na⁺ + glucose มากขึ้น** → NaCl ไปถึง macula densa น้อย → TGF แปลว่า GFR ต่ำ → **afferent ขยาย** → P_GC สูง → กรองมากเกิน (hyperfiltration) → กระจุกบาดเจ็บ albuminuria
- **ACEi/ARB** ลด P_GC ทาง **ขยาย efferent** · **SGLT2 inhibitor** ลด P_GC ทาง **คืน TGF → หด afferent** → ใช้ร่วมกันได้และเสริมกัน (KDIGO 2022 Diabetes in CKD)
- eGFR ลดเล็กน้อยช่วง 2–4 สัปดาห์แรกหลังเริ่ม SGLT2i หรือ ACEi/ARB = \"hemodynamic dip\" ที่คาดไว้ ไม่ใช่ไตบาดเจ็บ
""",
    ["ไตขาดเลือด: PG ขยาย afferent + AII หด efferent = สองมือพยุง GFR",
     "NSAID ตัด PG → afferent หด · ACEi/ARB ตัด AII → efferent คลาย → GFR ตกเฉพาะตอนขาดเลือด",
     "Triple whammy = NSAID + ACEi/ARB + diuretic",
     "Cr ขึ้น ≤ ~30% หลังเริ่ม ACEi/ARB ยอมรับได้ · ขึ้นมาก → นึกถึงขาดน้ำ/NSAID/renal artery stenosis",
     "เบาหวาน: SGLT2 ดูดมาก → TGF → afferent ขยาย → hyperfiltration · SGLT2i หด afferent · ACEi ขยาย efferent"],
    [mcq(N(11), "A 79-year-old woman with heart failure takes enalapril 10 mg twice daily and furosemide 40 mg daily. After a week of ibuprofen for knee osteoarthritis, she becomes drowsy and oliguric. Creatinine has risen from 1.1 to 2.6 mg/dL; urinalysis is bland and FENa is 0.4%. Which mechanism best explains the fall in GFR?",
         ["Allergic interstitial nephritis from ibuprofen",
          "Loss of prostaglandin-mediated afferent dilation in a kidney whose angiotensin II-dependent efferent tone is already blocked",
          "Acute tubular necrosis from furosemide toxicity", "Bilateral ureteric obstruction by papillary necrosis",
          "Increased glomerular capillary hydrostatic pressure from efferent constriction"], 1,
         "HF + furosemide = เลือดเข้าไตน้อย ไตพึ่ง **PG (afferent)** และ **AII (efferent)** · enalapril ตัด AII ไปแล้ว → ibuprofen ตัด PG อีก → afferent หด efferent ไม่หดชดเชย → P_GC ตก → GFR ↓ (= **triple whammy**) · ปัสสาวะใส FENa < 1% = ท่อไตยังดี (hemodynamic/pre-renal)\n\n"
         "- **AIN** — จะมีไข้ ผื่น WBC cast eosinophiluria และ FENa มักไม่ต่ำ\n- **ATN** — FENa > 2% มี muddy brown cast · furosemide ไม่ทำให้ ATN\n"
         "- **papillary necrosis อุดท่อ** — พบน้อยมาก และจะมีปวด/เลือด/ไตบวมน้ำ\n- **P_GC เพิ่มจาก efferent หด** — ACEi ทำให้ efferent **คลาย** ไม่ใช่หด",
         "HF + ACEi + diuretic + NSAID = triple whammy → hemodynamic AKI", "Prostaglandins, angiotensin II and hemodynamic AKI",
         R("Glomerular hydrostatic pressure — PG and NSAIDs · AII maintains GFR", GH), [GFRH, AKI, AKI_B, NSAID, RAASD, DIUR, ADR, ADRDRUG, HF]),
     mcq(N(12), "A 55-year-old man with type 2 diabetes, eGFR 58 mL/min/1.73 m² and albuminuria 600 mg/g already takes losartan. Two weeks after empagliflozin is added, his eGFR is 52 mL/min/1.73 m²; he is euvolaemic and well. What is the most likely explanation?",
         ["Empagliflozin-induced acute interstitial nephritis", "Restored tubuloglomerular feedback causing afferent arteriolar constriction and lower intraglomerular pressure",
          "Efferent arteriolar dilation caused by empagliflozin", "Osmotic acute tubular necrosis from glucosuria",
          "Increased Bowman's capsule pressure from glucose crystals"], 1,
         "SGLT2i บล็อกการดูด Na⁺/glucose ที่ PT → **NaCl ไปถึง macula densa มากขึ้น** → TGF ทำงานคืน → **afferent หด** → P_GC ↓ → eGFR ลดเล็กน้อย (~3–6 mL/min) ช่วงแรก = **hemodynamic dip ที่คาดไว้** ซึ่งลดภาระกระจุกและชะลอการเสื่อมระยะยาว → ไม่ต้องหยุดยา (กลไกและการใช้ทางคลินิกเติมจากตำรา/KDIGO 2022 — สไลด์สอนแค่ \"hyperglycemia activates TGF → hyperfiltration\")\n\n"
         "- **AIN** — ไม่มีอาการ/ตะกอนบ่งชี้ และไม่ใช่ผลที่พบบ่อยของยา\n- **efferent ขยาย** — เป็นกลไกของ losartan/ACEi ไม่ใช่ SGLT2i\n"
         "- **osmotic ATN** — ไม่เกิดจาก glucosuria ระดับนี้\n- **ผลึกกลูโคส** — ไม่มีจริง",
         "SGLT2i: Na⁺ ถึง macula densa ↑ → afferent หด → eGFR dip ที่ตั้งใจ", "TGF and SGLT2 inhibitors", R("Autoregulation — hyperglycemia activates TGF", BB, "KDIGO 2022 Diabetes Management in CKD"), [GFRH, DM, DM_B, DMDRUG, CKD_B])],
    [GFRH, AKI, AKI_B, NSAID, RAASD, DIUR, ADR, ADRDRUG, HF, DM, DMDRUG, RAS, SHOCK], {"lowflow": F.lowflow(), "tgf": F.tgf()}, source=SRC_ADD)

# ═════════════════════════════════════════════ 7
sec("nephro-phy1-07", "Autoregulation — myogenic response และ tubuloglomerular feedback",
    "MAP 80–170 → RBF/GFR เกือบคงที่ · myogenic 3–10 วินาที · TGF ที่ JGA · หายไปเมื่อ MAP < 75 · อาหารโปรตีนสูงเพิ่ม GFR", 9,
"""### Autoregulation คืออะไร
กลไก **ในตัวไตเอง** (ไม่ต้องอาศัยเส้นประสาทหรือฮอร์โมน — ไตปลูกถ่ายที่ไม่มีเส้นประสาทก็ทำได้) ที่ตรึง RBF และ GFR ไว้เกือบคงที่ เมื่อ **MAP อยู่ระหว่าง 80–170 mmHg**
[[fig:autoreg]]

### 1. Myogenic response (3–10 วินาที)
- เกิดที่ **arcuate artery, interlobular artery และ afferent arteriole** → คง RBF
- ลำดับในสไลด์: ความดันในหลอดเลือด ↑ → ผนังถูกยืด → **stretch-gated cation channel** เปิด → Na⁺ เข้า → **depolarization** → **voltage-gated Ca²⁺ channel** เปิด → Ca²⁺ เข้า → [Ca²⁺]i ↑ → **หลอดเลือดหด** → RBF กลับเท่าเดิม
- ประโยชน์: RBF/GFR นิ่งเวลาเปลี่ยนท่า · **กันกระจุกจากความดันสูง** ใน HT, DM, ESRD (ถ้ากลไกนี้เสีย ความดันทั้งตัวจะส่งตรงถึงกระจุก → glomerulosclerosis — ตำรา)

### 2. Tubuloglomerular feedback (TGF)
- เกิดที่ **juxtaglomerular apparatus (JGA)** — จุดที่ปลาย TAL (macula densa) แนบกับ afferent ของ nephron ตัวเอง → คง **GFR**
- GFR ↑ → NaCl ไหลถึง distal tubule/macula densa ↑ → **afferent หด** → GFR ลดกลับ
- (ตำรา — รายละเอียดในภาพ JGA ของสไลด์อ่านไม่ได้) macula densa รับ NaCl ผ่าน **NKCC2** → หลั่ง **ATP → adenosine** → **A1 receptor** ที่ afferent → หด · ทิศตรงข้าม: NaCl ↓ → adenosine ↓ + PGE₂/NO → afferent ขยาย และ **renin ↑** → AII หด efferent
- **loop diuretic** บล็อก NKCC2 ที่ macula densa ด้วย → TGF ไม่ทำงาน (และ renin ↑) — ตำรา

### ข้อจำกัด (สไลด์ \"Note!!!\")
1. **ไม่ทำงานเมื่อ MAP < 75 mmHg** → ใน shock RBF/GFR ตกตามความดันตรง ๆ = **pre-renal AKI** · ผู้ป่วยความดันสูงเรื้อรัง ช่วงนี้เลื่อนขึ้น (ตำรา) → MAP \"ปกติ\" ก็อาจไม่พอ
2. **ไม่สมบูรณ์** — RBF/GFR ยังเปลี่ยนเล็กน้อยตามความดัน
3. ฮอร์โมนและ sympathetic ที่ตอบสนองต่อปริมาตร ECF **ยังเปลี่ยน RBF/GFR ได้** แม้อยู่ในช่วง autoregulation

### อาหารโปรตีน/คาร์โบไฮเดรตสูงเพิ่ม GFR
กรดอะมิโนและกลูโคสถูกดูดกลับคู่กับ Na⁺ ที่ PT มากขึ้น → NaCl ถึง macula densa ลด → TGF ขยาย afferent → GFR ↑ (สไลด์จัดเป็นผลของ autoregulation mechanism) — กลไกเดียวกับ hyperfiltration ในเบาหวาน (หัวข้อ 6)

#### ทำไมถึงมีอาการนี้ — ผู้ป่วย sepsis ที่ MAP 60 ปัสสาวะออกน้อย
MAP ต่ำกว่าช่วง autoregulation → afferent ขยายสุดแล้วก็ยังไม่พอ → P_GC ตกตามความดัน → GFR ↓ → oliguria · เป้าหมาย MAP ≥ 65 mmHg ในแนวทาง sepsis จึงเกี่ยวกับการคืนเลือดเข้าไต (ตำรา)
""",
    ["Autoregulation คง RBF/GFR ที่ MAP 80–170 ไม่ต้องใช้เส้นประสาท/ฮอร์โมน",
     "Myogenic: ยืด → stretch cation channel → depolarize → VGCC → Ca²⁺ เข้า → หด (3–10 วินาที)",
     "TGF: NaCl ถึง macula densa ↑ → adenosine (A1) → afferent หด",
     "MAP < 75 → autoregulation หาย → GFR ตกตามความดัน (pre-renal)",
     "อาหารโปรตีนสูง/น้ำตาลสูง → Na ถูกดูดที่ PT มาก → TGF → GFR ↑"],
    [mcq(N(13), "A 63-year-old man with septic shock has MAP 58 mmHg despite fluids. Before vasopressors, his urine output falls to 10 mL/h. A student asks why renal autoregulation did not protect his GFR. What is the best answer?",
         ["Autoregulation only operates when MAP is above about 75–80 mmHg; below this, GFR falls with perfusion pressure",
          "Sepsis abolishes the macula densa, so only the myogenic response remains", "Autoregulation fails because angiotensin II dilates the efferent arteriole",
          "Autoregulation maintains urine output but not GFR", "Autoregulation requires intact renal sympathetic nerves, which are blocked in sepsis"], 0,
         "สไลด์: autoregulation คง RBF/GFR ที่ **MAP 80–170 mmHg** และ **ไม่ทำงานเมื่อ MAP < 75** · MAP 58 → afferent ขยายเต็มที่แล้วก็ไม่พอ → P_GC และ GFR ลดตามความดัน → oliguria (pre-renal) → ต้องคืนความดัน (vasopressor)\n\n"
         "- **macula densa หายไป** — ไม่ใช่ เป็นเพราะความดันต่ำกว่าช่วงที่ทำงานได้\n- **AII ขยาย efferent** — AII **หด** efferent\n"
         "- **คงปัสสาวะไม่คง GFR** — กลับกัน autoregulation คง RBF/GFR ส่วนปริมาณปัสสาวะขึ้นกับการดูดกลับ\n- **ต้องอาศัยเส้นประสาท** — ผิด autoregulation เป็นกลไกในตัวไต (independent of renal nerve)",
         "MAP < 75 → autoregulation หาย", "Limits of autoregulation", R("Autoregulation of RBF & GFR — Note!!!"), [GFRH, SHOCK, SHOCK_B, OLIG, AKI]),
     mcq(N(14), "A kidney transplant (which has no renal nerve supply) is studied intra-operatively. When renal artery pressure is raised from 100 to 140 mmHg, afferent arteriolar resistance increases within seconds and RBF returns towards baseline. Which sequence best describes this response?",
         ["Stretch → opening of stretch-gated cation channels → depolarisation → voltage-gated Ca²⁺ entry → smooth-muscle contraction",
          "Stretch → nitric oxide release → hyperpolarisation → contraction", "Increased NaCl at macula densa → renin release → efferent constriction",
          "Baroreceptor reflex → sympathetic α1 activation → afferent constriction", "Stretch → prostaglandin E₂ release → afferent constriction"], 0,
         "ตอบสนองภายในวินาทีและเกิดในไตที่ไม่มีเส้นประสาท = **myogenic response** (3–10 วินาที ที่ afferent) · ลำดับตามสไลด์: ยืด → **stretch-gated cation channel** → Na⁺ เข้า → **depolarization** → **VGCC** เปิด → Ca²⁺ เข้า → หด\n\n"
         "- **NO → hyperpolarization → หด** — NO ทำให้ **ขยาย**\n- **macula densa → renin → efferent หด** — renin ไม่เพิ่มเมื่อ NaCl ถึงมาก และ TGF ใช้เวลานานกว่า\n"
         "- **baroreceptor → sympathetic** — ไตปลูกถ่ายไม่มีเส้นประสาท และ reflex จะ **ลด** sympathetic เมื่อความดันสูง\n- **PGE₂ → หด** — PGE₂ ทำให้ afferent ขยาย",
         "Myogenic = ยืด → VGCC → Ca²⁺ → หด (ไม่ต้องใช้เส้นประสาท)", "Myogenic mechanism", R("Autoregulation — Myogenic response"), [GFRH, CIRC])],
    [GFRH, CIRC, SHOCK, OLIG, AKI, DM, HT], {"autoreg": F.autoreg()})

# ── END SECTIONS


# ═════════════════════════════════════════════ ประกอบคาบ
LECNAME = "สรีรวิทยาไตพื้นฐาน I (Watchara Chongsa PhD)"
MEQ, OSCE = [], []

LECTURE = {
 "lec": LEC, "date": "พื้นฐานสรีรวิทยา (ปรีคลินิก)",
 "title": "สรีรวิทยาไตพื้นฐาน I — การทำงานของไต GFR และการขนส่งในท่อไต",
 "subtitle": "หน้าที่ 7 ข้อของไต · RBF และ afferent/efferent · clearance (PAH, inulin, creatinine, eGFR) · filtration barrier · Starling forces · NSAID/ACEi/SGLT2i · autoregulation (myogenic, TGF) · filtration fraction และ glomerulotubular balance · PT (glucose Tm, Fanconi, acetazolamide) · loop/DT/CD + ยาขับปัสสาวะ + Bartter/Gitelman/Liddle · organic secretion · FE/FENa · countercurrent · Cosm/C_H₂O",
 "objectives": [
   "บอกหน้าที่ของไต 7 ข้อ และอธิบายอาการที่เกิดเมื่อหน้าที่แต่ละข้อเสียไป (azotemia, K สูง, ซีด, renal osteodystrophy, acidosis)",
   "อธิบายการควบคุม RBF ด้วย sympathetic, สาร vasoactive และ RAAS และคำนวณ ERPF/RPF/RBF จาก PAH clearance",
   "อธิบายโครงสร้าง filtration barrier ที่กั้นตามขนาดและประจุ และเชื่อมกับ proteinuria/hematuria",
   "คำนวณ NFP และ GFR จากแรง Starling และทำนายผลของการหด/ขยาย afferent และ efferent ต่อ RBF, GFR และ FF",
   "อธิบายกลไก hemodynamic AKI จาก NSAID และ ACEi/ARB และผลของ SGLT2 inhibitor ต่อ TGF",
   "อธิบาย autoregulation (myogenic, TGF), filtration fraction และ glomerulotubular balance",
   "อธิบายการขนส่ง Na K Ca Mg Pi HCO₃⁻ glucose และน้ำในแต่ละส่วนของ nephron และเชื่อมกับฤทธิ์ข้างเคียงของยาขับปัสสาวะและโรคของท่อไต",
   "อธิบายการหลั่ง organic anion/cation และ drug interaction ที่ท่อไต",
   "คำนวณและแปลผล clearance, FE (FENa), C_osm และ C_H₂O",
   "อธิบาย countercurrent mechanism และ urea recycling ในการทำปัสสาวะเข้มข้นและเจือจาง"],
 "nlGap": "",
 "guidelines": [],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบของข้อใหม่ (ทำก่อน publish ครั้งแรกเท่านั้น) — ข้อที่ตัวเลือกเรียงตามตัวเลขไม่สลับ
ORDERED = {N(5)}
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED or not it["id"].startswith("NEPH-PHY1-MCQ"):
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "nephro.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LEC]
data.insert(0, LECTURE)

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

# ผูกข้อ Mock (คลัง Ward Drill ชุด mock ที่ยังว่าง) — ลงเป็น kind "old"
from link_mock import link_mock
MOCK_MAP = {}
added_m = link_mock(SET, LEC, {k: v for k, v in MOCK_MAP.items() if any(s["id"] == k for s in S)})

from collections import Counter
newi = [i for s in L["sections"] for i in s["items"] if i["id"].startswith("NEPH-PHY1")]
print("sections %d | ข้อใหม่ %d | mock %d | meq %d | osce %d | figs %d | nl %d" % (
    len(S), len(newi), added_m, len(L["meq"]), len(L["osce"]), sum(len(s.get("figs") or {}) for s in S), len(codes)))
print("answer positions (ข้อใหม่):", dict(sorted(Counter(i["answer"] for i in newi).items())))
print("nephro.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
