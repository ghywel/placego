#!/usr/bin/env python3
"""GC404: one hand-derived exterior condition for GC403's failed shortcut.
Preregistered P1: k=0 => column7<=column8 at time4 removes all28 GC403
failures (0.6). Counterfactual: it removes the first witness but not all.
Derived with time3 column5=0: k=v OR w; k=0 => v=w=0;
next columns7,8=z,z OR u. Controls4096 original rows and scalar/packed
steps. Unexpected scope check counts all remaining cover failures.
OUTCOME: P1 REFUTED:12 of28 removed,16 remain among704 admitted rows.
One-step premise-negative control retained; no long preparation claim.
"""
import itertools
import json
from rule30_gpt_gate_bridge import evolve,pattern


def main():
    # Exhaust every choice for the four local inputs, with column5=0.
    for v,w,z,u in itertools.product((0,1),repeat=4):
        k=v|w; l=v^(w|z); r=w^(z|u)
        assert k or l<=r
    # Without column5=0, (column5,v,w,z,u)=(1,1,0,0,0)
    # produces k,l,r=0,1,0: the condition is not unconditional.
    assert (1^(1|0),1^(0|0),0^(0|0))==(0,1,0)
    count=pos=bad=excluded=0; witness=None
    for a,h,k in itertools.product((0,1),repeat=3):
        if not any(h==(a^v) and k==(v|w) for v,w in itertools.product((0,1),repeat=2)):
            continue
        for tail in itertools.product((0,1),repeat=7):
            row=[0,0,1-a,0,1,h,k]+list(tail);cut=evolve(row,4,4)
            if k==0 and row[7]>row[8]:
                excluded+=bool(cut[6] and not pattern(cut));continue
            count+=1
            if cut[6]:
                pos+=1
                if not pattern(cut):
                    bad+=1
                    if witness is None:witness=row
    controls=0
    for free in range(4096):
        row=[0,free&1,1,1,1,0,0]+[(free>>j)&1 for j in range(1,12)]
        r=evolve(row,0,4)
        assert r[6] or r[7]<=r[8]
        controls+=1
    print(json.dumps({'original_controls':controls,'local_controls':16,
                     'premise_negative_control':'PASS','admitted':count,
                     'antecedent_positive':pos,'failures':bad,
                     'old_failures_excluded':excluded,'first_failure':witness,
                     'P1':'HELD' if bad==0 else 'REFUTED'},indent=2))


if __name__=='__main__':main()
