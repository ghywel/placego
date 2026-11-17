#!/usr/bin/env python3
"""GC416 preregistration: Abel prefix imbalance identity and range bound.
Widths2..5, T=m..9; retained boundaries and empty cases. Independent literal
H increments. Unexpected zero-total synthetic guard still has nonzero weight.
No shape theorem or asymptotic count estimate.
"""
from collections import Counter
from fractions import Fraction
from collatz_gpt_backward_weights import backward,states_at
import json


def abel(I,delta):
    top=max(set(I)|set(delta)|{0})
    B={-1:0};s=0
    for a in range(top+1):s+=I.get(a,0);B[a]=s
    direct=sum((I.get(a,0)*delta.get(a,0)/2 for a in range(top+1)),Fraction())
    gradients={a:delta.get(a,0)-delta.get(a+1,0) for a in range(-1,top+1)}
    assert sum(gradients.values())==0
    transformed=sum((B[a]*g/2 for a,g in gradients.items()),Fraction())
    variation=sum(abs(g) for g in gradients.values())
    oscillation=max(B.values())-min(B.values())
    assert direct==transformed and abs(direct)<=Fraction(oscillation,4)*variation
    return direct


def main():
    cases=empty=0
    for w in range(2,6):
        m=w-1;rows=states_at(w,9)
        for T in range(m,10):
            f=backward(T)
            for t in range(m,T):
                I=Counter()
                for x,a in rows[t]:I[a]+=1 if x%2 else -1
                delta={a:f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
                value=abel(I,delta)
                literal=sum((f[t+1][a] for x,a in rows[t+1]),Fraction())-sum((f[t][a] for x,a in rows[t]),Fraction())
                assert value==literal
                cases+=1;empty+=not rows[t]
    # Total I is zero, but its two classes see different demand weights.
    guard=abel({0:1,1:-1},{0:Fraction(3,4),1:Fraction(1,4)})
    assert guard==Fraction(1,4)
    # Lower support jump is necessary: a single spike has variation two.
    assert abel({0:1},{0:Fraction(1)})==Fraction(1,2)
    print(json.dumps(dict(increments=cases,empty=empty,zero_total_guard=str(guard),exact_identity_bound_and_literal_H='PASS')))


if __name__=='__main__':main()
