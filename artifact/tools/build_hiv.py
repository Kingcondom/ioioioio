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


# ───────────────────────────── 7
sec("id-hiv-07", "เริ่มยาต้านไวรัส — rapid ART, สูตรแรก และวิธีกินยาแต่ละตัว",
    "เริ่มเร็วที่สุด (same-day/rapid ART) · TDF/TAF + 3TC/FTC + DTG · RPV กินพร้อมอาหาร · EFV ก่อนนอนท้องว่าง", 10,
"""### เริ่มเมื่อไร
แนวทางไทย 2025 สนับสนุน **same-day ART หรือ rapid ART** — เริ่มยาต้านโดยเร็วที่สุดหลังวินิจฉัย **ไม่ต้องรอผล CD4** เพราะการเริ่มเร็วลดการตาย ลดการหลุดจากระบบ และลดการแพร่เชื้อ
**ข้อยกเว้นสำคัญ** — สงสัย **cryptococcal หรือ TB meningitis** ต้องรักษาเชื้อก่อนแล้วจึงเริ่ม ART (หัวข้อ 10 และ 13) เพราะ IRIS ในสมองอันตรายถึงชีวิต

### สูตรแรก
ตารางสูตรยาในสไลด์เป็นภาพ — โครงที่แนวทางไทยและ WHO ใช้เป็นหลักคือ
**NRTI 2 ตัว + INSTI 1 ตัว**: **TDF (หรือ TAF) + 3TC (หรือ FTC) + dolutegravir**
- INSTI ได้ผลแรง ดื้อยายาก ผลข้างเคียงน้อย
- สูตรทางเลือกที่ยังใช้: NNRTI เช่น **efavirenz** หรือ **rilpivirine**

### TAF กับ TDF
| | **TDF 300 มก.** | **TAF 25 มก.** |
|---|---|---|
| ขนาดยา | — | **ราว 1/10** ของ TDF |
| tenofovir ในพลาสมา | สูง | **ต่ำลง 90%** |
| ในเซลล์เป้าหมาย | ได้ผล | **TFV-DP ในเซลล์ยังพอ** — ได้ผลเท่ากัน |
| พิษต่อไตและกระดูก | มากกว่า | **น้อยกว่า** |
**กลไก** — TAF ถูกเปลี่ยนเป็นรูปออกฤทธิ์ **ภายในเซลล์** ยาจึงไม่ค้างในเลือดไปทำร้าย proximal tubule

### วิธีกินที่ต้องสอนผู้ป่วย (สไลด์)
| ยา | วิธีกิน | เหตุผล |
|---|---|---|
| **Rilpivirine (RPV)** | **กินพร้อมอาหาร (อย่างน้อย 400 kcal) ตรงเวลาทุกมื้อ** · ห้ามกินตอนท้องว่างหรือกับเครื่องดื่มอย่างเดียว | ต้องมีอาหารจึงดูดซึมได้ |
| **Efavirenz (EFV)** | **กินก่อนนอน ตอนท้องว่าง** · ไม่กินพร้อมอาหารไขมันสูง | ไขมันเพิ่มการดูดซึม → ผลข้างเคียงทางสมองมากขึ้น (มึนงง ฝันร้าย) · กินก่อนนอนให้หลับผ่านช่วงยาสูง |

### Hypersensitivity
สไลด์มีหัวข้อ hypersensitivity reaction (ภาพ) — ยาที่ต้องระวังคือ **abacavir** (สัมพันธ์กับ **HLA-B5701** ต้องตรวจก่อนให้ และ **ห้ามให้ซ้ำ** หลังแพ้ เพราะอาการรุนแรงถึงตาย) และ **nevirapine** (ผื่นและตับอักเสบรุนแรงในสัปดาห์แรก ๆ)
""",
    ["Same-day/rapid ART ไม่ต้องรอ CD4 · ยกเว้นสงสัย crypto/TB meningitis",
     "สูตรหลัก: TDF/TAF + 3TC/FTC + DTG",
     "TAF ขนาด 1/10 ของ TDF · tenofovir ในพลาสมาต่ำลง 90% · พิษไตน้อยกว่า",
     "RPV กินพร้อมอาหาร ≥ 400 kcal · EFV ก่อนนอนท้องว่าง",
     "Abacavir → ตรวจ HLA-B5701 · แพ้แล้วห้ามให้ซ้ำ"],
    [mcq(N(13), "A patient starting rilpivirine-based ART asks how to take the tablet. Which advice is correct?",
         ["Take it at bedtime on an empty stomach", "Take it with a meal of at least about 400 kcal, at the same time each day",
          "Take it with a protein shake only", "Take it with antacids to reduce nausea", "Timing and food do not matter"], 1,
         "สไลด์: **RPV กินพร้อมอาหาร (อย่างน้อย 400 kcal) และตรงเวลาทุกมื้อ ห้ามกินตอนท้องว่างหรือดื่มเพียงเครื่องดื่ม** เพราะจะลดการดูดซึมยา → ระดับยาต่ำ → ดื้อยา\n\nการกินก่อนนอนตอนท้องว่างเป็นคำแนะนำของ **efavirenz** (ตรงข้ามกัน) · RPV ยังถูกรบกวนด้วยยาลดกรด (PPI ห้ามใช้ร่วม)",
         "RPV = พร้อมอาหาร · EFV = ก่อนนอนท้องว่าง", "Rilpivirine administration", R("คำแนะนำเกี่ยวกับยาในการเริ่มยาต้าน")),
     mcq(N(14), "Why does tenofovir alafenamide (TAF) 25 mg cause less renal toxicity than tenofovir disoproxil fumarate (TDF) 300 mg while remaining equally effective?",
         ["TAF is not converted to active drug", "TAF produces about 90% lower plasma tenofovir while maintaining effective intracellular tenofovir-diphosphate in target cells",
          "TAF is excreted by the liver only", "TAF is a protease inhibitor", "TAF is given only once a week"], 1,
         "สไลด์ TAF vs TDF: **TAF 25 มก. (ราว 1/10 ของ TDF 300 มก.) ทำให้ tenofovir ในพลาสมาต่ำลง 90% แต่ยังคงระดับ TFV-DP ในเซลล์เป้าหมายได้ผล**\n\nพิษต่อ **proximal tubule** และกระดูกเกิดจาก tenofovir ที่ค้างในพลาสมา เมื่อพลาสมาต่ำลง พิษจึงน้อยลง",
         "TAF: พลาสมาต่ำ 90% · ในเซลล์ยังพอ → พิษไตน้อย", "TAF vs TDF", R("TAF vs TDF")),
    ])

