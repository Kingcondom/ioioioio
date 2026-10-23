# -*- coding: utf-8 -*-
"""ตรวจและดูตัวอย่างไฟล์ภาพเคลื่อนไหว/หลักจำของ learn (รูปแบบอธิบายใน patch_learn_anim.py)

    python3 anim_tool.py check   <data dir> <anim.json>
    python3 anim_tool.py preview <data dir> <learn index.html (ยังไม่ patch)> <anim.json> <out dir> [port]

check   — โครงสร้าง, section/หัวข้อมีจริง, SVG เป็น XML ถูกต้อง, ใช้แต่ class ของธีม, ขั้น data-s ครบ, ไม่มี script/สีตายตัว
preview — สร้างหน้า learn ที่ใส่ไฟล์นี้แล้ว เปิดด้วย Chromium ถ่ายภาพแต่ละภาพเคลื่อนไหวทุกขั้น (สว่าง) + ขั้นสุดท้าย (มืด)
          และกล่องหลักจำ → <out dir>/<key>-s<i>.png, <key>-dark.png, mnem-<sec>.png
"""
import sys, os, json, re, glob, shutil, subprocess, tempfile
import xml.etree.ElementTree as ET

ALLOWED = set("""lg sm xs b mid end mu i2 tac tok tbad tms twa tpa bx sk ac ok bad ms wa acf okf badf msf waf inkf muf ruf paf
ln lmu lac lok lbad lms lwa lru w2 w3 w5 da dt ns fl rv sl pl""".split())
MARKERS = {"ah", "ah-ac", "ah-ok", "ah-bad", "ah-ms", "ah-wa", "ah-mu"}
BAD_TAGS = {"script", "foreignObject", "image", "style", "a", "iframe", "use", "object", "embed"}
SVGNS = "{http://www.w3.org/2000/svg}"


def load_sections(data_dir, st):
    d = json.load(open(os.path.join(data_dir, st + ".json"), encoding="utf-8"))
    return {s["id"]: s for L in d for s in L["sections"]}


def headings(md):
    return [m.group(2).strip() for m in re.finditer(r"^\s*(#{3,4})\s+(.*)$", md, re.M)]


def check_svg(svg, n, where):
    errs = []
    if len(svg) > 16000:
        errs.append(f"{where}: SVG ยาว {len(svg)} ตัวอักษร (เกิน 16000)")
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as e:
        return [f"{where}: SVG ไม่ใช่ XML ที่ถูกต้อง: {e}"]
    if root.tag != SVGNS + "svg":
        errs.append(f"{where}: root ต้องเป็น <svg xmlns=\"http://www.w3.org/2000/svg\">")
    vb = root.get("viewBox", "")
    m = re.match(r"^\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*$", vb)
    if not m:
        errs.append(f"{where}: ต้องมี viewBox=\"0 0 W H\"")
    else:
        w, h = float(m.group(1)), float(m.group(2))
        if w > 560 or w < 260:
            errs.append(f"{where}: ความกว้าง viewBox {w} (ควร 320–480, ห้ามเกิน 560)")
        if h > 520:
            errs.append(f"{where}: ความสูง viewBox {h} สูงเกิน (≤ 520)")
    if root.get("role") != "img" or not root.get("aria-label"):
        errs.append(f"{where}: ต้องมี role=\"img\" และ aria-label บรรยายภาพ")
    if root.get("width") or root.get("height"):
        errs.append(f"{where}: ห้ามใส่ width/height ที่ <svg> (ให้ย่อขยายตามจอ)")
    seen = set()
    for el in root.iter():
        tag = el.tag.replace(SVGNS, "")
        if tag in BAD_TAGS:
            errs.append(f"{where}: ห้ามใช้ <{tag}>")
        for a, v in el.attrib.items():
            an = a.split("}")[-1]
            if an.lower().startswith("on"):
                errs.append(f"{where}: ห้าม attribute {an}")
            if an in ("fill", "stroke", "color", "stop-color") and v not in ("none", "currentColor"):
                errs.append(f"{where}: ห้ามกำหนดสีตายตัว {an}=\"{v}\" (ใช้ class ของธีม)")
            if an == "style" and re.search(r"(fill|stroke|color|url\()", v):
                errs.append(f"{where}: ห้ามกำหนดสี/url ใน style=\"{v[:40]}\"")
            if an in ("marker-end", "marker-start", "marker-mid"):
                mm = re.match(r"url\(#([\w-]+)\)$", v)
                if not mm or mm.group(1) not in MARKERS:
                    errs.append(f"{where}: marker ใช้ได้เฉพาะ {sorted(MARKERS)} ได้ {v}")
            if an == "href" or (an.endswith("href")):
                if not v.startswith("#"):
                    errs.append(f"{where}: href ภายนอกไม่ได้")
            if an == "id":
                errs.append(f"{where}: ห้ามตั้ง id ใน SVG (ซ้ำกันข้ามภาพ) — ใช้ path ใน <animateMotion path=…> แทน")
        for c in (el.get("class") or "").split():
            if c not in ALLOWED:
                seen.add(c)
        ds, dx = el.get("data-s"), el.get("data-x")
        for nm, v in (("data-s", ds), ("data-x", dx)):
            if v is not None and (not v.isdigit() or not 1 <= int(v) <= n):
                errs.append(f"{where}: {nm}=\"{v}\" ต้องเป็นเลข 1–{n}")
        if ds and "pl" in (el.get("class") or "").split():
            errs.append(f"{where}: อย่าใส่ class pl บน element ที่มี data-s (ห่อด้วย <g data-s> แล้วใส่ pl ข้างใน)")
    if seen:
        errs.append(f"{where}: class ที่ไม่มีในธีม: {sorted(seen)} · ใช้ได้: {' '.join(sorted(ALLOWED))}")
    steps_used = {int(e.get("data-s")) for e in root.iter() if (e.get("data-s") or "").isdigit()}
    missing = [k for k in range(2, n + 1) if k not in steps_used]
    if missing:
        errs.append(f"{where}: ขั้น {missing} ไม่มี element data-s ของตัวเอง (ทุกขั้น 2..{n} ต้องมีอะไรโผล่ใหม่)")
    return errs


