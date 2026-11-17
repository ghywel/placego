# Block 2: the outside work read against the queue and the open items — Cloud, CL752, 6 November 2026

*Block 2 of [WARM-LEADS](../WARM-LEADS.md): read `lhallee/rule30-open` and N. Berzai's paper and note against our open
items and every row of the [SW-02 submission queue](wolfram-agents/DELIVERY-QUEUE.md#sw-02-submission-queue-6-november-2026),
and mark each row known, partly known or clear. Opened in CL752 with predictions; this file is the table of matches
and the reasoning. Statuses are the sources' own labels where quoted (rule30-open: proved in Lean, computed,
conjecture, negative; Berzai: Proved, Exact, Measured, Known, Open) and the record's otherwise.*

**Sources and how they were read.** `rule30-open` at HEAD `f877f5af` (unchanged since GC2688; `git ls-remote` at
16:5x GMT): `CATALOG.md` (190 modules, 904 headline theorems, 67 findings, 75 negative results) read in full,
`README.md` and `ROADMAP.md` in full, and 79 module notes, findings, negative results and literature pages fetched by
raw URL and read where a queue row or a lead pointed; no clone, no build, no kernel receipt (GPT's GC2688 read
`WedgeLadderQ01.lean` at source; everything else here is read from the `.md` notes with their stated headline names).
Its commit dates were not read (no history without a clone); its text pins kit `932cf8d` and discusses kit main of
1 November, so its files are of early November or earlier. Berzai: repository `nateberzai-svg/rule30-left-edge` at
HEAD `d9cb3d57`; the note (15 pages, 30 September, revised 8 October) §§5–6 and the README in full; the paper (99
pages, 8 October) §§12, 17.1, 17.3–17.7, 18 to 18.1, 19, 24–26 and Remark 17.24 in full, the rest by its table of
contents and keyword search. Both disclose Claude's assistance, as this project does.

## 1. The queue rows

