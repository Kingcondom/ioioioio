#!/usr/bin/env python3
"""
patch_dash_review.py — ปุ่ม "ฝึกข้อสอบคาบที่ทวนแล้ว" ใน MED421 Lectures (dashboard)

    python3 dashboard/patch_dash_review.py <dashboard index.html> <out.html> [--edits edits.json]

ปุ่มอยู่ในแผง "การทวนของฉัน" (ใต้ช่องนับทวนแล้ว/ถึงรอบ) — รวมทุกคาบที่กด ✓ ทวนไว้แล้วอย่างน้อย 1 รอบ
และมีข้อสอบใน Drill แล้วเปิด Ward Drill ที่ `#review~<hash drill ของคาบ>_<จำนวนรอบที่ทวน>~…`
(hash drill = `drill[0]` ของคาบใน LECS เช่น chest-03 · neuro-N02 · derm) เรียงจากคาบที่ทวนล่าสุด
คาบที่ชี้ชุดเดียวกันรวมเป็นอันเดียว · Drill ต้องมีโหมด "คาบที่ทวนแล้ว" (patch_drill_review.py)

รันได้กับหน้าที่ยังไม่แพตช์เท่านั้น · --edits เขียนคู่ old/new ไว้ส่งให้ edit_version ของ artifact
"""
import json, sys

CSS_ANCHOR = ".links a small{margin-left:auto;font-size:11.5px;font-weight:500;color:var(--ink-3)}\n"
CSS = """.practice{display:flex;align-items:center;gap:11px;text-decoration:none;border-radius:16px;padding:11px 13px;
  background:var(--lav);color:var(--lav-ink);transition:background .2s var(--e),transform .18s var(--e)}
a.practice:hover{background:var(--lav-2);transform:translateY(-1px)}
.practice svg{width:22px;height:22px;flex:none}
.practice b{display:block;font-family:var(--display);font-weight:600;font-size:14px;line-height:1.3}
.practice small{display:block;font-size:12px;opacity:.85;line-height:1.4}
.practice.off{background:var(--sunk);color:var(--ink-3)}
"""

FN_ANCHOR = "function renderSide(){\n"
FN = r"""/* ฝึกข้อสอบคาบที่ทวนแล้ว → Ward Drill #review~<hash drill>_<รอบที่ทวน>~… (patch_dash_review.py)
   รวมคาบที่ทวนแล้วอย่างน้อย 1 รอบและมีข้อสอบใน Drill · คาบที่ชี้ชุดเดียวกันรวมกัน · เรียงจากที่ทวนล่าสุด */
function practiceKeys(){
  var by={},out=[];
  LECS.forEach(function(l){var ds=R[l.id]||[];if(!ds.length||!l.drill)return;
    var k=l.drill[0],last=ds[ds.length-1];
    if(!/^[A-Za-z0-9]+(-[A-Za-z0-9.]+)?$/.test(k))return;
    if(!by[k]){by[k]={k:k,n:0,last:"",s:l.start};out.push(by[k]);}
    var x=by[k];x.n=Math.max(x.n,ds.length);if(last>x.last)x.last=last;});
  out.sort(function(a,b){return a.last<b.last?1:a.last>b.last?-1:a.s-b.s;});
  return out;
}
function practiceHtml(){
  var ks=practiceKeys();
  if(!ks.length)return "<div class='practice off'>"+ICON.target+"<span><b>ฝึกข้อสอบคาบที่ทวนแล้ว</b>"+
    "<small>กด ✓ คาบที่ทวนแล้ว ข้อสอบเก่าของคาบนั้นจะรวมให้ฝึกใน Ward Drill แยกปี · MCQ / MEQ / SAQ</small></span></div>";
  var url=DRILL+"#review~"+ks.map(function(x){return x.k+"_"+x.n;}).join("~");
  return ext(url,"practice",ICON.target+"<span><b>ฝึกข้อสอบคาบที่ทวนแล้ว</b><small>"+ks.length+" คาบ · แยกปี · MCQ / MEQ / SAQ ใน Ward Drill</small></span>",
    "ฝึกข้อสอบของ "+ks.length+" คาบที่ทวนแล้ว ใน Ward Drill");
}
"""

TILES_OLD = """<span>ยังไม่ถึงคาบ</span></button></div>"+\n"""
TILES_NEW = """<span>ยังไม่ถึงคาบ</span></button></div>"+\n    practiceHtml()+\n"""

EDITS = [
    (CSS_ANCHOR, CSS_ANCHOR + CSS),
    (FN_ANCHOR, FN + FN_ANCHOR),
    (TILES_OLD, TILES_NEW),
]


def patch(html):
    for old, new in EDITS:
        n = html.count(old)
        assert n == 1, f'anchor พบ {n} ครั้ง (ต้อง 1): {old[:70]!r}'
        html = html.replace(old, new)
    return html


if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    html = open(src, encoding='utf-8').read()
    open(out, 'w', encoding='utf-8').write(patch(html))
    if '--edits' in sys.argv:
        fn = sys.argv[sys.argv.index('--edits') + 1]
        json.dump([{'old_text': o, 'new_text': n} for o, n in EDITS], open(fn, 'w', encoding='utf-8'), ensure_ascii=False)
    print('patched', out)
