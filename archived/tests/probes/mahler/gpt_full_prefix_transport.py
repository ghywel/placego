#!/usr/bin/env python3
"""GC2939: bounded exact controls for the ancestry-preserving Mahler transport.

No imports from Local's census. All bounds and controls are fixed before launch.
"""
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import random


def walk(n, width):
    bits = []
    for _ in range(width):
        bits.append(n & 1)
        n = (3*n + (n & 1)) // 2
    return tuple(bits), n


def valid(bits):
    # Every zero-padded real tail, using exact integers (no slack automaton).
    num, den = 0, 1
    for bit in reversed(bits):
        num, den = bit*den + 2*num, 3*den
        if 2*num >= den:
            return False
    return True


def slack(bits):
    c = Fraction(1)
    for bit in bits:
        c = min(Fraction(1), 3*c/2 - bit)
        if c <= 0:
            return c
    return c


def residue(bits):
    n = 1 << len(bits)
    return -sum(bit * (1 << i) * pow(3, -i-1, n)
                for i, bit in enumerate(bits)) % n if bits else 0


def main():
    sets, full, counts = {}, {}, {'word_checks': 0, 'transport_cases': 0,
                                  'physical_starts': 0, 'long_prefix_cases': 0}
    for w in range(13):
        sets[w], full[w] = set(), []
        for n in range(1 << w):
            bits, _ = walk(n, w)
            assert residue(bits) == n
            assert valid(bits) == (slack(bits) > 0)
            if valid(bits):
                sets[w].add(n)
            if slack(bits) == 1:
                full[w].append(bits)
            counts['word_checks'] += 1
    f = [len(full[w]) for w in range(13)]
    assert all(f[n+2] <= f[n+1]+f[n] for n in range(11))
    assert all(f[n+3] <= 5*f[n] for n in range(10))

    def check(prefix, k, j, long=False):
        ell, r = len(prefix), residue(prefix)
        got, g = walk(r, ell)
        assert got == prefix and slack(prefix) == 1
        modulus = 1 << (k+j)
        multiplier = 3**ell
        image = {((v-g)*pow(multiplier, -1, modulus)) % modulus
                 for v in sets[k+j]}
        actual = 0
        for t in range(1 << k):
            n = r + (1 << ell)*t
            bits, state = walk(n, ell)
            assert bits == prefix and state == g + multiplier*t
            suffix, _ = walk(state, k+j)
            survives = valid(prefix+suffix)
            assert survives == valid(suffix) == (t in image)
            actual += survives
            counts['physical_starts'] += 1
        assert actual == sum(t < (1 << k) for t in image)
        if j == 0:
            assert actual == len(sets[k])
        counts['transport_cases'] += 1
        counts['long_prefix_cases'] += long

    for ell in range(8):
        for prefix in full[ell]:
            for k in range(1, 6):
                for j in range(4):
                    check(prefix, k, j)
    rng = random.Random(2939)
    long_prefix = tuple(b for _ in range(85) for b in (rng.randrange(2), 0, 0)) + (0, 0)
    assert len(long_prefix) == 257
    for k in range(3, 6):
        for j in range(4):
            check(long_prefix, k, j, True)

    # Deliberately break fullness: p=101 has slack 1/8, so the first 1 is illegal.
    prefix = (1, 0, 1)
    r = residue(prefix)
    actual = sum(valid(walk(r + (1 << 3)*t, 4)[0]) for t in range(2))
    assert actual != len(sets[1])
    # Same pair differences, hence same Fourier energy at every frequency;
    # different fixed top-bit collision counts. This refutes a literal identity.
    pairs = [{0, 1}, {3, 4}]
    differences = [sorted((a-b) % 8 for a in s for b in s) for s in pairs]
    collisions = [sum((a//4) == (b//4) for a in s for b in s) for s in pairs]
    assert differences[0] == differences[1] and collisions == [4, 2]
    lam = math.cos(math.pi/5)
    kappa = 1-lam
    K = 5*(1+2/lam)/(1-1/(2*lam))
    mu = 1-2*kappa/K
    delta = math.log(1/mu)/(3*math.log(2.71))
    C = mu**(-2/3)/(2*mu-1)
    print(json.dumps({'status':'PASS', 'counts':counts, 'A':[len(sets[w]) for w in range(13)],
        'F':f, 'nonfull_control':{'prefix':'101','slack':'1/8','k':1,'j':0,
                                 'actual':actual,'false_full_prediction':len(sets[1])},
        'pair_control':{'modulus':8,'sets':[sorted(s) for s in pairs],
                        'ordered_top_bit_collisions':collisions,'same_pair_differences':True},
        'unexpected_prefix':{'length':257,'seed':2939,
            'sha256':hashlib.sha256(bytes(long_prefix)).hexdigest()},
        'informational_float_constants':{'K':K,'mu':mu,'delta':delta,'C':C},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))


if __name__ == '__main__':
    main()
