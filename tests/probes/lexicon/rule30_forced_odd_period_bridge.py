"""GC1092: an odd-period successor above an alternating-white parent dies.

Missing check-free inference: Jen excludes a fully white left tail;
the reported forced-only periodic case needs a separate parity bridge.
Record searched: forced.only|check.free with periodic|Jen ->6 hits,
3 files; odd.periodic|odd.spatial.period|odd.period with checkerboard|
alternating.white|white.*parity ->4 hits in2 files, no bridge theorem.
P1: named pure visible01/10 have black forced cells indefinitely in
both phases. HELD by exact seven-column cycles, not a period search.
P2: standard visible1 and other visible0 have white forced tails and
black checks. HELD; each violates a defining X4 prohibition.
P3 before controls: for odd q, alternating-white x on[a-2,b+2]
and q-periodic y=F(x) on[a-1,b+1] imply F^4(x)=0 on[a+2,b-q-2].
Proof: y obeys the XOR neighbor recurrence on one parity; odd-q
translation supplies the other. Its period3 linear pattern dies in3.
Counterfactual/unexpected: even q2 checkerboard is fixed, not killed.
Controls: scalar versus packed finite updates, arbitrary exterior
fixtures, all four period3 linear patterns, and exact periodic inverse
columns versus triangular time reconstruction. No solver, CUT, broad
periodic search or record computation. The missing all-periodic
forced-only theorem is a review question, not declared refuted.
"""
from itertools import product


def scalar(row):
    return tuple(row[j-1] ^ (row[j] | row[j+1])
                 for j in range(1, len(row)-1))


def packed(row):
    n = len(row)-2
    v = sum(x << j for j, x in enumerate(row))
    w = (v ^ ((v >> 1) | (v >> 2))) & ((1 << n)-1)
    return tuple((w >> j) & 1 for j in range(n))


def evolve(row, steps):
    rows = [tuple(row)]
    for _ in range(steps):
        nxt = scalar(rows[-1])
        assert nxt == packed(rows[-1])
        rows.append(nxt)
    return rows


def periodic_columns(word, phase):
    period = 2*len(word)
    b = tuple((t+phase) % 2 for t in range(period))
    a = tuple(1 if b[t] else 1-int(word[t//2]) for t in range(period))
    states, seen = [], {}
    while (a, b) not in seen:
        seen[a, b] = len(states)
        states.append((a, b))
        c = tuple(a[(t+1) % period] ^ (a[t] | b[t])
                  for t in range(period))
        assert all(a[(t+1) % period] == (c[t] ^ (a[t] | b[t]))
                   for t in range(period))
        b, a = a, c
    return states, seen[a, b]


def triangular_row(word, phase, depth):
    future = ()
    for t in range(depth-1, -1, -1):
        wall = (t+phase) % 2
        visible = int(word[(t//2) % len(word)]) if wall == 0 else 0
        now = [wall, ((t+1+phase) % 2) ^ (wall | visible)]
        for later in future:
            now.append(later ^ (now[-1] | now[-2]))
        future = tuple(now[1:])
    return future


def main():
    local = fixtures = rejected = periodic = 0
    for left, right in product((0, 1), repeat=2):
        y = scalar((0, left, 0, right, 0))
        assert y == (left, left ^ right, right)
        assert y[1] == (y[0] ^ y[2])
        local += 1
    linear_patterns = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
    for pattern in linear_patterns:
        assert not any(evolve(pattern*8, 3)[3])
    for q in (1, 3, 5, 7, 9):
        a, b = 10, 10+q+18
        width = b+12
        for white_parity in (0, 1):
            for pattern in linear_patterns:
                for exterior in product((0, 1), repeat=4):
                    x = tuple(0 if i % 2 == white_parity else pattern[i % 3]
                              for i in range(width))
                    x = exterior + x[4:-4] + tuple(1-z for z in exterior)
                    rows = evolve(x, 4)
                    y = rows[1]
                    hypothesis = all(y[i-1] == y[i+q-1]
                                     for i in range(a-1, b+2-q))
                    if not hypothesis:
                        rejected += 1
                        continue
                    assert all(x[i] == 0 for i in range(a-2, b+3)
                               if i % 2 == white_parity)
                    assert all(y[i-1] == (y[i-2] ^ y[i])
                               for i in range(a, b-q+1))
                    assert all(rows[4][i-4] == 0
                               for i in range(a+2, b-q-1))
                    fixtures += 1
    even_counter = evolve((1, 0)*30, 4)
    assert even_counter[4] == (1, 0)*26
    controls = {}
    for word, phase in (('1', 0), ('0', 1), ('01', 0), ('10', 0),
                        ('01', 1), ('10', 1)):
        states, start = periodic_columns(word, phase)
        period = len(states)-start
        expected = tuple(states[j if j < len(states) else
                                start+(j-start) % period][0][0]
                         for j in range(128))
        assert triangular_row(word, phase, 128) == expected
        forced_cycle = tuple(expected[j] for j in range(start, start+2*period)
                             if (j+1+phase) % 2 == 1)
        if len(word) == 1:
            assert not any(forced_cycle)
            assert any(expected[start:start+2*period])
        else:
            assert start == 0 and period == 7 and any(forced_cycle)
        controls[word, phase] = (start, period,
                                ''.join(str(s[0][0]) for s in states))
        periodic += 1
    print(dict(local_identities=local, nilpotent_patterns=4,
               finite_fixtures=fixtures, rejected_premises=rejected,
               periodic_controls=periodic, even_q_counterexample='PASS',
               odd_q_bridge='ALL q PROOF-SKETCH',
               periodic_forced_only_general='REVIEW GAP',
               prize_bound='OPEN'))
    print(controls)


if __name__ == '__main__':
    main()
