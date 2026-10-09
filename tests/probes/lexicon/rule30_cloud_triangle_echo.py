#!/usr/bin/env python3
"""rule30_cloud_triangle_echo.py: EC, the triangle-top echo C(d, s) under fair rows, exactly, as rationals.

RUN-ON:     cpu, one core (Python 3 standard library; bit-sliced big integers); seconds, under 1 GB
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_triangle_echo.py [DMAX=9]

Why. CL095's velocimetry measured C(d, d) = 0, 2.10, 0.25, 1.92, 0.73, 1.25, 0.87, 1.37 (d = 1 .. 8) on a fair
random line. C(d, s) is P(top at (r, i) and top at (r + d, i + s)) / P(top)^2, a top being the left end of a bounded
white run of width at most 3 that does not continue a run one cell wider on each side in the row before
(rule30_cloud_velocimetry.py, tops()). GPT's GC851 proved that a top depends on seven sites of the previous row, and
that tops are independent outside d - 6 <= s <= d + 6. So under an iid fair row (G97: every evolved row is again iid
fair) C(d, s) is a finite sum over 7 + 2d + |s - d| sites, an exact rational. CL102's queue named this closed form.

Method. Enumerate every assignment of row r - 1 on the window that both events need, all at once (each site a
2^n-bit integer), evolve it d + 1 steps with the light cone shrinking by a cell a side, and count the assignments
where each event holds. P(top) comes from its own seven-site window. Every number is an exact fraction.

Record searched: "C\\(d, ?d\\)" with "exact|rational|closed form" -> only VE-U in rule30_cloud_velocimetry.py (the
measured values); "triangle" with "density" -> §8.68's 3 2^-(L+4) law for core triangles and C5's 3/32 width-1
birth density (GC847). No exact C(d, s) in the record.

PREDICTIONS, written 2026-10-09 22:01 BST, before any run of this script.
  EC-C1 (control, must hold): C(d, s) = 1 exactly for s = d - 7 and s = d + 7 at d = 1, 2, 3 (GC851's band).
  EC-C2 (control, must hold): a direct simulation of a 2^20-cell fair random line over 64 rows gives P(top) and
         C(1, 1), C(2, 2) within 4 standard errors of the exact values.
  EC-P1 (0.6): the exact C(d, d) agree with CL095's measured values within 0.15 at every d = 1 .. 8.
  EC-P2 (0.6): C(1, 1) = 0 exactly: no top has another top one row down and one cell right.
  EC-P3 (0.5): C(d, d) - 1 alternates in sign exactly from d = 1 to DMAX.
  EC-U, the unexpected check (0.4): the even-d excesses C(d, d) - 1 decrease strictly with d (the measured 0.25 at
         d = 6 against 0.37 at d = 8 is noise).
  Counterfactual. If EC-P1 fails by more than the measurement's scale, the random-line run was not measuring the
  fair-row law, and CL095's line should be re-read. If EC-P3 fails, the "alternation law in triangles" reading of
  CL095 was too strong.
"""
import random
import sys
from fractions import Fraction

DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9


