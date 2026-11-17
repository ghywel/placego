---
Template: ComputationalEssay
Name: The Free-Middle Theorem: Late Survival Does Not Restrict Additive Ranks of Rule 30's Zero-Boundary Left Half
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. In rule 30's zero-boundary left half, a rank made of any function of width and boundary windows plus an integer additive density, bounded below linearly and nonincreasing on rows that survive to within a growing margin of their width, has a conserved density; so no nonnegative rank of this form strictly decreases on every late double step. The lower bound is necessary.
Abstract: In core Lean 4.35.0 we prove a strengthened ranking barrier for the zero-boundary left half of rule 30. Fix a margin u(W) tending to infinity. A finite row of width W is late if it passes the checks at times 0 and 2 and every even check through max(W - u(W), 0). Consider a rank consisting of an arbitrary integer function of the width and two fixed boundary windows plus an integer density on m-cell windows. Here m and the edge-window width are positive; for the boundary reduction, both windows have at least m - 1 cells. If the rank is at least -KW on late rows and never increases along their double steps, the density is conserved on every closed walk, hence a constant plus a shift coboundary, and the rank depends only on the width and boundary windows. Consequently no nonnegative rank of this form strictly decreases along every late double step. The proof plants a periodic word behind a stripe prefix and uses balance of the four-step image. The available middle grows with both width and margin; no sublinear assumption on u is needed. Popcount minus W^2 shows why the linear lower bound matters. Nothing here decides Q01 or Problem 1.
Keywords: [rule 30, Rule 30 Prize, period two, zero-boundary left half, Q01, ranking function, barrier, conservation law, additive density, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: Rule 30 has no additive conservation law](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/structure/conservation-laws.md)"]
---

## 1. The statement

The kit's `Q01` is the period-2 form of Problem 1 in the zero-boundary left half. It says that every finite start eventually turns column `-1` white at an even time. A termination proof would be a rank: a natural number attached to each row that strictly decreases along every surviving double step. The kit's barrier `Rule30ZeroBoundaryBarriers.no_local_ranking` (B2) shows that no function of the width, a wall window of `w` cells and an edge window of `e` cells can be such a rank. This module strengthens B2 in two directions at once. The rank may contain an additive density, and it need only decrease on rows passing a width-dependent cutoff, with a margin tending to infinity.

Fix `u : Nat → Nat` with `u(W) → ∞`. A row of width `W` is *late* (`Late u s W`) if its double step survives and depth `1` is black at every even time up to `W - u(W)`. A *rank* is `β(W, wall window, edge window) + Σ h(window)`, where the sum runs over the `m`-cell windows of the row and `β` and `h` are arbitrary integer functions. Here `m ≥ 1` and `e ≥ 1`. The boundary reduction and additive-ranking obstruction use `w, e ≥ m - 1`; fixed shorter windows can be enlarged while ignoring the extra cells.

- `free_middle`: suppose the rank is at least `-K W` on late rows and never increases along their double steps. Then `h` is conserved on every closed walk of overlapping windows, in the sense of the kit's `Rule30LocalConservation.CyclicConserved`. By the kit's `cyclic_conserved_iff_shift_coboundary`, `h` is a constant plus a shift coboundary (`free_middle_coboundary`).
- `rank_local`: once both windows have at least `m - 1` cells, such a rank is a function of (width, wall window, edge window) alone.
- `no_local_ranking_late`: no function of (width, wall window, edge window) is nonnegative on late rows and strictly decreases along their double steps.
- `no_additive_ranking_late`: hence no rank of the additive form does either.
- `lower_bound_needed`: the lower bound cannot be dropped. Popcount minus `W²` strictly decreases along every surviving double step of every finite row, and popcount is not a constant plus a coboundary.

Survival short of the whole row therefore puts no constraint on additive potentials beyond the boundary windows.

## 2. Why the middle is free

Survival through time `T` reads only the depths `1, …, T + 1` of the start, because that is where the light cone of depth `1` at time `T` ends. The two baseline checks at times `0` and `2` are required as well. Thus all the check conditions of a late row lie inside the prefix of length `B(W) = max(3, max(W - u(W), 0) + 1)`. The number of depths beyond that sufficient prefix is `max(W - B(W), 0) = min(max(W - 3, 0), max(u(W) - 1, 0))`. It tends to infinity with `W`, even when `u(W)` exceeds `W`. Exact width fixes the top cell, and the boundary labels and interfaces use a fixed further number of cells; the remaining middle still grows without bound.

The proof plants a cyclic word `d` in that free part. Its row (`mkRow`) has three parts:
- the stripe `…10101` on the first `D` depths;
- `μ + 2` periods of `d`;
- an edge label of `e` cells on top.

The stripe is a fixed point of the zero-boundary dynamics (`zrow_stripe`), so a long enough stripe makes the row, and its double step, late. After four steps the windows inside the stripe are unchanged. Each period of `d` contributes exactly the four-step rise of `d` (`rho`), up to a bounded error from the two interfaces and the edge (`rise_mkRow`).

## 3. The proof

Suppose some cyclic word `d` of length `N ≥ m + 8` has a positive four-step rise `ρ`.
- **The rows.** Build planted rows of widths `W₀ + 4n` whose middles hold `μₙ + 2` periods of `d`, with `μₙ` chosen from `u` so that the rows stay late and `μₙ → ∞`.
- **The labels.** Each row's edge label is the edge window the previous row has four steps later (`labels`). Then `Bₙ = β(W₀ + 4n, stripe wall, label n)` is the same number at the end of one step and the start of the next.
- **Descent.** Descent along two double steps gives `Bₙ₊₁ ≤ Bₙ − μₙ ρ + C`, with `C` independent of `n`.
- **The lower bound.** It gives `Bₙ ≥ −(K + H)(W₀ + 4n)`, where `H` bounds `|h|`.
- **Contradiction.** Since `μₙ → ∞`, the descent eventually drives `Bₙ` down faster than the lower bound allows (`rho_nonpos_of_descent`).

So no cyclic word of length at least `m + 8` has a positive rise. Balance rules out negative rises too.
- **Balance.** Summed over all `2^N` cyclic words of a length `N ≥ m + 8`, the four-step rise is zero (`wsum_rho`). The four-step image of an `(m + 8)`-cell word is `2⁸`-to-one onto the `m`-cell words (`wsum_image`), and so is the crop to its middle `m` cells (`wsum_crop`). The image count is left permutivity: the leftmost cell enters each output by exclusive or.
- **Closed walks.** Every closed walk of the kit's form is, after repetition, a cyclic word of length at least `m + 8` (`closed_weight_eq_rho`). That gives `CyclicConserved` (`cyclic_conserved_of_rho`).

For the restricted B2 (`no_local_ranking_late`), the kit's own proof works after one change. It uses the truncated stripes `trunc n` and finitely many of their double steps, up to some `j₂`. Those rows are late once `u ≥ 4 j₂ + 2` at their widths, and long enough truncations ensure that.

## 4. Scope

- **Densities.** The densities are integer-valued; rational densities reduce to integer ones by clearing denominators.
- **The margin.** `u` must tend to infinity. A bounded margin is not covered: it leaves only a bounded reservoir by this construction. The case `u = 0` requires checks through the whole width. No claim about the bounded-margin case follows from this theorem.
- **Which rows.** As in the kit's barriers, the late population includes rows that are not the left half of rule 30 under an alternating centre.
- **Not claimed.** Nothing here bears on nonlinear or nonlocal rankings, decides `Q01`, or proves Problem 1.

## 5. Worked numbers

The cell below checks balance and the planted rise by direct computation.
- **Balance.** It takes popcount on cyclic words of length `9`, and the count of `11` on cyclic words of length `10`. For each it lists the total four-step rise over all words, the largest rise, and the numbers of words whose rise is positive and negative.
- **The planted rise.** It takes a cyclic word `d` of length `9` whose popcount rise, read from its deep end, is largest. It plants `μ + 2` periods of `d` after a stripe of `12` depths, under one black top cell, and reports the four-step popcount change of that row. The change grows by exactly the rise of `d` with each step of `μ`.

```wl
cstep[x_] := MapThread[BitXor[#1, BitOr[#2, #3]] &, {RotateRight[x], x, RotateLeft[x]}];
rise[x_, h_, m_] := With[{y = Nest[cstep, x, 4]}, Total[h /@ Partition[y, m, 1, 1]] - Total[h /@ Partition[x, m, 1, 1]]];
stats[n_, h_, m_] := With[{r = rise[#, h, m] & /@ Tuples[{0, 1}, n]}, {Total[r], Max[r], Count[r, _?Positive], Count[r, _?Negative]}];
pop[w_] := First[w];
c11[w_] := Boole[w === {1, 1}];
words = Tuples[{0, 1}, 9];
maxRise = Max[rise[Reverse[#], pop, 1] & /@ words];
best = Last[Select[words, rise[Reverse[#], pop, 1] == maxRise &]];
row[D_, mu_, d_] := With[{n = Length[d], q = (mu + 2) Length[d]}, Join[{0}, Table[Which[k <= D, Mod[k, 2], k <= D + q, d[[Mod[k, n] + 1]], True, 1], {k, D + q + 1}]]];
zstep[s_] := With[{t = Join[s, {0, 0}]}, Join[{0}, Table[BitXor[t[[k + 2]], BitOr[t[[k + 1]], t[[k]]]], {k, 1, Length[t] - 2}]]];
changes = Table[With[{s = row[12, mu, best]}, Total[Rest[Nest[zstep, s, 4]]] - Total[Rest[s]]], {mu, 0, 6}];
{stats[9, pop, 1], stats[10, c11, 2], best, maxRise, changes}
```

## 6. Prior art and scope

