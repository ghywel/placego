#!/usr/bin/env python3
"""B41/MI097, preregistered 485f7995.

One fixed allocation-flip repair for B40's only failure. Keep old71
witnesses; exact72-domain comparison. Trap both ends, wrong root and
coverage-preserving wrong sums rejected. Unexpected repaired span22.
One repair / one CPU second, no expanded domain or candidate search.
OUTCOME: one fixed repair certifies; old71 unchanged and complete72-domain
comparison passes, all controls pass; repaired span22. CPU0.004957 s.
Raw outside git SHA256
78084a40ec04e84135efa7b88bb6da00e46255434c6baa4c1b0aafaed187aa0a.
Original class failure retained. New classification/flip hand SKETCH.
"""
from collections import Counter
import hashlib
import json
import time
from pathlib import Path
from path_forest_two_ended_subdivision import domains
from path_forest_cycle_cover import materialize,setup
from path_forest_receiving_chains import certificate_ok


def main():
    start=time.process_time();p=Path('/tmp/math-instinct-b40-two-ended.json');data=p.read_bytes()
    source=json.loads(data)
    assert len(source['failures'])==1 and source['failures'][0]['params']==[6,6,21,6]
    target=(68,68,70,100,112,122,122,122)
    # The inherited -1 edge at6->5 has both outward +5 options occupied.
    base={0,5,6,11};assert 6+5 in base and 5-5 in base
    selected={0:0,3:6,1:1,5:7,6:12,7:17,2:22}
    witness=materialize(target,selected);assert certificate_ok(witness['bins'],target)
    assert max(selected.values())-min(selected.values())==22
    labels=[min(x,27-x) for x in selected.values()]
    assert len(set(labels))==7
    wrong=dict(selected)
    for i in (1,5,6,7,2):wrong[i]-=1
    try:materialize(target,wrong)
    except ValueError as ex:assert str(ex)=='complementary pair reused'
    else:raise AssertionError('omitted independent cycle root accepted')
    bins=[set(x) for x in witness['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,target)
    all_targets={target}
    for r in source['results']:
        if 'witness' not in r:continue
        t=tuple(r['targets']);assert certificate_ok(r['witness']['bins'],t);all_targets.add(t)
    assert all_targets==set(domains()) and len(all_targets)==72
    assert time.process_time()-start<1
    print(json.dumps(dict(status='ALL_72_WITH_ONE_FLIP',target=target,selected=selected,
        witness=witness,span=22,labels=labels,original_failure_retained=True,
        parent_sha256=hashlib.sha256(data).hexdigest(),controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
