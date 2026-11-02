#!/usr/bin/env python3
"""เพิ่มแท็บ "ข้อสอบแยกปี" ใน Ward Drill — รวมทุกระบบในปีเดียว ไม่แยกเรื่อง

ใช้:  python3 ward_drill/patch_years.py ward_drill/index.html   (แก้ไฟล์เดิม · รันซ้ำได้)

ปีของแต่ละข้อมาจากฟิลด์ `years` ที่มีอยู่แล้ว (ดึงจาก ref/src ตอน build) ไม่ได้เพิ่มข้อใหม่
ลำดับในปีหนึ่ง: MCQ คลังข้อสอบเก่า (เรียงตาม src = รอบสอบ/เลขข้อ) → MCQ ข้อใหม่ที่อิงปีนั้น → MEQ → OSCE/SAQ
"""
import sys

CSS = """
/* ---------- ข้อสอบแยกปี ---------- */
.tag.sys{color:var(--ink-2);background:var(--surface-sunk);font-weight:600}
"""

RAIL = """    <div id="yablock" style="display:none">
      <h2>ปีที่ออก</h2>
      <div class="parts" id="yayear"></div>
      <h2 class="qzh">Part</h2>
      <div class="parts" id="yapart"></div>
      <h2 class="qzh">ที่มา</h2>
      <div class="parts" id="yasrc"></div>
      <p class="qzinfo" id="yainfo"></p>
    </div>
"""

