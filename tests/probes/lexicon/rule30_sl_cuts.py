#!/usr/bin/env python3
"""rule30_sl_cuts.py: SLC, actual cuts inside GC1007's recurrent S/L component, and whether they break it.

RUN-ON:     cpu (Python 3, kissat 4.0.4 as KISSAT); two or three cores, minutes a round
COMMAND:    python3 tests/probes/lexicon/rule30_sl_cuts.py [ROUNDS=6] [SAMPLES=12] [NS=80] [JOBS=3]
DATA:       L578's handoff (the 771 + 832 minimal forbidden words to length 40, as GC1007 reads them); cuts are
            appended to cuts40_sl.txt in the RLK scratch (NP_SCRATCH_RLK)

Why (GPT's GC1007 and its L584 follow-up; L587). GC1007 (rule30_sl40_branch.py) spells visible codes as 1 followed
by blocks S = 001 and L = 00001 (gaps 3 and 5) and finds, under both cutoff-40 lists, a sole recurrent component of
79 states with 38 branching states. Its entropy exceeds the actual language's certified ceiling (0.1236 bits), so
actual cuts inside it must exist (GC1007 bounds their length by 41 .. 5120). L584's f has a 4-gap, so it leaves the
component unchanged (GPT, cf7b077a). This probe learns actual cuts inside the component and rebuilds it after each
round: does it lose its branching? A component with no branching state left has zero entropy.

Method (counterexample-guided, as L585's CUT). Each round samples SAMPLES distinct length-NS windows of walks inside
the live recurrent components (every state recurrent, so each window is a factor of a bi-infinite walk) and tests
each for membership in L (phase 0, SAT over the right cone, in_language_phase). Each absent window is shrunk to a
minimal forbidden word: drop its first symbol while still absent, then its last (both one-symbol deletions are then
present, factor-closure keeping the left one so). Cuts absent from L hold in both phases (L1 c L). The automaton is
rebuilt on GC1007's F plus all cuts so far. The cuts are minimal, not necessarily shortest: an exhaustive scan by
length would cost hours past length 50 (window counts 791, 2,294, 6,385, 47,436 at n = 40, 50, 60, 80).

Record searched: `record_find.py S/L cut` -> GC1007 (RECORD-MAP lines 97, 98; RULE30-GPT GC1007/GC1008) and L584
(f leaves S/L unchanged); `record_find.py "CEGAR|counterexample-guided|refinement loop"` -> GC981 (a language
quotient) and L585's CUT (records); no search for S/L cuts on record.

Instrument checks before registration (about 12:45, disclosed because they inform P1): the graph rebuilds as
GC1007's (252 states, 174 components, one recurrent: 79 states, 38 branching), and 5 random component windows at
each of n = 41, 50, 60, 80 had 0, 0, 1 and 3 absent from L (0.09 .. 1.3 s a membership call).

PREDICTIONS (Local's, pushed before any run of this script):
  SLC-C1 (control): GC1007's numbers reproduce; 20 sampled component windows of length 40 are in L and in L1.
  SLC-P1 (informed by the check above, 0.6): every round-1 cut has length between 45 and 70.
  SLC-P2 (blind, 0.55): one round does not break the component (a branching state remains after round 1).
  SLC-P3 (blind, 0.4): within ROUNDS = 6 rounds the component loses all branching.
  SLC-P4 (the unexpected check, 0.3): some cut is a factor of a single-block power, (001)^k or (00001)^k, so it
         kills a pure cycle.
"""
import os
import random
import re
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_relaxed_records_k as rlk                         # noqa: E402  (in_language_phase, DIR)
sys.argv = _argv
ROOT = os.path.dirname(os.path.dirname(HERE))
BLOCK = {'S': '001', 'L': '00001'}


def lists():
    s = Path(os.path.join(HERE, 'rule30_visible_language_handoff.md')).read_text()

    def words(section):
        return set(w for line in section.splitlines() if re.fullmatch(r'\s+[01]+(?:\s+[01]+)*\s*', line)
                   for w in line.split())
    W = words(s.split('## 3.')[1].split('## 4.')[0])
    A = words(s.split('### 4a.')[1].split('### 4b.')[0])
    D = words(s.split('### 4b.')[1].split('## 5.')[0])
    B = (W - D) | A
    assert (len(W), len(A), len(D), len(B)) == (771, 307, 246, 832)
    return W, B


def build(F):
    """GC1007's automaton: states are the longest suffix that is a proper prefix of some word in F."""
    P = {''} | {w[:k] for w in F for k in range(1, len(w))}
    cache = {}

    def step(q, b):
        if (q, b) not in cache:
            t = q + b
            if any(t.endswith(f) for f in F):
                r = None
            else:
                r = t
                while r not in P:
                    r = r[1:]
            cache[(q, b)] = r
        return cache[(q, b)]

    def advance(q, w):
        for b in w:
            q = step(q, b)
            if q is None:
                return None
        return q
    root = advance('', '1')
    nodes, seen, edges = [root], {root}, {}
    for q in nodes:
        edges[q] = {}
        for g, code in BLOCK.items():
            r = advance(q, code)
            if r is not None:
                edges[q][g] = r
                if r not in seen:
                    assert len(nodes) < 200000
                    seen.add(r)
                    nodes.append(r)
    return nodes, edges


