# Our Rule 30 results against the Rule30PrizeKit catalogue (a sub-agent of Cloud, 2026-10-22; reading only; read by Cloud in CL568)

Kit read at the verifier's commit `cc1e0e0`: `lean/README.md` (54 modules), `equivalents/CATALOG.md`, and the modules
Rule30PeriodTwo, Rule30ZeroBoundary, Rule30PeriodTwoCoupled, Rule30MaskedJen, Rule30FiniteMaskedJen, Rule30Diagonals,
Rule30RightPeriods, Rule30ZeroBoundaryBarriers, Rule30BlackRuns, Rule30BlackRunBlocks, Rule30WhiteRunEight,
Rule30StripCertificates, Rule30StripCertificateTable, Rule30Realization, Rule30DrivenLeft, Rule30ZeroBoundaryWidth52,
Rule30ZeroBoundarySmall, Rule30PeriodTwoLanguage/Width5/Width6 (docstrings and the named theorems; not every proof).
Our side: PROOFS.md entries 1–43 and G.GPT131–136, RULE30-PRIZE.md §8.20, 8.33, 8.36, 8.37, 8.39, 8.54–8.59, 8.56,
8.84, PERIOD-TWO.md §2–6, STATE-OF-THE-PROOF.md. Verdict key: ALREADY = in the kit up to phase or normalization;
PARTLY = a weaker, special or differently stated form is there; ABSENT = nothing comparable found.

## 1. The map

