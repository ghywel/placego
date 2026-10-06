"""G101 IF1 preregistered NOT RUN: publish before execution.
Observer p_t=floor(3t/4), t0..4; all512 inputs at sites-1..7.
Four-flip histogram = 4*[1,3,5,7,3,9,7,29] for each first-bit value.
Mean11/4, variance7/8 versus independent13/16; covariance(1,3)=1/32.
First stay flip independent of the entire subsequent triple.
No long-ray rerun, selected seed or asymptotic variance assertion.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def main():
    counts=Counter()
    for word in product((0,1),repeat=9):
        row=dict(zip(range(-1,8),word))
        samples=[row[0]]
        for t in range(1,5):
            row={i:(30 >> (4*row[i-1]+2*row[i]+row[i+1])) & 1
                 for i in range(-1+t,8-t)}
            samples.append(row[(3*t)//4])
        flips=tuple(a^b for a,b in zip(samples,samples[1:]))
        counts[flips]+=1
    triple=[1,3,5,7,3,9,7,29]
    histogram=[counts[f] for f in product((0,1),repeat=4)]
    assert histogram==[4*c for c in triple]*2
    means=[sum(Fraction(c*f[i],512) for f,c in counts.items()) for i in range(4)]
    assert means==[Fraction(1,2)]+[Fraction(3,4)]*3
    for i in range(4):
        for j in range(i+1,4):
            cov=sum(Fraction(c*f[i]*f[j],512) for f,c in counts.items())-means[i]*means[j]
            assert cov==(Fraction(1,32) if (i,j)==(1,3) else 0)
    mean=sum(means)
    variance=sum(Fraction(c,512)*(sum(f)-mean)**2 for f,c in counts.items())
    assert mean==Fraction(11,4) and variance==Fraction(7,8)
    assert variance!=Fraction(13,16)
    print('IF1 PASS: all512 inputs at sites-1..7; exact four-flip histogram')
    print('Histogram0000..1111:',histogram)
    print('Mean11/4; variance7/8 vs independent13/16; covariance(1,3)=1/32')


if __name__=='__main__':
    main()
