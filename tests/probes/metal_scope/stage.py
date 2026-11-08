#!/usr/bin/env python3
"""Serial build/run with exact reaped CPU and sampled live all-thread CPU.
run_capped separately supplies process-tree, RSS, pressure, output and disk guards.
GPU time/latency limits in the native process are checked after completion only;
no claim that killing the host cancels an in-flight GPU dispatch.
"""
import hashlib,json,os,re,resource,signal,subprocess,sys,time
from pathlib import Path
out=Path(os.environ['CAPPED_OUT'])
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def thermal():
    r=subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=4)
    text=r.stdout+r.stderr
    with (out/'thermal.txt').open('a') as f:f.write(text)
    limits=re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',text)
    if r.returncode or len(limits)!=2 or any(x!='100' for x in limits):raise RuntimeError('THERMAL_MONITOR_STOP')
plan=json.loads(Path(sys.argv[1]).read_text());stop=[];records=[]
for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda s,f:stop.append(s))
def save(n,x):(out/n).write_text(json.dumps(x,indent=2)+'\n')
def run(job):
    args=[a.replace('{out}',str(out)).replace('{binary}',os.environ.get('METAL_SCOPE_BINARY','')) for a in job['args']]
    if stop or cpu()>=plan['worker_stop']:raise RuntimeError('STAGE_STOP')
    thermal();t=time.monotonic();last=0;rc=None;reason='EXIT';use=None
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(job['cpu'],job['cpu']))
    with (out/(job['name']+'.stdout')).open('w') as fo,(out/(job['name']+'.stderr')).open('w') as fe:
        p=subprocess.Popen(args,stdout=fo,stderr=fe,preexec_fn=limit)
        try:
            while True:
                pid,status,u=os.wait4(p.pid,os.WNOHANG)
                if pid:rc=os.waitstatus_to_exitcode(status);use=u;p.returncode=rc;break
                now=time.monotonic()
                if stop:reason='EXTERNAL_STOP';break
                if now-t>job['wall']:reason='WALL_STOP';break
                if now-last>=.5:
                    r=subprocess.run(['ps','-p',str(p.pid),'-o','time='],capture_output=True,text=True,timeout=3)
                    if r.returncode:
                        pid,status,u=os.wait4(p.pid,os.WNOHANG)
                        if pid:rc=os.waitstatus_to_exitcode(status);use=u;p.returncode=rc;break
                        raise RuntimeError('CPU_MONITOR_FAILURE')
                    m,s=r.stdout.strip().split(':');total=cpu()+60*int(m)+float(s)
                    save('live.json',{'job':job['name'],'aggregate_cpu_s':total,'wall_s':now-t})
                    if total>=plan['worker_stop']:reason='AGGREGATE_CPU_STOP';break
                    if int(now-t)//5 != int(last-t)//5:thermal()
                    last=now
                time.sleep(.05)
        finally:
            if rc is None:
                p.terminate();deadline=time.monotonic()+1
                while True:
                    pid,status,u=os.wait4(p.pid,os.WNOHANG)
                    if pid:rc=os.waitstatus_to_exitcode(status);use=u;p.returncode=rc;break
                    if time.monotonic()>deadline:
                        p.kill();_,status,use=os.wait4(p.pid,0);rc=os.waitstatus_to_exitcode(status);p.returncode=rc;break
                    time.sleep(.05)
            record={'name':job['name'],'args':args,'returncode':rc,'reason':reason,'wall_s':time.monotonic()-t,'cpu_s':use.ru_utime+use.ru_stime,'maxrss_bytes':use.ru_maxrss,'worker_cpu_s':cpu()}
            records.append(record);save(job['name']+'.receipt.json',record)
    if reason!='EXIT' or rc not in job.get('success_returncodes',[0]):
        raise RuntimeError('JOB_FAILED:'+job['name']+':'+reason)
    if job.get('required_stdout_lines'):
        lines=set((out/(job['name']+'.stdout')).read_text().splitlines())
        record['required_stdout_lines']=job['required_stdout_lines']
        record['stdout_lines_ok']=all(line in lines for line in job['required_stdout_lines'])
        save(job['name']+'.receipt.json',record)
        if not record['stdout_lines_ok']:raise RuntimeError('JOB_OUTPUT_CHECK_FAILED:'+job['name'])
    thermal()
try:
    for p,h in plan['input_sha256'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    if 'binary_sha256' in plan:
        assert hashlib.sha256(Path(os.environ['METAL_SCOPE_BINARY']).read_bytes()).hexdigest()==plan['binary_sha256'],'binary'
    for job in plan['jobs']:run(job)
    save('output_hashes.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file() and (p.suffix in ('.air','.metallib') or p.name=='scope')})
except BaseException as e:stop.append(repr(e));raise
finally:save('summary.json',{'records':records,'worker_cpu_s':cpu(),'stop':stop})
