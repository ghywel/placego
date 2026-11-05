#!/usr/bin/env python3
"""decide.py (Local, L1532): the one free choice. Check on the letter words alone: after B the next letter is A for every lower state; after A it is A exactly when the entering state is (0,0).
And the smallest words of cells below A that force each answer."""
from reachlib import *
A=[0,0,1,1,1,1,0,0,0,1,1]; B=[0,1,0,1,1,1,0,0,0,1,1]
def nextletter(word,s):
    x=sum(b<<i for i,b in enumerate(word)); n=len(word)
    y=step(x,n,s)
    return let(y,n+3)
for name,w in (('A',A),('B',B)):
    print(name,{s:nextletter(w,s) for s in STATES})
# words below A: which short lower words force the entering state to be (0,0)?
def enter_states(word):
    """the set of states after reading word (low to high) from all four"""
    S=set(STATES)
    for c in word:
        S={(c^(p1|p2),p1) for p1,p2 in S}
    return S
import itertools
print('shortest lower words forcing the choice below A (read low to high, ending at offset 11):')
for L in range(1,11):
    fa=[];fb=[]
    for bits in itertools.product((0,1),repeat=L):
        S=enter_states(bits)
        if S=={(0,0)}: fa.append(bits)
        if (0,0) not in S: fb.append(bits)
    def st(b): return ''.join('#' if c else '.' for c in b)
    print(L,'force A',len(fa),[st(b) for b in fa[:6]],'| force B',len(fb),[st(b) for b in fb[:6]])
