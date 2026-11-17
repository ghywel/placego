"""Compare passage clocks with actual seed resets and eventual phase words."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import numpy as np

K, M, P = 87867, 87866, 16
BASE, START, END = M-128, 81700, 84100
OUT = Path(os.environ['CAPPED_OUT'])


def pinned(env, digest):
    raw = Path(os.environ[env]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest
    return raw


def step(x, mask):
    return ((x << 2) ^ ((x << 1) | x)) & mask


def edge(x, y, width):
    d = x ^ y
    return (d & -d).bit_length()-1 if d else width


def bit(x, j):
    return (x >> j) & 1


def main():
    cycle = pinned('WHITE_SEED_CYCLE','28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71')
    sz = (K+8)//8
    phases = [int.from_bytes(cycle[r*sz:(r+1)*sz],'little') for r in range(P)]
    def next_phase(s,j):
        return next((s+h+1 for h in range(P) if bit(phases[(s+h)%P],j)),None)
    width=K+1
    mask=(1 << width)-1
    ref=[]; x=1
    for t in range(END+1):
        if t >= START: ref.append(x)
        x=step(x,mask)
    seed_endpoints = {}
    for line in Path(__file__).with_name('white_parent_witness.out').read_text().splitlines():
        if ' J(T)=' in line:
            seed_endpoints[line.split(' J(T)=')[0].strip()]=int(re.search(r't1=\s*(\d+)',line)[1])
    free=39088
    cases=[(f'1 + 2^{j}',1 | 1 << j) for j in (free,39089,39090,39100,40000)]
    rng=np.random.default_rng(606)
    def random_tail():
        u=rng.integers(0,2,size=K-free,dtype=np.uint8)
        return int.from_bytes(np.packbits(u,bitorder='little').tobytes(),'little') << (free+1)
    cases.extend((f'random {i}',1 | 1 << free | random_tail()) for i in range(20))
    cases.extend([('all ones from 39088',1 | (mask ^ ((1 << free)-1))),
                  ('alternating from 39088',1 | sum(1 << j for j in range(free,K+1,2)))])
    cases.extend((f'control {i}',1 | random_tail()) for i in range(5))
    records=[]; traces={}; pooled=Counter(); failures=[]
    for label, initial in cases:
        y=initial
        for _ in range(START):y=step(y,mask)
        h={}; targets={}; previous=None
        for dt,a in enumerate(ref):
            t=START+dt
            left=edge(a,y,width)
            if previous is None: assert left < BASE
            else: assert previous <= left
            lo=BASE-1 if not h else max(h)+1
            for j in range(lo,min(M+1,left)):
                h[j]=t
                targets[j]=bit(a^y,j+1)  # discrepancy for adding the next wheel
            if left>M:
                assert t==seed_endpoints[label]
                break
            previous=left
            y=step(y,mask)
        assert BASE-1 in h and M in h and BASE <= previous <= M
        for j in range(BASE,M+1):
            s=h[j-1]; e=targets[j-1]
            actual=s if not e else next(t+1 for t in range(s,END) if bit(ref[t-START],j-1))
            predicted=s if not e else next_phase(s,j-1)
            assert actual==h[j]
            pooled['wheel_visits']+=1;pooled['inherited']+=not e
            pooled['phase_wrong']+=predicted!=actual
            if e: pooled['genuine_resets']+=1;pooled['reset_phase_wrong']+=predicted!=actual
            if predicted!=actual and len(failures)<8:
                failures.append(dict(label=label,wheel=j,entry=s,observed=actual,phase_prediction=predicted))
        u=h[M]-1; j=previous
        rec=dict(label=label,t1=u+1,source=j,source_entry=h[j-1],
                 phase_source_prediction=next_phase(h[j-1],j-1),
                 source_actual_parent=bit(ref[u-START],j-1),
                 source_phase_parent=bit(phases[u%P],j-1),
                 target_actual_parent=bit(ref[u-START],M-1),
                 target_phase_parent=bit(phases[u%P],M-1),
                 target_entry=h[M-1],target_inherited=h[M]==h[M-1])
        assert rec['source_actual_parent']==1
        records.append(rec);traces[label]=[h[j] for j in range(BASE-1,M+1)]
    # CL721's crossing of a moving band: replay just the named short head, not the previous censuses.
    original=json.loads(pinned('CROSSINGS','503707c370d626433ed214399ce203376ba10fabda9d8af5c121f7ebf9cc80e0'))
    smallmask=(1 << 6001)-1
    seed=[1]
    for _ in range(6100):seed.append(step(seed[-1],smallmask))
    old=[]
    for c in original:
        if c['t'] < 0 or c['seed'] in ('0x1','0x5'):continue
        y=int(c['seed'],16); s=c['shift']; u=c['t']; j=c['J']
        entry=None
        for v in range(u+s+1):
            t=v-s
            if t>=0 and edge(seed[t],y,6001)>=j and entry is None:entry=t
            if t==u:assert edge(seed[t],y,6001)==j
            y=step(y,smallmask)
        assert entry is not None and next(t+1 for t in range(entry,u+1) if bit(seed[t],j-1))==u+1
        old.append(dict(seed=c['seed'],cross=u,source=j,entry=entry,phase_prediction=next_phase(entry,j-1),
                        lag_edge_at_entry=edge(seed[entry],seed[entry+P],6001)))
    assert len(old)==17
    result=dict(width=width,first_profile_wheel=BASE-1,events=records,passages=traces,counts=dict(pooled),
                phase_failures=failures,old_crossings=old)
    (OUT/'passage.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASSAGE_CLOCK_DONE',len(records),dict(pooled))


if __name__=='__main__':main()
