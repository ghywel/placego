#!/usr/bin/env python3
"""GC2366: sequential retained wall/rigidity jobs under run_capped.
Single-process solvers only. Live child CPU + reaped children + driver sampled;
external TERM/INT and every child receipt are persisted before returning.
"""
import gc
import gzip
import threading
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
from rain_to_phase import cnf2, phases
from upward_rigid import cnf as rigidity_cnf

STOP = []
OUT = None
PLAN = None
START = time.monotonic()


def save(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2)+'\n')


def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def thermal():
    r=subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=4)
    text=r.stdout+r.stderr
    with (OUT/'thermal.txt').open('a') as f:f.write(text)
    import re
    limits=re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',text)
    if r.returncode or len(limits)!=2 or any(x!='100' for x in limits):
        raise RuntimeError('THERMAL_MONITOR_STOP')


def command(name, args, budget, wall):
    if STOP: raise RuntimeError('EXTERNAL_STOP')
    def cap(): resource.setrlimit(resource.RLIMIT_CPU,(budget,budget))
    before=cpu(); t0=time.monotonic(); reason='EXIT'; last=0
    with (OUT/(name+'.stdout')).open('w') as fo, (OUT/(name+'.stderr')).open('w') as fe:
        p=subprocess.Popen(args,stdout=fo,stderr=fe,preexec_fn=cap)
        try:
            while p.poll() is None:
                now=time.monotonic()
                if STOP: reason='EXTERNAL_STOP';break
                if now-t0>=wall:reason='CHILD_WALL_STOP';break
                if now-last>=1:
                    r=subprocess.run(['ps','-p',str(p.pid),'-o','time='],capture_output=True,text=True,timeout=3)
                    if r.returncode and p.poll() is not None:break
                    fields=r.stdout.strip().split(':')
                    if r.returncode or len(fields)!=2:raise RuntimeError('CPU_MONITOR_FAILURE')
                    live=60*int(fields[0])+float(fields[1])
                    total=cpu()+live
                    save('cpu-live.json',{'worker_aggregate_cpu_s':total,'stage_wall_s':now-START,'child':name})
                    if total>=PLAN['worker_cpu_stop']:reason='AGGREGATE_CPU_STOP';break
                    if now-t0>=5 and int(now-t0)//5!=int(last-t0)//5:thermal()
                    last=now
                time.sleep(.1)
        except BaseException as e:
            reason=type(e).__name__+':'+str(e)
            STOP.append(reason)
        finally:
            if p.poll() is None:
                p.terminate()
                try:p.wait(timeout=1)
                except subprocess.TimeoutExpired:p.kill();p.wait()
            if STOP:reason='EXTERNAL_STOP:'+str(STOP)
            result={'command':args,'returncode':p.returncode,'reason':reason,'wall_s':time.monotonic()-t0,
                    'aggregate_cpu_increment_s':cpu()-before,'worker_cpu_total_s':cpu()}
            save(name+'.receipt.json',result)
    if STOP or reason.startswith(('AGGREGATE','CPU_MONITOR')):raise RuntimeError(reason)
    return result


def write_cnf(path,nv,clauses):
    with path.open('w') as f:
        f.write(f'p cnf {nv} {len(clauses)}\n')
        for c in clauses:f.write(' '.join(map(str,c))+' 0\n')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def literal_check(cols,p,kind,fixed):
    b=lambda j,t:(cols[j]>>(t%p))&1
    if kind=='wall':
        assert cols[:2]==fixed['top'] and cols[-2:]==fixed['bottom']
        assert all((b(j,t)^b(j,t+1))==(b(j-2,t)|b(j-1,t)) for j in range(2,len(cols)) for t in range(p))
    else:
        assert cols[:2]==fixed['bottom_reversed'] and cols[2]!=fixed['expected_predecessor']
        assert all((b(j,t)^b(j,t+1))==(b(j+2,t)|b(j+1,t)) for j in range(len(cols)-2) for t in range(p))


