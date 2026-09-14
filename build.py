#!/usr/bin/env python3
"""
build.py — สร้างเว็บทำข้อสอบ + PDF ทุกระบบ จากไฟล์ JSON ใน data/

วิธีใช้
    python3 build.py              # สร้างทุกระบบที่อยู่ใน config.json
    python3 build.py chest        # สร้างเฉพาะบางระบบ
    python3 build.py --no-pdf     # สร้างเฉพาะเว็บ (เร็วกว่ามาก ตอนกำลังเขียนข้อ)

สิ่งที่ทำให้อัตโนมัติ
    1. รวมไฟล์ JSON ของแต่ละระบบ
    2. ตรวจ schema + หาข้อผิดพลาดที่พบบ่อย (id ซ้ำ, ตัวเลือกไม่ครบ 5, lec ไม่มีในปฏิทิน)
    3. สลับตำแหน่งเฉลย (ผู้เขียนข้อเขียน answer: 0 เสมอ) แบบ deterministic ด้วย seed
    4. ฝังข้อมูลลง template.html -> drill.html
    5. เรนเดอร์ PDF ต่อระบบด้วย headless Chromium

เพิ่มระบบใหม่ = เขียนไฟล์ JSON ใน data/ + เพิ่ม block ใน config.json เท่านั้น
"""
import json, os, random, subprocess, sys, glob, collections

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
os.chdir(ROOT)
CFG = json.load(open('config.json', encoding='utf-8'))
NL_PATH = CFG.get('nl_reference_file', 'refs/nl_2567.json')
NL = json.load(open(NL_PATH, encoding='utf-8')) if os.path.exists(NL_PATH) else {'entries': {}}
NL_ENTRIES = NL.get('entries', {})

CHROME_CANDIDATES = sorted(glob.glob('/opt/pw-browsers/chromium*/chrome-linux/chrome')) + [
    '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome',
]


# ---------------------------------------------------------------- helpers
def load_many(paths):
    out = []
    for p in paths:
        if not os.path.exists(p):
            die(f'ไม่พบไฟล์ {p} (ระบุไว้ใน config.json)')
        out += json.load(open(p, encoding='utf-8'))
    return out


def die(msg):
    print('\n  ✗ ' + msg + '\n', file=sys.stderr)
    sys.exit(1)


def warn(msg):
    print('  ! ' + msg)


def group_old(items, lecture_order, seen_lecture_names):
    """คลังข้อสอบเก่ารับได้ 2 แบบ
       (ก) จัดกลุ่มมาแล้ว  [{lec, lecture, count_note, items:[...]}, ...]
       (ข) รายการแบน       [{id, lec, lecture, q, choices, answer, note, src}, ...]  <- แนะนำแบบนี้
    """
    if items and isinstance(items[0], dict) and 'items' in items[0]:
        return items
    by = collections.OrderedDict()
    for it in items:
        by.setdefault(it['lec'], []).append(it)
    order = [l for l in lecture_order if l in by] + [l for l in by if l not in lecture_order]
    groups = []
    for lec in order:
        rows = by[lec]
        groups.append({
            'lec': lec,
            'lecture': rows[0].get('lecture') or seen_lecture_names.get(lec, ''),
            'count_note': 'เรียบเรียงจากโพย MED28–MED35 เป็นตัวเลือก 5 ข้อพร้อมเฉลย — %d ข้อ' % len(rows),
            'items': rows,
        })
    return groups


