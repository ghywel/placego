#!/usr/bin/env python3
"""GC418 preregistered seven-case allocation diagnostic, no asymptotic fit.
Widths2..8, T=8*(w-1); compare G213 range-variation with original absolute
allocation sum. Predict at least one improvement, not universal domination.
Independent literal H checks; retain final-empty ensembles.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward,states_at


def main():
    out=[]
    for w in range(2,9):
        m=w-1;T=8*m;rows=states_at(w,T);f=backward(T)
        old=new=signed=Fraction()
        for t in range(m,T):
            I=Counter()
            for x,a in rows[t]:I[a]+=1 if x%2 else -1
            d={a:f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
            prefix=0;B=[0]
            for a in range(T+1):prefix+=I[a];B.append(prefix)
            tv=sum(abs(d.get(a,0)-d.get(a+1,0)) for a in range(-1,T+1))
            term=sum((I[a]*d[a]/2 for a in I),Fraction())
            literal=sum((f[t+1][a] for _,a in rows[t+1]),Fraction())-sum((f[t][a] for _,a in rows[t]),Fraction())
            assert term==literal
            old+=sum((abs(I[a])*d[a]/2 for a in I),Fraction())
            new+=Fraction(max(B)-min(B),4)*tv;signed+=term
        Q=sum((f[m][a] for _,a in rows[m]),Fraction());C=len(rows[T])
        assert signed==C-Q and abs(signed)<=old and abs(signed)<=new
        out.append(dict(w=w,T=T,C=C,Q=str(Q),old_bound=str(old),new_bound=str(new),new_over_old=float(new/old) if old else None,improved=new<old,empty_discrepancy_retained=(C==0 and signed!=0)))
    print(json.dumps({'cases':out,'prediction_any_improvement':any(r['improved'] for r in out),'literal_identity_and_bounds':'PASS'},indent=2))


if __name__=='__main__':main()
