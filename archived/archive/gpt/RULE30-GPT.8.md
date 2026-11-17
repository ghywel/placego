# RULE30-GPT, volume 8: GC966 to GC1117 (2026-10-10 to 2026-10-11)

*A frozen volume of [RULE30-GPT.md](../../RULE30-GPT.md), rotated out of it unchanged on 2026-10-22 in the documentation spring clean. New entries go in the live file; the list of volumes is at its top.*

## GC966 — L552 transient-to-cycle phase interface check (2026-10-10 05:50 BST)

**Bounded informed hand audit, not a new wall theorem.** Broad literal/stage
phase search was noisy (299hits80files); narrowed BlackEnd38/GC951 +
phase/boundary/wrap ->2hits1file. GC951 and L552/CL175 read in full.
Expected the stage definition using C_(i mod p) to agree with the
terminal transient edge A_(m-1)->C_0 because p=q+1 and m=n0*p.
Countercontrol: if m is arbitrary, the aligned definition must instead
use C_((i-m) mod p). Distinct singleton cycle masks at p=3,m=1 make
the registered terminal edge target C0 while the unshifted definition
selects C1; that terminal inclusion alone cannot certify the join.
This is an abstract phase fixture, not an actual strip counterexample.

At the intended m, divisibility gives m mod p=0, so the join matches;
the periodic transition from phaseq to0 needs its own registered
wrap edge. If source permits m=0, its base must separately cover
full0 in C0; the A_(m-1) terminal edge is then not the base obligation.
Generator/Lean source still unpublished here, so these are assembly
requirements, not source defects or kernel acceptance. CL175's
coverage-direction read ACK, no duplicate generator/size run.

**Owner steer and next.** The owner asks whether we are moving toward
the proof instead of continuous restatement. Report sharp B3 and
completed supporting formal proofs honestly, with the actual-history
Q7 budget still open. Further generic identity/threshold/suffix
refinements remain stopped. With the source-review queue caught up,
next reasoning must target a concrete selected-history budget mechanism
and retain failure if it supplies only another identity. L552 kernel
run stays Local's. Verifiedea3fb131/31676d8c; Cloud off-pool rule read
and accepted, no work/request routed there. Scratch deferred, room closed.


#### GC968 — Stop the independent temporal-wrap charge (2026-10-10 06:10 BST)

Q7 growth attempt, no new theorem or experiment. Record searched: backward/absorption +
wrap/winding/finite-support -> 12 hits in 7 files; G7, G185, G200 and G203 read.
Prediction for the hand check: separate black source cells do not furnish additive wrap
charges. Countercontrol: an empty finite pair has no moving front. Unexpected check:
finite-support nonabsorption and cyclic absorption have different terminal states.

For the backward map H(a,b)=(Sb XOR(a OR b),a), start from a nonempty finite source
(a,0) on integer temporal sites. Its leftmost occupied site is m. At that site the
leading state alternates (1,0), (1,1), then creates (1,0) one site left; nothing lies
further left to cancel it. Thus after n steps the leading site is m-floor(n/2),
regardless of how many other black source cells lie to its right. This controls
one exterior front, not one conserved front per black cell. Moreover H(a,b)=0
requires a=0 and Sb=b: on finite support this forces b=0, while on a temporal
circle b=1 is also possible. Cyclic absorption is a collective event, not a
sequence of independently counted finite-pulse deaths.

The attempted additive charge by source weight is therefore unsupported: the
exterior argument tracks only an extremal front and cannot multiply its wrap
time by the number of source cells. It supplies no superlinear stage bound.
No new source census or scalar-potential variant is queued. Stop this mechanism;
next return to selected waiting intervals and seek an actual cross-interval
constraint, rather than another period-growth identity.


#### GC970 — RRL certificate design: finite-word transduction with a white-run counter (2026-10-10)

Design toward the all-depth proof, not a proved bound. Record searched: visible/RRL +
automaton/transducer/invariant/regular; read GC549's cone reduction and RRL's Relaxed
model. Local's RLK registration at 334fa326 received; no run outcome inferred.
Prediction before the hand design: finite temporal words suffice, without assuming
bi-infinite extension of finite witnesses. Countercontrol: retaining the terminal
sample through every depth would falsely permit reconstruction beyond the cone.
Unexpected check: the wall's initial white cell is not part of a run starting at
negative depth, so the initial run counter must be zero in both phases.

Use letters (u(t),v(t)) for a column and its right neighbour. The exact left
reconstruction is the length-decreasing transduction

    h(u,v)(t) = (u(t+1) XOR (u(t) OR v(t)), u(t)),  0 <= t < n-1.

The output is (new left column, old column). Initial words of length n>=1 have
u(t)=(t+phase) mod 2. Apply the chosen forbidden visible words to v at white
wall times strictly before n-1; v(n-1) is unused. This initial language is
regular. One step needs two input letters; a singleton produces no left cell
and cannot advance the spatial run counter. For phase 0 the first output
bit is NOT v(0); for phase 1 it is 1, agreeing with the direct wall equation.

Candidate certificate: regular languages I_0,...,I_C of nonempty pair words.
The initial language is contained in I_0. For each r, split h(I_r) by its first
output bit: black outputs must lie in I_0, white outputs in I_(r+1). For r=C,
the white-output language must be empty. Each obligation is a finite automaton
image/inclusion or emptiness test; the transducer reads overlapping letters
and flushes no final output. This is a concrete verification format, not a
claim that iteration stabilizes or such languages exist for C=17.

Induction over reconstructed depth would then bound every initial negative-side
white run by C, for every finite cone and both phases: choose an initial temporal
word long enough for the last reconstructed site. The shrinking terminal endpoint
matches RRL's T=d+L-1. No temporal-language equality at deeper columns is assumed;
the I_r languages describe their full pair traces, not the original visible DFA.
This avoids the unjustified inference that a regular visible language alone
settles the all-depth question. Next implement the exact transduction and seek
a closed overapproximation; absent closure there is no record bound or prize proof.


#### GC971 — Exact finite-word image engine controls (2026-10-10)

Implemented GC970's DFA initial language and exact inverse-column image in
rule30_rrl_transducer.py; source predictions precede execution. Initial/image
state counts are 81/53 and 82/54 for phases 0 and 1. All 10,920 pair-word
initial-membership controls through length 6 pass; image languages at lengths
1..3 equal independently enumerated literal images. Reconstructed cells agree
with the literal Rule 30 table. Unexpected singleton has empty output; terminal
visible countercontrol fails as required. The first controls only reached short
visible words, so an addendum was written before testing all 2,046 binary visible
words through length 10 in each phase; substring exclusion agrees throughout.
No actual right language enumeration, invariant search, record bound or prize
claim. Next apply this exact image to bounded candidate closures with a state cap.


#### GC972 — First four exact inverse images remain compact (2026-10-10)

Bounded proof-engine search preregistered in rule30_rrl_transducer.py before
execution: 4 inverse depths per phase, 2,000 states and 20 seconds. Minimized
complete-DFA sizes at depths 0..4 are 55,54,52,50,43 (white-first) and
56,55,54,52,50 (black-first). Prediction all <=200 HELD; no cap reached.
Minimization preserves membership in all control words through length 3;
the distinct-phase countercontrol fails as required. Unexpected sink counted.
These are exact images of the K10 finite visible relaxation, not actual-language
counts or records. No white-run counter closure tested yet. Next combine images
with the spatial white-run counter and test a capped closure, rather than extend
depth scans merely for their state counts.


#### GC973 — Capped counter closure unfinished (2026-10-10)

Phase-0 K10, C32 exact counter-language iteration ran 12 preregistered rounds
under a 3,000-state operation cap and 20-second budget. Controls for union,
first-bit filtering, containment and sink pruning PASS; phase countercontrol
fails as required. No cap reached (P1 HELD). Final nonempty DFA sizes are
600,500,348,221,88,40,40; closure was not achieved. This supplies no record
bound, no refutation of C32, and no nonregularity conclusion. Local L556's
K16 witness already rules out C17 for K16 and K10. Retain the failed closure;
next seek a sound finite overapproximation with exact inclusion checks, or
use Local's stronger language, rather than extend this iteration for counts.


#### GC974 — Boundary-only widening cannot certify a white-run bound (2026-10-10)

Specific obstruction to the proposed GC973 next step; hand argument, not second-read.
Known triangular mechanism: G18.4 and G130; certificate object: GC970. Fix v.
After d inverse-column steps the first bit is u(d) XOR a function of earlier
u bits and v(0..d-1), by induction in GC970's recurrence. Thus each successive
u(d) independently sets that depth's initial-row cell without changing earlier
depths. This applies to arbitrary pair words, not only clock words.

For a boundary-only abstraction retaining the first and last m letters and
forgetting the middle, take an accepted clock word of length n=2m+C+1.
Modify only u(m)..u(m+C) to force depths m..m+C white. Both boundaries
remain unchanged, so the abstraction admits this C+1 run for every C.
Therefore this abstraction cannot satisfy GC970's all-depth bounded-run
obligations for any finite allowance. This is not a witness in the full clock
language, and does not close widening that retains internal factor constraints.

Preregistered controls in rule30_rrl_boundary.py: both phases, m=4,8,16,
C=32, all six constructions PASS. Independent inverse truth-table replay
checks the white cells; a final-pivot flip changes its target and preserves
earlier depths; even the terminal right bit is preserved. Full clock
membership rejects all six as expected. Stop boundary-only widening; next
state merging must retain internal constraints and pass exact image inclusions.


#### GC975 — Internal length-3 factor widening loses the bound (2026-10-10)

Implemented sound DFA widening retaining accepted short words, allowed
prefixes/suffixes of length k-1 and all internal factors of length k. Exact
source containment is checked on each widening. Preregistered phase-0 K10,
k3 C32 closure search admits a white output from counter32 at round34;
P1 HELD, no cap. Toy finite-language membership through length5, forbidden
middle countercontrol and empty-language unexpected check PASS. This
refutes this abstract C32 candidate only: no physical witness, no all-k
conclusion. Stop k3 C32; next refinement should retain a distinguishing
constraint from a spurious history rather than blindly increase k.


#### GC976 — Spurious zero trap identifies the lost constraint (2026-10-10)

GC975 diagnostic preregistered before execution, at most8 exact images.
First trap at depth5: exact unary-zero language has maximum length3,
whereas length-3 factor widening accepts every zero word of length>=3.
Recovered initial pair word (0,2,1,2,0,2,1,2) passes direct clock/forbidden
checks; independent inverse truth-table replay yields (0,0,0) at depth5.
Exact rejection of length20 and widened infinite unary cycle controls PASS.
The first execution failed on list/tuple equality; corrected and rerun.

Hand obstruction, not second-read: any source counter language containing
000 is widened to include every 0^n, n>=3 (same prefixes, suffixes, factors).
Since h(0^(n+1))=0^n, arbitrarily many white counter increments follow.
The recovered history places 000 in a reachable counter language, so this
widening cannot certify any finite allowance for K10, not merely C32.
The concrete lost distinction is 000 versus 0000 at exact depth5. Preserve
its provenance or a stronger context when refining; do not globally forbid
0000 in all counter languages without proof. No conclusion about all k or
Local's strengthened relaxation. Next seek a contextual separating constraint,
not another allowance or blind factor-length scan.


#### GC977 — Exact leading-zero profile repairs trap but not closure (2026-10-10)

Targeted refinement intersects GC975 widening with the source's exact allowed
leading-zero lengths, exit letters and accepted pure-zero lengths; every
source inclusion is checked. Toy profile controls through length5, GC976
000/0000 countercontrol and empty-source check PASS (P1 HELD). Capped
phase-0 K10 C32 search instead overflows at round35; prediction of a source
zero-prefix cycle REFUTED. No cap, invariant or physical witness. Thus this
profile removes the diagnosed trap but still loses needed continuation
information. Stop scalar prefix patches; recover the full false history and
locate its first unsupported continuation before another refinement run.


#### GC978 — Counter13 overflow ancestry loses post-exit continuation (2026-10-10)

Preregistered backward diagnostic of GC977's same capped search. Starting
from its shortest overflow word, twenty recovered inverse edges pass independent
truth-table checks. The backward trace first encounters widening loss at
round15/counter13: 0^13 13203220 is accepted by refinement but rejected
by that update's exact union source (P1/P2 HELD). Its first nonextendible
prefix is 0^13 1320322, length20; the length19 prefix is still coaccessible.
Thus leading-zero length and exit letter agree with the source while a later
continuation is unsupported. This is one ancestry's first encountered loss,
not the earliest loss globally; the source itself may contain older abstract
losses. No physical witness or new record bound. Next retain the residual
continuation state after this exit instead of another scalar prefix summary.


#### GC979 — Recovered seven-letter separator works, closure still fails (2026-10-10)

Preserve exact source residual states through the first7 letters starting at
the zero block's exit, then widen. Preregistered GC978 separator control
rejects its loss and contains the exact union source (P1 HELD); independent
finite-toy and keep1/empty controls PASS. Targeted phase-0 K10 C32 closure
still overflows at round36, with no cap (state-cap prediction REFUTED).
No invariant or physical witness. This repairs that known continuation loss
but does not solve the bound. Park fixed packet-length refinements; further
work must preserve residual automaton states, not extend packet cutoffs.


#### GC980 — Residual-test quotient preserves separator but still overflows (2026-10-10)

Group source DFA states by acceptance of a suffix-closed continuation test
set (GC978 lost word's suffixes, words through length2, zero words through4).
Retain all quotient edges nondeterministically, then determinize. Every
source inclusion and test membership is checked. Toy/zero/empty controls
and GC978 separator control PASS. Phase-0 K10 C32 candidate overflows
at round37 (P2 HELD), no cap. No invariant or physical witness. Next recover
this quotient's new false history before changing tests; packet cutoffs remain
parked. No claim that any finite test set will produce a certificate.


#### GC981 — Two guided refinements, then shared time cap (2026-10-10)

Bounded residual learner recovered and excluded two losses with source
containment/inverse controls: 0^28 at counter6/round10, then length23 at
counter11/round15. Test suites grow42->66->87; both candidates overflow
at round37. Third attempt stops on the total20-second budget. No closure;
five-attempt prediction incomplete, not a completed pass. First loss already
has dead prefix 0^6, so full-word acceptance tests spend24 extra zero suffix
tests. Next preserve whether a test prefix has any continuation as well as
its acceptance, to block all extensions of a short dead prefix.


#### GC982 — Short dead-prefix viability blocks pumping, not overflow (2026-10-10)

Acceptance-plus-viability residual signatures preserve every tested prefix's
ability to continue. With44 tests, dead0^6 blocks GC981's 0^28 loss and
all its extensions (source inclusion, toy/CF/U controls PASS); the prior
acceptance-only refinement used66 tests. Phase-0 K10 C32 still overflows
at round37 (P2 HELD). No cap or invariant. Generic partition-feature additions
are stalled; next inspect a specific lost clock-history constraint before
adding tests. No implication against all finite residual certificates.


#### GC983 — Exact white-first origin survives every black reset (2026-10-10)

Phase0 origin starts white, all reset outputs black: keep the whole initial
DFA exact, quotient only its black reset component. Input is K10 plus
Local's certified absent words17 and21, not the full K18 list. Two-way
white-origin containment holds at every update; origin/empty-black/word21
controls PASS. Capped C32 candidate still overflows at round38 (P1/P2
HELD), no invariant or physical witness. Long initial constraints now survive
exactly; remaining abstraction loss is in black-reset feedback. L558/L559
reject C17 through K20, not every finite bound or finite-type route.


#### GC984 — Endpoint-sensitive gap compensation (2026-10-10)

Preregistered bounded hand block, replying to L556/L559: determine the exact
gap constraints of their absent words before designing a wheel/kick grammar.
Record searched: `00100010001010100|4,4,2,2` AND
`context|proper factor|endpoint` -> no hit (including ledger fallback).
Prediction: word17 forbids gaps4422 only with both exterior gaps>=3; word21
forbids preceding5 followed by4444. Counterfactual: either internal motif
alone is forbidden. Independent control: enumerate all exterior gaps2..5
and compare literal binary substring membership. Unexpected check: word21
has only a left endpoint condition, unlike word17. No language census.

Outcome: all literal controls PASS. Write gaps as distances between successive
visible ones. Word17 is `00` + `1000100010101` + `00`; its core has gaps4422.
L556/L557 report minimal absence, so the proper core is present in the actual
white-start visible language. In any interior occurrence with a preceding and
following one, absence of word17 therefore forces the preceding gap=2 OR the
following gap=2: otherwise both endpoint zero pairs exist. This uses absence
of11 to make gaps>=2, and does not require an upper gap bound. It is a concrete
compensation constraint for route3, not an unconditional ban on4422.

Word21 has four leading zeros and core `10001000100010001` (gaps4444),
with no trailing zeros. With absence of00000, its interior left context is
exactly a preceding gap5; hence5,4,4,4,4 is forbidden. L559's shortest-absent
factor claim makes its proper core present too. Finite endpoints retain their
observed zero contexts; no unseen exterior one is assumed. The 16 two-sided
and four one-sided binary controls agree. Actual-language membership and
absence here rely on Local's reported census/SAT checks, not fresh GPT replay.
No all-depth bound or exact kick grammar. Next seek a conserved charge across
these compensating gap2 events; do not replace binary constraints by bare motifs.


#### GC985 — Can the compensating gap2 survive the short constraints? (2026-10-10)

Missing inference: GC984's two possible compensating flanks may themselves
be excluded by the already established K10 words. Before adopting a charge
argument, test both branches against the nine-word input of GC983.
Record searched: `4422|4,4,2,2` AND `charge|cycle|density` -> only GC984 ledger
hits. Prediction: at least one of the16 exterior-gap contexts2..5 survives.
Counterfactual: presence of the proper core guarantees an interior extension;
finite-language factoriality alone does not give this. Independent control:
compare direct substring checks with initial-DFA acceptance of the corresponding
visible code. Unexpected check: identify whether only a boundary occurrence
can survive when all short constraints are imposed. No actual-language census.

Adaptive prediction before the second control: nine-word contexts survive at
(2,2),(2,4),(3,2),(4,2),(5,2). Shared commit ea0ae954 now supplies the full25
words. Predict some survive after this stronger input; explicitly test a zero
before the first flank one, since it is forced in every noninitial occurrence
by11 absence. This endpoint control may distinguish a transient compensation
from a recurrent one; no fixed-point/record sweep is started.

Outcome: first prediction HELD, but unexpected boundary restriction is strict.
Nine-word and full25-word controls leave the same five flank pairs when the
first flank one starts the code. With a leading zero (forced before every
noninitial one), fullK18 leaves only(5,2). All48 direct-substring/DFA comparisons
PASS (16 nine-word,16 fullK18 without prefix,16 with prefix);244 boundary/interior
and44222 controls PASS. This is a necessary rule, not realization of the survivor.

Hand derivation: consider4422 with preceding gap a and following gap b, and
with a zero before the preceding one. Absences11/00000 give2<=a,b<=5.
GC984 gives a=2 OR b=2. The candidate a=2 contains `010100010001`
(prefix0 + gaps244); a=3 contains `010010001` (prefix0 + gaps344).
Thus b=2 and a is4 or5. Candidate a=4 contains `010001000100010101`
(prefix0 + gaps44422), Local's length18 word. Hence a=5,b=2:

    every such interior4422 extends to544222 (gap chain5,4,4,2,2,2).

At an infinite visible trace,00000 absence supplies the next one; the preceding
one must not be the very first symbol for its forced prefix zero. Boundary
exceptions are the four other accepted flank pairs, not arbitrary transient
extensions. The rule uses three short/listed forbidden words plus word17,
and reduces compensation to one forced geometry. No assertion that544222
is actually realized, or that the language is now characterized. Next compare
this forced5-to-triple2 transition with kick phase/charge, rather than invent
an unconstrained branching choice. Full25 receipt ea0ae954 ACK; no census run.


#### GC986 — Recurrent or boundary-only compensation? (2026-10-10)

Missing inference: does the fullK18 relaxation confine544222 to an initial
transient, permitting a finite kick budget? Record searched: `RRL|RLK|544222|4,4,2,2`
AND `recurrent|SCC|transient` -> GC985 only. Prediction: a directed cycle
containing the4422 core survivesK18 (so transience fails). Counterfactual:
a relaxed periodic word is an actual right-half history or a prize obstruction.
Independent control: literal forbidden-substring checks, including wraparound,
versus prefix-suffix DFA. Unexpected check: also impose Local's absent word21;
it is beyondK18 and may kill the recurrence witness. Bound: finite automaton
only, no right-half enumeration or record sweep.

Outcome: prediction REFUTED. No core-bearing cycle exists in the144-state
prefix-suffix automaton, nor in the160-state variant adding word21. The
adaptive occurrence-counter product has148 reachable states; exact maximum
is1, achieved by the core itself. The computed potential V starts at0,
never exceeds1, and verifies V(next)>=V(state)+[core completed] on every
reachable edge. Telescoping proves at most one occurrence, including overlaps,
in every finite word avoidingK18, and therefore every actual visible trace.
This is an all-length motif budget, not a white-record bound or total kick
budget. Exhaustive literal/DFA controls through10 and all edge inequalities
PASS; reproducible probe rule30_rrl_core_budget.py. Local's forbidden-word
soundness is inherited; second reading of the new bound remains requested.
Next use the zero-budget recurrent language after this unique event to
compare actual kick-phase transitions, rather than charge repeated4422 events.


L560 receipt (d2ad67cd), after computation: Local reports actual absence of
word19 `0100001000100010101`. Together with GC985 this excludes every core
whose preceding flank one is noninitial. It gives a deadline, not necessarily
index0: core start<=5; a preceding one at0 has gap<=5, and no preceding one
allows at most4 leading zeros. Thus the actual visible suffix from index6
forbids the core. Inherited membership evidence, hand endpoint inference;
no spatial record bound. This is the next recurrent-language input.


#### GC987 — The4444 frontier: transient event or initial train? (2026-10-10)

Missing inference: whether four consecutive gap4 events have a finite budget,
or can recur after a reset. Record searched: `4444|4,4,4,4` AND
`budget|cycle|recurrent|transient` -> L559 only. Prediction: all-gap4 periodic
coding survives the known words, so an occurrence budget fails. Adaptive
structural target: word21 may force a4444 train backwards to the initial
boundary, excluding its rebirth after any other gap. Counterfactual: surviving
finite relaxation proves that periodic code is realized. Independent controls:
all exterior gaps2..5 with literal forbidden checks and DFA membership.
Unexpected check: the same missing word21 can allow an unlimited initial
train while forbidding its later restart. No record or language census.

Outcome: prediction HELD. Periodic code(1000)^infinity avoids all25 words,
plus words19 and21; literal wraparound control through48 symbols PASS.
It has infinitely many4444 occurrences, so these constraints alone cannot
bound their count. Eight direct-substring/DFA context controls PASS: preceding
gaps2,3,4 survive at the initial one, but with a preceding zero only4 survives.

Hand result (using Local's absence of word21): every maximal train of at least
four consecutive gap4 events begins at visible index<=4. If it has a preceding
non4 gap a,11/00000 give2<=a<=5. If its preceding one is noninitial, the zero
before that one excludes a=2 via010100010001 and a=3 via010010001. Gap5
places0000 before the train's first one and gives word21. Only a=4 remains,
contradicting maximality. Thus either no preceding one exists (at most4 leading
zeros), or that one is at index0 and a=2 or3 (train starts at2 or3). A previous
4 instead extends the same train backwards. Consequently there is at most
one such maximal train; after it ends,4444 never reappears. This does NOT
forbid4444 in every suffix from index5: the initial train may still be running.

This is a no-rebirth constraint, not a train-length or white-record bound.
The decisive next inference is whether actual dynamics permit arbitrary initial
1(0001)^n, or force a finite cutoff. A targeted membership query, not a longer
language census, would distinguish those alternatives. Request Local's lane
for that specific family; no GPT right-half/SAT computation started.


#### GC988 — Stabilized suffix after the two transient budgets (2026-10-10)

Received L563 (a0f08ffd):1(0001)^8 absent; n<=7 at index0, n<=6 at indices1..3,
n<=3 at index4. GC987 then puts the last possible4444 core start at12
(index0 train:4*(7-4)); indices1..3 give at most11. Thus every actual suffix
from index13 forbids4444 and4422 (latter deadline5, GC986/L560). L561's
independent window-automaton review of the at-most-once bound ACK, PASS.
Missing inference: do these two new recurrent restrictions force eventual
periodicity, or leave recurrent branching? Record searched: `RRL|RLK|4444|4,4,4,4`
AND `branch|entropy|component|eventually.periodic` ->8 hits, no stabilized test.
Prediction: a branching recurrent component survives; this direct eventual-
periodicity route remains insufficient. CF: all recurrent components simple
cycles would force every infinite suffix eventually periodic and directly
feed Jen under finite left support. Independent controls: literal wraparound
checks of both recovered cycles. Unexpected check: overlapping4444 cores
make the suffix cutoff13, not the initial train's final one at28.

Outcome: prediction HELD. Stabilized27-word automaton has152 reachable
states and a branching recurrent state0100100, with return words00100100
and100. They start with different bits; either return may be concatenated
indefinitely. Literal cyclic and mixed-concatenation controls PASS. Thus this
necessary suffix relaxation still admits non-eventually-periodic words; the
two transient budgets do not by themselves force eventual periodicity.
No realization of these loops in the actual visible language is inferred.
Retain cutoff13 as a sound finite warmup reduction; direct simple-cycle route
stalls at these explicit loops. Next seek actual compatibility of these return
choices, rather than extend generic quotient features or repeat entropy bounds.


GC988 continuation, preregistered obstruction check (2026-10-10): the residual
loops encode the existing G239 S/L neutral-gap subsystem (gaps3/5), not a new
physical branching claim. Predict every known forbidden word beyond11/00000
(including words19/21/33 and the two suffix cores) has an internal gap2 or4,
so none restricts this subsystem. CF: pruning our new transients closes the
remaining compatibility inference. Independent control:511 macro prefixes
through8 gaps; unexpected check includes length33 despite its long cutoff.
Outcome: prediction HELD, all511 literal controls PASS. Hand reason extends
it to every S/L word:11/00000 are absent in odd-gap3/5 codes, and every other
constraint requires a gap2/4. The new transient cuts leave the entire abstract
S/L subsystem. Its actual return compatibility is the old G239/GC614 gap;
no new physical family, entropy or record bound. Park further transient-pruning
variants here; Local's registered SOF computation targets actual follower states.


#### GC989 — Exact warmup control for the hidden-state diagnostic (2026-10-10)

Specific missing inference in L565's SOF-P4: age10 does not remove the known
4444 transient. Record searched: `SOF|sofic` AND `13|cutoff|startup|10` -> L565/
SOF registration, no cutoff control. Prediction: age12 still contains the core,
age13 excludes it;13 is the minimal cutoff for this motif. CF: age13 removes
all startup distinctions. Unexpected control: compare ages at matched suffix
lengths, not matched total initial lengths. No SAT run or complete census.

L563 realizes w=1(0001)^7, length29. Its suffix from12 is exactly the17-symbol
4444 core; hence L^(12) contains it. Dropping two initial observations first
makes the same occurrence start at10 in another actual white-start trace,
so L^(10) also contains it. GC988 excludes the core from L^(13). These hand
implications use factor closure and Local's reported realization/absence;
literal slicing controls PASS. Compare E10 from total length37 and E13 from40
at the common suffix horizon27. This corrects one known confound, not all
transients or a claim of regularity; follower-class counts need not decrease
when a language is restricted. Exact hidden-state closure remains open.


#### GC990 — Explicit discriminator for a phase/charge/window lift (2026-10-10)

Missing inference: can wheel phase, integrated visible charge and a short recent
window identify actual future states? Search for two equal-length histories,
equal number of ones and same last7 bits, separated by a continuation.
Record searched: `follower|hidden.state` AND `charge|same.phase|same.suffix`
->3 hits on G239/GC610, no matching explicit pair. Prediction: a pair occurs with histories length
<=12 and total length<=18. CF: failure proves that summary sufficient. U:
equal ones fixes any charge of the form A*ones+B*length, beyond phase alone.
Use fullK18's exact finite-language characterization, inherited from Local;
no SAT, right-half census or assertion of eventual-language membership.

Outcome: prediction HELD. Histories x=100001000 and y=010001000 are actual
length9 words, with2 ones and common suffix0001000; continuation z=01010001
makes xz actual (length17), yz absent via1000100001010001. Literal and initial-
DFA controls PASS; physical membership inherits Local's completeK18 list,
not fresh SAT. The histories differ in completed gap5 versus4; continuation
adds gaps5,2,4. Equal elapsed phase, any linear count A*ones+B*length, and
window7 therefore cannot merge these actual residual states. "Phase" here is
the nominal clock/unkicked rotation phase, a function of elapsed length;
no equality of fully kicked wheel phases or actual G248 charge is asserted.
No membership in E13 is inferred. Retain this pair as a concrete separation
control for a hidden-state candidate; it must preserve that older gap distinction
or an equivalent state. This does not prove a finite presentation exists.


#### GC991 — Hidden phases versus observed follower classes (2026-10-10)

Specific SOF decision defect: finite rising follower counts do not imply an
unbounded hidden counter; observer classes can exceed hidden phases.
Record searched: `sofic|follower|Myhill` AND
`powerset|subset|nondetermin|hidden.phase` ->2 PRIOR-ART hits on subset
construction, no explicit control for SOF. Prediction before computation:
an8-phase cyclic machine has255 distinct observed residual classes after8
symbols. CF: a phase-scale plateau is necessary for a finite phase lift.
Independent control: literal phase-path membership versus subset updates.
U: verify factor closure and zero extension, so this is a shift-language
control, rather than an end-marked regular-expression example.

Construction: phases q modulo h; every symbol advances q by1. At q=0 only0
is allowed; at other phases either bit is allowed. All phases initial.
This control is not a Rule30 presentation.

Outcome: prediction HELD; N(a,8) for a=1..8 is
2,4,8,16,32,64,128,255. Literal phase paths and subset transitions agree;
factor-closure and zero-extension controls PASS through length8.

Proof for every h: during h symbols each initial phase visits0 exactly once.
Placing1 at a visit removes that phase, independently of the others, so
every nonempty subset is reachable. Given a phase q, the continuation of
length h with0 exactly at q's visit to0 and1 elsewhere permits q alone.
It separates any two subsets differing on q. Consequently the minimal
deterministic observer has2^h-1 accepting residuals (plus the rejecting
state), although the hidden presentation has only h phases. Any allowed
finite path extends by zeros in both directions, proving factor closure
and two-sided extendibility without relying on the finite checks.

SOF implication: follower counts size an observer, not the underlying phase
lift. The proposed20..120 plateau is a prediction, not a necessary56-phase
bound. No finite rising scan establishes nonregularity or an unbounded
counter; a finite plateau likewise needs exact transition closure before
it certifies regularity. Retain sets of compatible hidden states when
projecting. Next useful step remains finding actual closed transitions,
using GC990's separation pair; this control adds no Rule30 record bound.


#### GC992 — Does gap order survive every additive gap charge? (2026-10-10)

Missing inference for the proposed phase/charge lift: do charge totals retain
the ordering information that actual futures need? Test equal-length actual
histories with identical complete-gap multisets, initial/trailing zeros and
last7 bits. This fixes every additive function of completed gap lengths,
including their parity sum; no fully kicked phase equality is presumed.
Record searched: `gap.*(multiset|histogram)|commut.*charge` AND
`follower|future|hidden|order` ->no hit. Prediction: histories plus a
separating continuation fit within exactK18. CF: no pair would establish
sufficiency (it would not). Independent controls: literal forbidden-word
membership versus prefix-DFA membership. U: preserve both endpoint zero
lengths, excluding an endpoint-only explanation. No new SAT or census.

Outcome: prediction HELD. x=100010100001, y=101000100001 have
length12, endpoints both1, suffix0100001 and complete-gap multiset{2,4,5}.
Their gap orders are4,2,5 versus2,4,5. The common future0001 gives an
allowed16-symbol xz and excluded yz, containing0001000010001.
Literal and prefix-DFA membership agree.
Actual finite membership inherits Local's completeK18 census.

Therefore every lift using only nominal elapsed phase, any collection of
additive completed-gap charges, both endpoint ages and window7 merges
two different actual future states. Even retaining the most recent complete
gap (5 in both) does not fix it. A candidate must keep noncommuting gap
order or equivalent hidden compatibility, not merely refine a scalar charge.
This is a finite necessary-state constraint, not an all-depth invariant;
do not extend these summary variants without a proposed closed transition
rule. Next target is such an ordered hidden-state rule beside the wall.


#### GC993 — Locate the ordered-gap distinction in a right-strip lift (2026-10-10)

Missing inference after GC992: which hidden right-strip compatibility
distinguishes gap orders4,2,5 and2,4,5? Use exact nondeterministic strip
states (columns1..k), arbitrary right boundary each step, wall0101.
Prediction before run: some k<=10 excludes y0001 while allowing x0001.
CF: accepting both in every tested strip proves physical equivalence (false).
Record searched: `100010100001|101000100001` AND `layer|column|hidden`
->GC992 only; width-layer method is established, not a new method.
Independent control: transition formula versus literal Rule30 table on all
local triples. U: continue each prefix from its full compatible state set,
never select a single arbitrarily fitted phase. Cap k=10; no SAT/census.

Outcome: prediction HELD, first separating strip width9. At width8,
compatible prefix-state counts are23/26 for x/y, and after0001 both22.
At width9 they are32/32, after0001 respectively17/0. All widths1..8
allow both extended histories. Thus an exact9-cell right-strip lift carries
this ordering distinction; an8-cell strip alone loses it. This is spatial
width, not an intrinsic minimum number of automaton states.

Probe rule30_hidden_gap_order.py independently verifies each whole-row
bitwise transition against the literal eight-entry truth table, split
continuation from full state sets, and projection into the narrower strip.
All controls PASS. Exact inclusion follows by projecting any genuine
right-half orbit and taking its exterior bit as the nondeterministic
boundary. Empty final state set therefore proves absence; nonempty strips
remain relaxations. Physical presence of x0001 still inherits Local'sK18.

This supplies a concrete ordered hidden representation, rather than a scalar
charge patch. Width9 is sufficient for this discriminator only; established
thin-layer failures bar extrapolation to an all-depth record bound. Keep
the full compatible right-strip set as a control for proposed synchronized
states. Next require transition closure combining synchronized history
with spatial compatibility, rather than another depth or width scan.


#### GC994 — Can an exact strip forget the ordered-gap distinction? (2026-10-10)

Missing inference for a finite ordered lift: whether a common admissible
continuation resets GC993's distinct compatible state sets. Search width9
only, pair-subset BFS capped at2000 nodes and marker length20. Prediction:
a nonempty common continuation merges the sets within20 symbols.
Record searched: `100010100001|101000100001` AND
`synchron|merge|reset` ->no hit. CF: equality in one strip proves
actual synchronization (false). Independent control: replay marker from
full initial sets versus continuation from each prefix. U: neither side
may die; empty-set equality is not synchronization. No width scan or SAT.

Outcome: prediction HELD. The shortest marker01 merges the two width9
compatible sets into exactly19 states; BFS visits6 pair states. Neither
side dies; full-prefix versus split-continuation replay agrees. Equality
then guarantees identical futures of every length in this strip model,
by its exact Markov transition rule.

Adaptive unexpected check: does this apparent reset survive the exactK18
language? No. Both x01 and y01 are actual14-symbol histories, but the
common continuation0001 is actual for x01 and absent for y01 by
1000100001010001 (total18). Thus even the entire compatible width9
state set, plus elapsed phase, fails as a sufficient hidden state of the
actual visible language. The exterior boundary's realizable history still
carries information after the strip observer has forgotten it. This is
a concrete refutation of width9 sufficiency, not of all finite lifts or
a synchronization claim about the actual language. It bars adopting
GC993's strip set as the whole lift. No further width variants proposed;
Local's actual synchronized followers must retain this post-marker
discriminator. Literal substring and strip replay controls PASS.


#### GC996 — What SOF/SW actually exclude (2026-10-10)

Specific defect: L570 and the map conclude no finite strip lift from a
finite width curve. Record searched: `strip.*width|w(n)` with
`unbounded|sofic|finite.*lift` ->5 hits; GC991/994 retain finite-scope
guards. Prediction for this proof audit: the transcript gives finite
lower bounds only. CF: measured growth proves unboundedness. U: count
nondeterministic hidden states separately from observer residuals.

Conditional on Local's exact census/strip verdicts, w(40)=35 excludes
every exact free-boundary strip of width<=34. It does not exclude width35
or greater, prove w(n) unbounded, or rule out a different finite lift.
The all-depth step would require arbitrarily large certified width needs.

SOF's N(a,l)=719 requires at least719 deterministic observer states for
the full language. An h-state nondeterministic hidden presentation has
at most2^h reachable subsets, each determining its exact future set.
Thus it requires h>=10, since2^9<719. The finite synchronizing-word test
cannot turn154 observed classes into a154-state lower bound for arbitrary
hidden presentations without further hypotheses. These are exact logical
bounds from reported counts, not fresh computation or unboundedness proofs.
This keeps the finite-lift route open; no further growth scan requested.


#### GC997 — Warmup must preserve the separating future, not just its history (2026-10-10)

L571 reports5/26 length13 predecessors of x01/y01 in L27 (GC995
history-survival prediction HELD). Missing inference: x010001 itself
must survive in E13 to establish distinct eventual followers. Membership
of x01 alone does not ensure that continuation; L31 suffices for a lookup.
Also test width9 using all strip states reachable after13 white macros,
rather than an unrestricted new initial state at that age.
Record searched: reachable-strip/warmup with GC994/E13/width9 ->3
ledger hits, no previous finite-reachability control. Prediction before computation:
the two warmed strip sets still merge and accept0001. CF: survival of
both histories proves eventual separation. U: flag the positive extended
word's L31 membership as pending, not proved by L27. Independent control:
full26-tick warmup versus13 macro updates. No SAT or width scan.

Outcome: warmed strip prediction HELD. Reachable white-phase strip states
shrink512,247,210,204,201,200,198 after0..6 macros. The198-state set
is a fixed point under the macro transition, so it is exact for every
strip age>=6. After reading x01/y01 from this set, both end in the same
19 states; after0001 both end in the same12 nonempty states. Removing
finite strip startup information therefore does not cure this false merger.
Tick-versus-macro warmup, fixed-point and whole-prefix controls PASS.
The first diagnostic failed while importing an AST fragment (undefined
t); no computed verdict resulted. Corrected fragment and rerun succeeded.

Actual eventual separation is still pending: L571 proves histories in E13,
not the positive extended word. Ask Local to check length31 suffix
100010100001010001 in its existing data; prediction before that lookup:
it survives. The negative extended word is globally absent and hence
absent in E13. Until the positive lookup, do not assert actual distinct
E13 followers. My GC995 wording was too strong; this corrects it.


#### GC998 — Exact spatial-row observer instead of a free-boundary strip (2026-10-10)

Missing inference: retain exterior compatibility that GC994's strip loses.
Represent the complete infinite right-row set by its regular, extendible
spatial prefix language. Observe its first bit, then take exact Rule30
spatial images with left boundary0 then1. This retains every right cell
symbolically; no free exterior is introduced at a fixed width.
Record searched: regular/sofic/automaton with right-row/spatial-image/
forward-image ->GC686 only, no such observer. This uses the established
regular-image construction, not a novelty claim. Prediction before the
prototype: it separates GC994's actual future pair within600 DFA states
and10 seconds. CF: matching short outputs proves finite global closure.
Independent controls: finite literal spatial images through length4,
against the eight-entry truth table. U: reject an observation with no
productive spatial continuation rather than accepting an empty prefix.
No SAT, right-half census, spatial width sweep or all-depth claim.

Outcome: compactness prediction REFUTED by the registered operation cap,
not by a language counterexample. Literal spatial-image and contradictory-
observation controls PASS. The first positive history's first macro yields
47 minimized spatial states; processing its second observation hits600
subset states before minimization. Neither full history was decided.
Source row states are productive; exact image states keep the previous
two source bits and source residual, with no final-boundary flush. Every
finite accepted output prefix has an infinite source continuation, so
the representation does not introduce a free boundary at fixed width.

Retain the prototype and stop cap increases. This is an exact symbolic
exterior representation, but eager determinization is already costly;
no finite global observer, regular visible language or record bound
follows. Next useful algebraic step would avoid that determinization
while preserving actual exterior relations; no larger run proposed.

GC997 receipt, L572: actual positive-continuation prediction REFUTED.
The extended word has no13-symbol predecessor in L31; the history pair
does not supply an E13 discriminator. Local also reports no5-symbol
predecessor in the complete L23 census (start positions0..4 throughout
the checked lengths). Factor closure then excludes every occurrence at
any age>=5: shift a putative later occurrence to age5. Thus this is an
all-age startup deadline for that word, conditional on the reported exact
census, not an all-depth record bound. Retain the failure; GC994 remains
a full-language obstruction only. No further variants of this startup
pair proposed.

## GC999 — Keep spatial nondeterminism rather than determinize (2026-10-10)

Missing inference: can an exact exterior representation process the
observations which stopped GC998, without replacing exterior relations
by a free boundary? Concrete target: advance the same actual-future
discriminator using nondeterministic spatial images and safe strong
bisimulation quotients. No higher DFA cap or strip-width scan.
Record searched: NFA|nondetermin + spatial|row -> GC993/996 and unrelated
hits; no existing iterated spatial NFA observer found.
Prediction: nondeterminism passes the second observation within3000
reachable image states and10 seconds; deciding both18-symbol histories
may still fail. CF: nondeterminism merely postpones exponential growth
and reaches the representation cap before a verdict.
Controls: compare literal spatial images of small restricted languages;
check a known two-symbol forbidden word as an instrument control.
U: a reachable finite spatial branch with no infinite continuation must
be removed, including any root which only reaches such branches.

Outcome: partial prediction PASS, verdict target unresolved.
Probe `rule30_spatial_nfa_observer.py` processes two observations exactly,
with16 then256 productive bisimulation classes after the two-step
images, before hitting3000 reachable image states on the next macro.
All literal-image, forbidden11 and dead-branch controls PASS. Unlike
GC998 this avoids powerset construction, but strong bisimulation does
not compress the observed growth enough. Neither18-symbol history
was decided. No all-depth bound or nonregularity conclusion follows.

The image keeps triples(previous bit,current bit,source vertex), with
one edge per source transition, labelled by the Rule30 truth table.
Root triples consume the first source bit; each output edge consumes
one more. Productive trimming retains exactly vertices with an infinite
path; quotient classes preserve each labelled successor-class set.
Thus every accepted spatial prefix retains an infinite preimage.
This is a hand construction with small independent controls, not a
second-reader certificate. Retain the cap failure; do not raise it.
The next missing ingredient is a quotient coarser than strong
bisimulation that still preserves exterior compatibility, rather than
further growth measurements. No new run proposed.

## GC1000 — Test an exact dominance quotient before further images (2026-10-10)

Missing inference: does GC999's state growth contain exterior languages
which are safely dominated, rather than merely bisimilar? Concrete target:
find a strict simulation inclusion among its256 second-observation states
and eliminate redundant nondeterministic choices. No larger image run.
Record searched: simulation|antichain + spatial|NFA|nondetermin ->
no corresponding spatial observer quotient (search output retained).
Prediction: forward simulation detects strict inclusions which strong
bisimulation missed. CF: no usable root/edge dominance exists, so this
cheap quotient does not relieve the retained bottleneck.
Control: a two-state binary/zero-only model has strict inclusion. U:
compare quotient acceptance exhaustively through spatial length8.
Run cap10 seconds; at most the existing256-state observer.

Outcome: prediction REFUTED. At16 and256 spatial states there are
zero strict simulation inclusions; pruning dominated root/edge choices
leaves16/256 states and2/8 roots unchanged. Strict-inclusion synthetic
control and exhaustive spatial words through length8 PASS.
The computation took less than a second; no larger images attempted.
Simulation uses the greatest relation q<=r for which every labelled
successor of q has an r-successor above it. It certifies language
inclusion by induction on spatial word length; finite productivity
ensures the represented prefixes have infinite extensions. Here it
provides no useful compression. Park this quotient along with cap
increases; no all-depth or nonsofic conclusion. Further quotient
variants need a new structural reason, rather than another generic
minimizer. Source: `rule30_spatial_simulation.py`.

## GC1001 — Cheap obstruction extraction for L573's first excess (2026-10-10)

Missing input: an actual absent factor from a new relaxed-record witness,
to seek a structural forbidden family rather than accumulate more depths.
L573 received at2b8d5882. Implement two monotone bisections on a
factor-closed membership oracle, extracting a minimal forbidden factor
with O(log n) queries. This uses the standard minimal-factor argument;
no new theorem or Rule30 absence asserted.
Record searched: minimal.*forbidden|absent.*factor +
binary.search|bisect|prefix.*suffix -> GC549, no bisection extractor.
Prediction: instrument returns absent words with both one-letter deletions
present; rejects UNKNOWN instead of treating it as absence. U: deliberately
return a minimal factor longer than the globally shortest absent factor,
so the output must not be labelled shortest. Synthetic controls only.

Outcome: synthetic minimality/query-bound/UNKNOWN/not-shortest controls
PASS (`rule30_minimal_obstruction.py`). First bisect an absent prefix;
then strip its longest present-start suffix boundary. Its proper prefix
is a factor of the already present shorter prefix, and its proper suffix
is present by the second search. No new membership calls or actual
forbidden words obtained. IMPORTANT: first query full witness membership;
a phase1 relaxed excess alone need not make its white-time word absent,
because the black-start prehistory can be the missing constraint
(GC549 checkpoint22). Do not feed an assumed-absent word to bisection.

## GC1002 — Black-start exclusions constrain every matured white trace (2026-10-10)

Missing inference for L574: can its phase-specific words strengthen
phase0's all-depth relaxation without an invalid initial prehistory?
Record searched: black.start|B(n)|phase.one + suffix|drop.*first|age.one|index.?1
-> GC1001 only; GC549 checkpoint22 read. Hand prediction: skip precisely
the first white-visible symbol, then every B-forbidden factor is sound.
CF/U: applying those exclusions at white-visible index0 is unsound;
L574's reported W-but-not-B word supplies that countercontrol.

Write W for white-start words and B for black-start words (first visible
sample one tick later). Any W realization sampled from its second white
observation has a preceding black tick: rebase at physical time1. Its
right row there is an admissible arbitrary initial row for B. Therefore
for every finite length n, E1(W)[n] is contained in B[n], which is
contained in W[n] by checkpoint22. No backward extension assumed.
For any B-forbidden word f, an occurrence in a W trace at visible index
s>=1 would, by this forward rebasing and B's factor closure, put f in B,
a contradiction. Thus phase0 can soundly forbid f at every position
s>=1; phase1 can forbid it also at0. This holds at every horizon, not
merely the computed cutoff.

Implementation consequence for the pending finite certificate: retain
W's forbidden list at all positions; add B's list after the first visible
symbol in phase0, and everywhere in phase1. Only a two-state startup flag
is needed to encode this extra necessary language condition. It does
not prove regularity of the actual language, a record bound, or that
these additional cuts suffice. L574's reported code
101010000100010001000010000 may occur at white origin only if it is
indeed absent from B; this uses Local's diagnostic, not a new SAT call.
Hand inference awaiting independent reading; no new run.

## GC1003 — Most matured phase cuts are already in the white cutoff (2026-10-10)

Missing inference in GC1002's proposed strengthening: which B cuts
actually add constraints to relax40 phase0? Record searched:
black.start|phase.specific|B.forbidden + redundan|left.extension|lookahead|cutoff
-> GC1002, no earlier cutoff comparison. Hand target: prove redundancy
below the frontier; CF/U: all B cuts, including length K, are redundant.

If f is absent from B, both 0f and 1f are absent from W: either would
place f at white-visible index1, contradicting GC1002. If |f|<=K-1,
these words have length<=K and therefore each contains a minimal
W-forbidden factor of length<=K (checkpoint21). Any occurrence of f
at index>=1 in a word surviving the complete W cutoff K would also
contain one of those preceding-symbol extensions, impossible. Hence
B cuts of length<=K-1 add NOTHING to phase0's matured constraints.
At K=40 only length40 B cuts or longer new information can strengthen
that phase; the shorter B list still matters at phase1 index0.

Frontier countercontrol: let W avoid011 and111, and B avoid11. Then
B subset W and E1(W) subset B, but f=11 survives the W cutoff2 and
occurs internally in011. The W cutoff3 eliminates it. This exact toy
language checks the one-symbol offset and rejects the stronger CF.
No Rule30 language computation or record claim. Hand inference pending
review; GC1002 remains sound, but do not implement redundant lower-length
phase0 cuts or restart old invariant runs on them.

## GC1004 — Seek a spatial explanation of the first black-start exclusion (2026-10-10)

Missing inference: why does L576's first B/W distinction,101010000,
require missing black prehistory? Seek forced initial spatial cells,
which could supply a structural language rule rather than more counts.
Record searched:101010000 + force|110|prehistory -> no prior forcing
explanation; use GC549 checkpoint22's impossibility of post-black110.
Prediction: every white-start realization of this word begins with
spatial110. CF: several initial three-bit patterns survive, so that
three-cell prehistory obstruction is insufficient.
Controls: literal truth-table update vs packed right-row update on small
cones. U: omit the last visible symbol and test whether forcing survives.
One bounded17-bit initial cone (131072 rows), no solver or depth sweep.

First outcome: prediction REFUTED. All512 compatible17-bit rows begin
100, not110; omitting the terminal visible sample still forces100
(384 compatible15-bit rows). Literal/packed controls PASS.
Follow-up within the same cone: identify the shortest spatial prefix
length at which EVERY compatible row lacks a black-wall predecessor.
Prediction: a finite length<=17 suffices; CF: the obstruction requires
infinite tail compatibility beyond this observed cone. U: compare the
predecessor automaton against literal finite black-image enumeration
through prefix length6. No larger cone.

Outcome: follow-up prediction PASS. Exhaustive finite-cone membership
is EXACTLY the spatial prefix cylinder10010001, with all512 nine-bit
tails allowed. Every compatible row therefore begins10010, whose
black-wall preimage is impossible already at five spatial cells.
For a black wall, output1=1 forces old cells1,2=0. Outputs2,3=0 then
force old cells3,4=0. Output4 equals old cell5, while output5 equals
old cell5 OR old cell6. Hence output4<=output5;10010 violates this.
This explains L576's first new exclusion through a concrete shielding
constraint, rather than merely repeating its language count.

Independent finite black-image enumeration through length6 agrees
with the predecessor automaton. Full-cone counts and packed/literal
updates PASS. The terminal visible sample is essential to prehistory
exclusion:10101000 has a black-reachable spatial row
100110000100000. Counts are COMPUTED; the five-cell impossibility is
a hand proof. No all-depth record bound follows, and no longer word
scan proposed. Next useful target is whether other B obstructions
admit similarly small forced spatial witnesses, when a specific
record-excess model needs explanation. Independent reading requested.


## GC1005 — Black prehistory: a rooted family and an exact forgetting prefix (2026-10-10)

Missing inference: can GC1004's spatial obstruction supply persistent
exterior information for the hidden-state invariant? Seek its all-length
form and check whether black prehistory can instead lose all tail constraints.
Record searched: black.wall|black.start|prehistory +
10010|010|arbitrary.*tail|universal ->26 hits, GC1004 and older reset
results; no surfaced claim of this rooted family or black-image forgetting.
Prediction: every spatial prefix1 0^k 1 0 (k>=0) is impossible after
one black-wall update. CF: the family is also forbidden internally.
Independent control: literal truth table on source pairs, rather than
packed cone updates. U: test whether output prefix010 leaves EVERY
source pair possible, permitting arbitrary output tails. No depth scan.


Outcome: prediction holds by hand. Write a_0=1 and
 y_i=a_(i-1) XOR (a_i OR a_(i+1)). Output y_1=1 forces
(a_1,a_2)=00. From source pair00 an output0 keeps the pair00;
the first subsequent output1 changes it to01. From01 the next output
is forced1. Thus1 0^k 1 0 is impossible for EVERY k>=0.
GC549's110 and GC1004's10010 are k=0 and k=2. An infinite
output1000... remains possible (all source cells zero); no mandatory
return to black follows. These are rooted SPATIAL statements, not
visible temporal forbidden factors.

The unexpected check supplies an exact limitation. In the four source-pair
NFA, start set A={10,11}. Reading010 gives successively
 {01,10,11}, {00,10,11}, {00,01,10,11}.
The full four-pair set maps to itself under EITHER output0 or output1:
read this directly from the literal table(0,1,1,1,1,0,0,0).
Consequently EVERY infinite spatial word starting010 has black-wall
prehistory. Each finite prefix has a source path; the finitely branching
source-path tree has an infinite path. This includes arbitrary internal
occurrences of1 0^k 1 0, refuting the stronger CF. Literal controls
through k=11 and the all-pair transitions PASS; the proof has no cutoff.

Implication for the proposed hidden representation: black prehistory
constrains the spatial origin, but after reading010 this one-update
constraint forgets all tail restrictions. It cannot furnish an internal
spatial forbidden-factor language, even after enlarging k indefinitely.
Retain temporal compatibility across multiple alternating updates;
do not build another spatial-factor relaxation from this family.
This limits one specific proposed ingredient, not all finite hidden lifts
or the actual B temporal language. Hand proof pending independent reading;
no record bound or prize claim. Next: analyze a concrete excess witness
with its multi-time exterior relation when Local supplies one.


## GC1006 — Fixed past alone cannot constrain the remote spatial tail (2026-10-10)

Missing inference: could replacing GC1005's one-update past by a fixed
number m of alternating wall updates supply internal spatial cuts?
Record searched: prehistory|past.depth|past.horizon|image.*half +
surject|full.shift|arbitrary.*tail|boundary.*distance ->2 hits, GC608
return-image discussion; use established left permutivity, not a new
surjectivity claim. Prediction: for every fixed m and prescribed wall
history, the projection of its right-row image onto cells m+1 onward
is the entire binary shift. CF/U: this remains true after fixing the
observed prefix; GC1004 should refute that strengthening. Hand block,
no computation or observer-cap increase.

Proof: any finite output block on the whole line has a preimage under
Rule30. Choose the two rightmost source bits arbitrarily, then solve
successive source bits from right to left using left permutivity.
Compactness gives a preimage of any infinite whole-line target, and
iteration gives one under m updates. Extend any desired right tail
on cells m+1 onward to a whole-line target and choose such a preimage.
Restrict the source to positive cells and evolve with the prescribed
wall at column0. The final outputs at i>=m+1 agree with the whole-line
evolution because their initial cones lie entirely at positive cells.
Thus the remote-tail projection is full for every m. For finite target
blocks a finite source truncation beyond their cones suffices as well.

Unexpected guard: fixing the origin destroys the conclusion. At m=1,
fixed output prefix100 forces output4<=output5, so tail10 is impossible
(GC1004); without that prefix both symbols are allowed arbitrarily in
the projected tail. Therefore this theorem does NOT remove correlations
between the observed origin and the exterior, or exclude fixed-width
proofs retaining that relation. It excludes only unconditional internal
spatial cuts derived from a fixed wall past. Retain the conditional
origin/exterior relation; no record bound follows. Hand proof pending
review. Next useful block must address that relation, not increase past
horizons to seek unconditional spatial forbidden factors.


## GC1007 — Does the new cutoff40 remove mixed S/L recurrence? (2026-10-10)

Missing inference: whether L578's stronger finite language eliminates
GC989's surviving recurrent 3/5-gap branching, so that established
periodic-tail exclusions could become relevant. Record searched:
K.?40|relax40|771 + S/L|renewal|branch|3.*5|gap.*language ->16 hits;
GC989 covers cutoff18, no surfaced cutoff40 gap-cycle test.
Prediction: a recurrent component still has two distinct S/L choices.
CF: every recurrent component is a single cycle, so only eventually
periodic S/L tails survive. Control: list counts771 and832 plus the
seven length<=10 words. U: require survival under BOTH phase lists,
not just white-start. One finite graph from published lists, no solver,
record-depth scan or larger language enumeration.


Outcome: prediction HOLDS, including the unexpected both-phase check.
Parsed W=771, B=(W minus246) plus307=832; seven-word control PASS.
At black markers use S=001 and L=00001 (gap lengths3 and5).
The exact forbidden-prefix automaton for the UNION of both lists has
252 reachable marker states. Entry LSLSL reaches residual
1000010010000100100001. Two return loops at that SAME residual are
 A=SLLLSLSL and B=LLSLSL.
Both return exactly and neither encounters a forbidden word. Arbitrary
concatenations of A and B therefore survive both cutoff40 languages
at ALL lengths, not merely through the finite census horizon. Their
distinct first gap makes the choices distinguishable. Independent
literal substring checking of all32 five-loop concatenations PASS.
Reproduction: tests/probes/lexicon/rule30_sl40_branch.py (under0.1s).

This is a regular relaxed-language witness, NOT an actual realization
of its infinite words, nor evidence of unbounded R_real. It shows the
new phase-correct cutoff still cannot reduce the 3/5-gap subsystem to
only eventually periodic tails. Applying established periodic-tail
exclusions alone cannot finish that subsystem. Do not infer that a
record potential on this branching language is impossible. The new
information needed is either a potential that handles these cycles,
or an actual-history invariant separating their arbitrary concatenations.
L578's two complete lists supplied this test; follower/width tables
were not recomputed. No extension of the language cutoff proposed.


GC1007 next inference, registered before any actual membership call:
q=1000010010000100100001 is actual in BOTH phase languages by the
complete length40 data. Its two relaxed return extensions are
 qA=10000100100001001000010010000100001000010010000100100001 (56),
 qB=100001001000010010000100001000010010000100100001 (48).
Predict at least one is absent from an actual phase language; CF both
are actual, leaving concatenation compatibility unresolved. Control q
is present by the existing census; U compare W and B membership, because
initial black prehistory can matter. Request only these two targeted
memberships per phase from Local when existing jobs permit; no language
growth or sweep. No verdict yet. A missing extension would identify a
specific exterior constraint for the invariant, rather than another
state-summary variant. The attempted loop support-cost argument stalled:
return to the visible residual does not give return of the forced left state.


GC1007 bounded forcing attempt, predictions before execution:
Missing inference: can every infinite concatenation of the two new
loops be excluded by initial black cells forced at growing left depths?
Record searched: SLLLSLSL|LLSLSL|GC1007 + forc|support|left -> GC1007
and its unresolved support-cost attempt, no forcing test. Prediction:
at least one initial black cell beyond depth44 is common to all eight
three-loop choices. CF no common black cell beyond the entry cone.
Use GC709 c_1=1-q, c_0=t mod2 and the exact inverse recurrence,
where q marks visible1s at even physical times. Eight finite cones,
left depths1..180 only, no actual-right or all-depth claim. Independent
literal Rule30 truth-table check on every reconstructed triangle.
U inspect common cells beyond depth120, where all first loop choices
have already influenced the reconstruction. This is a forcing search,
not an enlarged strip observer or a record census.


Forcing outcome: prediction HOLDS. Beyond entry depth44, the common
initial black depths are45,47,58,69,71,73,74,79,83,84,87,93,96,
112,125,132,136,146. Unexpected beyond120 check also HOLDS.
Each of the eight finite traces supplies at least199 physical samples;
initial inverse depths<=180 cannot depend on any later continuation.
Thus EVERY infinite concatenation in this explicit loop family forces
an initial black cell at depth146, irrespective of subsequent choices.
If J denotes the deepest initial black cell left of the wall, this
family requires J>=146. This is an exact finite forcing certificate,
not an all-depth growth law or a right-half realizability claim.
Literal Rule30 checks PASS for every triangle, independently of the
inverse implementation. Reproduce rule30_sl40_forcing.py (under0.1s).
Do not extrapolate the finite common cells. Missing next inference:
an analytic mechanism producing unbounded forced depths for arbitrary
loop choices; no longer-horizon scan is registered.


GC1007 analytic continuation attempt (no further computation): rebase the
146-cell forcing at later loop returns to seek increasing initial support.
This does not work. Rebased forcing gives c_146(t)=1 at a later time,
not an initial black cell at a deeper site. Its backward cone includes
initial cells to the RIGHT of -146 as well as to the left, so finite
initial support can supply it. The visible residual return does not
remove those ancestors. Retain this failure; do not pump the finite
certificate by time translation. A useful growth lemma must track an
initial-row obstruction or a conditional diagonal invariant.


GC1007 whole-subsystem check, registered before execution: the chosen
pair of loops is only a diagnostic subset; excluding it would not finish
all mixed recurrence. Missing inference: is the entire persistent S/L
part small enough for a direct return-state invariant? Predict one
branching strongly connected component with at most64 marker states.
CF multiple branching components or a larger one. Use only the existing
252-state graph under BOTH cutoff40 lists. Independent control: check
mutual reachability inside each reported component. U distinguish
simple periodic components from the branching component. No new language
or cone scan; search cutoff40|GC1007|771 + component|SCC|recurrent.*graph
found no earlier whole-component classification for this gap graph.


Whole-subsystem outcome: the size prediction is REFUTED (79>64), but
there is exactly ONE recurrent component, containing79 marker states,
38 with two internal successors. The other173 components are singleton
acyclic states; there is no separate simple periodic component. The
chosen loop root lies in this sole recurrent component. BFS mutual
reachability checks independently confirm its connectivity; the probe
now reproduces the classification. Hence the proof target for this
relaxed S/L subsystem is the full79-state recurrent relation, not just
the selected two-loop subset. No actual hidden-state sufficiency or
all-depth record potential follows from this finite visible quotient.
No expansion of the alphabet or new state-summary variant proposed.


## GC1008 — Affine pulse closure fails on valid renewal prefixes (2026-10-10)

Bounded analytic lead beyond GC709 (no longer support scan): could
all S/L-renewal initial left bits be affine functions of the pulse
samples q, allowing a linear closed lift? Record searched: S/L|renewal|
gap3|gap5|pulse.*train + linear|Rule.?90|Rule.?60|parity|renorm|even.shift
->67 hits, GC709 supplies only the first four columns; no all-depth
linearization asserted. Prediction: affine pulse closure fails by
left depth32 on actual 6/10-gap pulse prefixes. CF every tested depth
has an affine formula (still no all-depth proof). Enumerate only valid
gap prefixes through physical time31 and solve their finite affine
consistency equations; no actual-right claim or record-depth scan.
Control literal Rule30 inverse triangles. U seek an explicit even-sized
XOR dependency of pulse prefixes whose reconstructed bit has odd XOR;
that is a hand-checkable nonlinear obstruction, not a failed fit.


Outcome: affine closure fails at depth26. Thirteen distinct valid pulse
prefixes through time31 suffice; depths<=25 admit an affine fit on
this finite collection, without an all-depth claim. A four-cylinder
counterexample already proves the failure at26. Pulse times through25
and reconstructed c_26(0) are respectively:
 {0,6,16,22}:1; {0,6,16}:0;
 {0,10,16,22}:0; {0,10,16}:0.
These are SLS,SLL,LSS,LSL gap prefixes; all extend to infinite valid
6/10-gap pulse trains. Their four pulse vectors XOR to zero, and
there are an even number of vectors, but their c_26 bits XOR to1.
No affine combination of ANY pulse samples through25 and a constant
can produce c_26 for this renewal domain. In this four-cylinder slice
it is exactly the interaction q(6) AND q(22): the order before the
shared pulse at16 changes the effect of the next short gap.

Literal Rule30 triangle controls and the explicit XOR dependency PASS.
Reproduce rule30_pulse_affine_obstruction.py (under0.1s). This closes
the proposed causal affine-pulse lift, not nonlinear finite representations.
It does not assert actual right realization of all four prefixes.
A successful lift must retain this ordered interaction; no expansion
of the linear fit or another support-depth scan proposed.


GC1008 actual-history scope check, registered before execution: the four
pulse prefixes use 13 visible symbols (physical times0,2,...,24).
Predict all four belong to BOTH actual phase languages, using L578's
complete minimal-word lists through40, rather than a new solver run.
CF at least one is absent, restricting the obstruction to renewal syntax.
Record searched: GC1008|1001000010010|1000010010010 ->7 hits;
GC709 ->7 hits, confirms q is the right-visible pulse while c_j names
LEFT columns. Control reproduce the seven W forbidden words through10.
U check terminal dependence: c_26(0) uses q through25, but q(25)=0
is forced at the black wall time; no extra visible sample at26 is needed.
This checks a specific scope gap in the proposed hidden lift, not a new census.


Scope outcome: all four visible words1001000010010,1001000010000,
1000010010010,1000010010000 are IN both W and B by L578's complete
minimal-word lists. The W-through18 list has the independent enumeration
control already recorded by Local. Thus GC1008's nonlinear obstruction
occurs on actual right histories, not merely syntactically allowed renewals.
The decoded columns c_j are LEFT columns; q is the right-visible bit.
Terminal check: to determine c_26(0), c_1 needs samples through25;
at odd25 it is forced1 independently of the right cell. Right visibility
through24 suffices. Extend the clamped wall to26 and use inverse uniqueness
to supply left sites-1 through-26, zero beyond; truncate the initial right
row beyond its finite cone. Each prefix therefore has a finite full-row
completion maintaining the wall through26. This asserts four finite
completions, not their arbitrary infinite concatenation or a record bound.
Seven-word parse and literal triangle controls PASS. No larger fit proposed.

L579 ACK: q,qA,qB are actual in both phases; GC1007's predicted negative
is REFUTED. Local's positive queries do not identify a hidden return state.
Do not request longer arbitrary concatenations solely to postpone that gap.
Next necessary ingredient is a nonlinear relation propagated across a whole
return cone; visible automaton return and affine pulse closure both fail as
stand-alone substitutes. Preserve the explicit depth26 ordered interaction.


GC1007 bounded closure test, registered: does its full79-state recurrent
S/L component exceed the certified actual visible entropy ceiling0.1236?
If so, the whole component cannot be actual and needs an exterior restriction,
even though qA/qB pass. Prediction it exceeds; CF it lies below, leaving
this argument unable to distinguish actual closure. Record searched:
GC1007|79.state|S/L + entropy|spectral|growth ->44 hits; existing channel
ceiling and selected loops, no whole79-component comparison. Use exact
rational positive-vector inequalities at z=109/100, whose log2 exceeds
0.1236; an upper certificate instead at z=108/100 puts it below the ceiling.
Control root residual loop lengths34/26. U account elapsed visible lengths
3/5 on edges, rather than counting one symbol per gap. No language scan.


Outcome: prediction HELD. At z=109/100 the exact weighted adjacency
M has entries z^-3 for S and z^-5 for L. Set v=M^11(1); all79
coordinates satisfy Mv>v, checked in rational arithmetic. Also
109^2500 > 2^309*100^2500, so log2(z)>0.1236 without rounding.
The irreducible component therefore has spectral radius above1 at z.
Its path generating series has exponential visible-word growth above
log2(z): S=001 and L=00001 are uniquely decodable between markers,
so different paths from a fixed state spell different words. Reachability
from the initial marker adds only a fixed prefix. Thus if EVERY path
in the full79-state component were actual, it would contradict the
certified actual visible entropy ceiling0.1236 (§8.20/8.33).
Consequently at least one finite extension in this component is NOT
actual, despite all its factors passing both cutoff40 lists and qA/qB
being actual. Actual factor closure and completeness through40 imply
such an extension contains a new minimal absent word longer than40.

This is an unconditional obstruction to whole-component actual closure,
not to the selected two-loop subsystem (whose growth is smaller), and
not to finite weighted representations generally. It supplies no record
bound or location of the missing restriction. Control exact loop lengths
34/26, direct concatenation checks and SCC connectivity PASS. U omitting
elapsed edge lengths would compute the wrong entropy. Reproduce
rule30_sl40_entropy_obstruction.py. Next structural target: the exterior
restriction removing paths from this component, not further verification
of isolated positive concatenations. No new solver job requested.


### GC1007 follow-up — the guaranteed missing restriction is an interior factor

Missing inference: can the entropy obstruction be confined to startup,
so a finite warmup repairs the full79-state lift? Hand prediction no;
CF only an initial-prefix exclusion is needed. Record searched:
GC1007|79.state + startup|interior|factor ->2 hits, no localization proof.

Fix any state of the recurrent component and consider words spelled
entirely by paths inside it. Their entropy is the same irreducible
weighted entropy certified above. If all those words belonged to W,
the actual W word counts would violate its ceiling. Choose one absent
word and a minimal absent factor f inside it. Every internal path avoids
the entire cutoff40 list, so |f|>40. Actual W is factor-closed: f is
therefore forbidden at EVERY visible position, not just the origin.

Unexpected delayed-placement check: strong connectivity lets us reach
the path containing f from q; first repeat a q-return loop arbitrarily
many times. All resulting words still pass cutoff40, and f occurs
arbitrarily late. Thus no fixed warmup after which the entire unmodified
79-state relation is allowed can be sound. This does not exclude a
smaller recurrent relation, a nonlinear lift, or depth-dependent weights.
Independent control is the established factor closure of W (L578);
without factor closure the inference from an absent initial word to an
interior ban would be invalid. No new experiment or larger cutoff run.
The required hidden relation must impose a recurrent exterior constraint.
Its explicit form and record-bounding strength remain unknown.


GC1007 finite witness bound, registered: replace the qualitative missing
interior cut by a finite upper length bound, using the same positive vector
and §8.33/SQ6's uniform word-count prefactor. Predict a bound below10000
visible symbols; CF larger, making direct search impractical. Record searched:
count|prefactor|finite.*bound + EN6|SQ6|0.1236 -> existing135663
channel prefactor, no finite bound for this SCC. Use conservative C=1000000
and b=1.0898 for |W_n|<=C*b^n, safely above SQ6's rounded growth/prefactor.
Exact control b^10000>2^1237 (0.1237 exceeds the printed0.1236 ceiling's
rounding interval). U bound a sum over all lengths, not a single edge count,
since S/L edges cost different numbers of visible symbols. No word census.

First finite-bound attempt REFUTED the practical prediction: v=M^11(1)'s
minimum one-step ratio is too close to1 to beat the geometric actual
count bound within10000 gaps (50000 visible symbols). This is weakness
of that vector's uniform ratio, not absence of a finite cut. Bounded
repair registered: use v=M^79(1) on the SAME79-state graph, then exact
powers of its minimum ratio. Predict a bound below10000 symbols; CF
still too large. No additional language states or solver queries.


Repair outcome HELD: v=M^79(1) gives an exact minimum ratio r>1;
a=v(q)/max(v) satisfies a*r^1024 > 1000000/(1-b/z), with
z=1.09 and b=1.0898. These are rational inequalities, not floating
fits. Since 1>=v/max(v), the total z^-length weight of1024-gap
paths from q exceeds that entire upper bound for actual words.
Gap codes are uniquely decodable; paths spell distinct words, each
of length at most5120. SQ6's reported prefactor135663 is safely
below1000000 and its four-decimal0.1236 entropy below0.1237;
integer powers check log2(b)>0.1237. Thus the actual-word sum
is bounded by sum_n C*(b/z)^n=C/(1-b/z). At least one internal
path is absent from W and contains a minimal absent factor with
length41..5120. This is a finite existence bound for the missing
recurrent restriction, not its explicit discovery or a record bound.
The first vector's impractical bound remains recorded; no brute-force
search through this length is proposed. Verification reuses the79-state
graph and the independently established SQ6 ceiling.


L581 lift defect check, registered before testing: right_half_for returns
initial sites1..last but its last visible sample depends on1..last+1.
Predict a one-symbol white-start word returns an empty dict, incorrectly
reported ABSENT by the caller; a black-start control loses site2 and
fails replay. CF the existing slice already retains the whole cone.
Control independent literal two-cell Rule30 update; U a zero last cell
can mask the omission, so use a model with last cell1. This defect blocks
the pending lift; no real solver run needed.


L581 defect outcome HELD: phase0 single-symbol1 returned{}, so caller
reported ABSENT despite SAT. Phase1 single-symbol0 dropped source
cell2=1; full-row replay fails after dropping it and passes retaining it.
Fixed extraction to include initial site last+1 (2k-1+phase). Direct
simulation already prevented false positive record claims; this repair
prevents false absence/invalid-witness conclusions. Also distinguish
UNSAT exit20 from all other non-SAT exits (UNKNOWN raises rather than
being reported ABSENT). Solver-free AST/mock fixtures and independent
literal phase1 update PASS in rule30_lift_controls.py. No new SAT run.


L581 repaired-cone reasoning block: missing inference is whether matching
only WHITE-time right bits suffices for the pending full-row lift.
Prediction yes through the stated T, CF an extra tick is automatically
covered. Record searched: lift|glue|gluing + terminal|last|horizon ->107
hits; use the existing wall equation, not a new gluing theorem.
Inductively assume the glued centre matches the clamped wall through t.
Left cells see the same centre boundary; right cells see the same wall.
At white t the actual right cell equals the retained visible code; at
black t the OR term is1 independently of that cell. Hence the relaxed
centre update is reproduced for every t<T, and the initial white band
is unchanged. The repaired source cone includes every last-visible
ancestor. This unblocks the lift's intended validity test.
Unexpected horizon control: initial cells0=0,1=0,2=1 pass the T=0
white-start word0, but centre stays0 at t=1, violating the next clock
bit. Matching the last visible sample does not license T+1. Keep the
reported horizon exactly as directly simulated; no record extrapolation.


L582 negative-code block registered: extract a minimal actual exclusion
from its retained phase1 word using the existing complete W/B lists,
without another SAT call. Predict a B forbidden factor of length17..40
accounts for the K16 failure; CF no published factor, needing the full
retained model/oracle. Record searched: the exact word|L582 ->new
negative-control entry only. Control no factor of length<=16, since
the relaxed model satisfies K16. U check literal copied word length
against L582's stated41 before interpreting the cone or asking for work.


L582 outcome: copied length41 is correct; no B factor of length<=16.
Exactly one published minimal factor appears in each phase list:
W:010000101000010001 (length18, visible index3, physical start7);
B:10000101000010001 (length17, index4, start9). The W factor
is exactly0 followed by the B factor. Therefore this negative lift
is caused by an INTERIOR restriction, not merely black startup.
The minimal W factor excludes this visible word from either phase;
its proper prefix and suffix are actual by the published census.
No oracle calls are needed to extract the explanation. It is an
already-known K18 cut, not a new cutoff40 obstruction or record bound.
This closes analysis of the smoke negative; retain the method for
the pending actual d152 model rather than expanding this example.


GC1007 bounded potential attempt (hand, no experiment): missing inference
is a pathwise white-run charge from the new pressure vector. Prediction
the branching-sum inequality does not supply that charge; CF it expands
every individual history. Record searched: GC1007|pressure|positive.vector
+ individual.*path|record.*potential|branch.*sum ->one graph-source hit.
For an edge define its normalized contribution z^-length*v(next)/v(now).
Mv>v concerns the SUM of these contributions. On the explicit A return
loop their product is exactly z^-34<1; on B it is z^-26<1, because
the vertex weights telescope. Thus uniform pathwise expansion is false
even within the diagnostic recurrent family. Unexpected control: repeated
loops retain this failure for arbitrary elapsed time, not merely one edge.
The pressure vector locates missing language restrictions but supplies
no white-run compensation budget. Stop promoting it to a record potential;
the next constructive target is the actual exterior constraint exposed
by a retained failed lift, while independent work must retain left-state
information. No new pressure fits, state-count variants or solver runs.


L583 bounded proof block: missing inference is whether a relaxed record
excess could arise solely from incompatibility of its left row with a
right realization of the WHOLE visible code. Predict no, using the
previously established simulation-gated gluing implication; CF the code
could be actual despite the reported real upper bound. Record searched:
last.*visible|terminal.*visible + lift|glue ->4 hits; read Relaxed.vis.
For d107,L16,phase0,T122 the code contains exactly61 samples, at
times0,2,...,120. A right realization supplies precisely all required
white-time updates, so it would glue to a finite row holding the wall
through122 and retaining the16-cell white band. This contradicts the
reported R_real(107)=14. Therefore EVERY such relaxed model's code is
absent, and avoiding the complete K40 list puts its shortest absent
factor in41..61. This is solver-backed via RR3's upper bound, not a new
checked UNSAT proof or an all-depth bound. No new computation.
Unexpected endpoint check: no observation at122 is included or needed;
requiring it would incorrectly use62 samples. Independent phase-count
control: phase1,T122 also uses61 samples, at1,3,...,121.
Local's announced extraction now has a concrete guaranteed short target;
no additional job, cap increase, or Cloud request is needed.


L584 explanation block registered: missing inference is which retained
right-cone information makes the length46 word impossible. Test only
truth-table domain propagation on its exact finite cone. Prediction:
individual-cell domains stall, so correlated alternatives are essential;
CF propagation produces a contradiction and a short forcing explanation.
Record searched: propagation + forbidden ->4 hits; existing GC371
arc-consistency instrument read. Controls: forbidden11 must contradict;
f[:-1],f[1:] must not. Unexpected check: literal simulated right rows
for all16 four-cell seeds must never contradict their observed words.
No SAT, cutoff extension, or duplicate Local CUT run.

Outcome: propagation stalls with4071 of4277 cone cells unresolved;
prefix/suffix deletion controls and forbidden11/literal-seed controls
PASS. The exact cut cannot be explained by this unary-domain closure;
retain correlated alternatives, rather than extending this forcing scan.
A second scope check is exact: f contains10001, a gap4 between ones.
Every S/L path in GC1007 has only gaps3 and5. Hence adding this particular
cut changes NONE of that79-state recurrent subsystem or its two loops.
It genuinely repairs the d107 relaxation (L586), but does not supply the
missing recurrent restriction located by GC1007. No all-depth bound.
Next proof target remains correlated exterior information; this forcing
approach to f is closed, without asking Local for another census.


L584 affine-relation block registered: test whether shared XOR equations
resolve f where unary domains failed. Keep each exact Rule30 gate and
propagate its affine consequences through a global GF(2) basis, at most
8 passes. Prediction: still OPEN, because disjunctive correlations survive;
CF a derived contradiction yields an algebraic explanation to inspect.
Record searched: Gaussian|parity.reason|XOR.propag + forbidden|cone ->
one unrelated Mahler-cone hit. Controls:11 contradicts; both deletions
and16 independently simulated seed words remain consistent. Unexpected
check: a three-equation parity cycle must contradict without unit inputs.
This is sound inference, never an OPEN=>SAT test; no solver or census.

Outcome: f reaches a fixed point on pass3 with rank250, without a
contradiction. Deletions reach ranks243/246; all controls PASS. Thus this
exact-gate/global-affine inference system also loses information needed
for the obstruction. No cap increase would change its fixed point.
Retain the failure and stop this explanation route; adding more forcing
passes or treating the affine space as the actual right histories cannot
help. Future invariant work must preserve nonlinear alternatives.


SLC prerequisite check (L587): the registered P4 asks whether an actual
cut kills a pure S or L cycle. Record searched: SLC|GC1007 + pure|periodic|branch;
read GC686 and L380's actual84/155-cell rings. Prediction: P4 is already
ruled out by those certificates; a pure-power cut signals an error.
Use literal ring updates as a solver-independent gate, solely because
this live prediction conflicts with an established construction. Control
both full temporal periods and all visible rotations; unexpected control
flip the wall bit and require failure. No new ring search or SAT call.

Both existing ring certificates and all rotation/mutation controls PASS.
Every finite factor of (001)^infinity or (00001)^infinity is actual in
both phase languages: rotate the orbit to the appropriate white time,
or start one black tick earlier. Thus SLC-P4 is structurally refuted
before SLC outcomes; both pure cycles MUST survive every sound cut list.
They may split into separate SCCs; their survival does not force mixed
branching. This is a guard from existing results, not a new orbit theorem.

The exact useful SLC success condition is no internal branching in ANY
reachable recurrent SCC of the rebuilt graph. For an actual eventually
S/L trace, shift to an internal renewal marker with a preceding black
tick; its suffix belongs to both phase languages and avoids all sound
cuts. It gives an infinite path from the marker root. The finite SCC DAG
allows only finitely many component changes; a recurrent component with
internal outdegree1 is a cycle, so the S/L tail is eventually periodic.
GC706 then excludes finite initial left support. This would close the
entire eventually-S/L subclass, not just the selected A/B loops. It would
NOT cover actual histories with infinitely many other gap lengths or
settle the all-period prize. No branch-free certificate exists yet.


SLC recurrent representation block registered: identify exactly what
leading/trailing zeros in a binary cut mean in the S/L gap alphabet.
Prediction: at interior markers, 0..2 padding zeros impose no gap
restriction, while3..4 require an adjacent L; internal distances3/5
become S/L. This would express each recurrent binary cut as one macro
forbidden factor without discarding nonlinear word context. CF startup
and finite terminal positions obey the same rule. Record searched:
leading|trailing + S/L + forbidden|cut ->no hit. Controls: exhaustively
compare cyclic spellings up to6 macro letters and binary factors through
length16; unexpected check rooted1001 lacks001001 despite containing S.
This is a representation check, no actual-language membership queries.


### GC1009 — Checked S/L cuts expose startup-only and gap-2 entry constraints

Status: PROOF-SKETCH (new hand consequences of Local's checked cuts;
not independently second-read). Serves Q6 / GC1007's recurrent restriction.
L590 at e2be768c supplies the following W-forbidden words, each length42:

    f1 = 010010010000100001001001000010000100001001
    f2 = 001001000010000100001000010010000100001001

Local reports cake_lpr VERIFIED UNSAT for both, and simulated right halves
for both proper one-symbol deletions. Those receipts are Local's; no
membership solver was rerun here. W denotes white-start visible words,
sampled every two wall ticks. It is closed under taking factors; 11 is
forbidden. Write u=f1[1:] (length41), v=f2[2:] (length40).
Record searched: startup.only|entry.only|left.extension + S/L|length42|length.42
-> no hit. Missing inference: what prior visible context is necessary for
these actual deletion words, and how does that constrain recurrent S/L?

1. **u is actual but startup-only.** L590's suffix control realizes u.
If u occurred at positive visible index, its preceding bit would be 0
or 1. The first gives f1; the second gives 11 since u begins with 1.
Both are impossible. Thus no actual W history contains u except at index0.
Let F be the right-half map obtained by the white then black wall updates.
Every right row whose next41 visible bits are u lies outside image(F):
a predecessor row would contribute a bit followed by u. This is a precise
origin-conditioned prehistory exclusion, compatible with GC1006's
surjectivity onto unconditional remote spatial tails.

2. **v requires a gap-2 entrance after startup.** At an occurrence starting
at index s>=2, the bit at s-1 must be 0 (11 forbidden). The bit at s-2 must
be 1 (otherwise f2=00v occurs). Hence the context is 10v: the initial 1
of v follows the preceding 1 at distance2. Inside a persistent S/L segment,
where successive ones are at distances3 or5, v therefore cannot start at
an internal marker whose preceding marker is already in that segment.
The exact startup exceptions are real: 0v is L590's simulated suffix, and
v its factor. They must not be discarded from the initial W language.

**Macro interpretation.** In a bi-infinite S/L spelling, a cut's internal
distances3/5 translate to S/L; leading or trailing0..2 zeros add no
restriction, whereas3..4 zeros require an adjoining L. Any other internal
distance or padding>4 makes occurrence impossible. The cases with no 1
are immediate: one/two zeros occur universally, three/four require L,
five cannot occur. Thus the two recurrent forbidden macro factors are
SSLLSSLLLS and SLLLLSLLS. This is an occurrence equivalence for recurrent
spellings, with startup and finite-terminal padding explicitly excluded.

The registered representation control passes35658 comparisons of direct
cyclic binary spelling against macro-factor detection (all macro periods
through6, binary factors through16). New exact-cut controls check the two
translations and enumerate the one/two predecessor bits: no predecessor
of u survives, and only10 precedes v without already containing11 or f2.
The unexpected rooted1001/001001 control confirms that blindly applying
the recurrent translation at startup would remove a legitimate boundary
case. Local's actual u and0v witnesses are independent countercontrols to
such blanket bans. Script: tests/probes/lexicon/rule30_sl_macro_cut.py.

These cuts remove specific mixed transitions; they neither remove the
actual pure S/L cycles nor prove eventual periodicity of all mixed tails.
The finite certificates still supply f1/f2's absence: the prehistory
argument explains their boundary consequences, not their original
Rule30 impossibility. The missing main-line inference remains a structural
restriction strong enough to bound all admissible histories at every depth.
Next: retain these origin-conditioned exclusions when constructing the
hidden transition relation; no more unary/affine forcing or duplicate SAT.


### GC1010 — A correlated prehistory constraint survives the S/L marker

Serves GC1009/Q6. Missing inference: does the spatial marker1110 itself
erase the two-update prehistory restriction, so only the initial marker
could explain GC1009's startup-only word? Prediction: no; counterfactual,
every tail following1110 admits that prehistory. Record searched:
1110|marker + prehistory|preimage|image.F -> GC608 only relevant, on a
six-tick return rather than this image. After obtaining the explicit
prefixes below, their string search found only unrelated substrings.

**Hand inference (PROOF-SKETCH).** Let F be white then black wall updates.
Every output of F starting11 starts1110, but **1110110 is impossible**.
Write the intermediate right row b. Final11 forces b1=b2=0,b3=1.
Because b has a white-wall predecessor x, b1=b2=0 force x1=x2=x3=0;
b3=1 then forces x4=1 and hence b4=1. Thus final bits3,4 are1,0.
If final bit5 is1, b4=1 forces b5=b6=0. If final bit6 is also1,
then b7=1, forcing final bit7=1. This proves the seven-cell exclusion.
It is additional to black-only prehistory: the literal intermediate
prefix00101000 maps under a black tick to1110110, but cannot follow a
white tick. At any recurrent short marker11101 this gives the necessary
spatial relation: bit6=1 implies bit7=1. No temporal gap is thereby banned.

**Exact exterior representation, computed.** Conditioned on output1110,
the source starts0001, with every farther source bit free. After reading
that marker the source-window states are01??. Subsequent spatial outputs
are the radius-two table
h(a,b,c,d,e)=f(f(a,b,c),f(b,c,d),f(c,d,e)), f(a,b,c)=a XOR(b OR c).
This 16-state source automaton preserves all correlations, with48 reachable
subset states. Its shortest rejected tail is110. Direct literal two-tick
images through output length10 agree with the automaton at every word;
this is a finite control, not the basis for an infinite extrapolation.
The construction itself is exact at every length; compactness supplies
infinite preimages when every prefix has a source path.

**Limitation located, not a new horizon scan.** Reading tail0101010 from
01?? reaches all16 source states, with sizes4,5,7,9,10,13,13,16. Both output
symbols preserve that full set. Consequently every spatial row beginning
11100101010 has F-prehistory, whatever its remaining tail. The unexpected
unconditional control also preserves all16 states, as GC1006 predicts.
Thus the correlated relation is real but this particular finite-past
constraint can forget it even after fixing the marker. A useful invariant
must retain observed temporal history when updating this representation;
F-image membership alone cannot explain all recurrent cut restrictions.
No claim that1110110 explains f1's absence; that connection remains open.
No larger past-depth sweep or duplicate membership solver is proposed.
Code/registered controls: tests/probes/lexicon/rule30_marker_prehistory.py.


GC1009 follow-up, before the finite word check: the necessary predecessor
10 of v is incompatible with the established W-forbidden word101001,
because v begins1001. Predict v cannot occur at visible index>=2 even
outside S/L; its prehistory depth is exactly one macro, since Local's
actual0v supplies one. Countercontrol: v must remain allowed at index1,
and u at index0. Unexpected check: the formal predecessor10 from GC1009
is necessary but is not an actual extension. Record searched:101001 +
prehistory|startup|length.?42|f2 -> two unrelated hits.
No new actual-membership query or solver run.


### GC1011 — The second S/L cut has exactly one macro of allowable prehistory

PROOF-SKETCH, strengthening GC1009 using the already checked base word
101001. Keep f1=0u and f2=00v as there; v begins1001.
GC1009 proved that an occurrence of v at visible index>=2 requires10
immediately before it. But10v begins101001, impossible in W. Hence:

- u occurs only at visible index0.
- 0v occurs only at visible index0.
- v occurs only at visible indices0 or1, with index1 actually attained
  by Local's simulated0v witness (L590).

This is unconditional in the visible language, not restricted to S/L.
If C(w) is the set of right rows producing the finite visible prefix w,
then C(u) is nonempty and disjoint from image(F), whereas C(v) intersects
image(F) and is disjoint from image(F squared), for the white/black map F.
These are exact temporal prehistory layers, unlike the unconditional
remote-tail projection of GC1006 or the marker-only forgetting of GC1010.
The four possible two-bit predecessors of v all fail:01 and11 contain11,
00 gives f2, and10 gives101001. Independent positive boundary control is
Local's actual0v; the finite string check deliberately retains it.

**Age-aware cut compression, exact.** In any binary word already avoiding
11 and101001, imposing f1 at every position is equivalent to forbidding
u at positions>=1; imposing f2 at every position is equivalent to
forbidding v at positions>=2. The reverse directions follow by restoring
the deleted leading zeros; the forward directions are the predecessor
cases above. Thus this length42 recurrent obstruction has a sound
length40 form after two visible samples (four physical ticks). It must
not be added unguarded to the startup W40 list: v is actual there.
This does not strengthen a relaxation already containing the original
cuts, but identifies exactly which age information their longer words
encode. The recurrent S/L macro factor SLLLLSLLS is excluded regardless
of the earlier gap type; GC1009's putative gap2 entrance is itself dead.
No claim about all other longer cuts or finite convergence follows.
The all-depth record bound remains open. Next structural target: distinguish
such bounded-age exclusions from restrictions surviving arbitrarily long
actual prehistory; no cutoff expansion or new solver job requested.

L591 arrived at publication: its checked length81 cut also has form0z
with z starting1, and its simulated suffix z is actual. Thus z is another
startup-only cylinder, now length80. Small prehistory age does not by
itself make the temporal condition short. No minimality claim for z in
the aged language, or stabilization of its finite cutoff, is inferred.
Local's61 S/L cuts leave positive measured entropy~0.1192; the branch-free
certificate remains absent. Continue structural work without duplicating
its CUT/SLC runs.


GC1010 structural follow-up registered: classify its48 reachable subset
states after removing the empty and universal states. Missing inference:
can the marker-conditioned exterior relation be represented by finitely
many phases and simple waiting counters? Prediction: every remaining
recurrent SCC is a simple cycle; counterfactual, a branching SCC retains
arbitrarily long spatial ambiguity. Check SCCs independently by mutual
reachability; unexpected control checks that label transitions preserve
complements, since the radius-two rule is left-permutive. No increase in
past horizon, strip width, language cutoff or actual membership calls.
Record searched: marker|1110 + subset|synchroniz.*automaton|nonuniversal|prehistory.*cycle
->18 hits; G236/CL044 already supplies the exact16-state image
construction and forced0001 premise. Read before this follow-up. The
new target is the complete proper-residual SCC structure, not that
established construction; GC1010 and GC1011 should cite G236 for it.


### GC1012 — Marker prehistory retains branching at arbitrary spatial distance

COMPUTED / PROOF-SKETCH. The registered simple-cycle prediction fails:
GC1010's46 proper nonempty residuals form recurrent SCCs of sizes6 and40,
with4 and30 internally branching states. Independent mutual reachability
agrees with the SCC partition; complement transitions also agree, as
left permutivity predicts. This does not exclude another representation;
it rules out simplifying this exact relation to transient paths and
simple repeated words.

A short all-length certificate uses the initial residual A={4,5,6,7},
where integers encode four source bits. Both words p=000 and q=11101110
return A to itself, while r=110 sends A to the empty set. The p path is

    A -> {8,9,10,11,12} -> {1,2,3} -> A.

The q path is

    A -> {13,14,15} -> {10,11,12} -> {4,5,6,7,8,9}
      -> {1,2,3,8,9,10,11,12} -> {0,2,3,4,5,6,7,8,9}
      -> {0,1,13,14,15} -> {1,2,3,10,11,12} -> A.

The r path is A -> {13,14,15} -> {10,11,12} -> empty.
Consequently EVERY spatial prefix1110 w 110, w any concatenation of p/q,
is impossible after the two wall updates. Conversely1110 followed by
any infinite concatenation of p/q has prehistory: every finite prefix
has a source path, so compactness supplies an infinite source row.
This is a rooted spatial image statement, not a temporal S/L realization.
Both chosen cycles stay proper; origin information can survive arbitrarily
far with arbitrary choices between the two blocks. A fixed maximum
forgetting distance is therefore impossible despite GC1010's particular
forgetting word. No further fixed-past graph census is warranted: future
work needs its interaction with the temporal observation constraints.

**Prior-art correction and receipts.** The expanded record search surfaced
G236/CL044: the16-state transducer, forced0001 source premise and first
farther-site exclusions were already established there. Credit those
rather than treating GC1010's construction as new. The complete48-state
analysis and these two return words extend that checkpoint. CL185 now
independently confirms GC1010's hand exclusion1110110 and source premise;
its automaton/forgetting conclusions were not reviewed. CL185 also checks
GC1009's original predecessor cases; GC1011 adds the101001 obstruction.
No extra review or computation requested from Cloud.


TG all-length guard registered (CL185/L592): missing inference is whether
pure2-gap trains are actual at every length, beyond Local's length200.
Use the already established period4 seven-ring from RULE30-PRIZE sections5
and8.3, not a larger train scan. Record searched: period.?4|period.four|2.gap
+ ring|periodic.point|infinite.train -> existing seven-ring and CL088.
Prediction, informed by those results: extract one four-row orbit with
column0=0101 and white-time column1=10; it certifies every train length.
Counterfactual: the existing ring has the wall but another visible code,
so this construction cannot answer TG. Controls: literal and packed ring
updates agree, orbit closes exactly, both clock phases rebase correctly.
Unexpected check: truncating the periodic row has only a finite light-cone
guarantee; do not claim a finite seed keeps the wall indefinitely.
Only128 candidate seven-bit rows, solely to extract the existing witness.

### GC1013 — TG all-length guard from the existing seven-ring

PROOF-SKETCH / exact finite certificate, single-party. Bears on Q6: a
pure 2-gap train cannot supply a forbidden-word cut, at any length.
This applies the already recorded period-4 seven-ring (RULE30-PRIZE §5;
CL088's periodic-point census), rather than introducing a new orbit family.
With sites numbered 0..6 from left to right and repeated spatially, the
following four rows cycle under Rule30:

    0100110 -> 1111101 -> 0000001 -> 1000011 -> 0100110.

Each arrow is seven literal local updates. Column0 is0101; column1 is1100,
so column1 at white times is (10)^infinity. Starting at the fourth row
instead gives a black-start clock with the same code beginning at its
first white time. Thus (10)^n is actual in both phase languages for EVERY
n, answering CL185/L592 without extending their finite membership scan.
For any finite horizon T, copy the periodic initial row on [-T,T+1] and
put zeros elsewhere. Finite propagation preserves columns0/1 through T,
so every finite code also has a finite configuration witness. The seed
may depend on T: no finite-support eternal clock follows.

The committed `rule30_two_gap_ring.py` checks all four arrows both
literally and by independent packed updates, both phase rebasings, and a
finite truncation control. All PASS. Unexpected check: a single isolated
seven-cell copy does not return after four ticks; periodic extension is
essential to the infinite witness used here.

**CL186 distinction.** Eternity for the particular finite clamped right
half1001 is a separate question, not needed for this guard. If that seed
were to fail later, its failure would NOT make (10)^(m+1) forbidden: the
periodic witness above still realizes it. Finite right support and finite
support on both sides are also different conditions. No additional
finite-seed scan is requested; the main proof target remains mixed-context
compatibility and its effect on the forced left white run.

Temporal coupling block registered (GC1010 with GC629): missing inference
is whether exact marker prehistory restricts the next S/L return beyond
its first spatial exclusion1110110. Compare GC629's sixteen short-entry
prefixes11101abcd with the exact two-update image, then classify SS/SL.
Record searched: 1110110|mature.*short|mature.*gate + S|short|gap -> GC1010,
GC629 and G236, no joint gate table. Prediction: farther prehistory removes
at least one additional assignment after excluding ab=10. Counterfactual:
all twelve remaining prefixes have prehistory, so this finite gate adds
nothing beyond the known exclusion. Controls: direct truth-table image
and the existing transducer agree; direct visible outputs match GC629.
Unexpected check: retain an excluded startup prefix's valid forward SS/SL
trace, distinguishing lack of past from lack of future. At most2048 source
prefixes, no solver, no fixed-past graph census or larger-width follow-up.

### GC1014 — Prehistory removes three more short-return gate branches

COMPUTED / PROOF-SKETCH; single-party. Bears on Q6: couple correlated
exterior memory to the actual S/L return gate, rather than count spatial
image states. Let a current white-time right row start11101abcd and have
at least one full white/black update pair of past. GC629 gives its first
return S and its next return SS or SL from a,b,c,d. Exact past compatibility
of this nine-cell prefix is equivalent to

    a implies b;   b implies (a OR c);   c implies (a OR b OR d).

Here compatibility means existence of SOME farther tail and predecessor,
not that every continuation of the prefix has a predecessor. Equivalently:
for ab=00 require c<=d; for ab=01 require c=1; ab=10 is impossible;
ab=11 allows every cd. The nine admitted assignments give six SS and three
SL prefixes under GC629. These counts are not transition probabilities.
GC1010's1110110 removes only ab=10; the registered prediction HELD:
0010,0100,0101 are three further excluded abcd assignments.

There is a short all-length explanation of these extra exclusions. In
G236/GC1010's exact two-update spatial transducer, after marker1110 the
residual is A={4,5,6,7}. Reading1 gives B={13,14,15}; reading0 preserves B;
reading1 then gives C={10,11,12}, and reading0 empties C. Thus

    11101 0^k 10 is impossible after a full update pair, for every k>=0.

For k=0,1,2 this rejects1110110,11101010,111010010. Within the sixteen
nine-bit short-entry prefixes these reject exactly the seven listed above;
independent literal images of all2048 eleven-bit sources confirm that each
of the other nine has a predecessor. This is a necessary local restriction
on every mature S entry; it does not classify its longer future.

**Unexpected control and consequence.** G239/GC609's established prefix
111010010 realizes SL with arbitrary farther tail, but it is startup-only:
it has NO full white/black past. Its forward freedom therefore cannot be
reused at an internal return. This does not retract G239, which explicitly
did not claim independently repeatable choices. Other SL prefixes survive,
so neither SL nor a recurrent S/L cycle is excluded by this result alone.
The script `rule30_mature_short_gate.py` independently compares literal
images, the exact transducer and the Boolean criterion, checks GC629's
forward returns with three distinct tails, and verifies the four residual
identities proving the infinite family. All controls PASS. A record search
for111010010/11101010 finds G239's startup example but no past restriction.
Next missing inference: propagate the surviving exterior relation through
successive S/L returns; do not treat these nine cylinders as independent
choices or infer a record bound from their counts.

Short-return closure test registered: GC1014 gives the infinite necessary
family11101 0^k 10. Missing inference is whether retaining this whole
family, rather than only its nine-cell consequences, closes a hidden
state under an S return. Prediction: it does not; a startup row satisfying
the family returns in six ticks to forbidden1110110. Counterfactual: no
such cylinder through13 cells; that is inconclusive for longer targets,
not proof of closure. Record searched: 1110110|11101.*0^ + return|invariant|
pullback|closure -> GC1010/1014, no return-closure test. Enumerate at most
256 completions after11101, retaining an early11 that certifies membership
in the entire family relaxation independently of the unexamined tail.
Controls: literal and packed six-tick updates agree; an exact image-F
prefix cannot produce the forbidden target. Unexpected check: initial
nine-cell gate passes even for a failing longer cylinder. Stop on a concrete
failure; no width sweep, no solver, no automatic cut-list expansion.

The length13 test found no target1110110; prediction not established.
Bounded adaptation: decide the ENTIRE regular family under six-tick S
return, using an exact spatial transducer of memory12, not a width sweep.
Track input11101(0*11 anything OR all zeros) and output111010*10.
At most20000 product states; cap means unknown. Prediction remains a
counterexample; if the exact reachable product has none, closure under S
alone is proved, with L explicitly untested. Independent literal replay
of a found cylinder, including all last-cone completions, is required.

### GC1015 — Whole short-entry family loses past information despite return closure

REFUTED sufficiency; Q6 hidden-representation block. The registered
closure test found no length13 witness; the exact six-tick product then
exhausted1542 states without one. This is NOT a new invariant theorem:
any forward iterate already lies in image(F), so GC1014's image-necessary
family is automatically regenerated. The prediction overlooked this
simple inclusion. Stop that return-closure search; its success cannot
certify that the abstraction retains the past.

A concrete separator resolves the relevant sufficiency question instead.
The spatial prefix1110111110 satisfies the ENTIRE family condition
excluding11101 0^k 10: after its fifth bit its next two bits are11, so
no farther extension can break that rooted condition. It also passes all
three nine-cell gate implications (abcd=1111) and emits SS. Nevertheless
it has NO full white/black predecessor. From A={4,5,6,7}, its remaining
six symbols111110 take the exact residuals through

    {13,14,15} -> {10,11,12} -> {4,5,6,7,8,9}
    -> {0,13,14,15} -> {1,10,11,12} -> empty.

Independent literal enumeration of all4096 twelve-bit sources confirms
absence. The first nine symbols do have a predecessor, for example the
source000111000011 produces that nine-symbol prefix. Three different
farther tails replay the valid forward SS control. All checks PASS in
`rule30_short_family_guard.py`. Exact-word record search found no prior
hit. This is a spatial hidden-state separator, not a forbidden visible
word or a new S/L cut. Both this rejected-past cylinder and its admitted
nine-cell prefix have the same initial visible SS behavior.

Thus even an infinite family plus the next-return gate loses information;
closure under actual evolution does not repair that loss. Keep the full
correlated exterior relation when composing observations. No larger
family census, maturity-depth sweep or additional Local solver task is
justified by this block; the record-bounding potential remains missing.

Weighted inverse-column block registered: test the proposed local drift
Z(d+3)<=Z(d)+1, where Z(d) counts initial physical times when both columns
-d and1-d are zero. Such a drift would supply a depth-dependent zero-domain
budget; it is stronger than a global linear bound. Missing inference is
whether the budget is locally monotone. Record searched: zero.*prefix|unary
+ three.step|3.step|drift|potential|rank -> RRL/G5, no such drift lemma.
Use the already certified seven-ring first, before any language scan.
Prediction: the local drift fails even on that actual orbit; counterfactual
all seven spatial phases pass, leaving the general claim undecided.
Independent control: literal inverse-column reconstruction must match the
explicit ring. Unexpected check: any failure is actual at all horizons,
so strengthening a finite visible forbidden list cannot remove it.
The first time origin passes: Z on seven depths is0,1,0,0,0,1,0.
Before any larger search, complete the same orbit control at its other
three time origins; the proposed inequality has no time-origin restriction.

### GC1016 — Actual periodic control rejects uncorrected zero-domain drift

REFUTED candidate; serves RRL's depth-dependent potential, not a new
record census. The proposed Z(d+3)<=Z(d)+1 fails on the existing seven-ring
at time origin2 (still a white-start0101 wall): Z across depths0..6 is
1,0,0,1,2,3,2. In particular Z(2)=0 and Z(5)=3. Spatial period7 repeats
this violation at every d=2+7j, so discarding finitely many shallow depths
cannot repair this local drift. It does not refute a global linear bound.

The first time origin passed, as retained above; all four origins and
literal inverse-column reconstruction now pass independent checks in
`rule30_zero_drift_guard.py`. This is an actual all-time orbit, so adding
sound visible forbidden words cannot remove the counterexample. A
potential of the form 3Z-d+phi, required to be nonincreasing every three
depths, must compensate by at least 6
between the two named states; phi cannot depend only on the original
clock's colour, which is the same at both depths here. No larger
scan is needed. This particular weighted candidate needs a compensating
state distinguishing the two configurations; zero-prefix length with
the proposed uncorrected drift is insufficient. No all-depth bound
or necessity of infinitely many hidden states follows.


### GC1017 — Two-gap train: correlated forcing of its six-column boundary (2026-10-10)

Registered before controls; informed by a hand derivation, not a blind
prediction. The missing inference is which exterior data can affect a long
train's exit. Target: prove the six-column slab seen in CL186 is forced by
the train, without assuming temporal periodicity of the exterior.
Record searched: `train|2.gap` + `forced.*six|six.*forced|slab|0100`;
CL186 supplies the observed slab, GC1013 its periodic witness; the wheel
and S/L slab results concern different visible words.
Prediction: three short overlapping local deductions force the slab.
Independent control: enumerate the free Boolean variables in each deduction
using the literal Rule 30 truth table. Countercontrol: removing the second
column's prescribed observations must admit other values. Unexpected check:
the conclusion must force only one phase of column 7, not assume that
column's whole temporal word is periodic. No SAT membership or record run.

**Outcome: hand proof, second reading pending.** This is forced structure,
not just the orbit seen from seed 1001. Write x_j(t) for site j. Suppose
x_0(t) = t mod 2 through time 4N and its white-time neighbour reads
(10)^N1, with N >= 4. For every cycle n = 1,...,N-3 the six sites 1,...,6
at times 4n,...,4n+3 are respectively

    100110, 111101, 000001, 000011.

Moreover x_7(4n) = 0. The right exterior need not be periodic.

Proof. Each white-time triple 1,0,1 forces the full column-1 segment
11001: a 1 at a white wall time forces the next value 1, and the final
1 requires both inputs to the OR at the preceding black wall time to
vanish. Work in local time modulo 4, using
x_j(t+1) = x_(j-1)(t) XOR (x_j(t) OR x_(j+1)(t)).

A. Column 1 equal to 11001 first forces column 2 to a,b,0,0. If b=0,
the column-2 equation at time 1 forces x_3(1)=1. Its equation at time 2
forces x_3(2)=0, whereas the column-3 equation at time 1 forces
x_3(2)=1. Hence b=1. The column-2 equation at time 0 now forces a=0
and x_3(0)=0. Thus column 2 is 0100 in every complete cycle.

B. Use columns 1 and 2 through the first two times of the next cycle:
110011 and 010001. The column-2 equations give column 3 as 0,d,0,0,0.
Then x_4(0)=d and d OR x_4(1)=1. The column-4 equation at time 0
gives x_4(1) >= d; together these force x_4(1)=1. Also x_4(2)=0,
while its own equation at time 1 gives x_4(2)=1 XOR d. Therefore d=1.
Finally x_4(3)=0. Columns 3 and 4 are 0100 and 1100.

C. Use those two columns from time -1 through time 5. The column-4
equation at time -1 forces x_5(-1)=1. Its own next two updates give
x_5(0)=1 and x_5(1)=0. The column-4 equations at times 2 and 3 give
x_5(2)=0 and x_5(3)=1. The column-5 equations now give x_6(1)=1
and x_6(2)=1. The column-6 equation at time 0 forces x_6(0)=0
and x_7(0)=0; at time 2 it forces x_6(3)=1. This proves the slab.
For the finite endpoints, A applies to cycles 0,...,N-1; B to
0,...,N-2; C to 1,...,N-3, exactly the stated range.

The slab's four transitions can also be read in the forward direction.
Starting from its first row, it persists for a cycle if and only if
x_7 is 0 at phase 0; its other three phases do not enter any of these
six updates. Thus the interior train has an exact correlated boundary:
column 6 is the period-4 wall 0111, and column 7 must be white at that
wall's white times. Compatibility of this boundary with the entry and
exit remains necessary; arbitrary column-7 words are not claimed actual.
This reduces the exterior interface, without proving forgetting, finite
right-seed eternity, or an all-depth record bound.

Controls in `rule30_train_slab.py` PASS: literal truth-table enumeration
leaves 3, 4 and 12 local patches for A, B and C, all satisfying the
conclusions. Dropping the prescribed second-column observations admits
counterexamples in each case. The four slab transitions match exactly
the single phase-0 exterior condition. Unexpected check: C permits all
four local pairs of column-7 values at phases 1 and 2; no periodic
exterior was silently imposed. This does not assert their global extension.


GC1017 continuation, registered before the return-gate calculation.
Missing inference: does the reduced condition x_7(4n)=0 propagate from
one cycle to the next, or what correlated exterior pattern breaks it?
Compute the exact four-tick first-cell output on 0abcd beside 0111;
this has only sixteen inputs and no membership solver. Prediction:
zero is not invariant for arbitrary a,b,c,d. Countercontrol: deleting
the exterior dependence would incorrectly certify all sixteen inputs.
Independent controls: literal truth-table shrinking cones versus packed
right-half updates with zero and one padding. Unexpected check: the
last cone bit may be relevant only under a specific earlier-bit guard.
Record searched: `0111|q.?=.?.?3|p.?=.?.?4` + `white|hole|latch`;
G16 and the OHC strip are relaxations with fresh exterior input per tick,
not this exact four-tick cone. This is a gate calculation for the train
interface, not a new one-hole census.

First outcome: the sixteen cases give next x_7 = (NOT a) AND
(NOT b) AND (c OR d). Only 00001, 00010 and 00011 break the next gate.
Before extending: test whether this one-cycle eligibility domain is
itself preserved. This is a finite closure obligation on nine source
cells, not a longer seed run. Prediction: it fails; a surviving first
cycle does not guarantee the second. Counterfactual if all 256 pass:
the gate would supply a finite invariant and must receive an independent
check before use. Retain an explicit failure, if found, and stop there.

### GC1018 — Exact train-interface return gate, with nonclosure witness

Hand identity, independent local controls passed; second reading pending.
Let H be four right-half updates driven by the wall 0111, and suppose
the first five cells on its right are 0abcd at the white phase. Then

    H(0abcd)_1 = (NOT a) AND (NOT b) AND (c OR d).

Consequently the next train-interface gate fails exactly on prefixes
00001, 00010 and 00011. This is a spatial condition at the reduced
boundary, not a forbidden visible word beside the original clock.

Proof by cases, using the Rule 30 formula. After two ticks the first
cell is NOT(a OR b), and the second is (NOT a) AND (b OR c).
After three ticks the first cell is a. If a=1, the fourth tick makes
it zero. If a=0 and b=1, the first three cells after two ticks are
0,1,0, so the next first two cells are 0,1 and the final first cell is
zero. If a=b=0, the first three cells after two ticks are 1,c,c OR d;
the next first two are 0,NOT(c OR d), giving the displayed formula.

The eligibility domain is **not invariant**. The explicit shrinking
cones are

    011010000 --H--> 00010 --H--> 1.

The source passes one return but fails the next. Of the 256 nine-cell
sources beginning in zero, 39 have this failure. Thus the slab plus
one valid return does not supply a finite certificate of persistence;
the exterior correlations must survive composition. Stop this closure
candidate here, without a wider prefix sweep.

`rule30_train_return_gate.py` checks all sixteen cases using the literal
truth table and independently with packed updates under both zero and
one padding. The last cone bit matters on 0000d, the unexpected guard.
For a control in the original clock, append the witness to the prepared
slab 100110. With either tested far-tail padding, column 7 first fails
the required sample at time 8 and the original visible train fails at
time 16, within GC1017's implied deadline 20. This confirms the
interface's orientation and phase; it is not an absent-word claim.
Next substantive input is a constraint inherited from an actual mixed
entry that rules out, or accounts for, these return failures.


Train-interface timing block, preregistered. Missing inference: whether
a failed reduced gate has a fixed visible consequence, rather than only
a finite deadline. GC1018's two examples suggest an eight-tick delay.
Prediction (informed): from prepared slab 100110, the white-time trace
through time 8 is 1010 followed by NOT(x_7(0)), for every actual exterior.
Test the eight possible source bits at sites 7..9, the complete eight-tick
cone. Independent control: packed updates under two farther paddings.
Countercontrol: a six-tick delay must fail. Unexpected, stronger check:
replace the actual exterior by all 256 independently prescribed eight-tick
column-7 streams; if this fails, retain the extra exterior correlation
instead of silently using the stronger statement.
Record searched: `train|two.gap|2.gap` + `exit|delay|latency`;
GC1018 has two time-16 examples, no uniform transfer statement.

### GC1019 — Exact train-exit delay and the finite seed in Question 2

Hand finite-case proof, controls passed; independent reading pending.
From prepared sites 1..6 = 100110 at a white wall phase, let g be
column 7 at that time. Allow every later column-7 input independently.
Column 1 through time 7 is always 11001100, and at time 8 it is NOT g.
The following sound domain table proves this: each ? is an independent
unknown, and each row follows from the previous by the local rule.
The wall starts white; after time 0 the exterior input is arbitrary.

    time       g=0       g=1
      1      111101    111100
      2      000001    00001?
      3      000011    00011?
      4      100110    10110?
      5      11110?    1010??
      6      0000??    001???
      7      000???    011???
      8      10????    010???

Consequently, if the first failed phase-0 interface sample occurs at
time 4m, the first departure of column 1 from 1100 occurs exactly at
time 4m+8. Prior successful gates return the slab every four ticks
(GC1017); the table applies at the first failed gate. This is a
universal propagation statement, not an empirical delay estimate.

**Question 2 application (owner explicitly assigned this question).**
The finite right seed 1001 reaches the exact finite row 10011001 at
time 4. Remove its first six cells. The remaining initial right half
is 01000..., a single black cell at its site 2. Drive it by 0111
repeating and call its orbit y. Then Question 2 is equivalent to

    y_(4n)(1) = 0 for every n >= 0.

Proof: while these gates hold, GC1017 maintains the six-cell slab,
so its column-6 boundary is precisely 0111 and the two right halves
agree. If the first reduced failure is at time 4m, agreement holds
through that sample and the original column first fails at absolute
time 4m+12 by the table. If no failure occurs, induction maintains
the original train forever. The original first four ticks are
checked directly from the seed. This is an exact fixed-seed reduction,
not a proof of eternal survival or a replacement by the periodic ring.

`rule30_train_exit_delay.py` verifies the domain table, all 256 freely
controlled exterior streams, all eight actual nine-cell cones, two
farther paddings, and the time-4 seed. The stronger free-input check
passes; a six-tick delay is rejected. Next work on the reduced seed's
correlated return failures from GC1018, not another long simulation.


Q2 block, preregistered applicability check: can the newly reported
period-8 boundary use the existing one-sided p8 lock, rather than a new
closure search? Missing inference is whether its boundary word has the
lock's required single-white shape. Read only times 16..23 of the given
seed to identify that word; this is not a longer survival run or a
proof of its period. Prediction: the word need not have one white bit;
if it does, inspect the finite lock hypotheses before attempting a
self-consistency argument. Countercontrol: period 8 alone is insufficient
to invoke a theorem for 01111111. Independently use literal cells and
packed updates. Unexpected check: inspect all eight columns of the
reported period-8 band, since the useful boundary may precede site 14.
Record searched: `0111|q.?=.?.?3|p.?=.?.?4` + `white|hole|latch`,
then q7/p8 lock -> GC805/806 and GC893's existing one-sided lock.

Applicability outcome: site 14 has word 11110111 at times 16..23,
so the single-white requirement does hold (the cautious prediction was
wrong). Credit correction: the precise causal P8Lock audit is GC878,
not GC893. New bounded proof check: verify the eight first-14-cell rows
and a warmup through time 32. Prediction: they close if column 15 is
zero at phase 4; the existing 16-tick all-input lock supplies that bit
at every later white phase from the already correct past, enabling
strong induction without assuming an eternal wall. Countercontrol:
flip that bit at the white phase and check that the next band row fails.
Independent control: literal shrinking-cone evolution versus packed
evolution, and an explicit replay of the five-cell lock image sets.
Unexpected check: arbitrary initial tails beyond site 46 should also
be shielded, since they cannot change the 32-tick warmup. No long run
or solver call. Record searched: P8Lock source and GC878 causal transfer.


### GC1020 — The finite seed 1001 has an eternal two-gap train (KIMI Question 2)

**Status:** complete finite-certificate/induction argument, independent
Claude reading pending (PROOF-SKETCH under the record's status convention).
This applies Local's existing P8Lock, not a new one-hole lock theorem.
The key new step is causal feedback: only a finite *past* of the proposed
boundary is needed to guarantee the next band update. No eternal boundary
is assumed in the induction. Q3 and the prize remain open.

**Claim.** Under the externally clamped boundary x_t(0) = t mod 2,
the right seed x_0 = 1001000... has x_t(1) = 1100 repeating for all
t >= 0. More strongly, from t = 16 its first fourteen cells equal
P_(t mod 8), where sites are written left to right:

    phase    P_phase
      0      10011000100101
      1      11110101111101
      2      00000101000001
      3      00001101100011
      4      10011001010110
      5      11110111010101
      6      00000100010101
      7      00001110110101

**Finite premises, independently encoded controls.** The retained
`tests/probes/lexicon/rule30_train_p8_closure.py` checks all the following.
Literal Rule 30 lookup and packed Boolean updates agree. A shrinking
46-cell cone checks x_t(1) for 0 <= t <= 32 and the displayed band for
16 <= t <= 32. These checks need no assumption about sites beyond 46.
Every displayed row, with boundary phase mod 2, advances to the next
row for either exterior bit, except phase 4: there it does so exactly
when x_t(15) = 0. In particular column 14 reads 11110111, a rotation
of the one-white/seven-black wall.

**Causal lock, existing result.** If a cell reads 0111111101111111
at times a through a+15, its right neighbour is white at a+16,
whatever the five-cell starting state and whatever inputs arrive at the
sixth cell to its right. This is the n = 0 case of Local's
`tests/probes/lean/P8Lock.lean`, `p8_lock`; GC878 audits its causal
physical transfer. Only the sixteen specified wall bits are used.
To make the finite premise reproducible without a Lean installation,
start with all 32 five-bit states and repeatedly take the union of
both exterior-input successors, using these sixteen wall bits.
The successive image sizes are

    25,20,22,20,20,18,16,13,11,11,15,17,17,15,14,10.

The final image is exactly

    00000,00001,01000,01001,01010,
    01011,01100,01101,01110,01111.

Every member begins white. The probe reconstructs these exact sets
using independent literal and packed update implementations. Unioning
both inputs at every step covers every possible exterior sequence,
including exterior bits correlated with the interior. The eight-tick
image still contains a black-first state, so replacing sixteen by eight
in this argument fails its countercontrol. The established Lean theorem
was source-read; no new Lean compilation is claimed.

**Induction proving eternity.** The warmup supplies all rows from
16 through 32. Suppose the displayed band has held through time t,
where t >= 32. If t mod 8 is not 4, its last cell is black and masks
site 15; the finite transition table gives the correct band at t+1.
If t mod 8 is 4, then t >= 36 and a = t-16 >= 20. By the induction
hypothesis, site 14 on times a through t-1 is exactly two copies of
01111111. Apply the causal lock to sites 15..19, treating site 20 as
arbitrary at every update. It gives x_t(15) = 0, which is precisely
the missing condition for the phase-4 band transition. Thus the band
also advances correctly in this case. Strong induction proves the
band for all t >= 16. Its first cell has profile 11001100; the checked
warmup handles earlier times. This proves the claim.

**Unexpected stronger consequence.** The same conclusion holds for
*every* initial right half whose first 46 cells are 1001 followed by
42 zeros, with no restriction on the remaining tail. Finite speed
makes the warmup identical; the induction already allows every
subsequent exterior input. The probe checks zero and all-one finite
far-tail controls, but the universal-tail assertion follows from the
cone and the proof, not from those two tests. Neither periodicity nor
aperiodicity of site 15 is required or proved.

**Why the earlier window searches do not refute this.** Their failure
was closure of the particular sets sampled along the orbit. This proof
keeps a sixteen-tick boundary history and uses the exact five-cell
all-input lock; it never assumes that a sampled window set is closed.
The original first-macro gate at the 0111 boundary need not be invariant
(GC1018). The proof closes at the farther 01111111 boundary instead.

**Scope and credit.** Cloud's corrected fourteen-site observation
(CL187) identifies the useful boundary; Local's P8Lock supplies the
lock; GPT supplies the phase table and causal self-consistency induction.
The earlier seven-ring certificate (GC1013) realized the same visible
train with a periodic right tail; it did not prove this specified finite
right seed or the arbitrary-tail cylinder result. No finite left half
or all-depth record bound is constructed. `proof_dupes.py --near G271`
returned 03, C1, C2; all three read. Their white latch/checkerboard
rules and G271's black lock are antecedents, not the finite-seed
feedback induction proved here. Waiting-room referral only until
independent review; no new reviewed proof number is claimed.

**Filing check for waiting entry W282.** `proof_dupes.py --near W282`
returned G271, 10 and 37; all read in full. G271 contains the reused
P8 lock and its language consequence, but not this seed or feedback
induction. Entry 10 requires a leftmost black cell and bounds paired
repeats; entry 37 excludes constant columns in a nonzero finite global
seed. Neither applies to the imposed alternating boundary here. W282
is filed for review with its own summary; it is not yet a reviewed entry.


Preregistered post-GC1020 block (Q6 hidden-state scope). Missing inference:
does a long observed two-gap train itself certify entry into the new
absorbing band, or can the same visible prefix still carry a delayed exit?
A useful concrete result is an exact family of arbitrarily delayed exits,
which would require any record-bounding representation to retain the
distinction. Test only the existing GC1018 escape suffix behind zero to
three copies of the established seven-cell train background. Prediction:
the escape propagates through each copy with a fixed delay; counterfactual:
if it heals or the delay is irregular, stop this particular transport
claim rather than enlarge the search. The original GC1018 placement is
the positive control, the unperturbed periodic background the negative
control. Use a literal shrinking cone and independent packed updates.
Unexpected check: all-white versus periodic continuation after the escape
suffix, to distinguish a transported front from a far-tail effect.
Record searched: `seven.ring|7.ring|seven.cell` +
`defect|perturb|exit|train` -> GC1013 periodic witness, no such transport
claim. This is a bounded diagnostic; an affine finite table is not proof.

### GC1021 — The known train escape does not immediately transport across a ring copy

Bounded diagnostic, not a proof of eventual healing. Put the GC1018
suffix 011010000 at site 7 + 7m, with the established seven-ring row
to its left, m = 0,1,2,3. The original placement first breaks column
1's train at time 16; none of the other three breaks it through time
100. This holds with either white or periodic continuation after the
suffix. Literal shrinking cones and packed updates agree; the unmodified
periodic cone never exits, and the original placement reproduces the
known positive control. The proposed simple transport mechanism gains
no support; no fixed-delay law or all-time healing follows from the
finite results. Stop this transport diagnostic without increasing its
horizon or varying defects. A follow-up check shows the m = 1 white-tail
case does not match GC1020's exact band over times 16..32, so that
particular certificate cannot simply be reused at that onset.

Retained instrument: `rule30_train_escape_transport.py`. This is not
an R_real measurement, a new forbidden-word theorem, or a proof that
finite visible memory suffices. The main unresolved inference remains
how mixed-entry histories constrain later exits; a generic delayed
pulse cannot be assumed to supply its counterexamples. CL188 received:
GC1018 is independently checked, GC1019's equivalence is hand-accepted;
GC1017's independently checked finite instance is not itself a review
of the all-length proof. TR's capped deep calls remain UNKNOWN.

GC1020 review receipt, 2026-10-10: CL189 and L595 independently
reproduce every finite premise and accept the causal induction and
arbitrary-tail consequence. Question 2 is now PROVED; W282 promoted
to reviewed G282. The same three near-entry comparisons were read
before promotion; no new theorem beyond GC1020. Scope clarification
for CL189: failure of sampled-window closures does not establish that
no finite spatial invariant can carry the correlation. GC1020 proves
sufficiency of temporal information, not necessity of that representation.
Question 3 remains open.


Preregistered conditioned-interface block (Q6, after G282). Missing
inference: whether a sustained visible two-gap train forces the reduced
0111 interface into just its period-4 or period-8 modes. GC1017 supplies
the exact zero hole samples, but not the intervening three samples.
Inspect only the five-cell, four-tick transition relation, retaining
zero first cells at both endpoints and all sixteen exterior streams.
Prediction: its recurrent part still permits branching nonperiodic
first-cell output; if so, a concrete recurrent ambiguity, not a larger
width sweep, is the result. Counterfactual: if every recurrent output is
periodic, derive that finite implication and its entry margin. Literal
and packed macro encodings must agree. Controls: known seven-ring and
G282 trajectories restrict to accepted edges; a failing GC1018 source
is rejected. Unexpected check: distinguish multiple input paths with
identical visible output from genuine output ambiguity at the same state.
Record searched: `0111|p.?=.?.?4` + `condition|zero.*hole|hole.*zero|zero.*sample`
-> GC1017/1018; one-hole language results alone do not give this
conditioned full-trace implication. No SAT, record scan or Local job.

The five-cell graph has two distinct twelve-tick returns to state
01001, so the predicted visible ambiguity is present. Before treating
this as a real right-half ambiguity, check the prescribed exterior
stream against its own Rule 30 equation with the known fifth cell.
Prediction: at least one artificial return violates this one-cell
temporal compatibility. Countercontrol: the true seven-ring's exterior
passes. This identifies what correlation the relaxation discards, rather
than claiming its recurrent paths are actual or increasing the strip.

### GC1022 — Recurrent train-interface ambiguity is already lost at the exterior cell

Exact countermodel for the five-cell free-exterior relaxation, not
for actual right halves. Drive it by 0111 and retain white first cells
at times 4n. The following four-tick returns, each checked by literal
and packed Rule 30, all have white endpoints (state bits left first):

    start   exterior   end     first-cell trace
    01001     0001     01001       0101
    01001     0000     01000       0101
    01000     0000     00100       0101
    00100     0110     01001       0000

Thus state 01001 has two twelve-tick return words with traces
A = 010101010101 and B = 010101010000. Concatenate the first loop
three times for A, or the last three edges for B. Every binary choice
of these returns stays within the zero-hole constraint. The bit at
position 9 of each twelve-tick trace distinguishes A from B, so an
non-eventually-periodic choice yields a non-eventually-periodic trace in this
relaxation. This is genuine output ambiguity, not merely multiple
inputs carrying the same trace. The reduced five-cell relation alone
cannot force the interface to its period-4 or period-8 modes.

**The missing correlation is explicit.** Let u_t be the prescribed
exterior bit and z_t the fifth retained cell. A real exterior cell
must satisfy u_(t+1) = z_t XOR (u_t OR v_t) for some next cell v_t.
When u_t = 1 it necessarily has u_(t+1) = 1 - z_t. The artificial
A stream 000100010001 violates this at ticks 3,7,11 of its periodic
repeat; B's stream 000000000110 violates it at tick 10. In every
violation (z_t,u_t,u_(t+1)) = (0,1,0), impossible for either v_t.
So these precise return paths cannot be actual, even though their
interior states recur and all required hole samples are white.

**Do not delete their output words.** At the same start 01001, the
actual seven-ring exterior 100110011001 returns to that state with
the same output A and satisfies the exterior equation. Excluding a
spurious hidden path does not license excluding its visible trace.
No claim about all realizations of B, or any longer strip, is made.
The G282 seed and seven-ring positive controls restrict correctly to
the relation; GC1018's failing prefix 00010 is rejected for every
exterior block. All 32 states and sixteen four-tick exterior blocks
pass independent encodings. `rule30_train_hidden_returns.py` retains
the checks. Stop this bounded relation test: its concrete lost
constraint is temporal compatibility of the exterior, not lack of
a recurrent state or failure of one-tick cell domains. The all-depth
record bound remains open; no Local solver work is duplicated.

CL190 boundary block, registered before controls. Missing inference:
whether the proposed entry/exit theorem is already a consequence of
short certified forbidden words, with the initial endpoint retained.
Record searched: `train|2.gap` + `exit|entrance` -> GC1017/1019 and
CL190; read RLK's printed K18 list and GC984/985 endpoint arguments.
Hand prediction: exit4 then5 follows from the short list, but entrance3
may survive when its preceding one is the very first visible bit.
CL190's ten-bit entrance window does not test that endpoint. Check only
4096 finite right seeds for the concrete prefix10010101010; finding one
refutes unqualified (N), while no hit means UNKNOWN. No absence inference,
SAT call or extension of this search. Independently replay any witness
with a literal shrinking cone. Unexpected control: compare entrance3 at
index0 with the same motif preceded by zero, which contains0100101.
The seven-ring must supply the continuing train control. The exit proof
will keep the existence of an exit explicit: G282 permits eternal trains.

### GC1023 — CL190's train exit rule, with a necessary startup exception at entry

Hand consequence of the verified RLK forbidden words, plus an independently
replayed finite counterexample. No new language-membership solver result.
The required absent factors, all already in RLK's printed K18 list, are

    11, 00000, 101001, 0100101, 0101010000,
    0101000101, 01010001001, 010100010001.

Their absence is inherited from Local's certificate work (MFC/L590),
not re-proved by the substring checker below. All following implications
hold for every word avoiding these eight factors, hence for both actual
phase languages and all time-shifted factors. A finite word may end before
a stated next one: conclusions concern gaps that occur, or infinite traces.

**Exit (E), for every n>=4.** Let a maximal train have at least four
visible ones, all consecutive gaps2, and suppose it exits. No gap is1
(absence of11) or >=6 (absence of00000). Gap3 following a gap2 would
contain101001. Gap5 after the last three train ones, with the zero
immediately preceding them, would contain0101010000. That leading zero
is present within any four-one train. Therefore its first non-2 gap
is4. The next gap cannot be2,3,4: the preceding two train ones and
that exit would respectively contain0101000101,01010001001,
010100010001. Gaps1 and >=6 remain excluded, leaving exactly5.
This is uniform in train length by taking a suffix at the exit; no
length extrapolation or eventual finite-state claim is involved.
An eternal train has no exit, as G282 explicitly permits.

**Entrance (N) needs its initial endpoint.** At the start of a maximal
train, its preceding non-2 gap is among3,4,5. A gap3 followed by the
train's first gap2 gives100101. If the earlier one has any preceding
visible symbol, it must be0 (absence of11), giving forbidden0100101.
Thus a noninitial earlier one forces entrance4 or5. But the earlier
one may be at visible index0, where no preceding symbol exists.

That exception is real. With the white-start clock and the finite
right seed11110111 (sites1..8, all farther sites zero), the first11
white-time samples are

    10010101010 = 100 + (10)^4.

The preceding one is at index0, the train starts at index3, and its
entrance gap is3. This directly refutes CL190's unqualified (N) at
n=4, even when 'train' is interpreted as maximal. A 4096-seed bounded
search found seed239; literal shrinking-cone evolution through time20
independently agrees with packed evolution. No search beyond that
registered bound was used. The source is an actual finite right seed,
not a free-boundary strip model. It is not a finite full-line clock.

`rule30_train_boundary.py` retains the witness and all gap-case substring
checks. The seven-ring is the eternal-train positive control. Unexpected
endpoint control: prefixing this actual visible word by0 produces the
forbidden0100101; realizability is not preserved by that extra past.
The ten-bit entrance census in CL190 necessarily puts a gap3 predecessor
away from index0, so it could not see this exception.

Question B remains open. The boundary mode tests unconditioned
membership of (10)^n u; it does not test membership of p(10)^n u for
every earlier prefix p. Also finite-horizon stabilization with n0
allowed to depend on m would not by itself give a single synchronizing
word or regular continuation language. Next retain that quantifier
when testing whether actual mixed-entry correlations survive trains;
no extra Local run is requested by this block. These boundary rules
are already implied by short cuts, so they cannot explain the retained
length45/46/81 overshoots that avoid those cuts.

### GC1024 — Actual entry memory across a train: two concrete follower separations

CL190 Question B block. Missing inference: equality of future languages
conditioned on different visible prefixes, not equality of the train's
unconditioned continuation sets. Before any new run, use the retained
CUT witnesses. Record searched: the two L593 length45/46 strings ->
L593; read L591's length81 certificate and simulated deletion controls.
Prediction by direct factorization: these already separate actual
prefix-conditioned followers. No new membership experiment. An
unexpected control is to compare successive train lengths in L593:
conditioned followers need not be nested even though unconditioned
followers are nested.

Write T=10. L591's checked absent length81 word factors exactly as

    p T^10 u,
    p = 01000,
    u = 00100001010101010001000010010010010000100001000010000101.

Here u has56 symbols. The proper prefix and proper suffix were both
realized by simulation in L591; the whole word was cake_lpr-rejected.
Consequently p T^10 is an actual history (a prefix of the first
control). With p'=1000, p' T^10 u is actual (the second control).
The future u is therefore possible after p' T^10 and impossible after
p T^10, although both histories end with the identical twenty-symbol
train T^10. All claims here inherit those explicit L591 evidence gates;
no fresh solver or absence replay is claimed. Both prefixes are nonempty,
and both traces have a white-start wall. This is actual visible-history
memory, unlike GC1022's artificial free-exterior loops. If B is true,
its threshold n0(56) must exceed10.

The sharper short-horizon example uses L593's fixed

    q = 000010001010000,   v = 0010000101.

L593 reports q T^12 v absent with a checked cut, but q T^13 v present
by its SAT membership run. Factoriality gives q T^12 actual (a prefix
of the present word) and T^12 v actual (a suffix). Thus a ten-bit future
allowed after the unconditioned train is disallowed after a realizable
specific prefix. This contradicts CL190's asserted prefix-independent
ten-bit sets through n14, not its eventual-forgetting conjecture.
If that positive membership is accepted, n0(10)>=13. Its positive side
is currently a reported SAT verdict, not a new directly replayed model;
Cloud is asked for one retained simulated model, not a wider scan.

The unconditioned follower sets F_n(m) are nested: T^(n+1)u actual
implies T^n u actual by deleting its first T. At each fixed m a finite
descending sequence of subsets therefore eventually stabilizes. That
alone gives neither an explicit threshold nor independence from q.
In fact v is allowed after q T^11, excluded after q T^12, and allowed
again after q T^13, according to L593. Hence the corresponding
prefix-conditioned follower sets are not nested. This is the unexpected
control: one cannot obtain B by applying that simple finite-set argument
to a fixed earlier prefix. No claim of persistent memory at arbitrarily
large n follows. The remaining target is a uniform-in-prefix forgetting
bound, or a family of actual follower separations with unbounded n.

CL191(B'') bounded causal diagnostic, registered before execution.
Missing inference: does an early perturbation of the actual L596 right
row survive invisibly through its eleven-cycle train and alter a later
visible bit? This could locate a concrete carrier of memory; it would
not replace GC1024's existential follower-set separation. Record searched:
train + exit/entrance and the retained GC1021/1022 diagnostics; neither
compares early perturbations of the newly verified L596 configuration.
Prediction: among the45 single/pair flips in initial sites1..9 there is
one changing both the early visible prefix and a later continuation while
preserving the entire first train. Counterfactual: every such change
breaks the train or is erased; then stop, without widening the search.
Use the existing published right row with a clamped clock, no solver.
Independent literal shrinking-cone replay is required for any selected
pair. Unexpected check: distinguish a difference in the later future
from an early defect that disappears completely; record the first and
last differing site during the common train rather than infer pinning
from the backward cone alone.

### GC1025 — Early one/two-bit perturbations do not expose the train's memory carrier

The registered45 perturbations of L596's initial sites1..9 all break
its visible T^11 at indices5..26. Their first differing train index is
one of5,7,9,11,23. The predicted surviving early perturbation was not
found. Every packed trace agrees with an independent literal shrinking
cone through time168. An out-of-cone site170 flip leaves the trace
unchanged. Since no candidate preserves the train, the planned internal
damage-envelope comparison has no selected pair and was not performed.
This proves only isolation under those45 mutations with that fixed tail;
it proves neither uniqueness nor pinning under coordinated farther changes.
Stop this diagnostic, without adding mutation sites or orders.

CL193 closes GC1024's requested positive gate: the retained101-site row
reads q T^13 v under both packed and independent literal evolution through
time100; its site21 flip fails. Thus the n0(10)>=13 obstruction now has
a directly replayed positive model as well as L593's checked negative
cut. CL192 also independently confirms GC1023's factor argument and
startup exception. `rule30_train_carrier.py` retains these controls.
The flag poll succeeded this tick after the prior single-file read failure;
no outstanding transport blocker is inferred. The next proof target is
correlated entry/exit compatibility, with Cloud helping formulate a
sharper bounded lemma under the owner's current division of work.

Failed-gate exit packet, registered before computation (serves CL190 A
and the requested B'' mechanism). Missing inference: how much of the
exit is fixed by the prepared six-cell slab and its first failed exterior
sample, independently of the earlier entry. GC1019 gives only the first
eight ticks; GC1023 supplies gap4 then5 by forbidden factors. Test the
stronger forward statement from the exact spatial prefix1001101 beside
the white-start clock: white-time samples through time22 are always
101000100001, for every right exterior. This would identify a universal
exit packet and delimit where entry memory can reappear. Record searched:
train + exit/entrance -> GC1017/1019/1023; no twenty-two-tick packet
statement. Prediction is informed by the observed exit, not a new scan
prediction. Enumerate precisely its radius-one cone: all65536 assignments
to sites8..23, once. A counterexample refutes this stronger statement and
ends the test; no cone expansion. Independent literal replay of extrema
and any counterexample; g=0 must fail the proposed exit packet (seven-ring
control). Unexpected check: compare a genuine right evolution with freely
prescribed column7 inputs, so any extra needed correlation is explicit.

The exact23-cell cone gives one white trace,101000100001, on all65536
tails. The free-column7 model first permits a different white bit at
time16; its example stream starts10, impossible here since x7(0)=1
and x6(0)=0 force x7(1)=1. Before filing a large cone certificate,
retain exactly that missing cell equation: test the seven-cell prefix
with free column8 inputs through22. Prediction: this seven-cell temporal
relation suffices for the entire exit packet. If not, retain the exact
cone proof and stop; no progressive strip-width search.

### GC1026 — A seven-cell failed gate forces the entire exit packet

The seven-cell relation suffices. Starting from1001101, its exact images
through22 ticks all have a common first bit at each time, giving the full
trace11001100010011010001001 and white trace101000100001. W283 in
PROOFS.md lists every image and its two-input recurrence, a finite proof
candidate awaiting an independent reader. Thus the failed gate generates
the exit4,5 for every exterior, without using earlier entry history.

All512 local literal/packed gates agree; all22 image transitions replay
exactly; all65536 exact23-cell cones produce the full trace. The unexpected
six-cell countercontrol loses the packet at time16 because it allows a
site7 stream beginning10, violating that cell's own update. The seven-ring
with gate0 keeps the train instead. This isolates a necessary retained
cell equation for this particular relaxation; it is not a lower bound on
all possible representations. Checker: rule30_train_exit_packet.py.

This explains the universal exit but does not explain the later
prefix-conditioned follower separation. No permanent forgetting, recurrent
classification or record bound follows. Next target remains the
correlated information surviving beyond this forced packet; Cloud's
bounded question-design request remains pending.

CL194 arrived during publication. Its proposed gated propagation to the
last car is unsound for exiting trains: the retained CL193 positive
model has sites1..7 equal1001101 at74 and1011010 at78 (last car),
violating the imposed successful gate and fixed slab. Direct replay
is a concrete countercontrol, not a new search. Stop gates at certified
interior time62 and propagate the complete near-wall strip through the
exit instead. Failure of any bounded relaxed interface is not proof
of nonsoficity or of a far-field physical carrier. Cloud is asked to
revise the bounded target before any census; details in chat GC1026.

### GC1027 — The correct train endpoint is its penultimate car

Missing inference (CL194 repair): locate an exact slab/gate interface
for the decision to exit, rather than forcing the slab through the last
car. Record searched: train + penultimate/n-6/first-exit -> GC1019 and
unrelated wheel exits; the endpoint extension below is not recorded.
Hand prediction: the slab persists to the penultimate car, and its gate
is exactly the complement of the first symbol after the train. This is
a corollary of GC1017/1019, not a new state census. Counterfactual: the
last-car slab is forced; CL193 already refutes it. Unexpected check:
use the actual exiting positive model, rather than the eternal train,
to verify both indexing and the unforced last-car boundary.

**Endpoint lemma (hand proof).** Let the wall be white at time a and
suppose column1's white-time word starting there is T^n, T=10, n>=5.
Then at every time a+4j, 1<=j<=n-2, sites1..6 are100110. For
1<=j<=n-3, site7 at that time is0. At s=a+4(n-2),

    x_1(a+4n) = 1 XOR x_7(s).

GC1017 applied to the initial T^(n-1)1 gives the slab at a+4.
If the slab is known at a+4j and j<=n-3, the observed black at
 a+4(j+2) and GC1019 force x_7(a+4j)=0. The four slab transitions
therefore return100110 at a+4(j+1). Induction reaches j=n-2;
GC1019 there gives the displayed identity. No gate at j=n-2 was
imposed, since the corresponding visible sample lies after T^n.
The last car (j=n-1) need not retain the slab.

**Concrete reduction of CL194.** Here a=30, n12's endpoint is70 and
n13's is74. Start A(w) at46, as proposed, and use n-6 successful
gated cycles, not n-5. For the first-symbol obstruction q T^12 0,
the endpoint target is simply site7=1; no full v membership set is
needed. Exact actual prefix histories satisfy that equivalence. In a
free-exterior relaxation, an empty intersection with site7=1 proves
absence, while a nonempty intersection may be a spurious history.
A(w) may remain the sound superset from q T^8, because both longer
prefixes contain it. This fixes the specific containment failure and
removes the proposed 2^w suffix-membership calls for this first target.

The retained q T^13 v model has1001100 at70,1001101 at74 and1011010
at78, so it passes the repaired endpoint and fails the old one. W283
also shows a failed endpoint fixes the first eight symbols following
T^n to00100001; the last two bits01 of v=0010000101 remain a separate
constraint. Thus the first-symbol and full-v cuts must not be conflated.
CL194's claimed q T^12 0 absence is received SAT evidence, not a fresh
checked absence proof here. No all-depth or nonsoficity result follows.

### GC1028 — A nine-bit interior target replaces the proposed width search

Before computation: missing inference in CL195 is whether a finite width
must certify the specific first-symbol obstruction. At time62 the
longer target forces the six-cell slab. Its two further successful gates
are at62 and66; exit after twelve cars is the failed gate at70 (GC1027).
Thus sites7..15 at62 determine all three gates by finite speed: no site16
input can reach site7 by70. Prediction: the exact predicate on these nine
bits, gates0,0,1 at offsets0,4,8 beside0111, is equivalent to the desired
exit for an actual row with the prepared slab. This gives a concrete
width15 sufficiency with an exact prefix-conditioned set, rather than
an unknown width to search. Record searched: train/0111 + nine/9.bit/
gate-eight/width15/width17 -> GC1018's return formula and unrelated wheel
widths, not this prefix-conditioned exit predicate.

Enumerate only the512 nine-bit local sources to retain that target set;
this is not a language-membership census. Independent literal shrinking
cones and full six-cell-slab evolution must agree on the predicate.
Counterfactual: the gate at offset8 can be changed by a farther exterior
input; the cone forbids this. Unexpected check: neither the slab nor
the target predicate may be assigned to every q T^9 history without
conditioning; include the slab explicitly in the prefix-state query.
No new SAT job or width sweep is authorized by this computation.

**Outcome and exact reduction.** The target set B consists of39 words,
written site7 first:

    01101????       (16)
    01110????       (16)
    0111100??       (4)
    0111111ab, (a,b) != (0,0)    (3).

Question marks are independent bits. Literal shrinking cones, packed
updates with two opposite far tails, and1024 full-slab traces agree on
all512 sources. The checker also verifies the four patterns equal the
computed set exactly. In every case the three gates0,0,1 are equivalent
to the full-slab white trace T^4 0 through16 ticks. This finite table
identity is independently reproducible in rule30_train_exit_target.py.

Let A' be the set of nine-bit words at sites7..15 at time62 among actual
right halves realizing q T^9 AND having sites1..6=100110 at62. Then

    q T^12 0 is realizable  iff  A' intersects B.

Forwards: GC1027 forces the slab and successful gates62,66, followed by
failed gate70. Their cones give a word in B. Backwards: take the actual
prefix realizer witnessing A'. Its gates through70 depend only on
sites7..15 at62 while the slab persists through the two successful
cycles. Membership in B gives exactly the remaining T^4 0, overlapping
the last car of q T^9, hence the desired full visible word. No splicing
of independently chosen histories is used. Every actual witness for
A' already supplies the entire right exterior.

This proves width15 suffices for THIS slab-filtered interface. It does
not assert that CL195's unfiltered free-strip propagation is exact at15.
For that original method, width17 at62 always suffices for the first-bit
query ending78: site18 cannot reach site1 within16 ticks. Each accepted
17-bit state has one actual prefix realizer; the entire remaining
column1 trace is determined by that state and the clock. Thus any
surviving relaxed path has a real trace, and conversely. Conditional on
CL194's reported first-bit absence, CL195's original W*<=17 and it
empties by78, without a width search. For the full-v horizon96, the
analogous elementary bound is35. These are causal bounds, not SW's
empirical width40 comparison and not uniform bounds for growing words.

The least width remains uncomputed. More importantly, recognizing A'
retains the difficult earlier-prefix correlations: the39 local targets
are not a finite-state description of all actual histories. This
reduction identifies exactly what the next structural explanation must
exclude; it does not manufacture the missing prefix invariant.

CL196 asks for a free-LR bound using the new toolkit. The transfer fails
its domain control: a freely prescribed column1=1 has a well-defined
inverse left evolution with column-1=t mod2, whereas actual Rule30 to
the right excludes its white samples11 in two ticks. This is not a
finite-left counterexample; it prevents using the right-language cuts
as premises for unrestricted LR. The regular-edge route still requires
joint nonlinear incompatibility of GC598's late-source compensation
with the odd wall condition; GC599 prevents a bounded-restart shortcut.
No new bound results from this attempted transfer. Retain the actual-
right prefix-exclusion target rather than restating the closed routes.

### GC1029 — Move past the cutoff-40 obstruction to the final exit bit

Relevance check before the next proof: q T^12 0 has length40, so its
reported absence is already implied by the complete cutoff40 language.
It cannot tighten relax40. L593's original q T^10 v cut has length45,
comes from a relax40-accepted code and is cake_lpr-verified absent.
That is the appropriate missing constraint. Here q=000010001010000,
T=10, v=0010000101. Every factor of its relaxed source of length<=40
is actual, by completeness of the base list. In particular q T^10 0
(length36) is actual. W283 then forces the first eight exit bits; the
ninth is0 because any white-time1 forces the next white-time0. Only
v's final1 is the new constraint. This uses L593's recorded provenance,
not a new SAT replay or a claim that all of its variants are minimal.

Missing inference: characterize that final1 using the retained W283
state at offset22 from the failed gate. Hand prediction, before the
finite check: of W283's15 possible seven-cell rows there, exactly
{25,49,89} permit the final1 at26; every row forces0 at24. No larger
strip or language enumeration. Independent literal four-tick updates
for every row and all16 exterior streams will check this statement.
Countercontrol: the other12 rows must give0 at26; otherwise the proposed
partition fails. Unexpected check: the ninth exit symbol is automatic,
so do not spend work explaining a nonexistent ninth-bit obstruction.

**Outcome and hand derivation.** All240 four-tick continuations pass.
For any white-start row with x1=1, put (a,b,c,d)=(x2,x3,x4,x5).
After one tick its next three cells are u=NOT(a OR b),
v=a XOR(b OR c), w=b XOR(c OR d). After two ticks x1=0,
x2=NOT(u OR v), x3=u XOR(v OR w). The white sample at four ticks
is1 exactly when these last two cells both vanish. That requires u=1
and v OR w=1: u=0 would require v=1 from x2=0, contradicting x3=0.
Consequently a=b=0 and c OR d=1 are necessary and sufficient.
In W283's exact offset22 image this selects25,49,89, written spatially
1001100,1000110,1001101. All other12 states force the final0,
independently of every farther input.

For the verified length45 cut, the failed gate is at62; offset22 is84,
the automatic zero is86 and the final forbidden one is88. The next
structural question is why actual histories q T^10 followed by the
permitted exit avoid those three states at84. It concerns a restriction
missing from relax40, unlike the q T^12 first-symbol target. W283 now
has this explicit final-bit corollary and its240-case countercontrols;
independent review requested. The earlier39-state reduction is correct
but the cutoff40 relevance check parks that particular exclusion task.

GC1029 correlated-proof diagnostic, registered before execution.
Missing inference: can the verified45-cut's entry/exit incompatibility
be derived by local pair relations, rather than opaque full-cone SAT?
The new evidence is its three explicit final-bit states and CL197's
separate two-cell obstruction; this is not a repeat of unary or affine
forcing. Retain all six pair projections of each four-variable Rule30
gate, filter its eight tuples against the shared pair domains, and
iterate to a fixed point. Prediction (low confidence): the45-cut reaches
an empty relation. Counterfactual: pair consistency stalls; record that
failure and stop, without larger clusters or a width sweep. Controls:
11 must be rejected; CL193's simulated51-symbol word must survive.
Unexpected check: every surviving pair domain in the positive control
must contain its actual simulated pair, not merely leave the CSP nonempty.
Record searched: f46 domain/affine probes and GC1028/1029; no pair-domain
proof of this45-cut is recorded. This is a bounded symbolic proof test,
not a new membership verdict or a duplicate solver run.


**Pair diagnostic outcome (single-party).** Prediction refuted: the
45-bit cut reaches a nonempty fixed point with 3,668 of 4,094 unary
domains unresolved and 17,456 of 19,668 pair domains unrestricted.
The positive control survives, including every actual simulated pair;
11 is rejected. Instrument retained in rule30_cut_pair_domains.py.
This supplies no actual realizer and does not challenge the verified
UNSAT cut. Local gate-pair propagation does not explain its obstruction.
Stop this diagnostic as registered; the missing inference remains the
earlier-history exclusion of the three final-bit states, not a request
for larger clusters or another membership run.


GC1029 backward packet separator test, registered before execution.
Missing inference: bring the final-bit obstruction back toward the
failed gate, where entry history might impose a simple condition.
Use only W283's existing seven-cell transition graph: pull the three
final-bit states backward and check for a forced intermediate row after
the forward image first branches. Prediction: a unique such row is
necessary for the last 1. A bottleneck would give a concrete earlier
state to exclude. Counterfactual: every branching layer retains multiple
successful rows; then stop, without widening or enumerating histories.
Control: forward reachability reconstructed from literal transitions
must equal W283's stored table. Unexpected check: distinguish rows that
can reach the target from rows whose every continuation reaches it;
existential backward reachability must not be reported as forced success.
Record searched: packet AND backward|dominator|separator -> GC979/980
context-widening hits, different object; no W283 backward-state test.


**Backward separator outcome (GC1029).** The prediction holds.
At offset 7 the forward image is {6,70}, but only row 6 can reach
{25,49,89} at offset 22. In spatial order the necessary row is
0110000 rather than 0110001. Define B22={25,49,89} and
Bt={r in St: some u has J_(t mod 2)(r,u) in B_(t+1)} using W283's
exact image table. Direct backward recurrence gives B7={6}; its
cardinalities at offsets 8..22 are
2,2,2,2,2,3,3,3,3,4,4,3,3,3,3.
Independent forward counts with the packed transition give 11,904 of
32,768 exterior strings successful from row 6 at offset 7, and zero
from row 70. Therefore this is a necessary separator, not a sufficient
exit condition. The actual CL193 positive model has row 6 at time 81,
seven ticks after its failed gate at 74, as required.

For q T^10 v the separator is at time 69: its forbidden final 1 at
88 would require x7(69)=0. This moves the earlier-history question
15 ticks earlier, to one branch of an already forced six-cell row.
Whether q T^10 0 can realize that branch is not decided here. If it
can, the later exterior correlations still matter. No claim of a
proof of the 45-bit cut or of an all-depth record bound. The same
checker retains the backward relation and independent forward counts.


CL198 pinning block, preregistered before execution. The new evidence is
Cloud's reported 24-cell forced row at time 30. Missing inference:
derive those cells without SAT using the now-proved train slab and
failed-gate packet as macro premises. Test unary projection once with
these extra proved relations, not the old unstrengthened unary or affine
method. Prediction: this derives the stated row for the leading-0 word.
Controls: the leading-1 word must not contradict; compare with the
unstrengthened leading-0 baseline. Unexpected check: the macro premises
must also hold on CL193's actual model after shifting its failed gate
from 74 to 62. If pinning stalls, retain the unresolved positions and
stop; no additional cluster or width search. Record searched: GC1029
pair diagnostic, GC1027 slab, W283 packet and CL198; this combination
has not been tested. CL198's SAT pinning is received evidence, not yet
a hand proof or a checked certificate of the pinning step.


**CL198 pinning diagnostic outcome.** Prediction refuted. Plain unary
propagation and propagation strengthened by the proved slab/gates and
all 23 seven-cell packet relations both leave row 30 as a leading 1
and 23 unknown cells. The leading-1 control also remains nonempty;
all added macro premises hold on the actual shifted CL193 packet.
The first harness horizon 86 omitted some packet cells and raised a
KeyError; horizon 92 repairs that setup defect. No result from the
failed invocation is counted. Retained instrument:
rule30_train_macro_pinning.py. Stop this route, without further domains.
CL198's reported SAT pinning remains plausible received evidence;
the propagation from its pinned strip does not by itself prove the
pinning. GC1029 final-bit identity review accepted. The backward
separator and its branch query remain pending; no new data requested.


GC1029 transport block, registered before execution. CL199 gives a
new concrete row, 1001000 at odd time 75. The backward may/must sets
suggest more than a necessary cut: from that row the white sample
13 ticks later should equal NOT(x8 at the starting tick), independently
of every later exterior input. This would replace the 13-tick residual
query by an exact one-bit transport identity, conditional on that row.
Test all 8,192 controlled exterior streams and independently all 128
literal 14-cell cones. Counterfactual/unexpected check: changing only
the starting clock phase must destroy this identity; retain a witness.
Do not infer that q forces the row or the exterior value from this
identity. Record searched: 1001000 AND transport|thirteen|13.tick|complement
-> no earlier transport result; CL199 states only the first transition.


Transport check update: all 8,192 streams and 128 exact cones pass,
but the proposed wrong-phase countercontrol is refuted: the identity
also holds for every controlled stream under the other clock phase.
Do not count a failed countercontrol as a pass. New analytical negative
control before execution: change the starting site 7 from 0 to 1.
Then the first exterior bit is masked by the OR at that site, so streams
that differ only in their first bit have identical subsequent states;
they cannot both satisfy the complementary-output identity. Retain that
pair, and verify both clock phases on independent literal cones.


**GC1030: exact delayed transport (review pending).** With either phase
of an alternating wall, an initial seven-cell row 1001000 satisfies
x1(t+13)=1-x8(t). This remains true with completely independent
exterior inputs at every later tick. Thus under CL199's row at time 75,
the final symbol at 88 is exactly the complement of x8(75), not just
subject to a necessary condition. Proving that q forces the row and
x8(75)=1 remains open here.

Finite proof: encode the seven cells little-endian, so the row is 9.
For initial wall bit b and exterior bit u, set S1={J_b(9,u)} and
S_(k+1)={J_((b+k) mod 2)(r,v): r in S_k, v in {0,1}} for 1<=k<13,
with W283's explicit packed Rule 30 transition J. The four exact S13
sets, in order (b,u)=(0,0),(0,1),(1,0),(1,1), are:

- {27,37,43,47,79,91,101,111,123};
- {6,14,22,38,62,70,78,86,102,110};
- {7,25,39,45,89,103,109};
- {4,24,28,40,52,60,68,88,92,100,104,116,120,124}.

Their least bits are respectively 1,0,1,0, proving the identity for
all subsequent inputs. The retained packet checker reconstructs the
sets, independently checks 16,384 packed input streams and 256 literal
14-cell cones. Changing site 7 to 1 destroys the identity: its OR masks
the first input, and streams 0 and 1 both give final bit 1. The proposed
wrong-phase countercontrol instead failed, revealing phase independence;
that failed prediction is retained rather than counted as a control pass.


### GC1031 — CL200 free-model junction question: two constant pieces

Missing inference: is a bound depending only on junction count valid
in the unrestricted free visible model? Test the two simplest periodic
pieces, 1^n followed by 0 forever, at n=1,2,4,8,16,32,64. Prediction:
a white run grows with n, potentially permitting an explicit family
counterexample. This is not Cloud's train/S/L scan. A finite scan alone
will not establish unboundedness. Counterfactual: measured runs plateau;
then stop the family, without period or connector sweeps. Control:
independent packed and literal inverse recurrence must agree. Unexpected
check: count only white runs closed by black cells on both ends, avoiding
truncated-boundary growth. Record searched: junction AND periodic|bound
-> CL200 and unrelated uses; no two-constant-piece result recorded.
The word 11 is not actual beside the wall; the test addresses the
explicitly requested free-model claim, not the actual-language variant.


**Outcome and the inference that needs repair.** For n=1,2,4,8,16,32,64,
the closed-run maxima are 1,3,4,4,6,9,7. Independent inverse recurrences
agree. This neither proves unbounded growth nor a plateau; stop this
family rather than extend a scan. Instrument: rule30_two_constant_junction.py.

There is a separate causal gap in CL200's proposed implication. A cell
at depth r depends on column -1 at times 0..r-1, hence on visible indices
0..floor((r-1)/2). A run at depths d..d+L-1 therefore uses a prefix of
M=1+floor((d+L-2)/2) visible symbols. Its whole cone is not bounded by d
alone. If an additive junction estimate L<=B+C*J counts junctions in
that prefix, the elementary J<=M-1 gives only
(1-C/2)*L <= B+C*(d-2)/2. For C>=2 this supplies no upper bound on L.
In particular the proposed empirical scale of 6..10 cells per junction
cannot be substituted into that step to obtain a linear record bound.
This does not refute a junction theorem. It identifies the extra
localization needed: count only junctions in the starting cell's cone,
or prove an independent bound on the number relevant to the entire
run, or a quantitative density bound strong enough to absorb L.

The dictionary must also be fixed: an arbitrary finite S/L word is not
itself a bounded-period piece, and permitting an arbitrary period lets
one call any finite code a single piece. Pure pieces can have positive
white runs, so a base term B is needed even when J=0. These qualifications
precede any extrapolation from JN's finite templates. They do not change
Local's computational lane or request another scan.


### GC1032 — A two-cell barrier replaces the full CL199 row premise

Missing inference: reduce the entry-side obligation without another
pinning experiment. In W283 the offset-13 rows are {9,57,73,105,121}.
The offset-14 rows which can still reach the final 1 are {30,46,126}.
Hand derivation: the next step misses this set exactly when site 5 is
1, or site 7 is 0 and the exterior site 8 is 1. Thus the actual-entry
proof need only force the latter pair at time 75; it need not first
force row 1001000 or the 24-cell strip. This remains an unproved
entry-side premise, but the packet-side implication is unconditional
within the five-state packet image.

Before checking the ten transitions: prediction is the exact guard
G=x5 OR ((NOT x7) AND x8). Countercontrol: row 9 with exterior 0 must
remain viable. Unexpected check: exterior 1 alone is not a barrier;
row 73 must remain viable with that value. Record searched: GC1029
backward sets, GC1030 and CL199; no two-cell-only barrier stated.


**GC1032, packet barrier (review pending).** At offset 13 from W283's
failed gate, the guard x5 OR ((NOT x7) AND x8) forces the offset-26
output to 0, independently of all subsequent exterior inputs.
The complete transition table from its five possible rows, for
exterior inputs 0 and 1 respectively, is:
9 -> (30,94); 57 -> (78,14); 73 -> (126,126);
105 -> (46,46); 121 -> (14,14).
The previously established backward set at offset 14 is {30,46,126}.
The guard is exactly the condition for missing this set, proving the
claim. It is also exact for guaranteed rejection against arbitrary
later exterior streams: outside the guard, a path to the final 1
remains. This latter statement is about the controlled packet, not
actual right-half realizability.

For the 45-bit cut, it suffices to derive x7(75)=0 and x8(75)=1 from
the entry/exit history; the other five row bits need not be pinned.
The still weaker disjunctive guard itself would also suffice. Neither
entry implication is proved here. All ten transitions and the viable
rows (9, exterior 0) and (73, exterior 1) pass literal controls.


### GC1034 — The pinned 24-site strip does not itself give an autonomous future

Missing inference: could CL198's pinned strip serve as a concrete reset state
for the hidden representation? Record searched: `CL198` + `strip` found the
existing finite propagation, not an autonomous-future certificate. The
prediction and controls were written before this bounded test in
`rule30_pinned_strip_future.py`. This is a different forward question from
the stopped entry-pinning attempts; it assumes the reported strip.

Starting at time30 with 100110011001100000000010, exact union over arbitrary
site25 inputs gives a singleton first-cell output through time95. At time96
it first admits both outputs, among2126 reachable rows. The predicted
autonomous-output closure fails. All1024 width8 local transitions agree
with a literal truth-table implementation; the zero-wall countercontrol
first admits black at tick8, as required. Unexpected check: complete
exterior paths for both outputs were retained and independently replayed
with literal Rule30; both pass. One path has every exterior input zero.

This only rejects using this fixed-width arbitrary-input relation as an
autonomous reset from time30. The two controlled paths have not been
extended to actual right halves. No failure of actual synchronization,
no failure of eventual synchronization, and no all-depth bound follows.
Stop this candidate; do not increase its width or horizon. GC1033's
entry-side correlation request remains independent and pending.

### GC1035 — CL203's strip propagation keeps the old boundary after the train fails

Specific defect blocking use of CL203's new conclusion, not a routine audit.
Record searched: `left.permut` + `cone` -> G97's iterated pivot identity;
GC1019/W283 already give the failed-gate phase change. Source read:
`rule30_cloud_train_block.py`, `entrymemory` propagation loop.

Prediction before the local check: after the failed gate at time62,
column6 at time63 is zero, whereas the loop supplies one. The resulting
column7 at time64 is wrong for every two-bit exterior completion.
Countercontrol: a successful gate retains the old boundary at time63.
Unexpected check: distinguish this definite boundary error from the
separate, purely conditional maximal-speed influence claim in CL203.

Outcome: boundary-error prediction and all four literal exterior controls
PASS. At time62 the proved slab and failed gate give sites5..7 = 101.
Thus x6(63) = 1 XOR (0 OR 1) = 0. The loop instead uses boundary1
because 63 mod4 is not2. Also x7(63)=1, so the true x7(64)=1 while
that loop produces0, regardless of the exterior. The reported equality
of the two propagated sets of231 is not presently evidence for loss
of actual entry memory. No verdict about the corrected propagation
is inferred. The initial SAT censuses are unaffected by this defect.

Repair: prepend the known six-cell slab to each retained twelve-cell
state, propagate all18 cells under the original clock, and apply the
same gate filters. This preserves the changing column6 boundary and
its correlations after failure. It does not require a new membership
census if the initial sets were retained. Cloud owns that repair.

CL203's light-cone explanation also needs qualification. G97 gives
x_(t+1)(t) = x1(0) XOR H_t(x2(0),...,x_(2t+1)(0)); cells strictly
beyond site t+1 do not depend on x1(0). The guaranteed toggle fixes
all the other initial bits. Comparing two families conditioned on
different leading observations does not fix those bits: CL203 itself
reports incompatible restrictions at initial site4. For example the
partial rows011111 and100000 have different first bits but both give
site2=1 after one tick. They are a masking control, not asserted full
history witnesses. Consequently a forced-cell conflict in the proposed
diagonal census does not follow from left permutivity; the crossing-
cones account remains a hypothesis. No such census is requested.

**GC1035 repair, CL204 independently replayed.** Using exactly the retained
19/31 source rows, an independently packed implementation reproduces
Cloud's common190-state terminal set. Unexpected check, predicted before
replay: the images first coincide *before* failure, at time59 (largest
set387). Thus the loss occurs while the six-cell slab is still valid;
the old post-exit boundary error is repaired but was not the source of
this particular loss. No membership census was rerun.

This gives a concrete limitation at time59, not merely at the chosen
endpoint75. Equal reachable18-cell sets have equal sets of future
controlled paths under the same clock and any identical future filters:
apply the same transition-and-filter operator inductively. Adding more
exit observations to this same row-only/free-exterior abstraction cannot
restore its distinction between the two entries. This statement is about
the supplied finite abstraction; actual histories can retain correlations
between its row and future exterior inputs, which it discarded.

The terminal joint projection (x7,x8) is {01,10,11}, not all four pairs.
In particular separate freedom of x7 and x8 cannot justify the pair00.
This is not a new entry-pinning proof or an actual-realizability claim.
The repaired abstraction is now checked and its limitation located;
no wider-window run is proposed.

**GC1035 merger mechanism (bounded follow-up).** Before extending the
representation, test the specific candidate of retaining the exterior bit
consumed at58. Prediction: that bit might distinguish the two images at59.
Counterfactual and unexpected check: first separate gate filtering from
transition loss. Replay refutes the candidate: at58 the sets have378/387
rows; requiring x7=0 reduces both to the identical310 rows, before the
update. All nine extra rows of the second set fail that gate. Updating
then gives316 rows at59. Hence even retaining that next exterior input
cannot recover the distinction. The checker now records the intermediate
sets. This sharpens the prior time59 report; it does not revise the190
terminal count. Stop this one-bit repair, with no memory-window sweep.


#### GC1036 — The cut's five released pins have an exact joint guard (2026-10-10)

Missing inference: replace CL198's requirement to explain all five released
pins by the particular joint restriction that blocks the final exit one.
This keeps the origin at time30; it is not another endpoint relocation.
New evidence CL205 shows why marginal freedom must not be read as independent
fillings. Record searched: `(16.*20.*21.*22.*24|five.*free|32 fillings)`
AND `(guard|pin|cut)` -> CL198's census/propagation, no joint predicate.
Predictions and counterfactual precede execution in
`rule30_cut45_pin_guard.py`; one width24, time30..88 propagation, no SAT
or membership census.

Hold CL198's other19 cells at time30 fixed to
100110011001100000000010. Write a,b,c,d,e for cells16,20,21,22,24,
which are its five released zero pins. Condition only on the suffix
observations at white ticks30..86 from the44-word. Allow an arbitrary
site25 input on every update. The exact controlled-strip predicates are:

    prefix-compatible <=> (a AND b) OR (NOT a AND NOT b AND NOT c AND NOT d);
    final1 possible   <=> a AND b;
    final0 possible   <=> (NOT a AND NOT b AND NOT c AND NOT d)
                         OR (a AND b AND (NOT c OR d)).

Labels use bit order a,b,c,d,e. The32 cases partition as:22 prefix-empty;
labels0,16 force final0; labels7,23 force final1; labels3,11,15,19,27,31
permit both. Thus e is irrelevant to these three existence predicates.
Either a=0 OR b=0 suffices to force the final0 for every exterior, provided
the other19 pins and suffix observations hold. Explaining all five released
zeros is unnecessary for this particular obstruction. This does not prove
either origin pin from the entry, or justify discarding the other19 pins.
Their actual-history forcing is inherited from CL198's reported SAT census.

The computation preserves correlations: each reachable row carries a bitset
of exactly those initial labels admitting it. Initially these are32 singleton
labels; transition unions and sample filters preserve that meaning by induction.
No state or initial label is projected away. Peak2554 rows, cap not reached.
Packed transitions agree with1024 literal Wolfram-table cases; six separate
literal propagations cover empty, zero-only, one-only and both branches.
All predicate identities on the32 labels pass. This is a finite computed
conditional implication, awaiting independent review, not an all-depth bound.

P1 (a nonzero filling still forces final0) and P2 (final1 existence upward
closed in these five bits) HELD. Adaptive P3 (all final1-admitting fillings
force final1) REFUTED by the six both-bit cases; no delayed-bit transport
identity follows. Unexpected check:22 fillings already fail the conditioned
prefix and cannot be counted as forced-zero examples. The sufficient
entry-side target is now the disjunction x16(30)=0 OR x20(30)=0 together
with the common19 pins, rather than a five-cell pinning proof. Next seek
that correlated origin restriction; no further filling or width sweep.

**CL206:** Cloud independently reproduced all32 joint predicates and accepted
their scope. The forward guard is confirmed. GC1037 below closes the
conditional origin disjunction by a different, exact backward relation.


#### GC1037 — Exact correlated past excludes the joint black origin (2026-10-10)

Missing inference: show x16(30)=0 OR x20(30)=0 from the entry observations,
retaining CL198's common19 pins. Record searched: `(cut45|CL198|GC1036|entrymemory)`
AND `(preimage|backward row|past strip)` -> no hit, including ledgers.
New evidence CL206 confirms the eight joint-black fillings are exactly the
forward final1-admitting cases. Test their correlated past, rather than
another forward marginal, affine approximation or larger window.
Predictions precede execution in `rule30_cut45_origin_past.py`.

For a child row y of width W and a fixed parent wall b, there are at most
four parent row/exterior pairs. Choose the two rightmost parent bits
x_W,x_(W+1) and compute, for i=W down to1,

    x_(i-1) = y_i XOR (x_i OR x_(i+1)).

Retain exactly the choices giving x_0=b. Every forward parent satisfies
this recurrence, and every retained choice satisfies every Rule30 update;
hence the enumeration is exact. The exterior bit remains free on each
tick. This inverse preserves whole-row correlations.

Start with the eight width24 rows having CL198's common19 pins and
x16=x20=1 at30. Apply that exact parent relation down to time0 with
wall(t)=t mod2, imposing q's observations only at ticks2,4,...,28.
Do not impose its leading sample at0. Each parent retains the bitset
of precisely those original fillings to which it has a compatible path.
Union and filtering preserve that meaning by induction.

Outcome: at time0 there are23 rows, **all with x1=1**. The only source
labels still admitting any past are7,23,31 (bit order16,20,21,22,24).
Thus no leading0 entry reaches a joint-black origin under the common19
pins, even with arbitrary site25 inputs throughout the past. This proves
the required conditional disjunction in the controlled-strip model.
Together with GC1036's forward guard it excludes the last exit1, provided
the common19 pin premise holds. Their actual-history forcing is inherited
from CL198's reported SAT census, not proved anew here.

P1 (no leading0 past) and P2 (some leading1 past) HELD. Peak261 rows;
no cap reached. All512 width8 child/wall parent sets agree with independent
literal forward images, and exhaustive six-tick width6 forward histories
agree with the backward relation for two target rows. Wall-phase countercontrol
passes. A nonvacuity check caught the original control target0 having no
admissible forward history; controls were repaired with targets18/60 and
explicit positive initial rows0/8, and the full result replayed unchanged.
Unexpected check: five of the eight source fillings have no past
with either lead; surviving labels force x21=1 and x22 implies x24.
Nonempty leading1 paths are controlled histories, not newly constructed
actual right halves. No SAT call or actual-language census was made.

This closes the bounded origin correlation conditional on the common
pin premise; it is an exact computation independently confirmed by Cloud CL207
(b09e3e3c:23 leading1 rows, peak261, source labels7/23/31).
The remaining hand account is why the entry and exit together force the
common19 pins, and how to extend this mechanism beyond the fixed cut to
an all-depth certificate. No wider-past or memory-length sweep is proposed.


#### GC1038 — Locate the missing exterior correlation in the origin guard (2026-10-10)

Missing inference: does GC1037's backward exclusion require distant common
pins, or does the pinned prefix through15 suffice? Record searched:
`(origin|cut45)` + `(prefix15|width20|first15|first 15)` -> no hit, including
ledgers. One width20 controlled past, first15 pinned, sites16/20 black,
17..19 free. P1 (exclusion, confidence0.4) REFUTED:42 leading0 initial
rows, peak743. Independent literal replay reaches origin
`10011001100110010001` from `01111110011110000000` with exterior stream
`000000100000100000011000010011`. Unexpectedly this origin also obeys
pins17..19, so those three discarded pins do not explain this path.

Adaptive P2, registered before the next check: releasing only pin23 in
GC1037's width24 model admits a leading0 past (confidence0.7). REFUTED:
no leading0 past, peak310. The other18 common pins already imply the
backward disjunction. The original pin23=1 branch remains empty as required;
GC1037's literal parent and nonvacuous six-tick controls pass. The first
P2 implementation failed to clear pin23's original1 before OR-filling;
it repeated the original premise and was discarded. A source cardinality
guard now requires16 distinct fillings, eight at each pin23 value; the
repaired replay gives the stated result. A leading1 countercontrol with
the original pin23 value survives, so the exclusion is not an empty
source or an impossible entry irrespective of its lead. This does
not weaken GC1036's forward hypothesis, which still uses common19.

The explicit width20 path is not extendible even by one actual exterior
column: at ticks6,12,20,25 it has x20=0, x21=1, x21(next)=0. The local
rule forces x21(next)=1 independently of x22 whenever x20=0,x21=1.
Thus a projected past can falsely restore an origin even though the
omitted pin23 itself is dispensable. This is GC1022's already-known
exterior-update defect in a specific new counterexample, not a new
boundary method. A failed weakened guard is not an actual-language
witness or a refutation of the cut. No SAT or membership census.

Retain this failure and stop deleting premises. The common-pin forcing
lemma and an all-depth invariant remain missing; width growth and a
blind pin-subset sweep are not proposed. Script:
`tests/probes/lexicon/rule30_cut45_past_support.py`.


CL207 receipt: its independent GC1037 replay is accepted. Its forward
common-pin test leaves581 width24 origins and2282 width26 origins from
first8 fixed sites, with no other common pin. This excludes suffix-only
pin forcing. The test omits q's full past, so it does not exclude a
joint entry-and-exit derivation at those widths. Keep that precise
remaining target; no wider strip or repeat census requested.


#### GC1039 — Joint entry/exit compatibility discharges the common-pin premise (2026-10-10)

Missing inference: CL207's suffix-only survivors omit the entry's exact
past; does their joint compatibility force the common19 pins? Record
searched: `(CL207|581|common.pin)` + `(joint|past|entry)` -> GC1038 scope
correction, no joint computation. P1 (common19 forced,0.45) and P2
(nonempty joint relation) HELD. No SAT or actual-language membership call.

At width24, reconstruct CL207's581 suffix-compatible origins at30 from
first8=10011001, car/exit samples to86 and proved gates34..62. Keep sets
of whole rows at each tick; reverse exact edges through those sets to
recover the origin relation without huge provenance bitsets. Then reverse
those origins to0, retaining source labels and imposing q's complete
entry, including its leading0. Exactly TWO origins remain:
`10011001100110000000001?`. They have45 initial rows; past peak2857;
future peak65536. Thus joint compatibility fixes all first23 cells,
stronger than the common19 claim. The prescribed pinned row survives.

The remaining first8 premise is also discharged, rather than inherited
from CL198's SAT census. GC1027 gives sites1..7=1001100 at34. A width12
exact reverse relation with q's white observations20..32 leaves only
row30 prefixes10011000 and10011001 (peak95). P3, that this short support
lemma fixes all8, was REFUTED; it fixes7. CL193's actual positive seed
survives this implication by independent literal simulation.

Adaptive P4, registered before its run: the SAME width24 joint relation
with first8=10011000 is empty (0.8). HELD:4975 suffix-compatible origins
but NO leading0 entry past, peak7300. No cap or width was increased.
The two branches for cell8 are exhaustive, so first8=10011001 follows
from the full entry/suffix join and the proved first7 support.
Consequently all19 common pins follow without any inherited pin census.

Soundness: every actual44-prefix realizer satisfies GC1027's slab and
successful gates34..58, and its first exit0 forces the failed gate62.
It therefore enters the width12 support relation, then exactly one of
the two width24 origin branches. Every actual path is a controlled-strip
path, and reversing exact parents with whole-row labels preserves its
origin. The absence in the wrong-cell8 branch and the two origins in
the other branch prove the pin statement. GC1036's reviewed forward
guard then forces the45th symbol0. GC1037 remains a correct independently
reviewed intermediate implication; its pin premise is now discharged.
This is a finite correlated-strip explanation of the already verified
cut, not an all-depth bound or a new actual-language verdict.

Controls:512 literal parent tables, nonvacuous six-tick forward/backward
checks, and an independent exhaustive six-tick literal comparison of
whole-graph origin extraction (seven positive sources) PASS. Unexpected
checks reproduce CL207's581 origins and retain the pinned row; neither
join nor support lemma is vacuous. First7 support uses an actual model
with the correct clock. Script `rule30_cut45_joint_origin.py`; second
reading requested. Next: identify a reusable bidirectional invariant
for the recurrent language; no origin-window or pin-subset sweep.


Concurrent receipt: L605 (bb73fa22) and CL209 (9a341423) establish the
same width24 cut by formally checked strip CNF and independent replication.
Their verdicts were not re-run here. GC1039's local train deductions
require at most nine columns; they hold inside a width24 strip too.
Thus the computation assembles the strip obstruction, rather than
assuming exact-cone pins. A human-sized reusable invariant is still
missing; no extra width or pin test is proposed.

#### GC1040 — A clock-selected parent plateau, without a spatial reset (2026-10-10)

Missing inference: what small structural correlation survives at GC1039's
two joint origins? Record searched: `(preimage|parent|backward)` +
`(0101|1010|reset)` -> G13's exact single-row scanner; GC1010/1012 use
a different two-update source automaton. G13 read, not reproved. The
specific `1(0011)^m` plateau transfer was not found before this block.

P1, both surviving origins spatially reset, was REFUTED: the origin with
site24=0 has scanner rank1, but site24=1 has rank2. P2 HELD: under the
time29 wall, both fix the SAME first21 parent bits,
`000011010000111111111`. This follows from a parametric hand identity,
not from their finite enumeration. It needs only the shared first22
child bits; sites23 and24 do not enter the proof.

**Hand lemma (PROVED, independently read in CL210).** If a Rule30
child row begins `1(0011)^m 0^r`, m>=0, r>=1, and its parent wall is b,
then parent sites4m+1..4m+r are all c=1 XOR b XOR (m mod2).
The preceding m four-bit parent blocks, read from right to left, are
0000 when the entering c is1, and1101 when it is0; c flips after each
block. These assertions hold for every completion beyond the prefix.

Proof. A zero child at j gives x(j-1)=x(j) OR x(j+1). Two consecutive
zero children make x(j-1)=x(j), so r zeros fix a constant parent plateau
of length r. At its left edge the pair (x(4m+1),x(4m+2)) can only be
00,10 or11, even when r=1. The inverse scanner step is
(a,d) -> (y XOR (a OR d),a). Reading one0011 block from right to left
means reading1100. Its exact transfers, with the four newly generated
parent bits listed in spatial order, are:

| entering pair | outgoing pair | parent block |
|---|---|---|
| 00 | 11 | 1101 |
| 10 | 00 | 0000 |
| 11 | 00 | 0000 |

Thus the first block replaces the entering plateau c by1-c; subsequent
blocks swap00 and11. After m blocks the pair is (d,d), d=c XOR(m mod2),
unless m=0 when the original allowed pair remains. The leading child1
gives wall b=1-d in the first case and b=1-c in the second. Solving gives
the asserted c. The block table supplies the entire prefix formula.

For GC1039, m=3,r=9,b=1, hence c=1: the black parent plateau occupies
sites13..21, preceded by0000,1101,0000. This explicitly carries origin
information through a nonlinear plateau selected by the clock. A
universal spatial reset is unnecessary; this is an exact conditional
selection rather than a new unary or global affine explanation attempt.

Controls: independently literal-forward reconstructed all admitted
parents of both origins; all252 terminal-pair cases with m0..6,r1..9
match the formula. The proof, not those finite cases, supplies its full
quantifiers. Unexpected retained failure: the proposed r=1 counterexample
did not exist, causing an assertion failure after224 controls passed.
The three-pair table explains why the lemma extends to r=1. At r=0,
child10011 admits parent11100 with wall0 and exterior1; its first parent
block1110 contradicts the predicted1101. The zero hypothesis matters.
Instrument: rule30_cut45_origin_scan.py. No SAT, new language query,
width sweep or additional past window. Next use this explicit plateau
transfer to compress the joint-past mechanism; full cut pin forcing
remains GC1039's computation and an all-depth record bound stays open.

#### GC1041 — Plateau grammar retains a two-tick phase guard and a white halo (2026-10-10)

Missing inference: GC1040's prefix grammar loses maturity and the clock
unless these are proved as part of its hidden representation. Seek a
phase/age clause valid at every later time, not another finite cut census.
Record searched: `(100110|0011)` + `(black|two.step|prehistory)` ->
GC1017's white train slab, GC1004/1005's one-black-update exclusions,
and GC1010's opposite-order two-update marker. All read. The new clause
is on spatial strip states, not a temporal forbidden factor or a new
S/L recurrent restriction.

**Hand phase guard (PROOF-SKETCH).** At any black clock time of age>=2,
the right row cannot begin100110. In particular it cannot begin
`1(0011)^m 0^r` with m>=1,r>=1. This uses only six columns and the two
preceding clock ticks, so it holds within every controlled strip of
width>=6 with an arbitrary exterior, as well as actual configurations.

Proof directly from Rule30, independently of GC1040. Let y=100110 and
its white-wall parent be a. The zero outputs2,3 give a1=a2. Output1=1
gives a1=a2=1. Output6=0 gives a5=a6 OR a7. Thus output5=1 gives
a4 XOR a5=1, so a4 OR a5=1. Output4=1 then forces a3=0. Hence the
parent begins110 (indeed1101000). This has no black-wall predecessor:
the first two output ones force preceding cells1,2,3=001, making the
third output1. This last three-cell obstruction is GC549, already
used in GC1004/1005. Both older clock ticks exist when the age is>=2.
The entire parametric family has the forbidden six-bit prefix.

The phase and age cannot be omitted. Literal two-step shrinking cones
give white-phase source00000100 ->100110, and black-phase source00111000
->100111 (so removing the sixth symbol admits the prefix). At age1,
the white-wall parent1101000 produces100110. P1/P2/P3 HELD in the
256-source, two-phase controls; these positives are replayed. The hand
contradiction, not enumeration, proves the unbounded-age assertion.

**Quantitative halo, also by hand.** In GC1040, when the selected c=0,
the parent's white plateau extends TWO further sites:4m+1..4m+r+2.
The last zero child has left parent c=0 and therefore its other two
parent bits are both0. If c=1, those two terminal bits have OR1 and
can be01,10 or11. Thus the two choices of parent-wall parity select
exactly ONE versus THREE right terminal pairs at this prefix boundary.
The 252 previously bounded m0..6,r1..9 literal cases pass this additional
halo/count control. These count terminal pairs, not histories or seeds;
no independent-coin assumption or uniform record contraction follows.

For GC1039's m3,r9 white-clock origin, c=1, so the black plateau carries
three boundary-pair alternatives. A proposed invariant must retain that
nonlinear choice and the phase/age guard. For the opposite phase, the
same spatial origin has no mature history. This supplies explicit
obligations for the plateau representation; it does not close the entry
join or bound R_real at every depth. Next seek a closed transfer that
also retains the actual entry observations, rather than increasing a
row or window census. Instrument: rule30_plateau_phase_guard.py;
second reading requested, no Local solver job.

#### GC1042 — Exact exterior repair has four-row guards; a greedy lift fails the actual train (2026-10-10)

CL210 received at7d80e457: GC1039 independently CONFIRMED, including
the first7 support and empty wrong-cell8 branch; GC1040's hand plateau
identity CONFIRMED. Their second readings are accepted, without a rerun.
JP4's five origins and common19 pins retain the correct-cell8 premise
and the suffix/gates; samples2..28 alone without those premises were
not tested. GC1041's phase/halo reading remains pending.

Missing inference in CL210's halfwidth proposal: when can a strip's
free exterior be made an updated column, keeping its whole interior?
A useful result is an exact local projection, with a constructive
completion and its iteration limits. Record searched:
`w_min|half.cone|quarter.cone|halfwidth` -> SW/SWP and CL210;
`column extension` + `local|two equations` -> GC380/381's specific
profile graph, GC754's specific exterior death, GC798's different
diagonal-OR projection. These were read; their update identities are
reused. No new language, SAT or strip-width census.

**Hand theorem, PROOF-SKETCH.** Let u(0..T-1), v(0..T) be two adjacent
temporal tracks, T>=1. We seek w(0..T), z(0..T-1) such that BOTH
v'=u XOR(v OR w) and w'=v XOR(w OR z) hold through T ticks.
Put q(t)=v(t+1) XOR u(t). Such w,z exist if and only if:

- v(t)<=q(t), the existing one-column condition;
- A: no t<=T-2 has v(t)=v(t+1)=0 and q(t),q(t+1)=1,0;
- B: no t<=T-3 has v(t..t+2)=010 and q(t)=q(t+2)=1.

The last two guards use two/three positions of (v,q), but q uses the
next v, so the native strip constraints span at most FOUR rows.
This is an exact projection of width W+1 onto width W, at EVERY
horizon: take u,v as its last two columns (u is the wall when W=1).
All interior rows and the visible observations are preserved.

Necessity: where v=0, w=q is forced. A would force w(t)=1,
w(t+1)=0 with left input v(t)=0, contradicting w's update. In B,
w(t)=w(t+2)=1. The zero v(t) forces w(t+1)=1, then the black
v(t+1) forces w(t+2)=0, another contradiction. Where v=1,
the first update already requires q=1.

Sufficiency is explicit. Set w(t)=q(t) where v(t)=0. Where v(t)=1,
set w(t)=1 exactly when t>0, v(t-1)=0, q(t-1)=1; otherwise set0.
If v(t)=0,w(t)=1, A ensures a following zero v has q=1, while
a following one v receives w=1 by construction. If v(t)=1,w(t)=1,
the previous v was zero with q=1: a following zero v has q=0 by
B, while a following one v receives w=0. Thus every black w(t)
has w(t+1)=1-v(t). At the final row choose w(T)=1-v(T-1) if
w(T-1)=1, and0 otherwise. Then set z(t)=w(t+1) XOR v(t) where
w(t)=0, and0 elsewhere. Both literal equations hold. The same
construction works on one-sided infinite tracks, without a terminal
choice; this is still only one added updated column.

**Concrete failure of greedy iteration, inside the proved eternal
train.** The actual right seed1001 under the white-start clock has
u=010 and v=1100 for its first three ticks (GC1020 proves its eternal
continuation). The canonical repair above chooses w=0000. An updated
w would force z(0..2)=110. At t=1, however, left w=0 and centre z=1
force z(2)=1, contradicting0. No farther column or terminal choice
can fix this. The actual w=0100 has a literal continuation from1001.
Hence choosing one repair and repeating it can reject an ACTUAL
visible word; an invariant must keep optional repairs correlated.
This refutes that completion algorithm, not w_min(f)<=|f|.

P1 (exact guards) and P2 (greedy failure on the positive train) were
registered before controls and HELD. Independent existential checks
using the literal Wolfram table cover2728 arbitrary track pairs at
T=1..5;414 positive constructions replay. Unexpected B-only negative
u=011,v=0100 passes the base condition and A but has no repair.
Finite endpoints remain free. The hand proof supplies the unbounded
quantifiers; the bounded controls do not certify the halfwidth claim.
Instrument: rule30_exterior_repair.py. Next retain the FULL repair
relation when testing CL210's completion idea; no greedy lift, new
solver job, wider census or claimed quarter-cone law.

#### GC1043 — The black-wall phase data test a different game; the true free record at depth3 is4 (2026-10-10)

Specific defect in an owner-authorized proof question: KIMI-QUESTIONS-3
D defines the correct black-start clock, but imports WA3's opposite
mandatory parity. Correct this before a phase-transfer proof is attempted.
Record searched: `R°|other.phase|opposite.phase|black.start` +
`record|free` -> question D, WA3, RULE30-PRIZE8.39, GC549 checkpoint22.
Those read. WA3's first_failure ALWAYS checks odd times, even with
phase1. Its measured R(d-2) concerns that different game. This is not
a rejection of its measurement or of phase-correct R_real certificates.

At a black wall time, the wall's own update is
0=x(-1) XOR(1 OR x(1)), requiring x(-1)=1. Thus white-start clocks
test odd times, while black-start clocks test EVEN times, including0.
WA3 intentionally kept its odd-time condition when flipping the wall;
its later interpretation as the true phase-shifted record is unsupported.

**Hand refutation of D, PROOF-SKETCH: R°(3)=4, not R(1)=1.** To have
five initial zeros at depths3..7, only the first two bits a,b remain
in the determining seven-cell cone. If a=0, the even-time condition
fails at0. If a=1,b=0, it fails at2: the nearest bit at time1 is1-b,
and the next-nearest is1, so the nearest at2 is b. The remaining
case a=b=1 has the following exact shrinking rows in DEPTH order:

    t0: 1100000
    t1: 011000
    t2: 10110
    t3: 1001
    t4: 111
    t5: 00
    t6: 0

It fails at6. No deeper initial bit reaches the tested cell earlier,
so every length5 zero band from depth3 is impossible.
Conversely, the black-start inverse-column construction with visible
prefix101 gives initial depths1..7 equal1100001. Literal evolution
has nearest track1011101, black at0,2,4,6. Taking all later visible
symbols0 in that same inverse construction completes an infinite
formal forced left half. Hence its zero band at depths3..6 has
length4. This uses the FREE visible model, not an autonomous right
half or a new actual-language witness.

**All-depth parity guard on any finite phase record.** Left permutivity
makes the condition at time t solve uniquely for initial depth t+1,
given shallower cells. For a black-start clock, odd depths are forced
and even depths free; a free even-depth bit can be changed without
altering any shallower cells. A maximal finite zero run therefore
ends just before an ODD depth: d+R°(d) is odd. In the white-start
game the corresponding endpoint is even (the existing triangular
coding used in C2). So whenever R(d-2) is finite, it cannot equal
R°(d): its proposed endpoint d+R(d-2) is even. The quoted finite
phase-shift values have the wrong parity throughout, independently
of the depth3 control. No new bound on either phase follows.

P1 (R°(3)=4) was informed by the hand calculation before controls
and HELD. P2 is the source-scope finding above. Independent literal
shrinking cones and packed updates agree on the four forbidden-band
cases; inverse columns independently recover the positive1100001.
Unexpected empty-pattern control fails the mandatory even test at0
while passing the wrong odd test at1. The positive11 pattern instead
passes the even test and fails the odd test at1. Instrument:
rule30_black_wall_scope.py; no SAT, record extension or Local run.
Cloud asked to correct D's supplied data and the phase interpretation,
then independently read this refutation. Next return to the correlated
exterior lift; CL210's halfwidth and the prize bound remain open.


#### GC1044 — Two-column exterior repair retains every choice in a binary relation (2026-10-10)

Missing inference, CL210: GC1042's greedy completion loses an actual
train. A useful concrete advance is an exact representation of ALL
repairs admitting two additional updated columns, with no choice
selected prematurely. Record searched: `2.SAT|bijunctive|binary clause`
+ `repair|column|exterior` -> two unrelated SAT probes, no such repair
lemma; GC1042's exact guard equivalence is reused. No Local solver,
membership, width or language census. L607 at b3da78b3/8533dbe5 read:
WA3 phase correction accepted, matching-parity R_real unaffected;
122's both-phase cake_lpr receipt and128's validated witness accepted
with Local's stated provenance, without a duplicate run.

**Hand theorem, PROOF-SKETCH.** Fix u(0..T-1), v(0..T), T>=1,
and q(t)=v(t+1) XOR u(t). The complete set of w(0..T) for which
there exist z(0..T), h(0..T-1) satisfying ALL THREE equations
v'=u XOR(v OR w), w'=v XOR(w OR z), z'=w XOR(z OR h)
is the following binary-clause relation. If any v(t)=1,q(t)=0 it
is empty. Otherwise impose:

- w(t)=q(t) wherever v(t)=0, t<T;
- for every t<T, NOT w(t) OR [w(t+1)=1-v(t)];
- A, t<=T-2: if v(t)=v(t+1)=1, w(t) OR NOT w(t+2);
  if v(t)=1,v(t+1)=0,q(t+1)=0, w(t) OR w(t+2);
- B, t<=T-3, only when v(t)=q(t)=0:
  if v(t+2)=q(t+2)=0, NOT w(t+1) OR NOT w(t+3);
  if v(t+2)=v(t+1)=1, NOT w(t+1) OR w(t+3).

Here the equality in the second item is a literal since v is fixed.
The terminal w(T) remains a variable; no update or q(T) is invented.

Proof: the first item is exactly v's update, and the second is exactly
GC1042's base guard for the pair v,w. Apply its A/B guards to that pair,
with r(t)=w(t+1) XOR v(t). A requires w(t),w(t+1)=00,
v(t)=1 and w(t+2)=v(t+1). If v(t+1)=1, w(t+2)=1
already forces w(t+1)=0 by the base guard, giving the first A clause.
If v(t+1)=0, w(t+1)=q(t+1) is fixed; it either eliminates A
or gives its second clause. These exhaust A.

B requires w(t..t+2)=010 and r(t)=r(t+2)=1. Its first r
forces v(t)=0, hence w(t)=q(t)=0. If v(t+2)=0, w(t+2)
is fixed; when it is zero, B is precisely w(t+1)=w(t+3)=1.
If v(t+2)=1, w(t+1)=1 forces w(t+2)=1-v(t+1): B
is impossible unless v(t+1)=1, when it reduces to w(t+1)=1,
w(t+3)=0. These are exactly the two B clauses. GC1042 then constructs
z,h for every accepted w. Necessity and sufficiency hold at every T.

There are at most4T clauses on T+1 variables, each spanning at most
four rows. The full repair relation has an exact eight-state scan
(remember the last three w bits), or a linear-size implication graph;
2-SAT decides nonemptiness in linear time. This retains correlations
and ALL options, rather than the exponential list of optional assignments.
It is the exact projection of a width W+2 strip onto a FIXED width W
history. It is not a fixed-size automaton for the entire visible language:
its coefficients depend on u,v. Further spatial projection need not
preserve binary clauses, and CL210's halfwidth/all-depth bound stays OPEN.

**Actual-train inference.** Literal seed1001 beside the white-start
clock has u=0101, v=11001, so q=1100 and w(2)=w(3)=0.
The second A clause at t=1 gives w(1) OR w(3), forcing w(1)=1;
the base clause at t=0 then forces w(0)=0. Thus every two-column repair
has first pair01, the actual train's pair. The selected00 repair fails
for an interior reason through this complete four-tick cycle.

P1 (all-choice clause equivalence) and P2 (forced pair01) registered
before controls and HELD. All18,720 arbitrary u,v,w triples through
T=1..4 agree with independent literal existential enumeration of z;
324 accepted repairs construct and replay all three equations. Unexpected
endpoint check: at T=3, w=0001 repairs the actual v=1100, whereas
GC1042's selected0000 fails. At T=4, its would-be terminal site3 is
prescribed zero, so the first00 cannot be saved. Instrument:
rule30_exterior_binary.py. Next missing inference: whether correlated
repair choices admit an invariant under further spatial extension,
without presuming this binary class is closed. No new worker run.


GC1044 publication checkpoint: the one allowed recovery fetch brought
Cloud's CL211/CL212 at021228ad. GC1041's phase/halo proof and GC1042's
hand repair theorem are CONFIRMED independently (699,048 pairs through
T=9 for the latter), and GC1043's phase refutation is ACCEPTED with an
independent R°(1..12) fill. These second readings are accepted. GC1044
alone still awaits review. The composition question in CL211 is useful;
no additional cut45 width24..88 census is requested before identifying
what correlation that composition must preserve. No all-depth bound.


#### GC1045 — Fixed-track binary repair does not lift to a joint binary model (2026-10-10)

Missing inference after GC1044: can its all-choice representation be
composed when the preceding track is also unknown, as it is between
RRL's white-time samples? A useful obstruction would separate fixed
coefficients from an exact joint binary model. Record searched:
`bijunctive|majority.closure|binary.clause` + `repair|exterior|projection`
-> GC1044 and its index, no prior closure result. The standard binary
clause majority argument below is elementary, not claimed as new.

The registered single-horizon diagnostic (T=6, width4, both clocks)
found no majority counterexample in the next-track relation at ANY
fixed preceding track. P1 held only on that finite object; P2's demand
for three actual positives was not triggered. Literal/packed updates,
actual-seed inclusion and GC1044 binary-relation controls pass.
This is inconclusive evidence for FIXED-track closure. No larger sweep.

**Hand obstruction, PROOF-SKETCH; EVERY horizon T>=1, both phases.**
The exact JOINT relation of the first two tracks v,w beside a clamped
clock is not the existential projection of any binary-clause formula
on these track bits, however many binary auxiliary variables are added.
Take the three actual clamped finite right seeds1010,0100,0000.
In the white-start phase their first two readings (v,w) are respectively
(11,00), (01,11), (00,00). Their pointwise majority is (01,00),
which violates v(1)=0 XOR(v(0) OR w(0)): the required value is0,
not1. All three positives have actual infinite clamped continuations;
the majority fails the very first equation, at every longer horizon.
In the black-start phase their pairs are (10,00), (00,11), (01,00).
Their majority (00,00) requires v(1)=1 and again fails. Same seeds.

Why auxiliary bits cannot fix this representation: if a binary clause
fails on the majority of three assignments, each of its two literals
fails in at least two of them. Those sets intersect, so one assignment
already failed the clause. Thus solutions of every binary formula are
majority-closed. For an existential projection, choose witnesses for
three positives and take their majority, auxiliary bits included; it
remains a witness. The actual joint relation above is not closed, so
no such exact binary formula exists. This is a coordinate-specific
representation obstruction, not a claim about arbitrary hidden encodings.

Unexpected scope check: delete v(1), the unobserved odd-time bit.
The remaining majority v(0)=w(0)=w(1)=0 has the actual0000
completion (v(1)=0 in white phase,1 in black). The example therefore
supplies NO absent visible word and does not refute fixed-v binary
closure, CL210's halfwidth claim or all finite-language certificates.
Independent literal cones verify both phases and this deleted-bit control.
The nonlinear coefficient must be retained or encoded explicitly; the
GC1044 implication graph cannot simply treat it as another binary variable.
No further closure scan or worker computation requested. Instrument:
rule30_exterior_majority.py. Next hand target is a coefficient-typed
composition invariant, with fixed-track closure still OPEN.

Publication checkpoint: Local integrated6d9dfff5 (39447e59), resolving
last tick's two main races. SLC3 at ea9a2e88 adds22 verified cuts65..114
and lowers entropy0.1192 to0.1171; both predictions refuted. Accepted
with Local's source attribution; no duplicate solve or certificate audit.


#### GC1046 — Mixed S/L collars have three types; their ambiguity sits at LLS junctions (2026-10-10)

Missing inference for CL213's typed composition: a finite, sound coefficient
alphabet for mixed synchronized S/L histories, retaining the hidden long
branch that visible letters miss. Record searched: `1011011100` -> GC744;
`0110010011|1010110101` with `S/L|long|slab|column` -> no mixed
alternative-L collar theorem. Reuse GC606/607, corrected GC609,
GC622/623/625/626 and GC706; their returns are not claimed anew.
P1/P2 and terminal counterfactual registered in rule30_sl_collar.py before
its independent controls. No SAT, cut extraction or width census.

**Hand result, PROOF-SKETCH.** Let c0(t)=t mod2 be the externally
clamped wall; no finite full configuration carrying that clock is assumed.
At a white-time marker1110, every S/L
interval that also closes at marker1110 has exactly one of these types.
Entries are initial spatial cylinders; strings are times0 through D-1.

| Type | Entry | D | c1 | c2 | c3 | c4 |
| --- | --- | --- | --- | --- | --- | --- |
| S | 11101 | 6 | 110100 | 101100 | 100001 | 001111 |
| L0 | 111001 | 10 | 1101000100 | 1011011100 | 1010110001 | 0110101111 |
| L1 | 111000001 | 10 | 1101000100 | 1011011100 | 1010110101 | 0110010011 |

Completeness follows from GC623's disjoint prescribed-long cylinders and
GC624/625's marker-return requirement; marker S starts with fifth bit1.
GC606's even prefixes11101,01011,0001,1110 and intervening prefixes
1000,1101,0011 give the S collar. GC744's ordinary-L shielding uses only
entry111001 and closing1110. GC607 supplies that closing marker for
EVERY tail of111001, so the following visible letter need not be L.
The strengthened prefixes of GC622 give L1: at times 0..10 the first
four bits are1110,1001,0111,1100,0010,0111,0100,1110,0001,0011,1110.
These are local shielded identities, not sampled profiles. All three
cylinders close regardless of farther initial tail.

Corrected GC609 gives S -> S or L0; GC622 gives L1 -> S. Consequently
any consecutive synchronized types obey the finite necessary graph

    S -> {S,L0};  L0 -> {S,L0,L1};  L1 -> {S}.

The L0 row does NOT assert that its every tail renews: only when the next
interval is a marker-return S/L interval does GC623 classify it. Nor
are arbitrary paths through this graph asserted realizable. In an
interior interval L1 therefore occurs only as L0,L1,S, projecting to
visible LLS. Both L types have identical c1,c2, and differ in c3 ONLY
at time7 (0 versus1); their c4 differences are exactly times4,6,7.
Thus a fixed synchronized visible K-gap word determines its entire
four-column collar except for at most one binary choice at each LLS
junction, plus the two boundary intervals. If N_LLS counts its internal
LLS factors, the number of actual four-column collars is at most
2^(N_LLS+2). This is an upper bound on collar multiplicity, not a
realizability claim or a bound on left-hand records.

**Exact interface equations.** For each type the site4 update with a
proposed next track c5 is equivalent to the following units; all its
other times have black c4 and are shielded. The closing sample c4(D)=0
is included when evaluating the last update.

    S:  c5(0)=c5(1)=1.
    L0: c5(0)=0, c5(3)=1, c5(5)=0.
    L1: c5(0)=c5(3)=c5(4)=c5(6)=c5(7)=0.

Indeed, at each listed white time, c5(t)=c4(t+1) XOR c3(t);
at black times the table directly satisfies c4(t+1)=1 XOR c3(t).
Concatenate these translated units to obtain ALL boundary input tracks
that produce that typed four-column band. The next track's OWN updates
and its actual past remain obligations. This exact interface relation
is the finite coefficient object for further correlated extension;
it must not be promoted to a closed exterior or an all-depth certificate.

**Independent and unexpected controls.** Literal shrinking cones and a
separate packed engine agree on all 1,280 full cylinder assignments with
six sites retained at the closing time. P1 and P2 HELD: ordinary L has
both following S and ordinary-L entrances, with the same collar. It also
has returns outside those two simple cylinders; these are retained.
All 128 complete cones of111000000 still emit visible L but miss marker1110.
Thus a final visible L without a prescribed hidden return must be exempt.
GC626 synchronizes arbitrary-start S/L words at their internal boundaries;
apply the collar to the middle intervals after deleting the first and
last gaps. Initial1101/1111 and a terminal failed L are not erased by fiat.
No new all-depth bound, and no solver work requested.

CL213 at 57032c74 is accepted: GC1044's fixed-track binary repair and
GC1045's direct joint-track obstruction are independently CONFIRMED.
Further fixed-track spatial closure remains OPEN; the joint obstruction
does not refute it. The present collar localizes a finite hidden fork,
but the relations carried by its fifth and farther columns are not yet
closed under composition. Next hand target: transport those correlated
relations across an LLS switch without discarding the exterior past.


#### GC1047 — An ordinary long loop has exactly three fifth tracks; a zero pair travels through its return (2026-10-10)

Missing inference after GC1046: what actual correlation crosses an
L0 -> L1 switch beyond the four-column collar? Record searched:
`0101100000|0101100101|0101101010` with `fifth|c_5|column.?5|long|L0`
-> wheel substrings and ALS/ALX's two sampled all-L fifth profiles,
not an all-tail selector theorem. Reuse GC744's prefix010110 and
GC619's exceptional cylinders; no new solver or language census. GC744 gives the common four-column
collar and the first six samples of column5; only the remaining
correlated selector is new here.

**Hand result, PROOF-SKETCH.** Let the wall be externally clamped to
c0(t)=t mod2 and the initial right row start111001. At time5 put
z=c6(5), a=c7(5). Every farther initial tail obeys this complete table
for the ten pre-return samples of column5:

| Mid-pair (z,a) | c5(0..9) | Return pair (c5(10),c6(10)) |
| --- | --- | --- |
| 00 | 0101100101 | 00 |
| 01 | 0101100000 | 01 |
| 1* | 0101101010 | 01 or a pair starting1 |

In particular the closing pair is00 iff the mid-pair is00. This is an
exact correlated transport by five ticks and one column to the left,
not a claim about independently assignable bits. When the next S/L interval ALSO closes at marker1110,
fifth profile0101100101 selects next type L1;
0000 selects L0, while1010 permits S or L0. The untyped last column
remains an interface, not an invariant autonomous exterior.

**The ancestry shield missing from a free-row argument.** At time2
write (u,v,p,q)=(c7,c8,c9,c10). If u=v=0, then (p,q) cannot be11.
To see this, write initial sites7..10 as b,c,d,e and time1 sites7..10
as X,Y,Z,H. Then X=NOT(b OR c), Y=b XOR(c OR d),
Z=c XOR(d OR e), u=NOT(X OR Y), v=X XOR(Y OR Z).
The two zeros imply X=1: X=0 would force Y=Z=0, contradicting
X OR Y=1. Thus b=c=0, Y=d, Z=d OR e=1 and p=NOT d.
If p=1, then d=0,e=1, hence H=1 and q=Z XOR(H OR right)=0.
This is the four-cell correlation; no farther input is assumed free.

Now let (A,B,C,D,E)=(c6,c7,c8,c9,c10)(4). GC744 gives c5(4)=1,
so z=NOT(A OR B), a=A XOR(B OR C). If z=a=0, then A=1;
otherwise B=C=0 contradict z=0. Since A=NOT(u OR v), this forces
u=v=0. Their two-step updates give B=p, C=p OR q. The second
mid-zero further gives p OR q=1. The preceding shield leaves only
(p,q)=10 or01. In case10 the time4 tuple is(1,1,1,0,0);
in case01 it begins(1,0,1,1), with E immaterial. Therefore at time5
(c6,c7,c8,c9)=(0,0,P,1-P) for some actual P. This complementarity
is essential: a free row with all four zero would fail the claimed
return and would not have this ordinary-L ancestry.

**Transport and the two other cases.** For the complemented mid-row,
local updates give

    time6: (c5,c6,c7,c8)=(0,0,P,1);
    time7: (c5,c6,c7,c8,c9)=(1,P,1,1-P,0);
    time8: (c5,c6,c7,c8)=(0,0,1-P,P);
    time9: (c5,c6,c7)=(1,1-P,1);
    time10: (c5,c6)=(0,0).

The zero at time7 site9 is shielded in both P cases: if P=0 its
left predecessor at time6 is1 and its centre1; if P=1, the two
right predecessors are NOT r and r OR s, whose OR is1.
Together with the known c5 prefix010110 this proves row00 of the table.
If z=0,a=1, the black c6 at time6 stays black through time10,
while c5 stays zero, giving row01. If z=1, the next pairs(c5,c6)
are11 then00; c5's remaining values are10. At time8 let
r=c6(8),s=c7(8). Then c5(10)=r OR s; if this is zero,
c6(9)=1 and c6(10)=1. Thus this last case never returns pair00.
These three cases exhaust all actual tails.

**Independent controls and scope countercheck.** P1 was registered
before the first controls; P3 was explicitly informed by their three
profiles and registered before its checks. All 1,024 complete cones
through site16 pass literal and independent packed updates, including
the early ancestry shield, exact selector and pair transport;112 have
mid/return00. No bounded scan is being used as the universal proof.
GC619's prefixes1110010001000 and1110010001001, each with both farther
cone extremes, share fifth profile0101100101 and return first eight
bits11100000; their ninth bits are respectively1 and0. Thus the
profile alone does NOT force the full L1 entrance. The extra ninth
bit is real correlated information, not disposable boundary slack.
In an already synchronized next L, its closing-marker demand selects
the valid L1 branch by GC623; without that future demand it may fail.

This closes the fifth-track selector and pair-transport inference,
not full exterior composition, halfwidth or an all-depth record bound.
Next missing inference: whether the transported complement pair has
an equally sound successor relation through the L1-S switch, retaining
the ninth-bit ancestry instead of declaring fresh branch choices.


## GC1048 — The alternative long loop carries a ninth-column gate through its short successor (2026-10-10)

**Missing inference and prediction.** CL214 confirms GC1046/1047 and asks for the successor relation through L1-S, retaining the ninth entrance bit. The concrete target is a correlated carrier deciding the following collar type, not another visible-word census. Record searched: L1|alternative.long|111000001 with fifth|sixth|successor|correlat|profile finds the established return proofs but no successor-pair theorem; the three new profile/prefix strings find no relevant result. GC622 and corrected GC609 are reused; GC689 assumes all-S and does not supply this switch relation. Before controls, the retained probe predicts the exact fifth/sixth tracks below, the ninth-track gate, and both following types. The counterfactual deletes the ninth entrance premise. Its unexpected paired-cone check keeps every other input identical.

Let time0 be a white-wall row beginning111000001 (L1), and put h=c9(5), j=c9(8). For EVERY farther tail,

    c5(0..9)=0010010010, c6(0..9)=0000110110,
    (c6,c7)(10)=(1-h,1), h=1 implies c8(10)=1,
    c5(16)=h OR NOT j.

Thus after the forced L1-S pair the next entrance is L0 exactly when h=0 and j=1; otherwise it is S. These are samples of one actual ninth-column track, three physical ticks apart. They are not independently selectable Boolean labels. Both outcomes occur on complete cones. This strengthens L1->S: its S entrance always has site7 black and, when site6 is white, site8 black.

**Hand transport.** GC622 gives time4 prefix0010011BC with B OR C=1, hence time5 prefix01111100. Write its next four bits h,k,r,s. Time6 starts0100001; its sites8..11 are h, h OR k, h XOR(k OR r), k XOR(r OR s). Time7 starts1110011; its sites8 and9 are respectively

    A=NOT(h OR k), B'=h XOR(h OR k OR r).

For h=1 both are0; for h=0 their OR is1. Hence c8(8)=1 XOR(A OR B')=h. Also c7(8)=0, shielded by the adjacent black pair at time7. Consequently time8 begins0001110h. The displayed fifth/sixth tracks follow directly from these prefixes and GC622's earlier rows; no farther-tail values are fixed.

Now write time8 sites9,10,11 as j,k',l. Time9 sites5..10 are

    0,0,1-h,h OR j,h XOR(j OR k'),j XOR(k' OR l).

Time10 begins11101. Its sixth and seventh sites are1-h and1. If h=1 its eighth site is1. If h=0 its eighth/ninth sites d,e are

    d=NOT(j OR k'), e=j XOR(j OR k' OR l).

Their OR is NOT j: split j=0 (NOT k' OR k' OR l=1) and j=1 (both0). This is the correlated pair transported into S.

For any S row11101a1de, one tick gives sites6..8 equal0,1-a,NOT(d OR e); two ticks give sites6,7 equal a,(1-a) OR NOT(d OR e). Corrected GC609 says that S's returned fifth bit is their XOR. It is1 when a=0 and d OR e when a=1. Substituting a=1-h and the transported pair gives h OR NOT j. The same reviewed S-return theorem forces its sixth bit1 when its fifth bit0, so that branch is specifically L0. This completes the all-tail hand implication.

**Controls and scope.** Literal shrinking cones and an independent packed update agree on all8,192 completions through site22, retaining six sites after16 ticks. Both following types occur; every asserted track, pair and gate passes. The paired unexpected check uses111000000 versus111000001 with thirteen identical zero farther bits: their time10 prefixes are10011000 and11101011. Deleting the ninth entrance bit loses the marker, as the earlier terminal-exit warning predicts; it cannot be erased in this transport. No SAT or Local language/membership work was duplicated.

This supplies CL214's finite successor coefficient, extending the L1 slab from four to six columns and carrying an actual farther-column relation through S. It does not bound the number of distinct relations under unlimited composition, make h,j free inputs, or prove a record bound. Next useful obligation: whether the ninth-track gate can be transported across successive mixed returns by a closed relation class. No further finite cone census is proposed. Cloud hand review requested.

**Receipt, CL214 at55e7e400.** Cloud independently confirms GC1046's collar/interface and GC1047's selector/pair transport, with its own complete cones; the shield derivation also checks line by line. GC1046's type completeness/transition graph reuse earlier reviewed entries rather than receiving a new exhaustive derivation in CL214. The ninth-bit limitation is confirmed. These readings promote those results, within their existing scopes; GC1048 remains a proof sketch pending its own reading.


## GC1049 — A short successor retains an entrance-sensitive Horn clause; no-refork closure is unresolved (2026-10-10)

**Missing inference.** Can GC1048's L1-S-L0 branch forbid an immediate next L1, closing a small typed relation class? Record searched: LLSLL|L1SL0L1|alternative.*short.*long with forbid|absen|return|gate gives4 unrelated prior hits;111011100110|000111001 with ancestor|prehistory|image|successor gives0. Each prediction below was written before its check; later ones are explicitly informed by the earlier outcomes. No Local solver or visible-language membership run was duplicated.

**Hand result.** The branch h=0,j=1 of GC1048 has time8 prefix000111001 and time10 prefix111011100. Its time10 sites10..12 obey

    c10 AND c11 implies c12.

Indeed time9 site9 is1, since time8 sites8,9 are0,1. If time10 site10 is1, its update from that black left neighbour forces time9 sites10,11 both0. Time10 site11 then equals time9 site12. If it too is1, time9 site12 is black; updating site12 with white site11 forces time10 site12=1 regardless of site13. This three-literal implication uses the actual two-tick ancestry, not merely the returned S prefix. It is a Horn clause on that successor row.

All32 complete two-tick cones agree with independent literal/packed updates and verify the clause. Thus the relaxed S cone1110111001101000000000000, which completes S-L0 into another L1 after16 ticks, cannot be the full successor row on this actual L1-S-L0 branch: it violates the clause. This is a concrete spurious typed transition removed by retaining prehistory. It does not exclude every refork.

**Failures retained.** P1 predicted no next mid00 from the S cylinder111011100;228 of512 complete cones refute it. Informed P2 predicted no full refork in that S cylinder; the displayed complete cone refutes it. P3 then predicted an actual L1-S-L0-L1 among1024 deterministic random full cones: the sample expectation is REFUTED, while actual existence remains UNKNOWN, with no absence claim. The sample is nonvacuous:147 L1-S-L0 cases,94 with the next mid00. P4 predicted that a seven-bit return1110000 from the S cylinder requires initialsites10..12=110;11101110011100000000000 refutes it. Informed P5 repaired that hypothesis to the full nine-bit L1 gate;1110111001110000000000000 refutes it too. All retained counterexamples replay independently. The latter111-tail is the unexpected check: it passes the new clause while reforking in the relaxed S cylinder, so the clause alone does not discharge the closure target. No larger scan is proposed.

**Disposition.** This narrows the missing invariant to correlations in the L1 prehistory beyond the nine-bit S entrance. The simple mid-pair and three-bit origin-shield shortcuts are stopped; the actual no-refork claim is neither proved nor refuted. Next seek a backward-closed family of entrance-dependent clauses under the typed return maps, without treating a necessary clause as a sufficient lift or adding another window census. Cloud review requested for the hand clause and the distinction between the actual and relaxed reforks. All-depth record boundedness remains open.


## GC1050 — The complete ordinary-to-alternative long switch has four thirteen-bit cylinders (2026-10-10)

**Missing inference.** Typed composition needs the complete L0->L1 entrance, not just GC619's one sufficient cylinder. The new hand observation is that GC1047's complemented mid-pair also transports its first bit to returned site7. Record searched:1110010001 with complete|necessary|MUX|selector|gate|thirteen gives9 hits, the earlier GC614/618/619 and GC1047 facts, not a complete switch classification. This block switches from GC1049's stopped closure scans to an all-tail Boolean derivation. Predictions before controls: the return first8 is11100000 iff the input begins1110010001; its ninth bit then has the mux formula below.

For every white-wall row beginning111001, the next row after its ten-tick L0 is in L1 exactly when the initial row begins one of

    1110010001000, 1110010001010,
    1110010001011, 1110010001100.

Every farther tail is allowed in each cylinder. Equivalently, the initial first10 bits must be1110010001 and, for f,g,h at initialsites11,12,13,

    L1 gate = (NOT f AND g) OR (NOT g AND NOT h).

This is a multiplexer: g=1 selects NOT f, g=0 selects NOT h. GC619's old cylinder is just f=g=0; its NOT-thirteenth-bit gate cannot be applied after forgetting those two whites.

**Necessity of the ten-bit prefix.** If the return starts1110000, its sites5,6 are00. GC1047 therefore gives mid00 and time5 sites8,9 equal P,1-P. Its time9 sites6,7 are1-P,1, so returned site7 equals P. Thus P=0. In GC1047's proof the time2 pair(p,q) atsites9,10 is10 when P=0, and01 when P=1. The same proof forces time2 sites7,8 both0; its initialsites7,8 are both0. Writing initialsites9,10 as d,e, its intermediate Y=d, Z=d OR e=1 and p=NOT d show that p=1 forces d=0,e=1. This is exactly1110010001. Conversely that prefix gives time2 sites7..10=0010, then the mid-pair with P=0. GC1047's transport gives the first7 return bits1110000. At time8 its sites6..8 are010. Writing its sites9,10 as w,z, the time9 sites7..9 are1,NOT w,w OR z; returned site8 is0 because (NOT w) OR(w OR z)=1. Hence the first8 return bits are11100000 iff that ten-bit prefix holds.

**The ninth-bit mux.** The ten-bit prefix gives time4 prefix0011111100. GC618/619's shielded calculation, which uses that prefix and arbitrary farther bits, says returned site9 is NOT E, where E=c11(4). To expose its original coefficients, write time2 sites11..13 as r,s,t. Its prefix0111000010 gives time3 sites10..12 equal NOT r,r OR s,r XOR(s OR t). Consequently

    E = r OR NOT(s OR t),
    return site9 = NOT r AND(s OR t).

Let J=NOT(f OR g), K=f XOR(g OR h), V=g XOR(h OR i), W=h XOR(i OR j), with i,j arbitrary farther initial bits. Direct two-tick updates give r=NOT(J OR K), s=J XOR(K OR V), t=K XOR(V OR W). For r=0 there are two cases. J=0,K=1 forces s=1, so the gate is1. J=1 means f=g=0, giving K=h,V=h OR i; here s OR t=NOT h, as in GC619's reviewed cancellation. J=K=0 has r=1 and gate0. The J=0,K=1 case is precisely g=1,f=0 or g=0,f=1,h=0. Together these cases yield the displayed mux and exhaust all initial bits, proving the four cylinders.

**Controls and scope.** All512 complete fixed-ten-prefix cones for the ninth return bit agree with independent literal/packed updates. Another256 varied-prefix farther-tail extremes check the necessary prefix; these are controls, not the proof of all-tail necessity. Both predictions hold. The unexpected positive1110010001100 lies outside GC619's old cylinder and succeeds;1110010001110 has a white thirteenth bit but fails, refuting extension of the old single-bit formula without its coefficient prefix. No solver, visible-language membership job or strip-width scan.

This completes the finite hidden-fork gate, shrinking the next actual-prehistory target to the union of four explicit cylinders. Intersecting their preimages with L1-S ancestry is now the concrete closure obligation; GC1049's no-refork remains unresolved. Unlimited relation closure and the all-depth record bound remain open. Cloud hand review requested.

**L609 receipt at7be937a9.** Accepted and ACKed: both-phase kissat UNSAT at d140,L18 over verified cuts gives R_real(140)<=17; formal certificate replay is still pending. The d131 witness is reported VALID. The dip between the witnessed18s at136 and152 is retained with that provenance; no duplicate audit or run.


## GC1051 — Actual alternative-long ancestry forbids the immediate hidden refork (2026-10-10)

**Missing inference.** Does GC1050's four-cylinder L0-to-L1 gate meet the actual sixteen-tick L1-S image? Record searched:L1.S.L0|1110010001 with ancestr|preimage|no.refork|successor ->5 hits, GC619/1047/1049 and its probe, no exclusion. The new hand step is to transport GC1047's EXISTING four-cell ancestry shield to time3; no wider closure census or Local solver job.

**Hand result, review pending.** For EVERY initial farther tail after white-wall prefix111000001, time16 cannot begin1110010001. Consequently the typed return sequence L1-S-L0-L1 is impossible: GC1050 makes that ten-bit prefix necessary for its last switch. This concerns the hidden collar types, not an unconditional absence of the visible word LSLL. Unlimited relation closure and the all-depth record bound remain open.

Write h=c9(5). If the short successor at10 feeds L0 at16, GC1048 gives h=0 and j=c9(8)=1, and its S entrance begins111011100. We need three local facts.

**1. The short-return gate.** For a white-wall S row111011100 with sites10..13=a,b,c,d, its six-tick return begins1110010001 iff

    a=b=1 and c OR d=1.

At time2 its prefix is01011111, followed by

    U=NOT(a OR b), V=(1-a)(b OR c),
    W=(a OR b) XOR[(a XOR(b OR c)) OR(b XOR(c OR d))].

At time3 write p=NOT(U OR V), q=U XOR(V OR W), r=V XOR(W OR right). Time4 sites8..11 are p,p OR q,A=p XOR(q OR r),B=q XOR(r OR right). Returned site7 is NOT(p OR q); site8 is0 for p=1 and q OR r for p=0. Their two zeros force p=1, and returned site9 is then A OR B. Its zero forces A=B=0 and q=1 (A=0 gives q OR r=1; B=0 gives q=r OR right). Conversely p=q=1 gives U=V=0,W=1,r=1, hence A=B=0 and returned sites7..10=0001. Finally U=V=0,W=1 is equivalent to a=b=1,c OR d=1 by splitting a and b. Thus an actual refork would require sites10,11 of the S entrance both black.

**2. L1 forces a white tenth site at time5 when h=0.** Initial L1 gives time2 prefix011110110; the ninth zero is essential. Put b=c10(2), c=c11(2). Time3 sites8..10 are0,NOT b,b OR c. Time4 sites8,9 are b,1. Hence h=NOT b. If h=0 then b=1, time3 begins1100001001, time4 site10 is1, and k=c10(5)=0. At time5 write sites11..16=r,s,u,v,w,x. GC1047's shield, translated from its initial anchor at sites5,6 to time3 sites9,10=01, gives

    r=s=0 implies (u,v) != (1,1).

This is the same two-tick ancestry lemma with a spatial shift, retaining an actual past; no independent assignment of the child bits is permitted.

**3. The required S pair contradicts that shield.** Under h=k=0 the time5 row begins0111110000. Direct updates give j=NOT(r OR s), so j=1 forces r=s=0. At time8 site10 is then u. Since time9 site9=1, a black time10 site10 forces time9 sites10,11 both0. Their two equations force time8 site10=1, hence u=1. The time8 sites9..12 now equal1110. Let o be its site13. Time10 site11 equals NOT o, so its required black value forces o=0. The last local update yields

    o = NOT G,
    G = 1 XOR[(NOT(v OR w)) OR(v XOR(w OR x))].

Thus o=0 requires v OR w=1 and v=w OR x. These imply v=1 (v=0 would force w=x=0), and w OR x=1. In particular the required S pair forces r=s=0,u=v=1, contrary to fact2. This proves the exclusion without a tail cutoff.

**Correction and retained failures.** While deriving this gate I found a shifted intermediate coefficient in GC1048: its time6 site10 is h XOR(k OR r), not k XOR(r OR s), which belongs at site11; time7's B' loses the extra s. Those intermediate lines are corrected above. Their shield conclusion and every stated GC1048 theorem remain valid: the corrected B' is0 for h=1, and k OR r for h=0, preserving A OR B'=1 in the latter case. The existing8,192-cone controls now explicitly check these intermediate equations too. Two proposed positive constructions and a proposed time5 prefix equivalence failed before the corrected proof and are retained in the new probe. They are not actual reforks.

**Independent and unexpected controls.** Literal and packed engines, with both starting wall phases explicit, pass128 complete local S gates,64 black-phase successor gates (3 positives),64 translated shields (12 applicable), and64 L1 antecedents. The retained relaxed row1110111001110000000000000 really reforks and passes GC1049's Horn clause; its loss of the translated two-tick past is exactly why the new exclusion does not apply. Controls check the local hand implications; none is presented as a finite census proving universal absence. Next seek the same transported shield across an intervening L0 or S, to determine whether hidden forks have a recursive separation law. Cloud hand review requested; no computation or time-critical work.

**Recovery receipt, CL215 at1facb241.** Accepted: Cloud independently exhausts the full cones for GC1048/1049 (8,192 tails) and GC1050 (16,384 tails), confirming the successor, Horn clause and exact four-cylinder gate in both directions. These conclusions now have a second reader; the intermediate indexing correction above does not change them. GC1051 itself still awaits its reading. No further run requested.


## GC1052 — One whole mature short-to-long branch cannot renew the hidden fork (2026-10-10)

**Missing inference.** GC1051 excludes immediate L1-S-L0-L1; locate which other mature S entrances could renew a fork before attempting a longer-return closure. Record searched:S.L0.L1|short.*fork|111010110|111011101 with gate|preimage|ancestr|successor ->6 hits, GC1049/1051 and references, no three-branch fork precursor. Reuse GC1014's maturity clauses and GC629's four-bit return gate: a mature S feeding L0 starts exactly one of111010001,111010011,111011100. This classification is established, not proved anew.

**New hand result, review pending.** The entire middle branch111010011 returns L0 with

    (c7(6),c8(6)) = (NOT w,w), w=initialsite10 OR initialsite11,

for EVERY farther tail. Therefore this branch cannot feed the next L1: GC1050 requires the L0 entrance to begin1110010001, with both sites7,8 white. This removes a whole mature hidden precursor independently of how it was entered.

The initial prefix gives time2 prefix01011000. Put w=c9(2), q=c10(2). Direct updates retain

    time3 sites6..9 = (1,0,w,w OR q);
    time4 sites5..8 = (0,1,1-w,w OR q);
    time5 sites6,7 = (1,0).

The last zero is shielded by (1-w) OR(w OR q)=1. Now write H=c8(5), I=c9(5). The return sites7,8 are exactly(1-H,H OR I), whose OR is1. Retaining one more ancestry relation sharpens this: w=initialsite10 OR initialsite11, and w=0 forces q=1. If w=1, the displayed updates give H=1; if w=0,q=1, time4 sites7..9 are111, giving H=I=0. Hence the pair is exactly(1-w,w). This initial-coordinate selector was predicted after the first controls suggested complementarity, then checked separately in the same complete cones. No free assignment of H,I or loss of their past is used.

Consequently a mature S-L0-L1 must start from111010001 or111011100. The latter has GC1051's exact first-ten-bit gate and is excluded specifically when preceded by L1-S. Whether the first prefix or an intervening return propagates a closed ancestry relation remains open; no bound on total fork counts follows yet.

**Failure retained.** In parallel with this hand step I predicted a complete fork gate for111010001. It fails on1110100010000100: its six-tick return starts1110010101, not1110010001. The proposed derivation made time4 site6 white; it is black. This gate classification is stopped for this block, with the concrete failure in the probe; no repaired variants or wider mixed-word scan.

**Controls.** All128 complete six-tick cones for111010011 pass literal and packed engines, including each displayed intermediate relation; both returned pairs01,10 occur; the new selector also passes. The unexpected startup111010010 really feeds L0 but violates GC1014's mature ab=00,c<=d condition, so it must remain outside the three-prefix classification. The earlier relaxed1110111001110... still reaches L1, preventing extension of this new obstruction to every S-to-L0 branch. Cloud hand review requested, no computation requested. Next useful obligation is transport of the surviving111010001 branch's correlated past; unlimited coefficient closure and the all-depth prize bound remain open.

**CL216 receipt at7f41518c.** Read §8.82 and the ledger: the swarm's black-phase coupling and three-shape lemma are accepted with Cloud's stated independent checks, its depth62 table remains third-party computation, and the lane's skeptic is still queued. It supplies no all-depth bound. No duplicate record computation or certificate audit. The present proof block remains on the hidden S/L ancestry target.

**CL217 receipt at4a41cdec.** Accepted: Cloud independently checks all131,072 L1 cones through site26;18,432 have the L0 branch and none has the barred ten-bit prefix at16. The five reported prefixes are1110010011,1110010100,1110010101,1110011011,1110011110. GC1051 is now second-read, within its typed-sequence scope; GC1052 remains pending. These concrete successor prefixes offer the next hand transport target across an intervening ordinary L, without a new width or mixed-word census.


## GC1053 — No ordinary-long return can prepare an immediate hidden fork (2026-10-10)

**Missing inference.** Transport CL217's five L1-S-L0 successor prefixes through an intervening ordinary L0. Record searched: their five strings with return|transport|interven|fork ->14 hits, GC1049..1052 and references, no intervening-L0 guard. A narrower L0.L0.L1|111001000|ordinary.*ordinary with preced|imposs|forbid|all.L|ALF|GC746|GC747 gives11 hits. Read GC744..747: their all-L future budgets do not give the single-return hand implication below. Reuse GC1047's exact mid-selector and two-tick ancestry shield, and GC1050's necessary fork prefix.

**All-tail hand theorem, second reader pending.** Every white-wall row initially beginning111001 which returns to L0 after ten ticks satisfies

    c7(10) OR c8(10) OR c9(10) = 1.

Thus the typed sequence L0-L0-L1 is impossible, since GC1050 requires the middle L0 to begin1110010001 to feed L1. This also excludes L1-S-L0-L0-L1, independently of CL217's five-prefix census. These are hidden collar constraints, not bans on the corresponding untyped visible words. No all-depth record bound is claimed.

**Proof.** Put z=c6(5), a=c7(5). GC1047 supplies the exhaustive cases. If z=a=0, the return has c6(10)=0 and cannot be L0. If z=0,a=1, time5 begins0110001. Write x,y,w for its sites8,9,10, and put A=NOT(x OR y), B=x XOR(y OR w). Its next two rows have sites6..9 equal(1,1,A,B) and(1,0,D,E), where D=NOT(A OR B) and E=A XOR(B OR right). At time8 sites6..8 are(1,NOT D,D OR E); their last pair has OR1. Hence time9 sites5..7 are(0,1,0). For Q=c8(9), R=c9(9), the returned sites7,8 are(NOT Q,Q OR R), with OR1. This establishes the stronger two-site blocker in the mid01 case.

It remains z=1. At time5 sites5,6 are01 and the prefix is011001. GC1047 gives c5(6)=1, c5(7)=0, c5(8)=1. Let time7 sites7..12 be u,v,p,q,r,s. At time8,

    (c6,c7) = (u,u OR v).

The GC1047 closing-L0 criterion requires these two sites both white, so u=v=0. Crucially the actual time5 anchor01 and its two Rule30 updates impose GC1047's translated shield

    u=v=0 implies (p,q) != (1,1).

For u=v=0 the same updates give time8 sites8..11 as

    p, p OR q, p XOR(q OR r), q XOR(r OR s).

At time9, c7=p and c8=p OR q. Therefore c7(10)=NOT(p OR q). If the returned sites7 and8 are both0, the first equation gives p OR q=1; the second then forces p=1. With p=1, time9 sites8,9 are10. If returned site9 is also0, time9 site10 must be1. Its equation is

    c10(9) = 1 XOR[(1 XOR(q OR r)) OR(q XOR(r OR s))].

A value1 forces q OR r=1 and q=r OR s. They imply q=1: q=0 would give r=s=0 and contradict the first equality. Thus three returned zeros force p=q=1, contrary to the translated shield. This proves the claimed OR guard for every farther tail.

**Initial bounded attempt and controls.** Before controls P1 predicted that CL217's five prefixes already barred the next fork precursor. All5*1,024 complete ten-tick local cones passed literal/packed engines. Their hand blockers were: the first three use mid00 or mid01;1110011011 returns S;1110011110, if it returns L0, has returned site9=1. Following those explicit equations, I predicted and derived the stronger P2 above, replacing reliance on the five-prefix list by the universal ancestry shield. Separate controls check256 complete five-tick black-phase mid1 cones (48 L0 returns),128 mid01 cones, and64 translated shield cones (12 applicable), including the displayed intermediate equations. They test the local proof steps rather than substitute a depth scan for proof.

**Unexpected check and retained failure.** The unlifted black-phase row11010000111 followed by zeros reaches1110010001 in three ticks. Its input sites7..10=0011 violate the shield; a free-row relaxation would really admit the barred target. My first unexpected-control prediction used1101000011 followed by zeros and failed, returning1110010011. The correction retains the additionally necessary time7sites11 OR12=1; p=q=1 alone was never a sufficiency claim in the proof. The existing relaxed S row1110111001110... also reaches the fork precursor, confirming that fork births from S are not excluded. Both independent engines agree.

**Consequence and next intention.** Together with GC1046/1051, an interior L1 birth has a preceding S-L0, and that S cannot be the immediate successor of L1. The surviving birth past must therefore pass through another S or L0 before that S; this is a concrete separation constraint, not a finite-state closure certificate or bound on the number of births. Next hand target is transport of this shield through the surviving S entrance, retaining its actual past. Cloud hand review and one concrete next obligation requested; no solver, membership or mixed-word scan.

**CL218 receipt at31364769.** Cloud independently checks8,192 S111010011 cones, with returned pair10 in2,048 and01 in6,144; accepts the hand relation and retained failure. GC1052 is now second-read. No run requested from Local.


## GC1054 — A mature hidden fork must have an ordinary-long/short past (2026-10-10)

**Missing inference.** GC1053 removes L0-L0-L1; determine which S ancestry can still prepare a fork. Record searched:S.S.L0.L1|S.S.L1|short.*short|111010001|111011100 with fork|ancestr|preimage|successor|gate ->40 hits. Read GC629/689 and GC1014. The new input is GC1053's adjacent-pair shield, which suggests an output obstruction for the first mature S branch rather than repairing GC1052's failed complete fork formula.

**Two all-tail hand lemmas, review pending.** (A) Every white-wall row111010001 returns L0 after six ticks with c8 OR c9=1. Therefore this whole mature S branch cannot feed L1. (B) Any S return which is again S and has black site6 has site7 black and c8 OR c9=1. Consequently a short-return image cannot begin111011100.

For (A), initial111010001 gives time2 prefix010110010. Write U=c10(2), V=c11(2). At time3 sites6..10 are(1,1,1,NOT U,U OR V). Thus time4 first9 is000101000: the zero at its site9 is shielded by (NOT U) OR(U OR V)=1. In particular its site6 is BLACK, retaining the correction which invalidated GC1052's old gate. Put C=c10(4), E=c11(4). Time5 sites6..10 are(1,1,0,C,C OR E), hence returned sites7..9 are

    (0, NOT C, C OR E).

Their last pair has OR1 for every actual C,E. GC1050's necessary fork prefix requires both sites white, proving the obstruction independently of any farther tail or earlier entry.

For (B), let time2 sites6,7,8 be x,y,z. A following S requires x XOR y=1 (GC609/629). If xy=01 then time3 sites6,7 are01, time4 sites6,7 are11, time5 sites6,7 are00, and returned site6 is0. Thus a black returned sixth site forces xy=10. Here time3 site7=NOT z. Its site8 is z OR right, so time4 site7=1. Time5 site6=0 and site7=z; returned site6=z. A black return therefore forces z=1. The successive triples at sites6..8 are now

    time3: (0,0,1); time4: (0,1,1); time5: (0,1,0).

For F=c9(5), G=c10(5), the return sites6..9 are exactly

    (1,1,NOT F,F OR G).

This proves the second OR blocker. Prefix111011100 would instead have sites6..9=1100, contradicting it. Unlike GC689, this is a finite-return necessity without assuming an infinite all-S future.

**Concrete fork-origin consequence.** GC1014's mature S-to-L0 entrances are111010001,111010011,111011100. Lemma(A) and GC1052 exclude the first two from feeding L1. Therefore every mature S-L0-L1 birth uses the last prefix, with its exact GC1051 gate: S-entry sites10,11 both1 and sites12 OR13=1. First, GC1053 requires the L0 immediately before a fork to have an S predecessor: an L0 predecessor is barred, and an L1 predecessor would itself return S. At that S entrance, lemma(B) excludes a preceding S, while GC1051 excludes a preceding L1 when the required fork gate is imposed. The remaining predecessor is L0. Thus every fully internal hidden fork has the past

    L0-S-L0-L1,

and its S entrance begins111011100. An L1 is followed by S, so such a fork sits in an untyped visible LSLLS block. This is a necessary placement of the hidden type; it does not forbid LSLLS, force a fork there, or bound total fork counts. Initial S entries lacking a two-tick past and terminal unsynchronized L entries remain exempt. The all-depth record bound and a closed hidden representation remain open.

**Predictions and independent controls.** P1 initially proposed a predecessor characterization for111011100 after S; lemma(B) makes it vacuous, so it is not reported as a nonempty branch classification. P2/P3 predicted both OR blockers before controls. All1,024 complete six-tick S cones (96 applicable black-sixth S returns) and128 first-branch cones pass literal/packed engines, including every displayed intermediate tuple. The retained failed GC1052 cone1110100010000100 still returns1110010101, consistent with(A), while the relaxed1110111001110... still reaches the fork prefix and L1: short sources must not be banned independently of their past. Startup111010010 still feeds L0 and violates the mature-prefix condition. No mixed-word, membership, solver or width scan.

**CL219 receipt at95e0f521 and next intention.** Cloud independently checks16,384 L0 cones,9,376 L0 returns, confirms GC1053's OR guard and its hand implications. GC1053 is now second-read. Its additional reported absence of returned triple110 is received computation, not a new theorem here. Next substantive obligation: intersect the remaining111011100 fork gate with the actual L0-S past, retaining correlations, and determine whether a fork birth is realized or further shielded. Cloud hand review and question design requested and flagged; no computation requested from Local.


## GC1055 — The hidden alternative-long fork is confined to startup of an S/L run (2026-10-10)

**Missing inference.** Intersect GC1054's last possible mature origin L0-S-L0-L1 with actual L0-S past. Record searched:L0.S.L0.L1|111011100|long.*short.*fork with L0|ordinary|ancestr|preimage ->25 hits, GC1051..1054 and references, no origin exclusion. Further fork/alternative-long with at-most-one/first-three/transient finds26 unrelated hits, no startup-only result. Reuse GC1047's ordinary-L mid-selector, the reviewed fork gates, and the three mature S-to-L0 branches; no larger word or solver scan.

**New all-tail lemma, independently confirmed CL221.** Every L0 return which is S with black site6 has returned sites6..9

    (1,1,NOT H,H OR I), H=c9(9), I=c10(9).

Therefore NO L0-S return can start111011100. The entire remaining origin is barred even before imposing its extra fork gate.

**Hand proof.** GC1047's mid00 and mid01 cases return with white site5, so an S return requires mid1: time5 begins011001. Let time7 sites7..10 be u,v,p,q. From c5(6)=1,c5(7)=0,c5(8)=1, direct updates give time8 sites6..9 as

    u, A=u OR v, B=u XOR(v OR p), C=v XOR(p OR q),

and time9 sites6..8 as

    NOT A, F=u XOR(A OR B), G=A XOR(B OR C).

Returned site5 is A; returned site6 is (NOT A) OR F. A black fifth/sixth pair forces A=1,F=1. Then F=NOT u, so u=0 and v=1. These give B=1, G=0, and time9 sites6..8=010. The final update yields the claimed returned tuple, with its last pair having OR1. No earlier ancestry shield or independence of H,I is needed for this implication. A free S111011100 row is still permitted; it cannot be this L0 image.

**Uniform startup bound for the hidden type.** Consider any run of synchronized return cylinders S,L0,L1, numbered0,1,..., with the wall white at the markers. Suppose L1 occurred at index k>=3. GC1050 and the collar table force its predecessor to be L0. GC1053 forces the predecessor of that L0 to be S (L1 would return S, and L0-L0-L1 is barred). That S entrance has an actual two-tick past because k-2>=1. By GC1014, GC1052 and GC1054, only S111011100 can prepare the required fork. A preceding S cannot create that prefix by GC1054. A preceding L1 cannot supply its fork gate by GC1051. A preceding L0 cannot create it by the new lemma. These exhaust the typed run and give a contradiction.

Thus L1 can occur only at indices0,1,2. It can occur AT MOST ONCE there: an L1 returns S, and S cannot return L1, so two L1 entrances need separation at least three indices. After the third return every remaining long entrance in that run is L0. In particular the four-column collar then has no hidden L0/L1 ambiguity and is determined by the visible S or L symbol. This is a uniform finite startup statement, not a depth scan or a counting assumption.

The scope is EACH uninterrupted synchronized S/L run. Other visible gap types can start a new run; an untyped terminal L remains outside the cylinder hypotheses. The surviving S/L0 component can still branch, its farther exterior correlations remain open, and no all-depth white-record bound or prize claim follows. The recurrent-L1 explanation route is closed in this precise scope.

**Controls and initial proposal.** P1 sought a two-tick shield violation from the full fork gate; the stronger source-prefix exclusion makes that extraction vacuous, so it is not claimed as a new shield theorem. P2 predicted the displayed OR guard before controls. All256 complete five-tick mid1 cones pass literal/packed engines, including every intermediate tuple;112 have the applicable black-sixth S return. The startup bound is proved by the typed predecessor cases above, not by enumeration of longer words.

**Unexpected origin check.** Initial L1 row111000001110011100 followed by zeros really returns1110111000101 at time10. Thus the L0-image lemma cannot be extended to every long source. Its sites10,11 are01 and fail the fork gate, agreeing with GC1051. The free S1110111001110... still reaches L1. These independent controls preserve the distinction between excluding a source prefix and excluding a gate on a source that does occur.

**Receipts and next intention.** CL220 at ac858135 independently confirms both GC1054 lemmas (2,048 first-branch and32,768 S cones) and the origin placement; GC1054 is now second-read. Local4235d5c5 reports d144 phase0 UNSAT at18 with16 cuts; this is accepted as reported solver evidence, not independently certificate-replayed, and phase1 remains pending. Next proof target is the recurrent S/L0 fifth-track selector with the canonical four-column collar, retaining farther correlations. No more hidden-L1 recurrence or mixed-word scans. Cloud hand review and concrete next-obligation design requested and flagged.


## GC1056 — Short-marker zero is absorbing, and the mature fifth collar has one LL choice (2026-10-10)

**Missing inference.** After the hidden L1 startup closes, find an actual correlated carrier in the recurrent S/L0 component. Record searched: short/SS/all-S/S-block with sixth/site6/c6 and monotone/birth/absorbing ->6 hits; GC689 and ASF read. The 111000/111010 fifth-track search finds15 hits, including the known all-S track, but no finite SS marker monotonicity or mature mixed table. GC744..747 and ALF's existing all-L forcing are reused, not rederived. P1/P2 and counterfactuals precede controls in rule30_short_marker_decay.py.

**New finite-return guard, independently confirmed CL223.** Across ANY SS return, the sixth-site marker satisfies u_next<=u. A black next marker moreover requires initial sites6,7=11 and sites8 OR9=1. Therefore once this marker becomes white within an uninterrupted S block it stays white until the block ends; a long return can reset it.

Write a,b,c,d for initial sites6..9 and x,y,z for time2 sites6..8. GC629 gives x=NOT(A OR B), y=A XOR(B OR C), where A=NOT(a OR b), B=a XOR(b OR c), C=b XOR(c OR d). SS means x XOR y=1. Direct updates give returned site6=x AND z: in branch xy=01, time3 sites6,7=01, time4=11, time5=00, so the return is white. In branch xy=10, time3 sites6,7=(0,NOT z); if z=0 the same shield gives a white return. If z=1, time4 sites6,7=(0,R), and time5 sites6,7=(NOT R,R OR Q), so their OR is1. This establishes the formula without treating R,Q as independent.

Black returned6 thus requires x=1. Then A=B=0. If a=0, B=0 forces b=c=0, contradicting A=0; hence a=1. If b=0, B=0 forces c=1, so C=1 and y=1, contradicting SS. Thus b=1; y=C=0 now requires c OR d=1. In particular black cannot be born from a white sixth marker across SS. GC689's infinite all-S gate did not assert this initial-marker implication.

**Short fifth track and its origin.** Every S loop has fifth pre-closing profile1110(x OR y)0. The first four samples are1110. At time3 site6 is NOT(x OR y), giving fifth sample4=x OR y. If that is black, sample5 is white by shielding; if white, time3 sixth is black and time4 sixth is black, again forcing fifth sample5 white. SS therefore has111010. For SL, x=y and the two possible profiles are111000 and111010.

The second SL profile cannot occur when this S has a preceding S or L0. GC1054/1055 show that a black-sixth S image from either type has sites6..9=(1,1,NOT F,F OR G), whose last pair has OR1. GC629 then forces the following return to be S. Hence an SL source with such a predecessor has a=0; the gate requires b=0,c OR d=1, which gives x=y=0 and profile111000. This uses the actual image guard, not independent mature-prefix choices.

Together with GC1047, from index4 onward in any typed S/L run the fifth pre-closing tracks are:

| Current/next type | Fifth track |
| --- | --- |
| SS | 111010 |
| SL0 | 111000 |
| L0S | 0101101010 |
| L0L0 | 0101100000 or0101101010 |

GC1055 ensures the previous type at these indices is S or L0. An L0S return requires GC1047's mid1 branch; an L0L0 return allows mid01 or mid1. Thus only the LL edge retains the fifth-track selector in this mature collar. This is a necessary correlated representation, not a claim that arbitrary LL selector choices are realizable or that the farther exterior closes. The all-depth realized-record bound remains open.

**Independent and unexpected controls.** All128 complete S cones for returned site6 pass literal and packed updates, including the displayed intermediate identities:80 return S,12 with black sixth. The initial output label1,024 was a reporting error, corrected to an actual counter before publication; no larger run was performed. Source111011101 with both farther extremes returns a black sixth again: monotonicity allows1-to-1 persistence. Source111010000 keeps a white sixth. Actual L1 source111000001110011100 followed by zeros returns1110111000101, then SL0 with fifth111010. This refutes extending the mature SL profile to an S preceded by L1 and preserves the startup qualification. No longer-word, solver, membership or record census.

**Receipt and next intention.** CL221 at b8d011ab independently confirms GC1055 on65,536 L0 cones (8,576 qualifying returns), its L1 counterexample and its startup derivation; GC1055 is now second-read. Next hand target is the surviving LL fifth selector's correlated origin or transport, beyond the already known all-L forcing budgets. Cloud review and that specific obligation design requested and flagged; no computation requested from Local.


## GC1057 — Trace halfwidth repair can require changing the initial strip row (2026-10-10)

**Missing inference, CL222.** Determine whether GC1044's correlated exterior extension can prove the trace-width claim while retaining the initial strip row. A concrete counterexample would close that stronger repair premise; an explicit trace-preserving rewrite would identify what a useful invariant must allow. Record searched: halfwidth/trace-form/repair with fixed initial/prefix/preservation ->30 hits, GC1042/1044/1045 read; no frozen-initial-row halfwidth counterexample. A five-sample trace/origin search gives44 hits, no matching fibre guard; merger/first-update/right-boundary gives3 unrelated hits. No Local solver, membership, cut or width census duplicated.

**All-tail hand obstruction and exact origin, independently confirmed CL225.** At a white wall start, every actual initial row010... has first-column trace01001 through time4. A free width3 strip with initial010 and first exterior samples10 instead has trace01000. Thus even at the proposed halfwidth horizon l=5<=2W-1, appending arbitrary actual right cells while retaining all W initial cells cannot repair this strip. This refutes the frozen-initial-row premise, not trace-language exactness: actual initial0111... does realize01000.

More precisely the actual trace01000 occurs IF AND ONLY IF the initial row begins011 and initial sites4 OR5=1. The first two trace bits force initial sites1,2=01. Write the next three initial cells c,D,E. Time1 sites1..4 are (1,1,NOT(c OR D),c XOR(D OR E)), time2 sites1,2 are00, and time2 site3 is

    NOT[NOT(c OR D) OR(c XOR(D OR E))] = c AND(D OR E).

For c=0 its OR bracket is NOT D OR D OR E=1; for c=1 it is NOT(D OR E), proving the equality. Time3 first-column bit is0, its second-column bit is c AND(D OR E), and time4 first-column bit is NOT[c AND(D OR E)]. This proves the fibre guard for every farther tail, including necessity. In a free width3 strip, the corresponding bit is NOT[(c OR D) AND NOT G], with G its unconstrained next exterior sample. Choosing c=0,D=1,G=0 creates the bad frozen origin; an actual update would give G=c XOR(D OR E)=1, forbidding it.

**Concrete repair primitive, not an all-length extension theorem.** Change only initial site3 from0 to1 and keep first exterior sample1. The two width3 rows010 and011 both update to110, so all interior information about this change is erased after one tick. The exterior's next value0 now becomes legitimate because its new left neighbour is black. Any actual row0111... has the required trace, so this initial-boundary rewrite discharges this particular obstruction.

The merger identity holds at every strip width W>=2, in either wall phase: changing only initial site W leaves the whole updated interior row unchanged when initial site W-1 and exterior site W+1 are black. The black penultimate cell shields its update; the last cell's OR with the black exterior is1 in either branch; all other interior updates are unchanged. With a white exterior the last output distinguishes the two branches. This is an elementary local merger applied to repair, not a claim that every later obstruction admits this rewrite.

**Predictions, independent controls and retained limitation.** P1's frozen-row refutation passes four complete actual010 cones, the explicit strip, and an actual changed-site3 witness. Informed P3's exact fibre passes all32 five-input cones using literal and packed shrinking updates. The unexpected01101 source is positive despite white site4, so the origin guard must retain the OR, not just site4. P4 merger and white-exterior countercontrols pass both wall phases. A single preregistered W=4,l=7 diagnostic also finds all1,024 strip cases repairable while retaining the first W-1 initial cells, against128 actual cones; P2 HELD only there. This is finite evidence for that stronger invariant, not a uniform proof. No larger-width variant is scheduled.

**Disposition.** Frozen-W-initial-row repair is CLOSED as a proof strategy for CL222. Trace-preserving initial rewrites must be allowed; GC1044's fixed-column binary relation cannot alone append a repair to this bad origin. The next concrete hand case is a terminal repair obstruction with a white penultimate cell, where this one-tick merger is unavailable. Cloud review and obligation design requested and flagged. All-length trace exactness, recurrent hidden closure and the prize record bound remain open.


**GC1057 publication receipt.** CL223 at100ef46d independently confirms GC1056's finite SS marker guard on32,768 S cones and its short/long fifth tracks on the S cones and16,384 L0 cones. The mature-S exclusion was not separately censused there; it follows from the confirmed S/L0 image guards as written. GC1056 is second-read with that provenance; no new census run here.


## GC1058 — White-penultimate edge repair can require an unbounded initial rewrite (2026-10-10)

**Missing inference, CL222/GC1057.** Handle the white-penultimate case of trace-preserving initial repair, where GC1057's one-cell merger is unavailable. A uniform rewrite primitive or a necessary unbounded repair cost would constrain the proposed halfwidth proof. Record searched: coalesc/merg/preimage/inverse with delta/difference/boundary rewrite ->91 hits; white penultimate/10100/11001/fixed exterior ->42 hits; 11000/10110/0^n/rewrite ->17 hits. G13 and GC1040 read; their existing inverse recurrence is reused. Predictions and counterfactual precede controls in rule30_edge_rewrite_carrier.py. No solver, membership, relaxed-record or width census.

**Parametric merger, independently confirmed CL226.** For every n>=2 and b in {0,1}, append either block to any common initial prefix:

    X = 11 0^n b,       Y = 10 1^(n-1) 0 (NOT b).

Give both rows the same black first exterior sample. Their entire updated interiors agree, either wall phase. Their last initial bits differ, their penultimate bits are both white, and their first-column initial bits agree. If L is the cell just before the block (the wall sample when the common prefix is empty), the common child block is

    (NOT L) 0 1 0^(n-2) b 1.

The first cell is black in both parents, so its child is NOT L and shields the common prefix. The second child is0: in X its left and centre are black; in Y its left and right are black. The third child is1: X has left1 with centre/right0; Y has left0 and centre1. Every intervening child is0, from a triple000 in X or left/centre11 in Y. The penultimate child is b: X has left/centre00 and right b, while Y has left1, centre0 and right NOT b. The last child is1 because its left is0 and the exterior is black. These checks also cover n=2, whose intervening segment is empty. No independence of evolved exterior cells is assumed.

**One-step cost is forced, not just expensive for this construction.** The known left-permutive inverse gives parent(i-1)=child(i) XOR(parent(i) OR parent(i+1)). Fixing the child row, the exterior bit and the last parent bit therefore uniquely determines the entire parent and its wall sample. For the opposite last bit of X, the only same-image parent is Y. They differ in n+1 cells; the leftmost difference is n+1 sites inward from the outer edge. Thus no fixed-radius initial-suffix rewrite can always flip the last bit while preserving the entire one-step interior image with this exterior fixed. This closes only that stronger merger strategy, not every bounded-window lemma, finite-type representation or trace-exactness proof. A repair allowed to change later interior rows has not been ruled out.

**Actual two-tick guard and its limit.** If X and Y are given the SAME actual farther initial tail, beginning with black exterior1, they still have the same entire interior at times1 AND2. At time1, the exterior bits are NOT b and b, but the common last interior child is black, so its next OR masks that difference. All other time2 interior updates use equal interior neighbours. This is a real two-tick repair primitive, not merely a free-strip merger. It does not guarantee longer equality: with b=1 and common farther initial tail beginning101, the next farther cell has time1 value0. At time2 the two exterior bits are1 and0 while the common last interior bit is0, so the last interior bits differ at time3. The farther tail cannot be silently held equal as a time-dependent free boundary after its first update.

**Independent and unexpected controls.** Literal Wolfram-table and packed one-step updates agree on36 selected cases: n=2,3,7; b=0,1; both wall phases; common prefixes empty,00,101. Backward reconstruction gives exactly X and Y with the same wall, and the n+1 Hamming count holds. All108 selected actual common-tail controls agree on the interior at times1,2. The unexpected actual101 tail for n=2,b=1 diverges at the last interior site at time3. The n=1 and white-exterior countercontrols fail coalescence as predicted. The uniform claims are hand algebra, not extrapolation from these selected checks.

**Receipts and disposition.** Verified62a472fe/ce61845a: CL225 independently confirms GC1057's trace origin and local merger; GC1057 is second-read. CL224 and §8.84's barrier/front proposal are received with third-party and computer-assisted provenance; no replay or change of lane here. The next missing inference is how an initial rewrite accommodates its necessarily altered actual exterior after the two-tick shield expires, at the horizon2W-1. Cloud review and that concrete compatibility obligation requested and flagged; no Local computation. Halfwidth, hidden exterior closure and the prize record bound remain open.


## GC1059 — Every two-tick strip has an actual repair changing at most its last initial cell (2026-10-10)

**Missing inference, CL222.** Does the white-penultimate case actually require GC1058's unbounded one-step merger to normalize the next exterior input? A uniform two-tick realization would identify which apparent exterior disagreements need repair. Record searched: trace/halfwidth/repair with two-tick/two-step/preimage ->59 hits; strip/exterior/repair with two-tick/time2 and initial/prefix ->28 hits. The existing exterior relations, inverse scanner and GC1057/1058 are reused; no uniform initial-prefix normalization found. Predictions and negative control precede the64 local controls in rule30_two_tick_normalize.py.

**Uniform construction, independently confirmed CL227.** For ANY width W>=2, initial strip row x and first two free exterior samples E,G, there is an actual initial right row preserving initial sites1..W-1 and both entire strip rows at times1,2. Only initial site W may change; two actual cells appended at W+1,W+2 suffice, followed by any tail. Either alternating-wall phase works.

Write a=x(W-1), b=x(W), and v for the first strip child. If E=0, append actual cells E,F with F=b XOR G. Their actual next exterior is b XOR(E OR F)=G, so both rows agree without changing x. If E=1 and G=NOT b, append E,F=1,0; again the next exterior is G and no rewrite is needed.

The remaining case is E=1,G=b. Its first child has last bit v(W)=NOT a. When a=1, flip only initial b. GC1057's local merger preserves the whole first child, and the actual next exterior becomes NOT(NOT b)=b=G, so the second child also agrees. When a=0, make NO initial change and append1,0. The actual next exterior is NOT b rather than G, but the common first child has v(W)=1. That black centre masks either exterior value in its next OR. Every other second-row update uses equal interior neighbours. Thus the two full observed rows agree despite an exterior disagreement. All assertions depend only on these two appended cells; arbitrary farther tails are allowed.

**Why the GC1058 obstruction does not apply.** Its long rewrite is forced when one insists on flipping the outer parent bit and keeping the complete first child fixed. That flip is unnecessary for two-tick realization with white penultimate cell: the black child masks the inconsistent next exterior. Normalization therefore costs at most one initial change for ALL widths, even though the stronger opposite-bit merger can cost arbitrarily many. This distinction follows from an explicit construction, not a larger scan. The lemma preserves the first initial trace bit because W>=2.

**Independent and unexpected controls.** All64 width3 local cases pass literal/packed strip and actual shrinking-cone checks:8 use the single-bit rewrite,8 mask a genuinely unequal next exterior. Both farther-tail extremes pass; a selected long GC1058 white-penultimate example repairs without any initial change. Unexpected boundary failure: width1, black-start, initial0 and free exterior10 emits000, while every actual row retaining initial first0 emits001. Thus the width condition cannot be dropped. These controls support the hand construction, not an all-horizon census.

**Remaining inference.** This normalizes two ticks, not the entire horizon2W-1. An induction dropping two observations needs a lift of the repaired time2 row through its actual two-tick prehistory, retaining the original first two trace bits. The construction above does not supply that lift and cannot be iterated by treating each later strip row as a fresh unconstrained initial row. Next bounded target: the correlated two-tick preimage relation for that lift, allowing intermediate near-edge cells to change. Cloud hand review and concrete lift-obligation design requested and flagged; no Local computation. Halfwidth and the all-depth bound remain open.


**GC1059 publication receipt, CL226.** Verified4a7937fb. Cloud independently confirms GC1058's merger on360 selected cases and its actual two-tick guard on5,760, and accepts the inverse-cost corollary. Its closing phrase “no bounded local primitive exists there” must be restricted to an opposite-outer-bit rewrite preserving the whole one-step interior image with fixed exterior. It is not a prohibition on every trace repair: GC1059 supplies a bounded two-tick normalization precisely by declining the unnecessary flip in the white-penultimate branch. No computational duplication here; CL226 received with that qualification.


## GC1060 — Exact prefix-conditioned boundary relation for the two-tick lift (2026-10-10)

**Missing inference, GC1059/CL222.** Can the next bit of a repaired time2 row be lifted while retaining its preceding child prefix and the prescribed initial prefix? Determine the exact admissible boundary relation, rather than treating this bit as freely replaceable. Record searched: two-tick/two-step with lift/fixed-prefix/prehistory ->26 hits; with prefix/lift and toggle/surject/last-bit/penultimate/freedom ->6 hits. G236's existing two-step spatial map is reused; no new generic image transducer or subset census. Predictions, counterfactual and controls precede execution in rule30_two_tick_prefix_lift.py.

**Exact local lift criterion, confirmed CL228.** Fix ANY initial prefix through site j+1, j>=3, with u,a,b,c at sites j-2..j+1. Put P=u XOR(a OR b), the time1 bit at j-1. Let Q,R be time2 bits at j,j+1. All child bits through j-1 are already fixed by that initial prefix, in either wall phase. Varying the next two initial bits d,e, with any farther tail, gives EXACTLY:

| Initial suffix condition | Admissible Q,R |
| --- | --- |
| bc=01 | Q=NOT P, R=a |
| bc=10, a=0 | Q=NOT P, R=0 |
| bc=10, a=1 | Either Q, R=1 |
| bc=11 | Q=P XOR NOT a, either R |
| bc=00, a=1 | Q=NOT P, either R |
| bc=00, a=0 | (P,0), (P,1), (NOT P,1) |

Therefore, given feasible Q, BOTH values of the next child bit R lift with the entire initial prefix and child prefix through j retained IF AND ONLY IF bc=11 OR [bc=00 AND(a=1 OR Q=P)]. Mixed bc locks R to a. Initial000 with Q=NOT P instead locks R to1. The first two original trace bits are retained, since their initial dependency lies within the fixed prefix. This is a boundary-pair lift, not a claim that every subsequent child tail lifts.

**Derivation and explicit realizers.** From G236's two-step map, the relevant first-row bits are A=a XOR(b OR c), B=b XOR(c OR d), C=c XOR(d OR e); Q=P XOR(A OR B), R=A XOR(B OR C). For mixed bc, B OR C=1 and A=NOT a, giving R=a and the displayed Q branches. For bc=11, B=0, C=NOT(d OR e), so Q is fixed and both R values occur. For bc=00, Q=P XOR(a OR d), R=a XOR(d OR e). If a=1, Q is fixed and R is free. If a=0, d=Q XOR P; d=1 forces R=1, while d=0 leaves R=e free. This proves necessity.

Sufficiency is constructive. For bc=11 choose d=0,e=a XOR R. For bc=00,a=1 choose d=0,e=NOT R; for bc=00,a=0 choose d=Q XOR P and e=R when d=0, else e=0. For bc=10,a=1 choose d=1 XOR Q XOR P,e=0. The other two mixed branches use d=e=0. Every admitted pair thus has an explicit two-cell initial extension; arbitrary farther tails leave the specified child prefix unchanged.

**Controls and concrete obstruction.** All128 complete six-input local cones (both wall phases) agree under literal and packed evolution, giving exactly the table and freedom criterion; all56 admitted pair/phase witnesses pass the explicit construction. Initial prefix0001 at white start always gives time2 prefix1110, so replacing its fourth child bit by1 while retaining the initial0001 and first three child bits111 cannot lift. The same boundary blocker survives translation past common prefix1010. The unexpected0000 case admits both R values before fixing Q, but Q=1 forces R=1; an unconditional output-bit freedom test misses the constraint. No solver, word-membership, wider strip or NFA census.

**Receipt and next intention.** Verified22c5c852: CL227 confirms GC1059 on992 local cases across widths2..6 and accepts the CL226 scope correction; GC1059 is second-read. The proposed two-observation induction must carry this prefix-conditioned relation, not just a repaired time2 row with a free next bit. Next missing inference: choose a future trace representative satisfying the forced boundary value when the pair is mixed or the000 guard is active, or move the initial repair farther left while preserving the trace. Cloud review and that concrete representative-selection obligation requested and flagged; no new computation. Halfwidth and the prize bound remain open.


## GC1061 — A delayed packet enforces its prefix-conditioned lift bit (2026-10-10)

**Missing inference, GC1060/CL222.** Does future trace matching itself retain a forced boundary bit in a nonvacuous actual two-tick image? Compose the reviewed GC1030 packet transport with the exact lift guard. Record searched:1001000|0011111 with ancestr|preimage|past|two.tick|time.?2 ->22 hits; GC1004/1005 give the phase obstruction, GC1030 gives transport, no complete packet origin surfaced. Predictions, counterfactual and selected independent controls were written before execution in rule30_packet_origin_lift.py. No word-membership, solver or width scan.

**Complete packet origin, confirmed CL230.** Let x be an actual initial right row, y its first update and z its second, with the wall initially black. Then

    z1..7=1001000 iff x1..7=0011111 and x8 OR x9=1.
    Under that condition, z8=x8 XOR(x9 OR x10).

Write c,d,e for x8,x9,x10. Necessity follows from the two local updates. Since the second update has a white wall, z1..4=1001 forces y1=y2=1 and either y1..4=1110 or1101. The second option has rooted prefix110, impossible after a black-wall update by GC1005. Thus y1..4=1110. Successively z5=z6=z7=0 force y5..8=0000, so y1..8=11100000.

The black-wall update then gives x1=x2=0,x3=1, x4 OR x5=1, and

    x4=x5 OR x6, x5=x6 OR x7,
    x6=x7 OR x8, x7=x8 OR x9.

These equations force x4=x5=x6=x7=1: if x5=0 then x6=0 and x4=0; if x6=0 then x7=0 and x5=0; if x7=0 then x8=0 and x6=0. Each contradicts the already forced preceding black bit. Hence c OR d=1. Conversely, initial prefix0011111 with c OR d=1 gives y1..8=11100000 directly, establishing the required z prefix. Its next bit is z8=y7 XOR(y8 OR y9)=y9=c XOR(d OR e). This proves both directions, for every farther tail. At initially white wall phase this time2 packet is impossible: z would be a black-wall image containing rooted10010, barred by GC1004. Phase matters for actual ancestry despite GC1030's phase-independent future transport.

**Concrete representative selection.** GC1030 gives x1(15)=1-z8. Therefore every future representative starting with z1..7=1001000 and matching the original first-column trace at times2..15 must retain z8. In the fixed-initial-prefix branch c=0, the origin relation forces d=1 and z8=1; future trace matching through its thirteenth tick automatically imposes this GC1060 mixed-pair lift guard. The guard is nonvacuous: initial001111101 gives this packet and z8=1, regardless of farther tail. For c=1 either z8 lifts: choose d=e=0 for z8=1, or d=1,e=0 for z8=0. In particular a black trace endpoint at time15 forces initial site8 black in this packet cylinder. For width W>=9 the original horizon2W-2 includes time15, and its proposed width W-1 future representative can retain the first seven cells and observe all14 symbols. This discharges the *next-bit* obligation in this one cylinder; it does not lift the remainder of the child tail.

**Controls, limitations and receipt.** Eight c,d,e cones agree under independent literal and packed updates; twelve selected actual endpoint controls (the six feasible cases, two farther-tail extremes) agree with the composed formula. The short64-case black-image negative control passes. Unexpected check:0011111100 gives z8=1, whereas0011111110 gives z8=0; ancestry alone cannot force the packet's next bit. The white-phase impossibility and the two positive black-phase witnesses prevent a vacuous compatibility lemma. No exhaustive rerun of GC1030's established transport proof. Verified0fe7193b/14d52ffa: CL228 confirms GC1060's full table and freedom criterion, now second-read. CL229 received; nonsoficity, even if proved, would not exclude a finite visible-language relaxation certificate. Next missing inference: an analogous trace-preserving choice for other forced-bit cylinders, especially those where the bit is masked rather than observed. General representative selection, whole-tail lifting, halfwidth and the all-depth prize bound remain open.


## GC1062 — Forced-zero repair carries a compatible first future input (2026-10-10)

**Missing inference, GC1060/1061.** Correct a wrong future boundary bit without losing its two-tick origin or silently treating the first future exterior as free. Record searched:0001|1010 with forced.zero|three.bit.*lift|prefix.condition|next.bit.*lift|first.*exterior.*repair ->6 hits; GC1060's pair relation and GC1057's merger are reused. GC605/606's return gates were read before the rooted example below. Predictions and controls precede execution in rule30_forced_zero_bridge.py. No solver, language-membership or width census.

**Uniform coupled repair, confirmed CL231.** Fix any initial prefix K through j+1, j>=3. Exactly two GC1060 suffixes force the next child bit R=0 while its predecessor Q=1: initial sites j-2..j+1 are0001 or1010. Let m=j+1. A candidate future controlled width-m row retaining the actual time2 prefix through j may nevertheless end in the wrong bit R=1. Replace its last bit by0 AND its first future exterior input by1, copying every later input. GC1057's merger makes every whole interior row after the first future tick identical to the candidate's, for arbitrarily long controlled continuations. The initial first-column bit also agrees since m>=4. This is a trace-preserving correction of that candidate.

Crucially, the corrected row and first input have a common actual two-tick origin retaining K. Append initial cells d=e=1 at j+2,j+3, with every farther tail allowed. Write S for time2 site j+2 (the first future input). Then (Q,R,S)=101 in both source cases. In GC1060 notation A=a XOR(b OR c), B=b XOR(c OR d), C=c XOR(d OR e), D=d XOR(e OR f), with arbitrary f. The first suffix gives (P,A,B,C,D)=(0,1,1,0,0), and the second gives (0,1,0,1,0). Thus Q=P XOR(A OR B)=1, R=A XOR(B OR C)=0, S=B XOR(C OR D)=1. All earlier child bits are fixed by K, and the original first two trace observations are retained. The actual origin also realizes the corrected first future interior update.

If the candidate already has R=0, either first input S lifts without changing the candidate: for S=0 choose (d,e)=(0,0) under0001 or(0,1) under1010; for S=1 choose(1,1) in either case. The same equations give QRS=100 or101, independently of f. Thus every candidate retains a prefix-compatible R and its first exterior input after the specified correction. These are exact three-bit lifts. Later candidate inputs still require temporal compatibility with that origin; the arbitrary-horizon equality is a statement about *controlled* continuations, not an actual whole-tail lift.

**A whole halfwidth horizon closes in one rooted cylinder.** Every white-start controlled strip of width at least4 beginning111r has seven-symbol trace

    110100(r OR d),

where d is its initial site5, or its first exterior input at width4. This extends the known GC605/606 entrance calculation without assuming an actual farther tail. Set A=NOT(r OR d). Its first four rows begin

    time1:100A; time2:01AC with C=A OR B;
    time3:11(NOT C)H with H=A XOR(C OR D);
    time4:00F with F=C AND NOT H=A.

B,D may be controlled exterior bits; the retained relation C>=A suffices. Time5 begins0F and the time6 first bit is NOT F. This proves the full formula for every later controlled input.

Consequently ANY white-start free width5 strip initially0001p has nine-symbol trace00110100b, where b=(p OR E) AND NOT G for its first two exterior samples E,G. Its time2 row begins1110b, so the formula applies. For an actual initial row0001p, its time2 fifth bit is p AND(x6 OR x7), by the local update. Thus actual0001bb, with any farther tail, has the same trace: its time2 fifth bit is b. This retains the first W-1=4 initial cells and realizes the entire target horizon2W-1=9 for this cylinder. The known GC605 entry witnesses supply both origins; the new step is their complete trace-repair obligation. In particular a future representative1111... may be replaced by actual11101... through its six-tick horizon, and that replacement lifts through initial0001 with cells5,6 black.

**Controls and remaining gap.** All32 seven-input local cones (two suffixes, both phases) and8 explicit QRS lifts pass independent literal/packed evolution. Four selected translated controlled trajectories agree after the coupled correction; eight width4 controls check the mask identity. Sixteen selected root-strip controls match the actual normal form. Unexpected guard: free initial00010 with first inputs10 has time8 endpoint1, while every actual initial00010 has endpoint0; the last initial bit must change. Correcting only the child boundary bit while retaining first input0 also fails the whole-child merger. The correction must carry the input, not just the bit. No general full-horizon induction follows: forced-zero cases with Q=0, forced-one cases, and compatibility of later exterior samples remain missing. Next hand target is one of those remaining carriers; Cloud review and that specific design obligation flagged after publication. Halfwidth and the all-depth prize bound remain open.


**GC1062 publication receipt.** Verified0701b2fb: CL230 confirms GC1061's complete packet origin on4,096 initial cones, both phases, and accepts the reviewed transport composition; GC1061 is second-read. Verifiedd9ba0aeb: L610's witnesses at18 cover125..136 except132 (undecided); no new job or solver work here. The forced-zero bridge is the new review request.


## GC1063 — A white zero collar reads the forced boundary bit before the horizon (2026-10-10)

**Missing inference, GC1060/1062.** The Q=0,R=0 carrier has no black predecessor for the merger. Can matching future traces instead forbid a wrong R, with an actual trace-preserving origin? Seek a readout and origin for the rooted initial1001 branch. Record searched:00110|11001100|1001000|1001001 with time.?5|time.?8|readout|halfwidth|repair|first.*nine ->27 hits. GC1019's known eight-tick delay starts from prepared100110, not this four-site origin condition; it is not rerun. Predictions and controls precede execution in rule30_zero_carrier_readout.py. No solver, word-membership or width sweep.

**Controlled readout, confirmed CL232.** Every white-start width4 controlled row000r has trace00110r through time5, regardless of every exterior sample. Its seventh symbol is0 if r=1; if r=0 it is (NOT E) AND(F OR G), where E,F,G are its first three exterior samples. Hence any actual future representative retaining the first three zeros and matching the actual source branch's six-symbol future prefix001100 must keep R=0. This is observation-based selection of a forced-zero bit with Q=0, rather than the Q=1 merger.

For the local proof, the first update begins00r(r OR E); the second begins(1,r,r OR E,C) with C=r XOR(r OR E OR F). If r=1, its first four cells are1110, and GC1062's reviewed111r formula gives the stated seven-symbol trace0011010. If r=0, the second row begins(1,0,E,E OR F). Its next first four cells are(1,NOT E,E OR F,H), with H=E XOR(E OR F OR G). The fourth row begins00A, with A=(NOT E) XOR[(E OR F) OR H]. If E=1 then A=1; if E=0 then A=NOT(F OR G). Thus the fifth-row first bit is0 and the sixth is NOT A=(NOT E) AND(F OR G). All symbols used are interior bits or the specified controlled inputs; later input correlations are unnecessary.

**Complete root-cylinder lift.** Any white-start free width5 initial row1001p has first two observations11 and time2 row0000S, where S=(p OR E) AND NOT G for its first two exterior samples. Apply the readout using its site5 track: its first three width4 exterior samples are S, S OR H, S XOR(S OR H OR I), where H,I are the original strip's next two exterior samples. The nine-symbol full trace is therefore

    11001100b, with b=(NOT S) AND(H OR I).

For either b, actual initial100100(NOT b), with ANY farther tail, has that trace and retains the first W-1=4 initial cells. To check the origin algebra, write f,g,h for its initial sites7..9. Its time2 sites5..7 are

    0, NOT(f OR g), f XOR[(f OR g) OR(f XOR(g OR h))].

The last two have OR=NOT f: f=1 makes both zero; f=0 gives NOT g and g OR h. The actual version of the readout for prefix0000def has seventh symbol(NOT d) AND(e OR f), so this origin has endpoint NOT(initial site7)=b. Thus the whole horizon2W-1=9 closes in this rooted Q=0 branch, including the correlated two-bit child tail; no arbitrary repaired row is restarted mid-orbit.

**Controls, limitation and receipt.** Thirty-two selected width4 streams verify the readout under independent literal and packed updates. All32 root parameter combinations match64 actual normal-form controls (two farther-tail extremes). Unexpected spatial guard: prefix010r, also with penultimate0, emits1 at time5 for BOTH r values (four selected controls). Q=0 alone therefore supplies no readout; the three-zero collar is essential. This countercontrol leaves the other rooted Q=0 branch (initial0010 at white phase) for a different mechanism, and no translation to arbitrary j is claimed. Verified186484b3: CL231 confirms GC1062's carrier and both trace formulas, with its stated896/512 cases; promoted. The new Intel handover announcement changes no present lane. Next missing inference is a depth-uniform collar or replacement argument for the remaining forced carriers. General halfwidth, later exterior compatibility and the all-depth prize bound remain open.


## GC1064 — Releasing one origin cell removes every white forced-zero carrier at arbitrary depth (2026-10-10)

**Missing inference, GC1060/1063.** The white-predecessor forced-zero readout lacks a depth-uniform collar. Instead of fixing the original initial prefix through j+1, retain it through j, while still retaining the COMPLETE time2 child prefix through j. This is permitted by the unconditioned halfwidth question, which prescribes a trace rather than its entire initial row. Record searched:two.tick|two.step|halfwidth|child.*prefix with one.*(cell|bit)|releas|relax|shorter and lift|boundary|origin|freedom ->30 hits in13 files. GC1060's local equations are reused; no released-cell whole-prefix criterion surfaced. Predictions and controls precede execution in rule30_released_origin_cell.py. No solver, word-membership or width census.

**Uniform actual-origin freedom, confirmed CL235.** Fix any actual initial prefix through j, j>=3, and any feasible time2 child prefix through j. Suppose its last bit Q is white. Let u,a,b be initial sites j-2,j-1,j. Either value of the next child bit R has an actual two-tick origin retaining BOTH prefixes, except when uab=011, which forces R=1. Thus every forced-zero case with Q=0 in GC1060 becomes free after releasing exactly one initial cell. This holds at every j and both clock phases, with any farther tail. The original first two trace observations remain unchanged.

**The preceding child cell is the essential guard.** Write c,d,e for initial sites j+1..j+3. In GC1060 notation put

    P=u XOR(a OR b), A=a XOR(b OR c), B=b XOR(c OR d),
    C=c XOR(d OR e), Q=P XOR(A OR B), R=A XOR(B OR C).

The preceding child bit is F=H XOR(P OR A), with H the first-update bit at j-2, fixed by the retained initial prefix. All earlier child cells through j-2 are fixed too. If b=1, A=NOT a is independent of c; if P=1, P OR A=1. Hence c may change while retaining F exactly when b=1 OR P=1. Otherwise b=P=0 and A=a XOR c, so retaining F pins c. An unguarded union of GC1060's pair tables would miss this constraint.

For Q=0 the feasible origin triples and explicit extensions are:

| Retained uab | New c,d,e realizing desired R |
| --- | --- |
| 000 | 0,0,R |
| 001 | 1,0,R |
| 010 | 0,0,NOT R |
| 011 | 0,0,0; only R=1 |
| 100 | 1,0,0 for R=0; 0,1,0 for R=1 |
| 111 | 1,0,NOT R |

The other triples101,110 cannot have Q=0. In the000 row, feasibility already requires the original c=0; the construction keeps it. Every other row permits c to change by the guard above. Substitution gives Q=0 and the claimed R, while preserving F and every preceding child cell. This proves sufficiency with an explicit finite origin extension, not a free mid-orbit restart. For011, P=1,A=0; Q=0 requires B=1, forcing c=d=0. Then R=0 XOR(1 OR C)=1 for every e, proving the sole obstruction's necessity.

**Controls, sharpness and next inference.** All256 seven-cell local cones in both phases agree under literal and packed updates; all456 permitted-bit constructors preserve the full child prefix and the original first two observations under both farther-tail extremes. Of these,152 change the released initial cell. The first executable111,Q1 constructor used the wrong d; its mixed-pair equation gives d=0, and the witness was corrected before the passing run. The fibre criterion itself was unaffected. Unexpected check: original0001 with Q=1 appears to gain R=1 by releasing c if only Q is retained, but the preceding child cell flips. Whole-prefix retention correctly excludes that construction.

This supplies an arbitrary-depth alternative to the special zero collar: the forced-zero/white-predecessor origin obstruction itself disappears when one initial cell is released. It does not supply the selected child's whole tail or a matching future trace. The remaining white-predecessor carrier is now precisely011 with Q=0,R=1; black-predecessor carriers and later exterior compatibility also remain. Next useful inference is a future-trace repair compatible with that single white carrier, or a counterexample to that repair. Cloud hand review and that concrete design question requested and flagged; no worker run. Halfwidth and the all-depth prize bound remain open.


**GC1064 recovery receipt.** Verified016a8e79: CL232 independently confirms GC1063, including correct exterior indexing, the full root-cylinder formula and every farther-tail origin; promoted. IN001, CL233 and L611 received. The skeptics qualify the soficity evidence and correct the absent-word family; no lane change or repeated computation. The owner-requested connectivity check succeeds, the research heartbeat remains active, and publication resumes from the committed GC1064 checkpoint.


## GC1065 — The remaining white carrier lifts its next bit and first future input together (2026-10-10)

**Missing inference, GC1064.** Its sole white-predecessor guard011,Q0,R1 still blocks a future R0. Release the preceding initial boundary position too, while retaining the COMPLETE child prefix. Record searched:white carrier/origin release/prefix j-1 ->12 hits in4 files; frontier/ENTRY/G236 with011 and origin/prefix ->82 hits in33 files. GC549 checkpoint28 already has exactly the five-state frontier encountered below; its missing011 certificate is reused, not re-derived by another subset census. Predictions and independent controls precede execution in rule30_white_carrier_pair_lift.py.

**Joint actual lift at every depth, confirmed CL236.** Fix an initial prefix through j-1 ending01 at sites j-2,j-1, j>=3, and its feasible time2 child prefix through j ending Q=0. Every pair R,S at the next two child sites has an actual two-tick origin retaining these prefixes. S is the first future exterior, so the selected child row through j+1 AND its whole first future interior update lift together. The first two original trace observations remain unchanged. Relative to GC1060, two initial positions j,j+1 are released; in its remaining011 branch the pair construction changes only the formerly fixed bit at j from1 to0.

Use GC1064's u,a,b,c,d,e and let f be the next initial bit. Here u=0,a=1, so the first-update bit P at j-1 is1 for either b. Consequently the second-update cells j-2 and j-1 are independent of BOTH released b,c: their OR gates see this black P. Every earlier child cell is already fixed by the retained initial prefix. Choose

    b=c=0, d=(NOT R) AND(NOT S), e=(NOT R) AND S,
    f=S when R=1; arbitrary f when R=0.

Then A=1,B=d,C=d OR e,D=d XOR(e OR f). Thus Q=0, the next child bit is1 XOR(d OR e)=R, and the following bit is d XOR[(d OR e) OR D]=S. For R=0 this is S=NOT d; for R=1, d=e=0 and S=f. Farther initial bits cannot affect the specified child prefix and pair. This is an actual origin construction, not a trace-only toggle or a restarted orbit.

**Exact remaining tail carrier, reusing G236.** After Q=0, the two-step transducer's state (a,b,c,d) ranges over exactly

    A={1000,1001,1010,1011,1100}.

Indeed bc=00 or01 permits either d; bc=10 requires d=0; bc=11 gives Q=1. These are compatible with the entire preceding child prefix as proved above. Therefore the conditional language of EVERY remaining child-tail cell is exactly the existing G236 language from A, uniformly in j and wall phase. A path supplies an initial extension, and conversely every extension supplies a path; the finite-prefix and infinite-path scopes are the usual G236 construction. In particular G236's known missing tail011 still applies: releasing two positions does NOT make arbitrary whole child tails lift.

**Independent controls and unexpected failure of a greedy origin.** All256 local cones in both phases pass literal/packed checks;160 qualifying Q0 origins respect the reviewed guard. All64 joint constructors preserve the full child prefix, first two original observations and first future interior update. Unexpectedly the convenient b=c=00 normal form loses valid three-bit tails: with R=S=1 it forces the third child bit1, whereas b,c,d,e,f,g=0,1,1,1,0,1 realizes110. Four selected controls verify this discrepancy. Thus retain all five carrier states for longer selection; do not iterate the chosen normal form greedily. No solver, visible membership, width sweep or automaton exploration. Verifiedd7c4544c: CL234's orchestration update received without lane change. Next missing inference is trace-preserving future selection inside this specific retained A-language, beyond its first boundary pair. Cloud review and that concrete design target flagged; general halfwidth and the all-depth record bound remain open.


**GC1065 publication receipt.** Verified e5711114: CL235 independently confirms GC1064 at j=3..6 in both phases, with180 Q0 contexts (150 free,30 in011), the whole-prefix guard and its hand proof. GC1064 promoted. Its individually free later bits are received; GC1065 retains their full joint tail relation rather than inferring independence. No computational duplication.


## GC1066 — The white carrier lifts two future updates, but exact row retention stops at three (2026-10-10)

**Missing inference.** GC1065 lifts the next child bit and first future input, but the second freely selected input still needs a compatible origin. Record searched: halfwidth|origin|white carrier with four tick|two future|second future ->13 hits in4 files. GC1059's masked-input primitive and GC1065's origin guard are reused. Predictions preceded the controls in rule30_white_carrier_two_future.py; no solver, membership or width census.

**Uniform hand construction, confirmed CL237.** Keep GC1065's initial prefix through j-1 ending01 and complete time2 child prefix through j ending Q0, j>=3. For ANY next child bit R and two future strip inputs S,G, an actual original row retains the selected time2 prefix through j+1 and BOTH subsequent complete interior rows through j+1. Original observations at times0,1 are retained. In the same initial variables set b=c=0 and choose (d,e,f,g):

    R=S=0: (1,1,G,0); R=0,S=1: (0,1,0,0); R=1: (0,0,S,0).

The next child triple R,S,T is respectively00G,010,1SS. The actual second exterior is R XOR(S OR T). If R=S=0 it equals G. Otherwise the first updated boundary bit is R OR S=1, masking any mismatch with G on the second update. All other cells already have the correct neighbours. GC1065's black P guard preserves the entire preceding child prefix under the initial change. This supplies an original four-tick cone with two subsequent full rows, without demanding equality of the irrelevant exterior sample.

**Concrete limit to iteration.** Take a feasible child ending L,Q,R,S,T=10001, where L is site j-1, and free future inputs010. Matching the first interior row forces S0; matching the second, with L1,Q0,R0, forces T1 and leaves the boundary white. Its third actual exterior is (R OR S) XOR[(R XOR(S OR T)) OR(S XOR(T OR U))]=1 for EVERY U. The requested third input0 therefore flips the last interior cell. No original tail can retain all three rows. Such a child has an actual GC1065 origin: retained initial site j-3=1, sites j-2,j-1=01, then b=c=0,d=e=f=1,g=0. This works at every j>=4 in both phases (also j=3 in the black phase). The obstruction already occurs in ordinary Rule30 future dynamics; it is not a new absence of the A-language.

**Controls and next inference.** All64 literal/packed original cones retain the past and both future rows;24 have masked exterior mismatches, refuting the stronger equality requirement. Eight controls with arbitrary U verify the third-row obstruction. The unexpected observable check retains the same first-column trace through that horizon despite the different last cell: this is a failure of complete-row iteration, NOT a halfwidth counterexample. Future selection must now quotient the specific third-row boundary discrepancy or change earlier child representatives before it becomes observable. General halfwidth and the all-depth record certificate remain open. Verified6ee2f664; Intel's strategy claim received without a lane change. Deferred GC1065 integration completed before this block.


**GC1066 review receipt.** Verified250eadbe: CL236 independently confirms GC1065 in30 retained contexts, both phases, and accepts the five-state carrier and greedy-origin failure. Promoted GC1065. Its extra checks on other initial endings are received as scoped computation; no pair freedom outside the stated01 hypothesis is inferred. GC1066 keeps that same hypothesis and remains the new review target.


## GC1067 — An alternating collar repairs the third-row barrier before readout (2026-10-10)

**Missing inference.** GC1066's row-retention barrier might admit a changed child representative. The concrete target is its child10001/input010 obstruction with an alternating inner collar and fourth input0. Record searched:010100|010101 with merge|coalesce|repair|rewrite|four tick ->13 hits in8 files;01100|010100 with origin|third|halfwidth|boundary ->44 hits in19 files. GC1057/1059 masks and GC1065 origin retention are reused. Predictions precede controls in rule30_white_barrier_observable_repair.py. No solver or language/width census.

**Controlled trace repair, PROVED (CL238).** At any width W>=6 and either wall phase, replace the initial final six bits010100 by010101 AND exterior input block0100 by0101. Copy every later controlled input. Every row differs only in the last two cells before update4; at update4 the complete interior rows coincide, and thereafter stay equal. Thus the complete first-column trace agrees at every horizon. This does not require equality of intermediate rows.

Let L be the third-last cell. The common alternating collar0101 preceding the last pair keeps L=1 at times0..3, masking any changed right neighbour. The last-pair recurrence is (Q,R)'=(1 XOR(Q OR R), Q XOR(R OR E)). With the stated inputs its old/new pairs are

    time:       0       1       2       3       4
    old:       00      10      00      10      01
    new:       01      01      01      01      01.

All earlier cells coincide by the black-centre mask. The common time4 pair01 makes the last cell black again at time5. Therefore even WITHOUT copying exterior inputs, arbitrary differences in the next two samples are masked: the complete time5 and time6 interiors still agree.

**Actual original origin.** For j>=7 retain an original prefix through j-1 ending010101 and its feasible time2 child through j ending Q0. The child suffix through j is01010 (direct two-step update of the retained alternating collar, with GC1065's P1 guard). A future controlled row appending R0 and inputs0100 followed by any two samples can be realized through SIX future updates, preserving the original first two observations. Replace original sites j..j+6 by0000001 and allow every farther tail. This keeps the child prefix through j, appends child1001 at sites j+1..j+4, and forces its actual first four future exterior samples0101: with R,S,T,U=1001, the exterior after one update is1, after two is0, and after three is U OR V=1. The controlled merger and two subsequent masks prove the actual nine-observation lift. After that horizon, matching the actual exterior to the copied controlled continuation is still missing.

**Failures and controls.** The first hand candidate01100 incorrectly assumed the discrepancy remained outward: its first updated inner neighbour is white, letting a second-row difference enter the third-last cell. Two literal controls retain that failure. Changing the TARGET fourth input from0 to1 also destroys update4 coalescence (32 negative controls), so0100 is essential here. The passing controls cover32 mergers with arbitrary earlier bits, both phases and continuations, and64 actual original cones with arbitrary farther bits and the two additional target inputs. This is a specific observable repair of the GC1066 barrier, not an all-case repair or halfwidth theorem. Next missing inference is later actual exterior closure for this common row or a wider collar repair covering the remaining contexts.


**GC1067 receipt for CL237 at69d3f398.** Independent960-case constructor and1,920-child barrier review accepted; GC1066 promoted. The offered boundary quotient is received as a design suggestion, not an equivalence theorem. GC1067 supplies its concrete changed-representative instance, with later actual closure still missing.


## GC1068 — The first unmasked post-merger input admits both actual origins (2026-10-10)

**Missing inference.** GC1067's actual repair stops after six future updates. Match its next exterior sample when the common boundary becomes white. Record searched:110100|six input|time6 with carrier|origin|image|constant1 ->43 hits in19 files; black boundary|constant1 with six|seven and exterior|origin|image ->31 hits in15 files. Reuse GC1067's collar and merger; no solver, membership, NFA or width census. Predictions precede controls in rule30_white_collar_next_input.py.

**Hand closure of one more input, PROVED (CL240).** Retain the same original prefix through j-1 ending010101, j>=7, and feasible time2 child through j ending Q0. A target child appending R0 with future inputs0100xyz has an actual origin preserving its first TEN original observations and its complete future interiors at times4..7. Replace original sites j..j+6 by0000000 if z=0, or0000111 if z=1; every farther tail is allowed.

Both constructors retain the complete child prefix through j and append R1. The resulting child ends010101. Its last cell stays black at future times0..5, so NONE of the first six actual exterior samples affect its interior. The GC1067 merger therefore works with these actual samples, even though they need not be0101; the two following masks retain the target's arbitrary x,y. It remains only to match the actual exterior at future6 to z.

Write S,T,U,V for the child's next sites beyond R. For z=0 the origin gives S0. With left driver R=1, S0 implies S after two updates is0: S'=NOT T, T'=T OR U, so S''=NOT(NOT T OR T OR U)=0. Repeating this through time6 gives S6=0. For z=1 the origin gives R,S,T,U,V=11101, uniformly over farther bits. With the same black driver, its successive right prefixes are

    future time: 0     1     2     3    4    5   6
    S onward:   1101  0001  1011  001  111  00  1.

Each displayed cell uses a fixed black OR mask or the preceding displayed prefix. Thus S6=1. Matching z gives the seventh complete future update. This is a specific ten-observation origin lift, not an iteration to arbitrary horizons. For example, z=1 makes the NEXT actual exterior equal NOT R6; later requested samples remain correlated.

**Controls and retained failure.** All128 literal/packed original cones preserve the past, trace and seventh future update in both phases, with arbitrary selected earlier/farther bits. The earlier fixed0000001 origin always has S6=0. It fails32 controls requesting z1 with a white boundary at future6, but32 otherwise identical black-boundary controls mask that mismatch. In these selected contexts the boundary is the retained earlier child bit p: its leading left-to-right causal path crosses six alternating OR=1 gates, giving R6=p. The first hand attempt to arrange S6=1 used V2 instead of the required V3; the corrected11101 shield above avoids that indexing error. Next missing inference is coupled input7 compatibility after this origin selection, or a representative repair when its forced next sample is wrong.


**GC1068 receipt for CL238 at195dd080 and CL239 at0b8a322f.** The independent30-context merger and96-origin review is accepted; GC1067 promoted. The survey of157 repairable pattern/input pairs supports pursuing changed representatives, but is not an all-context closure proof. The corrected even-length tightness at2,4,36 is received; no odd-only induction shortcut is assumed. GC1068 still awaits its separate review.


## GC1069 — A white-white endpoint forces the next input; its trace can still lift (2026-10-10)

**Missing inference.** Choose GC1068's eighth future input without mistaking a full-row obstruction for visible failure. Record searched: boundary|exterior with consecutive|successive|two white|white.white|input7|input.?10 ->63 hits in22 files; input7|NOT R6|coupled input7 ->2 hits, GC1068 only. Predictions and independent controls precede execution in rule30_white_collar_pair_guard.py; no solver or language census.

**Universal obstruction, PROVED (CL241).** Write Q,R for the final two interior cells and S,T outside. Every actual cone obeys R'=Q XOR(R OR S), S'=R XOR(S OR T). If at future6 Q=1,R=0 and at future7 R=0, then S6=1 and S7=1, independently of T. A target exterior block ending10 therefore cannot retain its complete interior rows6,7,8 under ANY actual representative. This is stronger than failure of GC1068's chosen origin. An explicit retained original prefix10010101 in phase0 gives target child0000010100 with inputs01000010; its Q6,R6=10 and R7=0 satisfy the obstruction.

**Visible lift despite the obstruction.** GC1068 gives complete interior equality at original time9. With the same left clock, arbitrary later exteriors cannot distinguish column1 before original time W+9: the first possible difference is at siteW at time10, then moves left at most one site per update. Consequently every continuation of the specified collar target lifts its first W+9 original observations. This proves the full 2W-1 halfwidth horizon for this cylinder at W=8,9,10, not for arbitrary cylinders or widths. For W>=11 the remaining visibility deficit is W-10 observations. The obstruction is in the hidden rows, not these observed prefixes.

**Review receipt and controls.** CL240 at9572abc4 independently confirms GC1068 on384 cones; accepted and promoted. CL240.1 at212f1f5e correctly withdraws the claim that its zero branch leaves input7 free: both specified origins force S7=NOT R6. For the zero origin, the child begins R,S,T,U,V,W=1000i(i OR k) with i,k arbitrary. Under black R through5, S6=0: if i=0 then T2=1 stays black at even times; if i=1 then T2=T4=0 but U4=V4=0, so T6=1 again. Thus S7=R6 XOR T6=NOT R6. A wrong requested sample needs no interior repair when R7 is black. Added controls after receiving that correction verify both branches and this mask: 128 masked mismatches and128 full-row failures among512 selected W10 contexts, including32 universal white-white obstructions. Two continuations per context give1,024 nineteen-observation lifts, literal/packed engines agree. The unexpected check is that all those row failures still lift the full halfwidth trace. No independent-input assumption survives. Next: a different representative past the first visible deadline, or a finite coupled boundary invariant; all-context halfwidth and the record bound remain open.


## GC1070 — Long alternating collars release a locked exterior pair, not a free sample (2026-10-10)

**Missing inference.** Can GC1068's first-unmasked-input construction scale with alternating-collar length? Record searched: alternating|collar with difference|discrepancy|visibility|deadline ->29 hits in8 files; collar|alternating with black.lock|nine.black|constant.black|9.*lock|long.*collar ->23 hits in10 files. Reuse the reviewed nine-update black-wall lock of PROOFS entry38, not a new lock census. Predictions precede controls in rule30_long_collar_release.py.

**All-length release guard, reviewed (CL242; independent controls at K10).** Let even K>=10, W=j+1>=K+2. Retain the original prefix through j-1 ending (01)^(K/2), and its feasible time2 child through j ending Q0. The repaired child appending R1 has final K cells (01)^(K/2). These remain alternating in the triangle shrinking from the left; its last cell R is black at future times0..K-1 for EVERY exterior. Entry38's black-wall lemma forces the next exterior pair S,T=01 by future9, and it persists through futureK. Thus the first released sample S_K is forced0 for every actual tail. After release S_(K+1)=NOT R_K. Larger collars give a deterministic coupled interface, not more independent-input freedom. In particular R_K=0 with requested inputK=1 makes full-row retention at K+1 impossible for every actual tail of that repaired child. For K>=14 the same obstruction holds even if only the common rows4..K are retained: their K-4 black-driver updates suffice for the lock, regardless of the earlier representative.

**A positive visible cylinder at every width.** Give the target child R0 and future inputs0100, arbitrary samples4..K-1, then sampleK=0. Replace original sites j..j+6 by0000000, with arbitrary farther tail; GC1068's origin guard preserves the child prefix and appends R1. GC1067 merges all interiors at future4; the black endpoint masks every intermediate sample, and the locked exterior0 matches sampleK. Complete interiors therefore agree through futureK+1 (original timeK+3). Locality lifts the first W+K+3 original observations under arbitrary later controlled inputs. If K>=W-4, this covers the full2W-1 halfwidth horizon. Such even K exist for every W>=12, subject to this specific initial collar and released zero; no all-context halfwidth result is claimed.

**Controls and review receipt.** At K10,18 and W=K+4,128 selected origin/continuation controls pass literal/packed engines and the complete halfwidth trace. Requesting released1 with R_K=0 gives64 full-row failures, but all64 observed halfwidth traces still match: evidence of extra zero-lane shielding, not a proved larger horizon. The independent-input counterfactual fails by the all-length lock argument. CL241 at121a9f1f accepted; GC1069 promoted. Its later-visibility samples are received as evidence, and no exhaustive horizon run is requested. Next proof target: a uniform zero-lane obstruction at the first released mismatch, or a compatible finite carrier using this forced01 exit. General halfwidth and the all-depth record bound remain open.


## GC1071 — A finite moving-front selector heals coupled long-collar releases (2026-10-10)

**Missing inference.** Identify a uniform black shield after GC1070's first released mismatch. Record searched: zero.lane|anti.diagonal with collar|black|repair ->1 irrelevant hit; front|moving.frame|diagonal with collar|period.?16|four.bit|four.cell ->60 hits in28 files. Reuse GC1070's lock and GC1057's last-cell merger. Predictions and controls are in rule30_collar_front_selector.py; no solver or language census.

**Exact finite front, PROVED after CL243 independent review.** Assume the repaired child has even K>=10 alternating final cells and a white cell immediately before them, at i=W-K. Put a_t=x_t(i+t), b_t=x_t(i-1+t), c_t=x_t(i-2+t), with a_0=0, b_0=b, c_0=c. The untouched alternating cells ahead have OR1; the next ahead bit equals a_t. Thus through the collar the moving frame closes exactly as

    a'=NOT a; b'=b XOR a; c'=c XOR(b OR a).

At release the actual locked exterior01 keeps the needed recurrence valid. The common inner cell at futureK+1 is C=c_(K+1), with

    K mod8:    0       2       4           6
    C:         c XOR b c       (NOT c) XOR b NOT c.

Also B=b_K=b XOR((K/2) mod2). This is an all-K finite selector: a has period2, b flips every two updates, c flips after four, so the complete triple returns after eight.

**Exact coupled repair.** The target released sample1 differs from actual0 at the white endpoint R_K=0. At K+1 the actual/target endpoints are B and NOT B, with common inner neighbour C; the next actual exterior is1. Target next sample w merges the COMPLETE interiors at K+2 exactly when C=1 and (w=1 OR B=0). If C=0, the difference enters the next inner cell; if C=1 it is masked there, and the endpoint equality reduces to (NOT B) OR w=1. Hence every such target lifts W+K+4 original observations under arbitrary later controlled samples. This supplies a coupled finite repair beyond the released-zero cylinder, not a general zero-lane invariant.

**Failure, controls, receipt.** The first negative control incorrectly required w0 always to break merger: K10,b=c=1 has C1,B0, so the target endpoint is already black and masks w0. Retained and corrected before the added controls. Four exact eight-step cycles and128 literal/packed origin-front controls at K10,12,14,16 pass;64 released11 mergers,32 additional masked10 mergers,32 genuinely failing10 controls. CL242 ate776b643 accepted; its K10 exhaustive review supports GC1070, while K18 controls remain GPT's. Ledger rotation adopted before appending. Next missing cases have C0 or C1,B1,w0; they need a later coupled repair or a different representative. General halfwidth and the prize bound remain open.


CL243 at a99a152a independently confirms the recurrence and exact merger criterion, exhaustive at K10 and sampled at K12; GC1071 promoted. Its black-before cases are a separate additional branch.

## GC1072 — The unhealed collar has three white propagation centres at unbounded lengths (2026-10-10)

**Missing inference and failed prediction.** GC1071 leaves C=0. For W=K+4, a released-one discrepancy first appears at future K+1; only its fastest leftward path can affect the last halfwidth observation. Predicted that one of the first three propagation centres is black. Record searched: collar|front with zero.lane|fastest|halfwidth|seven.cell ->22 hits in 10 files. No such exclusion was established. This prediction is REFUTED, including an infinite family; no fourth-centre search follows.

**Finite certificate, independently confirmed CL244.** Retain original prefix p0(01)^(K/2) and the GC1070 all-zero extension, with even K>=10. In the actual future define z_r(t)=x_t(4+t-r), r=0..6. Start at future2, when the frame covers sites0..6 and includes the real wall bit. Its triangular recurrence is z_0'=NOT z_0, z_1'=z_1 XOR z_0, and z_r'=z_r XOR(z_(r-1) OR z_(r-2)). The alternating collar supplies the ahead bits. For the three centres z_2(K+1), z_4(K+2), z_6(K+3), their dependency triangles stay inside the retained row through future K. GC1070's locked exterior supplies the final endpoint update; later exterior values cannot change these centres.

For p=phase=1 the future2 state is 0101101. Direct iteration returns this state after 32 steps; after11,12,13 steps it reads 1001111,0111000,1100110. Thus at K=12+32n all THREE centres are white, for every n>=0. This proves recurrence of the specific local obstruction, not a complete zero lane or visible absence. A black shield farther left, healing, or a changed origin may still repair the trace.

**Controls and scope.** rule30_collar_zero_lane.py checks four exact32-step cycles and 256 actual fronts, all passing in independent literal/packed engines;32 three-centre and64 two-centre failures. Period16 fails on every rooted seven-bit state. The unexpected wall-initialization check caught a one-site offset: interior sites1..7 predicted001 where actual100; corrected to wall plus sites1..6 before rerunning. General halfwidth and the all-depth record bound remain open. Next work must use coupled visible repair or another origin, rather than assuming these three centres stop the defect.


CL244 at df94d896 independently confirms the exact period32 cycle, all-length negative family, and inward discrepancy; its eight white-centre residue classes are received finite-cycle computation.

## GC1073 — A high fifth-track LL selector forces two separated origin pins (2026-10-10)

**Missing inference.** Return to the recurrent S/L0 interface: determine whether GC1056's surviving LL selector can discard its farther origin correlation. Record searched: LL/long selector with successor/transport ->10 hits in 5 files; returned110/ninth with L0-L0 ->36 hits in 12 files; exact111001110 ->26 hits, none establishing the guard below. CL219's absence of returned seventh-to-ninth triple 110 was computation; its short hand proof now unblocks the selector argument. No Local solver, cut, membership or record run duplicated.

**New all-tail selector guard, proof sketch.** If an ordinary-long source begins 111001, its fifth pre-return track is 0101101010, and it returns L0, its initial sites 7 AND 9 are black. This holds without any preceding-type assumption.

Put b,c,d at initial sites 7,8,9. The time 3 sixth bit is NOT(A OR B), where A=NOT(b OR c), B=b XOR(c OR d). The time 3 and time 5 sixth bits are equal: GC1044's exact projection clauses A at 3 and B at 2, using the fixed fifth prefix 010110, give both implications. The high fifth selector has time 5 sixth 1 by GC1047. Hence A=B=0, which forces b=1 and c OR d=1.

The remaining branch bcd=110 ALWAYS returns S. Let e be initial site 10. The following shielding chains give actual sites 6 onward (only shown cells asserted; every farther tail is arbitrary):

| Time | e=0 | e=1 |
| --- | --- | --- |
| 1 | 100 | 100 |
| 2 | 011 | 0101 |
| 3 | 1100 | 1101 |
| 4 | 001 | 0001 |
| 5 | 111 | 101 |
| 6 | 100 | 101 |
| 7 | 01 | 001 |
| 8 | 11 | 01 |
| 9 | 0 | 0 |

GC1047 supplies fifth track 0101101010 in either branch. Its time 9 bit is0 and site 4 there is1; the displayed time 9 sixth 0 therefore gives returned fifth 1. This is S, contradicting the asserted L0 successor. Thus d=1 and the only high-LL origin triples are 101 or111. Their occurrence is not asserted sufficient.

**Past gate and retained failures.** GC1053's mid01 branch has time 9 sites 6..10=(1,0,Q,R,Z), so its returned triple is(NOT Q,Q OR R,Q XOR(R OR Z)), never 110. Its mid1 branch gives time 9=(1,p,p OR q,N,z), N=NOT p AND(q OR r); the return is(NOT(p OR q),N,(p OR q) XOR(N OR z)), also never 110. Thus a preceding L0 independently excludes that origin triple, but the new future-conditioned pin is stronger.

The initial proposed counterexample without an L0 past failed. A second prediction incorrectly held time2 site8 constant, omitting e; the intermediate control caught it. Splitting e repairs the proof. Changing e to1 still fails to restore high LL. Final controls:24 local identities,256 complete shielding cones,15 selected high-LL positives, independent literal/packed updates all pass. This supplies a correlated hidden-interface pin, not a record bound. Next inference is its transport through mixed S/L0 returns, retaining ninth-site correlation instead of fresh LL choices.


## GC1074 — The mature short-to-long high selector has an exact correlated origin gate (2026-10-10)

**Missing inference.** Transport GC1073's high-LL origin pins through a preceding S, retaining the ninth-site correlation. Record searched: 111010011|1110011 with high LL/profile/ninth pin/selector ->7 hits in 5 files; GC1052/1054/1056 give the existing mature branches and returned pair, not this ninth-bit formula. Reuse them and GC1073's equality of the time 3 and time 5 sixth bits. No solver, membership, mixed-word scan or relaxed-record computation.

**Complete mature SL coefficient gate, proof sketch.** At a mature S entrance (index 4 or later in a synchronized S/L run), the following L0 fifth track is high 0101101010 exactly when the S origin begins 11101001100 and, writing f,g,h,i for its sites 12..15,

    G = (f OR g) OR NOT(h OR i) = 1.

Otherwise that following L0 has low track 0101100000. This selects its fifth track; the next-return condition must be read separately. A high ordinary-L track alone does not assert a following L0.

**Hand transport.** GC1056 restricts a mature SL source to GC1054's branch A=111010001 or GC1052's branch B=111010011. A returns with site 7 white and sites 8 OR 9=1. B returns sites 7,8=(NOT w,w), w=initial 10 OR 11. When w=1, site 7 is also white. In both cases the next L0 time 3 sixth bit is white; the reviewed nonfork guards exclude the mid00 alternative, so its fifth track is low.

For B with w=0, the origin begins 11101001100. The returned sites 7,8 are 10. Define time 2 sites 11,12,13 by

    A=NOT(f OR g), B=NOT f AND(g OR h),
    C=(f OR g) XOR[(f XOR(g OR h)) OR(g XOR(h OR i))].

Their next first pair is D=NOT(A OR B), E=A XOR(B OR C). Local updates give time 4 sites 9..11=(1,0,NOT(D OR E)), time 5 sites 8..10=(0,0,D OR E), and returned site 9=D OR E. If f OR g=1, A=0 and D OR E=NOT B OR B OR C=1. If f=g=0, A=1,B=h,C=h OR i, giving D OR E=NOT(h OR i). Thus returned site 9 is exactly G for every farther tail. The next L0 has initial sites 7..9=(1,0,G), so its time 3/time 5 sixth bit equals G. GC1047 then selects the high track when G=1; when G=0, GC1052 bars L1 and the track is low.

**Finite hidden relation.** The high branch requires initial 10=initial 11=0 plus BOTH clauses (f OR g OR NOT h) and (f OR g OR NOT i). These are correlated origin conditions, not fresh ninth-bit choices. All-white f,g,h,i gives high, while f=g=0 and h OR i=1 gives low; the first pair alone does not decide it. 32 exact local gate controls, 26 high and 6 low, agree in independent literal/packed engines and all intermediate identities. The first white pair countercontrol passes. Next missing inference is transport through an ordinary L0 and composition without fresh origin bits; no all-depth record bound is claimed.


CL245 at 57efcfa2 independently confirms GC1073 as stated; its stronger exhaustive result excludes origin triple 101 from high LL. GC1073 is PROVED with that second reading. Composed with GC1074, this makes a high long track after a mature short return S: its origin triple is 101, so it cannot return L0. This last sharpening has CL245 computation plus the new hand transport as provenance; the all-tail hand exclusion of 101 is the next concrete proof obligation. The low branch and ordinary-L composition remain open.


## GC1075 — The high 101 long origin has an all-tail short-return shield (2026-10-11)

**Missing inference.** Replace CL245's exhaustive exclusion of high-LL origin 101 by hand transport, closing GC1074's high mature SL successor read. Record searched: 111001101|101.*high|high.*101 with shield|return|exclu ->11 hits in 5 files. GC1053 already handles 1011, but not the full 101 cylinder. No solver, language membership or mixed-word scan.

**All-tail hand proof, second reading pending.** Every ordinary-L origin beginning 111001101 has high fifth track 0101101010 and returns S. Its exact shield at sites 6 onward is:

| Time | Asserted prefix |
| --- | --- |
| 0 | 1101 |
| 1 | 1001 |
| 2 | 0111 |
| 3 | 1100 |
| 4 | 001 |
| 5 | 111 |
| 6 | 100 |
| 7 | 01 |
| 8 | 11 |
| 9 | 0 |

The first three updates use GC1047's ordinary-L fifth prefix 010110, valid for every farther tail. Each asserted output bit either has both right inputs displayed or has a displayed black input that masks the unshown bit. In particular the time 3 sixth bit is 1. GC1073's exact projection equates this to the time 5 sixth bit, so GC1047 selects the high track. This supplies the fifth bits used in the remaining displayed updates. They are the existing GC1073 1100 shield after time 3. At time 9 sites 4,5,6 are 1,0,0, hence the returned fifth bit is 1: the successor is S. No origin bit after site 9 is constrained.

Consequently every high LL origin begins 111001111: GC1073 already eliminated 110, and the new shield eliminates 101. GC1074's high mature SL produces precisely the long origin triple 101, so that long returns S. Its low track returns L0 by GC1047. Thus the fifth selector after a mature short determines the next S/L0 type; it cannot be an independently chosen high LL branch.

**Controls and retained failure.** Before controls the complete shield and high-then-S were predicted. All 15 one-step implications, with arbitrary fresh right bits, and 128 complete local cones pass independent literal/packed engines. The unexpected check incorrectly predicted that origins 101 and 1100 have different first two shield rows: the first cone already showed their common 1001 at time 1. Corrected before rerun; both have 0111 at time 2 and 1100 at time 3, even with unrelated farther tails. This strengthens the shield merger, not a complete row merger.

CL246 at a2a3f25c independently confirms GC1074's gate and intermediate identities, with the mature/startup distinction retained; GC1074 is PROVED. This new all-tail shield remains a proof sketch pending review. Next missing inference is ordinary-L transport of the surviving high-LL 111 origin, jointly with its next-return condition; all-depth composition and the prize bound remain open.


CL246.1 at 9b31ba05 corrects CL246's truncated time-16 return read; its longer complete cones confirm S. The gate review is unchanged. The successor claim here uses the new all-tail shield and complete return controls, independently of that initial incomplete read.


## GC1076 — An actual high LL carries a time-five marker into the next selector (2026-10-11)

**Missing inference.** Carry GC1075's high-LL origin 111 through the ordinary-long return without assigning a fresh next triple. Record searched: 111001111|high.*LL|LL.*high with transport|return|site9|ninth ->31 hits in 12 files. GC1053 has the general closing map; it does not supply the marker-dependent shield below.

**Hand transport, proof sketch.** An ordinary-L origin 111001111 has time 4 sites 6..8=000 and time 5 sites 6,7=10. Write a,b,c at time 5 sites 8,9,10. Its high fifth track returns L0 exactly when a=0 and b OR c=1: the time 7 seventh bit is automatically 0, and its eighth is 0 precisely under that condition, by GC1047's closing read.

On that return, the two updates give time 6 sites 6..9=(1,1,b,1) and time 7 sites 6..9=(0,0,0,NOT b). The retained marker b is therefore essential. If b=0, c=1 and the time 7 tenth bit is also 0. GC1053's high closing map has p=1,q=0, hence returned sites 7,8=00; its proved OR guard forces returned site 9=1. This branch returns triple 001 and cannot make the next fifth track high.

If b=1, time 7 has FOUR whites at sites 6..9. Write Q,R,S at its sites 10,11,12. Using the actual fifth bits 0,1,0 at times 7,8,9, three local updates give the returned triple

    (NOT Q, Q OR R, NOT Q AND(R OR S)).

It is 010,100,101 or111. GC1073's time-three/time-five identity at the returned L0 makes its next fifth track high exactly when its ninth bit is black, equivalently Q=0 and R OR S=1. Thus any further high track requires b=1; a further high LL additionally requires R=1, since 101 forces S by GC1075. These are correlated samples on the SAME actual history, not freely realizable Q,R,S states.

**Failures and scope.** The first prediction incorrectly made time 6 site 8 equal b OR c, giving an unconditional four-white shield. The local b=0,c=1 control refuted it: that branch has 0001 at time 7. The second prediction wrongly made every non-high next track the low renewal D=0101100000. Origin 11100111101101 followed by zeros returns 001, then track X=0101100101 and exits the synchronized S/L0 collar. That unconditioned low-track inference is closed. On an actual continuing mature run, X is excluded by the next return premise; outside it, retain D and X separately.

All 48 local two-tick shields and 8 closing identities pass. Among 64 selected actual origins, 29 are current high LL: 23 next D, 6 X exits, no next H. This sample absence does NOT prove that further H is impossible. Literal/packed engines agree. The unexpected common-map claim also fails: at Q=1,R=S=0 the reviewed low mid01 map gives 011, while this high branch gives 010. The added algebra control shows the maps agree only for Q=0; Q=1 is pinned to 010 here for every R,S. Thus the retained high past removes a low-branch output rather than merging the complete maps.

CL247 at 8e871b28 independently confirms GC1075, now PROVED. Next specific obligation is whether the actual b=1 ancestry excludes or restricts Q=0,R=1 (the next high-LL gate), keeping the farther samples coupled. No Local solver, membership or relaxed-record run. No all-depth bound claimed.


## GC1077 — Actual high LL forces a white seventh return and cannot repeat high (2026-10-11)

**Missing inference.** GC1076 leaves a relaxed next-high gate b=1,Q=0,R OR S=1. Derive its actual ancestry exclusion. Record searched: high/high or 111001111 with ancestry/transport/gate ->21 hits in 8 files; high LL with 001/010, consecutive high or Q=1 ->18 hits in 11 files. The retained 29-sample absence was not proof. Predictions and local controls preceded the incoming CL248 computation.

**All-tail hand proof, second reading pending.** A high LL origin begins 111001111 by GC1075. At time 1 its sites 6..9 are 1000. Write u,v,w at sites 10,11,12 there. Local updates give time 2 sites 9..11=(u,u OR v,u XOR(v OR w)), and time 3 sites 8..10=(NOT u,u OR v,NOT u AND(v OR w)). Consequently the time 5 eighth bit a equals 1 when u=1 and NOT(v OR w) when u=0. Closing L0 requires a=0, so u=0,v OR w=1. Under that condition the time 5 ninth bit b is NOT v.

For b=0 GC1076 already forces returned sites 7..9=001, whose following fifth track cannot be high. For b=1 the actual earlier bits must be u=v=0,w=1. They force time 3 sites 6..12=1110110 and time 4 sites 6..11=000010. Write E,F for the next two sites of that time 4 row. Time 5 sites 6..12 are then

    (1,0,0,1,1,NOT E,E OR F).

Since NOT E OR(E OR F)=1, the next row has sites 6..11=111100, and time 7 sites 6..10=00001. Thus Q=1, independent of every farther tail. GC1076's closing map returns 010 regardless of R,S, contradicting the necessary Q=0 for another high track.

The returned 010 origin always has the ordinary low track D: its sites 6 onward at times 1..5 are 101,001,011,010,01, so its time 5 pair is the reviewed mid01 selector. It renews L0. Therefore every high LL returns triple 001 or 010, with seventh site WHITE; its successor ordinary-long fifth track is never high. In a continuing mature S/L0 run it is D. The 001 branch can instead exit with X outside that premise. This is an all-length hidden-track exclusion, not a ban on untyped visible LL or a record bound.

**Controls and unexpected check.** All 16 local origin gates, 8 shield continuations, 4 closing identities and 48 actual controls on the two b=1 cylinders pass literal/packed engines. The retained 001-to-X witness still exits. A relaxed time 4 band 00001110 really reaches returned triple 111 and passes the next-high gate, but its eleventh site is black where actual ancestry forces white. This identifies the precise lost equation in fresh-state composition. No failed prediction in this block; no longer scan or solver run.

CL248 at 8b86c271 independently confirms GC1076, now PROVED, and computes the no-repeat consequence exhaustively. Its 59,392 high-LL returns have next tracks D or X only. The new hand inference strengthens its b=1 disjunction to Q=1; review requested. Next missing inference is transport of the forced 010 low successor together with its inherited high past, toward restrictions on renewal after an intervening D. All-depth composition and the prize remain open.


## GC1078 — A finite ordinary-low core closes at every renewal length (2026-10-11)

**Missing inference.** Carry GC1077's forced 010 successor through arbitrarily many low renewals without a fresh 111 origin. Record searched: 111001010|H.D.H|high.*low.*high with ancestry/inheritance/transport/shield ->14 hits in7 files; 010.*011.*100|11100101 with ordinary|L0 and closure/invariant/shield ->21 hits in10 files. The broader search was noisy and replaced by this narrower intersection. GC1053 gives the general closing map, GC1077 the first D renewal; neither supplies this invariant component.

**Hand theorem, proof sketch pending second reading.** Let C={010,011,100} denote origin sites 7..9 after ordinary-L prefix111001. Every such source has fifth track D=0101100000, returns L0 with triple in C or101, and has no other returned triple. If it returns101, the next long has high track H=0101101010 and returns S by GC1075. Thus, at every run length, successive L0 renewals stay in C until a possible single H-to-S escape. No high LL can occur after entering C while that consecutive long run continues. This is a sound finite hidden component; it is not a full hidden representation or an all-depth record bound.

**Origin and pair guard.** Initial sites6..9 are1010,1011 or1100. Each forces time1 sites6..8=101; the common prefixes at times2..5 are001,011,010,01. These steps use only GC1047's already proved first six ordinary-L fifth bits010110. Its mid01 selector therefore gives D and L0, without assuming the track used to derive the selector.

Write E,F at time4 sites9,10. The pair x,y at time5 sites8,9 is

    x=NOT E, y=E OR F, hence x OR y=1.

With z=time5site10 and B=x XOR(y OR z), GC1053's low update gives time6 sites6..9=110B. Writing K=time6site10, the next prefix is (1,0,NOT B,B OR K); time8 sites6..8=(1,B,1). Hence time9site8 Q=NOT B. If Q=0, B=1, so time7 sites6..9=1001 and time8 sites6..9=1111, whatever lies farther right. Thus time9site9 R=0 whenever Q=0.

The reviewed mid01 closing map returns sites7..9

    (NOT Q, Q OR R, Q XOR(R OR Z)), Z=time9site10.

For Q=0 the actual R=0 guard gives100 or101. For Q=1 it gives010 or011. These are precisely C or101; no claim that every abstract transition is realizable. Apply this same implication at each actual return: the prefix is again111001 and the new triple again lies in C, so induction proves closure for every number of consecutive low renewals. The101 escape uses GC1075's all-tail shield, not an independent next-return choice. In particular GC1077's b=1 high-LL branch enters C at010, after which a later high can only terminate that long run with S.

**Controls and unexpected check.** Predictions preceded execution. Six initial gates, eight one-step chain implications, four pair identities,96 guarded mid01 bands and32 free mid01 bands pass. Forty-eight selected actual origins pass independent literal and packed engines through both returns: returned011=18,010=13,100=11,101=6. The six101 cases all give H then S; the others give D then L0. The unexpected free time5 band010001000 returns111 under D, and eight of the32 free bands do so. Its x=y=0 violates the actual pair guard. This countercontrol identifies why projecting to the low fifth track alone loses closure. No failed prediction, language census, solver or relaxed-record run in this block; controls are evidence for the local identities, the induction is the all-length proof.

CL249 at11371755 independently confirms GC1077's hand ancestry and forced010/D renewal; GC1077 is PROVED. L612 at2dc9537d reports R_real(144)<=17 in both phases by kissat on verified cuts, with certificate checks queued; that computational scope is retained without replay. Next specific inference: carry the b=0 high-LL returned001, together with its inherited past, through its D continuation or X exit and test whether it can re-enter111. That branch remains outside C; the full relaxation and prize bound remain open.


## GC1079 — The inherited 001 branch really renews high after one low unit (2026-10-11)

**Missing inference and failed shortcut.** Does GC1078's finite core C={010,011,100} absorb every b=0 high-LL branch after its001-to-D continuation? No: the actual 21-bit origin111001111011111110010, with EVERY farther tail, produces consecutive ordinary-long fifth tracks H,D,H and returns triples001 at10 and111 at20. This refutes absorption into C and any ban on H-D-H. It does not refute an at-most-one-high-LL statement: the third high unit's return is a separate obligation.

Record searched:111001001|001.*high|high.*001 with inheritance/transport/renewal/shield/origin ->29 hits in9 files; the exact new origin or100011000001 with origin/shield/return ->no hit, including ledgers. No further solver, language or record scan.

**Finite all-tail hand certificate, second reading pending.** At origin sites6..21 the asserted prefix is1111011111110010. The following prefixes at sites6 onward give a complete causal shield certificate:

| Time | Prefix |
| --- | --- |
| 1 | 100001000000111 |
| 2 | 010011100001100 |
| 3 | 11111001001101 |
| 4 | 0000011111100 |
| 5 | 100011000001 |
| 6 | 110110100011 |
| 7 | 000100110110 |
| 8 | 00111110010 |
| 9 | 1110000111 |
| 10 | 1001001100 |
| 11 | 111111101 |
| 12 | 000000001 |
| 13 | 000000011 |
| 14 | 100000110 |
| 15 | 01000110 |
| 16 | 11101 |
| 17 | 10001 |
| 18 | 1101 |
| 19 | 1001 |
| 20 | 1111 |

Each next prefix follows by l XOR(c OR r). Every output has its three inputs displayed, or a displayed black OR input masks the missing right bit. Some prefix lengths are retained by that mask; no exterior is set to zero in the proof. GC1076's111 origin has time5 pair10 and hence H; the first five displayed steps use only GC1047's fixed first six ordinary-L fifth bits. The high fifth bits then supply times5..9. At10, prefix111001 is restored with triple001 and next sites10..12=001. Times10..14 again use only the fixed first six ordinary-L fifth bits. The time15 pair01 selects D, supplying the remaining low closing bits. At20 the returned triple is111, which selects H again by GC1076. Thus the boundary bits used in the certificate are justified at each selector, without circularly assuming a renewal.

The first long has marker b=time5site9=0 and returns001. At15 the actual next low band begins010001: its time15 sites8,9 are BOTH white. This is exactly the exceptional low-band mechanism excluded by GC1078's x OR y=1 guard on C, now realized on the other inherited high past. Its closing shield at16..20 forces returned111 for all farther bits. Retaining the fifth track and the fact of a preceding high unit still loses this distinction.

**Controls and unexpected check.** Predictions preceded execution. All40 one-step implications, including a fresh arbitrary right bit in each, pass;32 actual controls with four added initial bits and two far constants agree in literal and packed engines through30 ticks. They all have H,D,H, the predicted prefixes, and the exceptional actual mid01 band. The third H returns prefix111011 in these32 controls; this is evidence only, not an all-tail return theorem. The unexpected check therefore succeeds: GC1078's free-band111 successor can occur on an actual001 origin with inherited high past. Its C guard remains sound. The absorption shortcut is REFUTED; the new cylinder certificate is a proof sketch, with no failed certificate prediction.

CL250 atf9460bdd independently confirms GC1078's origin guard, closing step and101 escape; GC1078 is PROVED. Its induction is unchanged. Next specific missing inference: when inherited001-to-D returns111, does the following H necessarily terminate with S, or can it renew high LL? Carry that next-return condition on the same history; do not assign a fresh111 tail. Full hidden closure and the all-depth prize bound remain open.


## GC1080 — The 001 low-to-high return has an exact finite origin gate (2026-10-11)

**Missing inference.** Decide whether the high after an ordinary001 low renewal returns L0 or S, retaining its actual past. Record searched:001/111 or H-D-H with inheritance/third/repeat/marker/return and ordinary/high/renew ->50 hits in16 files;00100001|00110000|001011 with high/HLL/ordinary and gate/origin/inheritance ->5 hits in3 files (old31-template and GC1079, no exact gate). No language census or solver.

**Exact all-tail gate, PROVED (independent CL252).** Let initial sites7..9=001 after111001, and name sites10..19 a,b,c,d,e,f,g,h,i,j. The conjunction of D, returned111 at10, and following H returning L0 at20 holds exactly on the union:

- A: sites10..17=00100001; sites18,19 arbitrary.
- B: sites10..17=00110000 and i OR j=1.
- C: sites10..15=001011, g OR h=1, and either (g,h) is not11 or i=j=0.

Every such cylinder is an all-tail statement. No earlier-high premise is used in this first gate. Conditional on D returning111, the equivalent same-history gate is simply time3sites15=time3site16=0. Otherwise its following H returns S. This decides a next-return condition, not just the next fifth track.

**Hand derivation.** The001 origin forces time1 sites6..9=1111. Write A through I at time1 sites10..18. At time2 sites10..17 are

    p=NOT(A OR B), q=A XOR(B OR C), r=B XOR(C OR D),
    s=C XOR(D OR E), t=D XOR(E OR F),
    U=E XOR(F OR G), V=F XOR(G OR H), W=G XOR(H OR I).

D requires p=0. In its mid01 closing map, a returned111 requires time5sites8,9 both0, since GC1078's guarded map excludes111. For that white pair, with z=time5site10 and k=time5site11, direct updates give closing Q=z and, when z=0, R=k. Thus returned111 is equivalent to z=0,k=1. Translating these four conditions backward through the two zero-prefix updates gives p=q=r=s=0,t=1; time3sites6..14=000000011. The first four equations imply A=B=C=1 and D OR E=1. With t=1, either D=1,E=F=0 or D=0,E=1 (F free).

Let v,w be time3sites15,16. They are NOT(U OR V), U XOR(V OR W). From the forced black time3site14, updates give time5prefix01000110, time5site14 a'=v OR w, and time10sites6..12=(1,1,1,1,1,a',a'). If a'=1, the next high origin has sites10,11,12=111. Its time1 u=v=w=0 violates GC1077's necessary high-LL gate, so it returns S. If a'=0, the time5 fifteenth bit is1; its low closing OR shield also forces time10site13=0. The next origin therefore begins1110011111000. For an ordinary high origin111001111100d, name its next three initial bits e,f,g. Its time1 samples u,v,w are0,1,d; time2 gives M=NOT(d OR e), N=NOT d AND(e OR f OR g), hence M OR N=NOT d. GC1076/77's b=0 closing sample c=M OR N therefore gives the all-tail criterion d=0. Hence it returns L0 here. The next-return gate is v=w=0, equivalently U=1,V OR W=1.

Substituting time1 bits from the initial row completes the finite gate. A=B=C=1 forces a=b=0,c=1. The D=1,E=F=0 case plus U=1 gives A's00100001. The D=0,E=1 case plus U=1 gives either B's00110000 with i OR j=1, or C's001011. In C, G=0 means g OR h=1; H OR I=1 is automatic for01/10 and requires i=j=0 for11. These exhaust the Boolean cases, with no farther-tail assumption.

**Inherited-high restriction.** GC1077's earlier high b=0 branch has time5prefix100011. Naming its next two bits e',f', the returned001 origin has sites10=11=e' OR f'. If that pair is11, the next001 selector is X; D requires e'=f'=0 and the returned pair00. On this00 branch, two further shared samples M,N give returned sites12,13=(M,M OR N), so12<=13. Cases A and C above both require c=1,d=0 and are impossible with this inherited D past. Therefore an actual earlier high followed by001-D-111 can renew high LL only in B: the low origin must begin11100100100110000 and sites18 OR19 must be1. Conversely B gives that high LL whenever such an inherited origin exists. Excluding or realizing this exact remaining joint cylinder is the next obligation; it has not been assumed absent.

**Controls, correction and unexpected check.**48 qualified time1 bands,32 direct high-return decoder controls and128 inherited pair controls pass;32 pair00 cases give D and the inequality,96 others give X.56 selected actual001 origins give32 high LL and24 high S, matching the gate.64 selected earlier-high origins plus two known GC1079 controls pass literal/packed engines. The initial64 selection had no composed D-to111 case; the two explicit GC1079 controls supply nonvacuous composition, both S. An initial hand claim placed12<=13 on every b=0 return; its derivation uses the00 pair, so that unconditioned claim was withdrawn. The64 passing samples did not justify it. The published gate keeps the D premise.

The unexpected actual origin11100100100100001 gives D then high LL for every farther tail, while c=1,d=0 violates the inherited inequality. Thus the source001 alone does not force a high successor to terminate; its earlier high past must remain in the hidden representation. No unconditional low-to-high ban survives this control.

CL251 atab233880 independently confirms GC1079, now PROVED, and exhaustively confirms that its specific21-bit cylinder ends the third high with S. That cylinder conclusion does not exclude the remaining B origin on another inherited history. Next: its actual earlier-high preimage, using the exact pair guards above. Full hidden closure and the all-depth record bound remain open.


## GC1081 — The remaining inherited origin is actual: high LL can repeat after D (2026-10-11)

**Missing inference resolved; a shortcut refuted.** GC1080 leaves only B on an actual earlier-high past. The 24-bit source **111001111011111110011101**, with every farther tail, realizes B and has successive ordinary-long fifth tracks H,D,H, with both H units returning L0. Thus even an at-most-one-high-LL rule within a consecutive long run is false. This is an all-tail finite certificate, PROVED (independent CL253); it does not assert arbitrarily many repeats or an all-depth bound.

Record searched: 00110000|11100100100110000|high.*low.*high with inherited/preimage/origin/shield/gate ->29 hits in 11 files; exact source or 100011000001111 with origin/shield/return/repeat ->0 hits. Local's membership and relaxed-record lane was not duplicated.

**Exact inherited gate.** On the earlier high's time-5 band, suppose sites 6..13=10001100, and name sites 14..24 g,h,i,j,k,l,m,n,o,p,q. Its time-10 ordinary 001 origin is in B exactly when

    g=h=i=0, j=k=l=m=1,
    n OR o=1, and [(n,o)!=11 or p=q=0].

The returned sites 18,19 then equal 01. The premise retains the inherited pair 00 needed for D, rather than assigning a fresh low origin.

Here is the Boolean elimination. The required returned sites 12,13=11 first force g=h=0 and i OR j=1. The next returned pair 14,15=00 forces i=0,j=1: the alternative i=1 makes the two white conditions incompatible. Direct updates now give time-7 site 18 A=k AND(l OR m), and returned sites 16,17=(0,NOT A). Thus A=1, so k=1 and l OR m=1. Write

    L=l XOR(m OR n), M=m XOR(n OR o),
    N=n XOR(o OR p), O=o XOR(p OR q).

Under A=1, returned site 18 is 0. Returned site 19 is 1 precisely when L=M=0 and N OR O=1: time-7 sites 19,20 are L,L OR M; when both vanish, sites 21,22 are N,N OR O. Substituting these into the two remaining updates gives that equivalence. With l OR m=1, L=M=0 is equivalent to l=m=1,n OR o=1. If (n,o)=01 or 10 then N OR O=1 automatically; if 11, it requires p=q=0. This proves both directions of the exact gate without a cutoff extrapolation.

**Actual all-tail construction.** The source's prefixes at sites 6 onward are tabulated in `tests/probes/lexicon/rule30_inherited_high_repeat.py`. Each next prefix follows from l XOR(c OR r), with every right input either displayed or masked by a displayed black OR input. In particular:

- At 5: 100011000001111011; the pair 10 selects H by GC1047, and the joint gate above is satisfied with n,o=01.
- At 7: 00010011011010011; sites 7,8=00 give the first high LL by GC1047.
- At 10: 100100110000010; the restored ordinary origin begins 1110010010011000001, exactly B with sites 18,19=01.
- At 15: 010001100100; pair 01 selects D. Its return at 20 has prefix 1110011111000, so the next selector is H and its return is L0 by GC1080's high decoder.

The boundary bits used through 20 are justified at each selector: first six ordinary-L bits 010110, then H, then the fixed initial ordinary-L bits and D. The certificate stops at 20; it does not extrapolate its shrinking prefix through 30. The third return uses the independently confirmed all-tail decoder, whose criterion is initial site 13=0. Both high LL units therefore hold for every far tail.

**Controls and unexpected check.** Predictions preceded execution. 40 one-step implications with a fresh arbitrary right bit, 2,048 local Boolean-band controls (nine positives), and 64 selected actual histories pass; the actual histories agree in independent literal and packed engines. Changing only initial site 21 from 1 to 0 makes the source a GC1079 sibling: its first 21 bits are 111001111011111110010. That sibling has the same H,D,H fifth tracks but ends the third H in S, for every tail by CL251. The new source ends in L0. This single-bit countercontrol shows why the fifth-track sequence and an earlier high label alone do not decide the return. No failed control prediction; the at-most-one-high shortcut is REFUTED.

CL252 at ca6ee8c8 confirms GC1080's exact gate, high decoder and conditional inherited rule; GC1080 is PROVED. L613 at 6949a727 is ACKed with its kissat/verified-cut scope and pending certificates retained. Next specific inference: transport the post-repeat high origin 1110011111000 through its returned 001, retaining the joint tail gate above, to decide whether another D-to-high-LL renewal is possible. The sound low core C remains closed, while this branch genuinely lies outside it. Arbitrary repetition, the full hidden relaxation and the all-depth prize bound remain open.


## GC1082 — A second high LL carries a sparse guard into the closed low core (2026-10-11)

**Missing inference and result.** Can GC1081's repeated high LL renew high LL again through another low unit? No. An actual H-D-H with both high returns L0 puts a black bit at site 15 of the second high origin. That high's following 001 unit either exits the mature S/L0 scope through X, or begins 001000 and D enters the closed core C={010,011,100} or 101, whose H ends in S. Consequently **every consecutive ordinary-long run inside a mature S/L0 history has at most two high LL units, at every run length**. This is PROVED (independent CL254). It bounds a hidden return type, not R_real(d); changes of visible gap type remain outside this renewal argument.

Record searched: 1110011111000|0001111 with repeat/renew/inheritance/transport/origin ->17 hits in 7 files; canonical prefix,001000 or at-most-two with core/high/renew/guard/transport ->4 hits in 2 files. The existing record left the post-repeat branch open. No membership or relaxed-record run.

**Sparse inherited bit.** GC1080/81 show that an actual earlier high LL, D, then another high LL requires low origin B, with sites 18,19=01. Thus that low origin begins 1110010010011000001. Its finite prefix shield through time 8 ends with sites 6..15=1101111110; every one-step implication is displayed in the probe. Name z,w at time 8 sites 16,17. Then time 9 sites 13..16 are(0,0,NOT z,z OR w), so time 10 sites 14,15=(NOT z,1). Its high successor therefore begins 1110011111000 and has **site 15=1**, whatever the farther tail. The sparse bit lies beyond the contiguous thirteen-bit prefix retained in GC1081.

**The high carrier discharges into C.** For a high origin 1110011111000, let e=site 14,f=site 15. Its reviewed decoder gives H returning 001. If e=0,f=1, time 1 sites 12..14=001, which forces time 5 site 12=1; the returned 001's sites 10,11 are 11, selecting X. The reviewed mature LL table excludes X from a continuing S/L0 history.

If e=1 (either f), time 1 sites 6..14=100001011 and time 2 sites 6..14=010011010. Write D,E for time 2 sites 15,16. At time 3, sites 12..15=(0,1,NOT D,D OR E). Their complementary OR fixes time 4 sites 6..14=000001110. Writing N,O at time 4 sites 15,16, time 5 sites 6..13=10001100 and sites 14,15=(NOT N,N OR O). Their OR is 1. For a high time 5 band 10001100 with sites 14..17=g,h,i,j, direct updates give returned site 12=NOT(g OR h) AND(i OR j); hence it is 0 here. The returned low origin begins 111001001000.

For any ordinary 001000 origin, time 1 sites 6..11=111110. With C,D at time 1 sites 12,13, time 2 sites 6..12=00000 followed by NOT C,C OR D. Direct transport gives time 5 sites 6..9=(0,1,NOT C,1). Its low closing pair therefore has x OR y=1. GC1078's reviewed guarded mid01 map gives returned C or 101; the latter's next H ends S. This entrance uses the same actual history, without assigning a fresh tail at the low return.

**All-length deduction.** Start at the first high LL in a continuing mature ordinary-long run. GC1077 returns 010 or 001. The 010 branch enters C immediately. The 001 branch next selects D (X would leave scope); the reviewed D closing map can return only C,101 or 111: its sole extra formal value 110 is excluded by GC1053. C is closed, 101 terminates with H-to-S, and 111 selects the only possible second high. If that high returns S the run ends. If it returns L0, the sparse guard above applies and forces X exit or two D units into C/101. No later high LL is possible. The deduction covers every number of intervening low renewals; it is not a finite cutoff census.

**Controls and unexpected check.** Predictions preceded execution. 16 prefix implications, 4 two-tick OR controls, 32 actual B histories, 96 canonical high histories and 128 histories of ordinary 001000 pass; actual histories agree in literal and packed engines. The unexpected 25-bit source **1110011111000000001000001** has canonical prefix but sites 14,15=00, and really gives H-D-H with both H returning L0 for every tail. Its finite shield agrees with GC1081 from time 3 onward; 40 fresh-right implications and 32 actual controls pass. Thus banning another renewal from the thirteen-bit canonical prefix alone is false: the inherited sparse fifteenth bit is essential. No failed control prediction.

CL253 at b9c879f0 independently confirms GC1081's actual source, exact joint gate and one-bit sibling; GC1081 is PROVED. Next concrete inference: determine which low origin triples a mature S-to-L return creates, and carry their inherited D past into C or this two-high carrier. That decides how the finite high counter resets across mixed S/L strings. The complete hidden relaxation and all-depth prize bound remain open.


## GC1083 — A core escape carries a sparse guard across the short return (2026-10-11)

**Missing inference.** Extend GC1082's finite high counter across S, retaining the actual low-core past of a 101 escape. Record searched: 111001101 with 111010001|mixed|next short -> 3 hits in 2 files; GC1052/1075 leave this bridge. CL254 at 205a1856 independently confirms GC1082, now PROVED. No solver, membership or record computation was duplicated.

**New joint guard, PROVED (CL255/255.1; its core-A premise is barred in GC1084).** If an ordinary L0 origin in C={010,011,100} returns 101 and that high unit returns short origin A=111010001, then the 101 origin begins **11100110111011**. In particular its site 14 is black. The next S origin has **1110100011a1**, with a free site 11 and a black site 12. That S necessarily returns the exceptional ordinary low triple **001**, rather than entering C immediately. This is a conditional implication on one actual history; existence of its complete C-origin preimage remains open. It neither refutes mixed-core closure nor proves a mixed counter bound.

**Hand transport.** For an arbitrary 101 origin, its S return is A exactly when time-4 sites 9..12=0011 and sites 13 OR 14=1. Propagating backward through the GC1075 shield, the first condition alone requires initial sites 10..14=11100 or 1101*. This first gate does not retain a core past.

A C origin whose D returns 101 has time-8 prefix 1111 at sites 6..9, by GC1078. Name time-8 sites 10..16 a,b,c,d,e,f,g. The 101 return forces a=b=0. Its returned site 10 is 1; site 11 is NOT(c OR d). The A gate requires this eleventh bit to be 1, hence c=d=0. Returned sites 12,13 then equal e,e OR f. Returned site 14 is e XOR((e OR f) OR(e XOR(f OR g))); the earlier unconditional e XOR(f OR g) formula was wrong (CL255.1). When e=0, as required by the surviving A option, it is f OR g. The 11100 option is impossible since site 12<=site 13; the 1101* option forces e=0,f=1, and therefore site 14=1. Thus the required time-8 packet is 1111000001 at sites 6..15, and two updates give the stated 101 prefix.

From that prefix, high-unit prefixes at sites 6 onward are 100100010, 01111011, 11000010 at times 1..3. With D,E at time-3 sites 14,15, time 4 is 0010011 followed by NOT D,D OR E. Their OR forces time-5 prefix 11111100. The next prefixes are 1000001,0100011,1110110 at times 6..8. With a,b at time-8 sites 13,14, time 9 is 000010 followed by NOT a,a OR b, and time 10 is 00011a1. This gives the S prefix with black site 12, independently of every farther bit. For any S origin 1110100011bc, direct updates give time-4 site 10=b OR c. GC1054's returned triple (0,NOT C,C OR E) is therefore 001 when c=1. No tail is replaced at a return.

**Controls and retained failures.** 26 one-step implications with fresh exterior bits, 64 core-closing bands (32 return 101, two joint packets), 1,024 inherited-packet controls, 128 high-packet histories, 256 short-gate controls and 2,048 unrestricted 101 cones pass; literal and packed engines agree. The unrestricted cones have 192 A returns. The unexpected returned A-site10 was initially misindexed as white; it is black. A first 19-cell cone could not read that tenth cell at time 10; the 20-cell control fixes the range. Three informed core constructions (010 with zeros,100/011 with period110) failed to produce the proposed immediate bridge: each stays in C at 10, and the two that reach 101 at 20 have site11=0. These failures establish no absence result.

The unrestricted 25-bit cylinder **1110011011101000000000000** does give H-to-S(A)-to-L001 for every tail, by its finite causal cone (64 independent controls pass). Its 101-site14=0 violates the new core guard, so it supplies no counterexample with a C past. The sparse bit is essential to representing that past. Next specific inference: intersect the forced S prefix 1110100011a1 with GC1080's three low-to-high-LL gates on the same history, rather than assigning a fresh low001 tail. The full mixed relaxation and all-depth prize bound remain open.


## GC1084 — A core escape cannot return the dangerous short origin A (2026-10-11)

**Missing inference and result, PROVED (CL256, structural no-A statement).** CL255 at afcc8d34 reports a finite all-tail absence: no C-to101 escape returns S-A. Its formula correction CL255.1 at 5625c5a5 is ACKed and applied above. The new hand proof identifies the obstruction: **a core escape's 101 origin with site 11=1 must have sites 12,13=11**. GC1083's A antecedent needs sites 10..14=11100 or1101*, both incompatible. If that returned S next takes L0, it must be **B=111010011**, by the reviewed mature SL-origin table. The unconditional B conclusion originally written here did not follow from that table: SS images need separate exclusion (GC1085). The no-A bridge holds for every far tail, independently of any cutoff.

Record searched: 1110100011|111010001 with00110000|00100001|001011|high.LL ->9 hits in5 files; the initial target was the forced short's B-image gate. After CL255 ruled out its core-A past, that work was parked and the direct core obstruction took priority. No solver, membership or record run.

**Two exhaustive packets on one history.** A core D has fixed prefixes101,001,011,010 at times1..4 (GC1078). Write time-5 sites8..13 as x,y,z,u,v,w. At time6, site9 is B=x XOR(y OR z), and sites10..12 are C=y XOR(z OR u),D=z XOR(u OR v),E=u XOR(v OR w). The 101 return gives B=1 and time8sites10,11=00. A black eleventh returned bit adds time8sites12,13=00. The four white conditions imply time7sites10..12=111; hence C=D=0,E=1.

Let time4sites9..14 be p,q,r,s,t,j. Its actual010 prefix gives x=NOT p,y=p OR q,z=p XOR(q OR r),u=q XOR(r OR s),v=r XOR(s OR t),w=s XOR(t OR j). Eliminating B=1,C=D=0,E=1 leaves exactly two cases: time4sites9..14=**000001**, or sites9..13=**10001**. This is a Boolean case split, with no independently assigned returned tail.

In the first case, direct updates force time6sites6..14=110100110. Time7sites13,14=(0,NOT H), where H is time6site15. The already-required white time8site13 forces H=0. Time8site14 is then1, giving returned sites12,13=11.

In the second case, the time4 packet10001 and time3prefix011 force time3sites9..14=000001. Using time2prefix001, that zero chain requires time2sites9..12=1111. Its next pair has OR1 and the following XOR is1. Using time1prefix101, these requirements force time1sites9..15=**0010001**. Two updates give time3sites9..15=**0000010**, including the extra white fifteenth bit. Let H,I be time3sites16,17. Then time4sites14..16=(1,NOT H,H OR I), whose last pair has OR1. Thus time5sites14,15=00, time6site14=1, time7sites13,14=01, and time8site14=1. The sparse bit comes from that complementary pair; a contiguous-prefix calculation loses it.

**Controls, failures and unexpected check.** Predictions preceded each control.1,024 independent time4 split controls (42 qualified),512 backward-chain controls,16 first-packet controls,64 complementary-pair controls and384 selected actual core cones pass; literal and packed engines agree. These check the local hand implications, rather than replacing them with a finite absence scan. The selected actual escapes return101 prefix11100110111110 and S-B. A reversed core100 construction11100110011111100 failed to put the black time8 bit at15: it is at14, and the source returns B. This unexpected check exposed the packet obstruction. A naive contiguous shield and a proposed nine-cell packet also failed; the proof retains the seven-cell packet plus its complementary pair.

The parked short-B attempt had false predictions: the white short marker was claimed unable to produce B, and a proposed19-bit preimage missed a branch. The actual short cylinder11101000110110111000001 gives B and a following high LL, but cannot have the just-barred C-to101-toA past. Such a positive short source does not reopen the core bridge. Next specific inference: can a mature B short return A through SS, allowing a later A-toL001 reset? Carry its same short history; the full mixed carrier and all-depth prize bound remain open.


## GC1085 — The B label can restart A; retain the inherited core past (2026-10-11)

**Missing inference and correction.** GC1052 already proves B=111010011 always returns L0, so GC1084's proposed B-toSS target was vacuous. GC1056 classifies mature **SL** sources as A/B; it does not classify every mature S image. GC1084's unconditional B conclusion is narrowed above to the next-SL case. Its structural no-A proof remains unchanged. Record searched: 1110011011|111010011 with return.*B|SS|short.*short|core ->23 hits in8 files; GC1052/1056/1074/1083 read.

**Concrete all-tail obstruction, PROVED (CL257).** The short cylinder **11101001100111010000** returns **11100110111011** at time6. Its retained prefixes at times1..5 are1000111101110001100,010110000100101101,11010100111110100,0001011110000011,001101000100011. Each is the exact Rule30 update of the previous retained prefix with wall input t mod2; arbitrary farther cells cannot affect them. GC1083's reviewed high shield then forces **1110100011a1** at16 and **111001001** at22. Thus B can restart A and the exceptional low001, even though B cannot take SS. No C-origin preimage of this entire history is claimed.

**Predictions and failures.** P1, that B-to101 ancestry bars the A antecedent, failed:30 of512 complete short cones have high sites10..14=11011. P2, that the reported core-like high packets force the following B sites10 OR11=1, also failed:1011000* and10111110 admit the white pair (32/256 and64/128 cones). Fresh high packets do not retain a core past. Stop these B-label shortcuts; no larger prefix sweep. The unexpected all-white GC1074 selector remains high. Six exact prefix implications and64 selected composed controls pass independent literal/packed engines. Their all-tail conclusion comes from the causal prefix chain and GC1083, not a sampled core absence.

**Next specific obligation.** Retain actual C ancestry across the returned B and its next101: exclude the dangerous A antecedent there, or produce its actual C preimage. The B label alone is insufficient. No solver, CUT, membership or record computation was duplicated; the full mixed carrier and all-depth prize bound remain open.

**GC1085 publication receipt.** CL256 at adc9e46d independently confirms GC1084's two-case hand proof and named cylinders; the structural no-A bridge is promoted. The S-B extension there remains sampled; GC1085 retains the separate SL qualification. No repeat audit or computation.


## GC1086 — A core guard survives one B bridge (2026-10-11)

**Missing inference, PROVED (CL258).** Carry actual core ancestry through B, whose label alone admits A reset (GC1085). For the core escape with a black eleventh high-origin bit, GC1084 forces **11100110111110**. Its S image is B with site10=0 and **site11=0 implies site12=0**. Conversely, **B-to101-toA requires B-site12=1**. These hand implications bar the immediate B-to101-toA restart in this actual core branch. They do not close arbitrary mixed lengths or the core escape with a white eleventh bit. Record searched: 11100110111110|11101001100111010000 with reset|guard|ancestr|prefix|core ->5 hits in3 files; GC1084/1085 read. CL257 at636eda33 confirms GC1085, promoted above.

**Long image proof.** Reuse GC1075's actual high fifth track H=0101101010. The forced origin gives time2 sites10..12=100, time3 sites10,11=01 and time4 sites6..10=00101. The black time3 site11 forces time4 site11=1, extending the packet to **001011**. Time5 sites6..11=111010. With u,v at time5 sites12,13, time6 sites11,12=(NOT u,u OR v), whose OR is1. Thus time7 sites6..11=**010110**, including a white eleventh bit. Let K,L be time7 sites12,13. Time8 sites11,12=(NOT K,K OR L); time9 sites10,11=(K,1). The S return at10 therefore has sites6..11=00110(NOT K). When K=1, time9 site12=1, so returned site12=0. This proves both the B image and the inherited implication without replacing its tail.

**Short implication and composition.** GC1052 permits B-to101 only when B sites10,11=00. Under that condition, write f,g,h,i at12..15. GC1074 gives high selector G=(f OR g) OR NOT(h OR i). For f=0,G=1 there are two cases: g=1 gives time2 sites11..13=010; g=0 forces h=i=0 and gives100. Both have time3 sites11,12=01, hence time4 site12=1. The next high-origin site11 is NOT(R OR S), R,S being short time4 sites12,13, and is therefore0. GC1083's A antecedent needs that eleventh bit black. Thus A requires f=1. On the inherited B above, a black site11 puts the next long origin in C; a white site11 gives f=0, and the next long is either C or101 whose S return cannot be A. This is one same-history composition, not an absorbing invariant for all future returns.

**Controls and limits.** P1's stronger pair-zero prediction held on1,024 cones, but only site12 is proved here. P2's proposed packet closure failed: generic1011000 can give B-site13=1 with white10,11 (nine cones), and B000000 can return1011001 (three cones). Stop that closure. P3/P4's sparse implications pass256 high histories,64 free closing packets and32 short cones, with literal/packed agreement. The unexpected initial black pair12,13 becomes the relevant white B-site12; its farther image cannot be assigned independently. Next specific gap: derive the white-eleventh core escape's actual high packet, retaining its core prehistory. No solver, CUT, membership or record run; the all-depth bound remains open.


## GC1087 — The low core is absorbing through all mixed renewals (2026-10-11)

**Result, PROVED (CL259).** The missing white-eleventh escape closes in the synchronized phase-zero renewal frame. The following concrete three-type union is forward invariant for every farther tail and every renewal length:

| Type | Actual origin prefix or guard | Next type |
| --- | --- | --- |
| C | Ordinary L0, sites7..9 in {010,011,100} | C or J |
| J | Ordinary L0, prefix111001101100 or11100110111110 | guarded B |
| guarded B | S prefix111010011, site10=0, and site11=0 implies site12=0 | C or J |

Thus after entering C, every later short is B, every next long lies in C or J, and **no SS or high LL occurs at any later renewal**. Exceptional long001/111 and S-A never restart. This is a same-history invariant, not a finite scan; it does not bound R_real(d). Record searched: 1110011011000|111100010|white.eleventh core ->3 hits in3 files; GC1085/1086 read. CL258 at60d0b2ba confirms GC1086, promoted. L614 atca4508b5 is received (141>=18 witness;142 undecided), with no run requested.

**The new core entrance proof.** Reuse GC1078's C-toC/101 and GC1084's black-eleventh escape packet. On a core101 escape, time6 sites6..9=1101. Write C,D,E,J for sites10..13. The required white time8sites10,11 force C=D=0 and E OR J=1: if F=NOT(C OR D), G=C XOR(D OR E), K=D XOR(E OR J), then those white bits give F OR G=1 and F=G OR K, hence F=1. For E=0, J=1; time8sites12,13=10, and closing gives high10..13=1000, within J.

For E=1, GC1084's time4 split is000001 at9..14 or10001 at9..13. Its second packet already forces time7sites13,14=01, hence white time8site13 and a black eleventh returned bit. For the first, actual time2prefix001 is the missing information. Write a..g at time3sites9..15. The time4zero chain forces a=b=c=d=1. Its final1 allows e,f,g=100 or01*. Write x,y,z,u,v,w,t at time2sites9..15. The four black a..d force x=y=u=v=0,z=1, giving e=w and f=w OR t. Thus e<=f and the100 option is impossible. The remaining option forces time2sites9..15=0010001, hence g=1 and time3sites9..15=**1111011**. Time4site15 is therefore0. With l,m at time4sites16,17, time5sites15,16=(NOT l,l OR m); their OR is1, forcing time6site15=0. Time7sites13,14 are again01. Thus E=1 always has a black eleventh returned bit and reaches GC1084's high11110 packet. This proves C-toJ on both branches.

**Mixed closure, without widening the tail independently.** The broader high100 prefix already reaches time4sites6..11=**001011**: time1sites10,11=01, then time2 and time3 have that same pair, forcing time4sites10,11=11. The rest of the packet is GC1075's common shield. Both J prefixes therefore satisfy GC1086's reviewed time4-to-B sparse guard. For guarded B, a black site11 puts the next long in C by GC1052. If site11 is white, site12=f is white. GC1074 gives either low100 in C or high101. In the high case GC1086's short proof gives time4site12=1, so time5sites10..12=111 and returned high10..12=100. The latter lies in the broader J prefix, including site13=1. The table now closes, and induction applies at every subsequent renewal.

**Controls and remaining gap.** Predictions preceded the local controls:1,024 backward packets (eight qualified),four complementary-pair cases,16 white-E closures,32 high shields and64 short cones (40 high outputs) pass; full high/short cones agree literal/packed. Four unexpected counterfeit time4packets with black15 return101 with white11 and black12, outside J: they lack the just-proved core past. The previous B13-black exception and high1001 successor remain allowed, so the failed two-packet closure is not reinstated. Next concrete admission gap: the unguarded B-to101-toA-to001 bridge's D return on the same history. This invariant covers an entered component, while upstream admission and the all-depth record certificate remain open. No CUT, membership or solver run duplicated.


## GC1088 — The unguarded B reset can return 111 and reach SS (2026-10-11)

**Missing inference and result, PROVED (CL261).** GC1087 closes the entered low core, but does GC1085's actual B-to101-toA-to001 bridge enter it at its next D return? Not necessarily. The finite origin **11101001100111010000 followed by 24 white cells**, with every farther tail, returns high111 at32, S at42 and S again at48. It gives concrete evasion of immediate admission and crosses back into SS. It does not refute eventual admission or prove arbitrarily many such resets.

Record searched: B.to101.toA|11101001100111010000|unguarded B ->10 hits in6 files; GC1080/82/83/85/87 read. Predictions preceded the controls. The initial claim that A1a1 forces001000 failed; its low outputs include001011,001010 and001001. A proposed D-image inequality12<=13 failed in38/256 and64/256 local cones for the two marker choices. Actual high11011 past with A11=1 does force A13=1, but adding that bit still leaves24/128 violations. These label-only admission shortcuts are stopped. The white-tail diagnostic then returned111 at32 rather than C; the following certificate promotes that particular trajectory to an all-tail cylinder.

**Causal certificate.** Starting from the 44 fixed bits, retain each completely determined spatial prefix under Rule30. An output before the last known cell has all three inputs displayed. If the last known cell is black, its OR masks the unknown next input and one additional output is determined. This is an exact induction over arbitrary exterior bits, not an assumption of a white infinite tail. The source retains24 fixed cells at32,20 at42 and17 at48; the probe checks both fresh exterior choices at every step. Selected checkpoints are:

| Time | Forced origin prefix |
| --- | --- |
| 6 | 11100110111011 |
| 16 | 1110100011111 |
| 22 | 111001001001011 |
| 32 | 111001111111 |
| 42 | 11101110101000010111 |
| 48 | 11101111000111011 |

The actual fifth tracks are D=0101100000 on22..31, H=0101101010 on32..41, and SS=111010 on42..47. Thus the D return is outside C/J, its next high terminates in S, and that S takes SS. These are samples of the same forced rows, with no freely assigned tail at a renewal. The unexpected SS image still has a **black sixth marker**: the initial prediction of immediate whitening at48 failed. GC1056's monotone white-marker absorption does not imply instant whitening.

All96 fresh-right prefix implications and32 independent literal/packed composed controls pass. The local failed inequalities have explicit retained witnesses. No solver, CUT, membership or relaxed-record computation was run. CL259 at e58f3e27 independently confirms all three GC1087 transitions and the induction, so GC1087 is promoted to PROVED; L615 at86391577 is ACKed with its138>=18 witness scope, and CUT-P23's142 run is left to Local. Next missing inference is admission after this actual black-marker SS segment, retaining the high-to-S past. The finite relaxation must carry that segment; neither this cylinder nor the absorbing component yet gives an all-depth record bound.


Independent review CL261 at c79ab298 confirms the stated all-tail result; promoted to PROVED.


## GC1089 — The last black SS marker can force A and another 001 reset (2026-10-11)

**Missing inference and result, PROVED (CL262).** Does whitening after a black-marker SS segment force core admission? No. A mature black S has sites6..9 in {1101,1110,1111}. Its SS image is S-A exactly when the origin begins **111011111** and sites10..14 are **11100 or1101***. That A image has **site10=site12=1**, so its next SL returns ordinary low001 by GC1083's reviewed gate. This exact dangerous-reset selector explains an upstream obstruction; it neither asserts recurrent resets nor a record bound.

Record searched: black.*short|black.*marker|sixth.marker with001|111010001|core|admission ->22 hits in11 files; GC1054/55/56 read. ASF's established future forcing is reused without another all-S run. The initial no-A10-black prediction failed in12/384 complete local cones, all on1111. The corrected selector was derived before its controls. A separate prediction that GC1088's fixed44-bit source reaches this selector by54 or60 also failed: its forced prefixes are111011110001101 and1110111100011. Do not extend that cylinder or scan successors.

**Hand necessity.** GC1056 gives the returned sixth marker. Initial1101 retains a black marker, excluding A. Initial1110 can whiten only with initial site10=1; its time1sites6..10=00001, which gives returned site7=1, again excluding A. For initial1111, time1sites6..9=0000. Name time1sites10..15 A,B,C,D,E,F. Direct SS transport gives returned site7=A. Under A=0, write Z,K for time5sites9,10. Then

    Z = NOT B XOR(B OR C OR D).

An A image requires Z=0 and K=1. The former gives B=0 and C OR D=1. With B=0, K=NOT C AND(D OR R), where R=time4site11. Therefore K=1 forces C=0, hence D=1. Thus the target requires time1sites10..13=0001. Conversely that packet gives the target by the shield below. If initial sites10..14 are e,f,g,h,i, the four equations are

    NOT(e OR f)=0, e XOR(f OR g)=0,
    f XOR(g OR h)=0, g XOR(h OR i)=1.

They force e=1. For g=1, h=i=0 and f=1, giving11100. For g=0, f=h=1 and i is free, giving1101*. These exhaust both directions of the origin selector.

**Same-history image shield.** Time1sites6..13=00000001 forces the successive prefixes at sites6 onward:

    time2: 10000011; time3: 01000110; time4: 1110110.

With u,v at time4sites13,14, time5sites6..13 are000010 followed by(NOT u,u OR v). The closing time6sites6..12 are **00011u1**. Hence the white S image is A with10=12=1, regardless of all farther cells. Its next short fifth track is111000, and GC1083's A gate has time4site10=A11 OR A12=1; the following long triple is001. No tail is selected independently at either return. This supports both actual finite cylinders11101111111100 and1110111111101 through SS then SL001.

**Controls and limits.** All1,536 complete literal/packed six-tick cones agree (48 A images),256 scalar backward bands satisfy the iff, fresh-right shield implications pass, and64 composed controls verify both cylinders through12. The unexpected white A source1110100010000100 returns010 in C: the A-to001 claim requires the proved black-SS image packet. Next missing inference is the actual low001 return's high gate with this black-SS past retained, rather than a free A label. Eventual admission and the all-depth bound remain open; no solver, CUT, membership or record computation.

L616's137 witness and CUT-P24 are received without duplication. IN002's strategy proposal is received; its preamble leaves assessment to Cloud and makes no lane change, so the owner-prioritized RRL structural block continues. The merged chat had an empty duplicate L616 heading and an older timestamp on its body; the empty heading is removed and the intended02:07 correction from3b74ce15 restored on that body. The over-limit map is compressed to its index role without changing the research claims.


Independent review CL262 at c79ab298 confirms the stated all-tail result; promoted to PROVED.


## GC1090 — The white-eleventh black-SS reset enters the absorbing core (2026-10-11)

**Missing inference and result, PROVED (CL266).** Retain GC1089's black-SS past across A-to001. Its A image has **site13=site11**, in addition to10=12=1. Every such A returns001 with **site10=0**, so the ensuing long always has D and renews L0. If A11 is white, the low return begins **11100100101**, whose D return enters **C={010,011}** for every farther tail. From there GC1087's proved union is absorbing at every subsequent renewal length. Thus this whole white-eleventh branch admits the core after22 ticks from the black SS origin. The black-eleventh branch remains open.

Record searched: black.SS|111011111|last black with001|gate|past|inherited ->25 hits in9 files; GC1080/89 read. Predictions preceded controls; failed generic A pair inequalities were not resumed. The new sparse bit comes from actual SS prehistory, not a selected A tail.

**Inherited A bit.** GC1089 gives time3sites6..13=01000110. With X,Y at14,15 there, time4sites13,14 are(NOT X,X OR Y). Write u=time4site13, which equals returned A11. For u=0, X=1 forces time4site14=1; time5sites12..14=111, so returned A13=0. For u=1, time5sites12,13=01, so returned A13=1. Therefore A13=A11 on both actual branches.

**All A resets here take D.** For an A packet with10=12=1, write u=A11. Its time1sites6..12=101100(NOT u); time2sites6..12=00101 followed by(NOT u,NOT u OR W). Time3sites10..12 are(1,u AND NOT W,u AND(W OR V)); their last-pair OR is u. Hence time4sites6..11=10001(NOT u), time5sites6..10=11011, and the low return's sites6..10=**10010**. The restored full origin is1110010010. At that low origin, name its next bits b,c. Its time1sites10,11=(NOT b,b OR c), whose OR is1; time2site10 is white. The successive prefixes at6 onward are then00000,0000,100,01, so the ordinary mid01 selector gives D and L0. This bars X on the entire reset family.

**White branch admission.** For u=0, actual A13=0 gives A sites6..13=00011010. With E,F at14,15, the time1sites12..14 pair is(1,NOT E,E OR F), forcing time2site13=0. Time2sites6..13=00101110. The next complementary pair forces time4site13=1. Direct closing gives low sites6..11=100101, hence full origin11100100101. Its causal prefix shield through10 updates is listed in the probe; its final forced prefix is **11100101**, already restricting the returned triple to010/011. Every implication checks both fresh right inputs. This proves entrance into C without a finite absence scan or a farther-tail assignment.

**Controls and failures.**128 ancestry packets,256 generic A short packets,128 white packets,20 fresh-right low-shield implications and64 independent literal/packed composed controls pass;22 composed rows use the admitted branch. An initial prediction of a100/101 return used the wrong fifth-track phase and failed;256 complete controls instead give010, but only the sufficient010/011 shield is proved here. The unexpected fresh A with white11 and black13,11101000110110100010 followed by whites, gives111 after its D. It violates the actual A13=A11 guard. The first diagnostic mis-concatenated that retained tuple into17 bits and returned C; both strings remain in the probe, and its initial thirteenth-bit assertion was corrected accordingly.

CL260 at60a23bb4 is ACKed: its strategy assessment offers GPT the check-free hand target and permits choosing the handoff moment. Finish the remaining black-eleventh reset packet first; then reassess that target after Cloud's forced-only definition replication. L616 is ACKed; the stray header mentioned by CL260 was already repaired in GC1089. No Local computation, CUT, membership or record run. Upstream black-eleventh admission and the all-depth prize bound remain open.


CL266 at632485b2 independently confirms the shield and all-tail result; promoted to PROVED.

## GC1091 — A black-SS reset can renew high LL before exiting through X (2026-10-11)

**Missing inference and result, PROVED (CL267).** GC1090's white-eleventh branch enters the absorbing core. Its black-eleventh branch instead has low prefix **11100100100**, but can still renew111 and high LL. The actual fixed30-cell origin **111011111111000000100011110111** forces SS, SL, D, H, X through42 ticks for every farther tail: high LL occurs22..32; the following ordinary long selects X and exits the mature S/L0 component. This is one all-tail transient family, not universal black-branch admission or a record bound.

Record searched: black.SS|black.eleventh|00011111 with001|gate|past|admission ->37 hits in19 files; GC1080/1088/1090 read. Predictions preceded controls. The no111 D-return prediction fails on this actual source;61 of512 selected composed histories also fail, evidence only. No larger source census or extension of GC1088's failed cylinder was used.

**Black A shield.** Actual A6..13=00011111. Name its time1sites14,15 q,r and time2site15 s. Successive short prefixes at sites6 onward are10110000;0010100;111011;100010;11011;100100. In the fourth row, sites12,13 are a=NOT(q OR r), h=NOT q AND(r OR s). Thus a OR h=NOT q. Time5sites11,12 are(q OR r,NOT q), whose OR is1, forcing returned low11=0; low10 is already white by GC1090. This proves the packet for arbitrary farther cells. It does not assert that A13=1 is necessary: the unexpected fresh source1110100011110 with white exterior also has this low packet, refuting that control prediction.

**Same-history certificate.** Exact known-prefix propagation uses all three displayed inputs, or masks the unknown right input when the last known middle cell is black. The30 fixed initial cells force:

| Time | Determined prefix |
| --- | --- |
| 6 | 1110100011111111010010000010 |
| 12 | 1110010010010000100101100 |
| 22 | 111001111100001101001 |
| 32 | 1110010011101000 |
| 42 | 111000101 |

At12, sites10..17=00100001 are GC1080's reviewed family A, so D returns111 at22 and H returns L0 at32. This high LL is actual, with no independently reset tail. At32 sites10,11=11; time33sites10,11=00 and time34site10=1. The reviewed ordinary selector therefore takes X=0101100101 on32..41, rather than D. Its exit and all displayed prefixes are shielded against every farther tail.

All256 scalar short packets,8 Boolean identities,84 fresh-right prefix implications and64 independent literal/packed histories pass. The failed universal admission prediction and failed necessity countercontrol remain explicit. No solver, CUT, membership or record computation.

CL263/CL264 at0db2fc8c are received: the forced-only definition now replicates independently in both phases; sampled deep bounds retain their third-party qualification pending witnesses. L617's flag atbe538948 is verified and ACKed. The remaining black branch is not closed by this transient cylinder. After these failed automatic-admission shortcuts, next assess the offered check-free hand target from its proved periodic case, as CL260 permits; retain the RRL absorbing component and upstream past constraints, without further fixed-source extension scans. No Local task or time-critical Cloud dependency.

CL267 at632485b2 independently confirms the shield and all-tail result; promoted to PROVED.


## GC1092 — An odd-period successor over a forced-white parity interval is nilpotent (2026-10-11)

**Missing inference.** The check-free route needs a bridge from white forced cells, with checks ignored, to the periodic-stretch mechanisms. The available D2 proof summary excludes a fully white tail by Jen; that alone does not exclude a white forced tail. The stronger reported eventually-periodic forced-only theorem needs its separate argument. This is a scope question for review, not a refutation of its X4 version.

Record searched: forced.only|check.free withperiodic|Jen ->6 hits in3 files; odd.periodic|odd.spatial.period|odd.period withcheckerboard|alternating.white|white.*parity ->4 hits in2 files, no bridge theorem. STRATEGY-PLAN D2 and RULE30-PRIZE8.88 read. Predictions preceded all controls; no periodic search or record computation duplicated.

**Finite bridge, PROVED (CL268).** Let y=F(x) under ordinary Rule30, with either parity of x white throughout[a-2,b+2]. Suppose y is q-periodic on[a-1,b+1], for positive odd q, and b-a>=q+4. Then

    F^4(x)_i = 0 for every i in[a+2,b-q-2].

For a centre i on the white parent parity, the local image has y_(i-1)=x_(i-1), y_i=x_(i-1) XOR x_(i+1), y_(i+1)=x_(i+1). Hence y_i=y_(i-1) XOR y_(i+1). On the other parity, translate this relation by q; the periodicity premise supplies all three equalities. Thus the relation holds for every i in[a,b-q]. It determines one of the four linear period3 patterns000,011,101,110 on[a-1,b-q+1]. Each nonzero pattern maps to a single-black period3 pattern, then111, then000. Three more updates therefore kill every radius3 cone inside that interval, proving the displayed bound. This holds for every positive odd q and arbitrary exterior bits. On a left half-line the same argument gives an eventually white row after four ticks.

**The parity matters.** The even-q counterexample x=...1010... is fixed by Rule30, has a white parity and a period2 successor, and never dies. The finite lemma therefore supplies an actual restriction on periodic ancestry, with loss q+4; it does not provide the missing assertion that a survivor must encounter such an odd-period successor interval.

**Exact periodic controls and the reported scope.** The periodic inverse-column rule is c(t)=a(t+1) XOR(a(t) OR b(t)), with a the current left column and b its right neighbour. Named pure visible01 and10 give exact seven-column cycles in both wall phases. Their initial depth projections are respectively1000000/0110010 in the standard phase and1011111/1100001 in the other. Because7 is odd, both forced parities sample every cycle position infinitely often; each named sequence has black forced cells indefinitely. This is a concrete periodic case, independently checked by triangular time reconstruction, not a general periodic theorem.

Conversely, standard visible1 gives depth projection01 followed by the repeating01 tail; other-phase visible0 gives1 followed by01. Their forced tails are white while their check tails contain blacks. They violate11 and00000 respectively, so neither refutes X4. They do show precisely why Jen's full-white-tail exclusion cannot alone prove the stronger statement quoted in8.88. Please supply the separate forced-only periodic bridge or qualify that assertion pending it; keep the within-X4 conjecture unchanged.

Controls pass:4 local parity identities, all4 nilpotent period3 patterns,352 finite odd-q fixtures with arbitrary exterior (288 others correctly fail the periodicity premise), the fixed even-q counterexample, and6 exact periodic-column controls independently reconstructed through128 depths. No failed prediction. No solver, CUT, membership, relaxed-record or broad period search. CL266/267 confirm GC1090/1091 and both are promoted. L618's flag is verified and ACKed. Next missing inference: extend this odd-period ancestry bridge across earlier time slices, or identify the exact separate periodic forced-only argument before using it. The all-depth prize bound remains open.


## GC1093 — The two white-parity second images intersect in four nilpotent rows (2026-10-11)

**Missing inference advanced.** GC1092 covers an odd-periodic immediate successor. It cannot be used for a later slice without retaining its earlier origin. A finite hidden graph now handles the second slice, at every odd spatial period; arbitrary earlier slices and the periodic forced-only theorem remain open. CL268 at0964681c confirms GC1092, now promoted, and accepts the scope correction:8.88's periodic forced-only exclusion is COMPUTED through visible period10, with its general argument owed. No Local or Intel run duplicated.

Record searched: white.parity|alternating.white|checkerboard.white withancestor|earlier|period|collapse ->18 hits in5 files; parity.image|phase.intersection|white.parity withtwo.step|second.update|intersection ->0 hits. G122/G124 inverse graphs, G152, GC1092 and strategy D2/D3 read. Predictions preceded controls and the adaptive graph construction. The proposed XOR-linear second-image classification failed and is retained below.

**Exact hidden representation, PROVED (CL269).** Let A_even be all bi-infinite rows white at every even site, and A_odd the corresponding odd-white rows. Then

    F^2(A_even) intersect F^2(A_odd)
      = {000..., (001)..., (010)..., (100)...}.

Write the free odd bits of x in A_even as z_j=x_(2j+1). Directly applying Rule30 twice gives its output pair

    (w_(2j), w_(2j+1))
      = (NOT z_(j-1) AND z_j,
         z_(j-1) XOR (NOT z_j AND z_(j+1))).

For an origin in A_odd with free even bits u_j, the output pair is

    (u_(j-1) XOR (NOT u_j AND u_(j+1)),
     NOT u_j AND u_(j+1)).

Set a=z_(j-1), b=z_j, c=z_(j+1), d=u_(j-1), e=u_j, f=u_(j+1). Equating these two pairs gives an exact16-state graph with state(a,b,d,e), next state(b,c,e,f), and common output label(E,O). No independent choice is lost: consecutive states retain the overlapping hidden bits of both origins. Its complete nonempty edge table is below; all unlisted states have no outgoing edge. Each displayed label applies to every target in its row.

| State | Targets | Output pair |
| --- | --- | --- |
|0000|0000|00|
|0001|0010,0011|00|
|0010|0101|01|
|0110|1000,1100|10|
|0111|1010,1011,1110,1111|10|
|1000|0100|00|
|1001|0110,0111|00|
|1010|0001|01|
|1110|1001,1101|01|

The only cycles are the zero loop0000 and0111 ->1110 ->1001 ->0111. The latter's labels10,01,00 give100100..., a single-black period3 row. No noncycle edge enters either cycle. Every departure terminates within four edges: the longest is0111 ->1010 ->0001 ->0010 ->0101, whose last state has no successor. Other departures are the terminal choices at0111,1110 ->1101, and1001 ->0110 ->1000 ->0100 or1100; the remaining transient states lie on these chains. Thus a bi-infinite walk stays on one cycle, proving containment in the four stated rows. Conversely001010 ->011011 ->010010; shifting the origin by3 exchanges its white parity without changing that second image. Spatial rotations give all three singleton phases, and zero supplies the fourth row, proving equality.

**Finite consequence, PROVED (CL269).** A path of K output pairs has its first K-4 edges recurrent, since a noncycle edge cannot have four further edges after it. Those first pairs are therefore zero or one consistent singleton period3 pattern. Both types die after two more Rule30 updates wherever the radius2 cone fits. This finite statement allows arbitrary exterior cells; it does not assume a globally periodic parent or a recurrent physical orbit.

Let x be white on either parity throughout[a-2,b+2], and w=F^2(x) q-periodic on[a,b], with q positive odd and b-a>=q+14. Then

    F^4(x)_i=0 on[a+3,b-q-11].

Use x'_i=x_(i+q), which has the opposite white parity and the same second image on[a,b-q]. Let c be the first site at least a on x's white parity, so c<=a+1, and take K=floor((b-q-c+1)/2) complete output pairs. Both origin cones fit inside their white-parity intervals. The graph forces the first K-4 pairs, on[c,c+2K-9], into one of the four nilpotent rows. Two updates kill[c+2,c+2K-11], which contains[a+3,b-q-11]. This proves the displayed all-odd-q bound and the corresponding far-left half-line statement. It extends the parity bridge by one earlier slice, still killing by time4. No encounter premise, arbitrary-time extension or prize bound is supplied.

**Failures and controls.** P3 predicted the XOR-linear period3 family of GC1092 for the second image. REFUTED by the exact singleton cycle:100 fails the XOR-neighbor identity, while100 ->111 ->000 is the correct extinction mechanism. P1/P2 named seven-ring ancestry controls and the unexpected five-ring control pass on160 parity-white starts; this is evidence only, not the all-period proof. The initial temporary control stopped with an IndexError on short cycles before verdicts; padding repaired it, retaining scalar/packed crosschecks. The even-q fixed checkerboard remains a counterexample to dropping oddness. P4 finite interval controls pass:64 hidden packets independently checked by literal two-step cones, all16 five-edge graph paths start recurrent,352 arbitrary-exterior fixtures (288 other fixtures correctly fail periodicity). Source:tests/probes/lexicon/rule30_two_step_parity_bridge.py. Next substantive missing inference: decide whether later-image intersections admit new mergers outside these nilpotent rows; images do not in general commute with intersection, so this second-slice certificate cannot simply be iterated.


## GC1094 — The third-image parity intersection is exactly the two constants (2026-10-11)

**Missing inference advanced.** GC1093 cannot be iterated by silently commuting image and intersection. Retaining both origins at the next slice proves that particular transition, not an all-time rule. CL269 at7d93d0cf independently confirms GC1093's graph, four-row intersection and finite bound; GC1093 is promoted. No solver, language-membership, record or periodic search duplicated.

Record searched: parity.image|phase.intersection|white.parity withlater|third|intersection|merger ->5 hits in3 files, GC1093's source and unrelated parity references; no third-image theorem located. Predictions P1 (exactly zero/one) and P2 (at worst two further ticks to zero) both held; counterfactual and unexpected bridge check preceded the graph computation.

**Exact intersection, PROVED (CL270).** With A_even/A_odd as in GC1093,

    F^3(A_even) intersect F^3(A_odd) = {000...,111...}
      = F(F^2(A_even) intersect F^2(A_odd)).

For the first origin, take its eight cells at sites-3..4 to be(a,0,b,0,c,0,g,0); for the opposite origin take(0,d,0,e,0,f,0,h). Three Rule30 updates give the two output cells at0,1:

    first:  (a XOR b XOR (NOT c AND g), b OR c OR g),
    second: (d OR e OR f, d XOR e XOR (NOT f AND h)).

The three-input OR on the origin's black parity is the new structural constraint. Equating the pairs gives state(a,b,c,d,e,f), next(b,c,g,e,f,h), and one common two-cell label. This retains both origin histories, rather than intersecting their marginals. The exact256-packet table has64 edges. Its ten cycle edges are the zero loop000000, labelled00, and the following three cycles, every edge labelled11:

    011101 ->110011 ->101110 ->011101
    011110 ->110101 ->101011 ->011110
    011011 ->110110 ->101101 ->011011.

The complete certificate in rule30_third_image_parity_bridge.py assigns each of the64 states a height in0..6. Every other edge strictly decreases that height and has no cycle-state target. Thus no noncycle edge can enter a cycle, continue for more than6 edges, or connect two recurrent components. This is checked over all64 edges, including possible bridges, not inferred from sampled cycles. The bound6 is attained by110101 ->101010 ->011100 ->110000 ->100001 ->000010 ->001100. Every bi-infinite common-origin path therefore stays on one of the four cycles, giving only the two constant output rows. Both outputs occur: zero has zero origins;001010 ->011011 ->010010 ->111111, and shifting its origin by3 changes white parity while leaving the third image unchanged. This proves equality and the particular image/intersection identity above.

**Finite all-odd-q consequence, PROVED (CL270).** Any K-pair path has its first K-6 edges recurrent: after a noncycle edge at most five further edges can occur. The first K-6 pairs consequently form one constant row, whose next update is white. Let x have either white parity on[a-3,b+3], and w=F^3(x) be q-periodic on[a,b], with q positive odd and b-a>=q+16. Then

    F^4(x)_i=0 on[a+2,b-q-14].

As in GC1093, x'_i=x_(i+q) supplies the opposite-parity origin with the same third image on[a,b-q]. Set c to the first white-parity site at least a, and K=floor((b-q-c+1)/2). The retained origin cones fit. The first K-6 output pairs are constant on[c,c+2K-13]; one more update kills[c+1,c+2K-14], containing[a+2,b-q-14]. The same argument holds on a far-left half-line. This is the third-slice bridge, still dying by physical time4, with arbitrary exteriors and no assumption that the parent is periodic.

**Validation and limit.** Literal scalar updates crosschecked against independent packed updates verify both formulas on all256 packets; the same constructor recovers GC1093's entire16-state table. The64-state height partition and all64 seven-edge paths verify the finite exit certificate.640 exterior fixtures satisfy the periodicity premise and pass the displayed interval bound;640 others correctly reject it. The even-q fixed checkerboard refutes deleting oddness or either origin. The unexpected intercomponent-path check is essential: cycles alone would not classify bi-infinite outputs if bridges existed. No failed prediction. This fixed-time identity still gives no later-time closure or all-depth bound; further fixed-time scans are not such a proof. Next proof target is a phase distinction preserved outside the common nilpotent basin, using the three-input OR ancestry constraint, rather than assuming the third-slice identity persists.


## GC1095 — A local0010 birth refutes a static third-image phase carrier (2026-10-11)

**Missing inference decided.** The proposed all-time phase distinction needs a carrier preserved by Rule30. The concrete carrier U=F^3(A_even) union F^3(A_odd) is not forward closed, even on a recurrent nonnilpotent orbit. This closes that shortcut, not every finite-type route or phase invariant. CL270 at19e1f7de confirms GC1094, now promoted. No further fixed-time graph scan or Local computation.

Record searched: parity.phase|white.parity|parity.origin|OR3|phase.distinction withpersist|invariant|merger|nilpotent ->15 hits in8 files; third.image|white.parity|parity.origin withforward.closed|forward.invariant|carrier ->one unrelated board paragraph. GC1094's joint OR3 formulas are the antecedent; the named ring is a control, not a new periodic-point discovery.

**Local obstruction, PROVED (CL271).** U forbids the spatial word0010 at every site. GC1094's first output pair is(a XOR b XOR(NOT c AND g), b OR c OR g), or(a OR b OR c, a XOR b XOR(NOT c AND g)) for the opposite origin parity. In either case a pair00 forces a=b=c=g=0. The next pair, with new hidden bit h, is(h,h) in the first case or(0,h) in the second. Thus00 cannot be followed by10. Both white parities are covered, and translating the window just exchanges them, proving the prohibition at every site with arbitrary exterior.

**Exact carrier exit.** The spatial period4 row1000 has one white parity and follows

    1000 ->1101 ->0001 ->1011 ->0010 ->0111 ->0100 ->1110 ->1000.

Its third image1011 is in U by construction; its fourth0010 is outside U by the prohibition. Hence F(U) is not a subset of U. The12-cell cylinder100010001000 fixes the fourth-image patch0010 for every exterior, so the local exit is not a ring-boundary artefact. A globally parity-white completion supplies the actual carrier counterexample; arbitrary exteriors alone need not preserve the global carrier premise.

**Failure retained and scope.** The original six-cycle prediction was REFUTED:0111 maps0100, not1000. Scalar and packed updates agreed; this was a trajectory prediction error, not an instrument failure. The verified eight-cycle leaves the unchanged third/fourth-image argument intact. Its four temporal column traces are11010001,01000111,00011101,01110100; every one fails period2. Thus it refutes neither GC1092..94's odd-period slice lemmas nor the alternating-wall conjecture. The missing wall coupling cannot be replaced by this static carrier.64 OR3 packets and256 arbitrary-exterior cylinder controls pass; the full eight-cycle is independently checked. Source:tests/probes/lexicon/rule30_parity_carrier_exit.py. Stop this carrier closure attempt. Next return to the RRL main line: the actual black-A reset's001-to101 ancestry, where an inherited guard could bar another A restart; no global-affine or unary explanation resumed.


## GC1096 — A black-A restart needs a four-step ancestry guard (2026-10-11)

**Missing inference.** Can the actual black-SS reset's00100-to101 ancestry bar another A? The equal pair A11=A13=1 alone cannot. A fresh all-tail counter-cylinder restarts A, but its first20 cells are excluded by every four-step clamped past. Thus this shortcut fails and a concrete correlated ancestry guard survives; the universal actual-SS restart exclusion remains open. CL271 at12a07331 confirms GC1095, now promoted.

Record searched: black.eleventh|00011111 with101|guard|restart ->33 hits17files; GC1083/84/89/90/91 read. No solver, visible-language membership, CUT or record computation. Predictions preceded the successive controls. Source:tests/probes/lexicon/rule30_black_A_ancestry_guard.py.

**Fresh counter-cylinder.** The30-cell origin111010001111100000111000000000 has black A11=A13. For every exterior, its forced prefixes are

    time6:  111001001000100110000111
    time16: 1110011011101100101
    time26: 11101000110110110.

Its fifth track is S+D+H, and it returns A at26.52 fresh-right implications certify the cylinder, including extending the determined prefix when its last known cell is black;64 complete literal/packed histories independently agree. This refutes P1's no-restart assertion under the equal-pair premise. It is not an actual black-SS counterexample.

**All-age near-wall guard, PROVED (CL272), with finite certificate.** At every even age T>=4 beside the clamped0101 wall, a row cannot start with

    11101000111110000011.

For any target y of length n, choose the rightmost two parent bits a,b. The substitutions x[j-1]=y[j] XOR(x[j] OR x[j+1]) for j=n-1 down to1 determine the entire parent. Keep it precisely when y[0]=wall XOR(x[0] OR x[1]). This exhausts all four choices, with no assumption on the farther exterior. Applied three times with wall values1,0,1 to the displayed20-cell packet, the complete inverse sets have4,8,20 elements; all20 third parents begin1110010. The source checks every inverse edge forward and retains the complete construction. No fourth parent with wall0 can have that seven-cell image: if x0=1, the first two image bits force x1=x2=0, the third forces x3=1, contradicting image bit3=0. If x0=0, image bits0..5 successively force x1..x6=100001, contradicting image bit6=0. Hence the inverse tree is empty at four steps. Translation in time by any even amount preserves the same wall values, proving the stated all-age exclusion. It excludes the fresh counter-cylinder without banning every restart selector.

**Failures and controls retained.** P2's4096 specified actual-SS constructions (prefix11101111111100, twelve free cells, ten whites) found no restart; this finite failure proves no universal absence. P3 predicted an actual six-step preimage of the fresh counter; it fails already at four steps. The inverse instrument control recovers the known GC1091 source among632 six-step preimages and checks every edge forward. P4 predicted a prefix of at most19 would suffice; REFUTED, its19-cell prefix has a four-step parent, independently propagated forward, whereas20 is absent. P5's corrected20-cell guard holds. The unexpected selected control whitens A13 while retaining black A11 and reaches C at16; no necessity claim follows.

Next transport the full black-SS past into the entire101-toA selector, beyond the one forbidden cylinder. This block supplies a necessary joint guard, not an absorbing carrier or an all-depth record bound. Stop extending the failed4096 construction scan.


## GC1097 — Mature black-A ancestry excludes the complete S-D-H-A restart (2026-10-11)

**Missing inference moved.** The black-A reset's entire00100-to101-toA gate is excluded, at every even clamped age T>=4 and for every farther tail. This extends GC1096's single forbidden cylinder to a whole macro transition. CL272 ate6ab8147 independently confirms that earlier guard, now promoted. The following B guard and the all-depth record bound remain open.

Record searched: black.eleventh|GC1096 with101|guard|restart ->16hits8files; GC1083/91/96 read. Predictions and adaptive alternatives preceded each packet check. Source:tests/probes/lexicon/rule30_black_A_no_restart.py. No solver, CUT, visible-language membership or record computation.

**Statement, PROVED (CL274 atc4744f11), with complete finite packet certificate.** Let the row at even T>=4 start1110100011111, the black-A prefix with sites6..13=00011111. GC1091 gives low00100 after S6. Suppose its next ten ticks have fifth track D and return101. GC1075 gives H, and GC1083 says returning A after H requires that101 origin's sites10..14 be11100 or1101*. Neither alternative is possible with this past.

Use GC1096's complete inverse substitution, checking its first cell against the wall. The full selector11100110111100 has no two-step clamped parent. Selector1110011011101 has exactly four two-step parents; their sites6..15 at D-time8 are

    1110111010, 1110111011, 1110111100, 1111000001.

The first, second and third have no earlier D past after respectively one, two and one backward updates, since the prescribed fifth cells there are white. By hand, an image beginning1110 beside a white fifth cell forces its parent to begin0100. Extending the first packet forces its parent bit9black and contradicts the final image0; the third contradicts image bit8. The second has only parents01000100010/11, whose prefix010 itself has no white-fifth parent: initial image0 forces the first parent pair00, image1 forces the next parent1, contradicting the next image0. These alternatives cannot simply be dropped by assuming time8prefix1111; that prediction P6 failed and the extra alternatives are retained.

For the remaining packet1111000001, the complete eight-step backward D construction has1282 parents. Exactly248 match the required low prefix100100; every one begins10010001. Transport these248 through the preceding S6, retaining the established black-A shield prefixes at its times0..5:

    00011111,10110000,0010100,111011,100010,11011.

The complete retained inverse sets have sizes788,522,1680,838,608,384. Every final parent begins000111110000011 at sites6..20. Including the A prefix's first five cells gives exactly11101000111110000011, excluded by GC1096's four-step clamped guard at every even age>=4. Thus the final selector has no actual parent of the stated age. The finite construction exhausts the necessary origin packets; translating its time origin by any even amount proves the all-age macro exclusion. In particular actual black-SS resets at time6 qualify. This is a local transition exclusion, not a cutoff scan extrapolated to a record bound.

**Controls and retained uncertainty.** Every inverse edge is checked forward; all384 final packets independently propagate through S6+D8 to the target.64 nonvacuous literal/packed actual histories use the36-cell source111011111111000010000000000000000000: black A at6,low00100 at12,101 at22,H then B at32. The fresh GC1096 source still returns A, refuting deletion of the age premise. P3's shorter low10010001 packet has eight black-A parents and forces only A14..16white, so it alone does not prove exclusion; the full D8 packet is essential. P4's additional actual-SS time3 guard rules out A14..18fivewhites and holds, but the reviewed GC1096 guard suffices for this proof. The identified unexpected check is P6's three1110 alternatives, excluded only by earlier D past. No failed alternative is promoted to a theorem.

Next carry this same black-A past through the remaining101-toB branch and decide B12 under white B10/B11; that is the missing guard for admission to GC1087's absorbing carrier. No additional construction scan or Local run requested.


## GC1098 — Black-A past guards its first B; white short blocks remain (2026-10-11)

**Missing inference moved.** If black-A's S-D101-H continuation returns B immediately, its B10=B11white forces B12white. Thus B with white10 enters GC1087's guarded-B carrier; black B10 instead enters C on its next short by GC1052. This handles the first-B branch for every tail. It does not cover an intervening unbounded SS block. The returned S's sixth marker is white, so those outstanding short blocks keep a white marker by GC1056. GC1097's no-A certificate is still awaiting independent review.

Record searched:101.*B|B.*101 withwhite12|site.12|sparse|admission ->88hits28files; black.eleventh|GC1097 withguard|B ->22hits10files. GC1086/87/1075 read. Source:tests/probes/lexicon/rule30_black_A_B_admission.py. No solver, CUT, visible membership or record run.

**Sparse guard, PROVED (CL275), with complete packet certificate.** Start with black-A1110100011111, sites6..13=00011111. Its fourth S row begins100010 at6, and its sixth is low100100, by GC1091. Suppose D returns101 and its H returns bad B, namely sites6..12=0011001. Pull the latter back through H's last three updates; intersect with its known time7prefix01. There are13 parents. Pull through its earlier seven updates, retaining GC1075's high101 shields1101,1001,0111,1100,001,111,100. The complete112 high parents have only three first-ten-cell prefixes:

    1101101101,1101101110,1101110000.

These are necessary conditions for bad B, without assuming core J ancestry. Pull all three backwards through D10, retaining the verified low prefix shields at its times0..5:

    100100,11111,0000,000,10,0.

The complete retained sizes are12,20,29,14,24,25,23,64,228,108. Thus108 low parents survive; low00100 alone has not excluded the bad prefixes. Pull those108 back through S's final tick, retaining S5prefix11011:240 parents. One more backwards S tick leaves no parent beginning10001. Black-A's actual S4prefix100010 implies10001, giving the contradiction. Completeness follows from the two free rightmost bits and left-permutive substitution at each inverse edge; every edge is checked forward. Hence the sparse B guard holds independently of farther tail or time origin. It needs the short past, not just the low label.

**White marker and nonvacuity.** GC1075's H8prefix11 gives H9prefix00 by black-cell masking. H10's first cell is then white. The fixed36-cell actual SS source111011111111000011001000000000000000 forces black A at6,low00100 at12,101 at22,B0011000 at32, and core100 at38 for every tail.76 causal fresh-right implications and64 literal/packed histories confirm it. Conversely the fresh high source11100110110110100000000 forces bad B111010011001 after10 for every exterior, independently checked in64 histories; the preceding black-A short past is essential.

**Errors retained.** The first apparent low-only exclusion used incorrectly copied D shields01111/1100. Direct scalar transport corrected them to11111/0000; the erroneous empty-set verdict is invalid and withdrawn. Ten fresh-right checks now guard those premises. The corrected108 low parents disprove that stronger inference, while the two preceding S ticks close the intended one. Two attempted A13 sharpness controls still had no parent; the first retained earlier consequences, and weakening all shields still retained the low premise. No necessity of A13black is claimed. The selected J control and four immediate exteriors predicted black B13 but gave it white; stop that selection, retain the earlier generic-pair refutation, and assert only sparse B12 here.

Next carry the same inherited past through an arbitrary white-marker SS block to its first SL return. Immediate first-B admission and the mature no-A bridge leave precisely that inter-run transport missing; the all-depth record bound stays open. L619 at92bbe913 received: sampled bounds35 at699/1371, two unreproduced witness bounds, CUT-P19 UNKNOWN, verified SAT200 round0 cuts; no duplicate work.


## GC1099 — One white SS after D-H preserves the sparse B guard (2026-10-11)

**Missing inference moved.** Suppose a D renewal returns101, its H returns S, and that S performs one SS before returning B. If B10=B11white, then B12white. This all-tail macro exclusion does not need a black-A origin or a low100100 premise. It reaches the first delayed B branch; arbitrary white-SS blocks and their A exits remain open. CL274 atc4744f11 independently confirms GC1097, now promoted; its full-row proof and sharp age-2 countercontrol are received. L620 at2aa2c252 and CL273 independently verify all sixteen sampled witnesses; no duplicate replay.

Record searched: white.SS|white.marker with admission|A11|eleventh ->5hits4files; relevant GC1056/1087/1089/1090/1098 sources read. The broader100100|00100 search with SS|short.block gave310hits116files; narrowed100100 with SS gave148hits66files, with the named ancestry sources read. Predictions and adaptive failures are retained in tests/probes/lexicon/rule30_white_SS_exit_guard.py. No solver, CUT, membership or record computation.

**PROVED (CL277), uniform in time and arbitrary exterior; the guard is vacuous for actual one-SS B exits.** Bad B is sites6..12=0011001. Its complete six-step SS pullback with a white initial marker has195 parents, all realizing SS in the full row. Pull those through H's ten ticks using reviewed GC1075 shields1101,1001,0111,1100,001,111,100. The retained counts are438,1351,4545,1595,1452,4487,8473,5590,14120,22724. Every high origin begins1101001 at sites6..12; its first10 cells are precisely that prefix followed by all eight three-bit words. Thus only one seven-cell necessary packet remains.

That packet has no four-step past beside four white fifth cells. The complete inverse layers are

    1101001
    -> {01011010,01011011,01011100,01100001}
    -> {001111010,001111011,001111100}
    -> {0001001101,0001001110,0001001111}
    -> empty.

The last contradiction is already in00010: with a white left cell, its first three zero images force four initial white cells; image bit3black then forces the next parent black, contradicting image bit4white. Every inverse edge is forward checked. D's last four fifth cells are white, so any actual D-to101 high origin has exactly the past that this packet lacks. Bad B after H-SS is therefore impossible. This is a fixed joint-past certificate valid at every even translated origin, not a finite-depth record scan. B with black10 or black11 enters C by GC1052; B00 now has the sparse guard. This does not exclude A or a further SS.

**Nonvacuity and limitations.** The fresh low29-cell source11100100100010000110100000000 forces D-H-SS-SS for every farther tail. Its causal prefixes at10,20,26 begin111001101,111010000,111010000 respectively. Thus white short blocks really can occur after a00100 low return; fifth-track freedom cannot be discarded. Its earlier actual black-SS ancestry is not established.140 fresh-right causal implications and320 literal/packed histories pass, including four generic white-SS/H-SS counter-cylinders and the known white-SS control111010000.

**Failures retained, next inference.** White marker alone and fresh H101 both permit black-A and bad B after one SS. A ten-cell projection leaves11200 black-A parents with six different first13 prefixes, refuting the proposed five-white ancestry shortcut; these are relaxed packets, not actual restart witnesses. Full entrance transport through D and S reached220160 packets; its first preceding SS layer reached606208, over the preregistered500000 cap. That attempt is UNKNOWN and stopped. The initial full-row replay assertion exposed a separate defect: prescribing the fifth track is a relaxation, so the realized track must be checked; the corrected filter removes30 of212 white-SS A parents. Next seek a closed joint-past invariant for repeated white SS, including A exits; do not extend that capped inverse tree or infer all-block admission from this one-SS guard. The owner-prioritized RRL target remains active; the suggested check-free hand target stays parked while this missing inference is unresolved.


## GC1100 — Actual white SS can delay and restart black A (2026-10-11)

**Missing inference resolved negatively.** Mature black-A S-D101-H can enter white SS and return black A after that extra block. The no-entrance shortcut is REFUTED by an actual black-SS origin, rather than a fresh low packet. The all-tail certificate below is PROVED (CL278 at31212576); admission after arbitrary white SS and the all-depth record bound remain OPEN. GC1097 excludes an immediate A return and is unaffected.

Record searched: black.A.*SS|SS.*black.A with entrance|age|no.SS ->19hits8files; GC1097..99 and CL275 read. Predictions, counterfactual, adaptive failures and controls are retained in tests/probes/lexicon/rule30_black_A_white_SS_entrance.py. No solver, CUT, language-membership or record run.

**Actual delayed reset, certificate.** Fix the first41 cells to

    11101111111010000001101000000001111001010.

For every farther exterior, black SS at0 gives black A1110100011111 at6, low11100100100 at12, high111001101 at22, white SS111010000 at32, black A1110100011111 again at38, and low11100100100 at44. The fifth track on0..43 is SS-S-D-H-SS-S. At each tick enumerate both fresh right cells against the determined prefix; retain exactly the cells whose images agree in all four choices. Black-cell masking can extend the determined prefix. This gives88 causal implications and proves independence from every exterior, not only a selected padded tail.64 independent literal/packed full histories agree, and the discovered inverse path is replayed forward at every edge. The black-A label names its black eleventh cell: the sixth marker at32 and38 is white, consistent with GC1056's white-marker persistence.

**Full strip matters, independently of future projection.** CL275 confirms GC1098, now PROVED, and strengthens it: D-H-B00 implies B12white without black-A or low ancestry. Independently pulling bad B111010011001 through full H retains3,5,13,46,79,60,152,420,104,112 high packets; five backward D ticks give164,460,456,96,0. The known fresh bad-high prefix is present among112, and the known actual good-B path passes all20 inverse H/D edges. Projecting these112 complete high packets to sites6 onward gives exactly the unprojected sub-row H set, so no farther future cells were lost. With the fifth boundary freed, its corresponding five D layers retain448,588,968,280,224. The difference therefore requires consistency of the strip generating column5, not merely retaining more future bits. The original GC1098 short-past proof remains valid, but its assertion that that past is essential is superseded by CL275.

**Failures retained.** The complete H and D entrance layers ended at248 and17376 respectively; S then hit555392 at S-time2, above the preregistered500000 cap before the A filter. That frontier was UNKNOWN and stopped. A different existential streaming decoder, with reviewed S/SS shields and250000 inverse-edge cap, found the displayed actual origin after110783 edges. It selects one verified path and proves existence only; no complete-layer absence is inferred. The follow-up prediction of a second SS at38 failed: A returns instead. Default replay retains the certificate; optional construct reproduces that bounded derivation. Do not extend either stopped complete ancestry tree.

**Unexpected alignment check.** Its even-time visible word through44 is10010010000100001001001, with gap lengths3,3,5,5,3,3. Thus its LLSS portion is5533, whereas GC986's at-most-one4422 motif is1000100010101. The proposed occurrence-budget transfer fails; the two/four zeros inside S/L are not their gap lengths. No reset rank or charge follows.

**CL277 received.** The GC1099 packet computation is independently CONFIRMED, hence its conditional guard promoted; Cloud also reports the stronger absence of any B after H and one white SS from an actual101 return, plus exclusions across longer blocks. Our units do use fifth track111010 and white sixth markers at every white SS entrance/return. Its stronger all-block packet claims are not replayed here. The actual A exit above remains and answers the remaining branch concretely. L622/L623 received: corrected deep-C sample count2^31 per phase and agreement of existing SOF visible counts; no duplicate computation.

Next seek an inherited joint-past invariant or record potential for repeated delayed A resets. This counter rules out removing the SS branch as an unrealized boundary artifact; it neither exhibits an infinite reset orbit nor excludes a depth-dependent record bound. Check-free work remains parked under the owner's RRL priority.


## GC1101 — A finite hidden potential bounds consecutive one-SS delayed A resets (2026-10-11)

**PROVED, independently confirmed CL279.** The GC1100 delayed reset cannot repeat indefinitely with exactly one white SS on each return to black-eleventh A. Starting with any of the three13-cell A prefixes specified below, at any even clamped age, at most two consecutive typed macros M=S6-D10110-H10-SS6 return black-eleventh A. This bound is independent of farther tails and age; it is not an all-depth record bound or a bound for variable SS-block lengths. GC1100 is now PROVED after CL278's independent16384-exterior exhaustion and three-valued check. No sharpness for two actual returns is asserted.

Record searched: delayed|white.SS|black.A with strip|rank|potential ->28hits17files; white.SS|white.marker with A13|A11|black.eleventh ->6hits5files. GC1096..1100 and CL275/277 read. Predictions and adaptive failures are retained in tests/probes/lexicon/rule30_delayed_A_strip_rank.py. No solver, CUT, visible-membership or record computation.

**Sound hidden representation.** Keep the first20 cells, updated jointly beside the alternating wall. At every tick allow both values of cell21; OR masking removes the second image when cell20 is black. This contains every actual history, including every correlation imposed by the exterior, while allowing extra boundary histories. Column5 is generated by the same strip; retain its prescribed M track, not an independently clamped fifth boundary. Label every initial packet and transport the union of its origin labels through each update, so final macro edges retain joint origin-to-endpoint compatibility.

At time6 retain the common low prefix111001001; at16 the D return1110011011; at26 white S111010. The tenth bit at16 is black because1110011010 has no predecessor beside wall1, whereas111001101 has one: that row has sixteen actual clamped past ticks even when the macro starts at age0. The final A's black-eleventh white-SS exit has sites10..13 in1100,1101,1111. This last exhaustive six-tick cone has5120 scalar/packed cases and includes all farther exteriors. Thus there are384 initial/end packets, three13-cell prefixes followed by seven arbitrary bits. Restoring GC1096's forbidden mature packet shows no starting-age premise is needed here.

**Explicit potential.** For a packet whose first13 cells are P=1110100011111, assign rank2 when sites14..20 are0000010 or0000011; rank1 when they are1111000 or11101 followed by either two bits; rank0 otherwise. The other two A prefixes1110100011100/1101 always have rank0. The complete32-tick finite relation has273 edges and66 distinct endpoints. Every edge strictly lowers this specified potential. All seven positive-rank packets have outgoing edges, no other packet does, and only three of the66 endpoints have any outgoing edge. Therefore no path has three M edges. Inductively projecting any actual repeated-reset history gives a path in this relation, proving the uniform two-return bound; the argument uses finite transition completeness and a decreasing invariant, not extrapolation from a finite age scan.

**Controls and failures.** Every packed strip transition is checked by independent scalar Rule30 formulas with both right inputs. Eight origin-by-origin scalar set flows independently match the labeled relation, including both rank2 packets and the two additional A types. GC1100's actual macro follows an edge of rank1 to0. The narrower1111-only candidate was acyclic too, with181 edges; however its claimed endpoint completeness failed: black11 white-SS returns also have1100/1101. The prediction that those extra types enter core C on the next S failed; both return low001. They are retained in the corrected representation and have no M-to-black11 successor. An initially inferred245-edge fresh count was incorrect; exhaustive joint construction gives273 and the potential is checked on those edges. No failed shortcut supports the theorem. The identified unexpected check is endpoint productivity: only three of66 image packets can themselves take M; replacing origin-labeled edges by a Cartesian endpoint image would fabricate recurrence.

Next transport this potential through arbitrary numbers of white SS before the A exit, or identify an explicit relation edge that raises it. Mixed types and variable block lengths remain open. The fixed20-cell success supplies new invariant evidence for that step; no wider-strip sweep, stopped ancestry tree, or Local computation requested. L622's cced5ea7 flag ACKed; Local's SP11..14 registration received and its lane preserved.


## GC1102 — Arbitrary SS transport breaks the reset rank but bounds each SS block by three (2026-10-11)

**PROVED (CL280).** GC1101's one-SS reset potential does not extend to variable SS-block lengths in the same20-cell relaxation. Nevertheless every represented A-S-D101-H history has at most three consecutive white SS blocks before its next non-SS return, at every even starting age and for every farther tail. This has a reviewed finite decreasing SS potential, not a finite-length scan extrapolated to all lengths. Repeated variable-block A resets and the all-depth record bound remain OPEN.

Record searched: white.SS|SS.block|delayed with potential|rank|arbitrary|repeat ->34hits13files; GC1056/1100/1101 and CL277 read. Predictions, failures and controls are retained in tests/probes/lexicon/rule30_delayed_A_SS_star_rank.py. No solver, CUT, visible membership, record run or wider-strip sweep.

**All-length hidden relation.** Start with GC1101's384 packets: first13 cells111010001 followed by1100,1101 or1111, then seven arbitrary cells. Transport their origin labels jointly through S6-D10110-H10 using the same necessary pins and alternating wall.81 white-SS entrance packets remain. Apply SS6 repeatedly, retaining the five valid white-SS nine-cell entrance prefixes and carrying only newly reached origin/packet pairs. This least-fixed-point iteration exhausts all SS block lengths because its finite domain has at most384 times10240 pairs, each newly processed once. Independently verify that applying SS to the final137 reachable entrance packets adds no origin label at any continuation and that its A exits equal the recorded all-length exits. No fixed k cutoff is used.

**Uniform SS-block certificate.** The complete inner SS relation on those137 reachable packets has244 edges and is acyclic. The source lists the seven packets of rank2 and49 of rank1; the remaining81 have rank0. Every inner edge strictly lowers this explicit potential. An actual continued SS block projects to an inner edge, since the full strip evolves jointly and the saturated origin relation contains it. Therefore there are at most two continuations between SS entrances and at most three complete SS6 blocks after A-S-D-H. The whole typed return occurs by44 ticks from the A origin. This conclusion is uniform in age and exterior, with no assertion that three actual blocks are attainable.

**Reset-rank failure retained.** The all-length A-return relation has742 edges and101 endpoints.192 edges fail to decrease GC1101's A potential. In particular

    11101000111111110100 -> itself

occurs with two white SS blocks (M_2 has38 ticks), whereas it has no one-SS self-edge. Thus the bounded SS residence does not itself bound repeated resets. GC1101's exact one-SS theorem is unaffected; the broader20-cell reset-rank candidate is CLOSED, not all finite hidden-language routes.

**Identified consistency defect, not a no-lift proof.** One explicit free-boundary path for that self-edge has column21 word00000011000011000001000100011010000010. At ticks7,13,19,23,28,30,36 it violates the necessary actual update b(t)=1 implies b(t+1)=1-a(t), where a is column20 and b column21. This follows directly from Rule30's OR masking. That path cannot come from any jointly evolving right half. Other paths to the same self-edge have not been excluded, so the actual self-loop lift remains OPEN. The defect identifies a temporal boundary constraint to retain next; it does not license deleting the loop from the current sound overapproximation.

**Controls.** The k=1 edge set equals GC1101's273-edge relation exactly. Eight independent scalar SS set flows match the packed propagation. The actual GC1100 delayed reset remains an edge and its real boundary passes15 nonvacuous black-mask controls; the fresh low counter-cylinder independently retains two SS blocks. Every extracted self-edge update is scalar-checked. The unexpected check separates the acyclic inner SS graph from the cyclic A-return graph; endpoint or iteration counts alone would miss that distinction.

Next decide whether the named M_2 self-edge has any boundary history satisfying column21's own temporal update, and retain that consistency in a hidden invariant. No complete ancestry tree or larger-width sweep. GC1101 review is pending; no Local/Intel computation requested.


## GC1103 — Variable A resets have at most two exceptional outputs and a finite-left deadline (2026-10-11)

**PROVED (CL281), serves Q6.** Any consecutive typed black-eleventh A return chain M_k=S6-D10110-H10-SS6^k, with the same three A13 types and necessary pins as GC1101/1102, has at most two returns with k different from2. Thus its only recurrent macro output is M_2, even though its hidden packets can branch. For an actual full-line history with leftmost black at -J at the chain's start, J>=-1, the chain lasts at most7J+796 ticks. This bounds the delayed-A obstruction at every left depth; admission to this regime, exits from it and the full realized-record bound remain OPEN. CL279 at bc4876c9 independently confirmed GC1101; promoted here.

Record searched: column21|GC1102|11101000111111110100 with boundary|lift|mask|loop ->6 hits4files. GC1101/1102 sources, GC706's reviewed finite periodic-motif cost and RULE30-PRIZE8.54 read. Predictions, counterfactuals, failures and controls are in tests/probes/lexicon/rule30_delayed_A_boundary_memory.py. No solver, CUT, visible-membership or record computation.

**Boundary repair does not remove the loop.** Keep x=sites1..20 and b=site21. Update x jointly using b; update b by a XOR(b OR c), where a=site20 and c is an arbitrary fresh site22. Equivalently b=1 forces next b=1-a; b=0 permits either value. Every actual history projects to this relation. For GC1102's named20-packet11101000111111110100, the complete M_2 initial/terminal boundary relation is exactly0->0 and0->1. Initial b=1 dies at the101 pin at tick16. A retained0->0 path has boundary word000000111000000000110001100111100001100, including the final bit, and repeats as a controlled21-cell strip because38 is even. Hence the prediction that this specific temporal defect excludes every loop lift is REFUTED. Actual right-half realizability is still OPEN; do not widen cosmetically or confuse a controlled strip with an actual exterior.

**Switch to the output invariant.** Reuse GC1102's existing20-cell relation and label each edge by its number k of SS blocks. The inner SS certificate bounds k by3; the union of k=1,2,3 edges equals its all-length fixed-point relation exactly (742 edges). Mutual reachability gives one recurrent component: the three packets11101000111111110100,11101000111111110101,11101000111111110111, all nine directed edges, all labelled k=2. This identified unexpected check separates packet branching from output branching.

The source gives an explicit potential rho: rank2 on two hex packets, rank1 on eight, rank0 on the other374 represented packets (little-endian bit0 is site1). For every labelled edge x -> y,

    rho(x) >= rho(y) + [k != 2].

The verifier exhausts every edge and label against that fixed table. Telescoping bounds exceptional k=1 or3 returns by2 on any finite or infinite path. Unlike GC1101's strict reset rank, rho may remain constant on M_2 cycles. Forward joint-strip layers independently fix the full column1 word of every macro, including odd times: h(SLLS^k), with h(S)=110100 and h(L)=1101000100. Thus every infinite typed chain eventually repeats the38-tick word h(SLLSS); no packet determinism is assumed.

**Concrete finite-left bound.** At most two exceptional macros, each duration<=44, split any chain into at most three runs of M_2. A run of n M_2 macros starting at elapsed time a has adjacent wall/column1 traces38-periodic on its38n pre-closing samples. The left edge is then J+a cells away. GC706's finite motif bound gives38n<=J+a+76, including J=-1. Hence its endpoint is at most2a+C, C=J+76. Inserting two exceptional intervals of duration at most E=44 yields the universal end bound

    T <= 7C + 6E = 7J + 796.

Empty runs only weaken this bound. No actual sharpness is claimed. It uses a fixed, proven exception budget; the earlier mixed-letter change inequality alone had no such budget. In particular an infinite typed A-return chain is incompatible with finite left support, despite the surviving controlled-strip loop.

**Checks and next inference.** Four independent scalar21-cell macro set flows reproduce the named boundary relation;32 actual GC1100 joint updates pass. The previously chosen inconsistent loop path is rejected as a negative control. The explicit exception potential is checked on all labelled edges; the full column1 words agree with GC706's independently derived block lift. Network/gate connectivity works and the scheduled heartbeat remains ACTIVE; no recovery change needed. Next establish which non-A exits/reentries can replenish this exception potential, or extend the output certificate to those exact transitions. Repeating wider strips or insisting on packet acyclicity is not the next step. Cloud review requested for the labelled relation, potential and7J+796 composition; no Local/Intel run requested.


## GC1104 — Non-black A exits of the delayed SS block enter the absorbing core (2026-10-11)

**PROVED (CL283 at23812902), with a finite hidden certificate and hand shield, serves Q6.** Under GC1101/1102's typed A-S-D101-H ancestry, after one or more white SS blocks every non-SS exit is A. A black eleventh gives the three already represented A13 types; a white eleventh enters GC1087's absorbing C after its next S6-D10, for every farther exterior. Thus a white-A exit cannot replenish GC1103's exception budget by later returning to black A. This closes that exact exit route, not general admission or R_real(d).

Record searched: A.exit|non.A|reentr|replenish with core|guard|GC1087|GC1103 ->27 hits17files; the named sources and GC1087/1090/1102/1103 read. Predictions, failures and controls are retained in tests/probes/lexicon/rule30_delayed_A_exit_admission.py. No solver, CUT, visible-membership, record or wider-strip computation.

**All-length exit coverage.** Reuse the reviewed20-cell finite relation, including original A labels and its all-length SS fixed point. Its SS terminal image has139 non-SS packets:101 black-eleventh A packets and38 white-eleventh A packets. The latter first13 cells are1110100011010 (26 packets) or1110100011011 (12); there is no B or010 exit in this relaxation. Applying S gives57 low packets, all beginning1110010010. Applying D gives157 packets, all in C010 or C100. Every intermediate fifth bit is checked on the unfiltered successor set, so these conclusions do not silently discard a different long track. All packed images of those S/D layers match independent scalar Rule30 images with both right inputs. The finite-state coverage and original SS fixed-point induction make the result uniform in age, SS length and exterior, not an extrapolation from a depth scan.

**Structural reason for the exceptional white-A branch.** When low site11 is black, its prefix11100100101 is GC1090's reviewed C010/011 entrance shield. When low site11 is white, retained ancestry forces the longer common prefix111001001001001. Its known prefixes at D1 through D7 are

    100111111111111, 011100000000000, 11001000000000,
    0011110000000, 011000100000, 01010111000, 1101010010.

At D7 sites9,10=10. With a,b at11,12, D8 sites10,11=(NOT a,a OR b), whose OR is1. The known D8 prefix is000101111, so its site9 is black and D9 site10 is0. D9 sites8,9 are00, giving D10 site9=0. The final first9 cells are111001100: C100. This uses a joint OR constraint that the conservative prefix-only replay discarded; that initial method retained only eight endpoint cells and was inconclusive. Four independent local a,b controls and all16 complete19-cell causal cones confirm the repaired shield. The first13 bits alone fail on1110010010010000000, retained as a negative control. Fresh white11 A also need not admit C: GC1090's counter still returns111. Admission here uses the actual delayed-SS ancestry.

**Scope and receipt.** The38 relaxation exits are not asserted to be actually attainable. Eight independent scalar SS set flows and GC1100's actual black-A exit pass. The identified unexpected check is nonvacuity: B is absent, so no new B guard is advertised. Cloud CL280/281 at bfba2be7/855b2cb3 independently confirms GC1102/1103, promoted above. CL280 reports the named20-packet loop absent under width28 refinement, while CL281 reports other M_2 recurrent packets persisting through width36; these are received computations, not GPT reruns. The periodic-output deadline remains the relevant proved obstruction, and I need no further actual-loop search or wider refinement for this step. IN005/CL282 received; Intel's exact-language forced-only lane remains separate and the X_4 hand target stays parked.

Next missing inference: the same black-A low001 D return can choose111 instead of101 (GC1091). Retain that diversion's high-to-S/SS ancestry and test whether it can replenish the A exception potential. White-A exit reentry is now closed; the111 diversion and core record bound remain open.


## GC1105 — The111 diversion replenishes the existing exception rank in the20-cell relaxation (2026-10-11)

**Candidate extension REFUTED (PROVED CL284 at efea097c); actual lifting OPEN, serves Q6.** The missing inference was whether GC1103's finite exception budget survives black-A S-D111-H reentry. Its111 branch returns121 short packets, all with a black sixth marker; treating them as the reviewed white-SS entrance is false. One following SS gives17 typed black-A endpoints and98 labelled edges increasing GC1103's rank. Retaining arbitrary further SS yields a new recurrent M3 self-loop, so the existing20-cell representation cannot charge every non-M2 return by a finite decreasing vertex potential. This is a concrete failure of that representation, not a counterexample to the prize or to every finite-type route.

Record searched: GC1091/diversion with111/replenish ->2 hits2files; high.LL with two/bound/budget ->35 hits16files;111.diversion/D111/black.SS with all.k/fixed.point/exception.rank/potential ->3 hits2files, including the working probe. GC1080/1082/1091 and the delayed-reset sources read. The two-high long-run budget is already GC1082; its reproduction here is a control, not a new result. Predictions and failed admission shortcuts are retained in tests/probes/lexicon/rule30_black_A_111_diversion.py.

**All-length hidden obstruction.** Propagate the same384 A13 origin labels through S6-D10-H10, pinning low001 at6 and111 at16. At26 the complete retained image has228 packets:107 ordinary lows and121 black-marker shorts. From those shorts, the monotone SS fixed point has1115 packets and68 typed A endpoints, representing7166 origin/end pairs. Its closure is explicitly checked on all successors; the nine discovery waves are not used as a duration bound. The SS relation itself has a two-block cycle. Union with the reviewed101 return relation gives one recurrent21-packet component with231111 edges.

The named packet **11101000111011100000** returns to itself after S-D111-H and exactly three SS blocks. A finite visited-set search extracts its shortest return; every transition of the resulting44-tick path is independently scalar checked. Its full column1 word is **h(SLLSSS)**, where h(S)=110100 and h(L)=1101000100. Charging this non-M2 self-edge would require rho(x)>=rho(x)+1, impossible for any finite vertex potential. The right boundary is still refreshed freely each tick; no coherent infinite right-half lift or actual realization is claimed. GC706 excludes eventual periodic output for finite left support, but does not supply a budget for mixtures of M2 and this retained M3 obstruction.

**Controls and next inference.** Eight independent scalar origin flows, eight scalar SS flows, two family-B scalar flows, and GC1091's actual all-tail X cylinder pass. The identified unexpected check is the black marker at every H111 short endpoint, opposite to H101's white marker. The low branch reproduces GC1082's two-high bound but does not enter C/J automatically:36 of86 subsequent D endpoints miss the current guard. No solver, membership, record, larger strip or realization sweep. CL283 received and GC1104 promoted. Next seek a same-history111/black-SS guard that separates the new M3 recurrence from the reviewed101/white-SS M2 component; general admission and the all-depth record bound remain open.


## GC1106 — Joint boundary memory retains two distinct234-tick output cycles (2026-10-11)

**Obstruction in the joint21-cell relaxation, PROVED (CL285), serves Q6.** The specific missing equation after GC1105 is site21's temporal update, b'=a XOR(b OR c), with a at20 and c at22. Keeping it preserves all four boundary-colour returns of the named M3 packet **11101000111011100000** through44 ticks. It also preserves a mixed M2/M3 recurrent component and two explicitly scalar-verified234-tick loops at the same full21-cell state whose column1 words differ. Therefore this representation admits non-eventually-periodic outputs; GC1103's periodic-output deadline does not extend through these reentries using this boundary equation alone. Actual infinite right-half lifting and the prize bound remain open.

Record searched: GC1105/named packet/M3 with boundary/guard/past/self/recur ->42 hits18files, many unrelated M3 collisions; GC1103/1105 sources read. Predictions and failures are retained in tests/probes/lexicon/rule30_111_A_joint_boundary.py. The unexpected check: the named five-SS self-return vanishes, despite its complete three-SS boundary relation. That absence does not separate M2 from M3: the joint101 and111 SS fixed points have635 and1669 packets, and their union has one32-packet recurrent component with104 internal M2 edges. Fixed-point closure is checked; discovery depth is not a duration bound.

**Explicit output certificate.** Let A be the named M3 packet with boundary21=0, and B=11101000111111110100 with boundary21=0. The A-to-B connector is111/k1 via11101000111110001000 with boundary1, then101/k2. The B-to-A connector is101/k2 via11101000111011010100 with boundary0, then111/k3. Every macro has column1 word h(SLLS^k). Inserting B's38-tick M2 self-loop gives a190-tick A-to-A excursion E. Its44-tick M3 self-loop F can be placed before or after E. Both FE and EF are234 ticks, start and end at A with the same wall phase, and disagree first at tick44. Every time-level transition in both walks is independently scalar checked.

At each return, either walk can be concatenated again. Their equal lengths and differing traces give2^n distinct output words of length234n, hence model entropy at least1/234 bits per tick. Sampling the distinguishing bit at each block also yields a non-eventually-periodic model trace from any non-eventually-periodic sequence of choices. The refreshed site22 inputs are part of this model; no actual right-half realization is inferred. The mixed-output certificate uses explicit witnesses, independently of the SCC census. Three independent scalar whole-macro flows and26 actual GC1091 joint updates pass. No larger strip, solver, membership or record run.

CL284 independently confirms GC1105's closure, mixed20-cell component and named M3 self-return; its98 rank increases remain GPT-computed, not Cloud-replicated. Received width28 recurrence and inconclusive realization-search receipts; no GPT repetition. Next target: use the branch/SS-length labels of Cloud's already computed two width28 components to identify a concrete separating guard or a surviving mixed-output obstruction; request those existing labels if retained, with no new widening or realization search.


## GC1107 — A nonlinear short-gap selector reaches the twelfth left column (2026-10-11)

**PROVED (CL286), serves Q6's missing same-history carrier.** CL285 confirms that mixed M2/M3 output survives even in Cloud's existing width28 component; periodic-output separation is unavailable there. Seek a nonlinear left carrier of these renewal choices. Let q_s=x_1(2s), with wall x_0(2s)=0. In synchronized S/L, q marks black renewals, separated by3 or5 white-clock samples. The sparse variable is q, not its complement. The new exact identities are

    x_-12(2s)=q_(s+2) q_(s+5),
    x_-12(2s+1)=q_(s+4) OR q_(s+6).

Thus for an interior renewal r>=2, x_-12(2r-4) is1 exactly when the gap following r is S. A long gap gives0. This transports the S/L choice to a specific left cell using a nonlinear same-history product. It holds for every continuation of the synchronized family, not only GC1106's chosen loops. No all-depth transport or realized-record bound follows yet.

**Hand derivation.** Write q_i=q_(s+i), Q_ij=q_i OR q_j, and Q_123=q_1 OR q_2 OR q_3. Every product q_i q_j with0<|i-j|<3 vanishes. For paired samples (e,o), forcing one column left from adjacent right pair (a,b) gives (o_s XOR(e_s OR a_s), e_(s+1) XOR(o_s OR b_s)). The inverse wall first gives (1-q_0,1). Successive left pairs are:

| Depth | Even sample | Odd sample |
|---|---|---|
|1|1-q_0|1|
|2|q_0|q_1|
|3|1-q_1|1-q_1|
|4|0|q_2|
|5|1-Q_12|1-q_1|
|6|q_2|Q_123|
|7|1-Q_23|1-q_3|
|8|0|Q_34|
|9|1-Q_24|1|
|10|Q_24|Q_35|
|11|1-Q_35|1-Q_35|
|12|q_2 q_5|Q_46|

In the last even update, (1-Q_35) XOR((1-Q_35) OR Q_24)=Q_35 Q_24. Expanding the product kills q_3 q_2, q_3 q_4 and q_5 q_4, leaving q_2 q_5. This is precisely where the nonlinear short-gap marker remains. All formulas need only ones separated by at least3; allowed distances need not be exactly3/5.

**Controls and limits.** Record searched: column.-12/depth12/twelfth/short-gap-left with S/L/renewal/forced/selector/gap ->5 hits4files; GC1007's finite-forcing/pumping failure and GC706/784 read. No prior twelfth-left-column selector found there. Registered P1/P2 hold on41 complete length9 sparse cones and all16 four-letter S/L lifts. Every reconstructed triangle vertex passes the independent literal Rule30 table. Short-marker control001001000 refutes replacing the product by XOR. Unexpected control000000101 has no11 but a distance2 pair and refutes that weaker premise. The probe computes these local identities only, with no solver, membership or record run. A preliminary complement-marker convention was corrected before the controls. GC1007 already bars pumping this by time translation: a later left marker does not force an initial black cell farther left. Next missing inference is a depth-advancing nonlinear carrier that retains the initial-row obstruction; another finite common-cell scan will not establish it.

**CL285 receipt.** GC1106's explicit walks and entropy scope are independently confirmed; promoted. Cloud reports its existing width28 component of97 states mixes101/k2,111/k1 and111/k3, while its10-state component is pure M2; no GPT repetition. Its joint101 closure counts226 continuing packets versus our635 total retained packets, including terminal exits; keep those counting conventions distinct, with635 still GPT-computed. No extra width or realization search requested.


## GC1108 — The left12 short-marker has a lossless finite inverse (2026-10-11)

**PROVED (CL287), serves Q6's finite hidden representation.** Missing inference after GC1107: does the left short-marker forget the L choices in the mixed recurrence? It does not on the relevant paired-L language. More generally, let q mark an S/L renewal trace with no three consecutive L, and set z_s=q_s q_(s+3). Then, away from both boundaries of a finite trace (or on a continued infinite trace),

    q_s = z_s OR z_(s-3) OR [z_(s-8) AND NOT z_(s-5)].

Each term implies q_s=1: the second marks the endpoint of an S; the third marks the endpoint of the L immediately after an S. Conversely, a q marker begins an S (first term), begins an L preceded by an S (second), or begins a second L preceded by an S-L pair (third). The no-LLL premise exhausts those cases. Consecutive z markers are separated by3+5l with l=0,1,2, so the exact image has gaps3/8/13; inserting the intervening L markers proves the converse. Typed-A output has L in exact pairs, so its carrier has only gaps3/13. On Cloud's reported width28 mixed component the macro labels k=1,2,3 become carrier blocks3^k followed by13; no new graph run or actual realization assertion.

Let p_s=x_-12(2s)=z_(s+2). The inverse reads the original renewal bit from four even samples of this left column:

    q_s = p_(s-2) OR p_(s-5) OR [p_(s-10) AND NOT p_(s-7)].

Thus it uses physical lags4,10,20,14. Write this decoder as R_s(p). The full adjacent forced columns are

    x_-11(2s)=x_-11(2s+1)=1-[R_(s+3) OR R_(s+5)],
    (x_-12(2s),x_-12(2s+1))=(p_s,R_(s+4) OR R_(s+6)).

This is a concrete finite-window code of the adjacent left pair by a finite renewal alphabet, retaining the nonlinear guard. It is not yet a closed update in spatial depth. Marker deletion preserves entropy: for extendable factor counts, N_q(n)<=N_z(n+8) and N_z(n)<=N_q(n+3). Hence no information-rate gain follows from removing L markers.

**Controls.** Record searched: short-marker/left12/twelfth/13-gap with inverse/reconstruct/lossless/recover/paired/entropy ->4 hits2files; GC624/1008/1107 read.131 cyclic eight-letter controls pass, independently compared with h(S)/h(L);110 contain an isolated L, the unexpected weaker case. The original82 counted cyclic LSL (isolated S), corrected after CL287. All-S refutes deleting the nonlinear guard; SLLL refutes removing the run bound. GC1106's FE/EF give distinct234-tick left12 codes, first even disagreement at34, versus column1's44. Their common first six q samples make every left12 block independent of the next choice; complete inverse triangles agree. Arbitrary binary choices therefore survive in this left12 representation too. No solver, membership, record or wider-strip run. Next seek a depth-advancing update or obstruction for this coded pair; finite-window invertibility alone supplies neither, and GC1007's initial-row pumping failure remains binding.

CL286 independently verifies GC1107's whole sparse-cone premise and all twelve paired identities; promoted. Its failure of a weaker local no11 premise is received, not rerun. Local's342c857a RLK142 phase0 receipt is read without duplicating the computation; phase1 remains pending.


## GC1109 — The SLL prefix destroys the proposed eight-depth carrier return (2026-10-11)

**Canonical-return route refuted; universal cone certificate PROVED (CL288).** Missing inference after GC1108: can its finite-window left pair advance by repeating the same two-field template? At depths3/4 and11/12, the right column has equal even/odd samples R_s and the left column's odd sample is1-R_(s+1). Registered prediction: the same class returns eight depths later at19/20 on the admitted mixed FE output. It fails, already at physical time2. Pure M2 and M3 controls fail identically. This closes that specific proposed return, not every finite-type representation. No nearby-depth or width sweep follows.

The failure is independent of the later mixed choices. Every macro begins h(S)h(L)h(L), whose first eleven even samples are q=10010000100. The wall inverse fixes column -1 as pairs(1-q_s,1); forcing successively left through the complete22-sample triangle leaves, at depths14..20,

    14:010111001, 15:11000101, 16:0101011, 17:011110,
    18:10001, 19:1110, 20:001.

Each depth loses one terminal sample; no unknown continuation enters. Consequently every such SLL prefix forces x_-19(2)=1 and x_-19(3)=0. The inverse equation at that black cell then forces x_-20(2)=1 regardless of x_-18(2). The lost field is the even/odd phase asymmetry, and it has a definite effect on the next even sample; it cannot be discarded by the two-field return. At time0 the canonical pair still passes, the unexpected check: synchronized endpoints alone miss the obstruction.

Record searched: GC1108/canonical-pair/paired-return/eight-column/depth20 with left/carrier/renewal/inverse/S/L ->7 hits6files; GC1107/8 and GC1007 read. Independent packed circular forcing and literal Rule30 triangle checks agree; the separate finite cone proves the continuation-independent implication. Failure counts119/19/24 for FE/M2/M3 are diagnostic, not depth deadlines. GC1108's lossless finite code remains intact. After the failed closure, extracted the universal SLL phase defect instead of varying depths. Next design must transport or budget that defect together with the carrier and initial-row constraints; repeating the canonical template and translating this finite marker cannot give the all-depth bound. No record, solver, membership or larger-strip run.


GC1109 receipt update: CL287 confirms GC1108's interior inverse, decoder and carrier grammar; promoted with the finite terminal-boundary qualification. Its control-count discrepancy exposed our mislabeled LSL predicate:82 were isolated-S controls, while SLS gives110 isolated-L controls. Corrected the predicate and descriptions; all131 inverse controls still pass. No new record run or replay of Cloud's larger checks.


## GC1110 — A recurrent phase field rectifies into a positive S/L black shield (2026-10-11)

**PROVED (CL289), serves Q6's hidden representation.** Missing inference: which renewal interactions produce GC1109's dropped phase field, and what does it force in the next column? It is recurrent even without L gaps. Exact nonlinear forcing yields a positive renewal code at left20: its even-time trace has no consecutive whites, on every synchronized S/L continuation. This is a temporal shield at a fixed depth, not an all-depth record bound or a closed spatial update.

Put q_i=q_(s+i), and delta_19(s)=x_-19(2s) XOR x_-19(2s+1). Boolean substitution, reducing only products whose markers are less than3 apart, gives

    delta_19 = q5 XOR q6 XOR q7 XOR q2q5 XOR q3q6 XOR q3q7
               XOR q4q8 XOR q5q9 XOR q6q9 XOR q2q5q8,
    x_-20(2s) = q5 XOR q7 XOR q3q7 XOR q4q9 XOR q5q9
                XOR q2q5q9 XOR q3q6q9.

In S/L, markers four samples apart are impossible: separation at least3 prevents an intervening marker, while consecutive gaps are3 or5. Delete those products. The remaining four terms in the second identity are pairwise disjoint, so

    x_-20(2s) = q5 OR q7 OR (q4 AND q9) OR (q3 AND q6 AND q9).

Let b_u=x_-20(2u-14), u>=7. Partition b between consecutive renewals. A long gap gives10110; a short gap preceded by L gives101; a short gap preceded by S gives111. Indeed each renewal r supplies black samples at u=r and r+2; an L adds r+3, and an SS pair adds r+4. These are exactly the four positive terms. The three blocks start black and contain no00, proving the shield across boundaries too. In particular every renewal r>=7 forces x_-20(2r-14)=1. At that sample, column -19's pair is(1-q_(r-3),q_(r-3)), so its phase defect is1.

**Structural consequence and controls.** On all-S, delta_19 and left20's even trace are identically1. Thus this phase field cannot be budgeted as a finite set of L-induced exceptions. At an all-S window10010010010, the cubic SS term alone supplies the left20 black cell; deleting it fails. The general sparse formula also covers arbitrary larger gaps, but the positive S/L simplification requires exclusion of gap4.

Record searched: phase/ANF/polynomial/cubic/degree, sparse/Boolean/polynomial, GC1109 ->20 hits11files; G138/139 and GC1107..1109 read. Predictions precede the symbolic derivation and controls in rule30_sl_phase_collision.py. Exact Boolean-polynomial reduction and independent literal Rule30 triangles agree on all88 sparse length11 windows, including23 with a gap exceeding5 (the identified unexpected domain check), and640 phase windows of32 cyclic five-letter S/L controls. P1/P2 hold; the singleton truncation and cubic deletion fail as specified. No solver, visible-membership, record, width or nearby-depth sweep. Next missing inference is transport of this recurrent positive shield and its renewal code in spatial depth while retaining the initial-row condition; the fixed-depth code alone does not supply it.

CL288 independently confirms GC1109's universal cone and failed return; promoted. Cloud's larger finite triangle and failure counts are received, not rerun. Our119/19/24 counts sum both template failures over each entire circular FE/M2/M3 word; CL288 uses finite interior windows. The scopes differ, not the verdict. No Local or Intel job.


## GC1111 — The reported 120-symbol M2 cut would pay for the typed101 chain on the right (2026-10-11)

**Concrete derived cap; absence receipt pending.** The fixed-depth shield has no proved spatial transport yet. Switched to a specific missing inference: GC1103's typed101 recurrent output is pure M2, but Local L591 already reports the cyclic gap word 5,5,3,3,3 absent at visible length 120. This is the SAME cyclic word as M2=SLLSS, not M3. If that reported absence is confirmed with its retained word/phase receipt, every actual consecutive typed101 A-return chain has at most 23 completed returns and duration 886 ticks, independent of initial left radius J. This would replace GC1103's finite-left deadline for this subclass with a right-language deadline. It does not cover 111 reentries or general records.

**Specific inference.** One M2 return gives 19 visible samples and 38 physical ticks. Eight returns give 152 samples. They contain every length 120 cyclic factor of the primitive 19-sample period: starts 0..18 suffice, with every such factor also occurring at a strictly positive start within those 152 samples. The phase guard matters at a time 0 chain onset. A visible factor starting at original time 2r>0 has a black-phase origin at 2r-1, so every such actual factor belongs to L1 as well as L. Thus an absence in either reported phase can be used after startup; no unrecorded choice of cyclic alignment is needed.

GC1103's reviewed rank bounds non-M2 returns by 2, splitting the chain into at most 3 M2 runs. Once L591's absence is confirmed, each run has at most 7 returns. Hence at most 3*7+2=23 completed macros and at most 3*7*38+2*44=886 ticks. This excludes the pure M2 recurrent component as an actual infinite typed101 history even when it survives width 36. It leaves GC1106's mixed 111/101 recurrence unresolved.

Record searched: SLC3/macro-SLL/typed-cut/GC1106 with intersect/cut/language/cycle ->15 hits in 9 files; SLC2/5,5,3,3,3 with 120/period/cycle ->1 hit in 1 file. L591 and the SLC header report the absence but provide no exact 120 word, tested phase or verification receipt in git; the retained cut file is unavailable here. Requested that existing evidence from Local, with no new membership or solver run. Controls in rule30_m2_reported_cut_cap.py compare independent gap and physical h spellings, all 19 cyclic factors and the positive-age cover. Eight periods pass; seven miss 5 factors (counterfactual refuted). The identified unexpected check is the unavailable time-1 origin, repaired by the positive-age occurrence. The reviewed rank was reused, not recomputed. No verified absence is claimed by this probe.

CL289 independently confirms GC1110's polynomials, positive renewal code and scope; promoted without rerunning its larger controls. Next: receive the specific retained cut/phase certificate and inspect existing SLC cuts against the mixed macro output; the two public length 42 cuts contain LLL and are inert on this paired-L output. No new layer widening or realization search.


## GC1112 — The mixed recurrence overlaps pure M2 for exactly 87 visible samples (2026-10-11)

**Hand proof and finite ranking certificate; second review pending, serves Q6.** Missing inference: can GC1111's reported 120-symbol M2 absence also cut the reviewed mixed recurrence? It cannot on its own. Every pure-M2 factor of length at least 88 is absent from the entire arbitrary-concatenation language of GC1106's two generators FE and EF. Adding any collection of these M2-only cuts therefore leaves that explicit model's binary branching intact. A minimized M2 cut of length at most 87 could still act on it; the retained L591 receipt remains necessary. Intersection with the other retained SLC cuts remains unassessed here and belongs to Local's lane. This concerns a sound obstruction in the joint21-cell relaxation, not actual right-half membership or the all-depth record bound.

**Marker-spacing proof.** A macro M_k spells SLLS^k, has visible duration 13+3k, and has exactly one LL triple: three black markers with consecutive gaps 5,5, starting three samples after its onset. Consecutive LL triples are separated by 16, 19 or 22 samples for k=1,2,3. The generators' k words are FE=(3,1,2,2,2,3) and EF=(1,2,2,2,3,3). Both end in 3; neither starts in 2. Hence every run of three 2s is exactly the interior of E, preceded by 1 and followed by 3, and no run of four 2s occurs across any generator boundary.

An 88-symbol factor of the periodic M2 word contains at least four complete LL triples: their starts are 19 apart, and a length-11 triple fits in 78 possible starting positions. Four such triples force three consecutive k=2 macros. Let T be the first of those macro onsets. The matching M2 phase is then fixed. In the preceding k=1 macro, the nearest mismatch is T-6: M2 has a marker, the mixed word does not. After the three M2 macros, k=3 starts at T+57; the first following mismatch is T+82, where the mixed word has a marker and M2 does not. Both statements are independent of the next macro because its first three-gap S is fixed. The entire intervening interval [T-5,T+81] agrees, and has length 87. Any 88-symbol window containing the four LL triples must include one of those mismatches, contradiction. The 87-symbol interval in E attains the bound.

**Independent all-length check.** rule30_mixed_m2_overlap.py constructs the complete matching product of both 117-sample generator spellings with all 19 M2 phases, including every possible bit start and every choice-boundary crossing. Its 2,718 matching states admit a locally verified integer rank at most 87 falling by at least one on each edge. Every matching factor yields a path with one state per symbol, so the certificate bounds every length, rather than extrapolating a finite scan. Gap-marker spellings agree with independent even samples of h(S)/h(L); a separate cyclic EF control attains 87. The negative self-period product has a cycle. The identified unexpected check is partial LL triples and unaligned factors at FE/EF boundaries; these are included in both the counting proof and product graph. P1 (no 105-factor) and P2 (sharp 87) hold; the claim that the reported 120-factor alone destroys mixed branching is refuted. No membership, solver, relaxed-record, width or realization run.

Record searched: M2/M_2/LLSSS with longest-factor/common-factor/cut-FE/matching-factor ->9 hits in 6 files; relevant GC1103/1106/1111 and the existing exact macro-cut translation read. Next use Local's retained minimal M2 cut to determine whether it is short enough, or contains a different mixed-output factor, to address this surviving obstruction. L625/L626 and their correction at b41ffe83 received and ACKed; nothing requested of GPT in those receipts.


## GC1113 — The bare mixed bridge survives long M2 cuts; the reported cut would charge its optional waits (2026-10-11)

**Hand proof and finite certificate; second review pending, serves Q6.** Missing inference: which part of the mixed recurrence can GC1111's M2 absence pay for? GC1106's optional B loop can be erased. Its reviewed A-to-B and B-to-A connectors have durations 32+38 and 38+44, returning to the same full joint21-cell endpoints and wall phase. Their bare concatenation E_0 takes 152 ticks. Inserting m copies of the reviewed 38-tick B21=0 self-loop gives E_m with k word (1,2^(m+2),3) and duration 152+38m. Full boundary memory is retained; loop erasure is licensed by the same 21-cell B state and even duration, not only by its 20-cell projection. No new path or strip search is needed.

F E_0 and E_0 F are distinct 196-tick closed walks at A, first differing at physical tick 44. Arbitrary choices therefore give model entropy at least 1/196 bits per tick. Their longest factor shared with pure M2 is exactly 68 visible samples. Consequently every collection of pure-M2 cuts of length at least 69 leaves this bare mixed branching intact. This improves GC1112's threshold of 88 for the unnecessarily delayed E_1 witness. Intersection with other retained SLC cuts is unassessed; actual infinite right-half lifting and the all-depth record bound remain open.

**Parameterized overlap and the specific waiting charge.** For any fixed m, both generators end in k=3 and neither starts in 2, so the only run of m+2 consecutive M2 macros lies inside E_m, preceded by k=1 and followed by k=3. Let T be its onset. The nearest mismatches with its aligned M2 period are T-6 and T+19(m+2)+25. All intervening samples match: the interval [T-5,T+19(m+2)+24] has length B_m=68+19m. A putative matching factor of length B_m+1 contains at least m+3 complete LL triples (length 11, starts 19 apart), forcing this entire M2 run and its phase; it must then include one of those mismatches. This proves the sharp all-length bound. At m=0 it is 68, independently certified by a complete falling-rank product for all bit starts and all FE_0/EF_0 choice boundaries.

At m=4 the matching interval has length 144 and contains all 19 distinct length-120 M2 factors; its first sample is at visible age 11 within E_m. Thus the positive-age phase guard is automatic. On confirmation of L591's reported absence, every actual bridge of this named form has m<=3 and duration <=152+3*38=266 ticks, independently of the tested cyclic alignment or phase. At m=3 the interval has length 125 and covers only 6 of the 19 factors, so that smaller uniform threshold fails. The charge bounds optional waiting, not the number of reentries: the undelayed E_0/F model still branches. No verified absence or whole-SCC deadline is claimed.

Record searched: GC1106/M2/M_2/SLLS with loop-erasure/196/overlap68/connector152/minimal-connector ->5 hits in 4 files, all unrelated. Reused the reviewed joint witnesses; no discovery rerun. Predictions in rule30_minimal_mixed_bridge.py precede its controls. Gap markers and independent physical h spellings agree; the complete bare product has verified maximum rank 68; literal cyclic containment independently confirms the 6-versus-19 rotation counts. The identified unexpected check is full endpoint and wall-phase preservation on loop erasure. P1/P2 hold; optional-loop necessity is refuted. Next assess Local's retained minimal M2 cut against the stricter threshold 68, or use an existing non-M2 SLC cut that actually touches the bare connector. Proof review and evidence requests are retained while publication is unconfirmed.

## GC1114 — The exact verified M2 cut gives a sharp 672-tick typed101 grammar bound (2026-10-11; corrected GC1116)

**Hand proof and finite certificate; second proof review pending, serves Q6.** L627 certifies f=(00001 00001 001 001 001)^6 absent in both phases. The originally recorded 620-tick/16-macro calculation used the ONE-SAMPLE rotated marker-start word from h, not this gap-ending word. That combinatorial calculation did not establish absence of its tested rotation. GC1116 caught the mismatch before this application was published. The prediction that correcting the phase would leave620/16 unchanged was REFUTED. Recomputing with the exact114 certified bits gives18 completed macros/672 ticks, independent of J. This is a correction, not a claim that cyclic rotations inherit finite-word absence.

For q=h(M2)[::2], f=(q[4:]+q[:4])^6. GC1103 bounds exceptional k!=2 macros by2 in a typed101 chain. Seven M2 macros contain f, so a terminal run has at most6. Six M2 followed by any further macro contain f, since all macros have the same first four samples. Thus before M1 there can be at most5. Five M2 followed by M3 and any successor contain f, using the successor's first marker; hence before a nonterminal M3 there can be at most4. A terminal M3 may retain5, just as a terminal M1 may.

If the word ends in M2, split it into at most two exceptional blocks (preceding run plus its exceptional macro) and the final run. An M1 block costs at most5*38+32=222 ticks; an M3 block at most4*38+44=196. The final run costs at most6*38=228, giving672. If it ends exceptionally, its terminal block costs at most5*38+44=234 and its preceding block at most222, below672. The count bound is5+5+6+2=18. The grammar word (2^5,1,2^5,1,2^6) avoids f and attains both maxima; this is grammar sharpness, not actual CA realization.

**Actual mixed bridge charge requires its endpoint.** E_3=(1,2^5,3) alone avoids the corrected cut. Appending its fixed endpoint marker1 contains f starting at visible20, with the last bit at the A endpoint. Every actual E_m bridge ends at this same A marker, so E_3 remains forbidden and m<=2, duration<=228. E_2 plus its endpoint avoids f. Omitting the endpoint would lose this inference. The bare196-tick generators still branch; overlap68 is shorter than either verified M2 cut.

rule30_fixed_m2_cut_charge.py now uses the exact L627 bits and verifies all43 reachable prefix/exception states by weighted and count ranks672/18. Every transition, including rejected ones, passes independent literal suffix matching. The extremal grammar word and bridge endpoint controls pass. The original predictions and failure are retained in its header. The absence premise is Local's cake_lpr computation (L627), read at4b22d445 and not rerun; the charge awaits its second reader. No all-depth bound or deadline for arbitrary111 reentries is obtained.

## GC1115 — The positive left20 code has a finite causal inverse on the mixed grammar (2026-10-11)

**Hand proof; second review pending, serves Q6's hidden representation.** Missing inference: GC1109's canonical phase return fails, and GC1110's left20 even trace becomes dense. Does that phase obstruction erase the recurrent mixed choices, or require a different finite language representation? It retains them. Reuse the proved b_u=x_-20(2u-14), u>=7, with renewal blocks L:10110, S after L:101, S after S:111. If ell_r marks a renewal whose following gap is L, then

    ell_r=(1-b_(r+1))(1-b_(r+4))(1-b_(r+6)), r>=6.

This nonlinear detector is exact on every S/L continuation. Each L renewal r contributes zeros of b at r+1,r+4,r+6; the last is supplied by the next block and may coincide with the next L's first zero. Consecutive L renewals separated by k short gaps have distance 5+3k. The zero-gap list is therefore 3,2 followed by a gap 3k when k>0; at k=0 the third zero is shared with the next block. The consecutive-zero signature 3,2 occurs only at the first zero of an L block. No intermediate zero can hide within either tested gap, since all zero gaps are at least 2. This proves the detector, including isolated L's.

**Bounded past decoder.** GC1106/13's mixed grammar has at most four consecutive S's: every M_k=SLLS^k ends with at most three and the next macro begins with one. Thus successive L renewals are at most 17 samples apart. For u>=22 let J_u be the smallest j in 0..16 for which ell_(u-j)=1. It exists, identifies the latest L renewal, and

    q_u=1 exactly when J_u is in {0,5,8,11,14}.

The latest L starts at distance 0, followed by its first S renewal at distance 5 and further ones every 3 until the next L. Taking the latest L is essential: an older L could falsely predict a marker inside a later long gap. The decoder needs only b_[u-15..u+6], 22 even samples. In physical time these are x_-20 at times 2u-44,2u-42,...,2u-2, strictly before q_u=x_1(2u). At the first guarded target u=22 the observations are times 0..42 and the target is time 44. This supplies a concrete finite past representation beyond the failed canonical phase template. For example the named 114-symbol M2 predicate pulls back to a 135-sample b predicate through this decoder; its CA-absence receipt remains unread.

**Scope and the specific obstruction to iteration.** Without the bounded-S guard, phase-shifted all-S traces have distinct q and identical b=1 everywhere, so this inverse cannot cover all S/L. Even under the guard, b contains 11, and when an L occurs its complement has black-marker gap 2 (zeros r+4,r+6 of b). Neither bit presentation is again an S/L visible trace. The inverse therefore preserves mixed information but does not close a depth iteration; a decorated image language and its evolution are still required. It gives no initial spatial record bound or infinite right-half lift.

Record searched: GC1110/left20/depth20/column20 with decoder/invert/recover/zero-3-2/recognition ->5 hits in 5 files, unrelated. Reused GC1110 and the earlier sparse left12 inverse; no polynomial derivation or depth scan repeated. rule30_sl_positive_code_inverse.py independently compares positive blocks with literal Rule30 inverse triangles on 1,536 phase samples, and verifies the decoder on 1,398 samples satisfying no S^5, including 29 isolated-L and 6 four-S controls. Physical h spellings separately fix q. P1/P2 hold; unbounded-S inversion is refuted. The identified unexpected check is failed bit/complement image reuse despite the lossless inverse, preventing a false closure claim. Next retain L-marker age in a decorated image state when testing depth evolution; no unguarded canonical return or unary/affine explanation is revived.


## GC1116 — Paired renewal age carries left20/21, but spatial forcing exposes the next gap choice (2026-10-11)

**Hand structure and exhaustive finite interface certificate; second review pending, serves Q6.** Missing inference: GC1115's nonlinear inverse retains the mixed choices, but can its latest-L age represent the full paired trace and evolve in spatial depth? For the full mixed macro grammar M_k=SLLS^k, k=1..3, the answer is concrete: 22 temporal states carry both phases of columns -19,-20,-21; column -22 requires the current temporal edge, giving 24 states for this interface. No uniform finite-state closure is proved.

The L renewals occur in pairs. Write A_i, i=0..4, for age after the first L, and B_i, i=0..16, after the second. A4 goes to B0. At B10 and B13 choose either A0 or the next B age; B16 goes to A0. All other edges increment age. The second-L to next-first-L distance is 11,14 or17, corresponding to two, three or four intervening S gaps. Conversely every bi-infinite path in this graph gives precisely this macro grammar up to time shift. The graph is strongly connected, so every finite path has two-sided extension. At A_i the q marker is1 only at i=0; at B_i it is1 for i=0,5,8,11,14. GC1110's dense b emission is0 at A1,A4 and B1,B4,B6, and1 elsewhere.

At state s at visible time u, define e_d=x_-d(2u-14), o_d=x_-d(2u-13). The q window [u-7,u+3] is determined by s: the preceding S train fixes the past around a first L, and future gap choices at B10/B13 agree through the next three samples. Thus literal forcing supplies node functions for paired19/20. For a temporal successor v the paired inverse equations are

    e_(d+1)(s)=o_d(s) XOR (e_d(s) OR e_(d-1)(s)),
    o_(d+1)(s,v)=e_d(v) XOR (o_d(s) OR o_(d-1)(s)).

Both successor b=e20 emissions at B10/B13 are1, so paired21 is still a node function. But e21(A0)=0 and e21(B11)=e21(B14)=1. At either branching state paired20=10 and paired21=11; hence e22=0, while o22=1 on the reset edge and0 on the continue edge. All other states have one successor. Retaining the current edge therefore gives a sound full paired22 emission on all24 edges; it does not give a closed update rule for further spatial columns.

**Identified counter and meaning.** The local source windows at either branch are001001001000 and001001001001, indexed from u-7 through u+4. They agree through u+3 and differ only at u+4, with paired22 outputs01 and00. The newest-source bit has coefficient1 in the literal inverse cone; the obstruction is the next L-pair gap decision, not a lost renewal marker or an affine fitting error. This counters current-age spatial closure specifically. It does not refute other finite hidden representations or all finite-type routes.

Record searched: the GC1115/renewal-age and paired-left20/image-closure searches recorded in the probe found no existing age interface. rule30_sl_age_spatial_interface.py checks all44 length12 local graph paths, every centered node and edge, against independent Rule30 truth-table parent lookup and the paired equations. Original physical h spellings of all27 macro triples independently give exactly the same local q language; no new CA membership search. P1/P2 hold. The unexpected check is identical future markers through three samples despite an undecided reset, with the fourth sample exposed exactly by odd22. Next assess whether these future gap decisions can be charged or merged under the already verified non-M2 cuts; merely adding longer future queues is not an all-depth certificate.

**Receipt adoption and delivery recovery.** Fetched and read L627 at4b22d445 and L628 at16d037d8, including their M2C source and CL291/292. Local's cake_lpr-verified absence of the EXACT f=(LLSSS)^6 in both phases discharges the corrected GC1114 application premise: every actual completed typed101 chain has <=18 macros/672 ticks, and every actual named E_m bridge has m<=2/228 ticks. The exact pattern alignment correction is detailed in GC1114; its old620/16 application is withdrawn. This is a hand/certificate bound awaiting its own second proof review; actual absence is Local's verified computation, not rerun here. L628's second cut explains CL292's rotation correction; no blanket length120 absence is used. The bare mixed model still branches because its overlap68 is shorter than either cut. Both receipt flags ACKed. One bounded fetch succeeded; publication is being resumed in the existing branch. No prize or all-depth record bound is claimed.


## GC1117 — The left22 even image visibly marks L pairs and retains phase through unbounded S trains (2026-10-11)

**Hand proof, independent literal controls; second review pending, serves Q6's hidden representation.** Missing inference after GC1116: is its exposed future gap choice a loss of renewal information that could pay for a record bound? The even field instead preserves the exact pair renewal code, including unbounded short trains. This uses the already derived left22 interface; no new depth sweep or canonical return test.

Let q_u=x_1(2u) be a trace with L's in pairs, separated by at least two S gaps, and c_u=x_-22(2u-14). Write r for a FIRST L renewal. The interval to the next first L has length13+3k, k>=1, and its c block is

    C_k=0111110111010110 (110)^(k-1).

This holds at every interval length, not only k<=3. To see the extension, the literal inverse cone for c_u uses exactly q_[u-7,u+3]. At first-L age0..12, the previous pair's L markers lie outside its past boundary and the next first L (at least16 away) lies outside its future boundary, so the finite prefix is fixed. At ages13 through the sample before the next first L, the cone agrees with a pure-S marker trace: its past excludes the second L at age5, and its future sees no missing marker until three samples after the next first L. Literal forcing there repeats110. Thus inserting any further S gap adds exactly110; boundary cases remain fixed. The 13-position prefix and three pure-S phases are finite truth-table identities, checked independently in the probe.

Each C_k begins and ends0 and has no internal00. Consequently FIRST L's are exactly

    eta_r=(1-c_(r-1))(1-c_r)=1.

This equality conserves the number and positions of L-pair renewals through this interface. The image interval lengths16,19,22 identify k=1,2,3 in the mixed grammar, and13+3k identifies arbitrary k. A full finite presentation of the larger paired-L image uses prefix ages0..14 and a three-state tail15,16,17: at tail15 reset to age0 or continue to16;16 goes17 and17 returns15. Its18 states permit arbitrary k>=1 and the pure-S limit. This is an explicit fixed-depth language, not a spatially invariant graph.

**A finite past inverse without a maximum S-run.** Among eta_(u-j), j=0..11, at most one is1. If it exists, q_u=1 exactly when its age is0,5 or10. If none exists, q_u=1-c_(u-1). At age12 this last rule gives0; from age13 onward the110 tail carries the short-renewal phase. It also recovers all three pure-S phases when there are no L pairs anywhere. Thus q is a13-sample past function of c_[u-12,u], even without the no-S^5 premise needed for GC1115's dense left20 inverse. For u>=19 the physical observations are at times2u-38,2u-36,...,2u-14, all before target2u. The first guarded target time38 uses observations0..24. No phase is silently guessed on a long short-gap train.

Record searched: left22/column22/paired-L with markers/00/recoding/inverse/renewal found11 hits in6 files, principally GC1116; the specific13-past/block-word search found2 unrelated paragraphs. rule30_sl_pair_marker_code.py compares original physical macro spellings against independent Rule30 truth-table triangles on1782 phase samples (all27 mixed macro triples and two long-S controls), including738 samples without a recent pair marker. Both predictions hold; all three pure-S phases remain distinct. The identified unexpected outside-premise k=0 control ALSO decodes; it is recorded, without enlarging the proved guard. This extends the marker decoder to unbounded short trains and closes the particular phase-erasure question. It does not bound initial spatial records or prove an all-depth image invariant. Next require a genuinely restrictive joint-phase or visible-language condition on this conserved code; counting its pair resets as dissipated branch events would be false.

CL294 atdd85a32a independently confirms GC1112..1116. GC1114's corrected exact-cut672-tick/18-macro and endpoint-sensitive228-tick bridge bounds, GC1115's interior detector/inverse, and GC1116's branch obstruction are promoted. Cloud's larger controls and finite-five-generator overlap checks are received, not rerun; our all-length overlap certificates remain separately attributed. No new Local computation is requested.

CL295 at4ce0358d independently confirms GC1117's blocks for k=1..4, interior00 detector,3542 past-inverse checks and all three pure-S phases. GC1117 is promoted; the all-k tail argument remains the stated hand extension, independently checked only at those four k's. The final three padding samples are outside the detector's future-cone guard.
