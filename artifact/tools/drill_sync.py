#!/usr/bin/env python3
"""
drill_sync.py — ส่งข้อสอบใหม่จากบทเรียน (MED421 learn) เข้า Ward Drill

Ward Drill (artifact Fdi5gcNXKqFLAXg4fQBV7X) build จาก branch `claude/adoring-babbage-zkg8ih`
(config.json + data/*.json --build.py--> drill.html) ไม่ใช่ repo นี้
สคริปต์นี้เขียนไฟล์ลงใน checkout ของ branch นั้น — รันซ้ำได้ ผลเหมือนเดิม

    git worktree add ../drillwt origin/claude/adoring-babbage-zkg8ih
    python3 artifact/tools/drill_sync.py ../drillwt
    cd ../drillwt && python3 build.py --no-pdf

สิ่งที่ทำ
  1. ดึงข้อ MCQ ที่เขียนใหม่ในบทเรียน (เฉพาะ id ขึ้นต้นตาม PREFIX — ข้อ N-MCQ/MOCK มีในคลังอยู่แล้ว)
     แปลงเป็น schema คลัง โดยคงลำดับตัวเลือก/เฉลยเดิมของบทเรียน (กระจายเฉลยสมดุลแล้ว · ตัวอักษรตรงกันทั้งสองเว็บ)
  2. ดึง MEQ/OSCE ของบทเรียนเดียวกัน
  3. config.json: เพิ่มคาบ (lectures) + lecture_order + ไฟล์ใน `mcq_late`/`meq`
     `mcq_late` = ข้อที่ build.py *ไม่สลับ* ตัวเลือก และไม่ดึงเลขสุ่มของ seed → ลำดับตัวเลือกของข้อเดิมไม่เปลี่ยน
     (คำตอบที่ผู้ใช้บันทึกไว้เก็บเป็นเลขตำแหน่ง — ถ้าลำดับเปลี่ยน คำตอบเก่าจะชี้ผิดข้อ)
  4. build.py: รองรับ `mcq_late`
  5. template.html: ลิงก์ตรง #<ชุด>-<คาบ> (applyHash — ของ live v11 จาก Lecture Dashboard)
     + โจทย์ MEQ/OSCE ที่มีตารางเรนเดอร์เป็นตารางจริง
  6. refs/nl_2567.json: เติมรหัส NL ที่ข้อใหม่อ้าง (คัดจาก artifact/data/nl.json — ประกาศฉบับเต็ม)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEARN = os.path.join(HERE, '..', 'data')

# (ไฟล์บทเรียน, lec ในบทเรียน, ชุดในคลัง, lec ในคลัง, prefix ข้อใหม่, ชื่อไฟล์คลัง, คาบใหม่ {date, week} หรือ None)
JOBS = [
    ('nephro.json', '14', 'nephro', '14', 'NEPH-GN-', 'gn', None),
    ('nephro.json', '30', 'nephro', '30', 'NEPH-UTI-', 'uti', None),
    ('nephro.json', 'Imaging', 'nephro', 'IMG', 'NEPH-IMG-', 'img',
     {'date': 'ไม่ระบุวัน — handout Lec19 (อ.ธนิศร)', 'week': '', 'al': 0}),
    ('hemonc.json', '12/10', 'heme', 'H04', 'HON-WBC-', 'wbc', {'date': 'จ. 12 ต.ค.', 'week': 5, 'al': 0}),
    ('endo.json', '14/10', 'endo', 'E05', 'END-DM-', 'dm', {'date': 'พ. 14 ต.ค.', 'week': 5, 'al': 0}),
]
# ตำแหน่งคาบใหม่ใน lecture_order: แทรกหลังคาบนี้ (None = ขึ้นก่อน)
AFTER = {'IMG': '28', 'H04': None, 'E05': 'E04'}
BLURB = {
    'nephro': '8 คาบบรรยาย · 15.9% ของ lecture ทั้งหมด · ออกสอบหนักทุกรุ่น · '
              'ข้อจากบทเรียน glomerular disease · UTI · renal imaging',
    'heme': '4 คาบบรรยาย · Approach to WBC disorder and lymphadenopathy (อ.เบญจมาภรณ์) · '
            'โลหิตจางและธาลัสซีเมีย · เกล็ดเลือด การแข็งตัวของเลือด และการให้เลือด · มะเร็งเม็ดเลือดและภาวะฉุกเฉินที่เกี่ยวข้อง',
    'endo': '5 หัวข้อ · Diabetes mellitus ตั้งแต่วินิจฉัยถึง DKA (ศ.นพ.ชัยชาญ) · '
            'Metabolic syndrome โรคอ้วน และไขมันในเลือดผิดปกติ (อ.นวพร) · เบาหวานและภาวะฉุกเฉินทางเมตาบอลิก (DKA · HHS · น้ำตาลต่ำ) · '
            'โรคของต่อมไทรอยด์ · ต่อมหมวกไต ต่อมใต้สมอง และเมตาบอลิซึมของกระดูก',
}
MCQ_KEYS = ('id', 'lec', 'lecture', 'topic', 'stem', 'choices', 'answer', 'explain', 'pearl', 'ref', 'nl')


def lectures_of(fn):
    d = json.load(open(os.path.join(LEARN, fn), encoding='utf-8'))
    return d['lectures'] if isinstance(d, dict) else d


def dump(path, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')


def convert(drill):
    cfg_p = os.path.join(drill, 'config.json')
    cfg = json.load(open(cfg_p, encoding='utf-8'))
    sets = {s['key']: s for s in cfg['sets']}
    nl_codes = set()
    report = []
    for fn, lec, setk, dlec, prefix, tag, newlec in JOBS:
        L = next(l for l in lectures_of(fn) if l['lec'] == lec)
        name = next((m['lecture'] for m in L.get('meq', []) + L.get('osce', []) if m['id'].startswith(prefix)), L['title'])
        mcq = []
        for s in L['sections']:
            for it in s.get('items', []):
                if it['kind'] != 'mcq' or not it['id'].startswith(prefix):
                    continue
                out = dict(it, lec=dlec, lecture=name)
                out = {k: out[k] for k in MCQ_KEYS if out.get(k) not in (None, '', [])}
                assert len(out['choices']) == 5 and len(set(out['choices'])) == 5, it['id']
                mcq.append(out)
        meq = []
        for m in L.get('meq', []) + L.get('osce', []):
            if not m['id'].startswith(prefix):
                continue
            o = {k: v for k, v in m.items() if not k.startswith('_') and k != 'years'}
            o['lec'], o['lecture'] = dlec, name
            meq.append(o)
        for it in mcq + meq:
            nl_codes |= set(it.get('nl', []))
        mf, ef = f'data/{setk}_mcq_{tag}.json', f'data/{setk}_meq_{tag}.json'
        dump(os.path.join(drill, mf), mcq)
        dump(os.path.join(drill, ef), meq)
        s = sets[setk]
        late = s.setdefault('mcq_late', [])
        if mf not in late:
            late.append(mf)
        if ef not in s['meq']:
            s['meq'].append(ef)
        if newlec:
            cfg['lectures'][dlec] = newlec
        order = s['lecture_order']
        if dlec not in order:
            a = AFTER.get(dlec)
            order.insert(order.index(a) + 1 if a in order else 0, dlec)
        report.append(f'{setk:7s} {dlec:4s} MCQ {len(mcq):2d} · MEQ/OSCE {len(meq)} ← learn {fn} {lec}')
    for k, b in BLURB.items():
        sets[k]['blurb'] = b
    dump(cfg_p, cfg)
    return nl_codes, report


def add_nl(drill, codes):
    p = os.path.join(drill, 'refs', 'nl_2567.json')
    ref = json.load(open(p, encoding='utf-8'))
    full = json.load(open(os.path.join(LEARN, 'nl.json'), encoding='utf-8'))
    added, missing = [], []
    for c in sorted(codes):
        if c in ref['entries']:
            continue
        if c not in full:
            missing.append(c)
            continue
        e = full[c]
        ref['entries'][c] = {k: e[k] for k in ('part', 'section', 'page', 'title') if k in e}
        added.append(c)
    dump(p, ref)
    return added, missing


def patch_build(drill):
    p = os.path.join(drill, 'build.py')
    t = open(p, encoding='utf-8').read()
    if "mcq_late" in t:
        return False
    rep = [
        ("        mcq = load_many(s.get('mcq', []))\n",
         "        mcq = load_many(s.get('mcq', []))\n"
         "        # mcq_late = ข้อจากบทเรียน (MED421 learn) จัดลำดับตัวเลือกมาแล้ว — ไม่สลับ และไม่ดึงเลขสุ่ม\n"
         "        #            ข้อเดิมจึงได้ลำดับตัวเลือกเท่าเดิมทุกข้อ (คำตอบที่บันทึกไว้เก็บเป็นเลขตำแหน่ง)\n"
         "        late = load_many(s.get('mcq_late', []))\n"),
        ("        for it in mcq + meq:\n            names.setdefault",
         "        for it in mcq + late + meq:\n            names.setdefault"),
        ("        validate(k, mcq, meq, oldg, CFG['lectures'])\n",
         "        validate(k, mcq + late, meq, oldg, CFG['lectures'])\n"),
        ("            it['answer'] = it['choices'].index(correct)\n",
         "            it['answer'] = it['choices'].index(correct)\n        mcq = mcq + late\n"),
    ]
    for a, b in rep:
        assert t.count(a) == 1, a
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)
    return True


APPLYHASH = '''
/* ---------- ลิงก์ตรงจาก Lecture Dashboard: #<ชุด> หรือ #<ชุด>-<คาบ> เช่น #cardio-13 ---------- */
function applyHash(){
  var h=String(location.hash||"").replace(/^#/,"");
  if(!h)return false;
  var i=h.indexOf("-"),k=i<0?h:h.slice(0,i),l=i<0?"":h.slice(i+1);
  if(!BANK[k])return false;
  state.set=k;state.mode="new";state.part="all";state.lec="all";
  if(l){
    if(newItems(k).some(function(it){return it.lec===l;}))state.lec=l;
    else if(BANK[k].old.some(function(g){return g.lec===l;})){state.mode="old";state.lec=l;}
  }
  save();return true;
}
applyHash();
window.addEventListener("hashchange",function(){if(applyHash()){render();window.scrollTo(0,0);}});
'''


def patch_template(drill):
    p = os.path.join(drill, 'template.html')
    t = open(p, encoding='utf-8').read()
    done = []
    if 'function applyHash' not in t:
        a = '\n\nrender();\n})();\n</script>'
        assert t.count(a) == 1
        t = t.replace(a, '\n' + APPLYHASH + '\nrender();\n})();\n</script>')
        done.append('applyHash')
    old = ('  if(it.vignette)h+="<div class=\'vign\'>"+inline(it.vignette)+"</div>";\n'
           '  if(it.instruction)h+="<div class=\'vign\'>"+inline(it.instruction)+"</div>";\n')
    new = ('  if(it.vignette)h+=vign(it.vignette);\n'
           '  if(it.instruction)h+=vign(it.instruction);\n')
    if old in t:
        t = t.replace(old, new)
        a = 'function md(src){'
        t = t.replace(a, '/* โจทย์ MEQ/OSCE: มีตาราง → เรนเดอร์ด้วย md() ไม่งั้นคงบรรทัดเดิม (pre-wrap) */\n'
                         'function vign(s){return /^\\s*\\|/m.test(s)?"<div class=\'vign md vmd\'>"+md(s)+"</div>":'
                         '"<div class=\'vign\'>"+inline(s)+"</div>";}\n' + a, 1)
        a = '.vign strong{font-weight:600}'
        t = t.replace(a, a + '\n.vign.vmd{white-space:normal}', 1)
        done.append('vign-md')
    open(p, 'w', encoding='utf-8').write(t)
    return done


def main():
    if len(sys.argv) != 2 or not os.path.exists(os.path.join(sys.argv[1], 'build.py')):
        sys.exit(__doc__)
    drill = sys.argv[1]
    codes, report = convert(drill)
    added, missing = add_nl(drill, codes)
    print('\n'.join(report))
    print(f'NL: เติม {len(added)} รหัส' + (f' · ไม่พบในประกาศ {missing}' if missing else ''))
    print('build.py:', 'patched' if patch_build(drill) else 'มี mcq_late แล้ว')
    print('template.html:', patch_template(drill) or 'ครบแล้ว')


if __name__ == '__main__':
    main()