def proof_stream(name, reading):
    """Bounded gzip transport, never an expanded regular proof file."""
    fifo=OUT/(name+'.pipe')
    fifo.unlink(missing_ok=True);os.mkfifo(fifo)
    target=OUT/(name+'.lrat.gz'); receipt={}
    chunk_bytes=PLAN.get('proof_chunk_mib',0)*1024*1024
    expanded_limit=PLAN.get('proof_expanded_mib',128)*1024*1024
    def transfer():
        h=hashlib.sha256(); count=0; parts=[]
        try:
            if chunk_bytes:
                if reading:
                    with open(fifo,'rb') as source:
                        while True:
                            block=source.read(chunk_bytes)
                            if not block:break
                            count+=len(block)
                            if count>expanded_limit:raise RuntimeError('EXPANDED_PROOF_LIMIT')
                            h.update(block)
                            part=OUT/(name+'.lrat.%05d.gz'%len(parts))
                            with gzip.open(part,'wb',compresslevel=1) as dest:dest.write(block)
                            parts.append({'name':part.name,'bytes':part.stat().st_size,
                                          'sha256':hashlib.sha256(part.read_bytes()).hexdigest()})
                    save(name+'-parts.json',parts)
                else:
                    parts=json.loads((OUT/(name+'-parts.json')).read_text())
                    with open(fifo,'wb') as dest:
                        for part in parts:
                            path=OUT/part['name']
                            assert hashlib.sha256(path.read_bytes()).hexdigest()==part['sha256']
                            with gzip.open(path,'rb') as source:
                                while True:
                                    block=source.read(65536)
                                    if not block:break
                                    count+=len(block)
                                    if count>expanded_limit:raise RuntimeError('EXPANDED_PROOF_LIMIT')
                                    h.update(block);dest.write(block)
            else:
                source=open(fifo,'rb') if reading else gzip.open(target,'rb')
                with source:
                    dest=gzip.open(target,'wb',compresslevel=1) if reading else open(fifo,'wb')
                    with dest:
                        while True:
                            block=source.read(65536)
                            if not block:break
                            count+=len(block)
                            if count>expanded_limit:raise RuntimeError('EXPANDED_PROOF_LIMIT')
                            h.update(block);dest.write(block)
            receipt.update(bytes=count,sha256=h.hexdigest(),complete=True,parts=len(parts))
        except BaseException as e:
            receipt.update(bytes=count,error=repr(e),complete=False,parts=len(parts));STOP.append('PROOF_STREAM_FAILURE')
        finally:save(name+('-compress.json' if reading else '-decompress.json'),receipt)
    th=threading.Thread(target=transfer,daemon=True);th.start()
    return fifo,th,receipt


