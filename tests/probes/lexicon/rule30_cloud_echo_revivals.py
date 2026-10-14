#!/usr/bin/env python3
"""rule30_cloud_echo_revivals.py: ER, INSTINCT-CLOUD.md S7. Are the kick's coherence revivals rigid cells or interference?

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_echo_revivals.py [N=3072] [SEEDS=16]
COST:       expected seconds.

Why. 8.103 measured, for each lag m before a kick, the bias b_m of the parity of the echo terms reaching column 1
(the ANDs at sites k >= 3 whose half-line Rule 150 kernel to site 1 after m rows is odd). Past the forced rows,
coherence revives at lags 9 (+0.94), 13 (+0.53) and 17 (-0.49). INSTINCT-CLOUD.md S7 asked why. The first guess, that
revivals sit at lags where the kernel reaches few cells, already fails on 8.103's numbers: lag 16 reaches 2 cells and
has bias -0.26, lag 13 reaches 6 and has +0.53. Two readings remain.
  Rigid cells: each sampled AND cell is nearly fixed at a kick, and the parity is fixed because its cells are.
  Interference: the cells vary one by one, but their parity is locked, so the coherence lives in their correlations.
Test. For each lag m and kernel site k, p(m, k) = P(AND at row r-1-m, site k = 1) over kick bits. If the cells were
independent, the parity's bias would be b_ind(m) = -prod_k (1 - 2 p(m, k)). Rigid cells give |b_ind| close to |b_m|;
interference gives |b_ind| much smaller than |b_m|. Same world, seeds and kick bits as rule30_cloud_echo_interference.py.

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  R1 (exact control): b_m recomputed here equals 8.103's at every lag (same seeds, same kick bits): +0.937 at 9,
     +0.534 at 13, -0.489 at 17.
  R2 (0.5, a genuine coin flip): at the three revival lags 9, 13 and 17, |b_ind| is within 0.15 of |b_m| with the same
     sign (rigid cells). The alternative, |b_ind| < |b_m| / 2 at two or more of them, would be interference.
  R3 (0.6): at the forced lags 2, 3, 4 and 6 (|b_m| = 1), every sampled cell is rigid (p in {0, 1}), so b_ind = b_m.
  U, the unexpected check (0.5): the revivals appear in both main kick classes. Split by the clean phase before the
     kick (52 or 32), |b_m| >= 0.3 at lag 9 in each class, with the same sign.
  Counterfactual. R2's alternative (interference) would make the owner's reading literal: the cells conspire by their
  correlations, not one by one.
"""
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3072
SEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 16
LO = 1024
MAXLAG = 24
U = '00010011010001001101000100110100010011010001001101001101'
ROT = {sum(int(U[(p + j) % 56]) << j for j in range(56)): p for p in range(56)}
LOW = (1 << 72) - 1


def sites(m):
    return (1 << (m + 1)) - 2


def run(seed):
    rnd = random.Random(9100 + seed)
    row = rnd.getrandbits(2 * N + 64) << 1
    states, col1 = [], []
    for t in range(N):
        row = (row & ~1) | (t % 2)
        states.append(row & LOW & ~1)
        col1.append((row >> 1) & 1)
        row = (row << 1) ^ (row | (row >> 1))
    return states, col1


def windows(c):
    win = sum(c[j] << j for j in range(56))
    out = [ROT.get(win)]
    for t in range(1, len(c) - 55):
        win = (win >> 1) | (c[t + 55] << 55)
        out.append(ROT.get(win))
    return out


def main():
    kernel, e = [], 2
    for _ in range(MAXLAG):
        kernel.append([k for k in range(3, MAXLAG + 2) if (e >> k) & 1])
        e = ((e << 1) ^ e ^ (e >> 1)) & sites(MAXLAG + 8)
    kicks = []
    for seed in range(SEEDS):
        states, c = run(seed)
        ph = windows(c)
        for r in range(LO, N):
            if ph[r - 56] is not None and ph[r - 55] is None:
                ands = [states[r - 1 - m] & (states[r - 1 - m] >> 1) for m in range(MAXLAG)]
                kicks.append((ph[r - 56], ands))
    n = len(kicks)
    print('kick bits: %d' % n)
    print('\nlag  cells  b_m     b_ind   rigid cells   (b = 2P(parity = 1) - 1)')
    for m in range(MAXLAG):
        ks = kernel[m]
        par = sum(bin(a[m] & sum(1 << k for k in ks)).count('1') & 1 for _, a in kicks)
        bm = 2 * par / n - 1
        prod, rigid = 1.0, 0
        for k in ks:
            p = sum((a[m] >> k) & 1 for _, a in kicks) / n
            prod *= 1 - 2 * p
            rigid += p in (0.0, 1.0)
        bind = -prod
        print('%3d  %5d  %+.3f  %+.3f   %d of %d' % (m, len(ks), bm, bind, rigid, len(ks)))
    print('\nU: bias at lags 9, 13, 17 by kick class')
    for cls in (52, 32):
        sub = [a for p, a in kicks if p == cls]
        out = []
        for m in (9, 13, 17):
            mask = sum(1 << k for k in kernel[m])
            par = sum(bin(a[m] & mask).count('1') & 1 for a in sub)
            out.append('%+.3f' % (2 * par / len(sub) - 1))
        print('  class %d (%d kicks): lags 9, 13, 17: %s' % (cls, len(sub), ', '.join(out)))


if __name__ == '__main__':
    main()
