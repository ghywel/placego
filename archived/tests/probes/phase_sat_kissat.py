#!/usr/bin/env python3
"""L1307 T29 (Local, 2026-11-02): driver running phase_sat.py's encodings through the Kissat command line.
reports/rule30-genealogy.md section 34. Run: python3 tests/probes/phase_sat_kissat.py MODE P MMIN MMAX PER_INSTANCE_S
For each depth period m in [MMIN, MMAX] and each twist s in Z/P, writes the CNF to a temporary file, runs
`kissat -q` with a per-instance time limit, and reports SAT / UNSAT / TIMEOUT. A SAT model is decoded into its columns,
with their valuations and least periods. UNSAT is Kissat-reported, not LRAT-certified.
"""
import os
import subprocess
import sys
import tempfile
import time
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'phase_sat.py')).read().split("if __name__ == '__main__':")[0])
mode, p, mmin, mmax, lim = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
M_, integ, val, rot, canon, lp = tools(p)
tally = {'SAT': 0, 'UNSAT': 0, 'TIMEOUT': 0}; t0 = time.time(); undecided = []
with tempfile.TemporaryDirectory() as td:
    for m in range(mmin, mmax + 1):
        for s in range(p):
            e = Enc(p, m, s, mode); fn = os.path.join(td, 'i.cnf')
            with open(fn, 'w') as f:
                f.write('p cnf %d %d\n' % (e.nv, len(e.cl)))
                for c in e.cl:
                    f.write(' '.join(map(str, c)) + ' 0\n')
            try:
                r = subprocess.run(['kissat', '-q', fn], capture_output=True, text=True, timeout=lim)
                out = r.stdout
                res = 'SAT' if '\ns SATISFIABLE' in '\n' + out else ('UNSAT' if 'UNSATISFIABLE' in out else 'TIMEOUT')
            except subprocess.TimeoutExpired:
                res = 'TIMEOUT'
            tally[res] += 1
            if res == 'TIMEOUT':
                undecided.append((m, s))
            if res == 'SAT':
                model = [int(x) for line in out.splitlines() if line.startswith('v ') for x in line[2:].split()]
                cols = e.decode([l for l in model if l != 0])
                print('SAT m=%d s=%d: valuations %s, least periods %s, %d column classes' % (
                    m, s, sorted(set(val(c) for c in cols)), sorted(set(lp(c) for c in cols)),
                    len(set(canon(c) for c in cols))), flush=True)
        print('m=%d done: %s, elapsed %.0f s' % (m, tally, time.time() - t0), flush=True)
print('%s p=%d m=%d..%d: %s; undecided (m, s): %s' % (mode, p, mmin, mmax, tally, undecided[:40]))
