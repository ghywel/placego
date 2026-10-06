"""G87 PB1-PB2, preregistered before running in the containing publication.
PB1 attained sixth-prefix extrema on existing a=5..12 words.
PB2 exact a21 budget and eight-step guards 251/255; no meeting claim.
CF dropping positive minimum-offset correction must fail at a5.
"""
from itertools import combinations
from fractions import Fraction
from collatz_gpt_boundary_loss import admissible
from collatz_gpt_offset_codes import intercept, evolve
from collatz_gpt_forced_spacing import extrema


def states(n,t):
    out = [n]
    for _ in range(t):
        n = (3*n+1)//2 if n%2 else n//2
        out.append(n)
    return out


def main():
    words = 0
    for a in range(5,13):
        A = 3**a
        t = A.bit_length()-1
        low,high = [],[]
        lo,hi = extrema(a)
        for positions in combinations(range(t),a):
            selected = set(positions)
            word = tuple(int(j in selected) for j in range(t))
            if not admissible(word):
                continue
            words += 1
            B = intercept(word)
            if word[:6] == (1,1,0,1,1,1):
                low.append(B)
            if word[:6] == (1,1,1,1,1,0):
                high.append(B)
        assert max(low) == hi-32*3**(a-5)
        assert min(high) == A+32*3**(a-5)-2**(a+1)
        actual = Fraction(max(low)-min(high),A)
        assert actual == Fraction(hi-lo,A)-Fraction(64,243)+Fraction(2,3)**a
    A = 3**21
    lo,hi = extrema(21)
    numerator = hi-lo-64*3**16+2**21
    assert numerator == 40809080460 < 4*A == 41841412812
    assert evolve(251,8)[0] == (1,1,0,1,1,0,1,1)
    assert evolve(255,8)[0] == (1,)*8
    x,y = states(251,9),states(255,9)
    for s,c in ((6,44),(7,62),(8,89)):
        assert y[s] == 9*x[s]+c
    assert x[8]%2 != y[8]%2
    assert intercept((1,1,0,1,1,1,0)) == 287
    assert intercept((1,1,1,1,1,0,0)) == 211
    assert Fraction(287-211,243) > Fraction(319-211,243)-Fraction(64,243)
    print('PB1 PASS eight attained extrema pairs;',words,'existing words')
    print('PB2 PASS exact budget and eight-step affine guards; correction CF REFUTED')
    print('No meeting asserted or sought')


if __name__ == '__main__':
    main()
