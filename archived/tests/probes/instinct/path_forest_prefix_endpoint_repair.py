#!/usr/bin/env python3
"""B45/MI106, preregistered fc1e9f47.

W21,Z2,v7,u6/7, sorted three surpluses with B=a+b in5/6. Predict7 fixed
one-before/two-after witnesses, exact independent stripe domain. Prior
1476 witnesses recheck plus two missing equals original1478. No larger
cycle or target search. Downshift, wrong sums and B4 countercontrol fail.
Cap10 new targets/one CPU second including existing-certificate recheck.
OUTCOME: all7 fixed stripe witnesses pass; prior1476 unchanged plus two
missing targets equal original1478 domain. Downshift/wrong-sums/B4
countercontrols reject. CPU0.130838 s. Raw outside git SHA256
833895ffcbfe85b3a4c0502ef9eea476e8f0ca9ae302cebd1dd664059ff12908.
Finite regime COMPUTED; no hand proof of universal all-after availability.
Original all-after failures retained.
"""
from collections import Counter
from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path
import time
from path_forest_prefix_compatibility import parameters
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def construct(u,a,b,c,force=None):
    q=a+b+c;B=a+b;assert q==16-u
    selected={5:1,6:1+a,1:B+1,3:B+8,0:B+6,7:B+6+u,2:22}
    if force=='down':selected={i:x-1 for i,x in selected.items()}
    target=(56+2*u,70,70,108,112,112+2*a,112+2*b,112+2*c)
    witness=materialize(target,selected);assert certificate_ok(witness['bins'],target)
    return dict(params=(u,7,21,2,a,b,c),targets=target,selected=selected,witness=witness)


def main():
    start=time.process_time();p=Path('/tmp/math-instinct-b44-prefix-compatibility.json');raw=p.read_bytes()
    previous=json.loads(raw);assert previous['total']==1478 and previous['certified']==1476
    params=[(u,a,b,c) for u in (6,7) for a,b,c in combinations_with_replacement(range(1,6),3)
            if a+b+c==16-u and a+b in (5,6)]
    assert len(params)==7
    direct={(56+2*u,70,70,108,112)+high for u in (6,7)
            for high in combinations_with_replacement(range(114,123,2),3)
            if sum((56+2*u,70,70,108,112)+high)==784 and sum((x-112)//2 for x in high[:2]) in (5,6)}
    results=[]
    for p in params:
        assert len(results)<10 and time.process_time()-start<1
        results.append(construct(*p))
    assert {tuple(x['targets']) for x in results}==direct
    for p,force in (((6,2,4,4),'down'),((7,1,3,5),None)):
        try:construct(*p,force=force)
        except ValueError as ex:assert str(ex)=='complementary pair reused'
        else:raise AssertionError('counterfactual accepted')
    sample=results[0];bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    union={tuple(x['targets']) for x in results}
    for x in previous['results']:
        if 'chosen' not in x:continue
        assert certificate_ok(x['chosen']['witness']['bins'],x['targets']);union.add(tuple(x['targets']))
    assert union==set(parameters()) and len(union)==1478
    old_missing={tuple(x['targets']) for x in previous['failures']}
    assert old_missing<={tuple(x['targets']) for x in results}
    assert time.process_time()-start<1
    print(json.dumps(dict(status='ALL_1478_WITH_FIXED_REPAIR',stripe=results,
        old_certificates=1476,added_missing=2,controls='PASS',
        source_sha256=hashlib.sha256(raw).hexdigest(),
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
