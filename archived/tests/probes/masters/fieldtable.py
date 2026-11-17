"""The field tier's table from fieldtier.sh's field.tsv (2026-09-12).
    fieldtable.py <field.tsv>
One row per scene and host: the frames read, the median and 90th-percentile |error| in px, the gross
fraction (> 2 px), the median angular error, and the gain |v| measured / |v| true -- each averaged over the
frames read; a note where fieldcheck.py found a neighbouring truth frame a better fit."""
import csv
import sys
from collections import defaultdict

rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
by = defaultdict(list)
for r in rows: by[(r["scene"], r["host"])].append(r)
scenes = []
for r in rows:
    if r["scene"] not in scenes: scenes.append(r["scene"])
print("%-20s %-8s %-10s %8s %8s %7s %7s %6s  %s" % ("scene", "host", "frames", "med px", "p90 px", "gross%", "angle", "gain", "note"))
for sc in scenes:
    for host in ("metal", "placebo"):
        rs = by.get((sc, host))
        if not rs: continue
        n = len(rs)
        med = sum(float(r["median_px"]) for r in rs) / n; p90 = sum(float(r["p90_px"]) for r in rs) / n
        gross = sum(float(r["gross_pct"]) for r in rs) / n
        moving = [r for r in rs if float(r["v_true"]) >= 1.0]          # angle and gain mean nothing on a near-still frame
        angs = [float(r["angle_deg"]) for r in moving if r["angle_deg"] != "nan"]
        ang = sum(angs) / len(angs) if angs else float("nan")
        gains = [float(r["v_meas"]) / float(r["v_true"]) for r in moving]
        gain = sum(gains) / len(gains) if gains else float("nan")
        notes = sum(1 for r in rs if r["note"].strip())
        print("%-20s %-8s %-10s %8.3f %8.3f %7.1f %7.1f %6.3f  %s" % (sc, host, ",".join(r["k"] for r in rs), med, p90, gross, ang, gain,
                                                                   ("%d frame(s) fit the neighbour better" % notes) if notes else ""))
