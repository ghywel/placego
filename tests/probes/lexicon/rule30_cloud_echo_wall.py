#!/usr/bin/env python3
"""rule30_cloud_echo_wall.py: EW, door (d). Are the kicks born where cr fires near the wall? (RULE30-PRIZE.md 8.102)

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_echo_wall.py [N=3072] [SEEDS=16]
COST:       expected a minute or two.

Why. 8.49 left a hypothesis untested: "the kicks are born where that term [cr] fires near the wall". 8.100 wrote Rule 30
as the Rule 150 jump XOR the echoes of every earlier AND, and the owner made that door (d) of CONSTELLATION.md
section H. Beside the wall (site 0 clamped to t mod 2, sites >= 1 random to beyond the light cone, as in
rule30_cloud_ruler_kicks.py, world B) the same identity holds on the half-line:
    v_(t+1) = L v_t  XOR  w_t e_1  XOR  N(v_t),   L = Rule 150 with site 0 held at 0,  N(v)_k = v_k v_(k+1),
so column 1 at row r is, exactly for any horizon M,
    [L^M v_(r-M)]_1  XOR  (the wall's drive over the last M rows)  XOR  (echoes of the ANDs at rows r-M .. r-1).
An AND at site k reaches site 1 only after k - 1 rows, so the echoes from sites 1 .. M make the sum exact.

Three readings of 8.49's hypothesis.
  Literal: the AND at the wall cell fires on the step that makes the kick. Entry 28 (Proposition 15) already says a kick
    lands just after a white, which forbids it. Kept here as an exact control.
  Echo lens: R(M, B), the reconstruction that keeps only the ANDs at sites 1 .. B, reproduces column 1 at kick bits
    for B small against M.
  True dynamics: T(M, B), the true clamped rule run for M rows from the true sites 1 .. B with fresh random bits
    beyond, reproduces column 1. Small B at kick bits would mean the kick is born near the wall.
Rows. A row r is a clean bit when column 1 over rows r-55 .. r is a rotation of U. It is a kick bit when the window
ending at r-1 is clean and the one ending at r is not, so r is the bit that breaks the rotation.

PREDICTIONS, written 2026-10-14 before any run and pushed at 16:28 BST in affb206 (the 16:30 first written here was a misread clock) (N = 3072 rows, 16 seeds, rows from 1024; all kick bits,
every 8th other row; M = 8, 16, 32).
  D0 (exact control): R(M, M) equals column 1 at every analysed row, for each M.
  D1 (exact control, entry 28): at every kick bit r, site 1 is white at row r-1, so the AND at the wall cell is silent
     on the step before every kick.
  D2 (0.75): the echo lens is not local. For M = 16 and 32 and every B <= M/2, R(M, B) agrees with column 1 at a
     rate in [0.4, 0.6], at clean bits and at kick bits alike. Reason: the jump carries the interior's bits into
     column 1 and the far echoes must cancel them; cutting the echoes leaves the jump's interior part uncancelled.
  D3 (0.6): the true dynamics is local where the wheel runs: T(16, 8) >= 0.95 at clean bits.
  D4 (0.5): kicks carry news from about half a cell a row back (slips are domain walls moving half a cell a step,
     8.7 and 8.8). At kick bits T(32, 16) >= 0.95 and T(32, 4) <= 0.8, and T(32, 8) is lower at kick bits than at
     clean bits by at least 0.1.
  E (the unexpected check, 0.6): the number of echo terms reaching column 1 (ANDs with an odd kernel to site 1) over
     the last 16 rows has the same mean at kick bits as at clean bits, within 10 percent.
  Counterfactual. R(M, small B) well away from 0.5 at clean bits would make the echo lens local where the wheel runs,
  and kicks could then be traced to near-wall echoes. T(M, small B) near 1 at kick bits would make kicks born near the
  wall in the true dynamics, 8.49's hypothesis in a non-literal form.

OUTCOME of the registered run, 2026-10-14 16:29 BST (N = 3072, 16 seeds, 1,138 kick bits; 1.3 s).
  D0 PASS: R(M, M) equals column 1 at every analysed row for M = 8, 16 and 32.
  D1 PASS: site 1 is white on the row before all 1,138 kick bits, so the AND at the wall cell never fires there.
  D2 REFUTED narrowly, as registered. At clean bits and at M = 32 it holds: 0.471 .. 0.536 for M = 16 and
     0.486 .. 0.515 for M = 32, for every kind of bit. At kick bits with M = 16 it lies outside [0.4, 0.6]:
     B = 0: 0.608, B = 1: 0.392, B = 4: 0.392, B = 8: 0.613.
  D3 HELD at the threshold: T(16, 8) = 0.950 at clean bits, where R(16, 8) = 0.495. The dynamics is local where the
     wheel runs, and the echo lens is not.
  D4 PART. T(32, 4) = 0.600 <= 0.8 at kick bits, and T(32, 8) is 0.628 at kick bits against 0.830 at clean bits. But
     T(32, 16) = 0.772 < 0.95: a kick needs more than half a cell a row. The depth needed at kick bits lies in (4, 6]
     for M = 8, (8, 12] for M = 16 and (16, 24] for M = 32: 0.5 to 0.75 cells a row. Near the wall (B <= 4) a kick
     bit is reproduced only 0.56 .. 0.60 of the time at every M.
  E REFUTED (the unexpected check): kick bits have more echo terms over 16 rows, 22.91 against 20.30 at clean bits, a
     difference of 2.61 with standard error 0.125 across seeds (post hoc).
  Not predicted (post hoc, a surprise): at M = 8 the echo lens is sharply structured at kick bits. R(8, 2) = 0.085 and
     R(8, 6) = 0.915, so the echoes from sites 3 .. 6 over the last 8 rows sum to 1 at almost every kick bit.
  Reading. 8.49's hypothesis is closed in all three readings. Literal: D1 and entry 28. True dynamics: kicks are news
  arriving from 0.5 to 0.75 cells a row out, not born at the wall. Echo lens: coin-like at M = 32. The Rule 150 echo
  picture is exact but not local: where the true rule is local (clean bits, T(16, 8) = 0.95), the jump carries the
  interior's bits into column 1 and the far echoes cancel them, so cutting the echoes gives a coin (R(16, 8) = 0.495).
  The OR's blocking, which makes the wheel local, shows up in the echo picture only as cancellation.
"""
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3072
SEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 16
LO = 1024
U = '00010011010001001101000100110100010011010001001101001101'
ROT = {sum(int(U[(p + j) % 56]) << j for j in range(56)): p for p in range(56)}
GRID = {8: (0, 1, 2, 4, 6, 8), 16: (0, 1, 2, 4, 8, 12, 16), 32: (0, 1, 2, 4, 8, 16, 24, 32)}
LOW = (1 << 72) - 1


