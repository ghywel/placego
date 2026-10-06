"""G37 exact finite maximum plus a proved decreasing infinite tail."""
from fractions import Fraction
from collatz_gpt_signed_bound import word


def main():
    assert 36*8**32 < 9**32
    z=1;rows=[]
    for k in range(32):
        nxt=(3*z+1)//2
        rows.append((k,z,nxt,Fraction(2**nxt,3**(z-k))))
        z=nxt
    cutoff=next(k for k,z,nxt,q in rows if nxt-z>=32)
    for (k,z,nxt,q),(_,_,after,qn) in zip(rows,rows[1:]):
        gap=nxt-z;nextgap=after-nxt
        assert 2*nextgap<=3*gap+2
        assert qn/q == Fraction(2**nextgap,3**(gap-1))
        if k>=cutoff:
            assert qn<q
    peak=max(rows[:cutoff+1],key=lambda row:row[3])
    qmax=peak[3]
    assert all(q<=qmax for _,_,_,q in rows)
    height=(qmax.numerator+qmax.denominator-1)//qmax.denominator
    n=height-1
    zeros=set();z=1
    while z<128:
        zeros.add(z);z=(3*z+1)//2
    target=tuple(int(i not in zeros) for i in range(128))
    actual=word(n,1,128)
    mismatch=next(i for i,(a,b) in enumerate(zip(actual,target)) if a!=b)
    assert height>=qmax and actual!=target
    print(f'SB1 PASS:32 exact budgets; global tail certificate starts at gap index{cutoff}')
    print(f'Global maximum at k{peak[0]}, z{peak[1]}: {qmax}; ceiling height{height}')
    print(f'Unexpected SB2 / CF REJECTED: start{n} passes all bare budgets, mismatch at index{mismatch}')
    print('Rational realization of the infinite target remains unresolved')


if __name__=='__main__':main()
