# Sector test: iota(Y) = (shift - width) mod P on the left side, P = 16 at K = 448, P = 8 at K = 64.
# (1) least depth with period 16; (2) census; (3) invariance on merges and along orbits; (4) survival by sector.
# Strips fork only at wheels >= 53,208, so strips are NOT censused here; every sector below is a shift sector.
import sys,collections,math
def F(y): return (y>>1)^(y|(y<<1))
def mk(K):
    M=(1<<K)-1
    return M,(lambda v:((v<<2)^((v<<1)|v))&M)
def ref_cycle(K):
    M,g=mk(K); v=1
    for _ in range(4*K+400): v=g(v)
    c=[v];u=g(v)
    while u!=v: c.append(u);u=g(u)
    return c
def top_read(y,K):
    b=format(y,'b')
    assert len(b)>=K
    return int(b[:K][::-1],2)
class Sect:
    def __init__(s,K):
        s.K=K; s.M,s.g=mk(K); s.c=ref_cycle(K); s.P=len(s.c); s.idx={v:i for i,v in enumerate(s.c)}
    def shift(s,y):
        t=0; w=y.bit_length()
        while y.bit_length()<s.K: y=F(y);t+=1
        v=top_read(y,s.K)
        while v not in s.idx: v=s.g(v);t+=1
        return (s.idx[v]-t)%s.P
    def iota(s,y): return (s.shift(y)-y.bit_length())%s.P
def main():
    print('period by depth:',[(K,len(ref_cycle(K))) for K in (8,12,32,64,128,256,384,392,396,398,399,400,401,402,404,408,416,448,512)])
    S16=Sect(448); S8=Sect(64)
    print('P at K=448:',S16.P,' P at K=64:',S8.P)
    # census and consistency of the two sectors
    for W in (6,9,12):
        h=collections.Counter(S16.iota(y) for y in range(1<<(W-1),1<<W))
        print('W',W,'rows',1<<(W-1),'sectors',len(h),'min',min(h.values()),'max',max(h.values()))
    bad=0
    for y in range(1,1<<12):
        if S16.iota(y)%8!=S8.iota(y)%8 and S8.P==8: bad+=1
    print('sector mod 8 from K=448 vs K=64: mismatches',bad)
    # orbit invariance
    bad=0
    for y in list(range(1,1<<11)):
        z=y;i=S16.iota(y)
        for a in range(1,6):
            z=F(z)
            if S16.iota(z)!=i: bad+=1
    print('orbit invariance over 5 ticks, rows<2^11: violations',bad)
    # merge invariance
    for W in (10,12,13):
        groups=collections.defaultdict(list)
        for y in range(1<<(W-1),1<<W):
            z=y
            for _ in range(64): z=F(z)
            groups[z].append(y)
        merged=[g for g in groups.values() if len(g)>1]
        viol=sum(1 for g in merged if len({S16.iota(y) for y in g})>1)
        print('W',W,'distinct at tick 64',len(groups),'merged groups',len(merged),'largest',max(map(len,merged)),'groups with two sectors',viol)
    # control: a wrong invariant must fail. shift alone (no width) on rows of different width is not constant on orbits
    y=5; print('control: raw shift changes along an orbit:',[S16.shift(z) for z in (y,F(y),F(F(y)))])
    # survival by sector, W = 32, distinct rows, sector mod 8
    W=32; n=W//2; M=(1<<W)-1
    rows={}
    for f in range(1<<n):
        col=0
        for i in range(n):
            col|=1<<(2*i)
            if (f>>i)&1: col|=1<<(2*i+1)
        # sideways recursion in time-bitset form
        c0=col; y=c0&1
        c1=(c0>>1)^c0
        y|=(c1&1)<<1
        a,b=c0,c1
        for k in range(2,W):
            a,b=b,(b>>1)^(b|a)
            y|=(b&1)<<k
        rows[y]=1
    ys=list(rows)
    print('rows at W=32:',len(ys))
    t=0
    for _ in range(W): ys=[F(y) for y in ys]
    t=W
    ys=list(set(ys))
    sec={}
    S=S8
    for y in ys: sec[y]=S.iota(y)
    print('tick',t,'distinct',len(ys),'sector counts',sorted(collections.Counter(sec.values()).items()))
    while len(ys)>=64:
        # pass = black at the current even tick
        ps=collections.Counter();tot=collections.Counter()
        for y in ys:
            tot[sec[y]]+=1
            if y&1: ps[sec[y]]+=1
        N=sum(tot.values()); p=sum(ps.values())/N
        chi=sum((ps[k]-tot[k]*p)**2/(tot[k]*p*(1-p)) for k in tot if tot[k])
        zmax=max(abs(ps[k]-tot[k]*p)/math.sqrt(tot[k]*p*(1-p)) for k in tot if tot[k])
        print('tick',t,'N',N,'pass',round(p,4),'chi2(7)',round(chi,1),'max|z|',round(zmax,2))
        nxt={}
        for y in ys:
            if y&1:
                z=F(F(y))
                nxt.setdefault(z,sec[y])
        ys=list(nxt); sec=nxt; t+=2
if __name__=="__main__": main()
