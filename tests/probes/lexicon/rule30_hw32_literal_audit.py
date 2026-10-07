"""GC370: independent scalar audit of L224's published 39-edge witness.

Prediction and counterfactual recorded in CLOUD-LOCAL before execution.
This checks the displayed segment, not its root ancestry or the full HW32 census.
"""
import json
import re
from fractions import Fraction
from pathlib import Path


def bit(word, index):
    return (word >> (index % 32)) & 1


def reset(word, clock):
    return next(i + 1 for i in range(32) if bit(word, clock + i))


def scalar_edge(a, b, c):
    return all(bit(c, i + 1) == (bit(a, i) ^ (bit(b, i) | bit(c, i)))
               for i in range(32))


def pulse(word):
    return any(all(bit(word, i) == int(i % p == s) for i in range(32))
               for p in (1, 2, 4, 8, 16, 32) for s in range(p))


def main():
    ledger = Path('CHAT-LEDGER.md').read_text()
    block = ledger.split('## L224 ', 1)[1].split('\n## ', 1)[0]
    matches = re.findall(r'^    (\d+) ([0-9a-f]{8}) ([0-9a-f]{8}) (\d+) (\d+) (-?\d+)$',
                         block, re.M)
    rows = [(int(d), int(a, 16), int(b, 16), int(pc), int(dl), int(z))
            for d, a, b, pc, dl, z in matches]
    assert len(rows) == 40
    clocks = []
    for d, a, b, pc, dl, z in rows:
        assert (z + 5 * d) % 2 == 0
        t = (z + 5 * d) // 2
        clocks.append(t)
        assert b.bit_count() == pc
        assert reset(b, t) == dl
    for i, (left, right) in enumerate(zip(rows, rows[1:])):
        d, a, b, pc, dl, z = left
        assert right[0] == d + 1 and right[1] == b
        assert scalar_edge(a, b, right[2])
        assert clocks[i + 1] == clocks[i] + dl
        assert right[5] - z == 2 * dl - 5
    segment = rows[:-1]
    assert not any(pulse(row[2]) for row in segment)
    elapsed = sum(row[4] for row in segment)
    debt = Fraction(2 * elapsed - 5 * len(segment), 2)
    assert debt == Fraction(rows[-1][5] - rows[0][5], 2) == Fraction(157, 2)
    long = [row for row in segment if row[4] >= 10]
    long_debt = sum((Fraction(2 * row[4] - 5, 2) for row in long), Fraction(0))
    assert [row[4] for row in long] == [10, 12, 11, 14, 16, 13]
    assert long_debt == 61
    assert not scalar_edge(rows[0][1], rows[0][2], rows[1][2] ^ 1)
    assert reset(rows[0][2], clocks[0] + 1) != rows[0][4]
    endpoint_included = debt + Fraction(2 * rows[-1][4] - 5, 2)
    assert endpoint_included == 78 != debt
    out = dict(records=40, transitions=39, elapsed=elapsed, debt=str(debt),
               popcount_sum=sum(row[3] for row in segment),
               mean_popcount=sum(row[3] for row in segment) / len(segment),
               long_delays=[row[4] for row in long], long_debt=str(long_debt),
               other_debt=str(debt-long_debt), endpoint_included=str(endpoint_included),
               controls='PASS', scope='literal segment; no root ancestry replay')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
