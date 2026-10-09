#!/usr/bin/env python3
"""GC880: bounded independent certificate audit of Local L498, width eight only.
Predictions recorded in CLOUD-LOCAL before execution: W^22=W^26; singleton
phase words 1001^(q-2) for q10..29; stable sizes31/21/7 at q10/12/20.
Counterfactual: macro equality alone certifies every inserted phase (it does not).
Independent control: literal rule-number table against the Boolean formula.
Unexpected controls: q9 is not determined, and report actual stabilization
iterations instead of assuming the peer's fixed loop cap reaches a fixed point.
RUN-ON: cpu (standard Python3); COMMAND: python3 tests/probes/lexicon/rule30_gpt_white_end_audit.py
No SAT, widening, random experiment or external data; output is exact integers.
OUTCOME (2026-10-09 22:35 BST): all assertions PASS. W22=W26 and W21!=W25;
q10..29 have exact word1001^(q-2), sizes31/21/7 as predicted; q9 has10*1111111.
Every q10..29 stabilizes after2 or3 strict macro images, below the peer cap200.
Whole-relation equality plus the hand phase argument in GC880 covers all q>=10.
"""
K = 8
N = 1 << K
ALL = (1 << N) - 1


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def step(s, wall, outside):
    out = 0
    for j in range(K):
        a = wall if j == 0 else (s >> (K - j)) & 1
        b = (s >> (K - 1 - j)) & 1
        c = outside if j == K - 1 else (s >> (K - 2 - j)) & 1
        out = (out << 1) | ((30 >> (4 * a + 2 * b + c)) & 1)
    return out


REL = [[(1 << step(s, wall, 0)) | (1 << step(s, wall, 1))
        for s in range(N)] for wall in (0, 1)]


def image(S, relation):
    out = 0
    for s in bits(S):
        out |= relation[s]
    return out


def main():
    assert all(((30 >> (4*a + 2*b + c)) & 1) == (a ^ (b | c))
               for a in (0, 1) for b in (0, 1) for c in (0, 1))
    powers = [[1 << s for s in range(N)]]
    for _ in range(29):
        powers.append([image(S, REL[0]) for S in powers[-1]])
    assert powers[22] == powers[26]
    assert powers[21] != powers[25]
    sizes, steps, profiles = {}, {}, {}
    for q in range(9, 30):
        macro = [image(REL[1][s], powers[q]) for s in range(N)]
        S = ALL
        count = 0
        while True:
            T = image(S, macro)
            assert T & ~S == 0
            if T == S:
                break
            S = T
            count += 1
            assert count <= N
        T, word = S, ''
        for wall in [1] + [0] * q:
            vals = {(s >> (K-1)) & 1 for s in bits(T)}
            assert vals
            word += str(next(iter(vals))) if len(vals) == 1 else '*'
            T = image(T, REL[wall])
        assert T == S
        sizes[q], steps[q], profiles[q] = S.bit_count(), count, word
        if q >= 10:
            assert word == '100' + '1' * (q-2)
    assert '*' in profiles[9]
    assert [sizes[q] for q in (10, 12, 20)] == [31, 21, 7]
    print('PASS: literal Rule30 table; whole W22=W26; W21!=W25')
    print('PASS: q10..29 exact phase words; stable sizes q10/12/20 = 31/21/7')
    print('unexpected q9:', profiles[9])
    print('stabilization strict images:', steps)
    print('uniform representatives q26..29:', {q: profiles[q] for q in range(26, 30)})


if __name__ == '__main__':
    main()
