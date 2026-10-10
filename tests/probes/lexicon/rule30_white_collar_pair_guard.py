"""GC1069: distinguish the next actual input obstruction from trace failure.
Missing inference: can GC1068's next sample be chosen independently?
Record searched: boundary|exterior with consecutive|successive|two white|
white.white|input7|input.?10 ->63 hits in22 files; input7|NOT R6|
coupled input7 ->2 hits, GC1068 only. No new general closure found.
P1 BEFORE controls: an actual endpoint R6=0, Q6=1 with R7=0 must
have exterior S6=1 and S7=1, whatever its farther tail. Requested
samples10 cannot keep all three interior rows6,7,8. This excludes
ALL actual representatives retaining those rows, not only one origin.
P2: the two GC1068 constructors have S7=NOT R6 whenever z=1.
The wrong requested input7 is masked when the common R7 is black.
Counterfactual: failure of the old fixed origin alone explains the
next white-white obstruction. P1's local rule must refute this.
Unexpected check: every target continuation still has the same first
W+9 original observations under GC1068's origin: full interior equality
at original time9 shields column1 until timeW+8. At W=10 this is the
full nineteen-observation halfwidth horizon, even if row8 differs.
Controls: one W=10 family, both phases and all selected earlier,
input and farther bits; two continuations from each context. No
solver, membership, NFA, strip-width or trace-language census.
Informed P3 AFTER the first passing block, BEFORE the added controls:
CL240.1 corrects its predecessor: these SAME two origins force
S7=NOT R6 on both z branches. Check this, and distinguish raw input
mismatch from interior failure: a black R7 masks the mismatch.
Hand proof: R'=Q XOR(R OR S); S'=R XOR(S OR T).
R6=0,Q6=1,R7=0 forces S6=1, hence S7=1. At a white R7,
changing S7 flips R8. A mismatch first born at original time10,
siteW cannot reach site1 until timeW+9. Halfwidth for general W
and changed representatives after this obstruction remain OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def main():
    local_guards = 0
    for Q, R, S, T in product((0, 1), repeat=4):
        Rp = Q ^ (R | S)
        Sp = R ^ (S | T)
        if (Q, R, Rp) == (1, 0, 0):
            assert S == Sp == 1
            local_guards += 1
    checked = blocked = masked = row_failures = 0
    examples = []
    for p, q, phase, x, y, z, w, h, k in product((0, 1), repeat=9):
        prefix = (p, q) + bits('010101')
        ref = run(prefix + bits('001110') + (0,)*4, 2, phase)
        child = ref[2][:10]
        assert child[-6:] == bits('010100')
        tail = bits('0000111' if z else '0000000')
        far = (h, k, 1-h, 1-k)*6
        actual = run(prefix + tail + far, 18, phase)
        want8 = strip(child, bits('0100') + (x, y, z, w), phase)
        assert all(actual[t+2][:10] == want8[t] for t in range(4, 8))
        Q6, R6 = want8[6][-2:]
        R7 = want8[7][-1]
        assert actual[9][10] == 1-R6
        bad_row = not R7 and w == R6
        assert (actual[10][:10] != want8[8]) == bool(bad_row)
        assert actual[10][:9] == want8[8][:9]
        row_failures += bool(bad_row)
        if R7 and w == R6:
            assert actual[10][:10] == want8[8]
            masked += 1
        if z:
            if (Q6, R6, w) == (1, 0, 0):
                assert R7 == 0
                assert actual[10][:9] == want8[8][:9]
                assert actual[10][9] != want8[8][9]
                blocked += 1
                if not examples: examples.append((p, q, phase, x, y, z, w))
        for suffix in ((0,)*8, bits('10110101')):
            wanted = strip(child, bits('0100')+(x, y, z, w)+suffix, phase)
            assert trace(actual) == trace(ref[:2]) + trace(wanted)
            checked += 1
    assert blocked and masked
    print({'local_universal_guards': local_guards,
           'nineteen_observation_lifts': checked,
           'white_white_row_obstructions': blocked,
           'black_mask_controls': masked, 'fixed_origin_row_failures': row_failures,
           'first_obstruction': examples,
           'literal_packed': 'PASS', 'visibility_guard': 'PASS'})


if __name__ == '__main__':
    main()
