"""GC1037: exact correlated past of GC1036's final-one origin fillings.

Missing inference: do the entry observations force x16(30)=0 OR x20(30)=0,
given CL198's common19 pins? Concrete sufficient result: exclude all eight
a=b=1 fillings by a backward width24 controlled-strip relation.
Record searched: (cut45|CL198|GC1036|entrymemory) +
(preimage|backward row|past strip) -> no hit, including ledgers.
New evidence: CL206 independently confirms GC1036's exact joint guard.
P1: no leading0 past survives for any of these eight fillings.
P2: at least one leading1 past survives (the inherited actual witness control).
Counterfactual: exclusion in a controlled strip is necessary for actual absence;
if a relaxed leading0 past survives, it does not refute the actual cut.
Controls: all width8 parent sets versus independent literal forward images;
six-tick labelled backward relation versus exhaustive width6 forward histories.
Unexpected check: if P1 fails, retain and literally replay a complete relaxed
past, distinguishing a definite failure from a cap or marginal speculation.
One width24 past, time30..0, 20000 rows, 30 s; no SAT or membership query.
OUTCOME: P1/P2 HELD. Maximum261 rows; only23 initial rows survive and
every one begins1. Surviving origin labels are7/23/31 (bit order16,20,21,22,24).
All parent and six-tick controls PASS. The unexpected extra restriction is
that five of the eight candidate origin fillings have no past with either
lead; the remaining three all have site21=1 and site22 implies site24.
This proves the conditional disjunction in the controlled strip; common19
pin forcing is still inherited from CL198, and no all-depth schema follows.
Control repair: a nonvacuity guard caught the original six-tick target0
having no admissible forward history. BEFORE the repaired replay, use
targets18/60, reached by literal initial rows0/8 with all-zero inputs;
require those explicit positives in the independently enumerated preimages.
The empty-target failure is retained; the origin result is replayed below.
"""

import signal
from itertools import product

PIN = '100110011001100000000010'
FREE = (16, 20, 21, 22, 24)
ENTRY = '000010001010000'


def parents(child, wall, width):
    # Left permutivity: the two rightmost parent bits determine the whole parent.
    for last, exterior in product((0, 1), repeat=2):
        row = last << (width - 1)
        current, right = last, exterior
        for i in range(width, 0, -1):
            left = ((child >> (i - 1)) & 1) ^ (current | right)
            if i > 1:
                row |= left << (i - 2)
            current, right = left, current
        if current == wall:
            yield row, exterior


def literal(row, wall, exterior, width):
    bits = [wall] + [(row >> i) & 1 for i in range(width)] + [exterior]
    return sum(((30 >> (4 * bits[i] + 2 * bits[i + 1] + bits[i + 2])) & 1) << i
               for i in range(width))


def controls():
    for wall in (0, 1):
        forward = {s: set() for s in range(256)}
        for row in range(256):
            for exterior in (0, 1):
                forward[literal(row, wall, exterior, 8)].add((row, exterior))
        for child in range(256):
            assert set(parents(child, wall, 8)) == forward[child]
    assert (0, 0) in set(parents(0, 0, 8))
    assert (0, 0) not in set(parents(0, 1, 8))
    targets = (18, 60)
    samples = {0: 0, 2: 1, 4: 0}
    for target in targets:
        expected = set()
        for row in range(64):
            for inputs in range(64):
                s = row
                for t in range(6):
                    if t in samples and (s & 1) != samples[t]:
                        break
                    s = literal(s, t % 2, (inputs >> t) & 1, 6)
                else:
                    if s == target:
                        expected.add(row)
        assert expected, 'multi-tick control target must have a nonempty forward preimage'
        assert (0 if target == 18 else 8) in expected
        actual = {target}
        for t in range(5, -1, -1):
            actual = {p for s in actual for p, _ in parents(s, t % 2, 6)}
            if t in samples:
                actual = {p for p in actual if (p & 1) == samples[t]}
        assert actual == expected
    print('parent truth-table and six-tick forward/backward controls PASS', flush=True)


def main():
    controls()
    initial = sum(int(c) << i for i, c in enumerate(PIN))
    rows = {}
    for label in range(32):
        if label & 3 != 3:
            continue
        s = initial | sum(((label >> j) & 1) << (i - 1) for j, i in enumerate(FREE))
        rows[s] = (1 << label, 0, s)
    counts = [(30, len(rows))]
    for t in range(29, -1, -1):
        nxt = {}
        for child, (labels, inputs, origin) in rows.items():
            for parent, exterior in parents(child, t % 2, 24):
                if t > 0 and t % 2 == 0 and (parent & 1) != int(ENTRY[t // 2]):
                    continue
                if parent in nxt:
                    old_labels, old_inputs, old_origin = nxt[parent]
                    nxt[parent] = (old_labels | labels, old_inputs, old_origin)
                else:
                    nxt[parent] = (labels, inputs | (exterior << t), origin)
        rows = nxt
        counts.append((t, len(rows)))
        if len(rows) > 20000:
            raise RuntimeError('state cap; no origin exclusion inferred')
    masks = [0, 0]
    for row, (labels, _, _) in rows.items():
        masks[row & 1] |= labels
    assert masks[0] == 0 and masks[1] == sum(1 << k for k in (7, 23, 31))
    print('counts', counts)
    print('origin_labels_by_lead', [[k for k in range(32) if (mask >> k) & 1] for mask in masks])
    print('P1', masks[0] == 0, 'P2', masks[1] != 0)
    if masks[0]:
        row = next(s for s in rows if not s & 1)
        _, inputs, origin = rows[row]
        s = row
        for t in range(30):
            if t % 2 == 0:
                assert (s & 1) == int(ENTRY[t // 2])
            s = literal(s, t % 2, (inputs >> t) & 1, 24)
        assert s == origin and all((s >> (i - 1)) & 1 for i in (16, 20))
        print('relaxed_past', format(row, '024b')[::-1],
              'inputs', format(inputs, '030b')[::-1],
              'origin30', format(origin, '024b')[::-1], 'literal replay PASS')


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(30)
    try:
        main()
    finally:
        signal.alarm(0)
