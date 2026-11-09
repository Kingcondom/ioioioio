# -*- coding: utf-8 -*-
"""ใส่โครงหน้าแบบ Teaching Round ลงหน้า MED421 learn: python3 apply_tr.py <in.html> <out.html>"""
import sys,os
D=os.path.dirname(os.path.abspath(__file__))
src,dst=sys.argv[1],sys.argv[2]
h=open(src,encoding='utf-8').read()
assert "var TR=(function" not in h,"already patched"
css=open(os.path.join(D,'tr.css'),encoding='utf-8').read()
js=open(os.path.join(D,'tr.js'),encoding='utf-8').read()
def rep(a,b,n=1):
    global h
    assert h.count(a)==n,(h.count(a),a[:80])
    h=h.replace(a,b)
# 1) CSS ต่อท้าย stylesheet หลัก
rep("\n</style>\n\n<svg width=\"0\"", css+"\n</style>\n\n<svg width=\"0\"")
# 2) ประวัติการทวนรายวัน: state.log ซิงก์บัญชีไปกับ done/ans/rate
rep('done:{},ans:{},notes:{},rate:{},theme:"",hide:{}};','done:{},ans:{},notes:{},rate:{},theme:"",hide:{},log:{}};')
rep('''  rate:pick(o.rate,function(v){return typeof v==="string"&&v.length<40;})};}''',
'''  rate:pick(o.rate,function(v){return typeof v==="string"&&v.length<40;}),log:normLog(o.log)};}
/* ประวัติการทวนรายวัน {yyyy-mm-dd:[section id]} เก็บ 60 วันล่าสุด (ผู้ใช้ขอ 9 พ.ย.) */
function normLog(o){var r={};if(!o||typeof o!=="object")return r;
  Object.keys(o).filter(function(k){return /^\\d{4}-\\d{2}-\\d{2}$/.test(k)&&Array.isArray(o[k]);}).sort().slice(-60).forEach(function(k){
    var a=[];o[k].forEach(function(v){if(typeof v==="string"&&v.length<80&&a.indexOf(v)<0)a.push(v);});if(a.length)r[k]=a.slice(-200);});return r;}
function mergeLog(a,b){var r={};[a||{},b||{}].forEach(function(o){Object.keys(o).forEach(function(k){r[k]=(r[k]||[]).concat(o[k].filter(function(v){return (r[k]||[]).indexOf(v)<0;}));});});return normLog(r);}''')
rep('if(k==="p"){var p=normP(data);state.done=p.done;state.ans=p.ans;state.rate=p.rate;}',
    'if(k==="p"){var p=normP(data);state.done=p.done;state.ans=p.ans;state.rate=p.rate;state.log=p.log;}')
rep('state.done=Object.assign({},c.done,l.done);state.ans=Object.assign({},l.ans,c.ans);state.rate=Object.assign({},c.rate,l.rate);}',
    'state.done=Object.assign({},c.done,l.done);state.ans=Object.assign({},l.ans,c.ans);state.rate=Object.assign({},c.rate,l.rate);state.log=mergeLog(c.log,l.log);}')
# 3) สีเน้นใช้ lime ทั้งเว็บ (เลิกสีประจำชุดที่ตั้งเป็น inline style)
rep('function applyAccent(c){\n','function applyAccent(c){\n  var r0=document.documentElement.style;["--accent","--accent-soft","--accent-ink","--on-accent"].forEach(function(k){r0.removeProperty(k);});return;\n')
# 4) JS ก่อน boot
rep("renderSync();\nboot();", js+"\nrenderSync();\nboot();")
open(dst,'w',encoding='utf-8').write(h)
print("ok",len(h))
