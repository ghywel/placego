"""GC1105: the111 diversion of a typed black-eleventh A return.

Missing inference: can A-S-D111-H replenish GC1103's A exception
budget, bypassing its D101-H-whiteSS relation? Keep its same-history
20-cell origin labels, and classify both H exits. An unconditional
X exit of the high-LL branch would remove this particular reentry;
a surviving D or A route must be retained as a concrete obstruction.
Record searched: GC1091|diversion|black.eleventh with
111.*replenish|high.restart ->2 hits2files; GC1080/1091/1101..1104
sources read. The old no111 prediction is already refuted.
P1 BEFORE run: every H-low endpoint after this A-S-D111 ancestry
has sites10,11 black, and hence selects X rather than D. P2 BEFORE
run: every H-S endpoint has white marker6, so the same white-SS
output certificate could apply after its entrance is established.
Counterfactual: this diversion can directly return black A or high
LL followed by D; either would retain a replenishment route outside
GC1103. Stop on a concrete failure, not a larger strip sweep.
Controls: independent scalar complete20-cell images for selected
origin flows; actual GC1091 all-tail cylinder must remain represented.
Unexpected check: black-marker S may persist after H111, in contrast
to H101; distinguish this from a mere S/SS prefix classification.
No solver, CUT, membership, wider strip or relaxed-record run.
P1/P2 REFUTED:107 H-low packets include66 with pair00 selecting D;
all121 H-S packets have black marker6. The actual X cylinder survives.
P3 BEFORE gate check: the66 retained D endpoints cannot satisfy
GC1080's inherited renewal family B (10..17=00110000,18 OR19=1).
If true, the next D-H cannot be another high LL; prove the gate
exclusion on this same-history set rather than assume pair00 suffices.
P4 BEFORE short composition: the121 black S endpoints do not return
A through one SS. A counter retains immediate rank replenishment.
P3/P4 REFUTED: two low packets meet family B;17 black A endpoints
follow one SS. These are relaxation paths, not claimed actual lifts.
P5 BEFORE structural low-branch closure: those two family-B packets
force pair11 at the next H-low endpoint and hence X. This would
bound consecutive high LL diversions after typed A by two H blocks,
without a cutoff or global admission claim. Check unfiltered
continuations and a complete local causal cone for a sufficient
family-B prefix; retain every other exit.
P5 pair11 prediction REFUTED: the46 next H-low endpoints have00
or11, but their13-prefixes are1110010010000,1110010010001 or
1110010011101. Thus none meets family B. P6 BEFORE final exclusion:
no third consecutive D111-H-low follows typed A in this relaxation;
verify the necessary family-B gate against every second low packet
and directly compose once, retaining other D/H exits. The precise
bound is two, with no claim of actual sharpness. Independently
reproduce the two family-B continuations with scalar set updates.
P7 BEFORE exception check: the immediate17 A-return packets from
black SS cannot increase GC1103's exception rank. A failing labelled
edge keeps reset-budget replenishment open even if P6 holds.
P6 HELD; P7 REFUTED:98 labelled edges increase the existing rank.
P8 BEFORE terminal composition: pair00 second-H low packets force
D and land in C/J, while pair11 selects X. Check the forced track
unfiltered and classify the complete core guard, not just the101
label. A failed guard retains the remaining escape explicitly.
P8 REFUTED:24 pair00 origins force D, but36 of86 endpoints are
outside the established C/J guard. All endpoints are010 or101,
so a third111 return is barred before its H is even considered.
OUTCOME: finite hidden certificate bounds consecutive D111-H-low
blocks following a typed A-S by two, uniformly at every even age
and exterior. The two family-B20 packets differ only at site20;
their19-cell prefix forces D111-H-low without track filtering.
No actual sharpness asserted. Immediate black-SS A reentry and98
rank increases survive this relaxation; the reset-budget extension
is OPEN. No extra complete-cone check was run for the false P5
pair11 claim. Scalar origin controls8, family-B flows2 and the
GC1091 actual-history control are independent of packed transport.
Record correction: high.LL with two|bound|budget ->35 hits16files;
GC1082 read. Its reviewed all-length two-high budget already covers
this long-run bound. The2-block computation is a control, not a new
theorem. The new obstruction is the111-to-blackSS A rank increases.
Record searched:111.diversion|D111|black.SS with all.k|fixed.point|
exception.rank|potential before the next check; no prior combined
111/101 all-k A exception graph found. P9 BEFORE fixed-point run:
after arbitrary SS following the111 diversion, adding its A edges
to GC1103's existing101 relation admits a finite potential charging
every macro except its recurrent M2. Retain complete origin labels
through the monotone SS fixed point (both marker colours), not a k
cutoff. A new recurrent non-M2 edge closes that extension candidate.
P9 structural obstruction:111 SS fixed point has1115 packets,
68 A endpoints/7166 edges; combined with101 graph it has one21-state
recurrent component,231111 edges. Inner SS has a two-block cycle.
This alone does not prove a non-M2 recurrent output:111 and101 may
have the same visible word. P10 BEFORE shortest-path extraction:
the named self-edge11101000111011100000 has SS count other than2.
Use finite visited-set BFS on SS macro packets, then replay the
complete time-level witness with an independent scalar engine.
P10 HELD: shortest named self-return uses three SS blocks and
outputs h(SLLSSS),44 ticks. Thus the original M2 exception-potential
extension is REFUTED in this exact20-cell relaxation. A packet
self-loop cannot strictly lower any finite vertex potential. This
does not imply an actual right-half lift or rule out every finite-
type certificate. No wider strip or extra realization scan follows.
Next missing inference: a same-history111/black-SS guard separating
the new M3 recurrence from the reviewed101/white-SS M2 component.
"""
import rule30_delayed_A_SS_star_rank as r
from rule30_black_SS_high_restart import SOURCE
from rule30_sl_no_refork import bits,run
from rule30_delayed_A_boundary_memory import exception_rank,recurrent_language
from rule30_delayed_A_exit_admission import core_long

