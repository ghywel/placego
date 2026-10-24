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

## 7. The kit at 2f63afd (2026-10-24): eighteen new modules, what to adopt and what not to repeat (Cloud, 2026-10-24 13:27 BST; CL615)

The verifier still pins cc1e0e0 (`api/environment`); the catalog has moved to 86 modules in seven commits since 9679f83:
Nikolay Murzin's Problem 3 statements; Troy Lowry with Codex, pull requests #6, #7 and #9 (fifteen modules); AIOvernight's
#4. Shallow clone in the scratchpad; docstrings read in full, theorem lists read.

| module(s) | what it says | for us |
|---|---|---|
| `Rule30Problem3`, `equivalents/ProblemThree` | **Problem 3 formalized**: a one-tape deterministic Turing machine reading the binary digits of n; three strengths, `Problem3` (no machine in time C(n+1)), `Problem3Verbal` (none in o(n)), `Problem3Robust` (none in n^o(1), model-independent); each implies the next, and `Problem3Robust` implies Problem 1. The checker does not take Problem 3 claims yet. | **Adopt, and close D4.** PRIZE-PROBLEMS.md's D4 asked for "the precise statement of prize problem 3 the record will accept": the kit has now written it; our record points at it (dated note added) and stops drafting its own. Also the reason the GPU cannot help Problem 3 (§H.2) is now a formal fact: a unit-cost RAM computes c(n) in O(n) bitwise operations, which is why only the robust form is model-independent. |
| `Rule30TraceEdge` | `EdgeObservable` (open): finite nonzero configurations with the same infinite center trace have the same left edge. **It implies Problem 1** (the 49th `problem1_of_*`). Full trace injectivity is false (the stripe seeds). | **A new sufficient condition in our territory**: our left-diagonal results (submission 3: periods unbounded, no adjacent whites, the settled band) and Theorem E are statements about what the center trace forces on the left. GPT's task-5 reading (GC1780, GPT-EDGE-OBSERVABLE-REVIEW.md; adopted CL617, 2026-10-24 14:26 BST): cautiously receptive, open; mixed-sign edges reduce to both-negative by a common restart; the one provable case is the standard rightmost-disagreement lemma (a common initial right half gives the first center disagreement exactly at time -q), not a substantive submission; B2/B3/A⁗ do not supply the missing second column; the finite kill test E1 (8,064 positioned rows, horizon 256) was run by Cloud at the owner's word (CL618, 2026-10-24 14:36 BST): no different-edge collision at horizon 256; the predeclared deadline -a + 8 is refuted (edges -6 and -5 agree through time 22), so no deadline of the form -a + c with small c. **E2 and E2b (CL620, 2026-10-24 15:30 BST) reversed the reading:** at fixed edges the maximal agreement does not grow with the right support at all, and by the light cone it saturates at the true maximum once the support exceeds it; certified (finite, exhaustive, pending GPT's check of the argument): M(-2,-1) = 8, M(-3,-2) = 14, M(-4,-3) = 13. The conjecture holds for these three edge pairs with exact deadlines; a submission-shaped question is with GPT. Not a compute job; no further reformulation without a new idea (a condition under which one trace fixes enough right-head information). |
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
