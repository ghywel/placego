"""G104 OM1-OM2 preregistered NOT RUN: publish before execution.
OM1 widths1..4, all right flags and fixed three-bit tails:
right update maps each old block bijectively onto output blocks.
OM2 anchored left depths0..3, every old row and flag pattern:
density1/2, pair disagreement1/2 or3/4 according to the right cell's flag.
Exact Bernoulli weights give pair disagreement1/2+eps/4.
Unexpected guard: unchanged density does not imply unchanged pair law.
Infinite-bulk theorem controls, no finite cyclic or scaling rerun.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def main():
    right_cases=left_cases=weighted=0
    for width in range(1,5):
        for flags in product((0,1),repeat=width):
            for tail in product((0,1),repeat=3):
                counts=Counter()
                for prefix in product((0,1),repeat=width):
                    old=dict(zip(range(-1,width-1),prefix))
                    old.update(zip(range(width-1,width+2),tail))
                    new={width:truth(old[width-1],old[width],old[width+1])}
                    for i in range(width-1,-1,-1):
                        new[i]=truth(old[i-1],old[i],new[i+1] if flags[i] else old[i+1])
                    out=tuple(new[i] for i in range(width))
                    counts[out]+=1
                    # Independent inverse: XOR algebra, with the tail held fixed.
                    recovered=dict(zip(range(width-1,width+2),tail))
                    inverse_new={width:truth(*tail)}
                    for i in range(width-1,-1,-1):
                        r=inverse_new[i+1] if flags[i] else recovered[i+1]
                        recovered[i-1]=out[i]^(recovered[i]|r)
                        inverse_new[i]=out[i]
                    assert all(recovered[i]==old[i] for i in range(-1,width-1))
                    right_cases+=1
                assert len(counts)==2**width and set(counts.values())=={1}
    for d in range(4):
        flag_moments=[]
        for bits in product((0,1),repeat=d+2):
            flags=dict(zip(range(-d,2),bits))
            counts=Counter()
            for word in product((0,1),repeat=d+5):
                old=dict(zip(range(-d-2,3),word))
                new={}
                for i in range(-d-1,2):
                    l=new[i-1] if flags.get(i,0) else old[i-1]
                    new[i]=truth(l,old[i],old[i+1])
                counts[new[0],new[1]]+=1
                left_cases+=1
            total=2**(d+5)
            means=[Fraction(sum(c*p[i] for p,c in counts.items()),total) for i in (0,1)]
            pair=Fraction(counts[0,1]+counts[1,0],total)
            assert means==[Fraction(1,2)]*2
            assert pair==(Fraction(3,4) if bits[-1] else Fraction(1,2))
            flag_moments.append((sum(bits),means,pair))
        for eps in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
            for i in (0,1):
                mean=sum(eps**k*(1-eps)**(d+2-k)*m[i] for k,m,p in flag_moments)
                assert mean==Fraction(1,2)
                weighted+=1
            pair=sum(eps**k*(1-eps)**(d+2-k)*p for k,m,p in flag_moments)
            assert pair==Fraction(1,2)+eps/4
            weighted+=1
    print('OM1 PASS:',right_cases,'right input cases; fixed-tail bijection and inverse')
    print('OM2 PASS:',left_cases,'left input cases;',weighted,'weighted moments')
    print('Density1/2 both ways; left pair disagreement1/2+eps/4, not invariant fair pairs')


if __name__=='__main__':
    main()
