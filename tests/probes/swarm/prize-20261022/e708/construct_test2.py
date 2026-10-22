#!/usr/bin/env python3
"""Theorem 2 (general, non-squarefree) construction test.
Heavy a (omega>=3): block w_a = a / P(a)^{v}, hosts at distinct multiples (greedy in increasing t_a = M // w_a).
Then for each prime p: Z_p = top r_p elements of I minus hosts by v_p, r_p = #{light a: p|a} + #{heavy a: P(a)=p}.
Check prod(A) | prod(B) and |B| <= 2n whenever sorted t_(i) >= i. Also counts how often the condition holds."""
import random, sys, time
sys.path.insert(0, '.')
from g708 import factor
T0 = time.time(); TL = 150
rng = random.Random(7080)

def vp(x, p):
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def build(A, I):
    M = max(A)
    F = {a: factor(a) for a in A}
    heavy = [a for a in A if len(F[a]) >= 3]
    light = [a for a in A if len(F[a]) < 3]
    w = {a: a // (max(F[a]) ** F[a][max(F[a])]) for a in heavy}
    order = sorted(heavy, key=lambda a: M // w[a])
    if any(M // w[a] < i + 1 for i, a in enumerate(order)):
        return 'cond-fails', None
    used, host = set(), {}
    for a in order:
        c = next(b for b in I if b % w[a] == 0 and b not in used)
        host[a] = c; used.add(c)
    B = set(used)
    primes = sorted({p for a in A for p in F[a]})
    for p in primes:
        r = sum(1 for a in light if p in F[a]) + sum(1 for a in heavy if max(F[a]) == p)
        pool = sorted((b for b in I if b not in used), key=lambda b: -vp(b, p))
        B.update(pool[:r])
    return 'ok', B

def check(A, B):
    e = {}
    for a in A:
        for p, k in factor(a).items():
            e[p] = e.get(p, 0) + k
    return all(sum(vp(b, p) for b in B) >= k for p, k in e.items())

st = dict(tests=0, cond=0, heavy_sets=0, max_heavy=0)
while __name__ == '__main__' and time.time() - T0 < TL:
    n = rng.randint(3, 9)
    X = rng.choice([500, 3000, 20000])
    kind = rng.random()
    if kind < 0.6:   # bias toward many heavy elements, non-squarefree allowed
        pool = [a for a in range(30, X + 1) if len(factor(a)) >= 3]
    else:
        pool = list(range(2, X + 1))
    A = sorted(rng.sample(pool, n))
    s = rng.randrange(10 ** 6, 10 ** 10)
    I = list(range(s, s + A[-1]))
    status, B = build(A, I)
    st['tests'] += 1
    h = sum(1 for a in A if len(factor(a)) >= 3)
    st['max_heavy'] = max(st['max_heavy'], h) if status == 'ok' else st['max_heavy']
    if h:
        st['heavy_sets'] += 1
    if status == 'ok':
        st['cond'] += 1
        assert check(A, B) and len(B) <= 2 * n, ('THEOREM 2 FAIL', A, s, len(B))
if __name__ == '__main__': print('construct_test2 passed:', st, 't=%.0fs' % (time.time() - T0), flush=True)
