"""GC1149: closing-inclusive white-time SS cuts for a zero-record query.

Record searched: GC626|GC606|110100|synchron AND
even.sample|odd|startup|marker|finite ->303 hits75files.
Read GC626,705,706,707,1148 and RRL transducer's terminal convention.
Missing inference: translate GC1148's full-time inequality into the
white-time visible alphabet, with an arbitrary startup and exact endpoints.
P1 BEFORE execution: every actual completed short gap, even from an
unmarked startup, gives full-time110100. No first-gap loss is necessary.
P2: let T=d+L full-time samples be retained at indices0..T-1.
At white anchor a=phase+2s put n=ceil((d+a+6)/6).
If L>=2a+6 and a+6n<T, the white-time word(100)^n1 at index s
is forbidden CONDITIONAL ON the initial zero interval[d,d+L-1].
The observed closing1 forces n actual S gaps; P1 lifts them to6n
full-time samples, and GC1148 rejects the initial zero interval.
Counterfactual: omitting the closing bit still fixes the full lift.
Find an actual100 prefix whose full-time word is not110100.
Independent control: all1024 complete10-cell cones by the literal
Wolfram truth table, checked against a separate packed shrinking engine.
Unexpected: both black-origin odd anchors and query windows where the
minimum full-time contradiction fits but its visible closing does NOT.
No solver, CUT, record census, language enumeration, strip widening,
admission search or Cloud realization work. Finite controls supplement
the hand proof; they do not supply its all-depth quantifier.
ADDENDUM BEFORE adapter controls: physical samples and RRL's tested
samples have different terminal conventions. An M=d+L pair word's
last visible bit is unused by direct_initial. Use terminal_drop=1:
the closing bit must satisfy a+6n<M-1, i.e. be at mostM-2.
The first run's P2 is correct for physically retained full samples;
it must not silently substitute M for the RRL tested horizonM-1.
Check both conventions and retain cases accepted only by the former.
"""
from itertools import product

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
H = (1, 1, 0, 1, 0, 0)


def literal(row, ticks, phase=0):
    rows = [tuple(row)]
    for t in range(ticks):
        old = rows[-1]
        wall = (phase+t) % 2
        rows.append(tuple(TABLE[4*(wall if i == 0 else old[i-1])
                                + 2*old[i]+old[i+1]]
                          for i in range(len(old)-1)))
    return rows


def packed(row, ticks, phase=0):
    value = sum(b << i for i, b in enumerate(row))
    width = len(row)
    rows = [tuple(row)]
    for t in range(ticks):
        value = (((value << 1) | ((phase+t) % 2))
                 ^ (value | (value >> 1))) & ((1 << (width-1))-1)
        width -= 1
        rows.append(tuple((value >> i) & 1 for i in range(width)))
    return rows


def specification(d, L, phase, terminal_drop=0):
    """Indexed cuts in white-time q; no globally forbidden word list."""
    T = d+L-terminal_drop
    cuts = []
    for a in range(phase, max(0, (L-6)//2+1), 2):
        n = (d+a+11)//6
        if a+6*n < T:
            cuts.append(((a-phase)//2, '100'*n+'1', a, n))
    return cuts


def main():
    short = unmarked = 0
    truncated = None
    for row in product((0, 1), repeat=10):
        rows = literal(row, 6)
        assert rows == packed(row, 6)
        v = tuple(r[0] for r in rows)
        q = v[::2]
        if q == (1, 0, 0, 1):
            assert v[:6] == H
            assert row[:3] == (1, 1, 1)
            short += 1
            unmarked += row[:4] != (1, 1, 1, 0)
        if q[:3] == (1, 0, 0) and v[:6] != H and truncated is None:
            truncated = (''.join(map(str, row)), ''.join(map(str, v)))
    assert short and unmarked and truncated
    # Independent end/index checks, not actual visible-language membership.
    checked = odd = nonfitting = adapter = boundary = 0
    for d in range(1, 61):
        for L in range(1, 41):
            for phase in (0, 1):
                T = d+L
                for s, word, a, n in specification(d, L, phase):
                    assert a == phase+2*s and (phase+a) % 2 == 0
                    assert L >= 2*a+6 and 6*n >= d+a+6
                    assert 6*(n-1) < d+a+6
                    times = tuple(phase+2*(s+j) for j in range(len(word)))
                    assert times[0] == a and times[-1] == a+6*n
                    assert all(t < T for t in times)
                    assert word == '100'*n+'1'
                    checked += 1
                    odd += phase
                for a in range(phase, max(0, (L-6)//2+1), 2):
                    K = d+a+6
                    n = (K+5)//6
                    assert a+K <= T
                    nonfitting += a+6*n >= T
                physical = specification(d, L, phase)
                tested = specification(d, L, phase, terminal_drop=1)
                assert all(cut in physical for cut in tested)
                for s, word, a, n in tested:
                    assert a+6*n <= T-2
                    adapter += 1
                for cut in physical:
                    if cut not in tested:
                        assert cut[2]+6*cut[3] == T-1
                        boundary += 1
    assert checked and odd and nonfitting and adapter and boundary
    # The formula has no small-depth dependence. Do not allocate these words.
    large = 0
    for d in (10**6+1, 10**9+3, 10**18+5):
        for phase in (0, 1):
            a = phase
            n = (d+a+11)//6
            L = max(2*a+6, a+6*n-d+1)
            assert a+6*n < d+L and 6*n >= d+a+6
            large += 1
    print(dict(complete_cones=1024, literal_packed='PASS',
               completed_S=short, unmarked_S=unmarked,
               truncated_counter=truncated, indexed_cuts=checked,
               odd_anchor_cuts=odd, closing_outside_query=nonfitting,
               RRL_tested_cuts=adapter, unused_terminal_exclusions=boundary,
               large_integer_controls=large,
               first_gap_loss=0, all_depth_R_real='OPEN'))


if __name__ == '__main__':
    main()

# OUTCOME: P1/P2 and terminal adapter HELD in their stated conventions.
# 1024 literal/packed cones;96 completedS,64 initially unmarked.
# Unclosed lift REFUTED by1000000000 ->1100010.
# 15880 physical cuts,7450 odd anchors,14920 RRL cuts;
# 960 closings at unused terminal,3560 rounded closings out of window.
# Six large-integer controls PASS. Quantifier is supplied by hand proof.
# No startup loss; all-depth record bound and non-SS coverage remain OPEN.
