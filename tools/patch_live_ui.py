#!/usr/bin/env python3
"""แพตช์หน้าตา Ward Drill ที่ publish อยู่ (ผู้ใช้ขอ 14 พ.ย. 2569)

1. แยกหน้า "ข้อแต่ง" กับ "ข้อจากโพย"
   - ข้อแต่ง  = ข้อใหม่ที่ไม่มีฟิลด์ years (เขียนขึ้นเองจากสไลด์/แนวทาง)
   - ข้อจากโพย = คลังข้อสอบเก่าทั้งหมด + ข้อใหม่ที่มี years (เรียบเรียงจากข้อสอบจริงของรุ่นนั้น)
2. หน้าแรก: แสดง keyword ของข้อที่ตอบผิด (โชว์อย่างเดียว ไม่ต้องกด)
   - ข้อใหม่ใช้ topic · ข้อเก่าซึ่งไม่มี topic ใช้คำตอบที่ถูกเป็น keyword

ใช้:  python3 tools/patch_live_ui.py <in.html> <out.html>   (รันซ้ำได้ — ถ้าแพตช์อยู่แล้วจะข้าม)
"""
import sys

MARK = "/* ui-split-poy v2 */"

EDITS = [
    # 1) ชื่อแท็บ
    ('{k:"new",label:"ข้อสอบใหม่"},{k:"old",label:"คลังข้อสอบเก่า"}',
     '{k:"new",label:"ข้อแต่ง"},{k:"old",label:"ข้อจากโพย"}'),
    # 2) ตัวช่วยแยกข้อ
    ('function yrs(it){return it.years||[];}',
     'function yrs(it){return it.years||[];}\n' + MARK +
     '\nfunction isPoy(it){return yrs(it).length>0;}'
     '\nfunction craftItems(set){return newItems(set).filter(function(it){return !isPoy(it);});}'
     '\nfunction poyNew(set){return newItems(set).filter(isPoy);}'),
    # 3) นับในแถบคาบ
    ('if(state.mode!=="old")return newItems(state.set);',
     'if(state.mode==="new")return craftItems(state.set);\n  if(state.mode!=="old")return newItems(state.set);'),
    ('    g.items.forEach(function(it){out.push({lec:it.lec||g.lec,lecture:it.lecture||g.lecture});});\n  });\n  return out;',
     '    g.items.forEach(function(it){out.push({lec:it.lec||g.lec,lecture:it.lecture||g.lecture});});\n  });\n'
     '  poyNew(state.set).forEach(function(it){out.push({lec:it.lec,lecture:it.lecture});});\n  return out;'),
    # 4) ตัวเลขบนแท็บ
    ('var mcounts={new:newItems(state.set).length,\n    old:BANK[state.set].old.reduce(function(a,g){return a+g.items.length;},0),',
     'var mcounts={new:craftItems(state.set).length,\n    old:BANK[state.set].old.reduce(function(a,g){return a+g.items.length;},0)+poyNew(state.set).length,'),
    # 5) หน้าข้อแต่ง
    ('function renderNew(stream){\n  var items=filtered();',
     'function renderNew(stream){\n  var items=filtered().filter(function(it){return !isPoy(it);});'),
]

