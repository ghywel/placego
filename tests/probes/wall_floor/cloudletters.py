#!/usr/bin/env python3
"""cloudletters.py (Local, L1532): the letters on the cloud and the lock class from E<w>.txt: longest repeat of AB and of AAB in each class, and the block words."""
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
WA=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1))); WB=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
def load(w):
    V=[];part=[];term=[];adj=[]
    for l in open(f'E{w}.txt'):
        h,p,t,c,a,b,cc,d=l.split()
        V.append(int(h,16)); part.append(int(p)); term.append(int(t)); adj.append((int(a),int(b),int(cc),int(d)))
    return V,part,term,adj
for w in [int(a) for a in sys.argv[1:]]:
    V,part,term,adj=load(w)
    n=len(V)
    let=['A' if (v>>(w-11))&2047==WA else 'B' if (v>>(w-11))&2047==WB else '?' for v in V]
    size=defaultdict(int)
    for p in part: size[p]+=1
    tp=sorted({part[i] for i in range(n) if term[i]},key=lambda p:-size[p])
    for name,p in zip(('cloud','lock'),tp):
        nodes=[i for i in range(n) if part[i]==p]; S=set(nodes)
        # longest path in the subgraph where letters alternate
        succ={i:[j for j in set(adj[i]) if j in S and let[j]!=let[i]] for i in nodes}
        # detect cycle and longest path by DFS with colors
        color={}; best={}; cyc=False
        def dfs(u):
            global cyc
            st=[(u,iter(succ[u]))]; color[u]=1; best[u]=1
            while st:
                v,it=st[-1]
                for x in it:
                    if color.get(x,0)==1: cyc=True; continue
                    if color.get(x,0)==0:
                        color[x]=1; best[x]=1; st.append((x,iter(succ[x]))); break
                    best[v]=max(best[v],best[x]+1)
                else:
                    color[v]=2; st.pop()
                    if st: p_=st[-1][0]; best[p_]=max(best[p_],best[v]+1)
        for i in nodes:
            if i not in color: dfs(i)
        # word counts of labelled paths
        cur={i:1 for i in nodes}
        print(f'w {w} {name}: size {len(nodes)}, letters {"".join(sorted({let[i] for i in nodes}))}, alternating cycle {cyc}, longest alternating path (letters) {max(best.values())}')
