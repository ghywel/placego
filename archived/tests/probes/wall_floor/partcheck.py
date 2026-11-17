#!/usr/bin/env python3
"""partcheck.py (Local, L1533): every small cyclic part of E(w): do its letters follow AB or AAB on every edge inside the part? And do all ten lock windows start with a reset word?"""
import sys,json
from collections import defaultdict,deque
WA=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1))); WB=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
def isF(c): return c[0]==0 and c[1]!=c[2] and c[3]==1 and c[5]==1 and c[6]==0 and c[8]==0 and c[9]==1
for f in ('lock45.json','lock136.json'):
    S=json.load(open(f))
    S=[[1 if ch=='#' else 0 for ch in s] if isinstance(s,str) else s for s in S]
    print(f,len(S),'windows start with a reset word:',sum(isF(s) for s in S))
for w in [int(a) for a in sys.argv[1:]]:
    V=[];part=[];term=[];cyc=[];adj=[]
    for l in open(f'E{w}.txt'):
        h,p,t,c,a,b,cc,d=l.split()
        V.append(int(h,16)); part.append(int(p)); term.append(int(t)); cyc.append(int(c)); adj.append((int(a),int(b),int(cc),int(d)))
    n=len(V)
    let=['A' if (v>>(w-11))&2047==WA else 'B' for v in V]
    size=defaultdict(int)
    for p in part: size[p]+=1
    into=defaultdict(int)
    for i in range(n):
        for j in set(adj[i]):
            if part[i]!=part[j]: into[part[j]]+=1
    res=[]
    for p in {part[i] for i in range(n) if cyc[i] and not term[i]}:
        nodes=[i for i in range(n) if part[i]==p]; S=set(nodes)
        # phase assignment modulo 2 and 3
        def consistent(word):
            m=len(word)
            ph={}
            for st in range(m):
                if word[st]!=let[nodes[0]]: continue
                ph={nodes[0]:st}; q=deque([nodes[0]]); ok=True
                while q and ok:
                    u=q.popleft()
                    for x in set(adj[u]):
                        if x in S:
                            e=(ph[u]+1)%m
                            if word[e]!=let[x]: ok=False;break
                            if x in ph:
                                if ph[x]!=e: ok=False;break
                            else: ph[x]=e;q.append(x)
                if ok: return True
            return False
        fam='AB' if consistent('AB') else 'AAB' if consistent('AAB') else 'OTHER'
        res.append((size[p],fam,into[p]))
    print('w',w,sorted(res,reverse=True))
