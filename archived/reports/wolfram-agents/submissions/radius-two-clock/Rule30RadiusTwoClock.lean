module

public import Ruliology.CellularAutomata.Rule30Prize

/-!
# A radius-two left-permutive rule with an exactly alternating column from a finite seed

Rule 30 is left-permutive: the new cell is the left neighbour exclusive-or a function of the
others. Problem 1 asks whether its center column can be eventually periodic from the single cell.
For left-permutive rules of radius two the answer can be yes, from a finite seed, already with
two states. For Booleans `p` and `q` let `N p q` be the rule

  `new x i = x (i - 2) xor g (x (i - 1)) (x i) (x (i + 1)) (x (i + 2))`,

where `g a b c d` is true unless `b`, `c` and `d` are all equal, except that `g 1 1 0 1 = p` and
`g 1 0 1 1 = q`.

* `clock`: from exactly the black cells `0` and `2`, the columns `-2` and `-1` are `t mod 2` at
  every time `t`, for all four rules. `column0_alternates`: from the black cells `2` and `4`,
  column `0` alternates.
* `rule_facts`: each rule is white-quiescent, nonlinear and not right-permutive; it is
  left-permutive by its form.

**The proof is finite.** The row at time `t` is a doubled block field `z t` on the cells up to
`2 t - 1`, followed by black cells at `2 t + 2` and, at even times, at `2 t` (`row_formula`). On
doubled rows the rule never reads the two exceptional windows and acts as rule 150 on the blocks
(`step_doubled`); the frontier adds a source at block `t`, and at block `t - 1` at even times
(`z`). The block field's frontier is `z t (t - 1) = z t (t - 2) = (t odd)` (`z_frontier`). For
the column, the reflection `j ↦ -2 - j` commutes with rule 150; the difference `d t` of the field
and its reflection is the even band `E n` of the positions `-2 n, …, 2 n - 2` at the times
`2 n` and `E (n + 1)` at `2 n + 1` (`d_band`), so block `-1` flips at every step (`z_clock`). No
power series are used.

The rules are not rule 30, and nothing here bears on rule 30's center column; the example shows
that left-permutivity at radius two alone does not exclude a periodic column from a finite seed.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30RadiusTwoClock

/-! ### The rules -/

/-- The nonlinear part: not all of `b`, `c`, `d` equal, except on two windows. -/
def g (p q : Bool) (a b c d : Bool) : Bool :=
  if a && b && !c && d then p else if a && !b && c && d then q else !(b == c && c == d)

/-- One step of the rule `N p q` on the whole line. -/
def stepN (p q : Bool) (x : Int → Bool) : Int → Bool :=
  fun i => xor (x (i - 2)) (g p q (x (i - 1)) (x i) (x (i + 1)) (x (i + 2)))

/-- The evolution of `N p q`. -/
def evolN (p q : Bool) (x : Int → Bool) : Nat → Int → Bool
  | 0 => x
  | t + 1 => stepN p q (evolN p q x t)

/-- The seed: black exactly at the cells `0` and `2`. -/
def seed02 : Int → Bool := fun i => decide (i = 0 ∨ i = 2)

/-- **The local rule.** White-quiescent, not right-permutive, and not affine over `GF(2)`. -/
theorem rule_facts : ∀ p q : Bool,
    g p q false false false false = false ∧
    (∃ a b c d, xor a (g p q b c d false) = xor a (g p q b c d true)) ∧
    ¬ (∀ b c d e b' c' d' e' : Bool,
      xor (g p q (xor b b') (xor c c') (xor d d') (xor e e')) (g p q false false false false) =
        xor (g p q b c d e) (g p q b' c' d' e')) := by decide

/-! ### The block field -/

/-- The source at the frontier. -/
def src (t : Nat) (j : Int) : Bool := decide (j = t) || (decide (t % 2 = 0) && decide (j = (t : Int) - 1))

theorem dT (a b : Int) (h : a = b) : decide (a = b) = true := decide_eq_true h
theorem dF (a b : Int) (h : ¬ a = b) : decide (a = b) = false := decide_eq_false h

/-- The block field: rule 150 on the blocks, with the frontier sources. -/
def z : Nat → Int → Bool
  | 0, _ => false
  | t + 1, j => xor (xor (xor (z t (j - 1)) (z t j)) (z t (j + 1))) (src t j)