# ───────────────────────────── 8
sec("id-hiv-08", "ติดตามการรักษา พิษของ TDF และยาตีกัน",
    "ติดตาม VL และ CD4 · TDF ทำ proximal tubulopathy ใช้เกณฑ์ 2 ใน 4 · rifampicin ตีกับ DTG และ PI", 8,
"""### ติดตามผลการรักษา
ตารางการตรวจทางห้องปฏิบัติการในสไลด์เป็นภาพ หลักที่ใช้คือ
- **HIV viral load** — ตัวชี้วัดหลักว่ายาได้ผล เป้า **ตรวจไม่พบ** · VL ไม่ลงตามคาด → ตรวจการกินยาก่อน แล้วจึงคิดถึงดื้อยา
- **CD4** — บอกระดับภูมิคุ้มกัน ใช้ตัดสินใจเรื่องยาป้องกันโรคฉวยโอกาส
- **คัดกรองโรคร่วม** — **HBV และ HCV** (สไลด์มีหัวข้อ HBV/HIV และ HCV/HIV) · ไขมัน น้ำตาล การทำงานของไต

**HBV ร่วมกับ HIV** — TDF/TAF และ 3TC/FTC **ออกฤทธิ์ต่อ HBV ด้วย** สูตรยาต้องมี tenofovir เสมอ และ **ห้ามหยุดยาเหล่านี้เอง** เพราะตับอักเสบจาก HBV จะกำเริบรุนแรง

### พิษของ TDF — proximal tubular dysfunction (สไลด์)
| เกณฑ์ | |
|---|---|
| 1 | **Proteinuria** — dipstick > 1+ มากกว่า 1 ครั้ง หรือ **UP/C > 15 มก./มิลลิโมล** |
| 2 | **Glycosuria** (น้ำตาลในเลือดปกติ) |
| 3 | **eGFR < 90** โดยไม่มีสาเหตุอื่น |
| 4 | **Phosphaturia** |
**เข้า 2 ใน 4 ข้อ → ติดตามใกล้ชิด และพิจารณาเปลี่ยนเป็นสูตรที่ไม่มี TDF** (เช่น TAF)

**กลไก** — tenofovir เข้าเซลล์ proximal tubule ผ่าน OAT ทำลาย mitochondria → ท่อไตส่วนต้นดูดกลับสารไม่ได้ (คล้าย Fanconi syndrome) → เสียน้ำตาล ฟอสเฟต โปรตีนโมเลกุลเล็กทางปัสสาวะ

### ยาตีกันที่ต้องรู้
ตารางยาตีกันในสไลด์เป็นภาพ — คู่ที่พบบ่อยที่สุดในไทยคือ **rifampicin** (เหนี่ยวนำเอนไซม์ตับและ UGT1A1)
| ยาต้าน | กับ rifampicin |
|---|---|
| **Dolutegravir** | ระดับยาลด → **เพิ่มเป็น 50 มก. วันละ 2 ครั้ง** ระหว่างได้ rifampicin |
| **Efavirenz 600 มก.** | ใช้ร่วมได้ ไม่ต้องปรับ |
| **Protease inhibitors (boosted)** | **ห้ามใช้ร่วม** — ระดับยาลดมาก |
| **TAF** | ไม่แนะนำร่วมกับ rifampicin |
""",
    ["ติดตาม VL (เป้าตรวจไม่พบ) และ CD4 · คัดกรอง HBV/HCV",
     "HBV ร่วม → สูตรต้องมี tenofovir · ห้ามหยุดเอง",
     "TDF tubulopathy: proteinuria · glycosuria · eGFR < 90 · phosphaturia → 2/4 พิจารณาเปลี่ยนยา",
     "Rifampicin: DTG 50 มก. วันละ 2 ครั้ง · EFV ใช้ได้ · boosted PI ห้าม"],
    [mcq(N(15), "A man on TDF/3TC/DTG has a normal blood glucose but urine dipstick shows 2+ glucose and 2+ protein on two occasions, with eGFR 96 and normal serum phosphate. According to the Thai criteria, what should be done?",
         ["Nothing, because eGFR is above 90", "Stop all ART immediately",
          "He meets 2 of 4 criteria for TDF proximal tubular dysfunction: monitor closely and consider switching to a regimen without TDF", "Start insulin", "Add a second NRTI"], 2,
         "เกณฑ์ **TDF proximal tubular dysfunction** (สไลด์): **(1) proteinuria (2) glycosuria (3) eGFR < 90 ไม่มีสาเหตุอื่น (4) phosphaturia** — **เข้า 2 ใน 4 → ติดตามใกล้ชิดและพิจารณาเปลี่ยนเป็นสูตรที่ไม่มี TDF**\n\nผู้ป่วยมี **glycosuria ทั้งที่น้ำตาลในเลือดปกติ + proteinuria** = 2 ข้อแล้ว eGFR ยังปกติก็ไม่ได้ตัดภาวะนี้ · ไม่ใช่เบาหวาน จึงไม่ต้องให้ insulin",
         "Glycosuria ที่น้ำตาลปกติในผู้ใช้ TDF = tubulopathy", "TDF nephrotoxicity", R("Adverse reaction from TDF")),
     mcq(N(16), "A patient on TDF/3TC/dolutegravir 50 mg once daily is diagnosed with pulmonary TB and starts a rifampicin-containing regimen. What adjustment is required?",
         ["No change", "Increase dolutegravir to 50 mg twice daily during and for 2 weeks after rifampicin",
          "Switch dolutegravir to lopinavir/ritonavir", "Stop ART until TB treatment is complete", "Halve the dose of dolutegravir"], 1,
         "**Rifampicin เหนี่ยวนำ UGT1A1 และ CYP3A** ทำให้ระดับ dolutegravir ลดลงมาก → ต้อง **เพิ่มเป็น 50 มก. วันละ 2 ครั้ง** ระหว่างได้ rifampicin และต่ออีกราว 2 สัปดาห์หลังหยุด (เอนไซม์ยังถูกเหนี่ยวนำอยู่)\n\n**Boosted PI ห้ามใช้ร่วมกับ rifampicin** · **ห้ามหยุด ART** — ผู้ป่วยวัณโรคที่ติด HIV ต้องได้ทั้งสองอย่าง",
         "Rifampicin + DTG → DTG 50 มก. วันละ 2 ครั้ง", "Rifampicin–dolutegravir interaction", ["ตารางยาตีกันในสไลด์เป็นภาพ — " + TG], NLN + ["2.3.1(20)"]),
    ])

# ───────────────────────────── 9
sec("id-hiv-09", "หญิงตั้งครรภ์และการป้องกันการติดเชื้อจากแม่สู่ลูก",
    "เริ่ม ART เร็วที่สุด · VL < 50 ใกล้คลอดลดการติดจาก 20–30% เหลือ 0.1–0.5% · ยาทารก 2–6 สัปดาห์ · นมผสม", 7,
"""### หลักการ (สไลด์)
- **เริ่ม ART โดยเร็วที่สุด** เป้าหมายคือ **กดไวรัสให้ได้ตลอดการตั้งครรภ์**
- **VL ของแม่ < 50 copies/mL ใกล้คลอด** → อัตราการติดเชื้อสู่ทารกลดจาก **20–30% เหลือ 0.1–0.5%**
- ตรวจ **HIV VL** ระหว่างตั้งครรภ์ตามแนวทาง (โดยเฉพาะช่วงใกล้คลอด) เพื่อวางแผนการคลอดและยาทารก
- หญิงที่ **ไม่เคยฝากครรภ์และไม่เคยได้ยา** มาคลอด → ถือเป็นกลุ่มเสี่ยงสูง ต้องเริ่มยาทันทีและให้ยาทารกแบบเข้มข้น

### ป้องกันทารก (NIH HIVinfo ในสไลด์)
| ช่วง | สิ่งที่ทำ |
|---|---|
| **ก่อน ระหว่าง และหลังตั้งครรภ์** | แม่กินยาต้านต่อเนื่อง |
| **คลอด** | VL **สูงหรือไม่ทราบ** → **ผ่าตัดคลอดตามนัด (scheduled C-section)** |
| **หลังคลอด** | **ทารกได้ยาต้าน 2–6 สัปดาห์แรก** |
| **การให้นม** | **นมผสมไม่มีความเสี่ยง** · แม่ที่ VL ตรวจไม่พบ ให้นมแม่ความเสี่ยง **< 1% แต่ไม่ใช่ 0** → ปรึกษาเลือกวิธีร่วมกัน |

**ทำไม VL ใกล้คลอดสำคัญที่สุด** — การติดเชื้อส่วนใหญ่เกิด **ระหว่างคลอด** ที่ทารกสัมผัสเลือดและสารคัดหลั่งของแม่ ปริมาณไวรัสในขณะนั้นจึงกำหนดความเสี่ยง
""",
    ["หญิงตั้งครรภ์ติดเชื้อ → เริ่ม ART เร็วที่สุด",
     "VL < 50 ใกล้คลอด → ติดสู่ลูกจาก 20–30% เหลือ 0.1–0.5%",
     "VL สูง/ไม่ทราบ → scheduled C-section · ทารกได้ยา 2–6 สัปดาห์",
     "นมผสมไม่มีความเสี่ยง · นมแม่ขณะ VL ตรวจไม่พบ < 1% แต่ไม่ใช่ 0"],
    [mcq(N(17), "A pregnant woman with HIV started ART at 14 weeks. Her viral load at 36 weeks is below 50 copies/mL. Approximately what is the risk of perinatal transmission with continued suppression?",
         ["20–30%", "10–15%", "5%", "0.1–0.5%", "Exactly zero"], 3,
         "สไลด์: **VL ของแม่ < 50 copies/mL ใกล้คลอด ลดอัตราการติดเชื้อจากแม่สู่ลูกจาก 20–30% เหลือ 0.1–0.5%**\n\nความเสี่ยงไม่เป็นศูนย์ ทารกจึงยังต้องได้ **ยาต้าน 2–6 สัปดาห์** และต้องวางแผนการให้นม (นมผสมไม่มีความเสี่ยง)",
         "แม่ VL < 50 ใกล้คลอด → ติดสู่ลูก 0.1–0.5%", "Perinatal transmission", R("Pregnant women with HIV"), NLN + ["2.3.16-3(1)"]),
    ], NLN + ["2.3.16-3(1)", "B10.2.2-3(1)"])

