#!/usr/bin/env python3
"""reachlib.py (Local, L1532): words as ints, bit i = cell i of the word, low to high, top two cells the wall pair."""
import random
from locklib import inv,top,W
WAi=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1)))
WBi=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
M11=(1<<11)-1
def let(x,n):
    t=(x>>(n-11))&M11
    return 'A' if t==WAi else 'B' if t==WBi else '?'
STATES=((0,0),(0,1),(1,0),(1,1))
def step(x,n,s):
    """one backward tick at fixed low end: returns new word of length n+3; s=(p1,p2) the two output cells below the word"""
    p1,p2=s; out=0
    for j in range(n):
        o=((x>>j)&1)^(p1|p2); out|=o<<j; p2=p1; p1=o
    b=1
    for j in range(n,n+3):
        b^=1; o=b^(p1|p2); out|=o<<j; p2=p1; p1=o
    return out
def win(r,w,d=None):
    """top w cells of row r ending at the wall pair, as an int"""
    d=top(r) if d is None else d
    lo=d+2-w
    return (r>>lo)&((1<<w)-1)
def fresh(seed,low=40):
    random.seed(seed)
    x=1|(random.getrandbits(low-1)<<1); b=(x>>(low-1))&1
    for j in range(low,W):
        b^=1
        if b: x|=1<<j
    return x
def show(x,n): return ''.join('#' if (x>>i)&1 else '.' for i in range(n))
def forced(x,n,T,cap=300000):
    """How many next letters are forced for every lower state on every tick, up to T. Fixed low end, state free on each tick (an over-count of what real rows can do, so a forced letter is truly forced)."""
    S={x}; m=n; word=''
    for t in range(1,T+1):
        N=set()
        for y in S:
            for s in STATES: N.add(step(y,m,s))
        m+=3
        L={let(y,m) for y in N}
        if len(L)>1 or '?' in L: return t-1,word,L
        word+=next(iter(L)); S=N
        if len(S)>cap: return t,word,'cap'
    return T,word,None
