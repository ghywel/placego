#!/usr/bin/env python3
"""GC2465: read and replay reachable positive-RUP support of retained gap43.
No solver, changed query, trajectory, proof search or minimized-core claim.
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

OUT=Path(os.environ['CAPPED_OUT'])
ENC=Path(os.environ['GAP43_ENCODER'])
SOL=Path(os.environ['GAP43_SOLVE'])


def check_hash(path, expected):
    data=path.read_bytes()
    assert hashlib.sha256(data).hexdigest()==expected,path.name
    return data


def thermal():
    own=resource.getrusage(resource.RUSAGE_SELF);kids=resource.getrusage(resource.RUSAGE_CHILDREN)
    assert own.ru_utime+own.ru_stime+kids.ru_utime+kids.ru_stime<30,'WORKER_AGGREGATE_STOP'
    r=subprocess.run(['pmset','-g','therm'],capture_output=True,text=True,timeout=4)
    (OUT/'thermal.txt').open('a').write(r.stdout+r.stderr)
    limits=re.findall(r'CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)',r.stdout+r.stderr)
    assert r.returncode==0 and len(limits)==2 and set(limits)=={'100'},'THERMAL_STOP'


def closure(added, final, count):
    seen=set();todo=[final]
    while todo:
        n=todo.pop()
        if n in seen:continue
        seen.add(n)
        if n<=count:
            assert n>=1
            continue
        assert n in added,'MISSING_DEPENDENCY'
        hints=added[n][1]
        assert all(0<h<n for h in hints),'RAT_OR_FORWARD_HINT_UNSUPPORTED'
        todo.extend(hints)
    return seen


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    thermal()
    helper=Path('tests/probes/guarded_wall_proof_support.py')
    raw=check_hash(helper,'a4a4deb8c8f48b32befd5878910145a3e160ec4350d4e358223a56cb69fc7df8')
    functions=[x for x in ast.parse(raw).body if isinstance(x,ast.FunctionDef) and x.name=='rup']
    assert len(functions)==1
    ns={};exec(compile(ast.Module(body=functions,type_ignores=[]),str(helper),'exec'),ns)
    rup=ns['rup']
    # Known tiny dependency cone, unused clause3 and a two-step chain.
    toy={1:[1],2:[-1],3:[2]};ad={4:([1],[1]),5:([],[4,2])}
    assert closure(ad,5,3)=={1,2,4,5}
    assert rup([1],[1],toy)
    assert rup([],[4,2],{**toy,4:[1]})
    assert not rup([],[4,2],{1:[1],2:[1],4:[1]})
    for bad in ({4:([1],[-1]),5:([],[4,2])},{4:([1],[99]),5:([],[4,2])}):
        try:closure(bad,5,3)
        except AssertionError:pass
        else:raise AssertionError('NEGATIVE_CONTROL_NOT_REJECTED')
    cnf=check_hash(ENC/'gap43.cnf','2be93cfbb953c4959a10615cb6cdc3163616c5409818e997c697b553d2bfca67')
    proof=check_hash(SOL/'original.lrat','41e370e66879ab40f10b6cb2cbd1bde1677507e8aedeee6ce0d08ef21669bbbd')
    baseline=check_hash(ENC/'baseline.bits','f7077a90bf28a7e748a20a04bfc3926c13b28033b4b72e770a6ecc34a43c24fe')
    lower=check_hash(ENC/'flip43-under-cut42.bits','7cf93283d323b9df0076ff3bc19df0590f9f250a7900f3a925ea55d75083ff92')
    lines=cnf.decode().splitlines();assert lines[0]=='p cnf 36058 214305'
    original={}
    for n,line in enumerate(lines[1:],1):
        vs=list(map(int,line.split()));assert vs.pop()==0
        assert len({abs(v) for v in vs})==len(vs),'REPEATED_VARIABLE'
        original[n]=vs
    assert len(original)==214305
    def unsatisfied(bits):
        return [n for n,c in original.items() if not any(bits[abs(v)]==(v>0) for v in c)]
    assert unsatisfied(baseline)==[214305]
    assert unsatisfied(lower)==[214304]
    added={};deleted=0
    for line in proof.decode().splitlines():
        fields=line.split()
        if fields[1]=='d':deleted+=1;continue
        vs=list(map(int,fields));n=vs[0];z=vs.index(0,1)
        assert n>214305 and n not in added and vs[-1]==0
        clause,hints=vs[1:z],vs[z+1:-1]
        assert len({abs(v) for v in clause})==len(clause),'REPEATED_VARIABLE'
        added[n]=(clause,hints)
    final=max(added);assert added[final][0]==[]
    reachable=closure(added,final,214305)
    inputs={n:original[n] for n in sorted(reachable) if n<=214305}
    steps={n:added[n] for n in sorted(reachable) if n>214305}
    assert {214304,214305}<=set(inputs),'ESSENTIAL_MODEL_CONTROLS_ABSENT'
    database=dict(inputs)
    for k,(n,(clause,hints)) in enumerate(steps.items()):
        assert rup(clause,hints,database),('RUP_REPLAY_FAILURE',n)
        database[n]=clause
        if k%1000==0:
            usage=resource.getrusage(resource.RUSAGE_SELF)
            assert usage.ru_utime+usage.ru_stime<18,'CPU_GUARD'
            thermal()
    units=[n for n in inputs if 214009<=n<=214304]
    unit_positions=[n-214009-252 for n in units]
    starts=[];v=1
    for t in range(149):starts.append(v);v+=390-2*t
    def location(v):
        t=bisect.bisect_right(starts,v)-1
        return t,-252+t+v-starts[t]
    assert location(391)==(1,-251) and location(36058)==(148,-11)
    gates={}
    for n in inputs:
        if n<=214008:
            t,x=location(391+(n-1)//6)
            gates.setdefault(t,set()).add(x)
    frontier=[dict(t=t,count=len(xs),left=min(xs),right=max(xs)) for t,xs in sorted(gates.items())]
    free_inputs=sorted({abs(v)-253 for n,c in inputs.items() for v in c if 297<=abs(v)<=390})
    result=dict(status='REACHABLE_POSITIVE_RUP_SUPPORT_REPLAYED',original_clauses=214305,
        original_additions=len(added),deletion_lines_ignored=deleted,
        reachable_inputs=len(inputs),reachable_additions=len(steps),
        input_gates=sum(n<=214008 for n in inputs),input_units=len(units),
        input_positions=unit_positions,uses_goal=214305 in inputs,uses_unit43=214304 in inputs,
        gate_frontier=frontier,initial_free_variables_seen=free_inputs,
        final_id=final,reachable_nonunit_additions=sum(len(c)>1 for c,h in steps.values()),
        controls='toy closure excludes unused3; toy RUP; flippedunit rejection; negative/forward hints rejected; retained baseline/lower fullclauses',
        scope='dependency support and RUP replay, not a minimal core or a new original checker run')
    (OUT/'support-ids.json').write_text(json.dumps(dict(inputs=list(inputs),steps=list(steps)))+'\n')
    (OUT/'support.json').write_text(json.dumps(result,indent=2)+'\n')
    thermal();print(json.dumps(result,indent=2))


if __name__=='__main__':main()
