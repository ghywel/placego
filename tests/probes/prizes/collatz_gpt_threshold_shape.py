"""G95 NS1-NS2, preregister before execution. NOT RUN.
NS1 MUST HOLD: every binary barrier word h1..6, forward integer demand
DP agrees with independent full-string enumeration, mass 2^h.
NS2 BLIND: no-adjacent-zero schedules h1..12 all give log-concave laws.
Stop at first failure, retain full schedule/law, independently enumerate.
UNEXPECTED COUNTERFACTUAL MUST FAIL: all fair-bit demand laws are
log-concave, even without the schedule restriction.
REFUTED-BY: schedule 00011 gives atoms (26,5,1)/32, with 25 < 26.
No actual-start population, earlier-profile rerun or global bound.
ADDENDUM BEFORE EXECUTION: Local L048 at 5d2fda9 refutes the all-length
no-adjacent-zero sufficient restriction on the actual schedule. NS2 length12
finite prediction is retained but NOT RUN; default executes NS1 only.
No broader family search; explicit --shape is outside this updated run plan.
"""
from collections import Counter
from itertools import accumulate, product
import json
from pathlib import Path
import sys


def dp(schedule):
    states = Counter({(0, 0): 1})
    barrier = 0
    for increment in schedule:
        barrier += increment
        nxt = Counter()
        for (z, demand), count in states.items():
            for bit in (0, 1):
                zz = z+bit
                nxt[zz, max(demand, barrier-zz)] += count
        states = nxt
    law = Counter()
    for (_, demand), count in states.items():
        law[demand] += count
    return [law[j] for j in range(sum(schedule)+1)]


def enumerated(schedule):
    barriers = list(accumulate(schedule))
    law = Counter()
    for bits in product((0, 1), repeat=len(schedule)):
        gaps = [b-z for b, z in zip(barriers, accumulate(bits))]
        law[max([0]+gaps)] += 1
    return [law[j] for j in range(sum(schedule)+1)]


def violation(law):
    for j in range(1, len(law)-1):
        if law[j]**2 < law[j-1]*law[j+1]:
            return j
        if law[j] == 0 and any(law[:j]) and any(law[j+1:]):
            return j
    return None


def main(run_shape=False):
    controls = 0
    for h in range(1, 7):
        for schedule in product((0, 1), repeat=h):
            law = dp(schedule)
            assert law == enumerated(schedule) and sum(law) == 2**h
            controls += 1
    guard = (0, 0, 0, 1, 1)
    assert dp(guard) == enumerated(guard) == [26, 5, 1]
    assert violation(dp(guard)) == 1
    profiles = 0
    failure = None
    for h in (range(1, 13) if run_shape else ()):
        for schedule in product((0, 1), repeat=h):
            if any(x == y == 0 for x, y in zip(schedule, schedule[1:])):
                continue
            law = dp(schedule)
            assert sum(law) == 2**h
            profiles += 1
            j = violation(law)
            if j is not None:
                assert law == enumerated(schedule)
                failure = dict(h=h,schedule=''.join(map(str,schedule)),law=law,index=j)
                break
        if failure:
            break
    Path('/private/tmp/placego-gpt-threshold-shape.json').write_text(
        json.dumps(dict(controls=controls,profiles=profiles,failure=failure),indent=2))
    print('NS1 PASS:',controls,'independent barrier/coin laws')
    print('Unrestricted fair-bit log-concavity counterfactual REFUTED: (26,5,1)/32')
    print('NS2', 'NOT RUN (superseded by L048)' if not run_shape else ('REFUTED' if failure else 'HELD in finite scope'), 'after',profiles,'schedules')
    print('Independent failure:',failure)
    print('No actual demand shape theorem or unmatched allocation estimate inferred')


if __name__ == '__main__':
    main(run_shape="--shape" in sys.argv)
