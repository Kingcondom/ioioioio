from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Infectious"

# ---------------------------------------------------------------- 03-01 Malaria biology & dx
F_CYCLE = fig("id-03-01-f1", "วงจรชีวิตเชื้อมาลาเรียในคน และตำแหน่งที่ยาออกฤทธิ์", '''<svg viewBox="0 0 740 440">
 <defs><marker id="id-03-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="10" y="10" width="200" height="60" rx="10" class="c2soft"/>
 <text x="110" y="34" text-anchor="middle" class="tb">ยุงก้นปล่อง Anopheles</text>
 <text x="110" y="54" text-anchor="middle" class="t3">กัด → ปล่อย sporozoite</text>
 <path d="M110 70V100" class="ln" marker-end="url(#id-03-01-a)"/>
 <rect x="10" y="102" width="330" height="150" rx="12" class="sunk"/>
 <text x="22" y="124" class="tb">ตับ (liver stage) — ยังไม่มีไข้</text>
 <rect x="24" y="136" width="140" height="44" rx="8" class="box"/>
 <text x="94" y="155" text-anchor="middle" class="t2">Hepatic schizont</text>
 <text x="94" y="171" text-anchor="middle" class="t3">แบ่งตัว 1–2 wk</text>
 <rect x="184" y="136" width="146" height="44" rx="8" class="misssoft"/>
 <text x="257" y="155" text-anchor="middle" class="tb">Hypnozoite</text>
 <text x="257" y="171" text-anchor="middle" class="t3">เฉพาะ P. vivax / ovale</text>
 <text x="184" y="202" class="t3">หลับอยู่หลายเดือน → relapse</text>
 <rect x="184" y="212" width="146" height="30" rx="8" class="ok"/>
 <text x="257" y="232" text-anchor="middle" class="tw">Primaquine</text>
 <path d="M94 180V280" class="ln" marker-end="url(#id-03-01-a)"/>
 <text x="104" y="232" class="t3">merozoite</text>
 <text x="104" y="248" class="t3">ออกสู่เลือด</text>
 <rect x="10" y="282" width="720" height="148" rx="12" class="badsoft"/>
 <text x="22" y="304" class="tb">เลือด (blood stage) — ทำให้เกิดอาการ</text>
 <rect x="30" y="318" width="120" height="40" rx="8" class="box"/>
 <text x="90" y="343" text-anchor="middle" class="t2">Ring form</text>
 <path d="M150 338H178" class="ln" marker-end="url(#id-03-01-a)"/>
 <rect x="180" y="318" width="120" height="40" rx="8" class="box"/>
 <text x="240" y="343" text-anchor="middle" class="t2">Trophozoite</text>
 <path d="M300 338H328" class="ln" marker-end="url(#id-03-01-a)"/>
 <rect x="330" y="318" width="120" height="40" rx="8" class="box"/>
 <text x="390" y="343" text-anchor="middle" class="t2">Schizont</text>
 <path d="M450 338H478" class="ln" marker-end="url(#id-03-01-a)"/>
 <rect x="480" y="318" width="236" height="40" rx="8" class="bad"/>
 <text x="598" y="335" text-anchor="middle" class="tw">RBC แตก → merozoite</text>
 <text x="598" y="351" text-anchor="middle" class="tw">hemolysis + cytokine → ไข้</text>
 <path d="M598 358V376H90V360" class="lnf" marker-end="url(#id-03-01-a)"/>
 <text x="110" y="394" class="t3">วนซ้ำทุก 48 ชม. (vivax/ovale) · 72 ชม. (malariae) · 24 ชม. (knowlesi)</text>
 <rect x="30" y="402" width="300" height="20" rx="4" class="c1"/>
 <text x="180" y="417" text-anchor="middle" class="tw">ACT · artesunate · chloroquine · quinine</text>
 <rect x="420" y="102" width="310" height="150" rx="12" class="c1soft"/>
 <text x="432" y="124" class="tb">Gametocyte (ring บางส่วน)</text>
 <text x="432" y="146" class="t2">ไม่ก่ออาการ แต่ติดต่อกลับสู่ยุง</text>
 <text x="432" y="168" class="t2">P. falciparum: crescent/banana</text>
 <rect x="432" y="182" width="286" height="30" rx="8" class="ok"/>
 <text x="575" y="202" text-anchor="middle" class="tw">Primaquine single dose (Pf)</text>
 <text x="432" y="236" class="t3">ตัดวงจรการแพร่เชื้อในชุมชน</text>
 <path d="M240 318L470 252" class="lnf" marker-end="url(#id-03-01-a)"/>
 <path d="M520 102L210 40" class="lnf" marker-end="url(#id-03-01-a)"/>
 <text x="380" y="62" class="t3">ยุงดูดเลือดได้ gametocyte</text>
</svg>''', "ไล่ลูกศรจากยุง → ตับ → เลือด · ยา ACT/chloroquine ฆ่าระยะในเลือด ส่วน primaquine ฆ่า hypnozoite (กัน relapse ใน vivax/ovale) และ gametocyte (ตัดการแพร่เชื้อใน falciparum)")

