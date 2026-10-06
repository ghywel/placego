"""Slow-wall switch audit, predictions before run, 2026-10-06.

SP0 must: for wall0^a1^b, a1..8,b1..24, the first a+b-1 cells of
  row0 depend only on its a visible white bits; monotone blocks yield a+1
  distinct prefixes, independent of arbitrary later column1 values.
SP1 must: if b>=3a+1, row0 is checkerboard on depths4a..a+b-1,
  for arbitrary white bits, not just monotone ones. a1..8,b<=40.
SP2 blind: for balanced a=b4..16, every monotone white block forces a black
  cell at depth at least a within the certified prefix of length2a-1.
SP3 unexpected must: SP1 holds for arbitrary nonperiodic boundary bits before
  the black run, with no white-block premise. a1..8, eight random cases each.
CF must fail: the checkerboard to depth b-1 holds at the last black phase
  before a white time (first left cell is1, rather than checkerboard0).
REFUTED-BY: a prefix mismatch or a differing protected-band cell invalidates
  SP0/SP1/SP3; retain any SP2 counterexample without replacing its prediction.
OUTCOME: pending. Small finite mechanism audit; no Local record job repeated.
"""

import random
from rule30_gpt_condrey_holes import forced_columns


def inverse_row(future, wall, first):
    # x0 is the current wall bit; x1 is obtained by inverting its update.
    out = [wall, first]
    for y in future:
        out.append(y ^ (out[-1] | out[-2]))
    return out[1:]


def prefix(a, b, visible):
    row = [int(j % 2 == 0) for j in range(1, b)]
    for t in range(a-1, -1, -1):
        first = visible[t] ^ int(t == a-1)
        row = inverse_row(row, 0, first)
    return row


def main():
    rng = random.Random(2026100618)
    cases = 0
    for a in range(1, 9):
        for b in range(1, 25):
            p = a+b
            tau = [int(t % p >= a) for t in range(3*p+50)]
            prefixes = []
            for r in range(a+1):
                visible = [0]*r + [1]*(a-r)
                expected = prefix(a, b, visible)
                assert len(expected) == p-1
                for _ in range(2):
                    sigma = visible + [rng.randrange(2) for _ in range(len(tau)-a)]
                    cols = forced_columns(tau, sigma, p-1)
                    assert [col[0] for col in cols] == expected, (a,b,r)
                    cases += 1
                prefixes.append(tuple(expected))
            assert len(set(prefixes)) == a+1, (a,b)
    print('SP0 PASS:', cases, 'prefix comparisons; all192 blocks have a+1 distinct prefixes')
    cases = 0
    for a in range(1, 9):
        for b in range(3*a+1, 41):
            for _ in range(8):
                row = prefix(a, b, [rng.randrange(2) for _ in range(a)])
                assert all(row[j-1] == int(j % 2 == 0) for j in range(4*a, a+b))
                cases += 1
    print('SP1 PASS:', cases, 'protected-band comparisons')
    failures = []
    for a in range(4, 17):
        for r in range(a+1):
            row = prefix(a, a, [0]*r + [1]*(a-r))
            last = max((j for j, x in enumerate(row, 1) if x), default=0)
            if last < a:
                failures.append((a,r,last,row))
    print('SP2', 'REFUTED' if failures else 'HELD', failures)
    cases = 0
    for a in range(1, 9):
        b = 3*a+5
        for _ in range(8):
            n = a+b+20
            tau = [rng.randrange(2) for _ in range(a)] + [1]*b + [rng.randrange(2) for _ in range(20)]
            sigma = [rng.randrange(2) for _ in range(n)]
            cols = forced_columns(tau, sigma, a+b-1)
            assert all(cols[j-1][0] == int(j % 2 == 0) for j in range(4*a, a+b))
            cases += 1
    print('SP3 PASS:', cases, 'nonperiodic protected-band comparisons')
    tau = [1,1,1,1,0,0]
    cols = forced_columns(tau, [0]*len(tau), 1)
    assert cols[0][3] == 1
    print('CF FAILS AS REQUIRED: last-black time3 has left cell1')
    print('ALL CONTROLS PASS')


if __name__ == '__main__':
    main()
