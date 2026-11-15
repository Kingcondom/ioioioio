"""ประกอบชุด "แก่นละ 1 ข้อ" + "โจทย์รวบยอด" → prep_data.json, prep.html (หน้าเว็บ) และ print_*.html (สำหรับ PDF)
ใช้: python3 analysis/build_prep.py <scratch_dir>   (ต้องมี bank.json, in2/, out2/)
"""
import json, sys, os, hashlib, random, re, html
ROOT = os.path.dirname(os.path.abspath(__file__)); S = sys.argv[1]
ORDER = ['cardio','nephro','chest','neuro','air','infect','gi','endo','heme','derm','onco']
LABEL = {'cardio':('Cardio','หัวใจและหลอดเลือด'),'nephro':('Nephro','ไต สารน้ำ เกลือแร่'),'chest':('Chest','ระบบหายใจ'),
 'neuro':('Neuro','ระบบประสาท'),'air':('AIR','ภูมิแพ้ ภูมิคุ้มกัน ข้อ'),'infect':('Infect','โรคติดเชื้อ'),'gi':('GI','ทางเดินอาหารและตับ'),
 'endo':('Endo','ต่อมไร้ท่อ'),'heme':('Heme','โลหิตวิทยา'),'derm':('Derm','ผิวหนัง'),'onco':('Onco','มะเร็งวิทยา')}
bank = json.load(open(f'{S}/bank.json'))
items = {i['id']: i for v in bank.values() for g in v.get('old', []) for i in g['items']}
def shuffle(choices, ans, key):
    idx = list(range(len(choices))); random.Random(int(hashlib.md5(key.encode()).hexdigest()[:8], 16)).shuffle(idx)
    return [choices[i] for i in idx], idx.index(ans)
sets = []
for s in ORDER:
    tf, of = f'{S}/in2/{s}_themes.json', f'{S}/out2/{s}.json'
    if not (os.path.exists(tf) and os.path.exists(of)): continue
    T = {t['theme']: t for t in json.load(open(tf))}; O = json.load(open(of))
    one = []
    for o in O['one_per_theme']:
        t = T[o['theme']]; it = items[o['id']]
        others = [{'q': x['q'], 'a': x['answer'], 'years': x['years']} for x in t['items'] if x['id'] != o['id']]
        one.append({'id': it['id'], 'theme': t['theme'], 'years': t['theme_years'], 'n': t['n'], 'q': it['q'],
                    'choices': it['choices'], 'answer': it['answer'], 'note': it.get('note', ''), 'src': it.get('src', ''),
                    'related': o['related'], 'fix': o.get('fix', ''), 'others': others})
    one.sort(key=lambda x: (-len(x['years']), -x['n'], -(max(x['years']) if x['years'] else 0)))
    syn = []
    for q in O['synth']:
        ch, a = shuffle(q['choices'], q.get('answer', 0), q['id'])
        yrs = sorted({y for th in q['covers_themes'] if th in T for y in T[th]['theme_years']})
        syn.append({'id': q['id'], 'title': q['title'], 'q': q['stem'], 'choices': ch, 'answer': a, 'explain': q['explain'],
                    'fullcover': q['fullcover'], 'pearl': q.get('pearl', ''), 'themes': q['covers_themes'],
                    'nl': q.get('covers_nl', []), 'years': yrs})
    sets.append({'key': s, 'label': LABEL[s][0], 'thai': LABEL[s][1], 'one': one, 'synth': syn})
PICMAP = {'PIC35-01':'ECG บอกตำแหน่ง STEMI','PIC35-02':'STEMI reperfusion','PIC35-03':'Bradyarrhythmia','PIC35-20':'UTI: เดาเชื้อจาก gram stain',
 'PIC35-21':'นิ่วไต','PIC35-22':'TB: วินิจฉัย/โปรแกรม','PIC35-23':'CXR lobar pneumonia','PIC35-15':'Anaphylaxis','PIC35-16':'Crystal arthritis',
 'PIC35-18':'Dermatomyositis','PIC35-17':'Septic / gonococcal','PIC35-06':'Scrub typhus','PIC35-07':'Malaria: วินิจฉัย','PIC35-05':'HIV CNS',
 'PIC35-04':'HIV CNS','PIC35-14':'Acute watery diarrhea','PIC35-13':'Thyroid nodule','PIC35-24':'IDA: อาการ','PIC35-12':'Herpesvirus vesicles',
 'PIC35-09':"Wood's lamp",'PIC35-10':'Onychomycosis','PIC35-11':'Herpes zoster','PIC35-08':"Wood's lamp",'PIC35-19':'Lung cancer: paraneoplastic'}
