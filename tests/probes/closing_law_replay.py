#!/usr/bin/env python3
"""L1406 (Local, 2026-11-03): scalar replay of the Lean closing law (tests/probes/lean/ClosingLaw.lean) in the kit's
gate-clock indexing, for the OR family (Rule 30's right edge). Run: python3 tests/probes/closing_law_replay.py J SEEDS

flag(n) = prefixExp(n + 1) - prefixExp(n), with prefixExp(n + 1) = prefixExp(n) + [XOR over one period 2^prefixExp(n)
of force(n)], force(k, t) = OR(col k t, col (k - 1) t), col 0 = white, col (k + 1) t = bit k at time t (kit
Rule30GateClocks). For every n with flag(n) = 1 followed by m >= 0 pairs 10 and a 1 (flags n + 1 ... n + 2m + 1; every m, not only the
largest), the Lean
theorem says m + 1 <= 2^E (E = prefixExp n) and flag(n + 2m + 2) = 1 iff m + 1 = 2^E. Checked on the single-cell seed
and on random finite seeds; prints every occurrence count and any violation.
"""
import random
import sys

J = int(sys.argv[1]) if len(sys.argv) > 1 else 22
SEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 200


def flags(seed, J):
    """prefixExp(0..J) for the OR gate clock of a finite seed (bits beyond the list are white)."""
    x = list(seed) + [0] * (J + 2 - len(seed))
    E = [0]
    hist = [x[:]]                                  # hist[t][j] = bit j at time t
    def ensure(T):
        while len(hist) < T:
            y = hist[-1]
            z = [y[0] ^ 0] + [y[1] ^ (y[0] | 0)] + [y[j] ^ (y[j - 1] | y[j - 2]) for j in range(2, len(y))]
            hist.append(z)
    col = lambda k, t: 0 if k == 0 else hist[t][k - 1]
    for n in range(J):
        P = 1 << E[n]
        ensure(P)
        acc = 0
        for t in range(P):
            acc ^= col(n, t) | col(max(n - 1, 0), t)
        E.append(E[n] + acc)
    return E


def check(E):
    f = [E[i + 1] - E[i] for i in range(len(E) - 1)]
    occ = viol = closes = 0
    kinds = {}
    for n in range(len(f)):
        if f[n] != 1:
            continue
        m = 0
        while True:
            last = n + 2 * m + 1
            if last + 1 >= len(f) or f[last] != 1:
                break
            occ += 1
            q0 = 1 << E[n]
            nxt = f[last + 1] == 1
            closes += nxt
            kinds[(m, q0, nxt)] = kinds.get((m, q0, nxt), 0) + 1
            if not (m + 1 <= q0 and (nxt == (m + 1 == q0))):
                viol += 1
                print('VIOLATION', n, m, q0, nxt, ''.join(map(str, f)))
            if nxt:
                break
            m += 1                                   # flags last, last + 1 = 1, 0: one more pair
    return occ, viol, closes, ''.join(map(str, f)), kinds


occ, viol, closes, word, kinds = check(flags([1], J))
print('single seed, %d flags: %s; occurrences %d, closing with 1: %d, violations %d; (m, q0, closes): %s' % (
    J, word, occ, closes, viol, sorted(kinds.items())))
rng = random.Random(1406)
tot = [0, 0, 0]
allk = {}
for _ in range(SEEDS):
    seed = [rng.getrandbits(1) for _ in range(rng.randrange(1, 40))]
    o, v, c, _, k = check(flags(seed, 22))
    tot[0] += o; tot[1] += v; tot[2] += c
    for key, val in k.items():
        allk[key] = allk.get(key, 0) + val
print('%d random seeds (lengths 1..39, 22 flags each): occurrences %d, violations %d, closing with 1: %d' % (SEEDS, *tot))
print('(m, q0, closes) counts:', sorted(allk.items()))
print('CLOSING_REPLAY_DONE')
