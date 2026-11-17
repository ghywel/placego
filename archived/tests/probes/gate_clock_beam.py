#!/usr/bin/env python3
"""gate_clock_beam.py: beam search toward the gate-clock bound's second threshold (L1239).

RUN-ON:  cpu, Python 3 standard library; minutes under the caps in reports/rule30-gate-clock-sharpness.md (block 2).
CLAIM:   lower bounds on max E(n) over depth-varying two-input gate families, by explicit witnesses (each kept state is
         reached by an actual gate sequence from the zero start); COMPUTED. A beam can miss better families, so a
         shortfall is not evidence of an obstruction, only of this beam.

Same states and moves as gate_clock_sharpness.py: (P, u, v) = streams of bits k-2 and k-1 over the prefix period P, a
move picks one of the 16 gates (table index 2*b + s) for bit k with seed 0, and a doubling happens iff the forcing has odd
weight over P. Streams are normalized only by complementing each to start with 0 (a symmetry), not by rotation. Ranking
at each depth: exponent (higher first), then the resource, the kit's difference order of the newest stream v over P
(lower first). The order is the largest r <= P - 1 with Delta^(P - r) v = 0, computed from the least vanishing index by
descending powers of two (Delta^(2^w) = S^(2^w) + I over F2).
"""
import json
import random
import sys


def prefix_xor(f, P):
    """Bit t of the result is f(0) xor ... xor f(t) (inclusive), for t < P."""
    x, sh = f, 1
    mask = (1 << P) - 1
    while sh < P:
        x ^= (x << sh) & mask
        sh <<= 1
    return x


def forcing(g, u, v, mask):
    f = 0
    for b in (0, 1):
        for s in (0, 1):
            if (g >> (2 * b + s)) & 1:
                f |= (v if b else ~v) & (u if s else ~u)
    return f & mask


def step(P, u, v, g):
    mask = (1 << P) - 1
    f = forcing(g, u, v, mask)
    w = (prefix_xor(f, P) << 1) & mask  # w(0) = 0, w(t) = f(0) xor ... xor f(t - 1)
    if bin(f).count('1') & 1:
        return 2 * P, v | (v << P), w | ((~w & mask) << P)
    return P, v, w


def norm(P, x):
    return x ^ ((1 << P) - 1) if x & 1 else x


def rot(x, r, P):
    r %= P
    mask = (1 << P) - 1
    return ((x >> r) | (x << (P - r))) & mask if r else x


def least_vanishing(x, P):
    """Least j >= 0 with Delta^j x = 0 for a P-periodic stream, P a power of two (Delta x(t) = x(t+1) xor x(t))."""
    if x == 0:
        return 0
    cur, j, w = x, 0, P >> 1
    while w >= 1:
        t = cur ^ rot(cur, w, P)
        if t:
            cur, j = t, j + w
        w >>= 1
    return j + 1


def order(x, P):
    return P - max(least_vanishing(x, P), 1)


def order_direct(x, P):
    """The kit's definition, by direct differences: largest r <= P - 1 with Delta^(P - r) x = 0."""
    diffs = [x]
    for _ in range(P):
        diffs.append(diffs[-1] ^ rot(diffs[-1], 1, P))
    best = 0
    for r in range(1, P):
        if diffs[P - r] == 0:
            best = r
    return best


def threshold(nu, q):
    t = 1
    for k in range(q):
        t = t + 2 ** (nu + t + k)
    return t


def B(n):
    d, q = n // 2, 0
    while not d < threshold(0, q):
        q += 1
    return (n + 1) // 2 + q


def beam(n_max, K, gates=range(16)):
    states = {(1, 0, 0)}
    out = []
    for k in range(n_max):
        children = set()
        for (P, u, v) in states:
            for g in gates:
                P2, v2, w2 = step(P, u, v, g)
                children.add((P2, norm(P2, v2), norm(P2, w2)))
        ranked = sorted(children, key=lambda s: (-(s[0].bit_length() - 1), order(s[2], s[0])))
        states = set(ranked[:K])
        best = ranked[0]
        out.append({'n': k + 1, 'B': B(k + 1), 'maxE': best[0].bit_length() - 1,
                    'resource_of_best': order(best[2], best[0]), 'children': len(children)})
        print(json.dumps(out[-1]), flush=True)
    return out


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 38
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    rng = random.Random(20261031)
    ctl = {'order_matches_definition': all(order(x, P) == order_direct(x, P)
                                            for P in (2, 4, 8, 16, 32, 64) for x in
                                            [0, (1 << P) - 1] + [rng.getrandbits(P) for _ in range(40)])}
    P, u, v, es = 1, 0, 0, [0]
    for k in range(12):
        mask = (1 << P) - 1
        f = forcing(14, u, v, mask)
        seed = 1 if k == 0 else 0
        w = (prefix_xor(f, P) << 1) & mask
        if seed:
            w ^= mask
        if bin(f).count('1') & 1:
            P, u, v = 2 * P, v | (v << P), w | ((~w & mask) << P)
        else:
            u, v = v, w
        es.append(P.bit_length() - 1)
    ctl['or_control'] = es
    ctl['or_control_ok'] = es == [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6]
    print(json.dumps(ctl), flush=True)
    res = beam(n_max, K)
    print(json.dumps({'summary': [(r['n'], r['B'], r['maxE'], r['resource_of_best']) for r in res]}), flush=True)


if __name__ == '__main__':
    main()
