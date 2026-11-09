
/* ===================== เวอร์ชันคอม: แถบซ้าย · การ์ดเรียนต่อพร้อมฟังก์ชันของ learn · แถบขวา · ค้นหา Ctrl K ===================== */
var DESK=matchMedia("(min-width:1100px)");
var SV='<svg viewBox="0 0 24 24" aria-hidden="true">';
var PINS=[{t:"Hb Bart's (γ₄)",b:"O₂ affinity สูง ปล่อย O₂ ไม่ได้",r:"-2deg"},{t:"Retic",b:"RPI ≥ 2 = แตก/เสีย",r:"1.5deg"}];
function grs(s){try{return Array.from(new Intl.Segmenter("th",{granularity:"grapheme"}).segment(s),function(x){return x.segment})}catch(e){return Array.from(s)}}
function inl(t){return esc(t).replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>")}
function segs(h){return h.split(/\s·\s/).filter(Boolean)}
function mdr(src){
  var L=String(src||"").split("\n"),o=[],i=0,para=[];
  function fp(){if(para.length){o.push("<p>"+para.map(function(x){return segs(inl(x)).join("<br>")}).join("<br>")+"</p>");para=[]}}
  while(i<L.length){var l=L[i];
    if(/^###\s+/.test(l)){fp();o.push("<h3>"+inl(l.replace(/^###\s+/,""))+"</h3>");i++;continue}
    if(/^\s*\|/.test(l)){fp();var rows=[];while(i<L.length&&/^\s*\|/.test(L[i])){rows.push(L[i]);i++}
      var cells=rows.map(function(r){return r.trim().replace(/^\||\|$/g,"").split("|").map(function(c){return c.trim()})});
      var head=cells[0],body=cells.slice(cells[1]&&/^:?-{2,}/.test(cells[1][0])?2:1);
      o.push("<div class='tbar'><button class='btn press' data-tq>ปิดเพื่อทวน</button><button class='btn press' data-pin='t'>ปักตารางใน Post-it</button></div>"+
        "<div class='twrap'><table><thead><tr>"+head.map(function(c){return "<th>"+inl(c)+"</th>"}).join("")+"</tr></thead><tbody>"+
        body.map(function(r){return "<tr>"+r.map(function(c){var s=segs(inl(c));return "<td>"+(s.length>1?s.map(function(x){return "<span class='seg'>"+x+"</span>"}).join(""):(s[0]||""))+"</td>"}).join("")+"</tr>"}).join("")+"</tbody></table></div>");continue}
    if(/^\s*>\s?/.test(l)){fp();var q=[];while(i<L.length&&/^\s*>\s?/.test(L[i])){q.push(L[i].replace(/^\s*>\s?/,""));i++}o.push("<div class='callout'>"+mdr(q.join("\n"))+"</div>");continue}
    if(/^\s*[-•]\s+/.test(l)){fp();var it=[];while(i<L.length&&/^\s*[-•]\s+/.test(L[i])){it.push("<li>"+segs(inl(L[i].replace(/^\s*[-•]\s+/,""))).join("<br>")+"</li>");i++}o.push("<ul>"+it.join("")+"</ul>");continue}
    if(/^\s*\d+[.)]\s+/.test(l)){fp();var it2=[];while(i<L.length&&/^\s*\d+[.)]\s+/.test(L[i])){it2.push("<li>"+inl(L[i].replace(/^\s*\d+[.)]\s+/,""))+"</li>");i++}o.push("<ol>"+it2.join("")+"</ol>");continue}
    if(!l.trim()){fp();i++;continue}
    para.push(l.trim());i++}
  fp();return o.join("")}

