#!/usr/bin/env python3
"""L1307 T29 (Local, 2026-11-02): one (MODE, P, M, S) instance of phase_sat.py through Kissat, with a time limit.
Run: python3 tests/probes/phase_sat_one.py MODE P M S LIMIT_S [CNF_OUT]   (e.g. neg 32 30 14 900)
With CNF_OUT the DIMACS file is also written there, for an LRAT run (CaDiCaL, then cake_lpr) on an UNSAT answer.
"""
import os, subprocess, sys, tempfile, time
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'phase_sat.py')).read().split("if __name__ == '__main__':")[0])
mode, p, m, s, lim = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
M_, integ, val, rot, canon, lp = tools(p)
e = Enc(p, m, s, mode); t0 = time.time()
if len(sys.argv) > 6:
    with open(sys.argv[6], 'w') as f:
        f.write('p cnf %d %d\n' % (e.nv, len(e.cl)))
        for c in e.cl: f.write(' '.join(map(str, c)) + ' 0\n')
with tempfile.TemporaryDirectory() as td:
    fn = os.path.join(td, 'i.cnf')
    with open(fn, 'w') as f:
        f.write('p cnf %d %d\n' % (e.nv, len(e.cl)))
        for c in e.cl: f.write(' '.join(map(str, c)) + ' 0\n')
    try:
        out = subprocess.run(['kissat', '-q', fn], capture_output=True, text=True, timeout=lim).stdout
        res = 'SAT' if '\ns SATISFIABLE' in '\n' + out else ('UNSAT' if 'UNSATISFIABLE' in out else 'TIMEOUT')
    except subprocess.TimeoutExpired:
        res, out = 'TIMEOUT', ''
print('%s p=%d m=%d s=%d: %s in %.0f s' % (mode, p, m, s, res, time.time() - t0), flush=True)
if res == 'SAT':
    model = [int(x) for line in out.splitlines() if line.startswith('v ') for x in line[2:].split()]
    cols = e.decode([l for l in model if l != 0])
    print('   valuations %s, least periods %s, %d column classes' % (sorted(set(val(c) for c in cols)), sorted(set(lp(c) for c in cols)), len(set(canon(c) for c in cols))))
