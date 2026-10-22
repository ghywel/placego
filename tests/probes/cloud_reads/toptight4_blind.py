"""CL527: four-bin co-singleton top-tight instances (CL509; least H(h) slack only at triples, A the complement bin):
blind rules for A's realization (a 3-subset of sum u_A) and whether the three-bin CHILD is feasible (not family
membership).  Rules: lexmax, maxmin (largest minimum), minmax (smallest maximum), lexmin.  Samples: kholek DUMPEVERY.

OUTCOME (CL527): h = 1 (M = 12): 11,706 irreducible; lexmax 11,612, maxmin 11,612, minmax 11,614, lexmin 11,682,
any 11,706 (100%).  h = 2 (M = 13): 13,226; lexmax/maxmin 12,898, minmax 12,948, lexmin 13,213, any 13,225; the one miss
is [0,13] minus {6,7}, (19,19,19,21): three equal targets.
"""
import sys
from itertools import combinations
from collections import Counter

def L(r): return r * (r - 1) // 2

def feasible(pool, sizes, t):
    if not sizes: return True
    for A in combinations(pool, sizes[0]):
        if sum(A) == t[0] and feasible([x for x in pool if x not in A], sizes[1:], t[1:]): return True
    return False

def run(M, h, files, C=(3, 3, 3, 3)):
    cnt = Counter(); ex = []
    for f in files:
        for line in open(f):
            if not line.startswith('V'): continue
            hs, ts = line[len('V holes'):].split('|')
            H = list(map(int, hs.split())); t = list(map(int, ts.split()))
            S = [x for x in range(M + 1) if x not in H]; k = 4
            sig = {J: sum(t[i] for i in J) - L(sum(C[i] for i in J)) - h * sum(C[i] for i in J)
                   for s in range(1, k) for J in combinations(range(k), s)}
            mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
            if any(len(J) <= k - 2 for J in arg): continue
            A = [i for i in range(k) if i not in arg[0]][0]
            oth = [i for i in range(k) if i != A]
            Rs = [R for R in combinations(S, 3) if sum(R) == t[A]]
            picks = {'lexmax': max(Rs), 'maxmin': max(Rs, key=lambda R: (min(R), R)),
                     'minmax': min(Rs, key=lambda R: (max(R), R)), 'lexmin': min(Rs)}
            cnt['n'] += 1; anyok = False
            for name, R in picks.items():
                rest = [x for x in S if x not in R]
                ok = feasible(rest, [C[i] for i in oth], [t[i] for i in oth])
                cnt[name] += ok; anyok |= ok
            cnt['any'] += anyok
            if not anyok and len(ex) < 4: ex.append((H, t, A))
    return cnt, ex

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    cnt, ex = run(M, h, sys.argv[3:])
    print(M, h, dict(cnt), 'no-rule examples:', ex, flush=True)
