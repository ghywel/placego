module

public import Ruliology.CellularAutomata.Rule30FirstChecks

/-!
# The degree of the first check

`Rule30FirstChecks.check n l = Theta (word l) (2 n + 1)` is the first check past the free range: the
cell at depth `2 n + 1` of the constrained row whose free bits are the `n` bits of `l`. As a Boolean
function of `f 0, …, f (n - 1)` over `𝔽₂`, we prove two algebraic normal form coefficient laws
and its exact degree here for every positive `n`.

The coefficient of the monomial of a mask `S` is the exclusive-or of the function over the points
below `S` (`coeff`), and every function is the exclusive-or of the coefficients below its argument
(`anf_expansion`).

* `top_coefficient`: for `n ≥ 1` the coefficient of `f 0 ⋯ f (n - 1)` is `n mod 2`.
* `omit_coefficient`: for `n ≥ 2` the coefficient of the monomial without `f 1` is `n + 1 mod 2`.
* `check_degree`: so the degree of the check is `n` for odd `n` and `n - 1` for even `n`. At even `n`
  the top coefficient alone would only bound the degree; the second coefficient is what fixes it.
* `ones_parity`: for `n ≥ 1` the number of words on which the check is black is congruent to `n`
  modulo `2`.
* `first_check_parity`: with `Rule30FirstChecks.first_check_count`, for `n ≥ 1` the number of rows of
  width at most `2 n` that are black at column `-1` at every even tick through `2 n` is congruent to
  `n` modulo `2`. This is a congruence, not a count.
* `walsh_mod_four`, `walsh_one`: the Walsh sum `2 ^ n - 2 * ones n` is `2 mod 4` exactly at odd
  `n ≥ 2`; at `n = 1` it is `0`.
* `other_phase_odd`: in the other clock phase, with the free bits at the even steps and column `-1`
  black at the odd ones, the check at depth `2 n` (`otherCheck`) has top coefficient `1` for every
  `n ≥ 1`. So its weight is always odd, and the two phases differ at every even `n`.

The proof is a derivative along the anti-diagonals of the reconstruction. Flipping the newest free
bit flips every cell on the anti-diagonal before the top one (`Rule30ZeroBoundary.recon_aff`), so
the change of the top cell is the exclusive-or of the negated cells two anti-diagonals back (`diag`).
Summing out the first free bit `f 0` kills every one of those cells at a time `≥ 2`, and only two
survive: the previous check and the cell `bcell` at depth `2 m` and time `1` (`top_succ`). The same
derivative for `bcell` leaves only the previous `bcell` (`bsum`), so the top coefficient changes at
every step. Fixing `f 1 = 0` before summing gives the second recurrence (`rsum_succ`, `tsum_succ`).
In the other phase the first free bit sits at time `0`, so only the cell at time `0`, the previous
check, survives (`other_flip`), and the top coefficient never changes.

Nothing here bears on the single seed, and Problems 1 to 3 stay open.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30FirstCheckDegree

open Rule30ZeroBoundary Rule30FirstChecks

/-! ### Exclusive-or sums over the cube -/

/-- The exclusive-or of `F` over all bit lists of length `n`. -/
def xs : Nat → (List Bool → Bool) → Bool
  | 0, F => F []
  | n + 1, F => xor (xs n (fun l => F (false :: l))) (xs n (fun l => F (true :: l)))

theorem xs_congr {n : Nat} {F G : List Bool → Bool} (h : ∀ l, l.length = n → F l = G l) :
    xs n F = xs n G := by
  induction n generalizing F G with
  | zero => exact h [] rfl
  | succ n ih =>
    show xor (xs n _) (xs n _) = xor (xs n _) (xs n _)
    rw [ih (fun l hl => h (false :: l) (by simp [hl])), ih (fun l hl => h (true :: l) (by simp [hl]))]

theorem xs_xor (n : Nat) (F G : List Bool → Bool) :
    xs n (fun l => xor (F l) (G l)) = xor (xs n F) (xs n G) := by
  induction n generalizing F G with
  | zero => rfl
  | succ n ih =>
    show xor (xs n fun l => xor (F (false :: l)) (G (false :: l)))
        (xs n fun l => xor (F (true :: l)) (G (true :: l))) =
      xor (xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l)))
        (xor (xs n fun l => G (false :: l)) (xs n fun l => G (true :: l)))
    rw [ih (fun l => F (false :: l)) (fun l => G (false :: l)),
      ih (fun l => F (true :: l)) (fun l => G (true :: l))]
    generalize xs n (fun l => F (false :: l)) = a
    generalize xs n (fun l => G (false :: l)) = b
    generalize xs n (fun l => F (true :: l)) = c
    generalize xs n (fun l => G (true :: l)) = d
    cases a <;> cases b <;> cases c <;> cases d <;> rfl

