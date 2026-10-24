#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common skin diseases for internists (อ.ภูริต ภูรีศรีศักดิ์ · Purit Pureesrisak, MD · Division of Dermatology รพ.ราชวิถี) → data/derm.json (ชุดใหม่ Derm)
ต้นฉบับ: Drive 1PWIdpHHF6dsoLSsPoJhJgsdE9mJWTzH8 "Lec นศพ ปี 4 (66).pdf" (140 หน้า ภาพสแกนจาก iPhone — ข้อความดึงได้น้อย อ่านจากภาพทุกหน้า)
โน้ตสไลด์: slides/derm66_notes.md · ภาพประกอบ: figs_derm.py (31 ภาพ)
lec = "Derm1" (ไม่มีคาบนี้ในคลัง Ward Drill · ไม่พบวันบรรยาย) · date "สไลด์ปี 2566 (อ.ภูริต)"
สไลด์มี: primary/secondary lesion · eczema (ระยะ การแบ่ง การรักษา) · AD · pityriasis alba · seborrheic · stasis · xerotic · dyshidrosis ·
nummular · prurigo nodularis · LSC · ACD/ICD · miliaria · urticaria/angioedema · STD (syphilis, chancroid, gonorrhoea/DGI, LGV) ·
leprosy (ภาพล้วน) · EM/SJS/TEN + SCORTEN · panniculitis/erythema nodosum
สไลด์ไม่มี/ล้าสมัย (เติมจากแนวทางและระบุในบทเรียน): กลไกโมเลกุล (filaggrin, IL-31, granulysin) · ความแรงของ steroid/FTU · eczema herpeticum ·
EAACI 2022 urticaria · CDC STI 2021 (ceftriaxone 500 mg, late latent, neurosyphilis, partner notification) · WHO leprosy 2018 (3 ยาทุกราย) ·
HLA-B1502/HLA-B5801 · ภาวะ angioedema จาก bradykinin
คลัง Ward Drill: ไม่มีคาบผิวหนัง · ผูก Mock exam ที่ตรงเรื่อง (MOCK-008 016 058 059 060)"""
import json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from svg import fig
import figs_derm as F
from link_mock import link_mock

SET, LEC = "derm", "Derm1"
SRC = "สไลด์ อ.ภูริต — Dermatology lecture for 4th year medical student Part 1"
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
N = lambda n: "DERM-D1-MCQ-%02d" % n
R = lambda p, *g: ["สไลด์ อ.ภูริต — " + p] + list(g)

# ─── รหัส นล.
RASH, ITCH, SUBQ, GU, LAD, FEVER, LEUK = "2.1.50", "2.1.51", "2.1.54", "2.1.48", "2.1.57", "2.1.1", "2.1.59"
ECZ, ECZ_B = "2.3.12(7)", "B4.2.2(11)"
URT, URT_B = "2.3.12(14)", "B4.2.2(12)"
DYSH, DYSH_B = "2.3.12(8)", "B4.2.2(14)"
EMEN, EMEN_B = "2.3.12-3(5)", "B4.2.2-3(7)"
LEP, LEP_B = "2.3.12-3(9)", "B4.2.2-3(1)"
SJS, SJS_B = "2.2.49", "B4.2.2(13)"
STI, STI_B, URETH, URETH_B = "2.3.1(19)", "B10.2.2(1)", "2.3.14(7)", "B10.2.2(4)"
ULC, ULC_B = "2.3.12(13)", "B4.2.3(4)"
PAPSQ, PAPSQ_B = "2.3.12-3(11)", "B4.2.2-3(8)"
HSV_B, VZV_B, BULL = "B4.2.2(5)", "B4.2.2(6)", "2.3.12-3(2)"
TINEA, SCAB, CELL, IMP = "2.3.12(11)", "2.3.12(10)", "2.3.12(4)", "2.3.12(9)"
SHOCK, ANAPH_B, HYPERS = "2.2.7", "B1.4.11(1)", "B1.4.11"
STRUCT, EPI, FUNC, AGE_SK = "B4.1.1(1)", "B4.1.1(2)", "B4.1.2(1)", "B4.1.3(2)"
EMOL, ANTIPRU, TCS, AH, CS, NSAID = "B4.4(1)", "B4.4(2)", "B4.4(7)", "B6.4(1)", "B1.7.4", "B5.4(1)"
ADR, ANTIMIC, PKSP = "B1.7.1(4)", "B1.7.2", "B1.7.1(3)"
KOH, KOH_B, TZ_B, GRAM, GRAM_B = "3.1.10", "B4.3(1)", "B4.3(2)", "3.1.9", "B1.5.2(5)"
SERO, SERO_B, SEROP, BX = "3.3.16", "B10.3(8)", "B1.5.1(8)", "B1.6.1(1)"
INFARTH, INFARTH_B = "2.3.13-3(6)", "B5.2.2-3(1)"
PNEURO, ENTRAP = "2.3.6-3(9)", "2.3.6-3(10)"
VASC = "2.3.13-3(16)"
PERINAT = "2.3.16-3(1)"

# ═════════════════════════════════════════════ 1
sec("derm-d1-01", "ภาษาของผิวหนัง (1): primary lesion — บอกชนิดจาก “ความลึก” และ “สิ่งที่อยู่ข้างใน”",
    "Macule/patch · papule/plaque · nodule · wheal · vesicle/bulla · pustule — เกณฑ์ 1 cm และกลไกที่ทำให้แต่ละชนิดหน้าตาต่างกัน", 9,
"""### โครงของคาบ (สไลด์)
อ.ภูริตเริ่มจากภาพตัดขวางผิวหนัง (epidermis · dermis · ไขมัน พร้อมต่อมเหงื่อ ต่อมไขมัน รูขุมขน เส้นประสาท หลอดเลือด) และต้นไม้แบ่งกลุ่มโรคผิวหนัง: **non-infectious inflammatory** (papulosquamous/eczematous · urticaria/erythema · autoimmune CTD · autoimmune bullous) · **infectious** (เชื้อรา โปรโตซัว แบคทีเรีย ไวรัส) · **neoplastic** · **อื่น ๆ** (metabolic/toxic · genodermatoses) แล้วไล่หัวข้อ: terminology → dermatitis/eczema → urticaria → dyshidrosis → miliaria → STD → leprosy → EM/SJS/TEN → erythema nodosum

> สไลด์ทั้งชุดเป็นภาพถ่ายผู้ป่วย บทเรียนนี้ **บรรยายรอยโรคเป็นคำ** แทนภาพ และใช้ภาพตัดขวางแบบแผนผัง (ไม่มีภาพถ่าย) · ✍️ = ลายมือที่จดในสไลด์ (สิ่งที่อาจารย์เน้นในห้อง)

### Primary lesion (สไลด์ “Primary lesion” 4 หน้า)
[[fig:primary]]
| ชนิด | นิยามในสไลด์ | อยู่ชั้นไหน / ข้างในคืออะไร | ตัวอย่างในสไลด์ |
|---|---|---|---|
| **Macule** | แบน ขอบเขตชัด **< 1 cm** สีเข้มขึ้น/ซีดลง หรือสีอื่น (ชมพู แดง ม่วง) | สีเปลี่ยนโดยไม่มีปริมาตรเพิ่ม (melanin, เลือด, หลอดเลือดขยาย) | ephelid (กระ), lentigo, petechiae, viral exanthem แบบแบน |
| **Patch** | แบน **> 1 cm** | เหมือน macule แต่ใหญ่ | vitiligo, melasma, Mongolian spot, café-au-lait |
| **Papule** | นูน **< 1 cm** — นูนเพราะ epidermis หนาขึ้น และ/หรือ มีเซลล์/สารสะสมใน dermis | เนื้อแน่น ไม่มีน้ำ | seborrheic keratosis (✍️ “กระเนื้อ”), cherry hemangioma, molluscum, wart, small-vessel vasculitis |
| **Plaque** | นูน **> 1 cm** | epidermis หนา (psoriasis ✍️ “สะเก็ดเงิน”, LSC, nummular) หรือ dermis หนา (granuloma annulare, sarcoidosis, keloid, morphea) | |
| **Nodule** | คลำได้ “**ปริมาตรมากกว่า papule**” (✍️ ขีดเน้น) มัก > 1 cm อยู่ใน dermis และ/หรือไขมัน ส่วนใหญ่อาจอยู่ใต้ผิว | ก้อนลึก — คลำชัดกว่ามองเห็น | epidermoid cyst, lipoma, metastasis, neurofibroma, **panniculitis เช่น erythema nodosum** |
| **Wheal** (✍️ ขีดเน้น) | นูน **ชั่วคราว** จาก **dermal edema** มักซีดกลาง ขอบแดง | ✍️ “บวมจาก dermis” | **urticaria** (✍️ “ลมพิษ”) |
| **Vesicle** | นูน **< 1 cm** (✍️ ขีดเน้น) น้ำใส อาจกลายเป็นหนอง บุ๋มกลาง หรือแตกเป็น erosion | ช่องน้ำในหรือใต้ epidermis | HSV, VZV, dermatitis herpetiformis, dyshidrotic eczema |
| **Bulla** | **> 1 cm** (✍️ ขีดเน้น) น้ำใส | | friction blister, bullous pemphigoid, bullous FDE, coma bullae |
| **Pustule** (✍️ “ตุ่มหนอง”) | มัก < 1 cm มีหนอง | ตามรูขุมขน (folliculitis, acne) หรือไม่ตามรูขุมขน (pustular psoriasis, AGEP) | |

#### ทำไมถึงมีอาการนี้ — หน้าตาของรอยโรคบอกกลไก
| ลักษณะ | กลไก | ใช้อย่างไร |
|---|---|---|
| แบน คลำไม่ได้ | สีเปลี่ยนจาก melanin, hemoglobin หรือหลอดเลือดขยาย โดยไม่มีเซลล์หรือน้ำเพิ่ม | กดด้วยแผ่นใส (**diascopy**): ผื่นแดงจากหลอดเลือดขยายจะจาง · **purpura (เลือดออกนอกหลอดเลือด) กดไม่จาง** → คิดถึง vasculitis/เกล็ดเลือดต่ำ (ข้อมูลเสริม) |
| นูนเนื้อแน่น | epidermis แบ่งตัวมากขึ้น (psoriasis, wart) หรือเซลล์อักเสบ/เนื้องอก/สารสะสมใน dermis | papule/plaque — ดูผิวด้านบนต่อว่ามี scale หรือไม่ |
| นูนชั่วคราวแล้วย้ายที่ | plasma รั่วออกจาก venule ใน dermis บนแล้วถูกดูดกลับในไม่กี่ชั่วโมง | wheal = ลมพิษ — **ดูที่ “เวลา”** มากกว่ารูปร่าง (หัวข้อ 11) |
| ตุ่มน้ำ | เซลล์ epidermis แยกจากกัน: น้ำแทรกระหว่างเซลล์ (spongiosis — eczema), เซลล์หลุดจากกัน (acantholysis — pemphigus), หรือแยกที่รอยต่อกับ dermis (pemphigoid, TEN) | ยิ่งแยกตื้น หลังคายิ่งบาง ตุ่มยิ่งหย่อนและแตกง่าย |
| ตุ่มหนอง | neutrophil สะสม — **ไม่จำเป็นต้องเป็นการติดเชื้อ** (pustular psoriasis, AGEP ปลอดเชื้อ) | ตามรูขุมขนหรือไม่ บอกกลุ่มโรค |
| ก้อนลึก | เซลล์/สารอยู่ใน dermis ล่างหรือไขมัน — ผิวบนปกติหรือแดงเล็กน้อย | ต้อง **คลำ** เสมอ (erythema nodosum กดเจ็บ) |

[[fig:tree]]
""",
    ["แบน = macule (< 1 cm) / patch (> 1 cm) · นูนเนื้อแน่น = papule / plaque · ลึก = nodule",
     "น้ำใส = vesicle (< 1 cm) / bulla (> 1 cm) · หนอง = pustule",
     "Wheal = dermal edema ชั่วคราว (✍️ “บวมจาก dermis” = ลมพิษ) — แยกจาก plaque ด้วย “เวลา”",
     "คลำทุกรอยโรค: นูนเล็กน้อยมองไม่เห็น · ก้อนลึก · กดเจ็บ · กดแล้วจาง (diascopy)"],
    [mcq(N(1), "A 25-year-old woman has a 2-day history of intensely itchy, pink, raised, flat-topped lesions 1–4 cm in size on the trunk and arms. Several lesions have a pale centre. She notices that each lesion disappears within a few hours while new ones appear elsewhere. There is no scale, crust, or vesicle. Which term best describes the primary lesion?",
         ["Wheal", "Plaque", "Papule", "Nodule", "Patch"], 0,
         "นูน แดงรอบ ซีดกลาง **หายเองในไม่กี่ชั่วโมงแล้วไปขึ้นที่ใหม่** = **wheal** (dermal edema ชั่วคราว — ✍️ “บวมจาก dermis”) ซึ่งเป็นรอยโรคของลมพิษ · ลักษณะที่ใช้แยกคือ “ความไม่คงที่” ไม่ใช่ขนาด\n\n"
         "- **Plaque** — นูน > 1 cm แต่ **คงที่** เป็นวันถึงเดือน (เช่น psoriasis)\n- **Papule** — นูน < 1 cm และคงที่\n"
         "- **Nodule** — ก้อนลึกใน dermis/ไขมัน คลำได้มากกว่าเห็น\n- **Patch** — แบน คลำไม่ได้",
         "นูน + หายใน < 24 ชม. + ย้ายที่ = wheal", "Primary lesion — wheal", R("Primary lesion (wheal)"), [RASH, URT, STRUCT]),
     mcq(N(2), "A 30-year-old man has a 3-cm, flat, non-palpable, sharply demarcated area of complete depigmentation on the dorsum of his left hand. There is no scale or change in skin texture, and sensation is normal. Which term best describes this primary lesion?",
         ["Patch", "Macule", "Plaque", "Atrophy", "Erosion"], 0,
         "แบน คลำไม่ได้ ขนาด **> 1 cm** = **patch** (สไลด์ยกตัวอย่าง vitiligo) · ความรู้สึกปกติช่วยตัด leprosy ที่เป็นผื่นซีดแบบ “ชา” (หัวข้อ 16)\n\n"
         "- **Macule** — แบนเหมือนกันแต่ < 1 cm\n- **Plaque** — ต้องนูน\n"
         "- **Atrophy** — ผิวบาง เหี่ยว มันวาวหรือยุบ (secondary change) ไม่ใช่แค่สีเปลี่ยน\n- **Erosion** — ผิวหลุดบางส่วน ชื้น ไม่ใช่ผิวปกติที่สีเปลี่ยน",
         "แบน > 1 cm = patch · แบน < 1 cm = macule", "Primary lesion — patch", R("Primary lesion (macule/patch)"), [RASH, STRUCT]),
     mcq(N(3), "A 78-year-old bedridden woman has several tense, dome-shaped blisters 2–3 cm in diameter filled with clear fluid on the lower legs and trunk. Which term best describes these primary lesions, and at what level is the split most likely to be?",
         ["Bullae — split beneath the epidermis (subepidermal)", "Vesicles — split within the stratum corneum", "Pustules — collection of neutrophils within the epidermis",
          "Wheals — oedema of the upper dermis", "Nodules — inflammation of the subcutaneous fat"], 0,
         "ตุ่มน้ำใส **> 1 cm** = **bulla** · ตุ่มที่ **ตึง (tense)** ไม่แตกง่ายบอกว่าหลังคาหนา = แยก **ใต้ epidermis ทั้งชั้น** (เช่น bullous pemphigoid ในผู้สูงอายุ ซึ่งสไลด์ยกเป็นตัวอย่างของ bulla) · ถ้าแยกตื้นในชั้น epidermis หลังคาจะบางและหย่อน แตกง่าย (pemphigus)\n\n"
         "- **Vesicle** — < 1 cm และการแยกในชั้นขี้ไคลจะบางมาก\n- **Pustule** — ข้างในเป็นหนอง ไม่ใช่น้ำใส\n"
         "- **Wheal** — ไม่มีช่องน้ำ เป็นการบวมของ dermis\n- **Nodule** — ก้อนเนื้อแน่น ไม่ใช่ตุ่มน้ำ",
         "ตุ่มน้ำ > 1 cm = bulla · ตึง = แยกลึก (subepidermal)", "Primary lesion — bulla", R("Primary lesion (vesicle/bulla)"), [RASH, BULL, EPI])],
    [RASH, STRUCT, EPI, FUNC], {"primary": F.primary(), "tree": F.lesion_tree()},
    source="สไลด์ อ.ภูริต — skin anatomy · classification tree · Primary lesion (หน้า 2–8)")

# ═════════════════════════════════════════════ 2
sec("derm-d1-02", "ภาษาของผิวหนัง (2): secondary lesion และการบรรยายรอยโรคเป็นประโยค",
    "Crust · scale · fissure · erosion vs ulcer · excoriation · atrophy · lichenification · 5 ขั้นการบรรยาย · ฝึกจากภาพในสไลด์", 9,
"""### Secondary lesion (สไลด์ “Secondary lesion” 3 หน้า)
[[fig:secondary]]
| ชนิด | นิยามในสไลด์ | ✍️ / ตัวอย่าง |
|---|---|---|
| **Crust** | น้ำเหลือง เลือด หรือหนองที่แห้งบนผิว อาจมีแบคทีเรีย (มักเป็น Staphylococcus) | ✍️ “สะเก็ด” · “สะเก็ดน้ำเหลือง” — eczema, impetigo, HSV/VZV ระยะท้าย, EM |
| **Scale** | hyperkeratosis — ขี้ไคลสะสมจากการแบ่งตัวมากขึ้นและ/หรือหลุดช้า | ชนิดของขุยช่วยวินิจฉัย: psoriasis (micaceous สีเงินหนา) · tinea (leading scale ที่ขอบ) · EAC (trailing scale) · actinic keratosis (สาก) · pityriasis rosea (collarette) |
| **Fissure** | รอยแยกเป็นเส้น มักเจ็บ จากผิวแห้ง หนา ไม่ยืดหยุ่น | angular cheilitis, hand dermatitis |
| **Erosion** | **เสีย epidermis บางส่วน** (✍️ ขีดเน้น) | impetigo, แรงเสียดสี, pemphigus |
| **Ulceration** | **เสีย epidermis ทั้งชั้น** (✍️ ขีดเน้น) อาจลึกถึง dermis หรือไขมัน | ecthyma, pyoderma gangrenosum, stasis ulcer, neuropathic ulcer |
| **Excoriation** | บาดแผลจากภายนอก (การเกา) ต่อ epidermis | ✍️ “รอยเกา” — โรคที่คัน (AD, แมลงกัด), neurotic excoriation |
| **Atrophy** | epidermis บาง เหี่ยว มันวาว / dermis ยุบ (collagen, elastin หาย) | ✍️ “ดูฝ่อ” — lichen sclerosus, **striae จาก steroid แรง** |
| **Lichenification** | epidermis หนา (acanthosis) ลายผิวชัดขึ้น | ✍️ “ผิวหนังหนาขึ้น สีคล้ำขึ้น skin fissure ดูมากขึ้นชัดขึ้น” — LSC, AD |

