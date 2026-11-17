"""GC1131: the H endpoint before N's white-SS carrier.
Missing inference: GC1130 closes non-AP13 terminals AFTER white SS,
but H endpoints that never enter that carrier may escape/replenish A.
Retain the same original AP13 ancestry through A-S-D111-H-low-D101-H
and classify every endpoint at tick 46, before the white-SS filter.
Record searched: H.endpoint|H.exit|white.SS AND outside.*carrier|
non.SS|terminal|other.exit -> 18 hits in 8 files; D101|H101|N.route|
H.low AND non.SS|A.return|guarded.B|H.endpoint -> 23 hits in 9 files.
GC1098, GC1104, GC1126 and GC1130 sources read; no new width.
P1 BEFORE run: all endpoints outside white SS are low C/J or guarded
B, so no extra A return is omitted before the N white-SS entrance.
If false retain an original-origin path to the surviving endpoint.
Counterfactual: discarding H endpoints before the SS filter proves
admission of the whole branch. Any surviving noncore endpoint refutes it.
Controls: independently scalar replay one full original-origin path;
all 22 old white-SS entrances unchanged; no fifth-track filtering on
any claimed forced continuation, and exact labels retained throughout.
Unexpected check: an apparent noncore A endpoint may be white-eleventh
and need the existing admission guard rather than a new black-A macro.
P2 BEFORE run: every outside-white-SS endpoint not already C/J or B
has white-eleventh A, lies in GC1104's old terminal set, and forces
S-D into C/J. If false keep its selector/prefix, not a fresh A theorem.
20s cap. No solver, CUT, membership, product or record computation.
OUTCOME: P1/P2/P3/P4 REFUTED; P5 original-label/path controls PASS.
H46 has 196 packets: 22 white SS, 130 already C/J or guarded B,
44 white-eleventh A (27 prefix13=1110100011010, 17 ...1011).
No extra black AP13 endpoint exists. The 44 A endpoints are not a
subset of GC1104's admitted 38. Their unfiltered S images number 85;
two prefix15 types fail its sufficient guard, 111001001001100 and
111001001001111. Following unfiltered D gives 225 packets, 45
outside C/J, all high111: 32 prefix13=1110011111110 and 13
1110011111000. Full 62-tick scalar path retained below.
This identifies an omitted white-A interruption, not a width-28
recurrent exit or actual realization. Stop the failed absorption
extension; next retain the recurrent origin for this precise detour.
REFUTED-BY: source 11101000111011100000 at 0, white A
11101000110110110111 at 46, low 11100100100110000110 at 52,
high111 11100111110000000000 at 62, every joint update scalar checked.
"""
# First outcome: P1 REFUTED (44 pending white-A packets, no black AP13);
# P2 old terminal-set inclusion REFUTED. Keep the selected scalar path.
# P3 BEFORE adaptive continuation: after unfiltered S, the pending
# white-A images satisfy GC1104's sufficient low guard: site11 black
# with prefix11=11100100101, or site11 white with the inherited
# prefix15=111001001001001. This would import its existing OR shield
# despite failed terminal-packet inclusion; no fresh white-A shortcut.
# P4 BEFORE control: unfiltered D from every S image lands in C/J.
# Counterfactual must fail: all pending terminals already lie in the
# old 38-packet set. Its recorded failure must remain in this test.
# Unexpected: the loss of old endpoint-set inclusion need not lose
# the smaller sufficient guard after the six-tick S leg.
import signal
from collections import Counter
import rule30_111_low_white_return as n
import rule30_delayed_A_exit_admission as a

r=n.r;q=n.q


def full_witness(start,end,extra=()):
    track=q.S+q.D+q.H+q.D+q.H+extra
    pins={6:n.bits('111001001'),16:n.bits('111001111'),26:n.bits('111001'),36:n.bits('1110011011')}
    states={start};parents=[]
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x>>4)&1!=b:continue
            if t==26 and (x>>9)&3:continue
            for y in q.successors(x,t):
                if t+1 in pins:
                    p=pins[t+1]
                    if y&((1<<len(p))-1)!=q.pack(p):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert end in states
    path=[end]
    for row in reversed(parents):path.append(row[path[-1]])
    path.reverse()
    assert path[0]==start
    assert all(y in q.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    assert ''.join(str(x&1) for x in path[:-1])==('110100'+'1101000100'*4+('1101001101000100' if extra else ''))
    return path


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    starts,_,_,after,ent,_,_,_,_=n.relation()
    assert len(ent)==22
    other={x:o for x,o in after.items() if x not in ent}
    good={x:o for x,o in other.items() if a.core_long(x) or a.guarded_b(x)}
    pending={x:o for x,o in other.items() if x not in good}
    fmt=lambda x:''.join(map(str,q.unpack(x)))
    print('H46_counts',dict(total=len(after),SS=len(ent),other=len(other),already_core_or_B=len(good),pending=len(pending)),
          'pending_prefix13',dict(Counter(fmt(x)[:13] for x in pending)),flush=True)
    oldstarts,oldent=r.initial();oldseen,_,_,_=r.closure(oldstarts,oldent)
    oldout=r.flow(oldseen,q.SS)
    oldwhite={x for x in oldout if x&r.SSMASK not in r.SSPREFIX and x&q.AMASK not in r.AP}
    p2=set(pending)<=oldwhite
    print('P1',not pending,'P2_old_admitted_subset',p2,
          'pending_black_AP13',sum(x&q.AMASK in r.AP for x in pending),flush=True)
    if pending:
        z=min(pending);i=(pending[z]&-pending[z]).bit_length()-1
        full_witness(starts[i],z)
        print('pending_witness',fmt(starts[i]),fmt(z),'scalar_PASS',flush=True)
    if p2 and pending:
        low,sc=a.unfiltered(set(pending),q.S)
        late,dc=a.unfiltered(low,q.D)
        assert all(a.core_long(x) for x in late)
        print('P2_admission_unfiltered_PASS',len(late),'by_tick',62,flush=True)
    # P5 BEFORE counter extraction: each packed unfiltered endpoint has
    # the same original-origin labels as the S-D relation, and a noncore
    # endpoint admits a complete 62-tick independently scalar-checked
    # path through the retained white-A at tick 46. A label/path failure
    # retracts the counter rather than asserting a fresh entrance.
    if pending:
        low,sc=a.unfiltered(set(pending),q.S)
        guard=lambda x: ((x>>10)&1 and x&((1<<11)-1)==q.pack(n.bits('11100100101'))) or (
            not((x>>10)&1) and x&((1<<15)-1)==q.pack(n.bits('111001001001001')))
        late,dc=a.unfiltered(low,q.D)
        labelled=r.flow(pending,q.S+q.D)
        assert set(labelled)==set(late)
        bad={x:o for x,o in labelled.items() if not a.core_long(x)}
        print('retained_noncore_after_SD',len(bad),
              'prefix13',dict(Counter(fmt(x)[:13] for x in bad)),flush=True)
        if bad:
            z=min(bad);i=(bad[z]&-bad[z]).bit_length()-1
            path=full_witness(starts[i],z,q.S+q.D)
            assert path[46] in pending
            print('full_counter_62',fmt(path[0]),fmt(path[46]),fmt(path[52]),fmt(z),
                  'scalar_PASS',flush=True)
        print('P3_low_sufficient_guard',all(guard(x) for x in low),
              'P4_CJ',all(a.core_long(x) for x in late),
              'S_images',len(low),'D_images',len(late),
              'guard_failure_prefix15',sorted({fmt(x)[:15] for x in low if not guard(x)}),flush=True)
    signal.alarm(0)


if __name__=='__main__':main()
