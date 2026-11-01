#!/usr/bin/env python3
"""L1282 (Local, 2026-11-01): independent exhaustive check of GPT's GC2354 fresh-input collision law, in Local's own
code. Run: python3 tests/probes/genealogy_fresh_bits_local.py  (seconds; no files written)
Three fixed right halves (111 = the seed's time-one row, 1011001, 1001); every 14-bit left word; three complete
episodes. Checks: each run-length list with sum L <= 14 has exactly 2^(14 - sum L) left words and one consumed
prefix; the exposure identity B - t = -sum L at each reset; and the list decoded by the all-zero left word.
"""
import numpy as np
from itertools import product
from collections import defaultdict
NL = 14
for right in ('111', '1011001', '1001'):
    rh = [int(c) for c in right]
    groups = defaultdict(set); counts = defaultdict(int); bad = 0
    T = 60; W = 2 * T + NL + len(rh) + 10; O = NL + T + 5     # O = index of position 0
    for word in product((0, 1), repeat=NL):
        x = np.zeros(W, dtype=np.uint8)
        for j, v in enumerate(word): x[O - 1 - j] = v        # word lists bits at -1, -2, ...
        for j, v in enumerate(rh): x[O + j] = v
        B, t, Ls, ok = 0, 0, [], True
        while len(Ls) < 3:
            q = O + B + 1 + int(np.flatnonzero(x[O + B + 1:])[0])   # first black right of B
            M = q - (O + B) - 1
            for _ in range(M // 2):
                x = np.concatenate(([0], x[:-2] ^ (x[1:-1] | x[2:]), [0])).astype(np.uint8); t += 1
                nB = int(np.flatnonzero(x[:O + B + 2]).max()) - O
                assert nB == B + 1; B = nB
            a = B
            while x[O + a - 1] == 1: a -= 1
            L = B - a + 1
            x = np.concatenate(([0], x[:-2] ^ (x[1:-1] | x[2:]), [0])).astype(np.uint8); t += 1
            nB = int(np.flatnonzero(x[:O + B + 2]).max()) - O
            assert nB == a, (word, B, a, nB)
            B = nB; Ls.append(L)
            if B - t != -sum(Ls): bad += 1
            if sum(Ls) > NL: ok = False; break
        if ok:
            key = tuple(Ls); counts[key] += 1; groups[key].add(word[:sum(Ls)])
    viol = [(k, counts[k]) for k in counts if counts[k] != 2 ** (NL - sum(k)) or len(groups[k]) != 1]
    print(f'right half {right}: {len(counts)} three-episode lists with sum L <= {NL}; count = 2^(14 - sum L) and one consumed prefix '
          f'for every list: {not viol}; c identity failures {bad}; list for the all-zero word {[k for k in groups if (0,)*sum(k) in groups[k]]}')
