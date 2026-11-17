"""G102 CI1 preregistered through84d09c9; PASS 2026-10-06.
DepthsD0..5, all fair initial words and D neighbour race flags.
Forced target race; terminal neighbour synchronous.
Right q_D=Q_D/4, Q_0=1/2, Q_D=1/2+eps*Q_(D-1)/2.
Left q_D=1/2. Exact weights eps0,1/4,1/2,1.
Unexpected guard: adjacent right races inject where isolated race does not.
First-row open-boundary model only, no long noisy run or cone law.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def injection(old,flags,d,right):
    new={}
    indices=range(d+1,0,-1) if right else range(-d-1,0)
    sites=range(1,d+1) if right else range(-d,0)
    races=dict(zip(sites,flags))
    for i in indices:
        l=new[i-1] if not right and races.get(i,0) else old[i-1]
        r=new[i+1] if right and races.get(i,0) else old[i+1]
        new[i]=truth(l,old[i],r)
    raced=truth(old[-1] if right else new[-1],old[0],new[1] if right else old[1])
    return raced ^ truth(old[-1],old[0],old[1])


def main():
    cases=checks=0
    for right in (False,True):
        for d in range(6):
            lo,hi=(-1,d+2) if right else (-d-2,1)
            hist=Counter()
            for word in product((0,1),repeat=d+4):
                old=dict(zip(range(lo,hi+1),word))
                for flags in product((0,1),repeat=d):
                    hist[sum(flags)] += injection(old,flags,d,right)
                    cases+=1
            for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
                measured=sum(Fraction(count,2**(d+4))*eps**k*(1-eps)**(d-k)
                             for k,count in hist.items())
                q=Fraction(1,2)
                for _ in range(d):
                    q=Fraction(1,2)+eps*q/2
                expected=q/4 if right else Fraction(1,2)
                assert measured==expected
                if right:
                    limit=1/(4*(2-eps))
                    assert limit-measured==(eps/2)**(d+1)/(4*(2-eps))
                checks+=1
    old={-1:0,0:0,1:0,2:0,3:1}
    assert injection(old,(0,),1,True)==0
    assert injection(old,(1,),1,True)==1
    print('CI1 PASS:',cases,'word and flag combinations;',checks,'exact weighted checks')
    print('Right finite recurrence and remainder PASS; left conditional injection1/2')
    print('Adjacent-race guard PASS: isolated injection0, chained injection1')


if __name__=='__main__':
    main()
