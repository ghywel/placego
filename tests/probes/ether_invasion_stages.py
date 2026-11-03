#!/usr/bin/env python3
"""L1367 T55d (Local, 2026-11-03): is the classic ether invaded at positive speed by some right half?
reports/rule30-genealogy.md section 59a. Run: python3 tests/probes/ether_invasion_stages.py SECONDS_PER_STAGE STEP STAGES

One tail is built stage by stage at alignment (0, 0): stage k has horizon T_k = STEP * k; its free bits are the
positions in [0.9 T_(k-1) - 40, 0.9 T_k + 40) (bits beyond about 0.9 T cannot reach a front near -0.15 T by time T),
earlier bits kept from the previous stage. Greedy single-flip local search with restarts of the stage's bits maximises
the depth -L(T_k). Per stage: the depth, the depth / T_k, and the whole front path every STEP ticks; at the end the
tail is replayed by a separate list oracle and its digest printed.
"""
import hashlib
import random
import sys
import time

SECS, STEP, K = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
c0, c1 = 0, 0
TMAX = STEP * K
LO, HI = -2 * TMAX - 20, 2 * TMAX + 20   # the left edge's garbage must stay left of any front (L1367 fix)
n = HI - LO + 1; mask = (1 << n) - 1
ref0 = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, HI + 1))
left = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, 0))
refs = [ref0]
for t in range(TMAX):
    r = refs[-1]; refs.append(((r << 1) ^ (r | (r >> 1))) & mask)
rng = random.Random(554)


def front(a, T, marks=()):
    out = {}
    for t in range(1, T + 1):
        a = ((a << 1) ^ (a | (a >> 1))) & mask
        if t in marks or t == T:
            d = (a ^ refs[t]) >> (t + 1) << (t + 1)
            out[t] = (d & -d).bit_length() - 1 + LO if d else None
    return out


def depth(a, T):
    L = front(a, T)[T]
    return -L if L is not None else -10 ** 6


tail = 0                                         # bits of the right half, as offsets from x = 0
for k in range(1, K + 1):
    T = STEP * k
    lo_b = max(0, int(0.9 * STEP * (k - 1)) - 40); hi_b = int(0.9 * T) + 40
    bits = list(range(lo_b, hi_b))
    base = left | (tail << (0 - LO))
    t0 = time.time(); best = (depth(base, T), tail)
    while time.time() - t0 < SECS:
        tl = best[1]
        for x in bits:                           # restart: re-randomise the new block only (keep the old part)
            if x >= int(0.9 * STEP * (k - 1)) and rng.random() < 0.5:
                tl ^= 1 << x
        a = left | (tl << (0 - LO)); s = depth(a, T); stall = 0
        while stall < 200 and time.time() - t0 < SECS:
            x = rng.choice(bits)
            tl2 = tl ^ (1 << x); a2 = left | (tl2 << (0 - LO)); s2 = depth(a2, T)
            if s2 >= s:
                stall = 0 if s2 > s else stall + 1
                tl, s = tl2, s2
            else:
                stall += 1
        if s > best[0]:
            best = (s, tl)
    s, tail = best
    print('stage %d T=%d: depth %d (%.3f per tick)' % (k, T, s, s / T), flush=True)
path = front(left | (tail << (0 - LO)), TMAX, marks=tuple(range(STEP, TMAX + 1, STEP)))
print('front path every %d ticks: %s' % (STEP, [path[t] for t in sorted(path)]))
L = -2 * TMAX - 5
bl = [(tail >> i) & 1 for i in range(2 * TMAX)]
g = [TAB[(x + c0) % 7][c1] if x < 0 else (bl[x] if x < len(bl) else 0) for x in range(L, -L + 1)]
e = [TAB[(x + c0) % 7][c1] for x in range(L, -L + 1)]
for _ in range(TMAX):
    g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]
    e = [e[i - 1] ^ (e[i] | e[i + 1]) for i in range(1, len(e) - 1)]
    L += 1
rep = next((L + i for i in range(len(g)) if g[i] != e[i] and L + i < 0), None)
print('replay (list oracle): leftmost difference at T=%d: %s; tail bits 0..%d sha256 %s' % (
    TMAX, rep, 2 * TMAX - 1, hashlib.sha256(''.join(map(str, bl)).encode()).hexdigest()[:16]))
print('ETHER_INVASION_STAGES_DONE')
