#!/usr/bin/env python3
"""Direct original-CNF proof obligations for two historical column8 bits.

Only initial-black phase and the head word25·3353; no source64, fibre or DFA
assumptions. A shorter335 countermodel is retained for each conclusion.
"""
import argparse
import json
from pathlib import Path
from pysat.solvers import Cadical195


def rows(x,n):
    out=[x]
    for t in range(n):
        x=((x<<1)|int(t%2==0)) ^ (x|(x>>1));out.append(x)
    return out


def head_word(word):
    s=0;ones={0}
    for c in word:s+=int(c);ones.add(s)
    return {3+2*k:int(k in ones) for k in range(s+1)}


def build(word,negative=None):
    h=45;width=46;ids=[];n=0
    for t in range(h+1):
        ids.append(list(range(n+1,n+width-t+1)));n+=width-t
    true=n+1;c=[[true]]
    for t in range(h):
        for i,d in enumerate(ids[t+1]):
            a=ids[t][i-1] if i else (true if t%2==0 else -true)
            b,z=ids[t][i:i+2]
            c.extend(([-b,a,d],[-b,-a,-d],[-z,a,d],[-z,-a,-d],
                      [b,z,-a,d],[b,z,a,-d]))
    c.extend([ids[t][0] if b else -ids[t][0]] for t,b in head_word(word).items())
    if negative:
        t,bit=negative;c.append([ids[t][7] if bit else -ids[t][7]])
    return c,ids,true


def assignment(root,ids,true):
    rr=rows(root,45);values={true:True}
    for t,vs in enumerate(ids):values.update({v:bool(rr[t]>>i&1) for i,v in enumerate(vs)})
    return values,rr


def satisfied(c,values):return all(any(values[abs(v)]==(v>0) for v in clause) for clause in c)


def main():
    p=argparse.ArgumentParser();p.add_argument('--prefixes',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    prior={x['word']:x for x in json.loads(a.prefixes.read_text())}
    # Opposite histories from the exact last-good335 models, not a new search.
    counter={}
    for w,t,bit in [(3357,13,0),(14941,10,1)]:
        q=next(x for x in prior[w]['checks'] if x['prefix']==3 and x['answer'] is True)
        root=int(q['witness']['root'])&((1<<46)-1)
        c,ids,n=build('25335',(t,bit));vals,rr=assignment(root,ids,n)
        assert satisfied(c,vals)
        counter[t]={'root':str(root),'word':w,'column8':rr[t]>>7&1,
                    'head_word':'25335','all_clauses':True}
    # Known real A/E history controls the stronger base with neither bit fixed.
    known=rows(2135555,74)[-1]&((1<<46)-1)
    base,ids,n=build('253353');vals,rr=assignment(known,ids,n)
    assert satisfied(base,vals)
    result={'known_fixture':str(known),'shorter_prefix_countermodels':counter,'proofs':[]}
    for t,opposite in [(10,1),(13,0)]:
        c,ids,n=build('253353',(t,opposite));stem=a.out/f'guard{t}'
        with stem.with_suffix('.cnf').open('w') as f:
            f.write(f'p cnf {n} {len(c)}\n')
            for clause in c:f.write(' '.join(map(str,clause))+' 0\n')
        with Cadical195(bootstrap_with=c,with_proof=True) as s:
            s.conf_budget(5000);answer=s.solve_limited()
            r={'time':t,'opposite':opposite,'answer':answer,'stats':s.accum_stats()}
            if answer is False:
                stem.with_suffix('.drat').write_text('\n'.join(s.get_proof())+'\n')
            elif answer:
                m=set(x for x in s.get_model() if x>0)
                root=sum(int(v in m)<<i for i,v in enumerate(ids[0]))
                v,rr=assignment(root,ids,n);assert satisfied(c,v)
                r['counterexample']=str(root)
            result['proofs'].append(r)
    (a.out/'guard-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
