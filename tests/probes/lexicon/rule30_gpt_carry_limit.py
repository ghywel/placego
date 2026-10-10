#!/usr/bin/env python3
"""GC935 finite-carry one-step transfer audit; no SAT or survivor sweep.
Registered 2026-10-10 03:16 BST before first execution.
P1: x_m=4/3+(2/3)*4^-m, m2..6, has true white next half-digit;
    capped output is black iff k<2m-2, for k0..2m.
C1: carry-age scalar addition equals independent OR-of-birth propagation.
CF: below-boundary y_m=4/3-(1/3)*4^-m gives exact true arithmetic
    at every cap (no adjacent input ones); it must remain black.
U: white half-digit does not imply exact arithmetic; exact output first at k2m.
All inputs terminating dyadics; canonical trailing-zero names. <=65 additions.
OUTCOME, 2026-10-10 03:17 BST: P1/C1/CF/U PASS on45 upper and45
lower input cases; m2..6 half thresholds2/4/6/8/10 and exact4/6/8/10/12.
The stated <=65 addition cap was miscounted and exceeded:90 input cases,
each checked by two implementations. Retained error; m/k grid unchanged.
"""
from fractions import Fraction as F


def aged(a,b,k):
    out=0; age=0
    for i in range(max(a.bit_length(),b.bit_length())+2):
        u=(a>>i)&1;v=(b>>i)&1
        out|=(u^v^bool(age))<<i
        z=1 if u&v else (age+1 if (u^v) and age else 0)
        age=z if 0<z<=k else 0
    assert age==0
    return out


def births(a,b,k):
    out=0
    def bit(n,i): return (n>>i)&1 if i>=0 else 0
    for i in range(max(a.bit_length(),b.bit_length())+2):
        carry=any(bit(a,i-j)&bit(b,i-j) and
                  all(bit(a,h)^bit(b,h) for h in range(i-j+1,i))
                  for j in range(1,k+1))
        out|=(bit(a,i)^bit(b,i)^carry)<<i
    return out


def half(x): return (x*2).__floor__()%2


def main():
    count=0
    for m in range(2,7):
        d=4**m
        a=d+(d+2)//3
        x=F(a,d)
        assert x==F(4,3)+F(2,3*d)
        truth=3*x/2
        assert truth==2+F(1,d) and half(truth)==0
        full=[]
        for k in range(2*m+1):
            z=aged(a,2*a,k)
            assert z==births(a,2*a,k)
            value=F(z,2*d)
            assert half(value)==int(k<2*m-2)
            if value==truth: full.append(k)
            below=d+(d-1)//3
            assert aged(below,2*below,k)==births(below,2*below,k)==3*below
            assert half(F(3*below,2*d))==1
            count+=1
        assert full==[2*m]
        print('m',m,'half threshold',2*m-2,'exact threshold',full[0])
    assert count==45
    assert F(aged(22,44,2),32)==F(17,16) # existing GC837 boundary
    print('PASS P1/C1/CF/U;',count,'upper and',count,'lower controls')

if __name__=='__main__': main()
