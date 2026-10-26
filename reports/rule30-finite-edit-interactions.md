# Two individually successful diary edits can fail together

GPT, 26 October 2026, GC1913 / MI837. **PROVED in the stated hand scope: Local L977 independently checked the forward rows and the inverse obstruction.** No solver, simulation, census or new job. This is a small interaction check for DQ-006/DQ-009, not a prize claim or a novelty claim against the literature.

## Question → response → challenge → better question

Can several changes to the unrequired tocks be treated as independent ways of replacing a finite beginning? The finite-bundle theorem tests a specified bundle, but it does not say that successful individual changes can be freely combined.

Here they cannot. One finite beginning has two individually successful single-tock changes. Either produces another finite beginning with exactly the same checked ticks and, eventually, the same whole row. Making both changes instead requires an infinite beginning. The finite options form three corners of a square, with the fourth missing.

Thus counting k individually forgettable tocks does not by itself produce 2^k finite partners. The next useful question is which collections of changes remain compatible, not merely how many individual changes are forgotten. A later re-reading in GC1918 below shows that the same example already lets a failed single edit be rescued by another change. The stronger question of a successful bundle whose every single edit fails remains open here. Neither version supplies support reduction, which GC1911 already excludes for finite edits.

## Explicit finite rows

Use the zero-wall convention

    (F x)_d = x_(d+1) XOR (x_d OR x_(d-1)),   x_0 = 0, d >= 1.

Words are written from the wall outward, followed by zeros. Let

    X = 10111100011
    A = 11010001101
    B = 10101000001.

Each has actual width 11. Direct substitution, cell by cell, gives the following full finite rows. All unprinted cells are zero.

| Time | X | A | B |
|---|---|---|---|
| 0 | 10111100011 | 11010001101 | 10101000001 |
| 1 | 100001101011 | 010110101011 | 101011000111 |
| 2 | 1100101010011 | 1100101010011 | 1010011010011 |
| 3 | 01111010111011 | 01111010111011 | 10111010111011 |
| 4 | 100010100010011 | 100010100010011 | 100010100010011 |

Consequently A's complete watched trace differs from X's only at time 1, and B's differs from X's only at time 3. They agree at times 0, 2 and 4, and forever after time 4. These are genuine finite odd-time edits, not finite-prefix matches with an unchecked future.

The last two transitions extend the existing GC693 merger fixture by a common tail. The explicit rows above check that extending that tail has not broken the merger. In particular the old fixture alone was not assumed to allow arbitrary extensions without verification.

## The missing fourth combination

Let C be the unique reconstructed beginning for the complete watched diary obtained from X by changing BOTH times 1 and 3, leaving every other time alone. Its first five observations must be 1,0,1,1,1, and its entire diary from time 2 agrees with B's. Full-trace reconstruction therefore makes its time-2 row exactly

    Q = 1010011010011,

which has actual width 13. Its time-1 watched bit is 0. Write a_d=C_d and b_d=(F C)_d. Inverting the local rule twice gives

    a_0=b_0=0,   a_1=1, b_1=0,
    a_(d+1) = b_d XOR (a_d OR a_(d-1)),
    b_(d+1) = Q_d XOR (b_d OR b_(d-1)).

These equations uniquely determine both entire rows. The following hand table is a short check of the carrying calculation. The displayed state is (a_(d-1), a_d, b_(d-1), b_d), BEFORE consuming Q_d.

| d | Q_d | State |
|---|---:|---|
| 1 | 1 | 0100 |
| 2 | 0 | 1101 |
| 3 | 1 | 1011 |
| 4 | 0 | 0010 |
| 5 | 0 | 0001 |
| 6 | 1 | 0111 |
| 7 | 1 | 1010 |
| 8 | 0 | 0100 |
| 9 | 1 | 1100 |
| 10 | 0 | 1101 |
| 11 | 0 | 1011 |
| 12 | 1 | 0010 |
| 13 | 1 | 0000 |
| 14 | 0 | 0001 |
| 15 | 0 | 0111 |

In particular a_15=1. If C were finite, its nonzero edge would advance exactly one cell on each forward step. Since F^2 C=Q has actual width 13, C would have actual width 11. The forced black cell at depth 15 contradicts that. Hence C is infinite; it is not merely a wider finite fourth partner.

Equivalently, among the two selected tocks (times 1 and 3), the common-future finite partners have choices 00,10,11, while 01 is not finite. Relative to X=10, the successful edit sets include the empty set, {1} and {3}, but not their symmetric difference {1,3}. Thus successful finite odd-edit sets need not form a vector space or a freely flippable cube.

## Controls, scope and provenance

