"""
render_pdf.py — แปลง bank_merged.json เป็น HTML สำหรับพิมพ์ (ต่อ 1 ระบบ)
ไม่ต้องเรียกตรง ๆ — build.py เรียกให้แล้ว
"""
import json, re, html, sys, os

CFG  = json.load(open('config.json', encoding='utf-8'))
NL_PATH = CFG.get('nl_reference_file', 'refs/nl_2567.json')
NL_ENTRIES = (json.load(open(NL_PATH, encoding='utf-8')).get('entries', {})
              if os.path.exists(NL_PATH) else {})
BANK = json.load(open('bank_merged.json', encoding='utf-8'))

LEC = {k: (v.get('date', ''), v.get('week', ''), v.get('al', 0))
       for k, v in CFG['lectures'].items()}
SETMETA = {s['key']: dict(title=s['label'], thai=s['thai'],
                          accent=s['accent']['light'], soft=s['accent']['soft'],
                          blurb=s.get('blurb', ''))
           for s in CFG['sets']}

E = lambda s: html.escape(str(s))

def inline(t):
    t = E(t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*([^*\n]+)\*', r'<i>\1</i>', t)
    return t

def md(src):
    lines = str(src).split('\n'); out = []; i = 0; para = []
    def flush_para():
        if para:
            out.append('<p>' + '<br>'.join(inline(x) for x in para) + '</p>'); para.clear()
    while i < len(lines):
        L = lines[i]
        if L.strip().startswith('|'):
            flush_para(); rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            sep = len(cells) > 1 and all(re.fullmatch(r':?-{2,}:?', c) for c in cells[1])
            head, body = cells[0], (cells[2:] if sep else cells[1:])
            h = '<table><thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in head) + '</tr></thead><tbody>'
            for r in body:
                h += '<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>'
            out.append(h + '</tbody></table>'); continue
        m_ul = re.match(r'^\s*[-•]\s+(.*)$', L); m_ol = re.match(r'^\s*\d+[.)]\s+(.*)$', L)
        if m_ul or m_ol:
            flush_para(); ordered = bool(m_ol); items = []
            while i < len(lines):
                m = re.match(r'^\s*\d+[.)]\s+(.*)$', lines[i]) if ordered else re.match(r'^\s*[-•]\s+(.*)$', lines[i])
                if not m: break
                txt = m.group(1); i += 1
                while i < len(lines) and re.match(r'^\s{2,}\S', lines[i]) \
                        and not re.match(r'^\s*[-•]\s', lines[i]) and not re.match(r'^\s*\d+[.)]\s', lines[i]) \
                        and not lines[i].strip().startswith('|'):
                    txt += ' ' + lines[i].strip(); i += 1
                items.append('<li>%s</li>' % inline(txt))
            tag = 'ol' if ordered else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join(items), tag)); continue
        if not L.strip():
            flush_para(); i += 1; continue
        para.append(L.strip()); i += 1
    flush_para()
    return ''.join(out)

def short(n): return re.sub(r'\s*\(.*$', '', str(n))
def teacher(n):
    m = re.search(r'\(([^)]*อ\.[^)]*)\)', str(n)); return m.group(1) if m else ''

