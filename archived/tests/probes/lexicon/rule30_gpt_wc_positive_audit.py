#!/usr/bin/env python3
"""GC881: replay only Local L499's fourteen named width-eight positive walls.
RUN-ON: cpu, Python3; COMMAND: python3 tests/probes/lexicon/rule30_gpt_wc_positive_audit.py
Predictions in CLOUD-LOCAL before execution: all14 named walls determine every
phase; slow-wall rotations and doubled period give corresponding output words.
Unexpected controls: 01 and white-end q9 remain non-determined. Failure of
this sufficient test is not a realizability certificate. No necklace census,
widening, SAT, randomness or peer code; uses GPT's literal-rule relation.
OUTCOME: all14 positives PASS; all10 slow-wall rotations and doubled period
PASS. Non-determined controls: 01 -> **; 0000000001 -> 0*11111111.
Only the named positive certificates are replayed, not census completeness.
"""
from rule30_gpt_white_end_audit import ALL, N, REL, bits, image

WORDS = (
    '0011111111',
    '00000000001', '00000000011',
    '000000000001', '000000000011',
    '0000000000001', '0000000000011', '0000000001011',
    '00000000000001', '00000000000011', '00000000001011',
    '00000000010011', '00000000010111', '00000000011011',
)


def audit(word):
    S, strict = ALL, 0
    while True:
        T = S
        for w in word:
            T = image(T, REL[int(w)])
        assert not T & ~S
        if T == S:
            break
        S = T
        strict += 1
        assert strict <= N
    T, col = S, ''
    for w in word:
        v = {(s >> 7) & 1 for s in bits(T)}
        assert v
        col += str(next(iter(v))) if len(v) == 1 else '*'
        T = image(T, REL[int(w)])
    assert T == S
    return col, S.bit_count(), strict


def main():
    assert len(set(WORDS)) == 14
    for w in WORDS:
        rots = {w[i:] + w[:i] for i in range(len(w))}
        assert w == min(rots) and len(rots) == len(w)
        col, size, strict = audit(w)
        assert '*' not in col, (w, col)
        print(w, col, size, strict)
    w = WORDS[0]
    col = audit(w)[0]
    assert col == '0110000000'
    for i in range(len(w)):
        assert audit(w[i:] + w[:i])[0] == col[i:] + col[:i]
    assert audit(w * 2)[0] == col * 2
    assert '*' in audit('01')[0]
    assert '*' in audit('0' * 9 + '1')[0]
    print('PASS: all14 positives;10 slow-wall rotations; doubled-period control')
    print('unexpected non-determined controls:', audit('01')[0], audit('0' * 9 + '1')[0])


if __name__ == '__main__':
    main()
