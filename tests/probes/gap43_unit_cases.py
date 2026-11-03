#!/usr/bin/env python3
"""GC2467: root unit closure, then only if needed the two initial44 cases.
Reasons replay independently; a successful case proof is exported as LRAT
against the unchanged original CNF, never the assumption-augmented formula.
"""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time

OUT=Path(os.environ['CAPPED_OUT']);ENC=Path(os.environ['GAP43_ENCODER'])
CHECKER='/usr/local/bin/cake_lpr'
REPORT={'status':'STARTED','cases':[],'commands':[]}


def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def save():
    REPORT['worker_cpu_s']=cpu()
    (OUT/'unit-cases.json').write_text(json.dumps(REPORT,indent=2)+'\n')


def thermal():
    assert cpu()<40,'AGGREGATE_WORKER_STOP'
    r=subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=4)
    with (OUT/'thermal.txt').open('a') as f:f.write(r.stdout+r.stderr)
    vals=re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',r.stdout+r.stderr)
    assert r.returncode==0 and len(vals)==2 and set(vals)=={'100'},'THERMAL_STOP'


def check_hash(path,digest):
    b=path.read_bytes();assert hashlib.sha256(b).hexdigest()==digest,path.name
    return b


def load_functions(path,digest,names):
    b=check_hash(path,digest)
    selected=[n for n in ast.parse(b).body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in selected}==set(names)
    ns={};exec(compile(ast.Module(body=selected,type_ignores=[]),str(path),'exec'),ns)
    return ns


