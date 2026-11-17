#!/usr/bin/env python3
"""sideways_locks_replay.py (Local, Block 8): the plain-Python replay of the essay's worked-numbers cell.
Reads the three locks from the portal source (Rule30Submission.lean, argument 1) and prints the list the notebook's first
Output cell must equal: for lock5, lock7, lock7b in turn, [windows, period, word of column 1 as a string,
failures in the two-cell model, failures with column W + 1 free at both ticks, first odd tick at which its witness's
window is in the lock]."""
import re, sys
src = open(sys.argv[1]).read()
def codes(name):
    body = src[src.index('def %sCodes' % name):]
    body = body[:body.index('\n]\n')]
    return [[int(x) for x in re.findall(r'\d+', m)] for m in re.findall(r'\[([\d,\s]+)\]', body.split(':= [', 1)[1])]
def st(e, c): return ((e << 1) | c) ^ (e | (e >> 1))
def cells(w, W): return [st(st(w | (e << W), 0), 1) & ((1 << W) - 1) for e in range(4)]
def free(w, W):
    m = (1 << W) - 1
    return [st((st(w | (a << W), 0) & m) | (b << W), 1) & m for a in (0, 1) for b in (0, 1)]
out = []
for name, W, R in (('lock5', 34, 28998), ('lock7', 30, 1891), ('lock7b', 45, 3793493)):
    C = codes(name); p = len(C); S = set(c for k in C for c in k)
    word = ''.join(str(C[k][0] & 1) for k in range(p))
    assert all(all((c & 1) == C[k][0] & 1 for c in C[k]) for k in range(p))
    fc = sum(1 for k in range(p) for c in C[k] for v in cells(c, W) if v not in C[(k + 1) % p])
    ff = sum(1 for c in S for v in free(c, W) if v not in S)
    D, t = R, 0
    while not (t % 2 == 1 and (D & ((1 << W) - 1)) in S):
        D = st(D, 1 if t % 2 == 0 else 0); t += 1
    out.append([len(S), p, word, fc, ff, t])
print(out)
