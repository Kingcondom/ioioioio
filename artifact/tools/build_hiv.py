#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AIDS and HIV infection (พ.ญ.มนัสวี · Manasawee Wantanatavatod) → data/id.json
ต้นฉบับ: Drive 13PhGovTDoDXERCeB2zfMC1_1nZq2mAlJ "HIV and AIDS พ.ญ.มนัสวี.pdf" · บรรยาย จ. 5 ต.ค. 2569
โน้ตสไลด์: slides/hiv_notes.md — สไลด์ที่เป็นตาราง/ภาพ (WHO staging, สูตรยาแรก, ตาราง OI prophylaxis,
การรักษา cryptococcosis) ไม่มีข้อความ → เนื้อหาส่วนนั้นอิงแนวทางไทย/WHO และระบุไว้ในบทเรียน
ไม่มีข้อสอบในคลัง Ward Drill สำหรับคาบนี้ — ข้อสอบเขียนใหม่ทั้งหมด"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
NLN = ["2.3.1(9)"]
SRC = "สไลด์ พ.ญ.มนัสวี — AIDS and HIV infection (2026)"
S = []
def sec(sid, title, summary, minutes, md, pearls, items, nl=None):
    S.append({"id": sid, "title": title, "summary": summary, "minutes": minutes, "source": SRC,
              "nl": nl or NLN, "md": md, "pearls": pearls, "items": items})
def mcq(iid, stem, choices, answer, explain, pearl, topic, ref, nl=None):
    assert len(choices) == 5 and 0 <= answer <= 4
    return {"id": iid, "kind": "mcq", "stem": stem, "choices": choices, "answer": answer,
            "explain": explain, "pearl": pearl, "topic": topic, "src": "", "ref": ref, "nl": nl or NLN}
N = lambda n: "ID-HIV-MCQ-%02d" % n
R = lambda p: ["สไลด์ พ.ญ.มนัสวี — " + p]
TG = "แนวทางการตรวจรักษาและป้องกันการติดเชื้อเอชไอวี ประเทศไทย 2025"

