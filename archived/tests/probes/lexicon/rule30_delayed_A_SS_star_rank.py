"""GC1102: transport the GC1101 potential through arbitrary white SS blocks.

Missing inference: the one-SS A reset has a finite decreasing rank,
but variable SS block lengths might restore it. Compute the exact
least fixed point of the same sound20-cell boundary relaxation for
M_k=S-D101-H-SS^k-Ablack11, all k>=1, not a finite k cutoff.
Record searched: white.SS|SS.block|delayed with potential|rank|arbitrary|
repeat ->34 hits13files; GC1100/1101, GC1056 and CL277 read.
P1 BEFORE run: every all-k macro edge still lowers GC1101's explicit
rank. P2 if P1 fails: the all-k graph is nevertheless acyclic with
height<=3. A cycle closes this potential candidate; retain its actual
finite relaxation edges and do not sweep larger widths.
Counterfactual: inserting extra SS restores a positive-rank packet,
so the proven k=1 bound does not control repeated variable blocks.
Controls: k=1 edges exactly match GC1101; the actual GC1100 path is
retained; independent scalar six-tick set flows check selected SS
origins; fresh low NONVACUOUS gives two genuine SS blocks.
Unexpected check: reachable inner SS recurrence can survive even if
the A-return graph is acyclic. Test inner recurrence separately; do
not infer a bound on SS residence from a bound on reset counts.
P1/P2 REFUTED: the all-k relation has742 edges and a self-loop at
11101000111111110100;192 edges do not lower the old potential.
The fixed point needs three waves, but that alone is not a duration
proof. Do not widen the strip or infer no actual lift from a cycle.
P3 BEFORE independent SS-potential extraction: the reachable inner
SS graph has height<=2, hence at most three consecutive SS blocks
after this A-S-D-H ancestry. Verify a decreasing vertex potential
and fixed-point closure, rather than extrapolating the three waves.
P4 BEFORE path extraction: the named A self-loop first appears with
two SS blocks. An explicit free-boundary path will violate the
column21 black-mask temporal update; one failed path does not exclude
other lifts of that same loop. Retain this attribution distinction.
P3/P4 HELD: the explicit137-vertex SS potential has rank counts
81,49,7 at heights0,1,2 and strictly decreases on244 inner edges.
Thus at most three SS blocks follow any represented A-S-D101-H
ancestry, uniformly in even age and exterior. The named A self-loop
first occurs at k=2; one stored boundary path fails seven column21
updates. Actual loop realizability remains OPEN, not refuted.
No solver, CUT, exact visible membership, or relaxed-record run.
"""
from collections import deque
import rule30_delayed_A_strip_rank as q
from rule30_black_A_white_SS_entrance import WHITE_SS, ACTUAL
from rule30_white_SS_exit_guard import NONVACUOUS
from rule30_sl_no_refork import bits,run

AP={q.pack(bits('111010001'+s)) for s in ('1100','1101','1111')}
SSMASK=(1<<9)-1
SSPREFIX={q.pack(x) for x in WHITE_SS}

# Explicit finite certificate on the all-k reachable SS packets.
SS_RANK_ONE={
    0x617, 0x2617, 0xc617, 0x14617, 0x1a617, 0x1c617, 0x1e617, 0x20617,
    0x2e617, 0x32617, 0x34617, 0x3a617, 0x3c617, 0x54617, 0x5a617, 0x5c617,
    0x60617, 0x62617, 0x6c617, 0x6e617, 0x72617, 0x7c617, 0x7e617, 0x80617,
    0x82617, 0x8c617, 0x94617, 0x9a617, 0x9c617, 0x9e617, 0xa0617, 0xae617,
    0xb2617, 0xb4617, 0xba617, 0xbc617, 0xc2617, 0xcc617, 0xdc617, 0xde617,
    0xe0617, 0xe2617, 0xec617, 0xee617, 0xf2617, 0xf4617, 0xfa617, 0xfc617,
    0xfe617,
}
SS_RANK_TWO={
    0x8617, 0x28617, 0x48617, 0x88617, 0xa8617, 0xc8617, 0xe8617,
}


