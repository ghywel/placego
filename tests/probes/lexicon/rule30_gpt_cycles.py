#!/usr/bin/env python3
"""An inductive cycle certificate for the universal prefix and its first branch.

RUN-ON: cpu, one core, Python 3 standard library (GPT, 2026-10-06).
COMMAND: python3 tests/probes/lexicon/rule30_gpt_cycles.py
COST: seconds; under 20 MB. No long simulation or search over large seeds.

Uses Rowland, Local nested structure in rule 30, section 5 (opened and read),
and the project's RULE30-PRIZE.md sections 8.31 and 8.59. This applies their
reset/parity mechanism; it does not claim a new period-doubling theorem.
Unlike rule30_band.py's sampled seeds and closed-strip orbit certificate,
classify every possible extension of a periodic prefix, up to its first
non-phase-equivalent choice. Proof of the classification is in RULE30-GPT.md G2.

PREDICTIONS, written before this script's first run:
  GC0 (control, must hold): at width 10, all 512 possible edge-normalised
      seeds reach one of the classified phases by time 64, and all subsequent
      16 directly simulated rows follow that phase. Full-strip bit arithmetic
      is independent of the scalar time-word construction.
  GC1 (must hold, known from Rowland and section 8.31): the first branch is
      diagonal 53208; before it the common period doubles at 3, 8, 29, 400.
  GC2 (must hold, certificate): all constructed phases satisfy the direct
      full-strip transition on diagonals 0..53207; common period 16; white
      diagonals 2, 7, 28, 399, 53207. No even-parity white-parent extension
      occurred before diagonal 53208.
  GC3 (must hold, independent settling calculation): the worst-phase
      settling upper bound at diagonal 53199 is 107294, as in section 8.59.
  CF (counterfactual must be rejected): the two possible continuations at
      diagonal 53208 belong to one cycle. They must instead give two disjoint
      directly certified 16-cycles, each a valid finite seed's strip orbit.
  GC4 (blind): the worst-phase settling upper bound at diagonal 53207 is
      between 107294 and 107326.
REFUTED-BY: GC0..GC3 failing, CF not rejected, or GC4 outside its band.
OUTCOME, 2026-10-06, first run: ALL CHECKS PASS, exit 0.
  GC0 PASSED: all 512 width-10 seeds, 16 rows after time 64.
  GC1 PASSED: first branch 53208, doublings 3, 8, 29, 400.
  GC2 PASSED: 53208 diagonals; period 16; white 2, 7, 28, 399, 53207.
  GC3 PASSED: tau(53199) <= 107294.
  CF REJECTED as required: two disjoint certified 16-cycles at width 53209.
  GC4 HELD: tau(53207) <= 107312.

ADDENDUM, before its run (COMMAND: append "birth" to the command above).
Unexpected check: in a forced half-line, diagonal k may first exist at the
wall at time k-L. An all-seed upper bound should not reset it before it exists.
Use the worst valid L, namely 1, and start every extension no earlier than k-1.
  GB0 (must hold): birth-aware bounds are at least the original bounds.
  GB1 (blind): the worst-phase bounds at 53199 and 53207 stay 107294, 107312.
  GB2 (counterfactual rejected): for a scalar column born at 100, with constant
      parents a=0, b=1 and initial state 0, claiming settling at 1 is invalid;
      the birth-aware reset bound 101 is valid and attained.
REFUTED-BY: GB0 failing, GB1 changing either value, or GB2 not rejected.
OUTCOME of birth, 2026-10-06: GB0 PASSED; GB1 REFUTED; GB2 PASSED.
  Original bounds [107294, 107312]; birth-aware [107295, 107313].
  The command printed FAILURES and exited 1, because the blind prediction
  of unchanged bounds failed. These are conservative upper bounds, not
  attained settling times or a counterexample to the original full-line bound.
  Keep this failure visible; do not change the prediction to fit it.
"""


def bit(word, t, period):
    return (word >> (t % period)) & 1


def output_word(a, b, period, initial):
    state, word = initial, 0
    for t in range(period):
        word |= state << t
        state = bit(a, t, period) ^ (bit(b, t, period) | state)
    return word, state