# ───────────────────────────── 1
sec("id-hiv-01", "ไวรัสและกลไก — ทำไม CD4 คือเป้าหมาย",
    "HIV-1 กับ HIV-2 · วงจรชีวิตของไวรัส · ยาแต่ละกลุ่มตัดวงจรตรงไหน", 9,
"""### ตัวไวรัส
**HIV** อยู่ในสกุล **Lentivirus** วงศ์ **Retroviridae** มีสองสปีชีส์
| | **HIV-1** | **HIV-2** |
|---|---|---|
| ความชุก | **ราว 95% ทั่วโลก** | แอฟริกาตะวันตกเป็นหลัก |
| ความรุนแรง | สูง | **ต่ำกว่า** แพร่ยากกว่า |
| สายพันธุ์ | group M, O, N · M แบ่ง subtype A–K · **CRF01_AE พบมากในเอเชียตะวันออกเฉียงใต้** | ต่างจาก HIV-1 มากกว่า 55% |
| **การตอบสนองต่อยา** | ไวต่อ NNRTI | **ดื้อ NNRTI โดยกำเนิด** → ใช้ integrase inhibitor หรือ protease inhibitor |

### ทำไมผู้ป่วยติดเชื้อฉวยโอกาส
HIV ติดเชื้อและทำลาย **CD4+ T cell** (รวมถึง macrophage และ dendritic cell) ซึ่งเป็นแกนของ **ภูมิคุ้มกันระดับเซลล์ (cell-mediated immunity)** ที่ใช้กำจัด **เชื้อที่อยู่ในเซลล์** — วัณโรค เชื้อรา (Pneumocystis, Cryptococcus, Talaromyces, Histoplasma) MAC และไวรัส เมื่อ CD4 ลดลง เชื้อเหล่านี้จึงก่อโรคได้เป็นลำดับตามระดับ CD4

### วงจรชีวิตของไวรัส และยาที่ตัดแต่ละขั้น
| ขั้น | เกิดอะไร | ยาที่ตัดขั้นนี้ |
|---|---|---|
| **1. จับเซลล์** | **gp120** ของไวรัสจับ **CD4** (ร่วมกับ co-receptor CCR5/CXCR4) | **Attachment inhibitor** (fostemsavir — จับ gp120) · **Post-attachment inhibitor** (ibalizumab — จับ CD4) · **CCR5 antagonist** (maraviroc) |
| **2. หลอมเยื่อหุ้ม** | ไวรัสหลอมกับเยื่อหุ้มเซลล์ ปล่อย capsid เข้าไป | **Fusion inhibitor** (enfuvirtide) |
| **3. Reverse transcription** | **reverse transcriptase** ลอก RNA เป็น DNA | **NRTI** (TDF, TAF, 3TC, FTC, ABC, AZT) · **NNRTI** (EFV, RPV, NVP, ETR, DOR) |
| **4. Integration** | **integrase** แทรก DNA ไวรัสเข้า genome ของเซลล์ | **INSTI** (dolutegravir, bictegravir, cabotegravir, raltegravir) |
| **5. ประกอบตัว** | **protease** ตัดโปรตีนให้เป็นไวรัสที่สมบูรณ์ | **PI** (darunavir, lopinavir, atazanavir, ritonavir) |
| (capsid) | เปลือกหุ้มสารพันธุกรรม | **Capsid inhibitor** (lenacapavir) |

### ART ทำอะไรได้ และทำอะไรไม่ได้
**ART ช่วยชีวิต แต่ไม่ทำให้หายขาด** — เพราะ DNA ของไวรัสฝังอยู่ใน genome ของเซลล์ที่พักตัว (latent reservoir)
เมื่อกินยาสม่ำเสมอ ART จะ **ลดปริมาณไวรัส · ลดการแพร่เชื้อ · ป้องกันไม่ให้เป็น AIDS · ปกป้องระบบภูมิคุ้มกัน · ทำให้อายุขัยใกล้คนปกติ**
""",
    ["HIV-1 ราว 95% · HIV-2 แอฟริกาตะวันตก ดื้อ NNRTI โดยกำเนิด",
     "HIV ทำลาย CD4 → เสียภูมิคุ้มกันระดับเซลล์ต่อเชื้อในเซลล์",
     "gp120 จับ CD4 → RT → integrase → protease",
     "NRTI/NNRTI ตัด RT · INSTI ตัด integrase · PI ตัด protease",
     "ART ไม่ทำให้หายขาด เพราะมี latent reservoir"],
    [mcq(N(1), "A man from West Africa is diagnosed with HIV-2 infection. Which drug class should NOT be relied on in his regimen?",
         ["Integrase strand transfer inhibitors", "Protease inhibitors", "Nucleoside reverse transcriptase inhibitors",
          "Non-nucleoside reverse transcriptase inhibitors", "Pharmacokinetic boosters"], 3,
         "สไลด์ตาราง HIV-1 vs HIV-2: **HIV-2 ดื้อ NNRTI โดยกำเนิด** (efavirenz, rilpivirine, doravirine, nevirapine) เพราะตำแหน่งจับยาบน reverse transcriptase ต่างจาก HIV-1 → สูตรยาต้องใช้ **integrase inhibitor หรือ protease inhibitor** ร่วมกับ NRTI\n\nHIV-2 พบมากใน **แอฟริกาตะวันตก** และมีความรุนแรงต่ำกว่า HIV-1",
         "HIV-2 → ห้ามพึ่ง NNRTI", "HIV-2 and NNRTI", R("HIV-1 vs HIV-2")),
     mcq(N(2), "Dolutegravir blocks which step of the HIV replication cycle?",
         ["Binding of gp120 to CD4", "Fusion of viral and cell membranes", "Reverse transcription of viral RNA into DNA",
          "Integration of viral DNA into the host genome", "Cleavage of viral polyproteins by protease"], 3,
         "**Dolutegravir** เป็น **integrase strand transfer inhibitor (INSTI)** — ยับยั้ง integrase ไม่ให้แทรก DNA ของไวรัสเข้า genome ของเซลล์\n\nเทียบ: **NRTI/NNRTI** ยับยั้ง reverse transcriptase · **PI** ยับยั้ง protease · **fostemsavir** จับ gp120 · **enfuvirtide** ยับยั้งการหลอมเยื่อหุ้ม",
         "INSTI (DTG, BIC, CAB, RAL) ยับยั้ง integrase", "ART mechanism", R("Replication cycle / FDA-approved HIV medicines"), NLN + ["B1.5.3(3)"]),
    ], NLN + ["B1.5.3(3)", "B1.4.10(2)"])