/* ---------- แถบซ้าย ---------- */
var side=el("aside","side");side.setAttribute("aria-label","เมนูหลัก");document.body.appendChild(side);
function renderSide(){
  side.innerHTML="";
  side.appendChild(el("div","sd-brand","<b>MED421 learn</b><span>Internal medicine</span>"));
  var plus=el("button","sd-plus press",SV+'<path d="M12 5v14M5 12h14"/></svg>ทางลัด');plus.type="button";plus.addEventListener("click",function(){openMenu(null)});side.appendChild(plus);
  var nv=el("nav","sd-nav");
  [["home","หน้าแรก",I.home],["lec","คาบเรียน",I.lec],["write","ฝึกเขียน",I.write],["review","ทบทวนข้อที่ผิด",I.review],["pin","Post-it ห้ามลืม",IC.pin]].forEach(function(x){
    var b=el("button","press",x[2]+"<span>"+x[1]+"</span>");b.type="button";if(x[0]==="home")b.setAttribute("aria-current","page");
    if(x[0]==="review"&&WR)b.appendChild(el("span","n",String(WR)));
    b.addEventListener("click",function(){toast(x[0]==="home"?"หน้าแรก":"ในเว็บจริง: เปิด "+x[1])});nv.appendChild(b)});
  side.appendChild(nv);
  side.appendChild(el("div","sd-h","ชุดวิชา"));
  var cs=el("div","sd-courses");
  DATA.courses.forEach(function(c){
    var L=DATA.lec[c.set],all=0,ok=0;(L||[]).forEach(function(l){l.secs.forEach(function(s){all++;if(st(s)==="ok")ok++})});
    var p=all?ok/all:(h(c.set)%60)/100;
    var b=el("button","sd-c press","<span class='mr' style='--p:"+p.toFixed(2)+"'></span><b>"+esc(c.label)+"<small>"+esc(c.thai)+"</small></b><em>"+Math.round(p*100)+"%</em>");b.type="button";
    if(c.set===cur)b.setAttribute("aria-current","true");
    b.addEventListener("click",function(){go(c.set)});cs.appendChild(b)});
  side.appendChild(cs);
  var ft=el("div","sd-foot");ft.appendChild(el("span","sync","<i></i>บันทึกในบัญชี"));
  var th=el("button","btn press",IC.theme.replace('aria-hidden="true"','aria-hidden="true" style="width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8"')+"โหมดสี");th.type="button";th.addEventListener("click",function(){act("theme")});ft.appendChild(th);
  side.appendChild(ft);
}