# ───────────────────────────── 10
sec("id-hiv-10", "วัณโรคในผู้ติดเชื้อ HIV",
    "CD4 สูงเป็นแบบ classic · CD4 ต่ำเป็นปอดกลีบล่าง ไม่มีโพรง และนอกปอด · steroid ใน CNS TB · ปรับยาต้าน", 10,
"""### ภาพทางคลินิกขึ้นกับ CD4 (สไลด์)
| CD4 | ภาพที่พบ |
|---|---|
| **> 350** | **classic** — **ปอดกลีบบนมีโพรง** ไข้ อาการทั่วตัว |
| **< 200** | **ปอดกลีบล่าง ไม่มีโพรง** (CXR อาจดูเกือบปกติ) และ **วัณโรคนอกปอดมากขึ้น** — **ต่อมน้ำเหลือง ทางเดินปัสสาวะ ไขกระดูก ระบบประสาท** |
**กลไก** — โพรงเกิดจากปฏิกิริยาภูมิคุ้มกันที่ทำลายเนื้อปอด เมื่อ CD4 ต่ำ ร่างกายสร้าง granuloma และโพรงไม่ได้ เชื้อจึงกระจายออกนอกปอดแทน (สอดคล้องกับคาบ Extrapulmonary TB: disseminated TB 87.5% ในผู้ป่วย HIV)

### การตรวจ (สไลด์)
- **AFB smear บวกไม่ยืนยันวัณโรค** — อาจเป็น **NTM** (เช่น MAC ซึ่งพบมากในผู้ป่วย HIV)
- **AFB smear ลบไม่ตัดวัณโรค** — เชื้ออาจมีแต่มองไม่เห็น
- **Culture** — อาหารแข็ง **Lowenstein-Jensen, Middlebrook 7H10/7H11** · อาหารเหลว **Middlebrook 7H9** (เร็วกว่า)
- ส่ง **Xpert MTB/RIF** ร่วมเสมอ

### การรักษา
- สูตรมาตรฐาน **2HRZE/4HR** เหมือนผู้ไม่ติดเชื้อ
- **สูตร 4 เดือน 2HPZM/2HPM** (rifapentine 1,200 มก. + moxifloxacin 400 มก.) — สไลด์ระบุว่า **ใช้ร่วมได้เฉพาะสูตร ART ที่มี efavirenz เท่านั้น**
- **CNS TB → steroid** (สไลด์): **prednisolone 40–60 มก./วัน × 2–4 สัปดาห์ → 30 มก. × 2 สัปดาห์ → 15 มก. × 2 สัปดาห์ → 5 มก. × 1–2 สัปดาห์**

### จังหวะเริ่ม ART ในผู้ป่วยวัณโรค (ตารางในสไลด์เป็นภาพ — ตามแนวทางไทย/WHO)
- **เริ่ม ART ภายใน 2 สัปดาห์หลังเริ่มยาวัณโรค** เมื่อผู้ป่วยทนยาได้
- **ยกเว้น TB meningitis** → รอ **4–8 สัปดาห์** เพราะ IRIS ในสมองอันตราย
- **ปรับยาต้านให้เข้ากับ rifampicin** (หัวข้อ 8)

### IRIS (immune reconstitution inflammatory syndrome)
หลังเริ่ม ART ภูมิคุ้มกันฟื้นตัวและเริ่มต่อสู้กับเชื้อที่มีอยู่ → อาการ **แย่ลงชั่วคราว** (paradoxical) หรือ **เผยโรคที่ซ่อนอยู่** (unmasking) — ไม่ได้แปลว่ายาล้มเหลว
""",
    ["CD4 > 350 → upper lobe cavity · CD4 < 200 → lower lobe ไม่มีโพรง + EPTB (LN, GU, BM, CNS)",
     "AFB บวกอาจเป็น NTM · AFB ลบไม่ตัดวัณโรค",
     "2HPZM/2HPM ใช้ได้เฉพาะกับสูตร EFV",
     "CNS TB: prednisolone 40–60 มก. แล้วค่อย ๆ ลด",
     "ART ภายใน 2 สัปดาห์หลังยาวัณโรค · TB meningitis รอ 4–8 สัปดาห์"],
    [mcq(N(18), "A man with HIV and CD4 count 60 cells/µL has 6 weeks of fever and weight loss. Chest radiograph shows right lower-lobe infiltrate without cavitation and mediastinal lymphadenopathy. Which statement is most accurate?",
         ["TB is unlikely because there is no upper-lobe cavity", "This atypical pattern is typical of TB at low CD4 counts, and extrapulmonary disease should be sought",
          "A positive AFB smear would confirm M. tuberculosis", "TST is the best test to diagnose active TB here", "Cavitation is more common at CD4 < 200"], 1,
         "สไลด์: **CD4 < 200 → ปอดกลีบล่าง ไม่มีโพรง และเป็นวัณโรคนอกปอดมากขึ้น** (ต่อมน้ำเหลือง ทางเดินปัสสาวะ ไขกระดูก ระบบประสาท) ภาพ classic ที่กลีบบนมีโพรงพบเมื่อ CD4 > 350\n\nข้อผิด: **AFB smear บวกไม่ยืนยัน MTB** เพราะอาจเป็น NTM (ต้อง Xpert/culture) · TST ไม่ใช้วินิจฉัย active TB และมักลบใน CD4 ต่ำ",
         "CD4 ต่ำ: วัณโรคไม่มีโพรง กลีบล่าง และนอกปอด", "TB presentation by CD4", R("Mycobacterium tuberculosis in PLWH"), NLN + ["2.3.1(20)", "B6.2.2(8)"]),
     mcq(N(19), "A patient with HIV on a dolutegravir-based ART regimen is being considered for the 4-month rifapentine–moxifloxacin TB regimen (2HPZM/2HPM). According to the lecture, what limits its use?",
         ["It cannot be used in any person with HIV", "It can be combined only with efavirenz-based ART",
          "It requires stopping ART for 4 months", "It is only for TB meningitis", "It can be used only if CD4 > 500"], 1,
         "สไลด์: **2HPZM/2HPM (rifapentine 1,200 มก. + moxifloxacin 400 มก.) สามารถใช้ร่วมกับ EFV-based เท่านั้น**\n\nเหตุผล: rifapentine เหนี่ยวนำเอนไซม์ตับรุนแรง ข้อมูลระดับยาที่ปลอดภัยมีเฉพาะกับ efavirenz · ผู้ป่วยที่ใช้ DTG จึงควรใช้ **สูตรมาตรฐาน 2HRZE/4HR** ร่วมกับ **DTG 50 มก. วันละ 2 ครั้ง**",
         "2HPZM/2HPM + ART ได้เฉพาะ EFV", "Rifapentine-moxifloxacin regimen", R("Treatment of tuberculosis"), NLN + ["2.3.1(20)"]),
     mcq(N(20), "A patient with HIV and newly diagnosed TB meningitis is not yet on ART. When should ART generally be started?",
         ["The same day as TB treatment", "Within 2 weeks of TB treatment", "After about 4–8 weeks of TB treatment",
          "After completing 12 months of TB treatment", "Never during TB treatment"], 2,
         "ในวัณโรคตำแหน่งอื่นเริ่ม ART **ภายใน 2 สัปดาห์** หลังยาวัณโรค แต่ใน **TB meningitis ให้รอราว 4–8 สัปดาห์** เพราะ **IRIS ในสมอง** (สมองบวม ความดันในกะโหลกสูง) อันตรายถึงชีวิต\n\nร่วมกับ **steroid** ตามสไลด์: prednisolone 40–60 มก./วัน แล้วค่อย ๆ ลดใน 7–10 สัปดาห์",
         "TB meningitis + HIV → ART หลัง 4–8 สัปดาห์", "ART timing in TB meningitis", R("Treatment of tuberculosis"), NLN + ["2.3.1(20)", "2.3.6(5)"]),
    ], NLN + ["2.3.1(20)", "B6.2.2(8)"])

