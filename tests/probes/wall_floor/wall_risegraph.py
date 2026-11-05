#!/usr/bin/env python3
"""wall_risegraph.py (Local, L1552): the rise rule of genealogy 64.5b as a graph on (phase, D) along the third lock's strip. Forward tick: (p, D) -> (p-1, D-r), r allowed by the strip's cells at D in phase p.
A climb in backward time walks it in reverse. Prints, for each node, its reverse edges, and how deep a climb from it can go with no retreat. Then the witness's actual route."""
import json,sys
rows=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]   # by offset, top first; backward-tick order
P=len(rows); N=min(len(r) for r in rows)
print('phases',P,'length',N,'first ? by phase',[r.find('?') for r in rows])
x=lambda p,k: rows[p][k]=='#'
known=lambda p,k: 0<=k<N and rows[p][k]!='?'
def options(p,D):
    if not all(known(p,k) for k in (D-1,D,D+1,D+2)): return None
    if not x(p,D-1): return [5],False
    if not x(p,D):
        if not x(p,D+1): return [4],False
        return [3],True
    if x(p,D+1) or x(p,D+2): return [4,3],False
    return [4],True
LO,HI=100,170
rev={}   # (q,Dp) -> list of (q+1,D)
unk={}
for q in range(P):
    for Dp in range(10,HI):
        e=[];u=False
        for D in range(Dp+3,Dp+6):
            o=options((q+1)%P,D)
            if o is None: u=True; continue
            if D-Dp in o[0]: e.append(((q+1)%P,D))
        rev[(q,Dp)]=e; unk[(q,Dp)]=u
memo={}
def deepest(n):
    if n in memo: return memo[n]
    memo[n]=n[1]
    best=n[1]; top=False
    for m in rev.get(n,[]):
        b,t=deepest(m)
        if b>best: best=b
        top=top or t
    if unk.get(n): top=True
    memo[n]=(best,top)
    return memo[n]
for n in list(rev): 
    memo.pop(n,None)
import functools
sys.setrecursionlimit(10000)
memo={}
def deep(n):
    if n in memo: return memo[n]
    best=n[1]; open_=bool(unk.get(n))
    for m in rev.get(n,[]):
        b,o=deep(m)
        best=max(best,b); open_=open_ or o
    memo[n]=(best,open_)
    return memo[n]
print('node map: per phase, for D, the deepest D a climb from (p,D) reaches with no retreat; + means it runs into unknown cells')
for p in range(P):
    print('phase',p,' '.join(f'{D}:{deep((p,D))[0]}{"+" if deep((p,D))[1] else ""}' for D in range(LO,160)))
print('dead ends (no reverse edge, all cells known), D from 100:')
for p in range(P):
    print(' phase',p,[D for D in range(LO,160) if not rev[(p,D)] and not unk[(p,D)]])
json.dump({f'{p},{D}':[list(m) for m in rev[(p,D)]] for (p,D) in rev},open('risegraph.json','w'))