/* ---------- แถบขวา: ถาม AI · ข้อที่ผิด · Post-it · คีย์ลัด ---------- */
var dock=el("aside","dock");dock.setAttribute("aria-label","เครื่องมือข้างจอ");document.body.appendChild(dock);
var AIQ="",AILOG=[];
function renderDock(){
  dock.innerHTML="";
  var ai=el("section","dk");
  ai.appendChild(el("div","dk-h","<h3 class='ai-h'>ถาม AI</h3><small>Claude จากบัญชีคุณ</small>"));
  ai.appendChild(el("div","ai-ctx","อิงหัวข้อ: "+esc(DATA.pv.title)));
  var log=el("div","ai-log");
  if(!AILOG.length)log.appendChild(el("div","ai-m ai","ลากคลุมข้อความในบทเรียนแล้วกด <b>ถาม AI ↗</b> หรือพิมพ์ถามได้เลย"));
  AILOG.forEach(function(m){log.appendChild(el("div","ai-m "+m.r,(m.q?"<div class='ai-q'>"+esc(m.q)+"</div>":"")+esc(m.t)))});
  ai.appendChild(log);
  var ch=el("div","ai-chips");["อธิบายง่าย ๆ","ทำไม (กลไก)","เคสข้อสอบ","วิธีจำ"].forEach(function(t){var b=el("button","press",t);b.type="button";b.addEventListener("click",function(){ask(t)});ch.appendChild(b)});ai.appendChild(ch);
  var f=el("form","ai-form");var ta=el("textarea");ta.rows=1;ta.placeholder=AIQ?"ถามเรื่องข้อความที่เลือก…":"พิมพ์คำถาม…";f.appendChild(ta);
  var sb=el("button","press","ส่ง");sb.type="submit";f.appendChild(sb);
  f.addEventListener("submit",function(e){e.preventDefault();if(ta.value.trim())ask(ta.value.trim())});
  ta.addEventListener("keydown",function(e){if(e.key==="Enter"&&!e.shiftKey&&!e.isComposing){e.preventDefault();f.requestSubmit()}});
  ai.appendChild(f);dock.appendChild(ai);
  setTimeout(function(){log.scrollTop=log.scrollHeight},0);

  var w=el("section","dk");w.appendChild(el("div","dk-h","<h3>ข้อที่ผิดล่าสุด</h3><small>"+WR+" ข้อรอทวน</small>"));
  var ul=el("ul","wl");
  (DATA.lec[cur]||DATA.lec.hemonc).reduce(function(a,l){return a.concat(l.secs.filter(function(s){return wrong(s)}).map(function(s){return {l:l,s:s}}))},[]).slice(0,3).forEach(function(x){
    var li=el("li");li.appendChild(el("span",null,"<small>ผิด "+wrong(x.s)+" ข้อ · คาบ "+esc(x.l.lec)+"</small>"+esc(x.s.t)));
    var b=el("button","btn press","ทำใหม่");b.type="button";b.addEventListener("click",function(){toast("ในเว็บจริง: ล้างคำตอบแล้วทำข้อนี้ใหม่")});li.appendChild(b);ul.appendChild(li)});
  w.appendChild(ul);dock.appendChild(w);

  var pn=el("section","dk");pn.appendChild(el("div","dk-h","<h3>Post-it ที่ปักไว้</h3><small>"+PINS.length+" ใบ</small>"));
  var nb=el("div","notes");PINS.slice(-4).reverse().forEach(function(p,i){var n=el("div","pn"+(p.fresh?" new":""),"<b>"+esc(p.t)+"</b>"+esc(p.b));n.style.setProperty("--r",p.r||"0deg");p.fresh=false;nb.appendChild(n)});
  pn.appendChild(nb);dock.appendChild(pn);

  var k=el("section","dk");k.appendChild(el("div","dk-h","<h3>คีย์ลัด</h3>"));
  var kl=el("ul","keys");[["ค้นหาหัวข้อทุกวิชา","Ctrl K"],["ตอบข้อสอบ (หลังอ่านจบ)","1–5"],["เปลี่ยนชุดวิชา","Alt ← →"],["หมุนเลือกคาบ","ดับเบิลคลิก"],["โหมดพรีเซนต์","P"]].forEach(function(x){kl.appendChild(el("li",null,"<span>"+x[0]+"</span><span class='kbd'>"+x[1]+"</span>"))});
  k.appendChild(kl);dock.appendChild(k);
}
function ask(t){
  AILOG.push({r:"me",t:t,q:AIQ});AIQ="";
  AILOG.push({r:"ai",t:"(ร่าง) ในเว็บจริง Claude จะตอบเรื่องนี้โดยอิงเนื้อหาหัวข้อ \""+DATA.pv.title.slice(0,40)+"…\" ที่เปิดอยู่"});
  renderDock()}

