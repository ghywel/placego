"""G105 ZR1 predictions published throughf0f3a1b before execution.
PASS:43648 row/flag/direction cases and40 exact weighted checks.
W3..7, all old words and flags, both races.c scan directions.
Right zero-output preimages2; left2 iff no effective flags, otherwise1.
Exact eps0,1/4,1/2,1 weights test zero-row mass; no long-run rerun.
Unexpected guard: zero and one cyclic rows coalesce synchronously.
"""
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def update(old,flags,right):
    w=len(old)
    new=[0]*w
    for i in (range(w-1,-1,-1) if right else range(w)):
        l=new[i-1] if not right and flags[i] and i>0 else old[(i-1)%w]
        r=new[i+1] if right and flags[i] and i<w-1 else old[(i+1)%w]
        new[i]=truth(l,old[i],r)
    return tuple(new)


def main():
    cases=weighted=0
    for w in range(3,8):
        zero=(0,)*w
        one=(1,)*w
        assert update(zero,zero,True)==update(one,zero,True)==zero
        for right in (False,True):
            counts=[]
            for flags in product((0,1),repeat=w):
                preimages=[]
                for old in product((0,1),repeat=w):
                    new=update(old,flags,right)
                    cases+=1
                    if new==zero:
                        preimages.append(old)
                expected=[zero,one] if right or not any(flags[1:]) else [zero]
                assert set(preimages)==set(expected),(w,right,flags,preimages)
                counts.append((sum(flags),len(preimages)))
            for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
                mass=sum(eps**k*(1-eps)**(w-k)*n for k,n in counts)/2**w
                predicted=Fraction(2,2**w) if right else (1+(1-eps)**(w-1))/2**w
                assert mass==predicted,(w,right,eps,mass,predicted)
                weighted+=1
    assert cases==43648 and weighted==40
    print('ZR1 PASS:',cases,'row-flag-direction cases;',weighted,'exact weighted checks')
    print('Zero-row preimages: right2; left2 without effective flags, otherwise1')
    print('Absorbing zero and finite cyclic coalescence guards PASS')


if __name__=='__main__':
    main()
