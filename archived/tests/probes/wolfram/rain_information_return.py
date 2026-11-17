#!/usr/bin/env python3
"""GC2027: fixed follow-up, scalar audit and fate of the eight-step information return."""
import hashlib,json,os
from pathlib import Path
TRUTH=(0,1,1,1,1,0,0,0)
TMAX=12
LO,HI=-12,20


def evolve(row):return [TRUTH[4*row[j-1]+2*row[j]+row[j+1]] for j in range(1,len(row)-1)]


def main():
    # Full scalar replay of all nine causally relevant exterior bits, for each a.
    return_values={a:set() for a in (0,1)}
    for a in (0,1):
        for code in range(512):
            row=[a,0,1,0,1,0,1,0]+[(code>>j)&1 for j in range(9)]
            for _ in range(8):row=evolve(row)
            assert len(row)==1
            return_values[a].add(row[0])
    assert return_values=={0:{0},1:{1}}
    # Fix the entire left half-line to rain through x=7 (white); all relevant right bits are free.
    # The finite left buffer is wider than the queried cones, so there is no clamped evolution.
    pairs=[set() for _ in range(TMAX+1)]
    witnesses={};examples={};rows_checked=0
    for code in range(1<<13):
        row=[int(i%2==0) for i in range(LO,8)]+[(code>>j)&1 for j in range(13)]
        traces=[]
        for t in range(TMAX+1):
            pair=(row[7-(LO+t)],row[8-(LO+t)])
            pairs[t].add(pair);witnesses.setdefault((t,pair),code);traces.append(pair)
            if t<TMAX:row=evolve(row)
        rows_checked+=1
        if len(examples)<12 and traces[8]!=(0,1):examples[str(code)]=traces
    result={'status':'PASS','return_values':{a:sorted(v) for a,v in return_values.items()},
            'scalar_prefix_cases':1024,'half_line_cases':rows_checked,
            'pair_values_at_x7_x8':[sorted(v) for v in pairs],
            'witnesses':{str(t)+':'+''.join(map(str,p)):c for (t,p),c in witnesses.items()},
            'unlocked_at_eight_examples':examples,
            'first_uniform_lock':next((t for t,s in enumerate(pairs) if s=={(0,1)}),None),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witnesses','unlocked_at_eight_examples')}))

if __name__=='__main__':main()
