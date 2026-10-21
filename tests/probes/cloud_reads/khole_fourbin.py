"""CL501: four bins 3333 on [0, M] minus h interior holes: the least margin of infeasible spectrum-feasible
instances, split by whether two equal-size bins have equal targets (equal shares).
Data so far: h = 1: non-repeat exceptions only at margin 1 (F(s, M)); h = 2 (M = 13): non-repeat to margin 2,
repeat to margin 4.
Prediction (written first): a ladder.  h = 0 (M = 11): no exceptions at margin >= 1.  h = 3 (M = 14): non-repeat
exceptions reach margin 3 exactly, repeated ones reach margin >= 5.  Counterfactual: non-repeat margin stays at 2
for h = 3 (then the non-repeat threshold does not grow with holes), or jumps past 3.

OUTCOME (CL501, 99 s): h = 0, M = 11: no exceptions (held).  h = 3, M = 14: 7,047,486 spectrum-feasible;
non-repeat exceptions reach margin 8, repeated ones margin 18 (holes 6,7,8, targets 21,21,21,21).  FAILED: the
ladder is 1, 2, 8, not 1, 2, 3.  Split by longest run of adjacent holes (khole_runs.py): isolated holes still give
non-repeat exceptions at margin 5 (holes 5,7,9, targets 10,11,31,32); runs of 2 reach 7; a run of 3 reaches 8.
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/twohole_fourbin.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a

def run_h(M, C, h):
    rep_m = Counter(); nr_m = Counter(); spec = 0; ex = {}
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for Q in itertools.combinations(range(1, M), h):
        pool = [x for x in range(M + 1) if x not in Q]; tot = sum(pool); n = len(pool)
        sp = spectra(pool); F = feasible_set(pool, C)
        mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[n - c:])
        for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
            t = t3 + (tot - sum(t3),)
            tJ = {J: sum(t[i] for i in J) for J in SUB}
            if not all(tJ[J] in sp[CJ[J]] for J in SUB): continue
            spec += 1
            if t3 in F: continue
            m = min(min(tJ[J] - mins(CJ[J]), maxs(CJ[J]) - tJ[J]) for J in SUB)
            rep = any(t[i] == t[j] and C[i] == C[j] for i in range(4) for j in range(i + 1, 4))
            (rep_m if rep else nr_m)[m] += 1
            key = ('rep' if rep else 'nr', m)
            ex.setdefault(key, (Q, tuple(sorted(t))))
    return spec, rep_m, nr_m, ex

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    spec, rep_m, nr_m, ex = run_h(M, (3, 3, 3, 3), h)
    print('M', M, 'holes', h, 'spectrum-feasible', spec)
    print('  non-repeat exceptions by margin', sorted(nr_m.items()))
    print('  repeated exceptions by margin', sorted(rep_m.items()))
    for k in sorted(ex): print('   ', k, ex[k])
    sys.stdout.flush()
