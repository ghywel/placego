#!/usr/bin/env python3
"""Is the AB phase locked? Find rows that sit in AB, then the closure of their top windows under every pair of lower bits, and whether the letters are forced."""
import random,sys
W=3200
def inv(y):
    x=y&1; p1=1; p2=0
    for j in range(1,W):
        o=((y>>j)&1)^(p1|p2); x|=o<<j; p2=p1; p1=o
    return x
def top(x):
    e=(~(x^(x>>1)))&((1<<(W-2))-1)&~1
    return e.bit_length()-1
WA=(0,0,1,1,1,1,0,0,0,1,1); WB=(0,1,0,1,1,1,0,0,0,1,1)
def window(r,w,d=None):
    d=top(r) if d is None else d
    return tuple((r>>(d+1-(w-1)+i))&1 for i in range(w))
def letter(win):
    t=win[-11:]
    return 'A' if t==WA else 'B' if t==WB else '?'
def back(win,s):
    inp=list(win); b=inp[-1]
    for i in range(16):
        b^=1; inp.append(b)
    p1,p2=s; out=[p2,p1]
    for bit in inp:
        o=bit^(p1|p2); out.append(o); p2=p1; p1=o
    k=len(out)-2
    while k>=0 and out[k]!=out[k+1]: k-=1
    return k-2-(len(win)-2),out,k
def closure(start,w,cap=20000):
    g={s:set() for s in start}; st=list(start)
    while st:
        win=st.pop()
        for s in ((0,0),(0,1),(1,0),(1,1)):
            d,out,k=back(win,s)
            if d!=3: return None
            nw=tuple(out[k+2-w:k+2]); g[win].add(nw)
            if nw not in g:
                g[nw]=set(); st.append(nw)
                if len(g)>cap: return 'big'
    return g
