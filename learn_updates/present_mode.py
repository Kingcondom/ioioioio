# -*- coding: utf-8 -*-
"""เพิ่มโหมดพรีเซนต์ทั้งคาบ (อธิบายให้คนอื่นฟัง บนจอมีแค่ keyword) ให้หน้า MED421 learn
python3 present_mode.py <in.html> <out.html>"""
import sys
SRC, DST = sys.argv[1], sys.argv[2]
h = open(SRC, encoding="utf-8").read()
assert "var Pres=" not in h, "already patched"

CSS = r"""
/* ลิงก์ยาวในกล่อง นล./แนวทาง ทำหน้าล้นจอบนมือถือ — ให้ตัดบรรทัดได้ */
.nlbox li>span{min-width:0;overflow-wrap:anywhere}
/* ---------- โหมดพรีเซนต์ (ผู้ใช้ขอ 9 พ.ย.) ---------- */
.pv{position:fixed;inset:0;z-index:70;background:var(--paper);color:var(--ink);display:flex;flex-direction:column;font-family:var(--sans);font-size:16px;line-height:1.65}
.pv[hidden]{display:none!important}
.pv:focus{outline:none}
.pv-top,.pv-bot{display:flex;align-items:center;gap:var(--s-2);padding:var(--s-2) var(--s-4);background:var(--surface)}
.pv-top{border-bottom:1px solid var(--rule)}.pv-bot{border-top:1px solid var(--rule)}
.pv-top select{min-height:44px;min-width:0;flex:0 1 360px;font:inherit;font-size:14px;color:var(--ink);background:var(--surface);border:1px solid var(--rule-strong);border-radius:var(--r-md);padding:0 var(--s-2)}
.pv-meta{margin-left:auto;display:flex;gap:var(--s-3);font-size:14px;color:var(--ink-3);font-variant-numeric:tabular-nums;white-space:nowrap}
.pv-prog{height:4px;background:var(--surface-sunk)}.pv-prog i{display:block;height:100%;background:var(--accent);transition:width .18s var(--e)}
.pv-stage{flex:1;overflow:auto;-webkit-overflow-scrolling:touch}
.pv-slide{max-width:880px;margin:0 auto;padding:var(--s-6) var(--s-4) var(--s-7)}
.pv-eye{font-size:14px;line-height:1.6;font-weight:600;color:var(--accent-ink);margin:0 0 var(--s-2)}
.pv-h1{font-size:30px;line-height:1.3;font-weight:600;margin:0 0 var(--s-3);text-wrap:balance}
.pv-h2{font-size:24px;line-height:1.35;font-weight:600;margin:0 0 var(--s-3);text-wrap:balance}
.pv-ask{font-size:16px;color:var(--ink-2);margin:0 0 var(--s-5);text-wrap:pretty}
.pv-kw{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:var(--s-2)}
.pv-kw li{font-size:18px;line-height:1.45;font-weight:600;padding:var(--s-2) var(--s-3);border:1px solid var(--rule-strong);border-radius:var(--r-md);background:var(--surface)}
.pv-kw li strong{font-weight:600}
.pv-more{font-size:14px;color:var(--ink-3);margin:var(--s-2) 0 0}
.pv-vis{margin-top:var(--s-5)}
.pv-rate{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s-2);margin-top:var(--s-6);padding-top:var(--s-4);border-top:1px dashed var(--rule)}
.pv-rate>span{font-size:14px;color:var(--ink-3);margin-right:var(--s-2)}
.pv-rate .btn.on,.pv-rate .btn.on:hover{background:var(--accent-soft);color:var(--accent-ink);border-color:var(--accent)}
.pv-notes{margin-top:var(--s-5);padding:var(--s-4);border:1px solid var(--rule);border-radius:var(--r-lg);background:var(--surface)}
.pv-notes>h3{font-size:14px;line-height:1.6;font-weight:600;color:var(--ink-3);margin:0 0 var(--s-2)}
.pv-list{margin:var(--s-3) 0 0;padding-left:var(--s-5)}.pv-list li{margin:var(--s-1) 0}
.pv-sub{font-size:18px;line-height:1.45;font-weight:600;margin:var(--s-5) 0 var(--s-2)}
.pv-stats{display:flex;flex-wrap:wrap;gap:var(--s-2);margin:var(--s-3) 0 0;padding:0;list-style:none}
.pv-stats li{font-size:16px;padding:var(--s-2) var(--s-3);border:1px solid var(--rule);border-radius:var(--r-md);background:var(--surface);font-variant-numeric:tabular-nums}
.pv-weak{display:grid;gap:var(--s-2);margin-top:var(--s-3)}
.pv-weak .btn{justify-content:flex-start;white-space:normal;text-align:left;width:100%}
.pv-acts{display:flex;flex-wrap:wrap;gap:var(--s-2);margin-top:var(--s-5)}
.pv-bot .sp{flex:1;min-width:0;text-align:center;font-size:14px;color:var(--ink-3);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pv-top,.pv-bot,.pv-stage,.pv-slide{min-width:0}.pv-slide{overflow-wrap:anywhere}
@media (max-width:560px){.pv-h1{font-size:24px;line-height:1.35}.pv-h2{font-size:20px;line-height:1.4}.pv-kw li{font-size:16px;line-height:1.5}
  .pv-slide{padding:var(--s-5) var(--s-4) var(--s-6)}.pv-meta .pv-time{display:none}.pv-top,.pv-bot{padding:var(--s-2)}}
"""

