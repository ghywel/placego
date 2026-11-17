#!/usr/bin/env python3
"""collatz_audit_g83_g89.py: Local's second reading of GPT's G83 to G90 (forced spacing, prefix orientation, the
paired-prefix certificate, the first admitted collision at odd count 22, and the weighted-class guard), by a method
GPT did not use: every admitted word is enumerated (39,993,895 of them at a = 22) and every same-count collision is
found from the intercepts, with no pruning. Exact integers only. (Local, 2026-10-06; PROOFS.md notes; chat.)

RUN-ON:     cpu (collatz_fibres.c via cc; Python 3 standard library)
COMMAND:    python3 tests/probes/prizes/collatz_audit_g83_g89.py [AMAX=22] [--extend]   (--extend adds a = 23)
COST:       about a minute at AMAX = 22 on one core; a = 23 adds about a minute and 1.4 GB.

CHECKS, GPT's claims as stated at ca9d765 and 23c22c2, written before this script's first full run (while building,
the engine was smoked to a = 17, reproducing L043's counts and no collision, and its unrestricted mode was run at a = 3
to 8; neither touches a = 18 to 23):
  K1 (G81-G89, the classification): no realized same-count admitted collision for a <= 21; at a = 22 exactly five,
     the pairs of G89's table (smaller start, start + 4, common terminal after 34 steps), each meeting first at step 34,
     both starts of one width, every check of the direct evolution exact.
  K2 (G83, G67): over W_a the least intercept is 3^a - 2^a and the greatest is G67's B_max, for a = 1..22; R_a is
     increasing for a >= 2, R_a <= a/3 - 1 + (2/3)^a for a = 1..64, R_20 < 4 < R_21 with G83's fractions, R_22 < 8.
  K3 (G84, G87): the prefix extrema min B_110 = 13*3^a/9 - 2^(a+1), max B_111 = B_max - 4*3^(a-3) (a >= 3),
     max B_110111 = B_max - 32*3^(a-5), min B_111110 = 3^a + 32*3^(a-5) - 2^(a+1) (a >= 5) are attained, checked on
     every admitted word for a <= 14; G84's a = 21 numerator 37365342780 and G87's 40809080460 < 4*3^21.
  K4 (G89's displayed identities): 2^34*9770112830 = 3^22*5348744187 + 166780787837 = 3^22*5348744191 + 41256549401,
     the two parity words, 22 odd steps each, admission at all 34 prefixes; the lift k*2^34 for k = 1..3.
  K5 (G90): starts 11843133435 and 11843133439 have odd counts 21 and 22 after 33 steps, 22 and 22 after 34, a common
     terminal 21632881628; backward weights f_33(21) = 1/2, f_33(22) = 1; literal changes 1/2 and 0.
  C1 (positive control, must be seen): the unrestricted words (no admission) at a = 3..8 give exactly the meeting pairs
     of a direct scan of all starts below 2^(t+1).
  K6 (G86): the 33-bit slack word is admitted; its 27-bit suffix first fails the fresh barrier at 26 and is admitted
     against the shifted one. K7 (G88): the completion extrema are attained for every admitted prefix, a = 2..11.
  X1 (extension, --extend, blind): a = 23 has more realized pairs than a = 22.
  (K6 and K7 were added after the first full run, which had K1 to K5, C1 and X1.)

OUTCOME, 2026-10-06 (AMAX = 22 with --extend; M5, one core, 14 s): ALL CHECKS PASS. |W_a| for a = 18..23: 663,535,
1,900,470, 5,936,673, 13,472,296, 39,993,895, 87,986,917. No realized collision for a <= 21; at a = 22 exactly G89's
five pairs, displacement 4, equal widths, first meeting at 34; all five lower starts are 251 mod 256 with prefixes
11011011 / 11111111 (G87's a = 21 necessity holds at a = 22 as well; four pairs have ninth bits 0 / 1, one 1 / 0).
X1 HELD: a = 23 has 20 realized pairs, all displacement 4, equal widths, exact; NONE first meets at its horizon 36
(15 first meet at step 35, 5 at step 34), so at a = 23 every collision is a shorter-horizon meeting padded by later
common bits. The first full run marked all twenty "not ok": its ok flag also required a first meeting at step t,
which is right for G89's a = 22 claim and wrong for the extension; the flag was split (exactness, first-meeting step)
and the run repeated, with the same pairs.
"""
import math
import os
import subprocess
import sys
import tempfile
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
EXE = os.path.join(tempfile.gettempdir(), 'collatz_fibres_audit')
subprocess.run(['cc', '-O3', '-o', EXE, os.path.join(HERE, 'collatz_fibres.c')], check=True)
fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


