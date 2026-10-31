#!/usr/bin/env python3
"""
patch_drill_review.py — โหมด "คาบที่ทวนแล้ว" ใน MED421 Ward Drill

    python3 dashboard/patch_drill_review.py <drill.html> <out.html> [--edits edits.json]

รับรายการคาบที่ทวนแล้วจาก Lecture Dashboard ผ่านลิงก์ `#review~<ชุด>-<lec>_<รอบ>~…`
(ปุ่ม "ฝึกข้อสอบคาบที่ทวนแล้ว" ใน dashboard — patch_dash_review.py) แล้วรวมข้อสอบของแต่ละคาบ
แยกตามปีที่ออก (MED28–MED35) → MCQ / MEQ / SAQ·OSCE

- ข้อของคาบ = คลังข้อสอบเก่า + MCQ ใหม่ + MEQ/OSCE ที่ lec ตรงกัน
- ปีที่ออกใช้ฟิลด์ `years` ที่ build.py ดึงจาก ref/src อยู่แล้ว
- ส่วนของข้อสอบในปีนั้น (MCQ/MEQ/SAQ) อ่านจากข้อความ src/ref ช่วงที่ตามหลัง "MEDxx"
  (ไม่ระบุ = MCQ) · MEQ/OSCE ใหม่ใช้ part ของข้อเอง · ข้อที่ไม่มีปี = "ข้อฝึกเพิ่ม"
- รายการคาบเก็บใน localStorage `med421-drill-reviewed` และในบัญชี `data/users/<id>/drill-reviewed`
  = {keys:[{k:"chest-03", n:2}], at:"ISO"} (หน้า drill ต้องมี capabilities {db:{}, user:{}} อยู่แล้ว)
- คำตอบใช้ state.answers / state.shown เดิม จึงนับรวมกับโหมดอื่นและซิงก์เข้าบัญชีตามปกติ

รันได้กับหน้าที่ยังไม่แพตช์เท่านั้น (ทุก anchor ต้องเจอครั้งเดียว) · --edits เขียนคู่ old/new
ไว้ส่งให้ edit_version ของ artifact ได้ตรง ๆ
"""
import json, sys

CSS_ANCHOR = ".foot b{color:var(--ink-2)}\n"
CSS = r"""
/* ---------- คาบที่ทวนแล้ว (โหมด review) ---------- */
.rvcard .topic{margin-bottom:2px}
.rvmx{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 14px}
.rvmx th,.rvmx td{border-bottom:1px solid var(--rule);padding:6px 6px;text-align:center}
.rvmx th{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.rvmx th:first-child,.rvmx td:first-child{text-align:start;white-space:nowrap}
.rvmx td:first-child{font-weight:600;color:var(--ink-2)}
.rvmx .none{color:var(--ink-3);opacity:.6}
.rvcell{appearance:none;border:1px solid var(--rule-strong);background:none;color:var(--accent-ink);font:inherit;
  font-family:var(--mono);font-size:12px;border-radius:999px;padding:3px 11px;cursor:pointer;min-width:52px}
.rvcell:hover{border-color:var(--accent);background:var(--accent-soft)}
.rvcell.full{background:var(--ok-soft);border-color:transparent;color:var(--ok)}
.rvcell:active{transform:scale(.96)}
.rvacts{display:flex;flex-wrap:wrap;gap:8px}
.rvy{margin-top:10px;padding-top:14px;border-top:2px solid var(--accent)}
.rvsub{display:flex;align-items:baseline;gap:10px;padding:2px 4px}
.rvsub h3{font-size:15px;font-weight:700;color:var(--accent-ink)}
.rvsub .meta{font-family:var(--mono);font-size:11px;color:var(--ink-3)}
.rvunit{background:var(--accent-soft);color:var(--accent-ink);border-radius:var(--r-lg);padding:14px 18px}
.rvunit h2{font-size:19px;font-weight:700}
.rvunit p{margin:4px 0 0;font-size:12.5px}
.tag.rvfrom{color:var(--miss);background:var(--miss-soft)}
.rvinfo{margin:10px 0 0;font-size:12.5px;color:var(--ink-3);line-height:1.6}
.rvinfo a{color:var(--accent-ink)}
"""

