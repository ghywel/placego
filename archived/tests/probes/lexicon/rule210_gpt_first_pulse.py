"""GC472 controls for the uniform first-deviation pulse lemma.
P1: odd first flip at e fails centre clock at time e.
P2: even first flip has Delta_e(s)=1 iff s<=first black D_(e-1).
C0: independent exact binomial background matches literal Rule210.
CF0: odd first flip passes its clock; must fail on every odd e.
Unexpected: a black predecessor at time0 gives a one-sample pulse.
REFUTED-BY: any incorrect pulse, odd clock equality or background mismatch.
OUTCOME: P1/P2 HELD64; C0 PASS352; CF0 rejected32 odd flips;
unexpected initial-black predecessor gives20 one-sample pulses.
"""
from math import comb

def run(seed,n):
    row={i:int(i in seed) for i in range(-20,21)};out=[row]
    for t in range(n):
        row={i:(210>>(4*row.get(i-1,0)+2*row.get(i,0)+row.get(i+1,0)))&1
             for i in range(-20,21)}
        out.append(row)
    return out

def linear(seed,t,i):
    return sum((comb(t,k)&1)*int(i-t+2*k in seed)
               for k in range(t+1))%2

if __name__=='__main__':
    count=checks=immediate=0
    for mask in range(8):
        left={-k for j,k in enumerate((1,3,5)) if (mask>>j)&1}
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        y=run(seed,8)
        for e in range(1,9):
            x=run(seed^{e},e)
            for s in range(e+1):
                assert y[s][e-s]==linear(seed,s,e-s);checks+=1
            delta=[x[s][e-s]^y[s][e-s] for s in range(e+1)]
            if e%2:
                assert delta==[1]*(e+1)
                assert x[e][0]!=e%2
            else:
                tau=next(s for s in range(e) if y[s][e-1-s])
                assert delta==[int(s<=tau) for s in range(e+1)]
                assert x[e][0]==e%2
                immediate+=int(tau==0)
            count+=1
    assert immediate>0
    print('PASS',count,'first flips;',checks,'binomial controls;',
          immediate,'one-sample pulses')