def t_of(a):
    return (3 ** a).bit_length() - 1


def bmax(a):
    return sum(3 ** (a - 1 - i) * 2 ** ((3 ** i).bit_length() - 1) for i in range(a))


def T(n):
    return (3 * n + 1) // 2 if n & 1 else n // 2


def word_of(n, t):
    w, odd = [], 0
    for _ in range(t):
        w.append(n & 1)
        n = T(n)
    return w, n


def admitted(w):
    a = 0
    for L, b in enumerate(w, 1):
        a += b
        if 3 ** a < 2 ** L:
            return False
    return True


def run(amin, amax, free=False):
    args = [EXE, str(amin), str(amax)] + (['free'] if free else [])
    out = subprocess.run(args, capture_output=True, check=True, text=True).stdout
    ext, summ, pairs = {}, {}, {}
    for line in out.split('\n'):
        f = line.split()
        if not f:
            continue
        if f[0] == 'EXT':
            ext[int(f[1])] = (int(f[2]), int(f[3]))
        elif f[0] == 'A':
            summ[int(f[1])] = dict(words=int(f[5]), res=int(f[7]), pairs=int(f[9]), realized=int(f[11]))
        elif f[0] == 'PAIR':
            a = int(f[1])
            pairs.setdefault(a, []).append((int(f[2]), int(f[3]), int(f[4]), int(f[5]), int(f[7]), int(f[8]), int(f[10]),
                                            int(f[12])))
    return ext, summ, pairs


# C1: the positive control
for a in range(3, 9):
    t = t_of(a)
    _, summ, pairs = run(a, a, free=True)
    mine = sorted((p[0], p[1]) for p in pairs.get(a, []))
    byterm = {}
    for n in range(0, 2 ** (t + 1)):
        w, m = word_of(n, t)
        if sum(w) == a:
            byterm.setdefault(m, []).append(n)
    scan = sorted((x, y) for v in byterm.values() for x in v for y in v if x < y and x < 2 ** t)
    check('C1 a=%d unrestricted pairs = direct scan' % a, mine == scan, '%d pairs' % len(scan))

# K1, K2: the classification and the extrema
amax = int([x for x in sys.argv[1:] if not x.startswith('--')][0]) if [x for x in sys.argv[1:] if not x.startswith('--')] else 22
ext, summ, pairs = run(1, amax)
for a in range(1, amax + 1):
    print('a=%2d t=%2d |W_a|=%10d colliding residues %d realized %d' % (a, t_of(a), summ[a]['words'], summ[a]['res'],
                                                                         summ[a]['realized']))
check('K1 no realized collision for a <= 21', all(summ[a]['realized'] == 0 for a in range(1, min(amax, 21) + 1)))
G89 = [(5348744187, 5348744191, 9770112830), (7435082747, 7435082751, 13581056558),
       (11843133435, 11843133439, 21632881628), (15231450875, 15231450879, 27822043514),
       (15257926651, 15257926655, 27870404645)]
