#!/usr/bin/env python3
"""G25 preregistered TC1/TC2/CF and unexpected TC3 in RULE30-GPT.md.
OUTCOME: TC1=120, TC2=5080 histories/64 families, TC3=168 pass; CF rejected.
Small algebraic audit, not right-half realizability or a support bound.
"""
import itertools
import random
from rule30_gpt_condrey_holes import forced_columns

def columns(tau,sigma,n):
    return tuple(col[0] for col in forced_columns(tau,sigma,n))

def backward(tau,sigma,n):
    # Unknown row at time n cannot affect row0 depths<=n.
    row=[]
    for t in range(n-1,-1,-1):
        x=[tau[t],tau[t+1] ^ (tau[t] | sigma[t])]
        for y in row: x.append(y ^ (x[-1] | x[-2]))
        row=x[1:]
    return tuple(row)

def forward_recover(row,tau,n):
    x=list(row); result=[]
    for t in range(n):
        result.append(tau[t+1] ^ x[0] if tau[t]==0 else None)
        # Independent scalar truth table, cells ordered from wall outward.
        extended=[tau[t]]+x+[0]
        x=[(30 >> (4*extended[j+2]+2*extended[j+1]+extended[j])) & 1 for j in range(len(x)-1)]
    return result

def main():
    rng=random.Random(2506); count=0; families=0; leading=0; masking=0
    for a in range(1,5):
        for b in range(2,6):
            p=a+b
            for n in range(1,5):
                N=n*p; tau=[int(t%p>=a) for t in range(N+1)]; found=set()
                for latches in itertools.product(range(a+1),repeat=n):
                    sigma=[int(t%p>=latches[t//p]) if t%p<a else 0 for t in range(N)]
                    # Width-one extension: black first bit must1 when last white bit1.
                    for k,r in enumerate(latches): sigma[k*p+a]=int(r<a)
                    sigma+=[0]
                    row=columns(tau,sigma,N);assert row==backward(tau,sigma,N)
                    recovered=forward_recover(row,tau,N)
                    assert all(recovered[t]==sigma[t] for t in range(N) if tau[t]==0)
                    found.add(row);count+=1
                assert len(found)==(a+1)**n;families+=1
            N=3*p; tau=[int(t%p>=a) for t in range(N+1)]
            for q in range(N):
                s=[rng.randrange(2) for _ in tau];other=s[:]
                if tau[q]==0:
                    other[q]^=1
                    for t in range(q+1,N):other[t]=rng.randrange(2)
                    x=columns(tau,s,N);y=columns(tau,other,N)
                    assert next(i+1 for i,(u,v) in enumerate(zip(x,y)) if u!=v)==q+1
                    leading+=1
                else:
                    other[q]^=1
                    assert forced_columns(tau,s,N)==forced_columns(tau,other,N)
                    masking+=1
    print('TC1 PASS first-difference cases',leading)
    print('TC2 PASS histories',count,'families',families,'independent backward and forward inverses')
    print('TC3 PASS whole-triangle black-bit masking cases',masking)
    print('CF REJECTED: every complete-period prefix is distinct')

if __name__=='__main__':main()
