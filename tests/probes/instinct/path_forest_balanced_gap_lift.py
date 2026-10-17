#!/usr/bin/env python3
"""B125/MI271: audit a HAND-derived balanced triple gap-lifting formula.

All odd k1..15, ALL holes0..3k:200 formula checks, no existence search.
Primary explicit3-row magic formula; independent literal token/sum/floor-
ceiling checks, k7 fixed-table comparison, reflection and even-k rejection.
Also all15 balanced original-q8 fixtures, direct literal token validator.
Predicted all pass;2CPU sec/64MiB,first failure stops,no repairs/domain growth.
Known well-distributed magic equipartition context is PRIOR-ART; general
rank-gap corollary is a single-party hand argument, novelty unassessed.
"""
from collections import Counter
from pathlib import Path
import json
import resource
import sys
import time

START=time.process_time()


def check_budget():
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':rss*=1024
    if time.process_time()-START>2 or rss>64*1024*1024:raise RuntimeError('cap')


def magic(k):
    if k<1 or k%2==0:raise ValueError('positive odd column count required')
    m=(k-1)//2
    return [(i,k+(i+m)%k,2*k+3*m-i-(i+m)%k) for i in range(k)]


def lift(k,h):
    if not 0<=h<=3*k:raise ValueError('hole range')
    return [tuple(x+(x>=h) for x in row) for row in magic(k)]


def literal(k,h,rows):
    # No formula for sums or choice of columns enters this validator.
    assert len(rows)==k and all(len(r)==3 for r in rows)
    assert Counter(x for row in rows for x in row)==Counter(x for x in range(3*k+1) if x!=h)
    total=sum(x for x in range(3*k+1) if x!=h)
    small,larger=divmod(total,k)
    assert sorted(map(sum,rows))==[small]*(k-larger)+[small+1]*larger


def main():
    cases=0;endpoint=0
    # Fixed table not computed by magic(): independent check at our actual k7.
    table=[(0,10,20),(1,11,18),(2,12,16),(3,13,14),
           (4,7,19),(5,8,17),(6,9,15)]
    output={'status':'ERROR'}
    try:
        for k in range(1,16,2):
            base=magic(k);assert all(sum(row)==(9*k-3)//2 for row in base)
            assert all(len({row[j]//k for j in range(3)})==3 for row in base)
            for h in range(3*k+1):
                check_budget();rows=lift(k,h);literal(k,h,rows);cases+=1
                reflected=[tuple(3*k-x for x in row) for row in rows]
                literal(k,3*k-h,reflected)
                if h==3*k:assert rows==base;endpoint+=1
                if k==7:
                    fixed=[tuple(x+int(x>=h) for x in row) for row in table]
                    assert rows==fixed
        assert cases==200 and endpoint==8
        try:magic(6)
        except ValueError:pass
        else:raise AssertionError('even k accepted')
        try:lift(7,22)
        except ValueError:pass
        else:raise AssertionError('bad hole accepted')
        fixtures=[]
        for a in range(69,98,2):
            if a<=91:b=13;h=(a-49)//2;C=[1,3,5,7,9,11,a-36]
            else:b=11;h=(a-91)//2;C=[1,3,5,7,9,a-80,55]
            triples=[tuple(b+2*x for x in row) for row in lift(7,h)]
            triples.sort(key=sum);target=(a,)+tuple(map(sum,triples));bins=[C]+triples
            assert len(set(C))==7 and sum(C)==a
            assert tuple(sorted(target))==target and sum(target)==784
            assert min(target)>=69 and max(target)<=121 and all(t%2 for t in target)
            assert Counter(x for row in bins for x in row)==Counter(range(1,56,2))
            assert all(sum(row)==t for row,t in zip(bins,target))
            fixtures.append({'target':target,'bins':bins})
        assert len(fixtures)==15
        output.update(status='COMPLETE_FORMULA_AUDIT',formula_cases=cases,
                      reflection_cases=cases,k7_fixed_table_comparisons=22,
                      endpoint_cases=endpoint,even_k_rejected=True,bad_hole_rejected=True,
                      actual_q8_fixtures=fixtures)
    except Exception as e:output.update(status='FAILED_OR_CAP',reason=repr(e),completed=cases)
    output.update(cpu_seconds=time.process_time()-START,
                  peak_rss_native=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(output,sort_keys=True,separators=(',',':')))
    return 0 if output['status']=='COMPLETE_FORMULA_AUDIT' else 2


if __name__=='__main__':raise SystemExit(main())
