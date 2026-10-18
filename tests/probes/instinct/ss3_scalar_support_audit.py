#!/usr/bin/env python3
"""MI431 / B225: bounded audit of MI422 and MI426 scalar support.
Run: python3 tests/probes/instinct/ss3_scalar_support_audit.py OUTDIR
Predictions, counterfactuals, controls, and caps frozen in MI431.
This is a supporting finite check, not an infinite theorem or parent census.
"""
import hashlib
import json
import math
from pathlib import Path
import sys
import time

START = time.monotonic()
COUNTS = dict(pools=0, subsets=0, complete_spectra=0, band_calls=0, band_values=0)
FAMILIES = {}
CACHE = {}
STREAM = None


def L(m): return m*(m-1)//2


def guard():
    if time.monotonic()-START > 30:
        raise TimeoutError('30-second cap')


def pool(m,H,kind):
    k=(math.isqrt(8*H+1)-1)//2
    t=H-k*(k+1)//2
    if kind=='Q' and t:
        k+=1
        p=m-k
        high=[p+1+2*i-(i>=t) for i in range(k)]
    else:
        p=m-k
        high=[p+1+2*i+(i>=k-t) for i in range(k)]
    return tuple(range(p))+tuple(high),p


def spectra(U):
    U=tuple(U)
    if U in CACHE: return CACHE[U]
    guard()
    m=len(U)
    assert tuple(sorted(set(U)))==U and min(U)>=0
    N=1<<m
    if COUNTS['subsets']+N>20000000:
        raise TimeoutError('20-million-subset cap')
    # Literal mask enumeration: each subset is evaluated exactly once.
    sums=[0]*N
    cards=[0]*N
    literal=[set() for _ in range(m+1)]
    literal[0].add(0)
    for mask in range(1,N):
        bit=mask & -mask
        previous=mask^bit
        cards[mask]=cards[previous]+1
        sums[mask]=sums[previous]+U[bit.bit_length()-1]
        literal[cards[mask]].add(sums[mask])
    # Separate polynomial/cardinality bitset calculation.
    dp=[1]+[0]*m
    for i,v in enumerate(U):
        for c in range(i+1,0,-1): dp[c] |= dp[c-1]<<v
    total=sum(U)
    for c in range(m+1):
        packed={x for x in range(total+1) if (dp[c]>>x)&1}
        assert packed==literal[c],('full spectrum mismatch',U,c)
        assert {total-x for x in literal[c]}==literal[m-c],('complement',U,c)
    COUNTS['pools']+=1
    COUNTS['subsets']+=N
    COUNTS['complete_spectra']+=m+1
    STREAM.write(json.dumps(dict(U=U,spectra=[sorted(x) for x in literal]),separators=(',',':'))+'\n')
    CACHE[U]=literal
    return literal


def check(family,m,a,U,total,lo,hi,parameters):
    guard()
    if lo>hi: return
    assert len(U)==m and sum(U)==total,(family,'moment',parameters,U)
    missing=sorted(set(range(lo,hi+1))-spectra(U)[a])
    COUNTS['band_calls']+=1
    COUNTS['band_values']+=hi-lo+1
    FAMILIES[family]=FAMILIES.get(family,0)+1
    if missing:
        raise ValueError(dict(family=family,m=m,a=a,U=U,band=[lo,hi],missing=missing,parameters=parameters))


def run():
    for h,U,target in ((5,(0,2,3,5,7,9),13),(7,(0,2,3,5,8,10),14)):
        assert target not in spectra(U)[3],('known negative disappeared',h)
    assert 5 not in {l+t for l in (0,1,3,4) for t in (0,3,6)}
    for m in range(6,13):
        for p in range(5,m):
            k=m-p
            for i in range(k+1):
                for j in range(i,k+1):
                    e=[0]*i+[1]*(j-i)+[2]*(k-j)
                    U=tuple(range(p))+tuple(p+1+2*v+e[v] for v in range(k))
                    A=k*(k+1)//2+sum(e)
                    if A<m: continue
                    for a in range(3,m-2):
                        b=m-a
                        check('first',m,a,U,L(m)+A,L(a)+A-b+1,L(a)+a+a*b-1,dict(p=p,e=e))
        for H in range(1,m*m+1):
            P,p=pool(m,H,'P')
            Q,w=pool(m,H,'Q')
            for a in range(3,m-2):
                b=m-a
                if w>=3 and H<a*b:
                    highs=Q[w:]
                    for cut in range(len(highs)+1):
                        U=Q[:w]+tuple(v+(i>=cut) for i,v in enumerate(highs))
                        D=len(highs)-cut
                        check('second',m,a,U,L(m)+H+D,L(a)+H+D,L(a)+a*b,dict(H=H,cut=cut))
                if p>=5:
                    for q in range(1,p):
                        if H<q: continue
                        U=tuple(v+(v>=q) for v in P)
                        A=H+m-q
                        check('punctured-P',m,a,U,L(m)+A,L(a)+A-b+1,L(a)+a+a*b-1,dict(H=H,q=q))
                if w>=4:
                    for q in range(1,w):
                        U=tuple(v+(v>=q) for v in Q)
                        A=H+m-q
                        check('punctured-Q',m,a,U,L(m)+A,L(a)+A,L(a)+a*b,dict(H=H,q=q))
    return dict(status='COMPLETE_PASS',counts=COUNTS,families=FAMILIES,
                controls='two known q1 negatives, span-sharpness, full spectra and complements PASS')


def main():
    global STREAM
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    with (out/'spectra.jsonl').open('w') as STREAM:
        try: result=run()
        except TimeoutError as exc:
            result=dict(status='PARTIAL',reason=str(exc),counts=COUNTS,families=FAMILIES)
        except Exception as exc:
            result=dict(status='FAIL',reason=repr(exc),counts=COUNTS,families=FAMILIES)
    result['seconds']=time.monotonic()-START
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['spectra_sha256']=hashlib.sha256((out/'spectra.jsonl').read_bytes()).hexdigest()
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
