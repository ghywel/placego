#!/usr/bin/env python3
"""Independent finite counterchecks of Cloud 8.109 and 8.110 (GPT, 2026-10-14).
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/mahler/mahler_gpt_sign_review.py
RUN-ON: owner's Intel host, standard-library Python, one process; expected <30 s.
Record searched: record_find.py '8\.109|8\.110|sign rule|no11|no 11' ->
Cloud 8.109/8.110, G50/G51, GC1221/1222; no11 is necessary, not sufficient.
Independent implementation: direct integer T-iteration plus exact constraints
on the INITIAL fractional part; no Cloud code or residue formula imported.
Erdos uses all ternary 0/1 units, not Cloud's exponent-lifting tree.

PREDICTIONS BEFORE FIRST RUN:
 SR1 control: direct Mahler windows reproduce A(1..10)=2,3,5,8,12,18,27,40,60,90.
 SR2 must hold: x/3 intersection at depths1..12 is exactly {0,2^(T-1)}.
 SR3 must hold: for e=-15..40 except0 with 3^v2(e)*odd(e)=3 mod4,
     actual Mahler survivors equal A_T restricted to v2(r)>=max(T-v2(e)-1,0).
 SR4 must hold: on all 0/1 ternary units through10 digits, every sign-minus
     multiplier in -15..40 has exactly the survivors x=1 mod3^max(k-v3(e),1).
 SR5 control: generalized binomial coefficients for e=-40..40 except0,
     j=2..32 obey v3(C(e,j))>=v3(e)-v3(j); j*h-v3(j)>=2*h at h1..4.
 CF1 must FAIL: all Mahler sign-minus finite intersections are {0,2^(T-1)},
     regardless of multiplier valuation (Cloud's retained wrong criterion).
 CF2 must FAIL: all Erdos sign-minus finite intersections are {1}.
 U unexpected must FAIL: drop the unit hypothesis in the squaring theorem;
     x=3 and x^2=9 both have ternary digits0/1, but x!=1.
REFUTED-BY: any SR failure or any non-rejection of CF1/CF2/U. Boundaries and
negative exponents included. Finite checks support, never replace, hand proofs.
OUTCOME: NOT RUN at preregistration. Retain failures; append outcome after run.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def val(n,p):
    if not n:
        return 10**9
    z=0
    while n%p==0:
        n//=p; z+=1
    return z


def window(r,t):
    # u_j = a*u_0-d; constrain every iterate to [0,1/2).
    lo,hi=F(0),F(1,2)
    a,d=F(1),F(0)
    n=r
    for _ in range(t):
        b=n%2; n=(3*n+b)//2
        a=3*a/2; d=(3*d+b)/2
        lo=max(lo,d/a); hi=min(hi,(d+F(1,2))/a)
        if lo>=hi:
            return False
    return True


def ternary01(x,k):
    for _ in range(k):
        if x%3==2:
            return False
        x//=3
    return True


def main():
    counts=[]; triples=0; comparisons=0; old_m=[]
    for t in range(1,13):
        A={r for r in range(1<<t) if window(r,t)}
        counts.append(len(A)); mod=1<<t
        assert {r for r in A if 3*r%mod in A}=={0,1<<(t-1)},t
        triples+=1
        for e in range(-15,41):
            if not e: continue
            a=val(e,2); u=e//2**a
            if 3**a*u%4!=3: continue
            actual={r for r in A if e*r%mod in A}
            expected={r for r in A if r%2**max(t-a-1,0)==0}
            assert actual==expected,(t,e,actual,expected)
            comparisons+=1
            if actual!={0,1<<(t-1)} and not old_m:
                old_m=[t,e,sorted(actual)]
    assert counts[:10]==[2,3,5,8,12,18,27,40,60,90],counts
    print('SR1 PASS counts:',counts)
    print('SR2 PASS depths:',triples)
    print('SR3 PASS exact finite Mahler comparisons:',comparisons)
    old_e=[]; epairs=0; unit_words=0
    for k in range(1,11):
        mod=3**k
        C={1+sum(d*3**(j+1) for j,d in enumerate(bits)) for bits in product((0,1),repeat=k-1)}
        unit_words+=len(C)
        for e in range(-15,41):
            if not e: continue
            b=val(e,3); u=e//3**b
            if u%3!=2: continue
            actual={x for x in C if ternary01(pow(x,e,mod),k)}
            expected={x for x in C if (x-1)%3**max(k-b,1)==0}
            assert actual==expected,(k,e,actual,expected)
            epairs+=1
            if actual!={1} and not old_e:
                old_e=[k,e,sorted(actual)]
    print('SR4 PASS finite Erdos comparisons:',epairs,'unit words:',unit_words)
    tests=0
    for e in range(-40,41):
        if not e: continue
        b=val(e,3)
        for j in range(2,33):
            c=comb(e,j) if e>=0 else (-1)**j*comb(-e+j-1,j)
            assert val(c,3)>=b-val(j,3),(e,j,c)
            for h in range(1,5):
                assert j*h-val(j,3)>=2*h,(j,h)
                tests+=1
    print('SR5 PASS valuation checks:',tests)
    assert old_m and old_e
    print('CF1 REJECTED [T,e,survivors]:',old_m)
    print('CF2 REJECTED [k,e,unit survivors]:',old_e)
    assert ternary01(3,3) and ternary01(9,3) and 3!=1
    print('U REJECTED: 3=(10)_3 and 9=(100)_3; unit restriction is essential')
    print('ALL INDEPENDENT CHECKS PASS')

if __name__=='__main__': main()
