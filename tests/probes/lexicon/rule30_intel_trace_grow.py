#!/usr/bin/env python3
"""rule30_intel_trace_grow.py: SX's SAT engine (SX-P10): the real column-1 traces T(l) beside the wall grown level by
level, the minimal absent traces, and the least excluding width w(f) of each, in either wall phase.

RUN-ON:     the Intel MacBook; Python 3 with pysat 1.9 (CaDiCaL 1.5.3); a pool of worker processes
COMMAND:    python3 tests/probes/lexicon/rule30_intel_trace_grow.py PHASE LMAX [WORKERS]
            (writes NP_SCRATCH_SX/grow_p{PHASE}_l{LMAX}.log: "T l |T(l)|" and "M l trace w(f)")

Wall x_t(0) = (t + phase) mod 2; rule x_{t+1}(i) = x_t(i-1) XOR (x_t(i) OR x_t(i+1)); a trace is y_t = x_t(1), t =
0..l-1. Realness: one CaDiCaL instance holds the light cone of column 1 to time CONE - 1 (cells (t, i), 1 <= i <= CONE
- t, CONE = LMAX + 2), with an auxiliary o = (b OR c) per cell; a trace prefix is tested by assumptions on column 1,
so a prefix of any length l <= CONE is real exactly when the solver answers SAT (the cone's further cells are free).
Growth: T(l+1) is the set of real g + b with g in T(l) and (g + b)[2:] in T(l-1) (a two-step shift keeps the phase, so
real traces are closed under it); the candidates that are not real are the minimal absent traces. Strips: the width-W
instance keeps the cells (t, i), i <= W, with a free input e_t beside column W; f is in T^W(l) exactly when it answers
SAT with f assumed; w(f) is found by bisection, since T^(W+1) is contained in T^W and T^l(l) = T(l).
"""
import os, sys, time
from multiprocessing import Pool
from pysat.solvers import Solver

CONE = 66                     # the light cone's depth; set to LMAX + 2 by the command line
PHASE = None
_G = {}


def _cone_clauses(phase, n, width=None):
    """clauses and the column-1 variables of the light cone (width None) or of the width-W strip, times 0..n-1"""
    var = {}; nxt = [1]; cl = []

    def v(key):
        if key not in var: var[key] = nxt[0]; nxt[0] += 1
        return var[key]
    W = width
    for t in range(n):
        top = n - t if W is None else min(W, n - t)
        for i in range(1, top + 1): v(('x', t, i))
    for t in range(1, n):
        top = n - t if W is None else min(W, n - t)
        for i in range(1, top + 1):
            y = v(('x', t, i)); b = v(('x', t - 1, i))
            if W is not None and i == W: c = v(('e', t - 1))                       # the free input beside column W
            else: c = v(('x', t - 1, i + 1))
            o = v(('o', t, i))
            cl += [[-b, o], [-c, o], [-o, b, c]]
            if i == 1:
                if (t - 1 + phase) & 1: cl += [[y, o], [-y, -o]]                    # y = NOT o
                else: cl += [[y, -o], [-y, o]]                                      # y = o
            else:
                a = v(('x', t - 1, i - 1))
                cl += [[-y, a, o], [-y, -a, -o], [y, -a, o], [y, a, -o]]
    col1 = [var[('x', t, 1)] for t in range(n)]
    return cl, col1


def _init(phase, cone):
    global PHASE, CONE
    PHASE, CONE = phase, cone
    cl, col1 = _cone_clauses(phase, CONE)
    s = Solver(name='cadical153', bootstrap_with=cl)
    _G['cone'] = (s, col1); _G['strips'] = {}


def _strip(W):
    if W not in _G['strips']:
        cl, col1 = _cone_clauses(PHASE, CONE, width=W)
        _G['strips'][W] = (Solver(name='cadical153', bootstrap_with=cl), col1)
    return _G['strips'][W]


def _assume(col1, f): return [col1[t] if c == '1' else -col1[t] for t, c in enumerate(f)]


def is_real(f):
    s, col1 = _G['cone']; return f, s.solve(assumptions=_assume(col1, f))


def least_width(f):
    lo, hi = 1, len(f)                          # f is in T^W for W < w(f), not for W >= w(f); not in T^l(l)
    while lo < hi:
        mid = (lo + hi) // 2
        s, col1 = _strip(mid)
        if s.solve(assumptions=_assume(col1, f)): lo = mid + 1
        else: hi = mid
    return f, lo


def grow(phase, lmax, workers=8, log=None):
    t0 = time.time(); out = open(log, 'w') if log else sys.stdout
    T = {0: {''}, 1: {'0', '1'}}
    print(f'T 1 2', file=out, flush=True)
    with Pool(workers, initializer=_init, initargs=(phase, lmax + 2)) as pool:
        for l in range(1, lmax):
            cands = [g + b for g in sorted(T[l]) for b in '01' if l + 1 < 3 or (g + b)[2:] in T[l - 1]]
            res = pool.map(is_real, cands, chunksize=max(1, len(cands) // (8 * workers)))
            T[l + 1] = {f for f, ok in res if ok}; absent = sorted(f for f, ok in res if not ok)
            widths = pool.map(least_width, absent, chunksize=1) if absent else []
            print(f'T {l + 1} {len(T[l + 1])}', file=out, flush=True)
            for f, w in widths: print(f'M {l + 1} {f} {w}', file=out, flush=True)
            if l >= 2: T.pop(l - 1, None)
            print(f'  phase {phase} l = {l + 1}: |T| = {len(T[l + 1])}, minimal absent {len(absent)}, '
                  f'{time.time() - t0:.0f} s', file=sys.stderr, flush=True)
    if log: out.close()


if __name__ == '__main__':
    phase, lmax = int(sys.argv[1]), int(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    scratch = os.environ.get('NP_SCRATCH_SX', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-sx'))
    os.makedirs(scratch, exist_ok=True)
    grow(phase, lmax, workers, os.path.join(scratch, f'grow_p{phase}_l{lmax}.log'))
