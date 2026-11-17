#!/usr/bin/env python3
"""clos.py (Local, L1532): the graph of width-w windows under every lower state, from the windows of a quiet AAB stretch. Strongly connected parts, where the letters can go, whether a lock is reachable.
Each of the four lower states gets weight 1/4 for the Markov estimate. Free states can invent paths, so this graph over-counts what real rows do."""
import sys,time
import numpy as np
from reachlib import *
sys.setrecursionlimit(1000000)
def nxt(x,w,s):
    y=step(x,w,s)
    return y>>3
def graph(start,w,cap=400000):
    g={}; st=list(start)
    for v in start: g[v]=None
    while st:
        v=st.pop(); e=[]
        for s in STATES:
            u=nxt(v,w,s); e.append(u)
            if u not in g:
                g[u]=None; st.append(u)
                if len(g)>cap: return None
        g[v]=e
    return g
def sccs(g):
    idx={};low={};on=set();stack=[];out=[];c=[0]
    for root in g:
        if root in idx: continue
        work=[(root,0)]
        while work:
            v,i=work.pop()
            if i==0:
                idx[v]=low[v]=c[0]; c[0]+=1; stack.append(v); on.add(v)
            rec=False
            e=g[v]
            while i<len(e):
                u=e[i]; i+=1
                if u not in idx:
                    work.append((v,i)); work.append((u,0)); rec=True; break
                elif u in on: low[v]=min(low[v],idx[u])
            if rec: continue
            if low[v]==idx[v]:
                comp=[]
                while True:
                    u=stack.pop(); on.discard(u); comp.append(u)
                    if u==v: break
                out.append(comp)
            if work:
                p,_=work[-1]; low[p]=min(low[p],low[v])
    return out
def quiet_rows(seed,n=90,skip=300):
    y=fresh(seed)
    for t in range(skip): y=inv(y)
    rows=[]; seq=''
    # find 60 letters of pure AAB then keep
    for t in range(640):
        d=top(y); seq+=let(win(y,11,d),11); rows.append(y); y=inv(y)
        if len(seq)>=n and all(seq[-n+i:-n+i+3] in('AAB','ABA','BAA') for i in range(n-3)):
            return rows[-n:]
        if len(rows)>400: rows=rows[-200:]; seq=seq[-200:]
    return None
if __name__=='__main__':
    seeds=[int(a) for a in sys.argv[1].split(',')]
    rows=[]
    for sd in seeds:
        r=quiet_rows(sd)
        if r: rows+=r
    print('rows',len(rows),flush=True)
    for w in [int(a) for a in sys.argv[2].split(',')]:
        t0=time.time()
        start={win(r,w) for r in rows}
        g=graph(start,w)
        if g is None: print('w',w,'start',len(start),'closure over cap'); continue
        comps=sccs(g)
        cid={}
        for i,c in enumerate(comps):
            for v in c: cid[v]=i
        terminal=[i for i,c in enumerate(comps) if all(cid[u]==i for v in c for u in g[v])]
        L={v:let(v,w) for v in g}
        print(f'w {w}: start {len(start)} closure {len(g)} comps {len(comps)} terminal {len(terminal)} time {time.time()-t0:.1f}',flush=True)
        for i in terminal[:12]:
            c=comps[i]
            print('   terminal size',len(c),'letters',''.join(sorted({L[v] for v in c})),show(c[0],w))
        big=sorted(comps,key=len,reverse=True)[:4]
        for c in big:
            print('   comp size',len(c),'letters',''.join(sorted({L[v] for v in c})))
