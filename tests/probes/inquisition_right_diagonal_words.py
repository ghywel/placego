#!/usr/bin/env python3
"""inquisition_right_diagonal_words.py: the words a single right diagonal of Rule 30 can never carry (T-S2, DQ-033).

RUN-ON:     cpu (Python 3 + numpy), about a minute
COMMAND:    python3 tests/probes/inquisition_right_diagonal_words.py [NMAX=10]

Census: the patterns of s(t) = x(t, t), t = 0..n-1, over every base row covering the light cone (exact, since Rule 30
is onto). Prints the minimal forbidden words (forbidden, with every proper factor allowed), their flip words
f(t) = s(t+1) XOR s(t), and the complement check. Independent control: Rule 30 run 2000 steps from three seeded random
rows of width 6001 (np.random.default_rng(31 + i)); every right diagonal clear of the corrupted edges (L1257 fix: the first run scanned one diagonal) is scanned for each minimal forbidden word
(must be absent) and for every allowed word of length <= 8 (expected present). Predictions P-R1, P-R2:
reports/inquisition-20261031.md (round 2), committed before this ran.
"""
import sys
import numpy as np

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
CHUNK = 1 << 22


def diagonal_language(n):
    h = n
    lo, hi = -(h - 1), (n - 1) + (h - 1)
    B = hi - lo + 1
    one = np.uint64(1)
    seen = np.zeros(0, dtype=np.uint64)
    for start in range(0, 1 << B, CHUNK):
        row = np.arange(start, min(1 << B, start + CHUNK), dtype=np.uint64)
        pat = np.zeros_like(row)
        for t in range(h):
            pat |= ((row >> np.uint64(t - lo)) & one) << np.uint64(t)
            if t + 1 < h:
                row = (row << one) ^ (row | (row >> one))
        seen = np.union1d(seen, np.unique(pat))
    return {tuple((int(v) >> i) & 1 for i in range(n)) for v in seen}


def main():
    langs = {n: diagonal_language(n) for n in range(1, NMAX + 1)}
    minimal = []
    for n in range(1, NMAX + 1):
        for w in range(1 << n):
            word = tuple((w >> i) & 1 for i in range(n))
            if word in langs[n]:
                continue
            if n > 1 and (word[1:] not in langs[n - 1] or word[:-1] not in langs[n - 1]):
                continue
            minimal.append(word)
    print("counts:", [len(langs[n]) for n in range(1, NMAX + 1)])
    comp_ok = all(tuple(1 - b for b in w) in [m for m in minimal if len(m) == len(w)] for w in minimal)
    print(f"minimal forbidden words up to length {NMAX}: {len(minimal)}; complement-closed: {comp_ok}")
    for w in minimal:
        flips = ''.join(str(w[i] ^ w[i + 1]) for i in range(len(w) - 1))
        print(f"  {''.join(map(str, w))}   flips {flips}")
    # independent control on random spacetimes
    T, Wd = 2000, 6001
    found_forbidden = 0
    allowed8 = {w for w in langs[8]}
    seen8 = set()
    for i in range(3):
        rng = np.random.default_rng(31 + i)
        row = rng.integers(0, 2, Wd, dtype=np.uint8)
        rows = [row]
        for _ in range(T - 1):
            new = np.zeros_like(row)
            new[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
            row = new
            rows.append(row)
        S = np.array(rows)
        for j0 in range(0, Wd - 2 * (T - 1)):          # diagonal x(t, j0 + t) stays clear of both corrupted edges
            diag = S[np.arange(T), j0 + np.arange(T)]
            st = ''.join(map(str, diag))
            for w in minimal:
                if ''.join(map(str, w)) in st:
                    found_forbidden += 1
            if j0 % 4 == 0:
                for a in range(0, T - 8):
                    seen8.add(tuple(diag[a:a + 8]))
    print(f"control: forbidden-word occurrences in random spacetimes: {found_forbidden}; "
          f"allowed length-8 words seen: {len(seen8 & allowed8)} of {len(allowed8)}; disallowed seen: {len(seen8 - allowed8)}")
    print("RIGHT_DIAGONAL_WORDS_DONE")


if __name__ == '__main__':
    main()
