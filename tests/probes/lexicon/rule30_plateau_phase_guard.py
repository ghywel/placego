"""GC1041: the plateau cylinder has a two-tick maturity/phase guard.

Missing inference: GC1040 selects a parent plateau from a spatial prefix,
but does that prefix also preserve an age/clock restriction? A useful
hidden-state invariant must retain these, not only a list of row patterns.
Record searched: (100110|0011) + (black|two.step|prehistory) -> GC1017's
white train slab, GC1004/1005's one-black-update rooted exclusions;
GC1010 concerns the opposite-order two-update marker1110. Those read.
Hand claim before controls: a black-phase row of age>=2 cannot begin
100110, hence cannot begin1(0011)^m 0^r for m>=1,r>=1. Its preceding
white-wall parent must start110, which has no black-wall predecessor.
P1: exhaustive literal two-step black-phase cone has no100110 output.
P2: the white-phase cone admits100110; do not ban this actual train slab.
P3: black-phase10011 (last symbol removed) is admitted at age2, and the
whole100110 is admitted at age1. The age and sixth-bit guards matter.
Counterfactual: this local spatial age clause does not bound records or
exclude the train at its correct white phase. No temporal-word verdict.
Controls: literal Wolfram-table shrinking cones, both clock phases; each
positive is retained and replayed. Unexpected check: positive at age1
but negative at age2, without increasing the cone or solver scope.
Bound: 256 source rows, two updates, six output cells; no SAT or scan.
OUTCOME: P1/P2/P3 HELD. White-phase positive00000100 ->100110;
black-phase shortened positive00111000 ->100111. At age1 the white
parent1101000 gives100110. All are literal shrinking-cone replays.
Adaptive quantitative consequence, before its controls: GC1040's c=0
parent plateau extends TWO more sites to the right and admits only the
terminal pair00; c=1 admits the other THREE terminal pairs. Check the
same m0..6,r1..9 cases, without increasing any cone or time window.
These are terminal-pair counts, not initial seed or history counts.
"""


def tick(bits, wall):
    source = [wall] + bits
    return [(30 >> (4 * source[i] + 2 * source[i+1] + source[i+2])) & 1
            for i in range(len(bits)-1)]


def main():
    outputs = {}
    for phase in (0, 1):
        table = {}
        for number in range(256):
            bits = [(number >> i) & 1 for i in range(8)]
            result = tick(tick(bits, phase), 1-phase)
            word = ''.join(map(str, result))
            table.setdefault(word, ''.join(map(str, bits)))
        outputs[phase] = table
    p1 = '100110' not in outputs[1]
    p2 = '100110' in outputs[0]
    short = next((word for word in outputs[1] if word.startswith('10011')), None)
    parent = list(map(int, '1101000'))
    one = ''.join(map(str, tick(parent, 0)))
    p3 = short is not None and one == '100110'
    assert p1 and p2 and p3
    for phase, word in ((0, '100110'), (1, short)):
        source = outputs[phase][word]
        assert ''.join(map(str, tick(tick(list(map(int, source)), phase),
                                     1-phase))) == word
        print('two-step positive phase', phase, 'source', source, 'output', word)
    print('one-step positive white parent1101000 ->', one)
    print('P1', p1, 'P2', p2, 'P3', p3, 'literal cone controls PASS')
    from rule30_cut45_origin_scan import scan
    from rule30_cut45_origin_past import literal
    cases = 0
    for m in range(7):
        for r in range(1, 10):
            word = '1' + '0011' * m + '0' * r
            width = len(word)
            child = sum(int(c) << i for i, c in enumerate(word))
            counts = [0, 0]
            for right in ((0, 0), (0, 1), (1, 0), (1, 1)):
                end, history = scan(word, right)
                row = sum(pair[0] << (width - 1 - i)
                          for i, pair in enumerate(history))
                assert literal(row, end[0], right[1], width) == child
                c = 1 ^ end[0] ^ (m % 2)
                counts[c] += 1
                assert (right == (0, 0)) == (c == 0)
                if c == 0:
                    assert ((row >> (width-1)) & 1) == right[1] == 0
                cases += 1
            assert counts == [1, 3]
    print('terminal-pair count and white-plateau halo controls PASS', cases)


if __name__ == '__main__':
    main()
