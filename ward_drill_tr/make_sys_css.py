# -*- coding: utf-8 -*-
"""สร้าง sys_colors.css — สีประจำระบบ 12 ระบบ (ผู้ใช้ขอ 13 พ.ย. 2569)
ธีม Teaching Round ใช้ตัวแปร --lime/--lime-2/--lime-3/--on-lime/--pen ทั้งหน้า
ไฟล์นี้แค่สลับค่าชุดนั้นตามระบบ: ทั้งหน้า (html[data-set]) และของที่เป็นของระบบนั้นเอง (.sys-<key>)"""
import os
# key: (hue, ตัวคูณความอิ่มสี)
SYS = {'cardio': (352, 1), 'nephro': (178, 1), 'chest': (218, 1), 'neuro': (278, 1), 'air': (40, 1),
       'infect': (150, 1), 'gi': (22, 1), 'endo': (88, 1), 'heme': (322, 1), 'derm': (196, 1),
       'onco': (30, .4), 'mock': (248, 1)}
LIGHT = dict(lime=(70, 89), lime2=(62, 62), lime3=(55, 47), onl=(60, 16), pen=(65, 30), ona=(50, 10))
DARK = dict(lime=(32, 20), lime2=(55, 60), lime3=(60, 70), onl=(70, 90), pen=(70, 74), ona=(50, 10))
def block(h, k, P):
    c = lambda n: 'hsl(%d %d%% %d%%)' % (h, round(P[n][0] * k), P[n][1])
    return ('--lime:%s;--lime-2:%s;--lime-3:%s;--on-lime:%s;--pen:%s;'
            '--accent:var(--lime-2);--accent-soft:var(--lime);--accent-ink:var(--pen);--on-accent:%s'
            % (c('lime'), c('lime2'), c('lime3'), c('onl'), c('pen'), c('ona')))
out = ['/* ===================== สีประจำระบบ (ผู้ใช้ขอ 13 พ.ย. 2569) — สร้างจาก make_sys_css.py ===================== */']
for s, (h, k) in SYS.items():
    out.append(':root[data-set="%s"],.sys-%s{%s}' % (s, s, block(h, k, LIGHT)))
out.append('@media (prefers-color-scheme:dark){')
for s, (h, k) in SYS.items():
    out.append('  :root:not([data-theme="light"])[data-set="%s"],:root:not([data-theme="light"]) .sys-%s{%s}' % (s, s, block(h, k, DARK)))
out.append('}')
for s, (h, k) in SYS.items():
    out.append(':root[data-theme="dark"][data-set="%s"],:root[data-theme="dark"] .sys-%s{%s}' % (s, s, block(h, k, DARK)))
out.append(r'''
/* ข้อความสีเน้นบนพื้นขาว → ใช้สีเข้ม (--accent ตอนนี้เป็นสีกลาง อ่านไม่ชัดถ้าเป็นตัวหนังสือ) */
.qno,.tag.yr,.tag.old,.tag.pic,.nlchip,.panel h4,.nllist i,.brand-mark,.rvsub h3,a{color:var(--accent-ink)}
.qno,.tag.yr,.tag.old,.tag.pic,.nlchip{background:var(--accent-soft)}
/* การ์ดระบบหน้าแรก: แถบสีด้านบน + ป้ายชื่อสีระบบ + แถบความคืบหน้า */
.tr-card{box-shadow:inset 0 6px 0 var(--lime-2);padding-top:20px}
.tr-card.done{box-shadow:inset 0 6px 0 var(--lime-3)}
.tr-card.cur{box-shadow:inset 0 6px 0 var(--lime-2),0 0 0 2px var(--lime-3)}
.tr-c-no{align-self:start;justify-self:start;background:var(--lime);color:var(--on-lime);border-radius:999px;padding:2px 12px;font-size:18px;line-height:1.45}
.tr-c-day{background:var(--surface-sunk);color:var(--pen)}
.tr-c-bar{background:color-mix(in srgb,var(--lime) 60%,var(--rule))}
/* แถบเลือกระบบ: จุดสีหน้าชื่อ · ปุ่มที่เลือกเป็นพื้นสีระบบ */
#setbar .tab::before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--lime-2);margin-inline-end:8px;vertical-align:1px}
#setbar .tab[aria-selected="true"]{background:var(--lime);color:var(--on-lime)}
#setbar .tab[aria-selected="true"]::before{background:var(--lime-3)}
/* แถบซ้ายบนคอม: วงความคืบหน้าเป็นสีระบบ */
.tr-sd-c .mr{background:conic-gradient(var(--lime-3) calc(var(--p)*360deg),color-mix(in srgb,var(--lime-2) 45%,var(--rule)) 0)}
/* มือถือ 2 คอลัมน์: ชื่อระบบห้ามโดนตัด — ป้าย "กำลังทำ" ขึ้นบรรทัดใหม่แทน */
.tr-c-top{flex-wrap:wrap}.tr-c-no{flex:none;max-width:100%}
/* ป้ายระบบในโหมดรวมหลายระบบ (ข้อสอบแยกปี / มีรูป / คาบที่ทวน) */
.tag.sys[class*="sys-"]{background:var(--lime);color:var(--on-lime)}
/* หน้าต่างรายคาบของระบบ: หัวสีระบบ */
.tr-sheet[class*="sys-"] .tr-sh-head{box-shadow:inset 4px 0 0 var(--lime-2);padding-inline-start:12px}
''')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sys_colors.css'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('ok')
