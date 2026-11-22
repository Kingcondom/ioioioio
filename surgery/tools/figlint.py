import json,sys,re
import xml.etree.ElementTree as ET
OKC=set("bx sk ac ok bad ms wa acf okf badf msf waf inkf muf ruf paf ln lmu lac lok lbad lms lwa lru w2 w3 w5 da dt ns lg sm xs b mid end mu i2 tac tok tbad tms twa tpa".split())
MK={"url(#ah)","url(#ah-ac)","url(#ah-ok)","url(#ah-bad)","url(#ah-ms)","url(#ah-wa)","url(#ah-mu)"}
bad=0
def err(m):
    global bad;bad+=1;print("ERROR:",m)
for p in sys.argv[1:]:
    L=json.load(open(p,encoding="utf-8"));nf=0
    for s in L["sections"]:
        figs=s.get("figs") or {}
        refs=re.findall(r"^\s*\[\[fig:([\w-]+)\]\]\s*$",s["md"],re.M)
        if not figs:err(f"{s['id']}: no figure")
        for k in refs:
            if k not in figs:err(f"{s['id']}: md references missing fig {k}")
        for k,f in figs.items():
            nf+=1;sid=f"{s['id']}/{k}"
            if not re.match(r"^[a-z0-9_-]+$",k):err(f"{sid}: bad key")
            if k not in refs:err(f"{sid}: not placed in md as [[fig:{k}]]")
            for a in ("title","cap","svg"):
                if not f.get(a):err(f"{sid}: missing {a}")
            svg=f.get("svg","")
            try:root=ET.fromstring(svg)
            except Exception as x:err(f"{sid}: SVG not well-formed XML: {x}");continue
            vb=root.get("viewBox","").split()
            if len(vb)!=4:err(f"{sid}: missing viewBox")
            elif float(vb[2])>440:err(f"{sid}: viewBox width {vb[2]} > 440")
            if root.get("width") or root.get("height"):err(f"{sid}: remove width/height attrs")
            if not root.get("aria-label"):err(f"{sid}: aria-label missing")
            if re.search(r"#[0-9a-fA-F]{3,6}\b(?!-)",re.sub(r'url\(#ah[-a-z]*\)',"",svg)):err(f"{sid}: hard-coded hex colour")
            if re.search(r"<(style|image|script|foreignObject)",svg):err(f"{sid}: forbidden element")
            if re.search(r'(fill|stroke)="(?!none)',svg):err(f"{sid}: fill/stroke attribute — use classes")
            for c in re.findall(r'class="([^"]*)"',svg):
                for t in c.split():
                    if t not in OKC:err(f"{sid}: unknown class {t}")
            for m in re.findall(r'marker-end="([^"]+)"',svg):
                if m not in MK:err(f"{sid}: unknown marker {m}")
            if len(svg)>9000:print(f"WARN: {sid}: svg large ({len(svg)} chars)")
    print(f"{p}: {nf} figures")
sys.exit(1 if bad else 0)
