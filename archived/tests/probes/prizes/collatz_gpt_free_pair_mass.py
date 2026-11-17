"""G41 FM1/FM2: exact endpoint mode and exceptional-event controls."""
from fractions import Fraction
from itertools import product
from math import comb
from collatz_gpt_conditioning import admissible
from collatz_gpt_pair_cancellation import direct


def counts(w, L, survivors):
    mixed = free = 0
    near = False
    for t in range(0, len(w)-1, 2):
        if t < L:
            continue
        s = sum(w[:t])
        near |= 3**s <= 2**(t+1)
        if w[t] != w[t+1]:
            mixed += 1
            v = w[:t]+(w[t+1], w[t])+w[t+2:]
            free += v in survivors
    return mixed, free, near


def main():
    modes = containments = 0
    for T in range(1, 13):
        endpoints = {}
        for w in product((0, 1), repeat=T):
            endpoints.setdefault(sum(w), []).append(w)
        for a, words in endpoints.items():
            p = Fraction(a, T)
            endpoint_mass = comb(T, a)*p**a*(1-p)**(T-a)
            assert endpoint_mass >= Fraction(1, T+1)
            modes += 1
            survivors = {w for w in words if admissible(w)}
            if not survivors:
                continue
            for L in range(T+1):
                data = {w: counts(w, L, survivors) for w in words}
                for k in range(T//2+1):
                    exceptional = {w for w, (m, f, near) in data.items() if near or m <= k}
                    bad = {w for w in survivors if data[w][1] <= k}
                    assert bad <= exceptional
                    assert len(bad)*len(words) <= T*len(exceptional)*len(survivors)
                    containments += 1
    # Away-from-one scope: no free mixed pair in the all-one endpoint.
    assert counts((1,)*12, 0, {(1,)*12})[:2] == (0, 0)
    # Frequency blindness: three independently free mixed pairs, trailing11.
    base = (1,)*4+(1, 0)*3+(1, 1)
    T, a = len(base), sum(base)
    M, h = 3**a, 3**7
    terminal = {}
    for r in range(2**T):
        w, q, valid = direct(r, T)
        if valid:
            terminal[w] = q
    cube = []
    for bits in product((0, 1), repeat=3):
        w = (1,)*4+sum(((1, 0) if b == 0 else (0, 1) for b in bits), ())+(1, 1)
        assert w in terminal
        cube.append(w)
    assert h < M
    assert len({h*terminal[w] % M for w in cube}) == 1
    assert counts(base, 0, set(cube))[1] == 3
    print(f'FM1: {modes} exact endpoint-mode inequalities; {containments} event/conditioning controls through T12')
    print('Unexpected FM2: all-one exception; 8-word/3-free-pair cube invisible to nonzero harmonic3^7')
    print('ALL CHECKS PASS; no frequency-uniform or aggregate decay inferred')


if __name__ == '__main__':
    main()