theorem xs_const (n : Nat) (c : Bool) : xs (n + 1) (fun _ => c) = false := by
  show xor (xs n fun _ => c) (xs n fun _ => c) = false
  generalize xs n (fun _ => c) = a
  cases a <;> rfl

theorem xs_not (n : Nat) (F : List Bool → Bool) : xs (n + 1) (fun l => !F l) = xs (n + 1) F := by
  have h := xs_xor (n + 1) F (fun _ => true)
  rw [xs_const] at h
  have e : xs (n + 1) (fun l => !F l) = xs (n + 1) (fun l => xor (F l) true) :=
    xs_congr fun l _ => by cases F l <;> rfl
  rw [e, h]
  generalize xs (n + 1) F = a
  cases a <;> rfl

/-- A function that does not read the first bit sums to `false`. -/
theorem xs_head {n : Nat} {F : List Bool → Bool} (h : ∀ l, F (false :: l) = F (true :: l)) :
    xs (n + 1) F = false := by
  show xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l)) = false
  rw [show (fun l => F (false :: l)) = (fun l => F (true :: l)) from funext h]
  generalize xs n (fun l => F (true :: l)) = a
  cases a <;> rfl

/-- Summing the last bit first. -/
theorem xs_snoc (n : Nat) (F : List Bool → Bool) :
    xs (n + 1) F = xs n (fun l => xor (F (l ++ [false])) (F (l ++ [true]))) := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show xor (xs (n + 1) _) (xs (n + 1) _) = xs (n + 1) _
    rw [ih, ih]
    rfl

theorem toNat_xor (a b : Bool) : (xor a b).toNat = (a.toNat + b.toNat) % 2 := by
  cases a <;> cases b <;> rfl

/-- The parity of a count over the cube is the exclusive-or sum. -/
theorem cubeSum_parity (n : Nat) (F : List Bool → Bool) :
    cubeSum n (fun l => (F l).toNat) % 2 = (xs n F).toNat := by
  induction n generalizing F with
  | zero =>
    show (F []).toNat % 2 = (F []).toNat
    generalize F [] = a
    cases a <;> rfl
  | succ n ih =>
    have h1 : cubeSum n (fun l => (F (false :: l)).toNat) % 2 = (xs n fun l => F (false :: l)).toNat :=
      ih _
    have h2 : cubeSum n (fun l => (F (true :: l)).toNat) % 2 = (xs n fun l => F (true :: l)).toNat :=
      ih _
    show (cubeSum n (fun l => (F (false :: l)).toNat) + cubeSum n (fun l => (F (true :: l)).toNat)) % 2 =
      (xor (xs n fun l => F (false :: l)) (xs n fun l => F (true :: l))).toNat
    rw [toNat_xor]
    omega

/-! ### The derivative along an anti-diagonal -/

/-- `zs a (k + 1) t` is the exclusive-or of the negated cells `recon a i (t + k - 1 - i)` for
`i < k`: the anti-diagonal two steps behind the one through depth `k + 1` and time `t`. -/
def zs (a : Nat → Bool) : Nat → Nat → Bool
  | 0, _ => false
  | 1, _ => false
  | k + 2, t => xor (zs a (k + 1) (t + 1)) (!recon a k t)

theorem zs_two (a : Nat → Bool) (k t : Nat) :
    zs a (k + 2) t = xor (zs a (k + 1) (t + 1)) (!recon a k t) := rfl

/-- `zs a k t` only reads `a` at times `≥ t`. -/
theorem zs_local {a b : Nat → Bool} {t : Nat} (h : ∀ s, t ≤ s → a s = b s) :
    ∀ k, zs a k t = zs b k t := by
  have key : ∀ k, (∀ t, (∀ s, t ≤ s → a s = b s) → zs a k t = zs b k t) ∧
      (∀ t, (∀ s, t ≤ s → a s = b s) → zs a (k + 1) t = zs b (k + 1) t) := by
    intro k
    induction k with
    | zero => exact ⟨fun _ _ => rfl, fun _ _ => rfl⟩
    | succ k ih =>
      refine ⟨ih.2, fun t h => ?_⟩
      show zs a (k + 2) t = zs b (k + 2) t
      rw [zs_two, zs_two, ih.2 (t + 1) (fun s hs => h s (by omega)),
        recon_local k t (fun j _ => h (t + j) (by omega))]
  exact fun k => (key k).1 t h

