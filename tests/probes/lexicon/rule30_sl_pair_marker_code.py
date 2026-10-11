"""GC1117: a visible pair marker in the already derived left22 even field.

Missing inference: GC1116's pending odd-phase branch need not be a
loss of renewal information. Does its even field carry a locally
recognizable reset, including arbitrarily long S trains? Derive the
named column22 output; no new depth sweep or canonical return test.
Record searched: left.?22|column.?22|GC1116|paired.?L with marker|00|
recod|inverse|renewal ->11 hits6 files (GC1116 and adjacent inverses).
Second search with13.*(past|sample)|0111110111010110|pair.*00|
00.*pair|unbounded.*short ->2 unrelated hits (board and wake).
P1 BEFORE controls: for paired L's separated by at least2 S gaps,
c_u=x_-22(2u-14) codes first-L intervals by C_k=C_1(110)^(k-1),
C_1=0111110111010110, k>=1. First L's are EXACTLY the second
zero of00; eta_r=(1-c_(r-1))(1-c_r). This is an all-length identity.
P2: q has a13-sample PAST inverse even without a maximum S-run:
if eta occurs within the past12 positions, its age is0,5 or10
exactly when q=1; otherwise q_u=1-c_(u-1). The image's110 tail
carries the short-marker phase; a bounded last-L age is unnecessary.
Counterfactual: like left20, pure-S phases collapse at22. Must fail.
Independent controls: original physical h macro spellings, literal
Rule30 truth-table forcing, reset/decoder code that uses only c.
Unexpected check: all3 pure-S phases, and very long paired-L spacing,
must retain phase despite no recent00. Also retain k=0 as an identified
outside-premise check; no result there is assumed in the proof.
OUTCOME: P1/P2 HELD,1782 literal phase samples,738 with no pair
marker in the last12 positions. All3 pure-S phases recover correctly;
collapse counterfactual REFUTED. Outside k=0 control also decodes,
an unexpected positive control; no extension of the proved guard is
inferred. First guarded target38 uses observations0..24.
No CA membership, Local solver work, record bound or all-depth closure.
"""
from itertools import product
import rule30_sl_age_spatial_interface as prior


BASE = '0111110111010110'


def source(ks):
    q = []
    first = []
    r = 0
    for k in ks:
        letters = 'SLL' + 'S' * k
        h = ''.join('110100' if a == 'S' else '1101000100' for a in letters)
        q.extend(map(int, h[::2]))
        first.append(r + 3)
        r += len(h) // 2
    return q, first


def forced(q):
    n = len(q)
    return [prior.literal(tuple(q[(u - 7 + i) % n] for i in range(12)))[22][0]
            for u in range(n)]


def eta(c):
    return [int(not c[(r - 1) % len(c)] and not c[r]) for r in range(len(c))]


def decode(c):
    marks = eta(c)
    n = len(c)
    out = []
    for u in range(n):
        near = [j for j in range(12) if marks[(u - j) % n]]
        assert len(near) <= 1
        out.append(int(near[0] in (0, 5, 10)) if near else 1 - c[(u - 1) % n])
    return out


def main():
    checks = long_tail = 0
    for ks in list(product((1, 2, 3), repeat=3)) + [(1, 19, 2), (31, 1, 1)]:
        q, starts = source(ks)
        c = forced(q)
        expected = [0] * len(q)
        expected_c = [None] * len(q)
        for r, k in zip(starts, ks):
            expected[r] = 1
            word = BASE + '110' * (k - 1)
            for i, bit in enumerate(word):
                pos = (r + i) % len(q)
                assert expected_c[pos] is None
                expected_c[pos] = int(bit)
        assert c == expected_c
        assert eta(c) == expected and decode(c) == q
        checks += len(q)
        long_tail += sum(not any(eta(c)[(u - j) % len(q)] for j in range(12))
                         for u in range(len(q)))
    pure = []
    for phase in range(3):
        q = [int((u + phase) % 3 == 0) for u in range(18)]
        c = forced(q)
        assert not any(eta(c)) and decode(c) == q
        pure.append(tuple(c))
    assert len(set(pure)) == 3
    outside, _ = source((0, 0, 0))
    c0 = forced(outside)
    try:
        outside_decoder = decode(c0) == outside
    except AssertionError:
        outside_decoder = False
    assert 2 * (19 - 12) - 14 == 0 and 2 * 19 - 14 == 24 < 38
    print(dict(P1='HELD', P2='HELD', literal_samples=checks,
               no_recent_pair_samples=long_tail, pure_S_phases=3,
               collapse_counterfactual='REFUTED', outside_k0_decoder=outside_decoder,
               inverse_past_samples=13, first_target_time=38,
               last_observation_time=24, all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
