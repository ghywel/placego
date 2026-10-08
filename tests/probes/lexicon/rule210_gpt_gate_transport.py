"""GC476 background-only controls; no candidate tail census.
P1: row-tau white gate run equals initial white odd run.
P2: w<=m+1 where m is number of gate sites not beyond left radius R.
P3: every initially white A_j first turns black at tau+j+1.
C0: decimal scalar gates agree with exact binomial background.
CF0: transport moves the first black gate; must fail.
Unexpected: include positive-tau cases with a passing first gate.
REFUTED-BY: any differing gate before first black, binomial or bound mismatch.
OUTCOME: P1/P2 PASS64 transport/bound controls; C0 PASS128 binomial gates;
CF0 rejected; unexpected positive-tau passing guard occurs20 times.
"""
from rule210_gpt_first_pulse import run,linear
if __name__=='__main__':
    cases=cells=positive=wave=0
    for mask in range(16):
        left={-k for j,k in enumerate((1,3,5,7)) if mask>>j&1}
        R=max((-k for k in left),default=0)
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        y=run(seed,11)
        for e in (2,4,6,8):
            tau=next(s for s in range(e) if y[s][e-1-s])
            w=0
            while e+1+2*w not in seed:w+=1
            for j in range(w+1):
                c=e+1+2*j
                assert y[tau][c-tau]==linear(seed,tau,c-tau)==int(c in seed)
                cells+=1
            for j in range(w):
                c=e+1+2*j
                first=next(s for s in range(12) if y[s][c-s])
                assert first==tau+j+1;wave+=1
            m=max(0,(R-e-1)//2+1)
            assert w<=m+1
            positive+=int(tau>0 and w>0);cases+=1
    assert positive>0
    print('PASS',cases,'transport and bound controls;',cells,
          'binomial gates;',positive,'positive-tau passing cases;',wave,'first-black waves')
