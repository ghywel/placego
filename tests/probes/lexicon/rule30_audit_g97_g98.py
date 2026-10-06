#!/usr/bin/env python3
"""rule30_audit_g97_g98.py: Local's second reading of GPT's G97 (the moving-frame flip law under a fair spatial
ensemble, and temporal independence for non-rightward observers) and G98 (clock reparametrization, lattice diamonds,
background-dependent fronts, non-commuting local updates), independent of GPT's SC1-SC3 and DC1-DC2. Exact
enumeration. (Local, 2026-10-06; PROOFS.md notes; chat.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g97_g98.py      (seconds)

CHECKS (GPT's claims at a233f59 and 5bb1aac):
  P1 (G97): every output word of length k = 1..10 has exactly four preimages of length k + 2.
  P2 (G97): over the 32 five-cell neighbourhoods, flips after a left, stay and right step number 16, 16, 24, and the
     three Boolean forms (a XOR (b AND NOT c), b XOR (c OR d) XOR c, d OR e) are the literal ones.
  P3 (G97 corollary): for every increment word over {-1, 0} of length 1..5, evolving every initial word on the cone,
     the sampled vector (s_0..s_N) is uniform; with one +1 step the flip probability is 3/4 instead.
  P4 (G98): the row-interval diamond count equals a path-reachability count for T = 0..14, |X| <= T; 5 at T = 2, X = 0.
  P5 (G98): from one black cell on the zero background the leftmost black is at -t for t <= 60; the two local update
     orders from a seed at site 1 give {0} and {0, 1}.
  P6 (G98): the continuum diamond area (bT - X)(X + aT)/(a + b) is maximal at X/T = (b - a)/2 (a = 0.246, b = 1, grid).
"""
from itertools import product

fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


R30 = lambda l, c, r: l ^ (c | r)
ok = True
for k in range(1, 11):
    cnt = {}
    for s in range(2 ** (k + 2)):
        x = [(s >> i) & 1 for i in range(k + 2)]
        y = tuple(R30(x[i], x[i + 1], x[i + 2]) for i in range(k))
        cnt[y] = cnt.get(y, 0) + 1
    ok &= len(cnt) == 2 ** k and set(cnt.values()) == {4}
check('P1 four preimages for every output word, k = 1..10', ok)
fl = {-1: 0, 0: 0, 1: 0}
forms = True
for a, b, c, d, e in product((0, 1), repeat=5):
    nxt = {-1: R30(a, b, c), 0: R30(b, c, d), 1: R30(c, d, e)}
    for v in (-1, 0, 1):
        fl[v] += nxt[v] ^ c
    forms &= (nxt[-1] ^ c) == (a ^ (b & (1 - c))) and (nxt[0] ^ c) == (b ^ (c | d) ^ c) and (nxt[1] ^ c) == (d | e)
check('P2 flips 16, 16, 24 and the three Boolean forms', (fl[-1], fl[0], fl[1]) == (16, 16, 24) and forms, str(fl))


def samples(init, lo, incs):
    """init: dict site -> bit on [lo, hi]; evolve by full rows on the shrinking valid interval; observer at 0."""
    row, L, H = init, lo, max(init)
    p, out = 0, [init[0]]
    for inc in incs:
        row = {i: R30(row[i - 1], row[i], row[i + 1]) for i in range(L + 1, H)}
        L, H = L + 1, H - 1
        p += inc
        out.append(row[p])
    return tuple(out)


ok3 = True
for n in range(1, 6):
    for incs in product((-1, 0), repeat=n):
        lo, hi = -2 * n, n             # every cell the observer's cone needs, with margin
        cnt = {}
        for s in range(2 ** (hi - lo + 1)):
            init = {lo + i: (s >> i) & 1 for i in range(hi - lo + 1)}
            v = samples(init, lo, incs)
            cnt[v] = cnt.get(v, 0) + 1
        ok3 &= len(cnt) == 2 ** (n + 1) and len(set(cnt.values())) == 1
flip_right = 0
for s in range(2 ** 6):
    init = {-3 + i: (s >> i) & 1 for i in range(6)}
    v = samples(init, -3, (1,))
    flip_right += v[0] ^ v[1]
check('P3 non-rightward observers: sample vectors uniform (all words to length 5); one right step flips 3/4',
      ok3 and flip_right * 4 == 3 * 64, '%d/64' % flip_right)


def formula(T, X):
    return sum(max(0, min(s, X + T - s) - max(-s, X - T + s) + 1) for s in range(T + 1))


def reach(T, X):
    fut = {(0, 0)}
    frontier = {(0, 0)}
    for s in range(1, T + 1):
        frontier = {(s, y + d) for (_, y) in frontier for d in (-1, 0, 1)}
        fut |= frontier
    return sum(1 for (s, y) in fut if abs(X - y) <= T - s)


ok4 = all(formula(T, X) == reach(T, X) for T in range(15) for X in range(-T, T + 1))
check('P4 diamond row-interval count = reachability count, T <= 14; T = 2, X = 0 gives 5', ok4 and formula(2, 0) == 5)
row = {0}
ok5 = True
for t in range(1, 61):
    row = {i for i in range(-t - 1, t + 2) if R30(int(i - 1 in row), int(i in row), int(i + 1 in row))}
    ok5 &= min(row) == -t
st = {1}
for i in (0, 1):
    v = R30(int(i - 1 in st), int(i in st), int(i + 1 in st))
    st = (st | {i}) if v else (st - {i})
st2 = {1}
for i in (1, 0):
    v = R30(int(i - 1 in st2), int(i in st2), int(i + 1 in st2))
    st2 = (st2 | {i}) if v else (st2 - {i})
check('P5 leftmost black at -t on the zero background (t <= 60); local orders give {0} and {0, 1}',
      ok5 and st == {0} and st2 == {0, 1}, '%s %s' % (sorted(st), sorted(st2)))
a, b, T = 0.246, 1.0, 1000
areas = [((b * T - X) * (X + a * T) / (a + b), X) for X in range(int(-a * T), int(b * T) + 1)]
check('P6 continuum area maximal at X/T = (b - a)/2 = 0.377', abs(max(areas)[1] / T - (b - a) / 2) <= 0.001,
      '%.3f' % (max(areas)[1] / T))
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
