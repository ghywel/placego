#!/usr/bin/env python3
"""GC1977: bounded Intel qualification of L1027's three historical controls.
Frozen before execution. Requires run_capped.py and CAPPED_OUT. No main search.
Visible index j is physical time 2*j, with wall x(t,0)=t%2.
Retain CNF, binary DRAT, solver output and independently replayed SAT witnesses.
UNSAT is solver-reported, not independently certificate-verified in this stage.
"""
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
CASES = [('0010001',32), ('1000101',34), ('00101010001000010101',43)]
ROOT = None
ROWS = []


def cnf(word, j, encoding):
    h = 2 * (j + len(word) - 1)
    cells = {}; clauses = []; nv = 0
    for t in range(h+1):
        for i in range(1,h-t+2):
            nv += 1; cells[t,i] = nv
    for t in range(h):
        for i in range(1,h-t+1):
            c,r,y = cells[t,i],cells[t,i+1],cells[t+1,i]
            if encoding == 'table':
                for lbit,cbit,rbit in itertools.product((0,1),repeat=3):
                    if i == 1 and lbit != t%2: continue
                    inputs = [(c,cbit),(r,rbit)]
                    if i > 1: inputs.append((cells[t,i-1],lbit))
                    clauses.append([(-v if b else v) for v,b in inputs]
                                   + [y if TABLE[4*lbit+2*cbit+rbit] else -y])
            else:
                nv += 1; o = nv
                clauses += [[-c,o],[-r,o],[c,r,-o]]
                if i == 1:
                    clauses += [[-y,-o],[y,o]] if t%2 else [[-y,o],[y,-o]]
                else:
                    l = cells[t,i-1]
                    clauses += [[-y,l,o],[-y,-l,-o],[y,-l,o],[y,l,-o]]
    for k,b in enumerate(word):
        v = cells[2*(j+k),1]; clauses.append([v if b=='1' else -v])
    return h,cells,nv,clauses


def replay(bits, h):
    row = list(bits); history = [row[:]]
    for t in range(h):
        row = [TABLE[4*(t%2 if i==0 else row[i-1])+2*row[i]+row[i+1]]
               for i in range(len(row)-1)]
        history.append(row[:])
    return history


def budget():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    if a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime > 450:
        raise RuntimeError('aggregate CPU pre-call guard')


def solve(w,j,encoding,tag):
    budget(); h,cells,nv,clauses=cnf(w,j,encoding)
    p=ROOT/tag; p.mkdir()
    with (p/'input.cnf').open('w') as f:
        f.write(f'p cnf {nv} {len(clauses)}\n')
        for c in clauses: f.write(' '.join(map(str,c))+' 0\n')
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    start=time.monotonic()
    with (p/'solver.txt').open('w') as f:
        try:
            r=subprocess.run(['kissat','-q',str(p/'input.cnf'),str(p/'proof.drat')],
                             stdout=f,stderr=subprocess.STDOUT,timeout=30,preexec_fn=limits)
            code=r.returncode
        except subprocess.TimeoutExpired:
            code=None
    status={10:'SAT',20:'UNSAT'}.get(code,'UNKNOWN')
    rec=dict(word=w,visible_index=j,physical_start=2*j,encoding=encoding,
             status=status,returncode=code,wall_s=time.monotonic()-start,
             variables=nv,clauses=len(clauses),witness_checked=False,
             proof_checked=False)
    if status=='SAT':
        vals={}
        for line in (p/'solver.txt').read_text().splitlines():
            if line.startswith('v '):
                for x in map(int,line[2:].split()):
                    if x: vals[abs(x)]=x>0
        assert all(any(vals.get(abs(v))==(v>0) for v in c) for c in clauses), 'invalid SAT model'
        bits=[int(vals[cells[0,i]]) for i in range(1,h+2)]
        hist=replay(bits,h)
        assert all(bool(hist[t][i-1])==vals[v] for (t,i),v in cells.items()), 'physical cone mismatch'
        assert ''.join(str(hist[2*(j+k)][0]) for k in range(len(w)))==w
        witness=dict(initial_right=''.join(map(str,bits)),outside_right='zero',
                     visible_trace=''.join(str(hist[t][0]) for t in range(0,h+1,2)))
        (p/'witness.json').write_text(json.dumps(witness,indent=2)+'\n')
        rec['witness_checked']=True
    (p/'result.json').write_text(json.dumps(rec,indent=2)+'\n')
    ROWS.append(rec)
    (ROOT/'results.json').write_text(json.dumps(ROWS,indent=2)+'\n')
    print(json.dumps(rec),flush=True)
    return status


def small_controls():
    # Independent exhaustive physical language, 2^9 initial rows at largest case.
    from pysat.solvers import Solver
    checks=0
    for n,j in [(1,0),(2,0),(3,0),(4,0),(3,1),(4,1)]:
        h=2*(j+n-1)
        words=set()
        for bits in itertools.product((0,1),repeat=h+1):
            hist=replay(bits,h)
            words.add(''.join(str(hist[2*(j+k)][0]) for k in range(n)))
        for tup in itertools.product('01',repeat=n):
            w=''.join(tup)
            for enc in ('table','or'):
                _,_,_,clauses=cnf(w,j,enc)
                with Solver(name='g3',bootstrap_with=clauses) as s:
                    assert s.solve()==(w in words), (w,j,enc)
                checks+=1
    # Counterfactual: adjacent visible ones are forbidden, but 01 is present.
    _,_,_,c=cnf('11',0,'table')
    with Solver(name='g3',bootstrap_with=c) as s: assert not s.solve()
    # Unexpected check: shifting a real history two physical ticks preserves
    # the wall phase, and translates the visible word by exactly one index.
    for bits in itertools.product((0,1),repeat=9):
        hist=replay(bits,8); shifted=replay(hist[2],6)
        assert shifted==hist[2:]
    (ROOT/'controls.json').write_text(json.dumps(dict(small_membership_checks=checks,
        exact_two_tick_shift_cases=512,passed=True),indent=2)+'\n')


def main():
    global ROOT
    ROOT=Path(os.environ['CAPPED_OUT']); os.nice(10)
    small_controls()
    gate=True
    for w,d in CASES:
        for j,expected in [(d-1,'SAT'),(d,'UNSAT')]:
            for enc in ('table','or'):
                got=solve(w,j,enc,f'w{len(w)}-{w}-j{j}-{enc}')
                gate &= got==expected
    summary=dict(stage='historical qualification only',gate_passed=gate,
                 main_search_launched=False,unsat_certificates_independently_checked=False)
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)
    return 0 if gate else 1

if __name__=='__main__':
    try: raise SystemExit(main())
    except Exception as e:
        if ROOT: (ROOT/'failure.json').write_text(json.dumps({'error':str(e)},indent=2)+'\n')
        raise
