#!/usr/bin/env python3
"""B122/MI265 prereg: SB7 boundary kill, no full domain/census.

All30 two-valued odd E28 profiles plus lexicographic min/max profiles
at each minimum69..97 (15 minima,<=60 unique union). Force cardinality
7 at first/smallest target,3 elsewhere. Blind prediction all WITNESS.
Stop at first NO_WITNESS/UNKNOWN; never add profiles or raise cap.
Independent partition validators, toy all-majorization-pass/unrealizable
four-pair control, ties by relabeling, impossible total-cardinality control.
Per-profile50k states/overall500k,10CPU sec/128MiB,known catalogue cap1M.
REFUTED-BY: a complete NO_WITNESS profile; caps give UNKNOWN, not a refutation.
OUTCOME MI266:all54 union profiles pass;29 full reference buckets,controls
pass;542 nodes,max15/profile,CPU0.339239sec/RSS25325568bytes. No negative
reference branch exercised. Raw11710bytes SHA256
1bfa55c0e20b397eedba14e34f954c171bdd3d5cf118afb22b79db925e5533c7;local only.
"""
from itertools import combinations
import json
import resource
import time

import path_forest_subset_catalogue as base
import path_forest_split_anchor_pilot as validation


class Budget(base.Budget):
    def check(self,node=False):
        if node:self.total+=1;self.local+=1
        if self.local>50000 or self.total>500000:raise base.Cap('search_nodes')
        if self.catalogue>1000000:raise base.Cap('catalogue_masks')
        if self.joins>2000000:raise base.Cap('reference_joins')
        if time.process_time()-self.start>10:raise base.Cap('cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>128*1024*1024:
            raise base.Cap('rss')


def extremum(a,largest):
    """Greedy lex extreme, preserving sortedness, oddness and total."""
    out=[a];left=784-a;lower=a
    for n in range(7,0,-1):
        if largest:
            x=min(121,left//n)
            if x%2==0:x-=1
        else:
            x=max(lower,left-(n-1)*121)
        assert lower<=x<=121 and x%2 and n*x<=left<=x+(n-1)*121
        out.append(x);left-=x;lower=x
    assert left==0 and tuple(sorted(out))==tuple(out)
    return tuple(out)


def domain():
    two={tuple([a]*r+[b]*(8-r))
         for a in range(69,122,2) for b in range(a+2,122,2)
         for r in range(1,8) if r*a+(8-r)*b==784}
    # Independent multiplicity relation around the even average98.
    control={tuple([98-x]*r+[98+y]*(8-r))
             for r in range(1,8) for x in range(1,30,2) for y in range(1,24,2)
             if r*x==(8-r)*y}
    assert two==control and len(two)==30
    extreme={extremum(a,k) for a in range(69,98,2) for k in (False,True)}
    all_rows=sorted(two|extreme)
    assert len(all_rows)<=60
    return all_rows,two,extreme


def solve(m,t,cards,cat,budget):
    if sum(cards)!=m:raise ValueError('cardinality total')
    budget.local=0;universe=(1<<m)-1;failed=set()
    options=[tuple(mask for mask in cat[s] if mask.bit_count()==c and mask&universe==mask)
             for s,c in zip(t,cards)]
    def visit(left,used):
        budget.check(True)
        if not left:
            assert used==universe
            return {}
        state=tuple(sorted((t[i],cards[i]) for i in left)),used
        if state in failed:return None
        fitting={i:tuple(mask for mask in options[i] if not mask&used) for i in left}
        if any(not v for v in fitting.values()):failed.add(state);return None
        i=min(left,key=lambda i:(len(fitting[i]),i))
        choices=[(i,mask) for mask in fitting[i]]
        remaining=universe^used
        while remaining:
            bit=remaining&-remaining;remaining^=bit
            other=[(j,mask) for j in left for mask in fitting[j] if mask&bit]
            if len(other)<len(choices):choices=other
        for j,mask in choices:
            rest=visit(tuple(k for k in left if k!=j),used|mask)
            if rest is not None:return {j:mask,**rest}
        failed.add(state);return None
    masks=visit(tuple(range(len(t))),0)
    if masks is None:return None
    bins=[[2*j+1 for j in range(m) if masks[i]>>j&1] for i in range(len(t))]
    assert base.old.verify_witness(m,t,bins) and list(map(len,bins))==cards
    return bins


def controls(cat,budget):
    # An actual four-bin impossibility that satisfies EVERY scalar subset bound.
    t=(10,10,22,22);cards=[2]*4
    for n in range(1,5):
        for ids in combinations(range(4),n):
            k=2*n;s=sum(t[i] for i in ids)
            assert k*k<=s<=k*(16-k)
    assert solve(8,t,cards,cat,budget) is None
    # Known positive one7+seven3 witness from B121.
    t=(97,97,97,97,99,99,99,99)
    bins=solve(28,t,[7]+[3]*7,cat,budget)
    assert bins and validation.independent_ok(bins,t)
    for j in range(4):
        swapped=[list(b) for b in bins]
        swapped[0],swapped[j]=swapped[j],swapped[0]
        assert validation.independent_ok(swapped,t)
        assert len(swapped[j])==7
    try:solve(28,t,[3]*8,cat,budget)
    except ValueError as e:assert str(e)=='cardinality total'
    else:raise AssertionError('incomplete token inventory accepted')
    bad=[list(b) for b in bins];bad[0][0]=bad[1][0]
    assert not validation.independent_ok(bad,t)
    return dict(all_majorization_not_sufficient=True,known_buffer=True,
                equal_minimum_relabelings=4,wrong_cardinality_rejected=True,
                duplicate_inventory_rejected=True)


def reference_no_witness(t,cat,budget):
    """Independently try every buffer, then pivot a smallest free token."""
    dead=set()
    def triples(free,totals):
        budget.check(True)
        if not totals:return free==0
        key=free,totals
        if key in dead:return False
        xbit=free&-free;x=xbit.bit_length()-1;rest=free^xbit
        ys=[j for j in range(x+1,28) if rest>>j&1]
        for target in set(totals):
            for y,z in combinations(ys,2):
                if 2*(x+y+z)+3!=target:continue
                left=list(totals);left.remove(target)
                if triples(rest^(1<<y)^(1<<z),tuple(left)):return True
        dead.add(key);return False
    for buffer in cat[t[0]]:
        if buffer.bit_count()==7 and triples(((1<<28)-1)^buffer,tuple(t[1:])):
            return False
    return True


def main():
    budget=Budget();rows=[];out={}
    try:
        cat,coeff=base.catalogue(budget)
        assert sum(coeff)==129658
        targets,two,extreme=domain()
        refs=base.mitm(cat,{s for t in targets for s in t}|{10,22},budget)
        out.update(declared_profiles=len(targets),two_valued_profiles=len(two),
                   extreme_profiles=len(extreme),full_reference_buckets=refs,
                   controls=controls(cat,budget))
        for t in targets:
            out['pending_target']=t
            # All general cardinality-majorization bounds hold without search.
            for mask in range(1,256):
                k=sum((7 if i==0 else 3) for i in range(8) if mask>>i&1)
                s=sum(t[i] for i in range(8) if mask>>i&1)
                assert k*k<=s<=k*(56-k)
            bins=solve(28,t,[7]+[3]*7,cat,budget)
            row=dict(targets=t,status='WITNESS' if bins else 'NO_WITNESS',nodes=budget.local,
                     two_valued=t in two,extreme=t in extreme)
            if bins:
                h=[3]+[1]*7
                assert validation.literal_ok(bins,t,h) and validation.independent_ok(bins,t)
                row['bins']=bins
            rows.append(row)
            if bins is None:
                assert reference_no_witness(t,cat,budget)
                row['independent_no_witness']=True
                out['status']='STOP_FIRST_COUNTEREXAMPLE';break
        else:out['status']='COMPLETE_DECLARED_BOUNDARY_TEST'
        out['pending_target']=None
        out.update(rows=rows,prediction_all_work=all(r['status']=='WITNESS' for r in rows)
                   and len(rows)==len(targets))
    except base.Cap as e:
        out.update(status='UNKNOWN_CAP',reason=str(e),rows=rows)
    out.update(total_nodes=budget.total,cpu_seconds=time.process_time()-budget.start,
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(out,separators=(',',':')))


if __name__=='__main__':
    main()
