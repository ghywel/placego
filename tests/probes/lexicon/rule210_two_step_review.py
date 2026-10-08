#!/usr/bin/env python3
"""rule210_two_step_review.py: TS, Local's independent reading of GC459 (GPT's two-step readout: a white intervening
bit gives x_(t+2)(j+2) = x_t(j) XOR ((1 - x_t(j+3)) x_t(j+4)), and, with GC458's two vanishing statements,
x_(2n+2)(3) = s_n XOR x_(2n)(5) in every empty-left full 0101 Rule 210 orbit), requested by GPT's review flag of
2026-10-08. Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_two_step_review.py
COST:       to be recorded (expected seconds).

What this adds to GPT's controls. GC459's controls are 32 local patches; its translated embedding cannot fail, since
the two-step central bit has radius two and never sees the exterior bits. This reading tests the identity and its
application on actual orbit prefixes: a census of every empty-left full 0101 prefix to depth T = 48 (sites 1 .. T at
time 0; every site left of the centre white; centre x_t(0) = t mod 2 for t = 0 .. T). With sites beyond T unknown, a
cell x_t(i) is determined exactly when i + t <= T, and every check below stays inside that cone.

Own coding as in PX (rule210_prefix_review.py): a row is an integer, site i at bit B - (i + OFF), stepped as
new = (row >> 1) ^ (~row & (row << 1)), masked. s_n = x_(2n)(1), V_t(i) = x_t(i) x_t(i+1).

PREDICTIONS (Local's, published before the run):
  TS-P1: all 16 five-bit inputs with a white intervening bit satisfy Q = s XOR ((1 - h) z) under this coding, and
         exactly 4 of them (h = z = 1) have Q != s XOR z (GC459's counts reproduced).
  TS-P2: on every census survivor, at every n with 2n + 5 <= T: x_(2n)(2) = 0 and V_(2n)(4) = 0 (GC458 / G231's two
         statements), and x_(2n+2)(3) = s_n XOR x_(2n)(5) (GC459's application), with no failure near the frontier.
  TS-P3 (blind, confidence 0.5): the census has exactly one survivor at every depth 7 .. 48.
  TS-P4: G26's effective input holds on every survivor: s_0 = 1 and s_n = floor(log2 n) mod 2 for 1 <= n,
         2n + 1 <= T.
  TS-P5 (in-orbit counterfactual, confidence 0.7): somewhere in the survivors' determined cones a cell has a white
         intervening bit x_t(j+1) = 0 but h z = x_t(j+3) x_t(j+4) = 1, so the second hypothesis is not idle in real
         orbits, not only in local patches.
  TS-C0 (control): the integer coding agrees with a scalar truth-table evolution on every survivor's cone.
  TS-C1 (control): the identity holds at every (t, j) in every survivor's cone with x_t(j+1) = 0 and t + 2 <= T
         (a failure here would be a coding fault or a false identity).
OUTCOME (first run), 2026-10-08 05:05 (M5, one run at commit 657ed9c; transcript outside Git; 0.0 s).
  TS-P1 HELD: 16 white inputs; the 4 that need the h z correction are exactly those with h = z = 1.
  TS-P2 HELD: G231's two vanishings and GC459's application hold at every n with 2n + 5 <= 48 on every survivor; no
         frontier failure.
  TS-P3 REFUTED: survivor counts by depth run 1, 2, 3, 6, 1, 2 with period 6 from depth 1. Exactly one survivor at
         every depth = 1 or 5 (mod 6); at the other depths up to six, differing only in trailing sites not yet decided.
         The unique depth-47 prefix is the set of sites 1 .. 47 coprime to 6, {1, 5, 7, 11, 13, ..., 43, 47}.
  TS-P4 HELD. TS-C0 and TS-C1 PASS.
  TS-P5 HELD as stated, but only through a frontier artefact: its single witness (t 0, j 44, patch 00011) lies on the
         depth-48 survivor whose undecided site 48 is black. On the forced prefix (sites 1 .. 47, coprime to 6) no cone
         cell with a white intervening bit has h z = 1.
Observation after the run (not predicted; hand proof, to be filed through review). Every site coprime to 6 is odd, so
the row R(i) = [i >= 1 and gcd(i, 6) = 1] has black cells only where t + i is odd at t = 0. G26's parity argument then
runs over the whole line: adjacent cells are never both black, (1 - c) r = r, and the orbit is exactly Rule 90. Even
times leave the centre white. At odd t = 2m + 1 the centre is the sum of C(2m+1, j) over m + 1 <= j <= 2m + 1 with
j != m + 2 (mod 3) (site i = 2j - 2m - 1). That index set is symmetric under j -> 2m + 1 - j, and the trisection
formula gives the j = m + 2 class the total (2^(2m+1) - 2)/3, so the sum is (2^(2m+1) + 1)/3, a Jacobsthal number,
always odd (1, 3, 11, 43, ...). So R gives an empty-left full 0101 Rule 210 orbit: the family GC454 .. GC459 speak of is
not empty. Every member equals R exactly when every member has all even initial sites white: those then run Rule 90,
whose odd sites the centre fixes triangularly (site t enters time t with coefficient 1). The census forces R through
site 47.

DEEP MODE (python3 tests/probes/lexicon/rule210_two_step_review.py deep), predictions published before its run:
  TS-P6: the seed R restricted to sites 1 .. 3000 gives centre x_t(0) = t mod 2 for every t <= 3000.
  TS-P7: the census continued to depth 240 keeps the count pattern by depth mod 6 (1:1, 2:2, 3:3, 4:6, 5:1, 0:2), and
         every unique survivor (depths = 1, 5 mod 6) is R restricted to sites 1 .. d.
  TS-P8: inside R's determined cone through 3000 (i + t <= 3000), every black cell has t + i odd and no two adjacent
         cells are black, so every product V_t(i) vanishes and Rule 210 acts as Rule 90 throughout.
  TS-C2 (control): for m < 300 the exact integer sum above equals (2^(2m+1) + 1)/3.
"""
import time

