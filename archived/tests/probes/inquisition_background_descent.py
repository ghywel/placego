#!/usr/bin/env python3
"""inquisition_background_descent.py: a one-depth descent certificate for every small periodic background, giving
same-edge rigidity at every depth (L1261, round 6, T-D).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/inquisition_background_descent.py [PMAX=12] [QMAX=72] [A=4] [BMAX=16] [WORKERS=6]

Generic two-sided model (as in ether_six_depth_descent_certificate.py): X_j(t), j in Z, any initial state,
X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) at every depth; black-edge rows are the initial states ...0001x1x2...
A background R is a ring cycle (p, q, orbit) of T-G, R_j(t) = orbit[t mod q][j mod p], a two-sided solution.
Window instance W(s, b; r, u): put the top pair at relative depths (0, 1) with alignment (r, u), reference value
R_(j+r)(t+u) at relative depth j and tick t. For EVERY generic configuration (enumerated implicitly by kissat on the
exact light cone, depths lo..1 at t = 0, lo = min(-2(s+b), -1-2s)), if the top pair equals the reference on ticks
0..s+b, then the pair at relative depths (-1, 0) equals the reference at tick s. (Only X_(-1)(s) is new.) UNSAT of the
violation proves the instance.
Certificate for R: for every alignment (r, u), the start windows W(s, b_s) for s = 0..A-1 and the bulk window W(A, b)
(look-behind A; by time translation it serves every tick s >= A) hold with look-aheads <= BMAX. Then an episode of length
L >= L0 = max_s (s + b_s) + 1 at depth k+1 contains one of length L - b at depth k, so M_R(k+1) <= max(L0 - 1, M_R(k) + b).
With M_R(1) finite (T-G, exhaustive) this gives M_R(k) finite for every k, i.e. no black-edge code follows R at two
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
WORK = tempfile.mkdtemp(prefix='bdesc-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))


def holds(orbit, p, q, r, u, s, b):
    T = s + b
    lo = min(-2 * T, -1 - 2 * s)
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
    cl.append([(-var(j, s) if ref(j, s) else var(j, s)) for j in (-1, 0)])
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


def min_b(orbit, p, q, r, u, s):
    """Smallest look-ahead b <= BMAX for which W(s, b; r, u) holds (monotone in b), else None."""
    if not holds(orbit, p, q, r, u, s, BMAX):
        return None
    lo, hi = 0, BMAX
    while lo < hi:
        mid = (lo + hi) // 2
        if holds(orbit, p, q, r, u, s, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def certify(p, q, orbit):
    jobs = [(r, u, s) for r in range(p) for u in range(q) for s in range(A + 1)]
    with ThreadPoolExecutor(WORKERS) as ex:
        res = list(ex.map(lambda j: (j, min_b(orbit, p, q, *j)), jobs))
    fails = [j for j, b in res if b is None]
    if fails:
        return None, fails[:3]
    bulk = max(b for (r, u, s), b in res if s == A)
    starts = [max(b for (r, u, s), b in res if s == s0) for s0 in range(A)]
    L0 = max(s0 + starts[s0] for s0 in range(A)) + 1
    return (bulk, starts, L0), None


def main():
    refs = []
    for p in range(1, PMAX + 1):
        refs += cycles(p, QMAX)
    print(f"{len(refs)} backgrounds; generic one-depth descent windows, look-behind A = {A}, look-ahead <= {BMAX}", flush=True)
    for p, q, orbit in refs:
        cert, fails = certify(p, q, orbit)
        name = f"(p={p}, q={q}, {''.join(map(str, orbit[0]))})"
        if cert is None:
            print(f"{name}: NO certificate up to b = {BMAX}; first failing (r, u, s): {fails}", flush=True)
            if p == 4 and q == 8:
                raise SystemExit("control failed: PR69 ether has no certificate")
        else:
            bulk, starts, L0 = cert
            print(f"{name}: CERTIFIED  bulk look-ahead b = {bulk}, start look-aheads {starts}, L0 = {L0}  =>  "
                  f"M_R(k+1) <= max({L0 - 1}, M_R(k) + {bulk}) for every k", flush=True)
            if p == 2 and q == 2:
                raise SystemExit("control failed: the alternating background was certified, yet it attaches")
    os.rmdir(WORK)
    print("BACKGROUND_DESCENT_DONE")


if __name__ == '__main__':
    main()
