module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Rule 30: the wall of a rain-tailed edge code

Read a row from its rightmost black cell, as in `Rule30FrozenRuler`: the row is an edge code, and one tick of rule 30 is the edge map `T`.
This module studies codes with a *rain tail*, cells that alternate from some index on. `T` keeps such a tail and so does every
predecessor, and the *wall* is the last equal pair below the tail. In the `Rule30EdgeStaircases` rain pair, `1010…` has no wall, while `11010…` has its wall at index 0.
The transport and nonperiodicity statements below require a window start at least 2; the local wall rule requires depth at least 5.

* `predecessor_unique`: every code has exactly one predecessor under `T`, so a backward tick is well defined.
* `top_up`, `top_stay`, `top_minus_one`, `top_minus_two`, `top_minus_three`: the wall moves by an exact local rule under `T`.
* `step_rain_tail`, `back_rain_tail`: the tail survives a forward tick and every backward tick.
* `front_back`, `front_not_periodic`: a code with one of eighteen windows of eleven cells at its wall has every predecessor of the same
  form three cells higher, whatever lies below the window, and it is not periodic.
* `deep_words`: three backward advances of three cells leave one of two words at the wall, the *letters* `A = ..####...##` and
  `B = .#.###...##`.
* `no_BB`, `no_AAA`: neither `BB` nor `AAA` occurs. `witness_AA`, `witness_AB`, `witness_BA`, `witness_ABA`: these words do occur.
* `reset`, `above`, `again`, `letters`: the ten-cell word `0, b, !b, 1, u, 1, 0, v, 0, 1`. It contains a reset word `0 1^(3m+1) 0`
  of the family in `Rule30ResetFreeRuns`, with inverse synchronization in `Rule30InverseCascade.run_resets` (kit PR 60), so nothing from below passes it, and with rain above it, it reappears three cells higher.
* `letter_after_B`, `letter_after_A`: the next letter, from the two new cells under the window.
* `Closed`, `Held`, `held_back`, `held_forever`, `held_not_periodic`: a closed set of windows holds a row for ever, whatever lies below.

Nothing here concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30RightWall

open Rule30FrozenRuler

set_option autoImplicit false
set_option maxRecDepth 8192

/-- A row: bit `0` is the rightmost black cell, bit `k` the cell `k` places behind it. -/
abbrev Row := Nat → Bool

/-- One tick of rule 30 on rows: the kit's edge map. -/
abbrev step : Row → Row := T

/-- `t` ticks, with the row first. -/
abbrev iter (x : Row) (t : Nat) : Row := Rule30FrozenRuler.iter t x

theorem step_zero (x : Row) : step x 0 = x 0 := rfl
theorem step_one (x : Row) : step x 1 = xor (x 1) (x 0) := rfl
theorem step_add (x : Row) (j : Nat) : step x (j + 2) = xor (x (j + 2)) (x (j + 1) || x j) := rfl

theorem iter_zero_bit {x : Row} (h : x 0 = true) (t : Nat) : iter x t 0 = true := by
  induction t with
  | zero => exact h
  | succ t ih => exact ih

theorem iter_add (x : Row) (s t : Nat) : iter x (s + t) = iter (iter x s) t := by
  induction t with
  | zero => rfl
  | succ t ih => show step (iter x (s + t)) = step (iter (iter x s) t); rw [ih]

/-! ## Rain tails survive both ways -/

def seg (x : Row) : Nat → Nat → List Bool
  | _, 0 => []
  | L, n + 1 => x L :: seg x (L + 1) n

/-- The inverse recursion read along a list: `p1`, `p2` are the two output bits below it. -/
def back (p1 p2 : Bool) : List Bool → List Bool
  | [] => []
  | b :: r => xor b (p1 || p2) :: back (xor b (p1 || p2)) p1 r

def alt (b : Bool) : Nat → List Bool
  | 0 => []
  | n + 1 => b :: alt (!b) n

theorem seg_length (x : Row) (n : Nat) : ∀ L, (seg x L n).length = n := by
  induction n with
  | zero => intro L; rfl
  | succ n ih => intro L; simp [seg, ih]

theorem seg_append (x : Row) (a b : Nat) : ∀ L, seg x L (a + b) = seg x L a ++ seg x (L + a) b := by
  induction a with
  | zero => intro L; simp [seg]
  | succ a ih =>
    intro L
    have : a + 1 + b = (a + b) + 1 := by omega
    rw [this]
    show x L :: seg x (L + 1) (a + b) = (x L :: seg x (L + 1) a) ++ seg x (L + (a + 1)) b
    rw [ih (L + 1)]
    have : L + 1 + a = L + (a + 1) := by omega
    rw [this]; rfl

theorem seg_getD (x : Row) (n : Nat) : ∀ L i, i < n → (seg x L n).getD i false = x (L + i) := by
  induction n with
  | zero => intro L i h; omega
  | succ n ih =>
    intro L i h
    cases i with
    | zero => rfl
    | succ i =>
      show (seg x (L + 1) n).getD i false = x (L + (i + 1))
      rw [ih (L + 1) i (by omega)]
      have : L + 1 + i = L + (i + 1) := by omega
      rw [this]

theorem seg_alt {x : Row} {J : Nat} (h : ∀ j, J ≤ j → x (j + 1) = !x j) (n : Nat) :
    ∀ L, J ≤ L → seg x L n = alt (x L) n := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    show x L :: seg x (L + 1) n = x L :: alt (!x L) n
    rw [ih (L + 1) (by omega), h L hL]

theorem back_seg {z x : Row} (hs : step z = x) (n : Nat) :
    ∀ L, 2 ≤ L → seg z L n = back (z (L - 1)) (z (L - 2)) (seg x L n) := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    obtain ⟨i, rfl⟩ : ∃ i, L = i + 2 := ⟨L - 2, by omega⟩
    have hx : x (i + 2) = xor (z (i + 2)) (z (i + 1) || z i) := by rw [← hs]; rfl
    have ho : xor (x (i + 2)) (z (i + 1) || z i) = z (i + 2) := by
      rw [hx]; cases z (i + 2) <;> cases (z (i + 1) || z i) <;> rfl
    show z (i + 2) :: seg z (i + 2 + 1) n =
      xor (x (i + 2)) (z (i + 1) || z i) :: back (xor (x (i + 2)) (z (i + 1) || z i)) (z (i + 1)) (seg x (i + 2 + 1) n)
    rw [ho, ih (i + 2 + 1) (by omega)]
    rfl

/-- Once a predecessor is the complement of a rain tail on two adjacent bits, it is for ever. -/
theorem compl_tail {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) (d : Nat) :
    z (J + d) = !x (J + d) ∧ z (J + d + 1) = !x (J + d + 1) := by
  induction d with
  | zero => exact ⟨h0, h1⟩
  | succ d ih =>
    obtain ⟨a, b⟩ := ih
    refine ⟨b, ?_⟩
    have hxx : x (J + d + 2) = xor (z (J + d + 2)) (z (J + d + 1) || z (J + d)) := by rw [← hs]; rfl
    have hxs := hx (J + d) (by omega)
    have hor : (z (J + d + 1) || z (J + d)) = true := by
      rw [b, a, hxs]; cases x (J + d) <;> rfl
    rw [hor] at hxx
    show z (J + d + 2) = !x (J + d + 2)
    rw [hxx]; cases z (J + d + 2) <;> rfl

theorem tail_of_compl {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) : ∀ j, J ≤ j → z (j + 1) = !z j := by
  intro j hj
  obtain ⟨d, rfl⟩ : ∃ d, j = J + d := ⟨j - J, by omega⟩
  obtain ⟨a, b⟩ := compl_tail hs hx h0 h1 d
  rw [a, b, hx (J + d) (by omega)]

/-- A rain tail survives a forward tick. -/
theorem step_rain_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) :
    ∀ j, D + 2 ≤ j → step x (j + 1) = !step x j := by
  intro j hj
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 2 := ⟨j - 2, by omega⟩
  have a1 := h i (by omega)
  have a2 := h (i + 1) (by omega)
  have a3 := h (i + 2) (by omega)
  show xor (x (i + 3)) (x (i + 2) || x (i + 1)) = !xor (x (i + 2)) (x (i + 1) || x i)
  rw [a3, a2, a1]
  cases x i <;> rfl

theorem chk_tail : ∀ p1 p2 b : Bool,
    (back p1 p2 (alt b 5)).getD 3 false = !(alt b 5).getD 3 false ∧
    (back p1 p2 (alt b 5)).getD 4 false = !(alt b 5).getD 4 false := by decide

