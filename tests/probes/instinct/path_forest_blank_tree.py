#!/usr/bin/env python3
"""B83/MI189 prereg4066824e: exact fixed-skeleton interior blank lifting.

Six lifts, six cut audits, two refusals, one B79 control, one sign-changing
compaction;two actual E28 partitions.1CPU sec/64MiB. No skeleton search.
Tree degree elimination is standard; general skeleton selection stays OPEN.
OUTCOME: all prescribed checks pass;0.001700CPU sec,17416192RSS bytes.
Raw SHA2560ccc40c6c39454c5edd9c35f666a152118e2c7dfe4fcba8b7f6c3540b4159c11.
"""
from collections import Counter,deque
import json
import resource
import time

import path_forest_balanced_bridge as instrument
import path_forest_coloured_chains as b79
from path_forest_interlaced_pairs import physical,literal


class Refused(Exception):pass


def skeleton(w):
    assert set(w)=={'A','B'}
    chains={c:[i for i,x in enumerate(w) if x==c] for c in 'AB'}
    gaps={}
    for c in 'AB':
        for i,(r,s) in enumerate(zip(chains[c],chains[c][1:])):
            gaps[c+str(i)]=(r,s)
    edges={}
    for j in range(1,len(w)):
        active=[e for e,(r,s) in gaps.items() if r<j<=s]
        assert len(active)<=2
        if len(active)==2:
            assert active[0][0]!=active[1][0];edges[j]=active
    # Independent union-find check of the graph's no-cycle claim.
    parent={e:e for e in gaps}
    def find(v):
        while v!=parent[v]:v=parent[v]
        return v
    for u,v in edges.values():
        u,v=find(u),find(v);assert u!=v;parent[u]=v
    return chains,gaps,edges


def solve(w,targets,k):
    chains,gaps,edges=skeleton(w)
    desired={c+str(i):d for c in 'AB' for i,d in enumerate(targets[c])}
    assert set(desired)==set(gaps)
    h={e:desired[e]-(s-r) for e,(r,s) in gaps.items()}
    if min(h.values(),default=0)<0:raise Refused('negative demand')
    if any(sum(v for e,v in h.items() if e[0]==c)!=k for c in 'AB'):
        raise Refused('unbalanced demand total')
    remaining={e:set() for e in gaps}
    for j,(u,v) in edges.items():remaining[u].add(j);remaining[v].add(j)
    queue=deque(e for e in gaps if len(remaining[e])<=1);z={};peeled=set();trace=[]
    while queue:
        u=queue.popleft()
        if u in peeled:continue
        if not remaining[u]:
            if h[u]!=0:raise Refused('nonzero isolated residual')
        else:
            assert len(remaining[u])==1
            j=next(iter(remaining[u]));v=next(v for v in edges[j] if v!=u)
            weight=h[u]
            if weight<0:raise Refused('negative edge')
            z[j]=weight;h[u]=0;h[v]-=weight
            trace.append(dict(leaf=u,edge=j,neighbour=v,weight=weight,neighbour_residual=h[v]))
            if h[v]<0:raise Refused('negative neighbour residual')
            remaining[u].remove(j);remaining[v].remove(j)
            if len(remaining[v])<=1:queue.append(v)
        peeled.add(u)
    assert len(peeled)==len(gaps) and set(z)==set(edges)
    if sum(z.values())!=k:raise Refused('wrong blank count')
    return z,dict(gaps=gaps,edges=edges,trace=trace)


def expand(w,z):
    assert all(0<=j<=len(w) and v>=0 and isinstance(v,int) for j,v in z.items())
    n=len(w)+sum(z.values());A=[];B=[]
    for i,c in enumerate(w):
        (A if c=='A' else B).append(i+sum(v for j,v in z.items() if j<=i))
    p=2*n-1-2*(A[0]+B[0]);q=2*(A[-1]+B[-1])-(2*n-1)
    dA=[v-u for u,v in zip(A,A[1:])];dB=[v-u for u,v in zip(B,B[1:])]
    xs,word=physical(2*n,A,B)
    assert word[0]==p and word[len(B)]==q
    assert Counter(word)==Counter((p,q,*(-2*d for d in dA+dB)))
    assert literal(2*n,xs) and instrument.literal_geometry(2*n,set(),xs)
    assert len(set(A+B))==len(A)+len(B)
    return dict(n=n,w=w,blanks=z,A=A,B=B,p=p,q=q,dA=dA,dB=dB,positions=xs,word=word)


