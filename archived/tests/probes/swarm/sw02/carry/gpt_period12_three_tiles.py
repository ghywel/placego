#!/usr/bin/env python3
"""Literal three-symbol34-cell code on the existing period12 return graph.

This also completes the originally intended full1632 kit local checks.
No new graph search, period, width or long orbit is enumerated.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import re


def main():
    source=(Path(os.environ['PARITY_KIT'])/'lean/Ruliology/CellularAutomata/Rule30MovingWaves.lean').read_bytes()
    assert hashlib.sha256(source).hexdigest()=='0ab24513cc18e4225e2b17bd0358a2776d387b8b21a32ff0bdb6945142bc72f3'
    kit=[]
    for name in ('zeroProfiles','oneProfiles'):
        kit.append([int(s) for s in re.search(r'def '+name+r' : List Nat :=\s*\[([^]]+)\]',source.decode())[1].split(',')])
    data=json.loads(Path(os.environ['PERIOD12_GRAPH']).read_text())
    branches=sorted(tuple(v) for v in data['summary']['branch_states'])
    routes={}
    for row in data['returns']:
        s=branches.index(tuple(row['start']));t=branches.index(tuple(row['end']))
        routes[s,int(s!=t)]=[tuple(v) for v in row['path']]
    tiles=[]
    for word in ((0,1,1),(1,0,1),(1,1,0)):
        branch=0;path=[]
        for bit in word:
            path.extend(routes[branch,bit][:-1]);branch^=bit
        assert branch==0 and len(path)==34
        tiles.append([v[0] for v in path][::-1])
    assert all(tile in tiles for tile in kit)
    def failures(library):
        bad=0;checks=0
        for a,b in itertools.product(library,repeat=2):
            both=a+b
            for i,t in itertools.product(range(34),range(12)):
                x,y,z=[(both[i+j]>>t)&1 for j in range(3)]
                want=(30>>(4*x+2*y+z))&1
                bad += want!=((both[i]>>((t+1)%12))&1);checks+=1
        return checks,bad
    assert failures(kit)==(1632,0)
    assert failures(tiles)==(3672,0)
    words=[[p&1 for p in tile] for tile in tiles]
    assert len({tuple(w) for w in words})==3
    decoder=next((i,j) for i in range(34) for j in range(i+1,34)
                 if len({(w[i],w[j]) for w in words})==3)
    mutant=[tile.copy() for tile in tiles];mutant[1][7]^=1
    assert failures(mutant)[1]>0
    result={'events':[[0,1,1],[1,0,1],[1,1,0]],'profiles':tiles,
            'initial_words':[''.join(map(str,w)) for w in words],
            'decoder_offsets':decoder,'decoder_values':[(w[decoder[0]],w[decoder[1]]) for w in words],
            'kit_tile_indices':[tiles.index(tile) for tile in kit],
            'kit_checks':failures(kit),'three_tile_checks':failures(tiles),
            'mutant_failures':failures(mutant)[1]}
    (Path(os.environ['CAPPED_OUT'])/'three-tiles.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    print('PERIOD12_THREE_TILES_PASS',flush=True)


if __name__=='__main__':main()
