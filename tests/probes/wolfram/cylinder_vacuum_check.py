#!/usr/bin/env python3
"""L1487 (Local, 2026-11-03): exhaustive checks of GC2598's generic steps (GPT-CYLINDER-HISTORY-TRANSFER-20261103.md).
Run: python3 tests/probes/wolfram/cylinder_vacuum_check.py TMAX
For every t = 1 .. TMAX and every initial word on [p-t, p+t+1] (p = 0; exterior cells cannot reach the events by causality):
  1. N(t,p) and X(t,p) = 0  iff  initial [p-t, p+t] all white.
  2. N(t,p), X(t,p) = 0, X(t,p+1) = 1  iff  initial [p-t, p+t+1] = 0^(2t+1) 1.
  3. W_g (g = 1..t) iff X(t,p) = 0 and g is the least black on the ray X(t-j, p+j-2), j = 1..t; B_g likewise with
     X(t,p+1) = 1. Hence exactly one of {vacuum, W_1..W_t} holds iff X(t,p) = 0 (and the B form for the pair event).
  4. The guarded criterion: an initial black in [p-t, p+t] and, for every u < t, a white at time u in [p-t+u, p+t-u-2]
     force X(t,p) = 1; its two countercontrols (initial 100 at t = 1; the all-white row) behave as GC2598 says.
5. The tick-19 table: from the root word 0101010010001101110011101 on [-9, 15] with every exterior cell unknown, three-valued
   Rule 30 forces X(u, j_u) = 0 at GC2598's 19 positions, each inside J_u = [u - 9, 27 - u]. (Three-valued propagation alone
   does not force X(19, 10); criterion 4 does, from these witnesses.)
6. The moving-coordinate example: initial 01010 on [-2, 2] gives 101 on [-1, 1]; the pair event holds at (1, p = 0),
   r_1 = X(1, 1) = 1 and r_2 = X(2, 0) = 0.
Prints counts and PASS/FAIL only.
"""
import sys
from itertools import product

TMAX = int(sys.argv[1])
rule = lambda a, b, c: a ^ (b | c)
ok = True


def report(name, cond):
    global ok
    ok &= bool(cond)
    print('%s: %s' % (name, 'PASS' if cond else 'FAIL'))


def evolve(row, steps):
    rows = [row]
    for _ in range(steps):
        r = rows[-1]; lo, hi = min(r), max(r)
        rows.append({x: rule(r[x - 1], r[x], r[x + 1]) for x in range(lo + 1, hi)})
    return rows


c1 = c2 = c3 = c4 = True; n = 0; nguard = 0
for t in range(1, TMAX + 1):
    lo, hi = -t - 2 * t, t + 1 + 2 * t          # white padding so every needed cell exists
    for core in product((0, 1), repeat=2 * t + 2):  # cells p-t .. p+t+1
        row = {x: 0 for x in range(lo, hi + 1)}
        for i, b in enumerate(core):
            row[-t + i] = b
        R = evolve(row, t)
        X = lambda s, x: R[s][x]
        ray = [X(t - j, j - 2) for j in range(1, t + 1)]
        N = not any(ray)
        vac = not any(core[:2 * t + 1])
        c1 &= (N and X(t, 0) == 0) == vac
        c2 &= (N and X(t, 0) == 0 and X(t, 1) == 1) == (vac and core[2 * t + 1] == 1)
        W = []; B = []
        for g in range(1, t + 1):
            u = t - g
            blk = all(X(u, x) == 1 for x in range(-g, g - 1))
            W.append(blk and (X(u, g - 1) | X(u, g)) == 1)
            B.append(blk and (X(u, g - 1), X(u, g), X(u, g + 1)) in ((0, 1, 0), (0, 1, 1), (1, 0, 0)))
        least = next((j for j in range(1, t + 1) if ray[j - 1]), None)
        c3 &= all(W[g - 1] == (X(t, 0) == 0 and least == g) for g in range(1, t + 1))
        c3 &= all(B[g - 1] == (X(t, 0) == 0 and X(t, 1) == 1 and least == g) for g in range(1, t + 1))
        c3 &= (vac + sum(W)) == (1 if X(t, 0) == 0 else 0)
        c3 &= ((vac and core[2 * t + 1] == 1) + sum(B)) == (1 if (X(t, 0) == 0 and X(t, 1) == 1) else 0)
        guard = any(core[:2 * t + 1]) and all(any(X(u, x) == 0 for x in range(-t + u, t - u - 1)) for u in range(t))
        if guard:
            nguard += 1; c4 &= X(t, 0) == 1
        n += 1
    # the padding cells are white; varying them cannot change the events, by causality (every cone lies in [p-t, p+t+1])
report('1. vacuum equivalence (%d words, t = 1..%d)' % (n, TMAX), c1)
report('2. vacuum with the black right neighbour', c2)
report('3. W_g / B_g = least black witness; the decompositions are exact and disjoint', c3)
report('4. guarded white-witness criterion (%d guarded words, all output black)' % nguard, c4)
# countercontrols of 4
R = evolve({x: v for x, v in zip(range(-3, 4), [0, 0, 1, 0, 0, 0, 0])}, 1)   # initial 100 on [-1, 1]
report('4. countercontrol: initial 100 at t = 1 gives output 1 while J_0 = {-1} is black', R[1][0] == 1 and R[0][-1] == 1)
R = evolve({x: 0 for x in range(-3, 4)}, 1)
report('4. countercontrol: the all-white row has every J_u white and output 0', R[1][0] == 0)

# 5. three-valued replay of the tick-19 witnesses
U = None
root = '0101010010001101110011101'
row = {x: U for x in range(-60, 61)}
for i, ch in enumerate(root):
    row[-9 + i] = int(ch)


def rule3(a, b, c):
    if b == 1 or c == 1:
        return None if a is None else 1 - a
    if b == 0 and c == 0:
        return a
    # b or c unknown, the other not 1
    if a is None:
        return None
    if a == 0:
        return None   # 0 xor (b or c): unknown
    return None


rows = [row]
for s in range(19):
    r = rows[-1]
    rows.append({x: rule3(r[x - 1], r[x], r[x + 1]) for x in range(min(r) + 1, max(r))})
wit = [(0, -9), (1, -7), (2, -7), (3, -5), (4, -5), (5, -3), (6, -3), (7, -1), (8, -1), (9, 1), (10, 1), (11, 4), (12, 5),
       (13, 6), (14, 6), (15, 8), (16, 8), (17, 10), (18, 9)]
c5 = all(rows[u][j] == 0 and u - 9 <= j <= 27 - u for u, j in wit)
report('5. tick-19: all 19 witnesses forced white from the root alone, each in its J_u', c5)
print('   plain three-valued propagation leaves X(19, 10) = %s (unforced); with initial -8 black in [-9, 29] and the 19\n'
      '   witnesses, criterion 4 forces it to 1 (the carried GC2570 tableau proves the same value)' % rows[19][10])
print('   row 17 on 8..10: %s' % [rows[17][x] for x in (8, 9, 10)])

# 6. moving coordinate
R = evolve({x: v for x, v in zip(range(-4, 5), [0, 0, 0, 1, 0, 1, 0, 0, 0])}, 2)
report('6. moving-coordinate example (101 at time 1; r_1 = 1, r_2 = 0)', [R[1][x] for x in (-1, 0, 1)] == [1, 0, 1] and
       R[1][0] == 0 and R[1][1] == 1 and R[2][0] == 0)
print('ALL PASS' if ok else 'SOME FAIL')
