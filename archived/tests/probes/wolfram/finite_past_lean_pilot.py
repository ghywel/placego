#!/usr/bin/env python3
"""One frozen serial Lean development pilot; no retries, downloads or native compilation.
Use only beneath run_capped.py --track-tree. Live aggregate worker CPU accounting
adds this driver's CPU, reaped child CPU and the sole live Lean child's CPU.
Outer run_capped/time overhead is reported separately, not included in that sum.
"""
import argparse, hashlib, json, os, re, resource, shutil, subprocess, sys, time
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--lean', required=True)
p.add_argument('--kit', required=True)
p.add_argument('--sources', required=True)
a = p.parse_args()
out = Path(os.environ['CAPPED_OUT'])
src, build = out/'src', out/'build'
src.mkdir(); build.mkdir()
record = {'status':'RUNNING','cpu_stop_seconds':110,'sample_interval_seconds':0.25,
          'outer_supervisor_cpu_included':False,'runs':[],'thermal':[]}
active = None
start = time.monotonic()

def save():
    (out/'pilot.json').write_text(json.dumps(record,indent=2)+'\n')

def cpu_finished():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()+r.ru_utime+r.ru_stime

def thermal():
    r = subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=5)
    text = r.stdout+r.stderr
    nums = re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',text)
    okay = r.returncode==0 and len(nums)==2 and all(int(v)==100 for v in nums)
    okay = okay and 'No thermal warning level' in text and 'No performance warning level' in text
    record['thermal'].append({'wall':time.monotonic()-start,'exit':r.returncode,'text':text,'okay':okay})
    if not okay: raise RuntimeError('THERMAL_OR_MONITOR_STOP')

def live_cpu(pid):
    r = subprocess.run(['ps','-p',str(pid),'-o','time='],capture_output=True,text=True,timeout=5)
    if not r.stdout.strip():
        if active.poll() is not None: return 0.0
        raise RuntimeError('CPU_MONITOR_FAILURE')
    if r.returncode: raise RuntimeError('CPU_MONITOR_FAILURE')
    s=r.stdout.strip(); days=0
    if '-' in s: d,s=s.split('-',1); days=int(d)
    f=s.split(':')
    if len(f)==2: value=float(f[0])*60+float(f[1])
    elif len(f)==3: value=float(f[0])*3600+float(f[1])*60+float(f[2])
    else: raise RuntimeError('CPU_MONITOR_PARSE_FAILURE')
    # poll reaps an exited compiler, whose complete CPU is then in RUSAGE_CHILDREN.
    return 0.0 if active.poll() is not None else days*86400+value

def run(tag,args,expected_failure=False):
    global active
    thermal()
    if cpu_finished()>=110: raise RuntimeError('AGGREGATE_CPU_STOP')
    rec={'tag':tag,'expected_failure':expected_failure,'samples':[]}
    record['runs'].append(rec); save()
    env=dict(os.environ,LEAN_PATH=str(build),OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='1')
    t0=time.monotonic(); next_thermal=t0+2
    with (out/(tag+'.stdout')).open('w') as so, (out/(tag+'.stderr')).open('w') as se:
        active=subprocess.Popen([a.lean,'-j2','-M640']+args,cwd=src,env=env,stdout=so,stderr=se)
        rec['pid']=active.pid
        while active.poll() is None:
            worker=live_cpu(active.pid)
            total=cpu_finished()+worker
            rec['samples'].append([round(time.monotonic()-t0,3),round(total,4)])
            if total>=110: raise RuntimeError('AGGREGATE_CPU_STOP')
            if time.monotonic()-start>=280: raise RuntimeError('DRIVER_WALL_STOP')
            if time.monotonic()>=next_thermal:
                thermal(); next_thermal=time.monotonic()+2
            time.sleep(0.25)
        rec['exit']=active.returncode; rec['wall_seconds']=time.monotonic()-t0
        rec['aggregate_cpu_after']=cpu_finished(); active=None
    save()
    output=(out/(tag+'.stdout')).read_text()+(out/(tag+'.stderr')).read_text()
    if expected_failure:
        if rec['exit']==0 or 'type mismatch' not in output.lower():
            raise RuntimeError('NEGATIVE_CONTROL_FAILED')
    elif rec['exit']!=0 or 'sorryAx' in output:
        raise RuntimeError('COMPILATION_FAILED:'+tag)

try:
    os.nice(10)
    record['nice']=os.getpriority(os.PRIO_PROCESS,0)
    if record['nice']<10: raise RuntimeError('NICE_NOT_APPLIED')
    specs=[
      (Path(a.kit)/'lean/Ruliology/CellularAutomata/Rule30Jen.lean','Ruliology/CellularAutomata/Rule30Jen.lean','0700944834df40a026191a7fe4c1ab22114c6509a319afc1d71877e30a22c6bc'),
      (Path(a.kit)/'lean/Ruliology/CellularAutomata/Rule30Realization.lean','Ruliology/CellularAutomata/Rule30Realization.lean','da6444504fc3d9789ccdae0f042f63e980b6f0de1ce23958d5387e6d4999eac5'),
      (Path(a.sources)/'Rule30FinitePastDraft.lean','Rule30FinitePastDraft.lean','a46243a1ac7ed1732f6bbce9986c9434152f934c1e3d62ec251dee3e8c0acf3f'),
      (Path(a.sources)/'FinitePastGuard.lean','FinitePastGuard.lean','464868dfd7435abf6f842c92b9144ef3949149e56c9b1724d706a39e0806abf1')]
    record['sources']=[]
    for original,rel,expected in specs:
        data=original.read_bytes(); digest=hashlib.sha256(data).hexdigest()
        if digest!=expected: raise RuntimeError('SOURCE_HASH_MISMATCH:'+rel)
        target=src/rel; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
        (build/rel).parent.mkdir(parents=True,exist_ok=True)
        record['sources'].append({'file':rel,'sha256':digest})
    version=subprocess.run([a.lean,'--version'],text=True,capture_output=True,timeout=5)
    record['version']=version.stdout.strip()
    if version.returncode or 'version 4.33.1' not in version.stdout: raise RuntimeError('TOOLCHAIN_MISMATCH')
    save()
    for _,rel,_ in specs:
        tag=Path(rel).stem
        run(tag,['-o',str((build/rel).with_suffix('.olean')),rel])
    bad=src/'NegativeControl.lean'
    bad.write_text('import Rule30FinitePastDraft\nexample : False := by\n  exact Ruliology.CellularAutomata.Rule30FinitePastDraft.zero_not_finite_nonzero\n')
    run('NegativeControl',[bad.name],expected_failure=True)
    thermal()
    record['status']='PASS'
except BaseException as e:
    record['status']='FAILED';record['error']=str(e)
    if active is not None:
        active.terminate()
        try: active.wait(timeout=3)
        except subprocess.TimeoutExpired: active.kill();active.wait(timeout=3)
        record['active_cleanup_returncode']=active.returncode
    raise
finally:
    record['aggregate_cpu_final']=cpu_finished()
    record['wall_seconds']=time.monotonic()-start
    save()
