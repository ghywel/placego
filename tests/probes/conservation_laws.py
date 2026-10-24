#!/usr/bin/env python3
"""Local conservation laws of an elementary CA on k-cell windows (Cloud, CL611, 2026-10-24).

Usage: python3 tests/probes/conservation_laws.py RULE POWER KMAX
Prints, for k = 1..KMAX, the dimension of {g : sum of g over the k-windows of x equals the sum over
the k-windows of F^POWER x for every cyclic x} against the trivial dimension 2^(k-1) (constants plus
telescoping differences). Nontrivial = 0 means no local conservation law at window k. The cyclic
words tested are all words of length <= min(k+5, 14) plus 400 random longer ones; rank over GF(p).
Controls: rule 184 shows one nontrivial law at every k (particle number); rule 170 (the shift)
conserves every density. Result recorded in CHAT-LEDGER.md CL611: rule 30, F and F^2, k <= 8: none.
"""
# space {g : sum of g over windows of x == sum over windows of F x, for every cyclic x} versus the
import sys, itertools, random
P = 2**61-1
def rule_fn(r):
    return lambda l,c,rr: (r >> (l*4+c*2+rr)) & 1
def step(x, f):
    n=len(x); return [f(x[(i-1)%n], x[i], x[(i+1)%n]) for i in range(n)]
def win_counts(x, k):
    n=len(x); v=[0]*(1<<k)
    for i in range(n):
        idx=0
        for j in range(k): idx=(idx<<1)|x[(i+j)%n]
        v[idx]+=1
    return v
def rank_modp(rows):
    rows=[r[:] for r in rows]; rank=0; ncol=len(rows[0]) if rows else 0
    piv_rows=[]
    for col in range(ncol):
        pr=None
        for i in range(rank,len(rows)):
            if rows[i][col]%P: pr=i;break
        if pr is None: continue
        rows[rank],rows[pr]=rows[pr],rows[rank]
        inv=pow(rows[rank][col],P-2,P)
        rows[rank]=[(a*inv)%P for a in rows[rank]]
        for i in range(len(rows)):
            if i!=rank and rows[i][col]%P:
                m=rows[i][col]; rows[i]=[(a-m*b)%P for a,b in zip(rows[i],rows[rank])]
        rank+=1
    return rank
def dim_conserved(r, k, power, Nmax, nrand=400, seed=1):
    f=rule_fn(r); rows=[]
    def add(x):
        y=x
        for _ in range(power): y=step(y,f)
        a=win_counts(x,k); b=win_counts(y,k)
        rows.append([(a[i]-b[i])%P for i in range(1<<k)])
    for n in range(1,Nmax+1):
        for bits in itertools.product((0,1),repeat=n): add(list(bits))
    rnd=random.Random(seed)
    for _ in range(nrand):
        n=rnd.randint(Nmax+1, Nmax+12); add([rnd.randint(0,1) for _ in range(n)])
    return (1<<k)-rank_modp(rows)
if __name__=="__main__":
    r=int(sys.argv[1]); power=int(sys.argv[2]); kmax=int(sys.argv[3])
    for k in range(1,kmax+1):
        Nmax=min(k+5, 14)
        d=dim_conserved(r,k,power,Nmax)
        print(f"rule {r} F^{power} k={k}: dim conserved = {d}, trivial = {2**(k-1)}, nontrivial = {d-2**(k-1)}", flush=True)
