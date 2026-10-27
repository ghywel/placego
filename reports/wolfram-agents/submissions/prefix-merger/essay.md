---
Template: ComputationalEssay
Name: A seven-cell rewrite beside the white wall that merges in two steps, for every tail and every finite cut
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial result on the Rule 30 Prize kit's zero-boundary left half, proved in Lean: the starts 1100011 and 1010101 beside the white wall, followed by the same arbitrary tail, have equal rows from time 2 on, and so do their truncations at every common depth of at least 7; inside the kit's reconstruction Theta, the corresponding free-bit change is confined to depths 1 to 6.
Abstract: For the kit's zero-boundary left half (`Rule30ZeroBoundary.zrow`), consider the starts $1100011\,\tau$ and $1010101\,\tau$, read from the wall outward, with the same arbitrary tail $\tau$ from depth $8$ on. We prove that their rows are equal at time $2$ (`mergePrefix_two`) and so at every later time (`mergePrefix_future`). The same holds for their truncations at any common depth $W \ge 7$ (`mergePrefix_truncate`), which are finitely supported. The depth-$7$ cell is needed: with it white and a white tail, the truncations at depth $6$ do not merge (`mergePrefix_needs_seven`). Inside the kit's reconstruction `Theta`, take free-bit sequences $f$, $g$ that agree from index $1$ on, with $f_1 = f_2 = 1$. Then $\Theta f$ reads this prefix with $a = f_0$ (`theta_prefix`). $\Theta f$ and $\Theta g$ agree at every depth $k \ge 7$ (`theta_first_edit_local`), and their truncations at every $W \ge 7$ merge at time $2$ (`theta_truncate_merge`). The kit's `two_step_shift` already merges the untruncated $\Theta f$ and $\Theta g$; what is added is the localization, which survives a common finite cut. Two reading lemmas are included. Merged rows have the same last black depth, by the kit's `zrow_edge` (`merge_preserves_last_black`). A merger together with the earlier even observations is equivalent to agreement at every even time (`odd_edits_iff_guarded_merge`). Not claimed: a death-time bound, any decision of `Q01`, or anything about the center column.
Keywords: [rule 30, Rule 30 Prize, Q01, zero boundary, Theta, reconstruction, merger, finite support, truncation, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30ZeroBoundary in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean)"]
---

## The question

The kit's open statement `Q01` concerns the left half of rule 30 beside a white wall (`Rule30ZeroBoundary.zrow`): can a finitely supported start keep the cell beside the wall black at every even time? The kit rebuilds every such start from its free bits by `Theta`. Two different free-bit sequences give different starts, but their histories can *merge*: once two rows are equal, they stay equal. When a merger happens, which cells were really different? And does the merger survive when both starts are cut to a common finite width, as every finitely supported start must be? This essay gives an exact answer for one such merger: a rewrite of the seven cells nearest the wall.

## Two starts that merge, whatever follows them

One step of the zero-boundary left half, on depths `1, 2, …` (the wall at depth `0` is white):

```wl
zstep[w_] := With[{p = Join[{0}, w, {0, 0}]}, Table[BitXor[p[[k + 2]], BitOr[p[[k + 1]], p[[k]]]], {k, 1, Length[w] + 1}]];
startA[tail_] := Join[{1, 1, 0, 0, 0, 1, 1}, tail]; startB[tail_] := Join[{1, 0, 1, 0, 1, 0, 1}, tail];
tails = {{}, {1}, {0, 1, 1, 0, 1}, {1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1}};
Table[{Nest[zstep, startA[tl], 1] === Nest[zstep, startB[tl], 1], Nest[zstep, startA[tl], 2] === Nest[zstep, startB[tl], 2]}, {tl, tails}]
```

For each tail the rows differ at time `1` and agree at time `2`. Dropping the black cell at depth `7`, with nothing after it, they no longer agree:

```wl
{Nest[zstep, {1, 1, 0, 0, 0, 1}, 2], Nest[zstep, {1, 0, 1, 0, 1, 0}, 2]}
```

## The theorems