สไลด์สรุปด้วยตาราง “The lesions of the skin” แบ่งเป็น **นูน** (papule plaque nodule cyst wheal scar …) · **บุ๋ม** (erosion ulcer atrophy striae burrow …) · **แบน** (macule patch erythema erythroderma) · **เปลี่ยนที่ผิว** (scale crust excoriation fissure lichenification eschar) · **มีน้ำ** (vesicle bulla pustule furuncle abscess) · **หลอดเลือด** (purpura telangiectasia infarct)

#### ทำไมถึงมีอาการนี้
| ลักษณะ | กลไก | ใช้ทางคลินิก |
|---|---|---|
| Erosion หายไม่เป็นแผลเป็น | ยังเหลือ basal layer และเซลล์ต้นกำเนิดในรูขุมขน → epidermis งอกคลุมใหม่ได้ | แผลตื้นจาก pemphigus, impetigo, ตุ่มน้ำแตก |
| Ulcer หายเป็นแผลเป็น | dermis ถูกทำลาย → fibroblast สร้าง collagen ใหม่แทน | หาสาเหตุ: หลอดเลือด (stasis, arterial), เส้นประสาท (เบาหวาน, **เรื้อน**), ติดเชื้อ, มะเร็ง |
| Crust สีเหลืองน้ำผึ้ง | serum ที่ซึมออกแห้งพร้อมแบคทีเรีย | ผื่น eczema ที่มี crust เหลือง → คิดถึง **ติดเชื้อแทรก** (impetiginization) |
| Lichenification | เกา/ถูซ้ำ → keratinocyte แบ่งตัวป้องกันตัว melanin เพิ่ม | บอกว่า **คันและเรื้อรัง** — eczema ระยะ chronic (หัวข้อ 3) |
| Koebner phenomenon | การบาดเจ็บของผิว (รอยเกา) กระตุ้นให้โรคขึ้นตามรอยนั้นในคนที่มีโรคอยู่ | ✍️ “lichen planus in linear pattern” (สไลด์หน้า 14) — พบใน psoriasis, LP, vitiligo |

### บรรยายรอยโรคอย่างไร (ภาคปฏิบัติ)
[[fig:describe]]
**แม่แบบประโยค**: [จำนวน] + [ชนิด primary lesion] + [ขนาด] + [สี] + [ขอบ] + [secondary change] + [การเรียงตัว] + [ตำแหน่ง/การกระจาย] + [ผลการคลำ]

### ฝึกจากภาพในสไลด์ (หน้า 13–16)
| ภาพ | บรรยายเป็นคำ | ✍️ / คำตอบ |
|---|---|---|
| หน้า 13 หลัง | กลุ่มตุ่มน้ำใสหลายเม็ดบนฐานแดง เรียงเป็นแถบด้านเดียวของหลัง | ✍️ “Group of vesicle on erythematous base” · ✍️ เขียน “Herpes simplex” — กลุ่มตุ่มน้ำบนฐานแดงเป็นลักษณะของ **ไวรัสกลุ่ม herpes** ถ้าเรียงตาม dermatome ข้างเดียวแบบภาพนี้ = **herpes zoster** (ผู้เขียนบทเรียนเห็นว่าภาพเข้ากับ zoster มากกว่า) |
| หน้า 14 ลำตัว | papule ม่วงหัวแบนเรียงเป็นเส้นตรงตามรอยข่วน | ✍️ “lichen planus in linear pattern” = **Koebner (isomorphic) phenomenon** |
| หน้า 15 หลังมือ | plaque แดงขอบชัดหลายแผ่น ปกคลุมด้วยขุยหนาสีเงิน | psoriasis (papulosquamous) |
| หน้า 16 “Diagnosis?” มือ | ผื่นแดง ขอบไม่ชัด ผิวหยาบ มีขุยและสะเก็ดบนหลังมือ คนไข้เกา | ✍️ “ดูคัน (itching, pruritus)” + ✍️ “ดูสาก → epidermal change” = สองคำใบ้ของ **eczema** (hand dermatitis) |
""",
    ["Erosion = เสียบางส่วนของ epidermis (หายไม่เป็นแผลเป็น) · Ulcer = เสียทั้งชั้นถึง dermis (เป็นแผลเป็น)",
     "Crust (✍️ สะเก็ดน้ำเหลือง) สีเหลืองบน eczema → คิดถึงติดเชื้อแทรก",
     "Lichenification (✍️ หนา คล้ำ ลายผิวชัด) = เกามานาน",
     "Koebner: รอยโรคขึ้นตามรอยบาดเจ็บ — psoriasis, lichen planus, vitiligo",
     "บรรยาย: ตำแหน่ง → การเรียงตัว → ชนิด/ขนาด/สี/ขอบ → secondary change → คลำ"],
    [mcq(N(4), "A 45-year-old man with pemphigus vulgaris has several moist, red, shallow, denuded areas on the trunk where blisters had been. The base is glistening and does not extend into the dermis. When they heal, what is expected and what is the correct term for these lesions?",
         ["Erosions — they heal without scarring", "Ulcers — they heal with scarring", "Fissures — they heal with hyperpigmented lines",
          "Excoriations — they heal with lichenification", "Atrophy — the skin remains thin and shiny"], 0,
         "ผิวหลุดตื้น ชื้น เสียแค่ **บางส่วนของ epidermis** = **erosion** (✍️ “partial loss of the epidermis”) — เพราะ basal layer และเซลล์ต้นกำเนิดในรูขุมขนยังอยู่ ผิวจึงงอกคลุมใหม่ **ไม่เป็นแผลเป็น** · สไลด์ยก pemphigus เป็นตัวอย่างของ erosion\n\n"
         "- **Ulcer** — เสียทั้งชั้นลงถึง dermis จึงเป็นแผลเป็น\n- **Fissure** — รอยแยกเป็นเส้น ไม่ใช่บริเวณกว้าง\n"
         "- **Excoriation** — รอยเกาเป็นเส้นตามเล็บ\n- **Atrophy** — ผิวบางลงแต่ยังคลุมอยู่ ไม่ใช่ผิวหลุด",
         "Erosion ไม่เป็นแผลเป็น · ulcer เป็นแผลเป็น", "Secondary lesion — erosion vs ulcer", R("Secondary lesion (erosion/ulceration)"), [RASH, BULL, ULC]),
     mcq(N(5), "A 40-year-old man has itchy, flat-topped, violaceous papules on the wrists. On the flank, identical papules are arranged in a straight line exactly along a recent scratch mark. Which phenomenon is shown, and in which disease is it characteristic?",
         ["Koebner (isomorphic) phenomenon — lichen planus", "Nikolsky sign — pemphigus vulgaris", "Auspitz sign — tinea corporis",
          "Dermatographism — scabies", "Pathergy — seborrheic dermatitis"], 0,
         "รอยโรคเดียวกับโรคเดิม **ขึ้นตามแนวบาดเจ็บ** = **Koebner (isomorphic) phenomenon** — สไลด์หน้า 14 (✍️ “lichen planus in linear pattern”) · พบใน lichen planus, psoriasis, vitiligo\n\n"
         "- **Nikolsky** — ถูผิวแล้วหนังกำพร้าเลื่อนหลุด (pemphigus, SJS/TEN)\n- **Auspitz** — ขูดขุย psoriasis แล้วมีจุดเลือดออก ไม่เกี่ยวกับ tinea\n"
         "- **Dermatographism** — ขีดผิวแล้วเป็น wheal เป็นเส้น (ลมพิษชนิด physical) ไม่ใช่ papule ม่วงที่คงอยู่\n- **Pathergy** — ตุ่มหนองหลังเข็มแทง (Behçet, pyoderma gangrenosum)",
         "รอยโรคเดิมขึ้นตามรอยข่วน = Koebner (LP, psoriasis, vitiligo)", "Configuration — Koebner phenomenon", R("หน้า 14 Koebnerization of lichen planus"), [RASH, PAPSQ, PAPSQ_B])],
    [RASH, ITCH, ULC, PAPSQ, STRUCT], {"secondary": F.secondary(), "describe": F.describe()},
    source="สไลด์ อ.ภูริต — Secondary lesion · Table 5-1 · ภาพฝึกบรรยาย (หน้า 9–16)")

# ═════════════════════════════════════════════ 3
sec("derm-d1-03", "Eczema/dermatitis — นิยาม 3 ระยะ และการแบ่ง endogenous/exogenous",
    "คัน + แดง + ขุย + ตุ่มน้ำเล็ก · acute → subacute → chronic (spongiosis → lichenification) · โรคที่ต้องแยก", 9,
"""### นิยาม (สไลด์)
- **Eczema และ dermatitis มีความหมายเดียวกัน** = การอักเสบของ epidermis และ dermis
- ทุกโรคในกลุ่มนี้มีสามอย่างร่วมกัน: **คัน (pruritus) · อักเสบ · barrier ของผิวเสีย**
- ลักษณะทางคลินิก: “inflammation of the skin characterised by **itching, redness, scaling and clustered papulovesicles**”
- ✍️ ภาพ “Diagnosis?” หน้า 16: “**ดูคัน**” + “**ดูสาก → epidermal change**” — ผื่นที่คันและมีการเปลี่ยนแปลงของผิวด้านบน (ขุย สาก ซึม) คือคำใบ้แรกของ eczema · ต่างจากลมพิษที่คันแต่ผิวด้านบนเรียบ

### 3 ระยะ (สไลด์ Stages of eczema)
[[fig:stages]]
| ระยะ | สิ่งที่เห็น (สไลด์) | สิ่งที่เกิดในผิว |
|---|---|---|
| **Acute** | erythema, papule เล็ก ๆ, **vesicle ที่แตก → ซึม (oozing) และสะเก็ด** | spongiosis — น้ำแทรกระหว่าง keratinocyte จนเป็นตุ่มน้ำเล็ก |
| **Subacute** | บวมและตุ่มน้ำลดลง เหลือ papule, erythema และขุยบ้าง | parakeratosis (เซลล์สร้างเร็วจนนิวเคลียสค้าง) |
| **Chronic** | ไม่ซึม ไม่มีสะเก็ด ผิว **แห้ง มีขุย อาจแตก** · เกาซ้ำ → **lichenification** = หนา hyperkeratosis สีคล้ำ ลายผิวชัด | acanthosis + hyperkeratosis + melanin เพิ่ม |

> ระยะไม่ได้บอกชนิดของโรค — eczema ทุกชนิดผ่านได้ทั้งสามระยะ และผื่นคนเดียวกันอาจมีหลายระยะพร้อมกัน แต่ระยะ **กำหนดยาพื้น (vehicle)** ที่ต้องใช้ (หัวข้อ 4)

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกโรค/รักษาอย่างไร |
|---|---|---|
| คัน | cytokine ชนิด Th2 โดยเฉพาะ **IL-31** กระตุ้นปลายประสาทคันโดยตรง + ผิวแห้ง · histamine มีบทบาทน้อย | antihistamine ช่วยได้น้อย (ช่วยให้หลับเท่านั้น) — ต่างจากลมพิษ (ข้อมูลเสริม) |
| ซึม (oozing) | spongiosis → ตุ่มน้ำเล็กแตก → serum ไหลออก | ระยะ acute — ใช้ wet compress/ยาพื้นที่ไม่ปิดผิว |
| สะเก็ดเหลือง | serum แห้ง ± S. aureus | crust เหลืองน้ำผึ้งมาก/มีหนอง → ติดเชื้อแทรก |
| ขุย | keratinocyte สร้างเร็วและหลุดผิดปกติ | ระยะ subacute/chronic |
| ผิวหนาลายชัด สีคล้ำ | เกาซ้ำ → acanthosis + post-inflammatory hyperpigmentation | ✍️ “ผิวหนาขึ้น สีคล้ำขึ้น” — chronic |
| ขอบไม่ชัด | การอักเสบกระจายในชั้นผิวโดยไม่มีขอบเขตของเชื้อหรือ plaque ที่ชัด | ต่างจาก psoriasis (ขอบชัด ขุยหนาสีเงิน) และ tinea (ขอบนูนชัด กลางจาง) |

### การแบ่งกลุ่ม (สไลด์ Classification of eczema)
| Endogenous (เกิดจากในตัว) | Exogenous (เกิดจากสิ่งภายนอก) |
|---|---|
| Atopic · Seborrheic · Discoid (nummular) · Pityriasis alba · Stasis · Asteatotic/xerotic (✍️ “แห้ง”) · Dyshidrosis/pompholyx (✍️ “มาเป็นตุ่มน้ำ”) · Prurigo nodularis · Lichen simplex chronicus | Irritant contact dermatitis · Allergic contact dermatitis · Photodermatitis |

