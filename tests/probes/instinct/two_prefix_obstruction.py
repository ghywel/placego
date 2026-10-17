#!/usr/bin/env python3
"""B89/MI202 preregde13924c: two-prefix obstruction shape H2.

Steps length3..7,values1..4; proper barriers separated>=max step.
100000 questions,10CPU sec/128MiB. Stop first rich unavoidable pair,
no repair or enlarged grid. Independent permutations for length<=5.
OUTCOME MI203: H2 survives20390 questions,16015 rich;890 unavoidable,
all nearly constant.3165 independent comparisons/3 controls pass.
CPU1.505551s,RSS18427904bytes. Artifact SHA256
 d03fa79ad13689666e37c6e57084601244b57d2196c45959a410bd8c6de304b5.
MI204 supplies a separate uniform hand PROOF-SKETCH, not an extrapolation.
"""
from collections import Counter
from itertools import combinations_with_replacement,permutations
import json
import resource
import time


def sums_for(d):
    sums=[0]*(1<<len(d))
    for mask in range(1,len(sums)):
        bit=mask&-mask;j=bit.bit_length()-1
        sums[mask]=sums[mask^bit]+d[j]
    return sums


def reachable(d,x,y,sums=None):
    if sums is None:sums=sums_for(d)
    full=(1<<len(d))-1;parents={0:None}
    for mask in range(full+1):
        if mask not in parents:continue
        for j in range(len(d)):
            if (mask>>j)&1:continue
            new=mask|(1<<j)
            if sums[new] in (x,y) or new in parents:continue
            parents[new]=(mask,j)
    if full not in parents:return None,sorted(parents)
    order=[];mask=full
    while mask:
        prior,j=parents[mask];order.append(d[j]);mask=prior
    order.reverse()
    assert Counter(order)==Counter(d)
    prefix=0
    for v in order[:-1]:
        prefix+=v;assert prefix not in (x,y)
    return order,sorted(parents)


def literal_permutation(d,x,y):
    for order in sorted(set(permutations(d))):
        prefix=0;bad=False
        for v in order[:-1]:
            prefix+=v
            if prefix==x or prefix==y:bad=True;break
        if not bad:return list(order)
    return None


def main():
    start=time.process_time();rows=[];independent=0;rich=0;traps=0
    controls=[]
    for d,x,y,expect in (((1,1,2),1,3,False),((1,1,2,2),2,3,False),((1,1,2,2),1,3,True)):
        order,_=reachable(d,x,y);oracle=literal_permutation(d,x,y)
        assert bool(order)==bool(oracle)==expect
        controls.append(dict(d=d,x=x,y=y,exists=expect,order=order))
    for m in range(3,8):
        for d in combinations_with_replacement(range(1,5),m):
            S=sum(d);largest=max(d);sums=sums_for(d);near=max(Counter(d).values())>=m-1
            for x in range(1,S):
                for y in range(x+largest,S):
                    order,masks=reachable(d,x,y,sums)
                    if m<=5:
                        oracle=literal_permutation(d,x,y);independent+=1
                        assert bool(order)==bool(oracle),(d,x,y,'independent mismatch')
                    row=dict(d=d,x=x,y=y,near_constant=near,order=order)
                    rows.append(row);rich+=not near;traps+=not bool(order)
                    assert len(rows)<=100000 and time.process_time()-start<10
                    if order is None and not near:
                        assert literal_permutation(d,x,y) is None
                        print(json.dumps(dict(status='FIRST_H2_COUNTEREXAMPLE',preregistration='de13924c',
                                              counterexample=row,reachable_masks=masks,subset_sums=sums,
                                              questions=len(rows),independent_checks=independent,
                                              controls=controls,rows=rows,cpu_seconds=time.process_time()-start,
                                              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),separators=(',',':')))
                        return
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='H2_SURVIVES_FIXED_DOMAIN',preregistration='de13924c',questions=len(rows),
                         independent_checks=independent,rich_questions=rich,unavoidable_pairs=traps,
                         controls=controls,rows=rows,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
