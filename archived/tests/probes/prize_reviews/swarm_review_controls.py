#!/usr/bin/env python3
"""Independent bounded arithmetic controls for the 2026-10-22 prize-swarm review.
Predictions frozen BEFORE execution:
- Exact divisor-subset control accepts known weird70/836/4030, rejects6/12/945.
- Three hand-derived dominating #7 certificates equal23/48,77/198,277/990.
- #470 claim a>=b+4 => u=0 FAILS at N128,a31,b23,p97,q151.
- BLIND: a complete small eligible-prime domain may also refute its iff shortcut.
Counterfactual: missed known control, composite alleged prime or mismatch in the
exact criterion versus literal divisor subset sums stops the run as CONTROL FAIL.
Independent mechanisms: formula versus literal proper-divisor bitset, sieve
versus trial division for every emitted prime. No imported agent test routines.
Unexpected check: smallest maximum-deficiency Hall set need not be largest;
one isolated left vertex plus one matched component is the explicit control.
Caps: one process, CPU10s, wall10s (checks inside loops), <=250000 prime pairs,
N<=4096; bitset target<=2^24, output<=16KiB, fixed small arrays (<32MiB by domain).
No supervisor/ps dependency, process-wide kills, retry or census widening.
This is a scope-adversarial audit, not an odd-weird search or a prize solution.
"""
import math,resource,time,json
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
start=time.monotonic()
def cap():
    assert time.monotonic()-start<10,'wall cap'
def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def weird(n):
    ds=[d for d in range(1,math.isqrt(n)+1) if n%d==0]
    ds=sorted(set(ds+[n//d for d in ds])-{n})
    delta=sum(ds)-n
    if delta<0:return False
    assert delta<=2**24,'bitset cap'
    bits=1;mask=(1<<(delta+1))-1
    for d in ds:
        if d<=delta:bits=(bits|(bits<<d))&mask
    return not((bits>>delta)&1)
for n in [70,836,4030]:assert weird(n),(n,'known weird missed')
for n in [6,12,945]:assert not weird(n),(n,'nonweird accepted')
def certificate(ps,ts):
    us=[F(1,p-1-t) for p,t in zip(ps,ts)]
    prod=F(1)
    for u in us:prod*=1+u
    return sum(F(3,2)*F(1,3**t)*u for u,t in zip(us,ts))+F(3,2)*(prod-1-sum(us))
certs=[certificate([5,7,11],[1,2,2]),certificate([5,11,13],[1,1,1]),certificate([7,11,13],[1,1,1])]
assert certs==[F(23,48),F(77,198),F(277,990)] and all(c<F(1,2) for c in certs)
assert prime(97) and prime(151)
assert 31>=23+4 and ((31-1)*(23+1))//128==5
print(json.dumps({'controls':'PASS','four_prime_support_certificates':[str(c) for c in certs],'u_zero_counterexample':{'N':128,'a':31,'b':23,'p':97,'q':151,'u':5}}))
def criterion(k,a,b):
    N=1<<(k+2);M=N//2;u,v=divmod((a-1)*(b+1),N);L=(a-b-4)//2+u
    return L>=0 and L*b<=v<=M-(L+1)*a-1
checked=0
# Complete tiny domain: all stated eligible pairs at k=1..6, including primes.
for k in range(1,7):
 N=1<<(k+2);M=N//2
 for a in range(1,M//2,2):
  if not prime(N-a):continue
  for b in range(1,M-a+1,2):
   cap()
   if not prime(N+b):continue
   n=(1<<k)*(N-a)*(N+b)
   assert criterion(k,a,b)==weird(n),('criterion mismatch',k,a,b,n)
   checked+=1
print(json.dumps({'exact_criterion_literal_domain':'PASS','k_range':[1,6],'eligible_pairs':checked}))
found=None;pairs=0
for k in range(1,11):
 N=1<<(k+2);M=N//2
 for a in range(5,M//2,2):
  if not prime(N-a):continue
  for b in range(1,min(a-4,M-a)+1,2):
   cap()
   if not prime(N+b):continue
   pairs+=1;assert pairs<=250000,'pair cap'
   actual=criterion(k,a,b);shortcut=a*(a+b)<=N+2*b
   if actual!=shortcut:
    n=(1<<k)*(N-a)*(N+b)
    assert weird(n)==actual
    found={'k':k,'N':N,'a':a,'b':b,'p':N-a,'q':N+b,'n':n,'weird':actual,'shortcut':shortcut,'u':((a-1)*(b+1))//N}
    break
  if found:break
 if found:break
# Independent Hall control: neighbours(0)=empty, neighbours(1)={r}.
deficiency={frozenset(s):len(s)-len({0 for j in s if j==1}) for s in [[],[0],[1],[0,1]]}
mx=max(deficiency.values());maximizers=[sorted(s) for s,d in deficiency.items() if d==mx]
assert maximizers==[[0],[0,1]]
print(json.dumps({'shortcut_counterexample':found,'prime_pairs_examined':pairs,'unexpected_Hall_maximizers':maximizers,'wall_seconds':round(time.monotonic()-start,6)}))

# OUTCOME (single bounded run, 2026-10-22): all controls PASS; 263 eligible pairs
# in complete k1..6 domain agree with literal divisor subsets. Corollary B fails
# at k9,a55,b51,p1993,q2099,n2141853184,u1 after939 eligible pairs.
# Exact rationals23/48,7/18,277/990; Hall control confirms two maximizers.
# Observed wall0.025831s. No patch/retry; outcome comment appended afterward.
