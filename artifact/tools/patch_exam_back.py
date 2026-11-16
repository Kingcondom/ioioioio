"""MED422 exam room: the exit button goes back to the screen you came from (user asked 16 Nov 2026).
Usage: python3 patch_exam_back.py <in.html> <out.html>   (apply after patch_exam_jitter.py)"""
import sys
p=open(sys.argv[1],encoding='utf-8').read()
def R(o,n):
    global p
    assert p.count(o)==1,(p.count(o),o[:80]); p=p.replace(o,n)
# view history: CUR = the screen on show, PREV = where the exit button goes back to
R('function renderHome(tab="home"){\n  run=null; stopClock(); chrome(false); $("#clock").hidden=true; $("#homeBtn").hidden=true; TAB=tab;',
  '/* ปุ่ม "ออกจากห้องสอบ" กลับไปหน้าก่อนหน้า (ผู้ใช้ขอ 16 พ.ย.) — CUR คือหน้าที่เปิดอยู่ PREV คือทางกลับ */\n'
  'let CUR={k:"tab",tab:"home"},PREV=[];\n'
  'function enterView(v){if(CUR&&!(CUR.k===v.k&&CUR.sid===v.sid&&CUR.pid===v.pid)){PREV.push(CUR);if(PREV.length>12)PREV.shift()}CUR=v}\n'
  'function goBack(){const v=PREV.pop();run=null;stopClock();$("#clock").hidden=true;CUR=null;\n'
  '  if(v&&v.k==="pick"){const s=getSet(v.sid);if(s)return renderPick(s)}\n'
  '  if(v&&v.k==="pat"&&PATS.some(x=>x.id===v.pid))return renderPattern(v.pid);\n'
  '  renderHome(v&&v.k==="tab"?v.tab:(TAB||"home"))}\n'
  'function renderHome(tab="home"){\n  run=null; stopClock(); chrome(false); $("#clock").hidden=true; $("#homeBtn").hidden=true; TAB=tab;CUR={k:"tab",tab};PREV=[];')
R('chrome(true);run=null;$("#homeBtn").hidden=false;$("#clock").hidden=true;$("#where").textContent="แพทเทิร์น · "+P.title;',
  'chrome(true);run=null;$("#homeBtn").hidden=false;$("#clock").hidden=true;$("#where").textContent="แพทเทิร์น · "+P.title;enterView({k:"pat",pid});')
R('  run={set,mode,only,queue:buildQueue(set,mode,only),idx:0,ans:{},chat:{},grade:{},started:new Date().toISOString(),strict:true};\n  $("#homeBtn").hidden=false;',
  '  run={set,mode,only,queue:buildQueue(set,mode,only),idx:0,ans:{},chat:{},grade:{},started:new Date().toISOString(),strict:true};\n  enterView({k:"run"});$("#homeBtn").hidden=false;')
R('chrome(true);$("#where").textContent=set.title;$("#homeBtn").hidden=false;',
  'run=null;stopClock();$("#clock").hidden=true;chrome(true);$("#where").textContent=set.title;$("#homeBtn").hidden=false;enterView({k:"pick",sid:set.id});')
R('b.onclick=()=>{bell(0);run={set,mode:"meq",',
  'b.onclick=()=>{bell(0);enterView({k:"run"});run={set,mode:"meq",')
R('$("#homeBtn").onclick=()=>{ if(run&&!run.finished&&!confirmLeave())return; renderHome(); };',
  '$("#homeBtn").onclick=()=>{ if(run&&!run.finished&&!confirmLeave())return; goBack(); };')
open(sys.argv[2],'w',encoding='utf-8').write(p);print("ok")
