"""ตรวจ out2/<sys>.json   ใช้: python3 check2.py <sys>"""
import json, sys
S = '/tmp/claude-0/-home-user/347a4502-c25a-5e77-97d4-8abdcb942e77/scratchpad'
s = sys.argv[1]
T = json.load(open(f'{S}/in2/{s}_themes.json')); G = json.load(open(f'{S}/in2/{s}_nlgaps.json'))
O = json.load(open(f'{S}/out2/{s}.json'))
err = []
names = {t['theme'] for t in T}; ids = {i['id'] for t in T for i in t['items']}
got = {o['theme'] for o in O['one_per_theme']}
if got != names: err.append(f'one_per_theme ไม่ตรงชุดแก่น: ขาด {sorted(names-got)[:5]} เกิน {sorted(got-names)[:5]}')
for o in O['one_per_theme']:
    if o.get('id') not in ids: err.append(f"id ไม่อยู่ใน input: {o.get('id')}")
    if len(o.get('related', '')) < 120: err.append(f"related สั้นเกิน: {o['theme'][:40]}")
cov_t = set(); cov_n = set()
for q in O['synth']:
    for k in ('id', 'title', 'stem', 'choices', 'explain', 'fullcover', 'pearl', 'covers_themes', 'covers_nl'):
        if k not in q: err.append(f"{q.get('id')} ขาด {k}")
    if len(q.get('choices', [])) != 5 or len(set(q.get('choices', []))) != 5: err.append(f"{q.get('id')} ตัวเลือกต้อง 5 ไม่ซ้ำ")
    if q.get('answer', 0) != 0: err.append(f"{q.get('id')} answer ต้องเป็น 0")
    bad = set(q.get('covers_themes', [])) - names
    if bad: err.append(f"{q.get('id')} covers_themes ชื่อไม่ตรง: {list(bad)[:2]}")
    cov_t |= set(q.get('covers_themes', [])); cov_n |= set(q.get('covers_nl', []))
if names - cov_t: err.append(f'แก่นที่ยังไม่มีโจทย์รวบยอดคลุม: {sorted(names-cov_t)}')
gn = {g['topic'] for g in G}
if gn - cov_n: err.append(f'NL gap ที่ยังไม่คลุม: {sorted(gn-cov_n)}')
if cov_n - gn: err.append(f'covers_nl ชื่อไม่ตรง: {sorted(cov_n-gn)[:3]}')
print('\n'.join(err) if err else f'OK: {len(O["one_per_theme"])} แก่น, โจทย์รวบยอด {len(O["synth"])} ข้อ')
