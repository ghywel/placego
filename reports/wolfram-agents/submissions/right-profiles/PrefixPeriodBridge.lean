import RightProfilesDraft

/-!
# From least prefix periods to the right-profile 11011 restriction

GC2118 staging source: UNCOMPILED, pending independent carrying read.
This extends the already delivered conditional right-profile identities. It does
not assert that individual diagonal periods are monotone, or construct the
least prefix periods for arbitrary initial worlds. Its physical corollary uses
actual Rule 30 diagonals and explicit least/common prefix-period hypotheses.
-/

namespace Rule30PrefixPeriodBridge

open Rule30RightProfiles

/-- A common period from time zero for all profiles with index at most `n`. -/
def PrefixPer (D : Nat → Nat → Bool) (n p : Nat) : Prop :=
  ∀ i, i ≤ n → ∀ t, D i (t + p) = D i t

/-- The least strictly positive common prefix period. -/
def LeastPrefix (D : Nat → Nat → Bool) (n p : Nat) : Prop :=
  0 < p ∧ PrefixPer D n p ∧
    ∀ r, 0 < r → PrefixPer D n r → p ≤ r

/-- Append a profile with the same common period. No minimality is needed. -/
theorem prefix_append {D : Nat → Nat → Bool} {n p : Nat}
    (h : PrefixPer D n p) (hn : ∀ t, D (n + 1) (t + p) = D (n + 1) t) :
    PrefixPer D (n + 1) p := by
  intro i hi t
  by_cases he : i = n + 1
  · subst i; exact hn t
  · exact h i (by omega) t

/-- If a triangular integrator doubles the least prefix period, its new bit
complements at the old period. The old prefix need only HAVE that period. -/
theorem antiperiod_of_minimal_double {D : Nat → Nat → Bool}
    (hs : ∀ n, 2 ≤ n → ∀ t,
      D n (t + 1) = xor (D n t) (D (n - 1) t || D (n - 2) t))
    (n p : Nat) (hn : 2 ≤ n) (hp : 0 < p)
    (hold : PrefixPer D (n - 1) p) (hnew : LeastPrefix D n (2 * p)) :
    ∀ t, D n (t + p) = !D n t := by
  let g := fun t => D (n - 1) t || D (n - 2) t
  have hg : ∀ t, g (t + p) = g t := by
    intro t
    dsimp [g]
    rw [hold (n - 1) (by omega) t, hold (n - 2) (by omega) t]
  have hshift : ∀ t, D n (t + p) = xor (D n t) (xr g p) :=
    running_shift (hs n hn) hg
  cases he : xr g p with
  | false =>
    have hd : ∀ t, D n (t + p) = D n t := by
      intro t
      rw [hshift, he, Bool.xor_false]
    have hprefix : PrefixPer D n p := by
      intro i hi t
      by_cases h : i = n
      · subst i; exact hd t
      · exact hold i (by omega) t
    have hle := hnew.2.2 p hp hprefix
    omega
  | true =>
    intro t
    rw [hshift, he]
    cases D n t <;> rfl

