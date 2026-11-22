# Step animations + reading guide — spec for writers

You add two things to each assigned lecture file in `/tmp/claude-0/-home-user-ioioioio/4a8e7fa6-56da-5a1d-895e-ef4b716ded4e/scratchpad/parts/<course>_<lec>.json`:
(A) 1–2 **step-by-step mechanism animations** per lecture, and (B) a lecture-level **reading guide** (`reading`).
Edit with a Python script (json.load → modify → json.dump(ensure_ascii=False, indent=1)). Change nothing else: do not touch existing `figs`, `items`, `meq`, `osce`, ids, answers, or md text (except inserting the `[[anim:key]]` line). Other agents edit other files at the same time — only touch your assigned files; keep helper scripts in `.../scratchpad/animwork/<your-tag>/`.
All diagrams must be ORIGINAL schematics designed from the lesson content — do not trace or reproduce figures from Schwartz or any book. Reading-guide text is your own Thai; Schwartz section names may be cited by their heading titles only.

## (A) Animations
The engine plays an SVG step by step (auto-play with ‹ ⏸ › buttons and step dots; a caption per step under the picture; also shown on present-mode slides). It is the same SVG class system as the static figures — read `tools/FIG_SPEC.md` first for the SVG rules (viewBox width 420 ≤ 440, classes only, no hard-coded colours, Thai text spacing, arrows/markers).

Data: `section["anims"] = {"<key>": {"title": "...", "svg": "<svg ...>", "steps": [{"t": "short step title", "cap": "1–2 Thai sentences, **bold** key terms"}, ...]}}` and a line `[[anim:<key>]]` (own line, blank lines around) inside the `###` block it explains. If that block already holds a `[[fig:...]]` of the same idea, put the animation in a different block or pick another mechanism — don't show the same picture twice.

Step mechanics:
- `data-s="k"` on an element = it appears at step k (hidden before). Elements without data-s are always visible (use for a fixed frame/anatomy).
- `data-x="k"` = it disappears from step k on (use to swap a "before" state for an "after" state, e.g. normal vessel → occluded vessel).
- The element appearing at the current step fades in; earlier ones stay.
- Motion classes: `fl` on a line/path = flowing dashes along it (blood/fluid/signal flow; add `rv` to reverse, `sl` to slow); `pl` = gentle pulse (use for "this is the problem" — e.g. ischemic tissue). **An element with `pl` must not carry data-s/data-x** — wrap it: `<g data-s="3"><rect class="bad pl" .../></g>`. Group several elements of one step in a `<g data-s="k">`.
- 4–7 steps (max 9). Every step should reveal or change something. The final step usually shows where treatment acts (`ok`), or the full loop closed.
- Keep labels from different steps from overlapping when both are visible; the checker renders every step separately.

Choose mechanisms that are truly sequential or cyclic — cascades, feedback loops (lethal triad, compartment syndrome, ICP), flow changes (shunts, portal hypertension, obstruction → strangulation), time courses (wound healing phases, burn shock), or an approach algorithm walked step by step (NL3). Per track: n12 pathophysiology cascades; n3 bedside sequence with the mechanism behind each step; res mechanism → classification/decision with thresholds.
Count: **1 per lecture, 2 when the lecture has two major dynamic mechanisms** (aim ~1.3 average).

Worked example (passes checks): `tools/example_anim.json`, rendered steps in `.../scratchpad/shots/anim/`.

## (B) Reading guide — `lecture["reading"]`
```json
"reading": {
  "minutes": 90,                                   // realistic total for this lecture incl. questions
  "start": "1–2 Thai sentences: how to approach this lecture (what to grasp first, what to skip on a first pass)",
  "order": [ {"sec": "<section id>", "level": "must", "why": "short Thai reason"}, ... ],   // EVERY section exactly once, in the recommended reading order (may differ from file order); level must|extra
  "schwartz": [ {"ch": "Ch 5", "part": "section heading in the chapter (English, as titled)", "why": "Thai: what to read it for"} ],   // 2–4 items; grep the chapter file to get real heading names
  "beyond": [ "**Guideline/trial name (year)** — Thai: why it matters" ],   // 2–4 items; current guidelines/landmark trials relevant to this group's level; only ones you are confident exist
  "tips": [ "Thai: a pattern the exam asks / a trap" ]     // 3–5 items, specific to this group's exam (n12: NL1-2 MCQ · n3: MEQ/OSCE critical points · res: ABSITE/board)
}
```
`level`: "must" = core for this group's exam; "extra" = deeper/optional. Usually 2–3 must per lecture.

## Checks (each lecture must pass all, 0 errors/problems)
- `python3 -I tools/figlint.py <file>` (now also checks animations and the reading guide)
- `node tools/figrender.js <file> [--png <dir>]` (renders every figure AND every animation step; view a few step PNGs)
- `python3 -I /home/user/ioioioio/surgery/validate.py <file>`
