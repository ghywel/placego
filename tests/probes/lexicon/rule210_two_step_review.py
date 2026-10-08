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
OUTCOME: not yet run.
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


if __name__ == '__main__':
    main()
