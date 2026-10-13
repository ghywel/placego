#!/usr/bin/env python3
"""Bounded algebra controls for the physical middle-parity word (GC1207).

RUN-ON: cpu, standard-library Python. No CA evolution, solver or census.
COMMAND: python3 tests/probes/lexicon/rule30_middle_parity_decoder.py

Record searched: middle.parity|M_a|b XOR w with
decod|recover|two.block|anticip -> no hit, including active ledger fallback.
GC1204..1206 and G27.2 read. GC1205's R recoding is different: its decoder
needs an initial visible bit or an R1 anchor. Here two adjacent M suffice.

PREDICTIONS before execution (2026-10-13):
 D1: all eight no11 quadruples have b=M(v,b,w)*(1-M(b,w,z)).
 D2: the 64 six-bit truth inputs satisfying no11 give M words avoiding
     111 and0010; M0000 iff the five visible bits starting at its anchor
     are00000. Basic-cut inputs therefore also avoid M0000.
 D3: all16 four-bit M inputs obey the local reverse-consistency test:
     recoding D(m0,m1),D(m1,m2),D(m2,m3) returns m1 iff neither
     m1m2m3=111 nor m0m1m2m3=0010.
 Independent: direct XOR formula versus the two-case OR explanation;
     the accepted125 fixture's stored visible bits versus GC1206's
     already computed M00011. Initial fixture prediction0001 is retained
     below as a failed endpoint expectation. No CA replay.
 Unexpected endpoint control: visible quadruples0101 and0010 both
     start with M1 but have different b; one parity cannot decode b.
 Dropped-premise control: visible0110 has b1 but decoded0 without no11.
 Counterfactual: this lossless local recoding is a new information price.
     It is not: the fixed-boundary fibre size is at most four, and no
     origin-independent finite closure or all-depth bound is claimed.

OUTCOME: D1/D2/D3 pass (8/21/16 inputs). The fixture expectation0001
failed: M00011 recovers0000, with the visible1 beyond the last decoded
sample. Corrected endpoint expectation; all controls then pass. No
change to the decoder or experiment inputs.
"""
import json
from itertools import product
from pathlib import Path


def m(v, b, w):
    return b ^ w ^ (v * w)


def encode(q):
    return [m(*q[i - 1:i + 2]) for i in range(1, len(q) - 1)]


def decode(bits):
    return [a * (1 - b) for a, b in zip(bits, bits[1:])]


def no11(q):
    return all(not (a and b) for a, b in zip(q, q[1:]))


def main():
    quads = sixes = 0
    for v, b, w, z in product((0, 1), repeat=4):
        if no11((v, b, w, z)):
            first, second = m(v, b, w), m(b, w, z)
            assert first == (b | (w * (1 - v)))
            assert first * (1 - second) == b
            quads += 1
    for q in product((0, 1), repeat=6):
        if not no11(q):
            continue
        bits = encode(q)
        s = ''.join(map(str, bits))
        assert '111' not in s and s != '0010'
        assert (s == '0000') == (q[1:] == (0,) * 5)
        assert decode(bits) == list(q[1:-2])
        sixes += 1
    for bits in product((0, 1), repeat=4):
        q = decode(bits)
        bad = bits[1:] == (1, 1, 1) or bits == (0, 0, 1, 0)
        assert (m(*q) == bits[1]) == (not bad)
    assert m(0, 1, 0) == m(0, 0, 1) == 1
    assert decode(encode((0, 1, 0, 1)))[0] == 1
    assert decode(encode((0, 0, 1, 0)))[0] == 0
    assert decode(encode((0, 1, 1, 0)))[0] == 0  # differs from b=1
    root = Path(__file__).resolve().parents[3]
    records = json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
    f = next(r for r in records if r['depth'] == 125 and r['phase'] == 1)
    q = tuple(int(f['visible'][(t - 1) // 2]) for t in range(131, 144, 2))
    assert len(q) == 7 and encode(q) == [0, 0, 0, 1, 1]
    assert decode(encode(q)) == list(q[1:-2]) == [0, 0, 0, 0]
    print('PASS: %d no11 quadruples; %d no11 six-bit inputs; 16 reverse inputs; '
          'fixed125 algebra and both negative controls' % (quads, sixes))


if __name__ == '__main__':
    main()
