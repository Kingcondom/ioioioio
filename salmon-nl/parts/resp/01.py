from lib import lecture, sec, mcq, mcq_ordered, fig

D = "สไลด์ NL2-Respiratory"
OLD = "ข้อสอบเก่าในสไลด์ MedSalmon"

# ---------------------------------------------------------------- figures
FIG_SPIRO = '''<svg viewBox="0 0 720 360">
 <defs><marker id="resp-01-01-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="230" y="12" width="260" height="46" rx="10" class="acsoft"/>
 <text x="360" y="32" text-anchor="middle" class="tb">Spirometry: ดู FEV1/FVC ก่อน</text>
 <text x="360" y="49" text-anchor="middle" class="t3">(post-bronchodilator)</text>
 <path d="M300 58L170 100" class="ln" marker-end="url(#resp-01-01-a)"/>
 <path d="M420 58L550 100" class="ln" marker-end="url(#resp-01-01-a)"/>
 <text x="196" y="76" text-anchor="middle" class="ta">&lt; 0.7</text>
 <text x="524" y="76" text-anchor="middle" class="ta">≥ 0.7</text>
 <rect x="40" y="102" width="260" height="62" rx="10" class="box"/>
 <text x="170" y="126" text-anchor="middle" class="tb">Obstructive pattern</text>
 <text x="170" y="146" text-anchor="middle" class="t3">TLC ↑ · RV ↑ · FEV1 ↓↓↓ · FVC ↓</text>
 <rect x="420" y="102" width="260" height="62" rx="10" class="box"/>
 <text x="550" y="126" text-anchor="middle" class="tb">FVC ↓ → สงสัย Restrictive</text>
 <text x="550" y="146" text-anchor="middle" class="t3">TLC ↓ · RV ↓ · FEV1 ปกติ/↓ · ratio ปกติ/↑</text>
 <path d="M170 164V200" class="ln" marker-end="url(#resp-01-01-a)"/>
 <rect x="30" y="202" width="280" height="56" rx="10" class="c1soft"/>
 <text x="170" y="225" text-anchor="middle" class="tb">หลังพ่น bronchodilator</text>
 <text x="170" y="245" text-anchor="middle" class="t2">FEV1 ↑ ≥ 12% และ ≥ 200 ml ?</text>
 <path d="M110 258L80 290" class="ln" marker-end="url(#resp-01-01-a)"/>
 <path d="M230 258L260 290" class="ln" marker-end="url(#resp-01-01-a)"/>
 <text x="78" y="276" text-anchor="middle" class="ta">YES</text>
 <text x="266" y="276" text-anchor="middle" class="ta">NO</text>
 <rect x="20" y="292" width="140" height="56" rx="10" class="oksoft"/>
 <text x="90" y="315" text-anchor="middle" class="tb">Reversible</text>
 <text x="90" y="335" text-anchor="middle">→ Asthma</text>
 <rect x="190" y="292" width="140" height="56" rx="10" class="badsoft"/>
 <text x="260" y="315" text-anchor="middle" class="tb">Irreversible</text>
 <text x="260" y="335" text-anchor="middle">→ COPD</text>
 <path d="M550 164V200" class="ln" marker-end="url(#resp-01-01-a)"/>
 <rect x="400" y="202" width="300" height="146" rx="10" class="c2soft"/>
 <text x="550" y="226" text-anchor="middle" class="tb">Restrictive lung disease</text>
 <text x="414" y="252" class="t2">• ILD / CTD (SSc, RA, SLE)</text>
 <text x="414" y="276" class="t2">• Pneumoconiosis (asbestosis)</text>
 <text x="414" y="300" class="t2">• Chest wall, neuromuscular (เสริม)</text>
 <text x="414" y="328" class="t3">ยืนยันด้วย TLC ↓ (lung volume) (เสริม)</text>
</svg>'''

FIG_LOOP = '''<svg viewBox="0 0 720 330">
 <defs><marker id="resp-01-01-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="360" y="22" text-anchor="middle" class="tb">Flow–volume loop ช่วงหายใจออก (เสริม)</text>
 <path d="M50 250H690" class="ln" marker-end="url(#resp-01-01-b)"/>
 <path d="M50 250V50" class="ln" marker-end="url(#resp-01-01-b)"/>
 <text x="58" y="48" class="t3">Flow</text>
 <text x="50" y="272" class="t3">ปริมาตรปอดมาก (TLC)</text>
 <text x="690" y="272" text-anchor="end" class="t3">ปริมาตรปอดน้อย (RV) →</text>
 <path d="M200 250C206 110 226 82 250 84C320 92 420 170 480 250" class="lnok"/>
 <path d="M110 250C116 150 130 130 146 132C190 160 260 228 400 250" class="lnbad"/>
 <path d="M380 250C386 150 400 130 416 132C450 140 500 200 540 250" class="lnc2"/>
 <text x="150" y="122" text-anchor="middle" class="t3">Obstructive</text>
 <text x="262" y="74" text-anchor="middle" class="t3">ปกติ</text>
 <text x="430" y="122" text-anchor="middle" class="t3">Restrictive</text>
 <rect x="470" y="50" width="230" height="96" rx="8" class="sunk"/>
 <rect x="484" y="66" width="16" height="4" class="ok"/>
 <text x="508" y="72" class="t2">ปกติ</text>
 <rect x="484" y="90" width="16" height="4" class="bad"/>
 <text x="508" y="96" class="t2">Obstructive: เว้า เลื่อนซ้าย</text>
 <rect x="484" y="114" width="16" height="4" class="c2"/>
 <text x="508" y="120" class="t2">Restrictive: แคบ เลื่อนขวา</text>
 <text x="484" y="138" class="t3">ซ้าย = TLC/RV สูง (air trapping)</text>
 <rect x="50" y="290" width="640" height="32" rx="8" class="sunk"/>
 <text x="370" y="311" text-anchor="middle" class="t2">Obstructive: peak flow ต่ำ ขาลงเว้า (scooped) · Restrictive: รูปทรงคงเดิมแต่ปริมาตรเล็ก</text>
</svg>'''

FIG_AECOPD = '''<svg viewBox="0 0 720 380">
 <defs><marker id="resp-01-02-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="200" y="10" width="320" height="46" rx="10" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">AECOPD: O2 keep SpO2 88–92%</text>
 <text x="360" y="48" text-anchor="middle" class="t3">ABG เมื่อ SpO2 &lt; 92% หรือมี exacerbation</text>
 <path d="M360 56V82" class="ln" marker-end="url(#resp-01-02-a)"/>
 <rect x="130" y="84" width="460" height="50" rx="10" class="box"/>
 <text x="360" y="105" text-anchor="middle" class="tb">อ่าน ABG: pH ≤ 7.35 และ PaCO2 ≥ 45 mmHg ?</text>
 <text x="360" y="124" text-anchor="middle" class="t3">หรือ hypoxemia ไม่ดีขึ้น · หอบมาก · ใช้ accessory muscles</text>
 <path d="M250 134L150 168" class="ln" marker-end="url(#resp-01-02-a)"/>
 <path d="M470 134L570 168" class="ln" marker-end="url(#resp-01-02-a)"/>
 <text x="180" y="150" class="ta">ไม่มี</text>
 <text x="525" y="150" class="ta">มี</text>
 <rect x="20" y="170" width="260" height="62" rx="10" class="oksoft"/>
 <text x="150" y="194" text-anchor="middle" class="tb">O2 mask with bag</text>
 <text x="150" y="214" text-anchor="middle" class="t3">+ ยา (ด้านล่าง) · ติดตาม ABG</text>
 <rect x="440" y="170" width="260" height="62" rx="10" class="misssoft"/>
 <text x="570" y="194" text-anchor="middle" class="tb">NIPPV</text>
 <text x="570" y="214" text-anchor="middle" class="t3">acute respiratory acidosis</text>
 <path d="M570 232V258" class="ln" marker-end="url(#resp-01-02-a)"/>
 <rect x="440" y="260" width="260" height="46" rx="10" class="badsoft"/>
 <text x="570" y="280" text-anchor="middle" class="tb">NIPPV ไม่ดีขึ้น → ETT</text>
 <text x="570" y="297" text-anchor="middle" class="t3">+ mechanical ventilation</text>
 <rect x="20" y="256" width="400" height="114" rx="10" class="sunk"/>
 <text x="36" y="280" class="tb">ยาทุกราย</text>
 <text x="36" y="302" class="t2">• NB SABA (salbutamol) ± SAMA (ipratropium)</text>
 <text x="36" y="324" class="t2">• Systemic steroid: prednisone PO / MP, dexa IV</text>
 <text x="36" y="346" class="t2">• ATB เฉพาะ purulent sputum + หอบ/ไอมากขึ้น</text>
 <text x="48" y="363" class="t3">หรือ on mechanical ventilation</text>
</svg>'''

FIG_GOLD = '''<svg viewBox="0 0 720 330">
 <defs><marker id="resp-01-03-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <text x="360" y="22" text-anchor="middle" class="tb">GOLD ABE: แบ่งตามประวัติ exacerbation และอาการ</text>
 <rect x="150" y="40" width="540" height="78" rx="10" class="badsoft"/>
 <text x="420" y="66" text-anchor="middle" class="tb">Group E</text>
 <text x="420" y="86" text-anchor="middle" class="t2">exacerbation ≥ 2 ครั้ง หรือ admit ≥ 1 ครั้ง/ปี (เสริม)</text>
 <text x="420" y="106" text-anchor="middle" class="ta">LABA + LAMA (+ ICS ถ้า eos ≥ 300)</text>
 <rect x="150" y="130" width="265" height="96" rx="10" class="oksoft"/>
 <text x="282" y="156" text-anchor="middle" class="tb">Group A</text>
 <text x="282" y="176" text-anchor="middle" class="t3">อาการน้อย (mMRC 0–1) (เสริม)</text>
 <text x="282" y="206" text-anchor="middle" class="ta">A bronchodilator</text>
 <rect x="425" y="130" width="265" height="96" rx="10" class="misssoft"/>
 <text x="557" y="156" text-anchor="middle" class="tb">Group B</text>
 <text x="557" y="176" text-anchor="middle" class="t3">อาการมาก (mMRC ≥ 2) (เสริม)</text>
 <text x="557" y="206" text-anchor="middle" class="ta">LABA + LAMA</text>
 <text x="20" y="80" class="t2">exacerbation</text>
 <text x="20" y="98" class="t2">บ่อย</text>
 <text x="20" y="170" class="t2">exacerbation</text>
 <text x="20" y="188" class="t2">0–1 ครั้ง</text>
 <text x="20" y="206" class="t3">(ไม่ admit)</text>
 <path d="M150 248H690" class="ln" marker-end="url(#resp-01-03-a)"/>
 <text x="420" y="268" text-anchor="middle" class="t3">อาการมากขึ้น →</text>
 <rect x="20" y="282" width="680" height="40" rx="8" class="sunk"/>
 <text x="360" y="307" text-anchor="middle" class="t2">ทุกกลุ่ม: เลิกบุหรี่ · วัคซีน influenza + pneumococcal · pulmonary rehab · LTOT ถ้า PaO2 ≤ 55 / SaO2 ≤ 88%</text>
</svg>'''