theorem z_support : ∀ (t : Nat) (j : Int), (j < -(t : Int) ∨ (t : Int) ≤ j) → z t j = false
  | 0, _, _ => rfl
  | t + 1, j, h => by
    simp only [z]
    rw [z_support t (j - 1) (by omega), z_support t j (by omega), z_support t (j + 1) (by omega)]
    unfold src
    have h1 : ¬ (j = (t : Int)) := by omega
    have h2 : ¬ (j = (t : Int) - 1) := by omega
    simp [h1, h2]

theorem par_succ (t : Nat) : decide ((t + 1) % 2 = 1) = !decide (t % 2 = 1) := by
  rcases Nat.mod_two_eq_zero_or_one t with h | h
  · rw [decide_eq_true (show (t + 1) % 2 = 1 by omega), decide_eq_false (show ¬ t % 2 = 1 by omega)] <;> rfl
  · rw [decide_eq_false (show ¬ (t + 1) % 2 = 1 by omega), decide_eq_true (show t % 2 = 1 by omega)] <;> rfl

theorem par_even (t : Nat) : decide (t % 2 = 0) = !decide (t % 2 = 1) := by
  rcases Nat.mod_two_eq_zero_or_one t with h | h
  · rw [decide_eq_true (show t % 2 = 0 by omega), decide_eq_false (show ¬ t % 2 = 1 by omega)] <;> rfl
  · rw [decide_eq_false (show ¬ t % 2 = 0 by omega), decide_eq_true (show t % 2 = 1 by omega)] <;> rfl

theorem src_at (t : Nat) : src t (t : Int) = true := by unfold src; simp

theorem src_below (t : Nat) : src t ((t : Int) - 1) = decide (t % 2 = 0) := by
  unfold src
  rw [decide_eq_false (show ¬ ((t : Int) - 1 = (t : Int)) by omega), decide_eq_true (show (t : Int) - 1 = (t : Int) - 1 from rfl)]
  cases decide (t % 2 = 0) <;> rfl

theorem z_frontier : ∀ (t : Nat), z t ((t : Int) - 1) = decide (t % 2 = 1) ∧
    z t ((t : Int) - 2) = decide (t % 2 = 1)
  | 0 => ⟨rfl, rfl⟩
  | t + 1 => by
    obtain ⟨h1, h2⟩ := z_frontier t
    have e0 : z t (t : Int) = false := z_support t (t : Int) (by omega)
    have e1 : z t ((t : Int) + 1) = false := z_support t ((t : Int) + 1) (by omega)
    refine ⟨?_, ?_⟩
    · rw [show ((t + 1 : Nat) : Int) - 1 = (t : Int) by omega]
      simp only [z]
      rw [h1, e0, e1, src_at, par_succ]
      cases decide (t % 2 = 1) <;> rfl
    · rw [show ((t + 1 : Nat) : Int) - 2 = (t : Int) - 1 by omega]
      simp only [z]
      rw [show (t : Int) - 1 - 1 = (t : Int) - 2 by omega, show (t : Int) - 1 + 1 = (t : Int) by omega,
        h1, h2, e0, src_below, par_succ, par_even]
      cases decide (t % 2 = 1) <;> rfl

/-! ### The row formula -/

/-- The row at time `t`: doubled blocks up to the cell `2 t - 1`, then black cells at `2 t + 2`
and, at even times, at `2 t`. -/
def row (t : Nat) (i : Int) : Bool :=
  if i ≤ 2 * (t : Int) - 1 then z t (i / 2)
  else decide (i = 2 * (t : Int) + 2) || (decide (t % 2 = 0) && decide (i = 2 * (t : Int)))

theorem g_doubled_even (p q a b c : Bool) : g p q a b b c = xor b c := by
  cases a <;> cases b <;> cases c <;> rfl

theorem g_doubled_odd (p q a b : Bool) : g p q a a b b = xor a b := by
  cases a <;> cases b <;> rfl

