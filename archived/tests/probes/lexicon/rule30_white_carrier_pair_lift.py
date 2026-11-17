"""GC1065: the remaining white carrier lifts a joint boundary pair.
Missing inference: GC1064's 011,Q0,R1 guard blocks a wrong future R0.
Retain initial through j-1 and entire time2 child through j (j>=3).
If initial j-2,j-1=01 and child j=0, either next-child pair R,S lifts.
S is the first future exterior; the whole first future interior update
therefore lifts too, while original first two observations are retained.
Record searched:011|white.*carrier|white.*predecessor with origin
release/prefix j-1 ->12 hits in4 files. Frontier/ENTRY/G236 with011
and origin/prefix ->82 hits in33 files. G236/GC549 checkpoint28 already
has EXACTLY the five-state frontier below; no new subset/width census.
P1 before controls: varying initial b,c,d after retained u,a=01 and
emitting Q0 yields {1000,1001,1010,1011,1100}, independent of j/phase.
P2: set b=c=0, d=NOT R AND NOT S, e=NOT R AND S;
if R1 set f=S, otherwise f is arbitrary. Then next child bits are R,S.
Counterfactual: changing b destroys a preceding child cell. The fixed
first-update black cell P1 must mask that change in the whole prefix.
Known whole-tail-reset failure: G236's frontier forbids next tail011.
Reuse its proof, not another absence or automaton-universality run.
Unexpected: normalizing every origin to b=c=00 is NOT complete at
three outputs: tail110 lifts through bc01, but bc00 with R=S=1 forces T1.
Independent controls: literal and packed;256 local cones,64 selected
joint constructors, both phases and actual farther bits. No solver,
visible language membership, strip widths or return-word computation.
Exact conditional spatial origin language is not an all-future trace
invariant, nor an all-depth record bound. Future selection still missing.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_gpt_entry_image import ENTRY, bulk


def main():
    frontier = set()
    for b, c, d in product((0, 1), repeat=3):
        if bulk((0, 1, b, c, d)) == 0:
            frontier.add((1, b, c, d))
    assert frontier == ENTRY
    qualifying = 0
    for v, b, c, d, e, f, g, phase in product((0, 1), repeat=8):
        initial = (v, 0, 1, b, c, d, e, f, g)
        child = run(initial, 2, phase)[2]
        if child[3] == 0:
            qualifying += 1
            assert child[4:7] != (0, 1, 1)  # Reviewed G236 guard reused.
    lifts = 0
    for v, phase, R, S, extra_f, extra_g in product((0, 1), repeat=6):
        d, e = (1-R) & (1-S), (1-R) & S
        f = S if R else extra_f
        actual = run((v, 0, 1, 0, 0, d, e, f, extra_g, 0), 2, phase)
        reference = run((v, 0, 1, 1, 0, 0, 0, 0, 0, 0), 2, phase)
        assert actual[2][:4] == reference[2][:4]
        assert actual[2][4:6] == (R, S)
        assert tuple(r[0] for r in actual[:2]) == tuple(r[0] for r in reference[:2])
        # Future width5 interior: lifting R plus S lifts its first full update.
        wanted = reference[2][:4]+(R,)
        wall = phase
        one = tuple((wall if j == 0 else wanted[j-1])
                    ^ (wanted[j] | (wanted[j+1] if j < 4 else S))
                    for j in range(5))
        extended = run((v, 0, 1, 0, 0, d, e, f, extra_g, 0), 3, phase)
        assert extended[3][:5] == one
        lifts += 1
    for v, phase in product((0, 1), repeat=2):
        child = run((v,)+bits('01011101'), 2, phase)[2]
        assert child[3:7] == (0, 1, 1, 0)
        for g in (0, 1):
            child = run((v,)+bits('0100001')+(g,), 2, phase)[2]
            assert child[3:7] == (0, 1, 1, 1)
    print({'frontier_states': len(frontier), 'local_cones': 256,
           'Q0_origin_controls': qualifying, 'joint_pair_lifts': lifts,
           'noncanonical_110_controls': 4, 'literal_packed': 'PASS',
           'first_future_update': 'PASS', 'known_011_guard': 'PASS',
           'greedy_normal_form_incomplete': 'PASS'})


if __name__ == '__main__':
    main()
