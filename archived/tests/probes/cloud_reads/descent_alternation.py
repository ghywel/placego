"""CL505: CL439's descent step, five bins -> four, with CL443's untested ALTERNATION (lower or reflected family).
Input: H5(h) feasible instances sampled by kholek.c (DUMPEVERY).  For an instance on S = [0, M] minus H, sizes C,
targets t: delete one bin A by a realization R (|R| = c_A, sum t_A); the child is S minus R with the other four bins,
re-indexed to its own interval [a, b], with h' = (b - a + 1) - |child| holes.  The child is GOOD if it lies in H4(h')
(lower: u_J >= L(r) + h' r) or its reflection x -> b - x does (upper).  The least-slack facet is argmin over proper
groups J of u_J - L(r) - h r; a singleton {A} is bottom-tight, a four-group is top-tight for its complement A.
Measured: ANY (some bin, some realization), SEL (the facet's bin), each lower-only and with alternation; children in
the family are also checked for feasibility (an infeasible family child would be an H4 exception).

OUTCOME (CL505).  M = 14, h = 0 (15,067 sampled H5 instances, 33333): least facet single 6,985 / top 5,406 /
pair-triple 2,676.  Single: lower child 100%.  Top: lower 64%, upper 100%, alternation 100%.  ANY bin 86.6% (the rest
are pair/triple-facet instances).  M = 15, h = 1 (16,072): single 5,448, lower 100%.  Top 8,774: lower 41%, upper 32%,
alternation 55%.  ANY 73%.  No family child was infeasible.  P1 failed, P2 roughly held (64%, 41%), P3 held at h = 0
and failed at h = 1.
"""
import sys, itertools
from collections import Counter
from itertools import combinations

def key(targets, sizes):
    k = len(sizes); mu = 10 ** 9
    for s in range(1, k):
        for J in combinations(range(k), s):
            r = sum(sizes[i] for i in J); u = sum(targets[i] for i in J)
            mu = min(mu, (u - r * (r - 1) // 2) // r if u >= r * (r - 1) // 2 else -1)
    return mu

def feasible(pool, sizes, t):
    if not sizes: return True
    for A in combinations(pool, sizes[0]):
        if sum(A) == t[0]:
            rest = [x for x in pool if x not in A]
            if feasible(rest, sizes[1:], t[1:]): return True
    return False

def child_status(S, C, t, A, R):
    rest = [x for x in S if x not in R]; a, b = rest[0], rest[-1]
    hh = (b - a + 1) - len(rest)
    sz = [C[i] for i in range(len(C)) if i != A]; tt = [t[i] for i in range(len(C)) if i != A]
    low = [u - a * c for u, c in zip(tt, sz)]
    up = [c * b - u for u, c in zip(tt, sz)]
    lo_ok = key(low, sz) >= hh; up_ok = key(up, sz) >= hh
    return lo_ok, up_ok, rest, sz, tt, hh

def run(M, h, files, C=(3, 3, 3, 3, 3)):
    cnt = Counter(); bad_family = []
    for f in files:
        for line in open(f):
            if not line.startswith('V'): continue
            hs, ts = line[len('V holes'):].split('|')
            H = list(map(int, hs.split())); t = list(map(int, ts.split()))
            S = [x for x in range(M + 1) if x not in H]; k = len(C)
            facets = []
            for s in range(1, k):
                for J in combinations(range(k), s):
                    r = sum(C[i] for i in J); facets.append((sum(t[i] for i in J) - r * (r - 1) // 2 - h * r, s, J))
            facets.sort(); sl, s, J = facets[0]
            ftype = 'single' if s == 1 else ('top' if s == k - 1 else 'pair/triple')
            if ftype == 'single': selA = J[0]
            elif ftype == 'top': selA = [i for i in range(k) if i not in J][0]
            else: selA = None
            cnt['n'] += 1; cnt['type_' + ftype] += 1
            res = {}
            for A in range(k):
                lo_any = up_any = False
                for R in combinations(S, C[A]):
                    if sum(R) != t[A]: continue
                    lo_ok, up_ok, rest, sz, tt, hh = child_status(S, C, t, A, R)
                    lo_any |= lo_ok; up_any |= up_ok
                    if (lo_ok or up_ok) and not feasible(rest, sz, tt):
                        bad_family.append((H, t, A, R, hh))
                res[A] = (lo_any, up_any)
            cnt['ANY_lower'] += any(v[0] for v in res.values())
            cnt['ANY_alt'] += any(v[0] or v[1] for v in res.values())
            if selA is not None:
                cnt['SEL_' + ftype] += 1
                cnt['SEL_lower_' + ftype] += res[selA][0]
                cnt['SEL_alt_' + ftype] += res[selA][0] or res[selA][1]
                if ftype == 'single': cnt['SEL_upper_' + ftype] += res[selA][1]
                if ftype == 'top': cnt['SEL_upper_' + ftype] += res[selA][1]
    return cnt, bad_family

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    cnt, bad = run(M, h, sys.argv[3:])
    print(M, h, dict(sorted(cnt.items())))
    print('family children that are infeasible:', len(bad), bad[:5], flush=True)
