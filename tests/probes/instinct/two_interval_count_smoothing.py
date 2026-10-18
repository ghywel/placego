#!/usr/bin/env python3
"""B193 / MI379: fixed P,Q=3..6 positive count-row diagnostic.

Prediction: combined scalar rank bounds and total exactly describe the
sum of the two three-bin partition maps. Counterfactual: retain every
missing target in this fixed domain; no larger run. Independent row
controls: literal disjoint subsets versus sequential assignment DP.
Unexpected control: a zero-count row destroys the proposed smoothing.
Cap: 400 ordered row pairs, 10 CPU seconds, no retry. Raw JSON on stdout.
"""
import itertools as it
import json
import time

START = time.process_time()

def budget():
    if time.process_time() - START > 10:
        raise RuntimeError('B193 ten-CPU-second cap; incomplete, no retry')

def L(n):
    return n*(n-1)//2

def literal(n):
    out = {}
    values = tuple(range(n))
    for a in range(n+1):
        for A in it.combinations(values, a):
            left = tuple(x for x in values if x not in A)
            for b in range(n-a+1):
                key = (a,b,n-a-b)
                sums = out.setdefault(key,set())
                for B in it.combinations(left,b):
                    sums.add((sum(A),sum(B),L(n)-sum(A)-sum(B)))
        budget()
    return out

def assignment_dp(n):
    states = {(0,0,0,0)}
    for x in range(n):
        nxt = set()
        for a,b,s,t in states:
            nxt.add((a+1,b,s+x,t))
            nxt.add((a,b+1,s,t+x))
            nxt.add((a,b,s,t))
        states = nxt
        budget()
    out = {}
    for a,b,s,t in states:
        out.setdefault((a,b,n-a-b),set()).add((s,t,L(n)-s-t))
    return out

def combined(A,B):
    return {tuple(x+y for x,y in zip(a,b)) for a in A for b in B}

def rank_region(P,Q,l,k):
    low = tuple(L(a)+L(b) for a,b in zip(l,k))
    high = tuple(a*(P-1)-L(a)+b*(Q-1)-L(b) for a,b in zip(l,k))
    total = L(P)+L(Q)
    return {(x,y,total-x-y) for x in range(low[0],high[0]+1)
            for y in range(low[1],high[1]+1)
            if low[2] <= total-x-y <= high[2]}

def main():
    maps = {}
    for n in (1,3,4,5,6,7,8):
        maps[n] = literal(n)
        assert maps[n] == assignment_dp(n), ('row-map disagreement',n)
    neg = (3,4,14)
    assert neg in rank_region(7,1,(1,3,3),(1,0,0))
    assert neg not in combined(maps[7][(1,3,3)],maps[1][(1,0,0)])
    controls = [(8,4,(2,3,3),(0,2,2),(8,13,13)),
                (5,5,(1,2,2),(1,2,2),(4,3,13)),
                (5,5,(1,2,2),(1,2,2),(4,13,3)),
                (4,5,(1,1,2),(1,2,2),(2,3,11))]
    for P,Q,l,k,target in controls:
        assert target in combined(maps[P][l],maps[Q][k])
    count = 0
    targets = 0
    failures = []
    for P in range(3,7):
        for Q in range(3,7):
            for l in sorted(x for x in maps[P] if min(x)>0):
                for k in sorted(x for x in maps[Q] if min(x)>0):
                    actual = combined(maps[P][l],maps[Q][k])
                    expected = rank_region(P,Q,l,k)
                    assert actual <= expected
                    offsets = tuple(a*(P-1)+b*(Q-1) for a,b in zip(l,k))
                    assert actual == {tuple(z-x for z,x in zip(offsets,t)) for t in actual}
                    missing = sorted(expected-actual)
                    if missing:
                        failures.append({'P':P,'Q':Q,'low_counts':l,'high_counts':k,
                                         'missing':missing})
                    count += 1
                    targets += len(expected)
                    budget()
    assert count == 400
    print(json.dumps({'status':'COMPLETE','row_maps_independently_equal':[1,3,4,5,6,7,8],
                      'positive_controls':len(controls),'zero_count_negative_control':'PASS',
                      'row_pairs':count,'rank_targets':targets,'failures':failures,
                      'cpu_seconds':time.process_time()-START},sort_keys=True))

if __name__ == '__main__':
    main()
