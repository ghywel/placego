#!/usr/bin/env python3
"""L1309 T32 (Local, 2026-11-02): upward rigidity of light-speed phases, by SAT (Kissat).
reports/rule30-genealogy.md section 37 (predictions written first).
Run: python3 tests/probes/upward_rigid.py [PHASE ...] [--dmax D] [--limit S] [--cnf DIR]   PHASE in G8 G16 480 P1024

A state (c_(k-1), c_k) of a phase is upward rigid at depth D if no configuration agrees with the phase on columns
k-1 and k, extends D columns upward (Delta U_j = U_(j+2) OR U_(j+1), j = 0 .. D-1, all columns time-rings of length
p), and has column k-2 different from the phase's. For each class representative, D increases until UNSAT.
UNSAT answers are Kissat-reported; --cnf DIR keeps the CNF files for LRAT certification.
"""
import os
import subprocess
import sys
import tempfile
import time
here = os.path.dirname(os.path.abspath(__file__))
RING16 = ('###..#.#.#####....#...##.##.######..#.###.#.##.##..##.##...####.#.....##..###.#.#..#......####...#.#..#..'
          '###.#..##.#...#.##...#.')


def ring_columns(ring, p):
    """Columns (time-rings of length p) of a ring evolved by c(y)_i = y_i ^ (y_(i-1) | y_(i-2))."""
    N = len(ring); z = list(ring); cols = [0] * N
    for t in range(p):
        for i in range(N):
            cols[i] |= z[i] << t
        z = [z[i] ^ (z[i - 1] | z[i - 2]) for i in range(N)]
    assert z == list(ring), 'ring does not return after p steps'
    return cols


def phases():
    out = {}
    out['G8'] = (8, ring_columns([1, 0, 0, 0], 8), list(range(1)))
    out['G16'] = (16, ring_columns([1 if ch == '#' else 0 for ch in RING16], 16), list(range(8)))
    cyc = [tuple(int(x, 16) for x in l.split()) for l in open(os.path.join(here, 'phase480_p32.txt')) if not l.startswith('#')]
    out['480'] = (32, [u for u, v in cyc], list(range(30)))           # column i = u_i; state (u_i, v_i) = (col i, col i+1)
    ring = [int(ch) for ch in open(os.path.join(here, 'phase1024_ring.txt')).read().strip()]
    out['P1024'] = (1024, ring_columns(ring, 1024), [0])
    return out


def cnf(p, cols, k, D):
    """Fixed U_0 = col k, U_1 = col k-1; unknown U_2 .. U_(D+1); deviation U_2 != col k-2."""
    N = len(cols); nv = 0; cl = []
    U = []
    for j in range(D + 2):
        U.append(list(range(nv + 1, nv + p + 1))); nv += p
    for j, c in ((0, cols[k % N]), (1, cols[(k - 1) % N])):
        for t in range(p):
            cl.append([U[j][t] if (c >> t) & 1 else -U[j][t]])
    for j in range(D):
        for t in range(p):
            nv += 1; o = nv; a, b = U[j + 2][t], U[j + 1][t]
            cl += [[-a, o], [-b, o], [a, b, -o]]
            x, y = U[j][(t + 1) % p], U[j][t]
            for bx in (0, 1):
                for by in (0, 1):
                    for bo in (0, 1):
                        if bx ^ by ^ bo:
                            cl.append([x if not bx else -x, y if not by else -y, o if not bo else -o])
    ph = cols[(k - 2) % N]
    cl.append([-U[2][t] if (ph >> t) & 1 else U[2][t] for t in range(p)])
    return nv, cl


def solve(nv, cl, limit, keep=None):
    with tempfile.TemporaryDirectory() as td:
        fn = keep or os.path.join(td, 'i.cnf')
        with open(fn, 'w') as f:
            f.write('p cnf %d %d\n' % (nv, len(cl)))
            for c in cl:
                f.write(' '.join(map(str, c)) + ' 0\n')
        try:
            out = subprocess.run(['kissat', '-q', fn], capture_output=True, text=True, timeout=limit).stdout
        except subprocess.TimeoutExpired:
            return 'TIMEOUT'
        return 'SAT' if '\ns SATISFIABLE' in '\n' + out else ('UNSAT' if 'UNSATISFIABLE' in out else 'TIMEOUT')


if __name__ == '__main__':
    args = sys.argv[1:]
    dmax = int(args[args.index('--dmax') + 1]) if '--dmax' in args else 16
    limit = int(args[args.index('--limit') + 1]) if '--limit' in args else 120
    keep = args[args.index('--cnf') + 1] if '--cnf' in args else None
    names = [a for a in args if a in ('G8', 'G16', '480', 'P1024')] or ['G8', 'G16', '480', 'P1024']
    ph = phases()
    for name in names:
        p, cols, reps = ph[name]; t0 = time.time(); res = []
        for k in reps:
            got = None
            for D in range(1, dmax + 1):
                nv, cl = cnf(p, cols, k, D)
                kf = os.path.join(keep, '%s_k%d_D%d.cnf' % (name, k, D)) if keep else None
                r = solve(nv, cl, limit, kf)
                if r == 'UNSAT':
                    got = D; break
                if r == 'TIMEOUT':
                    got = 'timeout at D=%d' % D; break
            res.append(got)
            print('%s p=%d state k=%d: %s' % (name, p, k, ('upward rigid at depth D=%d' % got) if isinstance(got, int)
                                                  else (got or 'SAT up to D=%d' % dmax)), flush=True)
        ok = [r for r in res if isinstance(r, int)]
        print('== %s: %d of %d state classes upward rigid; largest D needed %s; %.0f s' % (
            name, len(ok), len(res), max(ok) if ok else None, time.time() - t0), flush=True)
