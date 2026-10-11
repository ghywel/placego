"""GC1154: indexed RRL repeat comparators, including untyped words.

Missing inference: turn the already proved Theorem B into a finite
white-time root constraint without canonical S/L lifts or saved rings.
Record searched: periodic|period|4q|4m with query.condition|indexed|
terminal_drop|initial.*interval|record.condition|repeat.*cut
->73 hits27files; GC970/971/974/976, GC709/1148/49/51/53,
PROOFS entry6 and RULE30-PRIZE8.54 read. B itself is reused.
P1 BEFORE controls: for initial left zeros[d,d+L-1], white anchor
a=phase+2s and m>=1 with L>=2a+4m-1, forbid period m in the
C=ceil((d+a+4m-2)/2) white-time bits beginning at s.
Equivalently require some q[s+j]!=q[s+j-m], m<=j<C.
P2: its last used physical bit a+2(C-1) is <=d+L-2; the final
RRL pair's unused right bit never enters the comparator.
Independent: literal-table left decoder versus the first-LEFT-column
identity (white:1-q, black:1), and late-row comparison with the
infinite periodic reference restricted to the observed cone.
Counterfactual: periodic WHITE-time samples require periodic odd
RIGHT samples for the same left row. Vary all odd samples using
three different patterns; left reconstruction must remain identical.
Unexpected: flip the UNUSED last right bit in every control, retain
odd initial wall phases and both parities of the last needed depth.
Only templates10,1000,10010000, d=1,2,7,12, a=0..3, arbitrary
pre-anchor prefixes; no solver, language membership, record maximum,
finite-automaton census, hidden closure or period-length sweep.
REFUTED-BY: a complete target zero interval on these samples, a
reference mismatch, or an endpoint beyond the RRL tested horizon.
OUTCOME 2026-10-11 15:09 UTC: P1/P2 PASS.1080 complete inverse
controls, including720 odd anchors and540 odd final depths; three
odd-right patterns and both unused-terminal values give identical
initial rows.17160 indexed specifications (7920 odd-phase) and24
large-integer endpoint controls PASS. Theorem B supplies the all-depth
argument; no all-depth bound on R_real or hidden closure is inferred.
"""
from itertools import product
from rule30_SS_record_residence import decode


def specifications(d, length, phase):
    """(white index s, period m, tested visible length C, anchor a).

    Each item forbids ALL period-m words, represented by comparators
    rather than enumerating their 2**m possible period blocks.
    The record query and its initial wall phase are premises.
    """
    assert d >= 1 and length >= 1 and phase in (0, 1)
    out = []
    for a in range(phase, max(0, (length-3)//2+1), 2):
        for m in range(1, (length-2*a+1)//4+1):
            k = d+a+4*m-2
            out.append(((a-phase)//2, m, (k+1)//2, a))
    return out


def violates(q, s, m, count):
    assert count > m and len(q) >= s+count
    return all(q[s+j] == q[s+j-m] for j in range(m, count))


def main():
    controls = odd = parity = 0
    for block in ('10', '1000', '10010000'):
        m = len(block)
        for a in range(4):
            phase = a % 2
            for d in (1, 2, 7, 12):
                length = 2*a+4*m-1
                k = d+a+4*m-2
                horizon = d+length
                ref_v = tuple(int(block[t//2 % m]) if t % 2 == 0 else 1
                              for t in range(k+1))
                reference, _ = decode(ref_v, 0)
                for pre in product((0, 1), repeat=a):
                    fixed = None
                    for mode in range(3):
                        for terminal in (0, 1):
                            v = pre+tuple(int(block[t//2 % m]) if t % 2 == 0
                                         else (0, 1, (t//2) % 2)[mode]
                                         for t in range(horizon-a))
                            v = v[:-1]+(terminal,)
                            row, cols = decode(v, phase)
                            assert all(cols[-j][a] == reference[j]
                                       for j in range(1, k+1))
                            assert len(row[d:]) == length and any(row[d:])
                            if fixed is None:
                                fixed = row
                            else:
                                assert row == fixed
                            # First left column is independent of odd right bits.
                            for t in range(horizon-1):
                                assert cols[-1][t] == (1-v[t] if (phase+t) % 2 == 0 else 1)
                            s, mm, count, aa = next(z for z in specifications(d, length, phase)
                                                  if z[1] == m and z[3] == a)
                            visible = ''.join(str(v[t]) for t in range(phase, horizon-1, 2))
                            assert violates(visible, s, mm, count)
                            controls += 1
                            odd += phase
                            parity += k % 2
    indexed = odd_indexed = 0
    for d in range(1, 13):
        for length in range(1, 41):
            for phase in (0, 1):
                for s, m, count, a in specifications(d, length, phase):
                    k = d+a+4*m-2
                    assert length >= 2*a+4*m-1
                    assert 2*(count-1) < k <= 2*count
                    assert count > m
                    assert a == phase+2*s
                    assert a+2*(count-1) <= d+length-2
                    indexed += 1
                    odd_indexed += phase
    big = 0
    for d in (10**20+1, 10**30+2):
        for phase in (0, 1):
            for s, m, count, a in specifications(d, 13, phase):
                assert a+2*(count-1) <= d+11
                big += 1
    print('CONTROLS PASS', controls, 'odd anchors', odd, 'odd depths', parity)
    print('INDEXED SPECS PASS', indexed, 'odd phase', odd_indexed,
          'large-integer specs', big)


if __name__ == '__main__':
    main()
