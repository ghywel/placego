"""rule30_audit_g53_g54.py: Local's check of GPT's G53 (period-block entropy conversion) and G54 (the gap-matrix
coarse squeeze for every periodic wall), the second reader's companion to an argument audit. It recomputes G54's
examples from G15's gap matrices (A for gap 1, F for gap 2, J for gaps >= 3): the wall 0^7 1 against G14's recorded
visible rate 0.354491897 bits per physical step, the period-8 walls 00111111 and 01101111 (roots 3 and 4), the
one-hole walls (1/p), 0101 (log2 of the golden ratio over 2), the cyclic invariance of the spectral radius, and
G53's 001 example (all white bits 0 give column -1 = 011 whatever the black-phase bits are). (Local, 2026-10-06;
PROOFS.md G53/G54 notes; chat L026.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g53_g54.py      (a second)
OUTCOME, 2026-10-06: ALL CHECKS PASS (0^7 1 gives 0.354491897 = G14; roots 3 and 4; 1/p; log2(phi)/2; the 001 example).
"""
import math
import numpy as np

A = np.array([[1, 1], [0, 1]]); F = np.array([[1, 1], [1, 0]]); J = np.array([[1, 1], [1, 1]])
B = lambda g: A if g == 1 else (F if g == 2 else J)


def bound(word):
    p = len(word); whites = [i for i in range(p) if word[i] == '0']
    gaps = [(whites[(k + 1) % len(whites)] - whites[k]) % p or p for k in range(len(whites))]
    rhos = []
    for s in range(len(gaps)):                     # every cyclic starting point
        M = np.eye(2, dtype=np.int64)
        for g in gaps[s:] + gaps[:s]: M = M @ B(g)
        t, d = M[0, 0] + M[1, 1], M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        rhos.append((t + math.sqrt(t * t - 4 * d)) / 2)
    return math.log2(rhos[0]) / p, max(rhos) - min(rhos), gaps


fails = 0
b, spread, _ = bound('00000001'); print("0^7 1:", round(b, 9), "against G14's 0.354491897; cyclic spread", spread); fails += abs(b - 0.354491897) > 1e-9
b, _, g = bound('00111111'); print("00111111: gaps", g, "bound", b, "= log2(3)/8:", abs(b - math.log2(3) / 8) < 1e-12); fails += abs(b - math.log2(3) / 8) > 1e-12
b, _, g = bound('01101111'); print("01101111: gaps", g, "bound", b, "= 2/8:", abs(b - 0.25) < 1e-12); fails += abs(b - 0.25) > 1e-12
for p in (3, 4, 5, 8):
    b, _, _ = bound('0' + '1' * (p - 1)); fails += abs(b - 1 / p) > 1e-12
b, _, _ = bound('01'); print("0101: bound", round(b, 6), "= log2(phi)/2:", abs(b - math.log2((1 + 5 ** 0.5) / 2) / 2) < 1e-12)
fails += abs(b - math.log2((1 + 5 ** 0.5) / 2) / 2) > 1e-12
for p in range(3, 12):                              # 0^(p-1) 1 closed form
    b, _, _ = bound('0' * (p - 1) + '1'); fails += abs(b - math.log2(((p - 1) + math.sqrt((p - 1) ** 2 + 4)) / 2) / p) > 1e-12
tau = [0, 0, 1]
outs = set()
for blackbits in range(2**10):
    pi = []
    for t in range(30):
        sigma = 0 if tau[t % 3] == 0 else (blackbits >> (t // 3)) & 1
        pi.append(tau[(t + 1) % 3] ^ (tau[t % 3] | sigma))
    outs.add(tuple(pi))
print("001, white bits 0, 1024 black-phase choices: distinct column -1 words", len(outs), "first period", list(outs)[0][:3])
fails += len(outs) != 1 or list(outs)[0][:3] != (0, 1, 1)
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
