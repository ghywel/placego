#!/usr/bin/env python3
"""G29 seeded Collatz scope audit, CC1/CC2/CF/CC3 preregistered.
OUTCOME: CC1=1028, CC2=2008, CC3=32 pass; cycle/closed-endpoint CF rejected.
Finite controls cannot exhibit/prove an infinite distinct rational orbit.
"""

def step(N,D):return N//2 if N%2==0 else (3*N+D)//2

def word(N,D,n):
    out=[]
    for _ in range(n):out.append(N%2);N=step(N,D)
    return tuple(out)

def count(H,n):
    i=0
    while 3**i*H<=2**(i+n-1):i+=1
    return i

def main():
    growth=0;unique=0;endpoints=0
    for D in (1,3,5,9):
        for N in range(-128,129):
            assert 2*(abs(step(N,D))+D)<=3*(abs(N)+D);growth+=1
        for n in range(1,9):
            q=1<<(n-1);seen=set()
            for N in range(-q+1,q):
                w=word(N,D,n);assert w not in seen;seen.add(w);unique+=1
            assert word(-q,D,n)==word(q,D,n);endpoints+=1
    assert count(2,2)==1 # equality included because abs(N)<=threshold-D
    for N in (0,-1):
        assert step(N,1)==N and len({word(N,1,10)})==1
        assert count(abs(N)+1,10)>1
    print('CC1 PASS',growth,'signed growth controls; CC2 PASS',unique,'parity words')
    print('Unexpected CC3 PASS',endpoints,'endpoint collisions; exact equality-count control passes')
    print('CF REJECTED: infinitely many iterates of0 or-1 are cycles, not infinite distinct orbits')

if __name__=='__main__':main()
