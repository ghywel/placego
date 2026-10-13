#!/usr/bin/env python3
"""GC1170: carry child-phase cuts in a formal birth-parent language.

RUN-ON: CPU, standard library. No solver, record search or Q/P census.
COMMAND: python3 tests/probes/lexicon/rule30_birth_parent_language.py
Record searched: parent-language/birth-automaton/child-phase with
cut/coupling/root/prepend ->48 hits13files; G25,8.82, GC1002/3,
GC1158/59 and GC1169 read.

PREDICTIONS before execution (2026-10-13):
 T1: F0(C0(0w))=C1(w), F1(C1(w))=C0(w), in every known prefix;
     compare truth-table inversion with an independent forward step.
 T2: canonical S parent0100101 of real B word100101 must pass when
     its first0 is kept outside the child B cut automaton.
 T3: formal B parent101010000 of the known real S word must pass
     the child S cuts, even though parent B cuts reject it.
 CF: applying the parent's ordinary phase catalog is sound; T2/T3
     are existing actual-word countercontrols to this claim.
 Unexpected: even using the correct child B catalog fails T2 if
     the synthetic first0 is consumed as a child visible bit.
 Independently compare prefix-machine and direct substring acceptance
     on all words<=10. These are finite cut tests, not real membership.

OUTCOME:4094 prefix-machine/direct controls and252 formal time-shift
controls pass. Both actual-child countercontrols are retained while
ordinary parent-phase filters reject them. The synthetic-bit wrong
consumption also rejects the real B example. Nonminimal live-prefix
state bounds are12845 (childS) and13660 (childB, including startup).
These are root-language states, not a common all-depth inverse bound.
"""
from functools import lru_cache
from itertools import product
from rule30_phase_prepend_guard import cuts, forbidden
from rule30_prefix_realization import inverse, rule


class ParentMachine:
    """The wall phase is1-child; the root filter carries child-phase cuts."""
    START = '<synthetic0>'

    def __init__(self, fs, child_phase):
        self.child_phase = child_phase
        self.terminal = frozenset(fs[child_phase])
        self.prefixes = frozenset({''} | {f[:i] for f in fs[child_phase]
                                        for i in range(1, len(f))})
        self.live_state_bound = len(self.prefixes)+(child_phase == 1)

    @lru_cache(None)
    def step(self, state, bit):
        if state == self.START:
            return '' if bit == '0' else None
        s = state+bit
        if any(s[i:] in self.terminal for i in range(len(s))):
            return None
        return next(s[i:] for i in range(len(s)+1) if s[i:] in self.prefixes)

    def accepts_prefix(self, v):
        s = self.START if self.child_phase == 1 else ''
        for bit in v:
            s = self.step(s, bit)
            if s is None:
                return False
        return True


def image(a, wall, n):
    return [rule(a[j+1], a[j], wall if j == 0 else a[j-1]) for j in range(n)]


def main():
    fs = cuts()
    machines = [ParentMachine(fs, p) for p in (0, 1)]
    nchecks = 0
    for n in range(11):
        for bits in product('01', repeat=n):
            v = ''.join(bits)
            expected = [not forbidden(v, fs[0]),
                        not v or (v[0] == '0' and not forbidden(v[1:], fs[1]))]
            for p in (0, 1):
                assert machines[p].accepts_prefix(v) == expected[p]
                nchecks += 1
    print('direct/prefix-machine controls', nchecks, 'PASS; state bounds',
          [m.live_state_bound for m in machines])

    shifts = 0
    for n in range(1, 7):
        for bits in product((0, 1), repeat=n):
            w = list(bits)
            childB = inverse(w, 1)
            parentS = inverse([0]+w, 0)
            assert image(parentS, 0, 2*n) == childB
            childS = inverse(w, 0)
            parentB = inverse(w, 1)
            assert image(parentB, 1, 2*n-1) == childS[:2*n-1]
            shifts += 2
    print('formal time-shift controls', shifts, 'PASS')

    wB, wS = '100101', '101010000'
    assert not forbidden(wB, fs[1]) and not forbidden(wS, fs[0])
    assert machines[1].accepts_prefix('0'+wB)
    assert forbidden('0'+wB, fs[0])
    assert forbidden('0'+wB, fs[1])  # wrong synthetic-bit consumption
    assert machines[0].accepts_prefix(wS)
    assert forbidden(wS, fs[1])
    print('both actual-child countercontrols retained PASS; ordinary parent filters reject')
    print('ALL CHECKS PASS; no bound on record or birth maxima')


if __name__ == '__main__':
    main()
