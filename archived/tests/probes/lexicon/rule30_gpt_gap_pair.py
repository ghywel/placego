#!/usr/bin/env python3
"""GC504 fixed local controls for the forbidden visible word 101001.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_gap_pair.py
PREDICTIONS registered in CLOUD-LOCAL before execution:
 GP0: visible 101 iff initial sites a,b,q,r,z satisfy a=1,b=q=0,
      r OR z=1; all 32 patches checked in both previous implementations.
 GP1: cylinder 00010 maps after two ticks to 11100 in first five sites,
      and 11100 maps to 0111 in first four, independent of sites 6,7.
 CF: gap lengths 1 then 2 can concatenate freely, refuted by GC504 proof.
 UNEXPECTED: five-site triggers close through short canalized transitions.
 OUTCOME (2026-10-08): GP0 PASS on 32 patches, GP1 PASS on 8
 transitions, each in two implementations. Local proof refutes CF.
 No longer horizon or output-count scan.
"""
from rule30_gpt_boundary_collision import packed, literal


def two_steps(seed):
    mask=(1<<7)-1
    row=seed
    for t in (0,1):
        row=(((row<<1)|t) ^ (row | (row>>1))) & mask
    black={i+1 for i in range(7) if seed>>i&1}
    for t in (0,1):
        black.discard(0)
        if t: black.add(0)
        black={i for i in range(1,max(black,default=0)+2)
               if 30>>(4*int(i-1 in black)+2*int(i in black)+int(i+1 in black))&1}
    return row, sum(1<<(i-1) for i in black if i<=7)


def main():
    for seed in range(32):
        a,b,q,r,z=[seed>>i&1 for i in range(5)]
        expect=bool(a and not b and not q and (r or z))
        assert (packed(seed,3)=='101')==expect
        assert (literal(seed,3)=='101')==expect
    for tail in range(4):
        for base,mask,target in [(8,31,7),(7,15,14)]:
            a,b=two_steps(base | (tail<<5))
            assert a&mask==target and b&mask==target
    print('GP0 PASS: 32 initial patches in two implementations')
    print('GP1 PASS: 8 canalized patch transitions in two implementations')
    print('CF refuted by local proof, not a larger word scan')
    print('ALL CHECKS PASS')


if __name__=='__main__': main()
