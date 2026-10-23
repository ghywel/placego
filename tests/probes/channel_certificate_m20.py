#!/usr/bin/env python3
"""CL587 job2; frozen domain/caps in reports/wolfram-agents/GPT-CHANNEL-M20.md.
Usage: python3 tests/probes/channel_certificate_m20.py OUTSIDE_GIT_OUTPUT_DIRECTORY
Retain failures; do not automatically retry a capped child or tune a certificate.
"""
import hashlib
import json
import math
import os
import resource
import subprocess
import sys
import time
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = time.monotonic()
DEN = 10**9

# malloc_size measures this owned C child's allocations without ps or privileges.
GUARD = r'''
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <malloc/malloc.h>
static size_t live_bytes=0,peak_bytes=0;
static void room(size_t base,size_t n) {
 if(n>((size_t)1<<30) || base>((size_t)1<<30)-n) {
  fprintf(stderr,"HEAP_CAP\n"); exit(91);
 }
}
static void account(void *p) {
 if(!p) {fprintf(stderr,"ALLOCATION_FAILED\n"); exit(92);}
 live_bytes+=malloc_size(p);
 if(live_bytes>peak_bytes)peak_bytes=live_bytes;
 room(0,live_bytes);
}
static void *gm(size_t n) {room(live_bytes,n);void*p=malloc(n);account(p);return p;}
static void *gc(size_t n,size_t s) {
 if(s && n>SIZE_MAX/s)exit(93);
 room(live_bytes,n*s);void*p=calloc(n,s);account(p);return p;
}
static void *gr(void*p,size_t n) {
 size_t old=p?malloc_size(p):0;
 room(live_bytes-old,n);void*q=realloc(p,n);
 live_bytes-=old;account(q);return q;
}
static void gf(void*p) {if(p)live_bytes-=malloc_size(p);free(p);}
#define malloc gm
#define calloc gc
#define realloc gr
#define free gf
#define main entropy_main
'''
SUFFIX = r'''
#undef main
int main(int argc,char**argv) {
 int rc=entropy_main(argc,argv);
 fprintf(stderr,"GUARD_PEAK_BYTES %zu\n",peak_bytes);
 return rc;
}
'''


def cpu_limit(seconds):
    return lambda: resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds+1))


def child(cmd, dest, label, cpu=240, wall=300):
    before=time.monotonic()
    with (dest/(label+'.stdout')).open('w') as out, (dest/(label+'.stderr')).open('w') as err:
        p=subprocess.Popen(cmd,stdout=out,stderr=err,preexec_fn=cpu_limit(cpu))
        try:
            code=p.wait(timeout=wall)
            result={'exit_code':code,'wall_seconds':time.monotonic()-before,'timeout':False}
        except subprocess.TimeoutExpired:
            p.kill();p.wait()
            result={'exit_code':p.returncode,'wall_seconds':time.monotonic()-before,'timeout':True}
    (dest/(label+'.receipt.json')).write_text(json.dumps(result,sort_keys=True))
    return result


def tick(dest):
    assert time.monotonic()-START < 720,'whole-job wall cap'
    assert sum(p.stat().st_size for p in dest.iterdir() if p.is_file())<=20<<20,'data output cap'
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert (rss if sys.platform=='darwin' else rss*1024)<=512<<20,'Python sampled peak RSS cap'


def check(adj,weights,num,den=DEN):
    return all(w>0 and den*sum(weights[j] for j in row if j>=0)<=num*w
               for row,w in zip(adj,weights))


def scalar_next(row,m,wall,ext):
    bits=[wall]+[(row>>i)&1 for i in range(m)]+[ext]
    return sum(((30>>(4*bits[i]+2*bits[i+1]+bits[i+2]))&1)<<i for i in range(m))


def literal_graph(m):
    first=frozenset(range(1<<m));states=[first];index={first:0};adj=[]
    for S in states:
        successors=[]
        for b in (0,1):
            T=frozenset(scalar_next(scalar_next(s,m,0,u),m,1,v)
                        for s in S if s&1==b for u in (0,1) for v in (0,1))
            if not T:
                successors.append(-1);continue
            if T not in index:
                index[T]=len(states);states.append(T)
            successors.append(index[T])
        adj.append(successors)
    return adj


def parse_certificate(path):
    adj=[];weights=[]
    for line in path.read_text().splitlines():
        i,a,b,w=line.split();assert int(i)==len(adj)
        adj.append([int(a),int(b)])
        weights.append(max(1,int((Decimal(w)*(1<<20)).to_integral_value(rounding=ROUND_CEILING))))
    assert all(-1<=j<len(adj) for row in adj for j in row)
    return adj,weights


def accepted(adj,word):
    s=0
    for b in word:
        s=adj[s][b]
        if s<0:return False
    return True


def emit_lean(adj,weights,num,path):
    # Zero sentinel for dead edges, all live state IDs shifted by one.
    lines=['import Lean','set_option maxRecDepth 200000','set_option maxHeartbeats 0',
           'namespace ChannelCertificate',
           'def weights : Array Nat := #['+','.join(map(str,[0]+weights))+']',
           'def good (r : Nat × Nat × Nat) : Bool :=',
           f'  decide (0 < r.2.2 ∧ {DEN} * (weights.getD r.1 0 + weights.getD r.2.1 0) ≤ {num} * r.2.2)']
    chunks=0
    for offset in range(0,len(adj),256):
        data=','.join(f'({a+1},{b+1},{weights[i]})' for i,(a,b) in enumerate(adj[offset:offset+256],offset))
        lines += [f'def chunk{chunks} : Array (Nat × Nat × Nat) := #[{data}]',
                  f'theorem chunk{chunks}_ok : chunk{chunks}.all good = true := by decide',
                  f'#print axioms chunk{chunks}_ok']
        chunks+=1
    lines+=['end ChannelCertificate']
    path.write_text('\n'.join(lines)+'\n')
    return chunks


