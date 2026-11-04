"""Exact one- or two-update guarantees for a prefix and an otherwise free tail."""
import hashlib
import json
import os
from pathlib import Path

K, T, BLOCK, TAU = 87867, 122880, 512, 117323
MASK=(1 << (K+1))-1
OUT=Path(os.environ['CAPPED_OUT'])


def step(x):
    return (x<<2) ^ ((x<<1)|x)


def bit(x,k):
    return (x >> k) & 1


def one(x,z):
    return z+bit(x,z)


def two(x,y,z):
    first=one(x,z)
    return one(y,first)+int((x >> (z-2)) & 7 == 2)


def exhaustive():
    # Four old common bits (indices 0..3); expose EVERY extension through bit 6.
    table=[]
    for common in range(16):
        words=[step(step(common | (tail << 4))) & 127 for tail in range(8)]
        varied=0
        for w in words:varied |= w ^ words[0]
        assert varied
        z=(varied & -varied).bit_length()-2
        assert z==two(common,step(common),3) and z<=5
        table.append(z-3)
    return table


def main():
    assert T%BLOCK==0
    table=exhaustive()
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    ref=int.from_bytes(raw[:(K+8)//8],'little')
    blocks=[1];a=1
    for t in range(1,T+1):
        a=step(a)&MASK
        if t%BLOCK==0:blocks.append(a)
    assert a==ref
    need=[K]*(T+1); take=bytearray(T)
    for b in range(T//BLOCK-1,-1,-1):
        xs=[blocks[b]]
        for _ in range(BLOCK): xs.append(step(xs[-1])&MASK)
        assert xs[-1]==blocks[b+1]
        for i in range(BLOCK-1,-1,-1):
            t=b*BLOCK+i;x,y=xs[i:i+2]
            n=need[t+1];via1=n-bit(x,n-1)
            need[t]=via1;take[t]=1
            if t+2<=T:
                n=need[t+2]
                via2=next(z for z in range(n-2,n+1) if two(x,y,z)>=n)
                if via2<via1:need[t]=via2;take[t]=2
    # Independent forward maximization over both last-tile lengths, using the
    # exhaustive truth table (not the closed two-tick formula).
    starts=[39087,39088,need[0],need[0]-1]
    best=starts[:];prior=None;previous=None;a=1; arrivals=[{} for z in starts]
    path=bytearray();z=need[0];when=0;new_tiles=0
    for t in range(T):
        if t==when:
            d=take[t];path.append(d)
            if d==1: z=min(K,one(a,z))
            else:
                assert z>=3
                new_tiles+=((a>>(z-2))&7)==2
                z=min(K,z+table[(a>>(z-3))&15])
            when+=d
            assert z>=need[when]
        nxt=[]
        for i,index in enumerate(best):
            n=min(K,one(a,index))
            if prior is not None:
                j=prior[i]
                n=max(n,min(K,j+table[(previous>>(j-3))&15]))
            nxt.append(n)
            for target in (K-1,K):
                if n>=target:arrivals[i].setdefault(target,t+1)
        prior,best=best,nxt
        previous,a=a,step(a)&MASK
    assert z==K and when==T
    assert best[2]==K and best[3]<K
    assert best[1]==K
    (OUT/'tile-path.u8').write_bytes(path)
    result=dict(T=T,K=K,initial_inclusive=need[0],matched_bits=need[0]+1,
                starts=starts,ends=best,arrivals=arrivals,table=table,
                ones=path.count(1),twos=path.count(2),strict_special_tiles=new_tiles,
                path_sha256=hashlib.sha256(path).hexdigest(),known_last_black=TAU)
    (OUT/'guard.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TWO_TICK_GUARD_DONE',result)


if __name__=='__main__':main()
