#!/usr/bin/env python3
"""GC1023 / CL190: endpoint-aware train boundary argument.

Predictions registered in RULE30-GPT.md before the bounded seed search.
OUTCOME: seed239 (11110111, site1 first) realizes10010101010;
this refutes unqualified entrance (N) at n4. Short forbidden-word
containments prove exit4,5 and the corrected noninitial entrance rule,
inheriting the verified RLK absences rather than re-solving membership.
Independent shrinking-cone replay, ring and endpoint controls below.
"""
F = ('11', '00000', '101001', '0100101', '0101010000',
     '0101000101', '01010001001', '010100010001')


def gapword(gs):
    return '1' + ''.join('0' * (g-1) + '1' for g in gs)


def literal(seed, steps):
    row = [(seed >> i) & 1 for i in range(steps+1)]
    out = []
    for t in range(steps+1):
        out.append(row[0])
        p = [t % 2] + row
        row = [(30 >> (4*p[i]+2*p[i+1]+p[i+2])) & 1
               for i in range(len(row)-1)]
    return out


def main():
    row, packed = 239, []
    for t in range(21):
        packed.append(row & 1)
        row = ((row << 1) | (t % 2)) ^ (row | (row >> 1))
    assert packed == literal(239, 20)
    visible = ''.join(map(str, packed[::2]))
    assert visible == '10010101010' and visible[3:] == '10'*4
    assert all(f not in visible for f in F)
    assert '0100101' in '0' + visible  # Unexpected: the initial endpoint matters.
    # All possible first non-2 gaps: >=6 already contain five zeros.
    for g in (1, 3, 4, 5, 6):
        w = gapword((2, 2, 2, g))
        assert any(f in w for f in F) == (g != 4)
    for h in range(1, 7):
        w = gapword((2, 2, 2, 4, h))
        assert any(f in w for f in F) == (h != 5)
    # Earlier one noninitial, hence preceded by zero (absence of11).
    for g in range(1, 7):
        w = '0' + gapword((g, 2, 2, 2)) + '0'
        assert any(f in w for f in F) == (g not in (2, 4, 5))
    ring = ('0100110', '1111101', '0000001', '1000011')
    for t in range(4):
        r = list(map(int, ring[t]))
        nxt = [r[(i-1)%7] ^ (r[i] | r[(i+1)%7]) for i in range(7)]
        assert ''.join(map(str, nxt)) == ring[(t+1)%4]
    assert ''.join(ring[t%4][1] for t in range(0, 32, 2)) == '10'*8
    print('PASS: seed239 ->', visible, '; exit4,5; noninitial entrance4/5; ring control')


if __name__ == '__main__':
    main()
