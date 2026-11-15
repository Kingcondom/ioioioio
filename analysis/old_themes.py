"""จัดกลุ่มข้อสอบเก่า (data/*_old_*.json) ตาม "แก่น" ของโจทย์ แล้วดูว่าแต่ละรุ่นออกข้อใหม่ที่ไม่เคยอยู่ในโพยรุ่นก่อนกี่แก่น
รัน: python3 analysis/old_themes.py  → analysis/old_themes.json + analysis/old_themes.md
"""
import json, glob, re, collections, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ids(prefix, nums, w):
    return [f"{prefix}-OLD-{n:0{w}d}" for n in nums]
C  = lambda *n: ids('C', n, 2)
N  = lambda *n: ids('N', n, 3)
CH = lambda *n: ids('CH', n, 2)
A  = lambda *n: ids('AIR', n, 2)

# (ระบบ, แก่น, รายการข้อ)
THEMES = [
 ('Cardio','Pericarditis: วินิจฉัยจากท่าโน้มตัว + ECG ST ยกทุก lead / PR กด', C(1,3,4,14,108)),
 ('Cardio','Pericarditis: รักษาด้วย NSAID/aspirin + colchicine', C(2)+A(33)),
 ('Cardio','Cardiac tamponade: Beck triad, pulsus paradoxus, electrical alternans → pericardiocentesis', C(5,7,8,9,12,15)),
 ('Cardio','Constrictive pericarditis ต่างจาก tamponade', C(16)),
 ('Cardio','Pericardial effusion: TB (ADA สูง) vs มะเร็ง', C(17)),
 ('Cardio','Myocarditis: สาเหตุส่วนใหญ่คือไวรัส', C(11)),
 ('Cardio','Doxorubicin cardiomyopathy', C(13)),
 ('Cardio','ECG บอกตำแหน่ง STEMI (ผนัง/หลอดเลือด, right-sided lead)', C(10,42,43,51,54,104)),
 ('Cardio','จำแนกชนิด shock และ hemodynamics (JVP, SVR)', C(6,18,19,20,23,28,32)),
 ('Cardio','Tachyarrhythmia ไม่เสถียร → synchronized cardioversion / defibrillation', C(21,70,101,102)),
 ('Cardio','AF กับ stroke: CHA2DS2-VASc, MS + AF → warfarin', C(22,56,65,66)),
 ('AIR','Anaphylaxis: type I, IM adrenaline, พก auto-injector', C(24,25,26)+A(1,2,3)),
 ('Nephro','ขาดน้ำ/shock ± Na ต่ำ → 0.9% NSS', C(27,29)+N(50,53,55)),
 ('Chest','Vasovagal ระหว่างเจาะน้ำในช่องปอด', C(30)+CH(31)),
 ('Cardio','Shock liver (ischemic hepatitis)', C(31)),
 ('Cardio','STEMI reperfusion: primary PCI vs fibrinolysis, เกณฑ์สำเร็จ', C(33,34,50,52)),
 ('Cardio','กลไก ischemia: plaque rupture, fixed stenosis, microvascular', C(35,40,41)),
 ('Cardio','ACS spectrum: stable angina / UA / NSTEMI, troponin ซ้ำ, high-risk', C(36,37,38,39,105)),
 ('Cardio','Mechanical complication หลัง MI (VSR)', C(44,81)),
 ('Cardio','ไขมัน/statin/FH', C(45,46,47)),
 ('Cardio','เจ็บแน่นหน้าอก → ตรวจแรกคือ ECG 12 lead', C(48)),
 ('Cardio','Stable angina: ห้าม short-acting nifedipine', C(49)),
 ('Cardio','ลำดับการอ่าน/รายงาน ECG', C(53,106)),
 ('Cardio','Secondary prevention หลัง MI', C(55)),
 ('Cardio','ยาคุม rate/rhythm ของ AF', C(57,58)),
 ('Cardio','จำ AF ให้ได้: pulse deficit, ECG, RVR → HF/syncope', C(59,67,68,71)),
 ('Cardio','Bradyarrhythmia: AV block ทุกดีกรี, SSS → pacing', C(60,95,96,97,98,99)),
 ('Cardio','ต้นเหตุ tachyarrhythmia: thyrotoxicosis / thyroid storm / alcohol', C(61,62,63,64,69)),
 ('Cardio','SVT → adenosine', C(100)),
 ('Nephro','HyperK: ECG T สูงแหลม → Ca gluconate, ยาลด K', C(103,107,109)+N(64,65,69)),
 ('Cardio','Mitral stenosis: เสียง, rheumatic, echo', C(72,73,74,92,93,94)),
 ('Cardio','Aortic regurgitation (รวม Marfan)', C(75,76)),
 ('Cardio','Aortic stenosis', C(77,78)),
 ('Cardio','MR / MVP', C(79,80)),
 ('Cardio','Congenital shunt murmur (PDA / ASD)', C(82,91)),
 ('Cardio','Pulmonary hypertension + right HF', C(83)),
 ('Cardio','Acute rheumatic fever (ASO, Jones)', C(84,85)),
 ('Cardio','Infective endocarditis: hemoculture, signs, ยา, prophylaxis', C(86,87,88,89,90)),
 ('Cardio','วินิจฉัย HT: white coat / resistant / secondary / lifestyle', C(110,111,112,121)),
 ('Cardio','เลือกยาลดความดันตามสถานการณ์ (RAS, ตั้งครรภ์, CCB บวม, dissection)', C(113,114,124,127)),
 ('Cardio','HFrEF: GDMT (ACEI/ARNI + BB …)', C(115,116)),
 ('Cardio','Acute LHF / pulmonary edema: อาการ กลไก CXR', C(117,118,119,129)),
 ('Cardio','HF พื้นฐาน: NYHA, precipitant, JVP แยกจากตับแข็ง', C(120,122,123)),
 ('Cardio','Cardiorenal / high-output state', C(125,126)+N(49,116,117)),
 ('Chest','COPD hypercapnic respiratory failure: O2 เกิน, NIV', C(128)+CH(19,32)),
 ('Nephro','Diabetic nephropathy: hyperfiltration, UACR, SGLT2i, ACEI', C(130)+N(39,40,41,42)),
 ('Chest','ผลข้างเคียงยา TB (INH, RIF, PZA, EMB)', CH(1,2,3,4,5)+A(23)),
 ('Chest','TB: วินิจฉัย/โปรแกรม (culture, MDR, adherence, isolation, apex)', CH(6,7,8,9,10)),
 ('Chest','PCP ใน HIV / ผู้ได้ยากดภูมิ', CH(11,22)+A(16)),
 ('Nephro','Drug-induced AIN (sterile pyuria, WBC cast)', CH(12)+N(22,114,120)),
 ('Chest','อ่าน ABG', CH(13,14,15,16,21)),
 ('Chest','Hypoxemia physiology: shunt, A-a gradient, ARDS', CH(17,18,20)),
 ('Chest','Pleural fluid: Light criteria และสาเหตุ', CH(23,24,25,26,27,34)),
 ('Chest','ตรวจร่างกาย pleural effusion', CH(33)),
 ('Chest','Pneumothorax (tension / iatrogenic)', CH(28,29)),
 ('Chest','Re-expansion pulmonary edema', CH(30)),
 ('Chest','Occupational lung disease (silica, asbestos, mesothelioma, occupational asthma)', CH(35,36,37,38)),
 ('Chest','CXR lobar pneumonia', CH(39)),
 ('Chest','Lung cancer: SVC syndrome, มะเร็งที่สัมพันธ์บุหรี่', CH(40,42)),
 ('Chest','Small cell lung cancer → SIADH', CH(41)+N(57)),
 ('Chest','Pneumonia: เดาเชื้อจากเบาะแส', CH(43,45,46,47,56)),
 ('Chest','CAP severity → รักษา OPD', CH(44)),
 ('Chest','COPD: วินิจฉัยและรักษาระยะคงที่', CH(48,49,50,51)),
 ('Chest','Asthma: วินิจฉัยและรักษา', CH(52,53,54,55)),
 ('Nephro','Hypercalcemia: PHPT, มะเร็ง, myeloma, ลำดับการรักษา', N(1,2,3,4,13,14)),
 ('Nephro','Tumor lysis syndrome', N(5,6,111)),
 ('Nephro','Hypocalcemia: สาเหตุ', N(7,8,9,12)),
 ('Nephro','Magnesium และ hypoK ดื้อ (amphotericin)', N(10,11,15)),
 ('Nephro','Nephrotic syndrome: นิยาม/ตรวจปัสสาวะ', N(16,17,18,32,75)),
 ('Nephro','Nephrotic: ภาวะแทรกซ้อน VTE', N(19)),
 ('Nephro','Glomerular disease ตามบริบท (MN-มะเร็ง, MCD, HIVAN, heroin, myeloma)', N(20,21,23,24,25)),
 ('Nephro','Urine cast บอกตำแหน่ง (RBC/WBC/muddy brown)', N(26,72,73,74)),
 ('Nephro','Hematuria: glomerular vs urologic', N(27,81,82)),
 ('Nephro','ชนิด proteinuria (glomerular/functional/orthostatic)', N(28,78,79)),
 ('Nephro','Acute nephritic: PSGN vs IgA', N(29,30,33)),
 ('Nephro','Lupus nephritis', N(31,76,85,86)),
 ('Nephro','CKD vs AKI: ไตเล็ก = เรื้อรัง', N(34,35,36,37)),
 ('Nephro','eGFR / Cockcroft-Gault', N(38,47)),
 ('Nephro','Metformin กับ eGFR', N(43)),
 ('AIR','Crystal arthritis: gout / CPPD / BCP', A(19,20,21,22,29,30,31)+N(44)),
 ('Nephro','NSAID กับไต', N(45,113)),
 ('Nephro','Uremia และข้อบ่งชี้ dialysis', N(46,48,124)),
 ('Nephro','Hyponatremia: approach และแก้อย่างปลอดภัย (ODS, thiazide, pseudo)', N(51,52,54,56,68)),
 ('Nephro','Adrenal insufficiency', N(58,59)),
 ('Nephro','Periodic paralysis / K shift (thyrotoxic)', N(60,61,62,66,71)),
 ('Nephro','Electrolyte กับอาการชัก', N(63)),
 ('Nephro','HypoK อื่น ๆ (leptospirosis, ECG U wave)', N(67,70)),
 ('Nephro','Fanconi syndrome', N(77)),
 ('Nephro','นิ่วไต (calcium oxalate, struvite/Proteus, uric)', N(80,83,84,87,103)),
 ('Nephro','Asymptomatic bacteriuria: รักษาเมื่อไร', N(88,89,100)),
 ('Nephro','Simple cystitis (เกณฑ์ culture, ยาสั้น)', N(90,104)),
 ('Nephro','UTI: เดาเชื้อจาก gram stain / สายสวน', N(91,93,99)),
 ('Nephro','เบาหวานกับ UTI (รวม SGLT2i)', N(92,97)),
 ('Nephro','UTI ซ้ำในผู้ชาย → ตรวจต่อมลูกหมาก', N(94)),
 ('Nephro','Pyelonephritis ซับซ้อน (abscess, de-escalate, sepsis AKI)', N(95,96,118)),
 ('Nephro','Cyclophosphamide hemorrhagic cystitis', N(98)),
 ('Nephro','Purple urine bag syndrome', N(101)),
 ('Nephro','Renal TB (sterile pyuria)', N(102)),
 ('Nephro','Prerenal vs ATN (FENa, cast, กลไก)', N(105,106,107,108,115,119)),
 ('Nephro','Rhabdomyolysis / statin myopathy (CK)', N(109,110,123)+A(36,37)),
 ('Nephro','Contrast-associated AKI', N(112)),
 ('Nephro','Obstructive AKI (BPH)', N(121)),
 ('Nephro','Lithium nephrogenic DI', N(122)),
 ('AIR','SJS จาก allopurinol (HLA-B*58:01)', A(4,5)),
 ('AIR','Transfusion reaction', A(6,7)),
 ('AIR','Immune cytopenia → หา SLE/HIV/HCV', A(8,9,10)),
 ('AIR','ผลข้างเคียงยากดภูมิใน SLE (วัคซีน, DM, HCQ ตา, AVN, MMF ตั้งครรภ์)', A(11,12,17,44,49)),
 ('AIR','จำแนก arthritis (OA/RA/SpA/AOSD/chikungunya)', A(13,27,28,45,50)),
 ('AIR','เลือก autoantibody (ANA, dsDNA/Sm, drug-induced, APS, Scl-70, ANCA)', A(14,15,18,34,41,48)),
 ('AIR','Septic / gonococcal arthritis', A(24,25,26,32)),
 ('AIR','Scleroderma renal crisis', A(35)),
 ('AIR','Dermatomyositis → หามะเร็ง', A(38)),
 ('AIR','GCA / PMR', A(39,46)),
 ('AIR','IgA vasculitis (HSP)', A(40)),
 ('AIR','ความปลอดภัย DMARD/biologic ใน RA', A(42,43,47)),
]