MODES_OLD = '{k:"quiz",label:"สุ่มทำข้อสอบ"}];'
MODES_NEW = '{k:"quiz",label:"สุ่มทำข้อสอบ"},{k:"review",label:"คาบที่ทวนแล้ว"}];'

RAIL_OLD = '<p class="qzinfo" id="qzinfo"></p>\n    </div>\n'
RAIL_NEW = RAIL_OLD + """    <div id="rvblock" style="display:none">
      <h2>คาบที่ทวนแล้ว</h2>
      <div class="lecs" id="rvlecs"></div>
      <div id="rvfilters">
        <h2 class="qzh">Part</h2>
        <div class="parts" id="rvpart"></div>
        <h2 class="qzh">ปีที่ออก</h2>
        <div class="parts" id="rvyear"></div>
      </div>
      <p class="rvinfo" id="rvinfo"></p>
    </div>
"""

CONNECT_OLD = 'SYNC.ref.onSnapshot(onSnap,function(e){if(e&&e.code==="revoked"){SYNC.mode="local";renderSync();}});'
CONNECT_NEW = CONNECT_OLD + '\n      rvConnect(db,uid);'

SCORE_OLD = 'function updateScore(){\n  if(state.mode==="quiz"){'
SCORE_NEW = 'function updateScore(){\n  if(state.mode==="review"){rvScore();return;}\n  if(state.mode==="quiz"){'

SETBAR_OLD = 'if(k===state.set)return;state.set=k;state.lec="all";save();render();'
SETBAR_NEW = 'if(k===state.set&&state.mode!=="review")return;if(state.mode==="review")state.mode="new";state.set=k;state.lec="all";save();render();'

MCOUNT_OLD = 'hot:hotList(state.set).length};\n  if(!mcounts[state.mode]&&state.mode!=="quiz"){state.mode="new";save();}'
MCOUNT_NEW = ('hot:hotList(state.set).length,\n    review:rvUnits().length};\n'
              '  if(!mcounts[state.mode]&&state.mode!=="quiz"&&state.mode!=="review"){state.mode="new";save();}')

MFILTER_OLD = 'return m.k==="new"||m.k==="quiz"||mcounts[m.k]>0;'
MFILTER_NEW = 'return m.k==="new"||m.k==="quiz"||m.k==="review"||mcounts[m.k]>0;'

RAILSHOW_OLD = ('var qz=state.mode==="quiz";\n'
                '  document.getElementById("lecbar").parentNode.style.display=qz?"none":"";\n'
                '  document.getElementById("quizblock").style.display=qz?"":"none";\n'
                '  if(qz)buildQuizRail();\n'
                '  var showBtns=!qz&&(')
RAILSHOW_NEW = ('var qz=state.mode==="quiz",rv=state.mode==="review";\n'
                '  document.getElementById("lecbar").parentNode.style.display=(qz||rv)?"none":"";\n'
                '  document.getElementById("quizblock").style.display=qz?"":"none";\n'
                '  document.getElementById("rvblock").style.display=rv?"":"none";\n'
                '  if(rv)document.getElementById("partblock").style.display="none";\n'
                '  if(qz)buildQuizRail();\n'
                '  if(rv)buildRvRail();\n'
                '  var showBtns=!qz&&(rv||')

STREAM_OLD = '  if(qz)renderQuiz(stream);\n'
STREAM_NEW = '  if(qz)renderQuiz(stream);\n  else if(rv)renderReview(stream);\n'

ACTIVE_OLD = 'function activeItems(){\n  if(state.mode==="new")return filtered();'
ACTIVE_NEW = 'function activeItems(){\n  if(state.mode==="review")return rvActive();\n  if(state.mode==="new")return filtered();'

HASH_OLD = 'function applyHash(){\n  var h=String(location.hash||"").replace(/^#/,"");\n  if(!h)return false;\n'
HASH_NEW = HASH_OLD + '  if(h==="review"||/^review~/.test(h)){rvFromHash(h);return true;}\n'

