#!/usr/bin/env python3
"""B91/MI208 prereg460620c4: known Grasshopper completion application.

Two literal E28 partitions, frozen B87 residual pointer and ascending-order
collision control.1CPU sec/64MiB; no profile/order grid or existence solver.
Known theorem PRIOR-ART; new endpoint selection remains PROOF-SKETCH.
OUTCOME MI209:2 formula calls/2 E28 partitions pass; frozen residual
membership confirmed; ascending second-order bag valid but geometry rejects.
CPU0.015648s,RSS19415040bytes. Artifact SHA256
f01f4071caabbe8a04c213693b8cb160cde8e8a2284e040fe3d508ef60000871.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation


def main():
    start=time.process_time();d=[1,2,3,4,5,8];A=[0,5,13]
    prior_path=Path('/tmp/math-instinct-b87-admission-synthesis.json');raw=prior_path.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);match=next(v for v in prior['records'] if v['d']==d)
    assert not match['admissions'] and match['positive_pairs']==[[21,25],[23,23]]
    rows=[validation.validate(28,d,25,21,A,[1,2,4,7,11],0,True),
          validation.validate(28,d,23,23,A,[2,6,7,9,12],0,True)]
    assert rows[0]['positions']==[0,25,23,19,13,5,26,10]
    assert rows[1]['positions']==[0,23,15,13,9,3,26,10]
    badB=[2,3,5,8,12];xs,word=validation.physical(28,A,badB)
    assert Counter(word)==Counter((23,23,*(-2*v for v in d)))
    assert all(0<=x<28 for x in xs) and len(set(xs))==8
    assert set(A)&set(badB)=={5}
    assert not validation.literal(28,xs) and not validation.instrument.literal_geometry(28,set(),xs)
    assert 17 in xs and 10 in xs and 17+10==27
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='460620c4',
                         known_tool='IMO2009 C7 Variant2, distinct positive jumps',
                         source_artifact_sha256=digest,prior_residual=match,formula_calls=2,
                         E28_partitions=2,rows=rows,
                         ascending_second_control=dict(B=badB,positions=xs,word=word,
                                                       bag_valid=True,folded_geometry_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