pfix = {}
for f in os.listdir(f'{S}/review') if os.path.isdir(f'{S}/review') else []:
    if f.endswith('_pics_fix.json'):
        for r in json.load(open(f'{S}/review/{f}')): pfix[r['id']] = r.get('fix', '')
pics = []
theme_ix = {x['theme']: x for st in sets for x in st['one']}
for p in json.load(open(f'{ROOT}/prep_src/pics.json')):
    th = next(t for t in theme_ix if t.startswith(PICMAP[p['id']]))
    q = {'id': p['id'], 'set': p['sys'], 'theme': th, 'title': p['topic'], 'img': p['img'], 'years': [int(y) for y in p.get('years', [])],
         'fix': pfix.get(p['id'], ''), 'pearl': p.get('pearl', '')}
    if p.get('choices'):
        q.update(kind='pic', q=p['stem'], choices=p['choices'], answer=p['answer'], explain=p['explain'])
    else:
        q.update(kind='saq', q=p['vignette'], station=p.get('station', ''), parts=p['questions'])
    pics.append(q)
    theme_ix[th].setdefault('pics', []).append({'id': p['id'], 'img': p['img']})
data = {'pics': pics, 'sets': sets, 'n_one': sum(len(x['one']) for x in sets), 'n_syn': sum(len(x['synth']) for x in sets)}
json.dump(data, open(f'{ROOT}/prep_data.json', 'w'), ensure_ascii=False)
tpl = open(f'{ROOT}/prep_template.html').read()
open(f'{ROOT}/prep.html', 'w').write(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')))

# ---------- print HTML ----------
E = lambda t: html.escape(str(t))
def inl(t): return re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?!\*)', r'<i>\1</i>', re.sub(r'\*\*\*?(.+?)\*\*\*?', r'<b>\1</b>', E(t)))
def md(t):
    out, ul = [], False
    for L in str(t).split('\n'):
        L = L.rstrip()
        if re.match(r'^\s*[-*] ', L):
            if not ul: out.append('<ul>'); ul = True
            out.append('<li>' + inl(re.sub(r'^\s*[-*] ', '', L)) + '</li>')
        else:
            if ul: out.append('</ul>'); ul = False
            if L.strip(): out.append('<p>' + inl(L) + '</p>')
    if ul: out.append('</ul>')
    return ''.join(out)
LET = 'ABCDE'
CSS = '''@page{size:A4;margin:14mm 13mm 15mm 13mm}
body{font-family:"IBM Plex Sans Thai","Noto Sans Thai",sans-serif;font-size:10.5pt;line-height:1.6;color:#151a14;margin:0}
h1{font-size:22pt;margin:0 0 4pt}.cover{padding:40mm 10mm 0;page-break-after:always}.cover p{font-size:11pt;color:#3f463c;max-width:150mm}
h2{font-size:16pt;margin:0 0 2pt;padding:6pt 10pt;background:#d5f0a6;border-radius:8pt;page-break-before:always}
h2 small{font-size:10pt;font-weight:500;margin-left:6pt}
.q{border:1px solid #e2e5de;border-radius:8pt;padding:8pt 10pt;margin:8pt 0;page-break-inside:avoid}
.hd{display:flex;gap:6pt;flex-wrap:wrap;align-items:center;font-size:8.5pt;color:#6b7268;margin-bottom:3pt}
.no{font-weight:700;color:#3d7a17}.yr{background:#eff0ec;border-radius:4pt;padding:0 4pt;font-family:"IBM Plex Mono",monospace}
.th{font-weight:600;font-size:11pt;margin:0 0 3pt}.stem{margin:0 0 4pt}
ol.ch{margin:0 0 4pt;padding-left:0;list-style:none}ol.ch li{margin:1pt 0}
.ans{background:#f6f7f3;border-radius:6pt;padding:6pt 8pt;margin-top:4pt;font-size:9.8pt}
.ans .k{font-weight:700;color:#3d7a17}.lab{font-weight:700;font-size:9pt;color:#3d7a17;margin:5pt 0 1pt}
.fix{background:#fdecea;color:#8a2a22;border-radius:4pt;padding:3pt 6pt;margin-top:4pt}
.ans ul{margin:1pt 0 1pt 14pt;padding:0}.ans p{margin:1pt 0}.pearl{font-style:normal;background:#fff3b0;padding:2pt 5pt;border-radius:4pt;display:inline-block;margin-top:4pt}
.small{font-size:8.5pt;color:#6b7268}\n.figs{display:flex;flex-wrap:wrap;gap:6pt;margin:3pt 0}.figs figure{margin:0;flex:0 1 46%}.figs img{max-width:100%;max-height:60mm;border-radius:4pt;display:block}.figs.big figure{flex:1 1 100%}.figs.big img{max-height:110mm}.figs figcaption{font-size:8pt;color:#6b7268}'''
def doc(title, intro, body):
    return (f'<!doctype html><html lang="th"><meta charset="utf-8"><title>{E(title)}</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&family=IBM+Plex+Mono&display=swap">'
            f'<style>{CSS}</style><div class="cover"><h1>{E(title)}</h1>{intro}</div>{body}</html>')