### โรคที่ต้องแยกจาก eczema (ข้อมูลเสริม — ไม่อยู่ในสไลด์)
| โรค | ต่างอย่างไร | ตรวจ |
|---|---|---|
| Tinea (dermatophyte) | ขอบนูนชัดมีขุยที่ขอบ (leading scale) กลางจาง ข้างเดียวหรือไม่สมมาตร | **KOH** ก่อนทา steroid (steroid ทำให้ tinea ลาม = tinea incognito) |
| Psoriasis | plaque ขอบชัด ขุยหนาสีเงิน ข้อศอก เข่า หนังศีรษะ | ประวัติครอบครัว · Auspitz |
| Scabies | คันกลางคืน ซอกนิ้ว ข้อมือ อวัยวะเพศ คนในบ้านเป็นด้วย | ขูดหาตัวไร |
| Mycosis fungoides | “eczema” ในผู้ใหญ่/สูงอายุที่ไม่หายด้วย steroid ที่บริเวณไม่โดนแดด | **biopsy** |
""",
    ["Eczema = dermatitis: คัน + อักเสบ + barrier เสีย · ✍️ “ดูคัน + ดูสาก (epidermal change)”",
     "Acute = ตุ่มน้ำเล็ก ซึม สะเก็ด (spongiosis) · Subacute = ขุย · Chronic = แห้ง แตก lichenification",
     "ระยะไม่ได้บอกโรค แต่บอกยาพื้น: เปียกใช้แห้ง · แห้งใช้มัน",
     "Endogenous 9 โรค vs exogenous 3 โรค (ICD · ACD · photodermatitis)",
     "Eczema ข้างเดียว ขอบนูนชัด → KOH หา tinea ก่อนให้ steroid"],
    [mcq(N(6), "Three days after wearing new rubber boots, a 35-year-old man develops intensely itchy erythema on the dorsa of both feet with tiny clustered vesicles, oozing, and yellowish crusts. A skin biopsy is taken. Which histological finding is most characteristic of this stage?",
         ["Spongiosis with intraepidermal vesicles", "Acanthosis with compact hyperkeratosis", "Acantholysis with suprabasal cleft",
          "Interface dermatitis with necrotic keratinocytes", "Septal panniculitis with giant cells"], 0,
         "ตุ่มน้ำเล็กเป็นกลุ่ม ซึม และสะเก็ด = **acute eczema** (ที่นี่น่าจะเป็น allergic contact dermatitis ต่อยาง) · พยาธิสภาพหลักของ eczema ระยะเฉียบพลันคือ **spongiosis** — น้ำแทรกระหว่าง keratinocyte จนกลายเป็นตุ่มน้ำเล็กในชั้น epidermis\n\n"
         "- **Acanthosis + hyperkeratosis** — ระยะ chronic (lichenification)\n- **Acantholysis** — pemphigus (เซลล์หลุดจากกันเพราะ autoantibody ต่อ desmoglein)\n"
         "- **Interface dermatitis** — lichen planus, EM, SJS/TEN\n- **Septal panniculitis** — erythema nodosum",
         "Acute eczema = spongiosis → vesicle → ooze", "Stages of eczema — histology", R("Stages of eczema"), [ECZ, ECZ_B, BX]),
     mcq(N(7), "Which of the following is classified as an exogenous eczema in the lecture?",
         ["Irritant contact dermatitis", "Atopic dermatitis", "Seborrheic dermatitis", "Nummular (discoid) eczema", "Stasis dermatitis"], 0,
         "สไลด์แบ่ง exogenous eczema = ผื่นจากสิ่งภายนอก 3 โรค: **irritant contact dermatitis · allergic contact dermatitis · photodermatitis** · ที่เหลือ (atopic, seborrheic, nummular, pityriasis alba, stasis, asteatotic, dyshidrosis, prurigo nodularis, LSC) เป็น **endogenous**\n\n"
         "- **Atopic** — barrier + Th2 จากพันธุกรรม\n- **Seborrheic** — ✍️ “endogenous eczema” ตอบสนองต่อ Malassezia ในคนที่ไว\n"
         "- **Nummular** — ไม่ทราบสาเหตุชัด\n- **Stasis** — จากความดันหลอดเลือดดำในตัว (แม้อาจมี ACD ซ้อนได้)",
         "Exogenous = ICD · ACD · photodermatitis", "Classification of eczema", R("Classification of eczema"), [ECZ, ECZ_B])],
    [ECZ, ECZ_B, ITCH, RASH, TINEA, KOH], {"stages": F.eczema_stages()},
    source="สไลด์ อ.ภูริต — Eczema/Dermatitis · Stages · Classification (หน้า 16–24)")

# ═════════════════════════════════════════════ 4
sec("derm-d1-04", "รักษา eczema — วงจรคัน-เกา บันไดการรักษา ยาพื้น และความแรงของ steroid",
    "Emollient เป็นฐาน · topical steroid ตามระยะ/ตำแหน่ง · TCI · phototherapy · systemic ระยะสั้น · ✍️ ฟอกสบู่", 10,
"""### วงจร eczema (สไลด์ “The eczema cycle” และ “Breaking the eczema cycle”)
[[fig:cycle]]
- ✍️ จุดเริ่มคือ **“ฟอกสบู่”** → barrier เสีย → เสียน้ำ → สิ่งระคายและแบคทีเรียแทรก → อักเสบ + **คัน** (✍️) → **เกา** (✍️) → barrier แย่ลงอีก
- จุดตัดวงจรในสไลด์: **moisturizer** (“more vaseline” — ยิ่งเนื้อมันข้นยิ่งเก็บน้ำได้ดี) · **bleach bath** (ลดแบคทีเรีย) · **steroid** (“No inflammation = no itchiness = no scratching”) · healing

### การรักษาในสไลด์ (Treatment of eczema)
[[fig:ladder]]
1. **แก้สาเหตุ**: เลี่ยงสาร sensitizer และตัวทำละลาย รักษา varicose vein แหล่งติดเชื้อ เลี่ยงน้ำร้อน
2. **ยาปฏิชีวนะ broad-spectrum** ถ้ามีติดเชื้อแทรก
3. **Oral antihistamine**
4. **Topical corticosteroid** (✍️ ขีดเน้น) ความแรงเหมาะกับอายุและตำแหน่ง วันละ 2 ครั้งเป็นวัน ๆ — **cream ใช้ acute/subacute · ointment ใช้ผื่นแห้งเรื้อรัง**
5. **Emollient** เช่น vaseline ในผิวแห้งและผื่นเรื้อรัง
6. **Topical immunomodulator**: tacrolimus 0.03% ointment หรือ pimecrolimus 1% cream วันละ 2 ครั้ง
7. **Systemic steroid ระยะสั้น** เฉพาะ acute รุนแรงและกระจาย
8. **Phototherapy**: PUVA, narrowband UVB

#### ทำไมต้องเลือกยาพื้นตามระยะ
| ระยะ | ยาพื้น | เหตุผล |
|---|---|---|
| Acute ซึมมาก | **wet compress** (NSS) 15–20 นาที แล้ว cream/lotion | น้ำระเหยช่วยเย็น ลดคัน ล้างน้ำเหลือง · ยาพื้นมันจะปิดทับน้ำเหลืองและเปื่อย |
| Subacute | **cream** | กึ่งน้ำกึ่งมัน ทาง่าย ไม่เหนอะ |
| Chronic แห้ง หนา | **ointment** | ปิดผิว (occlusive) เก็บน้ำ และทำให้ยาซึมผ่านขี้ไคลหนาได้มากขึ้น |

### ความแรงของ steroid ตามตำแหน่ง (ข้อมูลเสริม — สไลด์บอกแค่ “ตามอายุและตำแหน่ง”)
[[fig:site]]
| ความแรง | ตัวอย่าง | ใช้ที่ |
|---|---|---|
| อ่อน | hydrocortisone 1–2.5%, desonide | หน้า เปลือกตา อวัยวะเพศ ข้อพับ เด็กเล็ก |
| กลาง | triamcinolone acetonide 0.1%, betamethasone valerate 0.1% | ลำตัว แขนขา |
| แรง–แรงมาก | betamethasone dipropionate 0.05%, clobetasol propionate 0.05% | ฝ่ามือ ฝ่าเท้า ผื่นหนา lichenified (ระยะสั้น) |

- ผลข้างเคียงเฉพาะที่: **atrophy, striae** (ภาพ striae ในสไลด์ secondary lesion), telangiectasia, perioral dermatitis, acne, ทำให้ tinea ลาม · ผลทั้งร่างกายเมื่อทาแรงกว้างนาน (โดยเฉพาะเด็ก): กด HPA axis
- **TCI** (tacrolimus, pimecrolimus) ไม่ทำให้ผิวบาง → เหมาะหน้า เปลือกตา ข้อพับ และใช้ระยะยาวแบบสัปดาห์ละ 2 ครั้งกันกำเริบ · ผลข้างเคียงหลัก: แสบร้อนช่วงแรก
- **Systemic steroid**: ให้สั้นเท่านั้น — หยุดแล้วผื่นมักกำเริบแรงกว่าเดิม (rebound) จึงไม่ใช้คุมระยะยาว (AAD 2023/EuroGuiDerm 2022)
- **Antihistamine**: ชนิดง่วง (chlorpheniramine, hydroxyzine) ก่อนนอนช่วยให้หลับและเกาน้อยลง · ชนิดไม่ง่วงแทบไม่ลดคันจาก eczema
""",
    ["ฐานบันได = emollient + เลี่ยงสบู่แรง/น้ำร้อน (✍️ ฟอกสบู่ = จุดเริ่มของวงจร)",
     "Cream = acute/subacute · ointment = แห้งเรื้อรัง · ซึมมาก → wet compress ก่อน",
     "ความแรงตามตำแหน่ง: หน้า/ข้อพับ/อวัยวะเพศ อ่อน · ฝ่ามือฝ่าเท้า/ผื่นหนา แรง",
     "TCI = ไม่ทำให้ผิวบาง → เปลือกตา หน้า ระยะยาว",
     "Systemic steroid เฉพาะระยะสั้นในรายรุนแรง — ระวัง rebound"],
    [mcq(N(8), "A 48-year-old construction worker has a 2-year history of thick, dry, lichenified, fissured plaques on both palms that itch intensely. KOH examination is negative. Which topical regimen is most appropriate initially?",
         ["Clobetasol propionate 0.05% ointment twice daily for 2–3 weeks plus a greasy emollient",
          "Hydrocortisone 1% cream twice daily", "Betamethasone valerate 0.1% lotion once daily",
          "Mupirocin ointment three times daily", "Tacrolimus 0.03% ointment as monotherapy"], 0,
         "ผื่น **chronic** (หนา แห้ง แตก lichenified) ที่ **ฝ่ามือ** (ขี้ไคลหนามาก ดูดซึมยาได้น้อย) → ต้องใช้ steroid **แรงมาก** ในยาพื้น **ointment** (สไลด์: ointment สำหรับผื่นแห้งเรื้อรัง) ระยะสั้น ร่วมกับ emollient มัน ๆ\n\n"
         "- **Hydrocortisone 1% cream** — อ่อนเกินไปสำหรับฝ่ามือ ใช้ที่หน้า/ข้อพับ\n- **Lotion** — ยาพื้นน้ำ เหมาะหนังศีรษะ/ผื่นซึม ไม่ใช่ผื่นหนาแห้ง\n"
         "- **Mupirocin** — ใช้เมื่อมีติดเชื้อแทรก ไม่รักษาการอักเสบ\n- **Tacrolimus 0.03%** — ความแรงต่ำ ไม่พอสำหรับผื่นหนาที่ฝ่ามือในระยะแรก",
         "ผื่นหนาแห้งที่ฝ่ามือ = steroid แรง + ointment", "Topical steroid potency and vehicle", R("Treatment of eczema", "AAD/EuroGuiDerm eczema guideline"), [ECZ, TCS, EMOL]),
     mcq(N(9), "A 32-year-old woman with atopic dermatitis has recurrent eczema of both upper eyelids. She has used a medium-potency steroid cream intermittently for a year and now has mild skin thinning. Which is the most appropriate long-term topical treatment?",
         ["Tacrolimus ointment twice daily, then twice weekly for maintenance", "Clobetasol propionate 0.05% cream daily for 3 months",
          "Betamethasone dipropionate 0.05% ointment twice daily", "Ketoconazole 2% cream twice daily", "Oral prednisolone 30 mg/day for 4 weeks"], 0,
         "เปลือกตาเป็นผิวบางที่ดูดซึม steroid มาก และเริ่มมีผิวบาง → เลือก **topical calcineurin inhibitor** (tacrolimus/pimecrolimus — สไลด์ topical immunomodulators) ซึ่ง **ไม่ทำให้ผิวบาง** ใช้ระยะยาวได้ และใช้แบบสัปดาห์ละ 2 ครั้งเพื่อกันกำเริบ (proactive)\n\n"
         "- **Clobetasol / betamethasone dipropionate** — แรงเกินไปสำหรับเปลือกตา เสี่ยง atrophy ต้อหิน ต้อกระจก\n- **Ketoconazole** — สำหรับ seborrheic dermatitis/เชื้อรา ไม่ใช่ AD\n"
         "- **Oral prednisolone 4 สัปดาห์** — systemic steroid ใช้ระยะสั้นในรายรุนแรงกระจายเท่านั้น และ rebound เมื่อหยุด",
         "เปลือกตา/หน้า ระยะยาว = TCI", "Topical calcineurin inhibitors", R("Treatment of eczema (topical immunomodulators)"), [ECZ, ECZ_B, TCS, CS]),
     mcq(N(10), "A 26-year-old man develops acute contact dermatitis on the forearm with weeping vesicles and serous exudate. Which initial local measure is most appropriate?",
         ["Cool saline wet compresses for 15–20 minutes followed by a mid-potency steroid cream", "Thick petrolatum ointment under occlusion",
          "Topical neomycin ointment", "Hot water soaks to dry the lesions", "Oral prednisolone 1 mg/kg tapered over 3 weeks without topical therapy"], 0,
         "ผื่น **acute ซึมมาก** → หลัก “**เปียกใช้แห้ง**”: wet compress ด้วยน้ำเกลือเย็น ช่วยเย็น ลดคัน ล้างน้ำเหลือง แล้วตามด้วย steroid **cream** (สไลด์: cream สำหรับ acute/subacute)\n\n"
         "- **Ointment ปิดทับ** — กักน้ำเหลือง ทำให้ผิวเปื่อยและติดเชื้อ ใช้กับผื่นแห้งเรื้อรัง\n- **Neomycin** — เป็นสาเหตุ ACD ที่พบบ่อย (สไลด์ stasis: topical antibiotic) และไม่มีติดเชื้อ\n"
         "- **น้ำร้อน** — ทำลาย barrier และกระตุ้นคัน (สไลด์ให้เลี่ยง hot water)\n- **Oral prednisolone** — สงวนไว้กับผื่นกว้างรุนแรง และไม่ใช่การรักษาเฉพาะที่ขั้นแรก",
         "Acute ซึม = wet compress → cream", "Vehicle selection by stage", R("Treatment of eczema"), [ECZ, TCS, CS])],
    [ECZ, ECZ_B, TCS, EMOL, ANTIPRU, AH, CS], {"cycle": F.eczema_cycle(), "ladder": F.tx_ladder(), "site": F.steroid_site()},
    source="สไลด์ อ.ภูริต — The eczema cycle · Treatment of eczema (หน้า 25–27) + AAD 2023/EuroGuiDerm 2022 (ความแรง steroid, FTU — ไม่อยู่ในสไลด์)")

# ═════════════════════════════════════════════ 5
sec("derm-d1-05", "Atopic dermatitis และ pityriasis alba",
    "คัน + ผื่นตามวัย (หน้า/extensor → ข้อพับ → มือ) + เป็นเรื้อรัง + ประวัติ atopy · barrier + Th2 · ผื่นซีดหลังแดด", 9,
"""### Atopic dermatitis (สไลด์)
- พบ **15–20% ในเด็กเล็ก** (✍️ “พบมากในเด็ก แต่ adult ก็เจอได้”)
- **Major features** (สไลด์): **คัน** · ผื่น eczema (acute/subacute/chronic) ที่มี **รูปแบบตามวัย** — หน้าและด้าน extensor ในทารก · ข้อพับ/lichenification ในเด็กและผู้ใหญ่ · **เป็นเรื้อรังหรือกำเริบซ้ำ** · **ประวัติ atopy ของตนเองหรือครอบครัว** (allergic rhinitis, asthma, AD)
- ✍️ ภาพข้อพับเข่า: “**eczema ตามข้อพับ → atopic dermatitis**”
- ภาพในสไลด์: ทารกผื่นแก้มซึมมีสะเก็ด · เด็กผื่นหนาที่ข้อพับแขน · ผื่นลามจากข้อพับถึงข้อมือมี excoriation · prurigo papule ใน AD · nipple eczema ในวัยรุ่น

