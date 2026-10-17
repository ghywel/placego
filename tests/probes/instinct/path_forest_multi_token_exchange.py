#!/usr/bin/env python3
"""B120/MI261: three original FIRST-anchor failures, no new target sample.

BEFORE RUN: predict all three have ordinary partitions retaining EXACT
FIRST anchors and slot counts, although their one-selected-token model
is impossible. Enumerate all size2/4 subsets with required sums, then
exact cover; return first witness, no policy change. Convert each witness
to one selected endpoint per free complementary pair, h_i outgoing and
incoming endpoints per bin, using even-degree graph orientation. Clone
permutation, aggregate moves and reconstructed bins must agree exactly.
Independent literal/token-bitset validators, mask subsets versus recursive
sum generation; loops/parallel edges/disconnected control. Wrong permutation
and reused-pair controls reject. Unexpected: keeping anchors in the graph
creates odd bin degrees and must be refused. Euler is known prior art;
application remains SKETCH, no general target-existence proof.
Caps3 targets,200k nodes/target,500k overall,5CPU sec/128MiB. Stop on
control failure/cap; preserve NO_WITNESS or UNKNOWN, no broader run.
REFUTED-BY: any original target without a witness within the fixed cap.
"""
from collections import Counter
from itertools import combinations
import json
import resource
import time

import path_forest_split_anchor_pilot as pilot


CASES=[(16461642,(77,77,83,85,107,117,119,119)),
       (6321549,(71,73,77,105,107,109,121,121)),
       (2079026,(69,69,75,103,111,116,120,121))]


class Cap(Exception):
    pass


