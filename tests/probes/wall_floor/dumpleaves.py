#!/usr/bin/env python3
"""dumpleaves.py: the leaves of the exact periodic tree at width >= KMIN, as cell words. Usage: P WORD KMAX KMIN"""
import sys
P=int(sys.argv[1]); WORD=sys.argv[2]; KMAX=int(sys.argv[3]); KMIN=int(sys.argv[4])
MASK=(1<<P)-1
def rotl1(w): return ((w<<1)|(w>>(P-1)))&MASK
b=0
for t in range(P):
    if WORD[t%len(WORD)]=='B': b|=1<<t
cst=[1,1,0,0,0,1,1,1]
Y=[MASK if c else 0 for c in cst]+[b^MASK,b,0,b^MASK]
out=[]
def rec(K):
    if K>=KMAX: out.append(list(Y)); return
    d=rotl1(Y[K-5])^Y[K-2]; m=Y[K-1]
    if m&~d: out.append(list(Y)); return
    f=d&~m; sub=m
    while True:
        Y.append(f|sub); rec(K+1); Y.pop()
        if sub==0: break
        sub=(sub-1)&m
rec(12)
seen=set()
for L in out:
    K=len(L)
    if K<KMIN: continue
    for ph in range(P):
        s=''.join('#' if (L[K-1-i]>>ph)&1 else '.' for i in range(K))
        if s in seen: continue
        seen.add(s); print(s)
