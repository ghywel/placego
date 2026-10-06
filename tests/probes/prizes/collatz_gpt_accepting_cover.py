"""G88 RC3, preregistered before running in the containing publication.
Independently validate 319 rejecting classes and five accepting singletons
for a22,t34,delta4. Require disjoint complete cover and reject a corrupted
accepting residue. Direct trajectories, position sums, first meetings.
No a23/a24 search. Certificate data outside Git; review still required.
"""
from collections import Counter
from itertools import combinations
import hashlib
import json
from pathlib import Path
from collatz_gpt_collision_tree import tree
from collatz_gpt_cover_audit import reason, extrema_by_positions


def witness(r,a,t,delta):
    x,y = r,r+delta
    starts = (x,y)
    positions = ([],[])
    counts = [0,0]
    for k in range(t):
        for side,z in enumerate((x,y)):
            if z%2:
                positions[side].append(k)
                counts[side] += 1
            assert 3**counts[side] >= 2**(k+1), 'invalid acceptance'
        x = (3*x+1)//2 if x%2 else x//2
        y = (3*y+1)//2 if y%2 else y//2
        if k+1 < t:
            assert x != y, 'early meeting'
    assert counts == [a,a] and x == y, 'invalid acceptance'
    assert starts[0].bit_length() == starts[1].bit_length(), 'width'
    offsets = [sum(3**(a-1-i)*2**p for i,p in enumerate(pp)) for pp in positions]
    assert offsets[0]-offsets[1] == delta*3**a, 'invalid acceptance'
    for n,B in zip(starts,offsets):
        assert 2**t*x == 3**a*n+B, 'affine'
    return dict(starts=starts,terminal=x,offsets=offsets,positions=positions)


def audit(cuts,accepted,a=22,t=34,delta=4):
    reasons = Counter(reason(s,r,a,t,delta) for s,r in cuts)
    witnesses = [witness(r,a,t,delta) for r in accepted]
    classes = cuts+[(t,r) for r in accepted]
    for (s,r),(q,u) in combinations(classes,2):
        assert (r-u)%2**min(s,q) != 0, 'overlap'
    assert sum(2**(t-s) for s,r in classes) == 2**t, 'coverage'
    return reasons,witnesses


def main():
    lo,hi = extrema_by_positions([],0,22)
    assert hi-lo < 8*3**22, "displacement reduction"
    cuts = []
    result = tree(22,34,4,True,cuts=cuts)
    accepted = result['witnesses']
    assert result['complete'] and len(cuts) == 319 and len(accepted) == 5
    reasons,rows = audit(cuts,accepted)
    corrupt = [accepted[0]+1]+accepted[1:]
    try:
        audit(cuts,corrupt)
    except AssertionError as exc:
        assert 'invalid acceptance' in str(exc)
    else:
        raise AssertionError('corrupted acceptance accepted')
    payload = json.dumps(dict(a=22,horizon=34,displacement=4,cuts=cuts,accepted=accepted,
                              reasons=dict(reasons),witnesses=rows,producer=result),indent=2)
    Path('/private/tmp/placego-gpt-collision-partition-a22.json').write_text(payload)
    print('RC3 PASS:',len(cuts),'rejecting classes and',len(accepted),'accepting residues cover',2**34)
    print('Independent rejection reasons:',dict(reasons))
    print('All five pairs first meet at34; corrupted accepting residue rejected')
    print('Certificate SHA256:',hashlib.sha256(payload.encode()).hexdigest())
    print('Exactly five same-count collision families at a22; second-model review pending')


if __name__ == '__main__':
    main()