[[fig:age]]

#### ทำไมถึงมีอาการนี้ (กลไกเป็นข้อมูลเสริม — ไม่อยู่ในสไลด์)
[[fig:mech]]
| อาการ | กลไก | ผลทางคลินิก |
|---|---|---|
| ผิวแห้งตลอดเวลา | filaggrin ลดลง (ยีน FLG หรือถูก IL-4/IL-13 กด) → natural moisturizing factor น้อย ขี้ไคลเก็บน้ำไม่ได้ | ต้องทา emollient ทุกวันแม้ไม่มีผื่น |
| คันมากแม้ผื่นน้อย | **IL-31** จาก Th2 จับปลายประสาทคันโดยตรง | antihistamine ไม่ค่อยช่วย · ยาที่ยับยั้ง IL-4/13/31 ได้ผล |
| ผื่นที่ข้อพับ (เด็ก/ผู้ใหญ่) | เหงื่อ เสียดสี อับชื้น ระคายผิวที่ barrier เสีย | ✍️ “eczema ตามข้อพับ” |
| ผื่นแก้ม/extensor (ทารก) | น้ำลาย การถูไถตอนคลาน | ตำแหน่งเปลี่ยนตามวัย |
| ติดเชื้อแทรกง่าย | S. aureus เกาะผิว AD > 90% · antimicrobial peptide ลดลงจาก Th2 | crust เหลือง → ยาปฏิชีวนะ · bleach bath |
| ภูมิแพ้อื่นตามมา | allergen ซึมผ่านผิวที่เสีย → sensitize เป็น IgE | atopic march: food allergy → asthma → allergic rhinitis |

> **Eczema herpeticum** (ข้อมูลเสริม): ผู้ป่วย AD ที่มีตุ่มน้ำ/แผลตื้นกลม ๆ เป็นกลุ่ม (punched-out erosions) เจ็บ และไข้ = HSV ลามบนผิวที่ barrier เสีย → **acyclovir ทันที** ห้ามเพิ่ม steroid

### การรักษา AD
ใช้บันไดเดียวกับหัวข้อ 4: emollient ทุกวัน · เลี่ยงสบู่แรง น้ำร้อน ผ้าขนสัตว์ · topical steroid ตามตำแหน่ง · TCI ที่หน้า/เปลือกตา · ติดเชื้อ → ยาปฏิชีวนะ · ง่วงก่อนนอนถ้าคันจนนอนไม่ได้ · รุนแรง → NB-UVB, cyclosporine, dupilumab/JAK inhibitor (สองตัวหลังไม่อยู่ในสไลด์)

### Pityriasis alba (สไลด์)
- พบบ่อยใน **เด็กและวัยรุ่นที่เป็น AD**
- **ผื่นซีด (hypopigmented) ขอบไม่ชัดหลายวง ขนาด 0.5–2 cm มีขุยละเอียด** ที่หน้า ไหล่ แขน
- ชัดขึ้น **หลังโดนแดด** · รักษา: **topical steroid (อ่อน) + sunscreen**

#### ทำไมผื่นจึงซีด
การอักเสบเล็กน้อยแบบ eczema รบกวนการส่ง melanin จาก melanocyte ไป keratinocyte (post-inflammatory hypomelanosis) · เมื่อโดนแดด ผิวรอบ ๆ คล้ำขึ้นแต่ผื่นไม่คล้ำตาม จึงเห็นชัดขึ้น

| ผื่นซีดที่ต้องแยก | ต่างอย่างไร |
|---|---|
| **Pityriasis alba** | เด็ก AD หน้า ขอบไม่ชัด ขุยละเอียด ความรู้สึกปกติ |
| Pityriasis versicolor | ผู้ใหญ่ลำตัวส่วนบน ขุยละเอียดเมื่อขูด · **KOH พบ spaghetti and meatballs** |
| Vitiligo | **ขาวจั๊วะ (depigmented)** ขอบชัด ไม่มีขุย |
| **Leprosy (indeterminate/TT)** | ผื่นซีดที่ **ชา** ขนร่วง เหงื่อไม่ออก — **ต้องตรวจความรู้สึกเสมอในประเทศไทย** (หัวข้อ 16) |
| Nevus depigmentosus | เป็นแต่เกิด คงที่ |
""",
    ["AD: คัน + ผื่นตามวัย + เรื้อรัง/กำเริบ + ประวัติ atopy (✍️ พบมากในเด็กแต่ผู้ใหญ่ก็เป็น)",
     "ทารก = แก้ม + extensor · เด็ก = ข้อพับ (✍️) · ผู้ใหญ่ = ข้อพับ มือ ผื่นหนา",
     "Barrier เสีย (filaggrin) + Th2 (IL-4/13/31) → แห้ง คัน ติด S. aureus ง่าย",
     "AD + แผลตื้นกลมเป็นกลุ่ม เจ็บ ไข้ = eczema herpeticum → acyclovir",
     "Pityriasis alba = ผื่นซีดขุยละเอียดที่หน้าเด็ก AD หลังโดนแดด → steroid อ่อน + sunscreen · ตรวจชาเพื่อตัดเรื้อน"],
    [mcq(N(11), "A 7-year-old boy has had a recurrent itchy rash since infancy. Examination shows lichenified, excoriated eczematous plaques in both antecubital and popliteal fossae. He has asthma, and his mother has allergic rhinitis. What is the most likely diagnosis?",
         ["Atopic dermatitis", "Seborrheic dermatitis", "Psoriasis vulgaris", "Scabies", "Irritant contact dermatitis"], 0,
         "ครบ major features ในสไลด์: **คัน · ผื่น eczema ที่ข้อพับในเด็ก (✍️ “eczema ตามข้อพับ”) · เรื้อรังกำเริบตั้งแต่ทารก · ประวัติ atopy** ของตนเองและครอบครัว = **atopic dermatitis**\n\n"
         "- **Seborrheic** — ขุยเหลืองมันที่หนังศีรษะ หน้า (T-zone) ไม่ใช่ข้อพับ\n- **Psoriasis** — plaque ขอบชัดขุยหนาที่ด้าน extensor (ศอก เข่า)\n"
         "- **Scabies** — ซอกนิ้ว ข้อมือ อวัยวะเพศ คนในบ้านเป็น ไม่เรื้อรังเป็นปี\n- **ICD** — ตรงจุดสัมผัสสาร (มือ) ไม่มีรูปแบบตามวัย",
         "ข้อพับ + เรื้อรัง + atopy = AD", "Atopic dermatitis — diagnosis", R("Atopic dermatitis · Distribution of AD by age"), [ECZ, ECZ_B, ITCH]),
     mcq(N(12), "A 5-year-old girl with known atopic dermatitis develops fever and a sudden painful eruption of clustered, monomorphic, punched-out erosions with haemorrhagic crusts over her eczematous cheeks and neck over 2 days. What is the most appropriate management?",
         ["Start systemic acyclovir promptly", "Increase to a potent topical corticosteroid", "Oral cloxacillin alone",
          "Topical ketoconazole cream", "Wet wraps with mid-potency steroid and review in 2 weeks"], 0,
         "AD + ไข้ + แผลตื้นกลม ๆ ขนาดเท่ากันเป็นกลุ่ม เจ็บ เกิดเร็ว = **eczema herpeticum** (HSV ลามบนผิวที่ barrier เสีย) → ให้ **acyclovir ทันที** (ข้อมูลเสริม — ไม่อยู่ในสไลด์) และตรวจตาถ้าใกล้ตา\n\n"
         "- **เพิ่ม steroid / wet wrap** — กดภูมิเฉพาะที่ ทำให้ไวรัสลามมากขึ้น\n- **Cloxacillin อย่างเดียว** — ใช้เมื่อมี S. aureus แทรก (อาจให้ร่วมได้) แต่ไม่รักษาไวรัส\n"
         "- **Ketoconazole** — สำหรับเชื้อรา/seborrheic dermatitis",
         "AD + แผลตื้นกลมเป็นกลุ่ม + ไข้ = eczema herpeticum → acyclovir", "Atopic dermatitis — complication", ["AAD Atopic dermatitis guideline 2023 (ไม่อยู่ในสไลด์)"], [ECZ_B, HSV_B, FEVER]),
     mcq(N(13), "A 9-year-old boy with atopic dermatitis has several ill-defined, slightly scaly, hypopigmented patches 1–2 cm on both cheeks that became more noticeable after a beach holiday. Sensation over the patches is normal and KOH is negative. What is the most appropriate treatment?",
         ["Low-potency topical corticosteroid, emollient and sunscreen", "Topical ketoconazole 2% cream for 2 weeks", "Rifampicin, dapsone and clofazimine",
          "Hydroquinone 4% cream", "Narrowband UVB phototherapy three times weekly"], 0,
         "เด็ก AD + ผื่นซีดขอบไม่ชัดขุยละเอียดที่แก้ม ชัดขึ้นหลังโดนแดด ความรู้สึกปกติ KOH ลบ = **pityriasis alba** → สไลด์: **topical steroid (อ่อน เพราะที่หน้า) + sunscreen** ร่วมกับ emollient\n\n"
         "- **Ketoconazole** — pityriasis versicolor (KOH บวก)\n- **MDT** — leprosy ซึ่งผื่นจะ **ชา** ความรู้สึกปกติจึงตัดได้\n"
         "- **Hydroquinone** — ทำให้ผิว **ขาวขึ้น** ใช้กับ melasma ไม่ใช่ผื่นซีด\n- **NB-UVB** — ใช้กับ vitiligo/ผื่นกว้าง ไม่จำเป็นในโรคที่หายเองนี้",
         "Pityriasis alba = steroid อ่อน + sunscreen · เช็คชาทุกผื่นซีด", "Pityriasis alba", R("Pityriasis alba"), [ECZ, ECZ_B, TCS])],
    [ECZ, ECZ_B, ITCH, EMOL, TCS, HSV_B, LEP], {"age": F.ad_age(), "mech": F.ad_mech()},
    source="สไลด์ อ.ภูริต — Atopic dermatitis · Pityriasis alba (หน้า 28–35) + AAD 2023 (กลไก, eczema herpeticum — ไม่อยู่ในสไลด์)")

# ═════════════════════════════════════════════ 6
sec("derm-d1-06", "Seborrheic dermatitis — ผื่นตรงที่ต่อมไขมันมาก",
    "Malassezia + sebum · T-zone ขุยเหลืองมัน (✍️ นศพ.ชอบเป็น) · Parkinson/HIV/stroke · steroid + antifungal", 7,
"""### สไลด์
- 1–3% ของผู้ใหญ่ (**23% ในผู้สูงอายุ**) · ✍️ “**พบได้ในทุกอายุ**” · เรื้อรัง หลายปัจจัย (ทั้ง endogenous และ exogenous — ✍️ “endogenous eczema”)
- **การอักเสบตอบสนองต่อยีสต์ Malassezia** (✍️ ขีดเน้น)
- ✍️ “**เด่นที่ T zone**” · ✍️ “**นศพ. ชอบเป็น → เครียด นอนดึก พักผ่อนน้อย**”
- **Clinical**: อาการน้อยสุด = ขุยที่หนังศีรษะ (**รังแค** — ✍️ “อาการน้อยสุดของ seb derm”) · **ผื่นแดงขอบไม่ชัดมีขุยมัน (greasy)** (✍️ “เหลือง ๆ”) · ตำแหน่ง: หนังศีรษะ ร่องจมูก–แก้ม หู คิ้ว หน้าอก หลังส่วนบน
- **ปัจจัยเสี่ยง**: อายุมาก ชาย อ้วน **เครียด/ซึมเศร้า** (✍️ ขีดเน้น) ฤดูหนาว เหล้า บุหรี่ ความดันสูง **HIV** **โรคทางระบบประสาท (stroke — ✍️ ขีดเน้น, Parkinson)** — ภาพในสไลด์เป็นผู้สูงอายุติดเตียงใส่สายให้อาหาร มีขุยเหลืองมันที่คิ้ว (✍️ วง “greasy scale”)
- **Treatment**: ปรับวิถีชีวิต · ยาทา: **corticosteroid** (✍️ ดาว) · **แชมพูและยาทาต้านเชื้อรา** (✍️ “รักษา Malassezia yeast”) · calcineurin inhibitor

[[fig:seb]]

#### ทำไมถึงมีอาการนี้
| อาการ/ปัจจัย | กลไก | ใช้อย่างไร |
|---|---|---|
| อยู่ที่ T-zone หนังศีรษะ หลังหู หน้าอก | Malassezia ต้องใช้ไขมันจากผิว จึงอยู่หนาแน่นตรงที่ต่อมไขมันมาก | ตำแหน่งเป็นกุญแจวินิจฉัย |
| ขุยเหลืองมัน ขอบไม่ชัด | lipase ของเชื้อย่อย sebum เป็นกรดไขมันอิสระที่ระคายผิว → อักเสบ + keratinocyte หลุดเร็ว ขุยจึงชุ่มไขมัน | ต่างจาก psoriasis (ขุยแห้งสีเงิน ขอบชัด) |
| Parkinson, stroke | sebum มากขึ้น ใบหน้าขยับน้อย ทำความสะอาดยาก | ✍️ ภาพผู้ป่วยติดเตียง |
| HIV | ภูมิคุ้มกันเปลี่ยน → ผื่นกว้าง รุนแรง ดื้อการรักษา | **ผู้ใหญ่ตอนต้นที่เป็นผื่นรุนแรงทันที → ตรวจ HIV** |
| เครียด อดนอน ฤดูหนาว | ภูมิคุ้มกันและ barrier เปลี่ยน | ✍️ “นศพ. ชอบเป็น” |
| ดีขึ้นด้วยยาต้านเชื้อรา | ลดจำนวน Malassezia = ลดตัวกระตุ้น | ใช้ ketoconazole ซ้ำเป็นระยะกันกำเริบ |

### การรักษาที่ใช้จริง (รายละเอียดเพิ่มเติมจากตำรา)
- **Ketoconazole 2%** cream/shampoo (หรือ selenium sulfide, ciclopirox) — แชมพูทิ้งไว้ 5 นาทีก่อนล้าง สัปดาห์ละ 2–3 ครั้ง แล้วลดเป็น 1 ครั้งเพื่อคุม
- **Steroid อ่อน** (hydrocortisone 1%) ระยะสั้นที่หน้าเมื่อกำเริบ · TCI เมื่อต้องใช้นาน
- โรคนี้ **คุมได้แต่ไม่หายขาด** — อธิบายผู้ป่วยว่าจะกลับเป็นเมื่อเครียด/หน้าหนาว

