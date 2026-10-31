#!/usr/bin/env python3
"""
patch_drill_review.py — โหมด "คาบที่ทวนแล้ว" ใน MED421 Ward Drill

    python3 dashboard/patch_drill_review.py <drill.html> <dashboard index.html> <out.html> [--edits edits.json]

รวมข้อสอบของคาบที่กด ✓ ทวนแล้วใน Lecture Dashboard แยกตาม **วันที่ทวน** → คาบ → ปีที่ออก (MED28–MED35)
→ MCQ / MEQ / SAQ·OSCE

ข้อมูลการทวนมาได้ 2 ทาง (ใช้ตัวที่ `at` ใหม่กว่า)
1. ซิงก์อัตโนมัติ — งานตั้งเวลาของ Claude อ่าน `data/users/<id>/slides` ของ dashboard
   แล้วเขียน `data/users/<id>/drill-reviewed` ของ drill = {reviews:{<id คาบ dashboard>:[วันที่ทวน]}, at, src:"sync"}
   (at = updatedAt ของเอกสาร dashboard · หน้า drill เปิดอยู่ก็อัปเดตเองผ่าน onSnapshot)
2. ปุ่ม "ฝึกข้อสอบคาบที่ทวนแล้ว" ใน dashboard (patch_dash_review.py) ส่งทางลิงก์ทันที
   `#review~y2026~<MMDDHHMM>.<MMDD>.<MMDD>~…` (id คาบ 2026-MM-DD-HHMM · วันที่ทวน 2026-MM-DD)

- DLECS (id คาบ dashboard → [hash drill, ชื่อคาบ, อาจารย์]) ฝังจาก LECS ของ dashboard ตอนแพตช์
- ข้อของคาบ = คลังข้อสอบเก่า + MCQ ใหม่ + MEQ/OSCE ที่ lec ตรงกัน · ปีจาก `years`
- Part ของปีนั้นอ่านจาก src (คลังเก่า) / ref (MCQ ใหม่) ช่วงข้อความหลัง MEDxx — ไม่ระบุ = MCQ
  MEQ/OSCE ใหม่ใช้ part ของข้อเอง · ข้อที่ไม่มีปี = "ข้อฝึกเพิ่ม"
- คำตอบใช้ state.answers / state.shown เดิม จึงนับรวมกับโหมดอื่นและซิงก์เข้าบัญชีตามปกติ

รันได้กับหน้าที่ยังไม่แพตช์เท่านั้น (ทุก anchor ต้องเจอครั้งเดียว) · --edits เขียนคู่ old/new สำหรับ edit_version
"""
import json, re, subprocess, sys

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
.rvday{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:12px;padding:14px 18px;border-radius:var(--r-lg);
  background:var(--surface);border:1px solid var(--rule);box-shadow:var(--shadow)}