T = 48
B = 160
MASK = (1 << (B + 1)) - 1
OFF = 60                                   # site i lives at bit B - (i + OFF)


def bit(row, i):
    return (row >> (B - (i + OFF))) & 1


def step(row):
    return ((row >> 1) ^ (~row & (row << 1))) & MASK


def rows_of(sites, n):
    row = 0
    for i in sites:
        row |= 1 << (B - (i + OFF))
    out = [row]
    for _ in range(n):
        out.append(step(out[-1]))
    return out


def scalar_rows(sites, n):
    rule = {(l, c, r): (210 >> (4 * l + 2 * c + r)) & 1 for l in (0, 1) for c in (0, 1) for r in (0, 1)}
    lo, hi = -n - 4, T + n + 8
    cells = {i: 0 for i in range(lo, hi + 1)}
    for i in sites:
        cells[i] = 1
    out = [dict(cells)]
    for _ in range(n):
        cells = {i: rule[cells.get(i - 1, 0), cells[i], cells.get(i + 1, 0)] for i in range(lo, hi + 1)}
        out.append(dict(cells))
    return out


def two_step(patch):
    s, b, q, h, z = patch
    row = 0
    for k, v in enumerate(patch):
        if v:
            row |= 1 << (B - (10 + k + OFF))
    return bit(step(step(row)), 12)


def census():
    alive, counts = [[]], {}
    for d in range(1, T + 1):
        nxt = []
        for pre in alive:
            for v in (0, 1):
                sites = [i + 1 for i, b in enumerate(pre + [v]) if b]
                rs = rows_of(sites, d)
                if all(bit(rs[t], 0) == t % 2 for t in range(d + 1)):
                    nxt.append(pre + [v])
        alive = nxt
        counts[d] = len(alive)
    return alive, counts


