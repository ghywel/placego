# Left sectors of rows under F (white wall). v = the row read from its top cell; v -> 4v xor (2v|v) mod 2^K is one tick.
# sector(Y) = (strip, (shift - width) mod 16). Claim: constant on merge classes. Exact integer arithmetic.
import sys,collections
K=64; MK=(1<<K)-1
def f(v): return ((v<<2)^((v<<1)|v))&MK
def F(y): return (y>>1)^(y|(y<<1))
def cycles():
    seen={}; cyc=[]
    # canonical cycle representative = least element; strip id by first discovery
    for v0 in range(1,1<<12,2):
        v=v0; path={}
        while v not in path and v not in seen:
            path[v]=len(path); v=f(v)
        if v in path:
            c=[];u=v
            while True:
                c.append(u);u=f(u)
                if u==v:break
            i=c.index(min(c)); c=c[i:]+c[:i]
            idx=len(cyc); cyc.append(c)
            for j,u in enumerate(c): seen[u]=(idx,j)
        for u in path:
            seen.setdefault(u,None)
    return cyc
def top_read(y,K):
    w=y.bit_length(); s=format(y,'b')[:K]
    return int(s[::-1],2) if s else 0
if __name__=='__main__':
    for Kk in (8,12,16,20,24,32,40,48,56,64):
        M=(1<<Kk)-1; g=lambda v:((v<<2)^((v<<1)|v))&M
        reps=set(); lens=collections.Counter()
        import random
        random.seed(Kk)
        for _ in range(3000):
            v=random.getrandbits(Kk)|1
            for _ in range(4*Kk+200): v=g(v)
            c=[v];u=g(v)
            while u!=v and len(c)<5000: c.append(u);u=g(u)
            reps.add(min(c)); lens[len(c)]+=1
        print('K',Kk,'cycles found',len(reps),'lengths',sorted(lens.items()))
