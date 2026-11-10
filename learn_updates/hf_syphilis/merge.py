"""merge.py <live data dir> <out dir> — add HF to cardio and 10/11 to id, update index.json intros"""
import json, sys, os
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
H = os.path.dirname(os.path.abspath(__file__))
def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:60]); return s.replace(a, b)
def put(setname, lec):
    d = json.load(open(os.path.join(src, setname + ".json"), encoding="utf-8"))
    d = [l for l in d if l["lec"] != lec["lec"]] + [lec]
    json.dump(d, open(os.path.join(out, setname + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
    return len(d)
nc = put("cardio", json.load(open(os.path.join(H, "cardio_hf.json"), encoding="utf-8")))
ni = put("id", json.load(open(os.path.join(H, "id_gus.json"), encoding="utf-8")))
idx = json.load(open(os.path.join(src, "index.json"), encoding="utf-8"))
for c in idx:
    if c["set"] == "cardio" and "คาบ HF" not in c["intro"]:
        c["lectureCount"] = nc
        c["intro"] = rep(c["intro"], "หกคาบของชุด Cardio", "เจ็ดคาบของชุด Cardio")
        c["intro"] = rep(c["intro"], "· และคาบ 36 Basic ECG", "· คาบ 36 Basic ECG")
        c["intro"] = rep(c["intro"], "(อ่าน ECG 5 ขั้น พร้อมภาพ ECG บนกระดาษกราฟ)",
            "(อ่าน ECG 5 ขั้น พร้อมภาพ ECG บนกระดาษกราฟ) · และคาบ HF Heart failure ของ อ.Chatchai Pitakrattanachai (สไลด์ พ.ย. 2569) ตั้งแต่นิยาม กลไก การวินิจฉัย ถึงสี่เสาหลักของยาและ decompensated HF ที่อัปเดตตาม **2026 ESC HF guideline**")
        c["howto"] = c.get("howto", "") + ("\n\n**คาบ HF** — สไลด์ของอาจารย์ครอบคลุมนิยามถึงระบาดวิทยา (หัวข้อ 1–9) ส่วนการรักษา (หัวข้อ 10–12) เสริมจากแนวทางปัจจุบัน · "
            "กล่อง **อัปเดตแนวทาง ·** บอกจุดที่ ESC 2026 เปลี่ยน เช่น **เหลือสองกลุ่ม HFrEF < 50% กับ HFpEF ≥ 50%** · ระยะ A–D · MRA Class I ทุกช่วง LVEF · ยึด **warm/cold · wet/dry** เป็นแกนของ decompensated HF")
    if c["set"] == "id" and "10 พ.ย." not in c["intro"]:
        c["lectureCount"] = ni
        c["intro"] = c["intro"].rstrip() + (" · คาบล่าสุด **Genital ulcer และ syphilis (อ. 10 พ.ย.)** เรียบเรียงจากบันทึกเสียงบรรยาย — แยกแผลที่อวัยวะเพศ 5 โรค · "
            "herpes · chancroid · donovanosis · LGV · ระยะของซิฟิลิส · การแปลผล serology (traditional กับ reverse algorithm) · neurosyphilis · ยาตามระยะ · หญิงตั้งครรภ์และ congenital syphilis ตรวจทานกับ CDC 2021/2024 WHO และคู่มือกรมควบคุมโรค")
        c["howto"] = c.get("howto", "") + ("\n\n**คาบ syphilis** — อาจารย์เน้นว่า **ข้อสอบถามชื่อยาและขนาด** · \"หญิงตั้งครรภ์ VDRL บวก ทำอย่างไร\" · VDRL ผลบวกลวง · และ **ใช้ non-treponemal titre ติดตามการรักษา** · "
            "กล่อง **อัปเดตแนวทาง ·** บอกจุดที่แนวทางปัจจุบันต่างจากที่พูดในคาบ")
json.dump(idx, open(os.path.join(out, "index.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("cardio lectures", nc, "| id lectures", ni)
