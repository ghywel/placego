"""GC382 exact core lift. NOT YET RUN at publication.
Prediction: column5 remains ambiguous in the width13 core.
Counterfactual: one coupled column removes all column5 ambiguity.
Fixed run: base width12 core, at most1204 lifted vertices, no wider census.
Independent control: direct width5 enumeration against width4 lift.
Unexpected check: compare edges as well as nodes; vertex agreement alone is weak.
COMMAND: python3 tests/probes/lexicon/rule30_locked_lift.py
"""
import json,re
from pathlib import Path
from rule30_locked_core import core,scalar


def lift(m,U,alive,out):
    # State bit m-1 is the new column m+1 bit.
    nodes={(p,s|(e<<(m-1))) for p,s in alive for e in (0,1)}
    edges={n:set() for n in nodes};inc={n:set() for n in nodes}
    for p,z in nodes:
        s=z&((1<<(m-1))-1);e=z>>(m-1)
        target=scalar(s,m,p,U,e)
        if target is None or ((p+1)%len(U),target) not in out[p,s]:continue
        last=(s>>(m-2))&1
        for f in (0,1):
            n=last^(e|f);v=((p+1)%len(U),target|(n<<(m-1)))
            edges[p,z].add(v);inc[v].add((p,z))
    kept=nodes.copy();rounds=0
    while True:
        dead={n for n in kept if not(edges[n]&kept) or not(inc[n]&kept)}
        if not dead:break
        kept-=dead;rounds+=1
    return kept,{n:edges[n]&kept for n in kept},rounds


def main():
    U=list(map(int,re.search(r'^U = "([01]+)"',Path('tests/probes/lexicon/rule30_wheel_left.py').read_text(),re.M).group(1)))
    _,a,o=core(4,U,details=True);b,bo,_=lift(4,U,a,o)
    _,direct,do=core(5,U,details=True)
    assert b==direct and bo==do
    # Literal scalar evaluation at the wider width checks each retained arc.
    meta,a,o=core(12,U,details=True);b,bo,r=lift(12,U,a,o)
    for p,z in b:
        targets={((p+1)%56,v) for f in (0,1) if (v:=scalar(z,13,p,U,f)) is not None}
        assert bo[p,z]==targets&b
    forced={}
    for x in range(2,14):
        sets=[{(z>>(x-2))&1 for p,z in b if p==t} for t in range(56)]
        if all(len(s)==1 for s in sets):forced[x]=''.join(str(next(iter(s))) for s in sets)
    print(json.dumps(dict(base_vertices=len(a),candidate_vertices=2*len(a),width=13,remaining=len(b),rounds=r,forced_columns=forced,direct_width5_control=True,all_retained_scalar_edges=True),indent=2))

if __name__=='__main__':main()
