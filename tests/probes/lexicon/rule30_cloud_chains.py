#!/usr/bin/env python3
"""rule30_cloud_chains.py: CH, the owner's chain reading of the single cell's pattern: the rows read off as one binary
chain, and that chain split at the exact order/chaos boundary B(t) of section 8.74 into an orderly chain and a random
chain (side question; serves nothing on the status board directly, CONSTELLATION.md).

RUN-ON:     cpu (Python 3; numpy for block counts; standard-library lzma and zlib)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_chains.py [LOG2T=12] [LOG2P=10]
COST:       a minute or two at LOG2T = 12 (chains of 16 million bits); several minutes at 13.

The owner's idea (chat, 2026-10-10): read the pattern not as rows and columns but as one long binary chain, the rows
concatenated; then split that chain at the orderly wave front into two chains, "like a complex number", one of the
orderly side and one of the random side. Does the orderly chain tell us about the random one, and do the chains carry
structure their two-dimensional form hides?

What is exact, with no run needed. Cell i of row t (rows of the single cell, read from the left edge) sits at chain
position t^2 + t + i, so the rule becomes one recurrence with a growing lag,
    a[p] = a[p - 2t - 1] XOR (a[p - 2t] OR a[p - 2t + 1]),   t = floor(sqrt(p)),
except at the two cells at each end of a row, where a lagged term falls outside the previous row and reads 0. Row
starts are the squares; the centre column is the pronic numbers t (t + 1). Read from the left edge, the first e
diagonals are a closed system (section 8.31), so the orderly chain (the first B(t) bits of each row, B from section
8.74) is autonomous, and the random chain (the rest) is driven by it at its left boundary and never feeds back: a
clock driving a register, not two independent coordinates. The centre column lies in the random chain at offset
t - B(t), about 0.25 t from the front, and the front never returns to it (section 8.74).

What is measured: whether the split separates compressible order from incompressible chaos in the chains' own
one-dimensional terms, and whether the random chain is the coin it looks like.
  Chains to t = 2^LOG2T: F (full rows, t >= 2), O (bits 0 .. B(t) - 1 of each row), C (bits B(t) .. 2t), the
  near-front band N (64 bits from B(t)), the centre band M (64 bits centred on bit t, the centre column), and an
  i.i.d. fair-coin chain I of C's length (seed 30).
  Statistics: xz (lzma preset 9, extreme) and zlib-9 ratios on the bit-packed chains; density; block entropy rates
  h_k = H_k - H_(k-1) over overlapping k-blocks, k = 2, 4, 8, 12, 16; run-length frequencies against 2^-L.
Record searched: concatenat, row-major, run-length, lzma, compressib (no chain reading in the record; section 8.20
measured column entropies, 8.74 the boundary, 8.30 the band).

PREDICTIONS, written 2026-10-10 19:15 BST, before the first run (LOG2T = 12, LOG2P = 10).
  CH-P0 (control). B(t) never decreases; every row from t = 2 starts 110 and ends with 1; the orderly share of F is
      between 0.33 and 0.42 (B is about 0.75 t of a row's 2t + 1 bits).
  CH-P1 (blind). xz ratio of O at most 0.30; of C at least 0.97; of I at least 0.99; of F between 0.55 and 0.85.
  CH-P2 (blind). Block entropy rate h_16 of C at least 0.98 bits per bit and of I at least 0.99; of O at most 0.80
      (its two-dimensional order need not show in one-dimensional blocks; confidence 0.5).
  CH-P3 (blind). C's density within 0.49 .. 0.51, and its run frequencies for L = 1 .. 10, both colours, within 10%
      of 2^-L (the uniform measure is Rule 30-invariant, and the random side should be close to it by now).
  CH-P4 (unexpected check). The near-front band N compresses better than the centre band M: xz ratio of N at most
      0.90 and of M at least 0.97, because the diagonals just past B(t) have periods 2^11 .. 2^13, whose repeats fall
      inside xz's window, while the centre's do not. Confidence 0.4.
  Counterfactual: if the split did not separate order from chaos, C's xz ratio falls below 0.9 (CH-P1 fails); if the
  chaotic side is not near the uniform measure at these times, CH-P3 fails. Refuted-by: any of the above.
"""
import lzma, math, random, sys, time, zlib
from itertools import groupby
import numpy as np


def rows(n):
    V = [1]
    for _ in range(n):
        v = V[-1]
        V.append((v << 2) ^ ((v << 1) | v))      # bit e = x_t(-t + e): the e-th diagonal from the left edge
    return V


