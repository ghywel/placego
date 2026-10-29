#!/usr/bin/env python3
"""paired_column_runs_census.py: every periodic point on a ring of 3..18 cells against Theorem B's bound (L1084).

RUN-ON: cpu, under a second. On a ring every column of a periodic point shares its least period P, so every
maximal white run of row 0 must have length <= 2P - 2 (zero_run_le), and every odd one of length >= 3 at most
2P - 5 (odd_zero_run_le). Prediction: no violation; the bound attained at small P. Counterfactual: a violation
refutes the formal statement's reading. Result (2026-10-29): no violation; attained at P = 3 (the period-3 ether
(000011111001)^inf, runs of 4) and P = 4 ((0000001)^inf, runs of 6). Cross-checked at n = 10 against a naive
period count (38 periodic states, periods 1, 5, 15).
"""
import time


def census(n):
    """(least period, longest white run, longest odd white run >= 3) for every nonzero periodic point of the n-ring."""
    mask = (1 << n) - 1
    nxt = [(((x << 1) | (x >> (n - 1))) & mask) ^ (x | (((x >> 1) | ((x & 1) << (n - 1))) & mask)) for x in range(1 << n)]
    state = bytearray(1 << n)
    out = []
    for s in range(1, 1 << n):
        if state[s]:
            continue
        path, x = [], s
        while state[x] == 0:
            state[x] = 1
            path.append(x)
            x = nxt[x]
        if state[x] == 1:                                   # a new cycle, entered at x
            cyc = path[path.index(x):]
            for y in cyc:
                if y == 0:
                    continue
                bits = [(y >> i) & 1 for i in range(n)]
                k = bits.index(1)
                runs = [len(r) for r in ''.join(map(str, bits[k:] + bits[:k])).split('1') if r]
                out.append((len(cyc), max(runs, default=0), max([r for r in runs if r % 2 and r >= 3], default=0)))
        for y in path:
            state[y] = 2
    return out


def main():
    t0 = time.time()
    longest, odd, bad = {}, {}, []
    for n in range(3, 19):
        for p, r, o in census(n):
            longest[p] = max(longest.get(p, 0), r)
            odd[p] = max(odd.get(p, 0), o)
            if p >= 2 and r > 2 * p - 2:
                bad.append(('even', n, p, r))
            if o and o > 2 * p - 5:
                bad.append(('odd', n, p, o))
    print('rings 3..18, %.1f s, violations: %s' % (time.time() - t0, bad))
    print('P: (longest white run, 2P-2, longest odd run >= 3, 2P-5) for P <= 40:',
          {p: (longest[p], 2 * p - 2, odd[p], 2 * p - 5) for p in sorted(longest) if p <= 40})


if __name__ == '__main__':
    main()
