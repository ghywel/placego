"""Cloud's carrying-read instrument for GPT's G339 (CL479): two holes, sizes (3,3,c), filler at max-1.

I1  the 21-row table: Sigma_3(U) for each pool U (m = 6, 7, 8), the missing sums strictly inside (alpha, beta),
    and which of them lie within 2 of an edge.
I2  filler uniqueness: for every M in 10..20 and internal hole pair with z6 - z5 = 1, the c-subsets of S with
    sum beta_S(c) - 1 are exactly {z5} u {z7..}; and when z6 - z5 > 1 the value beta - 1 is not in the spectrum.
I3  the statement itself, by brute force: M = 10..20, all internal hole pairs, w = beta - 1, every (u, v) with
    all three singleton spectra feasible; exceptions should be exactly holes (1,4) (12,12) and (2,3) (8,16)/(16,8).
Prediction: 0 discrepancies in I1-I3.  Counterfactual: a table row off by one would show in I1; a second
exception family in I3 would refute the exhaustion claim.

OUTCOME (1.4 s): I1 all 21 rows agree with G339's table, including the near-edge entries and the two
central ones (12 in row 8;1,4 and 8/16 in row 8;2,3).  I2 M = 10..20: 0 uniqueness failures, 0 cases of
max-1 achievable with z6 - z5 > 1.  I3: 11,022 instances, exceptions exactly holes (1,4) (12,12) and (2,3)
(8,16) at every M.  Prediction held.
"""
import itertools, sys

def sig(U, k):
    return {sum(c) for c in itertools.combinations(sorted(U), k)}

def I1():
    pools = [(6, (), [x for x in range(7) if x != 5])]
    pools += [(7, (p,), [x for x in range(8) if x not in (p, 6)]) for p in range(1, 6)]
    pools += [(8, (p, q), [x for x in range(9) if x not in (p, q, 7)]) for p in range(1, 7) for q in range(p + 1, 7)]
    out = []
    for m, holes, U in pools:
        s3 = sig(U, 3); a, b = min(s3), max(s3)
        miss = [v for v in range(a, b + 1) if v not in s3]
        central = [v for v in miss if v - a > 2 and b - v > 2]
        out.append((m, holes, (a, b), miss, central))
        print(f'  m={m} holes={holes} alpha,beta={a},{b} missing={miss} central={central}')
    return out

def I2_I3(MMAX):
    bad_unique = bad_spec = 0; exceptions = []; n = 0
    for M in range(10, MMAX + 1):
        c = M - 7
        for q1 in range(1, M):
            for q2 in range(q1 + 1, M):
                S = [x for x in range(M + 1) if x not in (q1, q2)]; tot = sum(S)
                z = S
                beta = sum(z[-c:]); w = beta - 1
                csets = [C for C in itertools.combinations(S, c) if sum(C) == w]
                if z[6] - z[5] == 1:
                    if csets != [tuple([z[5]] + z[7:])]: bad_unique += 1
                else:
                    if csets: bad_spec += 1
                    continue
                s3 = sig(S, 3)
                U = [x for x in S if x not in csets[0]]
                u3 = sig(U, 3)
                for u in s3:
                    v = tot - w - u
                    if v not in s3: continue
                    n += 1
                    if u in u3: continue           # U's complement of a sum-u triple has sum v automatically
                    exceptions.append((M, (q1, q2), (u, v, w)))
    print('  I2: filler-uniqueness failures', bad_unique, ' max-1 in spectrum with z6-z5>1:', bad_spec)
    print('  I3: instances', n, ' exceptions:', exceptions)
    kinds = sorted({(e[1], tuple(sorted(e[2][:2]))) for e in exceptions})
    print('  I3 exception shapes (holes, sorted(u,v)):', kinds)

if __name__ == '__main__':
    print('I1 table:'); I1()
    I2_I3(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
