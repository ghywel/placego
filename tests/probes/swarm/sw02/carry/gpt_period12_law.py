#!/usr/bin/env python3
"""Fixed small graph analysis and ordinary-time period controls.

New predictions/formula and scope are frozen in the period12 report.
Reads only the frozen generated certificate; no graph/period expansion.
"""
import itertools
import json
import os
from pathlib import Path
from math import gcd,lcm


def packed_step(x,n):
    mask=(1<<n)-1
    left=((x<<1)|(x>>(n-1)))&mask
    right=(x>>1)|((x&1)<<(n-1))
    return left^(x|right)


def primitive(w):
    return all(any(w[i]!=w[i%k] for i in range(len(w)))
               for k in range(1,len(w)) if len(w)%k==0)


def main():
    data=json.loads(Path(os.environ['PERIOD12_GRAPH']).read_text())
    comp={tuple(v) for v in data['root_component']}
    adj={tuple(v):[tuple(w) for w in ws] for v,ws in data['adj']}
    branches=sorted(tuple(v) for v in data['summary']['branch_states'])
    def rot(w,k):return ((w>>k)|(w<<(12-k)))&4095
    assert tuple(rot(w,6) for w in branches[0])==branches[1]
    routes={}
    for row in data['returns']:
        s=branches.index(tuple(row['start']));t=branches.index(tuple(row['end']))
        cross=int(s!=t);routes[s,cross]=[tuple(v) for v in row['path']]
        assert len(routes[s,cross])-1==14-4*cross
    cases=[]
    for m in range(1,7):
        for word in itertools.product(range(2),repeat=m):
            if not primitive(word):continue
            r=sum(word);length=14*m-4*r
            branch=0;path=[]
            for _ in range(2 if r%2 else 1):
                for cross in word:
                    segment=routes[branch,cross]
                    assert segment[0]==branches[branch]
                    path.extend(segment[:-1]);branch^=cross
            assert branch==0
            assert all(path[(i+1)%len(path)] in adj[v] for i,v in enumerate(path))
            # The stored path runs LEFT in space. Reverse to increasing sites.
            row=[v[0]&1 for v in path][::-1];n=len(row)
            assert n==(2 if r%2 else 1)*length
            x=sum(b<<i for i,b in enumerate(row));initial=x
            # Literal least spatial period of this initial row.
            spatial=next(k for k in range(1,n+1) if
                         all(row[i]==row[(i+k)%n] for i in range(n)))
            assert spatial==n
            predicted=(12*length//gcd(2*length,length+6) if r%2 else lcm(12,length))
            for t in range(1,predicted+1):
                x=packed_step(x,n)
                if x==initial:break
            assert t==predicted and x==initial,(word,n,predicted,t)
            cases.append({'events':word,'crosses':r,'length':length,
                          'spatial_period':n,'ordinary_F_period':t})
    # Does any *linear parity* have a component-dependent constant value?
    rows=[]
    components=[]
    for vs in data['time_components'][:6]:
        words=[(v[0]<<12)|v[1] for v in vs];components.append(words)
        rows.extend(v^words[0] for v in words[1:])
    basis={}
    for x in rows:
        while x:
            b=x.bit_length()-1
            if b not in basis:basis[b]=x;break
            x^=basis[b]
    annihilator=[]
    for free in range(24):
        if free in basis:continue
        z=1<<free
        for pivot in sorted(basis):
            if (basis[pivot]&z).bit_count()%2:z^=1<<pivot
        assert all((v&z).bit_count()%2==0 for v in rows)
        annihilator.append({'mask':z,'component_values':[(words[0]&z).bit_count()%2 for words in components]})
    ans={'period_cases':len(cases),'cases':cases,'within_component_difference_rank':len(basis),
         'constant_parity_basis':annihilator}
    (Path(os.environ['CAPPED_OUT'])/'period-law.json').write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps({k:v for k,v in ans.items() if k!='cases'}),flush=True)
    print('PERIOD12_PERIOD_LAW_PASS',flush=True)


if __name__=='__main__':main()