- **The rewrite** (`mergePrefix_two`, `mergePrefix_future`). For every tail `τ : ℕ → Bool`, the starts `mergePrefix false τ` (depths `1 .. 7` read `1 1 0 0 0 1 1`) and `mergePrefix true τ` (`1 0 1 0 1 0 1`), with `τ` from depth `8` on, have equal rows at time `2`, and therefore at every time `2 + t`.
- **Finite cuts** (`mergePrefix_truncate`, `mergePrefix_truncate_fin`). For every `W ≥ 7`, the truncations of the two starts at depth `W` are finitely supported and have equal rows at time `2`.
- **The depth-7 cell is needed** (`mergePrefix_needs_seven`). With depth `7` white and a white tail, the truncations at depth `6` differ at time `2`.
- **Inside `Theta`** (`theta_prefix`, `theta_first_edit_local`, `theta_truncate_merge`). Take free-bit sequences `f` and `g` that agree from index `1` on, with `f 1 = f 2 = true`. Then `Theta f` reads the prefix with `a = f 0` at depths `1 .. 7`, and `Theta f` and `Theta g` agree at every depth `k ≥ 7`. Their truncations at every common depth `W ≥ 7` have equal rows at time `2`.
- **Reading a merger** (`trace_tail_iff_row`, `merge_preserves_last_black`, `odd_edits_iff_guarded_merge`). Rows equal at time `T` are the same as equal column `1` from `T` on. Merged starts have their last black cell at the same depth. Agreement at every even time and every time from `T` on is the same as a merger at `T` together with the earlier even observations.

## The idea of the proof

1. **Locality.** A cell at depth `k` and time `2` reads the start at depths `k - 2 .. k + 2`. From depth `10` on the two starts read only the common tail, so their rows agree there (`step_local`). Depths `0 .. 9` read the start up to depth `11`: the prefix and the first four tail cells. A Boolean case split on those four cells settles them.
2. **Cuts.** For `W ≥ 7` the truncation of `mergePrefix a τ` is `mergePrefix a` with the cut tail, at every depth `k ≥ 1` (`truncate_mergePrefix`). Depth `0` is the wall, which no row reads (`zrow_congr_pos`). So the cut starts are again an instance of step 1.
3. **Inside `Theta`.** `Theta f` is the kit's reconstruction `recon (alt f) · 0`, and `alt f` differs from `alt g` only at time `1`. From time `2` on the reconstructions agree at every depth (`recon_local`). At times `0` and `1` the depths `7` and `8` read `alt` only up to time `8`, where the window is fixed by `f 0` and `f 3`, and a finite check shows they do not depend on `f 0`. The kit's recursion `recon_two` then carries agreement at two consecutive depths outward to every depth.
4. **Reading.** `trace_tail_iff_row` is the kit's `zrow_det` and `zrow_shift`. `merge_preserves_last_black` compares the two edges given by the kit's `zrow_edge`.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit

/-!
# Rule 30 beside a white wall: a seven-cell prefix rewrite that merges after two steps, for every tail

The zero-boundary left half (`Rule30ZeroBoundary.zrow`): depth `0` is a white wall, and depth `k ≥ 1`
updates by rule 30. Two starts that differ only in the seven cells next to the wall,

  `1 1 0 0 0 1 1` and `1 0 1 0 1 0 1` (read from the wall outward, depths `1 .. 7`),

followed by the **same** arbitrary tail at depths `8, 9, …`, have equal rows at time `2`
(`mergePrefix_two`), and therefore equal rows at every later time (`mergePrefix_future`). The same
holds for their truncations at any common depth `W ≥ 7` (`mergePrefix_truncate`), so finitely
supported starts of every width `W ≥ 7` merge. The depth-7 cell is needed: with it white and the
tail white, the two starts do not merge at time `2` (`mergePrefix_needs_seven`).

**Inside the kit's reconstruction.** For free-bit sequences `f`, `g` that agree from index `1` on, with
bits `1` and `2` black, `Theta f` reads the rewrite's prefix at depths `1 .. 7` with `a = f 0`
(`theta_prefix`), `Theta f` and `Theta g` agree at every depth `k ≥ 7` (`theta_first_edit_local`), and
their truncations at every common depth `W ≥ 7` merge at time `2` (`theta_truncate_merge`). The
untruncated merger is the kit's `two_step_shift`; what is added is the localization, which survives a
common finite cut.

General facts used to read such mergers (`trace_tail_iff_row`, `merge_preserves_last_black`): two
starts whose rows agree at time `T` have the same column `1` from `T` on and conversely; and rows
that merge have their last black cells at the same depth.

Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). The equal-width statement is
a short application of the kit's `zrow_det` and `zrow_edge`. Nothing here bounds a death time or
decides `Q01`.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Ruliology.CellularAutomata.Rule30ZeroBoundary

