# -*- coding: utf-8 -*-
import json, random, re, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
D = HERE + "data/"   # อ่านจากไฟล์ที่เผยแพร่แล้ว (สคริปต์ลบคาบ 16/11 เดิมแล้วใส่ใหม่ จึงรันซ้ำได้)
O = HERE
sys.path.insert(0, HERE)
import lec_a, lec_b  # noqa
S = lec_a.S
LECNAME = "ทบทวน Microorganism — จุลชีววิทยาคลินิกและปรสิต (บันทึกเสียง จ. 16 พ.ย. + สไลด์ Microorganism 2026)"

ids = json.load(open(D + "id.json", encoding="utf8"))
index = json.load(open(D + "index.json", encoding="utf8"))
NL = json.load(open(D + "nl.json", encoding="utf8"))
tmpl_item = ids[3]["sections"][0]["items"][0]
tmpl_meq = ids[3]["meq"][0]
tmpl_osce = ids[3]["osce"][0]

rng = random.Random(1611)
errs = []
POS = [0,1,2,3,4]*8; rng.shuffle(POS)
for s in S:
    s["source"] = lec_a.SRC
    keys = set(re.findall(r"\[\[img:([\w-]+)\]\]", s["md"]))
    for k in keys:
        if k not in s["imgs"]: errs.append(f"{s['id']} missing img {k}")
    for k, g in s["imgs"].items():
        if k not in keys: errs.append(f"{s['id']} unused img {k}")
        if not os.path.exists(O + g["src"]): errs.append(f"missing file {g['src']}")
    if not s["imgs"]: del s["imgs"]
    for c in s["nl"]:
        if c not in NL: errs.append(f"{s['id']} bad nl {c}")
    for it in s["items"]:
        ch = it["choices"]; assert len(ch) == 5 and len(set(ch)) == 5, it["id"]
        right = ch[0]; rest = ch[1:]; rng.shuffle(rest)
        pos = POS.pop(0); ch = rest[:pos] + [right] + rest[pos:]
        it["choices"] = ch; it["answer"] = pos
        it["kind"] = "mcq"; it.setdefault("src", "")
        for c in it["nl"]:
            if c not in NL: errs.append(f"{it['id']} bad nl {c}")
        it2 = {k: it[k] for k in tmpl_item.keys() if k in it}
        for k in it:
            if k not in it2: it2[k] = it[k]
        it.clear(); it.update(it2)
    order = ["id", "title", "summary", "minutes", "source", "nl", "md", "pearls", "items", "imgs"]
    s2 = {k: s[k] for k in order if k in s}
    s.clear(); s.update(s2)

