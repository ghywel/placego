#!/usr/bin/env python3
"""B60/MI141, prereg3daf5e21: uniform four cancelling-gap construction.

Same2380 gap multisets/945 E28 corollaries as B59, no domain growth.
Predict all new formulas succeed;21 matching capacities checked by independent
subset DP; retained monotone-root failure, deliberately broken assignments,
and tight(4,4,8,8) are controls. Five CPU seconds, no fallback or cap raise.
OUTCOME MI142: all2380 formulas,21 capacities,945 partitions/controls PASS;
CPU0.195547s. Artifact SHA256
2d5471ae91aa9be1415d25529d85260d4d00c79ea5ac592f5ebc0e4cc564f03f.
Hand candidate remains SKETCH pending independent carrying read; no L8 claim.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
import json
import time
from path_forest_unlike_pairs import Budget,good,greedy,materializations


def literal_matching(n,g):
    edges=[]
    for a in range(min(n,g)):
        path=list(range(a,n,g))
        edges.extend(zip(path[::2],path[1::2]))
    return edges


def reference_capacity(n,g):
    # Generic graph subset recurrence, independent of residue-path formula.
    adj=[{y for y in range(n) if abs(x-y)==g} for x in range(n)]
    @lru_cache(None)
    def dp(mask):
        if not mask:return 0
        bit=mask&-mask;x=bit.bit_length()-1;rest=mask^bit
        return max([dp(rest)]+[1+dp(rest^(1<<y)) for y in adj[x] if rest>>y&1])
    return dp((1<<n)-1)


def construct(gaps):
    assert len(gaps)==4 and list(gaps)==sorted(gaps)
    large=[i for i,g in enumerate(gaps) if g>=8]
    small=[i for i,g in enumerate(gaps) if g<=7]
    ell=len(large);out={};holes=set();trace=[]
    for j,i in enumerate(large,1):
        r=13-ell+j;l=27-r-gaps[i]
        assert 0<=l<=5+ell and l<14-ell and l not in holes
        holes.add(l);out[i]=(l,27-r)
    used=set(holes);n=14-ell
    if ell==0:
        for i in small:
            x=next(x for x in range(14) if x not in used)
            y=x+gaps[i]
            assert y<=13 and y not in used
            out[i]=(x,y);used.update((x,y))
        branch='low-half'
    elif ell==4:branch='all-large'
    elif ell==1 and all(gaps[i] in (4,5) for i in small):
        base=[(j,j+gaps[i]) for j,i in enumerate(small)]
        points={x for e in base for x in e};d=max(points)
        assert len(points)==6 and 0 in points and 3 not in points and d in (6,7)
        c=next(c for c in range(13-d) if not {x+c for x in points}&holes)
        for i,(x,y) in zip(small,base):out[i]=(c+x,c+y)
        branch='compact-weak'
    else:
        order=list(small)
        if ell==2:order.sort(key=lambda i:gaps[i]!=4)
        if ell==1:
            strong=next(i for i in order if gaps[i] not in (4,5))
            order.remove(strong);order.append(strong)
        for j,i in enumerate(order):
            matching=literal_matching(n,gaps[i])
            residual=[e for e in matching if not set(e)&used]
            bound={3:[1],2:[2,1],1:[4,2,1]}[ell][j]
            assert len(residual)>=bound,(gaps,holes,used,residual,bound)
            trace.append(dict(gap=gaps[i],remaining=len(residual),lower_bound=bound))
            out[i]=residual[0];used.update(residual[0])
        branch='path-matchings'
    pairs=[out[i] for i in range(4)]
    assert good(gaps,pairs)
    return pairs,dict(large_count=ell,holes=sorted(holes),branch=branch,capacities=trace)


def controls():
    table={1:(5,6,6),2:(5,6,6),3:(5,6,6),4:(4,4,5),
           5:(5,5,5),6:(5,6,6),7:(4,5,6)}
    checked=[]
    for g,values in table.items():
        for n,value in zip((11,12,13),values):
            m=literal_matching(n,g)
            assert len({x for e in m for x in e})==2*len(m)
            assert all(y-x==g and 0<=x<y<n for x,y in m)
            assert len(m)==reference_capacity(n,g)==value
            checked.append((n,g,value))
    pairs,info=construct((4,4,4,14))
    assert info['holes']==[0] and {0,4,1,5,2,6}&set(info['holes'])
    badlow=[27-r-d for r,d in zip(range(10,14),(11,10,9,8))]
    assert len(set(badlow))==1
    monotone=greedy((3,11,13,14))
    assert [x for x,y in monotone]==[0,1,4,2]
    _,tight=construct((4,4,8,8))
    residual=[e for e in literal_matching(12,4) if not set(e)&set(tight['holes'])]
    assert tight['holes']==[6,7] and len(residual)==2
    return dict(capacity_table=checked,monotone_root_failure=monotone,
                tight_case=tight,tight_residual=residual,broken_controls='REJECTED')


def main():
    budget=Budget();checks=controls();rows=[];branches=Counter()
    for gaps in combinations_with_replacement(range(1,15),4):
        assert time.process_time()-budget.start<5 and len(rows)<2380
        pairs,trace=construct(gaps);branches[(trace['large_count'],trace['branch'])]+=1
        rows.append(dict(gaps=gaps,primary=pairs,construction=trace))
    assert len(rows)==2380
    certificates,counts=materializations(rows,budget)
    print(json.dumps(dict(status='FORMULA_VALIDATION',tested=len(rows),results=rows,
        branch_counts={str(k):v for k,v in branches.items()},controls=checks,
        corollary_certificates=certificates,corollary_counts=counts,
        cpu_seconds=time.process_time()-budget.start),indent=2))


if __name__=='__main__':main()
