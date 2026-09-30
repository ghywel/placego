"""ENERGY-TRANSFER.md 3.6c: merge census_local.py's saved histograms from several batches of sources.

    census_local_merge.py <local_*.npz> [...]

Sums the per-band, per-label histograms and prints the same table, L1, L2 and the A/B control as census_local.py,
plus every source's own gap. Numbers only.
"""
import sys

import numpy as np

LABELS = ("flag", "pre", "A", "B")
Z = [np.load(p, allow_pickle=False) for p in sys.argv[1:]]
BANDS, BINS = Z[0]["bands"], Z[0]["bins"]
for z in Z[1:]:
    assert np.array_equal(z["bands"], BANDS) and np.array_equal(z["bins"], BINS), "the batches used different bands or bins"
H = {lab: sum(z[f"all_{lab}"] for z in Z) for lab in LABELS}


def med(hist):
    c = np.cumsum(hist); n = c[-1] if len(c) else 0
    if n == 0: return float("nan"), 0
    return float(BINS[np.searchsorted(c, n / 2)] + 0.025), int(n)


print(f"merged {len(Z)} batches: {sum(len(z['names']) for z in Z)} extracts")
print(f"{'band px/f':>10s} | {'flagged':>15s} {'pre-rule':>15s} {'unflagged A':>15s} {'unflagged B':>15s} | flag-A   A-B")
gaps, ab = [], []
for i in range(len(BANDS) - 1):
    m = {lab: med(H[lab][i]) for lab in LABELS}
    c = lambda lab: f"{m[lab][0]:6.2f} ({m[lab][1]:7d})"
    g = m["flag"][0] - (m["A"][0] + m["B"][0]) / 2; x = m["A"][0] - m["B"][0]
    print(f"{BANDS[i]:4.0f}-{BANDS[i + 1]:<4.0f} | {c('flag')} {c('pre')} {c('A')} {c('B')} | {g:+6.2f} {x:+6.2f}")
    if m["flag"][1] >= 50 and m["A"][1] + m["B"][1] >= 50: gaps.append(g)
    if m["A"][1] >= 50 and m["B"][1] >= 50: ab.append(abs(x))
G = np.array(gaps); half = len(G) // 2
print(f"L1: mean flagged - unflagged gap over {len(G)} bands: {G.mean():+.2f} dB (at most -2.0 to pass) -> {'PASSED' if G.mean() <= -2 else 'MISSED'}")
print(f"L2: slower half {G[:half].mean():+.2f}, faster half {G[half:].mean():+.2f} -> {'PASSED' if G[half:].mean() < G[:half].mean() else 'MISSED'}")
print(f"CONTROL: max |A - B| {max(ab):.2f} dB -> {'HELD' if max(ab) <= 0.3 else 'MOVED'}")
print("\nper extract (mean gap over its bands with 50+ cells of each):")
per = []
for z in Z:
    for i, name in enumerate(z["names"]):
        gs = []
        for b in range(len(BANDS) - 1):
            f, nf = med(z[f"src{i}_flag"][b]); u, nu = med(z[f"src{i}_A"][b] + z[f"src{i}_B"][b])
            if nf >= 50 and nu >= 50: gs.append(f - u)
        per.append((str(name), np.mean(gs) if gs else float("nan"), len(gs)))
for name, g, nb in per:
    print(f"  {name[:60]:62s} {g:+6.2f} dB over {nb} bands" if nb else f"  {name[:60]:62s} --")
v = np.array([g for _, g, nb in per if nb])
print(f"extracts with a gap: {len(v)}; worse than -2 dB: {int((v <= -2).sum())}; worse at all: {int((v < 0).sum())}; median {np.median(v):+.2f}")
