#!/usr/bin/env python3
"""triage_flags.py: Block 1. Give every SW-02 flag not yet applied a home. Repository files get a dated note at the end of the flagged paragraph; kit and portal flags go to the owner's M list or the
maintainers' list; design-input flags are recorded as corrected in the briefs. Rewrites the last section of reports/SW02-RESULTS.md."""
import collections, json, os, re
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
FREEZE = os.path.join(DATA, "rec-full")
ALIAS = {"atlas": "reports/rule30-structure-atlas.md"}
MLIST = {100: "M-1", 25: "M-2", 26: "M-2", 97: "M-3", 95: "M-4", 112: "M-5", 123: "M-5", 116: "M-6", 121: "M-6", 124: "M-6", 125: "M-6", 127: "M-6", 71: "M-7", 92: "M-7", 107: "M-7"}
left = json.load(open(os.path.join(DATA, "state", "flags-left.json")))
full = {int(r["flag"]): r for r in json.load(open(os.path.join(DATA, "state", "verdicts.json"))) if str(r.get("flag")).isdigit()}
homes = collections.defaultdict(list)
ins = collections.defaultdict(list)
for r in left:
    n = int(r["flag"])
    at = str(full[n].get("summary_at"))
    m = re.match(r"\s*([^\s:;,(]+)(?::(\d+))?", at)
    f = ALIAS.get(m.group(1), m.group(1)) if m else ""
    ln = int(m.group(2)) if m and m.group(2) else None
    cor = re.sub(r"\s+", " ", str(full[n].get("correction") or "").strip())
    low = f.lower()
    if n in MLIST:
        homes["Owner's list, " + MLIST[n]].append(r)
    elif low.startswith(("kit", "equivalents", "lean/")):
        homes["Kit, cosmetic: for the maintainers if a PR touches the file"].append(r)
    elif low.startswith("portal"):
        homes["Portal, cosmetic: the entry's author; no action from us"].append(r)
    elif f.startswith(("reports/SW02-SWARM-DESIGN", "reports/CLOUD-SW02", "sw/", "tasks/")):
        homes["Design inputs: corrected in the attack briefs (L1561); the design stays as written"].append(r)
    elif f.startswith("archive/"):
        homes["Archive: left as history; this entry is the correction"].append(r)
    elif os.path.exists(f) and ln and cor:
        ins[f].append((ln, n, full[n].get("verdict"), cor))
        homes["Record: dated note added in Block 1"].append(r)
    else:
        homes["Record: no line or correction to apply; this entry is the note"].append(r)
done = 0
for f, items in sorted(ins.items()):
    ref = open(os.path.join(FREEZE, f), encoding="utf-8").read().split("\n") if os.path.exists(os.path.join(FREEZE, f)) else []
    cur = open(f, encoding="utf-8").read().split("\n")
    pos = []
    for ln, n, v, cor in items:
        text = ref[ln - 1] if 0 < ln <= len(ref) else None
        i = cur.index(text) if text in cur else min(ln - 1, len(cur) - 1)
        j = i
        while j < len(cur) and cur[j].strip():
            j += 1
        pos.append((j, "*(SW-02 note, Local, 6 November 2026, flag %d, %s, cosmetic, checked against source by a sub-agent: %s)*" % (n, v, cor[:600])))
    for j, note in sorted(pos, key=lambda x: -x[0]):
        cur[j:j] = ["", note]
        done += 1
    open(f, "w", encoding="utf-8").write("\n".join(cur))
L = ["## Flags with their homes", "", "*Block 1, 6 November 2026. 51 corrections went in as dated notes first; the rest are sorted here, so that every flag has a home. Flags 174 and 175 are comments in their probes.*", ""]
for h, rs in sorted(homes.items()):
    L += ["### %s (%d)" % (h, len(rs)), ""]
    for r in rs:
        c = re.sub(r"\s+", " ", str(r.get("correction") or r.get("why")))
        c = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", c)
        L.append("- Flag %s (%s, %s) at `%s`: %s" % (r.get("flag"), r.get("verdict"), r.get("severity"), str(r.get("at"))[:70], c[:300]))
    L.append("")
p = "reports/SW02-RESULTS.md"
s = open(p, encoding="utf-8").read()
s = s[:s.index("## Flags not applied as notes")] + "\n".join(L)
open(p, "w", encoding="utf-8").write(s)
print(done, "notes;", {k: len(v) for k, v in homes.items()}, sum(len(v) for v in homes.values()))