if amax >= 22:
    got = sorted((p[0], p[1], p[2]) for p in pairs.get(22, []))
    check('K1 a=22: exactly the five pairs of G89', got == sorted(G89), str(got))
    check('K1 a=22: displacement 4, equal widths, direct evolution exact, first meeting at 34',
          all(p[3] == 4 and p[4] == p[5] and p[6] == 1 and p[7] == 34 for p in pairs[22]))
    for p in sorted(pairs[22]):
        wl, _ = word_of(p[0], 34)
        wu, _ = word_of(p[1], 34)
        print('  pair %d / %d: prefixes %s / %s, lower start mod 256 = %d' % (p[0], p[1], ''.join(map(str, wl[:9])),
                                                                             ''.join(map(str, wu[:9])), p[0] % 256))
check('K2 least intercept 3^a - 2^a', all(ext[a][0] == 3 ** a - 2 ** a for a in range(1, amax + 1)))
check('K2 greatest intercept B_max (G67)', all(ext[a][1] == bmax(a) for a in range(1, amax + 1)))
R = {a: Fr(bmax(a) - (3 ** a - 2 ** a), 3 ** a) for a in range(1, 65)}
check('K2 R_a increasing for a >= 2', all(R[a + 1] > R[a] for a in range(2, 64)))
check('K2 R_a <= a/3 - 1 + (2/3)^a', all(R[a] <= Fr(a, 3) - 1 + Fr(2, 3) ** a for a in range(1, 65)))
check('K2 R_20, R_21 fractions and R_20 < 4 < R_21, R_22 < 8',
      R[20] == Fr(13805179460, 3486784401) and R[21] == Fr(43561973452, 10460353203) and R[20] < 4 < R[21] and R[22] < 8,
      'R_22 = %.4f' % float(R[22]))

# K3: prefix extrema on every admitted word for a <= 14
def words(a):
    caps = [(3 ** i).bit_length() - 1 for i in range(a)]
    t = t_of(a)
    out = []
    def go(i, prev, ps):
        if i == a:
            w = [0] * t
            for p in ps:
                w[p] = 1
            out.append(w)
            return
        for p in range(0 if i == 0 else prev + 1, caps[i] + 1):
            go(i + 1, p, ps + [p])
    go(0, -1, [])
    return out


def B_of(w):
    B = 0
    for L, b in enumerate(w):
        if b:
            B = 3 * B + 2 ** L
    return B


ok3 = True
for a in range(3, 15):
    W = words(a)
    by = lambda pre: [B_of(w) for w in W if w[:len(pre)] == pre]
    ok3 &= min(by([1, 1, 0])) == 13 * 3 ** a // 9 - 2 ** (a + 1) and max(by([1, 1, 1])) == bmax(a) - 4 * 3 ** (a - 3)
    if a >= 5:
        ok3 &= max(by([1, 1, 0, 1, 1, 1])) == bmax(a) - 32 * 3 ** (a - 5)
        ok3 &= min(by([1, 1, 1, 1, 1, 0])) == 3 ** a + 32 * 3 ** (a - 5) - 2 ** (a + 1)
    ok3 &= all(admitted(w) for w in W)
check('K3 four prefix extrema attained on every admitted word, a = 3..14 (and every enumerated word admitted)', ok3)
a = 21
n84 = (R[a] - Fr(16, 27) + Fr(2, 3) ** a) * 3 ** a
n87 = (R[a] - Fr(64, 243) + Fr(2, 3) ** a) * 3 ** a
check('K3 G84 numerator 37365342780 and G87 numerator 40809080460 < 4*3^21',
      n84 == 37365342780 and n87 == 40809080460 and n87 < 4 * 3 ** 21, '%s %s' % (n84, n87))

# K4: G89's displayed identities and lifts
wa, ta = word_of(5348744187, 34)
wb, tb = word_of(5348744191, 34)
ok4 = (2 ** 34 * 9770112830 == 3 ** 22 * 5348744187 + 166780787837 == 3 ** 22 * 5348744191 + 41256549401 and
       ''.join(map(str, wa)) == '1101101101011011100110110110101101' and
       ''.join(map(str, wb)) == '1111111111011100100111011100001100' and sum(wa) == sum(wb) == 22 and
       admitted(wa) and admitted(wb) and ta == tb == 9770112830 and B_of(wa) == 166780787837 and
       B_of(wb) == 41256549401 and 166780787837 - 41256549401 == 4 * 3 ** 22)