def checker(name,cnf,proof,cap,wall):
    thermal()
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(cap,cap))
    t=time.monotonic()
    p=subprocess.run([CHECKER,'--CML_HEAP_SIZE=384','--CML_STACK_SIZE=64',str(cnf),str(proof)],
                     capture_output=True,text=True,timeout=wall,preexec_fn=limits)
    (OUT/(name+'.stdout')).write_text(p.stdout)
    (OUT/(name+'.stderr')).write_text(p.stderr)
    REPORT['commands'].append(dict(name=name,rc=p.returncode,wall_s=time.monotonic()-t))
    save()
    return p.returncode,p.stdout+p.stderr


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));thermal()
    ns=load_functions(Path('tests/probes/guarded_wall_boundary_screen.py'),
        'ac9cc3d6e1f93e0ce6f95a7a04f8373650301114c3a1c609bdab02b2d5564db4',
        ('unit_closure','replay'))
    close,replay=ns['unit_closure'],ns['replay']
    rup=load_functions(Path('tests/probes/guarded_wall_proof_support.py'),
        'a4a4deb8c8f48b32befd5878910145a3e160ec4350d4e358223a56cb69fc7df8',('rup',))['rup']
    for cs,expected in (([[1],[-1,2]],False),([[1],[-1]],True),([[1,2],[-1,2]],False)):
        vals,tr,passes,conflict=close(cs,2);known=replay(cs,tr,conflict)
        assert (conflict is not None)==expected
        assert len(known)==sum(v!=0 for v in vals)
    toy=[[1,2],[-1,2],[1,-2],[-1,-2]]
    assert close(toy,2)[3] is None
    for assumption in (-1,1):
        cs=[[assumption]]+toy;v,tr,p,conflict=close(cs,2)
        assert conflict is not None and tr[0]==(assumption,1)
        replay(cs,tr,conflict)
        hints=[cid-1 for _,cid in tr if cid!=1]+[conflict-1]
        assert rup([-assumption],hints,{i:c for i,c in enumerate(toy,1)})
    try:replay([[1]],[(-1,1)])
    except AssertionError:pass
    else:raise AssertionError('CORRUPT_REASON_ACCEPTED')
    check_hash(Path(CHECKER),'445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23')
    micro=OUT/'micro.cnf';micro.write_text('p cnf 1 2\n1 0\n-1 0\n')
    good=OUT/'micro.lrat';good.write_text('3 0 1 2 0\n')
    rc,text=checker('micro-check',micro,good,1,4)
    assert rc==0 and 's VERIFIED UNSAT' in text
    empty=OUT/'empty.lrat';empty.write_bytes(b'')
    rc,text=checker('reject-empty',micro,empty,1,4)
    assert 's VERIFIED UNSAT' not in text and 'empty clause not derived' in text
    raw=check_hash(ENC/'gap43.cnf','2be93cfbb953c4959a10615cb6cdc3163616c5409818e997c697b553d2bfca67')
    lines=raw.decode().splitlines();assert lines[0]=='p cnf 36058 214305'
    clauses=[]
    for line in lines[1:]:
        a=list(map(int,line.split()));assert a.pop()==0 and len({abs(v) for v in a})==len(a)
        assert all(1<=abs(v)<=36058 for v in a);clauses.append(a)
    assert len(clauses)==214305
    for name,digest,expected in (
        ('baseline.bits','f7077a90bf28a7e748a20a04bfc3926c13b28033b4b72e770a6ecc34a43c24fe',214305),
        ('flip43-under-cut42.bits','7cf93283d323b9df0076ff3bc19df0590f9f250a7900f3a925ea55d75083ff92',214304)):
        bits=check_hash(ENC/name,digest)
        bad=[i for i,c in enumerate(clauses,1) if not any(bits[abs(v)]==(v>0) for v in c)]
        assert bad==[expected]
    original={i:c for i,c in enumerate(clauses,1)}
    proof=[];derived=214306
    def run_case(name,assumption=None):
        thermal();cs=clauses if assumption is None else [[assumption]]+clauses
        vals,tr,passes,conflict=close(cs,36058)
        known=replay(cs,tr,conflict)
        assert len(known)==sum(v!=0 for v in vals)
        if conflict is None:
            for c in cs:
                if any(vals[abs(v)]==(1 if v>0 else -1) for v in c):continue
                assert sum(vals[abs(v)]==0 for v in c)>=2,'NOT_A_FIXED_POINT'
        path=OUT/(name+'-trail.jsonl')
        path.write_text(''.join(json.dumps([lit,cid])+'\n' for lit,cid in tr))
        item=dict(name=name,assumption=assumption,forced=len(tr),passes=passes,
                  conflict_clause=conflict,trail_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  scope='no-conflict is inconclusive, not SAT; case IDs shifted by1 when assumption prepended')
        REPORT['cases'].append(item);save();thermal()
        return tr,conflict
    tr,conflict=run_case('root')
    if conflict is not None:
        hints=[cid for _,cid in tr]+[conflict]
        assert rup([],hints,original)
        proof.append((derived,[],hints));REPORT['result']='ROOT_UNIT_CONTRADICTION'
    else:
        outcomes=[]
        for assumption in (-297,297):
            tr,conflict=run_case('initial44-'+str(int(assumption>0)),assumption)
            outcomes.append(conflict is not None)
            if conflict is not None:
                assert tr[0]==(assumption,1) and conflict>1
                hints=[cid-1 for _,cid in tr if cid!=1]+[conflict-1]
                clause=[-assumption];assert rup(clause,hints,original)
                proof.append((derived,clause,hints));derived+=1
        if all(outcomes):
            hints=[p[0] for p in proof];db=original|{p[0]:p[1] for p in proof}
            assert rup([],hints,db);proof.append((derived,[],hints))
            REPORT['result']='BOTH_INITIAL44_CASES_UNIT_CONTRADICTIONS'
        else:REPORT['result']='UNIT_SCREEN_INCONCLUSIVE_ORIGINAL_UNSAT_UNCHANGED'
    if proof and proof[-1][1]==[]:
        path=OUT/'short-original.lrat'
        path.write_text(''.join(str(i)+' '+' '.join(map(str,c))+(' ' if c else '')+'0 '+' '.join(map(str,h))+' 0\n' for i,c,h in proof))
        rc,text=checker('original-short-check',ENC/'gap43.cnf',path,10,15)
        assert rc==0 and 's VERIFIED UNSAT' in text,'SHORT_ORIGINAL_CERTIFICATE_NOT_VERIFIED'
        REPORT['certificate']=dict(status='UNCHANGED_CHECKER_ORIGINAL_CNF_LRAT_VERIFIED',
            additions=len(proof),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    REPORT['status']='COMPLETED';REPORT['controls']='toy propagation/conflict/incompleteness; two-case toy with RUP translation; corruptreason; micro good/emptyproof; originalmodel polarity guards'
    thermal();save();print(json.dumps(REPORT,indent=2))


try:main()
except BaseException as e:
    REPORT['status']='FAILED';REPORT['failure']=repr(e);save();raise
