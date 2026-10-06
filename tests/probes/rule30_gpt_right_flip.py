"""G100 RF1 preregistered NOT RUN. Publish before execution.
Exact right-step flip triples on 64 fair six-bit words:
counts000..111 = [1,3,5,7,3,9,7,29]. Consecutive pair covariance0;
lag2 covariance1/32; variance of three-flip count5/8, not iid9/16.
Independent controls: literal Rule30 spacetime versus H triangular map;
both initial origin bits must give identical counts.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def literal(bits,origin):
    row=dict(enumerate((origin,)+bits))
    samples=[origin]
    for t in range(1,4):
        row={i:(30 >> (4*row[i-1]+2*row[i]+row[i+1])) & 1
             for i in range(t,7-t)}
        samples.append(row[t])
    return tuple(a^b for a,b in zip(samples,samples[1:]))


def transported(bits):
    row=bits
    flips=[]
    for t in range(3):
        flips.append(row[0]|row[1])
        if t<2:
            row=tuple(row[j]^(row[j+1]|row[j+2]) for j in range(len(row)-2))
    return tuple(flips)


def main():
    counts=Counter()
    for bits in product((0,1),repeat=6):
        expected=transported(bits)
        assert literal(bits,0)==literal(bits,1)==expected
        counts[expected]+=1
    histogram=[counts[f] for f in product((0,1),repeat=3)]
    assert histogram==[1,3,5,7,3,9,7,29]
    mean=[sum(Fraction(c*f[j],64) for f,c in counts.items()) for j in range(3)]
    assert mean==[Fraction(3,4)]*3
    def covariance(i,j):
        return sum(Fraction(c*f[i]*f[j],64) for f,c in counts.items())-mean[i]*mean[j]
    assert covariance(0,1)==covariance(1,2)==0
    assert covariance(0,2)==Fraction(1,32)
    variance=sum(Fraction(c,64)*(sum(f)-sum(mean))**2 for f,c in counts.items())
    assert variance==Fraction(5,8) and variance!=3*Fraction(3,16)
    print('RF1 PASS: 64 six-bit words, both origin bits, two independent formulations')
    print('Flip histogram000..111:',histogram)
    print('Adjacent covariance0; lag2 covariance1/32; count variance5/8 vs iid9/16')


if __name__=='__main__':
    main()
