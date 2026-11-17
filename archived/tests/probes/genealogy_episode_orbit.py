#!/usr/bin/env python3
"""L1281 (Local, 2026-11-01): GC2353's episode laws checked on the actual single-seed orbit (GPT's probe uses
finite ten-bit rows). Run: python3 tests/probes/genealogy_episode_orbit.py   (seconds; no files written)

Front B(t+1) = max{i <= B(t)+1 : x_i(t+1) = 1}, B(1) = -1. At every time u: M = white gap ahead of B, z = x_(B-1),
L = black run ending at B. Checked at every u <= 20000:
  (a) the number of consecutive advances starting at u is exactly floor(M/2);
  (b) the step after them stays iff z XOR (floor(M/2) mod 2) = 0;
  (c) every nonadvance moves the front by -(L-1);
  (d) after a nonadvance landing at p, x_(p-1)(t+1) = 1 XOR x_(p-2)(t).
"""
import numpy as np

T = 20000
W = 2 * T + 9
C = T + 4
row = np.zeros(W, dtype=bool)
row[C] = True
row = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
B = -1
rec = []            # per u: (B, M, z, L, step, trailing bit after the step, x_(B'-2) at u)
for u in range(1, T):
    p = C + B
    ahead = np.flatnonzero(row[p + 1:])
    M = int(ahead[0])                                   # the right edge is black, so the gap is finite
    z = int(row[p - 1])
    behind = np.flatnonzero(~row[:p + 1][::-1])
    L = int(behind[0])                                  # black run ending at B (the cell left of the edge is white)
    nrow = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
    Bn = int(np.flatnonzero(nrow[:p + 2]).max()) - C
    pn = C + Bn
    rec.append((B, M, z, L, Bn - B, int(nrow[pn - 1]), int(row[pn - 2])))
    B, row = Bn, nrow
rec = np.array(rec)
Bs, Ms, zs, Ls, st, trail, prev2 = rec.T
n = len(st)
bad_a = bad_b = bad_c = bad_d = checked = 0
for u in range(n):
    r = Ms[u] // 2
    if u + r >= n:
        break
    checked += 1
    if not (np.all(st[u:u + r] == 1) and st[u + r] != 1):
        bad_a += 1
    zr = zs[u] ^ (r % 2)
    if (st[u + r] == 0) != (zr == 0):
        bad_b += 1
for u in range(n):
    if st[u] != 1:
        if st[u] != -(Ls[u] - 1):
            bad_c += 1
        if trail[u] != 1 - prev2[u]:
            bad_d += 1
nonadv = int(np.sum(st != 1))
print(f'(a) consecutive advances = floor(M/2): {checked} start times checked, {bad_a} failures')
print(f'(b) stay iff z XOR (floor(M/2) mod 2) = 0: {bad_b} failures')
print(f'(c) nonadvance step = -(L-1): {nonadv} nonadvances, {bad_c} failures')
print(f'(d) trailing bit after a nonadvance = 1 XOR x_(p-2): {bad_d} failures')
# Episode bookkeeping (COMPUTED, descriptive only): B = sum over episodes of floor(M/2) - (L-1)
starts = [0] + [u + 1 for u in range(n - 1) if st[u] != 1]
tot_adv = tot_ret = 0
for u in starts:
    r = Ms[u] // 2
    if u + r < n:
        tot_adv += r
        tot_ret += Ls[u + r] - 1
adv_all = int(np.sum(st == 1))
ret_all = int(-np.sum(st[st != 1]))
assert -1 + adv_all - ret_all == B
print(f'episodes {len(starts)}: gap advances in completed episodes {tot_adv}, retreats {tot_ret}; over all steps '
      f'-1 + {adv_all} advances - {ret_all} retreat = {-1 + adv_all - ret_all} = B({T}) = {B}')
assert bad_a == bad_b == bad_c == bad_d == 0
print('GENEALOGY_EPISODE_ORBIT_DONE')