# ───────────────────────────── 2
sec("id-hiv-02", "การติดต่อ และ U=U",
    "เพศสัมพันธ์มากกว่า 80% · ปัจจัยสำคัญที่สุดคือปริมาณไวรัส · กดไวรัสได้ = ไม่แพร่เชื้อ", 7,
"""### สามทางหลัก (สไลด์)
| ทาง | รายละเอียด |
|---|---|
| **เพศสัมพันธ์** | **มากกว่า 80% ของผู้ติดเชื้อทั่วโลก** |
| **ทางเลือด** | ใช้เข็มฉีดยาร่วมกัน |
| **แม่สู่ลูก** | ในครรภ์ ระหว่างคลอด หรือทางนมแม่ |

### ปัจจัยที่เพิ่มการแพร่ทางเพศสัมพันธ์
1. **ปริมาณไวรัส (viral load) สูง — ปัจจัยสำคัญที่สุด** (จึงแพร่ง่ายมากในช่วง acute HIV ที่ไวรัสสูงที่สุด)
2. **มีโรคติดต่อทางเพศสัมพันธ์ร่วม โดยเฉพาะแผลที่อวัยวะเพศ** (ซิฟิลิส เริม แผลริมอ่อน) — เยื่อบุเสียและมีเซลล์เป้าหมายมารวมกันที่แผล
3. **พฤติกรรม** — หลายคู่ ไม่ใช้ถุงยาง มีเพศสัมพันธ์ขณะใช้สารเสพติด **การร่วมเพศทางทวารหนัก** (เยื่อบุบางชั้นเดียว)
- **การขลิบอวัยวะเพศชายลดความเสี่ยง** (ผิวด้านในหนังหุ้มปลายมีเซลล์เป้าหมายมาก)

### ความเสี่ยงต่อครั้ง (Smith, MMWR 2005 — ตัวเลขที่ใช้กันทั่วไป)
| การสัมผัส | ความเสี่ยงต่อครั้ง |
|---|---|
| รับเลือด | ~90% |
| ใช้เข็มฉีดยาร่วม | ~0.67% |
| **ร่วมเพศทางทวารหนัก ฝ่ายรับ** | **~0.5%** (สูงสุดในทางเพศ) |
| เข็มตำ (บุคลากร) | ~0.3% |
| ร่วมเพศทางช่องคลอด ฝ่ายรับ | ~0.1% |
| ทางปาก | ต่ำมาก |

### U=U — Undetectable = Untransmittable
**ผู้ที่กินยาต้านจนกดไวรัสในเลือดได้ต่ำกว่า 200 copies/mL อย่างต่อเนื่อง จะไม่แพร่เชื้อให้คู่นอนทางเพศสัมพันธ์** (DHHS)
→ ART จึงเป็นทั้ง **การรักษา** และ **การป้องกัน (treatment as prevention)** ในคราวเดียว
""",
    ["ทางเพศสัมพันธ์ > 80% · ปัจจัยสำคัญที่สุด = viral load สูง",
     "แผลที่อวัยวะเพศและ anal sex เพิ่มความเสี่ยง · การขลิบลดความเสี่ยง",
     "Receptive anal ~0.5%/ครั้ง สูงสุดในทางเพศ · เข็มตำ ~0.3%",
     "U=U: VL < 200 copies/mL ต่อเนื่อง → ไม่แพร่ทางเพศสัมพันธ์"],
    [mcq(N(3), "Which single factor most strongly determines the risk of sexual transmission of HIV from an infected partner?",
         ["The partner's CD4 count", "The partner's plasma HIV viral load", "Whether the partner has HIV-1 subtype B",
          "The partner's age", "The duration of the relationship"], 1,
         "สไลด์ transmission: **viral load สูงคือปัจจัยที่สำคัญที่สุด** ของการแพร่ทางเพศสัมพันธ์ — ความเสี่ยงเพิ่มตามปริมาณไวรัสในเลือดและสารคัดหลั่ง\n\nหลักฐานกลับด้านคือ **U=U**: เมื่อกดไวรัสได้ต่ำกว่า 200 copies/mL ต่อเนื่อง จะ **ไม่แพร่เชื้อทางเพศสัมพันธ์** · ช่วง **acute HIV** ที่ไวรัสสูงมากจึงเป็นช่วงที่แพร่ง่ายที่สุด",
         "ปัจจัยแพร่ทางเพศที่สำคัญที่สุด = viral load", "Determinants of transmission", R("Transmission")),
     mcq(N(4), "A man living with HIV has taken ART consistently for 2 years, with all viral loads below 50 copies/mL. He asks whether he can transmit HIV to his HIV-negative partner through condomless sex. What is the correct counselling?",
         ["Yes, the risk is about 0.1% per act", "Yes, unless his CD4 count is above 500",
          "No: sustained plasma HIV RNA below 200 copies/mL prevents sexual transmission (U=U)", "No, because ART cures HIV after 2 years", "He must stop ART before conceiving"], 2,
         "สไลด์ **Undetectable = Untransmittable** (DHHS): การใช้ ART จนกด **HIV RNA < 200 copies/mL ป้องกันการแพร่เชื้อสู่คู่นอนทางเพศสัมพันธ์**\n\nข้อควรเสริมในการให้คำปรึกษา: **ต้องกินยาต่อเนื่องและตรวจ viral load ตามนัด** · U=U ไม่ป้องกันโรคติดต่อทางเพศสัมพันธ์อื่น · ART **ไม่ได้ทำให้หายขาด**",
         "U=U: VL < 200 ต่อเนื่อง = ไม่แพร่ทางเพศ", "U=U counselling", R("ART to prevent sexual transmission")),
    ], NLN + ["2.3.1(19)"])

