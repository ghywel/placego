#!/usr/bin/env python3
"""GC549 fixed certificate audit; preregistered 2026-10-08 before this replay.
Scope: phase zero, horizon 17, nine visible symbols, depths 13..17 only.
C1: reduced polynomial recurrence equals an independent time-column inverse
    on all 89 no-11 codes (and all initial depths 1..17).
C2: the five printed checkpoint19 polynomials equal regenerated polynomials.
P1: eleven free codes pass the band; no-11 leaves only 010101001;
    adding 101001 excludes it. This replays CP18, not a new record search.
CF: no-11 alone excludes the band; must fail on 010101001.
Unexpected check: depth17 retains monomial c1*c3*c5*c7.
REFUTED-BY: any coefficient mismatch, inverse mismatch or changed code set.
No actual-right enumeration, SAT, increased horizon or asymptotic claim.
OUTCOME (GPT, 2026-10-08): C1 PASS, 89 codes at depths 1..17;
C2 PASS, five coefficient expressions; P1 HELD, eleven free codes,
sole no-11 survivor 010101001, excluded by 101001; CF REFUTED;
unexpected quartic PASS. Single-party replay, not independent second reading.
"""
from itertools import product

ZERO = frozenset()
ONE = frozenset({frozenset()})

def add(a, b):
    return a ^ b

def mul(a, b):
    result = set()
    for x in a:
        for y in b:
            z = x | y
            if any(i + 1 in z for i in z):
                continue
            if z in result:
                result.remove(z)
            else:
                result.add(z)
    return frozenset(result)

def either(a, b):
    return add(add(a, b), mul(a, b))

def shift(a):
    return frozenset(frozenset(i + 1 for i in x) for x in a)

def polynomials():
    f, g = [ZERO, add(ONE, frozenset({frozenset({0})}))], [ONE, ONE]
    for j in range(1, 17):
        f.append(add(g[j], either(f[j], f[j-1])))
        g.append(add(shift(f[j]), either(g[j], g[j-1])))
    return f

def scalar_inverse(code):
    # Time columns, independent of polynomial operations and pair grouping.
    wall = [t % 2 for t in range(18)]
    right = [code[t//2] if t % 2 == 0 else 0 for t in range(17)]
    out = [0]
    for _ in range(17):
        left = [wall[t+1] ^ (wall[t] | right[t]) for t in range(len(wall)-1)]
        out.append(left[0])
        right, wall = wall, left
    return out

def evaluate(p, code):
    value = 0
    for term in p:
        value ^= int(all(code[i] for i in term))
    return value

def parse(s):
    return frozenset(frozenset() if term == '1' else frozenset(map(int, term.split(',')))
                     for term in s.split(';'))

PRINTED = [
 '1;3;4;5;6;1,3;2,5',
 '4;6;1,3;2,4;2,5;3,5;4,6;1,3,6',
 # CP19 prints p14+p15, rather than p15 itself.
 '1;5;7;3,6;2,4,6',
 '5;2,4;2,5;3,7;4,6;4,7;1,3,5;1,3,7;2,4,6;2,4,7;2,5,7',
 '1;4;5;8;1,3;3,7;4,6;1,3,6;1,3,7;2,4,6;2,4,7;1,3,5,7',
]

def main():
    f = polynomials()
    expressions = [f[13], f[14], add(f[14], f[15]), f[16], f[17]]
    assert expressions == [parse(s) for s in PRINTED], 'C2 coefficients'
    codes = list(product((0, 1), repeat=9))
    free = [c for c in codes if not any(scalar_inverse(c)[13:18])]
    allowed = [c for c in codes if not any(c[i] and c[i+1] for i in range(8))]
    for c in allowed:
        assert [evaluate(p, c) for p in f] == scalar_inverse(c), ('C1', c)
    surviving = [''.join(map(str, c)) for c in free if c in allowed]
    assert len(allowed) == 89 and len(free) == 11
    assert surviving == ['010101001']
    assert not [w for w in surviving if '101001' not in w]
    assert frozenset({1, 3, 5, 7}) in f[17]
    print('C1 PASS: 89 codes, 17 depths; C2 PASS: five expressions')
    print('P1 HELD: 11 free codes, sole no-11 survivor 010101001; gap restriction excludes')
    print('CF REFUTED: no-11 alone is insufficient; unexpected quartic PASS')

if __name__ == '__main__':
    main()
