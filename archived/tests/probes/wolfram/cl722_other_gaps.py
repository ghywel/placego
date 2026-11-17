"""Predict the other named CL722 passages from their own measured contact geometry."""
import hashlib
import json
import os
import re
from pathlib import Path
import numpy as np
from cl722_two_tick_guard import step,exhaustive
from cl722_contact_phase import J,M,MASK,agree_bits
from cl722_phase_fold import origin_path

OUT=Path(os.environ['CAPPED_OUT'])
STOP=85000


def main():
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    size=(87867+8)//8
    words=[int.from_bytes(raw[r*size:(r+1)*size],'little') for r in range(16)]
    rng=np.random.default_rng(606);nb=87867-J
    for _ in range(20):rng.integers(0,2,size=nb,dtype=np.uint8)
    cases=[(f'1 + 2^{j}',1<<j) for j in (39089,39090,39100,40000,45000,50000,60000,70000,80000,85000,87000,87800,87865,87866,87867)]
    for i in range(5):
        tail=rng.integers(0,2,size=nb,dtype=np.uint8)
        cases.append((f'control {i}',int.from_bytes(np.packbits(tail,bitorder='little').tobytes(),'little') << (J+1)))
    records=[];cache={};table=exhaustive()
    for label,right in cases:
        j=(right & -right).bit_length()-1
        if j>M:
            records.append(dict(label=label,j=j,predicted=0,certified=True,reason='initial agreement through target'))
            continue
        cut=(j-1)//2
        width=max(12000,M-j+1);mask=(1<<width)-1
        y=(right>>j)&mask;a=1
        for _ in range(cut):
            y=step(y)&mask;a=step(a)&MASK
        assert a.bit_length()-1==2*cut and 2*cut<j
        matches=[agree_bits(y,w,width) for w in words]
        r=max(range(16),key=matches.__getitem__)
        assert matches[r]>=12000
        if (j,r) not in cache:
            v=a | ((words[r]<<j)&MASK);v0=v
            for h in range(cut,STOP+1):
                if v==a:break
                v=step(v)&MASK;a=step(a)&MASK
            else:
                cache[j,r]=(None,None)
            if v==a:
                n,x=origin_path(v0,h-1-cut,M,16*j+r,table) if h>cut+1 else (M+1,v0)
                cache[j,r]=h,max(0,n-j)
        predicted,need=cache[j,r]
        records.append(dict(label=label,j=j,cut=cut,phase=r,matched=matches[r],required=need,
                            predicted=predicted,certified=need is not None and matches[r]>=need))
    expected={}
    for line in Path(__file__).with_name('white_parent_witness.out').read_text().splitlines():
        if ' J(T)=' in line:expected[line.split(' J(T)=')[0].strip()]=int(re.search(r't1=\s*(\d+)',line)[1])
    for r in records:
        r['actual']=expected[r['label']]
        if r['certified']:assert r['actual']==r['predicted']
    (OUT/'gaps.json').write_text(json.dumps(records,indent=2)+'\n')
    print('OTHER_GAPS_DONE',len(records),sum(r['predicted']==r['actual'] for r in records),sum(r['certified'] for r in records))


if __name__=='__main__':main()
