#!/usr/bin/env python3
"""langset.py (Local, L1532): the settled language by sets of rows. The set of rows with a given letter word is carried as a diagram; each extension is one backward tick on the whole set, restricted to the next letter.
The low end has a free state on each tick, so an empty set is a proof that the word is forbidden; a non-empty set is a candidate, tested against the exact counts of L1529."""
import sys,time
sys.setrecursionlimit(100000)
from obdd import Set,STATES
WA=(0,0,1,1,1,1,0,0,0,1,1); WB=(0,1,0,1,1,1,0,0,0,1,1)
LET={'A':WA,'B':WB}
def start(letter,n):
    lv=[]
    for i in range(n-11): lv.append([(0,0)])
    w=LET[letter]
    for i,c in enumerate(w): lv.append([(0,-1) if c==0 else (-1,0)])
    return Set(lv,0,n)
RAIN=(0,1,0)
def tick_r(S,letter):
    n=S.n; lv=S.lv; top=n+3; req=LET[letter]; base=top-11
    new=[[] for _ in range(top)]; cons=[{} for _ in range(top)]; memo=[{} for _ in range(top+1)]
    def build(i,M):
        if i==top: return 0
        m=memo[i]; r=m.get(M)
        if r is not None: return r
        ch=[-1,-1]
        for o in (0,1):
            if i>=base and req[i-base]!=o: continue
            nx=set()
            if i<n:
                L=lv[i]
                for node,p1,p2 in M:
                    k=L[node][o^(p1|p2)]
                    if k!=-1: nx.add((k,o,p1))
            else:
                rc=RAIN[i-n]
                for node,p1,p2 in M:
                    if o^(p1|p2)==rc: nx.add((0,o,p1))
            if nx: ch[o]=build(i+1,frozenset(nx))
        if ch[0]==-1 and ch[1]==-1:
            m[M]=-1; return -1
        key=(ch[0],ch[1]); d=cons[i]; r=d.get(key)
        if r is None:
            r=len(new[i]); new[i].append(key); d[key]=r
        m[M]=r
        return r
    root=build(0,frozenset((S.root,a,b) for a,b in STATES))
    if root==-1: return None
    return Set(new,root,top)
def word_set(word,n0):
    S=start(word[0],n0)
    for c in word[1:]:
        S=tick_r(S,c)
        if S is None: return None
    return S
def width(S): return max(len(l) for l in S.lv)
if __name__=='__main__':
    LM=int(sys.argv[1]); n0=int(sys.argv[2]) if len(sys.argv)>2 else 11+3*LM
    t0=time.time()
    cur={'A':start('A',n0),'B':start('B',n0)}
    print('L=1 attainable 2',flush=True)
    for L in range(2,LM+1):
        nxt={}; forb=[]; mw=0
        for w,S in cur.items():
            for c in 'AB':
                v=w+c
                if v[1:] not in cur: continue
                T=tick_r(S,c)
                if T is None: forb.append(v)
                else:
                    nxt[v]=T; mw=max(mw,width(T))
        print(f'L={L} attainable {len(nxt)} minimal forbidden {len(forb)} max width {mw} time {time.time()-t0:.1f}',flush=True)
        for v in forb: print('   ',v)
        cur=nxt
