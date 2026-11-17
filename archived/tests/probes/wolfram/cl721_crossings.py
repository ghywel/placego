"""Inspect only pre-reported terminal transitions of CL721, without searching for a crossing."""
import json
import os
from pathlib import Path

MASK = (1 << 8192) - 1
P = 16


def wanted_rows(seed, ticks):
    result = {}
    v = seed
    for t in range(max(ticks) + 1):
        if t in ticks:
            result[t] = v
        v = ((v << 2) ^ ((v << 1) | v)) & MASK
    return result


def first(word):
    return (word & -word).bit_length()-1 if word else 8192


def main():
    os.nice(10)
    log = Path(__file__).with_name('walk_merge.out').read_text()
    cases = []
    for line in log.splitlines():
        parts = line.split()
        if parts and parts[0].startswith('0x') and 'identical' not in parts:
            seed, shift, tick = int(parts[0],16), int(parts[2]), int(parts[4])
            assert tick == int(parts[5]) and tick >= max(0, -shift)
            cases.append((seed,shift,tick))
    assert len(cases) == 18 and sum(seed == 5 for seed,_,_ in cases) == 1
    times = {tick+d for _,_,tick in cases for d in (0,1,P,P+1)}
    ref = wanted_rows(1,times)
    result = []
    for seed,shift,t in cases:
        other = wanted_rows(seed,{t+shift+d for d in (0,1,P,P+1)})
        a, a1, ap, ap1 = (ref[t+d] for d in (0,1,P,P+1))
        y, y1, yp, yp1 = (other[t+shift+d] for d in (0,1,P,P+1))
        b, b1, c, c1 = map(first,(a^ap,a1^ap1,y^yp,y1^yp1))
        j, j1, jp = map(first,(a^y,a1^y1,ap^yp))
        assert 0 < j <= b <= b1 < j1 < 8192
        assert b != c and b1 == c1 and jp >= j1
        assert (c == j if j < b else c > b)
        result.append(dict(seed=hex(seed),shift=shift,t=t,B=b,B1=b1,other_B=c,
                           J=j,J1=j1,Jp=jp,merge_decider=(a>>(j-1))&1,
                           edge_decider=(a>>(b-1))&1))
    assert all(r['merge_decider'] == 1 for r in result)
    (Path(os.environ['CAPPED_OUT'])/'crossings.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
