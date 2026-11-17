#!/usr/bin/env python3
"""Pinned Gimsatul build/controls/benchmark. One direct command at a time.
wait4 supplies exact reaped command CPU (all threads); sampled live CPU enforces
stage totals. run_capped supplies independent tree/pressure/disk monitoring.
"""
import hashlib,json,os,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
import intel_phase_review as mon
OUT=Path(os.environ['CAPPED_OUT']); PLAN=json.loads(Path(sys.argv[1]).read_text())
mon.OUT=OUT
STOP=[]; results=[]
for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda s,f:STOP.append(s))
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
def run(name,args,cap,wall,expected=None):
    if STOP or mon.cpu()>=PLAN['worker_cpu_stop']:raise RuntimeError('STAGE_STOP')
    mon.thermal(); t0=time.monotonic();last=0;use=None;rc=None;reason='EXIT'
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(cap,cap))
    with (OUT/(name+'.stdout')).open('w') as fo,(OUT/(name+'.stderr')).open('w') as fe:
        p=subprocess.Popen(args,stdout=fo,stderr=fe,preexec_fn=limits)
        try:
            while True:
                pid,status,use0=os.wait4(p.pid,os.WNOHANG)
                if pid:
                    use=use0;rc=os.waitstatus_to_exitcode(status);p.returncode=rc;break
                now=time.monotonic()
                if STOP:reason='EXTERNAL_STOP';break
                if now-t0>wall:reason='WALL_STOP';break
                if now-last>=.5:
                    r=subprocess.run(['ps','-p',str(p.pid),'-o','time='],capture_output=True,text=True,timeout=3)
                    if r.returncode: # a possible exit race; wait4, never assume CPU zero
                        pid,status,use0=os.wait4(p.pid,os.WNOHANG)
                        if pid:use=use0;rc=os.waitstatus_to_exitcode(status);p.returncode=rc;break
                        raise RuntimeError('CPU_MONITOR_FAILURE')
                    m,s=r.stdout.strip().split(':');live=60*int(m)+float(s)
                    total=mon.cpu()+live
                    save('live.json',{'job':name,'aggregate_cpu_s':total,'wall_s':now-t0})
                    if total>=PLAN['worker_cpu_stop']:reason='AGGREGATE_CPU_STOP';break
                    if int(now-t0)//5!=int(last-t0)//5:mon.thermal()
                    last=now
                time.sleep(.05)
        finally:
            if rc is None:
                p.terminate();deadline=time.monotonic()+1
                while True:
                    pid,status,use0=os.wait4(p.pid,os.WNOHANG)
                    if pid:use=use0;rc=os.waitstatus_to_exitcode(status);p.returncode=rc;break
                    if time.monotonic()>deadline:
                        p.kill();_,status,use=os.wait4(p.pid,0);rc=os.waitstatus_to_exitcode(status);p.returncode=rc;break
                    time.sleep(.05)
            rec={'name':name,'args':args,'returncode':rc,'reason':reason,'wall_s':time.monotonic()-t0,
                 'cpu_s':use.ru_utime+use.ru_stime,'maxrss_bytes':use.ru_maxrss,'stage_cpu_s':mon.cpu()}
            save(name+'.receipt.json',rec);results.append(rec)
    if reason!='EXIT':raise RuntimeError(reason)
    if expected is not None and rc!=expected:raise RuntimeError('UNEXPECTED_EXIT:'+name)
    mon.thermal();return rec

def model_check(cnf,output):
    lits={int(v) for line in output.splitlines() if line.startswith('v ') for v in line[2:].split() if v!='0'}
    assert not any(-v in lits for v in lits)
    clause=[]
    for line in cnf.read_text().splitlines():
        if line.startswith(('c','p')):continue
        for v in map(int,line.split()):
            if v:clause.append(v)
            else:assert any(v in lits for v in clause);clause=[]
    assert not clause

def main():
    if PLAN['mode']=='build':
        src=Path(os.environ['GIMSATUL_SOURCE']); dst=OUT/'src';dst.mkdir()
        assert subprocess.check_output(['git','-C',str(src),'rev-parse','HEAD'],text=True).strip()==PLAN['source_commit']
        assert not subprocess.check_output(['git','-C',str(src),'status','--porcelain'],text=True).strip()
        for p in src.iterdir():
            if p.suffix in ('.c','.h') or p.name in ('VERSION','LICENSE'):shutil.copyfile(p,dst/p.name)
        save('sources.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dst.iterdir()})
        version=(dst/'VERSION').read_text().strip()
        (dst/'config.h').write_text('#define VERSION '+json.dumps(version)+'\n#define GITID '+json.dumps(PLAN['source_commit'])+'\n#define COMPILER "Apple clang -O3 -DNDEBUG -Wall"\n#define BUILD "Intel Darwin; reproducible metadata without hostname"\n')
        for p in sorted(dst.glob('*.c')):
            run('build-'+p.stem,['/usr/bin/clang','-O3','-DNDEBUG','-Wall','-c',str(p),'-o',str(p.with_suffix('.o'))],5,12,0)
        binary=dst/'gimsatul'
        run('link',['/usr/bin/clang','-O3','-o',str(binary),*[str(p) for p in sorted(dst.glob('*.o'))],'-lm','-pthread'],8,15,0)
        save('binary.json',{'sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),'path':str(binary)})
    else:
        binary=Path(os.environ['GIMSATUL_BINARY']);assert hashlib.sha256(binary.read_bytes()).hexdigest()==PLAN['binary_sha256']
        for job in PLAN['jobs']:
            cnf=Path(job['cnf']);assert hashlib.sha256(cnf.read_bytes()).hexdigest()==job['sha256']
            args=[str(binary),'--threads='+str(job['threads']),str(cnf)]
            if job.get('proof'):args.append(str(OUT/(job['name']+'.drat')))
            rec=run(job['name'],args,job['cpu'],job['wall'],job.get('expected_rc'))
            if rec['returncode']==10 and job.get('known_unsat'):raise RuntimeError('KNOWN_UNSAT_DISAGREEMENT')
            if rec['returncode']==10:
                model_check(cnf,(OUT/(job['name']+'.stdout')).read_text());rec['model_checked']=True
            if rec['returncode']==20 and job.get('proof'):
                name=job['name']+'-check'
                run(name,['/usr/local/bin/drat-trim',str(cnf),str(OUT/(job['name']+'.drat'))],5,10)
                assert 's VERIFIED' in (OUT/(name+'.stdout')).read_text();rec['proof_checked']=True
            if rec['returncode'] in (-9,-24):
                if rec['cpu_s'] < .95*job['cpu']:raise RuntimeError('UNEXPLAINED_SOLVER_SIGNAL')
                rec['censored']='CPU_LIMIT'
            elif rec['returncode'] not in (10,20):raise RuntimeError('SOLVER_FAILURE')
            save(job['name']+'.receipt.json',rec)
try:main()
except BaseException as e:
    STOP.append(repr(e));raise
finally:save('summary.json',{'results':results,'worker_cpu_s':mon.cpu(),'stop':STOP})