/* ---------- การ์ด "เรียนต่อ" พร้อมฟังก์ชันของ learn ---------- */
var ANS={},QOPEN=false;
function studyCard(){
  var P=DATA.pv,c=el("section","study");c.setAttribute("aria-label","เรียนต่อจากที่ค้าง");
  var hd=el("div","st-head");
  hd.appendChild(el("div","st-ht","<small>เรียนต่อ · คาบ "+esc(P.lec)+" · อ่าน ~"+P.minutes+" นาที</small><h3>"+esc(P.title)+"</h3>"));
  var ac=el("div","st-acts");
  [["โหมดทวน","hide"],["▶ พรีเซนต์","pres"],["ปักหัวข้อใน Post-it","pinsec"]].forEach(function(x){var b=el("button","btn press",x[0]);b.type="button";
    b.addEventListener("click",function(){if(x[1]==="pinsec"){addPin(P.title.split("—")[0].trim(),"หัวข้อ · คาบ "+P.lec)}else toast(x[1]==="pres"?"ในเว็บจริง: เปิดโหมดพรีเซนต์ตั้งแต่หัวข้อนี้":"ในเว็บจริง: ซ่อนเนื้อหา เหลือหัวข้อให้นึกเอง")});ac.appendChild(b)});
  hd.appendChild(ac);c.appendChild(hd);
  var meta=el("div","st-meta");P.nl.slice(0,4).forEach(function(k){meta.appendChild(el("span","nl","นล. "+esc(k)+(DATA.nlTitles[k]?" · "+esc(DATA.nlTitles[k]):"")))});
  if(P.nl.length>4)meta.appendChild(el("span","tag","อีก "+(P.nl.length-4)+" รหัส"));c.appendChild(meta);
  var body=el("div","st-body");
  var left=el("div");var pr=el("div","prose",mdr(P.md));left.appendChild(pr);
  if(P.more)left.appendChild(el("p","hint","อีก "+P.more+" หัวข้อย่อยในบทเรียนเต็ม"));
  (P.mnem||[]).forEach(function(m){var mn=el("div","mn");
    var mh=el("div","mn-h","<div><small>หลักจำ</small><b>"+esc(m.name)+"</b></div>");var pb=el("button","btn press","ปักใน Post-it");pb.type="button";pb.addEventListener("click",function(){addPin(m.name,m.what)});mh.appendChild(pb);mn.appendChild(mh);
    mn.appendChild(el("ul",null,(m.lines||[]).map(function(r){return "<li><b>"+esc(r[0])+"</b><span>"+inl(r[1])+"</span></li>"}).join("")));
    if(m.note)mn.appendChild(el("p",null,inl(m.note)));left.appendChild(mn)});
  body.appendChild(left);
  var n=P.items.length,gate=el("div","gate");gate.innerHTML="<div><b>อ่านจบแล้ว ลองตอบ "+n+" ข้อของหัวข้อนี้</b><span>ข้อสอบจะขึ้นต่อด้านล่าง ตอบแล้วเฉลยพร้อมคำอธิบายทันที</span></div>";
  var gb=el("button","btn primary press","ทำข้อสอบท้ายหัวข้อ");gb.type="button";gate.appendChild(gb);left.appendChild(gate);
  var qz=el("div","quiz");qz.hidden=true;qz.appendChild(el("div","q-head","<h4>เช็คความเข้าใจ</h4><small>"+n+" ข้อ · กดเลข 1–5 เพื่อตอบ</small>"));
  gb.addEventListener("click",function(){gate.hidden=true;qz.hidden=false;QOPEN=true;qz.classList.add("in");
    setTimeout(function(){try{qz.scrollIntoView({block:"start",behavior:RM?"auto":"smooth"})}catch(_){}},40)});
  P.items.forEach(function(it,qi){var q=el("div","qz");q.dataset.qi=qi;renderQ(q,it,qi);qz.appendChild(q)});
  body.appendChild(qz);c.appendChild(body);
  var ft=el("div","st-foot");ft.appendChild(el("span","hint","ตอบครบทุกข้อแล้วหัวข้อนี้จะนับว่าเรียนจบ"));
  var nx=el("button","btn press","เปิดบทเรียนเต็มหัวข้อนี้");nx.type="button";nx.addEventListener("click",function(){toast("ในเว็บจริง: เปิดหน้าหัวข้อเต็ม")});ft.appendChild(nx);c.appendChild(ft);
  c.addEventListener("click",function(e){
    var b=e.target.closest&&e.target.closest("button");if(!b)return;
    if(b.hasAttribute("data-tq")){var tw=b.parentNode.nextElementSibling,on=!tw.classList.contains("cov");tw.classList.toggle("cov",on);
      tw.querySelectorAll("td+td").forEach(function(td){td.classList.remove("op");td.dataset.h=grs(td.textContent.trim()).slice(0,2).join("")+"…"});b.textContent=on?"เลิกปิด":"ปิดเพื่อทวน";return}
    if(b.getAttribute("data-pin")==="t"){var t2=b.parentNode.nextElementSibling,hh=t2.previousElementSibling.previousElementSibling;var ttl=(hh&&hh.tagName==="H3"?hh.textContent:"ตาราง");
      addPin(ttl,t2.querySelectorAll("tbody tr").length+" แถว · แถวละใบ");return}
  });
  c.addEventListener("click",function(e){var td=e.target.closest&&e.target.closest(".twrap.cov td+td");if(td)td.classList.toggle("op")});
  /* ลากคลุมข้อความแล้วถาม AI */
  pr.addEventListener("mouseup",function(){setTimeout(function(){var s=window.getSelection(),t=s&&String(s).trim();
    if(!t||t.length<2){selask.classList.remove("on");return}var r=s.getRangeAt(0).getBoundingClientRect();
    selask.style.left=(r.right+window.scrollX-60)+"px";selask.style.top=(r.bottom+window.scrollY+8)+"px";selask.classList.add("on");selask._t=t},10)});
  return c}
