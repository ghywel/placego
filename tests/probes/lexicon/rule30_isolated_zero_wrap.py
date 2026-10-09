#!/usr/bin/env python3
"""rule30_isolated_zero_wrap.py: WT, the finite wrap certificate that GPT's GC806 needs for the black-end walls 0 1^q
at every q >= 17, built independently (no third-party code). Local's run (chat L430), with these predictions pushed
before it.

RUN-ON:     cpu (Python 3, standard library); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_isolated_zero_wrap.py

GC806's argument, in the strip of positions -6 .. 6 with free outer cells (rule30_isolated_zero_strip.py's relaxation):
column 0 reads 0 1^q, phase 0 being the 0. (a) Ten 1-ticks force columns +1, +2 to 01 within nine updates, and 01 then
stays. (b) Seven 1-ticks force columns -6 .. 0 to 1010101, so for q >= 17 every phase 11 .. q - 6 row lies in C, the 14
rows 101010101 + s with the suffix s (columns +3 .. +6) not 1100 or 1101. (c) The last 1-row (phase q) has column -1 = 1
and columns +1, +2 = 01, so its nine-bit prefix (columns -6 .. +2) is one of 32 words h + 1101. The wrap table: from
each of the 32 x 16 rows at phase q, follow every strip path through phase 0 (centre 0) and phases 1 .. 11 (centre 1),
with every outer input, and ask which rows can be in C at phase 11. If only prefixes whose column -2 is 0 can (GC806:
only 110001101), then column -1 is 1 at every phase 0, and column -1 is periodic with period q + 1 along every infinite
strip path for every q >= 17; with column 0, Jen's theorem with a clock (PROOFS.md entry 5) excludes the wall.

PREDICTIONS (Local's, published before the run):
  WT-C1 (control, GC806's truth table): every one of the 32 x 512 five-cell / nine-step boundary paths reaches the pair
        01 at columns +1, +2 within nine updates of centre 1, and some path needs exactly nine.
  WT-C2 (control, against SG): for q = 17 .. 24, every vertex of the single cyclic component at phases 11 .. q - 6 lies
        in C, and its column -1 at phase 0 is 1.
  WT-P1 (blind, confidence 0.8; GC806 reports the source checker's answer, not replayed by GPT): of the 32 prefixes,
        exactly 110001101 can reach C at phase 11.
  WT-P2 (blind, confidence 0.85): every prefix that can reach C has column -2 = 0 (the bit the argument needs).
  Counterfactual: a second prefix with column -2 = 1 reaching C would leave column -1 at phase 0 free, and the uniform
  argument would need more than this table.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_isolated_zero_strip as sg                               # noqa: E402

W, CENTRE = 13, 6


def bit(r, pos):
    return (r >> (pos + 6)) & 1


def prefix(r):
    return ''.join(str(bit(r, p)) for p in range(-6, 3))


def suffix(r):
    return ''.join(str(bit(r, p)) for p in range(3, 7))


def in_c(r):
    return prefix(r) == '101010101' and suffix(r) not in ('1100', '1101')


def step(rows, centre):
    out = set()
    for r in rows:
        base = sg.INNER[r]
        if ((base >> CENTRE) & 1) != centre:
            continue
        for outer in range(4):
            out.add(base | (outer & 1) | ((outer >> 1) << (W - 1)))
    return out


def lemma_table():
    """GC806's truth table: columns +1 .. +5 = b .. f, z the free +6 input, centre held at 1"""
    worst = 0
    for s in range(32):
        for zs in range(512):
            b, c, d, e, f = [(s >> k) & 1 for k in range(5)]
            n = 0
            while not (b == 0 and c == 1):
                if n == 9:
                    return None
                z = (zs >> n) & 1
                b, c, d, e, f = 1 ^ (b | c), b ^ (c | d), c ^ (d | e), d ^ (e | f), e ^ (f | z)
                n += 1
            worst = max(worst, n)
    return worst


def main():
    worst = lemma_table()
    print('WT-C1', 'PASS' if worst == 9 else 'FAIL', '(worst %s updates)' % worst)
    c2 = True
    for q in range(17, 25):
        verts, succ = sg.graph(q)
        comps = [c for c in sg.sccs(len(verts), succ) if len(c) > 1]
        assert len(comps) == 1
        for v in comps[0]:
            r, ph = verts[v]
            if 11 <= ph <= q - 6 and not in_c(r):
                c2 = False
            if ph == 0 and bit(r, -1) != 1:
                c2 = False
    print('WT-C2', 'PASS' if c2 else 'FAIL')
    reach = {}
    for h in range(32):
        pre = format(h, '05b') + '1101'
        for s in range(16):
            row = 0
            for k, ch in enumerate(pre + format(s, '04b')):
                row |= int(ch) << k                                  # character k is position k - 6
            assert prefix(row) == pre
            rows = {row}
            rows = step(rows, 0)                                      # phase q -> 0
            for _ in range(11):                                       # phases 1 .. 11
                rows = step(rows, 1)
            if any(in_c(r) for r in rows):
                reach.setdefault(pre, []).append(format(s, '04b'))
    for pre in sorted(reach):
        print('prefix %s (column -2 = %s) reaches C from suffixes %s' % (pre, pre[4], ' '.join(reach[pre])))
    print('WT-P1', 'HELD' if list(reach) == ['110001101'] else 'REFUTED (%s)' % sorted(reach))
    print('WT-P2', 'HELD' if reach and all(p[4] == '0' for p in reach) else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