| ต้องแยก | ต่างอย่างไร |
|---|---|
| Psoriasis (sebopsoriasis) | plaque ขอบชัด ขุยหนาสีเงิน มีที่ศอก เข่า เล็บ |
| **SLE malar rash** | ผื่นแก้มรูปผีเสื้อที่ **ไม่ลงร่องจมูก–แก้ม** · seb derm **ชอบอยู่ในร่องจมูก–แก้ม** |
| Rosacea | ตุ่มแดง/หนอง หลอดเลือดฝอย หน้าแดงง่าย ไม่มีขุยมัน |
| Tinea faciei | ขอบนูนชัด KOH บวก |
| AD ทารก | ซ้อนกันได้ (สไลด์ AD by age) — AD คันมากกว่า |
""",
    ["Seb derm = Malassezia + sebum → ขุยเหลืองมัน ขอบไม่ชัด ที่ T-zone หนังศีรษะ หลังหู หน้าอก",
     "รังแค = อาการน้อยที่สุด (✍️) · ✍️ นศพ.ชอบเป็น: เครียด นอนดึก",
     "ปัจจัยเสี่ยงที่ต้องจำ: Parkinson · stroke · HIV",
     "ผื่นรุนแรงเกิดใหม่ในผู้ใหญ่ตอนต้น → ตรวจ HIV",
     "รักษา: ยาต้านเชื้อรา (ketoconazole) + steroid อ่อนระยะสั้น · คุมได้ไม่หายขาด"],
    [mcq(N(14), "A 68-year-old man with Parkinson disease has erythematous patches with greasy, yellowish scales on the scalp, eyebrows, glabella, and nasolabial folds. The rash worsens in winter and is mildly itchy. Which treatment is most appropriate?",
         ["Ketoconazole 2% shampoo and cream plus a short course of low-potency topical corticosteroid",
          "Clobetasol propionate 0.05% cream to the face for 3 months", "Oral terbinafine 250 mg daily for 6 weeks",
          "Permethrin 5% cream overnight", "Hydroxychloroquine 200 mg daily"], 0,
         "ขุยเหลืองมันที่หนังศีรษะ คิ้ว หว่างคิ้ว ร่องจมูก–แก้ม ใน **ผู้ป่วย Parkinson** (ปัจจัยเสี่ยงในสไลด์) = **seborrheic dermatitis** → สไลด์: **steroid ทา + แชมพู/ยาทาต้านเชื้อรา** (✍️ “รักษา Malassezia yeast”) — ที่หน้าใช้ steroid อ่อนระยะสั้น\n\n"
         "- **Clobetasol ที่หน้า 3 เดือน** — แรงเกิน ผิวบาง perioral dermatitis rosacea\n- **Oral terbinafine** — dermatophyte ที่เล็บ/ผิว ไม่ได้ผลดีกับ Malassezia และไม่จำเป็น\n"
         "- **Permethrin** — scabies\n- **Hydroxychloroquine** — cutaneous lupus (ผื่นแก้มที่ **ไม่ลงร่องจมูก–แก้ม**)",
         "Seb derm = antifungal + steroid อ่อน", "Seborrheic dermatitis — treatment", R("Seborrheic dermatitis: Clinical · Risk factor · Treatment"), [ECZ, ECZ_B, TCS, TINEA]),
     mcq(N(15), "A previously healthy 27-year-old man presents with a 1-month history of an extensive, severe eruption of greasy, scaly erythematous plaques on the face, scalp, chest and groin that has not responded to topical treatment. He also has oral thrush. Which investigation is most important next?",
         ["HIV antibody/antigen test", "Patch testing", "Serum IgE level", "Antinuclear antibody", "Skin biopsy for mycosis fungoides"], 0,
         "seborrheic dermatitis **รุนแรง กว้าง เกิดใหม่ในผู้ใหญ่ตอนต้น ดื้อการรักษา** + **oral thrush** → ต้องคิดถึง **HIV** (สไลด์ระบุ HIV เป็นปัจจัยเสี่ยงของ seb derm) — การตรวจ HIV เปลี่ยนการดูแลมากที่สุด\n\n"
         "- **Patch test** — หา allergen ใน ACD\n- **IgE** — ไม่ช่วยวินิจฉัยหรือเปลี่ยนการรักษา\n"
         "- **ANA** — คิดถึงเมื่อผื่นแก้มไม่ลงร่องจมูก ร่วมกับอาการ SLE\n- **Biopsy MF** — คิดถึงใน “eczema” ผู้สูงอายุที่ไม่หาย แต่ thrush ชี้ไปทางภูมิคุ้มกันบกพร่องก่อน",
         "Seb derm รุนแรง + thrush ในคนหนุ่ม → ตรวจ HIV", "Seborrheic dermatitis — risk factor HIV", R("Seborrheic dermatitis: Risk factor"), [ECZ, STI, RASH])],
    [ECZ, ECZ_B, TCS, TINEA, RASH], {"seb": F.seb()},
    source="สไลด์ อ.ภูริต — Seborrheic dermatitis (หน้า 36–41)")

# ═════════════════════════════════════════════ 7
sec("derm-d1-07", "Eczema ที่ขาผู้สูงอายุ: stasis dermatitis และ xerotic (asteatotic) eczema",
    "Venous hypertension → hemosiderin + eczema + แผล · compression · ผิวแห้งแตกลายงาที่หน้าแข้ง · xerosis กว้าง → หาโรคทางระบบ", 9,
"""### Stasis dermatitis (สไลด์)
- ชื่ออื่น: stasis eczema, hypostatic eczema, varicose eczema · เกิดที่ **ขา** ในผู้ที่มี **venous insufficiency มานาน**
- **ซ้อนด้วย allergic contact dermatitis ได้บ่อย** — ยาปฏิชีวนะทา, lanolin, emulsifier, paraben, iodine, balsam of Peru, น้ำหอม, สารจากพืช
- **Clinical** (✍️ ดาว): ผื่นรอบข้อเท้าและน่อง **สองข้าง** · **triad: ขนร่วง (alopecia) · ผิวมันเหมือนขี้ผึ้ง (waxy) · สีน้ำตาลเหลืองจาก hemosiderin** (✍️ ลูกศรชี้ “hemosiderin pigment” ในภาพขาที่มีเส้นเลือดขอด) · ภาวะแทรกซ้อน: **แผล · cellulitis · lymphangitis**
- ✍️ ภาพขา: “Lower leg สีไม่ค่อย… · Stasis eczema”
- **Treatment**: **compression** (stocking, elastic bandage) · topical steroid · emollient

