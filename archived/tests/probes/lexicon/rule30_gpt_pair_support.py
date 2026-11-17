#!/usr/bin/env python3
"""G62 NG1-NG2 published at8648f02 before first run.
NG1 MUST:32 patches x(1..5) under imposed wall0 then1;
columns1-2 odd pair is absent; even pair implies s_next=0.
NG2 MUST:4096 G26 effective indices; down gates n=4^r-1 including0.
CF MUST FAIL: an odd-time columns1-2 black pair is compatible.
Unexpected guard MUST: allowed even pair survives the column2 update.
Local Dirichlet patches are not full-clock or finite witnesses.
"""
from itertools import product


def f(l,c,r):return (210>>(4*l+2*c+r))&1


def main():
    count=odd_pairs=even_pairs=guard=0
    for s,b,q,h,z in product((0,1),repeat=5):
        d=f(0,s,b);c=f(s,b,q);r=f(b,q,h);v=f(q,h,z)
        nxt=f(1,d,c)
        # Also evaluate columns2/3 at second step; no extra prediction.
        _b_next=f(d,c,r);_q_next=f(c,r,v)
        assert d*c==0
        if s*b:
            even_pairs+=1
            assert nxt==0
        if (s,d,nxt,b,c)==(1,0,0,1,1):guard+=1
        count+=1;odd_pairs+=d*c
    eff=lambda n:1 if n==0 else (n.bit_length()-1)%2
    actual=[n for n in range(4096) if eff(n)==1 and eff(n+1)==0]
    expected=[];power=1
    while power-1<4096:
        expected.append(power-1);power*=4
    assert actual==expected and actual[0]==0
    assert guard>0 and odd_pairs==0
    print('NG1 PASS:',count,'patches;',even_pairs,'even-pair patches;',guard,'guards')
    print('NG2 PASS:4096 indices; down gates',actual)
    print('CF REFUTED:0 odd pairs; permitted even-pair guard retained')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: NG1 PASS32 patches/8 even-pair guards; NG2
# PASS4096 indices; odd-pair CF REFUTED. No full-orbit assertion.