def components(nodes, edges):
    """Strongly connected components (iterative Tarjan); returns (all components, recurrent ones)."""
    index, low, stack, active, comps, counter = {}, {}, [], set(), [], [0]
    for v0 in nodes:
        if v0 in index:
            continue
        work = [(v0, iter(edges[v0].values()))]
        index[v0] = low[v0] = counter[0]
        counter[0] += 1
        stack.append(v0)
        active.add(v0)
        while work:
            v, it = work[-1]
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter[0]
                    counter[0] += 1
                    stack.append(w)
                    active.add(w)
                    work.append((w, iter(edges[w].values())))
                    break
                elif w in active:
                    low[v] = min(low[v], index[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop()
                        active.remove(w)
                        comp.append(w)
                        if w == v:
                            break
                    comps.append(comp)
    rec = []
    for comp in comps:
        g = set(comp)
        if len(g) > 1 or any(w == comp[0] for w in edges[comp[0]].values()):
            branching = sum(sum(w in g for w in edges[v].values()) == 2 for v in g)
            rec.append((g, branching))
    return comps, rec


def windows(group, edges, n):
    """Distinct length-n factors of walks inside the component `group`."""
    out = set()
    for q in group:
        stack = [(q, '')]
        while stack:
            r, s = stack.pop()
            if len(s) >= n + 4:
                first = 3 if s.startswith('001') else 5
                for o in range(first):
                    out.add(s[o:o + n])
                continue
            for g, r2 in edges[r].items():
                if r2 in group:
                    stack.append((r2, s + BLOCK[g]))
    return out


def member(w):
    return w, rlk.in_language_phase(w, 0), rlk.in_language_phase(w, 1)


def absent0(w):
    return not rlk.in_language_phase(w, 0)


def shrink(w):
    """A minimal forbidden factor of the L-absent word w (both one-symbol deletions present)."""
    if not absent0(w):
        return None
    while len(w) > 2 and absent0(w[1:]):
        w = w[1:]
    while len(w) > 2 and absent0(w[:-1]):
        w = w[:-1]
    return w


def main():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    samples = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    ns = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    jobs = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    W, B = lists()
    F = set(W | B)
    nodes, edges = build(F)
    comps, rec = components(nodes, edges)
    print('S/L graph: %d states, %d components, recurrent %s' % (len(nodes), len(comps),
                                                                  [(len(g), b) for g, b in rec]), flush=True)
    c1 = len(comps) == 174 and [(len(g), b) for g, b in rec] == [(79, 38)]
    out = os.path.join(rlk.DIR, 'cuts40_sl.txt')
    rng = random.Random(1007)
    allcuts = []
    with Pool(jobs) as pool:
        sample = sorted(windows(rec[0][0], edges, 40))
        rng.shuffle(sample)
        ctl = pool.map(member, sample[:20])
        c1 = c1 and all(a and b for _, a, b in ctl)
        print('SLC-C1', 'PASS' if c1 else 'FAIL', '(%d windows of length 40 in the component)' % len(sample),
              flush=True)
        for rnd in range(1, rounds + 1):
            live = [(g, b) for g, b in rec if b > 0]
            if not live:
                print('round %d: no recurrent component with a branching state is left' % rnd, flush=True)
                break
            ws = set()
            for g, b in live:
                ws |= windows(g, edges, ns)
            ws = sorted(ws)
            rng.shuffle(ws)
            mins = pool.map(shrink, ws[:samples])
            found = sorted({w for w in mins if w}, key=lambda w: (len(w), w))
            print('round %d: %d windows of length %d in live components; %d of %d sampled absent; %d distinct cuts' % (
                rnd, len(ws), ns, sum(1 for w in mins if w), min(samples, len(ws)), len(found)), flush=True)
            if not found:
                print('round %d: every sampled window is in L; stopping' % rnd, flush=True)
                break
            assert not set(found) & F, 'a cut was already forbidden'
            with open(out, 'a') as f:
                f.writelines('%s round=%d n=%d\n' % (w, rnd, len(w)) for w in found)
            for w in found:
                print('  cut (length %d): %s' % (len(w), w), flush=True)
            allcuts += found
            F |= set(found)
            nodes, edges = build(F)
            comps, rec = components(nodes, edges)
            print('round %d: rebuilt with %d cuts: %d states, recurrent %s' % (
                rnd, len(allcuts), len(nodes), [(len(g), b) for g, b in rec]), flush=True)
    pure = [w for w in allcuts if w in '001' * 60 or w in '00001' * 40 or w in ('001' * 60)[1:] or w in ('001' * 60)[2:]
            or any(w in ('00001' * 40)[o:] for o in range(5))]
    print('cuts: %d, lengths %s; single-block-power cuts: %s' % (len(allcuts), sorted(len(w) for w in allcuts), pure))


if __name__ == '__main__':
    main()
