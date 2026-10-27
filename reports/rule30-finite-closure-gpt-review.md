# L1002 carrying review: finite predecessors and the off-edge black-run obstruction

GC1936 / MI855, GPT, 27 October 2026. Owner-requested manual review.
Source f0c2978ca434251073dcdb779bdee48dbf8bb0f9: complete L1002, amended
run/staircase/ruler notes, and all129 lines of closure_finite_look.py read.
No new numerical run, schedule, job or portal work.

## Verdict

Local's adoption of GC1935 is accepted. The corrected compatible-phase
formulation stands. The finite-predecessor dichotomy, the equivalence reducing
assertion A to the eventually-ones question, and the fixed-offset compactness
formulation all carry by hand. A remains open. The negative-time tower also
carries after keeping its finite boundary correction: the third predecessor
is eventually period3, not a globally period3 edge code.

## 1. Exact inverse and finite-predecessor classification

Write r_j and q_j for bits of R and Q=T^-1(R), with q_-1=q_-2=0. The inverse
is unique, determined successively by

    q_j = r_j XOR (q_(j-1) OR q_(j-2)).

For finite odd R of top bit d, r_j=0 for j>d, so beyond d the recurrence is
q_j=q_(j-1) OR q_(j-2). Either the pair (q_d,q_(d-1)) is00 and the tail is0,
or the tail becomes all1 by bit d+1 at the latest. In the finite case, r_d=1
forces q_(d-2)=1 and q_(d-1)=q_d=0, so the top bit of Q is exactly d-2.
Conversely q_(d-1)=0,q_(d-2)=1 gives that finite case. This criterion refers
to predecessor bits q, not the corresponding bits of R.

The small cases are explicit: R=1 has Q=-1, and R=3 has Q=-3 (eventually1).
Thus the finite alternative is only available for d>=2. This fills the
otherwise implicit small-degree boundary in the statement.

## 2. Both directions of the reduction carry

Let Omega be the closed set of codes whose every finite prefix belongs to the
cycle C_k of1. T and its unique triangular inverse preserve Omega: each acts
as a permutation of every C_k. This supplies the inverse invariance used here.

Let B say that -1 is the only eventually-all-ones point of Omega.

**B implies A.** Start with any finite odd R in Omega and repeatedly invert.
Each finite predecessor lowers the top degree by2, so a chain of finite
predecessors cannot continue indefinitely. The first eventually-ones predecessor
is in Omega, hence is -1 under B. Its image is1. Reversing the finitely many
steps shows R=T^tau(1) for a nonnegative ordinary integer tau.

**A implies B.** If Q in Omega is eventually1, then T(Q) has an eventually0
tail (1 XOR(1 OR1)=0), so is a finite odd code R in Omega. Under A it is
T^tau(1). If tau>=1, uniqueness of the inverse gives Q=T^(tau-1)(1), a finite
code, contradicting its eventually1 tail. Hence tau=0, Q=T^-1(1)=-1.

Therefore the two assertions are equivalent, not merely one-way implications.

## 3. The past and the cap formula

Reading from the edge, LOW BIT FIRST:

- T^-1(1) has bits111111... and is -1.
- T^-2(1) has bits100100100...: bit j is1 exactly for j divisible by3.
- T^-3(1) has bits111011011...: bit0 is1, and for j>=1 it is0 exactly when
  j is divisible by3. Equivalently it is an initial1 followed by110 repeated.

Substitution into the inverse recurrence proves each infinite pattern by
induction on j. In particular the third row has a boundary defect; saying
"period3 with two ones" describes its tail. In 2-adic rational notation the
last two codes are -1/7 and1/7 respectively. These are not ordinary finite
starting rows. Their periodic interiors connect to GC1932's ancestry tower;
retain edge-frame orientation and finite boundaries when making that connection.

For any fixed depth k, these negative-time prefixes occur at ordinary phases
(p_k-j) mod p_k on C_k. Thus "visible at time p_k-j" is correct when p_k>=j,
or with the phase interpreted modulo p_k. It is a finite-window statement.

For any positive L, the first L bits at time u are all1 iff the code is -1
mod2^L. Applying the invertible T takes that residue to1, so equivalently
T^(u+1)(1)=1 mod2^L, i.e. p_L divides u+1. The cap formula carries exactly.
It controls black runs TOUCHING the edge; it does not bound detached runs.

## 4. The geometric equivalent, with the quantifiers retained

An eventually-ones Q != -1 in Omega has a last zero at some depth z>=1,
followed by ones at every greater depth. Every finite prefix of Q occurs on
the ordinary single-seed orbit. Thus black runs starting at depth z+1 after
that zero have unbounded length across orbit times, for that fixed z.

Conversely, suppose for a FIXED z the orbit has runs beginning at z+1,
preceded by zero at z, with arbitrarily large lengths. Compactness supplies
a convergent subsequence of these orbit points. Its limit lies in Omega,
retains zero at z and has ones at all larger depths. It is eventually1 and
is not -1. This proves the claimed equivalence.

The desired statement is therefore:

    for every fixed z>=1, there exists a finite B(z) bounding those lengths
    at every ordinary time.

It does NOT assert one bound for all z. It does not follow just from finite
periodicity of a strip: as the candidate run length grows, the strip we must
inspect grows too. Nor does the edge-touching cap formula establish it.
The missing fact has become a precise geometric question, but is not solved.

## 5. Source audit of the numerical support

No rerun or raw-output audit. Counts and timings below remain Local-reported.
The source makes the reported interpretations checkable:

- A1 enumerates all odd R<2^24 and tests exact membership in C_44. A finite
  prefix mismatch really excludes that R from Omega. The12 stated survivors
  are known forward rows, so if the printed equality holds this settles A
  for all codes in that size range, not merely their first few updates.
  It does not settle unbounded code size.
- A2 follows from that equality plus the finite-depth theorem for the excluded
  codes; A3 is not asserted. Keep that distinction.
- A1 is PRINTED, not part of the exit condition. Neither hits==forward nor
  extra==[] can cause a nonzero exit in the current script. B1's reach63 list
  is also printed only. A zero process exit therefore certifies only the
  explicit C1/C2/C3 conditions, not all A/B predictions. Inspect retained
  output to adopt the numerical outcomes, and add assertions before reuse.
- The masked64-bit evolution is exact on bits0..63. A run reaching bit63 is
  censored, not proven to end there. The reported absence of such runs from
  z<=40 makes the observed maxima exact within the reported time window.
- No resource supervisor or raw receipt is cited by the new note. This review
  does not certify execution time, aggregate resource enforcement or the
  printed maxima as independently inspected artifacts. No repeat is requested.

The useful independent result here is the hand equivalence and its exact
quantifiers. The numerical support remains separately labelled.

## Next concrete action

Adopt the reduction, retain the compatible-phase theorem, and keep A open.
A future proof must bound detached black runs for each fixed offset, or find
an equivalent obstruction to an eventually-ones closure point other than -1.
The existing cap formula cannot be used as that bound without a new argument.
Local can correct the third-predecessor wording and checker exit coverage
without rerunning or widening the search. Gut: warm; the gap now has a precise
picture and a valid equivalence, rather than only a missing abstract phase.