class Budget:
    def __init__(self):
        self.start=time.process_time();self.total=0;self.local=0

    def check(self,node=False):
        if node:self.total+=1;self.local+=1
        if self.local>200000 or self.total>500000:raise Cap('nodes')
        if time.process_time()-self.start>5:raise Cap('cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>128*1024*1024:
            raise Cap('rss')


def candidate_reference(free,k,wanted):
    """Independent recursive increasing subsets with arithmetic pruning."""
    out=set()
    def visit(start,left,remain,mask):
        if not left:
            if remain==0:out.add(mask)
            return
        if len(free)-start<left:return
        if sum(free[start:start+left])>remain or sum(free[-left:])<remain:return
        for j in range(start,len(free)-left+1):
            visit(j+1,left-1,remain-free[j],mask|(1<<free[j]))
    visit(0,k,wanted,0)
    return out


def partition(t,R,a,h,budget):
    free=[x for x in range(28) if min(x,27-x) not in R]
    candidates=[]
    for target,anchor,slots in zip(t,a,h):
        k=2*slots;wanted=(target-anchor-k)//2
        assert target-anchor-k==2*wanted
        masks=[sum(1<<x for x in c) for c in combinations(free,k) if sum(c)==wanted]
        assert set(masks)==candidate_reference(free,k,wanted)
        candidates.append(masks);budget.check()
    failed=set();universe=sum(1<<x for x in free)
    def visit(left,used):
        budget.check(True)
        if not left:
            assert used==universe
            return {}
        if (left,used) in failed:return None
        options={i:[m for m in candidates[i] if not m&used] for i in left}
        i=min(left,key=lambda i:(len(options[i]),i))
        for m in options[i]:
            rest=visit(tuple(j for j in left if j!=i),used|m)
            if rest is not None:return {i:m,**rest}
        failed.add((left,used));return None
    masks=visit(tuple(range(8)),0)
    if masks is None:return None,[len(v) for v in candidates]
    bins=[sorted(([a[i]] if a[i] else [])+[2*x+1 for x in free if masks[i]>>x&1])
          for i in range(8)]
    assert pilot.literal_ok(bins,t,h) and pilot.independent_ok(bins,t)
    return bins,[len(v) for v in candidates]


def orient(M,core):
    """Orient unused-edge closed walks; loops contribute two to degree."""
    owner={x:i for i,b in enumerate(core) for x in b}
    assert len(owner)==sum(map(len,core))
    labels=sorted({min(x,M-1-x) for x in owner})
    assert all(r in owner and M-1-r in owner for r in labels)
    edges=[(owner[r],owner[M-1-r],r) for r in labels]
    degrees=Counter(v for u,w,_ in edges for v in (u,w))
    if any(v%2 for v in degrees.values()):raise ValueError('odd degree')
    unused=set(range(len(edges)));directed=[]
    while unused:
        j=min(unused);start=edges[j][0];v=start
        while True:
            incident=[j for j in sorted(unused) if v in edges[j][:2]]
            if not incident:break
            j=incident[0];unused.remove(j);u,w,r=edges[j]
            nxt=w if v==u else u
            # Baseline at tail keeps its final endpoint and sends the other.
            send=M-1-r if v==u else r
            assert owner[send]==nxt
            directed.append(dict(tail=v,head=nxt,label=r,send=send))
            v=nxt
        assert v==start
    incoming=Counter(e['head'] for e in directed)
    outgoing=Counter(e['tail'] for e in directed)
    assert incoming==outgoing
    return directed


def encode(M,core,h):
    assert [len(b) for b in core]==[2*v for v in h]
    edges=orient(M,core)
    outgoing=[[e['send'] for e in edges if e['tail']==i] for i in range(len(core))]
    incoming=[[e['send'] for e in edges if e['head']==i] for i in range(len(core))]
    assert list(map(len,outgoing))==list(h)==list(map(len,incoming))
    image={}
    for source,destination in zip(outgoing,incoming):
        image.update(zip(sorted(source),sorted(destination)))
    selected=list(image)
    assert len(selected)==len({min(x,M-1-x) for x in selected})==sum(h)
    assert Counter(image.values())==Counter(selected)
    rebuilt=[];moves=[]
    for source in outgoing:
        baseline={v for x in source for v in (x,M-1-x)}
        final=sorted((baseline-set(source))|{image[x] for x in source})
        assert len(final)==2*len(source)
        rebuilt.append(final);moves.append([image[x]-x for x in sorted(source)])
    assert rebuilt==[sorted(b) for b in core]
    return dict(edges=edges,outgoing=outgoing,permutation=sorted(image.items()),
                micro_moves=moves,rebuilt=rebuilt)


def controls():
    # Two parallel cross-bin edges plus a disconnected loop, all even degrees.
    core=[[0,1],[4,5],[2,3]]
    row=encode(6,core,[1,1,1])
    assert len(row['edges'])==3
    assert sum(e['tail']==e['head'] for e in row['edges'])==1
    # Two loops, with no genuine exchanges at all.
    loops=encode(4,[[0,3],[1,2]],[1,1])
    assert all(d==0 for ds in loops['micro_moves'] for d in ds)
    try:orient(4,[[0],[1,2,3]])
    except ValueError as e:assert str(e)=='odd degree'
    else:raise AssertionError('odd degree accepted')
    selected=[0,3]
    assert len({min(x,3-x) for x in selected})!=len(selected)
    wrong=dict(row['permutation']);keys=sorted(wrong);wrong[keys[0]]=wrong[keys[1]]
    assert Counter(wrong.values())!=Counter(wrong.keys())
    return dict(parallel_disconnected=row,loops=loops,
                odd_degree_rejected=True,reused_pair_rejected=True,
                wrong_permutation_rejected=True)


def main():
    budget=Budget();control=controls();rows=[]
    for rank,t in CASES:
        budget.local=0;R,a,h=next(pilot.policies(t))
        try:
            bins,counts=partition(t,R,a,h,budget)
            result=dict(rank=rank,targets=t,reserved=sorted(R),anchors=a,slots=h,
                        candidate_counts=counts,status='WITNESS' if bins else 'NO_WITNESS')
            if bins:
                core=[sorted((v-1)//2 for v in b if v!=a[i]) for i,b in enumerate(bins)]
                certificate=encode(28,core,h)
                moves=[(x-z-56*s)//2 for x,z,s in zip(t,a,h)]
                assert list(map(sum,certificate['micro_moves']))==moves
                reconstructed=[sorted(([a[i]] if a[i] else [])+[2*x+1 for x in c])
                               for i,c in enumerate(certificate['rebuilt'])]
                assert reconstructed==bins
                assert pilot.literal_ok(reconstructed,t,h) and pilot.independent_ok(reconstructed,t)
                assert any(sum(d!=0 for d in ds)>1 for ds in certificate['micro_moves'])
                # Leaving singleton anchors in the graph violates degree balance.
                try:orient(28,[[(v-1)//2 for v in b] for b in bins])
                except ValueError as e:assert str(e)=='odd degree'
                else:raise AssertionError('anchors retained in Euler graph')
                result.update(bins=bins,moves=moves,certificate=certificate,
                              anchor_removal_control='ODD_DEGREE_REJECTED')
            result['nodes']=budget.local;rows.append(result)
        except Cap as e:
            rows.append(dict(rank=rank,status='UNKNOWN',cap=str(e),nodes=budget.local));break
    print(json.dumps(dict(status='COMPLETE_FIXED_THREE' if len(rows)==3 else 'PARTIAL_CAP',
        prediction_all_original_allocations_work=len(rows)==3 and all(r['status']=='WITNESS' for r in rows),
        rows=rows,controls=control,total_nodes=budget.total,
        cpu_seconds=time.process_time()-budget.start,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),separators=(',',':')))


if __name__=='__main__':
    main()