/-- **The derivative in the second newest entry.** If `a` and `b` differ only at time `d - 1`, then
along the anti-diagonal of time `d` the cells differ by `zs`. -/
theorem diag (a b : Nat → Bool) (d : Nat) (hd : 1 ≤ d) (hab : ∀ s, s ≠ d - 1 → a s = b s)
    (hflip : xor (a (d - 1)) (b (d - 1)) = true) :
    ∀ k t, t + (k + 1) = d + 1 → xor (recon a (k + 1) t) (recon b (k + 1) t) = zs a (k + 1) t := by
  intro k
  induction k with
  | zero =>
    intro t ht
    show xor (a t) (b t) = false
    rw [hab t (by omega)]
    generalize b t = x
    cases x <;> rfl
  | succ k ih =>
    intro t ht
    have e1 := ih (t + 1) (by omega)
    have e2 : xor (recon a (k + 1) t) (recon b (k + 1) t) = true := by
      rw [recon_aff k a b t (fun j hj => hab (t + j) (by omega)), show t + k = d - 1 by omega]
      exact hflip
    have e3 : recon a k t = recon b k t := recon_local k t (fun j hj => hab (t + j) (by omega))
    show xor (recon a (k + 2) t) (recon b (k + 2) t) = xor (zs a (k + 1) (t + 1)) (!recon a k t)
    rw [recon_two, recon_two, ← e1, ← e3]
    revert e2
    generalize recon a (k + 1) (t + 1) = p
    generalize recon b (k + 1) (t + 1) = q
    generalize recon a (k + 1) t = y
    generalize recon b (k + 1) t = y'
    generalize recon a k t = z
    cases p <;> cases q <;> cases y <;> cases y' <;> cases z <;> decide

/-! ### Column `-1` of a word with one more bit -/

theorem alt_snoc_ne (l : List Bool) (s : Nat) (hs : s ≠ 2 * l.length + 1) :
    alt (word (l ++ [false])) s = alt (word (l ++ [true])) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2]
    rcases Nat.lt_or_gt_of_ne (show s / 2 ≠ l.length by omega) with hlt | hgt
    · rw [word_lt l [false] hlt, word_lt l [true] hlt]
    · obtain ⟨j, hj⟩ : ∃ j, s / 2 = l.length + (j + 1) := ⟨s / 2 - l.length - 1, by omega⟩
      rw [hj, word_ge, word_ge]
      rfl

theorem alt_snoc_top (l : List Bool) (b : Bool) : alt (word (l ++ [b])) (2 * l.length + 1) = b := by
  unfold alt
  rw [ite_eq_right (by omega), show (2 * l.length + 1) / 2 = l.length + 0 by omega, word_ge]
  rfl

theorem alt_snoc_low (l : List Bool) (b : Bool) (s : Nat) (hs : s < 2 * l.length + 1) :
    alt (word (l ++ [b])) s = alt (word l) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2, word_lt l [b] (by omega)]

theorem alt_cons (b c : Bool) (l : List Bool) (s : Nat) (hs : 2 ≤ s) :
    alt (word (b :: l)) s = alt (word (c :: l)) s := by
  unfold alt
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
  · rw [ite_eq_right h2, ite_eq_right h2]
    obtain ⟨j, hj⟩ : ∃ j, s / 2 = j + 1 := ⟨s / 2 - 1, by omega⟩
    rw [hj]
    rfl

theorem snoc_hab (p : List Bool) :
    ∀ s, s ≠ 2 * p.length + 2 - 1 → alt (word (p ++ [false])) s = alt (word (p ++ [true])) s :=
  fun s hs => alt_snoc_ne p s (by omega)

theorem snoc_flip (p : List Bool) :
    xor (alt (word (p ++ [false])) (2 * p.length + 2 - 1))
      (alt (word (p ++ [true])) (2 * p.length + 2 - 1)) = true := by
  rw [show 2 * p.length + 2 - 1 = 2 * p.length + 1 by omega, alt_snoc_top, alt_snoc_top]
  rfl

/-! ### The two recurrences for the top coefficient -/

