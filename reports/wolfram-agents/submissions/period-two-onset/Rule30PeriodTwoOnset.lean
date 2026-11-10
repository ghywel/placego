module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Jen

/-!
# Period 2: the column-1 words of widths 5 and 6 from two ticks on, for every history

`Rule30PeriodTwoWidth5.col1_constraints` and `Rule30PeriodTwoWidth6.col1_constraints` say: if the
center column of rule 30 from a single black cell is white, black, white, … from a time `T`, then
from some later time on, column `1` read at consecutive white times never spells a word of their
lists `col1Forbidden`. This module gives the later time, `T + 2`, and drops the single seed: the
same words are excluded for every space-time history `H : Nat → Int → Bool` that obeys rule 30 at
the columns `1..b` (`Obeys`), whatever its other columns do, finite or not.

* `win_dstep`: if column `0` is white at the tick `s` and black at `s + 1`, the window of columns
  `1..b` at `s + 2` is the double step `dstep` of the window at `s`, whose only other inputs are the
  two cells of column `b + 1` at `s` and `s + 1`.
* `img5_length`, `img6_length`: one double step takes the `32` windows of width `5` onto `20`
  windows, and the `64` of width `6` onto `38` (`img`). `img5_closed`, `img6_closed`: the double
  step takes these back into themselves, whatever column `b + 1` does.
* `no_word5`, `no_word6`: if column `0` alternates white, black on the `2 m` ticks
  `s, s + 1, …, s + 2 m - 1`, then column `1` at the ticks `s + 2, s + 4, …, s + 2 m` does not read
  a word of `forbidden5` (resp. `forbidden6`) of length `m`. These are the kit's lists
  `col1Forbidden`. `no_short6`: at width `6`, the kit's word `1010100001` can be shortened to
  `101010000`.
* `onset5`, `onset6`: so if column `0` alternates from `T` on, no word of the lists is read from
  any white time `t ≥ T + 2`. `col1_constraints5`, `col1_constraints6` are the kit's statements
  for the single seed with `T' = T + 2`.
