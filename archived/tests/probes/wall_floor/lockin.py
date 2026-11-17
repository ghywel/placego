#!/usr/bin/env python3
"""lockin.py (Local, L1532): where the AAB lock's top cells sit in E(w): in the cloud, or in a part of their own?"""
import sys,json
from collections import defaultdict
S=json.load(open('lock136.json'))
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
for w in [int(a) for a in sys.argv[1:]]:
    V={};part=[];term=[];adj=[];vals=[]
    for i,l in enumerate(open(f'E{w}.txt')):
        h,p,t,c,a,b,cc,d=l.split()
        V[int(h,16)]=i; part.append(int(p)); term.append(int(t)); adj.append((int(a),int(b),int(cc),int(d))); vals.append(int(h,16))
    size=defaultdict(int)
    for p in part: size[p]+=1
    cloud=max({part[i] for i in range(len(part)) if term[i]},key=lambda p:size[p])
    res=[]
    for s in S:
        v=nat(s[136-w:])
        i=V.get(v)
        if i is None: res.append('absent'); continue
        res.append(f'{"cloud" if part[i]==cloud else "part size %d%s"%(size[part[i]]," terminal" if term[i] else ""):s}')
    print(w,res)
    # the edges into the part
    idx=[V.get(nat(s[136-w:])) for s in S]
    ps={part[i] for i in idx if i is not None and part[i]!=cloud}
    for p in ps:
        into=sum(1 for i in range(len(part)) if part[i]!=p and any(part[j]==p for j in adj[i]))
        outof=sum(1 for i in range(len(part)) if part[i]==p and any(part[j]!=p for j in adj[i]))
        print('   part',p,'size',size[p],'windows with an edge in',into,'windows with an edge out',outof)
