#!/usr/bin/env python3
"""bg_breaks2.py: the (34, 42) class of (12, 68) to t = 1700: onset t0, break time, and break time minus onset; and how many of the
short-period 'laws' of CL673 were two-repeat artefacts of the detector (t0 within 3 periods of the window's end)."""
import numpy as np
from collections import Counter
exec(open('background_breaks.py').read().split("Rc = fronts(0, 51, 1600, 6000)")[0])
def law(inc, upto):
    seg = inc[:upto]; n = len(seg)
    for per in range(1, 301):
        if n < 3*per: break
        if np.array_equal(seg[n-2*per:n-per], seg[n-per:]):
            t0 = n - 2*per
            while t0 > 0 and seg[t0-1] == seg[t0-1+per]: t0 -= 1
            return t0, per, int(seg[t0:t0+per].sum())
    return None
T, J = 1700, 6000
rows = []; short = Counter(); short_total = Counter()
for r in range(p):
    for s in range(q):
        R = fronts(r, s, T, J); inc = np.diff(R); l = law(inc, 700)
        if not l: continue
        t0, per, sh = l
        b = next((t for t in range(t0 + per, T) if inc[t] != inc[t - per]), None)
        if (per, sh) == (34, 42): rows.append((r, s, t0, b, (b - t0) if b else None))
        else:
            short_total[(per, sh)] += 1
            if 700 - t0 < 3 * per + 2: short[(per, sh)] += 1
print("(34, 42) class:", len(rows), "alignments; onset t0 values:", sorted(Counter(t0 for *_, t0, b, d in [(a, b, c, d, e) for a, b, c, d, e in rows]).items()))
print("  break time minus onset (None = no break by 1700):", sorted(Counter(d for *_, d in rows).items(), key=lambda x: (x[0] is None, x[0])))
print("  break times:", sorted(Counter(b for *_, b, d in rows).items(), key=lambda x: (x[0] is None, x[0])))
print("short-period 'laws' at 700: total by class", dict(short_total), "| of which onset within three periods of the window's end", dict(short))
print("BG_BREAKS2_DONE")
