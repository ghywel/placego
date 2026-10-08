#!/usr/bin/env python3
"""GC549 CP30; preregistered before first run in retained checkpoint record.
Canonical prefix11100; classify time12 sites2,3 using1024 source rows of15 sites.
P1 blind: pair depends only on source sites6..8.
C1: independent literal trace equals CP29 paired trace on every source.
CF: all8 three-bit tails permit pair01; must fail by CP29.
Unexpected: retain all possible pairs when dependence reaches farther.
REFUTED-BY: C1 mismatch, multiple pairs in a bucket, or all buckets permit01.
OUTCOME: C1 PASS; P1 REFUTED in4 of8 buckets; CF REFUTED.
Only source tail001 permits pair01. The finite cone supplies a necessary
3-gap entry condition, not the final2-gap exclusion or a hand proof.
"""
from itertools import product
from rule30_gpt_gap_continuation import literal_trace, paired_trace

def main():
    buckets = {}
    for tail in product((0,1), repeat=10):
        source = (1,1,1,0,0) + tail
        assert literal_trace(source) == paired_trace(source)
        row = list(source)
        for t in range(12):
            left = [t%2] + row[:-1]
            row = [(30 >> (4*left[j]+2*row[j]+row[j+1])) & 1
                   for j in range(len(row)-1)]
        buckets.setdefault(''.join(map(str,tail[:3])),set()).add(
            ''.join(map(str,row[1:3])))
    print({k: sorted(v) for k,v in buckets.items()})
    assert [k for k,v in buckets.items() if '01' in v] == ['001']
    print('C1 PASS; P1 REFUTED; CF REFUTED;1024 source rows, complete cone')

if __name__ == '__main__':
    main()
