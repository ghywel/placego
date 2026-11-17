#!/usr/bin/env python3
"""B223 / MI428: finite LEFT projection of the unchanged MI419 selector.

RUN-ON: cpu, Python standard library. No claim about repaired complements.
COMMAND: python3 tests/probes/instinct/ss3_small_left_selector.py OUTDIR
Predictions/counterfactual/controls/caps were frozen in MI428 before this run.
Full raw profiles and summary are written outside git. A cap is PARTIAL.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time

START = time.monotonic()
MAX_SECONDS, MAX_PROFILES, MAX_COMBINATIONS = 120, 20000, 20000000
COUNTS = dict(screened=0, profiles=0, literal_combinations=0, spectra=0,
              tail_checks=0, failures=0, missing_values=0)
CACHE = {}
SELECTED = {}


def guard():
    if time.monotonic()-START > MAX_SECONDS:
        raise TimeoutError('120-second cap')
    if COUNTS['profiles'] > MAX_PROFILES:
        raise TimeoutError('20000-profile cap')
    if COUNTS['literal_combinations'] > MAX_COMBINATIONS:
        raise TimeoutError('20-million-combination cap')


def L(m):
    return m*(m-1)//2


def staircase(r, H):
    k = (math.isqrt(8*H+1)-1)//2
    t = H-k*(k+1)//2
    p = r-k
    return list(range(p))+[p+1+2*i+(i >= k-t) for i in range(k)], p, k, t


def select(r, h, q):
    key = (r,h,q)
    if key in SELECTED:
        return SELECTED[key]
    walk = list(range(r))
    previous_g = None
    previous = None
    for H in range(h+min(q,r)+1):
        R,p,k,t = staircase(r,H)
        assert R == walk, ('independent rank walk', key,H,R,walk)
        ell = sum(v < q for v in R)
        g = H-ell
        if previous_g is not None:
            assert g-previous_g in (1,2)
        if g >= h:
            if g == h:
                mode,base = 'hit',p
            else:
                assert g == h+1 and previous_g == h-1
                R,base = previous
                R = R.copy()
                if q != base:
                    assert base-1 in R and base not in R
                    R[R.index(base-1)] = base
                    mode = 'skip-prefix'
                else:
                    R[-1] += 1
                    mode = 'skip-maximum'
            U = tuple(v+(v >= q) for v in R)
            assert len(U) == len(set(U)) == r and q not in U
            assert tuple(sorted(U)) == U and sum(U) == L(r)+r+h
            assert sum(R)-L(r)-sum(v < q for v in R) == h
            result = dict(U=U,base=base,mode=mode,H=H)
            SELECTED[key] = result
            return result
        previous_g = g
        previous = (R,p)
        # Independent construction: grow one indicated Ferrers row.
        walk[r-1-t] += 1
    raise AssertionError(('no crossing',key))


def spectra(U, a):
    key = (U,a)
    if key in CACHE:
        return CACHE[key]
    r = len(U)
    dp = [1]+[0]*r
    used = 0
    for v in U:
        used += 1
        for j in range(used,0,-1):
            dp[j] |= dp[j-1] << v
    total = sum(U)
    maps = [{v for v in range(total+1) if (bits >> v)&1} for bits in dp]
    count = math.comb(r,a)
    if COUNTS['literal_combinations']+count > MAX_COMBINATIONS:
        raise TimeoutError('20-million-combination cap before spectrum')
    literal = {sum(C) for C in itertools.combinations(U,a)}
    COUNTS['literal_combinations'] += count
    assert literal == maps[a], ('full spectrum mismatch',U,a)
    assert {total-v for v in literal} == maps[r-a], ('complement',U,a)
    COUNTS['spectra'] += 1
    CACHE[key] = (maps[a],maps[r-a])
    return CACHE[key]


def run(out):
    groups = {}
    controls = set()
    forecast_counterexample = None
    with (out/'profiles.jsonl').open('w') as stream:
        for r in range(6,17):
            for a in range(3,r-2):
                b = r-a
                for h in range(a*b-1):
                    for q in range(1,2*r):
                        guard()
                        COUNTS['screened'] += 1
                        selected = select(r,h,q)
                        if selected['base'] >= 5:
                            continue
                        COUNTS['profiles'] += 1
                        guard()
                        U = selected['U']
                        actual,comp = spectra(U,a)
                        lower,upper = L(a)+a+h+1,L(a)+a+a*b-1
                        missing = sorted(set(range(lower,upper+1))-actual)
                        comp_missing = set(range(L(b)+b+h+1,L(b)+b+a*b))-comp
                        assert {sum(U)-v for v in missing} == comp_missing
                        if q == 2*r-1:
                            for offset in (11,101):
                                assert select(r,h,q+offset)['U'] == U
                                COUNTS['tail_checks'] += 1
                        row = dict(r=r,a=a,b=b,h=h,q=q,tail=(q==2*r-1),
                                   **selected,band=[lower,upper],missing=missing)
                        stream.write(json.dumps(row,separators=(',',':'))+'\n')
                        if missing:
                            COUNTS['failures'] += 1
                            COUNTS['missing_values'] += len(missing)
                            group = f"r{r}:{selected['mode']}:min{min(a,b)}"
                            groups[group] = groups.get(group,0)+1
                            if min(a,b) >= 4 and forecast_counterexample is None:
                                forecast_counterexample = row
                        if (r,a,q,h) in ((6,3,1,5),(6,3,1,7)):
                            target = 13 if h == 5 else 14
                            assert target in missing, ('known negative vanished',row)
                            controls.add((h,target))
    assert controls == {(5,13),(7,14)}
    return dict(status='COMPLETE',counts=COUNTS,failures_by_group=groups,
                forecast='REFUTED' if forecast_counterexample else 'SURVIVED_FINITE_DOMAIN',
                first_forecast_counterexample=forecast_counterexample,
                known_negative_controls=sorted(controls))


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True,exist_ok=False)
    try:
        result = run(out)
    except TimeoutError as exc:
        result = dict(status='PARTIAL',reason=str(exc),counts=COUNTS)
    except Exception as exc:
        result = dict(status='FAIL',reason=repr(exc),counts=COUNTS)
        (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
        raise
    result['seconds'] = time.monotonic()-START
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['raw_sha256'] = hashlib.sha256((out/'profiles.jsonl').read_bytes()).hexdigest()
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
