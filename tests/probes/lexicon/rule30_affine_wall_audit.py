#!/usr/bin/env python3
"""C7 second-reading controls; preregistered before execution, 2026-10-07.

Known before running: C7/G138 give the formal depth-four product A*B;
Lemma3 forbids consecutive visible ones for a real right half. Hand
substitution predicts the table below through depth7 on that restricted domain.
P1 (derived control): every one of 256 finite right seeds matches the table.
P2 (not observed): with D=0, all four (B,E) combinations occur; the depth7
    odd output has mixed XOR difference1, unlike an affine function.
C1: all eight lookup-table updates agree with the Boolean Rule30 formula.
CF: applying the same phase-specific table beside wall1010 must fail.
U: hidden odd-time column1 bits are supplied literally to the inverse;
    independently zeroing them must leave its forced columns unchanged.
CPU, standard library, <1s expected; one width8 enumeration, no extension.
OUTCOME (2026-10-07, GPT Intel CPU, one run): P1/P2/C1/CF/U PASS,
256 seeds; opposite-phase mismatches256. Witness seeds for (B,E)=
00,01,10,11 are01101000,00100000,00000000,00000010, respectively;
all have A=D=0, outputs1,1,0,1, mixed XOR1. No extension.
REFUTED-BY: CF phase-specific table fails on all256 shifted-wall seeds.
No initial-tail or prize conclusion.
"""
from itertools import product


def right_trace(seed, phase):
    row = list(seed) + [0]*10
    trace = []
    for t in range(10):
        trace.append(row[0])
        padded = [(t+phase) % 2] + row + [0]
        row = [(30 >> (4*l+2*c+r)) & 1
               for l,c,r in zip(padded,padded[1:],padded[2:])]
    return trace


def inverse(trace, phase):
    cols = [[(t+phase) % 2 for t in range(10)]]
    older = trace
    for _ in range(7):
        inner = cols[-1]
        out = [inner[t+1] ^ (inner[t] | older[t])
               for t in range(len(inner)-1)]
        older = inner
        cols.append(out)
    return [(c[0],c[1]) for c in cols[1:]]


def expected(trace):
    a,b,d,e = trace[0::2][:4]
    return [(1-a,1),(a,b),(1-b,1-b),(0,d),
            ((1-b)^d,1-b),(d,b^d^e),(1^d^e,1^e^(b&e))]


def main():
    for l,c,r in product((0,1), repeat=3):
        assert (30 >> (4*l+2*c+r)) & 1 == l ^ (c | r)
    witnesses = {}
    phase_misses = 0
    for seed in product((0,1), repeat=8):
        trace = right_trace(seed,0)
        a,b,d,e = trace[0::2][:4]
        assert not (a&b or b&d or d&e)
        got = inverse(trace,0)
        assert got == expected(trace), (seed,trace,got,expected(trace))
        hidden_zero = [v if t%2==0 else 0 for t,v in enumerate(trace)]
        assert inverse(hidden_zero,0) == got
        if d == 0:
            witnesses.setdefault((b,e),(seed,got[-1][1]))
        shifted = right_trace(seed,1)
        phase_misses += inverse(shifted,1) != expected(shifted)
    assert set(witnesses) == set(product((0,1), repeat=2)), witnesses
    assert sum(v[1] for v in witnesses.values()) % 2 == 1
    assert phase_misses > 0
    print('P1 P2 C1 CF U PASS; 256 seeds; phase mismatches',phase_misses)
    for bits,(seed,value) in sorted(witnesses.items()):
        print('B,E',bits,'seed',''.join(map(str,seed)),'depth7 odd',value)


if __name__ == '__main__':
    main()
