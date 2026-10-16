#!/usr/bin/env python3
"""B81/MI184 preregce319d40: sorted pairs differing<=1, delta in{1,2}.

Nine formula calls/five E28 partitions; all-smaller, misplaced2/2, doubled
long-edge and outside-class positive controls.1CPU sec/64MiB. No search or
expanded profile grid. General class iff remains SKETCH.
OUTCOME:nine formula calls/five E28 partitions and all controls pass.
0.001503CPU sec,15900672bytes RSS. Raw SHA256
717ef6c924338669998de85d2799c124b86b761cdb20d5004f067cc2bf87cbc0.
"""
from collections import Counter
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def physical(M,A,B):
    xs=[2*A[0]]+[M-1-2*b for b in B]+[2*a for a in reversed(A[1:])]
    word=[v-u for u,v in zip(xs,xs[1:]+[xs[0]])]
    return xs,word


def literal(M,xs):
    return (all(0<=x<M for x in xs) and len(set(xs))==len(xs)
            and len({min(x,M-1-x) for x in xs})==len(xs))


def coupled(M,d,p,q,partition=False):
    assert M%2==0 and len(d)>0 and len(d)%2==0 and min(d)>=2
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*sum(d)
    assert max(p,q)<=M-3 and not(p==q==M-3)
    sd=sorted(d);pairs=list(zip(sd[::2],sd[1::2]))
    assert all(y-x<=1 for x,y in pairs)
    r=sum(x!=y for x,y in pairs)
    if r==0:
        candidates=[i for i,v in enumerate((p,q)) if (v-(M-3))%4==0]
        assert len(candidates)==1;first=candidates[0]
    else:first=0 if p>=q else 1
    P=(p,q)[first];Q=(p,q)[1-first]
    alpha=(M-1-P)//2;beta=(M-3-Q)//2
    assert alpha>=1 and beta>=1
    initial=1 if alpha%2 else 2;a=(alpha-initial)//2
    delta=initial;small=[v for v in pairs if v==(2,2)];others=[v for v in pairs if v!=(2,2)]
    ordered=[];early=False
    if initial==2 and small:
        j=next(i for i,(x,y) in enumerate(others) if x!=y)
        ordered.append(others.pop(j));early=True
    ordered+=small+others
    A=[a];B=[a+initial];trace=[]
    for x,y in ordered:
        before=delta
        if x==y:u=v=x
        elif delta==1:u,v=x,y
        else:u,v=y,x
        assert 0<delta<u
        A.append(A[-1]+u);B.append(B[-1]+v);delta=B[-1]-A[-1]
        assert delta in (1,2)
        trace.append(dict(pair=(x,y),before=before,u=u,v=v,after=delta))
    assert delta==(1 if beta%2 else 2) and delta<=beta
    assert all(A[i]<B[i]<A[i+1]<B[i+1] for i in range(len(A)-1))
    assert A[0]+B[0]==alpha and A[-1]+B[-1]==(M-1+Q)//2
    assert 0<=a and B[-1]<=M//2-1 and len(d)+2<=M//2
    loads=(A[-1]-A[0],B[-1]-B[0])
    assert abs(loads[0]-loads[1])<=1 and max(loads)<=M//2-2
    xs,word=physical(M,A,B)
    assert len(xs)==len(d)+2 and word[0]==P and word[len(B)]==Q
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert all(e<0 and e%2==0 for j,e in enumerate(word) if j not in (0,len(B)))
    assert literal(M,xs) and instrument.literal_geometry(M,set(),xs)
    assert all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
    bins=None;targets=None;selected=None
    if partition:
        assert M==28 and len(d)==6
        e=[p,q]+[-2*v for v in d];h=[1,1]+[2]*6
        targets=[56*s+2*v for s,v in zip(h,e)]
        assert all(68<=v<=122 for v in targets) and sum(targets)==784
        pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)}
        selected={}
        for j,move in enumerate(word):
            owner=first if j==0 else 1-first if j==len(B) else pool[-move//2].pop(0)
            assert e[owner]==move;selected[owner]=xs[j]
        assert all(not v for v in pool.values())
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h) and instrument.independent_ok(M,bins,targets)
    return dict(M=M,d=d,p=p,q=q,first_positive_owner=first,first_positive=P,
                alpha=alpha,beta=beta,initial_delta=initial,final_delta=delta,
                early_unequal=early,A=A,B=B,trace=trace,loads=loads,
                positions=xs,word=word,targets=targets,bins=bins,selected=selected)


def naive(M,d,p,q,all_smaller=False):
    alpha=(M-1-p)//2;delta=1 if alpha%2 else 2;a=(alpha-delta)//2
    A=[a];B=[a+delta];sd=sorted(d)
    for x,y in zip(sd[::2],sd[1::2]):
        if x==y or all_smaller or delta==1:u,v=x,y
        else:u,v=y,x
        A.append(A[-1]+u);B.append(B[-1]+v);delta=B[-1]-A[-1]
    xs,word=physical(M,A,B)
    return dict(A=A,B=B,positions=xs,word=word,final_delta=delta)


def main():
    start=time.process_time();rows=[]
    for d,p,q in (((3,3,3,4,4,4),21,21),((3,3,3,4,4,4),25,17),
                  ((2,2,3,3,3,4),19,15),((2,3,3,4,5,6),25,21),
                  ((2,2,3,3,5,5),23,17)):
        rows.append(coupled(28,d,p,q,True))
    rows.extend((coupled(8,(2,2),5,3),coupled(16,(2,2,3,4),11,11),
                 coupled(32,(2,3,4,5,6,7),29,25),coupled(300,tuple(range(2,22)),297,163)))
    assert len(rows)==9 and sum(r['bins'] is not None for r in rows)==5
    assert rows[2]['early_unequal'] and rows[2]['trace'][0]['pair']==(3,4)
    assert rows[4]['first_positive']==17
    drift=naive(32,(2,3,4,5,6,7),29,25,True)
    assert drift['final_delta']==4 and drift['B'][-1]==16 and not literal(32,drift['positions'])
    assert Counter(drift['word'])==Counter((29,25,-4,-6,-8,-10,-12,-14))
    collision=naive(28,(2,2,3,3,3,4),19,15)
    assert collision['A'][1]==collision['B'][0] and not literal(28,collision['positions'])
    assert Counter(collision['word'])==Counter((19,15,-4,-4,-6,-6,-6,-8))
    refused=[]
    for name,args in (('doubled_long_edge',(24,(3,3,3,4,4,4),21,21)),
                      ('half_one_scope',(28,(1,1,3,3,7,7),25,19)),
                      ('pair_gap_scope',(28,(2,2,2,4,4,4),25,11))):
        try:coupled(*args)
        except AssertionError:refused.append(name)
        else:raise AssertionError('missing refusal '+name)
    outside=[0,25,21,13,5,16,12,8]
    assert literal(28,outside) and instrument.literal_geometry(28,set(),outside)
    outside_word=[v-u for u,v in zip(outside,outside[1:]+[outside[0]])]
    assert Counter(outside_word)==Counter((25,11,-4,-4,-4,-8,-8,-8))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='ce319d40',
                         formula_calls=len(rows),E28_partitions=5,rows=rows,
                         naive_all_smaller=drift,naive_pair_order=collision,scope_rejections=refused,
                         outside_class_positive=dict(positions=outside,word=outside_word),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
