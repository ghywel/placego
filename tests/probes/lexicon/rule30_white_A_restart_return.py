"""GC1133: can the precise white-A interruption return to the typed core?
Missing inference: GC1132 identifies P/Q origins for high111 at62,
but high111 alone is not an A-return. Compose that SAME ancestry
through H and arbitrary positive SS with the existing joint-21
least fixed point. No width sweep or independently fresh endpoint.
Record searched: GC1132|white.A.interruption AND SS|AP13|return
-> 9 hits in 5 files. Existing GC1106 closure and GC1132 flow read.
P1 BEFORE run: no such restarted path returns to the 32-state core
through H followed by any positive SS count. A return is a concrete
unlisted transition, not a proof of an actual right-half lift.
P2 BEFORE run: if an AP13 return exists, it cannot be Q itself, so
there is no self-packet reset replenishment on this new branch.
Counterfactual: the high111 endpoint by itself is a typed A macro;
its low prefix111001 must fail the AP13 guard before H or SS.
Controls: the 65 inherited high endpoints and P/Q origin set remain;
every retained AP13 endpoint has its complete original label; scalar
full-path replay for a retained return, including its SS duration.
Unexpected: an H-low endpoint would be dropped by the SS entrance
filter; count it separately and keep its scope open.
20s cap. No CUT, membership, product, wider strip, record or solver run.
OUTCOME before owner-requested restart pause: P1 REFUTED; P2 HELD.
H72 splits into 152 short and 81 low packets (the identified
unexpected scope check is nonvacuous). SS closure has 1388 packets,
115 AP13 endpoints, 22 inside the old core, 44 original/core pairs.
Q cannot self-return on this detour; P is a productive endpoint.
A scalar-replayed Q-to-111010001110111000000 return uses k=3,
90 ticks, with completed visible word printed by the probe.
CL315/CL316 arrived at the checkpoint: P and Q extend no width-28
recurrent state, independently confirmed by Cloud's width-28 flow.
Thus this joint-21 return computation is retained as relaxation
only; no further cycle, widening or realization work is intended.
Owner asked to stop for a restart. All scripts finished; heartbeat
paused. Resume at untyped entrances and total transient duration,
not this now-excluded recurrent-origin branch.
REFUTED-BY: the original-labelled 90-tick Q-to-core scalar path.
"""
import signal
import rule30_white_A_recurrent_origin as gate
import rule30_111_A_joint_boundary as m

q=m.q;r=gate.r
bits=m.p.bits
P=gate.P
Q=(q.pack(bits('11101000111111110100')),0)


def full_witness(a,z,k):
    track=q.S+q.D+q.H+q.D+q.H+q.S+q.D+q.H+q.SS*k
    pins={6:bits('111001001'),16:bits('111001111'),26:bits('111001'),36:bits('1110011011'),62:bits('111001111')}
    states={a};parents=[]
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x[0]>>4)&1!=b:continue
            if t==26 and (x[0]>>9)&3:continue
            if t==46 and x[0]&((1<<13)-1) not in {q.pack(bits('1110100011010')),q.pack(bits('1110100011011'))}:continue
            if t==72 and not((x[0]>>4)&1):continue
            for y in m.j.successors(x,t):
                if t+1 in pins:
                    p=pins[t+1]
                    if y[0]&((1<<len(p))-1)!=q.pack(p):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert z in states
    path=[z]
    for row in reversed(parents):path.append(row[path[-1]])
    path.reverse();assert path[0]==a
    assert all(y in m.j.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    word=''.join(str(x[0]&1) for x in path[::2])
    assert word=='100'+'10000'*4+'100'+'10000'*2+'100'*k+'1'
    return path,word


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    _,_,_,core,m2,_=m.combined_graph()
    assert len(core)==32 and len(m2)==104
    starts=sorted(core)
    _,high=gate.relation({x:1<<i for i,x in enumerate(starts)})
    assert len(high)==65 and gate.source_set(high,starts)=={P,Q}
    assert all(x[0]&q.AMASK not in r.AP for x in high)
    h=m.flow(high,q.H)
    short={x:o for x,o in h.items() if (x[0]>>4)&1}
    low={x:o for x,o in h.items() if not((x[0]>>4)&1)}
    seen,ends=m.closure(short)
    internal={x:o for x,o in ends.items() if x in core}
    pairs={(starts[i],z) for z,o in internal.items() for i in range(len(starts)) if o>>i&1}
    selfq=(Q,Q) in pairs
    fmt=lambda x:''.join(map(str,q.unpack(x[0])))+str(x[1])
    print('H72_split',dict(short=len(short),low=len(low)),'SS_carrier',len(seen),
          'all_AP13_ends',len(ends),'core_ends',len(internal),'core_pairs',len(pairs),
          'P1_no_core_return',not pairs,'P2_no_Q_self',not selfq,
          'endpoints_that_can_start_detour',sorted(map(fmt,set(internal)&{P,Q})),flush=True)
    if pairs:
        a,z=(Q,Q) if selfq else min(pairs)
        # Finite visited-set BFS finds an SS duration; no cutoff claim.
        _,hi=gate.relation({a:1});cur=m.flow(hi,q.H)
        cur={x:o for x,o in cur.items() if (x[0]>>4)&1}
        visited=set();k=0
        while cur:
            visited.update(cur);k+=1;cur=m.flow(cur,q.SS)
            if z in cur:break
            cur={x:o for x,o in cur.items() if x not in visited}
        assert z in cur
        path,word=full_witness(a,z,k)
        print('return_witness',fmt(a),fmt(z),'SS_count',k,'ticks',len(path)-1,
              'completed_word',word,'scalar_PASS',flush=True)
    signal.alarm(0)


if __name__=='__main__':main()