def bits(v):
    return format(v, 'b')[::-1]                  # from the left edge; the last bit (the right edge) is always 1


def pack(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, 'big')


def ratios(s):
    data = pack(s)
    return (len(lzma.compress(data, preset=9 | lzma.PRESET_EXTREME)) / len(data),
            len(zlib.compress(data, 9)) / len(data))


def block_rates(s, kmax=16):
    a = (np.frombuffer(s.encode(), dtype=np.uint8) - 48).astype(np.int64)
    n = len(a) - kmax + 1
    v = np.zeros(n, dtype=np.int64)
    for j in range(kmax):
        v = (v << 1) | a[j:j + n]
    H = {}
    for k in range(1, kmax + 1):
        c = np.bincount(v >> (kmax - k), minlength=1 << k).astype(np.float64)
        p = c[c > 0] / n
        H[k] = float(-(p * np.log2(p)).sum())
    return {k: H[k] - H[k - 1] for k in range(2, kmax + 1)}


def run_table(s, lmax=10):
    counts = {'0': [0] * (lmax + 2), '1': [0] * (lmax + 2)}
    for ch, g in groupby(s):
        L = sum(1 for _ in g)
        counts[ch][min(L, lmax + 1)] += 1
    out = {}
    for ch in '01':
        total = sum(counts[ch])
        out[ch] = [counts[ch][L] / total / 2 ** -L for L in range(1, lmax + 1)]   # observed / fair-coin
    return out


def main(log2t=12, log2p=10):
    t0 = time.time()
    N, P = 1 << log2t, 1 << log2p
    V = rows(N + P)
    F, O, C, NB, MB, Bs = [], [], [], [], [], []
    for t in range(2, N + 1):
        s = bits(V[t])
        x = V[t] ^ V[t + P]
        B = (x & -x).bit_length() - 1 if x else 2 * t + 1
        Bs.append(B)
        F.append(s); O.append(s[:B]); C.append(s[B:])
        NB.append(s[B:B + 64]); MB.append(s[max(0, t - 32):t + 32])
    frame = all(s.startswith('110') and s.endswith('1') for s in F)
    mono = all(b <= c for b, c in zip(Bs, Bs[1:]))
    F, O, C, NB, MB = (''.join(x) for x in (F, O, C, NB, MB))
    I = format(random.Random(30).getrandbits(len(C)), 'b').zfill(len(C))
    share = len(O) / len(F)
    print('rows 2 .. %d, P = %d: F %d bits, O %d, C %d; B(%d) = %d; frame 110..1 %s; B monotone %s; orderly share %.3f'
          % (N, P, len(F), len(O), len(C), N, Bs[-1], frame, mono, share), flush=True)
    print('CH-P0', 'HELD' if frame and mono and 0.33 <= share <= 0.42 else 'REFUTED')
    R = {}
    for name, s in (('F', F), ('O', O), ('C', C), ('I', I), ('N', NB), ('M', MB)):
        xz, zl = ratios(s)
        h = block_rates(s)
        R[name] = (xz, zl, s.count('1') / len(s), h)
        print('%s: %9d bits, xz %.4f, zlib %.4f, density %.4f, h_k (k = 2, 4, 8, 12, 16) = %s'
              % (name, len(s), xz, zl, R[name][2], ' '.join('%.4f' % h[k] for k in (2, 4, 8, 12, 16))), flush=True)
    p1 = R['O'][0] <= 0.30 and R['C'][0] >= 0.97 and R['I'][0] >= 0.99 and 0.55 <= R['F'][0] <= 0.85
    p2 = R['C'][3][16] >= 0.98 and R['I'][3][16] >= 0.99 and R['O'][3][16] <= 0.80
    print('CH-P1', 'HELD' if p1 else 'REFUTED', '| CH-P2', 'HELD' if p2 else 'REFUTED')
    runs = run_table(C)
    ok = all(0.9 <= r <= 1.1 for ch in '01' for r in runs[ch])
    print('C runs, observed / 2^-L for L = 1 .. 10: zeros', ' '.join('%.3f' % r for r in runs['0']),
          '| ones', ' '.join('%.3f' % r for r in runs['1']))
    p3 = 0.49 <= R['C'][2] <= 0.51 and ok
    print('CH-P3', 'HELD' if p3 else 'REFUTED')
    p4 = R['N'][0] <= 0.90 and R['M'][0] >= 0.97
    print('CH-P4 (unexpected check)', 'HELD' if p4 else 'REFUTED', '(%d s)' % (time.time() - t0))


if __name__ == '__main__':
    a = [int(x) for x in sys.argv[1:]]
    main(*a)
