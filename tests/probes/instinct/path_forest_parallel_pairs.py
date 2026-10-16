#!/usr/bin/env python3
"""B80/MI182 prereg712f33c0: paired halves>=2, parallel unit-offset chains.

Eight formula calls (four E28 partitions), size-one/jump-bound scope controls
and wrong-positive-owner geometry-only control.1CPU sec/64MiB. No search,
repair or widened family. General paired-move iff remains SKETCH.
OUTCOME:eight calls/four actual E28 partitions and all named controls pass;
three smaller-positive-first cases.0.001363CPU sec,15335424bytes RSS. Raw SHA256
cc53333c2dd4dfcf9fe33f4618766ba2433efe16172cf9ece66207ea80581ba5.
"""
from collections import Counter
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def raw(M,D,a):
    C=[0]
    for d in D:C.append(C[-1]+d)
    A=[a+x for x in C];B=[a+1+x for x in C]
    xs=[2*A[0]]+[M-1-2*v for v in B]+[2*u for u in reversed(A[1:])]
    word=[v-u for u,v in zip(xs,xs[1:]+[xs[0]])]
    return A,B,xs,word


def literal(M,xs):
    return (all(0<=x<M for x in xs) and len(set(xs))==len(xs)
            and len({min(x,M-1-x) for x in xs})==len(xs))


def construct(M,D,p,q,partition=False):
    assert M%2==0 and len(D)>=1 and min(D)>=2
    assert p>0 and q>0 and p%2 and q%2 and p+q==4*sum(D)
    assert max(p,q)<=M-3
    candidates=[i for i,v in enumerate((p,q)) if (v-(M-3))%4==0]
    assert len(candidates)==1
    first=candidates[0];P=(p,q)[first];Q=(p,q)[1-first]
    a=(M-3-P)//4
    assert a>=0 and a+sum(D)<=M//2-2
    A,B,xs,word=raw(M,D,a)
    assert not set(A)&set(B) and len(xs)==2*len(D)+2<=M//2
    assert literal(M,xs) and instrument.literal_geometry(M,set(),xs)
    assert all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
    assert word[0]==P and word[len(B)]==Q
    assert all(e<0 and e%2==0 for j,e in enumerate(word) if j not in (0,len(B)))
    expected=Counter((p,q,*(-2*d for d in D for _ in range(2))))
    assert Counter(word)==expected
    # Compare actual physical differences to both index-chain gap lists.
    halfbag=Counter(-e//2 for e in word if e<0)
    assert halfbag==Counter(v-u for seq in (A,B) for u,v in zip(seq,seq[1:]))
    d=[v for v in D for _ in range(2)]
    assert halfbag==Counter(d)
    targets=None;bins=None;selected=None
    if partition:
        assert M==28 and len(D)==3
        e=[p,q]+[-2*v for v in d];h=[1,1]+[2]*6
        targets=[56*s+2*v for s,v in zip(h,e)]
        assert all(68<=v<=122 for v in targets) and sum(targets)==784
        pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)}
        selected={}
        for j,move in enumerate(word):
            owner=first if j==0 else 1-first if j==len(B) else pool[-move//2].pop(0)
            assert e[owner]==move
            selected[owner]=xs[j]
        assert all(not v for v in pool.values())
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h) and instrument.independent_ok(M,bins,targets)
    return dict(M=M,D=D,p=p,q=q,first_positive_owner=first,first_positive=P,
                start_index=a,A=A,B=B,positions=xs,word=word,
                original_negative_halves=d,targets=targets,bins=bins,selected=selected)


def main():
    start=time.process_time()
    rows=[construct(8,(2,),5,3),construct(14,(2,3),11,9),
          construct(16,(2,3),11,9),construct(200,tuple(range(2,12)),197,63)]
    for D,pairs in (((2,3,5),((25,15),(23,17))),((3,3,5),((25,19),(23,21)))):
        for p,q in pairs:rows.append(construct(28,D,p,q,True))
    assert len(rows)==8 and sum(r['bins'] is not None for r in rows)==4
    assert rows[2]['first_positive']==9 and rows[5]['first_positive']==17
    assert rows[7]['first_positive']==21
    scope=[]
    for name,args in (('odd_jump_bound',(28,(3,3,5),27,17)),
                      ('paired_half_one_scope',(28,(1,3,7),25,19))):
        try:construct(*args)
        except AssertionError:scope.append(name)
        else:raise AssertionError('scope guard missing: '+name)
    A,B,bad_xs,bad_word=raw(28,(1,3,7),0)
    assert set(A)&set(B) and not literal(28,bad_xs)
    assert not instrument.literal_geometry(28,set(),bad_xs)
    # Deliberately floor the invalid root for input23/21: geometry alone passes.
    a=(25-23)//4
    _,_,wrong_xs,wrong_word=raw(28,(3,3,5),a)
    assert literal(28,wrong_xs) and instrument.literal_geometry(28,set(),wrong_xs)
    assert wrong_word[0]==25 and wrong_word[4]==19
    assert Counter(wrong_word)!=Counter((23,21,-6,-6,-6,-6,-10,-10))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='712f33c0',
                         formula_calls=len(rows),E28_partitions=4,rows=rows,scope_rejections=scope,
                         paired_half_one_geometry=dict(A=A,B=B,positions=bad_xs,word=bad_word),
                         wrong_owner_geometry_only=dict(positions=wrong_xs,word=wrong_word),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
