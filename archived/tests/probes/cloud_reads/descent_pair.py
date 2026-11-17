"""CL506: CL439's descent on PAIR/TRIPLE facets, five bins -> three.  For a sampled H5(h) instance whose least
margin-adjusted slack is a pair J (bottom-tight pair) or a triple (top-tight complementary pair), delete that pair P by
a realization: a 6-subset R of the pool with sum t_P that splits into the two bins' targets.  The child is the other
three bins on S minus R, re-indexed to its interval, h' = span - size; GOOD if it lies in H3(h') (lower) or its
reflection does (upper).  Also: ANY pair of bins.  Family children are checked for feasibility.

OUTCOME (CL506).  M = 14, h = 0: bottom-tight pair 1,265: lower 100%; top-tight pair (triple facet) 1,411: upper 100%.
M = 15, h = 1: bottom-tight pair 951: lower 100%; top-tight 899: lower 37%, upper 34%, alternation 49%, any other
pair rescues 24.  Two infeasible family children, both h' = 7 (three-bin T(h) cores).  P1 held, P2 failed.
"""
import sys
from collections import Counter
from itertools import combinations
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/descent_alternation.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a

def splits(R, c1, t1):
    return any(sum(B) == t1 for B in combinations(R, c1))

def pair_status(S, C, t, P):
    X, Y = P; m = C[X] + C[Y]; lo_any = up_any = False; bad = []
    for R in combinations(S, m):
        if sum(R) != t[X] + t[Y] or not splits(R, C[X], t[X]): continue
        rest = [x for x in S if x not in R]; a, b = rest[0], rest[-1]; hh = (b - a + 1) - len(rest)
        oth = [i for i in range(len(C)) if i not in P]; sz = [C[i] for i in oth]; tt = [t[i] for i in oth]
        lo = key([u - a * c for u, c in zip(tt, sz)], sz) >= hh; up = key([c * b - u for u, c in zip(tt, sz)], sz) >= hh
        lo_any |= lo; up_any |= up
        if (lo or up) and not feasible(rest, sz, tt): bad.append((tuple(R), hh))
        if lo_any and up_any: break
    return lo_any, up_any, bad

def run_pairs(M, h, files, C=(3, 3, 3, 3, 3)):
    cnt = Counter(); bads = []
    for f in files:
        for line in open(f):
            if not line.startswith('V'): continue
            hs, ts = line[len('V holes'):].split('|')
            H = list(map(int, hs.split())); t = list(map(int, ts.split()))
            S = [x for x in range(M + 1) if x not in H]; k = len(C)
            facets = sorted((sum(t[i] for i in J) - sum(C[i] for i in J) * (sum(C[i] for i in J) - 1) // 2
                             - h * sum(C[i] for i in J), s, J) for s in range(1, k) for J in combinations(range(k), s))
            sl, s, J = facets[0]
            if s not in (2, 3): continue
            P = J if s == 2 else tuple(i for i in range(k) if i not in J)
            tag = 'pair' if s == 2 else 'triple'
            cnt['n_' + tag] += 1
            lo, up, bad = pair_status(S, C, t, P); bads += bad
            cnt['lower_' + tag] += lo; cnt['upper_' + tag] += up; cnt['alt_' + tag] += lo or up
            if not (lo or up):
                anyok = False
                for Q in combinations(range(k), 2):
                    l2, u2, b2 = pair_status(S, C, t, Q); bads += b2
                    if l2 or u2: anyok = True; break
                cnt['anypair_rescue_' + tag] += anyok
    return cnt, bads

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    cnt, bad = run_pairs(M, h, sys.argv[3:])
    print(M, h, dict(sorted(cnt.items())), 'infeasible family children:', len(bad), bad[:3], flush=True)
