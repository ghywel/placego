"""CL501: are the two-hole four-bin exceptions at least margin 2 also all equal-shares (a repeated (size, target))?
If so, the candidate two-hole statement is: margin >= 2 and no repeated (size, target) => feasible.
Prediction (written first): no; some margin-2 exceptions are one-hole-style cores without repetition.
Counterfactual: all repeated => the clean statement holds at M = 13-14.

OUTCOME (CL501): held.  M = 13: 408 margin-2 exceptions, 240 without repeat (holes (2,8), (2,11), (4,9), (5,11));
M = 14 3334: 312, 216 without repeat.  Example holes (2,8), targets 6, 15, 26, 34: 6 forces {0,1,5}, after which
every 15 needs 2, 5 or 8.  So two holes: non-repeat exceptions at margin <= 2, repeated ones to margin 4.
"""
import sys
from collections import Counter
sys.argv = ['x']
exec(open('tests/probes/cloud_reads/twohole_fourbin.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
for M, C in ((13, (3, 3, 3, 3)), (14, (3, 3, 3, 4))):
    cnt, exc = run(M, C)
    for mm in (2,):
        e = [(h, t, m) for h, t, m in exc if m == mm]
        nr = [(h, t) for h, t, m in e if not any(t[i] == t[j] and C[i] == C[j] for i in range(4) for j in range(i + 1, 4))]
        print(M, C, 'margin', mm, 'exceptions', len(e), 'without repeat', len(nr))
        print('   by holes:', sorted(Counter(h for h, t in nr).items()))
        seen = set()
        for h, t in nr:
            k = (h, tuple(sorted(zip(C, t))))
            if k in seen: continue
            seen.add(k)
            if len(seen) <= 12: print('   ', h, sorted(zip(C, t)))
    sys.stdout.flush()
