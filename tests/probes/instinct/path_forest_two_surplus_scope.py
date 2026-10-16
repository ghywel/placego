#!/usr/bin/env python3
"""MI091 synthesis audit, preregistered 7a62bc7c.

Existing B32/B34/B35/B38 artifacts should equal all even E28 targets with
t5=t6=112: 4,523 distinct targets. No new search. Literal certificates
rechecked, parameterized union compared to independent sorted-low domain.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_two_surplus_runway import core_target


def main():
    targets=set();digests={};counts={}
    for block,name in ((32,'two-surplus'),(34,'zero-surplus'),
                       (35,'one-surplus'),(38,'two-surplus-direct')):
        p=Path(f'/tmp/math-instinct-b{block}-{name}.json')
        data=p.read_bytes();d=json.loads(data);digests[p.name]=hashlib.sha256(data).hexdigest()
        before=len(targets)
        for r in d['results']:
            if block==32:
                t=core_target(*r['params'])
                witness=materialize(t,{int(i):x for i,x in r['selected'].items()})
            else:t=tuple(r['targets']);witness=r['witness']
            assert certificate_ok(witness['bins'],t)
            targets.add(t)
        counts[str(block)]=len(targets)-before
    assert len(targets)==4523
    low=defaultdict(list)
    for xs in combinations_with_replacement(range(68,113,2),4):low[sum(xs)].append(xs)
    direct=set();highcounts={}
    for a in range(6):
        for b in range(a,6):
            high=(112,112,112+2*a,112+2*b)
            family={xs+high for xs in low[784-sum(high)]}
            direct.update(family);highcounts[f'{a},{b}']=len(family)
    assert targets==direct
    old=sum(n for k,n in highcounts.items() if k.startswith('0,'))
    assert old==1538 and counts=={'32':122,'34':284,'35':1198,'38':2919}
    print(json.dumps(dict(status='EXACT_4523',count=len(targets),old_region=old,
        added_two_surplus=2919+66,component_counts=counts,highcounts=highcounts,
        artifact_sha256=digests,all_literal_certificates='PASS'),indent=2))


if __name__=='__main__':main()