JS = r"""
/* ---------- ข้อสอบแยกปี: รวมทุกระบบของปีเดียว ไม่แยกเรื่อง ---------- */
var YA={y:"",part:"all",src:"all"},YA_KEY="med421-drill-yearall",YA_CACHE=null,YA_STEP=60,YA_SHOW=60;
try{var ya0=JSON.parse(localStorage.getItem(YA_KEY)||"null");
  if(ya0&&typeof ya0==="object")["y","part","src"].forEach(function(f){if(typeof ya0[f]==="string")YA[f]=ya0[f];});}catch(e){}
function yaKeep(){try{localStorage.setItem(YA_KEY,JSON.stringify(YA));}catch(e){}}
function yaPart(p){p=String(p||"MCQ");return p==="MEQ"?"MEQ":(/SAQ|OSCE/i.test(p)?"SAQ":"MCQ");}
function yaAll(){
  if(YA_CACHE)return YA_CACHE;var out=[];
  SETS.forEach(function(s){var B=BANK[s.k];
    B.old.forEach(function(g){g.items.forEach(function(it){if(yrs(it).length)
      out.push({set:s.k,kind:it.choices?"oldc":"oldp",it:it,g:g,part:it.choices?"MCQ":yaPart(it.part),src:"old"});});});
    B.mcq.forEach(function(it){if(yrs(it).length)out.push({set:s.k,kind:"mcq",it:it,part:"MCQ",src:"new"});});
    B.meq.forEach(function(it){if(yrs(it).length)out.push({set:s.k,kind:"long",it:it,part:yaPart(it.part),src:"new"});});
  });
  return YA_CACHE=out;
}
function yaYears(){var c={};yaAll().forEach(function(e){yrs(e.it).forEach(function(y){c[y]=(c[y]||0)+1;});});
  return Object.keys(c).sort().reverse().map(function(y){return {y:y,n:c[y]};});}
function yaRank(e){return e.part==="MCQ"?(e.src==="old"?0:1):(e.part==="MEQ"?2:3);}
function yaOfYear(){var ys=yaYears();if(!ys.length)return [];
  if(!ys.some(function(o){return o.y===YA.y;}))YA.y=ys[0].y;
  return yaAll().filter(function(e){return yrs(e.it).map(String).indexOf(YA.y)>=0;});}
function yaList(){
  return yaOfYear().filter(function(e){return (YA.part==="all"||e.part===YA.part)&&(YA.src==="all"||e.src===YA.src);})
    .map(function(e,i){return {e:e,i:i};})
    .sort(function(a,b){return yaRank(a.e)-yaRank(b.e)||
      (a.e.src==="old"&&b.e.src==="old"?String(a.e.it.src||"").localeCompare(String(b.e.it.src||""),"th",{numeric:true}):0)||a.i-b.i;})
    .map(function(x){return x.e;});
}
function yaChips(id,opts,cur,pick){var el=document.getElementById(id);el.innerHTML="";
  opts.forEach(function(o){var b=document.createElement("button");b.type="button";b.className="chip";
    b.setAttribute("aria-pressed",String(cur===o.k));b.textContent=o.label+(o.n!=null?" · "+o.n:"");
    if(o.n===0&&cur!==o.k)b.disabled=true,b.style.opacity=".45";
    b.addEventListener("click",function(){pick(o.k);YA_SHOW=YA_STEP;yaKeep();render();window.scrollTo(0,0);});el.appendChild(b);});}
function buildYaRail(){
  var ys=yaYears(),yr=yaOfYear();
  yaChips("yayear",ys.map(function(o){return {k:o.y,label:"MED"+o.y,n:o.n};}),YA.y,function(k){YA.y=k;});
  function cnt(f){return yr.filter(f).length;}
  yaChips("yapart",[{k:"all",label:"ทั้งหมด",n:yr.length},
    {k:"MCQ",label:"MCQ",n:cnt(function(e){return e.part==="MCQ";})},
    {k:"MEQ",label:"MEQ",n:cnt(function(e){return e.part==="MEQ";})},
    {k:"SAQ",label:"OSCE / SAQ",n:cnt(function(e){return e.part==="SAQ";})}],YA.part,function(k){YA.part=k;});
  yaChips("yasrc",[{k:"all",label:"ทั้งหมด",n:yr.length},
    {k:"old",label:"ข้อสอบเก่า (เรียบเรียงจากโพย)",n:cnt(function(e){return e.src==="old";})},
    {k:"new",label:"ข้อใหม่ที่อิงข้อสอบปีนั้น",n:cnt(function(e){return e.src==="new";})}],YA.src,function(k){YA.src=k;});
  document.getElementById("yainfo").innerHTML="รวมทุกระบบของปีที่เลือก ไม่แยกเรื่อง · ปีดึงจากช่อง ref/ที่มาของแต่ละข้อ — ข้อที่เคยออกหลายปีจะอยู่ในทุกปีนั้น · ที่มาของข้อ (รอบสอบ เลขข้อ) ขึ้นหลังตอบ · แสดงทีละ "+YA_STEP+" ข้อ";
}
function yaEl(e){var el;
  if(e.kind==="mcq")el=renderMCQ(e.it,0);
  else if(e.kind==="long")el=renderLong(e.it);
  else if(e.kind==="oldc")el=renderOldChoice(e.it,e.g);
  else{el=document.createElement("article");el.className="item";
    el.innerHTML="<div class='ihead'><span class='qno'>"+esc(e.it.id||"")+"</span></div>"+
      "<p class='q'>"+inline(e.it.q||"")+"</p><p class='a'>"+inline(e.it.a||"")+"</p><p class='src'>"+inline(e.it.src||"")+"</p>";}
  var hd=el.querySelector(".ihead");
  if(hd){var t=document.createElement("span");t.className="tag sys";t.textContent=setLabel(e.set);
    hd.insertBefore(t,hd.children[1]||null);}
  return el;
}
function renderYa(stream){
  var list=yaList();
  if(!list.length){stream.innerHTML="<p class='empty'>ไม่มีข้อในเงื่อนไขนี้ — ลองเปลี่ยน Part หรือที่มา</p>";return;}
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ข้อสอบ MED"+esc(YA.y)+" · รวมทุกระบบ</h2><span class='meta'>"+list.length+" ข้อ</span>";
  stream.appendChild(head);
  var shown=0;
  [[0,"MCQ · คลังข้อสอบเก่า (เรียบเรียงจากโพย MED"+YA.y+")"],[1,"MCQ · ข้อใหม่ที่อิงข้อสอบ MED"+YA.y],
   [2,"MEQ"],[3,"OSCE / SAQ"]].forEach(function(g){
    var l=list.filter(function(e){return yaRank(e)===g[0];});if(!l.length||shown>=YA_SHOW)return;
    var h=document.createElement("div");h.className="part-head";
    h.innerHTML="<h2 style='font-size:16px'>"+esc(g[1])+"</h2><span class='meta'>"+l.length+" ข้อ</span>";
    stream.appendChild(h);
    l.forEach(function(e){if(shown>=YA_SHOW)return;shown++;stream.appendChild(yaEl(e));});
  });
  if(list.length>shown){var mb=document.createElement("button");mb.type="button";mb.className="ghost qzbtn";
    mb.textContent="แสดงเพิ่มอีก "+Math.min(YA_STEP,list.length-shown)+" ข้อ (เหลือ "+(list.length-shown)+" ข้อ)";
    mb.addEventListener("click",function(){var y=window.scrollY;YA_SHOW+=YA_STEP;render();window.scrollTo(0,y);});
    stream.appendChild(mb);}
}
"""

