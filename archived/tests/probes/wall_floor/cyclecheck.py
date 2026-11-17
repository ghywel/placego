#!/usr/bin/env python3
"""cyclecheck.py (Local, L1546): are the free graph's interior cycles other exact periodic solutions? Lists where the exact period-2 and period-4 solutions with letters AB first leave the lock's strip, with how deep they go, against the offsets of the cycles."""
import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
lock=[l.strip()[::-1] for l in open('cyc45.txt') if l.strip()]   # phase 0 letter A, phase 1 letter B, by offset
def tree(P,WORD,KMAX):
    MASK=(1<<P)-1
    rot=lambda w:((w<<1)|(w>>(P-1)))&MASK
    b=0
    for t in range(P):
        if WORD[t%len(WORD)]=='B': b|=1<<t
    cst=[1,1,0,0,0,1,1,1]
    Y=[MASK if c else 0 for c in cst]+[b^MASK,b,0,b^MASK]
    out=[]
    def rec(K):
        kids=0
        if K<KMAX:
            d=rot(Y[K-5])^Y[K-2]; m=Y[K-1]
            if not (m&~d):
                f=d&~m; sub=m
                while True:
                    Y.append(f|sub); kids+=1; rec(K+1); Y.pop()
                    if sub==0: break
                    sub=(sub-1)&m
        if kids==0: out.append(list(Y))
    rec(12)
    return out
for P,KM in ((2,70),(4,140)):
    L=tree(P,'AB',KM)
    res=defaultdict(lambda:[0,0])
    for Y in L:
        K=len(Y)
        # first offset where any phase leaves the strip
        d=None
        for k in range(min(K,41)):
            for t in range(P):
                ph=t%2     # bit t of the columns: letter AB with t even = A
                c='#' if (Y[k]>>t)&1 else '.'
                if lock[ph][k]!=c:
                    d=(k,ph); break
            if d: break
        if d is None: d=(41,'floor')
        r=res[d]; r[0]+=1; r[1]=max(r[1],K)
    print('period',P,'solutions',len(L),'first departure from the lock strip (offset, phase): count, deepest:',sorted((k,v) for k,v in res.items() if True)[:24])