def check(data_dir, path):
    a = json.load(open(path, encoding="utf-8"))
    errs, warns = [], []
    st = a.get("set")
    try:
        secs = load_sections(data_dir, st)
    except Exception as e:
        return [f"set '{st}' โหลดไม่ได้: {e}"], []
    keys = set()
    per_sec = {}
    for i, it in enumerate(a.get("items", [])):
        w = f"items[{i}]"
        s = secs.get(it.get("sec"))
        if not s:
            errs.append(f"{w}: ไม่มี section id '{it.get('sec')}' ใน {st}")
            continue
        aft = it.get("after", "")
        if aft and aft.strip() not in headings(s["md"]):
            errs.append(f"{w}: ไม่พบหัวข้อ '{aft}' ใน {s['id']} · มี: {headings(s['md'])}")
        an = it.get("anim") or {}
        k = an.get("key", "")
        w = f"{w} [{k}]"
        if not re.match(r"^[a-z0-9][a-z0-9-]{2,40}$", k):
            errs.append(f"{w}: key ต้องเป็น a-z0-9- ยาว 3–41")
        if k in keys:
            errs.append(f"{w}: key ซ้ำ")
        keys.add(k)
        if k in (s.get("anims") or {}):
            errs.append(f"{w}: key ชนกับที่มีอยู่ใน section")
        if not an.get("title"):
            errs.append(f"{w}: ไม่มี title")
        steps = an.get("steps") or []
        if not 3 <= len(steps) <= 7:
            errs.append(f"{w}: ควรมี 3–7 ขั้น (ได้ {len(steps)})")
        for j, sp in enumerate(steps):
            if not sp.get("t") or len(sp["t"]) > 70:
                errs.append(f"{w}: steps[{j}].t ว่างหรือยาวเกิน 70")
            if not sp.get("cap") or len(sp["cap"]) > 360:
                errs.append(f"{w}: steps[{j}].cap ว่างหรือยาวเกิน 360")
        errs += check_svg(an.get("svg", ""), max(len(steps), 1), w)
        per_sec[s["id"]] = per_sec.get(s["id"], 0) + 1
    for sid, c in per_sec.items():
        if c > 2:
            warns.append(f"{sid}: มีภาพเคลื่อนไหว {c} ภาพใน section เดียว (ปกติ 1–2)")
    for i, m in enumerate(a.get("mnem", [])):
        w = f"mnem[{i}] {m.get('name','')}"
        if m.get("sec") not in secs:
            errs.append(f"{w}: ไม่มี section id '{m.get('sec')}'")
        for f in ("name", "what", "src"):
            if not m.get(f):
                errs.append(f"{w}: ไม่มี {f}")
        ls = m.get("lines")
        if not isinstance(ls, list) or not ls or not all(isinstance(x, list) and len(x) == 2 and all(isinstance(y, str) and y for y in x) for x in ls):
            errs.append(f"{w}: lines ต้องเป็น [[คำ, ความหมาย], ...] ไม่ว่าง")
    lecs = {}
    for it in a.get("items", []):
        lecs.setdefault(it.get("sec", "").rsplit("-", 1)[0], 0)
        lecs[it.get("sec", "").rsplit("-", 1)[0]] += 1
    return errs, warns


