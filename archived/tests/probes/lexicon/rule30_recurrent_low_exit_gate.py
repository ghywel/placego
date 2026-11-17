"""GC1128: which omitted 111 exits can start inside the old recurrent core?

Missing inference (CL306): N sources disappear from the width-28
macro graph, but second-111 and X exits might leave its recurrent
components and return by an unlabelled route. Use the EXISTING joint
21 core as a necessary projection, keeping all original labels.
Record searched: H.low|X.exit|second.111 AND recurrent.*exit|exit.*recurrent
-> one status-board hit; GC1105/1106/1126 and CL306 sources read.
P1 BEFORE run: no A-S-D111-H-low path starts in the existing 32-state
joint core. If false, retain every low endpoint, not only N sources.
P2 BEFORE run: any retained low has pair00 selecting D, with no X
selector, and D cannot reach another 111. This would isolate N or
low-core admission as the remaining exit. Counterfactual: an omitted
X or second-111 branch leaves a recurrent origin; retain the full
origin/exit label and scalar flow instead of claiming admission.
Controls: old component size 32 and M2 edges 104; independent scalar
flows from every core origin through the same pins and then D.
Unexpected check: a first H-low may already satisfy C/J, making
its continuing high branch vacuous; classify the complete low guard.
No width refinement, product, membership, CUT, or realization run.
P1/P2 REFUTED: 123 low packets and 129 original-origin pairs;
93 pair00 and 30 pair11, none in C/J. D has 21 second-111
endpoints (225 total, 79 outside C/J). All 32 scalar origins agree.
The projection still permits both omitted exits. No width-28 or
actual return assertion follows from these 21-cell paths.
P3 BEFORE witness extraction: both selectors and a second-111
endpoint have complete scalar-replayed original 21-cell paths;
a label mismatch would retract the corresponding counterexample.
P4 BEFORE source-selection check: all X-selected lows and all
second-111 endpoints originate in the same SINGLE core state,
111010001110111000011 (sites 1..21). If false, retain the complete
source set; do not shrink the width-28 follow-up to that packet.
P3/P4 HELD. Both omitted exits have exactly that one productive
core origin. The two selectors and second-111 paths scalar-replay.
Any width-28 macro cycle projects to this known joint-21 cycle
component, so only extensions of this prefix can take these exits
from the width-28 recurrent components. Presence there is not tested.
"""
import signal
from collections import Counter
import rule30_111_A_joint_boundary as m
from rule30_delayed_A_exit_admission import core_long

q=m.q
bits=m.p.bits


def scalar(labels,track,pins=None):
    for t,b in enumerate(track):
        nxt={}
        for x,o in labels.items():
            if (x[0]>>4)&1!=b:continue
            for y in m.j.scalar_successors(x,t):nxt[y]=nxt.get(y,0)|o
        if pins and t+1 in pins:
            p=pins[t+1];mask=(1<<len(p))-1;v=q.pack(p)
            nxt={x:o for x,o in nxt.items() if x[0]&mask==v}
        labels=nxt
    return labels


def witness(a,z,track,pins):
    states={a};parents=[]
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x[0]>>4)&1!=b:continue
            for y in m.j.successors(x,t):
                if t+1 in pins:
                    pre=pins[t+1];mask=(1<<len(pre))-1
                    if y[0]&mask!=q.pack(pre):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert z in states
    path=[z]
    for layer in reversed(parents):path.append(layer[path[-1]])
    path.reverse();assert path[0]==a
    assert all(y in m.j.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    return path


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    _,_,components,core,m2,_=m.combined_graph()
    assert sorted(map(len,components))==[32]
    assert len(core)==32 and len(m2)==104
    starts=sorted(core);labels={x:1<<i for i,x in enumerate(starts)}
    pin={6:bits('111001001'),16:bits('111001111')}
    high=m.flow(labels,q.S+q.D+q.H,pin)
    assert high==scalar(labels,q.S+q.D+q.H,pin)
    low={x:o for x,o in high.items() if x[0]&63==m.p.LOW}
    selectors=Counter((x[0]>>9)&3 for x in low)
    assert len(low)==123 and selectors=={0:93,3:30}
    assert not any(core_long(x[0]) for x in low)
    pending={x:o for x,o in low.items() if (x[0]>>9)&3==0}
    after=m.flow(pending,q.D)
    assert after==scalar(pending,q.D)
    prefix=lambda x,n:''.join(map(str,q.unpack(x[0])[:n]))
    pairs=[(starts[i],z) for z,o in low.items()
           for i in range(len(starts)) if o>>i&1]
    assert len(pairs)==129
    print(dict(core_origins=len(starts),first_H_low=len(low),
               labelled_low_pairs=len(pairs),selectors=dict(selectors),
               first_low_in_core=sum(core_long(x[0]) for x in low),
               D_endpoints=len(after),D_triples=dict(Counter(prefix(x,9)[6:] for x in after)),
               D_outside_CJ=sum(not core_long(x[0]) for x in after),
               P1_no_low=not low,
               P2_only_D_no_111=all((x[0]>>9)&3==0 for x in low) and
                   not any(prefix(x,9)[6:]=='111' for x in after),
               independent_scalar_all_origins='PASS'),flush=True)
    if low:
        for pair in sorted(selectors):
            z=min(x for x in low if (x[0]>>9)&3==pair)
            i=(low[z]&-low[z]).bit_length()-1;a=starts[i]
            witness(a,z,q.S+q.D+q.H,pin)
            print('low_selector_witness',pair,(prefix(a,20),a[1]),
                  (prefix(z,20),z[1]),flush=True)
    second={x:o for x,o in after.items() if prefix(x,9)[6:]=='111'}
    assert len(second)==21 and len(after)==225
    assert sum(not core_long(x[0]) for x in after)==79
    z=min(second);i=(second[z]&-second[z]).bit_length()-1;a=starts[i]
    # The endpoint relation kept the pair00 condition at tick 26.
    # Reconstruct in two legs via the matching original label.
    middle=next(x for x,o in pending.items() if o>>i&1 and
                z in m.flow({x:1},q.D))
    first=witness(a,middle,q.S+q.D+q.H,pin)
    last=witness(middle,z,q.D,{})
    assert first[-1]==last[0]
    source_set=lambda relation:{starts[i] for o in relation.values()
                               for i in range(len(starts)) if o>>i&1}
    xs=source_set({x:o for x,o in low.items() if (x[0]>>9)&3==3})
    hs=source_set(second)
    named=(q.pack(bits('11101000111011100001')),1)
    assert xs==hs=={named}
    print('omitted_exit_origin_sets',
          {k:sorted((prefix(x,20),x[1]) for x in v)
           for k,v in [('X',xs),('second111',hs)]},
          'P4_single_common_origin',xs==hs=={named},flush=True)
    print('second_111_witness',(prefix(a,20),a[1]),
          (prefix(middle,20),middle[1]),(prefix(z,20),z[1]),
          'ticks',36,'scalar_paths_PASS',flush=True)
    signal.alarm(0)


if __name__=='__main__':main()
