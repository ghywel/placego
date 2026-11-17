"""GC1106: the identified omitted boundary equation of GC1105's M3 loop.

Missing inference: does the new111/black-SS M3 packet recurrence
survive when column21 has its own Rule30 update? The20-cell witness
refreshes that bit independently. Retain this specific equation
on the named self-return, without a wider-strip sweep or a solver.
Record searched: GC1105|11101000111011100000|M3 with boundary|guard|
past|self|recur ->42 hits18files (M3 has unrelated collisions);
GC1103 and GC1105 source and current ledgers read. Their named
loops and111 pin differ; no prior joint-boundary M3 result found.
P1 BEFORE run: every44-tick M3 self-return of the named20-packet
dies when b21'=a20 XOR(b21 OR c22) is retained, c22 still fresh.
Counterfactual: both boundary colours may permit a coherent21-cell
return; no actual infinite right-half lift follows from that alone.
Controls: independent scalar21-cell whole-path set flows for each
initial boundary colour; GC1091 actual111 diversion stays represented;
forgetting b projects inside GC1105's free-input transitions.
Unexpected: a nonempty one-macro relation can be transient between
boundary colours. Check its complete2x2 return relation before
claiming the packet loop remains recurrent.
Stop this representation on a surviving recurrent relation; do not
extend a strip sweep or infer realizability from a failed chosen path.
P1 REFUTED: all four boundary-colour returns survive; the M3 loop
remains recurrent with its missing temporal equation restored.
P2 BEFORE the structural switch: the very same21-cell packet with
white boundary admits both three and five SS blocks. Two distinct
equal-duration concatenations (M3M5 versus M5M3,100 ticks) would
then yield arbitrary binary choices in this model, defeating the
eventual-periodic-output explanation as well as the old potential.
Keep geometry and origin fixed; this is an explicit second-cycle
certificate, not a width or membership sweep. No actual coherent
right-half realization or global record conclusion is inferred.
P2 REFUTED: five SS returns vanish for this named packet although
its three-SS boundary relation is complete. This new distinction
motivates P3 BEFORE structural graph composition: in the same joint
representation,111/M3 and101/M2 recurrent components separate.
Keep both origin labels and the same finite SS least fixed point;
do not count discovery rounds as an SS duration bound. A common
SCC containing the named M3 self-loop and a101-M2 cycle refutes
the pure-periodic-component explanation for this representation.
P3 REFUTED: both are in one32-state recurrent component;104 M2
edges remain inside it. P4 BEFORE explicit output certificate:
shortest macro connectors between the M3 and old M2 self-packets
yield two distinct equal-duration closed walks by placing the M3
loop before or after the connected M2 excursion. Scalar-replay
every joint update, and test trace inequality explicitly; SCC
membership or packet multiplicity alone is not output entropy.
P4 HELD: four connector macros, labels(111,1),(101,2),(101,2),
(111,3), join the M3 and M2 white-boundary self-packets both ways.
The connected M2 excursion is190 ticks. Moving the44-tick M3 loop
before or after it gives two234-tick joint closed walks, with first
column1 disagreement at44. Every concatenated update scalar checked.
Their endpoints and wall phases agree, so arbitrary choices give
2^n model traces at234n ticks (entropy at least1/234 bits per tick).
This refutes the one-boundary-cell periodic-output explanation;
actual infinite right-half lifting and the prize bound stay OPEN.
No wider strip, Local solver, membership or record experiment.
"""
import rule30_delayed_A_boundary_memory as j
import rule30_black_A_111_diversion as p
from rule30_black_SS_high_restart import SOURCE

q=j.q
TARGET=q.pack(p.bits('11101000111011100000'))
TRACK=q.S+q.D+q.H+q.SS*3
PINS={6:p.bits('111001001'),16:p.bits('111001111')}


def flow(labels,track,pins=None):
    for t,b in enumerate(track):
        nxt={}
        for state,o in labels.items():
            if (state[0]>>4)&1!=b:continue
            for y in j.successors(state,t):nxt[y]=nxt.get(y,0)|o
        if pins and t+1 in pins:
            pre=pins[t+1];mask=(1<<len(pre))-1;v=q.pack(pre)
            nxt={y:o for y,o in nxt.items() if y[0]&mask==v}
        labels=nxt
    return labels


