#!/usr/bin/env python3
"""คาบที่ทวนแล้ว: สุ่มข้อสอบของแต่ละวันที่ทวน (ผู้ใช้ขอ 9 พ.ย. 2569)

ตั้งค่าได้: ปีที่ออก (ทุกปี / 3 ปีล่าสุด / 5 ปีล่าสุด / เลือกเองทีละปี + ข้อฝึกเพิ่มที่ไม่ระบุปี) ·
Part (MCQ / MEQ / SAQ-OSCE เลือกได้หลายอัน) · จำนวนข้อต่อคาบ (ตั้งทุกคาบพร้อมกัน หรือปรับทีละคาบ)
ข้อสอบเก่า (มีปีที่ออก) ถูกเลือกก่อนข้อฝึกเพิ่ม · ชุดของแต่ละวันจำไว้ในเครื่อง (med421-drill-rvquiz)
คำตอบในชุดเก็บแยก (เริ่มสะอาด) และเขียนทับ state.answers ด้วย → นับในบัญชีตามปกติ

ใช้:  python3 ward_drill/patch_rvquiz.py ward_drill/index.html   (แก้ไฟล์เดิม · รันซ้ำได้)
"""
import sys

CSS = """/* ---------- สุ่มข้อสอบของวันที่ทวน ---------- */
.rqcfg .rqh{font-family:var(--mono);font-size:10.5px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-3);margin:16px 0 9px}
.rqcfg .rqh:first-child{margin-top:0}
.rqcfg .parts+.parts{margin-top:7px}
.rqlist{display:flex;flex-direction:column;gap:8px;margin:12px 0 4px}
.rqrow{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;padding:10px 12px;background:var(--surface-sunk);border-radius:var(--r-md)}
.rqname{flex:1 1 260px;min-width:0;font-size:14px;line-height:1.45}
.rqname b{font-weight:600}
.rqname span{display:block;font-size:12px;color:var(--ink-3)}
.rqstep{display:flex;align-items:center;gap:6px}
.rqstep .chip{padding:7px 13px;background:var(--surface)}
.rqstep .chip[aria-pressed="true"]{background:var(--accent)}
.rqval{font-family:var(--mono);font-size:14px;min-width:4.2em;text-align:center}
.rvday .reveal{white-space:normal}
"""

