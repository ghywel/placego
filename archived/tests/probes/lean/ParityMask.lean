import Mathlib

/-!
# G.GPT269 (GPT's GC846), machine-checked core (Local, 2026-10-09)

GC846: for odd period q, a periodic spatial parity mask leaves every vertex of the lifted profile graph with at most
one incoming edge, so the live set (vertices with an infinite forward path) is a union of cycles, and an odd-driver
entry (no predecessor at all) cannot start a tail whose parity mask is purely periodic.

Formalized here:
- `live_has_pred`: in a finite type, if every live vertex has a successor that is live and every vertex has at most
  one predecessor, then every live vertex has a live predecessor (the degree count of GC846, step 3).
- `diff_eq_cases`: two cyclic words with the same difference word Δ (Δ A t = A t xor A (t + 1)) are equal or
  complementary (GC846, step 2).
- `parity_compl`: complementing a word of odd length flips its black parity; so a prescribed parity admits at most one
  of A and its complement (`at_most_one_pred`).
- `diff_even`, `odd_driver_no_pred`: a difference word has even weight, so an odd-weight driver D or U has no
  predecessor (GC816, used at GC846's critical entry).

How to check: as for RootedReturn.lean; the `#print axioms` lines must list no `sorryAx`.
-/

namespace ParityMask

/-- The counting core: live vertices with live successors and unique predecessors all have live predecessors. -/
theorem live_has_pred {S : Type*} [Finite S] (L : Set S) (R : S → S → Prop)
    (hout : ∀ v ∈ L, ∃ w ∈ L, R v w)
    (hin : ∀ v v' w, R v w → R v' w → v = v') :
    ∀ w ∈ L, ∃ v ∈ L, R v w := by
  classical
  choose f hfL hfR using hout
  let g : L → L := fun v => ⟨f v.1 v.2, hfL v.1 v.2⟩
  have ginj : Function.Injective g := by
    intro a b hab
    have h : f a.1 a.2 = f b.1 b.2 := congrArg Subtype.val hab
    apply Subtype.ext
    exact hin a.1 b.1 (f b.1 b.2) (h ▸ hfR a.1 a.2) (hfR b.1 b.2)
  have gsurj : Function.Surjective g := Finite.injective_iff_surjective.mp ginj
  intro w hw
  obtain ⟨v, hv⟩ := gsurj ⟨w, hw⟩
  refine ⟨v.1, v.2, ?_⟩
  have : f v.1 v.2 = w := congrArg Subtype.val hv
  exact this ▸ hfR v.1 v.2

/-- The cyclic difference word. -/
def diff {q : ℕ} (A : ZMod q → Bool) : ZMod q → Bool := fun t => xor (A t) (A (t + 1))

/-- Equal differences: the two words are equal or complementary. -/
theorem diff_eq_cases {q : ℕ} [NeZero q] (A A' : ZMod q → Bool) (h : diff A = diff A') :
    A' = A ∨ A' = fun t => !A t := by
  -- D = A xor A' is invariant under t -> t + 1, hence constant
  have step : ∀ t, xor (A (t + 1)) (A' (t + 1)) = xor (A t) (A' t) := by
    intro t
    have := congrFun h t
    simp only [diff] at this
    cases ha : A t <;> cases ha' : A' t <;> cases hb : A (t + 1) <;> cases hb' : A' (t + 1) <;> simp_all
  have const : ∀ k : ℕ, xor (A (0 + k)) (A' (0 + k)) = xor (A 0) (A' 0) := by
    intro k
    induction k with
    | zero => simp
    | succ k ih => rw [show ((0 : ZMod q) + ((k + 1 : ℕ) : ZMod q)) = (0 + k) + 1 by push_cast; ring, step, ih]
  have all : ∀ t, xor (A t) (A' t) = xor (A 0) (A' 0) := by
    intro t
    have := const t.val
    rwa [zero_add, ZMod.natCast_zmod_val] at this
  cases h0 : xor (A 0) (A' 0)
  · left; funext t; have h1 := all t; rw [h0] at h1; revert h1; cases A t <;> cases A' t <;> simp
  · right; funext t; have h1 := all t; rw [h0] at h1; revert h1; cases A t <;> cases A' t <;> simp

/-- Black parity of a word. -/
def parity {q : ℕ} [NeZero q] (A : ZMod q → Bool) : Bool :=
  decide ((Finset.univ.filter fun t => A t = true).card % 2 = 1)

/-- Complementing a word of odd length flips its parity. -/
theorem parity_compl {q : ℕ} [NeZero q] (hq : q % 2 = 1) (A : ZMod q → Bool) :
    parity (fun t => !A t) = !parity A := by
  have hsplit : (Finset.univ.filter fun t => (!A t) = true).card +
      (Finset.univ.filter fun t => A t = true).card = q := by
    have h := Finset.card_filter_add_card_filter_not (s := (Finset.univ : Finset (ZMod q))) (fun t => A t = true)
    rw [Finset.card_univ, ZMod.card] at h
    have e : (Finset.univ.filter fun t => (!A t) = true) = (Finset.univ.filter fun t => ¬ (A t = true)) := by
      ext t; simp
    rw [e]; omega
  unfold parity
  set cA := (Finset.univ.filter fun t => A t = true).card
  set cB := (Finset.univ.filter fun t => (!A t) = true).card
  have key : (cB % 2 = 1) ↔ ¬ (cA % 2 = 1) := by omega
  by_cases h : cA % 2 = 1 <;> simp [h, key]

/-- GC846's unique predecessor: two solutions of the same difference equation with the same parity, at odd q,
are equal. -/
theorem at_most_one_pred {q : ℕ} [NeZero q] (hq : q % 2 = 1) (A A' : ZMod q → Bool)
    (h : diff A = diff A') (hp : parity A = parity A') : A = A' := by
  rcases diff_eq_cases A A' h with h1 | h1
  · exact h1.symm
  · exfalso
    rw [h1, parity_compl hq] at hp
    cases hpa : parity A <;> simp_all

/-- A cyclic difference word has even weight (the sum telescopes round the cycle). -/
theorem diff_even {q : ℕ} [NeZero q] (A : ZMod q → Bool) :
    (∑ t, (if diff A t then (1 : ZMod 2) else 0)) = 0 := by
  have hx : ∀ t, (if diff A t then (1 : ZMod 2) else 0) =
      (if A t then 1 else 0) + (if A (t + 1) then 1 else 0) := by
    intro t
    have key : ∀ a b : Bool, (if (xor a b) = true then (1 : ZMod 2) else 0) =
        (if a = true then 1 else 0) + (if b = true then 1 else 0) := by decide
    exact key (A t) (A (t + 1))
  simp_rw [hx, Finset.sum_add_distrib]
  have shift : (∑ t : ZMod q, (if A (t + 1) then (1 : ZMod 2) else 0)) = ∑ t, (if A t then 1 else 0) :=
    Fintype.sum_equiv (Equiv.addRight 1) _ _ (fun t => rfl)
  rw [shift, ← two_mul]
  have : (2 : ZMod 2) = 0 := rfl
  rw [this, zero_mul]

/-- GC846's entry: a driver word of odd weight has no predecessor, since no difference word equals it. -/
theorem odd_driver_no_pred {q : ℕ} [NeZero q] (B : ZMod q → Bool)
    (hB : (∑ t, (if B t then (1 : ZMod 2) else 0)) = 1) (A : ZMod q → Bool) : diff A ≠ B := by
  intro h
  have := diff_even A
  rw [h, hB] at this
  exact absurd this (by decide)

end ParityMask

#print axioms ParityMask.live_has_pred
#print axioms ParityMask.diff_eq_cases
#print axioms ParityMask.parity_compl
#print axioms ParityMask.at_most_one_pred
#print axioms ParityMask.diff_even
#print axioms ParityMask.odd_driver_no_pred
