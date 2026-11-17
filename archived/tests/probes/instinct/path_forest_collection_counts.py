#!/usr/bin/env python3
"""B64/MI149 prereg1082a510: counts only, no spatial placement work.

326119 even E28 parents. Unordered multisets of primitive signed MOVE types,
equal copies indistinguishable; count coefficient by piece-size partition.
Predict <2M collections,<100k atom types,>1000 primitive-eight parents.
Independent indexed-partition/deduplicated controls: all small zero-sum
multisets on +/-1..3 through length6 and64 fixed spread actual ranks.
Counterfactual labelled/ordered count; unexpected full-parent injectivity
versus per-atom reuse. Caps40 CPU sec/512MiB/250k atoms/10M count states/
2M reference states. Stop partial UNKNOWN, no restart, ordering or solver.
OUTCOME MI150:all326119 parents,576515 collections,max6,36735 atom types;
9426 primitive-eight parents.57 toy/64 spread reference controls PASS.
CPU29.465412s/RSS131452928 bytes, no cap. Artifact SHA256
db6d4ccfe32911fba66625d71a0c2e8df2a82f6879d46caea2a4d0679713fa1e.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
import json
import resource
import sys
import time
from path_forest_uniformity import count
from path_forest_exceptional_counts import gaussian_coefficients


class Cap(Exception):pass


class Budget:
    def __init__(self):self.start=time.process_time();self.states=0;self.reference=0
    def check(self):
        if time.process_time()-self.start>40:raise Cap('CPU')
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if sys.platform!='darwin':rss*=1024
        if rss>512*1024**2:raise Cap('RSS')
        if self.states>10000000:raise Cap('COUNT_STATES')
        if self.reference>2000000:raise Cap('REFERENCE_STATES')


def atom_types(a):
    n=len(a);sums=[0]*(1<<n);masks=[];types=set()
    for m in range(1,1<<n):
        bit=m&-m;sums[m]=sums[m^bit]+a[bit.bit_length()-1]
        if sums[m]==0 and not any(m&b==b for b in masks):
            masks.append(m);types.add(tuple(a[i] for i in range(n) if m>>i&1))
    return tuple(sorted(types))


def subtract(a,b):
    left=[];j=0
    for x in a:
        if j<len(b) and b[j]==x:j+=1
        elif j<len(b) and b[j]<x:return None
        else:left.append(x)
    return tuple(left) if j==len(b) else None


def coefficients(a,budget):
    atoms=atom_types(a)
    @lru_cache(None)
    def go(left,start):
        budget.states+=1
        if budget.states%10000==0:budget.check()
        if not left:return (((),1),)
        answer=Counter()
        for i in range(start,len(atoms)):
            atom=atoms[i]
            if atom[0]!=left[0]:continue
            rest=subtract(left,atom)
            if rest is None:continue
            for sizes,n in go(rest,i):answer[tuple(sorted(sizes+(len(atom),)))]+=n
        return tuple(sorted(answer.items()))
    answer=dict(go(a,0));assert answer
    return atoms,answer


def reference_collections(a,budget):
    # Indexed set partitions anchored at the first remaining INDEX; only at
    # the end forget copy labels and component order. Direct proper subsets
    # decide primitiveness, independently of minimal-mask pruning.
    n=len(a);atoms=[]
    for m in range(1,1<<n):
        values=tuple(a[i] for i in range(n) if m>>i&1)
        if sum(values):continue
        minimal=True
        for s in range(1,(1<<len(values))-1):
            budget.reference+=1
            if sum(values[j] for j in range(len(values)) if s>>j&1)==0:
                minimal=False;break
        if minimal:atoms.append((m,values))
    @lru_cache(None)
    def go(left):
        budget.reference+=1
        if not left:return frozenset(((),)),1
        pivot=left&-left;out=set();labelled=0
        for m,part in atoms:
            if m&pivot and left&m==m:
                rest,ways=go(left^m);labelled+=ways
                out.update(tuple(sorted(parts+(part,))) for parts in rest)
        return frozenset(out),labelled
    out,labelled=go((1<<n)-1)
    for collection in out:assert tuple(sorted(x for part in collection for x in part))==a
    by_size=Counter(tuple(sorted(map(len,c))) for c in out)
    budget.check()
    return set(v for _,v in atoms),dict(by_size),labelled


def check_reference(a,budget):
    atoms,answer=coefficients(a,budget);ref,other,labelled=reference_collections(a,budget)
    assert set(atoms)==ref and answer==other,(a,answer,other)
    return sum(answer.values()),labelled


def targets():
    def gen(k,lo,total,prefix):
        if not k:
            if not total:yield tuple(68+2*x for x in prefix)
            return
        for x in range(max(lo,total-27*(k-1)),min(27,total//k)+1):
            yield from gen(k-1,x,total-x,prefix+(x,))
    return gen(8,0,120,())


def sizes(total,lo=2):
    if total==0:yield ();return
    for x in range(lo,total+1):
        for rest in sizes(total-x,x):yield (x,)+rest


def main():
    budget=Budget();N=count(8,0,27,120)
    assert N==gaussian_coefficients(8,27,120)[120]==326119
    small=0
    for k in range(2,7):
        for a in combinations_with_replacement((-3,-2,-1,1,2,3),k):
            if not sum(a):check_reference(a,budget);small+=1
    assert check_reference((-1,-1,1,1),budget)==(1,2)
    assert check_reference((-1,-1,-1,1,2),budget)[0]==1
    assert (-1,-1,1,1) not in atom_types((-1,-1,1,1))
    assert (-1,1) in atom_types((-1,1)) and (-1,1) in atom_types((-2,-1,1,2))
    patterns=sorted({p for n in range(2,9) for p in sizes(n)})
    ids={p:i for i,p in enumerate(patterns)};assert len(patterns)==21
    spread={j*(N-1)//63 for j in range(64)};checked=0
    catalog=set();totals=Counter();parents=Counter();hist=Counter();active=Counter();negatives=Counter()
    rows=[];maximum=0;max_rank=None;primitive_parents=Counter();reason=None
    try:
        previous=None
        for rank,t in enumerate(targets()):
            if rank%1000==0:budget.check()
            assert previous is None or previous<t;previous=t
            moves=tuple(sorted(x for x in ((t[i]-(56 if i<2 else 112))//2 for i in range(8)) if x))
            assert sum(moves)==0 and len([x for x in moves if x>=6])==2
            large=[x for x in moves if x>=6];other=[x for x in moves if x<6]+[0]*(8-len(moves))
            reconstructed=tuple(56+2*x for x in large)+tuple(sorted(112+2*x for x in other))
            assert reconstructed==t
            atoms,answer=coefficients(moves,budget)
            if rank in spread:
                ref,independent,_=reference_collections(moves,budget)
                assert set(atoms)==ref and answer==independent;checked+=1
            catalog.update(atoms)
            if len(catalog)>250000:raise Cap('ATOM_TYPES')
            total=sum(answer.values());hist[total]+=1
            if total>maximum:maximum=total;max_rank=rank
            for p,n in answer.items():
                assert sum(p)==len(moves);totals[p]+=n;parents[p]+=1
            if len(atoms)==1 and atoms[0]==moves:primitive_parents[len(moves)]+=1
            active[len(moves)]+=1;negatives[sum(x<0 for x in moves)]+=1
            rows.append([total,[[ids[p],n] for p,n in sorted(answer.items())]])
            if rank and rank%50000==0:
                print('counted',rank,'parents; CPU',round(time.process_time()-budget.start,2),file=sys.stderr)
        assert len(rows)==N and checked==64
    except Cap as cap:reason=str(cap)
    atom_summary=Counter((len(a),sum(x>0 for x in a),sum(x<0 for x in a)) for a in catalog)
    collections=sum(k*v for k,v in hist.items())
    assert collections==sum(totals.values()) and sum(active.values())==len(rows)==sum(hist.values())
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':rss*=1024
    print(json.dumps(dict(status='COMPLETE_COUNTS' if reason is None else 'UNKNOWN_PARTIAL',
        cap=reason,expected_parents=N,parents=len(rows),total_collections=collections,
        distinct_atom_types=len(catalog),maximum_collections=maximum,maximum_rank=max_rank,
        count_histogram=dict(hist),active_counts=dict(active),negative_counts=dict(negatives),
        primitive_parent_counts=dict(primitive_parents),
        piece_size_patterns=patterns,collection_counts_by_pattern={str(k):v for k,v in totals.items()},
        parents_offering_pattern={str(k):v for k,v in parents.items()},
        atom_counts_by_size_sign={str(k):v for k,v in atom_summary.items()},
        catalog=sorted(catalog),parent_rows=rows,
        controls=dict(status='PASS',toy_parents=small,actual_spread_parents=checked,
                      count_states=budget.states,reference_states=budget.reference),
        cpu_seconds=time.process_time()-budget.start,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
