"""GC1103: decide the named two-SS loop with its boundary evolving jointly.

Missing inference: GC1102's20-cell M_2 self-loop has a bad chosen
column21 history, but other histories might satisfy the boundary's
own Rule30 update. Retain exactly that identified missing equation,
not a width sweep: x is sites1..20, b is site21, c is a fresh site22.
x' is the actual20-cell update using b; b'=a XOR(b OR c), a=site20.
Thus b=1 forces b'=1-a, while b=0 permits either next b. Every
actual history projects to this finite hidden relation.
Record searched: column21|GC1102|11101000111111110100 with
boundary|lift|mask|loop ->6 hits4files; GC1101/1102 sources read.
P1 BEFORE run: no joint-boundary M_2 path returns the named20-packet
11101000111111110100, for either initial or terminal b. If false,
retain the complete2x2 initial/terminal boundary relation and a path;
do not call a surviving path an actual right-half realization.
Counterfactual: temporal consistency removes only the previously
chosen bad boundary word; a different lift preserves the obstruction.
Controls: independently written scalar21-cell transitions and whole
macro set flows; the actual GC1100 M_1 path remains represented;
forgetting b projects inside GC1102's free-boundary relation.
Unexpected check: even a surviving one-block path need not repeat
with its boundary state. Inspect the2x2 boundary-return graph,
including a possible two-cycle; do not demand b'=b prematurely.
No solver, CUT, exact visible membership or relaxed-record run.
REFUTED-BY: GC1102's inconsistent boundary word fails the new joint
transition; the known-wrong variant that it remains a valid lift is
explicitly rejected in main. The actual GC1100 history is retained.
P1 REFUTED: the complete boundary relation is0->0 and0->1. Black
initial b dies at the101 pin (tick16); white b has a recurrent lift.
The explicit21-cell controlled strip is therefore still cyclic.
P2 BEFORE the switch to structural cycle-language analysis: all
recurrent edges in GC1102's existing20-cell graph have k=2, so its
recurrent macro output is a single periodic word even if packets
branch. A different recurrent k refutes this explanation. Reuse the
existing graph; no wider-strip, solver, membership or record run.
Counterfactual for P2: one SCC mixes k=1,2,3 returns, retaining a
nonperiodic visible renewal language. Identify actual labelled edges
in that SCC rather than inferring output entropy from packet counts.
P2 HELD: exactly one recurrent SCC, three packets/all nine edges,
and every recurrent edge has k=2. P3 BEFORE certificate extraction:
a finite weighted potential bounds k!=2 returns by at most four;
each macro's column1 trace is fixed by k, including odd times.
Check both explicitly. This targets periodic output, not packet
acyclicity; periodic packet branching need not obstruct a record bound.
P3 HELD more strongly: exceptional rank<=2 (374 zero, eight one,
two two). The complete column1 macro is h(SLLS^k), with k=1..3.
Together with GC706's reviewed periodic-motif cost this gives the
typed finite-left deadline7J+796 ticks: three M_2 blocks, at most
two exceptional macros of duration<=44. This does not cover exits
from the typed A-return chain or prove the full record bound.
"""
import rule30_delayed_A_SS_star_rank as r
from rule30_sl_no_refork import bits,run

q=r.q
TARGET=q.pack(bits('11101000111111110100'))
PINS={6:bits('111001001'),16:bits('1110011011'),26:bits('111010')}
EXCEPTION_ONE={0x11f17,0x1ff17,0x21f17,0x2ff17,0x6ff17,0x81f17,0xaff17,0xeff17}
EXCEPTION_TWO={0x41f17,0xc1f17}


def exception_rank(x):
    return 2 if x in EXCEPTION_TWO else (1 if x in EXCEPTION_ONE else 0)


def successors(state,t):
    x,b=state
    y=(((x<<1)|(t&1))^(x|(x>>1)|(b<<19)))&q.MASK
    a=(x>>19)&1
    return ((y,1-a),) if b else ((y,0),(y,1))


def scalar_successors(state,t):
    old=q.unpack(state[0])+(state[1],)
    return {tuple((q.pack(new[:20]),new[20])) for c in (0,1)
            for new in [tuple(((t&1) if j==0 else old[j-1])^
                             (old[j]|(old[j+1] if j<20 else c))
                             for j in range(21))]}


def allowed(state,t,b):
    x=state[0]
    return ((x>>4)&1)==b and (t<26 or (t-26)%6 or x&r.SSMASK in r.SSPREFIX)


def pin(state,time):
    if time not in PINS:return True
    p=PINS[time]
    return state[0]&((1<<len(p))-1)==q.pack(p)


def paths(k,initial_b,scalar=False):
    states={(TARGET,initial_b)};parents=[];counts=[]
    image=scalar_successors if scalar else successors
    for t,b in enumerate(q.S+q.D+q.H+q.SS*k):
        nxt={}
        for x in sorted(states):
            if not allowed(x,t,b):continue
            for y in image(x,t):
                if pin(y,t+1):nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt);counts.append(len(states))
    endpoints={s for s in states if s[0]==TARGET}
    result={}
    for last in endpoints:
        path=[last]
        for layer in reversed(parents):path.append(layer[path[-1]])
        path.reverse();result[last[1]]=path
    return endpoints,result,counts