JS = r"""/* ---------- สุ่มข้อสอบของวันที่ทวน (ผู้ใช้ขอ 9 พ.ย. 2569) ----------
   ตั้งค่า: ปีที่ออก (ทุกปี / 3 ปีล่าสุด / 5 ปีล่าสุด / เลือกเอง + ข้อฝึกเพิ่ม) · Part · จำนวนข้อต่อคาบ
   ข้อสอบเก่า (มีปี) มาก่อนข้อฝึกเพิ่ม · ชุดของแต่ละวันเก็บในเครื่อง · คำตอบของชุดเก็บแยก (เริ่มสะอาด) และเขียนทับ state.answers */
var RQKEY="med421-drill-rvquiz";
var RQS={view:"",day:"",cfg:{years:"all",pick:[],x:true,parts:["MCQ","MEQ","SAQ"],def:5,n:{}},sets:{}};
try{var rq0=JSON.parse(localStorage.getItem(RQKEY)||"null");if(rq0&&typeof rq0==="object"){
  if(rq0.view==="cfg"||rq0.view==="set")RQS.view=rq0.view;if(typeof rq0.day==="string")RQS.day=rq0.day;
  var c0=rq0.cfg||{},C0=RQS.cfg;
  if(["all","last3","last5","pick"].indexOf(c0.years)>=0)C0.years=c0.years;
  if(Array.isArray(c0.pick))C0.pick=c0.pick.filter(function(y){return /^\d\d$/.test(y);});
  if(typeof c0.x==="boolean")C0.x=c0.x;
  if(Array.isArray(c0.parts))C0.parts=c0.parts.filter(function(p){return p==="MCQ"||p==="MEQ"||p==="SAQ";});
  if(typeof c0.def==="number")C0.def=c0.def;
  if(c0.n&&typeof c0.n==="object")Object.keys(c0.n).forEach(function(k){if(typeof c0.n[k]==="number")C0.n[k]=c0.n[k];});
  if(rq0.sets&&typeof rq0.sets==="object")Object.keys(rq0.sets).forEach(function(d){var s=rq0.sets[d];
    if(s&&Array.isArray(s.ids))RQS.sets[d]={ids:s.ids.filter(Array.isArray),at:String(s.at||""),desc:String(s.desc||""),ans:normA(s.ans)};});
}}catch(e){}
function rqKeep(){try{localStorage.setItem(RQKEY,JSON.stringify(RQS));}catch(e){}}
function rqOn(){return state.mode==="review"&&!!RQS.view&&RQS.day===RV.day;}
function rqIsStore(s){var S=RQS.sets[RQS.day];return !!(S&&s===S.ans);}
function rqUnits(d){return rvUnits().filter(function(u){return u.days.indexOf(d)>=0;});}
function rqAllYears(us){var ys={};us.forEach(function(u){Object.keys(rvMatrix(u)).forEach(function(y){if(y!=="x")ys[y]=1;});});
  return Object.keys(ys).sort().reverse();}
function rqYearSet(us){var C=RQS.cfg,all=rqAllYears(us),set={};
  (C.years==="last3"?all.slice(0,3):C.years==="last5"?all.slice(0,5):C.years==="pick"?C.pick:all).forEach(function(y){set[y]=1;});
  if(C.x)set.x=1;return set;}
function rqCands(u,yset){var mx=rvMatrix(u),seen={},ex=[],px=[];
  rvYears(mx).forEach(function(y){if(!yset[y])return;
    RV_PARTS.forEach(function(P){if(RQS.cfg.parts.indexOf(P.k)<0)return;
      (mx[y][P.k]||[]).forEach(function(e){if(seen[e.it.id])return;seen[e.it.id]=1;(y==="x"?px:ex).push({e:e,y:y,p:P.k});});});});
  return {ex:ex,px:px,n:ex.length+px.length};}
function rqN(u){var v=RQS.cfg.n[u.id];return typeof v==="number"?v:RQS.cfg.def;}
function rqTake(c,n){var k=n<0?c.n:Math.min(n,c.n);return qShuffle(c.ex.slice()).concat(qShuffle(c.px.slice())).slice(0,k);}
function rqDesc(us){var C=RQS.cfg,all=rqAllYears(us),L=function(a){return a.map(function(x){return "MED"+x;}).join(", ");};
  var y=C.years==="all"?"ทุกปี":C.years==="last3"?"3 ปีล่าสุด ("+L(all.slice(0,3))+")":C.years==="last5"?"5 ปีล่าสุด ("+L(all.slice(0,5))+")":
    (C.pick.length?L(C.pick.slice().sort().reverse()):"ไม่เลือกปี");
  return y+(C.x?" + ข้อฝึกเพิ่ม":"")+" · "+C.parts.map(rvPLabel).join(" / ");}
function rqOpen(d,view){RQS.day=d;RQS.view=view;RV.day=d;RV.lec="all";RV.list=0;RV.year="all";RV.part="all";
  rqKeep();rvSave();render();window.scrollTo({top:0});}
function rqDraw(d){var us=rqUnits(d),ys=rqYearSet(us),ids=[];
  us.forEach(function(u){rqTake(rqCands(u,ys),rqN(u)).forEach(function(c){ids.push([u.id,c.e.it.id,c.y,c.p]);});});
  RQS.sets[d]={ids:ids,at:new Date().toISOString(),desc:rqDesc(us),ans:{}};rqOpen(d,"set");}
function rqItems(){var S=RQS.sets[RQS.day];if(!S)return [];var um={};rvUnits().forEach(function(u){um[u.id]=u;});
  var out=[];S.ids.forEach(function(r){var u=um[r[0]];if(!u)return;
    var e=u.es.filter(function(x){return x.it.id===r[1];})[0];if(e)out.push({u:u,e:e,y:r[2],p:r[3]});});return out;}
function rqScore(){var S=RQS.sets[RQS.day],its=RQS.view==="set"?rqItems():[],d=0,r=0;
  its.forEach(function(x){var a=S&&S.ans[x.e.it.id];if(a){d++;if(a.ok)r++;}});
  var pct=d?Math.round(r/d*100):0;
  document.getElementById("sc-done").textContent=d;document.getElementById("sc-right").textContent=r;
  var acc=document.getElementById("sc-acc");acc.textContent=d?pct+"%":"—";acc.style.setProperty("--pct",pct);
  document.getElementById("railnote").innerHTML="<b>สุ่มข้อสอบของวัน"+esc(rvDate(RQS.day))+"</b> คะแนนด้านบนนับเฉพาะชุดที่สุ่มอยู่ · "+
    "คำตอบนับรวมกับโหมดอื่นและบันทึกในบัญชี · กด <b>1–5</b> เพื่อตอบข้อที่เห็นอยู่บนจอ";}
function rqBtn(label,cls,fn){var b=document.createElement("button");b.type="button";b.className=cls||"reveal";b.textContent=label;
  b.addEventListener("click",fn);return b;}
function rqChip(label,on,fn,dis){var b=document.createElement("button");b.type="button";b.className="chip";
  b.setAttribute("aria-pressed",String(!!on));b.textContent=label;if(dis){b.disabled=true;b.style.opacity=".45";}
  b.addEventListener("click",function(){fn();rqKeep();render();});return b;}
function rqBack(stream,extra){var bar=document.createElement("div");bar.className="rvback";
  bar.appendChild(rqBtn("← ภาพรวม "+rvDate(RQS.day),"ghost",function(){RQS.view="";rqKeep();render();window.scrollTo({top:0});}));
  (extra||[]).forEach(function(b){bar.appendChild(b);});stream.appendChild(bar);}
function renderRqCfg(stream){
  var d=RQS.day,us=rqUnits(d),C=RQS.cfg,all=rqAllYears(us),ys=rqYearSet(us);
  rqBack(stream,RQS.sets[d]?[rqBtn("กลับไปชุดที่สุ่มไว้","ghost",function(){rqOpen(d,"set");})]:[]);
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>สุ่มข้อสอบของวัน"+esc(rvDate(d,1))+"</h2><span class='meta'>"+us.length+" คาบ</span>";stream.appendChild(head);
  var c=document.createElement("section");c.className="item qzcard rqcfg";
  function h(t){var x=document.createElement("h4");x.className="rqh";x.textContent=t;c.appendChild(x);}
  function row(){var x=document.createElement("div");x.className="parts";c.appendChild(x);return x;}
  h("ปีที่ออก");var r1=row();
  [["all","ทุกปี"],["last3","3 ปีล่าสุด"],["last5","5 ปีล่าสุด"]].forEach(function(o){
    r1.appendChild(rqChip(o[1],C.years===o[0],function(){C.years=o[0];}));});
  var r2=row();
  all.forEach(function(y){r2.appendChild(rqChip("MED"+y,!!ys[y],function(){
    var cur=all.filter(function(z){return ys[z];}),i=cur.indexOf(y);if(i>=0)cur.splice(i,1);else cur.push(y);C.years="pick";C.pick=cur;}));});
  r2.appendChild(rqChip("ข้อฝึกเพิ่ม (ไม่ระบุปี)",C.x,function(){C.x=!C.x;}));
  h("Part");var r3=row();
  RV_PARTS.forEach(function(P){r3.appendChild(rqChip(P.label,C.parts.indexOf(P.k)>=0,function(){
    var i=C.parts.indexOf(P.k);if(i>=0)C.parts.splice(i,1);else C.parts.push(P.k);}));});
  h("จำนวนข้อต่อคาบ");var r4=row();
  [3,5,10,-1].forEach(function(n){r4.appendChild(rqChip(n<0?"ทุกคาบ: ทั้งหมด":"ทุกคาบ: "+n+" ข้อ",
    C.def===n&&us.every(function(u){return typeof C.n[u.id]!=="number";}),
    function(){C.def=n;us.forEach(function(u){delete C.n[u.id];});}));});
  var tot=0,list=document.createElement("div");list.className="rqlist";
  us.forEach(function(u){var cd=rqCands(u,ys),n=rqN(u),k=n<0?cd.n:Math.min(n,cd.n);tot+=k;
    var rw=document.createElement("div");rw.className="rqrow";
    rw.innerHTML="<div class='rqname'><b>"+esc(setLabel(u.set))+" · Lec "+esc(u.lec)+"</b> "+esc(u.title)+
      "<span>มีตามตัวกรอง "+cd.n+" ข้อ"+(cd.n?" · ข้อสอบเก่า "+cd.ex.length+" · ข้อฝึกเพิ่ม "+cd.px.length:"")+" · จะได้ "+k+" ข้อ</span></div>";
    var st=document.createElement("div");st.className="rqstep";
    st.appendChild(rqChip("−",false,function(){C.n[u.id]=Math.max(0,(n<0?cd.n:Math.min(n,cd.n))-1);},n===0));
    var val=document.createElement("b");val.className="rqval";val.textContent=n<0?"ทั้งหมด":String(n);st.appendChild(val);
    st.appendChild(rqChip("+",false,function(){C.n[u.id]=n+1;},n<0||n>=cd.n));
    st.appendChild(rqChip("ทั้งหมด",n<0,function(){C.n[u.id]=-1;}));
    rw.appendChild(st);list.appendChild(rw);});
  c.appendChild(list);
  var go=rqBtn("เริ่มสุ่ม "+tot+" ข้อ","reveal qzgo",function(){rqDraw(d);});go.disabled=!tot;go.style.marginTop="10px";c.appendChild(go);
  var nt=document.createElement("p");nt.className="qzinfo";
  nt.textContent=(tot?"":"ไม่มีข้อตามตัวกรอง — เลือกปีหรือ Part เพิ่ม · ")+"ข้อสอบเก่า (มีปีที่ออก) ถูกเลือกก่อนข้อฝึกเพิ่ม · ข้อที่ออกหลายปีนับครั้งเดียว · "+
    "ค่าที่ตั้งจำไว้ใช้กับวันอื่นด้วย · ชุดที่สุ่มเริ่มสะอาด คำตอบยังนับรวมในบัญชี";
  c.appendChild(nt);stream.appendChild(c);
}
function renderRqSet(stream){
  var d=RQS.day,S=RQS.sets[d],its=rqItems();
  rqBack(stream,[rqBtn("ปรับตั้งค่า","ghost",function(){rqOpen(d,"cfg");}),rqBtn("สุ่มชุดใหม่","ghost",function(){rqDraw(d);})]);
  if(!its.length){var em=document.createElement("p");em.className="empty";
    em.textContent="ชุดนี้ไม่มีข้อ — กด “ปรับตั้งค่า” แล้วเลือกปี / Part / จำนวนข้อใหม่";stream.appendChild(em);return;}
  var done=0,right=0,mc=0;
  its.forEach(function(x){if(x.e.it.choices){mc++;var a=S.ans[x.e.it.id];if(a){done++;if(a.ok)right++;}}});
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ชุดสุ่มของวัน"+esc(rvDate(d,1))+"</h2><span class='meta'>"+its.length+" ข้อ</span>";stream.appendChild(head);
  var info=document.createElement("p");info.className="oldnote wide";
  info.textContent=S.desc+" · ตอบแล้ว "+done+"/"+mc+" ข้อเลือกตอบ"+(its.length>mc?" · MEQ/SAQ "+(its.length-mc)+" ข้อ กดดูแนวคำตอบทีละข้อ":"");
  stream.appendChild(info);
  var lastU=null;
  its.forEach(function(x,i){
    if(x.u!==lastU){lastU=x.u;var n=its.filter(function(z){return z.u===x.u;}).length,h=document.createElement("div");h.className="rvunit";
      h.innerHTML="<h2>"+esc(setLabel(x.u.set))+" · Lec "+esc(x.u.lec)+" — "+esc(x.u.title)+"</h2><p>"+n+" ข้อในชุดนี้</p>";stream.appendChild(h);}
    var e=x.e,el;
    if(e.kind==="mcq")el=renderMCQ(e.it,i,S.ans);
    else if(e.kind==="oldc")el=renderOldChoice(e.it,e.g,S.ans);
    else el=rvRender(e,x.y,x.p);
    var ih=el.querySelector(".ihead");
    if(ih){ih.insertAdjacentHTML("afterbegin","<span class='tag qzno'>ข้อ "+(i+1)+"/"+its.length+"</span>");
      var t="";
      if(e.kind==="oldc")t+=x.y==="x"?"":yearBadge(e.it);
      if(x.y==="x")t+="<span class='tag'>ข้อฝึกเพิ่ม</span>";
      if(e.it.choices&&x.p!=="MCQ")t+="<span class='tag rvfrom'>จาก "+esc(rvPLabel(x.p))+" · เรียบเรียงเป็นตัวเลือก</span>";
      if(t)ih.insertAdjacentHTML("beforeend",t);}
    stream.appendChild(el);});
  if(mc&&done===mc){
    var pct=Math.round(right*100/mc),s=document.createElement("section"),by={},order=[],wrong=[];s.className="item qzcard";
    its.forEach(function(x){if(!x.e.it.choices)return;var a=S.ans[x.e.it.id],k=x.u.id;
      if(!by[k]){by[k]={u:x.u,n:0,r:0};order.push(k);}by[k].n++;if(a.ok)by[k].r++;else wrong.push(x);});
    s.innerHTML="<h3 class='topic'>สรุปชุดนี้: ถูก "+right+"/"+mc+" ข้อ ("+pct+"%)</h3><ul class='qzby'>"+order.map(function(k){var b=by[k];
      return "<li><b>"+esc(setLabel(b.u.set))+" Lec "+esc(b.u.lec)+"</b> "+esc(b.u.title)+" — "+b.r+"/"+b.n+"</li>";}).join("")+"</ul>";
    var acts=document.createElement("div");acts.className="railacts qzacts";
    acts.appendChild(rqBtn("สุ่มชุดใหม่","reveal",function(){rqDraw(d);}));
    if(wrong.length)acts.appendChild(rqBtn("ทำข้อที่ผิดอีกรอบ ("+wrong.length+")","reveal",function(){
      RQS.sets[d]={ids:wrong.map(function(x){return [x.u.id,x.e.it.id,x.y,x.p];}),at:new Date().toISOString(),desc:"ข้อที่ผิดจากชุดก่อน",ans:{}};
      rqKeep();render();window.scrollTo({top:0});}));
    s.appendChild(acts);stream.appendChild(s);}
}

"""

