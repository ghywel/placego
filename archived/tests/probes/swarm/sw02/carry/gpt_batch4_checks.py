#!/usr/bin/env python3
"""Fixed certificate controls and p<=128 replay; no new search horizon.

Predictions/counterfactuals and aggregate stage limits are in the batch4 report.
All generated data is written under CAPPED_OUT by the serial stage supervisor.
"""
import itertools
import json
import os
from pathlib import Path


def lasso():
    c = [136,14,139,200,111,53,209,28,215,101,68,7,197,100,183,154,232,14,235,178,34,131,226,50,219,77,116,7,245,89,17,193,113,25,237,166,58,131,250,172,136,224,184,140,246,83,29,193,125,86,68,112,92,70,123,169,142,224,190,43,34,56,46,35,189,212,71,112,95,149,17,28,23,145,222,106,163,56,175,202,136,14]
    def failures(x):
        return sum(((x[j+1] >> ((t+1)%8)) & 1) !=
                   (((x[j] >> t)&1) ^ (((x[j+1]>>t)&1)|((x[j+2]>>t)&1)))
                   for j in range(80) for t in range(8))
    assert c[:2] == c[-2:] and failures(c) == 0
    assert all(any(((c[1]>>t)&1) != ((c[1]>>((t+p)%8))&1)
                   for t in range(8)) for p in range(1,8))
    mutant = c.copy(); mutant[2] ^= 1
    assert failures(mutant) > 0
    assert not any(all(((c[1]>>((s+t)%8))&1)==((w>>(t%4))&1)
                      for t in range(8)) for s in range(8) for w in range(16))
    print(json.dumps({'lasso_edges':640,'failures':0,'mutation_failures':failures(mutant)}),flush=True)


def words():
    a,b='11000101111000','11000101110101000111'
    def language(blocks):
        return {s[i:i+25] for combo in itertools.product(blocks,repeat=4)
                for s in [''.join(combo)] for i in range(len(s)-24)}
    def bad(blocks,rule=30,k=12):
        count=0
        for w in language(blocks):
            row=list(map(int,w))
            for _ in range(k):
                row=[(rule>>(4*row[i]+2*row[i+1]+row[i+2]))&1
                     for i in range(len(row)-2)]
            count += row[0]!=int(w[0])
        return count
    assert len(language((a,b)))==62 and bad((a,b))==0
    assert bad((a,b),k=11)>0 and bad((a,b),rule=90)>0
    am=a[:5]+str(1-int(a[5]))+a[6:]
    assert bad((am,b))>0
    print(json.dumps({'LN12_windows':62,'failures':0,'mutant_failures':bad((am,b)),
                      'rule90_failures':bad((a,b),rule=90)}),flush=True)


def tree(p):
    full=(1<<p)-1; a=sum(1<<t for t in range(1,p,2)); na=a^full
    stack=[(a,a,1,1,None)]; best=None; maxdepth=0
    nodes=sumh=rain=deaths=splits=doublings=0
    while stack:
        u,v,h,depth,parent=stack.pop(); nodes+=1;sumh+=h
        assert depth<=3000 and nodes<=1121550
        link=(u,v,h,parent)
        if depth>maxdepth: maxdepth=depth;best=link
        parity=((u|v)&((1<<(2*h))-1)).bit_count()%2
        if parity and 2*h==p: deaths+=1;continue
        x=u|v;s=1
        while s<p: x^=x<<s;s*=2
        w=(x<<1)&full
        if not parity:
            splits+=1; children=(w,w^full);hh=h
        else:
            doublings+=1;children=(w,);hh=2*h
        for ww in children:
            if (v==a and ww==na) or (v==na and ww==a):rain+=1
            else:stack.append((v,ww,hh,depth+1,link))
    path=[]
    while best:
        u,v,h,best=best;path.append((u,v,h))
    path.reverse()
    # Independent scalar checks on every retained transition, including wrap.
    for (u,v,h),(vv,w,hh) in zip(path,path[1:]):
        assert v==vv
        assert all(((w>>((t+1)%p))&1)==
                   (((w>>t)&1)^(((u>>t)&1)|((v>>t)&1))) for t in range(p))
        for word in (u,v):
            assert all(((word>>t)&1)==((word>>((t+2*h)%p))&1) for t in range(p))
        assert any(((u>>t)&1)!=((u>>((t+h)%p))&1) or
                   ((v>>t)&1)!=((v>>((t+h)%p))&1) for t in range(p))
    top=sum(2*h==p for u,v,h in path)
    result={'p':p,'nodes':nodes,'two_sumH':2*sumh,'longest':maxdepth,
            'rain':rain,'deaths':deaths,'splits':splits,'doublings':doublings,
            'retained_top_layer_nodes':top}
    print(json.dumps(result),flush=True)
    if p==128:
        assert (nodes,2*sumh,maxdepth,rain,deaths,doublings)==(1121550,143381758,2033,0,560085,1381)
        assert top>=1928
        (Path(os.environ['CAPPED_OUT'])/'p128-retained-path.json').write_text(json.dumps(path)+'\n')


if __name__=='__main__':
    lasso();words()
    for p in (2,4,8,16,32,64,128):tree(p)
    print('BATCH4_FIXED_CHECKS_PASS',flush=True)
