#!/usr/bin/env python3
"""L1309 T33 (Local, 2026-11-02): is there a short wall from the rain into a phase? Two-point SAT (Kissat).
reports/rule30-genealogy.md section 37.4 (predictions written first).
Run: python3 tests/probes/rain_to_phase.py PHASE DMIN DMAX LIMIT_S [rev | from SRC | dlist D1,D2,...]
(PHASE in G8 G16 480 P1024; SRC in G8 G16: every state of SRC, lifted to PHASE's period, is tried on top.)
With rev the roles swap (phase state on top, rain at the bottom): a wall from the phase into the rain, the control
direction, which the complete cores at p = 8 and 16 say exists.

Columns c_0 (top) .. c_(D+3) (bottom), all time-rings of length p. Top two: a rain state, (a, NOT a) or (NOT a, a),
with a = 0101... . Bottom two: a fixed state (c_(k-1), c_k) of the phase. In between, every column obeys
Delta c_j = c_(j-2) OR c_(j-1) (j = 2 .. D+3), the same local constraints as upward_rigid.py.
A SAT answer is a wall from the rain into the phase of D transition columns: with the black edge above the rain and the
phase below, an eternal point under a black edge that is not the rain. UNSAT answers are Kissat-reported.
"""
import os
import subprocess
import sys
import tempfile
import time
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'upward_rigid.py')).read().split("if __name__ == '__main__':")[0]
src = src.replace("here = os.path.dirname(os.path.abspath(__file__))", "here = %r" % here)
exec(src)


def cnf2(p, top, bot, D):
    n = D + 4; nv = n * p; cl = []
    V = [list(range(j * p + 1, j * p + p + 1)) for j in range(n)]
    for j, c in ((0, top[0]), (1, top[1]), (n - 2, bot[0]), (n - 1, bot[1])):
        for t in range(p):
            cl.append([V[j][t] if (c >> t) & 1 else -V[j][t]])
    for j in range(2, n):
        for t in range(p):
            nv += 1; o = nv; a, b = V[j - 2][t], V[j - 1][t]
            cl += [[-a, o], [-b, o], [a, b, -o]]
            x, y = V[j][(t + 1) % p], V[j][t]
            for bx in (0, 1):
                for by in (0, 1):
                    for bo in (0, 1):
                        if bx ^ by ^ bo:
                            cl.append([x if not bx else -x, y if not by else -y, o if not bo else -o])
    return nv, cl, V


if __name__ == '__main__':
    name, dmin, dmax, limit = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rev = len(sys.argv) > 5 and sys.argv[5] == 'rev'
    p, cols, reps = phases()[name]; N = len(cols); M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    bot = (cols[(0 - 1) % N], cols[0])
    tops = [(A, M ^ A), (M ^ A, A)]; src = 'rain'
    if 'from' in sys.argv:
        src = sys.argv[sys.argv.index('from') + 1]; q, qcols, _ = phases()[src]; NQ = len(qcols)
        lift = lambda c: sum(((c >> (t % q)) & 1) << t for t in range(p))
        tops = []
        for k in range(NQ):
            for r in range(q):
                st = tuple(lift(((qc >> r) | (qc << (q - r))) & ((1 << q) - 1)) for qc in (qcols[(k - 1) % NQ], qcols[k]))
                if st not in tops:
                    tops.append(st)
    Ds = [int(x) for x in sys.argv[sys.argv.index('dlist') + 1].split(',')] if 'dlist' in sys.argv else range(dmin, dmax + 1)
    for D in Ds:
        nsat = nun = nto = 0
        for top in tops:
            t0 = time.time(); nv, cl, V = cnf2(p, bot, top, D) if rev else cnf2(p, top, bot, D)
            with tempfile.TemporaryDirectory() as td:
                fn = os.path.join(td, 'i.cnf')
                with open(fn, 'w') as f:
                    f.write('p cnf %d %d\n' % (nv, len(cl)))
                    for c in cl:
                        f.write(' '.join(map(str, c)) + ' 0\n')
                try:
                    out = subprocess.run(['kissat', '-q', fn], capture_output=True, text=True, timeout=limit).stdout
                    r = 'SAT' if '\ns SATISFIABLE' in '\n' + out else ('UNSAT' if 'UNSATISFIABLE' in out else 'TIMEOUT')
                except subprocess.TimeoutExpired:
                    r, out = 'TIMEOUT', ''
            nsat += r == 'SAT'; nun += r == 'UNSAT'; nto += r == 'TIMEOUT'
            if src == 'rain':
                print('%s p=%d D=%d %s rain(%s): %s (%.0f s)' % (name, p, D, 'phase above' if rev else 'phase below', 'a,~a' if top[0] == A else '~a,a', r, time.time() - t0), flush=True)
            if r == 'SAT':
                model = set(int(x) for line in out.splitlines() if line.startswith('v ') for x in line[2:].split() if int(x) > 0)
                colsw = [sum(1 << t for t in range(p) if V[j][t] in model) for j in range(D + 4)]
                print('   WALL FOUND (%s); columns top to bottom (hex):' % ('phase -> rain' if rev else ('%s -> phase' % src)))
                for c in colsw:
                    print('   %0*x' % (p // 4, c))
                sys.exit(0)
        if src != 'rain':
            print('%s p=%d D=%d from %s (%d top states): UNSAT %d, TIMEOUT %d, SAT %d' % (name, p, D, src, len(tops), nun, nto, nsat), flush=True)
