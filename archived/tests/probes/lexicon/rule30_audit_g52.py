"""rule30_audit_g52.py: Local's check of GPT's G52 (Corollary F for phase-aligned period blocks), written as the
second reader's companion to an argument audit, not a rerun of GPT's MF controls. It checks the step that carries
the proof: on a nonconstant periodic wall, matching white-phase vectors of column 1 over ell complete periods at
times p*i and p*i' make the column pair (-1, 0) identical over p*ell times (Lemma 1), whatever column 1 does at black
phases; and the wall 001 example (column -1 reads 0, 1, 1 at its phases with column 1 white), which shows why the
blocks must be phase-aligned. (Local, 2026-10-06; PROOFS.md G52 note; chat L023.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g52.py      (a second)
OUTCOME, 2026-10-06: 1,764 random walls (periods 2 to 9), 0 failures; wall 001 gives 0, 1, 1.
"""
import random
random.seed(20261006)
def col_m1(tau, sigma, T):
    p = len(tau)
    return [tau[(t + 1) % p] ^ (tau[t % p] | sigma[t]) for t in range(T)]
bad = n = 0
for trial in range(2000):
    p = random.randint(2, 9)
    tau = [random.randint(0, 1) for _ in range(p)]
    if all(x == tau[0] for x in tau): continue
    white = [ph for ph in range(p) if tau[ph] == 0]
    if not white: continue
    blocks = [[random.randint(0, 1) for _ in white] for _ in range(30)]
    i, ip, ell = 3, 3 + random.randint(1, 10), random.randint(1, 8)
    for k in range(ell): blocks[ip + k] = list(blocks[i + k])            # matched white-phase vectors
    sigma = []
    for m in range(30):
        for ph in range(p):
            sigma.append(blocks[m][white.index(ph)] if ph in white else random.randint(0, 1))  # black-phase bits arbitrary
    c = col_m1(tau, sigma, 30 * p)
    a, ap = p * i, p * ip
    n += 1
    bad += any(c[a + s] != c[ap + s] or tau[(a + s) % p] != tau[(ap + s) % p] for s in range(p * ell))
c001 = col_m1([0, 0, 1], [0] * 9, 9)[:3]
print("G52: matched phase-aligned blocks give identical (-1, 0) windows:", n, "random walls, failures", bad,
      "; wall 001 with sigma = 0, column -1 at phases 0, 1, 2:", c001)
