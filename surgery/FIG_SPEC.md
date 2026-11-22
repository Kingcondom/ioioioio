# Pathophysiology diagrams — spec for figure writers

Goal: the app's lessons are text-heavy. Add **structural diagrams (inline SVG)** so the mechanism / structure of each topic can be seen at a glance instead of read as paragraphs — like the sister app NL1 learn. The engine already renders them (theme-aware colours, dark mode, "ปิดป้าย · ทายเอง" label-cover quiz, and present-mode slides use them).

All diagrams must be ORIGINAL schematics you design from the lesson content. Do not trace or reproduce figures/tables from Schwartz or any other book.

## Where the data lives
Lecture files: `/tmp/claude-0/-home-user-ioioioio/4a8e7fa6-56da-5a1d-895e-ef4b716ded4e/scratchpad/parts/<course>_<lec>.json` (one lecture object; `sections[]` each have `id`, `title`, `md`, ...). Edit them in place with a Python script (json.load → modify → json.dump(ensure_ascii=False, indent=1)). Do NOT change anything except: add `figs`, insert `[[fig:key]]` lines into `md`, and (optional) shorten a paragraph the diagram now fully shows (keep every number/threshold that is not in the diagram). Never touch `items`, `meq`, `osce`, ids or answers.

## How to add a figure
1. `section["figs"] = {"<key>": {"title": "...", "cap": "...", "svg": "<svg ...>...</svg>"}}` — key: lowercase letters/digits/`_`/`-`, unique within the section.
2. Put a line containing exactly `[[fig:<key>]]` in `md` (its own line, blank line before and after), placed inside the `###` block it illustrates — usually right after that block's first sentence/paragraph. Each `###` block is one present-mode slide, so the diagram should sit in the block whose idea it shows.
3. `title`: short Thai/English title (e.g. "Septic shock: จาก PAMP ถึง hypotension"). `cap`: 1–2 Thai sentences saying how to read the diagram, **bold** the key terms (the cap is hidden while labels are covered).

Count: **1 figure per section (required), a 2nd only when the section has a second, clearly different mechanism.**

## What to draw (per track)
- `n12` (NL1-2): pathophysiology chains — trigger → mechanism → physiological change → clinical signs/lab → why the treatment works (treatment hits which arrow). Or a labelled anatomy schematic when anatomy is the point (e.g. hernia canal, Calot triangle, portal circulation).
- `n3` (NL3): the pathophysiology behind the bedside approach — e.g. why the patient is hypotensive and where each intervention acts; or an approach flowchart whose branches are explained by mechanism (finding → meaning → action).
- `res` (Resident): mechanism + decision structure — e.g. the pathophysiology that underlies a classification and what each class means for operative choice; complication cascades; algorithms with thresholds.
Prefer a causal structure (boxes + arrows, feedback loops, compartments, before/after) over a text box list. Every box short: 1–4 words per line, ≤3 lines.

## SVG rules (the engine styles SVG through CSS classes — never hard-code colours)
- Root: `<svg viewBox="0 0 W H" role="img" aria-label="Thai one-line description" xmlns="http://www.w3.org/2000/svg">`. **W = 420 (max 440)** so it fits a phone without scrolling; H as needed (160–420). No width/height attributes, no `<style>`, no `fill="#..."`/`stroke="#..."`/`style="fill..."`, no `<image>`, no fonts, no scripts, no `<foreignObject>`.
- Shapes default to outline. Fill/stroke classes (put on rect/circle/ellipse/path/polygon):
  `bx` plain box · `sk` sunk/neutral · `ac` accent (key step) · `ok` good/normal/treatment · `bad` harmful/danger · `ms` warning/compensation · `wa` blue/neutral-alt (e.g. fluid, venous) ·
  solid fills (small markers/bars): `acf okf badf msf waf inkf muf ruf paf` ·
  lines (path/line/polyline): `ln lmu lac lok lbad lms lwa lru` + width `w2 w3 w5` + `da` dashed / `dt` dotted.
- Text: `<text x y class="...">` default 13px. Size `lg`(15) `sm`(11.5) `xs`(10.5); `b` bold; anchor `mid` / `end`; colour `mu` `i2` `tac` `tok` `tbad` `tms` `twa` `tpa`.
  Multi-line: `<text x="" y="" class="xs"><tspan x="SAME_X" dy="0">line1</tspan><tspan x="SAME_X" dy="1.25em">line2</tspan></text>`.
  Thai glyphs are tall: give each text line ≥ 14px vertical room (xs) / 16px (13px text). Keep text ≥ 6px inside its box and inside the viewBox. Estimate width ≈ 0.55 × font-size per character (Thai ≈ 0.6).
- Arrows: `<path d="M.. L.." class="ln" marker-end="url(#ah)"/>`; coloured heads: `#ah-ac #ah-ok #ah-bad #ah-ms #ah-wa #ah-mu` matching the line class (`lac`→`#ah-ac`, …). End arrows 4–6px before the target box edge.
- Rounded boxes `rx="6"`. Use colour by meaning (bad = injury/danger, ok = treatment/normal, ms = compensation, ac = central step), not decoration. Always pair colour with a word or ↑ ↓ (colour alone must not carry meaning).
- Keep it legible: ≤ ~14 boxes, labels in Thai/English mixed as clinicians speak (e.g. "preload ↓", "lactate ↑").

## Check before you finish each lecture
`python3 -I tools/figlint.py <file>` (static rules) and
`node tools/figrender.js <file>` (renders every figure in Chromium; reports text outside the viewBox, text sticking out of its box, and overlapping labels). Fix until both report 0 problems. Also run `python3 -I /home/user/ioioioio/surgery/validate.py <file>`.
Optionally look at a PNG: `node .../figrender.js <file> --png <outdir>` writes one PNG per figure (use the Read tool to view a few).

## Worked example (passes both checks)
`tools/example_fig.json` — hemorrhagic shock chain (420×250, 8 boxes, compensation in `ms`, harm in `bad`, central concept `ac`, treatment `ok`). Its rendered PNG: `.../scratchpad/shots/fig/x-00-1_hemo.png`. Match this density and legibility; vary layout to fit each mechanism (loops, compartments, branching flowcharts, anatomy outlines).

Work one lecture at a time (write figures → run both checks → fix → next lecture). Other agents edit other lecture files at the same time: only touch the files assigned to you, and keep your helper scripts in your own folder `.../scratchpad/figwork/<your-tag>/`.
