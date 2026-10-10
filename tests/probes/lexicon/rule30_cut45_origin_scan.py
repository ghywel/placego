"""GC1040: does a spatial reset explain the two surviving joint origins?

Missing inference: GC1039's joint relation succeeds, but its origin memory
has no small structural explanation. Test the existing G13 inverse-row
scanner on its TWO surviving origins, not on new widths or time windows.
Record searched: (preimage|parent|backward) + (0101|1010|reset) -> G13's
complete reset language; GC1010/1012's different, two-update source scanner.
G13 read; no new reset theorem or actual-language membership query.
P1 (0.6): both origins have a spatial reset that isolates their left prefix.
P2 (0.5): after imposing the time29 wall, both origins have the SAME parent
prefix through site20; the clock may resolve a nonreset scanner branch.
Counterfactual: failure of P1 does not refute correlated pin forcing, which
GC1039 already computes. A common parent prefix would not propagate forever.
Controls: independent literal forward reconstruction of every admitted
parent; exclude every other parent among the four terminal pair choices.
Unexpected check: retain both site24 choices separately, including the one
with no spatial reset, rather than combining their unary marginals.
Bound: two children, four right terminal pairs each, ONE reverse tick.
No SAT, repeated membership query, pin deletion or window enlargement.
OUTCOME: P1 REFUTED, P2 HELD. The site24=0 origin has scanner rank1;
site24=1 has rank2. Both nevertheless fix the same first21 parent bits:
000011010000111111111. A reset is NOT needed: the time29 wall selects
the black plateau through a thirteen-symbol prefix transfer.
Adaptive hand claim, BEFORE its controls: for child prefix
1(0011)^m 0^r, r>=2, a parent with wall b has constant sites
4m+1..4m+r of value c=1 XOR b XOR (m mod2). Reading each0011
block backwards swaps00 and11. Its parent block is0000 for incoming11,
1101 for incoming00. Controls below test m0..6,r2..9 and all four
terminal pairs. Countercontrol prediction: r=1 need not obey the formula.
RETAINED FAILURE: that countercontrol produced NO counterexample; its
assertion failed after the224 positive controls passed. Direct algebra
then shows one zero already restricts the entering pair to00,10,11,
on which0011 has the claimed parent block. The correct claim is r>=1.
Before corrected controls: use r=0 instead; entering01 is then allowed
and gives parent block1110 rather than1101. This must be a literal
counterexample, not just a speculative failure of the proof.
This parametric identity explains one origin-past correlation, not
GC1039's pin forcing or an all-depth record ceiling.
"""

from rule30_cut45_origin_past import parents, literal


def scan(word, pair):
    history = []
    c, r = pair
    for y in reversed(word):
        history.append((c, r))
        c, r = int(y) ^ (c | r), c
    return (c, r), history


def main():
    reports = []
    for last in '01':
        word = '10011001100110000000001' + last
        child = sum(int(c) << i for i, c in enumerate(word))
        endpoints = set()
        direct = set()
        for c in (0, 1):
            for r in (0, 1):
                end, history = scan(word, (c, r))
                endpoints.add(end)
                row = sum(pair[0] << (23 - i) for i, pair in enumerate(history))
                assert literal(row, end[0], r, 24) == child
                if end[0] == 1:   # actual time29 wall
                    direct.add((row, r))
        assert direct == set(parents(child, 1, 24)) and direct
        rows = [''.join(str((row >> i) & 1) for i in range(24))
                for row, _ in sorted(direct)]
        common = ''.join(rows[0][i] if all(s[i] == rows[0][i] for s in rows)
                         else '?' for i in range(24))
        reports.append((endpoints, rows, common))
        print('origin24', last, 'scanner_image', sorted(endpoints),
              'parents', rows, 'common', common)
    p1 = all(len(r[0]) == 1 for r in reports)
    prefixes = {s[:20] for _, rows, _ in reports for s in rows}
    p2 = len(prefixes) == 1
    print('P1', p1, 'P2', p2, 'literal controls PASS')
    cases = 0
    for m in range(7):
        for r in range(1, 10):
            word = '1' + '0011' * m + '0' * r
            width = len(word)
            child = sum(int(c) << i for i, c in enumerate(word))
            for right in ((0, 0), (0, 1), (1, 0), (1, 1)):
                end, history = scan(word, right)
                row = sum(pair[0] << (width - 1 - i)
                          for i, pair in enumerate(history))
                assert literal(row, end[0], right[1], width) == child
                c = 1 ^ end[0] ^ (m % 2)
                assert all(((row >> (i - 1)) & 1) == c
                           for i in range(4 * m + 1, 4 * m + r + 1))
                expected = [''] * m
                entering = c
                for j in range(m - 1, -1, -1):
                    expected[j] = '0000' if entering else '1101'
                    entering ^= 1
                bits = ''.join(str((row >> i) & 1) for i in range(width))
                assert bits[:4*m] == ''.join(expected)
                cases += 1
    bad = []
    for m in range(7):
        word = '1' + '0011' * m
        for right in ((0, 0), (0, 1), (1, 0), (1, 1)):
            end, history = scan(word, right)
            row = sum(pair[0] << (len(word) - 1 - i)
                      for i, pair in enumerate(history))
            c = 1 ^ end[0] ^ (m % 2)
            expected = [''] * m
            entering = c
            for j in range(m - 1, -1, -1):
                expected[j] = '0000' if entering else '1101'
                entering ^= 1
            bits = ''.join(str((row >> i) & 1) for i in range(len(word)))
            assert literal(row, end[0], right[1], len(word)) == sum(
                int(c) << i for i, c in enumerate(word))
            if bits[:4*m] != ''.join(expected):
                bad.append((m, right, end, bits))
    assert bad, 'r=0 must have a literal counterexample'
    print('parametric literal controls PASS', cases,
          'r=0 counterexample', bad[0])


if __name__ == '__main__':
    main()