def main():
    items = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data/*_old_*.json'))):
        for x in json.load(open(f)):
            x['years'] = sorted({int(y) for y in re.findall(r'MED\s?(\d\d)(?!\d)', x['src'])})
            items[x['id']] = x
    seen = collections.Counter(i for _, _, l in THEMES for i in l)
    dup = [i for i, c in seen.items() if c > 1]; miss = set(items) - set(seen); extra = set(seen) - set(items)
    assert not dup and not miss and not extra, (dup, miss, extra)

    themes = []
    for sysname, name, lst in THEMES:
        yrs = collections.Counter(y for i in lst for y in items[i]['years'])
        themes.append({'system': sysname, 'theme': name, 'n': len(lst), 'years': dict(sorted(yrs.items())),
                       'first': min(yrs), 'items': [{'id': i, 'lec': items[i]['lec'], 'years': items[i]['years'],
                       'q': items[i]['q'], 'a': items[i]['choices'][items[i]['answer']]} for i in lst]})
    YEARS = sorted({y for x in items.values() for y in x['years']})
    per_year = []
    for Y in YEARS:
        hit = [t for t in themes if Y in t['years']]
        new = [t for t in hit if t['first'] == Y]
        # ข้อในปีนั้นที่แก่นเคยมีแล้ว แต่ตัวข้อเองเพิ่งโผล่ครั้งแรก (มุมใหม่ของแก่นเดิม)
        new_angle = [it for t in hit if t['first'] < Y for it in t['items'] if it['years'] and it['years'][0] == Y]
        yi = [x for x in items.values() if Y in x['years']]
        repeat = [x for x in yi if x['years'][0] < Y]          # ข้อเดิมซ้ำ (เคยอยู่ในโพยรุ่นก่อน)
        per_year.append({'year': Y, 'items': len(yi), 'themes': len(hit),
                         'repeat_items': len(repeat), 'new_angle_items': len(new_angle),
                         'new_theme_items': len(yi) - len(repeat) - len(new_angle),
                         'new_themes': [{'theme': t['theme'], 'system': t['system'],
                                         'items': [it for it in t['items'] if Y in it['years']]} for t in new]})
    out = {'n_items': len(items), 'n_themes': len(themes), 'themes': themes, 'per_year': per_year}
    json.dump(out, open(os.path.join(ROOT, 'analysis/old_themes.json'), 'w'), ensure_ascii=False, indent=1)
    return out

if __name__ == '__main__':
    o = main()
    print(o['n_items'], 'ข้อ', o['n_themes'], 'แก่น')
    sz = collections.Counter(t['n'] for t in o['themes']); print('ขนาดแก่น', sorted(sz.items()))
    for t in sorted(o['themes'], key=lambda t: (-len(t['years']), -t['n']))[:25]:
        print(t['n'], len(t['years']), t['years'], t['theme'])
    for p in o['per_year']:
        print(f"MED{p['year']}: {p['items']} ข้อ/{p['themes']} แก่น | ซ้ำข้อเดิม {p['repeat_items']} | แก่นเดิมมุมใหม่ {p['new_angle_items']} | แก่นใหม่ {len(p['new_themes'])} แก่น ({p['new_theme_items']} ข้อ)")
