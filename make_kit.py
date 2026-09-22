#!/usr/bin/env python3
"""
make_kit.py — แพ็กชุดไฟล์สำหรับยกไปทำงานต่อในแชทใหม่ -> med421-kit.zip

    python3 make_kit.py            # เอาไฟล์ครบ (รวม export/*.md)
    python3 make_kit.py --lean     # ไม่เอา export/*.md และ bank_merged.json (ไฟล์เล็กลงมาก)

สิ่งที่ใส่ไปให้: สเปก · พรอมป์ · โค้ด build ทั้งหมด · เทมเพลต · ข้อสอบใน data/ ·
บทเรียนใน learn/ · ดัชนีเกณฑ์แพทยสภา refs/ · README_KIT.md ที่สรุปสถานะล่าสุดให้อัตโนมัติ
ไม่ใส่ไฟล์ที่ build เองได้ (drill.html, learn.html, print_*.html, MED421_*.pdf)
"""
import json, os, sys, zipfile, datetime

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
os.chdir(ROOT)
LEAN = '--lean' in sys.argv
OUT = 'med421-kit.zip'

FILES = ['SPEC.md', 'PROMPT.md', 'config.json', 'build.py', 'build_learn.py', 'render_pdf.py',
         'check_numbers.py', 'export_text.py', 'make_kit.py', 'template.html', 'learn_template.html']
DIRS = ['data', 'learn', 'refs']
if not LEAN:
    FILES.append('bank_merged.json')
    DIRS.append('export')


def readme():
    cfg = json.load(open('config.json', encoding='utf-8'))
    bank = json.load(open('bank_merged.json', encoding='utf-8')) if os.path.exists('bank_merged.json') else {}
    lines = ['# MED421 kit — อ่านไฟล์นี้ก่อน', '',
             'แพ็กเมื่อ %s' % datetime.date.today().isoformat(), '',
             'ชุดนี้ทำงานต่อได้ทันทีโดยไม่ต้องมีไฟล์อื่น — **อ่าน `SPEC.md` ก่อนเริ่มเสมอ** '
             'แล้วดูพรอมป์สำเร็จรูปใน `PROMPT.md`', '',
             '## คลังข้อสอบ (`data/` → build.py → drill.html + PDF)', '',
             '| ชุด | MCQ ใหม่ | MEQ/OSCE | คลังข้อสอบเก่า |', '|---|---|---|---|']
    for k, s in bank.items():
        lines.append('| %s | %d | %d | %d |' % (k, len(s.get('mcq', [])), len(s.get('meq', [])),
                                                sum(len(g['items']) for g in s.get('old', []))))
    lines += ['', '## บทเรียน (`learn/` → build_learn.py → learn.html + export/learn_*.md)', '',
              '| ชุด | คาบ | หัวข้อ | ข้อเช็คความเข้าใจ | MEQ / OSCE |', '|---|---|---|---|---|']
    for p in sorted(__import__('glob').glob('learn/*.json')):
        c = json.load(open(p, encoding='utf-8'))
        nq = sum(len(s.get('quiz', [])) + len(s.get('extra', [])) for l in c['lectures'] for s in l['sections'])
        lines.append('| %s | %s | %d | %d | %d / %d |' % (
            c['set'], ' · '.join(l['lec'] for l in c['lectures']),
            sum(len(l['sections']) for l in c['lectures']), nq,
            sum(len(l.get('meq', [])) for l in c['lectures']),
            sum(len(l.get('osce', [])) for l in c['lectures'])))
    lines += ['', '## คำสั่งที่ใช้บ่อย', '', '```bash',
              'python3 build.py --no-pdf        # รวมข้อสอบ -> bank_merged.json + drill.html',
              'python3 build.py air             # เฉพาะชุดเดียว (ใส่ --no-pdf เพื่อข้าม PDF)',
              'python3 build_learn.py           # บทเรียน -> learn.html + export/learn_<ชุด>.md',
              'python3 check_numbers.py         # ตรวจ ABG/ตัวเลขในโจทย์ให้สอดคล้องกัน',
              'python3 make_kit.py              # แพ็กชุดนี้ใหม่',
              '```', '',
              '## สิ่งที่ยังไม่ได้ทำ (งานที่รอทำต่อ)', '',
              '- บทเรียนของ Chest คาบ 17 (เยื่อหุ้มปอด/respiratory failure) · 21 (CXR/โรคจากการทำงาน) · 37 (pneumonia/asthma/COPD) — ข้อสอบมีครบแล้วใน data/',
              '- บทเรียนของ Cardio · Nephro · Mock NL — ยังไม่ได้เริ่ม',
              '- คลังข้อสอบของระบบที่ยังไม่ทำ: Infectious · Neuro · GI · Endocrine · Hemato · Skin · Onco',
              '- วันที่จริงของ lecture AIR (คาบ 08, 23, 33) ใน `config.lectures` ยังเป็น TBD',
              '- ชุด Mock ยังไม่มี `pearl` รายข้อ และผูกรหัส NL ไว้ระดับหมวด', '',
              '## ไฟล์ที่ไม่ได้ใส่มา (สร้างเองได้จากคำสั่งด้านบน)', '',
              '`drill.html` · `learn.html` · `print_*.html` · `MED421_*.pdf`'
              + ('' if not LEAN else ' · `bank_merged.json` · `export/`'), '']
    return '\n'.join(lines)


def main():
    n = 0
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr('README_KIT.md', readme()); n += 1
        for f in FILES:
            if os.path.exists(f):
                z.write(f); n += 1
        for d in DIRS:
            for root, _, files in os.walk(d):
                for f in sorted(files):
                    if f.endswith(('.json', '.md')):
                        z.write(os.path.join(root, f)); n += 1
    print('  ✓ %s  %d ไฟล์  %.1f MB' % (OUT, n, os.path.getsize(OUT) / 1024 / 1024))


if __name__ == '__main__':
    main()
