#!/usr/bin/env python3
"""GC2941: bounded exact ancestry/ternary controls and floating energy comparisons."""
from gpt_fejer_pair_energy import starts
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def val3(x):
    assert x
    a=0
    while x%3==0:a+=1;x//=3
    return a


def main():
    counts=defaultdict(int); measured=[]; wrong_prefix=0
    for w in range(1,11):
        N=1<<w;R=3**w
        residues=starts(0,w);A=len(residues)
        words=[];bs=[];ks=[]
        for r in residues:
            z=r;B=0;word=[]
            for i in range(w):
                b=z%2;word.append(b);B=3*B+b*(1<<i);z=(3*z+b)//2
            assert R*r+B==N*z and 0<=B<R/2 and 0<=z<R
            assert z==(B*pow(N,-1,R))%R
            words.append(tuple(word));bs.append(B);ks.append(z)
            counts['literal_transport']+=1
            for n in range(w+1):
                Bv=0
                for i,b in enumerate(word[w-n:]):Bv=3*Bv+b*(1<<i)
                assert z%(3**n)==Bv*pow(1<<n,-1,3**n)%(3**n)
                counts['suffix_congruences']+=1
        assert len(set(ks))==A
        if w<=8:
            for i in range(A):
                for j in range(i):
                    trailing=0
                    while trailing<w and words[i][w-1-trailing]==words[j][w-1-trailing]:trailing+=1
                    assert val3(bs[i]-bs[j])==trailing
                    leading=0
                    while leading<w and words[i][leading]==words[j][leading]:leading+=1
                    wrong_prefix+=int(val3(bs[i]-bs[j])!=leading)
                    counts['exact_pair_valuations']+=1
        if w<=6:
            mark=np.zeros(N,dtype=np.int64);mark[list(residues)]=1
            sums=np.concatenate(([0],np.cumsum(np.tile(mark,2))))
            for L in range(1,N+1):
                rr=(L-1).bit_length()
                assert int(max(sums[x+L]-sums[x] for x in range(N)))<=len(starts(0,rr))
                counts['all_circular_intervals']+=N
        rs=np.asarray(residues,dtype=np.float64);kk=np.asarray(ks,dtype=np.float64)
        for H in [2,4,8,16,32]:
            if H>N:continue
            hh=np.arange(1,H);weights=2*(1-hh/H)
            z=np.exp(2j*np.pi*np.outer(hh,rs)/N)
            zz=np.exp(2j*np.pi*np.outer(hh,kk)/R)
            g=z.sum(axis=1)/A;gg=zz.sum(axis=1)/A
            norm=lambda x:float(np.sqrt(weights@(np.abs(x)**2)))
            err=norm(g-gg);bound=math.pi/N*math.sqrt(H*(H*H-1)/6)
            assert err<=bound+1e-10
            for ell in range(w+1):
                q=3**ell
                if q>H:break
                n=w-ell;classes=defaultdict(list)
                for i,word in enumerate(words):classes[word[ell:]].append(i)
                D=sum(len(v)**2+float(weights@(np.abs(z[:,v].sum(axis=1))**2)) for v in classes.values())/A**2
                cap=(H+math.pi**2*q*q/(3*H))/A
                assert D<=cap+1e-10
                counts['same_suffix_energy']+=1
                for inds in classes.values():
                    base=inds[0];seen=set()
                    for idx in inds:
                        d=int(residues[idx])-int(residues[base])
                        Bu=0;Bu0=0
                        for t,b in enumerate(words[idx][:ell]):Bu=3*Bu+b*(1<<t)
                        for t,b in enumerate(words[base][:ell]):Bu0=3*Bu0+b*(1<<t)
                        value=q*d+Bu-Bu0
                        assert value%N==0
                        k=(value//N)%q
                        assert k not in seen;seen.add(k)
                        counts['distinct_grid_slots']+=1
            measured.append({'w':w,'H':H,'sqrt_energy_error':err,'formula_bound':bound})
    assert wrong_prefix>0
    print(json.dumps({'status':'PASS','counts':dict(counts),'wrong_prefix_failures':wrong_prefix,
        'measurements':measured,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':main()
