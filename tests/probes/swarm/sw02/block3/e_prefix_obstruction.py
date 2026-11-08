#!/usr/bin/env python3
"""Locate the earliest impossible E prefix inside the already frozen cone."""
import argparse
import json
from pathlib import Path
from pysat.solvers import Cadical195
from e_launch_completion import cnf,heads,verify

E='33535555'


def wanted(k):
    word='25'+E[:k];s=0;ones={0}
    for c in word:s+=int(c);ones.add(s)
    return {3+2*t:int(t in ones) for t in range(s+1)}


def solve(w,k,out,fibres):
    c,ids,n=cnf(w,True);old=heads(True)
    assert c[-len(old):]==[[ids[t][0] if b else -ids[t][0]] for t,b in old.items()]
    c=c[:-len(old)]+[[ids[t][0] if b else -ids[t][0]] for t,b in wanted(k).items()]
    stem=out/f'w{w}-prefix{k}'
    with stem.with_suffix('.cnf').open('w') as f:
        f.write(f'p cnf {n} {len(c)}\n')
        for clause in c:f.write(' '.join(map(str,clause))+' 0\n')
    with Cadical195(bootstrap_with=c,with_proof=True) as s:
        s.conf_budget(5000);answer=s.solve_limited()
        r={'prefix':k,'answer':answer,'stats':s.accum_stats()}
        if answer:
            model=s.get_model();pos=set(x for x in model if x>0)
            root=sum(int(v in pos)<<i for i,v in enumerate(ids[0]))
            r['witness']=verify(root,model,ids,wanted(k),w,fibres)
        elif answer is False:
            with stem.with_suffix('.drat').open('w') as f:
                for line in s.get_proof():f.write(line+'\n')
        return r


def main():
    p=argparse.ArgumentParser();p.add_argument('--prior',type=Path,required=True)
    p.add_argument('--fibres',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    prior=json.loads(a.prior.read_text());fibres={x['word']:set(x['roots']) for x in json.loads(a.fibres.read_text())}
    result=[]
    for item in prior:
        if item['answer'] is not False:continue
        assert item['launch_control']['answer'] is True
        w=item['word'];lo,hi=1,8;checks=[]
        while hi-lo>1:
            k=(lo+hi)//2;r=solve(w,k,a.out,fibres);checks.append(r)
            if r['answer'] is None:break
            if r['answer']:lo=k
            else:hi=k
        r={'word':w,'last_good':lo,'first_bad':hi,'checks':checks,
           'exact':hi-lo==1,'last_good_from_prior':lo==1,'first_bad_from_prior':hi==8}
        result.append(r);(a.out/'prefix-result.json').write_text(json.dumps(result,indent=2)+'\n')
        print(w,lo,hi,r['exact'],flush=True)


if __name__=='__main__':main()
