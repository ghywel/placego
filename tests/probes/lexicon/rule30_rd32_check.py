#!/usr/bin/env python3
"""rule30_rd32_check.py: Local's second reading of GPT's RD32 (rule30_debt32.c, GC325): an independent recomputation, in
Python, of the slope-5/2 whole-prefix reference debt D and the endpoint drawup h on all sixteen rooted histories at the
common frontier 2^20 = 1,048,576, at common period 32.

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_rd32_check.py
COST:       several minutes; cap 1,200 CPU s.

Shared with RD32: only the child constructor rule30_rq3.children. Written separately: the walk (period 32 from the root,
rotation children followed once, genuine branches both ways), the clock, the debt, the drawup. Clock: T = 0 at the
root (0, 1^32); at depth d with driver w_d, delay 0 if w_d = 0, else 1 + the least i >= 0 with w_d(T_d + i mod 32) = 1.
With z_d = 2 T_d - 5 d (doubled units), D = max over a <= b <= F of z_b - z_a and h = z_F - min z, halved. The clock is
also recorded at GPT's witness depths to check each witness's elapsed time and debt. TM6 found no period-32 zero below
65,821,412, so every history reaches the frontier without a further zero; any zero above depth 894,234 aborts.
No predictions: this verifies a published table, and any disagreement is reported as found.
OUTCOME, 2026-10-07 17:56 (M5, one run; CPU 163.2 s): ALL AGREE. The sixteen histories reach the frontier with their
known N_5; every D (32.5, 40, 40.5, 43.5, 39.5, 39.5, 36.5, 39.5, 39.5, 39.5, 42.5, 40, 39.5, 45, 60, 60 in N_5 order),
every endpoint h (0, 0, 10, 2, 4, 3.5, 0, 3.5, 3.5, 2, 0.5, 0, 7.5, 0, 3.5, 0) and every witness's elapsed time and debt
equal RD32's table. Separately, GPT's rule30_debt32.c, built and run here on M5 (0.376 s CPU), printed the same table
and certified the frontier: a separate execution of GPT's code and a separately written recomputation both agree.
"""
import resource
import sys

sys.path.insert(0, __import__('os').path.dirname(__file__))
import rule30_rq3 as rq3

Q, FULL, F = 32, (1 << 32) - 1, 1 << 20
RD32 = {87867: (65, 0, (147140, 147181), 135), 183184: (80, 0, (170583, 170617), 125),
        196189: (81, 20, (615612, 615661), 163), 229338: (87, 4, (97505, 97540), 131),
        253537: (79, 8, (120349, 120368), 87), 271596: (79, 7, (120349, 120368), 87),
        291257: (73, 0, (235434, 235471), 129), 527724: (79, 7, (120349, 120368), 87),
        551910: (79, 7, (120349, 120368), 87), 555813: (79, 4, (120349, 120368), 87),
        575211: (85, 1, (504520, 504561), 145), 634886: (80, 0, (609521, 609551), 115),
        645655: (79, 15, (120349, 120368), 87), 667052: (90, 0, (798744, 798770), 110),
        770532: (120, 7, (725127, 725155), 130), 894235: (120, 0, (725127, 725155), 130)}   # doubled D, doubled h
NEED = sorted({x for v in RD32.values() for x in v[2]})


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def reset_delay(w, T):
    if w == 0:
        return 0
    for i in range(Q):
        if (w >> ((T + i) % Q)) & 1:
            return i + 1


def is_rot(u, v):
    return any(rq3.rot(u, k, Q) == v for k in range(Q))


results = []
# stack items: (x, y, depth, T, zmin, D, n5 or None, recorded clocks)
stack = [(0, FULL, 0, 0, 0, 0, None, {})]
while stack:
    x, y, d, T, zmin, D, n5, rec = stack.pop()
    rec = dict(rec)
    while True:
        if cpu() > 1200:
            print('CAP')
            sys.exit(1)
        z = 2 * T - 5 * d
        D = max(D, z - zmin)
        zmin = min(zmin, z)
        if d in NEED:
            rec[d] = T
        if d == F:
            results.append((n5, D, z - zmin, rec))
            break
        if y == 0:
            if d > 894234:
                print('UNEXPECTED period-32 zero at depth %d' % d)
                sys.exit(1)
            kids = rq3.children(x, 0, Q)
            c1, c2 = kids
            if is_rot(c1, c2):
                if d > 399 and n5 is None:
                    n5 = d + 1                                   # the doubling 16 -> 32 is this history's N_5
            else:
                stack.append((0, c2, d + 1, T, zmin, D, n5, rec))
            x, y, d = 0, c1, d + 1
            continue
        T += reset_delay(y, T)
        x, y, d = y, rq3.children(x, y, Q)[0], d + 1

ok = sorted(r[0] for r in results) == sorted(RD32)
print('sixteen histories reach the frontier with the known N_5:', ok, len(results))
for n5, D, h, rec in sorted(results):
    dd, hh, (a, b), el = RD32[n5]
    wit = rec[b] - rec[a] == el and 2 * el - 5 * (b - a) == dd
    good = D == dd and h == hh and wit
    print('N_5 %7d: D %5.1f (RD32 %5.1f), h %5.1f (RD32 %5.1f), witness [%d, %d] elapsed %d (RD32 %d): %s'
          % (n5, D / 2, dd / 2, h / 2, hh / 2, a, b, rec[b] - rec[a], el, 'agree' if good else 'DISAGREE'))
    ok &= good
print('ALL AGREE' if ok else 'DISAGREEMENT FOUND', '; CPU %.1f s' % cpu())
