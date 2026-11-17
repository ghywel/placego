#!/usr/bin/env python3
"""B90/MI205 prereg8349c2fa: arithmetic two-prefix exception audit.

Reuse frozen B89 DP20390 outcomes;12 named DP fixtures only.
2CPU sec/64MiB; no wider existence grid, repair or proof upgrade.
OUTCOME MI207:20390 frozen results agree;1250 constant/3125 one-exception/
16015 rich,560/330/0 unavoidable.3485 arithmetic orders checked;12 named
DP fixtures pass. CPU0.246513s,RSS34115584bytes. Artifact SHA256
81dac6e9ac30605b91d9ed47a870e026f21fad461619ca925d10ca1b4d41d553.
MI206's uniform classification remains SKETCH with MI204 dependency.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import resource
import time

import two_prefix_obstruction as control


def interval_order(r,s,t,x,y):
    lo=0;hi=r
    for z in (x,y):
        if z%s==0 and 1<=z//s<=r:hi=min(hi,z//s-1)
        if (z-t)%s==0 and 0<=(z-t)//s<=r-1:lo=max(lo,(z-t)//s+1)
    if lo>hi:return None,lo,hi
    return [s]*lo+[t]+[s]*(r-lo),lo,hi


def classify(d,x,y):
    counts=Counter(d);s,r=counts.most_common(1)[0];m=len(d)
    if r==m:
        bad=x%s==0 or y%s==0
        return 'constant',bad,None if bad else list(d),None
    if r==m-1:
        t=next(v for v in d if v!=s)
        bad=x%s==0 and (y-x-t)%s==0
        order,lo,hi=interval_order(r,s,t,x,y)
        return 'one_exception',bad,order,(lo,hi)
    return 'rich',False,None,None


def literal(d,x,y,order):
    assert Counter(order)==Counter(d)
    prefix=0
    for v in order[:-1]:
        prefix+=v;assert prefix not in (x,y)


def main():
    start=time.process_time();source=Path('/tmp/math-instinct-b89-two-prefix.json')
    raw=source.read_bytes();digest=hashlib.sha256(raw).hexdigest()
    assert digest=='d03fa79ad13689666e37c6e57084601244b57d2196c45959a410bd8c6de304b5'
    prior=json.loads(raw);assert prior['status']=='H2_SURVIVES_FIXED_DOMAIN'
    counts=Counter();traps=Counter();rows=[];constructed=0
    for row in prior['rows']:
        d,x,y=row['d'],row['x'],row['y'];assert 0<x<y<sum(d) and y-x>=max(d)
        kind,bad,order,bounds=classify(d,x,y)
        assert bad==(row['order'] is None),(row,kind,bad,bounds)
        if kind!='rich':
            assert (order is None)==bad
            if order:literal(d,x,y,order);constructed+=1
        else:literal(d,x,y,row['order'])
        counts[kind]+=1;traps[kind]+=bad
        rows.append(dict(d=d,x=x,y=y,kind=kind,unavoidable=bad,arithmetic_order=order,k_interval=bounds))
    assert len(rows)==20390 and counts['constant']+counts['one_exception']==4375
    fixtures=[(2,1,3,1,4),(3,3,2,2,6),(4,5,2,5,12),(4,5,2,2,10),
              (5,2,7,2,9),(5,2,7,1,8),(3,3,6,3,9),(3,3,6,2,8),
              (6,4,3,4,11),(6,4,3,3,12),(2,7,1,1,14),(2,1,3,1,2)]
    checks=[]
    for i,(r,s,t,x,y) in enumerate(fixtures):
        d=[s]*r+[t];kind,bad,order,bounds=classify(d,x,y)
        oracle,_=control.reachable(d,x,y)
        assert bool(order)==bool(oracle),(i,d,x,y)
        if order:literal(d,x,y,order)
        if i<11:
            assert y-x>=max(d) and bad==(oracle is None)
        else:
            assert y-x<max(d) and bad and order is not None and oracle is not None
        checks.append(dict(r=r,s=s,t=t,x=x,y=y,separation_valid=y-x>=max(d),
                           congruence_unavoidable=bad,order=order,k_interval=bounds))
    assert checks[1]['k_interval']==(1,1) and checks[1]['order']==[3,2,3,3]
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='8349c2fa',
                         reused_artifact_sha256=digest,questions=len(rows),class_questions=counts,
                         class_unavoidable=traps,arithmetic_orders=constructed,controls=checks,
                         rows=rows,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
