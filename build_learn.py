#!/usr/bin/env python3
"""
build_learn.py — สร้างเว็บ "เรียนเนื้อหา" (learn.html) จากไฟล์บทเรียนใน learn/ + คลังข้อสอบ bank_merged.json

วิธีใช้
    python3 build_learn.py            # สร้างทุกระบบที่มีไฟล์บทเรียนใน learn/
    python3 build_learn.py air        # ตรวจเฉพาะระบบที่ระบุ (learn.html ยังรวมทุกระบบเสมอ)

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

    # learn.html รวมทุกระบบไว้ในไฟล์เดียวเสมอ (สลับชุดได้ในหน้าเว็บ)
    # อาร์กิวเมนต์เป็นแค่ตัวกรองว่าจะให้ build หยุดถ้าระบบนั้นมีปัญหา ไม่ได้ตัดระบบอื่นออกจากไฟล์
    files = sorted(glob.glob('learn/*.json'))
    if not files:
        die('ไม่พบไฟล์บทเรียนใน learn/')
    known = [os.path.splitext(os.path.basename(f))[0] for f in files]
    for a in args:
        if a not in known:
            die('ไม่พบไฟล์บทเรียน learn/%s.json — มีให้เลือก: %s' % (a, ', '.join(known)))

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

    # ---- ไฟล์ข้อความของบทเรียน (เอาไปวางในแชทอื่นได้ทั้งไฟล์)
    os.makedirs('export', exist_ok=True)
    for c in courses:
        out = [f"# บทเรียน MED421 · {c['label']} — {c.get('title','')}", '']
        if c.get('intro'):
            out += [c['intro'], '']
        n_sec = sum(len(l['sections']) for l in c['lectures'])
        n_q = sum(len(s['items']) for l in c['lectures'] for s in l['sections'])
        out += [f"{len(c['lectures'])} คาบ · {n_sec} หัวข้อ · ข้อเช็คความเข้าใจ {n_q} ข้อ · "
                f"MEQ {sum(len(l['meq']) for l in c['lectures'])} · "
                f"OSCE/SAQ {sum(len(l['osce']) for l in c['lectures'])}",
                '', '---', '']
        for l in c['lectures']:
            out += [f"## คาบ {l['lec']} · {l['title']}" + (f" ({l['date']})" if l.get('date') else ''), '']
            if l.get('subtitle'):
                out += [l['subtitle'], '']
            if l.get('objectives'):
                out += ['**วัตถุประสงค์**'] + [f'- {o}' for o in l['objectives']] + ['']
            for sec in l['sections']:
                out += [f"### [{sec['id']}] {sec['title']}", '']
                if sec.get('summary'):
                    out += [f"_{sec['summary']}_", '']
                if sec.get('source'):
                    out += [f"ที่มา: {sec['source']}", '']
                if sec.get('nl'):
                    out += ['NL: ' + ' · '.join(
                        f"{code} {NL_ENTRIES.get(code, {}).get('title', '')}".strip() for code in sec['nl']), '']
                out += [sec['md'].strip(), '']
                if sec.get('pearls'):
                    out += ['**จำไปสอบ**'] + [f'- {x}' for x in sec['pearls']] + ['']
                if sec['items']:
                    out += [f"**ข้อสอบเช็คความเข้าใจ ({len(sec['items'])} ข้อ)**", '']
                for it in sec['items']:
                    out += [f"[{it['id']}] {it.get('topic','')}".strip(), '', it['stem'], '']
                    out += [f"{'ABCDE'[i]}. {ch}" for i, ch in enumerate(it['choices'])]
                    out += ['', f"ANSWER: {'ABCDE'[it['answer']]}. {it['choices'][it['answer']]}", '']
                    if it.get('explain'):
                        out += ['EXPLAIN:', it['explain'].strip(), '']
                    if it.get('pearl'):
                        out += [f"PEARL: {it['pearl']}", '']
                    if it.get('src'):
                        out += [f"SRC: {it['src']}", '']
                    if it.get('ref'):
                        out += ['REF: ' + ' | '.join(it['ref']), '']
                    if it.get('nl'):
                        out += ['NL: ' + ' · '.join(
                            f"{code} {NL_ENTRIES.get(code, {}).get('title', '')}".strip() for code in it['nl']), '']
                    out += ['']
            for it in l['meq']:
                out += [f"### [{it['id']}] MEQ — {it.get('topic','')}", '', it.get('vignette', ''), '']
                for q in it.get('questions', []):
                    out += [q['q'], '', 'แนวคำตอบ:', q['a'].strip(), '']
            for it in l['osce']:
                out += [f"### [{it['id']}] {it.get('station','OSCE/SAQ')} — {it.get('topic','')}", '',
                        it.get('instruction', ''), '', 'เฉลยและเกณฑ์ให้คะแนน:', (it.get('answer') or '').strip(), '']
            out += ['---', '']
        path = 'export/learn_%s.md' % c['set']
        open(path, 'w', encoding='utf-8').write('\n'.join(out))
        print('  ✓ %-22s %.0f KB' % (path, len(''.join(out).encode()) / 1024))

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
