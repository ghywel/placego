#!/usr/bin/env python3
"""GC445: fixed width7,T48,t28 and t29 only, no scan.
MC1 MUST HOLD: count/state signed identities and literal H; count matches >=
state matches and A_count<=A_state. MC2 BLIND: A_count<E in at least one.
CF: count grouping universally <=G74; must fail on same-class synthetic pool.
Unexpected guard: failed even child retained, synthetic multiplicity preserved.
OUTCOME: NOT RUN.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_coalescence_weights import grouped
from collatz_gpt_superlevel_allocation import layer


def bins(parents,d,state=False):
    O,E=Counter(),Counter()
    for x,a in parents:
        bit=x%2;b=a+bit;y=(3*x+1)//2 if bit else x//2
        key=(y,b) if state else b
        (O if bit else E)[key]+=1
    signed=bound=curvature=residual=Fraction();matches=0
    for key in O.keys()|E.keys():
        b=key[1] if state else key
        o,e=O[key],E[key];M=min(o,e)
        u,v=d.get(b-1,0),d.get(b,0)
        curvature+=M*(u-v)/2
        residual+=((o-M)*u-(e-M)*v)/2
        signed+=(o*u-e*v)/2
        bound+=(M*abs(u-v)+(o-M)*u+(e-M)*v)/2
        matches+=M
    assert signed==curvature+residual
    return signed,bound,matches,curvature,residual


def main():
    rows=states_at(7,48);f=backward(48);cases=[]
    for t in (28,29):
        d={a:f[t+1][a+1]-f[t+1][a] for a in range(49)}
        c=bins(rows[t],d);s=bins(rows[t],d,True)
        I=Counter()
        for x,a in rows[t]:I[a]+=1 if x%2 else -1
        direct,E,old,median=layer(I,d)
        literal=sum((f[t+1][a] for _,a in rows[t+1]),Fraction())-sum((f[t][a] for _,a in rows[t]),Fraction())
        assert c[0]==s[0]==literal==direct==grouped(rows[t],d,t)[0]
        assert c[2]>=s[2] and c[1]<=s[1]
        cases.append(dict(t=t,S=str(c[0]),count_bound=str(c[1]),state_bound=str(s[1]),
                          count_matches=c[2],state_matches=s[2],curvature=str(c[3]),residual=str(c[4]),
                          layer=str(E),old=str(old),median=str(median),improves_layer=c[1]<E))
    synthetic=[(3,2),(4,2)];d={2:Fraction(1)}
    assert bins(synthetic,d)==(0,1,0,0,0)
    assert layer({2:0},d)[1:3]==(0,0)
    assert bins(synthetic*2,d)==(0,2,0,0,0)
    assert bins([(4,2)],d)[0]==Fraction(-1,2)
    print(json.dumps(dict(cases=cases,controls='PASS',blind_any_layer_gain=any(c['improves_layer'] for c in cases),
                          class_domination_counterfactual='REFUTED',multiplicity_and_lost_child='PASS'),indent=2))


if __name__=='__main__':main()
