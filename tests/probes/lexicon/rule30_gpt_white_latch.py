#!/usr/bin/env python3
"""G14: exact width-one latch counts for wall0^(p-1)1, p>=2.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_white_latch.py
RUN-ON: GPT Intel CPU, one process; standard library, small exhaustive counts.
PREDICTIONS before first run, 2026-10-06:
 WL0 control: sigma<=sigma_next at wall0, and not(sigma=sigma_next=1)
     at wall1, are exactly existence of rho in the center equation.
 WL1 theorem control: all sigma words for n periods plus endpoint
     counted by sum of entries of [[p,1],[1,0]]^n; p2..8, n<=5,
     capped at15 time transitions for brute force.
 WL2 theorem control: distinct visible words (omit wall1 positions,
     retain next-period first bit) counted by [[p-1,1],[1,0]]^n.
 WL3 control: p2 visible count is F(n+3), existing section8.2 result;
     growth constant golden ratio. Full-column rate is1+sqrt(2).
 WL4 unexpected: constant0 wall gives only N+2 sigma words of
     lengthN+1, not exponential; constant1 has no visible bits.
 CF must fail: full sigma traces and distinct visible words have the
     same count; one period p2 has4 full traces but3 visible words.
 REFUTED-BY: any count/scalar control fails or CF not rejected.
 These are width-one relaxations with freely chosen rho at each time;
 no assumption that rho is an actual further Rule30 column is made.
"""
import itertools,math


def allowed(tau,a,b):
    return a<=b if tau==0 else not(a==b==1)


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def count(m,n):
    a=[[m,1],[1,0]];b=[[1,0],[0,1]]
    for _ in range(n):b=matmul(b,a)
    return sum(map(sum,b))


def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def main():
    for tau,a,b in itertools.product([0,1],repeat=3):
        actual=any(b==(tau^(a|rho)) for rho in [0,1])
        assert actual==allowed(tau,a,b)
    checks=0
    for p in range(2,9):
        for n in range(1,min(5,15//p)+1):
            size=p*n;tau=[int(t%p==p-1) for t in range(size+1)]
            full=[];visible=set()
            for word in itertools.product([0,1],repeat=size+1):
                if all(allowed(tau[t],word[t],word[t+1]) for t in range(size)):
                    full.append(word)
                    visible.add(tuple(word[t] for t in range(size+1) if not tau[t]))
            assert len(full)==count(p,n),(p,n,len(full),count(p,n))
            assert len(visible)==count(p-1,n),(p,n,len(visible),count(p-1,n))
            if p==2:assert len(visible)==fib(n+3)
            checks+=1
    assert count(2,1)==4 and count(1,1)==3
    for size in range(1,13):
        zeros=sum(all(a<=b for a,b in zip(w,w[1:]))
                  for w in itertools.product([0,1],repeat=size+1))
        assert zeros==size+2
    assert ((1+math.sqrt(5))/2)**2-(1+math.sqrt(5))/2==1.0
    print('ALL CONTROLS PASS: %d exhaustive period/length cases; constants checked; CF4!=3'%checks,flush=True)
    for p in [2,3,4,8,16,64]:
        whole=(p+math.sqrt(p*p+4))/2
        visible=(p-1+math.sqrt((p-1)**2+4))/2
        print('p=%d full_bits/step=%.9f visible_bits/step=%.9f independent_bound=%.9f'%(p,math.log2(whole)/p,math.log2(visible)/p,math.log2(p+1)/p),flush=True)


if __name__=='__main__':main()