/-- The prefix `a`-word at depths `1 .. 7` and a common tail from depth `8` on. With `a = false`
the prefix reads `1 1 0 0 0 1 1`, with `a = true` it reads `1 0 1 0 1 0 1`. -/
def mergePrefix (a : Bool) (tail : Nat → Bool) : Nat → Bool
  | 0 => false
  | 1 => true
  | 2 => !a
  | 3 => a
  | 4 => false
  | 5 => a
  | 6 => !a
  | 7 => true
  | k + 8 => tail k

theorem zrow_zero_eq (L : Nat → Bool) (k : Nat) (hk : 1 ≤ k) : zrow L 0 k = L k := by
  match k, hk with
  | j + 1, _ => rfl

theorem zrow_succ_eq (L : Nat → Bool) (t k : Nat) (hk : 1 ≤ k) :
    zrow L (t + 1) k = xor (zrow L t (k + 1)) (zrow L t k || zrow L t (k - 1)) := by
  match k, hk with
  | j + 1, _ => rfl

/-- One step of locality: rows that agree on depths `a .. b` (with `a ≥ 1`) agree one step later
on depths `a + 1 .. b - 1`. -/
theorem step_local {L M : Nat → Bool} {t a b : Nat} (ha : 1 ≤ a)
    (h : ∀ i, a ≤ i → i ≤ b → zrow L t i = zrow M t i) :
    ∀ i, a + 1 ≤ i → i + 1 ≤ b → zrow L (t + 1) i = zrow M (t + 1) i := by
  intro i h1 h2
  rw [zrow_succ_eq L t i (by omega), zrow_succ_eq M t i (by omega),
    h (i + 1) (by omega) (by omega), h i (by omega) (by omega), h (i - 1) (by omega) (by omega)]

theorem mergePrefix_tail (a : Bool) (tail : Nat → Bool) (j : Nat) :
    mergePrefix a tail (j + 8) = tail j := rfl

/-- **The two starts merge after two steps, for every common tail.** -/
theorem mergePrefix_two (tail : Nat → Bool) :
    zrow (mergePrefix false tail) 2 = zrow (mergePrefix true tail) 2 := by
  funext k
  -- far from the wall only the common tail matters
  by_cases hk : 10 ≤ k
  · have h0 : ∀ i, 8 ≤ i → i ≤ k + 2 →
        zrow (mergePrefix false tail) 0 i = zrow (mergePrefix true tail) 0 i := by
      intro i hi _
      obtain ⟨j, rfl⟩ : ∃ j, i = j + 8 := ⟨i - 8, by omega⟩
      rw [zrow_zero_eq _ _ (by omega), zrow_zero_eq _ _ (by omega)]
      rfl
    have h1 := step_local (t := 0) (a := 8) (b := k + 2) (by omega) h0
    exact step_local (t := 1) (a := 9) (b := k + 1) (by omega) (fun i ha hb => h1 i ha (by omega))
      k (by omega) (by omega)
  · -- near the wall: depths 0 .. 9 read the start up to depth 11, i.e. the tail cells 0 .. 3
    have e : k = 0 ∨ k = 1 ∨ k = 2 ∨ k = 3 ∨ k = 4 ∨ k = 5 ∨ k = 6 ∨ k = 7 ∨ k = 8 ∨ k = 9 := by
      omega
    rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    · simp [zrow, mergePrefix] <;>
      cases tail 0 <;> cases tail 1 <;> cases tail 2 <;> cases tail 3 <;> simp

/-- After the merger the two starts have the same rows for ever. -/
theorem mergePrefix_future (tail : Nat → Bool) (t : Nat) :
    zrow (mergePrefix false tail) (2 + t) = zrow (mergePrefix true tail) (2 + t) := by
  funext k
  rw [zrow_shift, zrow_shift, mergePrefix_two]

theorem truncate_mergePrefix (a : Bool) (tail : Nat → Bool) (W : Nat) (hW : 7 ≤ W) (k : Nat)
    (hk : 1 ≤ k) :
    truncate (mergePrefix a tail) W k = mergePrefix a (fun j => tail j && decide (j + 8 ≤ W)) k := by
  match k, hk with
  | 1, _ => simp [truncate, mergePrefix]; omega
  | 2, _ => simp [truncate, mergePrefix]; omega
  | 3, _ => simp [truncate, mergePrefix]; omega
  | 4, _ => simp [truncate, mergePrefix]
  | 5, _ => simp [truncate, mergePrefix]; omega
  | 6, _ => simp [truncate, mergePrefix]; omega
  | 7, _ => simp [truncate, mergePrefix]; omega
  | j + 8, _ => simp [truncate, mergePrefix]