| Row | Verdict | Where it is known, exactly | What stays ours |
|---|---|---|---|
| S-01 Q01 ⇔ Mortality ⇔ repeat budgets | **CLEAR** | Neither source has it. `rule30-open`'s own ladder lists "`Q01` ⇒ mortality (the kit states it open)" among its open arrows (`WedgeLadder.md`); Berzai has no mortality notion | The whole equivalence (GC2690) |
| S-02 Bounded amplification, 2^3955 guarded rows | **CLEAR** for the theorem; the supply law **PARTLY** | No amplification in either source. The measured supply (reset gaps ≤ 120, BN-12) has a cousin in `settled-words.md` (largest white run of the settled words W_j < log₂ j + 6 to depth 200,000; `RunTransfer`: the reset cost of a diagonal is at most two more than the longest agreement run of the pair before it; `seed-finite-certificate.md`: one step can cost 24 by depth 200,000) | The forced twin, the reset induction, the count (GC2690); H(ρ) stays a conjecture |
| S-03 First-check bound, S_2n(2n) = 2^n(1 − p_n), two of three \|c_n\| ≤ 19/20 | **CLEAR** | No anti-concentration statement for the checks anywhere. `no-finite-certificate.md` notes that only two GF(2) parity checks hold over 14 free cells; `forced-bits-dense.md` has the degree and monomial counts of the forced bits to s = 11 and nothing on their sums | All of it |
| S-04 SEP ⇔ Q[N] ⇔ LR₁; SEP ⇒ Q01Gap; BWH ⇒ D(W) ≤ 2W + 4 | **PARTLY** | BWH ⇒ Q01 is `bwh_Q01` and Q01 ⇒ SEP is `q01_constantTailSeparator` (both Lean, GC2688). The death bound is there as a reading, not a theorem: "read through the chart, BWH at depth n is Q01 for starts of width about 2n with a time horizon about twice the width, as simulation confirms for n ≤ 12" (ROADMAP). SEP ⇒ BinaryCTS is listed open there; LR₁ and Q01Gap do not appear | SEP ⇔ Q[N] ⇔ LR₁, SEP ⇒ Q01Gap, and the proved form of the death bound; state the row against the ladder |
| S-05 ¬AbsorptionT t001 | **KNOWN** | `Traps001.not_absorptionT_t001` (Lean), as GC2688 found; also "entry into one of any three of four traps is false" (`absorption_any_excludes`) | Nothing: known, reproved (BN-L1) |
| S-06 Parity law S_2n(2n) ≡ n mod 2; degree law of the checks | **PARTLY** | Degree law: `forced-bits-dense.md` computes the forced bit u_(2s+1) as a polynomial of full degree s + 1 in the s + 1 free bits for s ≤ 11, with about half the monomials. Parity law: the swarm's record skeptic placed it in Berzai's paper in the other clock phase; my search of the paper for it found only the centre-cell degree law (Theorem 14.7), so that match stays the swarm's, unverified by me | The all-n hand proof of the degree law (XP-1.1) and the parity law as stated |
| S-07 Radius-2 family with an exactly alternating column | **CLEAR** | `rule30-open`'s sibling results are radius 1 (Rules 150 and 210); Berzai's sibling is Rule 60 with a constant column (§25) | All of it |
| S-08 Planted survivors: linear hybrid; finite-state map | **CLEAR** for both constructions | The sibling-rule planted survivor is `Analogs.Rule210.rule210_finite_half` ("a single 1 next to the column keeps the Rule 210 condition for ever"), which is the same door as our portal theorem `not_Q01_210` (R30-20261022-920c1b, 22 October); `Rule150Descent` proves the opposite for pure Rule 150 (no finite half survives, by a two-step descent) | The 90/150 hybrid with its classification and the finite-state map |
| S-09 Exact black-count law; five-column bound | **PARTLY** | `Columns.ColumnTransfer` (Lean): counts of black cells move left by at most a factor of three, by summing the pointwise left-permutivity bounds; densities d̄_(i−1) ≤ 2 d̄_i + d̄_(i+1). The exact law and the five-column bound 3T + 2 are not there | The exact law and the five-column bound; cite `ColumnTransfer` as the same method |
| S-10 Period-5 and period-7 locks; the gate trap's tail restriction | **PARTLY**: period 7 **KNOWN**, period 5 **CLEAR**, the tail restriction **PARTLY** | `PeriodTwo.SevenLock` (Lean): 195 windows of columns 1–32 closed under every input, column 1 repeats 0101000 at the white steps, `sevenLock_not_finSupp_Psi` and `no_alternating_of_sevenLock` exclude period two for every right half that enters, whatever lies beyond column 32; `gate-census.md`: 0.7–0.9% of halves to 20 cells enter it. Their census has three sets only (gap trap, ether family, lock of period seven); our period-5 lock lies inside the gap trap (CP-2.3), where their census counts it as a gap-trap entry. The tail restriction: `slip-geometry.md` has it for the empty half only (no two gaps of 3 adjacent, 17,734 gaps of 3 and 89,259 of 5 to 10⁶) | The period-5 lock; the restriction for every R (3,3 transient, 3553 and 3535353 never); the window-level identity of our 66 windows of 30 columns with their 195 of 32 is for Block 8 to check |
| S-11 The cut ether is off the seed's edge cycle | **PARTLY** | The backward half follows from `Frames.SeedPastPeriods` (Lean, extends the kit): the seed's past rows are eventually periodic to the left with periods growing without bound (`rho_not_evZero`, `rho_no_short_period`), so no finite configuration is a past row | The forward half (no c7cut N is a forward seed row) |
| S-12 p(n) − n → ∞ for free words of finite rows; near-squares | **PARTLY** in object, **CLEAR** in statement | Berzai §9 studies L(01), the language of interfaces beside the pinned column, which is the set of complemented free words of the coupled left halves: Prop 9.2 (uncountability of L(w) excludes w), Cor 9.4 (the exponential clause is not computationally dischargeable), Prop 9.7 (branching criterion), Remark 9.6 (positive measured entropy of L(01)); his p(n) = 2n to n ≤ 16 is for the centre column (Remark 14.5). Nothing per finite row | The per-row complexity rung and the near-square bound |
| S-13 Free-middle theorem; B2+ rank barriers | **PARTLY** | `conservation-laws.md`: no additive conservation law (window ≤ 12 on the orbit; all rows to k = 6; the kit's four-step theorems); `forced-bits-dense.md` cites the kit's B1, B2, B6 with their exact scopes; the kit's barriers themselves | Survival with a horizon short of the whole row (XP-3.1) and the B2+ extensions |

**The owner's M rows.** M-1 stands: `rule30-open` also lists the converse Q01 ⇒ mortality as open, so the kit's
"converse not known" is corrected by GC2690 alone. M-2 stands: `rule30-open` reads B1, B2, B6 at the modules' scope
("a ranking that decreases ... through a finite abstraction, through the width and windows, or through a finite
automaton read from the edge") and says nothing of the README rows. M-3 and M-4: neither source touches the lines.
M-5 and M-6: the portal entries 829c71, 1c93e6, c13fb2 and d75e27 do not appear in `rule30-open`'s literature pages,
which track one prize submission (R30-20261025-0554f7, Goux); Berzai cites neither the kit nor the portal. M-7
stands: `no_edge_dfa_ranking` is described there as one functional, as M-7 says.

## 2. The warm leads and the ajar doors

- **Lead 1, door 1, Block 3: the trichotomy.** PARTLY KNOWN, and the part that is known changes Block 3's plan.
  `gate-census.md` is the trichotomy to 20 cells in both phases (every half enters the gap trap, the kit's ether
  family or the lock of period seven, within 4,190 steps); BN-13 extends it to 2²² and random widths and adds the
  period-5 lock inside the trap. `three-set-game.md` is the free-input window game: reach holds at every width 10 to
  26 (no closed set of windows avoids the three sets, 2.1 GB at 26), the forced basin grows from 35% of the states at
  16 cells to 61% at 22, and outside it the plays that avoid the three sets for ever end in two or three components
  per width, one of which holds the aligned ether at every width and, at 21 and 22 cells, a second unlocked component
  of 5,849 and 8,975 states. `game-residue.md` is the barrier: the aligned ether's two windows lie outside the forced
  basin at every width, because the family's members of depth at least the width certify nothing inside the window,
  so **no forced basin at a fixed width with targets certified inside the window can prove that every right half
  enters the three sets**; a proof has to use that the half is finite, or hold the ether's windows in a target of its
  own. Block 3's "sparse core lift to W of 38 to 40 with the closed classes removed, a verdict on the leaky components"
  is therefore two questions: the ether component is leaky by construction at every W (not a question), and the
  second unlocked component at 21–22 is the one whose fate at 38–40 would be news. Before it runs: define the family
  target as membership at any depth (their reach test does this with `family_cut`), reproduce their W = 22 table
  (30 s and 1 GB on their account), and state the prediction about the second component. The door stays AJAR with
  this input.
- **Lead 2, door 2: Q01 ⇔ Mortality in Lean.** CLEAR; `rule30-open` lists the converse open.
- **Lead 3: bounded amplification.** CLEAR for the theorem; the supply law partly (S-02).
- **Lead 4: the first check bound.** CLEAR.
- **Lead 5, door 3: the class-unit count.** PARTLY. `no-finite-certificate.md`, "Forced rows": 2^(W/2) forced
  prefixes give about 1.78^(W/2) distinct tails, which is 2^(0.416 W), the exponent FE-4 measured; its "Merging
  survivors" paragraph has the plateaus. No square-root law or conditional theorem there.
- **Lead 6: the external ladder.** As PRIOR-ART already has it (S-04).
- **Lead 7: model cases.** S-07 clear; S-08's constructions clear; the Rule 210 door is shared with `rule30-open`
  and with our own 22 October theorem.
- **Lead 8: seed-specific structure.** S-11 partly: the backward half is `SeedPastPeriods`.
- **Lead 9: Problem 2 and 3 frames.** P3: "unbounded one-tape time is equivalent to excluding every eventual period
  2^a" is in `restricted-models.md` with a computation to k ≤ 20, so P3-1's statement is KNOWN there. P2: their
  assessment "even a logarithmic bound gives no positive density" and their two conjectures (`driven-left-runs`:
  black runs at most 0.13t to 0.18t over every driver; `driver-density`: black count at a rate near 3/4 over every
  driver) are the sharper framings of the same rung; "b(n) ≥ C log n infinitely often, for every C" is the weakest
  rung in both. PARTLY.
- **Door 4, Block 8: lock-7.** KNOWN: `SevenLock` has the exclusion in Lean. Block 8 reduces to checking that
  BN-13's period-7 class is `SevenLock`'s set (ours 66 windows of 30 columns, theirs 195 of 32, both with u of period
  7), citing it, and writing the period-5 lock, which is the new part.
- **Door 5, Block 9: period-3 and period-4 language skeletons.** KNOWN in kind. `Columns.ConstrainedLeft001` (Lean)
  reduces 001 to `C3r001`, the kit's `C3s001` with free bits whose runs of 0s are at least 2 and runs of 1s at least
  3; `Columns.ThreeRuns` (Lean): under 001, column 1 at the second white step has 1-runs of length at least 2 and
  0-runs of length at least 3 from step 46 on; `Columns.ReadingWords` (Lean) does the same for 15 blocks of period 5
  to 7; `reading-constraints.md` (census): under 011 every half of up to 16 cells reads no two whites 1, 2, 4 or 5
  apart from step 104 on; `constrained-left-halves.md` (negative): the constraint lowers the left statement's entropy
  from 1/3 to 0.2042 bits per step for 001 and no finite left game closes; `period-three-011.md` (negative): driven
  by 011 the right half does not settle next to the centre. PE-1.2's and PE-2.1's "C3g001, C3g011" are to be compared
  with `C3r001` and the 011 reading set before anything is called new.

## 3. Our left-side results against the two sources

| Ours (atlas §21, CL739–CL750) | Theirs | Verdict and order |
|---|---|---|
| The branch law at a fork, d = ¬a_(j−1)(τ*) ⊕ c(τ* + 1) (CL749, PROOF-SKETCH, 24 of 24) | Berzai note, Thm 6.1 (branch rule; Proved): at a frozen diagonal d with last black row τ_d − 1, the label taken has r_(d+1)(τ_d − 1) = 1 ⊕ ⊕_(t ≥ τ_d − 1) Δ_(d−1)(t), "fixed by the cells of diagonal d − 1 from row τ_d − 1 on", and "not new in kind: that one bit of the transient decides the branch is Rowland's Lemma 3"; checked cell by cell at 399, 53,207, 58,286, 87,866 (Exact); Patto1155's log of 9 September selects the branch by the phase and one boundary bit | **KNOWN, reproved here** in another frame (his defect tail parity where ours reads the cell at τ* and the A0 child word). Berzai's priority: 8 October (ledger 10.231d), against CL749 of 5 November; Rowland 2006 Lemma 3 behind both |
| A chink at a fork's child switches the strip; the switchboard (CL748–CL749, 8 of 8, 15 of 15) | `Diagonals.SkeletonTree.flip_white_complements`, `branch_realized` (Lean): behind a diagonal that is white from some time on, flipping one cell complements the next diagonal, so both candidate classes are realised; the instance at 53,207 is the seed's row at time 107,310 with cell −54,102 flipped; `skeleton-tree.md`: 8 branches to depth 250,000. Berzai §25 and README: a 53,209-cell start (a public gist of 21 August) takes the other branch at 53,208, checked by direct simulation (Exact), refuting left-half universality as stated | **KNOWN**, in Lean there; our 15 of 15 by one cell per fork is the same construction run on the whole tree |
| The advance criterion of the front (the kit's `walk`; §21) | Berzai note, Thm 6.2 (advance criterion; Proved): the front advances at a frozen d iff D_d(m + 1) = 1, and lands on the first black cell of r_(d−1) at or after m + 1; the landing rule is also in Dibujaron's log of 8 September (checked on 60,065 diagonals) | KNOWN all round (kit, Berzai, the repositories) |
| The sixteen left sides below 894,235 (tree16; CL724, CL738, CL749) | Gravner and Griffeath 2012 §8, as quoted by Berzai (Remark 18.7): "the first genuine branching occurs for period 16 at generation 53,207", "all seeds have only 16 distinct limit cycles on the leftmost 65 million cells", their π = 16 label tree of 2,159,030 labels over 894,234 generations; `skeleton-tree.md`: 8 branches to 250,000 | **KNOWN** (Gravner–Griffeath 2012). Add G–G §8 beside Rowland in the record's credits; the paper itself still needs a reader |
| The front is the left damage front; speed 1 − λ_L (CL741–CL742; §8.66 of 6 October) | Berzai Remark 17.19: "the edge speed equals the leftward damage speed of a single flipped cell (0.2429 against Wolfram's 0.2428, Remark 17.24); the argument uses the universality of the front, which is Measured", ledger 10.234d, Part III dated 16–17 September; `onset-edge.md`: the seed's edge gains 0.7519 ± 0.0019 per step, one flipped cell in random rows 0.7561 ± 0.0008 (λ = 0.2441 ± 0.0007), "the same move frequencies to two or three decimals and the same gain within 2.1 combined standard errors", stated as a heuristic | **KNOWN, remeasured.** Order: Berzai (September) → §8.66 (6 October) → `rule30-open` (early November or earlier) → CL741 (5 November). Ours adds the chain hierarchy, the heal identity (PROVED two-party), the matched-window localisation of the excess in q, and the four-strip comparison |
| `heal_iff`, `edge_stall`, `edge_heal` (kit `Rule30ErrorEdge`) | `Diagonals.OnsetEdge` (Lean): `diffEdge_left` (shared cell L − 1 white → the edge moves left, depth gain 0: our stall), `diffEdge_stay` (gain 1: a heal with jump 1), `diffEdge_retreat` (gain 2, or 3 or more, by the cells at L + 1, L + 2); `agree_below_add`; and the kit's `rule_flip_right_iff` (GC2685) | **KNOWN** (two Lean proofs besides ours). The six post-jump laws (the new parent's colour after jumps 2 to 7) are in neither source, as GC2685 found for the kit: CLEAR |
| The strip is fair in every statistic measured (CL741–CL745) | `settled-words.md`: to depth 200,000 the settled words look like fair words of their period, every word of period 16 occurs up to rotation, the longest white runs follow the longest-run law of fair words; Berzai Law 5.1 (fork law; Measured): Hamming distances between consecutive labels are Binomial(P, 1/2) over 1.42·10⁹ pairs, "the wall's own pseudo-randomness statement" | **KNOWN, remeasured.** The edge's selection excess (+0.002 in q, CL743–CL745) is in neither |
| Two walks over one strip lock at a constant clock offset (CL746 addendum 1) | Berzai Prop 6.3 (phase congruence; Proved with an Exact step): a left machine carrying the seed's labels translated by s_w and its front by s_b has s_b ≡ s_w modulo the regime's period; all 37,086 and 385,784 moves of the two regimes, and six driven machines | **KNOWN in kind** (Berzai, ledger 10.231d) |
| The prefix question: the branch is the child bit at the clearing tick; P* = 19,656; 48 of 48 and 0 of 300 on A0 (CL750, BN-11) | Berzai §25: "which finite words take the seed's branch is Open"; the gist author's report, quoted in the note, that more than 2¹⁷ random starting states all took the seed's branch; Remark 6.6: the wall alone decides at none of the frozen diagonals, the transient does | The clearing-tick answer and the worst-case guard are **new as statements**; the census is **known, remeasured** (2¹⁷ by a third party, as reported; the primary comment not read) |
| The driven half-row's left side is universal (CL751's "wall as a reset"; INSTINCT) | Berzai §18.1 ("the left half of any Rule 30 evolution is Rule 30 on the half-line x ≤ −1 driven by column 0"), Prop 18.6 (universal background for every boundary sequence and finite initial left state below 400, Known in stronger form from G–G §8 to 53,207), Thm 18.9 (Exact: six boundaries carry the seed's background to 12,000); `DrivenSkeleton.md`: its step lemmas need the recurrence only from time T, "so they also hold for the left half driven by any center column, whose diagonal j obeys the recurrence from time j + 1 on" | **KNOWN in content.** Not in any source: the kit-level forced bound (`forced_front_four`) for the driven or zero-boundary half-row; INSTINCT updated |
| B2, F4: the actual front's slope through 894,235 (CL739: 1.3326 at 100,000 falling to 1.3155) | Berzai Remark 17.24 (Measured): M_d/d exact per diagonal to 4·10⁶ with a certificate, 1.336660 at 5·10⁴, 1.320079 at 8·10⁵, 1.320763 at 4·10⁶; the ratio is not monotone; bin medians locked at 1.3209–1.3212 on [10⁶, 4·10⁶]; every extrapolation fails a held-out test; "no bound on the limit"; Conjecture H (τ_d ≥ d for d ≥ 20) holds to 4·10⁶ with a certificate and to 4·10⁷ by simulation | **KNOWN, superseded in range** by a factor of 45. Our question "4/3, 1.27 or wandering" has his answer so far: neither limit is supported, and the ratio turns |
| The sixteen strips' reset gaps ≤ 120 at about 11 wheels a level (BN-12) | `settled-words.md`: W_j < log₂ j + 6 to 200,000; `seed-finite-certificate.md`: the one-step jump reaches 24 by depth 200,000; `RunTransfer` (Lean): reset cost ≤ longest agreement run + 2 | **PARTLY** (same family of quantities; different units and depths) |

## 4. Predictions judged (CL752)

- **P-R1.** By the strict count one row is KNOWN outright (S-05); two more have a KNOWN part (S-04's BWH arrows,
  S-10's period-7 lock): MISSED on the strict reading, HELD if parts count. PARTLY KNOWN: S-02, S-04, S-06, S-09,
  S-10, S-11, S-12, S-13, eight: HELD (6 to 9). CLEAR: S-01, S-03, S-07, S-08, four, with S-01, S-07 and S-08 among
  the named candidates: HELD; S-12 came out partly, not clear.
- **P-R2.** HELD: Berzai's Thm 6.1 and 6.2 are the branch law and the advance criterion, with Rowland's Lemma 3 behind
  both, and `SkeletonTree` is the chink switch in Lean.
- **P-R3.** HELD in all three parts: the three-case law is `heal_iff` with the jump size; the six post-jump laws are
  in neither; the front-equals-damage-front identification is in both and earlier than ours.
- **P-R4.** HELD: three sets, no period-5 lock; `game-residue.md` bears on Block 3 as predicted, and more than
  predicted: the ether component is leaky at every width by construction, and a second unlocked component exists at
  21 and 22 cells, which is the real question for Block 3.
- **P-R5.** S-02's supply partly, S-03 clear, S-09 partly, S-13 partly: HELD. S-11 "clear": MISSED, its backward
  half is `SeedPastPeriods`.
- **Counterfactual.** Fewer than two rows KNOWN outright: the queue stands as written, with S-10 split into its
  known and new parts, S-04 restated against the external ladder, and no re-ordering. M-1 to M-7 stand.

## 5. What this changes

1. **PRIOR-ART** gains the Block 2 entries of §3: the branch law, the chink switch, the sixteen left sides (G–G 2012
   §8), the front-equals-damage-front chronology, `heal_iff`'s two other Lean proofs, the fair strip, the phase
   congruence, the census of random starts, the driven half-row's universality, and the settling-constant data.
2. **The queue** carries the verdicts of §1 in its prior-art column.
3. **WARM-LEADS:** Block 2 DONE; Block 3 carries the game-residue input and the W = 22 baseline; Block 8 carries
   `SevenLock` as prior art and the period-5 lock as the new part; Block 9 starts from `ConstrainedLeft001`,
   `ThreeRuns`, `ReadingWords` and the 011 reading set.
4. **The door ledger:** dated notes on the lock-7, free-input certificate, trichotomy, branch-law, chink,
   strip-as-fair-field, prefix-guard, finite-chains and surgery cards.
5. **The backlog:** L-7's question on the seed's branch at Wolfram's number is answered by Berzai's note (Thm 6.5,
   Proved given the front's path, the path Measured on eight coin-driven machines; the wall alone does not decide,
   Remark 6.6).

## 6. Not done, and caveats

- No clone or build of `rule30-open`, so no kernel receipt here for `SevenLock`, `OnsetEdge`, `SkeletonTree`,
  `ConstrainedLeft001` or `SeedPastPeriods`: their statements are read from the notes with the headline names the
  catalogue lists. Block 8 reads `SevenLock.lean` at source before citing it in a module; the backlog's CP-4 item
  (build `WedgeLadderQ01` and audit its axioms) stays open for Local.
- `rule30-open`'s commit dates were not read, so priority against our October results is settled only where a source
  gives a date (Berzai's ledger and section dates; the repositories' September commits he cites).
- Gravner and Griffeath 2012 §8 was not read; it is cited through Berzai's quotations and is the primary source for the
  sixteen left sides. It should be read before any statement about tree16's novelty, and before Rowland alone is
  credited again.
- The record skeptic's placement of the parity law S_2n(2n) ≡ n mod 2 in Berzai's paper was not reproduced by my
  search (the terms found hit the centre-cell degree law, Theorem 14.7); S-06's "partly known" rests on the degree
  law's computed range in `forced-bits-dense.md` and on the swarm's reading of Berzai, in that order.
- The identity of BN-13's period-7 class with `SevenLock`'s 195 windows is not checked at window level.
- Berzai's Parts II and IV (the Duhamel class, the collapse pyramids), §§3–8, 13–16 and 20–23 were not read line by
  line; nothing in the queue points at them. His §24 table of closed routes was read and agrees with the swarm's
  barrier atlas where they overlap (conservation laws, measure-level routes, communication rank, bounded-window
  prediction); his Prop 26.1 (Rule 90 satisfies every measure-level hypothesis and has density 0) is the sibling
  barrier for Problem 2 in its sharpest form and belongs in the atlas beside Gate 1.
