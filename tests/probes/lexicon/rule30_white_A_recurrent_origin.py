"""GC1132: recurrent origins of GC1131's S-separated white-A detour.
Missing inference: the 20-cell white-A counter may start outside every
width-28 recurrent state, as GC1128's direct second111/X exits did.
Keep original labels of the EXISTING joint-21 cyclic component through
A-S-D111-H-low(pair00)-D101-H-whiteA-S-D111. A sound origin exclusion
would discharge this precise detour from that recurrent regime.
Record searched: white.A|GC1131|S.separated AND recurrent|origin.gate|
interruption -> 9 hits in 5 files; GC1128 and GC1131 sources read.
P1 BEFORE run: none of the known 32 recurrent origins permits the
white-eleventh A interruption at H46 and high111 at D62.
Counterfactual: the same 20-cell prefix as a recurrent packet implies
the whole origin is recurrent after the evolving 21st bit is retained.
Test the complete original-label relation, not a selected packet.
P2 BEFORE run: if an origin survives, it must be the same prefix P
as GC1128, already excluded from width-28 recurrent components.
A different productive prefix must remain a separate entrance target.
Controls: old core=32 and internal M2 edges=104; independent scalar
flows from each core origin through all 62 ticks with the same pins;
scalar full-path replay of one survivor if nonempty. Projection into
width20 must lie in GC1131's exactly retained white-A packet set.
Unexpected: a core-origin path may reach white A at46 but all such
origins die on the ensuing S-D, so separate the two label sets.
20s cap. No width refinement, product, CUT, membership or record run.
OUTCOME: P1/P2 REFUTED, but the complete productive origin set has
only TWO states: P=111010001110111000011 (GC1128) and
Q=111010001111111101000. 64 white-A endpoints at46 and 65
high111 endpoints at62 carry 130 productive origin/end pairs. Both
origins reach white A and high111; no dying-only origin. Every one
of the 32 scalar flows agrees, and a complete Q path scalar-replays.
CL310's published 11 mixed-component prefixes contain neither P
nor Q: this detour cannot leave its 97-state component. P is also
absent from the 10-state component; Q's membership there was not
reported. Request that retained-prefix lookup, no graph rerun.
The complete visible word is 100(10000)^4 100 10000 1 (32 bits);
Local can compare against its already exact both-phase language.
REFUTED-BY: the complete Q path below, not an actual right lift.
"""
import signal
from collections import Counter
import rule30_111_A_joint_boundary as m
import rule30_recurrent_low_exit_gate as g
import rule30_N_H_exit_gate as old

q=m.q;r=old.r
bits=m.p.bits
P=(q.pack(bits('11101000111011100001')),1)


def relation(labels,engine=m.flow):
    high=engine(labels,q.S+q.D+q.H,{6:bits('111001001'),16:bits('111001111')})
    low={x:o for x,o in high.items() if x[0]&63==m.p.LOW and (x[0]>>9)&3==0}
    high2=engine(low,q.D+q.H,{10:bits('1110011011')})
    white={x:o for x,o in high2.items() if x[0]&((1<<13)-1) in {
        q.pack(bits('1110100011010')),q.pack(bits('1110100011011'))}}
    after=engine(white,q.S+q.D)
    end={x:o for x,o in after.items() if x[0]&((1<<9)-1)==q.pack(bits('111001111'))}
    return white,end


def source_set(relation,starts):
    return {starts[i] for o in relation.values() for i in range(len(starts)) if o>>i&1}


def witness(a,z):
    track=q.S+q.D+q.H+q.D+q.H+q.S+q.D
    pins={6:bits('111001001'),16:bits('111001111'),26:bits('111001'),36:bits('1110011011')}
    states={a};parents=[]
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x[0]>>4)&1!=b:continue
            if t==26 and (x[0]>>9)&3:continue
            if t==46 and x[0]&((1<<13)-1) not in {
                q.pack(bits('1110100011010')),q.pack(bits('1110100011011'))}:continue
            for y in m.j.successors(x,t):
                if t+1 in pins:
                    p=pins[t+1]
                    if y[0]&((1<<len(p))-1)!=q.pack(p):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert z in states
    path=[z]
    for row in reversed(parents):path.append(row[path[-1]])
    path.reverse()
    assert path[0]==a
    assert all(y in m.j.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    return path


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    _,_,components,core,m2,_=m.combined_graph()
    assert len(core)==32 and len(m2)==104 and sorted(map(len,components))==[32]
    starts=sorted(core);labels={x:1<<i for i,x in enumerate(starts)}
    white,end=relation(labels)
    wsrc=source_set(white,starts);src=source_set(end,starts)
    # Verify projection against the old full-origin white-A certificate.
    _,_,_,after,ent,_,_,_,_=old.n.relation()
    oldwhite={x for x in after if x not in ent and not old.a.core_long(x) and not old.a.guarded_b(x)}
    assert {x[0] for x in white}<=oldwhite
    for a in starts:
        sw,se=relation({a:1},g.scalar)
        assert sw=={x:1 for x,o in white.items() if o>>starts.index(a)&1}
        assert se=={x:1 for x,o in end.items() if o>>starts.index(a)&1}
    fmt=lambda x:''.join(map(str,q.unpack(x[0])))+str(x[1])
    print('counts',dict(white46=len(white),white46_origins=len(wsrc),high111_62=len(end),productive_origins=len(src),
                       origin_endpoint_pairs=sum(o.bit_count() for o in end.values())),
          'white46_origin_prefixes',sorted(map(fmt,wsrc)),
          'productive_origin_prefixes',sorted(map(fmt,src)),
          'P1_no_core_origin',not src,'P2_only_old_P',bool(src) and src=={P},
          'all32_scalar_controls','PASS',flush=True)
    if end:
        z=min(end);i=(end[z]&-end[z]).bit_length()-1
        path=witness(starts[i],z)
        word=''.join(str(x[0]&1) for x in path[::2])
        expected='100'+'10000'*4+'100'+'10000'+'1'
        assert word==expected and len(word)==32
        print('witness',[(t,fmt(path[t])) for t in (0,26,46,52,62)],'scalar_PASS',
              'visible_completed',word,'length',len(word),flush=True)
        assert src=={P,(q.pack(bits('11101000111111110100')),0)}

    signal.alarm(0)


if __name__=='__main__':main()
