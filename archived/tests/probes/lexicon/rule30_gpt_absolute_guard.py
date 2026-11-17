#!/usr/bin/env python3
"""Validate the hand two-integrator absolute guard on GC716's same four prefixes.
Predicted before first execution, 2026-10-09: H0 equals direct zero-tail guard;
flipping the odd pivot changes that guard by common-white parity P.
Independent decimal direct evolution is the control. Unexpected: collect the
second ahead diagonal only through d-2; at d-1 it would cross the wall.
Feed stored GC708 JSON on stdin. No new words, depth boxes or horizons.
OUTCOME: formula held on all four stored prefixes; decimal controls PASS.
H0/P are 1/1, 0/0, 0/0, 1/1 for SS, SL, LS, LL.
"""
import json, sys
from rule30_gpt_zero_tail_guard import evolve

def integrators(bits,d):
    a=[0]+bits+[0]*(d+4)
    F=H=P=0
    for t in range(d):
        a[0]=t%2
        r=a[d-1-t]
        H ^= F | r
        P ^= 1-r
        if t<d-1:
            s=a[d-2-t]
            F ^= r | s
        a=[0]+[a[j+1]^(a[j]|a[j-1]) for j in range(1,len(a)-1)]+[0]
    return H,P

def main():
    rows={x['word']:x['left'] for x in json.load(sys.stdin)['rows']}
    out=[]
    for p in ('SS','SL','LS','LL'):
        B=sum(6 if c=='S' else 10 for c in p);d=B+7
        bits=list(map(int,rows[p+'SS'][:d-1]))+[0,0]
        H,P=integrators(bits,d)
        direct=evolve(bits,d,True)[d]
        assert H==direct
        flip=bits.copy();flip[d-1]=1
        assert evolve(flip,d,True)[d]==H^P
        out.append({'prefix':p,'d':d,'H0':H,'P':P})
    print(json.dumps({'controls':'PASS','predicted_formula':'HELD','rows':out},indent=2))
if __name__=='__main__':main()