[[fig:stasis]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| บวมกดบุ๋มช่วงเย็น | ความดันใน capillary สูง → น้ำรั่วออกนอกหลอดเลือด | ยกขา/compression ลดได้ |
| สีน้ำตาลเหลือง | RBC รั่วออก → macrophage ย่อย hemoglobin เป็น **hemosiderin** | ✍️ “hemosiderin pigment” — ไม่ใช่ melanin จึงไม่จางด้วยยาทาฝ้า |
| ผื่น eczema คัน | เม็ดเลือดขาวติดค้างใน capillary ที่ช้า หลั่งสารอักเสบ · fibrin cuff ขัดขวาง O2 | steroid ทาลดการอักเสบ แต่ต้นเหตุคือความดัน |
| ผิวแข็งตึง ขาเรียวเหมือนขวดคว่ำ | อักเสบเรื้อรังของไขมัน → พังผืด (lipodermatosclerosis — ข้อมูลเสริม) | ระยะท้าย |
| แผลเหนือตาตุ่มใน | ผิวขาด O2 + บาดเจ็บเล็กน้อย | venous ulcer → compression เป็นหลัก (ตรวจ ABI ก่อนพันแน่น) |
| แพ้ยาทาง่าย | barrier เสียนาน + ทายาหลายชนิดซ้ำ ๆ | ผื่นลามขึ้นหลังทายา → นึกถึง ACD (neomycin, lanolin) |

> **Stasis สองข้าง vs cellulitis**: stasis เป็น **สองข้าง** คัน ไม่ร้อนมาก ไม่มีไข้ · cellulitis มัก **ข้างเดียว** ปวด ร้อน แดงลาม ไข้ — การให้ยาปฏิชีวนะกับ stasis สองข้างเป็นความผิดพลาดที่พบบ่อย (ข้อมูลเสริม)

### Xerotic (asteatotic) eczema (สไลด์)
- ชื่ออื่น asteatotic dermatitis, **eczema craquelé** · ✍️ “**แห้ง ๆ แตก ๆ**”
- **โรคผิวหนังที่วินิจฉัยบ่อยที่สุดในผู้สูงอายุ** แต่พบได้ทุกวัย · สัมพันธ์กับ **ไขมันในผิวลดลงและเสียน้ำผ่านผิว (TEWL)** · พบบ่อยหน้าหนาว
- **Clinical**: ขุย แดง แตก คัน · **ร่องแดงหลายเหลี่ยมคั่นแผ่นขุยแห้ง** — “cracked porcelain” “crazy pavement” “dry riverbed” · ตำแหน่งบ่อยที่สุด **หน้าแข้งด้านหน้า–ข้าง** (✍️ “หน้าแข้ง (ปกติแห้งสุด)”) · ภาพหน้าท้อง ✍️ “แห้งมากกกก”
- **Extensive xerotic eczema** ต้องหา: **มะเร็งภายใน เช่น lymphoma** · **ยาขับปัสสาวะ** · ผิวแห้งทั่วไปจาก atopic eczema, ไตวายเรื้อรัง, ตับวาย, AIDS, myxedema, malabsorption (vitamin A, zinc)

[[fig:xerosis]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| ลายแตกหลายเหลี่ยม | ขี้ไคลที่ขาดไขมันหดตัวเป็นแผ่น แตกตามแนวที่อ่อนแอ | ลายเฉพาะ — วินิจฉัยได้จากการมอง |
| ร่องแดงคัน | ร่องลึกถึง epidermis → สารระคายเข้า → อักเสบตามร่อง | ทา steroid กลางในยาพื้น ointment ระยะสั้น |
| หน้าแข้งเป็นก่อน | ต่อมไขมันน้อยที่สุดของร่างกาย | ✍️ “ปกติแห้งสุด” |
| ผู้สูงอายุ + หน้าหนาว + อาบน้ำร้อน | ไขมันผิวลดตามวัย ความชื้นอากาศต่ำ น้ำร้อน/สบู่ล้างไขมัน | แก้ที่พฤติกรรม: อาบน้ำอุ่นสั้น สบู่อ่อน ทา emollient ทันทีหลังอาบ |
| แห้งทั้งตัว | ต่อมเหงื่อ/ไขมันทำงานลด (hypothyroid) การสร้างขี้ไคลผิดปกติ (lymphoma = acquired ichthyosis) ขาดน้ำ (diuretic) ขาดสารอาหาร | ซักประวัติยา ตรวจ TSH ไต ตับ HIV CBC ตามข้อบ่งชี้ |
""",
    ["Stasis: ผื่นสองข้างรอบข้อเท้า + triad (ขนร่วง · ผิวมันขี้ผึ้ง · สีน้ำตาลเหลือง hemosiderin)",
     "รักษาต้นเหตุด้วย compression + steroid ทา + emollient · ระวัง ACD จากยาทา",
     "Stasis สองข้าง ≠ cellulitis — อย่าให้ยาปฏิชีวนะโดยไม่มีข้อบ่งชี้",
     "Xerotic eczema: ลายแตกแบบกระเบื้องร้าวที่หน้าแข้งผู้สูงอายุ หน้าหนาว (✍️ แห้ง ๆ แตก ๆ)",
     "แห้งทั้งตัว → lymphoma · diuretic · CKD/ตับ · hypothyroid · HIV · ขาด zinc/vit A"],
    [mcq(N(16), "A 70-year-old woman with long-standing varicose veins has itchy, scaly, erythematous plaques around both ankles and lower calves, with yellow-brown pigmentation, hair loss and shiny skin. Both legs are equally affected, are not warm, and she is afebrile. What is the most appropriate management?",
         ["Compression stockings with a mid-potency topical steroid and emollient", "Oral cephalexin for 10 days", "Topical neomycin–bacitracin ointment twice daily",
          "Urgent venous duplex to exclude bilateral DVT, then anticoagulation", "Hydroquinone cream to lighten the pigment"], 0,
         "ผื่นรอบข้อเท้า **สองข้าง** + **triad (ขนร่วง ผิวมันขี้ผึ้ง สีน้ำตาลเหลือง hemosiderin)** ใน varicose vein = **stasis dermatitis** → สไลด์: **compression + topical steroid + emollient** (compression แก้ความดันหลอดเลือดดำที่เป็นต้นเหตุ — ควรตรวจชีพจร/ABI ก่อนพันแน่น)\n\n"
         "- **Cephalexin** — ไม่มีลักษณะ cellulitis (สองข้าง ไม่ร้อน ไม่มีไข้)\n- **Neomycin–bacitracin** — สไลด์เตือนว่า stasis ซ้อน **ACD จากยาปฏิชีวนะทา** ได้บ่อย\n"
         "- **Duplex/anticoagulant** — DVT ทั้งสองข้างพร้อมกันพร้อมผื่นเรื้อรังไม่เข้ากับภาพนี้\n- **Hydroquinone** — สีมาจาก hemosiderin ไม่ใช่ melanin",
         "Stasis = compression + steroid + emollient · อย่าใช้ยาปฏิชีวนะทา", "Stasis dermatitis", R("Stasis dermatitis: Clinical · Treatment"), [ECZ, ECZ_B, TCS, CELL]),
     mcq(N(17), "An 82-year-old man complains of itchy shins every winter. Examination shows dry skin on both anterior shins with a network of fine red fissures separating plates of scale, resembling cracked porcelain. He bathes twice daily with hot water and antibacterial soap. What is the best initial treatment?",
         ["Lukewarm short baths, mild soap substitute, liberal emollient after bathing and a mid-potency steroid ointment for a short period",
          "Oral antihistamine alone", "Topical ketoconazole cream", "Oral prednisolone 20 mg for 2 weeks", "Topical salicylic acid 10% to remove scale"], 0,
         "ผิวแห้งแตกลายกระเบื้องร้าวที่หน้าแข้งผู้สูงอายุ หน้าหนาว = **xerotic (asteatotic) eczema** — ต้นเหตุคือ **ไขมันผิวลด + TEWL** ซ้ำเติมด้วยน้ำร้อนและสบู่แรง → แก้พฤติกรรม + **emollient** (ฐานบันได) + steroid กลางในยาพื้น **ointment** ระยะสั้นสำหรับร่องที่อักเสบ\n\n"
         "- **Antihistamine อย่างเดียว** — ไม่แก้ผิวแห้ง และชนิดง่วงเสี่ยงล้มในผู้สูงอายุ\n- **Ketoconazole** — ไม่มีเชื้อรา\n"
         "- **Oral prednisolone** — ไม่จำเป็นสำหรับผื่นเฉพาะที่\n- **Salicylic acid 10%** — ลอกขุยแต่ระคายผิวแตก ทำให้แสบมากขึ้น",
         "Xerotic eczema = emollient + เลิกน้ำร้อน/สบู่แรง ± steroid ointment", "Xerotic eczema", R("Xerotic eczema: Clinical"), [ECZ, EMOL, TCS, AGE_SK]),
     mcq(N(18), "A 66-year-old man has developed generalized dry, scaly, itchy skin over the past 4 months, despite regular emollient use. He has lost 6 kg, has night sweats, and is not taking any new medications. What is the most important next step?",
         ["Evaluate for lymphoma (CBC, lymph node examination, imaging as indicated)", "Switch to a stronger emollient and review in 6 months",
          "Patch testing for fragrance allergy", "Start oral antifungal therapy", "Prescribe a 4-week course of oral prednisolone"], 0,
         "สไลด์: **extensive xerotic eczema ต้องหามะเร็งภายใน โดยเฉพาะ malignant lymphoma** · ผิวแห้งทั่วตัวเกิดใหม่ในผู้สูงอายุ + **น้ำหนักลด เหงื่อออกกลางคืน** (B symptoms) → ตรวจหา lymphoma ก่อน (acquired ichthyosis เป็น paraneoplastic)\n\n"
         "- **รอ 6 เดือน** — พลาดโรคร้ายแรง\n- **Patch test** — ไม่มีประวัติชี้ไปทาง ACD และไม่อธิบาย B symptoms\n"
         "- **Antifungal** — ไม่มีหลักฐานเชื้อรา\n- **Prednisolone** — บดบังอาการ lymphoma และไม่ใช่การวินิจฉัย",
         "Xerosis ทั้งตัว + B symptoms → หา lymphoma", "Extensive xerotic eczema — systemic causes", R("Extensive xerotic eczema"), [ECZ, ITCH, LAD])],
    [ECZ, ECZ_B, ITCH, TCS, EMOL, ULC, CELL, AGE_SK], {"stasis": F.stasis(), "xerosis": F.xerosis()},
    source="สไลด์ อ.ภูริต — Stasis dermatitis · Xerotic eczema (หน้า 42–50)")

# ═════════════════════════════════════════════ 8
sec("derm-d1-08", "Nummular eczema · prurigo nodularis · lichen simplex chronicus — โรคของวงจรคัน-เกา",
    "ผื่นรูปเหรียญซึม · nodule แข็งจากการแกะ · plaque หนาจากการถู · ตัดวงจรเกาและหาสาเหตุคันทั้งตัว", 7,
"""### สามโรคในสไลด์ (แต่ละโรคเริ่มจากภาพ “Diagnosis?”)
| โรค | สไลด์ | ✍️ / ภาพ |
|---|---|---|
| **Nummular eczema** | โรคเรื้อรัง ไม่ทราบสาเหตุ · papule/papulovesicle รวมกันเป็น **plaque รูปเหรียญ** มีซึม สะเก็ด ขุย · หญิงพบที่ **แขนและหลังมือ** ชายพบที่ **ขา** | ภาพ: plaque กลมหลายวงที่ข้อเท้าและหลังเท้า |
| **Prurigo nodularis** | คันเรื้อรัง · **nodule แข็งมี hyperkeratosis ขนาด 0.5–3 cm** อาจมีรอยเกา · สัมพันธ์กับ **AD หรือโรคทางระบบที่ทำให้คัน** | ✍️ “nodule เกา…” · ภาพ: nodule หลายเม็ดที่แขนด้านนอก มีแผลถลอกด้านบน |
| **Lichen simplex chronicus** | คันมาก เรื้อรัง · **plaque lichenified หนึ่งหรือหลายแผ่น** · หนังศีรษะ **ท้ายทอย** แขนขาด้าน extensor **ข้อเท้า** อวัยวะเพศ/ทวาร | ✍️ “lichen simplex chronicus” (ภาพข้อเท้า) · ✍️ “Scrotum” (ภาพ LSC ที่ถุงอัณฑะ) |

[[fig:itch]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้อย่างไร |
|---|---|---|
| เกาแล้วหายคันชั่วคราว | สัญญาณเจ็บจากการเกากดสัญญาณคันในไขสันหลัง | อธิบายผู้ป่วยว่าการเกาคือตัวต่อวงจร |
| ผิวหนาเป็น plaque (LSC) | ถูซ้ำที่เดิม → keratinocyte แบ่งตัวป้องกัน → acanthosis + hyperkeratosis | อยู่ตรงที่มือเอื้อมถึงง่าย (ท้ายทอย ข้อเท้า อวัยวะเพศ) |
| nodule แข็ง (PN) | แกะเป็นจุด ๆ ซ้ำ → epidermis หนาเป็นก้อน + ปลายประสาทใน dermis งอกเพิ่ม | ✍️ “nodule เกา” — ต้องหาโรคที่ทำให้คันทั้งตัว |
| ยิ่งเกายิ่งคัน | ปลายประสาทไวขึ้น (neural sensitization — ข้อมูลเสริม) | ต้องตัดวงจรด้วยการปิดแผล/ยาทาแรง ไม่ใช่แค่บอกว่า “อย่าเกา” |
| ผื่นรูปเหรียญซึม (nummular) | eczema ที่ขอบเขตกลมชัด มักมีผิวแห้งพื้นฐานและ S. aureus ร่วม | **ต้องแยก tinea corporis** ด้วย KOH (tinea มีขอบนูนกลางจาง) |

### การรักษา (สไลด์ไม่ได้ให้รายละเอียดเฉพาะโรค — ใช้หลัก eczema + ข้อมูลเสริม)
- **Steroid แรงทาปิด (occlusion)** หรือแผ่นแปะ steroid · ฉีด triamcinolone เข้ารอยโรคใน nodule ที่ดื้อ
- **ปิดทับ** (พลาสเตอร์ hydrocolloid, Unna boot) ป้องกันการเกา · ตัดเล็บ · antihistamine ชนิดง่วงก่อนนอน
- **PN**: ตรวจหาสาเหตุคันทั้งตัว — CBC, BUN/Cr, LFT, TSH, glucose, HIV/HBV/HCV ตามความเสี่ยง · รายที่ดื้อ: phototherapy, gabapentinoid, dupilumab (ไม่อยู่ในสไลด์)
- จัดการความเครียดและนิสัยการเกา (habit reversal)
""",
    ["วงจรคัน-เกา: เกาแล้วหายชั่วคราว → ผิวหนา + ประสาทไว → คันมากขึ้น",
     "LSC = plaque หนาจากการถูที่เดิม (ท้ายทอย ข้อเท้า ✍️ scrotum)",
     "Prurigo nodularis = nodule แข็ง 0.5–3 cm จากการแกะ → หาโรคทางระบบที่ทำให้คัน",
     "Nummular = plaque รูปเหรียญซึม (หญิง: แขน/หลังมือ · ชาย: ขา) → KOH ตัด tinea",
     "รักษา: steroid แรงทาปิด + ป้องกันการเกา + ยาง่วงก่อนนอน"],
    [mcq(N(19), "A 45-year-old woman has a single, thick, hyperpigmented, scaly plaque with exaggerated skin markings on the nape of her neck. She admits rubbing it constantly when stressed at work. KOH is negative. Which management is most appropriate?",
         ["Potent topical corticosteroid under occlusion plus measures to stop rubbing (covering, habit reversal, sedating antihistamine at night)",
          "Topical terbinafine for 4 weeks", "Oral isotretinoin", "Reassurance only because it will resolve spontaneously",
          "Low-potency hydrocortisone lotion once daily"], 0,
         "plaque lichenified แผ่นเดียวที่ **ท้ายทอย** จากการถูซ้ำเมื่อเครียด KOH ลบ = **lichen simplex chronicus** · ผิวหนามากจึงต้องใช้ **steroid แรง + ปิดทับ** ให้ยาซึมและกันการเกา พร้อมตัดวงจรนิสัยการถู\n\n"
         "- **Terbinafine** — KOH ลบ ไม่ใช่เชื้อรา\n- **Isotretinoin** — สิว ไม่เกี่ยว\n"
         "- **ปลอบอย่างเดียว** — วงจรคัน-เกาไม่หยุดเอง\n- **Hydrocortisone lotion** — อ่อนเกินสำหรับผื่นหนา",
         "LSC = steroid แรงทาปิด + หยุดถู", "Lichen simplex chronicus", R("Lichen simplex chronicus"), [ECZ, ITCH, TCS]),
     mcq(N(20), "A 58-year-old man has a 1-year history of generalized itch and multiple firm, dome-shaped, hyperkeratotic, excoriated nodules 0.5–2 cm on the extensor arms and legs. He has no personal history of atopy. Which approach is most appropriate besides symptomatic treatment?",
         ["Screen for systemic causes of pruritus: CBC, renal and liver function, thyroid function, glucose, and HIV/hepatitis serology",
          "Excise every nodule surgically", "Prescribe oral antibiotics for 6 weeks", "Patch test to the standard series only", "Start methotrexate immediately without further evaluation"], 0,
         "nodule แข็งมี hyperkeratosis และรอยเกาหลายเม็ดที่แขนขาด้านนอก + คันทั้งตัว = **prurigo nodularis** · สไลด์: สัมพันธ์กับ **AD หรือโรคทางระบบที่ทำให้คัน** — ผู้ป่วยไม่มี atopy จึงต้องหา **CKD ตับ (cholestasis) เลือด (lymphoma, polycythemia) ไทรอยด์ เบาหวาน HIV/HBV/HCV**\n\n"
         "- **ผ่าตัดทุกเม็ด** — ไม่แก้วงจรคัน จะเกิดใหม่\n- **Antibiotic 6 สัปดาห์** — ไม่มีการติดเชื้อเป็นสาเหตุ\n"
         "- **Patch test** — ใช้เมื่อสงสัย ACD ไม่ใช่ภาพนี้\n- **Methotrexate ทันที** — ยาขั้นสูงก่อนหาสาเหตุ",
         "Prurigo nodularis → หาสาเหตุคันทั้งตัว", "Prurigo nodularis", R("Prurigo nodularis"), [ECZ, ITCH, RASH])],
    [ECZ, ECZ_B, ITCH, TCS, ANTIPRU, TINEA, KOH], {"itch": F.itch_scratch()},
    source="สไลด์ อ.ภูริต — Nummular eczema · Prurigo nodularis · Lichen simplex chronicus (หน้า 53–58)")

# ═════════════════════════════════════════════ 9
sec("derm-d1-09", "Dyshidrosis (pompholyx) และ miliaria — ตุ่มน้ำที่เกี่ยวกับมือ เท้า และเหงื่อ",
    "ตุ่มน้ำใสลึก “เม็ดสาคู” ที่ฝ่ามือ ข้างนิ้ว (✍️ เคยเป็น!) · ท่อเหงื่ออุดตื้น/ลึก → crystallina/rubra/profunda", 7,
"""### Dyshidrosis / pompholyx (สไลด์ — ✍️ ดาวทั้งสองหน้า)
- ภาพ “Diagnosis?” ฝ่ามือ: ✍️ “**Dyshidrosis**” · ✍️ วงตุ่ม “**มีตุ่มน้ำใส ๆ**” · “**มีตุ่มนูน**”
- พบบ่อยใน **วัยรุ่นและผู้ใหญ่ตอนต้น** (✍️ ขีดเน้น + ดอกจัน)
- **ตุ่มน้ำลึก (deep-seated vesicles) ที่ฝ่ามือ ข้างนิ้ว และฝ่าเท้า** (✍️ ขีดเน้น + ดอกจัน)
- ลักษณะ “**tapioca**” (✍️ “**เม็ดสาคู**”) · **คัน** · **ติดเชื้อแบคทีเรียแทรกบ่อย**
- ✍️ “**ใส ๆ คัน ๆ อยู่ลึก ๆ**” · ✍️ “**เคยเป็น!**” · ✍️ สัมพันธ์กับ “**allergic rhinitis, asthma**” · ✍️ “**Treat by topical steroid**”

[[fig:pomph]]

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกโรค |
|---|---|---|
| ตุ่มน้ำ “ลึก” ไม่แตก | ฝ่ามือฝ่าเท้ามีขี้ไคลหนาที่สุดของร่างกาย กดตุ่มน้ำจาก spongiosis ไว้ใต้หลังคาหนา | เห็นเป็นเม็ดใส ๆ ใต้ผิวเหมือนสาคู · ผิวบางที่อื่นตุ่มจะแตกซึม |
| คันมาก ข้างนิ้วก่อน | ข้างนิ้วมีขี้ไคลบางกว่าฝ่ามือเล็กน้อย ตุ่มจึงโผล่ให้เห็นก่อน | ข้างนิ้วเป็นตำแหน่งเฉพาะของโรค |
| เป็นช่วงร้อน/เครียด | เหงื่อและความเครียดกระตุ้น (แต่ต่อมเหงื่อไม่ได้อุดจริง — ชื่อ “dyshidrosis” เป็นชื่อเดิม) | สัมพันธ์กับ atopy (✍️) |
| หนอง สะเก็ดเหลือง | ตุ่มแตกแล้วติด S. aureus | ให้ยาปฏิชีวนะร่วม |
| ลอกเป็นวงหลังตุ่มแห้ง | หลังคาหนาหลุดออกเป็นแผ่น (collarette) | ระยะหาย |

**รักษา**: steroid **แรง** ทา (ผิวหนา) ± ปิดทับ · wet compress ในระยะตุ่มน้ำ · emollient · เลี่ยงสารระคาย ใส่ถุงมือ · ติดเชื้อ → antibiotic · ต้องแยก **tinea pedis/manuum** (KOH — มีตุ่มน้ำที่เท้าได้และอาจทำให้เกิด id reaction ที่มือ), **scabies** (ซอกนิ้ว มีอุโมงค์), **ACD** ต่อสารที่จับ (patch test ถ้าดื้อ)

### Miliaria (ผด) — สไลด์
- เกิดจาก **ท่อเหงื่อเสียความต่อเนื่อง (disruption of sweat ductal integrity)**
- ปัจจัยเสริม: **UV · แบคทีเรียประจำผิว · เหงื่อออกซ้ำ ๆ** · พบบ่อยใน **ทารกและที่อากาศร้อน** · **หายเองภายในราว 1 วัน**
- ภาพ: **miliaria crystallina** (✍️ ขีดเน้น) — ตุ่มน้ำใสเล็กมากเหมือนหยดน้ำค้าง **ไม่มีผื่นแดง** · miliaria pustulosa · miliaria rubra (ตุ่มแดง)

[[fig:mil]]

| ชนิด | ระดับที่ท่ออุด | หน้าตา | พบใน |
|---|---|---|---|
| Crystallina | ใต้/ในชั้นขี้ไคล | ตุ่มใสเล็กมาก ไม่แดง ไม่คัน แตกง่าย | ทารก · **ผู้ป่วยในที่มีไข้สูงเหงื่อออกมากนอนติดเตียง** |
| Rubra (ผดผื่นแดง) | กลาง epidermis | ตุ่มแดงเล็ก คัน/แสบร้อน | อากาศร้อนชื้น เสื้อผ้าหนา |
| Pustulosa | ต่อจาก rubra | ตุ่มหนองเล็กปลอดเชื้อบนฐานแดง | |
| Profunda | ระดับ DEJ/dermis | ตุ่มสีเนื้อ เหงื่อไม่ออกบริเวณนั้น (เสี่ยง heat exhaustion) | เป็นผดซ้ำ ๆ ในเขตร้อน |

> **ทำไมลึกยิ่งแดง**: เหงื่อที่รั่วในชั้นขี้ไคลไม่สัมผัสเซลล์มีชีวิต จึงไม่อักเสบ (crystallina) · เหงื่อที่รั่วในชั้นเซลล์มีชีวิตหรือ dermis กระตุ้นการอักเสบ → แดง คัน (rubra) · **รักษา**: ทำให้เย็น ระบายอากาศ เสื้อผ้าโปร่ง เลี่ยงครีมข้นที่อุดรูเหงื่อ · calamine lotion ลดคัน
""",
    ["Dyshidrosis = ตุ่มน้ำใสลึก “เม็ดสาคู” ที่ฝ่ามือ ข้างนิ้ว ฝ่าเท้า คันมาก (✍️ ใส ๆ คัน ๆ อยู่ลึก ๆ)",
     "ลึกเพราะขี้ไคลฝ่ามือหนา กดตุ่มไว้ไม่ให้แตก",
     "วัยรุ่น/ผู้ใหญ่ตอนต้น สัมพันธ์ atopy · ✍️ รักษาด้วย topical steroid (แรง) · ติดเชื้อแทรกบ่อย",
     "Miliaria = ท่อเหงื่ออุด: crystallina (ตื้น ใส ไม่แดง) · rubra (กลาง epidermis แดงคัน) · profunda (ลึก)",
     "ผดหายเองใน ~1 วันเมื่อเย็นลง"],
    [mcq(N(21), "A 22-year-old medical student with allergic rhinitis has recurrent episodes of intensely itchy, clear, deep-seated 1–2 mm vesicles along the sides of the fingers and on the palms, worse during exam periods and hot weather. KOH from the palm is negative. What is the most appropriate treatment?",
         ["Potent topical corticosteroid (e.g., clobetasol) for a short course with emollients and irritant avoidance",
          "Oral acyclovir for 7 days", "Permethrin 5% cream to the whole body", "Topical clotrimazole for 4 weeks", "Oral isotretinoin"], 0,
         "ตุ่มน้ำใสลึก “เม็ดสาคู” ที่ข้างนิ้วและฝ่ามือ คันมาก กำเริบเมื่อร้อน/เครียด ในคนหนุ่มสาวที่มี atopy KOH ลบ = **dyshidrosis (pompholyx)** → ✍️ “**Treat by topical steroid**” — ต้องเป็นชนิด **แรง** เพราะผิวฝ่ามือหนา\n\n"
         "- **Acyclovir** — herpetic whitlow เป็นกลุ่มตุ่มน้ำเจ็บที่ปลายนิ้วข้างเดียว ไม่ใช่ตุ่มคันกำเริบซ้ำสองมือ\n- **Permethrin** — scabies (ซอกนิ้ว อุโมงค์ คันกลางคืน คนในบ้านเป็น)\n"
         "- **Clotrimazole** — KOH ลบ\n- **Isotretinoin** — สิว",
         "Dyshidrosis = topical steroid แรง (✍️)", "Dyshidrosis (pompholyx)", R("Dyshidrosis (Pompholyx)"), [DYSH, DYSH_B, TCS]),
     mcq(N(22), "A 60-year-old man admitted with pneumonia has had high fever and profuse sweating for 3 days while lying supine. The nurse notices hundreds of tiny, clear, fragile, dew-drop-like vesicles on his back and chest without surrounding erythema or itch. What is the most appropriate management?",
         ["Reassure, keep the skin cool and dry, and change damp clothing — it resolves without specific treatment", "Start intravenous acyclovir",
          "Stop all antibiotics because this is a drug-induced blistering eruption", "Perform a skin biopsy to exclude pemphigus", "Apply clobetasol ointment under occlusion"], 0,
         "ตุ่มใสเล็กมากเหมือนหยดน้ำค้าง เปราะ **ไม่แดง ไม่คัน** หลังไข้และเหงื่อออกมากขณะนอนหงาย = **miliaria crystallina** (ภาพในสไลด์) — ท่อเหงื่ออุดตื้นในชั้นขี้ไคล เหงื่อไม่สัมผัสเซลล์มีชีวิตจึงไม่อักเสบ · สไลด์: **หายเองภายในราว 1 วัน** → ทำให้เย็นและแห้ง\n\n"
         "- **Acyclovir** — HSV/VZV เป็นตุ่มบนฐานแดงเป็นกลุ่ม\n- **หยุดยาปฏิชีวนะ** — ไม่ใช่ drug eruption (ไม่มีผื่นแดง/เยื่อบุ)\n"
         "- **Biopsy** — ไม่จำเป็นในภาพคลาสสิก\n- **Clobetasol ปิดทับ** — อุดรูเหงื่อมากขึ้น",
         "ตุ่มใสหยดน้ำค้างไม่แดงหลังเหงื่อออก = miliaria crystallina → ทำให้เย็น", "Miliaria", R("Miliaria"), [DYSH, DYSH_B, RASH])],
    [DYSH, DYSH_B, TCS, TINEA, SCAB, KOH], {"pomph": F.pompholyx(), "mil": F.miliaria()},
    source="สไลด์ อ.ภูริต — Dyshidrosis · Miliaria (หน้า 51–52, 64–66)")

# ═════════════════════════════════════════════ 10
sec("derm-d1-10", "Contact dermatitis — irritant (“ระคาย ไม่ใช่แพ้”) vs allergic (type IV)",
    "ICD 80% สัมพันธ์อาชีพ · ACD ต้อง sensitize ก่อน · ตำแหน่งบอกสาเหตุ (✍️ หัวเข็มขัด) · patch test", 8,
"""### Allergic contact dermatitis (สไลด์)
- **Cell-mediated (type IV) delayed-type hypersensitivity**
- อาการคือผื่น **eczema** (acute หรือ chronic)
- ตำแหน่งที่พบบ่อย: **มือ เท้า หน้า (รวมเปลือกตา)**
- ภาพ “Diagnosis?”: plaque สีคล้ำมีขุยรูปสี่เหลี่ยมที่ใต้สะดือ ✍️ “**ดู epidermal change ดูสาก**” · ✍️ “**ดูเหลี่ยม ๆ**” → ✍️ “**from หัวเข็มขัด**” (nickel)
- ภาพอื่น: ผื่นใต้แหวน (nickel) · patch test บวกหลายตำแหน่ง (bacitracin, chloroxylenol, 2-hydroxyethyl methacrylate — บางตัวไม่อยู่ในชุดคัดกรองมาตรฐาน)

### Irritant contact dermatitis (สไลด์)
- ✍️ “**ระคายเคือง ไม่ใช่แพ้**” · การอักเสบที่ **ไม่ผ่านภูมิคุ้มกัน** จากสารเคมี กายภาพ หรือชีวภาพ
- **80% ของ contact dermatitis เป็นชนิด irritant** และมักสัมพันธ์กับ **อาชีพ** (ภาพ: มือช่างเชื่อม)
- **Atopic dermatitis เป็นปัจจัยเสี่ยงหลักของ irritant hand dermatitis**
- Acute (รอยแดงเป็นเส้นที่แขน) vs chronic (ฝ่ามือแห้งแตก) · **ICD เรื้อรังควรทำ patch test เพื่อตัด ACD**

[[fig:contact]]

#### ทำไมถึงมีอาการนี้
| ลักษณะ | ICD | ACD |
|---|---|---|
| กลไก | สารทำลาย keratinocyte และไขมันผิวโดยตรง | hapten จับโปรตีนผิว → Langerhans cell → memory T cell → สัมผัสซ้ำแล้ว T cell กลับมา |
| ใครเป็น | **ทุกคน** ถ้าสัมผัสมาก/บ่อยพอ | เฉพาะคนที่เคย sensitize |
| เวลา | นาที–ชั่วโมงหลังสัมผัส | **24–72 ชม.** หลังสัมผัสซ้ำ (T cell ต้องเดินทางมา) |
| อาการเด่น | แสบ เจ็บ ตึง > คัน | **คันมาก** |
| ขอบเขต | จำกัดตรงที่สัมผัส | **ลามเลยขอบได้** และขึ้นที่อื่น |
| ตัวอย่าง | สบู่ น้ำ (wet work) alcohol hand rub ตัวทำละลาย กรด/ด่าง | **nickel** (หัวเข็มขัด แหวน ต่างหู) น้ำหอม สารกันเสีย ยาง ยาทา (neomycin) ยาย้อมผม (PPD) |
| Patch test | ลบ | **บวก** |

[[fig:patch]]

**ตำแหน่งบอกสาเหตุ**: ใต้สะดือ (หัวเข็มขัด nickel) · ติ่งหู (ต่างหู) · เปลือกตา (ยาทาเล็บ — มือแตะตา, เครื่องสำอาง) · หลังเท้า (ยางรองเท้า) · หน้าแข้งที่มี stasis (ยาทา) · มือ (ถุงมือยาง หรือ ICD จาก wet work)

**รักษา** (ใช้บันไดหัวข้อ 4): หา/เลี่ยงสาร (สำคัญที่สุด) · steroid ทาตามระยะ · ผื่นกว้างรุนแรง (เช่นพืชพิษ) → prednisolone สั้น ๆ · ICD มือ: ใส่ถุงมือ (มีผ้าฝ้ายด้านใน) ลด wet work ทา emollient บ่อย
""",
    ["ICD = ระคาย ไม่ผ่านภูมิ (✍️) · 80% · อาชีพ · เป็นได้ทุกคน · แสบ > คัน · ตรงที่สัมผัส",
     "ACD = type IV · ต้อง sensitize ก่อน · 24–72 ชม. · คันมาก · ลามเลยขอบได้ · patch test บวก",
     "รูปทรงเหลี่ยม/ตรงตำแหน่งวัตถุ = exogenous (✍️ ดูเหลี่ยม ๆ → หัวเข็มขัด nickel)",
     "AD เป็นปัจจัยเสี่ยงหลักของ irritant hand dermatitis",
     "ICD เรื้อรัง → patch test เพื่อตัด ACD ที่ซ้อน (สไลด์)"],
    [mcq(N(23), "A 30-year-old man has a recurrent, itchy, scaly, hyperpigmented rectangular plaque just below the umbilicus. It flares 1–2 days after he wears a particular belt. Which mechanism and confirmatory test are correct?",
         ["Type IV (T-cell–mediated) hypersensitivity to nickel; patch test", "Type I (IgE-mediated) hypersensitivity; skin prick test",
          "Direct cytotoxic irritation by friction; no test needed", "Dermatophyte infection; KOH preparation", "Immune-complex deposition; direct immunofluorescence"], 0,
         "ผื่น eczema รูปสี่เหลี่ยมตรงตำแหน่งหัวเข็มขัด (✍️ “ดูเหลี่ยม ๆ → from หัวเข็มขัด”) ขึ้น **1–2 วันหลังสัมผัส** = **allergic contact dermatitis ต่อ nickel** — **type IV delayed hypersensitivity** (สไลด์) → ยืนยันด้วย **patch test**\n\n"
         "- **Type I / prick test** — ลมพิษ/contact urticaria ภายในนาที ไม่ใช่ผื่น eczema 1–2 วัน\n- **Friction irritation** — ไม่อธิบายการขึ้นซ้ำแบบช้าเฉพาะเข็มขัดเส้นเดียว\n"
         "- **KOH** — tinea มีขอบนูนกลางจาง ไม่ผูกกับเข็มขัด\n- **DIF** — โรค autoimmune bullous/vasculitis",
         "ผื่นรูปวัตถุ + ขึ้นช้า 1–3 วัน = ACD → patch test", "Allergic contact dermatitis", R("Allergic contact dermatitis"), [ECZ, ECZ_B, HYPERS]),
     mcq(N(24), "A 34-year-old hairdresser has had dry, fissured, scaly dermatitis of the backs of both hands and finger webs for 2 years. She washes hair many times daily without gloves. Her dermatitis improves on holidays. Despite gloves and emollients for 2 months, it persists. What is the most appropriate next step?",
         ["Patch testing to exclude coexisting allergic contact dermatitis", "Skin prick testing to foods", "Serum total IgE",
          "Oral antifungal therapy", "Long-term oral prednisolone"], 0,
         "ผื่นหลังมือ ซอกนิ้ว แห้งแตกในงาน wet work ดีขึ้นตอนหยุดงาน = **irritant contact dermatitis** (80% ของ contact dermatitis สัมพันธ์อาชีพ) · แต่ช่างทำผมสัมผัส **allergen สำคัญ** (PPD ยาย้อมผม, สารกันเสีย, ยาง) และผื่นไม่หายแม้ปรับพฤติกรรม → สไลด์: **ICD เรื้อรังควรทำ patch test เพื่อตัด ACD**\n\n"
         "- **Prick test อาหาร / IgE** — สำหรับ type I ไม่ช่วยใน contact dermatitis\n- **Antifungal** — ไม่มีหลักฐาน tinea (ควร KOH ถ้าสงสัย)\n"
         "- **Prednisolone ระยะยาว** — ผลข้างเคียงมาก ไม่แก้สาเหตุ",
         "ICD เรื้อรังที่มือ → patch test ตัด ACD", "Irritant contact dermatitis", R("Irritant contact dermatitis (patch testing)"), [ECZ, ECZ_B])],
    [ECZ, ECZ_B, HYPERS, TCS, EMOL], {"contact": F.contact(), "patch": F.patch_test()},
    source="สไลด์ อ.ภูริต — Allergic contact dermatitis · Irritant contact dermatitis (หน้า 59–63)")

# ═════════════════════════════════════════════ 11
sec("derm-d1-11", "Urticaria และ angioedema — mast cell, wheal–flare, สาเหตุ และ acute vs chronic",
    "Wheal ชั่วคราว < 24 ชม. · angioedema ลึก เจ็บ บวมนาน · allergic vs non-allergic · 12 สาเหตุในสไลด์ · 6 สัปดาห์", 10,
"""### นิยาม (สไลด์)
- **Urticaria**: บวมนูนแดงขอบชัด **คัน** และ **evanescent (ชั่วคราว)** = wheal + flare (✍️ “ลมพิษ”)
- **Angioedema**: บวมของ **dermis ชั้นลึกและ subcutaneous/submucosa** — **เจ็บมากกว่าคัน ขอบไม่ชัด สีซีดหรือสีผิว** · ภาพสไลด์: ลมพิษที่หน้า คอ ลำตัว + บวมรอบตา

[[fig:mast]]

### Pathophysiology (สไลด์)
- **Allergic**: histamine เป็นตัวกลางสำคัญ · **mast cell** เป็นแหล่ง histamine หลักในผิว · allergen จับ **IgE บนผิว mast cell** → degranulation → histamine และสารอื่น → **capillary/venule รั่วเฉพาะที่**
- **Non-allergic**: mast cell แตกโดยตรงไม่ผ่าน antigen–antibody จาก **aspirin, neuropeptide, NSAID, opiate, ciprofloxacin, polymyxin, rifampicin, vancomycin**
  - กลไกของ aspirin/NSAID ที่ละเอียดกว่า (ข้อมูลเสริม): ยับยั้ง COX-1 → prostaglandin E2 (ตัวเบรก mast cell) ลด และกรด arachidonic ไปทาง **leukotriene** มากขึ้น → ลมพิษ/angioedema ไม่ผ่าน IgE จึง **เป็นกับ NSAID ทุกตัวที่ยับยั้ง COX-1** (cross-reactive) — celecoxib มักใช้ได้

#### ทำไมถึงมีอาการนี้
| อาการ | กลไก | ใช้แยกโรค |
|---|---|---|
| นูน (wheal) | histamine → H1 บน endothelium ของ venule ใน dermis บน → รอยต่อเซลล์เปิด plasma รั่ว | ✍️ “บวมจาก dermis” |
| ซีดกลาง แดงรอบ | น้ำที่บวมกดหลอดเลือดตรงกลาง · ปลายประสาทส่งสัญญาณย้อน (axon reflex) ทำให้ arteriole รอบ ๆ ขยาย = flare | wheal-and-flare = triple response ของ Lewis |
| คันมาก | histamine กระตุ้นปลายประสาท C-fiber ใน dermis บน | antihistamine ได้ผลดี (ต่างจาก eczema) |
| แต่ละวงหายใน < 24 ชม. | histamine ถูกทำลายเร็ว lymphatic ดูดน้ำกลับ | **วงเดียวอยู่ > 24–48 ชม. เจ็บ ทิ้งรอยช้ำ → urticarial vasculitis → biopsy** (ข้อมูลเสริม) |
| Angioedema บวมนาน 1–3 วัน เจ็บตึง | อยู่ในชั้นลึกที่เนื้อเยื่อหลวม เก็บน้ำได้มาก ดูดกลับช้า มีปลายประสาทรับความเจ็บมากกว่าคัน | ปาก เปลือกตา ลิ้น อวัยวะเพศ **กล่องเสียง** |

[[fig:angio]]

### สาเหตุของลมพิษ (สไลด์ 12 ข้อ)
1. **อาหาร**: สารปรุงแต่ง/กันเสีย ปลา กล้วย ถั่ว ไข่ ช็อกโกแลต ชีส
2. **ยา**: aspirin, NSAID, ยาปฏิชีวนะ เช่น penicillin
3. **สารที่หายใจ**: เกสร ฝุ่น ขนสัตว์
4. **พยาธิลำไส้**
5. **ความเครียด**
6. **แหล่งติดเชื้อ** (ฟัน ทอนซิล ทางเดินปัสสาวะ)
7. **Physical**: ร้อน เย็น น้ำ แรงสั่น แสงแดด แรงกด
8. **Cholinergic urticaria**: wheal เล็ก ๆ ร่วมกับเหงื่อออกจากความร้อนหรืออารมณ์
9. แมลงกัดต่อย
10. **Contact urticaria** (เช่นจากอาชีพ)
11. **โรคทางอายุรกรรม**: ตับอักเสบ ท่อน้ำดีอุดตัน **H. pylori**
12. **Serum sickness**

### Acute vs chronic (สไลด์)
| | Acute | Chronic |
|---|---|---|
| นิยาม | เป็นต่อเนื่องหรือเป็น ๆ หาย ๆ **< 6 สัปดาห์** | **≥ 6 สัปดาห์** |
| สาเหตุ | หาได้บ่อยกว่า: ติดเชื้อไวรัส (พบบ่อยที่สุด) ยา อาหาร แมลง | ส่วนใหญ่หาไม่พบ = **chronic idiopathic (spontaneous) urticaria** (autoimmune ต่อ IgE/FcεRI ราวครึ่งหนึ่ง — ข้อมูลเสริม) |
| ตรวจ | ไม่ต้องตรวจมากถ้าประวัติชัด | CBC with diff + ESR/CRP เป็นพื้นฐาน · ตรวจเพิ่มตามประวัติ (EAACI 2022) |

> **Angioedema ที่ไม่มีลมพิษเลย** → คิดถึง **bradykinin**: ACE inhibitor (เกิดได้แม้กินมาหลายปี) และ hereditary angioedema (C4 ต่ำ, C1-INH ต่ำ) — antihistamine/steroid/adrenaline ได้ผลน้อย ต้องหยุด ACEi (ข้อมูลเสริม — ไม่อยู่ในสไลด์)
""",
    ["Wheal = dermal edema จาก histamine (✍️ บวมจาก dermis) — แต่ละวงหายใน < 24 ชม.",
     "Angioedema = บวมลึก เจ็บ > คัน ขอบไม่ชัด อยู่ 1–3 วัน — อันตรายเมื่ออยู่ที่กล่องเสียง",
     "Allergic (IgE) vs non-allergic (mast cell แตกตรง: aspirin/NSAID, opiate, vancomycin, polymyxin, cipro, rifampicin)",
     "Acute < 6 สัปดาห์ · chronic ≥ 6 สัปดาห์ ส่วนใหญ่ idiopathic",
     "วงเดียวอยู่ > 24–48 ชม. + ทิ้งรอยช้ำ → urticarial vasculitis · angioedema ไม่มีลมพิษ → ACEi/HAE"],
    [mcq(N(25), "A 35-year-old woman develops generalized wheals and lip swelling 1 hour after taking ibuprofen for headache. She had a similar reaction to aspirin last year but tolerates paracetamol. Which mechanism best explains her reaction?",
         ["Cyclooxygenase-1 inhibition shifting arachidonic acid metabolism toward leukotrienes and activating mast cells, without specific IgE",
          "IgE antibodies specific to the ibuprofen molecule", "Immune-complex deposition in dermal vessels", "Bradykinin accumulation from inhibited kininase II",
          "Cytotoxic CD8 T cells against keratinocytes"], 0,
         "ลมพิษ/angioedema กับ **NSAID หลายตัวที่ไม่เกี่ยวข้องกันทางโครงสร้าง** (ibuprofen, aspirin) แต่ paracetamol ได้ = **non-allergic** (สไลด์: aspirin/NSAID ทำให้ mast cell แตกโดยไม่ผ่าน antigen–antibody) — กลไกคือ **ยับยั้ง COX-1** → PGE2 ลด และ leukotriene เพิ่ม จึงเป็นกับ NSAID ทุกตัวที่ยับยั้ง COX-1 (cross-reactivity)\n\n"
         "- **IgE เฉพาะยา** — จะแพ้ยาตัวเดียว ไม่ cross ทุก NSAID\n- **Immune complex** — serum sickness/urticarial vasculitis เกิดช้าเป็นวัน\n"
         "- **Bradykinin** — ACE inhibitor angioedema ไม่มีลมพิษ\n- **CD8 T cell** — SJS/TEN",
         "ลมพิษกับ NSAID หลายตัว = COX-1 → leukotriene (non-allergic)", "Urticaria — non-allergic NSAID mechanism", R("Urticaria: pathophysiology", "EAACI NSAID hypersensitivity classification"), [URT, URT_B, ADR, NSAID]),
     mcq(N(26), "A 62-year-old man taking enalapril for 4 years presents with marked swelling of the lower lip and tongue that developed over several hours. There are no wheals and no itch. Blood pressure 138/84 mmHg, SpO2 97%, no stridor. What is the most important step in management?",
         ["Stop enalapril permanently and observe the airway closely", "Switch enalapril to lisinopril", "Give oral cetirizine and discharge",
          "Start long-term prednisolone", "Reassure — angioedema cannot occur after years of ACE inhibitor use"], 0,
         "angioedema ของปาก/ลิ้น **ไม่มีลมพิษ ไม่คัน** ในผู้ที่ใช้ **ACE inhibitor** = **bradykinin-mediated angioedema** (ACE = kininase II ถูกยับยั้ง bradykinin จึงคั่ง) — เกิดได้แม้ใช้มาหลายปี · ต้อง **หยุด ACEi ตลอดไป** และเฝ้าทางเดินหายใจ (ข้อมูลเสริม — สไลด์บอกแค่ว่า angioedema เจ็บมากกว่าคัน ขอบไม่ชัด)\n\n"
         "- **เปลี่ยนเป็น ACEi ตัวอื่น** — เป็น class effect\n- **Cetirizine แล้วกลับบ้าน** — antihistamine ได้ผลน้อยในกลไก bradykinin และลิ้นบวมเสี่ยงอุดกั้นทางเดินหายใจ\n"
         "- **Prednisolone ระยะยาว** — ไม่ได้ผลกับ bradykinin\n- **“ใช้มานานแล้วไม่เป็น”** — ผิด เกิดได้ทุกเวลา",
         "Angioedema ไม่มีลมพิษ + ACEi = bradykinin → หยุด ACEi", "Angioedema — ACE inhibitor", ["EAACI/WAO angioedema guidance (ไม่อยู่ในสไลด์)"], [URT, URT_B, ADR]),
     mcq(N(27), "A 40-year-old woman has had recurrent itchy wheals almost daily for 4 months without an identifiable trigger. Which statement is correct?",
         ["This is chronic urticaria (≥ 6 weeks); most cases have no identifiable external cause", "This is acute urticaria because each wheal lasts < 24 hours",
          "Extensive allergy testing to foods usually finds the cause", "Each wheal typically lasts 3–7 days", "Systemic corticosteroids are the first-line long-term treatment"], 0,
         "สไลด์: **acute < 6 สัปดาห์ · chronic ≥ 6 สัปดาห์** และ “เมื่อไม่พบสาเหตุเรียก **chronic idiopathic urticaria**” — เป็นภาวะที่พบบ่อยที่สุดของลมพิษเรื้อรัง\n\n"
         "- **Acute เพราะแต่ละวง < 24 ชม.** — acute/chronic แบ่งตาม **ระยะเวลารวมของโรค** ไม่ใช่อายุของแต่ละวง\n- **ตรวจภูมิแพ้อาหารพบสาเหตุ** — ใน chronic spontaneous urticaria ไม่ค่อยพบ ไม่แนะนำตรวจกว้าง ๆ\n"
         "- **แต่ละวงอยู่ 3–7 วัน** — wheal อยู่ < 24 ชม. ถ้านานกว่าให้คิดถึง urticarial vasculitis\n- **Systemic steroid ระยะยาว** — ใช้แค่ระยะสั้นเมื่อกำเริบ ยาหลักคือ sgAH",
         "Chronic urticaria = ≥ 6 สัปดาห์ ส่วนใหญ่ idiopathic", "Acute vs chronic urticaria", R("Acute VS Chronic urticaria"), [URT, URT_B])],
    [URT, URT_B, ITCH, RASH, ANAPH_B, HYPERS, ADR], {"mast": F.urt_mast(), "angio": F.urt_vs_angio()},
    source="สไลด์ อ.ภูริต — Urticaria and angioedema · pathophysiology · causes · acute vs chronic (หน้า 67–73)")

# ═════════════════════════════════════════════ 12
sec("derm-d1-12", "รักษาลมพิษ — antihistamine เป็นแกน บันไดลมพิษเรื้อรัง และ angioedema ที่ทางเดินหายใจ",
    "รักษาสาเหตุ · sgAH → 4 เท่า → omalizumab → cyclosporine (EAACI 2022) · ✍️ ให้ยากิน · adrenaline IM", 8,
"""### การรักษาในสไลด์ (Urticaria: treatment)
1. **รักษาสาเหตุ** ถ้าทำได้
2. **Anti-H1 เป็น first line** — ชนิดดั้งเดิม (ง่วง): chlorpheniramine, diphenhydramine, hydroxyzine · ชนิดไม่ง่วง: **cetirizine, loratadine, fexofenadine, desloratadine**, acrivastine
3. **Anti-H2** อาจเพิ่มร่วมกับ anti-H1 (cimetidine, ranitidine)
4. **Systemic drug** (✍️ “ให้ยากิน”)
5. **ยาทาเฉพาะที่**: calamine lotion ลดความรู้สึกคัน
6. **Angioedema** ที่ทำให้ทางเดินหายใจอุดกั้น (oropharyngeal–laryngeal edema): **epinephrine 1:1,000 เป็น first line** (สไลด์เขียน “ให้ใต้ผิวหนัง” และเว้นขนาดไว้)

### บันไดลมพิษเรื้อรัง (สไลด์ Chronic urticaria: treatment — Beck LA et al. 2017)
[[fig:ladder]]
| ขั้น | EAACI/GA²LEN/EDF/WAO (ในสไลด์) | US practice parameter (ในสไลด์) |
|---|---|---|
| 1 | sgAH | sgAH เดี่ยว + เลี่ยงสิ่งกระตุ้น (NSAID, physical) |
| 2 | ไม่คุมใน 2–4 สัปดาห์ → **เพิ่ม sgAH ถึง 4 เท่า** | เพิ่มขนาด sgAH / เพิ่ม sgAH อีกตัว / H2 blocker / leukotriene antagonist / first-gen AH ก่อนนอน |
| 3 | ไม่คุมใน 2–4 สัปดาห์ → **+ omalizumab** | เพิ่ม first-gen AH (hydroxyzine, doxepin) |
| 4 | ไม่คุมใน 6 เดือน → **+ cyclosporine** | omalizumab หรือ cyclosporine · ยาต้านการอักเสบ/กดภูมิอื่น |

> **อัปเดตจากสไลด์ (EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022)**: คงบันได sgAH → ×4 → omalizumab → cyclosporine · **ไม่แนะนำ** H2 blocker หรือ montelukast เป็นขั้นมาตรฐาน และ **ไม่แนะนำ first-generation antihistamine** (ง่วง กดสมาธิ รบกวนการนอนแบบ REM) · steroid ทั้งร่างกายใช้เฉพาะ **ระยะสั้น ≤ 10 วัน** เมื่อกำเริบ · **ranitidine ถูกถอนจากตลาดปี 2020** (สาร NDMA)

#### ทำไมยาแต่ละขั้นได้ผล
| ยา | กลไก | หมายเหตุ |
|---|---|---|
| sgAH (cetirizine ฯลฯ) | inverse agonist ที่ H1 receptor บน endothelium และปลายประสาท → ไม่รั่ว ไม่คัน | ผ่านสมองน้อย จึงไม่ง่วง → เพิ่มขนาดได้ถึง 4 เท่าอย่างปลอดภัย |
| First-gen AH | ผ่าน blood–brain barrier + anticholinergic | ง่วง ปากแห้ง ปัสสาวะคั่ง สับสนในผู้สูงอายุ |
| Omalizumab | anti-IgE จับ IgE อิสระ → FcεRI บน mast cell ลดลง → mast cell แตกยาก | ได้ผลทั้งชนิด autoallergic และ autoimmune |
| Cyclosporine | ยับยั้ง calcineurin ใน T cell และลดการหลั่งจาก mast cell | เฝ้าความดันและการทำงานของไต |
| Adrenaline | α1 → หลอดเลือดหด ลดการรั่ว · β2 → หลอดลมขยาย ยับยั้งการหลั่งจาก mast cell | **ยาเดียวที่แก้ทางเดินหายใจบวม/anaphylaxis ได้ทันที** |

### Angioedema/anaphylaxis — ทางเดินหายใจ (อัปเดตจากสไลด์)
- อาการเตือน: เสียงแหบ เสียงหายใจดัง (stridor) กลืนลำบาก ลิ้นบวม ความดันตก ผื่นทั่วตัว + หอบ
- **Adrenaline 1 mg/mL (1:1,000) 0.01 mg/kg สูงสุด 0.5 mg (ผู้ใหญ่ 0.5 mL) IM ที่ต้นขาด้านนอก** ซ้ำได้ทุก 5–15 นาที (WAO/EAACI anaphylaxis) — สไลด์เขียน SC ซึ่งเป็นคำแนะนำเดิม **IM ดูดซึมเร็วและระดับยาสูงกว่า**
- ร่วมกับ: นอนราบยกขา O2 สารน้ำ · antihistamine และ steroid เป็นยาเสริม ไม่ใช่ยาหลัก · เตรียมใส่ท่อช่วยหายใจ/เจาะคอถ้ากล่องเสียงบวม
- Angioedema จาก bradykinin (ACEi, HAE): adrenaline ได้ผลน้อย → icatibant/C1-INH concentrate/FFP ตามที่มี
""",
    ["ลำดับแรก: หาและเลี่ยงสาเหตุ · ยาหลัก = second-generation H1 antihistamine",
     "Chronic: sgAH → เพิ่มถึง 4 เท่า (2–4 สัปดาห์) → omalizumab → cyclosporine",
     "2022: ไม่แนะนำ H2 blocker/montelukast/first-gen AH เป็นขั้นมาตรฐาน · steroid สั้น ≤ 10 วันเท่านั้น",
     "Angioedema ทางเดินหายใจ/anaphylaxis = adrenaline 0.5 mg IM ต้นขา (สไลด์เขียน SC — ปัจจุบัน IM)",
     "Calamine lotion ลดคันเฉพาะที่ (สไลด์)"],
    [mcq(N(28), "A 29-year-old woman with chronic spontaneous urticaria for 5 months has persistent daily wheals despite taking cetirizine 10 mg once daily regularly for 4 weeks. There is no angioedema. According to the EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022 guideline, what is the next step?",
         ["Increase cetirizine up to 4 times the standard dose (e.g., 10 mg up to four times daily)", "Add oral prednisolone 30 mg daily for 3 months",
          "Add ranitidine 150 mg twice daily", "Switch to chlorpheniramine 4 mg three times daily", "Start cyclosporine"], 0,
         "ขั้นที่ 1 (sgAH ขนาดปกติ) ไม่คุมใน 2–4 สัปดาห์ → ขั้นที่ 2 คือ **เพิ่ม sgAH ตัวเดิมได้ถึง 4 เท่า** (ตรงกับแผนภาพในสไลด์และแนวทาง 2022) — sgAH ผ่านสมองน้อยจึงเพิ่มขนาดได้ปลอดภัย\n\n"
         "- **Prednisolone 3 เดือน** — steroid ใช้แค่ระยะสั้น ≤ 10 วันเมื่อกำเริบ\n- **Ranitidine** — H2 blocker ไม่แนะนำเป็นขั้นมาตรฐานแล้ว และ ranitidine ถูกถอนจากตลาด\n"
         "- **Chlorpheniramine** — first-gen AH ง่วง ไม่แนะนำ\n- **Cyclosporine** — ขั้นที่ 4 หลัง omalizumab",
         "sgAH ไม่คุม → เพิ่มถึง 4 เท่าก่อน", "Chronic urticaria — treatment ladder", R("Chronic urticaria: treatment", "EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022"), [URT, URT_B, AH]),
     mcq(N(29), "Ten minutes after eating shrimp, a 24-year-old man develops generalized wheals, swelling of the lips and tongue, hoarseness, wheeze, and a blood pressure of 78/40 mmHg. What is the most appropriate first drug and route?",
         ["Adrenaline (epinephrine) 1 mg/mL, 0.5 mg intramuscularly into the anterolateral thigh", "Chlorpheniramine 10 mg intravenously",
          "Hydrocortisone 200 mg intravenously", "Adrenaline 1 mg intravenous bolus (1:10,000) immediately", "Salbutamol nebulization alone"], 0,
         "ลมพิษ + angioedema ลิ้น/กล่องเสียง (เสียงแหบ) + หลอดลมตีบ + ความดันตก = **anaphylaxis** → ยาแรกคือ **adrenaline 0.5 mg IM ที่ต้นขาด้านนอก** ซ้ำได้ทุก 5–15 นาที · สไลด์ระบุ adrenaline 1:1,000 เป็น first line ใน angioedema ที่ทางเดินหายใจ (สไลด์เขียน SC — ปัจจุบันแนะนำ IM เพราะดูดซึมเร็วกว่า)\n\n"
         "- **Chlorpheniramine / hydrocortisone** — ยาเสริม ไม่แก้ทางเดินหายใจบวมหรือความดันตกทันที\n"
         "- **Adrenaline 1 mg IV bolus** — ขนาดสำหรับ cardiac arrest เสี่ยงหัวใจเต้นผิดจังหวะ (IV ใช้แบบหยด/ขนาดเล็กโดยผู้ชำนาญเมื่อ IM หลายครั้งไม่ได้ผล)\n- **Salbutamol อย่างเดียว** — แก้แค่หลอดลม",
         "Anaphylaxis = adrenaline 0.5 mg IM ต้นขา", "Angioedema/anaphylaxis — adrenaline", R("Urticaria: treatment (angioedema)", "WAO Anaphylaxis Guidance 2020"), [URT, SHOCK, ANAPH_B])],
    [URT, URT_B, AH, ANAPH_B, SHOCK, CS], {"ladder": F.urt_ladder()},
    source="สไลด์ อ.ภูริต — Urticaria: treatment · Chronic urticaria: treatment (หน้า 74–75) + EAACI/GA²LEN/EuroGuiDerm/APAAACI 2022 · WAO anaphylaxis 2020")
