# -*- coding: utf-8 -*-
"""MED421 learn: เพิ่มหน้า "คาบเรียน" ของแต่ละระบบ (การ์ดทุกคาบ กดเข้าไปดูทีละคาบ) — ใช้บนมือถือไม่ต้องเลื่อนยาว

    python3 patch_learn_lectures.py <index.html ของ learn (ดาวน์โหลดมา หรือไฟล์ที่ unwrap แล้ว)> <ไฟล์ออก>

- แท็บใหม่ "คาบเรียน" (view = lectures) · กดการ์ด → view = lecture แสดงเฉพาะคาบนั้น + ปุ่มคาบก่อน/ถัดไป + MEQ/OSCE ของคาบ
- ลิงก์ตรงจาก dashboard (#<ชุด>-<คาบ>) เปิดหน้าคาบนั้นเลย แทนการเลื่อนหาในหน้าภาพรวม
- ต้องรันบนหน้าที่มีแพตช์ลิงก์ตรง (patch_deeplinks) แล้ว · ไม่แตะส่วนบันทึกในบัญชี (patch_learn_sync)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402


def patch(src):
    s = unwrap(src) if src.startswith("<!doctype html><html><head><meta charset=utf8>") else src
    # 1) แท็บ
    s = sub(s, '''var TABS=[{k:"home",label:"ภาพรวม"},''', '''var TABS=[{k:"home",label:"ภาพรวม"},{k:"lectures",label:"คาบเรียน"},''')
    s = sub(s, '''(state.view===t.k||(state.view==="section"&&t.k==="learn")?" on":"")''',
            '''(state.view===t.k||(state.view==="section"&&t.k==="learn")||(state.view==="lecture"&&t.k==="lectures")?" on":"")''')
    # 2) แยกการ์ดคาบออกจากหน้าภาพรวมเป็น lecCard(l)
    a = s.index("  lectures().forEach(function(l){\n    var done=l.sections.filter")
    b = s.index("  });\n  return h;\n}\n\nfunction viewSection(){")
    body = s[a:b]
    inner = body[len("  lectures().forEach(function(l){\n"):]
    s = s[:a] + "  lectures().forEach(function(l){h+=lecCard(l);});\n  return h;\n}\n" + r'''
/* ---------- หน้า "คาบเรียน": การ์ดทุกคาบของชุด → กดเข้าไปดูทีละคาบ ---------- */
function lecCard(l){
  var h="";
''' + inner.replace("\n    ", "\n  ") + '''  return h;
}
function lecStat(l){
  var n=l.sections.length,d=l.sections.filter(function(s){return secStat(s).complete;}).length,
      q=l.sections.reduce(function(a,s){return a+s.items.length;},0);
  return {n:n,done:d,q:q,pct:n?Math.round(d*100/n):0};
}
function viewLectures(){
  var c=course(),ls=lectures();
  var h="<section class='card'><div class='eyebrow'>"+esc(c.label)+" · คาบเรียน</div><h2>เลือกคาบที่จะเรียน</h2>"+
    "<p class='lede'>ชุดนี้มี "+ls.length+" คาบ · กดการ์ดเพื่อเข้าไปดูหัวข้อ ข้อเช็ค MEQ และ OSCE ของคาบนั้น</p>"+
    "<div class='lgrid'>"+ls.map(function(l){var st=lecStat(l);
      return "<button class='ltile' data-openlec='"+esc(l.lec)+"'>"+
        "<span class='lnum'>คาบ "+esc(l.lec)+(l.date&&!/^TBD/.test(l.date)?" · "+esc(l.date):"")+"</span>"+
        "<b>"+esc(l.title)+"</b>"+(l.subtitle?"<span class='lsub'>"+esc(l.subtitle)+"</span>":"")+
        "<span class='lprog'><span class='bar'><i style='width:"+st.pct+"%'></i></span><span>เรียนจบ "+st.done+"/"+st.n+" หัวข้อ</span></span>"+
        "<span class='lchips'><span class='chip'>ข้อเช็ค "+st.q+"</span><span class='chip'>MEQ "+(l.meq||[]).length+"</span><span class='chip'>OSCE/SAQ "+(l.osce||[]).length+"</span></span>"+
        "</button>";}).join("")+"</div></section>";
  return h;
}
function viewLecture(){
  var ls=lectures(),l=lecOf(state.lec);
  if(!l)return viewLectures();
  var i=ls.indexOf(l),prev=ls[i-1],next=ls[i+1];
  var nav="<div class='nav lnav'><button class='btn' data-tab='lectures'>← คาบทั้งหมด</button><span style='flex:1'></span>"+
    (prev?"<button class='btn' data-openlec='"+esc(prev.lec)+"'>‹ คาบ "+esc(prev.lec)+"</button>":"")+
    (next?"<button class='btn' data-openlec='"+esc(next.lec)+"'>คาบ "+esc(next.lec)+" ›</button>":"")+"</div>";
  var h=nav+lecCard(l);
  var pr=[];(l.meq||[]).forEach(function(it){pr.push({k:"meq",it:it});});(l.osce||[]).forEach(function(it){pr.push({k:"osce",it:it});});
  if(pr.length)h+="<section class='card'><div class='eyebrow'>ฝึกต่อของคาบนี้</div><h2>MEQ และ OSCE/SAQ</h2><div class='grid'>"+pr.map(function(x){
    var r=state.rate[x.it.id];
    return "<button class='tile' data-pid='"+esc(x.it.id)+"' data-pv='"+x.k+"'><b>"+esc(x.it.topic||x.it.id)+"</b>"+
      "<span>"+esc(x.k==="meq"?"MEQ · "+((x.it.questions||[]).length)+" คำถามย่อย":(x.it.station||"OSCE/SAQ"))+"</span>"+
      "<span class='chip"+(r?" acc":"")+"' style='align-self:flex-start;margin-top:4px'>"+(r?("ประเมินตัวเองแล้ว: "+r):"ยังไม่ได้ทำ")+"</span></button>";}).join("")+"</div></section>";
  return h+nav;
}
''' + s[b + len("  });\n  return h;\n}\n"):]
    # 3) render + events
    s = sub(s, '''  else if(state.view==="review")h=viewReview();''',
            '''  else if(state.view==="review")h=viewReview();
  else if(state.view==="lectures")h=viewLectures();
  else if(state.view==="lecture")h=viewLecture();''')
    s = sub(s, '''  if(t.dataset.lec){state.lec=''', '''  if(t.dataset.openlec){state.view="lecture";state.lec=t.dataset.openlec;state.sec=null;state.pid=null;render();window.scrollTo({top:0});return;}
  if(t.dataset.lec){state.lec=''')
    s = sub(s, '''  if(t.dataset.pid!==undefined&&t.dataset.pid!==""){state.pid=t.dataset.pid;''',
            '''  if(t.dataset.pid!==undefined&&t.dataset.pid!==""){if(t.dataset.pv)state.view=t.dataset.pv;state.pid=t.dataset.pid;''')
    s = sub(s, '''      state.course=t.dataset.course;state.view="home";state.lec=null;''',
            '''      state.course=t.dataset.course;state.view=(state.view==="lectures"||state.view==="lecture")?"lectures":"home";state.lec=null;''')
    # หน้าหัวข้อ: ปุ่มกลับหน้าคาบ
    s = sub(s, '''  h+="<div class='nav' style='margin-top:14px'>"+
     (idx>0?''', '''  h+="<div class='nav' style='margin-top:14px'>"+
     "<button class='btn' data-openlec='"+esc(l.lec)+"'>↑ หน้าคาบ "+esc(l.lec)+"</button>"+
     (idx>0?''')
    # 4) ลิงก์ตรงจาก dashboard เปิดหน้าคาบนั้นเลย
    a = s.index("  state.lec=hit.lec;render();\n  var el=document.getElementById(\"lec-\"+slug(hit.lec));")
    b = s.index("\n}", a)
    s = s[:a] + "  state.view=\"lecture\";state.lec=hit.lec;render();window.scrollTo({top:0});" + s[b:]
    # 5) CSS
    s = sub(s, '''.tile:hover{border-color:var(--accent);transform:translateY(-2px)}''', '''.tile:hover{border-color:var(--accent);transform:translateY(-2px)}
.lgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:13px;margin-top:16px}
.ltile{text-align:left;font:inherit;color:var(--ink);background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--accent);border-radius:var(--r-md);
  padding:14px 15px;cursor:pointer;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:6px;min-width:0;
  transition:border-color .22s var(--e),transform .22s var(--e)}
.ltile:hover{border-color:var(--accent);transform:translateY(-2px)}
.ltile .lnum{font:600 11.5px/1.3 var(--mono);color:var(--accent-ink);letter-spacing:.02em}
.ltile b{font-size:16px;font-weight:700;line-height:1.3;letter-spacing:-.01em}
.ltile .lsub{font-size:12.8px;color:var(--ink-3);line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.ltile .lprog{display:flex;align-items:center;gap:8px;font-size:12.3px;color:var(--ink-2);margin-top:2px}
.ltile .lprog .bar{width:90px;flex:none}
.ltile .lchips{display:flex;flex-wrap:wrap;gap:5px}
.lnav{align-items:center}''')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    out = patch(open(sys.argv[1], encoding="utf-8").read())
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print("ok", len(out))
