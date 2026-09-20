#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""map รหัส นล. ให้ครบในคาบใหม่ 4 คาบ + ใส่แนวทางเวชปฏิบัติปัจจุบันสำหรับหัวข้อที่เกณฑ์ฯ ไม่มีรหัสจำเพาะ"""
import json, os

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # โฟลเดอร์ artifact/
NLD = json.load(open(os.path.join(BUILD, "data", "nl.json"), encoding="utf-8"))

# ── รหัส นล. ต่อหัวข้อย่อย (เรียงตามลำดับ section ในแต่ละคาบ) ──────────────
SEC_NL = {
 ("cardio", "24/9"): [
   ["2.3.9(6)", "B7.2.6(2)", "B7.1.1", "B7.1.2(2)"],
   ["2.3.9(6)", "B7.2.6(2)", "2.1.35", "3.1.12", "3.3.23"],
   ["B7.4(1)", "B7.4(2)", "B7.4(3)", "B7.4(8)", "2.3.9(3)", "B7.2.5(6)"],
   ["2.2.1", "B7.2.6(1)", "3.3.13", "B7.3(2)"],
   ["3.1.12", "B7.3(3)", "2.2.1", "2.1.35"],
   ["2.2.1", "B7.2.6(1)", "2.2.3", "B7.2.5(3)"],
   ["2.2.1", "B7.2.6(1)"],
   ["3.3.13", "B7.3(2)", "2.1.35", "2.2.1"],
   ["2.2.1", "B7.2.6(1)", "2.3.9(1)", "B7.2.5(5)"],
   ["2.2.1", "B7.2.6(1)", "2.3.9(1)"],
   ["2.3.9(3)", "2.3.9(4)", "2.3.9(5)", "B7.2.5(1)", "B7.2.5(2)", "B7.2.5(6)", "B7.3(1)", "B7.4(8)"],
 ],
 ("neuro", "23/9"): [
   ["2.3.6", "2.2.17"],
   ["2.3.6", "2.1.5", "2.1.4"],
   ["2.3.6"], ["2.3.6", "2.1.22"], ["2.3.6"], ["2.3.6"], ["2.3.6"],
   ["2.3.6"], ["2.3.6", "3.3.20"], ["2.3.6"], ["2.3.6"], ["2.3.6"],
 ],
 ("neuro", "15/10"): [
   ["2.3.6", "2.3.1"],
   ["2.3.6", "2.1.1", "3.3.20"],
   ["2.3.6", "3.1.7", "3.1.9"],
   ["2.3.6", "2.3.1", "2.1.1"],
   ["2.3.6", "2.3.4(20)", "3.1.9"],
   ["2.3.6", "2.3.1"],
   ["2.3.6", "3.3.20", "2.3.1"],
   ["2.3.6", "2.3.1"],
   ["2.3.13", "B5.2.2-3(3b)", "2.1.22", "2.1.45"],
 ],
 ("neuro", "9/10"): [
   ["2.3.6", "3.1.7"],
   ["2.3.6", "3.1.7", "3.3.20"],
   ["2.3.6", "3.1.7"],
   ["2.3.6", "3.1.7", "3.1.9"],
   ["2.3.6"], ["2.3.6"],
 ],
}