def partition(row):
    assert row['n']==14 and row['p']>0 and row['q']>0
    d=row['dA']+row['dB'];assert len(d)==6
    e=[row['p'],row['q']]+[-2*v for v in d];h=[1,1]+[2]*6
    targets=[56*s+2*v for s,v in zip(h,e)]
    assert min(targets)>=68 and max(targets)<=122 and sum(targets)==784
    pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)};selected={}
    for j,move in enumerate(row['word']):
        owner=0 if j==0 else 1 if j==len(row['B']) else pool[-move//2].pop(0)
        assert e[owner]==move;selected[owner]=row['positions'][j]
    assert all(not v for v in pool.values())
    bins=instrument.materialize(28,set(),[0]*8,h,e,selected,targets)
    assert instrument.literal_ok(28,bins,targets,h) and instrument.independent_ok(28,bins,targets)
    row.update(targets=targets,bins=bins,selected=selected)


def lift(w,ta,tb,k):
    z,graph=solve(w,{'A':ta,'B':tb},k);row=expand(w,z);base=expand(w,{})
    assert row['dA']==list(ta) and row['dB']==list(tb)
    assert row['p']==base['p']+2*k and row['q']==base['q']+2*k
    assert row['p']>0 and row['q']>0
    row.update(graph=graph,base=base)
    return row


def main():
    start=time.process_time()
    rows=[lift('ABABBBBA',(2,11),(5,2,2,2),6),
          lift('ABABBBBA',(2,5),(2,1,1,1),0),
          lift('ABABBBBA',(2,17),(8,3,3,3),12),
          lift('ABABAB',(3,3),(3,3),2),
          lift('ABBBBA',(8,),(2,2,2),3),
          lift('AABB',(1,),(1,),0)]
    assert rows[0]['blanks']=={2:0,3:3,4:1,5:1,6:1}
    assert rows[0]['A']==[0,2,13] and rows[0]['B']==[1,6,8,10,12]
    assert (rows[0]['p'],rows[0]['q'])==(25,23);partition(rows[0])
    assert (rows[2]['p'],rows[2]['q'])==(37,35)
    assert [rows[3]['blanks'][j] for j in (2,3,4)]==[1,0,1]
    assert (rows[4]['p'],rows[4]['q'])==(15,13)
    audits=[]
    for w,j,change in [('AABB',0,(-2,2)),('AABB',1,(0,2)),('AABB',2,(0,0)),
                       ('AABB',3,(2,0)),('AABB',4,(2,-2)),('ABAB',2,(2,2))]:
        base=expand(w,{});after=expand(w,{j:1})
        assert (after['p']-base['p'],after['q']-base['q'])==change
        for c in 'AB':
            indices=[i for i,v in enumerate(w) if v==c]
            expected=[(s-r)+int(r<j<=s) for r,s in zip(indices,indices[1:])]
            assert after['d'+c]==expected
        audits.append(dict(base=base,cut=j,after=after,change=change))
    refused=[]
    for w,ta,tb,k in [('ABABAB',(4,2),(2,4),2),('AABB',(2,),(2,),1)]:
        try:lift(w,ta,tb,k)
        except Refused as e:refused.append(dict(w=w,A=ta,B=tb,k=k,reason=str(e)))
        else:raise AssertionError('missing fixed-skeleton refusal')
    positive=b79.sparse(16,13,11,[4,4,2,2])
    assert Counter(positive['word'])==Counter((13,11,-8,-8,-4,-4))
    compact=expand('ABBBBBBB',{});assert (compact['p'],compact['q'])==(13,-1)
    signlift=expand('ABBBBBBB',{0:4,6:1,7:1})
    assert signlift['A']==[4] and signlift['B']==[5,6,7,8,9,11,13]
    assert (signlift['p'],signlift['q'])==(9,7)
    assert signlift['dA']==[] and signlift['dB']==[1,1,1,1,2,2]
    partition(signlift)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='4066824e',
                         fixed_lifts=6,cut_audits=6,E28_partitions=2,rows=rows,audits=audits,
                         refused=refused,global_positive_despite_fixed_refusal=positive,
                         unexpected_compaction=dict(compact=compact,lifted=signlift),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