| Ours (where) | Statement, one sentence | Reader status | Nearest kit item | Verdict |
|---|---|---|---|---|
| Lemma 1, where column 1 is invisible (PROOFS 1; §7) | The left half sees column 1 only at column 0's white times. | proved (Local); elementary | `Rule30MaskedJen.effective_boundary`, `effective_step` | ALREADY |
| Lemma 2, rotations equivalent (PROOFS 2) | One rotation of a periodic column word per class suffices. | proved | `Rule30PeriodTwo.normalize`; `Rule30ZeroBoundary.Q01_iff_any_phase` | ALREADY |
| Lemma 3, two local rules; visible bits never `11` (PROOFS 3; §8.2) | Beside 0101… the visible column-1 bits have no two ones in a row (free bits no `00`). | proved; checked T1, T2 | `Rule30PeriodTwo.golden`; `Rule30ZeroBoundary.free_bits_no00_no11111` | ALREADY; the kit's `11111` half is not in our lemma |
| Lemma 4, newest bit enters once as XOR; linear and forced cells (PROOFS 4) | The depth-k cell is σ(k−1) ⊕ g_k(earlier) at white times, forced at black times. | proved; checked P2 | `Rule30ZeroBoundary.zrow_aff`, `pivot`, `tri_odd`/`tri_even`, `two_step_shift` | ALREADY |
| The wall form (§8.39; PERIOD-TWO §2) | Rule 30 on x ≤ −1 against an alternating wall; the forced left halves are those keeping the cell beside the wall black at every black wall time. | proved (WA0–WA2 checks); GC1043 phase correction | `Rule30ZeroBoundary.zrow`, `Theta`, `InX`, `Q01`; `Rule30PeriodTwo.left_half_zero_driven` | ALREADY (see §2 below) |
| LR, and R(d) finite ∀d ⟺ LR (PERIOD-TWO §2; §8.76) | No column 1 makes the forced left half eventually zero; equivalently the record R(d) is finite at every depth (König). | proved (the equivalence) | `Rule30ZeroBoundary.Q01`, `Q01_iff_bounded` (via `uniform_death`, `koenig`), `Q01_iff_staged` | ALREADY: Q01 is LR |
| Theorem A, Jen with a clock (PROOFS 5; §8.54) | Columns i, i+1 P-periodic on [a,b] with the edge L left of i force b ≤ 2a+L+2P−1. | proved; Lean (TheoremA.lean, own defs) | `Rule30MaskedJen.finitary_jen` (seed, i = 0: never both P-periodic on [n−P, 2n]); `Rule30FiniteMaskedJen.window_jen_col` (any configuration with a leftmost black cell) | ALREADY (theirs is stronger: `orCol` in place of column i+1) |
| Theorem A′, the window principle (PROOFS 7; §8.58) | A common block of n values of (i, i+1) at times a < a′ needs n ≤ L + a′. | proved; Lean | `Rule30MaskedJen.determine`, `window_jen_col`; `Rule30FiniteMaskedJen.window_jen_col` | ALREADY (same statement with `orCol`; our Collatz pairing is essay material) |
| Theorem A‴, with the band (PROOFS 10) | Row a′ is white on diagonals L+a′−n+1 … a′−a−1; a black diagonal b < a′−a gives n ≤ L+a′−b. | proved; Lean | `determine` gives the row agreement; the diagonal consequence is not stated | PARTLY |
| Theorem B, a zero run beside periodic columns (PROOFS 6) | Columns 0, 1 P-periodic from time 0 (P ≥ 2): zero runs of row 0 have length ≤ 2P−2 (odd runs ≤ 2P−5, GPT). | proved; Lean (TheoremB.lean) | nothing on zero runs under periodic drivers; `Rule30ZeroBoundary.zero_run_local` is a locality lemma | ABSENT (low prize value: Jen already forbids the hypothesis for finite starts) |
| Lemma B1, white then black (PROOFS 8) | An eventually white left diagonal is followed two later by an eventually black one; no two adjacent eventually white. | proved; Lean | `Rule30Diagonals.D_periodic` only (eventual period 2^j) | ABSENT |
| Lemma B2, the clock never stops (PROOFS 9) | The left diagonals' eventual periods are unbounded; infinitely many eventually white and black diagonals; quantitative k ≤ 4^P+1. | proved; second-read Cloud CL173, GPT GC963; Lean | `D_periodic` (upper bound only); lower bounds exist only for RIGHT diagonals (`Rule30RightPeriods.period_gt`, `per_bound`) | ABSENT (the kit cites Rowland 2006 for left-side doubling: PRIOR-ART flavour) |
| Entry 42, left periods divide 2^(k−2) (PROOFS 42) | Diagonal k ≥ 2 settles with period dividing 2^(k−2). | proved; second-read Cloud CL171/172, GPT GC962; Lean | `Rule30Diagonals.D_periodic` (period 2^j for diagonal j); `Rule30FiniteDiagonals.Ld_periodic` | ALREADY (ours is sharper by the index shift only) |
| Lemma B3, no long white run in the settled band (PROOFS 12) | In a band of diagonals settled with period P, a white run is < 2P. | proved; second-read Cloud CL170, GPT GC960; Lean (sharp 2P−1) | none | ABSENT |
| Theorem A⁗ (PROOFS 13) | A repeat's white run cannot lie in the settled band: n ≤ L + a′ − M + 2P − 1. | proved; second-read GPT GC959/960; Lean | none | ABSENT |
| Corollary F, near-squares fatal (PROOFS 11) | Column 1 with ℓ(i_j, i′_j) ≥ i′_j − K at unbounded i′_j − i_j never has a finite left half. | proved (Local); no second reader named | none | ABSENT |
| Theorem E, every Sturmian column 1 excluded (PROOFS 14; §8.57) | For irrational α and any θ, the Sturmian visible bits give a forced left half that is never eventually zero (LR for every rotation coding). | proved (Local, 2026-10-05); no second reader named in PROOFS.md; GPT's G131 builds on its Step 0 | CATALOG.md mentions "Sturmian" once, as a remark that Sturmian sequences are not EP; `Rule30DrivenLeft.no_periodic_column` covers only eventually periodic drivers | ABSENT |
| Theorem E″ (PROOFS 15) | Any coding by finitely many arcs, for α with infinitely many partial quotients > 2^(r+1). | proved (Local); no second reader named | none | ABSENT |
| G131 (block factors), G132 (circle-covering and one-character torus codes), G133–G136 (kicked and bounded-type codes) | Theorem E's exclusion survives every finite block factor; the one-orbit-endpoint arc codings; super-geometric kicks cannot rescue golden-angle codes. | GPT; second-read Local (L085, L086 …) | none | ABSENT |
| Proposition 7, Jen (PROOFS 17; §8.13) | Column 0 eventually periodic and nonzero, column 1 eventually periodic: the forced left half is never eventually zero. | proved; Lean (JenProp7) | `Rule30Jen.not_adjacent`; `Rule30DrivenLeft.col_neg_one_not_periodic`, `no_periodic_column`; `Rule30FiniteConfigs.jen` | ALREADY (Jen 1986) |
| The squeeze lemma and channel bound (PROOFS 19; §8.20, §8.33) | Beside 0101…, column 1's visible bits carry ≤ log₂λ_m bits per visible bit for every layer width m; certified 0.1292 (m = 26), 0.1236 (m = 28) by a Collatz–Wielandt vector in exact arithmetic; every left column ≤ 0.0618 bits/step. | proved (lemma) + certified computation; independent review session; GPT not recorded as second reader | `Rule30PeriodTwoWidth5/6` forbid a few column-1 words at strip widths 5, 6; `count_constrained` counts starts, not column-1 words; `LargeDeviations`/`coverEntropy` in the catalogue bound the whole rule's entropy (log 2 ≤ h ≤ log 3), not column 1 beside a wall | ABSENT as an entropy ceiling; PARTLY as "forbidden patterns at small width" |
| Q10's certified minimal absent words of the visible language to length 48 (§8.83, §8.89; cake_lpr) | Every minimal absent word to length 48 is excluded by a strip no wider than itself. | computed; DRAT certificates, verified checker; single-party in parts (IN011) | `Rule30PeriodTwoWidth5/6` (`col1_constraints`: `11`, `00000`, gap pairs 21, 23, 12, triples 114, 132, 241, 243) | PARTLY (the kit has the mechanism and a handful of words; ours go far further but are SAT-certified, not kernel-checked) |
| R(d) exact to depth 89, R(89) = 75 (§8.36, §8.37; PERIOD-TWO §3) | For every column 1, the forced left half is not zero from any depth ≤ 89 on: Q01 for every start of width ≤ 88, measured by `records.c`. | computed (Local, C; Cloud's depths 53, 61, 65 reproduced on a second machine; swarm lane q1 blind-matched 65, 69, 73); not kernel-checked | `Rule30ZeroBoundaryWidth52.q01_width_le_52` (kernel-checked; W ≤ 56 during the attempt); CATALOG: LHC searches "up to width about 36" | PARTLY: ours reaches further (88 vs 52), theirs is a Lean theorem |
| The deep ladder, left edge ≥ 249 (§8.56) | R(24, 249) = 26: no configuration with column 0 = 0101… from time 0 has its leftmost black cell within 248 cells, whatever its right half. | computed (Local, 4.3 h); predictions first | nothing two-sided at that depth; `Rule30PeriodTwoSideways` has `CQ01` forms, no width result | ABSENT (computation, not kernel-checkable at that size) |
| Two-sided searches (§8.21, §5): no right half ≤ 32 with left ≤ 108; periods 2–6 over right halves ≤ 18 | finite exclusions | computed | `Rule30Window`: no period ≤ 4096 with transient ≤ 8192 for the single seed; `Rule30FactorWindow`: T + P ≥ 16359 | PARTLY (different objects: ours are over finite configurations, theirs the seed) |
| Period 1, Condrey's theorem reproved (PROOFS 37; §8.76) | No nonzero finite configuration has an eventually constant column. | proved; second-read Local L417 | `Rule30Prize.no_column_eventually_constant`; `Rule30FiniteConfigs.no_column_eventually_constant` | ALREADY |
| Entry 38, black-end walls 0 1^q, q = 7 or q ≥ 9 (PROOFS 38) | No finite seed has a column eventually reading 0 1^q. | second-read both ways; Lean (BlackEnd38base, BlackLock) | `Rule30BlackRuns.not_eventually_zero_ones` (k ≥ 9); `01111111` in `Rule30StripCertificateTable` (q = 7); `Rule30BlackRunBlocks.no_period_black_run_then_white` (1^r 0, r ≥ 18) | ALREADY (ours is stated for every column of every finite configuration; theirs for the center of the seed, extended in `Rule30FiniteBlackRuns`) |
| Entry 40, the white end 1 0^q, q ≥ 10 (PROOFS 40) | No finite seed has a column eventually reading 1 0^q, for every q ≥ 10 (uniform proof, Theorem A finish). | second-read Cloud CL110, GPT GC880; Lean (WhiteEnd.lean) | the kit has q = 10, 11, 12 only, as three table entries (`00000000001`, `000000000001`, `0000000000001`); `Rule30WhiteRunEight` is the two-black family 0^r 1 1, r ≥ 8 | PARTLY: the uniform family is ABSENT |
| Entry 41, 139 more words (PROOFS 41) | 24 words of period 10–14 and 115 of period 15–18 excluded by the width-8/10 one-sided relaxation + Theorem A. | computed twice (Local WC, Cloud WR2); Lean (JenRoute.lean, kernel `decide`) | `Rule30StripCertificateTable` (30 words of length 8–13 at K ≤ 9). Overlap: ours contains their length-10 words 0000000011, 0011111111 and length 11–13 entries 00000000001, 00000000011, 000000000001, 000000000011, 0000000000001, 0000000000011, 0000000000101, 0000000001011, 0000000010011; ours adds 00000001111, 000000000101, 0000000001101, 0000000001111, all nine of period 14 and all 115 of period 15–18; theirs adds run-type words (00111111111, 01011111111, 000111111111, …) covered by our entry 38 only in part | PARTLY: ≥ 128 of our words are not in the kit |
| Proposition 5, Rule 90 has no finite configuration with a period-2 column (PROOFS 16) | Lucas' theorem at times 2^n, 2^n + 1. | proved | `Rule30Realization.center90` (single seed eventually constant) | ABSENT as stated (sibling; barrier material) |
| The parity invariant (PROOFS 18; §8.65) | Beside 0101…, Rule 210's forced left half is exactly Rule 90's; LR fails for Rule 210. | proved (Local); GPT's witness | `Rule30Realization.center210`, `barrier` | ABSENT; sharpens the kit's barrier: the Q01 analogue is FALSE for rule 210 |
| Propositions 16, 18, 19 (PROOFS 29, 31, 32) | No finite Rule 210 seed keeps the full 0101 clock (the two-sided period-2 statement HOLDS for rule 210). | second-read both ways (GC478 / L285) | none | ABSENT; with the parity invariant: for rule 210, CQ01's analogue is true while Q01's is false |
| Proposition 6, the pure wheel cannot make a finite left half (PROOFS 20) | Column 1 = the universal wheel U at any phase: the left half is eventually periodic in depth with period 15,009,104,432, never zero. | certified computation (Brent + replay) | `Rule30PeriodTwoCoupled.ether_coupled_witness` is the kit's infinite witness (the stripe) | ABSENT (a specific column 1; computed) |
| Propositions 11–15 (kicks, pulses, landing; PROOFS 24–28) | Structure of the wheel's kicks. | second-read GPT | none | ABSENT; off the kit's framing |
| Propositions 20, 21 (checkerboard fringe; PROOFS 33, 34) | Infinitely many finite seeds share the single cell's whole pattern; a seed sharing the centre column begins its left half where its right half alone fails. | second-read | CATALOG [21] stripe-seeds (`TransformsSeeds`): seeds 1, 11, 101, 1011, … have non-EP center iff the seed does; `Rule30Realization.seed_perturbation` | PARTLY |
| Proposition 22 (faster-than-light rows are periodic; PROOFS 35) | elementary (Boyle–Lee flavour) | second-read | none | ABSENT (not prize-relevant) |
| Proposition 23 (right-edge triangles are a ruler sequence; PROOFS 36) | The triangles on the single cell's right edge follow the ruler sequence. | second-read GPT GC730 | `Rule30RightPeriods.rows_at_powers_of_two`, `last_one`/`last_white` (row 2^k u reads 1 0^J 1) | PARTLY (same phenomenon, different statement) |
| Every rooted walk returns (PROOFS 39) | At every period q the rooted profile walk reaches a zero child. | second-read GPT GC867; Lean (RootedReturn) | none | ABSENT (a statement about the kick-game census, not about rule 30's prize statements directly) |
| Closed routes (PERIOD-TWO §4): thin layers, entropy squeeze as reduction, SAT crib, merging lemma, Chebyshev identity, wheel rigidity, self-similarity, Q6/Q7 methods | Each is closed with its reason. | recorded | `Rule30ZeroBoundaryBarriers`: no finite-abstraction, local, or edge-DFA ranking proves Q01; two-sided `no_joint_local_ranking`; `Rule30Realization.barrier` (rules 90, 150, 210) | PARTLY: the kit's barriers are theorems about proof shapes; ours are closed experiments and reductions; "bounded runs from a thin layer" (§8.14, §8.41) is the measured face of their B2/B6 |
| Collatz and Mahler cross-problem material (COLLATZ-PRIZE §5, MAHLER.md, trio-technical) | the shared wall; Terras's bijection as Theorem A′'s twin | mixed | none (the catalogue's §7 broader perspectives cites Kopra's fractional multiplication, which is the Mahler link) | essay material only, not a Rule 30 result |

Counts (rows above): ALREADY 11, PARTLY 11, ABSENT 17 (counting the G131–136 bundle and Props 16/18/19 as one each).

## 2. Q01 beside LR and the wall form

**The kit's two forms.** `Rule30PeriodTwo.Q01`: for every m ≥ 1 and every row s : ℤ → Bool with s(−m) = true and s white
left of −m, it is not the case that the left half driven by the white column (`L (fun _ => false) s`) has column −1
black at every even time 2k. `Rule30ZeroBoundary.Q01`: ∀ L, FinSupp L → ¬ InX L, with `zrow` rule 30 on depths
k ≥ 1 and the wall (depth 0) held white, and `InX L := ∀ s, zrow L (2s) 1 = true`. The kit proves them equivalent:
`Q01_iff_staged : Q01 ↔ Rule30PeriodTwo.Q01` (Rule30ZeroBoundary.lean:1200), and `Q01_iff_any_phase` (line 773)
shows the phase T of the even steps is immaterial. `not_eventually_period_two_of_Q01` then excludes an eventual period 2
of the seed's center column for every transient; `Rule30FiniteConfigs.no_leftFinite_period_two_of_Q01` does it for every
configuration with a leftmost black cell.

**Ours.** LR (PERIOD-TWO §2, §7): no column 1 at all makes the forced left half for 0101… eventually zero, where the
forced left half is row 0's left half rebuilt by left permutivity from column 0 = 0101… (from time 0) and an arbitrary
column 1. The wall form (§8.39): run rule 30 on x ≤ −1 against a wall white at even and black at odd times; the forced
left halves are exactly the evolutions in which the cell beside the wall is black at every odd time.

**Same statement.** (i) *Dynamics.* The kit holds the wall white; we run it alternating. On a history that keeps the
condition, the cell beside the wall is black at every black wall time, so (x_t(−1) ∨ wall_t) = 1 = (x_t(−1) ∨ 0) there,
and at white wall times the two rules coincide; the kit's `effective_step` says the same thing for real evolutions. So
the two systems have the same constrained histories. (ii) *Condition.* Ours: beside-wall cell black whenever the wall is
black (odd times, with the wall black at odd times). Kit: column −1 black at the even steps, in the normal form where the
center is black at even steps (`normalize`, `m1_even`). Both say "column −1 is black whenever column 0 is"; the phase
offset is absorbed by `Q01_iff_any_phase`. GPT's GC1043 warning (a black-start clock watches even times) is exactly this
phase bookkeeping, already handled in the kit. (iii) *Quantifier.* Our "every column 1" is every free-bit sequence; the
kit's `realization`/`Theta` make the constrained starts a bijective image of the free bits (`Theta_unique`), so
"every finitely supported start" and "every column 1 with a finite forced row" are the same set; the all-white start is
excluded on both sides (column −1 white at time 0 / `0 < m`). (iv) *Finite support versus leftmost black cell.* `FinSupp`
plus nonzero is "has a leftmost black cell"; the zero start is not `InX`. No difference.

**Also already theirs.** Our "R(d) finite at every depth ⟺ LR" is `Q01_iff_bounded` (bounded white runs of the forced row,
via `uniform_death` and `koenig`). Our doubling conjecture R(d) ≤ d + 4 corresponds to their observed death table
(`q01_width_le_52`: depth 1 turns white by an even time ≤ 96 = D(52), "tightness observed, not proved"; the linear bound
2W + 8 proved for W ≤ 52). Our R_real(d) (realizable column 1s only, Q6) has no kit counterpart; it is the two-sided
`CQ01` restricted by depth, which the kit states but does not bound.

## 3. Candidate partial submissions, ranked

1. **The white-end family and 129 excluded column words** (PROOFS 40, 41; our WhiteEnd.lean and JenRoute.lean).
   *Kit statement.* `theorem Rule30Submission.not_eventually_one_zeros (q : ℕ) (hq : 10 ≤ q) : ¬ Rule30StripCertificates.EventuallyWord (true :: List.replicate q false)`
   plus `theorem Rule30Submission.not_eventually_words139 : ∀ w ∈ words139, ¬ EventuallyWord w`, both for the seed's
   `center`; and the finite-configuration forms through `Rule30FiniteConfigs`' `evol` (every column, every nonzero row
   with a leftmost black cell), which is what our Lean already proves with its own `ev`.
   *Mathlib.* None needed beyond what the kit imports; our files import Mathlib, which the kit allows.
   *Effort.* 1–3 days: re-target our `step`/`ev` lemmas to the kit's `cell`/`evol`, replace Theorem A's finish by
   `Rule30FiniteMaskedJen.window_jen_col` or keep ours, and check that the per-word `decide` (2^8 and 2^10 states, ≤ 6
   periods) stays inside the four-minute sandbox (the kit's own 30-word table is a single `decide +kernel`).
   *Gap risk.* Low: second-read both ways, machine-checked, exhaustive finite parts replicated by separate code.
   *New relative to the kit.* The uniform 1 0^q family for every q ≥ 10 (the kit has q = 10, 11, 12 by table) and
   ≥ 128 words of lengths 11–18 not in `certTable`. Modest in value, but a clean first submission and the quickest.
2. **The channel bound as a kernel-checked entropy ceiling** (PROOFS 19; §8.20, §8.33).
   *Kit statement.* With `V n` the set of column-1 words at n consecutive white times that occur under an alternating
   center (defined through the kit's strip relaxation, as in `Rule30PeriodTwoLanguage.simMask`): `theorem
   Rule30Submission.visible_language_growth : ∀ n, (V_m n).card ≤ C_m * λ'^n` at a fixed layer width m, stated with an
   integer Collatz–Wielandt vector w and the inequality A·w ≤ λ'·w checked by `decide +kernel`; the corollary that
   column −1's complexity beside 0101… is at most 2^(n·0.0618) for m = 28 follows by Lemma 4's halving.
   *Mathlib.* Finsets and `Nat` arithmetic only if the automaton is kept finite; no reals (state λ' as a rational).
   *Effort.* 4–8 days. Soundness (every real right half's column 1 lies in every layer language) is the kit's own
   strip-relaxation soundness in a new guise; the hard part is the kernel budget: m = 8 (56 states), 12 (402), 16
   (2,260) and 20 (12,749 states) are surely within four minutes; m = 26 (179,181 states) and 28 (448,144) probably
   not (the kit's width-52 chunks cost 20 s and 3 GB each). A submission at m = 20 certifies 0.1533 bits per visible
   bit; m = 28's 0.1236 would be reported as computation, not Lean.
   *Gap risk.* Low (reviewed by a separate session; exact arithmetic).
   *New relative to the kit.* Yes: the catalogue has no entropy or growth bound on column 1 beside a wall; its
   forbidden-pattern lists at widths 5–6 are the first two rows of this ladder.
3. **Theorem E: Q01 for every Sturmian column 1** (PROOFS 14), with G131's block-factor extension.
   *Kit statement.* `theorem Rule30Submission.q01_sturmian (α θ : ℝ) (hα : Irrational α) : ¬ Rule30ZeroBoundary.FinSupp (Rule30ZeroBoundary.Theta (fun s => decide (Int.fract (θ + s * α) < α)))`
   (free bits are the complement of the visible bits, and a complemented Sturmian word is Sturmian; fix the arc
   convention in the essay). Equivalently `¬ InX (Theta f)` for that f, by `inX_iff`.
   *Mathlib.* Continued fractions of reals (`GenContFract.of`, convergents `convs`), the best-approximation
   property ‖mα‖ ≥ |δ_n| for 0 < |m| < q_{n+1}, the alternating signs and |δ_{n−1}| = a_{n+1}|δ_n| + |δ_{n+1}|; some of
   this is in Mathlib, the best-approximation inequality may have to be proved. Step 0 is `window_jen_col` in the kit
   (our Theorem A in visible bits), so the rule-30 part is already there.
   *Effort.* 1–3 weeks, most of it Diophantine bookkeeping in Lean.
   *Gap risk.* Moderate: PROOFS.md records no second reader for Theorem E or E″ (GPT's G131 reuses Step 0 and was read
   by Local); formalization will be the first full audit. Step 4 (all partial quotients 1) is the delicate case.
   *New relative to the kit.* Yes, and it is the first class of column 1 beyond the eventually periodic ones for
   which Q01 is proved; `Rule30DrivenLeft.no_periodic_column` is the kit's furthest point.
4. **Lemmas B1–B3 and Theorem A⁗, with Corollary F** (PROOFS 8–13; our JenPow2.lean, LemmaB3.lean, TheoremA4.lean).
   *Kit statement.* For every configuration with a leftmost black cell (`Rule30FiniteDiagonals`' setting): `∀ P ≥ 1, ∃
   j, ¬ eventually P-periodic (D j)` (B2); the settled-band white-run bound (B3, 2P − 1); A⁗'s inequality; Corollary F
   as `¬ FinSupp (Theta f)` for any f with near-squares at unbounded periods.
   *Mathlib.* None essential.
   *Effort.* 2–4 days (already in Lean with our own definitions; retarget to `D`/`Ld`).
   *Gap risk.* Low (second-read by Cloud and GPT; machine-checked).
   *New relative to the kit.* B1–B3 and A⁗ are absent; B2's unboundedness is close to Rowland 2006 (credit it);
   Corollary F's exclusions (period-doubling, Chacon, substitution fixed points with a double letter) are new.
5. **The rule-210 barrier pair** (PROOFS 18, 32): beside 0101… rule 210's forced left half is rule 90's, so the Q01
   analogue FAILS for rule 210, while no nonzero finite rule-210 configuration has an eventually 2-periodic center
   column (the CQ01/FinConf analogue HOLDS). *Statement* in the kit's `Rule30Realization.run g` vocabulary with
   `g = fun c r => !c && r`. *Effort* 3–5 days (GC478's clearing-front proof is by hand). *Gap risk* low–moderate.
   *New:* yes; it sharpens the kit's own barrier (`Rule30ZeroBoundaryBarriers` scope note) by showing a sibling where
   Q01-alone is false but the two-sided statement is true, which argues for attacking CQ01.
6. **Width beyond 52** (R(d) to 89; the 248-cell ladder). Not kernel-checkable: R(89) took 14 h in C (about 2^36
   forced walks), the ladder 2.1 billion tree nodes. Report in the essay as reproducible computation with code,
   beside the kit's kernel-checked 52; do not claim it as a Lean result.
7. **Certified minimal absent words to length 48** (§8.83): the kit's `occurs`/`simMask` machinery would kernel-check
   the short ones at strip widths ≤ 10 cheaply (a day), but they are conditional constraints, not exclusions; lowest
   value.

Not candidates: Theorems A, A′ (in the kit, stronger), Prop 7, Condrey, entry 38, entry 42 (in the kit); the wheel and
kick propositions (outside the kit's framing); Theorem B (vacuous for finite starts by Jen).

## 4. Where the kit supersedes or corrects our record

- **Q01 is LR, and it is kernel-checked for every start of width ≤ 52** (`Rule30ZeroBoundaryWidth52`; ≤ 56 during the
  attempt). Our one-sided exclusion reaches width 88 (R(89) = 75) but by C computation; PERIOD-TWO §2/§3 and NOW.md
  should record the kit's Lean result and the equivalence (`Q01_iff_staged`, `Q01_iff_bounded`) with a dated note.
- **Theorem A and the window principle are in the kit** in a stronger `orCol` form (`Rule30MaskedJen`, dated 2026-10-15;
  ours 2026-10-05). STATE-OF-THE-PROOF §3's "which a limited search did not find in print" and §8's letter should say
  so; priority of our record is visible in git.
- **New to our record, for PRIOR-ART.md:** `Rule30Window` (no period ≤ 4096 with transient ≤ 8192 for the seed) and
  `Rule30FactorWindow` (T + P ≥ 16359); `Rule30WhiteSeed.problem1_black_or_white`; the period-3 reductions
  (`Rule30EtherThree*`: Q001, C3s001, C3w, AbsorptionT) and period-4 reductions (`Rule30Ether`, absorption, the 109-state
  wall); `Rule30WhiteRunEight` (0^r 1 1, r ≥ 8) and Theorem B′ (`1^r u` for eight blocks); `Rule30ZeroBoundaryBarriers`
  (no finite-abstraction, local or edge-DFA ranking proves Q01; `no_joint_local_ranking` two-sided); the 54 equivalent
  forms (CATALOG.md), including the black-wall form [54] and coupled-halves [33]. Our §8.40 "every word up to period 4"
  games are measured; the kit has proved reductions for periods 3 and 4.
- **Our entry 41 table and the kit's 30-word table overlap and each has words the other lacks** (see the map); PROOFS 41
  should cite `Rule30StripCertificateTable` and note the kit's run-type words (00111111111, 01011111111, 000111111111, …)
  that our one-sided relaxation at widths 8/10 does not determine.
- **No contradiction found.** The kit's death-time observations (W ≤ 39: column −1 white within about 1.25W–2W steps;
  W ≤ 52: ≤ 2W + 8) agree with our doubling conjecture R(d) ≤ d + 4 (runs end by 2d + 3). The kit's LHC search width
  ("about 36") is below ours (88), consistent.
- **Mechanics to note in NOW.md:** submissions need a Wolfram kernel on the owner's machine signed in with the owner's Wolfram
  ID (Local's job), Lean v4.35.0 and Mathlib 56a005855e at kit commit cc1e0e0, no `native_decide`, a four-minute
  automatic check, and the owner's explicit consent per submission.

*Dated note (Cloud, 2026-10-23 07:18 BST).* The kit moved on after `cc1e0e0` (19 commits to `9679f83`; the verifier still
builds at `cc1e0e0`): [41] natural boundary is proved through Szegő, [46] Durand–Cobham is stated with its integer-base
direction, `ApproximateRecurrence` gives Problem 1 as the absence of approximate linear recurrences, and the kit now
accepts partial results as pull requests. Our white end is in it as `Rule30WhiteEnd`. Two submissions by others
(stripe family with four tail cells; Q001 up to width 37 with a verified checker for every period) are filed in
PRIOR-ART.md's kit addendum; neither touches Q01/LR. The public page's abstracts for submissions 7, 8 and 9 are
garbled (the API sends one byte per character unless each text is wrapped in `utf8`; skill 1.14.0 says so), and the
new abstract guidance is Markdown with TeX in 100–250 words; see CL592.

## 5. Submitted on the night of 2026-10-22/23 (Cloud, 2026-10-23 01:11 BST)

Nine submissions (the ninth on the morning of 2026-10-23), each a module passing the kit's `Check.lean` with the three standard axioms and a computational
essay in the fast cell order, built by Local on the M5 and submitted on the owner's standing consent (CL574, L758).
All nine stand at **Lean Verified** (the verifier's kernel replay); Human Verified is pending for all. Folders under
`reports/wolfram-agents/submissions/`.

| # | folder | id | headlines | map row / candidate | verifier |
|---|---|---|---|---|---|
| 1 | white-end | R30-20261022-c27323 | `not_eventuallyWord_white_end`, `white_end`, `white_end_finite`, `white_end_seed` | entry 40; candidate 1 | maintainer rerun (two timeouts), 23:06 |
| 2a | words-A | R30-20261022-5c4fbf | `not_eventuallyWord_words`, `words_general` (48 words, lengths 11–16) | entry 41; candidate 1 | maintainer rerun, 00:44 |
| 2b | words-B | R30-20261022-70d23b | the same for 80 words of lengths 17–18 | entry 41; candidate 1 | maintainer rerun, 00:44 |
| 3 | diagonals | R30-20261022-0616de | `seed_no_adjacent_white`, `seed_white_then_black`, `seed_periods_unbounded(_quant)`, `seed_infinitely_many_white/black`, `lemma_B2`, `lemma_B3_sharp` | entries 8, 9, 12; candidate 4 | automatic, first attempt, 00:02 |
| 4 | theorem-a4 | R30-20261022-1d5070 | `center_A4_sharp`, `center_A4`, `theorem_A4(_sharp)`, `theorem_A3`, `lemma_B3_sharp` | entries 10, 12, 13; candidate 4 | automatic, 00:04 |
| 5 | corollary-f | R30-20261022-91b0b0 | `corollary_F`, `col_m1`, `blocks_of_visible`, `theorem_A3`, `infinitely_many_black`, `lemma_B2` | entry 11; candidate 4 (first formalization) | automatic, 00:09 |
| 6 | rule-210 | R30-20261022-920c1b | `not_Q01_210`, `parity_invariant`, `linear`, `white_start_inX`, `white_start_parity`, `no_adjacent` | entry 18, §8.65; candidate 5, first half (first formalization) | automatic, 00:46 |
| 7 | sturmian | R30-20261023-e872a3, superseded by R30-20261023-0c4a33 (abstract corrected, Lean Verified 07:43) | `characteristic_excluded`, `characteristic_block_excluded`, `characteristic_excluded_compl`, `fibonacci_excluded`, `cw_near_square`, `std_near_comm`, `corollary_F` | entry 14's characteristic case with G131's block codes; candidate 3 in part (first formalization) | automatic, 01:02 |
| 8 | sturmian-all | R30-20261023-234c71, superseded by R30-20261023-8084e6 (abstract corrected, Lean Verified 07:44) | `sturmian_excluded`, `sturmian_excluded_clock0`, `sturmian_excluded_fract`, `sturmian_block_excluded`, `sturmian_pairs`, `exists_block_collision`, `no_small_period`, `corollary_F` | entry 14 in full, every slope and intercept, by GPT's GC1694 route; candidate 3 complete | automatic, 05:54 |
| 10 | channel-12 | R30-20261023-4767e0 | `channel_bound_12`, `channel_bound_12_eventually`, `channel_ncard_12`, `Cert.bound`, `check_sound`, `weight_bound`, `win_step2`, `visFrom_mem`, `cert12_valid` | candidate 2, the channel bound at width 12 as a theorem: 0.2581 bits per visible bit, by a verified checker that rebuilds the automaton in the kernel (GPT's specification GPT-CL594-CHANNEL-BRIDGE.md); GPT's read GC1707 PASS | automatic, 10:47 |
| 11 | channel-14 | R30-20261023-4d1a54 | `channel_bound_14`, `bound_of`, `explicit_sound`, `stateCheck_spec`, `weight_bound`, `win_step2`, `visFrom_mem`, `all14` | candidate 2 at width 14 (0.2445 bits) by GPT's explicit-state design (GC1708): one kernel theorem per state, 919 of them | maintainer rerun (two timeouts), 14:03; Human Verified by 2026-10-24 |
| 9 | rule-210-two-sided | R30-20261023-b5421a, superseded by R30-20261023-1bf4dc (abstract corrected, Lean Verified 07:44) | `no_finite_clock`, `no_finite_eventually_alternating`, `seed_not_eventually_alternating`, `clock_bg`, `parity_left_of_clock`, `no_finite_clock90`, `Dev.even_impossible`, `Dev.odd_impossible` | entry 32 (Proposition 19), from GPT's chain GC1700 with two substitutions; candidate 5 complete; GPT's review GC1705 PASS, one prose erratum in the README | automatic, 06:45 |
| 12 | d-exact | R30-20261023-8e6bd3 | `death_time_52_exact`, `width56_lower`, `width60_lower` | the kit's `Q01` frontier: D(52) = 96 exactly (the kit had the upper bound), witnesses at 56 and 60 (Local's D-exact lane, L810–L822; GPT's read GPT-D-EXACT-SUBMISSION-REVIEW.md) | automatic, 22:41; Human Verified by 2026-10-24 |
| 13 | d-exact-56 | R30-20261023-ac3898 | the width-56 certificate: D(56) = 100 exactly, 1,024 chunk checks in one module (the verifier's time test, L827, L832) | `Q01` frontier at width 56 | automatic, 23:38; Human Verified by 2026-10-24 |
| 14 | d-exact-60 | R30-20261024-71f858 | `death_time_60_exact`, `q01_width_le_60`: D(60) = 114 exactly, 4,096 chunk checks and the witness (L859; the plain build on the owner's word, CL609's scope clarification, L858) | `Q01` frontier at width 60, the M5's kernel frontier | submitted 09:00, Lean Unverified (queued) at 08:16Z |
| 15 | d-lower-64-72 (Local) | R30-20261024-b16332 | `width64_lower` to `width72_lower`: D(64..72) >= 116, 120, 122, 124, 130, witnesses from the GPU census (L874) | `Q01` frontier: kernel-checked lower bounds where the kit has no statement | automatic, Lean Verified 2026-10-24 |
| 16 | edge-sep (Cloud) | R30-20261024-991a71 | `sep_8`, `sep_13`, `sep_14`, `attained_8/13/14`, `separationB`, `centers_spec`: three exact negative-edge cases of the kit's `EdgeObservable`, deadlines 8, 13, 14 (CL622, L886) | the trace-edge conjecture, first instances | automatic, Lean Verified 2026-10-24 (L888) |
| 17 | d-lower-74 (Local) | R30-20261024-a129c3 | `width74_lower`: D(74) >= 134, witness from the width-74 GPU census (L890) | `Q01` frontier | automatic, Lean Verified 2026-10-24 (L893) |
| 18 | d-lower-76 (Local) | R30-20261024-4dcf69 | `width76_lower`: D(76) >= 138, witness from the width-76 GPU census (L896) | `Q01` frontier; the census epoch's last width (CL624 stop rule) | automatic, Lean Verified 2026-10-24 (L897) |
| 19 | trap-pair families (Local, GPT's GC1836 theorem) | R30-20261024-8d7751 | two infinite families of right halves (agreeing with R31 on 1..28 or R495 on 1..24) absorbed by the ether: `CQ01` for every member (L930 to L936) | the kit's coupled question `CQ01`; the first family-shaped result, as the maintainer's criterion asks (issue 14, CL629) | automatic, Lean Verified 2026-10-25 00:46 BST (L936) |
| 20 | right-edge (S1) | R30-20261027-61e435 | `frozen_ruler`, `no_width_at_depth`, `depth_dichotomy`, `edge_evol`, `edge_run_alternates`: a finite-depth right edge follows the single-cell ruler with a fixed cap (L1001, GC1935; formalized L1016 to L1019; GPT's final pass GC1969) | catalog module `Rule30FrozenRuler`, kit PR #42 | automatic, Lean Verified 2026-10-27 14:04 UTC |
| 21 | edge staircases (S2) | R30-20261027-196370 | `staircase_ends`, `staircase_ends_pow`, `front_step`, `period_two_iff`, `no_fixed_point`, `agree_rain_eternal`, `rain_row_eternal`: staircases near the single cell's right edge end; the odd 2-cycles of the edge map are ±1/3; rain rows keep a two-step patch (L1007, GC1948, GC1947; formalized L1017 to L1020; GPT's final pass GC1969) | catalog module `Rule30EdgeStaircases`, kit PR #42 | automatic, Lean Verified 2026-10-27 14:04 UTC |
| 22 | prefix merger (S3) | R30-20261027-352e5d | `mergePrefix_two`, `mergePrefix_truncate`, `mergePrefix_needs_seven`, `theta_first_edit_local`, `theta_truncate_merge`, `merge_preserves_last_black`, `odd_edits_iff_guarded_merge`: a seven-cell rewrite beside the white wall that merges in two steps for every tail and every common cut W ≥ 7 (GC1930/L996; statement chain GC1965; formalized L1021 to L1022; GPT's pass GC1972) | catalog module `Rule30PrefixMerger`, kit PR #42 | automatic, Lean Verified 2026-10-27 14:05 UTC |

The verifier runs at about half the M5's speed (L760): the two kernel-heavy word modules time out at four minutes
and go through a maintainer's rerun; hand-proof modules pass automatically in about three minutes. Candidates 6 and 7 were not attempted. Candidate 3 is complete (row 8, 2026-10-23: GPT's GC1694 pigeonhole route, which
showed CL582's "not a corollary of Corollary F" wrong). Candidate 2 (the channel bound) is no longer parked: on the owner's word of 2026-10-23 the soundness bridge was built
at width 12 (row 10; widths 14 and 16 follow as separate modules, CL597). Its earlier state was: GPT's GC1702 found
the exact certificates at widths 16 and 20 (2,260 and 12,749 states) but no kernel-normalizing encoding, and the
layer-to-DFA inclusion would need a witness of about 14 million row occurrences; the four-minute feasibility is not
established. Candidate 5 is complete (row 9, 2026-10-23: PROOFS 32 formalized from GPT's statement chain GC1700, the background built
sideways and the finite case by rule 90's freshman's dream in place of the chain's residue arithmetic; GPT's review
requested in CL590). The record's corrections of §4
were applied with dated notes on 2026-10-23 (PROOFS 41, PERIOD-TWO §11, PRIOR-ART). On the public page at 06:14Z
seven of the ten are Human Verified (rows 1–6 and 2a/2b) and the white end is a Kit Contribution; rows 7–9 are not yet tagged.

## 6. The public page on 2026-10-24 (Cloud, 08:16Z listing; CL612)

Twenty-eight entries (the superseded ones dropped), all Lean Verified but our 71f858 (queued). **Ours: rows 1 to 13 are
Human Verified**, the white end a Kit Contribution. Three teams were on the page on 2026-10-23 (Ying Yin's stripe tails,
giraudsa's Q001 to width 37); since then eleven entries from five other teams. The tag vocabulary now holds "Prize
Claimed"; no entry carries it. None of the eleven is a Kit Contribution. What each is, and whether it touches our lines:

| id | team (agent) | what it proves | touches us |
|---|---|---|---|
| R30-20261023-60d213 | AIOvernight with Codex and Claude (Claude Code) | **Sparse16**: if the zero-boundary half is black at depth 1 at the 56 even times 0..110, at least 17 of L(1..111) are black; so `Q01` holds for every start of weight ≤ 16 with any farther tail. A finite-cone certificate on the kit's own definitions. | **Yes**: a weight-bounded `Q01` (weight in depths 1..111, any farther tail), complementary to our width-bounded D-exact line (rows 12 to 14). A "width <= 60 or weight <= 16" statement is a corollary union of two proved domains, not a new frontier (GC1775); a genuinely new mixed theorem would have to cover starts outside both. Their cone method is the kit's `recon`, as ours; their theorem is an exact negative control for any `Q01` search engine (GPU-METAL-JOBS §J.1). |
| R30-20261024-03b551 | Luis Perez Morales with Claude (Claude Code) | Problem 2 partial: a black block starting at time a has length ≤ a, a white block starting at a ≥ 3 has length ≤ a − 3; every window [a, 2a) has a black cell; blackCount n ≥ log2 n + 1. Cites our 0616de and 1d5070 ("Herbert et al.") for the white runs of a row. | **Yes**, adjacent: run bounds on the single-seed column by locality; compare our Theorem E / A⁗ (rows 3 to 5), which are about rows and repeats. Their white bound a − 3 is on the column itself. |
| R30-20261024-1fc962 | Luis Perez Morales with Claude (Claude Code) | **Period-3 ether erodes**: no period-3 wall of any width (the kit had ≤ 12); a 24-state front with a potential 5D + 2t + ψ non-increasing on 23 states, a 576-case kernel check. The ether-and-wall route cannot exclude 001 or 011 with any wall. | Period 3, not our period-2 line. Its potential lives on a restricted 24-state front with an explicit time term, which is not the unrestricted local-sum class CL611 closed for `Q01` (GC1775); neither the method nor our obstruction transfers without reading its domain. |
| R30-20261023-521830 | AIOvernight (Claude Code) | Excludes the eventual words 0^9 1 and 0^7 1 0 1 1 for the single seed, by strip rank certificates (widths 12 and 6). | **Yes**: 0^9 1 is exactly the q = 9 case our white end (row 1) leaves open and names in `control_q9`. Our README should note it (done, this commit). |
| R30-20261023-7a9ed3 | AIOvernight (Claude Code) | 0^q 1 0 1 1 1 excluded for q ≥ 9 (single seed; Troy Lowry's PR #1 to the kit had q ≥ 62), plus 87 words of lengths 12 to 16. | Adjacent to rows 2a/2b (our 128 words of lengths 11 to 18); overlap of lists not checked. |
| R30-20261023-8fe04c | Troy Lowry with Codex | Forbidden suffixes: no column of a leftmost-black start eventually repeats 0^r v 011 for r ≥ 10|v| + 41 (and 001001, 111001 at 10|v| + 71), for every word v. | Generalizes the white-padding family beyond fixed tails. It does not contain our white end: the suffixes 011, 001001, 111001 carry two or more black cells and rotation preserves the count, while 1 0^q has one (GC1775). Related padding results, prior art for any padding claim of ours. |
| R30-20261023-524848 | Troy Lowry with Codex | Six-bit black-ended cores u: 0^r u excluded for r ≥ 74, all sixteen; with the five-tail theorem every tail of length ≤ 6 is covered. | Same family. |
| R30-20261024-ad6cac | Troy Lowry with Codex | Distinct positions have distinct complete column traces, distinguished by time ≤ max(|p|, |q|) + 18. | Not our line. |
| R30-20261023-c5e3c0, 603218 | Andy Norris with Jesse v1.4 | Shield cascades (the black-run shield's right boundary fixed for 2j steps, horizon 4j), 11 0^q excluded for q ≥ 8, strip fixed-point meta-theorems, a Kleene block catalog; 603218 adds Problem 2 Cesàro/Abel/simple-normality equivalences and Problem 3 bridges (ANF degree 2t − 1, Walsh balance, query complexity [2t − 1, 2t + 1]). | 11 0^q for q ≥ 8 neighbours our white end; the Problem 3 bridges are the first formal statements near the kit's complexity concepts. |
| R30-20261023-7e9e6e | G.P.J.W. Quint with Gemini | Jen's left-permutive class is exactly {90, 150, 210, 30}; rule 30 is the only one with a non-eventually-constant center; left-cone reconstruction lemmas. | Rule 210 appears (our rows 6 and 9 use it); otherwise a classification, not our line. |

**What follows for us.** (a) Sparse16 and D-exact bound `Q01` by weight (in depths 1..111) and by width; their union is a corollary, not
new ground (GC1775). (b) 0^9 1 is no longer open: the white end's gap is closed by 521830.
(c) The run-length results of 03b551 on the column should be read against Theorem E and A⁗ before anyone claims a
column run bound here. (d) Nothing on the page touches the channel bound (rows 10 and 11) or the Sturmian exclusions.

### 6.1 The page at 12:23Z, 2026-10-24 (Cloud, 2026-10-24 13:27 BST; CL615)

Twenty-nine entries. Changes since 08:16Z: **our failed 71f858 carries the Human Verified tag** (a reviewer read the
content despite the failed check; the check itself is unchanged, "ran out of the sandbox's memory"); 603218, 7e9e6e, 03b551
and 1fc962 are Human Verified; 7a9ed3 (white padding before 10111) and ad6cac (distinct column traces) are **Kit
Contributions** and now modules of the kit (§7). One new entry, Lean Unverified and running:

| id | team | what it proves | touches us |
|---|---|---|---|
| R30-20261024-1e1b3b | G.P.J.W. Quint with Gemini | Under an alternating center (`Rule30PeriodTwo`), closed forms for the forced left skeleton through column -10 in terms of the odd column -1 bits s(k): four even-step OR gates saturate to true by `golden` (s(k) = false implies s(k+1) = true), column duplications (-5 even equals -3 even; -6 odd equals -4 even shifted), and s not eventually periodic by Jen. Nothing claimed for `Q01`. | Our period-2 line, but nothing to adopt: `golden` is our Lemma 3 (visible bits never 11, free bits never 00; MAP §1 row "ALREADY"), the forced left half is §5 of RULE30-PRIZE.md (Condrey's triangular uniqueness), and the channel automaton computes every such closed form mechanically. Do not spend time re-deriving skeleton columns by hand. |

### 6.2 The page at 16:38Z, 2026-10-24 (Cloud, 2026-10-24 17:39 BST; status review)

Thirty-three entries. Ours: seventeen; 1 to 13 Human Verified; 14 (71f858) failed on the sandbox's memory, tagged Human
Verified; **15 (R30-20261024-b16332, the death-time lower bounds D(64..72) from the GPU census) and 16 (R30-20261024-991a71,
the three exact negative-edge cases of `EdgeObservable`, deadlines 8, 13, 14) are Lean Verified**, not yet tagged. Gemini's
1e1b3b is now Lean Verified. Two new foreign entries:

| id | team | what it proves | touches us |
|---|---|---|---|
| R30-20261024-ddbfbd | AIOvernight (Claude Code) | The pointwise XOR of two rule 30 histories is a history iff one is zero or they are equal (`xor_history_iff`); a general superposition classification, proposed as a kit contribution. | Not our line; prior art for any "linearity" idea (our record has none). |
| R30-20261024-9d92a2 | Emerson Villafuerte with Antigravity (Google DeepMind) | 74 headlines in five families: semigroup-saturated strip certificates excluding 8 white-run and 14 black-run word families for every column of every nonzero finite configuration; unconditional `CQEmpty` for period 4 and period-3 `001` (no left-finite configuration coupled with the empty right half); a **period-2 sideways dichotomy** (`isR30_bad_or_periodic`, `Psi_free_constraints_width6_of_finSupp`, `Psi_even_first_defect_le_10`, `Psi_black_in_window_16`). | **Yes, the period-2 family**: the third family works on the kit's sideways (free-bit) form of `Q01`, the object of our D-exact and channel lines. Read by GPT (task 6, GC1796/GC1798, GPT-CL623-EXTERNAL-PREFIX-REVIEW.md; CL625, 2026-10-24 20:19 BST): Psi is `Theta` of the complementary right-driven trace, a smaller domain than the census's free bits; the depth-10 stripe defect is not death; the kit list has **nine** forbidden words, not thirteen, and all nine are rejected by our 31-state width-6 channel automaton after its initial state (six are admitted as initial words), replicated independently by Cloud; the parametric word families cover 48 of our 128 excluded words up to rotation, a later generalization, not prior art against submissions 2a/2b; Sparse16 cannot prune coarse high-prefix cylinders (GC1798: a branch with 16 free low bits contains a stripe completion of weight 17). No prefix bound for the census came out of it. |

### 6.3 The page at 23:03Z, 2026-10-24 (Cloud, 2026-10-25 00:04 BST; CL628)

Thirty-five entries. **Ours: 15, 16, 17 and 18 are now Human Verified** (nineteen of our twenty ids; 14 is the failed one,
also tagged). Five more foreign entries became Kit Contributions (Troy Lowry's suffix families and six-bit cores, the run
bounds and the period-3 erosion of Luis Perez Morales's team, AIOvernight's XOR rigidity); Antigravity's 9d92a2 is Human
Verified. One new entry: R30-20261024-f177ae (G.P.J.W. Quint with Gemini, Lean Verified): stripe prefixes with five tail
cells, extending the kit's `Rule30ZeroBoundaryStripeFour`, and 32,767 of the 32,768 odd residue classes of the omitted
four-bit tail (m odd, v = 13). Ying Yin's stripe line, not ours; prior art for any stripe-prefix claim.

### 6.4 Public check objects at 01:03:10Z, 2026-10-25 (GPT, GC1851)

Thirty-eight entries. Directly read the catalogue's complete check objects:
our width-74 a129c3 and width-76 4dcf69 are Lean Verified/Human Verified;
trap-families 8d7751 is Lean Verified, not yet Human Verified in this snapshot.
Family verifier fields exactly match local Check JSON (106 replayed constants).
The former raw-external-status review dependencies close. No login-API retry.

New 0554f7, Lean Verified (143 constants), proves consecutive centre black runs
from a>=1 have L+2floor((a-1)/5)<=a, hence5L<=3a+10. GPT read every submitted
proof body and carrying kit dependencies: scoped PASS. Backward healing of an
alternating finite block plus the adjacent black left-edge pair carries it.
White bounds retain the right-front/nine-black hypotheses; logarithmic white
count improved. This does not bound D(W), whose even-time black observations
do not supply a consecutive black run. New d1bcba is still evaluating, Lean
Unverified and no Lean file supplied; advertised diagonal-defect extensions
await carrying-source/completed-check review. Full scopes, hashes and fixed
private-store packet: `GPT-PUBLIC-STATUS-AND-FIFTHS-REVIEW.md`. No new compute.

**Update01:13:39Z (GC1852):** d1bcba now Lean Verified,735replayed/20selected
headlines, source7473bbaa available. GPT read allnewPhase4 proofs; old9d92a2
declaration body byte-exact. Scoped formal PASS: consecutive centre black
L<=a-2 fora>=4, whiteL<=a-5 only with exactpreRow andell+7<=a. Fixed-diagonal
linear bounds do not prove the source prose's sublinear/O(1) assertions. No
all-widthD transfer. Named review COMPLETE WITH PROSE/SCOPE CORRECTIONS;
`GPT-D1BCBA-DIAGONAL-REVIEW.md`, fixed six-file private packet. No new compute.

### 6.4 The page at 05:11Z, 2026-10-25 (Cloud, 2026-10-25 05:12 BST; CL630)

Thirty-eight entries. **Ours: twenty ids, nineteen Lean Verified, nineteen Human Verified**; the new one is the trap-pair
families (R30-20261024-8d7751, row 19 of section 5), Lean Verified, not yet tagged. Two new foreign entries: Jean-Pierre Goux
with Claude, R30-20261025-0554f7, a three-fifths bound on black runs of the single-seed center column (5L <= 3a + 10 where
the catalog had L <= a; GPT's scoped read GC1851 PASS); and Antigravity's R30-20261025-d1bcba superseding its 9d92a2 with
fourteen more headlines (left-diagonal defect spectra; GPT's GC1852: the appendix carries, the word "sublinear" does not).
GPT read the rest of the externals overnight (GC1853 to GC1859: the kit's backward certificates, StripeMeeting, XOR rigidity
on the whole line only, period-three erosion, the padding families, sparse predecessor lists, tail rotation); their
reports are in reports/wolfram-agents/GPT-*.md.

### 6.5 The page at 12:10Z, 2026-10-25 (Cloud, 2026-10-25 12:12 GMT; CL634)

Forty-five entries, forty-three Lean Verified and two Lean Unverified. **Ours: twenty ids, nineteen Lean Verified and Human
Verified; the trap-pair families (R30-20261024-8d7751) still Lean Verified without the tag.** Seven new foreign entries
since 05:11Z, all already read by GPT at source: Tensorbend's Problem 2 equivalence (R30-20261025-5105a7, superseding eb3b91;
section 9, GC1864), Tensorbend's cut-rank middle reduction (bcf514; section 10, GC1865), Tensorbend's single-cell period-four
absorption for the word 0001 (b572b3, and its large-position subset e88630; section 11, GC1874), Quint with Gemini's
unconditional four- and five-cell stripe tails (017d83, superseding 82d00b; section 11), and Tensorbend's two-cell
period-four pair: dacb3e (large positions) and a02087 (all finite right halves supported above 30, with no finite-support
hypothesis on the tail) Lean Verified (GC1878), while 81e2c6 (the two-cell result at every position) is Lean Unverified:
its check reports a compilation failure with no diagnostic (GC1877). Gone from the listing: Quint with Gemini's
R30-20261024-f177ae (five tail cells and the punctured cycle), which was Lean Verified at 23:03Z; the page carries no reason.
Nothing here bounds D(W) for all W or treats an arbitrary onset row; GPT's reading (GC1878) is that the protected-cone
mechanism now stands in externally verified sources and the open wall is getting an arbitrary onset row into a certified
family. Nothing to wrap in beyond sections 9 to 11; nothing of ours repeats theirs.

## 7. The kit at 2f63afd (2026-10-24): eighteen new modules, what to adopt and what not to repeat (Cloud, 2026-10-24 13:27 BST; CL615)

The verifier still pins cc1e0e0 (`api/environment`); the catalog has moved to 86 modules in seven commits since 9679f83:
Nikolay Murzin's Problem 3 statements; Troy Lowry with Codex, pull requests #6, #7 and #9 (fifteen modules); AIOvernight's
#4. Shallow clone in the scratchpad; docstrings read in full, theorem lists read.

| module(s) | what it says | for us |
|---|---|---|
| `Rule30Problem3`, `equivalents/ProblemThree` | **Problem 3 formalized**: a one-tape deterministic Turing machine reading the binary digits of n; three strengths, `Problem3` (no machine in time C(n+1)), `Problem3Verbal` (none in o(n)), `Problem3Robust` (none in n^o(1), model-independent); each implies the next, and `Problem3Robust` implies Problem 1. The checker does not take Problem 3 claims yet. | **Adopt, and close D4.** PRIZE-PROBLEMS.md's D4 asked for "the precise statement of prize problem 3 the record will accept": the kit has now written it; our record points at it (dated note added) and stops drafting its own. Also the reason the GPU cannot help Problem 3 (§H.2) is now a formal fact: a unit-cost RAM computes c(n) in O(n) bitwise operations, which is why only the robust form is model-independent. |
| `Rule30TraceEdge` | `EdgeObservable` (open): finite nonzero configurations with the same infinite center trace have the same left edge. **It implies Problem 1** (the 49th `problem1_of_*`). Full trace injectivity is false (the stripe seeds). | **A new sufficient condition in our territory**: our left-diagonal results (submission 3: periods unbounded, no adjacent whites, the settled band) and Theorem E are statements about what the center trace forces on the left. GPT's task-5 reading (GC1780, GPT-EDGE-OBSERVABLE-REVIEW.md; adopted CL617, 2026-10-24 14:26 BST): cautiously receptive, open; mixed-sign edges reduce to both-negative by a common restart; the one provable case is the standard rightmost-disagreement lemma (a common initial right half gives the first center disagreement exactly at time -q), not a substantive submission; B2/B3/A⁗ do not supply the missing second column; the finite kill test E1 (8,064 positioned rows, horizon 256) was run by Cloud at the owner's word (CL618, 2026-10-24 14:36 BST): no different-edge collision at horizon 256; the predeclared deadline -a + 8 is refuted (edges -6 and -5 agree through time 22), so no deadline of the form -a + c with small c. **E2 and E2b (CL620, 2026-10-24 15:30 BST) reversed the reading:** at fixed edges the maximal agreement does not grow with the right support at all, and by the light cone it saturates at the true maximum once the support exceeds it; certified (finite, exhaustive, pending GPT's check of the argument): M(-2,-1) = 8, M(-3,-2) = 14, M(-4,-3) = 13. The conjecture holds for these three edge pairs with exact deadlines. **Formalized (CL622, 2026-10-24 16:36 BST):** `submissions/edge-sep/`, the kit's checker pass (583 constants, eight headlines, standard axioms); GPT's module read requested before Local builds the notebook. Not a compute job; no further reformulation without a new idea (a condition under which one trace fixes enough right-head information). |
| `Rule30TraceMerge`, `Rule30TraceAmbiguity`, `Rule30FeedbackErasure` | Limits of reconstructing the left half from the center trace: two rows with edge -3 and different cells at -1 have identical entire center traces (right halves infinite periodic); for every horizon two **finite** rows agree on the first H center bits and differ at -1; and two distinct finite configurations (black at 1; black at 1 and 2) have identical complete center and right-head traces, both non-eventually-constant. | **Do not repeat**: any idea of "recover the configuration from the center column" is settled negatively in these exact senses; only `EdgeObservable` (the edge, not the cells) survives as a question. Our job 2 is unaffected: it reconstructs column -1 from column 1 under the clock by left-permutivity, not from the center trace alone. |
| `Rule30ControlledResponse`, `Rule30TerminalClock`, `Rule30PeriodicProfileCounter`, `Rule30ClockMask`, `Rule30FiniteClockCertificate`, `Rule30FiniteClockSixteen` | The right half as a controlled system: its response to every left driver is equivalent to head/OR observations of a triangular diagonal map; the rewrites 011 to 01 and 101 to 11 preserve responses and every full-state return time; infinite tails can hide a head period (period 8 examples); **a finite-support right half whose full clock divides 16 cannot hide a shorter head period** (`period_loss_requires_infinite_tail`, a 68-node kernel certificate). | **Adjacent to the channel bound and to `CQ01`.** Our channel automaton is the right half with *free* left inputs; this is the right half with *every* left driver, and its finite-clock certificates are the right-half counterpart of "finite support is essential" on the left. Read before any `CQ01` work; nothing of ours is superseded (the channel bound counts visible words, which these modules do not). |
| `Rule30DrivenPrefix`, `Rule30PackedReconstruction` | Packed rows of the **alternating-driven right half** with exact bit soundness (`packed_sound`), prefix dependence (`iterate_mod_bit`: bit j after n steps depends on the first j + 2n bits), gate windows; and packed checks of the scalar sideways reconstruction, sound inside the represented light cone. | **Adopt as job 2's right-side engine** (GPU-METAL-JOBS §J.4): the finite-horizon soundness map GPT required is largely in the kit already; a census implementation should use these definitions and cite the lemmas rather than prove its own. |
| `Rule30SpacingRenormalization`, `Rule30ExactReturn`, `Rule30SpacingGapCounterexample` | morpholib's eight-column reconstruction identity (fractastical, Theorem 14) made exact: under gate spacing at least three, shifting the reconstruction eight columns left transforms the gate by G(r+2) xor G(r+4); the condition survives iteration only for gates white from index four or five on; a period-31 gate with spacings 3 and 5 reconstructs to seventeen white cells at depths 528 to 544, so the identity does not iterate unconditionally. Period 2 not excluded. | Not our line; prior art for any "renormalization" or "self-similar reconstruction" idea (our record has none: record searched). |
| `Rule30ColumnSeparation`, `Rule30WhitePad10111` | The two Kit Contributions of §6 (distinct column traces by time max(abs p, abs q) + 18; no eventual 0^q 10111 for q >= 9). | Prior art; the second neighbours our word exclusions (rows 2a/2b). |

**Not to repeat, in one list:** the precise Problem 3 statement (D4); a packed engine for the alternating-driven right half;
packed sideways-reconstruction checks; reconstruction of cells from the center trace; the eight-column renormalization;
the 0^9 1 and 0^q 10111 exclusions; the forced left skeleton's closed forms. **To wrap in:** D4 closed by pointer;
`EdgeObservable` as a GPT mathematics task; the kit's finite-clock and driven-prefix modules as the reference for `CQ01`
work; the Human Verified tag on 71f858 as the sign that the content was read.

## 8. Selected kit3eca backward-certificate sources (GPT, GC1853, 2026-10-25)

KitHEAD remains3eca23c0 (118module catalogue); comparison against section7's
2f63afd has32added sources/eightcommits. This closes a selected source-review
gap, not a newly observed kit update or a blanket review of118modules.

| Source read | What carries | Scope retained |
|---|---|---|
| BackwardVacuum/BackwardTube/RestrictedBackwardTube/ZeroPredecessor, full | Predecessor chains from actual endpoint vacuum, forward/backward intersections, restricted checks on an actual invariant set; physical periodic padding exclusions | Checks quantify both farboundary bits; singletonvacuum mask1; actual invariant membership and endpoint hypotheses required; conditional certificate existence only |
| WhitePulse/WhitePaddingVacuumCriterion/WhitePadding/FiniteStrips, full | Nine-black shield survives arbitrary finite pulse; periodic early-arrival forces forbidden adjacent periodic columns; necessary earlywhite/vacuum prefix; pumping and generic vacuum avoidance | Chosen0^r u families with stated r/width/certificate bounds; does not establish every pulse has a certificate, CQ01 or universalD(W) |
| FiniteBlackRuns/LightCone, carrying bodies only | Encoding/shield/black-stays/driven cone and locality interfaces used above | No full-module re-audit or new kernel replay |

Eight fullsources1430lines; report `GPT-3ECA-BACKWARD-CERTIFICATES.md`, fixed
15payload private packet/digests. EmptyZ/allwhite-pulse hand countercontrols
prevent vacuous restricted checks/universalcertificate-existence inference.
Target01 hasr=m=1, failingr>=21; no all-width transfer or heldlane reopening.
Other additions remain outside this selected review. StripeMeeting docstring/
final statements only: proof/certificate unreviewed, no new claim adopted.

**Dated coverage update (GPT, GC1854/MI787, 2026-10-25):** the separate
`GPT-STRIPE-MEETING-REVIEW.md` now completes all1031 lines of StripeMeeting
and all semantic definitions/proof declarations of its108-line certificate;
the entire2321-node pool was parsed as literal data. Scoped source PASS,
no kernel replay. Exact common cut, white separator and low-bit-first grammar
retained. Arbitrary-length run induction plus actual-row/zero-flush bridge
supports unbounded row sizes. Relation preserves traces via TWO steps;
meeting under equal observations is at time0 or1. Eventual entry for every
equal-trace pair is NOT proved. Hand reflected-coordinate/one-step negative
controls prevent a false physical/normalizer interpretation. No Psi/CQ01 or
all-widthD(W) transfer; five retained payloads/readbacks, no compute request.



**Further selected source read (GPT, GC1855/MI788):** XorRigidity all326 lines,
34 declarations, scoped source/hand PASS in `GPT-XOR-RIGIDITY-REVIEW.md`.
Whole-line actual histories admit exact pointwise XOR only for zero or equal
inputs, with no support condition. Spatial-distance induction, arbitrary cuts
and formal shear carry. Four Boolean kernel declarations read, not replayed.
Hand site0 exception on the sheared half line prevents a direct boundary-driven
transfer; no centre-trace/conservation/CQ01/all-widthD inference. Five fixed
payloads/readbacks; other kit additions remain outside these selected reviews.


**Period-three coverage update (GPT, GC1856/MI789):** EtherThreeErosion,
WhiteTailErosion and EtherThree fully read988lines; Ether driver interface only.
Scoped source PASS: finite perturbation erosion3w+6, extension using some
defect within a speed-one frontier, white-tail witness W+n+12 and arbitrarily
late departures. All-width no_wall applies to WallOK strips universally closed
under far bits; not all tail-constrained traps or period-three traces. Exact
bad-state potential increase/one-cell far-bit controls retained. Temporalperiod3
ether is distinct from phase3 of period4 ether. `GPT-PERIOD-THREE-EROSION-REVIEW.md`;
nine fixed payloads/readbacks, no kernel replay/CQ01-D transfer/new potential job.


**Uniform-padding coverage (GPT, GC1857/MI790):** all121 wrapper lines and
all semantic declarations/bodies of1136-line WhitePaddingFamilies read;
156 mask literals parsed, no image/kernel evaluation. A-E tail/K/N:
101011/6/13,1101/7/14,11101/9/23,101/9/23,1111/10/31, uniformly every
leftmost-black configuration/column/transient with arbitrary right tail.
Extra cheap/heavy components read in their stated scopes; Heavy commonN49
retains three stabilization times28/49/32. `GPT-UNIFORM-PADDING-REVIEW.md`;
eight fixed payloads/readbacks. No universal-tail certificate existence,
finite survival deadline or CQ01/all-widthD transfer.


**Sparse-check interface (GPT, GC1858/MI791):** SparsePreimage all78 lines
read, scoped PASS. Lists are predecessor/source states despite docstring
“target” wording; exact Z=stateMask L is essential, actual invariant membership
separate. One-cell hand countercontrol and four fixed payloads/readbacks;
`GPT-3ECA-BACKWARD-CERTIFICATES.md` addendum, no evaluation/global D inference.


**Rotation/reduction scope (GPT, GC1859/MI792):** WordRotation/ShortTail/
FiveTailReduction/SixTailReduction/FiveTail,all568lines read. Exact rotation
collects white ends into r+a+b. Short<=4,r49 uniform theorem and periodic
complement form carry through GC1857's read certificates. Five/six reductions
at69/77 retain new-core/imported premises; FiveTail core dependencies not
independently carried, SixTail unread. `GPT-TAIL-ROTATION-REVIEW.md`,eight
fixed payloads/readbacks; no blanket core-certificate adoption or D deadline.


**Five-tail carrying closure (GPT, GC1860/MI793):** FiveTailTube1238lines/all
semantic bodies plus VacuumExample54/WhitePadding10101 63 fully read;
FiveTail's eight new cores now independently carried at source-review scope.
Known uniform length<=5,r>=69 exclusion for every leftmost-black configuration,
column and transient, arbitrary right tail. Exceptional10101 usesK16/L24,
actual period-boundary vacuum and restricted source membership; OR trace is
0^(r-8)1^8 10101, not all-white in the white phase. ExactK-1+54=69 bound and
three sparse-list/mask bindings checked. `GPT-FIVE-CORE-REVIEW.md`; ten fixed
payloads/readbacks, no kernel/transition replay. SixTail/new six-core closure
still unread; no arbitrary-tail/deadline/CQ01/all-widthD transfer. CL630's
family replay count corrected by pointer in GC1860:106;143 is foreign0554f7.


**Six-tail carrying closure (GPT, GC1861/MI794):** all semantic bodies of
SixTailBackward1347/SixTailEndpoints509 plus full SixTail57/SixTailSharpened105
read,2018 new lines. Known uniform length<=6/r77 exclusion now carried and
sharpened to74 for every leftmost-black configuration/column/transient,
arbitrary right tail. Endpoint110001 K12/L14/r74 forces OR0^(r-2)1^8;
111101 K10/L3/r72 gives OR equal proposed word. Inclusive physical boundary,
fixed backward block at END of long white run and explicit74 rotation using
FiveTail69 checked.174 backward Q masks/158 steps/49 endpoint masks PASS,
no dynamics/Lean replay. `GPT-SIX-CORE-REVIEW.md`;13 fixed payloads/readbacks.
No arbitrary-tail/frequency/finite deadline/CQ01/all-widthD transfer; other
unread kit additions retain their unread status.


**Suffix/catalogue coverage (GPT, GC1862/MI795):** ForbiddenSuffix/SuffixFamilies/
PaddedWords and actual WhitePad10111/WhiteRunEight/WhiteEnd/WhiteEndChecks
fully read1523lines, plus carrying BlackRuns period-class bodies. Uniform
arbitrary v: no0^r v011 for r>=10|v|+41; v001001/v111001 for10|v|+71.
Full-set suffix image, no stabilization premise. PaddedWords seed-center
dispatch8/9/10/49/69/74 carries, but informal least wording needs qualification:
raw011 returns49 although0^7 011=0^8 11 is excluded by bound8. Definition74
beyondlength6 has no theorem there. Smaller8/9 not automatically all-left-finite;
WhiteEnd10 separately uniform. `GPT-SUFFIX-FAMILIES-REVIEW.md`;12 fixed
payloads/readbacks, no checker/Lean replay or finite/globalD deadline.


**CenterRuns coverage completion (GPT, GC1863/MI796):** full531lines/33 theorem
bodies now read, source/hand PASS, reusing GC1851 stronger three-fifths review.
White-window[a,2a] is inclusive; counts exclude n. General black bound retains
STRICT lo-i<a; a just-arrived edge black cell disproves the weaker<= premise.
Existing public-status/fifths review section6;4 fixed payloads/readbacks.
No new run bound, kernel replay or even-time survival/spatial forced-row D
bridge. Selected added-module gaps closed, imported-dependency partial scopes
preserved; global/local-template incubation remains, no new quota/job.


## 9. New public Problem 2 equivalence (GPT, GC1864, 2026-10-25)

Catalogue 06:58:30Z: 39 entries. R30-20261025-5105a7 supersedes eb3b91;
Lean Verified, 118 constants, one selected equivalence headline, standard
axioms, no verified official target. Both actual sources are byte-identical
586-line modules; GPT full source/hand PASS. For any Boolean discrepancy
walk, balance along one strictly increasing sequence plus relative gaps
tending to zero is equivalent to density one-half. Converse takes identity
scales; no Rule 30-specific balanced-scale sequence or rate is constructed.
A helper's bounded-relative-gap label actually refers to additive gaps
[N,N+m]. Fixed positive relative gaps fail the hand dyadic tent control.
The exact official Problem2 count bridge carries. No density, normality,
CQ01 or all-width D(W) conclusion; novelty unassessed. Full scope and fixed
evidence: `GPT-P2-SINGLE-SEQUENCE-REVIEW.md`.


## 10. New public cut-rank middle reduction (GPT, GC1865, 2026-10-25)

Catalogue 07:49:03Z: 40 entries, new R30-20261025-bcf514 Lean Verified;
113 constants, one selected iff headline, standard axioms, no verified official
target. GPT read the entire 589-line source: scoped source/hand PASS.
For arbitrary field-valued words and n>=2, maximal ceiling-log cut rank is
equivalent to strict half-rank at one even middle cut or BOTH odd middle
cuts. Both rank-doubling inequalities follow from restriction/interleaving.
RankMax is not full matrix rank: a 4-by-4 middle rank 3 qualifies. Hand odd
rank pairs(2,1)/(1,2) and n0/1 controls preserve exact scope. No actual Rule 30
center-rank theorem, complexity lower bound or Problem 3 solution. Novelty
unassessed; fixed evidence/full review: `GPT-CUT-RANK-MIDDLE-REVIEW.md`.


## 11. Public period-four and stripe-tail families (GPT, GC1874, 2026-10-25)

b572b3: all-position/all-phase single-cell absorption for0001; e88630 the
p0/p>=31 subset. Actual source PASS,120 finite cases plus protected cone;
full finite-input Absorption unproved.82d00b and byte-identical017d83:
unconditional four-/five-bit tails after arbitrary stripe prefix, death at
an even time<=d-1+45; large front cycle covers all arrival phases. Actual
source PASS/external Lean Verified; no global D bound. Abstract1100 fixed
stripe/uniqueness and36 odd classes are incorrect (source1010 and33).
8f032d external check passed but its own source URL404, so its source review
remains pending. Full source scopes, hashes and19 retained payloads in
`GPT-PERIOD4-AND-STRIPE-TAIL-REVIEW.md`; no local replay or new submission.


## 12. Portal and verifier update at 18:59Z on 2026-10-25 (GPT, GC1884)

41 live entries,40 Lean Verified/one Unverified, compared to45 at12:27Z. Added01554c explicitly supersedes d1bcba and changes only one source comment to qualify the spatial white-row bound;735 external replay constants/20 selected headlines, no new formal result. Absent:d1bcba,bcf514,81e2c6,e88630,dacb3e. Only d1bcba's removal has an explicit replacement relation in this delta; other removal reasons unknown. All40 retained entry objects unchanged.

Verifier image8/kit0090056412733accaa27643d3cbbf982104f2251 adds StripeFrontLift, StripeTail13Completion and StripeFourComplete. All883 lines source-read. Generic projection, universal return period and sparse return-map certificate lifting are reusable; the actual four-tail family and46-bit cycle already occur in reviewed017d83. The lift requires exceptional white witnesses; periodicity alone fails the hand width2 signal control. No all-tail coverage, universalD(W) or new experiment. Full evidence/scope: `GPT-PORTAL-UPDATE-20261025-EVENING.md`.

**Morning public refresh (GPT GC1892, 2026-10-26):** direct catalogue09:07:17Z has40 entries(39 Lean Verified,1 Unverified), no new IDs since the preceding evening snapshot. Older9d92a2 absent;017d83 abstract has only an encoding repair, five display-group changes. All retained headlines/checks/statuses/tags and catalogue environment unchanged; separate environment still image8/kit0090056. No new source review or general bound. See `GPT-PORTAL-UPDATE-20261026-MORNING.md`.

**Ownership audit (GPT GC1896, 26 October 2026):** live10:30:13Z catalogue retains all20 current team submissions, now all20 Human Verified;19 Lean Verified, width60 still Lean Unverified. Only our three documented abstract-correction originals are absent and explicitly superseded. None of the six recent disappearances is ours. Primary issue14 guidance against further single widths remains; existing portal listing differs from kit inclusion. See [removal audit](GPT-PORTAL-REMOVAL-AUDIT-20261026.md).


## 13. Morning update, 27 October 2026 (GPT GC1938)

Live09:44:10Z catalogue52 entries,12 added/no removed since26October10:30Z;50 Lean Verified/2 Unverified. All20 current team entries remain;19 Lean Verified,19 Human Verified. Width60 entry71f858 lost Human Verified without an explained reason; its Lean Unverified status persists. External017d83 is now a Kit Contribution. Kit7d665044/image10. [Full delta and review scope](GPT-PORTAL-UPDATE-20261027-MORNING.md).

Selected230bc7 trap proof gives empty-right3/5 gate gaps from sample146, finite-left Q01Gap remains open; c137e0 gives an infinite-periodic-left/finite-right natural clock, not a finite-seed counterexample. Supporting spacing transform cannot iterate on its gate. Other new results catalogued with their read level; b035ac evaluation error/no Lean source is not formal verification. No new submission or runtime job.


## 14. Morning update, 28 October 2026 (GPT GC1999)

Live 08:54:15Z catalogue: 56 entries, 55 Lean Verified/one Unverified. Since GC1976, added e34744/6827d2, absent 01554c/b035ac. e34744 source byte-identical to 01554c; existing linear/conditional scope review applies. Complete 6827d2 source and carrying imported steps reviewed: periodic centre implies pulses and nonperiodic left columns, not a contradiction. All 23 team entries present; S1/S2/S3 Lean Verified, human tags empty. External 1910d0/1b82d8/0ef9c8 gained Human Verified. Kit/image unchanged; no official prize target verified. [Full review and evidence](GPT-PORTAL-UPDATE-20261028-MORNING.md).
