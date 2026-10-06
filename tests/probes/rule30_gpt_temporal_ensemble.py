"""G97 SC3 preregistered NOT RUN: publish before execution.
All left/stay observer paths length1..4: uniform sampled/flip words,
flip-count expectation N/2, variance N/4. Right-step guard: 3/4 flips.
Enumerate initial words on complete finite cones; no padded cells used.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def traces(increments):
    positions = [0]
    for step in increments:
        positions.append(positions[-1]+step)
    lo = min(p-t for t,p in enumerate(positions))
    hi = max(p+t for t,p in enumerate(positions))
    samples = Counter()
    for word in product((0,1), repeat=hi-lo+1):
        row = dict(zip(range(lo,hi+1),word))
        trace = [row[0]]
        for t,p in enumerate(positions[1:],1):
            row = {i:(30 >> (4*row[i-1]+2*row[i]+row[i+1])) & 1
                   for i in range(lo+t,hi-t+1)}
            trace.append(row[p])
        samples[tuple(trace)] += 1
    return samples


def main():
    paths = words = 0
    for n in range(1,5):
        for increments in product((-1,0),repeat=n):
            samples = traces(increments)
            assert len(samples) == 2**(n+1)
            assert len(set(samples.values())) == 1
            multiplicity = next(iter(samples.values()))
            flips = Counter()
            for sample,count in samples.items():
                flips[tuple(a^b for a,b in zip(sample,sample[1:]))] += count
            assert len(flips) == 2**n
            assert set(flips.values()) == {2*multiplicity}
            total = sum(flips.values())
            mean = sum(Fraction(sum(f)*c,total) for f,c in flips.items())
            variance = sum(Fraction(c,total)*(sum(f)-mean)**2 for f,c in flips.items())
            assert mean == Fraction(n,2) and variance == Fraction(n,4)
            words += sum(samples.values())
            paths += 1
    guard = traces((1,))
    flip = sum(c for s,c in guard.items() if s[0]^s[1])
    assert Fraction(flip,sum(guard.values())) == Fraction(3,4)
    print('SC3 PASS:',paths,'observer paths,',words,'initial words; uniform samples/flips')
    print('SC3 moments PASS: exact mean N/2 and variance N/4 for every path')
    print('Right-step scope guard PASS: 3/4 flips, not1/2')


if __name__ == '__main__':
    main()
