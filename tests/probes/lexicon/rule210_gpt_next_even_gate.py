"""GC474 exact next-even transient controls, not a prefix census.
P1: V(s+1)=E(s) XOR (1 XOR a(s) XOR O(s))*V(s).
P2: passing previous odd gate implies V(e+2)=0 for either new bit.
C0: exact binomial predecessor background matches scalar Rule210.
CF0: some passing odd gate is killed by the next even clock; must fail.
Unexpected C1: the next even initial choice is erased by its clock time.
REFUTED-BY: any vector mismatch, binomial mismatch or survivor V(e+2)=1.
OUTCOME: P1 PASS128 vectors; C0 PASS64; P2 PASS64 gate survivors;
CF0 rejected on all64 survivors; unexpected C1 PASS32 paired choices.
"""
from rule210_gpt_first_pulse import run,linear

if __name__=='__main__':
    controls=binomials=survivors=erased=0
    for mask in range(8):
        left={-k for j,k in enumerate((1,3,5)) if (mask>>j)&1}
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        y=run(seed,10)
        for e in (2,4,6,8):
            tau=next(s for s in range(e) if y[s][e-1-s])
            gate=y[tau][e+1-tau]
            assert gate==linear(seed,tau,e+1-tau)
            assert y[e+1][0]==linear(seed,e+1,0)==1
            binomials+=2
            for d in (0,1):
                outputs=[]
                for v in (0,1):
                    altered=seed^{e}
                    if d:altered^={e+1}
                    if v:altered^={e+2}
                    x=run(altered,e+2)
                    expected=[v]
                    for s in range(e+2):
                        E=int(s<=tau)
                        a=y[s][e+1-s]
                        O=d if s==0 else (y[s-1][e+2-s] if s<=tau+1 else gate)
                        expected.append(E^((1^a^O)*expected[-1]))
                    actual=[x[s][e+2-s]^y[s][e+2-s] for s in range(e+3)]
                    assert actual==expected
                    if gate==0:
                        assert actual[e+2]==0 and x[e+2][0]==0
                        survivors+=1
                    outputs.append(actual);controls+=1
                if gate==0:
                    assert outputs[0][-1]==outputs[1][-1]==0;erased+=1
    assert survivors==64 and erased==32
    print('PASS',controls,'transient vectors;',binomials,'binomial controls;',
          survivors,'passing odd gates also pass even clock;',erased,'erased pairs')
