#!/usr/bin/env python3
"""TG1: bounded inverse ancestry for GC350's two-zero-run counterfamily.
RUN-ON: CPU, Python standard library, one process.
COMMAND: python3 tests/probes/lexicon/rule30_two_gap_ancestry.py
CAP: 2 CPU seconds globally; 25000 saved full pairs per target, cap => UNDECIDED.
Targets: q8 v4..7 and the published q16 v11 countercontrol only. No forward
census, full q16 sweep or longer trajectory. Data stays outside Git.
Preregistered: TG-P1 (blind, uncertain) some q8 target is rooted. TG-C1 roots
and known q4 (0,3) depth8 absorb; TG-C2 q2 (1,2) has inverse cycle2.
TG-CF a compatible triple is not ancestry evidence (the q2 nonrooted control).
TG-U reverse every absorbed saved chain and check literal forward triples;
positive depth8 control makes this nonvacuous even if no surveyed target roots.
Retain all statuses, first zero-hit depths, cycle lengths and caps. No extrapolation.
"""
import json
import resource
from rule30_sparse_ancestry import packed, scalar


def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime


def decide(start,q,t0):
    chain=[];seen={};state=start
    for k in range(25001):
        if cpu()-t0>2:return {'status':'UNDECIDED','reason':'CPU cap','steps':k}
        if state==(0,0):
            assert chain[-1]==(0,(1<<q)-1)
            forward=list(reversed(chain))
            assert all(scalar(*nxt,q)==cur for cur,nxt in zip(forward,forward[1:]))
            return {'status':'ROOTED','depth':k-1,'first_zero_hit':k}
        if state in seen:return {'status':'NONROOTED','preperiod':seen[state],'cycle':k-seen[state]}
        if k==25000:return {'status':'UNDECIDED','reason':'state cap','steps':k}
        seen[state]=k;chain.append(state)
        nxt=packed(*state,q)
        assert nxt==scalar(*state,q)
        state=nxt
    raise AssertionError('unreachable')


def main():
    t0=cpu()
    for q in (2,4,8):assert decide((0,(1<<q)-1),q,t0)['depth']==0
    assert decide((0,3),4,t0)['depth']==8
    assert decide((1,2),2,t0)['cycle']==2
    rows=[]
    for q,v in [(8,4),(8,5),(8,6),(8,7),(16,11)]:
        c=1|4|sum(1<<i for i in range(v,q))
        a=packed(1,c,q)[0]
        assert a==1|2|4|(1<<(v-1)) and a.bit_count()==4
        rows.append({'q':q,'v':v,'A':a,'B':1,**decide((a,1),q,t0)})
    q8=[r for r in rows if r['q']==8]
    verdict='HELD' if any(r['status']=='ROOTED' for r in q8) else ('UNDECIDED' if any(r['status']=='UNDECIDED' for r in q8) else 'REFUTED')
    print(json.dumps({'rows':rows,'TG_P1':verdict,'controls':'PASS','cpu':cpu()-t0},indent=2))

if __name__=='__main__':main()
