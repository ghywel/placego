"""G112 WH1-WH3 preregistered NOT RUN; publish before execution.
WH1:672 effective one-step ring cases (1344 full flag assignments), white-right agreement always holds.
WH2:two seven-bit finite cylinders; pulse traces0011/0110, clean bin B.
WH3 unexpected: left-reading00001 with flag at1 violates white implication.
Counterfactual: orientation does not matter. REFUTED-BY:WH3, if predicted.
Independent controls: XOR/OR versus literal table; explicit cylinder traces.
No repetition of Local's three-tick production enumeration.
"""
from itertools import product


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def ring(old,flags,right=True):
    w=len(old)
    new=list(old)
    order=range(w-1,-1,-1) if right else range(w)
    for i in order:
        j=(i+1)%w if right else (i-1)%w
        neighbour=new[j] if flags[i] else old[j]
        l=old[(i-1)%w] if right else neighbour
        r=neighbour if right else old[(i+1)%w]
        new[i]=truth(l,old[i],r)
    return new


def cylinder(word,pulse):
    a=dict(zip(range(-3,4),word))
    b=dict(a)
    it,jt=[a[0]],[b[0]]
    for t in range(1,4):
        aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
        assert aa=={i:a[i-1]^(a[i]|a[i+1]) for i in aa}
        bb={}
        for i in sorted(aa,reverse=True):
            r=bb[i+1] if pulse and t==1 and i==0 else b[i+1]
            bb[i]=truth(b[i-1],b[i],r)
            assert bb[i]==(b[i-1]^(b[i]|r))
        a,b=aa,bb
        it.append(a[0]);jt.append(b[0])
    return tuple(it),tuple(jt)


def main():
    count=0
    for w in range(3,6):
        for old in product((0,1),repeat=w):
            ideal=[old[(i-1)%w]^(old[i]|old[(i+1)%w]) for i in range(w)]
            for effective in product((0,1),repeat=w-1):
                raced=ring(old,effective+(0,))
                for j in range(w):
                    if ideal[(j+1)%w]==raced[(j+1)%w]==0:
                        assert ideal[j]==raced[j]
                count+=1
    assert count==672  # effective flags only; terminal flag is disabled
    print('WH1 PASS:672 effective cases, equivalent to1344 full flag assignments')
    i,j=cylinder((0,0,0,0,0,1,0),True)
    assert (i,j)==((0,0,1,1),(0,1,1,0))
    i,j=cylinder((0,1,1,0,0,0,0),False)
    assert i==j and i[1:3]==(1,1)
    print('WH2 PASS:two positive finite cylinders and independent XOR/OR controls')
    old=(0,0,0,0,1)
    ideal=[old[(i-1)%5]^(old[i]|old[(i+1)%5]) for i in range(5)]
    raced=ring(old,(0,1,0,0,0),False)
    assert ideal[2]==raced[2]==0 and ideal[1]!=raced[1]
    print('WH3 PASS:orientation-free white-agreement counterfactual refuted')


if __name__=='__main__':
    main()
