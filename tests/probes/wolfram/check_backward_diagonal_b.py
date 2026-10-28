#!/usr/bin/env python3
"""GC2017: independent Local-ray reconstruction and retained-view consistency.

Fixed 38-step scope; imports the earlier Local ray implementation, not the new
B constructor. Also finds a finite child word forcing the failed cell.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import sys
from root_past_tails import rays

TRUTH = (0, 1, 1, 1, 1, 0, 0, 0)


def main():
    folder = Path(sys.argv[1])
    data = json.loads((folder/'view.json').read_text())
    result = json.loads((folder/'result.json').read_text())
    assert result['first_impossible_depth'] == 38
    buf = {name:base64.b64decode(data[name]) for name in ('a','b')}
    def at(name,t,x):
        i = x-data['x0']
        assert 0 <= i < data['w'] and data['t0'] <= t < data['t0']+data['h']
        return (buf[name][(t-data['t0'])*data['stride']+i//8] >> (7-i%8)) & 1

    # A separate ray generator, with only the short left window needed to decide
    # the 38 requested cells. Each symbolic ray extends to infinity.
    def cell(r,i):
        win,tail = r
        return win[i] if i<=0 else tail[(i-1)%len(tail)]
    levels = []
    live = [({i:int(i==0) for i in range(-40,1)},(0,))]
    for d in range(1,39):
        nxt=[]; count=0
        for child in live:
            for tail in rays(child[1]):
                win={}
                for i in range(0,-41,-1):
                    c = win[i+1] if i+1<=0 else tail[i%len(tail)]
                    r = win[i+2] if i+2<=0 else tail[(i+1)%len(tail)]
                    # Left-permutivity: test both choices against the truth table.
                    win[i] = next(l for l in (0,1) if TRUTH[4*l+2*c+r]==cell(child,i+1))
                parent=(win,tail);count+=1
                for i in range(-39,1+3*len(tail)):
                    assert cell(child,i)==TRUTH[4*cell(parent,i-1)+2*cell(parent,i)+cell(parent,i+1)]
                if win[-d]==1-d%2:nxt.append(parent)
        levels.append({'depth':d,'parents_examined':count,'survivors':len(nxt)})
        assert levels[-1]==result['levels'][d-1]
        live=nxt
    assert not live

    equations=0
    for name in ('a','b'):
        for t in range(data['t0'],data['t0']+data['h']-1):
            for x in range(data['x0']+1,data['x0']+data['w']-1):
                assert at(name,t+1,x)==TRUTH[4*at(name,t,x-1)+2*at(name,t,x)+at(name,t,x+1)]
                equations+=1
    assert all(at('b',-d,-d)==1-d%2 for d in range(38))
    assert at('b',-38,-38)==0
    assert all(at('a',-d,-d)==1 for d in range(513))
    assert all(at('a',0,x)==int(x==0)==at('b',0,x) for x in range(data['x0'],data['x0']+data['w']))

    forcing=None
    for length in range(1,257):
        word=[at('b',-37,x) for x in range(-37,-37+length)]
        left=[]
        for c,r in ((0,0),(0,1),(1,0),(1,1)):
            for b in reversed(word):
                l=next(l for l in (0,1) if TRUTH[4*l+2*c+r]==b)
                c,r=l,c
            left.append(c)
        if left==[0,0,0,0]:
            forcing={'child_time':-37,'child_x0':-37,'length':length,
                     'word':''.join(map(str,word)),'parent_cell':[-38,-38],
                     'outputs_for_all_four_far_pairs':left}
            break
    assert forcing is not None
    packet={'independent_levels':levels,'display_equations_checked':equations,
            'finite_forcing_certificate':forcing,
            'view_sha256':hashlib.sha256((folder/'view.json').read_bytes()).hexdigest()}
    (Path(os.environ['CAPPED_OUT'])/'verified.json').write_text(json.dumps(packet,indent=2)+'\n')
    print(json.dumps({'equations':equations,'forcing':forcing}))


if __name__=='__main__':main()
