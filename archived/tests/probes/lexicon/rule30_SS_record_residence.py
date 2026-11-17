"""GC1148: record-conditioned residence of a visible all-SS block.

Missing inference: replace arbitrary SS residence by a finite,
depth-dependent budget when testing a long initial left zero run.
Record searched:110100|GC705|L372 AND white.interval|white.window|
zero.interval|zero.window|record.bound|record.condition ->12 hits10files.
GC686,705,706,710, L372 and RULE30-PRIZE8.71 read. L372's ring
identity and GC706's visible lift are reused, not rediscovered.
P1 BEFORE controls: the saved84-cell ring has largest cyclic
spatial white gap5. Its least period is not needed here.
P2 BEFORE controls: let a>=0 have a white wall, and column1 on
times a..a+N-1 be(110100)^n, N=6n. An initial zero interval at
depths d..d+L-1 obeys L<=2a+5 OR N<=d+a+5, at EVERY depth.
Proof: the white triangle at time a covers depths d+a through
d+L-1-a, while the visible block fixes the ring through depthN-1.
Six consecutive cells in the common interval contradict P1.
Counterfactual: SS residence is bounded without the L threshold.
The known infinite all-S ring has actual five-white intervals and
unbounded SS residence, so this unconditional deadline must fail.
Independent controls: direct scalar ring evolution, fresh temporal
left-permutive reconstruction with all local edges checked, and
all127 arbitrary visible prefixes at a=0..6 (both wall phases).
Unexpected: a may be odd if the initial wall phase is black.
Check that the block's START is white; copying initial phase0
to every odd a would silently change the hypotheses.
REFUTED-BY: any failed ring equality, gap>5, or zero interval
violating the displayed disjunction in a reconstructed tableau.
No record search by solver, new language computation, strip,
inverse ancestry, SS cutoff theorem or original676 admission run.
ADDENDUM before truncated-window controls: the same proof uses
only the N observed samples and thus holds for any N, not just6n.
P3: in a (d,L) record query with T=d+L samples, for every white
anchor0<=a<=floor((L-6)/2), forbid the lengthK=d+a+6 prefix of
(110100)^infinity at a. Its end a+K=d+2a+6<=T is already observed.
These are INDEXED, QUERY-CONDITIONED cuts, not globally absent
words. Test all127 prefixes again with d=1..12 and the minimal
truncated lengthK; every full left-zero target must be rejected.
T,K,N,a count FULL-TIME column1 samples. Applying the condition
to an even-sampled language requires its justified temporal lift;
do not identify an arbitrary even prefix with the full110100 word.
"""
from itertools import product
from rule30_all_s_left_depth import RING, P

H = tuple(map(int, '110100'))
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def ring(i):
    return (RING >> (i % P)) & 1


def decode(v, phase):
    cols = {0: tuple((phase+t) % 2 for t in range(len(v))), 1: v}
    row = [cols[0][0]]
    for k in range(1, len(v)):
        up, right = cols[1-k], cols[2-k]
        now = tuple(up[t+1] ^ (up[t] | right[t])
                    for t in range(len(up)-1))
        cols[-k] = now
        row.append(now[0])
        for t, left in enumerate(now):
            assert up[t+1] == TABLE[4*left+2*up[t]+right[t]]
    return row, cols


def main():
    # The reviewed ring is reused; this control checks the new
    # spatial-gap constant with a literal implementation.
    old = tuple(ring(i) for i in range(P))
    gap_positions = [i for i in range(P)
                     if not any(ring(i+j) for j in range(5))]
    assert gap_positions
    assert all(any(ring(i+j) for j in range(6)) for i in range(P))
    cyclic_gaps = []
    black = [i for i, b in enumerate(old) if b]
    for i, j in zip(black, black[1:]+[black[0]+P]):
        cyclic_gaps.append(j-i-1)
    assert max(cyclic_gaps) == 5
    for t in range(6):
        assert old[0] == t % 2 and old[1] == H[t]
        old = tuple(TABLE[4*old[(i-1) % P]+2*old[i]+old[(i+1) % P]]
                    for i in range(P))
    assert old == tuple(ring(i) for i in range(P))
    # Arbitrary prefixes need not have a physical right realization;
    # their reconstructed LEFT tableaux nevertheless obey every
    # local Rule30 equation, which is enough for this implication.
    prefixes = windows = matched = 0
    N = 48
    for a in range(7):
        phase = a % 2
        assert (phase+a) % 2 == 0
        for prefix in product((0, 1), repeat=a):
            v = prefix + H*8
            row, cols = decode(v, phase)
            for k in range(N):
                assert cols[-k][a] == ring(-k)
                matched += 1
            L = 2*a+6
            for d in range(1, N-a-5):
                assert N >= d+a+6
                assert any(row[d:d+L])
                assert len(row[d:d+L]) == L
                windows += 1
            prefixes += 1
    # Actual infinite all-S supplies the threshold countercontrol.
    d = next(d for d in range(1, P+1)
             if not any(ring(-k) for k in range(d, d+5)))
    assert any(ring(-k) for k in range(d, d+6))
    counter_N = 6*(d+6)
    assert counter_N > d+5
    actual, _ = decode(H*(counter_N//6), 0)
    assert actual[d:d+5] == [0]*5
    truncated = fits = 0
    for a in range(7):
        for prefix in product((0, 1), repeat=a):
            for depth in range(1, 13):
                K = depth+a+6
                v = prefix + tuple(H[t % 6] for t in range(K))
                row, cols = decode(v, a % 2)
                assert any(row[depth:])
                assert len(row[depth:]) == 2*a+6
                assert all(cols[-k][a] == ring(-k) for k in range(K))
                truncated += 1
    for depth in range(1, 34):
        for L in range(1, 25):
            for phase in (0, 1):
                for a in range((L-6)//2+1):
                    if (phase+a) % 2:
                        continue
                    K = depth+a+6
                    assert L >= 2*a+6
                    assert a+K <= depth+L
                    fits += 1
    print(dict(max_cyclic_white_gap=5, gap_positions=gap_positions,
               prefix_tableaux=prefixes, tested_record_windows=windows,
               late_ring_matches=matched, literal_ring='PASS',
               record_disjunction='ALL-DEPTH HAND PROOF',
               unconditional_SS_deadline='REFUTED by saved actual ring',
               five_white_counter_depth=d, counter_N=counter_N,
               truncated_query_controls=truncated, query_fit_checks=fits,
               odd_a_phase_control='PASS',
               original_A_26='L>=58 implies6n<=d+31',
               all_depth_R_real='OPEN'))


if __name__ == '__main__':
    main()

# OUTCOME: P1/P2/P3 HELD. The saved ring's cyclic white gap is
# exactly5 (five-zero spatial window at22; in depth order at58).
#127 prefix tableaux give4692 record windows and6096 ring matches;
#1524 truncated-query controls and3300 query-fit checks PASS.
# All decoded local edges use the literal Rule30 table; scalar
# ring evolution closes at6. The odd-a initial-black phase passes.
# Unconditional residence refuted: actual ring has L=5 at d=58
# and N=384 (indeed unlimited), larger than d+5. Threshold matters.
# Proof is all-depth; these finite controls are not its induction.
# Record-conditioned restrictions are indexed by d,L,phase and a;
# they must not enter the list of globally absent language words.
# All-depth R_real, total untyped residence and676 admission OPEN.
