#!/usr/bin/env python3
"""lock6in.py (Local, L1534): where the projections of a closed set sit in E(w), width by width. Usage: JSON WIDTHS..."""
import sys,json
from collections import defaultdict
d=json.load(open(sys.argv[1]))
S=[w for p in d for w in d[p]] if isinstance(d,dict) else d
K=len(S[0])
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
for w in [int(a) for a in sys.argv[2:]]:
    V={};part=[];term=[];cyc=[];adj=[]
    for i,l in enumerate(open(f'E{w}.txt')):
        h,p,t,c,a,b,cc,dd=l.split()
        V[int(h,16)]=i; part.append(int(p)); term.append(int(t)); cyc.append(int(c)); adj.append((int(a),int(b),int(cc),int(dd)))
    size=defaultdict(int)
    for p in part: size[p]+=1
    cloud=max({part[i] for i in range(len(part)) if term[i]},key=lambda p:size[p])
    res=defaultdict(int)
    for s in S:
        v=nat(s[K-w:]); i=V.get(v)
        if i is None: res['absent']+=1
        elif part[i]==cloud: res['cloud']+=1
        else: res[f'part {size[part[i]]}{" terminal" if term[i] else ""}{" cyclic" if cyc[i] else ""}']+=1
    print(w,dict(res),flush=True)
