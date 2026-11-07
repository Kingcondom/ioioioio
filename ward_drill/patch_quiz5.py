#!/usr/bin/env python3
"""โหมดสุ่มทำข้อสอบ: เพิ่มขอบเขต "ระบบละ 5 ข้อ" — สุ่ม 5 ข้อจากทุกระบบ ยกเว้น Mock NL

ใช้:  python3 ward_drill/patch_quiz5.py ward_drill/index.html   (แก้ไฟล์เดิม · รันซ้ำได้)
"""
import sys

REPL = [
    ('var QZ_SCOPE=[{k:"set",label:"ระบบนี้ทุกคาบ"},{k:"all",label:"ทุกระบบ"}];',
     'var QZ_SCOPE=[{k:"set",label:"ระบบนี้ทุกคาบ"},{k:"all",label:"ทุกระบบ"},{k:"per",label:"ระบบละ 5 ข้อ (ไม่รวม Mock NL)"}];\n'
     'var QZ_PER=5,QZ_SKIP={mock:1};',
     "var QZ_PER=5"),
    ('if(qr.scope==="set"||qr.scope==="all")quiz.scope=qr.scope;',
     'if(qr.scope==="set"||qr.scope==="all"||qr.scope==="per")quiz.scope=qr.scope;', 'qr.scope==="per"'),
    ('    var e=idx[id];if(quiz.scope==="set"&&e.set!==state.set)return false;',
     '    var e=idx[id];if(quiz.scope==="set"&&e.set!==state.set)return false;\n'
     '    if(quiz.scope==="per"&&QZ_SKIP[e.set])return false;', 'quiz.scope==="per"&&QZ_SKIP'),
    # สุ่มแยกทีละระบบ ระบบละ QZ_PER ข้อ เรียงตามลำดับแท็บระบบ
    ('function qDraw(ids){\n  quiz.ids=ids||qShuffle(qPool()).slice(0,quiz.n);',
     'function qPerSet(){var idx=qIndex(),by={};qPool().forEach(function(id){var s=idx[id].set;(by[s]=by[s]||[]).push(id);});\n'
     '  var out=[];SETS.forEach(function(s){if(by[s.k])out=out.concat(qShuffle(by[s.k]).slice(0,QZ_PER));});return out;}\n'
     'function qWant(){return quiz.scope==="per"?qPerSet().length:Math.min(quiz.n,qPool().length);}\n'
     'function qDraw(ids){\n  quiz.ids=ids||(quiz.scope==="per"?qPerSet():qShuffle(qPool()).slice(0,quiz.n));',
     "function qPerSet()"),
    ('(quiz.scope==="all"?"ทุกระบบ":setLabel(state.set))+" · "+QZ_POOL',
     '(quiz.scope==="per"?"ระบบละ "+QZ_PER+" ข้อ (ไม่รวม Mock NL)":quiz.scope==="all"?"ทุกระบบ":setLabel(state.set))+" · "+QZ_POOL',
     '"ระบบละ "+QZ_PER+" ข้อ (ไม่รวม Mock NL)":quiz.scope'),
    ('  var n=qPool().length;\n  document.getElementById("qzinfo").textContent="มีให้สุ่ม "+n+" ข้อ"+(n<quiz.n&&n?" (น้อยกว่าที่เลือก จะได้ "+n+" ข้อ)":"");',
     '  var n=qPool().length,per=quiz.scope==="per",qn=document.getElementById("qzn");\n'
     '  qn.style.display=per?"none":"";if(qn.previousElementSibling)qn.previousElementSibling.style.display=per?"none":"";\n'
     '  if(per){var w=qWant(),k=0,idx=qIndex(),seen={};qPool().forEach(function(id){if(!seen[idx[id].set]){seen[idx[id].set]=1;k++;}});\n'
     '    document.getElementById("qzinfo").textContent="จะได้ "+w+" ข้อ จาก "+k+" ระบบ ("+QZ_PER+" ข้อต่อระบบ เรียงตามระบบ) · ไม่รวม Mock NL";}\n'
     '  else document.getElementById("qzinfo").textContent="มีให้สุ่ม "+n+" ข้อ"+(n<quiz.n&&n?" (น้อยกว่าที่เลือก จะได้ "+n+" ข้อ)":"");',
     'var n=qPool().length,per=quiz.scope==="per"'),
    ('(quiz.scope==="all"?" ทุกระบบ":" ของ "+esc(setLabel(state.set)))',
     '(quiz.scope==="per"?" ระบบละ "+QZ_PER+" ข้อ ทุกระบบยกเว้น Mock NL":quiz.scope==="all"?" ทุกระบบ":" ของ "+esc(setLabel(state.set)))',
     '" ระบบละ "+QZ_PER+" ข้อ ทุกระบบยกเว้น Mock NL"'),
    ('b.textContent="เริ่มสุ่ม "+Math.min(quiz.n,pool)+" ข้อ";', 'b.textContent="เริ่มสุ่ม "+qWant()+" ข้อ";', '"เริ่มสุ่ม "+qWant()'),
    ('(quiz.scope==="all"||e.set!==state.set?', '(quiz.scope!=="set"||e.set!==state.set?', 'quiz.scope!=="set"||e.set'),
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
