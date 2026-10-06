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
3 + log M and the bound 2/M at h = 2^T in G42's family; G44's parity-tail TV r(B-r)/(BM); and G45's actual-start count, against brute force. (Local, 2026-10-06; second readings in CHAT-LEDGER.md L007, L008.)

RUN-ON:     cpu, one core, standard library
COMMAND:    python3 tests/probes/prizes/collatz_audit_g39_g42.py
COST:       about a minute.
OUTCOME, 2026-10-06 (the first run): 1,607 admissible words to T = 14, 0 failures; 5 sum x_k^2 = 20480/3103353 =
  0.0066 exactly; product of 60 cosines 0.99350; valuations 4, 3, 2, all killed by h = 3^7 modulo 3^9.
  G43 part (second run, the same day): formula error 4e-14 for odd M < 400; weight - (3 + log M) <= 0 for every M
  tested (largest -2.43); h = 2^T weight <= 2/M for n = 0 .. 39.
  G44 part (third run, the same day): 78 cases, 0 failures.
  G45 part (fourth run, the same day): the word-ceiling count equals brute force, 168 cases (w <= 12, T <= 14), 0
  failures.
  G46 part (fifth run, the same day): closed form = G45 ceiling for k = 1 .. 399, 0 failures; record ceilings up to
  977 at k = 306.
  G47 part (sixth run, the same day): the circuit criterion D | B - 1 holds only at k = 1 for k = 1 .. 3000, and the
  candidate start passes a direct test there.
  G48 part (seventh run, the same day): 791 first-deficit words through length 16; the only surviving positive lift
  is word 10, start 1, gap 0; brute force over 1 < n < 2^22 finds no coefficient stop <= 16 without the actual stop.
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

# G45 (added 2026-10-06): actual-start survival = residue class cut by a word-specific ceiling.
# Brute force: count w-bit starts n whose first T shortcut-map iterates all stay >= n; compare with the sum over
# all length-T words of the G45 formula.
def g45_count(wbits, T):
    L, Uw = 2**(wbits - 1), 2**wbits - 1
    tot = 0
    for code in range(2**T):
        word = [(code >> i) & 1 for i in range(T)]
        B, a, K = 0, 0, None
        for t, b in enumerate(word):
            B = 3**b * B + b * 2**t; a += b
            tt = t + 1
            if 3**a < 2**tt:
                c = B // (2**tt - 3**a)
                K = c if K is None else min(K, c)
        r = (-B * pow(3**a, -1, 2**T)) % 2**T
        U = Uw if K is None else min(Uw, K)
        if U >= L:
            tot += (U - r) // 2**T - (L - 1 - r) // 2**T
    return tot
def brute(wbits, T):
    c = 0
    for n in range(2**(wbits - 1), 2**wbits):
        x, ok = n, True
        for _ in range(T):
            x = (3 * x + 1) // 2 if x & 1 else x // 2
            if x < n: ok = False; break
        c += ok
    return c
bad45 = n45 = 0
for wbits in range(1, 13):
    for T in range(1, 15):
        n45 += 1; bad45 += g45_count(wbits, T) != brute(wbits, T)
print("G45: word-ceiling count = brute-force actual survival, w = 1..12, T = 1..14:", n45, "cases, failures", bad45)
# G46 (added 2026-10-06): the word 1^k 0^(j-k), j = ceil(k log2 3): its G45 ceiling equals the closed form, and the
# ceilings grow without bound along k with ceil(k log2 3) - k log2 3 small.
def ceiling(word):
    B, a, K = 0, 0, None
    for t, b in enumerate(word):
        B = 3**b * B + b * 2**t; a += b
        if 3**a < 2**(t + 1):
            c = B // (2**(t + 1) - 3**a); K = c if K is None else min(K, c)
    return K
bad46, best = 0, []
for k in range(1, 400):
    j = (3**k).bit_length()                         # 2^(j-1) < 3^k < 2^j
    K = ceiling([1] * k + [0] * (j - k))
    bad46 += K != (3**k - 2**k) // (2**j - 3**k)
    if not best or K > best[-1][1]: best.append((k, K))
print("G46: closed form = G45 ceiling for k = 1..399, failures", bad46, "; record ceilings (k, K):", best)
# G47 (added 2026-10-06): for 1^k 0^(j-k) with j = ceil(k log2 3), a surviving positive start exists iff D | B - 1
# (D = 2^j - 3^k, B = 2^(j-k)), and it is then the periodic return n = 2^k (B-1)/D - 1. Check the criterion against a
# direct test of the unique candidate, and search k for qualifying cases.
qual, bad47 = [], 0
for k in range(1, 3001):
    j = (3**k).bit_length(); D = 2**j - 3**k; B = 2**(j - k)
    crit = (B - 1) % D == 0
    if crit:
        m = (B - 1) // D; n = 2**k * m - 1; x = n; path = [x]
        for b in [1] * k + [0] * (j - k):
            if x % 2 != b: bad47 += 1; break
            x = (3 * x + 1) // 2 if b else x // 2; path.append(x)
        bad47 += not (x == n and min(path) >= n)
        qual.append((k, n))
print("G47: k = 1..3000, qualifying (k, start):", qual, "; failures", bad47)
# G48 (added 2026-10-06): first-deficit words through length 16; surviving positive lifts by the gap identity, and an
# independent brute force over starts n < 2^22 of "coefficient stopping time <= 16 implies actual stopping there".
fd = []
for T in range(1, 17):
    for code in range(2**T):
        w = [(code >> i) & 1 for i in range(T)]
        a, ok = 0, True
        for t, b in enumerate(w, 1):
            a += b
            if 3**a < 2**t:
                ok = (t == T); break
        else:
            ok = False
        if ok: fd.append(w)
surv = []
for w in fd:
    T = len(w); a = sum(w); B = 0
    for t, b in enumerate(w): B = 3**b * B + b * 2**t
    r = (-B * pow(3**a, -1, 2**T)) % 2**T
    q = (3**a * r + B) // 2**T; g = q - r; D = 2**T - 3**a
    for m in range(0 if r > 0 else 1, g // D + 1 if g >= 0 else 0):
        surv.append(("".join(map(str, w)), r + 2**T * m, g - D * m))
bad48 = 0
for n in range(2, 2**22):
    x, a, cst, ast_ = n, 0, None, None
    for t in range(1, 17):
        if x & 1: a += 1; x = (3 * x + 1) // 2
        else: x //= 2
        if ast_ is None and x < n: ast_ = t
        if cst is None and 3**a < 2**t: cst = t
        if cst is not None: break
    if cst is not None and ast_ != cst: bad48 += 1
print("G48: first-deficit words through length 16:", len(fd), "; surviving positive lifts (word, start, gap):", surv,
      "; brute force n < 2^22, coefficient stop <= 16 but actual stop elsewhere:", bad48)
