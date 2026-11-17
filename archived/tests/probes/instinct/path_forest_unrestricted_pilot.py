#!/usr/bin/env python3
"""B128/MI277 standalone SAME2000 mixed pilot/checker; imports no old solver.

Frozen B57 SHA checked; original-coordinate rank checks and full domain count.
Independent full14+14 MITM catalogue + ALL123 generating-function counts.
Each variable-cardinality bin checked literally, exact next sample target,
all28 tokens and every sum. Stream excludes machine timings for reproducibility.
Caps checker30CPU/150wall/256MiB; primary200k/query,10M total,60CPU/90wall.
ONE invocation,stop first negative/cap/error;no policy repair or long run.
OUTCOME MI278:239 literal rows;target240 UNKNOWN at1B scans/109105 pending
states. All catalogue/oracle controls pass. P1/P3 miss;no rerun/cap increase.
Raw P3 reporting field excluded pending work; expression corrected BELOW after
the run, raw report retained unchanged. Full2000 runtime remains unmeasured.
Usage: python3 FILE BINARY FROZEN_B57_JSON LOCAL_OUTPUT_PREFIX
"""
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time

START=time.process_time();WALL=time.monotonic()


def rss():
    r=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r if sys.platform=='darwin' else r*1024


def budget():
    if time.process_time()-START>30 or time.monotonic()-WALL>150 or rss()>256*1024*1024:
        raise RuntimeError('checker cap')