def main():
    global OUT,PLAN
    OUT=Path(os.environ['CAPPED_OUT']); PLAN=json.loads(Path(sys.argv[1]).read_text())
    for s in (signal.SIGTERM,signal.SIGINT):signal.signal(s,lambda s,f:STOP.append(s))
    resource.setrlimit(resource.RLIMIT_CPU,(PLAN.get('driver_cpu_cap',15),PLAN['process_cpu_cap']))
    results=[]
    try:
        thermal(); ph=phases()
        for job in PLAN['jobs']:
            if STOP:break
            name=job['name']; path=OUT/(name+'.cnf'); kind=job['kind'];fixed={}
            if kind=='unit':
                p=0;nv=1;cl=[[1],[-1]];n=0
            else:
                p,cols,_=ph[job['phase']];D=job['D']; mask=(1<<p)-1
                if kind=='wall':
                    a=sum(1<<t for t in range(1,p,2));tops=[[a,mask^a],[mask^a,a]]
                    bottom=[cols[-1],cols[0]]
                    top=tops[job.get('rain',0)]
                    if job.get('same_phase'):top=[cols[-D-3],cols[-D-2]]
                    nv,cl,_=cnf2(p,top,bottom,D);n=D+4
                    fixed={'top':top,'bottom':bottom}
                else:
                    nv,cl=rigidity_cnf(p,cols,0,D);n=D+2
                    fixed={'bottom_reversed':[cols[0],cols[-1]],'expected_predecessor':cols[-2]}
            digest=write_cnf(path,nv,cl)
            if job.get('hash_prefix'):assert digest.startswith(job['hash_prefix'])
            save(name+'.input.json',dict(job,cnf_sha256=digest,variables=nv,clauses=len(cl)))
            args=[job['solver'],'-q',str(path)]
            if job.get('proof'):args=[job['solver'],'-q','--lrat',str(path),str(OUT/(name+'.lrat'))]
            if job.get('compressed'):
                fifo,th,stream=proof_stream(name,True);args[-1]=str(fifo)
            rec=command(name,args,job['cpu'],job['wall'])
            if job.get('compressed'):
                th.join(timeout=3);save(name+'-compress.json',stream)
                if th.is_alive() or not stream.get('complete'):raise RuntimeError('PROOF_STREAM_FAILURE')
                fifo.unlink()

            status='SAT' if rec['returncode']==10 else 'UNSAT' if rec['returncode']==20 else 'UNKNOWN'
            result=dict(job,status=status,cnf_sha256=digest)
            if status=='SAT':
                raw=(OUT/(name+'.stdout')).read_text(); lits={int(x) for line in raw.splitlines() if line.startswith('v ') for x in line[2:].split() if x!='0'}
                assert not any(-x in lits for x in lits)
                assert all(any(l in lits for l in c) for c in cl)
                cs=[sum(1<<t for t in range(p) if 1+j*p+t in lits) for j in range(n)]
                literal_check(cs,p,kind,fixed)
                result.update(columns_hex=list(map(hex,cs)),literal_checked=True,model_checked=True)
            del cl;gc.collect()
            if status=='UNSAT' and job.get('proof'):
                proofpath=OUT/(name+'.lrat')
                if job.get('compressed'):proofpath,th,unstream=proof_stream(name,False)
                check=command(name+'-check',['/usr/local/bin/cake_lpr','--CML_HEAP_SIZE=384','--CML_STACK_SIZE=64',str(path),str(proofpath)],job['check_cpu'],job['check_wall'])
                if job.get('compressed'):
                    th.join(timeout=3);save(name+'-decompress.json',unstream)
                    assert not th.is_alive() and unstream.get('complete') and unstream['sha256']==stream['sha256']
                    proofpath.unlink()

                result['certificate_verified']=check['returncode']==0 and 's VERIFIED UNSAT' in (OUT/(name+'-check.stdout')).read_text()
                if not result['certificate_verified']:raise RuntimeError('CERTIFICATE_NOT_VERIFIED')
                if kind=='unit':
                    empty=OUT/'empty.lrat';empty.write_bytes(b'')
                    bad=command('reject-empty',['/usr/local/bin/cake_lpr','--CML_HEAP_SIZE=32','--CML_STACK_SIZE=32',str(path),str(empty)],2,3)
                    assert 's VERIFIED UNSAT' not in (OUT/'reject-empty.stdout').read_text()
                    result['empty_proof_rejected']=True
            results.append(result);save(name+'.result.json',result);print(json.dumps(result),flush=True)
            if job.get('expected') and status!=job['expected']:raise RuntimeError('CONTROL_OR_PREDICTION_MISMATCH')
            if rec['returncode']==-25:raise RuntimeError('FILE_LIMIT_STOP')
            if status=='UNKNOWN' and rec['returncode'] not in (-9,-24,-15,0):raise RuntimeError('SOLVER_FAILURE')
        if not STOP:thermal()
    finally:
        save('summary.json',{'results':results,'stop':STOP,'worker_cpu_s':cpu(),'wall_s':time.monotonic()-START})
    if STOP:raise SystemExit(2)

if __name__=='__main__':main()
