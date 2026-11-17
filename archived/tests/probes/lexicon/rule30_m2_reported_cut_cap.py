"""GC1111: connect a reported actual-language cut to the typed101 rank.

Missing inference: GC1103's pure M2 SCC still survives width36,
but Local L591 already reports its periodic visible word absent
at length 120. Does this give a right-paid typed101 duration bound,
independent of initial left radius? No new membership query is made.
Record searched: SLC3|macro.*(SLL|k.?1|k.?3)|typed.*cut|GC1106
with intersect|cut|language|cycle ->15hits9files; SLC2|5,5,3,3,3
with120|period|cycle ->1 hit in 1 file. L591, SLC header and reviewed
GC1103 rank read. The full cut file is unavailable in this checkout.
P1 BEFORE controls: eight M2 returns contain EVERY length 120
cyclic factor of the 19-sample visible period, at positive sample
age as well. This suffices whichever rotation/phase L591 tested.
REFUTED-BY: any cyclic factor missing from eight complete periods.
Counterfactual: seven periods suffice uniformly over rotations.
REFUTED-BY: a length 120 cyclic factor absent from their 133 samples.
Controls: spell q independently from gaps and from h(S)/h(L);
compare Local's LLSSS block spelling by cyclic rotation, not an
assumed phase. Reuse the reviewed rank<=2; do not recompute it.
Unexpected check: at a time0 macro onset a black-phase query
cannot be based at time-1. Require an occurrence starting AFTER
sample0. The eight-period cover must still hold.
Evidence guard: L591 gives no explicit120 word/phase/certificate
in git. A derived cap is pending that retained receipt, not a
new verified absence or unconditional certificate. Ask Local for
the existing artifact; do not restart the old realization search.
OUTCOME: P1 HELD for all 19 cyclic factors, including positive age.
Seven periods miss 5 factors, so that counterfactual is REFUTED.
The uniform arithmetic gives23 returns/886 ticks. No membership
was tested: this remains derived from L591's reported120 absence,
pending its precise word/phase and retained verification receipt.
"""

from itertools import accumulate


def contains(word, factor, minimum_start=0):
    return any(word[i:i+len(factor)] == factor
               for i in range(minimum_start, len(word)-len(factor)+1))


def main():
    letters = 'SLLSS'
    gaps = [3 if a == 'S' else 5 for a in letters]
    marks = [0] + list(accumulate(gaps))[:-1]
    q = ''.join('1' if i in marks else '0' for i in range(sum(gaps)))
    h = {'S': '110100', 'L': '1101000100'}
    assert ''.join(h[a] for a in letters)[::2] == q
    local = '00001' * 2 + '001' * 3
    rotations = {q[r:] + q[:r] for r in range(19)}
    assert len(q) == 19 and len(rotations) == 19 and local in rotations
    factors = {(p * 7)[:120] for p in rotations}
    assert len(factors) == 19
    assert all(contains(q * 8, f) for f in factors)
    assert all(contains(q * 8, f, 1) for f in factors)
    missed = sorted(f for f in factors if not contains(q * 7, f))
    assert missed
    # GC1103 supplies <=2 non-M2 macros, hence <=3 M2 runs.
    # With at most7 M2 returns per run and exceptional length<=44:
    macros = 3 * 7 + 2
    duration = 3 * 7 * 38 + 2 * 44
    assert (macros, duration) == (23, 886)
    print(dict(P1='HELD', rotations=len(rotations),
               seven_period_missing=len(missed),
               positive_age_eight_period_cover='PASS',
               typed101_completed_returns=macros,
               typed101_duration=duration,
               scope='derived from reported L591 absence; exact receipt pending'))


if __name__ == '__main__':
    main()
