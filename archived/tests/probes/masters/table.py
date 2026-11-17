"""The master tier's table from check.sh's results.tsv (2026-09-12).

    table.py <results.tsv> [--md] [--cap 40]

One block per shader stem: rows the scenes, columns the two hosts' ladder means, with linear and hold
beside (once per scene). Then a summary per stem: the mean over scenes of the CAPPED reading (analyze.py's
convention -- above CAP_DB a difference is not one anyone can see, and an average of a 60 with a 22 is
arithmetic on two quantities), the count of scenes where the shader beats linear, and the host gap.
Read a scene's row before its stem's mean: the table is the finding, the mean is the index.
"""
import csv
import sys
from collections import defaultdict

path = sys.argv[1]
md = "--md" in sys.argv
cap = float(sys.argv[sys.argv.index("--cap") + 1]) if "--cap" in sys.argv else 40.0

rows = list(csv.DictReader(open(path), delimiter="\t"))
scenes = []
for r in rows:
    if r["scene"] not in scenes: scenes.append(r["scene"])
by = defaultdict(dict)          # (scene, stem) -> host -> (mean, min)
for r in rows:
    by[(r["scene"], r["stem"])][r["host"]] = (float(r["mean"]), float(r["min_past5"]))
stems = []
for r in rows:
    if r["stem"] != "-" and r["stem"] not in stems: stems.append(r["stem"])

def f(v): return "%6.2f" % v if v is not None else "     -"
def get(sc, stem, host):
    d = by.get((sc, stem), {}); return d[host][0] if host in d else None

out = []
if md:
    out.append("| scene | linear | hold |" + "".join(" %s metal | %s placebo |" % (s, s) for s in stems))
for stem in stems:
    out.append("")
    out.append("== " + stem)
    out.append("%-20s %7s %7s %7s %7s   %s" % ("scene", "metal", "placebo", "linear", "hold", "metal-placebo"))
    for sc in scenes:
        m, p = get(sc, stem, "metal"), get(sc, stem, "placebo")
        li, ho = get(sc, "-", "linear"), get(sc, "-", "hold")
        gap = "%+.2f" % (m - p) if m is not None and p is not None else "-"
        out.append("%-20s %s %s %s %s   %s" % (sc, f(m), f(p), f(li), f(ho), gap))

out.append("")
out.append("summary (mean of the reading capped at %.0f dB over %d scenes; beats = scenes where placebo > linear)" % (cap, len(scenes)))
out.append("%-44s %7s %7s %6s %7s" % ("stem", "placebo", "metal", "beats", "gap"))
for stem in stems:
    ps = [min(get(sc, stem, "placebo"), cap) for sc in scenes if get(sc, stem, "placebo") is not None]
    ms = [min(get(sc, stem, "metal"), cap) for sc in scenes if get(sc, stem, "metal") is not None]
    beats = sum(1 for sc in scenes if get(sc, stem, "placebo") is not None and get(sc, "-", "linear") is not None
                and get(sc, stem, "placebo") > get(sc, "-", "linear"))
    gaps = [get(sc, stem, "metal") - get(sc, stem, "placebo") for sc in scenes
            if get(sc, stem, "metal") is not None and get(sc, stem, "placebo") is not None]
    out.append("%-44s %s %s %3d/%-2d %s" % (stem, f(sum(ps) / len(ps) if ps else None), f(sum(ms) / len(ms) if ms else None),
                                            beats, len(scenes), ("%+.2f" % (sum(gaps) / len(gaps))) if gaps else "-"))
lin = [min(get(sc, "-", "linear"), cap) for sc in scenes if get(sc, "-", "linear") is not None]
hol = [min(get(sc, "-", "hold"), cap) for sc in scenes if get(sc, "-", "hold") is not None]
out.append("%-44s %s   (hold %s)" % ("linear", f(sum(lin) / len(lin) if lin else None), f(sum(hol) / len(hol) if hol else None)))
print("\n".join(out))
