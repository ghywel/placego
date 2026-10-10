"""GC1070: a long alternating carrier has a forced first released input.
Missing inference: does extending GC1068's alternating collar keep
its first unmasked actual input selectable at arbitrary collar length?
Record searched: alternating|collar + difference|discrepancy|visibility|
deadline ->29 hits in8 files; collar|alternating + black.lock|nine.black|
constant.black|9.*lock|long.*collar ->23 hits in10 files. Reuse PROOFS
entry38's nine-update black-wall lock; do not reprove or census it.
P1 BEFORE controls: retained original alternating suffix of even
length K>=10 gives repaired child finalK=(01)^(K/2), hence endpoint
R black at future0..K-1. The reviewed lock forces exterior S,T=01
at future9 and throughK. The first released sample S_K is therefore
0 for EVERY actual tail, not independently selectable.
P2: target old child R0, inputs0100, arbitrary samples4..K-1, then
sampleK=0 admits the all-zero GC1068 origin and complete equality
from future4 throughK+1. First W+K+3 original observations lift
for arbitrary later input samples. K=W-4 closes the full halfwidth
horizon for this cylinder at every even W>=14 (not all cylinders).
Counterfactual: larger alternating collars improve independent-input
steering. P1 refutes this while P2 retains a useful visible cylinder.
Unexpected check: when requested sampleK=1 and R_K=0, full-row
retention fails universally, but the visible halfwidth trace may
still agree. Measure this distinction without inferring absence.
Controls: two nonadjacent K values10,18, both phases, selected
arbitrary earlier/farther bits and two intermediate input blocks.
Literal/packed actual cones, decimal-table strips. No solver,
word membership, NFA or strip-language census.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def main():
    lifts = blocked = invisible = visible = 0
    for K in (10, 18):
        W = K+4
        T = 2*W-2
        for p, q, phase, h, k, mode in product((0, 1), repeat=6):
            prefix = (p, q) + bits('01')*(K//2)
            ref = run(prefix + bits('001110') + (0,)*4, 2, phase)
            child = ref[2][:W]
            assert child[-K:] == bits('01')*(K//2-1) + (0, 0)
            far = (h,k,1-h,1-k)*24
            actual = run(prefix + bits('0000000') + far, T, phase)
            assert actual[2][:W-1] == child[:-1]
            assert actual[2][W-1] == 1
            assert all(actual[t+2][W-1] == 1 for t in range(K))
            assert all(actual[t+2][W:W+2] == (0,1) for t in range(9,K+1))
            assert actual[K+2][W-1] == q
            middle = tuple((t+mode)&1 for t in range(K-4))
            following = tuple((t+h+k)&1 for t in range(T-2-K-1))
            for e in (0,1):
                ext = bits('0100') + middle + (e,) + following
                wanted = strip(child, ext, phase)
                assert all(actual[t+2][:W] == wanted[t] for t in range(4,K+1))
                if e == 0:
                    assert actual[K+3][:W] == wanted[K+1]
                    assert trace(actual) == trace(ref[:2])+trace(wanted)
                    lifts += 1
                elif q == 0:
                    assert actual[K+3][:W-1] == wanted[K+1][:W-1]
                    assert actual[K+3][W-1] != wanted[K+1][-1]
                    blocked += 1
                    same = trace(actual) == trace(ref[:2])+trace(wanted)
                    invisible += bool(same)
                    visible += not same
    assert blocked and invisible
    print({'all_width_cylinder_controls': lifts,
           'released_one_row_obstructions': blocked,
           'still_matching_halfwidth_traces': invisible,
           'selected_trace_failures': visible,
           'literal_packed': 'PASS', 'long_collar_lock': 'PASS'})


if __name__ == '__main__':
    main()