q=r.q
LOW=q.pack(bits('111001'))
HIGH=q.pack(bits('111001111'))


def diversion(starts, scalar=False):
    labels={x:1<<i for i,x in enumerate(starts)}
    counts=[]
    pins={6:bits('111001001'),16:bits('111001111')}
    for t,b in enumerate(q.S+q.D+q.H):
        nxt={}
        for x,o in labels.items():
            if (x>>4)&1!=b:continue
            step=q.scalar_successors(x,t) if scalar else q.successors(x,t)
            for y in step:nxt[y]=nxt.get(y,0)|o
        if t+1 in pins:
            pre=pins[t+1];mask=(1<<len(pre))-1;v=q.pack(pre)
            nxt={y:o for y,o in nxt.items() if y&mask==v}
        labels=nxt;counts.append(len(labels))
    return labels,counts


def family_b(x):
    return ((x>>9)&255==q.pack(bits('00110000')) and bool((x>>17)&3))


def unfiltered(states,track):
    for t,b in enumerate(track):
        assert all((x>>4)&1==b for x in states)
        states={y for x in states for y in q.successors(x,t)}
    return states


def scalar_flow(states,track):
    for t,b in enumerate(track):
        assert all((x>>4)&1==b for x in states)
        states={y for x in states for y in q.scalar_successors(x,t)}
    return states


def ss_closure(entrances):
    seen={};delta=entrances;ends={};waves=0
    while delta:
        for x,o in delta.items():seen[x]=seen.get(x,0)|o
        out=r.flow(delta,q.SS)
        for x,o in out.items():
            assert (x>>4)&1
            if x&q.AMASK in r.AP:ends[x]=ends.get(x,0)|o
        delta={x:o&~seen.get(x,0) for x,o in out.items()}
        delta={x:o for x,o in delta.items() if o};waves+=1
        assert waves<=len(entrances)*(1<<q.WIDTH)*384+1
    complete=r.flow(seen,q.SS)
    assert all(not(o&~seen.get(x,0)) for x,o in complete.items())
    assert {x:o for x,o in complete.items() if x&q.AMASK in r.AP}==ends
    return seen,ends,waves


