import json, sys, re
ERR=[];WARN=[]
def e(m):ERR.append(m)
def w(m):WARN.append(m)
REQ_L=["lec","date","title","subtitle","objectives","sections","meq","osce"]
def chk_mcq(it,sid,ids):
    for k in ["id","kind","stem","choices","answer","explain","pearl","topic"]:
        if k not in it:e(f"{sid}: item missing {k}")
    iid=it.get("id","?")
    if iid in ids:e(f"duplicate id {iid}")
    ids.add(iid)
    if not str(iid).startswith(sid.upper()+"-"):w(f"{iid}: id should start with {sid.upper()}-")
    ch=it.get("choices",[])
    if len(ch)!=5:e(f"{iid}: needs 5 choices, has {len(ch)}")
    if len(set(c.strip().lower() for c in ch))!=len(ch):e(f"{iid}: duplicate choices")
    if it.get("answer")!=0:e(f"{iid}: answer must be 0 (correct choice first)")
    ex=it.get("explain","")
    if re.search(r"(ข้อ|ตัวเลือก|choice|option)\s*\(?[A-Ea-e]\)?(?![A-Za-z])",ex):w(f"{iid}: explain seems to reference an option letter")
    if len(ex)<200:w(f"{iid}: explain short ({len(ex)} chars)")
    if len(it.get("stem",""))<120:w(f"{iid}: stem short")
def chk_md(md,sid):
    if re.search(r"^\s*#{1,2}\s",md,re.M):e(f"{sid}: md uses #/## heading (only ###/#### allowed)")
    if "<" in md and re.search(r"<[a-zA-Z/]",md):w(f"{sid}: md contains HTML-like tag")
    if re.search(r"!\[|\]\(http",md):e(f"{sid}: md contains image/link syntax")
    n3=len(re.findall(r"^\s*###\s",md,re.M))
    if n3<2:w(f"{sid}: only {n3} ### headings")
    if len(md)<2000:w(f"{sid}: md short ({len(md)} chars)")
    # table separator check
    lines=md.split("\n")
    for i,L in enumerate(lines):
        if L.strip().startswith("|") and (i==0 or not lines[i-1].strip().startswith("|")):
            if i+1>=len(lines) or not re.match(r"^\s*\|\s*:?-{2,}",lines[i+1]):w(f"{sid}: table at line {i} lacks separator row")
def main(p):
    try:L=json.load(open(p,encoding="utf-8"))
    except Exception as x:print("ERROR: not valid JSON:",x);sys.exit(1)
    if isinstance(L,list):e("file must contain ONE lecture object, not a list");L=L[0] if L else {}
    for k in REQ_L:
        if k not in L:e(f"lecture missing {k}")
    ids=set()
    course=p.split("/")[-1].split("_")[0]
    for s in L.get("sections",[]):
        sid=s.get("id","?")
        if not re.match(rf"^{course}-{L.get('lec')}-\d+$",sid):e(f"section id {sid} should look like {course}-{L.get('lec')}-1")
        if sid in ids:e(f"duplicate section id {sid}")
        ids.add(sid)
        for k in ["title","summary","md","pearls","items","source","minutes"]:
            if k not in s:e(f"{sid}: missing {k}")
        chk_md(s.get("md",""),sid)
        for m in s.get("mnem",[]) or []:
            if not isinstance(m,dict) or "name" not in m or not isinstance(m.get("lines",[]),list):e(f"{sid}: bad mnem")
        for it in s.get("items",[]):chk_mcq(it,sid,ids)
    for m in L.get("meq",[]):
        for k in ["id","topic","vignette","questions"]:
            if k not in m:e(f"meq missing {k}")
        if m.get("id") in ids:e(f"duplicate id {m.get('id')}")
        ids.add(m.get("id"))
        for q in m.get("questions",[]):
            if "q" not in q or "a" not in q:e(f"{m.get('id')}: question needs q and a")
    for o in L.get("osce",[]):
        for k in ["id","topic","station","instruction","answer"]:
            if k not in o:e(f"osce missing {k}")
        if not re.search(r"\d+\s*นาที",o.get("station","")):e(f"{o.get('id')}: station must contain '<n> นาที'")
        if o.get("id") in ids:e(f"duplicate id {o.get('id')}")
        ids.add(o.get("id"))
    ns=len(L.get("sections",[]));nq=sum(len(s.get("items",[])) for s in L.get("sections",[]))
    for m in WARN:print("WARN:",m)
    for m in ERR:print("ERROR:",m)
    print(f"{p}: {ns} sections, {nq} MCQ, {len(L.get('meq',[]))} MEQ, {len(L.get('osce',[]))} OSCE — {len(ERR)} errors, {len(WARN)} warnings")
    sys.exit(1 if ERR else 0)
for p in sys.argv[1:]:main(p)