CSS = """
@page{size:A4;margin:17mm 15mm 16mm 15mm;}
@page:first{margin:0}
*{box-sizing:border-box}
body{font-family:"DejaVu Sans","Loma",sans-serif;font-size:9.6pt;line-height:1.58;color:#14191f;margin:0}
h1,h2,h3,h4{font-family:"DejaVu Serif","Loma",serif;margin:0;font-weight:700}
code{font-family:"DejaVu Sans Mono",monospace;font-size:.85em;background:#eef1f5;padding:0 2px}
.mono{font-family:"DejaVu Sans Mono",monospace}
p{margin:0 0 5pt}
ul,ol{margin:0 0 5pt;padding-left:14pt}
li{margin-bottom:2pt}
table{border-collapse:collapse;width:100%;font-size:8.6pt;margin:0 0 6pt}
th,td{border:.5pt solid #b9c3cd;padding:2.5pt 4pt;text-align:left;vertical-align:top}
th{background:#eef1f5}

/* cover */
.cover{height:297mm;padding:34mm 24mm 22mm;display:flex;flex-direction:column;page-break-after:always;
       border-top:11mm solid var(--ac)}
.cover .kicker{font-family:"DejaVu Sans Mono",monospace;font-size:9pt;letter-spacing:.22em;color:var(--ac);margin-bottom:10mm}
.cover h1{font-size:34pt;line-height:1.06;letter-spacing:-.5pt}
.cover .thai{font-size:15pt;color:#4a5764;margin-top:3mm;font-family:"DejaVu Sans","Loma",sans-serif}
.cover .rule{height:1.6pt;background:#14191f;margin:9mm 0 7mm}
.cover dl{display:grid;grid-template-columns:36mm 1fr;row-gap:2.4mm;font-size:10pt;margin:0}
.cover dt{font-family:"DejaVu Sans Mono",monospace;font-size:8.4pt;letter-spacing:.1em;color:#68747f;padding-top:1.5pt}
.cover dd{margin:0}
.cover .spacer{flex:1}
.cover .note{font-size:8.6pt;color:#5b6773;border-top:.5pt solid #c3ccd6;padding-top:4mm;line-height:1.6}

/* running structure */
h2.sec{font-size:17pt;border-bottom:2pt solid #14191f;padding-bottom:2mm;margin:0 0 5mm;page-break-before:always;page-break-after:avoid}
h2.sec:first-of-type{page-break-before:avoid}
h2.sec .sub{display:block;font-family:"DejaVu Sans","Loma",sans-serif;font-size:9pt;font-weight:400;color:#5b6773;margin-top:1.5mm}
h3.part{font-size:12.5pt;margin:7mm 0 3mm;padding:1.6mm 3mm;background:var(--soft);border-left:2.4pt solid var(--ac);page-break-after:avoid}
h4.lec{font-size:10.5pt;margin:6mm 0 2.5mm;color:var(--ac);page-break-after:avoid;border-bottom:.5pt solid var(--ac);padding-bottom:1mm}

.q{page-break-inside:avoid;margin-bottom:4.5mm}
.qh{font-family:"DejaVu Sans Mono",monospace;font-size:8.2pt;color:#68747f;margin-bottom:1mm}
.qh b{color:var(--ac)}
.qt{font-weight:700;margin:0 0 1.5mm}
.stem{margin:0 0 2mm;text-align:justify}
.ch{margin:0;padding-left:0;list-style:none}
.ch li{margin-bottom:1.2mm;padding-left:7mm;text-indent:-7mm}
.ch .l{font-family:"DejaVu Sans Mono",monospace;font-weight:700;color:#3f4b58}

/* answer key */
.key{page-break-inside:avoid;margin-bottom:5mm;border-top:.5pt solid #c3ccd6;padding-top:2.5mm}
.key .kh{display:flex;gap:3mm;align-items:baseline;margin-bottom:1.5mm}
.key .id{font-family:"DejaVu Sans Mono",monospace;font-size:8.4pt;color:#68747f}
.key .ans{font-family:"DejaVu Sans Mono",monospace;font-weight:700;color:#136c45;font-size:10pt}
.key .tt{font-weight:700}
.key .body{font-size:9.1pt}
.pearl{background:#f7efdf;border-left:2pt solid #8a5608;padding:2mm 3mm;margin:2.5mm 0 0;font-size:9pt}
.pearl b.tag,.refs b.tag{font-family:"DejaVu Sans Mono",monospace;font-size:7.6pt;letter-spacing:.12em;display:block;margin-bottom:1mm}
.pearl b.tag{color:#8a5608}
.refs{margin-top:2.5mm;font-size:8.3pt;color:#5b6773}
.refs b.tag{color:#68747f}
.refs ul{padding-left:12pt}

/* long items */
.vign{background:#f2f5f8;border:.5pt solid #c3ccd6;padding:3mm;white-space:pre-wrap;font-size:9.1pt;margin-bottom:3mm}
.subq{margin-bottom:3.5mm}
.subq .qq{font-weight:700;margin-bottom:1.5mm}
.lines{border-bottom:.4pt solid #c9d2da;height:6.4mm}
.station{font-family:"DejaVu Sans Mono",monospace;font-size:8.4pt;color:#8a5608;margin-bottom:2mm}

/* old bank */
.old{page-break-inside:avoid;display:grid;grid-template-columns:17mm 1fr;gap:3mm;border-top:.4pt dotted #b9c3cd;padding:1.6mm 0}
.old .pt{font-family:"DejaVu Sans Mono",monospace;font-size:7.6pt;letter-spacing:.06em;color:#68747f;padding-top:.8mm}
.old .oq{margin:0 0 .8mm}
.old .oa{margin:0;font-size:9pt;color:#136c45;font-weight:700}
.old .os{margin:.8mm 0 0;font-family:"DejaVu Sans Mono",monospace;font-size:7.6pt;color:#7b8691;line-height:1.45}
.oldq{page-break-inside:avoid;border-top:.4pt dotted #b9c3cd;padding:3mm 0 2mm}
.oldq .ch li.ok{font-weight:700;color:#136c45}
.oldq .oans{margin:1.6mm 0 1mm;font-size:9pt;font-weight:700;color:#136c45}
.oldq .os{margin:1mm 0 0;font-family:"DejaVu Sans Mono",monospace;font-size:7.6pt;color:#7b8691;line-height:1.45}
.lecnote{font-size:8.6pt;color:#5b6773;margin:0 0 2mm}
"""

