"""G106 TF1 predictions published throughd05bb6b before execution.
PASS:43648 old-word/flag cases and60 exact weighted flip means.
D0..4 anchored right-reading recursion, all old words and flags.
Flip means for steps-1,0 are1/2; step1 has recurrence U_D.
Weights eps0,1/4,1/2,1; exact bulk remainder, finite eps1 endpoint.
Unexpected guard: invariant spatial measure does not fix temporal mean.
"""
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def main():
    cases=checks=0
    for d in range(5):
        moments=[]
        for flags_word in product((0,1),repeat=d+2):
            flags=dict(zip(range(-1,d+1),flags_word))
            counts=[0,0,0]
            for word in product((0,1),repeat=d+5):
                old=dict(zip(range(-2,d+3),word))
                new={d+1:truth(old[d],old[d+1],old[d+2])}
                for i in range(d,-2,-1):
                    r=new[i+1] if flags[i] else old[i+1]
                    new[i]=truth(old[i-1],old[i],r)
                for j,delta in enumerate((-1,0,1)):
                    counts[j]+=old[0]^new[delta]
                cases+=1
            assert counts[:2]==[2**(d+4)]*2
            moments.append((sum(flags_word),counts))
        for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
            u=Fraction(3,4)
            for _ in range(d):
                u=Fraction(3,4)-eps/4+eps*u/2
            bulk=(3-eps)/(4-2*eps)
            assert bulk-u==eps/(8-4*eps)*(eps/2)**d
            for j,target in enumerate((Fraction(1,2),Fraction(1,2),u)):
                actual=sum(eps**k*(1-eps)**(d+2-k)*c[j] for k,c in moments)/2**(d+5)
                assert actual==target,(d,eps,j,actual,target)
                checks+=1
    assert cases==43648 and checks==60
    print('TF1 PASS:',cases,'old-word-flag cases;',checks,'exact weighted flip means')
    print('Left/stay1/2; right U_D and remainder agree; bulk at eps1/2 is5/6')


if __name__=='__main__':
    main()
