"""rule30_audit_g60_g66.py: Local's checks of GPT's G60 to G66 (the Rule 210 right-realization and strip chain), the
second reader's companion to argument audits, independent of GPT's controls. (Local, 2026-10-06; PROOFS.md notes;
chat L035.)
COMMAND:    python3 tests/probes/lexicon/rule30_audit_g60_g66.py      (about a minute)
OUTCOME, 2026-10-06: ALL CHECKS PASS (G60 wall, G61/G62 tables, transitions, G63 lemma 15/15, G64 template 2,554, G65 mirror,
  G66 localization 240,116).
"""
import random
from math import comb
random.seed(20261006)
f210 = lambda l, c, r: l ^ r ^ (c & r)
fails = 0

# G60: build v by the binomial recursion and evolve full Rule 210 from the odd-supported seed; the centre must be tau.
for trial in range(12):
    q = random.choice([1, 2, 3, 4]); base = [random.randint(0, 1) for _ in range(q)]
    if not any(base): base[0] = 1
    N = 60; a = [base[n % q] for n in range(N)]
    v = []
    for n in range(N):
        acc = a[n]
        for j in range(n): acc ^= (comb(2 * n + 1, n - j) & 1) & v[j]
        v.append(acc)
    T = 2 * N; W = 2 * T + 10; c = T + 5
    x = [0] * W
    for j in range(N): x[c + 2 * j + 1] = v[j]
    for t in range(T):
        tau_t = 0 if t % 2 == 0 else a[(t - 1) // 2]
        fails += x[c] != tau_t
        x = [f210(x[i - 1] if i else 0, x[i], x[i + 1] if i + 1 < W else 0) for i in range(W)]
print("G60: full Rule 210 from the recursion's seed reproduces the wall (12 periodic inputs, 120 steps)")

# G61: exhaustive truth table for the two column-1 updates under the 0101 wall.
acc = set()
for s in (0, 1):
    for d in (0, 1):
        for sn in (0, 1):
            ok = any(f210(0, s, b) == d and f210(1, d, cc) == sn for b in (0, 1) for cc in (0, 1))
            fails += ok != (d == 0 or (s == 0 and sn == 1))
# G62: with column 2's update, odd pairs never, even pairs force s_next = 0.
for s in (0, 1):
    for b in (0, 1):
        for qq in (0, 1):
            for z in (0, 1):
                d = f210(0, s, b); cc = f210(s, b, qq); sn = f210(1, d, cc)
                fails += d & cc
                if s & b: fails += sn != 0
# G26 transitions: s_0 = 1, s_n = floor(log2 n) mod 2.
s = [1] + [(n.bit_length() - 1) % 2 for n in range(1, 5000)]
ups = [n for n in range(4999) if s[n] == 0 and s[n + 1] == 1]
downs = [n for n in range(4999) if s[n] == 1 and s[n + 1] == 0]
fails += ups != [2 ** (2 * r + 1) - 1 for r in range(len(ups))]
fails += downs != [4 ** r - 1 for r in range(len(downs))]
print("G61/G62: truth tables exhaustive; G26 up-transitions", ups[:5], "down-transitions", downs[:6])

# G63: the local extension lemma, exhaustively. For disjoint-phase L, C in {00, 10, 01} (pairs = (even, odd)), every R
# word on [0, 7] that satisfies C's updates and admits a farther column F for R's updates must equal swap(C) xor L on
# [2, 5].
pairs = [(0, 0), (1, 0), (0, 1)]
val = lambda pr, t: pr[t % 2]
acc_total = 0
for L in pairs:
    for C in pairs:
        if L[0] & C[0] or L[1] & C[1]: continue
        for Rw in range(256):
            R = [(Rw >> t) & 1 for t in range(8)]
            if any(f210(val(L, t), val(C, t), R[t]) != val(C, t + 1) for t in range(7)): continue
            if not any(all(f210(val(C, t), R[t], (Fw >> t) & 1) == R[t + 1] for t in range(7)) for Fw in range(128)): continue
            acc_total += 1
            want = (C[1] ^ L[0], C[0] ^ L[1])
            fails += any(R[t] != want[t % 2] for t in range(2, 6))
cyc = {}
for a in (0, 1):
    v = [(0, 1), (a, 0)]
    for k in range(2, 14): v.append((v[-1][1] ^ v[-2][0], v[-1][0] ^ v[-2][1]))
    fails += v[6:12] != v[0:6]
    cyc[a] = ["%d%d" % x for x in v[:6]]
print("G63: lemma exhaustive,", acc_total, "accepted local R words, all forced on [2,5]; cycles", cyc)

# G64: on a real full realization (G60's construction for the 0101 wall), column k matches the forced template at
# every time outside radius 2k of the dyadic boundaries {2^j - 1} and the virtual -1.
N = 300; a = [1] * N; v = []
for n in range(N):
    acc_ = a[n]
    for j in range(n): acc_ ^= (comb(2 * n + 1, n - j) & 1) & v[j]
    v.append(acc_)
T = 2 * N; W = 2 * T + 10; c0 = T + 5
x = [0] * W
for j in range(N): x[c0 + 2 * j + 1] = v[j]
rows = []
for t in range(T):
    rows.append(x[:])
    x = [f210(x[i - 1] if i else 0, x[i], x[i + 1] if i + 1 < W else 0) for i in range(W)]
sstream = [1] + [(n.bit_length() - 1) % 2 for n in range(1, N + 2)]
B = [-1] + [2 ** j - 1 for j in range(1, 12)]
checked = 0
for k in range(1, 6):
    for t in range(T - 4):
        if min(abs(t - b) for b in B) <= 2 * k: continue
        n = t // 2
        va = [(0, 1), (sstream[n], 0)]
        for kk in range(2, k + 1): va.append((va[-1][1] ^ va[-2][0], va[-1][0] ^ va[-2][1]))
        fails += rows[t][c0 + k] != va[k][t % 2]; checked += 1
print("G64: forced template matches a full G60 realization at", checked, "samples (columns 1..5, t < 596)")

# G65: G60's seed for the 0101 wall XOR a mirrored finite odd-depth left row keeps the wall under full Rule 210; the
# union-language count formula; the mixed-parity guard {1} versus {-2, 1, 2}.
N2 = 40; a2 = [1] * N2; h = []
for n in range(N2):
    acc_ = a2[n]
    for j in range(n): acc_ ^= (comb(2 * n + 1, n - j) & 1) & h[j]
    h.append(acc_)
for trial in range(20):
    e = [random.randint(0, 1) for _ in range(6)]
    T2 = 2 * N2; W2 = 2 * T2 + 20; cc = T2 + 10
    xx = [0] * W2
    for j in range(N2): xx[cc + 2 * j + 1] = h[j] ^ (e[j] if j < len(e) else 0)
    for j, ej in enumerate(e): xx[cc - (2 * j + 1)] = ej
    for t in range(T2 - 2):
        fails += xx[cc] != t % 2
        xx = [f210(xx[i - 1] if i else 0, xx[i], xx[i + 1] if i + 1 < W2 else 0) for i in range(W2)]
fails += [2 ** ((n + 1) // 2) + 2 ** (n // 2) - 1 for n in range(1, 9)] != [2, 3, 5, 7, 11, 15, 23, 31]
def centre2(seed):
    W3 = 21; c3 = 10; z = [0] * W3
    for i in seed: z[c3 + i] = 1
    for _ in range(2): z = [f210(z[i - 1] if i else 0, z[i], z[i + 1] if i + 1 < W3 else 0) for i in range(W3)]
    return z[c3]
fails += (centre2([1]), centre2([-2, 1, 2])) != (0, 1)
print("G65: mirrored left rows keep the 0101 wall (20 rows, 78 steps); counts 2,3,5,7,11,15,23,31; guard centre", (centre2([1]), centre2([-2, 1, 2])))

# G66: for random finite E in [-R, R], (A^t E)(i) = 0 whenever 2^(q+1) - t > R + |i| (2^q <= t < 2^(q+1)).
zero_checked = 0
for trial in range(40):
    R = random.randint(1, 8); W4 = 2 * 600 + 2 * R + 10; c4 = W4 // 2
    y = [0] * W4
    for i in range(-R, R + 1): y[c4 + i] = random.randint(0, 1)
    for t in range(1, 512):
        y = [(y[i - 1] if i else 0) ^ (y[i + 1] if i + 1 < W4 else 0) for i in range(W4)]
        q = t.bit_length() - 1
        for i in range(-6, 7):
            if (1 << (q + 1)) - t > R + abs(i):
                fails += y[c4 + i]; zero_checked += 1
print("G66: Rule 90 localization near powers of two,", zero_checked, "predicted zeros checked")
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
