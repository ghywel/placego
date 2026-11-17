#!/usr/bin/env python3
"""Smallest anchored rows for short words, in backward order: x carries the last letter, step x the one before, and so on."""
A=[0,0,1,1,1,1,0,0,0,1,1]; B=[0,1,0,1,1,1,0,0,0,1,1]
Wd={'A':A,'B':B}
N=120
def step(x): return (x ^ ((x<<1)|(x<<2))) & ((1<<N)-1)
def rowof(low,n,win):
    x=low
    for i,b in enumerate(win):
        if b: x|=1<<(n+i)
    b=win[-1]
    for j in range(n+11,N):
        b^=1
        if b: x|=1<<j
    return x
def seg(x,p): return [(x>>(p+i))&1 for i in range(11)]
def top(x):
    k=N-4
    while k>=1 and ((x>>k)&1)!=((x>>(k+1))&1): k-=1
    return k
for word in ('AA','AB','BA','ABA','BAB','AAB','BAA'):
    found=None
    for n in range(1,20):
        for low in range(1,1<<n,2):
            x=rowof(low,n,Wd[word[-1]]); ok=True; y=x; p=n
            for s in range(1,len(word)):
                y=step(y); p-=3
                if p<0 or seg(y,p)!=Wd[word[len(word)-1-s]] or top(y)!=p+9: ok=False;break
            if ok and top(x)==n+9: found=(n,low,bin(low)); break
        if found: break
    print(word,'deepest row: low bits',found)