# ───────────────────────────── 3
sec("id-hiv-03", "ธรรมชาติของโรค และ acute HIV",
    "acute retroviral syndrome → ระยะสงบ 7–10 ปี → CD4 < 200 = AIDS · acute HIV เลียนแบบ mononucleosis", 9,
"""### ธรรมชาติของโรค
| ระยะ | เวลา | สิ่งที่เกิด |
|---|---|---|
| **Acute retroviral syndrome** | **6–12 สัปดาห์แรก** | ไวรัสพุ่งสูงมาก CD4 ลดชั่วคราว แพร่เชื้อง่ายที่สุด |
| **Clinical latency** | **7–10 ปี** | ไม่มีอาการ แต่ไวรัสแบ่งตัวและ CD4 ลดลงช้า ๆ ตลอด |
| **AIDS** | เมื่อ **CD4 < 200 cells/mm³** หรือเกิดโรคที่บ่งชี้ AIDS | ติดเชื้อฉวยโอกาสและมะเร็ง |

### Acute/early HIV (DHHS)
- อาการเริ่ม **2–4 สัปดาห์หลังติดเชื้อ** · **ราว 30% ไม่มีอาการ**
- **คล้าย infectious mononucleosis** (EBV, CMV)
| ระบบ | อาการ |
|---|---|
| ทั่วไป | ไข้ อ่อนเพลีย ปวดกล้ามเนื้อ เหงื่อออกกลางคืน น้ำหนักลด |
| ต่อมน้ำเหลือง | รักแร้ คอ ท้ายทอย · **PGL = โต ≥ 2 ตำแหน่ง นาน ≥ 3 เดือน** |
| ช่องปาก | เจ็บคอ **แผลในปากที่เจ็บ** |
| ผิวหนัง | **ผื่นทั่วตัว (พบบ่อย)** |
| ทางเดินอาหาร | คลื่นไส้ ท้องเสีย เบื่ออาหาร |
| ระบบประสาท | **ปวดศีรษะ (พบบ่อย)** · พบน้อยแต่รุนแรง: aseptic meningitis, demyelinating polyneuropathy, mononeuritis multiplex |

**ทำไมต้องจับให้ได้** — วินิจฉัยเร็ว → รักษาเร็ว → โรคดำเนินช้าลง และ **ลดการแพร่เชื้อ** (ช่วงนี้ไวรัสสูงที่สุด)

### กฎสำคัญจากสไลด์
**วินิจฉัยโรคติดต่อทางเพศสัมพันธ์ใด ๆ → ต้องตรวจ HIV และคิดถึง acute HIV เสมอ**

### การวินิจฉัยแยกโรค
EBV และ non-EBV mononucleosis (เช่น CMV) · COVID-19 · ไข้หวัดใหญ่ · ตับอักเสบจากไวรัส · ติดเชื้อ streptococcus · **ซิฟิลิส (secondary syphilis ก็มีไข้ ผื่น ต่อมน้ำเหลืองโต)**

**กับดัก** — ในช่วง acute HIV แอนติบอดียังอาจไม่ขึ้น การตรวจที่จับได้ต้องเป็น **4th generation (มี p24 antigen)** หรือ **HIV RNA**

### Long-term nonprogressor (LTNP)
- ส่วนน้อยที่คง **CD4 > 500 และ VL < 5,000 copies/mL นาน ≥ 8 ปีโดยไม่มี ART** · ราว **1–5%**
- **Elite controller** — VL ตรวจไม่พบ (< 50) โดยไม่กินยา — พบน้อยมาก
- ขึ้นกับปัจจัยของผู้ป่วย พันธุกรรม และไวรัส
""",
    ["Acute HIV 2–4 สัปดาห์หลังติด · 30% ไม่มีอาการ · คล้าย mononucleosis",
     "ไข้ ผื่น เจ็บคอ แผลในปาก ต่อมน้ำเหลืองโต ปวดศีรษะ",
     "เป็น STI ใด ๆ → ตรวจ HIV และคิดถึง acute HIV",
     "Clinical latency 7–10 ปี · CD4 < 200 = AIDS",
     "LTNP: CD4 > 500 + VL < 5,000 ≥ 8 ปี ไม่มียา (1–5%)"],
    [mcq(N(5), "A 22-year-old man has 5 days of fever, sore throat with painful oral ulcers, a generalised maculopapular rash and cervical lymphadenopathy. He was treated for gonorrhoea 4 weeks ago. Monospot is negative. Which test is most appropriate to detect his most likely diagnosis?",
         ["HIV antibody-only rapid test", "Fourth-generation HIV antigen/antibody test with HIV RNA if negative or indeterminate",
          "CD4 count alone", "Repeat Monospot in 2 weeks", "Throat culture only"], 1,
         "ภาพของ **acute retroviral syndrome** — ไข้ เจ็บคอ **แผลในปากที่เจ็บ ผื่นทั่วตัว** ต่อมน้ำเหลืองโต **2–4 สัปดาห์หลังสัมผัส** และเพิ่งเป็น **STI** (สไลด์: STI ใด ๆ → ตรวจ HIV และคิดถึง acute HIV)\n\nช่วงนี้แอนติบอดีอาจยังไม่ขึ้น → ต้องใช้ **4th generation (ตรวจ p24 antigen ด้วย)** และถ้ายังสงสัยให้ตรวจ **HIV RNA (NAT)**\n\nการตรวจแอนติบอดีอย่างเดียวอาจได้ผลลบปลอม · CD4 ไม่ใช่การตรวจวินิจฉัย",
         "Acute HIV → 4th gen Ag/Ab ± HIV RNA", "Acute HIV diagnosis", R("Acute/early HIV infection"), NLN + ["3.3.15", "2.3.1(19)"]),
     mcq(N(6), "Which definition best fits a long-term nonprogressor (LTNP) with HIV?",
         ["CD4 below 200 within 2 years of infection", "CD4 above 500 and viral load below 5,000 copies/mL for at least 8 years without ART",
          "Undetectable viral load only while taking ART", "Negative HIV antibody despite positive HIV RNA", "HIV-2 infection with high viral load"], 1,
         "สไลด์ LTNP: **CD4 > 500/µL และ viral load < 5,000 copies/mL นาน ≥ 8 ปีโดยไม่มี ART** · พบราว **1–5%** ของผู้ติดเชื้อ\n\n**Elite controller** เป็นกลุ่มย่อยที่ VL ตรวจไม่พบ (< 50 copies/mL) โดยไม่กินยา · ความต่างเกิดจากปัจจัยของผู้ป่วย พันธุกรรม และไวรัส",
         "LTNP: CD4 > 500 + VL < 5,000 ≥ 8 ปี ไม่มียา", "Long-term nonprogressor", R("Long-term nonprogressor")),
    ], NLN + ["2.1.57"])