def recurrent_components(graph):
    reach={}
    for root in graph:
        seen={root};todo=[root]
        while todo:
            x=todo.pop()
            for y in graph[x]-seen:seen.add(y);todo.append(y)
        reach[root]=seen
    remaining=set(graph);out=[]
    while remaining:
        root=min(remaining)
        comp={x for x in remaining if root in reach[x] and x in reach[root]}
        remaining-=comp
        if len(comp)>1 or root in graph[root]:out.append(comp)
    return out


def shortest_return(start):
    end,_=diversion([start]);states={x for x in end if (x>>4)&1}
    seen=set();k=0
    while states:
        seen|=states;k+=1
        states=set(r.flow({x:1 for x in states},q.SS))
        if start in states:return k
        states-=seen
    return None


def full_path(start,k):
    states={start};parents=[]
    pins={6:bits('111001001'),16:bits('111001111')}
    for t,b in enumerate(q.S+q.D+q.H+q.SS*k):
        nxt={}
        for x in sorted(states):
            if (x>>4)&1!=b:continue
            for y in q.successors(x,t):
                if t+1 in pins:
                    p=pins[t+1]
                    if y&((1<<len(p))-1)!=q.pack(p):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert start in states
    path=[start]
    for layer in reversed(parents):path.append(layer[path[-1]])
    path.reverse()
    assert path[0]==path[-1]==start
    assert all(path[t+1] in q.scalar_successors(x,t) for t,x in enumerate(path[:-1]))
    return path


