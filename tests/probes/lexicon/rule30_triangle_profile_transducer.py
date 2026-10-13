#!/usr/bin/env python3
"""Exact growing pair-word update between actual triangle paths (GC1208).

RUN-ON: cpu, standard-library Python; no solver, census or membership.
COMMAND: python3 tests/probes/lexicon/rule30_triangle_profile_transducer.py

Record searched: path|diagonal|profile with word.transducer|four.state|
sequential|carry.state|scan.*pair ->11 hits8files; transducer with
origin|zero.tail|finite.support ->5hits5files; transducer|pair.word|
pair.path|pair.profile with forward|two.tick|two.step|length.*grow|growing
->17hits7files. GC717, GC1203..1207, GC971's inverse transducer and
G236's spatial two-tick transducer read. None is this growing pair-path
update; the Rule30 local rule and fixed entry packet are credited.

PREDICTIONS before execution (2026-10-13):
 P1: on all16 four-cell inputs (C,B,A,H), T=(A XOR(B OR C),
     H XOR(A OR B)) matches two independent Wolfram30 updates. Each
     fixed input pair(C,B) permutes the four carry pairs(A,H).
 P2: d2/5/8,a0/1/4,both phases,two fixed tails (36 cases), scanning
     the old path after its head, starting with fixed head(1,1-e),
     then appending(1,C XOR B), exactly gives the next physical path.
     The input's actual terminal is retained even if its guard is0.
 P3: adjacent old pairs recover all holes; the carry supplies the
     outward source bit. The resulting sources equal literal quads.
     On the existing125 fixture, five updates a4..8 match the physical
     words and the M00011 middle parities already computed in GC1206.
 Independent: full physical paths from literal and packed Rule30;
     finite-state scanning uses only pair words, never an unseen cell.
 Unexpected sharp boundary: d5,p0,a1,k7, flipping initial k+3=10
     leaves the old word unchanged but flips the next head's partner.
     The fixed-head update must fail for that shortened white band.
 Counterfactual: replacing a failed black terminal10 by11 is harmless.
     Formal carry00 gives distinct outputs for10 and11 (not a real
     witness claim). Also invertible carry actions do not imply an
     invertible whole word map: inputs01 and11 have the same action.
 No assertion of four total persistent states: word length grows by1.

P4 ADDENDUM before execution: encode carry(A,H) as s=A+2H modulo4.
 Input00 acts by -s,10 by s+1, and01/11 by3-s. Check these on the
 same16 local inputs. These are the eight-element dihedral group's
 local carry actions; the whole growing-word update is not claimed
 affine, invertible or finite-state.

OUTCOME: all predictions pass:16 local inputs/dihedral coordinates, four
carry permutations,36 fixed paths (20 failed old guards), five existing
fixture updates, sharp horizon and false-repair controls. No scan added.
"""
import json
from itertools import product
from pathlib import Path
from rule30_zero_triangle_guard_transport import literal, packed, seed_for
from rule30_zero_triangle_adjacent_charge import cell, path


def step_letter(letter, carry):
    c, b = letter
    a, high = carry
    return a ^ (b | c), high ^ (a | b)


def advance(word, e):
    result = [(1, 1 - e)]
    for letter in word[1:]:
        result.append(step_letter(letter, result[-1]))
    c, b = result[-1]
    result.append((1, c ^ b))
    return result


def physical(rows, phase, d, a, e):
    k, crop = d + 2 * a + e, a + 1
    n = k - crop
    return [(cell(rows, phase, crop + u, n - u),
             cell(rows, phase, crop + u, n - u + 1)) for u in range(n + 1)]


def word_sources(word, next_word):
    holes, sources = [], []
    for u, (c, b) in enumerate(word[:-1]):
        h = (1 - c) * (1 - (b ^ word[u + 1][1]))
        holes.append(h)
        if u == 0:
            sources.append(0)       # fixed black head; GC1204's first source
        else:
            a = next_word[u - 1][0]
            sources.append((a * b) ^ (h * (a ^ b)))
    return holes, sources


def compare(rows, phase, d, a, e):
    old, nxt = physical(rows, phase, d, a, e), physical(rows, phase, d, a + 1, e)
    assert advance(old, e) == nxt
    assert word_sources(old, nxt) == path(rows, phase, d, a, e)
    assert len(nxt) == len(old) + 1 and nxt[-1][1] == (nxt[-2][0] ^ nxt[-2][1])
    return old, nxt


def main():
    for c, b, a, high in product((0, 1), repeat=4):
        expected = ((30 >> (4*a + 2*b + c)) & 1,
                    (30 >> (4*high + 2*a + b)) & 1)
        assert step_letter((c, b), (a, high)) == expected
        s = a + 2*high
        new = step_letter((c, b), (a, high))
        phase = ((3-s) if b else (s+1 if c else -s)) % 4
        assert new[0] + 2*new[1] == phase
    for letter in product((0, 1), repeat=2):
        assert len({step_letter(letter, state) for state in product((0, 1), repeat=2)}) == 4
    cases, failed_old = 0, 0
    for d, a, phase, tail in product((2, 5, 8), (0, 1, 4), (0, 1), (0, 1)):
        e = 1 ^ ((d + phase) % 2)
        k = d + 2*a + e
        seed = seed_for(d, k + 2, tail)
        rows = packed(seed, phase, k + 2, 2*k + 10)
        assert rows == literal(seed, phase, k + 2, 2*k + 10)
        old, _ = compare(rows, phase, d, a, e)
        failed_old += old[-1][1] == 0
        cases += 1
    d, phase, a, e = 5, 0, 1, 0
    base = seed_for(d, 9, 0)
    base[10] = 0
    changed = base.copy()
    changed[10] = 1
    rows0 = packed(base, phase, 9, 30)
    rows1 = literal(changed, phase, 9, 30)
    old0 = physical(rows0, phase, d, a, e)
    old1 = physical(rows1, phase, d, a, e)
    new0 = physical(rows0, phase, d, a+1, e)
    new1 = physical(rows1, phase, d, a+1, e)
    assert old0 == old1 and new0[0][0] == new1[0][0] == 1
    assert new0[0][1] ^ new1[0][1] == 1
    assert advance(old1, e) != new1 and advance(old0, e) == new0
    assert step_letter((1, 0), (0, 0)) != step_letter((1, 1), (0, 0))
    assert all(step_letter((0, 1), state) == step_letter((1, 1), state)
               for state in product((0, 1), repeat=2))
    root = Path(__file__).resolve().parents[3]
    f = next(r for r in json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
             if r['depth'] == 125 and r['phase'] == 1)
    seed = {j: int(b) for j, b in enumerate(f['left'], 1)}
    rows = packed(seed, 1, 144, 290)
    assert rows == literal(seed, 1, 144, 290)
    bits = []
    for a in range(4, 9):
        old, nxt = compare(rows, 1, 125, a, 1)
        assert old[-1] == nxt[-1] == (1, 1)
        bits.append(sum(word_sources(old, nxt)[1][3:-5]) % 2)
    assert bits == [0, 0, 0, 1, 1]
    print('PASS:16 local inputs;4 carry permutations;%d fixed paths (%d failed old guards retained);'
          '5 fixture updates;sharp boundary and false-guard controls' % (cases, failed_old))


if __name__ == '__main__':
    main()
