"""G116 PE0-PE2 preregistered NOT RUN;publish before execution.
512 nine-bit words through4 ticks;isolated source right pulse on tick1.
PE0 must echo F,0,F. PE1 E4=F*(I1 XOR I2 XOR I3),32 fourth errors.
64 injections,448 noninjections. PE2 injected ideal triples8 words8 each;
I2,I3 bins8/16 errors but I1 refinements deterministic.
Unexpected shallow-average guard;REFUTED-BY:PE2 last-two-sample sufficiency.
Independent literal-table/XOR-OR updates;no repeated-race job.
OUTCOME 2026-10-06 21:25 BST after241fb49:PE0-PE2 PASS.
512 words;64 injections,32 fourth errors;8 ideal triples8 each.
"""
from collections import Counter
from itertools import product


def truth(l,c,r):
    return (30>>(4*l+2*c+r))&1


def main():
    triples=Counter();shallow=Counter();refined=Counter()
    injections=errors=0
    for word in product((0,1),repeat=9):
        a=dict(zip(range(-4,5),word));b=dict(a)
        ii=[a[0]];ee=[0]
        for t in range(1,5):
            aa={i:truth(a[i-1],a[i],a[i+1]) for i in range(min(a)+1,max(a))}
            bb={i:truth(b[i-1],b[i],b[i+1]) for i in aa}
            if t==1:
                bb[0]=truth(b[-1],b[0],bb[1])
            for i in aa:
                right=bb[1] if t==1 and i==0 else b[i+1]
                assert aa[i]==(a[i-1]^(a[i]|a[i+1]))
                assert bb[i]==(b[i-1]^(b[i]|right))
            a,b=aa,bb;ii.append(a[0]);ee.append(a[0]^b[0])
        f=int(word[4:7]==(0,0,1))
        assert ee[1:4]==[f,0,f]
        assert ee[4]==f*(ii[1]^ii[2]^ii[3])
        injections+=f;errors+=ee[4]
        if f:
            triples[tuple(ii[1:4])]+=1
            shallow[ii[2],ii[3],ee[4]]+=1
            refined[ii[1],ii[2],ii[3],ee[4]]+=1
    assert (injections,errors)==(64,32)
    assert len(triples)==8 and set(triples.values())=={8}
    assert len(shallow)==8 and set(shallow.values())=={8}
    assert len(refined)==8 and set(refined.values())=={8}
    print('PE0 PASS:512 histories;64 injections,448 noninjections;source echo')
    print('PE1 PASS:gated three-sample parity;32 fourth errors')
    print('PE2 PASS:8 injected ideal triples8 times each;shallow8/16 versus deterministic I1 refinement')


if __name__=='__main__':
    main()