S1 = sec("id-03-01", "Malaria: life cycle, clinical & diagnosis",
    "Pf, Pv พบบ่อยสุดในไทย · ชายแดน · hypnozoite (Pv/Po) → relapse · severe มักเป็น Pf · thick/thin smear gold standard · RDT แยกได้แค่ Pf/non-Pf",
    minutes=9, source=f"{D} หน้า 108–117, 131–132", nl=["2.3.1(14)", "B2.3(9)", "3.1.3"],
    md='''
### เชื้อและการติดต่อ

- **Plasmodium falciparum, vivax, ovale, malariae, knowlesi** · ยุงก้นปล่อง **Anopheles spp.**
- **P. vivax และ P. falciparum พบบ่อยที่สุดในไทย**
- พื้นที่เสี่ยง: **จังหวัดติดชายแดน** พม่า ลาว กัมพูชา มาเลเซีย เช่น **กาญจนบุรี ราชบุรี จันทบุรี ตาก อำนาจเจริญ นราธิวาส**
- P. knowlesi (ลิงแสม) พบในป่าภาคใต้/ตะวันตก (เสริม)

### Life cycle → อาการ

[[fig:id-03-01-f1]]

- **P. vivax, P. ovale**: sporozoite บางส่วนกลายเป็น **hypnozoite** ในตับ
- Merozoite แบ่งตัวใน RBC → **hemolysis** → cytokine ↑ → **ไข้**
- Ring form บางส่วนกลายเป็น **gametocyte** (ติดต่อกลับสู่ยุง)

| คำ | ความหมาย |
|---|---|
| Primary attack | เป็นครั้งแรก |
| **Relapse** | เป็นซ้ำโดยไม่ได้รับเชื้อใหม่ จาก **hypnozoite (P. vivax/P. ovale)** |
| **Recrudescence** | เป็นซ้ำโดยไม่ได้รับเชื้อใหม่ เพราะ **เชื้อในเลือดกำจัดไม่หมด** (ยาไม่พอ/ดื้อยา) |
| Reinfection | ได้รับเชื้อใหม่ |

### อาการ

- **ประวัติอาศัย/เดินทางจากพื้นที่ระบาดภายใน 2 เดือน** · เคยเป็น malaria ใน 1 ปี
- **ไข้สูง/ไข้เป็นรอบ** (หนาวสั่น → ร้อน → เหงื่อออก) · ไข้วันเว้นวัน = vivax/ovale (เสริม)
- Headache, malaise, N/V, anorexia · **hepatosplenomegaly** · ซีด เหลือง เกล็ดเลือดต่ำ
- **Severe malaria (ส่วนใหญ่ P. falciparum)**: alteration of consciousness, seizure, dyspnea (pulmonary edema/ARDS), shock, jaundice, oliguria/anuria, **hemoglobinuria** (blackwater), severe anemia, **hypoglycemia** · hyperparasitemia (> 10% ตาม WHO (เสริม))

### Investigation

- **Thick & thin blood smear = gold standard**
  - **Thick**: screening ว่าติดเชื้อหรือไม่ และนับจำนวนเชื้อ
  - **Thin**: ดู RBC morphology → **ระบุชนิดเชื้อ** · คำนวณ % parasitemia
- **Rapid diagnostic test (RDT)**: บอกได้แค่ **P. falciparum หรือ non-P. falciparum**
- ตรวจ **G6PD** ก่อนให้ primaquine · glucose, Cr, bilirubin, CBC ในรายรุนแรง (เสริม)

### Thin smear แยกชนิด

| ชนิด | ขนาด RBC | ลักษณะเด่น |
|---|---|---|
| **P. falciparum** | **ปกติ** | Ring **double chromatin**, **multiple rings** ใน RBC เดียว, **accolé (appliqué)** · gametocyte **crescent/banana** · มักเห็นแค่ ring กับ gametocyte |
| P. malariae | ปกติ | Trophozoite **band form** |
| **P. vivax** | **โต** | Trophozoite **amoeboid** · **Schüffner's dots** |
| P. ovale | โต | Trophozoite/RBC **รูปไข่ ขอบหยัก (fimbriated, tufted ends)** · Schüffner's dots ชัด |

> RBC โตขึ้น = vivax/ovale · RBC ขนาดปกติ + หลาย ring + double chromatin = falciparum
''',
    figs=[F_CYCLE],
    pearls=[
        "Pf กับ Pv พบบ่อยสุดในไทย · จังหวัดชายแดน (ตาก กาญจนบุรี ฯลฯ)",
        "Hypnozoite เฉพาะ vivax/ovale → relapse · recrudescence = เชื้อเก่าในเลือดกำจัดไม่หมด",
        "Thick smear = มีเชื้อไหม · thin smear = เชื้อชนิดไหน · RDT แยกแค่ Pf/non-Pf",
        "Pf: RBC ปกติ double chromatin multiple rings accolé crescent gametocyte",
        "Pv: RBC โต amoeboid Schüffner's dots",
    ],
    items=[
        mcq("ID-03-01-1",
            "A 25-year-old woman has fever every other day. Malaria is suspected. The thin blood smear shows enlarged infected red blood cells containing amoeboid trophozoites with Schüffner's dots. What is the causative organism?",
            "Plasmodium vivax",
            ["Plasmodium falciparum", "Plasmodium ovale", "Plasmodium malariae", "Plasmodium knowlesi"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ภาพ smear บรรยายเป็นข้อความ)",
            explain='''**RBC โต + amoeboid trophozoite + Schüffner's dots** + ไข้วันเว้นวัน = **P. vivax** (สไลด์เฉลยจาก infected RBC enlargement)
- P. falciparum ทำให้ RBC ขนาดปกติ เห็น ring double chromatin หลาย ring
- P. ovale ก็ทำให้ RBC โตและมี Schüffner's dots แต่ RBC เป็นรูปไข่ขอบหยัก ไม่ใช่ amoeboid
- P. malariae RBC ขนาดปกติ trophozoite เป็น band form ไข้ทุก 72 ชม.
- P. knowlesi RBC ขนาดปกติ ไข้ทุก 24 ชม.''',
            pearl="RBC โต + amoeboid + Schüffner = P. vivax", topic="Malaria smear",
            ref=[f"{D} หน้า 117, 131–132"], nl=["2.3.1(14)", "B2.3(9)"]),
        mcq("ID-03-01-2",
            "A 30-year-old man was treated for P. vivax malaria with chloroquine alone 4 months ago and recovered completely. He has not left Bangkok since. He now has fever again and the smear shows P. vivax. What is the best term for this episode?",
            "Relapse",
            ["Recrudescence", "Reinfection", "Primary attack", "Drug-induced hemolysis"],
            explain='''ไม่ได้รับเชื้อใหม่ (อยู่กรุงเทพฯ) + เคยรักษา **vivax ด้วย chloroquine อย่างเดียวโดยไม่ได้ primaquine** → hypnozoite ในตับตื่นขึ้นมา = **relapse**
- Recrudescence คือเชื้อในเลือดกำจัดไม่หมด มักเกิดภายในไม่กี่สัปดาห์ ไม่ได้มาจาก hypnozoite
- Reinfection ต้องได้รับเชื้อใหม่จากพื้นที่ระบาด
- Primary attack ไม่ใช่ เพราะเคยเป็นแล้ว
- Drug-induced hemolysis ไม่ทำให้พบเชื้อในเลือด''',
            pearl="Vivax/ovale ไม่ได้ primaquine → relapse จาก hypnozoite", topic="Relapse vs recrudescence",
            ref=[f"{D} หน้า 110–111"], nl=["2.3.1(14)"]),
        mcq("ID-03-01-3",
            "A 32-year-old soldier returns from the Thai–Myanmar border in Tak with fever and chills for 3 days. A rapid diagnostic test for malaria is positive for non-P. falciparum. What is the most appropriate next step to determine the species?",
            "Thin blood smear",
            ["Thick blood smear alone", "Repeat rapid diagnostic test", "Hemoculture", "Malaria antibody serology"],
            explain='''RDT บอกได้แค่ **Pf หรือ non-Pf** → ต้องดู **thin blood smear** เพื่อดู RBC morphology และ **ระบุชนิดเชื้อ** (vivax/ovale/malariae/knowlesi) ซึ่งมีผลต่อการให้ primaquine
- Thick smear เหมาะสำหรับ screening/นับจำนวนเชื้อ แต่ระบุชนิดไม่ได้ดี
- RDT ซ้ำก็ยังแยกชนิดไม่ได้
- Hemoculture ไม่ใช้วินิจฉัย malaria
- Antibody serology บอกการติดเชื้อในอดีต ไม่ใช่การวินิจฉัยโรคปัจจุบัน''',
            pearl="Thick = มีเชื้อไหม · thin = ชนิดอะไร", topic="Malaria investigation",
            ref=[f"{D} หน้า 113"], nl=["2.3.1(14)", "B2.3(9)"]),
        mcq("ID-03-01-4",
            "A 26-year-old rubber tapper from Chanthaburi has fever for 6 days, confusion and dark urine. Thin smear shows normal-sized red cells containing multiple ring forms with double chromatin dots and banana-shaped gametocytes. Which species is responsible?",
            "Plasmodium falciparum",
            ["Plasmodium vivax", "Plasmodium ovale", "Plasmodium malariae", "Babesia microti"],
            explain='''RBC ขนาดปกติ + **multiple rings, double chromatin** + **gametocyte รูปกล้วย (crescent)** + ซึม ปัสสาวะดำ (hemoglobinuria) = **severe P. falciparum**
- P. vivax และ P. ovale ทำให้ RBC โต
- P. malariae trophozoite เป็น band form ไม่มี crescent gametocyte
- Babesia มี ring form คล้ายได้ (Maltese cross) แต่ไม่มี gametocyte รูปกล้วย และไม่ใช่โรคในบริบทนี้''',
            pearl="Banana gametocyte = P. falciparum", topic="Pf morphology",
            ref=[f"{D} หน้า 112, 116, 140"], nl=["2.3.1(14)", "B2.3(9)"]),
    ])

