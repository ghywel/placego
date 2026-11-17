#!/usr/bin/env python3
"""lockperiodic.py (Local, L1532): every exact solution of period P below letters WORD, by columns as in wall_periodic.c. A lock contains a cycle of windows, so it contains such a solution at its width.
Forcing is monotone in width, so only the leaves of the tree (or the nodes at KMAX) need testing: a window whose letters are forced for all lower cells for T ticks. Prints the best forced depth by width."""
import sys,time
from reachlib import *
from obdd import *
from reach3 import forcedT
P=int(sys.argv[1]); WORD=sys.argv[2]; KMAX=int(sys.argv[3]); TT=int(sys.argv[4]); CAP=int(sys.argv[5]) if len(sys.argv)>5 else 256
MASK=(1<<P)-1
def rotl1(w): return ((w<<1)|(w>>(P-1)))&MASK
b=0
for t in range(P):
    if WORD[t%len(WORD)]=='B': b|=1<<t
cst=[1,1,0,0,0,1,1,1]
Y=[MASK if c else 0 for c in cst]+[b^MASK,b,0,b^MASK]
leaves=[]; count={}
def rec(K):
    count[K]=count.get(K,0)+1
    if K>=KMAX:
        leaves.append(list(Y)); return
    d=rotl1(Y[K-5])^Y[K-2]; m=Y[K-1]
    if m&~d:
        leaves.append(list(Y)); return
    forced_=d&~m
    sub=m; kids=0
    while True:
        Y.append(forced_|sub); n0=len(leaves); rec(K+1); Y.pop(); kids+=1
        if sub==0: break
        sub=(sub-1)&m
rec(12)
print('P',P,WORD,'leaves',len(leaves),'deepest',max(count),flush=True)
best={}
t0=time.time()
res=[]
for L in leaves:
    K=len(L)
    # the phase-0 row: cell at offset k is bit 0 of Y_k; word low..high = offsets K-1..0
    for ph in range(1):
        x=0
        for i in range(K):
            k=K-1-i
            if (L[k]>>ph)&1: x|=1<<i
        f,word,why,n=forcedT(x,K,TT,CAP)
        res.append((f,K,x,word))
        if f>best.get(K,-1): best[K]=f
res.sort(key=lambda r:(-r[0],r[1]))
print('time',round(time.time()-t0,1))
print('best forced depth by leaf width:',' '.join(f'{k}:{best[k]}' for k in sorted(best)))
for f,K,x,word in res[:6]:
    print('forced',f,'width',K,show(x,K),word[:60])
print('leaves with depth >=',TT,':',sum(1 for r in res if r[0]>=TT))
