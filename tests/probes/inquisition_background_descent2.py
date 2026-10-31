#!/usr/bin/env python3
"""inquisition_background_descent2.py: an onset-free D-depth descent certificate for every small periodic background, giving
same-edge rigidity at every depth (L1261, round 6, T-D; D > 1 added for T-D2).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/inquisition_background_descent2.py [PMAX=12] [QMAX=72] [A=4] [BMAX=16] [WORKERS=6] [DLIST=1]
            [ONLY=p:q,p:q,...] [ALIST=4,8]   (DLIST: depth steps D tried in order; ONLY: these backgrounds;
            ALIST: look-behinds tried in order). T-D2 uses bulk windows only (onset-free descent).

Generic two-sided model (as in ether_six_depth_descent_certificate.py): X_j(t), j in Z, any initial state,
X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) at every depth; black-edge rows are the initial states ...0001x1x2...
A background R is a ring cycle (p, q, orbit) of T-G, R_j(t) = orbit[t mod q][j mod p], a two-sided solution.
Window instance W(s, b; r, u): put the top pair at relative depths (0, 1) with alignment (r, u), reference value
R_(j+r)(t+u) at relative depth j and tick t. For EVERY generic configuration (enumerated implicitly by kissat on the
exact light cone, depths lo..1 at t = 0, lo = min(-2(s+b), -1-2s)), if the top pair equals the reference on ticks
0..s+b, then the pair at relative depths (-D, -D+1) equals the reference at tick s (for D = 1 only X_(-1)(s) is new). UNSAT
of the violation proves the instance; lo = min(-2(s+b), -D-2s).
Certificate for R: for every alignment (r, u), the start windows W(s, b_s) for s = 0..A-1 and the bulk window W(A, b)
(look-behind A; by time translation it serves every tick s >= A) hold with look-aheads <= BMAX. Then an episode of length
L >= L0 = max_s (s + b_s) + 1 at depth k+1 contains one of length L - b at depth k, so M_R(k+D) <= max(L0 - 1, M_R(k) + b).
With M_R(1..D) finite (T-G, exhaustive) this gives M_R(k) finite for every k, i.e. no black-edge code follows R at two
adjacent depths forever. Prints, per background, the minimal look-aheads and the implied bounds, or the first alignment
that fails. Controls: the alternating background (2, 2) must FAIL (it attaches, T-G); PR69's ether (4, 8) must pass.
Predictions P-D1..P-D3: reports/inquisition-20261031.md (round 6), committed before this ran.
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inquisition_ring_references import cycles  # noqa: E402

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 72
A = int(sys.argv[3]) if len(sys.argv) > 3 else 4
BMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 16
WORKERS = int(sys.argv[5]) if len(sys.argv) > 5 else 6
DLIST = [int(x) for x in sys.argv[6].split(',')] if len(sys.argv) > 6 else [1]
ONLY = {tuple(int(y) for y in x.split(':')) for x in sys.argv[7].split(',')} if len(sys.argv) > 7 else None
ALIST = [int(x) for x in sys.argv[8].split(',')] if len(sys.argv) > 8 else [A]
WORK = tempfile.mkdtemp(prefix='bdesc2-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))


def holds(orbit, p, q, r, u, s, b, D=1):
    T = s + b
    lo = min(-2 * T, -D - 2 * s)
    ids = {}

    def var(j, t):
        key = (j, t)
        if key not in ids:
            ids[key] = len(ids) + 1
        return ids[key]

    ref = lambda j, t: orbit[(t + u) % q][(j + r) % p]
    cl = []
    for t in range(T):
        for j in range(lo + 2 * (t + 1), 2):
            a, bb, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-a, bb, c, d], [a, -bb, c, d], [a, bb, -c], [-a, -bb, -c], [a, bb, -d], [-a, -bb, -d]]
    for t in range(T + 1):
        for j in (0, 1):
            cl.append([var(j, t)] if ref(j, t) else [-var(j, t)])
    cl.append([(-var(j, s) if ref(j, s) else var(j, s)) for j in (-D, -D + 1)])
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {len(ids)} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        pr = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    if pr.returncode not in (10, 20):
        raise SystemExit(f"kissat failed: {pr.returncode}")
    return pr.returncode == 20


def min_b(orbit, p, q, r, u, s, D=1):
    """Smallest look-ahead b <= BMAX for which W(s, b; r, u) holds (monotone in b), else None."""
    if not holds(orbit, p, q, r, u, s, BMAX, D):
        return None
    lo, hi = 0, BMAX
    while lo < hi:
        mid = (lo + hi) // 2
        if holds(orbit, p, q, r, u, s, mid, D):
            hi = mid
        else:
            lo = mid + 1
    return lo


def certify(p, q, orbit, D=1, a=4):
    """Bulk-only certificate: for every alignment, W(a, b; D) holds for some b <= BMAX. Every onset is an initial
    state, so an episode of length L at depth k+D contains one of length L - a - b at depth k (ticks a..L-1-b):
    M_R(k+D) <= M_R(k) + a + b, with no start windows needed."""
    jobs = [(r, u) for r in range(p) for u in range(q)]
    with ThreadPoolExecutor(WORKERS) as ex:
        res = list(ex.map(lambda j: (j, min_b(orbit, p, q, j[0], j[1], a, D)), jobs))
    fails = [j for j, b in res if b is None]
    if fails:
        return None, fails[:3]
    return max(b for j, b in res), None


def main():
    refs = []
    for p in range(1, PMAX + 1):
        refs += cycles(p, QMAX)
    print(f"{len(refs)} backgrounds; generic one-depth descent windows, look-behind A = {A}, look-ahead <= {BMAX}", flush=True)
    for p, q, orbit in refs:
        if ONLY is not None and (p, q) not in ONLY:
            continue
        name = f"(p={p}, q={q}, {''.join(map(str, orbit[0]))})"
        done = False
        for D in DLIST:
            for a in ALIST:
                bulk, fails = certify(p, q, orbit, D, a)
                if bulk is not None:
                    print(f"{name}: CERTIFIED with D = {D}, look-behind a = {a}: bulk look-ahead b = {bulk}  =>  "
                          f"M_R(k+{D}) <= M_R(k) + {a + bulk} for every k (slope bound {(a + bulk) / D:.2f})", flush=True)
                    if p == 2 and q == 2:
                        raise SystemExit("control failed: the alternating background was certified, yet it attaches")
                    done = True
                    break
                print(f"{name}: no bulk certificate with D = {D}, a = {a} up to b = {BMAX}; failing (r, u): {fails}",
                      flush=True)
            if done:
                break
        if not done and p == 4 and q == 8:
            raise SystemExit("control failed: PR69 ether has no certificate")
    os.rmdir(WORK)
    print("BACKGROUND_DESCENT_DONE")


if __name__ == '__main__':
    main()