# ---------------------------------------------------------------- 03-02 Malaria treatment
F_TX = fig("id-03-02-f1", "เลือกยารักษามาลาเรีย (ตามสไลด์)", '''<svg viewBox="0 0 740 420">
 <defs><marker id="id-03-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="260" y="10" width="220" height="40" rx="10" class="acsoft"/>
 <text x="370" y="35" text-anchor="middle" class="tb">Malaria ยืนยันแล้ว</text>
 <path d="M320 50L150 84" class="ln" marker-end="url(#id-03-02-a)"/>
 <path d="M420 50L590 84" class="ln" marker-end="url(#id-03-02-a)"/>
 <rect x="10" y="86" width="280" height="54" rx="10" class="bad"/>
 <text x="150" y="108" text-anchor="middle" class="tw">Severe / complicated</text>
 <text x="150" y="128" text-anchor="middle" class="tw">ซึม ชัก ช็อก AKI เหลือง น้ำตาลต่ำ</text>
 <rect x="10" y="150" width="280" height="110" rx="10" class="badsoft"/>
 <text x="22" y="174" class="tb">IV artesunate</text>
 <text x="22" y="194" class="t3">(IV quinine ถ้าไม่มี artesunate)</text>
 <text x="22" y="216" class="t2">ดีขึ้น/กินได้ → ACT 3 วัน</text>
 <text x="22" y="236" class="t2">+ primaquine</text>
 <text x="22" y="254" class="t3">เช็ค glucose ทุกราย (quinine → น้ำตาลต่ำ)</text>
 <rect x="320" y="86" width="410" height="40" rx="10" class="ok"/>
 <text x="525" y="111" text-anchor="middle" class="tw">Uncomplicated</text>
 <rect x="320" y="136" width="200" height="124" rx="10" class="oksoft"/>
 <text x="332" y="158" class="tb">P. falciparum</text>
 <text x="332" y="180" class="t2">DHA-piperaquine</text>
 <text x="332" y="198" class="t3">หรือ artesunate-pyronaridine</text>
 <text x="332" y="222" class="t2">+ primaquine</text>
 <text x="332" y="240" class="t3">(ฆ่า gametocyte)</text>
 <rect x="530" y="136" width="200" height="124" rx="10" class="c1soft"/>
 <text x="542" y="158" class="tb">P. vivax / ovale</text>
 <text x="542" y="180" class="t2">Chloroquine</text>
 <text x="542" y="200" class="t2">+ primaquine 14 วัน</text>
 <text x="542" y="220" class="t3">(ฆ่า hypnozoite)</text>
 <text x="542" y="244" class="t3">Pm / Pk: chloroquine (หรือ ACT)</text>
 <rect x="10" y="280" width="350" height="128" rx="10" class="misssoft"/>
 <text x="22" y="304" class="tb">ตั้งครรภ์</text>
 <text x="22" y="326" class="t2">Pf ไตรมาส 1: quinine + clindamycin</text>
 <text x="22" y="348" class="t2">Pf ไตรมาส 2–3: DHA-piperaquine</text>
 <text x="22" y="370" class="t2">Non-Pf: chloroquine</text>
 <text x="22" y="394" class="tb">ห้าม primaquine (ทารก hemolysis)</text>
 <rect x="380" y="280" width="350" height="128" rx="10" class="c2soft"/>
 <text x="392" y="304" class="tb">G6PD deficiency</text>
 <text x="392" y="326" class="t2">รักษาเหมือนเดิม</text>
 <text x="392" y="348" class="t2">แต่ลดขนาด/ไม่ให้ primaquine</text>
 <text x="392" y="370" class="t3">(oxidant → NADPH/GSH ไม่พอ → hemolysis)</text>
 <text x="392" y="394" class="t3">ตรวจ G6PD ก่อนให้ primaquine (เสริม)</text>
</svg>''', "แยก severe ก่อน (IV artesunate) แล้วเลือกยาตามชนิดเชื้อ · primaquine เป็นยาตัวที่สองที่ต้องระวังในหญิงตั้งครรภ์และ G6PD deficiency")

