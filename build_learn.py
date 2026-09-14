#!/usr/bin/env python3
"""
build_learn.py — สร้างเว็บ "เรียนเนื้อหา" (learn.html) จากไฟล์บทเรียนใน learn/ + คลังข้อสอบ bank_merged.json

วิธีใช้
    python3 build_learn.py            # สร้างทุกระบบที่มีไฟล์บทเรียนใน learn/
    python3 build_learn.py air        # สร้างเฉพาะบางระบบ

แนวคิด
    - เนื้อหาบทเรียนอยู่ในไฟล์ learn/<ระบบ>.json อย่างเดียว (markdown ภาษาไทย)
    - ทุกหัวข้อผูก "ข้อสอบเช็คความเข้าใจ" ด้วย id ของข้อในคลัง (bank_merged.json)
      ถ้าหัวข้อไหนไม่มีข้อสอบในคลัง เขียนข้อเองในฟิลด์ "extra" ได้เลย (answer: 0 เสมอ — สคริปต์สลับให้)
    - MEQ / OSCE ของแต่ละคาบผูกด้วย id เช่นกัน
    - ผลลัพธ์เป็นไฟล์เดียว learn.html เปิดออฟไลน์ได้

โครงสร้าง learn/<ระบบ>.json — ดู SPEC.md §8
"""
import json, os, sys, glob, random, collections

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
os.chdir(ROOT)

CFG = json.load(open('config.json', encoding='utf-8'))
NL_PATH = CFG.get('nl_reference_file', 'refs/nl_2567.json')
NL = json.load(open(NL_PATH, encoding='utf-8')) if os.path.exists(NL_PATH) else {'entries': {}}
NL_ENTRIES = NL.get('entries', {})


def die(msg):
    print('\n  ✗ ' + msg + '\n', file=sys.stderr)
    sys.exit(1)


def warn(msg):
    print('  ! ' + msg)


def index_bank(bank):
    """id -> ข้อสอบ (รวมทั้งข้อใหม่ MCQ/MEQ/OSCE และคลังข้อสอบเก่า)"""
    idx = {}
    for setkey, s in bank.items():
        for it in s.get('mcq', []):
            idx[it['id']] = dict(it, _kind='mcq', _set=setkey)
        for it in s.get('meq', []):
            idx[it['id']] = dict(it, _kind='meq', _set=setkey)
        for g in s.get('old', []):
            for it in g.get('items', []):
                if 'choices' in it:
                    idx[it['id']] = dict(it, _kind='old', _set=setkey,
                                         stem=it.get('q', ''), explain=it.get('note', ''))
    return idx


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not os.path.exists('bank_merged.json'):
        die('ไม่พบ bank_merged.json — รัน python3 build.py ก่อน')
    bank = json.load(open('bank_merged.json', encoding='utf-8'))
    idx = index_bank(bank)
    setmeta = {s['key']: s for s in CFG['sets']}

    files = sorted(glob.glob('learn/*.json'))
    if args:
        files = [f for f in files if os.path.splitext(os.path.basename(f))[0] in args]
    if not files:
        die('ไม่พบไฟล์บทเรียนใน learn/ (ที่ตรงกับ: %s)' % (', '.join(args) or 'ทั้งหมด'))

    courses, missing = [], []
    for path in files:
        c = json.load(open(path, encoding='utf-8'))
        key = c.get('set') or os.path.splitext(os.path.basename(path))[0]
        meta = setmeta.get(key) or {}
        rng = random.Random('learn:%s:%s' % (CFG.get('shuffle_seed', 0), key))
        nsec = nquiz = 0

        for lec in c['lectures']:
            lec['date'] = CFG['lectures'].get(lec['lec'], {}).get('date', '')
            for sec in lec['sections']:
                nsec += 1
                items = []
                for qid in sec.get('quiz', []):
                    it = idx.get(qid)
                    if not it:
                        missing.append('%s → %s' % (sec['title'], qid))
                        continue
                    items.append({
                        'id': it['id'], 'kind': it['_kind'],
                        'stem': it.get('stem') or it.get('q', ''),
                        'choices': it['choices'], 'answer': it['answer'],
                        'explain': it.get('explain', ''), 'pearl': it.get('pearl', ''),
                        'topic': it.get('topic', ''), 'src': it.get('src', ''),
                        'ref': it.get('ref', []), 'nl': it.get('nl', []),
                    })
                for n, q in enumerate(sec.get('extra', []), 1):
                    # ข้อที่เขียนเองในบทเรียน — เขียน answer: 0 เสมอ แล้วสลับตรงนี้
                    ch = list(q['choices'])
                    if len(ch) != len(set(ch)):
                        die('%s: ข้อเขียนเองมีตัวเลือกซ้ำกัน' % sec['title'])
                    correct = ch[q.get('answer', 0)]
                    rng.shuffle(ch)
                    items.append({
                        'id': '%s-Q%d' % (sec['id'].upper(), n), 'kind': 'own',
                        'stem': q['stem'], 'choices': ch, 'answer': ch.index(correct),
                        'explain': q.get('explain', ''), 'pearl': q.get('pearl', ''),
                        'topic': sec['title'], 'src': '', 'ref': q.get('ref', []),
                        'nl': q.get('nl', []),
                    })
                if not items:
                    warn('หัวข้อ "%s" ยังไม่มีข้อสอบเช็คความเข้าใจ' % sec['title'])
                sec['items'] = items
                sec.pop('quiz', None); sec.pop('extra', None)
                nquiz += len(items)

            for field in ('meq', 'osce'):
                out = []
                for qid in lec.get(field, []):
                    it = idx.get(qid)
                    if not it:
                        missing.append('%s (%s) → %s' % (lec['title'], field, qid))
                        continue
                    out.append(it)
                lec[field] = out

        c['set'] = key
        c.setdefault('label', meta.get('label', key.upper()))
        c.setdefault('thai', meta.get('thai', ''))
        c['accent'] = meta.get('accent', {})
        courses.append(c)
        print('  ✓ %-6s %d คาบ · %d หัวข้อ · ข้อเช็คความเข้าใจ %d ข้อ · MEQ %d · OSCE/SAQ %d'
              % (key, len(c['lectures']), nsec, nquiz,
                 sum(len(l['meq']) for l in c['lectures']),
                 sum(len(l['osce']) for l in c['lectures'])))

    if missing:
        die('อ้าง id ข้อสอบที่ไม่มีในคลัง %d จุด:\n    - %s' % (len(missing), '\n    - '.join(missing[:20])))

    t = open('learn_template.html', encoding='utf-8').read()
    html = (t.replace('__TITLE__', CFG['site'].get('learn_title', 'MED421 · เรียนเนื้อหา Internal Medicine'))
             .replace('__NL__', json.dumps(NL_ENTRIES, ensure_ascii=False))
             .replace('__COURSES__', json.dumps(courses, ensure_ascii=False)))
    open('learn.html', 'w', encoding='utf-8').write(html)
    print('  ✓ learn.html  %.0f KB' % (len(html.encode()) / 1024))


if __name__ == '__main__':
    print('\nMED421 learn build\n' + '-' * 52)
    main()
    print('-' * 52 + '\nเสร็จแล้ว — เปิด learn.html ในเบราว์เซอร์ได้เลย\n')