/-- A rain tail survives a backward tick, three bits higher: every predecessor of a rain-tailed row is rain-tailed. -/
theorem back_rain_tail {z x : Row} {D : Nat} (hD : 2 ≤ D) (hs : step z = x)
    (h : ∀ j, D ≤ j → x (j + 1) = !x j) : ∀ j, D + 3 ≤ j → z (j + 1) = !z j := by
  have e := back_seg hs 5 D hD
  rw [seg_alt h 5 D (Nat.le_refl D)] at e
  obtain ⟨c0, c1⟩ := chk_tail (z (D - 1)) (z (D - 2)) (x D)
  rw [← e, seg_getD z 5 D 3 (by omega)] at c0
  rw [← e, seg_getD z 5 D 4 (by omega)] at c1
  have s3 : (alt (x D) 5).getD 3 false = x (D + 3) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 3 (by omega)
  have s4 : (alt (x D) 5).getD 4 false = x (D + 4) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 4 (by omega)
  rw [s3] at c0
  rw [s4] at c1
  exact tail_of_compl hs (fun j hj => h j (by omega)) c0 c1

/-! ## The top-wall rule -/

/-- `D` is the top wall: its two cells agree and rain lies above. -/
def Top (x : Row) (D : Nat) : Prop := x (D + 1) = x D ∧ ∀ j, D + 1 ≤ j → x (j + 1) = !x j

/-- A white top wall rises by two and turns black. -/
theorem top_up {x : Row} {k : Nat} (h : Top x (k + 5)) (hw : x (k + 5) = false) :
    Top (step x) (k + 7) ∧ step x (k + 7) = true := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have s7 : step x (k + 7) = xor (x (k + 7)) (x (k + 6) || x (k + 5)) := rfl
  have s8 : step x (k + 8) = xor (x (k + 8)) (x (k + 7) || x (k + 6)) := rfl
  have b6 : x (k + 6) = false := by rw [show k + 6 = k + 5 + 1 from rfl, e, hw]
  have r7 : step x (k + 7) = true := by rw [s7, a1, b6, hw]; rfl
  have r8 : step x (k + 8) = true := by rw [s8, a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 7 + 1 = k + 8 from rfl, r7, r8], ?_⟩, r7⟩
  intro j hj
  exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- A black top wall with a black cell among the next two stays and turns white. -/
theorem top_stay {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (hc : (x (k + 4) || x (k + 3)) = true) : Top (step x) (k + 5) ∧ step x (k + 5) = false := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = false := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = false
    rw [hb, hc]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 5 + 1 = k + 6 from rfl, r5, r6], ?_⟩, r5⟩
  intro j hj
  by_cases c6 : j = k + 6
  · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
  · by_cases c7 : j = k + 7
    · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
    · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Above a black top wall with two white cells under it, the row after a tick reads black, white, black from the wall up. -/
theorem top_fall_rain {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) :
    step x (k + 5) = true ∧ step x (k + 6) = false ∧ ∀ j, k + 5 ≤ j → step x (j + 1) = !step x j := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = true := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = true
    rw [hb, h4, h3]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨r5, r6, ?_⟩
  intro j hj
  by_cases c5 : j = k + 5
  · subst c5; rw [show k + 5 + 1 = k + 6 from rfl, r5, r6]; rfl
  · by_cases c6 : j = k + 6
    · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
    · by_cases c7 : j = k + 7
      · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
      · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Retreat by one: the wall drops one cell and stays black. -/
theorem top_minus_one {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = true) :
    Top (step x) (k + 4) ∧ step x (k + 4) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = true := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = true
    rw [h4, h3, h2]; rfl
  exact ⟨⟨by rw [show k + 4 + 1 = k + 5 from rfl, r4, r5], hr⟩, r4⟩

/-- Retreat by two: the wall drops two cells and turns white. -/
theorem top_minus_two {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = false) :
    Top (step x) (k + 3) ∧ step x (k + 3) = false := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = false := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = false
    rw [h3, h2, h1]; rfl
  refine ⟨⟨by rw [show k + 3 + 1 = k + 4 from rfl, r3, r4], ?_⟩, r3⟩
  intro j hj
  by_cases c4 : j = k + 4
  · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
  · exact hr j (by omega)

/-- Retreat by three: the wall drops three cells and stays black. -/
theorem top_minus_three {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = true) :
    Top (step x) (k + 2) ∧ step x (k + 2) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = true := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = true
    rw [h3, h2, h1]; rfl
  have r2 : step x (k + 2) = true := by
    show xor (x (k + 2)) (x (k + 1) || x k) = true
    rw [h2, h1]; rfl
  refine ⟨⟨by rw [show k + 2 + 1 = k + 3 from rfl, r2, r3], ?_⟩, r2⟩
  intro j hj
  by_cases c3 : j = k + 3
  · subst c3; rw [show k + 3 + 1 = k + 4 from rfl, r3, r4]; rfl
  · by_cases c4 : j = k + 4
    · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
    · exact hr j (by omega)

/-! ## The robust backward front -/

/-- The eighteen windows, low to high; the top wall is their last two cells. -/
def B11 : List (List Bool) := [
  [false, true, false, false, true, false, false, false, false, true, true],
  [false, false, true, false, true, false, false, false, false, true, true],
  [true, false, true, false, true, false, false, false, false, true, true],
  [false, true, false, true, false, true, false, false, false, true, true],
  [false, false, true, true, false, true, false, false, false, true, true],
  [true, false, true, true, false, true, false, false, false, true, true],
  [false, true, false, true, true, true, false, false, false, true, true],
  [false, false, true, true, true, true, false, false, false, true, true],
  [true, false, true, true, true, true, false, false, false, true, true],
  [false, true, false, false, true, false, false, true, false, true, true],
  [false, false, true, false, true, false, false, true, false, true, true],
  [true, false, true, false, true, false, false, true, false, true, true],
  [false, true, false, true, false, true, false, true, false, true, true],
  [false, false, true, true, false, true, false, true, false, true, true],
  [true, false, true, true, false, true, false, true, false, true, true],
  [false, true, false, true, true, true, false, true, false, true, true],
  [false, false, true, true, true, true, false, true, false, true, true],
  [true, false, true, true, true, true, false, true, false, true, true]]

/-- A row with its window of eleven cells from `L` in `B11` and rain above it. -/
def Front (x : Row) (L : Nat) : Prop :=
  seg x L 11 ∈ B11 ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

/-- A window with seven cells of rain over its last. -/
def inp (w : List Bool) : List Bool := w.take 10 ++ alt (w.getD 10 false) 7

theorem chk_mem : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool, ((back p1 p2 (inp w)).drop 3).take 11 ∈ B11 := by decide +kernel
theorem chk_a : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 14 false = !(back p1 p2 (inp w)).getD 13 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(inp w).getD 15 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 16 false = !(inp w).getD 16 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(back p1 p2 (inp w)).getD 14 false := by decide +kernel
theorem chk_wall : ∀ w, w ∈ B11 → w.getD 9 false = w.getD 10 false := by decide +kernel

theorem seg_inp {x : Row} {L : Nat} (h : ∀ j, L + 10 ≤ j → x (j + 1) = !x j) : seg x L 17 = inp (seg x L 11) := by
  have e1 : seg x L 11 = seg x L 10 ++ seg x (L + 10) 1 := seg_append x 10 1 L
  have e2 : (seg x L 11).take 10 = seg x L 10 := by
    rw [e1]; exact List.take_left' (seg_length x 10 L)
  have e3 : (seg x L 11).getD 10 false = x (L + 10) := seg_getD x 11 L 10 (by omega)
  show seg x L 17 = (seg x L 11).take 10 ++ alt ((seg x L 11).getD 10 false) 7
  rw [e2, e3, ← seg_alt h 7 (L + 10) (Nat.le_refl _)]
  exact seg_append x 10 7 L