JS_SCORE = r"""  if(state.mode==="yearall"){var yl=yaList().filter(function(e){return e.it.choices;}),yd=0,yr=0;
    yl.forEach(function(e){var a=state.answers[e.it.id];if(a){yd++;if(a.ok)yr++;}});
    var yp=yd?Math.round(yr/yd*100):0;
    document.getElementById("sc-done").textContent=yd;document.getElementById("sc-right").textContent=yr;
    var ya=document.getElementById("sc-acc");ya.textContent=yd?yp+"%":"—";ya.style.setProperty("--pct",yp);
    document.getElementById("railnote").innerHTML="<b>ข้อสอบ MED"+esc(YA.y)+"</b> MCQ ที่ทำได้ "+yl.length+" ข้อ · คะแนนด้านบนนับเฉพาะ MCQ ในตัวกรองที่เลือก · กด <b>1–5</b> เพื่อตอบข้อที่เห็นอยู่บนจอ";
    return;}
"""

REPL = [
    ("@media print{", CSS.lstrip("\n") + "@media print{", ".tag.sys{"),
    ('{k:"pic",label:"ข้อสอบมีรูป"}', '{k:"yearall",label:"ข้อสอบแยกปี"},{k:"pic",label:"ข้อสอบมีรูป"}', 'k:"yearall"'),
    ("/* ---------- ข้อสอบที่เป็นรูป: ฟิลด์ img = [{src, cap}] ---------- */",
     JS.strip("\n") + "\n/* ---------- ข้อสอบที่เป็นรูป: ฟิลด์ img = [{src, cap}] ---------- */", "function renderYa("),
    ('    pic:picItems("all").length,', '    pic:picItems("all").length,\n    yearall:yaAll().length,', "yearall:yaAll().length"),
    ('pc=state.mode==="pic";', 'pc=state.mode==="pic",ym=state.mode==="yearall";', 'ym=state.mode==="yearall"'),
    ('style.display=(qz||rv||pc)?"none":"";', 'style.display=(qz||rv||pc||ym)?"none":"";\n'
     '  document.getElementById("yablock").style.display=ym?"":"none";\n  if(ym)buildYaRail();', "if(ym)buildYaRail();"),
    ("(rv||pc||(state.mode", "(rv||pc||ym||(state.mode", "(rv||pc||ym||"),
    ("  else if(pc)renderPic(stream);\n", "  else if(pc)renderPic(stream);\n  else if(ym)renderYa(stream);\n", "else if(ym)renderYa(stream);"),
    ('  if(state.mode==="pic")return picItems()',
     '  if(state.mode==="yearall")return yaList().map(function(e){return e.it;});\n  if(state.mode==="pic")return picItems()',
     'if(state.mode==="yearall")return yaList()'),
    ('  if(state.mode==="pic"){var pl=picItems()', JS_SCORE + '  if(state.mode==="pic"){var pl=picItems()', 'if(state.mode==="yearall"){var yl'),
    ('    <div id="picblock" style="display:none">', RAIL + '    <div id="picblock" style="display:none">', 'id="yablock"'),
    # คลิกแท็บระบบระหว่างอยู่ในโหมดแยกปี → กลับไป "ข้อสอบใหม่" ของระบบนั้น
    ('if(k===state.set&&state.mode!=="review")return;if(state.mode==="review")state.mode="new";',
     'if(k===state.set&&state.mode!=="review"&&state.mode!=="yearall")return;if(state.mode==="review"||state.mode==="yearall")state.mode="new";',
     'state.mode!=="yearall")return;'),
    # ลิงก์ตรง #year หรือ #year-35
    ('  if(h==="pic"){', '  if(/^year(-\\d\\d)?$/.test(h)){state.mode="yearall";var ym0=h.match(/\\d\\d/);if(ym0)YA.y=ym0[0];yaKeep();save();return true;}\n  if(h==="pic"){',
     "state.mode=\"yearall\";var ym0"),
    ("อยู่ในแท็บ “ข้อสอบมีรูป”</p>", "อยู่ในแท็บ “ข้อสอบมีรูป” · ทำข้อสอบทีละปี (รวมทุกระบบ) ได้ที่แท็บ “ข้อสอบแยกปี”</p>", "แท็บ “ข้อสอบแยกปี”"),
]


def main():
    p = sys.argv[1]
    html = open(p, encoding="utf-8").read()
    for old, new, marker in REPL:
        if marker in html:
            continue
        c = html.count(old)
        assert c == 1, f"anchor found {c}x: {old[:70]!r}"
        html = html.replace(old, new)
    open(p, "w", encoding="utf-8").write(html)
    print("patched", p)


if __name__ == "__main__":
    main()
