"""GC1126: can a111 H-low escape reset the typed A budget via D101?

Missing inference: the cut-closed direct A-return graph omits H-low
exits. Decide whether one such exit can reach a black11 A again
through D101-H and arbitrary white SS, retaining its original A
ancestry. A no-return certificate would close this specific detour;
a retained return must be explained before claiming admission.
Record searched: H.low|high.LL with reentr|admission|third|budget
->20 hits12files; H.low|111.low|low.exit with white.SS|A.return|
A.reentry|D101 ->12 hits8files. GC1087/1104/1105 sources read;
the reviewed two-high-low bound is reused, not reproved.
P1 BEFORE run: no original A-S-D111-H-low-D101-H history reaches
a black11 AP13 endpoint after any positive number of white SS.
Counterfactual: an omitted low detour replenishes the A budget;
retain a complete original-origin/end pair rather than just fresh
low packets. Use the existing20-cell relaxation, no widening.
Controls: independently scalar-replay a selected full origin flow;
GC1105's first H-low set remains107 packets; GC1100's actual direct
white-SS A return must remain a positive control.
Unexpected check: first H-low branches might have no D101-H-whiteSS
entrance, making no-reset vacuous. Count the entrance separately.
Finite visited-set closure certifies all SS counts, not a time bound.
No CUT, membership, solver, relaxed-record or Local111-word run.
P1 REFUTED: 22 nonvacuous white SS entrances reach 51 black A
endpoints with 1,530 original-origin/end pairs; first SS returns no A.
P2 BEFORE structural certificate: these 62 inner white SS packets
are a subset of GC1102's 137 packets and obey its existing rank <= 2.
If false, do not import that duration bound; keep exact all-count
reachability and the counterexample. P3 BEFORE witness/control:
a represented low detour returns A with k = 2, spelling SLLLLSS
(58 physical ticks), and the complete independent scalar origin
flow agrees. This is a relaxation witness, not an actual lift.
P2/P3 HELD: all 62 packets reuse the old rank; their maximum rank
is 1, so at most two SS blocks can finish this detour. All black A
returns therefore have exactly k = 2, since the first has none.
P4 BEFORE final equality check: the k = 2 labelled endpoint relation
equals the complete fixed-point relation, including all 1,530 pairs.
OUTCOME: P1 REFUTED; P2/P3/P4 HELD. The omitted return is a
58-tick macro N=SLLLLSS, visible completed word below. This gives
a specific missing transition/cut target, not global admission or
actual realizability. No new vertex rank is fitted; GC1102's rank
is checked on every inner edge of this different entrance set.
REFUTED-BY: retained original A packet 11101000111011100000 returns
to 11101000111001100000 via N in the sound20-cell relation.
"""
import rule30_black_A_111_diversion as p
import rule30_delayed_A_SS_star_rank as r
from rule30_sl_no_refork import bits

q=r.q


def witness(a,z,k):
    track=q.S+q.D+q.H+q.D+q.H+q.SS*k
    pins={6:bits('111001001'),16:bits('111001111'),
          26:bits('111001'),36:bits('1110011011')}
    states={a};parents=[]
    for t,bit in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x>>4)&1!=bit:continue
            if t==26 and (x>>9)&3!=0:continue
            if t>=46 and (t-46)%6==0 and x&r.SSMASK not in r.SSPREFIX:continue
            for y in q.successors(x,t):
                if t+1 in pins:
                    pre=pins[t+1]
                    if y&((1<<len(pre))-1)!=q.pack(pre):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert z in states
    path=[z]
    for layer in reversed(parents):path.append(layer[path[-1]])
    path.reverse()
    assert path[0]==a
    assert all(y in q.scalar_successors(x,t)
               for t,(x,y) in enumerate(zip(path,path[1:])))
    expected='110100'+'1101000100'*4+'110100'*k
    assert ''.join(str(x&1) for x in path[:-1])==expected
    return path,expected


