"""MED422 exam room: mark stations/cases already done in the pick list, with how many times (user asked 16 Nov 2026).
Usage: python3 patch_exam_done.py <in.html> <out.html>   (apply after patch_exam_back.py)"""
import sys
p=open(sys.argv[1],encoding='utf-8').read()
def R(o,n):
    global p
    assert p.count(o)==1,(p.count(o),o[:80]); p=p.replace(o,n)
R('.wrap{max-width:1100px;margin:0 auto;padding:16px}',
  '.wrap{max-width:1100px;margin:0 auto;padding:16px}\n'
  '/* ทำแล้วกี่ครั้ง ในรายการเลือกสถานี (ผู้ใช้ขอ 16 พ.ย.) */\n'
  '.setrow.done .d{color:var(--green)}\n'
  '.donec{display:inline-flex;align-items:center;gap:4px;font-size:.78rem;font-weight:600;line-height:1.3;color:var(--green);background:rgba(52,168,83,.12);border:1px solid rgba(52,168,83,.35);border-radius:999px;padding:2px 10px;margin:2px 0;white-space:nowrap}\n'
  '.donec.no{color:var(--muted);background:transparent;border-color:var(--edge);font-weight:500}')
R('function renderPick(set){\n',
  'function doneMap(set){ // key → {n: ครั้งที่ทำ, last: วันที่ล่าสุด} นับเฉพาะครั้งที่มีคำตอบหรือคะแนนจริง\n'
  '  const m={},has=v=>v!=null&&JSON.stringify(v)!=="{}"&&JSON.stringify(v)!=="[]"&&v!=="";\n'
  '  ATT.filter(a=>a.setId===set.id).forEach(a=>{const seen={};\n'
  '    Object.keys(Object.assign({},a.ans||{},a.grade||{})).forEach(k=>{\n'
  '      if(!has((a.ans||{})[k])&&!has((a.grade||{})[k]))return;\n'
  '      const u=k.startsWith("m")?k.replace(/p\\d+$/,""):k;if(seen[u])return;seen[u]=1;\n'
  '      const r=m[u]||(m[u]={n:0,last:""});r.n++;const t=a.finishedAt||a.startedAt||"";if(t>r.last)r.last=t;});});\n'
  '  return m;\n'
  '}\n'
  'function doneChip(r){if(!r)return `<span class="donec no">ยังไม่เคยทำ</span>`;\n'
  '  const d=r.last?new Date(r.last).toLocaleDateString("th-TH",{day:"numeric",month:"short",timeZone:"Asia/Bangkok"}):"";\n'
  '  return `<span class="donec" title="ทำแล้ว ${r.n} ครั้ง${d?" · ล่าสุด "+d:""}">✓ ทำแล้ว ${r.n} ครั้ง${d?" · "+d:""}</span>`}\n'
  'function renderPick(set){\n')
R('''   <div class="sets">${set.stations.map(st=>`<div class="setrow glass"><div class="d"><b>${st.n}</b>${set.bank?"ข้อ":"สถานี"}</div>
     <div><h3>${esc(st.title)}</h3>''',
  '''   <div class="sets">${set.stations.map(st=>`<div class="setrow glass${DM["s"+st.n]?" done":""}"><div class="d"><b>${DM["s"+st.n]?"✓ ":""}${st.n}</b>${set.bank?"ข้อ":"สถานี"}</div>
     <div><h3>${esc(st.title)}</h3>${doneChip(DM["s"+st.n])} ''')
R('''   ${set.meq.map((c,i)=>`<div class="setrow glass"><div class="d"><b>M${i+1}</b>MEQ</div><div><h3>${esc(c.title)}</h3>''',
  '''   ${set.meq.map((c,i)=>`<div class="setrow glass${DM["m"+i]?" done":""}"><div class="d"><b>${DM["m"+i]?"✓ ":""}M${i+1}</b>MEQ</div><div><h3>${esc(c.title)}</h3>${doneChip(DM["m"+i])} ''')
R('enterView({k:"pick",sid:set.id});\n  $("#app").innerHTML=`<h2',
  'enterView({k:"pick",sid:set.id});const DM=doneMap(set);\n  $("#app").innerHTML=`<h2')
open(sys.argv[2],'w',encoding='utf-8').write(p);print("ok")
