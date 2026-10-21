"""CL490: classify every gap of depth >= 3 in the k-subset sums of an interval minus <= 3 values (n >= 7).

Normalise by trimming endpoint deletions and translating so the pool is [0, N] minus D (internal), and by
reflection so the gap sits at the LOW end (depth measured from the minimum).  Record the deletion set's offsets
from 0 (all deletions, even far ones), k, and the gap's offset from the minimum.  Prediction (written first): every
depth-3/4 gap has ALL of its relevant deletions within the first 8 values, i.e. the families are finite and
independent of N, and only k = 3 (or n - 3) occurs.  Counterfactual: a depth >= 3 gap with k >= 4 or with a
deletion beyond 8 that matters would make the complement lemma harder.
OUTCOME (N <= 18, 13 s).  Prediction FAILED in form, held in spirit: gaps of depth 3 occur for every k, not just
k = 3, but always in the same four RELATIVE patterns, deletions k + {-2,2,3}, k + {-1,0,4}, k + {-1,1,3},
k + {0,1,2} (low-end normal form, pool starting at 0); depth 4 only for k = 3 with {4,5,6} (and, for larger k,
only at the smallest pool, which is that pattern through complementation k <-> n - k).  Stable in N.
"""
import itertools, sys
from collections import defaultdict

def sig(R, k):
    s = set()
    for c in itertools.combinations(R, k): s.add(sum(c))
    return s

def run(NMAX):
    fam = defaultdict(set)
    for N in range(8, NMAX + 1):
        for d in (1, 2, 3):
            for D in itertools.combinations(range(1, N), d):
                R = [x for x in range(N + 1) if x not in D]; n = len(R)
                if n < 7: continue
                for k in range(3, n - 2):
                    s = sig(R, k); a, b = min(s), max(s)
                    for v in range(a + 3, b - 2):
                        if v in s: continue
                        dl, du = v - a, b - v
                        if dl <= du:   # low-end gap
                            key = (k, dl, tuple(x for x in D if x <= 12))
                        else:          # reflect
                            Dr = tuple(sorted(N - x for x in D)); key = (n - k if False else k, du, tuple(x for x in Dr if x <= 12))
                        fam[key].add(N)
    return fam

if __name__ == '__main__':
    fam = run(int(sys.argv[1]))
    ks = defaultdict(int)
    for (k, dep, D), Ns in sorted(fam.items()):
        ks[k] += 1
        print(f'k={k} depth={dep} low deletions={D} seen at N in [{min(Ns)}, {max(Ns)}] ({len(Ns)} values)')
    print('families by k:', dict(ks))
