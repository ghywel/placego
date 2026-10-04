#!/usr/bin/env python3
"""Two shaders' half-rate tests compared FRAME BY FRAME (2026-10-01, CM3 and L2 for the trust gate and the cut switch).

    framediff.py <control per-frame tsv> <variant per-frame tsv> [census.tsv]

The tsvs are halfrate.py's PER_FRAME output (source, t0, k, label, PSNR-Y) over the same extracts. Printed: how many odd
frames changed (by more than 0.01 dB), the change's median and spread, the extremes, and per extract the change of the
unflagged median (the L2 gate's number). With cutstat.py's census.tsv, each changed frame is also checked against the
cut ground truth: odd frame k bridges source frames k - 1 and k + 1, so it spans a cut if scdet scored either pair
(k - 1, k) or (k, k + 1) at 10 or more.
"""
import sys
from collections import defaultdict

import numpy as np


def load(p):
    d = {}
    for line in open(p):
        c = line.rstrip("\n").split("\t")
        if len(c) != 5: continue
        d[(c[0], c[1], int(c[2]))] = (c[3], float(c[4]))
    return d


a, b = load(sys.argv[1]), load(sys.argv[2])
keys = sorted(k for k in a if k in b)
cuts = set()
if len(sys.argv) > 3:
    for line in open(sys.argv[3]).read().splitlines()[1:]:
        src, k, _, _, sc = line.split("\t")
        if float(sc) >= 10: cuts.add((src.split("@")[0], src.split("@")[1], int(k)))
d = np.array([b[k][1] - a[k][1] for k in keys])
ch = np.abs(d) > 0.01
print(f"{len(keys)} odd frames in both; {ch.sum()} changed ({100 * ch.mean():.2f} percent)")
if ch.any():
    q = np.percentile(d[ch], [0, 10, 50, 90, 100])
    print("the change where it changed, dB, percentiles 0/10/50/90/100: " + " ".join(f"{x:+.2f}" for x in q))
    print(f"  changed frames up {int((d[ch] > 0).sum())}, down {int((d[ch] < 0).sum())}; sum of changes {d[ch].sum():+.1f} dB")
    if cuts:
        on_cut = [i for i, k in enumerate(keys) if ch[i] and ((k[0][:40], k[1], k[2] - 1) in cuts or (k[0][:40], k[1], k[2]) in cuts)]
        print(f"  changed frames whose bridged pair spans a real cut: {len(on_cut)}"
              + (" -- " + ", ".join(f"{keys[i][0][:20]}@{keys[i][1]} k{keys[i][2]} {d[i]:+.2f}" for i in on_cut[:8]) if on_cut else ""))
    worst = np.argsort(d)[:5]
    print("  the worst: " + "; ".join(f"{keys[i][0][:24]}@{keys[i][1]} k{keys[i][2]} ({a[keys[i]][0]}) {d[i]:+.2f}" for i in worst if d[i] < -0.01))
med = defaultdict(lambda: ([], []))
for k in keys:
    if a[k][0] == "none":
        med[(k[0], k[1])][0].append(a[k][1]); med[(k[0], k[1])][1].append(b[k][1])
dm = sorted((np.median(v[1]) - np.median(v[0]), s) for s, v in med.items())
print(f"unflagged median per extract ({len(dm)}): from {dm[0][0]:+.2f} ({dm[0][1][0][:30]}@{dm[0][1][1]}) to {dm[-1][0]:+.2f} "
      f"({dm[-1][1][0][:30]}@{dm[-1][1][1]}); extracts down more than 0.3 dB: {sum(x < -0.3 for x, _ in dm)}")
