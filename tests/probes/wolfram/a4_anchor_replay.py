#!/usr/bin/env python3
"""L1423 (Local, 2026-11-03): direct replay of A4's kernel-checked law, without the closure. Run: python3 tests/probes/wolfram/a4_anchor_replay.py T
Simulate the inserted edge (on a row 2T + 100 cells wide on the left, so the anchor stays in the exact region) on the ring background 100100000 (alignment (0, 0)) by rule 30 to time T, follow the anchor
(A(300) = -72; A decreases by 1 when its own cell becomes a mismatch), and check at every t in [300, T]: the background is intact
at and left of A, a mismatch lies in (A, A + 24], and -14 <= 19 (A + 72) + 5 (t - 300) <= 22. Also the leftmost mismatch F(t).
"""
import sys
import numpy as np

T = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
# optional: WORD SOFF A0 P S LO HI W (default the (9, 57) case: 100100000 0 -72 19 14 -14 22 24)
WORD, SOFF, A0, P, S, LOB, HIB, W = (sys.argv[2], *map(int, sys.argv[3:10])) if len(sys.argv) > 9 else ('100100000', 0, -72, 19, 14, -14, 22, 24)
y = np.array([int(ch) for ch in WORD], dtype=np.uint8); NN = len(y)
cst = lambda s: s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y):
    orb.append(cur.copy()); cur = cst(cur)
q = len(orb)
E = lambda t, x: int(orb[(t + SOFF) % q][(t - x) % NN])
WL = 2 * T + 100; WR = T + 50; c = WL                # the truncated ends spoil one more cell per tick
row = np.array([E(0, x) if x < 0 else int(x == 0) for x in range(-WL, WR)], dtype=np.uint8)
ref = np.array([E(0, x) for x in range(-WL, WR)], dtype=np.uint8)


def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n


A = None; lo_v = 10 ** 9; hi_v = -10 ** 9; bad = 0; fronts = []
for t in range(T + 1):
    if t > 0:
        row = step(row); ref = step(ref)
    if t == 300:
        A = A0
        assert all(row[c + x] == E(300, x) for x in range(-(WL - 300) + 1, A0 + 1))
    elif t > 300:
        if row[c + A] != ref[c + A]:
            A -= 1
    if t >= 300:
        d = np.flatnonzero((row ^ ref)[t + 1: len(row) - t - 1]) + t + 1 - c   # the exact region only
        assert A > -WL + t + 1, 'anchor left the exact region'
        F = int(d.min())
        ok = F > A and F <= A + W
        v = P * (A - A0) + (P - S) * (t - 300)
        lo_v = min(lo_v, v); hi_v = max(hi_v, v); bad += not ok
        if t % 500 == 0:
            fronts.append((t, A, F))
print('%s, s = %d: replay to T = %d: %d (A - A0) + %d (t - 300) ranges over [%d, %d] (kernel bound [%d, %d]); front outside (A, A + %d]: %d times'
      % (WORD, SOFF, T, P, P - S, lo_v, hi_v, LOB, HIB, W, bad))
print('(t, A, F) every 500 ticks:', fronts)
print('A4_REPLAY_DONE')
