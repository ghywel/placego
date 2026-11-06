#!/usr/bin/env python3
"""build_backlog.py: reports/SW02-BACKLOG.md from the swarm's unserved test requests and open questions, as tick-off lists. Generated once; tick items by hand after that."""
import glob, json, os, re
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
HOME = os.path.expanduser("~")


def t(x, n):
    s = re.sub(r"\s+", " ", str(x if x is not None else "")).strip().replace(HOME, "~")
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    return s[:n].rstrip() + "…" if len(s) > n else s


def rows(name):
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, "out", "*", name))):
        who = f.split("/")[-2]
        if who.startswith("SM"):
            continue
        for line in open(f, encoding="utf-8"):
            try:
                out.append((who, json.loads(line)))
            except ValueError:
                pass
    return out


SERVED = {"AM-3": ["Reset chains"], "BR-2": ["BN-02"], "PE-1": ["Lean replay", "Finish the trap"], "CP-1": ["R1:"], "BR-5": ["Right dichotomy"], "CP-2": ["Census of tail"], "LN-06": ["Run a termination"], "LN-07": ["Extend gate-past"]}
L = ["# SW-02 backlog", "",
     "*Generated 6 November 2026 from the swarm's files. Work listed here is optional and unordered within a section; [WARM-LEADS](../WARM-LEADS.md) sets the order. Tick an item in the commit that settles it, citing the ledger entry. Scripts named are in the raw archive (`cited/local/sw02-all-20261106.tar.gz`, folder `out/<agent>/`). Each test still needs its prediction and controls written before it runs; the fields here are the agents' proposals.*", "",
     "## Test requests", "", "*Requests marked done were covered by the bench (BN-02, BN-11 to BN-16, BN-L1).*", ""]
for who, r in rows("requests.jsonl"):
    test = str(r.get("test"))
    done = any(test.startswith(p) or p in test[:60] for p in SERVED.get(who, []))
    L.append("- [%s] **%s.** %s *Cost:* %s" % ("x" if done else " ", who, t(test, 260), t(r.get("cost_estimate"), 90)))
L += ["", "## Open questions", ""]
for who, r in rows("questions.jsonl"):
    L.append("- [ ] **%s.** %s" % (who, t(r.get("question"), 240)))
open("reports/SW02-BACKLOG.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print(os.path.getsize("reports/SW02-BACKLOG.md") // 1024, "KB", sum(1 for x in L if x.startswith("- [x]")), "done", sum(1 for x in L if x.startswith("- [ ]")), "open")