S2 = sec("id-03-02", "Malaria: treatment & prevention",
    "Pf: DHA-PPQ หรือ AS-pyronaridine + primaquine · Pv/Po: CQ + PQ · ท้องไตรมาส 1 quinine + clinda · severe IV artesunate · G6PD ลด/งด PQ · ไทยไม่ให้ยาป้องกัน",
    minutes=9, source=f"{D} หน้า 118–130, 133–144", nl=["2.3.1(14)", "B1.7.2"],
    md='''
### Uncomplicated malaria (ตามสไลด์)

| เชื้อ | ยา |
|---|---|
| **P. falciparum** | **Dihydroartemisinin-piperaquine (DHA-PPQ) + primaquine** หรือ **artesunate-pyronaridine + primaquine** |
| **P. vivax / P. ovale** | **Chloroquine + primaquine** |
| P. malariae / P. knowlesi | **Chloroquine** หรือ artemisinin-based combination (ACT) |

- **Primaquine** ใช้กำจัด **hypnozoite** (vivax/ovale กัน relapse) หรือ **gametocyte** (falciparum ตัดการแพร่เชื้อ)
- ขนาดยา (สไลด์หน้า 118–125 เป็นตารางภาพ — ตามแนวทางกรมควบคุมโรค/WHO (เสริม)):
  - DHA-PPQ วันละครั้ง **3 วัน** (DHA 4 mg/kg/d, PPQ 18 mg/kg/d) · primaquine **single low dose 0.25 mg base/kg** สำหรับ Pf
  - Chloroquine รวม **25 mg base/kg ใน 3 วัน** (10–10–5) · primaquine **0.25–0.5 mg base/kg/day × 14 วัน** สำหรับ vivax/ovale

### หญิงตั้งครรภ์

| เชื้อ | ยา |
|---|---|
| P. falciparum **ไตรมาส 1** | **Quinine sulfate + clindamycin** (7 วัน (เสริม)) |
| P. falciparum ไตรมาส 2–3 | **DHA-PPQ** |
| Non-falciparum | **Chloroquine** (ให้ chloroquine prophylaxis รายสัปดาห์จนคลอด แล้วค่อยให้ primaquine หลังคลอด/หลังหยุดให้นม (เสริม)) |

- **ห้าม primaquine** เพราะทารกในครรภ์อาจ hemolysis (ไม่รู้ G6PD ของทารก)

### G6PD deficiency

- รักษาเหมือน uncomplicated malaria แต่ **ลดขนาดหรือไม่ให้ primaquine** (เช่น 0.75 mg/kg สัปดาห์ละครั้ง × 8 สัปดาห์ สำหรับ vivax (เสริม))
- กลไก: G6PD สร้าง **NADPH** → รักษา **glutathione (GSH)** ไว้ป้องกัน oxidative stress · ขาด G6PD → primaquine (oxidant) → RBC แตก (Heinz body, bite cell) → **ซีด เหลือง ปัสสาวะดำ**

### Complicated/severe malaria

- **IV artesunate** (2.4 mg/kg ที่ 0, 12, 24 ชม. แล้ววันละครั้ง (เสริม)) — ดีกว่า quinine
- **IV quinine** ถ้าไม่มี artesunate (เสี่ยง **hypoglycemia**, QT ยาว, cinchonism)
- อาการดีขึ้น/กินได้ → เปลี่ยนเป็นยากิน **ACT** (DHA-PPQ หรือ artesunate-pyronaridine) **+ primaquine**
- Supportive: **เช็ค glucose ทันทีเมื่อซึม/ชัก** (hypoglycemia จากเชื้อ + quinine + ตั้งครรภ์), ดูแล AKI, ปอดบวมน้ำ, ให้เลือดเมื่อซีดมาก (เสริม)

[[fig:id-03-02-f1]]

### Prevention

- **ป้องกันยุงกัด**: มุ้ง (ชุบยา) **ยาทากันยุง** โดยเฉพาะช่วงกลางคืน เสื้อแขนยาว
- **ไม่แนะนำให้กินยาป้องกัน (chemoprophylaxis) ในประเทศไทย** เพราะความชุกต่ำ และมีปัญหาเชื้อดื้อยา
  - ให้ยาป้องกันเมื่อไปพื้นที่ที่ **API (annual parasite incidence ต่อประชากร 1,000 คน) > 10 ต่อปี** — ไทย API < 1
- **Advice**: ถ้ามีไข้ภายใน **3 วัน – 2 เดือน** หลังออกจากพื้นที่ระบาด ให้สงสัย malaria และรีบมาตรวจ

> ข้อสอบเก่าบางข้อใช้สูตรเดิม **artesunate + mefloquine** สำหรับ uncomplicated Pf — แนวทางไทยปัจจุบัน (ตามสไลด์) ใช้ **DHA-PPQ + primaquine** ถ้าเจอตัวเลือกเก่าให้เลือก ACT ที่มีในตัวเลือก
''',
    figs=[F_TX],
    pearls=[
        "Uncomplicated Pf: DHA-PPQ (หรือ AS-pyronaridine) + primaquine",
        "Pv/Po: chloroquine + primaquine (กัน relapse)",
        "ท้องไตรมาส 1 + Pf: quinine + clindamycin · ห้าม primaquine ตลอดการตั้งครรภ์",
        "Severe malaria: IV artesunate (quinine ถ้าไม่มี) · ซึม/ชัก เช็คน้ำตาลก่อน",
        "ไทยไม่ให้ยาป้องกัน (API < 1) → ใช้ยากันยุง มุ้ง · ไข้ใน 2 เดือนหลังออกจากป่าให้นึกถึง",
    ],
    items=[
        mcq("ID-03-02-1",
            "A 30-year-old Thai woman has fever and chills for 2 weeks. Temperature 38.5 °C, liver span 10 cm. She is alert with stable vital signs and normal renal function. The blood smear shows normal-sized red cells with multiple ring forms with double chromatin. She is not pregnant and G6PD is normal. What is the most appropriate treatment?",
            "Dihydroartemisinin-piperaquine plus primaquine",
            ["Quinine plus clindamycin", "Chloroquine plus primaquine", "Chloroquine plus doxycycline", "Intravenous artesunate"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับตัวเลือกให้ตรงแนวทางปัจจุบัน)",
            explain='''**Uncomplicated P. falciparum** (ring double chromatin หลายตัว ไม่มีอาการรุนแรง) ในผู้ใหญ่ไม่ตั้งครรภ์ → **ACT: DHA-PPQ + primaquine** (หรือ artesunate-pyronaridine + primaquine) — ข้อสอบเก่าเฉลย "artesunate + mefloquine" ซึ่งเป็น ACT สูตรเดิมของไทย
- Quinine + clindamycin ใช้ในหญิงตั้งครรภ์ไตรมาสแรก
- Chloroquine + primaquine ใช้กับ vivax/ovale — falciparum ดื้อ chloroquine
- Chloroquine + doxycycline ไม่ใช่สูตรรักษาที่แนะนำ
- IV artesunate ใช้ใน severe malaria ซึ่งรายนี้ไม่มีเกณฑ์''',
            pearl="Uncomplicated Pf = ACT (DHA-PPQ) + primaquine", topic="Uncomplicated Pf",
            ref=[f"{D} หน้า 126, 133–134"], nl=["2.3.1(14)"]),
        mcq("ID-03-02-2",
            "A woman at 10 weeks' gestation has high-grade fever and mild jaundice; other findings are within normal limits and she is fully alert. The blood smear shows ring forms with double chromatin. What is the most appropriate treatment?",
            "Quinine plus clindamycin",
            ["Artesunate plus mefloquine", "Chloroquine plus primaquine", "Quinine plus mefloquine", "Quinine plus doxycycline"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Uncomplicated **P. falciparum ในไตรมาสแรก** → **quinine sulfate + clindamycin** (ตามสไลด์) · ไตรมาส 2–3 ใช้ DHA-PPQ
- Artesunate + mefloquine เป็น ACT ที่สไลด์ไม่ใช้ในไตรมาสแรก (WHO ปี 2022 อนุญาต ACT ในไตรมาสแรกได้แล้ว แต่ข้อสอบไทยยึดตามสไลด์ (เสริม))
- Chloroquine + primaquine เป็นสูตรของ vivax และ primaquine ห้ามในหญิงตั้งครรภ์
- Quinine + mefloquine ไม่ใช่สูตรมาตรฐาน
- Doxycycline ห้ามในหญิงตั้งครรภ์ (ฟันและกระดูกทารก)''',
            pearl="Pf + ตั้งครรภ์ไตรมาส 1 = quinine + clindamycin", topic="Malaria in pregnancy",
            ref=[f"{D} หน้า 127, 135–136"], nl=["2.3.1(14)"]),
        mcq("ID-03-02-3",
            "A 40-year-old woman traveled to Tak 2 weeks ago. For the past week she has had fever, and today she became drowsy and had one generalized seizure. The smear shows ring forms, multiple infected red cells and accolé forms. What is the most appropriate initial management?",
            "Intravenous 50% glucose after a bedside glucose check",
            ["CT scan of the brain", "Intravenous ceftriaxone", "Intravenous phenobarbital", "Lumbar puncture"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''Severe falciparum malaria ที่ซึมและชัก — สิ่งแรกที่แก้ได้ทันทีคือ **hypoglycemia** (เชื้อใช้กลูโคส + TNF ยับยั้ง gluconeogenesis + ถ้าได้ quinine กระตุ้น insulin) → เจาะน้ำตาลปลายนิ้วแล้วให้ **50% glucose IV** (สไลด์เฉลย hypoglycemia) จากนั้นให้ IV artesunate
- CT brain ไม่ใช่สิ่งแรก ภาวะนี้อธิบายได้ด้วย cerebral malaria/hypoglycemia
- Ceftriaxone ใช้ถ้าสงสัย bacterial meningitis แต่ smear ยืนยัน malaria แล้ว
- Phenobarbital ใช้หยุดชักที่ยังชักอยู่ แต่ต้องแก้สาเหตุที่แก้ได้ก่อน
- Lumbar puncture ในผู้ป่วยซึม ชัก ไม่ใช่ initial management''',
            pearl="Severe malaria ซึม/ชัก → เช็คและแก้ hypoglycemia ก่อน", topic="Severe malaria hypoglycemia",
            ref=[f"{D} หน้า 112, 137–138"], nl=["2.3.1(14)"]),
        mcq("ID-03-02-4",
            "A 40-year-old woman has fever and right upper quadrant pain after camping in a forest. Temperature 38.5 °C, tachycardic, BP stable. Creatinine 3.4 mg/dL and total bilirubin 4 mg/dL. The smear shows numerous ring forms and trophozoites within red cells (parasitemia 6%). What is the most appropriate treatment?",
            "Intravenous artesunate",
            ["Oral mefloquine", "Oral primaquine", "Oral chloroquine", "Oral atovaquone-proguanil"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์ (ปรับ Cr/bilirubin ให้เข้าเกณฑ์ severe)",
            explain='''Malaria ที่มี **AKI (Cr > 3) และเหลือง** ร่วมกับ parasitemia สูง = **complicated/severe malaria** → **IV artesunate** (สไลด์เดิมให้ Cr 2.1 ซึ่งต่ำกว่าเกณฑ์ WHO (> 3 mg/dL) จึงปรับตัวเลขให้สอดคล้อง)
- Mefloquine เป็นยากิน ใช้ใน uncomplicated เท่านั้น และไม่ใช้เดี่ยว
- Primaquine ฆ่า hypnozoite/gametocyte ไม่ได้ฆ่าเชื้อในเลือดเร็วพอ
- Chloroquine ใช้กับ non-falciparum uncomplicated
- Atovaquone-proguanil เป็นยากินสำหรับ uncomplicated/ป้องกัน ไม่ใช่ severe''',
            pearl="Severe malaria (AKI, เหลือง, ซึม) → IV artesunate", topic="Severe malaria",
            ref=[f"{D} หน้า 129, 139–140"], nl=["2.3.1(14)"]),
        mcq("ID-03-02-5",
            "A 20-year-old man with non-falciparum malaria is treated with chloroquine, primaquine and an antipyretic. Three days later he develops scleral icterus, pallor and dark urine. What is the most likely mechanism?",
            "Decreased NADPH level in red blood cells",
            ["Drug interaction between chloroquine and the antipyretic", "Biliary obstruction", "Chloroquine-induced hepatotoxicity", "Interruption of enterohepatic circulation"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''หลังได้ยา oxidant (**primaquine**, chloroquine) แล้วซีด เหลือง ปัสสาวะดำ = **hemolysis จาก G6PD deficiency** → G6PD สร้าง **NADPH** ไม่พอ → glutathione ไม่พอ → RBC ทนต่อ oxidative stress ไม่ได้
- Drug interaction ระหว่าง chloroquine กับยาลดไข้ไม่ทำให้ hemolysis
- Biliary obstruction ไม่ทำให้ซีดและปัสสาวะดำแบบ hemoglobinuria
- Chloroquine hepatotoxicity พบได้น้อยมาก และไม่อธิบายการซีดเฉียบพลัน
- Enterohepatic circulation ไม่เกี่ยวกับ hemolysis''',
            pearl="Primaquine + เหลือง ซีด = G6PD deficiency (NADPH ↓)", topic="Primaquine G6PD",
            ref=[f"{D} หน้า 128, 141–142"], nl=["2.3.1(14)", "B1.7.2"]),
        mcq("ID-03-02-6",
            "A medical student plans a 3-day, 2-night hiking trip in Kanchanaburi and asks how to prevent malaria. What is the most appropriate advice?",
            "Use mosquito repellent consistently, especially at night",
            ["No precaution is needed; treat if illness occurs", "Take sulfadoxine-pyrimethamine for 3 days before the trip", "Take doxycycline from 7 days before until after the trip", "Take quinine from 3 days before and daily during the trip"],
            kind="old", src="ตัวอย่างข้อสอบในสไลด์",
            explain='''ประเทศไทย API < 1 ต่อ 1,000 ต่อปี → **ไม่แนะนำ chemoprophylaxis** ให้ **ป้องกันยุงกัด** (ทายากันยุง มุ้ง เสื้อแขนยาว) และแนะนำว่าถ้ามีไข้ภายใน 3 วัน – 2 เดือนให้มาตรวจ
- ไม่ทำอะไรเลยไม่ถูก ยังต้องป้องกันยุงกัด
- Sulfadoxine-pyrimethamine (Fansidar) ไม่ใช้ป้องกันในไทย (ดื้อยา ผลข้างเคียง SJS)
- Doxycycline prophylaxis ใช้เมื่อไปพื้นที่ API > 10 และต้องกินต่อ 4 สัปดาห์หลังออก ไม่ใช่ 7 วัน
- Quinine ไม่ใช้เป็นยาป้องกัน''',
            pearl="เที่ยวป่าในไทย → ยากันยุง ไม่ต้องกินยาป้องกัน", topic="Malaria prevention",
            ref=[f"{D} หน้า 130, 143–144"], nl=["2.3.1(14)", "B1.5.1(5)"]),
    ])

LECTURE = lecture("03", "Malaria",
    "Life cycle · smear · ACT · pregnancy · G6PD · severe malaria · prevention",
    objectives=[
        "อธิบายวงจรชีวิตเชื้อ แยก relapse/recrudescence/reinfection ได้",
        "ใช้ thick/thin smear และ RDT แยกชนิดเชื้อได้",
        "เลือกยาตามชนิดเชื้อ ความรุนแรง การตั้งครรภ์ และ G6PD ได้",
        "ให้คำแนะนำการป้องกันมาลาเรียสำหรับคนเดินป่าในไทยได้",
    ],
    sections=[S1, S2])
