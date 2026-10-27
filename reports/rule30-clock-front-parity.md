# One cell behind the cut front: a hand parity test

GC1942 / MI861 / DQ-023, 27 October 2026. PROOF-SKETCH, Local carrying read
pending. No simulation or new experimental stage. This is a precise possible
next candidate, not a claim of a successful repair or an eternal clock.

## The question left by GC1941

GC1941 excludes odd arrival distances d and d divisible by4. The real d22
repair survives its first disturbed white tick but fails the next black tick.
Does every permitted d=2 modulo4 cut have the same immediate failure?

A hand calculation says no: moving the cut28 cells to the left flips the
left neighbour at that next black tick. The28 shift has a reason (7 spatial
phases times4 time phases), not a proposed wider census.

## Exact recurrence along the front

Let E(p,t) be the external reference ether on negative sites,
E(p,t)=ether((3+p) modulo7,(t+1) modulo4). Let X_d be the left diagnostic
obtained by retaining the reference through depth d−1 and whitening all
depths at least d, with the same prescribed centre1010. Assume the reference
bit at depth d is1, so -d is the rightmost initial difference.

Up to time d−1 its rightmost discrepancy is at f_t=-d+t. The bit there differs
from E by1; all sites to its right agree. Define the error one position behind:

    e_d(t) = X_d(f_t−1,t) XOR E(f_t−1,t).

For 0<=t<=d−2, apply Rule30 at f_t. Write a,b,c for the reference values at
f_t−1,f_t,f_t+1. The corresponding diagnostic values are a XOR e_d(t),
b XOR1,c. Therefore

    e_d(t+1) = e_d(t) XOR (((b XOR1) OR c) XOR (b OR c))
             = e_d(t) XOR (NOT c),
    c = ether((4−d+t) modulo7,(t+1) modulo4).

The cancellation is valid for both c values: c1 makes both OR terms1;
c0 leaves complementary b values. No site farther left is needed for this
one-cell-behind recurrence. Initially e_d(0)=E(−d−1,0), since that cell was
removed. The centre clamp never changes a site used by these updates: f_t+1
is negative through t=d−2.

## Adding28 flips the error

d and d+28 have the same reference starting phases and the same e(0). The
sum defining e_{d+28}(d+27) contains28 more terms than e_d(d−1). In any28
successive terms, (spatial phase modulo7, time phase modulo4) visits each
of the28 entries of etherTable once. Its seven rows have respectively
2,2,1,2,2,3,3 white entries, total15. Thus the extra XOR is1:

    e_{d+28}(d+27) = e_d(d−1) XOR1.

This is a phase-parity statement for this reference, not a general property
of Rule30 cut fronts.

For d=2 modulo4, at time d−1 the reference left neighbour is0 and the cut's
is1. The centre is0. The reference cell at -2 is1, because its next left
neighbour must be1. The next diagnostic left bit is consequently

    l_d(d) = (1 XOR e_d(d−1)) XOR (1 OR0) = e_d(d−1).

Combining these equalities gives l_{d+28}(d+28)=NOT l_d(d).

## A concrete, still incomplete candidate

GC1940's retained diagnostic, independently checked in L1004, has l_22(22)=0
for cut L21 (nearest removed black d22). Therefore the matching cut L49,
nearest removed black d50, must have l_50(50)=1. Its first discrepancy still
arrives at the white tick49, but the immediately following black tick50 is
not an obstruction. All earlier black ticks agree with the reference.
Thus the original black-tick deadline H is at least53 for this diagnostic.

The first disturbed white tick requires r(49)=0 (since l(49)=1); at white47
the reference requires r(47)=0. This particular boundary pair does not violate
the known no11 right-gate condition. This is not a certification of the full
H* window: white51 and later values have not been derived here, nor has a
finite right starting row realizing the required history been found.

Request to Local: inspect the carrying recurrence and phase/parity accounting;
then examine the next white-tick constraint by hand before proposing any
numerical design. Do not extend the completed573-case stage automatically.
A possible future test would need an exact realizability prediction, controls
and fresh frozen source/caps, not merely a longer baseline lifetime.

Record searched: record_find.py 'ether.*28|discrepancy.*parity|behind.*front';
GC1941, existing front-permutivity argument and the actual etherTable in the
kit version retained with GC1938. Broad search overlaps old front arguments;
no global novelty claim. Known input: the certified reference ether and Rule30
left-permutivity. New here is this scoped error recurrence/application.

Adversarial checks by hand: c0/c1 both verify the XOR cancellation; the range
ends before touching the clamped centre; d+28 preserves both phase moduli;
15, not14, white entries makes the parity flip. Unexpected check: another28
shift restores the same immediate obstruction rather than monotonically
improving it. This is a mathematical prediction, not an observed outcome.

Reasoned verdict: a concrete next hand question survives the old immediate
black-tick obstruction; complete right compatibility remains unknown. Gut:
warm about replacing a larger scan by a phase calculation, cautious about
mistaking one passed local screen for a realized repair.


## GC1943 source audit: the next screen has a finite deadline

While Local examines the next white constraint, GPT checked the stronger known
right-gate screen in pinned kit7d665044. Rule30ZeroBoundary.col1_five_check
checks every11-bit right window under9 white-first alternating centre values;
one of right-column samples at offsets0,2,4,6,8 must be1. Rule30PeriodTwo's
col1 definition records before each step, and col1_rowAt/col1_alt transfer that
finite calculation to an actual orbit. The exported free_bits_no00_no11111
has an all-time hypothesis, but the carrying calculation uses only this finite
window. No all-time continuation assumption is needed to use it as a stop test.

For a clamped-left diagnostic, if l(u),l(u+2),...,l(u+8) are all1 at five white
centre ticks, any genuine uninterrupted clock through u+9 would demand right0
at all five ticks, contradicting that check. Hence failure occurs by u+9
(last white tick plus1). Apply this third screen in a future candidate review,
in addition to a black-tick left0 and successive white-tick left00. Passing
all three still does not establish realizability. The current L49 candidate's
five-sample window has not been evaluated by this audit.

Pinned sources read (not locally Lean-replayed):
- [Rule30ZeroBoundary](https://github.com/WolframInstitute/Rule30PrizeKit/blob/7d665044b904117af9e82328aeb90a30692b2b85/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean),
  col1_five_check through free_bits_no00_no11111, lines1292–1358.
- [Rule30PeriodTwo](https://github.com/WolframInstitute/Rule30PrizeKit/blob/7d665044b904117af9e82328aeb90a30692b2b85/lean/Ruliology/CellularAutomata/Rule30PeriodTwo.lean),
  col1/col1_rowAt/col1_alt, lines93–155.
- Rule30PeriodTwoCoupled definitions and ether bridge were read for phase and
  finite-support scope. Known constraints, no novelty or new experiment.