def recurrent_language():
    starts,entrances=r.initial();labels=entrances;edge_labels={}
    for k in (1,2,3):
        out=r.flow(labels,q.SS)
        for x,origins in out.items():
            if x&q.AMASK not in r.AP:continue
            while origins:
                low=origins&-origins;i=low.bit_length()-1
                edge_labels.setdefault((starts[i],x),set()).add(k)
                origins^=low
        labels={x:o for x,o in out.items() if x&r.SSMASK in r.SSPREFIX}
    assert not labels # GC1102's <=3 inner SS bound, independently used.
    _,ends,_,_=r.closure(starts,entrances)
    assert set(edge_labels)=={(starts[i],x) for x,o in ends.items()
                             for i in range(len(starts)) if (o>>i)&1}
    adjacency={x:set() for x in starts}
    for x,y in edge_labels:adjacency[x].add(y)
    # Independent simple reachability, including length-zero paths.
    reach={}
    for root in starts:
        seen={root};todo=[root]
        while todo:
            x=todo.pop()
            for y in adjacency[x]-seen:seen.add(y);todo.append(y)
        reach[root]=seen
    remaining=set(starts);components=[]
    while remaining:
        root=min(remaining)
        s={x for x in remaining if x in reach[root] and root in reach[x]}
        remaining-=s
        if len(s)>1 or root in adjacency[root]:components.append(s)
    reports=[]
    for component in components:
        es={e:k for e,k in edge_labels.items() if set(e)<=component}
        ks=set().union(*es.values())
        reports.append(dict(vertices=len(component),edges=len(es),
                            SS_lengths=sorted(ks),
                            packets=[''.join(map(str,q.unpack(x))) for x in sorted(component)],
                            mixed_edges=[(''.join(map(str,q.unpack(x))),
                                          ''.join(map(str,q.unpack(y))),sorted(k))
                                         for (x,y),k in sorted(es.items()) if k!={2}]))
    # A zero-cost recurrent SCC permits a potential for exceptional outputs.
    rank={x:0 for x in starts};waves=0
    while True:
        new={x:max([rank[x]]+[rank[y]+int(any(k!=2 for k in ks))
                            for (a,y),ks in edge_labels.items() if a==x])
             for x in starts}
        if new==rank:break
        rank=new;waves+=1
        assert waves<=len(starts) # no positive-cost cycle in this graph.
    assert all(rank[x]>=rank[y]+int(k!=2)
               for (x,y),ks in edge_labels.items() for k in ks)
    assert all(rank[x]==exception_rank(x) for x in starts)
    assert all(exception_rank(x)>=exception_rank(y)+int(k!=2)
               for (x,y),ks in edge_labels.items() for k in ks)
    return reports,rank,edge_labels


def visible_macro(k):
    starts,_=r.initial();states=set(starts);word=[]
    for t,b in enumerate(q.S+q.D+q.H+q.SS*k):
        states={x for x in states if allowed((x,0),t,b)}
        column={x&1 for x in states}
        assert len(column)==1,(k,t,column)
        word.append(next(iter(column)))
        states={y for x in states for y in q.successors(x,t) if pin((y,0),t+1)}
    assert {x&1 for x in states}=={1}
    out=''.join(map(str,word))
    assert out=='110100'+'1101000100'*2+'110100'*k
    return out


def main():
    relation=set();saved={};counts=[];scalar_cases=0
    for k in (1,2):
        for b in (0,1):
            end,path,n=paths(k,b)
            independent,_,_=paths(k,b,scalar=True)
            assert end==independent;scalar_cases+=1
            if k==1:assert not end
            else:
                counts.append(n)
                relation|={(b,y[1]) for y in end}
                saved.update({(b,z):p for z,p in path.items()})
    for path in saved.values():
        for t,(x,y) in enumerate(zip(path,path[1:])):
            assert y in scalar_successors(x,t)
            assert y[0] in q.scalar_successors(x[0],t)
            if x[1]:assert y[1]==1-((x[0]>>19)&1)
    # Positive actual path, with every joint update independently checked.
    actual=run(r.ACTUAL+(0,)*60,38)
    for t in range(6,38):
        x=(q.pack(actual[t][:20]),actual[t][20])
        y=(q.pack(actual[t+1][:20]),actual[t+1][20])
        assert set(successors(x,t))==scalar_successors(x,t)
        assert y in successors(x,t)
        assert allowed(x,t-6,q.TRACK[t-6]) and pin(y,t-5)
    assert relation=={(0,0),(0,1)}
    repeat=any((b,b) in relation for b in (0,1)) or {(0,1),(1,0)}<=relation
    # A negative control is the old path, including its actual boundary bits.
    old,old_b=r.selfloop_path(TARGET,2)
    assert any((old[t+1],old_b[t+1]) not in successors((old[t],old_b[t]),t)
               for t in range(len(old_b)-1))
    print(dict(named_two_SS_boundary_relation=sorted(relation),
               boundary_graph_recurrent=repeat,scalar_macro_controls=scalar_cases,
               actual_joint_update_controls=32,
               black_boundary_dies_at_tick=next(i+1 for i,n in enumerate(counts[1]) if not n),
               witness_boundary={str(e):''.join(str(s[1]) for s in p) for e,p in saved.items()},
               P1='HELD' if not relation else 'REFUTED',
               actual_right_half_lift='OPEN',all_depth_record_bound='OPEN'),flush=True)
    reports,rank,edges=recurrent_language()
    print(dict(recurrent_components=reports,
               exceptional_macro_rank_counts={h:list(rank.values()).count(h) for h in sorted(set(rank.values()))},
               maximum_non_two_SS_returns=max(rank.values()),typed_finite_left_deadline='7J+796',
               column1_macro_words={k:visible_macro(k) for k in (1,2,3)}),flush=True)


if __name__=='__main__':main()