FIG_ASTHMA_EX = '''<svg viewBox="0 0 720 330">
 <defs><marker id="resp-01-05-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arr"/></marker></defs>
 <rect x="210" y="10" width="300" height="46" rx="10" class="acsoft"/>
 <text x="360" y="30" text-anchor="middle" class="tb">Asthma exacerbation</text>
 <text x="360" y="48" text-anchor="middle" class="t3">ประเมินความรุนแรง (พูด, RR, PR, SpO2, PEF)</text>
 <path d="M300 56L190 90" class="ln" marker-end="url(#resp-01-05-a)"/>
 <path d="M420 56L530 90" class="ln" marker-end="url(#resp-01-05-a)"/>
 <rect x="20" y="92" width="330" height="150" rx="10" class="misssoft"/>
 <text x="185" y="116" text-anchor="middle" class="tb">Mild – moderate</text>
 <text x="36" y="142" class="t2">• O2 mask with bag (SpO2 93–95% เสริม)</text>
 <text x="36" y="166" class="t2">• NB SABA: salbutamol</text>
 <text x="36" y="190" class="t2">• Systemic steroid: prednisone PO</text>
 <text x="36" y="222" class="t3">steroid ให้เร็วตั้งแต่แรก ไม่ต้องรอ</text>
 <rect x="370" y="92" width="330" height="150" rx="10" class="badsoft"/>
 <text x="535" y="116" text-anchor="middle" class="tb">Severe / life-threatening</text>
 <text x="386" y="142" class="t2">• O2 · ETT ถ้า respiratory failure</text>
 <text x="386" y="166" class="t2">• NB SABA + SAMA (+ ipratropium)</text>
 <text x="386" y="190" class="t2">• Pred PO หรือ MP / dexa IV</text>
 <text x="386" y="214" class="t2">• ± IV MgSO4 / high-dose ICS</text>
 <path d="M360 242V266" class="ln" marker-end="url(#resp-01-05-a)"/>
 <rect x="100" y="268" width="520" height="52" rx="10" class="box"/>
 <text x="360" y="289" text-anchor="middle" class="tb">ประเมินซ้ำที่ 1 ชม. (เสริม)</text>
 <text x="360" y="308" text-anchor="middle" class="t3">ดีขึ้น PEF &gt; 60–80% → กลับบ้าน + steroid PO · ไม่ดีขึ้น/แย่ลง → admit, ICU</text>
</svg>'''

FIG_GINA = '''<svg viewBox="0 0 740 330">
 <text x="370" y="22" text-anchor="middle" class="tb">GINA track 1: reliever = PRN low-dose ICS/formoterol ทุก step</text>
 <rect x="20" y="230" width="170" height="60" rx="8" class="oksoft"/>
 <text x="105" y="252" text-anchor="middle" class="tb">STEP 1–2</text>
 <text x="105" y="272" text-anchor="middle" class="t3">Controller: ไม่มี</text>
 <rect x="200" y="180" width="170" height="110" rx="8" class="c1soft"/>
 <text x="285" y="202" text-anchor="middle" class="tb">STEP 3</text>
 <text x="285" y="222" text-anchor="middle" class="t3">Daily low-dose</text>
 <text x="285" y="238" text-anchor="middle" class="t3">ICS/formoterol</text>
 <rect x="380" y="130" width="170" height="160" rx="8" class="misssoft"/>
 <text x="465" y="152" text-anchor="middle" class="tb">STEP 4</text>
 <text x="465" y="172" text-anchor="middle" class="t3">Daily medium-dose</text>
 <text x="465" y="188" text-anchor="middle" class="t3">ICS/formoterol</text>
 <rect x="560" y="80" width="170" height="210" rx="8" class="badsoft"/>
 <text x="645" y="102" text-anchor="middle" class="tb">STEP 5</text>
 <text x="645" y="122" text-anchor="middle" class="t3">Daily high-dose</text>
 <text x="645" y="138" text-anchor="middle" class="t3">ICS/formoterol</text>
 <text x="645" y="160" text-anchor="middle" class="t3">+ add-on LAMA</text>
 <text x="645" y="176" text-anchor="middle" class="t3">(tiotropium)</text>
 <text x="105" y="214" text-anchor="middle" class="t3">อาการ &lt; 4–5 วัน/สัปดาห์</text>
 <text x="285" y="262" text-anchor="middle" class="t3">อาการเกือบทุกวัน</text>
 <text x="285" y="278" text-anchor="middle" class="t3">หรือตื่น ≥ 1/สัปดาห์</text>
 <text x="465" y="246" text-anchor="middle" class="t3">อาการทุกวัน หรือตื่น</text>
 <text x="465" y="262" text-anchor="middle" class="t3">≥ 1/สัปดาห์ + lung</text>
 <text x="465" y="278" text-anchor="middle" class="t3">function ต่ำ</text>
 <text x="645" y="262" text-anchor="middle" class="t3">STEP 4 แล้ว</text>
 <text x="645" y="278" text-anchor="middle" class="t3">ยังคุมไม่ได้</text>
 <rect x="20" y="300" width="710" height="24" rx="6" class="sunk"/>
 <text x="375" y="317" text-anchor="middle" class="t2">ทุก step: เลี่ยง trigger · วัคซีน · F/U clinical + spirometry · เช็ค inhaler technique/compliance ก่อน step up</text>
</svg>'''

# ---------------------------------------------------------------- sections
S1 = sec("resp-01-01", "Spirometry: Obstructive vs Restrictive",
    "อ่าน FEV1/FVC แยก obstructive/restrictive แล้วใช้ bronchodilator response แยก asthma กับ COPD",
    minutes=5, source=f"{D} หน้า 4–7", nl=["3.3.18", "2.3.10(1)", "2.3.10(3)"],
    md='''
### ทำไมต้องเริ่มที่ spirometry
Spirometry วัดว่าคนไข้ **เป่าลมออกได้เร็วแค่ไหน (FEV1)** และ **ได้ทั้งหมดเท่าไร (FVC)** — โรคปอดเรื้อรังแบ่งได้สองกลุ่มใหญ่ตามกลไก
- **Obstructive**: ทางเดินหายใจแคบ ลมออกช้า → FEV1 ลดมากกว่า FVC → **FEV1/FVC < 0.7** · ลมค้าง (air trapping) ทำให้ **TLC และ RV สูง**
- **Restrictive**: ปอด/ผนังอกขยายไม่ได้ ปริมาตรปอดเล็กลงทั้งหมด → FEV1 และ FVC ลดพอ ๆ กัน → **ratio ปกติหรือสูง** · TLC, RV ต่ำ

| | Obstructive | Restrictive |
|---|---|---|
| TLC | ↑ | ↓ |
| RV | ↑ | ↓ |
| FEV1 | ↓↓↓ | ปกติ / ↓ |
| FVC | ↓ | ↓ |
| FEV1/FVC | ↓ (< 0.7) | ปกติ / ↑ |
| ตัวอย่างโรค | Asthma, COPD, bronchiectasis | ILD, SSc, asbestosis |

[[fig:resp-01-01-spiro]]

### แยก Asthma กับ COPD ด้วย bronchodilator test
เมื่อพบ obstructive (FEV1/FVC < 0.7) ให้พ่น bronchodilator แล้วเป่าซ้ำ
- **FEV1 เพิ่ม ≥ 12% และ ≥ 200 ml** → reversible airflow obstruction → **Asthma**
- เพิ่มไม่ถึงเกณฑ์ → irreversible airflow obstruction → **COPD**

> ต้องผ่าน **ทั้งสองเงื่อนไข** (≥ 12% และ ≥ 200 ml) — โจทย์ชอบให้ FEV1 เพิ่ม 15% แต่แค่ 150 ml เพื่อหลอกว่า reversible

[[fig:resp-01-01-loop]]

#### เคล็ดลับอ่านค่า (เสริม)
- Restrictive จริงต้องยืนยันด้วย **TLC ต่ำ** (body plethysmography) — spirometry อย่างเดียวบอกได้แค่ "สงสัย"
- Mixed pattern: ratio < 0.7 + FVC ต่ำมาก เช่น silicosis (สไลด์หน้า 218 บอกว่า PFT เป็น mix ได้)
''',
    figs=[fig("resp-01-01-spiro", "อ่าน spirometry ทีละขั้น", FIG_SPIRO,
              "เริ่มจาก FEV1/FVC → ถ้า < 0.7 ดู bronchodilator response แยก asthma (reversible) กับ COPD (irreversible)"),
          fig("resp-01-01-loop", "รูปทรง flow–volume loop", FIG_LOOP,
              "แกนนอนเรียงจากปริมาตรมาก (ซ้าย) ไปน้อย (ขวา): obstructive เลื่อนซ้ายและขาลงเว้า, restrictive แคบและเลื่อนขวา")],
    pearls=["FEV1/FVC < 0.7 = obstructive · ratio ปกติหรือสูง + FVC ต่ำ = สงสัย restrictive",
            "Obstructive: TLC ↑ RV ↑ (air trapping) · Restrictive: TLC ↓ RV ↓",
            "Reversible = FEV1 ↑ ≥ 12% **และ** ≥ 200 ml หลังพ่นยา → asthma; ไม่ถึง → COPD",
            "ILD, SSc, asbestosis ให้ restrictive pattern"],
    items=[
        mcq("RESP-01-01-1", """A 58-year-old man with 40 pack-years of smoking has exertional dyspnea. Spirometry: FEV1/FVC 0.58, FEV1 55% predicted. After inhaled salbutamol, FEV1 increases by 6% (90 mL). Which pattern best describes his lung function?""",
            "Irreversible obstructive defect consistent with COPD",
            ["Reversible obstructive defect consistent with asthma",
             "Restrictive defect consistent with interstitial lung disease",
             "Normal spirometry",
             "Mixed defect requiring repeat test after oral steroid"],
            explain="""FEV1/FVC 0.58 (< 0.7) คือ obstructive และหลังพ่นยา FEV1 เพิ่มแค่ 6% และ 90 ml ไม่ถึงเกณฑ์ ≥ 12% และ ≥ 200 ml จึงเป็น irreversible obstruction ร่วมกับประวัติสูบบุหรี่ เข้าได้กับ COPD
- Reversible obstruction แบบ asthma ต้องเพิ่มทั้ง ≥ 12% และ ≥ 200 ml ซึ่งไม่ถึง
- Restrictive defect จะมี ratio ปกติหรือสูง ไม่ใช่ 0.58
- Spirometry ปกติไม่ได้ เพราะ ratio ต่ำชัด
- Mixed defect ต้องมี FVC/TLC ต่ำร่วมด้วย และการลอง oral steroid ไม่ใช่ขั้นตอนวินิจฉัย COPD""",
            pearl="Obstructive + bronchodilator response ไม่ถึง 12%/200 ml = COPD",
            topic="Spirometry", ref=[f"{D} หน้า 6–7"], nl=["3.3.18", "2.3.10(3)"]),
        mcq("RESP-01-01-2", """A 26-year-old woman has episodic wheeze and nocturnal cough. Spirometry: FEV1/FVC 0.66, FEV1 2.10 L. Fifteen minutes after salbutamol, FEV1 is 2.45 L. Which interpretation is correct?""",
            "Significant reversibility (about 17% and 350 mL), supporting asthma",
            ["No reversibility because the change is less than 400 mL",
             "Restrictive pattern because FEV1/FVC is above 0.6",
             "Irreversible obstruction, supporting COPD",
             "Result is uninterpretable without a methacholine test"],
            explain="""FEV1 เพิ่มจาก 2.10 เป็น 2.45 L = 350 ml คิดเป็น 350/2100 ≈ 17% ผ่านทั้งเกณฑ์ ≥ 12% และ ≥ 200 ml → reversible airflow obstruction เข้ากับ asthma
- เกณฑ์ไม่ได้ใช้ 400 ml เกณฑ์คือ 200 ml (400 ml เป็นค่าที่บางแนวทางใช้บอก "very large response" ไม่ใช่ cut-off วินิจฉัย)
- Restrictive ดูจาก ratio ปกติหรือสูงร่วมกับ FVC ต่ำ ไม่ใช่ "ratio > 0.6" และ 0.66 ยังต่ำกว่า 0.7
- Irreversible obstruction ผิดเพราะเพิ่มเกินเกณฑ์ชัดเจน
- Methacholine challenge ใช้เมื่อ spirometry ปกติแต่ยังสงสัย asthma ในรายนี้วินิจฉัยได้แล้ว""",
            pearl="คำนวณทั้ง % และ ml เสมอ: (หลัง − ก่อน)/ก่อน",
            topic="Bronchodilator response", ref=[f"{D} หน้า 7, 31"], nl=["3.3.18", "2.3.10(1)"]),
        mcq("RESP-01-01-3", """A 50-year-old non-smoker with progressive dyspnea has fine bibasilar crackles. Which spirometry/lung volume profile is most expected?""",
            "FEV1/FVC 0.85, FVC 60% predicted, TLC reduced",
            ["FEV1/FVC 0.55, FVC 80% predicted, TLC increased",
             "FEV1/FVC 0.60, FEV1 improves 15% and 250 mL after bronchodilator",
             "FEV1/FVC 0.65, RV increased, TLC increased",
             "Normal FEV1/FVC and normal TLC with low DLCO only from anemia"],
            explain="""ผู้ป่วยไม่สูบบุหรี่ เหนื่อยมากขึ้นเรื่อย ๆ มี fine crackles ที่ฐานปอด นึกถึง ILD ซึ่งเป็น restrictive: ratio ปกติหรือสูง FVC ต่ำ และ TLC ต่ำ
- ratio 0.55 กับ TLC สูงคือ obstructive (COPD) ไม่ใช่ ILD
- ratio 0.60 ที่ตอบสนองต่อยาพ่นคือ asthma
- RV และ TLC สูงคือ air trapping ของ obstructive disease
- ค่าปกติทั้งหมดและ DLCO ต่ำจากซีดไม่อธิบาย crackles และอาการเหนื่อยที่ค่อย ๆ เป็นมากขึ้น""",
            pearl="ILD = restrictive: ratio ปกติ/สูง, FVC ↓, TLC ↓",
            topic="Restrictive pattern", ref=[f"{D} หน้า 6, 206"], nl=["3.3.18"]),
    ])

