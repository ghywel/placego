"""GC378 fixed width12 ambiguity audit. Preregistered in CLOUD-LOCAL.md.
Prediction: two56-period strip cycles disagree at an ambiguous column5 phase.
Controls: independently replay every scalar cell; flipping one row bit must reject.
Unrestricted periodic exterior input is not a realized global right half.
"""
import json,re
from pathlib import Path
from rule30_locked_core import core


def replay(path,U,mutate=False):
    rows=[]
    for p,s in path[:-1]:
        rows.append([p%2,U[p]]+[(s>>i)&1 for i in range(11)])
    if mutate: rows[10][5]^=1
    exterior=[]
    for i,row in enumerate(rows):
        target=rows[(i+1)%56]
        good=[]
        for e in (0,1):
            src=row+[e]
            nxt=[src[x-1]^(src[x]|src[x+1]) for x in range(1,13)]
            if nxt==target[1:]:good.append(e)
        if not good:return None
        exterior.append(good[0])
    return exterior


def main():
    text=Path('tests/probes/lexicon/rule30_wheel_left.py').read_text()
    U=[int(c) for c in re.search(r'^U = "([01]+)"',text,re.M).group(1)]
    meta,alive,out=core(12,U,details=True)
    phases=[p for p in range(56) if len({(s>>3)&1 for q,s in alive if q==p})==2]
    assert len(phases)==2
    p=phases[0];cycles={}
    for root in sorted(n for n in alive if n[0]==p):
        layers=[{root:None}]
        for t in range(56):
            parents={}
            for n in sorted(layers[-1]):
                for v in sorted(out[n]):parents.setdefault(v,n)
            layers.append(parents)
        if root not in layers[-1]:continue
        path=[root]
        for t in range(56,0,-1):path.append(layers[t][path[-1]])
        path.reverse();assert path[0]==path[-1]
        ext=replay(path,U);assert ext is not None
        assert replay(path,U,mutate=True) is None
        bit=(root[1]>>3)&1
        cycles.setdefault(bit,dict(path=path,exterior=ext))
    print(json.dumps(dict(width=12,ambiguous_column5_phases=phases,
                         cycle_start_phase=p,closed_walk_choices=cycles,
                         two_distinct_cycles=len(cycles)==2),indent=2))

if __name__=='__main__':main()
