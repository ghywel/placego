#!/usr/bin/env python3
"""B56/MI130 preregistered5167e2b4: known-class reflection-aware choice.

Exactly30 B55 residuals. Interior first term, opposite sign to current sum
thereafter; no arbitrary order fallback. Prefix 28-bit translation pruning
versus independent complete multiset permutations/direct final labels.
Compare whole feasible-order/origin-mask maps. Primitive/range checks,
prefix mask and omitted-reflection controls, invalid-sign/nonprimitive,
duplicate/wrong-sum controls. Unexpected old-min-positive/negative starts.
Caps30 targets/250k nodes/2M raw perms/100k class orders/1M root checks/
10 CPU seconds incl complete certificate delivery audit. Preserve7798 old
witnesses unchanged; exact full7828 domain and residual set checked.
INSTRUMENT NOTE: first execution completed checks but failed at final
serialization: Python cannot sort mixed tuple/list target keys. Export
key normalized to tuple before unchanged rerun; no mathematics/cap change.
OUTCOME: all30 residuals have witnesses in the prescribed known class.
Complete feasible-order/origin maps agree:4775 accepted reference orders,
4208 feasible orders,9404 feasible order/origin pairs.15906 adaptive nodes,
1209600 raw reference permutations,123480 unique words,41203 direct roots.
All30 retain a possible smallest-positive start;20 also allow negative
interior starts. All7828 final partitions and exact independent full-domain
audit pass. CPU0.734438 s; full immutable certificate in shared store:
cited/instinct/b56-four-surplus-complete-8da086b17c026c33.json, SHA256
8da086b17c026c333f103bda3a2d629bf18ee4b91d381f174641ddc24010db49.
Full named four-surplus finite region COMPUTED; no full E28/L8 or general
reflection-avoidance theorem. Cloud check-in follows this block as requested.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json
import math
import sys
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok
from path_forest_factorization_audit import direct_domain

ALL=(1<<28)-1


class BudgetError(Exception):
    pass


class Budget:
    def __init__(self):
        self.start=time.process_time();self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        caps={'nodes':250000,'raw_permutations':2000000,'class_orders':100000,'root_checks':1000000}
        if (key in caps and self.counts[key]>caps[key]) or time.process_time()-self.start>10:
            raise BudgetError(key)
    def time(self):return time.process_time()-self.start


def moves(p):
    u,v,W,Z,steps=p
    return {0:u,1:v,2:-W,3:-Z,**{4+i:s for i,s in enumerate(steps)}}


def primitive(p):
    reachable=1
    for x in moves(p).values():
        if x>0:reachable|=reachable<<x
    return not reachable&(1<<p[2])


def range_mask(p):
    lo=max(0,-p);hi=min(27,27-p)
    return 0 if lo>hi else ((1<<(hi-lo+1))-1)<<lo


def extend(mask,p,earlier):
    if p in earlier:return 0
    mask&=range_mask(p)
    for q in earlier:
        numerator=27-p-q
        if numerator%2==0 and 0<=numerator//2<=27:
            mask&=~(1<<(numerator//2))
    return mask


def direct_mask(points):
    good=0
    for b in range(28):
        xs=[x+b for x in points]
        if all(0<=x<=27 for x in xs) and len({min(x,27-x) for x in xs})==len(xs):
            good|=1<<b
    return good


def allowed_vertices(word,p):
    W,v=p[2],p[1]
    if not -W<word[0]<v:return None
    current=0;points=[]
    for k,x in enumerate(word):
        if k and current*x>=0:return None
        points.append(current);current+=x
    assert current==0
    assert len(set(points))==8 and min(points)>=1-W and max(points)<=v-1
    assert max(points)-min(points)<=26
    return points


def adaptive(p,budget):
    values=tuple(sorted(moves(p).values()));feasible={}
    def visit(left,partial,points,mask,word):
        budget.add('nodes')
        if not left:
            assert partial==0
            if mask:feasible[word]=mask
            return
        assert not word or partial!=0
        mask=extend(mask,partial,points)
        if not mask:return
        for x in sorted(set(left),key=lambda x:(-abs(x),x)):
            if (not word and not -p[2]<x<p[1]) or (word and x*partial>=0):continue
            k=left.index(x);rest=left[:k]+left[k+1:]
            visit(rest,partial+x,points+(partial,),mask,word+(x,))
    visit(values,0,(),ALL,())
    return feasible


def reference(p,budget):
    values=tuple(moves(p).values());budget.add('raw_permutations',math.factorial(8))
    words=sorted(set(permutations(values)));feasible={};accepted=0
    for word in words:
        budget.add('unique_reference_words')
        points=allowed_vertices(word,p)
        if points is None:continue
        budget.add('class_orders');accepted+=1;mask=0
        lo=max(0,-min(points));hi=min(27,27-max(points))
        for b in range(lo,hi+1):
            budget.add('root_checks')
            labels=[min(x+b,27-x-b) for x in points]
            if len(set(labels))==8:mask|=1<<b
        if mask:feasible[word]=mask
    return feasible,accepted,len(words)


def certificate(p,t,word,b):
    available={}
    for i,x in moves(p).items():available.setdefault(x,[]).append(i)
    selected={};order=[];current=0
    for x in word:
        i=available[x].pop(0);selected[i]=current+b;order.append(i);current+=x
    assert current==0
    w=materialize(t,selected)
    assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
    return dict(order_values=word,order_owners=order,origin=b,selected=selected,witness=w)


def controls(base):
    points=(0,5,-16,-9,-2,3,-10,-5);mask=ALL;previous=()
    for x in points:
        mask=extend(mask,x,previous);previous+=(x,)
        assert mask==direct_mask(previous)
    e=base['unresolved'][0];xs=tuple(e['selected'].values());full=ALL;only_range=ALL;old=()
    for x in xs:
        full=extend(full,x,old);only_range&=range_mask(x);old+=(x,)
    assert full==0 and only_range!=0
    b=(only_range&-only_range).bit_length()-1
    assert len({min(x+b,27-x-b) for x in xs})<8
    p=(7,7,21,13,(5,5,5,5))
    assert allowed_vertices((5,5,7,7,-21,-13,5,5),p) is None
    assert not primitive((8,8,20,6,(2,2,2,4)))
    t=(70,70,70,86,122,122,122,122)
    selected={4:22,2:27,0:6,1:13,5:20,3:25,6:12,7:17};w=materialize(t,selected)
    bins=[list(x) for x in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)
    bins=[set(x) for x in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert sorted(x for group in bins for x in group)==list(range(1,56,2))
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)


def main():
    budget=Budget();raw=Path(sys.argv[1]).read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='ae7e59d8060d54998898f7682847b34d48f53351aed784a8f75ec9c5eb90f767'
    base=json.loads(raw);assert len(base['certificates'])==7798 and len(base['unresolved'])==30
    controls(base);results=[];new=[];unresolved=[]
    try:
        for e in base['unresolved']:
            budget.add('targets');assert budget.counts['targets']<=30
            p=e['params'];t=tuple(e['targets']);assert primitive(p)
            first=adaptive(p,budget);second,accepted,unique=reference(p,budget)
            assert first==second
            row=dict(params=p,targets=t,class_orders=accepted,unique_reference_words=unique,
                     feasible_orders=len(first),feasible_origin_count=sum(bin(m).count('1') for m in first.values()))
            if first:
                word=min(first);m=first[word];b=(m&-m).bit_length()-1
                chosen=certificate(p,t,word,b);row['chosen']=chosen
                row['old_min_positive_start_possible']=any(w[0]==min(p[4]) for w in first)
                row['negative_interior_start_possible']=any(w[0]<0 for w in first)
                row['feasible_start_values']=sorted({w[0] for w in first})
                new.append(dict(targets=t,bins=chosen['witness']['bins'],method='reflection_aware_nyctalopic'))
            else:unresolved.append(row)
            results.append(row)
        certificates=list(base['certificates'])+new;keys=set()
        for e in certificates:
            budget.add('certificate_checks');t=tuple(e['targets']);assert t not in keys;keys.add(t)
            assert certificate_ok(e['bins'],t) and bitset_ok(e['bins'],t)
        full,factorable=direct_domain()
        missing={tuple(e['targets']) for e in unresolved}
        assert len(full)==7828 and keys<=full and full-keys==missing
        assert len(certificates)==7798+len(new) and len(missing)==30-len(new)
        budget.add('delivery_audit')
    except BudgetError as err:
        print(json.dumps(dict(status='UNKNOWN',cap=str(err),counts=dict(budget.counts),
                              completed_results=results,cpu_seconds=budget.time()),indent=2));return
    print(json.dumps(dict(status='COMPLETE_CLASS_DIAGNOSIS',tested=30,new_certificates=len(new),
        certified=len(certificates),total_domain=7828,results=results,unresolved=unresolved,
        certificates=sorted(certificates,key=lambda e:tuple(e['targets'])),source_sha256=digest,
        counts=dict(budget.counts),controls='PASS',cpu_seconds=budget.time()),indent=2))


if __name__=='__main__':main()