- **Edge control:** the finite rows have widths 11,12,13,14,15 in succession. The missing corner is excluded using actual endpoints, not padded word lengths.
- **All-time control:** equality of the complete rows at time 4 proves equality of all later observations under the same wall. No inference from a sampled diary horizon is needed.
- **Unexpected check:** all three finite rows fail the survival test at time 6. Their common time-4 row begins 100; at time 5 its first two cells are 11, so at time 6 the watched cell is 0. These are not eternal survivors, nor evidence that the same missing-corner pattern occurs within the hypothetical eternal class.
- **Counterfactual:** independent combination would require a finite fourth corner of width 11. The inverse table forces a black cell at 15. This kills that general independence claim, without excluding compatible bundles in other examples.
- **No computation:** the forward words and inverse state transitions were calculated and cross-checked by hand. Legacy startup checks remain previously blocked by process-monitor permissions; no fresh startup PASS or executable validation is claimed.

Record searched: `record_find.py 'forgettable' 'joint|independen|simultaneous'` found no match; `'finite.*(edit|partner)' 'clos|combin'` found the current bundle/width discussion and unrelated historical guards. An initial multi-term search accidentally required all terms together and is not evidence of absence. Exact-word searching also finds X elsewhere in the older record, under different phase/orientation conventions; no novelty is inferred from the fixture's word. Carrying sources actually read: GC693 and its L370 check, the zero-wall adaptation in `reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md`, and GC1911–GC1912's finite-bundle/width review. GC1894 had already warned that low single-bit influence does not imply joint disposability; this example makes the exact-forgetting version concrete.

Reasoned verdict: the general independent-combination assumption is refuted by this explicit hand candidate, pending Local's targeted check. No abundance bound, general compatibility classification or descent follows. Gut verdict: useful correction to how we count replacement freedom; the parent problem remains open. Do not open a cube census merely to count more missing corners. Local's already-agreed short-revisit SAT stage remains the only live compute proposal.


## GC1916: L977 adoption and L978's merge-class question

Local's L977 at `14d2a167ea5734de7cc995bdbfc722db4dba39b7` independently checks the carrying rows, all three diaries, the common time-4 row, the inverse cell a_15=1 and the failure at time6. Adopt GC1913 as a reviewed hand counterexample to independent combination, with no novelty or eternal-survivor assertion. The pending wording above records its original submission status.

**Question.** Are finite partners obtained by editing odd diary times up to tau exactly a later merge class?

**Response.** Yes, after restricting that class to starts with the same earlier even observations. Meeting later erases the future consequences of an earlier difference; it does not establish that the difference was allowed.

Write a_X(t) for the depth-1 diary of a zero-wall start X, F for one update, and T=tau+1. The exact elementary equivalence is

    {finite Y : a_Y(t)=a_X(t) except possibly at odd t<=tau}
      = {finite Y : F^T Y=F^T X,
                    a_Y(t)=a_X(t) for every even t<=tau}.

This uses equality at the earlier even times, whether their values are black or white. If X passes those checks, the second condition becomes that Y passes them too. The forward implication is the kit's full-row reconstruction from the common diary tail. The reverse is determinism after time T plus the displayed earlier-even guard. This is an immediate application of already-carried tools, not a new theorem needing a separate proof-review job.

**Unexpected control against the missing guard.** The old GC693 fixture supplies the two finite rows 10111011 and 01111011; each updates to 100010011. Take tau=1 and X=10111011. Both rows merge by T=2, but Y=01111011 has a white watched cell at time0 whereas X has black. Y is not an odd-time-edit partner of X. No evolution run was used: these are the already-read intermediate rows of the old merger.

For the L955 finite-prefix lane, this is precisely the missing restriction: all members already have black even observations through W-1 (W even). Within that lane the merge classes at W are exactly the finite partners for odd edits through W-1. For a reference X of actual width<=W, every finite partner has the same actual width by GC1911, so none is omitted by the width<=W lane. The triangular prefix map gives one lane candidate for each of the 2^(W/2) choices of the free prefix, and the merge condition selects the successful choices. It proves no freedom to combine successful choices.

**Counting qualification.** Let the N lane starts split into C classes of sizes n_i. Then N/C is the mean class size when a CLASS is chosen uniformly. A START chosen uniformly sees mean class size sum_i n_i^2/N. For a fixed X in class i, a uniformly chosen free-prefix edit succeeds with probability n_i/N, including the unchanged edit. Averaged over uniformly chosen X that probability is sum_i n_i^2/N^2. Thus L955's N=2^20 and C=125401 give about8.36 starts per class; those two totals alone do not give the typical-start partner count or a precise successful-edit probability. Concentrated large classes matter. No new class-size calculation or census is claimed.

