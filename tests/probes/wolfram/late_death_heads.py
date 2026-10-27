#!/usr/bin/env python3
"""L1042: the start-only heads that end every decidable late death, from the certified phase-0 list.

Local, 2026-10-27. For each word w of L of length 6..12 whose legal-past tree stays within the certified length 44
(lexicon/rule30_local_mfw44.txt; see left_extension_tree.py), compute d(w). For each late death (d >= 17), take every
deepest legal past u+w and its shortest prefix h with d(h) = 1 (both one-symbol pasts certified absent): the
terminal head. Reads the list only: no cellular-automaton evolution, solver or sampling.
"""
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import left_extension_tree as T

F, M = T.F, T.M


def legal(s):
    return not any(s[i:j] in F for i in range(len(s)) for j in range(i + 2, min(len(s), i + M) + 1))


def gaps(s):
    return tuple(len(g) for g in re.findall(r'(?<=1)0*(?=1)', s))


def death(w):
    level, d = [w], 0
    while True:
        if len(level[0]) > 44:
            return None, None
        nxt = [a + s for s in level for a in '01' if not T.killers(a + s)]
        if not nxt:
            return d + 1, level
        level, d = nxt, d + 1


words = {0: ['']}
for n in range(1, 13):
    words[n] = [w + a for w in words[n - 1] for a in '01' if not any((w + a)[i:] in F for i in range(len(w) + 1))]
heads, late, undecided = collections.Counter(), [], 0
for n in range(6, 13):
    for w in words[n]:
        d, deep = death(w)
        if d is None:
            undecided += 1
            continue
        if d < 17:
            continue
        late.append((d, w))
        for s in deep:
            heads[next(s[:k] for k in range(1, len(s) + 1) if not legal('0' + s[:k]) and not legal('1' + s[:k]))] += 1
print('late deaths (d >= 17), lengths 6..12:', len(late), '; words beyond the certified range:', undecided)
print('death times:', sorted(collections.Counter(d for d, _ in late).items()))
for h, c in heads.most_common():
    print('terminal head', h, 'gaps', gaps(h), 'deepest pasts', c)
assert set(heads) == {'001000010001', '100010001000100010001001'}
