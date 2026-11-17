#!/usr/bin/env python3
"""Independent certificate replay and full factor-language comparison.

The tested grammar is written explicitly from the first return-automaton run.
No minimization/orbit implementation from that run is imported.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

A,E='25','33535555'


def parse(path):
    rows={}
    for line in path.read_text().splitlines():
        a=line.split();q=int(a[0]);assert q not in rows
        rows[q]={int(k):int(v) for k,v in (p.split(':') for p in a[2:])}
    assert all(t in rows for r in rows.values() for t in r.values())
    return rows


def move(T,q,w):
    for a in w:
        if q < 0 or int(a) not in T[q]:return -1
        q=T[q][int(a)]
    return q


def certificate(T,r):
    mapping={int(q):v for q,v in r['class_map'].items()}
    for q,o in r['raw_orbits'].items():
        q=int(q); states=o['states']; dest=o['dest'];m=o['mu'];p=o['period']
        assert len(states)==len(dest)==m+p and states[0]==q
        assert len(set(states))==len(states)
        for i,s in enumerate(states):
            assert move(T,s,A)==states[i+1 if i+1<len(states) else m]
            assert move(T,s,E)==dest[i]
        if q < 0:continue
        restricted=mapping[q]==1
        threshold=6 if r['width']==38 or not restricted else 7
        # Directly certify all n via each stored prefix and cyclic residue.
        # Beyond threshold the proposed output is constant; check each cycle
        # both before and after that threshold.
        for n in range(max(threshold,m)+2*p+1):
            i=n if n<len(dest) else m+(n-m)%p
            actual=mapping[dest[i]]
            wanted=1 if not restricted and n==4 else (0 if n>=threshold else -1)
            assert actual==wanted,(q,n,actual,wanted)
    assert mapping[move(T,0,E)]==0


def grammar(short_next):
    N=collections.defaultdict(lambda:collections.defaultdict(set))
    def edge(u,a,v):N[u][a].add(v);N[v]
    for s in (0,1):
        for n in range(8):
            b=('b',s,n)
            edge(b,2,('a',s,n));edge(('a',s,n),5,('b',s,min(7,n+1)))
            t=1 if s==0 and n==4 else 0 if n>=(6 if s==0 else short_next) else None
            if t is not None:
                v=b
                for k,c in enumerate(E):
                    u=('b',t,0) if k==len(E)-1 else ('e',t,k)
                    edge(v,int(c),u);v=u
    # All states as starts/ends gives factors of the bi-infinite graph language.
    # Explicitly verify that every state belongs to a single recurrent component.
    for reverse in (False,True):
        adj=collections.defaultdict(set)
        for u,row in N.items():
            for targets in row.values():
                for v in targets:adj[v if reverse else u].add(u if reverse else v)
        seen={next(iter(N))};todo=list(seen)
        while todo:
            for v in adj[todo.pop()]:
                if v not in seen:seen.add(v);todo.append(v)
        assert len(seen)==len(N)
    root=frozenset(N);ids={root:0};todo=collections.deque([root]);T={}
    while todo:
        S=todo.popleft();row={}
        for c in (2,3,5):
            V=frozenset(v for u in S for v in N[u].get(c,()))
            if V:
                if V not in ids:ids[V]=len(ids);todo.append(V)
                row[c]=ids[V]
        T[ids[S]]=row
    return T,len(N)


def compare(U,V):
    seen={(0,0)};todo=collections.deque([(0,0,'')])
    while todo:
        q,r,w=todo.popleft()
        if (q<0)!=(r<0):return {'equal':False,'word':w,'left_accepts':q>=0}
        for c in set(U.get(q,{}))|set(V.get(r,{})):
            z=U.get(q,{}).get(c,-1),V.get(r,{}).get(c,-1)
            if z not in seen:
                assert len(seen)<100000
                seen.add(z);todo.append((*z,w+str(c)))
    return {'equal':True,'product_states':len(seen)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--packet',type=Path,required=True)
    p.add_argument('--certificate',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();J=json.loads(a.certificate.read_text());out={}
    assert compare({0:{2:0}},{0:{2:1},1:{2:1}})['equal']
    assert compare({0:{2:0}},{0:{2:1},1:{}})['word']=='22'
    for w in (38,39,40,41):
        path=a.packet/'dfa2'/f'dfa_xx_W{w}_c0.txt';T=parse(path);r=J['widths'][str(w)]
        assert hashlib.sha256(path.read_bytes()).hexdigest()==r['input_sha256']
        r['width']=w;certificate(T,r)
        mutant=copy.deepcopy(r);mutant['raw_orbits'][str(r['initial_raw'])]['dest'][4]=-1
        try:certificate(T,mutant)
        except AssertionError:pass
        else:raise AssertionError('mutated certificate accepted')
        G,n=grammar(6 if w==38 else 7)
        result=compare(T,G)
        out[w]={'certificate_pass':True,'mutant_rejected':True,'factor_comparison':result,
                'grammar_nfa_states':n,'grammar_dfa_states':len(G)}
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/'factor-check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':main()
