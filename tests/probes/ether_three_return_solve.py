#!/usr/bin/env python3
"""GC2456: one separately frozen actual-row three-fast-fall SAT/LRAT attempt.
Reusable tool/CPU/checker functions come from the pinned successful driver AST.
No changed target, retry, horizon or presumed boundary input labelling.
"""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import re
import symtable
import builtins
import signal
import subprocess
import time

OUT=Path(os.environ['CAPPED_OUT'])
INPUT=Path(os.environ['RETURN_CNF_INPUT'])
MICRO=Path(os.environ['MICRO_CNF_INPUT'])
STOP=[];REPORT={'commands':[],'status':'STARTED'}
CADICAL='/usr/local/bin/cadical';CHECKER='/usr/local/bin/cake_lpr'
HELPER_HASH='11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
QUERY_HASH='b1eaa71b6dc95581ab800de9f99b2f3d5f6fff88cd37eb727659c1ecc0d98fb5'
p=Path(__file__).with_name('ether_gap_solve.py')
assert hashlib.sha256(p.read_bytes()).hexdigest()==HELPER_HASH
names={'save','cpu','thermal','command','check_proof','parse_model','load_encoder','solve'}
sel=[n for n in ast.parse(p.read_bytes()).body if isinstance(n,ast.FunctionDef) and n.name in names]
assert len(sel)==8
exec(compile(ast.Module(body=sel,type_ignores=[]),str(p),'exec'),globals())


def helper_missing_globals(namespace):
    table=symtable.symtable(ast.unparse(ast.Module(body=sel,type_ignores=[])),str(p),'exec')
    missing=set()
    def visit(scope):
        for symbol in scope.get_symbols():
            if symbol.is_referenced() and symbol.is_global():
                name=symbol.get_name()
                if name not in namespace and not hasattr(builtins,name):missing.add(name)
        for child in scope.get_children():visit(child)
    visit(table)
    return missing


# Pure dependency audit before any tool command; omission control reproduces GC2457.
assert helper_missing_globals(globals())==set(),'MISSING_HELPER_GLOBAL'
assert helper_missing_globals({k:v for k,v in globals().items() if k!='re'})=={'re'},'DEPENDENCY_NEGATIVE_CONTROL'



def query_module():
    p=Path(__file__).with_name('ether_three_return_cnf.py')
    assert hashlib.sha256(p.read_bytes()).hexdigest()==QUERY_HASH
    spec=importlib.util.spec_from_file_location('return_query',p)
    q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
    return q


