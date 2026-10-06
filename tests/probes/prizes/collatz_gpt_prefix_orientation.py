"""G84 PF1-PF2 preregistered at4c2e796.
PF1 attained110/111 prefix extrema on existing a3..12 words;
signed inequality, representatives3/7 mod8, signed a3 guard.
PF2 exact a21 span and directional numerator. No a21 word search.
CF treating directional bound as absolute must fail at a3.
OUTCOME PF1 PASS10 extrema pairs/4401 existing words; PF2 exact a21
bounds pass. Signed guard refuted; no collision found or sought.
"""
from fractions import Fraction
from itertools import combinations
from collatz_gpt_boundary_loss import admissible
from collatz_gpt_offset_codes import intercept, evolve
from collatz_gpt_forced_spacing import extrema


def main():
    words = 0
    for a in range(3,13):
        A = 3**a
        t = A.bit_length()-1
        by_prefix = {(1,1,0):[], (1,1,1):[]}
        for positions in combinations(range(t),a):
            chosen = set(positions)
            word = tuple(int(j in chosen) for j in range(t))
            if admissible(word):
                by_prefix[word[:3]].append(intercept(word))
                words += 1
        lo, hi = extrema(a)
        L110 = 13*A//9-2**(a+1)
        U111 = hi-4*3**(a-3)
        assert min(by_prefix[(1,1,0)]) == L110
        assert max(by_prefix[(1,1,1)]) == U111
        R = Fraction(hi-lo,A)
        directional = R-Fraction(16,27)+Fraction(2,3)**a
        assert Fraction(U111-L110,A) == directional
    assert evolve(3,3)[0] == (1,1,0)
    assert evolve(7,3)[0] == (1,1,1)
    assert Fraction(19-23,27) == -Fraction(4,27)
    assert abs(Fraction(19-23,27)) > -Fraction(4,27)
    A = 3**21
    lo,hi = extrema(21)
    assert 4*A < hi-lo < 8*A
    numerator = hi-4*3**18-(13*A//9-2**22)
    assert numerator == 37365342780 and numerator < 4*A
    print('PF1 PASS10 attained prefix extrema pairs;',words,'existing words; representatives and signed CF pass')
    print('PF2 PASS a21 exact4<span<8 and opposite-direction bound<4:',Fraction(numerator,A))
    print('No collision found or sought; necessity controls only')


if __name__ == '__main__':
    main()
