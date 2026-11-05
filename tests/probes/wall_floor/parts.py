#!/usr/bin/env python3
"""parts.py (Local, L1532): the small cyclic parts of E(w): size, edges in and out, letters along their cycles, and where the edges out go."""
import sys
from collections import defaultdict
WA=sum(b<<i for i,b in enumerate((0,0,1,1,1,1,0,0,0,1,1))); WB=sum(b<<i for i,b in enumerate((0,1,0,1,1,1,0,0,0,1,1)))
for w in [int(a) for a in sys.argv[1:]]:
    V=[];part=[];term=[];cyc=[];adj=[]
    for l in open(f'E{w}.txt'):
        h,p,t,c,a,b,cc,d=l.split()
        V.append(int(h,16)); part.append(int(p)); term.append(int(t)); cyc.append(int(c)); adj.append((int(a),int(b),int(cc),int(d)))
    n=len(V)
    let=['A' if (v>>(w-11))&2047==WA else 'B' if (v>>(w-11))&2047==WB else '?' for v in V]
    size=defaultdict(int)
    for p in part: size[p]+=1
    tp=sorted({part[i] for i in range(n) if term[i]},key=lambda p:-size[p])
    name={tp[0]:'CLOUD'}
    if len(tp)>1: name[tp[1]]='LOCK'
    cp=sorted({part[i] for i in range(n) if cyc[i]},key=lambda p:-size[p])
    into=defaultdict(int); out=defaultdict(lambda:defaultdict(int))
    for i in range(n):
        for j in set(adj[i]):
            if part[i]!=part[j]:
                into[part[j]]+=1; out[part[i]][part[j]]+=1
    print(f'w {w}: E {n}, parts {len(size)}, not cyclic windows {sum(1 for i in range(n) if not cyc[i])}')
    for p in cp:
        nodes=[i for i in range(n) if part[i]==p]
        # letter words of a shortest cycle through a node, by following any edge inside the part
        S=set(nodes); start=nodes[0]; seen={start:''}; cur=[start]; word=None
        from collections import deque
        q=deque([start]); par={start:None}
        while q and word is None:
            u=q.popleft()
            for x in set(adj[u]):
                if x==start:
                    # unwind
                    wd='';v=u
                    while v is not None: wd=let[v]+wd; v=par[v]
                    word=wd; break
                if x in S and x not in par: par[x]=u; q.append(x)
        tgt=sorted(((name.get(k,'size %d'%size[k]),c) for k,c in out[p].items()),key=lambda t:-t[1])[:4]
        print(f'   part size {size[p]} {name.get(p,"")} in {into[p]} out {sum(out[p].values())} letters {"".join(sorted({let[i] for i in nodes}))} a cycle {word} goes to {tgt}')