# ───────────────────────────── 4
sec("id-hiv-04", "WHO clinical staging และโรคที่บ่งชี้ AIDS",
    "สี่ระยะตามอาการ · AIDS = CD4 < 200 หรือ stage 4 · โรคที่บ่งชี้ระดับ CD4", 8,
"""สไลด์ WHO clinical staging เป็นตารางภาพ ส่วนนี้สรุปตาม **WHO clinical staging of HIV disease ในผู้ใหญ่** ที่ใช้ในแนวทางไทย

| Stage | ตัวอย่างอาการ/โรค |
|---|---|
| **1** | ไม่มีอาการ · **persistent generalized lymphadenopathy (PGL)** |
| **2** | น้ำหนักลด **< 10%** · ติดเชื้อทางเดินหายใจส่วนบนซ้ำ · **งูสวัด** · แผลมุมปาก แผลร้อนในซ้ำ · **ผื่นคัน PPE** · seborrheic dermatitis · เชื้อราที่เล็บ |
| **3** | น้ำหนักลด **> 10%** · ท้องเสียเรื้อรัง **> 1 เดือน** · ไข้เรื้อรัง **> 1 เดือน** · **เชื้อราในช่องปาก** · **oral hairy leukoplakia** · **วัณโรคปอด** · ติดเชื้อแบคทีเรียรุนแรง · เหงือกอักเสบเนื้อตาย · ซีด/เม็ดเลือดขาวต่ำ/เกล็ดเลือดต่ำ ไม่ทราบสาเหตุ |
| **4 (AIDS)** | **HIV wasting** · **PCP** · ปอดอักเสบแบคทีเรียซ้ำ · **เริมเรื้อรัง > 1 เดือน** · **เชื้อราในหลอดอาหาร** · **วัณโรคนอกปอด** · **Kaposi sarcoma** · **CMV** · **toxoplasmosis สมอง** · HIV encephalopathy · **cryptococcosis นอกปอด** · **disseminated NTM (MAC)** · PML · **talaromycosis** · **histoplasmosis** · lymphoma · มะเร็งปากมดลูกระยะลุกลาม |

### AIDS
**CD4 < 200 cells/mm³ หรือมีโรคใน stage 4** อย่างใดอย่างหนึ่ง

### CD4 บอกว่าควรนึกถึงเชื้ออะไร
| CD4 (cells/mm³) | เชื้อฉวยโอกาสที่เริ่มพบ |
|---|---|
| **ทุกระดับ** (มากขึ้นเมื่อ CD4 ต่ำ) | **วัณโรค** · ปอดอักเสบแบคทีเรีย · งูสวัด |
| **< 200** | **PCP** · เชื้อราในปาก/หลอดอาหาร |
| **< 150** | **Histoplasmosis** |
| **< 100** | **Cryptococcosis** · **Talaromycosis** · **Toxoplasmosis** |
| **< 50** | **Disseminated MAC** · **CMV retinitis** |

**People with advanced HIV disease** (ตามสไลด์และ WHO) = **CD4 < 200 หรือ WHO stage 3–4** — กลุ่มนี้ต้องได้ชุดคัดกรองและป้องกันโรคฉวยโอกาสเต็มรูปแบบ (หัวข้อ 12)
""",
    ["Stage 1 PGL · 2 งูสวัด น้ำหนักลด < 10% · 3 oral candida, OHL, TB ปอด · 4 PCP, EPTB, crypto, MAC, talaro, histo",
     "AIDS = CD4 < 200 หรือ stage 4",
     "CD4 < 200 PCP · < 150 histo · < 100 crypto/talaro/toxo · < 50 MAC/CMV",
     "Advanced HIV disease = CD4 < 200 หรือ stage 3–4"],
    [mcq(N(7), "A man with newly diagnosed HIV has oral candidiasis and has lost 12% of his body weight over 4 months. He has no other illnesses. Under WHO clinical staging, which stage is he?",
         ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Cannot be staged without a CD4 count"], 2,
         "**Oral candidiasis** และ **น้ำหนักลดมากกว่า 10%** เป็นเกณฑ์ของ **WHO stage 3** (น้ำหนักลดน้อยกว่า 10% เป็น stage 2)\n\nถ้าเชื้อราลามไปที่ **หลอดอาหาร** จะเป็น **stage 4** · WHO clinical staging ใช้อาการ **ไม่ต้องใช้ CD4**",
         "Oral candida + น้ำหนักลด > 10% = stage 3 · esophageal candida = stage 4", "WHO staging", ["WHO clinical staging of HIV disease (สไลด์เป็นภาพ)"]),
     mcq(N(8), "At which CD4 count does disseminated Mycobacterium avium complex infection typically occur?",
         ["Below 500 cells/µL", "Below 350 cells/µL", "Below 200 cells/µL", "Below 100 cells/µL", "Below 50 cells/µL"], 4,
         "สไลด์ MAC: **disseminated MAC เกิดใน PLWH ที่ CD4 < 50 cells/µL** — ระดับต่ำที่สุดในบรรดาเชื้อฉวยโอกาส ร่วมกับ CMV retinitis\n\nลำดับที่ควรจำ: **PCP < 200 · histoplasmosis < 150 · cryptococcus / talaromyces / toxoplasma < 100 · MAC / CMV < 50**",
         "MAC และ CMV: CD4 < 50", "CD4 thresholds for OI", R("Mycobacterium avium complex")),
    ], NLN + ["2.3.1-3(6)"])

