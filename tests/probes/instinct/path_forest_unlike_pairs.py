#!/usr/bin/env python3
"""B59/MI139 preregistered79022fd7: four unlike cancelling components.

All2380 sorted gap multisets from1..14, two exact independent folded
matching/physical-root searches. Predict all witness, naive ascending
greedy fails >=1. Secondary descending greedy is an unexpected check.
Small pool8 two-gap brute controls incl gap3 twice, omitted-fold counter-
example, known repeated-gap class, exact945 E28 domain/two literal checkers.
Caps2400 gap cases/945 corollaries/2M nodes/fiveCPU seconds, no bigger
cycles, alternate factorization or cap raise. REFUTED-BY: any missing
witness, domain/control mismatch; greedy forecast refuted if none fail.
Raw outside git. Finite COMPUTED, no universal hand theorem or L8 bound.
OUTCOME: all2380 multisets certify in both exact implementations. BOTH
ascending and descending greedy rules also succeed in every case, so the
forecast of >=1 ascending failure is REFUTED.23874 exact-search nodes,
CPU0.375611s. Exact945 E28 corollaries (45/225/675 by pair count), two
literal checkers and all controls PASS. Full immutable output SHA256
8ab5816e409d0d202b6ae605a9228e8bb40db7edd7e42eaacad8ea6d7f07f112.
No assertion about arbitrary component order, general pieces or full L8.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import setup,materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok
from path_forest_repeated_pieces import construct as repeated


class Budget:
    def __init__(self):self.start=time.process_time();self.nodes=0
    def step(self):
        self.nodes+=1
        assert self.nodes<=2000000 and time.process_time()-self.start<5,'CAP'


def lab(x,N=28):return min(x,N-1-x)


def formula(g,N):
    return [(i,j) for i in range(N//2) for j in range(i+1,N//2)
            if j-i==g or i+j==N-1-g]


def primary(gaps,budget,N=28):
    def go(k,used):
        budget.step()
        if k==len(gaps):return []
        for i,j in formula(gaps[k],N):
            m=(1<<i)|(1<<j)
            if m&used:continue
            answer=go(k+1,used|m)
            if answer is not None:
                x=next(x for x in range(N-gaps[k]) if {lab(x,N),lab(x+gaps[k],N)}=={i,j})
                return [(x,x+gaps[k])]+answer
        return None
    return go(0,0)


def secondary(gaps,budget,N=28):
    def go(todo,used):
        budget.step()
        if not todo:return {}
        i=todo[-1];g=gaps[i]
        for x in range(N-g):
            labels={min(x,N-1-x),min(x+g,N-1-x-g)}
            if len(labels)<2 or used&labels:continue
            rest=go(todo[:-1],used|labels)
            if rest is not None:return {i:(x,x+g),**rest}
        return None
    answer=go(tuple(range(len(gaps))),set())
    return None if answer is None else [answer[i] for i in range(len(gaps))]


def good(gaps,pairs,N=28):
    if pairs is None or len(pairs)!=len(gaps):return False
    for g,(x,y) in zip(gaps,pairs):
        if not 0<=x<y<N or y-x!=g:return False
    xs=[x for pair in pairs for x in pair]
    return len({min(x,N-1-x) for x in xs})==len(xs)


def greedy(gaps,descending=False):
    used=set();out={}
    order=list(range(len(gaps)))
    if descending:order.reverse()
    for i in order:
        g=gaps[i]
        for x in range(28-g):
            labels={lab(x),lab(x+g)}
            if len(labels)==2 and not labels&used:
                out[i]=(x,x+g);used|=labels;break
        else:return None
    return [out[i] for i in range(len(gaps))]


def controls(budget):
    for g in range(1,15):
        direct={tuple(sorted((lab(x),lab(x+g)))) for x in range(28-g) if lab(x)!=lab(x+g)}
        assert set(formula(g,28))==direct
        assert repeated(g,g,4)
    for gaps in combinations_with_replacement(range(1,5),2):
        brute=any(len({min(x,7-x) for x in (a,a+gaps[0],b,b+gaps[1])})==4
                  for a in range(8-gaps[0]) for b in range(8-gaps[1]))
        a=primary(gaps,budget,8);b=secondary(gaps,budget,8)
        assert (a is not None)==(b is not None)==brute
        if brute:assert good(gaps,a,8) and good(gaps,b,8)
    assert primary((3,3),budget,8) is None
    bad=[(0,13),(14,27)];assert len({x for pair in bad for x in pair})==4
    assert not good((13,13),bad)


def domain_primary():
    out=set()
    for u in range(6,15):
        for v in range(u,15):
            for k in range(3):
                for small in combinations_with_replacement(range(1,6),k):
                    e=[u,v]+[-u,-v]+list(small)+[-x for x in small]+[0]*(4-2*k)
                    t=(56+2*u,56+2*v)+tuple(sorted(112+2*x for x in e[2:]))
                    assert sum(t)==784 and tuple(sorted(t))==t
                    out.add(t)
    return out


def domain_reference():
    out=set()
    for low in combinations_with_replacement(range(68,111,2),2):
        for k in range(3):
            for high in combinations_with_replacement(range(114,123,2),k):
                magnitudes=[(x-56)//2 for x in low]+[(x-112)//2 for x in high]
                middle=sorted(112-2*x for x in magnitudes)+[112]*(4-2*k)
                t=low+tuple(middle)+high
                if all(68<=x<=122 for x in t) and tuple(sorted(t))==t and sum(t)==784:
                    _,_,e=setup(t)
                    assert Counter(x for x in e if x>0)==Counter(-x for x in e if x<0)
                    out.add(t)
    return out


def materializations(rows,budget):
    lookup={tuple(row['gaps']):row['primary'] for row in rows}
    domain=domain_primary();assert len(domain)==945 and domain==domain_reference()
    answers=[];counts=Counter()
    for t in sorted(domain):
        assert time.process_time()-budget.start<5
        _,_,e=setup(t);positive=defaultdict(list);negative=defaultdict(list)
        for i,x in enumerate(e):
            if x>0:positive[x].append(i)
            if x<0:negative[-x].append(i)
        real=sorted(x for x in e if x>0);padded=tuple(sorted(real+[1]*(4-len(real))))
        selected={}
        for g,(x,y) in zip(padded,lookup[padded]):
            if not positive[g]:continue
            selected[positive[g].pop(0)]=x;selected[negative[g].pop(0)]=y
        w=materialize(t,selected)
        assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
        counts[len(real)]+=1;answers.append(dict(targets=t,bins=w['bins']))
    assert [counts[k] for k in (2,3,4)]==[45,225,675]
    t=answers[0]['targets'];bins=[set(b) for b in answers[0]['bins']]
    x,y=min(bins[0]),min(bins[2]);bins[0].remove(x);bins[2].remove(y)
    bins[0].add(y);bins[2].add(x)
    assert sorted(x for b in bins for x in b)==list(range(1,56,2))
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)
    return answers,dict(counts)


def main():
    budget=Budget();controls(budget);rows=[];failed=[];ascending=[];descending=[]
    for gaps in combinations_with_replacement(range(1,15),4):
        assert len(rows)<2400
        a=primary(gaps,budget);b=secondary(gaps,budget)
        assert (a is not None)==(b is not None)
        if a is not None:assert good(gaps,a) and good(gaps,b)
        else:failed.append(gaps)
        ga=greedy(gaps);gd=greedy(gaps,True)
        if ga is None:ascending.append(gaps)
        else:assert good(gaps,ga)
        if gd is None:descending.append(gaps)
        else:assert good(gaps,gd)
        rows.append(dict(gaps=gaps,primary=a,secondary=b,greedy_ascending=ga,greedy_descending=gd))
    assert len(rows)==2380
    certificates,counts=materializations(rows,budget) if not failed else ([],{})
    print(json.dumps(dict(status='COMPLETE_CLASS_TEST',tested=len(rows),failed=failed,
        greedy_ascending_failures=ascending,greedy_descending_failures=descending,
        results=rows,corollary_certificates=certificates,corollary_counts=counts,
        nodes=budget.nodes,controls='PASS',cpu_seconds=time.process_time()-budget.start),indent=2))


if __name__=='__main__':main()
