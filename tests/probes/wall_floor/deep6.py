#!/usr/bin/env python3
"""deep6.py (Local, L1534): the deepest exact periodic words below letters WORD at period P that do not pass through a floor. Prints the depth profile and writes the deepest words. Usage: P WORD KMAX CAP OUT"""
import sys
sys.setrecursionlimit(100000)
P=int(sys.argv[1]); WORD=sys.argv[2]; KMAX=int(sys.argv[3]); CAP=int(sys.argv[4]); OUT=sys.argv[5]
MASK=(1<<P)-1
def rotl1(w): return ((w<<1)|(w>>(P-1)))&MASK
b=0
for t in range(P):
    if WORD[t%len(WORD)]=='B': b|=1<<t
cst=[1,1,0,0,0,1,1,1]
Y=[MASK if c else 0 for c in cst]+[b^MASK,b,0,b^MASK]
count={}; nodes=[0]; deep=[0]; keep=[]
def rec(K):
    count[K]=count.get(K,0)+1
    if K>deep[0]:
        deep[0]=K; keep.clear()
    if K==deep[0]: keep.append(list(Y))
    nodes[0]+=1
    if K>=KMAX or nodes[0]>CAP: return
    d=rotl1(Y[K-5])^Y[K-2]; m=Y[K-1]
    if m&~d: return
    f=d&~m; sub=m
    while True:
        Yk=f|sub
        floor=(Yk==MASK and K>7 and Y[K-2]==MASK and Y[K-3]==0 and Y[K-5]==0 and Y[K-6]==MASK and Y[K-1]==(rotl1(Y[K-4])^MASK))
        if not floor:
            Y.append(Yk); rec(K+1); Y.pop()
        if sub==0: break
        sub=(sub-1)&m
rec(12)
print('P',P,WORD,'nodes',nodes[0],'deepest',deep[0],'kept',len(keep))
ks=sorted(count)
print('solutions by offset (every 20):',' '.join(f'{k}:{count[k]}' for k in ks if k%20==0))
with open(OUT,'w') as f:
    for L in keep[:64]:
        K=len(L)
        for ph in range(P):
            f.write(''.join('#' if (L[K-1-i]>>ph)&1 else '.' for i in range(K))+'\n')
