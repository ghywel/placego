#!/usr/bin/env python3
"""rule30_local_review_gc549.py: LR, Local's second reading of GPT's GC549 checkpoints 19, 20, 23 and 25 (row Q6; the
reading Local took in L286). The hand readings are in the chat; this probe replays their finite claims in Local's own
coding. Predictions pushed before the run.

RUN-ON:     cpu, Python standard library, seconds
COMMAND:    python3 tests/probes/lexicon/rule30_local_review_gc549.py

Local's coding (independent of GPT's paired recursion and of rule30_gpt_gc549_certificate.py): the left half is
rebuilt column by column on the time grid. With the clock on column 0, x_t(-1) = x_(t+1)(0) XOR (x_t(0) OR x_t(1)),
which needs column 1 only at the wall's white times (the visible word); then for j >= 2,
x_t(-j) = x_(t+1)(-(j-1)) XOR (x_t(-(j-1)) OR x_t(-(j-2))) on the cone t + j <= T. f_j = x_0(-j), g_j = x_1(-j).

PREDICTIONS (Local's, published before the run):
  LR-C1 (control): f_1 = 1 XOR c_0 at phase 0, and the word 0101 gives initial depths 1 .. 8 = 10000001 (GPT's
        worked control, checkpoint 15).
  LR-P1 (confidence 0.9): GPT's five printed polynomials (checkpoint 19: p13, p14, p14 + p15, p16, p17) equal Local's
        f_13, f_14, f_14 XOR f_15, f_16, f_17 on all 89 no-11 words of length 9, as unconditional identities.
  LR-P2 (confidence 0.95): exactly 11 of the 512 nine-symbol words make f_13 .. f_17 all zero at phase 0, and the
        only no-11 one is 010101001 (checkpoint 18; Cloud's RRL C3 found the same in its own coding).
  LR-P3 (confidence 0.9): on the no-11 domain the reduced polynomial of f_17 has coefficient 1 on c1 c3 c5 c7
        (checkpoint 20), computed by Moebius inversion over the no-11 index sets.
  LR-P4 (confidence 0.95): the identity f_(j+1) XOR f_j = g_j XOR f_(j-1) (1 XOR f_j) holds for j = 1 .. 16 on all
        512 words (checkpoint 20).
  LR-P5 (confidence 0.85): at phase 1 (wall black at time 0; visible symbols at times 1, 3, .., 17), no nine-symbol
        word avoiding 11 and 101001 makes initial depths 12 .. 18 all white with the clock through time 18
        (checkpoint 23's R_1(12) <= 6, checked directly rather than by its erosion argument).
  LR-P6 (confidence 0.95): checkpoint 25's two-step frontier identities hold on 20,000 random rows with an initial
        zero band at depths a .. b (2 <= a, b - a >= 3): x_2(-(a+1)) = x_0(-(a-1)), x_2(-j) = 0 for a + 2 <= j <= b - 2,
        x_2(-(b-1)) = x_0(-(b+1)).
  Unexpected check (descriptive): the largest degree of f_13 .. f_17 on the no-11 domain.
OUTCOME: not yet run.
"""
import random
from itertools import product


def left_cells(word, phase, T):
    """f_j = x_0(-j) for j <= T and g_j = x_1(-j) for j <= T - 1, from the visible word and the clock"""
    clock = [(t + phase) % 2 for t in range(T + 2)]           # phase 0: white at time 0
    white = [t for t in range(T + 1) if clock[t] == 0]
    col1 = {t: word[k] for k, t in enumerate(white) if k < len(word)}
    x = {}
    for t in range(T):                                       # column -1 on t = 0 .. T - 1
        c0 = clock[t]
        x[t, 1] = clock[t + 1] ^ (c0 | col1[t]) if c0 == 0 else clock[t + 1] ^ 1
    for t in range(T + 1):
        x[t, 0] = clock[t]
    for j in range(2, T + 1):
        for t in range(0, T - j + 1):
            x[t, j] = x[t + 1, j - 1] ^ (x[t, j - 1] | x[t, j - 2])
    f = {j: x[0, j] for j in range(1, T + 1)}
    g = {j: x[1, j] for j in range(1, T)}
    f[0], g[0] = clock[0], clock[1]
    return f, g


def no11(w):
    return all(not (w[i] and w[i + 1]) for i in range(len(w) - 1))


def has(w, pat):
    s = ''.join(map(str, w))
    return pat in s


