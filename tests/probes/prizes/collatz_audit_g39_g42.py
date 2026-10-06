#!/usr/bin/env python3
"""collatz_audit_g39_g42.py: Local's independent exact check of GPT's G39 to G42 (PROOFS.md section E2), written as
the second reader's companion to an argument audit, NOT a rerun of GPT's scripts. Exact integers and fractions.
Checks, for every coefficient-admissible parity word with 3^a > 2^T and T <= 14: G39's bound
binomial(T,a)/T <= A(T,a) <= binomial(T,a); G40's skeleton cube (a surviving skeleton with F free pairs has exactly
2^F words, free meaning a mixed pair at (t, s) with 3^s > 2^(t+1)) and its swap additivity, verified EXACTLY OVER Q
(f_w(0) = f_w0(0) + sum of 3^(a-s-1) / 2^(T-t) over the free pairs oriented 01), which is stronger than G40's
statement modulo 3^a; G42's affine identity 2^T q = 3^a r + sum_odd_j 2^j 3^(a - S_(j+1)) for T <= 10 with the Terras
representative r; G42's family sum 5 * sum x_k^2 = 20480/3103353 and its cosine product; G41's frequency-boundary
valuations; and (added the same day) G43's binary-reader coefficient 2/[M(1 + e(-h/M))], its total weight bound
3 + log M and the bound 2/M at h = 2^T in G42's family; and G44's parity-tail TV r(B-r)/(BM). (Local, 2026-10-06; second readings in CHAT-LEDGER.md L007, L008.)

RUN-ON:     cpu, one core, standard library
COMMAND:    python3 tests/probes/prizes/collatz_audit_g39_g42.py
COST:       about a minute.
OUTCOME, 2026-10-06 (the first run): 1,607 admissible words to T = 14, 0 failures; 5 sum x_k^2 = 20480/3103353 =
  0.0066 exactly; product of 60 cosines 0.99350; valuations 4, 3, 2, all killed by h = 3^7 modulo 3^9.
  G43 part (second run, the same day): formula error 4e-14 for odd M < 400; weight - (3 + log M) <= 0 for every M
  tested (largest -2.43); h = 2^T weight <= 2/M for n = 0 .. 39.
  G44 part (third run, the same day): 78 cases, 0 failures.
"""
from fractions import Fraction as Fr
from itertools import combinations
from math import comb
import cmath, math
def admissible(w):
    s = 0
    for t, b in enumerate(w, 1):
        s += b
        if 3**s <= 2**t: return False
    return True
def fw0(w):  # f_w(0) over Q: odd step at 1-indexed i contributes 3^(ones after i) / 2^(T-i+1)
    T = len(w); tot = Fr(0); after = sum(w)
    for i, b in enumerate(w, 1):
        if b: after -= 1; tot += Fr(3**after, 2**(T - i + 1))
    return tot
def rep_and_q(w):  # Terras representative r in [0,2^T) and terminal integer q
    T = len(w); a = sum(w)
    for r in range(2**T):
        x, ok = r, True
        for b in w:
            if x % 2 != b: ok = False; break
            x = (3*x + 1)//2 if b else x//2
        if ok: return r, x
