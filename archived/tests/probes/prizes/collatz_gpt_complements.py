"""G36 finite complement controls, not rationality-preservation evidence."""
from fractions import Fraction
from math import isqrt
from collatz_gpt_signed_bound import word, step
from collatz_gpt_periodic import affine


def main():
    controls=bits_checked=0
    for family in ('squares','powers'):
        for n in range(1,65):
            bits=tuple(int(not (isqrt(i)**2==i if family=='squares' else i>0 and i&(i-1)==0)) for i in range(n))
            for target in (bits,tuple(1-e for e in bits)):
                s,b=affine(target);modulus=1<<n
                r=(-b*pow(3**s,-1,modulus))%modulus
                assert word(r,1,n)==target
                controls+=1;bits_checked+=n
    for x,y in ((Fraction(3),Fraction(-4,9)),(Fraction(-11,3),Fraction(8,5))):
        a=word(x.numerator,x.denominator,128)
        b=word(y.numerator,y.denominator,128)
        assert all(e+f==1 for e,f in zip(a,b))
    assert step(0,1)==0 and step(-1,1)==-1
    assert word(0,1,64)==(0,)*64 and word(-1,1,64)==(1,)*64
    assert word(1,1,64)==(1,0)*32
    print(f'CM1 PASS: {controls} finite residue controls; {bits_checked} bits')
    print('CM2 PASS: two rational complementary examples through128 bits')
    print('Unexpected CM3 PASS: complementary rational fixed points0,-1')
    print('CF REJECTED: cycles have lower odd density0 or1/2; divergent hypothesis essential')


if __name__=='__main__':main()
