#!/usr/bin/env python3
"""B82/MI186, prereg2574b6ff: signed near-pair chains, differences<=3.

Exactly11 formula calls/6 E28 partitions, named crossing/balance/scope
controls.1CPU sec/64MiB, no order search or census. Infinite claim SKETCH.
OUTCOME:11 calls/6 partitions and controls pass;0.001968CPU sec,17440768RSS
bytes. Raw SHA2564c05d480b34797291c72ae69b13491a25bffb25abbe86c0144207e09a2279045.
"""
from collections import Counter
import json
import resource
import time

import path_forest_balanced_bridge as instrument
from path_forest_interlaced_pairs import physical, literal


def construct(M,d,p,q,partition=False):
    assert M%2==0 and d and len(d)%2==0 and min(d)>=2
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*sum(d)
    assert max(p,q)<=M-3 and not p==q==M-3
    sd=sorted(d);pairs=list(zip(sd[::2],sd[1::2]))
    assert all(y-x<=3 for x,y in pairs)
    odd=[t for t in pairs if (t[1]-t[0])%2]
    if not odd:
        owners=[i for i,v in enumerate((p,q)) if (v-(M-3))%4==0]
        assert len(owners)==1;first=owners[0]
    else:first=0 if p>=q else 1
    P=(p,q)[first];Q=(p,q)[1-first]
    alpha=(M-1-P)//2;beta=(M-3-Q)//2
    initial=1 if alpha%2 else 2;a=(alpha-initial)//2
    hazard=[t for t in pairs if t==(2,2) or t[1]-t[0]==2]
    rest=[t for t in pairs if not(t==(2,2) or t[1]-t[0]==2)]
    ordered=[];early=False
    if initial==2 and hazard:
        j=next(i for i,(x,y) in enumerate(rest) if (y-x)%2)
        ordered.append(rest.pop(j));early=True
    ordered+=hazard+rest
    A=[a];B=[a+initial];trace=[]
    for x,y in ordered:
        delta=B[-1]-A[-1];g=y-x;sgn=1 if delta>0 else -1
        if g==0:change=0
        elif g==1:change=sgn if abs(delta)==1 else -sgn
        else:
            if g==2:assert abs(delta)==1
            change=-sgn*g
        u,v=(x,y) if change>=0 else (y,x)
        previous_max=max(A[-1],B[-1])
        A.append(A[-1]+u);B.append(B[-1]+v)
        after=B[-1]-A[-1]
        assert after==delta+change and after in (-2,-1,1,2)
        assert previous_max<min(A[-1],B[-1])
        trace.append(dict(pair=(x,y),before=delta,after=after,u=u,v=v,
                          crossed=delta*after<0))
    final=B[-1]-A[-1]
    assert abs(final)==(1 if beta%2 else 2) and abs(final)<=beta
    assert A[0]+B[0]==alpha and A[-1]+B[-1]==(M-1+Q)//2
    assert min(A+B)>=0 and max(A+B)<=M//2-1
    assert len(set(A+B))==len(A+B)==len(d)+2 and len(d)+2<=M//2
    assert all(max(A[i],B[i])<min(A[i+1],B[i+1]) for i in range(len(A)-1))
    loads=(A[-1]-A[0],B[-1]-B[0])
    assert max(loads)<=M//2-1 and loads[1]-loads[0]==final-initial
    xs,word=physical(M,A,B)
    assert word[0]==P and word[len(B)]==Q
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert literal(M,xs) and instrument.literal_geometry(M,set(),xs)
    assert all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
    bins=targets=selected=None
    if partition:
        assert M==28 and len(d)==6
        h=[1,1]+[2]*6;e=[p,q]+[-2*v for v in d]
        targets=[56*s+2*v for s,v in zip(h,e)]
        assert min(targets)>=68 and max(targets)<=122 and sum(targets)==784
        pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)}
        selected={}
        for j,move in enumerate(word):
            owner=first if j==0 else 1-first if j==len(B) else pool[-move//2].pop(0)
            assert e[owner]==move;selected[owner]=xs[j]
        assert all(not v for v in pool.values())
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h)
        assert instrument.independent_ok(M,bins,targets)
    return dict(M=M,d=d,p=p,q=q,first_positive_owner=first,alpha=alpha,beta=beta,
                initial_delta=initial,final_delta=final,early_odd_pair=early,
                A=A,B=B,loads=loads,trace=trace,positions=xs,word=word,
                targets=targets,bins=bins,selected=selected)


