"""Measure the race between the incoming phase difference and the merge front."""
import hashlib
import json
import os
from pathlib import Path
from cl722_contact_phase import J,M,CUT,MASK,RIGHTMASK
from cl722_two_tick_guard import step

OUT=Path(os.environ['CAPPED_OUT'])


def first(d):
    return (d & -d).bit_length()-1 if d else M+1


def main():
    raw=Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    size=(87867+8)//8
    a=1
    for _ in range(CUT):a=step(a)&MASK
    ys=[a|((int.from_bytes(raw[r*size:(r+1)*size],'little')&RIGHTMASK)<<J) for r in range(16)]
    pairs=[(r,r+8) for r in range(8)]+[(r,r+4) for r in (0,1,2,3,8,9,10,11)]
    probes={pair:dict(start=first(ys[pair[0]]^ys[pair[1]]),release=None,min_margin=None,
                        first_collision=None,collision_ticks=0,join=None) for pair in pairs}
    for t in range(CUT,84066):
        js=[first(y^a) for y in ys]
        for (r,s),p in probes.items():
            if p['join'] is not None:continue
            g=first(ys[r]^ys[s])
            if g>p['start'] and p['release'] is None:
                p['release']=[t,js[r],js[s],g]
            if g>M:
                p['join']=t
                continue
            # Exclude the clipped equality sentinel from numerical margins.
            e=min(js[r],js[s])
            assert (js[r]==js[s])==(g>e)
            gap=g-e
            if p['min_margin'] is None or gap<p['min_margin'][0]:p['min_margin']=[gap,t,e,g]
            if js[r]!=js[s]:
                p['collision_ticks']+=1
                if p['first_collision'] is None:p['first_collision']=[t,js[r],js[s],g]
        ys=[step(y)&MASK for y in ys];a=step(a)&MASK
    for (r,s),p in probes.items():
        assert p['start']==J+(400 if s-r==8 else 29)
        assert p['release'] and p['join']
        if s-r==8:assert p['first_collision'] is None and p['min_margin'][0]>0
    result=[dict(r=r,s=s,**p) for (r,s),p in probes.items()]
    (OUT/'separation.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PHASE_SEPARATION_DONE',len(result))


if __name__=='__main__':main()
