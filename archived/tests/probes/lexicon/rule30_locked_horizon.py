"""GC381 fixed-fixture finite horizon. Prediction max14/15 arcs, not15/16.
No assertion about alternative width12 paths or globally realized right halves.
"""
import json,re,sys
from pathlib import Path


def horizon(c,U):
    states=dict(c['path'][:-1])
    rows={p:[p%2,U[p]]+[(states[p]>>i)&1 for i in range(11)] for p in range(56)}
    allowed={p:{e for e in (0,1) if rows[(p+1)%56][12]==(rows[p][11]^(rows[p][12]|e))} for p in rows}
    out={(p,e):{((p+1)%56,n) for n in allowed[(p+1)%56] if any(n==(rows[p][12]^(e|f)) for f in (0,1))} for p in rows for e in allowed[p]}
    rank={}; layers=[]
    while len(rank)<len(out):
        layer={n for n in out if n not in rank and all(v in rank for v in out[n])}
        assert layer,'Cycle prevents a finite horizon certificate'
        for n in layer:rank[n]=1+max((rank[v] for v in out[n]),default=0)
        layers.append(layer)
    root=max(rank,key=rank.get);path=[root]
    while out[path[-1]]:path.append(max(out[path[-1]],key=rank.get))
    assert len(path)==rank[root]
    # Independently replay the entire selected finite strip, including the wall.
    ext=[]
    for (p,e),(q,n) in zip(path,path[1:]):
        src=rows[p]+[e];target=rows[q]+[n]
        choices=[f for f in (0,1) if [src[x-1]^(src[x]|(src+[f])[x+1]) for x in range(1,14)]==target[1:]]
        assert choices;ext.append(choices[0])
    # A physical finite segment may end with an unconstrained terminal bit:
    # no column12 update is imposed at that last row. Add this endpoint explicitly.
    p,e=path[-1];q=(p+1)%56;f=0;n=rows[p][12]^(e|f)
    src=rows[p]+[e,f];target=rows[q]+[n]
    assert [src[x-1]^(src[x]|src[x+1]) for x in range(1,14)]==target[1:]
    assert n not in allowed[q], 'A permitted terminal bit would contradict maximality'
    # Unexpected all-phase check: a global maximum need not start at phase0.
    by_phase={p:max((rank[p,e]-1 for e in allowed[p]),default=-1) for p in range(56)}
    return dict(max_arcs=len(path)-1,start_phase=root[0],phase0_arcs=by_phase[0],all_phase_arcs=by_phase,path=path,exterior14=ext,scalar_replay=True,finite_segment_arcs=len(path),terminal_bit=n,terminal_phase=q)


def main():
    fixture=json.load(open(sys.argv[1]))
    U=list(map(int,re.search(r'^U = "([01]+)"',Path('tests/probes/lexicon/rule30_wheel_left.py').read_text(),re.M).group(1)))
    result={b:horizon(c,U) for b,c in fixture['closed_walk_choices'].items()}
    assert [result[b]['max_arcs'] for b in ('0','1')]==[14,15]
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
