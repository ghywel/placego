"""GC475 independent E3 proof controls; no Local simulator imported.
P1: first odd gate a(tau) equals initial a(0).
P2: on a passing first odd gate, E3 final error equals initial c(0).
C0: binomial background matches both scalar initial/final gates.
CF0: new-bit choices can repair c(0)=1; must fail.
Unexpected: SB witness L={-5,-7},e2 passes both odd gates for every choice.
REFUTED-BY: any gate mismatch or repair; no general uniqueness claimed.
OUTCOME: P1/C0 PASS64 initial gates; P2 PASS320 E3 choices;
CF0 rejected192 blocked choices;128 survive; unexpected SB witness PASS8.
"""
from rule210_gpt_first_pulse import run,linear
if __name__=='__main__':
    gates=cases=blocked=survive=unexpected=0
    for mask in range(16):
        left={-k for j,k in enumerate((1,3,5,7)) if mask>>j&1}
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        y=run(seed,11)
        for e in (2,4,6,8):
            tau=next(s for s in range(e) if y[s][e-1-s])
            gate=y[tau][e+1-tau]
            assert gate==y[0][e+1]==linear(seed,tau,e+1-tau)
            gates+=1
            if gate:continue
            c0=y[0][e+3]
            assert y[e+3][0]==linear(seed,e+3,0)==1
            for bits in range(8):
                changed=seed^{e}
                for j in range(3):
                    if bits>>j&1:changed^={e+1+j}
                x=run(changed,e+3)
                error=x[e+3][0]^1
                assert error==c0
                assert all(x[t][0]==t%2 for t in range(e+4))==(c0==0)
                cases+=1;blocked+=c0;survive+=1-c0
                if left=={-5,-7} and e==2:
                    assert c0==0;unexpected+=1
    assert blocked and survive and unexpected==8
    print('PASS',gates,'binomial initial gates;',cases,'E3 choices;',
          blocked,'blocked;',survive,'survive; SB witness',unexpected)
