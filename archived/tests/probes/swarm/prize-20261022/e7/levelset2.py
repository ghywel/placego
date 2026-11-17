#!/usr/bin/env python3
"""Stronger level-set criterion: avoid top sets for some families, average the rest.

lcm | q^a m.  Families F_d' (d' | m, d' > 1), F_d' = sum of distinct q^-i at residues mod d'.
Lemma A (sorted values): k-th largest value <= c q^(1-k), c = q/(q-1); total of ranks >= k is <= c q^(1-k).
Let A = { y in Z/m : y mod d' avoids the top (k_d' - 1) residues of F_d' for every d' }  (k_d' >= 1).
For y uniform on Z/m:  P(A) >= prod_p (1 - sum_{pure p-power d'} (k-1)/d') - sum_{mixed d'} (k-1)/d'  =: PA.
E[S | A] <= sum_d' min( c q^(1-k_d') ,  c q^(1-k_d') / (d' PA) ).
If PA > 0 and that sum <= (q-2)/(q-1), some y has S(y) <= (q-2)/(q-1) and its q-adic slice is uncovered
(pure q-powers contribute T < 1/(q-1)).  Families beyond the cutoff D: k = 1, average bound c/(d' PA), summed
over all smooth d' > D up to D*1e6 plus a 1e-6 margin.
"""
import sys, math

def smooth(primes, D):
    out = [1]
    for p in primes:
        new = []
        for d in out:
            x = d
            while x <= D:
                new.append(x); x *= p
        out = new
    return sorted(d for d in out if d > 1)

def score(primes, q, fam, ks, tail_inv):
    c = q / (q - 1)
    pure = {p: 0.0 for p in primes}; mixed = 0.0
    for d in fam:
        ps = [p for p in primes if d % p == 0]
        cost = (ks[d] - 1) / d
        if len(ps) == 1: pure[ps[0]] += cost
        else: mixed += cost
    PA = 1.0
    for p in primes:
        PA *= max(0.0, 1 - pure[p])
    PA -= mixed
    if PA <= 0:
        return None, PA
    E = 0.0
    for d in fam:
        b = c * q ** (1 - ks[d])
        E += min(b, b / (d * PA))
    E += c * tail_inv / PA + 1e-6
    return E, PA

def main():
    primes = [int(x) for x in sys.argv[1].split(',')]
    q = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    D = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    need = (q - 2) / (q - 1)
    fam = smooth(primes, D)
    tail_inv = sum(1.0 / d for d in smooth(primes, D * 10**6) if d > D)
    ks = {d: 1 for d in fam}
    # initial: avoid a little on the smallest families
    for d in fam[:3]:
        ks[d] = 2
    cur, PA = score(primes, q, fam, ks, tail_inv)
    if cur is None:
        cur = 1e9
    improved = True; it = 0
    while improved and it < 200:
        improved = False; it += 1
        for d in fam:
            for delta in (1, -1, 2, -2):
                k2 = ks[d] + delta
                if k2 < 1 or k2 > min(d, 40):
                    continue
                old = ks[d]; ks[d] = k2
                s, pa = score(primes, q, fam, ks, tail_inv)
                if s is not None and s < cur - 1e-12:
                    cur = s; PA = pa; improved = True
                else:
                    ks[d] = old
    small = {d: k for d, k in ks.items() if k > 1}
    print(f"primes={primes} q={q} D={D}: E[S|A] <= {cur:.5f} (need <= {need:.5f}), P(A) >= {PA:.5f}; "
          f"avoided-top sizes k-1 for d': { {d: k-1 for d, k in small.items()} }")
    print("VERDICT:", "SUCCESS" if cur <= need else "FAIL", flush=True)

if __name__ == '__main__':
    main()
