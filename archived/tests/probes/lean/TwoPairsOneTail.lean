import LeakDescent

/-!
An exact test for whether two low prefixes admit a confined pair over one
common upper tail. Indices n=k+2 allow direct use of the interior edge rule.
The argument applies to arbitrary rows, including black-edge rows.
-/
namespace TwoPairsOneTail

open CanonicalDecoration LeakDescent
open Ruliology.CellularAutomata.Rule30FrozenRuler

def top (k : Nat) (x : Code) (t : Nat) : Bool := iter t x (k+1)

def driver (k : Nat) (x : Code) (t : Nat) : Bool :=
  top k x t || iter t x k

/-- Parity of the driver up to, and excluding, tick t. -/
def cumulative (v : Nat → Bool) : Nat → Bool
  | 0 => false
  | t+1 => xor (cumulative v t) (v t)

private theorem digit_value (k : Nat) (x : Code) (t : Nat) :
    iter t x (k+2) = xor (x (k+2)) (cumulative (driver k x) t) := by
  induction t with
  | zero => change x (k+2) = xor (x (k+2)) false; cases x (k+2) <;> rfl
  | succ t ih =>
    change xor (iter t x (k+2)) (driver k x t) =
      xor (x (k+2)) (xor (cumulative (driver k x) t) (driver k x t))
    rw [ih]
    cases x (k+2) <;> cases cumulative (driver k x) t <;> cases driver k x t <;> rfl

private theorem cancel {a b c : Bool} (h : xor a b = xor a c) : b = c := by
  cases a <;> cases b <;> cases c <;> simp_all

private theorem masked {a u v : Bool} (ne : u ≠ v) (h : (a || u) = (a || v)) :
    a = true := by
  cases a <;> cases u <;> cases v <;> simp_all

/-- On a prescribed common upper tail, only its first digit affects confinement.
The driver words must match; every disagreement of their top input must occur
when the first upper digit is black. -/
theorem fixed_tail_iff (k : Nat) (x y : Code) (initial : InitialTail (k+1) x y) :
    Confined (k+1) 0 x y ↔
      (∀ t, driver k x t = driver k y t) ∧
      (∀ t, top k x t ≠ top k y t →
        xor (x (k+2)) (cumulative (driver k x) t) = true) := by
  constructor
  · intro confined
    have first (t : Nat) : iter t x (k+2) = iter t y (k+2) :=
      (confined t (k+2) (by omega)).symm
    have second (t : Nat) : iter t x (k+3) = iter t y (k+3) :=
      (confined t (k+3) (by omega)).symm
    constructor
    · intro t
      have h := first (t+1)
      change xor (iter t x (k+2)) (driver k x t) =
        xor (iter t y (k+2)) (driver k y t) at h
      rw [← first t] at h
      exact cancel h
    · intro t ne
      have h := second (t+1)
      change xor (iter t x (k+3)) (iter t x (k+2) || top k x t) =
        xor (iter t y (k+3)) (iter t y (k+2) || top k y t) at h
      rw [← second t, ← first t] at h
      rw [← digit_value]
      exact masked ne (cancel h)
  · rintro ⟨v, mask⟩
    have words : driver k x = driver k y := funext v
    have first (t : Nat) : iter t x (k+2) = iter t y (k+2) := by
      simp only [digit_value, initial (k+2) (by omega), words]
    have second (t : Nat) : iter t x (k+3) = iter t y (k+3) := by
      induction t with
      | zero => exact initial (k+3) (by omega)
      | succ t ih =>
        change xor (iter t x (k+3)) (iter t x (k+2) || top k x t) =
          xor (iter t y (k+3)) (iter t y (k+2) || top k y t)
        rw [ih, ← first t]
        by_cases same : top k x t = top k y t
        · rw [same]
        · have black := (digit_value k x t).trans (mask t same)
          rw [black] <;> simp
    exact (confined_iff_interfaces (k+1) x y).mpr
      ⟨initial, fun t => ⟨first t, second t⟩⟩

/-- The tail uses absolute digit positions. Only its entries at j≥k+2 are read. -/
def attach (k : Nat) (x z : Code) (j : Nat) : Bool :=
  if j < k+2 then x j else z j

private theorem attached_words (k : Nat) (x z : Code) :
    top k (attach k x z) = top k x ∧ driver k (attach k x z) = driver k x := by
  have low : AgreeBelow (k+2) (attach k x z) x := by
    intro i hi
    simp [attach, hi]
  have at_top (t : Nat) : top k (attach k x z) t = top k x t :=
    iter_agree low t (k+1) (by omega)
  exact ⟨funext at_top, funext (fun t => by
    unfold driver
    rw [at_top, iter_agree low t k (by omega)])⟩

/-- Some common tail works exactly when one choice of its first digit masks
all top disagreements. Equivalently the accumulated common driver has a
single parity on the disagreement times (including the empty case). -/
theorem some_tail_iff (k : Nat) (x y : Code) :
    (∃ z : Code, Confined (k+1) 0 (attach k x z) (attach k y z)) ↔
      (∀ t, driver k x t = driver k y t) ∧
      (∃ a : Bool, ∀ t, top k x t ≠ top k y t →
        xor a (cumulative (driver k x) t) = true) := by
  have criterion (z : Code) :
      Confined (k+1) 0 (attach k x z) (attach k y z) ↔
        (∀ t, driver k x t = driver k y t) ∧
        (∀ t, top k x t ≠ top k y t →
          xor (z (k+2)) (cumulative (driver k x) t) = true) := by
    have initial : InitialTail (k+1) (attach k x z) (attach k y z) := by
      intro j hj
      simp [attach, show ¬j < k+2 by omega]
    have cut : attach k x z (k+2) = z (k+2) := by simp [attach]
    simpa only [(attached_words k x z).1, (attached_words k x z).2,
      (attached_words k y z).1, (attached_words k y z).2, cut] using
      fixed_tail_iff k (attach k x z) (attach k y z) initial
  constructor
  · rintro ⟨z, h⟩
    obtain ⟨words, mask⟩ := (criterion z).mp h
    exact ⟨words, z (k+2), mask⟩
  · rintro ⟨words, a, mask⟩
    exact ⟨fun _ => a, (criterion (fun _ => a)).mpr ⟨words, mask⟩⟩

end TwoPairsOneTail
