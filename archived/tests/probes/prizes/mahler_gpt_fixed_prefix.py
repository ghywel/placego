#!/usr/bin/env python3
"""GC931: one CL148 prefix audit, not a start sweep or new example catalogue.
Registered before execution in CLOUD-LOCAL (2026-10-10 02:55 BST).
Target: W2=100000001000, first square W2W2; T=23,24 only.
P1: r23=449109 and r24>10**6 (informed by CL148, not blind).
C1: modular-inverse residue equals independent bitwise lift and direct replay.
CF: flip the final bit; it must change the T24 residue while retaining T23.
U: n31 satisfies the necessary coarse square-height bound but not the square.
Outcome: P1/C1/CF/U PASS; r23=449109, r24=8837717, flipped r24=449109.
No peer helpers, fractional census, trajectory extension, or data file.
"""
from fractions import Fraction


def parity(n, length):
    out = []
    for _ in range(length):
        out.append(n % 2)
        n = (3*n + 1)//2
    return out


def modular(bits):
    c = 0
    for t,b in enumerate(bits):
        c = 3*c + b*2**t
    return (-c * pow(3**len(bits), -1, 2**len(bits))) % 2**len(bits)


def lift(bits):
    r = 0
    for t,b in enumerate(bits):
        value = r
        for _ in range(t):
            value = (3*value + 1)//2
        if value % 2 != b:
            r += 2**t
    return r


def main():
    bits = list(map(int, '100000001000'*2))
    residues = {}
    for t in (23,24):
        target = bits[:t]
        r = modular(target)
        assert r == lift(target)
        assert parity(r,t) == target
        residues[t] = r
    assert residues[23] == 449109 and residues[24] > 10**6
    flipped = bits[:-1]+[1-bits[-1]]
    rf = modular(flipped)
    assert rf == lift(flipped) and parity(rf,24) == flipped
    assert rf != residues[24] and rf % 2**23 == residues[23]
    bound = Fraction(4,3)**12
    assert 32 > bound and parity(31,24) != bits
    assert modular([0]*3) == lift([0]*3) == 0
    assert parity(7,3) == [1]*3
    print({'residues':residues, 'last_bit_flip_residue':rf,
           'square_height_bound_n_plus_1':str(bound),
           'n31_height_pass_but_parity_fail':True,
           'P1':True, 'C1':True, 'CF':True, 'U':True})


if __name__ == '__main__':
    main()