def flow(labels,track,pins=None):
    for t,b in enumerate(track):
        nxt={}
        for x,origins in labels.items():
            if (x>>4)&1!=b:continue
            for y in q.successors(x,t):nxt[y]=nxt.get(y,0)|origins
        if pins and t+1 in pins:
            p=pins[t+1];m=(1<<len(p))-1;v=q.pack(p)
            nxt={y:o for y,o in nxt.items() if y&m==v}
        labels=nxt
    return labels


def initial():
    starts=[a|(v<<13) for a in sorted(AP) for v in range(128)]
    labels={x:1<<i for i,x in enumerate(starts)}
    h=flow(labels,q.S+q.D+q.H,{6:bits('111001001'),16:bits('1110011011'),26:bits('111010')})
    return starts,{x:o for x,o in h.items() if x&SSMASK in SSPREFIX}


def edges(starts,ends):
    index={x:i for i,x in enumerate(starts)};out=[set() for _ in starts]
    for x,origins in ends.items():
        while origins:
            low=origins&-origins;i=low.bit_length()-1
            out[i].add(index[x]);origins^=low
    return out


def closure(starts,entrances):
    seen={};delta=entrances;ends={};rounds=[];first_ends=None
    while delta:
        for x,o in delta.items():seen[x]=seen.get(x,0)|o
        out=flow(delta,q.SS)
        # Every black11 A exit is one of the three represented types.
        for x in out:
            if x&((1<<9)-1)==q.pack(bits('111010001')) and (x>>10)&1:
                assert x&q.AMASK in AP
            assert (x>>5)&1==0
        for x,o in out.items():
            if x&q.AMASK in AP:ends[x]=ends.get(x,0)|o
        if first_ends is None:first_ends=ends.copy()
        nxt={x:o&~seen.get(x,0) for x,o in out.items() if x&SSMASK in SSPREFIX}
        delta={x:o for x,o in nxt.items() if o}
        rounds.append((len(out),len(delta),sum(o.bit_count() for o in delta.values())))
        # The finite-domain bound is a termination proof, not a k cap.
        assert len(rounds)<=len(SSPREFIX)*(1<<(q.WIDTH-9))*len(starts)+1
    return seen,ends,first_ends,rounds


def cycle_iterative(graph):
    done=set();active={};path=[]
    for root in range(len(graph)):
        if root in done:continue
        active[root]=0;path=[root];stack=[iter(sorted(graph[root]))]
        while stack:
            v=path[-1]
            try:w=next(stack[-1])
            except StopIteration:
                done.add(v);del active[v];path.pop();stack.pop();continue
            if w in active:return path[active[w]:]+[w]
            if w in done:continue
            active[w]=len(path);path.append(w);stack.append(iter(sorted(graph[w])))
    return None


def dag_heights(graph):
    indeg=[0]*len(graph)
    for row in graph:
        for j in row:indeg[j]+=1
    queue=deque(i for i,n in enumerate(indeg) if not n);order=[]
    while queue:
        i=queue.popleft();order.append(i)
        for j in graph[i]:
            indeg[j]-=1
            if not indeg[j]:queue.append(j)
    assert len(order)==len(graph)
    h={}
    for i in reversed(order):h[i]=max((1+h[j] for j in graph[i]),default=0)
    assert all(h[i]>h[j] for i,row in enumerate(graph) for j in row)
    return h


def selfloop_path(start,k):
    track=q.S+q.D+q.H+q.SS*k
    states={start};parents=[]
    pins={6:bits('111001001'),16:bits('1110011011'),26:bits('111010')}
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x>>4)&1!=b:continue
            if t>=26 and (t-26)%6==0 and x&SSMASK not in SSPREFIX:continue
            for value,y in enumerate(q.successors(x,t)):
                if t+1 in pins:
                    pre=pins[t+1];m=(1<<len(pre))-1
                    if y&m!=q.pack(pre):continue
                nxt.setdefault(y,(x,value))
        parents.append(nxt);states=set(nxt)
    if start not in states:return None
    rows=[start];boundary=[];x=start
    for layer in reversed(parents):
        x,value=layer[x];rows.append(x);boundary.append(value)
    rows.reverse();boundary.reverse()
    assert rows[0]==rows[-1]==start
    assert all(rows[t+1] in q.scalar_successors(rows[t],t) for t in range(len(track)))
    return rows,boundary