meq = [
 dict(id="ID-MIC-MEQ-01", part="MEQ", lec="16/11", lecture=LECNAME,
  topic="HIV with subacute headache — CSF interpretation, cryptococcal meningitis, raised ICP and ART timing",
  vignette="ผู้ป่วยชายไทยอายุ 32 ปี มาด้วยปวดศีรษะมากขึ้นเรื่อย ๆ 3 สัปดาห์\nPI: 3 สัปดาห์ก่อนปวดศีรษะทั้งศีรษะ เป็นมากตอนเช้า คลื่นไส้อาเจียน 2 วันก่อนตามัว เห็นภาพซ้อน ไข้ต่ำ ๆ น้ำหนักลด 6 kg ใน 2 เดือน\nPH: 1 ปีก่อนตรวจพบ anti-HIV บวก ไม่ได้รับยาต้านไวรัส\nPE: BT 37.9 C · PR 96/min · BP 128/80 mmHg · alert, oriented · stiff neck เล็กน้อย · CN VI palsy ข้างซ้าย · fundi: papilledema ทั้งสองข้าง · ตุ่มนูนบุ๋มตรงกลาง 4–5 ตุ่มที่หน้าผาก · oral thrush\nLab: CD4 28 cells/µL · CT brain ไม่มีก้อน ไม่มี hydrocephalus\nCSF: opening pressure 36 cmH₂O · WBC 30/µL (L 90%) · protein 95 mg/dL · glucose 30 mg/dL (blood 98) · Gram stain ไม่พบเชื้อ",
  questions=[
   {"q": "1. จงแปลผล CSF และบอกการวินิจฉัยที่เป็นไปได้มากที่สุดพร้อมเหตุผล (3 คะแนน)", "a": "- **opening pressure สูงมาก (> 25)** · **lymphocyte เด่น WBC ไม่สูง** · **glucose ต่ำ** · protein สูง · Gram stain ลบ\n- ร่วมกับ **HIV ไม่ได้ยา CD4 < 100** · ปวดศีรษะ **เป็นสัปดาห์** · papilledema · CN VI palsy (ICP สูง) · ตุ่มบุ๋มที่ผิวหนัง\n→ **cryptococcal meningitis** (*Cryptococcus neoformans*)\n(differential: TB meningitis, neurosyphilis, toxoplasma — แต่ไม่มี focal lesion ใน CT)"},
   {"q": "2. จะส่งตรวจอะไรเพิ่มเพื่อยืนยัน และคาดว่าจะพบอะไร (2 คะแนน)", "a": "- **India ink** — ยีสต์กลมแตกหน่อ **มีแคปซูลใส** บนพื้นดำ\n- **CSF CrAg (และ serum CrAg)** — บวก ไวที่สุด\n- **เพาะเชื้อ CSF/เลือด** บน Sabouraud\n- ขูดตุ่มที่ผิวหนังย้อมดูยีสต์ได้"},
   {"q": "3. จงให้การรักษาด้วยยาต้านเชื้อรา (ระบุชื่อยาและระยะ) (3 คะแนน)", "a": "1. **Induction 2 สัปดาห์**: **amphotericin B** IV (deoxycholate 0.7–1 mg/kg/วัน) **+ flucytosine** 100 mg/kg/วัน กิน\n2. **Consolidation 8 สัปดาห์**: **fluconazole 800 mg/วัน**\n3. **Maintenance**: fluconazole 200 mg/วัน จน CD4 > 100 และ VL ไม่พบนาน ≥ 3–6 เดือน (รวม ≥ 1 ปี)\n- ทางเลือก WHO 2022: liposomal AmB 10 mg/kg ครั้งเดียว + flucytosine + fluconazole 14 วัน\n- **สะกด flucytosine ให้ถูก — ไม่ใช่ fluconazole**"},
   {"q": "4. ผู้ป่วยตามัวและ CN VI palsy จะจัดการความดันในกะโหลกอย่างไร (2 คะแนน)", "a": "- **เจาะหลังระบาย CSF ซ้ำ (therapeutic LP)** ให้ความดันลดลง ~50% หรือ < 20 cmH₂O **ทุกวัน** จนความดันปกติ\n- ความดันสูงต่อเนื่อง → lumbar drain / VP shunt\n- **ไม่ใช้ mannitol, acetazolamide หรือ steroid** ลดความดันในโรคนี้"},
   {"q": "5. ควรเริ่มยาต้านไวรัส HIV เมื่อใด เพราะเหตุใด และต้องให้ยาป้องกันโรคฉวยโอกาสอะไรบ้าง (2 คะแนน)", "a": "- **เลื่อน ART ไป 4–6 สัปดาห์หลังเริ่มยาต้านเชื้อรา** — เริ่มเร็วเพิ่มอัตราตายจาก **IRIS** ในสมอง\n- **co-trimoxazole** ป้องกัน PCP และ toxoplasma (CD4 < 200)\n- CD4 < 50 พิจารณาป้องกัน MAC ถ้ายังเริ่ม ART ไม่ได้ (แนวทางปัจจุบันไม่จำเป็นถ้าเริ่ม ART เร็ว)"},
  ],
  ref=["สไลด์ Microorganism 2026 — ตาราง CSF และ Cryptococcosis", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — Amphotericin B + flucytosine แล้ว fluconazole", "WHO. Guidelines for diagnosing, preventing and managing cryptococcal disease (2022)"],
  nl=["2.3.1-3(7)", "B3.3(2)", "2.3.1(9)", "B3.2.2(1)"], years=[], _kind="meq", _set="id"),
 dict(id="ID-MIC-MEQ-02", part="MEQ", lec="16/11", lecture=LECNAME,
  topic="Strongyloides hyperinfection with gram-negative bacteremia in a patient on corticosteroids",
  vignette="ผู้ป่วยหญิงไทยอายุ 48 ปี อาชีพทำนา จังหวัดขอนแก่น มาด้วยไข้ ไอ เหนื่อย 2 วัน\nPI: 6 สัปดาห์ก่อนได้รับการวินิจฉัย SLE nephritis ได้ prednisolone 60 mg/วัน · 1 สัปดาห์ก่อนปวดท้อง ท้องอืด ถ่ายเหลว · 2 วันก่อนไข้สูง ไอมีเสมหะปนเลือด เหนื่อยมากขึ้น · วันนี้ปวดศีรษะ ซึมลง\nPE: BT 39.2 C · PR 124/min · BP 86/50 mmHg · RR 32/min · SpO₂ 88% (room air) · stiff neck · crepitation ทั้งสองข้าง · ผื่นจ้ำเลือดเป็นแนวรอบสะดือและหน้าท้อง\nLab: WBC 15,800/µL (N 88%, E 1%) · Hb 10.2 g/dL · platelet 140,000/µL · CXR: diffuse bilateral infiltrates\nHemoculture 2/2 ขวด: Gram-negative bacilli\nSputum direct smear: พบตัวอ่อนพยาธิจำนวนมาก",
  questions=[
   {"q": "1. จงให้การวินิจฉัยที่เป็นไปได้มากที่สุด และอธิบายกลไกที่ทำให้เกิดภาวะนี้ (3 คะแนน)", "a": "**Strongyloides stercoralis hyperinfection / disseminated strongyloidiasis** ร่วมกับ **gram-negative bacteremia และ meningitis**\n- พยาธิอยู่ในตัวได้นานจาก **autoinfection** (คนอีสาน ทำนา)\n- **steroid ขนาดสูง** กดภูมิ → rhabditiform เปลี่ยนเป็น filariform ในลำไส้มากขึ้น ไชผ่านผนังลำไส้ ไปปอด (ไอเป็นเลือด ARDS) และอวัยวะอื่น\n- ตัวอ่อน **พาเชื้อแบคทีเรียลำไส้** เข้ากระแสเลือด → GN sepsis, meningitis\n- ผื่นจ้ำเลือดรอบสะดือ = ตัวอ่อนไชในผิวหนัง\n- eosinophil ไม่สูงเพราะ steroid"},
   {"q": "2. จงบอกการรักษาพยาธิ (ชื่อยา ขนาด ระยะเวลา) (2 คะแนน)", "a": "- **ivermectin 200 µg/kg/วัน** กินทุกวัน **จนตรวจเสมหะ/อุจจาระไม่พบตัวอ่อนติดต่อกัน ≥ 2 สัปดาห์**\n- กินไม่ได้/ลำไส้ไม่ดูดซึม → ivermectin ใต้ผิวหนัง (สัตวแพทย์) ตามที่มี\n- albendazole เป็นทางเลือกที่ด้อยกว่า"},
   {"q": "3. จงบอกการรักษาอื่นที่ต้องทำร่วม (3 คะแนน)", "a": "- **ยาปฏิชีวนะคลุม gram-negative และขนาด meningitis** เช่น **ceftriaxone 2 g IV q12h** (หรือ meropenem ตามความเสี่ยงเชื้อดื้อยา)\n- **ลดขนาดยากดภูมิให้น้อยที่สุด** เท่าที่โรค SLE จะยอม\n- **กู้ชีพ septic shock**: สารน้ำ 30 mL/kg · norepinephrine เป้า MAP ≥ 65 · ออกซิเจน/ใส่ท่อช่วยหายใจ\n- แยกเสมหะและอุจจาระ (ตัวอ่อนติดต่อได้)"},
   {"q": "4. ภาวะนี้ป้องกันได้อย่างไรในผู้ป่วยรายต่อไปที่จะได้ steroid ขนาดสูง (2 คะแนน)", "a": "- คนที่มาจาก **พื้นที่ระบาด** ก่อนเริ่ม steroid ขนาดสูง/ยากดภูมิ/ปลูกถ่ายอวัยวะ → **ตรวจ Strongyloides** (serology, อุจจาระด้วย agar plate culture)\n- หรือให้ **ivermectin 200 µg/kg ครั้งเดียว–2 วัน ล่วงหน้า (empirical)** เมื่อรอผลไม่ได้\n- ตรวจ **HTLV-1** ในรายที่เป็นซ้ำ"},
  ],
  ref=["สไลด์ Microorganism 2026 — Quiz 14 และ Nematodes treatment", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — hyperinfection ถามมากที่สุด ยาคือ ivermectin"],
  nl=["2.3.1(12)", "B1.7.2", "2.1.1"], years=[], _kind="meq", _set="id"),
]
osce = [
 dict(id="ID-MIC-OSCE-01", part="OSCE/SAQ", lec="16/11", lecture=LECNAME,
  topic="SAQ – Gram stain station: describe, diagnose, treat (5 slides)",
  station="SAQ (อ่านสไลด์ Gram stain) 5 นาที",
  instruction="สถานีมีสไลด์ 5 ภาพพร้อมประวัติสั้น ๆ ในแต่ละภาพ **จงบรรยายสิ่งที่เห็น ให้การวินิจฉัย และบอกยา** (ดูภาพจริงได้ในหัวข้อ 2–7 ของคาบนี้)\n\n| สไลด์ | ประวัติ | สิ่งที่เห็นในภาพ |\n|---|---|---|\n| A | CSF ชายอายุ 20 ปี ไข้ ซึม 2 วัน มีจ้ำเลือดที่ขา | เชื้อสีชมพูเป็นคู่รูปเมล็ดถั่วภายในเม็ดเลือดขาว |\n| B | Hemoculture ชายใช้ยาเสพติดชนิดฉีด | เชื้อสีม่วงกลมเกาะเป็นกลุ่ม |\n| C | CSF ชายขายเนื้อหมู หูขวาไม่ได้ยิน | เชื้อสีม่วงกลมเป็นคู่และสายสั้น |\n| D | หนองจากมือผู้ป่วยตับแข็ง มีตุ่มพองสีม่วง | เชื้อแท่งสั้นสีชมพูโค้ง |\n| E | เสมหะหญิง SLE ได้ steroid ขนาดสูง | เส้นใยสีม่วงแตกแขนงเป็นลูกปัด ย้อม modified AFB ติดสีแดง |\n\n**เขียนคำตอบทีละสไลด์ 3 ท่อน: บรรยาย · วินิจฉัย · ยา**",
  answer="**เกณฑ์ให้คะแนน (15 คะแนน — สไลด์ละ 3)**\n\n| สไลด์ | บรรยาย (1) | วินิจฉัย (1) | ยา (1) |\n|---|---|---|---|\n| A | Gram-negative **intracellular diplococci** | **meningococcal meningitis/meningococcemia** (*Neisseria meningitidis*) | **ceftriaxone** หรือ **PGS** · prophylaxis ผู้สัมผัส ciprofloxacin ครั้งเดียว |\n| B | Gram-positive cocci **in clusters** | ***Staphylococcus aureus*** bacteremia/**tricuspid IE** | **cloxacillin** (MSSA) · vancomycin ถ้า MRSA |\n| C | Gram-positive cocci **in pairs/short chains** | ***Streptococcus suis*** meningitis + sensorineural hearing loss | **penicillin G** หรือ **ceftriaxone** |\n| D | Gram-negative **curved rods** | ***Vibrio vulnificus*** necrotizing soft tissue infection | **ceftazidime + doxycycline** + debridement |\n| E | GP **beaded branching filaments**, **mAFB บวก** | **nocardiosis** (*Nocardia*) | **co-trimoxazole** + CT สมอง |\n\n**จุดที่ผู้คุมสอบดู** — ตอบ **ชื่อโรคพร้อมเหตุผล** ไม่ใช่ชื่อเชื้อเปล่า ๆ · **ชื่อวิทยาศาสตร์ genus + species ขีดเส้นใต้ สะกดถูก** · **ชื่อยาสะกดถูก** (ขนาดยาไม่ใช่จุดหลัก)",
  ref=["สไลด์ Microorganism 2026 — Quiz 1, 4, 5, 8, 9", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง) — รูปแบบ SAQ บรรยาย/เชื้อ/ยา"],
  nl=["3.1.9", "B1.5.2(5)", "B1.7.2"], years=[], _kind="meq", _set="id"),
 dict(id="ID-MIC-OSCE-02", part="OSCE/SAQ", lec="16/11", lecture=LECNAME,
  topic="SAQ – Parasitology station: malaria smear, eggs, larvae and oocysts",
  station="SAQ (อ่านสไลด์ปรสิต) 5 นาที",
  instruction="สถานีมีสไลด์ปรสิต 5 ภาพ **จงบอกชื่อเชื้อ (สะกดชื่อวิทยาศาสตร์ให้ถูก) ลักษณะที่ใช้วินิจฉัย และยารักษา** (ดูภาพจริงได้ในหัวข้อ 11–14)\n\n| สไลด์ | ประวัติ | สิ่งที่เห็น |\n|---|---|---|\n| A | ไข้หนาวสั่น กลับจากชายแดนไทย–เมียนมา | thin film: RBC ขนาดปกติ ring เล็กหลายวง บางอันชิดขอบเซลล์ |\n| B | ไข้ซ้ำทุก 48 ชม. เคยเป็นมาลาเรียเมื่อ 3 เดือนก่อน | thin film: RBC โตขึ้น มีจุดสีชมพูเต็มเซลล์ |\n| C | ตรวจอุจจาระเด็กนักเรียน | ไข่รูปถังเบียร์ มีจุกใสสองข้าง |\n| D | HIV ท้องเสียเรื้อรัง 2 เดือน | ย้อม modified AFB เห็น oocyst รีใหญ่ ~25 µm |\n| E | ชายกินหอยเชอรี่ดิบ ปวดศีรษะมาก CSF eosinophil 40% | — (ไม่มีภาพ ถามเชื้อและการรักษา) |\n\n**เขียนคำตอบทีละสไลด์**",
  answer="**เกณฑ์ให้คะแนน (10 คะแนน — ข้อละ 2)**\n\n| สไลด์ | เชื้อ + เหตุผล (1) | ยา (1) |\n|---|---|---|\n| A | ***Plasmodium falciparum*** — RBC ปกติ หลาย ring **appliqué/marginal form** double chromatin | **dihydroartemisinin–piperaquine + primaquine ครั้งเดียว** |\n| B | ***Plasmodium vivax*** — RBC โต **Schüffner's dots** · relapse จาก hypnozoite | **chloroquine + primaquine 14 วัน** (ตรวจ G6PD) |\n| C | ***Trichuris trichiura*** — **bipolar plugs** รูปถังเบียร์ | **albendazole** หรือ **mebendazole** |\n| D | ***Cystoisospora belli*** — oocyst รีใหญ่ที่สุด mAFB บวก | **co-trimoxazole** qid 10 วัน → bid 3 สัปดาห์ + ART |\n| E | ***Angiostrongylus cantonensis*** — eosinophilic meningitis หลังกินหอยดิบ | **ประคับประคอง เจาะหลังลดความดัน + prednisolone** (ไม่ให้ยาฆ่าพยาธิ) |\n\n**จุดที่ผู้คุมสอบดู** — แยก **primaquine ครั้งเดียว (PF ฆ่า gametocyte)** กับ **14 วัน (PV ฆ่า hypnozoite)** · ไม่สับสน ***Cryptosporidium*** (เล็ก ~5 µm รักษาด้วย ART) กับ *Cystoisospora* · สะกดชื่อยาให้ถูก",
  ref=["สไลด์ Microorganism 2026 — Quiz 12, 13, Isospora, Eosinophilic meningitis", "บรรยาย 16 พ.ย. 2569 (บันทึกเสียง)"],
  nl=["2.3.1(14)", "3.1.3", "2.3.1(12)", "2.3.1-3(6)", "2.3.1-3(8)"], years=[], _kind="meq", _set="id"),
]
for q in meq + osce:
    for c in q["nl"]:
        if c not in NL: errs.append(f"{q['id']} bad nl {c}")
    for k in list(q.keys()):
        pass

lecture = {
 "lec": "16/11", "date": "จ. 16 พ.ย.",
 "title": "ทบทวน Microorganism — อ่านสไลด์เชื้อ วินิจฉัย และรักษา",
 "subtitle": "โครงคำตอบ บรรยาย-วินิจฉัย-รักษา · Gram stain จัดกลุ่มเชื้อ · meningitis และตาราง CSF · streptococci · S. aureus และยา IE · Listeria · anthrax · Vibrio · ฝีในตับ · Nocardia · botulism · เชื้อราฉวยโอกาส · ตุ่มบุ๋มและ Mpox · NTM และ leprosy · PCP toxo coccidia · ไข่พยาธิ · Strongyloides · cysticercosis · มาลาเรีย",
 "objectives": [
  "ตอบโจทย์ภาพเชื้อแบบ \"บรรยาย วินิจฉัย และรักษา\" ได้ครบสามส่วน และเขียนชื่อวิทยาศาสตร์และชื่อยาได้ถูกต้อง",
  "จัดกลุ่มแบคทีเรียจาก Gram stain (รูปร่าง การเรียงตัว แคปซูล ตำแหน่งในเซลล์ spore) แล้วจับคู่กับโรคและประวัติสัมผัส",
  "แยก bacterial, cryptococcal meningitis และ HSV encephalitis จาก CSF และให้ยา empiric รวมถึงยาป้องกันผู้สัมผัส meningococcus",
  "เลือกยาตามเชื้อของ S. aureus bacteremia และ infective endocarditis",
  "แยกฝีในตับจาก amoeba, Klebsiella และ melioidosis และรักษาได้ถูกยา",
  "แยกเชื้อราฉวยโอกาส (Cryptococcus, Candida, Mucor, Aspergillus, Histoplasma, Talaromyces) จากรูปร่าง และให้สูตรยาที่ถูกต้อง",
  "วินิจฉัยแยกผื่นตุ่มบุ๋มและผื่นทั่วตัว (Mpox, อีสุกอีใส, syphilis ระยะ 2, เชื้อราใน HIV)",
  "วินิจฉัยและรักษา PCP (คำนวณขนาด co-trimoxazole), toxoplasma encephalitis และท้องเสียเรื้อรังจาก coccidia ในผู้ป่วย HIV",
  "แยกไข่และตัวอ่อนพยาธิที่สำคัญ รักษา Strongyloides hyperinfection และ neurocysticercosis ตามระยะ",
  "แยกชนิดเชื้อมาลาเรียจาก thin film และให้ยาตามแนวทางไทย รวมถึงบทบาทของ primaquine",
 ],
 "nlGap": "เกณฑ์ฯ มีรหัสของ meningitis (`นล. 2.3.6(5)`, `B3.2.2(1)`), meningococcal disease (`2.3.1(17)`), systemic mycoses (`2.3.1-3(7)`), PCP (`2.3.1(18)`), OI ใน HIV (`2.3.1-3(6)`), พยาธิลำไส้ (`2.3.1(12)`) และในเนื้อเยื่อ (`2.3.1-3(8)`), malaria (`2.3.1(14)`) และการย้อม Gram/AFB (`3.1.9`) ครบ แต่ **ไม่มีรหัสแยกของ *Vibrio vulnificus*, *S. suis*, Mpox และ NTM** (ใช้ necrotizing fasciitis, meningitis, VZV/rash และ tuberculosis แทน) · **บันทึกเสียงถอดชื่อยาผิดหลายคำ** (เช่น praziquantel, primaquine, tecovirimat) จึงยึดชื่อและขนาดยาตามสไลด์และแนวทางด้านล่าง · ผู้สอนไม่ได้บอกชื่อในบันทึก",
 "guidelines": [
  "**สไลด์ Microorganism 2026** (96 หน้า, Quiz 1–16) — แหล่งหลักของภาพและสูตรยาในคาบนี้",
  "**WHO. Guidelines for diagnosing, preventing and managing cryptococcal disease among adults, adolescents and children living with HIV (2022)** — single high-dose liposomal AmB",
  "**Baddour LM et al. Infective endocarditis in adults. AHA Scientific Statement. Circulation 2015;132:1435–86** — ยาตามเชื้อของ IE",
  "**Panel on Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents with HIV (NIH/CDC/IDSA)** — PCP, toxoplasma, cryptosporidiosis, cystoisosporiasis, MAC",
  "**แนวทางการรักษาโรคมาลาเรียในประเทศไทย (กองโรคติดต่อนำโดยแมลง กรมควบคุมโรค)** — ผู้สอนอ้างฉบับ 2562 (เปลี่ยนสูตร PF) และฉบับล่าสุด 2568",
  "**White AC Jr et al. Diagnosis and treatment of neurocysticercosis: IDSA/ASTMH guidelines. Clin Infect Dis 2018;66:e49–e75** — calcified ไม่ให้ยาฆ่าพยาธิ",
  "**CDC. Mpox clinical treatment guidance** — tecovirimat ในรายรุนแรง/ภูมิคุ้มกันบกพร่อง",
 ],
 "sections": S, "meq": meq, "osce": osce,
}
# ลำดับคีย์ให้ตรงกับคาบอื่น
tmpl_l = ids[3]
lecture = {k: lecture[k] for k in tmpl_l.keys() if k in lecture} | {k: v for k, v in lecture.items() if k not in tmpl_l}
for q in meq: assert set(q) == set(tmpl_meq), set(q) ^ set(tmpl_meq)
for q in osce: assert set(q) == set(tmpl_osce), set(q) ^ set(tmpl_osce)

if errs:
    print("\n".join(errs)); sys.exit(1)

ids = [l for l in ids if l["lec"] != "16/11"] + [lecture]
c = [c for c in index if c["set"] == "id"][0]
c["lectureCount"] = len(ids)
add_intro = " · คาบล่าสุด **ทบทวน Microorganism (จ. 16 พ.ย.)** จากสไลด์ Microorganism 2026 และบันทึกเสียง — ไล่ Quiz 1–16 แบบ \"บรรยาย วินิจฉัย และรักษา\": Gram stain ของเชื้อก่อ meningitis, streptococci, *S. aureus*, *Listeria*, anthrax, *Vibrio*, *Nocardia*, botulism · เชื้อราฉวยโอกาส · Mpox · PCP และ toxoplasma · coccidia · ไข่พยาธิและ *Strongyloides* · มาลาเรีย พร้อมภาพจากสไลด์ให้ลองอ่านก่อนกดดูเฉลย"
add_howto = "\n\n**คาบ Microorganism (16 พ.ย.)** — ทุกภาพ Quiz มีปุ่ม **ดูเฉลย** ลองตอบ 3 ท่อนเองก่อน: **บรรยาย → วินิจฉัย (โรค+เชื้อ+เหตุผล) → ยา** · ผู้สอนเน้น **สะกดชื่อเชื้อ (ขีดเส้นใต้) และชื่อยาให้ถูก** มากกว่าขนาดยา · ยกเว้น **co-trimoxazole ใน PCP (TMP 15 mg/kg/วัน)** ที่ต้องคำนวณได้ · หัวข้อที่ผู้สอนบอกว่า **ออกบ่อย**: สัตว์กัด (Pasteurella/Capnocytophaga) · anthrax (เคยออก) · syphilis ระยะ 2 · HIV diarrhea · **Strongyloides hyperinfection** · cysticercus ที่เจอโดยบังเอิญ · มาลาเรีย PF/PV"
if "Microorganism (จ. 16 พ.ย.)" not in c["intro"]: c["intro"] += add_intro
if "คาบ Microorganism (16 พ.ย.)" not in c["howto"]: c["howto"] += add_howto

os.makedirs(O + "data", exist_ok=True)
json.dump(ids, open(O + "data/id.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
json.dump(index, open(O + "data/index.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
n = sum(len(s["items"]) for s in S)
print("sections", len(S), "mcq", n, "imgs", sum(len(s.get("imgs", {})) for s in S), "lectures", len(ids))
print("answers", [it["answer"] for s in S for it in s["items"]])