# ───────────────────────────── 11
sec("id-hiv-11", "MAC และ Pneumocystis pneumonia (PCP)",
    "MAC เมื่อ CD4 < 50: ไข้ ท้องเสีย ตับม้ามโต ALP สูง · PCP เมื่อ CD4 < 200: เหนื่อยกึ่งเฉียบพลัน ออกแรงแล้ว SpO₂ ตก · steroid ตาม PaO₂", 11,
"""### Mycobacterium avium complex (MAC)
- **NTM** · disseminated MAC (ส่วนใหญ่ M. avium) เมื่อ **CD4 < 50**
- **อาการ** — **ไข้ เหงื่อออกกลางคืน น้ำหนักลด ท้องเสียเรื้อรัง ตับม้ามโต ต่อมน้ำเหลืองโตทั่วตัว**
- CD4 สูงกว่าหรือช่วงภูมิฟื้นตัว → เป็นเฉพาะที่ (ต่อมน้ำเหลือง ปอด กระดูก ฝี สมอง) · เกิด IRIS ได้
- **Lab** — **cytopenia** และ **alkaline phosphatase สูง**
- **วินิจฉัย** — อาการเข้ากัน + **เพาะเชื้อขึ้นจากเลือด ไขกระดูก หรือเนื้อเยื่อปลอดเชื้อ** · แยกสปีชีส์ด้วย PCR/WGS
- **Primary prophylaxis** — **ไม่แนะนำถ้าเริ่ม ART ทันที** · ให้เมื่อ **CD4 < 50 และ ไม่ได้ ART / ยัง viremic / ไม่มีสูตรที่กดไวรัสได้** (มักใช้ azithromycin สัปดาห์ละครั้ง)

### Pneumocystis pneumonia (PCP)
| | |
|---|---|
| เชื้อ | **Pneumocystis jirovecii** (ชื่อเดิม P. carinii) — ติดทางการหายใจ · **โรคที่บ่งชี้ AIDS** |
| ปัจจัยเสี่ยง | **CD4 < 200** ที่ไม่ได้ ART |
| อาการ | **เหนื่อยกึ่งเฉียบพลัน (เป็นสัปดาห์)** ไข้ **ไอแห้ง** เจ็บหน้าอก |
| ตรวจร่างกาย | **SpO₂ ตกเมื่อออกแรง (exertional desaturation)** · crackles |
| CXR | ปกติ ถึง **bilateral perihilar/butterfly ground-glass** · nodule bleb cyst ได้ · **น้ำในเยื่อหุ้มปอดหรือโพรงพบน้อย** |
| เบาะแสสำคัญ | **ปอดแฟบเอง (spontaneous pneumothorax) ในผู้ติดเชื้อ → สงสัย PCP** (จาก cyst/bleb แตก) |
| Lab | **LDH > 500** พบบ่อยแต่ไม่จำเพาะ · **1,3-β-D-glucan สูง** — ไม่จำเพาะ แต่ **ผลลบ NPV สูง** ช่วยตัดโรค |
| ยืนยัน | เห็นเชื้อใน **เสมหะ BAL หรือชิ้นเนื้อ** ด้วย **silver stain (GMS), Giemsa หรือ DFA** · cyst 5–8 µm · trophic 1–4 µm · **เพาะเชื้อไม่ได้** |

### การรักษา
- **TMP-SMX** เป็นยาหลัก นาน **21 วัน** (ตามแนวทาง)
- **เพิ่ม corticosteroid ถ้า PaO₂ < 70 mmHg (room air) หรือ A–a gradient ≥ 35 mmHg** — เริ่มเร็วที่สุด **ภายใน 72 ชม.** ของการรักษา PCP (สไลด์)
| วัน | Prednisone |
|---|---|
| 1–5 | **40 มก. วันละ 2 ครั้ง** |
| 6–10 | **40 มก. วันละครั้ง** |
| 11–21 | **20 มก. วันละครั้ง** |
**ทำไม steroid ช่วย** — เชื้อที่ตายหลังได้ยาปล่อยแอนติเจนกระตุ้นการอักเสบในถุงลม ทำให้ออกซิเจนแย่ลงใน 3–5 วันแรก steroid กดการอักเสบช่วงนี้ ลดการต้องใส่ท่อช่วยหายใจและการตาย
""",
    ["MAC: CD4 < 50 · ไข้ ท้องเสีย ตับม้ามโต · cytopenia + ALP สูง · dx เพาะเชื้อจากเลือด/ไขกระดูก",
     "MAC prophylaxis ไม่ต้องให้ถ้าเริ่ม ART ทันที",
     "PCP: CD4 < 200 · เหนื่อยกึ่งเฉียบพลัน ไอแห้ง exertional desaturation · CXR butterfly GGO",
     "Pneumothorax เองใน PLWH → PCP · β-D-glucan ลบช่วยตัดโรค",
     "Steroid เมื่อ PaO₂ < 70 หรือ A–a ≥ 35 · 40×2 → 40 → 20 รวม 21 วัน"],
    [mcq(N(21), "A man with HIV (CD4 35 cells/µL) not on ART has 2 months of fever, night sweats, weight loss, chronic diarrhoea and hepatosplenomegaly. Labs show pancytopenia and markedly raised alkaline phosphatase. Which test is most likely to confirm the diagnosis?",
         ["Sputum Gram stain", "Mycobacterial blood culture (or bone marrow culture)", "Serum cryptococcal antigen", "Stool ova and parasites only", "Chest CT"], 1,
         "ภาพของ **disseminated MAC** ตามสไลด์ — **CD4 < 50 · ไข้ เหงื่อออกกลางคืน น้ำหนักลด ท้องเสียเรื้อรัง ตับม้ามโต** และ lab **cytopenia + ALP สูง**\n\n**การวินิจฉัยที่แน่นอน: อาการเข้ากัน + เพาะเชื้อขึ้นจากเลือด ไขกระดูก หรือเนื้อเยื่อปลอดเชื้อ** · AFB smear บวกจะแยกจากวัณโรคไม่ได้ ต้องแยกสปีชีส์ด้วย PCR",
         "CD4 < 50 + ไข้ ท้องเสีย ตับม้ามโต ALP สูง = MAC → blood culture", "Disseminated MAC", R("Mycobacterium avium complex"), NLN + ["2.3.1-3(6)"]),
     mcq(N(22), "A woman with HIV (CD4 90 cells/µL) has 3 weeks of progressive dyspnoea and dry cough. SpO2 falls from 95% to 86% on walking. Chest radiograph shows bilateral perihilar ground-glass opacities. ABG on room air: PaO2 62 mmHg. Besides trimethoprim-sulfamethoxazole, what should be given?",
         ["Nothing else", "Prednisone 40 mg twice daily for 5 days, then tapering to complete 21 days", "Fluconazole", "Amphotericin B", "Ceftriaxone and azithromycin only"], 1,
         "ภาพของ **PCP** — CD4 < 200 · เหนื่อยกึ่งเฉียบพลัน ไอแห้ง **exertional desaturation** · CXR **bilateral perihilar GGO**\n\n**PaO₂ 62 < 70 mmHg** → เข้าเกณฑ์ **corticosteroid** (สไลด์: PaO₂ < 70 หรือ A–a ≥ 35 เริ่มภายใน 72 ชม.) — **prednisone 40 มก. วันละ 2 ครั้ง วันที่ 1–5 → 40 มก. วันละครั้ง วันที่ 6–10 → 20 มก. วันละครั้ง วันที่ 11–21**",
         "PCP + PaO₂ < 70 หรือ A–a ≥ 35 → prednisone", "PCP adjunctive steroid", R("Pneumocystis pneumonia"), NLN + ["2.3.1(18)"]),
     mcq(N(23), "A man with untreated HIV develops a sudden right pneumothorax. Which opportunistic infection should be strongly suspected?",
         ["Cryptococcal pneumonia", "Pneumocystis pneumonia", "Histoplasmosis", "Kaposi sarcoma", "MAC lymphadenitis"], 1,
         "สไลด์ PCP: **spontaneous pneumothorax ในผู้ติดเชื้อ HIV ควรสงสัย PCP อย่างมาก** — PCP ทำให้เกิด **cyst และ bleb** ในเนื้อปอด ซึ่งแตกจนลมรั่วเข้าช่องเยื่อหุ้มปอด\n\nตรวจต่อ: LDH, β-D-glucan (ผลลบช่วยตัดโรค) และหาเชื้อในเสมหะหรือ BAL ด้วย silver stain/Giemsa/DFA",
         "Pneumothorax เองในผู้ติด HIV → PCP", "PCP and pneumothorax", R("Pneumocystis pneumonia — diagnosis"), NLN + ["2.3.1(18)"]),
    ], NLN + ["2.3.1(18)", "2.3.1-3(6)"])