JS_ANCHOR = '/* ---------- actions ---------- */\n'
JS = r"""/* ---------- คาบที่ทวนแล้ว (โหมด review) ----------
   รายการคาบมาจาก Lecture Dashboard ผ่านลิงก์ #review~<ชุด>-<lec>_<รอบที่ทวน>~… (ปุ่ม "ฝึกข้อสอบคาบที่ทวนแล้ว")
   เก็บในเครื่อง (med421-drill-reviewed) และในบัญชี data/users/<id>/drill-reviewed = {keys:[{k,n}], at}
   ข้อของคาบ = คลังเก่า + MCQ ใหม่ + MEQ/OSCE ของ lec นั้น · แยกตามปีที่ออก (years) → MCQ / MEQ / SAQ·OSCE
   ส่วนของข้อสอบในปีนั้นอ่านจาก src/ref ช่วงที่ตามหลัง MEDxx (ไม่ระบุ = MCQ) · ข้อที่ไม่มีปี = ข้อฝึกเพิ่ม (x) */
var DASH="https://claude.ai/artifact/8ir2xCgMKC7Fn4MiE2a5AV";
var RVKEY="med421-drill-reviewed";
var RV_PARTS=[{k:"MCQ",label:"MCQ"},{k:"MEQ",label:"MEQ"},{k:"SAQ",label:"SAQ / OSCE"}];
var RV={keys:[],at:"",lec:"all",part:"all",year:"all"};
var RVS={ref:null,busy:0,sent:""};
function rvClean(a){var out=[],seen={};(Array.isArray(a)?a:[]).forEach(function(x){
  var k=x&&typeof x==="object"?x.k:x,n=x&&typeof x==="object"?x.n:0;
  if(typeof k!=="string"||!/^[A-Za-z0-9]+(-[A-Za-z0-9.]+)?$/.test(k)||seen[k])return;seen[k]=1;
  out.push({k:k,n:Math.max(0,Math.min(99,Math.floor(Number(n)||0)))});});return out.slice(0,150);}
try{var rr=JSON.parse(localStorage.getItem(RVKEY)||"null");if(rr&&typeof rr==="object"){
  RV.keys=rvClean(rr.keys);RV.at=typeof rr.at==="string"?rr.at:"";
  ["lec","part","year"].forEach(function(f){if(typeof rr[f]==="string")RV[f]=rr[f];});}}catch(e){}
function rvKeep(){try{localStorage.setItem(RVKEY,JSON.stringify(RV));}catch(e){}}
function rvSave(){rvKeep();rvWrite();}
function rvBody(){return JSON.stringify({keys:RV.keys,at:RV.at});}
function rvWrite(){
  if(!RVS.ref||RVS.busy||!RV.at)return;
  var b=rvBody();if(b===RVS.sent)return;
  RVS.busy=1;
  RVS.ref.set(JSON.parse(b)).then(function(){RVS.busy=0;RVS.sent=b;rvWrite();},function(){RVS.busy=0;});
}
function rvConnect(db,uid){
  RVS.ref=db.doc("data/users/"+uid+"/drill-reviewed");
  RVS.ref.onSnapshot(function(snap){
    var d=snap.exists?snap.data():null,at=d&&typeof d.at==="string"?d.at:"";
    if(d)RVS.sent=JSON.stringify({keys:rvClean(d.keys),at:at});
    if(at>RV.at){RV.keys=rvClean(d.keys);RV.at=at;RVU=null;rvKeep();render();}
    else if(RV.at>at)rvWrite();
  },function(){});
}
/* #review~chest-03_2~cardio-13_1 · #review เฉย ๆ = เปิดโหมดนี้ด้วยรายการเดิม */
function rvFromHash(h){
  var toks=h.split("~").slice(1),keys=[];
  toks.forEach(function(t){var m=t.match(/^([A-Za-z0-9]+(?:-[A-Za-z0-9.]+)?)(?:_(\d+))?$/);if(m)keys.push({k:m[1],n:Number(m[2]||0)});});
  keys=rvClean(keys);
  if(toks.length&&JSON.stringify(keys)!==JSON.stringify(RV.keys)){
    RV.keys=keys;RV.at=new Date().toISOString();RV.lec="all";RV.part="all";RV.year="all";RVU=null;}
  state.mode="review";save();rvSave();
}
function rvPartIn(t){t=String(t||"");
  return /\bMEQ\b/i.test(t)?"MEQ":/\b(SAQ|OSCE)\b/i.test(t)?"SAQ":/\bMCQ\b/i.test(t)?"MCQ":"";}
function rvE(e){
  var it=e.it,ys=yrs(it).map(String),own=e.kind==="long"?(it.part==="MEQ"?"MEQ":"SAQ"):"";
  var txt=e.kind==="mcq"?(it.ref||[]).join(" / "):e.kind==="long"?"":String(it.src||"");
  var all=own||rvPartIn(txt)||"MCQ",hits=[],re=/MED\s*(\d{2})/g,m;
  if(!own)while((m=re.exec(txt)))hits.push({y:m[1],i:m.index});
  e.by={};
  ys.forEach(function(y){var p=own;
    hits.forEach(function(h,j){if(!p&&h.y===y)p=rvPartIn(txt.slice(h.i,j+1<hits.length?hits[j+1].i:txt.length));});
    e.by[y]=p||all;});
  e.ys=ys;e.fmt=own||"MCQ";
  return e;
}
function rvEntries(s,lec){var es=[];
  BANK[s].old.forEach(function(g){g.items.forEach(function(it){
    if((it.lec||g.lec)===lec)es.push(rvE({it:it,g:g,kind:it.choices?"oldc":"oldp"}));});});
  BANK[s].mcq.forEach(function(it){if(it.lec===lec)es.push(rvE({it:it,kind:"mcq"}));});
  BANK[s].meq.forEach(function(it){if(it.lec===lec)es.push(rvE({it:it,kind:"long"}));});
  return es;
}
function rvLecsOf(s){var seen={},out=[];function add(l){if(l&&!seen[l]){seen[l]=1;out.push(l);}}
  BANK[s].old.forEach(function(g){add(g.lec);g.items.forEach(function(it){add(it.lec);});});
  newItems(s).forEach(function(it){add(it.lec);});return out;}
var RVU=null,RVUK="";
function rvUnits(){
  var key=JSON.stringify(RV.keys);if(RVU&&RVUK===key)return RVU;
  var out=[],seen={};out.miss=0;
  RV.keys.forEach(function(x){
    var i=x.k.indexOf("-"),s=i<0?x.k:x.k.slice(0,i),l=i<0?"":x.k.slice(i+1),hit=0;
    if(!BANK[s]){out.miss++;return;}
    (l?[l]:rvLecsOf(s)).forEach(function(lec){
      var id=s+"-"+lec;if(seen[id]){hit=1;return;}
      var es=rvEntries(s,lec);if(!es.length)return;
      seen[id]=1;hit=1;
      var e0=es.filter(function(e){return e.it.lecture||(e.g&&e.g.lecture);})[0];
      out.push({id:id,set:s,lec:lec,n:x.n,es:es,name:e0?(e0.it.lecture||e0.g.lecture):"Lec "+lec});
    });
    if(!hit)out.miss++;
  });
  RVU=out;RVUK=key;return out;
}
function rvMatrix(u){if(u.mx)return u.mx;var mx={};
  function put(y,p,e){var r=mx[y]=mx[y]||{};(r[p]=r[p]||[]).push(e);}
  u.es.forEach(function(e){if(e.ys.length)e.ys.forEach(function(y){put(y,e.by[y],e);});else put("x",e.fmt,e);});
  return u.mx=mx;}
function rvYears(mx){return Object.keys(mx).filter(function(y){return y!=="x";}).sort().reverse().concat(mx.x?["x"]:[]);}
function rvYLabel(y){return y==="x"?"ข้อฝึกเพิ่ม (ไม่ระบุปีที่ออก)":"MED"+y;}
function rvPLabel(p){return p==="SAQ"?"SAQ / OSCE":p;}
function rvDone(e){var it=e.it;
  if(it.choices)return !!state.answers[it.id];
  return (it.questions||[{}]).some(function(_,qi){return state.shown[it.id+"#"+qi];});}
function rvSel(){var us=rvUnits();return RV.lec==="all"?us:us.filter(function(u){return u.id===RV.lec;});}
/* ข้อที่แสดงตามตัวกรอง: [{u, y, p, list}] */
function rvBlocks(){var out=[];
  rvSel().forEach(function(u){var mx=rvMatrix(u);
    rvYears(mx).forEach(function(y){if(RV.year!=="all"&&RV.year!==y)return;
      RV_PARTS.forEach(function(P){if(RV.part!=="all"&&RV.part!==P.k)return;
        var list=mx[y][P.k];if(list&&list.length)out.push({u:u,y:y,p:P.k,list:list});});});});
  return out;}
function rvUniq(blocks){var seen={},out=[];
  blocks.forEach(function(b){b.list.forEach(function(e){if(!seen[e.it.id]){seen[e.it.id]=1;out.push(e);}});});return out;}
function rvActive(){return rvUniq(rvBlocks()).map(function(e){return e.it;});}
function rvScore(){
  var es=RV.lec==="all"&&RV.year==="all"&&RV.part==="all"?rvUniq(rvUnits().map(function(u){return {list:u.es};})):rvUniq(rvBlocks());
  var done=0,right=0;
  es.forEach(function(e){var a=e.it.choices&&state.answers[e.it.id];if(a){done++;if(a.ok)right++;}});
  var pct=done?Math.round(right/done*100):0;
  document.getElementById("sc-done").textContent=done;document.getElementById("sc-right").textContent=right;
  var acc=document.getElementById("sc-acc");acc.textContent=done?pct+"%":"—";acc.style.setProperty("--pct",pct);
  document.getElementById("railnote").innerHTML="<b>คาบที่ทวนแล้ว</b> คะแนนด้านบนนับเฉพาะข้อเลือกตอบที่กำลังดู · "+
    "ข้อเดียวกันที่ออกหลายปีจะอยู่ในทุกปีที่ออก ตอบครั้งเดียวนับครั้งเดียว · คำตอบนับรวมกับโหมดอื่นและบันทึกในบัญชีของคุณ";
}
function rvChips(id,opts,cur,pick){
  var el=document.getElementById(id);el.innerHTML="";
  opts.forEach(function(o){var b=document.createElement("button");b.type="button";b.className="chip";
    b.setAttribute("aria-pressed",String(o.k===cur));b.textContent=o.label;
    b.addEventListener("click",function(){pick(o.k);rvSave();render();});el.appendChild(b);});
}
function rvGo(lec,year,part){RV.lec=lec;RV.year=year||"all";RV.part=part||"all";rvSave();render();window.scrollTo({top:0});}
function buildRvRail(){
  var us=rvUnits(),el=document.getElementById("rvlecs");el.innerHTML="";
  if(RV.lec!=="all"&&!us.some(function(u){return u.id===RV.lec;}))RV.lec="all";
  function lb(id,slot,nm,ct){var b=document.createElement("button");b.type="button";b.className="lec";
    b.setAttribute("aria-pressed",String(RV.lec===id));
    b.innerHTML="<span class='slot'>"+esc(slot)+"</span><span class='nm'>"+esc(nm)+"</span><span class='ct'>"+ct+"</span>";
    b.addEventListener("click",function(){rvGo(id);});el.appendChild(b);}
  lb("all","ทั้ง","ภาพรวมทุกคาบ",us.length);
  us.forEach(function(u){lb(u.id,setLabel(u.set)+" "+u.lec,shortName(u.name),u.es.length);});
  rvChips("rvpart",[{k:"all",label:"ทั้งหมด"}].concat(RV_PARTS),RV.part,function(k){RV.part=k;});
  var ys={};rvSel().forEach(function(u){Object.keys(rvMatrix(u)).forEach(function(y){ys[y]=1;});});
  if(RV.year!=="all"&&!ys[RV.year])RV.year="all";
  var yo=[{k:"all",label:"ทุกปี"}].concat(Object.keys(ys).filter(function(y){return y!=="x";}).sort().reverse()
    .map(function(y){return {k:y,label:"MED"+y};})).concat(ys.x?[{k:"x",label:"ข้อฝึกเพิ่ม"}]:[]);
  rvChips("rvyear",yo,RV.year,function(k){RV.year=k;});
  document.getElementById("rvfilters").style.display=us.length?"":"none";
  var at=RV.at?new Date(RV.at):null;
  document.getElementById("rvinfo").innerHTML=(at&&!isNaN(at)?"รายการคาบอัปเดตจาก Lecture Dashboard เมื่อ "+
    esc(at.toLocaleDateString("th-TH",{day:"numeric",month:"short"})+" "+at.toLocaleTimeString("th-TH",{hour:"2-digit",minute:"2-digit"}))+" · ":"")+
    "ทวนคาบใหม่แล้ว กดปุ่ม <b>ฝึกข้อสอบคาบที่ทวนแล้ว</b> ใน <a href='"+DASH+"' target='_blank' rel='noopener'>Dashboard</a> อีกครั้งเพื่ออัปเดต";
}
function rvRender(e,y,p){
  var el;
  if(e.kind==="mcq")el=renderMCQ(e.it,0);
  else if(e.kind==="long")el=renderLong(e.it);
  else if(e.kind==="oldc")el=renderOldChoice(e.it,e.g);
  else{el=document.createElement("article");el.className="item";
    el.innerHTML="<div class='ihead'><span class='qno'>"+esc(e.it.id||"")+"</span><span class='tag old'>ข้อสอบเก่า</span></div>"+
      "<p class='q'>"+inline(e.it.q||"")+"</p><p class='a'>"+inline(e.it.a||"")+"</p><p class='src'>"+inline(e.it.src||"")+"</p>";}
  el.id="it-"+e.it.id+"--"+y;   /* ข้อเดียวกันอยู่ได้หลายปี — id ไม่ซ้ำ ตอบแล้วไม่กระโดดไปปีอื่น */
  var ih=el.querySelector(".ihead");
  if(ih){var t="";
    if(e.kind==="oldc"||e.kind==="oldp")t+=yearBadge(e.it);
    if(p!=="MCQ"&&e.it.choices)t+="<span class='tag rvfrom'>จาก "+esc(rvPLabel(p))+" · เรียบเรียงเป็นตัวเลือก</span>";
    if(t)ih.insertAdjacentHTML("beforeend",t);}
  return el;
}
function rvCount(list){var d=0;list.forEach(function(e){if(rvDone(e))d++;});return d;}
function renderReview(stream){
  var us=rvUnits();
  if(!us.length){
    var c=document.createElement("section");c.className="item qzcard";
    c.innerHTML="<h3 class='topic'>ยังไม่มีรายการคาบที่ทวนแล้ว</h3>"+
      "<p class='stem'>เปิด <a href='"+DASH+"' target='_blank' rel='noopener'>MED421 Lectures (Dashboard)</a> แล้วกดปุ่ม "+
      "<b>ฝึกข้อสอบคาบที่ทวนแล้ว</b> ที่แผงด้านข้าง — Drill จะรวมข้อสอบของทุกคาบที่คุณกดทวนไว้ แยกตามปีที่ออก และแยก MCQ / MEQ / SAQ ให้</p>"+
      (RV.keys.length?"<p class='lecline'>คาบในรายการยังไม่มีข้อสอบใน Drill</p>":"");
    stream.appendChild(c);return;}
  if(RV.lec==="all"&&RV.year==="all"&&RV.part==="all"){renderRvOverview(stream,us);return;}
  var blocks=rvBlocks();
  if(!blocks.length){stream.innerHTML="<p class='empty'>ไม่มีข้อในเงื่อนไขนี้ — ลองเลือกปีหรือ Part อื่น</p>";return;}
  var lastU=null,lastY=null;
  blocks.forEach(function(b){
    if(b.u!==lastU){lastU=b.u;lastY=null;
      var meta=LEC[b.u.lec]||{},t=teacher(b.u.name),h=document.createElement("div");h.className="rvunit";
      h.innerHTML="<h2>"+esc(setLabel(b.u.set))+" · Lec "+esc(b.u.lec)+" — "+esc(shortName(b.u.name))+"</h2>"+
        "<p>"+[t,meta.d,b.u.n?"ทวนแล้ว "+b.u.n+" รอบ":""].filter(Boolean).map(esc).join(" · ")+"</p>";
      stream.appendChild(h);}
    if(b.y!==lastY){lastY=b.y;
      var mx=rvMatrix(b.u)[b.y],yh=document.createElement("div");yh.className="part-head rvy";
      yh.innerHTML="<h2>"+esc(rvYLabel(b.y))+"</h2><span class='meta'>"+RV_PARTS.filter(function(P){return mx[P.k];})
        .map(function(P){return esc(P.label)+" "+mx[P.k].length;}).join(" · ")+"</span>";
      stream.appendChild(yh);}
    var sh=document.createElement("div");sh.className="rvsub";
    sh.innerHTML="<h3>"+esc(rvPLabel(b.p))+"</h3><span class='meta'>"+b.list.length+" ข้อ · ทำแล้ว "+rvCount(b.list)+"</span>";
    stream.appendChild(sh);
    b.list.forEach(function(e){stream.appendChild(rvRender(e,b.y,b.p));});
  });
}
function renderRvOverview(stream,us){
  var total=rvUniq(us.map(function(u){return {list:u.es};})).length;
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ข้อสอบของคาบที่ทวนแล้ว</h2><span class='meta'>"+us.length+" คาบ · "+total+" ข้อ</span>";
  stream.appendChild(head);
  var info=document.createElement("p");info.className="oldnote wide";
  info.textContent="เรียงตามคาบที่ทวนล่าสุด · กดตัวเลขในตารางเพื่อทำเฉพาะปีและ Part นั้น (ตัวเลข = ทำแล้ว/ทั้งหมด) · "+
    "ส่วนของข้อสอบ (MCQ/MEQ/SAQ) ดูจากที่มาที่โพยจดไว้ ข้อจาก MEQ/SAQ ที่เรียบเรียงเป็นตัวเลือกมีป้ายบอก"+
    (us.miss?" · มี "+us.miss+" คาบที่ยังไม่มีข้อสอบใน Drill":"");
  stream.appendChild(info);
  us.forEach(function(u){
    var mx=rvMatrix(u),meta=LEC[u.lec]||{},t=teacher(u.name);
    var sec=document.createElement("article");sec.className="item rvcard";
    var h="<div class='ihead'><span class='qno'>Lec "+esc(u.lec)+"</span><span class='tag'>"+esc(setLabel(u.set))+"</span>"+
      (meta.d?"<span class='tag'>"+esc(meta.d)+"</span>":"")+(u.n?"<span class='tag yr'>ทวนแล้ว "+u.n+" รอบ</span>":"")+"</div>"+
      "<h3 class='topic'>"+esc(shortName(u.name))+"</h3>"+(t?"<p class='lecline'>"+esc(t)+"</p>":"")+
      "<div class='tablewrap'><table class='rvmx'><thead><tr><th>ปีที่ออก</th>"+
      RV_PARTS.map(function(P){return "<th>"+esc(P.label)+"</th>";}).join("")+"</tr></thead><tbody>";
    rvYears(mx).forEach(function(y){
      h+="<tr><td>"+esc(y==="x"?"ข้อฝึกเพิ่ม":"MED"+y)+"</td>"+RV_PARTS.map(function(P){var L=mx[y][P.k];
        if(!L||!L.length)return "<td class='none'>—</td>";var d=rvCount(L);
        return "<td><button type='button' class='rvcell"+(d===L.length?" full":"")+"' data-y='"+y+"' data-p='"+P.k+"' aria-label='"+
          esc(rvYLabel(y)+" "+P.label+" ทำแล้ว "+d+" จาก "+L.length+" ข้อ")+"'>"+d+"/"+L.length+"</button></td>";}).join("")+"</tr>";
    });
    h+="</tbody></table></div>";
    sec.innerHTML=h;
    [].forEach.call(sec.querySelectorAll(".rvcell"),function(b){
      b.addEventListener("click",function(){rvGo(u.id,b.getAttribute("data-y"),b.getAttribute("data-p"));});});
    var acts=document.createElement("div");acts.className="rvacts";
    var ex=u.es.filter(function(e){return e.ys.length;}).length;
    var b1=document.createElement("button");b1.type="button";b1.className="reveal";
    b1.textContent="ทำข้อสอบเก่าทั้งคาบ ("+ex+" ข้อ)";b1.disabled=!ex;
    b1.addEventListener("click",function(){rvGo(u.id,"all","all");});acts.appendChild(b1);
    sec.appendChild(acts);stream.appendChild(sec);
  });
}

"""

EDITS = [
    (CSS_ANCHOR, CSS_ANCHOR + CSS),
    (MODES_OLD, MODES_NEW),
    (RAIL_OLD, RAIL_NEW),
    (CONNECT_OLD, CONNECT_NEW),
    (SCORE_OLD, SCORE_NEW),
    (SETBAR_OLD, SETBAR_NEW),
    (MCOUNT_OLD, MCOUNT_NEW),
    (MFILTER_OLD, MFILTER_NEW),
    (RAILSHOW_OLD, RAILSHOW_NEW),
    (STREAM_OLD, STREAM_NEW),
    (ACTIVE_OLD, ACTIVE_NEW),
    (HASH_OLD, HASH_NEW),
    (JS_ANCHOR, JS + JS_ANCHOR),
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
