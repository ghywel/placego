#!/usr/bin/env python3
"""GC2223 fixed Boolean guards and four finite entrance/exit controls. No widening."""
import hashlib
import json
import os
from pathlib import Path

WORDS = (149, 101, 89, 86)


def bg(t, j):
    return (WORDS[j % 4] >> (t % 8)) & 1


def literal(a, b, c):
    return (30 >> (4 * a + 2 * b + c)) & 1


def local_step(row):
    lo, hi = min(row), max(row)
    return {j: literal(row[j], row[j-1], row[j-2]) for j in range(lo+2, hi+1)}


def front_word(row, b, word):
    lo = b-len(word)+1
    return [row[j] for j in range(lo, b+1)] == word


def main():
    receipts = []
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                assert literal(a, b, c) == (a ^ (b | c))
    for t in range(8):
        for j in range(4):
            assert literal(bg(t, j), bg(t, j-1), bg(t, j-2)) == bg(t+1, j)
            assert bg(t+4, j+6) == bg(t, j)
    signatures = ((2, [1, 0, 1, 1]), (2, [1, 0, 0]),
                  (4, [1, 0, 0]), (6, [1, 0, 1]))
    for incoming in range(4):
        row = {j: bg(1, j) for j in range(-4, 11)}
        row.update({-4: incoming & 1, -3: incoming >> 1, -2: 1, -1: 0, 0: 1})
        snapshots = []
        for dt, (b, word) in enumerate(signatures, 1):
            row = local_step(row)
            assert front_word(row, b, word), (incoming, dt, row)
            assert row[b] != bg(1+dt, b)
            assert all(row[j] == bg(1+dt, j) for j in range(b+1, max(row)+1))
            snapshots.append({'time': 1+dt, 'front': b, 'guard': word})
        receipts.append({'incoming': incoming, 'cycle': snapshots})
    row = {j: bg(1, j) for j in range(-4, 11)}
    row.update({-4: 0, -3: 1, -2: 0, -1: 0, 0: 1})
    for _ in range(4):
        row = local_step(row)
    assert [row[j] for j in (4, 5, 6)] == [0, 0, 1]
    receipts.append({'omitted_guard_final': [row[j] for j in (4, 5, 6)]})
    row = [bg(0, j) for j in range(13)]
    for t, b in enumerate((0, 2, 2, 4, 6), 1):
        row = [literal(row[j], row[j-1] if j else 0, row[j-2] if j >= 2 else 0)
               for j in range(13)]
        assert max(j for j in range(13) if row[j] != bg(t, j)) == b, (t, row)
    assert row[4:7] == [1, 0, 1]
    receipts.append({'entrance_fronts': [0, 2, 2, 4, 6], 'final_guard': row[4:7]})
    for n, first in enumerate((6, 6, 9, 13)):
        width = 4*n+5
        packed = sum(7 << (4*i) for i in range(n)) + (5 << (4*n))
        row = [(packed >> j) & 1 for j in range(width)]
        trace = []
        for t in range(first+1):
            assert row == [(packed >> j) & 1 for j in range(width)]
            pair = row[4*n+3:4*n+5]
            target = [(234 >> (t % 8)) & 1, (170 >> (t % 8)) & 1]
            assert (pair == target) == (t < first), (n, t, pair, target)
            trace.append({'t': t, 'pair': pair, 'target': target})
            row = [literal(row[j], row[j-1] if j else 0, row[j-2] if j >= 2 else 0)
                   for j in range(width)]
            packed = (packed ^ ((packed << 1) | (packed << 2))) & ((1 << width)-1)
        receipts.append({'n': n, 'first_deviation': first, 'trace': trace})
    result = {'status': 'PASS', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'four local guards, one failed-guard control, one entrance, four fixed seeds',
              'receipts': receipts}
    (Path(os.environ['CAPPED_OUT']) / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'source_sha256', 'scope')}))


if __name__ == '__main__':
    main()