def sites(m):
    """Mask of sites 1 .. m."""
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


def clean_windows(c):
    """fl[t]: column 1 over rows t .. t+55 is a rotation of U."""
    win = sum(c[j] << j for j in range(56))
    fl = [win in ROT]
    for t in range(1, len(c) - 55):
        win = (win >> 1) | (c[t + 55] << 55)
        fl.append(win in ROT)
    return fl


def recon(states, r, M, B):
    """The echo lens: the Rule 150 jump from row r-M, the wall's drive, and the ANDs at sites 1 .. B only."""
    m, nb = sites(M + 1), sites(B)
    u = states[r - M] & m
    for s in range(r - M, r):
        v = states[s]
        u = ((u << 1) ^ u ^ (u >> 1)) & m
        u ^= (s % 2) << 1
        u ^= v & (v >> 1) & nb
    return (u >> 1) & 1


def true_local(states, r, M, B, rnd):
    """The true clamped rule for M rows from the true sites 1 .. B at row r-M, fresh random bits beyond."""
    m, keep = sites(M + 1), sites(B)
    u = (states[r - M] & keep) | ((rnd.getrandbits(M + 2) << 1) & m & ~keep)
    for s in range(r - M, r):
        u = (u & ~1) | (s % 2)
        u = ((u << 1) ^ (u | (u >> 1))) & m
    return (u >> 1) & 1


def main():
    kmask, e = [], 2
    for _ in range(33):
        kmask.append(e)
        e = ((e << 1) ^ e ^ (e >> 1)) & sites(40)
    tally = {}
    d0_bad = d1_bad = kicks_total = 0
    echo_terms = {'clean': [], 'kick': []}

    def add(key, ok):
        a, n = tally.get(key, (0, 0))
        tally[key] = (a + ok, n + 1)

    for seed in range(SEEDS):
        states, c = run(seed)
        fl = clean_windows(c)
        rnd = random.Random(55000 + seed)
        for r in range(LO, N):
            kick = fl[r - 56] and not fl[r - 55]
            clean = fl[r - 55]
            if not kick and r % 8:
                continue
            kind = 'kick' if kick else ('clean' if clean else 'other')
            if kick:
                kicks_total += 1
                d1_bad += (states[r - 1] >> 1) & 1
            for M, Bs in GRID.items():
                d0_bad += recon(states, r, M, M) != c[r]
                for B in Bs:
                    add(('R', M, B, kind), recon(states, r, M, B) == c[r])
                    add(('T', M, B, kind), true_local(states, r, M, B, rnd) == c[r])
            if kind in echo_terms:
                n = sum(bin(states[s] & (states[s] >> 1) & kmask[r - 1 - s]).count('1') for s in range(r - 16, r))
                echo_terms[kind].append(n)
    print('rows: N = %d, seeds = %d, analysed from row %d; kick bits: %d' % (N, SEEDS, LO, kicks_total))
    print('D0 exact identity: R(M, M) != column 1 at %d analysed (row, M) pairs' % d0_bad)
    print('D1 entry 28: kick bits with site 1 black at row r-1: %d of %d' % (d1_bad, kicks_total))
    for lens in ('R', 'T'):
        print('\n%s(M, B): agreement with column 1 at clean / kick / other bits' % lens)
        for M, Bs in GRID.items():
            for B in Bs:
                parts = []
                for kind in ('clean', 'kick', 'other'):
                    a, n = tally.get((lens, M, B, kind), (0, 0))
                    parts.append('%.3f (%5d)' % (a / n, n) if n else '   -  ')
                print('  M = %2d  B = %2d   %s' % (M, B, '   '.join(parts)))
    for kind, xs in echo_terms.items():
        print('E: echo terms reaching column 1 over 16 rows at %s bits: mean %.2f over %d rows'
              % (kind, sum(xs) / len(xs), len(xs)))


if __name__ == '__main__':
    main()