/-- **The robust backward front.** Every predecessor of a front is a front three cells higher, whatever lies below the window. -/
theorem front_back {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Front x L) : Front z (L + 3) := by
  obtain ⟨hw, hr⟩ := hf
  have e : seg z L 17 = back (z (L - 1)) (z (L - 2)) (inp (seg x L 11)) := by
    rw [back_seg hs 17 L hL, seg_inp hr]
  have ha := chk_a _ hw (z (L - 1)) (z (L - 2))
  have hb := chk_b _ hw (z (L - 1)) (z (L - 2))
  have hc := chk_c _ hw (z (L - 1)) (z (L - 2))
  have hd := chk_d _ hw (z (L - 1)) (z (L - 2))
  have hm := chk_mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd hm
  have g : ∀ i, i < 17 → (seg z L 17).getD i false = z (L + i) := fun i h => seg_getD z 17 L i h
  rw [g 13 (by omega), g 14 (by omega)] at ha
  rw [g 14 (by omega), g 15 (by omega)] at hd
  rw [g 15 (by omega)] at hb
  rw [g 16 (by omega)] at hc
  have q : ∀ i, i < 17 → (inp (seg x L 11)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hr]; exact seg_getD x 17 L i h
  rw [q 15 (by omega)] at hb
  rw [q 16 (by omega)] at hc
  have hwin : seg z (L + 3) 11 = ((seg z L 17).drop 3).take 11 := by
    have e1 : seg z L 17 = seg z L 3 ++ seg z (L + 3) 14 := seg_append z 3 14 L
    have e2 : seg z (L + 3) 14 = seg z (L + 3) 11 ++ seg z (L + 3 + 11) 3 := seg_append z 11 3 (L + 3)
    rw [e1, List.drop_left' (seg_length z 3 L), e2]
    exact (List.take_left' (seg_length z 11 (L + 3))).symm
  refine ⟨by rw [hwin]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + 15) (fun j hj => hr j (by omega)) hb hc
  intro j hj
  by_cases c1 : j = L + 13
  · subst c1; exact ha
  · by_cases c2 : j = L + 14
    · subst c2; exact hd
    · exact htail j (by omega)

theorem front_iter {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hper : iter x P = x) :
    ∀ i, i ≤ P → Front (iter x (P - i)) (L + 3 * i) := by
  intro i
  induction i with
  | zero => intro _; simpa [hper] using h
  | succ i ih =>
    intro hi
    have hs : step (iter x (P - (i + 1))) = iter x (P - i) := by
      have : P - i = (P - (i + 1)) + 1 := by omega
      rw [this]; rfl
    have := front_back (by omega) hs (ih (by omega))
    have e : L + 3 * i + 3 = L + 3 * (i + 1) := by omega
    rw [e] at this
    exact this

/-- **A row with a front is not periodic.** So a periodic row with a rain tail never shows one of the eighteen windows at its top. -/
theorem front_not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := front_iter hL h hper P (Nat.le_refl P)
  have e0 : P - P = 0 := by omega
  rw [e0] at hf
  have hf' : Front x (L + 3 * P) := hf
  obtain ⟨hw, _⟩ := hf'
  have hwall := chk_wall _ hw
  rw [seg_getD x 11 _ 9 (by omega), seg_getD x 11 _ 10 (by omega)] at hwall
  have hr := h.2 (L + 3 * P + 9) (by omega)
  have : L + 3 * P + 9 + 1 = L + 3 * P + 10 := rfl
  rw [this, ← hwall] at hr
  cases hb : x (L + 3 * P + 9) <;> simp [hb] at hr

/-! ## Forward transport of finite windows -/

/-- Compute a forward word starting two cells above the input start. -/
def shrink : List Bool → List Bool
  | a :: b :: c :: rest => xor c (b || a) :: shrink (b :: c :: rest)
  | _ => []

def shrinkN (word : List Bool) : Nat → List Bool
  | 0 => word
  | r + 1 => shrinkN (shrink word) r

theorem shrink_seg (z : Row) (A w : Nat) :
    shrink (seg z A (w + 2)) = seg (step z) (A + 2) w := by
  induction w generalizing A with
  | zero => rfl
  | succ w ih =>
    change xor (z (A + 2)) (z (A + 1) || z A) :: shrink (seg z (A + 1) (w + 2)) =
      step z (A + 2) :: seg (step z) (A + 2 + 1) w
    rw [ih] <;> rfl

/-- Exact locality in the original spatial coordinate, for every tick and width. -/
theorem shrinkN_seg (z : Row) (A r w : Nat) :
    shrinkN (seg z A (2 * r + w)) r = seg (iter z r) (A + 2 * r) w := by
  induction r generalizing z A w with
  | zero => simp [shrinkN, iter, Rule30FrozenRuler.iter]
  | succ r ih =>
    have length : 2 * (r + 1) + w = (2 * r + w) + 2 := by omega
    have pos : A + 2 + 2 * r = A + 2 * (r + 1) := by omega
    have time : iter (step z) r = iter z (r + 1) := by
      rw [Nat.add_comm r 1, iter_add z 1 r] <;> rfl
    rw [shrinkN, length, shrink_seg, ih, pos, time]

def contexts : Nat → List (List Bool)
  | 0 => [[]]
  | n+1 => (contexts n).map (false :: ·) ++ (contexts n).map (true :: ·)

theorem mem_contexts (c : List Bool) : c ∈ contexts c.length := by
  induction c with
  | nil => simp [contexts]
  | cons b bs ih =>
    change b :: bs ∈ (contexts bs.length).map (false :: ·) ++ (contexts bs.length).map (true :: ·)
    cases b with
    | false => exact List.mem_append_left _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)
    | true => exact List.mem_append_right _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)

/-! ## Three advances leave two letters -/

/-- An alternating tail above one wall excludes every higher wall. -/
private theorem excludes_higher {x : Row} {d e : Nat} (h : Top x d) (lt : d < e) : ¬Top x e := by
  intro upper
  have alt := h.2 e (by omega)
  rw [upper.1] at alt
  cases b : x e <;> simp [b] at alt

private theorem both_false {u v : Bool} (h : (u || v) = false) : u = false ∧ v = false := by
  cases u <;> cases v <;> simp_all

theorem marker {x : Row} (k : Nat) (a : Top x (k+5)) (b : Top (step x) (k+2)) :
    seg x (k+1) 6 = [true,false,false,false,true,true] := by
  have h5 : x (k+5) = true := by
    cases h : x (k+5) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_up a h).1)
  have white : (x (k+4) || x (k+3)) = false := by
    cases h : x (k+4) || x (k+3) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_stay a h5 h).1)
  obtain ⟨h4,h3⟩ := both_false white
  have h2 : x (k+2) = false := by
    cases h : x (k+2) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_minus_one a h5 h4 h3 h).1)
  have h1 : x (k+1) = true := by
    cases h : x (k+1) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_minus_two a h5 h4 h3 h2 h).1)
  have h6 : x (k+6) = true := a.1.trans h5
  change [x (k+1), x (k+2), x (k+3), x (k+4), x (k+5), x (k+6)] = _
  rw [h1,h2,h3,h4,h5,h6]

def wordA : List Bool := [false,false,true,true,true,true,false,false,false,true,true]
def wordB : List Bool := [false,true,false,true,true,true,false,false,false,true,true]
private def mark : List Bool := [true,false,false,false,true,true]

private theorem known : wordA ∈ B11 ∧ wordB ∈ B11 := by decide +kernel

/- Three forward retreat markers, displaced three cells at each step.
The ten free lower bits suffice for all three observations by exact locality. -/
set_option maxRecDepth 8192 in
set_option maxHeartbeats 1200000 in
private theorem local_cut : ∀ c, c ∈ contexts 10 →
    (((shrink (c ++ mark)).drop 5).take 6 = mark) →
    ((shrinkN (c ++ mark) 2).take 6 = mark) →
    (c ++ mark).drop 5 = wordA ∨ (c ++ mark).drop 5 = wordB := by decide +kernel

