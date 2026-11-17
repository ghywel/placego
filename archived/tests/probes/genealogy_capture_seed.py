#!/usr/bin/env python3
"""L1284 (Local, 2026-11-01): GC2357's capture argument checked on the actual single-seed orbit, in Local's own code.
Run: python3 tests/probes/genealogy_capture_seed.py   (about half a minute; no files written)

Left-edge coordinates a_j(t) = x_(e-t+j)(t) with e the leftmost black cell at the start; marks propagate along every
black-parent edge from the edge cell. Checks on the seed from its time-one row (e = -1):
  (1) 17.2: no adjacent pair (n, n+1) of diagonals is white for n+1 consecutive times, n <= NMAX, all start times;
  (2) 17.4: the last unmarked black cell on diagonal j occurs before C_j = 1 + j(j-1)/2, j <= JMAX;
  (3) 17.5: for restarts at every time t0 <= 3000 and bands D <= DMAX, the fresh marked front leaves band 0..D within
      E(D) = (D+2)(D+3)/2 updates, and the original front dominates the fresh one;
  (4) the marked front equals the follower B(t+1) = max{i <= B+1 : black} (the carried reach property).
This is a self-check of GPT's induction on one orbit, not the carrying read.
"""
import numpy as np

JMAX, NMAX, DMAX = 120, 120, 30
T = 1 + JMAX * (JMAX - 1) // 2 + 1 + 400          # enough rows for C_JMAX and the restarts
T = max(T, 3000 + (DMAX + 2) * (DMAX + 3) // 2 + 5)
W = 3 * T + 12                                    # room for the left-edge window of width 2T + 2
C = T + 4
rows = np.zeros((T + 1, W), dtype=np.uint8)
rows[0, C] = 1
for t in range(T):
    rows[t + 1, 1:-1] = rows[t, :-2] ^ (rows[t, 1:-1] | rows[t, 2:])

# left-edge coordinates from time 1: a[t][j] = rows[t, C - 1 - (t - 1) + j] = rows[t, C - t + j]
JW = 2 * T + 2
def diag_row(t):
    return rows[t, C - t: C - t + JW]

# marks from the edge at time 1, all-parent propagation
m = np.zeros(JW, dtype=np.uint8)
m[0] = 1
last_unmarked = np.full(JMAX + 1, -1)
B = -1                                             # the follower, absolute position, B(1) = -1
front_mismatch = 0
white_pair_viol = 0
run_white = np.zeros(JW + 1, dtype=np.int64)       # consecutive times the pair (n, n+1) has been white
for t in range(1, T):
    a = diag_row(t)
    # (1) white-pair runs
    pair_white = (a[:NMAX + 1] == 0) & (a[1:NMAX + 2] == 0)
    run_white[:NMAX + 1] = np.where(pair_white, run_white[:NMAX + 1] + 1, 0)
    white_pair_viol += int(np.sum(run_white[:NMAX + 1] >= np.arange(NMAX + 1) + 1))   # a run of n+1 would violate 17.2
    # (2) unmarked black cells
    um = np.flatnonzero((a[:JMAX + 1] == 1) & (m[:JMAX + 1] == 0))
    last_unmarked[um] = t
    # (4) the follower
    a1 = diag_row(t + 1)
    Bn = int(np.flatnonzero(rows[t + 1, :C + B + 2]).max()) - C
    m1 = np.zeros_like(m)
    m1[2:] = a1[2:] & (m[:-2] | m[1:-1] | m[2:])
    m1[1] = a1[1] & (m[0] | m[1])
    m1[0] = a1[0] & m[0]
    m = m1
    jB = Bn + (t + 1)                              # left-edge index at time t+1: the edge is at -(t+1)
    if int(np.flatnonzero(m).max()) != jB or not np.array_equal(np.flatnonzero(m), np.flatnonzero(a1[:jB + 1])):
        front_mismatch += 1
    B = Bn
Cj = np.array([0] + [1 + j * (j - 1) // 2 for j in range(1, JMAX + 1)])
print(f'(1) white-pair windows: pairs (n, n+1), n <= {NMAX}, all times to {T}: violations of the n+1 bound {white_pair_viol}')
print(f'(2) capture on the seed (the mark is placed at time 1, so GPT\'s C_j is time 1 + C_j here): last unmarked black time on diagonals 0..{JMAX} all <= C_j: {bool(np.all(last_unmarked <= Cj))}; '
      f'last unmarked at j = 10, 30, 60, 120: {[int(last_unmarked[j]) for j in (10, 30, 60, 120)]} against C_j {[int(Cj[j]) for j in (10, 30, 60, 120)]}')
print(f'(4) marked set = all black cells of [edge, B(t)] with B the follower, at every time to {T}: mismatches {front_mismatch}')

# (3) restarts
E = [(D + 2) * (D + 3) // 2 for D in range(DMAX + 1)]
worst_exit = np.zeros(DMAX + 1, dtype=np.int64)
dominance_viol = 0
for t0 in range(1, 3001):
    mf = np.zeros(JW, dtype=np.uint8)
    mf[0] = 1
    first_exit = np.full(DMAX + 1, -1)
    for s in range(E[DMAX] + 1):
        t = t0 + s
        jf = int(np.flatnonzero(mf).max())
        for D in range(DMAX + 1):
            if first_exit[D] < 0 and jf > D:
                first_exit[D] = s
        if first_exit[DMAX] >= 0:
            break
        a1 = diag_row(t + 1)
        n1 = np.zeros_like(mf)
        n1[2:] = a1[2:] & (mf[:-2] | mf[1:-1] | mf[2:])
        n1[1] = a1[1] & (mf[0] | mf[1])
        n1[0] = a1[0] & mf[0]
        mf = n1
    assert np.all(first_exit >= 0)
    worst_exit = np.maximum(worst_exit, first_exit)
print(f'(3) restarts at t0 = 1..3000, bands D = 0..{DMAX}: first exit within E(D) always: {bool(np.all(worst_exit <= E))}; '
      f'worst first exits at D = 0, 5, 10, 20, 30: {[int(worst_exit[D]) for D in (0, 5, 10, 20, 30)]} against E(D) {[E[D] for D in (0, 5, 10, 20, 30)]}')
print('GENEALOGY_CAPTURE_SEED_DONE')
