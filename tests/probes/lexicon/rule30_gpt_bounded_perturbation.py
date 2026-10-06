#!/usr/bin/env python3
"""G66 BP1-BP2 published at4ad587c before first run.
BP1 MUST:32 reflected odd-left masks through9,scalar Rule90 to512;
trace at-1 equals full Rule210 mirror-extension discrepancy, vanishes
when next-power gap>10. BP2 MUST:columns1..6 to500 match baseline
outside radius9+2k+4 dyadic-boundary neighborhoods.
CF analytically refuted by G65: radius-uniform entropy bound fails.
No empirical entropy estimate. Infinite right initial data truncated
only beyond the finite comparison cones.
"""
from math import comb


def step(row,number):
    if not row:return set()
    new=set()
    for i in range(min(row)-1,max(row)+2):
        index=4*(i-1 in row)+2*(i in row)+(i+1 in row)
        if (number>>index)&1:new.add(i)
    return new


def base_seed():
    h=[]
    for n in range(264):
        bit=1
        for j in range(n):bit^=(comb(2*n+1,n-j)&1)*h[j]
        h.append(bit)
    return {2*j+1 for j,b in enumerate(h) if b}


def main():
    B=[-1];power=2
    while power<=1024:B.append(power-1);power*=2
    base=base_seed()
    baseline=[];row=base.copy()
    for t in range(513):
        baseline.append(int(-1 in row));row=step(row,210)
    patterns={0:((0,1),(0,0),(0,1),(1,0),(0,0),(1,0)),
              1:((0,1),(1,0),(0,0),(1,0),(0,1),(0,0))}
    traces=zeros=forced=excluded=0
    for mask in range(32):
        E={i for j in range(5) if (mask>>j)&1 for i in (-(2*j+1),2*j+1)}
        row=base.symmetric_difference(E)
        for t in range(513):
            assert (0 in row)==bool(t%2)
            assert int(-1 in E)==(int(-1 in row)^baseline[t])
            traces+=1
            if t and (1<<t.bit_length())-t>10:
                assert -1 not in E;zeros+=1
            if t<=500:
                n=t//2;a=1 if n==0 else (n.bit_length()-1)%2
                for k in range(1,7):
                    if any(abs(t-b)<=9+2*k+4 for b in B):
                        excluded+=1;continue
                    assert int(k in row)==patterns[a][k%6][t%2]
                    forced+=1
            E=step(E,90);row=step(row,210)
    print('BP1 PASS:',traces,'discrepancies;',zeros,'next-power zero checks')
    print('BP2 PASS:',forced,'forced samples;',excluded,'excluded')
    print('Radius-uniform CF remains G65 analytic language counterexample')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: BP1 PASS16416 discrepancies/14304 zero checks;
# BP2 PASS62432 forced samples/33760 excluded. No entropy estimate.
