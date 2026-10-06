"""G93 DS1-DS2: preregister before running. NOT RUN.
DS1 MUST HOLD: for T1..8, every child time r1..T, enumerate all future
bits and compare demand atoms with backward weights; total mass one.
DS2 BLIND: every demand profile at T1..64,r1..T is log-concave.
Stop shape search at its first failure; retain and independently verify
its three atoms by enumeration if h<=16, otherwise forward coin counting.
UNEXPECTED/COUNTERFACTUAL MUST FAIL: a binomial convolution alone
guarantees log-concavity for arbitrary independent suffix shifts.
REFUTED-BY: explicit q[j]^2 < q[j-1]*q[j+1], or an internal support gap.
Finite coin diagnostic only: no actual allocation or global error bound.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
from collatz_gpt_backward_weights import backward
from collatz_gpt_boundary_loss import threshold


def atoms(T, r):
    row = backward(T)[r]
    return {j: row[j]-row.get(j-1, Fraction(0)) for j in range(T+2)}


def enumerated(T, r):
    law = Counter()
    for bits in product((0, 1), repeat=T-r):
        z, demand = 0, threshold(r)
        for k, bit in enumerate(bits, 1):
            z += bit
            demand = max(demand, threshold(r+k)-z)
        law[demand] += 1
    return {j: Fraction(law[j], 2**(T-r)) for j in range(T+2)}


def forward_atoms(T, r):
    # Independent forward survival CDF for each possible starting count.
    cdf = [Fraction(0)]
    for a in range(T+2):
        counts = Counter({0: 1}) if a >= threshold(r) else Counter()
        for k in range(1, T-r+1):
            nxt = Counter()
            for z, mass in counts.items():
                for bit in (0, 1):
                    if 3**(a+z+bit) >= 2**(r+k):
                        nxt[z+bit] += mass
            counts = nxt
        cdf.append(Fraction(sum(counts.values()), 2**(T-r)))
    return {j: cdf[j+1]-cdf[j] for j in range(T+2)}


def main():
    checks = 0
    for T in range(1, 9):
        for r in range(1, T+1):
            q = atoms(T, r)
            assert q == enumerated(T, r) and sum(q.values()) == 1
            checks += 1
    # B~Bin(1,1/2), independent shift S in {0,3}, each with probability 1/2.
    mixture = Counter(b+s for b in (0, 1) for s in (0, 3))
    assert mixture[2]**2 < mixture[1]*mixture[3]
    profiles = 0
    failure = None
    for T in range(1, 65):
        for r in range(1, T+1):
            q = atoms(T, r)
            assert sum(q.values()) == 1 and all(v >= 0 for v in q.values())
            profiles += 1
            for j in range(1, T+1):
                if (q[j]**2 < q[j-1]*q[j+1] or
                    (q[j] == 0 and any(q[k] > 0 for k in range(j))
                     and any(q[k] > 0 for k in range(j+1,T+2)))):
                    independent = enumerated(T, r) if T-r <= 16 else forward_atoms(T, r)
                    assert independent == q
                    failure = dict(T=T,r=r,h=T-r,j=j,
                                   atoms=[str(q[k]) for k in (j-1,j,j+1)])
                    break
            if failure:
                break
        if failure:
            break
    Path('/private/tmp/placego-gpt-demand-shape.json').write_text(
        json.dumps(dict(controls=checks,profiles=profiles,failure=failure),indent=2))
    print('DS1 PASS:', checks, 'independent future-string demand profiles')
    print('Binomial-convolution-alone counterfactual REFUTED: disconnected mixture support')
    print('DS2', 'REFUTED' if failure else 'HELD in finite scope', 'after', profiles, 'profiles')
    print('Independent counterexample:', failure)
    print('No actual population, shape theorem or count-error bound inferred')


if __name__ == '__main__':
    main()
