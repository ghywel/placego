#!/usr/bin/env python3
"""GC1978: one bounded Intel search after GC1977's successful anchor gate.
Run only via run_capped.py. Reuses frozen CNF/replay; no retries or scope growth.
Discovery UNSAT is numerical; confirmed death endpoints retain binary DRAT and
both CNFs. Certificate checking is not claimed. Stops after two distinct new
confirmed deaths, completed n24/J160 scope, or an enforced limit/short-gate failure.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time
import notebook_death_gate as gate

ROOT=None; seq=0; facts={}; deaths=[]; UNKNOWN=[]
MFW=Path(__file__).resolve().parents[1]/'lexicon/rule30_local_mfw44.txt'
COUNTS={7:25,8:36,19:596,20:721,21:875,22:1054,23:1255,24:1493}


def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2)+'\n')


def log(obj):
    with (ROOT/'queries.jsonl').open('a') as f: f.write(json.dumps(obj)+'\n')


def budget():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    if a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime > 3540:
        raise RuntimeError('aggregate CPU guard at3540s')


def languages():
    text=MFW.read_text().split('## phase 1')[0]
    forbidden=[x.strip() for x in text.splitlines() if x.strip() and set(x.strip())<=set('01')]
    L={0:['']}
    for n in range(1,25):
        L[n]=[w+b for w in L[n-1] for b in '01'
              if not any((w+b).endswith(f) for f in forbidden if len(f)<=n)]
        if n in COUNTS: assert len(L[n])==COUNTS[n], (n,len(L[n]))
    save('language.json',dict(source_sha256=hashlib.sha256(MFW.read_bytes()).hexdigest(),
         counts={n:len(L[n]) for n in L},words={n:L[n] for n in [8,20,21,22,23,24]},
         coverage='exact conditional on committed, previously certified MFW completeness'))
    return L


def physical_check(w,j,cells,clauses,nv,h,output):
    vals={}
    for line in output.splitlines():
        if line.startswith('v '):
            for x in map(int,line[2:].split()):
                if x: vals[abs(x)]=x>0
    assert all(any(vals.get(abs(v))==(v>0) for v in c) for c in clauses)
    bits=[int(vals[cells[0,i]]) for i in range(1,h+2)]
    hist=gate.replay(bits,h)
    assert all(bool(hist[t][i-1])==vals[v] for (t,i),v in cells.items())
    visible=''.join(str(hist[t][0]) for t in range(0,h+1,2))
    assert visible[j:j+len(w)]==w
    return dict(initial_right=''.join(map(str,bits)),zero_tail=True,visible_trace=visible)


def solve(w,j,enc='or',proof=False):
    global seq
    budget(); seq+=1; stem=f'q{seq:05d}'
    h,cells,nv,clauses=gate.cnf(w,j,enc)
    cnfpath=ROOT/(stem+'.cnf'); outpath=ROOT/(stem+'.solver'); pp=ROOT/(stem+'.drat')
    with cnfpath.open('w') as f:
        f.write(f'p cnf {nv} {len(clauses)}\n')
        for c in clauses: f.write(' '.join(map(str,c))+' 0\n')
    sha=hashlib.sha256(cnfpath.read_bytes()).hexdigest()
    cmd=['kissat','-q',str(cnfpath)]+([str(pp)] if proof else [])
    def limits(): resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    started=time.monotonic()
    with outpath.open('w') as f:
        try:
            p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=30,preexec_fn=limits)
            rc=p.returncode
        except subprocess.TimeoutExpired: rc=None
    status={10:'SAT',20:'UNSAT'}.get(rc,'UNKNOWN')
    rec=dict(query=stem,word=w,j=j,physical_start=2*j,encoding=enc,status=status,
             returncode=rc,wall_s=time.monotonic()-started,cnf_sha256=sha,
             proof_requested=proof,proof_checked=False)
    if status=='SAT':
        rec['witness']=physical_check(w,j,cells,clauses,nv,h,outpath.read_text())
    log(rec)
    if not proof and status!='UNKNOWN':
        # Retained recipe+hash reproduces discovery CNF; witnesses stay in JSONL.
        # Confirmed death proof inputs and failures are never deleted.
        cnfpath.unlink(); outpath.unlink()
    if status=='UNKNOWN': UNKNOWN.append(dict(word=w,j=j,query=stem))
    if seq%10==0 or status=='UNKNOWN' or proof:
        print(json.dumps({k:v for k,v in rec.items() if k!='witness'}),flush=True)
    return status


def learn(w,j,status):
    if status=='SAT':
        for n in range(1,len(w)+1):
            for k in range(len(w)-n+1):
                f=w[k:k+n]; p=facts.setdefault(f,[-1,None])
                p[0]=max(p[0],j+k)
                assert p[1] is None or p[0]<p[1], 'nestedness contradiction'
    elif status=='UNSAT':
        p=facts.setdefault(w,[-1,None]);p[1]=j if p[1] is None else min(p[1],j)
        assert p[0]<p[1], 'nestedness contradiction'


def known(w,j):
    p=facts.get(w,[-1,None])
    if p[0]>=j:return 'SAT'
    for n in range(1,len(w)+1):
        for k in range(len(w)-n+1):
            q=facts.get(w[k:k+n],[-1,None])
            if q[1] is not None and j+k>=q[1]:return 'UNSAT'
    return None


def query(w,j):
    k=known(w,j)
    if k:
        log(dict(word=w,j=j,status=k,inferred=True,rule='nestedness or offset-factor'))
        return k
    r=solve(w,j);learn(w,j,r);return r


def main():
    global ROOT
    ROOT=Path(os.environ['CAPPED_OUT']);os.nice(10)
    L=languages()
    # Small initial L8 independently enumerated over all32768 15-cell inputs.
    brute=set()
    for bits in itertools.product((0,1),repeat=15):
        h=gate.replay(bits,14);brute.add(''.join(str(h[t][0]) for t in range(0,15,2)))
    assert brute==set(L[8])
    # Scope gate: establish E34^8=E100^8 by complete enumeration of initial L8.
    # Equality for length7 follows by right extendability and taking prefixes.
    g=[]
    for w in L[8]:
        a=query(w,34)
        b='UNSAT' if a=='UNSAT' else query(w,100)
        g.append(dict(word=w,at34=a,at100=b))
    save('short_gap_gate.json',g)
    passed=all(x['at34']==x['at100'] and x['at34']!='UNKNOWN' for x in g)
    print('SHORT_GAP_GATE '+str(passed),flush=True)
    if not passed:
        save('summary.json',dict(result='SHORT_GAP_GATE_FAILED_OR_UNKNOWN',main_started=False))
        return 1
    # Already dual-encoded in GC1977; record proof dependency instead of re-solving.
    for w,d in gate.CASES:
        learn(w,d-1,'SAT');learn(w,d,'UNSAT')
    tested=0;complete=[]; early=False
    for n in range(20,25):
        for w in L[n]:
            tested+=1
            a=query(w,43)
            if a!='SAT':continue
            b=query(w,160)
            if b!='UNSAT':continue
            lo,hi=43,160
            while hi-lo>1:
                m=(hi+lo)//2;r=query(w,m)
                if r=='SAT':lo=m
                elif r=='UNSAT':hi=m
                else:break
            if hi-lo!=1:continue
            # Independent encoding at both endpoints, both full proof inputs kept.
            s=solve(w,lo,'table',True);u=solve(w,hi,'table',True)
            if s=='SAT' and u=='UNSAT':
                deaths.append(dict(word=w,length=n,last_occurrence=lo,first_absence=hi,
                    certainty='two encodings + physical SAT replay; DRAT retained/unverified'))
                save('deaths.json',deaths)
                print('NEW_DEATH '+json.dumps(deaths[-1]),flush=True)
                if len({x['first_absence'] for x in deaths})>=2:
                    early=True;break
            elif s!='UNKNOWN' and u!='UNKNOWN': raise RuntimeError('encoder disagreement')
        if early:break
        complete.append(n)
        print('LENGTH_COMPLETE '+str(n)+' queries='+str(seq),flush=True)
    save('summary.json',dict(result='TWO_NEW_DEATHS' if early else 'BOUNDED_SEARCH_FINISHED',
        main_started=True,completed_lengths=complete,words_processed=tested,solver_calls=seq,
        unknown=UNKNOWN,deaths=deaths,P1=bool(deaths),P2=len({x['first_absence'] for x in deaths})>=2,
        H0_within_scope=not deaths and not UNKNOWN and complete==list(range(20,25)),
        no_soficity_verdict=True))
    return 0

if __name__=='__main__':
    try:raise SystemExit(main())
    except Exception as e:
        if ROOT:save('failure.json',dict(error=str(e),solver_calls=seq,deaths=deaths,unknown=UNKNOWN))
        raise
