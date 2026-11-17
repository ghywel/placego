#!/usr/bin/env python3
"""For each n: rmin(n; G) = min over n-subsets S of G of the number of distances with multiplicity in [1, n].
SAT query (sat132.py with K, T=n+1): exists S with <= K such classes. Increase K from 2 until SAT.
Usage: rmin.py LAT P NMIN NMAX STEP PER_CALL_TL TOTAL_TL"""
import sys, subprocess, ast, time
lat, P, n0, n1, st, tl, tot = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
t0 = time.time()
def run(n, K):
    out = subprocess.run(['/usr/bin/python3', 'sat132.py', lat, str(P), str(n), str(K), str(tl)], capture_output=True,
                         text=True).stdout.strip().splitlines()[-1]
    return ast.literal_eval(out)
for n in range(n0, n1 + 1, st):
    if time.time() - t0 > tot:
        print('# total time limit at n=%d' % n, flush=True); break
    K = 2; res = None; note = ''
    while K <= 60:
        if time.time() - t0 > tot: note = 'total-timeout'; break
        r = run(n, K)
        if r['status'] == 'SATISFIABLE':
            res = r; break
        if r['status'] != 'UNSATISFIABLE':
            note = 'unknown at K=%d' % K; break
        K += 1
    print({'n': n, 'rmin': res['nrare'] if res else None, 'lower_bound': K if not res else res['nrare'], 'note': note,
           'S': res['S'] if res else None, 'profile': res['profile'] if res else None}, flush=True)