# ───────────────────────────── 5
sec("id-hiv-05", "ใครควรตรวจ HIV และหลัก 5C",
    "11 กลุ่มที่ต้องตรวจ · ยินยอม ปรึกษา ปกปิด ผลถูกต้อง ส่งต่อเข้ารักษา", 7,
"""### หลัก 5C ขององค์การอนามัยโลก (แนวทางไทย 2025)
| C | ความหมาย |
|---|---|
| **Consent** | ต้องได้รับ **ความยินยอม** จากผู้รับการตรวจ |
| **Counseling** | ให้คำปรึกษา **ทั้งก่อนและหลัง** การตรวจ |
| **Confidential** | **เก็บรักษาความลับ** อย่างเคร่งครัด |
| **Correct test result** | ผลการตรวจต้อง **ถูกต้องและชัดเจน** |
| **Connection to care** | ผลบวก → **ส่งเข้าระบบการรักษาด้วยยาต้านโดยเร็ว** |

### ผู้ที่ควรได้รับการตรวจ (แนวทางไทย 2025)
1. มี **อาการหรืออาการแสดง** ที่เข้าได้กับ HIV หรือ AIDS
2. มีหรือเคยมี **เพศสัมพันธ์โดยไม่ป้องกัน** — ทั้งชาย–ชาย และชาย–หญิง
3. **ผู้ป่วยวัณโรค**
4. **ผู้ติดโรคติดต่อทางเพศสัมพันธ์**
5. **ผู้ใช้ยาเสพติดชนิดฉีดและใช้เข็มร่วมกัน**
6. **หญิงตั้งครรภ์และสามี**
7. **ทารกที่เกิดจากมารดาติดเชื้อ**
8. **บุคลากรทางการแพทย์ที่เกิดอุบัติเหตุ** เสี่ยงติดเชื้อ
9. **ผู้ถูกล่วงละเมิดทางเพศ** และผู้ถูกกล่าวหา
10. ผู้ที่ต้องการตรวจ **ก่อนแต่งงาน** หรือคู่ที่ต้องการมีบุตร
11. ผู้ที่กำลังรับ **PrEP หรือ PEP**

**เหตุผลของข้อ 3–4** — วัณโรคและ STI เป็นทั้ง **ผลของ HIV** และ **ปัจจัยเสี่ยงร่วม** จึงต้องตรวจคู่กันเสมอ (เหมือนในคาบ Extrapulmonary TB: ผู้ป่วยวัณโรคทุกรายต้องตรวจ HIV)

### PrEP และ PEP (ยาจากสไลด์ FDA timeline)
- **PrEP (ก่อนสัมผัส)** — TDF/FTC (Truvada) · TAF/FTC (Descovy) · cabotegravir ฉีด
- **PEP (หลังสัมผัส)** — เริ่ม **ภายใน 72 ชั่วโมง** ยิ่งเร็วยิ่งดี กิน **28 วัน** (ตามแนวทางทั่วไป)
""",
    ["5C: Consent · Counseling ก่อน-หลัง · Confidential · Correct result · Connection to care",
     "ต้องตรวจ HIV: ผู้ป่วยวัณโรค · STI · หญิงตั้งครรภ์และสามี · IDU · บุคลากรเกิดอุบัติเหตุ · ผู้ถูกล่วงละเมิด",
     "PEP เริ่มภายใน 72 ชม. กิน 28 วัน"],
    [mcq(N(9), "Which of the following is NOT one of the WHO '5C' principles of HIV testing used in the Thai guideline?",
         ["Consent", "Counseling before and after testing", "Confidentiality", "Compulsory testing of all hospital admissions", "Connection to care"], 3,
         "หลัก **5C**: **Consent · Counseling · Confidential · Correct test result · Connection to care**\n\nการตรวจ **ภาคบังคับโดยไม่ได้รับความยินยอม** ขัดกับหลัก Consent โดยตรง การตรวจต้องเกิดจากความสมัครใจหลังได้รับคำปรึกษา",
         "5C = Consent, Counseling, Confidential, Correct, Connection", "5C principles", R("HIV diagnosis — 5C"), NLN + ["3.3.15"]),
     mcq(N(10), "Which patient group is specifically listed in the Thai 2025 guideline as requiring HIV testing even without symptoms of HIV?",
         ["Patients with newly diagnosed tuberculosis", "Patients with essential hypertension", "Patients with osteoarthritis",
          "Healthy blood donors under 18 years", "Patients with migraine"], 0,
         "แนวทางไทย 2025 ระบุ **ผู้ป่วยวัณโรค** เป็นหนึ่งใน 11 กลุ่มที่ต้องตรวจ HIV ร่วมกับ ผู้ติด STI · ผู้ใช้ยาฉีด · หญิงตั้งครรภ์และสามี · ทารกจากแม่ติดเชื้อ · บุคลากรที่เกิดอุบัติเหตุ · ผู้ถูกล่วงละเมิดทางเพศ · ผู้รับ PrEP/PEP\n\nเหตุผล: วัณโรคเป็นโรคฉวยโอกาสที่พบบ่อยที่สุดในผู้ติดเชื้อ HIV และผล HIV เปลี่ยนการรักษา (จังหวะเริ่ม ART ยาตีกันกับ rifampicin)",
         "ผู้ป่วยวัณโรคทุกรายต้องตรวจ HIV", "Who to test", R("ผู้ที่ควรได้รับการตรวจ"), NLN + ["3.3.15", "2.3.1(20)"]),
    ], NLN + ["3.3.15"])