/-- **On doubled rows the rule is rule 150 on the blocks.** -/
theorem step_doubled (p q : Bool) (x : Int → Bool) (w : Int → Bool) (i : Int)
    (hx : ∀ k, i - 2 ≤ k → k ≤ i + 2 → x k = w (k / 2)) :
    stepN p q x i = xor (xor (w (i / 2 - 1)) (w (i / 2))) (w (i / 2 + 1)) := by
  unfold stepN
  have hpar : i % 2 = 0 ∨ i % 2 = 1 := by omega
  rcases hpar with h | h
  · rw [hx (i - 2) (by omega) (by omega), hx (i - 1) (by omega) (by omega), hx i (by omega) (by omega),
      hx (i + 1) (by omega) (by omega), hx (i + 2) (by omega) (by omega),
      show (i - 2) / 2 = i / 2 - 1 by omega, show (i - 1) / 2 = i / 2 - 1 by omega,
      show (i + 1) / 2 = i / 2 by omega, show (i + 2) / 2 = i / 2 + 1 by omega, g_doubled_even]
    cases w (i / 2 - 1) <;> cases w (i / 2) <;> cases w (i / 2 + 1) <;> rfl
  · rw [hx (i - 2) (by omega) (by omega), hx (i - 1) (by omega) (by omega), hx i (by omega) (by omega),
      hx (i + 1) (by omega) (by omega), hx (i + 2) (by omega) (by omega),
      show (i - 2) / 2 = i / 2 - 1 by omega, show (i - 1) / 2 = i / 2 by omega,
      show (i + 1) / 2 = i / 2 + 1 by omega, show (i + 2) / 2 = i / 2 + 1 by omega, g_doubled_odd]
    cases w (i / 2 - 1) <;> cases w (i / 2) <;> cases w (i / 2 + 1) <;> rfl

/-- The row near the frontier, by the offset from `2 t`, with `b = (t odd)`. -/
def fr (b : Bool) (o : Int) : Bool := if o ≤ -1 then b else if o = 0 then !b else if o = 2 then true else false

/-- The next row near the old frontier. -/
def fs (b : Bool) (c : Int) : Bool := if c ≤ 1 then !b else if c = 2 then b else if c = 4 then true else false

theorem row_frontier (t : Nat) (o : Int) (ho : -4 ≤ o) :
    row t (2 * (t : Int) + o) = fr (decide (t % 2 = 1)) o := by
  obtain ⟨f1, f2⟩ := z_frontier t
  unfold row fr
  by_cases h : o ≤ -1
  · rw [ite_eq_left (show 2 * (t : Int) + o ≤ 2 * (t : Int) - 1 by omega), ite_eq_left h]
    rcases (show (2 * (t : Int) + o) / 2 = (t : Int) - 1 ∨ (2 * (t : Int) + o) / 2 = (t : Int) - 2 by omega)
      with e | e
    · rw [e, f1]
    · rw [e, f2]
  · rw [ite_eq_right (show ¬ (2 * (t : Int) + o ≤ 2 * (t : Int) - 1) by omega), ite_eq_right h]
    by_cases h0 : o = 0
    · subst h0
      rw [ite_eq_left rfl, dF _ _ (show ¬ (2 * (t : Int) + 0 = 2 * (t : Int) + 2) by omega),
        dT _ _ (show 2 * (t : Int) + 0 = 2 * (t : Int) by omega), par_even]
      cases decide (t % 2 = 1) <;> rfl
    · rw [ite_eq_right h0]
      by_cases h2 : o = 2
      · subst h2; rw [ite_eq_left rfl]; simp
      · rw [ite_eq_right h2]; simp; omega