# ───────────────────────────── 12
sec("id-hiv-12", "เชื้อราประจำถิ่น: Talaromycosis และ Histoplasmosis",
    "Talaromyces: CD4 < 100 ภาคเหนือ ตุ่มบุ๋มกลาง เชื้อแบ่งตัวแบบมีผนังกลาง · Histoplasma: CD4 < 150 มูลค้างคาว budding yeast", 10,
"""### Talaromycosis (Penicilliosis)
| | |
|---|---|
| เชื้อ | **Talaromyces marneffei** (ชื่อเดิม Penicillium marneffei) — **dimorphic fungus** |
| ใคร | **CD4 < 100** · โรคบ่งชี้ AIDS ที่พบบ่อยใน **เอเชียตะวันออกเฉียงใต้ — ภาคเหนือของไทย** เวียดนาม จีน |
| แหล่ง | **หนูอ้น (bamboo rat)** · ติดทางการหายใจ conidia |
| อาการ | **ไข้เรื้อรัง ต่อมน้ำเหลืองโต ตับโต ปอด** และ **ตุ่มผิวหนังมีรอยบุ๋มตรงกลาง (umbilicated skin nodules)** |
| ตุ่มบุ๋มกลาง แยกจาก | **molluscum contagiosum · cutaneous cryptococcosis · histoplasmosis** |
| CXR | จุดกระจายทั่วปอดคล้าย **miliary TB** |
| เพาะเชื้อ | ขึ้นใน **2–7 วัน** จากเสมหะ เลือด ผิวหนัง ต่อมน้ำเหลือง ไขกระดูก · ที่ **25°C เป็นรา + สีแดงซึมลงอาหารเลี้ยงเชื้อ (red pigment)** · ที่ 37°C เป็น yeast ไม่มีสี |
| กล้อง | yeast รูปไข่ **แบ่งตัวแบบ fission มีผนังกั้นกลาง (central septum)** ไม่ใช่ budding · ขนาดไม่เท่ากัน |
| ข้อควรระวัง | **galactomannan บวกข้ามได้** |

### Histoplasmosis
| | |
|---|---|
| เชื้อ | **Histoplasma capsulatum** — **endemic mycosis ที่พบบ่อยที่สุด** พบทั่วโลก |
| แหล่ง | **มูลนกหรือค้างคาว · เข้าถ้ำ** · หายใจเอาสปอร์ |
| ใคร | **CD4 < 150** |
| ผลการติดเชื้อ | **50–90% ไม่มีอาการ** |

| รูปแบบ | ลักษณะ |
|---|---|
| **Acute pulmonary** | คล้ายไข้หวัดใหญ่ หลังฟักตัว ~14 วัน · patchy pneumonitis ± ต่อมน้ำเหลืองขั้วปอดโต · ปวดข้อ erythema nodosum 5–10% |
| **Chronic pulmonary** | > 6 สัปดาห์ · **ชายสูงอายุที่เป็น COPD** · **ปอดกลีบบนเป็นโพรง คล้ายวัณโรคหรือมะเร็งปอด** |
| **Disseminated** | ไข้ น้ำหนักลด **ต่อมน้ำเหลือง ตับโต ไขกระดูก** · **adrenal insufficiency** · แผลในปาก ลำไส้อักเสบ · ผื่น · **pancytopenia, AST > ALT, ALP สูง** · miliary · สัมพันธ์กับ **HLH** |
| **Fibrosing mediastinitis** | ผลระยะยาว · พังผืดและหินปูนกดทางเดินหายใจหรือหลอดเลือด · **ยาฆ่าเชื้อราและ steroid ไม่ช่วย** · ใส่ stent |

**วินิจฉัย** — **culture เป็นมาตรฐาน** · กล้องเห็น yeast **2–4 µm ภายใน neutrophil/macrophage** · **Histoplasma antigen (EIA) ใน serum ปัสสาวะ BAL หรือ CSF** · แอนติบอดี

### แยกสองเชื้อด้วยกล้อง (สไลด์)
| | **Talaromyces marneffei** | **Histoplasma capsulatum** |
|---|---|---|
| Yeast | ขนาดไม่เท่ากัน **มีผนังกลาง แบ่งแบบ fission ไม่ budding** | ขนาดเท่ากัน รูปไข่ **budding** |
| Mold (25–30°C) | **สีแดงซึมลงอาหาร** | macroconidia ผิวขรุขระ (tuberculate) |

### การรักษาและป้องกัน
- รักษา (ตามแนวทาง): **amphotericin B** ระยะเหนี่ยวนำ แล้วต่อด้วย **itraconazole**
- **Primary prophylaxis (สไลด์)** — ผู้ใหญ่ **CD4 < 100 (talaromycosis) หรือ < 150 (histoplasmosis)** ที่อยู่ **พื้นที่ชุก** **และเริ่ม ART ไม่ได้ภายใน 4 สัปดาห์** · เด็กโดยทั่วไปไม่ให้
- **หยุด secondary prophylaxis** — talaromycosis **CD4 > 100** · histoplasmosis **CD4 > 150 นาน > 6 เดือน** · **VL ตรวจไม่พบ > 6 เดือน**
""",
    ["Talaromyces: CD4 < 100 · ภาคเหนือ · หนูอ้น · umbilicated skin nodules",
     "Talaromyces: red pigment ที่ 25°C · yeast แบ่งแบบ fission มี central septum",
     "Histoplasma: CD4 < 150 · มูลนก/ค้างคาว ถ้ำ · budding yeast ใน macrophage · antigen ในปัสสาวะ",
     "Disseminated histo: pancytopenia · AST > ALT · ALP สูง · adrenal insufficiency · HLH",
     "Prophylaxis: CD4 < 100/150 ในพื้นที่ชุก และเริ่ม ART ไม่ได้ใน 4 สัปดาห์"],
    [mcq(N(24), "A 30-year-old man from Chiang Mai with untreated HIV (CD4 22 cells/µL) has fever, hepatomegaly and multiple papules with central umbilication on the face. Skin scraping with Giemsa stain shows oval intracellular yeasts with a central transverse septum. Culture at 25°C grows a mould producing a red diffusible pigment. What is the diagnosis?",
         ["Histoplasmosis", "Cryptococcosis", "Talaromycosis", "Molluscum contagiosum", "Disseminated candidiasis"], 2,
         "ครบทุกเบาะแสของ **talaromycosis** ในสไลด์ — **CD4 < 100 · ภาคเหนือ · ไข้ ตับโต · ตุ่มบุ๋มกลาง** · yeast **แบ่งตัวแบบ fission มีผนังกลาง (central septum)** · ที่ 25°C เป็นรา **สีแดงซึมลงอาหารเลี้ยงเชื้อ**\n\nHistoplasma เป็น **budding yeast** ขนาดเท่ากัน ไม่มีผนังกลาง · ตุ่มบุ๋มกลางเป็น DDx ร่วมของ molluscum, cryptococcosis และ histoplasmosis จึงต้องอาศัยกล้องและการเพาะเชื้อ",
         "Central septum + red pigment = Talaromyces", "Talaromycosis", R("Talaromycosis"), NLN + ["2.3.1-3(7)", "B1.5.4(2)"]),
     mcq(N(25), "A man with HIV (CD4 80 cells/µL) who explores caves has fever, pancytopenia, AST higher than ALT, raised alkaline phosphatase, hepatosplenomegaly and diffuse miliary infiltrates. Which test offers rapid, sensitive support for the most likely diagnosis?",
         ["Urine Histoplasma antigen", "Serum cryptococcal antigen", "Sputum Gram stain", "Tuberculin skin test", "Galactomannan only"], 0,
         "ภาพของ **disseminated histoplasmosis** ตามสไลด์ — **CD4 < 150 · สัมผัสมูลค้างคาวในถ้ำ** · ไข้ ตับม้ามโต **pancytopenia, AST > ALT, ALP สูง** และ **miliary infiltrates** (ต้องระวัง adrenal insufficiency และ HLH)\n\n**Histoplasma antigen (EIA) ใน serum หรือปัสสาวะ** ให้ผลเร็วและไว · **culture เป็นมาตรฐาน** แต่ช้า · กล้องเห็น budding yeast 2–4 µm ใน neutrophil/macrophage",
         "Histo disseminated → urine/serum antigen + culture", "Disseminated histoplasmosis", R("Histoplasmosis — diagnosis"), NLN + ["2.3.1-3(7)"]),
    ], NLN + ["2.3.1-3(7)", "B1.5.4(2)"])

