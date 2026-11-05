#!/usr/bin/env python3
"""branches6.py (Local, L1546): the competing strips of the third lock. Along the lock's exact period-6 columns, every other allowed column at each offset, and how deep exact period-6 solutions go down that branch. Compared with where real quiet rows stop agreeing with the lock."""
import sys,time
sys.setrecursionlimit(100000)
rows=[l.strip()[::-1] for l in open('cyc175.txt') if l.strip()]
P=6; MASK=63
K0=len(rows[0])
col=[sum((1<<t) for t in range(P) if rows[t][k]=='#') for k in range(K0)]
rot=lambda w:((w<<1)|(w>>(P-1)))&MASK
# check the columns satisfy the tree relation
bad=0
for K in range(12,160):
    d=rot(col[K-5])^col[K-2]; m=col[K-1]
    if m&~d or (col[K]&~m)!=(d&~m): bad+=1
print('relation fails at',bad,'of the strip columns')
def deep(Y,cap):
    """deepest exact solution from the column list Y"""
    best=[len(Y)]; nodes=[0]
    def rec(K):
        if K>best[0]: best[0]=K
        nodes[0]+=1
        if nodes[0]>cap or K>700: return
        d=rot(Y[K-5])^Y[K-2]; m=Y[K-1]
        if m&~d: return
        f=d&~m; sub=m
        while True:
            Y.append(f|sub); rec(K+1); Y.pop()
            if nodes[0]>cap: return
            if sub==0: break
            sub=(sub-1)&m
    rec(len(Y))
    return best[0],nodes[0]>cap
out=[]
t0=time.time()
for K in range(12,164):
    d=rot(col[K-5])^col[K-2]; m=col[K-1]
    f=d&~m; sub=m; alts=[]
    while True:
        y=f|sub
        if y!=col[K]: alts.append(y)
        if sub==0: break
        sub=(sub-1)&m
    best=0;capped=False
    for y in alts:
        Y=col[:K]+[y]
        dp,c=deep(Y,60000)
        if dp>best: best=dp
        capped=capped or c
    out.append((K,len(alts),best,capped))
    if time.time()-t0>85: print('time limit at',K); break
print('offset: alternatives, deepest (+ if capped), only where an alternative reaches 10 cells deeper:')
print(' '.join(f'{K}:{n},{b}{"+" if c else ""}' for K,n,b,c in out if b>=K+10))
