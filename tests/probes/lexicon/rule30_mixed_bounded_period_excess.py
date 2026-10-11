"""GC1118: can periodic-piece deadlines pay for every bare mixed path?

Missing inference: repeated use of the bare E/F connectors might force
periodic factors with unbounded excess above twice their period. Test
an explicit path for which an ALL-PERIODS hand proof can refute that
inference, not a finite scan or an actual right-half realization.
Record searched: FE.?EF|GC1113|Thue.?Morse|overlap.?free with
periodic.*(excess|block|piece)|139|278|bounded.*power|critical.*exponent|
E.?F.*cod ->22 hits8files; GC706/707 and GC1113 read. Ordinary TM
finite-left exclusions are parked and concern a different temporal
word; this unequal-length coding is only a mixed-relaxation control.
P1 BEFORE execution: the 20-bit motif starting at a first L of k=1
recognizes exactly E starts in every E/F concatenation, despite F
being a suffix of E. On the Thue-Morse E/F path the marker spacing
is at most120. A hand overlap-descent proof then gives L<=2P+139
for EVERY visible factor of period P, including unaligned factors.
REFUTED-BY: a false motif occurrence or a defect in that descent.
P2 BEFORE execution: this path has no synchronized physical periodic
block whose length exceeds twice its period by more than278. Thus
GC706's inequalities alone cannot exclude it when initial J>=278.
This is NOT compatibility with an actual finite left or right half.
Counterfactual: every infinite bare mixed path violates some GC706
periodic-piece inequality at every fixed J. The explicit bound is
the counterexample for J>=278, provided the hand proof is sound.
Independent controls: literal h(S)/h(L) versus gap spelling; exhaust
all four E/F seams for the marker; directly project repeated h blocks
to visible periods. Periodic all-E/all-F controls MUST have arbitrarily
large excess. No CA membership, relaxed-record or solver computation.
Unexpected check: E/F is not prefix/suffix-free (F is E's suffix);
recognizability must use the k=1 first-L motif, not an assumed uniquely
decodable code. Odd-period overlap descent is checked separately from
even-period descent in finite TM prefixes, as a control of the proof.
OUTCOME: P1/P2 HELD. All316 seam windows recognize exactly E starts;
independent physical/gap spellings agree. The512-bit source control
has no overlap in28608 tested factors (14336 odd,14272 even periods).
E spacings are76,98,120. All-E/all-F have excess1064/308, as required.
The all-period bounds139 visible/278 aligned physical are HAND proofs
in GC1118, not extrapolations of these controls. The proposed universal
periodic-piece charge is REFUTED for this relaxed path with J>=278.
Actual finite-left and infinite-right realization remain unasserted.
"""

from itertools import product
import rule30_mixed_m2_overlap as old


KS = {0: (1, 2, 2, 3), 1: (3,)}  # E, F: closed joint21 walks
MARKER = '10000100001001001000'


def physical(ks):
    h = {'S': '110100', 'L': '1101000100'}
    return ''.join(h[a] for k in ks for a in 'SLL' + 'S' * k)


def encode(bits):
    return ''.join(old.spell(KS[b]) for b in bits)


def first_l_positions(bits):
    r, positions = 3, []
    for b in bits:
        if b == 0:
            positions.append(r)
        r += 76 if b == 0 else 22
    return positions


def occurrences(word, motif):
    return [i for i in range(len(word) - len(motif) + 1)
            if word[i:i+len(motif)] == motif]


def main():
    for b in (0, 1):
        assert old.spell(KS[b]) == physical(KS[b])[::2]
    assert len(encode([0])) == 76 and len(encode([1])) == 22
    assert encode([0]).endswith(encode([1]))
    assert encode([0])[3:23] == MARKER
    # Every motif window is shorter than the shortest block, so it
    # crosses at most one seam. Exhaustive ordered pairs suffice.
    seam_windows = 0
    for bits in product((0, 1), repeat=2):
        q = encode(bits)
        expected = [r for r in first_l_positions(bits)
                    if r+len(MARKER) <= len(q)]
        assert occurrences(q, MARKER) == expected
        seam_windows += len(q) - len(MARKER) + 1

    # A finite prefix is a control of the hand theorem, NOT evidence
    # extrapolated to all depths, periods, or infinite realization.
    tm = [0]
    for _ in range(9):
        tm = [c for b in tm for c in (b, 1-b)]
    assert all(tm[2*i] != tm[2*i+1] for i in range(len(tm)//2))
    assert all(tm[2*i] == tm[i] for i in range(len(tm)//2))
    checked = odd = even = 0
    for p in range(1, 65):
        for a in range(len(tm)-2*p):
            w = tm[a:a+2*p+1]
            assert w[:p+1] != w[p:]
            checked += 1
            odd += p % 2
            even += 1 - p % 2
    q = encode(tm)
    starts = first_l_positions(tm)
    assert occurrences(q, MARKER) == starts
    gaps = [s-r for r, s in zip(starts, starts[1:])]
    assert set(gaps) == {76, 98, 120}
    # Direct physical projection confirms the ONLY implication used:
    # an aligned physical D-periodic block yields visible period D/2.
    periodic_controls = {}
    for b in (0, 1):
        h = physical(KS[b])
        p = len(h)//2
        finite = h*16
        assert finite[:len(finite)-len(h)] == finite[len(h):]
        visible = finite[::2]
        assert visible[:-p] == visible[p:]
        excess = len(visible) - 2*p
        assert excess > 139
        periodic_controls['EF'[b]] = excess
    print(dict(P1='HELD controls; all-period bound proved in GC1118',
               P2='HELD by projection of the hand bound',
               marker=MARKER, seam_windows=seam_windows,
               tm_bits=len(tm), overlap_controls=checked,
               odd_period_controls=odd, even_period_controls=even,
               E_spacing=sorted(set(gaps)), visible_excess_bound=139,
               aligned_physical_excess_bound=278,
               periodic_control_excess=periodic_controls,
               membership_tested=False, all_depth_certificate=False))


if __name__ == '__main__':
    main()