/-- The four new-record/plateau hypotheses force the next prefix to close at
`8*p`. This is the 1101 -> 11010 rule when `p` is divisible by four.
Only the plateau needs a common period; its minimality is unnecessary. -/
theorem prefix_1101_closes {D : Nat → Nat → Bool}
    (hs : ∀ n, 2 ≤ n → ∀ t,
      D n (t + 1) = xor (D n t) (D (n - 1) t || D (n - 2) t))
    (k p : Nat) (hk : 2 ≤ k) (hp : 0 < p) (hp4 : p % 4 = 0)
    (h0 : PrefixPer D (k - 1) p)
    (h1 : LeastPrefix D k (2 * p))
    (h2 : LeastPrefix D (k + 1) (4 * p))
    (h3 : PrefixPer D (k + 2) (4 * p))
    (h4 : LeastPrefix D (k + 3) (8 * p)) :
    PrefixPer D (k + 4) (8 * p) := by
  have hd := antiperiod_of_minimal_double hs k p hk hp h0 h1
  have ha : ∀ t, D (k + 1) (t + 2 * p) = !D (k + 1) t := by
    apply antiperiod_of_minimal_double hs (k + 1) (2 * p) (by omega) (by omega)
    · simpa only [show k + 1 - 1 = k by omega] using h1.2.1
    · simpa only [show 2 * (2 * p) = 4 * p by omega] using h2
  have hc : ∀ t, D (k + 3) (t + 4 * p) = !D (k + 3) t := by
    apply antiperiod_of_minimal_double hs (k + 3) (4 * p) (by omega) (by omega)
    · simpa only [show k + 3 - 1 = k + 2 by omega] using h3
    · simpa only [show 2 * (4 * p) = 8 * p by omega] using h4
  have heta : eta (2 * p) (D k) = false := by
    apply eta_false_of_antiperiod (2 * p) (by omega) (D k)
    simpa only [show 2 * p / 2 = p by omega] using hd
  have hz : ∀ t, D (k + 4) (t + 8 * p) = D (k + 4) t := by
    have h := shift_law (2 * p) (by omega) (D k) (D (k + 1))
      (D (k + 2)) (D (k + 3)) (D (k + 4))
      (h1.2.1 k (by omega)) ha
      (by simpa only [show 2 * (2 * p) = 4 * p by omega] using h3 (k + 2) (by omega))
      (by simpa only [show 2 * (2 * p) = 4 * p by omega] using hc)
      (by
        intro t
        simpa only [show k + 2 - 1 = k + 1 by omega,
          show k + 2 - 2 = k by omega] using hs (k + 2) (by omega) t)
      (by
        intro t
        simpa only [show k + 4 - 1 = k + 3 by omega,
          show k + 4 - 2 = k + 2 by omega] using hs (k + 4) (by omega) t)
    intro t
    simpa only [show 4 * (2 * p) = 8 * p by omega, heta, Bool.xor_false] using h t
  have h := prefix_append h4.2.1 hz
  simpa only [show k + 3 + 1 = k + 4 by omega] using h

/-- The forbidden fifth doubling, stated in terms of least prefix periods. -/
theorem no_11011 {D : Nat → Nat → Bool}
    (hs : ∀ n, 2 ≤ n → ∀ t,
      D n (t + 1) = xor (D n t) (D (n - 1) t || D (n - 2) t))
    (k p : Nat) (hk : 2 ≤ k) (hp : 0 < p) (hp4 : p % 4 = 0)
    (h0 : PrefixPer D (k - 1) p)
    (h1 : LeastPrefix D k (2 * p))
    (h2 : LeastPrefix D (k + 1) (4 * p))
    (h3 : PrefixPer D (k + 2) (4 * p))
    (h4 : LeastPrefix D (k + 3) (8 * p)) :
    ¬ LeastPrefix D (k + 4) (16 * p) := by
  intro h5
  have h := prefix_1101_closes hs k p hk hp hp4 h0 h1 h2 h3 h4
  have := h5.2.2 (8 * p) (by omega) h
  omega

/-- Natural-index actual right diagonals, with no restriction on the seed. -/
def diagonals (x : Int → Bool) (n t : Nat) : Bool := rightDiag x (n : Int) t

theorem diagonals_step (x : Int → Bool) (n : Nat) (hn : 2 ≤ n) (t : Nat) :
    diagonals x n (t + 1) = xor (diagonals x n t)
      (diagonals x (n - 1) t || diagonals x (n - 2) t) := by
  unfold diagonals
  have h := rightDiag_step x (n : Int) t
  simpa only [show (n : Int) - 1 = ((n - 1 : Nat) : Int) by omega,
    show (n : Int) - 2 = ((n - 2 : Nat) : Int) by omega] using h

/-- A physical Rule 30 corollary, under the stated prefix-period hypotheses. -/
theorem actual_no_11011 (x : Int → Bool) (k p : Nat)
    (hk : 2 ≤ k) (hp : 0 < p) (hp4 : p % 4 = 0)
    (h0 : PrefixPer (diagonals x) (k - 1) p)
    (h1 : LeastPrefix (diagonals x) k (2 * p))
    (h2 : LeastPrefix (diagonals x) (k + 1) (4 * p))
    (h3 : PrefixPer (diagonals x) (k + 2) (4 * p))
    (h4 : LeastPrefix (diagonals x) (k + 3) (8 * p)) :
    ¬ LeastPrefix (diagonals x) (k + 4) (16 * p) :=
  no_11011 (diagonals_step x) k p hk hp hp4 h0 h1 h2 h3 h4

end Rule30PrefixPeriodBridge
