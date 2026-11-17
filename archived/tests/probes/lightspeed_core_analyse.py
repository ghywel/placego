#!/usr/bin/env python3
"""L1294 T20 (Local, 2026-11-02): analyse the bi-infinite core printed by lightspeed_core.c.
Run: python3 tests/probes/lightspeed_core_analyse.py tests/probes/lightspeed_core16.out 16
Tarjan on the core; classify cyclic components (white, rain, other, with state periods); group the acyclic core states
by the components they come from and go to (walls); describe the largest component (out-degrees, depth period, the
time shifts that equal depth shifts, and its ring at time 0).
"""
import sys
from collections import defaultdict
p=int(sys.argv[2]); M=(1<<p)-1; A=sum(1<<t for t in range(1,p,2))
pc=lambda x: bin(x).count('1')
def integ(d):
    y,s=d,1
    while s<p:
        y^=(y<<s)&M; s<<=1
    return (y<<1)&M
core=set()
for line in open(sys.argv[1]):
    if '(u, v)' in line:
        a=line.split('(u, v) = (')[1].split(')')[0].split(', ')
        core.add((int(a[0],16),int(a[1],16)))
succ={s:[t for t in ((s[1],integ(s[0]|s[1])),(s[1],integ(s[0]|s[1])^M)) if t in core] for s in core}
# Tarjan
idx={};low={};on=set();st=[];comps=[];c=[0]
sys.setrecursionlimit(100000)
def sc(v):
    idx[v]=low[v]=c[0];c[0]+=1;st.append(v);on.add(v)
    for w in succ[v]:
        if w not in idx: sc(w);low[v]=min(low[v],low[w])
        elif w in on: low[v]=min(low[v],idx[w])
    if low[v]==idx[v]:
        comp=[]
        while True:
            w=st.pop();on.discard(w);comp.append(w)
            if w==v:break
        comps.append(comp)
for v in core:
    if v not in idx: sc(v)
cyc=[cp for cp in comps if len(cp)>1 or cp[0] in succ[cp[0]]]
def per(x):
    for d in range(1,p+1):
        if p%d==0 and ((x>>d)|(x<<(p-d)))&M==x: return d
def kind(cp):
    s=set(cp)
    if s=={(0,0)}: return 'white'
    if s=={(A,M^A),(M^A,A)}: return 'rain'
    return 'other'
print('core',len(core),'cyclic components',len(cyc))
for cp in sorted(cyc,key=len):
    pers=sorted({max(per(u),per(v)) for u,v in cp})
    print('  size',len(cp),kind(cp),'state periods',pers)
cycstates=set().union(*[set(cp) for cp in cyc])
rest=core-cycstates
print('acyclic core states',len(rest))
# which cycle does each acyclic state come from / go to
compof={}
for i,cp in enumerate(cyc):
    for s in cp: compof[s]=i
def reach(s,fw=True):
    seen={s};stack=[s];hit=set()
    pred=defaultdict(list)
    for x in core:
        for y in succ[x]: pred[y].append(x)
    while stack:
        x=stack.pop()
        nb=succ[x] if fw else pred[x]
        for y in nb:
            if y in compof: hit.add(compof[y]); continue
            if y not in seen: seen.add(y);stack.append(y)
    return hit
walls=defaultdict(int)
for s in rest:
    walls[(tuple(sorted(reach(s,False))),tuple(sorted(reach(s,True))))]+=1
for (a,b),n in sorted(walls.items()):
    print('  wall states',n,'from',[ (len(cyc[i]),kind(cyc[i])) for i in a],'to',[(len(cyc[i]),kind(cyc[i])) for i in b])
big=max(cyc,key=len); bs=set(big)
outdeg=[sum(1 for t in succ[s] if t in bs) for s in big]
print('largest component: size',len(big),'out-degrees inside',sorted(set(outdeg)))
s0=min(big); cols=[s0[0]]; x=s0
while True:
    nx=[t for t in succ[x] if t in bs][0]
    cols.append(x[1]); x=nx
    if x==s0: break
L=len(cols)-1
print('cycle length (depth period m)',L)
ring0=[(cols[k]>>0)&1 for k in range(L)]
# minimal rotation period of the depth sequence of whole columns
mper=next(d for d in range(1,L+1) if L%d==0 and all(cols[k]==cols[(k+d)%L] for k in range(L)))
print('depth period of the columns',mper)
# time-shift symmetry: shifting time by s equals depth shift by r?
rot=lambda x,s: ((x>>s)|(x<<(p-s)))&M
for s in range(1,p):
    for r in range(L):
        if all(rot(cols[k],s)==cols[(k+r)%L] for k in range(L)):
            print('  time shift',s,'= depth shift',r); break
print('ring at time 0 (cell = depth, # black):', ''.join('#' if b else '.' for b in ring0))
print('black cells at time 0:',sum(ring0),'of',L)