def main():
    starts,entrances=initial()
    seen,ends,first,rounds=closure(starts,entrances)
    k1=edges(starts,first);old,old_edges,_=q.macro_relation(False,True)
    assert {(starts[i],starts[j]) for i,row in enumerate(k1) for j in row}=={
        (old[i],old[j]) for i,row in enumerate(old_edges) for j in row}
    graph=edges(starts,ends)
    bad=[(starts[i],starts[j]) for i,row in enumerate(graph) for j in row
         if q.potential(starts[i])<=q.potential(starts[j])]
    cycle=cycle_iterative(graph)
    assert sum(map(len,graph))==742 and len(bad)==192
    # Check the actual postfixed-point certificate of all-k coverage.
    complete=flow(seen,q.SS)
    assert {x:o for x,o in complete.items() if x&q.AMASK in AP}==ends
    assert all(not(o&~seen.get(x,0)) for x,o in complete.items() if x&SSMASK in SSPREFIX)
    nodes=sorted(seen);labels={x:1<<i for i,x in enumerate(nodes)}
    inner_out=flow(labels,q.SS)
    inner=edges(nodes,{x:o for x,o in inner_out.items() if x in seen})
    inner_cycle=cycle_iterative(inner)
    assert inner_cycle is None
    height=dag_heights(inner)
    assert max(height.values())==2
    assert max(height[nodes.index(x)] for x in entrances)==2
    explicit=lambda x:2 if x in SS_RANK_TWO else (1 if x in SS_RANK_ONE else 0)
    assert len(SS_RANK_ONE)==49 and len(SS_RANK_TWO)==7
    assert SS_RANK_ONE|SS_RANK_TWO<=set(nodes)
    assert all(height[i]==explicit(x) for i,x in enumerate(nodes))
    assert all(explicit(nodes[i])>explicit(nodes[j]) for i,row in enumerate(inner) for j in row)
    rank_counts={h:list(height.values()).count(h) for h in sorted(set(height.values()))}
    controls=0
    for x in nodes[::max(1,len(nodes)//8)][:8]:
        scalar={x}
        for t,b in enumerate(q.SS):
            scalar={y for a in scalar if (a>>4)&1==b for y in q.scalar_successors(a,t)}
        assert scalar==set(flow({x:1},q.SS));controls+=1
    rows=run(NONVACUOUS+(0,)*60,32)
    for t in (20,26):
        x=q.pack(rows[t][:20]);y=q.pack(rows[t+6][:20])
        assert x&SSMASK in SSPREFIX and y in flow({x:1},q.SS)
    actual=run(ACTUAL+(0,)*40,38)
    assert starts.index(q.pack(actual[38][:20])) in graph[starts.index(q.pack(actual[6][:20]))]
    # The necessary boundary-update condition accepts a real history.
    actual_boundary_black=0
    for t in range(6,38):
        if actual[t][20]:
            assert actual[t+1][20]==1-actual[t][19]
            actual_boundary_black+=1
    assert actual_boundary_black
    fmt=lambda x:''.join(map(str,q.unpack(x)))
    target=q.pack(bits('11101000111111110100'))
    assert selfloop_path(target,1) is None
    loop=selfloop_path(target,2)
    assert loop is not None
    path,boundary=loop
    violations=[t for t in range(len(boundary)-1)
                if boundary[t] and boundary[t+1]!=1-((path[t]>>19)&1)]
    assert violations
    print(dict(all_k_edges=sum(map(len,graph)),all_k_image=len(ends),
               SS_entrances=len(entrances),reachable_SS=len(seen),
               fixed_point_rounds=rounds,rank_violations=len(bad),
               A_selfloop=fmt(target),selfloop_SS_blocks=2,
               selfloop_boundary=''.join(map(str,boundary)),
               one_path_boundary_update_violations=violations,
               inner_SS_edges=sum(map(len,inner)),inner_SS_rank_counts=rank_counts,
               max_SS_blocks_after_A_D_H=3,scalar_SS_controls=controls,
               actual_boundary_mask_controls=actual_boundary_black,
               all_k_reset_potential='REFUTED in relaxation',
               actual_selfloop_lift='OPEN',all_depth_record_bound='OPEN'),flush=True)

if __name__=='__main__':main()