def main():
    starts,_=r.initial()
    end,counts=diversion(starts)
    low={x:o for x,o in end.items() if x&63==LOW}
    short={x:o for x,o in end.items() if (x>>4)&1}
    bad_low=[x for x in low if (x>>9)&3!=3]
    black_short=[x for x in short if (x>>5)&1]
    familyB=[x for x in low if family_b(x)]
    ss=r.flow(short,q.SS)
    a_returns={x:o for x,o in ss.items() if x&q.AMASK in r.AP}
    all_ss,all_a,ss_waves=ss_closure(short)
    all_111_edges={(starts[i],x) for x,o in all_a.items()
                   for i in range(len(starts)) if (o>>i)&1}
    _,_,old_edges=recurrent_language()
    combined={x:set() for x in starts}
    for a,z in set(old_edges)|all_111_edges:combined[a].add(z)
    components=recurrent_components(combined)
    recurrent_111=[(a,z) for comp in components for a,z in all_111_edges
                   if a in comp and z in comp]
    named=min(a for a,z in recurrent_111 if a==z)
    named_k=shortest_return(named)
    named_path=full_path(named,named_k)
    assert named==q.pack(bits('11101000111011100000')) and named_k==3
    assert ''.join(str(x&1) for x in named_path[:-1])==(
        '110100'+'1101000100'*2+'110100'*3)
    inner_nodes=sorted(all_ss)
    inner_out=r.flow({x:1<<i for i,x in enumerate(inner_nodes)},q.SS)
    inner=r.edges(inner_nodes,inner_out)
    inner_cycle=r.cycle_iterative(inner)
    assert len(all_ss)==1115 and len(all_a)==68 and len(all_111_edges)==7166
    assert sorted(map(len,components))==[21] and len(recurrent_111)==231
    assert inner_cycle is not None
    second=r.flow({x:1 for x in familyB},q.D+q.H,
                  {10:bits('111001111')})
    second_low=[x for x in second if x&63==LOW]
    assert not any(family_b(x) for x in second_low)
    third=r.flow({x:1 for x in second_low},q.D+q.H,
                 {10:bits('111001111')})
    assert not any(x&63==LOW for x in third)
    second_d={x for x in second_low if (x>>9)&3==0}
    second_d_end=unfiltered(second_d,q.D)
    noncore=[x for x in second_d_end if not core_long(x)]
    assert {x&r.SSMASK for x in second_d_end}=={
        q.pack(bits('111001010')),q.pack(bits('111001101'))}
    assert all((x>>9)&1 for x in second_d_end
               if x&r.SSMASK==q.pack(bits('111001101')))
    rank_increases=[]
    for z,origins in a_returns.items():
        while origins:
            b=origins&-origins;a=starts[b.bit_length()-1];origins^=b
            if exception_rank(z)>exception_rank(a):rank_increases.append((a,z))
    fmt=lambda x:''.join(map(str,q.unpack(x)))
    assert len(end)==228 and len(low)==107 and len(short)==121
    assert len(bad_low)==66 and len(black_short)==121
    assert {fmt(x) for x in familyB}=={
        '11100100100110000010','11100100100110000011'}
    assert len(second)==46 and set(second)==set(second_low)
    assert {fmt(x)[:13] for x in second}=={
        '1110010010000','1110010010001','1110010011101'}
    assert len(second_d)==24 and len(second_d_end)==86 and len(noncore)==36
    assert len(a_returns)==17 and len(rank_increases)==98
    # Independent scalar transport; every path has the prescribed
    # fifth track and the D111 pin is forced without filtering.
    for x in familyB:
        scalar=scalar_flow({x},q.D)
        assert all(y&r.SSMASK==HIGH for y in scalar)
        scalar=scalar_flow(scalar,q.H)
        assert scalar==set(r.flow({x:1},q.D+q.H,{10:bits('111001111')}))
    assert unfiltered(set(familyB),q.D+q.H)==set(second)
    for x in starts[::48]:
        assert diversion([x],True)[0]==diversion([x])[0]
    for x in sorted(all_ss)[::max(1,len(all_ss)//8)][:8]:
        scalar={x}
        for t,b in enumerate(q.SS):
            scalar={y for a in scalar if (a>>4)&1==b
                    for y in q.scalar_successors(a,t)}
        assert scalar==set(r.flow({x:1},q.SS))
    actual=run(SOURCE+(0,)*50,42)
    a=q.pack(actual[6][:20]);z=q.pack(actual[32][:20])
    assert z in end and end[z]&(1<<starts.index(a))
    assert tuple(row[4] for row in actual[6:32])==q.S+q.D+q.H
    assert tuple(row[4] for row in actual[32:42])==bits('0101100101')
    assert set(end)==set(low)|set(short)
    print(dict(origins=len(starts),H_endpoints=len(end),low_endpoints=len(low),
               short_endpoints=len(short),bad_low_pair=len(bad_low),
               first_bad_low=fmt(bad_low[0]) if bad_low else None,
               black_marker_short=len(black_short),
               first_black_short=fmt(black_short[0]) if black_short else None,
               short_prefix13=sorted({fmt(x)[:13] for x in short}),
               low_prefix13=sorted({fmt(x)[:13] for x in low}),
               inherited_familyB=len(familyB),
               first_familyB=fmt(familyB[0]) if familyB else None,
               black_SS_A_returns=len(a_returns),
               first_A_return=fmt(next(iter(a_returns))) if a_returns else None,
               second_H_endpoints=len(second),second_H_low=len(second_low),
               second_low_pairs=sorted({fmt(x)[9:11] for x in second_low}),
               second_low_prefix13=sorted({fmt(x)[:13] for x in second_low}),
               third_H_endpoints=len(third),third_H_low=0,
               immediate_A_rank_increases=len(rank_increases),
               first_rank_increase=[fmt(x) for x in rank_increases[0]] if rank_increases else None,
               second_D_origins=len(second_d),second_D_endpoints=len(second_d_end),
               second_D_noncore=len(noncore),
               first_second_D_noncore=fmt(noncore[0]) if noncore else None,
               scalar_origin_controls=8,scalar_family_B_controls=2,
               scalar_SS_controls=8,
               maximum_consecutive_H_low=2,
               all_SS_reachable=len(all_ss),all_SS_closure_waves=ss_waves,
               all_SS_A_endpoints=len(all_a),all_111_A_edges=len(all_111_edges),
               combined_recurrent_components=sorted(map(len,components)),
               recurrent_111_edges=len(recurrent_111),
               first_recurrent_111=[fmt(x) for x in sorted(recurrent_111)[0]] if recurrent_111 else None,
               named_selfedge=fmt(named),named_SS_length=named_k,
               named_column1=''.join(str(x&1) for x in named_path[:-1]),
               inner_SS_cycle=[fmt(inner_nodes[i]) for i in inner_cycle] if inner_cycle else None,
               actual_GC1091='PASS',all_depth_record_bound='OPEN'))


if __name__=='__main__':main()
