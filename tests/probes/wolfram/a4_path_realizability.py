#!/usr/bin/env python3
"""L1452 (Local, 2026-11-03): GC2548's test. Is the masked emptying path (a4_emptying_word.py's v2 export) realizable by
some right extension of the actual state? Run:
python3 tests/probes/wolfram/a4_path_realizability.py DATA63.json PATH.json OUT.cnf
Fixed: pattern PATTERN's exact row at T0 at and left of the window (background half-line and W-cell strip). Free: the cells
at relative positions W + 1 .. W + H (H = path length), the only ones that reach an input within H ticks (the anchor
never moves right). Constraints: Rule 30 on that light cone for H ticks, and the input cell at each READ tick equal to the
word. CaDiCaL (python-sat). A model is replayed by plain simulation: the one-way window must follow the path and empty.
"""
import json
import sys

import numpy as np
from pysat.solvers import Solver

data = json.load(open(sys.argv[1])); pj = json.load(open(sys.argv[2])); CNF = sys.argv[3]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
rule = lambda a, b, c: a ^ (b | c)
PAT, T0, W = pj['pattern'], pj['T0'], pj['W']; word = pj['word']; H = len(word)
dec = lambda e: (e[0], e[1], tuple(int(ch) for ch in e[2]))
path = [(dec(s), b, mv) for s, b, mv in pj['path']]


def step1(state, b):
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
    new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
    if new[0] != Eb(0, 1):
        ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
    else:
        ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
    Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
    return ((tq + 1) % q, ndq, ns), mv, any(ns[i] != Enew(i + 1) for i in range(len(ns)))


read = [(step1(st, 0)[0] != step1(st, 1)[0]) for st, _, _ in path]
# exact row at T0
TM = T0 + H + 5; lo = -2 * TM - 10; hi = TM + 22; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
for t in range(1, T0 + 1):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
Fi = int(np.flatnonzero(row ^ bg).min()); A0 = Fi - 1 - c
start = (T0 % q, (T0 - A0) % N, tuple(int(v) for v in row[Fi: Fi + W]))
assert start == path[0][0], 'the exported start state is not the actual state'
# anchor positions and input cells along the path
A = [A0]
for _, _, mv in path:
    A.append(A[-1] + (mv if mv is not None else 0))
xin = [A[k] + W + 1 for k in range(H)]
# variables: cell (k, x) for k = 0..H, x from XL to A0 + W + H - k (the light cone of the free cells)
XL = A0 - H - 3; XR = lambda k: A0 + W + H - k
vid = {}
def v(k, x):
    if (k, x) not in vid:
        vid[(k, x)] = len(vid) + 1
    return vid[(k, x)]
cl = []
for x in range(XL, XR(0) + 1):  # time T0 values
    if x <= A0 + W:
        val = int(row[c + x]); cl.append([v(0, x) if val else -v(0, x)])
for k in range(H):
    for x in range(XL + 1, XR(k + 1) + 1):
        a, b_, cc, o = v(k, x - 1), v(k, x), v(k, x + 1), v(k + 1, x)
        for la in (0, 1):
            for lb in (0, 1):
                for lc in (0, 1):
                    out = rule(la, lb, lc)
                    lit = lambda var, val: -var if val else var
                    cl.append([lit(a, la), lit(b_, lb), lit(cc, lc), o if out else -o])
    # the left boundary column XL at time k + 1 is background, unaffected by the free cells (XL + H < A0 + W + 1)
    t_abs = T0 + k + 1
    cl.append([v(k + 1, XL)] if E(XL, t_abs) else [-v(k + 1, XL)])
for k in range(H):
    if read[k]:
        cl.append([v(k, xin[k])] if word[k] else [-v(k, xin[k])])
# controls (L1452): the actual evolution's values at the same read space-time points must be SAT; and the shortest
# prefix of the word's read constraints that is already UNSAT
base = [c_ for c_ in cl[:len(cl) - sum(read)]]
act_rows = [row.copy()]
r_ = row.copy()
for k in range(H):
    n = np.zeros_like(r_); n[1:-1] = r_[:-2] ^ (r_[1:-1] | r_[2:]); r_ = n; act_rows.append(r_.copy())
ctl = base + [[v(k, xin[k])] if int(act_rows[k][c + xin[k]]) else [-v(k, xin[k])] for k in range(H) if read[k]]
with Solver(name='cadical195', bootstrap_with=ctl) as s_:
    print('positive control (the actual values at the same %d read points): %s' % (sum(read), 'SAT' if s_.solve() else 'UNSAT'))
reads = [k for k in range(H) if read[k]]
lo_, hi_ = 0, len(reads)
def unsat_prefix(m):
    with Solver(name='cadical195', bootstrap_with=base + [[v(k, xin[k])] if word[k] else [-v(k, xin[k])] for k in reads[:m]]) as s_:
        return not s_.solve()
while lo_ < hi_:
    mid = (lo_ + hi_) // 2
    if unsat_prefix(mid):
        hi_ = mid
    else:
        lo_ = mid + 1
print('shortest UNSAT prefix of the word\'s read constraints: %d of %d (the last of them at tick %s)' % (
    lo_, len(reads), reads[lo_ - 1] if lo_ else None))
nfree = sum(1 for x in range(A0 + W + 1, XR(0) + 1))
print('pattern %d T0=%d W=%d: path length %d, read inputs %d; free cells %d (relative %d..%d); variables %d, clauses %d' % (
    PAT, T0, W, H, sum(read), nfree, W + 1, W + H, len(vid), len(cl)))
with open(CNF, 'w') as f:
    f.write('p cnf %d %d\n' % (len(vid), len(cl)))
    for c_ in cl:
        f.write(' '.join(map(str, c_)) + ' 0\n')
with Solver(name='cadical195', bootstrap_with=cl) as s:
    sat = s.solve(); model = s.get_model() if sat else None
print('CaDiCaL: %s' % ('SAT' if sat else 'UNSAT'))
if sat:
    ms = set(l for l in model if l > 0)
    ext = [1 if v(0, x) in ms else 0 for x in range(A0 + W + 1, XR(0) + 1)]
    print('a realizing right extension (relative %d..%d): %s' % (W + 1, W + H, ''.join(map(str, ext))))
    print('the actual cells there:                       %s' % ''.join(str(int(row[c + x])) for x in range(A0 + W + 1, XR(0) + 1)))
    # replay: replace those cells, evolve the whole row, follow the one-way window
    r2 = row.copy()
    for i, x in enumerate(range(A0 + W + 1, XR(0) + 1)):
        r2[c + x] = ext[i]
    st = start; Aa = A0; emptied = None
    for k in range(H):
        b = int(r2[c + Aa + W + 1])
        if read[k]:
            assert b == word[k], 'replay input differs at a read tick'
        nst, mv, alive = step1(st, b)
        n = np.zeros_like(r2); n[1:-1] = r2[:-2] ^ (r2[1:-1] | r2[2:]); r2 = n
        Aa += mv
        if not alive:
            emptied = k + 1; break
        assert nst[2] == tuple(int(v_) for v_ in r2[c + Aa + 1: c + Aa + 1 + W]), 'window replay mismatch'
        assert nst == path[k + 1][0], 'replay leaves the exported path'
        st = nst
    print('forward replay by plain simulation: follows the path, window empties at step %s' % emptied)
print('A4_PATH_REALIZABILITY_DONE')