OLD_START = "function renderOld(stream){"
OLD_END = "/* ---------- main render ---------- */"
NEW_RENDER_OLD = r'''function renderOld(stream){
  var want=function(l){return state.lec==="all"||l===state.lec;};
  var groups=BANK[state.set].old.filter(function(g){return want(g.lec);});
  var pn=poyNew(state.set).filter(function(it){return want(it.lec);});
  var byLec={},order=[];
  groups.forEach(function(g){if(!byLec[g.lec]){byLec[g.lec]={g:g,extra:[]};order.push(g.lec);}});
  pn.forEach(function(it){if(!byLec[it.lec]){byLec[it.lec]={g:{lec:it.lec,lecture:it.lecture,items:[]},extra:[]};order.push(it.lec);}byLec[it.lec].extra.push(it);});
  var total=groups.reduce(function(a,g){return a+g.items.length;},0)+pn.length;
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ข้อจากโพย (MED28–MED35)</h2><span class='meta'>"+total+" ข้อ</span>";
  stream.appendChild(head);
  var n=document.createElement("p");n.className="oldnote wide";
  n.textContent="ข้อที่มาจากข้อสอบจริงทุกข้อ: คลังข้อสอบเก่าที่เรียบเรียงเป็นตัวเลือก 5 ข้อ + ข้อที่เขียนจากข้อสอบของรุ่นนั้น (มีป้าย MEDxx) — ข้อที่แต่งขึ้นเองอยู่ในแท็บ “ข้อแต่ง”";
  stream.appendChild(n);
  if(!order.length){var e=document.createElement("p");e.className="empty";e.textContent="ไม่มีข้อในเงื่อนไขนี้";stream.appendChild(e);return;}
  order.forEach(function(lec){
    var g=byLec[lec].g,extra=byLec[lec].extra,meta=LEC[g.lec]||{};
    var cnt=g.items.length+extra.length;
    var sec=document.createElement("section");sec.className="oldgrp";
    sec.innerHTML="<h3><span class='qno'>Lec "+esc(g.lec)+"</span>"+esc(shortName(g.lecture||""))+
      "<span class='tag'>"+esc(meta.d||"")+"</span><span class='tag'>"+cnt+" ข้อ</span></h3>"+
      (g.count_note?"<p class='oldnote'>"+esc(g.count_note)+"</p>":"");
    g.items.forEach(function(it){
      if(it.choices){ sec.appendChild(renderOldChoice(it,g)); return; }
      var d=document.createElement("div");d.className="olditem";
      d.innerHTML="<span class='pt'>"+esc(it.part)+"</span><div><p class='q'>"+inline(it.q)+"</p>"+
        "<p class='a'>"+inline(it.a)+"</p><p class='src'>"+inline(it.src)+"</p></div>";
      sec.appendChild(d);
    });
    extra.forEach(function(it,i){sec.appendChild(partOf(it)==="MCQ"?renderMCQ(it,i):renderLong(it));});
    stream.appendChild(sec);
  });
}

'''

HOME_ANCHOR = "  function viewHome(){"
HOME_FUNC = r'''  /* keyword ของข้อที่ตอบผิด (โชว์อย่างเดียว) */
  function trKw(e){var it=e.it,t=it.topic||"";
    if(!t&&it.choices&&it.choices[it.answer]!=null)t=it.choices[it.answer];
    t=String(t||it.id).replace(/^(SAQ|OSCE|MEQ)\s*[–-]\s*/,"");
    return t.length>70?t.slice(0,68)+"…":t;}
  function trWrongKw(){var L=wrongIn();if(!L.length)return "";
    var by={},n=0;L.forEach(function(e){(by[e.set]=by[e.set]||[]).push(e);});
    var hid=false;try{hid=localStorage.getItem(WK_KEY)==="1";}catch(e){}
    var h="<details class='tr-wk' aria-label='ข้อที่ตอบผิด'"+(hid?"":" open")+"><summary class='tr-whead'><h3>ข้อที่ตอบผิด</h3><span>"+L.length+" ข้อ · <u class='tr-wk-on'>ซ่อน</u><u class='tr-wk-off'>แสดง</u></span></summary>";
    SETS.forEach(function(s){var a=by[s.k];if(!a)return;
      h+="<div class='tr-wk-set'><b>"+esc(s.label)+"</b><div class='tr-wk-chips'>"+
        a.map(function(e){return "<span class='tr-wk-chip'>"+esc(trKw(e))+"</span>";}).join("")+"</div></div>";});
    return h+"</details>";}
  /* ซ่อน/แสดงการ์ดข้อที่ตอบผิด — จำไว้ในเครื่อง */
  var WK_KEY="med421-drill-wkhide";
  document.addEventListener("toggle",function(ev){var t=ev.target;
    if(t&&t.classList&&t.classList.contains("tr-wk")){try{localStorage.setItem(WK_KEY,t.open?"0":"1");}catch(e){}}},true);
'''
TILES_END = "<small>คาบที่ทวนแล้ว</small><b>\"+rvUnits().length+\"<em> คาบ</em></b></button></div>\";"
CSS = """
/* keyword ข้อที่ตอบผิดบนหน้าแรก */
.tr-wk{display:grid;gap:12px;background:var(--surface);border-radius:20px;padding:16px}
.tr-wk .tr-whead{margin:0;cursor:pointer;list-style:none;min-height:44px;align-items:center}
.tr-wk .tr-whead::-webkit-details-marker{display:none}
.tr-wk:not([open]){padding-block:4px}
.tr-wk u{text-decoration:none;color:var(--pen);font-weight:600;padding-left:4px}
.tr-wk[open] .tr-wk-off,.tr-wk:not([open]) .tr-wk-on{display:none}
.tr-wk-set{display:grid;gap:8px}
.tr-wk-set>b{font-size:14px;font-weight:600;color:var(--ink-2)}
.tr-wk-chips{display:flex;flex-wrap:wrap;gap:6px}
.tr-wk-chip{font-size:14px;line-height:1.4;padding:4px 12px;border-radius:999px;background:var(--bad-soft);color:var(--bad);max-width:100%}
</style>"""