# ───────────────────────────── 6
sec("id-hiv-06", "การตรวจวินิจฉัย — 4th generation, window period และขั้นตอน A1–A2–A3",
    "NAT · Ag/Ab combo · Ab อย่างเดียว · ตรวจสามชุดเรียงกัน · ผลสรุปไม่ได้ตรวจซ้ำ 2 สัปดาห์", 9,
"""### การตรวจสามชนิด (แนวทางไทย 2025)
| ชนิด | ตรวจอะไร | ใช้เมื่อไร |
|---|---|---|
| **Nucleic acid test (NAT)** | **HIV RNA** | สงสัยติดเชื้อในช่วง window · ทารก · วัดปริมาณไวรัส (VL) |
| **Antigen/antibody combination (4th generation)** | **p24 antigen + IgM/IgG** ต่อ HIV-1/2 | **การตรวจคัดกรองหลัก** |
| **Antibody อย่างเดียว** | IgM/IgG | ชุดยืนยันลำดับหลัง |

### ลำดับที่ตรวจพบหลังติดเชื้อ
**HIV RNA (ราว 10 วัน) → p24 antigen → antibody**
- **4th generation** ตรวจพบได้เร็วเพราะมี p24 — สไลด์ไทยระบุ window ราว **2 สัปดาห์** และ **พบการติดเชื้อส่วนใหญ่ภายใน 4 สัปดาห์**
- **ผลลบครั้งแรกหลังสัมผัสเสี่ยง → ตรวจซ้ำที่ 12 สัปดาห์** เพื่อยืนยันว่าไม่ติดเชื้อ

### ขั้นตอนการตรวจของไทย — สามชุดเรียงกัน
| ชุด | คุณสมบัติ |
|---|---|
| **A1** | **ตรวจได้ทั้ง antigen และ antibody (4th gen) — ไวสูงสุด** ใช้คัดกรอง |
| **A2** | ตรวจ Ag/Ab หรือ Ab อย่างเดียว · ใช้ antigen ต่างจาก A1 · **จำเพาะสูงกว่า A1** |
| **A3** | ตรวจ **Ab อย่างเดียว** · antigen ต่างจาก A1 และ A2 · **จำเพาะสูงกว่า A2** |
- **A1 ลบ** → ไม่พบการติดเชื้อ (ถ้าไม่อยู่ใน window)
- **A1 บวก → A2 บวก → A3 บวก** → **ติดเชื้อ**
- ผลขัดแย้งกัน → **สรุปไม่ได้ (inconclusive)**

**หลักคิด** — ชุดแรกเน้น **ไว** เพื่อไม่ให้หลุด ชุดต่อมาเน้น **จำเพาะ** เพื่อตัดผลบวกลวง

### ผลสรุปไม่ได้ (inconclusive)
- **ตรวจซ้ำที่ 2 สัปดาห์** ถ้ายังสรุปไม่ได้เหมือนเดิม → **สรุปว่ายังไม่พบการติดเชื้อ**
- ถ้าประเมินว่า **อาจอยู่ใน window period** → ส่ง **qualitative NAT** หรือ **HIV viral load** เพิ่ม เพื่อให้เริ่มยาต้านได้เร็ว
""",
    ["NAT (RNA) → p24 → antibody · 4th gen ตรวจ p24 + Ab",
     "4th gen ตรวจพบส่วนใหญ่ใน 4 สัปดาห์ · ลบหลังสัมผัส → ตรวจซ้ำ 12 สัปดาห์",
     "A1 ไวสูงสุด → A2 → A3 จำเพาะสูงขึ้นเรื่อย ๆ · บวกครบสามชุด = ติดเชื้อ",
     "Inconclusive → ตรวจซ้ำ 2 สัปดาห์ · สงสัย window → NAT/VL"],
    [mcq(N(11), "Why does the Thai HIV testing algorithm use the most sensitive assay (A1) first and progressively more specific assays (A2, A3) afterwards?",
         ["To reduce cost by skipping confirmation", "To avoid missing infections at screening and then exclude false positives before giving a diagnosis",
          "Because A3 detects HIV RNA", "Because antibody tests are more sensitive than antigen tests", "To shorten the window period to 3 days"], 1,
         "แนวทางไทย: **A1 = 4th generation ไวสูงสุด** ใช้คัดกรองเพื่อไม่ให้หลุดผู้ติดเชื้อ · **A2 และ A3 ใช้ antigen ต่างชุดกันและจำเพาะสูงขึ้นตามลำดับ** เพื่อตัดผลบวกลวงก่อนแจ้งผล\n\nต้องบวกครบทั้งสามชุดจึงสรุปว่าติดเชื้อ · การตรวจเหล่านี้เป็น serology ไม่ได้ตรวจ HIV RNA",
         "คัดกรองด้วยชุดไว → ยืนยันด้วยชุดจำเพาะ", "Thai HIV testing algorithm", R("HIV assay diagnosis A1–A3"), NLN + ["3.3.15", "B10.3(6)"]),
     mcq(N(12), "A woman's HIV result is 'inconclusive' (A1 positive, A2 negative). She had condomless sex 3 weeks ago. What is the next step according to the Thai guideline?",
         ["Report her as HIV-infected and start ART", "Report her as HIV-negative and discharge without follow-up",
          "Repeat testing in 2 weeks, and consider HIV RNA (NAT or viral load) because she may be in the window period", "Repeat testing in 6 months only", "Perform CD4 count to decide"], 2,
         "แนวทางไทย 2025: **ผลสรุปไม่ได้ → ตรวจซ้ำที่ 2 สัปดาห์** · ถ้ายังสรุปไม่ได้เหมือนเดิมจึงสรุปว่ายังไม่พบการติดเชื้อ\n\nผู้ป่วยรายนี้สัมผัสเสี่ยงเพียง 3 สัปดาห์ → **อาจอยู่ใน window period** (แอนติบอดียังขึ้นไม่ครบ) → ส่ง **qualitative NAT หรือ HIV viral load** เพิ่ม เพื่อไม่ให้เริ่มยาต้านช้า\n\nCD4 ไม่ใช่การตรวจวินิจฉัยการติดเชื้อ",
         "Inconclusive → ซ้ำ 2 สัปดาห์ ± NAT ถ้าสงสัย window", "Inconclusive HIV result", R("HIV testing interpretation"), NLN + ["3.3.15"]),
    ], NLN + ["3.3.15", "B10.3(6)"])

# ═══ ต่อส่วนที่ 2 ด้านล่าง ═══