function renderQ(q,it,qi){
  var a=ANS[it.id];q.innerHTML="";
  q.appendChild(el("small",null,"ข้อ "+(qi+1)+" · "+esc(it.topic||"")));
  q.appendChild(el("div","stem",inl(it.stem)));
  it.choices.forEach(function(ch,i){var b=el("button","ch press","<span class='k'>"+"ABCDE"[i]+"</span><span>"+inl(ch)+"</span>");b.type="button";
    if(a!=null){b.disabled=true;if(i===it.answer)b.classList.add("right");else if(i===a)b.classList.add("wrong")}
    b.addEventListener("click",function(){answer(qi,i)});q.appendChild(b)});
  if(a!=null){var ok=a===it.answer;q.appendChild(el("div","ver "+(ok?"ok":"no"),ok?"✓ ถูกต้อง":"✗ ยังไม่ใช่ — เฉลยคือข้อ "+"ABCDE"[it.answer]));
    q.appendChild(el("div","ex prose",mdr(it.explain)));if(it.pearl)q.appendChild(el("div","pearl","<b>Pearl · </b>"+inl(it.pearl)))}
  else q.appendChild(el("div","kh","กดเลข 1–5 บนคีย์บอร์ดเพื่อตอบได้"))}
function answer(qi,i){var it=DATA.pv.items[qi];if(ANS[it.id]!=null)return;ANS[it.id]=i;var q=document.querySelector('.qz[data-qi="'+qi+'"]');if(q){renderQ(q,it,qi);pop(q)}}
function addPin(t,b){PINS.push({t:t,b:b,r:(Math.random()*4-2).toFixed(1)+"deg",fresh:true});renderDock();toast("ปักลง Post-it แล้ว")}
var selask=el("button","selask","ถาม AI ↗");selask.type="button";document.body.appendChild(selask);
selask.addEventListener("mousedown",function(e){e.preventDefault()});
selask.addEventListener("click",function(){AIQ=selask._t||"";selask.classList.remove("on");try{window.getSelection().removeAllRanges()}catch(_){}
  if(!matchMedia("(min-width:1400px)").matches){toast("ในเว็บจริง: เปิดแชตถาม AI พร้อมข้อความที่เลือก");return}
  AILOG.push({r:"me",t:"อธิบายตรงนี้ให้เข้าใจง่าย ๆ",q:AIQ});AILOG.push({r:"ai",t:"(ร่าง) ในเว็บจริง Claude จะอธิบายข้อความที่เลือกในบริบทของหัวข้อนี้"});AIQ="";renderDock()});
document.addEventListener("mousedown",function(e){if(e.target!==selask)selask.classList.remove("on")});

