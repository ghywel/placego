#!/usr/bin/env python3
"""om119_courtade_kumar.py: openai/math family 119, the most informative Boolean function (Courtade-Kumar).

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/openai_math/om119_courtade_kumar.py
COST:       about half a minute.

The claim (preprint "Sharp binary information contraction on the discrete cube", 2026-09-24): let X be uniform
on {0,1}^n and let Y be X with each bit flipped independently with probability a. For every Boolean function f,
    I(f(X); Y) <= 1 - h(a),    h(a) = -a log2 a - (1-a) log2 (1-a),
which a dictator f(x) = x_i attains: one bit is the most a single yes/no answer about X can say about Y. This was
conjectured by Courtade and Kumar in 2014. The proof is long and analytic and Cloud has not reviewed it. Cloud
replicates the inequality on every Boolean function of n <= 4 bits (2^16 functions at n = 4), at seven noise
levels, by its own code: I = h(E f) - E_y h(P(f = 1 | Y = y)), updated along a Gray code.
Predictions (written before the run): the maximum is 1 - h(a) to within 1e-12 at every n and a, attained only by
the 2n dictators and anti-dictators. Fail: any function above 1 - h(a) by more than 1e-12, or another function at
the maximum. Small cases were already checked numerically in the literature, so this is replication, not news.
Unexpected check: which non-dictator comes second, and by how much it falls short.
Control: at n = 1 the four functions give 0, 0, 1 - h(a), 1 - h(a) exactly.
"""
import math


def h(p):
    return 0.0 if p <= 0 or p >= 1 else -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def scan(n, a):
    N = 1 << n
    K = [[a ** bin(x ^ y).count("1") * (1 - a) ** (n - bin(x ^ y).count("1")) for x in range(N)] for y in range(N)]
    q, ones, best = [0.0] * N, 0, []
    f = 0
    for k in range(1, 1 << N):                       # Gray code over the 2^N truth tables
        bit = (k & -k).bit_length() - 1
        f ^= 1 << bit
        sgn = 1 if f >> bit & 1 else -1
        ones += sgn
        for y in range(N):
            q[y] += sgn * K[y][bit]
        info = h(ones / N) - sum(h(t) for t in q) / N
        best.append((info, f))
    best.sort(reverse=True)
    # The running sums drift by about 1e-12 over 65536 updates: recompute the leaders from scratch.
    top = [(exact(f, K, N), f) for _, f in best[:64]]
    return sorted(top, reverse=True) + best[64:]


def exact(f, K, N):
    q = [sum(K[y][x] for x in range(N) if f >> x & 1) for y in range(N)]
    return h(bin(f).count("1") / N) - sum(h(t) for t in q) / N


def dictators(n):
    N = 1 << n
    out = set()
    for i in range(n):
        d = sum(1 << x for x in range(N) if x >> i & 1)
        out |= {d, ((1 << N) - 1) ^ d}
    return out


def main():
    ok = True
    for a in (0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45):
        cap = 1 - h(a)
        for n in (1, 2, 3, 4):
            best = scan(n, a)
            top = [f for i, f in best if i > cap - 1e-12]
            over = best[0][0] - cap
            ok &= over <= 1e-12 and set(top) == dictators(n)
            if n == 1:
                ok &= sorted(round(i, 12) for i, _ in best) == sorted([0.0, round(cap, 12), round(cap, 12)])
            if n == 4:
                second = next((i, f) for i, f in best if f not in dictators(n))
                print(f"a = {a:4.2f}: 1 - h(a) = {cap:.6f}; best at n <= 4 exceeds it by {over:+.1e}; "
                      f"maximisers exactly the dictators: {set(top) == dictators(n)}; "
                      f"best non-dictator at n = 4 ({second[1]:#06x}) {second[0] / cap:.4f} of the cap")
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
