#!/usr/bin/env python3
"""G57 preregistered DC1-DC3. Exact small-ring controls; no data files."""
from rule30_gpt_ring_quotient import scalar, vector, rotations, cycles
from rule30_gpt_ring_phase import theta, normalize


def moment(x, p):
    return sum(i * ((x >> i) & 1) for i in range(p)) % p


def correction(x, p):
    bits = [(x >> i) & 1 for i in range(p)]
    values = [bits[i] * bits[(i + 1) % p]
              + 2 * bits[(i - 1) % p] * (bits[i] | bits[(i + 1) % p])
              for i in range(p)]
    return sum(values), sum(i * e for i, e in enumerate(values)) % p


def audit(p):
    checked = 0
    for x in range(1, (1 << p) - 1):
        y = scalar(x, p)
        assert y == vector(x, p)
        c, d = correction(x, p)
        w, m = x.bit_count(), moment(x, p)
        assert y.bit_count() == 3 * w - c
        assert moment(y, p) == (3 * m - d) % p
        if y in (0, (1 << p) - 1):
            continue
        drift = (c * m - d * w) * pow(w * y.bit_count(), -1, p) % p
        assert drift == (theta(y, p) - theta(x, p)) % p
        checked += 1
    reps = sorted({normalize(x, p) for x in range(1 << p)})
    quotient = cycles(reps, lambda x: normalize(vector(x, p), p))
    zero_cycles, zero_edges, gauge_cases = [], [], 0
    for cycle in quotient:
        if cycle == [0]:
            continue
        original = [theta(vector(x, p), p) for x in cycle]
        phi = {x: int(i == 0) for i, x in enumerate(cycle)}
        changed = [(edge + phi[normalize(vector(x, p), p)] - phi[x]) % p
                   for x, edge in zip(cycle, original)]
        assert sum(changed) % p == sum(original) % p
        terminal = cycle[0]
        for _ in cycle:
            terminal = scalar(terminal, p)
        direct = rotations(cycle[0], p).index(terminal)
        assert sum(original) % p == direct
        if direct == 0:
            zero_cycles.append(len(cycle))
            zero_edges.append((len(cycle), tuple(original)))
        if len(cycle) >= 2:
            assert sum(a != b for a, b in zip(original, changed)) == 2
            gauge_cases += 1
    if p == 7:
        assert zero_cycles == [4]
    if p == 11:
        assert zero_cycles == [17]
    print('DC PASS:', p, 'drift states=', checked, 'zero cycles=', zero_cycles, 'gauge cases=', gauge_cases, 'zero-cycle increments=', zero_edges)
    return checked, gauge_cases


if __name__ == '__main__':
    results = [audit(p) for p in (3, 5, 7, 11, 13)]
    print('DC1 drift-state comparisons:', sum(a for a, b in results))
    print('DC2/DC3 quotient gauge controls:', sum(b for a, b in results))
    print('Exact finite identities only; no nonzero-cycle-sum theorem.')