def scalar_endpoints(a):
    states={a}
    pins={6:bits('111001001'),16:bits('111001111'),
          26:bits('111001'),36:bits('1110011011')}
    track=q.S+q.D+q.H+q.D+q.H
    for t,bit in enumerate(track):
        if t==26:states={x for x in states if (x>>9)&3==0}
        states={y for x in states if (x>>4)&1==bit
                for y in q.scalar_successors(x,t)}
        if t+1 in pins:
            pre=pins[t+1];mask=(1<<len(pre))-1;value=q.pack(pre)
            states={y for y in states if y&mask==value}
    seen=set();out=set();delta={x for x in states if x&r.SSMASK in r.SSPREFIX}
    while delta:
        seen|=delta;states=delta
        for t,bit in enumerate(q.SS):
            states={y for x in states if (x>>4)&1==bit
                    for y in q.scalar_successors(x,t)}
        out|={x for x in states if x&q.AMASK in r.AP}
        delta={x for x in states if x&r.SSMASK in r.SSPREFIX}-seen
    return out


def relation():
    starts,_=r.initial()
    high,_=p.diversion(starts)
    low={x:o for x,o in high.items() if x&63==p.LOW}
    assert len(low)==107
    pending={x:o for x,o in low.items() if (x>>9)&3==0}
    after=r.flow(pending,q.D+q.H,{10:bits('1110011011')})
    entrances={x:o for x,o in after.items() if x&r.SSMASK in r.SSPREFIX}
    seen,ends,first,rounds=r.closure(starts,entrances)
    return starts,low,pending,after,entrances,seen,ends,first,rounds


def main():
    starts,low,pending,after,ent,seen,ends,first,rounds=relation()
    pairs={(starts[i],z) for z,o in ends.items()
           for i in range(len(starts)) if (o>>i)&1}
    print(dict(first_H_low=len(low),D_candidates=len(pending),
               next_D101_H=len(after),white_SS_entrances=len(ent),
               SS_seen=len(seen),black_A_endpoints=len(ends),
               black_A_pairs=len(pairs),first_SS_A=len(first or {}),
               predicted_no_A=not pairs),flush=True)
    oldstarts,oldent=r.initial();oldseen,oldends,_,_=r.closure(oldstarts,oldent)
    extra=set(seen)-set(oldseen)
    inner={x:set(r.flow({x:1},q.SS)) & set(seen) for x in seen}
    def rank(x):return 2 if x in r.SS_RANK_TWO else 1 if x in r.SS_RANK_ONE else 0
    bad=[(x,y) for x in inner for y in inner[x] if rank(x)<=rank(y)]
    assert not extra and not bad and max(map(rank,seen))==1
    assert not first
    print(dict(old_rank_extra=len(extra),old_rank_bad_edges=len(bad),
               rank_counts={j:sum(rank(x)==j for x in seen) for j in range(3)}),flush=True)
    k2=r.flow(r.flow(ent,q.SS),q.SS)
    k2={z:o for z,o in k2.items() if z&q.AMASK in r.AP}
    assert k2==ends
    assert (len(ent),len(seen),len(ends),len(pairs))==(22,62,51,1530)
    z=min(k2);i=(k2[z]&-k2[z]).bit_length()-1;a=starts[i]
    path,word=witness(a,z,2)
    assert scalar_endpoints(a)=={z for z,o in ends.items() if (o>>i)&1}
    # Positive independent actual history for the previously established
    # direct reset; it is not a realization assertion about the low detour.
    from rule30_sl_no_refork import run
    actual=run(r.ACTUAL+(0,)*40,38)
    assert q.pack(actual[38][:20]) in oldends
    print(dict(witness_origin=''.join(map(str,q.unpack(a))),
               witness_endpoint=''.join(map(str,q.unpack(z))),
               witness_physical_ticks=len(path)-1,
               physical_word=word,visible_completed=word[::2]+'1',
               scalar_complete_origin='PASS',actual_direct_control='PASS'),flush=True)


if __name__=='__main__':main()