for k in range(1, 4):
    x, y = word_of(5348744187 + k * 2 ** 34, 34), word_of(5348744191 + k * 2 ** 34, 34)
    ok4 &= x[0] == wa and y[0] == wb and x[1] == y[1] == 9770112830 + k * 3 ** 22
check('K4 G89 identities, words, admission, lifts k = 1..3', ok4)

# K5: G90
w1, m1 = word_of(11843133435, 34)
w2, m2 = word_of(11843133439, 34)
f34 = lambda c: Fr(1) if c >= 22 else Fr(0)
f33 = lambda c: (f34(c) + f34(c + 1)) / 2
c1, c2 = sum(w1[:33]), sum(w2[:33])
ok5 = (c1, c2) == (21, 22) and sum(w1) == sum(w2) == 22 and m1 == m2 == 21632881628
ok5 &= f33(21) == Fr(1, 2) and f33(22) == 1 and f34(22) - f33(21) == Fr(1, 2) and f34(22) - f33(22) == 0
ok5 &= (11843133435).bit_length() == (11843133439).bit_length() == 34
check('K5 G90 classes 21/22 then 22/22, common terminal, weights 1/2 and 1, literal changes 1/2 and 0', ok5)

# K6 (G86): the slack guard; K7 (G88): the completion extrema against every admitted prefix for a <= 11
def first_fail(w, j0=0, s0=0):
    c = j0
    for L, b in enumerate(w, 1):
        c += b
        if 3 ** c < 2 ** (s0 + L):
            return L
    return None


gw = [1, 1, 0, 1, 1, 1] + [1] * 16 + [0] * 11
suf = [1] * 16 + [0] * 11
check('K6 G86 word (33 bits, 21 ones) admitted; suffix fails fresh at 26, admitted against the shifted barrier',
      len(gw) == 33 and sum(gw) == 21 and first_fail(gw) is None and first_fail(suf) == 26 and first_fail(suf, 5, 6) is None)
n7 = bad7 = 0
for a in range(2, 12):
    t = t_of(a)
    for s in range(1, t + 1):
        groups = {}
        for w in words(a):
            ps = [i for i, b in enumerate(w) if b]
            groups.setdefault(tuple(p for p in ps if p < s), []).append(B_of(w))
        for pre, bs in groups.items():
            j = len(pre)
            Bp = sum(3 ** (j - 1 - i) * 2 ** p for i, p in enumerate(pre))
            lo = 3 ** (a - j) * Bp + 2 ** s * (3 ** (a - j) - 2 ** (a - j))
            hi = 3 ** (a - j) * Bp + sum(3 ** (a - 1 - i) * 2 ** ((3 ** i).bit_length() - 1) for i in range(j, a))
            n7 += 1
            bad7 += min(bs) != lo or max(bs) != hi
check('K7 G88 completion extrema attained for every admitted prefix, a = 2..11', bad7 == 0, '%d prefixes' % n7)

if '--extend' in sys.argv:
    ext23, summ23, pairs23 = run(23, 23)
    s = summ23[23]
    print('a=23 t=%d |W_a|=%d colliding residues %d realized %d' % (t_of(23), s['words'], s['res'], s['realized']))
    for p in sorted(pairs23.get(23, [])):
        print('  pair', p[0], p[1], 'terminal', p[2], 'delta', p[3], 'widths', p[4], p[5], 'ok', p[6], 'first meet', p[7])
    check('X1 a=23 has more realized pairs than a=22', s['realized'] > 5, str(s['realized']))
    check('X1 every a=23 pair exact (direct evolution, odd counts, terminal, 128-bit identity)',
          all(p[6] == 1 for p in pairs23.get(23, [])))
    meets = sorted(p[7] for p in pairs23.get(23, []))
    print('  a=23 first-meeting steps:', {m: meets.count(m) for m in set(meets)}, '; equal widths:',
          all(p[4] == p[5] for p in pairs23.get(23, [])))

print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
