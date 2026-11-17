#!/usr/bin/env python3
"""B72/MI165 prereg3bfd9c29: formula allocation for b+4c and two122 bins.

All2002 labelled compositions of9 into6. Formula only; no slot/order search.
Independent stars-bars parameter set, coefficient counts,32-subset grouping
reference, literal reflection and two partition validators.10CPU sec/128MiB.
Proof is MI165 SKETCH; finite certificates do not upgrade its review status.
OUTCOME:2002/2002 pass;1994 labelled E28 assignments/677 distinct sorted
targets. Controls pass, six empty-outer extremes included.0.375130CPU sec,
23060480bytes RSS. Raw SHA256
373c303825209bd5f795c9d353588b7775d46376316335aa6bce918e96efc5b3.
"""
from collections import Counter
from itertools import combinations
import json
import resource
import time

import path_forest_odd_bridge as bridge
import path_forest_split_anchor_pilot as pilot

BASE=(77,79,81,87,89,91)
ANCHORS=(21,23,25,31,33,35,0,0)
RESERVED={10,11,12}


def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for first in range(n+1):
            for rest in compositions(n-first,k-1):
                yield (first,*rest)


def star_bar_reference():
    result=set()
    for bars in combinations(range(14),5):
        marks=(-1,*bars,14)
        result.add(tuple(marks[i+1]-marks[i]-1 for i in range(6)))
    return result


def coefficient_count(bounds):
    counts=[1]+[0]*9
    for bound in bounds:
        nxt=[0]*10
        for degree,value in enumerate(counts):
            for part in range(min(bound,9-degree)+1):
                nxt[degree+part]+=value
        counts=nxt
    return counts[9]


def formula(c):
    assert len(c)==6 and min(c)>=0 and sum(c)==9
    m=max(c);j=c.index(m)
    rest=[i for i in range(6) if i!=j]
    if m>=5:
        A=rest
    elif m==4:
        A=[next(i for i in rest if c[i]>0)]
    elif m==3:
        threes=[i for i in rest if c[i]==3]
        A=[threes[0] if threes else next(i for i in rest if c[i]==2)]
    else:
        assert m==2
        A=[i for i in rest if c[i]==2][:2]
        assert len(A)==2
    B=[i for i in rest if i not in A]
    s=sum(c[i] for i in A);t=sum(c[i] for i in B)
    assert s<=4 and t<=4
    # Reference is only an audit: the formula above does not use its answer.
    good_masks=[mask for mask in range(32)
                if sum(c[i] for k,i in enumerate(rest) if mask>>k&1)<=4
                and sum(c[i] for k,i in enumerate(rest) if not(mask>>k&1))<=4]
    chosen=sum(1<<rest.index(i) for i in A)
    assert chosen in good_masks
    left=[i for i in A if c[i]>0];right=[i for i in B if c[i]>0]
    geometry=bridge.construct(28,10,3,8-2*s,tuple(2*c[i] for i in left),5,5,
                              tuple(2*c[i] for i in right))
    owners=(*left,6,7,*right,j)
    selected=dict(zip(owners,geometry['positions']))
    targets=tuple(BASE[i]+4*c[i] for i in range(6))+(122,122)
    h=[1]*6+[2,2];h[j]=2
    moves=[(v-a-56*n)//2 for v,a,n in zip(targets,ANCHORS,h)]
    assert moves[j]==-(28-2*m) and moves[6:]==[5,5]
    assert all(moves[i]==2*c[i] for i in rest)
    assert sum(targets)==784 and sum(moves)==0
    assert set(selected)=={i for i,e in enumerate(moves) if e}
    assert all(selected[i]+moves[i]==geometry['positions'][(k+1)%len(owners)]
               for k,i in enumerate(owners))
    assert bridge.literal(list(selected.values()),28,RESERVED)
    bins=pilot.materialize(targets,RESERVED,ANCHORS,h,selected)
    assert pilot.literal_ok(bins,targets,h) and pilot.independent_ok(bins,targets)
    order=sorted(range(8),key=lambda i:(targets[i],i))
    st=[targets[i] for i in order];sb=[bins[i] for i in order];sh=[h[i] for i in order]
    assert pilot.literal_ok(sb,st,sh) and pilot.independent_ok(sb,st)
    inside=all(v<=121 for v in targets[:6])
    assert inside==(min(st)>=68 and max(st)<=122)
    return dict(parameters=c,targets=targets,slots=h,moves=moves,negative_owner=j,
                before_owners=left,after_owners=right,selected=selected,bins=bins,
                sorted_targets=st,sorted_bins=sb,sorted_slots=sh,in_E28=inside,
                root=8-2*s,centre=geometry['centre'],group_sums=(s,t))


def controls(row):
    c=(2,2,2,1,1,1);j=c.index(max(c));all_before=sum(c[i] for i in range(6) if i!=j)
    assert all_before==7 and 8-2*all_before==-6
    try:bridge.construct(28,10,3,-6,(4,4,2,2,2),5,5,())
    except AssertionError:pass
    else:raise AssertionError('negative root accepted')
    bins=row['bins'];targets=row['targets'];h=row['slots']
    bad=[list(b) for b in bins];bad[0][0]=bad[1][0]
    assert not pilot.literal_ok(bad,targets,h) and not pilot.independent_ok(bad,targets)
    bad=[list(b) for b in bins];bad[0][0],bad[1][0]=bad[1][0],bad[0][0]
    assert sorted(x for b in bad for x in b)==list(range(1,56,2))
    assert not pilot.literal_ok(bad,targets,h) and not pilot.independent_ok(bad,targets)
    return dict(all_before_invalid_root=-6,duplicate_token='REJECTED',
                inventory_preserving_wrong_sums='REJECTED')


def main():
    start=time.process_time();params=list(compositions(9,6))
    assert len(params)==len(set(params))==2002
    assert set(params)==star_bar_reference()
    assert coefficient_count([9]*6)==2002
    bounds=[(121-b)//4 for b in BASE]
    assert bounds==[11,10,10,8,8,7] and coefficient_count(bounds)==1994
    rows=[]
    for c in params:
        rows.append(formula(c))
        assert time.process_time()-start<10
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<128*1024*1024
    inside=[r for r in rows if r['in_E28']];outside=[r for r in rows if not r['in_E28']]
    assert len(inside)==1994 and len(outside)==8
    assert {r['parameters'] for r in inside}=={c for c in params if all(v<=b for v,b in zip(c,bounds))}
    empty=[r for r in rows if max(r['parameters'])==9]
    assert len(empty)==6 and all(not r['before_owners'] and not r['after_owners'] for r in empty)
    assert all(len(r['selected'])==3 and sorted(r['moves'])==[-10,0,0,0,0,0,5,5] for r in empty)
    cf=next(r for r in rows if r['parameters']==(2,2,2,1,1,1))
    control_result=controls(cf)
    distinct={tuple(r['sorted_targets']) for r in inside}
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_FORMULA_CERTIFICATES_PASS',preregistration='3bfd9c29',
                         labelled_parameters=len(rows),labelled_E28=len(inside),outside_E28=len(outside),
                         distinct_sorted_E28=len(distinct),maximum_histogram=dict(sorted(Counter(max(c) for c in params).items())),
                         independent_checks='complete parameter sets/count DP/32-subset reference/dual partition validators',
                         controls=control_result,empty_outer_cases=6,rows=rows,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