S2 = sec("resp-01-02", "COPD: วินิจฉัยและ acute exacerbation",
    "ผู้สูบบุหรี่ ไอเสมหะเรื้อรัง + post-BD FEV1/FVC < 0.7 · AECOPD: O2 88–92%, NIPPV เมื่อ pH ≤ 7.35 + PaCO2 ≥ 45",
    minutes=8, source=f"{D} หน้า 8–14, 19–24", nl=["2.3.10(3)", "2.2.11", "3.3.17"],
    md='''
### นิยามและกลไก
COPD คือ **airflow obstruction ที่ไม่กลับคืน (irreversible)** จากการอักเสบเรื้อรังของทางเดินหายใจและถุงลมที่ถูกทำลาย (emphysema) จากการสัมผัสควัน
- **Risk**: สูบบุหรี่ (สำคัญสุด), มลพิษทางอากาศ/ควันไฟจากการหุงต้ม
- Chronic bronchitis → เมือกมาก ไอเสมหะ · Emphysema → ผนังถุงลมถูกทำลาย ปอดยืดหยุ่นลด ทางเดินหายใจเล็กยุบตอนหายใจออก → air trapping

### อาการและตรวจร่างกาย
- ไอมีเสมหะเรื้อรัง, เหนื่อย, หายใจเร็ว
- **Barrel chest** (AP diameter ↑), **prolonged expiratory phase**
- **End-expiratory wheezing**, rhonchi

### Investigation
| การตรวจ | สิ่งที่พบ |
|---|---|
| Spirometry | **post-BD FEV1/FVC < 0.7** และ FEV1 ↑ < 12% หลังพ่นยา |
| ABG (เมื่อ SpO2 < 92% หรือ AECOPD) | PaO2 ↓ ± PaCO2 ↑ |
| CXR | flattened diaphragm, horizontal ribs + widened ICS, lung markings ↓ |
| CBC | Hct ↑ (secondary polycythemia จาก hypoxemia เรื้อรัง) |

> **Dx COPD ต้องมีทุกข้อ**: clinical + risk factor **และ** spirometry ยืนยัน irreversible obstruction (post-bronchodilator FEV1/FVC < 0.7) — CXR ช่วยแต่วินิจฉัยไม่ได้

### Acute exacerbation of COPD (AECOPD)
นิยาม: อาการเหนื่อย/ไอ/เสมหะ แย่ลงเฉียบพลันจนต้องปรับการรักษา — ส่วนใหญ่ trigger จาก **viral infection**
[[fig:resp-01-02-aecopd]]

#### 1. Oxygen และ ventilatory support
- **O2 mask with bag, keep SpO2 88–92%** — ไม่ให้สูงเกิน เพราะผู้ป่วย CO2 retainer ได้ O2 มากเกิน → V/Q mismatch แย่ลง + Haldane effect → PaCO2 ขึ้น (เสริม)
- **NIPPV** เมื่อมี respiratory acidosis (**PaCO2 ≥ 45 mmHg และ pH ≤ 7.35**), hypoxemia ไม่ดีขึ้น, หอบมาก, ใช้ accessory muscles
- **ETT** เมื่อใช้ NIPPV แล้วไม่ดีขึ้น

#### 2. Bronchodilators
- NB SABA: **salbutamol** หรือ SABA/SAMA: **salbutamol + ipratropium bromide**

#### 3. Systemic corticosteroid
- **Prednisone PO** หรือ methylprednisolone IV, dexamethasone IV (GOLD: prednisolone 40 mg/วัน 5 วัน — เสริม)

#### 4. Antibiotic — ไม่ให้ทุกราย
ส่วนใหญ่เกิดจาก virus ให้ ATB **เฉพาะ**
- **เสมหะเป็นหนองมากขึ้น (increased purulence) + เหนื่อยมากขึ้น** หรือไอบ่อยและรุนแรงขึ้น
- หรือผู้ป่วยที่ **on mechanical ventilation**
- ยา: **amoxicillin/clavulanate, azithromycin, doxycycline**

### อ่าน ABG ในคนไข้ COPD (เสริม)
| ภาวะ | pH | PaCO2 | HCO3 |
|---|---|---|---|
| Acute respiratory acidosis | ↓ มาก | ↑ | ↑ เล็กน้อย (1 ต่อ PaCO2 10) |
| Chronic (compensated) | ใกล้ปกติ | ↑ | ↑ (3.5–4 ต่อ PaCO2 10) |
| Acute on chronic (AECOPD) | ↓ | ↑ มาก | ↑ มากกว่าที่ acute จะอธิบายได้ |

> ตัวลวงยอดฮิต: COPD + ไข้ + เสมหะเหลือง + **infiltrate ที่ CXR** = **COPD exacerbation due to pneumonia** (รักษาแบบ CAP ด้วย) ไม่ใช่ AECOPD เฉย ๆ

> Wheeze ทั้ง inspiratory และ expiratory ที่ฟังชัดตรง sternum (central/fixed) → นึกถึง **tracheal tumor / central airway obstruction** ไม่ใช่ COPD
''',
    figs=[fig("resp-01-02-aecopd", "AECOPD: ใช้ ABG ตัดสิน ventilatory support", FIG_AECOPD,
              "ดู pH กับ PaCO2 ก่อน: respiratory acidosis → NIPPV, NIPPV ล้มเหลว → ETT; ยาพื้นฐานให้ทุกราย ส่วน ATB ให้ตามข้อบ่งชี้")],
    pearls=["Dx COPD = clinical + risk + post-BD FEV1/FVC < 0.7 (ต้องมีทุกข้อ)",
            "AECOPD: keep SpO2 88–92% ไม่ใช่ 100%",
            "NIPPV เมื่อ pH ≤ 7.35 และ PaCO2 ≥ 45 mmHg · NIPPV ไม่ดีขึ้น → ETT",
            "ATB ใน AECOPD เฉพาะ purulent sputum + หอบมากขึ้น หรือ on ventilator",
            "COPD ไข้ เสมหะเหลือง + infiltrate = AECOPD due to pneumonia"],
    items=[
        mcq("RESP-01-02-1", """A man who smokes 10–15 cigarettes/day has had recurrent dyspnea and cough for 2 years. Examination shows expiratory wheezing and rhonchi without a barrel-shaped chest. Vital signs and laboratory results are normal. What is the most likely diagnosis?""",
            "Chronic obstructive pulmonary disease",
            ["Asthma", "Bronchiectasis", "Lung cancer", "Tracheal tumor"],
            explain="""ผู้สูบบุหรี่ มีไอและเหนื่อยเป็น ๆ หาย ๆ มา 2 ปี ตรวจได้ expiratory wheeze และ rhonchi เข้ากับ COPD — barrel chest เป็นอาการระยะท้าย การไม่มีจึงไม่ตัด COPD ออก
- Asthma มักเริ่มในคนอายุน้อย มี atopy อาการเป็นช่วงกลางคืนหรือมีตัวกระตุ้นชัดเจน โจทย์ไม่ให้ข้อมูลเหล่านี้
- Bronchiectasis เด่นที่เสมหะเป็นหนองปริมาณมาก ไอเป็นเลือด และฟังได้ coarse crepitation
- Lung cancer ควรมีน้ำหนักลด ไอเป็นเลือด หรือ wheeze เฉพาะที่
- Tracheal tumor ให้ wheeze ทั้งหายใจเข้าและออก ฟังชัดตรงกลาง (stridor)""",
            pearl="Smoker + chronic cough + expiratory wheeze = COPD จนกว่าจะพิสูจน์ได้ว่าไม่ใช่",
            topic="COPD diagnosis", ref=[f"{D} หน้า 19–20"], nl=["2.3.10(3)"], kind="old", src=OLD),
        mcq("RESP-01-02-2", """A 40-year-old woman who has smoked for 10 years has progressive dyspnea. Examination reveals both inspiratory and expiratory wheezing, loudest over the sternum, with no wheeze in the lung periphery. What is the most likely diagnosis?""",
            "Tracheal tumor",
            ["COPD", "Asthma", "Bronchiectasis", "Pulmonary embolism"],
            explain="""Wheeze ที่ได้ยินทั้งช่วงหายใจเข้าและหายใจออก (fixed obstruction) ชัดที่สุดตรง sternum หมายถึงการอุดกั้นทางเดินหายใจใหญ่ส่วนกลาง เช่น tracheal tumor
- COPD และ asthma เป็น diffuse small airway obstruction จะได้ยิน expiratory wheeze กระจายทั่วทั้งสองปอด
- Bronchiectasis ฟังได้ coarse crepitation เสมหะมาก
- Pulmonary embolism มักฟังปอดได้ clear ไม่มี wheeze เด่น""",
            pearl="Inspiratory + expiratory wheeze ชัดตรงกลางอก = central airway obstruction",
            topic="Wheeze localization", ref=[f"{D} หน้า 21–22"], nl=["2.2.10"], kind="old", src=OLD),
        mcq("RESP-01-02-3", """A 60-year-old man with severe COPD has had fever and yellow sputum for 3 days. BT 38.2°C, RR 28/min, BP 140/90 mmHg, SpO2 80%. There are fine crackles at the right lower lung and generalized wheezing. CXR shows alveolar infiltration in the right lower lobe. What is the most likely diagnosis?""",
            "COPD exacerbation triggered by right lower lobe pneumonia",
            ["COPD exacerbation without pneumonia",
             "Pulmonary embolism with pulmonary infarction",
             "Pulmonary tuberculosis",
             "Lung cancer with post-obstructive collapse"],
            explain="""มี wheeze ทั่วปอดและ hypoxemia (exacerbation) ร่วมกับไข้ เสมหะเหลือง fine crepitation และ alveolar infiltrate ที่ RLL (pneumonia) คำตอบที่ครบที่สุดคือ AECOPD ที่มี pneumonia เป็นตัวกระตุ้น การรักษาจึงต้องใช้ ATB ขนาดของ CAP
- AECOPD อย่างเดียวไม่ได้อธิบาย infiltrate และ crepitation เฉพาะที่
- PE with infarction ให้ pleuritic pain เฉียบพลัน และ wedge-shaped opacity (Hampton hump) มักไม่มีเสมหะเหลือง
- Pulmonary TB เป็นแบบ subacute หลายสัปดาห์ รอยโรคอยู่ที่ upper lobe หรือเป็น cavity
- Lung cancer ไม่ทำให้มีไข้เฉียบพลัน 3 วันพร้อมเสมหะเหลือง""",
            pearl="AECOPD + new infiltrate → รักษาแบบ pneumonia ด้วย",
            topic="AECOPD vs pneumonia", ref=[f"{D} หน้า 23–24"], nl=["2.2.11", "2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-01-02-4", """A 68-year-old man with COPD presents with worsening dyspnea and increased purulent sputum. He is using accessory muscles. On O2 mask, SpO2 is 90%. ABG: pH 7.30, PaCO2 60 mmHg, HCO3 29 mEq/L, PaO2 62 mmHg. He has received nebulized salbutamol/ipratropium and IV methylprednisolone. What is the most appropriate next step?""",
            "Start noninvasive positive-pressure ventilation",
            ["Increase oxygen to keep SpO2 at 98–100%",
             "Immediate endotracheal intubation",
             "Give IV sodium bicarbonate",
             "Start IV aminophylline as the next step"],
            explain="""pH 7.30 กับ PaCO2 60 คือ acute on chronic respiratory acidosis (HCO3 29 แสดงว่ามี metabolic compensation จากภาวะเรื้อรังอยู่ก่อน) เข้าเกณฑ์ NIPPV คือ pH ≤ 7.35 และ PaCO2 ≥ 45 ร่วมกับใช้ accessory muscles ผู้ป่วยยังรู้สึกตัวและไม่มีข้อห้าม NIPPV ช่วยลดอัตราการใส่ท่อและอัตราตาย
- การเพิ่ม O2 ให้ SpO2 98–100% ทำให้ PaCO2 สูงขึ้นอีก เป้าหมายคือ 88–92%
- การใส่ท่อทันทีเก็บไว้ใช้เมื่อ NIPPV ไม่ได้ผล ซึม หรือมีข้อห้าม NIPPV
- Bicarbonate ไม่ใช่การรักษา respiratory acidosis ต้องแก้ที่การระบายอากาศ
- Aminophylline มีผลข้างเคียงมาก และไม่ใช่ขั้นตอนถัดไปตามสไลด์""",
            pearl="AECOPD + pH ≤ 7.35 + PaCO2 ≥ 45 → NIPPV ก่อน ETT",
            topic="AECOPD NIPPV", ref=[f"{D} หน้า 12"], nl=["2.2.11", "3.3.17"]),
        mcq("RESP-01-02-5", """A 66-year-old woman with COPD has 2 days of increased dyspnea and cough. Her sputum is white and unchanged in amount. She is alert, RR 22/min, SpO2 91% on room air, afebrile, and CXR shows hyperinflation without infiltrate. Which management is LEAST indicated?""",
            "Routine oral amoxicillin/clavulanate",
            ["Nebulized salbutamol with ipratropium",
             "Oral prednisone for a short course",
             "Controlled oxygen targeting SpO2 88–92%",
             "Review inhaler technique and smoking status before discharge"],
            explain="""Exacerbation ครั้งนี้ไม่มีเสมหะเป็นหนองมากขึ้น และไม่ได้ใช้เครื่องช่วยหายใจ ซึ่งส่วนใหญ่เกิดจาก virus ตามสไลด์จึงไม่ควรให้ ATB ทุกราย การให้ amoxicillin/clavulanate แบบ routine จึงเป็นข้อที่ไม่จำเป็นที่สุด
- NB salbutamol + ipratropium เป็นยาหลักของ AECOPD
- Prednisone ช่วงสั้น ๆ ทำให้ฟื้นตัวเร็วและลดการกำเริบซ้ำ
- O2 แบบควบคุมให้ SpO2 88–92% เหมาะกับ SpO2 91% ที่ยังเหนื่อย
- การทบทวนวิธีพ่นยาและการเลิกบุหรี่เป็นส่วนของการป้องกันการกำเริบซ้ำ""",
            pearl="ไม่มี purulent sputum และไม่ได้ on ventilator → ไม่ต้องให้ ATB ใน AECOPD",
            topic="AECOPD antibiotics", ref=[f"{D} หน้า 13–14"], nl=["2.2.11"]),
    ])

S3 = sec("resp-01-03", "COPD: การรักษาระยะยาว (GOLD)",
    "LABA หรือ LAMA → LABA+LAMA → +ICS เมื่อ eos ≥ 300 · เลิกบุหรี่ วัคซีน LTOT เมื่อ PaO2 ≤ 55",
    minutes=6, source=f"{D} หน้า 15–18, 25–28", nl=["2.3.10(3)", "B6.4(4)", "B6.4(5)"],
    md='''
### หลักการ
เป้าหมายคือ **ลดอาการ** และ **ลดการกำเริบ (exacerbation)** — ยาหลักคือ long-acting bronchodilator
- **LABA**: salmeterol, formoterol
- **LAMA**: tiotropium
- **ICS** ใช้เพิ่มเฉพาะคนที่กำเริบบ่อยและ **blood eosinophil ≥ 300 cells/µL** (ICS เพิ่มความเสี่ยง pneumonia — เสริม)

### ขั้นการให้ยาตามสไลด์
| Step | ยา |
|---|---|
| STEP 1 | LABA หรือ LAMA |
| STEP 2 | LABA + LAMA |
| STEP 3 | LABA + LAMA + ICS (เมื่อ blood eos ≥ 300) |

[[fig:resp-01-03-gold]]

| GOLD group | ยาเริ่มต้น |
|---|---|
| A | a bronchodilator (short หรือ long acting ก็ได้) |
| B | LABA + LAMA |
| E | LABA + LAMA (+ ICS ถ้า blood eos > 300) |

### ไม่ใช้ยา (ทำทุกคน)
- **Smoking cessation** — สิ่งเดียวที่ชะลอ FEV1 ที่ลดลงได้ชัด
- **Vaccine**: pneumococcal, influenza (ปีละครั้ง)
- Mucolytics: N-acetylcysteine
- **Pulmonary rehabilitation**, ใช้ยาสม่ำเสมอ (compliance)
- **Long-term oxygen therapy (LTOT)** เมื่อ **PaO2 ≤ 55 mmHg หรือ SaO2 ≤ 88% at rest** (ใช้ ≥ 15 ชม./วัน — เสริม) ช่วยลดอัตราตาย

> ป้องกัน exacerbation ตามสไลด์ = เลิกบุหรี่ · วัคซีน influenza/pneumococcal · compliance · pulmonary rehab

> ข้อสอบเก่า: "COPD กำเริบ 2 ครั้งใน 2 เดือน ให้ยาอะไรลดการกำเริบระยะยาว" ตัวเลือกมีแค่ SABA, SABA+SAMA, **LABA+ICS**, systemic steroid, theophylline → ตอบ LABA+ICS เพราะเป็นตัวเดียวที่เป็นยาควบคุมระยะยาว แต่ตามแนวทาง GOLD ปัจจุบัน (group E) ยาที่ควรเลือกคือ **LABA+LAMA** (ถ้ามีในตัวเลือกให้เลือกตัวนี้)
''',
    figs=[fig("resp-01-03-gold", "GOLD group A/B/E กับยาเริ่มต้น", FIG_GOLD,
              "แกนตั้งคือประวัติการกำเริบ แกนนอนคือความหนักของอาการ — group E ใช้ LABA+LAMA แล้วเติม ICS เฉพาะเมื่อ eos ≥ 300")],
    pearls=["COPD: LABA+LAMA เป็นแกนหลัก · ICS เติมเฉพาะ eos ≥ 300 + กำเริบบ่อย",
            "LTOT เมื่อ PaO2 ≤ 55 mmHg หรือ SaO2 ≤ 88% ขณะพัก",
            "เลิกบุหรี่ + วัคซีน influenza/pneumococcal ลดการกำเริบได้",
            "ไม่ใช้ ICS เดี่ยว ๆ ใน COPD (เสริม)"],
    items=[
        mcq("RESP-01-03-1", """A 65-year-old man with COPD has had 2 exacerbations requiring oral steroids in the past 2 months. CXR shows hyperinflation and increased AP diameter. He currently uses only PRN salbutamol. Which regimen is most appropriate to reduce future exacerbations?""",
            "LABA + LAMA (e.g., formoterol + tiotropium)",
            ["PRN SABA alone", "Scheduled SABA + SAMA",
             "Long-term oral prednisolone", "Oral sustained-release theophylline alone"],
            explain="""กำเริบ 2 ครั้งในช่วงเวลาสั้น จัดเป็น GOLD group E ยาเริ่มต้นคือ LABA + LAMA (ถ้า blood eos ≥ 300 ค่อยเติม ICS)
- SABA PRN ใช้บรรเทาอาการ ไม่ลดการกำเริบ
- SABA + SAMA เป็นยาออกฤทธิ์สั้น ใช้ตอน exacerbation ไม่ใช่ยาคุมระยะยาว
- Oral steroid ระยะยาวมีผลข้างเคียงมาก (กระดูกพรุน เบาหวาน ติดเชื้อ) และไม่แนะนำ
- Theophylline ออกฤทธิ์อ่อน therapeutic window แคบ ไม่ใช่ทางเลือกแรก
หมายเหตุ: ข้อสอบเก่าในสไลด์ไม่มีตัวเลือก LABA+LAMA จึงเฉลยว่า LABA + ICS""",
            pearl="COPD กำเริบบ่อย (group E) → LABA + LAMA ± ICS ตาม eos",
            topic="COPD maintenance", ref=[f"{D} หน้า 16–17, 25–26"], nl=["2.3.10(3)", "B6.4(4)"], kind="old", src=OLD),
        mcq("RESP-01-03-2", """A 60-year-old chronic smoker with progressive dyspnea has FEV1/FVC 0.60 and FEV1 30% predicted. Which intervention most clearly reduces the risk of future exacerbations?""",
            "Annual influenza vaccination",
            ["Regular high-protein diet", "Daily oral antihistamine",
             "Routine prophylactic amoxicillin every winter", "Long-term oral codeine"],
            explain="""ตามสไลด์ การป้องกัน COPD exacerbation ได้แก่ เลิกบุหรี่ วัคซีน influenza และ pneumococcal กินยาสม่ำเสมอ และ pulmonary rehab — การฉีดวัคซีนไข้หวัดใหญ่ทุกปีลดการกำเริบที่เกิดจาก virus ได้
- อาหารโปรตีนสูงช่วยเรื่องโภชนาการ แต่ไม่มีหลักฐานว่าลดการกำเริบ
- Antihistamine ไม่มีบทบาทใน COPD และทำให้เสมหะเหนียวขึ้น
- การให้ amoxicillin ป้องกันแบบ routine ไม่แนะนำ (macrolide ใช้เฉพาะบางรายที่เลือกแล้ว)
- Codeine กดการไอและกดการหายใจ เป็นอันตรายใน COPD รุนแรง""",
            pearl="Vaccine influenza + pneumococcal ทุกคนที่เป็น COPD",
            topic="COPD prevention", ref=[f"{D} หน้า 18, 27–28"], nl=["2.3.10(3)", "B1.4.8"], kind="old", src=OLD),
        mcq("RESP-01-03-3", """A 72-year-old man with stable COPD on LABA/LAMA has resting room-air ABG: pH 7.39, PaCO2 48 mmHg, HCO3 28 mEq/L, PaO2 52 mmHg (SaO2 86%). He quit smoking 1 year ago. Which additional therapy improves survival?""",
            "Long-term oxygen therapy for at least 15 hours per day",
            ["Add inhaled corticosteroid regardless of eosinophil count",
             "Nocturnal oxygen only when SpO2 drops below 80%",
             "Oral N-acetylcysteine",
             "Regular nebulized salbutamol four times daily"],
            explain="""PaO2 52 mmHg (≤ 55) และ SaO2 86% (≤ 88%) ขณะพักและอาการคงที่ เข้าเกณฑ์ LTOT ซึ่งเป็นหนึ่งในไม่กี่การรักษาที่ลดอัตราตายใน COPD (ร่วมกับการเลิกบุหรี่) ค่า ABG นี้ตรงกับ chronic compensated respiratory acidosis (pH ปกติ HCO3 สูง)
- การเติม ICS โดยไม่ดู eos ไม่เพิ่ม survival และเพิ่มความเสี่ยง pneumonia
- การให้ O2 เฉพาะกลางคืนและรอให้ SpO2 ลดต่ำกว่า 80% ไม่ใช่เกณฑ์ที่ถูก
- N-acetylcysteine ช่วยละลายเสมหะ แต่ไม่ช่วยให้อยู่รอดนานขึ้น
- พ่นยาขยายหลอดลมเพิ่มช่วยเรื่องอาการ แต่ไม่ลดอัตราตาย""",
            pearl="LTOT: PaO2 ≤ 55 หรือ SaO2 ≤ 88% at rest → ลด mortality",
            topic="LTOT", ref=[f"{D} หน้า 18"], nl=["2.3.10(3)"]),
        mcq("RESP-01-03-4", """A 64-year-old woman with COPD (GOLD group E) remains on LABA + LAMA and still had 2 exacerbations this year. Blood eosinophil count is 420 cells/µL. What is the most appropriate change?""",
            "Add an inhaled corticosteroid (triple therapy)",
            ["Switch to ICS monotherapy", "Stop LAMA and use LABA + ICS",
             "Add oral montelukast", "Add daily oral prednisolone 10 mg"],
            explain="""ใช้ LABA + LAMA แล้วยังกำเริบบ่อย และ blood eos ≥ 300 เป็นข้อบ่งชี้ให้เติม ICS เป็น LABA + LAMA + ICS (STEP 3 ตามสไลด์)
- ICS เดี่ยวไม่ใช้ใน COPD
- การหยุด LAMA เป็นการถอยการรักษา เพราะ LAMA ลดการกำเริบได้ดี
- Montelukast ไม่มีบทบาทใน COPD
- Oral steroid ระยะยาวมีผลข้างเคียงสูงและไม่แนะนำ""",
            pearl="Eos ≥ 300 + ยังกำเริบบน LABA/LAMA → เติม ICS",
            topic="Triple therapy", ref=[f"{D} หน้า 16–17"], nl=["B6.4(5)"]),
    ])

S4 = sec("resp-01-04", "Asthma: อาการและการวินิจฉัย",
    "Clinical + FEV1/FVC < 0.7 + variability ≥ 1 ข้อ (BD ↑FEV1 ≥ 12% และ 200 ml, methacholine ↓ ≥ 20%, PEF)",
    minutes=6, source=f"{D} หน้า 29–33, 42–47", nl=["2.3.10(1)", "3.3.18"],
    md='''
### ใครเป็น และกลไก
Asthma = **chronic airway inflammation** ทำให้หลอดลมไวเกิน (hyperresponsiveness) และตีบแบบ **กลับคืนได้ (reversible / variable)**
- **Risk**: atopy, allergy, กรรมพันธุ์, มลพิษ
- **Trigger**: ออกกำลังกาย, อากาศเย็น, allergen, ควัน
- **Comorbid**: allergic rhinitis, eczema

### อาการ
- ไอแห้งเรื้อรัง, เหนื่อย, **เป็นมากตอนกลางคืน/เช้ามืด**
- **Expiratory wheezing**
- ช่วงที่ไม่มีอาการ ตรวจร่างกายและ CXR อาจปกติ → ต้องพึ่ง PFT

### การวินิจฉัย (ต้องมีทุกข้อ)
1. **Clinical** เข้าได้
2. **Airflow obstruction**: FEV1/FVC < 0.7
3. **Variability ของ lung function** อย่างน้อย 1 ข้อ

| วิธี | เกณฑ์บวก |
|---|---|
| Spirometry หลังพ่น bronchodilator | FEV1 ↑ ≥ 12% **และ** ≥ 200 ml |
| Spirometry หลังรักษา 4 สัปดาห์ | FEV1 ↑ ≥ 12% และ ≥ 200 ml |
| Methacholine challenge test | FEV1 ↓ ≥ 20% |
| PEF variability 2 สัปดาห์ (ถ้าไม่มี spirometry) | > 10% |
| PEF หลังพ่น bronchodilator | ↑ ≥ 20% |
| PEF หลังรักษา 4 สัปดาห์ | ↑ ≥ 20% |

> **Predicted peak flow = ส่วนสูง (cm) × 5 − 400 (L/min)** เช่น สูง 160 cm → 800 − 400 = 400 L/min

#### Allergy workup
- Allergen-specific IgE ↑, skin prick test — หา trigger ไว้หลีกเลี่ยง

> โจทย์คลาสสิก: ไอ/หอบ เป็นตอนกลางคืนหรืออากาศเย็น ตรวจร่างกายและ CXR ปกติ → investigation ที่เหมาะคือ **pulmonary function test (spirometry)** ไม่ใช่ CT หรือ bronchoscopy

> คนอายุน้อยที่สูบบุหรี่ แต่อาการเป็นช่วงกลางคืนและอากาศเย็น → ยังคิดถึง **asthma** ก่อน chronic bronchitis
''',
    pearls=["Asthma Dx = clinical + FEV1/FVC < 0.7 + variability ≥ 1 ข้อ",
            "Methacholine challenge บวกเมื่อ FEV1 ลด ≥ 20%",
            "PEF: variability > 10% ใน 2 สัปดาห์ หรือ ↑ ≥ 20% หลังพ่นยา",
            "Predicted PEF = Ht(cm) × 5 − 400 L/min",
            "อาการกลางคืน/อากาศเย็น + PE และ CXR ปกติ → ส่ง PFT"],
    items=[
        mcq("RESP-01-04-1", """A 30-year-old man who smokes half a pack per day for 15 years presents with dyspnea for 2 hours. He has a history of cough and wheeze that typically occur at night and in cold weather. What is the most likely diagnosis?""",
            "Asthma",
            ["Bronchiectasis", "Chronic bronchitis", "Pulmonary tuberculosis", "Bronchogenic carcinoma"],
            explain="""อาการไอ หอบ ที่มักเป็นช่วงกลางคืนและเมื่ออากาศเย็น เป็นลักษณะของ variable airflow obstruction ใน asthma อายุ 30 ปียังน้อยเกินไปสำหรับ COPD
- Bronchiectasis เด่นที่เสมหะหนองปริมาณมากทุกวัน
- Chronic bronchitis ต้องไอมีเสมหะเกือบทุกวัน ≥ 3 เดือนต่อปีติดกัน 2 ปี ไม่ได้เป็นตามช่วงเวลา
- Pulmonary TB มีไข้ต่ำ น้ำหนักลด ไอเรื้อรังต่อเนื่อง ไม่สัมพันธ์กับอากาศเย็น
- Bronchogenic carcinoma ไม่น่าเป็นในอายุ 30 ปี และไม่มีลักษณะเป็นช่วงเวลา""",
            pearl="อาการกลางคืน + อากาศเย็น = variable obstruction = asthma",
            topic="Asthma clinical", ref=[f"{D} หน้า 42–43"], nl=["2.3.10(1)"], kind="old", src=OLD),
        mcq("RESP-01-04-2", """A 40-year-old man has had dry cough for 1 month, worse in cold weather and in the evening, occasionally with scant white sputum. Physical examination and CXR are normal. What is the most appropriate investigation?""",
            "Pulmonary function test (spirometry with bronchodilator)",
            ["Allergen skin test", "CT chest", "Sputum AFB", "Bronchoscopy"],
            explain="""อาการเข้ากับ asthma (cough-variant) และ CXR ปกติ การตรวจที่ยืนยันได้คือ spirometry พร้อม bronchodilator test เพื่อดู obstruction และ reversibility
- Skin prick test ใช้หาสารก่อภูมิแพ้หลังวินิจฉัย asthma แล้ว ไม่ได้ใช้วินิจฉัย
- CT chest ไม่ช่วยวินิจฉัย asthma และโดนรังสีโดยไม่จำเป็น
- Sputum AFB ใช้เมื่อสงสัย TB ซึ่งต้องมีไข้ น้ำหนักลด หรือ CXR ผิดปกติ
- Bronchoscopy เป็นหัตถการรุกล้ำ ใช้หา central lesion ไม่ใช้วินิจฉัย asthma""",
            pearl="สงสัย asthma + CXR ปกติ → spirometry",
            topic="Asthma investigation", ref=[f"{D} หน้า 44–45"], nl=["3.3.18"], kind="old", src=OLD),
        mcq("RESP-01-04-3", """A 22-year-old woman reports episodic chest tightness after exercise. Spirometry at rest is normal (FEV1/FVC 0.82) with no bronchodilator response. Asthma is still suspected. Which test result would best confirm the diagnosis?""",
            "Methacholine challenge causing a 25% fall in FEV1",
            ["Methacholine challenge causing a 10% fall in FEV1",
             "PEF diurnal variability of 6% over 2 weeks",
             "Total serum IgE above the reference range",
             "Chest X-ray showing hyperinflation"],
            explain="""เมื่อ spirometry ปกติแต่ยังสงสัย asthma ให้ทำ bronchial provocation ถ้า methacholine ทำให้ FEV1 ลดลง ≥ 20% ถือว่าบวก แสดงว่ามี airway hyperresponsiveness ลดลง 25% จึงยืนยันได้
- FEV1 ลด 10% ไม่ถึงเกณฑ์ 20%
- PEF variability ต้องมากกว่า 10% ค่า 6% ถือว่าปกติ
- IgE สูงบอกภาวะ atopy แต่ไม่ได้ยืนยัน variable airflow obstruction
- CXR ที่เห็น hyperinflation ไม่จำเพาะ และไม่ใช้วินิจฉัย asthma""",
            pearl="Methacholine: FEV1 ↓ ≥ 20% = บวก",
            topic="Bronchial provocation", ref=[f"{D} หน้า 31"], nl=["3.3.18", "2.3.10(1)"]),
        mcq_ordered("RESP-01-04-4", """A 34-year-old man, height 170 cm, has suspected asthma. Using the formula from the lecture, what is his approximate predicted peak expiratory flow?""",
            ["350 L/min", "400 L/min", "450 L/min", "500 L/min", "550 L/min"], 2,
            explain="""Predicted PEF = ส่วนสูง (cm) × 5 − 400 = 170 × 5 − 400 = 850 − 400 = 450 L/min
- 350 และ 400 L/min ได้จากการลบหรือคูณผิด (เช่นใช้ 150 หรือ 160 cm)
- 500 และ 550 L/min สูงเกินกว่าค่าที่คำนวณได้ ซึ่งมักเกิดจากลืมลบ 400 แล้วไปปรับเองภายหลัง
ค่านี้ใช้เป็นเป้าเทียบตอนประเมินความรุนแรงของ exacerbation เช่น PEF < 50% predicted ถือว่ารุนแรง (เสริม)""",
            pearl="Predicted PEF = Ht × 5 − 400",
            topic="Peak flow", ref=[f"{D} หน้า 30"], nl=["3.3.18"]),
        mcq("RESP-01-04-5", """An 18-year-old healthy male has had dyspnea and wheeze during exercise and at night 2–3 times in the past month. Physical examination today is normal. What is the most appropriate next step?""",
            "Spirometry with bronchodilator reversibility testing",
            ["Start oral montelukast without testing", "CT chest with contrast",
             "Echocardiography", "Reassure that exercise-related dyspnea is physiological"],
            explain="""อาการหอบตอนออกกำลังและกลางคืนเป็นพัก ๆ ต้อง rule in asthma ด้วย spirometry ก่อนเริ่มยาคุมระยะยาว ตามสไลด์คือ R/O asthma แล้วส่ง PFT
- การเริ่ม montelukast โดยไม่ตรวจ ข้ามขั้นการวินิจฉัย และไม่ใช่ยาแรกตาม GINA
- CT chest ไม่ช่วยวินิจฉัย asthma
- Echo ใช้เมื่อสงสัยโรคหัวใจ ซึ่งชายอายุ 18 ปีที่ตรวจร่างกายปกติไม่มีข้อบ่งชี้
- การบอกว่าเป็นอาการปกติจากการออกกำลังทำให้พลาดการวินิจฉัย เพราะมีอาการกลางคืนร่วมด้วย""",
            pearl="สงสัย asthma → ยืนยันด้วย spirometry ก่อนรักษาระยะยาว",
            topic="Asthma workup", ref=[f"{D} หน้า 46–47"], nl=["3.3.18"], kind="old", src=OLD),
    ])

S5 = sec("resp-01-05", "Asthma exacerbation",
    "Mild–mod: O2 + NB salbutamol + pred PO · Severe: + ipratropium, IV steroid, ± MgSO4 · Respiratory failure → ETT",
    minutes=7, source=f"{D} หน้า 34–36, 48–63, 67–68", nl=["2.2.11", "2.3.10(1)", "2.2.9"],
    md='''
### ประเมินความรุนแรง (สไลด์ 34 เป็นภาพ — สรุปจาก GINA, เสริม)
| | Mild–moderate | Severe | Life-threatening |
|---|---|---|---|
| พูด | เป็นประโยค/วลี | เป็นคำ ๆ | ซึม สับสน |
| RR | ↑ | > 30/min | — |
| PR | 100–120 | > 120 | bradycardia |
| SpO2 (RA) | 90–95% | < 90% | — |
| PEF | > 50% predicted | ≤ 50% | — |
| ตรวจ | wheeze | accessory muscles | **silent chest** |

> **Silent chest** (ฟังไม่ได้ยิน wheeze เพราะลมผ่านน้อยมาก) และ **PaCO2 ปกติหรือสูง** ในคนหอบ = ใกล้ respiratory failure

[[fig:resp-01-05-ex]]

### การรักษาตามสไลด์
#### Mild – moderate
- O2 mask with bag
- **NB SABA: salbutamol**
- **Systemic steroid: prednisone PO** (ให้ตั้งแต่แรก)

#### Severe
- O2 mask with bag · **ETT เมื่อ respiratory failure**
- **SABA + SAMA**: salbutamol + ipratropium bromide
- Systemic steroid: prednisone PO หรือ methylprednisolone IV, dexamethasone IV
- ± **IV MgSO4** / high-dose ICS

### อ่าน ABG ใน asthma (เสริม)
- ช่วงแรกหายใจเร็ว → **respiratory alkalosis (PaCO2 ต่ำ)** เป็นเรื่องปกติ
- ถ้า PaCO2 กลับมา "ปกติ" (40) ทั้งที่ยังหอบ = กล้ามเนื้อหายใจเริ่มล้า
- **pH 7.10 + PaCO2 70** = acute respiratory acidosis → **ใส่ ETT**

### หลังให้ยา 1 ชม.
- ดีขึ้น (PEF ดีขึ้นชัด สัญญาณชีพดี) → สังเกตอาการต่อ แล้ว D/C พร้อม oral steroid + step up controller (เสริม)
- ได้ SABA และ IV steroid แล้ว PEF ยังต่ำมาก ยังเหนื่อย → **admit**

### กับดักในข้อสอบเก่า
- **Stridor + wheeze** ที่ไม่ตอบสนองต่อ SABA → คิดถึง upper airway obstruction/anaphylaxis → **epinephrine (adrenaline) NB/IM** ไม่ใช่เพิ่ม bronchodilator
- คนไข้ asthma ใส่ ETT แล้ว agitation, CXR เห็น **RUL atelectasis** (เสมหะอุด) → **suction และเอาเสมหะออก** ไม่ใช่ sedative
- คนไข้ได้ O2 + salbutamol NB แล้ว ขั้นต่อไปที่ต้องได้คือ **systemic corticosteroid** (เช่น dexamethasone IV) — theophylline, terbutaline SC ไม่ใช่ยาหลักแล้ว
''',
    figs=[fig("resp-01-05-ex", "Asthma exacerbation ตามความรุนแรง", FIG_ASTHMA_EX,
              "แบ่งตามความรุนแรงก่อน: ทุกระดับได้ O2 + SABA + systemic steroid, ระดับ severe เติม ipratropium, IV steroid, MgSO4 และพร้อมใส่ท่อ")],
    pearls=["ทุก exacerbation: O2 + SABA + systemic steroid (อย่าลืม steroid)",
            "Severe: เติม ipratropium ± IV MgSO4 · respiratory failure → ETT",
            "Asthma + PaCO2 ปกติ/สูง หรือ silent chest = ใกล้ใส่ท่อ",
            "Stridor + wheeze ไม่ตอบสนอง SABA → epinephrine",
            "Asthma on ventilator + agitation + lobar atelectasis → suction"],
    items=[
        mcq("RESP-01-05-1", """A 40-year-old man with asthma has had a cold for 2 days. His home inhaler no longer helps. BT 37.4°C, BP 110/90 mmHg, PR 100/min, RR 28/min. There is wheezing at both lower lungs with accessory muscle use. What is the most appropriate initial management?""",
            "Nebulized salbutamol",
            ["Subcutaneous terbutaline", "IV aminophylline",
             "IV antibiotic for bronchitis", "Oral montelukast"],
            explain="""Asthma exacerbation ที่มี accessory muscle use รักษาด้วย O2 และ NB SABA (salbutamol) ทันที ร่วมกับ systemic steroid ในขั้นตอนเดียวกัน
- Terbutaline SC ใช้เมื่อพ่นยาไม่ได้หรือไม่มียาพ่น ไม่ใช่ทางเลือกแรก
- Aminophylline ได้ผลน้อยและมีพิษต่อหัวใจ จึงไม่ใช้เป็นยาแรก
- ATB ไม่จำเป็น เพราะส่วนใหญ่ trigger มาจาก viral URI และผู้ป่วยไม่มีไข้
- Montelukast ออกฤทธิ์ช้า ไม่ใช้รักษาอาการเฉียบพลัน
(ข้อสอบเก่านี้มีทั้ง IV steroid และ NB salbutamol ในตัวเลือก — เฉลยคือ NB salbutamol เพราะเป็นยาที่ต้องให้ก่อน)""",
            pearl="Asthma attack: SABA NB ก่อน แล้ว systemic steroid ตาม",
            topic="Asthma exacerbation", ref=[f"{D} หน้า 50–51"], nl=["2.2.11"], kind="old", src=OLD),
        mcq("RESP-01-05-2", """A patient with an acute asthma attack is in moderate distress. He has received oxygen and nebulized salbutamol. Which additional treatment should he receive now?""",
            "IV dexamethasone (systemic corticosteroid)",
            ["Subcutaneous terbutaline", "IV theophylline",
             "Nebulized beclomethasone only", "IV diphenhydramine"],
            explain="""Asthma exacerbation ทุกระดับต้องได้ systemic corticosteroid ร่วมกับ SABA เพื่อลดการอักเสบและลดการกลับเป็นซ้ำ ให้ทาง PO หรือ IV ก็ได้
- Terbutaline SC เป็น β2 agonist อีกตัว ซ้ำกับ salbutamol ที่ได้ไปแล้ว
- Theophylline IV ประสิทธิภาพต่ำ ผลข้างเคียงสูง
- Beclomethasone NB อย่างเดียวไม่แทน systemic steroid ในภาวะเฉียบพลัน
- Antihistamine ไม่มีบทบาทใน asthma exacerbation""",
            pearl="อย่าลืม systemic steroid ในทุก asthma exacerbation",
            topic="Systemic steroid", ref=[f"{D} หน้า 35–36, 56–57"], nl=["2.2.11"], kind="old", src=OLD),
        mcq("RESP-01-05-3", """A 28-year-old woman with a severe asthma attack is on an oxygen mask at 10 L/min with SpO2 90%. She is drowsy and has a silent chest despite nebulized salbutamol/ipratropium and IV steroid. ABG: pH 7.10, PaCO2 70 mmHg, HCO3 21 mEq/L. What is the most appropriate management?""",
            "Endotracheal intubation and mechanical ventilation",
            ["Continue nebulized salbutamol and repeat ABG in 1 hour",
             "IV sodium bicarbonate infusion", "Start BiPAP and send home if improved",
             "IV aminophylline loading"],
            explain="""pH 7.10 และ PaCO2 70 คือ acute respiratory acidosis (HCO3 ยังปกติ แสดงว่าเกิดเฉียบพลัน) ร่วมกับซึมและ silent chest เป็น life-threatening asthma ที่มี respiratory failure ต้องใส่ ETT ตามสไลด์
- การพ่นยาต่อแล้วรอ 1 ชม. อันตราย เพราะผู้ป่วยกำลังจะหยุดหายใจ
- Bicarbonate ไม่แก้ปัญหาการระบายอากาศ และทำให้ CO2 สูงขึ้นอีก
- BiPAP ใน asthma ที่ซึมแล้วไม่ปลอดภัย ระดับความรู้สึกตัวที่ลดลงเป็นข้อห้าม
- Aminophylline ไม่ช่วยแก้ respiratory failure""",
            pearl="Asthma + ซึม/silent chest/PaCO2 สูง → ETT",
            topic="Respiratory failure in asthma", ref=[f"{D} หน้า 36, 52–53"], nl=["2.2.9", "2.2.11"], kind="old", src=OLD),
        mcq("RESP-01-05-4", """A 20-year-old woman has had sudden dyspnea for 15 minutes. Examination shows inspiratory stridor and expiratory wheezing. Three doses of inhaled SABA did not help. What is the most appropriate next step?""",
            "Epinephrine",
            ["Nebulized ipratropium", "Oral corticosteroid", "Nebulized terbutaline", "IV theophylline"],
            explain="""Stridor บอกว่ามี upper airway obstruction (เช่น laryngeal edema จาก anaphylaxis) ร่วมกับ wheeze เฉียบพลันที่ไม่ตอบสนองต่อ SABA ยาที่ช่วยได้เร็วทั้ง upper airway edema และ bronchospasm คือ epinephrine (IM หรือ NB)
- Ipratropium และ terbutaline ขยายหลอดลมส่วนล่าง ไม่ลดการบวมของกล่องเสียง
- Oral steroid ออกฤทธิ์ช้าหลายชั่วโมง
- Theophylline IV ไม่ช่วยภาวะ upper airway obstruction""",
            pearl="Stridor + wheeze ที่ไม่ตอบ SABA → epinephrine",
            topic="Stridor", ref=[f"{D} หน้า 54–55"], nl=["2.2.10"], kind="old", src=OLD),
        mcq("RESP-01-05-5", """A 32-year-old woman intubated for status asthmaticus becomes agitated and restless despite ventilator support. Peak airway pressure rises. CXR shows opacification of the right upper lobe with elevation of the minor fissure and tracheal shift to the right. What is the most appropriate management?""",
            "Suction to remove the mucus plug and secretions",
            ["Increase PEEP", "Give a sedative and paralytic only",
             "Insert an intercostal chest drain on the right", "Thoracotomy"],
            explain="""Opacity ของ RUL ร่วมกับ minor fissure ที่ถูกดึงขึ้นและ trachea ที่เบี่ยงไปข้างเดียวกัน คือ RUL atelectasis จากเสมหะอุด (พบบ่อยใน asthma) การรักษาคือ suction เอาเสมหะออก ถ้าไม่ได้ผลอาจต้องทำ bronchoscopy
- การเพิ่ม PEEP ใน asthma เพิ่ม air trapping และความเสี่ยง barotrauma
- Sedation อย่างเดียวกลบอาการ แต่ไม่ได้แก้สาเหตุ
- ICD ใช้กับ pneumothorax ซึ่ง trachea จะเบี่ยงไปฝั่งตรงข้าม ไม่ใช่ฝั่งเดียวกัน
- Thoracotomy ไม่มีข้อบ่งชี้""",
            pearl="Atelectasis ดึง trachea เข้าหา · pneumothorax/effusion ดันออก",
            topic="Atelectasis on ventilator", ref=[f"{D} หน้า 67–68"], nl=["2.3.10(2)"], kind="old", src=OLD),
        mcq("RESP-01-05-6", """A man with asthma on budesonide 800 mcg/day presents with RR 26/min and PEF 150 L/min (predicted 400). After 2 doses of nebulized salbutamol and IV dexamethasone, 1 hour later RR is 25/min and PEF 300 L/min, but he still has mild wheeze. What is the most appropriate management?""",
            "Observe for another hour, recording RR, PR and PEF before deciding disposition",
            ["Discharge immediately on his previous regimen with follow-up in 4 weeks",
             "Discharge on budesonide 1600 mg/day",
             "Admit to ICU for intubation",
             "Give IV aminophylline and discharge"],
            explain="""PEF ดีขึ้นจาก 38% เป็น 75% predicted แต่ยังมี wheeze และ RR 25/min การตอบสนองครั้งนี้ยังไม่คงที่ ตามข้อสอบเก่าในสไลด์ให้สังเกตอาการต่อและบันทึก RR, PR, PEF ก่อนตัดสินใจ — ถ้าคงที่ค่อย D/C พร้อม oral steroid และ step up controller (เสริม)
- การ D/C ทันทีด้วยยาเดิมเสี่ยงกลับมาซ้ำ เพราะยังไม่ได้ดูว่าคงที่หรือไม่ และไม่ได้ปรับยา
- ตัวเลือก budesonide 1600 mg ใช้หน่วยผิด (ต้องเป็น mcg) และการ D/C ทันทีก็ยังเร็วเกินไป
- การ admit ICU เพื่อใส่ท่อเกินความจำเป็น เพราะผู้ป่วยดีขึ้นชัด
- Aminophylline ไม่มีที่ใช้ในจุดนี้""",
            pearl="ดีขึ้นแต่ยังไม่คงที่ → observe ต่อ แล้วค่อยตัดสินใจ D/C",
            topic="Disposition", ref=[f"{D} หน้า 62–63"], nl=["2.2.11"], kind="old", src=OLD),
    ])

S6 = sec("resp-01-06", "Asthma: การรักษาระยะยาว (GINA)",
    "Reliever PRN low-dose ICS/formoterol ทุก step · controller เพิ่มขนาด ICS/formoterol ตามอาการ · step 5 + LAMA",
    minutes=6, source=f"{D} หน้า 37–41, 64–66", nl=["2.3.10(1)", "B6.4(5)", "B6.4(4)"],
    md='''
### หลักการ GINA ปัจจุบัน (track 1 ตามสไลด์)
- ไม่ใช้ **SABA เดี่ยว** เป็น reliever อีกต่อไป เพราะไม่รักษาการอักเสบ และสัมพันธ์กับอัตราตาย (เสริม)
- Reliever ทุก step = **PRN low-dose ICS/formoterol** (เช่น budesonide/formoterol)
- Controller เพิ่มตามความถี่ของอาการ

[[fig:resp-01-06-gina]]

| Step | อาการ | Reliever | Controller |
|---|---|---|---|
| 1–2 | อาการ < 4–5 วัน/สัปดาห์ | PRN low-dose ICS/formoterol | — |
| 3 | อาการเกือบทุกวัน หรือตื่นกลางคืน ≥ 1/สัปดาห์ | PRN low-dose ICS/formoterol | Daily low-dose ICS/formoterol |
| 4 | อาการทุกวัน หรือตื่น ≥ 1/สัปดาห์ + lung function ต่ำ | PRN low-dose ICS/formoterol | Daily medium-dose ICS/formoterol |
| 5 | step 4 แล้วยังคุมไม่ได้ | PRN low-dose ICS/formoterol | Daily high-dose ICS/formoterol + add-on LAMA (tiotropium) ± biologic (anti-IgE/anti-IL5 — เสริม) |

### ไม่ใช้ยา
- หลีกเลี่ยง trigger/allergen (ฝุ่น เกสร ไรฝุ่น)
- Vaccine: pneumococcal, influenza
- F/U อาการ + spirometry

### ก่อน step up ต้องเช็ค (เสริม)
1. วิธีพ่นยาถูกไหม 2. กินยาสม่ำเสมอไหม 3. ยังสัมผัส trigger อยู่ไหม 4. มีโรคร่วม (rhinitis, GERD) ไหม

> ข้อสอบเก่า: ใช้ budesonide 400 mcg/วัน (ICS เดี่ยว ขนาดต่ำ–กลาง) แล้วยังหอบ ทั้งที่พ่นยาถูกและไม่ขาดยา PEF 50% → ยาเสริมที่ดีที่สุดคือ **inhaled LABA** (เปลี่ยนเป็น ICS/formoterol) — ดีกว่า LTRA, theophylline, anticholinergic; anti-IgE เก็บไว้ step 5
''',
    figs=[fig("resp-01-06-gina", "บันได GINA (track 1)", FIG_GINA,
              "ขั้นบันไดสูงขึ้นตามความถี่ของอาการ; reliever เหมือนกันทุกขั้นคือ PRN low-dose ICS/formoterol")],
    pearls=["GINA ปัจจุบัน: reliever = PRN low-dose ICS/formoterol ไม่ใช่ SABA เดี่ยว",
            "Step 3 low-dose · step 4 medium-dose · step 5 high-dose ICS/formoterol + LAMA",
            "ICS อย่างเดียวคุมไม่ได้ → เติม LABA (เป็น ICS/LABA) ดีกว่า LTRA/theophylline",
            "เช็ค technique + compliance ก่อน step up เสมอ"],
    items=[
        mcq("RESP-01-06-1", """A 42-year-old woman with asthma for 20 years uses inhaled budesonide 400 mcg/day. She still has daily wheeze despite correct inhaler technique, good adherence and no allergen exposure. She does not smoke. PEF is 50% predicted. Which add-on medication is most effective?""",
            "Inhaled long-acting β2 agonist (as ICS/formoterol)",
            ["Inhaled short-acting anticholinergic", "Oral leukotriene receptor antagonist",
             "Oral sustained-release theophylline", "Anti-IgE monoclonal antibody"],
            explain="""ผู้ป่วยคุมไม่ได้ทั้งที่ใช้ ICS เดี่ยว ขั้นต่อไปคือเติม LABA ให้เป็น ICS/formoterol (step 3–4) ซึ่งได้ผลดีกว่าการเพิ่มยาตัวอื่น
- Short-acting anticholinergic ใช้ตอน exacerbation ไม่ใช่ controller
- LTRA ใช้เป็นทางเลือกได้ แต่ได้ผลด้อยกว่า LABA
- Theophylline ได้ผลน้อยและมีพิษ
- Anti-IgE ใช้ใน step 5 หลังจากใช้ high-dose ICS/LABA แล้วยังคุมไม่ได้""",
            pearl="ICS เดี่ยวคุมไม่อยู่ → เติม LABA",
            topic="Asthma step-up", ref=[f"{D} หน้า 39, 64–66"], nl=["B6.4(4)", "B6.4(5)"], kind="old", src=OLD),
        mcq("RESP-01-06-2", """A 25-year-old newly diagnosed asthmatic has symptoms on 2 days per week and never wakes at night. Lung function is normal between episodes. According to current GINA track 1, what is the preferred regimen?""",
            "As-needed low-dose budesonide/formoterol only",
            ["As-needed salbutamol only", "Daily medium-dose ICS/formoterol plus as-needed salbutamol",
             "Daily montelukast", "Daily tiotropium"],
            explain="""อาการน้อยกว่า 4–5 วันต่อสัปดาห์จัดเป็น step 1–2 ตามสไลด์ ใช้ PRN low-dose ICS/formoterol อย่างเดียวโดยไม่ต้องมี controller ประจำ
- SABA เดี่ยวไม่แนะนำแล้ว เพราะไม่มีฤทธิ์ต้านการอักเสบ
- Medium-dose ICS/formoterol เป็น step 4 สูงเกินความจำเป็น
- Montelukast เป็นทางเลือกรอง ไม่ใช่ preferred
- Tiotropium ใช้เป็น add-on ใน step 5""",
            pearl="Step 1–2 = PRN ICS/formoterol อย่างเดียว",
            topic="GINA step 1–2", ref=[f"{D} หน้า 38–39"], nl=["2.3.10(1)", "B6.4(5)"]),
        mcq("RESP-01-06-3", """A 35-year-old man with asthma has symptoms most days of the week and wakes with cough once weekly. He uses only PRN low-dose budesonide/formoterol. Spirometry shows FEV1 85% predicted. What is the most appropriate controller?""",
            "Daily low-dose ICS/formoterol (maintenance and reliever)",
            ["Daily high-dose ICS/formoterol plus tiotropium", "Oral prednisolone 30 mg daily for 1 month",
             "Continue PRN only", "Add oral theophylline"],
            explain="""อาการเกือบทุกวันหรือตื่นกลางคืน ≥ 1 ครั้งต่อสัปดาห์ โดย lung function ยังดี เข้ากับ step 3 คือ daily low-dose ICS/formoterol และใช้ตัวเดียวกันเป็น reliever (MART)
- High-dose ICS/formoterol + LAMA เป็น step 5
- Oral steroid ระยะยาวไม่ใช่ controller เพราะผลข้างเคียงสูง
- ถ้าใช้ PRN ต่ออย่างเดียวจะคุมโรคไม่ได้
- Theophylline ไม่ใช่ทางเลือกตามแนวทาง""",
            pearl="Step 3 = daily low-dose ICS/formoterol",
            topic="GINA step 3", ref=[f"{D} หน้า 38–39"], nl=["B6.4(5)"]),
        mcq("RESP-01-06-4", """A 45-year-old woman with asthma on daily high-dose ICS/formoterol continues to have frequent exacerbations. Inhaler technique and adherence are confirmed. What is the next add-on therapy per the lecture?""",
            "Add a long-acting muscarinic antagonist (tiotropium)",
            ["Switch to PRN salbutamol only", "Reduce to low-dose ICS/formoterol",
             "Add an oral antihistamine", "Add a nebulized mucolytic"],
            explain="""ใช้ high-dose ICS/formoterol แล้วยังคุมไม่ได้ จัดเป็น step 5 ตามสไลด์ ให้เติม LAMA (tiotropium) ถ้ายังไม่ได้ผลจึงพิจารณา biologic หรือส่งต่อผู้เชี่ยวชาญ (เสริม)
- SABA อย่างเดียวเป็นการลดยาลงในผู้ป่วยที่คุมไม่ได้ เป็นอันตราย
- การลดเป็น low-dose ขัดกับหลัก step up
- Antihistamine และ mucolytic ไม่ใช่ add-on ของ asthma""",
            pearl="Step 5 = high-dose ICS/formoterol + LAMA",
            topic="GINA step 5", ref=[f"{D} หน้า 40"], nl=["B6.4(4)"]),
    ])

S7 = sec("resp-01-07", "Bronchiectasis",
    "หลอดลมขยายถาวรจากการติดเชื้อซ้ำ · เสมหะหนองมาก ไอเป็นเลือด · HRCT tram-track, signet-ring · macrolide ระยะยาว",
    minutes=6, source=f"{D} หน้า 69–77", nl=["2.3.10(5)", "B6.2.2(4)"],
    md='''
### กลไก
การติดเชื้อหรือการอักเสบซ้ำ ๆ ร่วมกับการกำจัดเสมหะที่บกพร่อง → ผนังหลอดลมถูกทำลาย → **หลอดลมขยายถาวร** → เสมหะคั่ง → ติดเชื้อซ้ำ (วงจรอุบาทว์)

**สาเหตุ**: pulmonary infection (TB, pneumonia รุนแรง — เสริม), cystic fibrosis, **ABPA**, COPD/smoking, immunodeficiency, autoimmune

### อาการ
- ไอเรื้อรังมีเสมหะ **ปริมาณมาก เป็นหนอง (copious mucopurulent sputum)**
- เหนื่อย, **ไอเป็นเลือด (hemoptysis)**
- Crepitation (coarse), wheezing · อาจมี clubbing (เสริม)

### Investigation
- **CXR** (เริ่มต้น): ในโรคระยะแรกมักไม่เห็นอะไร
- **HRCT chest** (gold standard): หลอดลมหนาและขยาย
  - **Tram-track**: ผนังหลอดลมหนาขนานกันสองเส้น (ตัดตามยาว)
  - **Signet-ring sign**: หลอดลมขยายใหญ่กว่าหลอดเลือดแดงที่วิ่งคู่กัน (ตัดขวาง)
  - Honeycombing, saccular หรือ cystic

### การรักษา
| | Acute exacerbation | Long-term |
|---|---|---|
| Airway | O2, mucolytics, airway clearance | airway clearance, mucolytics, bronchodilators |
| ATB | **amoxicillin/clavulanic acid, ciprofloxacin** | **azithromycin, erythromycin ≥ 3 เดือน** (ป้องกันการกำเริบ) |
| อื่น ๆ | — | เลิกบุหรี่, วัคซีน influenza/pneumococcal, รักษาสาเหตุ |

> ผู้ป่วยมีประวัติ TB + bronchiectasis มาด้วยไข้ ไอเป็นเลือด WBC สูง (PMN เด่น) CXR ไม่มีรอยโรคใหม่ AFB ลบ → **infected bronchiectasis** (ไม่ใช่ TB กลับเป็นซ้ำ หรือ aspergilloma)

> ทบทวน: ถ้า CXR เห็น **mobile fungus ball ใน cavity เก่า** ในคนที่เคยเป็น TB → aspergilloma (ดูหัวข้อ aspergillosis)
''',
    pearls=["Bronchiectasis: เสมหะหนองปริมาณมาก + hemoptysis + coarse crepitation",
            "HRCT: tram-track, signet-ring (bronchus ใหญ่กว่า artery คู่กัน)",
            "Exacerbation: amox/clav หรือ ciprofloxacin (คลุม Pseudomonas)",
            "ป้องกันการกำเริบ: macrolide (azithro/erythro) ≥ 3 เดือน"],
    items=[
        mcq("RESP-01-07-1", """A 65-year-old with a history of pulmonary tuberculosis and bronchiectasis presents with fever and hemoptysis for 1 day. BT 38°C. Coarse crackles are heard at the RUL. CXR shows old RUL infiltration without new infiltrate, mass or cavity. Hct 24%, WBC 12,500 (PMN 95%), platelets 250,000. Sputum AFB is negative. What is the most likely diagnosis?""",
            "Infected bronchiectasis",
            ["Aspergilloma", "Necrotizing pneumonia", "Recurrent pulmonary tuberculosis",
             "Ruptured pulmonary artery aneurysm"],
            explain="""มี bronchiectasis อยู่เดิม มาด้วยไข้เฉียบพลัน WBC สูงเด่น neutrophil และไอเป็นเลือด โดย CXR ไม่มีรอยโรคใหม่ เข้ากับ bronchiectasis ที่ติดเชื้อกำเริบ
- Aspergilloma ต้องเห็นก้อน fungus ball ใน cavity ซึ่ง CXR ไม่มี
- Necrotizing pneumonia ต้องมี consolidation ใหม่หรือ cavity
- TB กลับเป็นซ้ำมักเป็นแบบ subacute AFB บวก หรือมีรอยโรคใหม่
- Pulmonary artery aneurysm แตก (Rasmussen) ไอเป็นเลือดปริมาณมากมาก และควรเห็นรอยโรคใน cavity""",
            pearl="Bronchiectasis + ไข้ + hemoptysis + CXR ไม่เปลี่ยน = infected bronchiectasis",
            topic="Bronchiectasis exacerbation", ref=[f"{D} หน้า 74–75"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-01-07-2", """A 17-year-old boy has fever, dyspnea and green sputum. He has had recurrent chest infections since childhood. CXR shows a honeycomb appearance with ring shadows in both lower zones. What is the most likely diagnosis?""",
            "Bronchiectasis",
            ["COPD", "Recurrent aspiration pneumonia", "Idiopathic pulmonary fibrosis", "Pulmonary tuberculosis"],
            explain="""ติดเชื้อทางเดินหายใจซ้ำตั้งแต่เด็ก เสมหะเขียว และ CXR เห็นเงาวงแหวน/honeycomb (cystic bronchiectasis) เข้ากับ bronchiectasis ในคนอายุน้อยควรหาสาเหตุ เช่น CF หรือ immunodeficiency (เสริม)
- COPD ไม่เกิดในวัยรุ่นที่ไม่สูบบุหรี่
- Recurrent aspiration มักมีปัจจัยเสี่ยง เช่น กลืนลำบากหรือซึม และไม่ทำให้เกิดรอยโรค honeycomb
- IPF เกิดในผู้สูงอายุ ไอแห้ง ไม่มีเสมหะหนอง
- TB มักเป็นที่ upper lobe หรือเป็น cavity ไม่ใช่ ring shadows ทั้งสองข้าง""",
            pearl="วัยรุ่น + ติดเชื้อซ้ำ + เสมหะหนอง + ring shadows = bronchiectasis",
            topic="Bronchiectasis imaging", ref=[f"{D} หน้า 76–77"], nl=["2.3.10(5)"], kind="old", src=OLD),
        mcq("RESP-01-07-3", """A 50-year-old woman with chronic productive cough of copious purulent sputum and intermittent hemoptysis has a normal CXR. Which investigation is the gold standard for diagnosis?""",
            "High-resolution CT chest",
            ["Repeat CXR in 6 months", "Spirometry", "Bronchography with contrast", "Ventilation–perfusion scan"],
            explain="""CXR ไม่ไวพอใน bronchiectasis ระยะแรก ต้องใช้ HRCT ซึ่งเห็นผนังหลอดลมหนาและขยาย tram-track และ signet-ring sign
- การรอทำ CXR ซ้ำทำให้วินิจฉัยช้า
- Spirometry บอกได้แค่ว่ามี obstruction ไม่ได้ยืนยันโครงสร้างที่ผิดปกติ
- Bronchography เป็นวิธีเก่าที่ HRCT มาแทนแล้ว
- V/Q scan ใช้ประเมิน PE""",
            pearl="Bronchiectasis: HRCT = gold standard",
            topic="Bronchiectasis HRCT", ref=[f"{D} หน้า 70–71"], nl=["2.3.10(5)"]),
        mcq("RESP-01-07-4", """A 58-year-old man with bronchiectasis has 4 infective exacerbations per year despite airway clearance physiotherapy, vaccinations and smoking cessation. Sputum culture is negative for nontuberculous mycobacteria. Which long-term therapy is most appropriate to reduce exacerbations?""",
            "Long-term azithromycin for at least 3 months",
            ["Long-term oral prednisolone", "Inhaled corticosteroid monotherapy",
             "Oral amoxicillin only when sputum turns green", "Montelukast"],
            explain="""Bronchiectasis ที่กำเริบบ่อยแม้ทำ airway clearance แล้ว ตามสไลด์ให้ macrolide (azithromycin หรือ erythromycin) ต่อเนื่อง ≥ 3 เดือนเพื่อป้องกันการกำเริบ ก่อนเริ่มต้องตัด NTM ออกก่อน เพื่อไม่ให้เชื้อดื้อ macrolide (เสริม)
- Oral steroid เพิ่มความเสี่ยงติดเชื้อ
- ICS ไม่มีหลักฐานว่าช่วยใน bronchiectasis ที่ไม่มี asthma หรือ ABPA ร่วม
- การให้ amoxicillin เฉพาะตอนกำเริบเป็นการรักษา ไม่ใช่การป้องกัน
- Montelukast ไม่มีบทบาท""",
            pearl="Bronchiectasis กำเริบบ่อย → macrolide ระยะยาว ≥ 3 เดือน",
            topic="Bronchiectasis prevention", ref=[f"{D} หน้า 73"], nl=["2.3.10(5)"]),
    ])

LECTURE = lecture("01", "Obstructive lung diseases",
    subtitle="spirometry · COPD · asthma · bronchiectasis",
    objectives=["อ่าน spirometry แยก obstructive/restrictive และ reversible/irreversible ได้",
                "วินิจฉัยและรักษา AECOPD ตาม ABG (O2 88–92%, NIPPV, ETT) ได้",
                "เลือกยาระยะยาว COPD ตาม GOLD และ asthma ตาม GINA ได้",
                "จัดการ asthma exacerbation ตามความรุนแรง รวมถึงกับดัก stridor และ atelectasis ได้",
                "วินิจฉัยและรักษา bronchiectasis ได้"],
    sections=[S1, S2, S3, S4, S5, S6, S7])
