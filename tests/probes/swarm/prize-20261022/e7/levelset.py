#!/usr/bin/env python3
"""Hand-checkable level-set criterion (Kraft slice + sorted-values lemma), uniform in the exponent of q.

Setting: lcm | q^a * m, gcd(q, m) = 1.  For each divisor d' > 1 of m the progressions 3^i d' (here q^i d')
form a family F_d' : Z/d' -> [0, q/(q-1)], a sum of DISTINCT powers q^-i placed at residues.
Sorted-values lemma: the k-th largest value of F_d' is <= c q^(1-k), c = q/(q-1).
If y avoids the top (k_d' - 1) residues of every family, S(y) <= sum_d' c q^(1-k_d').
A covering needs S(y) > 1 - 1/(q-1) for every y (pure q-powers give T < 1/(q-1)).
So it suffices: sum_d' c q^(1-k_d') <= (q-2)/(q-1)  AND  some y avoids all top sets.
Avoidance (two-prime product structure m = p1^b p2^c, or general union bound):
  P(avoid) >= prod_p (1 - sum_{pure p-power families} (k-1)/d') - sum_{mixed families} (k-1)/d'   (> 0 needed)
Families are enumerated for ALL exponents up to a cutoff D on d'; families beyond D are charged with a
safe tail (see below), so a success covers every exponent b, c simultaneously.
"""
import sys, math, itertools

def families(primes, D):
    """all d' > 1 composed of the given primes with d' <= D"""
    out = [1]
    for p in primes:
        new = []
        for d in out:
            x = d
            while x <= D:
                new.append(x); x *= p
        out = new
    return sorted(d for d in out if d > 1)

def evaluate(primes, q, mu, D):
    c = q / (q - 1)
    fam = families(primes, D)
    ks = {}
    for d in fam:
        best = None
        for k in range(1, d + 1):
            val = (k - 1) / d + mu * c * q ** (1 - k)
            if best is None or val < best[0] - 1e-15:
                best = (val, k)
            if k > 60:
                break
        ks[d] = best[1]
    weight = sum(c * q ** (1 - ks[d]) for d in fam)
    # tail: families with d' > D.  Give each such family k with q^(1-k) <= 1/d'^2 ... charge cost (k-1)/d'
    # number of {primes}-smooth d' in (D, inf) is infinite; use k_d' = 1 + ceil(2 log_q d') so that
    # weight c q^(1-k) <= c / d'^2 and cost (k-1)/d' <= (1 + 2 log_q d')/d'; sum both over smooth d' > D.
    tw = 0.0; tc = 0.0
    big = families(primes, D * 10**6)
    for d in big:
        if d <= D:
            continue
        k = 1 + math.ceil(2 * math.log(d, q))
        tw += c * q ** (1 - k); tc += (k - 1) / d
    # remaining tail beyond D*1e6 bounded crudely by an integral-type estimate (negligible); add 1e-6 margin
    tw += 1e-6; tc += 1e-6
    need = (q - 2) / (q - 1)
    # avoidance: product over primes of pure-power families, minus mixed families (tail counted as mixed)
    pure = {p: 0.0 for p in primes}
    mixed = 0.0
    for d in fam:
        ps = [p for p in primes if d % p == 0]
        cost = (ks[d] - 1) / d
        if len(ps) == 1:
            pure[ps[0]] += cost
        else:
            mixed += cost
    prod = 1.0
    for p in primes:
        prod *= (1 - pure[p])
    avoid = prod - mixed - tc
    union = sum((ks[d] - 1) / d for d in fam) + tc
    return weight + tw, need, avoid, union, ks

def main():
    primes = [int(x) for x in sys.argv[1].split(',')]
    q = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    D = int(sys.argv[3]) if len(sys.argv) > 3 else 10**5
    best = None
    for e in range(-400, 401):
        mu = 10 ** (e / 100)
        w, need, avoid, union, ks = evaluate(primes, q, mu, D)
        if w <= need and (best is None or avoid > best[2]):
            best = (mu, w, avoid, union, ks)
    if best is None:
        print(f"primes={primes} q={q}: no mu meets the weight condition"); return
    mu, w, avoid, union, ks = best
    small = {d: k for d, k in ks.items() if d <= 400}
    print(f"primes={primes} q={q} D={D}: best mu={mu:.4g} weight={w:.5f} (need <= {(q-2)/(q-1):.5f}) "
          f"P(avoid)>={avoid:.5f} unionbound={union:.5f}  k(d') for d'<=400: {small}")
    print("VERDICT:", "SUCCESS (no covering for any exponents)" if avoid > 0 else "FAIL (criterion too weak)")

if __name__ == '__main__':
    main()