def replay_physical(q,cone,model):
    free={x:model[cone.var(0,x)] for x in range(14,125)}
    scalar=cone.scalar_model(free)
    assert scalar==model,'literal scalar replay'
    cone.packed_control(model)
    # A wider physical row, not the circuit's shrinking cone, verifies the half-line guard.
    T=132;lo=-296;hi=296
    def start(x):
        return q.initial(x) if x<=13 else free.get(x,0)
    row=[start(x) for x in range(lo,hi+1)]
    a=0;events=[];trace=[];M={671,1951,4767,6047,6815}
    for t in range(T+1):
        for x in range(q.LEFT+t,q.RIGHT-t+1):
            assert row[x-lo]==model[cone.var(t,x)],'wider physical/circuit mismatch'
        assert all(row[x-lo]==q.b.TAB[(x+2)%7][(t+3)%4] for x in range(-t,a+1)),'left ether guard'
        word=sum(row[a+i-lo] << (i-1) for i in range(1,14))
        trace.append(dict(t=t,a=a,phase=(t+3)%4,word=word,u=row[a+14-lo]))
        if t in (44,88,132):assert word in M,'minimum-reset consequence'
        if t==T:break
        nexta=a-7 if (row[a-1-lo] ^ (row[a-lo] | row[a+1-lo]))!=q.b.TAB[(a+2)%7][(t+4)%4] else a
        if nexta!=a:events.append(t+1)
        row=[row[i-1] ^ (row[i] | row[i+1]) for i in range(1,len(row)-1)]
        lo+=1;a=nexta
        if t%32==0:
            assert cpu()<95,'aggregate verification budget'
    assert events==[44,88,132]
    bits=''.join(str(free[x]) for x in range(14,125))
    witness=dict(root='B3 ether left, phase3, core1951, white beyond124',
        initial_free_range=[14,124],initial_free_bits=bits,
        free_sha256=hashlib.sha256(bits.encode()).hexdigest(),
        events=events,endpoints=[trace[t] for t in (0,44,88,132)],trace=trace)
    (OUT/'actual-witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    (OUT/'model.bits').write_bytes(model)
    return {k:v for k,v in witness.items() if k!='trace'}


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(20,90))
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda s,f:STOP.append(s))
    hashes=[(Path(CADICAL),'7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a'),
      (Path(CHECKER),'445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
      (INPUT/'return1.cnf','d5d53016c5bbbf06f5573b299e436807e8527b7c903ea7087a765e8e9a5d7a3f'),
      (INPUT/'return2.cnf','1f4ba5cfdf191e1a55bf7dee998ae1586c01cf542d198c8f65a1720e8cbd6066'),
      (INPUT/'return3.cnf','1798adbec9e562205ad3dd69634d89da1884edfa8086e4d8963bf1cbb523298c'),
      (INPUT/'known-two-return-model.bits','24384d4b369f1c312bc1add72cc0f7f8335ea625c43defd00dde03aa81e06810'),
      (MICRO/'010.cnf','ad4f2afcfaad0c7d46f277c3d46dff23184ef504d84f968b294e77d519c0ae4e'),
      (MICRO/'110-gap.cnf','e78928354d3e7d5fd4f013404867a2dcbe69e730616201c85a9ab6a21ef60250')]
    for p,h in hashes:assert hashlib.sha256(p.read_bytes()).hexdigest()==h,str(p.name)
    m=load_encoder();q=query_module();cone=q.ReturnCone()
    known=(INPUT/'known-two-return-model.bits').read_bytes()
    assert not m.disk_unsatisfied(INPUT/'return1.cnf',known)
    assert not m.disk_unsatisfied(INPUT/'return2.cnf',known)
    assert m.disk_unsatisfied(INPUT/'return3.cnf',known)==[cone.count(3)]
    small=m.Cone(-3,2,2,0,lambda x:[0,1,1,0,0,0][x+3])
    status,text,_=solve('small-sat',MICRO/'110-gap.cnf',1,3)
    assert status=='SAT'
    model=parse_model(text,small.nv)
    assert not m.disk_unsatisfied(MICRO/'110-gap.cnf',model)
    assert model==small.scalar_model({1:model[small.var(0,1)],2:model[small.var(0,2)]})
    status,_,proof=solve('small-unsat',MICRO/'010.cnf',1,3)
    assert status=='UNSAT'
    check_proof('small-check',MICRO/'010.cnf',proof,1,3)
    empty=OUT/'empty.lrat';empty.write_bytes(b'')
    rc,text,_=command('reject-empty',[CHECKER,'--CML_HEAP_SIZE=64','--CML_STACK_SIZE=32',str(MICRO/'010.cnf'),str(empty)],1,3)
    assert 's VERIFIED UNSAT' not in text and 'empty clause not derived' in text
    REPORT['controls']='known1/2 DIMACS SAT; known3 only finalfall fails; microSAT actual model; microUNSAT proof checked; emptyproof rejected'
    save()
    status,text,proof=solve('original',INPUT/'return3.cnf',25,40)
    REPORT['original_status']=status
    if status=='SAT':
        model=parse_model(text,cone.nv)
        assert not m.disk_unsatisfied(INPUT/'return3.cnf',model),'original DIMACS model rejected'
        REPORT['witness']=replay_physical(q,cone,model)
    elif status=='UNSAT':
        check_proof('original-check',INPUT/'return3.cnf',proof,30,50)
        REPORT['certificate']=dict(status='ORIGINAL_LRAT_CHECKED_UNSAT',proof_bytes=proof.stat().st_size,
                                  sha256=hashlib.sha256(proof.read_bytes()).hexdigest())
    REPORT['status']='THREE_FAST_FALLS_'+status
    thermal();save();print(json.dumps(REPORT,indent=2))


try:main()
except BaseException as e:
    REPORT['status']='FAILED';REPORT['failure']=repr(e);save();raise
