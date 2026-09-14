#!/usr/bin/env python3
"""
check_numbers.py — ไล่ตรวจตัวเลข ABG ทุกข้อใน data/ ว่าสอดคล้องกันเองหรือไม่

หาข้อความรูปแบบ  pH 7.28 ... PaCO2 68 ... HCO3 31  ในโจทย์/คำอธิบาย
แล้วตรวจด้วย Henderson–Hasselbalch:  pH = 6.1 + log( HCO3 / (0.03 * PaCO2) )
พร้อมรายงานการชดเชยตาม Winter's formula และการชดเชยของ respiratory acidosis

ใช้: python3 check_numbers.py            # ตรวจทุกไฟล์ใน data/
     python3 check_numbers.py chest      # ตรวจเฉพาะไฟล์ที่ชื่อมีคำว่า chest
"""
import json, re, math, glob, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)) or '.')
TOL = 0.03          # ยอมให้ต่างได้เท่านี้ (การปัดเศษปกติ)

PH   = re.compile(r'pH\s*[:=]?\s*(\d\.\d{2})', re.I)
PCO2 = re.compile(r'Pa?CO2\s*[:=]?\s*(\d{1,3}(?:\.\d)?)', re.I)
HCO3 = re.compile(r'HCO3\s*[:=]?\s*(\d{1,3}(?:\.\d)?)', re.I)


def texts(it):
    """เก็บทุกฟิลด์ที่อาจมีค่า ABG"""
    for k in ('stem', 'q', 'vignette', 'instruction', 'explain', 'note', 'answer'):
        v = it.get(k)
        if isinstance(v, str):
            yield k, v
    for q in it.get('questions', []) or []:
        yield 'questions.q', q.get('q', '')
        yield 'questions.a', q.get('a', '')


def check(field, txt):
    """คืน list ของปัญหาที่เจอในข้อความหนึ่งก้อน"""
    out = []
    # จับเป็นช่วง ๆ ละ 320 ตัวอักษร เพื่อไม่ให้จับ pH ของเคสหนึ่งไปคู่กับ HCO3 ของอีกเคส
    for m in PH.finditer(txt):
        window = txt[m.start():m.start() + 320]
        p = PCO2.search(window)
        h = HCO3.search(window)
        if not (p and h):
            continue
        ph, pco2, hco3 = float(m.group(1)), float(p.group(1)), float(h.group(1))
        if pco2 <= 0 or hco3 <= 0:
            continue
        calc = 6.1 + math.log10(hco3 / (0.03 * pco2))
        if abs(calc - ph) > TOL:
            out.append(f"[{field}] pH {ph} / PaCO2 {pco2} / HCO3 {hco3} → H-H ได้ {calc:.2f} "
                       f"(ต่าง {abs(calc - ph):.2f})")
        else:
            # ตัวเลขสอดคล้องแล้ว — รายงานการชดเชยไว้ให้ตรวจว่าข้อสรุปในเฉลยตรงกันไหม
            notes = []
            if hco3 < 22 and ph < 7.40:
                lo, hi = 1.5 * hco3 + 6, 1.5 * hco3 + 10
                verdict = ('พอดี' if lo <= pco2 <= hi
                           else ('สูงเกิน → resp acidosis ซ้อน' if pco2 > hi
                                 else 'ต่ำเกิน → resp alkalosis ซ้อน'))
                notes.append(f"Winter's คาด {lo:.0f}–{hi:.0f} ได้ {pco2:.0f} = {verdict}")
            if pco2 > 45:
                acute = 24 + (pco2 - 40) / 10 * 1
                chronic = 24 + (pco2 - 40) / 10 * 3.5
                notes.append(f"resp acidosis: HCO3 ถ้า acute ≈ {acute:.0f} / chronic ≈ {chronic:.0f} (จริง {hco3:.0f})")
            if notes:
                out.append(f"  · [{field}] pH {ph} PaCO2 {pco2} HCO3 {hco3} — " + ' ; '.join(notes))
    return out


def main():
    pat = sys.argv[1] if len(sys.argv) > 1 else ''
    files = [f for f in sorted(glob.glob('data/*.json')) if pat in f]
    if not files:
        print('ไม่พบไฟล์ใน data/'); return
    bad = ok = 0
    for f in files:
        rows = json.load(open(f, encoding='utf-8'))
        items = []
        for r in rows:
            items += r['items'] if isinstance(r, dict) and 'items' in r else [r]
        for it in items:
            hits = []
            for field, txt in texts(it):
                hits += check(field, txt)
            errs = [h for h in hits if not h.startswith('  ·')]
            info = [h for h in hits if h.startswith('  ·')]
            if errs:
                bad += 1
                print(f"\n✗ {it.get('id', '?')}  ({os.path.basename(f)})")
                for e in errs:
                    print('   ' + e)
            elif info:
                ok += 1
                print(f"\n✓ {it.get('id', '?')}")
                for i in info:
                    print('  ' + i)
    print(f"\n{'-' * 52}\nตัวเลขไม่สอดคล้อง {bad} ข้อ · ตรวจแล้วผ่าน {ok} ข้อ")
    print('หมายเหตุ: บรรทัด ✓ แสดงผลการชดเชยไว้ให้เทียบกับข้อสรุปในเฉลยด้วยตาอีกครั้ง')


if __name__ == '__main__':
    main()
