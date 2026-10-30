#!/usr/bin/env python3
"""gate_clock_sharpness.py: how sharp is the gate-clock bound when the gate may change with depth? (L1237)

RUN-ON:  cpu, Python 3 standard library; a few minutes at most under the caps in reports/rule30-gate-clock-sharpness.md.
CLAIM:   exact max over all two-input gate families (one gate per depth) and seeds of E(n), the exponent of the least
         period of the first n bits, for n up to the depth where the state count stays under the cap; and the same max
         restricted to families with a doubling in every pair of bits (E(2i) >= i for every i). COMPUTED, not proved.

Bit k evolves by x_k(t+1) = x_k(t) xor g_k(x_(k-1)(t), x_(k-2)(t)), missing bits white; gate tables are indexed 2*b + s
(OR = 14, AND = 8, XOR = 6). The future of bit k depends only on the two streams (u, v) = (x_(k-2), x_(k-1)) over their
common prefix period P, so the search works on such states, kept up to a joint time shift and up to complementing either
stream: the seed covers every phase and complementing the new stream, and the 16 gates are closed under complementing an
input. One seed value per bit therefore suffices.

Controls: OR with the single-cell seed, simulated without any reduction, must give the kit's exponents
0,0,1,1,2,3,3,4,5,5,6,6,6 (gate_clock_control.py); the affine-only max must stay within ceil(log2(n+1)).
"""
import json
import sys

AFFINE = [t for t in range(16) if ((t >> 3) ^ (t >> 2) ^ (t >> 1) ^ t) & 1 == 0]  # lambda = g(1,1)^g(1,0)^g(0,1)^g(0,0) = 0


def forcing(g, u, v, mask):
    """Bit-parallel f(t) = g(b, s) with b = v(t) (newer input), s = u(t) (older)."""
    f = 0
    for b in (0, 1):
        for s in (0, 1):
            if (g >> (2 * b + s)) & 1:
                f |= (v if b else ~v) & (u if s else ~u)
    return f & mask


def new_stream(f, P, seed):
    """w(0) = seed, w(t+1) = w(t) xor f(t), for t < P; returns w over P and the parity of f over one period."""
    w, cur = 0, seed
    for t in range(P):
        if cur:
            w |= 1 << t
        cur ^= (f >> t) & 1
    return w, bin(f).count('1') & 1


def step(P, u, v, g, seed):
    mask = (1 << P) - 1
    f = forcing(g, u, v, mask)
    w, par = new_stream(f, P, seed)
    if par:
        v2 = v | (v << P)
        w2 = w | ((~w & mask) << P)
        return 2 * P, v2, w2
    return P, v, w


def rot(x, r, P):
    mask = (1 << P) - 1
    return ((x >> r) | (x << (P - r))) & mask


def canon(P, u, v):
    mask = (1 << P) - 1
    best = None
    for cu in (0, mask):
        for cv in (0, mask):
            a, b = u ^ cu, v ^ cv
            for r in range(P):
                key = (rot(a, r, P), rot(b, r, P))
                if best is None or key < best:
                    best = key
    return (P,) + best


def search(n_max, gates, cap, pair_constraint=False):
    """Breadth-first over depths; returns per-depth max exponent and state counts, and stops at the cap."""
    states = {canon(1, 0, 0)}
    out = []
    for k in range(n_max):
        nxt = set()
        for (P, u, v) in states:
            for g in gates:
                P2, v2, w2 = step(P, u, v, g, 0)
                if pair_constraint and (k + 1) % 2 == 0 and (P2.bit_length() - 1) < (k + 1) // 2:
                    continue
                nxt.add(canon(P2, v2, w2))
        if not nxt:
            out.append({'n': k + 1, 'states': 0, 'maxE': None})
            break
        states = nxt
        es = [P.bit_length() - 1 for (P, _, _) in states]
        out.append({'n': k + 1, 'states': len(states), 'maxE': max(es), 'minE': min(es),
                    'E_counts': {e: es.count(e) for e in sorted(set(es))}})
        if len(states) > cap:
            out[-1]['stopped'] = 'state cap'
            break
    return out


def threshold(nu, q):
    t = 1
    for k in range(q):
        t = t + 2 ** (nu + t + k)
    return t


def B(n):
    d = n // 2
    q = 0
    while not d < threshold(0, q):
        q += 1
    return (n + 1) // 2 + q


def or_control(n):
    """OR at every depth, seed 1 (bit 0 black), no reduction: exponents of the first k bits, k = 0..n."""
    P, u, v = 1, 0, 0
    es = [0]
    for k in range(n):
        P, u, v = step(P, u, v, 14, 1 if k == 0 else 0)
        es.append(P.bit_length() - 1)
    return es


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 400000
    report = {'n_max': n_max, 'cap': cap}
    report['B'] = [B(n) for n in range(n_max + 1)]
    report['or_control'] = or_control(12)
    report['or_control_ok'] = report['or_control'] == [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6]
    report['affine'] = search(n_max, AFFINE, cap)
    report['affine_ok'] = all(r['maxE'] <= (r['n']).bit_length() for r in report['affine'] if r['maxE'] is not None)
    report['all'] = search(n_max, range(16), cap)
    report['pair_constrained'] = search(n_max, range(16), cap, pair_constraint=True)
    json.dump(report, sys.stdout, indent=1)
    print()


if __name__ == '__main__':
    main()
