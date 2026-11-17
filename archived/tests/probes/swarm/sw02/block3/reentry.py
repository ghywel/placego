#!/usr/bin/env python3
"""Block 3, BN-13 section E's question: why do rows that hold period 7 for hundreds of steps enter the gate later?

Prediction, written before the run: each long hold is a prefix of period-14 columns of finite depth that lies on no
closed lock, and it is ended from the right: inside the prefix, column M fails first and column 1 last.
Counterfactual: inside the prefix some column fails before the column to its right. Then the break does not arrive
from the right, and this account is wrong.

Measures, per row with a hold of at least 100 steps. M: leading columns with no failure of period 14 in the 56 ticks
around the middle of the hold. first(c): the first failure of column c after the middle. Columns past M fail all the
time, so only columns 1 to M can test the order.

Usage: reentry.py LATE_FILE REF_DIR [MAX_ROWS]    LATE_FILE is lift --rows output: R, tick, class.
"""
import sys, collections
sys.path.insert(0, sys.argv[2]); import ref
rows_in = [tuple(map(int, l.split())) for l in open(sys.argv[1])]
rows_in = [r for r in rows_in if r[2] == 1]
cap = int(sys.argv[3]) if len(sys.argv) > 3 else 300
hold = []
for R, tick, cls in rows_in[:cap]:
    rows = ref.drv(ref.alt_col, R, tick + 80)
    u = [rows[2 * s + 1] & 1 for s in range((tick + 80) // 2)]
    best = (0, 0); a = 0
    for s in range(7, len(u)):
        if u[s] != u[s - 7]: a = s
        elif s - a > best[1] - best[0]: best = (a, s)
    if best[1] - best[0] < 100: continue
    s0, s1 = best
    viol = lambda t, c: ((rows[t] ^ rows[t - 14]) >> c) & 1
    end = 2 * (s1 + 1) + 1  # first odd tick at which column 1 breaks period 14
    mid = (2 * s0 + 2 * s1) // 2 + 1
    M = next((c for c in range(128) if any(viol(t, c) for t in range(mid - 28, mid + 28))), 128)
    first = [next((t for t in range(mid, tick + 80) if viol(t, c)), None) for c in range(M)]
    known = all(f is not None for f in first)
    order = known and all(first[c] > first[c + 1] for c in range(M - 1))
    hold.append((R, tick, s1 - s0, M, order, end, first[-1] if known else None, known))
print('rows read', min(len(rows_in), cap), 'with a hold of at least 100 steps', len(hold))
print('M, leading period-14 columns at mid hold:', sorted(collections.Counter(h[3] for h in hold).items()))
print('rows with a failure seen in every prefix column:', sum(h[7] for h in hold))
print('of those, column M first and column 1 last, strictly:', sum(h[4] for h in hold))
print('entry tick minus column 1 failure:', sorted(collections.Counter(h[1] - h[5] for h in hold).items())[:12])
sp = [(h[5] - h[6]) / (h[3] - 1) for h in hold if h[7] and h[3] > 1]
if sp: print('ticks per column inside the prefix: min %.2f median %.2f max %.2f' % (min(sp), sorted(sp)[len(sp) // 2], max(sp)))
for h in hold[:6]: print(' R', h[0], 'entry', h[1], 'hold steps', h[2], 'M', h[3], 'ordered', h[4], 'column 1 fails', h[5], 'column M fails', h[6])
