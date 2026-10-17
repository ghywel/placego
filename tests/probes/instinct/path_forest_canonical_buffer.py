#!/usr/bin/env python3
"""B123/MI267 prereg: same54 targets, fixed canonical seven-set.

Blind prediction ALL54 canonical remainders have the seven prescribed
triples. Primary complete bin-mask MRV; reference raw smallest-token
partner recursion on first negative. Stop at first failure/cap, no repair.
Known69/97 positives; synthetic forced-anchor triple incompatibility
despite individual feasibility; wrong21/22 token inventory rejects.
50k nodes/profile shared across engines,500k total,10CPU sec/128MiB.
REFUTED-BY: a complete canonical failure; it does not refute SB7 or E28.
Raw output remains local pending artifact authorization.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_buffer_kill as boundary
import path_forest_split_anchor_pilot as validation


class Budget:
    def __init__(self):self.start=time.process_time();self.total=0;self.local=0
    def step(self):
        self.total+=1;self.local+=1
        if self.local>50000 or self.total>500000:raise RuntimeError('node cap')
        if time.process_time()-self.start>10:raise RuntimeError('cpu cap')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>128*1024*1024:
            raise RuntimeError('rss cap')


def canonical(a):
    row=[1,3,5,7,9,11,a-36] if a<=91 else [1,3,5,7,9,a-80,55]
    assert len(set(row))==7 and sum(row)==a and min(row)>=1 and max(row)<=55
    return tuple(sorted(row))


def primary(pool,targets,budget):
    if len(pool)!=3*len(targets):raise ValueError('wrong triple inventory')
    assert sum(pool)==sum(targets) and tuple(sorted(pool))==pool
    n=len(pool);by_sum={s:[] for s in set(targets)}
    for ids in combinations(range(n),3):
        s=sum(pool[i] for i in ids)
        if s in by_sum:by_sum[s].append(sum(1<<i for i in ids))
    dead=set();universe=(1<<n)-1
    def visit(left,used):
        budget.step()
        if not left:
            assert used==universe
            return []
        state=tuple(left),used
        if state in dead:return None
        fits={s:[m for m in by_sum[s] if not m&used] for s in set(left)}
        s=min(fits,key=lambda s:(len(fits[s]),s))
        rest=list(left);rest.remove(s)
        for mask in fits[s]:
            child=visit(tuple(rest),used|mask)
            if child is not None:return [(s,mask)]+child
        dead.add(state);return None
    rows=visit(tuple(sorted(targets)),0)
    if rows is None:return None
    inventory={s:[] for s in set(targets)}
    for s,mask in rows:inventory[s].append([pool[i] for i in range(n) if mask>>i&1])
    return [inventory[s].pop() for s in targets]


def reference(pool,targets,budget):
    """No precomputed triple rows: smallest token, owner, two raw partners."""
    dead=set()
    def visit(free,left):
        budget.step()
        if not left:return not free
        key=free,left
        if key in dead:return False
        first=free[0]
        for s in set(left):
            for y,z in combinations(range(1,len(free)),2):
                if first+free[y]+free[z]!=s:continue
                nextfree=tuple(v for i,v in enumerate(free) if i not in (0,y,z))
                rest=list(left);rest.remove(s)
                if visit(nextfree,tuple(rest)):return True
        dead.add(key);return False
    return visit(tuple(pool),tuple(sorted(targets)))


def controls(budget):
    # Each huge token is forced into its corresponding triple by separation.
    pool=tuple(range(1,16,2))+(101,1001,10001,100001)
    targets=(111,1011,10023,100023)
    assert sum(pool)==sum(targets)
    assert all(any(sum(c)==s for c in combinations(pool,3)) for s in targets)
    budget.local=0
    assert primary(pool,targets,budget) is None
    assert not reference(pool,targets,budget)
    known=((69,69,69,93,121,121,121,121),(97,97,97,97,99,99,99,99))
    for t in known:
        C=canonical(t[0]);pool=tuple(x for x in range(1,56,2) if x not in C)
        budget.local=0;rows=primary(pool,t[1:],budget)
        assert rows is not None and reference(pool,t[1:],budget)
        bins=[list(C)]+rows
        assert validation.literal_ok(bins,t,[3]+[1]*7)
        assert validation.independent_ok(bins,t)
    try:primary(tuple(range(13,56,2)),known[0][1:],budget)
    except ValueError as e:assert str(e)=='wrong triple inventory'
    else:raise AssertionError('22 tokens accepted for seven triples')
    return dict(forced_pair_obstruction=True,individually_feasible=True,
                two_known_positives=True,wrong_pool_size_rejected=True)


def main():
    budget=Budget();rows=[];out={}
    try:
        prior=Path('/tmp/math-instinct-b122-buffer-kill.json').read_bytes()
        assert hashlib.sha256(prior).hexdigest()=='1bfa55c0e20b397eedba14e34f954c171bdd3d5cf118afb22b79db925e5533c7'
        previous=json.loads(prior)
        targets,_,_=boundary.domain()
        assert targets==[tuple(r['targets']) for r in previous['rows']] and len(targets)==54
        out.update(prior_sha256=hashlib.sha256(prior).hexdigest(),declared=54,controls=controls(budget))
        for t in targets:
            out['pending_target']=t;budget.local=0;C=canonical(t[0])
            pool=tuple(x for x in range(1,56,2) if x not in C)
            interval=tuple(range(13,56,2)) if t[0]<=91 else tuple(range(11,54,2))
            hole=t[0]-36 if t[0]<=91 else t[0]-80
            assert pool==tuple(x for x in interval if x!=hole)
            triples=primary(pool,t[1:],budget)
            row=dict(targets=t,canonical_buffer=C,hole=hole,
                     status='WITNESS' if triples is not None else 'NO_WITNESS')
            if triples is None:
                assert not reference(pool,t[1:],budget)
                row['independent_negative']=True
                row['nodes']=budget.local;rows.append(row)
                out['status']='STOP_FIRST_CANONICAL_FAILURE';break
            bins=[list(C)]+triples
            assert validation.literal_ok(bins,t,[3]+[1]*7)
            assert validation.independent_ok(bins,t)
            row.update(nodes=budget.local,bins=bins);rows.append(row)
        else:out['status']='COMPLETE_SAME_54_CANONICAL_TEST'
        out.update(rows=rows,pending_target=None,
                   prediction_all_work=len(rows)==54 and all(r['status']=='WITNESS' for r in rows))
    except RuntimeError as e:
        out.update(status='UNKNOWN_CAP',reason=str(e),rows=rows)
    out.update(total_nodes=budget.total,cpu_seconds=time.process_time()-budget.start,
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(out,separators=(',',':')))


if __name__=='__main__':main()
