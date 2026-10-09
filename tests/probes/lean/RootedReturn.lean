import Mathlib

/-!
# Every rooted walk returns (Local's formalization, 2026-10-09; the hand proof is chat L487)

The rooted walks of S84 / RC88 / RW (rule30_r88_census.py, rule30_rooted_walk.c) step a pair of q-periodic profiles
(x, y) to (y, c), where the child c solves c(t + 1) = x(t) xor (y(t) or c(t)) cyclically. L487's argument: the step is
injective (x is recovered from y and c), a nonzero driver y has exactly one child, and the walk starts at a state with
no predecessor among nonzero-driver states; a finite set then forces a return (a zero child).

This file proves all of it, for every period q > 0 (not only dyadic q):
- `terminates`: an injective partial map on a finite type, iterated from a point with no preimage, reaches `none`;
- `step_injective`: equal (y, c) give equal parents x;
- `child_unique`, `child_exists`: a driver y that is black somewhere has exactly one cyclic child (the reset);
- `rooted_walk_returns`: from (0, c) with c nonzero, the walk by unique children reaches a zero child.
The step uses the census's convention, c (t + 1) = xor (x t) (y t || c t), which is `children()` in
rule30_r88_census.py with x = a and y = b. The rooted start (a, 0) has driver 0, and its nonzero children c give
exactly the states (0, c) covered here.

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

/-- Reset uniqueness: if the driver `y` is black at some tick `t0`, the cyclic child is unique. -/
theorem child_unique {q : ℕ} [NeZero q] (x y c c' : ZMod q → Bool) (t0 : ZMod q) (hy : y t0 = true)
    (hc : ∀ t, c (t + 1) = xor (x t) (y t || c t))
    (hc' : ∀ t, c' (t + 1) = xor (x t) (y t || c' t)) : c = c' := by
  -- agreement at t0 + 1, then along the cycle
  have base : c (t0 + 1) = c' (t0 + 1) := by rw [hc, hc', hy]; simp
  have run : ∀ k : ℕ, c (t0 + 1 + k) = c' (t0 + 1 + k) := by
    intro k
    induction k with
    | zero => simpa using base
    | succ k ih =>
      have e : t0 + 1 + ((k + 1 : ℕ) : ZMod q) = (t0 + 1 + k) + 1 := by push_cast; ring
      rw [e, hc, hc', ih]
  funext t
  have e : t = t0 + 1 + (((t - (t0 + 1)).val : ℕ) : ZMod q) := by
    rw [ZMod.natCast_zmod_val]; ring
  rw [e]
  exact run _

/-- Reset existence: if the driver `y` is black at some tick `t0`, a cyclic child exists. -/
theorem child_exists {q : ℕ} [NeZero q] (x y : ZMod q → Bool) (t0 : ZMod q) (hy : y t0 = true) :
    ∃ c : ZMod q → Bool, ∀ t, c (t + 1) = xor (x t) (y t || c t) := by
  -- d k is the child at t0 + 1 + k, run forward from the reset value at t0 + 1
  let d : ℕ → Bool := fun k => Nat.rec (!(x t0))
    (fun k dk => xor (x (t0 + 1 + k)) (y (t0 + 1 + k) || dk)) k
  have dsucc : ∀ k, d (k + 1) = xor (x (t0 + 1 + k)) (y (t0 + 1 + k) || d k) := fun k => rfl
  refine ⟨fun t => d (t - (t0 + 1)).val, ?_⟩
  intro t
  set k := (t - (t0 + 1)).val with hk
  have ht : t = t0 + 1 + (k : ZMod q) := by rw [hk, ZMod.natCast_zmod_val]; ring
  by_cases hlast : k + 1 < q
  · -- the next index is k + 1
    have hk1 : (t + 1 - (t0 + 1)).val = k + 1 := by
      have : t + 1 - (t0 + 1) = ((k + 1 : ℕ) : ZMod q) := by rw [ht]; push_cast; ring
      rw [this, ZMod.val_natCast, Nat.mod_eq_of_lt hlast]
    simp only
    rw [hk1, dsucc, ← ht]
  · -- k = q - 1: t = t0, and the reset closes the cycle
    have hkq : k + 1 = q := by
      have : k < q := by rw [hk]; exact ZMod.val_lt _
      omega
    have htt0 : t = t0 := by
      have : ((k + 1 : ℕ) : ZMod q) = 0 := by rw [hkq]; exact ZMod.natCast_self q
      rw [ht]; push_cast at this ⊢; linear_combination this
    have h0 : (t + 1 - (t0 + 1)).val = 0 := by rw [htt0]; simp
    simp only
    rw [h0, htt0, hy]
    simp [d]

/-- States with a nonzero driver. -/
abbrev St (q : ℕ) := {p : (ZMod q → Bool) × (ZMod q → Bool) // ∃ t, p.2 t = true}

/-- The rooted step: the unique child of a nonzero driver; `none` when that child is zero (a return). -/
noncomputable def walkStep {q : ℕ} [NeZero q] (p : St q) : Option (St q) := by
  classical
  let c := Classical.choose (child_exists p.1.1 p.1.2 (Classical.choose p.2) (Classical.choose_spec p.2))
  exact if h : ∃ t, c t = true then some ⟨(p.1.2, c), h⟩ else none

lemma walkStep_spec {q : ℕ} [NeZero q] (p p' : St q) (h : walkStep p = some p') :
    p'.1.1 = p.1.2 ∧ ∀ t, p'.1.2 (t + 1) = xor (p.1.1 t) (p.1.2 t || p'.1.2 t) := by
  classical
  unfold walkStep at h
  dsimp only at h
  split_ifs at h with hc
  cases h
  exact ⟨rfl, Classical.choose_spec (child_exists p.1.1 p.1.2 (Classical.choose p.2) (Classical.choose_spec p.2))⟩

/-- Every rooted walk returns: from (0, c) with c nonzero, the rooted step reaches a zero child. -/
theorem rooted_walk_returns {q : ℕ} [NeZero q] (c : ZMod q → Bool) (hc : ∃ t, c t = true) :
    ∃ n, orbit walkStep (⟨(fun _ => false, c), hc⟩ : St q) n = none := by
  classical
  apply terminates
  · intro p p' r hp hp'
    obtain ⟨h1, h2⟩ := walkStep_spec p r hp
    obtain ⟨h1', h2'⟩ := walkStep_spec p' r hp'
    have hy : p.1.2 = p'.1.2 := by rw [← h1, ← h1']
    have hx : p.1.1 = p'.1.1 := by
      apply step_injective p.1.1 p'.1.1 p.1.2 r.1.2 h2
      intro t; rw [h2' t, hy]
    exact Subtype.ext (Prod.ext hx hy)
  · intro p hp
    obtain ⟨h1, _⟩ := walkStep_spec p _ hp
    obtain ⟨t, ht⟩ := p.2
    have : p.1.2 t = false := by
      have := congrFun h1 t
      simpa using this.symm
    rw [ht] at this
    exact absurd this (by decide)

end RootedReturn

#print axioms RootedReturn.terminates
#print axioms RootedReturn.step_injective
#print axioms RootedReturn.child_unique
#print axioms RootedReturn.child_exists
#print axioms RootedReturn.rooted_walk_returns