# ---------------------------------------------------------------- validation
def validate(setkey, mcq, meq, oldgroups, lectures):
    errs, ids = [], collections.Counter()
    flat_old = [it for g in oldgroups for it in g['items']]
    # คลังเก่ามี 2 รูปแบบ: แบบตัวเลือก (มี choices) และแบบข้อความเดิม (part/q/a/src)
    old_choice = [it for it in flat_old if 'choices' in it]
    old_plain  = [it for it in flat_old if 'choices' not in it]

    for it in old_plain:
        missing = [f for f in ('part', 'q', 'a', 'src') if not it.get(f)]
        if missing:
            errs.append(f"ข้อสอบเก่าแบบข้อความขาดฟิลด์ {', '.join(missing)}: {str(it.get('q'))[:60]}")

    for it in mcq + old_choice:
        ids[it.get('id', '(ไม่มี id)')] += 1
        if len(it['choices']) != 5:
            errs.append(f"{it['id']} มี {len(it['choices'])} ตัวเลือก (ต้องเป็น 5)")
        if not isinstance(it.get('answer'), int) or not 0 <= it['answer'] < len(it['choices']):
            errs.append(f"{it['id']} ค่า answer ไม่ถูกต้อง")
        if len(set(it['choices'])) != len(it['choices']):
            errs.append(f"{it['id']} มีตัวเลือกซ้ำกัน")
    for it in meq:
        ids[it.get('id', '(ไม่มี id)')] += 1
        if it.get('part') == 'MEQ' and not it.get('questions'):
            errs.append(f"{it['id']} เป็น MEQ แต่ไม่มี questions")
        if it.get('part') != 'MEQ' and not it.get('answer'):
            errs.append(f"{it['id']} เป็น OSCE/SAQ แต่ไม่มี answer")

    for i, n in ids.items():
        if n > 1:
            errs.append(f"id ซ้ำ: {i} ({n} ครั้ง)")
    for it in mcq + meq + old_choice:
        if it.get('lec') not in lectures:
            errs.append(f"{it.get('id')} อ้าง lec {it.get('lec')} ซึ่งไม่มีใน config.lectures")

    # เตือน (ไม่ใช่ error)
    no_ref = [it['id'] for it in mcq + meq if not it.get('ref')]
    if no_ref:
        warn(f"[{setkey}] ไม่มี ref {len(no_ref)} ข้อ: {', '.join(no_ref[:6])}{' …' if len(no_ref) > 6 else ''}")
    no_pearl = [it['id'] for it in mcq if not it.get('pearl')]
    if no_pearl:
        warn(f"[{setkey}] ไม่มี pearl {len(no_pearl)} ข้อ: {', '.join(no_pearl[:6])}{' …' if len(no_pearl) > 6 else ''}")

    # --- เกณฑ์แพทยสภา (NL) — เตือนอย่างเดียว ไม่หยุด build
    everything = mcq + meq + old_choice
    if NL_ENTRIES:
        no_nl = [it['id'] for it in everything if not it.get('nl')]
        if no_nl:
            warn(f"[{setkey}] ยังไม่ผูกรหัส NL {len(no_nl)} ข้อ: {', '.join(no_nl[:6])}{' …' if len(no_nl) > 6 else ''}")
        bad = sorted({(it['id'], c) for it in everything for c in it.get('nl', []) if c not in NL_ENTRIES})
        if bad:
            warn(f"[{setkey}] รหัส NL ที่ไม่มีในดัชนี {len(bad)} จุด: "
                 + ', '.join(f'{i}:{c}' for i, c in bad[:6]) + (' …' if len(bad) > 6 else ''))

    if errs:
        die(f"ชุด {setkey} มีปัญหา {len(errs)} จุด:\n    - " + '\n    - '.join(errs[:30]))