theorem row_succ_frontier (t : Nat) (c : Int) (h1 : -2 ≤ c) (h2 : c ≤ 5) :
    row (t + 1) (2 * (t : Int) + c) = fs (decide (t % 2 = 1)) c := by
  have hnb : decide ((t + 1) % 2 = 1) = !decide (t % 2 = 1) := par_succ t
  have za : z (t + 1) (t : Int) = !decide (t % 2 = 1) := by
    have := (z_frontier (t + 1)).1
    rw [show ((t + 1 : Nat) : Int) - 1 = (t : Int) by omega, hnb] at this
    exact this
  have zb : z (t + 1) ((t : Int) - 1) = !decide (t % 2 = 1) := by
    have := (z_frontier (t + 1)).2
    rw [show ((t + 1 : Nat) : Int) - 2 = (t : Int) - 1 by omega, hnb] at this
    exact this
  unfold row fs
  by_cases h : c ≤ 1
  · rw [ite_eq_left (show 2 * (t : Int) + c ≤ 2 * ((t + 1 : Nat) : Int) - 1 by omega), ite_eq_left h]
    rcases (show (2 * (t : Int) + c) / 2 = (t : Int) ∨ (2 * (t : Int) + c) / 2 = (t : Int) - 1 by omega)
      with e | e
    · rw [e, za]
    · rw [e, zb]
  · rw [ite_eq_right (show ¬ (2 * (t : Int) + c ≤ 2 * ((t + 1 : Nat) : Int) - 1) by omega), ite_eq_right h]
    by_cases c2 : c = 2
    · subst c2
      rw [ite_eq_left rfl, dF _ _ (show ¬ (2 * (t : Int) + 2 = 2 * ((t + 1 : Nat) : Int) + 2) by omega),
        dT _ _ (show 2 * (t : Int) + 2 = 2 * ((t + 1 : Nat) : Int) by omega), par_even, par_succ]
      cases decide (t % 2 = 1) <;> rfl
    · rw [ite_eq_right c2]
      by_cases c4 : c = 4
      · subst c4; rw [ite_eq_left rfl]; simp; omega
      · rw [ite_eq_right c4]; simp; omega

theorem row_far (t : Nat) (k : Int) (hk : 2 * (t : Int) + 4 ≤ k) : row t k = false := by
  unfold row
  rw [ite_eq_right (show ¬ (k ≤ 2 * (t : Int) - 1) by omega)]
  simp; omega

/-- **The row formula.** -/
theorem row_formula (p q : Bool) : ∀ t, evolN p q seed02 t = row t
  | 0 => by
    funext i
    show seed02 i = row 0 i
    unfold row seed02
    by_cases h : i ≤ 2 * ((0 : Nat) : Int) - 1
    · rw [ite_eq_left h]
      simp only [z]
      exact decide_eq_false (by omega)
    · rw [ite_eq_right h]
      by_cases a : i = 0
      · subst a; rfl
      · by_cases b : i = 2
        · subst b; rfl
        · simp [a, b]
  | t + 1 => by
    funext i
    show stepN p q (evolN p q seed02 t) i = row (t + 1) i
    rw [row_formula p q t]
    by_cases hi : i ≤ 2 * (t : Int) - 3
    · -- the interior: doubled rule 150, no source
      rw [step_doubled p q (row t) (z t) i (fun k h1 h2 => by
        unfold row; rw [ite_eq_left (show k ≤ 2 * (t : Int) - 1 by omega)])]
      unfold row
      rw [ite_eq_left (show i ≤ 2 * ((t + 1 : Nat) : Int) - 1 by omega)]
      simp only [z]
      unfold src
      have h1 : ¬ (i / 2 = ((t : Nat) : Int)) := by omega
      have h2 : ¬ (i / 2 = ((t : Nat) : Int) - 1) := by omega
      simp [h1, h2]
    · by_cases hj : 2 * (t : Int) + 6 ≤ i
      · -- far right: white
        unfold stepN
        rw [row_far t (i - 2) (by omega), row_far t (i - 1) (by omega), row_far t i (by omega),
          row_far t (i + 1) (by omega), row_far t (i + 2) (by omega), row_far (t + 1) i (by omega)]
        rfl
      · -- the frontier: the eight cells 2t-2 .. 2t+5
        obtain ⟨c, rfl⟩ : ∃ c : Int, i = 2 * (t : Int) + c := ⟨i - 2 * (t : Int), by omega⟩
        have hc1 : -2 ≤ c := by omega
        have hc2 : c ≤ 5 := by omega
        unfold stepN
        rw [show 2 * (t : Int) + c - 2 = 2 * (t : Int) + (c - 2) by omega,
          show 2 * (t : Int) + c - 1 = 2 * (t : Int) + (c - 1) by omega,
          show 2 * (t : Int) + c + 1 = 2 * (t : Int) + (c + 1) by omega,
          show 2 * (t : Int) + c + 2 = 2 * (t : Int) + (c + 2) by omega,
          row_frontier t (c - 2) (by omega), row_frontier t (c - 1) (by omega), row_frontier t c (by omega),
          row_frontier t (c + 1) (by omega), row_frontier t (c + 2) (by omega),
          row_succ_frontier t c hc1 hc2]
        rcases (show c = -2 ∨ c = -1 ∨ c = 0 ∨ c = 1 ∨ c = 2 ∨ c = 3 ∨ c = 4 ∨ c = 5 by omega)
          with e | e | e | e | e | e | e | e <;> subst e <;> cases decide (t % 2 = 1) <;> rfl

