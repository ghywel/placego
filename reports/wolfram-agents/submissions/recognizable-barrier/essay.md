---
Template: ComputationalEssay
Name: No Ranking Through a Recognizable Statistic: The Kit's Ranking Barriers for Period Two Extended to Finite-Monoid Images, and Two Rows That Defeat Every Width-Bounded Rank
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. No rank of the width and a finite-monoid image of the row falls at every surviving double step, in the zero-boundary and the coupled frames; two rows of width 11 defeat every width-bounded rank. Statements about proof shapes; nothing here decides Q01 or period 2.
Abstract: In core Lean 4.35.0 we strengthen two of the kit's barriers for proofs that the center column of rule 30 is not eventually 2-periodic. A ranking proof would give every finite row of the zero-boundary left half a rank that falls at every surviving double step. The kit shows that no natural-number rank of the width and two bounded windows can do this, and that no finite automaton reading the row from its edge can supply the rank as its longest accepted prefix. We let the rank depend also on the image of the whole row under any morphism from Boolean words into any finite monoid, with values in any well-founded order. No such rank exists. This holds with the row read from its edge or from the wall, and in the kit's coupled two-sided frame at every flip of the center column. The kit's two-window barriers are the cases of the one-element monoid. The witnesses are the kit's: truncated stripes, whose rows after j double steps are a fixed word followed by a run of 01 pairs, and truncations of the 7-periodic ether. Separately, the rows 1493 and 1507, of width 11, survive fourteen double steps. So no integer rank between -1 and the width falls at every surviving step, and the kit's automaton barrier holds without its bound on the number of states. These are statements about proof shapes. Nothing here decides Q01 or period 2.
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, barrier, ranking function, finite monoid, recognizable, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## 1. The statement

The kit reduces an eventual period `2` of rule 30's center column to `Q01`, a question about the zero-boundary left half. A natural way to prove `Q01` would be a ranking function: a rank on finite rows that falls at every *surviving* double step, one that keeps depth `1` black at the two even ticks. The kit's `Rule30ZeroBoundaryBarriers` rules out two such shapes:
- `no_local_ranking` (`RankCert`): no natural-number rank of the width, a window at the wall and a window at the edge;
- `no_edge_dfa_ranking` (`CertE`): no rank given by the longest prefix of the row, read from its edge, that a finite automaton accepts.

The same module has a coupled two-sided version, `no_joint_local_ranking` (`JointCert`), over all finite configurations, with a strict fall at every flip of the center column.

A *recognizable statistic* of a row is its image under a morphism from Boolean words into a fixed finite monoid (`FinMonoid`, `FinMonoid.eval`). It is the classical notion behind regular languages: what a finite automaton remembers about a whole word. This module adds such a statistic to the arguments of the rank, and lets the rank take values in any well-founded order.

- `no_recognizable_ranking`, `no_recognizable_ranking_nat`: no rank of (width, image of the row read from its edge) falls at every surviving double step of every finitely supported row. `no_wall_recognizable_ranking`: the same with the row read from the wall. Reversing a word is reading it in the opposite monoid (`FinMonoid.op`, `FinMonoid.eval_reverse`).
- `no_windowed_recognizable_ranking`: the same with the kit's wall and edge windows added. For the one-element monoid it is the kit's `no_local_ranking` (`no_local_ranking_of_recognizable`).
- `no_joint_recognizable_ranking`, `no_joint_recognizable_ranking_nat`, `no_joint_windowed_recognizable_ranking`: the coupled frame. The statistic is the image of the whole configuration between its leftmost and rightmost black cells, read from left to right (`spanWord`). For the one-element monoid it is the kit's `no_joint_local_ranking` (`no_joint_local_ranking_of_recognizable`).
- `no_width_bounded_ranking`: no integer rank between `-1` and the width falls at every surviving double step. So `no_edge_automaton_ranking`: the kit's automaton barrier holds for every automaton with states in `Nat`, with no bound on their number.

## 2. The zero-boundary frame

The witnesses are the kit's truncated stripes `trunc n`, the stripe `…10101` cut off at an odd depth `n`, which survive for a long time.
- `edge_decomp`: for odd `n`, `j ≥ 1` and `4 j ≤ n`, the row after `j` double steps, read from its edge, is a word `Zw j` of length `4 j - 1` followed by `k = (n + 1 - 2 j) / 2` copies of `01`. The word `Zw j` does not depend on `n`.
- The images of the powers of `01` in the finite monoid are eventually periodic, with some period `π` from some index on.
- Along `j = 1 + i π`, two of the finitely many values of (image of `Zw j`, edge window) agree, at some `j₁ < j₂`, and `d = j₂ - j₁` is a multiple of `π`.
- Only then is the odd base depth `n₀` chosen, large enough for both times. Write `r m j` for the row after `j` double steps from `trunc (n₀ + 2 m)`. The rows `r m j₂` and `r (m + d) j₁` have the same width, the same windows and the same image, because their stripe exponents differ by `2 d`.
- A certificate would carry `r (m + d) j₁` down to `r m j₁` through the steps from `j₁` to `j₂`, for every `m`. That is an infinite descent in a well-founded order (`no_descent`).

## 3. The coupled frame

