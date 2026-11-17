#!/usr/bin/env python3
"""One direct zero-tail guard audit using GC708's four two-gap prefixes.
RUN-ON: cpu; feed stored GC708 JSON on standard input. No new words or horizons.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_mixed_left_cost.py |
         python3 tests/probes/lexicon/rule30_gpt_zero_tail_guard.py
Predictions before execution (2026-10-09): ZG-P1: zero tails after depth B+6 select
letters L,L,L,S for prefixes SS,SL,LS,LL respectively; the next black-time guards
pass,fail,fail,pass. Counterfactual a zero-selected letter automatically passes.
Controls: independent Boolean/decimal left updates agree, all earlier black-time
checks pass, flipping depth B+8 flips exactly the next guard value. Unexpected:
flipping deeper depth B+9 cannot rescue that guard. No supplied right neighbor
is used; the wall is clamped only to test necessary left compatibility.
OUTCOME (2026-10-09): ZG-P1 HELD; all controls PASS. SS/LL pass this one
guard; SL/LS fail at black time 23. No later survival conclusion.
"""
import json, sys

def evolve(bits, horizon, literal):
    a = [0] + bits + [0] * (horizon + 4)
    out = []
    for t in range(horizon + 1):
        a[0] = t % 2
        out.append(a[1])
        b = [0] * len(a)
        for j in range(1, len(a)-1):
            l,c,r = a[j+1],a[j],a[j-1]
            b[j] = ((30 >> (4*l+2*c+r)) & 1) if literal else l ^ (c | r)
        a = b
    return out

def main():
    rows = {r['word']: r['left'] for r in json.load(sys.stdin)['rows']}
    out=[]
    for p in ('SS','SL','LS','LL'):
        B=sum(6 if c=='S' else 10 for c in p)
        D=B+6; H=B+7
        bits=list(map(int, rows[p+'SS'][:D]))+[0,0,0]
        a=evolve(bits,H,False)
        assert a==evolve(bits,H,True)
        assert all(a[t]==1 for t in range(1,B+6,2))
        full=evolve(list(map(int,rows[p+'SS'])),H,True)
        assert all(full[t]==1 for t in range(1,H+1,2))
        assert a[:B+6]==full[:B+6]
        partner=bits.copy();partner[B+7]^=1
        ap=evolve(partner,H,True)
        assert ap[:H]==a[:H] and ap[H]==1-a[H]
        deeper=bits.copy();deeper[B+8]^=1
        assert evolve(deeper,H,True)==a
        out.append({'prefix':p,'D':D,'selected':'S' if a[B+6]==0 else 'L',
                    'black_time':H,'guard_pass':a[H]==1})
    held=[(x['selected'],x['guard_pass']) for x in out]==[
        ('L',True),('L',False),('L',False),('S',True)]
    print(json.dumps({'controls':'PASS','ZG-P1':'HELD' if held else 'REFUTED','rows':out},indent=2))
if __name__=='__main__':main()