def main():
    t0 = time.time()
    white = [p for p in ((a, 0, c, e, f) for a in (0, 1) for c in (0, 1) for e in (0, 1) for f in (0, 1))]
    p1 = all(two_step(p) == p[0] ^ ((1 - p[3]) * p[4]) for p in white)
    corr = [p for p in white if two_step(p) != p[0] ^ p[4]]
    p1 = p1 and len(white) == 16 and len(corr) == 4 and all(p[3] == p[4] == 1 for p in corr)
    print('TS-P1', 'HELD' if p1 else 'REFUTED', '(16 white inputs; %d need the h z correction)' % len(corr))

    alive, counts = census()
    print('survivors by depth:', ' '.join('%d:%d' % (d, counts[d]) for d in range(1, T + 1)))
    p3 = all(counts[d] == 1 for d in range(7, T + 1))
    p2 = p4 = c0 = c1 = True
    p5 = 0
    worst = []
    for pre in alive:
        sites = [i + 1 for i, b in enumerate(pre) if b]
        rs = rows_of(sites, T)
        sc = scalar_rows(sites, T)
        x = lambda t, i: bit(rs[t], i)
        for t in range(T + 1):
            for i in range(-t - 2, T - t + 1):
                if x(t, i) != sc[t][i]:
                    c0 = False
        for n in range(0, T):
            if 2 * n + 5 > T:
                break
            ok = (x(2 * n, 2) == 0 and x(2 * n, 4) * x(2 * n, 5) == 0
                  and x(2 * n + 2, 3) == x(2 * n, 1) ^ x(2 * n, 5))
            if not ok:
                p2 = False
                worst.append(('P2', n))
        for n in range(0, T):
            if 2 * n + 1 > T:
                break
            want = 1 if n == 0 else (n.bit_length() - 1) % 2
            if x(2 * n, 1) != want:
                p4 = False
                worst.append(('P4', n))
        for t in range(0, T - 1):
            for j in range(-t, T - t - 3):
                if j + 4 + t > T:
                    continue
                if x(t, j + 1) == 0:
                    if x(t + 2, j + 2) != x(t, j) ^ ((1 - x(t, j + 3)) * x(t, j + 4)):
                        c1 = False
                    if x(t, j + 3) * x(t, j + 4) == 1:
                        p5 += 1
    print('survivor sites (depth %d): %s' % (T, [[i + 1 for i, b in enumerate(p) if b] for p in alive]))
    print('TS-P2', 'HELD' if p2 and alive else 'REFUTED', worst[:6])
    print('TS-P3', 'HELD' if p3 else 'REFUTED')
    print('TS-P4', 'HELD' if p4 and alive else 'REFUTED')
    print('TS-P5', 'HELD' if p5 else 'REFUTED', '(%d in-orbit cells with a white intervening bit and h z = 1)' % p5)
    print('TS-C0', 'PASS' if c0 else 'FAIL')
    print('TS-C1', 'PASS' if c1 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


def deep():
    global B, MASK, OFF, T
    t0 = time.time()
    N, D = 3000, 240
    B, OFF = 2 * N + 40, N + 20
    MASK = (1 << (B + 1)) - 1
    R = [i for i in range(1, N + 1) if i % 6 in (1, 5)]
    rs = rows_of(R, N)
    p6 = all(bit(rs[t], 0) == t % 2 for t in range(N + 1))
    print('TS-P6', 'HELD' if p6 else 'REFUTED')
    pos_par = [sum(1 << p for p in range(B + 1) if p % 2 == k) for k in (0, 1)]
    p8 = True
    for t in range(N + 1):
        cone = MASK & ~((1 << (B - (N - t + OFF))) - 1)
        row = rs[t] & cone
        # site i at bit p = B - i - OFF; t + i even <=> p = t + B - OFF (mod 2)
        if row & pos_par[(t + B - OFF) % 2] or row & (row >> 1):
            p8 = False
            print('P8 fails at t', t)
            break
    print('TS-P8', 'HELD' if p8 else 'REFUTED')
    c2 = True
    for m in range(300):
        n = 2 * m + 1
        s, c = 0, 1
        for j in range(n + 1):
            if j >= m + 1 and (j - m - 2) % 3:
                s += c
            c = c * (n - j) // (j + 1)
        c2 &= s == (2 ** n + 1) // 3 and (2 ** n + 1) % 3 == 0
    print('TS-C2', 'PASS' if c2 else 'FAIL')
    B, OFF, T = 2 * D + 40, D + 20, D
    MASK = (1 << (B + 1)) - 1
    alive, counts = census()
    want = {1: 1, 2: 2, 3: 3, 4: 6, 5: 1, 0: 2}
    pat = all(counts[d] == want[d % 6] for d in range(1, D + 1))
    uniq = True
    alive, _ = [[]], None
    for d in range(1, D + 1):
        nxt = []
        for pre in alive:
            for v in (0, 1):
                sites = [i + 1 for i, b in enumerate(pre + [v]) if b]
                r2 = rows_of(sites, d)
                if all(bit(r2[t], 0) == t % 2 for t in range(d + 1)):
                    nxt.append(pre + [v])
        alive = nxt
        if d % 6 in (1, 5):
            uniq &= len(alive) == 1 and [i + 1 for i, b in enumerate(alive[0]) if b] == [i for i in R if i <= d]
    print('counts', ' '.join(str(counts[d]) for d in range(1, D + 1)))
    print('TS-P7', 'HELD' if pat and uniq else 'REFUTED', '(pattern %s, unique-and-R %s)' % (pat, uniq))
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    import sys
    deep() if sys.argv[1:] == ['deep'] else main()