/-- The cell at depth `2 m` and time `1` of the constrained history with free bits `l`. -/
def bcell (m : Nat) (l : List Bool) : Bool := recon (alt (word l)) (2 * m) 1

/-- The part of the derivative at times `≥ 2`, which does not read the first free bit. -/
def hc (m : Nat) (l : List Bool) : Bool := zs (alt (word (l ++ [false]))) (2 * m + 1) 2

theorem hc_cons (m : Nat) (b c : Bool) (l : List Bool) : hc m (b :: l) = hc m (c :: l) :=
  zs_local (t := 2) (fun s hs => alt_cons b c (l ++ [false]) s hs) (2 * m + 1)

/-- **The derivative of the check in its newest free bit.** -/
theorem check_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (check (m + 1) (p ++ [false])) (check (m + 1) (p ++ [true])) =
      xor (xor (hc m p) (!bcell m p)) (!check m p) := by
  subst hp
  have hd := diag (alt (word (p ++ [false]))) (alt (word (p ++ [true]))) (2 * p.length + 2)
    (by omega) (snoc_hab p) (snoc_flip p) (2 * p.length + 2) 0 (by omega)
  have e1 : recon (alt (word (p ++ [false]))) (2 * p.length) 1 = bcell p.length p :=
    recon_local _ 1 (fun j hj => alt_snoc_low p false (1 + j) (by omega))
  have e2 : recon (alt (word (p ++ [false]))) (2 * p.length + 1) 0 = check p.length p :=
    recon_local _ 0 (fun j hj => alt_snoc_low p false (0 + j) (by omega))
  show xor (recon (alt (word (p ++ [false]))) (2 * (p.length + 1) + 1) 0)
      (recon (alt (word (p ++ [true]))) (2 * (p.length + 1) + 1) 0) = _
  rw [show 2 * (p.length + 1) + 1 = 2 * p.length + 2 + 1 by omega, hd,
    show 2 * p.length + 2 + 1 = 2 * p.length + 1 + 2 by omega, zs_two,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1, e2]
  rfl

/-- **The derivative of `bcell` in its newest free bit.** -/
theorem bcell_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (bcell (m + 1) (p ++ [false])) (bcell (m + 1) (p ++ [true])) =
      xor (hc m p) (!bcell m p) := by
  subst hp
  have hd := diag (alt (word (p ++ [false]))) (alt (word (p ++ [true]))) (2 * p.length + 2)
    (by omega) (snoc_hab p) (snoc_flip p) (2 * p.length + 1) 1 (by omega)
  have e1 : recon (alt (word (p ++ [false]))) (2 * p.length) 1 = bcell p.length p :=
    recon_local _ 1 (fun j hj => alt_snoc_low p false (1 + j) (by omega))
  show xor (recon (alt (word (p ++ [false]))) (2 * (p.length + 1)) 1)
      (recon (alt (word (p ++ [true]))) (2 * (p.length + 1)) 1) = _
  rw [show 2 * (p.length + 1) = 2 * p.length + 1 + 1 by omega, hd,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1]
  rfl

theorem bsum (m : Nat) : xs (m + 1) (bcell (m + 1)) = true := by
  induction m with
  | zero => decide
  | succ m ih =>
    have h1 : xs (m + 1 + 1) (bcell (m + 1 + 1)) =
        xs (m + 1) (fun l => xor (hc (m + 1) l) (!bcell (m + 1) l)) := by
      rw [xs_snoc]
      exact xs_congr fun l hl => bcell_flip (m + 1) l hl
    rw [h1, xs_xor, xs_head (F := hc (m + 1)) (fun l => hc_cons (m + 1) false true l), xs_not, ih]
    rfl

/-- **The first recurrence.** The top sum of the check is the previous one plus the top sum of
`bcell`. -/
theorem top_succ (m : Nat) :
    xs (m + 2) (check (m + 2)) = xor (xs (m + 1) (check (m + 1))) (xs (m + 1) (bcell (m + 1))) := by
  have h1 : xs (m + 1 + 1) (check (m + 1 + 1)) =
      xs (m + 1) (fun l => xor (xor (hc (m + 1) l) (!bcell (m + 1) l)) (!check (m + 1) l)) := by
    rw [xs_snoc]
    exact xs_congr fun l hl => check_flip (m + 1) l hl
  rw [h1, xs_xor, xs_xor, xs_head (F := hc (m + 1)) (fun l => hc_cons (m + 1) false true l),
    xs_not, xs_not]
  generalize xs (m + 1) (check (m + 1)) = x
  generalize xs (m + 1) (bcell (m + 1)) = y
  cases x <;> cases y <;> rfl