private theorem slice_seg (x : Row) (L a m b : Nat) :
    ((seg x L (a+(m+b))).drop a).take m = seg x (L+a) m := by
  rw [seg_append x a (m+b) L, List.drop_left' (seg_length x a L),
    seg_append x m b (L+a), List.take_left' (seg_length x m (L+a))]

theorem deep_words (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) :
    seg z D 11 = wordA ∨ seg z D 11 = wordB := by
  obtain ⟨k, rfl⟩ : ∃ k, D=k+5 := ⟨D-5, by omega⟩
  have m0 := marker (k+9) a b
  have m1 := marker (k+6) b c
  have m2 := marker (k+3) c d
  let low := seg z k 10
  have whole : low ++ mark = seg z k 16 := by
    rw [seg_append z 10 6 k, m0]
    rfl
  have context : low ∈ contexts 10 := by
    simpa only [low, seg_length] using mem_contexts (seg z k 10)
  have p1 : ((shrink (low ++ mark)).drop 5).take 6 = mark := by
    rw [whole, shrink_seg z k 14, slice_seg (step z) (k+2) 5 6 3]
    exact m1
  have p2 : (shrinkN (low ++ mark) 2).take 6 = mark := by
    rw [whole, shrinkN_seg z k 2 12, seg_append (iter z 2) 6 6 (k+4),
      List.take_left' (seg_length (iter z 2) 6 (k+4))]
    exact m2
  have choices := local_cut low context p1 p2
  rw [whole, seg_append z 5 11 k, List.drop_left' (seg_length z 5 k)] at choices
  exact choices

theorem deep (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) : Front z D := by
  have choices := deep_words z D hD a b c d
  refine ⟨?_, a.2⟩
  rcases choices with w | w
  · rw [w]; exact known.1
  · rw [w]; exact known.2

/-! ## The language of the letters -/

private theorem incompatible (a b c : Bool) :
    ¬(xor c (b || a) = false ∧ xor false (c || b) = true ∧ xor true (false || c) = true) := by
  cases a <;> cases b <;> cases c <;> decide

private theorem readB {x : Row} {L : Nat} (w : seg x L 11 = wordB) (i : Nat) (hi : i < 11) :
    x (L+i) = wordB.getD i false := by rw [←w,seg_getD _ _ _ _ hi]

/-- The deeper B is on the predecessor row `z`. If its successor had B
three cells lower, the successor bits at offsets 2,3,4 would be 0,1,1,
while the input bits at offsets 3,4 would be 0,1. No choice of the other
three inputs is consistent with that update. -/
theorem no_BB (z : Row) (L : Nat) (deep : seg z (L+3) 11 = wordB) :
    seg (step z) L 11 ≠ wordB := by
  intro shallow
  have s2 : step z (L+2) = false := readB shallow 2 (by decide)
  have s3 : step z (L+3) = true := readB shallow 3 (by decide)
  have s4 : step z (L+4) = true := readB shallow 4 (by decide)
  have b3 : z (L+3) = false := readB deep 0 (by decide)
  have b4 : z (L+4) = true := readB deep 1 (by decide)
  change xor (z (L+2)) (z (L+1) || z L) = false at s2
  change xor (z (L+3)) (z (L+2) || z (L+1)) = true at s3
  change xor (z (L+4)) (z (L+3) || z (L+2)) = true at s4
  rw [b3] at s3
  rw [b4,b3] at s4
  exact incompatible (z L) (z (L+1)) (z (L+2)) ⟨s2,s3,s4⟩

/-- Extend bit 10 by alternation above the given eleven-bit source word. -/
def source (w low L j : Nat) : Bool :=
  if j < L then low.testBit j else if j < L+10 then w.testBit (j-L)
  else if (j-(L+10)) % 2 = 0 then w.testBit 10 else !(w.testBit 10)

private theorem read {x : Row} {L : Nat} {w : List Bool} (h : seg x L 11 = w) (i : Nat) (hi : i < 11) :
    x (L + i) = w.getD i false := by
  rw [← h, seg_getD _ _ _ _ hi]

private theorem or_false' {a b : Bool} (h : (a || b) = false) : a = false ∧ b = false := by
  cases a <;> cases b <;> simp_all

/-- **`A` cannot occur three times in succession.** The deepest window is on the row `z`, and the two later
windows are on its forward images, three cells lower each. -/
theorem no_AAA (z : Row) (L : Nat) (deep : seg z (L + 6) 11 = wordA)
    (mid : seg (step z) (L + 3) 11 = wordA) (top : seg (step (step z)) L 11 = wordA) : False := by
  -- the window on the top row against the middle row
  have v2 : step (step z) (L + 2) = true := read top 2 (by decide)
  have v4 : step (step z) (L + 4) = true := read top 4 (by decide)
  have u3 : step z (L + 3) = false := read mid 0 (by decide)
  have u4 : step z (L + 4) = false := read mid 1 (by decide)
  have u5 : step z (L + 5) = true := read mid 2 (by decide)
  have u7 : step z (L + 7) = true := read mid 4 (by decide)
  have z6 : z (L + 6) = false := read deep 0 (by decide)
  have z7 : z (L + 7) = false := read deep 1 (by decide)
  change xor (step z (L + 4)) (step z (L + 3) || step z (L + 2)) = true at v4
  rw [u4, u3] at v4
  have u2 : step z (L + 2) = true := by simpa using v4
  change xor (step z (L + 2)) (step z (L + 1) || step z L) = true at v2
  rw [u2] at v2
  have w1 : (step z (L + 1) || step z L) = false := by simpa using v2
  have u1 : step z (L + 1) = false := (or_false' w1).1
  -- the same two steps one row deeper
  change xor (z (L + 7)) (z (L + 6) || z (L + 5)) = true at u7
  rw [z7, z6] at u7
  have z5 : z (L + 5) = true := by simpa using u7
  change xor (z (L + 5)) (z (L + 4) || z (L + 3)) = true at u5
  rw [z5] at u5
  have w2 : (z (L + 4) || z (L + 3)) = false := by simpa using u5
  obtain ⟨z4, z3⟩ := or_false' w2
  change xor (z (L + 4)) (z (L + 3) || z (L + 2)) = false at u4
  rw [z4, z3] at u4
  have z2 : z (L + 2) = false := by simpa using u4
  change xor (z (L + 3)) (z (L + 2) || z (L + 1)) = false at u3
  rw [z3, z2] at u3
  have z1 : z (L + 1) = false := by simpa using u3
  change xor (z (L + 2)) (z (L + 1) || z L) = true at u2
  rw [z2, z1] at u2
  have z0 : z L = true := by simpa using u2
  -- wheel L + 1 of the middle row cannot be white
  cases L with
  | zero =>
    have e : step z 1 = xor (z 1) (z 0) := rfl
    simp only [Nat.zero_add] at u1 z1 z0
    rw [e, z1, z0] at u1
    cases u1
  | succ k =>
    have e : step z (k + 1 + 1) = xor (z (k + 1 + 1)) (z (k + 1) || z k) := rfl
    rw [e, z1, z0] at u1
    cases u1

/-! ## Witnesses on anchored rows -/

/-- The row `x` shows the word `w` from cell `L`, with rain above it. -/
def Shows (x : Row) (L : Nat) (w : List Bool) : Prop :=
  seg x L 11 = w ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

theorem source_tail (w low L j : Nat) (hj : L + 10 ≤ j) :
    source w low L (j + 1) = !source w low L j := by
  by_cases a : (j - (L + 10)) % 2 = 0
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega

/-- A forward image keeps the rain, given the few cells that the general lemma does not reach. -/
private theorem step_shows {x : Row} {L P : Nat} {w : List Bool} (h : ∀ j, L ≤ j → x (j + 1) = !x j)
    (hw : seg (step x) P 11 = w)
    (near : ∀ j : Fin (L + 2), P + 10 ≤ j.val → step x (j.val + 1) = !step x j.val) :
    Shows (step x) P w := by
  refine ⟨hw, fun j hj => ?_⟩
  by_cases c : j < L + 2
  · exact near ⟨j, c⟩ hj
  · exact step_rain_tail h j (by omega)

/-- `AA`: the row with low bits 33 below `A`. -/
theorem witness_AA :
    source 1596 33 6 0 = true ∧ Shows (source 1596 33 6) 6 wordA ∧ Shows (step (source 1596 33 6)) 3 wordA := by
  have t := source_tail 1596 33 6
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 16) t (by decide +kernel) (by decide +kernel)

/-- `AB` in backward order: `B` on the deeper row. The low bits are 7. -/
theorem witness_AB :
    source 1594 7 4 0 = true ∧ Shows (source 1594 7 4) 4 wordB ∧ Shows (step (source 1594 7 4)) 1 wordA := by
  have t := source_tail 1594 7 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `BA` in backward order: `A` on the deeper row. The low bits are 11. -/
theorem witness_BA :
    source 1596 11 4 0 = true ∧ Shows (source 1596 11 4) 4 wordA ∧ Shows (step (source 1596 11 4)) 1 wordB := by
  have t := source_tail 1596 11 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `ABA` on one row: both ends of the pair of pairs share one shallow history. The low bits are 97. -/
theorem witness_ABA :
    source 1596 97 7 0 = true ∧ Shows (source 1596 97 7) 7 wordA ∧ Shows (step (source 1596 97 7)) 4 wordB ∧
      Shows (step (step (source 1596 97 7))) 1 wordA := by
  have t := source_tail 1596 97 7
  have s1 : Shows (step (source 1596 97 7)) 4 wordB := step_shows (L := 17) t (by decide +kernel) (by decide +kernel)
  refine ⟨by decide, ⟨by decide +kernel, t⟩, s1, ?_⟩
  exact step_shows (L := 19) (fun j hj => s1.2 j (by omega)) (by decide +kernel) (by decide +kernel)

/-! ## The shield -/

namespace Reset

/-- The reset word. -/
def F (b u v : Bool) : List Bool := [false, b, !b, true, u, true, false, v, false, true]

/-- The first seven cells of the word. -/
def W (b u : Bool) : List Bool := [false, b, !b, true, u, true, false]

/-- The bit of the new word. -/
def newbit (b u p1 p2 : Bool) : Bool := if b || (!p1 && !p2) then !u else u

/-- **The reset.** Under any two lower cells the output on cells 3 to 9 of the word is the shape `W` with the new bit. -/
theorem reset : ∀ b u v p1 p2 : Bool, ((back p1 p2 (F b u v)).drop 3).take 7 = W (newbit b u p1 p2) (!v) := by decide

/-- **Nothing passes.** Above the word the output is the same function of the input, whatever the bits of the word and the cells below it. -/
theorem above (b u v p1 p2 : Bool) (r : List Bool) : (back p1 p2 (F b u v ++ r)).drop 10 = back false true r := by
  cases b <;> cases u <;> cases v <;> cases p1 <;> cases p2 <;> rfl

/-- **Again.** If the old row reads `s, !s, s` above the word, the new word is a reset word again, three cells higher. -/
theorem again : ∀ b u v s p1 p2 : Bool,
    ((back p1 p2 (F b u v ++ [s, !s, s])).drop 3).take 10 = F (newbit b u p1 p2) (!v) (!s) := by decide

/-- The wall letters are reset words, with `u` black and `v` white, under one black cell. -/
theorem letters : wordA = F false true false ++ [true] ∧ wordB = F true true false ++ [true] := by decide

end Reset

/-! ## Closed sets of windows -/

namespace WindowClosed

/-- A window with seven cells of rain over its last. -/
def inp (W : Nat) (w : List Bool) : List Bool := w.take (W - 1) ++ alt (w.getD (W - 1) false) 7

/-- The image of a window under the backward tick with lower cells `p1`, `p2`. -/
def next (W : Nat) (w : List Bool) (p1 p2 : Bool) : List Bool := ((back p1 p2 (inp W w)).drop 3).take W

/-- The finite checks. -/
structure Closed (W : Nat) (S : List (List Bool)) : Prop where
  pos : 1 ≤ W
  mem : ∀ w, w ∈ S → ∀ p1 p2 : Bool, next W w p1 p2 ∈ S
  a : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 3) false = !(back p1 p2 (inp W w)).getD (W + 2) false
  d : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(back p1 p2 (inp W w)).getD (W + 3) false
  b : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(inp W w).getD (W + 4) false
  c : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 5) false = !(inp W w).getD (W + 5) false

/-- A row with its window of `W` cells from `L` in `S` and rain above it. -/
def Held (W : Nat) (S : List (List Bool)) (x : Row) (L : Nat) : Prop :=
  seg x L W ∈ S ∧ ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j

theorem seg_inp {W : Nat} (hW : 1 ≤ W) {x : Row} {L : Nat} (h : ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j) :
    seg x L (W + 6) = inp W (seg x L W) := by
  have e1 : seg x L W = seg x L (W - 1) ++ seg x (L + (W - 1)) 1 := by
    have := seg_append x (W - 1) 1 L
    rwa [show W - 1 + 1 = W by omega] at this
  have e2 : (seg x L W).take (W - 1) = seg x L (W - 1) := by
    rw [e1]; exact List.take_left' (seg_length x (W - 1) L)
  have e3 : (seg x L W).getD (W - 1) false = x (L + (W - 1)) := seg_getD x W L (W - 1) (by omega)
  show seg x L (W + 6) = (seg x L W).take (W - 1) ++ alt ((seg x L W).getD (W - 1) false) 7
  rw [e2, e3, ← seg_alt (J := L + (W - 1)) (fun j hj => h j (by omega)) 7 (L + (W - 1)) (Nat.le_refl _)]
  have := seg_append x (W - 1) 7 L
  rwa [show W - 1 + 7 = W + 6 by omega] at this

private theorem seg_next (W : Nat) {z : Row} {L : Nat} :
    seg z (L + 3) W = ((seg z L (W + 6)).drop 3).take W := by
  have e1 : seg z L (W + 6) = seg z L 3 ++ seg z (L + 3) (W + 3) := by
    have := seg_append z 3 (W + 3) L
    rwa [show 3 + (W + 3) = W + 6 by omega] at this
  have e2 : seg z (L + 3) (W + 3) = seg z (L + 3) W ++ seg z (L + 3 + W) 3 := seg_append z W 3 (L + 3)
  rw [e1, List.drop_left' (seg_length z 3 L), e2]
  exact (List.take_left' (seg_length z W (L + 3))).symm

/-- One tick, on rows. -/
theorem next_seg {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : seg z (L + 3) W = next W (seg x L W) (z (L - 1)) (z (L - 2)) := by
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp C.pos hf.2]
  rw [seg_next, e]; rfl

/-- **The tick.** Every predecessor of a held row is held three cells higher, whatever lies below the window. -/
theorem held_back {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : Held W S z (L + 3) := by
  have hW := C.pos
  obtain ⟨hw, hr⟩ := id hf
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp hW hr]
  have ha := C.a _ hw (z (L - 1)) (z (L - 2))
  have hb := C.b _ hw (z (L - 1)) (z (L - 2))
  have hc := C.c _ hw (z (L - 1)) (z (L - 2))
  have hd := C.d _ hw (z (L - 1)) (z (L - 2))
  have hm := C.mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd
  have g : ∀ i, i < W + 6 → (seg z L (W + 6)).getD i false = z (L + i) := fun i h => seg_getD z (W + 6) L i h
  rw [g (W + 2) (by omega), g (W + 3) (by omega)] at ha
  rw [g (W + 3) (by omega), g (W + 4) (by omega)] at hd
  rw [g (W + 4) (by omega)] at hb
  rw [g (W + 5) (by omega)] at hc
  have q : ∀ i, i < W + 6 → (inp W (seg x L W)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hW hr]; exact seg_getD x (W + 6) L i h
  rw [q (W + 4) (by omega)] at hb
  rw [q (W + 5) (by omega)] at hc
  refine ⟨by rw [next_seg C hL hs hf]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + (W + 4)) (fun j hj => hr j (by omega)) hb
    (by rw [show L + (W + 4) + 1 = L + (W + 5) by omega]; exact hc)
  intro j hj
  by_cases c1 : j = L + (W + 2)
  · subst c1; exact ha
  · by_cases c2 : j = L + (W + 3)
    · subst c2; exact hd
    · exact htail j (by omega)

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher. -/
theorem held_forever {W : Nat} {S : List (List Bool)} (C : Closed W S) {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W S x L) :
    ∀ n z, iter z n = x → Held W S z (L + 3 * n) := by
  intro n
  induction n with
  | zero => intro z hz; rw [show iter z 0 = z from rfl] at hz; subst hz; exact h
  | succ n ih =>
    intro z hz
    have e : iter z (1 + n) = iter (iter z 1) n := iter_add z 1 n
    rw [Nat.add_comm n 1, e] at hz
    have := held_back C (by omega) (show step z = iter z 1 from rfl) (ih (iter z 1) hz)
    have e2 : L + 3 * n + 3 = L + 3 * (n + 1) := by omega
    rw [e2] at this
    exact this

end WindowClosed

/-- The predecessor, by triangular recovery of the whole row. -/
def previous (x : Row) : Row
  | 0 => x 0
  | 1 => xor (x 1) (x 0)
  | j + 2 => xor (x (j + 2)) (previous x (j + 1) || previous x j)

theorem xor_twice (a b : Bool) : xor (xor a b) b = a := by
  cases a <;> cases b <;> rfl

theorem step_previous (x : Row) : step (previous x) = x := by
  funext j
  cases j with
  | zero => rfl
  | succ k =>
    cases k with
    | zero => exact xor_twice _ _
    | succ i =>
      rw [step_add, previous]
      exact xor_twice _ _

theorem previous_step (x : Row) : previous (step x) = x := by
  have pair : ∀ i, previous (step x) i = x i ∧ previous (step x) (i + 1) = x (i + 1) := by
    intro i
    induction i with
    | zero => exact ⟨rfl, xor_twice _ _⟩
    | succ i ih =>
      refine ⟨ih.2, ?_⟩
      rw [previous, ih.1, ih.2, step_add]
      exact xor_twice _ _
  funext i
  exact (pair i).1

/-- **Every row has exactly one predecessor,** so a backward tick is well defined and the theorems on predecessors are not empty. -/
theorem predecessor_unique (x : Row) : ∃ z, step z = x ∧ ∀ y, step y = x → y = z :=
  ⟨previous x, step_previous x, fun y h => by rw [← h, previous_step]⟩

/-- `n` backward ticks. -/
def previousN : Nat → Row → Row
  | 0, x => x
  | n + 1, x => previous (previousN n x)

theorem iter_previousN (x : Row) (n : Nat) : iter (previousN n x) n = x := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have e := iter_add (previousN (n + 1) x) 1 n
    rw [Nat.add_comm 1 n] at e
    rw [e]
    show iter (step (previous (previousN n x))) n = x
    rw [step_previous]; exact ih

namespace WindowClosed

/-- **A held row is not periodic**, when each window of the set ends in the wall's equal pair. -/
theorem held_not_periodic {W : Nat} {S : List (List Bool)} (C : Closed W S) (hW : 2 ≤ W)
    (wall : ∀ w, w ∈ S → w.getD (W - 2) false = w.getD (W - 1) false)
    {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held W S x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := held_forever C hL h P x hper
  have hwall := wall _ hf.1
  rw [seg_getD x W _ (W - 2) (by omega), seg_getD x W _ (W - 1) (by omega)] at hwall
  have hr := h.2 (L + 3 * P + (W - 2)) (by omega)
  rw [show L + 3 * P + (W - 2) + 1 = L + 3 * P + (W - 1) by omega, ← hwall] at hr
  cases hb : x (L + 3 * P + (W - 2)) <;> simp [hb] at hr

/-- The two letters. -/
def letterSet : List (List Bool) := [wordA, wordB]

/-- **The letters are closed.** A row showing a letter with rain above it shows a letter at every backward tick. -/
theorem letters_closed : Closed 11 letterSet :=
  ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩

/-- **After `B` comes `A`,** for every pair of lower cells. -/
theorem letter_after_B {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (hb : seg x L 11 = wordB) : seg z (L + 3) 11 = wordA := by
  rw [next_seg letters_closed hL hs h, hb]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-- **After `A` comes `A` exactly when the two cells of the predecessor below the window are white.** -/
theorem letter_after_A {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (ha : seg x L 11 = wordA) : seg z (L + 3) 11 = if (z (L - 1) || z (L - 2)) then wordB else wordA := by
  rw [next_seg letters_closed hL hs h, ha]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-! ## Windows as numbers

The checks on a closed set are finite, and the kernel runs them on numbers. A window of `W` cells is a number. `load` puts the two lower
cells under it and rain over it, `run` is the backward sweep cell by cell, and `nxt` reads the image window off the result. The theorems say
this is `next` on words. -/

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := seg n.testBit 0 W

/-- One cell of the sweep: bit `i + 2` takes the inverse rule from the two bits below it. -/
def sw (i y : Nat) : Nat := y ^^^ ((((y >>> (i + 1)) ||| (y >>> i)) &&& 1) <<< (i + 2))

/-- The sweep. The test on `sw i y` never changes the value, since `0` stays `0`; it forces each cell as the kernel reaches it. -/
def run : Nat → Nat → Nat → Nat
  | 0, _, y => y
  | f + 1, i, y => cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y))

/-- The two lower cells, the window and six cells of rain over a black top. -/
def load (W n : Nat) (p1 p2 : Bool) : Nat := ((n ||| (42 <<< W)) <<< 2) ||| (p1.toNat <<< 1) ||| p2.toNat

/-- The whole sweep on a window. -/
def image (W n : Nat) (p1 p2 : Bool) : Nat := run (W + 6) 0 (load W n p1 p2)

/-- The image window. -/
def nxt (W n : Nat) (p1 p2 : Bool) : Nat := (image W n p1 p2 >>> 5) &&& (2 ^ W - 1)

/-- The finite check on one window number: a black top cell, and under each pair of lower cells rain resumes and the image window is in `T`. -/
def Fast (W : Nat) (T : List Nat) (n : Nat) : Prop :=
  n >>> (W - 1) = 1 ∧ ∀ p1 p2 : Bool, image W n p1 p2 >>> (W + 4) = 5 ∧ nxt W n p1 p2 ∈ T

instance (W : Nat) (T : List Nat) (n : Nat) : Decidable (Fast W T n) := by unfold Fast; infer_instance

theorem sw_bit (i y j : Nat) :
    (sw i y).testBit j = if j = i + 2 then xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) else y.testBit j := by
  have hone : ∀ a : Nat, (a &&& 1).testBit 0 = a.testBit 0 := by
    intro a; simp
  have hhi : ∀ (a k : Nat), (a &&& 1).testBit (k + 1) = false := by
    intro a k; simp [Nat.testBit_succ]
  unfold sw
  rw [Nat.testBit_xor, Nat.testBit_shiftLeft]
  by_cases c : j = i + 2
  · subst c
    simp only [ge_iff_le, Nat.le_refl, decide_true, Bool.true_and, Nat.sub_self, ite_true]
    rw [hone, Nat.testBit_or, Nat.testBit_shiftRight, Nat.testBit_shiftRight]
    simp
  · rw [ite_eq_right c]
    by_cases d : i + 2 ≤ j
    · obtain ⟨k, rfl⟩ : ∃ k, j = i + 2 + (k + 1) := ⟨j - (i + 2) - 1, by omega⟩
      rw [show i + 2 + (k + 1) - (i + 2) = k + 1 by omega, hhi]
      simp
    · simp [d]

theorem run_zero (f i : Nat) : run f i 0 = 0 := by
  induction f generalizing i with
  | zero => rfl
  | succ f ih =>
    have : sw i 0 = 0 := by simp [sw]
    simp [run, this]

theorem run_succ (f i y : Nat) : run (f + 1) i y = run f (i + 1) (sw i y) := by
  show cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y)) = _
  cases h : Nat.beq (sw i y) 0 with
  | false => rfl
  | true =>
    have : sw i y = 0 := Nat.eq_of_beq_eq_true h
    rw [this, run_zero]; rfl