# ---- v3: แถบล่าง "หน้าแรก | ใหม่ | เก่า | (+) | สุ่มสอบ | ทวนแล้ว" (ผู้ใช้ขอ 14 พ.ย.) ----
MARK3 = "/* ui-nav-newold v3 */"
EDITS_V3 = [
    ('var NAV=[["home","หน้าแรก"],["drill","ข้อสอบ"],["plus","ทางลัด"],["quiz","สุ่มสอบ"],["review","ทวนแล้ว"]]',
     MARK3 + 'var NAV=[["home","หน้าแรก"],["new","ใหม่"],["old","เก่า"],["plus","ทางลัด"],["quiz","สุ่มสอบ"],["review","ทวนแล้ว"]]'),
    ('function pageOf(){if(V.view==="home")return "home";if(state.mode==="quiz")return "quiz";if(state.mode==="review")return "review";return "drill";}',
     'function pageOf(){if(V.view==="home")return "home";if(state.mode==="quiz")return "quiz";if(state.mode==="review")return "review";'
     'if(state.mode==="new"||state.mode==="old")return state.mode;return "drill";}'),
    ('[["home","หน้าแรก","home"],["drill","ข้อสอบรายคาบ","drill"],["quiz","สุ่มทำข้อสอบ","quiz"],["review","คาบที่ทวนแล้ว","review"]]',
     '[["home","หน้าแรก","home"],["new","ข้อแต่ง (ใหม่)","new"],["old","ข้อจากโพย (เก่า)","old"],["quiz","สุ่มทำข้อสอบ","quiz"],["review","คาบที่ทวนแล้ว","review"]]'),
]
CSS_V3 = """
/* แถบล่าง 6 ปุ่ม */
.tr-bnav{grid-template-columns:repeat(6,minmax(0,1fr))}
@media (max-width:380px){.tr-bn{font-size:11px}.tr-main .tr-bn-ic{width:54px;height:54px;margin-top:-27px}}
</style>"""


def patch_v3(html):
    if MARK3 in html:
        return html
    for old, new in EDITS_V3:
        assert html.count(old) == 1, ("v3 anchor", old[:50], html.count(old))
        html = html.replace(old, new)
    k = html.index('<style id="tr-style">')
    e = html.index("</style>", k)
    return html[:e] + CSS_V3 + html[e + len("</style>"):]


def main(src, out):
    html = open(src, encoding="utf-8").read()
    if MARK in html:
        open(out, "w", encoding="utf-8").write(patch_v3(html))
        print("v1-2 already in; v3 applied")
        return
    for old, new in EDITS:
        assert html.count(old) == 1, ("anchor not unique/missing", old[:60], html.count(old))
        html = html.replace(old, new)
    a, b = html.index(OLD_START), html.index(OLD_END)
    html = html[:a] + NEW_RENDER_OLD + html[b:]
    assert html.count(HOME_ANCHOR) == 1 and html.count(TILES_END) == 1
    html = html.replace(HOME_ANCHOR, HOME_FUNC + HOME_ANCHOR)
    html = html.replace(TILES_END, TILES_END + "\n    h+=trWrongKw();")
    k = html.index('<style id="tr-style">')
    e = html.index("</style>", k)
    html = html[:e] + CSS + html[e + len("</style>"):]
    open(out, "w", encoding="utf-8").write(patch_v3(html))
    print("patched")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