/-- The exclusive-or of the check over all words is `n mod 2`. -/
theorem top_sum (n : Nat) (hn : 1 ≤ n) : xs n (check n) = decide (n % 2 = 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  induction m with
  | zero => decide
  | succ m ih =>
    rw [top_succ, ih (by omega), bsum]
    by_cases h : (m + 1) % 2 = 1
    · rw [decide_eq_true h, decide_eq_false (by omega)]
      rfl
    · rw [decide_eq_false h, decide_eq_true (by omega)]
      rfl

/-! ### The coefficient without `f 1` -/

/-- Insert a white bit at position `1`. -/
def ins : List Bool → List Bool
  | [] => [false]
  | x :: l => x :: false :: l

/-- The sum over the words with `f 1 = 0`, for checks of `m + 2` bits. -/
def rsum (m : Nat) : Bool := xs (m + 1) (fun l => check (m + 2) (ins l))

/-- The same sum for `bcell` of `m + 2` bits. -/
def tsum (m : Nat) : Bool := xs (m + 1) (fun l => bcell (m + 2) (ins l))

theorem ins_cons_length (x : Bool) (l : List Bool) : (ins (x :: l)).length = l.length + 2 := rfl

theorem tsum_succ (m : Nat) : tsum (m + 1) = tsum m := by
  have h1 : xs (m + 1 + 1) (fun l => bcell (m + 1 + 2) (ins l)) =
      xs (m + 1) (fun l => xor (hc (m + 2) (ins l)) (!bcell (m + 2) (ins l))) := by
    rw [xs_snoc]
    apply xs_congr
    intro l hl
    cases l with
    | nil => simp at hl
    | cons x l' =>
      exact bcell_flip (m + 2) (ins (x :: l')) (by rw [ins_cons_length]; simp at hl; omega)
  show xs (m + 1 + 1) (fun l => bcell (m + 1 + 2) (ins l)) = tsum m
  rw [h1, xs_xor, xs_head (F := fun l => hc (m + 2) (ins l))
    (fun l => hc_cons (m + 2) false true (false :: l)), xs_not]
  show xor false (tsum m) = tsum m
  generalize tsum m = a
  cases a <;> rfl

theorem rsum_succ (m : Nat) : rsum (m + 1) = xor (rsum m) (tsum m) := by
  have h1 : xs (m + 1 + 1) (fun l => check (m + 1 + 2) (ins l)) =
      xs (m + 1) (fun l =>
        xor (xor (hc (m + 2) (ins l)) (!bcell (m + 2) (ins l))) (!check (m + 2) (ins l))) := by
    rw [xs_snoc]
    apply xs_congr
    intro l hl
    cases l with
    | nil => simp at hl
    | cons x l' =>
      exact check_flip (m + 2) (ins (x :: l')) (by rw [ins_cons_length]; simp at hl; omega)
  show xs (m + 1 + 1) (fun l => check (m + 1 + 2) (ins l)) = xor (rsum m) (tsum m)
  rw [h1, xs_xor, xs_xor, xs_head (F := fun l => hc (m + 2) (ins l))
    (fun l => hc_cons (m + 2) false true (false :: l)), xs_not, xs_not]
  show xor (xor false (tsum m)) (rsum m) = xor (rsum m) (tsum m)
  generalize tsum m = a
  generalize rsum m = b
  cases a <;> cases b <;> rfl

theorem tsum_all (m : Nat) : tsum m = true := by
  induction m with
  | zero => decide
  | succ m ih => rw [tsum_succ, ih]

theorem rsum_all (m : Nat) : rsum m = decide (m % 2 = 0) := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [rsum_succ, ih, tsum_all]
    by_cases h : m % 2 = 0
    · rw [decide_eq_true h, decide_eq_false (by omega)]
      rfl
    · rw [decide_eq_false h, decide_eq_true (by omega)]
      rfl

/-! ### Algebraic normal form -/

/-- The coefficient of the monomial of the mask `S` in the algebraic normal form of `F`: the
exclusive-or of `F` over the bit lists below `S`. -/
def coeff : List Bool → (List Bool → Bool) → Bool
  | [], F => F []
  | false :: S, F => coeff S (fun l => F (false :: l))
  | true :: S, F => xor (coeff S (fun l => F (false :: l))) (coeff S (fun l => F (true :: l)))

theorem coeff_xor : ∀ (S : List Bool) (F G : List Bool → Bool),
    coeff S (fun l => xor (F l) (G l)) = xor (coeff S F) (coeff S G)
  | [], _, _ => rfl
  | false :: S, F, G => coeff_xor S (fun l => F (false :: l)) (fun l => G (false :: l))
  | true :: S, F, G => by
    show xor (coeff S fun l => xor (F (false :: l)) (G (false :: l)))
        (coeff S fun l => xor (F (true :: l)) (G (true :: l))) =
      xor (xor (coeff S fun l => F (false :: l)) (coeff S fun l => F (true :: l)))
        (xor (coeff S fun l => G (false :: l)) (coeff S fun l => G (true :: l)))
    rw [coeff_xor S (fun l => F (false :: l)) (fun l => G (false :: l)),
      coeff_xor S (fun l => F (true :: l)) (fun l => G (true :: l))]
    generalize coeff S (fun l => F (false :: l)) = a
    generalize coeff S (fun l => G (false :: l)) = b
    generalize coeff S (fun l => F (true :: l)) = c
    generalize coeff S (fun l => G (true :: l)) = d
    cases a <;> cases b <;> cases c <;> cases d <;> rfl

/-- **Möbius expansion.** `F x` is the exclusive-or of the coefficients of the masks below `x`, so
`coeff` is the algebraic normal form of `F`. -/
theorem anf_expansion : ∀ (x : List Bool) (F : List Bool → Bool), F x = coeff x (fun S => coeff S F)
  | [], _ => rfl
  | false :: x, F => anf_expansion x (fun l => F (false :: l))
  | true :: x, F => by
    have e : F (true :: x) = coeff x (fun S => coeff S fun l => F (true :: l)) :=
      anf_expansion x (fun l => F (true :: l))
    show F (true :: x) = xor (coeff x fun S => coeff S fun l => F (false :: l))
      (coeff x fun S => xor (coeff S fun l => F (false :: l)) (coeff S fun l => F (true :: l)))
    rw [coeff_xor x (fun S => coeff S fun l => F (false :: l)) (fun S => coeff S fun l => F (true :: l)),
      ← e]
    generalize coeff x (fun S => coeff S fun l => F (false :: l)) = a
    generalize F (true :: x) = c
    cases a <;> cases c <;> rfl

theorem coeff_replicate (n : Nat) (F : List Bool → Bool) : coeff (List.replicate n true) F = xs n F := by
  induction n generalizing F with
  | zero => rfl
  | succ n ih =>
    show xor (coeff (List.replicate n true) _) (coeff (List.replicate n true) _) = xor (xs n _) (xs n _)
    rw [ih, ih]

theorem coeff_omit (m : Nat) (F : List Bool → Bool) :
    coeff (true :: false :: List.replicate m true) F = xs (m + 1) (fun l => F (ins l)) := by
  show xor (coeff (List.replicate m true) fun l => F (false :: false :: l))
      (coeff (List.replicate m true) fun l => F (true :: false :: l)) =
    xor (xs m fun l => F (false :: false :: l)) (xs m fun l => F (true :: false :: l))
  rw [coeff_replicate, coeff_replicate]

/-! ### The coefficients and the degree of the check -/

/-- **The top coefficient.** For `n ≥ 1`, the coefficient of `f 0 ⋯ f (n - 1)` in the check is
`n mod 2`. -/
theorem top_coefficient (n : Nat) (hn : 1 ≤ n) :
    coeff (List.replicate n true) (check n) = decide (n % 2 = 1) := by
  rw [coeff_replicate]
  exact top_sum n hn

/-- **The coefficient without `f 1`.** For `n ≥ 2`, the coefficient of the monomial of every free
bit but `f 1` is `n + 1 mod 2`. -/
theorem omit_coefficient (n : Nat) (hn : 2 ≤ n) :
    coeff (true :: false :: List.replicate (n - 2) true) (check n) = decide (n % 2 = 0) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  rw [show m + 2 - 2 = m by omega, coeff_omit]
  have h := rsum_all m
  unfold rsum at h
  rw [h]
  exact decide_eq_decide.mpr (by omega)

/-- `F` on bit lists of length `n` has degree `d`: no mask with more than `d` ones has a nonzero
coefficient, and one with exactly `d` ones has. -/
def IsDegree (n : Nat) (F : List Bool → Bool) (d : Nat) : Prop :=
  (∀ S : List Bool, S.length = n → d < S.count true → coeff S F = false) ∧
    ∃ S : List Bool, S.length = n ∧ S.count true = d ∧ coeff S F = true

theorem count_full : ∀ S : List Bool, S.count true = S.length → S = List.replicate S.length true
  | [], _ => rfl
  | b :: S, h => by
    have hle : S.count true ≤ S.length := List.count_le_length
    cases b with
    | false =>
      simp at h
      omega
    | true =>
      simp at h
      rw [List.length_cons, List.replicate_succ, ← count_full S h]

/-- **The degree of the check** is `n` for odd `n` and `n - 1` for even `n`, for `n ≥ 1`. -/
theorem check_degree (n : Nat) (hn : 1 ≤ n) :
    IsDegree n (check n) (if n % 2 = 1 then n else n - 1) := by
  by_cases hodd : n % 2 = 1
  · rw [ite_eq_left hodd]
    refine ⟨fun S hS hlt => ?_, List.replicate n true, List.length_replicate, List.count_replicate_self,
      by rw [top_coefficient n hn, decide_eq_true hodd]⟩
    have hle : S.count true ≤ S.length := List.count_le_length
    omega
  · rw [ite_eq_right hodd]
    refine ⟨fun S hS hlt => ?_, true :: false :: List.replicate (n - 2) true, by simp; omega,
      by simp; omega, by rw [omit_coefficient n (by omega), decide_eq_true (by omega)]⟩
    have hle : S.count true ≤ S.length := List.count_le_length
    rw [count_full S (by omega), hS, top_coefficient n hn, decide_eq_false hodd]

/-! ### Parities of the counts -/

/-- The number of words of length `n ≥ 1` on which the check is black is congruent to `n`
modulo `2`. -/
theorem ones_parity (n : Nat) (hn : 1 ≤ n) : ones n % 2 = n % 2 := by
  have h := cubeSum_parity n (check n)
  have e : ones n = cubeSum n (fun l => (check n l).toNat) := rfl
  rw [e, h, top_sum n hn]
  rcases Nat.mod_two_eq_zero_or_one n with h0 | h1
  · rw [decide_eq_false (by omega), h0]
    rfl
  · rw [decide_eq_true h1, h1]
    rfl

/-- **The survivors of the first check, modulo 2.** For `n ≥ 1`, the number of rows of width at
most `2 n` that are black at column `-1` at every even tick through `2 n` is congruent to `n`
modulo `2`. -/
theorem first_check_parity (n : Nat) (hn : 1 ≤ n) : firstCheck n % 2 = n % 2 := by
  have h := first_check_count n
  have h2 := ones_parity n hn
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  rw [Nat.pow_succ] at h
  omega

/-- **The Walsh sum modulo 4.** For `n ≥ 2`, `2 ^ n - 2 * ones n` is `2` modulo `4` exactly at odd
`n`. -/
theorem walsh_mod_four (n : Nat) (hn : 2 ≤ n) :
    ((2 : Int) ^ n - 2 * (ones n : Int)) % 4 = 2 * ((n % 2 : Nat) : Int) := by
  have h := ones_parity n (by omega)
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  rw [show (2 : Int) ^ (m + 2) = 4 * 2 ^ m by rw [Int.pow_succ, Int.pow_succ]; omega]
  generalize (2 : Int) ^ m = N
  omega

/-- **The exception at `n = 1`.** There the Walsh sum is `0`, although `1` is odd. -/
theorem walsh_one : (2 : Int) ^ 1 - 2 * (ones 1 : Int) = 0 := by
  have h : ones 1 = 1 := by decide
  rw [h]
  rfl

/-! ### The other clock phase -/

/-- Column `-1` in the other phase: the free bits `g` at the even steps, black at the odd ones. -/
def altO (g : Nat → Bool) (t : Nat) : Bool := if t % 2 = 0 then g (t / 2) else true

/-- The first check past the free range in the other phase: the cell at depth `2 n` and time `0`
with the white wall, for the `n` free bits of `l`. -/
def otherCheck (n : Nat) (l : List Bool) : Bool := recon (altO (word l)) (2 * n) 0

theorem altO_snoc_ne (l : List Bool) (s : Nat) (hs : s ≠ 2 * l.length) :
    altO (word (l ++ [false])) s = altO (word (l ++ [true])) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
    rcases Nat.lt_or_gt_of_ne (show s / 2 ≠ l.length by omega) with hlt | hgt
    · rw [word_lt l [false] hlt, word_lt l [true] hlt]
    · obtain ⟨j, hj⟩ : ∃ j, s / 2 = l.length + (j + 1) := ⟨s / 2 - l.length - 1, by omega⟩
      rw [hj, word_ge, word_ge]
      rfl
  · rw [ite_eq_right h2, ite_eq_right h2]

theorem altO_snoc_top (l : List Bool) (b : Bool) : altO (word (l ++ [b])) (2 * l.length) = b := by
  unfold altO
  rw [ite_eq_left (by omega), show 2 * l.length / 2 = l.length + 0 by omega, word_ge]
  rfl

theorem altO_snoc_low (l : List Bool) (b : Bool) (s : Nat) (hs : s < 2 * l.length) :
    altO (word (l ++ [b])) s = altO (word l) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2, word_lt l [b] (by omega)]
  · rw [ite_eq_right h2, ite_eq_right h2]

theorem altO_cons (b c : Bool) (l : List Bool) (s : Nat) (hs : 1 ≤ s) :
    altO (word (b :: l)) s = altO (word (c :: l)) s := by
  unfold altO
  by_cases h2 : s % 2 = 0
  · rw [ite_eq_left h2, ite_eq_left h2]
    obtain ⟨j, hj⟩ : ∃ j, s / 2 = j + 1 := ⟨s / 2 - 1, by omega⟩
    rw [hj]
    rfl
  · rw [ite_eq_right h2, ite_eq_right h2]

/-- The part of the other-phase derivative at times `≥ 1`, which does not read `g 0`. -/
def ho (m : Nat) (l : List Bool) : Bool := zs (altO (word (l ++ [false]))) (2 * m + 1) 1

theorem ho_cons (m : Nat) (b c : Bool) (l : List Bool) : ho m (b :: l) = ho m (c :: l) :=
  zs_local (t := 1) (fun s hs => altO_cons b c (l ++ [false]) s hs) (2 * m + 1)

/-- **The other-phase derivative in the newest free bit.** Only one earlier cell survives at
time `0`, the previous check. -/
theorem other_flip (m : Nat) (p : List Bool) (hp : p.length = m) :
    xor (otherCheck (m + 1) (p ++ [false])) (otherCheck (m + 1) (p ++ [true])) =
      xor (ho m p) (!otherCheck m p) := by
  subst hp
  have hd := diag (altO (word (p ++ [false]))) (altO (word (p ++ [true]))) (2 * p.length + 1)
    (by omega) (fun s hs => altO_snoc_ne p s (by omega))
    (by rw [show 2 * p.length + 1 - 1 = 2 * p.length by omega, altO_snoc_top, altO_snoc_top]; rfl)
    (2 * p.length + 1) 0 (by omega)
  have e1 : recon (altO (word (p ++ [false]))) (2 * p.length) 0 = otherCheck p.length p :=
    recon_local _ 0 (fun j hj => altO_snoc_low p false (0 + j) (by omega))
  show xor (recon (altO (word (p ++ [false]))) (2 * (p.length + 1)) 0)
      (recon (altO (word (p ++ [true]))) (2 * (p.length + 1)) 0) = _
  rw [show 2 * (p.length + 1) = 2 * p.length + 1 + 1 by omega, hd,
    show 2 * p.length + 1 + 1 = 2 * p.length + 2 by omega, zs_two, e1]
  rfl

/-- **The other phase is always odd.** For every `n ≥ 1`, the check of the other phase is black
on an odd number of the `2 ^ n` words, so its top coefficient is `1` and its degree is `n`. -/
theorem other_phase_odd (n : Nat) (hn : 1 ≤ n) :
    coeff (List.replicate n true) (otherCheck n) = true := by
  rw [coeff_replicate]
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  induction m with
  | zero => decide
  | succ m ih =>
    have h1 : xs (m + 1 + 1) (otherCheck (m + 1 + 1)) =
        xs (m + 1) (fun l => xor (ho (m + 1) l) (!otherCheck (m + 1) l)) := by
      rw [xs_snoc]
      exact xs_congr fun l hl => other_flip (m + 1) l hl
    rw [h1, xs_xor, xs_head (F := ho (m + 1)) (fun l => ho_cons (m + 1) false true l), xs_not,
      ih (by omega)]
    rfl

end Rule30FirstCheckDegree
end Ruliology.CellularAutomata