def shortcut(M,d,p,q,all_smaller=False):
    alpha=(M-1-p)//2;initial=1 if alpha%2 else 2;a=(alpha-initial)//2
    A=[a];B=[a+initial];sd=sorted(d)
    for x,y in zip(sd[::2],sd[1::2]):
        delta=B[-1]-A[-1];g=y-x;sgn=1 if delta>0 else -1
        change=0 if g==0 else sgn if g==1 and abs(delta)==1 else -sgn*g
        u,v=(x,y) if all_smaller or change>=0 else (y,x)
        A.append(A[-1]+u);B.append(B[-1]+v)
    xs,word=physical(M,A,B)
    return dict(A=A,B=B,positions=xs,word=word,final_delta=B[-1]-A[-1])


def main():
    start=time.process_time()
    fixtures=[((2,2,2,4,4,4),25,11),((2,2,2,5,5,5),25,17),
              ((2,2,2,5,5,5),23,19),((2,4,4,4,4,6),25,23),
              ((2,2,2,4,4,5),23,15),((2,2,2,5,5,6),25,19)]
    rows=[construct(28,d,p,q,True) for d,p,q in fixtures]
    rows.extend((construct(10,(2,4),7,5),construct(12,(2,5),9,5),
                 construct(16,(2,5),11,3),construct(32,(2,3,3,6,6,6),27,25),
                 construct(500,tuple(v for i in range(10) for v in (2+4*i,5+4*i)),497,363)))
    assert len(rows)==11 and sum(r['bins'] is not None for r in rows)==6
    assert all(any(t['crossed'] for t in r['trace']) for r in rows)
    assert rows[2]['early_odd_pair'] and rows[2]['trace'][0]['after']==-1
    assert rows[4]['early_odd_pair'] and rows[4]['trace'][0]['after']==1
    assert any(t['before']==-2 and t['pair']==(5,6) and t['after']==-1 for t in rows[5]['trace'])
    load_edge=rows[9]
    assert load_edge['initial_delta']==2 and load_edge['final_delta']==-2
    assert load_edge['loads']==(15,11) and max(load_edge['A']+load_edge['B'])==15
    drift=shortcut(28,fixtures[3][0],25,23,True)
    assert drift['final_delta']==5 and max(drift['A']+drift['B'])==15
    assert not literal(28,drift['positions'])
    assert Counter(drift['word'])==Counter((25,23,-4,-8,-8,-8,-8,-12))
    collide=shortcut(28,fixtures[4][0],23,15)
    assert collide['A'][1]==collide['B'][0] and not literal(28,collide['positions'])
    assert Counter(collide['word'])==Counter((23,15,-4,-4,-4,-8,-8,-10))
    refused=[]
    for name,args in [('doubled_longest',(10,(2,5),7,7)),
                      ('long_edge',(10,(2,5),9,5)),
                      ('half1_scope',(28,(1,2,2,4,4,5),25,11)),
                      ('gap4_scope',(14,(2,6),11,5))]:
        try:construct(*args)
        except AssertionError:refused.append(name)
        else:raise AssertionError('missing refusal '+name)
    outside=[0,11,7,12];outside_word=[v-u for u,v in zip(outside,outside[1:]+outside[:1])]
    assert literal(14,outside) and instrument.literal_geometry(14,set(),outside)
    assert Counter(outside_word)==Counter((11,5,-4,-12))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='2574b6ff',
                         formula_calls=11,E28_partitions=6,rows=rows,
                         naive_all_smaller=drift,naive_pair_order=collide,
                         scope_rejections=refused,outside_gap4_positive=dict(positions=outside,word=outside_word),
                         unexpected_load_boundary=load_edge['loads'],cpu_seconds=elapsed,peak_rss_bytes=rss),
                     separators=(',',':')))


if __name__=='__main__':main()
