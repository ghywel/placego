#!/usr/bin/env python3
"""GC2454: encoder-only exact actual-row question: three consecutive44tick first falls from rho; endpoint words free.
No free per-tick boundary driver: all cells come from one initial row. No solver.
"""
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import resource
import time

OUT=Path(os.environ['CAPPED_OUT'])
ENCODER_HASH='0a0ab05fab78bfd99941e5574c7488f30e212ecdae36afb088a527a03ff18425'
PARENT_HASH='007321f1b4231e731621ef8e41bf73010f7a8973da9730506c494dab571c2eda'
TAIL_HASH='5e9e0870f9730666926f49cefb51a48dcba13713da5fed48beb8c70a5b25f1e7'
FRAME_HASH='c777a9b782d5af8466e7717755852db1c81204d54e1f3f0c45a17932b1c3df21'
HERE=Path(__file__).resolve().parent

def load(name,path,digest):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

m=load('literal_encoder',HERE/'ether_tail_cnf.py',ENCODER_HASH)
b=load('physical_oracle',HERE/'ether_retained_history_check.py',PARENT_HASH)
RHO=1951
LEFT,RIGHT,T=-152,124,132


def initial(x):
    return b.TAB[(x+2)%7][3] if x<=0 else ((RHO>>(x-1))&1 if x<=13 else 0)


class ReturnCone(m.Cone):
    def __init__(self):
        super().__init__(LEFT,RIGHT,T,13,initial)
    def goals(self,n):
        # Before each prescribed first re-anchor, its old anchor stays in the ether.
        for t in range(1,44*n):
            a=-7*(t//44)
            val=b.TAB[(a+2)%7][(t+3)%4]
            yield self.var(t,a),val,dict(kind='stable_anchor',t=t,x=a)
        for j in range(1,n+1):
            a=-7*(j-1);t=44*j
            yield self.var(t,a),0,dict(kind='fall',t=t,x=a)
    def clauses(self,n=3):
        for t in range(1,T+1):
            for x in range(LEFT+t,RIGHT-t+1):
                yield from m.gate(self.var(t-1,x-1),self.var(t-1,x),self.var(t-1,x+1),self.var(t,x))
        for v,val in self.fixed:yield [v if val else -v]
        for v,val,_ in self.goals(n):yield [v if val else -v]
    def count(self,n=3):return 6*(self.nv-self.widths[0])+len(self.fixed)+(44*n-1)+n
    def write(self,path,n=3):
        def lines():
            yield ('p cnf %d %d\n'%(self.nv,self.count(n))).encode()
            for cl in self.clauses(n):yield (' '.join(map(str,cl))+' 0\n').encode()
        size=sum(len(x) for x in lines());assert size<16<<20
        h=hashlib.sha256()
        with path.open('wb') as f:
            for x in lines():h.update(x);f.write(x)
        assert path.stat().st_size==size
        return dict(variables=self.nv,clauses=self.count(n),bytes=size,sha256=h.hexdigest())


def actual_template():
    bits=Path(os.environ['RETAINED_TAIL_BITS']).read_text().strip()
    assert len(bits)==1200 and hashlib.sha256(bits.encode()).hexdigest()==TAIL_HASH
    value=sum(int(c)<<i for i,c in enumerate(bits))
    # B(431, x-68), x=-152..124; start with its exact radius431 cone.
    lo,hi=LEFT-68-431,RIGHT-68+431
    row=[b.TAB[x%7][0] if x<0 else ((value>>x)&1) for x in range(lo,hi+1)]
    packed=sum(v<<i for i,v in enumerate(row));width=len(row)
    for t in range(431):
        row=[row[i-1] ^ (row[i] | row[i+1]) for i in range(1,len(row)-1)]
        packed=(((packed<<1) ^ (packed | (packed>>1)))>>1)&((1<<(width-2))-1)
        width-=2
        assert bytes(row)==bytes((packed>>i)&1 for i in range(width))
        if t%32==0:b.budget()
    assert len(row)==277
    return row


def main():
    assert resource.getrlimit(resource.RLIMIT_CPU)[0]<=20
    b.budget();b.kit_control()
    accepted=0
    for a,c,r,y in itertools.product((0,1),repeat=4):
        good=all(m.check_clause(cl,[0,a,c,r,y]) for cl in m.gate(1,2,3,4))
        assert good==(y==(a ^ (c|r)));accepted+=good
    assert accepted==8
    cone=ReturnCone();assert cone.nv==19285 and len(cone.fixed)==166
    assert cone.nv-cone.widths[0]==19008
    rows=actual_template()
    assert all(rows[x-LEFT]==initial(x) for x in range(LEFT,14))
    full=cone.scalar_model({x:rows[x-LEFT] for x in range(14,125)})
    cone.packed_control(full)
    paths={n:OUT/('return%d.cnf'%n) for n in (1,2,3)}
    result=dict(status='ENCODER_STARTED',solver_run=False,gate_assignments=16,gate_models=accepted,
        dimensions=dict(left=LEFT,right=RIGHT,T=T,variables=cone.nv,gates=19008,
                        fixed_initial=166,free_initial=list(range(14,125))),files={})
    for n in (1,2,3):
        result['files'][str(n)]=cone.write(paths[n],n)
        bad=m.disk_unsatisfied(paths[n],full)
        if n<3:assert bad==[]
        else:
            assert bad and min(bad)>6*19008+166
            expected_bad=[detail for v,val,detail in cone.goals(3) if full[v]!=val]
            assert all(g['kind']=='fall' and g['t']==132 for g in expected_bad)
            result['known_two_return_row_fails_three']=expected_bad
        b.budget()
    frame=Path(os.environ['RETAINED_FRAME_TRACE']).read_bytes()
    assert hashlib.sha256(frame).hexdigest()==FRAME_HASH
    frame=json.loads(frame)
    # The actual normalized third block is captured; it stays at anchor-14, not-21.
    for rel in (0,44,88,127,132):
        r=frame[431+rel];a=r['a']+68
        for i in range(1,14):
            if LEFT+rel<=a+i<=RIGHT-rel:
                assert full[cone.var(rel,a+i)]==((r['word']>>(i-1))&1)
    broken=full[:];broken[cone.var(1,LEFT+1)]^=1
    assert any(i<=6*19008 for i in m.disk_unsatisfied(paths[2],broken))
    (OUT/'known-two-return-model.bits').write_bytes(full)
    (OUT/'known-template.bits').write_text(''.join(map(str,rows))+'\n')
    result.update(status='ENCODER_CONTROLS_PASS',known_model_sha256=hashlib.sha256(full).hexdigest(),
        controls='gate truth table; packed/list B431 extraction; DIMACS known1/2 SAT, known3 lastfall-only failure; corruptgate rejection; B431..563 frame match',
        worker_cpu_s=b.cpu(),worker_wall_s=time.monotonic()-b.START_WALL)
    (OUT/'encoder.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