/-! ### The reflection argument -/

/-- The field minus its reflection about `-1`. -/
def d (t : Nat) (j : Int) : Bool := xor (z t j) (z t (-2 - j))

/-- The even band `-2 n, -2 n + 2, …, 2 n - 2`. -/
def E (n : Nat) (j : Int) : Bool := decide (j % 2 = 0 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2)

theorem E_t (n : Nat) (j : Int) (h : j % 2 = 0 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2) : E n j = true :=
  decide_eq_true h

theorem E_f (n : Nat) (j : Int) (h : ¬ (j % 2 = 0 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2)) : E n j = false :=
  decide_eq_false h

theorem d_step (t : Nat) (j : Int) :
    d (t + 1) j = xor (xor (xor (xor (d t (j - 1)) (d t j)) (d t (j + 1))) (src t j)) (src t (-2 - j)) := by
  unfold d
  simp only [z]
  rw [show -2 - j - 1 = -2 - (j + 1) by omega, show -2 - j + 1 = -2 - (j - 1) by omega]
  cases z t (j - 1) <;> cases z t j <;> cases z t (j + 1) <;> cases z t (-2 - (j + 1)) <;>
    cases z t (-2 - j) <;> cases z t (-2 - (j - 1)) <;> cases src t j <;> cases src t (-2 - j) <;> rfl

/-- **Rule 150 on the band**: `B E_n = E_n + δ (2 n - 1) + δ (-2 n - 1)`, including `n = 0`. -/
theorem band_step (n : Nat) (j : Int) :
    xor (xor (E n (j - 1)) (E n j)) (E n (j + 1)) =
      xor (xor (E n j) (decide (j = 2 * (n : Int) - 1))) (decide (j = -2 * (n : Int) - 1)) := by
  by_cases r1 : j ≤ -2 * (n : Int) - 2
  · rw [E_f n (j - 1) (by omega), E_f n j (by omega), E_f n (j + 1) (by omega),
      dF j _ (by omega), dF j _ (by omega)] <;> rfl
  · by_cases r2 : j = -2 * (n : Int) - 1
    · by_cases n0 : n = 0
      · subst n0
        rw [E_f 0 (j - 1) (by omega), E_f 0 j (by omega), E_f 0 (j + 1) (by omega),
          dT j _ (by omega), dT j _ (by omega)] <;> rfl
      · rw [E_f n (j - 1) (by omega), E_f n j (by omega), E_t n (j + 1) (by omega),
          dF j _ (by omega), dT j _ (by omega)] <;> rfl
    · by_cases r6 : 2 * (n : Int) ≤ j
      · rw [E_f n (j - 1) (by omega), E_f n j (by omega), E_f n (j + 1) (by omega),
          dF j _ (by omega), dF j _ (by omega)] <;> rfl
      · by_cases r5 : j = 2 * (n : Int) - 1
        · rw [E_t n (j - 1) (by omega), E_f n j (by omega), E_f n (j + 1) (by omega),
            dT j _ (by omega), dF j _ (by omega)] <;> rfl
        · by_cases pe : j % 2 = 0
          · rw [E_f n (j - 1) (by omega), E_t n j (by omega), E_f n (j + 1) (by omega),
              dF j _ (by omega), dF j _ (by omega)] <;> rfl
          · rw [E_t n (j - 1) (by omega), E_f n j (by omega), E_t n (j + 1) (by omega),
              dF j _ (by omega), dF j _ (by omega)] <;> rfl

/-- The band grows by its two new even endpoints. -/
theorem E_succ (n : Nat) (j : Int) :
    E (n + 1) j = xor (xor (E n j) (decide (j = 2 * (n : Int)))) (decide (j = -2 * (n : Int) - 2)) := by
  by_cases a : j = 2 * (n : Int)
  · rw [E_t (n + 1) j (by omega), E_f n j (by omega), dT j _ a, dF j _ (by omega)] <;> rfl
  · by_cases b : j = -2 * (n : Int) - 2
    · rw [E_t (n + 1) j (by omega), E_f n j (by omega), dF j _ a, dT j _ b] <;> rfl
    · rw [dF j _ a, dF j _ b]
      by_cases c : j % 2 = 0 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2
      · rw [E_t (n + 1) j (by omega), E_t n j c] <;> rfl
      · rw [E_f (n + 1) j (by omega), E_f n j c] <;> rfl

