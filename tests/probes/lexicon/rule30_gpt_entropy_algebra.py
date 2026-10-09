#!/usr/bin/env python3
"""GC857: independent forbidden-word algebra, not an OH macro-graph replay.
Prediction: the two L479 polynomials match direct prefix automata.
Countercontrol: a finite word-count ratio is not the limiting growth exactly.
Unexpected check: prefix exemptions change short counts but not entropy.
No external packages, solver, CA runs or data files.
"""
from itertools import permutations, product


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def determinant(matrix):
    n = len(matrix)
    out = [0] * (n + 1)
    for perm in permutations(range(n)):
        term = [(-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))]
        for i, j in enumerate(perm):
            term = mul(term, matrix[i][j])
        for i, x in enumerate(term):
            out[i] += x
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def automaton(patterns):
    states = sorted({w[:i] for w in patterns for i in range(len(w))}, key=lambda w: (len(w), w))
    trans = []
    for s in states:
        row = []
        for b in '01':
            w = s + b
            row.append(None if any(w.endswith(p) for p in patterns) else
                       max((i for i, q in enumerate(states) if w.endswith(q)), key=lambda i: len(states[i])))
        trans.append(row)
    return states, trans


def main():
    for patterns, expected in [(('1101',), [-1, 1, 0, -2, 1]),
                               (('1111', '11100'), [1, -1, -1, -1, -1, 1])]:
        states, trans = automaton(patterns)
        n = len(states)
        adj = [[sum(t == j for t in trans[i]) for j in range(n)] for i in range(n)]
        char = determinant([[[-adj[i][j], int(i == j)] for j in range(n)] for i in range(n)])
        assert char == expected, (patterns, char)
        gfden = determinant([[[int(i == j), -adj[i][j]] for j in range(n)] for i in range(n)])
        # (I-z A) f = 1; Cramer's rule for the empty-prefix starting state.
        matrix = [[[int(i == j), -adj[i][j]] for j in range(n)] for i in range(n)]
        for i in range(n):
            matrix[i][0] = [1]
        gfnum = determinant(matrix)
        counts, layer = [1], [1] + [0] * (n - 1)
        for length in range(1, 13):
            nxt = [0] * n
            for i, v in enumerate(layer):
                for t in trans[i]:
                    if t is not None:
                        nxt[t] += v
            layer = nxt
            counts.append(sum(layer))
            words = [''.join(w) for w in product('01', repeat=length)]
            strict = sum(not any(p in w for p in patterns) for w in words)
            exempt = sum(not any(w.startswith(p, j) for p in patterns for j in range(1, len(w))) for w in words)
            assert strict == counts[-1]
            L = max(map(len, patterns))
            assert strict <= exempt
            if length >= L:
                assert exempt <= 2 ** L * counts[length - L]
        length = min(map(len, patterns))
        words = [''.join(w) for w in product('01', repeat=length)]
        strict = sum(not any(p in w for p in patterns) for w in words)
        exempt = sum(not any(w.startswith(p, j) for p in patterns for j in range(1, len(w))) for w in words)
        assert exempt > strict
        def poly(x):
            return sum(v * x ** i for i, v in enumerate(char))
        lo, hi = 1.5, 2.0
        assert poly(lo) < 0 < poly(hi)
        for _ in range(60):
            mid = (lo + hi) / 2
            if poly(mid) < 0:
                lo = mid
            else:
                hi = mid
        root = (lo + hi) / 2
        assert abs(counts[12] / counts[11] - root) > 1e-8
        print(patterns, 'states', states, 'char ascending', char,
              'GF numerator/denominator ascending', gfnum, gfden,
              'growth approx', format(root, '.15f'),
              'short strict/exempt', strict, exempt)
    print('ALL CONTROLS PASS; no OH language-equality replay or actual entropy claim')


if __name__ == '__main__':
    main()
