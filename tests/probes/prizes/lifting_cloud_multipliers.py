#!/usr/bin/env python3
"""lifting_cloud_multipliers.py: door (a), the lifting table. Door (c)'s multiplier question, asked of all four problems.

RUN-ON:     cpu (Python 3 standard library; exact integers)
COMMAND:    python3 tests/probes/prizes/lifting_cloud_multipliers.py [KE=18] [KC=24] [TR=15]
COST:       expected under a minute.

Why. CONSTELLATION.md section H, door (a): ask each problem the record's questions about the others, and mark where
the answers differ. Door (c) (RULE30-PRIZE.md 8.109) asked one question of Mahler alone. Can the admissible set meet
its own images under multiplication by 2 or 3? It cannot, except at 0, while the unrelated unit 5 keeps a density-like
share. This probe asks the same question of Erdős and Collatz, and asks its nearest analogue (time doubling) of Rule
30. RULE30-PRIZE.md 8.110 holds the table.

Settings.
- Erdős. E_k is the set of exponent residues n mod M_k = 2 * 3^(k-1) whose power 2^n mod 3^k has its last k ternary
  digits in {0, 1}. 2 is a primitive root mod 3^k, so n mod M_k fixes 2^n mod 3^k. |E_k| = 2^(k-1) (CONSTELLATION.md
  G.1, GC1240). Multiplying the exponent by e raises x = 2^n to the power e.
- Collatz. Terras's map T(x) = x/2 or (3x + 1)/2. a_j is the number of odd steps among the first j. D_k is the set of
  residues r mod 2^k with 3^(a_j) > 2^j at every j <= k: coefficient stopping time beyond k. A positive integer > 1 in
  every D_k would never drop, so the Collatz conjecture says the 2-adic set K_C = lim D_k holds none.
- Mahler. A_T as in tests/probes/mahler/mahler_cloud_two_multipliers.py, imported from it.
- Rule 30. The prize's centre column c(t) from a lone 1 on the infinite line. Rule 30 is Rule 150 XOR AND(c, r).
  Rule 150's column satisfies c(2t) = c(t) exactly, because squaring is free over GF(2). Time doubling is the nearest
  thing Rule 30 has to a multiplier.
For a set S of residues and a multiplier e, f_e is the share of S that e maps back into S, and s_e is the set of
survivors.

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  C1 (exact control): |E_k| = 2^(k-1) for k = 1 .. KE, and the lifting tree equals direct enumeration for k <= 9.
  C2 (exact control): the Collatz tree equals direct iteration of T on every residue for k <= 12.
  C3 (exact control): the Rule 30 simulator reproduces OEIS A051023's first 100 terms (the string stored in
     tests/probes/lexicon/lexicon_check.py), and Rule 150's column has c(2t) = c(t) for every t < 2^TR.
  H1 (hand, PROOF-SKETCH, derived before the run): in Erdős, s_e(k) = {0} for every e = 2 mod 3 (here 2, 5, 8, 11 and
     -1) and every k. Write x = 2^n = 1 + 3y. If y is not 0 mod 3^(k-1), its lowest nonzero digit is a 1 at some
     position m < k - 1. x^e = 1 + 3ey + 9 C(e,2) y^2 + ..., and every term after 3ey is divisible by 3^(2m+2). So
     digit m + 1 of x^e is e mod 3 = 2, with no carry from below.
  H2 (hand): in Collatz, D_k lies in 3 + 4Z for k >= 2. So f_e = 0 for every even e and every e = 3 mod 4,
     including 2 and 3, at depth 2 already.
  H3 (hand control): Collatz's own direction. y = (2x - 1)/3 is odd with T(y) = x, and it maps D_k into D_(k+1), as
     Mahler's set is invariant under 2x/3 (8.109's Lemma 1).
  P1 (0.5): Erdős e = 3 is neither anti-invariant nor generic. Cubing fixes the digits near 1: if x = 1 + 3^(m+1) w,
     then x^3 = 1 + 3^(m+2) w + O(3^(2m+3)). A count heuristic gives about 2^(k/2) survivors, so f3 falls about 1/sqrt 2
     a step: ratios between 0.68 and 0.74 over k = 10 .. KE. The random baseline is 2/3.
  P2 (0.5): Erdős e = 1 mod 3 (here 4, 7 and 13) is density-like. f_e is within a factor 3 of the baseline
     (2/3)^(k-1) at k = KE.
  P3 (0.6): Collatz e = 1 mod 4 (5, 9, 13, -3) is density-like. At k = KC, f_e is within a factor 3 of D_k's density in
     3 + 4Z, which is |D_k| / 2^(k-2).
  P4 (0.5): Mahler. Besides 2 and 3, the products 4, 6 and 9 are anti-invariant, with only 0's shadows surviving.
     5, 7 and -1 are density-like.
  U, the unexpected check (0.8): Rule 30's column keeps no trace of Rule 150's time doubling. c(2t) = c(t) on a share
     of t in [1, 2^TR) within 0.5 +- 0.01.
  Counterfactuals. If H1 failed, the hand proof would be wrong. If U lay outside 0.49 .. 0.51, the AND would keep a
  trace of the linear part's Frobenius symmetry, and that would be a lever worth a door of its own. If P1 lay at 2/3,
  cubing would be generic after all.
"""
import importlib.util
import pathlib
import sys