JS = r"""
/* ---------- โหมดพรีเซนต์ (ผู้ใช้ขอ 9 พ.ย.) ----------
   อธิบายทั้งคาบให้คนอื่นฟัง — อธิบายได้ = เข้าใจแล้ว · บนจอมีแค่หัวข้อกับ keyword (คำตัวหนาในบทเรียน)
   ลำดับ: ปก → ต่อหัวข้อ (เปิดหัวข้อ → หัวข้อย่อย ### ละสไลด์ → ปิดหัวข้อ) → สรุปจุดที่ติด
   โน้ตเต็มซ่อนไว้ กดดูหลังอธิบายเสร็จ · ประเมินตัวเองเก็บใน state.rate คีย์ pv|ชุด|หัวข้อ#ลำดับ (ซิงก์บัญชี) */
var Pres=(function(){
  var P={el:null,S:[],i:0,lec:null,notes:false,t0:0,tick:null,back:null};
  var PKEY="med421-pres",RATES=[["ok","อธิบายได้"],["part","ติดบางจุด"],["no","ยังไม่ได้"]];
  function posGet(){try{return JSON.parse(localStorage.getItem(PKEY)||"{}")||{};}catch(e){return {};}}
  function posSet(v){try{var o=posGet();o[state.course+"|"+P.lec.lec]=v;localStorage.setItem(PKEY,JSON.stringify(o));}catch(e){}}
  function rk(key){return "pv|"+state.course+"|"+key;}
  function plain(t){return String(t==null?"":t).replace(/\*\*/g,"").replace(/`/g,"").replace(/\s+/g," ").trim();}
  function blocks(s){
    var bs=[],cur={title:"",lines:[]};
    String(s.md||"").split("\n").forEach(function(L){
      var m=/^\s*#{3,4}\s+(.*)$/.exec(L);
      if(m){bs.push(cur);cur={title:m[1],lines:[]};}else cur.lines.push(L);
    });
    bs.push(cur);
    return bs.filter(function(b){return b.title||b.lines.join("").trim();});
  }
  function keywords(lines){
    var seen={},out=[];
    function add(k){k=plain(k).replace(/[:：—–]\s*$/,"").trim();if(!k||k.length>60)return;var lo=k.toLowerCase();if(seen[lo])return;seen[lo]=1;out.push(k);}
    lines.forEach(function(L){var re=/\*\*([^*]+)\*\*/g,m;while((m=re.exec(L)))add(m[1]);});
    if(out.length<3){                       /* ไม่มีตัวหนาพอ → ใช้หัวแถวของตาราง (ข้ามแถวหัวตาราง) */
      var prevTable=false;
      lines.forEach(function(L){
        var isT=/^\s*\|/.test(L),isSep=/^\s*\|\s*:?-{2,}/.test(L);
        if(isT&&!isSep&&prevTable){var c=L.trim().replace(/^\|/,"").split("|")[0];if(plain(c).length<=40)add(c);}
        prevTable=isT;
      });
    }
    return out;
  }
  function visual(lines){
    for(var i=0;i<lines.length;i++){var m=/^\s*\[\[(fig|anim|img):([\w-]+)\]\]\s*$/.exec(lines[i]);if(m)return {t:m[1],k:m[2]};}
    return null;
  }
  function build(l){
    var S=[{type:"cover"}],n=l.sections.length;
    l.sections.forEach(function(s,si){
      var sum=String(s.summary||"").split(/\s·\s/).map(function(x){return x.trim();}).filter(Boolean);
      S.push({type:"sec",s:s,si:si,n:n,kw:sum.slice(0,10),more:Math.max(0,sum.length-10),key:s.id+"#sec"});
      blocks(s).forEach(function(b,bi){
        var kw=keywords(b.lines),vis=visual(b.lines);
        if(!kw.length&&!vis&&!b.title)return;
        S.push({type:"blk",s:s,si:si,n:n,b:b,kw:kw.slice(0,10),more:Math.max(0,kw.length-10),vis:vis,key:s.id+"#"+bi});
      });
      S.push({type:"end",s:s,si:si,n:n,key:s.id+"#end"});
    });
    S.push({type:"fin"});
    return S;
  }
  function chips(kw,more){
    if(!kw.length)return "<p class='pv-more'>หัวข้อนี้ไม่มีคำตัวหนา — อธิบายจากหัวข้อและภาพ</p>";
    return "<ul class='pv-kw'>"+kw.map(function(k){return "<li>"+inline(k)+"</li>";}).join("")+"</ul>"+
      (more?"<p class='pv-more'>อีก "+more+" คำอยู่ในโน้ต</p>":"");
  }
  function rateBox(key){
    var v=state.rate[rk(key)]||"";
    return "<div class='pv-rate' role='group' aria-label='อธิบายได้แค่ไหน'><span>อธิบายได้แค่ไหน</span>"+
      RATES.map(function(x){return "<button class='btn"+(v===x[0]?" on":"")+"' data-pvr='"+x[0]+"' aria-pressed='"+(v===x[0]?"true":"false")+"'>"+(v===x[0]?"✓ ":"")+x[1]+"</button>";}).join("")+"</div>";
  }
  function notesBox(title,html){
    return P.notes?"<section class='pv-notes prose'><h3>"+esc(title)+"</h3>"+html+"</section>":"";
  }
  function rated(){
    var c={ok:0,part:0,no:0,none:0},weak=[];
    P.S.forEach(function(x,i){if(!x.key)return;var v=state.rate[rk(x.key)];
      if(v==="ok")c.ok++;else if(v==="part"||v==="no"){c[v]++;weak.push(i);}else c.none++;});
    return {c:c,weak:weak};
  }
  function label(x){return x.s?(x.si+1)+". "+plain(x.s.title)+(x.type==="blk"?" › "+plain(x.b.title||"เปิดเรื่อง"):x.type==="end"?" › ปิดหัวข้อ":""):"";}
  function slideHtml(x){
    var l=P.lec,h="";
    if(x.type==="cover"){
      var nb=P.S.filter(function(y){return y.key;}).length,saved=+posGet()[state.course+"|"+l.lec]||0,r=rated();
      h="<p class='pv-eye'>โหมดพรีเซนต์ · คาบ "+esc(l.lec)+(l.date?" · "+esc(l.date):"")+"</p>"+
        "<h1 class='pv-h1'>"+esc(l.title)+"</h1>"+
        "<p class='pv-ask'>อธิบายทั้งคาบให้คนอื่นฟัง ถ้าอธิบายจนคนฟังเข้าใจได้ แปลว่าเราเข้าใจแล้ว · "+l.sections.length+" หัวข้อ "+nb+" สไลด์</p>"+
        "<h2 class='pv-sub'>วิธีใช้</h2><ol class='pv-list'>"+
        "<li>บนจอมีแค่คีย์เวิร์ด — พูดเชื่อมทุกคำด้วยภาษาของตัวเอง ไม่อ่านตาม</li>"+
        "<li>อธิบายจบแล้วค่อยกด <b>โน้ต</b> เทียบกับบทเรียน</li>"+
        "<li>ให้คะแนนตัวเองทุกสไลด์ จุดที่ติดจะรวมไว้หน้าสุดท้าย</li>"+
        "<li>ภาพกลไกจะปิดป้ายไว้ ให้อธิบายภาพเองก่อนกดเฉลย</li>"+
        "<li>คีย์บอร์ด: ลูกศรซ้าย/ขวาเลื่อนสไลด์ ปุ่ม N เปิดโน้ต ปุ่ม Esc ออก · มือถือปัดซ้าย/ขวาได้</li></ol>"+
        (l.objectives&&l.objectives.length?"<h2 class='pv-sub'>จบแล้วคนฟังต้องทำได้</h2><ol class='pv-list'>"+l.objectives.map(function(o){return "<li>"+inline(o)+"</li>";}).join("")+"</ol>":"")+
        (r.c.ok+r.c.part+r.c.no?"<p class='pv-more'>รอบก่อน: อธิบายได้ "+r.c.ok+" · ติดบางจุด "+r.c.part+" · ยังไม่ได้ "+r.c.no+"</p>":"")+
        (saved>0&&saved<P.S.length-1?"<div class='pv-acts'><button class='btn' data-pvgo='"+saved+"'>ต่อจากที่ค้าง · สไลด์ "+saved+"</button></div>":"");
      return h;
    }
    if(x.type==="fin"){
      var R=rated(),mins=Math.round((Date.now()-P.t0)/60000);
      h="<p class='pv-eye'>จบคาบ "+esc(l.lec)+"</p><h1 class='pv-h1'>สรุปการพรีเซนต์</h1>"+
        "<ul class='pv-stats'><li>✓ อธิบายได้ "+R.c.ok+"</li><li>~ ติดบางจุด "+R.c.part+"</li><li>✗ ยังไม่ได้ "+R.c.no+"</li><li>ยังไม่ประเมิน "+R.c.none+"</li><li>ใช้เวลา "+mins+" นาที</li></ul>";
      if(R.weak.length){
        h+="<h2 class='pv-sub'>จุดที่ต้องกลับไปอ่าน แล้วอธิบายใหม่</h2><div class='pv-weak'>"+R.weak.map(function(i){
          var y=P.S[i],v=state.rate[rk(y.key)];
          return "<button class='btn' data-pvgo='"+i+"'>"+(v==="no"?"✗ ยังไม่ได้ · ":"~ ติดบางจุด · ")+esc(label(y))+"</button>";}).join("")+"</div>"+
          "<div class='pv-acts'><button class='btn primary' data-pvgo='"+R.weak[0]+"'>ซ้อมจุดที่ติดอีกรอบ</button><button class='btn' data-pv='close'>ออกจากโหมดพรีเซนต์</button></div>";
      }else h+="<p class='pv-ask' style='margin-top:16px'>"+(R.c.none?"ยังมีสไลด์ที่ไม่ได้ประเมิน ย้อนกลับไปให้คะแนนเพื่อดูว่าติดตรงไหน":"อธิบายได้ทุกสไลด์ — คาบนี้พร้อมสอนคนอื่นแล้ว")+"</p>"+
          "<div class='pv-acts'><button class='btn primary' data-pv='close'>ออกจากโหมดพรีเซนต์</button><button class='btn' data-pvgo='0'>เริ่มใหม่</button></div>";
      return h;
    }
    var eye="หัวข้อ "+(x.si+1)+"/"+x.n;
    if(x.type==="sec"){
      return "<p class='pv-eye'>"+eye+" · เปิดหัวข้อ</p><h1 class='pv-h1'>"+esc(x.s.title)+"</h1>"+
        "<p class='pv-ask'>เปิดให้คนฟังรู้ก่อนว่าหัวข้อนี้ตอบคำถามอะไร และทำไมต้องรู้ แล้วไล่ภาพรวมตามคำข้างล่าง</p>"+
        chips(x.kw,x.more)+rateBox(x.key)+
        notesBox("โน้ต · สรุปหัวข้อ",x.s.summary?"<p>"+splitDots(inline(x.s.summary)).join("<br>")+"</p>":"<p>ไม่มีสรุป</p>");
    }
    if(x.type==="end"){
      var mn=(x.s.mnem||[]).map(function(m){return m.name;});
      return "<p class='pv-eye'>"+eye+" · ปิดหัวข้อ</p><h2 class='pv-h2'>"+esc(x.s.title)+"</h2>"+
        "<p class='pv-ask'>สรุปหัวข้อนี้ให้คนฟังในสามประโยค แล้วบอกว่าข้อสอบชอบถามตรงไหน"+(mn.length?" ปิดท้ายด้วยหลักจำ":"")+"</p>"+
        (mn.length?chips(mn,0):"")+rateBox(x.key)+
        notesBox("โน้ต · จำไปสอบ",(x.s.pearls&&x.s.pearls.length?"<ol>"+x.s.pearls.map(function(p){return "<li>"+inline(p)+"</li>";}).join("")+"</ol>":"")+
          (x.s.mnem&&x.s.mnem.length?"<div class='mnem'>"+mnemBody(x.s.mnem)+"</div>":""));
    }
    /* blk */
    var vis="";
    if(x.vis)vis="<div class='pv-vis'>"+(x.vis.t==="fig"?figHtml(x.vis.k):x.vis.t==="anim"?animHtml(x.vis.k):imgHtml(x.vis.k))+"</div>";
    return "<p class='pv-eye'>"+eye+" · "+esc(plain(x.s.title))+"</p><h2 class='pv-h2'>"+inline(x.b.title||"เปิดเรื่อง")+"</h2>"+
      "<p class='pv-ask'>อธิบายให้คนฟังเข้าใจ โดยพูดถึงทุกคำข้างล่าง"+(x.vis?" และอธิบายภาพก่อนเปิดป้าย":"")+"</p>"+
      chips(x.kw,x.more)+vis+rateBox(x.key)+
      notesBox("โน้ต · เนื้อหาในบทเรียน",md(x.b.lines.join("\n")));
  }
  function show(i){
    if(!P.el)return;
    P.i=Math.max(0,Math.min(P.S.length-1,i));posSet(P.i);
    var x=P.S[P.i];
    FIGS=(x.s&&x.s.figs)||{};ANIMS=(x.s&&x.s.anims)||{};IMGS=(x.s&&x.s.imgs)||{};FIGN=0;ANIMN=0;
    var stage=P.el.querySelector(".pv-stage");
    stage.innerHTML="<div class='pv-slide'>"+slideHtml(x)+"</div>";
    FIGS={};ANIMS={};IMGS={};
    stage.scrollTop=0;
    animInit(stage);
    stage.querySelectorAll(".pv-vis figure.fig:not(.pimg):not(.anim):not(.a3d)").forEach(function(fg){coverFig(fg);});
    P.el.querySelector(".pv-prog i").style.width=Math.round(P.i*100/(P.S.length-1))+"%";
    P.el.querySelector(".pv-count").textContent=(P.i+1)+" / "+P.S.length;
    P.el.querySelector("[data-pv='prev']").disabled=P.i===0;
    var nx=P.el.querySelector("[data-pv='next']"),last=P.i===P.S.length-1;nx.disabled=last;nx.classList.toggle("primary",!last);
    nx.textContent=P.i===P.S.length-2?"สรุป →":"ถัดไป →";
    var nb=P.el.querySelector("[data-pv='notes']");nb.setAttribute("aria-pressed",P.notes?"true":"false");nb.textContent=P.notes?"ซ่อนโน้ต":"โน้ต";
    var sel=P.el.querySelector("select"),si=x.s?x.si:-1;sel.value=String(si);
    P.el.querySelector(".pv-bot .sp").textContent=x.s?label(x):(x.type==="cover"?"ปก":"สรุป");
  }
  function clock(){
    var el=P.el&&P.el.querySelector(".pv-time");if(!el)return;
    var s=Math.floor((Date.now()-P.t0)/1000);el.textContent=Math.floor(s/60)+":"+("0"+s%60).slice(-2);
  }
  function close(){
    if(!P.el)return;
    clearInterval(P.tick);P.tick=null;P.el.remove();P.el=null;
    document.documentElement.style.overflow="";
    if(P.back&&P.back.focus)try{P.back.focus();}catch(e){}
  }
  function open(lecId,secId,from){
    var l=lecOf(lecId);if(!l||!l.sections.length)return;
    P.lec=l;P.S=build(l);P.notes=false;P.t0=Date.now();P.back=from||null;
    var el=document.createElement("div");el.className="pv";el.setAttribute("role","dialog");el.setAttribute("aria-modal","true");
    el.setAttribute("aria-label","โหมดพรีเซนต์ คาบ "+l.lec);el.tabIndex=-1;
    el.innerHTML="<div class='pv-top'><button class='btn' data-pv='close' aria-label='ออกจากโหมดพรีเซนต์'>✕ ออก</button>"+
      "<select aria-label='ไปที่หัวข้อ'><option value='-1'>ปก / สรุป</option>"+l.sections.map(function(s,i){return "<option value='"+i+"'>"+(i+1)+". "+esc(plain(s.title))+"</option>";}).join("")+"</select>"+
      "<button class='btn' data-pv='notes' aria-pressed='false'>โน้ต</button>"+
      "<span class='pv-meta'><span class='pv-count'></span><span class='pv-time'>0:00</span></span></div>"+
      "<div class='pv-prog'><i></i></div><div class='pv-stage' aria-live='polite'></div>"+
      "<div class='pv-bot'><button class='btn' data-pv='prev'>← ก่อนหน้า</button><span class='sp'></span><button class='btn primary' data-pv='next'>ถัดไป →</button></div>";
    document.documentElement.appendChild(el);P.el=el;
    document.documentElement.style.overflow="hidden";
    el.querySelector("select").addEventListener("change",function(e){
      var v=+e.target.value;
      if(v<0){show(0);return;}
      for(var i=0;i<P.S.length;i++)if(P.S[i].type==="sec"&&P.S[i].si===v){show(i);return;}
    });
    var tx=0,ty=0,ok=false,stage=el.querySelector(".pv-stage");
    stage.addEventListener("touchstart",function(e){var t=e.touches[0];ok=!(e.target.closest&&e.target.closest(".figsv,.tablewrap,.pv-notes"));tx=t.clientX;ty=t.clientY;},{passive:true});
    stage.addEventListener("touchend",function(e){if(!ok)return;var t=e.changedTouches[0],dx=t.clientX-tx,dy=t.clientY-ty;
      if(Math.abs(dx)>60&&Math.abs(dy)<45)show(P.i+(dx<0?1:-1));},{passive:true});
    P.tick=setInterval(clock,1000);
    var start=0;
    if(secId)for(var i=0;i<P.S.length;i++)if(P.S[i].type==="sec"&&P.S[i].s.id===secId){start=i;break;}
    show(start);el.focus();
  }
  document.addEventListener("click",function(e){
    if(!P.el)return;
    var b=e.target.closest&&e.target.closest(".pv button");if(!b)return;
    var a=b.getAttribute("data-pv");
    if(a==="close"){close();return;}
    if(a==="prev"){show(P.i-1);return;}
    if(a==="next"){show(P.i+1);return;}
    if(a==="notes"){P.notes=!P.notes;var y=P.el.querySelector(".pv-stage").scrollTop;show(P.i);if(P.notes){var n=P.el.querySelector(".pv-notes");if(n)n.scrollIntoView({block:"nearest"});}else P.el.querySelector(".pv-stage").scrollTop=y;return;}
    if(b.hasAttribute("data-pvgo")){show(+b.getAttribute("data-pvgo"));return;}
    var r=b.getAttribute("data-pvr");
    if(r){var x=P.S[P.i],k=rk(x.key);
      if(state.rate[k]===r)delete state.rate[k];else state.rate[k]=r;
      save();
      if(state.rate[k]==="ok"&&P.i<P.S.length-1)show(P.i+1);else{var y2=P.el.querySelector(".pv-stage").scrollTop;show(P.i);P.el.querySelector(".pv-stage").scrollTop=y2;}
    }
  });
  document.addEventListener("keydown",function(e){
    if(!P.el)return;
    var tg=e.target&&e.target.tagName;
    if(tg==="SELECT"||tg==="TEXTAREA"||tg==="INPUT")return;
    if(e.key==="Escape"){e.preventDefault();close();return;}
    if(e.key==="ArrowRight"||e.key==="PageDown"){e.preventDefault();show(P.i+1);return;}
    if(e.key==="ArrowLeft"||e.key==="PageUp"){e.preventDefault();show(P.i-1);return;}
    if((e.key==="n"||e.key==="N")&&!e.metaKey&&!e.ctrlKey){e.preventDefault();P.el.querySelector("[data-pv='notes']").click();}
  });
  return {open:open,close:close};
})();
"""

