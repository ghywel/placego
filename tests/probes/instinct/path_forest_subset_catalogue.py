#!/usr/bin/env python3
"""B121/MI263: anchor-free subset catalogue, exactly five E28 fixtures.

BEFORE RUN: all subsets of first28 odds with sum<=122, arbitrary sizes;
predict catalogue<=500k masks. Generating-function ALL sum counts and
MITM FULL masks at every fixture sum must agree. Exact cover has bin
and token columns, no anchors, roles, cycle classes or component assumptions.
Predict all five fixtures certify, each<1000 search nodes (blind), using
<=50k nodes/target,1M total,15CPU sec/256MiB. Compare every189 small
3-target question m<=6 to independent labelled-assignment oracle. Published
26-token67/102 lower witness and3,3,3 global conflict must reject; corrupted
inventory and coverage-preserving wrong-sum controls reject. Unexpected:
97/99 succeeds without preserving impossible R0 anchors; check every odd
token once, not merely each bin sum. No sample/census/policy sweep or
automatic follow-on. Raw stays local pending artifact authorization.
REFUTED-BY: catalogue>500k, any fixture unsolved, or >=1000 nodes/fixture.
OUTCOME MI264:129658 masks;123 GF counts/23 full MITM maps/189 oracle
questions and negative controls pass. All5 fixtures WITNESS,nodes9/9/9/27/9.
CPU0.406685sec/RSS24842240bytes. Raw1893bytes SHA256
964133f42e2271d7eba8e0dbbac3dfc203c2b0fa64757dc9b582e8463a0b6b29;local only.
"""
from collections import Counter, defaultdict
from itertools import product
import json
import resource
import time

import path_forest_pilot as old
import path_forest_split_anchor_pilot as validator


FIXTURES=[(97,97,97,97,99,99,99,99),
          (77,77,83,85,107,117,119,119),
          (71,73,77,105,107,109,121,121),
          (69,69,75,103,111,116,120,121),
          (90,90,91,91,93,103,111,115)]


class Cap(Exception):
    pass


