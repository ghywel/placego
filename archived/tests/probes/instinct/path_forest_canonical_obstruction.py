#!/usr/bin/env python3
"""B103/MI232 prereg90e1fa99: canonical split can fail despite capacity.

One frozen profile;72 complete root/order cases under BOTH parity roles,
three explicit alternate E28 partitions,one scaled lattice check.
2CPU sec/64MiB. No broader scan/whole-cycle solver; general E28 remains open.
OUTCOME MI233:72 cases with0/6/6 canonical witnesses,3 alternative E28
partitions and scaled control pass;0.017423CPU sec/19972096RSS bytes.
Artifact SHA256c2d4738c551cc2426a0d1d73c378dcaa5d4d30d37a3f4864d9ec13c9d8be81ed.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_two_unit_triangle import partition


def prefix(x,gaps):
    out=[x]
    for gap in gaps:out.append(out[-1]+gap)
    return out


def alternate(p,q):
    d=[2,2,5,5,7];alpha=(27-max(p,q))//2;c=min(alpha,2)
    assert alpha in (1,2,3) and c in (alpha,alpha-1)
    preA=[c,c+2,c+9];preB=[0,5,7,12];A=preA;B=preB
    first=0 if p>=q else 1;reflected=c==alpha-1
    if reflected:
        A=[13-v for v in reversed(A)];B=[13-v for v in reversed(B)];first=1-first
    row=validation.validate(28,d,p,q,A,B,first,False)
    row.update(M=28,d=d,p=p,q=q,alpha=alpha,root=c,preA=preA,preB=preB,reflected=reflected)
    return row


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);d=[2,2,5,5,7];pairs=[[17,25],[19,23],[21,21]]
    rec=next(v for v in prior['residual'] if v['d']==d)
    assert not rec['admissions'] and rec['positive_pairs']==pairs
    three_orders=sorted(set(permutations((2,2,7))))
    manual_shapes=[[0,2,4,11],[0,2,9,11],[0,7,9,11]]
    assert [prefix(0,v) for v in three_orders]==manual_shapes
    rows=[];by_pair={tuple(pair):dict(candidates=0,valid=0) for pair in pairs};offset_maps=[]
    role_specs=[('two_in_A',(5,5),(2,2,7),{-2,-1,0,1}),
                ('three_in_A',(2,2,7),(5,5),{-1,0,1,2})]
    for role,Agaps,Bgaps,bad in role_specs:
        X=13-sum(Agaps);Y=13-sum(Bgaps);offsets={};role_rows=[]
        for x in range(X+1):
            for y in range(Y+1):
                for ao,bo in product(sorted(set(permutations(Agaps))),sorted(set(permutations(Bgaps)))):
                    A=prefix(x,ao);B=prefix(y,bo);z=y-x;xs,word=validation.physical(28,A,B)
                    direct=not set(A)&set(B)
                    assert validation.literal(28,xs)==direct
                    assert validation.instrument.literal_geometry(28,set(),xs)==direct
                    assert direct==(z not in bad)
                    assert len(set(xs))==7 and all(0<=v<28 for v in xs)
                    P=word[0];Q=word[len(B)]
                    assert P>0 and Q>0 and P%2 and Q%2
                    assert Counter(word)==Counter((P,Q,*(-2*v for v in d)))
                    key=tuple(sorted((P,Q)))
                    if key in by_pair:
                        by_pair[key]['candidates']+=1;by_pair[key]['valid']+=direct
                    offsets.setdefault(z,[]).append(direct)
                    rr=dict(role=role,x=x,y=y,z=z,A=A,B=B,positions=xs,word=word,valid=direct)
                    rows.append(rr);role_rows.append(rr)
        assert len(role_rows)==36
        assert {z for z,vals in offsets.items() if not any(vals)}==bad
        assert set(offsets)==set(range(-X,Y+1))
        offset_maps.append(dict(role=role,X=X,Y=Y,universal_bad=sorted(bad),
                                valid_offsets=sorted(z for z,vals in offsets.items() if any(vals))))
    assert len(rows)==72
    assert [by_pair[tuple(v)]['candidates'] for v in pairs]==[18,30,18]
    assert [by_pair[tuple(v)]['valid'] for v in pairs]==[0,6,6]
    alternate_rows=[alternate(p,q) for p,q in pairs]
    partitions=[partition(v) for v in alternate_rows]
    reflected=alternate_rows[2];assert reflected['reflected']
    prexs,preword=validation.physical(28,reflected['preA'],reflected['preB'])
    assert validation.literal(28,prexs) and validation.instrument.literal_geometry(28,set(),prexs)
    assert (preword[0],preword[len(reflected['preB'])])==(23,19)
    assert Counter(preword)!=Counter((21,21,-4,-4,-10,-10,-14))
    badA=[1,6,11];badB=[0,7,9,11];badxs,badword=validation.physical(28,badA,badB)
    assert Counter(badword)==Counter((17,25,-4,-4,-10,-10,-14))
    assert set(badA)&set(badB)=={11} and len(set(badxs))==7 and all(0<=v<28 for v in badxs)
    assert not validation.literal(28,badxs) and not validation.instrument.literal_geometry(28,set(),badxs)
    scaled=validation.validate(54,[4,4,10,10,14],33,51,[0,10,20],[1,5,9,23],1,False)
    assert 20*13==10*26 and 22*13==11*26
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='90e1fa99',
                         input_sha256=digest,frozen_profile=rec,canonical_cases=72,
                         pair_maps=[dict(p=p,q=q,**by_pair[(p,q)]) for p,q in pairs],
                         offset_maps=offset_maps,canonical_rows=rows,
                         alternative_formula_calls=3,E28_partitions=3,
                         alternative_rows=alternate_rows,partitions=partitions,
                         omitted_reflection=dict(positions=prexs,word=preword,geometry_valid=True,
                                                 original_bag_valid=False),
                         naive_canonical=dict(A=badA,B=badB,positions=badxs,word=badword,
                                              original_bag_valid=True,folded_valid=False),
                         scaled_lattice_control=scaled,cpu_seconds=elapsed,peak_rss_bytes=rss),
                     separators=(',',':')))


if __name__=='__main__':main()