# CSS ต่อท้าย stylesheet ของหน้า
anchor = "\n</style>\n\n<svg width=\"0\""
assert h.count(anchor) == 1
h = h.replace(anchor, CSS + anchor)

# JS ก่อน boot
anchor = "renderSync();\nboot();"
assert h.count(anchor) == 1
h = h.replace(anchor, JS + anchor)

# ปุ่มในการ์ดคาบ (ปุ่มหลักของการ์ด)
old = "(hid?\"<span class='chip rvon'>โหมดทวน · ซ่อนเนื้อหาอยู่</span>\":\"\")+hideBtn(l)+\"</div>\";"
assert h.count(old) == 1
h = h.replace(old, "(hid?\"<span class='chip rvon'>โหมดทวน · ซ่อนเนื้อหาอยู่</span>\":\"\")+"
              "\"<button class='btn primary' data-act='present' data-plec='\"+esc(l.lec)+\"' title='อธิบายทั้งคาบให้คนอื่นฟัง บนจอมีแค่ keyword'>▶ พรีเซนต์คาบนี้</button>\"+hideBtn(l)+\"</div>\";")

# ปุ่มในหน้าหัวข้อ (ปุ่มรอง เริ่มจากหัวข้อนี้)
old = "nlChips(s.nl)+hideBtn(l)+"
assert h.count(old) == 1
h = h.replace(old, "nlChips(s.nl)+\"<button class='btn' data-act='present' data-plec='\"+esc(l.lec)+\"' data-psec='\"+esc(s.id)+\"'>▶ พรีเซนต์จากหัวข้อนี้</button>\"+hideBtn(l)+")

# ตัวจัดการคลิก
old = "  if(t.dataset.act===\"hidelec\"){"
assert h.count(old) == 1
h = h.replace(old, "  if(t.dataset.act===\"present\"){Pres.open(t.dataset.plec,t.dataset.psec||\"\",t);return;}\n" + old)

open(DST, "w", encoding="utf-8").write(h)
print("ok", len(h))
