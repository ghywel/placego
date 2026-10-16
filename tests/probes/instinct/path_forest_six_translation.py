#!/usr/bin/env python3
"""B36/MI087: sharp six-position translation, preregistered 1be3bc90.

Predict all distinct <=6-point shapes of span <=20 embed in 0..27 without
complementary pair reuse. Count D=19,20 boundary shapes, <10,000/five CPU
seconds. Independent direct folded labels vs blocked pair-sum roots.
Sharp span21 fixture fails; every one-point deletion passes. Repeated
positions and out-of-pool roots are rejected. No E28 target census.
OUTCOME: 9,084 boundary shapes pass (6,936 with six points); pair-sum and
direct-label roots agree, all controls pass, sharp span21 has no root and
all six one-point deletions do. CPU 0.147453 s. Raw outside git SHA256
d4c70d628510834a5930b78bc24a3f714b7303d250afdafc853bb5c0310ca1a5.
Hand argument PROOF-SKETCH; finite boundary checks COMPUTED.
"""
from itertools import combinations
import json
import time


def direct(points, root):
    positions=[root+x for x in points]
    if not positions or min(positions)<0 or max(positions)>27:return False
    labels=[min(x,27-x) for x in positions]
    return len(set(labels))==len(labels)


def roots(points):
    if len(points)!=len(set(points)):return []
    s=tuple(x-min(points) for x in points)
    return [r for r in range(28-max(s)) if direct(s,r)]


def sum_roots(points):
    if len(points)!=len(set(points)):return []
    s=tuple(x-min(points) for x in points)
    blocked={(27-x-y)//2 for x,y in combinations(s,2) if (x+y)%2}
    return [r for r in range(28-max(s)) if r not in blocked]


def main():
    start=time.process_time();counts={};results=[]
    for D in (19,20):
        for k in range(2,7):
            n=0
            for inner in combinations(range(1,D),k-2):
                if len(results)>=10000 or time.process_time()-start>=5:
                    print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
                s=(0,)+inner+(D,);a,b=roots(s),sum_roots(s)
                assert a==b and a,(s,a,b)
                results.append(dict(shape=s,roots=a));n+=1
            counts[f'{D}:{k}']=n
    assert counts['19:6']==3060 and counts['20:6']==3876
    for s in ((0,), (0,1,2,3,4,18),(0,2,4,6,8,18),(0,1,5,11,15,17)):
        assert roots(s)==sum_roots(s) and roots(s)
    sharp=(0,2,6,15,19,21)
    assert roots(sharp)==sum_roots(sharp)==[]
    deletion_roots=[]
    for i in range(6):
        s=sharp[:i]+sharp[i+1:];r=roots(s)
        assert r==sum_roots(s) and r
        deletion_roots.append(dict(deleted=sharp[i],roots=r))
    assert roots((0,0,1))==[] and not direct((0,0,1),0)
    assert not direct((0,20),8) and not direct((0,20),-1)
    print(json.dumps(dict(status='BOUNDARY_ALL',counts=counts,results=results,
        sharp=sharp,sharp_roots=[],deletions=deletion_roots,
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
