#!/usr/bin/env python3
"""G60 controls published at6a706a9 before run.
FR1 MUST:26 nonzero masks, periods2,4,6,8;256 reconstructed odd-site
bits; scalar full Rule210 centre recovers tau through time511.
FR2 MUST: right neighbor through time510 matches G58 dyadic filter;
left parity invariant holds throughout. No claim beyond finite cones.
CF MUST FAIL:16-bit odd-site truncation preserves periodic wall forever.
REFUTED-BY: initial radius<=31; Rule90 centre is0 at64..71,
a block containing a black wall time for every nonzero mask period<=8.
Unexpected G60 guard: finite site1 seed produces a nonperiodic input.
No blind prediction. OUTCOME appended only after run.
"""
from math import comb


def reconstruct(a):
    v=[]
    for n,bit in enumerate(a):
        out=bit
        for j in range(n):
            out ^= (comb(2*n+1,n-j)&1)*v[j]
        v.append(out)
    return v


def step(row):
    # Independent scalar truth table, not the additive formula.
    new={}
    if not row:
        return new
    for i in range(min(row)-1,max(row)+2):
        idx=4*row.get(i-1,0)+2*row.get(i,0)+row.get(i+1,0)
        if (210>>idx)&1:
            new[i]=1
    return new


def main():
    walls=centres=neighbors=truncations=0
    first_fail=[]
    for p in (2,4,6,8):
        for mask in range(1,1<<(p//2)):
            def a(n):return (mask>>(n%(p//2)))&1
            def tau(t):return a(t//2) if t%2 else 0
            v=reconstruct([a(n) for n in range(256)])
            row={2*j+1:1 for j,bit in enumerate(v) if bit}
            for t in range(512):
                assert row.get(0,0)==tau(t)
                centres+=1
                assert all((t+i)%2==1 for i in row)
                if t<=510:
                    pi=0
                    if t%2==0:
                        n=t//2;power=1
                        while power<=n:
                            pi ^= a(n-power);power*=2
                        want=a(n)^pi
                    else:
                        want=0
                    assert row.get(-1,0)==pi
                    assert row.get(1,0)==want
                    neighbors+=1
                row=step(row)
            short={2*j+1:1 for j,bit in enumerate(v[:16]) if bit}
            failures=[]
            for t in range(73):
                if short.get(0,0)!=tau(t):failures.append(t)
                if 64<=t<=71:assert short.get(0,0)==0
                short=step(short)
            assert failures and any(64<=t<=71 for t in failures)
            first_fail.append(failures[0]);truncations+=1;walls+=1
    # Analytic unexpected guard: invert the wall produced by a site1 seed.
    finite_input=[comb(2*n+1,n)&1 for n in range(256)]
    assert reconstruct(finite_input)==[1]+[0]*255
    print('FR1 PASS:',walls,'walls,',centres,'centre comparisons')
    print('FR2 PASS:',neighbors,'left/right filter comparisons')
    print('CF REFUTED:',truncations,'truncations; first failures range',min(first_fail),max(first_fail))
    print('Unexpected site1 inverse guard PASS256 bits')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: FR1 PASS26/13312; FR2 PASS13286; CF REFUTED
# all26 truncations, first failures33..43; site1 inverse PASS256 bits.