/-- The sweep leaves every bit below its start alone. -/
theorem run_low (f i y j : Nat) (hj : j < i + 2) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, ite_eq_right (by omega)]

/-- And every bit above its end. -/
theorem run_high (f i y j : Nat) (hj : i + 2 + f ≤ j) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, ite_eq_right (by omega)]

/-- **The sweep is `back`.** -/
theorem run_back (n i y : Nat) :
    seg (run n i y).testBit (i + 2) n = back (y.testBit (i + 1)) (y.testBit i) (seg y.testBit (i + 2) n) := by
  induction n generalizing i y with
  | zero => rfl
  | succ n ih =>
    have hseg : seg (sw i y).testBit (i + 3) n = seg y.testBit (i + 3) n := by
      have : ∀ (m L : Nat), i + 3 ≤ L → seg (sw i y).testBit L m = seg y.testBit L m := by
        intro m
        induction m with
        | zero => intro L _; rfl
        | succ m ihm =>
          intro L hL
          show (sw i y).testBit L :: seg (sw i y).testBit (L + 1) m = y.testBit L :: seg y.testBit (L + 1) m
          rw [ihm (L + 1) (by omega), sw_bit, ite_eq_right (by omega)]
      exact this n (i + 3) (Nat.le_refl _)
    have h2 : (sw i y).testBit (i + 2) = xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) := by
      rw [sw_bit, ite_eq_left rfl]
    have h1 : (sw i y).testBit (i + 1) = y.testBit (i + 1) := by
      rw [sw_bit, ite_eq_right (by omega)]
    show (run (n + 1) i y).testBit (i + 2) :: seg (run (n + 1) i y).testBit (i + 3) n =
      xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) ::
        back (xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i)) (y.testBit (i + 1)) (seg y.testBit (i + 3) n)
    rw [run_succ, run_low n (i + 1) (sw i y) (i + 2) (by omega), h2]
    have := ih (i + 1) (sw i y)
    rw [show i + 1 + 2 = i + 3 by omega, show i + 1 + 1 = i + 2 by omega, h2, h1, hseg] at this
    rw [this]

