#!/usr/bin/env python3
"""L1036: the exact tree of legal pasts (left extensions) of a visible word, from the certified phase-0 list.

Local, 2026-10-27. GC1991: for w in L, d(w) = 1 + max(d(0w), d(1w)), so d(w) - 1 is the height of the tree of
legal left extensions u (uw in L). The phase-0 minimal forbidden words of lexicon/rule30_local_mfw44.txt are
complete to length 44 and each is certified absent (cake_lpr), so while |uw| <= 44 membership is decided by the
list alone. This reads that list only: no cellular-automaton evolution, solver or sampling.
Prints the tree height, the branch count at each depth, and every dead branch with the certified words that kill
both of its one-symbol extensions, plus the gaps (runs of 0 between successive 1s) of the dead branch.
Usage: left_extension_tree.py WORD ...
"""
import re
import sys
from pathlib import Path

LIST = Path(__file__).resolve().parents[1] / 'lexicon' / 'rule30_local_mfw44.txt'


def phase0_words():
    out, ph = [], None
    for line in LIST.read_text().splitlines():
        line = line.strip()
        if line.startswith('## phase'):
            ph = line.split()[2].rstrip(':')
        elif line and not line.startswith('#') and ph == '0':
            out.append(line)
    return set(out)


F = phase0_words()
M = max(map(len, F))


def killers(s):
    """Listed words that are prefixes of s (only new factors appear when a symbol is prepended)."""
    return [s[:k] for k in range(2, min(len(s), M) + 1) if s[:k] in F]


def gaps(s):
    return [len(g) for g in re.findall(r'(?<=1)0*(?=1)', s)]


def tree(w):
    assert not any(w[i:j] in F for i in range(len(w)) for j in range(i + 2, len(w) + 1)), 'w not in L'
    level, depth, counts, dead = [w], 0, [], []
    while level:
        assert len(level[0]) <= 44, 'beyond the certified length; the list no longer decides'
        counts.append(len(level))
        nxt = []
        for s in level:
            kids = [a + s for a in '01' if not killers(a + s)]
            if not kids:
                dead.append((depth, s[:len(s) - len(w)], sorted({k for a in '01' for k in killers(a + s)})))
            nxt += kids
        level, depth = nxt, depth + 1
    return depth, counts, dead


if __name__ == '__main__':
    for w in sys.argv[1:]:
        d, counts, dead = tree(w)
        print('%s: d = %d; branches by depth %s' % (w, d, counts))
        for dep, u, k in dead:
            print('  dead at depth %2d: %s|%s  gaps %s  killed by %s' % (dep, u, w, gaps(u + w), k))
