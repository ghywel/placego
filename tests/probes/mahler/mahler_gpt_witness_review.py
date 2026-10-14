#!/usr/bin/env python3
"""GC1237: independent integer audit of L721's fixed 15-state witness.

Registered before execution, 2026-10-14 12:49 BST. No grid/game census.
Record searched: '15-state|14-state|W15|complement.*witness' and '7/57|RUIC'
-> three paragraphs in Local's existence-certificate source; L721 read.

Predictions: all 30 edges pass; deleting state 3 leaves 14 states and 28 edges,
both parities, closed under mirror with the SAME sigma and complemented carry.
Counterfactual: any failed edge quarantines the copied table/result until resolved.
Independent controls: flip an edge's carry; remove a referenced state; extend
a tight target beyond its image by one unit. Each must be rejected.
Unexpected check: the complete 15-state table is NOT mirror invariant, while
the 14-state core is. This tests the surplus-root explanation of the asymmetry.
Also check that this unchanged witness fails in the narrower [113,799]/912
window; that failure is only about this witness, not all possible strategies.
The constants are copied from L721 into integer units of 1/912. Source-table
agreement uses AST parsing only; neither Local's checker nor game is executed.

Outcome, 2026-10-14 12:51 BST: PASS after preregistration commit82032e9f.
All predictions held; all three negative controls rejected. This verifies a
finite existence certificate, not the universal continuous threshold. The
fixed response graph's independent endpoint-cycle bound is in RULE30-GPT GC1237.
"""
import ast
from fractions import Fraction
from pathlib import Path

# (left, right, parity, carry, sigma0 target ID, sigma1 target ID).
ROWS = {
    1: (117, 192, 0, 0, 2, 10),
    2: (213, 288, 0, 0, 4, 11),
    3: (277, 331, 0, 0, 5, 12),
    4: (320, 395, 0, 0, 6, 13),
    5: (416, 491, 0, 0, 7, 14),
    6: (480, 534, 0, 0, 8, 15),
    7: (682, 736, 0, 1, 9, 1),
    8: (725, 800, 0, 1, 10, 2),
    9: (112, 187, 1, 0, 7, 14),
    10: (176, 230, 1, 0, 8, 15),
    11: (378, 432, 1, 1, 9, 1),
    12: (421, 496, 1, 1, 10, 2),
    13: (517, 592, 1, 1, 11, 4),
    14: (624, 699, 1, 1, 13, 6),
    15: (720, 795, 1, 1, 14, 7),
}


def failures(rows, lower=112, upper=800):
    bad = []
    if {r[2] for r in rows.values()} != {0, 1}:
        bad.append('parity coverage')
    for i, (p, q, c, t, j0, j1) in rows.items():
        if not (lower <= p < q <= upper and c in (0, 1) and t in (0, 1)):
            bad.append((i, 'source/window'))
        for sigma, j in enumerate((j0, j1)):
            if j not in rows:
                bad.append((i, sigma, 'closure'))
                continue
            l, r, d = rows[j][:3]
            # Cross-multiplied containment, independent of fractional images.
            if not (3*p + 912*c - 1824*t <= 2*l < 2*r <= 3*q + 912*c - 1824*t
                    and d == ((sigma + t) & 1)):
                bad.append((i, sigma, 'image/parity'))
    return bad


def mirrored(rows):
    states = {r[:3]: i for i, r in rows.items()}
    for p, q, c, t, j0, j1 in rows.values():
        mi = states.get((912-q, 912-p, 1-c))
        if mi is None:
            return False
        other = rows[mi]
        if other[3] != 1-t:
            return False
        for sigma, j in enumerate((j0, j1)):
            l, r, d = rows[j][:3]
            target = states.get((912-r, 912-l, 1-d))
            if other[4+sigma] != target:
                return False
    return True


def source_agrees():
    source = Path(__file__).with_name('mahler_existence_certificate.py')
    tree = ast.parse(source.read_text())
    table = next(n.value for n in tree.body if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == '_W15' for t in n.targets))

    def literal(n):
        if isinstance(n, ast.Constant) and type(n.value) is int:
            return n.value
        if isinstance(n, (ast.Tuple, ast.List)):
            return tuple(literal(x) for x in n.elts)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'F' and not n.keywords:
            return Fraction(*(literal(x) for x in n.args))
        raise ValueError('unexpected source literal')

    published = literal(table)
    def state(i):
        p, q, c = ROWS[i][:3]
        return Fraction(p, 912), Fraction(q, 912), c
    copied = tuple((state(i), (row[3], state(row[4])), (row[3], state(row[5])))
                   for i, row in ROWS.items())
    return published == copied


def main():
    assert source_agrees(), 'source/transcription disagreement'
    assert not failures(ROWS)
    core = {i: row for i, row in ROWS.items() if i != 3}
    assert not failures(core)
    assert not mirrored(ROWS) and mirrored(core)
    corrupted = dict(core)
    p, q, c, t, j0, j1 = corrupted[1]
    corrupted[1] = p, q, c, 1-t, j0, j1
    assert failures(corrupted)
    assert failures({i: row for i, row in core.items() if i != 2})
    corrupted = dict(core)
    p, q, c, t, j0, j1 = corrupted[14]
    corrupted[14] = p-1, q, c, t, j0, j1  # breaks state 9's tight lower image
    assert failures(corrupted)
    assert failures(core, 113, 799)
    print('PASS: source agrees; 30 original edges and 28 core edges; both parities;')
    print('14-state mirror symmetry at same sigma; all three negative controls rejected;')
    print('unchanged witness rejected in narrower window. No grid/game census run.')


if __name__ == '__main__':
    main()
