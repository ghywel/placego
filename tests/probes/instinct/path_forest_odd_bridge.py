#!/usr/bin/env python3
"""B71/MI163 prereg256dd748: formula-only whole-path parity bridge.

4 positive geometry fixtures,2 essential-hypothesis controls,1 E28 partition.
No order/slot search, sample or grid.1CPU sec/64MiB. General hand proof in MI163;
checks do not upgrade it to PROVED. Chosen E28 slots are explicitly NON-GREEDY.
OUTCOME:4 formula fixtures/2 essential-hypothesis counterexamples/1 exact
E28 partition pass. Greedy slots differ, explicitly checked. No search.
0.000376CPU sec,14831616bytes RSS. Full raw SHA256
 a54b18648fcc5bd1f11fc213191457f9bab09719ddbe2087646b6c0fe20b9a94.
"""
import json
import resource
import time
import path_forest_split_anchor_pilot as pilot


def points(x,A,a,b,B):
    result=[x]
    for step in (*A,a,b,*B):result.append(result[-1]+step)
    return result


def literal(xs,M,R):
    return (all(0<=x<M for x in xs) and len(set(xs))==len(xs)
            and all(x+y!=M-1 for i,x in enumerate(xs) for y in xs[i+1:])
            and all(min(x,M-1-x) not in R for x in xs))


def construct(M,s,r,x,A,a,b,B):
    assert M>0 and M%2==0 and 0<=s and r>=1 and s+r<=M//2
    assert all(v>0 and v%2==0 for v in (*A,*B))
    assert a>0 and a%2==1 and b>0 and b%2==1 and x>=0 and x%2==0
    c=x+sum(A)+a;end=c+b+sum(B)
    assert x+sum(A)<s and s+r<=c<=M-1-s-r
    assert c+b>=M-s and end<M
    xs=points(x,A,a,b,B);R=set(range(s,s+r));labels=[min(y,M-1-y) for y in xs]
    assert len(set(labels))==len(labels) and not set(labels)&R
    assert literal(xs,M,R)
    return dict(M=M,reserved=sorted(R),root=x,before=A,bridge=(a,b),after=B,
                centre=c,positions=xs,labels=labels,negative_move=-(end-x))


def main():
    start=time.process_time();fixtures=[]
    for name,x,A,B in [('full',0,(4,4),(2,2,2)),('empty_before',8,(),(2,2)),
                       ('empty_after',0,(4,4),()),('both_empty',8,(),())]:
        row=construct(28,10,3,x,A,5,5,B);row['name']=name;fixtures.append(row)
    bad_outer=points(0,(1,1),11,5,(8,));bad_centre=points(0,(),1,17,(8,))
    assert bad_outer==[0,1,2,13,18,26]
    assert bad_centre==[0,1,18,26]
    assert not literal(bad_outer,28,{10,11,12}) and not literal(bad_centre,28,{10,11,12})
    for args in [(28,10,3,0,(1,1),11,5,(8,)),(28,10,3,0,(),1,17,(8,))]:
        try:construct(*args)
        except AssertionError:pass
        else:raise AssertionError('invalid hypothesis accepted')
    t=(85,87,89,91,93,95,122,122);R={10,11,12};a=[21,23,25,31,33,35,0,0]
    h=[2,1,1,1,1,1,2,2];owners=(1,2,6,7,3,4,5,0)
    selected=dict(zip(owners,fixtures[0]['positions']))
    e=[(x-z-56*s)//2 for x,z,s in zip(t,a,h)]
    assert e==[-24,4,4,2,2,2,5,5]
    assert [e[i] for i in owners]==[4,4,5,5,2,2,2,-24]
    bins=pilot.materialize(t,R,a,h,selected)
    Rg,ag,hg=list(pilot.policies(t))[10]
    assert Rg==R and ag==a and hg==[1,1,1,1,1,1,3,2] and hg!=h
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='FORMULA_CHECKS_PASS',preregistration='256dd748',
                         fixtures=fixtures,counterexamples=dict(outer_parity=bad_outer,centre_location=bad_centre),
                         targets=t,reserved=sorted(R),anchors=a,slots=h,moves=e,selected=selected,bins=bins,
                         greedy_slots=hg,greedy_slot_distinction='EXPLICIT_NON_GREEDY_CONSTRUCTION',
                         controls='PASS',cpu_seconds=elapsed,peak_rss_bytes=rss),indent=2))


if __name__=='__main__':main()
