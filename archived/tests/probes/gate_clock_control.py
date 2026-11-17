#!/usr/bin/env python3
"""gate_clock_control.py: statement control for the gate-clock package (L1217).

RUN-ON:  cpu, Python 3 standard library, about a minute; no files written except the JSON report on stdout.
CLAIM:   the Lean definitions of reports/wolfram-agents/submissions/gate-clocks/Rule30Submission.lean say what its
         README says. This is a control on meaning, not evidence for the theorems, which are proved there.

For x_j(t+1) = x_j(t) xor g_j(x_(j-1)(t), x_(j-2)(t)), missing bits white, it simulates the first N bits as one
integer, gate truth tables indexed 2*b + s (OR = 14, AND = 8, XOR = 6), and checks
  P1  lifting exponent (parity of the forcing over one prefix period) == log2(first return of the first n bits);
  P2  every window bound E(a+2m) - E(a) <= m + Q_{E(a)}(m), exact thresholds;
  P3  affine gates: E(n) <= ceil(log2(n+1));
  P4  OR from seed 1: E(15) <= 6 (the kit's per_14);
  C1  the binary counter (outside the class) has E(n) = n and is flagged against B(n) for n = 4..N.
"""
import json
import sys

N = 16
MASK = (1 << N) - 1


def anf(table):
    """(lam, alpha, beta, gamma) of g(b, s) = lam*b*s ^ alpha*b ^ beta*s ^ gamma, table index 2*b + s."""
    g = lambda b, s: (table >> (2 * b + s)) & 1
    gamma = g(0, 0)
    beta = g(0, 1) ^ gamma
    alpha = g(1, 0) ^ gamma
    lam = g(1, 1) ^ alpha ^ beta ^ gamma
    return lam, alpha, beta, gamma


def masks(tables):
    """Per-depth gate tables -> bit masks of the four ANF coefficients."""
    out = [0, 0, 0, 0]
    for j, t in enumerate(tables):
        for i, c in enumerate(anf(t)):
            out[i] |= c << j
    return out


def step(x, m):
    lam, alpha, beta, gamma = m
    b = (x << 1) & MASK          # bit j sees bit j-1
    s = (x << 2) & MASK          # and bit j-2; zeros shift in
    return x ^ ((lam & b & s) ^ (alpha & b) ^ (beta & s) ^ gamma)


def counter_step(x):
    return (x + 1) & MASK


def exponents(seed, stepper):
    """Direct least periods of the first n bits, n = 0..N, from one orbit of the N-bit state; and the forcing data."""
    x0 = seed & MASK
    first = [1] + [None] * N
    states = [x0]
    x = x0
    t = 0
    while any(f is None for f in first):
        x = stepper(x)
        t += 1
        states.append(x)
        for n in range(1, N + 1):
            if first[n] is None and (x ^ x0) & ((1 << n) - 1) == 0:
                first[n] = t
        if t > (1 << N):
            raise SystemExit('no return within 2^N steps')
    return first, states


def log2_exact(p):
    e = p.bit_length() - 1
    return e if p == 1 << e else None


def lifting(states, m):
    """E(0) = 0; E(n+1) = E(n) + parity of bit n's forcing over 2^E(n) steps from t = 0."""
    lam, alpha, beta, gamma = m
    E = [0]
    for n in range(N):
        par = 0
        for t in range(1 << E[n]):
            x = states[t]
            b = (x >> (n - 1)) & 1 if n >= 1 else 0
            s = (x >> (n - 2)) & 1 if n >= 2 else 0
            f = ((lam >> n) & 1) & b & s ^ ((alpha >> n) & 1) & b ^ ((beta >> n) & 1) & s ^ ((gamma >> n) & 1)
            par ^= f
        E.append(E[n] + par)
    return E


def threshold(nu, q):
    t = 1
    for k in range(q):
        t = t + 2 ** (nu + t + k)
    return t


def Q(nu, d):
    q = 0
    while not d < threshold(nu, q):
        q += 1
    return q


def B(n):
    return (n + 1) // 2 + Q(0, n // 2)


def clog2(k):
    return (k - 1).bit_length()


def main():
    seeds = [0, 1, 3, 5, 0b1011, 0xB5, 0xACE1, 0xFFFF]
    lcg, mixtures = 12345, {}
    rand_tables = []
    for _ in range(N):
        lcg = (1103515245 * lcg + 12345) % (1 << 31)
        rand_tables.append((lcg >> 16) % 16)
    mixtures['or-and-alternating'] = [14 if j % 2 == 0 else 8 for j in range(N)]
    mixtures['fixed-random-16'] = rand_tables
    mixtures['affine-mixture'] = [[6, 10, 12, 9, 3, 5, 15, 0][j % 8] for j in range(N)]
    mixtures['choked-and-or'] = [[2, 4, 14, 8][j % 4] for j in range(N)]
    families = {'gate-%02d' % t: [t] * N for t in range(16)}
    families.update(mixtures)
    report = {'N': N, 'cases': 0, 'P1': 0, 'P2_windows': 0, 'P3': 0, 'failures': []}
    for name, tables in families.items():
        m = masks(tables)
        affine = all(anf(t)[0] == 0 for t in tables)
        for seed in seeds:
            report['cases'] += 1
            first, states = exponents(seed, lambda x: step(x, m))
            direct = [log2_exact(p) for p in first]
            E = lifting(states, m)
            if direct != E:
                report['failures'].append(['P1', name, seed, direct, E])
                continue
            report['P1'] += 1
            for a in range(N + 1):
                for mm in range((N - a) // 2 + 1):
                    report['P2_windows'] += 1
                    if E[a + 2 * mm] - E[a] > mm + Q(E[a], mm):
                        report['failures'].append(['P2', name, seed, a, mm, E])
            if affine:
                if all(E[n] <= clog2(n + 1) for n in range(N + 1)):
                    report['P3'] += 1
                else:
                    report['failures'].append(['P3', name, seed, E])
    first, _ = exponents(1, lambda x: step(x, masks([14] * N)))
    E_or = [log2_exact(p) for p in first]
    report['P4'] = {'E15': E_or[15], 'ok': E_or[15] <= 6, 'E': E_or}
    if not report['P4']['ok']:
        report['failures'].append(['P4', E_or])
    first, _ = exponents(0, counter_step)
    E_c = [log2_exact(p) for p in first]
    flagged = [n for n in range(N + 1) if E_c[n] > B(n)]
    report['C1'] = {'E': E_c, 'flagged': flagged, 'ok': flagged == list(range(4, N + 1))}
    if not report['C1']['ok']:
        report['failures'].append(['C1', E_c, flagged])
    report['affine_families'] = sorted(n for n, t in families.items() if all(anf(x)[0] == 0 for x in t))
    report['verdict'] = 'PASS' if not report['failures'] else 'FAIL'
    json.dump(report, sys.stdout, indent=1)
    print()
    return 0 if report['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