# ───────────────────────────── 13
sec("id-hiv-13", "Cryptococcosis และสรุปยาป้องกันโรคฉวยโอกาสตาม CD4",
    "Crypto meningitis: คอแข็งพบเพียงหนึ่งในสี่ ความดันในกะโหลกสูงคือตัวฆ่า · ตารางป้องกันตาม CD4", 10,
"""### Cryptococcus (สไลด์)
| | **C. neoformans** | **C. gattii** |
|---|---|---|
| แหล่ง | **มูลนกพิราบ ต้นไม้ผุ** | **ต้นยูคาลิปตัส** |
| พื้นที่ | ทั่วโลก | เขตร้อนและกึ่งร้อน |
**กลุ่มเสี่ยง** — **PLWH ที่ CD4 < 100** · ผู้ปลูกถ่ายอวัยวะ · ใช้ steroid ระยะยาว

### อาการ
**ระบบประสาท**
- เยื่อหุ้มสมองอักเสบแบบเฉียบพลัน กึ่งเฉียบพลัน หรือเรื้อรัง
- **คอแข็งและกลัวแสงพบเพียงราว 1/4–1/3** → **ปวดศีรษะเรื้อรังในผู้ติด HIV ต้องเจาะหลังแม้ไม่มีคอแข็ง**
- **สติเปลี่ยนจากความดันในกะโหลกสูง**
- **เส้นประสาทสมองผิดปกติเกิดช่วงหลัง** — **เส้นประสาทตาเสียบ่อย** (ตามัวจนบอด)
- **cryptococcoma** ในสมอง · granuloma ไขสันหลัง · สมองเสื่อมเรื้อรังจาก hydrocephalus
**ปอด** — ไม่มีอาการ หรือคล้ายปอดอักเสบกึ่งเฉียบพลัน · nodule ต่อมน้ำเหลือง infiltrate โพรง

### วินิจฉัยและรักษา (สไลด์ส่วนนี้เป็นภาพ — ตามแนวทาง WHO/ไทย)
- **วัด opening pressure ทุกครั้งที่เจาะหลัง** · CSF **India ink** · **cryptococcal antigen (CrAg)** ใน CSF และเลือด · culture
- **Induction** — **amphotericin B + flucytosine** (หรือ fluconazole ขนาดสูงถ้าไม่มี flucytosine) → **consolidation fluconazole** → **maintenance fluconazole**
- **ความดันในกะโหลกสูง (≥ 25 cmH₂O) → เจาะระบายน้ำไขสันหลังซ้ำ (therapeutic LP)** — เป็นสาเหตุการตายหลัก · **steroid, mannitol, acetazolamide ไม่ช่วย**
- **เลื่อน ART ไปราว 4–6 สัปดาห์** หลังเริ่มยาฆ่าเชื้อรา (IRIS ในสมอง)
- **คัดกรอง serum CrAg** ในผู้ที่ CD4 ต่ำ (< 100) → ผลบวกแต่ไม่มีอาการ ให้เจาะหลังและให้ fluconazole แบบ pre-emptive

### สรุปยาป้องกันโรคฉวยโอกาสตาม CD4 (ตารางในสไลด์เป็นภาพ — ตามแนวทาง)
| CD4 (cells/mm³) | โรค | ยาป้องกัน |
|---|---|---|
| **< 200** | **PCP** (และ toxoplasmosis) | **TMP-SMX** |
| **< 150** ในพื้นที่ชุก | Histoplasmosis | itraconazole (ถ้าเริ่ม ART ไม่ได้ใน 4 สัปดาห์) |
| **< 100** | **Cryptococcosis** | **คัดกรอง CrAg** → บวกให้ fluconazole |
| **< 100** ในพื้นที่ชุก | Talaromycosis | itraconazole (ถ้าเริ่ม ART ไม่ได้ใน 4 สัปดาห์) |
| **< 50** และไม่ได้ ART/ยัง viremic | MAC | azithromycin |
| ทุกระดับ | **วัณโรค** | **คัดกรองอาการ → ให้ยารักษา LTBI** ถ้าไม่มี active TB |

**หยุดยาป้องกัน** เมื่อ ART ทำให้ **CD4 สูงเกินเกณฑ์นานพอและ VL ตรวจไม่พบ** — เพราะ ART คือการป้องกันที่ดีที่สุด
""",
    ["Crypto: C. neoformans (มูลนกพิราบ) · C. gattii (ยูคาลิปตัส) · CD4 < 100",
     "Crypto meningitis: คอแข็งเพียง 1/4–1/3 · ICP สูงทำให้ซึม · CN II เสียช่วงหลัง",
     "วัด opening pressure · ICP สูง → therapeutic LP ซ้ำ · steroid ไม่ช่วย",
     "เลื่อน ART 4–6 สัปดาห์หลังเริ่มรักษา crypto meningitis",
     "CD4 < 200 TMP-SMX · < 100 คัดกรอง CrAg · < 50 MAC ถ้าไม่ได้ ART"],
    [mcq(N(26), "A man with HIV (CD4 40 cells/µL) has 3 weeks of worsening headache and blurred vision but no neck stiffness. Lumbar puncture shows an opening pressure of 38 cmH2O, and CSF India ink is positive. In addition to antifungal induction therapy, what is the most important immediate measure?",
         ["Start ART today", "Dexamethasone to reduce intracranial pressure", "Repeated therapeutic lumbar punctures to lower CSF pressure",
          "Mannitol and acetazolamide", "Wait for culture before any treatment"], 2,
         "**Cryptococcal meningitis** — CD4 < 100 · ปวดศีรษะเรื้อรัง · สไลด์ย้ำว่า **คอแข็งพบเพียง 1/4–1/3** และ **สติเปลี่ยนจากความดันในกะโหลกสูง** · **เส้นประสาทตาเสียบ่อย**\n\n**ความดันในกะโหลกสูงเป็นสาเหตุการตายหลัก** → **เจาะระบายน้ำไขสันหลังซ้ำ** เมื่อ opening pressure ≥ 25 cmH₂O · **steroid, mannitol และ acetazolamide ไม่ช่วยและอาจเป็นผลเสีย** · **เลื่อน ART ไปราว 4–6 สัปดาห์** เพราะ IRIS",
         "Crypto meningitis + ICP สูง → therapeutic LP ซ้ำ", "Cryptococcal meningitis and ICP", R("Cryptococcus — clinical manifestations"), NLN + ["2.3.1-3(7)", "B3.2.2(1)"]),
     mcq(N(27), "A newly diagnosed man with HIV has CD4 160 cells/µL, no symptoms and a normal chest radiograph. Which opportunistic-infection prophylaxis is indicated now?",
         ["Azithromycin weekly for MAC", "Trimethoprim-sulfamethoxazole for Pneumocystis", "Fluconazole for all patients", "Itraconazole for all patients", "No prophylaxis is ever needed if ART is started"], 1,
         "**CD4 < 200 → TMP-SMX ป้องกัน PCP** (และช่วยป้องกัน toxoplasmosis) ร่วมกับเริ่ม ART โดยเร็ว\n\nข้ออื่น: **MAC prophylaxis** ใช้เมื่อ CD4 < 50 และไม่ได้ ART เท่านั้น (สไลด์: ไม่แนะนำถ้าเริ่ม ART ทันที) · **fluconazole** ให้เมื่อคัดกรอง CrAg บวก (CD4 < 100) · **itraconazole** สำหรับ talaro/histo ในพื้นที่ชุกเมื่อเริ่ม ART ไม่ได้ใน 4 สัปดาห์",
         "CD4 < 200 → TMP-SMX", "OI prophylaxis", ["ตาราง OI prophylaxis ในสไลด์เป็นภาพ — " + TG], NLN + ["2.3.1(18)"]),
    ], NLN + ["2.3.1-3(7)", "B3.2.2(1)", "2.3.1(18)"])