def nl_html(it):
    """บล็อกอ้างอิงเกณฑ์แพทยสภา พ.ศ. 2567 ต่อข้อ (ว่างถ้าไม่มี)"""
    codes = it.get('nl') or []
    if not codes:
        return ''
    lis = []
    for c in codes:
        e = NL_ENTRIES.get(c)
        if not e:
            lis.append('<li><b>NL %s</b> — ไม่พบในดัชนี</li>' % E(c))
            continue
        grp = ' (กลุ่มที่ %s)' % E(str(e['group'])) if e.get('group') else ''
        lis.append('<li><b>NL %s</b> %s%s — %s%s</li>'
                   % (E(c), E(e.get('title', '')), grp, E(e.get('section', '')),
                      ' หน้า %s' % E(str(e['page'])) if e.get('page') else ''))
    return '<div class="refs"><b class="tag">เกณฑ์แพทยสภา พ.ศ. 2567 (NL)</b><ul>%s</ul></div>' % ''.join(lis)


def render_set(setkey):
    S = SETMETA[setkey]; B = BANK[setkey]
    mcq = B['mcq']; longs = B['meq']; old = B['old']; hot = B.get('hot') or []
    meqs = [x for x in longs if x['part'] == 'MEQ']
    osces = [x for x in longs if x['part'] != 'MEQ']
    nold = sum(len(g['items']) for g in old)
    P = []
    P.append('<style>:root{--ac:%s;--soft:%s}%s</style>' % (S['accent'], S['soft'], CSS))

    # cover
    P.append(f"""<div class="cover">
      <div class="kicker">MED 421 / 422 &nbsp;·&nbsp; INTERNAL MEDICINE</div>
      <h1>{S['title']}<br>Question Set</h1>
      <div class="thai">{S['thai']} — ข้อสอบสร้างใหม่ 50 ข้อ พร้อมคลังข้อสอบเก่า</div>
      <div class="rule"></div>
      <dl>
        <dt>ชุดข้อสอบ</dt><dd>MCQ {len(mcq)} ข้อ · MEQ {len(meqs)} ชุด · OSCE / SAQ {len(osces)} สถานี</dd>
        <dt>คลังข้อสอบเก่า</dt><dd>{nold} ข้อ สกัดจาก MED28 – MED35</dd>
        <dt>แยกตาม</dt><dd>Lecture ของ MED421/422 กลุ่มที่ 3 (C+D) รพ.ราชวิถี</dd>
        <dt>รูปแบบข้อ</dt><dd>โจทย์ภาษาอังกฤษ 5 ตัวเลือก · เฉลยและคำอธิบายกลไกภาษาไทย</dd>
        <dt>หลักการออกข้อ</dt><dd>ทุกตัวเลือกมีเหตุผลรองรับ แต่ถูกเพียงข้อเดียว</dd>
        <dt>ระบบนี้</dt><dd>{S['blurb']}</dd>
      </dl>
      <div class="spacer"></div>
      <div class="note"><b>สารบัญ</b> &nbsp; ส่วนที่ 0 หัวข้อที่ออกสอบบ่อย &nbsp;·&nbsp; ส่วนที่ 1 ข้อสอบใหม่ (โจทย์) &nbsp;·&nbsp; ส่วนที่ 2 เฉลยและคำอธิบาย &nbsp;·&nbsp; ส่วนที่ 3 คลังข้อสอบเก่าแยกตาม lecture<br><br>
      คำเฉลยในโพยเก่าบางข้อไม่ตรงกับแนวทางเวชปฏิบัติปัจจุบัน จุดที่ต่างถูกทำเครื่องหมายไว้ในคำอธิบาย
      เอกสารนี้ใช้ทบทวนประกอบตำราและแนวทางเวชปฏิบัติ ไม่ใช่เอกสารทางการของหลักสูตร</div>
    </div>""")

    # ---- section 0: หัวข้อที่ออกบ่อย
    if hot:
        P.append('<h2 class="sec">ส่วนที่ 0 · หัวข้อที่ออกสอบบ่อย'
                 '<span class="sub">สรุปจากคลังข้อสอบเก่า MED28–MED35 ว่าแต่ละคาบถูกถามซ้ำเรื่องอะไร '
                 'และถามในรูปแบบ MCQ, MEQ หรือ OSCE/SAQ</span></h2>')
        for h in hot:
            d, w, al = LEC.get(h['lec'], ('', '', 0))
            P.append('<h4 class="lec">Lec %s · %s &nbsp;—&nbsp; %s (%s)</h4>'
                     % (E(h['lec']), E(short(h['lecture'])), E(d), E(h.get('level', ''))))
            for title, key in (('MCQ — ถามอะไรบ่อย', 'mcq'),
                               ('MEQ — โจทย์ที่เคยออก', 'meq'),
                               ('OSCE / SAQ — สถานีที่เคยออก', 'osce'),
                               ('ต้องตอบให้ได้', 'must')):
                rows = h.get(key) or []
                if not rows:
                    continue
                P.append('<div class="refs"><b class="tag">%s</b><ul>%s</ul></div>'
                         % (title, ''.join('<li>%s</li>' % inline(x) for x in rows)))
            tail = []
            if h.get('seen'):
                tail.append('เจอในโพย: %s' % E(h['seen']))
            if h.get('ids'):
                tail.append('ข้อตัวอย่างในเล่มนี้: %s' % E(', '.join(h['ids'])))
            if tail:
                P.append('<p class="lecnote">%s</p>' % ' &nbsp;·&nbsp; '.join(tail))

    # ---- section 1: questions
    P.append('<h2 class="sec">ส่วนที่ 1 · ข้อสอบ<span class="sub">ทำโดยยังไม่ดูเฉลย — เฉลยอยู่ในส่วนที่ 2</span></h2>')
    P.append('<h3 class="part">Part 1 · MCQ — เลือกคำตอบที่ถูกที่สุดเพียง 1 ข้อ (%d ข้อ)</h3>' % len(mcq))
    for n, it in enumerate(mcq, 1):
        d, w, al = LEC.get(it['lec'], ('', '', 0))
        P.append('<div class="q"><div class="qh"><b>%d.</b> &nbsp;%s &nbsp;·&nbsp; Lec %s &nbsp;·&nbsp; %s%s</div>'
                 % (n, E(it['id']), E(it['lec']), E(short(it['lecture'])), ' · AL' if al else ''))
        P.append('<p class="qt">%s</p>' % E(it['topic']))
        P.append('<p class="stem">%s</p>' % inline(it['stem']))
        P.append('<ul class="ch">' + ''.join(
            '<li><span class="l">%s.</span> %s</li>' % ('ABCDE'[i], inline(c)) for i, c in enumerate(it['choices'])
        ) + '</ul></div>')

    P.append('<h3 class="part">Part 2 · MEQ — ข้อเขียนเคสต่อเนื่อง (%d ชุด)</h3>' % len(meqs))
    for n, it in enumerate(meqs, 1):
        d, w, al = LEC.get(it['lec'], ('', '', 0))
        P.append('<div class="q"><div class="qh"><b>MEQ %d.</b> &nbsp;%s &nbsp;·&nbsp; Lec %s &nbsp;·&nbsp; %s</div>'
                 % (n, E(it['id']), E(it['lec']), E(short(it['lecture']))))
        P.append('<p class="qt">%s</p>' % E(it['topic']))
        P.append('<div class="vign">%s</div>' % inline(it['vignette']))
        for q in it['questions']:
            P.append('<div class="subq"><div class="qq">%s</div>%s</div>'
                     % (inline(q['q']), '<div class="lines"></div>' * 3))
        P.append('</div>')

    P.append('<h3 class="part">Part 3 · OSCE / SAQ — สถานีละ 5 นาที (%d สถานี)</h3>' % len(osces))
    for n, it in enumerate(osces, 1):
        P.append('<div class="q"><div class="qh"><b>สถานีที่ %d.</b> &nbsp;%s &nbsp;·&nbsp; Lec %s &nbsp;·&nbsp; %s</div>'
                 % (n, E(it['id']), E(it['lec']), E(short(it['lecture']))))
        P.append('<p class="qt">%s</p>' % E(it['topic']))
        if it.get('station'): P.append('<p class="station">%s</p>' % E(it['station']))
        P.append('<div class="vign">%s</div>' % inline(it['instruction']))
        P.append('<div class="lines"></div>' * 4 + '</div>')


    # ---- section 2: answers
    P.append('<h2 class="sec">ส่วนที่ 2 · เฉลยและคำอธิบาย<span class="sub">อธิบายกลไกเป็นแกน พร้อมเหตุผลการตัดตัวเลือกที่เหลือทีละข้อ</span></h2>')
    P.append('<h3 class="part">Part 1 · MCQ — เฉลย</h3>')
    rows = ''.join('<tr><td class="mono">%d</td><td class="mono">%s</td><td class="mono"><b>%s</b></td><td>%s</td></tr>'
                   % (n, E(it['id']), 'ABCDE'[it['answer']], E(it['topic'])) for n, it in enumerate(mcq, 1))
    P.append('<table><thead><tr><th style="width:8mm">ข้อ</th><th style="width:24mm">รหัส</th><th style="width:12mm">ตอบ</th><th>หัวข้อ</th></tr></thead><tbody>%s</tbody></table>' % rows)
    for n, it in enumerate(mcq, 1):
        P.append('<div class="key"><div class="kh"><span class="ans">%d. ตอบ %s</span><span class="tt">%s</span><span class="id">%s · Lec %s</span></div>'
                 % (n, 'ABCDE'[it['answer']], E(it['topic']), E(it['id']), E(it['lec'])))
        P.append('<div class="body">%s</div>' % md(it['explain']))
        if it.get('pearl'):
            P.append('<div class="pearl"><b class="tag">HIGH-YIELD PEARL</b>%s</div>' % md(it['pearl']))
        P.append('<div class="refs"><b class="tag">REF — ข้อสอบเก่าที่เป็นต้นแบบ</b><ul>%s</ul></div>%s</div>'
                 % (''.join('<li>%s</li>' % inline(r) for r in it.get('ref', [])), nl_html(it)))

    P.append('<h3 class="part">Part 2 · MEQ — แนวคำตอบ</h3>')
    for n, it in enumerate(meqs, 1):
        P.append('<div class="key"><div class="kh"><span class="ans">MEQ %d</span><span class="tt">%s</span><span class="id">%s · Lec %s</span></div>'
                 % (n, E(it['topic']), E(it['id']), E(it['lec'])))
        for q in it['questions']:
            P.append('<div class="subq"><div class="qq">%s</div><div class="body">%s</div></div>'
                     % (inline(q['q']), md(q['a'])))
        P.append('<div class="refs"><b class="tag">REF</b><ul>%s</ul></div>%s</div>'
                 % (''.join('<li>%s</li>' % inline(r) for r in it.get('ref', [])), nl_html(it)))

    P.append('<h3 class="part">Part 3 · OSCE / SAQ — แนวคำตอบและเกณฑ์การให้คะแนน</h3>')
    for n, it in enumerate(osces, 1):
        P.append('<div class="key"><div class="kh"><span class="ans">สถานีที่ %d</span><span class="tt">%s</span><span class="id">%s · Lec %s</span></div>'
                 % (n, E(it['topic']), E(it['id']), E(it['lec'])))
        P.append('<div class="body">%s</div>' % md(it['answer']))
        P.append('<div class="refs"><b class="tag">REF</b><ul>%s</ul></div>%s</div>'
                 % (''.join('<li>%s</li>' % inline(r) for r in it.get('ref', [])), nl_html(it)))

    # ---- section 3: old bank
    P.append('<h2 class="sec">ส่วนที่ 3 · คลังข้อสอบเก่า MED28 – MED35<span class="sub">%d ข้อ จัดกลุ่มตาม lecture พร้อมระบุรุ่น ครั้งที่สอบ loop และเลขข้อ</span></h2>' % nold)
    for g in old:
        d, w, al = LEC.get(g['lec'], ('', '', 0))
        P.append('<h4 class="lec">Lec %s · %s &nbsp;—&nbsp; %s (%d ข้อ)</h4>'
                 % (E(g['lec']), E(short(g['lecture'])), E(d), len(g['items'])))
        if g.get('count_note'): P.append('<p class="lecnote">%s</p>' % E(g['count_note']))
        for n, it in enumerate(g['items'], 1):
            if it.get('choices'):
                P.append('<div class="oldq"><div class="qh"><b>%s</b> &nbsp;·&nbsp; Lec %s</div>' % (E(it['id']), E(it.get('lec', g['lec']))))
                P.append('<p class="stem">%s</p>' % inline(it['q']))
                P.append('<ul class="ch">' + ''.join(
                    '<li%s><span class="l">%s.</span> %s</li>'
                    % (' class="ok"' if i == it['answer'] else '', 'ABCDE'[i], inline(c))
                    for i, c in enumerate(it['choices'])) + '</ul>')
                P.append('<p class="oans">ตอบ %s</p>' % 'ABCDE'[it['answer']])
                P.append('<div class="body">%s</div>' % md(it.get('note', '')))
                P.append('<p class="os">%s</p>%s</div>' % (inline(it.get('src', '')), nl_html(it)))
            else:
                P.append('<div class="old"><div class="pt">%s</div><div><p class="oq">%s</p><p class="oa">%s</p><p class="os">%s</p></div></div>'
                         % (E(it['part']), inline(it['q']), inline(it['a']), inline(it['src'])))
    return ''.join(P)


for k in (sys.argv[1:] or list(SETMETA)):
    body = render_set(k)
    doc = '<!doctype html><html lang="th"><head><meta charset="utf-8"><title>MED421 %s Question Set</title></head><body>%s</body></html>' % (SETMETA[k]['title'], body)
    open('print_%s.html' % k, 'w', encoding='utf-8').write(doc)
    print('wrote print_%s.html %.0f KB' % (k, len(doc.encode()) / 1024))