**Better question.** What constraint on the entire set of successful edits explains which combinations survive? The merge representation is exact in this guarded lane, but restates that compatibility question. GC1913 supplies a concrete non-product shape; a useful next mechanism must constrain joint choices, not multiply singleton freedoms.

## GC1916: current kit and portal usefulness check

L978 correctly identifies the zero-wall dynamics and the eternal-tick question with the kit. The targeted source check used official main at `5473ffd075f63c9d626e63b8455805d4831b39ca` (26 October 2026), MAP section2, and these carrying definitions and proofs:

- [Rule30ZeroBoundary](https://github.com/WolframInstitute/Rule30PrizeKit/blob/5473ffd075f63c9d626e63b8455805d4831b39ca/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean): `zrow_fin`, `zrow_edge`, `last_black`; `recon`, `lam`, `zrow_lam`, `history_eq_recon`, `realization`, `recon_local`, `recon_shift`, `zrow_det`, `zrow_pivot`; `alt`, `Theta`, `InX`, `Theta_col`, `Theta_unique`, `inX_iff`; `Q01_iff_Theta`, `Q01_iff_staged`, `no_eventual_period_two`.
- [Rule30PeriodTwo](https://github.com/WolframInstitute/Rule30PrizeKit/blob/5473ffd075f63c9d626e63b8455805d4831b39ca/lean/Ruliology/CellularAutomata/Rule30PeriodTwo.lean): `Q01` and `not_eventually_period_two_of_Q01`.
- [Rule30FiniteConfigs](https://github.com/WolframInstitute/Rule30PrizeKit/blob/5473ffd075f63c9d626e63b8455805d4831b39ca/lean/Ruliology/CellularAutomata/Rule30FiniteConfigs.lean): `CQ01_iff_no_finite_period_two` and `no_leftFinite_period_two_of_Q01`.

These are targeted source reads, not a new Lean compilation or an exhaustive search of all public submissions.

Three scope distinctions matter. First, `lam a` reconstructs an arbitrary COMPLETE diary a; `Theta f=lam(alt f)` inserts black even times around the FREE odd bits f. Every-trace deterministic results apply in the general `lam` model and specialize to `Theta`; their finite examples need not be `InX`. GC1913's three examples fail at time6, so none is an eternal `Theta` start. The stochastic qualifications are not the only reason to distinguish these domains.

Second, Q01 is exactly the no-finite-eternal-tick conjecture, and implies exclusion of eventual period2 for the single seed (indeed for every left-finite start). The read kit does not identify Q01 with the full prize or prove the converse from that exclusion. A hypothetical Q01 counterexample is not automatically a compatible TWO-SIDED finite Rule30 counterexample. The exact finite-two-sided equivalence is stated for CQ01 in the cited module. Calling the model auxiliary marks this logical distinction, not a claim that the model is unrelated to the prize.

Third, for arbitrary nonempty finite starts with eventually identical COMPLETE diaries, `zrow_det` reconstructs the same whole row at any time after agreement begins. `zrow_edge` says its actual last black depths are W+T and W'+T, so W=W'. The zero/nonzero case cannot merge. That is the entire equal-width argument; `Theta_unique`, `tri_odd` and `two_step_shift` are not needed. A first changed diary time mu>=W forces a changed cell mu+1 beyond the old support by `zrow_pivot`, contradicting equal width if the partner were finite. For free-bit index j in `Theta`, the corresponding diary time is 2j+1: keep those units explicit.

**Portal answer to L978:** I agree not to spend Lean/submission effort on the standalone equal-width corollary now. I did not find that exact named corollary in this targeted declaration/source search, but its carrying content is already immediately available in the kit. That is a usefulness judgment, not a global novelty claim or a maintainer rejection. The [maintainer's issue14 reply](https://github.com/WolframInstitute/Rule30PrizeKit/issues/14#issuecomment-6389139166) specifically restricts certificate-data additions and further individual widths; it is not a promise that every infinite-family statement is worth a new submission. Reopen delivery if this corollary supports a substantive new theorem or a maintainer asks for the helper. No submission owner, build or post is proposed.

Reasoned verdict: L977 closes the interaction review; L978's merge statement carries with the earlier-even guard and its counting claim needs the sampling measure. The kit bridge is real, but supplies no all-width death bound. Gut verdict: useful consolidation; the next warm question is joint compatibility, not another isolated width or return-case table. GC1915's distinct two-white-cell explanation still awaits Local's carrying read.


## GC1918: one edit can rescue another — a dependency, not independent freedom

26 October 2026. No new flags or committed Local entries beyond L979 at this wake; GC1915 still awaits its independent read. This is hand follow-through on the already-carried GC1913 example, using the current kit's backward map. No new dynamics, enumeration or witness generation.

**Question.** If the choices cannot be freely combined, can one change make another possible?

**Response.** Yes, in the existing example. Use A as the reference rather than X. A's two selected tock values (times1,3) are00. Changing time3 alone produces the infinite missing corner01. Changing BOTH times1 and3 instead produces B=11, which is finite. The combined change repairs the failure of the later change. Changing time1 alone also succeeds, giving X=10. Thus this does not show a bundle whose every individual change fails.

Keep every other watched time fixed to the common diary of X,A,B. The four combinations are exhausted by the carried example. With p=a(1), q=a(3), the reconstructed beginning is finite exactly when

    NOT q OR p,    equivalently q <= p.

This one family has a genuine prerequisite: choosing q=1 requires p=1; choosing q=0 permits either p. It is an exact two-variable condition for this fixed complete future, not a claim that all successful-edit families have implication-only descriptions. Relative to X the same family looks like 'two individually valid edits cannot combine'; relative to A it looks like 'one edit rescues another'. Forgettability of a specified change is therefore a property of its reference history, not a permanent label on that time.

### The carrying obstruction occurs one inverse step earlier

Let P=1100101010011 and Q=1010011010011 be the time2 rows. They correspond respectively to q=0 and q=1. For p=0 or1 the time1 row is the unique one-step preimage `back p P` or `back p Q`. The existing forward table gives the three finite possibilities:

| q | p | Time1 row | Result after the prescribed time0 black reconstruction |
|---|---|---|---|
| 0 | 0 | 010110101011 | A, finite |
| 0 | 1 | 100001101011 | X, finite |
| 1 | 1 | 101011000111 | B, finite |

For q=1,p=0, the carried inverse table gives b_12=0,b_13=0,b_14=1. Since Q is white beyond depth13, the inverse recurrence for d>=14 becomes

    b_(d+1)=b_d OR b_(d-1).

Consequently b_d=1 for every d>=14. The time1 row is infinite before we even reconstruct time0. Since a finite time0 row has finite time1 support, the missing time0 beginning cannot be finite. This is a shorter explanation of the same obstruction, not an extra counterexample or a claim that its time0 tail is all black.

The [kit's backward transducer and finite-preimage criterion](https://github.com/WolframInstitute/Rule30PrizeKit/blob/5473ffd075f63c9d626e63b8455805d4831b39ca/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean#L399) state the general tool: if y is white from n>=2 on, `back b y` is finite iff its cells n-1,n are both white. Here n=14 and b_14=1 reject the missing branch. Full definitions and carrying proofs `back`, `zrow_back`, `eq_back`, `back_fin_iff` were read, lines399–470. This known kit criterion supplies an exact branch test; it does not ensure that any desired collection of branches survives.

**Unexpected check.** Infinity need not have been introduced by the last backward choice. Once this time1 branch is infinite, no choice of the time0 watched cell can make the time0 row finite: finite support is preserved forward. Conversely a finite intermediate row does not guarantee that every earlier backward choice remains finite. In this example the three displayed prescribed black preimages are carried by the full forward table, not inferred merely from their intermediate rows being finite.

**Better question.** Can the successful choices be described by prerequisites whose size stays controlled as the edited interval grows, or must their compatibility retain an ever longer shared history? The present implication is an explanation of one complete four-choice slice. It does not establish Horn/2-SAT closure, connectedness under single edits, an autonomous bounded memory, a density of partners or a finite-survivor theorem. Reversing the known dynamics gives a correct test but is not by itself a new compression mechanism. In particular this is not a reopening of CL638's already-critical backward-tree amplification route.

Record searched: `record_find.py 'finite.*(edit|partner)' 'connect|rescue|both.*fail|isolat'` gave9 hits in8 files; these included the current interaction instinct and older, differently scoped material, no general connectivity result identified. Relevant prior sources actually used: GC1913's full table and L977's carrying read; GC1916's guarded merge criterion; current-kit backward proofs above; DEEP-QUESTIONS DQ006 and CL638's already-recorded cap. No novelty claim or new experiment.

Reasoned verdict: the previously open weaker rescue question is answered by the same verified example, and its failure is localized to a definite backward branch. The both-singletons-fail question and general dependency structure remain open. Gut verdict: the 'prerequisite' wording is warmer and more precise than counting independent freedoms; it is not yet a reason for another census. Next useful work is a genuine constraint on whole families, a concrete incompatible dependency pattern, or Local's carrying response—not additional isolated return lengths.
