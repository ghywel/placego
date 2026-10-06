"""G111 PC1-PC3 preregistered NOT RUN: publish before execution.
Exact active-flag count polynomial expansion and split determinants.
Three two-flag toys, twelve rational evaluations; no production table.
Unexpected guard: equality at eps1/2 does not mean an identically zero split.
OUTCOME 2026-10-06 20:54 BST, after d8d67d1: PC1-PC3 PASS;12 exact checks.
Coefficient vectors [0,1,-1], [0], [0,1,-3,2]; quarter-rate guard3/32.
"""
from fractions import Fraction
from itertools import product
from math import comb


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def expand(hist):
    m=len(hist)-1
    out=[0]*(m+1)
    for k,count in enumerate(hist):
        for j in range(m-k+1):
            out[k+j]+=count*comb(m-k,j)*(-1)**j
    return trim(out)


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)


def determinant(h_a,h_b,h_sa,h_sb):
    a=multiply(expand(h_sb),expand(h_a))
    b=multiply(expand(h_sa),expand(h_b))
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):
        out[i]+=x
    for i,x in enumerate(b):
        out[i]-=x
    return trim(out)


def evaluate(p,e):
    return sum(c*e**k for k,c in enumerate(p))


def main():
    checks=0
    expected=([0,1,-1],[0],[0,1,-3,2])
    for kind,predicted in enumerate(expected):
        hist=[[0]*3 for _ in range(4)]
        words=list(product((0,1),repeat=2))
        def events(x,y):
            s=(x,y,x^y)[kind]
            return (1,x,s,x*s)
        for x,y in words:
            for j,value in enumerate(events(x,y)):
                hist[j][x+y]+=value
        p=determinant(*hist)
        assert p==predicted
        for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
            probs=[sum(eps**(x+y)*(1-eps)**(2-x-y)*events(x,y)[j]
                       for x,y in words) for j in range(4)]
            direct=probs[3]*probs[0]-probs[2]*probs[1]
            assert evaluate(p,eps)==direct
            checks+=1
        print('PC'+str(kind+1),'PASS: determinant coefficients',p)
    assert checks==12
    assert evaluate(expected[2],Fraction(1,2))==0
    assert evaluate(expected[2],Fraction(1,4))==Fraction(3,32)
    print('PASS:12 exact determinant controls; half-rate equality/quarter-rate failure guard')


if __name__=='__main__':
    main()