theorem src_even (n : Nat) (j : Int) :
    src (2 * n) j = xor (decide (j = 2 * (n : Int))) (decide (j = 2 * (n : Int) - 1)) := by
  unfold src
  rw [show ((2 * n : Nat) : Int) = 2 * (n : Int) by omega, decide_eq_true (show (2 * n) % 2 = 0 by omega)]
  by_cases a : j = 2 * (n : Int)
  · rw [dT j _ a, dF j _ (by omega)] <;> rfl
  · rw [dF j _ a]; cases decide (j = 2 * (n : Int) - 1) <;> rfl

theorem src_odd (n : Nat) (j : Int) : src (2 * n + 1) j = decide (j = 2 * (n : Int) + 1) := by
  unfold src
  rw [show ((2 * n + 1 : Nat) : Int) = 2 * (n : Int) + 1 by omega,
    decide_eq_false (show ¬ (2 * n + 1) % 2 = 0 by omega)]
  cases decide (j = 2 * (n : Int) + 1) <;> rfl

theorem refl_eq (j c : Int) : decide (-2 - j = c) = decide (j = -2 - c) := by
  by_cases h : j = -2 - c
  · rw [dT j _ h, dT _ _ (by omega)]
  · rw [dF j _ h, dF _ _ (by omega)]

/-- **The reflected field is an even band.** -/
theorem d_band : ∀ n, d (2 * n) = E n ∧ d (2 * n + 1) = E (n + 1)
  | 0 => by
    have h0 : d 0 = E 0 := by
      funext j; unfold d; simp only [z]
      exact (E_f 0 j (by omega)).symm
    refine ⟨h0, ?_⟩
    funext j
    rw [d_step, show 2 * 0 = 0 from rfl, h0, band_step, src_even 0 j, src_even 0 (-2 - j), refl_eq, refl_eq,
      E_succ 0 j]
    rw [show -2 - 2 * ((0 : Nat) : Int) = -2 * ((0 : Nat) : Int) - 2 by omega,
      show -2 - (2 * ((0 : Nat) : Int) - 1) = -2 * ((0 : Nat) : Int) - 1 by omega,
      show 2 * ((0 : Nat) : Int) - 1 = -2 * ((0 : Nat) : Int) - 1 by omega]
    cases E 0 j <;> cases decide (j = 2 * ((0 : Nat) : Int)) <;> cases decide (j = -2 * ((0 : Nat) : Int) - 2) <;>
      cases decide (j = -2 * ((0 : Nat) : Int) - 1) <;> rfl
  | n + 1 => by
    obtain ⟨-, h1⟩ := d_band n
    have h2 : d (2 * (n + 1)) = E (n + 1) := by
      funext j
      rw [show 2 * (n + 1) = (2 * n + 1) + 1 by omega, d_step, h1, band_step, src_odd, src_odd, refl_eq]
      rw [show 2 * ((n + 1 : Nat) : Int) - 1 = 2 * (n : Int) + 1 by omega,
        show -2 * ((n + 1 : Nat) : Int) - 1 = -2 - (2 * (n : Int) + 1) by omega]
      cases E (n + 1) j <;> cases decide (j = 2 * (n : Int) + 1) <;> cases decide (j = -2 - (2 * (n : Int) + 1)) <;> rfl
    refine ⟨h2, ?_⟩
    funext j
    rw [d_step, h2, band_step, src_even (n + 1) j, src_even (n + 1) (-2 - j), refl_eq, refl_eq, E_succ (n + 1) j]
    rw [show -2 - 2 * ((n + 1 : Nat) : Int) = -2 * ((n + 1 : Nat) : Int) - 2 by omega,
      show -2 - (2 * ((n + 1 : Nat) : Int) - 1) = -2 * ((n + 1 : Nat) : Int) - 1 by omega]
    cases E (n + 1) j <;> cases decide (j = 2 * ((n + 1 : Nat) : Int)) <;>
      cases decide (j = 2 * ((n + 1 : Nat) : Int) - 1) <;> cases decide (j = -2 * ((n + 1 : Nat) : Int) - 2) <;>
      cases decide (j = -2 * ((n + 1 : Nat) : Int) - 1) <;> rfl

