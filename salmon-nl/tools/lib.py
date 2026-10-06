"""helper สำหรับเขียนเนื้อหา Salmon NL เป็น Python

แต่ละหมวดเขียนเป็นไฟล์ parts/<set>/<lec>.py ที่กำหนดตัวแปร LECTURE แบบนี้

    from lib import lecture, sec, mcq, fig
    LECTURE = lecture("03", "Upper GI bleeding", "UGIB · PUD · varices", objectives=[...], sections=[
        sec("gi-03-01", "Approach to UGIB", "สรุปหนึ่งบรรทัด", minutes=6,
            source="สไลด์ NL2-GI หน้า 40–52", nl=["2.1.40"],
            md='''...markdown...
    [[fig:ugib-flow]]
    ...''',
            figs=[fig("ugib-flow", "แนวทางเมื่อมี UGIB", '''<svg viewBox="0 0 720 360">...</svg>''', "คำอธิบายใต้ภาพ")],
            pearls=["...", "..."],
            items=[
                mcq("GI-03-01", "A 58-year-old man ... Which is the most appropriate next step?",
                    "คำตอบที่ถูก", ["ตัวลวง 1", "ตัวลวง 2", "ตัวลวง 3", "ตัวลวง 4"],
                    explain="คำอธิบายไทย ...", pearl="...", topic="Glasgow-Blatchford",
                    ref=["สไลด์ NL2-GI หน้า 45"], nl=["2.1.40"]),
            ]),
    ])

แล้วรัน  python3 tools/assemble.py <set>  → รวมทุกไฟล์ใน parts/<set>/ เป็น data/<set>.json + สลับคำตอบ + ตรวจ
"""

def lecture(lec, title, subtitle="", objectives=None, sections=None, meq=None, osce=None,
            guidelines=None, nlGap=None):
    d = {"lec": lec, "title": title, "subtitle": subtitle, "objectives": objectives or [],
         "sections": sections or [], "meq": meq or [], "osce": osce or []}
    if guidelines:
        d["guidelines"] = guidelines
    if nlGap:
        d["nlGap"] = nlGap
    return d

def sec(id, title, summary, md, pearls, items, minutes=5, source="", nl=None, figs=None):
    return {"id": id, "title": title, "summary": summary, "minutes": minutes, "source": source,
            "nl": nl or [], "md": md.strip("\n"), "figs": figs or [], "pearls": pearls, "items": items}

def fig(id, title, svg, caption=""):
    return {"id": id, "title": title, "svg": svg.strip(), "caption": caption}

def mcq(id, stem, correct, distractors, explain, pearl, topic="", ref=None, nl=None,
        keep_order=False, kind="mcq", src=""):
    """correct = ตัวที่ถูก · distractors = ตัวลวง 4 ตัว · keep_order=True เมื่อตัวเลือกเป็นลำดับธรรมชาติ
    (ตัวเลข/ระยะ) ให้ใส่ตัวเลือกเรียงแล้วใน distractors และระบุตำแหน่งที่ถูกด้วย correct_index ผ่าน mcq_ordered"""
    assert len(distractors) == 4, id
    return {"id": id, "kind": kind, "stem": stem.strip(), "choices": [correct] + list(distractors),
            "answer": 0, "_raw": True, "explain": explain.strip(), "pearl": pearl, "topic": topic,
            "src": src, "ref": ref or [], "nl": nl or []}

def mcq_ordered(id, stem, choices, answer, explain, pearl, topic="", ref=None, nl=None, kind="mcq", src=""):
    """ตัวเลือกเรียงตามธรรมชาติ ไม่สลับ — ส่ง choices 5 ตัวและ index ที่ถูก"""
    assert len(choices) == 5, id
    return {"id": id, "kind": kind, "stem": stem.strip(), "choices": list(choices), "answer": answer,
            "explain": explain.strip(), "pearl": pearl, "topic": topic, "src": src,
            "ref": ref or [], "nl": nl or []}