def gpt_polys(c):
    c1, c2, c3, c4, c5, c6, c7, c8 = c[1:9]
    p13 = 1 ^ c3 ^ c4 ^ c5 ^ c6 ^ (c1 & c3) ^ (c2 & c5)
    p14 = c4 ^ c6 ^ (c1 & c3) ^ (c2 & c4) ^ (c2 & c5) ^ (c3 & c5) ^ (c4 & c6) ^ (c1 & c3 & c6)
    p1415 = 1 ^ c5 ^ c7 ^ (c3 & c6) ^ (c2 & c4 & c6)
    p16 = (c5 ^ (c2 & c4) ^ (c2 & c5) ^ (c3 & c7) ^ (c4 & c6) ^ (c4 & c7) ^ (c1 & c3 & c5) ^ (c1 & c3 & c7)
           ^ (c2 & c4 & c6) ^ (c2 & c4 & c7) ^ (c2 & c5 & c7))
    p17 = (1 ^ c4 ^ c5 ^ c8 ^ (c1 & c3) ^ (c3 & c7) ^ (c4 & c6) ^ (c1 & c3 & c6) ^ (c1 & c3 & c7) ^ (c2 & c4 & c6)
           ^ (c2 & c4 & c7) ^ (c1 & c3 & c5 & c7))
    return p13, p14, p1415, p16, p17


def moebius(fun, n=9):
    """reduced polynomial on no-11 words: coefficient of each independent index set"""
    sets = [S for S in product((0, 1), repeat=n) if no11(S)]
    sets.sort(key=sum)
    coef = {}
    for S in sets:
        v = fun(S)
        for U, cu in coef.items():
            if cu and all(U[i] <= S[i] for i in range(n)):
                v ^= 1
        coef[S] = v
    return {S: v for S, v in coef.items() if v}


def step(cells):
    """one Rule 30 update of a dict site -> bit on a finite window (sites outside are taken as 0)"""
    lo, hi = min(cells), max(cells)
    return {i: cells.get(i - 1, 0) ^ (cells.get(i, 0) | cells.get(i + 1, 0)) for i in range(lo + 1, hi)}


def main():
    words = list(product((0, 1), repeat=9))
    nwords = [w for w in words if no11(w)]
    f, _ = left_cells((0, 1, 0, 1), 0, 8)
    c1 = all(left_cells(w, 0, 17)[0][1] == 1 ^ w[0] for w in words) and [f[j] for j in range(1, 9)] == [1, 0, 0, 0,
                                                                                                         0, 0, 0, 1]
    print('LR-C1', 'PASS' if c1 else 'FAIL', [f[j] for j in range(1, 9)])
    p1 = True
    for w in nwords:
        F, _ = left_cells(w, 0, 17)
        mine = (F[13], F[14], F[14] ^ F[15], F[16], F[17])
        p1 &= mine == gpt_polys(w)
    print('LR-P1', 'HELD' if p1 else 'REFUTED', '(%d no-11 words)' % len(nwords))
    band = [w for w in words if all(left_cells(w, 0, 17)[0][j] == 0 for j in range(13, 18))]
    band11 = [''.join(map(str, w)) for w in band if no11(w)]
    print('LR-P2', 'HELD' if len(band) == 11 and band11 == ['010101001'] else 'REFUTED', len(band), band11)
    co = moebius(lambda S: left_cells(S, 0, 17)[0][17])
    key = tuple(1 if i in (1, 3, 5, 7) else 0 for i in range(9))
    print('LR-P3', 'HELD' if co.get(key) == 1 else 'REFUTED', '(%d monomials in f_17)' % len(co))
    p4 = True
    for w in words:
        F, G = left_cells(w, 0, 17)
        for j in range(1, 17):
            p4 &= (F[j + 1] ^ F[j]) == (G[j] ^ (F[j - 1] & (1 ^ F[j])))
    print('LR-P4', 'HELD' if p4 else 'REFUTED')
    surv, surv_r = [], []
    for w in words:
        F, _ = left_cells(w, 1, 18)
        if all(F[j] == 0 for j in range(12, 19)):
            surv.append(''.join(map(str, w)))
            if no11(w) and not has(w, '101001'):
                surv_r.append(surv[-1])
    print('LR-P5', 'HELD' if not surv_r else 'REFUTED', 'unrestricted survivors %d, restricted %s' % (len(surv), surv_r))
    rng = random.Random(20261008)
    p6, n = True, 0
    for _ in range(20000):
        a = rng.randint(2, 12)
        b = a + rng.randint(3, 12)
        row = {-j: rng.getrandbits(1) for j in range(0, b + 8)}
        row.update({j: rng.getrandbits(1) for j in range(1, 6)})
        for j in range(a, b + 1):
            row[-j] = 0
        r2 = step(step(row))
        ok = r2[-(a + 1)] == row[-(a - 1)] and r2[-(b - 1)] == row[-(b + 1)]
        ok &= all(r2[-j] == 0 for j in range(a + 2, b - 1))
        p6 &= ok
        n += 1
    print('LR-P6', 'HELD' if p6 else 'REFUTED', '(%d rows)' % n)
    degs = {j: max(sum(S) for S in moebius(lambda S, j=j: left_cells(S, 0, 17)[0][j])) for j in range(13, 18)}
    print('unexpected check: degree of f_13 .. f_17 on no-11 words', degs)


if __name__ == '__main__':
    main()
