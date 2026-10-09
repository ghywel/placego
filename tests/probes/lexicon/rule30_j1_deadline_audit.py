"""GC660: explicit j=1 left-side deadline proof controls, not a width census.

Prediction: maximal observation counts are 3 (black start), 8 (white start).
Tables are the finite hand certificate. Independent finite seeds attain both.
"""

TABLES = {
    1: [{1}, {1, 2}, {2, 3}],
    0: [{1}, {1, 2}, {2, 3}, {1, 3, 4}, {1, 4, 5},
        {1, 2, 3, 5, 6}, {3, 6, 7}, {2, 3, 4, 5, 7, 8}],
}


def truth(l, c, r):
    return (30 >> ((l << 2) | (c << 1) | r)) & 1


for phase, rows in TABLES.items():
    for t, (row, following) in enumerate(zip(rows, rows[1:])):
        wall = phase ^ (t % 2)
        computed = {
            d for d in range(1, t+3)
            if truth(int(d+1 in row), int(d in row),
                     wall if d == 1 else int(d-1 in row))
        }
        assert computed == following
    failures = [t for t, row in enumerate(rows)
                if (phase ^ (t % 2)) and 1 not in row]
    assert failures == [len(rows)-1]
    black = {-1, 0, 2} if phase else {-1, 7}
    trace = []
    for t in range(9):
        trace.append(int(0 in black))
        # Finite support expands by at most one cell; no truncation.
        black = {
            i for i in range(min(black)-1, max(black)+2)
            if int(i-1 in black) ^ (int(i in black) | int(i+1 in black))
        }
    n = len(rows)
    assert trace[:n] == [phase ^ (t % 2) for t in range(n)]
    assert trace[n] != phase ^ (n % 2)
    print('phase', phase, 'max observations', n,
          'attaining trace', ''.join(map(str, trace)), 'PASS')
