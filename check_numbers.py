#!/usr/bin/env python3
"""ตรวจความสอดคล้องของตัวเลขในข้อสอบ (ABG / anion gap / Winter's formula).

ใช้:  python3 check_numbers.py [system ...]
ออก exit code 1 ถ้าพบข้อที่ตัวเลขขัดกันเอง
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PH_TOL = 0.03          # ยอมรับความคลาดเคลื่อน pH จาก Henderson-Hasselbalch
WINTER_TOL = 3.0       # mmHg นอกช่วง Winter's ที่ยังไม่ถือว่าผิด (เผื่อ mixed disorder ที่ตั้งใจ)


def hh_ph(hco3, paco2):
    """Henderson-Hasselbalch: pH = 6.1 + log10(HCO3 / (0.03 x PaCO2))"""
    return 6.1 + math.log10(hco3 / (0.03 * paco2))


def winters(hco3):
    """คาดการณ์ PaCO2 ใน metabolic acidosis: 1.5 x HCO3 + 8 +/- 2"""
    mid = 1.5 * hco3 + 8
    return mid - 2, mid + 2


def check_item(item):
    abg = item.get("abg")
    if not abg:
        return []
    out = []
    ph, paco2, hco3 = abg.get("ph"), abg.get("paco2"), abg.get("hco3")
    if None in (ph, paco2, hco3):
        out.append((item["id"], "ABG ไม่ครบ (ต้องมี ph, paco2, hco3)"))
        return out

    calc = hh_ph(hco3, paco2)
    if abs(calc - ph) > PH_TOL:
        out.append((item["id"],
                    "pH ไม่สอดคล้อง: ระบุ %.2f แต่ HH คำนวณได้ %.2f "
                    "(PaCO2 %s, HCO3 %s) -> ควรแก้ pH เป็น %.2f"
                    % (ph, calc, paco2, hco3, round(calc, 2))))

    # anion gap + Winter's เมื่อเป็น metabolic acidosis และให้ electrolyte มาครบ
    na, cl = abg.get("na"), abg.get("cl")
    if na is not None and cl is not None:
        ag = na - cl - hco3
        note = "AG = %d" % ag
        if hco3 < 22:
            lo, hi = winters(hco3)
            if not (lo - WINTER_TOL <= paco2 <= hi + WINTER_TOL):
                note += (" ; PaCO2 %s อยู่นอกช่วง Winter's %.0f-%.0f "
                         "(ตั้งใจให้เป็น mixed disorder หรือไม่?)" % (paco2, lo, hi))
        out.append((item["id"], "INFO " + note))
    elif hco3 < 22 and ph < 7.38:
        lo, hi = winters(hco3)
        if not (lo - WINTER_TOL <= paco2 <= hi + WINTER_TOL):
            out.append((item["id"],
                        "INFO PaCO2 %s นอกช่วง Winter's %.0f-%.0f (mixed disorder?)"
                        % (paco2, lo, hi)))
    return out


def main(argv):
    cfg = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    wanted = set(argv[1:])
    errors, infos, n_abg = [], [], 0

    for sysdef in cfg["systems"]:
        if wanted and sysdef["key"] not in wanted:
            continue
        data = json.loads((ROOT / sysdef["file"]).read_text(encoding="utf-8"))
        for item in data["items"]:
            if item.get("abg"):
                n_abg += 1
            for iid, msg in check_item(item):
                (infos if msg.startswith("INFO ") else errors).append((sysdef["key"], iid, msg))

    for key, iid, msg in infos:
        print("  [%s] %s: %s" % (key, iid, msg[5:]))
    for key, iid, msg in errors:
        print("  ERROR [%s] %s: %s" % (key, iid, msg))

    print("\nตรวจ ABG %d ข้อ — ไม่สอดคล้อง %d ข้อ" % (n_abg, len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
