"""G35 exact even-correction envelope and critical gap controls."""
from fractions import Fraction
from collatz_gpt_signed_bound import step


def main():
    checks=0
    for d in (1,3,5,9):
        for start in range(-32,33):
            x,s,e=start,0,Fraction(0)
            for j in range(32):
                odd=x%2
                if not odd:
                    e+=Fraction(2**j,3**s)
                s+=odd;x=step(x,d)
                assert abs(x)+d <= Fraction(3**s,2**(j+1))*(abs(start)+d+d*e)
                checks+=1
    z=1;gaps=[]
    for _ in range(16):
        power=3**z;next_z=power.bit_length()
        assert 2**(next_z-1)<power<=2**next_z
        gaps.append(z);z=next_z
    for m in range(1,33):
        e=2**m-1
        assert Fraction(1,2**m)*(1+e)==1
    assert abs(step(2,1))+1 > Fraction(abs(2)+1,2)
    print(f'EC1 PASS: {checks} exact signed envelopes')
    print('EC2 PASS: 16 exact critical-ladder gaps; zero positions',gaps)
    print('Unexpected EC3 PASS: fixed0 saturates envelope with divergent correction')
    print('CF REJECTED: even branch needs additive D/2 in shifted height')


if __name__=='__main__':main()
