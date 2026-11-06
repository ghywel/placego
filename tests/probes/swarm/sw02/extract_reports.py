#!/usr/bin/env python3
"""extract_reports.py JOURNAL NAME: copy a finished batch's journal outside the session folder, write each task's `report` field to
out/<id>/report.txt and its manifest to out/<id>/manifest.json, and print a one-line view of each."""
import json, os, shutil, sys
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
j, name = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(DATA, "journals"), exist_ok=True)
shutil.copy(j, os.path.join(DATA, "journals", name + ".jsonl"))
n = 0
for line in open(j):
    r = json.loads(line)
    if r.get("type") != "result" or not isinstance(r.get("result"), dict):
        continue
    m = r["result"]
    i = m.get("id")
    if not i:
        continue
    d = os.path.join(DATA, "out", i)
    os.makedirs(d, exist_ok=True)
    rep = m.pop("report", "") or ""
    if rep:
        open(os.path.join(d, "report.txt"), "w", encoding="utf-8").write(rep)
    json.dump(m, open(os.path.join(d, "manifest.json"), "w"), ensure_ascii=False, indent=0)
    n += 1
    print(i, m.get("outcome"), "PRIZE" if m.get("prize_level_claim") else "", len(rep), "|", (m.get("summary") or "")[:400].replace("\n", " "))
print(n, "results")
