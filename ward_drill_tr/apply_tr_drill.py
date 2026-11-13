# -*- coding: utf-8 -*-
"""ใส่โครงหน้าแบบ Teaching Round ลงหน้า MED421 Ward Drill

    python3 apply_tr_drill.py <live.html> <out.html>

<live.html> = ไฟล์ที่ Artifact action:read บันทึกไว้ (สคริปต์ตัด wrapper ของแพลตฟอร์มบรรทัดแรก
และ </body></html> ที่ซ้ำท้ายไฟล์ให้เอง) · ไม่ลบฟีเจอร์เดิม: quiz · ปุ่มปัก Post-it · คำตอบ/ประวัติ ·
คีย์ localStorage และการซิงก์บัญชีเดิมอยู่ครบ · เพิ่ม state.log (ประวัติการทำรายวัน) ซิงก์ไปเอกสารบัญชีเดียวกัน
"""
import sys, os
D = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
assert "var TR=(function" not in h, "already patched"

# 0) ตัด wrapper ของแพลตฟอร์ม (บรรทัดแรก) + </body></html> ที่ซ้ำท้ายไฟล์
W = '<!doctype html><html><head><meta charset=utf8>'
if h.startswith(W):
    h = h[h.index('\n') + 1:]
t = h.rstrip()
if t.endswith('</body></html>\n\n</body></html>') or t.count('</body></html>') >= 2:
    t = t[:t.rindex('</body></html>')].rstrip()
h = t + '\n'
assert h.startswith('<!doctype html>'), h[:60]

css = open(os.path.join(D, 'tr_drill.css'), encoding='utf-8').read()
js = open(os.path.join(D, 'tr_drill.js'), encoding='utf-8').read()
css += '\n' + open(os.path.join(D, 'sys_colors.css'), encoding='utf-8').read()   # สีประจำระบบ (13 พ.ย.)


def rep(a, b, n=1):
    global h
    assert h.count(a) == n, (h.count(a), a[:90])
    h = h.replace(a, b)


# 1) CSS ต่อท้าย stylesheet หลัก (ก่อน header)
rep('\n</style>\n\n<header class="mast">', '\n</style>\n<style id="tr-style">\n' + css + '</style>\n\n<header class="mast">')
# 2) ที่วางหน้าแรก
rep('<div class="wrap shell">', '<section class="wrap tr-homewrap" id="trHome" aria-label="หน้าแรก"></section>\n<div class="wrap shell">')
# 3) ประวัติการทำรายวัน state.log {yyyy-mm-dd:[id ข้อ]} เก็บ 60 วัน · ซิงก์บัญชีไปกับ answers/shown
rep('var state={set:"cardio",mode:"new",lec:"all",part:"all",answers:{},shown:{}};',
    'var state={set:"cardio",mode:"new",lec:"all",part:"all",answers:{},shown:{},log:{}};')
rep('state.answers=s.answers||{};state.shown=s.shown||{};',
    'state.answers=s.answers||{};state.shown=s.shown||{};state.log=normLog(s.log);')
rep('{answers:state.answers,shown:state.shown,set:state.set,mode:state.mode}',
    '{answers:state.answers,shown:state.shown,log:state.log,set:state.set,mode:state.mode}', 2)
rep('function norm(o){o=o||{};return {answers:normA(o.answers),shown:normS(o.shown)};}',
    'function norm(o){o=o||{};return {answers:normA(o.answers),shown:normS(o.shown),log:normLog(o.log)};}\n'
    '/* ประวัติการทำรายวัน {yyyy-mm-dd:[id ข้อ]} เก็บ 60 วันล่าสุด (ผู้ใช้ขอ 9 พ.ย. — หน้าแรกแบบ Teaching Round) */\n'
    'function normLog(o){var r={};if(!o||typeof o!=="object")return r;\n'
    '  Object.keys(o).filter(function(k){return /^\\d{4}-\\d{2}-\\d{2}$/.test(k)&&Array.isArray(o[k]);}).sort().slice(-60).forEach(function(k){\n'
    '    var a=[];o[k].forEach(function(v){if(typeof v==="string"&&v.length<60&&a.indexOf(v)<0)a.push(v);});if(a.length)r[k]=a.slice(-300);});return r;}\n'
    'function mergeLog(a,b){var r={};[a||{},b||{}].forEach(function(o){Object.keys(o).forEach(function(k){r[k]=(r[k]||[]).concat(o[k].filter(function(v){return (r[k]||[]).indexOf(v)<0;}));});});return normLog(r);}')
rep('function adopt(data){var n=norm(data);state.answers=n.answers;state.shown=n.shown;}',
    'function adopt(data){var n=norm(data);state.answers=n.answers;state.shown=n.shown;state.log=n.log;}')
rep('state.answers=Object.assign({},c.answers,l.answers);state.shown=Object.assign({},c.shown,l.shown);}',
    'state.answers=Object.assign({},c.answers,l.answers);state.shown=Object.assign({},c.shown,l.shown);state.log=mergeLog(c.log,l.log);}')
# 3b) ข้อจากหลายระบบในหน้าเดียว (ข้อสอบแยกปี / มีรูป / คาบที่ทวน): ป้ายและการ์ดใช้สีของระบบนั้น
rep('if(hd){var t=document.createElement("span");t.className="tag sys";',
    'el.classList.add("sys-"+e.set);if(hd){var t=document.createElement("span");t.className="tag sys sys-"+e.set;')
# 4) JS ก่อน render ครั้งแรก (อยู่ใน IIFE เดียวกับของเดิม จึงเรียก state/render/save ได้)
rep('\nrender();renderSync();\n})();', js + '\nrender();renderSync();\n})();')
open(dst, 'w', encoding='utf-8').write(h)
print("ok", len(h.encode('utf-8')))
