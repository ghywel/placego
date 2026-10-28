#!/usr/bin/env python3
"""GC2026: exact finite-cone completion versus ternary knowledge, W<=8,T<=8.
No sampled exteriors: bitsets enumerate all 2^16 right completions for each word.
Left of a+t is provably undetermined by left permutivity and is not simulated.
"""
import hashlib,json,os
from pathlib import Path
TMAX=8
TRUTH=(0,1,1,1,1,0,0,0)
checks=0


def ternary(l,c,r):
    if l is None:return None
    if c==1 or r==1:return l^1
    if c==0 and r==0:return l
    return None


def variable(j,n):
    block=1<<j
    raw=bytearray((1<<n)//8)
    # Bit j of the completion index, with bit 0 as the first free cell.
    for a in range(1<<n):
        if (a>>j)&1:raw[a//8]|=1<<(a%8)
    return int.from_bytes(raw,'little')


def main():
    global checks
    n=2*TMAX;full=(1<<(1<<n))-1
    variables=[variable(j,n) for j in range(n)]
    summary=[];first_gap=None;heals=[];right_extension=[];all_failures=[]
    cases=0
    for w in range(1,9):
        rowstats=[{'time':t,'exact_known':0,'ternary_known':0,'missed':0,'cases_with_gap':0} for t in range(1,TMAX+1)]
        for code in range(1<<w):
            bits=[(code>>i)&1 for i in range(w)]
            exact=[full if b else 0 for b in bits]+variables
            approx=bits+[None]*n
            prev_exact={i:bits[i] for i in range(w)}
            scalar_control=w<=3 and code in (0,1,(1<<w)-1)
            for t in range(1,TMAX+1):
                exact=[exact[j-1]^(exact[j]|exact[j+1]) for j in range(1,len(exact)-1)]
                approx=[ternary(approx[j-1],approx[j],approx[j+1]) for j in range(1,len(approx)-1)]
                known={t+j:int(v==full) for j,v in enumerate(exact) if v in (0,full)}
                aknown={t+j:v for j,v in enumerate(approx) if v is not None}
                assert all(known.get(i)==v for i,v in aknown.items())
                gap=sorted(set(known)-set(aknown));q=rowstats[t-1]
                q['exact_known']+=len(known);q['ternary_known']+=len(aknown);q['missed']+=len(gap);q['cases_with_gap']+=bool(gap)
                if gap and first_gap is None:
                    first_gap={'word':''.join(map(str,bits)),'width':w,'time':t,'position':gap[0],'forced':known[gap[0]]}
                for i in known:
                    if i>=w:right_extension.append({'word':bits,'time':t,'position':i})
                    if t>1 and i not in prev_exact and len(heals)<20:
                        heals.append({'word':''.join(map(str,bits)),'time':t,'position':i,'forced':known[i]})
                # Scalar truth-table controls over every short right completion, independent update syntax.
                if scalar_control and t<=3:
                    for a in range(1<<(2*t)):
                        s=bits+[(a>>j)&1 for j in range(2*t)]
                        for _ in range(t):s=[TRUTH[4*s[j-1]+2*s[j]+s[j+1]] for j in range(1,len(s)-1)]
                        for j,v in enumerate(s):
                            assert ((exact[j]>>a)&1)==v;checks+=1
                prev_exact=known
            cases+=1
        summary.append({'width':w,'levels':rowstats})
    # Small hand controls, without assuming the predicted outputs in the general enumeration.
    for a in (0,1):
        vals=[]
        for r in (0,1):
            for s in (0,1):
                z=[a,1,0,r,s]
                for _ in range(2):z=[TRUTH[4*z[i-1]+2*z[i]+z[i+1]] for i in range(1,len(z)-1)]
                vals.append(z[0])
        assert vals==[a]*4
    result={'status':'PASS','cases':cases,'right_variables':n,'first_gap':first_gap,'healing_examples':heals,
            'right_extension_examples':right_extension,'scalar_controls':checks,'summary':summary,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('summary','healing_examples')}))

if __name__=='__main__':main()