* `free_bit5`, `free_bit6`: column `-1` at the white times is the complement of column `1` when
  the rule holds at column `0` and the next tick is black, so it never reads a complemented word;
  this needs the alternation on two more ticks. `free_bit_constraints5`, `free_bit_constraints6`
  are the kit's statements for the single seed with `T' = T + 2`.

The method is the kit's (`Rule30GateTrap`, `Rule30GateTrapWords`): the windows that can have read
the first `k` samples of a word form a layer, the double step for every value of column `b + 1`
takes each layer into the next, and the last layer is empty (`run`, `excludes`). Here the first
layer is the image of all windows, so it needs no entry time. The relation forgets the columns
beyond `b + 1`, so the onset `T + 2` is not claimed to be the earliest for actual configurations.
Nothing here excludes period 2.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30PeriodTwoOnset

open Rule30Jen

/-! ## Histories and windows -/

/-- `H` obeys rule 30 at column `j`, at every tick. -/
def ObeysAt (H : Nat → Int → Bool) (j : Int) : Prop :=
  ∀ s, H (s + 1) j = rule (H s (j - 1)) (H s j) (H s (j + 1))

/-- `H` obeys rule 30 at the columns `1..b`. -/
def Obeys (b : Nat) (H : Nat → Int → Bool) : Prop :=
  ∀ j : Int, 1 ≤ j → j ≤ b → ObeysAt H j

/-- Rule 30 from a single black cell obeys rule 30 at every column. -/
theorem cell_obeysAt (j : Int) : ObeysAt cell j := fun _ => rfl

theorem cell_obeys (b : Nat) : Obeys b cell := fun j _ _ => cell_obeysAt j

/-- The cells of the columns `a, a + 1, …, a + n - 1` at the tick `s`. -/
def seg (H : Nat → Int → Bool) (s : Nat) (a : Int) : Nat → List Bool
  | 0 => []
  | n + 1 => H s a :: seg H s (a + 1) n

theorem length_seg (H : Nat → Int → Bool) (s : Nat) : ∀ (a : Int) (n : Nat), (seg H s a n).length = n
  | _, 0 => rfl
  | a, n + 1 => by rw [seg, List.length_cons, length_seg H s (a + 1) n]

/-- One tick of rule 30 on a window, with the cell `l` on its left and the cell `r` on its right. -/
def step (l r : Bool) : List Bool → List Bool
  | [] => []
  | [x] => [rule l x r]
  | x :: y :: z => rule l x y :: step x r (y :: z)

/-- A window obeying the rule moves by `step`, with its two outer cells as inputs. -/
theorem seg_step (H : Nat → Int → Bool) (s : Nat) : ∀ (n : Nat) (a : Int),
    (∀ j : Int, a ≤ j → j < a + n → ObeysAt H j) →
    seg H (s + 1) a n = step (H s (a - 1)) (H s (a + n)) (seg H s a n) := by
  intro n
  induction n with
  | zero => intro a _; rfl
  | succ n ih =>
    intro a h
    cases n with
    | zero =>
      show [H (s + 1) a] = [rule (H s (a - 1)) (H s a) (H s (a + ((0 + 1 : Nat) : Int)))]
      rw [h a (Int.le_refl a) (by omega) s, show a + ((0 + 1 : Nat) : Int) = a + 1 by omega]
    | succ m =>
      have e := ih (a + 1) (fun j h1 h2 => h j (by omega) (by omega))
      rw [show a + 1 - 1 = a by omega,
        show a + 1 + ((m + 1 : Nat) : Int) = a + ((m + 1 + 1 : Nat) : Int) by omega] at e
      show H (s + 1) a :: seg H (s + 1) (a + 1) (m + 1) =
        rule (H s (a - 1)) (H s a) (H s (a + 1)) ::
          step (H s a) (H s (a + ((m + 1 + 1 : Nat) : Int))) (seg H s (a + 1) (m + 1))
      rw [e, h a (Int.le_refl a) (by omega) s]

/-- Two ticks from a white tick of column `0`: the left inputs are white, then black, and `r₁`, `r₂`
are the cells of column `b + 1`. -/
def dstep (r₁ r₂ : Bool) (x : List Bool) : List Bool := step true r₂ (step false r₁ x)

/-- **The double step.** If column `0` is white at `s` and black at `s + 1`, the window of the
columns `1..b` at `s + 2` is the double step of the window at `s`. -/
theorem win_dstep {b : Nat} {H : Nat → Int → Bool} (hH : Obeys b H) {s : Nat}
    (h0 : H s 0 = false) (h1 : H (s + 1) 0 = true) :
    seg H (s + 2) 1 b = dstep (H s (1 + b)) (H (s + 1) (1 + b)) (seg H s 1 b) := by
  have hO : ∀ j : Int, 1 ≤ j → j < 1 + b → ObeysAt H j := fun j hj1 hj2 => hH j hj1 (by omega)
  show seg H (s + 1 + 1) 1 b = _
  rw [seg_step H (s + 1) b 1 hO, seg_step H s b 1 hO, show (1 : Int) - 1 = 0 by decide, h0, h1]
  rfl

/-! ## Finite sets of windows -/

/-- The four windows one double step can reach. -/
def succs (x : List Bool) : List (List Bool) :=
  [dstep false false x, dstep false true x, dstep true false x, dstep true true x]

theorem dstep_mem_succs (r₁ r₂ : Bool) (x : List Bool) : dstep r₁ r₂ x ∈ succs x := by
  cases r₁ <;> cases r₂ <;> simp [succs]

/-- A list of windows without repeats. -/
def nub : List (List Bool) → List (List Bool)
  | [] => []
  | x :: l => if x ∈ l then nub l else x :: nub l

theorem mem_nub {y : List Bool} : ∀ {l : List (List Bool)}, y ∈ nub l ↔ y ∈ l
  | [] => Iff.rfl
  | x :: l => by
    by_cases hx : x ∈ l
    · rw [nub, ite_eq_left hx, mem_nub, List.mem_cons]
      exact ⟨Or.inr, fun h => h.elim (fun e => e ▸ hx) id⟩
    · rw [nub, ite_eq_right hx, List.mem_cons, List.mem_cons, mem_nub]

/-- The windows of width `b` that one double step reaches. -/
def img (b : Nat) : List (List Bool) := nub ((allLists b).flatMap succs)

theorem mem_img {b : Nat} {x : List Bool} (hx : x.length = b) (r₁ r₂ : Bool) :
    dstep r₁ r₂ x ∈ img b := by
  rw [img, mem_nub, List.mem_flatMap]
  exact ⟨x, hx ▸ mem_allLists x, dstep_mem_succs r₁ r₂ x⟩

/-- `S` is closed under the double step, for every value of column `b + 1`. -/
def closedB (S : List (List Bool)) : Bool := S.all fun x => (succs x).all fun y => decide (y ∈ S)

theorem img5_length : (img 5).length = 20 := by decide +kernel
theorem img6_length : (img 6).length = 38 := by decide +kernel

/-- The `20` windows of width `5` are closed under the double step. -/
theorem img5_closed : closedB (img 5) = true := by decide +kernel

/-- The `38` windows of width `6` are closed under the double step. -/
theorem img6_closed : closedB (img 6) = true := by decide +kernel

/-! ## Words -/

/-- The windows of `S` whose column-`1` cell is `c`. -/
def layer (c : Bool) (S : List (List Bool)) : List (List Bool) := S.filter fun x => x.headD false == c

/-- The windows that a window of `L` can reach while column `1` reads the samples of `w`, one per
double step. -/
def run : List (List Bool) → List Bool → List (List Bool)
  | L, [] => L
  | L, c :: w => run (nub (layer c (L.flatMap succs))) w

/-- No window of `S` begins a reading of `w`. -/
def excludes (S : List (List Bool)) : List Bool → Bool
  | [] => false
  | c :: w => (run (layer c S) w).isEmpty

theorem headD_seg (H : Nat → Int → Bool) (s : Nat) (a : Int) (n : Nat) :
    (seg H s a (n + 1)).headD false = H s a := rfl

theorem mem_run {b : Nat} (hb : 0 < b) {H : Nat → Int → Bool} (hH : Obeys b H) :
    ∀ (w : List Bool) (L : List (List Bool)) (s : Nat), seg H s 1 b ∈ L →
      (∀ i, i < 2 * w.length → H (s + i) 0 = (i % 2 == 1)) →
      (∀ i, i < w.length → H (s + 2 + 2 * i) 1 = w.getD i false) →
      seg H (s + 2 * w.length) 1 b ∈ run L w
  | [], L, s, hL, _, _ => hL
  | c :: w, L, s, hL, hc, hr => by
    have h0 : H s 0 = false := hc 0 (by simp)
    have h1 : H (s + 1) 0 = true := hc 1 (by simp; omega)
    have hm : seg H (s + 2) 1 b ∈ nub (layer c (L.flatMap succs)) := by
      rw [mem_nub, layer, List.mem_filter, List.mem_flatMap, win_dstep hH h0 h1]
      refine ⟨⟨_, hL, dstep_mem_succs _ _ _⟩, ?_⟩
      rw [← win_dstep hH h0 h1]
      obtain ⟨n, rfl⟩ : ∃ n, b = n + 1 := ⟨b - 1, by omega⟩
      rw [headD_seg]
      have := hr 0 (by simp)
      rw [show s + 2 + 2 * 0 = s + 2 by omega] at this
      rw [this]; simp
    have := mem_run hb hH w _ (s + 2) hm
      (fun i hi => by
        have := hc (i + 2) (by simp at hi ⊢; omega)
        rwa [show s + (i + 2) = s + 2 + i by omega, show (i + 2) % 2 = i % 2 by omega] at this)
      (fun i hi => by
        have := hr (i + 1) (by simp; omega)
        rwa [show s + 2 + 2 * (i + 1) = s + 2 + 2 + 2 * i by omega] at this)
    rwa [List.length_cons, show s + 2 * (w.length + 1) = s + 2 + 2 * w.length by omega]

/-- A word that `img b` excludes is not read by column `1` at the ticks `s + 2, s + 4, …` when
column `0` alternates on the ticks `s, …, s + 2 m - 1`. -/
theorem no_word {b : Nat} (hb : 0 < b) {H : Nat → Int → Bool} (hH : Obeys b H) {w : List Bool}
    (hw : excludes (img b) w = true) (s : Nat)
    (hc : ∀ i, i < 2 * w.length → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < w.length → H (s + 2 + 2 * i) 1 = w.getD i false := by
  intro hr
  match w, hw, hc, hr with
  | c :: w, hw, hc, hr =>
    have h0 : H s 0 = false := hc 0 (by simp)
    have h1 : H (s + 1) 0 = true := hc 1 (by simp; omega)
    have hm : seg H (s + 2) 1 b ∈ layer c (img b) := by
      rw [layer, List.mem_filter, win_dstep hH h0 h1]
      refine ⟨mem_img (length_seg H s 1 b) _ _, ?_⟩
      rw [← win_dstep hH h0 h1]
      obtain ⟨n, rfl⟩ : ∃ n, b = n + 1 := ⟨b - 1, by omega⟩
      rw [headD_seg]
      have := hr 0 (by simp)
      rw [show s + 2 + 2 * 0 = s + 2 by omega] at this
      rw [this]; simp
    have hrun := mem_run hb hH w _ (s + 2) hm
      (fun i hi => by
        have := hc (i + 2) (by simp at hi ⊢; omega)
        rwa [show s + (i + 2) = s + 2 + i by omega, show (i + 2) % 2 = i % 2 by omega] at this)
      (fun i hi => by
        have := hr (i + 1) (by simp; omega)
        rwa [show s + 2 + 2 * (i + 1) = s + 2 + 2 + 2 * i by omega] at this)
    rw [excludes, List.isEmpty_iff] at hw
    rw [hw] at hrun
    exact List.not_mem_nil hrun

/-! ## The words of widths 5 and 6 -/

/-- The column-`1` words of `Rule30PeriodTwoWidth5.col1Forbidden`: `11`, `00000`, `100101`,
`10010001`. -/
def forbidden5 : List (List Bool) := [[true, true], [false, false, false, false, false],
  [true, false, false, true, false, true], [true, false, false, true, false, false, false, true]]

/-- The column-`1` words of `Rule30PeriodTwoWidth6.col1Forbidden`: those of width `5` and
`101001`, `1010100001`, `1010001001`, `10010000101`, `1001000010001`. -/
def forbidden6 : List (List Bool) := [[true, true], [false, false, false, false, false],
  [true, false, false, true, false, true], [true, false, false, true, false, false, false, true],
  [true, false, true, false, false, true], [true, false, true, false, true, false, false, false, false, true],
  [true, false, true, false, false, false, true, false, false, true],
  [true, false, false, true, false, false, false, false, true, false, true],
  [true, false, false, true, false, false, false, false, true, false, false, false, true]]

/-- `101010000`, the width-`6` word `1010100001` without its last sample. -/
def short6 : List Bool := [true, false, true, false, true, false, false, false, false]

theorem excludes5 : forbidden5.all (excludes (img 5)) = true := by decide +kernel
theorem excludes6 : forbidden6.all (excludes (img 6)) = true := by decide +kernel
theorem excludes_short6 : excludes (img 6) short6 = true := by decide +kernel

/-- **Width 5.** If `H` obeys rule 30 at the columns `1..5` and column `0` alternates white, black
on the ticks `s, …, s + 2 m - 1`, then column `1` at the ticks `s + 2, …, s + 2 m` does not read a
word of `forbidden5` of length `m`. -/
theorem no_word5 {H : Nat → Int → Bool} (hH : Obeys 5 H) (s : Nat) {w : List Bool}
    (hw : w ∈ forbidden5) (hc : ∀ i, i < 2 * w.length → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < w.length → H (s + 2 + 2 * i) 1 = w.getD i false :=
  no_word (by decide) hH (List.all_eq_true.1 excludes5 w hw) s hc

/-- **Width 6.** The same with the columns `1..6` and `forbidden6`. -/
theorem no_word6 {H : Nat → Int → Bool} (hH : Obeys 6 H) (s : Nat) {w : List Bool}
    (hw : w ∈ forbidden6) (hc : ∀ i, i < 2 * w.length → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < w.length → H (s + 2 + 2 * i) 1 = w.getD i false :=
  no_word (by decide) hH (List.all_eq_true.1 excludes6 w hw) s hc

/-- **The shortened width-6 word.** Column `1` does not read `101010000` either. -/
theorem no_short6 {H : Nat → Int → Bool} (hH : Obeys 6 H) (s : Nat)
    (hc : ∀ i, i < 2 * short6.length → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < short6.length → H (s + 2 + 2 * i) 1 = short6.getD i false :=
  no_word (by decide) hH excludes_short6 s hc

/-! ## From an alternation that starts at `T` -/

theorem clock_shift {H : Nat → Int → Bool} {T t : Nat} (hT : ∀ u, T ≤ u → H u 0 = ((u - T) % 2 == 1))
    (ht : T + 2 ≤ t) (hp : (t - T) % 2 = 0) (n : Nat) :
    ∀ i, i < n → H (t - 2 + i) 0 = (i % 2 == 1) := fun i _ => by
  rw [hT _ (by omega), show (t - 2 + i - T) % 2 = i % 2 by omega]

/-- **Width 5 from `T + 2`.** If `H` obeys rule 30 at the columns `1..5` and column `0` is white,
black, white, … from `T`, then from every white time `t ≥ T + 2`, column `1` read at consecutive
white times never spells a word of `forbidden5`. -/
theorem onset5 {H : Nat → Int → Bool} (hH : Obeys 5 H) (T : Nat)
    (hT : ∀ t, T ≤ t → H t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden5,
      ¬ ∀ i, i < pat.length → H (t + 2 * i) 1 = pat.getD i false := by
  intro t ht hp pat hpat hr
  refine no_word5 hH (t - 2) hpat (clock_shift hT ht hp _) fun i hi => ?_
  rw [show t - 2 + 2 + 2 * i = t + 2 * i by omega]
  exact hr i hi

/-- **Width 6 from `T + 2`.** The same with the columns `1..6` and `forbidden6`. -/
theorem onset6 {H : Nat → Int → Bool} (hH : Obeys 6 H) (T : Nat)
    (hT : ∀ t, T ≤ t → H t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden6,
      ¬ ∀ i, i < pat.length → H (t + 2 * i) 1 = pat.getD i false := by
  intro t ht hp pat hpat hr
  refine no_word6 hH (t - 2) hpat (clock_shift hT ht hp _) fun i hi => ?_
  rw [show t - 2 + 2 + 2 * i = t + 2 * i by omega]
  exact hr i hi

/-- **The kit's width-5 constraints with `T' = T + 2`** (`Rule30PeriodTwoWidth5.col1_constraints`
has `∃ T'`). -/
theorem col1_constraints5 (T : Nat) (h : ∀ t, T ≤ t → cell t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden5,
      ¬ ∀ i, i < pat.length → cell (t + 2 * i) 1 = pat.getD i false :=
  onset5 (cell_obeys 5) T h

/-- **The kit's width-6 constraints with `T' = T + 2`** (`Rule30PeriodTwoWidth6.col1_constraints`
has `∃ T'`). -/
theorem col1_constraints6 (T : Nat) (h : ∀ t, T ≤ t → cell t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden6,
      ¬ ∀ i, i < pat.length → cell (t + 2 * i) 1 = pat.getD i false :=
  onset6 (cell_obeys 6) T h

/-! ## The free bits -/

/-- At a white tick of column `0` followed by a black one, column `-1` is the complement of
column `1`, when the rule holds at column `0`. -/
theorem left_right {H : Nat → Int → Bool} (h0 : ObeysAt H 0) {u : Nat} (hu : H u 0 = false)
    (hu1 : H (u + 1) 0 = true) : H u (-1) = !H u 1 := by
  have e := h0 u
  rw [hu1, hu, show (0 : Int) - 1 = -1 by decide, show (0 : Int) + 1 = 1 by decide] at e
  revert e
  cases H u (-1) <;> cases H u 1 <;> decide

theorem free_of_col1 {H : Nat → Int → Bool} (h0 : ObeysAt H 0) (s : Nat) {w : List Bool}
    (hc : ∀ i, i < 2 * w.length + 2 → H (s + i) 0 = (i % 2 == 1))
    (hr : ∀ i, i < w.length → H (s + 2 + 2 * i) (-1) = !w.getD i false) :
    ∀ i, i < w.length → H (s + 2 + 2 * i) 1 = w.getD i false := by
  intro i hi
  have hu : H (s + 2 + 2 * i) 0 = false := by
    have := hc (2 + 2 * i) (by omega)
    rwa [show s + (2 + 2 * i) = s + 2 + 2 * i by omega, show (2 + 2 * i) % 2 = 0 by omega] at this
  have hu1 : H (s + 2 + 2 * i + 1) 0 = true := by
    have := hc (3 + 2 * i) (by omega)
    rwa [show s + (3 + 2 * i) = s + 2 + 2 * i + 1 by omega, show (3 + 2 * i) % 2 = 1 by omega] at this
  have e := left_right h0 hu hu1
  rw [hr i hi] at e
  revert e
  cases H (s + 2 + 2 * i) 1 <;> cases w.getD i false <;> decide

/-- **Free bits, width 5.** If moreover the rule holds at column `0` and the alternation lasts two
more ticks, column `-1` at the ticks `s + 2, …, s + 2 m` does not read the complement of a word of
`forbidden5`. -/
theorem free_bit5 {H : Nat → Int → Bool} (hH : Obeys 5 H) (h0 : ObeysAt H 0) (s : Nat)
    {w : List Bool} (hw : w ∈ forbidden5)
    (hc : ∀ i, i < 2 * w.length + 2 → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < w.length → H (s + 2 + 2 * i) (-1) = !w.getD i false := fun hr =>
  no_word5 hH s hw (fun i hi => hc i (by omega)) (free_of_col1 h0 s hc hr)

/-- **Free bits, width 6.** The same with the columns `1..6` and `forbidden6`. -/
theorem free_bit6 {H : Nat → Int → Bool} (hH : Obeys 6 H) (h0 : ObeysAt H 0) (s : Nat)
    {w : List Bool} (hw : w ∈ forbidden6)
    (hc : ∀ i, i < 2 * w.length + 2 → H (s + i) 0 = (i % 2 == 1)) :
    ¬ ∀ i, i < w.length → H (s + 2 + 2 * i) (-1) = !w.getD i false := fun hr =>
  no_word6 hH s hw (fun i hi => hc i (by omega)) (free_of_col1 h0 s hc hr)

/-- **The kit's width-5 free-bit constraints with `T' = T + 2`**
(`Rule30PeriodTwoWidth5.free_bit_constraints`). -/
theorem free_bit_constraints5 (T : Nat) (h : ∀ t, T ≤ t → cell t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden5,
      ¬ ∀ i, i < pat.length → cell (t + 2 * i) (-1) = !pat.getD i false := by
  intro t ht hp pat hpat hr
  refine free_bit5 (cell_obeys 5) (cell_obeysAt 0) (t - 2) hpat (clock_shift h ht hp _) fun i hi => ?_
  rw [show t - 2 + 2 + 2 * i = t + 2 * i by omega]
  exact hr i hi

/-- **The kit's width-6 free-bit constraints with `T' = T + 2`**
(`Rule30PeriodTwoWidth6.free_bit_constraints`). -/
theorem free_bit_constraints6 (T : Nat) (h : ∀ t, T ≤ t → cell t 0 = ((t - T) % 2 == 1)) :
    ∀ t, T + 2 ≤ t → (t - T) % 2 = 0 → ∀ pat ∈ forbidden6,
      ¬ ∀ i, i < pat.length → cell (t + 2 * i) (-1) = !pat.getD i false := by
  intro t ht hp pat hpat hr
  refine free_bit6 (cell_obeys 6) (cell_obeysAt 0) (t - 2) hpat (clock_shift h ht hp _) fun i hi => ?_
  rw [show t - 2 + 2 + 2 * i = t + 2 * i by omega]
  exact hr i hi

end Rule30PeriodTwoOnset
end Ruliology.CellularAutomata
