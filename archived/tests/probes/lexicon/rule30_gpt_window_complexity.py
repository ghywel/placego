#!/usr/bin/env python3
"""G64 predictions published atb917fb4 before first run.
WC1 MUST: k1..6,N1,2,4,8,16,32,64,128,starts0..4095:
early boundary count<=Q, marked samples<=(4k+1)Q;
late boundary count<=1, marked samples<=4k+1.
WC2 MUST: G60's scalar full0101 orbit,columns1..6,times0..500;
outside radius2k boundary neighborhoods, G63 template agrees.
CF REFUTED analytically in G64: sparse prefixes do not imply low
factor entropy. No empirical entropy estimate or blind prediction.
"""
from bisect import bisect_left,bisect_right
from math import comb


def boundaries(limit):
    out=[-1];power=2
    while power-1<=limit:
        out.append(power-1);power*=2
    return out


def scalar_step(row):
    new={}
    if not row:return new
    for i in range(min(row)-1,max(row)+2):
        index=4*row.get(i-1,0)+2*row.get(i,0)+row.get(i+1,0)
        if (210>>index)&1:new[i]=1
    return new


def main():
    B=boundaries(8192);windows=early=late=0
    for k in range(1,7):
        r=2*k
        for N in (1,2,4,8,16,32,64,128):
            L=N+2*r;M=1<<L.bit_length();Q=M.bit_length()
            assert M>=L+1 and M<2*(L+1)
            for u in range(4096):
                near=B[bisect_left(B,u-r):bisect_right(B,u+N-1+r)]
                marked=set()
                for b in near:
                    marked.update(range(max(u,b-r),min(u+N-1,b+r)+1))
                if u<M+r:
                    assert len(near)<=Q and len(marked)<=(2*r+1)*Q
                    early+=1
                else:
                    assert len(near)<=1 and len(marked)<=2*r+1
                    late+=1
                windows+=1
    v=[]
    for n in range(256):
        bit=1
        for j in range(n):bit^=(comb(2*n+1,n-j)&1)*v[j]
        v.append(bit)
    row={2*j+1:1 for j,bit in enumerate(v) if bit}
    patterns={0:((0,1),(0,0),(0,1),(1,0),(0,0),(1,0)),
              1:((0,1),(1,0),(0,0),(1,0),(0,1),(0,0))}
    B=boundaries(1024);samples=omitted=0
    for t in range(501):
        n=t//2;a=1 if n==0 else (n.bit_length()-1)%2
        for k in range(1,7):
            if any(abs(t-b)<=2*k for b in B):
                omitted+=1;continue
            assert row.get(k,0)==patterns[a][k%6][t%2]
            samples+=1
        row=scalar_step(row)
    print('WC1 PASS:',windows,'windows;',early,'early,',late,'late')
    print('WC2 PASS:',samples,'forced samples;',omitted,'excluded samples')
    print('CF remains the analytic concatenated-word counterexample; no entropy estimate')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: WC1 PASS196608 windows (3952 early/192656 late);
# WC2 PASS2524 forced samples,482 omitted. No empirical entropy estimate.
