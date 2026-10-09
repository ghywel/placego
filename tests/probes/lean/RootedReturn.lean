import Mathlib

/-!
# Every rooted walk returns (Local's formalization, 2026-10-09; the hand proof is chat L487)

The rooted walks of S84 / RC88 / RW (rule30_r88_census.py, rule30_rooted_walk.c) step a pair of q-periodic profiles
(x, y) to (y, c), where the child c solves c(t + 1) = x(t) xor (y(t) or c(t)) cyclically. L487's argument: the step is
injective (x is recovered from y and c), a nonzero driver y has exactly one child, and the walk starts at a state with
no predecessor among nonzero-driver states; a finite set then forces a return (a zero child).

This file proves the abstract core: an injective partial map on a finite type, iterated from a point with no
preimage, reaches `none`. It also proves the injectivity of the profile step: equal (y, c) give equal x. The
uniqueness of the child for a nonzero driver (the reset argument) is not formalized here.

How to check: copy into the formal-conjectures checkout used for Rule30Period1.lean (Mathlib available) and run
`lake env lean LocalScratch/RootedReturn.lean`; the `#print axioms` lines must list no `sorryAx`.
-/

namespace RootedReturn

/-- The orbit of `s0` under a partial map, as long as it is defined. -/
def orbit {S : Type*} (f : S → Option S) (s0 : S) : ℕ → Option S
  | 0 => some s0
  | n + 1 => (orbit f s0 n).bind f

/-- An injective partial map on a finite type, started at a point with no preimage, terminates. -/
theorem terminates {S : Type*} [Finite S] (f : S → Option S)
    (hinj : ∀ x x' y, f x = some y → f x' = some y → x = x')
    (s0 : S) (hs0 : ∀ x, f x ≠ some s0) :
    ∃ n, orbit f s0 n = none := by
  by_contra hne
  push Not at hne
  -- every orbit point is defined
  have hdef : ∀ n, ∃ s, orbit f s0 n = some s := fun n => Option.ne_none_iff_exists'.mp (hne n)
  choose g hg using hdef
  have hstep : ∀ n, f (g n) = some (g (n + 1)) := by
    intro n
    have h := hg (n + 1)
    simpa [orbit, hg n] using h
  have hg0 : g 0 = s0 := by
    have h := hg 0
    simp only [orbit, Option.some.injEq] at h
    exact h.symm
  -- g is not injective on ℕ, since S is finite
  obtain ⟨i, j, hij, heq⟩ := Finite.exists_ne_map_eq_of_infinite g
  -- take a pair with the least smaller index
  have key : ∀ m, ∀ i j, i < j → g i = g j → i ≠ m := by
    intro m
    induction m with
    | zero =>
      intro i j hlt heq h0
      subst h0
      obtain ⟨k, rfl⟩ : ∃ k, j = k + 1 := ⟨j - 1, by omega⟩
      exact hs0 (g k) (by rw [hstep k, ← heq, hg0])
    | succ m ih =>
      intro i j hlt heq hm
      subst hm
      obtain ⟨k, rfl⟩ : ∃ k, j = k + 1 := ⟨j - 1, by omega⟩
      have h1 : f (g m) = some (g (m + 1)) := hstep m
      have h2 : f (g k) = some (g (k + 1)) := hstep k
      rw [heq] at h1
      have hmk : g m = g k := hinj _ _ _ h1 h2
      exact ih m k (by omega) hmk rfl
  rcases Nat.lt_or_gt_of_ne hij with h | h
  · exact key i i j h heq rfl
  · exact key j j i h heq.symm rfl

/-- The profile step: the child `c` of the pair `(x, y)` satisfies `c (t + 1) = xor (x t) (y t || c t)` (indices
modulo `q`). Then `x` is determined by `y` and `c`: two parents with the same `(y, c)` are equal. -/
theorem step_injective {q : ℕ} [NeZero q] (x x' y c : ZMod q → Bool)
    (hx : ∀ t, c (t + 1) = xor (x t) (y t || c t))
    (hx' : ∀ t, c (t + 1) = xor (x' t) (y t || c t)) : x = x' := by
  funext t
  have h1 := hx t
  have h2 := hx' t
  rw [h1] at h2
  cases hxt : x t <;> cases hx't : x' t <;> cases y t <;> cases c t <;> simp_all

end RootedReturn

#print axioms RootedReturn.terminates
#print axioms RootedReturn.step_injective
