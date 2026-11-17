#!/usr/bin/env python3
"""GC2469: deterministic first goal-free unit unknown in both44 UP cases.
Reuse the retained positive-RUP proof. A candidate gets its own negated-cell
CNF and extracted LRAT checked without the old deviation goal; no SAT search.
"""
import ast
import bisect
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess

OUT=Path(os.environ['CAPPED_OUT']);ENC=Path(os.environ['GAP43_ENCODER'])
SOL=Path(os.environ['GAP43_SOLVE']);SUP=Path(os.environ['GAP43_SUPPORT'])
UP=Path(os.environ['GAP43_UNITS']);CHECKER='/usr/local/bin/cake_lpr'
REPORT={'status':'STARTED','commands':[]}


def hashed(path,digest):
    data=path.read_bytes();assert hashlib.sha256(data).hexdigest()==digest,path.name
    return data


def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def save():
    REPORT['worker_cpu_s']=cpu();(OUT/'lemma.json').write_text(json.dumps(REPORT,indent=2)+'\n')


def thermal():
    assert cpu()<40,'AGGREGATE_WORKER_STOP'
    r=subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=4)
    with (OUT/'thermal.txt').open('a') as f:f.write(r.stdout+r.stderr)
    vals=re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',r.stdout+r.stderr)
    assert r.returncode==0 and len(vals)==2 and set(vals)=={'100'},'THERMAL_STOP'


def checker(name,cnf,proof,cap,wall):
    thermal()
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(cap,cap))
    r=subprocess.run([CHECKER,'--CML_HEAP_SIZE=384','--CML_STACK_SIZE=64',str(cnf),str(proof)],
                     capture_output=True,text=True,timeout=wall,preexec_fn=limits)
    (OUT/(name+'.stdout')).write_text(r.stdout);(OUT/(name+'.stderr')).write_text(r.stderr)
    REPORT['commands'].append(dict(name=name,rc=r.returncode));save()
    return r.returncode,r.stdout+r.stderr


