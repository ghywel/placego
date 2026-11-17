"""G83 FS1-FS2 preregistered at e9b1213. Exact arithmetic and existing a<=12 words.
FS1 require span recurrence, strict monotonicity a>=2, span<4 through14.
First count with span>=4 left unpredicted. FS2 initial11/common offset
mod4/span controls; CF unconditional3-mod4 at horizon1 must fail on n1.
No extended a13..17 code search or new actual-start population.
OUTCOME: FS1 PASS64 exact spans,63 recurrences; first span>=4 at21.
FS2 PASS4403 existing words; both guards pass, horizon1 CF refuted.
Monotonicity plus exact R20<4 excludes collisions througha20.
"""
from fractions import Fraction
from itertools import combinations
from collatz_gpt_boundary_loss import admissible
from collatz_gpt_offset_codes import intercept, evolve


def extrema(a):
    A = 3**a
    return A-2**a, sum(3**(a-1-i)*2**((3**i).bit_length()-1) for i in range(a))


def main():
    spans = {}
    for a in range(1, 65):
        lo, hi = extrema(a)
        spans[a] = Fraction(hi-lo, 3**a)
        assert spans[a] <= Fraction(a,3)-1+Fraction(2,3)**a
        if a <= 14:
            assert spans[a] < 4
        if a > 1:
            b = a-1
            increment = Fraction(2**((3**b).bit_length()-1)-2**b, 3**a)
            assert spans[a]-spans[b] == increment
            assert spans[a] > spans[b] if b >= 2 else spans[a] == spans[b] == 0
    eligible = next(a for a in spans if spans[a] >= 4)
    words = 0
    for a in range(1, 13):
        t = (3**a).bit_length()-1
        lo, hi = extrema(a)
        for positions in combinations(range(t), a):
            chosen = set(positions)
            word = tuple(int(j in chosen) for j in range(t))
            if not admissible(word):
                continue
            B = intercept(word)
            assert lo <= B <= hi
            if a >= 2:
                assert word[:2] == (1,1)
                assert B % 4 == (5*3**(a-2)) % 4
            words += 1
    assert admissible(evolve(1,1)[0]) and 1 % 4 != 3
    for n in (625,597):
        word, a, y, deficit = evolve(n,9)
        assert a == 2 and y == 11 and deficit == 2 and not admissible(word)
    print('FS1 PASS64 exact spans/63 recurrence comparisons; first span>=4:', eligible)
    print('Bracket exact:', eligible-1, spans[eligible-1], eligible, spans[eligible])
    print('FS2 PASS', words, 'existing admitted words; horizon1 CF REFUTED; unrestricted guard excluded')


if __name__ == '__main__':
    main()
