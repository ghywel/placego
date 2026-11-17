"""GC384 fixed width13 phase12/14 pairing; prediction00/11, CF mixed path.
All core two-edge paths, including bridges. No width sweep.
Independent scalar two-step control tests Boolean implication only.
"""
import json,re
from pathlib import Path
from rule30_locked_core import core
from rule30_locked_lift import lift


def main():
    U=list(map(int,re.search(r'^U = "([01]+)"',Path('tests/probes/lexicon/rule30_wheel_left.py').read_text(),re.M).group(1)))
    _,a,o=core(12,U,details=True);b,bo,_=lift(12,U,a,o)
    pairs={};middle=set()
    for n in sorted(b):
        if n[0]!=12:continue
        for v in bo[n]:
            middle.add((v[1]>>3)&1)
            for w in bo[v]:
                key=str((n[1]>>3)&1)+str((w[1]>>3)&1)
                pairs.setdefault(key,[n,v,w])
    # Independent local scalar check with fixed column4=1 twice and middle5=0.
    # Explore columns5..8 and next exterior8; no width13 graph encoder involved.
    local=set()
    for s in range(16):
        row=[1]+[(s>>i)&1 for i in range(4)]
        nxt=[1]+[row[x-1]^(row[x]|row[x+1]) for x in range(1,4)]
        if nxt[1]!=0:continue
        end=nxt[0]^(nxt[1]|nxt[2]);local.add(str(row[1])+str(end))
    assert local=={'00','10','11'}
    print(json.dumps(dict(core_vertices=len(b),phase13_bits=sorted(middle),core_pair_paths=pairs,local_scalar_pairs=sorted(local)),indent=2))

if __name__=='__main__':main()
