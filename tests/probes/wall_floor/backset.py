#!/usr/bin/env python3
"""backset.py (Local, L1536): how far back can an entrance to a closed set go? A set of width-w windows as a decision diagram; pre(S) = settled windows with some lower state stepping into S. For each window that steps into the target from outside it, iterate pre until the set is empty or the depth limit is reached.
Usage: JSON WIDTH MAXDEPTH [MAXWIDTH]. """
import sys,json,time
sys.setrecursionlimit(1000000)
from obdd import Set,STATES,from_word
from reachlib import *
from clos import nxt
WA=(0,0,1,1,1,1,0,0,0,1,1); WB=(0,1,0,1,1,1,0,0,0,1,1)
RAIN=(0,1,0)
def pre(S,w):
    lv=S.lv
    new=[[] for _ in range(w)]; cons=[{} for _ in range(w)]; memo=[{} for _ in range(w+1)]
    base=w-11
    def accept(M):
        for node,p1,p2 in M:
            n=node; a,b=p1,p2; ok=True
            for j in range(3):
                o=RAIN[j]^(a|b)
                n=lv[w-3+j][n][o]
                if n==-1: ok=False;break
                b=a;a=o
            if ok: return True
        return False
    def build(i,M,ls):
        if i==w:
            return 0 if accept(M) else -1
        key=(M,ls); m=memo[i]; r=m.get(key)
        if r is not None: return r
        ch=[-1,-1]
        for c in (0,1):
            l2=ls
            if i>=base:
                ok=[]
                if ls in (0,1) and WA[i-base]==c: ok.append(1)
                if ls in (0,2) and WB[i-base]==c: ok.append(2)
                if not ok: continue
                l2=0 if len(ok)==2 else ok[0]
            nx=set()
            for node,p1,p2 in M:
                o=c^(p1|p2)
                if i<3: k=node
                else:
                    k=lv[i-3][node][o]
                    if k==-1: continue
                nx.add((k,o,p1))
            if nx: ch[c]=build(i+1,frozenset(nx),l2)
        if ch[0]==-1 and ch[1]==-1:
            m[key]=-1; return -1
        k2=(ch[0],ch[1]); d=cons[i]; r=d.get(k2)
        if r is None:
            r=len(new[i]); new[i].append(k2); d[k2]=r
        m[key]=r
        return r
    root=build(0,frozenset((S.root,a,b) for a,b in STATES),0)
    if root==-1: return None
    return Set(new,root,w)
def count(S):
    w=S.n
    c=[1]
    for i in range(w-1,-1,-1):
        cur=[]
        for a,b in S.lv[i]:
            cur.append((c[a] if a!=-1 else 0)+(c[b] if b!=-1 else 0))
        c=cur
    return c[S.root]
def width(S): return max(len(l) for l in S.lv)
def preds(v,w):
    y=lambda k:(v>>(w-1-k))&1
    top=0
    for k in range(0,w-5):
        c=y(k+3)^(y(k+4)|y(k+5))
        top|=c<<(w-1-k)
    out=set()
    for low in range(32):
        u=top|low
        if let(u,w)=='?': continue
        for s in STATES:
            if nxt(u,w,s)==v: out.add(u); break
    return out
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
if __name__=='__main__':
    d=json.load(open(sys.argv[1])); w=int(sys.argv[2]); D=int(sys.argv[3]); MW=int(sys.argv[4]) if len(sys.argv)>4 else 20000
    S=[x for p in d for x in d[p]]; K=len(S[0])
    T={nat(x[K-w:]) for x in S}
    ent=set()
    for v in T:
        for u in preds(v,w):
            if u not in T: ent.add(u)
    print(f'w {w}: target {len(T)} windows, entrances {len(ent)}',flush=True)
    t0=time.time(); died={}; alive=[]; big=0
    for u in sorted(ent):
        Sx=from_word(u,w); dep=0; res=None
        while dep<D:
            Sx=pre(Sx,w); dep+=1
            if Sx is None: res=dep; break
            if width(Sx)>MW: res='wide'; big+=1; break
        if res is None or res=='wide': alive.append((u,dep,count(Sx) if Sx else 0,width(Sx) if Sx else 0))
        else: died[res]=died.get(res,0)+1
    print('  dead by past length:',sorted(died.items()))
    print('  alive at depth limit or too wide:',len(alive),'examples',[(a[1],a[2] if a[2]<10**6 else 'many',a[3]) for a in alive[:6]],f'time {time.time()-t0:.1f}',flush=True)
