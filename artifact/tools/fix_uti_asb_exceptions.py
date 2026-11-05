# -*- coding: utf-8 -*-
"""แก้ข้อยกเว้นของ ASB ในแผนผัง neph-uti-01 ให้ตรงกับหัวข้อ 13 (สไลด์ให้สามกลุ่ม ไม่ใช่สองกลุ่ม)

แผนผัง "แยกกลุ่มเพื่อเลือกการรักษา" เขียนว่า ASB ไม่รักษา ยกเว้นตั้งครรภ์และก่อนหัตถการ = 2 ข้อ
แต่ตาราง "รักษาเฉพาะใคร" ของหัวข้อ 13 ตามสไลด์มี 3 กลุ่ม คือเพิ่มผู้รับการปลูกถ่ายไต
(พร้อมหมายเหตุว่า IDSA 2019 ไม่แนะนำถ้าผ่าตัดมาเกิน 1 เดือน) ผู้เรียนที่อ่านแผนผังก่อนจะจำได้ 2 ข้อ
ซึ่งขัดกับสไลด์ที่ใช้ออกสอบคาบนี้

รันซ้ำได้ (idempotent) · ใช้:  python3 artifact/tools/fix_uti_asb_exceptions.py [path/to/nephro.json]
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data", "nephro.json")

SVG_OLD = '<tspan x="354" dy="1.25em">ก่อนหัตถการ</tspan></text>'
SVG_NEW = '<tspan x="354" dy="1.25em">ก่อนหัตถการ</tspan><tspan x="354" dy="1.25em">ปลูกถ่ายไต</tspan></text>'

CAP_ANCHOR = "และหาสาเหตุ (หัวข้อ 8)"
CAP_ADD = (" · **ข้อยกเว้นของ ASB มีสามข้อตามสไลด์** คือ ตั้งครรภ์, ก่อนหัตถการที่ทำให้เยื่อบุมีเลือดออก"
           " และผู้รับการปลูกถ่ายไต (ข้อหลังนี้ IDSA 2019 ไม่แนะนำถ้าผ่าตัดมาเกิน 1 เดือน — หัวข้อ 13)")

MNEM_OLD = "(ยกเว้นตั้งครรภ์ · ก่อนหัตถการ)"
MNEM_NEW = "(ยกเว้นตั้งครรภ์ · ก่อนหัตถการ · ปลูกถ่ายไต)"

data = json.load(io.open(PATH, encoding="utf-8"))
lec = [l for l in data if l.get("lec") == "30"]
assert len(lec) == 1, "ไม่พบคาบ 30 ใน %s" % PATH
sec = [s for s in lec[0]["sections"] if s["id"] == "neph-uti-01"]
assert len(sec) == 1, "ไม่พบ neph-uti-01"
sec = sec[0]
done = []

f = sec["figs"]["classify"]
if SVG_NEW in f["svg"]:
    done.append("svg: อยู่แล้ว")
else:
    assert f["svg"].count(SVG_OLD) == 1, "ไม่พบบรรทัด 'ก่อนหัตถการ' ในแผนผัง (นับได้ %d)" % f["svg"].count(SVG_OLD)
    f["svg"] = f["svg"].replace(SVG_OLD, SVG_NEW)
    done.append("svg: เพิ่มบรรทัด 'ปลูกถ่ายไต'")

if CAP_ADD in f["cap"]:
    done.append("cap: อยู่แล้ว")
else:
    assert f["cap"].count(CAP_ANCHOR) == 1, "ไม่พบจุดต่อท้ายคำบรรยาย"
    f["cap"] = f["cap"].replace(CAP_ANCHOR, CAP_ANCHOR + CAP_ADD)
    done.append("cap: เพิ่มข้อยกเว้นสามข้อ")

n = 0
for blk in sec.get("mnem") or []:
    for ln in blk.get("lines") or []:
        if len(ln) > 1 and MNEM_OLD in ln[1]:
            ln[1] = ln[1].replace(MNEM_OLD, MNEM_NEW); n += 1
done.append("mnem: แก้ %d บรรทัด" % n if n else
            ("mnem: อยู่แล้วหรือไม่มีบรรทัดที่ต้องแก้" if sec.get("mnem") else "mnem: ไม่มีในไฟล์นี้"))

# ตรวจกฎของตัวเรนเดอร์: ** ต้องเป็นคู่ และตัวหนาห้ามมี * ข้างใน
assert f["cap"].count("**") % 2 == 0, "** ไม่เป็นคู่"
assert "```" not in f["cap"]

json.dump(data, io.open(PATH, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("%s\n  %s" % (PATH, "\n  ".join(done)))
