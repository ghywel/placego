"""Predict final passage from the isolated right packet, before either initial component touches.

Use the sixteen legal lower-strip phases as canonical right-hand inputs. Certify
transfer from an actual packet only if a reset path shields the entire target.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import numpy as np

from cl722_two_tick_guard import step, bit, one, two, exhaustive

J, M, CUT, STOP, BLOCK = 39088, 87866, 19543, 85000, 512
MASK=(1 << (M+1))-1
RIGHTMASK=(1 << (M+1-J))-1
OUT=Path(os.environ['CAPPED_OUT'])


def agree_bits(a,b,width):
    delta=(a^b)&((1<<width)-1)
    return (delta & -delta).bit_length()-1 if delta else width


def transfer(checkpoints,h,r,table):
    # Protect every wheel through M at h-1. The mismatch then rules out any
    # earlier passage; prefix autonomy transfers the agreement at h as well.
    end=h-1-CUT; need=[M]*(end+1); take=bytearray(end)
    for b in range((end-1)//BLOCK,-1,-1):
        left=b*BLOCK;right=min(end,left+BLOCK)
        xs=[checkpoints[b]]
        for i in range(right-left):xs.append(step(xs[-1])&MASK)
        if right%BLOCK==0:assert checkpoints[right//BLOCK]==xs[-1]
        for t in range(right-1,left-1,-1):
            x,y=xs[t-left:t-left+2]
            n=need[t+1];via1=n-bit(x,n-1)
            need[t]=via1;take[t]=1
            if t+2<=end:
                n=need[t+2]
                via2=next(z for z in range(n-2,n+1) if two(x,y,z)>=n)
                if via2<via1:need[t]=via2;take[t]=2
    z=need[0]; t=0;x=checkpoints[0];path=bytearray()
    while t<end:
        d=take[t];path.append(d)
        if d==1:z=min(M,one(x,z))
        else:z=min(M,z+table[(x>>(z-3))&15])
        for _ in range(d):x=step(x)&MASK
        t+=d
    assert z==M
    (OUT/f'phase-{r:02}.tiles').write_bytes(path)
    return need[0],hashlib.sha256(path).hexdigest()


def main():
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    sz=(87867+8)//8
    words=[int.from_bytes(raw[r*sz:(r+1)*sz],'little') & RIGHTMASK for r in range(16)]
    assert all((step(w)&RIGHTMASK)==words[(r+1)%16] for r,w in enumerate(words))
    assert len({w&((1<<12000)-1) for w in words})==16
    a=1
    for t in range(CUT):a=step(a)&MASK
    assert a.bit_length()-1==J-2
    canonical=[a | (w << J) for w in words]
    checkpoints=[[x] for x in canonical]; hits={}
    for t in range(CUT,STOP+1):
        for r,x in enumerate(canonical):
            if r in hits:continue
            if x==a:
                hits[r]=t
                continue
            if t>CUT and (t-CUT)%BLOCK==0:checkpoints[r].append(x)
            canonical[r]=step(x)&MASK
        if len(hits)==16:break
        a=step(a)&MASK
    table=exhaustive()
    requirements={}
    for r,h in sorted(hits.items()):
        z,digest=transfer(checkpoints[r],h,r,table)
        requirements[r]=dict(hit=h,initial_index=z,right_bits=max(0,z-J+1),path_sha256=digest)
    reported={}
    for line in Path(__file__).with_name('white_parent_witness.out').read_text().splitlines():
        if ' J(T)=' in line:reported[line.split(' J(T)=')[0].strip()]=int(re.search(r't1=\s*(\d+)',line)[1])
    rng=np.random.default_rng(606)
    cases=[('1 + 2^39088',1)]
    for i in range(20):
        bits=rng.integers(0,2,size=87867-J,dtype=np.uint8)
        cases.append((f'random {i}',1 | int.from_bytes(np.packbits(bits,bitorder='little').tobytes(),'little') << 1))
    cases.extend([('all ones from 39088',RIGHTMASK),('alternating from 39088',sum(1 << k for k in range(0,M-J+1,2)))])
    observed=[]
    for label,y in cases:
        y &= RIGHTMASK
        for t in range(CUT):y=step(y)&RIGHTMASK
        lengths=[agree_bits(y,w,M-J+1) for w in words]
        r=max(range(16),key=lengths.__getitem__)
        ph=r if lengths[r]>=12000 else None
        # A sufficient guard may use less than the 12,000-wheel phase diagnostic.
        certified=[r for r,q in requirements.items() if lengths[r]>=q['right_bits']]
        actual=reported[label]
        for r0 in certified:assert hits[r0]==actual
        observed.append(dict(label=label,phase=ph,longest=r,matched=lengths[r],required=requirements.get(r,{}).get('right_bits'),
                             predicted=hits.get(ph),actual=actual,certified=certified,
                             shifted_control=hits.get((r+1)%16)))
    result=dict(CUT=CUT,J=J,M=M,STOP=STOP,canonical=requirements,censored=sorted(set(range(16))-set(hits)),actual=observed)
    (OUT/'contact.json').write_text(json.dumps(result,indent=2)+'\n')
    print('CONTACT_PHASE_DONE',len(hits),sum(x['predicted']==x['actual'] for x in observed),sum(bool(x['certified']) for x in observed))


if __name__=='__main__':main()
