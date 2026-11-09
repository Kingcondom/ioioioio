
/* ===================== โครงหน้าแบบ Teaching Round (ผู้ใช้ขอ 9 พ.ย.) =====================
   ทุกฟังก์ชันเดิมยังอยู่ — ชั้นนี้แค่จัดที่ใหม่: แถบล่าง/แถบซ้าย · หน้าแรกการ์ดเขียว · หน้าต่างคาบ · วงล้อทางลัด
   วงล้อสลับคาบ · ปัดซ้าย-ขวา · ค้นหา Ctrl K · แถบขวา · ข้อสอบหลังอ่านจบ · ประวัติการทวนรายวัน (state.log ซิงก์บัญชี) */
var TR=(function(){
  var RM=false;try{RM=matchMedia("(prefers-reduced-motion: reduce)").matches}catch(e){}
  var DESK=matchMedia("(min-width:1100px)"),WIDE=matchMedia("(min-width:1400px)");
  var GOAL=5,EXAM="2026-11-17",PINKEY="med421-learn-pins",PROGKEY="med421-learn-prog";
  var GATE={},pendingLog=null;
  function el(t,c,h){var x=document.createElement(t);if(c)x.className=c;if(h!=null)x.innerHTML=h;return x}
  function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||"null");localStorage.setItem(k,JSON.stringify(v))}catch(e){return null}}
  function pad(n){return (n<10?"0":"")+n}
  function dkey(d){d=d||new Date();return d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate())}
  var WD=["อา.","จ.","อ.","พ.","พฤ.","ศ.","ส."],MO=["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."];
  function thaiDate(d){return WD[d.getDay()]+" "+d.getDate()+" "+MO[d.getMonth()]}
  var toastEl=el("div","tr-toast");toastEl.setAttribute("role","status");toastEl.setAttribute("aria-live","polite");document.documentElement.appendChild(toastEl);var toastT=null;
  function toast(m){toastEl.textContent=m;toastEl.classList.add("on");clearTimeout(toastT);toastT=setTimeout(function(){toastEl.classList.remove("on")},1300)}
  function pop(n){if(RM||!n)return;n.classList.remove("tr-pop");void n.offsetWidth;n.classList.add("tr-pop")}
  function loaded(){return COURSES.length&&course()&&course()._loaded}

  /* ---------- ประวัติการทวนรายวัน ---------- */
  function logToday(id){
    if(!id)return;state.log=state.log||{};var k=dkey(),a=state.log[k]||[];
    if(a.indexOf(id)<0){a.push(id);state.log[k]=a.slice(-200);save()}
  }
  function todayCount(){var a=(state.log||{})[dkey()];return a?a.length:0}
  function dayCount(d){var a=(state.log||{})[dkey(d)];return a?a.length:0}
  function streak(){var n=0,d=new Date();if(!dayCount(d))d.setDate(d.getDate()-1);while(dayCount(d)){n++;d.setDate(d.getDate()-1)}return n}
  document.addEventListener("click",function(e){
    var t=e.target.closest&&e.target.closest("button");if(!t)return;
    if(state.view==="section"&&((t.dataset.q&&t.closest("#main"))||t.dataset.act==="markread"))pendingLog=state.sec;
  },true);

  /* ---------- ตัวนับ ---------- */
  function wrongList(){var w=[];if(!loaded())return w;
    allSections().forEach(function(x){var n=0;x.sec.items.forEach(function(it){var v=state.ans[it.id];if(v!=null&&v!==it.answer)n++});if(n)w.push({l:x.lec,s:x.sec,n:n})});return w}
  function wrongCount(){return wrongList().reduce(function(a,x){return a+x.n},0)}
  function nlCount(){var set={};if(!loaded())return 0;lectures().forEach(function(l){lecNL(l).forEach(function(c){if(NL[c])set[c]=1})});return Object.keys(set).length}
  function examDays(){var t=new Date(EXAM+"T00:00:00"),n=new Date();n.setHours(0,0,0,0);return Math.round((t-n)/864e5)}
  function progCache(){if(!loaded())return;var o=ls(PROGKEY)||{},p=courseProgress();o[state.course]=p.total?p.done/p.total:0;ls(PROGKEY,o)}

  /* ---------- ไอคอน ---------- */
  var S='<svg viewBox="0 0 24 24" aria-hidden="true">';
  var I={
    home:S+'<path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5H15v-6H9v6H5.5A1.5 1.5 0 0 1 4 19z"/></svg>',
    lec:S+'<path d="M4.5 5.5A1.5 1.5 0 0 1 6 4h4.5A1.5 1.5 0 0 1 12 5.5v14a1.5 1.5 0 0 0-1.5-1.5h-6zM19.5 5.5A1.5 1.5 0 0 0 18 4h-4.5A1.5 1.5 0 0 0 12 5.5v14a1.5 1.5 0 0 1 1.5-1.5h6z"/></svg>',
    plus:S+'<path d="M12 5v14M5 12h14"/></svg>',
    write:S+'<path d="M5 19.5h4l10-10a2.1 2.1 0 0 0-3-3l-10 10z"/><path d="M14 8.5l3 3"/></svg>',
    review:S+'<path d="M4.5 12a7.5 7.5 0 1 0 2.2-5.3M4.5 4.5v3.7h3.7"/><path d="M12 8.5V12l2.5 2"/></svg>',
    next:S+'<path d="M5 12h12M13 7l5 5-5 5"/></svg>',
    pres:S+'<rect x="3.5" y="4.5" width="17" height="11" rx="1.5"/><path d="M12 15.5v4M8.5 19.5h7M10.5 8l3.5 2-3.5 2z"/></svg>',
    ai:S+'<path d="M12 3.5l1.9 4.8 4.8 1.9-4.8 1.9L12 16.9l-1.9-4.8-4.8-1.9 4.8-1.9zM18.5 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/></svg>',
    wrong:S+'<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/></svg>',
    meq:S+'<path d="M7 3.5h7l4.5 4.5v11A1.5 1.5 0 0 1 17 20.5H7A1.5 1.5 0 0 1 5.5 19V5A1.5 1.5 0 0 1 7 3.5z"/><path d="M13.5 3.5V8.5h5M8.5 12.5h7M8.5 16h5"/></svg>',
    osce:S+'<circle cx="12" cy="13" r="7"/><path d="M12 9.5V13l2.5 1.5M9.5 3.5h5"/></svg>',
    hide:S+'<path d="M3.5 12s3-6 8.5-6 8.5 6 8.5 6-3 6-8.5 6-8.5-6-8.5-6z"/><path d="M4 4l16 16"/></svg>',
    pin:S+'<path d="M5.5 4.5h13v10l-5 5h-8z"/><path d="M13.5 19.5v-5h5"/></svg>',
    swap:S+'<path d="M7 7h11l-3-3M17 17H6l3 3"/></svg>',
    toc:S+'<path d="M8.5 6.5h11M8.5 12h11M8.5 17.5h11M4.5 6.5h.01M4.5 12h.01M4.5 17.5h.01"/></svg>',
    theme:S+'<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"/></svg>',
    search:S+'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>'
  };

  /* ---------- นำทาง ---------- */
  function goView(v){state.view=v;state.pid=null;if(v!=="section"&&v!=="lecture"){state.sec=null}render();window.scrollTo({top:0})}
  function setCourse(set,dir){
    if(!set||set===state.course)return;state.course=set;
    if(["section","lecture"].indexOf(state.view)>=0)state.view="home";
    state.lec=null;state.sec=null;state.pid=null;TR.dir=dir||0;render();window.scrollTo({top:0});
    ensure(set).then(function(){TR.dir=dir||0;render()});
  }
  function shiftCourse(k){var a=COURSES.map(function(c){return c.set}),i=a.indexOf(state.course),j=i+k;
    if(j<0||j>=a.length){toast(k<0?"นี่คือชุดแรกแล้ว":"นี่คือชุดสุดท้ายแล้ว");return}
    setCourse(a[j],k);toast((k<0?"‹ ":"")+COURSES[j].label+(k>0?" ›":""))}
  function shiftSection(k){var list=allSections(),i=-1;list.forEach(function(x,n){if(x.sec.id===state.sec)i=n});var j=i+k;
    if(i<0||j<0||j>=list.length){toast(k<0?"นี่คือหัวข้อแรกของชุดแล้ว":"นี่คือหัวข้อสุดท้ายของชุดแล้ว");return}
    TR.dir=k;openSection(list[j].lec.lec,list[j].sec.id);toast((k<0?"‹ ":"")+list[j].sec.title.slice(0,40)+(k>0?" ›":""))}
  function shiftLecture(k){var ls2=lectures(),l=lecOf(state.lec),i=ls2.indexOf(l),j=i+k;
    if(i<0||j<0||j>=ls2.length){toast(k<0?"นี่คือคาบแรกแล้ว":"นี่คือคาบสุดท้ายแล้ว");return}
    state.lec=ls2[j].lec;TR.dir=k;render();window.scrollTo({top:0});toast("คาบ "+ls2[j].lec)}
  function shift(k){
    if(state.view==="section")return shiftSection(k);
    if(state.view==="lecture")return shiftLecture(k);
    return shiftCourse(k);
  }
  function openNext(){if(!loaded())return;var f=firstUnfinished();if(f)openSection(f.lec.lec,f.sec.id)}
  function aiOpen(){
    var fab=document.querySelector(".ai-fab"),pn=document.querySelector(".ai-panel");
    if(pn&&!pn.hidden){var ta=pn.querySelector("textarea");if(ta)ta.focus();return}
    if(fab&&!fab.hidden){fab.click();return}
    toast("ถาม AI ใช้ได้เมื่อเปิดหน้านี้ใน claude.ai ขณะล็อกอิน")}

  /* ---------- หน้าแรก ---------- */
  function cardStat(l){var n=l.sections.length,ok=0,w=0,q=0;l.sections.forEach(function(s){var st=secStat(s);if(st.complete)ok++;q+=s.items.length;s.items.forEach(function(it){var v=state.ans[it.id];if(v!=null&&v!==it.answer)w++})});return {n:n,ok:ok,w:w,q:q}}
  function viewHomeTR(){
    var c=course(),p=courseProgress(),t=todayCount(),wc=wrongCount(),nx=firstUnfinished(),ed=examDays(),now=new Date();
    var h="<section class='tr-home"+(TR.dir>0?" tr-slide-l":TR.dir<0?" tr-slide-r":"")+"'>";
    h+="<div class='tr-top'><div><h1>"+esc(c.label)+"</h1><div class='tr-thai'>"+esc(c.thai||"")+"</div></div><div class='tr-top-r'>"+
      (ed>=0?"<div class='tr-exam' title='สอบลงกอง 17–18 พ.ย.'><b>"+(ed?"อีก "+ed+" วัน":"วันนี้")+"</b><small>สอบลงกอง 17 พ.ย.</small></div>":"")+"</div></div>";
    h+="<div class='tr-hero-row'><section class='tr-hero' aria-label='ทวนวันนี้'><div class='tr-hero-r'><div class='tr-hero-t'>"+
      "<span class='tr-kicker'>วันนี้ "+thaiDate(now)+"</span><h2>ทวนวันนี้</h2><p>"+(t>=GOAL?"ครบเป้าแล้ว ทวนไป "+t+" หัวข้อ":"ทวนไปแล้ว "+t+" หัวข้อ จากเป้า "+GOAL+" หัวข้อ")+"</p></div>"+
      "<div class='tr-ring' style='--p:"+Math.min(1,t/GOAL).toFixed(2)+"' role='img' aria-label='ทวนแล้ว "+t+" จาก "+GOAL+"'><div class='tr-ring-in'><b>"+t+"/"+GOAL+"</b><small>หัวข้อ</small></div></div></div>"+
      (nx?"<button class='tr-next press' data-trnext='1'><span><small>เรียนต่อ · คาบ "+esc(nx.lec.lec)+"</small><b>"+esc(nx.sec.title)+"</b></span><i aria-hidden='true'>→</i></button>":"")+"</section>";
    var days=[],mx=1;for(var i=6;i>=0;i--){var d=new Date();d.setDate(d.getDate()-i);var v=dayCount(d);mx=Math.max(mx,v);days.push([d,v,i===0])}
    var tot=days.reduce(function(a,x){return a+x[1]},0),sk=streak();
    h+="<section class='tr-week' aria-label='7 วันล่าสุด'><h3>7 วันล่าสุด</h3><p>"+(sk?"ทวนติดกัน "+sk+" วัน · ":"")+"รวม "+tot+" หัวข้อ</p><div class='tr-bars'>"+
      days.map(function(x){return "<div class='"+(x[2]?"today":"")+"'><b>"+x[1]+"</b><i style='height:"+Math.max(6,Math.round(x[1]/mx*80))+"px'></i><span>"+WD[x[0].getDay()].replace(".","")+"</span></div>"}).join("")+"</div></section></div>";
    var meqN=lectures().reduce(function(a,l){return a+(l.meq||[]).length+(l.osce||[]).length},0);
    h+="<div class='tr-tiles'>"+
      "<button class='tr-tile press' data-trview='lectures'><small>เรียนจบ</small><b>"+p.done+"<em>/"+p.total+"</em></b></button>"+
      "<button class='tr-tile press"+(wc?" warn":"")+"' data-trview='review'><small>ข้อที่ผิด รอทวน</small><b>"+wc+"</b></button>"+
      "<button class='tr-tile press' data-trview='meq'><small>MEQ / OSCE</small><b>"+meqN+"</b></button>"+
      "<button class='tr-tile press tr-desk' data-trview='lectures'><small>รหัส นล. ที่ครอบคลุม</small><b>"+nlCount()+"</b></button></div>";
    h+="<div class='tr-whead'><h3>คาบเรียน</h3><span>"+lectures().length+" คาบ</span></div><div class='tr-grid'>";
    lectures().forEach(function(l){var s=cardStat(l);
      h+="<button class='tr-card press"+(s.ok===s.n?" done":"")+"' data-trlec='"+esc(l.lec)+"' aria-label='คาบ "+esc(l.lec)+" "+esc(l.title)+" เรียนแล้ว "+s.ok+" จาก "+s.n+" หัวข้อ'>"+
        "<div class='tr-c-top'><span class='tr-c-no'>"+esc(l.lec)+"</span>"+(l.date&&!/^TBD/.test(l.date)?"<span class='tr-c-day'>"+esc(l.date)+"</span>":"")+"</div>"+
        "<div class='tr-c-t'>"+esc(l.title)+"</div><div class='tr-c-bar'><i style='width:"+Math.round(s.ok*100/Math.max(1,s.n))+"%'></i></div>"+
        "<div class='tr-c-foot'><span class='tr-tag "+(s.ok===s.n?"ok":s.ok?"go":"")+"'>"+(s.ok===s.n?"✓ จบแล้ว":s.ok?"เรียน "+s.ok+"/"+s.n:"ยังไม่เริ่ม")+"</span>"+
        (s.w?"<span class='tr-tag bad'>ผิด "+s.w+"</span>":"")+"<span class='tr-tag'>"+s.q+" ข้อ</span></div></button>";
    });
    h+="</div><p class='tr-hint'>ดับเบิลคลิกพื้นที่ว่าง หรือกดค้าง 2 วินาที เพื่อหมุนเลือกคาบ · ปัดซ้าย-ขวาเพื่อเปลี่ยนชุดวิชา</p>";
    h+="<details class='tr-about'><summary>เกี่ยวกับชุด "+esc(c.label)+" และวิธีใช้</summary><div><p>"+esc(c.intro||"")+"</p>"+(c.howto?"<div class='callout'>"+md(c.howto)+"</div>":"")+"</div></details>";
    return h+"</section>";
  }

  /* ---------- หน้าต่างคาบ (เลื่อนขึ้นจากด้านล่าง) ---------- */
  var sh=el("dialog","tr-sheet");sh.setAttribute("aria-labelledby","trShT");document.body.appendChild(sh);var shClosing=false;
  function closeSheet(after){if(shClosing||!sh.open){if(after)after();return}shClosing=true;sh.classList.add("out");
    setTimeout(function(){if(sh.open)sh.close();sh.classList.remove("out");shClosing=false;if(after)after()},RM?0:170)}
  sh.addEventListener("cancel",function(e){e.preventDefault();closeSheet()});
  sh.addEventListener("click",function(e){if(e.target===sh)closeSheet()});
  function openLecSheet(l){
    if(!l)return;var s=cardStat(l),nx=l.sections.filter(function(x){return !secStat(x).complete})[0],hid=lecHidden(l);
    sh.innerHTML="<div class='tr-grab'></div>";
    var hd=el("div","tr-sh-head");hd.appendChild(el("div","tr-sh-ht","<small>คาบ "+esc(l.lec)+(l.date?" · "+esc(l.date):"")+" · เรียนแล้ว "+s.ok+"/"+s.n+" หัวข้อ</small><h3 id='trShT'>"+esc(l.title)+"</h3>"));
    var x=el("button","tr-x press","✕");x.type="button";x.setAttribute("aria-label","ปิด");x.addEventListener("click",function(){closeSheet()});hd.appendChild(x);sh.appendChild(hd);
    var body=el("div","tr-sh-body"),ol=el("ol","tr-sh-list");
    l.sections.forEach(function(sec){var st=secStat(sec),li=el("li"),b=el("button","press "+(st.complete?"ok":(st.answered||st.read)?"part":""));b.type="button";
      b.innerHTML="<span class='num' aria-hidden='true'></span><span class='tt'>"+esc(sec.title)+"</span><span class='qq'>"+sec.items.length+" ข้อ</span>";
      b.addEventListener("click",function(){closeSheet(function(){openSection(l.lec,sec.id)})});li.appendChild(b);ol.appendChild(li)});
    body.appendChild(ol);sh.appendChild(body);
    var ft=el("div","tr-sh-foot");
    var p=el("button","btn primary press",nx?"เรียนต่อหัวข้อ "+(l.sections.indexOf(nx)+1):"ทวนทั้งคาบอีกรอบ");p.type="button";
    p.addEventListener("click",function(){var t=nx||l.sections[0];closeSheet(function(){openSection(l.lec,t.id)})});ft.appendChild(p);
    var ac=el("div","tr-sh-acts");
    [["▶ พรีเซนต์คาบนี้",function(){closeSheet(function(){Pres.open(l.lec,"",null)})}],
     [hid?"เลิกโหมดทวน":"โหมดทวน",function(){state.hide=state.hide||{};var k=hideKey(l);if(state.hide[k])delete state.hide[k];else state.hide[k]=true;save();closeSheet(function(){state.view="lecture";state.lec=l.lec;render();window.scrollTo({top:0})})}],
     ["หน้าคาบ · MEQ "+(l.meq||[]).length+" · OSCE "+(l.osce||[]).length,function(){closeSheet(function(){state.view="lecture";state.lec=l.lec;state.sec=null;render();window.scrollTo({top:0})})}]
    ].forEach(function(a){var b=el("button","btn press",esc(a[0]));b.type="button";b.addEventListener("click",a[1]);ac.appendChild(b)});
    ft.appendChild(ac);sh.appendChild(ft);sh.showModal();
  }

  /* ---------- แถบล่างลอย (มือถือ) ---------- */
  var nav=el("nav","tr-bnav");nav.setAttribute("aria-label","หน้าหลักของแอป");
  var NAV=[["home","หน้าแรก"],["lectures","คาบเรียน"],["plus","ทางลัด"],["meq","ฝึกเขียน"],["review","ทบทวน"]],mb=null,nb={};
  NAV.forEach(function(x){var b=el("button","tr-bn"+(x[0]==="plus"?" tr-main":""));b.type="button";
    b.appendChild(el("span","tr-bn-ic",I[x[0]==="lectures"?"lec":x[0]==="meq"?"write":x[0]]));b.appendChild(el("span","tr-bn-t",x[1]));
    if(x[0]==="plus"){mb=b;b.setAttribute("aria-haspopup","menu");b.setAttribute("aria-expanded","false");b.setAttribute("aria-label","ทางลัด")}
    else b.addEventListener("click",function(){goView(x[0])});
    nb[x[0]]=b;nav.appendChild(b)});
  document.body.appendChild(nav);
  function pageOf(v){return v==="lectures"||v==="lecture"||v==="section"?"lectures":v==="meq"||v==="osce"?"meq":v==="review"?"review":"home"}

  /* ---------- แถบซ้าย (คอม) ---------- */
  var side=el("aside","tr-side");side.setAttribute("aria-label","เมนูหลัก");document.body.appendChild(side);
  function renderSide(){
    var pg=pageOf(state.view),wc=wrongCount(),pc=ls(PROGKEY)||{};
    var h="<div class='tr-sd-brand'><b>MED421 learn</b><span>Internal medicine</span></div>"+
      "<button class='tr-sd-plus press' data-trplus='1'>"+I.plus+"ทางลัด</button>"+
      "<button class='tr-sd-search press' data-trpal='1'>"+I.search+"<span>ค้นหา</span><span class='tr-kbd'>Ctrl K</span></button><nav class='tr-sd-nav'>";
    [["home","หน้าแรก","home"],["lectures","คาบเรียน","lec"],["meq","ฝึกเขียน MEQ/OSCE","write"],["review","ทบทวนข้อที่ผิด","review"]].forEach(function(x){
      h+="<button class='press' data-trview='"+x[0]+"'"+(pg===x[0]?" aria-current='page'":"")+">"+I[x[2]]+"<span>"+x[1]+"</span>"+(x[0]==="review"&&wc?"<span class='n'>"+wc+"</span>":"")+"</button>"});
    h+="<button class='press' data-trtoc='1'>"+I.toc+"<span>สารบัญหัวข้อ</span></button><button class='press' data-trai='1'>"+I.ai+"<span>ถาม AI</span></button>"+
      "<button class='press' data-trpin='1'>"+I.pin+"<span>Post-it ห้ามลืม</span></button></nav><div class='tr-sd-h'>ชุดวิชา</div><div class='tr-sd-courses'>";
    COURSES.forEach(function(c){var v=pc[c.set],pr=v==null?null:v;
      h+="<button class='tr-sd-c press' data-trcourse='"+esc(c.set)+"'"+(c.set===state.course?" aria-current='true'":"")+">"+
        "<span class='mr' style='--p:"+(pr||0).toFixed(2)+"'></span><b>"+esc(c.label)+"<small>"+esc(c.thai||"")+"</small></b><em>"+(pr==null?"":Math.round(pr*100)+"%")+"</em></button>"});
    var ss=document.getElementById("lsync");
    h+="</div><div class='tr-sd-foot'><span class='tr-sd-sync"+(ss&&/cloud/.test(ss.className)?" cloud":"")+"'><i></i>"+esc(ss?ss.textContent.trim():"")+"</span>"+
      "<button class='btn press' data-trtheme='1'>โหมดสี</button></div>";
    side.innerHTML=h;
  }
  (function(){var ss=document.getElementById("lsync");if(ss&&"MutationObserver" in window)new MutationObserver(function(){if(DESK.matches)renderSide()}).observe(ss,{childList:true,subtree:true,characterData:true,attributes:true})})();

  /* ---------- แถบขวา (คอมจอกว้าง) ---------- */
  var dock=el("aside","tr-dock");dock.setAttribute("aria-label","เครื่องมือข้างจอ");document.body.appendChild(dock);
  function renderDock(){
    if(!WIDE.matches){dock.innerHTML="";return}
    var w=wrongList().slice(0,4),pins=(ls(PINKEY)||[]).slice(-4).reverse();
    var h="<section class='tr-dk'><div class='tr-dk-h'><h3>ข้อที่ผิดในชุดนี้</h3><small>"+wrongCount()+" ข้อ</small></div>";
    h+=w.length?"<ul class='tr-wl'>"+w.map(function(x){return "<li><button class='press' data-trsec='"+esc(x.s.id)+"' data-trsl='"+esc(x.l.lec)+"'><small>ผิด "+x.n+" ข้อ · คาบ "+esc(x.l.lec)+"</small><span>"+esc(x.s.title)+"</span></button></li>"}).join("")+"</ul>":"<p class='tr-empty'>ยังไม่มีข้อที่ตอบผิดในชุดนี้</p>";
    h+="</section><section class='tr-dk'><div class='tr-dk-h'><h3>ปักจากหน้านี้ล่าสุด</h3><small>เครื่องนี้</small></div>";
    h+=pins.length?"<div class='tr-pins'>"+pins.map(function(p,i){return "<div class='tr-pn' style='--r:"+(i%2?1.2:-1.5)+"deg'><small>"+esc(p.k)+"</small>"+esc(p.t)+"</div>"}).join("")+"</div>":"<p class='tr-empty'>กดปุ่มปักตาราง หลักจำ หรือหัวข้อใน Post-it แล้วจะขึ้นที่นี่</p>";
    h+="</section><section class='tr-dk'><div class='tr-dk-h'><h3>คีย์ลัด</h3></div><ul class='tr-keys'>"+
      [["ค้นหาหัวข้อทุกวิชา","Ctrl K"],["ตอบข้อสอบ (เปิดข้อสอบแล้ว)","1–5"],["หัวข้อ/ชุดก่อน-ถัดไป","Alt ← →"],["หมุนเลือกคาบ","ดับเบิลคลิก"],["ทางลัด","+"]].map(function(x){return "<li><span>"+x[0]+"</span><span class='tr-kbd'>"+x[1]+"</span></li>"}).join("")+"</ul></section>";
    dock.innerHTML=h;
  }
  document.addEventListener("click",function(e){
    var a=e.target.closest&&e.target.closest("a[data-tqpin],a[data-mnpin],a.chip.acc[href*='BRsYSzd35']");if(!a)return;
    var k=a.hasAttribute("data-tqpin")?"ตาราง":a.hasAttribute("data-mnpin")?"หลักจำ":"หัวข้อ",t="";
    if(k==="ตาราง"){var bar=a.closest(".tqbar"),tw=bar&&bar.nextElementSibling,hh=tw&&tw.previousElementSibling;while(hh&&!/^H[34]$/.test(hh.tagName))hh=hh.previousElementSibling;t=hh?hh.textContent:"ตาราง"}
    else if(k==="หลักจำ"){var m=a.closest(".mnem"),b=m&&m.querySelector(".mnh b");t=b?b.textContent:"หลักจำ"}
    else{var s=secOf(lecOf(state.lec),state.sec);t=s?s.title:"หัวข้อ"}
    var arr=ls(PINKEY)||[];arr.push({k:k,t:String(t).slice(0,80),at:Date.now()});ls(PINKEY,arr.slice(-30));setTimeout(renderDock,50);
  },true);
  /* ถาม AI ติดข้างจอ */
  (function(){
    var tries=0,iv=setInterval(function(){
      var pn=document.querySelector(".ai-panel"),fab=document.querySelector(".ai-fab");if(!pn||!fab){if(++tries>40)clearInterval(iv);return}
      clearInterval(iv);
      function unfocus(){setTimeout(function(){var a=document.activeElement;if(a&&a.closest&&a.closest(".ai-panel"))a.blur()},200)}
      function sync(){document.documentElement.classList.toggle("tr-ai",WIDE.matches&&!pn.hidden)}
      new MutationObserver(sync).observe(pn,{attributes:true,attributeFilter:["hidden"]});
      var auto=false;try{auto=sessionStorage.getItem("tr-ai-closed")!=="1"}catch(e){auto=true}
      new MutationObserver(function(){if(WIDE.matches&&auto&&!fab.hidden&&pn.hidden){auto=false;fab.click();unfocus()}}).observe(fab,{attributes:true,attributeFilter:["hidden"]});
      pn.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("[data-ai='close']");if(b)try{sessionStorage.setItem("tr-ai-closed","1")}catch(_){}});
      if(WIDE.matches&&auto&&!fab.hidden&&pn.hidden){auto=false;fab.click();unfocus()}
      sync();WIDE.addEventListener&&WIDE.addEventListener("change",sync);
    },250);
  })();

  /* ---------- วงล้อทางลัด ---------- */
  var A=[["next","เรียนต่อ","เปิดหัวข้อที่ค้างไว้"],["pres","พรีเซนต์","อธิบายทั้งคาบ บนจอมีแค่คีย์เวิร์ด"],["ai","ถาม AI","ถามเรื่องหัวข้อที่เปิดอยู่"],
    ["wrong","ข้อที่ผิด","ทำข้อที่เคยผิดใหม่"],["meq","MEQ","ฝึกเขียนตอบ MEQ"],["osce","OSCE","สถานี OSCE/SAQ จับเวลา"],["hide","โหมดทวน","ซ่อนเนื้อหาของคาบนี้"],
    ["pin","Post-it","เปิดกระดาน Post-it ห้ามลืม"],["swap","สลับคาบ","หมุนเลือกคาบในชุดนี้"],["toc","สารบัญ","รายการหัวข้อทั้งหมด"],["theme","โหมดสี","สลับสว่าง/มืด/ตามเครื่อง"]];
  var N=A.length,RO=160,RI=78,GAP=1.6,PUSH=8,M=null;
  function pt(r,a){var t=a*Math.PI/180;return [r*Math.cos(t),r*Math.sin(t)]}
  function sector(a0,a1){var p1=pt(RO,a0),p2=pt(RO,a1),p3=pt(RI,a1),p4=pt(RI,a0),f=function(v){return v.toFixed(2)};
    return "M"+f(p1[0])+" "+f(p1[1])+"A"+RO+" "+RO+" 0 0 1 "+f(p2[0])+" "+f(p2[1])+"L"+f(p3[0])+" "+f(p3[1])+"A"+RI+" "+RI+" 0 0 0 "+f(p4[0])+" "+f(p4[1])+"Z"}
  function toc(){
    if(DESK.matches){document.body.classList.toggle("tr-toc");return}
    var o=document.getElementById("outline");if(!o||getComputedStyle(o).display==="none"){toast("เปิดคาบหรือหัวข้อก่อน แล้วสารบัญจะอยู่ท้ายหน้า");return}
    try{o.scrollIntoView({behavior:RM?"auto":"smooth"})}catch(_){}o.classList.remove("tr-flash");void o.offsetWidth;o.classList.add("tr-flash")}
  function act(k){
    if(k==="next")return openNext();
    if(k==="pres"){var lid=state.lec||(firstUnfinished()&&firstUnfinished().lec.lec);if(lid)Pres.open(lid,state.view==="section"?state.sec:"",null);return}
    if(k==="ai")return aiOpen();
    if(k==="wrong")return goView("review");
    if(k==="meq")return goView("meq");
    if(k==="osce")return goView("osce");
    if(k==="hide"){var l=lecOf(state.lec);if(!l){toast("เปิดคาบหรือหัวข้อก่อน แล้วค่อยใช้โหมดทวน");return}state.hide=state.hide||{};var hk=hideKey(l);if(state.hide[hk])delete state.hide[hk];else state.hide[hk]=true;render();toast(state.hide[hk]?"โหมดทวน: ซ่อนเนื้อหาแล้ว":"แสดงเนื้อหาแล้ว");return}
    if(k==="pin"){window.open(POSTIT,"_blank","noopener");return}
    if(k==="swap")return openWheel();
    if(k==="toc")return toc();
    if(k==="theme"){var tb=document.getElementById("themeBtn");if(tb)tb.click();var th=state.theme;toast(th==="dark"?"โหมดมืด":th==="light"?"โหมดสว่าง":"ตามเครื่อง");return}
  }
  function openMenu(drag){
    if(M)return;
    var ov=el("div","tr-rm");ov.setAttribute("role","menu");ov.setAttribute("aria-label","ทางลัด");
    var ring=el("div","tr-rm-ring");ov.appendChild(ring);
    var NS="http://www.w3.org/2000/svg",svg=document.createElementNS(NS,"svg");svg.setAttribute("class","tr-rm-svg");svg.setAttribute("viewBox","-170 -170 340 340");svg.setAttribute("aria-hidden","true");ring.appendChild(svg);
    var segs=[],its=[],wc=wrongCount();
    A.forEach(function(x,i){
      var a=-90+i*360/N,hh=180/N,pv=pt(PUSH,a);
      var g=document.createElementNS(NS,"g");g.setAttribute("class","tr-rm-seg");
      g.style.setProperty("--tx",pv[0].toFixed(1)+"px");g.style.setProperty("--ty",pv[1].toFixed(1)+"px");g.style.setProperty("--d",(i*26)+"ms");
      var pa=document.createElementNS(NS,"path");pa.setAttribute("d",sector(a-hh+GAP,a+hh-GAP));g.appendChild(pa);
      var gl=document.createElementNS(NS,"path");gl.setAttribute("class","tr-rm-glow");var o0=pt(RO+7,a-hh+GAP+2),o1=pt(RO+7,a+hh-GAP-2);
      gl.setAttribute("d","M"+o0[0].toFixed(2)+" "+o0[1].toFixed(2)+"A"+(RO+7)+" "+(RO+7)+" 0 0 1 "+o1[0].toFixed(2)+" "+o1[1].toFixed(2));g.appendChild(gl);
      svg.appendChild(g);segs.push(g);
      var c=pt((RO+RI)/2,a),it=el("button","tr-rm-it");it.type="button";it.setAttribute("role","menuitem");it.tabIndex=-1;
      it.style.setProperty("--x",c[0].toFixed(1)+"px");it.style.setProperty("--y",c[1].toFixed(1)+"px");it.style.setProperty("--tx",pv[0].toFixed(1)+"px");it.style.setProperty("--ty",pv[1].toFixed(1)+"px");it.style.setProperty("--d",(i*26)+"ms");
      it.innerHTML=I[x[0]];it.appendChild(el("span",null,x[1]));it.setAttribute("aria-label",x[1]+" "+x[2]);
      if(x[0]==="wrong"&&wc)it.appendChild(el("span","n",String(wc)));
      if(x[0]==="hide"&&!state.lec)it.classList.add("off");
      it.addEventListener("click",function(e){e.stopPropagation();pick(i)});
      ring.appendChild(it);its.push(it);
    });
    var hc=document.createElementNS(NS,"circle");hc.setAttribute("class","tr-rm-hubc");hc.setAttribute("r",RI-8);svg.appendChild(hc);
    var hub=el("div","tr-rm-hub");hub.appendChild(el("span","tg",esc(course()?course().label:"")));var hb=el("b",null,"ทางลัด"),hs=el("small",null,drag?"ลากไปที่ช่องแล้วปล่อย":"แตะช่องที่ต้องการ");hub.appendChild(hb);hub.appendChild(hs);ring.appendChild(hub);
    var tip=el("div","tr-rm-tip","แตะนอกวงหรือกด Esc เพื่อปิด");ov.appendChild(tip);
    document.body.appendChild(ov);mb.classList.add("on");mb.setAttribute("aria-expanded","true");
    var cx=0,cy=0,hl=-1,closing=false;
    function place(){
      if(DESK.matches){var rw=WIDE.matches?376:0;cx=264+(window.innerWidth-264-rw)/2;cy=window.innerHeight/2}
      else{var nbt=nav.getBoundingClientRect().top;cx=window.innerWidth/2;cy=Math.max(190,Math.min(nbt-RO-36,nbt/2+10))}
      ring.style.left=cx+"px";ring.style.top=cy+"px";tip.style.top=(cy+RO+18)+"px"}
    function setHl(i){if(i===hl)return;if(hl>=0){segs[hl].classList.remove("hl");segs[hl].querySelector(".tr-rm-glow").classList.remove("on");its[hl].classList.remove("hl")}hl=i;
      if(i>=0){segs[i].classList.add("hl");segs[i].querySelector(".tr-rm-glow").classList.add("on");its[i].classList.add("hl");hb.textContent=A[i][1];hs.textContent=A[i][2];if(navigator.vibrate&&drag)try{navigator.vibrate(4)}catch(e){}}
      else{hb.textContent="ทางลัด";hs.textContent=drag?"ลากไปที่ช่องแล้วปล่อย":"แตะช่องที่ต้องการ"}}
    function at(x,y){var dx=x-cx,dy=y-cy,d=Math.sqrt(dx*dx+dy*dy);if(d<RI*.7||d>RO+40)return{i:-1};var a=Math.atan2(dy,dx)*180/Math.PI+90;return{i:Math.round(((a%360)+360)%360/(360/N))%N}}
    function pick(i){if(closing||i<0)return;setHl(i);var s=segs[i];s.classList.remove("pick");void s.getBoundingClientRect();s.classList.add("pick");var k=A[i][0];setTimeout(function(){close(function(){act(k)})},RM?0:180)}
    function close(after){if(closing)return;closing=true;ov.classList.remove("on");ov.classList.add("out");mb.classList.remove("on");mb.setAttribute("aria-expanded","false");
      document.removeEventListener("keydown",key,true);window.removeEventListener("resize",place);window.removeEventListener("pointermove",mv,true);window.removeEventListener("pointerup",up,true);window.removeEventListener("pointercancel",up,true);
      setTimeout(function(){if(ov.parentNode)ov.remove();M=null;if(after)after()},RM?0:170)}
    function key(e){if(e.key==="Escape"){e.preventDefault();close()}
      else if(e.key==="ArrowRight"||e.key==="ArrowDown"){e.preventDefault();setHl((hl+1+N)%N);its[hl].focus({preventScroll:true})}
      else if(e.key==="ArrowLeft"||e.key==="ArrowUp"){e.preventDefault();setHl(hl<0?N-1:(hl-1+N)%N);its[hl].focus({preventScroll:true})}
      else if((e.key==="Enter"||e.key===" ")&&hl>=0){e.preventDefault();pick(hl)}}
    var dragging=!!drag,moved=false,sx=drag?drag.x:0,sy=drag?drag.y:0;
    function mv(e){var r=at(e.clientX,e.clientY);if(dragging&&(Math.abs(e.clientX-sx)>10||Math.abs(e.clientY-sy)>10))moved=true;if(e.pointerType==="mouse"||dragging)setHl(r.i)}
    function up(e){if(!dragging)return;dragging=false;if(moved){var r=at(e.clientX,e.clientY);if(r.i>=0)pick(r.i);else setHl(-1)}}
    window.addEventListener("pointermove",mv,true);window.addEventListener("pointerup",up,true);window.addEventListener("pointercancel",up,true);
    ov.addEventListener("click",function(e){if(e.target.closest&&e.target.closest(".tr-rm-it"))return;var r=at(e.clientX,e.clientY);if(r.i>=0)pick(r.i);else close()});
    document.addEventListener("keydown",key,true);window.addEventListener("resize",place);
    place();requestAnimationFrame(function(){if(!closing)ov.classList.add("on")});
    if(!drag)setTimeout(function(){if(!closing)try{its[0].focus({preventScroll:true});setHl(0)}catch(_){}},RM?0:120);
    M={close:close};
  }
  var lastPD=0;
  mb.addEventListener("pointerdown",function(e){if(e.button>0)return;lastPD=Date.now();e.preventDefault();if(M){M.close();return}openMenu({x:e.clientX,y:e.clientY})});
  mb.addEventListener("click",function(){if(Date.now()-lastPD>800){if(M)M.close();else openMenu(null)}});

  /* ---------- วงล้อสลับคาบ (ดับเบิลคลิก / กดค้าง 2 วิ) ---------- */
  var W=null;
  function openWheel(){
    if(W||!loaded())return;var L=lectures();if(!L.length)return;
    if(sh.open)closeSheet();
    var curI=Math.max(0,L.indexOf(lecOf(state.lec)));
    var ov=el("div","tr-wheel");ov.setAttribute("role","dialog");ov.setAttribute("aria-modal","true");ov.setAttribute("aria-label","สลับคาบ");
    var head=el("div","tr-wh-head");head.appendChild(el("b",null,"สลับคาบ · "+esc(course().label)));head.appendChild(el("span",null,L.length+" คาบในชุดนี้"));ov.appendChild(head);
    var cl=el("button","tr-wh-close","✕");cl.type="button";cl.setAttribute("aria-label","ปิด");ov.appendChild(cl);
    var stage=el("div","tr-wh-stage");ov.appendChild(stage);
    var NS="http://www.w3.org/2000/svg",svg=document.createElementNS(NS,"svg");svg.setAttribute("class","tr-wh-arc");var circ=document.createElementNS(NS,"circle");svg.appendChild(circ);stage.appendChild(svg);
    var knob=el("div","tr-wh-knob");stage.appendChild(knob);
    ov.appendChild(el("div","tr-wh-foot","ลากขึ้นลงหรือหมุนลูกกลิ้งเพื่อเลื่อน แตะคาบเพื่อเปิด"));
    var nodes=L.map(function(l,i){var s=cardStat(l);
      var n=el("div","tr-wh-it");if(state.lec&&l.lec===state.lec)n.classList.add("cur");
      var inr=el("div","tr-wh-in");inr.style.setProperty("--d",(Math.min(6,Math.abs(i-curI))*40)+"ms");
      var lb=el("div","tr-wh-lbl");lb.appendChild(el("b",null,esc(l.title)));lb.appendChild(el("small",null,"เรียนแล้ว "+s.ok+"/"+s.n+" หัวข้อ"+(l.date?" · "+esc(l.date):"")));
      var c=el("button","tr-wh-chip",esc(l.lec));c.type="button";c.setAttribute("aria-label","คาบ "+l.lec+" "+l.title);
      c.appendChild(el("span","dd"+(s.ok===s.n?" ok":""),s.ok===s.n?"✓":s.ok+"/"+s.n));
      inr.appendChild(lb);inr.appendChild(c);n.appendChild(inr);stage.appendChild(n);return n});
    document.body.appendChild(ov);document.body.classList.add("tr-lock");
    var wt=null,p=curI,anim=null,R=0,x0=0,cy=0,STEP=92,shown=-1,busy=false,closing=false;
    function geo(){var sw=stage.clientWidth,shh=stage.clientHeight;R=Math.max(shh*.78,440);x0=sw-148;cy=shh/2;var ax=x0+96,cx=ax+R;
      circ.setAttribute("cx",cx);circ.setAttribute("cy",cy);circ.setAttribute("r",R);circ.style.setProperty("--len",Math.ceil(2*Math.PI*R));knob.style.left=ax+"px";knob.style.top=cy+"px"}
    function paint(){
      for(var i=0;i<nodes.length;i++){var k=i-p,a=k*STEP/R,n=nodes[i],ak=Math.abs(k);
        if(ak>6){n.style.visibility="hidden";continue}n.style.visibility="";
        var x=x0+R*(1-Math.cos(a))+36,y=cy+R*Math.sin(a),sc=Math.max(.72,1-ak*.07);
        n.style.transform="translate("+x+"px,"+y+"px) translate(-100%,-50%) rotate("+(-a)+"rad) scale("+sc+")";
        n.style.opacity=Math.max(0,1-ak*.2);n.style.zIndex=String(100-Math.round(ak*10))}
      var c=Math.round(p);if(c!==shown){if(shown>=0&&nodes[shown])nodes[shown].classList.remove("on");shown=c;if(nodes[c])nodes[c].classList.add("on");if(anim&&navigator.vibrate)try{navigator.vibrate(4)}catch(e){}}}
    function clamp(v){return Math.max(0,Math.min(L.length-1,v))}
    function goTo(t,done){t=clamp(t);cancelAnimationFrame(anim);
      if(RM){p=t;paint();anim=null;if(done)done();return}
      var from=p,t0=performance.now(),dur=Math.min(520,220+Math.abs(t-from)*70);
      (function f(now){if(closing&&!done)return;var u=Math.min(1,(now-t0)/dur),e=1-Math.pow(1-u,3);p=from+(t-from)*e;paint();
        if(u<1)anim=requestAnimationFrame(f);else{anim=null;if(done)done()}})(t0)}
    function choose(i){if(busy)return;busy=true;goTo(i,function(){nodes[i].classList.add("pick");setTimeout(function(){close(function(){openLecSheet(L[i])})},RM?0:260)})}
    function close(after){if(closing)return;closing=true;busy=true;cancelAnimationFrame(anim);clearTimeout(wt);ov.classList.remove("on");ov.classList.add("out");
      document.removeEventListener("keydown",key,true);window.removeEventListener("resize",rs);
      setTimeout(function(){if(ov.parentNode)ov.remove();W=null;document.body.classList.remove("tr-lock");if(after)after()},RM?0:200)}
    function key(e){if(closing)return;if(e.key==="Escape"){e.preventDefault();close()}
      else if(e.key==="ArrowDown"||e.key==="ArrowRight"){e.preventDefault();goTo(Math.round(p)+1)}
      else if(e.key==="ArrowUp"||e.key==="ArrowLeft"){e.preventDefault();goTo(Math.round(p)-1)}
      else if(e.key==="Enter"||e.key===" "){if(document.activeElement===cl)return;e.preventDefault();choose(Math.round(p))}}
    function rs(){if(!closing){geo();paint()}}
    var drag=null;
    ov.addEventListener("pointerdown",function(e){if(e.target===cl)return;cancelAnimationFrame(anim);anim=null;drag={tg:e.target,y:e.clientY,p:p,v:0,moved:0,id:e.pointerId,ly:e.clientY,lt:performance.now()};try{ov.setPointerCapture(e.pointerId)}catch(_){}});
    ov.addEventListener("pointermove",function(e){if(!drag||e.pointerId!==drag.id)return;var dy=e.clientY-drag.y;drag.moved=Math.max(drag.moved,Math.abs(dy));
      var now=performance.now(),dt=Math.max(1,now-drag.lt);drag.v=.8*((drag.ly-e.clientY)/STEP/dt)+.2*drag.v;drag.ly=e.clientY;drag.lt=now;
      var np=drag.p-dy/STEP;if(np<0)np=np*.35;else if(np>L.length-1)np=L.length-1+(np-L.length+1)*.35;p=np;paint()});
    function up(e){if(!drag||e.pointerId!==drag.id)return;var d=drag;drag=null;
      if(d.moved<8){var tg=d.tg||e.target,c=tg.closest&&tg.closest(".tr-wh-chip,.tr-wh-lbl");
        if(c){var i=nodes.indexOf(c.closest(".tr-wh-it"));if(i>=0){choose(i);return}}
        if(!(tg.closest&&tg.closest(".tr-wh-it"))&&e.clientX<stage.getBoundingClientRect().left+40){close();return}
        goTo(Math.round(p));return}
      goTo(Math.round(p+d.v*220))}
    ov.addEventListener("pointerup",up);ov.addEventListener("pointercancel",up);
    ov.addEventListener("wheel",function(e){e.preventDefault();cancelAnimationFrame(anim);anim=null;p=clamp(p+e.deltaY/(e.deltaMode===1?3:120));paint();clearTimeout(wt);wt=setTimeout(function(){goTo(Math.round(p))},120)},{passive:false});
    cl.addEventListener("click",function(){close()});
    ov.addEventListener("click",function(e){e.stopPropagation()});
    document.addEventListener("keydown",key,true);window.addEventListener("resize",rs);
    geo();paint();
    requestAnimationFrame(function(){if(closing)return;ov.classList.add("on");var c=nodes[curI]&&nodes[curI].querySelector(".tr-wh-chip");if(c)try{c.focus({preventScroll:true})}catch(_){}});
    W={close:close};
  }
  /* ไม่เริ่มบนเนื้อหา/ข้อสอบ/ตาราง/ภาพ เพื่อไม่แย่งการเลือกข้อความไปถาม AI */
  var SKIP="input,textarea,select,[contenteditable],dialog,button,a,label,summary,.prose,.q,.vignette,.fig,table,.tablewrap,.ai-panel,.ai-sel,.pv,.tr-wheel,.tr-rm,.tr-bnav,.tr-side,.tr-dock,.mast,.tr-pal";
  var lastPT="mouse";
  document.addEventListener("pointerdown",function(e){lastPT=e.pointerType||"mouse"},true);
  document.addEventListener("dblclick",function(e){
    if(lastPT!=="mouse"||document.querySelector(".pv"))return;var t=e.target;if(!t||!t.closest||t.closest(SKIP))return;
    try{var sl=window.getSelection();if(sl)sl.removeAllRanges()}catch(_){}
    openWheel()});
  var hold=null,lring=null;
  function endHold(){if(!hold)return;clearTimeout(hold.t);clearTimeout(hold.rt);hold=null;document.body.classList.remove("tr-arm");if(lring){var r=lring;lring=null;r.classList.remove("go");setTimeout(function(){r.remove()},200)}}
  document.addEventListener("touchstart",function(e){
    endHold();if(W||M||sh.open||document.querySelector(".pv")||e.touches.length!==1)return;var t=e.target;if(!t||!t.closest||t.closest(SKIP))return;
    var tc=e.touches[0];hold={x:tc.clientX,y:tc.clientY};document.body.classList.add("tr-arm");
    hold.rt=setTimeout(function(){if(!hold)return;lring=el("div","tr-lp",'<svg viewBox="0 0 72 72" aria-hidden="true"><circle cx="36" cy="36" r="32"/></svg>');lring.style.left=hold.x+"px";lring.style.top=hold.y+"px";document.documentElement.appendChild(lring);requestAnimationFrame(function(){if(lring)lring.classList.add("go")})},250);
    hold.t=setTimeout(function(){if(!hold)return;endHold();if(navigator.vibrate)try{navigator.vibrate(12)}catch(_){}
      var until=Date.now()+900;document.addEventListener("click",function sup(ev){document.removeEventListener("click",sup,true);if(Date.now()<until){ev.preventDefault();ev.stopPropagation()}},true);openWheel()},2000);
  },{passive:true});
  document.addEventListener("touchmove",function(e){if(!hold)return;var tc=e.touches[0];if(!tc||Math.abs(tc.clientX-hold.x)>10||Math.abs(tc.clientY-hold.y)>10)endHold()},{passive:true});
  document.addEventListener("touchend",endHold,{passive:true});
  document.addEventListener("touchcancel",endHold,{passive:true});
  document.addEventListener("contextmenu",function(e){if(hold||W)e.preventDefault()});
  document.addEventListener("scroll",function(){if(hold)endHold()},{passive:true,capture:true});

  /* ---------- ปัดซ้าย-ขวา ---------- */
  function blocked(t){
    if(!t||!t.closest)return true;
    if(t.closest("input,textarea,select,dialog,.mast,.tr-rm,.tr-wheel,.tr-bnav,.pv,.ai-panel,.fig,.tr-pal"))return true;
    for(var n=t;n&&n!==document.body;n=n.parentElement){var cs=getComputedStyle(n);if((cs.overflowX==="auto"||cs.overflowX==="scroll")&&n.scrollWidth>n.clientWidth+2)return true}
    return false}
  var sx=0,sy=0,stt=0,okT=false;
  document.addEventListener("touchstart",function(e){if(e.touches.length!==1){okT=false;return}var t=e.touches[0];sx=t.clientX;sy=t.clientY;stt=Date.now();
    okT=!blocked(e.target)&&!sh.open&&!W&&!M&&!(window.getSelection&&String(window.getSelection()).length)},{passive:true});
  document.addEventListener("touchend",function(e){if(!okT)return;okT=false;var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;
    if(Date.now()-stt>800||Math.abs(dx)<70||Math.abs(dy)>Math.abs(dx)*.5)return;shift(dx<0?1:-1)},{passive:true});

  /* ---------- ค้นหาหัวข้อทุกวิชา (Ctrl K) ---------- */
  var PAL=null;
  function openPal(){
    if(PAL)return;
    var ov=el("div","tr-pal"),box=el("div","tr-pal-box");ov.appendChild(box);ov.setAttribute("role","dialog");ov.setAttribute("aria-modal","true");ov.setAttribute("aria-label","ค้นหาหัวข้อ");
    var iw=el("div","tr-pal-in",I.search);var inp=el("input");inp.placeholder="ค้นหาหัวข้อ คาบ หรือคำสำคัญ เช่น retic, gout, AKI";inp.setAttribute("aria-label","ค้นหา");iw.appendChild(inp);box.appendChild(iw);
    var ul=el("ul","tr-pal-list");ul.setAttribute("role","listbox");box.appendChild(ul);
    var ft=el("div","tr-pal-foot","<span><span class='tr-kbd'>↑ ↓</span> เลือก</span><span><span class='tr-kbd'>Enter</span> เปิด</span><span><span class='tr-kbd'>Esc</span> ปิด</span><span class='ld'></span>");box.appendChild(ft);
    document.body.appendChild(ov);var sel=0,res=[],idx=[];
    function build(){idx=[];var miss=0;COURSES.forEach(function(c){if(!c._loaded){miss++;return}
      (c.lectures||[]).forEach(function(l){idx.push({c:c,l:l,s:null,t:l.title,sub:"คาบ "+l.lec});l.sections.forEach(function(s){idx.push({c:c,l:l,s:s,t:s.title,sub:"คาบ "+l.lec+" · "+l.title})})})});
      ft.querySelector(".ld").textContent=miss?"กำลังโหลดอีก "+miss+" ชุด…":"ค้นได้ครบทุกชุด"}
    function hl(t,q){if(!q)return esc(t);var i=t.toLowerCase().indexOf(q.toLowerCase());return i<0?esc(t):esc(t.slice(0,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length))}
    function draw(){var q=inp.value.trim().toLowerCase();
      res=q?idx.filter(function(x){return (x.t+" "+x.sub+" "+x.c.label).toLowerCase().indexOf(q)>=0}).slice(0,12):idx.filter(function(x){return !x.s&&x.c.set===state.course});
      sel=Math.min(sel,Math.max(0,res.length-1));ul.innerHTML="";
      if(!res.length){ul.appendChild(el("li","tr-pal-empty","ไม่พบ ลองคำอื่น"));return}
      res.forEach(function(x,i){var li=el("li"),b=el("button",i===sel?"on":"","<span class='pc'>"+esc(x.c.label)+" · "+(x.s?"หัวข้อ":"คาบ")+"</span><span class='pt'>"+hl(x.t,inp.value.trim())+"<small>"+esc(x.sub)+"</small></span>");b.type="button";b.setAttribute("role","option");
        b.addEventListener("mousemove",function(){if(sel!==i){sel=i;draw()}});b.addEventListener("click",function(){choose(i)});li.appendChild(b);ul.appendChild(li)})}
    function choose(i){var x=res[i];if(!x)return;close();
      var go=function(){if(x.s)openSection(x.l.lec,x.s.id);else{state.view="lecture";state.lec=x.l.lec;state.sec=null;render();window.scrollTo({top:0})}};
      if(x.c.set!==state.course){state.course=x.c.set;ensure(x.c.set).then(go)}else go()}
    function close(){if(!PAL)return;PAL=null;ov.remove()}
    inp.addEventListener("input",function(){sel=0;draw()});
    inp.addEventListener("keydown",function(e){if(e.key==="ArrowDown"){e.preventDefault();sel=Math.min(res.length-1,sel+1);draw()}else if(e.key==="ArrowUp"){e.preventDefault();sel=Math.max(0,sel-1);draw()}else if(e.key==="Enter"){e.preventDefault();choose(sel)}else if(e.key==="Escape"){e.preventDefault();close()}});
    ov.addEventListener("mousedown",function(e){if(e.target===ov)close()});
    PAL={close:close};build();draw();inp.focus();
    Promise.all(COURSES.map(function(c){return ensure(c.set)})).then(function(){if(PAL){build();draw()}});
  }

  /* ---------- คีย์บอร์ด ---------- */
  document.addEventListener("keydown",function(e){
    if((e.ctrlKey||e.metaKey)&&(e.key==="k"||e.key==="K")&&!document.querySelector(".pv")&&!PAL){e.preventDefault();openPal();return}
    var tg=e.target&&e.target.tagName;if(tg==="INPUT"||tg==="TEXTAREA"||tg==="SELECT"||(e.target&&e.target.isContentEditable))return;
    if(document.querySelector(".pv"))return;
    if(PAL||W||M||sh.open)return;
    if(e.key==="/"&&DESK.matches){e.preventDefault();openPal();return}
    if(e.altKey&&(e.key==="ArrowLeft"||e.key==="ArrowRight")){e.preventDefault();shift(e.key==="ArrowLeft"?-1:1);return}
    if(e.key==="+"&&!e.ctrlKey&&!e.metaKey){e.preventDefault();openMenu(null);return}
    if(state.view==="section"&&/^[1-5]$/.test(e.key)&&!e.ctrlKey&&!e.metaKey&&!e.altKey){
      var q=[].filter.call(document.querySelectorAll("#main div.q[id^='q-']"),function(x){return x.offsetParent!==null&&!x.querySelector(".ch:disabled")})[0];
      if(q){var b=q.querySelectorAll(".ch")[+e.key-1];if(b){e.preventDefault();b.click()}}}
  });

  /* ---------- คลิกในชั้นนี้ ---------- */
  document.addEventListener("click",function(e){
    var b=e.target.closest&&e.target.closest("button");if(!b)return;
    if(b.dataset.trnext){pop(b);openNext();return}
    if(b.dataset.trlec){pop(b);openLecSheet(lecOf(b.dataset.trlec));return}
    if(b.dataset.trview){goView(b.dataset.trview);return}
    if(b.dataset.trsec){openSection(b.dataset.trsl,b.dataset.trsec);return}
    if(b.dataset.trcourse){setCourse(b.dataset.trcourse);return}
    if(b.dataset.trplus){openMenu(null);return}
    if(b.dataset.trpal){openPal();return}
    if(b.dataset.trtoc){toc();return}
    if(b.dataset.trai){aiOpen();return}
    if(b.dataset.trpin){window.open(POSTIT,"_blank","noopener");return}
    if(b.dataset.trtheme){act("theme");return}
    if(b.dataset.trgate){var sid=b.dataset.trgate;GATE[sid]=1;var m=document.getElementById("main"),g=m.querySelector(".tr-gate");if(g)g.remove();
      m.querySelectorAll("[data-trhid]").forEach(function(x){x.hidden=false;x.removeAttribute("data-trhid")});
      var qz=m.querySelector(".quiz");if(qz){qz.classList.add("tr-qin");setTimeout(function(){try{qz.scrollIntoView({block:"start",behavior:RM?"auto":"smooth"})}catch(_){}},40)}return}
  });

  /* ---------- หลัง render ทุกครั้ง ---------- */
  function after(){
    document.body.dataset.view=state.view||"home";
    var pg=pageOf(state.view);Object.keys(nb).forEach(function(k){if(k===pg)nb[k].setAttribute("aria-current","page");else nb[k].removeAttribute("aria-current")});
    var wc=loaded()?wrongCount():0,rb=nb.review,bn=rb.querySelector(".n");if(wc){if(!bn){bn=el("span","n");rb.appendChild(bn)}bn.textContent=wc}else if(bn)bn.remove();
    if(pendingLog&&loaded()){var s=secOf(lecOf(state.lec),pendingLog);if(s&&(secStat(s).complete||state.done[s.id]))logToday(s.id)}pendingLog=null;
    if(loaded())progCache();
    var m=document.getElementById("main");
    /* ข้อสอบหลังอ่านจบ */
    if(state.view==="section"&&loaded()){var s2=secOf(lecOf(state.lec),state.sec),qz=m.querySelector(".quiz");
      if(s2&&qz&&s2.items.length&&!secStat(s2).answered&&!GATE[s2.id]&&!lecHidden(lecOf(state.lec))){
        [].forEach.call(qz.children,function(c){if(!c.classList.contains("nav")){c.hidden=true;c.setAttribute("data-trhid","1")}});
        var g=el("div","tr-gate","<div><b>อ่านจบแล้ว ลองตอบ "+s2.items.length+" ข้อของหัวข้อนี้</b><span>ข้อสอบจะขึ้นต่อด้านล่าง ตอบแล้วเฉลยพร้อมคำอธิบายทันที</span></div>");
        var gb=el("button","btn press","ทำข้อสอบท้ายหัวข้อ");gb.type="button";gb.dataset.trgate=s2.id;g.appendChild(gb);qz.insertBefore(g,qz.firstChild)}}
    /* ฝึกเขียน: สลับ MEQ / OSCE */
    if((state.view==="meq"||state.view==="osce")&&!state.pid&&m.firstElementChild){var sg=el("div","tr-seg");
      [["meq","MEQ"],["osce","OSCE / SAQ"]].forEach(function(x){var b=el("button",null,x[1]);b.type="button";b.dataset.tab=x[0];b.setAttribute("aria-pressed",state.view===x[0]?"true":"false");sg.appendChild(b)});
      m.insertBefore(sg,m.firstChild)}
    if(state.view==="section"||state.view==="lecture"){if(TR.dir){var c=m.firstElementChild;if(c&&!RM){c.classList.add(TR.dir>0?"tr-slide-l":"tr-slide-r")}}}
    TR.dir=0;
    if(DESK.matches)renderSide();
    renderDock();
  }
  DESK.addEventListener&&DESK.addEventListener("change",function(){renderSide();renderDock()});
  WIDE.addEventListener&&WIDE.addEventListener("change",renderDock);
  return {after:after,home:viewHomeTR,dir:0,openWheel:openWheel,openMenu:openMenu,openPal:openPal,openLecSheet:openLecSheet,logToday:logToday,toast:toast};
})();
viewHome=TR.home;
var renderBase=render;
render=function(){renderBase();try{TR.after()}catch(e){if(window.console)console.error(e)}};
