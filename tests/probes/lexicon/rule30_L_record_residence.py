"""GC1151: all-depth record-conditioned residence for completed L chains.

Missing inference: extend indexed SS restrictions to pure L, with a
proved white-time lift from arbitrary startup and closing boundaries.
Record searched: all.L|all-L|L380|155|rigid.L AND
ring|gap|zero|white|forced|certificate|period ->654 hits158files.
GC626/706/743/745, L380's saved ring and GC1148/49 read.
P1 BEFORE run: saved155-ring has maximal cyclic white gap6.
P2: every completed visible L=10000 with closing1 has full1101000100,
including an unmarked1101 startup and a terminal100/101 exit.
P3 hand proof: initial zeros[d,d+L-1] and N full periodic L samples
from white anchor a imply L<=2a+6 OR N<=d+a+6, at EVERY depth.
Contradiction uses seven whites in the overlap of the shrinking
white interval and the inverse-forced reference ring.
White-time cut: n=ceil((d+a+7)/10); forbid(10000)^n1 at white index
s=(a-phase)/2 when L>=2a+7 and a+10n<T-drop. T=d+L; drop=1
for RRL's unused last paired visible sample, otherwise drop=0.
Counterfactual: the long gap's final closing marker must be1110 to
fix its ten samples. Retain actual closing100/101 countercontrols.
Independent: literal and packed complete13-cell cones; scalar saved
ring evolution; decoded triangles check every literal Rule30 edge.
Unexpected: initial1101 lacks1110 but has exactly the canonical lift.
No AL graph rerun, solver, CUT, language/record census, strip widening,
Cloud witness-fate computation or all-mixed-white-gap assertion.
"""
from itertools import product
from rule30_SS_record_even_cut import literal, packed
from rule30_SS_record_residence import decode

RING = 0x35409b1caa645d715104db5291a2fe8415260ce
P = 155
H = tuple(map(int, '1101000100'))
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def ring(i):
    return (RING >> (i % P)) & 1


def cuts(d, L, phase, terminal_drop=1):
    out = []
    for a in range(phase, max(0, (L-7)//2+1), 2):
        n = (d+a+16)//10
        if a+10*n < d+L-terminal_drop:
            out.append(((a-phase)//2, '10000'*n+'1', a, n))
    return out


def main():
    black = [i for i in range(P) if ring(i)]
    G = max(j-i-1 for i, j in zip(black, black[1:]+[black[0]+P]))
    assert G == 6
    assert all(any(ring(i+j) for j in range(7)) for i in range(P))
    old = tuple(ring(i) for i in range(P))
    for t in range(10):
        assert old[0] == t % 2 and old[1] == H[t]
        old = tuple(TABLE[4*old[(i-1) % P]+2*old[i]+old[(i+1) % P]]
                    for i in range(P))
    assert old == tuple(ring(i) for i in range(P))
    completed = unmarked = exited = 0
    exits = {}
    for row in product((0, 1), repeat=13):
        rows = literal(row, 10)
        assert rows == packed(row, 10)
        v = tuple(r[0] for r in rows)
        if v[::2] == (1, 0, 0, 0, 0, 1):
            assert v[:10] == H
            assert row[:4] == (1, 1, 0, 1) or row[:5] == (1, 1, 1, 0, 0)
            completed += 1
            unmarked += row[:4] == (1, 1, 0, 1)
            end = ''.join(map(str, rows[10][:3]))
            exits[end] = exits.get(end, 0)+1
            exited += end in ('100', '101')
    assert completed and unmarked and exited
    # Minimal full-sample contradiction, arbitrary visible prefixes.
    tested = 0
    for a in range(7):
        for prefix in product((0, 1), repeat=a):
            for d in range(1, 13):
                K = d+a+7
                v = prefix+tuple(H[t % 10] for t in range(K))
                row, cols = decode(v, a % 2)
                assert len(row[d:]) == 2*a+7 and any(row[d:])
                assert all(cols[-k][a] == ring(-k) for k in range(K))
                tested += 1
    fitted = odd = discarded = 0
    for d in range(1, 61):
        for L in range(1, 37):
            for phase in (0, 1):
                physical = cuts(d, L, phase, 0)
                tested_cuts = cuts(d, L, phase, 1)
                assert all(c in physical for c in tested_cuts)
                for s, word, a, n in tested_cuts:
                    assert a == phase+2*s
                    assert L >= 2*a+7 and 10*n >= d+a+7
                    assert 10*(n-1) < d+a+7
                    assert a+2*(len(word)-1) == a+10*n <= d+L-2
                    fitted += 1
                    odd += phase
                discarded += len(physical)-len(tested_cuts)
    # The length threshold is essential even on an actual infinite ring.
    d = next(d for d in range(1, P+1)
             if not any(ring(-k) for k in range(d, d+6)))
    assert any(ring(-k) for k in range(d, d+7))
    for depth in (10**6+1, 10**9+3, 10**18+5):
        for phase in (0, 1):
            a = phase
            n = (depth+a+16)//10
            L = 2*a+18  # sufficient RRL endpoint fit at every depth
            assert a+10*n <= depth+L-2 and 10*n >= depth+a+7
    print(dict(cyclic_white_gap=G, literal_ring='PASS', complete_cones=8192,
               completed_L=completed, unmarked_1101=unmarked,
               final_triples=exits, final_marker_countercontrols=exited,
               truncated_controls=tested, RRL_cuts=fitted,
               odd_anchor_cuts=odd, unused_terminal_discarded=discarded,
               six_white_ring_counter_depth=d,
               first_gap_loss=0, mixed_records='OPEN', all_depth_R_real='OPEN'))


if __name__ == '__main__':
    main()

# OUTCOME: P1/P2/P3 HELD.155-ring gap6 and literal closure PASS.
# 8192 complete cones,768 L,512 unmarked; final100/101/111=432/48/288.
# Final-marker counterfactual REFUTED by480 terminal exits.
# 1524 truncated controls;9120 RRL cuts,4194 odd anchors;
# 750 unused-terminal discards, six large-integer fits PASS.
# Actual ring at depth10 has six whites and unlimited L residence.
# Mixed/untyped records and every-depth R_real remain OPEN.
