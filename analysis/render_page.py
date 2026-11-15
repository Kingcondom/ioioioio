"""สร้างหน้า analysis/old_themes.html จาก analysis/old_themes.json (รัน old_themes.py ก่อน)"""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(ROOT, 'old_themes.json')))
html = r'''<title>แก่นโพย MED421</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* layout: คอลัมน์เดียวอ่านบนมือถือ — สรุปตัวเลข → กราฟรายรุ่น → หลุดโพยรายรุ่น → แก่นทั้งหมด */
:root{
  --p-ink:#1f2a37;--p-paper:#f6f8fb;--p-card:#ffffff;--p-teal:#0f766e;--p-teal-soft:#99d5cd;--p-amber:#c2410c;--p-line:#dfe5ee;--p-mute:#5b6676;
  --bg:var(--p-paper);--surface:var(--p-card);--ink:var(--p-ink);--muted:var(--p-mute);--line:var(--p-line);
  --accent:var(--p-teal);--accent-soft:var(--p-teal-soft);--new:var(--p-amber);--rep:#5b7fa6;--chip:#eef2f7;
  --f:"IBM Plex Sans Thai","Noto Sans Thai",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;
  --s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-5:24px;--s-6:32px;--s-7:48px;--r-sm:6px;--r-md:10px;--r-lg:16px;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11161d;--surface:#1a212b;--ink:#e6ebf2;--muted:#9aa6b6;--line:#2c3644;--accent:#3fb8a9;--accent-soft:#2a6f68;--new:#f08a4b;--rep:#7d9cc4;--chip:#232c38;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11161d;--surface:#1a212b;--ink:#e6ebf2;--muted:#9aa6b6;--line:#2c3644;--accent:#3fb8a9;--accent-soft:#2a6f68;--new:#f08a4b;--rep:#7d9cc4;--chip:#232c38;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font:400 16px/1.65 var(--f)}
.wrap{max-width:860px;margin:0 auto;grid-template-columns:minmax(0,1fr);padding-block:var(--s-5) var(--s-7);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:var(--s-5)}
h1{font-size:30px;line-height:1.3;font-weight:600;margin:0;text-wrap:balance}
h2{font-size:24px;line-height:1.35;font-weight:600;margin:0;text-wrap:balance}
h3{font-size:18px;line-height:1.45;font-weight:600;margin:0}
p{margin:0;text-wrap:pretty}
.sub{color:var(--muted);font-size:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:var(--s-4);display:grid;gap:var(--s-3)}
@media(min-width:700px){.card{padding:var(--s-5)}}
.num{font-family:var(--mono);font-variant-numeric:tabular-nums}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:var(--s-3)}
.stat{display:grid;gap:var(--s-1)}
.stat b{font:500 24px/1.35 var(--mono)}
.stat span{font-size:14px;color:var(--muted)}
ol{margin:0;padding-left:1.4em;display:grid;gap:var(--s-2)}
.legend{display:flex;flex-wrap:wrap;gap:var(--s-3);font-size:14px;color:var(--muted)}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.bars{display:grid;gap:var(--s-2)}
.bar{display:grid;grid-template-columns:64px 1fr 44px;gap:var(--s-2);align-items:center;font-size:14px}
.track{display:flex;height:24px;border-radius:var(--r-sm);overflow:hidden;background:var(--chip)}
.track div{height:100%;display:flex;align-items:center;justify-content:center;color:#fff;font:500 12px/1 var(--mono);min-width:0;overflow:hidden}
.seg-rep{background:var(--rep)}.seg-ang{background:var(--accent)}.seg-new{background:var(--new)}
.tabs{display:flex;flex-wrap:wrap;gap:var(--s-2)}
.tab{min-height:44px;padding:0 var(--s-4);border-radius:var(--r-md);border:1px solid var(--line);background:var(--surface);color:var(--ink);font:500 14px/1 var(--f);cursor:pointer;transition:background .15s,border-color .15s}
.tab:hover{border-color:var(--accent)}
.tab[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.tab:focus-visible,summary:focus-visible,select:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.yearhead{display:flex;flex-wrap:wrap;gap:var(--s-2) var(--s-4);font-size:14px;color:var(--muted)}
details{border-top:1px solid var(--line)}
details:first-of-type{border-top:0}
summary{cursor:pointer;padding:var(--s-3) 0;display:grid;grid-template-columns:1fr auto;gap:var(--s-2);align-items:start;list-style:none}
summary::-webkit-details-marker{display:none}
summary .t{font-weight:500}
summary .meta{display:flex;gap:var(--s-2);align-items:center;flex-wrap:wrap;justify-content:flex-end}
.badge{font:500 12px/1.5 var(--f);padding:2px 8px;border-radius:var(--r-sm);background:var(--chip);color:var(--muted);white-space:nowrap}
.badge.n{font-family:var(--mono);background:var(--accent);color:#fff}
.badge.sys{background:transparent;border:1px solid var(--line)}
.badge.newy{background:var(--new);color:#fff}
.yrs{display:flex;flex-wrap:wrap;gap:var(--s-1)}
.y{font:500 12px/1.5 var(--mono);padding:1px 6px;border-radius:var(--r-sm);background:var(--chip);color:var(--muted)}
.y.on{background:var(--accent-soft);color:var(--ink)}
.items{margin:0 0 var(--s-3);padding-left:1.4em;display:grid;gap:var(--s-3);font-size:14px}
.items li{display:grid;gap:var(--s-1)}
.items .q{overflow-wrap:anywhere}
.items .a{color:var(--accent);font-weight:500}
.items .id{font:500 12px/1.5 var(--mono);color:var(--muted)}
.controls{display:flex;flex-wrap:wrap;gap:var(--s-2)}
select,input{min-height:44px;border-radius:var(--r-md);border:1px solid var(--line);background:var(--surface);color:var(--ink);font:400 16px var(--f);padding:0 var(--s-3)}
input{flex:1 1 200px;min-width:0}
.ruler{display:grid;grid-template-columns:repeat(8,1fr);gap:2px}
.ruler span{height:8px;border-radius:2px;background:var(--chip)}
.ruler span.on{background:var(--accent)}
.note{font-size:14px;color:var(--muted)}
.empty{font-size:14px;color:var(--muted);padding:var(--s-3) 0}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="wrap">
  <header style="display:grid;gap:var(--s-2)">
    <h1>แก่นโพย MED421</h1>
    <p class="sub">คลังข้อสอบเก่าในหน้า MED421 Ward Drill <span id="nSys"></span> รวม <span class="num" id="nItems"></span> ข้อ จากโพย MED28–MED35 จัดกลุ่มตามแก่นของโจทย์ แล้วดูว่าแต่ละรุ่นมีอะไรที่ไม่เคยอยู่ในโพยรุ่นก่อน</p>
  </header>

  <section class="card">
    <div class="stats" id="stats"></div>
    <h3>สรุปสั้น</h3>
    <ol id="findings"></ol>
  </section>

  <section class="card">
    <h2>แต่ละรุ่น ออกซ้ำโพยแค่ไหน</h2>
    <div class="legend">
      <span><i class="seg-rep"></i>ข้อเดิมซ้ำ (เคยอยู่ในโพยรุ่นก่อน)</span>
      <span><i class="seg-ang"></i>แก่นเดิม แต่ถามมุมใหม่</span>
      <span><i class="seg-new"></i>หลุดโพย (แก่นไม่เคยออก)</span>
    </div>
    <div class="bars" id="bars"></div>
    <p class="note">ตัวเลขคือจำนวนข้อในคลังที่อ้างถึงรุ่นนั้น MED28–29 มีข้อในคลังน้อย ข้อของสองรุ่นนี้จึงนับเป็น "ใหม่" เกือบหมด ให้ดูแนวโน้มจาก MED30 เป็นต้นไป</p>
  </section>

  <section class="card">
    <h2>หลุดโพยในแต่ละรุ่น</h2>
    <p class="sub">แก่นที่ปรากฏครั้งแรกในรุ่นนั้น ไม่มีในโพยรุ่นก่อนหน้าเลย กดดูโจทย์ได้</p>
    <div class="tabs" id="yearTabs" role="group" aria-label="เลือกรุ่น"></div>
    <div class="yearhead" id="yearHead"></div>
    <div id="yearList"></div>
  </section>

  <section class="card">
    <h2>แก่นทั้งหมด</h2>
    <p class="sub">แถบ 8 ช่องใต้ชื่อคือ MED28 → MED35 ช่องที่เป็นสีคือรุ่นที่แก่นนั้นออก</p>
    <div class="controls">
      <select id="fSys" aria-label="ระบบ"><option value="">ทุกระบบ</option></select>
      <select id="fSort" aria-label="เรียงตาม">
        <option value="yrs">ออกหลายรุ่นก่อน</option>
        <option value="n">จำนวนข้อมากก่อน</option>
        <option value="first">ออกครั้งแรกล่าสุดก่อน</option>
      </select>
      <input id="fQ" type="search" placeholder="ค้นหาแก่นหรือโจทย์ เช่น hyperkalemia" aria-label="ค้นหา">
    </div>
    <p class="sub" id="allCount"></p>
    <div id="allList"></div>
  </section>

  <section class="card">
    <h3>ข้อควรรู้ก่อนใช้</h3>
    <ol class="note">
      <li>นับเฉพาะส่วน "คลังข้อสอบเก่า" ที่เรียบเรียงจากโพย ไม่รวม MCQ ที่แต่งใหม่และชุด mock<span id="noYear"></span></li>
      <li>ข้อที่โพยหลายรุ่นถามเรื่องเดียวกันถูกรวมเป็นข้อเดียวไว้แล้ว ปีของข้อดูจากช่อง "แหล่งที่มา" ของแต่ละข้อ</li>
      <li>โพยแต่ละรุ่นจดมาไม่ครบเท่ากัน (MED31 จดมาเยอะสุด MED28–29 น้อยสุด) รุ่นที่จดน้อยจะดูเหมือนออกซ้ำน้อย ส่วนรุ่นถัดไปจะดูเหมือนมีแก่นใหม่เยอะกว่าความจริง</li>
      <li>แก่นแบ่งตามระบบ เรื่องเดียวกันที่ถูกถามในสองระบบ (เช่น anaphylaxis ใน Cardio กับ AIR) อาจถูกนับเป็นสองแก่น</li>
      <li>การจัดแก่นเป็นดุลยพินิจ ข้อที่คาบเกี่ยวสองเรื่องถูกจัดไว้แก่นเดียวตามสิ่งที่โจทย์ถามจริง</li>
    </ol>
  </section>
</div>
<script>
const D = __DATA__;
const YEARS = D.per_year.map(p=>p.year);
const $ = id=>document.getElementById(id);
const esc = s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
$('nItems').textContent = D.n_items;
$('nSys').textContent = `${D.systems.length} ระบบ (${D.systems.join(', ')})`;

const multi = D.themes.filter(t=>t.n>=3), multiItems = multi.reduce((a,t)=>a+t.n,0);
const recur = D.themes.filter(t=>Object.keys(t.years).length>=4);
const single = D.themes.filter(t=>t.n===1).length;
if(D.no_year) $('noYear').textContent = ` มี ${D.no_year} ข้อที่โพยไม่ได้ระบุรุ่น จึงไม่อยู่ในกราฟรายรุ่น`;
$('stats').innerHTML = [
  [D.n_themes,'แก่นทั้งหมด'],
  [multi.length,`แก่นที่มี ≥3 ข้อ (${multiItems} ข้อ = ${Math.round(multiItems/D.n_items*100)}%)`],
  [recur.length,'แก่นที่ออก ≥4 รุ่น'],
  [single,'แก่นที่มีข้อเดียว'],
].map(([b,s])=>`<div class="stat"><b>${b}</b><span>${s}</span></div>`).join('');

const py = Object.fromEntries(D.per_year.map(p=>[p.year,p]));
const pct = y=>{const p=py[y];return Math.round((p.items-p.new_theme_items)/p.items*100)};
const topT = [...D.themes].sort((a,b)=>Object.keys(b.years).length-Object.keys(a.years).length||b.n-a.n).slice(0,5);
$('findings').innerHTML = [
  `โจทย์ ${D.n_items} ข้อ ยุบเหลือ ${D.n_themes} แก่น เฉลี่ยแก่นละ ${(D.n_items/D.n_themes).toFixed(1)} ข้อ แก่นที่มีตั้งแต่ 3 ข้อขึ้นไปมี ${multi.length} แก่น (${Math.round(multi.length/D.n_themes*100)}% ของแก่น)`,
  `แก่นที่ออกทนที่สุด: ${topT.map(t=>`${esc(t.theme.split(':')[0])} (${Object.keys(t.years).length} รุ่น)`).join(', ')}`,
  `ยิ่งรุ่นหลังยิ่งออกตามโพย: MED34 มี ${pct(34)}% และ MED35 มี ${pct(35)}% ของข้อที่อยู่ในแก่นที่เคยออกแล้ว`,
  `แต่ข้อเดิมเป๊ะมีไม่ถึงครึ่ง (MED35 ซ้ำข้อเดิม ${py[35].repeat_items}/${py[35].items} ข้อ = ${Math.round(py[35].repeat_items/py[35].items*100)}%) ที่เหลือส่วนใหญ่เป็นแก่นเดิมแต่ถามมุมใหม่ ต้องอ่านโพยให้เข้าใจแก่น ท่องคำตอบอย่างเดียวไม่พอ`,
  `MED35 หลุดโพยจริงแค่ ${py[35].new_themes.length} แก่น (${py[35].new_theme_items} ข้อ) ดูรายชื่อได้ในส่วน "หลุดโพยในแต่ละรุ่น"`,
].map(s=>`<li>${s}</li>`).join('');

const maxItems = Math.max(...D.per_year.map(p=>p.items));
$('bars').innerHTML = D.per_year.map(p=>{
  const seg=(v,c)=>v?`<div class="${c}" style="width:${v/p.items*100}%" title="${v}">${v>=4?v:''}</div>`:'';
  return `<div class="bar"><span class="num">MED${p.year}</span>
   <div class="track" style="width:${p.items/maxItems*100}%" role="img" aria-label="MED${p.year}: ซ้ำ ${p.repeat_items} มุมใหม่ ${p.new_angle_items} หลุดโพย ${p.new_theme_items}">
   ${seg(p.repeat_items,'seg-rep')}${seg(p.new_angle_items,'seg-ang')}${seg(p.new_theme_items,'seg-new')}</div>
   <span class="num">${p.items}</span></div>`}).join('');

function itemsHtml(list, hl){
  return `<ol class="items">${list.map(it=>`<li><span class="q">${esc(it.q)}</span><span class="a">→ ${esc(it.a)}</span>
   <span class="yrs"><span class="id">${it.id} คาบ ${it.lec}</span>${it.years.map(y=>`<span class="y${y===hl?' on':''}">MED${y}</span>`).join('')}</span></li>`).join('')}</ol>`;
}
let curYear = 35;
function renderYear(){
  const p = py[curYear];
  $('yearTabs').innerHTML = YEARS.map(y=>`<button class="tab" aria-pressed="${y===curYear}" data-y="${y}">MED${y} <span class="num">(${py[y].new_themes.length})</span></button>`).join('');
  $('yearHead').innerHTML = `<span>ข้อในคลัง <b class="num">${p.items}</b></span><span>ครอบคลุม <b class="num">${p.themes}</b> แก่น</span><span>แก่นใหม่ <b class="num">${p.new_themes.length}</b> (${p.new_theme_items} ข้อ)</span>`;
  $('yearList').innerHTML = p.new_themes.length ? p.new_themes.map(t=>`<details><summary><span class="t">${esc(t.theme)}</span><span class="meta"><span class="badge sys">${t.system}</span><span class="badge n">${t.items.length}</span></span></summary>${itemsHtml(t.items,curYear)}</details>`).join('')
    : '<p class="empty">รุ่นนี้ไม่มีแก่นใหม่</p>';
}
$('yearTabs').addEventListener('click',e=>{const b=e.target.closest('[data-y]');if(b){curYear=+b.dataset.y;renderYear()}});
renderYear();

[...new Set(D.themes.flatMap(t=>t.system.split(' + ')))].forEach(s=>$('fSys').insertAdjacentHTML('beforeend',`<option>${s}</option>`));
function renderAll(){
  const sys=$('fSys').value, q=$('fQ').value.trim().toLowerCase(), sort=$('fSort').value;
  let L = D.themes.filter(t=>(!sys||t.system.split(' + ').includes(sys))&&(!q||t.theme.toLowerCase().includes(q)||t.items.some(i=>(i.q+' '+i.a).toLowerCase().includes(q))));
  const ny=t=>Object.keys(t.years).length;
  L.sort(sort==='n'?(a,b)=>b.n-a.n||ny(b)-ny(a):sort==='first'?(a,b)=>(b.first||0)-(a.first||0)||b.n-a.n:(a,b)=>ny(b)-ny(a)||b.n-a.n);
  $('allCount').textContent = `แสดง ${L.length} แก่น ${L.reduce((a,t)=>a+t.n,0)} ข้อ`;
  $('allList').innerHTML = L.length ? L.map(t=>`<details><summary><span style="display:grid;gap:var(--s-1)"><span class="t">${esc(t.theme)}</span>
     <span class="ruler" aria-label="ออกใน ${Object.keys(t.years).map(y=>'MED'+y).join(', ')}">${YEARS.map(y=>`<span class="${t.years[y]?'on':''}" title="MED${y}"></span>`).join('')}</span></span>
     <span class="meta"><span class="badge sys">${t.system}</span><span class="badge">${ny(t)} รุ่น</span><span class="badge n">${t.n} ข้อ</span></span></summary>${itemsHtml(t.items)}</details>`).join('')
    : '<p class="empty">ไม่พบแก่นที่ตรงคำค้น ลองพิมพ์ชื่อโรคเป็นภาษาอังกฤษ หรือเลือก "ทุกระบบ"</p>';
}
['fSys','fSort','fQ'].forEach(id=>$(id).addEventListener('input',renderAll));
renderAll();
</script>
'''
open(os.path.join(ROOT, 'old_themes.html'), 'w').write(html.replace('__DATA__', json.dumps(d, ensure_ascii=False)))
print('ok')
