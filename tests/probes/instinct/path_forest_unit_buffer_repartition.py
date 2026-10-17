#!/usr/bin/env python3
"""B127/MI274 local audit: canonical C(s) plus ANY disjoint triple T, sum s+2.

Predict a4/6 equal-sum repartition at s+1, with1 kept in the6-bin, for all
s69..97 odd. Full LOCAL domain only:15*choose(21,3)=19950 triples screened;
not a q6-target census. Primary two exchange types; independent literal
all4-subset reference and separate raw-domain loops. Wrong source/sum/
intersection/duplicates reject. Unexpected valid equal-sum partition that
loses retained1 must fail. Caps2CPU s/64MiB/20k screens/1M reference subsets.
First failure stops;no repairs, larger domain or original-target search.
OUTCOME MI275:562/562 local triples pass,118020 reference subsets,all controls;
CPU0.07785s/RSS12021760bytes;hand candidate remains unreviewed. Raw local SHA256
86e5a93e3a0cf72ad2504b4297d3e90b3f624f20d2c890f2c2fee87b9babeaea.
"""
from collections import Counter
from itertools import combinations
import json
import resource
import sys
import time

START=time.process_time()
SCREENS=0
REFS=0


def budget():
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':rss*=1024
    if time.process_time()-START>2 or rss>64*1024*1024 or SCREENS>20000 or REFS>1000000:
        raise RuntimeError('cap')


def canonical(s):
    if s not in range(69,98,2):raise ValueError('source range')
    C=(1,3,5,7,9,11,s-36) if s<=91 else (1,3,5,7,9,s-80,55)
    assert len(set(C))==7 and sum(C)==s
    return tuple(sorted(C))


def construct(s,T):
    C=canonical(s)
    if len(T)!=3 or len(set(T))!=3 or set(T)&set(C) or sum(T)!=s+2:
        raise ValueError('triple hypothesis')
    if any(x not in range(1,56,2) for x in T):raise ValueError('token range')
    freeC=tuple(x for x in C if x!=1)
    for x in T:
        for pair in combinations(freeC,2):
            if sum(pair)==x-1:
                U=tuple(sorted(tuple(y for y in T if y!=x)+pair))
                W=tuple(sorted((set(C)|set(T))-set(U)))
                return U,W,'two_C_two_T'
        for triple in combinations(freeC,3):
            if sum(triple)+x==s+1:
                U=tuple(sorted((x,)+triple))
                W=tuple(sorted((set(C)|set(T))-set(U)))
                return U,W,'three_C_one_T'
    return None


def literal(s,C,T,U,W):
    return (len(U)==4 and len(W)==6 and 1 in W and
            sum(U)==sum(W)==s+1 and
            Counter(U+W)==Counter(C+T))


def reference(s,C,T):
    global REFS
    out=set();pool=tuple(sorted(C+T))
    for sub in combinations(pool,4):
        REFS+=1
        if 1 not in sub and sum(sub)==s+1:out.add(sub)
    budget();return out


def controls():
    s=69;C=canonical(s);T=(13,23,35)
    U=(1,11,23,35);W=tuple(sorted((set(C)|set(T))-set(U)))
    assert len(U)==4 and len(W)==6 and sum(U)==sum(W)==70
    assert Counter(U+W)==Counter(C+T) and not literal(s,C,T,U,W)
    ans=construct(s,T);assert ans and literal(s,C,T,ans[0],ans[1])
    for source,triple in ((67,T),(69,(13,23,37)),(69,(13,13,45)),(69,(1,15,55))):
        try:construct(source,triple)
        except ValueError:pass
        else:raise AssertionError('bad hypothesis accepted')
    return dict(valid_equal_sums_without_retained1_rejected=True,
                source_sum_duplicate_intersection_controls=True)


def main():
    global SCREENS
    out={'status':'ERROR'};rows=[];counts={};types=Counter()
    try:
        out['controls']=controls()
        for s in range(69,98,2):
            C=canonical(s);pool=tuple(x for x in range(1,56,2) if x not in C)
            domain=set()
            for T in combinations(pool,3):
                SCREENS+=1;budget()
                if sum(T)==s+2:domain.add(T)
            # Literal nested-loop generator: no cardinality/sum catalogue.
            raw=set()
            for x in range(1,56,2):
                for y in range(x+2,56,2):
                    for z in range(y+2,56,2):
                        if x+y+z==s+2 and all(v not in C for v in (x,y,z)):raw.add((x,y,z))
            assert domain==raw
            counts[s]=len(domain)
            for T in sorted(domain):
                ans=construct(s,T)
                assert ans is not None,('first construction failure',s,T)
                U,W,kind=ans;assert literal(s,C,T,U,W)
                candidates=reference(s,C,T);assert U in candidates
                rows.append({'source':s,'triple':T,'four':U,'six':W,'kind':kind,
                             'independent_candidates':len(candidates)})
                types[kind]+=1
        assert SCREENS==19950
        out.update(status='COMPLETE_LOCAL_FORMULA_AUDIT',counts=counts,rows=rows,types=dict(types))
    except Exception as e:out.update(status='FAILED_OR_CAP',reason=repr(e),rows=rows)
    out.update(screened=SCREENS,reference_subsets=REFS,cpu_seconds=time.process_time()-START,
               peak_rss_native=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
    return 0 if out['status']=='COMPLETE_LOCAL_FORMULA_AUDIT' else 2


if __name__=='__main__':raise SystemExit(main())
