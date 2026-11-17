#!/usr/bin/env python3
"""GC2941: signed pair, valuation and odd-dilation controls; no search enlargement."""
import os
for name in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']:
    os.environ[name] = '1'
from collections import Counter
from functools import lru_cache
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
import time
import numpy as np


def greedy(count):
    c = Fraction(1)
    ds, cs = [], []
    for _ in range(count):
        cs.append(c)
        b = int(c > Fraction(2, 3))
        ds.append(b)
        c = 3*c/2-b
    return ds, cs


D, SLACK = greedy(64)


def branches(s):
    return [(D[s], s+1)] + ([(0, 0)] if D[s] else [])


@lru_cache(None)
def starts(s, w):
    if not w:
        return (0,)
    n = 1 << w
    inv3 = pow(3, -1, n)
    return tuple(((2*r-b)*inv3) % n for b, t in branches(s) for r in starts(t, w-1))


def direct(n, s, w):
    c = SLACK[s]
    for _ in range(w):
        b = n & 1
        c = min(Fraction(1), 3*c/2-b)
        if c <= 0:
            return False
        n = (3*n+b)//2
    return True


@lru_cache(None)
def centered(s, t, w):
    n = 1 << w
    x, y = starts(s, w), starts(t, w)
    p = Counter((a-b) % n for a in x for b in y)
    return tuple(n*p[d]-len(x)*len(y) for d in range(n))


def exact_checks():
    cases, direct_cases, signed_cases = 0, 0, 0
    for w in range(1, 9):
        n = 1 << w
        for s in range(5):
            assert len(starts(s,w)) == len(set(starts(s,w)))
            assert set(starts(s,w)) == {a for a in range(n) if direct(a,s,w)}
            direct_cases += n
            for t in range(5):
                a = {b:len(starts(u,w-1)) for b,u in branches(s)}
                b = {c:len(starts(v,w-1)) for c,v in branches(t)}
                bias = (a.get(0,0)-a.get(1,0))*(b.get(0,0)-b.get(1,0))
                z = centered(s,t,w)
                for d in range(n):
                    rhs = (1 if d % 2 == 0 else -1)*bias
                    for x,u in branches(s):
                        for y,v in branches(t):
                            delta = x-y
                            if (d-delta) % 2 == 0:
                                rhs += 2*centered(u,v,w-1)[((3*d+delta)//2) % (n//2)]
                    assert z[d] == rhs
                    cases += 1
        # Polynomial form of the signed-boundary odd-frequency identity.
        boundary = np.zeros(n,dtype=np.int64)
        for r in starts(0,w-1):
            x, s = r, 0
            for _ in range(w-1):
                b = x & 1
                s = s+1 if b == D[s] else 0
                x = (3*x+b)//2
            if D[s] == 0:
                boundary[r] = 1 if x % 2 == 0 else -1
        indicator = np.zeros(n,dtype=np.int64)
        indicator[list(starts(0,w))] = 1
        assert np.array_equal(indicator[:n//2]-indicator[n//2:],boundary[:n//2])
        signed_cases += n//2
    return {'centered_pair_entries':cases,'direct_state_starts':direct_cases,
            'signed_boundary_coefficients':signed_cases}


def main():
    began = time.monotonic()
    controls = exact_checks()
    rng = random.Random(2941)
    records = []
    p1, p2_hits, p2_n = True, 0, 0
    for w in [8, 12, 16, 20, 22]:
        n = 1 << w
        r = np.array(starts(0,w),dtype=np.int64)
        a = len(r)
        f = np.zeros(n,dtype=np.float64)
        f[r] = 1
        spectrum = np.fft.rfft(f)
        power = (spectrum.real*spectrum.real+spectrum.imag*spectrum.imag)/(a*a)
        del spectrum, f
        total = power[0]+power[-1]+2*power[1:-1].sum()
        assert abs(total-n/a) <= 1e-9*(n/a)
        powers = [pow(3,ell,n) for ell in range(256)]
        random_odd = [2*rng.randrange(n//2)+1 for _ in range(64)]
        for j in [2,4,6,8,10]:
            H = 1 << (j+1)
            if H > n:
                continue
            hs = np.arange(1,H,dtype=np.int64)
            weights = 2*(1-hs/H)
            def energy(b):
                inds = (b*hs) % n
                inds = np.minimum(inds,n-inds)
                return float(weights @ power[inds])
            counts = Counter((r % (n//H)).tolist())
            C = sum(v*v for v in counts.values())
            mean = Fraction(H,a)-Fraction(C,a*a)
            physical = energy(1)
            pow_e = np.array([energy(b) for b in powers])
            rand_e = np.array([energy(b) for b in random_odd])
            assert abs(physical-energy(n-1)) < 1e-12
            if w == 8:
                observed = sum(energy(b) for b in range(1,n,2))/(n//2)
                assert abs(observed-float(mean)) < 1e-11
                # The complete powers-of-three cycle equals the odd average.
                assert abs(float(pow_e[:n//4].mean())-observed) < 1e-11
            if w >= 16:
                p1 = p1 and physical <= 3*H/a
                p2_hits += physical <= float(np.median(rand_e))
                p2_n += 1
            row={'w':w,'j':j,'H':H,'A':a,'physical_excess':physical,
                 'normalized_physical':physical*a/H,
                 'exact_odd_mean':[mean.numerator,mean.denominator],
                 'normalized_odd_mean':float(mean)*a/H,
                 'random64_median_normalized':float(np.median(rand_e))*a/H,
                 'powers256_mean_normalized':float(pow_e.mean())*a/H,
                 'powers256_max_normalized':float(pow_e.max())*a/H,
                 'powers256_max_at':int(pow_e.argmax()),
                 'powers256_min_normalized':float(pow_e.min())*a/H,
                 'powers256_first16_mean_normalized':float(pow_e[:16].mean())*a/H,
                 'random64_values_normalized':(rand_e*a/H).tolist(),
                 'powers256_values_normalized':(pow_e*a/H).tolist()}
            records.append(row)
        # Exact odd shell: one unmatched child for each boundary parent.
        boundary_count = 0
        for x in starts(0,w-1):
            s=0
            for _ in range(w-1):
                bit=x&1;s=s+1 if bit == D[s] else 0;x=(3*x+bit)//2
            boundary_count += D[s] == 0
        observed_odd = float(power[1:n//2:2].mean())
        assert abs(observed_odd-boundary_count/(a*a)) < 1e-11
        print(json.dumps({'checkpoint_w':w,'A':a,'odd_shell_A_times_mean':boundary_count/a}),flush=True)
        del power, r
    print(json.dumps({'status':'PASS','controls':controls,'prediction_P1':bool(p1),
       'prediction_P2':{'hits':int(p2_hits),'cases':p2_n,'held':bool(p2_hits*3>=p2_n*2)},
       'seed':2941,'records':records,'wall_s':time.monotonic()-began,
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))


if __name__ == '__main__':
    main()
