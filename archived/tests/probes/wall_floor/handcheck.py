#!/usr/bin/env python3
"""handcheck.py (Local, L1538): checks H1 and H4. H1: enumerate settled pasts by the forward rule. H4: the columns above the floors of the two floored locks against the hand formulas."""
import json,itertools
from reachlib import *
# H1: words of 11+5n cells by offset; forward image y'(k) = y(k+3) ^ (y(k+4) | y(k+5))
A=[1,1,0,0,0,1,1,1,1,0,0]; B=[1,1,0,0,0,1,1,1,0,1,0]
def isletter(y): return y[:11]==A or y[:11]==B
def fwd(y): return [y[k+3]^(y[k+4]|y[k+5]) for k in range(len(y)-5)]
def settled(y):
    while True:
        if not isletter(y): return False
        if len(y)<16: return True
        y=fwd(y)
S=[A,B]
for n in range(0,5):
    print('n',n,'width',11+5*n,'count',len(S),'formula',2*4**n)
    # brute extension: add five cells, keep those whose past stays settled
    N=[]
    for y in S:
        # y is y_1's word; build y_0 by trying all 16 + 5... direct: extend y_0 candidates from letters
        pass
    if n==4: break
    # direct enumeration by extending deeper: all words of S_(n+1) extend S_n as words (top cells)
    N=[]
    for y in S:
        for e in itertools.product((0,1),repeat=5):
            z=y+list(e)
            if settled(z): N.append(z)
    S=N
# H4 on the two floored locks
def col(ws,k): return [1 if w[len(w)-1-k]=='#' else 0 for w in ws]
L45=[''.join('#' if b else '.' for b in v) for v in json.load(open('lock45.json'))]
s136=json.load(open('lock136.json'))
for name,ph,c in (('AB',[L45[0],L45[1]],41),('AAB',[s136[5],s136[3],s136[1]],132)):
    P=len(ph)
    C=lambda n:col(ph,c-n)
    v=C(4)
    sh=lambda i:[v[(t+i)%P] for t in range(P)]
    neg=lambda a:[1-x for x in a]
    tests={1:neg(sh(-1)),2:[1]*P,3:[0]*P,5:[0]*P,6:[1]*P,7:neg(sh(1)),8:sh(1),9:neg(sh(1)),10:sh(2),11:neg(sh(2)),12:sh(2),13:neg(sh(3)),14:[a|b for a,b in zip(sh(2),sh(3))],15:neg(sh(3)),16:sh(4),17:neg(sh(3)),18:sh(4),19:neg(sh(5)),20:[a&b for a,b in zip(sh(4),sh(5))],21:[1-(a|b) for a,b in zip(sh(4),sh(5))]}
    bad=[n for n,e in tests.items() if C(n)!=e]
    print(name,'floor offset',c,'v',v,'formulas that fail:',bad, 'letters at offset 9',col(ph,9))
