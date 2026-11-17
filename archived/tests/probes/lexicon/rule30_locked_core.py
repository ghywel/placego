"""GC373 preregistered phase-graph trimming; widths4,8, no parameter search.
P: core fixes column2 at every phase. CF: fixes columns2..4 at width4.
Controls: scalar vs bitwise; incompatible constant1; finite-path boundary guard.
A synchronous pruning round removes nodes with no surviving in- or out-neighbour.
GC374: --wide runs the separately preregistered fixed width12 extension.
Outcome:71 rounds,602 core vertices; columns2..4 fixed, column5 not fixed.
"""
import json
import re
import sys
from pathlib import Path
from rule30_locked_paths import step


def scalar(s, m, p, U, e):
    b=[p%2,U[p]]+[(s>>i)&1 for i in range(m-1)]+[e]
    c=[b[i-1] ^ int(bool(b[i] or b[i+1])) for i in range(1,m+1)]
    if c[0]!=U[(p+1)%len(U)]: return None
    return sum(c[i-1]<<(i-2) for i in range(2,m+1))


def core(m,U,details=False):
    period=len(U); size=1<<(m-1)
    nodes={(p,s) for p in range(period) for s in range(size)}
    out={n:set() for n in nodes}; inc={n:set() for n in nodes}
    for p,s in nodes:
        for e in (0,1):
            c=scalar(s,m,p,U,e)
            assert c==step(s,m,p,U[p],U[(p+1)%period],e)
            if c is not None:
                v=((p+1)%period,c); out[p,s].add(v); inc[v].add((p,s))
    alive=nodes.copy(); losses=[]
    while True:
        dead={n for n in alive if not(out[n]&alive) or not(inc[n]&alive)}
        if not dead:break
        losses.append(len(dead)); alive-=dead
    forced={}
    if alive:
        for x in range(2,m+1):
            vals=[{(s>>(x-2))&1 for p,s in alive if p==t} for t in range(period)]
            if all(len(v)==1 for v in vals):forced[x]=''.join(str(next(iter(v))) for v in vals)
    # Unexpected check: a finite path of 2r edges with the observation at its centre
    # survives r simultaneous trimming rounds, including paths whose ends later die.
    r=len(losses); survivors=nodes.copy()
    for radius in range(1,r+1):
        prev=survivors
        survivors={n for n in prev if out[n]&prev and inc[n]&prev}
    assert survivors==alive
    # Forward/backward finite-path projection at centre r for every start phase;
    # independent traversal, shared graph edges (not an independent encoder).
    N=2*r+1
    for start in range(period):
        forward=[set(range(size))]
        for t in range(N-1):
            phase=(start+t)%period
            forward.append({v[1] for s in forward[-1] for v in out[phase,s]})
        viable=forward[-1]
        for t in range(N-2,r-1,-1):
            phase=(start+t)%period
            viable={s for s in forward[t] if any(v[1] in viable for v in out[phase,s])}
        centre=(start+r)%period
        assert {(centre,s) for s in viable}=={n for n in alive if n[0]==centre}
    result = dict(width=m,period=period,rounds=r,remaining=len(alive),losses=losses,
                forced_columns=forced,centre_path_check=True)
    if details: return result, alive, {n: out[n]&alive for n in alive}
    return result


def main():
    text=Path('tests/probes/lexicon/rule30_wheel_left.py').read_text()
    U=[int(c) for c in re.search(r'^U = "([01]+)"',text,re.M).group(1)]
    results=[core(m,U) for m in ((12,) if "--wide" in sys.argv else (4,8))]
    # Period2 encodes the wall phase even for a constant companion.
    neg=core(4,[1,1]); assert neg['remaining']==0
    print(json.dumps(dict(wheel=results,constant1_negative=neg),indent=2))

if __name__=='__main__': main()