theorem zrow_congr_pos {L M : Nat → Bool} (h : ∀ k, 1 ≤ k → L k = M k) : zrow L = zrow M := by
  funext t k
  induction t generalizing k with
  | zero =>
    cases k with
    | zero => rfl
    | succ j => exact h (j + 1) (by omega)
  | succ t ih =>
    cases k with
    | zero => rfl
    | succ j => simp only [zrow]; rw [ih (j + 1 + 1), ih (j + 1), ih (j + 1 - 1)]

/-- **Finite starts of every width `W ≥ 7` merge too.** The truncations at a common depth `W ≥ 7`
merge at time `2`. -/
theorem mergePrefix_truncate (tail : Nat → Bool) (W : Nat) (hW : 7 ≤ W) :
    zrow (truncate (mergePrefix false tail) W) 2 = zrow (truncate (mergePrefix true tail) W) 2 := by
  rw [zrow_congr_pos (truncate_mergePrefix false tail W hW),
    zrow_congr_pos (truncate_mergePrefix true tail W hW)]
  exact mergePrefix_two _

/-- The truncated starts are finitely supported. -/
theorem mergePrefix_truncate_fin (a : Bool) (tail : Nat → Bool) (W : Nat) :
    FinSupp (truncate (mergePrefix a tail) W) := ⟨W, truncate_fin _ W⟩

/-- **The depth-7 cell is needed.** With depth `7` white and a white tail the two six-cell starts
do not merge at time `2`. -/
theorem mergePrefix_needs_seven :
    zrow (truncate (mergePrefix false (fun _ => false)) 6) 2 ≠
      zrow (truncate (mergePrefix true (fun _ => false)) 6) 2 := by
  intro h
  have := congrFun h 8
  revert this
  decide

/-! ### Reading a merger -/

/-- Rows equal at time `T` give equal column `1` from `T` on, and conversely. -/
theorem trace_tail_iff_row (L M : Nat → Bool) (T : Nat) :
    (∀ t, T ≤ t → zrow L t 1 = zrow M t 1) ↔ zrow L T = zrow M T := by
  constructor
  · intro h
    funext k
    exact zrow_det L M k T (fun i _ => h (T + i) (by omega))
  · intro h t ht
    obtain ⟨u, rfl⟩ : ∃ u, t = T + u := ⟨t - T, by omega⟩
    rw [zrow_shift L T u 1, zrow_shift M T u 1, h]

/-- The rightmost black cell of a start. -/
def LastBlack (L : Nat → Bool) (m : Nat) : Prop := 1 ≤ m ∧ L m = true ∧ ∀ k, m < k → L k = false

/-- Starts whose rows merge have their last black cells at the same depth. -/
theorem merge_preserves_last_black (L M : Nat → Bool) (m n T : Nat)
    (hL : LastBlack L m) (hM : LastBlack M n) (hmerge : zrow L T = zrow M T) : m = n := by
  have eL := zrow_edge hL.1 hL.2.1 hL.2.2 T
  have eM := zrow_edge hM.1 hM.2.1 hM.2.2 T
  apply Classical.byContradiction
  intro hne
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · have a := eL.2 (n + T) (by omega)
    have b := eM.1
    rw [hmerge] at a
    rw [a] at b
    exact Bool.false_ne_true b
  · have a := eM.2 (m + T) (by omega)
    have b := eL.1
    rw [hmerge, a] at b
    exact Bool.false_ne_true b

/-- **Guarded merge.** Two starts have equal column `1` at every time from `T` on and at every
earlier even time exactly when their rows agree at time `T` and their earlier even observations
agree. A common future alone does not give the earlier checks. -/
theorem odd_edits_iff_guarded_merge (L M : Nat → Bool) (T : Nat) :
    (∀ t, T ≤ t ∨ t % 2 = 0 → zrow L t 1 = zrow M t 1) ↔
      (zrow L T = zrow M T ∧ ∀ t, t < T → t % 2 = 0 → zrow L t 1 = zrow M t 1) := by
  constructor
  · intro h
    exact ⟨(trace_tail_iff_row L M T).1 (fun t ht => h t (Or.inl ht)),
      fun t _ he => h t (Or.inr he)⟩
  · rintro ⟨hrow, hearly⟩ t ht
    by_cases hT : T ≤ t
    · exact (trace_tail_iff_row L M T).2 hrow t hT
    · rcases ht with ht | ht
      · exact absurd ht hT
      · exact hearly t (by omega) ht

