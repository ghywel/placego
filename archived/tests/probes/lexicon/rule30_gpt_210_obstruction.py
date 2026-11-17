#!/usr/bin/env python3
"""G28 preregistered GP1/GP2/GP3/CF; no width-survival search.
OUTCOME: GP1=47, GP2 zero centres9/17/33, GP3=16 pass; CF rejected.
Independent scalar tables for210 and90 vs shift and nonlinear-residue identity.
"""
import random

def scalar(seed,rule):
    if not seed:return set()
    return {i for i in range(min(seed)-1,max(seed)+2) if (rule>>(4*int(i-1 in seed)+2*int(i in seed)+int(i+1 in seed)))&1}

def linear(seed):
    return {i-1 for i in seed}^{i+1 for i in seed}

def main():
    seeds=set()
    for parity in (0,1):
        sites=[i for i in range(-4,5) if i%2==parity]
        for mask in range(1<<len(sites)):seeds.add(frozenset(i for j,i in enumerate(sites) if mask>>j&1))
    assert len(seeds)==47
    for seed in seeds:
        a=set(seed);b=set(seed)
        for t in range(34):
            assert a==b
            if t in (9,17,33):assert 0 not in a
            a=scalar(a,210);b=scalar(b,90)
    # Frobenius identity independent of parity, with nonzero offsets.
    rng=random.Random(2306)
    for _ in range(16):
        seed={i for i in range(-4,5) if rng.randrange(2)}
        a=set(seed);b=set(seed);D=set()
        snapshots=[set(seed)]
        for t in range(33):
            v={i for i in a if i+1 in a}
            D=linear(D)^v
            a=scalar(a,210);b=scalar(b,90);snapshots.append(b)
            assert a^b==D and scalar(b,90)==linear(b)
        for k in range(1,5):
            p=1<<k
            assert snapshots[p]=={i-p for i in seed}^{i+p for i in seed}
    assert scalar({1,2},210)^scalar({1,2},90)=={1}
    assert scalar({2},210)==scalar({2},90) and 0 not in scalar({2},210)
    print('GP1 PASS47 single-parity seeds through33 steps; GP2 centres at9,17,33 all0')
    print('GP3 PASS16 nonlinear-residue/Frobenius controls; mixed seed activates gate at1')
    print('CF REJECTED: global single parity cannot give finite0101 witness')

if __name__=='__main__':main()
