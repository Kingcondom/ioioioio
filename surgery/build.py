#!/usr/bin/env python3
"""ศัลย์ masterfucker — รวมไฟล์คาบ parts/<กลุ่ม>_<คาบ>.json → data/<กลุ่ม>.json + data/index.json

python3 build.py            # build ทุกกลุ่ม
ข้อกำหนดของไฟล์คาบอยู่ใน CONTENT_SPEC.md · ทุกข้อ MCQ เขียนคำตอบถูกไว้ choices[0] แล้ว build สลับตำแหน่งให้ (seed ตาม id — build ซ้ำได้ผลเดิม)
"""
import json, glob, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = sys.argv[sys.argv.index("--parts") + 1] if "--parts" in sys.argv else os.path.join(HERE, "parts")
OUT = os.path.join(HERE, "data")

COURSES = [
    {
        "set": "n12", "label": "NL1-2", "thai": "ศัลย์พื้นฐานและโรคที่พบบ่อย",
        "title": "NL1-2 · หลักศัลยศาสตร์และโรคศัลย์ที่พบบ่อย",
        "eyebrow": "นักศึกษาแพทย์ · เตรียมสอบ NL1-2",
        "practice": {"meq": "MEQ", "osce": "OSCE/SAQ", "write": "ฝึกเขียน"},
        "aiRole": "คุณเป็นติวเตอร์ศัลยศาสตร์ของนักศึกษาแพทย์ที่กำลังเตรียมสอบ NL1-2 (ใบประกอบวิชาชีพเวชกรรม ขั้นตอนที่ 1–2) และกำลังอ่านเว็บบทเรียน ศัลย์ masterfucker กลุ่ม NL1-2 อธิบายจากกลไกและพยาธิสรีรวิทยาไปหาอาการ การวินิจฉัย และการรักษาขั้นแรก ใช้ภาษาง่าย",
        "howto": "**วิธีใช้** — อ่านเนื้อหาในหัวข้อให้จบ แล้วทำข้อสอบท้ายหัวข้อ ระบบเฉลยพร้อมเหตุผลทันที · ตอบครบทุกข้อแล้วหัวข้อจะขึ้นว่าเรียนจบ · ข้อที่ตอบผิดรวมอยู่ใน **ทบทวน** · จบคาบแล้วลองเขียนตอบ **MEQ** ของคาบนั้น\n\nกลุ่มนี้เน้นกลไกของโรคศัลย์ อาการแบบฉบับ การวินิจฉัย และการรักษาขั้นแรก ตามแนวข้อสอบ NL1-2",
        "theme": None,
    },
    {
        "set": "n3", "label": "NL3", "thai": "ทักษะทางคลินิก · MEQ · OSCE",
        "title": "NL3 · แนวทางดูแลผู้ป่วยศัลย์ข้างเตียงและสถานีสอบ",
        "eyebrow": "นักศึกษาแพทย์ปี 6 / extern · เตรียมสอบ NL3",
        "practice": {"meq": "MEQ", "osce": "OSCE", "write": "ฝึก OSCE",
                     "osceH": "สถานี OSCE — จับเวลา ทำตามโจทย์ แล้วตรวจตาม checklist",
                     "osceLede": "อ่านโจทย์ กดเริ่มจับเวลา แล้วพูดหรือเขียนขั้นตอนให้ครบเหมือนอยู่หน้าผู้สอบ จากนั้นเปิด checklist ให้คะแนนตัวเองตามจริง"},
        "aiRole": "คุณเป็นอาจารย์ศัลยกรรมที่คุมสอบ NL3 (MEQ, OSCE, long case) ให้นักศึกษาแพทย์ปี 6 ที่กำลังอ่านเว็บบทเรียน ศัลย์ masterfucker กลุ่ม NL3 ตอบเป็นขั้นตอนที่ทำได้จริงข้างเตียงในโรงพยาบาลไทย บอกสิ่งที่ห้ามพลาด (critical fail) และเกณฑ์ส่งต่อ",
        "howto": "**วิธีใช้** — แต่ละคาบเป็นแนวทางดูแลผู้ป่วยหนึ่งกลุ่มอาการ อ่านแล้วทำข้อสอบสั้นท้ายหัวข้อ จากนั้นไปที่ **ฝึก OSCE** กดจับเวลาแล้วทำสถานีให้ครบก่อนเปิด checklist · **MEQ** ไล่เคสทีละขั้นเหมือนสอบจริง\n\nกลุ่มนี้เน้นสิ่งที่ต้องทำได้ทันที: ลำดับการประเมิน คำสั่งการรักษา หัตถการ และการสื่อสารกับผู้ป่วย",
        "theme": {"light": ["#d4f4ea", "#5fd3b0", "#22a884", "#06392b", "#0b6a50"],
                  "dark": ["#12332a", "#3fcfa6", "#6fe3c0", "#d6fff1", "#6fe3c0"]},
    },
    {
        "set": "res", "label": "Resident", "thai": "ศัลยศาสตร์ระดับแพทย์ประจำบ้าน",
        "title": "Resident · ศัลยศาสตร์เชิงลึก การผ่าตัด และหลักฐานอ้างอิง",
        "eyebrow": "แพทย์ประจำบ้าน · ABSITE / สอบบอร์ด",
        "practice": {"meq": "Case", "osce": "Mock oral", "write": "สอบปากเปล่า",
                     "osceH": "Mock oral board — จับเวลา 10 นาที ตอบตามคำถามผู้สอบ แล้วเทียบเกณฑ์",
                     "osceLede": "ให้เพื่อนอ่านคำถามผู้สอบทีละข้อ หรือพูดตอบเองดัง ๆ ภายในเวลา แล้วเปิดเฉลยดูว่าพลาด critical fail ข้อไหน"},
        "aiRole": "คุณเป็นอาจารย์ศัลยแพทย์ที่ติวแพทย์ประจำบ้านศัลยศาสตร์ (ระดับ ABSITE และสอบบอร์ด) ซึ่งกำลังอ่านเว็บบทเรียน ศัลย์ masterfucker กลุ่ม Resident ตอบเชิงลึก: ข้อบ่งชี้และทางเลือกการผ่าตัด classification ภาวะแทรกซ้อน ตัวเลขในแนวทางเวชปฏิบัติ และงานวิจัยสำคัญ ถ้าไม่แน่ใจชื่องานวิจัยหรือตัวเลขให้บอกตรง ๆ",
        "howto": "**วิธีใช้** — แต่ละหัวข้อสรุปเชิงลึกสำหรับแพทย์ประจำบ้าน: classification ทางเลือกการผ่าตัด ภาวะแทรกซ้อน และงานวิจัยสำคัญ · ข้อสอบท้ายหัวข้อเป็นแนว ABSITE · ฝึก **Mock oral** แบบสอบปากเปล่าจับเวลา 10 นาทีต่อสถานี\n\nตัวเลขและแนวทางอิง Schwartz 11e ตรวจกับแนวทางเวชปฏิบัติฉบับล่าสุดของสถาบันก่อนใช้กับผู้ป่วยจริง",
        "theme": {"light": ["#ffe1d6", "#ff9a76", "#f0663c", "#4a1606", "#a33a14"],
                  "dark": ["#3a1c12", "#ff8a63", "#ffab8c", "#ffe6dc", "#ffab8c"]},
    },
]


