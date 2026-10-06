"""rule30_audit_g59.py: Local's check of GPT's G59 (a finite periodic Rule 210 witness needs infinitely many nonlinear
events), the second reader's companion to an argument audit. Checks the two facts the proof uses: for finite rows
under Rule 90 the centre column is 0 at times 2^k + j for j < p once 2^k > R + p (the Frobenius identity
A^(2^k) = S^(2^k) + S^(-2^k) over GF(2)), and the scope guard (the infinite period-3 row 100... becomes 011..., a fixed
point, so finiteness cannot be dropped). (Local, 2026-10-06; PROOFS.md G59 note; chat L034.)
COMMAND:    python3 tests/probes/lexicon/rule30_audit_g59.py      (seconds)
"""
import random
random.seed(20261006)
fails = 0
for trial in range(300):
    R = random.randint(1, 12); p = random.randint(1, 8)
    W = 2 * (1 << 9) + 2 * R + 64; c = W // 2
    x = [0] * W
    for i in range(-R, R + 1): x[c + i] = random.randint(0, 1)
    cols = []
    for t in range((1 << 9) + p + 2):
        cols.append(x[c])
        x = [(x[i - 1] if i > 0 else 0) ^ (x[i + 1] if i < W - 1 else 0) for i in range(W)]
    k = next(k for k in range(1, 10) if (1 << k) > R + p)
    fails += any(cols[(1 << k) + j] for j in range(p))
row = [1, 0, 0] * 10
r1 = [row[i - 1] ^ row[(i + 1) % 30] for i in range(30)]
r2 = [r1[i - 1] ^ r1[(i + 1) % 30] for i in range(30)]
fails += r1[:3] != [0, 1, 1] or r2 != r1
print("G59: Frobenius zero blocks on 300 random finite rows, and the 100 -> 011 fixed point:", "ALL CHECKS PASS" if fails == 0 else f"{fails} FAILED")
