"""GC1060: exact boundary carrier for a prefix-preserving two-tick lift.
Missing inference (GC1059/CL222): can the next bit of a repaired time2
row be lifted while retaining its earlier row prefix and initial prefix?
Record searched: two-tick/two-step with lift/fixed-prefix/prehistory
->26 hits; adding toggle/surject/last-bit/penultimate/freedom ->6 hits.
G236's known two-step bulk transducer is reused, not reinvented.
P1 before controls: for fixed initial prefix through j+1, j>=3, write
u,a,b,c for sites j-2..j+1, P=u XOR(a OR b), Q=time2 sitej,
R=time2 sitej+1. The complete admissible (Q,R) relation is:
bc01: (NOT P,a); bc10,a0: (NOT P,0); bc10,a1: (either,1);
bc11: (P XOR NOT a,either); bc00,a1: (NOT P,either);
bc00,a0: (P,0),(P,1),(NOT P,1).
P2: given feasible Q, both R bits lift iff bc11 OR
(bc00 AND(a1 OR Q=P)). In particular arbitrary last-bit replacement
is NOT a sound induction step; mixed bc locks R to a.
Counterfactual: GC1059 normalization grants this lifting freedom too.
Independent controls: literal/packed actual cones for128 local cases,
and explicit tail construction for each permitted pair, no NFA census.
Unexpected check: prefix0000 has BOTH R values without conditioning,
but fixing Q=1 forces R=1. The child-prefix condition cannot be dropped.
No arbitrary whole-tail lift, halfwidth induction or record bound claim.
OUTCOME:128 local cones and56 explicit pair/phase lifts PASS;
conditioned freedom, translated0001 blocker and0000 Q guard PASS.
Uniform criterion is hand algebra awaiting second reading.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def relation(u, a, b, c):
    P = u ^ (a | b)
    if (b, c) == (0, 1):
        return {(1-P, a)}
    if (b, c) == (1, 0):
        return {(1-P, 0)} if a == 0 else {(0, 1), (1, 1)}
    if (b, c) == (1, 1):
        return {(P ^ (1-a), r) for r in (0, 1)}
    return {(1-P, r) for r in (0, 1)} if a else {(P, 0), (P, 1), (1-P, 1)}


def tail(u, a, b, c, Q, R):
    assert (Q, R) in relation(u, a, b, c)
    P = u ^ (a | b)
    if (b, c) == (1, 1):
        return (0, a ^ R)
    if (b, c) == (0, 0):
        if a:
            return (0, 1-R)
        d = Q ^ P
        return (d, R if d == 0 else 0)
    if (b, c) == (1, 0) and a:
        return (1 ^ Q ^ P, 0)
    return (0, 0)


def main():
    cones = witnesses = 0
    for prefix, phase in product(product((0, 1), repeat=4), (0, 1)):
        u, a, b, c = prefix
        got = set()
        earlier = None
        for d, e in product((0, 1), repeat=2):
            child = run(prefix + (d, e), 2, phase)[2]
            got.add(child[2:4])
            if earlier is None:
                earlier = child[:2]
            assert child[:2] == earlier
            cones += 1
        assert got == relation(*prefix)
        P = u ^ (a | b)
        for Q in {q for q, r in got}:
            free = {r for q, r in got if q == Q} == {0, 1}
            assert free == ((b, c) == (1, 1) or
                            ((b, c) == (0, 0) and (a == 1 or Q == P)))
        for Q, R in got:
            child = run(prefix + tail(*prefix, Q, R), 2, phase)[2]
            assert child[2:4] == (Q, R) and child[:2] == earlier
            witnesses += 1
    assert relation(0, 0, 0, 0) == {(0, 0), (0, 1), (1, 1)}
    for d, e in product((0, 1), repeat=2):
        assert run(bits('0001') + (d, e), 2)[2] == bits('1110')
        # Translate the same carrier past an unrelated common prefix.
        assert run(bits('10100001') + (d, e), 2)[2][6:8] == (1, 0)
    print({'local_cones': cones, 'explicit_pair_lifts': witnesses,
           'literal_packed': 'PASS', 'conditioned_freedom': 'PASS',
           '0001_blocker_translation': 'PASS', '0000_Q_guard': 'PASS'})


if __name__ == '__main__':
    main()
