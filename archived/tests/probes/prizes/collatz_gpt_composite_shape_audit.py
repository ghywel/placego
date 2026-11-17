"""GC469 independent local UP checks, not Local's actual-law sweep.
P1: C and B(C) preserve unimodal vectors length1..5, values0..3.
C0: explicit composite row equals independent two-branch pushforward.
CF0: C(B) repairs G219; must fail. CF1: B(C) needs no input shape;
must fail on(1,0,0,1). Unexpected: zero, plateau, terminal B guards.
REFUTED-BY: any preservation failure or explicit-row mismatch.
OUTCOME: P1 HELD496; C0 PASS1364; CF0/CF1 rejected as predicted;
zero, plateau and terminal guards PASS. Hand proof is GC469.
"""
from itertools import product

def push(p,kind):
    out=[0]*(len(p)+1)
    for j,v in enumerate(p):
        for bit in (0,1):
            dest=max(0,j-bit) if kind=='B' else j+1-bit
            out[dest]+=v
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def unimodal(p):
    # Independent criterion: some index is a nondecreasing/nonincreasing mode.
    return any(all(p[i]<=p[i+1] for i in range(k)) and
               all(p[i]>=p[i+1] for i in range(k,len(p)-1))
               for k in range(len(p)))

def explicit(p):
    p=list(p)+[0,0]
    return [3*p[0]+p[1]]+[p[j-1]+2*p[j]+p[j+1]
                                 for j in range(1,len(p)-1)]

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

if __name__=='__main__':
    count=0
    for n in range(1,6):
        for p in product(range(4),repeat=n):
            assert push(push(p,'C'),'B')==trim(explicit(p))
            if unimodal(p):
                assert unimodal(push(p,'C'))
                assert unimodal(push(push(p,'C'),'B'))
                count+=1
    wrong=push(push([20,21,22,23,24],'B'),'C')
    assert wrong==[61,104,88,92,71,24] and not unimodal(wrong)
    missing=push(push([1,0,0,1],'C'),'B')
    assert not unimodal(missing)
    assert push([1],'B')==[2]
    assert push(push([0,0,0],'C'),'B')==[0]
    assert push(push([1,2,2,1],'C'),'B')==[5,7,7,4,1]
    print('PASS',count,'unimodal vectors;1364 explicit/pushforward checks;',
          'wrong order',wrong,'missing premise',missing)
