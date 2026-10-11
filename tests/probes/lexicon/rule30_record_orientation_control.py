"""GC1152: distinguish the LEFT-record claim from CL348/349's RIGHT tests.

Missing inference: do the two published counterexamples meet the
zero-interval premise of GC1148/1151? Depth k there is site -k.
Record searched: CL348|CL349|negative.depth|sites.*1.*12 with
permut|record|GC1148|GC1151 ->26 hits17files. Sources GC1148/49/51,
CL348/349, Cloud's check and WORKING-TOGETHER section8 read.
P1 BEFORE run: both published right rows reproduce eleven samples
of the specified S or L trace with the alternating wall clamped.
P2: inverse decoding fixes sites 0,-1,...,-10 to the reference
ring, and each claimed zero interval on that LEFT side has a black.
Counterfactual: the right interval is also white at the same negative
depths. It must fail on both examples, so neither refutes the claim.
Independent controls: scalar complete full-row evolution versus a
packed engine, retaining only the complete cone; reference ring bits
versus the already published left decoder (all its edges are checked).
Unexpected: join each right counterexample to its forced left prefix
and zeros outside; the resulting finite configuration must generate
the wall and trace for eleven samples WITHOUT any clamping.
REFUTED-BY: a left target with all zeros, a ring/decode mismatch, or
a failure of the complete finite-row replay. Only the two published
examples; no new census, solver, right-language or mixed-gap run.
OUTCOME 2026-10-11 14:40 UTC: P1 and P2 PASS on both examples.
S full trace11010011010 fixes left depths0..10 to00110100010;
left depths5..10 read100010, while right sites5..10 are000000.
L full trace11010001001 fixes left depths0..10 to00110101010;
left depths4..10 read0101010, while right sites4..10 are0000000.
The counterfactual fails twice. Both unclamped finite full-row
controls PASS, scalar/packed agreement on every complete interior.
No conclusion about the all-depth mixed-record problem is drawn.
"""
from rule30_SS_record_residence import decode

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
CASES = (
    ('S', '111100000000', '110100', 0x688eb74a45efb082671ee, 84, 5, 6),
    ('L', '111000000000', '1101000100',
     0x35409b1caa645d715104db5291a2fe8415260ce, 155, 4, 7),
)


def main():
    for name, source, h, ring, period, d, length in CASES:
        right = tuple(map(int, source))
        r = right
        v = []
        for t in range(11):
            v.append(r[0])
            rr = (t % 2,)+r
            r = tuple(TABLE[4*rr[i-1]+2*rr[i]+rr[i+1]]
                      for i in range(1, len(rr)-1))
        assert v == [int(h[t % len(h)]) for t in range(11)]
        left, _ = decode(tuple(v), 0)
        assert left == [(ring >> ((-k) % period)) & 1 for k in range(11)]
        assert right[d-1:d+length-1] == (0,)*length
        target = left[d:d+length]
        assert len(target) == length and any(target)
        # Explicit finite full row. The interior complete cone remains
        # independent of the padded boundary for all eleven samples.
        lo, hi = -24, 30
        row = tuple(left[-i] if -10 <= i <= 0 else
                    right[i-1] if 1 <= i <= 12 else 0
                    for i in range(lo, hi+1))
        packed = sum(bit << j for j, bit in enumerate(row))
        mask = (1 << len(row))-1
        for t in range(11):
            assert row[-lo] == t % 2 and row[1-lo] == v[t]
            assert all(row[j] == ((packed >> j) & 1)
                       for j in range(t, len(row)-t))
            padded = (0,)+row+(0,)
            row = tuple(TABLE[4*padded[j]+2*padded[j+1]+padded[j+2]]
                        for j in range(len(row)))
            packed = ((packed << 1) ^ (packed | (packed >> 1))) & mask
        print(name, 'trace='+''.join(map(str, v)),
              'left_depths_0_to_10='+''.join(map(str, left)),
              'left_target='+''.join(map(str, target)),
              'right_target='+'0'*length, 'unclamped=PASS')
    print('ALL ORIENTATION CONTROLS PASS')


if __name__ == '__main__':
    main()
