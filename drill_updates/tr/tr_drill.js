
/* ===================== โครงหน้าแบบ Teaching Round สำหรับ Ward Drill (ผู้ใช้ขอ 9 พ.ย. 2569) =====================
   ทุกฟังก์ชันเดิมยังอยู่ — ชั้นนี้แค่จัดที่ใหม่: หน้าแรก (การ์ดเขียว + วงแหวน + การ์ดระบบ) · แถบล่าง/แถบซ้าย ·
   หน้าต่างระบบ (bottom sheet) · ตัวกรองบนมือถือ (ย้ายแถบ rail เดิมเข้า sheet) · วงล้อทางลัด · วงล้อสลับคาบ ·
   ปัดซ้าย-ขวา · ค้นหา Ctrl K · แถบขวา · ย่อ/ขยายเนื้อหา · ซ่อนแถบซ้าย/ขวา · ประวัติการทำรายวัน (state.log ซิงก์บัญชี) */
var TR=(function(){
  var RM=false;try{RM=matchMedia("(prefers-reduced-motion: reduce)").matches;}catch(e){}
  var de=document.documentElement;
  var DESK=matchMedia("(min-width:1100px)"),WIDE=matchMedia("(min-width:1400px)"),NARROW=matchMedia("(max-width:899px)");
  var UIKEY="med421-drill-ui",THKEY="med421-drill-theme",FZKEY="med421-drill-fz",PNKEY="med421-drill-panes",PINKEY="med421-drill-pins";
  var GOAL=20,EXAM="2026-11-17",POSTIT="https://claude.ai/artifact/BRsYSzd35CARo2m6Jw6ANY";
  var NAME={cardio:"หัวใจและหลอดเลือด",nephro:"ไตและสมดุลน้ำ เกลือแร่",chest:"ระบบหายใจ",neuro:"ระบบประสาท",air:"ภูมิแพ้ ภูมิคุ้มกัน รูมาติสซั่ม",
    infect:"โรคติดเชื้อ",gi:"ทางเดินอาหารและตับ",endo:"ต่อมไร้ท่อ",heme:"โลหิตวิทยา",derm:"ผิวหนัง",onco:"มะเร็งวิทยา",mock:"ชุดจำลอง NL Part 1"};
  function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||"null");if(v===null)localStorage.removeItem(k);else localStorage.setItem(k,JSON.stringify(v));}catch(e){return null;}}
  function el(t,c,h){var x=document.createElement(t);if(c)x.className=c;if(h!=null)x.innerHTML=h;return x;}
  function pad(n){return (n<10?"0":"")+n;}
  function dkey(d){d=d||new Date();return d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate());}
  var WD=["อา.","จ.","อ.","พ.","พฤ.","ศ.","ส."],MO=["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."];
  function thaiDate(d){return WD[d.getDay()]+" "+d.getDate()+" "+MO[d.getMonth()];}
  function setLbl(k){var s=SETS.filter(function(x){return x.k===k;})[0];return s?s.label:k;}
  function modeLbl(k){var m=MODES.filter(function(x){return x.k===k;})[0];return m?m.label:k;}

  /* ---------- หน้าที่กำลังดู (home / drill) — จำไว้ในเครื่องนี้ ---------- */
  var V={view:"home",dir:0};var u0=ls(UIKEY);if(u0&&u0.view==="drill")V.view="drill";
  if(String(location.hash||"").length>1)V.view="drill";
  function keepUI(){ls(UIKEY,{view:V.view});}

  /* ---------- โหมดสี (ตามเครื่อง / มืด / สว่าง) ---------- */
  var TH="";try{TH=localStorage.getItem(THKEY)||"";}catch(e){}if(TH!=="dark"&&TH!=="light")TH="";
  function thApply(){if(TH)de.setAttribute("data-theme",TH);else de.removeAttribute("data-theme");}
  function thName(){return TH==="dark"?"มืด":TH==="light"?"สว่าง":"ตามเครื่อง";}
  function thCycle(){TH=TH===""?"dark":TH==="dark"?"light":"";try{if(TH)localStorage.setItem(THKEY,TH);else localStorage.removeItem(THKEY);}catch(e){}thApply();toast("โหมดสี: "+thName());paint();}
  thApply();

  /* ---------- toast ---------- */
  var toastEl=el("div","tr-toast");toastEl.setAttribute("role","status");toastEl.setAttribute("aria-live","polite");de.appendChild(toastEl);var toastT=null;
  function toast(m){toastEl.textContent=m;toastEl.classList.add("on");clearTimeout(toastT);toastT=setTimeout(function(){toastEl.classList.remove("on");},1400);}
  function pop(n){if(RM||!n)return;n.classList.remove("tr-pop");void n.offsetWidth;n.classList.add("tr-pop");}
  function flash(n){if(!n)return;n.classList.remove("tr-flash");void n.offsetWidth;n.classList.add("tr-flash");}

  /* ---------- ย่อ/ขยายขนาดเนื้อหา — จำไว้ในเครื่องนี้ ---------- */
  var FZS=[.8,.9,1,1.1,1.2,1.35,1.5],FZ=1;var fz0=parseFloat(ls(FZKEY));if(FZS.indexOf(fz0)>=0)FZ=fz0;
  function fzApply(){de.style.setProperty("--fz",String(FZ));
    [].forEach.call(document.querySelectorAll(".tr-fz"),function(g){var o=g.querySelector("output");if(o)o.textContent=Math.round(FZ*100)+"%";
      var i=FZS.indexOf(FZ);g.querySelector("[data-trfz='-1']").disabled=i<=0;g.querySelector("[data-trfz='1']").disabled=i>=FZS.length-1;var r=g.querySelector("[data-trfz='0']");if(r)r.hidden=FZ===1;});}
  function fzStep(d){var i=FZS.indexOf(FZ);if(i<0)i=2;FZ=d===0?1:FZS[Math.max(0,Math.min(FZS.length-1,i+d))];ls(FZKEY,FZ===1?null:FZ);fzApply();}
  function fzBar(){var g=el("div","tr-fz");g.setAttribute("role","group");g.setAttribute("aria-label","ขนาดเนื้อหา");
    g.innerHTML="<span class='tr-fz-l'>ขนาดเนื้อหา</span><button type='button' class='press' data-trfz='-1' aria-label='ย่อเนื้อหา' title='ย่อ (ปุ่ม -)'>ก−</button><output aria-live='polite'>100%</output><button type='button' class='press' data-trfz='1' aria-label='ขยายเนื้อหา' title='ขยาย (ปุ่ม =)'>ก+</button><button type='button' class='press tr-fz-r' data-trfz='0' hidden>คืนค่า</button>";return g;}

  /* ---------- ซ่อนแถบซ้าย/ขวาบนคอม — จำไว้ในเครื่องนี้ ---------- */
  var PN={s:0,d:0};var pn0=ls(PNKEY);if(pn0){PN.s=pn0.s?1:0;PN.d=pn0.d?1:0;}
  var CHL='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>',
      CHR='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>';
  var rail={};
  function paneApply(){de.classList.toggle("tr-noside",!!PN.s);de.classList.toggle("tr-nodock",!!PN.d);
    if(!rail.s){rail.s=el("button","tr-rail tr-rail-l press",CHR+"<span>เมนู</span>");rail.s.type="button";rail.s.dataset.trpane="s";rail.s.setAttribute("aria-label","แสดงแถบซ้าย");rail.s.title="แสดงแถบซ้าย (ปุ่ม [)";
      rail.d=el("button","tr-rail tr-rail-r press",CHL+"<span>คะแนน</span>");rail.d.type="button";rail.d.dataset.trpane="d";rail.d.setAttribute("aria-label","แสดงแถบขวา");rail.d.title="แสดงแถบขวา (ปุ่ม ])";
      document.body.appendChild(rail.s);document.body.appendChild(rail.d);}}
  function paneToggle(k){PN[k]=PN[k]?0:1;ls(PNKEY,PN);paneApply();
    var a=document.activeElement;if(a&&a.dataset&&a.dataset.trpane){var f=PN[k]?rail[k]:document.querySelector(k==="s"?".tr-side [data-trpane]":".tr-dock [data-trpane]");if(f)try{f.focus({preventScroll:true});}catch(e){}}}

  /* ---------- ประวัติการทำรายวัน (นับข้อที่ตอบเอง/เปิดเฉลย MEQ ในวันนั้น) ---------- */
  function logToday(id){if(!id)return false;state.log=state.log||{};var k=dkey(),a=state.log[k]||[];
    if(a.indexOf(id)>=0)return false;a.push(id);state.log[k]=a.slice(-300);return true;}
  function dayCount(d){var a=(state.log||{})[dkey(d)];return a?a.length:0;}
  function streak(){var n=0,d=new Date();if(!dayCount(d))d.setDate(d.getDate()-1);while(dayCount(d)){n++;d.setDate(d.getDate()-1);}return n;}
  var pend=[];
  document.addEventListener("click",function(e){
    var b=e.target.closest&&e.target.closest(".choice,.reveal");if(!b||b.disabled)return;
    var a=b.closest("article.item[id^='it-']");if(a)pend.push(a.id.slice(3).replace(/--.*$/,""));
  },true);
  function flushPend(){if(!pend.length)return;var ids=pend,ch=false;pend=[];
    ids.forEach(function(id){var a=state.answers[id],sh=false;
      if(!(a&&!a.auto))for(var k in state.shown){if(k.indexOf(id+"#")===0){sh=true;break;}}
      if((a&&!a.auto)||sh){if(logToday(id))ch=true;}});
    if(ch)save();}

  /* ---------- ดัชนีข้อทั้งหมด ---------- */
  var IX=null;
  function idx(){if(IX)return IX;IX={};
    SETS.forEach(function(s){var B=BANK[s.k];if(!B)return;
      B.mcq.forEach(function(it){IX[it.id]={it:it,set:s.k,kind:"mcq",lec:it.lec,lecture:it.lecture};});
      B.meq.forEach(function(it){IX[it.id]={it:it,set:s.k,kind:"meq",lec:it.lec,lecture:it.lecture};});
      (B.old||[]).forEach(function(g){g.items.forEach(function(it){IX[it.id]={it:it,set:s.k,kind:"old",lec:it.lec||g.lec,lecture:it.lecture||g.lecture};});});});
    return IX;}
  function setStat(k){var B=BANK[k],t=0,d=0,r=0,w=0;
    function f(it){if(!it.choices)return;t++;var a=state.answers[it.id];if(a&&!a.auto){d++;if(a.ok)r++;else w++;}}
    B.mcq.forEach(f);(B.old||[]).forEach(function(g){g.items.forEach(f);});
    return {t:t,d:d,r:r,w:w,meq:B.meq.length};}
  function allStat(){var o={t:0,d:0,r:0,w:0,by:{}};SETS.forEach(function(s){var x=setStat(s.k);o.by[s.k]=x;o.t+=x.t;o.d+=x.d;o.r+=x.r;o.w+=x.w;});return o;}
  function wrongIn(set){var out=[],X=idx();Object.keys(X).forEach(function(id){var e=X[id];if(set&&e.set!==set)return;var a=state.answers[id];if(a&&!a.ok&&!a.auto)out.push(e);});return out;}
  function lecNum(a){var n=parseFloat(a);return isNaN(n)?1e9:n;}
  function lecsOf(k){var B=BANK[k],m={},out=[];
    function add(lec,name,kind,it){if(!lec)return;var L=m[lec];if(!L){L=m[lec]={lec:lec,name:name||"",n:0,o:0,t:0,d:0};out.push(L);}
      if(!L.name&&name)L.name=name;if(kind==="old")L.o++;else L.n++;
      if(it.choices){L.t++;var a=state.answers[it.id];if(a&&!a.auto)L.d++;}}
    B.mcq.concat(B.meq).forEach(function(it){add(it.lec,it.lecture,"new",it);});
    (B.old||[]).forEach(function(g){g.items.forEach(function(it){add(it.lec||g.lec,it.lecture||g.lecture,"old",it);});});
    out.sort(function(a,b){return lecNum(a.lec)-lecNum(b.lec)||String(a.lec).localeCompare(String(b.lec));});return out;}
  function modeCount(k,set){set=set||state.set;var B=BANK[set];
    if(k==="new")return newItems(set).length;
    if(k==="old")return (B.old||[]).reduce(function(a,g){return a+g.items.length;},0);
    if(k==="year")return yearItems(set).length;
    if(k==="hot")return hotList(set).length;
    if(k==="pic")return picItems("all").length;
    if(k==="yearall")return yaAll().length;
    if(k==="review")return rvUnits().length;
    return 1;}
  function firstOpen(set){var B=BANK[set],f=null;
    B.mcq.some(function(it){if(!state.answers[it.id]){f={it:it,kind:"mcq",lec:it.lec};return true;}return false;});
    if(f)return f;
    (B.old||[]).some(function(g){return g.items.some(function(it){if(it.choices&&!state.answers[it.id]){f={it:it,kind:"old",lec:it.lec||g.lec};return true;}return false;});});
    return f;}
  function examDays(){var t=new Date(EXAM+"T00:00:00"),n=new Date();n.setHours(0,0,0,0);return Math.round((t-n)/864e5);}

  /* ---------- ไอคอน ---------- */
  var S='<svg viewBox="0 0 24 24" aria-hidden="true">';
  var I={
    home:S+'<path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5H15v-6H9v6H5.5A1.5 1.5 0 0 1 4 19z"/></svg>',
    drill:S+'<rect x="4.5" y="3.5" width="15" height="17" rx="2"/><path d="M8 8.5h8M8 12h8M8 15.5h5"/></svg>',
    plus:S+'<path d="M12 5v14M5 12h14"/></svg>',
    quiz:S+'<path d="M4 7h3.5c2 0 3 1 4.5 3.5S14.5 17 16.5 17H20M4 17h3.5c1.2 0 2-.4 2.8-1.2M14.2 8.2c.7-.8 1.5-1.2 2.3-1.2H20M17.5 4.5 20 7l-2.5 2.5M17.5 14.5 20 17l-2.5 2.5"/></svg>',
    review:S+'<path d="M4.5 12a7.5 7.5 0 1 0 2.2-5.3M4.5 4.5v3.7h3.7"/><path d="M12 8.5V12l2.5 2"/></svg>',
    "new":S+'<path d="M7 3.5h7l4.5 4.5v11A1.5 1.5 0 0 1 17 20.5H7A1.5 1.5 0 0 1 5.5 19V5A1.5 1.5 0 0 1 7 3.5z"/><path d="M12 10.5v6M9 13.5h6"/></svg>',
    old:S+'<rect x="3.5" y="4.5" width="17" height="4" rx="1"/><path d="M5 8.5V18a1.5 1.5 0 0 0 1.5 1.5h11A1.5 1.5 0 0 0 19 18V8.5M10 12.5h4"/></svg>',
    year:S+'<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/></svg>',
    hot:S+'<path d="M12 21c3.6 0 6-2.4 6-5.8 0-3.4-2.6-5.2-3.4-8.7-1.6 1.6-2.2 3.2-2.2 4.6-1-.8-1.7-2-1.8-3.6C8.2 9.3 6 12 6 15.2 6 18.6 8.4 21 12 21z"/></svg>',
    yearall:S+'<path d="M12 4 3.5 8.5 12 13l8.5-4.5z"/><path d="M3.5 12.5 12 17l8.5-4.5M3.5 16.5 12 21l8.5-4.5"/></svg>',
    pic:S+'<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M20.5 16l-5-5-8.5 8.5"/></svg>',
    wrong:S+'<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/></svg>',
    swap:S+'<path d="M7 7h11l-3-3M17 17H6l3 3"/></svg>',
    search:S+'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>',
    ai:S+'<path d="M12 3.5l1.9 4.8 4.8 1.9-4.8 1.9L12 16.9l-1.9-4.8-4.8-1.9 4.8-1.9zM18.5 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/></svg>',
    pin:S+'<path d="M5.5 4.5h13v10l-5 5h-8z"/><path d="M13.5 19.5v-5h5"/></svg>',
    theme:S+'<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"/></svg>',
    filter:S+'<path d="M4 6h16M7 12h10M10 18h4"/></svg>'
  };

  /* ---------- นำทาง ---------- */
  function top0(){window.scrollTo({top:0});}
  function go(view){V.view=view;keepUI();render();top0();}
  function pageOf(){if(V.view==="home")return "home";if(state.mode==="quiz")return "quiz";if(state.mode==="review")return "review";return "drill";}
  function goPage(p){
    if(p==="home")return go("home");
    if(p==="drill"){if(state.mode==="quiz"||state.mode==="review")state.mode="new";}
    else state.mode=p;
    save();go("drill");}
  function setMode(k){
    if(k!=="quiz"&&k!=="review"&&!modeCount(k)){toast("ระบบ "+setLbl(state.set)+" ไม่มี “"+modeLbl(k)+"”");return;}
    state.mode=k;if(k!=="new")state.part="all";save();go("drill");}
  function setSet(k,stay){
    if(!BANK[k])return;
    if(state.mode==="review"||state.mode==="yearall"||state.mode==="pic")state.mode="new";
    state.set=k;state.lec="all";save();
    if(!stay)V.view=V.view==="home"?"home":"drill";keepUI();render();if(V.view!=="home")top0();}
  function goLec(k,lec){state.set=k;state.part="all";state.lec=lec;
    var hasNew=newItems(k).some(function(it){return it.lec===lec;});
    if(state.mode==="old"&&BANK[k].old.some(function(g){return g.lec===lec;}))state.mode="old";
    else state.mode=hasNew?"new":"old";
    save();go("drill");}
  function scrollToItem(id){var n=document.getElementById("it-"+id);if(!n)return;
    try{n.scrollIntoView({block:"start",behavior:RM?"auto":"smooth"});}catch(e){n.scrollIntoView();}flash(n);}
  function jump(id){var e=idx()[id];if(!e)return;
    state.set=e.set;state.part="all";state.lec=e.lec;state.mode=e.kind==="old"?"old":"new";
    save();V.view="drill";keepUI();render();setTimeout(function(){scrollToItem(id);},60);}
  function openNext(){var f=firstOpen(state.set);
    if(!f){toast("ทำครบทุกข้อของ "+setLbl(state.set)+" แล้ว");return;}jump(f.it.id);}
  function wrongQuiz(){
    if(!wrongIn().length){toast("ยังไม่มีข้อที่ตอบผิด");return;}
    quiz.scope="all";quiz.pool="wrong";state.mode="quiz";save();V.view="drill";keepUI();qDraw();toast("สุ่มจากข้อที่เคยตอบผิด");}
  function aiOpen(){
    var fab=document.querySelector(".aiw-fab"),pn=document.querySelector(".aiw-panel");
    if(pn&&!pn.hidden){var ta=pn.querySelector("textarea");if(ta)ta.focus();return;}
    if(fab&&!fab.hidden){fab.click();return;}
    toast("ถาม AI ใช้ได้เมื่อเปิดหน้านี้ใน claude.ai ขณะล็อกอิน");}
  function lecShiftList(){return ["all"].concat(lecList().map(function(L){return L.lec;}));}
  function shift(k){
    if(V.view==="home"){var a=SETS.map(function(s){return s.k;}),i=a.indexOf(state.set),j=i+k;
      if(j<0||j>=a.length){toast(k<0?"นี่คือระบบแรกแล้ว":"นี่คือระบบสุดท้ายแล้ว");return;}
      V.dir=k;state.set=a[j];state.lec="all";save();render();toast((k<0?"‹ ":"")+SETS[j].label+(k>0?" ›":""));return;}
    if(["new","old","year","hot"].indexOf(state.mode)<0){toast("ปัดเปลี่ยนคาบใช้ได้ในข้อสอบใหม่ คลังเก่า ตามปี และออกบ่อย");return;}
    var L=lecShiftList(),i2=L.indexOf(state.lec),j2=i2+k;
    if(i2<0||j2<0||j2>=L.length){toast(k<0?"นี่คือคาบแรกแล้ว":"นี่คือคาบสุดท้ายแล้ว");return;}
    state.lec=L[j2];V.dir=k;render();top0();
    if(state.lec==="all")toast("ทุกหัวข้อ");else{var m=lecList().filter(function(x){return x.lec===state.lec;})[0];toast("Lec "+state.lec+(m?" "+shortName(m.name).slice(0,32):""));}}

  /* ---------- หน้าแรก ---------- */
  var home=document.getElementById("trHome");
  function viewHome(){
    var A=allStat(),now=new Date(),t=dayCount(now),ed=examDays(),cs=A.by[state.set],nx=firstOpen(state.set),acc=A.d?Math.round(A.r/A.d*100):0;
    var h="<section class='tr-home"+(V.dir>0?" tr-slide-l":V.dir<0?" tr-slide-r":"")+"'>";
    h+="<div class='tr-top'><div><h1>Ward Drill</h1><div class='tr-thai'>ข้อสอบ MED421/422 · "+SETS.length+" ระบบ</div><span class='tr-syncm'><i></i><span></span></span></div><div class='tr-top-r'>"+
      "<button type='button' class='tr-srch press' data-trpal='1' aria-label='ค้นหาข้อสอบ' title='ค้นหา (Ctrl K)'>"+I.search+"</button>"+
      (ed>=0?"<div class='tr-exam' title='สอบลงกอง 17–18 พ.ย.'><b>"+(ed?"อีก "+ed+" วัน":"วันนี้")+"</b><small>สอบลงกอง 17 พ.ย.</small></div>":"")+"</div></div>";
    h+="<div class='tr-hero-row'><section class='tr-hero' aria-label='ทำข้อสอบวันนี้'><div class='tr-hero-r'><div class='tr-hero-t'>"+
      "<span class='tr-kicker'>วันนี้ "+thaiDate(now)+"</span><h2>ทำข้อสอบวันนี้</h2><p>"+(t>=GOAL?"ครบเป้าแล้ว ทำไป "+t+" ข้อ":"ทำไปแล้ว "+t+" ข้อ จากเป้า "+GOAL+" ข้อ")+"</p></div>"+
      "<div class='tr-ring' style='--p:"+Math.min(1,t/GOAL).toFixed(2)+"' role='img' aria-label='ทำแล้ว "+t+" จาก "+GOAL+" ข้อ'><div class='tr-ring-in'><b>"+t+"/"+GOAL+"</b><small>ข้อ</small></div></div></div>"+
      (nx?"<button type='button' class='tr-next press' data-trnext='1'><span><small>ทำต่อ · "+esc(setLbl(state.set))+" · Lec "+esc(nx.lec)+"</small><b>"+esc(nx.it.topic||nx.it.q||nx.it.id)+"</b></span><i aria-hidden='true'>→</i></button>"
         :"<button type='button' class='tr-next press' data-trwrong='1'><span><small>"+esc(setLbl(state.set))+" ทำครบทุกข้อแล้ว</small><b>สุ่มทำข้อที่เคยตอบผิด</b></span><i aria-hidden='true'>→</i></button>")+"</section>";
    var days=[],mx=1;for(var i=6;i>=0;i--){var d=new Date();d.setDate(d.getDate()-i);var v=dayCount(d);mx=Math.max(mx,v);days.push([d,v,i===0]);}
    var tot=days.reduce(function(a,x){return a+x[1];},0),sk=streak();
    h+="<section class='tr-week' aria-label='7 วันล่าสุด'><h3>7 วันล่าสุด</h3><p>"+(sk?"ทำติดกัน "+sk+" วัน · ":"")+"รวม "+tot+" ข้อ</p><div class='tr-bars'>"+
      days.map(function(x){return "<div class='"+(x[2]?"today":"")+"'><b>"+x[1]+"</b><i style='height:"+Math.max(6,Math.round(x[1]/mx*80))+"px'></i><span>"+WD[x[0].getDay()].replace(".","")+"</span></div>";}).join("")+"</div></section></div>";
    h+="<div class='tr-tiles'>"+
      "<button type='button' class='tr-tile press' data-trpage='drill'><small>ตอบเองแล้ว</small><b>"+A.d+"<em>/"+A.t+"</em></b></button>"+
      "<button type='button' class='tr-tile press' data-trpage='drill'><small>ความแม่น</small><b>"+(A.d?acc+"<em>%</em>":"—")+"</b></button>"+
      "<button type='button' class='tr-tile press"+(A.w?" warn":"")+"' data-trwrong='1'><small>ข้อที่ผิด รอทวน</small><b>"+A.w+"</b></button>"+
      "<button type='button' class='tr-tile press tr-desk' data-trpage='review'><small>คาบที่ทวนแล้ว</small><b>"+rvUnits().length+"<em> คาบ</em></b></button></div>";
    h+="<div class='tr-whead'><h3>ระบบ</h3><span>แตะเพื่อเลือกคาบ</span></div><div class='tr-grid'>";
    SETS.forEach(function(s){var x=A.by[s.k],full=x.t&&x.d>=x.t,cur=s.k===state.set,pc=x.t?Math.round(x.d*100/x.t):0,nL=lecsOf(s.k).length;
      h+="<button type='button' class='tr-card press"+(full?" done":"")+(cur?" cur":"")+"' data-trset='"+esc(s.k)+"' aria-label='"+esc(s.label)+" ทำแล้ว "+x.d+" จาก "+x.t+" ข้อ'>"+
        "<div class='tr-c-top'><span class='tr-c-no'>"+esc(s.label)+"</span>"+(cur?"<span class='tr-c-day'>กำลังทำ</span>":"")+"</div>"+
        "<div class='tr-c-t'>"+esc(NAME[s.k]||"")+" · "+nL+" คาบ</div>"+
        "<div class='tr-c-n'><b>"+x.d+"</b> / "+x.t+" ข้อ</div><div class='tr-c-bar'><i style='width:"+pc+"%'></i></div>"+
        "<div class='tr-c-foot'><span class='tr-tag "+(full?"ok":x.d?"go":"")+"'>"+(full?"✓ ครบแล้ว":x.d?"แม่น "+Math.round(x.r*100/x.d)+"%":"ยังไม่เริ่ม")+"</span>"+
        (x.w?"<span class='tr-tag bad'>ผิด "+x.w+"</span>":"")+(x.meq?"<span class='tr-tag'>MEQ/OSCE "+x.meq+"</span>":"")+"</div></button>";});
    h+="</div><p class='tr-hint'>ดับเบิลคลิกพื้นที่ว่าง หรือกดค้าง 2 วินาที เพื่อหมุนเลือกคาบ · ปัดซ้าย-ขวาเพื่อเปลี่ยนระบบ</p>";
    var bp=document.querySelector(".brand p"),ft=document.querySelector("footer.foot p");
    h+="<details class='tr-about'><summary>เกี่ยวกับ Ward Drill และที่มาของข้อสอบ</summary><div>"+(bp?"<p>"+bp.innerHTML+"</p>":"")+(ft?"<p>"+ft.innerHTML+"</p>":"")+
      "<button type='button' class='tr-btn press' data-trtheme='1'>โหมดสี: "+thName()+"</button></div></details>";
    home.innerHTML=h+"</section>";
  }

  /* ---------- หน้าต่างเลื่อนขึ้นจากด้านล่าง ---------- */
  var sh=el("dialog","tr-sheet");sh.setAttribute("aria-labelledby","trShT");document.body.appendChild(sh);var shClosing=false,railHome=null;
  function restoreRail(){if(!railHome)return;var r=document.querySelector(".tr-sheet .rail");if(r)railHome.p.insertBefore(r,railHome.n);railHome=null;}
  function closeSheet(after){if(shClosing||!sh.open){restoreRail();if(after)after();return;}shClosing=true;sh.classList.add("out");
    setTimeout(function(){if(sh.open)sh.close();sh.classList.remove("out");shClosing=false;restoreRail();if(after)after();},RM?0:170);}
  sh.addEventListener("cancel",function(e){e.preventDefault();closeSheet();});
  sh.addEventListener("click",function(e){if(e.target===sh)closeSheet();});
  function sheetHead(small,title){sh.innerHTML="<div class='tr-grab'></div>";
    var hd=el("div","tr-sh-head");hd.appendChild(el("div","tr-sh-ht","<small>"+small+"</small><h3 id='trShT'>"+title+"</h3>"));
    var x=el("button","tr-x press","✕");x.type="button";x.setAttribute("aria-label","ปิด");x.addEventListener("click",function(){closeSheet();});hd.appendChild(x);sh.appendChild(hd);}
  function openSetSheet(k){
    if(!BANK[k])return;restoreRail();var x=setStat(k),L=lecsOf(k);
    sheetHead(esc(setLbl(k))+" · ทำแล้ว "+x.d+"/"+x.t+" ข้อ"+(x.d?" · แม่น "+Math.round(x.r*100/x.d)+"%":""),esc(NAME[k]||setLbl(k)));
    var body=el("div","tr-sh-body"),ol=el("ol","tr-sh-list");
    L.forEach(function(l){var li=el("li"),b=el("button","press "+(l.t&&l.d>=l.t?"ok":l.d?"part":"")+(k===state.set&&state.lec===l.lec?" cur":""));b.type="button";
      b.innerHTML="<span class='num' aria-hidden='true'>"+esc(l.lec)+"</span><span class='tt'>"+esc(shortName(l.name)||("Lec "+l.lec))+"</span><span class='qq'>"+(l.n?"ใหม่ "+l.n:"")+(l.n&&l.o?"<br>":"")+(l.o?"เก่า "+l.o:"")+"</span>";
      b.setAttribute("aria-label","Lec "+l.lec+" "+shortName(l.name)+" ทำแล้ว "+l.d+" จาก "+l.t);
      b.addEventListener("click",function(){closeSheet(function(){goLec(k,l.lec);});});li.appendChild(b);ol.appendChild(li);});
    body.appendChild(ol);sh.appendChild(body);
    var ft=el("div","tr-sh-foot"),p=el("button","tr-btn primary press","ทำข้อสอบใหม่ทั้งระบบ · "+newItems(k).length+" ข้อ");p.type="button";
    p.addEventListener("click",function(){closeSheet(function(){state.set=k;state.lec="all";state.part="all";state.mode="new";save();go("drill");});});ft.appendChild(p);
    var ac=el("div","tr-sh-acts");
    [["old","คลังข้อสอบเก่า"],["year","MEQ/OSCE ตามปี"],["hot","ออกบ่อย"]].forEach(function(m){var n=modeCount(m[0],k);if(!n)return;
      var b=el("button","tr-btn press",esc(m[1])+" "+n);b.type="button";
      b.addEventListener("click",function(){closeSheet(function(){state.set=k;state.lec="all";state.part="all";state.mode=m[0];save();go("drill");});});ac.appendChild(b);});
    if(ac.children.length)ft.appendChild(ac);sh.appendChild(ft);sh.showModal();}
  function filtSummary(){var m=state.mode;
    if(["new","old","year","hot"].indexOf(m)>=0){if(state.lec==="all")return "ทุกคาบ"+(m==="new"&&state.part!=="all"?" · "+state.part:"");
      var x=lecList().filter(function(L){return L.lec===state.lec;})[0];return "Lec "+state.lec+(x?" "+shortName(x.name):"");}
    if(m==="quiz")return "ตั้งค่าชุดสุ่ม";if(m==="yearall")return "MED"+(YA&&YA.y?YA.y:"")+" · เลือกปีและ Part";if(m==="pic")return "เลือกข้อที่แสดง";if(m==="review")return "เลือกวันและคาบ";return "ตัวกรอง";}
  function openFilter(){
    var r=document.querySelector(".shell>.rail");if(!r)return;
    sheetHead(esc(setLbl(state.set))+" · "+esc(modeLbl(state.mode)),"ตัวกรองและปุ่มของหน้านี้");
    var body=el("div","tr-sh-body");sh.appendChild(body);
    railHome={p:r.parentNode,n:r.nextSibling};body.appendChild(r);
    var ft=el("div","tr-sh-foot"),p=el("button","tr-btn primary press","ดูข้อสอบ");p.type="button";p.addEventListener("click",function(){closeSheet();});ft.appendChild(p);sh.appendChild(ft);
    sh.showModal();}
  /* เลือกคาบในตัวกรองแล้วปิดเอง (capture: ปุ่มเดิม render ใหม่จนหลุดจาก DOM ก่อน bubble ถึง) */
  sh.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("#lecbar .lec,#rvlecs .lec");if(b&&railHome)setTimeout(function(){closeSheet();top0();},120);},true);

  /* ---------- แถบล่างลอย (มือถือ/แท็บเล็ต) ---------- */
  var nav=el("nav","tr-bnav");nav.setAttribute("aria-label","หน้าหลักของแอป");
  var NAV=[["home","หน้าแรก"],["drill","ข้อสอบ"],["plus","ทางลัด"],["quiz","สุ่มสอบ"],["review","ทวนแล้ว"]],mb=null,nb={};
  NAV.forEach(function(x){var b=el("button","tr-bn"+(x[0]==="plus"?" tr-main":""));b.type="button";
    b.appendChild(el("span","tr-bn-ic",I[x[0]]));b.appendChild(el("span","tr-bn-t",x[1]));
    if(x[0]==="plus"){mb=b;b.setAttribute("aria-haspopup","menu");b.setAttribute("aria-expanded","false");b.setAttribute("aria-label","ทางลัด");}
    else b.addEventListener("click",function(){goPage(x[0]);});
    nb[x[0]]=b;nav.appendChild(b);});
  document.body.appendChild(nav);

  /* ---------- แถบซ้าย (คอม) ---------- */
  var side=el("aside","tr-side");side.setAttribute("aria-label","เมนูหลัก");document.body.appendChild(side);
  function renderSide(A){
    var pg=pageOf();
    var h="<div class='tr-sd-top'><div class='tr-sd-brand'><b>Ward Drill</b><span>MED421/422 · ข้อสอบ</span></div><button type='button' class='tr-hide tr-hide-i press' data-trpane='s' aria-label='ซ่อนแถบซ้าย' title='ซ่อนแถบซ้าย (ปุ่ม [)'>"+CHL+"</button></div>"+
      "<button type='button' class='tr-sd-plus press' data-trplus='1'>"+I.plus+"ทางลัด</button>"+
      "<button type='button' class='tr-sd-search press' data-trpal='1'>"+I.search+"<span>ค้นหาข้อสอบ</span><span class='tr-kbd'>Ctrl K</span></button><nav class='tr-sd-nav'>";
    [["home","หน้าแรก","home"],["drill","ข้อสอบรายคาบ","drill"],["quiz","สุ่มทำข้อสอบ","quiz"],["review","คาบที่ทวนแล้ว","review"]].forEach(function(x){
      h+="<button type='button' class='press' data-trpage='"+x[0]+"'"+(pg===x[0]?" aria-current='page'":"")+">"+I[x[2]]+"<span>"+x[1]+"</span></button>";});
    h+="<button type='button' class='press' data-trwrong='1'>"+I.wrong+"<span>ข้อที่ผิด</span>"+(A.w?"<span class='n'>"+A.w+"</span>":"")+"</button>"+
      "<button type='button' class='press' data-trai='1'>"+I.ai+"<span>ถาม AI</span></button>"+
      "<button type='button' class='press' data-trpin='1'>"+I.pin+"<span>Post-it ห้ามลืม</span></button></nav><div class='tr-sd-h'>ระบบ</div><div class='tr-sd-courses'>";
    SETS.forEach(function(s){var x=A.by[s.k],pr=x.t?x.d/x.t:0;
      h+="<button type='button' class='tr-sd-c press' data-trside='"+esc(s.k)+"'"+(s.k===state.set?" aria-current='true'":"")+">"+
        "<span class='mr' style='--p:"+pr.toFixed(2)+"'></span><b>"+esc(s.label)+"<small>"+esc(NAME[s.k]||"")+"</small></b><em>"+(x.d?Math.round(pr*100)+"%":"")+"</em></button>";});
    h+="</div><div class='tr-sd-foot'><span class='tr-syncm'><i></i><span></span></span><button type='button' class='tr-btn press' data-trtheme='1'>โหมดสี: "+thName()+"</button></div>";
    side.innerHTML=h;var sf=side.querySelector(".tr-sd-foot");sf.insertBefore(fzBar(),sf.firstChild);}

  /* ---------- แถบขวา (คอมจอกว้าง) ---------- */
  var dock=el("aside","tr-dock");dock.setAttribute("aria-label","เครื่องมือข้างจอ");document.body.appendChild(dock);
  function txt(id){var n=document.getElementById(id);return n?n.textContent:"";}
  function renderDock(){
    if(!WIDE.matches){dock.innerHTML="";return;}
    var w=wrongIn(state.set),pins=(ls(PINKEY)||[]).slice(-4).reverse(),rn=document.getElementById("railnote");
    var h="<div class='tr-dk-top'><button type='button' class='tr-hide press' data-trpane='d' aria-label='ซ่อนแถบขวา' title='ซ่อนแถบขวา (ปุ่ม ])'><span>ซ่อน</span>"+CHR+"</button></div>";
    h+="<section class='tr-dk'><div class='tr-dk-h'><h3>คะแนน</h3><small>"+esc(V.view==="home"?setLbl(state.set):modeLbl(state.mode))+"</small></div><div class='tr-dk-sc'>"+
      "<div><b>"+esc(txt("sc-done"))+"</b><span>ทำแล้ว</span></div><div><b>"+esc(txt("sc-right"))+"</b><span>ถูก</span></div><div class='acc'><b>"+esc(txt("sc-acc"))+"</b><span>ความแม่น</span></div></div>"+
      (rn&&V.view!=="home"?"<p class='tr-dk-note'>"+rn.innerHTML+"</p>":"")+"</section>";
    h+="<section class='tr-dk'><div class='tr-dk-h'><h3>ข้อที่ผิดใน "+esc(setLbl(state.set))+"</h3><small>"+w.length+" ข้อ</small></div>";
    h+=w.length?"<ul class='tr-wl'>"+w.slice(-5).reverse().map(function(e){return "<li><button type='button' class='press' data-trjump='"+esc(e.it.id)+"'><small>"+esc(e.it.id)+" · Lec "+esc(e.lec)+"</small><span>"+esc(e.it.topic||e.it.q||"")+"</span></button></li>";}).join("")+"</ul>"
      :"<p class='tr-empty'>ยังไม่มีข้อที่ตอบผิดในระบบนี้</p>";
    h+="</section><section class='tr-dk'><div class='tr-dk-h'><h3>ปักจากหน้านี้ล่าสุด</h3><small>เครื่องนี้</small></div>";
    h+=pins.length?"<div class='tr-pins'>"+pins.map(function(p,i){return "<div class='tr-pn' style='--r:"+(i%2?1.2:-1.5)+"deg'><small>"+esc(p.k)+"</small>"+esc(p.t)+"</div>";}).join("")+"</div>"
      :"<p class='tr-empty'>กด “ปักไว้ใน post-it” ที่หัวข้อสอบ แล้วจะขึ้นที่นี่</p>";
    h+="</section><section class='tr-dk'><div class='tr-dk-h'><h3>คีย์ลัด</h3></div><ul class='tr-keys'>"+
      [["ค้นหาข้อสอบ","Ctrl K"],["ตอบข้อที่เห็นบนจอ","1–5"],["คาบก่อน-ถัดไป","Alt ← →"],["หมุนเลือกคาบ","ดับเบิลคลิก"],["ทางลัด","+"],["ย่อ/ขยายเนื้อหา","− ="],["ซ่อนแถบซ้าย / ขวา","[ ]"]]
        .map(function(x){return "<li><span>"+x[0]+"</span><span class='tr-kbd'>"+x[1]+"</span></li>";}).join("")+"</ul></section>";
    dock.innerHTML=h;}
  /* จำข้อที่กดปักไป Post-it (เฉพาะเครื่องนี้ ไว้โชว์ในแถบขวา) */
  document.addEventListener("click",function(e){
    var a=e.target.closest&&e.target.closest("a[href*='BRsYSzd35']");if(!a)return;var art=a.closest("article");if(!art)return;
    var id=String(art.id||"").replace(/^it-/,"").replace(/--.*$/,""),t=art.querySelector(".topic,.q,.stem");
    var arr=ls(PINKEY)||[];arr.push({k:id,t:String(t?t.textContent:id).slice(0,80),at:Date.now()});ls(PINKEY,arr.slice(-30));setTimeout(renderDock,50);
  },true);
  /* ถาม AI ติดข้างจอเมื่อเปิด (จอ ≥1400) */
  (function(){var tries=0,iv=setInterval(function(){
    var pn=document.querySelector(".aiw-panel");if(!pn){if(++tries>40)clearInterval(iv);return;}clearInterval(iv);
    function sync(){de.classList.toggle("tr-ai",WIDE.matches&&!pn.hidden);}
    new MutationObserver(sync).observe(pn,{attributes:true,attributeFilter:["hidden"]});sync();
    if(WIDE.addEventListener)WIDE.addEventListener("change",sync);},250);})();

  /* ---------- วงล้อทางลัด ---------- */
  var A=[["new","ข้อใหม่","ข้อสอบใหม่ของระบบนี้"],["old","คลังเก่า","ข้อสอบเก่า MED28–35"],["year","ตามปี","MEQ/OSCE แยกตามปี"],["hot","ออกบ่อย","ข้อที่ออกซ้ำหลายรุ่น"],
    ["yearall","แยกปี","ทำทีละปี รวมทุกระบบ"],["pic","มีรูป","ข้อสอบที่เป็นรูป"],["wrong","ข้อที่ผิด","สุ่มจากข้อที่เคยผิด"],["swap","สลับคาบ","หมุนเลือกคาบ"],
    ["search","ค้นหา","หาข้อจากทุกระบบ"],["ai","ถาม AI","ถามเรื่องที่อ่านอยู่"],["pin","Post-it","กระดาน Post-it ห้ามลืม"],["theme","โหมดสี","สลับสว่าง/มืด/ตามเครื่อง"]];
  var N=A.length,RO=160,RI=78,GAP=1.6,PUSH=8,M=null;
  function pt(r,a){var t=a*Math.PI/180;return [r*Math.cos(t),r*Math.sin(t)];}
  function sector(a0,a1){var p1=pt(RO,a0),p2=pt(RO,a1),p3=pt(RI,a1),p4=pt(RI,a0),f=function(v){return v.toFixed(2);};
    return "M"+f(p1[0])+" "+f(p1[1])+"A"+RO+" "+RO+" 0 0 1 "+f(p2[0])+" "+f(p2[1])+"L"+f(p3[0])+" "+f(p3[1])+"A"+RI+" "+RI+" 0 0 0 "+f(p4[0])+" "+f(p4[1])+"Z";}
  function act(k){
    if(["new","old","year","hot","yearall","pic"].indexOf(k)>=0)return setMode(k);
    if(k==="wrong")return wrongQuiz();
    if(k==="swap")return openWheel();
    if(k==="search")return openPal();
    if(k==="ai")return aiOpen();
    if(k==="pin"){window.open(POSTIT,"_blank","noopener");return;}
    if(k==="theme")return thCycle();}
  function openMenu(drag){
    if(M)return;if(sh.open)closeSheet();
    var ov=el("div","tr-rm");ov.setAttribute("role","menu");ov.setAttribute("aria-label","ทางลัด");
    var ring=el("div","tr-rm-ring");ov.appendChild(ring);
    var NS="http://www.w3.org/2000/svg",svg=document.createElementNS(NS,"svg");svg.setAttribute("class","tr-rm-svg");svg.setAttribute("viewBox","-170 -170 340 340");svg.setAttribute("aria-hidden","true");ring.appendChild(svg);
    var segs=[],its=[],wc=wrongIn().length;
    A.forEach(function(x,i){
      var a=-90+i*360/N,hh=180/N,pv=pt(PUSH,a);
      var g=document.createElementNS(NS,"g");g.setAttribute("class","tr-rm-seg");
      g.style.setProperty("--tx",pv[0].toFixed(1)+"px");g.style.setProperty("--ty",pv[1].toFixed(1)+"px");g.style.setProperty("--d",(i*24)+"ms");
      var pa=document.createElementNS(NS,"path");pa.setAttribute("d",sector(a-hh+GAP,a+hh-GAP));g.appendChild(pa);
      var gl=document.createElementNS(NS,"path");gl.setAttribute("class","tr-rm-glow");var o0=pt(RO+7,a-hh+GAP+2),o1=pt(RO+7,a+hh-GAP-2);
      gl.setAttribute("d","M"+o0[0].toFixed(2)+" "+o0[1].toFixed(2)+"A"+(RO+7)+" "+(RO+7)+" 0 0 1 "+o1[0].toFixed(2)+" "+o1[1].toFixed(2));g.appendChild(gl);
      svg.appendChild(g);segs.push(g);
      var c=pt((RO+RI)/2,a),it=el("button","tr-rm-it");it.type="button";it.setAttribute("role","menuitem");it.tabIndex=-1;
      it.style.setProperty("--x",c[0].toFixed(1)+"px");it.style.setProperty("--y",c[1].toFixed(1)+"px");it.style.setProperty("--tx",pv[0].toFixed(1)+"px");it.style.setProperty("--ty",pv[1].toFixed(1)+"px");it.style.setProperty("--d",(i*24)+"ms");
      it.innerHTML=I[x[0]];it.appendChild(el("span",null,x[1]));it.setAttribute("aria-label",x[1]+" "+x[2]);
      if(x[0]==="wrong"&&wc)it.appendChild(el("span","n",String(wc)));
      if(["old","year","hot","pic","yearall"].indexOf(x[0])>=0&&!modeCount(x[0]))it.classList.add("off");
      it.addEventListener("click",function(e){e.stopPropagation();pick(i);});
      ring.appendChild(it);its.push(it);});
    var hc=document.createElementNS(NS,"circle");hc.setAttribute("class","tr-rm-hubc");hc.setAttribute("r",RI-8);svg.appendChild(hc);
    var hub=el("div","tr-rm-hub");hub.appendChild(el("span","tg",esc(setLbl(state.set))));var hb=el("b",null,"ทางลัด"),hs=el("small",null,drag?"ลากไปที่ช่องแล้วปล่อย":"แตะช่องที่ต้องการ");hub.appendChild(hb);hub.appendChild(hs);ring.appendChild(hub);
    var tip=el("div","tr-rm-tip","แตะนอกวงหรือกด Esc เพื่อปิด");ov.appendChild(tip);
    document.body.appendChild(ov);mb.classList.add("on");mb.setAttribute("aria-expanded","true");
    var cx=0,cy=0,hl=-1,closing=false;
    function place(){
      if(DESK.matches){var lw=PN.s?72:264,rw=WIDE.matches&&!PN.d?376:0;cx=lw+(window.innerWidth-lw-rw)/2;cy=window.innerHeight/2;}
      else{var nbt=nav.getBoundingClientRect().top;cx=window.innerWidth/2;cy=Math.max(190,Math.min(nbt-RO-36,nbt/2+10));}
      ring.style.left=cx+"px";ring.style.top=cy+"px";tip.style.top=(cy+RO+18)+"px";}
    function setHl(i){if(i===hl)return;if(hl>=0){segs[hl].classList.remove("hl");segs[hl].querySelector(".tr-rm-glow").classList.remove("on");its[hl].classList.remove("hl");}hl=i;
      if(i>=0){segs[i].classList.add("hl");segs[i].querySelector(".tr-rm-glow").classList.add("on");its[i].classList.add("hl");hb.textContent=A[i][1];hs.textContent=A[i][2];if(navigator.vibrate&&drag)try{navigator.vibrate(4);}catch(e){}}
      else{hb.textContent="ทางลัด";hs.textContent=drag?"ลากไปที่ช่องแล้วปล่อย":"แตะช่องที่ต้องการ";}}
    function at(x,y){var dx=x-cx,dy=y-cy,d=Math.sqrt(dx*dx+dy*dy);if(d<RI*.7||d>RO+40)return{i:-1};var a=Math.atan2(dy,dx)*180/Math.PI+90;return{i:Math.round(((a%360)+360)%360/(360/N))%N};}
    function pick(i){if(closing||i<0)return;setHl(i);var s=segs[i];s.classList.remove("pick");void s.getBoundingClientRect();s.classList.add("pick");var k=A[i][0];setTimeout(function(){close(function(){act(k);});},RM?0:180);}
    function close(after){if(closing)return;closing=true;ov.classList.remove("on");ov.classList.add("out");mb.classList.remove("on");mb.setAttribute("aria-expanded","false");
      document.removeEventListener("keydown",key,true);window.removeEventListener("resize",place);window.removeEventListener("pointermove",mv,true);window.removeEventListener("pointerup",up,true);window.removeEventListener("pointercancel",up,true);
      setTimeout(function(){if(ov.parentNode)ov.remove();M=null;if(after)after();},RM?0:170);}
    function key(e){if(e.key==="Escape"){e.preventDefault();close();}
      else if(e.key==="ArrowRight"||e.key==="ArrowDown"){e.preventDefault();setHl((hl+1+N)%N);its[hl].focus({preventScroll:true});}
      else if(e.key==="ArrowLeft"||e.key==="ArrowUp"){e.preventDefault();setHl(hl<0?N-1:(hl-1+N)%N);its[hl].focus({preventScroll:true});}
      else if((e.key==="Enter"||e.key===" ")&&hl>=0){e.preventDefault();pick(hl);}}
    var dragging=!!drag,moved=false,sx=drag?drag.x:0,sy=drag?drag.y:0;
    function mv(e){var r=at(e.clientX,e.clientY);if(dragging&&(Math.abs(e.clientX-sx)>10||Math.abs(e.clientY-sy)>10))moved=true;if(e.pointerType==="mouse"||dragging)setHl(r.i);}
    function up(e){if(!dragging)return;dragging=false;if(moved){var r=at(e.clientX,e.clientY);if(r.i>=0)pick(r.i);else setHl(-1);}}
    window.addEventListener("pointermove",mv,true);window.addEventListener("pointerup",up,true);window.addEventListener("pointercancel",up,true);
    ov.addEventListener("click",function(e){if(e.target.closest&&e.target.closest(".tr-rm-it"))return;var r=at(e.clientX,e.clientY);if(r.i>=0)pick(r.i);else close();});
    document.addEventListener("keydown",key,true);window.addEventListener("resize",place);
    place();requestAnimationFrame(function(){if(!closing)ov.classList.add("on");});
    if(!drag)setTimeout(function(){if(!closing)try{its[0].focus({preventScroll:true});setHl(0);}catch(_){}},RM?0:120);
    M={close:close};}
  var lastPD=0;
  mb.addEventListener("pointerdown",function(e){if(e.button>0)return;lastPD=Date.now();e.preventDefault();if(M){M.close();return;}openMenu({x:e.clientX,y:e.clientY});});
  mb.addEventListener("click",function(){if(Date.now()-lastPD>800){if(M)M.close();else openMenu(null);}});

  /* ---------- วงล้อสลับคาบ (ดับเบิลคลิก / กดค้าง 2 วิ) ---------- */
  var W=null;
  function openWheel(){
    if(W)return;var L=lecsOf(state.set);if(!L.length)return;
    if(sh.open)closeSheet();
    var curI=0;L.forEach(function(l,i){if(l.lec===state.lec)curI=i;});
    var ov=el("div","tr-wheel");ov.setAttribute("role","dialog");ov.setAttribute("aria-modal","true");ov.setAttribute("aria-label","สลับคาบ");
    var head=el("div","tr-wh-head");head.appendChild(el("b",null,"สลับคาบ · "+esc(setLbl(state.set))));head.appendChild(el("span",null,L.length+" คาบในระบบนี้"));ov.appendChild(head);
    var cl=el("button","tr-wh-close","✕");cl.type="button";cl.setAttribute("aria-label","ปิด");ov.appendChild(cl);
    var stage=el("div","tr-wh-stage");ov.appendChild(stage);
    var NS="http://www.w3.org/2000/svg",svg=document.createElementNS(NS,"svg");svg.setAttribute("class","tr-wh-arc");var circ=document.createElementNS(NS,"circle");svg.appendChild(circ);stage.appendChild(svg);
    var knob=el("div","tr-wh-knob");stage.appendChild(knob);
    ov.appendChild(el("div","tr-wh-foot","ลากขึ้นลงหรือหมุนลูกกลิ้งเพื่อเลื่อน แตะคาบเพื่อเปิด"));
    var nodes=L.map(function(l,i){
      var n=el("div","tr-wh-it");if(state.lec===l.lec)n.classList.add("cur");
      var inr=el("div","tr-wh-in");inr.style.setProperty("--d",(Math.min(6,Math.abs(i-curI))*40)+"ms");
      var lb=el("div","tr-wh-lbl");lb.appendChild(el("b",null,esc(shortName(l.name)||("Lec "+l.lec))));lb.appendChild(el("small",null,"ทำแล้ว "+l.d+"/"+l.t+" ข้อ"+(LEC[l.lec]&&LEC[l.lec].d?" · "+esc(LEC[l.lec].d):"")));
      var c=el("button","tr-wh-chip",esc(l.lec));c.type="button";c.setAttribute("aria-label","Lec "+l.lec+" "+shortName(l.name));
      var full=l.t&&l.d>=l.t;c.appendChild(el("span","dd"+(full?" ok":""),full?"✓":l.d+"/"+l.t));
      inr.appendChild(lb);inr.appendChild(c);n.appendChild(inr);stage.appendChild(n);return n;});
    document.body.appendChild(ov);document.body.classList.add("tr-lock");
    var wt=null,p=curI,anim=null,R=0,x0=0,cy=0,STEP=92,shown=-1,busy=false,closing=false;
    function geo(){var sw=stage.clientWidth,shh=stage.clientHeight;R=Math.max(shh*.78,440);x0=sw-148;cy=shh/2;var ax=x0+96,cx=ax+R;
      circ.setAttribute("cx",cx);circ.setAttribute("cy",cy);circ.setAttribute("r",R);circ.style.setProperty("--len",Math.ceil(2*Math.PI*R));knob.style.left=ax+"px";knob.style.top=cy+"px";}
    function paint(){
      for(var i=0;i<nodes.length;i++){var k=i-p,a=k*STEP/R,n=nodes[i],ak=Math.abs(k);
        if(ak>6){n.style.visibility="hidden";continue;}n.style.visibility="";
        var x=x0+R*(1-Math.cos(a))+36,y=cy+R*Math.sin(a),sc=Math.max(.72,1-ak*.07);
        n.style.transform="translate("+x+"px,"+y+"px) translate(-100%,-50%) rotate("+(-a)+"rad) scale("+sc+")";
        n.style.opacity=Math.max(0,1-ak*.2);n.style.zIndex=String(100-Math.round(ak*10));}
      var c=Math.round(p);if(c!==shown){if(shown>=0&&nodes[shown])nodes[shown].classList.remove("on");shown=c;if(nodes[c])nodes[c].classList.add("on");if(anim&&navigator.vibrate)try{navigator.vibrate(4);}catch(e){}}}
    function clamp(v){return Math.max(0,Math.min(L.length-1,v));}
    function goTo(t,done){t=clamp(t);cancelAnimationFrame(anim);
      if(RM){p=t;paint();anim=null;if(done)done();return;}
      var from=p,t0=performance.now(),dur=Math.min(520,220+Math.abs(t-from)*70);
      (function f(now){if(closing&&!done)return;var u=Math.min(1,(now-t0)/dur),e=1-Math.pow(1-u,3);p=from+(t-from)*e;paint();
        if(u<1)anim=requestAnimationFrame(f);else{anim=null;if(done)done();}})(t0);}
    function choose(i){if(busy)return;busy=true;goTo(i,function(){nodes[i].classList.add("pick");setTimeout(function(){close(function(){goLec(state.set,L[i].lec);});},RM?0:260);});}
    function close(after){if(closing)return;closing=true;busy=true;cancelAnimationFrame(anim);clearTimeout(wt);ov.classList.remove("on");ov.classList.add("out");
      document.removeEventListener("keydown",key,true);window.removeEventListener("resize",rs);
      setTimeout(function(){if(ov.parentNode)ov.remove();W=null;document.body.classList.remove("tr-lock");if(after)after();},RM?0:200);}
    function key(e){if(closing)return;if(e.key==="Escape"){e.preventDefault();close();}
      else if(e.key==="ArrowDown"||e.key==="ArrowRight"){e.preventDefault();goTo(Math.round(p)+1);}
      else if(e.key==="ArrowUp"||e.key==="ArrowLeft"){e.preventDefault();goTo(Math.round(p)-1);}
      else if(e.key==="Enter"||e.key===" "){if(document.activeElement===cl)return;e.preventDefault();choose(Math.round(p));}}
    function rs(){if(!closing){geo();paint();}}
    var drag=null;
    ov.addEventListener("pointerdown",function(e){if(e.target===cl)return;cancelAnimationFrame(anim);anim=null;drag={tg:e.target,y:e.clientY,p:p,v:0,moved:0,id:e.pointerId,ly:e.clientY,lt:performance.now()};try{ov.setPointerCapture(e.pointerId);}catch(_){}});
    ov.addEventListener("pointermove",function(e){if(!drag||e.pointerId!==drag.id)return;var dy=e.clientY-drag.y;drag.moved=Math.max(drag.moved,Math.abs(dy));
      var now=performance.now(),dt=Math.max(1,now-drag.lt);drag.v=.8*((drag.ly-e.clientY)/STEP/dt)+.2*drag.v;drag.ly=e.clientY;drag.lt=now;
      var np=drag.p-dy/STEP;if(np<0)np=np*.35;else if(np>L.length-1)np=L.length-1+(np-L.length+1)*.35;p=np;paint();});
    function up(e){if(!drag||e.pointerId!==drag.id)return;var d=drag;drag=null;
      if(d.moved<8){var tg=d.tg||e.target,c=tg.closest&&tg.closest(".tr-wh-chip,.tr-wh-lbl");
        if(c){var i=nodes.indexOf(c.closest(".tr-wh-it"));if(i>=0){choose(i);return;}}
        if(!(tg.closest&&tg.closest(".tr-wh-it"))&&e.clientX<stage.getBoundingClientRect().left+40){close();return;}
        goTo(Math.round(p));return;}
      goTo(Math.round(p+d.v*220));}
    ov.addEventListener("pointerup",up);ov.addEventListener("pointercancel",up);
    ov.addEventListener("wheel",function(e){e.preventDefault();cancelAnimationFrame(anim);anim=null;p=clamp(p+e.deltaY/(e.deltaMode===1?3:120));paint();clearTimeout(wt);wt=setTimeout(function(){goTo(Math.round(p));},120);},{passive:false});
    cl.addEventListener("click",function(){close();});
    ov.addEventListener("click",function(e){e.stopPropagation();});
    document.addEventListener("keydown",key,true);window.addEventListener("resize",rs);
    geo();paint();
    requestAnimationFrame(function(){if(closing)return;ov.classList.add("on");var c=nodes[curI]&&nodes[curI].querySelector(".tr-wh-chip");if(c)try{c.focus({preventScroll:true});}catch(_){}});
    W={close:close};}
  /* ไม่เริ่มบนข้อสอบ/เฉลย/ตาราง/ภาพ เพื่อไม่แย่งการเลือกข้อความไปถาม AI */
  var SKIP="input,textarea,select,[contenteditable],dialog,button,a,label,summary,.item,.oldgrp,.panel,.vign,table,.tablewrap,.qfig,.aiw-panel,.aiw-sel,.tr-wheel,.tr-rm,.tr-bnav,.tr-side,.tr-dock,.tr-pal,.strip,.rail,.tr-card,.tr-hero";
  var lastPT="mouse";
  document.addEventListener("pointerdown",function(e){lastPT=e.pointerType||"mouse";},true);
  document.addEventListener("dblclick",function(e){
    if(lastPT!=="mouse")return;var t=e.target;if(!t||!t.closest||t.closest(SKIP))return;
    try{var sl=window.getSelection();if(sl)sl.removeAllRanges();}catch(_){}
    openWheel();});
  var hold=null,lring=null;
  function endHold(){if(!hold)return;clearTimeout(hold.t);clearTimeout(hold.rt);hold=null;document.body.classList.remove("tr-arm");if(lring){var r=lring;lring=null;r.classList.remove("go");setTimeout(function(){r.remove();},200);}}
  document.addEventListener("touchstart",function(e){
    endHold();if(W||M||sh.open||PAL||e.touches.length!==1)return;var t=e.target;if(!t||!t.closest||t.closest(SKIP))return;
    var tc=e.touches[0];hold={x:tc.clientX,y:tc.clientY};document.body.classList.add("tr-arm");
    hold.rt=setTimeout(function(){if(!hold)return;lring=el("div","tr-lp",'<svg viewBox="0 0 72 72" aria-hidden="true"><circle cx="36" cy="36" r="32"/></svg>');lring.style.left=hold.x+"px";lring.style.top=hold.y+"px";de.appendChild(lring);requestAnimationFrame(function(){if(lring)lring.classList.add("go");});},250);
    hold.t=setTimeout(function(){if(!hold)return;endHold();if(navigator.vibrate)try{navigator.vibrate(12);}catch(_){}
      var until=Date.now()+900;document.addEventListener("click",function sup(ev){document.removeEventListener("click",sup,true);if(Date.now()<until){ev.preventDefault();ev.stopPropagation();}},true);openWheel();},2000);
  },{passive:true});
  document.addEventListener("touchmove",function(e){if(!hold)return;var tc=e.touches[0];if(!tc||Math.abs(tc.clientX-hold.x)>10||Math.abs(tc.clientY-hold.y)>10)endHold();},{passive:true});
  document.addEventListener("touchend",endHold,{passive:true});
  document.addEventListener("touchcancel",endHold,{passive:true});
  document.addEventListener("contextmenu",function(e){if(hold||W)e.preventDefault();});
  document.addEventListener("scroll",function(){if(hold)endHold();},{passive:true,capture:true});

  /* ---------- ปัดซ้าย-ขวา ---------- */
  function blocked(t){
    if(!t||!t.closest)return true;
    if(t.closest("input,textarea,select,dialog,.tr-rm,.tr-wheel,.tr-bnav,.aiw-panel,.qfig,.tr-pal"))return true;
    for(var n=t;n&&n!==document.body;n=n.parentElement){var cs=getComputedStyle(n);if((cs.overflowX==="auto"||cs.overflowX==="scroll")&&n.scrollWidth>n.clientWidth+2)return true;}
    return false;}
  var sx=0,sy=0,stt=0,okT=false;
  document.addEventListener("touchstart",function(e){if(e.touches.length!==1){okT=false;return;}var t=e.touches[0];sx=t.clientX;sy=t.clientY;stt=Date.now();
    okT=!blocked(e.target)&&!sh.open&&!W&&!M&&!PAL&&!(window.getSelection&&String(window.getSelection()).length);},{passive:true});
  document.addEventListener("touchend",function(e){if(!okT)return;okT=false;var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;
    if(Date.now()-stt>800||Math.abs(dx)<70||Math.abs(dy)>Math.abs(dx)*.5)return;shift(dx<0?1:-1);},{passive:true});

  /* ---------- ค้นหาข้อสอบทุกระบบ (Ctrl K) ---------- */
  var PAL=null,SIDX=null;
  function searchIdx(){if(SIDX)return SIDX;SIDX=[];var X=idx();
    SETS.forEach(function(s){lecsOf(s.k).forEach(function(l){SIDX.push({lec:l.lec,set:s.k,t:"Lec "+l.lec+" "+shortName(l.name),sub:s.label+" · "+(l.n?"ข้อใหม่ "+l.n:"")+(l.n&&l.o?" · ":"")+(l.o?"ข้อเก่า "+l.o:""),k:"คาบ",s:(l.lec+" "+l.name).toLowerCase()});});});
    Object.keys(X).forEach(function(id){var e=X[id],it=e.it,t=it.topic||it.q||id;
      SIDX.push({id:id,set:e.set,t:t,sub:id+" · Lec "+e.lec+" "+shortName(e.lecture||""),k:e.kind==="old"?"ข้อเก่า":e.kind==="meq"?(it.part||"MEQ"):"MCQ",
        s:(id+" "+t+" "+(e.lecture||"")+" "+String(it.stem||it.vignette||"").slice(0,400)).toLowerCase()});});
    return SIDX;}
  function openPal(){
    if(PAL)return;if(sh.open)closeSheet();
    var ov=el("div","tr-pal"),box=el("div","tr-pal-box");ov.appendChild(box);ov.setAttribute("role","dialog");ov.setAttribute("aria-modal","true");ov.setAttribute("aria-label","ค้นหาข้อสอบ");
    var iw=el("div","tr-pal-in",I.search);var inp=el("input");inp.type="search";inp.placeholder="ค้นหา เช่น tamponade, AKI, C-MCQ-12";inp.setAttribute("aria-label","ค้นหา");iw.appendChild(inp);box.appendChild(iw);
    var ul=el("ul","tr-pal-list");ul.setAttribute("role","listbox");box.appendChild(ul);
    box.appendChild(el("div","tr-pal-foot","<span><span class='tr-kbd'>↑ ↓</span> เลือก</span><span><span class='tr-kbd'>Enter</span> เปิด</span><span><span class='tr-kbd'>Esc</span> ปิด</span><span>ค้นจาก "+SETS.length+" ระบบ</span>"));
    document.body.appendChild(ov);var sel=0,res=[];
    function hl(t,q){if(!q)return esc(t);var i=t.toLowerCase().indexOf(q.toLowerCase());return i<0?esc(t):esc(t.slice(0,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length));}
    function draw(){var q=inp.value.trim().toLowerCase(),X=searchIdx();
      res=q?X.filter(function(x){return x.s.indexOf(q)>=0||(x.sub+" "+setLbl(x.set)).toLowerCase().indexOf(q)>=0;}).slice(0,14):X.filter(function(x){return x.lec&&x.set===state.set;});
      sel=Math.min(sel,Math.max(0,res.length-1));ul.innerHTML="";
      if(!res.length){ul.appendChild(el("li","tr-pal-empty","ไม่พบ ลองคำอื่น หรือพิมพ์รหัสข้อ"));return;}
      res.forEach(function(x,i){var li=el("li"),b=el("button",i===sel?"on":"","<span class='pc'>"+esc(setLbl(x.set))+" · "+esc(x.k)+"</span><span class='pt'>"+hl(x.t,inp.value.trim())+"<small>"+esc(x.sub)+"</small></span>");b.type="button";b.setAttribute("role","option");
        b.addEventListener("mousemove",function(){if(sel!==i){sel=i;draw();}});b.addEventListener("click",function(){choose(i);});li.appendChild(b);ul.appendChild(li);});}
    function choose(i){var x=res[i];if(!x)return;close();if(x.id)jump(x.id);else goLec(x.set,x.lec);}
    function close(){if(!PAL)return;PAL=null;ov.remove();}
    inp.addEventListener("input",function(){sel=0;draw();});
    inp.addEventListener("keydown",function(e){if(e.key==="ArrowDown"){e.preventDefault();sel=Math.min(res.length-1,sel+1);draw();}else if(e.key==="ArrowUp"){e.preventDefault();sel=Math.max(0,sel-1);draw();}else if(e.key==="Enter"){e.preventDefault();choose(sel);}else if(e.key==="Escape"){e.preventDefault();close();}});
    ov.addEventListener("mousedown",function(e){if(e.target===ov)close();});
    PAL={close:close};draw();inp.focus();}

  /* ---------- คีย์บอร์ด ---------- */
  document.addEventListener("keydown",function(e){
    if((e.ctrlKey||e.metaKey)&&(e.key==="k"||e.key==="K")&&!PAL){e.preventDefault();openPal();return;}
    var tg=e.target&&e.target.tagName;if(tg==="INPUT"||tg==="TEXTAREA"||tg==="SELECT"||(e.target&&e.target.isContentEditable))return;
    if(PAL||W||M||sh.open)return;
    if(e.key==="/"&&DESK.matches){e.preventDefault();openPal();return;}
    if(e.altKey&&(e.key==="ArrowLeft"||e.key==="ArrowRight")){e.preventDefault();shift(e.key==="ArrowLeft"?-1:1);return;}
    if(e.key==="+"&&!e.ctrlKey&&!e.metaKey){e.preventDefault();openMenu(null);return;}
    if((e.key==="["||e.key==="]")&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&DESK.matches){if(e.key==="]"&&!WIDE.matches)return;e.preventDefault();paneToggle(e.key==="["?"s":"d");return;}
    if((e.key==="-"||e.key==="=")&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&V.view!=="home"){e.preventDefault();fzStep(e.key==="-"?-1:1);return;}
  });

  /* ---------- คลิกในชั้นนี้ ---------- */
  document.addEventListener("click",function(e){
    var b=e.target.closest&&e.target.closest("button");if(!b||!b.dataset)return;var d=b.dataset;
    if(d.trnext){pop(b);openNext();return;}
    if(d.trset){pop(b);openSetSheet(d.trset);return;}
    if(d.trpage){goPage(d.trpage);return;}
    if(d.trside){setSet(d.trside);return;}
    if(d.trwrong){wrongQuiz();return;}
    if(d.trjump){jump(d.trjump);return;}
    if(d.trplus){openMenu(null);return;}
    if(d.trpal){openPal();return;}
    if(d.trfilt){openFilter();return;}
    if(d.trai){aiOpen();return;}
    if(d.trpin){window.open(POSTIT,"_blank","noopener");return;}
    if(d.trtheme){thCycle();return;}
    if(d.trfz!=null){fzStep(+d.trfz);return;}
    if(d.trpane){paneToggle(d.trpane);return;}
  });

  /* ---------- สถานะบันทึกบัญชี (สำเนาจาก #lsync) ---------- */
  function syncMirror(){var s=document.getElementById("lsync");if(!s)return;var t=s.textContent.trim(),c=s.className;
    [].forEach.call(document.querySelectorAll(".tr-syncm"),function(m){m.className="tr-syncm"+(/cloud/.test(c)?" cloud":"")+(/busy/.test(c)?" busy":"");m.title=s.title||"";var sp=m.querySelector("span");if(sp)sp.textContent=t;});}

  /* ---------- หลัง render ทุกครั้ง ---------- */
  var lastView="";
  function paint(){
    var A=allStat();
    if(DESK.matches)renderSide(A);else side.innerHTML="";
    renderDock();syncMirror();fzApply();paneApply();}
  function after(){
    de.removeAttribute("data-set");              /* สีเน้น lime ทั้งเว็บ (เลิกสีประจำระบบ) */
    document.body.dataset.view=V.view;keepUI();
    flushPend();
    var pg=pageOf();Object.keys(nb).forEach(function(k){if(k===pg)nb[k].setAttribute("aria-current","page");else nb[k].removeAttribute("aria-current");});
    if(V.view==="home"){viewHome();}
    else{var st=document.getElementById("stream");
      if(st&&!st.querySelector(":scope>.tr-tools")){var tb=el("div","tr-tools"),fb=el("button","tr-filt press",I.filter+"<span></span>");fb.type="button";fb.dataset.trfilt="1";
        fb.querySelector("span").textContent=filtSummary();fb.setAttribute("aria-label","ตัวกรอง: "+filtSummary());tb.appendChild(fb);tb.appendChild(fzBar());st.insertBefore(tb,st.firstChild);}
      if(V.dir&&!RM&&st){var c=st.children[1];if(c)c.classList.add(V.dir>0?"tr-slide-l":"tr-slide-r");}
      if(home.innerHTML)home.innerHTML="";}
    if(lastView!==V.view){lastView=V.view;}
    V.dir=0;paint();}
  /* ข้อมูลที่ใช้ในหน้าแรกเปลี่ยนตามบัญชี → render ใหม่ทั้งชุด */
  /* ลิงก์ตรงจาก Lecture Dashboard (#cardio-13, #review~…) → เปิดหน้าข้อสอบเสมอ */
  window.addEventListener("hashchange",function(){if(String(location.hash||"").length>1&&V.view!=="drill"){V.view="drill";keepUI();render();window.scrollTo(0,0);}});
  if(DESK.addEventListener){DESK.addEventListener("change",paint);WIDE.addEventListener("change",paint);NARROW.addEventListener("change",function(){if(!NARROW.matches&&railHome)closeSheet();});}
  return {after:after,syncMirror:syncMirror,toast:toast,openWheel:openWheel,openMenu:openMenu,openPal:openPal,openSetSheet:openSetSheet,view:function(){return V.view;}};
})();
var renderBase=render;
render=function(){renderBase();try{TR.after();}catch(e){if(window.console)console.error(e);}};
var renderSyncBase=renderSync;
renderSync=function(){renderSyncBase();try{TR.syncMirror();}catch(e){}};
