#!/usr/bin/env python3
"""rule30_cloud_echo_interference.py: EI, the echo lens as interference at the kicks (RULE30-PRIZE.md 8.103)

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_echo_interference.py [N=3072] [SEEDS=16]
COST:       expected well under a minute.

Why. 8.102's surprise (INSTINCT-CLOUD.md S6): at kick bits, the echoes from sites 3 .. 8 over the last 8 rows sum to 1
at 91.5% of kicks (R(8, 2) = 0.085), while the echo lens is a coin almost everywhere else. The owner: "Echoes conspiring
sounds like interference." Over GF(2) an echo term is a phase: a sum of bits is a product of signs (-1)^bit, so a
biased parity is coherent interference and a fair one is decoherence. His next question asks whether compounded jumps
"remain rooted in the pattern or decohere". This probe measures where the coherence at a kick lives and how far it
reaches. Same world as rule30_cloud_echo_wall.py: site 0 clamped to t mod 2, sites >= 1 random beyond the light cone,
the same seeds, the same clean and kick bits.

Definitions. For a kick bit r and a lag m (the AND at row r-1-m), the echo terms at that lag are the ANDs at sites k
whose kernel to site 1 after m rows is odd. c_m is their parity over sites k >= 3, and the signed bias b_m = 2 P(c_m = 1)
- 1, taken over kick bits, is the interference amplitude at lag m. The track band at lag m holds sites with
0.4 m <= k - 1 <= 0.8 m + 1 and k >= 3: where a front arriving at 0.5 to 0.75 cells a row (8.102) sits. Off-track is
every other site k >= 3 that the kernel can reach (k - 1 <= m).

PREDICTIONS, written 2026-10-14 before any run, pushed before it (N = 3072, 16 seeds, rows from 1024).
  I1 (exact control): the parity of all echo terms at sites 3 .. 8 over lags 0 .. 7 is 1 at a fraction of kick bits equal
     to 1 - R(8, 2) of 8.102, that is 0.915.
  I2 (0.55): the coherence is short. |b_m| >= 0.3 at every lag m <= 5, and |b_m| <= 0.1 at every lag m = 12 .. 23,
     at kick bits.
  I3 (0.55): the coherence rides the front. For lags m = 2 .. 10 at kick bits, the track band's parity has a larger
     |bias| than the off-track parity at a majority of those lags, and the off-track |bias| is at most 0.2 at every one.
  U, the unexpected check (0.7), replicating L1 of 8.4 (98.1% of slips at wheel phases 32 and 52) with this instrument:
     the clean window's phase just before a kick takes two main values, 20 apart mod 56, holding at least 90% of
     kicks. Any third phase lies 10 from one of them (entry 27's class 42) and holds at most 2%.
  Counterfactual. |b_m| >= 0.3 at lags of 12 or more would make the kick's coherence long-range. Off-track parities as
  biased as the track's would mean S6 is not a front arriving.
"""
import random
import sys
from collections import Counter

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


def parity(x):
    return bin(x).count('1') & 1


def main():
    kmask, e = [], 2
    for _ in range(MAXLAG + 1):
        kmask.append(e)
        e = ((e << 1) ^ e ^ (e >> 1)) & sites(MAXLAG + 8)
    track, off = [], []
    for m in range(MAXLAG):
        tb = 0
        for k in range(3, m + 2):
            if 0.4 * m <= k - 1 <= 0.8 * m + 1:
                tb |= 1 << k
        track.append(tb)
        off.append(sites(m + 1) & ~sites(2) & ~tb)
    ones = {'kick': [0] * MAXLAG, 'clean': [0] * MAXLAG}
    on_t, on_o = [0] * MAXLAG, [0] * MAXLAG
    rows = {'kick': 0, 'clean': 0}
    i1 = 0
    phases = Counter()
    for seed in range(SEEDS):
        states, c = run(seed)
        ph = windows(c)
        for r in range(LO, N):
            kick = ph[r - 56] is not None and ph[r - 55] is None
            clean = ph[r - 55] is not None
            if not kick and (not clean or r % 8):
                continue
            kind = 'kick' if kick else 'clean'
            rows[kind] += 1
            if kick:
                phases[ph[r - 56]] += 1
                tot = 0
                for m in range(8):
                    a = states[r - 1 - m]
                    tot ^= parity(a & (a >> 1) & kmask[m] & sites(8) & ~sites(2))
                i1 += tot
            for m in range(MAXLAG):
                a = states[r - 1 - m]
                ands = a & (a >> 1) & kmask[m]
                ones[kind][m] += parity(ands & ~sites(2))
                if kick:
                    on_t[m] += parity(ands & track[m])
                    on_o[m] += parity(ands & off[m])
    nk, nc = rows['kick'], rows['clean']
    print('rows: kick bits %d, clean bits (every 8th) %d' % (nk, nc))
    print('I1: parity of echoes at sites 3..8 over lags 0..7 is 1 at %.3f of kick bits' % (i1 / nk))
    print('\nlag m   b_m kick   b_m clean   track b   off-track b   (signed biases 2P-1)')
    for m in range(MAXLAG):
        bk = 2 * ones['kick'][m] / nk - 1
        bc = 2 * ones['clean'][m] / nc - 1
        bt = 2 * on_t[m] / nk - 1 if track[m] else float('nan')
        bo = 2 * on_o[m] / nk - 1 if off[m] else float('nan')
        print('  %2d    %+.3f     %+.3f      %+.3f      %+.3f' % (m, bk, bc, bt, bo))
    print('\nU: clean-window phase just before each kick (phase: count)')
    for p, n in phases.most_common():
        print('  %2d: %5d  (%.1f%%)' % (p, n, 100 * n / nk))


if __name__ == '__main__':
    main()