bad = 0; checked = 0
for T in range(2, 15):
    for a in range(T + 1):
        if 3**a <= 2**T: continue
        words = []
        for ones in combinations(range(T), a):
            w = [0]*T
            for i in ones: w[i] = 1
            words.append(tuple(w))
        A = sum(admissible(w) for w in words)
        if not (comb(T, a) <= T * A and A <= comb(T, a)): bad += 1          # G39
        # G40: skeletons
        sk = {}
        for w in words:
            if not admissible(w): continue
            key = tuple(('M' if w[i] != w[i+1] else w[i]) for i in range(0, T - T % 2, 2)) + ((w[-1],) if T % 2 else ())
            sk.setdefault(key, []).append(w)
        for key, ws in sk.items():
            # free pairs: mixed pairs with 3^s > 2^(t+1)
            free = []; s = 0
            for j, k in enumerate(key[:T // 2]):
                t = 2 * j
                if k == 'M' and 3**s > 2**(t + 1): free.append((t, s))
                s += 2 if k == 1 else (1 if k == 'M' else 0)
            if len(ws) != 2**len(free): bad += 1                              # the cube
            w0 = None
            for w in ws:
                if all(w[t] == 1 for (t, _) in free) and all(w[2*j] == 1 for j, k in enumerate(key[:T // 2]) if k == 'M'): w0 = w
            for w in ws:  # exact additivity over Q
                eta = sum(Fr(3**(a - s - 1), 2**(T - t)) for (t, s) in free if w[t] == 0)
                if fw0(w) != fw0(w0) + eta: bad += 1
            checked += len(ws)
        # G42 identity on every admissible word for T <= 10
        if T <= 10:
            for w in words:
                if not admissible(w): continue
                r, q = rep_and_q(w)
                S = 0; rhs = 3**a * r
                for j, b in enumerate(w):
                    S += b
                    if b: rhs += 2**j * 3**(a - S)
                if 2**T * q != rhs: bad += 1
print("G39/G40/G42 checks on", checked, "admissible words, T <= 14: failures =", bad)
xs = [Fr(64, 2187) * Fr(16, 27)**k for k in range(200)]
print("G42 family: 5*sum x_k^2 =", 5 * Fr(4096, 3103353) * 5 / 5, "(closed form 20480/3103353 =", float(Fr(20480, 3103353)), "); partial 200 terms", float(5 * sum(x*x for x in xs)))
prod = 1.0
for x in xs[:60]: prod *= math.cos(math.pi * float(x))
print("G42 family: product of cos(pi x_k), 60 factors =", prod)
# G41 frequency boundary example: 1111 M M M 11, h = 3^7 mod 3^9
vals = [9 - s - 1 for s in (4, 5, 6)]
print("G41 boundary: valuations", vals, "; h*Delta divisible by 3^9 for all:", all(7 + v >= 9 for v in vals))
# G43 (added 2026-10-06): the +-1 parity reader on Z/M, M odd
e = lambda x: cmath.exp(2j * math.pi * x)
worst, over = 0.0, -1e9
for M in list(range(3, 400, 2)) + [3**k for k in range(6, 10)]:
    if M < 400:
        for h in range(1, M):
            direct = sum((1 - 2 * (x % 2)) * e(-h * x / M) for x in range(M)) / M
            worst = max(worst, abs(direct - 2 / (M * (1 + e(-h / M)))))
    W = 1 / M + sum(abs(2 / (M * (1 + e(-h / M)))) for h in range(1, M))
    over = max(over, W - (3 + math.log(M)))
fam = all(abs(2 / (3**(4 + 3*n) * (1 + e(-(2**(4 + 4*n) % 3**(4 + 3*n)) / 3**(4 + 3*n))))) <= 2 / 3**(4 + 3*n) + 1e-300 for n in range(40))
print("G43: max |direct - formula| (odd M < 400):", worst, "; max (weight - (3 + log M)):", over, "; family weight <= 2/M:", fam)
# G44 (added 2026-10-06): the parity-tail TV of uniform q modulo 3^a, computed from the parity words themselves
from collections import Counter
bad44 = n44 = 0
for a in range(1, 7):
    M = 3**a
    for d in range(1, 14):
        B = 2**d; words = Counter()
        for q in range(M):
            y, w = M + q, []
            for _ in range(d):
                w.append(y & 1); y = (3 * y + 1) // 2 if y & 1 else y // 2
            words[tuple(w)] += 1
        tv = Fr(1, 2) * (sum(abs(Fr(c, M) - Fr(1, B)) for c in words.values()) + Fr(B - len(words), B))
        r = M % B
        bad44 += tv != Fr(r * (B - r), B * M)
        if B >= M: bad44 += len(words) != M or tv != 1 - Fr(M, B)
        n44 += 1
print("G44: TV = r(B-r)/(BM) and injectivity for B >= M, a = 1..6, d = 1..13:", n44, "cases, failures", bad44)