/-! ### The rewrite inside the kit's reconstruction `Theta` -/

/-- The column-`1` window of `alt f` up to time `8`, with `f 1 = f 2 = true`. -/
def win (c e : Bool) (t : Nat) : Bool := if t = 1 then c else if t = 7 then e else true

theorem alt_eq_win (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) (t : Nat) (ht : t ≤ 8) :
    alt f t = win (f 0) (f 3) t := by
  have e : t = 0 ∨ t = 1 ∨ t = 2 ∨ t = 3 ∨ t = 4 ∨ t = 5 ∨ t = 6 ∨ t = 7 ∨ t = 8 := by omega
  rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> simp [alt, win, h1, h2]

theorem recon_win (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) (k t : Nat)
    (hkt : t + k ≤ 9) : recon (alt f) k t = recon (win (f 0) (f 3)) k t :=
  recon_local k t (fun j hj => alt_eq_win f h1 h2 (t + j) (by omega))

/-- **The prefix of `Theta f`.** With free bits `1` and `2` black, `Theta f` reads the rewrite's
prefix at depths `1 .. 7`: `1 1 0 0 0 1 1` when `f 0` is white, `1 0 1 0 1 0 1` when it is black. -/
theorem theta_prefix (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) :
    ∀ k, 1 ≤ k → Theta f k = mergePrefix (f 0) (fun j => Theta f (j + 8)) k := by
  intro k hk
  by_cases h8 : 8 ≤ k
  · obtain ⟨j, rfl⟩ : ∃ j, k = j + 8 := ⟨k - 8, by omega⟩
    rfl
  · show recon (alt f) k 0 = _
    rw [recon_win f h1 h2 k 0 (by omega)]
    have e : k = 1 ∨ k = 2 ∨ k = 3 ∨ k = 4 ∨ k = 5 ∨ k = 6 ∨ k = 7 := by omega
    rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      cases f 0 <;> cases f 3 <;> simp only [mergePrefix] <;> decide

/-- **Changing free bit `0` changes only depths `1 .. 6`.** If two free-bit sequences agree from
index `1` on and their bits `1` and `2` are black, their reconstructed starts agree at every depth
`k ≥ 7`. -/
theorem theta_first_edit_local (f g : Nat → Bool) (hrest : ∀ j, 1 ≤ j → f j = g j)
    (h1 : f 1 = true) (h2 : f 2 = true) : ∀ k, 7 ≤ k → Theta f k = Theta g k := by
  have g1 : g 1 = true := by rw [← hrest 1 (by omega)]; exact h1
  have g2 : g 2 = true := by rw [← hrest 2 (by omega)]; exact h2
  have late : ∀ k t, 2 ≤ t → recon (alt f) k t = recon (alt g) k t := by
    intro k t ht
    apply recon_local k t
    intro j _
    simp only [alt]
    split
    · rfl
    · exact hrest _ (by omega)
  have base : ∀ k t, 7 ≤ k → k ≤ 8 → t ≤ 1 → recon (alt f) k t = recon (alt g) k t := by
    intro k t hk7 hk8 ht
    rw [recon_win f h1 h2 k t (by omega), recon_win g g1 g2 k t (by omega), ← hrest 3 (by omega)]
    have ek : k = 7 ∨ k = 8 := by omega
    have et : t = 0 ∨ t = 1 := by omega
    rcases ek with rfl | rfl <;> rcases et with rfl | rfl <;>
      cases f 0 <;> cases g 0 <;> cases f 3 <;> decide
  have step : ∀ m,
      (recon (alt f) (7 + m) 0 = recon (alt g) (7 + m) 0 ∧
        recon (alt f) (7 + m + 1) 0 = recon (alt g) (7 + m + 1) 0 ∧
        recon (alt f) (7 + m) 1 = recon (alt g) (7 + m) 1 ∧
        recon (alt f) (7 + m + 1) 1 = recon (alt g) (7 + m + 1) 1) := by
    intro m
    induction m with
    | zero => exact ⟨base 7 0 (by omega) (by omega) (by omega), base 8 0 (by omega) (by omega) (by omega),
        base 7 1 (by omega) (by omega) (by omega), base 8 1 (by omega) (by omega) (by omega)⟩
    | succ n ih =>
      obtain ⟨a0, b0, a1, b1⟩ := ih
      have e : 7 + (n + 1) = 7 + n + 1 := by omega
      have e2 : 7 + n + 1 + 1 = (7 + n) + 2 := by omega
      rw [e, e2]
      refine ⟨b0, ?_, b1, ?_⟩
      · rw [recon_two, recon_two, b1, b0, a0]
      · rw [recon_two, recon_two, late (7 + n + 1) 2 (by omega), b1, a1]
  intro k hk
  obtain ⟨m, rfl⟩ : ∃ m, k = 7 + m := ⟨k - 7, by omega⟩
  exact (step m).1