- **The kit.** The kit's B2 (`Rule30ZeroBoundaryBarriers.no_local_ranking`) and its classification of conserved densities (`Rule30LocalConservation`) are used, not reproved. The latter cites T. Hattori and S. Takesue, Physica D 49 (1991), 295–322. The balance of left-permutive maps is classical (G. A. Hedlund, Math. Systems Theory 3 (1969), 320–375).
- **rule30-open.** [`lhallee/rule30-open`'s note on conservation laws](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/structure/conservation-laws.md) finds no additive conservation law on the single cell's orbit or on block counts. Its orbit and finite-width searches remain computations; it also cites the kit's all-width classification of conserved densities. Neither those searches nor that classification supplies a nonincrease-to-conservation argument on the late population. We retain the late-population additive-rank theorem as the additional formal statement, without a broader priority claim.
- **Where it came from.** The statement and a first proof came from a sub-agent run of our programme. GPT carried it, with repairs to the balance step, to the restriction to the late population and to the role of the lower bound.

What is new here, in Lean, is the barrier for the late population, with additive densities and its necessary lower bound. Nothing here proves `Q01` or Problem 1.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundaryBarriers` and `Rule30LocalConservation`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers
import Ruliology.CellularAutomata.Rule30LocalConservation
/-!
# Rule 30, zero-boundary left half: survival short of the whole row does not restrict additive ranks

`Rule30ZeroBoundaryBarriers.no_local_ranking` shows that no function of (width, wall window, edge
window) strictly decreases along every surviving double step of every finite start. This module
asks the same of a smaller population and a larger class of ranks.

**The late population.** Fix `u : Nat → Nat` tending to infinity (`ToInfty u`). `Late u s W` holds
for a finite row `s` of width `W` whose double step survives and which keeps depth `1` black at
every even time up to `W - u W`. The cutoff is natural subtraction, `max (W - u W) 0`; no sublinear-growth
assumption on `u` is made, so the cutoff need not be asymptotic to `W`.

**The ranks.** `rank w e m β h s W = β W (wallW w s) (edgeW e s W) + dens m h s W`: an arbitrary
integer function of the width and the two boundary windows, plus an integer density `h` summed over
the `m`-cell windows of the row (`dens`, each window read from its deep end, which is the
left-to-right order of the cells).

* `no_local_ranking_late`: no function of (width, wall window, edge window) is nonnegative on the
  late population and strictly decreases along each of its double steps.
* `free_middle`: if `rank ≥ -K W` on the late population and the rank never increases along its
  double steps, then `h` is conserved on every closed walk in the sense of
  `Rule30LocalConservation.CyclicConserved`, and so it is a constant plus a shift coboundary
  (`free_middle_coboundary`, by the kit's `cyclic_conserved_iff_shift_coboundary`).
* `rank_local`: for such an `h`, once `w` and `e` are at least `m - 1`, the rank is a function of
  (width, wall window, edge window) alone.
* `no_additive_ranking_late`: hence no rank of this form is nonnegative on the late population and
  strictly decreases along each of its double steps.
* `lower_bound_needed`: the lower bound cannot be dropped: popcount minus `W ^ 2` strictly decreases
  along every surviving double step of every finite row, and popcount is not a coboundary.

**Method.** A cyclic word `d` with a positive four-step rise (`rho`) is planted in the middle of a
row: the stripe `…10101` on the first `D` depths, `μ + 2` periods of `d`, and an edge label on top
(`mkRow`). The stripe keeps the row late, the middle is free because survival through `W - u W`
never sees it, and four steps raise the density by at least `μ` times the rise of `d` minus a
bounded error (`rise_mkRow`). Following the edge labels from row to row (`labels`) gives widths
`W0 + 4 n` along which `β` must fall faster than any linear bound once `μ` grows with `u`, which the
lower bound forbids (`rho_nonpos_of_descent`). Negative rises are excluded by balance: summed over
all cyclic words of a length `N ≥ m + 8`, the rise is zero (`wsum_rho`), because the four-step image
of an `(m + 8)`-cell word is `2 ^ 8`-to-one onto `m`-cell words (`wsum_image`) and so is the crop
(`wsum_crop`). Closed walks of the kit's form are cyclic words (`closed_weight_eq_rho`,
`cyclic_conserved_of_rho`).

Scope: integer densities only (rational ones follow by clearing denominators); `u` must tend to
infinity, and a bounded margin is not covered; the late population includes rows that are not the
left half of rule 30 under an alternating centre. Nothing here decides `Q01` or Problem 1. The
classification of conserved densities is the kit's; absence-of-conservation and balance arguments
for permutive cellular automata have a long literature (G. A. Hedlund, Endomorphisms and
automorphisms of the shift dynamical system, Math. Systems Theory 3 (1969), 320-375; T. Hattori and
S. Takesue, Physica D 49 (1991), 295-322).
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30ZeroBoundary Rule30ZeroBoundaryBarriers

/-! ### Late survivors -/

/-- `u` tends to infinity. -/
def ToInfty (u : Nat → Nat) : Prop := ∀ N, ∃ W0, ∀ W, W0 ≤ W → N ≤ u W

/-- The late population for the margin `u`: finite rows of width `W` whose double step survives
and which pass every even check of depth `1` through time `W - u W`. -/
def Late (u : Nat → Nat) (s : Nat → Bool) (W : Nat) : Prop :=
  1 ≤ W ∧ s W = true ∧ (∀ k, W < k → s k = false) ∧ Survives s ∧
    ∀ i, 2 * i ≤ W - u W → zrow s (2 * i) 1 = true

theorem iter_late {u : Nat → Nat} {n j W0 : Nat} (hn : n % 2 = 1) (hW : W0 ≤ n + 2 * j)
    (hu : ∀ W, W0 ≤ W → 4 * j + 2 ≤ u W) (hj : 2 * j + 2 ≤ n) (h1 : 1 ≤ n) :
    Late u (iter (trunc n) j) (n + 2 * j) := by
  have hw := zrow_edge (L := trunc n) (m := n) h1 (trunc_width hn).1 (trunc_width hn).2 (2 * j)
  refine ⟨by omega, hw.1, hw.2, iter_survives hn hj, fun i hi => ?_⟩
  have := hu (n + 2 * j) hW
  rw [iter_zrow]
  exact (trunc_survives hn).1 _ (by omega)

/-- **B2 for late survivors.** Let `u` tend to infinity. No integer function of (width, wall
window, edge window) is nonnegative on the late population and strictly decreases along each of
its double steps. The kit's `no_local_ranking` is the case of all surviving double steps; here the
rank need only decrease on rows that still pass every check through `W - u W`. -/
theorem no_local_ranking_late (w e : Nat) (u : Nat → Nat) (hu : ToInfty u)
    (R : Nat → List Bool → List Bool → Int)
    (hpos : ∀ s W, Late u s W → 0 ≤ R W (wallW w s) (edgeW e s W))
    (hdesc : ∀ s W, Late u s W →
      R (W + 2) (wallW w (dstep s)) (edgeW e (dstep s) (W + 2)) < R W (wallW w s) (edgeW e s W)) :
    False := by
  let n0 := 2 * e + 1
  have hn0 : n0 % 2 = 1 := by omega
  let E : Nat → List Bool := fun j => edgeW e (iter (trunc n0) j) (n0 + 2 * j)
  obtain ⟨j1, j2, hlt, -, hE⟩ := pigeonhole e E (fun j => by simp [E, edgeW])
  obtain ⟨W0, hW0⟩ := hu (4 * j2 + 2)
  let S := wallW w stripe
  let N0 := 2 * j2 + w + 2 + W0
  have late : ∀ m, N0 ≤ m → ∀ j, j ≤ j2 → Late u (iter (trunc (n0 + 2 * m)) j) (n0 + 2 * m + 2 * j) := by
    intro m hm j hj
    exact iter_late (W0 := W0) (by omega) (by omega) (fun W hW => by have := hW0 W hW; omega) (by omega) (by omega)
  have labels : ∀ m, N0 ≤ m → ∀ j, j ≤ j2 →
      wallW w (iter (trunc (n0 + 2 * m)) j) = S ∧
        edgeW e (iter (trunc (n0 + 2 * m)) j) (n0 + 2 * m + 2 * j) = E j := by
    intro m hm j hj
    have hn : (n0 + 2 * m) % 2 = 1 := by omega
    exact ⟨wall_iter hn w j (by omega), edge_iter n0 m e j (by omega)⟩
  have stepR : ∀ m, N0 ≤ m → ∀ j, j < j2 →
      R (n0 + 2 * m + 2 * (j + 1)) S (E (j + 1)) + 1 ≤ R (n0 + 2 * m + 2 * j) S (E j) := by
    intro m hm j hj
    have hstep := hdesc _ _ (late m hm j (by omega))
    have hit : dstep (iter (trunc (n0 + 2 * m)) j) = iter (trunc (n0 + 2 * m)) (j + 1) :=
      (iter_dstep _ j).symm
    rw [hit, (labels m hm (j + 1) (by omega)).1, (labels m hm j (by omega)).1,
      show n0 + 2 * m + 2 * j + 2 = n0 + 2 * m + 2 * (j + 1) by omega,
      (labels m hm (j + 1) (by omega)).2, (labels m hm j (by omega)).2] at hstep
    omega
  have chain : ∀ m, N0 ≤ m → ∀ i, i ≤ j2 - j1 →
      R (n0 + 2 * m + 2 * (j1 + i)) S (E (j1 + i)) + i ≤ R (n0 + 2 * m + 2 * j1) S (E j1) := by
    intro m hm i
    induction i with
    | zero => intro _; simp
    | succ i ih =>
      intro hi
      have ih' := ih (by omega)
      have h := stepR m hm (j1 + i) (by omega)
      rw [show j1 + (i + 1) = j1 + i + 1 by omega]
      push_cast
      omega
  let P := j2 - j1
  have hP : 1 ≤ P := by omega
  let f : Nat → Int := fun M => R M S (E j1)
  have period : ∀ m, N0 ≤ m → f (n0 + 2 * m + 2 * j1 + 2 * P) + P ≤ f (n0 + 2 * m + 2 * j1) := by
    intro m hm
    have h := chain m hm P (Nat.le_refl _)
    rw [show j1 + P = j2 by omega, ← hE,
      show n0 + 2 * m + 2 * j2 = n0 + 2 * m + 2 * j1 + 2 * P by omega] at h
    exact h
  let B := n0 + 2 * N0 + 2 * j1
  have descent : ∀ k : Nat, f (B + 2 * (k * P)) + (k * P : Nat) ≤ f B := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      have e1 : (k + 1) * P = k * P + P := Nat.succ_mul k P
      have h := period (N0 + k * P) (by omega)
      have e2 : n0 + 2 * (N0 + k * P) + 2 * j1 = B + 2 * (k * P) := by omega
      have e3 : B + 2 * ((k + 1) * P) = B + 2 * (k * P) + 2 * P := by rw [e1]; omega
      rw [e2] at h
      rw [e3, e1]
      push_cast at h ih ⊢
      omega
  have nonneg : ∀ k : Nat, 0 ≤ f (B + 2 * (k * P)) := by
    intro k
    have h := hpos _ _ (late (N0 + k * P) (by omega) j1 (by omega))
    rw [(labels _ (by omega) j1 (by omega)).1, (labels _ (by omega) j1 (by omega)).2,
      show n0 + 2 * (N0 + k * P) + 2 * j1 = B + 2 * (k * P) by omega] at h
    exact h
  let k := (f B).toNat + 1
  have h1 := descent k
  have h2 := nonneg k
  have hk : k ≤ k * P := Nat.le_mul_of_pos_right _ hP
  have h3 : (f B) ≤ ((f B).toNat : Int) := Int.self_le_toNat (f B)
  have : ((k * P : Nat) : Int) ≥ (k : Int) := by exact_mod_cast hk
  simp only [k] at this
  push_cast at this
  omega

/-! ### Finite sums -/

/-- `sumR n f = f 0 + ⋯ + f (n - 1)`. -/
def sumR : Nat → (Nat → Int) → Int
  | 0, _ => 0
  | n + 1, f => sumR n f + f n

theorem sumR_congr {n : Nat} {f g : Nat → Int} (h : ∀ i, i < n → f i = g i) :
    sumR n f = sumR n g := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [sumR]; rw [ih (fun i hi => h i (by omega)), h n (by omega)]

theorem sumR_add (a b : Nat) (f : Nat → Int) :
    sumR (a + b) f = sumR a f + sumR b (fun i => f (a + i)) := by
  induction b with
  | zero => simp [sumR]
  | succ b ih => rw [show a + (b + 1) = (a + b) + 1 by omega]; simp only [sumR]; rw [ih]; omega

theorem sumR_succ' (n : Nat) (f : Nat → Int) :
    sumR (n + 1) f = f 0 + sumR n (fun i => f (i + 1)) := by
  have h := sumR_add 1 n f
  rw [show 1 + n = n + 1 by omega] at h
  rw [h, sumR_congr (n := n) (f := fun i => f (1 + i)) (g := fun i => f (i + 1))
    (fun i _ => by rw [Nat.add_comm])]
  simp [sumR]

theorem sumR_zero {n : Nat} {f : Nat → Int} (h : ∀ i, i < n → f i = 0) : sumR n f = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [sumR]; rw [ih (fun i hi => h i (by omega)), h n (by omega)]; rfl

theorem sumR_lower {n : Nat} {f : Nat → Int} {B : Int} (h : ∀ i, i < n → -B ≤ f i) :
    -((n : Int) * B) ≤ sumR n f := by
  induction n with
  | zero => simp [sumR]
  | succ n ih =>
    simp only [sumR]
    have h1 := ih (fun i hi => h i (by omega))
    have h2 := h n (by omega)
    have e : ((n + 1 : Nat) : Int) * B = (n : Int) * B + B := by push_cast; rw [Int.add_mul, Int.one_mul]
    rw [e]; omega

theorem sumR_upper {n : Nat} {f : Nat → Int} {B : Int} (h : ∀ i, i < n → f i ≤ B) :
    sumR n f ≤ (n : Int) * B := by
  induction n with
  | zero => simp [sumR]
  | succ n ih =>
    simp only [sumR]
    have h1 := ih (fun i hi => h i (by omega))
    have h2 := h n (by omega)
    have e : ((n + 1 : Nat) : Int) * B = (n : Int) * B + B := by push_cast; rw [Int.add_mul, Int.one_mul]
    rw [e]; omega

/-- A sum over one period of an `N`-periodic sequence does not depend on where it starts. -/
theorem sumR_periodic {N : Nat} {g : Nat → Int} (hp : ∀ i, g (i + N) = g i) (a : Nat) :
    sumR N (fun i => g (a + i)) = sumR N g := by
  induction a with
  | zero => exact sumR_congr (fun i _ => by rw [Nat.zero_add])
  | succ a ih =>
    have h1 : sumR (N + 1) (fun i => g (a + i)) = sumR N (fun i => g (a + i)) + g (a + N) := rfl
    have h2 : sumR (N + 1) (fun i => g (a + i)) = g a + sumR N (fun i => g (a + 1 + i)) := by
      rw [sumR_succ']; simp only [Nat.add_zero]; congr 1
      exact sumR_congr (fun i _ => by rw [Nat.add_assoc, Nat.add_comm i 1])
    have h4 : g (a + N) = g a := hp a
    omega

theorem sumR_blocks {N : Nat} {g : Nat → Int} (hp : ∀ i, g (i + N) = g i) (a μ : Nat) :
    sumR (μ * N) (fun i => g (a + i)) = (μ : Int) * sumR N g := by
  induction μ with
  | zero => simp [sumR]
  | succ μ ih =>
    rw [Nat.succ_mul, sumR_add, ih]
    have h := sumR_periodic hp (a + μ * N)
    rw [sumR_congr (n := N) (f := fun i => g (a + (μ * N + i))) (g := fun i => g (a + μ * N + i))
      (fun i _ => by rw [Nat.add_assoc]), h]
    push_cast; rw [Int.add_mul, Int.one_mul]

theorem sumR_rev (n : Nat) (f : Nat → Int) : sumR n (fun i => f (n - 1 - i)) = sumR n f := by
  induction n generalizing f with
  | zero => rfl
  | succ n ih =>
    have e1 : sumR (n + 1) (fun i => f (n + 1 - 1 - i)) =
        sumR n (fun i => f (n + 1 - 1 - i)) + f (n + 1 - 1 - n) := rfl
    have e2 : sumR n (fun i => f (n + 1 - 1 - i)) = sumR n (fun i => (fun j => f (j + 1)) (n - 1 - i)) :=
      sumR_congr (fun i hi => by simp only; congr 1; omega)
    rw [e1, e2, ih (fun j => f (j + 1)), sumR_succ' n f, show n + 1 - 1 - n = 0 by omega]
    omega

/-! ### Sums over all words of a length -/

/-- `wsum n φ` sums `φ` over all `2 ^ n` Boolean words of length `n`. -/
def wsum : Nat → (List Bool → Int) → Int
  | 0, φ => φ []
  | n + 1, φ => wsum n (fun v => φ (false :: v)) + wsum n (fun v => φ (true :: v))

theorem wsum_congr {n : Nat} {φ ψ : List Bool → Int} (h : ∀ v, v.length = n → φ v = ψ v) :
    wsum n φ = wsum n ψ := by
  induction n generalizing φ ψ with
  | zero => exact h [] rfl
  | succ n ih =>
    simp only [wsum]
    rw [ih (fun v hv => h (false :: v) (by simp [hv])), ih (fun v hv => h (true :: v) (by simp [hv]))]

theorem wsum_add (n : Nat) (φ ψ : List Bool → Int) :
    wsum n (fun v => φ v + ψ v) = wsum n φ + wsum n ψ := by
  induction n generalizing φ ψ with
  | zero => rfl
  | succ n ih =>
    simp only [wsum]
    rw [ih (fun v => φ (false :: v)) (fun v => ψ (false :: v)),
      ih (fun v => φ (true :: v)) (fun v => ψ (true :: v))]
    omega

theorem wsum_sub (n : Nat) (φ ψ : List Bool → Int) :
    wsum n (fun v => φ v - ψ v) = wsum n φ - wsum n ψ := by
  induction n generalizing φ ψ with
  | zero => rfl
  | succ n ih =>
    simp only [wsum]
    rw [ih (fun v => φ (false :: v)) (fun v => ψ (false :: v)),
      ih (fun v => φ (true :: v)) (fun v => ψ (true :: v))]
    omega

theorem wsum_mul (n : Nat) (c : Int) (φ : List Bool → Int) :
    wsum n (fun v => c * φ v) = c * wsum n φ := by
  induction n generalizing φ with
  | zero => rfl
  | succ n ih =>
    simp only [wsum]
    rw [ih (fun v => φ (false :: v)), ih (fun v => φ (true :: v)), Int.mul_add]

theorem wsum_const (n : Nat) (c : Int) : wsum n (fun _ => c) = (2 : Int) ^ n * c := by
  induction n with
  | zero => simp [wsum]
  | succ n ih =>
    simp only [wsum]
    rw [ih, Int.pow_succ, Int.mul_comm ((2 : Int) ^ n) 2, Int.mul_assoc]
    omega

/-- Fubini: a word of length `a + b` is a word of length `a` followed by one of length `b`. -/
theorem wsum_append (a b : Nat) (φ : List Bool → Int) :
    wsum (a + b) φ = wsum a (fun u => wsum b (fun v => φ (u ++ v))) := by
  induction a generalizing φ with
  | zero => simp only [Nat.zero_add]; rfl
  | succ a ih =>
    rw [Nat.add_right_comm]
    simp only [wsum]
    rw [ih (fun v => φ (false :: v)), ih (fun v => φ (true :: v))]
    rfl

theorem wsum_snoc (n : Nat) (φ : List Bool → Int) :
    wsum (n + 1) φ = wsum n (fun v => φ (v ++ [false])) + wsum n (fun v => φ (v ++ [true])) := by
  rw [wsum_append n 1, ← wsum_add]
  rfl

theorem wsum_rot (n : Nat) (φ : List Bool → Int) :
    wsum (n + 1) (fun v => φ (v.drop 1 ++ v.take 1)) = wsum (n + 1) φ := by
  rw [wsum_snoc n φ]
  rfl

theorem rotate_succ (v : List Bool) (i : Nat) (hi : i < v.length) :
    (v.drop i ++ v.take i).drop 1 ++ (v.drop i ++ v.take i).take 1 = v.drop (i + 1) ++ v.take (i + 1) := by
  have hd : v.drop i = v[i] :: v.drop (i + 1) := List.drop_eq_getElem_cons hi
  have ht : v.take (i + 1) = v.take i ++ [v[i]] := by
    rw [List.take_add_one, List.getElem?_eq_getElem hi]; rfl
  rw [hd, ht]
  show (v.drop (i + 1) ++ v.take i) ++ [v[i]] = v.drop (i + 1) ++ (v.take i ++ [v[i]])
  rw [List.append_assoc]

/-- Rotation does not change a sum over all words. -/
theorem wsum_rotate (n : Nat) (φ : List Bool → Int) (i : Nat) (hi : i ≤ n) :
    wsum n (fun v => φ (v.drop i ++ v.take i)) = wsum n φ := by
  induction i generalizing φ with
  | zero => simp
  | succ i ih =>
    obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
    rw [wsum_congr (ψ := fun v => (fun x => φ (x.drop 1 ++ x.take 1)) (v.drop i ++ v.take i))
      (fun v hv => by simp only; rw [rotate_succ v i (by omega)]),
      ih (fun x => φ (x.drop 1 ++ x.take 1)) (by omega), wsum_rot]

theorem wsum_reverse (n : Nat) (φ : List Bool → Int) : wsum n (fun v => φ v.reverse) = wsum n φ := by
  induction n generalizing φ with
  | zero => rfl
  | succ n ih =>
    show wsum n (fun v => φ (false :: v).reverse) + wsum n (fun v => φ (true :: v).reverse) = wsum (n + 1) φ
    simp only [List.reverse_cons]
    rw [ih (fun v => φ (v ++ [false])), ih (fun v => φ (v ++ [true])), ← wsum_snoc]

theorem wsum_take (L r : Nat) (φ : List Bool → Int) :
    wsum (L + r) (fun v => φ (v.take L)) = (2 : Int) ^ r * wsum L φ := by
  rw [wsum_append, wsum_congr (ψ := fun u => (2 : Int) ^ r * φ u)
    (fun u hu => by
      rw [wsum_congr (ψ := fun _ => φ u) (fun v _ => by rw [← hu, List.take_left]), wsum_const]),
    wsum_mul]

theorem wsum_nonpos {n : Nat} {φ : List Bool → Int} (h : ∀ v, v.length = n → φ v ≤ 0) : wsum n φ ≤ 0 := by
  induction n generalizing φ with
  | zero => exact h [] rfl
  | succ n ih =>
    simp only [wsum]
    have h1 := ih (φ := fun v => φ (false :: v)) (fun v hv => h _ (by simp [hv]))
    have h2 := ih (φ := fun v => φ (true :: v)) (fun v hv => h _ (by simp [hv]))
    omega

theorem wsum_le_term {n : Nat} {φ : List Bool → Int} (h : ∀ v, v.length = n → φ v ≤ 0) :
    ∀ v, v.length = n → wsum n φ ≤ φ v := by
  induction n generalizing φ with
  | zero => intro v hv; rw [List.eq_nil_of_length_eq_zero hv]; exact Int.le_refl _
  | succ n ih =>
    intro v hv
    cases v with
    | nil => simp at hv
    | cons b v =>
      simp only [List.length_cons, Nat.add_right_cancel_iff] at hv
      simp only [wsum]
      have hf := wsum_nonpos (n := n) (φ := fun x => φ (false :: x)) (fun x hx => h _ (by simp [hx]))
      have ht := wsum_nonpos (n := n) (φ := fun x => φ (true :: x)) (fun x hx => h _ (by simp [hx]))
      cases b
      · have := ih (φ := fun x => φ (false :: x)) (fun x hx => h _ (by simp [hx])) v hv
        omega
      · have := ih (φ := fun x => φ (true :: x)) (fun x hx => h _ (by simp [hx])) v hv
        omega

theorem term_le_wsum {n : Nat} {φ : List Bool → Int} (h : ∀ v, v.length = n → 0 ≤ φ v) :
    ∀ v, v.length = n → φ v ≤ wsum n φ := by
  intro v hv
  have := wsum_le_term (φ := fun v => -φ v) (fun v hv => by have := h v hv; omega) v hv
  have e : wsum n (fun v => -φ v) = -wsum n φ := by
    have := wsum_mul n (-1) φ
    rw [wsum_congr (ψ := fun v => -1 * φ v) (fun v _ => by omega), this]; omega
  omega

theorem wsum_sumR (N n : Nat) (G : Nat → List Bool → Int) :
    wsum N (fun d => sumR n (fun a => G a d)) = sumR n (fun a => wsum N (G a)) := by
  induction n with
  | zero => simp only [sumR]; rw [wsum_const, Int.mul_zero]
  | succ n ih => simp only [sumR]; rw [wsum_add, ih]

/-! ### Depth windows -/

/-- The window of depths `a, …, a + n - 1` of a row, read from the deep end: `[f (a+n-1), …, f a]`.
This is the left-to-right order of the cells, so the kit's word operations apply directly. -/
def dwin (f : Nat → Bool) (a : Nat) : Nat → List Bool
  | 0 => []
  | n + 1 => f (a + n) :: dwin f a n

theorem dwin_length (f : Nat → Bool) (a n : Nat) : (dwin f a n).length = n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [dwin, ih]

theorem dwin_congr {f g : Nat → Bool} {a n : Nat} (h : ∀ j, a ≤ j → j < a + n → f j = g j) :
    dwin f a n = dwin g a n := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [dwin]; rw [h (a + n) (by omega) (by omega), ih (fun j h1 h2 => h j h1 (by omega))]

theorem dwin_getD (f : Nat → Bool) (a n t : Nat) (ht : t < n) :
    (dwin f a n).getD t false = f (a + n - 1 - t) := by
  induction n generalizing t with
  | zero => omega
  | succ n ih =>
    cases t with
    | zero => simp [dwin]
    | succ t =>
      simp only [dwin, List.getD_cons_succ]
      rw [ih t (by omega)]; congr 1; omega

theorem dwin_split (f : Nat → Bool) (a n k : Nat) : dwin f a (n + k) = dwin f (a + k) n ++ dwin f a k := by
  induction n with
  | zero => simp [dwin]
  | succ n ih =>
    rw [show n + 1 + k = (n + k) + 1 by omega]
    simp only [dwin, ih, List.cons_append]
    congr 1; rw [Nat.add_assoc, Nat.add_comm k n]

/-- One Rule 30 update of a window, in depth coordinates. -/
theorem shrink_dwin (s : Nat → Bool) (t a n : Nat) :
    Rule30LocalConservation.Corner.shrink (dwin (zrow s t) a (n + 2)) = dwin (zrow s (t + 1)) (a + 1) n := by
  induction n with
  | zero => simp [dwin, Rule30LocalConservation.Corner.shrink]
  | succ n ih =>
    show Rule30LocalConservation.Corner.shrink
        (zrow s t (a + (n + 2)) :: zrow s t (a + (n + 1)) :: zrow s t (a + n) :: dwin (zrow s t) a n) =
      zrow s (t + 1) (a + 1 + n) :: dwin (zrow s (t + 1)) (a + 1) n
    rw [Rule30LocalConservation.Corner.shrink]
    rw [← ih]
    simp only [dwin]
    congr 1
    rw [zrow_succ' (k := a + 1 + n) (by omega), show a + 1 + n + 1 = a + (n + 2) by omega,
      show a + 1 + n = a + (n + 1) by omega, show a + (n + 1) - 1 = a + n by omega]
    rfl

theorem four_dwin (s : Nat → Bool) (a n : Nat) :
    Rule30LocalConservation.Corner.four (dwin (zrow s 0) a (n + 8)) = dwin (zrow s 4) (a + 4) n := by
  unfold Rule30LocalConservation.Corner.four
  rw [shrink_dwin s 0 a (n + 6), shrink_dwin s 1 (a + 1) (n + 4), shrink_dwin s 2 (a + 2) (n + 2),
    shrink_dwin s 3 (a + 3) n]

theorem image_dwin (s : Nat → Bool) (a n : Nat) :
    Rule30LocalConservation.Corner.image (dwin (zrow s 0) a (n + 8)) = dwin (zrow s 4) (a + 4) n := by
  rw [Rule30LocalConservation.Word.image_eq_four, four_dwin]

theorem crop_dwin (f : Nat → Bool) (a m : Nat) :
    Rule30LocalConservation.Word.crop m (dwin f a (m + 8)) = dwin f (a + 4) m := by
  unfold Rule30LocalConservation.Word.crop
  rw [show m + 8 = 4 + (m + 4) by omega, dwin_split f a 4 (m + 4),
    List.drop_left' (by rw [dwin_length]), show m + 4 = m + 4 by rfl, dwin_split f a m 4,
    List.take_left' (by rw [dwin_length])]

/-- The four-step change of an additive density, read on a window of a row. -/
theorem change_dwin (s : Nat → Bool) (m : Nat) (h : List Bool → Int) (a : Nat) :
    Rule30LocalConservation.Cycle.change m h (dwin (zrow s 0) a (m + 8)) =
      h (dwin (zrow s 4) (a + 4) m) - h (dwin (zrow s 0) (a + 4) m) := by
  unfold Rule30LocalConservation.Cycle.change
  rw [image_dwin, crop_dwin]

/-! ### Balance: the four-step image is `2 ^ 8`-to-one on windows -/

open Rule30LocalConservation in
theorem image_cons' (a : Bool) (xs : List Bool) (h : 8 ≤ xs.length) :
    Corner.image (a :: xs) = Corner.q a xs :: Corner.image xs := by
  simp [Corner.image, h]

open Rule30LocalConservation in
/-- Every word of length `m` is the four-step image of exactly `2 ^ 8` words of length `m + 8`. -/
theorem wsum_image (m : Nat) (φ : List Bool → Int) :
    wsum (m + 8) (fun y => φ (Corner.image y)) = 256 * wsum m φ := by
  induction m generalizing φ with
  | zero =>
    rw [wsum_congr (ψ := fun _ => φ []) (fun y hy => by
      rw [List.eq_nil_of_length_eq_zero (by rw [Word.image_length, hy] : (Corner.image y).length = 0)]),
      wsum_const]
    rfl
  | succ m ih =>
    rw [show m + 1 + 8 = (m + 8) + 1 by omega]
    show wsum (m + 8) (fun v => φ (Corner.image (false :: v))) +
      wsum (m + 8) (fun v => φ (Corner.image (true :: v))) = 256 * wsum (m + 1) φ
    rw [← wsum_add]
    rw [wsum_congr (ψ := fun v => φ (false :: Corner.image v) + φ (true :: Corner.image v))
      (fun v hv => by
        rw [image_cons' false v (by omega), image_cons' true v (by omega), Corner.q_left true v]
        cases Corner.q false v <;> simp <;> omega)]
    rw [wsum_add, ih (fun v => φ (false :: v)), ih (fun v => φ (true :: v))]
    show _ = 256 * (wsum m (fun v => φ (false :: v)) + wsum m (fun v => φ (true :: v)))
    omega

open Rule30LocalConservation in
theorem wsum_crop (m : Nat) (φ : List Bool → Int) :
    wsum (m + 8) (fun y => φ (Word.crop m y)) = 256 * wsum m φ := by
  rw [show m + 8 = 4 + (m + 4) by omega, wsum_append]
  rw [wsum_congr (ψ := fun _ => 16 * wsum m φ) (fun u hu => by
    unfold Word.crop
    rw [wsum_congr (ψ := fun v => φ (v.take m)) (fun v _ => by rw [← hu, List.drop_left]),
      wsum_take m 4 φ]
    rfl)]
  rw [wsum_const]
  show (16 : Int) * (16 * wsum m φ) = 256 * wsum m φ
  omega

open Rule30LocalConservation in
theorem wsum_change (m : Nat) (h : List Bool → Int) : wsum (m + 8) (Cycle.change m h) = 0 := by
  unfold Cycle.change
  rw [wsum_sub, wsum_image m h, wsum_crop m h]
  omega

/-! ### Cyclic words and the balance identity -/

theorem getD_of_lt (l : List Bool) (i : Nat) (h : i < l.length) : l.getD i false = l[i] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h]; rfl

/-- The periodic row of depths read from a cyclic word: depth `k` carries letter `k mod N`. -/
def zf (d : List Bool) (k : Nat) : Bool := d.getD (k % d.length) false

/-- The four-step rise of an additive density on the cyclic word `d`: the sum of the kit's
`change` over the `N` windows of one period. -/
def rho (m : Nat) (h : List Bool → Int) (d : List Bool) : Int :=
  sumR d.length (fun a => Rule30LocalConservation.Cycle.change m h (dwin (zf d) a (m + 8)))

theorem zf_periodic (d : List Bool) (k : Nat) : zf d (k + d.length) = zf d k := by
  unfold zf; rw [Nat.add_mod_right]

theorem mod_lt2 {x n : Nat} (h : x < 2 * n) : x % n = if x < n then x else x - n := by
  split
  · exact Nat.mod_eq_of_lt (by assumption)
  · rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]

theorem zf_rotate (d : List Bool) (a k : Nat) (ha : a < d.length) :
    zf (d.drop a ++ d.take a) k = zf d (k + a) := by
  unfold zf
  have hl : (d.drop a ++ d.take a).length = d.length := by simp; omega
  rw [hl]
  have hN : 0 < d.length := by omega
  have hj : k % d.length < d.length := Nat.mod_lt _ hN
  rw [Nat.add_mod, Nat.mod_eq_of_lt ha]
  rw [mod_lt2 (x := k % d.length + a) (n := d.length) (by omega)]
  have hdl : (d.drop a).length = d.length - a := List.length_drop
  by_cases hc : k % d.length < d.length - a
  · rw [ite_eq_left (by omega)]
    rw [getD_of_lt _ _ (by rw [hl]; omega), List.getElem_append_left (by rw [hdl]; omega),
      List.getElem_drop, getD_of_lt _ _ (by omega)]
    congr 1; omega
  · rw [ite_eq_right (by omega)]
    rw [getD_of_lt _ _ (by rw [hl]; omega), List.getElem_append_right (by rw [hdl]; omega),
      List.getElem_take, getD_of_lt _ _ (by omega)]
    congr 1; rw [hdl]; omega

theorem dwin_zf_zero (d : List Bool) (L : Nat) (hL : L ≤ d.length) : dwin (zf d) 0 L = (d.take L).reverse := by
  induction L with
  | zero => simp [dwin]
  | succ L ih =>
    simp only [dwin]
    rw [ih (by omega), List.take_add_one, List.getElem?_eq_getElem (by omega)]
    simp only [Option.toList, List.reverse_append, List.reverse_cons, List.reverse_nil, List.nil_append,
      List.cons_append, Nat.zero_add]
    congr 1
    unfold zf
    rw [Nat.mod_eq_of_lt (by omega), getD_of_lt _ _ (by omega)]

theorem dwin_shift (f : Nat → Bool) (a n : Nat) : dwin f a n = dwin (fun k => f (k + a)) 0 n := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [dwin]; rw [ih, Nat.zero_add, Nat.add_comm a n]

theorem dwin_zf (d : List Bool) (a L : Nat) (ha : a < d.length) (hL : L ≤ d.length) :
    dwin (zf d) a L = ((d.drop a ++ d.take a).take L).reverse := by
  rw [dwin_shift, ← dwin_zf_zero _ L (by simp; omega)]
  exact dwin_congr (fun j _ _ => (zf_rotate d a j ha).symm)

/-- **Balance.** Summed over all cyclic words of a length `N ≥ m + 8`, the four-step rise of any
integer density is zero. -/
theorem wsum_rho (m : Nat) (h : List Bool → Int) (N : Nat) (hN : m + 8 ≤ N) :
    wsum N (rho m h) = 0 := by
  rw [wsum_congr (ψ := fun d => sumR N (fun a =>
      Rule30LocalConservation.Cycle.change m h (dwin (zf d) a (m + 8)))) (fun d hd => by
    unfold rho; rw [hd]), wsum_sumR]
  apply sumR_zero
  intro a ha
  rw [wsum_congr (ψ := fun d => (fun x => Rule30LocalConservation.Cycle.change m h ((x.take (m + 8)).reverse))
      (d.drop a ++ d.take a)) (fun d hd => by
    simp only; rw [dwin_zf d a (m + 8) (by omega) (by omega)]),
    wsum_rotate N (fun x => Rule30LocalConservation.Cycle.change m h ((x.take (m + 8)).reverse)) a (by omega)]
  obtain ⟨r, rfl⟩ : ∃ r, N = (m + 8) + r := ⟨N - (m + 8), by omega⟩
  rw [wsum_take (m + 8) r (fun x => Rule30LocalConservation.Cycle.change m h x.reverse),
    wsum_reverse, wsum_change, Int.mul_zero]

/-- If no cyclic word of length `N ≥ m + 8` has a positive four-step rise, none has a negative
one either. -/
theorem rho_eq_zero (m : Nat) (h : List Bool → Int) (N : Nat) (hN : m + 8 ≤ N)
    (hle : ∀ d : List Bool, d.length = N → rho m h d ≤ 0) :
    ∀ d : List Bool, d.length = N → rho m h d = 0 := by
  intro d hd
  have h1 := wsum_le_term hle d hd
  rw [wsum_rho m h N hN] at h1
  have h2 := hle d hd
  omega

/-! ### From cyclic words to the kit's closed walks -/

theorem ext_getD {l1 l2 : List Bool} (hl : l1.length = l2.length)
    (h : ∀ t, t < l1.length → l1.getD t false = l2.getD t false) : l1 = l2 :=
  List.ext_getElem hl (fun t h1 h2 => by rw [← getD_of_lt _ _ h1, ← getD_of_lt _ _ h2]; exact h t h1)

theorem getD_map_range (L t : Nat) (g : Nat → Bool) (ht : t < L) :
    ((List.range L).map g).getD t false = g t := by
  rw [getD_of_lt _ _ (by simpa using ht)]; simp

theorem take_append_succ (xs : List Bool) (b : Bool) (bs : List Bool) :
    (xs ++ b :: bs).take (xs.length + 1) = xs ++ [b] := by
  induction xs with
  | nil => rfl
  | cons x xs ihx =>
    show (x :: (xs ++ b :: bs)).take (xs.length + 1 + 1) = x :: (xs ++ [b])
    rw [List.take_succ_cons, ihx]

open Rule30LocalConservation.Cycle in
theorem weight_eq_sumR (cost : List Bool → Int) (xs bs : List Bool) :
    weight cost xs bs = sumR bs.length (fun i => cost (((xs ++ bs).drop i).take (xs.length + 1))) := by
  induction bs generalizing xs with
  | nil => rfl
  | cons b bs ih =>
    rw [weight, ih (shift xs b), shift_length, List.length_cons, sumR_succ']
    have e : shift xs b ++ bs = (xs ++ b :: bs).drop 1 := by
      unfold shift
      rw [← List.drop_append_of_le_length (by simp), List.append_assoc, List.singleton_append]
    have e2 : (xs ++ b :: bs).take (xs.length + 1) = xs ++ [b] := take_append_succ xs b bs
    rw [List.drop_zero, e2, e]
    congr 1
    apply sumR_congr
    intro i _
    rw [List.drop_drop, Nat.add_comm 1 i]

/-- `k` copies of a word. -/
def rep : Nat → List Bool → List Bool
  | 0, _ => []
  | k + 1, l => l ++ rep k l

theorem rep_length (k : Nat) (l : List Bool) : (rep k l).length = k * l.length := by
  induction k with
  | zero => simp [rep]
  | succ k ih => simp only [rep, List.length_append, ih, Nat.succ_mul]; omega

open Rule30LocalConservation.Cycle in
theorem run_rep (xs bs : List Bool) (hc : run xs bs = xs) (k : Nat) : run xs (rep k bs) = xs := by
  induction k with
  | zero => rfl
  | succ k ih => rw [rep, run_append, hc, ih]

open Rule30LocalConservation.Cycle in
theorem weight_rep (cost : List Bool → Int) (xs bs : List Bool) (hc : run xs bs = xs) (k : Nat) :
    weight cost xs (rep k bs) = (k : Int) * weight cost xs bs := by
  induction k with
  | zero => simp [rep, weight]
  | succ k ih =>
    rw [rep, weight_append, hc, ih]
    push_cast; rw [Int.add_mul, Int.one_mul, Int.add_comm]

/-- The periodic standard-order sequence of a word and its windows. -/
def pwin (b : List Bool) (L j : Nat) : List Bool :=
  (List.range L).map (fun t => b.getD ((j + t) % b.length) false)

theorem pwin_periodic (b : List Bool) (L j : Nat) : pwin b L (j + b.length) = pwin b L j := by
  unfold pwin
  apply List.map_congr_left
  intro t _
  rw [show j + b.length + t = (j + t) + b.length by omega, Nat.add_mod_right]

theorem getD_take_drop (X : List Bool) (j L t : Nat) (ht : t < L) (hX : j + t < X.length) :
    ((X.drop j).take L).getD t false = X.getD (j + t) false := by
  rw [getD_of_lt _ _ (by simp; omega), List.getElem_take, List.getElem_drop, getD_of_lt _ _ hX]

open Rule30LocalConservation.Cycle in
/-- A closed walk of length at least `m + 8` has the four-step rise of a cyclic word as weight. -/
theorem closed_weight_eq_rho (m : Nat) (h : List Bool → Int) (xs BS : List Bool) (hx : xs.length = m + 7)
    (hn : m + 8 ≤ BS.length) (hc : run xs BS = xs) :
    weight (change m h) xs BS = rho m h (((xs ++ BS).take BS.length).reverse) := by
  have hdrop : (xs ++ BS).drop BS.length = xs := by have := hc; rw [run_formula] at this; exact this
  have hX : (xs ++ BS).length = BS.length + m + 7 := by simp [hx]; omega
  have hxX : ∀ k, k < m + 7 → (xs ++ BS).getD k false = xs.getD k false := by
    intro k hk
    rw [getD_of_lt _ _ (by omega), getD_of_lt _ _ (by omega), List.getElem_append_left]
  rw [weight_eq_sumR, hx]
  generalize xs ++ BS = X at hdrop hX hxX ⊢
  generalize BS.length = n at hdrop hX hn ⊢
  have hXk : ∀ k, n ≤ k → k < n + m + 7 → X.getD k false = X.getD (k - n) false := by
    intro k h1 h2
    have e1 : X.getD k false = (X.drop n).getD (k - n) false := by
      rw [getD_of_lt _ _ (by omega), getD_of_lt _ _ (by simp; omega), List.getElem_drop]
      congr 1; omega
    rw [e1, hdrop, hxX _ (by omega)]
  generalize hbdef : X.take n = b
  have hb : b.length = n := by rw [← hbdef]; simp; omega
  have hbX : ∀ k, k < n → b.getD k false = X.getD k false := by
    intro k hk
    rw [← hbdef, getD_of_lt _ _ (by simp; omega), getD_of_lt _ _ (by omega), List.getElem_take]
  have hwin : ∀ j, j < n → ((X.drop j).take (m + 8)) = pwin b (m + 8) j := by
    intro j hj
    apply ext_getD (by simp [pwin]; omega)
    intro t ht
    have ht' : t < m + 8 := by simp at ht; omega
    rw [getD_take_drop X j (m + 8) t ht' (by omega)]
    unfold pwin
    rw [getD_map_range _ _ _ ht', hb, mod_lt2 (x := j + t) (n := n) (by omega)]
    split
    · rw [hbX _ (by omega)]
    · rw [hbX _ (by omega), hXk _ (by omega) (by omega)]
  have hrev : ∀ a, a < n → dwin (zf b.reverse) a (m + 8) = pwin b (m + 8) (n - 1 - a + (n - m - 7)) := by
    intro a ha
    apply ext_getD (by simp [pwin, dwin_length])
    intro t ht
    rw [dwin_length] at ht
    rw [dwin_getD _ _ _ _ ht]
    unfold pwin
    rw [getD_map_range _ _ _ ht]
    unfold zf
    rw [List.length_reverse, hb]
    have hk : (a + (m + 8) - 1 - t) < 2 * n := by omega
    have hm : (a + (m + 8) - 1 - t) % n < n := Nat.mod_lt _ (by omega)
    rw [getD_of_lt _ _ (by rw [List.length_reverse, hb]; exact hm), List.getElem_reverse,
      ← getD_of_lt _ _ (by omega), hb]
    congr 1
    rw [mod_lt2 hk, mod_lt2 (by omega)]
    split <;> split <;> omega
  have lhs : sumR n (fun i => change m h ((X.drop i).take (m + 7 + 1))) =
      sumR n (fun i => change m h (pwin b (m + 8) i)) :=
    sumR_congr (fun i hi => by rw [show m + 7 + 1 = m + 8 from rfl, hwin i hi])
  rw [lhs]
  unfold rho
  rw [List.length_reverse, hb]
  rw [sumR_congr (n := n) (f := fun a => change m h (dwin (zf b.reverse) a (m + 8)))
    (g := fun a => change m h (pwin b (m + 8) (n - 1 - a + (n - m - 7)))) (fun a ha => by rw [hrev a ha])]
  have hper : ∀ j, change m h (pwin b (m + 8) (j + n)) = change m h (pwin b (m + 8) j) := by
    intro j; rw [← hb, pwin_periodic]
  rw [sumR_rev n (fun j => change m h (pwin b (m + 8) (j + (n - m - 7))))]
  rw [sumR_congr (n := n) (f := fun j => change m h (pwin b (m + 8) (j + (n - m - 7))))
    (g := fun j => (fun i => change m h (pwin b (m + 8) i)) ((n - m - 7) + j))
    (fun j _ => by simp only; rw [Nat.add_comm j (n - m - 7)]),
    sumR_periodic (g := fun i => change m h (pwin b (m + 8) i)) hper (n - m - 7)]

/-- **From cyclic words to closed walks.** If every cyclic word of length at least `m + 8` has zero
four-step rise, the density is conserved on every closed walk in the kit's sense. -/
theorem cyclic_conserved_of_rho (m : Nat) (h : List Bool → Int)
    (hρ : ∀ d : List Bool, m + 8 ≤ d.length → rho m h d = 0) :
    Rule30LocalConservation.CyclicConserved m h := by
  intro xs hx bs hc
  cases bs with
  | nil => rfl
  | cons b bs' =>
    have hrun := run_rep xs (b :: bs') hc (m + 8)
    have hw := weight_rep (Rule30LocalConservation.Cycle.change m h) xs (b :: bs') hc (m + 8)
    have hlen : m + 8 ≤ (rep (m + 8) (b :: bs')).length := by
      rw [rep_length]; simp only [List.length_cons]
      exact Nat.le_mul_of_pos_right _ (by omega)
    have he := closed_weight_eq_rho m h xs _ hx hlen hrun
    rw [hρ _ (by simp only [List.length_reverse, List.length_take, List.length_append]; omega)] at he
    rw [he] at hw
    have := (Int.mul_eq_zero.1 hw.symm)
    rcases this with h0 | h0
    · omega
    · exact h0

/-! ### Additive ranks on rows -/

/-- The sum of `h` over the `m`-cell windows of a row of width `W`, each read from its deep end. -/
def dens (m : Nat) (h : List Bool → Int) (s : Nat → Bool) (W : Nat) : Int :=
  sumR (W + 1 - m) (fun k => h (dwin s (k + 1) m))

/-- A rank made of an arbitrary function of (width, wall window, edge window) and an additive
density of `m`-cell windows. -/
def rank (w e m : Nat) (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (s : Nat → Bool) (W : Nat) : Int :=
  β W (wallW w s) (edgeW e s W) + dens m h s W

theorem sumR_sub (n : Nat) (f g : Nat → Int) : sumR n f - sumR n g = sumR n (fun i => f i - g i) := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [sumR]; rw [← ih]; omega

theorem density_bound (m : Nat) (h : List Bool → Int) :
    ∃ H : Int, 0 ≤ H ∧ ∀ v : List Bool, v.length = m → -H ≤ h v ∧ h v ≤ H := by
  refine ⟨wsum m (fun v => ((h v).natAbs : Int)), ?_, ?_⟩
  · have := term_le_wsum (n := m) (φ := fun v => ((h v).natAbs : Int)) (fun v _ => by omega)
      (List.replicate m false) (by simp)
    omega
  · intro v hv
    have := term_le_wsum (n := m) (φ := fun v => ((h v).natAbs : Int)) (fun v _ => by omega) v hv
    omega

theorem dens_upper {m : Nat} {h : List Bool → Int} {H : Int} (hm : 1 ≤ m) (hH : 0 ≤ H)
    (hb : ∀ v : List Bool, v.length = m → -H ≤ h v ∧ h v ≤ H) (s : Nat → Bool) (W : Nat) :
    dens m h s W ≤ H * (W : Int) := by
  have h1 : dens m h s W ≤ ((W + 1 - m : Nat) : Int) * H :=
    sumR_upper (fun k _ => (hb _ (dwin_length _ _ _)).2)
  have h2 : ((W + 1 - m : Nat) : Int) * H ≤ (W : Int) * H :=
    Int.mul_le_mul_of_nonneg_right (by omega) hH
  rw [Int.mul_comm H]
  omega

/-! ### The carrying construction -/

/-- The row with the stripe on depths `1..D`, the periodic word `d` on `D+1..D+Q` and the edge label
`E` (read from the edge) on the top `|E|` depths. -/
def mkRow (D Q : Nat) (d E : List Bool) (k : Nat) : Bool :=
  if k = 0 then false
  else if k ≤ D then stripe k
  else if k ≤ D + Q then zf d k
  else if k ≤ D + Q + E.length then E.getD (D + Q + E.length - k) false
  else false

section Row
variable (D Q : Nat) (d E : List Bool)

theorem mkRow_stripe (k : Nat) (h1 : 1 ≤ k) (h2 : k ≤ D) : mkRow D Q d E k = stripe k := by
  unfold mkRow; simp [show k ≠ 0 by omega, h2]

theorem mkRow_mid (k : Nat) (h1 : D < k) (h2 : k ≤ D + Q) : mkRow D Q d E k = zf d k := by
  unfold mkRow; simp [show k ≠ 0 by omega, show ¬ k ≤ D by omega, h2]

theorem mkRow_top (hE : E.getD 0 false = true) (he : 1 ≤ E.length) :
    mkRow D Q d E (D + Q + E.length) = true := by
  unfold mkRow
  simp only [show D + Q + E.length ≠ 0 by omega, show ¬ D + Q + E.length ≤ D by omega,
    show ¬ D + Q + E.length ≤ D + Q by omega, ite_false, Nat.le_refl, ite_true, Nat.sub_self]
  exact hE

theorem mkRow_fin (k : Nat) (hk : D + Q + E.length < k) : mkRow D Q d E k = false := by
  unfold mkRow
  simp [show k ≠ 0 by omega, show ¬ k ≤ D by omega, show ¬ k ≤ D + Q by omega,
    show ¬ k ≤ D + Q + E.length by omega]

theorem mkRow_edge :
    edgeW E.length (mkRow D Q d E) (D + Q + E.length) = E := by
  apply ext_getD (by simp [edgeW])
  intro i hi
  simp only [edgeW, List.length_map, List.length_range] at hi
  unfold edgeW
  rw [getD_map_range _ _ _ hi]
  unfold mkRow
  simp only [show D + Q + E.length - i ≠ 0 by omega, show ¬ D + Q + E.length - i ≤ D by omega,
    show ¬ D + Q + E.length - i ≤ D + Q by omega, ite_false, show D + Q + E.length - i ≤ D + Q + E.length by omega,
    ite_true]
  congr 1; omega

theorem mkRow_wall (w : Nat) (hw : w ≤ D) : wallW w (mkRow D Q d E) = wallW w stripe :=
  map_range_congr fun i hi => mkRow_stripe D Q d E (i + 1) (by omega) (by omega)

/-- Near the wall the row evolves as the stripe. -/
theorem mkRow_evolve (t j : Nat) (h2 : j + t ≤ D) : zrow (mkRow D Q d E) t j = stripe j := by
  rw [zrow_light_cone (L' := stripe) t j (fun i hi1 hi2 => mkRow_stripe D Q d E i hi1 (by omega)),
    zrow_stripe]

end Row

theorem dstep_dstep (s : Nat → Bool) : dstep (dstep s) = zrow s 4 := by
  funext k
  unfold dstep
  exact (zrow_shift s 2 2 k).symm

theorem late_mkRow {u : Nat → Nat} {D Q : Nat} {d E : List Bool} (hE : E.getD 0 false = true)
    (he : 1 ≤ E.length) (hD : 5 ≤ D) (hu1 : D + Q + E.length - u (D + Q + E.length) + 1 ≤ D) :
    Late u (mkRow D Q d E) (D + Q + E.length) := by
  refine ⟨by omega, mkRow_top D Q d E hE he, fun k hk => mkRow_fin D Q d E k hk, ⟨?_, ?_⟩, ?_⟩
  · rw [zrow_zero_of_pos _ (by omega), mkRow_stripe D Q d E 1 (by omega) (by omega)]; rfl
  · rw [mkRow_evolve D Q d E 2 1 (by omega)]; rfl
  · intro i hi
    rw [mkRow_evolve D Q d E (2 * i) 1 (by omega)]; rfl

theorem late_dstep_mkRow {u : Nat → Nat} {D Q : Nat} {d E : List Bool} (hE : E.getD 0 false = true)
    (he : 1 ≤ E.length) (hD : 5 ≤ D)
    (hu2 : D + Q + E.length + 2 - u (D + Q + E.length + 2) + 3 ≤ D) :
    Late u (dstep (mkRow D Q d E)) (D + Q + E.length + 2) := by
  have hw := zrow_edge (L := mkRow D Q d E) (m := D + Q + E.length) (by omega)
    (mkRow_top D Q d E hE he) (fun k hk => mkRow_fin D Q d E k hk) 2
  refine ⟨by omega, hw.1, hw.2, ⟨?_, ?_⟩, ?_⟩
  · rw [zrow_zero_of_pos _ (by omega)]
    show zrow (mkRow D Q d E) 2 1 = true
    rw [mkRow_evolve D Q d E 2 1 (by omega)]; rfl
  · show zrow (zrow (mkRow D Q d E) 2) 2 1 = true
    rw [← zrow_shift, mkRow_evolve D Q d E (2 + 2) 1 (by omega)]; rfl
  · intro i hi
    show zrow (zrow (mkRow D Q d E) 2) (2 * i) 1 = true
    rw [← zrow_shift, mkRow_evolve D Q d E (2 + 2 * i) 1 (by omega)]; rfl

theorem dwin_zrow_zero (s : Nat → Bool) (a n : Nat) (ha : 1 ≤ a) : dwin (zrow s 0) a n = dwin s a n :=
  dwin_congr fun j h1 _ => zrow_zero_of_pos s (by omega)

/-- **The rise in the free middle.** Over four steps the density gains `μ` times the cyclic rise of
`d`, up to a bounded error from the wall, the two interfaces and the edge. -/
theorem rise_mkRow {m : Nat} {h : List Bool → Int} {H : Int} (hm : 1 ≤ m)
    (hb : ∀ v : List Bool, v.length = m → -H ≤ h v ∧ h v ≤ H)
    (D μ : Nat) (d E : List Bool) (hN : m + 8 ≤ d.length) (he : 1 ≤ E.length) (hD : m + 4 ≤ D) :
    (μ : Int) * rho m h d -
        (((m + 8 : Nat) : Int) * (2 * H) + ((2 * d.length + E.length - m - 3 : Nat) : Int) * (2 * H) +
          4 * H) ≤
      dens m h (zrow (mkRow D ((μ + 2) * d.length) d E) 4) (D + (μ + 2) * d.length + E.length + 4) -
        dens m h (mkRow D ((μ + 2) * d.length) d E) (D + (μ + 2) * d.length + E.length) := by
  let Q := (μ + 2) * d.length
  let Y := mkRow D Q d E
  let W := D + Q + E.length
  have hQ : Q = μ * d.length + 2 * d.length := by simp only [Q]; rw [Nat.add_mul]
  let δ : Nat → Int := fun k => h (dwin (zrow Y 4) (k + 1) m) - h (dwin Y (k + 1) m)
  have hrise : dens m h (zrow Y 4) (W + 4) - dens m h Y W =
      sumR (W + 1 - m) δ + sumR 4 (fun k => h (dwin (zrow Y 4) (W + 1 - m + k + 1) m)) := by
    have e4 : dens m h (zrow Y 4) (W + 4) =
        sumR (W + 1 - m) (fun k => h (dwin (zrow Y 4) (k + 1) m)) +
          sumR 4 (fun k => h (dwin (zrow Y 4) (W + 1 - m + k + 1) m)) := by
      unfold dens
      rw [show W + 4 + 1 - m = (W + 1 - m) + 4 by omega, sumR_add]
    have e0 : dens m h Y W = sumR (W + 1 - m) (fun k => h (dwin Y (k + 1) m)) := rfl
    have es := sumR_sub (W + 1 - m) (fun k => h (dwin (zrow Y 4) (k + 1) m)) (fun k => h (dwin Y (k + 1) m))
    rw [e4, e0]
    show _ = sumR (W + 1 - m) (fun k => h (dwin (zrow Y 4) (k + 1) m) - h (dwin Y (k + 1) m)) + _
    omega
  have hzones : W + 1 - m =
      (D - m - 4) + ((m + 8) + (μ * d.length + (2 * d.length + E.length - m - 3))) := by
    simp only [W]; rw [hQ]; omega
  have hA : sumR (D - m - 4) δ = 0 := by
    apply sumR_zero
    intro k hk
    show h (dwin (zrow Y 4) (k + 1) m) - h (dwin Y (k + 1) m) = 0
    rw [dwin_congr (g := stripe) (fun j h1 h2 => mkRow_evolve D Q d E 4 j (by omega)),
      dwin_congr (f := Y) (g := stripe) (fun j h1 h2 => mkRow_stripe D Q d E j (by omega) (by omega))]
    omega
  have hδ : ∀ k, -(2 * H) ≤ δ k := by
    intro k
    have h1 := hb _ (dwin_length (zrow Y 4) (k + 1) m)
    have h2 := hb _ (dwin_length Y (k + 1) m)
    show -(2 * H) ≤ h (dwin (zrow Y 4) (k + 1) m) - h (dwin Y (k + 1) m)
    omega
  have hB : -(((m + 8 : Nat) : Int) * (2 * H)) ≤ sumR (m + 8) (fun i => δ ((D - m - 4) + i)) :=
    sumR_lower (fun i _ => hδ _)
  have hDz : -(((2 * d.length + E.length - m - 3 : Nat) : Int) * (2 * H)) ≤
      sumR (2 * d.length + E.length - m - 3)
        (fun i => δ ((D - m - 4) + ((m + 8) + (μ * d.length + i)))) :=
    sumR_lower (fun i _ => hδ _)
  let g : Nat → Int := fun a => Rule30LocalConservation.Cycle.change m h (dwin (zf d) a (m + 8))
  have hg : ∀ a, g (a + d.length) = g a := by
    intro a
    show Rule30LocalConservation.Cycle.change m h (dwin (zf d) (a + d.length) (m + 8)) =
      Rule30LocalConservation.Cycle.change m h (dwin (zf d) a (m + 8))
    rw [dwin_shift (zf d) (a + d.length), dwin_shift (zf d) a]
    congr 1
    apply dwin_congr
    intro j _ _
    rw [show j + (a + d.length) = (j + a) + d.length by omega, zf_periodic]
  have hC : sumR (μ * d.length) (fun i => δ ((D - m - 4) + ((m + 8) + i))) = (μ : Int) * rho m h d := by
    have e1 : sumR (μ * d.length) (fun i => δ ((D - m - 4) + ((m + 8) + i))) =
        sumR (μ * d.length) (fun i => g (D + 1 + i)) := by
      apply sumR_congr
      intro i hi
      show h (dwin (zrow Y 4) ((D - m - 4) + ((m + 8) + i) + 1) m) -
          h (dwin Y ((D - m - 4) + ((m + 8) + i) + 1) m) =
        Rule30LocalConservation.Cycle.change m h (dwin (zf d) (D + 1 + i) (m + 8))
      have ha : (D - m - 4) + ((m + 8) + i) + 1 = (D + 1 + i) + 4 := by omega
      rw [ha, ← dwin_zrow_zero Y ((D + 1 + i) + 4) m (by omega), ← change_dwin Y m h (D + 1 + i),
        dwin_congr (f := zrow Y 0) (g := zf d) (fun j h1 h2 => by
          rw [zrow_zero_of_pos _ (by omega)]
          exact mkRow_mid D Q d E j (by omega) (by rw [hQ]; omega))]
    rw [e1, sumR_blocks hg (D + 1) μ]
    rfl
  have hX : -(4 * H) ≤ sumR 4 (fun k => h (dwin (zrow Y 4) (W + 1 - m + k + 1) m)) := by
    have := sumR_lower (n := 4) (f := fun k => h (dwin (zrow Y 4) (W + 1 - m + k + 1) m)) (B := H)
      (fun k _ => (hb _ (dwin_length _ _ _)).1)
    simpa using this
  have hsum : sumR (W + 1 - m) δ =
      sumR (D - m - 4) δ + (sumR (m + 8) (fun i => δ ((D - m - 4) + i)) +
        (sumR (μ * d.length) (fun i => δ ((D - m - 4) + ((m + 8) + i))) +
          sumR (2 * d.length + E.length - m - 3)
            (fun i => δ ((D - m - 4) + ((m + 8) + (μ * d.length + i)))))) := by
    rw [hzones, sumR_add, sumR_add (m + 8), sumR_add (μ * d.length)]
  show _ ≤ dens m h (zrow Y 4) (W + 4) - dens m h Y W
  rw [hrise, hsum, hA, hC]
  omega

/-! ### The free-middle theorem -/

/-- The edge labels of the carrying rows: each row's label is the edge window of the previous row
four steps later. -/
def labels (e : Nat) (Dn Qn Wn : Nat → Nat) (d : List Bool) : Nat → List Bool
  | 0 => true :: List.replicate (e - 1) false
  | n + 1 => edgeW e (zrow (mkRow (Dn n) (Qn n) d (labels e Dn Qn Wn d n)) 4) (Wn n + 4)

theorem labels_length (e : Nat) (he : 1 ≤ e) (Dn Qn Wn : Nat → Nat) (d : List Bool) (n : Nat) :
    (labels e Dn Qn Wn d n).length = e := by
  cases n with
  | zero => simp [labels]; omega
  | succ n => simp [labels, edgeW]

theorem labels_head (e : Nat) (he : 1 ≤ e) (Dn Qn Wn : Nat → Nat) (d : List Bool)
    (hW : ∀ n, Wn n = Dn n + Qn n + e) : ∀ n, (labels e Dn Qn Wn d n).getD 0 false = true := by
  intro n
  induction n with
  | zero => simp [labels]
  | succ n ih =>
    simp only [labels, edgeW]
    rw [getD_map_range _ _ _ (by omega), Nat.sub_zero]
    have hl := labels_length e he Dn Qn Wn d n
    have htop := mkRow_top (Dn n) (Qn n) d (labels e Dn Qn Wn d n) ih (by omega)
    rw [hl] at htop
    have hw := zrow_edge (L := mkRow (Dn n) (Qn n) d (labels e Dn Qn Wn d n)) (m := Dn n + Qn n + e)
      (by omega) htop (fun k hk => mkRow_fin _ _ d _ k (by rw [hl]; omega)) 4
    rw [hW n]; exact hw.1

/-- **The carrying step.** Under descent on the late population and a linear lower bound, no
cyclic word of length at least `m + 8` has a positive four-step rise. -/
theorem rho_nonpos_of_descent (w e m K : Nat) (hm : 1 ≤ m) (he : 1 ≤ e) (u : Nat → Nat) (hu : ToInfty u)
    (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (hlow : ∀ s W, Late u s W → -((K : Int) * (W : Int)) ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) ≤ rank w e m β h s W)
    (d : List Bool) (hN : m + 8 ≤ d.length) : rho m h d ≤ 0 := by
  obtain ⟨H, hH0, hb⟩ := density_bound m h
  refine Int.not_lt.1 (fun hpos => ?_)
  let c0 := e + m + w + 16
  obtain ⟨W1, hW1⟩ := hu (c0 + 2 * d.length)
  let W0 := W1 + c0 + 2 * d.length
  let Wn : Nat → Nat := fun n => W0 + 4 * n
  let v : Nat → Nat := fun n => min (min (u (Wn n)) (u (Wn n + 2))) (Wn n)
  let μn : Nat → Nat := fun n => (v n - c0) / d.length - 2
  let Qn : Nat → Nat := fun n => (μn n + 2) * d.length
  let Dn : Nat → Nat := fun n => Wn n - Qn n - e
  have hNpos : 0 < d.length := by omega
  have hv : ∀ n, c0 + 2 * d.length ≤ v n := by
    intro n
    have h1 := hW1 (Wn n) (by simp only [Wn, W0]; omega)
    have h2 := hW1 (Wn n + 2) (by simp only [Wn, W0]; omega)
    simp only [v, Wn, W0] at h1 h2 ⊢
    omega
  have hvW : ∀ n, v n ≤ Wn n := fun n => by simp only [v]; omega
  have hvu : ∀ n, v n ≤ u (Wn n) ∧ v n ≤ u (Wn n + 2) := fun n => by simp only [v]; omega
  have hdiv : ∀ n, 2 ≤ (v n - c0) / d.length := fun n =>
    (Nat.le_div_iff_mul_le hNpos).2 (by have := hv n; rw [Nat.mul_comm] at this ⊢; omega)
  have hQ : ∀ n, Qn n ≤ v n - c0 := by
    intro n
    have e1 : μn n + 2 = (v n - c0) / d.length := by have := hdiv n; simp only [μn]; omega
    simp only [Qn]; rw [e1]; exact Nat.div_mul_le_self _ _
  have hWn : ∀ n, Wn n = Dn n + Qn n + e := by
    intro n; have := hQ n; have := hvW n; have := hv n; simp only [Dn]; omega
  have hDn : ∀ n, m + w + 16 ≤ Dn n := by
    intro n; have := hQ n; have := hvW n; have := hv n; simp only [Dn, c0] at *; omega
  let E := labels e Dn Qn Wn d
  have hEl : ∀ n, (E n).length = e := labels_length e he Dn Qn Wn d
  have hEh : ∀ n, (E n).getD 0 false = true := labels_head e he Dn Qn Wn d hWn
  let Y : Nat → Nat → Bool := fun n => mkRow (Dn n) (Qn n) d (E n)
  have hWY : ∀ n, Wn n = Dn n + Qn n + (E n).length := fun n => by rw [hEl n]; exact hWn n
  have hY : ∀ n, Late u (Y n) (Wn n) := by
    intro n
    rw [hWY n]
    apply late_mkRow (hEh n) (by rw [hEl n]; exact he) (by have := hDn n; omega)
    rw [← hWY n]
    have := hQ n; have := hvu n; have := hvW n; have := hv n; simp only [Dn, c0] at *; omega
  have hY2 : ∀ n, Late u (dstep (Y n)) (Wn n + 2) := by
    intro n
    rw [hWY n]
    apply late_dstep_mkRow (hEh n) (by rw [hEl n]; exact he) (by have := hDn n; omega)
    rw [← hWY n]
    have := hQ n; have := hvu n; have := hvW n; have := hv n; simp only [Dn, c0] at *; omega
  let S := wallW w stripe
  let B : Nat → Int := fun n => β (Wn n) S (E n)
  have hrank : ∀ n, rank w e m β h (Y n) (Wn n) = B n + dens m h (Y n) (Wn n) := by
    intro n
    unfold rank
    rw [mkRow_wall _ _ _ _ w (by have := hDn n; omega)]
    have he' := mkRow_edge (Dn n) (Qn n) d (E n)
    rw [hEl n, ← hWn n] at he'
    show β (Wn n) (wallW w stripe) (edgeW e (Y n) (Wn n)) + _ = _
    rw [he']
  have hwall4 : ∀ n, wallW w (zrow (Y n) 4) = S := by
    intro n
    exact map_range_congr fun i hi =>
      mkRow_evolve (Dn n) (Qn n) d (E n) 4 (i + 1) (by have := hDn n; omega)
  have hrank4 : ∀ n, rank w e m β h (zrow (Y n) 4) (Wn n + 4) =
      B (n + 1) + dens m h (zrow (Y n) 4) (Wn n + 4) := by
    intro n
    unfold rank
    rw [hwall4 n]
    rfl
  have hstep : ∀ n, B (n + 1) + dens m h (zrow (Y n) 4) (Wn n + 4) ≤ B n + dens m h (Y n) (Wn n) := by
    intro n
    have h1 := hdesc _ _ (hY n)
    have h2 := hdesc _ _ (hY2 n)
    rw [dstep_dstep, show Wn n + 2 + 2 = Wn n + 4 by omega] at h2
    rw [← hrank n, ← hrank4 n]
    omega
  let Cst : Int := ((m + 8 : Nat) : Int) * (2 * H) + ((2 * d.length + e - m - 3 : Nat) : Int) * (2 * H) + 4 * H
  have hrise : ∀ n, (μn n : Int) * rho m h d - Cst ≤
      dens m h (zrow (Y n) 4) (Wn n + 4) - dens m h (Y n) (Wn n) := by
    intro n
    have := rise_mkRow hm hb (Dn n) (μn n) d (E n) hN (by rw [hEl n]; exact he) (by have := hDn n; omega)
    rw [hEl n] at this
    have e1 : Dn n + (μn n + 2) * d.length + e = Wn n := (hWn n).symm
    rw [e1] at this
    exact this
  let A : Int := (K : Int) + H
  have hlowB : ∀ n, -(A * (Wn n : Int)) ≤ B n := by
    intro n
    have h1 := hlow _ _ (hY n)
    rw [hrank n] at h1
    have h2 := dens_upper hm hH0 hb (Y n) (Wn n)
    have e1 : A * (Wn n : Int) = (K : Int) * (Wn n : Int) + H * (Wn n : Int) := Int.add_mul _ _ _
    rw [e1]; omega
  have hgrow : ∀ T : Nat, ∃ n1, ∀ n, n1 ≤ n → T ≤ μn n := by
    intro T
    obtain ⟨W2, hW2⟩ := hu (c0 + (T + 2) * d.length)
    refine ⟨W2 + c0 + (T + 2) * d.length, fun n hn => ?_⟩
    have h1 := hW2 (Wn n) (by simp only [Wn]; omega)
    have h2 := hW2 (Wn n + 2) (by simp only [Wn]; omega)
    have h3 : c0 + (T + 2) * d.length ≤ v n := by simp only [v, Wn] at h1 h2 ⊢; omega
    have h4 : T + 2 ≤ (v n - c0) / d.length := (Nat.le_div_iff_mul_le hNpos).2 (by omega)
    simp only [μn]; omega
  let P : Nat → Int := fun n => B n + A * (Wn n : Int)
  have hP0 : ∀ n, 0 ≤ P n := fun n => by have := hlowB n; simp only [P]; omega
  obtain ⟨n1, hn1⟩ := hgrow (Cst + 4 * A + 1).toNat
  have hPstep : ∀ n, n1 ≤ n → P (n + 1) + 1 ≤ P n := by
    intro n hn
    have h1 := hstep n
    have h2 := hrise n
    have h3 : ((Cst + 4 * A + 1).toNat : Int) ≤ (μn n : Int) := by exact_mod_cast hn1 n hn
    have h4 : (μn n : Int) * 1 ≤ (μn n : Int) * rho m h d :=
      Int.mul_le_mul_of_nonneg_left (by omega) (by omega)
    have h5 : Cst + 4 * A + 1 ≤ ((Cst + 4 * A + 1).toNat : Int) := Int.self_le_toNat _
    have e0 : ∀ x : Nat, A * ((x + 4 : Nat) : Int) = A * (x : Int) + 4 * A := by
      intro x; rw [show ((x + 4 : Nat) : Int) = (x : Int) + 4 by omega, Int.mul_add, Int.mul_comm A 4]
    have e1 : A * (Wn (n + 1) : Int) = A * (Wn n : Int) + 4 * A := by
      rw [show Wn (n + 1) = Wn n + 4 by simp only [Wn]; omega, e0]
    simp only [P]
    rw [e1]
    omega
  have hPj : ∀ j : Nat, P (n1 + j) + j ≤ P n1 := by
    intro j
    induction j with
    | zero => simp
    | succ j ih =>
      have := hPstep (n1 + j) (by omega)
      rw [show n1 + (j + 1) = n1 + j + 1 by omega]
      push_cast
      omega
  have := hPj ((P n1).toNat + 1)
  have := hP0 (n1 + ((P n1).toNat + 1))
  have := Int.self_le_toNat (P n1)
  push_cast at *
  omega

/-- **The free-middle theorem.** Let `u` tend to infinity, and let a rank be an arbitrary function
of (width, wall window, edge window) plus an integer additive density of `m`-cell windows. If the
rank is bounded below by `-K W` on the late population and never increases along its double steps,
then the density is conserved on every closed walk: survival short of the whole row does not
restrict additive potentials. -/
theorem free_middle (w e m K : Nat) (hm : 1 ≤ m) (he : 1 ≤ e) (u : Nat → Nat) (hu : ToInfty u)
    (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (hlow : ∀ s W, Late u s W → -((K : Int) * (W : Int)) ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) ≤ rank w e m β h s W) :
    Rule30LocalConservation.CyclicConserved m h :=
  cyclic_conserved_of_rho m h fun d hd =>
    rho_eq_zero m h d.length hd
      (fun d' hd' => rho_nonpos_of_descent w e m K hm he u hu β h hlow hdesc d' (by omega)) d rfl

/-- With the kit's classification: the density is a constant plus a shift coboundary. -/
theorem free_middle_coboundary (w e m K : Nat) (hm : 1 ≤ m) (he : 1 ≤ e) (u : Nat → Nat)
    (hu : ToInfty u) (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (hlow : ∀ s W, Late u s W → -((K : Int) * (W : Int)) ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) ≤ rank w e m β h s W) :
    Rule30LocalConservation.ShiftCoboundary m h :=
  (Rule30LocalConservation.cyclic_conserved_iff_shift_coboundary m hm h).1
    (free_middle w e m K hm he u hu β h hlow hdesc)

/-! ### A coboundary sums to its boundary windows -/

theorem sumR_telescope (n : Nat) (c : Int) (f : Nat → Int) :
    sumR n (fun k => c + f k - f (k + 1)) = (n : Int) * c + f 0 - f n := by
  induction n with
  | zero => simp [sumR]
  | succ n ih => simp only [sumR]; rw [ih]; push_cast; rw [Int.add_mul, Int.one_mul]; omega

theorem dwin_tail (s : Nat → Bool) (a n : Nat) : (dwin s a (n + 1)).tail = dwin s a n := rfl

theorem dwin_dropLast (s : Nat → Bool) (a n : Nat) : (dwin s a (n + 1)).dropLast = dwin s (a + 1) n := by
  rw [dwin_split s a n 1]
  exact List.dropLast_concat

theorem dwin_wall (s : Nat → Bool) (w m : Nat) (hw : m - 1 ≤ w) :
    dwin s 1 (m - 1) = ((wallW w s).take (m - 1)).reverse := by
  apply ext_getD (by simp [dwin_length, wallW]; omega)
  intro t ht
  rw [dwin_length] at ht
  rw [dwin_getD _ _ _ _ ht, getD_of_lt _ _ (by simp [wallW]; omega), List.getElem_reverse,
    List.getElem_take]
  unfold wallW
  rw [List.getElem_map, List.getElem_range]
  congr 1
  simp at *
  omega

theorem dwin_edge (s : Nat → Bool) (e m W : Nat) (he : m - 1 ≤ e) (hW : m ≤ W + 1) (hm : 1 ≤ m) :
    dwin s (W + 2 - m) (m - 1) = (edgeW e s W).take (m - 1) := by
  apply ext_getD (by simp [dwin_length, edgeW]; omega)
  intro t ht
  rw [dwin_length] at ht
  rw [dwin_getD _ _ _ _ ht, getD_of_lt _ _ (by simp [edgeW]; omega), List.getElem_take]
  unfold edgeW
  rw [List.getElem_map, List.getElem_range]
  congr 1
  omega

/-- **The rank is local.** When the density is a constant plus a shift coboundary and both
windows are at least `m - 1` cells long, the rank is a function of (width, wall window, edge
window) alone. -/
theorem rank_local (w e m : Nat) (hm : 1 ≤ m) (hw : m - 1 ≤ w) (he : m - 1 ≤ e)
    (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (hc : Rule30LocalConservation.ShiftCoboundary m h) :
    ∃ β' : Nat → List Bool → List Bool → Int, ∀ s W,
      rank w e m β h s W = β' W (wallW w s) (edgeW e s W) := by
  obtain ⟨c, p, hp⟩ := hc
  refine ⟨fun W a b => if m ≤ W + 1 then
      β W a b + (((W + 1 - m : Nat) : Int) * c + p ((a.take (m - 1)).reverse) - p (b.take (m - 1)))
    else β W a b, fun s W => ?_⟩
  unfold rank dens
  dsimp only
  split
  · rename_i hW
    congr 1
    obtain ⟨n, rfl⟩ : ∃ n, m = n + 1 := ⟨m - 1, by omega⟩
    rw [sumR_congr (g := fun k => c + p (dwin s (k + 1) n) - p (dwin s (k + 1 + 1) n)) (fun k _ => by
      rw [hp _ (dwin_length _ _ _), dwin_tail, dwin_dropLast])]
    rw [sumR_telescope (W + 1 - (n + 1)) c (fun k => p (dwin s (k + 1) n))]
    simp only [Nat.zero_add]
    rw [show W + 1 - (n + 1) + 1 = W + 2 - (n + 1) by omega]
    have h1 := dwin_wall s w (n + 1) hw
    have h2 := dwin_edge s e (n + 1) W he hW hm
    simp only [Nat.add_sub_cancel] at h1 h2 ⊢
    rw [h1, h2]
  · rename_i hW
    rw [show W + 1 - m = 0 by omega]
    simp [sumR]

/-- **No additive ranking of the late population.** Let `u` tend to infinity. No rank of the form
(any function of width, wall window and edge window) plus (an integer additive density of `m`-cell
windows) is nonnegative on the late population and strictly decreases along each of its double
steps, once the windows are at least `m - 1` cells long. -/
theorem no_additive_ranking_late (w e m : Nat) (hm : 1 ≤ m) (he1 : 1 ≤ e) (hw : m - 1 ≤ w)
    (he : m - 1 ≤ e) (u : Nat → Nat) (hu : ToInfty u)
    (β : Nat → List Bool → List Bool → Int) (h : List Bool → Int)
    (hpos : ∀ s W, Late u s W → 0 ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) < rank w e m β h s W) : False := by
  have hcob := free_middle_coboundary w e m 0 hm he1 u hu β h
    (fun s W hs => by have := hpos s W hs; simp; omega)
    (fun s W hs => Int.le_of_lt (hdesc s W hs))
  obtain ⟨β', hβ'⟩ := rank_local w e m hm hw he β h hcob
  exact no_local_ranking_late w e u hu β'
    (fun s W hs => by rw [← hβ']; exact hpos s W hs)
    (fun s W hs => by rw [← hβ', ← hβ']; exact hdesc s W hs)

/-! ### The lower bound cannot be dropped -/

/-- One-cell popcount. -/
def pop1 (v : List Bool) : Int := if v.headD false then 1 else 0

theorem pop1_dwin (s : Nat → Bool) (k : Nat) : pop1 (dwin s k 1) = if s k then 1 else 0 := by
  simp [pop1, dwin]

/-- **The lower bound is needed.** The rank `popcount - W ^ 2` strictly decreases along every
surviving double step of every finite row, while the popcount is not a constant plus a shift
coboundary. So `free_middle` fails without its lower bound. -/
theorem lower_bound_needed :
    (∀ s W, 1 ≤ W → s W = true → (∀ k, W < k → s k = false) →
      rank 0 1 1 (fun W _ _ => -((W : Int) * (W : Int))) pop1 (dstep s) (W + 2) <
        rank 0 1 1 (fun W _ _ => -((W : Int) * (W : Int))) pop1 s W) ∧
    ¬ Rule30LocalConservation.ShiftCoboundary 1 pop1 := by
  refine ⟨fun s W hW htop hfin => ?_, fun ⟨c, p, hp⟩ => ?_⟩
  · unfold rank dens
    simp only
    rw [show W + 2 + 1 - 1 = W + 2 by omega, show W + 1 - 1 = W by omega]
    have hub : sumR (W + 2) (fun k => pop1 (dwin (dstep s) (k + 1) 1)) ≤ ((W + 2 : Nat) : Int) * 1 :=
      sumR_upper (fun k _ => by rw [pop1_dwin]; split <;> omega)
    have hlb : 1 ≤ sumR W (fun k => pop1 (dwin s (k + 1) 1)) := by
      obtain ⟨W', rfl⟩ : ∃ W', W = W' + 1 := ⟨W - 1, by omega⟩
      simp only [sumR]
      have h0 : 0 ≤ sumR W' (fun k => pop1 (dwin s (k + 1) 1)) := by
        have := sumR_lower (n := W') (f := fun k => pop1 (dwin s (k + 1) 1)) (B := 0)
          (fun k _ => by rw [pop1_dwin]; split <;> omega)
        simpa using this
      rw [pop1_dwin, htop]
      simp only [ite_true]
      omega
    have e1 : ((W + 2 : Nat) : Int) * ((W + 2 : Nat) : Int) = (W : Int) * (W : Int) + 4 * (W : Int) + 4 := by
      rw [show ((W + 2 : Nat) : Int) = (W : Int) + 2 by omega, Int.add_mul, Int.mul_add, Int.mul_add]
      omega
    rw [e1]
    have e2 : ((W + 2 : Nat) : Int) * 1 = (W : Int) + 2 := by omega
    omega
  · have h1 := hp [true] rfl
    have h0 := hp [false] rfl
    simp [pop1] at h1 h0
    omega

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30LocalConservation"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"no_local_ranking_late", "wsum_rho", "cyclic_conserved_of_rho", "free_middle", "free_middle_coboundary", "rank_local", "no_additive_ranking_late", "lower_bound_needed"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.lower_bound_needed"]["KernelCheck"]
```
