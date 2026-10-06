"""G103 CP1 preregistered through43095bf; PASS 2026-10-06.
W3..5,T1..2, all rows and flags, both sequential race directions.
Clean backward cone forces agreement, despite arbitrary outside flags.
Exact weighted disagreement <=1-(1-eps)^M<=1-(1-eps)^(T*T).
Weights eps0,1/4,1/2,1. Final unflagged target alone is insufficient.
No stochastic scaling fit, effective-cone assumption or Local rerun.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def sync(row):
    w=len(row)
    return tuple(truth(row[(i-1)%w],row[i],row[(i+1)%w]) for i in range(w))


def noisy(row,flags,right):
    w=len(row)
    new=[0]*w
    for i in (range(w-1,-1,-1) if right else range(w)):
        l=new[i-1] if not right and flags[i] and i>0 else row[(i-1)%w]
        r=new[i+1] if right and flags[i] and i<w-1 else row[(i+1)%w]
        new[i]=truth(l,row[i],r)
    return tuple(new)


def main():
    cases=checks=0
    for w in range(3,6):
        for t in (1,2):
            cones=[{(s-1)*w+(i+d)%w for s in range(1,t+1)
                    for d in range(-(t-s),t-s+1)} for i in range(w)]
            for right in (False,True):
                hist=[Counter() for _ in range(w)]
                for initial in product((0,1),repeat=w):
                    ideal=initial
                    for _ in range(t):
                        ideal=sync(ideal)
                    for flags in product((0,1),repeat=w*t):
                        row=initial
                        for s in range(t):
                            row=noisy(row,flags[s*w:(s+1)*w],right)
                        k=sum(flags)
                        for i in range(w):
                            if all(not flags[j] for j in cones[i]):
                                assert row[i]==ideal[i]
                            hist[i][k]+=row[i]!=ideal[i]
                        cases+=1
                for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
                    for i in range(w):
                        p=sum(Fraction(c,2**w)*eps**k*(1-eps)**(w*t-k)
                              for k,c in hist[i].items())
                        bound=1-(1-eps)**len(cones[i])
                        assert p<=bound<=1-(1-eps)**(t*t)
                        assert p<=eps*t*t
                        checks+=1
    initial=(0,0,1,0,0)
    ideal=sync(sync(initial))
    first=noisy(initial,(1,0,0,0,0),True)
    final=noisy(first,(0,0,0,0,0),True)
    assert final[1]!=ideal[1]
    print('CP1 PASS:',cases,'row and flag histories;',checks,'weighted site bounds')
    print('Clean-cone agreement PASS for every case and site')
    print('Unexpected guard PASS: final unflagged target differs after an earlier ancestor race')


if __name__=='__main__':
    main()
