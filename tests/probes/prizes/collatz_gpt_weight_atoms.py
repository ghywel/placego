"""G75 WA1-WA2, preregistered at51a1a0e.
WA1 MUST HOLD: full future-string populations T1..10, reverse J/R
identity, every attained positive R-tail bound, J atom bounds L1..8.
Retain bounds above1 as vacuous. No sharpness or decay measurement.
WA2 MUST HOLD: exact squared binomial bound h0..256; T3,t1 guard.
CF: J's maximum atom is at most the binomial's; MUST FAIL for that guard.
REFUTED-BY: J=2 with probability1; Binomial(1,1/2) max atom1/2.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
WA1 PASS2036 reverse identities/57 tails/1304 atoms. ALL1304 atom
bounds vacuous at this small scope; no empirical nontrivial decay check.
Tail/atom exponential comparisons floating with1e-14 tolerance;
probabilities exact rational. WA2 PASS257 exact squared binomial bounds.
CF REFUTED. No actual orbit or large count experiment.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, sqrt
from collatz_gpt_boundary_loss import threshold


def main():
    strings = tails = atoms = vacuous = 0
    guard = None
    for T in range(1, 11):
        for t in range(T):
            h = T-t-1
            rc, jc = Counter(), Counter()
            for word in product((0, 1), repeat=h):
                z, J = 0, threshold(t+1)
                for j, b in enumerate(word, t+2):
                    z += b
                    J = max(J, threshold(j)-z)
                suffix = 0
                R = 0
                for k, b in enumerate(reversed(word), 1):
                    suffix += b
                    R = max(R, suffix-(threshold(T)-threshold(T-k)))
                assert J == threshold(T)-z+R and R >= 0
                rc[R] += 1
                jc[J] += 1
                strings += 1
            den = 2**h
            for r in range(1, max(rc)+1):
                probability = Fraction(sum(n for x, n in rc.items() if x >= r), den)
                assert float(probability) <= 32*exp(-(r-1)/2)+1e-14
                tails += 1
            for n in jc.values():
                for L in range(1, 9):
                    raw = L/sqrt(h+1)+32*exp(-(L-1)/2)
                    assert float(Fraction(n, den)) <= min(1, raw)+1e-14
                    vacuous += raw >= 1
                    atoms += 1
            if (T, t) == (3, 1):
                guard = (jc, rc)
                assert jc == Counter({2: 2}) and rc == Counter({0: 1, 1: 1})
                assert Fraction(max(jc.values()), den) > Fraction(comb(h, h//2), 2**h)
    for h in range(257):
        assert comb(h, h//2)**2*(h+1) <= 4**h
    print('WA1 PASS:', strings, 'reverse decompositions,', tails,
          'tail comparisons,', atoms, 'atom comparisons;', vacuous,
          'atom bounds vacuous')
    print('Tail/atom exponential comparisons use floating arithmetic with1e-14 tolerance; exact probabilities retained')
    print('WA2 PASS257 exact squared binomial bounds; guard:', guard)
    print('CF REFUTED: dependent overshoot makes J atom1, binomial atom1/2')


if __name__ == '__main__':
    main()
