#!/usr/bin/env python3
"""B79/MI180 preregb4de8b25: full coloured-chain fill and sparse contraction.

24 full-label formula calls,8 sparse calls (six E28 partitions), named scope
and wrong-deletion controls.2CPU sec/64MiB. No order, split or root search.
Hand full-label/sparse sufficient theorems remain SKETCH pending carrying read.
OUTCOME:24 full/8 sparse calls,6 actual E28 partitions and all named controls
pass.0.003476CPU sec,15544320bytes RSS. Raw SHA256
7067f4f35caf051cc01497dc304e6eb0ba582dedcd4b54cbe0203875f9007cb8.
"""
from collections import Counter
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def gaps(A,B):
    return [v-u for seq in (A,B) for u,v in zip(seq,seq[1:])]


def cycle(M,A,B):
    assert A==sorted(set(A)) and B==sorted(set(B)) and A[0]==0
    assert not set(A)&set(B) and len(A)>=2 and len(B)>=1
    xs=[0]+[M-1-2*v for v in B]+[2*u for u in reversed(A[1:])]
    word=[v-u for u,v in zip(xs,xs[1:]+[xs[0]])]
    assert word[0]==M-1-2*B[0]
    assert word[len(B)]==2*(A[-1]+B[-1])-(M-1)
    return xs,word


def validate(M,p,q,d,A,B,partition=False):
    xs,word=cycle(M,A,B)
    assert len(xs)==len(d)+2 and word[0]==p and word[len(B)]==q
    assert all(e<0 and e%2==0 for j,e in enumerate(word) if j not in (0,len(B)))
    # Physical differences, half-index gaps, and input sizes are separate bags.
    actual=Counter(-e//2 for e in word if e<0)
    assert actual==Counter(gaps(A,B))==Counter(d)
    assert all(0<=x<M for x in xs) and len(set(xs))==len(xs)
    labels=[min(x,M-1-x) for x in xs]
    assert len(set(labels))==len(xs) and instrument.literal_geometry(M,set(),xs)
    assert all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
    bins=None;targets=None;selected=None
    if partition:
        assert M==28 and len(d)==6
        e=[p,q]+[-2*v for v in d];h=[1,1]+[2]*6
        targets=[56*s+2*v for s,v in zip(h,e)]
        assert sum(targets)==784 and all(68<=v<=122 for v in targets)
        remaining={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)}
        selected={}
        for j,move in enumerate(word):
            owner=0 if j==0 else 1 if j==len(B) else remaining[-move//2].pop(0)
            assert e[owner]==move
            selected[owner]=xs[j]
        assert all(not v for v in remaining.values())
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h) and instrument.independent_ok(M,bins,targets)
    return dict(M=M,p=p,q=q,d=d,A=A,B=B,positions=xs,word=word,labels=labels,
                negative_bag=sorted(actual.items()),targets=targets,bins=bins,selected=selected)


def full(M,p,q,d,internal=None):
    n=M//2
    assert M%2==0 and len(d)==n-2 and min(d)>0
    assert p>=q>0 and p%2 and q%2 and p+q==2*sum(d)
    assert p<=M-3 and not(p==q==M-3)
    alpha=(M-1-p)//2;beta=(M-3-q)//2
    assert alpha>=1 and beta>=1
    high=[v for v in d if v>1]
    if internal is None:internal=high
    assert Counter(internal)==Counter(high)
    lengths=[alpha]+[v-1 for v in internal]+[beta]
    assert min(lengths)>=1 and sum(lengths)==n
    colours=[c%2 for c,length in enumerate(lengths) for _ in range(length)]
    A=[i for i,c in enumerate(colours) if c==0];B=[i for i,c in enumerate(colours) if c==1]
    assert set(A)|set(B)==set(range(n))
    row=validate(M,p,q,d,A,B)
    assert set(row['labels'])==set(range(n))
    row.update(run_lengths=lengths,colours=colours)
    return row


def sparse(M,p,q,d,partition=False):
    n=M//2;k=n-len(d)-2
    assert k>0 and len(d)>=2 and min(d)>0
    D,E=d[:2]
    assert min(D,E)>=k+2
    refined=[D-k]+list(d[1:])+[1]*k
    internal=[D-k,E]+[v for v in d[2:] if v>1]
    parent=full(M,p,q,refined,internal)
    first=sum(parent['run_lengths'][:2]);deleted=list(range(first,first+k))
    assert parent['run_lengths'][2]==E-1>=k+1
    assert set(deleted)<=set(parent['A'])
    A=[x for x in parent['A'] if x not in set(deleted)];B=parent['B']
    assert (A[0],A[-1],B[0],B[-1])==(parent['A'][0],parent['A'][-1],parent['B'][0],parent['B'][-1])
    row=validate(M,p,q,d,A,B,partition)
    row.update(label_deficit=k,deleted=deleted,refined=refined,parent=parent)
    return row


def main():
    start=time.process_time();rows=[]
    for n in (3,4,5,8,14,25):
        N=n-2
        rows.append(full(2*n,2*N-1,1,[1]*N))
        p=N if N%2 else N+1;q=2*N-p
        rows.append(full(2*n,p,q,[1]*N))
        rows.append(full(2*n,2*n-3,2*n-5,[n-1]+[1]*(n-3)))
        rows.append(full(2*n,2*n-3,2*n-5,[2]*N))
        assert len(rows)<=24 and time.process_time()-start<2
    assert len(rows)==24
    sparse_rows=[sparse(28,p,q,(8,8,1,1,1,1),True) for p,q in ((25,15),(23,17),(21,19))]
    for d in ((8,8,2,2,2,2),(10,10,1,1,1,1),(8,9,1,1,1,4)):
        sparse_rows.append(sparse(28,25,23,d,True))
    sparse_rows.append(sparse(20,17,11,(6,6,1,1)))
    sparse_rows.append(sparse(40,37,27,(14,14,1,1,1,1)))
    assert len(sparse_rows)==8
    hand=sparse_rows[2]
    assert hand['positions']==[0,21,5,3,1,20,4,2]
    assert hand['A']==[0,1,2,10] and hand['B']==[3,11,12,13]
    refusals=[]
    for name,fn in (
        ('doubled_long_edge',lambda:full(16,13,13,(1,1,1,2,4,4))),
        ('too_many_labels',lambda:full(6,3,1,(1,1))),
        ('two_large_admission_only',lambda:sparse(28,25,13,(7,8,1,1,1,1)))):
        try:fn()
        except AssertionError:refusals.append(name)
        else:raise AssertionError('scope rejection missing: '+name)
    parent=hand['parent'];first=sum(parent['run_lengths'][:2]);k=hand['label_deficit']
    too_many=set(range(first,first+k+1));bad_A=[x for x in parent['A'] if x not in too_many]
    bad_xs,bad_word=cycle(28,bad_A,parent['B'])
    assert instrument.literal_geometry(28,set(),bad_xs)
    assert len(bad_xs)!=len(hand['d'])+2
    assert bad_word[len(parent['B'])]!=hand['q']
    assert Counter(-e//2 for e in bad_word if e<0)!=Counter(hand['d'])
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='b4de8b25',
                         full_formula_calls=len(rows),sparse_formula_calls=len(sparse_rows),
                         E28_partitions=6,full=rows,sparse=sparse_rows,scope_rejections=refusals,
                         geometry_only_false_certificate=dict(A=bad_A,B=parent['B'],positions=bad_xs,word=bad_word),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
