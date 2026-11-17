#!/usr/bin/env python3
"""Read a gap DFA (lift --dfa-from) against a block list, exactly, at all word lengths.

conforms: every word of the language is a factor of a concatenation of the blocks. Checked on the product of the DFA with
the factor automaton of the blocks, so a word outside would be found at any length.
sep: for excursions a, b and the loop l, the n <= NMAX with a l^n b in the language.
free: whether separations chain freely: a l^n b l^m c is in the language for all listed n, m.
Usage: blocks.py FILE LOOP EXCURSION [EXCURSION ...]
"""
import sys
path, loop, *exc = sys.argv[1:]
T = {}
size = {}
for line in open(path):
    p = line.split()
    s = int(p[0]); size[s] = int(p[1]); T[s] = {}
    for x in p[2:]:
        g, t = x.split(':'); T[s][int(g)] = int(t)
def run(s, w):
    for ch in w:
        s = T[s].get(int(ch))
        if s is None: return None
    return s
blocks = [loop] + exc
# factor automaton: a position is (block index, offset); from the end of a block, any block may start
pos = [(b, o) for b in range(len(blocks)) for o in range(len(blocks[b]))]
def nxt(S, ch):
    out = set()
    for b, o in S:
        if blocks[b][o] != ch: continue
        if o + 1 < len(blocks[b]): out.add((b, o + 1))
        else: out.update((c, 0) for c in range(len(blocks)))
    return frozenset(out)
start = (0, frozenset(pos))
seen = {start}; todo = [(start, '')]; bad = []
while todo and len(bad) < 5:
    (s, S), w = todo.pop()
    for g, t in T[s].items():
        S2 = nxt(S, str(g))
        if not S2: bad.append(w + str(g)); continue
        k = (t, S2)
        if k not in seen: seen.add(k); todo.append((k, w + str(g)))
print(path.split('/')[-1], 'states', len(T), 'product', len(seen), 'conforms' if not bad else 'NOT: ' + str(bad[:3]))
NMAX = 400
seps = {}
for a in exc:
    for b in exc:
        ns = [n for n in range(NMAX + 1) if run(0, a + loop * n + b) is not None]
        seps[(a, b)] = ns
        gaps = [x for x in range(ns[0], NMAX + 1) if x not in ns] if ns else []
        print('  sep', a, b, 'count', len(ns), 'least', ns[:12], 'absent above least', gaps[:12])
print('  loop alone reaches', max(n for n in range(NMAX + 1) if run(0, loop * n) is not None))
e0 = exc[0]; ns = seps[(e0, e0)][:8]
ok = sum(run(0, e0 + loop * n + e0 + loop * m + e0) is not None for n in ns for m in ns)
print('  chains %s l^n %s l^m %s: %d of %d for n, m in %s' % (e0, e0, e0, ok, len(ns) ** 2, ns))
