#!/usr/bin/env python3
"""gc2313_moment_check.py (Local, L1251): exact control of GC2313's two-step boundary covariances and mass moments.

RUN-ON:  cpu, Python 3 standard library; under a second (at most 2^14 ancestor words).
CLAIM:   COMPUTED, exact rational arithmetic. Independent of GC2313's two-step identity: each output row is two plain
         Rule 30 steps, new(j) = old(j-1) xor (old(j) or old(j+1)), of the zero-padded ancestor.

Ensemble (GC2313): ancestor width L = W - 4, endpoints black, interior bits uniform; Z_i = F^2(x)_(i-2), 0 <= i <= L+3.
S = Z_1 + ... + Z_4, K = total black mass of the output row.

Prediction (written before the run): for every W in 14..20,
  Cov(S, Z_i) for i = 5, 6, 7, 8 is (1/8, 1/64, 0, -1/64), and Cov(S, Z_i) = 0 for 9 <= i <= L + 3;
  E K = W/2 + 1 and Var K = W/4 - 7/8; every output row has width exactly W with both endpoints black;
  the map from ancestors to outputs is injective.
Counterfactual: any mismatch means GC2313's identity, its conditional table or its width guard is wrong as written.
Widths 12 and 13, below GC2313's sufficient guard, are reported without a prediction.
"""
from fractions import Fraction as Fr
import json, sys


def step(cells):
    """One Rule 30 step on a finite list, with white cells outside; the result is two cells wider."""
    p = [0, 0] + cells + [0, 0]
    return [p[j - 1] ^ (p[j] | p[j + 1]) for j in range(1, len(p) - 1)]


def moments(W):
    L = W - 4
    rows = []
    for m in range(1 << (L - 2)):
        x = [1] + [(m >> k) & 1 for k in range(L - 2)] + [1]
        z = step(step(x))
        assert len(z) == L + 4
        rows.append(z)
    n = len(rows)
    width_ok = all(z[0] == 1 and z[-1] == 1 for z in rows)
    injective = len({tuple(z) for z in rows}) == n
    S = [sum(z[1:5]) for z in rows]
    K = [sum(z) for z in rows]
    ES = Fr(sum(S), n)
    cov = [Fr(sum(S[r] * rows[r][i] for r in range(n)), n) - ES * Fr(sum(rows[r][i] for r in range(n)), n)
           for i in range(L + 4)]
    EK = Fr(sum(K), n)
    VK = Fr(sum(k * k for k in K), n) - EK * EK
    return {'W': W, 'words': n, 'width_ok': width_ok, 'injective': injective,
            'cov_5_8': [str(c) for c in cov[5:9]], 'cov_9_on_zero': all(c == 0 for c in cov[9:]),
            'EK': str(EK), 'VarK': str(VK), 'EK_pred': str(Fr(W, 2) + 1), 'VarK_pred': str(Fr(W, 4) - Fr(7, 8)),
            '_ok': (width_ok and injective and cov[5:9] == [Fr(1, 8), Fr(1, 64), Fr(0), Fr(-1, 64)]
                    and all(c == 0 for c in cov[9:]) and EK == Fr(W, 2) + 1 and VK == Fr(W, 4) - Fr(7, 8))}


def main():
    out = [moments(W) for W in range(12, 21)]
    predicted = [r for r in out if r['W'] >= 14]
    ok = all(r['_ok'] for r in predicted)
    for r in out:
        print(json.dumps({k: v for k, v in r.items()}))
    print('GC2313_MOMENTS_PASS' if ok else 'GC2313_MOMENTS_FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