def picthumbs(x):
    if not x.get('pics'): return ''
    return '<div class="lab">รูปจากข้อสอบจริง MED35</div><div class="figs">' + ''.join(
        f'<figure><img src="{E(i["src"])}"><figcaption>{E(p["id"])}: {E(i["cap"])}</figcaption></figure>' for p in x['pics'] for i in p['img']) + '</div>'
def picblock(p):
    figs = '<div class="figs big">' + ''.join(f'<figure><img src="{E(i["src"])}"><figcaption>{E(i["cap"])}</figcaption></figure>' for i in p['img']) + '</div>'
    yrs = ''.join(f'<span class="yr">MED{y}</span>' for y in p['years'])
    fx = f'<div class="fix"><b>แก้ไข:</b> {inl(p["fix"])}</div>' if p['fix'] else ''
    if p['kind'] == 'pic':
        ch = ''.join(f'<li>{LET[i]}. {E(c)}</li>' for i, c in enumerate(p['choices']))
        body = f'<p class="stem">{E(p["q"])}</p>{figs}<ol class="ch">{ch}</ol><div class="ans"><span class="k">เฉลย {LET[p["answer"]]}. {E(p["choices"][p["answer"]])}</span>{md(p["explain"])}{fx}'
    else:
        qs = ''.join(f'<p class="th" style="font-size:10.5pt;margin-top:4pt">{E(q["q"])}</p><div class="ans">{md(q["a"])}</div>' for q in p['parts'])
        body = f'<p class="small">{E(p["station"])}</p><div class="stem">{md(p["q"])}</div>{figs}{qs}<div class="ans">{fx}'
    pr = f'<span class="pearl">{inl(p["pearl"])}</span>' if p['pearl'] else ''
    return (f'<div class="q"><div class="hd"><span class="no">{p["id"]}</span><span>แก่น: {E(p["theme"])}</span>{yrs}</div>'
            f'<p class="th">{E(p["title"])}</p>{body}{pr}</div></div>')
