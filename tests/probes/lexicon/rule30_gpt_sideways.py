"""Sideways two-track map audit, preregistered 2026-10-06.

SI0 must: F(a,b)=(S a XOR(a OR b),a) agrees with inverse Rule30 and commutes
  with the time shift for all periodic input pairs, P1..8.
SI1 must: image(c,a) iff c XOR S a contains every1 of a; each compatible
  output has exactly2**popcount(a) predecessors, all P1..8.
SI2 must: encode(c,a) as symbol2 where a=1, otherwise c. Its inverse uses
  c=1-a(next) at symbol2. Exactly3**P image words, P1..8.
SI3 unexpected must: uniform image words have second-track density1/3,
  whereas uniform inputs pushed through F have density1/2, P1..8.
SI4 must: conjugating F restricted to its image gives the stated radius-two
  ternary CA; compare every ternary periodic word at P1..6.
CF1 must fail: F is injective (a all1, b all0/all1 have the same output).
CF2 must fail: F maps its image onto itself (period-two output(c=10,a=00)
  has a unique predecessor outside the image, also excluding any nonperiodic
  predecessor of that bi-infinite periodic output).
REFUTED-BY: any count, fibre, recoding or local-rule mismatch invalidates the
  structural instrument. Image growth is not F's dynamical entropy.
OUTCOME: pending. Small exact classification, no Local job duplicated.
"""

from collections import Counter
from itertools import product


def shift(w,p):
    return (w >> 1) | ((w & 1) << (p-1))


def forward(a,b,p):
    return shift(a,p) ^ (a | b), a


def compatible(c,a,p):
    v = c ^ shift(a,p)
    return v & a == a


def encode(c,a,p):
    return tuple(2 if (a >> t) & 1 else (c >> t) & 1 for t in range(p))


def decode(z):
    p = len(z)
    a = sum(int(x == 2) << t for t,x in enumerate(z))
    c = sum((1-int(z[(t+1) % p] == 2) if x == 2 else x) << t
            for t,x in enumerate(z))
    return c,a


def ternary_step(z):
    out = []
    for t,x in enumerate(z):
        y,q = z[(t+1) % len(z)], z[(t+2) % len(z)]
        if x == 1:
            out.append(2)
        elif x == 0:
            out.append(y if y != 2 else 1-int(q == 2))
        else:
            out.append(2 if y != 2 else int(q == 2))
    return tuple(out)


def main():
    total = 0
    for p in range(1,9):
        n = 1 << p
        counts = Counter()
        for a,b in product(range(n), repeat=2):
            out = forward(a,b,p)
            c = sum((((a >> ((t+1) % p)) & 1) ^
                     (((a >> t) & 1) | ((b >> t) & 1))) << t
                    for t in range(p))
            assert out == (c,a)
            assert forward(shift(a,p),shift(b,p),p) == tuple(shift(x,p) for x in out)
            counts[out] += 1
            total += 1
        for c,a in product(range(n), repeat=2):
            assert bool(counts[c,a]) == compatible(c,a,p)
            if counts[c,a]:
                assert counts[c,a] == 2**a.bit_count()
                assert decode(encode(c,a,p)) == (c,a)
        codes = {encode(c,a,p) for c,a in counts}
        assert len(codes) == 3**p
        assert len(counts) == 3**p
        assert sum(a.bit_count() for c,a in counts) == p*3**(p-1)
        assert sum(a.bit_count()*v for (c,a),v in counts.items()) == p*4**p//2
        print('P',p,'inputs',4**p,'image',len(counts),'fibres/recoding/densities PASS')
    print('SI0-SI3 PASS:',total,'input pairs; exact fibres and ternary image')
    checked = 0
    for p in range(1,7):
        for z in product(range(3),repeat=p):
            a,b = decode(z)
            assert encode(*forward(a,b,p),p) == ternary_step(z)
            checked += 1
    print('SI4 PASS:',checked,'ternary periodic words')
    assert forward(3,0,2) == forward(3,3,2)
    assert forward(0,1,2) == (1,0)
    assert compatible(1,0,2) and not compatible(0,1,2)
    print('CF1/CF2 FAIL AS REQUIRED: noninjective; image not onto itself')
    print('ALL CONTROLS PASS')


if __name__ == '__main__':
    main()
