#!/usr/bin/env python3
"""L1046: the single seed's full-line pasts, built row by row, and the centre cells they prepend to the column.

Local, 2026-10-27. Exact: every parent row of a row y is fixed by its right ray, and the ray is a periodic point of
the one-period composite of G_b(c, r) = (b XOR (c OR r), c) over y's periodic right tail (GC1984, L1032). The rest
of the parent extends uniquely leftwards. Only cells 0, 1, 2, ... are kept, which is all the centre cell needs.
Every parent is checked against its child on [1, ...). Reproduces the recorded counts 1, 2, 5, 8, ..., 122.
Usage: root_pasts_exact.py DEPTH
"""
import math, sys
def G(b,s): c,r=s; return (b^(c|r), c)
class Row:
    # cells on [0, inf): win = cells 0..R-1, tail = periodic block starting at R
    def __init__(s, win, tail): s.win, s.tail, s.R = list(win), tuple(tail), len(win)
    def at(s,i): return s.win[i] if i < s.R else s.tail[(i-s.R) % len(s.tail)]
def parents(y):
    p, R = len(y.tail), y.R
    yv = lambda i: y.at(i)
    def comp(st):
        for i in range(R+p, R, -1): st = G(yv(i), st)
        return st
    states=[(a,b) for a in (0,1) for b in (0,1)]
    cyc=set()
    for st in states:
        seen=[]; v=st
        while v not in seen: seen.append(v); v=comp(v)
        cyc.update(seen[seen.index(v):])
    out=[]
    for st in cyc:
        c=1; v=comp(st)
        while v!=st: v=comp(v); c+=1
        pred={comp(u):u for u in cyc}
        q=c*p; x={}
        cur=st
        x[R], x[R+1] = st
        # walk forward in position: s_{R+kp} = pred^k(st); fill between by applying G downward
        for k in range(1, c+1):
            top = st
            for _ in range(k): top = pred[top]
            v = top; pos = R + k*p
            x[pos], x[pos+1] = v
            for i in range(pos, pos-p, -1):
                v = G(yv(i), v); x[i-1] = v[0]
        tail = tuple(x[R+j] for j in range(q))
        # left part: x_i = y_{i+1} XOR (x_{i+1} | x_{i+2}) for i = R-1 .. 0
        for i in range(R-1, -1, -1): x[i] = yv(i+1) ^ (x[i+1] | x[i+2])
        row = Row([x[i] for i in range(R)], tail)
        for i in range(1, R + 3*q + 3):   # verify the update on [1, ...)
            assert yv(i) == row.at(i-1) ^ (row.at(i) | row.at(i+1))
        out.append(row)
    return out
D=int(sys.argv[1])
level=[(Row([1],[0]), '')]   # (row, pre-column read from depth n down to depth 1)
for d in range(1, D+1):
    nxt=[]
    for y, pre in level:
        for x in parents(y): nxt.append((x, str(x.at(0)) + pre))
    level=nxt
    pcs={pre for _,pre in level}
    print('depth %2d: pasts %5d   distinct pre-columns %5d of %7d   log2(pasts)/d %.3f   max tail period %d'%(d,len(level),len(pcs),2**d,math.log2(len(level))/d,max(len(r.tail) for r,_ in level)),flush=True)
