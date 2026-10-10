#!/usr/bin/env python3
"""GC1004: first phase-language obstruction, a single finite right cone.
Predictions in RULE30-GPT.md. No SAT, records or growth sweep.
"""
import itertools
TRUTH = (0,1,1,1,1,0,0,0)

def step(q, n, wall):
    return (((q << 1) | wall) ^ (q | (q >> 1))) & ((1 << (n-1))-1)

def literal(q, n, wall):
    bits = [wall]+[(q >> i) & 1 for i in range(n)]
    return sum(TRUTH[4*bits[i]+2*bits[i+1]+bits[i+2]] << i for i in range(n-1))

for n in range(2,8):
    for q in range(1 << n):
        for wall in (0,1):
            assert step(q,n,wall) == literal(q,n,wall)
print('Literal/packed transition controls PASS')

def prefixes(word):
    n = 2*len(word)-1
    count = 0
    starts = set()
    for initial in range(1 << n):
        q = initial
        for t in range(n):
            if t % 2 == 0 and (q & 1) != int(word[t//2]):
                break
            if t == n-1:
                count += 1
                starts.add(''.join(str(initial >> i & 1) for i in range(3)))
            else:
                q = step(q,n-t,t % 2)
    return count, sorted(starts)

for word in ('101010000','10101000'):
    print(word, prefixes(word))

# Exact black-prehistory image: an output prefix consumes one extra source
# bit; every live pair has arbitrary infinite source continuation.
def black_parent(prefix):
    states = {(1,0),(1,1)}
    for bit in prefix:
        states = {(b,c) for a,b in states for c in (0,1)
                  if TRUTH[4*a+2*b+c] == int(bit)}
    return bool(states)

for k in range(1,7):
    images = {''.join(str(step(q,k+1,1) >> i & 1) for i in range(k))
              for q in range(1 << (k+1))}
    for bits in itertools.product('01',repeat=k):
        w = ''.join(bits)
        assert black_parent(w) == (w in images)
print('Predecessor automaton/literal prefix controls PASS')

word = '101010000'
models = []
for initial in range(1 << 17):
    q = initial
    for t in range(17):
        if t % 2 == 0 and (q & 1) != int(word[t//2]):
            break
        if t == 16:
            models.append(''.join(str(initial >> i & 1) for i in range(17)))
        else:
            q = step(q,17-t,t % 2)
common = ''.join(next(iter(s)) if len(s := {w[i] for w in models}) == 1 else '?'
                 for i in range(17))
print('Common spatial bits', common)
for k in range(1,18):
    patterns = {w[:k] for w in models}
    if not any(black_parent(w) for w in patterns):
        print('All prefixes lack black prehistory first at', k, 'patterns', sorted(patterns))
        break
else:
    print('Finite-prefix prehistory prediction REFUTED')
assert len(models) == 512 and common == '10010001?????????'
# Counting all 2^9 tails proves the entire prefix cylinder, not just examples.
assert all(w.startswith('10010001') for w in models)
assert not black_parent('10010')
short_parent = None
for initial in range(1 << 15):
    q = initial
    for t in range(15):
        if t % 2 == 0 and (q & 1) != int('10101000'[t//2]):
            break
        if t == 14:
            row = ''.join(str(initial >> i & 1) for i in range(15))
            if black_parent(row):
                short_parent = row
        else:
            q = step(q,15-t,t % 2)
    if short_parent is not None:
        break
assert short_parent is not None
print('Terminal sample essential: shorter trace has black-reachable row', short_parent)