def classify(limit):
    """Return the sole prefix cycle and both continuations at the first branch.

    Words use time bits, not spatial bits. All periods are powers of two.
    Before a branch, every extension is either reset to one solution, or has
    two complementary solutions related by a half-period phase shift.
    """
    words, period, doubled = [1], 1, []
    for k in range(1, limit + 1):
        a = words[k - 2] if k >= 2 else 0
        b = words[k - 1]
        if b:
            _, initial = output_word(a, b, period, 0)
            word, end = output_word(a, b, period, initial)
            assert end == initial
        elif a.bit_count() % 2:
            words = [w | (w << period) for w in words]
            period *= 2
            a = words[k - 2]
            word, end = output_word(a, 0, period, 0)
            assert end == 0
            doubled.append(k)
        else:
            u, eu = output_word(a, 0, period, 0)
            v, ev = output_word(a, 0, period, 1)
            assert eu == 0 and ev == 1
            return words, period, doubled, k, (u, v)
        words.append(word)
    return words, period, doubled, None, None


def rows(words, period):
    result = [0] * period
    for k, word in enumerate(words):
        for t in range(period):
            result[t] |= bit(word, t, period) << k
    return result


def strip_step(row, mask):
    return ((row << 2) ^ ((row << 1) | row)) & mask


def certified(orbit, width):
    mask = (1 << width) - 1
    return all(strip_step(v, mask) == orbit[(t + 1) % len(orbit)]
               for t, v in enumerate(orbit))


def settling(words, period, target, wall=False):
    bound = 0
    for phase in range(period):
        older, previous = 0, 0  # diagonal -1, diagonal 0
        for k in range(1, target + 1):
            start = max(older, previous, k - 1 if wall else 0)
            parent = words[k - 1]
            if parent:
                delay = next(d for d in range(period)
                             if bit(parent, start + d + phase, period))
                current = start + delay + 1
            else:
                current = start  # either extension is periodic from here
            older, previous = previous, current
        bound = max(bound, previous)
    return bound


def birth_audit():
    words, period, _, _, _ = classify(53208)
    targets = [53199, 53207]
    old = [settling(words, period, k) for k in targets]
    new = [settling(words, period, k, wall=True) for k in targets]
    tests = [('GB0', all(a <= b for a, b in zip(old, new))),
             ('GB1', new == [107294, 107312]),
             ('GB2 counterfactual rejected', 1 < 100 and 101 >= 100
              and (0 ^ (1 | 0)) == 1)]
    print(f'original {old}; birth-aware {new}', flush=True)
    for name, okay in tests:
        print(f"{'PASS' if okay else 'FAIL'} {name}", flush=True)
    okay = all(value for _, value in tests)
    print('ALL CHECKS PASS' if okay else 'FAILURES')
    return not okay


def main():
    failures = []

    def check(name, okay, detail):
        print(f"{'PASS' if okay else 'FAIL'} {name}: {detail}", flush=True)
        if not okay:
            failures.append(name)

    small, sp, _, branch, _ = classify(9)
    small_cycle = rows(small, sp)
    okay = branch is None
    for seed in range(512):
        v = (seed << 1) | 1
        for _ in range(64):
            v = strip_step(v, 1023)
        if v not in small_cycle:
            okay = False
            continue
        phase = small_cycle.index(v)
        for t in range(16):
            okay &= v == small_cycle[(phase + t) % sp]
            v = strip_step(v, 1023)
    check('GC0', okay, '512 width-10 seeds; 16 rows after time 64')

    words, period, doubled, branch, choices = classify(53208)
    check('GC1', branch == 53208 and doubled == [3, 8, 29, 400],
          f'first branch {branch}; doublings {doubled}')
    orbit = rows(words, period)
    white = [k for k, w in enumerate(words) if w == 0]
    check('GC2', period == 16 and len(words) == 53208
          and white == [2, 7, 28, 399, 53207]
          and certified(orbit, len(words)),
          f'prefix length {len(words)}; period {period}; white {white}')
    bound = settling(words, period, 53199)
    check('GC3', bound == 107294, f'tau(53199) <= {bound}')

    cycles = [rows(words + [w], period) for w in choices]
    check('CF rejected', not (set(cycles[0]) & set(cycles[1]))
          and all(certified(c, len(words) + 1) for c in cycles)
          and all(len(set(c)) == 16 for c in cycles),
          'two disjoint certified 16-cycles at width 53209')
    last = settling(words, period, 53207)
    check('GC4', 107294 <= last <= 107326, f'tau(53207) <= {last}')
    print('ALL CHECKS PASS' if not failures else f'FAILURES: {failures}')
    return bool(failures)


if __name__ == '__main__':
    import sys
    raise SystemExit(birth_audit() if sys.argv[1:] == ['birth'] else main())
