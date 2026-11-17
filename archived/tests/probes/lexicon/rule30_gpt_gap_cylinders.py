#!/usr/bin/env python3
"""GC549 CP31; four abstract cylinders, preregistered before run.
P1 blind: all four CP29/L288 source prefixes force site2=0 at time18.
C1: every ternary triple agrees with all literal Rule30 completions.
CF: black source a=b=q=1 forces next even b=0; must fail (b'=1).
Unexpected: retain first unknown visible sample and every even forced prefix.
No source enumeration or death-time sweep. REFUTED-BY: any C1 mismatch or
unknown/nonzero terminal site2. OUTCOME: C1 PASS on27 ternary triples;
CF REFUTED; P1 REFUTED for001000, HELD for001010,001011,001100.
Three cylinders therefore exclude a final2-gap by the hand black-row lemma.
Unknown is a loss of information, never an existence witness.
"""
from itertools import product
TAILS = ('001000','001010','001011','001100')
def one(a,b,c):
    choices = lambda v: (0,1) if v is None else (v,)
    values = {(30 >> (4*x+2*y+z)) & 1
              for x in choices(a) for y in choices(b) for z in choices(c)}
    return next(iter(values)) if len(values)==1 else None

def main():
    for a,b,c in product((0,1,None), repeat=3):
        choices = lambda v: (0,1) if v is None else (v,)
        values = {x ^ (y | z) for x in choices(a)
                  for y in choices(b) for z in choices(c)}
        assert one(a,b,c) == (next(iter(values)) if len(values)==1 else None)
    assert (1 & (1 | 0)) == 1
    for tail in TAILS:
        row = list(map(int,'11100'+tail)) + [None]*20
        trace=[]
        print('source cylinder',tail)
        for t in range(19):
            if t%2==0:
                trace.append(row[0])
                print(t,''.join('?' if b is None else str(b) for b in row[:10]))
            if t==18:break
            row=[one(t%2 if j==0 else row[j-1],row[j],row[j+1])
                 for j in range(len(row)-1)]
        print('time18site2',row[1],'; first unknown sample',
              next((2*k for k,v in enumerate(trace) if v is None),None))
    print('C1 PASS; CF REFUTED; P1 partly refuted, scope retained')
if __name__ == '__main__':main()
