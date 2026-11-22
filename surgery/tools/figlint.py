import json,sys,re
import xml.etree.ElementTree as ET
OKC=set("fl rv sl pl bx sk ac ok bad ms wa acf okf badf msf waf inkf muf ruf paf ln lmu lac lok lbad lms lwa lru w2 w3 w5 da dt ns lg sm xs b mid end mu i2 tac tok tbad tms twa tpa".split())
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
    na=0
    for s in L["sections"]:
        refs=re.findall(r"^\s*\[\[anim:([\w-]+)\]\]\s*$",s["md"],re.M)
        for k in refs:
            if k not in (s.get("anims") or {}):err(f"{s['id']}: md references missing anim {k}")
        for k,a in (s.get("anims") or {}).items():
            na+=1;sid=f"{s['id']}/anim:{k}"
            if k not in refs:err(f"{sid}: not placed in md as [[anim:{k}]]")
            if not re.match(r"^[a-z0-9_-]+$",k):err(f"{sid}: bad key")
            st=a.get("steps") or []
            if not (4<=len(st)<=9):err(f"{sid}: needs 4-9 steps, has {len(st)}")
            for i,x in enumerate(st):
                if not x.get("t") or not x.get("cap"):err(f"{sid}: step {i+1} needs t and cap")
            svg=a.get("svg","")
            try:root=ET.fromstring(svg)
            except Exception as x:err(f"{sid}: SVG not well-formed XML: {x}");continue
            vb=root.get("viewBox","").split()
            if len(vb)!=4 or float(vb[2])>440:err(f"{sid}: viewBox missing or wider than 440")
            if re.search(r"<(style|image|script|foreignObject|animate)",svg):err(f"{sid}: forbidden element (use step classes, not SMIL)")
            if re.search(r'(fill|stroke)="(?!none)',svg) or re.search(r"#[0-9a-fA-F]{3,6}\b",re.sub(r'url\(#ah[-a-z]*\)',"",svg)):err(f"{sid}: hard-coded colour")
            for c in re.findall(r'class="([^"]*)"',svg):
                for t in c.split():
                    if t not in OKC:err(f"{sid}: unknown class {t}")
            used=set()
            for el in root.iter():
                ds,dx=el.get("data-s"),el.get("data-x")
                for v in (ds,dx):
                    if v is not None and (not v.isdigit() or not 1<=int(v)<=len(st)):err(f"{sid}: data-s/x value {v} out of 1..{len(st)}")
                if ds and ds.isdigit():used.add(int(ds))
                cl=(el.get("class") or "").split()
                if (ds or dx) and "pl" in cl:err(f"{sid}: element with class pl cannot carry data-s/data-x (the pulse overrides hiding) — wrap it: <g data-s=..><rect class='.. pl'/></g>")
            miss=[i for i in range(2,len(st)+1) if i not in used]
            if miss:print(f"WARN: {sid}: steps {miss} reveal nothing new (data-s)")
    rd=L.get("reading")
    if rd is not None:
        ids=[s["id"] for s in L["sections"]]
        o=[x.get("sec") for x in rd.get("order",[])]
        if sorted(o)!=sorted(ids):err(f"reading.order must list every section once")
        for x in rd.get("order",[]):
            if x.get("level") not in ("must","extra"):err("reading.order level must be must/extra")
        for k in ("minutes","start","schwartz","beyond","tips"):
            if not rd.get(k):err(f"reading.{k} missing")
        for x in rd.get("schwartz",[]):
            if not x.get("ch") or not x.get("part"):err("reading.schwartz items need ch and part")
    print(f"{p}: {nf} figures, {na} animations, reading={'yes' if rd else 'no'}")
sys.exit(1 if bad else 0)
