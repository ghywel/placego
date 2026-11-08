#!/usr/bin/env python3
"""Thirteen retained launch fibres through one whole E, one shared cone.

Original initial-black drive, no free restart after A, no augmented clauses.
Every UNSAT proof is checked separately by a directly executed checker job.
"""
import argparse
import hashlib
import json
from pathlib import Path
from pysat.solvers import Cadical195

WORDS=(3357,4482,4498,4520,4521,4522,8797,9618,9640,9641,9642,14429,14941)


def drive(t): return int(t%2==0)


def rows(root,h):
    out=[root]
    for t in range(h):
        x=out[-1];out.append(((x<<1)|drive(t)) ^ (x|(x>>1)))
    return out


def heads(full):
    word='25'+'33535555' if full else '25'+'3'
    s=0;ones={0}
    for c in word:s+=int(c);ones.add(s)
    return {3+2*k:int(k in ones) for k in range(s+1)}


def cnf(word,full):
    h=85;w=h+1;n=0;ids=[]
    for t in range(h+1):
        ids.append(list(range(n+1,n+w-t+1)));n+=w-t
    true=n+1;clauses=[[true]]
    for t in range(h):
        for i,d in enumerate(ids[t+1]):
            a=ids[t][i-1] if i else (true if drive(t) else -true)
            b,c=ids[t][i:i+2]
            clauses.extend(([-b,a,d],[-b,-a,-d],[-c,a,d],[-c,-a,-d],
                            [b,c,-a,d],[b,c,a,-d]))
    for i in range(7):clauses.append([ids[1][i] if 64>>i&1 else -ids[1][i]])
    for t in range(14):clauses.append([ids[t+1][7] if word>>t&1 else -ids[t+1][7]])
    for t,b in heads(full).items():clauses.append([ids[t][0] if b else -ids[t][0]])
    return clauses,ids,true


def verify(root,model,ids,wanted,word,fibres):
    r=rows(root,85);positive=set(v for v in model if v>0)
    for t,rr in enumerate(ids):
        for i,v in enumerate(rr):assert (r[t]>>i&1)==int(v in positive)
    assert r[1]&127==64
    observed=sum((r[t+1]>>7&1)<<t for t in range(14));assert observed==word
    odd_prefix=r[1]&((1<<21)-1);assert odd_prefix in fibres[word]
    assert all(r[t]&1==b for t,b in wanted.items())
    cells=[root>>i&1 for i in range(root.bit_length()+90)]
    for t in range(86):
        assert sum(b<<i for i,b in enumerate(cells))==r[t]
        cells=[(drive(t) if i==0 else cells[i-1]) ^
               (cells[i]|(cells[i+1] if i+1<len(cells) else 0))
               for i in range(len(cells))]
    wrong=((root<<1)|0) ^ (root|(root>>1))
    assert (wrong&1)!=(r[1]&1), 'wrong initial phase mutant survived'
    return {'root':str(root),'width':root.bit_length(),'odd_prefix21':odd_prefix,
            'rows_hex':[hex(x) for x in r], 'input_word':observed,
            'all_cone_cells':True,'scalar_replay':True,'wrong_phase_mutant_rejected':True}


def solve_case(word,full,out,fibres):
    clauses,ids,n=cnf(word,full);stem=f'w{word}'+('' if full else '-launch')
    # Proof checked against exactly these original clauses, including units.
    path=out/(stem+'.cnf')
    with path.open('w') as f:
        f.write(f'p cnf {n} {len(clauses)}\n')
        for c in clauses:f.write(' '.join(map(str,c))+' 0\n')
    with Cadical195(bootstrap_with=clauses,with_proof=True) as solver:
        solver.conf_budget(10000 if full else 1000)
        answer=solver.solve_limited()
        result={'word':word,'full_E':full,'answer':answer,'stats':solver.accum_stats(),
                'cnf_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        if answer:
            model=solver.get_model();positive=set(x for x in model if x>0)
            root=sum(int(v in positive)<<i for i,v in enumerate(ids[0]))
            result['witness']=verify(root,model,ids,heads(full),word,fibres)
        elif answer is False:
            proof=solver.get_proof();p=out/(stem+'.drat')
            with p.open('w') as f:
                for line in proof:f.write(line+'\n')
            assert p.stat().st_size<16*1024*1024
            result['proof_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        return result


def main():
    p=argparse.ArgumentParser();p.add_argument('--fibres',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    f={int(x['word']):set(x['roots']) for x in json.loads(a.fibres.read_text())
       if x['end'] in (56,88,120)}
    assert tuple(sorted(f))==WORDS
    # Retained real fixture: its last A before E91 starts at77. Cut at74
    # (even phase), preserving the86-cell cone through actual tick159.
    known=rows(2135555,74)[-1]&((1<<86)-1);kr=rows(known,85)
    kw=sum((kr[t+1]>>7&1)<<t for t in range(14));assert kw in WORDS
    cc,ii,nn=cnf(kw,True)
    assignment={nn:True}
    for t,rr in enumerate(ii):
        assignment.update({v:bool(kr[t]>>i&1) for i,v in enumerate(rr)})
    assert all(any(assignment[abs(v)]==(v>0) for v in c) for c in cc)
    km=[v if b else -v for v,b in assignment.items()]
    control=verify(known,km,ii,heads(True),kw,f)
    (a.out/'known-fixture.json').write_text(json.dumps(control,indent=2)+'\n')
    results=[]
    for w in WORDS:
        result=solve_case(w,True,a.out,f)
        if result['answer'] is not True:
            result['launch_control']=solve_case(w,False,a.out,f)
        results.append(result)
        (a.out/'result.json').write_text(json.dumps(results,indent=2)+'\n')
        print(w,result['answer'],result['stats'],flush=True)


if __name__=='__main__':main()
