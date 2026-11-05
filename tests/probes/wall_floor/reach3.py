#!/usr/bin/env python3
"""Forced letters with an adaptive low end: after each tick, forget low cells until the diagram is narrow. Forgetting only adds rows, so a letter forced here is truly forced."""
import sys,time
from reachlib import *
from obdd import *
def letters(S):
    r=suffixes(S,S.n-11)
    return {('A' if v==WAi else 'B' if v==WBi else '?') for v in r}
def narrow(S,cap):
    k=0
    ws=[len(l) for l in S.lv]
    # highest level whose width exceeds cap
    hi=-1
    for i,wd in enumerate(ws):
        if wd>cap: hi=i
    if hi>=0: return lift(S,hi+1)
    return S
def forcedT(x,n,T,cap=256):
    S=from_word(x,n); word=''
    for t in range(1,T+1):
        S=tick(S)
        L=letters(S)
        if len(L)>1 or '?' in L: return t-1,word,L,S.n
        word+=next(iter(L))
        S=narrow(S,cap)
    return T,word,None,S.n
if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 5
    cap=int(sys.argv[2]) if len(sys.argv)>2 else 256
    y=fresh(seed)
    for t in range(600): y=inv(y)
    t0=time.time()
    for t in range(6):
        d=top(y); l=let(win(y,11,d),11)
        res=[]
        for w in (20,24,28,32,36,40,44,48,56,64,80,96,128,160,200):
            f,word,why,n=forcedT(win(y,w,d),w,200,cap)
            res.append(f'{w}:{f}')
        print(t,l,' '.join(res),f'{time.time()-t0:.1f}s',flush=True)
        y=inv(y)