def main(dest):
    assert sys.platform=='darwin','allocator wrapper is scoped to this macOS host'
    assert ROOT not in dest.parents,'certificate data must stay outside git'
    dest.mkdir(parents=True,exist_ok=False)
    original=ROOT/'tests/probes/lexicon/entropy2.c'
    source=dest/'entropy2_guarded.c'
    source.write_text(GUARD+original.read_text()+SUFFIX)
    exe=dest/'entropy2_guarded'
    cc=child(['cc','-O2','-o',str(exe),str(source),'-lm'],dest,'compile',cpu=30,wall=45)
    assert cc['exit_code']==0,'C compilation failed'
    assert check([[0,0]],[1],2,1) and not check([[0,0]],[1],1,1)
    assert check([[0,-1]],[1],1,1) and not check([[0,-1]],[1],0,1)
    controls=[]
    for m in range(1,9):
        raw=dest/f'control{m}.txt'
        r=child([str(exe),str(m),'4000','cert','0.001',str(raw)],dest,f'control{m}',cpu=30,wall=45)
        assert r['exit_code']==0
        adj,_=parse_certificate(raw)
        assert adj==literal_graph(m),('literal DFA mismatch',m)
        controls.append({'width':m,'states':len(adj)})
        tick(dest)
    lean_candidates=list((Path.home()/'.elan/toolchains').glob('leanprover--lean4---v4.33.1/bin/lean'))
    lean=lean_candidates[0] if lean_candidates else None
    results=[]
    for m,expected in ((16,2260),(20,12749)):
        raw=dest/f'raw{m}.txt'
        run=child([str(exe),str(m),'4000','cert','0.001',str(raw)],dest,f'generate{m}')
        assert run['exit_code']==0,('C construction stopped',m,run)
        adj,w=parse_certificate(raw)
        assert len(adj)==expected,('state-count mismatch',m,len(adj))
        num=max((DEN*sum(w[j] for j in row if j>=0)+w[i]-1)//w[i] for i,row in enumerate(adj))
        assert check(adj,w,num),'exact CW failure'
        assert not check(adj,w,DEN),'lambda=1 should fail'
        bad=w.copy();bad[0]=1
        assert not check(adj,bad,num),'corrupted weight should fail'
        h=math.log2(num/DEN)
        assert abs(h-({16:0.2130,20:0.1533}[m]))<0.002,'rate prediction failed'
        for seed in range(256):
            # 66 initial sites cover 32 visible observations, with a zero tail.
            row=seed;word=[];N=66;mask=(1<<N)-1
            for t in range(64):
                if not t%2:word.append(row&1)
                row=((((row<<1)|(t%2))^(row|(row>>1)))&mask)
            assert accepted(adj,word),('physical trace rejected',m,seed)
        payload={'width':m,'states':len(adj),'start':0,'dead':-1,
                 'numerator':num,'denominator':DEN,'successors':adj,'weights':w}
        path=dest/f'channel-m{m}.json'
        path.write_text(json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n')
        # Re-read via separate formula, explicitly preserving parallel edges.
        b=json.loads(path.read_text())
        for i,(a,c) in enumerate(b['successors']):
            v=(0 if a==-1 else b['weights'][a])+(0 if c==-1 else b['weights'][c])
            assert b['denominator']*v<=b['numerator']*b['weights'][i]
        lean_path=dest/f'ChannelM{m}.lean'
        chunks=emit_lean(adj,w,num,lean_path)
        bench=child([str(lean),str(lean_path)],dest,f'lean{m}',cpu=100,wall=120) if lean else {'available':False}
        if bench.get('exit_code')==0:
            out=(dest/f'lean{m}.stdout').read_text()
            assert 'sorryAx' not in out and 'ofReduceBool' not in out
            assert out.count('does not depend on any axioms')==chunks,'missing axiom receipt'
        result={'width':m,'states':len(adj),'R':num,'D':DEN,'bits_per_visible':h,
                'prefactor_ceiling':(w[0]+min(w)-1)//min(w),'max_weight_bits':max(w).bit_length(),
                'json_bytes':path.stat().st_size,'json_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                'lean_bytes':lean_path.stat().st_size,'lean_sha256':hashlib.sha256(lean_path.read_bytes()).hexdigest(),
                'generation':run,'lean_benchmark':bench,'chunks':chunks}
        results.append(result)
        print(json.dumps(result,sort_keys=True),flush=True)
        tick(dest)
    receipt={'verdict':'INTEGER_CERTIFICATES_PASS','results':results,'literal_DFA_controls':controls,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'entropy2_source_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
             'guarded_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'wall_seconds':time.monotonic()-START,
             'child_max_rss_platform_units':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
    (dest/'receipt.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True),flush=True)


if __name__=='__main__':
    main(Path(sys.argv[1]).resolve())
