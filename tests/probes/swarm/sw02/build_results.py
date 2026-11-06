#!/usr/bin/env python3
"""build_results.py HEAD.md: write reports/SW02-DOORS.md and reports/SW02-RESULTS.md from the compile wave's files. HEAD.md is Local's opening text."""
import collections, json, os, re, sys
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
HOME = os.path.expanduser("~")


def jl(p):
    out = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
    return out


def t(x, n=None):
    s = re.sub(r"\s+", " ", str(x if x is not None else "")).strip().replace(HOME, "~")
    s = re.sub(r"/pri" + r"vate/t" + r"mp\S*", "(scratch)", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)  # links in agents' text are relative to other documents
    return s[:n].rstrip() + "…" if n and len(s) > n else s


def doors():
    rows = []
    for k in ("CM-1a", "CM-1b", "CM-1c"):
        for r in jl(os.path.join(DATA, "out", k, "doors.jsonl")):
            r["part"] = k
            rows.append(r)
    order = ["AJAR", "OPEN / DEFERRED", "PENDING: argument", "SHUT: theorem", "REFUTED: witness", "NOT A PRIZE ROUTE", "ALIAS"]
    g = collections.defaultdict(list)
    for r in rows:
        v = str(r.get("verdict"))
        key = next((o for o in order if v.startswith(o)), "PENDING: argument" if v.startswith("PENDING") else v)
        g[key].append(r)
    L = ["# SW-02 door ledger", "",
         "*Compiled 6 November 2026 by three sub-agents of Local (CM-1a, b, c) from the 680 cards of Wave 1, updated from Waves 2 to 4. Sub-agent self-checks: a verdict here changes no status in the record. Verdicts follow the design's §5: a theorem closes only its stated class, a measurement shuts nothing, a failed search closes nothing, and a new hand closure is pending until a worker reads it. The compilers worked before GPT's GC2690, so doors on Mortality, AM-3's amplification, CT-2's check sums and SEP show PENDING where [GPT's carrying review](GPT-SW02-CARRY-REVIEW-20261106.md) has since carried a repaired statement: read that review first. The three parts merged within themselves, and aliases across parts are noted, not merged. The coverage is a finite manifest, not all possible methods.*", "",
         "| Verdict | Doors |", "|---|---|"]
    for o in order:
        L.append("| %s | %d |" % (o, len(g.get(o, []))))
    L.append("| Total | %d |" % len(rows))
    L.append("")
    for o in order:
        L += ["## %s" % o, ""]
        for r in sorted(g.get(o, []), key=lambda r: t(r.get("target"))):
            line = "- **%s** (target: %s). %s" % (t(r.get("door"), 120), t(r.get("target"), 80), t(r.get("route"), 300))
            if r.get("scope"):
                line += " *Scope:* %s" % t(r.get("scope"), 300)
            if r.get("source"):
                line += " *Source:* %s" % t(r.get("source"), 160)
            if r.get("evidence"):
                line += " *Evidence:* %s" % t(r.get("evidence"), 160)
            if o in ("AJAR", "OPEN / DEFERRED", "PENDING: argument"):
                if r.get("next_test"):
                    line += " *Next:* %s" % t(r.get("next_test"), 240)
                if r.get("cost"):
                    line += " *Cost:* %s" % t(r.get("cost"), 80)
            if r.get("reopen") and o in ("SHUT: theorem", "REFUTED: witness"):
                line += " *Reopen if:* %s" % t(r.get("reopen"), 160)
            L.append(line)
        L.append("")
    open("reports/SW02-DOORS.md", "w", encoding="utf-8").write("\n".join(L))
    return len(rows), {k: len(v) for k, v in g.items()}


def results(head):
    L = [open(head, encoding="utf-8").read().rstrip(), ""]
    L += ["## Answer sheet", "", "*Every question of the design's §8, compiled by CM-2. Statuses as the evidence allowed at compile time; GC2690 has since carried Q01 ⇔ Mortality, AM-3's finite statement, CT-2's first-check bound and SEP ⇔ LR₁, as above.*", ""]
    for r in jl(os.path.join(DATA, "out", "CM-2", "answers.jsonl")):
        L.append("- **%s. %s** %s *Status:* %s. *Open:* %s" % (t(r.get("id")), t(r.get("question"), 200), t(r.get("answer"), 900), t(r.get("status"), 160), t(r.get("open"), 300)))
    L += ["", "## Barrier atlas", "", "*Each no-go statement with the class it excludes. Kit theorems are as stated at the pin; new ones are pending a worker's read.*", ""]
    for r in jl(os.path.join(DATA, "out", "CM-2", "barriers.jsonl")):
        L.append("- **%s.** *Class:* %s *Statement:* %s *Status:* %s. *Source:* %s. *Leaves open:* %s" % (t(r.get("barrier"), 120), t(r.get("class"), 300), t(r.get("statement"), 300), t(r.get("status"), 80), t(r.get("source"), 120), t(r.get("leaves_open"), 220)))
    L += ["", "## Unforced findings", "", "*Things agents noticed that nobody asked for, kept for themselves.*", ""]
    for r in jl(os.path.join(DATA, "out", "CM-2", "unforced.jsonl")):
        L.append("- %s: %s (%s)" % (t(r.get("from"), 30), t(r.get("finding"), 420), t(r.get("status"), 80)))
    left = json.load(open(os.path.join(DATA, "state", "flags-left.json")))
    L += ["", "## Flags not applied as notes", "", "*53 checked corrections went into the record as dated notes, less two in Python probes (kept here). These are the rest: kit, portal and design items, and cosmetic ones. Kit and portal items need a maintainer or the entry's author.*", ""]
    for r in left:
        L.append("- Flag %s (%s, %s) at `%s`: %s" % (r.get("flag"), r.get("verdict"), r.get("severity"), t(r.get("at"), 70), t(r.get("correction") or r.get("why"), 300)))
    open("reports/SW02-RESULTS.md", "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    print(doors())
    results(sys.argv[1])
    for p in ("reports/SW02-DOORS.md", "reports/SW02-RESULTS.md"):
        print(p, os.path.getsize(p) // 1024, "KB")