PREVIEW_JS = r'''
const { chromium } = require(require.resolve('playwright', {paths:[require('child_process').execSync('npm root -g').toString().trim()]}));
const [base, specPath, out] = process.argv.slice(2);
const spec = JSON.parse(require('fs').readFileSync(specPath, 'utf8'));
const open = async (pg, sec) => { await pg.goto(base + '#' + spec.set + '-' + spec.lecOf[sec]); await pg.waitForTimeout(900);
  await pg.click(`[data-sec="${sec}"]`); await pg.waitForTimeout(500); };
(async()=>{
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const errs = [];
  for (const scheme of ['light','dark']) {
    const ctx = await b.newContext({viewport:{width:430,height:1000}, deviceScaleFactor:2, colorScheme:scheme, reducedMotion:'reduce'});
    const pg = await ctx.newPage(); pg.on('pageerror', e=>errs.push(e.message));
    for (const it of spec.items) {
      await open(pg, it.sec);
      const f = await pg.$(`figure.anim[data-ak="${it.anim.key}"]`);
      if (!f) { errs.push('ไม่เจอภาพ ' + it.anim.key + ' ในหน้า ' + it.sec); continue; }
      const n = it.anim.steps.length;
      const list = scheme === 'light' ? [...Array(n).keys()].map(i=>i+1) : [n];
      for (const i of list) {
        await f.$eval(`[data-astep="${i}"]`, el=>el.click()); await pg.waitForTimeout(150);
        await f.scrollIntoViewIfNeeded();
        await f.screenshot({path: `${out}/${it.anim.key}-${scheme==='light'?'s'+i:'dark'}.png`});
      }
    }
    if (scheme === 'light') for (const sec of [...new Set((spec.mnem||[]).map(m=>m.sec))]) {
      await open(pg, sec);
      const m = await pg.$('.mnem'); if (m) { await m.scrollIntoViewIfNeeded(); await m.screenshot({path:`${out}/mnem-${sec}.png`}); }
      else errs.push('ไม่เจอกล่องหลักจำใน ' + sec);
    }
    await ctx.close();
  }
  console.log(JSON.stringify({errors: errs}));
  await b.close();
})();
'''


def preview(data_dir, page, path, out, port=8790):
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    import patch_learn_anim as P
    a = json.load(open(path, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    root = tempfile.mkdtemp(prefix="animprev-")
    adir = os.path.join(root, "_a")
    os.makedirs(adir)
    shutil.copy(path, adir)
    P.patch_data(data_dir, adir, os.path.join(root, "data"))
    open(os.path.join(root, "index.html"), "w", encoding="utf-8").write(P.patch_page(open(page, encoding="utf-8").read()))
    d = json.load(open(os.path.join(data_dir, a["set"] + ".json"), encoding="utf-8"))
    a["lecOf"] = {s["id"]: re.sub(r"[^A-Za-z0-9._~-]", ".", L["lec"]) for L in d for s in L["sections"]}
    path = os.path.join(root, "spec.json")
    json.dump(a, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    js = os.path.join(root, "prev.js")
    open(js, "w").write(PREVIEW_JS)
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", root],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        import time
        time.sleep(0.8)
        r = subprocess.run(["node", js, f"http://127.0.0.1:{port}/index.html", path, out], capture_output=True, text=True, timeout=600)
        print(r.stdout.strip() or r.stderr.strip()[-2000:])
    finally:
        srv.terminate()
        shutil.rmtree(root, ignore_errors=True)
    print("ภาพอยู่ที่", out)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "check":
        e, w = check(sys.argv[2], sys.argv[3])
        for x in w:
            print("เตือน:", x)
        for x in e:
            print("ผิด:", x)
        print("ผ่าน" if not e else f"ไม่ผ่าน {len(e)} จุด")
        sys.exit(1 if e else 0)
    elif len(sys.argv) in (6, 7) and sys.argv[1] == "preview":
        preview(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]) if len(sys.argv) == 7 else 8790)
    else:
        sys.exit(__doc__)