ARGS = [int(a) for a in sys.argv[1:] if a.lstrip('-').isdigit()]
KE = ARGS[0] if len(ARGS) > 0 else 18
KC = ARGS[1] if len(ARGS) > 1 else 24
TR = ARGS[2] if len(ARGS) > 2 else 15
A051023 = ("1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,"
           "0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1")


def share(S, e, m):
    surv = {r for r in S if (e * r) % m in S}
    return len(surv) / len(S), surv


# ---- Erdős ---------------------------------------------------------------------------------------------------------
def erdos_tree(K):
    E = {1: {0}}                     # M_1 = 2; 2^n = 1 mod 3 exactly when n is even
    for k in range(1, K):
        M, p = 2 * 3 ** (k - 1), 3 ** (k + 1)
        E[k + 1] = {n + j * M for n in E[k] for j in range(3) if (pow(2, n + j * M, p) // 3 ** k) % 3 < 2}
    return E


def free_digits(x, k):
    for _ in range(k):
        if x % 3 == 2:
            return False
        x //= 3
    return True


def erdos():
    E = erdos_tree(KE)
    sizes_ok = all(len(E[k]) == 2 ** (k - 1) for k in range(1, KE + 1))
    direct_ok = all(E[k] == {n for n in range(2 * 3 ** (k - 1)) if free_digits(pow(2, n, 3 ** k), k)}
                    for k in range(1, 10))
    print('C1 |E_k| = 2^(k-1) for k = 1..%d: %s; tree = direct enumeration for k <= 9: %s' % (KE, sizes_ok, direct_ok))
    es = (2, 5, 8, 11, -1, 3, 4, 7, 13)
    print('\nErdős f_e (share of E_k kept by n -> e n), survivors |s_e|, and the baseline (2/3)^(k-1)')
    print('  k  ' + ''.join('%10s' % ('e=%d' % e) for e in es) + '    |s_3|    base')
    h1, f = True, {}
    for k in range(2, KE + 1):
        M = 2 * 3 ** (k - 1)
        row = {}
        for e in es:
            row[e], surv = share(E[k], e, M)
            if e % 3 == 2:
                h1 &= surv == {0}
            if e == 3:
                n3 = len(surv)
        f[k] = row
        print('%3d  ' % k + ''.join('%10.6f' % row[e] for e in es) + '%9d  %.6f' % (n3, (2 / 3) ** (k - 1)))
    print('\nH1 s_e(k) = {0} for e = 2, 5, 8, 11, -1 and every k = 2..%d: %s' % (KE, h1))
    r3 = [f[k + 1][3] / f[k][3] for k in range(10, KE)]
    print('P1 f3 step ratios over k = 10..%d: %s' % (KE, ' '.join('%.3f' % r for r in r3)))
    for e in (4, 7, 13):
        print('P2 e = %d: f_e / baseline at k = %d: %.2f' % (e, KE, f[KE][e] / (2 / 3) ** (KE - 1)))
    return E


# ---- Collatz -------------------------------------------------------------------------------------------------------
def collatz_tree(K):
    """D[k] as residues; each node carries (r, v = T^k(r) as an integer, a = odd steps so far)."""
    level = [(0, 0, 0)]
    D = {}
    for k in range(K):
        nxt = []
        for r, v, a in level:
            for rr, vv in ((r, v), (r + (1 << k), v + 3 ** a)):
                b = vv & 1
                v2 = (3 * vv + 1) // 2 if b else vv // 2
                if 3 ** (a + b) > 1 << (k + 1):
                    nxt.append((rr, v2, a + b))
        level = nxt
        D[k + 1] = {r for r, _, _ in level}
    return D


def collatz_direct(r, k):
    x, a = r, 0
    for j in range(1, k + 1):
        if x & 1:
            x, a = (3 * x + 1) // 2, a + 1
        else:
            x //= 2
        if 3 ** a <= 1 << j:
            return False
    return True


def collatz():
    D = collatz_tree(KC)
    c2 = all(D[k] == {r for r in range(1 << k) if collatz_direct(r, k)} for k in range(1, 13))
    print('\nC2 Collatz tree = direct iteration for k <= 12: %s' % c2)
    h2 = all(all(r % 4 == 3 for r in D[k]) for k in range(2, KC + 1))
    h3 = all({((2 * r - 1) * pow(3, -1, 1 << (k + 1))) % (1 << (k + 1)) for r in D[k]} <= D[k + 1]
             for k in range(1, KC))
    print('H2 D_k lies in 3 + 4Z for k = 2..%d: %s' % (KC, h2))
    print('H3 y = (2x - 1)/3 maps D_k into D_(k+1) for k = 1..%d: %s' % (KC - 1, h3))
    es = (2, 3, 7, -1, 5, 9, 13, -3)
    print('\nCollatz f_e and |D_k| / 2^(k-2) (density inside 3 + 4Z)')
    print('  k    |D_k|  ' + ''.join('%9s' % ('e=%d' % e) for e in es) + '    dens')
    for k in range(2, KC + 1):
        m = 1 << k
        row = {e: share(D[k], e, m)[0] for e in es}
        dens = len(D[k]) / (1 << (k - 2))
        if k % 2 == 0 or k == KC:
            print('%3d %8d  ' % (k, len(D[k])) + ''.join('%9.5f' % row[e] for e in es) + '  %.5f' % dens)
    print('P3 at k = %d, f_e / density: %s' % (KC, ', '.join('e=%d: %.2f' % (e, row[e] / dens) for e in (5, 9, 13, -3))))


# ---- Mahler --------------------------------------------------------------------------------------------------------
def mahler(TM=20):
    path = pathlib.Path(__file__).resolve().parents[1] / 'mahler' / 'mahler_cloud_two_multipliers.py'
    spec = importlib.util.spec_from_file_location('tm', path)
    tm = importlib.util.module_from_spec(spec)
    saved, sys.argv = sys.argv, [sys.argv[0]]
    spec.loader.exec_module(tm)
    sys.argv = saved
    es = (2, 3, 4, 6, 9, 5, 7, -1)
    print('\nMahler f_e on A_T, and survivors that are not 0 or 2^(T-1)')
    print('  T   |A_T|  ' + ''.join('%9s' % ('e=%d' % e) for e in es) + '   extra survivors for 4, 6, 9')
    for T in range(2, TM + 1):
        m = 1 << T
        S = {tm.residue(p) for p in tm.admissible(T)}
        row, extra = {}, {}
        for e in es:
            row[e], surv = share(S, e, m)
            if e in (4, 6, 9):
                extra[e] = len(surv - {0, 1 << (T - 1)})
        if T % 2 == 0:
            print('%3d %6d  ' % (T, len(S)) + ''.join('%9.5f' % row[e] for e in es) + '   %s' % extra)


# ---- Rule 30 -------------------------------------------------------------------------------------------------------
def columns(N):
    mask = (1 << (2 * N + 3)) - 1
    r30 = r150 = 1 << (N + 1)
    c30, c150 = [], []
    for _ in range(N + 1):
        c30.append((r30 >> (N + 1)) & 1)
        c150.append((r150 >> (N + 1)) & 1)
        r30 = ((r30 << 1) ^ (r30 | (r30 >> 1))) & mask
        r150 = ((r150 << 1) ^ r150 ^ (r150 >> 1)) & mask
    return c30, c150


def rule30():
    N = 1 << (TR + 1)
    c30, c150 = columns(N)
    ref = [int(x) for x in A051023.split(',')]
    print('\nC3 Rule 30 column = OEIS A051023 (%d terms): %s' % (len(ref), c30[:len(ref)] == ref))
    half = 1 << TR
    print('C3 Rule 150 column: c(2t) = c(t) for every t < 2^%d: %s' % (TR, all(c150[2 * t] == c150[t] for t in range(half))))
    agree = sum(c30[2 * t] == c30[t] for t in range(1, half)) / (half - 1)
    agree3 = sum(c30[3 * t] == c30[t] for t in range(1, N // 3)) / (N // 3 - 1)
    print('U  Rule 30: share of t in [1, 2^%d) with c(2t) = c(t): %.4f   (c(3t) = c(t), t < %d: %.4f)'
          % (TR, agree, N // 3, agree3))


if __name__ == '__main__':
    erdos()
    collatz()
    mahler()
    rule30()
