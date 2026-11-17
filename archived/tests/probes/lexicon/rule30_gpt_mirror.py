#!/usr/bin/env python3
"""G65 controls published at7026fff before first run.
MX1 MUST:32 finite odd-left masks through9,mirror onto G60 right;
scalar full Rule210 through256 steps retains0101 and global parity.
MX2 MUST:256 masks through15 cover all256 even-time column1 words;
length1..8 temporal factors at starts0,1 equal the analytic count.
CF MUST FAIL: arbitrary mirrored additions preserve centre trace;
{1} versus{-2,1,2} at time2 is the published mixed-parity guard.
No blind prediction; finite controls are not an entropy estimate.
"""
from math import comb


def step(row):
    new=set()
    if not row:return new
    for i in range(min(row)-1,max(row)+2):
        index=4*(i-1 in row)+2*(i in row)+(i+1 in row)
        if (210>>index)&1:new.add(i)
    return new


def clock_seed(size):
    h=[]
    for n in range(size):
        bit=1
        for j in range(n):bit^=(comb(2*n+1,n-j)&1)*h[j]
        h.append(bit)
    return {2*j+1 for j,b in enumerate(h) if b}


def mirror(base,mask,width):
    row=base.copy()
    for j in range(width):
        if (mask>>j)&1:
            row.symmetric_difference_update({-(2*j+1),2*j+1})
    return row


def main():
    base=clock_seed(136);checks=0
    for mask in range(32):
        row=mirror(base,mask,5)
        assert {i for i in row if i<0}=={-(2*j+1) for j in range(5) if (mask>>j)&1}
        for t in range(257):
            assert (0 in row)==bool(t%2)
            assert all((t+i)%2==1 for i in row)
            checks+=1
            row=step(row)
    prefixes=set();factors={N:set() for N in range(1,9)}
    for mask in range(256):
        row=mirror(base,mask,8);trace=[]
        for t in range(16):
            assert (0 in row)==bool(t%2)
            trace.append(int(1 in row));row=step(row)
        assert not any(trace[1::2])
        prefixes.add(tuple(trace[::2]))
        for N in factors:
            for start in (0,1):factors[N].add(tuple(trace[start:start+N]))
    assert len(prefixes)==256
    counts=[]
    for N,words in factors.items():
        expected=2**((N+1)//2)+2**(N//2)-1
        assert len(words)==expected
        counts.append(len(words))
    a={1};b={-2,1,2}
    for _ in range(2):a=step(a);b=step(b)
    assert 0 not in a and 0 in b
    print('MX1 PASS:32 masks;',checks,'clock/parity time checks')
    print('MX2 PASS:256 distinct8-bit prefixes; factor counts',counts)
    print('CF REFUTED:time2 centre0 versus1 for mixed-parity mirror')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: MX1 PASS32/8224; MX2 PASS256 prefixes,
# factor counts2,3,5,7,11,15,23,31; mixed-parity CF REFUTED.
