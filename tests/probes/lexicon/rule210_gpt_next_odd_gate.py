"""GC473 independent next-odd gate controls, not a background census.
P1: after first even flip, next odd clock holds iff background a(tau)=0,
independent of next odd initial-bit choice.
C0: binomial background gives same gate as decimal scalar Rule210.
CF0: a next initial bit repairs a blocked gate; must fail.
Unexpected C1: the first update erases this next bit's initial choice.
REFUTED-BY: any mismatched gate, shape or successful repair.
OUTCOME: P1/C0 PASS64 vectors and32 binomial gates; CF0 rejects32
blocked choices; unexpected C1 PASS32 pairs;32 next-clock passes retained.
"""
from rule210_gpt_first_pulse import run,linear
if __name__=='__main__':
    controls=passed=blocked=erased=0
    for mask in range(8):
        left={-k for j,k in enumerate((1,3,5)) if (mask>>j)&1}
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        y=run(seed,9)
        for e in (2,4,6,8):
            tau=next(s for s in range(e) if y[s][e-1-s])
            gate=y[tau][e+1-tau]
            assert gate==linear(seed,tau,e+1-tau)
            outputs=[]
            for d in (0,1):
                altered=seed^{e}
                if d:altered^={e+1}
                x=run(altered,e+1)
                delta=[x[s][e+1-s]^y[s][e+1-s] for s in range(e+2)]
                expected=[d]+[y[s-1][e+2-s] if s<=tau+1 else gate
                               for s in range(1,e+2)]
                assert delta==expected
                assert (x[e+1][0]==1)==(gate==0)
                passed+=int(gate==0);blocked+=int(gate==1)
                controls+=1;outputs.append(delta)
            assert outputs[0][1:]==outputs[1][1:];erased+=1
    assert passed and blocked
    print('PASS',controls,'gate controls;',passed,'pass own next clock;',
          blocked,'blocked; erased choices',erased)