def closure(entrances):
    seen={};delta=entrances;ends={}
    while delta:
        for x,o in delta.items():seen[x]=seen.get(x,0)|o
        out=flow(delta,q.SS)
        for x,o in out.items():
            assert (x[0]>>4)&1
            if x[0]&q.AMASK in p.r.AP:ends[x]=ends.get(x,0)|o
        delta={x:o&~seen.get(x,0) for x,o in out.items()}
        delta={x:o for x,o in delta.items() if o}
    complete=flow(seen,q.SS)
    assert all(not(o&~seen.get(x,0)) for x,o in complete.items())
    assert {x:o for x,o in complete.items() if x[0]&q.AMASK in p.r.AP}==ends
    return seen,ends


def combined_graph():
    starts20,_=p.r.initial();starts=[(x,b) for x in starts20 for b in (0,1)]
    graph={x:set() for x in starts};typed={};seen_counts={};m2_edges=set()
    for typ,high in ((101,'1110011011'),(111,'111001111')):
        entrances=flow({x:1<<i for i,x in enumerate(starts)},q.S+q.D+q.H,
                       {6:p.bits('111001001'),16:p.bits(high)})
        entrances={x:o for x,o in entrances.items() if (x[0]>>4)&1}
        seen,ends=closure(entrances);seen_counts[typ]=len(seen)
        for z,o in ends.items():
            while o:
                b=o&-o;a=starts[b.bit_length()-1];o^=b
                graph[a].add(z);typed.setdefault((a,z),set()).add(typ)
        if typ==101:
            out=flow(flow(entrances,q.SS),q.SS)
            for z,o in out.items():
                if z[0]&q.AMASK not in p.r.AP:continue
                while o:
                    b=o&-o;a=starts[b.bit_length()-1];o^=b;m2_edges.add((a,z))
    components=p.recurrent_components(graph)
    named=next(c for c in components if (TARGET,0) in c)
    named_m2=[(a,z) for a,z in m2_edges if a in named and z in named]
    return graph,typed,components,named,named_m2,seen_counts


def connector(graph,start,end):
    from collections import deque
    todo=deque([start]);parent={start:None}
    while todo:
        x=todo.popleft()
        if x==end:break
        for y in sorted(graph[x]):
            if y not in parent:parent[y]=x;todo.append(y)
    assert end in parent
    path=[end]
    while path[-1]!=start:path.append(parent[path[-1]])
    return path[::-1]


