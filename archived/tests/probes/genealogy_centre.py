#!/usr/bin/env python3
"""L1288 (Local, 2026-11-01): GPT's centre questions. Predictions P9a-P9e in reports/rule30-genealogy.md section 23.2,
written first. Run: python3 tests/probes/genealogy_centre.py   (about a minute; no files written)

Single seed. B(t) = max{i <= B(t-1)+1 : black}, B(1) = -1 (the left founder's reach front).
Part 1 (unpacked, t <= 20000): times with B < 0; unmarked black centre cells; episodes (L at each non-advance,
  with B before it); capture times T(j) of diagonals j <= 20000 and the margin j - T(j); run-length tail at the front.
Part 2 (packed, t <= 100000): min B(t) on [1000, 100000] and the running minimum per decade.
"""
import numpy as np

T = 20000
W = 2 * T + 9
C = T + 4
row = np.zeros(W, dtype=bool); row[C] = True
row = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
B = -1
Bs = [None, -1]
centre_unmarked = []
runs = []                       # (t, B(t), L) at non-advances
lastD = {}                      # for T(j): last time t with D(t) < j and diagonal j black
for t in range(1, T):
    nrow = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
    p = C + B
    L = int(np.flatnonzero(~row[:p + 1][::-1])[0])          # black run ending at B
    Bn = int(np.flatnonzero(nrow[:p + 2]).max()) - C
    if Bn != B + 1:
        runs.append((t, B, L))
        assert Bn == B - (L - 1)
    B, row = Bn, nrow
    Bs.append(B)
    if row[C] and B < 0:
        centre_unmarked.append(t + 1)
Bs = np.array(Bs[1:])            # Bs[t-1] = B(t), t = 1..T
neg = np.flatnonzero(Bs < 0) + 1
print(f'Part 1: B(t) < 0 at {len(neg)} times, the last at t = {neg.max()}; unmarked black centre cells at times {centre_unmarked[:12]}'
      f'{" ..." if len(centre_unmarked) > 12 else ""} (count {len(centre_unmarked)}, last {max(centre_unmarked) if centre_unmarked else None})')
rt = np.array([r[0] for r in runs]); rB = np.array([r[1] for r in runs]); rL = np.array([r[2] for r in runs])
late = rt >= 100
viol = np.flatnonzero(late & (rL > 2 * rB + 3))
ratio = (rL[rt >= 1000] - 1) / (rB[rt >= 1000] + 1)
print(f'  non-advances: {len(runs)}; at t >= 100 with L > 2B+3: {len(viol)}' + (f' (first at t = {rt[viol[0]]}, B = {rB[viol[0]]}, L = {rL[viol[0]]})' if len(viol) else '') +
      f'; largest (L-1)/(B+1) at t >= 1000: {ratio.max():.4f} (at t = {rt[rt >= 1000][ratio.argmax()]}, B = {rB[rt >= 1000][ratio.argmax()]}, L = {rL[rt >= 1000][ratio.argmax()]}); largest L overall {rL.max()}')
# T(j): capture time of diagonal j = 1 + last t with D(t) < j (ignoring the colour, an upper bound)
D = Bs + np.arange(1, T + 1)
Tj = np.zeros(T + 1, dtype=np.int64)
last_below = -1
for t in range(1, T + 1):
    pass
# for each j: last t with D(t) < j  <=> running maximum of D crosses j
runmax = np.maximum.accumulate(D)
# T(j) = 1 + max{t : D(t) < j}; D(t) < j for all t up to the first time runmax >= j is not right since D can dip later;
# compute exactly: last time D(t) < j via reverse cumulative min
revmin = np.minimum.accumulate(D[::-1])[::-1]          # revmin[t-1] = min_{s >= t} D(s)
# diagonal j is captured from T(j) = 1 + (last t with D(t) < j) = first t with revmin[t] >= j
js = np.arange(100, T + 1)
Tjs = np.searchsorted(revmin, js)  + 1                   # revmin is nondecreasing
margin = js - Tjs
sel = js >= 1000
print(f'  capture benchmark: T(j) <= j for all j in [100, {T}]: {bool(np.all(Tjs <= js))}; min margin j - T(j) over j >= 1000: {margin[sel].min()} '
      f'(at j = {js[sel][margin[sel].argmin()]}); min of (j - T(j))/j over j >= 1000: {(margin[sel] / js[sel]).min():.4f}; at j = 20000: T = {Tjs[-1]}')
tail = [(rL >= l).mean() for l in range(1, 11)]
print('  run-length tail at the front P(L >= l), l = 1..10: ' + ' '.join(f'{v:.4f}' for v in tail) + '; fair coin 2^(1-l): ' + ' '.join(f'{2.0 ** (1 - l):.4f}' for l in range(1, 11)))
print('  max ratio of tail to 2^(1-l), l <= 10: ' + f'{max(tail[l - 1] / 2.0 ** (1 - l) for l in range(1, 11)):.3f}; min: {min(tail[l - 1] / 2.0 ** (1 - l) for l in range(1, 11)):.3f}')

# Part 2: packed to 100000
T2 = 100000
NW = (2 * T2 + 260) // 64 + 2
OFF = 64 * (NW // 2)
x = np.zeros(NW, dtype=np.uint64)
x[OFF >> 6] |= np.uint64(1) << np.uint64(OFF & 63)
ONE = np.uint64(1); S63 = np.uint64(63)
def step(x):
    left = (x << ONE) | np.concatenate(([np.uint64(0)], x[:-1] >> S63))
    right = (x >> ONE) | np.concatenate((x[1:] << S63, [np.uint64(0)]))
    return left ^ (x | right)
def bit(arr, k):
    return int((int(arr[k >> 6]) >> (k & 63)) & 1)
def rightmost_black_at_or_below(arr, k):
    w = k >> 6
    word = int(arr[w]) & ((1 << ((k & 63) + 1)) - 1)
    while word == 0:
        w -= 1; word = int(arr[w])
    return 64 * w + word.bit_length() - 1
x = step(x); B = -1
mins = {}
curmin = 10 ** 9
for t in range(1, T2):
    nx = step(x)
    if bit(x, OFF + B + 1) == 0 and bit(x, OFF + B + 2) == 0:
        B = B + 1
    else:
        B = rightmost_black_at_or_below(nx, OFF + B) - OFF
    x = nx
    if t + 1 >= 1000:
        curmin = min(curmin, B)
    for lo, hi in ((1000, 10000), (10000, 100000)):
        if lo <= t + 1 < hi:
            mins[(lo, hi)] = min(mins.get((lo, hi), 10 ** 9), B)
print(f'Part 2 (packed): min B(t) on [1000, {T2}]: {curmin}; per decade: ' + ', '.join(f'[{lo}, {hi}): {v}' for (lo, hi), v in mins.items()) + f'; B({T2}) = {B}')
print('GENEALOGY_CENTRE_DONE')
