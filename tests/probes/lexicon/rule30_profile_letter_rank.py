#!/usr/bin/env python3
"""One bounded additive termination-rank test on the exact word update.

RUN-ON: cpu, standard-library Python; no solver or record census.
COMMAND: python3 tests/probes/lexicon/rule30_profile_letter_rank.py

Record searched: potential|rank|weight|invariant with dihedral|growing.word|
pair.word|carry.permut ->2 old inverse-transducer hits; letter.weight|
symbol.weight|additive.rank|termination.rank with profile|word|origin|pair
->no hit, including active ledgers. GC1205/06's count failures and the
new GC1208 exact closed word update read. This tests a termination rank
on its letters, not an event count or an information-price model.

PREDICTIONS before execution (2026-10-13):
 A1: iterate the actual125/phase1 word only from a0 to a9, with the
     retained finite-band horizon. Count vectors at a0/4/5/9 match
     independently extracted physical paths; each five-step difference
     sums to5. The named blocks0->5 and4->9 close the basic no11/no00000
     DFA at Z2 andZ1, respectively (registered from stored visible bits).
 A2 blind(.5): some coefficients c0,c1 in0..3, not both0, give a
     componentwise nonnegative combination of these two differences.
     If so, it is an exact obstruction to any strictly decreasing rank
     with nonnegative letter weights plus arbitrary basic-DFA potential.
     If not, this tiny coefficient check is inconclusive: no larger
     block, sample, coefficient sweep or fitted rank follows.
 A3 blind(.5): the same two endpoint pairs also have identical residuals
     for RLK's fixed phase1 certified-cut set (44allp1 plus cuts40).
     Refutation limits the obstruction to the basic DFA; no extra
     cuts, re-solving or membership test follows.
 Independent: transducer versus physical path; Counter versus explicit
     indicator sums; streaming residual versus direct longest suffix.
 Unexpected scope check: even coincident DFA states do not make a full
     hidden-state cycle: the word is five letters longer. Any obstruction
     concerns only this additive rank, not a repeatable physical orbit.
 Counterfactual: the four invertible carry actions alone force a rank
     decrease; the increasing word carries the remaining information.

OUTCOME: A1 passes. A2 REFUTED: the two count changes are(5,-1,-1,2)
and(0,-2,1,6), whose10 coordinate is negative in every nonzero
nonnegative combination, not merely coefficients0..3. The rank class
is not refuted. A3 NOT_RUN: the registered phase1 base list is absent
on this host. Initial loaderNone caused TypeError; corrected to report
missing data and finish unaffected controls. No substitute or sweep.
SECOND-PARTY OUTCOME (Local L695 at94b11d82, M5): the unchanged probe
executes A3 with its registered1226-word list. A3 REFUTED: both endpoint
closures False. A1/A2 independently match. No additional sample or run.
"""
import json
from collections import Counter
from itertools import product
from pathlib import Path
import rule30_relaxed_records_k as rlk
from rule30_triangle_profile_transducer import advance, physical
from rule30_zero_triangle_guard_transport import literal, packed


def counts(word):
    counter = Counter(c + 2*b for c, b in word)
    out = tuple(counter[j] for j in range(4))
    assert out == tuple(sum(c + 2*b == j for c, b in word) for j in range(4))
    return out


def residuals(code, forbidden):
    prefixes = {''} | {f[:j] for f in forbidden for j in range(1, len(f))}
    state, states = '', []
    for i, bit in enumerate(code):
        candidate = state + bit
        assert not any(candidate.endswith(f) for f in forbidden)
        state = max((s for s in prefixes if candidate.endswith(s)), key=len)
        direct = max((s for s in prefixes if code[:i+1].endswith(s)), key=len)
        assert state == direct
        states.append(state)
    return states


def main():
    root = Path(__file__).resolve().parents[3]
    f = next(r for r in json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
             if r['depth'] == 125 and r['phase'] == 1)
    seed = {j: int(b) for j, b in enumerate(f['left'], 1)}
    rows = packed(seed, 1, 144, 290)
    assert rows == literal(seed, 1, 144, 290)
    words = [physical(rows, 1, 125, 0, 1)]
    for a in range(9):
        assert 126 + 2*a + 3 <= 145
        words.append(advance(words[-1], 1))
        assert words[-1][-1] == (1, 1)
    for a in (0, 4, 5, 9):
        assert words[a] == physical(rows, 1, 125, a, 1)
    code = f['visible'][:72]      # through the last named endpoint, white143
    basic = residuals(code, ('11', '00000'))
    base = rlk.load_forbidden('44allp1')
    forbidden = (base + rlk.load_cuts(1, 40)) if base is not None else None
    full = residuals(code, forbidden) if forbidden is not None else None
    changes, full_closed = [], []
    for a, b in ((0, 5), (4, 9)):
        before, after = counts(words[a]), counts(words[b])
        delta = tuple(v-u for u, v in zip(before, after))
        assert sum(delta) == len(words[b])-len(words[a]) == 5
        i, j = 62+a, 62+b         # q_a at physical white125+2a
        assert basic[i] == basic[j]
        closed = (full[i] == full[j]) if full is not None else None
        full_closed.append(closed)
        changes.append(delta)
        print('block %d->%d counts %s->%s delta%s basic%s full-closed%s' %
              (a, b, before, after, delta, basic[i], closed))
    certs = []
    for c0, c1 in product(range(4), repeat=2):
        if c0+c1 == 0:
            continue
        total = tuple(c0*u+c1*v for u, v in zip(*changes))
        if min(total) >= 0:
            certs.append(((c0, c1), total))
    print('A2 certificate', min(certs, key=lambda z: (sum(z[0]), z[0])) if certs else 'none in registered domain')
    print('A3 endpoint closures', full_closed, 'cut count', len(forbidden)) if forbidden is not None else \
        print('A3 NOT_RUN: registered phase1 base list absent on this host; no substitute used')
    print('A1 independent controls pass; these are longer words, not hidden-state cycles')


if __name__ == '__main__':
    main()
