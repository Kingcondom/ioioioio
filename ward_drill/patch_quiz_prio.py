#!/usr/bin/env python3
"""โหมดสุ่มทำข้อสอบ: ตัวเลือก "เลือกข้อจาก" — คลังข้อสอบเก่าก่อน (ค่าเริ่มต้น) หรือคละเท่ากัน

คลังข้อสอบเก่าก่อน = สุ่มจากข้อสอบเก่า (kind "old") ให้ครบจำนวนก่อน ถ้าไม่พอจึงเติมด้วยข้อใหม่ (MCQ ที่เขียนขึ้นใหม่)
ใช้กับทุกขอบเขต: ระบบนี้ / ทุกระบบ / ระบบละ 5 ข้อ (ทำทีละระบบ)
ต้องรัน patch_quiz5.py ก่อน

ใช้:  python3 ward_drill/patch_quiz_prio.py ward_drill/index.html   (แก้ไฟล์เดิม · รันซ้ำได้)
"""
import sys

REPL = [
    ('var QZ_PER=5,QZ_SKIP={mock:1};',
     'var QZ_PER=5,QZ_SKIP={mock:1};\n'
     'var QZ_PRIO=[{k:"old",label:"คลังข้อสอบเก่าก่อน"},{k:"mix",label:"คละเก่ากับใหม่"}];',
     "var QZ_PRIO="),
    ('var quiz={scope:"set",n:20,pool:"any",ids:[],ans:{},set:"",from:""};',
     'var quiz={scope:"set",n:20,pool:"any",prio:"old",ids:[],ans:{},set:"",from:""};', 'pool:"any",prio:"old"'),
    ('if(qr.pool==="any"||qr.pool==="fresh"||qr.pool==="wrong")quiz.pool=qr.pool;',
     'if(qr.pool==="any"||qr.pool==="fresh"||qr.pool==="wrong")quiz.pool=qr.pool;\n'
     '  if(qr.prio==="old"||qr.prio==="mix")quiz.prio=qr.prio;', 'qr.prio==="mix"'),
    # เลือก n ข้อจากรายการ id: คลังเก่าก่อน แล้วเติมด้วยข้อใหม่
    ('function qPerSet(){',
     'function qPick(ids,n){var idx=qIndex();if(quiz.prio!=="old")return qShuffle(ids.slice()).slice(0,n);\n'
     '  var o=[],w=[];ids.forEach(function(id){(idx[id].kind==="old"?o:w).push(id);});\n'
     '  o=qShuffle(o).slice(0,n);return o.concat(qShuffle(w).slice(0,n-o.length));}\n'
     'function qPerSet(){', "function qPick("),
    ('if(by[s.k])out=out.concat(qShuffle(by[s.k]).slice(0,QZ_PER));',
     'if(by[s.k])out=out.concat(qPick(by[s.k],QZ_PER));', "qPick(by[s.k],QZ_PER)"),
    ('quiz.ids=ids||(quiz.scope==="per"?qPerSet():qShuffle(qPool()).slice(0,quiz.n));',
     'quiz.ids=ids||(quiz.scope==="per"?qPerSet():qPick(qPool(),quiz.n));', "qPick(qPool(),quiz.n)"),
    # ระบุในหัวชุดว่าเลือกแบบไหน
    ('+" · "+QZ_POOL.filter(function(p){return p.k===quiz.pool;})[0].label;',
     '+" · "+QZ_POOL.filter(function(p){return p.k===quiz.pool;})[0].label+(quiz.prio==="old"?" · คลังข้อสอบเก่าก่อน":"");',
     '(quiz.prio==="old"?" · คลังข้อสอบเก่าก่อน":"")'),
    ('  qChips("qzpool",QZ_POOL,quiz.pool,function(k){quiz.pool=k;});',
     '  qChips("qzpool",QZ_POOL,quiz.pool,function(k){quiz.pool=k;});\n'
     '  qChips("qzprio",QZ_PRIO,quiz.prio,function(k){quiz.prio=k;});', 'qChips("qzprio"'),
    ('      <div class="parts" id="qzpool"></div>\n',
     '      <div class="parts" id="qzpool"></div>\n'
     '      <h2 class="qzh">เลือกข้อจาก</h2>\n'
     '      <div class="parts" id="qzprio"></div>\n', 'id="qzprio"'),
    # ข้อใหม่ในชุดสุ่มติดป้าย "ข้อใหม่" ให้แยกกับ "ข้อสอบเก่า" ได้
    ('(quiz.scope!=="set"||e.set!==state.set?"<span class=\'tag\'>"+esc(setLabel(e.set))+"</span>":""));',
     '(quiz.scope!=="set"||e.set!==state.set?"<span class=\'tag\'>"+esc(setLabel(e.set))+"</span>":"")+'
     '(e.kind==="mcq"?"<span class=\'tag\'>ข้อใหม่</span>":""));', ">ข้อใหม่</span>\":\"\"));"),
]


def main():
    p = sys.argv[1]
    html = open(p, encoding="utf-8").read()
    for old, new, marker in REPL:
        if marker in html:
            continue
        c = html.count(old)
        assert c == 1, f"anchor found {c}x: {old[:70]!r}"
        html = html.replace(old, new)
    open(p, "w", encoding="utf-8").write(html)
    print("patched", p)


if __name__ == "__main__":
    main()