def var_masks(n):
    nbytes = max(1, (1 << n) // 8)
    out = []
    for i in range(n):
        if i < 3:
            pat = bytes([(0xAA, 0xCC, 0xF0)[i]]) * nbytes
        else:
            b = 1 << (i - 3)
            pat = (b'\x00' * b + b'\xff' * b) * (nbytes // (2 * b))
        out.append(int.from_bytes(pat, 'little') & ((1 << (1 << n)) - 1))
    return out


def step(cells):
    return [cells[j - 1] ^ (cells[j] | cells[j + 1]) for j in range(1, len(cells) - 1)]


def top(P, R, full):
    """P: previous row at a-2 .. a+4 (7 cells); R: this row at a-1 .. a+3 (5 cells). Returns the event's mask."""
    ev = 0
    for k in (1, 2, 3):
        run = R[0] & R[k + 1]
        for j in range(1, k + 1):
            run &= ~R[j]
        cont = P[0] & P[k + 3]
        for j in range(1, k + 3):
            cont &= ~P[j]
        ev |= run & ~cont & full
    return ev


def p_top():
    n = 7
    full = (1 << (1 << n)) - 1
    P = var_masks(n)
    R = step(P)
    return Fraction(top(P, R[0:5], full).bit_count(), 1 << n)


def joint(d, s):
    lo, hi = min(-2, s - 2 - d), max(4, s + 4 + d)
    n = hi - lo + 1
    full = (1 << (1 << n)) - 1
    S = [var_masks(n)]
    for _ in range(d + 1):
        S.append(step(S[-1]))

    def cells(k, x0, x1):                                  # row r - 1 + k, positions x0 .. x1 (relative to i)
        return [S[k][x - lo - k] for x in range(x0, x1 + 1)]
    A = top(cells(0, -2, 4), cells(1, -1, 3), full)
    B = top(cells(d, s - 2, s + 4), cells(d + 1, s - 1, s + 3), full)
    return Fraction((A & B).bit_count(), 1 << n)


def simulate_check(pt, exact):
    rng = random.Random(12)
    W = 1 << 20
    x = rng.getrandbits(W)
    rows = [x]
    mask = (1 << W) - 1
    for _ in range(66):
        x = ((x << 1) ^ (x | (x >> 1))) & mask            # bit j's left neighbour is bit j - 1
        rows.append(x)
    # tops by the same seven-site rule, as bitsets over a band away from the edges
    lo, hi = 200, W - 200
    band = ((1 << (hi - lo)) - 1) << lo

    def topset(prev, cur):
        def sh(v, k):                                      # bit a of the result is bit a + k of v
            return v >> k if k >= 0 else v << -k
        ev = 0
        for k in (1, 2, 3):
            run = sh(cur, -1) & sh(cur, k)
            for j in range(0, k):
                run &= ~sh(cur, j)
            cont = sh(prev, -2) & sh(prev, k + 1)
            for j in range(-1, k + 1):
                cont &= ~sh(prev, j)
            ev |= run & ~cont
        return ev & band
    E = [topset(rows[t - 1], rows[t]) for t in range(1, len(rows))]
    nb = hi - lo
    n_top = sum(e.bit_count() for e in E)
    n_cells = nb * len(E)
    pm = n_top / n_cells
    out = [('P(top)', pm, float(pt), (pm * (1 - pm) / n_cells) ** 0.5)]
    for d in (1, 2):
        jn = sum((E[t] & (E[t + d] >> d)).bit_count() for t in range(len(E) - d))
        nn = nb * (len(E) - d)
        cm = (jn / nn) / pm ** 2
        se = max(cm, 1e-9) ** 0.5 / (nn * pm ** 2) ** 0.5
        out.append(('C(%d, %d)' % (d, d), cm, float(exact[d]), se))
    return out


def main():
    pt = p_top()
    print('P(top) = %s = %.6f' % (pt, float(pt)), flush=True)
    c1 = True
    for d in (1, 2, 3):
        for s in (d - 7, d + 7):
            v = joint(d, s) / pt ** 2
            print('control C(%d, %d) = %s' % (d, s, v))
            c1 = c1 and v == 1
    print('EC-C1 (C = 1 outside the band): %s' % ('PASS' if c1 else 'FAIL'), flush=True)
    exact = {}
    for d in range(1, DMAX + 1):
        exact[d] = joint(d, d) / pt ** 2
        print('C(%d, %d) = %s = %.6f' % (d, d, exact[d], float(exact[d])), flush=True)
    chk = simulate_check(pt, exact)
    c2 = all(abs(m - e) <= 4 * se for _, m, e, se in chk)
    for name, m, e, se in chk:
        print('  direct %s: %.5f against exact %.5f (se %.5f)' % (name, m, e, se))
    print('EC-C2 (direct simulation within 4 se): %s' % ('PASS' if c2 else 'FAIL'))
    measured = [0, 2.10, 0.25, 1.92, 0.73, 1.25, 0.87, 1.37]
    ok = c1 and c2
    nd = 'NOT DECIDED (controls)'
    p1 = all(abs(float(exact[d]) - measured[d - 1]) <= 0.15 for d in range(1, 9)) if DMAX >= 8 else None
    print('EC-P1 (within 0.15 of the measured values, d = 1 .. 8): %s' % (
        nd if not ok or p1 is None else ('HELD' if p1 else 'REFUTED')))
    print('EC-P2 (C(1, 1) = 0): %s' % (nd if not ok else ('HELD' if exact[1] == 0 else 'REFUTED')))
    alt = all((exact[d] - 1) * (exact[d + 1] - 1) < 0 for d in range(1, DMAX))
    print('EC-P3 (C(d, d) - 1 alternates in sign, d = 1 .. %d): %s' % (DMAX, nd if not ok else (
        'HELD' if alt else 'REFUTED')))
    ev = [exact[d] - 1 for d in range(2, DMAX + 1, 2)]
    u = all(ev[k] > ev[k + 1] for k in range(len(ev) - 1))
    print('EC-U (even-d excesses strictly decreasing): %s %s' % (
        [round(float(v), 4) for v in ev], nd if not ok else ('HELD' if u else 'REFUTED')))


if __name__ == '__main__':
    main()