def goal_flags(steps,selected,goal):
    flags={}
    for n in sorted(selected):
        c,h=steps[n];assert all(0<v<n for v in h),'UNSUPPORTED_HINT'
        assert all(v<=214305 or v in flags for v in h),'MISSING_DEPENDENCY'
        flags[n]=any(v==goal or flags.get(v,False) for v in h)
    return flags


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));thermal()
    source=hashed(Path('tests/probes/guarded_wall_proof_support.py'),
        'a4a4deb8c8f48b32befd5878910145a3e160ec4350d4e358223a56cb69fc7df8')
    selected=[n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='rup']
    ns={};exec(compile(ast.Module(body=selected,type_ignores=[]),'retained_rup','exec'),ns);rup=ns['rup']
    toy={214306:([1],[1]),214307:([2],[214305]),214308:([3],[214306,214307])}
    assert goal_flags(toy,set(toy),214305)=={214306:False,214307:True,214308:True}
    try:goal_flags({214306:([1],[-1])},{214306},214305)
    except AssertionError:pass
    else:raise AssertionError('NEGATIVE_HINT_ACCEPTED')
    raw=hashed(ENC/'gap43.cnf','2be93cfbb953c4959a10615cb6cdc3163616c5409818e997c697b553d2bfca67')
    proof=hashed(SOL/'original.lrat','41e370e66879ab40f10b6cb2cbd1bde1677507e8aedeee6ce0d08ef21669bbbd')
    inventory=json.loads(hashed(SUP/'support-ids.json','13bcf5877e0138a65e673c9e994f5c12019e21d6e47003e65b94eab10fa25036'))
    baseline=hashed(ENC/'baseline.bits','f7077a90bf28a7e748a20a04bfc3926c13b28033b4b72e770a6ecc34a43c24fe')
    known=[]
    for name,h in (('root','2daa7e2c65582c351a6c27faca28de2cbf761987744ab64f308e57c0264006c0'),
                   ('initial44-0','b486b49ac1932c4ff82efc62cb1de9d0347432b5dec3550228ac6ea54022b7a3'),
                   ('initial44-1','9b0d930436fb995a418cc94d02e59f722589ede6cea4cc04133172d78abbaf1e')):
        trail=[json.loads(x) for x in hashed(UP/(name+'-trail.jsonl'),h).splitlines()]
        values={abs(l):int(l>0) for l,c in trail};assert len(values)==len(trail)
        known.append(values)
    assert known[1][297]==0 and known[2][297]==1
    steps={};rawsteps={}
    for line in proof.splitlines():
        f=line.split()
        if f[1]==b'd':continue
        a=list(map(int,f));z=a.index(0,1);n=a[0];assert a[-1]==0
        steps[n]=(a[1:z],a[z+1:-1]);rawsteps[n]=line+b'\n'
    selected=set(inventory['steps']);assert len(selected)==29644 and selected<=set(steps)
    flags=goal_flags(steps,selected,214305)
    candidates=[];root_candidates=[]
    for n in sorted(selected):
        c,h=steps[n]
        if len(c)!=1 or flags[n]:continue
        lit=c[0];assert baseline[abs(lit)]==int(lit>0),'GOAL_FREE_UNIT_FAILS_BASELINE'
        if abs(lit) not in known[0]:root_candidates.append(n)
        if abs(lit) not in known[1] and abs(lit) not in known[2]:candidates.append(n)
    REPORT.update(goal_free_units_unknown_at_root=len(root_candidates),
                  goal_free_units_unknown_in_both_cases=len(candidates),
                  controls='goal-dependency toy; negativehint rejected; immutable models/proof/threeclosure hashes; candidate baseline agreement')
    if not candidates:
        REPORT['status']='NO_GOAL_FREE_UNIT_OUTSIDE_BOTH_CASES';save();return
    chosen=candidates[0];lit=steps[chosen][0][0]
    starts=[];v=1
    for t in range(149):starts.append(v);v+=390-2*t
    t=bisect.bisect_right(starts,abs(lit))-1;x=-252+t+abs(lit)-starts[t]
    assert 0<t<=148 and -252+t<=x<=137-t
    ancestors=set();todo=[chosen]
    while todo:
        n=todo.pop()
        if n in ancestors:continue
        ancestors.add(n)
        if n in steps:
            assert not flags[n];todo.extend(steps[n][1])
        else:assert 1<=n<=214304
    assert 214305 not in ancestors
    lines=raw.splitlines(keepends=True);assert lines[0]==b'p cnf 36058 214305\n'
    original={i:list(map(int,line.split()))[:-1] for i,line in enumerate(lines[1:],1)}
    db={n:original[n] for n in ancestors if n<=214304}
    sub=[n for n in sorted(ancestors) if n in steps]
    for k,n in enumerate(sub):
        c,h=steps[n];assert rup(c,h,db),('SUBPROOF_REPLAY_FAILURE',n);db[n]=c
        if k%1000==0:thermal()
    query=lines[0]+b''.join(lines[1:-1])+f'{-lit} 0\n'.encode()
    empty_id=chosen+1
    extracted=b''.join(rawsteps[n] for n in sub)+f'{empty_id} 0 {chosen} 214305 0\n'.encode()
    assert len(query)<16<<20 and len(extracted)<16<<20
    qpath=OUT/'negated-cell.cnf';qpath.write_bytes(query)
    ppath=OUT/'cell.lrat';ppath.write_bytes(extracted)
    assert rup([],[chosen,214305],db|{214305:[-lit]})
    hashed(Path(CHECKER),'445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    micro=OUT/'micro.cnf';micro.write_text('p cnf 1 2\n1 0\n-1 0\n')
    good=OUT/'micro.lrat';good.write_text('3 0 1 2 0\n')
    rc,text=checker('micro-check',micro,good,1,4);assert rc==0 and 's VERIFIED UNSAT' in text
    empty=OUT/'empty.lrat';empty.write_bytes(b'')
    rc,text=checker('reject-empty',micro,empty,1,4)
    assert 's VERIFIED UNSAT' not in text and 'empty clause not derived' in text
    rc,text=checker('cell-check',qpath,ppath,8,12)
    assert rc==0 and 's VERIFIED UNSAT' in text,'CELL_LEMMA_NOT_VERIFIED'
    REPORT.update(status='GOAL_FREE_CELL_LEMMA_LRAT_CHECKED',candidate_id=chosen,literal=lit,
        physical=dict(t=t,x=x,value=int(lit>0)),candidate_selection='first retained proofID among goal-free units unknown in both44case closures',
        input_support=sum(n<=214304 for n in ancestors),derived_support=len(sub),
        original_goal_used=False,cnf_sha256=hashlib.sha256(query).hexdigest(),
        proof_sha256=hashlib.sha256(extracted).hexdigest(),proof_bytes=len(extracted),
        scope='fixed prefix43 finite physical cell; no universal capture/density/onebit memory claim')
    thermal();save();print(json.dumps(REPORT,indent=2))


try:main()
except BaseException as e:
    REPORT['status']='FAILED';REPORT['failure']=repr(e);save();raise
