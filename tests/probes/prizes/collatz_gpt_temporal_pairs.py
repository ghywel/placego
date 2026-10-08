#!/usr/bin/env python3
"""GC439: one width7,T48 canonical pair partition starting m6.
TP1 MUST HOLD: pair sums equal individual killed-potential changes;
G80 curvature only for admitted interior mixed paths; B<=sum abs(S).
TP2 BLIND: canonical adjacent pairs capture >half GC438 temporal budget.
CF: aggregate pair gain requires interior mixed paths; inspect, no verdict
unless a gained block has no such paths. Unexpected killed-inside blocks.
No larger scan or offset optimization.
OUTCOME 2026-10-08: TP1 PASS21 blocks,34 interior mixed controls,
3 boundary mixed paths,7 killed paths. TP2 REFUTED: capture14.48 percent.
Mixed-necessity CF REFUTED by positive-gain block t28 with no mixed paths.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_boundary_loss import threshold


def main():
    w,T,m=7,48,6
    populations=states_at(w,T)
    f=backward(T)
    H=[sum((f[t][a] for _,a in populations[t]),Fraction()) for t in range(T+1)]
    S={t:H[t+1]-H[t] for t in range(m,T)}
    absolute=sum((abs(s) for s in S.values()),Fraction())
    D=H[T]-H[m]
    temporal=absolute-abs(D)
    B=Fraction()
    rows=[]
    for t in range(m,T,2):
        change=parent_absolute=Fraction()
        counts=Counter()
        for x,a in populations[t]:
            y,b=x,a
            bits=[]
            alive=True
            for k in (t,t+1):
                if not alive:break
                bit=y%2
                bits.append(bit)
                b+=bit
                y=(3*y+1)//2 if bit else y//2
                alive=3**b>=2**(k+1)
            delta=(f[t+2][b] if alive else Fraction())-f[t][a]
            change+=delta
            parent_absolute+=abs(delta)
            if not alive:counts['killed']+=1
            if len(bits)==2 and sum(bits)==1:
                if a>=threshold(t+1):
                    curvature=(2*f[t+2][a+1]-f[t+2][a]-f[t+2][a+2])/4
                    assert alive and delta==curvature
                    counts['interior_mixed']+=1
                else:counts['boundary_mixed']+=1
        pair=S[t]+S[t+1]
        assert pair==change and abs(pair)<=parent_absolute
        gain=abs(S[t])+abs(S[t+1])-abs(pair)
        assert gain>=0
        B+=abs(pair)
        rows.append(dict(t=t,S0=str(S[t]),S1=str(S[t+1]),gain=str(gain),
                         pair=str(pair),parent_absolute=str(parent_absolute),counts=dict(counts)))
    assert B<=absolute and abs(D)<=B
    captured=absolute-B
    assert temporal==captured+B-abs(D)
    print(json.dumps(dict(w=w,T=T,m=m,blocks=rows,controls='PASS',
                          absolute=str(absolute),B=str(B),D=str(D),temporal=str(temporal),
                          captured=str(captured),capture_fraction=str(captured/temporal),
                          blind_over_half=captured>temporal/2,
                          mixed_necessity_refuted=any(Fraction(r['gain'])>0 and not r['counts'].get('interior_mixed') for r in rows)),indent=2))


if __name__=='__main__':main()