/* ---------- ค้นหาหัวข้อทุกวิชา (Ctrl K) ---------- */
var PAL=null;
function openPal(){
  if(PAL)return;var idx=[];
  Object.keys(DATA.lec).forEach(function(set){var c=DATA.courses.filter(function(x){return x.set===set})[0];
    DATA.lec[set].forEach(function(l){idx.push({k:"คาบ",c:c.label,t:l.title,s:"คาบ "+l.lec,set:set,l:l});l.secs.forEach(function(s){idx.push({k:"หัวข้อ",c:c.label,t:s.t,s:"คาบ "+l.lec+" · "+l.title,set:set,l:l})})})});
  var ov=el("div","pal"),box=el("div","pal-box");ov.appendChild(box);ov.setAttribute("role","dialog");ov.setAttribute("aria-modal","true");ov.setAttribute("aria-label","ค้นหาหัวข้อ");
  var iw=el("div","pal-in",SV+'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>');var inp=el("input");inp.placeholder="ค้นหาหัวข้อ คาบ หรือคำสำคัญ เช่น retic, thalassemia, gout";inp.setAttribute("aria-label","ค้นหา");iw.appendChild(inp);box.appendChild(iw);
  var ul=el("ul","pal-list");ul.setAttribute("role","listbox");box.appendChild(ul);
  box.appendChild(el("div","pal-foot","<span><span class='kbd'>↑ ↓</span> เลือก</span><span><span class='kbd'>Enter</span> เปิด</span><span><span class='kbd'>Esc</span> ปิด</span><span>ร่างนี้ค้นได้ในชุด Heme/Onc และ AIR</span>"));
  document.body.appendChild(ov);var sel=0,res=[];
  function hl(t,q){if(!q)return esc(t);var i=t.toLowerCase().indexOf(q.toLowerCase());return i<0?esc(t):esc(t.slice(0,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length))}
  function draw(){var q=inp.value.trim();res=(q?idx.filter(function(x){return (x.t+" "+x.s).toLowerCase().indexOf(q.toLowerCase())>=0}):idx.filter(function(x){return x.k==="คาบ"})).slice(0,8);
    sel=Math.min(sel,Math.max(0,res.length-1));ul.innerHTML="";
    if(!res.length){ul.appendChild(el("li","pal-empty","ไม่พบ ลองคำอื่น"));return}
    res.forEach(function(x,i){var li=el("li"),b=el("button",i===sel?"on":"","<span class='pc'>"+esc(x.c)+" · "+x.k+"</span><span class='pt'>"+hl(x.t,q)+"<small>"+esc(x.s)+"</small></span><span class='kbd'>↵</span>");b.type="button";b.setAttribute("role","option");
      b.addEventListener("mousemove",function(){if(sel!==i){sel=i;draw()}});b.addEventListener("click",function(){choose(i)});li.appendChild(b);ul.appendChild(li)})}
  function choose(i){var x=res[i];if(!x)return;close();if(x.set!==cur)go(x.set);setTimeout(function(){openLec(x.l)},x.set!==cur?300:0)}
  function close(){if(!PAL)return;PAL=null;ov.remove()}
  inp.addEventListener("input",function(){sel=0;draw()});
  inp.addEventListener("keydown",function(e){if(e.key==="ArrowDown"){e.preventDefault();sel=Math.min(res.length-1,sel+1);draw()}else if(e.key==="ArrowUp"){e.preventDefault();sel=Math.max(0,sel-1);draw()}else if(e.key==="Enter"){e.preventDefault();choose(sel)}else if(e.key==="Escape"){e.preventDefault();close()}});
  ov.addEventListener("mousedown",function(e){if(e.target===ov)close()});
  PAL={close:close};draw();inp.focus()}
document.addEventListener("keydown",function(e){
  var tg=e.target&&e.target.tagName;if(tg==="INPUT"||tg==="TEXTAREA")return;
  if((e.ctrlKey||e.metaKey)&&(e.key==="k"||e.key==="K")){e.preventDefault();openPal();return}
  if(e.key==="/"&&DESK.matches){e.preventDefault();openPal();return}
  if(PAL||W||M||sh.open)return;
  if(DESK.matches&&QOPEN&&/^[1-5]$/.test(e.key)){var its=DATA.pv.items;for(var q=0;q<its.length;q++){if(ANS[its[q].id]==null){answer(q,+e.key-1);break}}return}
  if(DESK.matches&&(e.key==="p"||e.key==="P")&&!e.ctrlKey&&!e.metaKey){toast("ในเว็บจริง: เปิดโหมดพรีเซนต์")}
});
