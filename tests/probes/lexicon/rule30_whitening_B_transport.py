"""GC1147: does the whitening transition protect the next B exit?

Missing inference: after GC1146 rejects two named relaxed paths,
can a last-black SS past supply the lost B guard through whitening?
Record searched: black.SS|last.black|whiten AND
two.SS|second.SS|SS2|bad.B|unguarded.B ->17 hits9 files.
GC1056,1089,1099,1142,1145,1146 read. The known generic white-SS
bad-B sources do not settle the joint black-SS/white-SS history.
P1 BEFORE run: every realized black-SS -> white-SS -> B history
has guarded B. Stop at the first actual counter; if none, exhaust
only the complete24-cell causal cones of this two-short lemma.
No longer SS word, strip graph, H lift, inverse or solver run.
Counterfactual: a whitening past alone loses the admission guard.
Retain an actual counter cylinder rather than a free-boundary path.
Independent controls: packed shrinking-cone discovery followed by
literal/packed full histories and fresh-right induction for every
step of the retained cylinder; both fifth tracks must be realized.
Unexpected: a black source whose FIRST SS exits bad B is excluded
from P1's domain. Check the intermediate SS gate explicitly, even
when the prescribed fifth track happens to be111010 twice.
P2 BEFORE transport extraction: the whitening counter, if present,
still has time1 sites6..9=0000, the known local whitening packet.
Thus that packet cannot by itself supply an invariant B guard.
The original676 A/H class and all-depth R_real stay OPEN.
REFUTED-BY: any realized black-SS/white-SS counter cylinder.
ADDENDUM before corrected control replay: the first invocation
found a counter and passed all128 complete controls, then failed
the auxiliary first-short control: its copied source111011111110010000
was mistyped. GC1142 records111011111111010000; use that exact source.
No discovery verdict depends on the mistyped control.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_001000_mixed_admission import certificate

SS = bits('111010')
BLACK = ('111011101', '111011110', '111011111')
WHITE = {bits(p) for p in
         ('111010000', '111010100', '111010101', '111010110', '111010111')}
BAD = bits('111010011001')


def pack(row):
    return sum(b << j for j, b in enumerate(row))


def unpack(x, n):
    return tuple((x >> j) & 1 for j in range(n))


def packed_rows(src):
    n = len(src)
    x = pack(src)
    out = [src]
    for t in range(12):
        n -= 1
        x = (((x << 1) | (t & 1)) ^ (x | (x >> 1))) & ((1 << n)-1)
        out.append(unpack(x, n))
    return out


def main():
    witness = None
    tested = 0
    for pre in BLACK:
        # 12 output cells at tick12 have exactly this24-cell cone.
        for tail in product((0, 1), repeat=15):
            src = bits(pre) + tail
            r = packed_rows(src)
            tested += 1
            if r[6][:9] not in WHITE or r[12][:12] != BAD:
                continue
            assert tuple(y[4] for y in r[:12]) == SS + SS
            witness = src
            break
        if witness is not None:
            break
    print('tested_before_stop', tested, 'P1',
          'REFUTED' if witness else 'HELD on complete cones', flush=True)
    if witness is None:
        assert tested == 3*(1 << 15)
        print('two_short_guard_finite_cone_certificate; all_depth_OPEN')
        return
    cert = certificate(witness, 12)
    assert cert[6][:9] in WHITE and cert[12][:12] == BAD
    assert cert[0][5] == 1 and cert[6][5] == cert[12][5] == 0
    assert tuple(y[4] for y in cert[:12]) == SS + SS
    assert cert[1][5:9] == bits('0000')
    controls = 0
    for tail in product((0, 1), repeat=5):
        for pattern in ((0,), (1,), (0, 1), (1, 0)):
            src = witness + tail
            far = tuple(pattern[j % len(pattern)] for j in range(80-len(src)))
            full = run(src + far, 12)
            assert all(full[t][:len(y)] == y for t, y in enumerate(cert))
            assert full[6][:9] in WHITE and full[12][:12] == BAD
            assert tuple(y[4] for y in full[:12]) == SS + SS
            controls += 1
    # A first-short bad-B source from GC1142 is NOT in this domain.
    first_bad = bits('111011111111010000')
    first = run(first_bad + (0,)*30, 12)
    assert first[6][:12] == BAD and first[6][:9] not in WHITE
    # Established fresh white-SS negative calibrates the B predicate.
    fresh = run(bits('11101' + '0000000000010') + (0,)*30, 6)
    assert fresh[6][:12] == BAD
    fmt = lambda r: ''.join(map(str, r))
    print('actual_source24', fmt(witness),
          'white_SS6', fmt(cert[6]), 'bad_B12', fmt(cert[12]),
          'time1_whitening_packet', fmt(cert[1][5:9]),
          'full80_controls', controls, 'causal_induction_PASS',
          'intermediate_gate_negative_PASS', 'H_A_lift_NOT_ASSERTED',
          'original676_and_all_depth_OPEN', flush=True)


if __name__ == '__main__':
    main()

# OUTCOME: P1 REFUTED; discovery stopped after49217 source24 cones.
# Source111011110100000001000000 has realized SS/SS, white SS
# prefix111010110 at6 and badB111010011001 at12, for EVERY exterior.
# P2 HELD: time1sites6..9=0000. Fresh-right induction and128 full80
# literal/packed controls pass. The mistyped auxiliary control is
# retained above; corrected first-short negative and fresh-white
# negative pass. This source's black prefix111011110 is excluded
# from the immediate H111 image by reviewed CL336; no H/A lift
# is asserted. Close only the whitening-past-only B transport.
# Original676 admission, other invariants and all-depth R_real OPEN.
