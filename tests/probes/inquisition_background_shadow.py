#!/usr/bin/env python3
"""inquisition_background_shadow.py: do the backgrounds that resist descent have shadows? (L1261, round 6, T-S3)

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/inquisition_background_shadow.py [BLIST=24,48,96] [A=8]

For each background that T-D2 could not certify, and one-depth windows (D = 1, look-behind A), it asks kissat for a
generic configuration on the exact light cone whose top pair follows the background on ticks 0..A+b while the pair one
depth down misses it at tick A, for the first alignment that T-D2 reports failing, at each b in BLIST. A violation that
survives b = 96 means the top pair's 105 ticks do not determine the next depth: evidence of a shadow (a different
solution sharing the pair). Also, from the b = max model, it prints the mismatch pattern of depths -1..-6 on ticks
0..15 against the background. Controls: PR69's ether and (5, 5) must give UNSAT already at b = 24 (T-D certified them).
Prediction P-S1..P-S2: reports/inquisition-20261031.md (round 6), committed before this ran.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]          # the ring module parses argv at import
from inquisition_ring_references import cycles  # noqa: E402
sys.argv = _argv

BLIST = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else [24, 48, 96]
A = int(sys.argv[2]) if len(sys.argv) > 2 else 8
WORK = tempfile.mkdtemp(prefix='shadow-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
# first failing alignment (r, u) at D = 1, a = 8 from T-D2's output; controls use (0, 0)
CASES = {(7, 28): (0, 13), (7, 63): (0, 4), (8, 20): None, (9, 72): None, (9, 57): None, (10, 6): None,
         (12, 68): None, (12, 12): None, (4, 8): (0, 0), (5, 5): (0, 0)}


def instance(orbit, p, q, r, u, s, b):
    T = s + b
    lo = min(-2 * T, -1 - 2 * s)
    ids = {}

    def var(j, t):
        if (j, t) not in ids:
            ids[(j, t)] = len(ids) + 1
        return ids[(j, t)]

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
    return ids, cl, ref


def solve(ids, cl):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {len(ids)} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        pr = subprocess.run(['kissat', '-q', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    if pr.returncode == 20:
        return None
    if pr.returncode != 10:
        raise SystemExit(f"kissat failed {pr.returncode}")
    lits = [int(x) for line in pr.stdout.splitlines() if line.startswith('v') for x in line.split()[1:]]
    return {abs(x): x > 0 for x in lits if x}


def first_failing(orbit, p, q, s, b):
    for r in range(p):
        for u in range(q):
            ids, cl, ref = instance(orbit, p, q, r, u, s, b)
            if solve(ids, cl) is not None:
                return (r, u)
    return None


def main():
    refs = [c for p in range(1, 13) for c in cycles(p, 72)]
    for p, q, orbit in refs:
        if (p, q) not in CASES:
            continue
        al = CASES[(p, q)] or first_failing(orbit, p, q, A, BLIST[0])
        name = f"(p={p}, q={q})"
        if al is None:
            print(f"{name}: no failing alignment at b = {BLIST[0]} (certifiable at D = 1, a = {A})", flush=True)
            continue
        r, u = al
        line, model = [], None
        for b in BLIST:
            ids, cl, ref = instance(orbit, p, q, r, u, A, b)
            m = solve(ids, cl)
            line.append(f"b={b}: {'SAT (violation exists)' if m else 'UNSAT'}")
            if m:
                model = (ids, m, ref, b)
        print(f"{name} alignment {al}: " + '; '.join(line), flush=True)
        if model:
            ids, m, ref, b = model
            for j in range(-1, -7, -1):
                row = ''.join(('x' if m.get(ids[(j, t)], False) != bool(ref(j, t)) else '.') if (j, t) in ids else ' '
                              for t in range(16))
                print(f"     depth {j:3d} mismatch on ticks 0..15: {row}", flush=True)
        if (p, q) in ((4, 8), (5, 5)) and any('SAT' in x and 'UNSAT' not in x for x in line):
            raise SystemExit("control failed: a certified background has a violation")
    os.rmdir(WORK)
    print("SHADOW_DONE")


if __name__ == '__main__':
    main()