def shuffle_item(it):
    if it.get("answer") != 0:
        raise SystemExit(f"{it['id']}: answer must be 0 in source (correct choice first)")
    rng = random.Random("sxm:" + it["id"])
    order = list(range(len(it["choices"])))
    rng.shuffle(order)
    it["choices"] = [it["choices"][i] for i in order]
    it["answer"] = order.index(0)


def main():
    os.makedirs(OUT, exist_ok=True)
    index = []
    seen = set()
    for c in COURSES:
        files = sorted(glob.glob(os.path.join(PARTS, c["set"] + "_*.json")))
        lectures = []
        for f in files:
            L = json.load(open(f, encoding="utf-8"))
            L.setdefault("meq", []); L.setdefault("osce", [])
            for s in L["sections"]:
                for k in ("pearls", "items"):
                    s.setdefault(k, [])
                for it in s["items"]:
                    shuffle_item(it)
            for x in [s["id"] for s in L["sections"]] + [i["id"] for s in L["sections"] for i in s["items"]] + \
                     [m["id"] for m in L["meq"]] + [o["id"] for o in L["osce"]]:
                if x in seen:
                    raise SystemExit(f"duplicate id {x} in {f}")
                seen.add(x)
            for m in L["meq"]:
                m.setdefault("lecture", L["title"])
            lectures.append(L)
        lectures.sort(key=lambda l: l["lec"])
        json.dump(lectures, open(os.path.join(OUT, c["set"] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        ns = sum(len(l["sections"]) for l in lectures)
        nq = sum(len(s["items"]) for l in lectures for s in l["sections"])
        nm = sum(len(l["meq"]) for l in lectures)
        no = sum(len(l["osce"]) for l in lectures)
        p = c["practice"]
        meta = {k: v for k, v in c.items() if v is not None}
        meta["intro"] = (f"{c['title'].split(' · ')[1]} — {len(lectures)} คาบ {ns} หัวข้อ ข้อสอบ MCQ {nq} ข้อ "
                         f"{p['meq']} {nm} โจทย์ {p['osce']} {no} สถานี สรุปเป็นภาษาไทยจาก Schwartz's Principles of Surgery 11e")
        meta["file"] = "data/" + c["set"] + ".json"
        meta["lectureCount"] = len(lectures)
        index.append(meta)
        print(f"{c['set']}: {len(lectures)} lectures, {ns} sections, {nq} MCQ, {nm} MEQ, {no} OSCE")
    json.dump(index, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({}, open(os.path.join(OUT, "nl.json"), "w"))


if __name__ == "__main__":
    main()
