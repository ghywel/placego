"""GC1110: identify the nonlinear source of the lost phase field.

Missing inference: GC1109 identifies a phase defect, but its SLL
example does not tell which renewal interactions produce that field
at arbitrary time. A source formula, valid on all continuations,
would make a proposed hidden representation retain the right data.
This is not a new canonical-return test or a depth sweep.
Record searched: phase.*(ANF|polynomial|cubic|degree)|sparse.*
(Boolean|polynomial)|GC1109 ->20 hits11 files; G138/139 and
GC1107..1109 read. Their all-depth locality does not give this source.
P1 BEFORE algebra/controls: after reducing only products of markers
at distance <3, the depth19 even/odd defect has degree at most3.
REFUTED-BY: a surviving higher-degree monomial in that exact quotient.
Counterfactual: retaining only the singleton terms of the exact
sparse expression explains the defect.
REFUTED-BY: an independent sparse input where all singleton terms
vanish but the phase defect does not.
Controls: independent literal Rule30 inverse triangles for every
sparse length11 window, checked against the symbolic expressions;
the already proved SLL cone. No solver, records or language census.
Unexpected check: retain windows with a marker gap exceeding5;
the sparse identity must not depend on S/L's maximum gap.
OUTCOME P1 HELD: degree3,88 sparse windows,23 with a gap >5;
unary counter00001000100. This counter is in the sparse relaxation,
not S/L (its gap4 is forbidden there).

ADDENDUM BEFORE the S/L controls: symbolic forcing gives an exact
depth20 even expression. Removing gap4 products under the S/L
premise leaves four pairwise disjoint positive terms:
  q_(s+5) OR q_(s+7) OR q_(s+4)q_(s+9)
  OR q_(s+3)q_(s+6)q_(s+9).
P2: with u=s+7 this partitions into renewal blocks L:10110,
S precededL:101, S precededS:111. Hence no00 at every depth20
even-time position; this is a temporal shield, not a depth deadline.
REFUTED-BY: any five-letter cyclic S/L control failing the exact
formula, block table or no00. Literal Rule30 is independent of ANF.
Unexpected check: all-S has depth19 phase defect identically1 and
depth20 even identically1; phase errors cannot be charged merely
to long gaps or a finite number of exceptional renewals. The cubic
term alone creates the even20 black cell on q=10010010010.
Counterfactual: drop that cubic term. The all-S window must refute it.
No new template return, nearby-depth sweep, solver or record run.
ADDENDUM OUTCOME: P2 HELD on640 phase windows of all32 five-letter
cyclic S/L controls; formula, block table and no00 all agree with
literal Rule30. Dropping the cubic term is REFUTED by all-S.
"""
from itertools import product


ONE = frozenset((0,))
ZERO = frozenset()


def sparse(mask):
    return not (mask & (mask << 1) or mask & (mask << 2))


def add(a, b):
    return a ^ b


def multiply(a, b):
    out = set()
    for u in a:
        for v in b:
            w = u | v
            if sparse(w):
                if w in out:
                    out.remove(w)
                else:
                    out.add(w)
    return frozenset(out)


def either(a, b):
    return add(add(a, b), multiply(a, b))


def symbolic():
    q = [frozenset((1 << i,)) for i in range(11)]
    wall = [ZERO, ONE] * 11
    first = [v for a in q for v in (add(ONE, a), ONE)]
    columns = [wall, first]
    for _ in range(2, 21):
        a, b = columns[-1], columns[-2]
        columns.append([add(a[t + 1], either(a[t], b[t]))
                        for t in range(len(a) - 1)])
    return columns


def evaluate(p, mask):
    return sum((mask & monomial) == monomial for monomial in p) % 2


def literal(q):
    columns = [[0, 1] * 11, [v for a in q for v in (1 - a, 1)]]
    for _ in range(2, 21):
        a, b = columns[-1], columns[-2]
        out = []
        for t in range(len(a) - 1):
            parents = [left for left in (0, 1)
                       if (30 >> (4 * left + 2 * a[t] + b[t])) & 1 == a[t + 1]]
            assert len(parents) == 1
            out.append(parents[0])
        columns.append(out)
    return columns


def names(p):
    return [tuple(i for i in range(11) if mask >> i & 1)
            for mask in sorted(p, key=lambda x: (bin(x).count('1'), x))]


def positive20(q):
    return int(q[5] or q[7] or (q[4] and q[9])
               or (q[3] and q[6] and q[9]))


def renewal_controls(phase):
    checks = 0
    for letters in product('SL', repeat=5):
        n = sum(3 if a == 'S' else 5 for a in letters)
        q = [0] * n
        blocks = [0] * n
        r = 0
        for k, letter in enumerate(letters):
            q[r] = 1
            word = '10110' if letter == 'L' else (
                '111' if letters[k - 1] == 'S' else '101')
            blocks[r:r + len(word)] = map(int, word)
            r += len(word)
        assert r == n
        for s in range(n):
            window = [q[(s + i) % n] for i in range(11)]
            concrete = literal(window)
            even = concrete[20][0]
            assert even == positive20(window) == blocks[(s + 7) % n]
            assert even or concrete[20][2]
            if all(a == 'S' for a in letters):
                assert concrete[19][0] ^ concrete[19][1] == 1
            checks += 1
    all_s = tuple(map(int, '10010010010'))
    concrete = literal(all_s)
    assert (concrete[19][0] ^ concrete[19][1]) == 1
    assert concrete[20][0] == 1 and not (all_s[5] or all_s[7]
                                        or (all_s[4] and all_s[9]))
    assert evaluate(phase, sum(v << i for i, v in enumerate(all_s))) == 1
    return checks


def main():
    columns = symbolic()
    phase = add(columns[19][0], columns[19][1])
    degree = max(bin(m).count('1') for m in phase)
    singletons = frozenset(m for m in phase if bin(m).count('1') <= 1)
    counter = None
    count = long_gap = 0
    for q in product((0, 1), repeat=11):
        mask = sum(v << i for i, v in enumerate(q))
        if not sparse(mask):
            continue
        concrete = literal(q)
        assert all(evaluate(p, mask) == v for c, d in zip(columns, concrete)
                   for p, v in zip(c, d))
        defect = concrete[19][0] ^ concrete[19][1]
        assert evaluate(phase, mask) == defect
        count += 1
        markers = [i for i, v in enumerate(q) if v]
        long_gap += any(b - a > 5 for a, b in zip(markers, markers[1:]))
        if defect and not evaluate(singletons, mask) and counter is None:
            counter = ''.join(map(str, q))
    renewal_checks = renewal_controls(phase)
    print(dict(degree=degree, phase=names(phase),
               even19=names(columns[19][0]), even20=names(columns[20][0]),
               complete_sparse_controls=count, larger_gap_controls=long_gap,
               unary_counter=counter, P1='HELD' if degree <= 3 else 'REFUTED',
               SL_controls=renewal_checks, P2='HELD', cubic_control='REFUTED'))


if __name__ == '__main__':
    main()