theorem load_low1 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 1 = p1 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 1 = false := by simp [Nat.testBit_shiftLeft]
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_low0 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 0 = p2 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 0 = false := by simp
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_bit (W n : Nat) (p1 p2 : Bool) (j : Nat) :
    (load W n p1 p2).testBit (j + 2) = (n.testBit j || (42 <<< W).testBit j) := by
  have e : ∀ b : Bool, (b.toNat <<< 1).testBit (j + 2) = false := by
    intro b; rw [Nat.testBit_shiftLeft]; cases b <;> simp [Nat.testBit_succ]
  have f : ∀ b : Bool, b.toNat.testBit (j + 2) = false := by
    intro b; cases b <;> simp [Nat.testBit_succ]
  simp only [load, Nat.testBit_or, e, f, Bool.or_false]
  rw [Nat.testBit_shiftLeft]
  simp [Nat.testBit_or]

theorem seg_ext {f g : Nat → Bool} (m : Nat) : ∀ L M, (∀ i, i < m → f (L + i) = g (M + i)) → seg f L m = seg g M m := by
  induction m with
  | zero => intro _ _ _; rfl
  | succ m ih =>
    intro L M h
    show f L :: seg f (L + 1) m = g M :: seg g (M + 1) m
    rw [show f L = g M from h 0 (by omega), ih (L + 1) (M + 1) (fun i hi => by
      rw [show L + 1 + i = L + (i + 1) by omega, show M + 1 + i = M + (i + 1) by omega]; exact h (i + 1) (by omega))]

/-- A number whose top bit is bit `W - 1`. -/
theorem top_facts {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) :
    n.testBit (W - 1) = true ∧ ∀ j, W ≤ j → n.testBit j = false := by
  constructor
  · have : (n >>> (W - 1)).testBit 0 = n.testBit (W - 1) := by simp
    rw [← this, hn]; rfl
  · intro j hj
    obtain ⟨k, rfl⟩ : ∃ k, j = (W - 1) + (k + 1) := ⟨j - (W - 1) - 1, by omega⟩
    have : (n >>> (W - 1)).testBit (k + 1) = n.testBit (W - 1 + (k + 1)) := by simp [Nat.testBit_shiftRight]
    rw [← this, hn]
    simp [Nat.testBit_succ]