# ---------------------------------------------------------------- build
def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    do_pdf = '--no-pdf' not in sys.argv

    setcfgs = [s for s in CFG['sets'] if not args or s['key'] in args]
    if not setcfgs:
        die('ไม่พบระบบที่ระบุใน config.json — มีให้เลือก: ' + ', '.join(s['key'] for s in CFG['sets']))

    bank = json.load(open('bank_merged.json', encoding='utf-8')) if os.path.exists('bank_merged.json') else {}
    seed = CFG.get('shuffle_seed', 20260913)

    for s in setcfgs:
        k = s['key']
        mcq = load_many(s.get('mcq', []))
        meq = load_many(s.get('meq', []))
        old_raw = load_many(s.get('old', []))

        names = {}
        for it in mcq + meq:
            names.setdefault(it['lec'], it.get('lecture', ''))
        oldg = group_old(old_raw, s.get('lecture_order', []), names)

        validate(k, mcq, meq, oldg, CFG['lectures'])

        # สลับตำแหน่งเฉลย — เขียนข้อด้วย answer: 0 เสมอ แล้วให้ตรงนี้สลับให้
        # seed แยกต่อระบบ เพื่อให้ build ระบบเดียวหรือทั้งหมดได้ผลเหมือนกันเสมอ
        rng = random.Random('%s:%s' % (seed, k))
        for it in mcq + [x for g in oldg for x in g['items'] if 'choices' in x]:
            ch, correct = it['choices'], it['choices'][it['answer']]
            order = list(range(len(ch))); rng.shuffle(order)
            it['choices'] = [ch[i] for i in order]
            it['answer'] = it['choices'].index(correct)

        bank[k] = {'mcq': mcq, 'meq': meq, 'old': oldg}
        dist = collections.Counter(x['answer'] for x in mcq)
        codes = {c for it in mcq + meq + [x for g in oldg for x in g['items']] for c in it.get('nl', [])}
        print(f"  ✓ {k:8s} MCQ {len(mcq):3d} · MEQ/OSCE {len(meq):2d} · เก่า {sum(len(g['items']) for g in oldg):3d}"
              f"   กระจายเฉลย {dict(sorted(dist.items()))}"
              + (f" · NL {len(codes)} หัวข้อ" if codes else ""))

    # เรียงลำดับ set ตาม config
    bank = {s['key']: bank[s['key']] for s in CFG['sets'] if s['key'] in bank}
    json.dump(bank, open('bank_merged.json', 'w', encoding='utf-8'), ensure_ascii=False)

    # ---- เว็บ
    t = open('template.html', encoding='utf-8').read()
    live = [s for s in CFG['sets'] if s['key'] in bank]
    lec_js = {k: dict(d=v.get('date', ''), w=v.get('week', ''), **({'al': 1} if v.get('al') else {}))
              for k, v in CFG['lectures'].items()}
    sets_js = [dict(k=s['key'], label=s['label']) for s in live]

    def css(sel, key_a, key_s, key_i, indent=''):
        return '\n'.join(
            f"{indent}{sel % s['key']}{{ --accent:{s['accent'][key_a]}; "
            f"--accent-soft:{s['accent'][key_s]}; --accent-ink:{s['accent'][key_i]}; }}"
            for s in live[1:])   # ชุดแรกใช้สีจาก :root เป็นค่าเริ่มต้น

    html = (t.replace('__TITLE__', CFG['site']['title'])
             .replace('__SUBTITLE__', CFG['site']['subtitle'])
             .replace('__SETCSS_LIGHT__',    css(':root[data-set="%s"]', 'light', 'soft', 'ink'))
             .replace('__SETCSS_AUTODARK__', css(':root:not([data-theme="light"])[data-set="%s"]',
                                                 'dark', 'darkSoft', 'darkInk', '  '))
             .replace('__SETCSS_DARK__',     css(':root[data-theme="dark"][data-set="%s"]',
                                                 'dark', 'darkSoft', 'darkInk'))
             .replace('__LEC__',  json.dumps(lec_js, ensure_ascii=False))
             .replace('__SETS__', json.dumps(sets_js, ensure_ascii=False))
             .replace('__NL__',   json.dumps(NL_ENTRIES, ensure_ascii=False))
             .replace('__DATA__', json.dumps(bank, ensure_ascii=False)))
    open('drill.html', 'w', encoding='utf-8').write(html)
    print(f"  ✓ drill.html  {len(html.encode())/1024:.0f} KB")

    if not do_pdf:
        print('  (ข้าม PDF ตาม --no-pdf)')
        return

    # ---- PDF
    subprocess.run([sys.executable, 'render_pdf.py'] + [s['key'] for s in setcfgs], check=True)
    chrome = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not chrome:
        warn('ไม่พบ Chromium — ได้ไฟล์ print_*.html แล้ว เปิดในเบราว์เซอร์แล้วสั่ง Print → Save as PDF ได้เลย')
        return
    for s in setcfgs:
        k = s['key']
        out = os.path.abspath(f'MED421_{k}.pdf')
        subprocess.run([chrome, '--headless', '--disable-gpu', '--no-sandbox',
                        '--no-pdf-header-footer', f'--print-to-pdf={out}',
                        'file://' + os.path.abspath(f'print_{k}.html')],
                       check=True, capture_output=True)
        print(f"  ✓ MED421_{k}.pdf  {os.path.getsize(out)/1024/1024:.1f} MB")


if __name__ == '__main__':
    print('\nMED421 question-bank build\n' + '-' * 52)
    main()
    print('-' * 52 + '\nเสร็จแล้ว — เปิด drill.html ในเบราว์เซอร์ได้เลย\n')
