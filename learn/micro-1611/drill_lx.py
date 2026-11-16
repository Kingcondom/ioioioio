# -*- coding: utf-8 -*-
"""ผูกคาบ 16/11 (Microorganism) เข้าแท็บ "เทียบโพยกับบทเรียน" ของ MED421 Prep Drill
ย้ายข้อสอบเก่าจากบทเสริม (gaps) ของชุด ID ที่คาบนี้ครอบคลุมแล้ว เข้าเป็นหัวข้อของคาบ 16/11
แล้วคำนวณตัวเลขสรุปใหม่

ใช้: python3 drill_lx.py <prep-drill.html ที่ดาวน์โหลดมา> <ไฟล์ปลายทาง.html>
รันซ้ำกับไฟล์ที่ใส่แล้วได้ (ถ้ามีคาบ 16/11 อยู่แล้วจะหยุด)
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.insert(0, HERE)
import lec_a, lec_b  # noqa
SECS = lec_a.S

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf8").read().split("\n")
li = next(i for i, L in enumerate(lines) if L.startswith("<script>const LX = "))
L = lines[li]
head, tail = "<script>const LX = ", L[L.rindex("</script>"):]
body = L[len(head):-len(tail)].rstrip()
semi = body.endswith(";")
LX = json.loads(body[:-1] if semi else body)

ID = next(s for s in LX["sys"] if s["set"] == "id")
if any(l["lec"] == "16/11" for l in ID["lectures"]):
    sys.exit("คาบ 16/11 อยู่ใน LX แล้ว")

# หัวข้อ (ลำดับใน SECS) → [(รหัสข้อในโพย, มุมที่ถาม, ป้ายสั้น)]
MAP = {
 2: [("PP34-INF-012", "mx", "GAS แพ้ penicillin → erythromycin"),
     ("ID-OLDP-003", "mx", "diphtheria แพ้ penicillin → erythromycin"),
     ("PP35-INF-058", "mx", "viral pharyngitis → รักษาตามอาการ")],
 3: [("PPNA-INF-125", "mx", "PVE MSSA: cloxacillin + rifampin + gentamicin")],
 5: [("PP30-INF-029", "dx", "ฝีตับในเบาหวาน = Klebsiella"),
     ("ID-OLDP-023", "fact", "ภาวะที่สัมพันธ์กับ Salmonella")],
 6: [("ID-OLDP-006", "interp", "GP beaded branching = Nocardia"),
     ("ID-OLDP-038", "interp", "partially acid-fast = Nocardia"),
     ("ID-OLDP-007", "mx", "Actinomyces → penicillin (โพยตอบ azithromycin)")],
 9: [("PP35-INF-035", "dx", "ตกปลา + ตุ่มม่วงที่มือ = M. marinum"),
     ("PP32-DER-048", "dx", "ตกปลา + ตุ่มม่วงที่มือ = M. marinum")],
 10: [("PP34-INF-019", "interp", "oocyst 4–6 µm = Cryptosporidium"),
      ("PP30-INF-141", "mx", "Cryptosporidium → เริ่ม ART"),
      ("PPSAQ-INF-128", "interp", "oocyst 25 µm = Cystoisospora → Bactrim")],
 13: [("PP30-INF-114", "ix", "ไข้หลังเข้าป่า → thick และ thin film"),
      ("PP33-INF-002", "interp", "RBC โต + Schüffner = P. vivax"),
      ("PP32-INF-050", "interp", "ring หลายวง + gametocyte กล้วย = P. falciparum"),
      ("PP31-INF-034", "mx", "PF → ACT + primaquine ครั้งเดียว"),
      ("PP31-INF-007b", "mx", "PF → ACT + primaquine ครั้งเดียว"),
      ("PP30-INF-117", "mx", "PF ตั้งครรภ์ไตรมาสแรก → quinine + clindamycin"),
      ("PP29-INF-118", "mx", "ป้องกันก่อนเข้าป่า → doxycycline"),
      ("PP31-INF-004", "mx", "ป้องกันก่อนเข้าป่า → doxycycline")],
}
WHY = {
 2: "เจ็บคอมีหนองแต่แพ้ penicillin → erythromycin; ไอ น้ำมูก ไม่มีหนอง → ไม่ให้ยาปฏิชีวนะ; pseudomembrane สีเทา = diphtheria",
 3: "MSSA ลิ้นเทียม = cloxacillin + rifampin ≥ 6 สัปดาห์ + gentamicin 2 สัปดาห์แรก",
 5: "ฝีในตับก้อนเดียวในเบาหวาน (เอเชีย) = Klebsiella",
 6: "ติดทั้ง Gram และ modified AFB = Nocardia; Actinomyces mAFB ลบ — โพยตอบ azithromycin แต่ยาหลักคือ penicillin",
 9: "ตุ่มม่วงแผลตกสะเก็ดที่หลังมือหลังตกปลา = M. marinum (รุ่น 32, 35)",
 10: "แยกด้วยขนาด oocyst ใน modified AFB: 4–6 µm Cryptosporidium (ART) vs 20–30 µm Cystoisospora (Bactrim)",
 13: "มาลาเรียถูกถาม 8 ข้อ รุ่น 29–33: แยก PF/PV จาก smear, ACT + primaquine ครั้งเดียว, ตั้งครรภ์ไตรมาสแรก, doxycycline ป้องกัน",
}
COLD = "ยังไม่มีข้อในโพย — ผู้สอนบอกว่าโจทย์ภาพแบบนี้อาจออกใน SAQ ให้บรรยาย วินิจฉัย และตอบชื่อยา"

# ดึงข้อออกจากบทเสริม
pool = {}
for g in ID["gaps"]:
    for q in g["q"]:
        pool[q["id"]] = (g, q)
moved = set()
secs, th_all, ang = [], [], {}
for i, s in enumerate(SECS):
    qs = []
    for qid, an, sub in MAP.get(i, []):
        g, q = pool[qid]
        q2 = dict(q); q2["an"] = an; q2["sub"] = sub
        qs.append(q2); moved.add(qid)
        ang[an] = ang.get(an, 0) + 1
        if q["t"] not in th_all: th_all.append(q["t"])
    ys = sorted({y for q in qs for y in q["y"]})
    subs = []
    for q in qs:
        if q["sub"] not in subs: subs.append(q["sub"])
    secs.append({"t": s["title"], "n": len(qs), "y": ys, "w": WHY.get(i) if qs else None,
                 "c": None if qs else COLD, "s": subs, "q": qs})
assert len(moved) == sum(len(v) for v in MAP.values())

for g in ID["gaps"]:
    g["q"] = [q for q in g["q"] if q["id"] not in moved]
    g["years"] = sorted({y for q in g["q"] for y in q["y"]})
    g["th"] = [t for t in g["th"] if any(q["t"] == t for q in g["q"])]
    g["traps"] = [t for t in g["traps"] if t["id"] not in moved]
ID["gaps"] = [g for g in ID["gaps"] if g["q"]]
for g in ID["gaps"]:   # ข้อ PVE ย้ายไปคาบ 16/11 แล้ว ชื่อบทเสริมไม่ต้องบอกอีก (เนื้อหาเดิมยังอยู่)
    g["title"] = g["title"].replace("กลไก, spectrum, ผลข้างเคียง และ prosthetic valve endocarditis", "กลไก, spectrum และผลข้างเคียง")

n = len(moved)
ID["lectures"].append({
 "lec": "16/11", "title": "ทบทวน Microorganism — อ่านสไลด์เชื้อ วินิจฉัย และรักษา", "n": n, "angle": ang,
 "pattern": "โพยถามเชื้อจากภาพหรือเบาะแสสั้น ๆ แล้วตามด้วยยา: มาลาเรีย 8 ข้อ (smear PF/PV, ACT + primaquine, ตั้งครรภ์, doxycycline ป้องกัน) รุ่น 29–33, HIV diarrhea แยกขนาด oocyst, Nocardia กับ modified AFB, M. marinum หลังตกปลา และ pharyngitis ที่แพ้ penicillin — ข้อเหล่านี้เดิมอยู่ในบทเสริม ย้ายมาเมื่อเพิ่มคาบ 16 พ.ย.",
 "tip": "ทวนหัวข้อ 14 (มาลาเรีย) ก่อนเพราะออกมากที่สุด แล้วหัวข้อ 11 (oocyst 5 · 8 · 25 µm) และหัวข้อ 7 (Nocardia ติด 2 สี) · ตอบแบบบรรยาย → วินิจฉัย → ยา และสะกดชื่อเชื้อกับชื่อยาให้ถูก",
 "th": th_all, "secs": secs})
ID["n_lec"] += n
ID["n_unc"] -= n

# แก้ข้อความของคาบ 12/11 ที่บอกว่า malaria ยังไม่มีใน learn
l12 = next(l for l in ID["lectures"] if l["lec"] == "12/11")
a = "malaria ถูกถาม 8 ข้อ (smear, ACT, prophylaxis) แต่ไม่มีใน learn"
assert a in l12["pattern"]; l12["pattern"] = l12["pattern"].replace(a, "malaria ถูกถาม 8 ข้อ (smear, ACT, prophylaxis) — ย้ายไปอยู่คาบ 16/11 แล้ว")
a = "เสริม malaria (smear vivax vs falciparum, DHA-piperaquine + primaquine, doxycycline prophylaxis) เอง"
assert a in l12["tip"]; l12["tip"] = l12["tip"].replace(a, "malaria ไปทวนที่คาบ 16/11 (Microorganism)")

# ตัวเลขสรุปทั้งหน้า
st = LX["stats"]
st["cov"] = sum(s["n_lec"] for s in LX["sys"])
st["gap"] = sum(s["n_unc"] for s in LX["sys"])
st["asked"] = sum(1 for s in LX["sys"] for l in s["lectures"] for x in l["secs"] if x["n"])
st["zero"] = sum(1 for s in LX["sys"] for l in s["lectures"] for x in l["secs"] if not x["n"])
tot = {}
for s in LX["sys"]:
    for l in s["lectures"]:
        for k, v in l["angle"].items(): tot[k] = tot.get(k, 0) + v
st["angle"] = {k: tot.get(k, 0) for k in st["angle"]}

f = LX["findings"]
i = next(i for i, x in enumerate(f) if "ข้อในโพยยังไม่มีคาบรองรับ" in x)
old = "<b>216 ข้อในโพยยังไม่มีคาบรองรับ</b> มากสุดคือ Neuro 61 ข้อ, ID 39, Heme 23, Cardio 21 (ความดันโลหิตสูง 13 ข้อ), Derm 17, Chest 16 และ GI 15 ข้อ"
assert f[i].startswith(old), f[i]
f[i] = f[i].replace(old, "<b>%d ข้อในโพยยังไม่มีคาบรองรับ</b> มากสุดคือ Neuro 61 ข้อ, Heme 23, Cardio 21 (ความดันโลหิตสูง 13 ข้อ), Derm 17, Chest 16, GI 15 และ ID %d ข้อ (ID ลดจาก 39 หลังเพิ่มคาบ Microorganism 16 พ.ย.)" % (st["gap"], ID["n_unc"]))

out = json.dumps(LX, ensure_ascii=False).replace("</", "<\\/")
lines[li] = head + out + (";" if semi else "") + tail
open(dst, "w", encoding="utf8").write("\n".join(lines))
print("moved", n, "ID", ID["n_lec"], ID["n_unc"], "stats", st, "gaps left", [g["id"] for g in ID["gaps"]])
