#!/usr/bin/env python3
"""rule30_kick_lock.py: KLK, how far out the structure that forbids a class-12 kick lies, as a function of the time
on the wheel (Local's run, committed in L226 under draw-and-work; claimed in CLOUD-LOCAL.md with these predictions
pushed before the run).

RUN-ON:     cpu; kissat on the PATH; one process per instance, JOBS at a time
COMMAND:    python3 tests/probes/lexicon/rule30_kick_lock.py [JOBS=8]
COST:       some minutes to half an hour (to be recorded).

The question is KS's and KK's (rule30_kick_bite_kissat.py, whose encoding is reused here): column 1 on the wheel U
at an even phase d for N steps, a departure at class 12, then 21 observations on a new phase; the row at t0 free;
t0 in {0, 1} and the 28 even phases, 56 cases. Here the cone is capped at width m: Rule 30 is imposed on columns
1 .. m only, and column m + 1 is free at every time, as in entry 26's automaton. A larger m can only remove
solutions. "Class 12 dies at (N, m)" means all 56 cases are UNSAT.
  1. The least N, in 113 .. 140, at which class 12 dies at full width (bisection; full width is KK's encoding).
  2. For N = 140, 147, 154, 161, 168: the least m at which class 12 dies (bisection over m in 12 .. 60).

PREDICTIONS, Local's, published before the run:
  KLK-C1 (control, CL028): at N = 168 the least m is 37 (class 12 alive at every case for m <= 36).
  KLK-C2 (control, KK): at full width class 12 is alive at N = 112 and dead at N = 140, so step 1's answer lies in
         113 .. 140.
  KLK-P1 (blind): the least m grows with N, and at N = 140, 147, 154, 161 it lies within 3 of 0.22 N (Cloud's
         reading of a locked region growing at about 0.22 columns per step).
  KLK-P2 (blind, uncertain): the least full-width N lies in 120 .. 135.
OUTCOME, 2026-10-07 21:38 (M5, one run at commit 04255b2, 277 s with 8 kissat processes; transcript outside Git).
KLK-C2 PASS: at full width class 12 is alive at 15 of 56 cases at N = 112 and dead at N = 140. Bisection: 1 case alive
at N = 126, none at 127, 129, 133, so the least full-width N is 127 (KLK-P2 HELD). KLK-C1 PASS: at N = 168 the least m
is 37. KLK-P1 REFUTED: the least m is 37 at every N = 140, 147, 154, 161, 168. It does not grow with the time on the
wheel, so the reading of a locked region spreading at about 0.22 columns per step does not survive. Whatever forbids
class 12 lies in a fixed band of 37 columns once N >= 140. Caveat: the bisection over N assumes that deaths stay dead
as N grows, which was not proved (a wider m can only remove solutions, so the bisection over m is sound).
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv

U, P = kk.U, kk.P
JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 8


def instance_capped(t0, d, a, N, m):
    """KK's instance with Rule 30 imposed on columns 1 .. m only (column m + 1 free); m = None is full width."""
    s = t0 + N
    while (s - d) % P != a:
        s += 1
    E = s + 20
    var = {}
    nv = [0]

    def v(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]

    clauses = []
    for t in range(t0 + 1, E + 1):
        top = 1 + (E - t) if m is None else min(m, 1 + (E - t))
        for i in range(1, top + 1):
            y, b, c = v(t, i), v(t - 1, i), v(t - 1, i + 1)
            nv[0] += 1
            o = nv[0]
            clauses += [[-b, o], [-c, o], [b, c, -o]]
            if i == 1:
                clauses += [[-y, o], [y, -o]] if (t - 1) % 2 == 0 else [[y, o], [-y, -o]]
            else:
                l = v(t - 1, i - 1)
                clauses += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for t in range(t0, s):
        clauses.append([v(t, 1) if U[(t - d) % P] else -v(t, 1)])
    sels = []
    for dn in range(0, P, 2):
        if U[(s - dn) % P] == U[(s - d) % P]:
            continue
        nv[0] += 1
        sel = nv[0]
        sels.append(sel)
        for t in range(s, E + 1):
            clauses.append([-sel, v(t, 1) if U[(t - dn) % P] else -v(t, 1)])
    clauses.append(sels)
    return nv[0], clauses


def solve(args):
    t0, d, N, m = args
    nv, clauses = instance_capped(t0, d, 12, N, m)
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
        path = f.name
    r = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
    os.unlink(path)
    return {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'ERROR %d' % r.returncode)


def alive(N, m, ex):
    res = list(ex.map(solve, [(t0, d, N, m) for t0 in (0, 1) for d in range(0, P, 2)]))
    if any(r.startswith('ERROR') for r in res):
        raise SystemExit('solver error at N %d m %s' % (N, m))
    return sum(r == 'SAT' for r in res)


def main():
    out = {}
    with ThreadPoolExecutor(JOBS) as ex:
        a112, a140 = alive(112, None, ex), alive(140, None, ex)
        print('full width: alive cases at N 112: %d, N 140: %d' % (a112, a140), flush=True)
        c2 = a112 > 0 and a140 == 0
        lo, hi = 112, 140                       # alive at lo, dead at hi
        while hi - lo > 1:
            mid = (lo + hi) // 2
            k = alive(mid, None, ex)
            print('  full width N %d: %d alive' % (mid, k), flush=True)
            lo, hi = (mid, hi) if k else (lo, mid)
        nfull = hi
        print('least full-width N with class 12 dead: %d' % nfull, flush=True)
        for N in (140, 147, 154, 161, 168):
            lo, hi = 12, 60                     # expect alive at lo, dead at hi
            if not alive(N, lo, ex) or alive(N, hi, ex):
                print('N %d: bracket [12, 60] does not hold' % N, flush=True)
                out[N] = None
                continue
            while hi - lo > 1:
                mid = (lo + hi) // 2
                k = alive(N, mid, ex)
                lo, hi = (mid, hi) if k else (lo, mid)
            out[N] = hi
            print('N %d: least m with class 12 dead = %d (0.22 N = %.1f)' % (N, hi, 0.22 * N), flush=True)
    print('KLK-C1', 'PASS' if out.get(168) == 37 else 'FAIL (%s)' % out.get(168))
    print('KLK-C2', 'PASS' if c2 else 'FAIL')
    p1 = all(out.get(N) is not None and abs(out[N] - 0.22 * N) <= 3 for N in (140, 147, 154, 161))
    pairs = ((140, 147), (147, 154), (154, 161), (161, 168))
    p1 &= all(out[a] <= out[b] for a, b in pairs if out.get(a) and out.get(b))
    print('KLK-P1', 'HELD' if p1 else 'REFUTED')
    print('KLK-P2', 'HELD' if 120 <= nfull <= 135 else 'REFUTED')


if __name__ == '__main__':
    main()
