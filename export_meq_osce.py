#!/usr/bin/env python3
"""
export_meq_osce.py — รวมข้อสอบ MEQ และ OSCE/SAQ ทั้งหมดเป็นไฟล์ Markdown ไฟล์เดียว

    python3 export_meq_osce.py        # -> export/MEQ_OSCE.md

ภาค 1  ข้อใหม่ในคิท (data/<ระบบ>_meq_osce.json) พร้อมเฉลยเต็ม แยก MEQ / OSCE
ภาค 2  ข้อสอบเก่าจากโพย MED28–MED35 คัดตามต้นฉบับ ตามช่วงบรรทัดใน sources/meq_osce_index.json
ภาค 3  หัวข้อ MEQ/OSCE ที่เคยออก (สรุปจาก data/<ระบบ>_hot.json)
ภาคผนวก  MEQ ร่างใน attic/ ที่ยังไม่ได้ยุบเข้าชุด
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
os.chdir(ROOT)
CFG = json.load(open('config.json', encoding='utf-8'))
NL_PATH = CFG.get('nl_reference_file', 'refs/nl_2567.json')
NL = json.load(open(NL_PATH, encoding='utf-8')).get('entries', {}) if os.path.exists(NL_PATH) else {}
INDEX = 'sources/meq_osce_index.json'
ATTIC = 'attic/respiratory_extra_items.json'
OUT = 'export/MEQ_OSCE.md'
SETS = [s for s in CFG['sets'] if s.get('meq')]


def load_many(paths):
    out = []
    for p in paths:
        d = json.load(open(p, encoding='utf-8'))
        out += d['items'] if isinstance(d, dict) else d
    return out


def br(text):
    """ขึ้นบรรทัดใหม่ตามต้นฉบับ (hard line break ของ Markdown)"""
    return '  \n'.join(l.rstrip() for l in text.strip().split('\n'))


def nl_text(codes):
    rows = []
    for c in codes or []:
        e = NL.get(c)
        rows.append('%s %s' % (c, e.get('title', '')) if e else c)
    return ' · '.join(rows)


def anchor(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).strip().replace(' ', '-')


# ---------- ภาค 1: ข้อใหม่ในคิท ----------

def kit_item(it, setlabel):
    L = ['#### %s · %s' % (it['id'], it.get('topic', '')),
         '*%s · Lecture %s · %s*' % (setlabel, it.get('lec', ''), it.get('lecture', '')), '']
    if it.get('station'):
        L += ['**สถานี:** ' + it['station'], '']
    if it.get('vignette'):
        L += ['**โจทย์**', '', br(it['vignette']), '']
    if it.get('instruction'):
        L += ['**คำสั่ง:** ' + br(it['instruction']), '']
    for q in it.get('questions') or []:
        L += ['**' + q['q'].strip() + '**', '', '> **เฉลย**', '', q['a'].strip(), '']
    if isinstance(it.get('answer'), str):
        L += ['**เฉลย / เกณฑ์ให้คะแนน**', '', it['answer'].strip(), '']
    if it.get('pearl'):
        L += ['**Pearl:** ' + it['pearl'], '']
    refs = it.get('ref') or []
    if isinstance(refs, str):
        refs = [refs]
    if refs:
        L += ['**ที่มา:**'] + ['- ' + r for r in refs] + ['']
    if it.get('nl'):
        L += ['**NL 2567:** ' + nl_text(it['nl']), '']
    L += ['---', '']
    return L


# ---------- ภาค 2: ข้อสอบเก่าตามต้นฉบับ ----------

# PDF บางหน้าแตกไม้โทออกจากพยัญชนะ ("ข ้อ" -> "ข้อ") — แก้เฉพาะกรณีนี้
# ช่องว่างหน้าสระ/วรรณยุกต์อื่น ๆ มักแทนตัว ห/ส ที่หายไป ("ใ ้" = ให้) จึงปล่อยไว้ตามต้นฉบับ
FIX_SPACE = re.compile(r'(?<=[ก-ฮ]) +(?=้)')
LIGATURES = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl'}


def clean_line(line):
    s = re.sub(r'[\x00-\x08\x0b-\x1f\x7f-\x9f]', '', line.rstrip())
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = FIX_SPACE.sub('', s).replace('ป่ วย', 'ป่วย').lstrip()
    if re.fullmatch(r'[=\-_*]{3,}', s):            # เส้นคั่น — กันไม่ให้กลายเป็นหัวข้อ setext / hr
        return '\\' + s
    if re.match(r'#{1,6}(\s|$)', s) or s.startswith('>') or re.match(r'\+\s', s):
        s = '\\' + s
    s = re.sub(r'<(?=[A-Za-z/!])', '&lt;', s)       # กันโดนตีความเป็นแท็ก HTML
    if s.count('**') % 2:                            # ดอกจันไม่ครบคู่ — กันตัวหนาลามข้ามบรรทัด
        s = s.replace('*', '\\*')
    return s


# หน้าโพย MED30 บางหน้าฟอนต์เพี้ยน: อังกฤษกลายเป็นอักษรละตินขยาย ไทยกลายเป็นซีริลลิก
# ถอดกลับด้วยตารางนี้ (ตัว C ใหญ่ถูกแปลงเป็นช่องว่าง จึงเดาจากบริบท)
CYR_LATIN = dict(zip('\xf1\u010e\u0110\u0117\u011f\u0139\u013a\u0142\u0148\u0158\u015b\u015f\u0168\u016a'
                     '\u0175\u0198\u019a\u019b\u01a3\u01af\u01b7\u01cf\u01d0\u01d5\u01d6\u01e1',
                     'abcdefghijklmnopqrstuvwxyz'))
CYR_LATIN.update({
    '0': 'E', 'I': 'G', 'P': 'H', 'e': 'J', 'g': 'K', 's': 'M', 'u': 'N', '\xae': 'S', '\xbb': 'T',
    '\xc2': 'U', '\xda': 'W', '\xd9': 'V', '\xa3': 'P', '\xa6': 'R', 'i': 'L', "'": 'D', 'U': 'I',
    'H': 'F', '\x01': 'A', '\x1e': 'B', '\xdf': 'X', '\xa5': 'Q', '\u01ea': 'fl', '\u01e9': 'fi',
    '\u0351': ' ', '\u0322': '.', '\u0324': ':', '\u0329': '?', '\u0323': ',', '\u0325': '\u2192',
    '\u0372': '+', '\u0378': '>', '\u0376': '=', '\u0332': '(', '\u0333': ')', '\u0338': '-', '\u032f': '/'})
CYR_LATIN.update({chr(0x2ec + i): str(i) for i in range(10)})
CYR_THAI_LOW = {0xe50: '\u0e16', 0xe62: '\u0e48', 0xe63: '\u0e49', 0xe64: '\u0e4a', 0xe65: '\u0e4b',
                0xe66: '\u0e4c'}
CYR_FIXES = [('\u0e40\u0e0a\u0e48\u0e19  PD', '\u0e40\u0e0a\u0e48\u0e19 COPD'), ('1. BC 2.', '1. CBC 2.'),
             ('\u0e2d\u0e48\u0e32\u0e19E G', '\u0e2d\u0e48\u0e32\u0e19 EKG')]   # ตัวที่หายไปทั้งตัว
SARA_AM = [('\u0e4d\u0e48\u0e32', '\u0e48\u0e33'), ('\u0e4d\u0e49\u0e32', '\u0e49\u0e33'),
           ('\u0e4d\u0e32', '\u0e33')]


def cyr_garbled(s):
    n = sum(1 for ch in s if 0x100 <= ord(ch) <= 0x52f)
    return len(s) > 3 and n / len(s) > 0.3


def decode_cyr(s):
    out = []
    for i, ch in enumerate(s):
        if ch == ' ':
            prv = CYR_LATIN.get(s[i - 1], '') if i else ' '
            nxt = CYR_LATIN.get(s[i + 1], '') if i + 1 < len(s) else ' '
            lost_c = (prv in (' ', '-', '(') and nxt.isalpha()) or \
                     (prv.isalpha() and prv.isupper() and not nxt.isalpha())
            out.append('C' if lost_c else ' ')
        elif ch in CYR_LATIN:
            out.append(CYR_LATIN[ch])
        elif 0x400 <= ord(ch) <= 0x4ff:
            d = ord(ch) + 0x9cd
            if d in CYR_THAI_LOW:
                out.append(CYR_THAI_LOW[d])
                continue
            out.append(chr(d + 4 if 0xe3c <= d <= 0xe5b else d))
        else:
            out.append(ch)
    t = ''.join(out)
    for a, b in SARA_AM + CYR_FIXES:
        t = t.replace(a, b)
    return t


# หน้าโพย MED29 บางหน้าไทยเป็นรหัส TIS-620 ที่ถูกเลื่อน: ตัวต้น/สระลอย -0x1D, สระหน้า/วรรณยุกต์ -0x1F
# (บางตัวตกไปอยู่ช่วงอักขระควบคุมจึงมองไม่เห็นในไฟล์) และวรรณยุกต์ตัวล่างกลายเป็น n o p q
TONE_LOW = dict(zip('nopq', '\u0e48\u0e49\u0e4a\u0e4b'))


def decode_tis(s):
    out = []
    for i, ch in enumerate(s):
        o = ord(ch)
        thai_before = bool(out) and '\u0e01' <= out[-1] <= '\u0e5b'
        nxt, nxt2 = s[i + 1:i + 2], s[i + 2:i + 3]
        if ch == ' ' and thai_before and nxt and (0x80 <= ord(nxt) <= 0xff or (
                nxt in TONE_LOW and not (nxt2.isascii() and nxt2.isalpha()))):
            out.append('\u0e02')  # ข ตกไปที่ U+0085 แล้วถูกแปลงเป็นช่องว่าง
            continue
        elif 0xc1 <= o <= 0xff:
            tis = o + 0x1f
        elif 0x80 <= o <= 0xc0 or (o < 0x20 and ch not in '\t\n\x0c'):
            tis = o + 0x1d
        elif ch in TONE_LOW and thai_before:
            out.append(TONE_LOW[ch])
            continue
        else:
            out.append(ch)
            continue
        out.append(chr(tis + 0xd60) if 0xa1 <= tis <= 0xfb else chr(tis) if tis < 0x80 else '')
    t = ''.join(out)
    for a, b in SARA_AM:
        t = t.replace(a, b)
    return t


def verbatim(path, start, end, font=None):
    lines = open(path, encoding='utf-8').read().split('\n')[start - 1:end]
    out, prev_blank = [], True
    for raw in lines:
        if cyr_garbled(raw):
            raw = decode_cyr(raw)
        elif font == 'tis' and re.search(r'[\x01-\x08\x0b\x0d-\x1f\x80-\xff]', raw):
            raw = decode_tis(raw)
        s = clean_line(raw)
        if not s:
            if not prev_blank:
                out.append('')
            prev_blank = True
            continue
        out.append(s + '  ')
        prev_blank = False
    while out and not out[-1]:
        out.pop()
    if out:
        out[-1] = out[-1].rstrip()
    return out


BATCH_ORDER = ['MED35', 'MED34', 'MED33', 'MED32', 'MED31', 'MED30', 'MED29', 'MED28']


def batch_key(b):
    return BATCH_ORDER.index(b) if b in BATCH_ORDER else len(BATCH_ORDER)


# ---------- ประกอบไฟล์ ----------

def main():
    kit = {s['key']: load_many(s['meq']) for s in SETS}
    meq = [(s, it) for s in SETS for it in kit[s['key']] if it.get('part') == 'MEQ']
    osce = [(s, it) for s in SETS for it in kit[s['key']] if it.get('part') != 'MEQ']
    index = json.load(open(INDEX, encoding='utf-8')) if os.path.exists(INDEX) else {'blocks': []}
    blocks = [b for b in index['blocks'] if not b.get('duplicate_of')]
    blocks.sort(key=lambda b: (batch_key(b['batch']), b['file'], b['start']))
    attic = json.load(open(ATTIC, encoding='utf-8')) if os.path.exists(ATTIC) else {'items': []}
    attic_meq = [it for it in attic['items'] if (it.get('type') or it.get('part')) in ('meq', 'MEQ')]

    L = ['# MED421 · รวมข้อสอบ MEQ และ OSCE/SAQ ทั้งหมด', '',
         'ไฟล์นี้สร้างจาก `export_meq_osce.py` — แก้ข้อมูลที่ต้นทางแล้วสั่งรันใหม่ อย่าแก้ไฟล์นี้ตรง ๆ', '',
         '| ส่วน | เนื้อหา | จำนวน |', '|---|---|---|',
         '| ภาค 1.1 | MEQ ข้อใหม่ในคิท (เฉลยเต็ม) | %d ข้อ |' % len(meq),
         '| ภาค 1.2 | OSCE/SAQ ข้อใหม่ในคิท (เฉลยเต็ม) | %d ข้อ |' % len(osce),
         '| ภาค 2 | ข้อสอบ MEQ/OSCE/SAQ เก่าจากโพย MED28–MED35 (ตามต้นฉบับ) | %d ช่วง |' % len(blocks),
         '| ภาค 3 | หัวข้อ MEQ/OSCE ที่เคยออก แยกรายคาบ | %d คาบ |'
         % sum(len(load_many(s.get('hot', []))) for s in SETS),
         '| ภาคผนวก | MEQ ร่างใน attic/ ที่ยังไม่ได้ยุบเข้าชุด | %d ข้อ |' % len(attic_meq), '',
         '---', '']

    # ภาค 1
    L += ['## ภาค 1 · ข้อใหม่ในคิท (Cardio · Nephro · Chest · AIR)', '',
          'เฉลยภาษาไทยเต็มทุกข้อ ใต้แต่ละข้อบอกว่าอิงข้อสอบเก่ารุ่นไหน และผูกเกณฑ์ NL 2567 ไว้', '']
    for title, rows in (('1.1 MEQ', meq), ('1.2 OSCE/SAQ', osce)):
        L += ['### %s (%d ข้อ)' % (title, len(rows)), '']
        L += ['| รหัส | ระบบ | หัวข้อ |', '|---|---|---|']
        L += ['| %s | %s | %s |' % (it['id'], s['label'], it.get('topic', '').replace('|', '/'))
              for s, it in rows]
        L += ['']
        for s, it in rows:
            L += kit_item(it, s['label'])

    # ภาค 2
    L += ['## ภาค 2 · ข้อสอบเก่าจากโพย MED28–MED35 (ตามต้นฉบับ)', '',
          'คัดเฉพาะส่วน MEQ / OSCE / SAQ จาก `sources/` เรียงจากรุ่นล่าสุด ข้อความคงตามต้นฉบับ'
          ' (แก้แค่ช่องว่างหน้าวรรณยุกต์ที่ PDF แตกออก) — เป็นการจำข้อสอบของนักศึกษา'
          ' เฉลยบางข้อไม่ตรงแนวทางปัจจุบัน ให้ตรวจกับภาค 1 อีกที หน้าที่ซ้ำกันในโพยตัดออกแล้ว', '']
    if blocks:
        L += ['| รุ่น | การสอบ | ชนิด | เคส/หัวข้อ |', '|---|---|---|---|']
        L += ['| %s | %s | %s | %s |' % (b['batch'], b['exam'], b['kind'], b['title'].replace('|', '/'))
              for b in blocks]
        L += ['']
    cur = None
    for b in blocks:
        if b['batch'] != cur:
            cur = b['batch']
            L += ['### %s' % cur, '']
        L += ['#### [%s] %s — %s' % (b['kind'], b['exam'], b['title']),
              '*ต้นฉบับ: `%s` บรรทัด %d–%d*' % (b['file'], b['start'], b['end']), '']
        if b.get('font') == 'cyr':
            L += ['*หน้านี้ฟอนต์ในโพยเพี้ยน ถอดกลับด้วยตารางแปลงอักษร อาจมีตัวสะกดผิดบางตัว*', '']
        elif b.get('font') == 'tis':
            L += ['*หน้านี้รหัสภาษาไทยในโพยเพี้ยน ถอดกลับด้วยการเลื่อนรหัส TIS-620 อาจมีตัวสะกดผิดบางตัว*', '']
        L += verbatim(b['file'], b['start'], b['end'], b.get('font'))
        L += ['', '---', '']

    # ภาค 3
    L += ['## ภาค 3 · หัวข้อ MEQ/OSCE ที่เคยออก (สรุปรายคาบ)', '']
    for s in SETS:
        hot = load_many(s.get('hot', []))
        if not hot:
            continue
        L += ['### %s (%s)' % (s['label'], s['thai']), '']
        for h in hot:
            L += ['**Lec %s · %s** — %s' % (h['lec'], h['lecture'], h.get('level', '')), '']
            for title, key in (('MEQ', 'meq'), ('OSCE/SAQ', 'osce')):
                for x in h.get(key) or []:
                    L += ['- *%s:* %s' % (title, x)]
            if h.get('seen'):
                L += ['- *เจอในโพย:* ' + h['seen']]
            L += ['']

    # ภาคผนวก
    if attic_meq:
        L += ['---', '', '## ภาคผนวก · MEQ ร่างใน attic/ (ยังไม่ได้ยุบเข้าชุด Chest)', '',
              'ร่างรุ่นแรกจาก `%s` — เฉลยยังเป็นภาษาอังกฤษ และยังไม่ผ่านการตรวจตาม SPEC.md' % ATTIC, '']
        for it in attic_meq:
            L += ['#### attic/%s · %s' % (it['id'], it.get('topic', '')), '',
                  '**โจทย์**', '', br(it.get('scenario', '')), '']
            for n, q in enumerate(it.get('questions') or [], 1):
                pts = ' (%s คะแนน)' % q['points'] if q.get('points') else ''
                L += ['**%d. %s**%s' % (n, q['q'], pts), '', '> **เฉลย**', '', q['a'], '']
            if it.get('pearl'):
                L += ['**Pearl:** ' + it['pearl'], '']
            if it.get('ref'):
                L += ['**ที่มา:** ' + (it['ref'] if isinstance(it['ref'], str) else ' | '.join(it['ref'])), '']
            L += ['---', '']

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write('\n'.join(L).rstrip() + '\n')
    print('  ✓ %s  %d KB · MEQ %d · OSCE/SAQ %d · โพยเก่า %d ช่วง · attic %d'
          % (OUT, os.path.getsize(OUT) / 1024, len(meq), len(osce), len(blocks), len(attic_meq)))


if __name__ == '__main__':
    main()
