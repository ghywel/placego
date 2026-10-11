"""GC1113: bound optional M2 waiting without losing the bare connector.

Missing inference: GC1111's M2 cut charges pure typed101 histories,
but what can it charge in the reviewed mixed bridge? GC1106 inserted
one optional B self-loop. Erase that same-state, even-duration loop,
and retain the full 21-cell endpoint and wall phase. No new path search.
Record searched: GC1106|M2|M_2|SLLS with loop.*eras|196|
overlap.*68|connector.*152|minimal.*connector ->5 hits4files,
all unrelated; GC1106/1111/1112 and their explicit witnesses read.
P1 BEFORE execution: E_m has k word (1,2^(m+2),3), duration
152+38m, and common M2 interval length 68+19m. For m=0 the
arbitrary FE_0/EF_0 language has sharp maximum68, not87.
REFUTED-BY: a 69-symbol matching path for those bare generators.
P2 BEFORE execution: m=4 contains every 120-symbol M2 rotation
at positive age; m=3 does not. Thus the reported absence would
bound optional waiting by3, with bridge duration<=266, regardless
of tested phase/rotation. It does not bound the number of bridges.
Counterfactual: the optional B loop is needed for binary branching.
REFUTED-BY: distinct equal-duration FE_0 and EF_0 outputs.
Controls: independent gap and physical h spellings; complete
matching graph with locally verified falling rank; independent
cyclic-generator containment for all19 factors at m=3 and m=4.
Unexpected: loop erasure requires the SAME full B endpoint, and
38 even ticks, to retain wall phase; a matching 20-cell packet alone
would not license erasure. Reuse the reviewed B21=0 witness, do
not rerun its discovery or assert an actual infinite right lift.
This probe makes no CA membership, solver, CUT or record query.
OUTCOME: P1/P2 HELD. The bare mixed language has verified maximum
rank68; its 196-tick generators first differ at44. The parameterized
matching interval agrees exactly, with its two nearest mismatches.
At m=3 only6 of19 rotations occur, at m=4 all19 occur at positive
age; independent cyclic containment agrees. Optional-loop necessity
is REFUTED. The 3-wait/266-tick charge is derived from the reported
L591 absence, whose exact receipt remains pending. Branch counts and
all-depth records remain unbounded by this argument.
"""

import rule30_mixed_m2_overlap as previous


def ks(m):
    return (1,) + (2,) * (m+2) + (3,)


def physical(word):
    h = {'S': '110100', 'L': '1101000100'}
    return ''.join(h[a] for k in word for a in 'SLL'+'S'*k)


def has_cyclic(word, factor):
    extended = word * (2 + len(factor)//len(word))
    return any(extended[i:i+len(factor)] == factor for i in range(len(word)))


def main():
    f = (3,)
    e0 = ks(0)
    p_fe, p_ef = physical(f+e0), physical(e0+f)
    assert len(p_fe) == len(p_ef) == 196
    assert next(i for i, (a, b) in enumerate(zip(p_fe, p_ef)) if a != b) == 44
    assert len(physical(ks(1))) - len(physical(e0)) == 38
    assert 38 % 2 == 0
    words = [previous.spell(f+e0), previous.spell(e0+f)]
    assert words == [p_fe[::2], p_ef[::2]]
    m2 = previous.spell((2,))
    rank = previous.rank_certificate(previous.pair_graph(words, m2))
    assert rank is not None and max(rank.values()) == 68
    assert previous.cyclic_overlap(words[1], m2) == 68

    # The direct interval is a control of the parameterized hand proof.
    # Test only the bare bridge and the two predicted waiting thresholds.
    covers = {}
    factors = {(m2[i:]+m2[:i])*7 for i in range(19)}
    factors = {w[:120] for w in factors}
    assert len(factors) == 19
    for m in (0, 3, 4):
        local = previous.spell(ks(m)+(1,))
        reference = ''.join(m2[(i-16) % 19] for i in range(len(local)))
        end = 11 + 68 + 19*m
        assert local[11:end] == reference[11:end]
        assert local[10] != reference[10] and local[end] != reference[end]
        interval = local[11:end]
        interval_factors = {interval[i:i+120] for i in range(len(interval)-119)}
        cyclic = previous.spell(f+ks(m))
        present = {w for w in factors if has_cyclic(cyclic, w)}
        covers[m] = len(factors & interval_factors)
        if m in (3, 4):
            assert present == factors & interval_factors
    assert covers[3] == 6 and covers[4] == 19
    assert 152+38*3 == 266
    print(dict(P1='HELD', P2='HELD', bare_block_ticks=196,
               first_physical_difference=44, sharp_bare_overlap=68,
               m3_rotations=6, m4_rotations=19, positive_sample_start=11,
               optional_wait_bound=3, bridge_tick_bound=266,
               waiting_bound_scope='reported L591 absence, receipt pending',
               membership_tested=False))


if __name__ == '__main__':
    main()
