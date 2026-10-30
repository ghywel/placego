#!/usr/bin/env python3
"""gate_clock_beam2.py: the L1239 beam with parent links, one traced family, and enforced controls (L1241, after GC2310).

RUN-ON:  cpu, Python 3 standard library; under a minute at n = 38, K = 64.
CLAIM:   one explicit gate family (one gate per depth, all seeds 0) whose first-n-bit exponents are printed, re-simulated
         from scratch by an independent plain stepper; COMPUTED. Its exponent at n = 38 is a lower bound for the max.

Differences from gate_clock_beam.py (GC2310's provenance gap): duplicates are merged by the same normalized key, but
each kept state is stored as its actual, unnormalized streams with its parent and gate, the best final state's ancestry is traced, and that gate sequence is re-simulated by
an independent bit-parallel evolution of the first n bits from the all-zero seed, reading each prefix's least period
from the states at times 2^e. Along the family it reports, per bit, whether it doubled, the order of the bit's own stream over the prefix
period (kit convention), and per pair the pattern. Controls are enforced: any failure exits 1.
"""
import json
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gate_clock_beam import step, order, order_direct, B, norm  # noqa: E402  (same directory, pinned by digest in the report)


def beam_traced(n_max, K):
    """Beam with parent links. Duplicates are merged by the complement-normalized key (as in gate_clock_beam.py, so the
    beam keeps the same diversity), but each kept entry stores an actual, unnormalized state, so the traced gate sequence
    is a real family from the all-zero seed."""
    start = (1, 0, 0)
    layers = [{start: None}]
    for k in range(n_max):
        children = {}
        for st in layers[-1]:
            P, u, v = st
            for g in range(16):
                ch = step(P, u, v, g)
                key = (ch[0], norm(ch[0], ch[1]), norm(ch[0], ch[2]))
                if key not in children:
                    children[key] = (ch, st, g)
        ranked = sorted(children, key=lambda s: (-(s[0].bit_length() - 1), order(s[2], s[0])))
        layers.append({children[key][0]: (children[key][1], children[key][2]) for key in ranked[:K]})
    best = min(layers[-1], key=lambda s: (-(s[0].bit_length() - 1), order(norm(s[0], s[2]), s[0])))
    gates, st = [], best
    for k in range(n_max, 0, -1):
        parent, g = layers[k][st]
        gates.append(g)
        st = parent
    return best, gates[::-1]


def plain_simulation(gates, e_max):
    """Independent of the beam's stream machinery: evolve the first n bits as one integer (bit j = cell j, missing bits
    white) from the all-zero seed, bit-parallel with per-depth ANF masks, and record the state at times 2^e. Prefix
    periods are powers of two, so E(m) is the least e <= e_max with x(2^e) = x(0) on bits 0..m-1."""
    n = len(gates)
    mask = (1 << n) - 1
    lam = alpha = beta = gamma = 0
    for j, t in enumerate(gates):
        g = lambda b, s: (t >> (2 * b + s)) & 1
        c0 = g(0, 0); c1 = g(0, 1) ^ c0; c2 = g(1, 0) ^ c0; c3 = g(1, 1) ^ c2 ^ c1 ^ c0
        gamma |= c0 << j; beta |= c1 << j; alpha |= c2 << j; lam |= c3 << j
    x0 = x = 0
    marks = {0: x0}
    for t in range(1, (1 << e_max) + 1):
        b, s = (x << 1) & mask, (x << 2) & mask
        x ^= (lam & b & s) ^ (alpha & b) ^ (beta & s) ^ gamma
        if t & (t - 1) == 0:
            marks[t.bit_length() - 1] = x
    out = []
    for m in range(n + 1):
        mm = (1 << m) - 1
        e = next((e for e in range(e_max + 1) if (marks[e] ^ x0) & mm == 0), None)
        out.append(e)
    return out


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 38
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    best, gates = beam_traced(n_max, K)
    # replay the traced gates through the beam's own stepper, recording per-bit data
    P, u, v = 1, 0, 0
    rows = []
    for k, g in enumerate(gates):
        P2, u2, v2 = step(P, u, v, g)
        rows.append({'bit': k, 'gate': g, 'doubled': P2 != P, 'E': P2.bit_length() - 1,
                     'order_of_bit': order(v2, P2)})
        P, u, v = P2, u2, v2
    replay_ok = (P, u, v) == best
    E_trace = [0] + [r['E'] for r in rows]
    E_plain = plain_simulation(gates, E_trace[-1])
    pairs = ''.join(('1' if rows[2 * i]['doubled'] else '0') + ('1' if rows[2 * i + 1]['doubled'] else '0') + ' '
                    for i in range(n_max // 2))
    out = {'n': n_max, 'K': K, 'gates': gates, 'E_trace': E_trace, 'B': [B(m) for m in range(n_max + 1)],
           'pairs': pairs.strip(), 'rows': rows, 'replay_ok': replay_ok,
           'plain_simulation_E': E_plain, 'plain_agrees': E_plain == E_trace}
    ok = replay_ok and E_plain == E_trace
    out['verdict'] = 'PASS' if ok else 'FAIL'
    json.dump(out, sys.stdout, indent=1)
    print()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
