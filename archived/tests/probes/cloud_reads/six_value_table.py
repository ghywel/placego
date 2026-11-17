"""CL492: the finite table of six-value pools (span <= 8, endpoints present, <= 3 internal deletions) and their
missing triple sums, for lemma (a)'s small-complement case (CL491).  Translation-invariant; reflection pairs noted.
Prediction (written first): 1 + 7 + 21 + 35 = 64 pools; the deep (central) gaps occur only in the three known
cores {0,2,3,5,6,8}, {0,1,3,4,5,9}-type (span 9 is excluded here), {0,1,2,6,7,8}, i.e. a handful of rows.
OUTCOME: 56 pools (prediction's 64 was an arithmetic slip: 1 + 5 + 15 + 35 = 56).  Seven have a gap of depth >= 3,
five classes up to reflection: {0,2,3,5,6,8} (12), {0,1,3,5,7,8} (7, 17), {0,1,2,6,7,8} (6, 12, 18), and the pairs
{0,2,3,4,7,8} <-> {0,1,4,5,6,8} (8, 16), {0,1,5,6,7,8} <-> {0,1,2,3,7,8} (10, 17 / 7, 14).  All other pools miss
only sums within 2 of an end.
"""
import itertools
rows = []
for N in range(5, 9):
    inner = list(range(1, N))
    d = N + 1 - 6
    for D in itertools.combinations(inner, d):
        W = [v for v in range(N + 1) if v not in D]
        s = {sum(c) for c in itertools.combinations(W, 3)}; a, b = min(s), max(s)
        miss = [v for v in range(a, b + 1) if v not in s]
        deep = [v for v in miss if min(v - a, b - v) >= 3]
        rows.append((tuple(W), a, b, miss, deep))
print(len(rows), 'six-value pools')
for W, a, b, miss, deep in rows:
    if miss: print(W, 'alpha,beta', a, b, 'missing', miss, 'deep', deep)
print('pools with a deep (depth >= 3) gap:', [r[0] for r in rows if r[4]])