REPL = [
    ("/* ---------- ข้อสอบแยกปี ---------- */\n", "/* ---------- ข้อสอบแยกปี ---------- */\n" + CSS, ".rqcfg .rqh{"),
    ("/* ---------- actions ---------- */\n", JS + "/* ---------- actions ---------- */\n", "function renderRqCfg("),
    ("  if(!rvListing()){renderRvOverview(stream,us);return;}",
     '  if(rqOn()){if(RQS.view==="set")renderRqSet(stream);else renderRqCfg(stream);return;}\n'
     "  if(!rvListing()){renderRvOverview(stream,us);return;}", "if(rqOn()){if(RQS.view"),
    ("function rvScore(){\n", "function rvScore(){\n  if(rqOn()){rqScore();return;}\n", "if(rqOn()){rqScore();return;}"),
    ("function rvActive(){return rvUniq(rvBlocks())",
     'function rvActive(){if(rqOn())return RQS.view==="set"?rqItems().map(function(x){return x.e.it;}):[];return rvUniq(rvBlocks())',
     'if(rqOn())return RQS.view==="set"'),
    ("function rvGo(o){o=o||{};", 'function rvGo(o){o=o||{};RQS.view="";rqKeep();', 'function rvGo(o){o=o||{};RQS.view=""'),
    ("    dh.appendChild(go);stream.appendChild(dh);",
     "    dh.appendChild(go);\n"
     "    (function(d){var S0=RQS.sets[d];\n"
     "      if(S0){var a0=Object.keys(S0.ans).length;\n"
     "        dh.appendChild(rqBtn(\"ทำชุดสุ่มต่อ (\"+S0.ids.length+\" ข้อ · ตอบแล้ว \"+a0+\")\",\"reveal\",function(){rqOpen(d,\"set\");}));}\n"
     "      dh.appendChild(rqBtn(S0?\"สุ่มใหม่ / ตั้งค่า\":\"สุ่มข้อสอบ (เลือกปี · Part · จำนวนข้อต่อคาบ)\",\"reveal\",function(){rqOpen(d,\"cfg\");}));\n"
     "    })(x.d);\n"
     "    stream.appendChild(dh);", "rqOpen(d,\"cfg\");}));"),
    # ปุ่ม เฉลยทั้งหมด / เริ่มใหม่ ให้มีผลกับชุดสุ่มด้วย
    ('    else (it.questions||[{}]).forEach(function(_,qi){state.shown[it.id+"#"+qi]=1;});\n  });\n  save();render();',
     '    else (it.questions||[{}]).forEach(function(_,qi){state.shown[it.id+"#"+qi]=1;});\n  });\n'
     '  if(rqOn()&&RQS.sets[RQS.day]){var SA=RQS.sets[RQS.day].ans;activeItems().forEach(function(it){'
     'if(it.choices&&!SA[it.id])SA[it.id]={pick:it.answer,ok:true,auto:1};});rqKeep();}\n  save();render();',
     "var SA=RQS.sets[RQS.day].ans"),
    ('    (it.questions||[{}]).forEach(function(_,qi){delete state.shown[it.id+"#"+qi];});\n  });\n  save();render();',
     '    (it.questions||[{}]).forEach(function(_,qi){delete state.shown[it.id+"#"+qi];});\n  });\n'
     '  if(rqOn()&&RQS.sets[RQS.day]){var SR=RQS.sets[RQS.day].ans;activeItems().forEach(function(it){delete SR[it.id];});rqKeep();}\n  save();render();',
     "var SR=RQS.sets[RQS.day].ans"),
]
# คำตอบที่กดในชุดสุ่ม → บันทึกชุดด้วย (มี 2 ที่: renderMCQ และ renderOldChoice)
STORE_OLD = "if(store===quiz.ans)qSave();save();render();"
STORE_NEW = "if(store===quiz.ans)qSave();if(rqIsStore(store))rqKeep();save();render();"


def main():
    p = sys.argv[1]
    html = open(p, encoding="utf-8").read()
    for old, new, marker in REPL:
        if marker in html:
            continue
        c = html.count(old)
        assert c == 1, f"anchor found {c}x: {old[:70]!r}"
        html = html.replace(old, new)
    if STORE_NEW not in html:
        assert html.count(STORE_OLD) == 2, html.count(STORE_OLD)
        html = html.replace(STORE_OLD, STORE_NEW)
    open(p, "w", encoding="utf-8").write(html)
    print("patched", p)


if __name__ == "__main__":
    main()
