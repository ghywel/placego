"""Forward-only replay for the key CL722 passage certificates. No optimizer or search."""
import hashlib
import json
import os
from pathlib import Path

ROOT=Path(os.environ['PASSAGE_EVIDENCE'])
OUT=Path(os.environ['CAPPED_OUT'])
K,M,J,T,CUT=87867,87866,39088,122880,19543


def evolve(x,mask):
    return ((x << 2) ^ (x | (x << 1))) & mask


def replay(x,z,tape,cap):
    mask=(1 << (cap+1))-1
    x &= mask
    for d in tape:
        assert d in (1,2)
        x1=evolve(x,mask)
        if d==2 and ((x>>(z-2))&7)==2:
            z+=2
        else:
            z+=(x>>z)&1
            if d==2:z+=(x1>>z)&1
        z=min(z,cap)
        x=x1 if d==1 else evolve(x1,mask)
    assert z==cap
    return x


def packet(stage,name):
    return (ROOT/stage/name).read_bytes()


def read(stage,name):
    return json.loads(packet(stage,name))


def main():
    manifest=(ROOT/'cert-input.json').read_bytes()
    assert hashlib.sha256(manifest).hexdigest()=='6f24bdac27209f943451e30ba0278f4928312886cd0aac60475449085b9c7907'
    for name,digest in json.loads(manifest).items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    g=read('guard','guard.json')
    c=read('contact','contact.json')
    fold=read('fold','fold.json')
    other=read('gaps','gaps.json')
    raw=packet('inputs','seed-cycle.bin')
    assert hashlib.sha256(raw).hexdigest()=='28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
    width=(K+8)//8;w=[int.from_bytes(raw[i*width:(i+1)*width],'little') for i in range(16)]
    tape=packet('guard','tile-path.u8')
    assert g['matched_bits']==29329 and sum(tape)==T
    assert replay(1,29328,tape,K)==w[0]
    canon=c['canonical']; mask=(1 << (M+1))-1
    times={CUT}
    for q in canon.values():times.update((q['hit']-1,q['hit']))
    for q in other:
        if q['predicted']:times.update((q['cut'],q['predicted']-1,q['predicted']))
    snapshots={};x=1
    for t in range(max(times)+1):
        if t in times:snapshots[t]=x
        x=evolve(x,mask)
    def test_case(j,r,cut,h,need,tape):
        assert sum(tape)==h-1-cut
        x=snapshots[cut] | ((w[r]<<j)&mask)
        last=replay(x,j+need-1,tape,M)
        assert last!=snapshots[h-1] and evolve(last,mask)==snapshots[h]
    for r in range(16):
        q=canon[str(r)];o=fold['origins'][r];assert o['phase']==r
        tape=packet('contact',f'phase-{r:02}.tiles')
        assert hashlib.sha256(tape).hexdigest()==q['path_sha256']
        test_case(J,r,CUT,q['hit'],q['right_bits'],tape)
        older=packet('fold',f'origin-{r:02}.tiles')
        assert sum(older)==CUT
        x=replay(int(o['packet'],16),o['initial_right_bits']-1,older,q['right_bits']-1)
        assert x==(w[r]&((1<<q['right_bits'])-1))
    for q in other:
        if q['predicted']==0:assert q['j']>M;continue
        j,r,h=q['j'],q['phase'],q['predicted']
        tape=b'' if h==q['cut']+1 else packet('gaps',f'origin-{16*j+r:02}.tiles')
        test_case(j,r,q['cut'],h,q['required'],tape)
    assert len(other)==20
    print('CHECKED guarded seed path, 16 contact paths, 16 finite-origin paths and all 20 other gap cases')


if __name__=='__main__':main()