# ── แนวทางเวชปฏิบัติปัจจุบัน + คำอธิบายช่องว่างของเกณฑ์ฯ ──────────────────
GL = {
 ("cardio", "24/9"): (
   "เกณฑ์ฯ มีรหัสครอบคลุมหัวข้อนี้ครบถ้วน เนื้อหาในคาบอิงแนวทางฉบับล่าสุดที่ใช้อยู่จริงดังนี้",
   ["**2023 ESC Guidelines for the management of acute coronary syndromes** — รวม STEMI และ NSTE-ACS เข้าเป็นฉบับเดียว (ฉบับที่สไลด์อ้างคือ STEMI 2017 และ NSTE-ACS 2020 ซึ่งยังใช้หลักการเดียวกัน)",
    "**2024 ESC Guidelines for the management of chronic coronary syndromes** (ปรับปรุงจากฉบับ 2019 ที่สไลด์ใช้)",
    "**Fourth Universal Definition of Myocardial Infarction (2018)** — นิยาม myocardial injury เทียบกับ infarction",
    "**2019 ESC/EAS Guidelines for the management of dyslipidaemias** — เป้าหมาย LDL ในผู้ป่วยความเสี่ยงสูงมาก",
    "แนวทางเวชปฏิบัติในการดูแลผู้ป่วยโรคหัวใจขาดเลือดในประเทศไทย — สมาคมแพทย์โรคหัวใจแห่งประเทศไทยฯ"]),
 ("neuro", "23/9"): (
   "**เกณฑ์ฯ ไม่มีรหัสจำเพาะสำหรับโรคลมชัก** มีเพียงรหัสหมวดใหญ่ `นล. 2.3.6 โรคระบบประสาท` เนื้อหาคาบนี้จึงสร้างจากแนวทางสากลฉบับปัจจุบันเป็นหลัก",
   ["**ILAE 2025 — Updated classification of epileptic seizures** (Beniczky S, et al. Epilepsia 2025) — การจำแนกชนิดการชักที่ใช้ในคาบนี้",
    "**ILAE 2022 — Classification and definition of epilepsy syndromes** ชุด 3 ฉบับ: วัยทารก (Epilepsia 2022;63:1349-1397), วัยเด็ก (63:1398-1442) และอายุที่หลากหลาย (63:1443-1474)",
    "**ILAE 2014 — A practical clinical definition of epilepsy** — เกณฑ์วินิจฉัยสามข้อ",
    "**NICE NG217 (2022) — Epilepsies in children, young people and adults** — การเลือกยากันชัก",
    "**ILAE 2013 — Evidence-based guideline: antiepileptic drug efficacy as initial monotherapy** (Glauser T, et al.) — ระดับหลักฐาน A–D ที่ใช้ในตารางเลือกยา"]),
 ("neuro", "15/10"): (
   "**เกณฑ์ฯ ไม่มีรหัสจำเพาะสำหรับ meningitis, encephalitis หรือ brain abscess** มีเพียงรหัสหมวดใหญ่ `นล. 2.3.6` และรหัสด้านการตรวจ (`3.1.7`, `3.1.9`) เนื้อหาคาบนี้จึงอิงแนวทางสากลปัจจุบัน",
   ["**ESCMID 2016 — Guideline on the diagnosis and treatment of acute bacterial meningitis**",
    "**IDSA 2017 — Practice Guidelines for Healthcare-Associated Ventriculitis and Meningitis**",
    "**IDSA 2008 — Management of Encephalitis** และ Continuum (Minneap Minn) 2021;27(4) Neuroinfectious Disease",
    "**IDSA 2010 / WHO 2022 — Cryptococcal disease**: induction ด้วย amphotericin B ร่วมกับ flucytosine หรือ fluconazole และการระบายความดันในกะโหลก",
    "**WHO 2022 — Consolidated guidelines on drug-resistant tuberculosis treatment** และแนวทางวัณโรคของประเทศไทย — สูตร 2 IRZE / 10 IR สำหรับ TB meningitis",
    "**IDSA 2015 — Native Vertebral Osteomyelitis** — spondylodiscitis และ spinal epidural abscess"]),
 ("neuro", "9/10"): (
   "**เกณฑ์ฯ ไม่มีรหัสจำเพาะสำหรับหัตถการเจาะหลังหรือการตรวจตา** รหัสที่ใกล้เคียงที่สุดคือ `นล. 3.1.7 Body fluid analysis (CSF, pleural, synovial)` ซึ่งคาบนี้ครอบคลุมแล้ว ส่วนเทคนิคหัตถการอิงแนวทางปัจจุบัน",
   ["**Engelborghs S, et al. Alzheimer's & Dementia: DADM 2017;8:111-126** — consensus guidelines for lumbar puncture (ฉบับที่สไลด์อ้างโดยตรง)",
    "**AAN 2005 (reaffirmed) — Practice parameter: lumbar puncture** และหลักฐานเรื่องขนาดเข็มกับ atraumatic needle",
    "**Nath S, et al. Lancet 2018;391:1197-1204** — atraumatic เทียบกับ conventional needle ลด post-dural-puncture headache",
    "**AAO Preferred Practice Pattern — Comprehensive Adult Medical Eye Evaluation** — มาตรฐานการวัด visual acuity และการส่องจอประสาทตา",
    "**ICHD-3 (2018)** — เกณฑ์วินิจฉัย post-dural puncture headache"]),
}

changed = 0
for (setname, lec), sec_codes in SEC_NL.items():
    path = os.path.join(BUILD, "data", "%s.json" % setname)
    data = json.load(open(path, encoding="utf-8"))
    L = [x for x in data if x["lec"] == lec]
    assert L, "ไม่พบคาบ %s %s" % (setname, lec)
    L = L[0]
    assert len(sec_codes) == len(L["sections"]), \
        "%s %s: ให้รหัสมา %d ชุด แต่มี %d หัวข้อ" % (setname, lec, len(sec_codes), len(L["sections"]))
    for sc, codes in zip(L["sections"], sec_codes):
        bad = [c for c in codes if c not in NLD]
        assert not bad, "รหัสไม่มีในพจนานุกรม: %r" % bad
        sc["nl"] = codes
        for it in sc.get("items", []):
            it["nl"] = codes            # ข้อสอบใช้รหัสเดียวกับหัวข้อที่สังกัด
    allc = sorted({c for cs in sec_codes for c in cs})
    for k in ("meq", "osce"):
        for x in L.get(k, []):
            x["nl"] = allc
    note, gls = GL[(setname, lec)]
    L["nlGap"] = note
    L["guidelines"] = gls
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("%-7s lec %-6s → นล. %2d รหัส · แนวทาง %d ฉบับ" % (setname, lec, len(allc), len(gls)))
    changed += 1
print("อัปเดต %d คาบ" % changed)