# ───────────────────────────── MEQ / OSCE
LECNAME = "AIDS and HIV infection (พ.ญ.มนัสวี)"
MEQ = [{"id": "ID-HIV-MEQ-01", "part": "MEQ", "lec": "5/10", "lecture": LECNAME,
 "topic": "Advanced HIV disease presenting with PCP — diagnosis, steroid, prophylaxis and ART timing",
 "vignette": """ผู้ป่วยชายไทยอายุ 34 ปี อาชีพพนักงานบริษัท มาโรงพยาบาลด้วยอาการเหนื่อยมากขึ้นเรื่อย ๆ 3 สัปดาห์
PI: 3 สัปดาห์ก่อน ไอแห้ง มีไข้ต่ำ ๆ เหนื่อยเวลาขึ้นบันได 1 สัปดาห์ก่อนเหนื่อยแม้เดินในบ้าน น้ำหนักลด 6 กก. ใน 2 เดือน กลืนแล้วเจ็บ
PH: ไม่มีโรคประจำตัว เคยรักษาซิฟิลิสเมื่อ 3 ปีก่อน ไม่เคยตรวจ HIV
PE: BT 38.2 C, PR 112/min, RR 28/min, BP 118/72 mmHg, SpO2 92% room air → 84% หลังเดิน 1 นาที
ผอม · ฝ้าขาวในช่องปากเช็ดออกได้ · ปอด fine crackles ทั้งสองข้างเล็กน้อย
Lab: CXR bilateral perihilar ground-glass opacities ไม่มี effusion · LDH 620 U/L · ABG (room air) PaO2 64 mmHg, A–a gradient 40 mmHg
Anti-HIV (A1, A2, A3) positive · CD4 28 cells/mm³ (4%)""",
 "questions": [
  {"q": "1. จงให้การวินิจฉัยโรคปอดที่น่าจะเป็นที่สุด และการตรวจที่ใช้ยืนยัน (3 คะแนน)",
   "a": """**Pneumocystis pneumonia (PCP)** ใน advanced HIV disease
เหตุผล: **CD4 < 200** · เหนื่อยกึ่งเฉียบพลัน ไอแห้ง ไข้ · **exertional desaturation** (92 → 84%) · CXR **bilateral perihilar GGO** ไม่มี effusion · **LDH สูง > 500**
**ยืนยัน**: หาเชื้อในเสมหะ (induced sputum) หรือ **BAL** ด้วย **silver stain (GMS), Giemsa หรือ DFA** · **β-D-glucan** ช่วยสนับสนุน (ลบช่วยตัดโรค) · เพาะเชื้อไม่ได้"""},
  {"q": "2. จงบอกการรักษา PCP และข้อบ่งชี้ของยาเสริมที่ผู้ป่วยรายนี้ต้องได้ (3 คะแนน)",
   "a": """- **TMP-SMX** ขนาดรักษา นาน **21 วัน**
- **Prednisone** เพราะ **PaO₂ 64 < 70** และ **A–a gradient 40 ≥ 35** — เริ่มภายใน 72 ชม.: **40 มก. วันละ 2 ครั้ง วันที่ 1–5 → 40 มก. วันละครั้ง วันที่ 6–10 → 20 มก. วันละครั้ง วันที่ 11–21**
- ให้ออกซิเจน"""},
  {"q": "3. จงบอกระยะของโรคตาม WHO clinical staging และโรคร่วมที่พบในผู้ป่วยรายนี้ (2 คะแนน)",
   "a": """**WHO stage 4 = AIDS** — PCP เป็นโรคใน stage 4 และ CD4 < 200
พบร่วม: **oral candidiasis** (stage 3) · **กลืนเจ็บ** → สงสัย **esophageal candidiasis** (stage 4) → รักษาด้วย fluconazole"""},
  {"q": "4. นอกจากรักษา PCP จะคัดกรองและป้องกันโรคฉวยโอกาสอื่นอะไรบ้างที่ระดับ CD4 นี้ (3 คะแนน)",
   "a": """- **คัดกรองวัณโรค** (อาการ CXR เสมหะ Xpert) — พบได้ทุกระดับ CD4 และเมื่อ CD4 ต่ำมักไม่มีโพรง
- **Serum cryptococcal antigen** (CD4 < 100) → บวกต้องเจาะหลังก่อนเริ่ม ART
- **TMP-SMX** ต่อเป็นยาป้องกันหลังรักษาครบ (secondary prophylaxis PCP + ป้องกัน toxoplasmosis)
- CD4 < 50: MAC prophylaxis **ไม่จำเป็นถ้าเริ่ม ART ทันที**
- ถ้าอยู่พื้นที่ชุกและเริ่ม ART ไม่ได้ใน 4 สัปดาห์ → พิจารณา itraconazole ป้องกัน talaromycosis
- ตรวจ **HBV, HCV, ซิฟิลิส**"""},
  {"q": "5. จะเริ่มยาต้านไวรัสเมื่อใด สูตรใด และต้องเฝ้าระวังอะไรหลังเริ่มยา (3 คะแนน)",
   "a": """- เริ่ม ART **ภายใน 2 สัปดาห์** หลังเริ่มรักษา PCP (ไม่ใช่ crypto/TB meningitis จึงไม่ต้องรอนาน) — ถ้า CrAg บวกหรือพบวัณโรคเยื่อหุ้มสมอง ต้องปรับจังหวะ
- สูตร **TDF (หรือ TAF) + 3TC (หรือ FTC) + dolutegravir**
- เฝ้าระวัง **IRIS** — อาการแย่ลงชั่วคราวหรือโรคที่ซ่อนอยู่ปรากฏขึ้น (เช่น วัณโรค) หลังภูมิฟื้นตัว
- ติดตาม **viral load** ให้ตรวจไม่พบ · ไต (ถ้าใช้ TDF) · ยาตีกันถ้าต้องใช้ rifampicin (DTG วันละ 2 ครั้ง)"""}],
 "ref": ["สไลด์ พ.ญ.มนัสวี — PCP, OI in advanced HIV disease, ART"], "nl": ["2.3.1(9)", "2.3.1(18)", "3.3.15", "2.3.1-3(7)"],
 "years": [], "_kind": "meq", "_set": "id"}]