theorem d_zero (t : Nat) : d t 0 = decide (1 ≤ t) := by
  obtain ⟨n, rfl | rfl⟩ : ∃ n, t = 2 * n ∨ t = 2 * n + 1 := ⟨t / 2, by omega⟩
  · rw [(d_band n).1]
    by_cases hn : n = 0
    · subst hn; rw [E_f 0 0 (by omega)] <;> rfl
    · rw [E_t n 0 (by omega), decide_eq_true (show 1 ≤ 2 * n by omega)]
  · rw [(d_band n).2, E_t (n + 1) 0 (by omega), decide_eq_true (show 1 ≤ 2 * n + 1 by omega)]

/-- **Block `-1` flips at every step.** -/
theorem z_clock : ∀ t, z t (-1) = decide (t % 2 = 1)
  | 0 => rfl
  | t + 1 => by
    have h := d_zero t
    unfold d at h
    rw [show (-2 : Int) - 0 = -2 by rfl] at h
    simp only [z]
    rw [show (-1 : Int) - 1 = -2 by rfl, show (-1 : Int) + 1 = 0 by rfl, z_clock t, par_succ]
    have hs : src t (-1) = decide (t = 0) := by
      unfold src
      rw [dF (-1) _ (by omega)]
      by_cases ht : t = 0
      · subst ht; rfl
      · rw [dF (-1) _ (by omega), decide_eq_false ht]; cases decide (t % 2 = 0) <;> rfl
    rw [hs]
    by_cases ht : t = 0
    · subst ht; rfl
    · rw [decide_eq_true (show 1 ≤ t by omega)] at h
      rw [decide_eq_false ht]
      revert h
      cases z t 0 <;> cases z t (-2) <;> cases decide (t % 2 = 1) <;> simp

/-! ### The clock -/

/-- **The clock.** From the black cells `0` and `2`, columns `-2` and `-1` of every `N p q` are
`t mod 2` at every time `t`. -/
theorem clock (p q : Bool) (t : Nat) :
    evolN p q seed02 t (-1) = decide (t % 2 = 1) ∧ evolN p q seed02 t (-2) = decide (t % 2 = 1) := by
  rw [row_formula]
  unfold row
  rw [ite_eq_left (show (-1 : Int) ≤ 2 * (t : Int) - 1 by omega),
    ite_eq_left (show (-2 : Int) ≤ 2 * (t : Int) - 1 by omega), show (-1 : Int) / 2 = -1 by rfl,
    show (-2 : Int) / 2 = -1 by rfl, z_clock]
  exact ⟨rfl, rfl⟩

theorem evolN_shift (p q : Bool) (x : Int → Bool) (k : Int) :
    ∀ t i, evolN p q (fun i => x (i - k)) t i = evolN p q x t (i - k)
  | 0, _ => rfl
  | t + 1, i => by
    show stepN p q (evolN p q (fun i => x (i - k)) t) i = stepN p q (evolN p q x t) (i - k)
    unfold stepN
    rw [evolN_shift p q x k t, evolN_shift p q x k t, evolN_shift p q x k t, evolN_shift p q x k t,
      evolN_shift p q x k t]
    rw [show i - 2 - k = i - k - 2 by omega, show i - 1 - k = i - k - 1 by omega,
      show i + 1 - k = i - k + 1 by omega, show i + 2 - k = i - k + 2 by omega]

/-- **Column `0` alternates** from the black cells `2` and `4`. -/
theorem column0_alternates (p q : Bool) (t : Nat) :
    evolN p q (fun i => decide (i = 2 ∨ i = 4)) t 0 = decide (t % 2 = 1) := by
  have h : (fun i : Int => decide (i = 2 ∨ i = 4)) = fun i => seed02 (i - 2) := by
    funext i; unfold seed02
    exact decide_eq_decide.2 ⟨fun h => by omega, fun h => by omega⟩
  rw [h, evolN_shift, show (0 : Int) - 2 = -2 by rfl]
  exact (clock p q t).2

end Rule30RadiusTwoClock
end Ruliology.CellularAutomata