/-- **Common truncations of `Theta` starts merge.** If two free-bit sequences agree from index `1`
on and their bits `1` and `2` are black, then for every common depth `W ≥ 7` the finitely supported
truncations of their reconstructed starts have equal rows at time `2`. -/
theorem theta_truncate_merge (f g : Nat → Bool) (hrest : ∀ j, 1 ≤ j → f j = g j)
    (h1 : f 1 = true) (h2 : f 2 = true) (W : Nat) (hW : 7 ≤ W) :
    zrow (truncate (Theta f) W) 2 = zrow (truncate (Theta g) W) 2 := by
  have g1 : g 1 = true := by rw [← hrest 1 (by omega)]; exact h1
  have g2 : g 2 = true := by rw [← hrest 2 (by omega)]; exact h2
  have htail : (fun j => Theta f (j + 8)) = (fun j => Theta g (j + 8)) :=
    funext fun j => theta_first_edit_local f g hrest h1 h2 (j + 8) (by omega)
  have tf : ∀ k, 1 ≤ k → truncate (Theta f) W k =
      truncate (mergePrefix (f 0) (fun j => Theta f (j + 8))) W k := by
    intro k hk; simp only [truncate]; rw [theta_prefix f h1 h2 k hk]
  have tg : ∀ k, 1 ≤ k → truncate (Theta g) W k =
      truncate (mergePrefix (g 0) (fun j => Theta f (j + 8))) W k := by
    intro k hk; simp only [truncate]; rw [theta_prefix g g1 g2 k hk, ← htail]
  rw [zrow_congr_pos tf, zrow_congr_pos tg]
  cases hf0 : f 0 <;> cases hg0 : g 0
  · rfl
  · exact mergePrefix_truncate _ W hW
  · exact (mergePrefix_truncate _ W hW).symm
  · rfl

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
thm = rule30Submission["Rule30Submission.theta_truncate_merge"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"mergePrefix_two", "mergePrefix_truncate", "mergePrefix_needs_seven", "theta_first_edit_local", "theta_truncate_merge", "merge_preserves_last_black", "odd_edits_iff_guarded_merge"}}]
```

The axioms of the headline `theta_truncate_merge` are standard ones only (the checker verifies all eleven headlines and replays the whole module):

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing decides `Q01`, bounds a death time, or concerns the center column. `FinSupp (Theta f)` is the open hypothesis of `Q01`; nothing here instantiates it.
- The untruncated merger of `Theta f` and `Theta g` is the kit's `two_step_shift`. Equal last black depth is a short application of `zrow_det` and `zrow_edge`. What this module adds is the explicit seven-cell rewrite, its survival under every common cut `W ≥ 7`, and its localization inside `Theta`.
- `W` is a cut bound; the actually occupied width of a truncated start may be smaller.
- The depth-7 countercontrol shows only that this rewrite needs depth `7`; it says nothing about other six-cell rewrites.
- The exact rewrite was not found in the kit's catalog or the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

The merger turned up in a census of sideways rows on the Apple M5. GPT (OpenAI) proved the two-step merger of this seven-cell pair by hand (GC1930), and Claude (Anthropic) read it independently (L996). GPT then wrote the statement chain for this module, separating the general reconstruction facts from the finite-cut rewrite (GC1965). Claude formalized it. The record is at github.com/ghywel/placego, reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md and reports/wolfram-agents/submissions/prefix-merger.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30ZeroBoundary.zrow`, `truncate`, `Theta`, `recon`, `recon_local`, `recon_two`, `zrow_det`, `zrow_shift`, `zrow_edge`, `two_step_shift`.
