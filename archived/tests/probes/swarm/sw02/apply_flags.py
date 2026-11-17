#!/usr/bin/env python3
"""apply_flags.py [--write]: turn SW-02's verified status flags into dated notes in the record, as SW-01 did. Material or CONFIRMED flags on repository
files only; kit, portal and design flags are listed for the results page. The line is found by its text at the freeze, so later edits do not shift it. A note goes at the end of
the flagged paragraph or table, never inside it. Earlier text is kept."""
import json, os, re, sys, collections
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
FREEZE = os.path.join(DATA, "rec-full")
SKIP = ("kit", "Kit", "portal", "equivalents", "sw/", "tasks/", "kit-prs", "reports/SW02-SWARM-DESIGN", "reports/CLOUD-SW02", "archive/", "lean/", "reports/GPT-SW02")
ALIAS = {"atlas": "reports/rule30-structure-atlas.md"}
write = "--write" in sys.argv
rows = json.load(open(os.path.join(DATA, "state", "verdicts.json")))
plan, left = collections.defaultdict(list), []
for r in rows:
    v = r.get("verdict")
    if v not in ("CONFIRMED", "PARTIAL"):
        continue
    sev = str(r.get("severity", "")).lower()
    cor = str(r.get("correction") or "").strip()
    at = str(r.get("summary_at") or "")
    m = re.match(r"\s*([^\s:;,(]+)(?::(\d+))?", at)
    f = m.group(1) if m else ""
    f = ALIAS.get(f, f)
    ln = int(m.group(2)) if m and m.group(2) else None
    if f.startswith(SKIP) or not os.path.exists(f) or ln is None or not cor or not (sev == "material" or v == "CONFIRMED"):
        left.append({"flag": r.get("flag"), "at": at[:80], "verdict": v, "severity": sev, "why": str(r.get("why"))[:300], "correction": cor[:600]})
        continue
    plan[f].append((ln, r.get("flag"), v, cor))
done = 0
for f, items in sorted(plan.items()):
    ref = open(os.path.join(FREEZE, f), encoding="utf-8").read().split("\n") if os.path.exists(os.path.join(FREEZE, f)) else []
    cur = open(f, encoding="utf-8").read().split("\n")
    ins = []
    for ln, flag, v, cor in items:
        text = ref[ln - 1] if 0 < ln <= len(ref) else None
        try:
            i = cur.index(text) if text else ln - 1
        except ValueError:
            i = min(ln - 1, len(cur) - 1)
        j = i
        while j < len(cur) and cur[j].strip():
            j += 1
        c = re.sub(r"\s+", " ", cor)[:700]
        ins.append((j, "*(SW-02 note, Local, 6 November 2026, flag %s, %s, checked against source by a sub-agent: %s)*" % (flag, v, c)))
    for j, note in sorted(ins, key=lambda x: -x[0]):
        cur[j:j] = ["", note]
        done += 1
    if write:
        open(f, "w", encoding="utf-8").write("\n".join(cur))
print("notes", done, "in", len(plan), "files; left for the results page", len(left))
json.dump(left, open(os.path.join(DATA, "state", "flags-left.json"), "w"), ensure_ascii=False, indent=0)
print({k: len(v) for k, v in plan.items()})