class Budget:
    def __init__(self):
        self.start=time.process_time();self.total=0;self.local=0;self.catalogue=0;self.joins=0

    def check(self,node=False):
        if node:self.total+=1;self.local+=1
        if self.local>50000 or self.total>1000000:raise Cap('search_nodes')
        if self.catalogue>1000000:raise Cap('catalogue_masks')
        if self.joins>2000000:raise Cap('reference_joins')
        if time.process_time()-self.start>15:raise Cap('cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:
            raise Cap('rss')


def catalogue(budget):
    out=[[] for _ in range(123)]
    def extend(start,s,mask):
        out[s].append(mask);budget.catalogue+=1
        if budget.catalogue%256==0:budget.check()
        for j in range(start,28):
            new=s+2*j+1
            if new>122:break
            extend(j+1,new,mask|(1<<j))
    extend(0,0,0)
    # Independent generating function, descending coefficient updates.
    coeff=[1]+[0]*122
    for odd in range(1,56,2):
        for s in range(122,odd-1,-1):coeff[s]+=coeff[s-odd]
    assert list(map(len,out))==coeff
    assert all(len(v)==len(set(v)) for v in out)
    return [tuple(v) for v in out],coeff


def mitm(catalogue,targets,budget):
    # Exhaustive bit products in two halves; independent of increasing recursion.
    halves=[]
    for start in (0,14):
        groups=defaultdict(list)
        for bits in product((0,1),repeat=14):
            s=sum((2*(start+j)+1)*b for j,b in enumerate(bits))
            if s<=122:groups[s].append(sum(b<<(start+j) for j,b in enumerate(bits)))
        halves.append(groups)
    checked=0
    for target in sorted(targets):
        masks=set()
        for s,lefts in halves[0].items():
            for a in lefts:
                for b in halves[1].get(target-s,()):
                    budget.joins+=1;masks.add(a|b)
                    if budget.joins%256==0:budget.check()
        assert masks==set(catalogue[target]);checked+=1
    return checked


def solve(m,targets,catalogue,budget):
    assert sum(targets)==m*m and all(0<t<=122 for t in targets)
    budget.local=0;universe=(1<<m)-1
    options={t:tuple(mask for mask in catalogue[t] if mask&universe==mask)
             for t in set(targets)}
    failed=set()
    def visit(left,used):
        budget.check(True)
        if not left:
            assert used==universe
            return {}
        state=(tuple(sorted(targets[i] for i in left)),used)
        if state in failed:return None
        fitting={i:tuple(mask for mask in options[targets[i]] if not mask&used) for i in left}
        if any(not v for v in fitting.values()):failed.add(state);return None
        remaining=universe^used
        if sum(min(mask.bit_count() for mask in fitting[i]) for i in left)>remaining.bit_count():
            failed.add(state);return None
        # Exact-cover columns include every bin AND every remaining token.
        pivot=min(left,key=lambda i:(len(fitting[i]),i))
        choices=[(pivot,mask) for mask in fitting[pivot]]
        counts=Counter()
        for rows in fitting.values():
            for mask in rows:
                while mask:
                    bit=mask&-mask;mask^=bit;counts[bit]+=1
        scan=remaining
        while scan:
            bit=scan&-scan;scan^=bit
            if counts[bit]<len(choices):
                choices=[(i,mask) for i in left for mask in fitting[i] if mask&bit]
        for i,mask in choices:
            child=visit(tuple(j for j in left if j!=i),used|mask)
            if child is not None:return {i:mask,**child}
        failed.add(state);return None
    masks=visit(tuple(range(len(targets))),0)
    if masks is None:return None
    bins=[[2*j+1 for j in range(m) if masks[i]>>j&1] for i in range(len(targets))]
    assert old.verify_witness(m,targets,bins)
    return bins


def main():
    budget=Budget();rows=[];out={}
    try:
        cat,coeff=catalogue(budget)
        count=sum(coeff);out.update(catalogue_masks=count,per_sum_counts=coeff,
                                   catalogue_under500k=count<=500000)
        refs=mitm(cat,{x for row in FIXTURES for x in row},budget)
        checked=0
        for m in range(1,7):
            oracle=old.exhaustive_oracle(m)
            for t in old.sorted_targets(m*m,3,1):
                bins=solve(m,t,cat,budget)
                assert (bins is not None)==(t in oracle)
                checked+=1
        assert checked==189
        assert solve(3,(3,3,3),cat,budget) is None
        lower=(67,67,67,67,102,102,102,102)
        assert solve(26,lower,cat,budget) is None
        out.update(mitm_full_maps=refs,small_oracle_questions=checked,
                   global_conflict_rejected=True,published_lower_witness_rejected=True)
        for target in FIXTURES:
            bins=solve(28,target,cat,budget)
            row=dict(targets=target,status='WITNESS' if bins else 'NO_WITNESS',nodes=budget.local)
            if bins:
                assert validator.independent_ok(bins,target)
                h=[(len(b)-t%2)//2 for b,t in zip(bins,target)]
                assert validator.literal_ok(bins,target,h)
                bad=[list(b) for b in bins];bad[0][0]=bad[1][0]
                assert not old.verify_witness(28,target,bad)
                assert not validator.independent_ok(bad,target)
                wrong=[list(b) for b in bins]
                wrong[0][0],wrong[1][0]=wrong[1][0],wrong[0][0]
                assert sorted(x for b in wrong for x in b)==list(range(1,56,2))
                assert not old.verify_witness(28,target,wrong)
                assert not validator.independent_ok(wrong,target)
                row.update(bins=bins,cardinalities=list(map(len,bins)))
            rows.append(row)
        out.update(status='COMPLETE_FIXED_FIVE',rows=rows,
                   prediction_all_work=all(r['status']=='WITNESS' for r in rows),
                   prediction_each_under1000=all(r['nodes']<1000 for r in rows))
    except Cap as e:
        out.update(status='UNKNOWN_CAP',reason=str(e),rows=rows)
    out.update(cpu_seconds=time.process_time()-budget.start,total_nodes=budget.total,
               reference_joins=budget.joins,
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(out,separators=(',',':')))


if __name__=='__main__':
    main()
