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

## GC1944 archival correction: this machinery and candidate were already known

A deeper read of the record-search hits found the exact antecedents, not merely
similar front arguments. GC1167 (13 October, independently carried L658) already
proved the one-cell-behind defect recurrence and its clamped endpoint.
GC1194/L679 already derived the28-step parity flip/56-step repetition on this
seven-ring ether. GC1195/L680 extends it to a finite nonlinear discrepancy tube.
GC1197/L682 already gives the allowed black-start arrival residues14,30,50
modulo56 for the same reference. Consequently GC1942's recurrence and d50
candidate are rediscoveries/applications of reviewed work, not fresh mechanisms.
The sentence above calling the scoped recurrence new here is superseded.

The coordinate match is exact: GC1197's black-start row A^1 is depth-first
1100001 repeated. That is precisely our depth d black iff d mod7 in0,1,2.
Its reference orbit R_(t+3 mod4)[−d mod7] has the same clock and initial row
as the ether used here. The two rule evolutions therefore coincide on the
left under the identical boundary. Its first-departure ell is our d; no
terminal-grammar conversion is needed for GC1197's general band statement.

Read complete archived entries GC1167, GC1194–GC1197 in
archive/gpt/RULE30-GPT.9.md. The finite-tube recurrence is:

    delta_s(next) = delta_s XOR
       ((a XOR delta_(s−1)) OR (b XOR delta_(s−2))) XOR (a OR b),

with delta0=1, delta_−1=delta_−2=0, reference a,b at the two sites ahead.
Each fixed-width block is triangular; its28-step map has order dividing2^R.
Stop the travelling representation when the front reaches depth1, then evolve
the endpoint cells under the real clamped wall. Reusing this reviewed theorem
is preferable to inventing another length scan. We do not reuse old minimal-end
class tables as verdicts for a different initial discrepancy packet.

The old record also warns against precisely that extrapolation: GC1196 retained
ten classes of a different finite-terminal family after R3, and GC1197 left
earlier departures unresolved. Those held experiments are not restarted here.
L49's next white condition and actual-right realization still need their own
specific review; its membership in the allowed first-two-arrival class is
already known. A numerical test needs a discriminating question beyond
reconfirming this phase classification.

Method correction: the initial record search returned GC1167/GC1195, but the
first pass read only the early displayed results. A search receipt is not an
adequate prior-work review unless the directly matching entries are followed.
The successful identification of a previously proved tool is useful; presenting
its reconstruction as new progress would not be. No new run or proof submission.

## GC1945: the next-white decision already has a short forbidden-word screen

For the actual L49/d50 question, all white-time right samples before49 equal
the reference if the earlier clock is preserved. Thus samples at41,43,45,47
are1,0,1,0; repairing arrival50 requires right0 at49. If the pending left
calculation gives l(51)=0, continuing through52 would require right1 at51,
creating the six-sample factor101001 at41,43,45,47,49,51.

That factor is already excluded in both phase sections of
`tests/probes/lexicon/rule30_local_mfw44.txt`. Its certified finite-language
absence is the premise reused by GC1023 and GC1196 (archive/gpt/RULE30-GPT.8.md
and .9.md). Under that existing reviewed certificate, l(51)=0 closes this
candidate by52 for every right completion. If l(51)=1, the required factor
is101000 and this particular screen does not exclude it. No value for l(51)
is asserted here; Local's hand calculation remains the selected dependency.

Source caution: the current kit's Rule30PeriodTwoWidth6.occ_g12 checks101001
inside its bad class, while col1_constraints transfers it only after an
unspecified eventual entry time. That exported eventual theorem alone must
NOT be used to reject a finite prefix at41. This application instead inherits
the project's finite-language certificate as GC1023/GC1196 did; no fresh SAT,
certificate replay or Lean compilation is claimed. If that inherited premise
is questioned, audit its carrying finite-cone certificate before using the
bound. Do not silently replace it with the kit's eventual claim.
