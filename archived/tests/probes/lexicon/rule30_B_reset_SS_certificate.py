"""GC1088: a same-history B reset evades immediate mixed-core admission.

Missing inference: GC1085's unguarded B-A-001 bridge's next D return.
Record searched: B.to101.toA|11101001100111010000|unguarded B ->
10 hits in6 files; GC1080/82/83/85/87 read. No admission proof found.
Predictions were written before each control in this order:
P1: A1a1 forces low001000. REFUTED: outputs include001011/010/001.
P2: on D, A1a1 forces returned12<=13. REFUTED:38/256 a0 and64/256
a1 complete local cones violate it. Stop the A-label inequality.
P3: GC1085's B20 with white exterior enters C by32. REFUTED:111
at32; high S at42. This diagnostic alone was not an all-tail proof.
P4: actual A11=1 forces A13=1 and restores P2. The sparse bit is
correct, but the inequality is REFUTED:24/128 cones still violate it.
Stop these A-label variants; retain a concrete same-history evasion.
P5: B20 plus24 white cells forces high111 with10..12 black at32,
then S at42, for every farther tail. HELD by causal-prefix induction.
P6: that S takes SS and has white marker6 at48. SS HELD; white marker
REFUTED. The actual black-marker SS prefix is11101111000111011.
Counterfactual: immediate admission into GC1087 C/J/guarded-B after
the B-A reset. This certificate stays outside at32,42 and48.
REFUTED-BY: any failed prefix implication or literal/packed mismatch
invalidates the certificate; no longer census is substituted for it.
Independent controls: each step with both fresh right inputs, then
32 composed histories checked with literal and packed engines.
Unexpected: actual SS still has black sixth marker; GC1056's white
absorption theorem must not be strengthened to immediate whitening.
No solver, CUT, membership or relaxed-record run. No eventual escape
or eventual nonadmission asserted. All-depth bound remains OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import update, propagate, S

SOURCE = bits('11101001100111010000' + '0'*24)
CHECKPOINTS = {
    6: '11100110111011',
    16: '1110100011111',
    22: '111001001001011',
    32: '111001111111',
    42: '11101110101000010111',
    48: '11101111000111011',
}


def certificate():
    rows = [SOURCE]
    for t in range(48):
        old = rows[-1]
        new = update((t % 2,) + old)
        # A black last known cell masks the unknown next cell in OR.
        if old[-1]:
            new += (old[-2] ^ 1,)
        for exterior in (0, 1):
            assert update((t % 2,) + old + (exterior,))[:len(new)] == new
        rows.append(new)
    for t, expected in CHECKPOINTS.items():
        assert rows[t][:len(expected)] == bits(expected)
    assert tuple(row[4] for row in rows[22:32]) == bits('0101100000')
    assert tuple(row[4] for row in rows[32:42]) == bits('0101101010')
    assert tuple(row[4] for row in rows[42:48]) == bits('111010')
    return rows


def main():
    forced = certificate()
    for far in product((0, 1), repeat=5):
        rows = run(SOURCE + far + tuple(1-x for x in far)*8, 48)
        for t, prefix in enumerate(forced):
            assert rows[t][:len(prefix)] == prefix
    # Retain explicit false inequality controls, rather than relying on
    # the exploratory counts as the proof of failure.
    for a, far in ((0, '10100010'), (1, '00001000')):
        out = propagate(bits('00011') + (a, 1) + bits(far), S)[6]
        assert out[4:8] == (0, 0, 1, 0)
    out = propagate(bits('00011111') + bits('1101000'), S)[6]
    assert out[4:8] == (0, 0, 1, 0)
    print(dict(prefix_implications=96, composed_controls=32,
               literal_packed='PASS', return32='111 high',
               return42='S', return48='S with black marker6',
               immediate_admission='REFUTED', eventual_admission='OPEN',
               all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
