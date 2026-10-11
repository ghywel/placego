"""GC1096: a black-A restart packet needs more than its equal pair.

Missing inference: actual black-SS toA to00100 to101 must bar anotherA.
Record searched: black.eleventh|00011111 with101|guard|restart ->33
hits17files; GC1083/84/89/90/91 read. No solver or visible-language job.
P1 before run: blackA6..13=00011111 bars101-toA. REFUTED by SOURCE.
P2 adaptive: an actual blackSS prefix plus12 free cells and10 whites
can restart likewise. FAILED4096 constructions; no absence theorem.
P3: SOURCE has a six-step actualSS preimage. FAILED: no fourth parent.
Inverse control, before relying on P3: knownGC1091 source occurs among
632 six-step inverses of its24-cell image. PASS, each edge resimulated.
P4: obstruction ends by19cells. REFUTED: minimum named prefix is20.
P5: its20cells have no four-step clamped past at any even age>=4,
whereas its19-cell prefix has one. HELD by complete inverse tree and
seven-cell contradiction. This is a fixed packet proof, not record scan.
Counterfactual: equalA11=A13=1 alone supplies the core no-A guard.
The fresh all-tail SOURCE refutes it; actual ancestry excludes SOURCE.
Unexpected: whitenA13, keepingA11black; selected trajectory entersC
at16 rather than101. No necessity claimed; no further census.
Independent controls: fresh-right causal shield and literal/packed
histories, backwards edges checked forward, known actual inverse.
Actual universal restart exclusion and all-depth bound remain OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import update, S, D

SOURCE = bits('111010001111100000111000000000')
FORBIDDEN = SOURCE[:20]
H = bits('0101101010')


def inverse(y, wall):
    # Complete: once the rightmost two bits are chosen, left
    # permutivity fixes every other bit; the wall checks the first.
    ans = set()
    for a, b in product((0, 1), repeat=2):
        x = [0] * (len(y)+1)
        x[-2:] = a, b
        for j in range(len(y)-1, 0, -1):
            x[j-1] = y[j] ^ (x[j] | x[j+1])
        if y[0] == wall ^ (x[0] | x[1]):
            assert update((wall,)+tuple(x)) == y
            ans.add(tuple(x))
    return ans


def backwards(word, steps):
    rows = {word}
    counts = []
    for t in range(5, 5-steps, -1):
        rows = {x for y in rows for x in inverse(y, t % 2)}
        counts.append(len(rows))
    return rows, counts


def main():
    rows = [SOURCE]
    implications = 0
    for t in range(26):
        old = rows[-1]
        new = update((t % 2,)+old)
        if old[-1]:
            new += (old[-2] ^ 1,)
        for right in (0, 1):
            assert update((t % 2,)+old+(right,))[:len(new)] == new
            implications += 1
        rows.append(new)
    assert rows[6][:11] == bits('11100100100')
    assert rows[16][:14] == bits('11100110111011')
    assert rows[26][:13] == bits('1110100011011')
    assert tuple(r[4] for r in rows[:26]) == S+D+H
    actual = 0
    for tail in product((0, 1), repeat=5):
        for far in (0, 1):
            literal = run(SOURCE+tail+(far,)*32, 26)
            for t, p in enumerate(rows):
                assert literal[t][:len(p)] == p
            actual += 1
    parents, counts = backwards(FORBIDDEN, 3)
    assert counts == [4, 8, 20]
    assert all(p[:7] == bits('1110010') for p in parents)
    assert not inverse(bits('1110010'), 0)
    assert backwards(FORBIDDEN, 4)[1] == [4, 8, 20, 0]
    shorter, _ = backwards(SOURCE[:19], 4)
    assert shorter
    # A full explicit shorter positive controls phase and indexing.
    p = min(shorter)
    assert run(p, 4)[4] == SOURCE[:19]
    known = bits('111011111111000000100011110111')
    preimages, _ = backwards(run(known, 6)[6], 6)
    assert len(preimages) == 632 and known in preimages
    # Record P2's bounded construction failure without extending it.
    for tail in product((0, 1), repeat=12):
        v = sum(b << j for j, b in enumerate(bits('11101111111100')+tail+(0,)*10))
        width, a = 36, None
        for t in range(22):
            width -= 1
            v = (((v << 1) | (t % 2)) ^ (v | (v >> 1))) & ((1 << width)-1)
            if t == 5:
                a = (v >> 10) & 1
        gate = tuple((v >> j) & 1 for j in range(9, 14))
        assert not (a == 1 and ((v >> 6) & 7) == 5 and
                    (gate == bits('11100') or gate[:4] == bits('1101')))
    changed = list(SOURCE)
    changed[12] = 0
    other = run(tuple(changed)+(0,)*24, 26)
    assert other[0][10] == 1 and other[0][12] == 0
    assert other[16][6:9] == bits('010')
    print(dict(prefix_implications=implications, actual_controls=actual,
               inverse_levels=counts, known_inverse=632,
               named_shorter_parent='PASS', unexpected_white13='C at16',
               P1='REFUTED', P2='FAILED4096; inconclusive',
               P3='FAILED', P4='REFUTED', P5='HAND GUARD',
               actual_restart_exclusion='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
