#!/usr/bin/env python3
"""fairzone.py (Local, L1544): the hand fact: at row s, cells at offsets K-3s and deeper are fair and independent of the window. Agreement of those cells with the strip row, on random rows in the third lock."""
import random
L=[l.strip() for l in open('lock175.txt') if l.strip()]
cyc=[l.strip()[::-1] for l in open('cyc175.txt') if l.strip()]
K=175
random.seed(9)
N=20000
res={}
for it in range(N):
    w=random.choice(L)
    y=[1 if c=='#' else 0 for c in w[::-1]]+[random.getrandbits(1) for _ in range(5*30+20)]
    for s in range(1,31):
        y=[y[k+3]^(y[k+4]|y[k+5]) for k in range(len(y)-5)]
        if s%5==0:
            B=K-3*s
            res.setdefault(s,[0,0,0])
            res[s][0]+=y[B]; res[s][1]+=y[B+1]; res[s][2]+=y[B]^y[B+2]
print('row s: mean of cell at K-3s, at K-3s+1, xor of K-3s and K-3s+2, each should be 0.5 (from',N,'rows):')
for s,v in res.items(): print(s,[round(a/N,3) for a in v])
