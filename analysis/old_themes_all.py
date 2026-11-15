"""จัดแก่นข้อสอบเก่า (bank[sys].old) ของหน้า MED421 Ward Drill ทั้ง 11 ระบบ
ใช้: python3 analysis/old_themes_all.py <bank.json> <themes_dir>
  bank.json  = JSON ใน <script id="bank"> ของหน้า Ward Drill
  themes_dir = โฟลเดอร์ <sys>.json รูปแบบ [{"theme":..., "ids":[...]}]
ผลลัพธ์: analysis/old_themes.json (render_page.py อ่านต่อ) + analysis/theme_map.json (สำเนาการจัดแก่น)
"""
import json, sys, os, collections
ROOT = os.path.dirname(os.path.abspath(__file__))
LABEL = {'cardio':'Cardio','nephro':'Nephro','chest':'Chest','neuro':'Neuro','air':'AIR','infect':'Infect',
         'gi':'GI','endo':'Endo','heme':'Heme','derm':'Derm','onco':'Onco'}
bank = json.load(open(sys.argv[1])); tdir = sys.argv[2]
items, themes, tmap = {}, [], {}
for s, v in bank.items():
    for g in v.get('old', []):
        for i in g['items']:
            items[i['id']] = dict(i, sys=s, years=sorted({int(y) for y in i.get('years', [])}))
for s in LABEL:
    if not os.path.exists(f'{tdir}/{s}.json'): continue
    tmap[s] = json.load(open(f'{tdir}/{s}.json'))
    for t in tmap[s]:
        themes.append({'system': LABEL[s], 'theme': t['theme'], 'ids': t['ids']})
# แก่นชื่อเดียวกันข้ามระบบ = แก่นเดียวกัน (รวมข้อ) และรวมแก่นที่ระบุใน merge.json (ชื่อปลายทาง: [ชื่อที่ยุบเข้า])
mfile = f'{tdir}/merge.json'
alias = {o: k for k, v in (json.load(open(mfile)).items() if os.path.exists(mfile) else []) for o in v}
merged = {}
for t in themes:
    name = alias.get(t['theme'], t['theme'])
    m = merged.setdefault(name, {'system': [], 'theme': name, 'ids': []})
    if t['system'] not in m['system']: m['system'].append(t['system'])
    m['ids'] += t['ids']
themes = [dict(m, system=' + '.join(m['system'])) for m in merged.values()]
seen = collections.Counter(i for t in themes for i in t['ids'])
dup = [i for i, c in seen.items() if c > 1]; miss = sorted(set(items) - set(seen)); extra = sorted(set(seen) - set(items))
assert not dup and not extra, (dup[:10], extra[:10])
if miss: print('ยังไม่ได้จัด', len(miss), 'ข้อ', miss[:10])
out_t = []
for t in themes:
    its = [items[i] for i in t['ids']]
    yrs = collections.Counter(y for it in its for y in it['years'])
    out_t.append({'system': t['system'], 'theme': t['theme'], 'n': len(its), 'years': dict(sorted(yrs.items())),
                  'first': min(yrs) if yrs else None,
                  'items': [{'id': it['id'], 'lec': it['lec'], 'years': it['years'], 'q': it['q'],
                             'a': it['choices'][it['answer']] if 'choices' in it else it.get('a', '')} for it in its]})
YEARS = sorted({y for x in items.values() for y in x['years']})
theme_of = {i: t for t in out_t for i in (it['id'] for it in t['items'])}
per_year = []
for Y in YEARS:
    yi = [x for x in items.values() if Y in x['years'] and x['id'] in theme_of]
    rep = [x for x in yi if x['years'][0] < Y]
    ang = [x for x in yi if x['years'][0] == Y and theme_of[x['id']]['first'] < Y]
    hit = {id(theme_of[x['id']]): theme_of[x['id']] for x in yi}.values()
    new = [t for t in hit if t['first'] == Y]
    per_year.append({'year': Y, 'items': len(yi), 'themes': len(hit), 'repeat_items': len(rep),
                     'new_angle_items': len(ang), 'new_theme_items': len(yi) - len(rep) - len(ang),
                     'new_themes': [{'theme': t['theme'], 'system': t['system'],
                                     'items': [it for it in t['items'] if Y in it['years']]} for t in new]})
no_year = sum(1 for x in items.values() if not x['years'])
o = {'n_items': len(items), 'n_themes': len(out_t), 'no_year': no_year,
     'systems': [LABEL[s] for s in LABEL if s in tmap], 'themes': out_t, 'per_year': per_year}
json.dump(o, open(f'{ROOT}/old_themes.json', 'w'), ensure_ascii=False, indent=1)
json.dump(tmap, open(f'{ROOT}/theme_map.json', 'w'), ensure_ascii=False, indent=1)
print(o['n_items'], 'ข้อ', o['n_themes'], 'แก่น', 'ไม่มีปี', no_year)
print('ขนาดแก่น', sorted(collections.Counter(t['n'] for t in out_t).items()))
for p in per_year:
    print(f"MED{p['year']}: {p['items']} ข้อ/{p['themes']} แก่น | ซ้ำ {p['repeat_items']} | มุมใหม่ {p['new_angle_items']} | แก่นใหม่ {len(p['new_themes'])} ({p['new_theme_items']} ข้อ)")
