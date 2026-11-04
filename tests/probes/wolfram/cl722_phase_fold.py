"""Explain the pre-contact phase quotient; transfer it back to finite initial rows."""
from array import array
from collections import Counter
from itertools import combinations
import hashlib
import json
import os
from pathlib import Path
from cl722_contact_phase import J,M,CUT,MASK,RIGHTMASK,BLOCK,agree_bits
from cl722_two_tick_guard import step,bit,one,two,exhaustive

OUT=Path(os.environ['CAPPED_OUT'])


def origin_path(start, count, last, r, table):
    mask=(1 << (last+1))-1
    blocks=[start & mask];x=blocks[0]
    for t in range(1,count+1):
        x=step(x)&mask
        if t%BLOCK==0:blocks.append(x)
    need=[last]*(count+1);take=bytearray(count)
    for b in range((count-1)//BLOCK,-1,-1):
        first=b*BLOCK;stop=min(count,first+BLOCK)
        xs=[blocks[b]]
        for _ in range(stop-first):xs.append(step(xs[-1])&mask)
        for t in range(stop-1,first-1,-1):
            a,y=xs[t-first:t-first+2]
            n=need[t+1];i=n-bit(a,n-1);take[t]=1
            if t+2<=count:
                n=need[t+2]
                assert n>=5
                j=next(z for z in range(n-2,n+1) if two(a,y,z)>=n)
                if j<i:i=j;take[t]=2
            need[t]=i
    t=0;z=need[0];y=start & mask;path=bytearray()
    while t<count:
        n=take[t];path.append(n)
        z=min(last,one(y,z) if n==1 else z+table[(y>>(z-3))&15])
        for _ in range(n):y=step(y)&mask
        t+=n
    assert t==count and z==last and y==x
    (OUT/f'origin-{r:02}.tiles').write_bytes(path)
    return need[0]+1,x


def main():
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    old=Path(os.environ['CONTACT_RESULT']).read_bytes()
    assert hashlib.sha256(old).hexdigest()=='601a9491056ac97a2e937fa514ea3adf5ba0951d9d3493bd85d267d9c33be97d'
    old=json.loads(old);data=[old['canonical'][str(r)] for r in range(16)]
    sz=(87867+8)//8
    words=[int.from_bytes(raw[r*sz:(r+1)*sz],'little') & RIGHTMASK for r in range(16)]
    labels=[q['hit'] for q in data]
    assert all(labels[r]==labels[(r+8)%16]==labels[(-r)%16] for r in range(16))
    # A four-valued label from two binary readings needs distinct codes
    # for all four labels and hence both bits constant within each label.
    def resolves(sites):
        codes={}
        for w,h in zip(words,labels):
            code=tuple(bit(w,i) for i in sites)
            if codes.setdefault(code,h)!=h:return False
        return True
    sensors=[list(pair) for pair in combinations(range(30),2) if resolves(pair)]
    assert resolves((3,8,29))
    prefix=next(i for i in range(30) if resolves(range(i+1)))
    controls=[]
    table=exhaustive()
    starts=[1]
    for _ in range(15):starts.append(step(starts[-1]))
    for r,q in enumerate(data):
        d=(r-CUT)%16;u=starts[d];length=q['right_bits']
        n,x=origin_path(u,CUT,length-1,r,table)
        assert (words[r] ^ x) & ((1<<length)-1)==0
        controls.append(dict(phase=r,descendant=d,packet=hex(u),initial_right_bits=n,hit=q['hit']))
    # Compare all canonical prefix-passage histories. Coinciding arrival times
    # are weaker than coinciding *states* through the target.
    a=1
    for _ in range(CUT):a=step(a)&MASK
    ys=[a | w<<J for w in words]
    profiles=[array('I') for _ in ys]
    pairs=[(r,s) for s in range(16) for r in range(s) if labels[r]==labels[s]]
    joins={}
    for t in range(CUT,max(labels)+1):
        for r,s in pairs:
            if (r,s) not in joins and ys[r]==ys[s]:joins[r,s]=t
        for r,y in enumerate(ys):
            first=agree_bits(y,a,M+1)
            hi=first-J
            if hi>len(profiles[r]):
                profiles[r].extend([t]*(hi-len(profiles[r])))
            assert hi==len(profiles[r])
        a=step(a)&MASK
        ys=[step(y)&MASK for y in ys]
    folded=[]
    for r,s in pairs:
        p,q=profiles[r],profiles[s]
        assert len(p)==len(q)==M-J+1 and p[-1]==q[-1]==labels[r]
        diffs=[J+i for i,(u,v) in enumerate(zip(p,q)) if u!=v]
        folded.append(dict(r=r,s=s,first_different=diffs[0] if diffs else None,
                           last_different=diffs[-1] if diffs else None,count=len(diffs),
                           target_state_join=joins[r,s],hit=labels[r]))
    # A concrete fourth-class initial row. The independent direct replay does
    # not use the clock, right-packet decomposition, or any reset path.
    y=1 | (7<<J);a=1;h=None
    for t in range(max(labels)+1):
        if a==y:h=t;break
        a=step(a)&MASK;y=step(y)&MASK
    assert h==labels[(CUT+1)%16]
    buf=b''.join(v.tobytes() for v in profiles)
    import sys
    assert sys.byteorder=='little'
    (OUT/'phase-passages.u32le').write_bytes(buf)
    counts=Counter(len({p[i] for p in profiles}) for i in range(len(profiles[0])))
    result=dict(prefix_last=prefix,pairs_in_first30=sensors,three_bit_sensor=[3,8,29],
                codes_three=[[bit(w,i) for i in (3,8,29)] for w in words],
                origins=controls,folds=folded,class_count_over_wheels=dict(counts),
                direct_fourth_hit=h,first_profile_wheel=J,last_profile_wheel=M,
                profiles_sha256=hashlib.sha256(buf).hexdigest())
    (OUT/'fold.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PHASE_FOLD_DONE',prefix,len(sensors),h)


if __name__=='__main__':main()
