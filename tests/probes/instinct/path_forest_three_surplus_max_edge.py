#!/usr/bin/env python3
"""B43/MI101 W22 three-surplus boundary, preregistered e598c441.

W22 forces u=v6, q11..15,Z=q-10. Predict11 targets with q counts4/3/2/1/1,
independent sorted-target domain. One7-cycle, prescribed order/root formula;
all literal certificates. Root0 q11 and sorted-root1 (3,3,5) fail. Wrong
sums rejected. Unexpected (4,4,4) allows all six roots by parity. Cap20
inputs/one CPU second, no order search or widened unmatched family.
OUTCOME: all11 formula certificates pass, exact direct-target set agrees,
q counts4/3/2/1/1, both bad-root/order and wrong-sum controls fail as
predicted. All six roots work for even fixture. CPU0.001306 s.
Raw outside git SHA256
34293beaf38b5cee6559cb376daa1ad09e0b0894088a824e26f97ab539c1cef8.
Uniform hand argument PROOF-SKETCH, finite witnesses COMPUTED.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_six_translation import roots


def construct(steps,force=None):
    a,b,c=steps;q=a+b+c;Z=q-10;A=16-q;R=22-q
    assert 11<=q<=15
    order=list(enumerate(steps,start=5));r=0
    if q==11:
        if a<=2:r=1
        else:
            last=next(i for i,value in order if value==3)
            order=[(i,v) for i,v in order if i!=last]+[(last,3)];r=2
    elif q==12 and c==5:r=1
    if force=='root0':r=0
    if force=='sorted_root1':order=list(enumerate(steps,start=5));r=1
    selected={1:0,3:6,0:A};x=R
    for i,value in order:selected[i]=x;x+=value
    assert x==22;selected[2]=x
    target=(68,68,68,112-2*Z,112,112+2*a,112+2*b,112+2*c)
    witness=materialize(target,{i:x+r for i,x in selected.items()})
    assert certificate_ok(witness['bins'],target)
    return dict(steps=steps,targets=target,order=order,root=r,shape=selected,witness=witness)


def main():
    start=time.process_time()
    choices=[s for s in combinations_with_replacement(range(1,6),3) if sum(s)>10]
    assert len(choices)==11
    assert [sum(sum(s)==q for s in choices) for q in range(11,16)]==[4,3,2,1,1]
    direct={(68,68,68,t,112)+high
            for high in combinations_with_replacement(range(114,123,2),3)
            for t in range(68,111,2) if 3*68+t+112+sum(high)==784}
    results=[]
    for s in choices:
        assert len(results)<20 and time.process_time()-start<1
        results.append(construct(s))
    assert {tuple(r['targets']) for r in results}==direct
    for s,force in (((1,5,5),'root0'),((3,3,5),'sorted_root1')):
        try:construct(s,force=force)
        except ValueError as ex:assert str(ex)=='complementary pair reused'
        else:raise AssertionError('wrong root/order accepted')
    even=construct((4,4,4));assert all(x%2==0 for x in even['shape'].values())
    assert roots(tuple(even['shape'].values()))==list(range(6))
    sample=results[0];bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    print(json.dumps(dict(status='ALL_11_MAX_EDGE',results=results,controls='PASS',
        even_fixture_roots=list(range(6)),cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
