#!/usr/bin/env python3
"""GC2941 stage 2: exact prefix moments, guarded centroid approximation, ternary tags."""
from gpt_fejer_pair_energy import starts, branches, D
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def v3(x):
    x = abs(int(x))
    if not x:
        return -1
    a=0
    while x % 3 == 0:
        a+=1;x//=3
    return a


def prefix_data(ell):
    # DP exact moments, independently compared with the literal prefix list.
    moments={0:(1,0,0)}
    words=[(0,0)]
    for depth in range(ell):
        nxt=defaultdict(lambda:[0,0,0])
        for s,(c,m,q) in moments.items():
            for bit,t in branches(s):
                z=bit*(1<<depth)
                nxt[t][0]+=c;nxt[t][1]+=3*m+z*c
                nxt[t][2]+=9*q+6*z*m+z*z*c
        moments={s:tuple(v) for s,v in nxt.items()}
        words=[(t,3*b+bit*(1<<depth)) for s,b in words for bit,t in branches(s)]
    oracle=defaultdict(lambda:[0,0,0])
    for s,b in words:
        oracle[s][0]+=1;oracle[s][1]+=b;oracle[s][2]+=b*b
        assert 2*b < 3**ell
    assert moments == {s:tuple(v) for s,v in oracle.items()}
    return moments,words


def main():
    summaries=[];p3=[];p4=[];rows=[]
    for w in [16,18,20,22]:
        n=1<<w;r=np.array(starts(0,w),dtype=np.int64);a=len(r)
        f=np.zeros(n,dtype=np.float64);f[r]=1
        spectrum=np.fft.rfft(f);del f
        def coeff(inds):
            inds=np.asarray(inds,dtype=np.int64)%n
            out=spectrum[np.minimum(inds,n-inds)].copy()
            # numpy FFT uses a negative sign, whereas G here uses exp(+2pi i x).
            mask=inds<=n//2
            out[mask]=np.conj(out[mask])
            return out
        hs=np.arange(1,2048,dtype=np.int64)
        gs=coeff(hs)
        tags=defaultdict(list)
        for h,z in zip(hs,gs):
            h=int(h);aa=(h & -h).bit_length()-1;u=h>>aa;m=w-aa
            exact3=v3(u);minus=v3(u-(1<<m));plus=v3(u+(1<<m))
            score=max(exact3,minus,plus)
            value=float(abs(z)**2/a/(1.5**aa))
            tags[score].append(value)
            rows.append({'w':w,'h':h,'v2':aa,'v3':exact3,'v3_minus':minus,'v3_plus':plus,
                         'A_gamma2':float(abs(z)**2/a),'valuation_adjusted':value})
        low=[v for k,vs in tags.items() if k<=1 for v in vs]
        high=[v for k,vs in tags.items() if k>=4 for v in vs]
        ratio=float(np.mean(high)/np.mean(low))
        if w in [20,22]:p4.append(ratio>=2)
        byscore={k:{'n':len(v),'mean':float(np.mean(v)),'max':float(max(v))} for k,v in sorted(tags.items())}
        summaries.append({'w':w,'A':a,'resonance_tags':byscore,'high_to_low_mean':ratio,
                          'mod3_counts':dict(Counter((r%3).tolist()))})
        if w not in [20,22]:continue
        for ell in ([7,9,10] if w==20 else [9,11,12]):
            H=8;hh=np.arange(1,H,dtype=np.int64);weights=2*(1-hh/H)
            moments,words=prefix_data(ell);k=w-ell
            transforms={}
            for s in moments:
                rr=np.array(starts(s,k),dtype=np.int64)
                transforms[s]=np.exp(2j*np.pi*np.outer(hh,rr)/(1<<k)).sum(axis=1)
            exact=np.zeros(len(hh),dtype=complex);centroid=exact.copy();unphased=exact.copy()
            variance_sum=Fraction(0)
            for s,(c,m,q) in moments.items():
                mean=Fraction(m,c);var=Fraction(q,c)-mean*mean
                centroid += c*np.exp(-2j*np.pi*hh*float(mean)/n)*transforms[s]
                unphased += c*transforms[s]
                variance_sum += c*var*len(starts(s,k))
            for s,b in words:
                exact += np.exp(-2j*np.pi*hh*b/n)*transforms[s]
            original=coeff((pow(3,ell,n)*hh)%n)
            assert np.max(np.abs(exact-original))/a < 2e-10
            def norm(v):return float(np.sqrt(weights @ (np.abs(v/a)**2)))
            actual_norm=norm(original);approx_norm=norm(centroid)
            error=norm(original-centroid)
            bound=(2*math.pi**2*float(variance_sum)/a/n**2)*math.sqrt(H*(H*H-1)*(2*H*H-3)/30)
            assert error <= bound+1e-10
            guard=H*3**ell/n
            selected=(w,ell) in [(20,9),(22,11)]
            relative=abs(approx_norm-actual_norm)/actual_norm
            if selected:p3.append(relative<=.2)
            summaries.append({'w':w,'ell':ell,'H':H,'phase_guard':guard,
                'normalized_original_energy':actual_norm**2*a/H,
                'normalized_centroid_energy':approx_norm**2*a/H,
                'normalized_unphased_energy':norm(unphased)**2*a/H,
                'actual_sqrt_energy_error':error,'certifying_formula_bound':bound,
                'sqrt_energy_relative_error':relative,'P3_selected':selected,
                'moments':{s:list(v) for s,v in moments.items()}})
        del spectrum,r
    print(json.dumps({'status':'PASS','P3_centroid20percent':p3,'P4_ternary_tags':p4,
        'summaries':summaries,'coefficients':rows,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))


if __name__ == '__main__':main()