def edge_path(start,end,typ):
    high=p.bits('1110011011' if typ==101 else '111001111')
    pin={6:p.bits('111001001'),16:high}
    states=set(flow({start:1},q.S+q.D+q.H,pin))
    states={x for x in states if (x[0]>>4)&1};seen=set();k=0
    while states:
        seen|=states;k+=1
        states=set(flow({x:1 for x in states},q.SS))
        if end in states:break
        states-=seen
    assert end in states
    states={start};parents=[]
    for t,b in enumerate(q.S+q.D+q.H+q.SS*k):
        nxt={}
        for x in sorted(states):
            if (x[0]>>4)&1!=b:continue
            for y in j.successors(x,t):
                if t+1 in pin:
                    pre=pin[t+1]
                    if y[0]&((1<<len(pre))-1)!=q.pack(pre):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert end in states
    path=[end]
    for row in reversed(parents):path.append(row[path[-1]])
    path.reverse();assert path[0]==start
    assert all(y in j.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    word=''.join(str(x&1) for x,_ in path[:-1])
    assert word=='110100'+'1101000100'*2+'110100'*k
    return path,typ,k


def concatenate(paths):
    out=paths[0].copy()
    for path in paths[1:]:
        assert out[-1]==path[0]
        out.extend(path[1:])
    return out


def paths(initial_b,scalar=False,k=3):
    states={(TARGET,initial_b)};parents=[];counts=[]
    image=j.scalar_successors if scalar else j.successors
    for t,b in enumerate(q.S+q.D+q.H+q.SS*k):
        nxt={}
        for state in sorted(states):
            if (state[0]>>4)&1!=b:continue
            for y in image(state,t):
                if t+1 in PINS:
                    pre=PINS[t+1]
                    if y[0]&((1<<len(pre))-1)!=q.pack(pre):continue
                nxt.setdefault(y,state)
        parents.append(nxt);states=set(nxt);counts.append(len(states))
    end={s for s in states if s[0]==TARGET};out={}
    for z in end:
        path=[z]
        for row in reversed(parents):path.append(row[path[-1]])
        path.reverse();out[z[1]]=path
    return end,out,counts


def main():
    relation=[];counts={};samples={}
    for b in (0,1):
        end,paths_b,n=paths(b)
        assert end==paths(b,True)[0]
        counts[b]=n
        for _,c in sorted(end):
            relation.append((b,c));samples[(b,c)]=paths_b[c]
            for t,(state,nxt) in enumerate(zip(paths_b[c],paths_b[c][1:])):
                assert nxt in j.scalar_successors(state,t)
                assert nxt[0] in q.successors(state[0],t)
    actual=p.run(SOURCE+(0,)*60,42)
    for t in range(6,32):
        state=q.pack(actual[t][:20]),actual[t][20]
        nxt=q.pack(actual[t+1][:20]),actual[t+1][20]
        assert nxt in j.successors(state,t)
    recurrent=any(a==b for a,b in relation) or ((0,1) in relation and (1,0) in relation)
    end5,path5,counts5=paths(0,k=5)
    assert end5==paths(0,True,k=5)[0]
    assert not end5 # The predicted M5 loop is a retained negative control.
    graph,typed,components,named,named_m2,seen_counts=combined_graph()
    a=TARGET,0;b=j.TARGET,0
    assert b in named
    m2_end,m2_path,_=j.paths(2,0)
    assert b in m2_end
    go=connector(graph,a,b);back=connector(graph,b,a)
    arcs=[edge_path(x,y,min(typed[(x,y)]))
          for route in (go,back) for x,y in zip(route,route[1:])]
    ng=len(go)-1
    excursion=concatenate([t[0] for t in arcs[:ng]]+[m2_path[0]]+[t[0] for t in arcs[ng:]])
    first=concatenate([samples[(0,0)],excursion])
    second=concatenate([excursion,samples[(0,0)]])
    assert first[0]==first[-1]==second[0]==second[-1]==a
    assert len(first)==len(second)
    choice1=''.join(str(x&1) for x,_ in first[:-1])
    choice2=''.join(str(x&1) for x,_ in second[:-1])
    assert choice1!=choice2
    assert len(first)==235
    assert next(t for t,(x,y) in enumerate(zip(choice1,choice2)) if x!=y)==44
    assert [(typ,k) for _,typ,k in arcs]==[(111,1),(101,2),(101,2),(111,3)]
    assert sorted(map(len,components))==[32] and len(named_m2)==104
    assert seen_counts=={101:635,111:1669}
    for path in (first,second):
        assert all(y in j.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    print(dict(boundary_relation=relation,recurrent=recurrent,
               terminal_layer_counts={b:n[-1] for b,n in counts.items()},
               scalar_macro_controls=3,
               actual_GC1091_updates=26,
               sample_boundary_words={str(k):''.join(str(b) for _,b in v)
                                      for k,v in samples.items()},
               five_SS_relation=[(0,b) for _,b in sorted(end5)],
               joint_SS_packet_counts=seen_counts,
               combined_SCC_sizes=sorted(map(len,components)),
               named_component_size=len(named),named_component_M2_edges=len(named_m2),
               first_named_M2=named_m2[0] if named_m2 else None,
               connector_macro_labels=[(typ,k) for _,typ,k in arcs],
               connector_go=[(''.join(map(str,q.unpack(x))),b) for x,b in go],
               connector_back=[(''.join(map(str,q.unpack(x))),b) for x,b in back],
               distinct_closed_walk_ticks=len(first)-1,
               first_output_difference=next(t for t,(x,y) in enumerate(zip(choice1,choice2)) if x!=y),
               model_entropy_lower_bound='1/234 bits per tick',
               actual_infinite_right_lift='OPEN',all_depth_record_bound='OPEN'))


if __name__=='__main__':main()