@lru_cache(None)
def ways(n,lo,total):
    if n==0:return int(total==0)
    if total<n*lo or total>122*n:return 0
    return sum(ways(n-1,x,total-x) for x in range(lo,min(122,total//n)+1))


def rank_original(target):
    rank=0;total=784;lower=68
    for n,x in zip(range(8,0,-1),target):
        rank+=sum(ways(n-1,v,total-v) for v in range(lower,x))
        total-=x;lower=x
    assert total==0
    return rank


def verify_partition(t,bins):
    return (len(t)==8 and len(bins)==8 and all(bins) and
            Counter(x for b in bins for x in b)==Counter(range(1,56,2)) and
            all(sum(b)==x for b,x in zip(bins,t)))


def check_identity(want,got):
    if tuple(want)!=tuple(got):raise ValueError('changed/missing/duplicated sample target')


def controls():
    t=(69,69,69,93,121,121,121,121)
    b=[[1,3,5,7,9,11,33],[13,15,41],[17,21,31],[19,23,51],
       [25,43,53],[27,39,55],[29,45,47],[35,37,49]]
    assert verify_partition(t,b)
    mixed=[x[:] for x in b];mixed[0].remove(1);mixed[-1].append(1)
    assert verify_partition((68,69,69,93,121,121,121,122),mixed)
    bad=[x[:] for x in b];bad[0][0]=bad[1][0];assert not verify_partition(t,bad)
    bad=[x[:] for x in b];bad[0][0],bad[1][0]=bad[1][0],bad[0][0]
    assert Counter(v for x in bad for v in x)==Counter(range(1,56,2))
    assert not verify_partition(t,bad)
    try:check_identity(t,(69,69,69,95,119,121,121,121))
    except ValueError:pass
    else:raise AssertionError('identity guard')
    return dict(arbitrary_bin_sizes_accepted=True,duplicate_token_rejected=True,
                inventory_preserving_wrong_sums_rejected=True,next_identity_guard=True)


def catalogue_check(path):
    halves=[]
    for offset in (0,14):
        groups=defaultdict(list);sums=[0]*(1<<14)
        for bits in range(1<<14):
            if bits:
                bit=bits&-bits;j=bit.bit_length()-1
                sums[bits]=sums[bits^bit]+2*(offset+j)+1
            if sums[bits]<=122:groups[sums[bits]].append(bits<<offset)
        halves.append(groups)
    reference=[set() for _ in range(123)]
    for a,left in halves[0].items():
        for b,right in halves[1].items():
            if a+b<=122:reference[a+b].update(x|y for x in left for y in right)
        budget()
    coeff=[1]+[0]*122
    for odd in range(1,56,2):
        for s in range(122,odd-1,-1):coeff[s]+=coeff[s-odd]
    seen=set();total=0
    with path.open() as f:
        for line in f:
            row=list(map(int,line.split()));s=row[0]
            assert s not in seen and 0<=s<=122;seen.add(s)
            masks=row[1:];assert len(masks)==len(set(masks))==coeff[s]
            assert set(masks)==reference[s];total+=len(masks)
    assert seen==set(range(123)) and total==129658
    return dict(full_mitm_buckets=123,full_gf_counts=123,masks=total)


def distribution(v):
    if not v:return {}
    a=sorted(v)
    return dict(n=len(a),total=sum(a),mean=sum(a)/len(a),min=a[0],
                p50=a[(len(a)-1)*50//100],p90=a[(len(a)-1)*90//100],
                p95=a[(len(a)-1)*95//100],p99=a[(len(a)-1)*99//100],max=a[-1])


def digest(path):
    h=hashlib.sha256();size=0
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b);size+=len(b)
    return dict(bytes=size,sha256=h.hexdigest())


def main():
    if len(sys.argv)!=4:raise SystemExit(__doc__)
    binary=Path(sys.argv[1]).resolve();frozen=Path(sys.argv[2]);prefix=Path(sys.argv[3])
    paths={k:Path(str(prefix)+suffix) for k,suffix in
           [('stream','.txt'),('primary','.primary.json'),('catalogue','.catalogue.tsv'),
            ('input','.input.txt'),('report','.json')]}
    if any(p.exists() for p in paths.values()):raise SystemExit('refuse overwrite/restart')
    out={'status':'ERROR'};nodes=[]
    try:
        raw=frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'
        g=json.loads(raw)['groups'][1];records=g['rows'];targets=[tuple(r['targets']) for r in records]
        assert len(records)==len(set(targets))==2000 and g['seed']==20261017
        assert g['total_domain']==ways(8,68,784)==24688633
        for t,r in zip(targets,records):
            budget();assert tuple(sorted(t))==t and min(t)>=68 and max(t)<=122 and sum(t)==784
            assert rank_original(t)==r['rank']
        out['frozen_input_sha256']=hashlib.sha256(raw).hexdigest();out['controls']=controls()
        with paths['input'].open('x') as f:
            for t in targets:f.write(' '.join(map(str,t))+'\n')
        with paths['input'].open() as inp,paths['stream'].open('x') as stream,paths['primary'].open('x') as err:
            proc=subprocess.run([str(binary),str(paths['catalogue'])],stdin=inp,stdout=stream,stderr=err,timeout=95,check=False)
        p=json.loads(paths['primary'].read_text());out['primary']=p
        if (proc.returncode==0)!=(p['status']=='COMPLETE_SAME_2000'):raise ValueError('exit/status disagreement')
        if p['status']=='ERROR' or not p['control_nodes']:raise ValueError('primary setup/control failure')
        out['catalogue_verification']=catalogue_check(paths['catalogue'])
        with paths['stream'].open() as f:
            assert f.readline()=='# B128 unrestricted m28:8 targets;8(size,tokens);nodes\n'
            for line in f:
                budget();v=list(map(int,line.split()));assert len(v)==45
                t=tuple(v[:8]);check_identity(targets[len(nodes)],t)
                offset=8;bins=[]
                for _ in range(8):
                    n=v[offset];offset+=1
                    if not 1<=n<=28:raise ValueError('bin cardinality')
                    bins.append(v[offset:offset+n]);offset+=n
                assert offset==44 and v[-1]>0 and verify_partition(t,bins)
                nodes.append(v[-1])
        assert len(nodes)==p['completed']==len(p['query_cpu_us'])
        assert sum(nodes)+p['pending_nodes']==p['pilot_attempted_nodes']
        if p['status']=='COMPLETE_SAME_2000':
            assert len(nodes)==2000 and not p['pending_target']
            out['status']='COMPLETE_SAME_2000_LITERAL_CERTIFICATES'
        elif p['status']=='FIRST_NO_WITNESS':
            check_identity(targets[len(nodes)],p['pending_target'])
            out['status']='PRIMARY_NEGATIVE_NOT_INDEPENDENTLY_CONFIRMED'
        else:out['status']=p['status']
        out['node_distribution']=distribution(nodes)
        out['query_cpu_us_distribution']=distribution(p['query_cpu_us'])
        out['all_completed_nodes']=nodes
        out['predictions']={'all2000_no_caps':out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES',
                            'primary_mean_loop_cpu_at_most1ms':len(nodes)==2000 and p['search_loop_cpu_seconds']<=2,
                            'max_nodes_at_most5000':bool(nodes) and max(nodes+[p['pending_nodes']])<=5000}
    except subprocess.TimeoutExpired:out.update(status='UNKNOWN_WATCHDOG')
    except Exception as e:out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-START,wall_seconds=time.monotonic()-WALL,
               checker_peak_rss_bytes=rss(),literal_rows_checked=len(nodes))
    out['artifacts']={k:digest(path) for k,path in paths.items() if k!='report' and path.exists()}
    paths['report'].write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    brief={k:v for k,v in out.items() if k not in ('primary','all_completed_nodes')}
    if 'primary' in out:brief['primary_summary']={k:v for k,v in out['primary'].items() if k!='query_cpu_us'}
    print(json.dumps(brief,sort_keys=True,separators=(',',':')))
    return 0 if out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES' else 2


if __name__=='__main__':raise SystemExit(main())