b1 = []
for st in sets:
    b1.append(f'<h2>{E(st["label"])}<small>{E(st["thai"])} · {len(st["one"])} แก่น</small></h2>')
    for k, x in enumerate(st['one'], 1):
        yrs = ''.join(f'<span class="yr">MED{y}</span>' for y in x['years'])
        ch = ''.join(f'<li>{LET[i]}. {E(c)}</li>' for i, c in enumerate(x['choices']))
        oth = ''
        if x['others']:
            oth = '<div class="lab">ข้ออื่นในแก่นนี้</div><ul>' + ''.join(f'<li>{E(o["q"][:160])}{"…" if len(o["q"])>160 else ""} → <b>{E(o["a"])}</b></li>' for o in x['others'][:6]) + '</ul>'
        b1.append(f'''<div class="q"><div class="hd"><span class="no">{st["label"]} {k}</span><span>ออก {len(x["years"])} รุ่น · {x["n"]} ข้อในแก่น</span>{yrs}</div>
<p class="th">{E(x["theme"])}</p><p class="stem">{E(x["q"])}</p><ol class="ch">{ch}</ol>
<div class="ans"><span class="k">เฉลย {LET[x["answer"]]}. {E(x["choices"][x["answer"]])}</span>{md(x["note"])}
{f'<div class="fix"><b>แก้ไขตามแนวทางปัจจุบัน:</b> {inl(x["fix"])}</div>' if x["fix"] else ''}
<div class="lab">เนื้อหาที่เกี่ยวข้องที่ต้องรู้</div>{md(x["related"])}{picthumbs(x)}{oth}<div class="small">{E(x["src"])}</div></div></div>''')
b1.append(f'<h2>ข้อสอบมีรูป<small>{len(pics)} ข้อ จากโพย MED35</small></h2>')
b1 += [picblock(p) for p in pics]
intro1 = (f'<p>ข้อสอบเก่าจากโพย MED28–MED35 ในคลัง MED421 Ward Drill {sum(len(s["one"]) for s in sets)} แก่น แก่นละ 1 ข้อ แยกตามระบบ '
          'เรียงจากแก่นที่ออกหลายรุ่นก่อน ทุกข้อบอกรุ่นที่แก่นนั้นเคยออก เฉลยมี "เนื้อหาที่เกี่ยวข้องที่ต้องรู้" ซึ่งรวมมุมที่ข้ออื่นในแก่นเคยถาม และ "ข้ออื่นในแก่นนี้" ไว้ทวนเร็ว</p>'
          '<p>เฉลยอยู่ใต้แต่ละข้อ ถ้าจะทำเป็นข้อสอบให้ปิดกล่องเฉลยไว้ก่อน</p>')
open(f'{ROOT}/print_one.html', 'w').write(doc('แก่นละ 1 ข้อ · MED421', intro1, ''.join(b1)))
b2 = []
for st in sets:
    b2.append(f'<h2>{E(st["label"])}<small>{E(st["thai"])} · {len(st["synth"])} ข้อ</small></h2>')
    for k, x in enumerate(st['synth'], 1):
        yrs = ''.join(f'<span class="yr">MED{y}</span>' for y in x['years'])
        ch = ''.join(f'<li>{LET[i]}. {E(c)}</li>' for i, c in enumerate(x['choices']))
        cov = '<div class="small">ครอบคลุมแก่น: ' + E(' / '.join(x['themes'])) + ('<br>เพิ่มจาก NL ที่ยังไม่เคยออก: ' + E(' / '.join(x['nl'])) if x['nl'] else '') + '</div>'
        b2.append(f'''<div class="q"><div class="hd"><span class="no">{x["id"]}</span><span>คลุม {len(x["themes"])} แก่น{f" + NL {len(x['nl'])} หัวข้อ" if x["nl"] else ""}</span>{yrs}</div>
<p class="th">{E(x["title"])}</p><p class="stem">{E(x["q"])}</p><ol class="ch">{ch}</ol>
<div class="ans"><span class="k">เฉลย {LET[x["answer"]]}. {E(x["choices"][x["answer"]])}</span>{md(x["explain"])}
<div class="lab">สรุปทั้งเรื่อง</div>{md(x["fullcover"])}{f'<span class="pearl">{inl(x["pearl"])}</span>' if x["pearl"] else ''}{cov}</div></div>''')
intro2 = (f'<p>โจทย์ใหม่ {sum(len(s["synth"]) for s in sets)} ข้อ แต่ละข้อรวมหลายแก่นของข้อสอบเก่าที่เป็นเรื่องเดียวกัน และเติมหัวข้อในเกณฑ์ NL 2567 ที่โพยยังไม่เคยออก '
          'ตั้งใจให้จำนวนข้อน้อยที่สุดแต่ครอบคลุมทุกแก่น เฉลยแต่ละข้อมี "สรุปทั้งเรื่อง" ไว้อ่านแทนการทำข้อสอบหลายข้อ</p><p>รุ่นที่แสดงคือรุ่นที่แก่นซึ่งข้อนั้นครอบคลุมเคยออก</p>')
open(f'{ROOT}/print_synth.html', 'w').write(doc('โจทย์รวบยอด · MED421', intro2, ''.join(b2)))
print(data['n_one'], data['n_syn'], [ (s['key'],len(s['one']),len(s['synth'])) for s in sets])
