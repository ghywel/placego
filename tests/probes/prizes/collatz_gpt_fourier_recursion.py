"""G38 exact histogram and independent Fourier controls; no decay claim."""
from collections import Counter, defaultdict
from cmath import exp
from math import pi


def brute(m):
    out=[]
    for r in range(1<<m):
        q,a=r,0;ok=True
        for t in range(1,m+1):
            b=q%2;a+=b;q=(3*q+1)//2 if b else q//2
            if 3**a<=2**t:
                ok=False;break
        if ok:out.append((a,q,r))
    return out


def child(a,q,b):
    epsilon=(b-q)%2
    return (3**b*(q+epsilon*3**a)+b)//2


def root(n,m):return exp(2j*pi*(n%m)/m)


def main():
    rows=[brute(m) for m in range(9)]
    histchecks=fourierchecks=0;worst=0.0
    for base in (2,4,8,16):
        modulus=base<<8;hist=Counter({(0,0):1})
        for m in range(9):
            assert hist==Counter((a,q%modulus) for a,q,_ in rows[m])
            assert sum(hist.values())==len(rows[m])
            histchecks+=1
            if m==8:break
            nxt=Counter()
            for (a,q),count in hist.items():
                for b in (0,1):
                    if 3**(a+b)>2**(m+1):
                        nxt[(a+b,child(a,q,b)%(modulus//2))]+=count
            hist=nxt;modulus//=2
    ternary=0
    for m in range(8):
        for a,q,r in rows[m]:
            for b in (0,1):
                if 3**(a+b)<=2**(m+1):continue
                modulus=3**(a+b);x=child(a,q,b)
                assert 0<=x<modulus
                assert x==((3**b*q+b)*pow(2,-1,modulus))%modulus
                ternary+=1
    alias=None
    for m in range(8):
        by_a=defaultdict(list)
        for a,q,r in rows[m]:by_a[a].append((q,r))
        for modulus in (2,4,8,16):
            for a,values in by_a.items():
                for b in (0,1):
                    if 3**(a+b)<=2**(m+1):continue
                    for h in range(modulus):
                        direct=sum(root(h*child(a,q,b),modulus) for q,_ in values)
                        theta=root(h*3**(a+b),2*modulus)
                        f0=sum(root(h*3**b*q,2*modulus) for q,_ in values)
                        f1=sum(root((h*3**b+modulus)*q,2*modulus) for q,_ in values)
                        formula=root(h*b,2*modulus)*((1+theta)*f0/2+(-1)**b*(1-theta)*f1/2)
                        error=abs(direct-formula);worst=max(worst,error)
                        assert error<1e-9;fourierchecks+=1
                    for q,r in values:
                        for q2,r2 in values:
                            if q%modulus==q2%modulus and child(a,q,b)%modulus!=child(a,q2,b)%modulus:
                                alias=alias or (m,a,modulus,b,r,q,r2,q2,child(a,q,b)%modulus,child(a,q2,b)%modulus)
    assert alias
    theta=1j
    assert abs((1+theta)/2)+abs((1-theta)/2)>1
    print(f'FR1 PASS: {histchecks} exact histogram comparisons; FR2 PASS: {fourierchecks} Fourier identities, max error{worst:.2g}')
    print('Unexpected FR3 alias (m,a,M,b,r,q,r2,q2,children):',alias)
    print(f'FR4 PASS: {ternary} exact ternary transitions')
    print('CF REJECTED: modulus M loses a carry bit; triangle coefficient norm can exceed1')


if __name__=='__main__':main()
