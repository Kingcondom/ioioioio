#!/usr/bin/env python3
"""
export_text.py — แปลงคลังข้อสอบทั้งหมดเป็นไฟล์ข้อความ (.md) สำหรับเอาไปใช้ต่อในแชทอื่น

    python3 export_text.py            # ทุกระบบ -> export/<ระบบ>.md + export/ALL.md
    python3 export_text.py air chest  # เฉพาะบางระบบ

อ่านจาก bank_merged.json (หลังสลับตัวเลือกแล้ว) ตัวอักษรเฉลยจึงตรงกับเว็บและ PDF
"""
import json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
os.chdir(ROOT)
CFG = json.load(open('config.json', encoding='utf-8'))
BANK = json.load(open('bank_merged.json', encoding='utf-8'))
NL_PATH = CFG.get('nl_reference_file', 'refs/nl_2567.json')
NL = json.load(open(NL_PATH, encoding='utf-8')).get('entries', {}) if os.path.exists(NL_PATH) else {}
LEC = CFG['lectures']
LETTERS = 'ABCDE'
OUT = 'export'


def nl_lines(it):
    codes = it.get('nl') or []
    if not codes:
        return []
    rows = []
    for c in codes:
        e = NL.get(c)
        if not e:
            rows.append('  - NL %s (ไม่พบในดัชนี)' % c)
            continue
        grp = ' [กลุ่มที่ %s]' % e['group'] if e.get('group') else ''
        rows.append('  - NL %s — %s%s · %s%s'
                    % (c, e.get('title', ''), grp, e.get('section', ''),
                       (' หน้า %s' % e['page']) if e.get('page') else ''))
    return ['NL (เกณฑ์แพทยสภา พ.ศ. 2567):'] + rows


def refs(it):
    r = it.get('ref') or ([it['src']] if it.get('src') else [])
    return ['REF: ' + ' | '.join(r)] if r else []


def mcq_block(it, kind='MCQ'):
    L = ['### [%s] %s' % (it['id'], it.get('topic') or kind),
         'Lecture: %s %s%s' % (it.get('lec', ''), it.get('lecture', ''),
                               (' · ' + LEC.get(it.get('lec'), {}).get('date', '')) if LEC.get(it.get('lec'), {}).get('date') else ''),
         '', 'Q: ' + (it.get('stem') or it.get('q', '')), '']
    L += ['%s. %s' % (LETTERS[i], c) for i, c in enumerate(it['choices'])]
    L += ['', 'ANSWER: %s. %s' % (LETTERS[it['answer']], it['choices'][it['answer']])]
    body = it.get('explain') or it.get('note')
    if body:
        L += ['', 'EXPLAIN:', body]
    if it.get('pearl'):
        L += ['', 'PEARL: ' + it['pearl']]
    L += [''] + refs(it) + nl_lines(it) + ['']
    return L


def long_block(it):
    L = ['### [%s] %s — %s' % (it['id'], it.get('part', ''), it.get('topic', '')),
         'Lecture: %s %s' % (it.get('lec', ''), it.get('lecture', '')), '']
    if it.get('vignette'):
        L += ['VIGNETTE:', it['vignette'], '']
    if it.get('station'):
        L += ['STATION: ' + it['station']]
    if it.get('instruction'):
        L += ['INSTRUCTION:', it['instruction'], '']
    for n, q in enumerate(it.get('questions') or [], 1):
        L += ['Q%d: %s' % (n, q['q']), 'A%d: %s' % (n, q['a']), '']
    if it.get('answer') and isinstance(it['answer'], str):
        L += ['ANSWER / เกณฑ์ให้คะแนน:', it['answer'], '']
    if it.get('pearl'):
        L += ['PEARL: ' + it['pearl'], '']
    L += refs(it) + nl_lines(it) + ['']
    return L


def export_set(key):
    s = next(x for x in CFG['sets'] if x['key'] == key)
    d = BANK[key]
    mcq, meq, old = d['mcq'], d['meq'], d['old']
    n_old = sum(len(g['items']) for g in old)
    L = ['# MED421 · %s (%s)' % (s['label'], s['thai']), '',
         s.get('blurb', ''), '',
         'ข้อใหม่: MCQ %d · MEQ/OSCE %d · คลังข้อสอบเก่า %d ข้อ' % (len(mcq), len(meq), n_old),
         'เฉลยเป็นตัวอักษรตรงกับเว็บและ PDF (ตัวเลือกถูกสลับด้วย seed ของชุดแล้ว)', '',
         '---', '', '## ส่วนที่ 1 · MCQ ข้อใหม่', '']
    for it in mcq:
        L += mcq_block(it)
    if meq:
        L += ['---', '', '## ส่วนที่ 2 · MEQ และ OSCE/SAQ', '']
        for it in meq:
            L += long_block(it)
    if n_old:
        L += ['---', '', '## ส่วนที่ 3 · คลังข้อสอบเก่า MED28–MED35', '']
        for g in old:
            L += ['## Lec %s · %s (%d ข้อ)' % (g['lec'], g.get('lecture', ''), len(g['items'])), '']
            for it in g['items']:
                L += mcq_block(it, 'ข้อสอบเก่า') if it.get('choices') else \
                     ['### [%s] %s' % (it.get('id', '-'), it.get('part', '')),
                      'Q: ' + it.get('q', ''), 'A: ' + it.get('a', '')] + refs(it) + ['']
    return '\n'.join(L)


def main():
    keys = [a for a in sys.argv[1:] if not a.startswith('-')] or [s['key'] for s in CFG['sets']]
    os.makedirs(OUT, exist_ok=True)
    parts = []
    for k in keys:
        if k not in BANK:
            print('  ! ข้าม %s (ยังไม่มีใน bank_merged.json — สั่ง build ก่อน)' % k)
            continue
        text = export_set(k)
        path = os.path.join(OUT, '%s.md' % k)
        open(path, 'w', encoding='utf-8').write(text)
        parts.append(text)
        print('  ✓ %s  %d KB' % (path, len(text.encode()) / 1024))
    if len(parts) > 1:
        allp = os.path.join(OUT, 'ALL.md')
        open(allp, 'w', encoding='utf-8').write(
            ('\n\n' + '=' * 70 + '\n\n').join(parts))
        print('  ✓ %s  %.1f MB' % (allp, os.path.getsize(allp) / 1024 / 1024))


if __name__ == '__main__':
    print('\nexport ข้อสอบเป็นไฟล์ข้อความ\n' + '-' * 40)
    main()
    print('-' * 40 + '\nเสร็จแล้ว — ไฟล์อยู่ในโฟลเดอร์ export/\n')
