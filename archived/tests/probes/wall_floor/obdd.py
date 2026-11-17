#!/usr/bin/env python3
"""obdd.py (Local, L1532): sets of words as layered decision diagrams, read from the low cell up, so that a backward tick can act on a whole set of rows at once.
A set: list of levels; level i is a list of (child0, child1), child -1 for nothing; the last level's children are 0 for present. tick() applies the inverse transducer with all four lower states."""
import sys
sys.setrecursionlimit(100000)
STATES=((0,0),(0,1),(1,0),(1,1))
class Set:
    __slots__=('lv','root','n')
    def __init__(s,lv,root,n): s.lv=lv; s.root=root; s.n=n
def from_word(x,n):
    lv=[]
    for i in range(n):
        c=(x>>i)&1
        lv.append([(0,-1) if c==0 else (-1,0)])
    return Set(lv,0,n)
def tick(S,states=STATES):
    n=S.n; lv=S.lv; top=n+3
    rain=(0,1,0)
    new=[[] for _ in range(top)]; cons=[{} for _ in range(top)]; memo=[{} for _ in range(top+1)]
    def child(i,node,c):
        if i<n: return lv[i][node][c]
        return 0 if c==rain[i-n] else -1
    def build(i,M):
        if i==top: return 0
        m=memo[i]; r=m.get(M)
        if r is not None: return r
        ch=[]
        for o in (0,1):
            nx=set()
            for node,p1,p2 in M:
                c=o^(p1|p2)
                k=child(i,node,c)
                if k!=-1: nx.add((k,o,p1))
            ch.append(build(i+1,frozenset(nx)) if nx else -1)
        key=(ch[0],ch[1])
        d=cons[i]; r=d.get(key)
        if r is None:
            r=len(new[i]); new[i].append(key); d[key]=r
        m[M]=r
        return r
    root=build(0,frozenset((S.root,a,b) for a,b in states))
    return Set(new,root,top)
def nodes_at(S,i):
    cur={S.root}
    for j in range(i):
        nx=set()
        for v in cur:
            a,b=S.lv[j][v]
            if a!=-1: nx.add(a)
            if b!=-1: nx.add(b)
        cur=nx
    return cur
def suffixes(S,i,cap=64):
    """the set of words on levels i..n-1, as ints with bit 0 = level i"""
    out={}
    for v in nodes_at(S,i):
        st=[(i,v,0)]
        while st:
            j,u,acc=st.pop()
            if j==S.n: out[acc]=1; continue
            a,b=S.lv[j][u]
            if a!=-1: st.append((j+1,a,acc))
            if b!=-1: st.append((j+1,b,acc|(1<<(j-i))))
            if len(out)>cap: return out
    return out
def size(S): return sum(len(l) for l in S.lv)
def width(S): return max(len(l) for l in S.lv)
def lift(S,k):
    """forget the k lowest cells: the set of what lies above them"""
    cur=nodes_at(S,k)
    lv=S.lv[k:]
    # a new root that unions the nodes at level k: do a subset construction
    n=S.n-k
    new=[[] for _ in range(n)]; cons=[{} for _ in range(n)]; memo=[{} for _ in range(n+1)]
    def build(i,M):
        if i==n: return 0
        r=memo[i].get(M)
        if r is not None: return r
        ch=[]
        for c in (0,1):
            nx={lv[i][v][c] for v in M if lv[i][v][c]!=-1}
            ch.append(build(i+1,frozenset(nx)) if nx else -1)
        key=(ch[0],ch[1]); d=cons[i]; r=d.get(key)
        if r is None:
            r=len(new[i]); new[i].append(key); d[key]=r
        memo[i][M]=r
        return r
    root=build(0,frozenset(cur))
    return Set(new,root,n)
