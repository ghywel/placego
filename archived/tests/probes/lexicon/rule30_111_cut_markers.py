"""GC1124: translate L631's f54/f56 into exact macro guards.
Missing inference: what do the newly delivered cuts remove from surviving
111 cycles and their arbitrary splices? Seek exact all-k marker constraints,
with finite terminal context; do not rerun CC or language membership.
Record searched: CL301/111 with splice/cycle-coverage/product-acyclic/two-cycle
->2 hits2files, GC1123's pending coverage and unrelated G99 audit.
L631 at ac4ae361 read: exact f54/f56 certificate premises, not rerun.
P1 BEFORE execution: f56 identifies macro121 followed by another macro;
continued121 is forbidden, but finite terminal121 remains accepted.
P2 BEFORE execution: f54 identifies a transition from M3 into M1, with
additional context possibly fixing the following macro. It cannot remove
pure M3; identify the exact cylinder rather than assuming SCC closure.
Counterfactual: killing individual periodic3/12 words automatically deletes
all cycle splices. No such coverage is inferred from a cycle list.
Independent controls planned: gap spelling versus literal physical h evens;
marker gaps versus factor matching on completed macro cones.
Unexpected check: cut begins inside an L gap, so its first complete FIRST-L
window can miss the preceding macro; retain that backward context.
P3 BEFORE the follow-up: f65 may detect23, the other common transition
in FE and the periodic123 word. An exact context requiring more labels
refutes that simple transition interpretation. Retain that failure.
OUTCOME: P1 HELD; P2 sharpened to31 with the finite guard below.
P3 simple23 interpretation REFUTED: f65 requires preceding3 and middle12.
All3906 complete cones pass exact literal and independent h controls.
f65 is redundant beside f54 within this macro grammar, not in all L.
The endpoint counter312 holds; all23-only words survive these three cuts.
No solver, membership, strip widening or relaxed-record computation.
"""
import rule30_mixed_cut_transfer as s
F54='000010000100100100100100001000010010010000100001001001'
F65='00001001001001001000010000100100100001000010010010010000100001001'
F56='01000010000100100100001000010010010010000100001001001000'

if __name__=='__main__':
    for f in (F54,F56,F65):
        ones=[i for i,c in enumerate(f) if c=='1']
        print('cut',len(f),'ones',ones,'gaps',[b-a for a,b in zip(ones,ones[1:])],
              'H',[i for i in range(len(f)-10) if f[i:i+11]=='10000100001'])
    for ks in ((3,1,2),(3,1,3),(3,1,1),(1,2,1),(1,2,1,1)):
        q=s.visible(ks)+'1'
        assert q==s.physical(ks)[::2]+'1'
        print('macro',ks,'completed',len(q),'f54',q.find(F54),'f56',q.find(F56))

# BEFORE exhaustive controls: marker gaps give the exact finite restrictions:
# f54: 31j with j>=2, or311 followed by another macro; offset4.
# f56: 121 followed by another macro; offset2.
# f65: 312 followed by another macro; offset9. Therefore f65 adds no
# pruning beside f54 on completed macro chains, at arbitrary k>=1.
# P3's23 interpretation is refuted: the prefix retains a preceding M3.
# Complete cones below control these symbolic inferences, not actual L.


def g54(w):
    return all(not(w[i:i+2]==(3,1) and
                   (w[i+2]>=2 or i+3<len(w))) for i in range(len(w)-2))


def g56(w):
    return all(w[i:i+3]!=(1,2,1) for i in range(len(w)-3))


def g65(w):
    return all(w[i:i+3]!=(3,1,2) for i in range(len(w)-3))


def controls():
    from itertools import product
    count=0
    for n in range(6):
        for w in product((1,2,3,4,17),repeat=n):
            q=s.visible(w)+'1'
            assert q==s.physical(w)[::2]+'1'
            assert (F54 not in q)==g54(w),w
            assert (F56 not in q)==g56(w),w
            assert (F65 not in q)==g65(w),w
            assert g65(w) or not g54(w),w
            count+=1
    # Dropping the endpoint loses exactly this terminal rejection.
    assert F54 not in s.visible((3,1,2))
    assert (s.visible((3,1,2))+'1').find(F54)==4
    assert g54((3,1,1)) and not g54((3,1,1,17))
    assert g56((1,2,1)) and not g56((1,2,1,17))
    # Every23-only word is accepted by all three guards; not a graph lift.
    assert all(g((2,3)*7) for g in (g54,g56,g65))
    print('complete_cones',count,'exact_guards_PASS','f65_redundant_to_f54',
          'terminal312_endpoint_counter_PASS','no_membership_test')


if __name__=='__main__':
    controls()
