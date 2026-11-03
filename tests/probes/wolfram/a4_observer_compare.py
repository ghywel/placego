#!/usr/bin/env python3
"""L1472 (Local, 2026-11-03): an independent machine check of GC2577's claim that the fifteen-state observer rejects every
base path that GC2564's six-flag 0011 monitor rejects (new accepted is a subset of old accepted). Random input sequences
drive A4's one-way window (W = 16) from pattern 3's actual state at t0 = 3000 on 1010000 (0, 4); both monitors run with the
existential input filter (a due colour constrains only an ACTIVE input; joins of two known values for the same physical
cell reject on disagreement, even on an ignored input). Reports, over many paths, how often the old monitor rejects, whether
the new one has rejected by the same tick, and the saved emptying path's outcome.
Run: python3 tests/probes/wolfram/a4_observer_compare.py DATA63.json PATH.json NPATHS LEN SEED [literal]
"""
import json
import random
import sys

import numpy as np

data = json.load(open(sys.argv[1])); pj = json.load(open(sys.argv[2])); NP, LEN, SEED = map(int, sys.argv[3:6])
LITERAL = len(sys.argv) > 6 and sys.argv[6] == 'literal'  # GC2579: use only the due value as known c (GC2577's formulas)
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
rule = lambda a, b, c: a ^ (b | c)


def step1(state, bit):
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else bit)
    new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
    if new[0] != Eb(0, 1):
        ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
    else:
        ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
    Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
    return ((tq + 1) % q, ndq, ns), mv, any(ns[i] != Enew(i + 1) for i in range(len(ns)))


def old_step(fl, strip, mv, active, label):
    """GC2564: flags (am, a0, ap, b0, bp, c); returns new flags or None (reject)."""
    am, a0, ap, b0, bp, c = fl
    if c and active and label == 0:
        return None
    g = {d: strip[len(strip) + d - 4: len(strip) + d] == (0, 0, 1, 1) for d in (-2, -1, 0)}
    if mv == 0:
        return (g[-1], g[0], False, a0, ap, bp)
    return (g[-2], g[-1], g[0], am, a0, b0)


def join(u, v):
    if u is None: return v, True
    if v is None or u == v: return u, True
    return None, False


def new_step(fl, strip, mv, active, label):
    """GC2577: (p0, p1, c) each None/0/1; returns new flags or None (reject)."""
    p0, p1, c = fl
    if c is not None and active and label != c:
        return None
    known_c = c if (c is not None or LITERAL) else (label if active else None)
    a, b = strip[-2], strip[-1]
    def a10(i):  # a10 ending at strip index i (0-based): strip[i-2], strip[i-1], strip[i] = v, 1, 0
        return strip[i - 2] if strip[i - 1] == 1 and strip[i] == 0 else None
    gm1, g0 = a10(len(strip) - 2), a10(len(strip) - 1)
    g1 = a if (b == 1 and known_c == 0) else None
    if mv == 0:
        qv = (1 - b) if known_c == 1 else None
        cc, ok = join(p1, qv)
        return (g0, g1, cc) if ok else None
    qv = (1 - a) if b == 1 else ((a ^ known_c) if known_c is not None else None)
    cc, ok = join(p0, qv)
    return (gm1, g0, cc) if ok else None


def run(start, word):
    st = start; fo = (False,) * 6; fn = (None, None, None); ro = rn = None
    for t, label in enumerate(word):
        nst0, mv0, al0 = step1(st, 0); nst1, mv1, al1 = step1(st, 1)
        active = nst0 != nst1
        nst, mv, alive = (nst1, mv1, al1) if label else (nst0, mv0, al0)
        if ro is None:
            o = old_step(fo, st[2], mv, active, label)
            if o is None: ro = t
            else: fo = o
        if rn is None:
            n = new_step(fn, st[2], mv, active, label)
            if n is None: rn = t
            else: fn = n
        if not alive:
            return ro, rn, t
        st = nst
    return ro, rn, None


dec = lambda e: (e[0], e[1], tuple(int(ch) for ch in e[2]))
start = dec(pj['start'])
ro, rn, te = run(start, pj['word'])
print('saved emptying word: old monitor rejects at tick %s, new observer at tick %s; window empties at %s' % (ro, rn, te))
act = pj['actual_inputs']
ro, rn, te = run(start, act)
print('soundness control, the actual evolution\'s %d inputs: old rejects at %s, new at %s (expected None, None); empties at %s'
      % (len(act), ro, rn, te))
# a longer soundness control: the actual evolution's inputs along the one-way window for 600 ticks
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
T0, TL, W = 3000, 600, len(start[2])
TM = T0 + TL + 5; lo = -2 * TM - 10; hi = TM + W + 40; c0 = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy(); row[c0] ^= 1; row[c0 + 1] ^= 1
for _ in range(T0):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
A = int(np.flatnonzero(row ^ bg).min()) - 1 - c0
assert (T0 % q, (T0 - A) % N, tuple(int(v) for v in row[c0 + A + 1: c0 + A + 1 + W])) == start
acts = []; st = start
for t in range(TL):
    bit = int(row[c0 + A + W + 1]); acts.append(bit)
    st, mv, alive = step1(st, bit)
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    A += mv
    assert st[2] == tuple(int(v) for v in row[c0 + A + 1: c0 + A + 1 + W]) and alive
ro, rn, te = run(start, acts)
print('soundness control, the actual evolution\'s %d inputs: old rejects at %s, new at %s (expected None, None)' % (TL, ro, rn))
random.seed(SEED); old_rej = both = new_only = viol = 0
for _ in range(NP):
    w = [random.randint(0, 1) for _ in range(LEN)]
    ro, rn, te = run(start, w)
    if ro is not None:
        old_rej += 1
        if rn is not None and rn <= ro: both += 1
        else: viol += 1
    elif rn is not None:
        new_only += 1
print('%d random paths of length %d: old rejects %d; new had rejected by the same tick in %d; VIOLATIONS (old rejects, new not yet) %d; new rejects where old accepts %d'
      % (NP, LEN, old_rej, both, viol, new_only))
print('A4_OBSERVER_COMPARE_DONE')