The witnesses are the truncations `c7cut N` of the spatially `7`-periodic orbit.
- `c7cut_span`: at a time `t = 28 c` with `2 t ≤ 14 N + 8`, the row between its ends is a left wedge of `2 t` cells, an ether word of length `14 N + 8 - 2 t`, and a right wedge of `2 t` cells.
- The wedges and the edge windows do not depend on `N` once `N` is large (`wedgeData_indep`). The center column flips at every tick in range, so a certificate falls at each of them (`jrank_step`, the kit's `jointRank_step` with the monoid image added).
- Pigeonhole both wedge images and both edge windows over the times `28 π i`, at some `i₁ < i₂`. Compare the rows `(N, t₂)` and `(N + ε, t₁)` with `7 ε = t₂ - t₁`. They have the same ends, the same center window and the same windows, and their ether lengths differ by `28 ε`, a multiple of `7 π`. So they have the same image, and the same descent follows.

## 4. Two sharp rows

`sharp_rows_check` is a kernel evaluation of the kit's integer form `G` of the double step. The rows `1493` and `1507`, of width `11`, keep depth `1` black at the even ticks `0, 2, …, 28` and turn it white at tick `30`. So they survive fourteen double steps (`sharp_rows_survive`, `sharp_rows_fourteen`). A rank between `-1` and the width that fell at each of them would go from at most `11` to below `-1` (`no_width_bounded_ranking`). The longest accepted prefix of a word lies between `-1` and its length, so `no_edge_automaton_ranking` follows for every automaton.

## 5. Worked numbers

The cell below computes, independently of the Lean module:
- the first even iterate of `G` from `1493` and from `1507`;
- for each bit length `L = 1, …, 12`, the largest first-even index over the odd rows of that length, and the rows attaining it at `L = 11`;
- the decomposition of `edge_decomp`, for every odd `n` from `5` to `41` and every `j` with `4 j ≤ n`: the width `n + 2 j`, the run of `01` pairs, and a prefix that depends only on `j`.

The largest first-even index by bit length is `1, 3, 2, 3, 4, 5, 6, 5, 9, 7, 15, 8`, so the bound "bit length plus four" is attained at length `11`, and there only by `1493` and `1507` (COMPUTED).

```wl
f[y_] := BitXor[BitShiftRight[y, 1], BitOr[y, BitShiftLeft[y, 1]]];
firstEven[y_] := LengthWhile[NestList[f[f[#]] &, y, 400], OddQ];
maxima = Table[Max[firstEven /@ Select[Range[2^(len - 1), 2^len - 1], OddQ]], {len, 1, 12}];
arg11 = Select[Range[2^10 + 1, 2^11 - 1, 2], firstEven[#] == maxima[[11]] &];
tick[row_] := Prepend[Table[BitXor[row[[k + 2]], BitOr[row[[k + 1]], row[[k]]]], {k, 1, Length[row] - 2}], 0];
iterRow[n_, j_] := Nest[Append[tick[#], 0] &, Join[{0}, Table[Mod[k, 2], {k, 1, n}], ConstantArray[0, 2 j + 2]], 2 j];
decomp = And @@ Flatten[Table[Module[{row = iterRow[n, j], w = n + 2 j, k = (n + 1 - 2 j)/2, edge},
      edge = row[[w + 1 ;; 2 ;; -1]];
      {row[[w + 1]] == 1, Total[row[[w + 2 ;;]]] == 0, Take[edge, -2 k] == Flatten[ConstantArray[{0, 1}, k]],
       Take[edge, 4 j - 1] == Take[Reverse[iterRow[4 j + 1, j][[2 ;; 6 j + 2]]], 4 j - 1]}],
     {n, 5, 41, 2}, {j, 1, Floor[n/4]}]];
{firstEven[1493], firstEven[1507], maxima, arg11, decomp}
```

## 6. Prior art and scope

- **The barriers and the witnesses** are the kit's: `Rule30ZeroBoundaryBarriers` with `RankCert`, `CertE` and `JointCert`, the truncated stripes with `edge_split` and `Z_shift`, and `c7cut` with `jointRank_step`. This module adds the monoid image and general well-founded ranges; the kit's two-window theorems are its one-element-monoid cases.
- **Recognizable statistics** are classical: a language is regular exactly when it is recognized by a morphism into a finite monoid.
- **The two rows.** The portal entry R30-20261108-a0fd36, by a third party, observed that `1493` and `1507` are sharp for its bound, a first even iterate at most the bit length plus four. Here their survival is kernel-checked and turned into a barrier.
- **Scope.** The certificates quantify over all finite rows or configurations, and so do the witnesses. Nothing here covers ranks whose values do not factor through a finite monoid and the width, such as value-unbounded weighted automata, or obligations restricted to particular starts. As in the kit (`trunc_not_left_half`), the truncated stripes are never the left half of rule 30 at the start of an alternating tail. So these barriers concern arguments that use the zero-boundary dynamics alone. Nothing here decides `Q01` or period `2`.
- **History.** Cloud's swarm run proposed B2+ (BR-2.1) and the width-bounded rider (LN-06). GPT carried B2+ by hand in both frames. A Local sub-agent formalized both under Local's direction, and Local checked and packaged the module.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundaryBarriers`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers
/-!
# Rule 30, period 2: no ranking through a recognizable statistic

A *recognizable statistic* of a finite row is its image under a morphism from Boolean words into a
fixed finite monoid (`FinMonoid`; the morphism is fixed by the images `img false`, `img true` of the
two letters, `FinMonoid.eval`). Rows are read from their edge, depths `W, W - 1, …, 1`
(`Rule30ZeroBoundaryBarriers.edgeWord`). Reading from the wall instead is the same statistic for
the opposite monoid (`FinMonoid.op`, `FinMonoid.eval_reverse`).

**Zero-boundary frame.** `RecCert S img r R`: the rank `R W (image of the row)` of every finitely
supported row of width `W` moves down along `r` at every surviving double step.
* `no_recognizable_ranking`: for every finite monoid, every morphism and every well-founded `r`, no
  such certificate exists; `no_recognizable_ranking_nat` is the case of natural-number ranks, and
  `no_wall_recognizable_ranking` the case of the row read from the wall.
* `no_windowed_recognizable_ranking`: the same with the wall window and the edge window of
  `Rule30ZeroBoundaryBarriers.RankCert` added to the arguments of the rank. For the one-element
  monoid this is the kit theorem `Rule30ZeroBoundaryBarriers.no_local_ranking`
  (`no_local_ranking_of_recognizable`).

The proof follows the truncated stripes `trunc n`. After `j ≥ 1` double steps, with `n` odd and
`4 j ≤ n`, the row read from its edge is `Zw j` followed by `(01)^k`, `k = (n + 1 - 2 j) / 2`, where
`Zw j` does not depend on `n` (`edge_decomp`). The powers of the image of `01` repeat with some
period `π` from some index `k0` on. Along `j = 1 + i π`, two of the finitely many values of the
image of `Zw j` (and of the edge window) agree, at `j1 < j2`, and `d = j2 - j1` is a multiple of `π`.
Only then is the odd base depth `n0` chosen. For `r m j`, the row after `j` double steps from
`trunc (n0 + 2 m)`, the rows `r m j2` and `r (m + d) j1` have the same width, the same image and the
same windows: their stripe exponents differ by `2 d`. A certificate would give a chain from
`r (m + d) j1` down to `r m j1` for every `m`, an infinite descent.

**Two sharp rows.** `sharp_rows_check` (kernel evaluation of the integer form): the rows
`1493` and `1507` (bit `i` at depth `i + 1`, width `11`) keep depth `1` black at the even times
`0, 2, …, 28`, that is through fourteen surviving double steps, and turn it white at time `30`
(`sharp_rows_survive`, `sharp_rows_fourteen`). Hence `no_width_bounded_ranking`: no rank `ρ s W`
with values in `Int` between `-1` and the width `W` falls at every surviving double step; it would go
from at most `11` to below `-1`. Corollary `no_edge_automaton_ranking`: no automaton reading the row
from its edge gives a ranking by its longest accepted prefix
(`Rule30ZeroBoundaryBarriers.CertE`), with no bound on its number of states.

**Coupled frame.** In the two-sided frame of `Rule30ZeroBoundaryBarriers.JointCert` (strict decrease
at every step where the center column flips, over all finite configurations), the whole finite
configuration between its leftmost and its rightmost black cell is read from left to right
(`spanWord`). `no_joint_recognizable_ranking`: no rank through (leftmost black position, rightmost
black position, image of the configuration) into a well-founded order decreases at every flip of the
center column. `no_joint_windowed_recognizable_ranking` adds the center window and the two edge
windows; for the one-element monoid it is `Rule30ZeroBoundaryBarriers.no_joint_local_ranking`
(`no_joint_local_ranking_of_recognizable`). The witnesses are the truncations `c7cut N` of the
spatially `7`-periodic orbit. At a time `t` divisible by `28` their row is a left wedge of `2 t`
cells, an ether word of length `14 N + 8 - 2 t` (`etherWord`) and a right wedge of `2 t` cells
(`c7cut_span`); the wedges and the edge windows do not depend on `N` once `N` is large
(`wedgeData_indep`). Pigeonhole the images of both wedges
and both edge windows over the times `28 π i`, at `i1 < i2`, and compare the rows `(N, t2)` and
`(N + ε, t1)` with `7 ε = t2 - t1`: they have the same ends, the same center window, the same
windows, and ether lengths that differ by `28 ε`, a multiple of `7 π`.

Scope: the witnesses are finite configurations, and the certificates quantify over all of them.
Apart from the width-bounded case, nothing here covers ranks whose values do not factor through a
finite monoid and the width (for example value-unbounded weighted automata), nor obligations that
are restricted to particular starts. As in the kit (`Rule30ZeroBoundaryBarriers.trunc_not_left_half`),
the truncated-stripe witnesses are never the left half of rule 30 at the start of an alternating
tail, so the zero-boundary barriers concern arguments that use the zero-boundary dynamics alone.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30ZeroBoundary Rule30ZeroBoundaryBarriers
open Rule30ZeroBoundary.IntegerForm (rowOfNat G zrow_rowOfNat_col1 iter_G_eq_iter_F_two_mul)

/-! ### Finite monoids and recognizable statistics -/

/-- A finite monoid on the type `M`: an associative product with a unit, and a list `elems` that
contains every element. -/
structure FinMonoid (M : Type) where
  mul : M → M → M
  one : M
  elems : List M
  mem_elems : ∀ x, x ∈ elems
  mul_assoc : ∀ x y z, mul (mul x y) z = mul x (mul y z)
  one_mul : ∀ x, mul one x = x
  mul_one : ∀ x, mul x one = x

namespace FinMonoid

variable {M : Type}

/-- The image of a word under the monoid morphism with letter images `img`. -/
def eval (S : FinMonoid M) (img : Bool → M) : List Bool → M
  | [] => S.one
  | b :: w => S.mul (img b) (eval S img w)

theorem eval_cons (S : FinMonoid M) (img : Bool → M) (b : Bool) (w : List Bool) :
    S.eval img (b :: w) = S.mul (img b) (S.eval img w) := rfl

/-- The image of a concatenation is the product of the images. -/
theorem eval_append (S : FinMonoid M) (img : Bool → M) :
    ∀ u v : List Bool, S.eval img (u ++ v) = S.mul (S.eval img u) (S.eval img v)
  | [], v => (S.one_mul _).symm
  | b :: u, v => by
    rw [List.cons_append, eval_cons, eval_cons, eval_append S img u v, S.mul_assoc]

/-- The opposite monoid. -/
def op (S : FinMonoid M) : FinMonoid M where
  mul x y := S.mul y x
  one := S.one
  elems := S.elems
  mem_elems := S.mem_elems
  mul_assoc x y z := (S.mul_assoc z y x).symm
  one_mul := S.mul_one
  mul_one := S.one_mul

/-- Reading a word backwards is reading it in the opposite monoid. -/
theorem eval_reverse (S : FinMonoid M) (img : Bool → M) :
    ∀ w : List Bool, S.eval img w.reverse = S.op.eval img w
  | [] => rfl
  | b :: w => by
    rw [List.reverse_cons, eval_append, eval_reverse S img w]
    show S.mul (S.op.eval img w) (S.mul (img b) S.one) = S.mul (S.op.eval img w) (img b)
    rw [S.mul_one]

/-- The one-element monoid. -/
def unit : FinMonoid Unit where
  mul _ _ := ()
  one := ()
  elems := [()]
  mem_elems _ := List.mem_singleton.2 rfl
  mul_assoc _ _ _ := rfl
  one_mul _ := rfl
  mul_one _ := rfl

end FinMonoid

open FinMonoid

/-- No infinite descending chain in a well-founded relation. -/
theorem no_descent {α : Type} {r : α → α → Prop} (hwf : WellFounded r) (f : Nat → α)
    (h : ∀ k, r (f (k + 1)) (f k)) : False := by
  have key : ∀ a, Acc r a → ∀ k, f k = a → False := by
    intro a ha
    induction ha with
    | intro a _ ih => intro k hk; exact ih (f (k + 1)) (hk ▸ h k) (k + 1) rfl
  exact key (f 0) (hwf.apply (f 0)) 0 rfl

/-- A sequence driven by a fixed left factor is periodic from the first index where it repeats. -/
theorem periodic_tail {M : Type} (mul : M → M → M) (q : M) (f : Nat → M)
    (hf : ∀ k, f (k + 1) = mul q (f k)) {k0 π : Nat} (h : f (k0 + π) = f k0) :
    ∀ a c, k0 ≤ a → f (a + c * π) = f a := by
  have one : ∀ x, f (k0 + x + π) = f (k0 + x) := by
    intro x
    induction x with
    | zero => simpa using h
    | succ x ih =>
      rw [show k0 + (x + 1) + π = (k0 + x + π) + 1 by omega, hf, ih]
      exact (hf (k0 + x)).symm
  have all : ∀ c x, f (k0 + x + c * π) = f (k0 + x) := by
    intro c
    induction c with
    | zero => intro x; simp
    | succ c ih =>
      intro x
      rw [show k0 + x + (c + 1) * π = k0 + (x + c * π) + π by rw [Nat.succ_mul]; omega, one,
        show k0 + (x + c * π) = k0 + x + c * π by omega, ih]
  intro a c ha
  have := all c (a - k0)
  rw [show k0 + (a - k0) = a by omega] at this
  exact this

/-- All pairs from two lists. -/
def prodList {A B : Type} (LA : List A) (LB : List B) : List (A × B) :=
  LA.flatMap fun a => LB.map fun b => (a, b)

theorem mem_prodList {A B : Type} {LA : List A} {LB : List B} {a : A} {b : B} (ha : a ∈ LA)
    (hb : b ∈ LB) : (a, b) ∈ prodList LA LB :=
  List.mem_flatMap.2 ⟨a, ha, List.mem_map.2 ⟨b, hb, rfl⟩⟩

theorem mem_allLists_of_length {l : List Bool} {e : Nat} (h : l.length = e) : l ∈ allLists e := by
  have := mem_allLists l
  rwa [h] at this

/-! ### The zero-boundary frame -/

/-- The row read from the wall: depths `1, 2, …, W`. -/
def wallWord (s : Nat → Bool) (W : Nat) : List Bool := (List.range W).map fun i => s (i + 1)

theorem wallWord_eq_reverse (s : Nat → Bool) : ∀ W, wallWord s W = (edgeWord s W).reverse
  | 0 => rfl
  | W + 1 => by
    have h1 : wallWord s (W + 1) = wallWord s W ++ [s (W + 1)] := by
      simp [wallWord, List.range_succ]
    have h2 : edgeWord s (W + 1) = s (W + 1) :: edgeWord s W := by
      unfold edgeWord
      rw [List.range_succ_eq_map, List.map_cons, List.map_map, Nat.sub_zero]
      congr 1
      apply List.map_congr_left
      intro i _
      show s (W + 1 - (i + 1)) = s (W - i)
      congr 1
      omega
    rw [h1, h2, List.reverse_cons, wallWord_eq_reverse s W]

/-- A ranking certificate through (width, recognizable statistic of the row read from its edge),
with values in `α` ordered by `r`: at every surviving double step of every finitely supported start
of width `W`, the rank moves down along `r`. -/
def RecCert {M α : Type} (S : FinMonoid M) (img : Bool → M) (r : α → α → Prop) (R : Nat → M → α) :
    Prop :=
  ∀ (s : Nat → Bool) (W : Nat), 1 ≤ W → s W = true → (∀ k, W < k → s k = false) → Survives s →
    r (R (W + 2) (S.eval img (edgeWord (fun k => zrow s 2 k) (W + 2)))) (R W (S.eval img (edgeWord s W)))

/-- The same with the row read from the wall, depths `1, 2, …, W`. -/
def WallRecCert {M α : Type} (S : FinMonoid M) (img : Bool → M) (r : α → α → Prop)
    (R : Nat → M → α) : Prop :=
  ∀ (s : Nat → Bool) (W : Nat), 1 ≤ W → s W = true → (∀ k, W < k → s k = false) → Survives s →
    r (R (W + 2) (S.eval img (wallWord (fun k => zrow s 2 k) (W + 2)))) (R W (S.eval img (wallWord s W)))

/-- A ranking certificate through (width, wall window, edge window, recognizable statistic). -/
def WinRecCert {M α : Type} (w e : Nat) (S : FinMonoid M) (img : Bool → M) (r : α → α → Prop)
    (R : Nat → List Bool → List Bool → M → α) : Prop :=
  ∀ (s : Nat → Bool) (W : Nat), 1 ≤ W → s W = true → (∀ k, W < k → s k = false) → Survives s →
    r (R (W + 2) (wallW w (fun k => zrow s 2 k)) (edgeW e (fun k => zrow s 2 k) (W + 2))
        (S.eval img (edgeWord (fun k => zrow s 2 k) (W + 2))))
      (R W (wallW w s) (edgeW e s W) (S.eval img (edgeWord s W)))

/-- The edge-side part of the truncated-stripe iterate after `j` double steps. -/
def Zw (j : Nat) : List Bool :=
  (List.range (4 * j - 1)).map fun i => zrow (trunc (4 * j + 1)) (2 * j) (4 * j + 1 + 2 * j - i)

/-- **Decomposition.** For odd `n`, `1 ≤ j` and `4 j ≤ n`, the truncated-stripe iterate after `j`
double steps, read from its edge, is `Zw j` followed by `(01)^k` with `k = (n + 1 - 2 j) / 2`; the
word `Zw j` does not depend on `n`. -/
theorem edge_decomp {n j : Nat} (hn : n % 2 = 1) (hj1 : 1 ≤ j) (hj : 4 * j ≤ n) :
    edgeWord (iter (trunc n) j) (n + 2 * j) = Zw j ++ altWord ((n + 1 - 2 * j) / 2) := by
  rw [edge_split hn j hj1 hj]
  congr 1
  obtain ⟨m, rfl⟩ : ∃ m, n = 4 * j + 1 + 2 * m := ⟨(n - 4 * j - 1) / 2, by omega⟩
  exact Z_shift (4 * j + 1) m j (by omega)

theorem eval_altWord_succ {M : Type} (S : FinMonoid M) (img : Bool → M) (k : Nat) :
    S.eval img (altWord (k + 1)) = S.mul (S.mul (img false) (img true)) (S.eval img (altWord k)) := by
  show S.mul (img false) (S.mul (img true) (S.eval img (altWord k))) = _
  rw [S.mul_assoc]

/-- **No ranking through width, wall window, edge window and a recognizable statistic.** For every
finite monoid `S`, letter images `img`, window sizes `w`, `e` and well-founded relation `r`, no rank
through (width, wall window, edge window, image of the row read from its edge) moves down along `r`
at every surviving double step of every finitely supported start. -/
theorem no_windowed_recognizable_ranking {M α : Type} (w e : Nat) (S : FinMonoid M)
    (img : Bool → M) {r : α → α → Prop} (hwf : WellFounded r)
    (R : Nat → List Bool → List Bool → M → α) : ¬ WinRecCert w e S img r R := by
  intro hR
  -- the powers of the image of `01` repeat from `k0` on with period `π`
  let pw : Nat → M := fun k => S.eval img (altWord k)
  obtain ⟨k0, k1, hk, -, hpk⟩ := pigeonhole_gen S.elems pw (fun _ => S.mem_elems _)
  obtain ⟨π, hπ⟩ : ∃ π, π = k1 - k0 := ⟨_, rfl⟩
  have hper : ∀ a c, k0 ≤ a → pw (a + c * π) = pw a :=
    periodic_tail S.mul (S.mul (img false) (img true)) pw (fun k => eval_altWord_succ S img k)
      (by rw [show k0 + π = k1 by omega]; exact hpk.symm)
  -- the images of `Zw j` and the edge windows, along `j = 1 + i π`
  obtain ⟨nb, hnb⟩ : ∃ nb, nb = 2 * e + 1 := ⟨_, rfl⟩
  let E : Nat → List Bool := fun j => edgeW e (iter (trunc nb) j) (nb + 2 * j)
  let v : Nat → M × List Bool := fun i => (S.eval img (Zw (1 + i * π)), E (1 + i * π))
  obtain ⟨i1, i2, hi, -, hv⟩ := pigeonhole_gen (prodList S.elems (allLists e)) v
    (fun i => mem_prodList (S.mem_elems _) (mem_allLists_of_length (by simp [E, edgeW])))
  obtain ⟨j1, hj1⟩ : ∃ j, j = 1 + i1 * π := ⟨_, rfl⟩
  obtain ⟨j2, hj2⟩ : ∃ j, j = 1 + i2 * π := ⟨_, rfl⟩
  have hZ : S.eval img (Zw j1) = S.eval img (Zw j2) := by
    rw [hj1, hj2]; exact congrArg Prod.fst hv
  have hE : E j1 = E j2 := by
    rw [hj1, hj2]; exact congrArg Prod.snd hv
  have hlt : i1 * π < i2 * π := Nat.mul_lt_mul_of_pos_right hi (by omega)
  obtain ⟨d, hd⟩ : ∃ d, d = j2 - j1 := ⟨_, rfl⟩
  have hdπ : d = (i2 - i1) * π := by rw [hd, hj1, hj2, Nat.sub_mul]; omega
  have h2d : 2 * d = (2 * (i2 - i1)) * π := by rw [hdπ, Nat.mul_assoc]
  -- only now the base depth
  obtain ⟨n0, hn0⟩ : ∃ n, n = nb + 2 * (4 * j2 + k0 + w) := ⟨_, rfl⟩
  let row : Nat → Nat → (Nat → Bool) := fun m j => iter (trunc (n0 + 2 * m)) j
  let ρ : Nat → Nat → α := fun m j =>
    R (n0 + 2 * m + 2 * j) (wallW w (row m j)) (edgeW e (row m j) (n0 + 2 * m + 2 * j))
      (S.eval img (edgeWord (row m j) (n0 + 2 * m + 2 * j)))
  have step : ∀ m j, 2 * j + 2 ≤ n0 + 2 * m → r (ρ m (j + 1)) (ρ m j) := by
    intro m j hj
    have hn : (n0 + 2 * m) % 2 = 1 := by omega
    have hw := zrow_edge (L := trunc (n0 + 2 * m)) (m := n0 + 2 * m) (by omega)
      (trunc_width hn).1 (trunc_width hn).2 (2 * j)
    have h := hR (row m j) (n0 + 2 * m + 2 * j) (by omega) hw.1 hw.2 (iter_survives hn hj)
    have hit : (fun k => zrow (row m j) 2 k) = row m (j + 1) := (iter_dstep _ j).symm
    rw [hit, show n0 + 2 * m + 2 * j + 2 = n0 + 2 * m + 2 * (j + 1) by omega] at h
    exact h
  have chain : ∀ m i, 1 ≤ i → i ≤ d → Relation.TransGen r (ρ m (j1 + i)) (ρ m j1) := by
    intro m i
    induction i with
    | zero => intro h; omega
    | succ i ih =>
      intro _ hi
      have hs := step m (j1 + i) (by omega)
      by_cases h0 : i = 0
      · subst h0; exact Relation.TransGen.single hs
      · exact Relation.TransGen.trans (Relation.TransGen.single hs) (ih (by omega) (by omega))
  have eq : ∀ m, ρ m j2 = ρ (m + d) j1 := by
    intro m
    have hn : (n0 + 2 * m) % 2 = 1 := by omega
    have hn' : (n0 + 2 * (m + d)) % 2 = 1 := by omega
    have hW : n0 + 2 * m + 2 * j2 = n0 + 2 * (m + d) + 2 * j1 := by omega
    have hwall1 : wallW w (row m j2) = wallW w stripe := wall_iter hn w j2 (by omega)
    have hwall2 : wallW w (row (m + d) j1) = wallW w stripe := wall_iter hn' w j1 (by omega)
    have hedge1 : edgeW e (row m j2) (n0 + 2 * m + 2 * j2) = E j2 := by
      show edgeW e (iter (trunc (n0 + 2 * m)) j2) (n0 + 2 * m + 2 * j2) = _
      rw [show n0 + 2 * m = nb + 2 * (4 * j2 + k0 + w + m) by omega]
      exact edge_iter nb (4 * j2 + k0 + w + m) e j2 (by omega)
    have hedge2 : edgeW e (row (m + d) j1) (n0 + 2 * (m + d) + 2 * j1) = E j1 := by
      show edgeW e (iter (trunc (n0 + 2 * (m + d))) j1) (n0 + 2 * (m + d) + 2 * j1) = _
      rw [show n0 + 2 * (m + d) = nb + 2 * (4 * j2 + k0 + w + m + d) by omega]
      exact edge_iter nb (4 * j2 + k0 + w + m + d) e j1 (by omega)
    have hmu : S.eval img (edgeWord (row m j2) (n0 + 2 * m + 2 * j2)) =
        S.eval img (edgeWord (row (m + d) j1) (n0 + 2 * (m + d) + 2 * j1)) := by
      show S.eval img (edgeWord (iter (trunc (n0 + 2 * m)) j2) (n0 + 2 * m + 2 * j2)) =
        S.eval img (edgeWord (iter (trunc (n0 + 2 * (m + d))) j1) (n0 + 2 * (m + d) + 2 * j1))
      rw [edge_decomp hn (by omega) (by omega), edge_decomp hn' (by omega) (by omega), eval_append,
        eval_append, hZ]
      congr 1
      have ha : (n0 + 2 * (m + d) + 1 - 2 * j1) / 2 =
          (n0 + 2 * m + 1 - 2 * j2) / 2 + (2 * (i2 - i1)) * π := by omega
      rw [ha]
      exact (hper _ _ (by omega)).symm
    show R (n0 + 2 * m + 2 * j2) (wallW w (row m j2)) (edgeW e (row m j2) (n0 + 2 * m + 2 * j2))
        (S.eval img (edgeWord (row m j2) (n0 + 2 * m + 2 * j2))) =
      R (n0 + 2 * (m + d) + 2 * j1) (wallW w (row (m + d) j1))
        (edgeW e (row (m + d) j1) (n0 + 2 * (m + d) + 2 * j1))
        (S.eval img (edgeWord (row (m + d) j1) (n0 + 2 * (m + d) + 2 * j1)))
    rw [hmu, hwall1, hwall2, hedge1, hedge2, hE, hW]
  have desc : ∀ m, Relation.TransGen r (ρ (m + d) j1) (ρ m j1) := by
    intro m
    rw [← eq m]
    have h := chain m d (by omega) (Nat.le_refl _)
    rw [show j1 + d = j2 by omega] at h
    exact h
  exact no_descent hwf.transGen (fun k => ρ (k * d) j1) fun k => by
    show Relation.TransGen r (ρ ((k + 1) * d) j1) (ρ (k * d) j1)
    rw [Nat.succ_mul]
    exact desc (k * d)

/-- **No ranking through width and a recognizable statistic.** For every finite monoid, every
monoid morphism from Boolean words (fixed by its letter images `img`) and every well-founded
relation `r`, no rank through (width, image of the row read from its edge) moves down along `r` at
every surviving double step of every finitely supported start. -/
theorem no_recognizable_ranking {M α : Type} (S : FinMonoid M) (img : Bool → M)
    {r : α → α → Prop} (hwf : WellFounded r) (R : Nat → M → α) : ¬ RecCert S img r R :=
  fun hR => no_windowed_recognizable_ranking 0 0 S img hwf (fun W _ _ x => R W x)
    fun s W h1 h2 h3 h4 => hR s W h1 h2 h3 h4

/-- **Natural-number ranks.** No function of (width, image of the row read from its edge under a
morphism into a finite monoid) into `Nat` strictly decreases at every surviving double step of every
finitely supported start. -/
theorem no_recognizable_ranking_nat {M : Type} (S : FinMonoid M) (img : Bool → M)
    (R : Nat → M → Nat) : ¬ RecCert S img (fun a b => a < b) R :=
  no_recognizable_ranking S img Nat.lt_wfRel.wf R

/-- **Reading from the wall.** The same barrier for the row read from the wall, depths
`1, 2, …, W`: this is the image of the row read from its edge in the opposite monoid. -/
theorem no_wall_recognizable_ranking {M α : Type} (S : FinMonoid M) (img : Bool → M)
    {r : α → α → Prop} (hwf : WellFounded r) (R : Nat → M → α) : ¬ WallRecCert S img r R := by
  intro hR
  apply no_recognizable_ranking S.op img hwf R
  intro s W h1 h2 h3 h4
  have h := hR s W h1 h2 h3 h4
  rw [wallWord_eq_reverse, wallWord_eq_reverse, eval_reverse, eval_reverse] at h
  exact h

/-- **The kit barrier on width, wall window and edge window, recovered.** This is
`Rule30ZeroBoundaryBarriers.no_local_ranking`, obtained from `no_windowed_recognizable_ranking` for
the one-element monoid. -/
theorem no_local_ranking_of_recognizable (w e : Nat) (R : Nat → List Bool → List Bool → Nat) :
    ¬ RankCert w e R :=
  fun hR => no_windowed_recognizable_ranking w e FinMonoid.unit (fun _ => ()) Nat.lt_wfRel.wf
    (fun W a b _ => R W a b) fun s W h1 h2 h3 h4 => hR s W h1 h2 h3 h4

/-! ### Two sharp rows -/

/-- **Kernel check.** Under the two-step map `G` of the integer form (bit `i` of the number at depth
`i + 1`), the numbers `1493` and `1507` stay odd for the iterates `0, 1, …, 14` and the fifteenth
iterate is even. Both have bit length `11`, so the first even iterate is the bit length plus four.
Credit: the portal entry R30-20261108-a0fd36 (by a third party) noted that these two rows are
empirically sharp for its bound, first even iterate at most size plus four. -/
theorem sharp_rows_check :
    (∀ s, s < 15 → (Rule30ZeroBoundary.IntegerForm.iter G s 1493).testBit 0 = true) ∧
      (Rule30ZeroBoundary.IntegerForm.iter G 15 1493).testBit 0 = false ∧
    (∀ s, s < 15 → (Rule30ZeroBoundary.IntegerForm.iter G s 1507).testBit 0 = true) ∧
      (Rule30ZeroBoundary.IntegerForm.iter G 15 1507).testBit 0 = false := by
  decide +kernel

theorem col1_even (Y s : Nat) :
    zrow (rowOfNat Y) (2 * s) 1 = (Rule30ZeroBoundary.IntegerForm.iter G s Y).testBit 0 := by
  rw [zrow_rowOfNat_col1, iter_G_eq_iter_F_two_mul]

/-- **The two rows have width `11`.** -/
theorem sharp_rows_width {Y : Nat} (hY : Y = 1493 ∨ Y = 1507) :
    rowOfNat Y 11 = true ∧ ∀ k, 11 < k → rowOfNat Y k = false := by
  have hlt : Y < 2 ^ 11 := by rcases hY with rfl | rfl <;> decide
  refine ⟨by rcases hY with rfl | rfl <;> decide, fun k hk => ?_⟩
  obtain ⟨i, rfl⟩ : ∃ i, k = i + 1 := ⟨k - 1, by omega⟩
  show Y.testBit i = false
  apply Nat.testBit_lt_two_pow
  have : 2 ^ 11 ≤ 2 ^ i := Nat.pow_le_pow_right (by omega) (by omega)
  omega

/-- **Survival.** In the zero-boundary left half, the rows `1493` and `1507` keep depth `1` black
at every even time `t ≤ 28` and turn it white at time `30`. -/
theorem sharp_rows_survive {Y : Nat} (hY : Y = 1493 ∨ Y = 1507) :
    (∀ t, t ≤ 28 → t % 2 = 0 → zrow (rowOfNat Y) t 1 = true) ∧ zrow (rowOfNat Y) 30 1 = false := by
  obtain ⟨h1, h2, h3, h4⟩ := sharp_rows_check
  refine ⟨fun t ht he => ?_, ?_⟩
  · rw [show t = 2 * (t / 2) by omega, col1_even]
    rcases hY with rfl | rfl
    · exact h1 _ (by omega)
    · exact h3 _ (by omega)
  · rw [show (30 : Nat) = 2 * 15 from rfl, col1_even]
    rcases hY with rfl | rfl
    · exact h2
    · exact h4

/-- **Fourteen surviving double steps**, and the fifteenth does not survive. -/
theorem sharp_rows_fourteen {Y : Nat} (hY : Y = 1493 ∨ Y = 1507) :
    (∀ j, j ≤ 13 → Survives (iter (rowOfNat Y) j)) ∧ ¬ Survives (iter (rowOfNat Y) 14) := by
  have h := sharp_rows_survive hY
  refine ⟨fun j hj => ?_, fun hs => ?_⟩
  · unfold Survives
    rw [iter_zrow, iter_zrow]
    exact ⟨h.1 _ (by omega) (by omega), h.1 _ (by omega) (by omega)⟩
  · have h2 := hs.2
    rw [iter_zrow] at h2
    rw [h.2] at h2
    exact Bool.false_ne_true h2

/-- **No width-bounded ranking.** No rank `ρ s W` of the finitely supported rows `s` of width `W`,
with values in `Int` between `-1` and `W`, strictly decreases at every surviving double step: from
the row `1493`, of width `11`, it would fall fourteen times and end below `-1`. -/
theorem no_width_bounded_ranking (ρ : (Nat → Bool) → Nat → Int)
    (hbd : ∀ s W, 1 ≤ W → s W = true → (∀ k, W < k → s k = false) → -1 ≤ ρ s W ∧ ρ s W ≤ W) :
    ¬ ∀ s W, 1 ≤ W → s W = true → (∀ k, W < k → s k = false) → Survives s →
      ρ (fun k => zrow s 2 k) (W + 2) < ρ s W := by
  intro hR
  have hwid := sharp_rows_width (Y := 1493) (Or.inl rfl)
  have hedge := zrow_edge (L := rowOfNat 1493) (m := 11) (by omega) hwid.1 hwid.2
  have hsurv := (sharp_rows_fourteen (Y := 1493) (Or.inl rfl)).1
  have chain : ∀ j, j ≤ 14 →
      ρ (iter (rowOfNat 1493) j) (11 + 2 * j) + j ≤ ρ (iter (rowOfNat 1493) 0) 11 := by
    intro j
    induction j with
    | zero => intro _; simp
    | succ j ih =>
      intro hj
      have h := hR (iter (rowOfNat 1493) j) (11 + 2 * j) (by omega) (hedge (2 * j)).1
        (hedge (2 * j)).2 (hsurv j (by omega))
      rw [show (fun k => zrow (iter (rowOfNat 1493) j) 2 k) = iter (rowOfNat 1493) (j + 1) from
        (iter_dstep _ j).symm, show 11 + 2 * j + 2 = 11 + 2 * (j + 1) by omega] at h
      have := ih (by omega)
      push_cast
      omega
  have h14 := chain 14 (by omega)
  have hb0 := hbd (iter (rowOfNat 1493) 0) 11 (by omega) (hedge 0).1 (hedge 0).2
  have hb14 := hbd (iter (rowOfNat 1493) 14) (11 + 2 * 14) (by omega) (hedge (2 * 14)).1
    (hedge (2 * 14)).2
  omega

/-- **No automaton ranking by the longest accepted prefix, of any size.** For every automaton
`A` (states in `Nat`, no bound on their number), the length of the longest accepted prefix of the
row read from its edge is not a ranking: it lies between `-1` and the width, so
`no_width_bounded_ranking` applies. This drops the finiteness hypothesis of
`Rule30ZeroBoundaryBarriers.no_edge_dfa_ranking`. -/
theorem no_edge_automaton_ranking (A : DFA) : ¬ CertE A := by
  intro hA
  refine no_width_bounded_ranking (fun s W => maxAcc A 0 (edgeWord s W)) ?_ hA
  intro s W _ _ _
  refine ⟨maxAcc_ge A 0 _, ?_⟩
  have := maxAcc_le A 0 (edgeWord s W)
  simpa [edgeWord] using this

/-! ### The coupled frame -/

open Rule30Realization (evol)

/-- The cells of `x` at the positions `lo, lo + 1, …, lo + n - 1`, from left to right. -/
def rowWord (x : Int → Bool) (lo : Int) (n : Nat) : List Bool :=
  (List.range n).map fun (i : Nat) => x (lo + (i : Int))

/-- The configuration `x` between the positions `lo` and `hi`, from left to right. -/
def spanWord (x : Int → Bool) (lo hi : Int) : List Bool := rowWord x lo (hi + 1 - lo).toNat

theorem rowWord_add (x : Int → Bool) (lo : Int) (a b : Nat) :
    rowWord x lo (a + b) = rowWord x lo a ++ rowWord x (lo + a) b := by
  unfold rowWord
  rw [range_add_map]
  congr 1
  apply List.map_congr_left
  intro i _
  congr 1
  push_cast
  omega

/-- A ranking certificate in the coupled frame through (leftmost black position, rightmost black
position, center window, left-edge window, right-edge window, recognizable statistic of the whole
configuration read from left to right), with values in `α` ordered by `r`: at every step where the
center column flips, the rank moves down along `r`. -/
def JointWinRecCert {M α : Type} (w e : Nat) (S : FinMonoid M) (img : Bool → M)
    (r : α → α → Prop) (R : Int → Int → List Bool → List Bool → List Bool → M → α) : Prop :=
  ∀ (x : Int → Bool) (lo hi : Int), x lo = true → x hi = true → (∀ p, p < lo → x p = false) →
    (∀ p, hi < p → x p = false) → evol x 1 0 = !evol x 0 0 →
    r (R (lo - 1) (hi + 1) (centerWin w (fun p => evol x 1 p))
        (leftWin e (fun p => evol x 1 p) (lo - 1)) (rightWin e (fun p => evol x 1 p) (hi + 1))
        (S.eval img (spanWord (fun p => evol x 1 p) (lo - 1) (hi + 1))))
      (R lo hi (centerWin w x) (leftWin e x lo) (rightWin e x hi) (S.eval img (spanWord x lo hi)))

/-- A ranking certificate in the coupled frame through (leftmost black position, rightmost black
position, recognizable statistic of the whole configuration read from left to right). -/
def JointRecCert {M α : Type} (S : FinMonoid M) (img : Bool → M) (r : α → α → Prop)
    (R : Int → Int → M → α) : Prop :=
  ∀ (x : Int → Bool) (lo hi : Int), x lo = true → x hi = true → (∀ p, p < lo → x p = false) →
    (∀ p, hi < p → x p = false) → evol x 1 0 = !evol x 0 0 →
    r (R (lo - 1) (hi + 1) (S.eval img (spanWord (fun p => evol x 1 p) (lo - 1) (hi + 1))))
      (R lo hi (S.eval img (spanWord x lo hi)))

/-- The ether `c7` read from the position `-1` on: black exactly at the multiples of `7`. -/
def etherWord (L : Nat) : List Bool := (List.range L).map fun (i : Nat) => c7 ((i : Int) - 1)

theorem etherWord_add (k L : Nat) : etherWord (7 * k + L) = etherWord (7 * k) ++ etherWord L := by
  unfold etherWord
  rw [range_add_map]
  congr 1
  apply List.map_congr_left
  intro i _
  rw [show (((7 * k + i : Nat) : Int) - 1) = ((i : Int) - 1) + 7 * (k : Int) by push_cast; omega,
    c7_shift]

/-- The row of the truncation `c7cut N` at time `t`. -/
def cx (N t : Nat) : Int → Bool := fun p => evol (c7cut N) t p
/-- The leftmost black position of `c7cut N` at time `t`. -/
def clo (N t : Nat) : Int := -(7 * (N : Int) + 1) - t
/-- The rightmost black position of `c7cut N` at time `t`. -/
def chi (N t : Nat) : Int := 7 * (N : Int) + 6 + t
/-- The first position of the right wedge (the last `2 t` cells) of `c7cut N` at time `t`. -/
def crs (N t : Nat) : Int := 7 * (N : Int) + 7 - t

/-- **Shape of the truncated rows.** At a time `t = 28 c` with `2 t ≤ 14 N + 8`, the row of
`c7cut N` between its ends is the left wedge of `2 t` cells, the ether word of length
`14 N + 8 - 2 t`, and the right wedge of `2 t` cells. -/
theorem c7cut_span (N c : Nat) (h : 2 * (28 * c) ≤ 14 * N + 8) :
    spanWord (cx N (28 * c)) (clo N (28 * c)) (chi N (28 * c)) =
      rowWord (cx N (28 * c)) (clo N (28 * c)) (2 * (28 * c)) ++
        (etherWord (14 * N + 8 - 2 * (28 * c)) ++
          rowWord (cx N (28 * c)) (crs N (28 * c)) (2 * (28 * c))) := by
  unfold spanWord
  rw [show (chi N (28 * c) + 1 - clo N (28 * c)).toNat =
      2 * (28 * c) + ((14 * N + 8 - 2 * (28 * c)) + 2 * (28 * c)) by unfold chi clo; omega,
    rowWord_add, rowWord_add]
  have hev : ∀ p, evol c7 (28 * c) p = c7 p := by
    intro p
    rw [show 28 * c = 0 + 4 * (7 * c) by omega, evol_c7_period_mul]
    rfl
  have hmid : rowWord (cx N (28 * c)) (clo N (28 * c) + ((2 * (28 * c) : Nat) : Int))
      (14 * N + 8 - 2 * (28 * c)) = etherWord (14 * N + 8 - 2 * (28 * c)) := by
    unfold rowWord etherWord
    apply List.map_congr_left
    intro i hi
    have hi' := List.mem_range.1 hi
    show evol (c7cut N) (28 * c) (clo N (28 * c) + ((2 * (28 * c) : Nat) : Int) + (i : Int)) =
      c7 ((i : Int) - 1)
    rw [c7cut_agree N (28 * c) (clo N (28 * c) + ((2 * (28 * c) : Nat) : Int) + (i : Int))
        (by unfold clo; omega) (by unfold clo; omega), hev,
      show clo N (28 * c) + ((2 * (28 * c) : Nat) : Int) + (i : Int) =
        ((i : Int) - 1) + 7 * (4 * (c : Int) - N) by unfold clo; push_cast; omega, c7_shift]
  rw [hmid, show clo N (28 * c) + ((2 * (28 * c) : Nat) : Int) +
      ((14 * N + 8 - 2 * (28 * c) : Nat) : Int) = crs N (28 * c) by unfold clo crs; omega]

/-- The left wedge does not depend on `N`. -/
theorem leftWedge_indep (N m t : Nat) (h : 2 * t ≤ 14 * N + 7) :
    rowWord (cx (N + m) t) (clo (N + m) t) (2 * t) = rowWord (cx N t) (clo N t) (2 * t) :=
  leftWin_indep (2 * t) N m t h

/-- The right wedge does not depend on `N`. -/
theorem rightWedge_indep (N m t : Nat) (h : 2 * t ≤ 14 * N + 8) :
    rowWord (cx (N + m) t) (crs (N + m) t) (2 * t) = rowWord (cx N t) (crs N t) (2 * t) := by
  unfold rowWord
  apply map_range_congr
  intro i _
  have := evol_local_ge (x := c7cut N) (x' := c7cut (N + m)) (d := 7 * (m : Int))
    (a := -(7 * (N : Int) + 1)) (fun p hp => c7cut_right_shift N m p hp) t (crs N t + i)
    (by unfold crs; omega)
  rw [show crs N t + (i : Int) + 7 * (m : Int) = crs (N + m) t + i by unfold crs; push_cast; omega]
    at this
  exact this

/-- The data compared by the pigeonhole: both edge windows and the images of both wedges. -/
def wedgeData {M : Type} (e : Nat) (S : FinMonoid M) (img : Bool → M) (N t : Nat) :
    List Bool × (M × M) :=
  (leftWin e (cx N t) (clo N t) ++ rightWin e (cx N t) (chi N t),
    (S.eval img (rowWord (cx N t) (clo N t) (2 * t)), S.eval img (rowWord (cx N t) (crs N t) (2 * t))))

theorem wedgeData_indep {M : Type} (e : Nat) (S : FinMonoid M) (img : Bool → M) (N m t : Nat)
    (he : e ≤ 14 * N + 7) (ht : 2 * t ≤ 14 * N + 7) :
    wedgeData e S img (N + m) t = wedgeData e S img N t := by
  have h1 : leftWin e (cx (N + m) t) (clo (N + m) t) = leftWin e (cx N t) (clo N t) :=
    leftWin_indep e N m t he
  have h2 : rightWin e (cx (N + m) t) (chi (N + m) t) = rightWin e (cx N t) (chi N t) :=
    rightWin_indep e N m t he
  unfold wedgeData
  rw [h1, h2, leftWedge_indep N m t ht, rightWedge_indep N m t (by omega)]

/-- The ranked quantity along the run of `c7cut N`. -/
def jrank {M α : Type} (w e : Nat) (S : FinMonoid M) (img : Bool → M)
    (R : Int → Int → List Bool → List Bool → List Bool → M → α) (N t : Nat) : α :=
  R (clo N t) (chi N t) (centerWin w (cx N t)) (leftWin e (cx N t) (clo N t))
    (rightWin e (cx N t) (chi N t)) (S.eval img (spanWord (cx N t) (clo N t) (chi N t)))

theorem jrank_step {M α : Type} {w e : Nat} {S : FinMonoid M} {img : Bool → M} {r : α → α → Prop}
    {R : Int → Int → List Bool → List Bool → List Bool → M → α} (hR : JointWinRecCert w e S img r R)
    (N t : Nat) (ht : t + 1 ≤ 7 * N + 1) :
    r (jrank w e S img R N (t + 1)) (jrank w e S img R N t) := by
  have hl := left_edge (x := c7cut N) (lo := -(7 * (N : Int) + 1)) (c7cut_lo N)
    (fun p hp => c7cut_below N p hp) t
  have hr := right_edge (x := c7cut N) (hi := 7 * (N : Int) + 6) (c7cut_hi N)
    (fun p hp => c7cut_above N p hp) t
  have halt : evol (fun p => evol (c7cut N) t p) 1 0 = !evol (fun p => evol (c7cut N) t p) 0 0 := by
    simp only [evol_restart, Nat.add_zero]
    rw [c7cut_agree N (t + 1) 0 (by omega) (by omega), c7cut_agree N t 0 (by omega) (by omega)]
    exact c7_center t
  have h := hR (fun p => evol (c7cut N) t p) (-(7 * (N : Int) + 1) - t) (7 * (N : Int) + 6 + t)
    hl.1 hr.1 hl.2 hr.2 halt
  have hfun : (fun p => evol (fun p => evol (c7cut N) t p) 1 p) =
      (fun p => evol (c7cut N) (t + 1) p) := by
    funext p; rw [evol_restart]
  rw [hfun, show -(7 * (N : Int) + 1) - ↑t - 1 = -(7 * (N : Int) + 1) - ↑(t + 1) by push_cast; omega,
    show 7 * (N : Int) + 6 + ↑t + 1 = 7 * (N : Int) + 6 + ↑(t + 1) by push_cast; omega] at h
  exact h

theorem jrank_chain {M α : Type} {w e : Nat} {S : FinMonoid M} {img : Bool → M} {r : α → α → Prop}
    {R : Int → Int → List Bool → List Bool → List Bool → M → α} (hR : JointWinRecCert w e S img r R)
    (N t : Nat) : ∀ d, 1 ≤ d → t + d ≤ 7 * N + 1 →
      Relation.TransGen r (jrank w e S img R N (t + d)) (jrank w e S img R N t) := by
  intro d
  induction d with
  | zero => intro h; omega
  | succ d ih =>
    intro _ hd
    have hs := jrank_step hR N (t + d) (by omega)
    by_cases h0 : d = 0
    · subst h0; exact Relation.TransGen.single hs
    · exact Relation.TransGen.trans (Relation.TransGen.single hs) (ih (by omega) (by omega))

/-- **Coupled frame: no ranking through the ends, the windows and a recognizable statistic.** For
every finite monoid `S`, letter images `img`, window sizes `w`, `e` and well-founded relation `r`,
no rank through (leftmost black position, rightmost black position, center window, left-edge
window, right-edge window, image of the whole configuration read from left to right) moves down
along `r` at every step where the center column flips, over all finite configurations. -/
theorem no_joint_windowed_recognizable_ranking {M α : Type} (w e : Nat) (S : FinMonoid M)
    (img : Bool → M) {r : α → α → Prop} (hwf : WellFounded r)
    (R : Int → Int → List Bool → List Bool → List Bool → M → α) :
    ¬ JointWinRecCert w e S img r R := by
  intro hR
  -- the powers of the image of one ether block repeat from `k0` on with period `π`
  let pB : Nat → M := fun k => S.eval img (etherWord (7 * k))
  have hpB : ∀ k, pB (k + 1) = S.mul (pB 1) (pB k) := by
    intro k
    show S.eval img (etherWord (7 * (k + 1))) =
      S.mul (S.eval img (etherWord (7 * 1))) (S.eval img (etherWord (7 * k)))
    rw [show 7 * (k + 1) = 7 * 1 + 7 * k by omega, etherWord_add, eval_append]
  obtain ⟨k0, k1, hk, -, hpk⟩ := pigeonhole_gen S.elems pB (fun _ => S.mem_elems _)
  obtain ⟨π, hπ⟩ : ∃ π, π = k1 - k0 := ⟨_, rfl⟩
  have hper : ∀ a c, k0 ≤ a → pB (a + c * π) = pB a :=
    periodic_tail S.mul (pB 1) pB hpB (by rw [show k0 + π = k1 by omega]; exact hpk.symm)
  have hether : ∀ L, S.eval img (etherWord L) =
      S.mul (pB (L / 7)) (S.eval img (etherWord (L % 7))) := by
    intro L
    show _ = S.mul (S.eval img (etherWord (7 * (L / 7)))) _
    rw [← eval_append, ← etherWord_add, Nat.div_add_mod]
  -- the wedge data at the times `28 π i`, each at its own base
  let v : Nat → List Bool × (M × M) := fun i =>
    wedgeData e S img (e + 28 * (π * i) + 1) (28 * (π * i))
  obtain ⟨i1, i2, hi, -, hv⟩ :=
    pigeonhole_gen (prodList (allLists (e + e)) (prodList S.elems S.elems)) v
      (fun i => mem_prodList (mem_allLists_of_length (by simp [leftWin, rightWin]))
        (mem_prodList (S.mem_elems _) (S.mem_elems _)))
  obtain ⟨Δ, hΔ⟩ : ∃ Δ, Δ = i2 - i1 := ⟨_, rfl⟩
  obtain ⟨c1, hc1⟩ : ∃ c, c = π * i1 := ⟨_, rfl⟩
  obtain ⟨c2, hc2⟩ : ∃ c, c = π * i2 := ⟨_, rfl⟩
  obtain ⟨g, hg⟩ : ∃ g, g = π * Δ := ⟨_, rfl⟩
  have hc : c2 = c1 + g := by
    rw [hc2, hc1, hg, hΔ, ← Nat.mul_add]
    congr 1
    omega
  have hg1 : 1 ≤ g := by rw [hg]; exact Nat.mul_pos (by omega) (by omega)
  have hgπ : (16 * Δ) * π = 16 * g := by rw [hg, Nat.mul_assoc, Nat.mul_comm Δ π]
  -- only now the base
  obtain ⟨N0, hN0⟩ : ∃ N, N = e + 28 * c2 + 1 + k0 + w := ⟨_, rfl⟩
  have hwd : ∀ N, N0 ≤ N →
      wedgeData e S img N (28 * c2) = wedgeData e S img (N + 4 * g) (28 * c1) := by
    intro N hN
    have a2 := wedgeData_indep e S img (e + 28 * c2 + 1) (N - (e + 28 * c2 + 1)) (28 * c2)
      (by omega) (by omega)
    have a1 := wedgeData_indep e S img (e + 28 * c1 + 1) (N + 4 * g - (e + 28 * c1 + 1)) (28 * c1)
      (by omega) (by omega)
    rw [show e + 28 * c2 + 1 + (N - (e + 28 * c2 + 1)) = N by omega] at a2
    rw [show e + 28 * c1 + 1 + (N + 4 * g - (e + 28 * c1 + 1)) = N + 4 * g by omega] at a1
    rw [a2, a1, hc1, hc2]
    exact hv.symm
  have eq : ∀ N, N0 ≤ N →
      jrank w e S img R N (28 * c2) = jrank w e S img R (N + 4 * g) (28 * c1) := by
    intro N hN
    have hw := hwd N hN
    unfold wedgeData at hw
    obtain ⟨hw1, hw2⟩ := Prod.mk.inj hw
    obtain ⟨hw3, hw4⟩ := Prod.mk.inj hw2
    obtain ⟨hl, hr⟩ := List.append_inj hw1 (by simp [leftWin])
    have e1 : clo N (28 * c2) = clo (N + 4 * g) (28 * c1) := by unfold clo; push_cast; omega
    have e2 : chi N (28 * c2) = chi (N + 4 * g) (28 * c1) := by unfold chi; push_cast; omega
    have ecw : centerWin w (cx N (28 * c2)) = centerWin w (cx (N + 4 * g) (28 * c1)) := by
      show centerWin w (fun p => evol (c7cut N) (28 * c2) p) =
        centerWin w (fun p => evol (c7cut (N + 4 * g)) (28 * c1) p)
      rw [centerWin_agree w N (28 * c2) (by omega), centerWin_agree w (N + 4 * g) (28 * c1) (by omega)]
      have : (fun p => evol c7 (28 * c2) p) = (fun p => evol c7 (28 * c1) p) := by
        funext p
        rw [hc, show 28 * (c1 + g) = 28 * c1 + 4 * (7 * g) by omega, evol_c7_period_mul]
      rw [this]
    have emu : S.eval img (spanWord (cx N (28 * c2)) (clo N (28 * c2)) (chi N (28 * c2))) =
        S.eval img (spanWord (cx (N + 4 * g) (28 * c1)) (clo (N + 4 * g) (28 * c1))
          (chi (N + 4 * g) (28 * c1))) := by
      rw [c7cut_span N c2 (by omega), c7cut_span (N + 4 * g) c1 (by omega)]
      simp only [eval_append]
      rw [hw3, hw4, hether (14 * N + 8 - 2 * (28 * c2)),
        hether (14 * (N + 4 * g) + 8 - 2 * (28 * c1))]
      have hq : (14 * (N + 4 * g) + 8 - 2 * (28 * c1)) / 7 =
          (14 * N + 8 - 2 * (28 * c2)) / 7 + (16 * Δ) * π := by omega
      have hr7 : (14 * (N + 4 * g) + 8 - 2 * (28 * c1)) % 7 = (14 * N + 8 - 2 * (28 * c2)) % 7 := by
        omega
      rw [hq, hr7, hper _ _ (by omega)]
    unfold jrank
    rw [emu, hl, hr, ecw, e1, e2]
  have desc : ∀ k, Relation.TransGen r (jrank w e S img R (N0 + (k + 1) * (4 * g)) (28 * c1))
      (jrank w e S img R (N0 + k * (4 * g)) (28 * c1)) := by
    intro k
    rw [show N0 + (k + 1) * (4 * g) = (N0 + k * (4 * g)) + 4 * g by rw [Nat.succ_mul]; omega,
      ← eq (N0 + k * (4 * g)) (by omega)]
    have h := jrank_chain hR (N0 + k * (4 * g)) (28 * c1) (28 * c2 - 28 * c1) (by omega) (by omega)
    rw [show 28 * c1 + (28 * c2 - 28 * c1) = 28 * c2 by omega] at h
    exact h
  exact no_descent hwf.transGen (fun k => jrank w e S img R (N0 + k * (4 * g)) (28 * c1)) desc

/-- **Coupled frame: no ranking through the ends and a recognizable statistic.** For every finite
monoid, every monoid morphism from Boolean words and every well-founded relation `r`, no rank
through (leftmost black position, rightmost black position, image of the whole configuration read
from left to right) moves down along `r` at every step where the center column flips, over all
finite configurations. -/
theorem no_joint_recognizable_ranking {M α : Type} (S : FinMonoid M) (img : Bool → M)
    {r : α → α → Prop} (hwf : WellFounded r) (R : Int → Int → M → α) : ¬ JointRecCert S img r R :=
  fun hR => no_joint_windowed_recognizable_ranking 0 0 S img hwf (fun lo hi _ _ _ x => R lo hi x)
    fun x lo hi h1 h2 h3 h4 h5 => hR x lo hi h1 h2 h3 h4 h5

/-- **Coupled frame, natural-number ranks.** -/
theorem no_joint_recognizable_ranking_nat {M : Type} (S : FinMonoid M) (img : Bool → M)
    (R : Int → Int → M → Nat) : ¬ JointRecCert S img (fun a b => a < b) R :=
  no_joint_recognizable_ranking S img Nat.lt_wfRel.wf R

/-- **The kit two-sided barrier, recovered.** This is
`Rule30ZeroBoundaryBarriers.no_joint_local_ranking`, obtained from
`no_joint_windowed_recognizable_ranking` for the one-element monoid. -/
theorem no_joint_local_ranking_of_recognizable (w e : Nat)
    (R : Int → Int → List Bool → List Bool → List Bool → Nat) : ¬ JointCert w e R :=
  fun hR => no_joint_windowed_recognizable_ranking w e FinMonoid.unit (fun _ => ()) Nat.lt_wfRel.wf
    (fun lo hi c l r _ => R lo hi c l r) fun x lo hi h1 h2 h3 h4 h5 => hR x lo hi h1 h2 h3 h4 h5

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"no_recognizable_ranking", "no_recognizable_ranking_nat", "no_wall_recognizable_ranking", "no_windowed_recognizable_ranking", "no_local_ranking_of_recognizable", "edge_decomp", "sharp_rows_check", "sharp_rows_width", "sharp_rows_survive", "sharp_rows_fourteen", "no_width_bounded_ranking", "no_edge_automaton_ranking", "no_joint_recognizable_ranking", "no_joint_recognizable_ranking_nat", "no_joint_windowed_recognizable_ranking", "no_joint_local_ranking_of_recognizable", "c7cut_span"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.c7cut_span"]["KernelCheck"]
```
