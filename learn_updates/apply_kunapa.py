# -*- coding: utf-8 -*-
"""แทรกหัวข้อจากสไลด์ อ.Kunapa เข้า data/hemonc.json (คาบ 9/11) + อัปเดต meta ของคาบและ data/index.json"""
import json, sys, os, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kunapa_sections as K

D = os.path.join(HERE, "artifact-files/265bd849-ef17-4a75-8de3-8fd750d5011b/data")
hem = json.load(open(os.path.join(D, "hemonc.json"), encoding="utf-8"))
idx = json.load(open(os.path.join(D, "index.json"), encoding="utf-8"))
nl = json.load(open(os.path.join(D, "nl.json"), encoding="utf-8"))

def move(item, to):
    ch = item["choices"]; right = ch.pop(item["answer"]); ch.insert(to, right); item["answer"] = to

secs = copy.deepcopy(K.NEW_SECTIONS)
# กระจายตำแหน่งเฉลยไม่ให้ซ้ำกันทั้งหัวข้อ
move(secs[0]["items"][0], 1)
move(secs[0]["items"][2], 4)
move(secs[4]["items"][2], 0)

# ---------- ตรวจความถูกต้อง
nlkeys = set(nl.keys()) if isinstance(nl, dict) else set(x.get("code") for x in nl)
L = [l for l in hem if l["lec"] == "9/11"][0]
oldids = {s["id"] for s in L["sections"]}
olditems = {i["id"] for l in hem for s in l["sections"] for i in s["items"]}
for s in secs:
    assert s["id"] not in oldids, s["id"]
    for code in s["nl"]:
        assert code in nlkeys, (s["id"], code)
    for it in s["items"]:
        assert it["id"] not in olditems, it["id"]
        assert len(it["choices"]) == 5 and len(set(it["choices"])) == 5, it["id"]
        assert 0 <= it["answer"] < 5
        for code in it["nl"]:
            assert code in nlkeys, (it["id"], code)

# ---------- แทรกหลัง hon-anm-00 (ถ้ามีของเดิมจากรอบก่อน ให้แทนที่)
L["sections"] = [s for s in L["sections"] if not s["id"].startswith("hon-anm-k")]
pos = [i for i, s in enumerate(L["sections"]) if s["id"] == "hon-anm-00"][0] + 1
L["sections"][pos:pos] = secs

# ---------- meta ของคาบ
L["title"] = "Anemia — สไลด์ อ.Kunapa + pathophysiology แบบไล่กลไก 21 ภาวะ"
L["subtitle"] = ("สไลด์คาบจริงของ อ.Kunapa Lam-arunthai (9 พ.ย.): นิยาม · onset · 4 กลไก · reticulocyte 3 แบบ · smear · "
                 "เคส aplastic / IDA / megaloblastic · thalassemia เหล็กเกินและยาขับเหล็ก — ต่อด้วย "
                 "approach to anemia ทั้งระบบ (algorithm ทีละขั้น) · พื้นฐาน MCV + retic · ขาดเหล็ก · ACD/hepcidin · sideroblastic · "
                 "α/β-thalassemia · B12 · folate · aplastic · CKD · ตับ/สุรา/ไทรอยด์ · HS · G6PD · PK · sickle · PNH · warm/cold AIHA · "
                 "DIC · TTP/HUS · เสียเลือดเฉียบพลัน — ไล่จากโมเลกุลถึงผลแล็บและอาการ พร้อมทริคจำสากลและภาพเคลื่อนไหว")
obj_new = "ตอบคำถามตามสไลด์ อ.Kunapa ได้: เกณฑ์ WHO และในหญิงตั้งครรภ์ · ตารางเสียเลือด · RPI/absolute retic/RI · เคส aplastic IDA megaloblastic · เกณฑ์เหล็กเกินและยาขับเหล็ก 3 ตัว"
if obj_new not in L["objectives"]:
    L["objectives"].insert(0, obj_new)
g_new = ("**สไลด์ อ.Kunapa Lam-arunthai — Approach to anemia (คาบ 9 พ.ย. 2569)** — ไฟล์ 'Approach to anemia (2).pdf' ใน Google Drive "
         "พร้อมโน้ตลายมือ (✍️) · ใช้กับหัวข้อ 'สไลด์ อ.Kunapa ①–⑤' · ตารางเหล็กเกิน/ยาขับเหล็กอ้าง Viprakasit et al. Vox Sang 2015 และ TIF guidelines")
if not any("Kunapa" in g for g in L["guidelines"]):
    L["guidelines"].insert(0, g_new)

# ---------- กล่องชี้ทางใน hon-anm-00
s00 = [s for s in L["sections"] if s["id"] == "hon-anm-00"][0]
box = ("> **Kunapa · สไลด์คาบจริง 9 พ.ย.** — หัวข้อถัดไป **สไลด์ อ.Kunapa ①–⑤** สรุปสไลด์ที่ใช้สอนในห้องพร้อมโน้ตลายมือ · "
       "ตัวเลขที่ต่างจากหัวข้อนี้: **onset acute ≤ 2–3 สัปดาห์ · chronic > 3 เดือน** และ **maturation time แบ่งที่ Hct 40/30/20** "
       "· สอบในคาบให้ยึดสไลด์\n\n")
if "Kunapa · สไลด์คาบจริง" not in s00["md"]:
    s00["md"] = box + s00["md"]

# ---------- index.json
c = [x for x in idx if x["set"] == "hemonc"][0]
add = ("คาบ **Anemia (9 พ.ย.)** อัปเดตตาม **สไลด์จริงของ อ.Kunapa Lam-arunthai** — 5 หัวข้อใหม่ (นิยาม/onset/4 กลไก/MCV · "
       "แล็บ reticulocyte 3 แบบและ smear · เคส aplastic anemia · เคส IDA และ megaloblastic · thalassemia เหล็กเกินและยาขับเหล็ก) "
       "พร้อมข้อสอบท้ายหัวข้อ 15 ข้อ · ")
if "อ.Kunapa" not in c["intro"]:
    c["intro"] = add + c["intro"]
c["intro"] = c["intro"].replace("คาบ **Anemia — pathophysiology แบบไล่กลไก 21 ภาวะ (9 พ.ย.)**",
                                "คาบ **Anemia — สไลด์ อ.Kunapa + pathophysiology แบบไล่กลไก 21 ภาวะ (9 พ.ย.)**")
howto_add = "\n\n**คาบ Anemia (9 พ.ย.)** — เริ่มที่หัวข้อ **สไลด์ อ.Kunapa ①–⑤** (ตรงกับที่สอนในห้อง) แล้วค่อยไล่กลไกรายโรคต่อ · กล่องที่ขึ้นต้นว่า **Kunapa ·** คือจุดที่สไลด์ต่างจากเนื้อหาเดิม"
if "สไลด์ อ.Kunapa ①–⑤" not in c["howto"]:
    c["howto"] += howto_add

json.dump(hem, open(os.path.join(D, "hemonc.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(idx, open(os.path.join(D, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("sections now:", [s["id"] for s in L["sections"]][:8], "... total", len(L["sections"]))
print("answers:", [[i["answer"] for i in s["items"]] for s in secs])
