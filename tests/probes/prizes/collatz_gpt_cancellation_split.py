#!/usr/bin/env python3
"""GC438: split within-increment and across-time cancellation, seven reused cases.
CS1 MUST HOLD: Etotal-|D| = within+temporal and literal-H telescoping.
CS2 BLIND: temporal > within at width7,T48.
CF: abs before telescoping leaves D unchanged; must fail if both signs occur.
Unexpected check: retain empty final populations with positive coin proxy Q.
No wider scan. Widths2..8,T=8*(w-1). OUTCOME: NOT RUN.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_superlevel_allocation import layer


def main():
    cases = []
    controls = 0
    for w in range(2, 9):
        m = w-1
        T = 8*m
        populations = states_at(w, T)
        f = backward(T)
        Etotal = absolute = signed = within = positive = negative = Fraction()
        positive_times = []
        negative_times = []
        for t in range(m,T):
            I = Counter()
            for x,a in populations[t]:
                I[a] += 1 if x % 2 else -1
            d = {a:f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
            S,E,_,_ = layer(I,d)
            literal = sum((f[t+1][a] for _,a in populations[t+1]),Fraction())-sum((f[t][a] for _,a in populations[t]),Fraction())
            assert S == literal
            Etotal += E
            absolute += abs(S)
            signed += S
            within += E-abs(S)
            positive += max(S,0)
            negative += max(-S,0)
            if S > 0:positive_times.append(t)
            if S < 0:negative_times.append(t)
            controls += 1
        Q = sum((f[m][a] for _,a in populations[m]),Fraction())
        D = len(populations[T])-Q
        temporal = absolute-abs(signed)
        assert D == signed
        assert temporal == 2*min(positive,negative)
        assert Etotal-abs(D) == within+temporal
        cases.append(dict(w=w,T=T,Q=str(Q),final=len(populations[T]),D=str(D),
                          component_total=str(Etotal),within=str(within),temporal=str(temporal),
                          positive_times=positive_times,negative_times=negative_times,
                          empty_final_positive_Q=not populations[T] and Q>0))
    seven = next(c for c in cases if c['w']==7)
    print(json.dumps(dict(cases=cases,controls=controls,control_status='PASS',
                          blind_temporal_dominates=Fraction(seven['temporal'])>Fraction(seven['within']),
                          abs_counterfactual_refuted=any(c['positive_times'] and c['negative_times'] for c in cases)),indent=2))


if __name__=='__main__':main()
