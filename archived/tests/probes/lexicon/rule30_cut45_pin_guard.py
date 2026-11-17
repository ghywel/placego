"""GC1036: retain the five released pin bits jointly, without an exterior census.

Missing inference: CL198 pins 24 cells from entry plus exit. Which joint
condition on its five released cells actually prevents the final exit one?
This tests an origin predicate, not another later endpoint relocation.
Record searched: (16.*20.*21.*22.*24|five.*free|32 fillings) +
(guard|pin|cut) -> CL198's existing census/propagation, no joint predicate.
New evidence: CL205 corrects separate freedoms to joint pairs 10/11;
independent fillings must likewise be distinguished from actual joint rows.
P1: some nonzero filling still excludes the final one under free exterior.
P2: the final-one fillings are upward closed in the five pin bits.
Counterfactual: five free SAT marginals imply all 32 fillings are realized.
Control: packed transition equals the literal Wolfram table for width 8.
Unexpected check: a filling may already fail the nine-symbol exit prefix;
do not misclassify an empty conditioned set as a forced final zero.
Bound: 32 labels in one width-24 propagation, time30..88, 20000 rows, 30 s.
No actual-language query, width sweep, unbounded claim or new SAT call.
First outcome: P1/P2 HELD. Prefix-empty labels22; zero-only0/16;
one-possible labels3/7/11/15/19/23/27/31. Peak2554, controls PASS.
Adaptive P3 BEFORE replay: every one-possible filling forces the final one.
Independent replay: propagate labels0/1/3/16/31 separately using literal
Wolfram-table updates, and compare both endpoint possibilities to the labelled
packed propagation. This checks empty, zero and possible-one branches.
OUTCOME: P3 REFUTED (six fillings permit both final bits). Literal replay
also includes label7, covering a final-one-only case. In bit order
a=x16,b=x20,c=x21,d=x22,e=x24 at30, prefix-compatible iff
(a AND b) OR (NOT a AND NOT b AND NOT c AND NOT d); final1 possible iff
a AND b. Final0 possible iff the second term OR
(a AND b AND (NOT c OR d)). These are controlled-strip existence predicates,
not actual right-half membership. Either a=0 or b=0 therefore suffices for
the cut given the other19 pins and suffix observations. No transport identity:
for most a=b=1 fillings the final bit still depends on the exterior.
"""

import signal

PIN = '100110011001100000000010'
FREE = (16, 20, 21, 22, 24)
WORD = '000010001010000' + '10' * 10 + '001000010'


def step(s, wall, exterior, width):
    p = s | (exterior << width)
    return (((p << 1) | wall) ^ (p | (p >> 1))) & ((1 << width) - 1)


def literal(s, wall, exterior, width):
    bits = [wall] + [(s >> i) & 1 for i in range(width)] + [exterior]
    return sum(((30 >> (4 * bits[i] + 2 * bits[i + 1] + bits[i + 2])) & 1) << i
               for i in range(width))


def main():
    for s in range(256):
        for wall in (0, 1):
            for exterior in (0, 1):
                assert step(s, wall, exterior, 8) == literal(s, wall, exterior, 8)
    assert len(PIN) == 24 and len(WORD) == 44
    assert all(PIN[i - 1] == '0' for i in FREE)
    initial = sum(int(c) << i for i, c in enumerate(PIN))
    rows = {}
    for label in range(32):
        s = initial | sum(((label >> j) & 1) << (i - 1) for j, i in enumerate(FREE))
        rows[s] = 1 << label
    peak = len(rows)
    for t in range(30, 89):
        if t % 2 == 0 and t <= 86:
            rows = {s: labels for s, labels in rows.items() if (s & 1) == int(WORD[t // 2])}
        if t == 88:
            masks = [0, 0]
            for s, labels in rows.items():
                masks[s & 1] |= labels
            classes = {name: [label for label in range(32) if test(label)] for name, test in (
                ('PREFIX_EMPTY', lambda k: not ((masks[0] | masks[1]) >> k) & 1),
                ('FINAL_ZERO_ONLY', lambda k: ((masks[0] >> k) & 1) and not ((masks[1] >> k) & 1)),
                ('FINAL_ONE_POSSIBLE', lambda k: (masks[1] >> k) & 1),
                ('FINAL_BOTH', lambda k: ((masks[0] & masks[1]) >> k) & 1),
            )}
            assert 0 in classes['FINAL_ZERO_ONLY']
            one = set(classes['FINAL_ONE_POSSIBLE'])
            upward = all((a | b) in one for a in one for b in range(32))
            minimal = [a for a in sorted(one) if not any(b != a and (a & b) == b for b in one)]
            for label in range(32):
                a, b, c, d, _ = [(label >> j) & 1 for j in range(5)]
                base = not (a or b or c or d)
                assert bool(((masks[0] | masks[1]) >> label) & 1) == bool((a and b) or base)
                assert bool((masks[1] >> label) & 1) == bool(a and b)
                assert bool((masks[0] >> label) & 1) == bool(base or (a and b and (not c or d)))
            for label in (0, 1, 3, 7, 16, 31):
                s = initial | sum(((label >> j) & 1) << (i - 1) for j, i in enumerate(FREE))
                separate = {s}
                for time in range(30, 89):
                    if time % 2 == 0 and time <= 86:
                        separate = {s for s in separate if (s & 1) == int(WORD[time // 2])}
                    if time < 88:
                        separate = {literal(s, time % 2, e, 24) for s in separate for e in (0, 1)}
                assert {s & 1 for s in separate} == {b for b in (0, 1) if (masks[b] >> label) & 1}
            print('classes', classes)
            print('P1', any(k != 0 for k in classes['FINAL_ZERO_ONLY']),
                  'P2', upward, 'minimal_one_masks', minimal,
                  'final_rows', len(rows), 'peak', peak, 'controls PASS')
            print('P3', not classes['FINAL_BOTH'], 'independent literal branches PASS')
            return
        nxt = {}
        for s, labels in rows.items():
            for exterior in (0, 1):
                ns = step(s, t % 2, exterior, 24)
                nxt[ns] = nxt.get(ns, 0) | labels
        rows = nxt
        peak = max(peak, len(rows))
        if len(rows) > 20000:
            raise RuntimeError('state cap; no predicate inferred')


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(30)
    try:
        main()
    finally:
        signal.alarm(0)