.rvday h2{font-size:19px;font-weight:700;margin-right:auto}
.rvday h2 small{font-size:12px;font-weight:600;color:var(--on-accent);background:var(--accent);border-radius:999px;padding:2px 9px;margin-left:8px;vertical-align:3px}
.rvday .meta{font-family:var(--mono);font-size:11px;color:var(--ink-3)}
.reveal.go{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.reveal.go:hover{background:var(--accent-ink);border-color:var(--accent-ink)}
.rvback{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
"""

MODES_OLD = '{k:"quiz",label:"สุ่มทำข้อสอบ"}];'
MODES_NEW = '{k:"quiz",label:"สุ่มทำข้อสอบ"},{k:"review",label:"คาบที่ทวนแล้ว"}];'

RAIL_OLD = '<p class="qzinfo" id="qzinfo"></p>\n    </div>\n'
RAIL_BLOCK = """    <div id="rvblock" style="display:none">
      <h2>วันที่ทวน</h2>
      <div class="parts" id="rvday"></div>
      <h2 class="qzh">คาบที่ทวนแล้ว</h2>
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
RAIL_NEW = RAIL_OLD + RAIL_BLOCK

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
JS_TMPL = r"""/* ---------- คาบที่ทวนแล้ว (โหมด review) ----------
   การทวนมาจาก Lecture Dashboard: {reviews:{<id คาบ>:["YYYY-MM-DD",…]}, at, src}
   ซิงก์อัตโนมัติ (งานตั้งเวลาเขียน data/users/<id>/drill-reviewed) หรือลิงก์ #review~y2026~<MMDDHHMM>.<MMDD>…
   ใช้ชุดที่ at ใหม่กว่า · เก็บสำเนาใน localStorage med421-drill-reviewed
   ข้อของคาบ = คลังเก่า + MCQ ใหม่ + MEQ/OSCE ของ lec นั้น · แยกตามวันที่ทวน → ปีที่ออก (years) → MCQ / MEQ / SAQ·OSCE
   ส่วนของข้อสอบในปีนั้นอ่านจาก src/ref ช่วงที่ตามหลัง MEDxx (ไม่ระบุ = MCQ) · ข้อที่ไม่มีปี = ข้อฝึกเพิ่ม (x) */
var DASH="https://claude.ai/artifact/8ir2xCgMKC7Fn4MiE2a5AV";
var RVKEY="med421-drill-reviewed";
/* งานตั้งเวลา (sync_reviews) เขียนทับบรรทัดถัดไปด้วยการทวนล่าสุดจาก dashboard — ใช้เฉพาะเมื่อผู้ดูคือเจ้าของ (u) */
var RV_SEED=null;
/* id คาบใน dashboard → [hash drill, ชื่อคาบ, อาจารย์] (จาก LECS ของ dashboard ตอนแพตช์) */
var DLECS=__DLECS__;
var RV_PARTS=[{k:"MCQ",label:"MCQ"},{k:"MEQ",label:"MEQ"},{k:"SAQ",label:"SAQ / OSCE"}];
var RV={rev:{},at:"",src:"",day:"all",lec:"all",part:"all",year:"all",list:0};
var RVS={ref:null,busy:0,sent:""};
var RV_M=["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."];
var RV_D=["อาทิตย์","จันทร์","อังคาร","พุธ","พฤหัสฯ","ศุกร์","เสาร์"];
var RV_TODAY=new Date(Date.now()+7*3600e3).toISOString().slice(0,10);
function rvDate(d,long){var p=d.split("-"),x=new Date(Date.UTC(+p[0],+p[1]-1,+p[2]));
  return (long?RV_D[x.getUTCDay()]+" ":"")+x.getUTCDate()+" "+RV_M[x.getUTCMonth()];}
function rvAgo(d){var p=d.split("-"),q=RV_TODAY.split("-");
  var n=Math.round((Date.UTC(+q[0],+q[1]-1,+q[2])-Date.UTC(+p[0],+p[1]-1,+p[2]))/864e5);
  return n<=0?"วันนี้":n===1?"เมื่อวาน":n+" วันก่อน";}
function rvCleanRev(o){var r={};if(o&&typeof o==="object")Object.keys(o).sort().forEach(function(id){
  if(!DLECS[id]||!Array.isArray(o[id]))return;
  var ds=o[id].filter(function(x){return typeof x==="string"&&/^\d{4}-\d{2}-\d{2}$/.test(x);});
  ds=ds.filter(function(x,i){return ds.indexOf(x)===i;}).sort().slice(-40);if(ds.length)r[id]=ds;});return r;}
try{var rr=JSON.parse(localStorage.getItem(RVKEY)||"null");if(rr&&typeof rr==="object"){
  RV.rev=rvCleanRev(rr.rev);RV.at=typeof rr.at==="string"?rr.at:"";RV.src=typeof rr.src==="string"?rr.src:"";
  ["day","lec","part","year"].forEach(function(f){if(typeof rr[f]==="string")RV[f]=rr[f];});RV.list=rr.list?1:0;}}catch(e){}
function rvKeep(){try{localStorage.setItem(RVKEY,JSON.stringify(RV));}catch(e){}}
function rvSave(){rvKeep();rvWrite();}
function rvBody(){return JSON.stringify({reviews:RV.rev,at:RV.at,src:RV.src});}
function rvWrite(){
  if(!RVS.ref||RVS.busy||!RV.at)return;
  var b=rvBody();if(b===RVS.sent)return;
  RVS.busy=1;
  RVS.ref.set(JSON.parse(b)).then(function(){RVS.busy=0;RVS.sent=b;rvWrite();},function(){RVS.busy=0;});
}
function rvConnect(db,uid){
  if(RV_SEED&&RV_SEED.u===uid&&typeof RV_SEED.at==="string"&&RV_SEED.at>RV.at){
    RV.rev=rvCleanRev(RV_SEED.reviews);RV.at=RV_SEED.at;RV.src="sync";RVU=null;rvKeep();render();}
  RVS.ref=db.doc("data/users/"+uid+"/drill-reviewed");
  RVS.ref.onSnapshot(function(snap){
    var d=snap.exists?snap.data():null,at=d&&typeof d.at==="string"?d.at:"";
    if(d)RVS.sent=JSON.stringify({reviews:rvCleanRev(d.reviews),at:at,src:typeof d.src==="string"?d.src:""});
    if(at>RV.at){RV.rev=rvCleanRev(d.reviews);RV.at=at;RV.src=typeof d.src==="string"?d.src:"";RVU=null;rvKeep();render();}
    else if(RV.at>at)rvWrite();
  },function(){});
}
/* #review~y2026~09151400.1013.1020~… · #review เฉย ๆ = เปิดโหมดนี้ด้วยข้อมูลเดิม */
function rvFromHash(h){
  var toks=h.split("~").slice(1),y="2026",rev={},n=0;
  toks.forEach(function(t){
    var m=t.match(/^y(\d{4})$/);if(m){y=m[1];return;}
    m=t.match(/^(\d{2})(\d{2})(\d{4})((?:\.\d{4})+)$/);if(!m)return;
    rev[y+"-"+m[1]+"-"+m[2]+"-"+m[3]]=m[4].slice(1).split(".").map(function(x){return y+"-"+x.slice(0,2)+"-"+x.slice(2);});n++;});
  rev=rvCleanRev(rev);
  if(n&&JSON.stringify(rev)!==JSON.stringify(RV.rev)){
    RV.rev=rev;RV.at=new Date().toISOString();RV.src="link";RVU=null;}
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
/* หน่วย = คาบใน drill (ชุด-lec) · dl = คาบใน dashboard ที่ชี้มา · days = วันที่ทวน */
var RVU=null,RVUK="";
function rvUnits(){
  var key=JSON.stringify(RV.rev);if(RVU&&RVUK===key)return RVU;
  var map={},out=[];out.miss=0;
  Object.keys(RV.rev).forEach(function(id){
    var D=DLECS[id],k=D[0],i=k.indexOf("-"),s=i<0?k:k.slice(0,i),l=i<0?"":k.slice(i+1),hit=0;
    if(!BANK[s]){out.miss++;return;}
    (l?[l]:rvLecsOf(s)).forEach(function(lec){
      var uid=s+"-"+lec,u=map[uid];
      if(!u){var es=rvEntries(s,lec);if(!es.length)return;
        var e0=es.filter(function(e){return e.it.lecture||(e.g&&e.g.lecture);})[0];
        u=map[uid]={id:uid,set:s,lec:lec,es:es,name:e0?(e0.it.lecture||e0.g.lecture):"Lec "+lec,whole:!l,dl:[],days:[]};out.push(u);}
      hit=1;if(u.dl.indexOf(id)<0)u.dl.push(id);
      RV.rev[id].forEach(function(d){if(u.days.indexOf(d)<0)u.days.push(d);});
    });
    if(!hit)out.miss++;
  });
  out.forEach(function(u){u.days.sort();u.last=u.days[u.days.length-1];
    u.title=u.whole?shortName(u.name):u.dl.map(function(id){return DLECS[id][1];}).join(" / ");
    u.by=DLECS[u.dl[0]][2]||teacher(u.name);});
  out.sort(function(a,b){return a.last<b.last?1:a.last>b.last?-1:a.id<b.id?-1:1;});
  RVU=out;RVUK=key;return out;
}
function rvDays(){var c={};rvUnits().forEach(function(u){u.days.forEach(function(d){c[d]=(c[d]||0)+1;});});
  return Object.keys(c).sort().reverse().map(function(d){return {d:d,n:c[d]};});}
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
function rvInDay(u){return RV.day==="all"||u.days.indexOf(RV.day)>=0;}
function rvSel(){return rvUnits().filter(function(u){return rvInDay(u)&&(RV.lec==="all"||u.id===RV.lec);});}
function rvListing(){return !!(RV.list||RV.lec!=="all"||RV.year!=="all"||RV.part!=="all");}
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
function rvExam(us){return rvUniq(us.map(function(u){return {list:u.es.filter(function(e){return e.ys.length;})};})).length;}
function rvScore(){
  var es=rvListing()?rvUniq(rvBlocks()):rvUniq(rvSel().map(function(u){return {list:u.es};}));
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
function rvGo(o){o=o||{};RV.lec=o.lec||"all";RV.year=o.year||"all";RV.part=o.part||"all";RV.list=o.list?1:0;
  if(o.day)RV.day=o.day;rvSave();render();window.scrollTo({top:0});}
function buildRvRail(){
  var us=rvUnits(),days=rvDays();
  if(RV.day!=="all"&&!days.some(function(x){return x.d===RV.day;}))RV.day="all";
  if(RV.lec!=="all"&&!rvSel().length)RV.lec="all";
  rvChips("rvday",[{k:"all",label:"ทุกวัน"}].concat(days.map(function(x){
    return {k:x.d,label:(x.d===RV_TODAY?"วันนี้ ":"")+rvDate(x.d)+" · "+x.n};})),RV.day,
    function(k){RV.day=k;RV.lec="all";RV.year="all";RV.part="all";RV.list=0;});
  var el=document.getElementById("rvlecs");el.innerHTML="";
  function lb(id,slot,nm,ct){var b=document.createElement("button");b.type="button";b.className="lec";
    b.setAttribute("aria-pressed",String(RV.lec===id&&(id!=="all"||!rvListing())));
    b.innerHTML="<span class='slot'>"+esc(slot)+"</span><span class='nm'>"+esc(nm)+"</span><span class='ct'>"+ct+"</span>";
    b.addEventListener("click",function(){rvGo({lec:id,list:id!=="all"});});el.appendChild(b);}
  var shown=us.filter(rvInDay);
  lb("all","ทั้ง","ภาพรวม"+(RV.day==="all"?"ทุกวัน":" "+rvDate(RV.day)),shown.length);
  shown.forEach(function(u){lb(u.id,setLabel(u.set)+" "+u.lec,u.title,u.es.length);});
  rvChips("rvpart",[{k:"all",label:"ทั้งหมด"}].concat(RV_PARTS),RV.part,function(k){RV.part=k;});
  var ys={};rvSel().forEach(function(u){Object.keys(rvMatrix(u)).forEach(function(y){ys[y]=1;});});
  if(RV.year!=="all"&&!ys[RV.year])RV.year="all";
  var yo=[{k:"all",label:"ทุกปี"}].concat(Object.keys(ys).filter(function(y){return y!=="x";}).sort().reverse()
    .map(function(y){return {k:y,label:"MED"+y};})).concat(ys.x?[{k:"x",label:"ข้อฝึกเพิ่ม"}]:[]);
  rvChips("rvyear",yo,RV.year,function(k){RV.year=k;});
  document.getElementById("rvfilters").style.display=us.length?"":"none";
  var at=RV.at?new Date(RV.at):null;
  document.getElementById("rvinfo").innerHTML="ดึงการทวนจาก <a href='"+DASH+"' target='_blank' rel='noopener'>Lecture Dashboard</a> อัตโนมัติ"+
    (at&&!isNaN(at)?" · ข้อมูลล่าสุด "+esc(at.toLocaleDateString("th-TH",{day:"numeric",month:"short"})+" "+
      at.toLocaleTimeString("th-TH",{hour:"2-digit",minute:"2-digit"}))+(RV.src==="link"?" (จากปุ่มใน Dashboard)":""):"")+
    " · อยากได้ทันทีกดปุ่ม <b>ฝึกข้อสอบคาบที่ทวนแล้ว</b> ใน Dashboard";
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
    c.innerHTML="<h3 class='topic'>ยังไม่มีคาบที่ทวนแล้ว</h3>"+
      "<p class='stem'>กด ✓ คาบที่ทวนแล้วใน <a href='"+DASH+"' target='_blank' rel='noopener'>MED421 Lectures (Dashboard)</a> — "+
      "Drill จะดึงมาเองตามรอบที่ตั้งเวลาไว้ แล้วรวมข้อสอบของแต่ละวันที่ทวน แยกปีที่ออก และแยก MCQ / MEQ / SAQ ให้ "+
      "อยากได้ทันทีกดปุ่ม <b>ฝึกข้อสอบคาบที่ทวนแล้ว</b> ที่แผงด้านข้างของ Dashboard</p>";
    stream.appendChild(c);return;}
  if(!rvListing()){renderRvOverview(stream,us);return;}
  var bar=document.createElement("div");bar.className="rvback";
  var back=document.createElement("button");back.type="button";back.className="ghost";back.textContent="← ภาพรวม"+(RV.day==="all"?"":" "+rvDate(RV.day));
  back.addEventListener("click",function(){rvGo();});bar.appendChild(back);
  if(RV.day!=="all"){var s=document.createElement("span");s.className="lecline";s.style.margin="0";
    s.textContent="ข้อสอบของคาบที่ทวน"+(RV.day===RV_TODAY?"วันนี้":"วัน"+rvDate(RV.day,1));bar.appendChild(s);}
  stream.appendChild(bar);
  var blocks=rvBlocks();
  if(!blocks.length){var em=document.createElement("p");em.className="empty";em.textContent="ไม่มีข้อในเงื่อนไขนี้ — ลองเลือกปีหรือ Part อื่น";stream.appendChild(em);return;}
  var lastU=null,lastY=null;
  blocks.forEach(function(b){
    if(b.u!==lastU){lastU=b.u;lastY=null;
      var meta=LEC[b.u.lec]||{},h=document.createElement("div");h.className="rvunit";
      h.innerHTML="<h2>"+esc(setLabel(b.u.set))+" · Lec "+esc(b.u.lec)+" — "+esc(b.u.title)+"</h2>"+
        "<p>"+[b.u.by,meta.d,"ทวน "+b.u.days.length+" รอบ · ล่าสุด "+rvAgo(b.u.last)].filter(Boolean).map(esc).join(" · ")+"</p>";
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
function rvCard(u,d){
  var mx=rvMatrix(u),meta=LEC[u.lec]||{};
  var sec=document.createElement("article");sec.className="item rvcard";
  var k=u.days.indexOf(d)+1;
  var h="<div class='ihead'><span class='qno'>Lec "+esc(u.lec)+"</span><span class='tag'>"+esc(setLabel(u.set))+"</span>"+
    (meta.d?"<span class='tag'>"+esc(meta.d)+"</span>":"")+"<span class='tag yr'>ทวนรอบที่ "+k+"</span></div>"+
    "<h3 class='topic'>"+esc(u.title)+"</h3>"+(u.by?"<p class='lecline'>"+esc(u.by)+"</p>":"")+
    "<div class='tablewrap'><table class='rvmx'><thead><tr><th>ปีที่ออก</th>"+
    RV_PARTS.map(function(P){return "<th>"+esc(P.label)+"</th>";}).join("")+"</tr></thead><tbody>";
  rvYears(mx).forEach(function(y){
    h+="<tr><td>"+esc(y==="x"?"ข้อฝึกเพิ่ม":"MED"+y)+"</td>"+RV_PARTS.map(function(P){var L=mx[y][P.k];
      if(!L||!L.length)return "<td class='none'>—</td>";var n=rvCount(L);
      return "<td><button type='button' class='rvcell"+(n===L.length?" full":"")+"' data-y='"+y+"' data-p='"+P.k+"' aria-label='"+
        esc(rvYLabel(y)+" "+P.label+" ทำแล้ว "+n+" จาก "+L.length+" ข้อ")+"'>"+n+"/"+L.length+"</button></td>";}).join("")+"</tr>";
  });
  h+="</tbody></table></div>";
  sec.innerHTML=h;
  [].forEach.call(sec.querySelectorAll(".rvcell"),function(b){
    b.addEventListener("click",function(){rvGo({lec:u.id,year:b.getAttribute("data-y"),part:b.getAttribute("data-p")});});});
  var acts=document.createElement("div");acts.className="rvacts";
  var ex=u.es.filter(function(e){return e.ys.length;}).length;
  var b1=document.createElement("button");b1.type="button";b1.className="reveal";
  b1.textContent="ทำทั้งคาบ ("+u.es.length+" ข้อ · ข้อสอบเก่า "+ex+")";
  b1.addEventListener("click",function(){rvGo({lec:u.id,list:1});});acts.appendChild(b1);
  sec.appendChild(acts);
  return sec;
}
function renderRvOverview(stream,us){
  var days=rvDays().filter(function(x){return RV.day==="all"||x.d===RV.day;});
  var head=document.createElement("div");head.className="part-head";
  head.innerHTML="<h2>ข้อสอบของคาบที่ทวนแล้ว</h2><span class='meta'>"+us.length+" คาบ · ทวนมา "+rvDays().length+" วัน</span>";
  stream.appendChild(head);
  var info=document.createElement("p");info.className="oldnote wide";
  info.textContent="แยกตามวันที่กดทวนใน Dashboard (ใหม่สุดก่อน) · ปุ่ม “ทำข้อสอบของวันที่ …” รวมทุกคาบของวันนั้นไว้ที่เดียว · "+
    "กดตัวเลขในตารางเพื่อทำเฉพาะปีและ Part นั้น (ทำแล้ว/ทั้งหมด) · ข้อจาก MEQ/SAQ ที่เรียบเรียงเป็นตัวเลือกมีป้ายบอก"+
    (us.miss?" · มี "+us.miss+" คาบที่ทวนแล้วแต่ยังไม่มีข้อสอบใน Drill":"");
  stream.appendChild(info);
  days.forEach(function(x){
    var du=us.filter(function(u){return u.days.indexOf(x.d)>=0;}),n=rvUniq(du.map(function(u){return {list:u.es};})).length;
    var dh=document.createElement("div");dh.className="rvday";
    dh.innerHTML="<h2>"+esc(rvDate(x.d,1))+(x.d===RV_TODAY?"<small>วันนี้</small>":"")+"</h2>"+
      "<span class='meta'>ทวน "+du.length+" คาบ · "+n+" ข้อ · ข้อสอบเก่า "+rvExam(du)+"</span>";
    var go=document.createElement("button");go.type="button";go.className="reveal go";
    go.textContent="ทำข้อสอบของวันที่ "+rvDate(x.d)+" ("+n+" ข้อ)";
    go.addEventListener("click",function(){rvGo({day:x.d,list:1});});
    dh.appendChild(go);stream.appendChild(dh);
    du.forEach(function(u){stream.appendChild(rvCard(u,x.d));});
  });
}

"""

DLECS_RE = re.compile(r'var LECS=\[.*?\n\];', re.S)


def dlecs_from_dashboard(path):
    """id คาบ → [hash drill, ชื่อคาบ, อาจารย์] จาก LECS ใน index.html ของ dashboard (ใช้ node ประเมิน)"""
    h = open(path, encoding='utf-8').read()
    s = h.index('var LECS=['); e = h.index('var EXTRAS=', s)
    js = ('global.LECS=null;' + h[s:e].replace('var LECS', 'global.LECS', 1) +
          ';var o={};LECS.forEach(function(l){if(l.drill)o[l.d+"-"+l.t.replace(":","")]=[l.drill[0],l.title,l.by||""];});'
          'process.stdout.write(JSON.stringify(o));')
    return json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout)


def edits(dlecs):
    js = JS_TMPL.replace('__DLECS__', json.dumps(dlecs, ensure_ascii=False, separators=(',', ':')))
    return [
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
        (JS_ANCHOR, js + JS_ANCHOR),
    ]


def patch(html, eds):
    for old, new in eds:
        n = html.count(old)
        assert n == 1, f'anchor พบ {n} ครั้ง (ต้อง 1): {old[:70]!r}'
        html = html.replace(old, new)
    return html


if __name__ == '__main__':
    src, dash, out = sys.argv[1], sys.argv[2], sys.argv[3]
    eds = edits(dlecs_from_dashboard(dash))
    open(out, 'w', encoding='utf-8').write(patch(open(src, encoding='utf-8').read(), eds))
    if '--edits' in sys.argv:
        fn = sys.argv[sys.argv.index('--edits') + 1]
        json.dump([{'old_text': o, 'new_text': n} for o, n in eds], open(fn, 'w', encoding='utf-8'), ensure_ascii=False)
    print('patched', out)
