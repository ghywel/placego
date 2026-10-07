"""GC380 extend fixed GC378 fixtures through column13, exterior14 free.
COMMAND: python3 .../rule30_locked_cycles.py > /tmp/cycles.json
         python3 .../rule30_locked_extend.py /tmp/cycles.json
P: both fixtures extend. CF: exact next column eliminates both fixtures.
Unexpected control: look for112 as well as56 periods in the112-vertex phase graph.
"""
import json,re,sys
from pathlib import Path


def audit(cycle,U):
    states=dict(cycle['path'][:-1])
    rows={p:[p%2,U[p]]+[(states[p]>>i)&1 for i in range(11)] for p in range(56)}
    allowed={p:{e for e in(0,1) if rows[(p+1)%56][12]==(rows[p][11]^(rows[p][12]|e))}
             for p in range(56)}
    out={}
    for p in range(56):
        for e in allowed[p]:
            out[p,e]={( (p+1)%56,n) for n in allowed[(p+1)%56]
                      if any(n==(rows[p][12]^(e|f)) for f in(0,1))}
    # Independent bit-row coding audits both boundary equations on every arc.
    for p in range(56):
        expected=set()
        for e in allowed[p]:
            for n in allowed[(p+1)%56]:
                for f in (0,1):
                    row=rows[p][11] | (rows[p][12]<<1) | (e<<2) | (f<<3)
                    nxt=(row<<1) ^ (row | (row>>1))
                    if ((nxt>>1)&1)==rows[(p+1)%56][12] and ((nxt>>2)&1)==n:
                        expected.add(((p,e),((p+1)%56,n)))
        actual={(node,v) for node in out if node[0]==p for v in out[node]}
        assert expected==actual
    # Independent negative graph guard: iterative sink deletion leaves no
    # possible forever-forward path for these two fixtures.
    alive=set(out);rounds=0
    while True:
        dead={n for n in alive if not (out[n]&alive)}
        if not dead:break
        alive-=dead;rounds+=1
    cycles=[]
    for length in(56,112):
        found=None
        for e in sorted(allowed[0]):
            root=(0,e);layers=[{root:None}]
            for t in range(length):
                parents={}
                for n in sorted(layers[-1]):
                    for v in sorted(out[n]):parents.setdefault(v,n)
                layers.append(parents)
            if root not in layers[-1]:continue
            path=[root]
            for t in range(length,0,-1):path.append(layers[t][path[-1]])
            path.reverse();found=path;break
        if found is None:
            cycles.append(dict(length=length,exists=False));continue
        extended=[rows[p]+[e] for p,e in found[:-1]]
        boundary=[]
        for t,row in enumerate(extended):
            target=extended[(t+1)%length]
            good=[]
            for f in(0,1):
                src=row+[f]
                nxt=[src[x-1]^(src[x]|src[x+1]) for x in range(1,14)]
                if nxt==target[1:]:good.append(f)
            assert good;boundary.append(good[0])
        # Unexpected mutation: changing column12 must flip next column13
        # when the same exterior14 input and expected next row are kept.
        bad=extended[10].copy();bad[12]^=1;src=bad+[boundary[10]]
        assert [src[x-1]^(src[x]|src[x+1]) for x in range(1,14)]!=extended[11][1:]
        cycles.append(dict(length=length,exists=True,column13=[e for p,e in found[:-1]],
                           exterior14=boundary,scalar_replay=True,mutation_rejected=True))
    return dict(paths=cycles,forward_core_vertices=len(alive),sink_rounds=rounds,bitrow_edges_checked=True)


def main():
    fixture=json.load(open(sys.argv[1]))
    text=Path('tests/probes/lexicon/rule30_wheel_left.py').read_text()
    U=[int(c) for c in re.search(r'^U = "([01]+)"',text,re.M).group(1)]
    assert fixture['width']==12
    print(json.dumps({bit:audit(c,U) for bit,c in fixture['closed_walk_choices'].items()},indent=2))

if __name__=='__main__':main()
