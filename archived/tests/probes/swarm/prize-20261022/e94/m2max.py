#!/usr/bin/env python3
"""For each n, m2max(n; G) = max over n-subsets S of G of the second-smallest distance multiplicity m2(S).
SAT query (sat132.py, K=1, threshold T): exists S with all but <=1 occurring classes having >= T pairs  <=>  m2max >= T.
Binary search between lo (SAT, witness m2) and hi (UNSAT). hi starts at n+1, which must be UNSAT (checked first).
Usage: m2max.py LAT P NMIN NMAX PER_CALL_TL TOTAL_TL"""
import sys, subprocess, ast, time
lat, P, n0, n1, tl, tot = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
t0 = time.time()
def run(n, T):
    out = subprocess.run(['/usr/bin/python3', 'sat132.py', lat, str(P), str(n), '1', str(tl), str(T)], capture_output=True,
                         text=True).stdout.strip().splitlines()[-1]
    return ast.literal_eval(out)
for n in range(n0, n1 + 1):
    if time.time() - t0 > tot:
        print('# total time limit at n=%d' % n, flush=True); break
    lo, hi, wit, note = 1, None, None, ''
    r = run(n, n + 1)
    if r['status'] == 'SATISFIABLE':
        print({'n': n, 'COUNTEREXAMPLE': r}, flush=True); continue
    if r['status'] != 'UNSATISFIABLE':
        print({'n': n, 'note': 'T=n+1 unknown'}, flush=True); continue
    hi = n + 1
    while hi - lo > 1:
        if time.time() - t0 > tot: note = 'total-timeout'; break
        mid = (lo + hi) // 2
        r = run(n, mid)
        if r['status'] == 'SATISFIABLE':
            lo = max(mid, r['m2']); wit = r
        elif r['status'] == 'UNSATISFIABLE':
            hi = mid
        else:
            note = 'unknown at T=%d' % mid; break
    print({'n': n, 'm2max_lo': lo, 'hi_unsat': hi, 'exact': hi - lo == 1, 'ratio': round(lo / n, 3), 'note': note,
           'S': wit['S'] if wit else None, 'profile': wit['profile'] if wit else None}, flush=True)