theorem load_seg {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (load W n p1 p2).testBit 2 (W + 6) = inp W (dec W n) := by
  obtain ⟨htop, hhi⟩ := top_facts hW hn
  have split : seg (load W n p1 p2).testBit 2 (W + 6) =
      seg (load W n p1 p2).testBit 2 (W - 1) ++ seg (load W n p1 p2).testBit (2 + (W - 1)) 7 := by
    rw [← seg_append]; congr 1; omega
  have hlow : ∀ j, j < W → (42 <<< W).testBit j = false := by
    intro j hj; simp [Nat.testBit_shiftLeft]; omega
  have htake : (dec W n).take (W - 1) = seg n.testBit 0 (W - 1) := by
    have e1 : dec W n = seg n.testBit 0 (W - 1) ++ seg n.testBit (0 + (W - 1)) 1 := by
      rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
    rw [e1]; exact List.take_left' (seg_length _ _ _)
  have hget : (dec W n).getD (W - 1) false = true := by
    have := seg_getD n.testBit W 0 (W - 1) (by omega)
    rw [Nat.zero_add] at this
    show (seg n.testBit 0 W).getD (W - 1) false = true
    rw [this, htop]
  have a1 : seg (load W n p1 p2).testBit 2 (W - 1) = seg n.testBit 0 (W - 1) := by
    have g : ∀ (m L : Nat), L + m ≤ W → seg (load W n p1 p2).testBit (L + 2) m = seg n.testBit L m := by
      intro m
      induction m with
      | zero => intro _ _; rfl
      | succ m ih =>
        intro L hLm
        show (load W n p1 p2).testBit (L + 2) :: seg (load W n p1 p2).testBit (L + 2 + 1) m = n.testBit L :: seg n.testBit (L + 1) m
        rw [load_bit, hlow L (by omega), Bool.or_false, show L + 2 + 1 = L + 1 + 2 by omega, ih (L + 1) (by omega)]
    exact g (W - 1) 0 (by omega)
  have a2 : seg (load W n p1 p2).testBit (2 + (W - 1)) 7 = alt true 7 := by
    have bit : ∀ k, k < 7 → (load W n p1 p2).testBit (2 + (W - 1) + k) = (alt true 7).getD k false := by
      intro k hk
      rw [show 2 + (W - 1) + k = (W - 1 + k) + 2 by omega, load_bit]
      have hs : ∀ m : Nat, (42 <<< W).testBit (W + m) = (42 : Nat).testBit m := by
        intro m; simp [Nat.testBit_shiftLeft]
      match k, hk with
      | 0, _ => rw [show W - 1 + 0 = W - 1 by omega, htop]; rfl
      | 1, _ => rw [show W - 1 + 1 = W + 0 by omega, hhi _ (by omega), hs]; rfl
      | 2, _ => rw [show W - 1 + 2 = W + 1 by omega, hhi _ (by omega), hs]; rfl
      | 3, _ => rw [show W - 1 + 3 = W + 2 by omega, hhi _ (by omega), hs]; rfl
      | 4, _ => rw [show W - 1 + 4 = W + 3 by omega, hhi _ (by omega), hs]; rfl
      | 5, _ => rw [show W - 1 + 5 = W + 4 by omega, hhi _ (by omega), hs]; rfl
      | 6, _ => rw [show W - 1 + 6 = W + 5 by omega, hhi _ (by omega), hs]; rfl
    have eq : ∀ (m : Nat) (l : List Bool) (L : Nat), l.length = m →
        (∀ k, k < m → (load W n p1 p2).testBit (L + k) = l.getD k false) → seg (load W n p1 p2).testBit L m = l := by
      intro m
      induction m with
      | zero => intro l _ hl _; cases l with
        | nil => rfl
        | cons _ _ => simp at hl
      | succ m ih =>
        intro l L hl h
        cases l with
        | nil => simp at hl
        | cons b r =>
          show (load W n p1 p2).testBit L :: seg (load W n p1 p2).testBit (L + 1) m = b :: r
          have h0 := h 0 (by omega)
          simp only [Nat.add_zero, List.getD_cons_zero] at h0
          rw [h0, ih r (L + 1) (by simpa using hl) (fun k hk => by
            have := h (k + 1) (by omega)
            rw [show L + (k + 1) = L + 1 + k by omega] at this
            simpa using this)]
    exact eq 7 _ _ rfl bit
  rw [split, a1, a2]
  show _ = (dec W n).take (W - 1) ++ alt ((dec W n).getD (W - 1) false) 7
  rw [htake, hget]

/-- The sweep is `back` on the loaded window. -/
theorem image_back {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (image W n p1 p2).testBit 2 (W + 6) = back p1 p2 (inp W (dec W n)) := by
  have := run_back (W + 6) 0 (load W n p1 p2)
  rw [show (0 : Nat) + 2 = 2 from rfl, show (0 : Nat) + 1 = 1 from rfl, load_low1, load_low0, load_seg hW hn] at this
  exact this

theorem next_fast {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    next W (dec W n) p1 p2 = dec W (nxt W n p1 p2) := by
  show ((back p1 p2 (inp W (dec W n))).drop 3).take W = _
  rw [← image_back hW hn]
  have e1 : seg (image W n p1 p2).testBit 2 (W + 6) =
      seg (image W n p1 p2).testBit 2 3 ++ seg (image W n p1 p2).testBit (2 + 3) (W + 3) := by
    rw [← seg_append]; congr 1; omega
  have e2 : seg (image W n p1 p2).testBit (2 + 3) (W + 3) =
      seg (image W n p1 p2).testBit (2 + 3) W ++ seg (image W n p1 p2).testBit (2 + 3 + W) 3 := seg_append _ _ _ _
  rw [e1, List.drop_left' (seg_length _ _ _), e2, List.take_left' (seg_length _ _ _)]
  refine seg_ext W _ _ (fun i hi => ?_)
  show (image W n p1 p2).testBit (2 + 3 + i) = ((image W n p1 p2 >>> 5) &&& (2 ^ W - 1)).testBit (0 + i)
  rw [Nat.testBit_and, Nat.testBit_shiftRight, Nat.testBit_two_pow_sub_one]
  simp only [Nat.zero_add]
  rw [show 5 + i = 2 + 3 + i by omega]
  simp [hi]

/-- **A closed set from numbers.** -/
theorem closed_fast {W : Nat} (hW : 1 ≤ W) (S : List Nat) (h : ∀ n, n ∈ S → Fast W S n) : Closed W (S.map (dec W)) := by
  have bits : ∀ n, n ∈ S → ∀ (p1 p2 : Bool) (k : Nat), k < 4 →
      (back p1 p2 (inp W (dec W n))).getD (W + 2 + k) false = (5 : Nat).testBit k := by
    intro n hn p1 p2 k hk
    have ok := ((h n hn).2 p1 p2).1
    rw [← image_back hW (h n hn).1, seg_getD _ _ _ _ (by omega), ← ok, Nat.testBit_shiftRight]
    rw [show 2 + (W + 2 + k) = W + 4 + k by omega]
  have rain : ∀ n, n ∈ S → ∀ (k : Nat), k < 2 → (inp W (dec W n)).getD (W + 4 + k) false = (42 : Nat).testBit (4 + k) := by
    intro n hn k hk
    rw [← load_seg hW (h n hn).1 false false, seg_getD _ _ _ _ (by omega), show 2 + (W + 4 + k) = (W + (4 + k)) + 2 by omega, load_bit]
    have hi := (top_facts hW (h n hn).1).2 (W + (4 + k)) (by omega)
    rw [hi]
    simp [Nat.testBit_shiftLeft]
  have sub : ∀ w, w ∈ S.map (dec W) → ∃ n, n ∈ S ∧ w = dec W n := by
    intro w hw
    obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
    exact ⟨n, hn, rfl⟩
  refine ⟨hW, ?_, ?_, ?_, ?_, ?_⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    rw [next_fast hW (h n hn).1]
    exact List.mem_map.2 ⟨_, ((h n hn).2 p1 p2).2, rfl⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b0 := bits n hn p1 p2 0 (by omega)
    have b1 := bits n hn p1 p2 1 (by omega)
    rw [show W + 2 + 0 = W + 2 by omega] at b0
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [b0, b1]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b1 := bits n hn p1 p2 1 (by omega)
    have b2 := bits n hn p1 p2 2 (by omega)
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [b1, b2]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b2 := bits n hn p1 p2 2 (by omega)
    have r0 := rain n hn 0 (by omega)
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [show W + 4 + 0 = W + 4 by omega] at r0
    rw [b2, r0]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b3 := bits n hn p1 p2 3 (by omega)
    have r1 := rain n hn 1 (by omega)
    rw [show W + 2 + 3 = W + 5 by omega] at b3
    rw [show W + 4 + 1 = W + 5 by omega] at r1
    rw [b3, r1]; decide

/-- The cells of a word above `k`, from the number. -/
theorem dec_drop (W k n : Nat) (hk : k ≤ W) : (dec W n).drop k = dec (W - k) (n >>> k) := by
  have e : dec W n = seg n.testBit 0 k ++ seg n.testBit (0 + k) (W - k) := by
    rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
  rw [e, List.drop_left' (seg_length _ _ _)]
  refine seg_ext (W - k) _ _ (fun i _ => ?_)
  simp [Nat.testBit_shiftRight]

theorem wordA_dec : wordA = dec 11 1596 := by decide
theorem wordB_dec : wordB = dec 11 1594 := by decide

/-- The word above cell `L + k` of a window, read on the row. -/
theorem seg_drop (x : Row) (L W k : Nat) (hk : k ≤ W) : (seg x L W).drop k = seg x (L + k) (W - k) := by
  have e : seg x L W = seg x L k ++ seg x (L + k) (W - k) := by
    rw [← seg_append]; congr 1; omega
  rw [e, List.drop_left' (seg_length x k L)]

theorem Fast.mono {W n : Nat} {T U : List Nat} (h : ∀ m, m ∈ T → m ∈ U) (f : Fast W T n) : Fast W U n :=
  ⟨f.1, fun p1 p2 => ⟨(f.2 p1 p2).1, h _ (f.2 p1 p2).2⟩⟩

/-- A word of `W` cells from a number whose top letter is `A` or `B` ends in the wall's equal pair. -/
theorem wall_of_letter {W n : Nat} (hW : 11 ≤ W) (h : n >>> (W - 11) = 1596 ∨ n >>> (W - 11) = 1594) :
    (dec W n).getD (W - 2) false = (dec W n).getD (W - 1) false := by
  have g1 := seg_getD n.testBit W 0 (W - 2) (by omega)
  have g2 := seg_getD n.testBit W 0 (W - 1) (by omega)
  rw [Nat.zero_add] at g1 g2
  show (seg n.testBit 0 W).getD (W - 2) false = (seg n.testBit 0 W).getD (W - 1) false
  rw [g1, g2]
  have e1 : n.testBit (W - 2) = (n >>> (W - 11)).testBit 9 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 9 = W - 2 by omega]
  have e2 : n.testBit (W - 1) = (n >>> (W - 11)).testBit 10 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 10 = W - 1 by omega]
  rw [e1, e2]
  rcases h with h | h <;> rw [h] <;> decide

/-- A lock: window numbers in `k` phases, each phase going to the next for every pair of lower cells. -/
structure Lock (W k : Nat) (Ph : List (List Nat)) (All : List Nat) : Prop where
  width : 11 ≤ W
  period : 0 < k
  cycle : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → Fast W (Ph.getD ((r + 1) % k) []) n
  sub : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → n ∈ All
  cover : ∀ n, n ∈ All → ∃ r, r < k ∧ n ∈ Ph.getD r []

namespace Lock
variable {W k : Nat} {Ph : List (List Nat)} {All : List Nat}

theorem closed (H : Lock W k Ph All) : Closed W (All.map (dec W)) :=
  closed_fast (by have := H.width; omega) All (fun n hn => by
    obtain ⟨r, hr, hm⟩ := H.cover n hn
    exact Fast.mono (H.sub _ (Nat.mod_lt _ H.period)) (H.cycle r hr n hm))

theorem phase (H : Lock W k Ph All) {x : Row} {L : Nat} (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ seg x L W ∈ (Ph.getD r []).map (dec W) := by
  obtain ⟨n, hn, e⟩ := List.mem_map.1 h.1
  obtain ⟨r, hr, hm⟩ := H.cover n hn
  exact ⟨r, hr, List.mem_map.2 ⟨n, hm, e⟩⟩

/-- **The phases follow each other for ever,** whatever lies below the window. -/
theorem forever (H : Lock W k Ph All) {x : Row} {L r : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L)
    (hp : seg x L W ∈ (Ph.getD (r % k) []).map (dec W)) :
    ∀ n z, iter z n = x → seg z (L + 3 * n) W ∈ (Ph.getD ((r + n) % k) []).map (dec W) := by
  have hW : 1 ≤ W := by have := H.width; omega
  intro n
  induction n with
  | zero =>
    intro z hz
    have e : z = x := hz
    subst e
    exact hp
  | succ n ih =>
    intro z hz
    have e : iter (step z) n = x := by
      have := iter_add z 1 n
      rw [Nat.add_comm 1 n] at this
      rw [← hz, this]; rfl
    obtain ⟨m, hm, em⟩ := List.mem_map.1 (ih (step z) e)
    have hy := held_forever H.closed hL h n (step z) e
    have q := next_seg H.closed (L := L + 3 * n) (by omega) rfl hy
    rw [← em, next_fast hW (H.cycle _ (Nat.mod_lt _ H.period) m hm).1] at q
    rw [show L + 3 * (n + 1) = L + 3 * n + 3 by omega, q]
    refine List.mem_map.2 ⟨_, ?_, rfl⟩
    have := ((H.cycle _ (Nat.mod_lt _ H.period) m hm).2 (z (L + 3 * n - 1)) (z (L + 3 * n - 2))).2
    rw [Nat.mod_add_mod] at this
    exact this

/-- **The letters run through the phases for ever.** -/
theorem letters (H : Lock W k Ph All) (lc : Nat → List Bool)
    (hl : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> (W - 11)) = lc r)
    {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + (W - 11)) 11 = lc ((r + n) % k) := by
  have hW := H.width
  obtain ⟨r, hr, hp⟩ := H.phase h
  refine ⟨r, hr, fun n z hz => ?_⟩
  have hp' : seg x L W ∈ (Ph.getD (r % k) []).map (dec W) := by rwa [Nat.mod_eq_of_lt hr]
  obtain ⟨m, hm, em⟩ := List.mem_map.1 (H.forever hL h hp' n z hz)
  have d1 := seg_drop z (L + 3 * n) W (W - 11) (by omega)
  rw [show W - (W - 11) = 11 by omega, ← em, dec_drop W (W - 11) m (by omega), show W - (W - 11) = 11 by omega] at d1
  rw [← d1]
  exact hl _ (Nat.mod_lt _ H.period) m hm

end Lock

/-- A row with the window `n` on a black edge, one white cell below it, and rain above it. -/
def anchor (W n j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false else if j < W + 2 then n.testBit (j - 2) else decide ((j - W) % 2 = 1)

/-- **Every window of a set occurs on an anchored row.** -/
theorem anchor_held {W n : Nat} {S : List (List Bool)} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (hm : dec W n ∈ S) :
    anchor W n 0 = true ∧ Held W S (anchor W n) 2 := by
  have htop := (top_facts hW hn).1
  have hs : seg (anchor W n) 2 W = dec W n := by
    refine seg_ext W 2 0 (fun i hi => ?_)
    simp [anchor, show ¬2 + i = 1 by omega, show 2 + i < W + 2 by omega]
  refine ⟨rfl, by rw [hs]; exact hm, fun j hj => ?_⟩
  by_cases c : j = W + 1
  · subst c
    have a1 : anchor W n (W + 1) = true := by
      simp only [anchor, show ¬W + 1 = 0 by omega, show ¬W + 1 = 1 by omega, show W + 1 < W + 2 by omega, ite_false, ite_true]
      rw [show W + 1 - 2 = W - 1 by omega]; exact htop
    have a2 : anchor W n (W + 1 + 1) = false := by
      simp only [anchor, show ¬W + 1 + 1 = 0 by omega, show ¬W + 1 + 1 = 1 by omega, show ¬W + 1 + 1 < W + 2 by omega, ite_false]
      rw [show W + 1 + 1 - W = 2 by omega]; rfl
    rw [a1, a2]; rfl
  · have q : W + 2 ≤ j := by omega
    simp only [anchor, show ¬j = 0 by omega, show ¬j + 1 = 0 by omega, show ¬j = 1 by omega, show ¬j + 1 = 1 by omega,
      show ¬j < W + 2 by omega, show ¬j + 1 < W + 2 by omega, ite_false]
    by_cases a : (j - W) % 2 = 1
    · have b : ¬(j + 1 - W) % 2 = 1 := by omega
      simp [a, b]
    · have b : (j + 1 - W) % 2 = 1 := by omega
      simp [a, b]

/-! ## Forward ticks on numbers -/

/-- One tick on a number: exactly the edge map. -/
def fw (y : Nat) : Nat := y ^^^ ((y <<< 1) ||| (y <<< 2))

def fwN : Nat → Nat → Nat
  | 0, y => y
  | k + 1, y => fw (fwN k y)

theorem fw_bit (y : Nat) : (fw y).testBit = step y.testBit := by
  funext j
  match j with
  | 0 => simp [fw, T]
  | 1 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]
  | j + 2 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]

theorem iter_fw (y k : Nat) : iter y.testBit k = (fwN k y).testBit := by
  induction k with
  | zero => rfl
  | succ k ih =>
    show step (iter y.testBit k) = _
    rw [ih]; exact (fw_bit _).symm

/-- Two rows that agree below `N` keep agreeing below `N`. -/
theorem iter_low {x y : Row} {N : Nat} (h : ∀ j, j < N → x j = y j) (k : Nat) : ∀ j, j < N → iter x k j = iter y k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    show step (iter x k) j = step (iter y k) j
    match j, hj with
    | 0, hj => exact ih 0 hj
    | 1, hj =>
      show xor _ _ = xor _ _
      rw [ih 1 hj, ih 0 (by omega)]
    | j + 2, hj =>
      show xor _ (_ || _) = xor _ (_ || _)
      rw [ih (j + 2) hj, ih (j + 1) (by omega), ih j (by omega)]

/-- A rain tail above `D` is a rain tail above `D + 2 k` after `k` ticks. -/
theorem iter_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) (k : Nat) :
    ∀ j, D + 2 * k ≤ j → iter x k (j + 1) = !iter x k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    exact step_rain_tail ih j (by omega)

end WindowClosed

end Ruliology.CellularAutomata.Rule30RightWall
