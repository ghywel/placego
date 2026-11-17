#!/usr/bin/env python3
"""GC2036: inverse tree of ONE target, compared to retained GC2034 supports."""
import hashlib,json,os,sys
from pathlib import Path
TRUTH=(0,1,1,1,1,0,0,0)
def pred(w):
    out=[]
    for u,v in ((0,0),(0,1),(1,0),(1,1)):
        a=[0]*len(w)+[u,v]
        for i in reversed(range(len(w))):a[i]=int(w[i])^(a[i+1]|a[i+2])
        assert ''.join(str(TRUTH[4*l+2*c+r]) for l,c,r in zip(a,a[1:],a[2:]))==w
        out.append(''.join(map(str,a)))
    return out
r=json.loads(Path(sys.argv[1]).read_text());cap=next(c for c in r['cases'] if c['name']=='black_cap')
words=['00010'];levels=[];checks=0
for t in reversed(range(9)):
    support=cap['levels'][t]['support'];minimum=None;projections={}
    for k in range(1,min(8,len(words[0]))+1):
        past={w[:k] for w in words};actual={w[:k] for w in support}
        overlap=past&actual
        projections[str(k)]={'past_count':len(past),'actual_count':len(actual),'intersection':len(overlap)}
        if not overlap:
            minimum=k;break
    levels.append({'t':t,'ancestors':len(words),'length':len(words[0]),'minimum_cut_prefix':minimum,
                   'counts':projections,'projected_ancestors':sorted({w[:minimum] for w in words}) if minimum else [],
                   'allowed_prefixes':sorted({w[:minimum] for w in support}) if minimum else []})
    if t:words=[v for w in words for v in pred(w)];checks+=len(words)
assert not any(w.startswith('01111110') for w in words)
out={'status':'PASS','levels':levels,'literal_inverse_checks':checks,'retained_result_sha256':hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(out,indent=2)+'\n')
for l in levels:print(l)
print('PASS',checks,'literal inverse checks')
