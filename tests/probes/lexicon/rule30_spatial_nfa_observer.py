#!/usr/bin/env python3
"""GC999 exact spatial NFA image observer. Predictions: RULE30-GPT.md.
Retains infinite exterior; productive trim and strong bisimulation only.
Budget: 10 seconds, 3000 reachable image states. No SAT or width census.
"""
import itertools
import time

END = time.monotonic() + 10
CAP = 3000
TRUTH = (0, 1, 1, 1, 1, 0, 0, 0)

def check():
    if time.monotonic() > END:
        raise RuntimeError('10-second cap')

def reduce(rows, roots):
    # Remove vertices with no infinite path, then unreachable vertices.
    live = set(range(len(rows)))
    while True:
        check()
        keep = {q for q in live if (rows[q][0] | rows[q][1]) & live}
        if keep == live:
            break
        live = keep
    roots = set(roots) & live
    seen = set(roots)
    todo = list(roots)
    for q in todo:
        for r in (rows[q][0] | rows[q][1]) & live:
            if r not in seen:
                seen.add(r)
                todo.append(r)
    if not roots:
        return [], set()
    # All productive vertices accept. Strong bisimulation is safe for
    # nondeterministic languages; this is not DFA minimization.
    part = {q: 0 for q in seen}
    while True:
        check()
        ids = {}
        new = {}
        for q in sorted(seen):
            key = (part[q], tuple(frozenset(part[r] for r in edge & seen)
                                  for edge in rows[q]))
            new[q] = ids.setdefault(key, len(ids))
        if new == part:
            break
        part = new
    out = [None] * len(set(part.values()))
    for q in seen:
        out[part[q]] = tuple({part[r] for r in edge & seen} for edge in rows[q])
    return out, {part[q] for q in roots}

def observe(nfa, bit):
    rows, roots = nfa
    edge = set().union(*(rows[q][bit] for q in roots)) if roots else set()
    root = (edge, set()) if bit == 0 else (set(), edge)
    return reduce(rows + [root], {len(rows)})

def image(nfa, wall):
    rows, roots = nfa
    states = []
    ids = {}
    def add(s):
        if s not in ids:
            if len(states) >= CAP:
                raise RuntimeError('3000 reachable image-state cap')
            ids[s] = len(states)
            states.append(s)
        return ids[s]
    initial = {add((wall, b, r)) for q in roots for b in (0, 1) for r in rows[q][b]}
    out = []
    for a, b, q in states:
        check()
        edges = (set(), set())
        for c in (0, 1):
            for r in rows[q][c]:
                edges[TRUTH[4*a + 2*b + c]].add(add((b, c, r)))
        out.append(edges)
    return reduce(out, initial)

def accepts(nfa, word):
    rows, qs = nfa
    for b in word:
        qs = set().union(*(rows[q][b] for q in qs)) if qs else set()
    return bool(qs)

FULL = ([({0}, {0})], {0})
for src in (FULL, observe(FULL, 0)):
    for wall in (0, 1):
        im = image(src, wall)
        for n in range(1, 5):
            literal = set()
            for w in itertools.product((0, 1), repeat=n+1):
                if accepts(src, w):
                    literal.add(tuple(TRUTH[4*(wall if i == 0 else w[i-1])+2*w[i]+w[i+1]] for i in range(n)))
            assert literal == {w for w in itertools.product((0, 1), repeat=n) if accepts(im, w)}
# Unexpected check: finite dead branches cannot realize infinite rows.
assert reduce([(set(), {1}), (set(), set())], {0}) == ([], set())
assert reduce([({0}, {1}), (set(), set())], {0}) == ([({0}, set())], {0})
assert not observe(image(image(observe(FULL, 1), 0), 1), 1)[1]
print('Literal images, forbidden11 and dead-branch controls PASS', flush=True)
for word in ('100010100001010001', '101000100001010001'):
    nfa = FULL
    sizes = []
    try:
        for i, b in enumerate(word):
            nfa = observe(nfa, int(b))
            if not nfa[1]:
                print('REJECT', word, 'at', i+1, 'sizes', sizes, flush=True)
                break
            if i+1 < len(word):
                nfa = image(image(nfa, 0), 1)
            sizes.append(len(nfa[0]))
        else:
            print('ACCEPT', word, 'sizes', sizes, flush=True)
    except RuntimeError as e:
        print('STOP', word, 'completed', len(sizes), 'sizes', sizes, str(e), flush=True)
        break
