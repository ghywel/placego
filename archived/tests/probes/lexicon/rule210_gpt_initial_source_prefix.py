#!/usr/bin/env python3
"""GC454 preregistered128 seeds, seven positive bits, empty left, centre times0..7.
Blind prediction: both V_1(3) values survive01010101. Outcome: REFUTED.
Scalar/bit-vector and site8 causal-tail controls; no larger census or full-clock construction.
RUN-ON: CPU, Python standard library. No data written into Git.
"""
import json

def scalar(seed):
    row=set(seed); trace=[]; source=None
    for t in range(8):
        trace.append(int(0 in row))
        if t==1: source=int(3 in row and 4 in row)
        row={i for i in range(-8,17) if (210>>(4*int(i-1 in row)+2*int(i in row)+int(i+1 in row)))&1}
    return trace,source

def bitvector(seed):
    word=sum(1<<(i+8) for i in seed); mask=(1<<25)-1; trace=[]; source=None
    for t in range(8):
        trace.append((word>>8)&1)
        if t==1: source=((word>>11)&1)*((word>>12)&1)
        word=((word<<1)^((~word)&(word>>1)))&mask
    return trace,source

def main():
    survivors={0:[],1:[]}; unrestricted={0:0,1:0}
    for bits in range(128):
        seed=[i+1 for i in range(7) if bits>>i&1]
        trace,source=scalar(seed)
        assert (trace,source)==bitvector(seed)
        assert (trace,source)==scalar(seed+[8])
        unrestricted[source]+=1
        if trace==[t%2 for t in range(8)]: survivors[source].append(seed)
    print(json.dumps({'controls':128,'survivors':survivors,'unrestricted_counts':unrestricted,
                      'blind_both_survive':bool(survivors[0] and survivors[1])}))

if __name__=='__main__': main()
