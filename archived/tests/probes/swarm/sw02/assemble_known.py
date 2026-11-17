#!/usr/bin/env python3
"""SW-02: assemble each attack task's Known inputs from Cloud's seeds, Wave 1's facts and the survey's questions, into DATA/known/<ID>.md."""
import glob, json, os
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
HEAD = ("The survey's lines are sub-agent self-checks. PROVED means a reader read it in the kit or a primary source. PROOF-SKETCH and MEASURED lines from the survey have had no worker's read: "
        "verify anything you lean on, and report any you find wrong. Where a survey line corrects an earlier input, trust the source you can read.")
facts, qs = {}, {}
for f in sorted(glob.glob(DATA + "/out/*/facts.jsonl")):
    who = f.split("/")[-2]
    if who.startswith("SM"):
        continue
    for line in open(f, encoding="utf-8"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        for x in (r.get("for") or []):
            facts.setdefault(str(x), []).append((who, r))
for f in sorted(glob.glob(DATA + "/out/*/questions.jsonl")):
    who = f.split("/")[-2]
    if who.startswith("SM"):
        continue
    for line in open(f, encoding="utf-8"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        fs = r.get("for") or []
        fs = fs if isinstance(fs, list) else [str(fs)]
        for x in fs:
            qs.setdefault(str(x).strip(), []).append((who, r))
IDS = ["AM-1", "AM-2", "AM-3", "AM-4", "AM-5", "CT-1", "CT-2", "CT-3", "CT-4", "CT-5", "CP-1", "CP-2", "CP-3", "CP-4", "CP-5", "CP-6", "PE-1", "PE-2", "PE-3", "P2-1", "P2-2", "P2-3",
       "P3-1", "P3-2", "P3-3", "BR-1", "BR-2", "BR-3", "BR-4", "BR-5", "BR-6", "XP-1", "XP-2", "XP-3", "XP-4", "XP-5", "HX-1", "HX-2"] + ["LN-%02d" % i for i in range(1, 14)]
extra = {}
p = os.path.join(DATA, "known", "extra.json")
if os.path.exists(p):
    extra = json.load(open(p, encoding="utf-8"))
for i in IDS:
    parts = []
    seed = os.path.join(DATA, "known", i + ".seed.md")
    if os.path.exists(seed):
        parts.append(open(seed, encoding="utf-8").read().strip())
    if i in extra:
        parts.append(extra[i])
    seen, lines = set(), []
    for who, r in facts.get(i, []):
        st = str(r.get("statement", "")).strip()
        k = st[:80]
        if k in seen:
            continue
        seen.add(k)
        lines.append("- %s [status: %s; population: %s; cite: %s; survey %s]" % (st, r.get("status", "?"), r.get("population", "?"), r.get("cite", "?"), who))
    if lines:
        parts.append("From the survey (Wave 1):\n" + "\n".join(lines))
    ql = ["- %s" % str(r.get("question", "")).strip() for who, r in qs.get(i, [])]
    if ql:
        parts.append("Questions the survey raised for you; take any you can:\n" + "\n".join(ql))
    txt = HEAD + "\n\n" + "\n\n".join(parts) if parts else "(None listed; search the record.)"
    open(os.path.join(DATA, "known", i + ".md"), "w", encoding="utf-8").write(txt)
print({i: os.path.getsize(os.path.join(DATA, "known", i + ".md")) // 1024 for i in IDS})
