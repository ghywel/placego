#!/usr/bin/env python3
"""L1438 (Local, 2026-11-03): P-g. Does a front that followed the 11/81 law for a long stretch ever leave it?
Reads a4_perturbation_census.py's saved F(t). Run: python3 tests/probes/wolfram/a4_slow_wall_stability.py SAVE.npz [RUN]
slow(t) means F(t + 81) - F(t) = -11. A slow stretch of length >= RUN is a run of consecutive t with slow(t), covering
[t, t + 81] for each t (so the front held the law for RUN + 81 ticks). Reports, by end state (fast 2/9, slow 11/81, other):
how many fronts had a slow stretch of length >= RUN, and, for those that left one, when and to what.
"""
import sys
from collections import Counter

import numpy as np

z = np.load(sys.argv[1]); F = z['F'].astype(np.int64); pats = z['pats']
RUN = int(sys.argv[2]) if len(sys.argv) > 2 else 243
TMAX = F.shape[0] - 1; NP = F.shape[1]
sl = (F[TMAX] - F[2000]) / (TMAX - 2000)
end = np.where(np.abs(sl + 2 / 9) < 0.01, 'fast', np.where(np.abs(sl + 11 / 81) < 0.005, 'slow', 'other'))
slow = (F[81:] - F[:-81]) == -11  # slow[t, k] for t in [0, TMAX - 81]


def runs(b):
    """(start, length) of the maximal True runs of a 1-d bool array."""
    d = np.diff(np.concatenate([[0], b.astype(np.int8), [0]]))
    s = np.flatnonzero(d == 1); e = np.flatnonzero(d == -1)
    return list(zip(s.tolist(), (e - s).tolist()))


left = Counter(); held = Counter(); examples = []
for k in range(NP):
    rs = [r for r in runs(slow[:, k]) if r[1] >= RUN]
    if not rs:
        continue
    held[end[k]] += 1
    last_end = rs[-1][0] + rs[-1][1] + 81  # the law holds up to this time
    if last_end < TMAX - 1:
        left[end[k]] += 1
        if len(examples) < 8:
            examples.append((int(pats[k]), end[k], 'slow from %d to %d' % (rs[-1][0], last_end)))
print('end states: %s' % dict(Counter(end.tolist())))
print('fronts with a slow stretch >= %d (law held >= %d ticks): %s' % (RUN, RUN + 81, dict(held)))
print('of those, fronts that left their last such stretch before %d: %s' % (TMAX, dict(left)))
print('examples (pattern, end state, last long slow stretch): %s' % examples)
oth = np.flatnonzero(end == 'other')
print('undecided ("other") fronts: %d; their late slopes: %s' % (len(oth), Counter(np.round(sl[oth], 3).tolist()).most_common(8)))
print('A4_SLOW_WALL_STABILITY_DONE')
