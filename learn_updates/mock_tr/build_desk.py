# -*- coding: utf-8 -*-
s=open('mock/mock_src.html',encoding='utf-8').read()
css=open('mock/desk_part.css',encoding='utf-8').read()
js=open('mock/desk_part.js',encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
rep("@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}",
    ".hero-row2{display:grid;gap:16px}\n"+css+"\n@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}")
rep('<span class="sync"><i></i>บันทึกในบัญชี</span>',
    '<span class="sync"><i></i>บันทึกในบัญชี</span>\n    <div class="top-r desk-only"><button class="search press" id="searchBtn" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg><span>ค้นหาหัวข้อทุกวิชา</span><kbd>Ctrl K</kbd></button><div class="exam" title="สอบลงกอง 17–18 พ.ย."><b>อีก 8 วัน</b><small>สอบลงกอง 17 พ.ย.</small></div></div>')
rep('WR=wr;document.querySelectorAll(".bn .n").forEach(function(n){n.textContent=wr;n.hidden=!wr});',
    'WR=wr;document.querySelectorAll(".bn .n").forEach(function(n){n.textContent=wr;n.hidden=!wr});\n  if(side){renderSide();renderDock()}')
rep('  wrap.appendChild(hero);\n','  var hr2=el("div","hero-row2");hr2.appendChild(hero);hr2.appendChild(weekCard());wrap.appendChild(hr2);\n')
rep('''  wrap.appendChild(tl);''','''  var nlt=el("button","tile press desk-only","<small>รหัส นล. ที่ครอบคลุม</small><b>"+(DATA.nlCount[cur]||"—")+"</b>");nlt.type="button";nlt.addEventListener("click",function(){toast("ในเว็บจริง: เปิดกล่อง นล. ของแต่ละคาบ")});tl.appendChild(nlt);
  wrap.appendChild(tl);
  if(cur==="hemonc")wrap.appendChild(studyCard());''')
# วงล้อทางลัดบนคอม: วางกลางพื้นที่เนื้อหา
rep('function place(){var nb=nav.getBoundingClientRect().top;cx=window.innerWidth/2;cy=Math.max(190,Math.min(nb-RO-36,nb/2+10));',
    'function place(){var nb=nav.getBoundingClientRect().top;cx=window.innerWidth/2;cy=Math.max(190,Math.min(nb-RO-36,nb/2+10));if(DESK.matches){var rw=matchMedia("(min-width:1400px)").matches?376:0;cx=264+(window.innerWidth-264-rw)/2;cy=window.innerHeight/2}')
WEEK=r'''
function weekCard(){var c=el("section","week desk-only");c.setAttribute("aria-label","สัปดาห์นี้");
  c.appendChild(el("h3",null,"สัปดาห์นี้"));c.appendChild(el("p",null,"ทวนติดกัน 4 วัน · รวม 22 หัวข้อ"));
  var b=el("div","bars"),d=["จ","อ","พ","พฤ","ศ","ส","อา"],v=[3,5,2,6,4,0,2],mx=6;
  d.forEach(function(x,i){var t=i===0;b.appendChild(el("div",t?"today":"","<b>"+(t?2:v[i])+"</b><i style='height:"+Math.max(6,Math.round((t?2:v[i])/mx*84))+"px'></i><span>"+x+"</span>"))});
  c.appendChild(b);return c}
'''
rep("renderChips();render(0);\n})();", WEEK+js+"\ndocument.getElementById('searchBtn').addEventListener('click',openPal);\nrenderChips();render(0);\n})();")
open('mock/mock_src2.html','w',encoding='utf-8').write(s)
d=open('mock_data2.json',encoding='utf-8').read()
open('mock/learn_mock2.html','w',encoding='utf-8').write(s.replace('__DATA__',d))
print('ok',len(s))
