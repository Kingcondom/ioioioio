# -*- coding: utf-8 -*-
"""รูปภาพ (ไฟล์ใน artifact) ในบทเรียน MED421 learn — [[img:key]] + section.imgs

    python3 patch_learn_img.py <learn index.html (ผ่าน patch_learn_anim แล้ว)> <out.html>

section.imgs = {key: {src:"img/pbs/p-20.jpg", alt, cap, credit?, quiz?:"เฉลย"}}
- รูปกดแล้วเปิดเต็มจอในแท็บใหม่ · lazy load
- ถ้ามี quiz: ซ่อนคำบรรยาย แสดงปุ่ม "ดูเฉลย" ให้ลองอ่านก่อน (spot diagnosis)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_deeplinks import unwrap, sub  # noqa: E402

CSS = r'''
/* ---------- รูปภาพในบทเรียน ([[img:key]] + section.imgs) ---------- */
.fig.pimg{padding:10px 10px 12px}
.fig.pimg a.pz{display:block;border-radius:var(--r-sm);overflow:hidden;background:var(--surface-sunk)}
.fig.pimg img{display:block;width:100%;height:auto;max-width:620px;margin:0 auto}
.fig.pimg .pcr{font-size:11.5px;color:var(--ink-3);margin-top:6px}
.fig.pimg .pq{margin-top:9px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.fig.pimg .pq b{font-size:13.5px;color:var(--accent-ink)}
.fig.pimg .pans{margin-top:8px;padding:10px 12px;border-radius:var(--r-sm);background:var(--ok-soft);border:1px solid var(--ok);font-size:13.6px;line-height:1.6}
'''

JS = r'''
/* ---------- รูปภาพในบทเรียน ---------- */
var IMGS={};
function imgHtml(k){
  var g=IMGS[k];if(!g||!g.src)return "";
  FIGN++;
  var h="<figure class='fig pimg'>"+(g.title?"<div class='figt'><span>ภาพ "+FIGN+"</span>"+inline(g.title)+"</div>":"")+
    "<a class='pz' href='"+esc(g.src)+"' target='_blank' rel='noopener' title='แตะเพื่อดูภาพเต็ม'><img src='"+esc(g.src)+"' alt='"+esc(g.alt||g.title||"")+"' loading='lazy' decoding='async'></a>";
  if(g.quiz){
    h+="<div class='pq'><b>"+inline(g.q||"ลองอ่าน smear นี้ก่อน — คิดว่าเป็นอะไร")+"</b><button class='btn' data-pqa='1'>ดูเฉลย</button></div>"+
       "<div class='pans hide'>"+inline(g.quiz)+"</div>";
  }else if(g.cap)h+="<figcaption>"+inline(g.cap)+"</figcaption>";
  if(g.credit)h+="<div class='pcr'>"+inline(g.credit)+"</div>";
  return h+"</figure>";
}
document.addEventListener("click",function(e){
  var b=e.target.closest&&e.target.closest("[data-pqa]");if(!b)return;
  var a=b.closest("figure").querySelector(".pans");if(!a)return;
  var hid=a.classList.toggle("hide");b.textContent=hid?"ดูเฉลย":"ซ่อนเฉลย";
});
'''


def patch(src):
    s = unwrap(src) if src.startswith("<!doctype html><html><head><meta charset=utf8>") else src
    if "function imgHtml" in s:
        return s
    assert "function animHtml" in s, "ต้องผ่าน patch_learn_anim ก่อน"
    s = sub(s, '.chip.anc{', CSS.strip() + '\n.chip.anc{')
    s = sub(s, '/* ---------- tiny markdown (เหมือน drill.html) ---------- */',
            JS.strip() + '\n\n/* ---------- tiny markdown (เหมือน drill.html) ---------- */')
    s = sub(s, '''    if(am){flushPara();out.push(animHtml(am[1]));i++;continue;}''',
            '''    if(am){flushPara();out.push(animHtml(am[1]));i++;continue;}
    var im=/^\\s*\\[\\[img:([\\w-]+)\\]\\]\\s*$/.exec(L);
    if(im){flushPara();out.push(imgHtml(im[1]));i++;continue;}''')
    s = sub(s, '''ANIMS=s.anims||{},ANIMN=0,''', '''ANIMS=s.anims||{},ANIMN=0,IMGS=s.imgs||{},''')
    s = sub(s, '''  FIGS={};ANIMS={};''', '''  FIGS={};ANIMS={};IMGS={};''')
    return s


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    open(sys.argv[2], "w", encoding="utf-8").write(patch(open(sys.argv[1], encoding="utf-8").read()))
    print("ok")
