"""Exact feasible target sets for the one-hole four-bin problem (CL478 data).

For (M, q, c) with sizes >= 3, enumerate every partition of [0, M] minus q and record the sum vector.
Writes a compact file per (M, c): feasible sum vectors by q.  Used to examine which cut-feasible
instances are infeasible and what invariant excludes them.

OUTCOME (with scratch gap2.py / exceptions.py), sizes >= 3, M = 12..16, all q, 12 size patterns:
9,124,490 instances with all 14 group targets in their scalar spectra; 44 infeasible, every one at least
margin exactly 1, all in ONE family up to relabelling and reflection (s >= 2, M >= s + 10, hole q = s + 4):
a bin of size s+1 pinned to [0,s-1] u {s+1}, a bin of size M-s-7 pinned to {s+7} u [s+9,M], and two
size-3 bins wanting 12+3s each on the core {s,s+2,s+3,s+5,s+6,s+8}.  Seen: s=2 at M=12..16, s=3 at
M=14..16, s=4 at M=16.  No infeasible instance at margin 0 or at margin >= 2.
M = 17 (six size patterns, ~10 min each in the background): 9,557,938 spectrum-feasible, 10 infeasible, all in
F(s, 17) with s = 2, 3, 4 and their reflections s = 7, 6, 5 (reflection maps F(s, M) to F(M - s - 8, M)).
Running total M = 12..17: 18,682,428 spectrum-feasible instances, 54 infeasible, one family.
"""
import itertools, sys, pickle, os, tempfile
# scratch data folder: $SCRATCH, else the system temp folder (was a session path; made portable 2026-10-22)
SCRATCH = os.environ.get('SCRATCH', tempfile.gettempdir())

def feasible_set(M, q, C):
    pool = [x for x in range(M + 1) if x != q]
    out = set()
    a, b, c, d = C
    for A in itertools.combinations(pool, a):
        sA = sum(A); r1 = [x for x in pool if x not in A]
        for B in itertools.combinations(r1, b):
            sB = sum(B); r2 = [x for x in r1 if x not in B]
            for Cc in itertools.combinations(r2, c):
                out.add((sA, sB, sum(Cc)))
    return out

if __name__ == '__main__':
    M = int(sys.argv[1]); C = tuple(map(int, sys.argv[2].split(',')))
    assert sum(C) == M
    res = {q: feasible_set(M, q, C) for q in range(1, M)}
    os.makedirs(os.path.join(SCRATCH, 'feas'), exist_ok=True)
    with open(os.path.join(SCRATCH, 'feas', f'F_{M}_{"".join(map(str,C))}.pkl'), 'wb') as f:
        pickle.dump(res, f)
    print(M, C, {q: len(v) for q, v in res.items()})
