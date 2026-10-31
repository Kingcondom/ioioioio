#!/usr/bin/env python3
"""
patch_dash_review.py — ปุ่ม "ฝึกข้อสอบคาบที่ทวนแล้ว" ใน MED421 Lectures (dashboard)

    python3 dashboard/patch_dash_review.py <dashboard index.html> <out.html> [--edits edits.json]

ปุ่มอยู่ในแผง "การทวนของฉัน" (ใต้ช่องนับทวนแล้ว/ถึงรอบ) — รวมทุกคาบที่กด ✓ ทวนไว้แล้วอย่างน้อย 1 รอบ
และมีข้อสอบใน Drill แล้วเปิด Ward Drill ที่ `#review~y2026~<MMDDHHMM ของคาบ>.<MMDD วันที่ทวน>…~…`
Drill จัดกลุ่มตามวันที่ทวนเอง · Drill ต้องมีโหมด "คาบที่ทวนแล้ว" (patch_drill_review.py)
ปกติ Drill ดึงการทวนจากบัญชีอัตโนมัติ (งานตั้งเวลา) ปุ่มนี้ใช้เมื่ออยากได้ทันที

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
FN = r"""/* ฝึกข้อสอบคาบที่ทวนแล้ว → Ward Drill #review~y2026~<MMDDHHMM>.<MMDD>.<MMDD>~… (patch_dash_review.py)
   ส่งทุกคาบที่ทวนแล้วและมีข้อสอบใน Drill พร้อมวันที่ทวน · drill จัดกลุ่มตามวันที่ทวนเอง
   (drill ซิงก์จากบัญชีอัตโนมัติด้วย ปุ่มนี้ใช้เมื่ออยากได้ทันที) */
function practiceRev(){
  var out=[];
  LECS.forEach(function(l){var ds=R[l.id]||[];if(!ds.length||!l.drill||!/^2026-\d\d-\d\d-\d{4}$/.test(l.id))return;
    out.push(l.id.slice(5,7)+l.id.slice(8,10)+l.id.slice(11)+ds.filter(function(d){return d.slice(0,4)==="2026";})
      .map(function(d){return "."+d.slice(5,7)+d.slice(8,10);}).join(""));});
  return out.filter(function(t){return t.length>8;});
}
function practiceHtml(){
  var ts=practiceRev();
  if(!ts.length)return "<div class='practice off'>"+ICON.target+"<span><b>ฝึกข้อสอบคาบที่ทวนแล้ว</b>"+
    "<small>กด ✓ คาบที่ทวนแล้ว ข้อสอบของคาบนั้นจะรวมให้ฝึกใน Ward Drill แยกตามวันที่ทวน · ปี · MCQ / MEQ / SAQ</small></span></div>";
  var url=DRILL+"#review~y2026~"+ts.join("~");
  return ext(url,"practice",ICON.target+"<span><b>ฝึกข้อสอบคาบที่ทวนแล้ว</b><small>"+ts.length+" คาบ · แยกตามวันที่ทวน · MCQ / MEQ / SAQ ใน Ward Drill</small></span>",
    "ฝึกข้อสอบของ "+ts.length+" คาบที่ทวนแล้ว ใน Ward Drill");
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