OSCE = [{"id": "ID-HIV-OSCE-01", "part": "OSCE/SAQ", "lec": "5/10", "lecture": LECNAME,
 "topic": "OSCE – Pre-test counselling for HIV testing (5C)",
 "station": "OSCE (ให้คำปรึกษาผู้ป่วยมาตรฐาน) 5 นาที",
 "instruction": """หญิงอายุ 26 ปี มาคลินิกเพราะเพิ่งได้รับการวินิจฉัย **ซิฟิลิสระยะที่ 2** แพทย์ต้องการส่งตรวจ HIV

ผู้ป่วยกังวลว่า "ถ้าผลเป็นบวกจะมีคนรู้ไหม แล้วถ้าติดแล้วจะต้องตายเลยหรือเปล่า"

**จงให้คำปรึกษาก่อนการตรวจ HIV (pre-test counselling) ภายใน 5 นาที**""",
 "answer": """**เกณฑ์ให้คะแนน (10 คะแนน)**

| ข้อ | สิ่งที่ต้องทำ | คะแนน |
|---|---|---|
| 1 | แนะนำตัว สร้างความไว้วางใจ ใช้ห้องที่เป็นส่วนตัว | 1 |
| 2 | อธิบาย **เหตุผลที่ควรตรวจ** — เป็นโรคติดต่อทางเพศสัมพันธ์ ซึ่งแนวทางไทยกำหนดให้ตรวจ HIV และแผลจากซิฟิลิสเพิ่มโอกาสติด HIV | 1 |
| 3 | **ประเมินความเสี่ยง** — คู่นอน การใช้ถุงยาง ช่วงเวลาที่สัมผัสเสี่ยงครั้งล่าสุด (เพื่อประเมิน window period) การตั้งครรภ์ | 1 |
| 4 | อธิบาย **วิธีตรวจและความหมายของผล** — ผลลบ ผลบวก และผลสรุปไม่ได้ · ถ้าเพิ่งสัมผัสเสี่ยงอาจอยู่ใน **window period** ต้องตรวจซ้ำ | 2 |
| 5 | **Confidential** — รับรองว่า **ผลเป็นความลับ** ไม่แจ้งใครโดยไม่ได้รับอนุญาต | 1 |
| 6 | ตอบความกลัว — ถ้าติดเชื้อ **มียาต้านที่ได้ผลดี กินสม่ำเสมอแล้วอายุขัยใกล้คนปกติ** และ **U=U** คือกดไวรัสได้แล้วไม่แพร่เชื้อทางเพศสัมพันธ์ · **ART ไม่ทำให้หายขาด** แต่คุมได้ | 2 |
| 7 | **Consent** — ถามความสมัครใจและขอความยินยอมก่อนเจาะเลือด · ผู้ป่วยมีสิทธิ์ปฏิเสธ | 1 |
| 8 | บอกแผนหลังได้ผล — **Connection to care** ถ้าบวกเริ่มยาได้เร็ว · ถ้าลบแนะนำการป้องกัน (ถุงยาง PrEP) และแจ้งคู่นอนให้มารักษาซิฟิลิส · เปิดโอกาสถาม | 1 |

**ข้อที่ทำให้เสียคะแนน**: เจาะเลือดก่อนได้รับความยินยอม · ไม่พูดถึงการรักษาความลับ · ใช้คำตัดสินหรือตำหนิพฤติกรรม · บอกว่าไม่มีความเสี่ยงแล้วไม่ต้องตรวจซ้ำ""",
 "ref": ["สไลด์ พ.ญ.มนัสวี — HIV diagnosis 5C, ผู้ที่ควรได้รับการตรวจ"], "nl": ["2.3.1(9)", "3.3.15", "2.3.1(19)"],
 "years": [], "_kind": "meq", "_set": "id"}]

LECTURE = {
 "lec": "5/10", "date": "จ. 5 ต.ค.",
 "title": "AIDS and HIV infection",
 "subtitle": "ไวรัสและวงจรชีวิต · การติดต่อและ U=U · acute HIV · WHO staging · ใครต้องตรวจและ 5C · 4th generation และขั้นตอน A1–A3 · เริ่ม ART และพิษยา · หญิงตั้งครรภ์ · วัณโรค MAC PCP · talaromycosis histoplasmosis cryptococcosis · ยาป้องกันตาม CD4",
 "objectives": [
   "อธิบายวงจรชีวิตของ HIV และบอกว่ายาต้านแต่ละกลุ่มตัดวงจรที่ขั้นใด",
   "ระบุปัจจัยที่เพิ่มการแพร่เชื้อ และอธิบาย U=U ให้ผู้ป่วยเข้าใจ",
   "จดจำอาการของ acute HIV และรู้ว่าเมื่อใดต้องตรวจ HIV",
   "แปลผลการตรวจ HIV ตามขั้นตอน A1–A2–A3 และจัดการผลสรุปไม่ได้หรือช่วง window period",
   "เลือกสูตรยาต้านเริ่มต้น สอนวิธีกินยา และติดตามพิษของ TDF กับยาตีกันกับ rifampicin",
   "ดูแลหญิงตั้งครรภ์ที่ติดเชื้อเพื่อป้องกันการติดเชื้อสู่ทารก",
   "วินิจฉัยและรักษาโรคฉวยโอกาสหลัก — วัณโรค MAC PCP talaromycosis histoplasmosis และ cryptococcosis — ตามระดับ CD4",
   "ให้ยาป้องกันโรคฉวยโอกาสตามระดับ CD4 และกำหนดจังหวะเริ่ม ART ร่วมกับโรคฉวยโอกาส"],
 "nlGap": "เกณฑ์ฯ มีรหัส HIV (`นล. 2.3.1(9)`) PCP (`2.3.1(18)`) และ systemic mycoses (`2.3.1-3(7)`) แต่ **ไม่มีรหัสของยาต้านไวรัสแต่ละกลุ่ม ขั้นตอนตรวจ A1–A3 MAC หรือ histoplasmosis โดยเฉพาะ** และสไลด์ส่วนตาราง (WHO staging, สูตรยาแรก, ยาตีกัน, ยาป้องกันโรคฉวยโอกาส, การรักษา cryptococcosis) เป็นภาพ เนื้อหาส่วนนั้นจึงอิงแนวทางด้านล่าง",
 "guidelines": [
   "**Thailand National Guidelines on HIV/AIDS Treatment and Prevention 2025** — 5C, กลุ่มที่ต้องตรวจ, ขั้นตอน A1–A3, คำแนะนำยา, TDF tubulopathy, OI prophylaxis (อาจารย์อ้างในสไลด์)",
   "**DHHS Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV** — acute HIV และ U=U (อาจารย์อ้างในสไลด์)",
   "**WHO Consolidated Guidelines on HIV (2021) และ Guidelines for diagnosing, preventing and managing cryptococcal disease (2022)**",
   "**NIH/CDC/IDSA Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents with HIV**",
   "**Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases, 9th ed.** (อาจารย์อ้างในสไลด์)"],
 "sections": S, "meq": MEQ, "osce": OSCE,
}

# กระจายตำแหน่งคำตอบให้ไม่กระจุกที่ข้อ B (ข้อที่ตัวเลือกเรียงลำดับตามธรรมชาติไม่สลับ)
ORDERED = {N(7), N(8), N(17), N(29)}
_slot = 0
for s in S:
    for it in s["items"]:
        if it["id"] in ORDERED:
            continue
        tgt = [0, 2, 4, 1, 3][_slot % 5]; _slot += 1
        a = it["answer"]
        if tgt != a:
            ch = it["choices"]; ch[a], ch[tgt] = ch[tgt], ch[a]; it["answer"] = tgt

path = os.path.join(BUILD, "data", "id.json")
data = [l for l in json.load(open(path, encoding="utf-8")) if l.get("lec") != LECTURE["lec"]]
data.append(LECTURE)
seen = set()
for l in data:
    for x in [i for s in l["sections"] for i in s["items"]] + l["meq"] + l["osce"] + [{"id": s["id"]} for s in l["sections"]]:
        assert x["id"] not in seen, "id ซ้ำ: " + x["id"]
        seen.add(x["id"])
nl = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))
codes = {c for s in S for c in s["nl"]} | {c for s in S for i in s["items"] for c in i["nl"]} | {c for m in MEQ + OSCE for c in m["nl"]}
missing = sorted(c for c in codes if c not in nl)
assert not missing, "รหัส นล. ไม่พบ: %s" % missing
for s in S:
    assert "```" not in s["md"], s["id"]
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
ipath = os.path.join(BUILD, "data", "index.json")
idx = json.load(open(ipath, encoding="utf-8"))
for m in idx:
    if m["set"] == "id": m["lectureCount"] = len(data)
json.dump(idx, open(ipath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print("sections %d | items %d | meq %d | osce %d | nl %d" % (len(S), sum(len(s["items"]) for s in S), len(MEQ), len(OSCE), len(codes)))
print("answer positions:", dict(sorted(Counter(i["answer"] for s in S for i in s["items"]).items())))
print("id.json มี %d คาบ: %s" % (len(data), [l["lec"] for l in data]))
