#!/usr/bin/env python3
"""Finite degree-two covariant phase question on the same180states.

Fixed26orbit-sum basis, no degree/horizon/core enlargement on failure.
"""
import itertools
import json
import os
from pathlib import Path
import random
from gpt_period12_return import gf4mul,rot,successors


def rotate_mask(mask,t):
    return sum(1<<(12*(i//12)+(i%12+t)%12) for i in range(24) if (mask>>i)&1)


def main():
    data=json.loads(Path(os.environ['PERIOD12_GRAPH']).read_text())
    monomials=[1<<i for i in range(24)]+[(1<<i)|(1<<j) for i in range(24) for j in range(i+1,24)]
    used=set();basis=[]
    omega_inv=(1,3,2)
    for mask in monomials:
        if mask in used:continue
        orbit=[];m=mask
        while m not in orbit:orbit.append(m);used.add(m);m=rotate_mask(m,1)
        if len(orbit)%3:continue
        basis.append([(m,omega_inv[t%3]) for t,m in enumerate(orbit)])
    assert len(basis)==26
    def values(pair):
        bits=pair[0]|(pair[1]<<12)
        ans=[]
        for poly in basis:
            z=0
            for m,a in poly:
                if bits&m==m:z^=a
            ans.append(z)
        return ans
    rows=[values(pair)+[1] for pair in data['root_component']]
    original=[r.copy() for r in rows];pivot=[];rank=0
    for col in range(len(basis)):
        rr=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if rr is None:continue
        rows[rank],rows[rr]=rows[rr],rows[rank]
        inv=(0,1,3,2)[rows[rank][col]]
        rows[rank]=[gf4mul(inv,x) for x in rows[rank]]
        for i in range(len(rows)):
            if i!=rank and rows[i][col]:
                a=rows[i][col];rows[i]=[x^gf4mul(a,y) for x,y in zip(rows[i],rows[rank])]
        pivot.append(col);rank+=1
    consistent=not any(not any(r[:-1]) and r[-1] for r in rows)
    result={'basis_size':26,'rank':rank,'consistent':consistent}
    if consistent:
        coeff=[0]*26
        for i,c in enumerate(pivot):coeff[c]=rows[i][-1]
        columns=[sum(gf4mul(a,r[i])<<(2*j) for j,r in enumerate(original))
                 for i in range(26) for a in (1,2,3)]
        singles=[(v,[(i//3,1+i%3)]) for i,v in enumerate(columns)]
        pairs={}
        for (u,a),(v,b) in itertools.combinations(singles,2):
            if a[0][0]==b[0][0]:continue
            pairs.setdefault(u^v,[]).append(a+b)
        target=sum(1<<(2*j) for j in range(len(original)))
        short=next((a for v,a in singles if v==target),None)
        if short is None:short=next(iter(pairs.get(target,[])),None)
        if short is None:
            short=next((a+b for v,a in singles for b in pairs.get(target^v,[])
                        if len({i for i,z in a+b})==3),None)
        if short is None:
            short=next((a+b for v,aa in pairs.items() for a in aa for b in pairs.get(target^v,[])
                        if len({i for i,z in a+b})==4),None)
        if short:
            coeff=[0]*26
            for i,a in short:coeff[i]=a
        def phase(pair):
            z=0
            for a,b in zip(coeff,values(pair)):z^=gf4mul(a,b)
            return z
        for t,comp in enumerate(data['time_components'][:6]):
            for pair in comp:assert phase(pair)==(1,2,3)[t%3]
        rng=random.Random(20261110)
        for _ in range(256):
            pair=(rng.randrange(4096),rng.randrange(4096))
            assert phase(tuple(rot(w,1) for w in pair))==gf4mul(2,phase(pair))
        bad=[];tested=0
        for _ in range(256):
            pair=(rng.randrange(4096),rng.randrange(4096))
            for child in successors(pair):
                tested+=1
                if phase(pair)!=phase(child):bad.append([pair,child,phase(pair),phase(child)])
        generated_bad=[]
        for pair,children in data['adj']:
            for child in children:
                if phase(pair)!=phase(child):generated_bad.append([pair,child])
        result.update({'terms':[(i,a) for i,a in enumerate(coeff) if a],
                       'short_at_most4':short,'basis':basis,
                       'arbitrary_legal_edges_tested':tested,'arbitrary_legal_failures':len(bad),
                       'first_arbitrary_failure':bad[:1],'generated_graph_failures':len(generated_bad)})
    (Path(os.environ['CAPPED_OUT'])/'quadratic-phase.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='basis'}),flush=True)
    print('PERIOD12_QUADRATIC_QUESTION_SETTLED',flush=True)


if __name__=='__main__':main()
