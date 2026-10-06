"""rule30_audit_g60_g66.py: Local's checks of GPT's G60 to G66 (the Rule 210 right-realization and strip chain), the
second reader's companion to argument audits, independent of GPT's controls. (Local, 2026-10-06; PROOFS.md notes;
chat L035.)
COMMAND:    python3 tests/probes/lexicon/rule30_audit_g60_g66.py      (seconds)
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
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
