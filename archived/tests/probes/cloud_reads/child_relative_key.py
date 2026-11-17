"""CL539: lexmin's three-bin child (CL536) measured in a RELATIVE margin: for the child's own pool S, rho_J = u_J -
lo_{r_J}(S) with lo_r the sum of the r smallest values, key = min over proper groups J of floor(rho_J / r_J).
Compared with the largest key among INFEASIBLE (3, 3, X) vectors on any pool of the child's shape (same M, h + 3
holes).  If the children sit strictly above that failure line, the child lands in a pool-relative family whose truth
is a three-bin statement.  Run: python3 child_relative_key.py [M,h,X ...].

OUTCOME (CL539): COLD.  Children keys (13,1,4): 0:3222, 1:8629, 2:322; (15,1,6): 0:8476, 1:19269, 2:2054.  Failure line
(4 holes): (13,*,4) keys 0..2; (15,*,6) keys 0..1.  Key >= 1 failures are mostly SPECTRAL GAPS (u = 11 not a triple sum
when 0, 2, 6, 7 are missing); with every group's spectrum required, failures at key >= 1 are still 201 (X = 4, up to key
2) and 19 (X = 6, key 1).  So 93% of children sit at or below the spectral failure line: a pool-relative margin family
is not the closure for lexmin's descent.
"""
import sys
from itertools import combinations
from collections import Counter
_argv_sl = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/small_toptight_census.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv_sl

def rkey(pool, sizes, t):
    p = sorted(pool); k = len(sizes); best = 1 << 30
    for s in range(1, k):
        for J in combinations(range(k), s):
            r = sum(sizes[i] for i in J); u = sum(t[i] for i in J)
            best = min(best, (u - sum(p[:r])) // r)
    return best

def children(M, h, X):
    C = (3, 3, 3, X); keys = Counter(); shapes = set()
    groups = [J for s in (1, 2, 3) for J in combinations(range(4), s)]
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        trip = {}
        for T in combinations(S, 3): trip.setdefault(sum(T), []).append(T)
        for u1 in range(3 + 3 * h, 3 * M):
            for u2 in range(u1, 3 * M):
                for u3 in range(u2, 3 * M):
                    t = (u1, u2, u3, tot - u1 - u2 - u3); sig = {}; bad = False
                    for J in groups:
                        r = sum(C[i] for i in J); u = sum(t[i] for i in J); s_ = u - L(r) - h * r
                        if s_ < 0: bad = True; break
                        sig[J] = s_
                    if bad: continue
                    mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
                    if any(len(J) <= 2 for J in arg): continue
                    tops = {[i for i in range(4) if i not in J][0] for J in arg}
                    if tops == {3}: continue
                    A = min(i for i in tops if i < 3); oth = [i for i in range(4) if i != A]
                    R = min(trip[t[A]]); rest = [x for x in S if x not in R]
                    keys[rkey(rest, [C[i] for i in oth], [t[i] for i in oth])] += 1
    return keys

def fail_line(M, nh, X):
    """largest relative key among infeasible (3, 3, X) vectors, pools [0, M] minus nh holes; plus the key histogram."""
    hist = Counter()
    for H in combinations(range(M + 1), nh):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        ach = set()
        for A in combinations(S, 3):
            rest = [x for x in S if x not in A]; a = sum(A)
            for B in combinations(rest, 3): ach.add((a, sum(B)))
        lo = sum(sorted(S)[:3]); hi = sum(sorted(S)[-3:])
        for u1 in range(lo, hi + 1):
            for u2 in range(u1, hi + 1):
                if (u1, u2) in ach: continue
                key = rkey(S, (3, 3, X), (u1, u2, tot - u1 - u2))
                if key >= 0: hist[key] += 1
    return hist

if __name__ == '__main__':
    doms = [tuple(map(int, a.split(','))) for a in sys.argv[1:]] or [(13, 1, 4), (15, 1, 6)]
    for M, h, X in doms:
        print('M', M, 'h', h, 'X', X, 'child keys', sorted(children(M, h, X).items()), flush=True)
        print('   fail line (h+3 holes)', sorted(fail_line(M, h + 3, X).items()), flush=True)
