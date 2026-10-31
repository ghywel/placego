module

public import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Rule 30: the longest ether-pair episode behind a black right edge

Read a row of rule 30 from its rightmost black cell, as in `Rule30FrozenRuler`: bit `k` of the
edge code is the cell `k` places behind the edge cell, and `iter t x` is the code at time `t`
(the edge map `T`). PR69 (`Rule30EtherGrounding`) introduced in this frame the four-column,
eight-tick ether `ether i t` (a two-sided solution, `ether_step`) and proved that no two adjacent
depths of a black-edge code can follow it *eventually*. This module computes how long they can
follow it. An **episode** at depths `k, k + 1` with phase `(i, q)` and onset `s` is a run of
consecutive ticks `t ≥ s` with `iter t x k = ether i (t + q)` and
`iter t x (k + 1) = ether (i + 1) (t + q)`.

* `episode_bound`: for every code `x` with a black edge (`x 0 = true`; finite or not), every depth
  `k ≥ 1`, every phase `(i, q)` and every onset `s`, no episode has `Lw k + 1` ticks, where
  `Lw k = floor(2k/3) + 4 - [k ≡ 0 or 2 (mod 6)]` (`episode_bound_all`: the bound for every `k`).
* `episode_witness`: GC2328's witness (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an
  episode of `Lw k` ticks at depths `k, k + 1` for every `k ≥ 1`.
* `episode_max`: together, **the longest episode is `M(k) = Lw k` for every `k ≥ 1`**.
* `witness_unique`: at phase class `7` (`s + q + 2i + 6k ≡ 7 (mod 8)`, the witness's class) every
  code with an episode of `Lw k` ticks has the witness's prefix (bits `0 .. k + 1`) at its onset.
  Bits beyond `k + 1` are free, and other phase classes may also attain `Lw k`.

Scope: a moving black right edge in PR69's frame. Nothing here concerns a fixed wall, the center
column or densities.

**The argument** (a front with a potential). `ether i t = e (t + 2 i)` with
`e = (1,1,0,1,0,1,0,0)` (`ether_eq`), so an episode's reference at depth `j` is the wave
`e (t + 2 j + c)` for one of 8 phase classes `c`, and `iter_add` moves the onset to `0`.

1. *Two-sided frame* (`X`, `E`, `D`). Depth `n : Nat` stands for edge depth `n - 8`; the cells
   above the edge are white. The black-edge state and the wave obey
   `X_n(t+1) = X_n(t) ⊕ (X_(n-1)(t) ∨ X_(n-2)(t))` at every `n ≥ 2` (`X_step`, `E_step`), so the
   mismatch `D = X ⊕ E` obeys `D_n(t+1) = D_n(t) ⊕ F_φ(D_(n-1)(t), D_(n-2)(t))`, `φ = t + 2n + c`
   (`D_step`), with `F` OR at `φ ∈ {0, 6}`, `¬a ∧ b` at `{1, 4}`, `a ∧ ¬b` at `{2, 3}`, AND at
   `{5, 7}`; `F(0, 0) = 0`.
2. *Clean tail* (`tail`, `tail_inv`). Replace the code beyond depth `k + 1` by the wave at time `0`.
   Prefix autonomy (`iter_agree`) keeps the pair; during an episode no mismatch reaches depth `k`.
   The mismatch is bounded above, and some white depth `-4 .. -1` mismatches, so the **front**
   (top mismatch) exists at every time (`low_one`, `top_exists`, `front_succ`).
3. *Lemma A* (`table`, `step`; 32 local cases): with front phase `ψ = t + 2R + 2 + c`, the front
   moves `+2` at `ψ ∈ {2, 4, 6, 7}`, `+1` at `ψ = 0`, `+1` at `ψ = 3` iff `D_(R-1) = 0`, `+1` at
   `ψ = 5` iff `D_(R-1) = 1`, else `0`, or retreats at `ψ = 1` when `D_(R-1) = D_(R-2) = 1`; every
   non-retreat move keeps the doubled potential `2R + g2(ψ) - 3t`,
   `g2 = (-3, 0, 3, -2, 1, -4, -1, 2)` (here `G = g2 + 4` and offset depths).
4. *Lemma B*: a retreat lands on an even phase and the only move onto phase `1` is the `+2` move
   from phase `4`, which leaves the cell below the new front clean; so nothing retreats from time
   `1` on and the potential is constant (`pot_inv`).
5. *Floors at time 1* (`floor_case`, `floor_arith`). The cells at depths `≤ 0` are fixed, which
   bounds the front at time `1` below. At `c = 2, 4` the only row healing every depth `≥ 1` at time
   `1` never becomes clean (`heal2`, `heal4`), which a clean tail does; at `c = 7` that row is the
   witness's (`heal7`) and every other row has potential `≥ 0`.
6. *Front comparison* (`final_arith`, `wit_front`, `wit_arith2`): at time `Lw k` the front is at
   depth `≥ k` — through the potential floor, or along the witness lane, whose moves are forced
   (front phases `2 → 7 → 4 → 1`, moves `+2, +2, +2, 0`, front `Rw`). That contradicts step 2.

**Provenance.** Local's (Claude's) hand proof "Proof 1: a front potential" (inquisition round 5,
L1259), carried two-party by GPT in GC2333 (which also supplied the scope repair: right-bounded
mismatch rather than finite support). The finite tables mirror the round's certificate
`ether_front_potential_certificate.py`. The method, a front state with a potential certified on
local patterns, is the kit's `Rule30EtherThreeErosion` (period-three ether). The ether, its frame
and `ether_step` are PR69's `Rule30EtherGrounding`, not in this kit build: `ether` is copied here
verbatim.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30EtherEpisode

set_option autoImplicit false

open Rule30FrozenRuler

/-! ### The ether and the wave -/

/-- PR69's ether (`Rule30EtherGrounding.ether`), copied verbatim: four spatial columns of the
one-in-four ether, bit `t` read in time order. -/
def ether (i t : Nat) : Bool :=
  (match i % 4 with
   | 0 => 43 | 1 => 202 | 2 => 178 | _ => 172).testBit (t % 8)

/-- The episode length `floor(2k/3) + 4 - [k = 0, 2 (mod 6)]`. -/
def Lw (k : Nat) : Nat := 2 * k / 3 + 4 - (if k % 6 = 0 ∨ k % 6 = 2 then 1 else 0)

/-- The wave `e = (1,1,0,1,0,1,0,0)`, period 8. -/
def e (p : Nat) : Bool := (43 : Nat).testBit (p % 8)

theorem e_mod (p : Nat) : e p = e (p % 8) := by
  simp only [e, Nat.mod_mod]

theorem e_congr {p q : Nat} (h : p % 8 = q % 8) : e p = e q := by
  simp only [e, h]

theorem ether_table : ∀ i, i < 4 → ∀ t, t < 8 → ether i t = e (t + 2 * i) := by decide

/-- `ether i t = e (t + 2 i)`. -/
theorem ether_eq (i t : Nat) : ether i t = e (t + 2 * i) := by
  have h := ether_table (i % 4) (Nat.mod_lt _ (by decide)) (t % 8) (Nat.mod_lt _ (by decide))
  have h1 : ether i t = ether (i % 4) (t % 8) := by
    simp only [ether, Nat.mod_mod]
  rw [h1, h]
  exact e_congr (by omega)

theorem wave_table : ∀ r, r < 8 → e (r + 5) = xor (e (r + 4)) (e (r + 2) || e r) := by decide

/-- The wave obeys the edge rule: `e (p + 1) = e p ⊕ (e (p - 2) ∨ e (p - 4))`. -/
theorem wave (p : Nat) : e (p + 5) = xor (e (p + 4)) (e (p + 2) || e p) := by
  have h := wave_table (p % 8) (Nat.mod_lt _ (by decide))
  rw [e_congr (show (p + 5) % 8 = (p % 8 + 5) % 8 by omega),
    e_congr (show (p + 4) % 8 = (p % 8 + 4) % 8 by omega),
    e_congr (show (p + 2) % 8 = (p % 8 + 2) % 8 by omega), e_mod p, h]

/-- PR69's `ether_step` (positive control): the ether is a two-sided solution of the edge rule. -/
theorem ether_step (i t : Nat) :
    ether i (t + 1) = xor (ether i t) (ether (i + 3) t || ether (i + 2) t) := by
  rw [ether_eq, ether_eq, ether_eq, ether_eq]
  have h := wave (t + 2 * i + 4)
  rw [e_congr (show (t + 2 * i + 4 + 5) % 8 = (t + 1 + 2 * i) % 8 by omega),
    e_congr (show (t + 2 * i + 4 + 4) % 8 = (t + 2 * i) % 8 by omega),
    e_congr (show (t + 2 * i + 4 + 2) % 8 = (t + 2 * (i + 3)) % 8 by omega),
    e_congr (show (t + 2 * i + 4) % 8 = (t + 2 * (i + 2)) % 8 by omega)] at h
  exact h

/-! ### The mismatch increment -/

/-- The mismatch increment at a cell of phase `φ`: OR at `φ ∈ {0, 6}`, `¬a ∧ b` at `{1, 4}`,
`a ∧ ¬b` at `{2, 3}`, AND at `{5, 7}`. -/
def F (φ : Nat) (a b : Bool) : Bool :=
  match φ with
  | 0 => a || b
  | 1 => !a && b
  | 2 => a && !b
  | 3 => a && !b
  | 4 => !a && b
  | 5 => a && b
  | 6 => a || b
  | _ => a && b

theorem F_zero (φ : Nat) : F φ false false = false := by
  unfold F; split <;> rfl

theorem F_table : ∀ r, r < 8 → ∀ a b : Bool,
    F ((r + 4) % 8) a b = xor ((xor (e (r + 2)) a) || (xor (e r) b)) (e (r + 2) || e r) := by
  decide

theorem F_spec (p : Nat) (a b : Bool) :
    F ((p + 4) % 8) a b = xor ((xor (e (p + 2)) a) || (xor (e p) b)) (e (p + 2) || e p) := by
  have h := F_table (p % 8) (Nat.mod_lt _ (by decide)) a b
  rw [show (p + 4) % 8 = (p % 8 + 4) % 8 by omega,
    e_congr (show (p + 2) % 8 = (p % 8 + 2) % 8 by omega), e_mod p, h]

/-! ### The two-sided frame (depth `n` stands for edge depth `n - 8`) -/

/-- The black-edge state at offset depth `n` (edge depth `n - 8`; white at negative depths). -/
def X (x : Nat → Bool) (n t : Nat) : Bool := if n < 8 then false else iter t x (n - 8)

/-- The reference wave of phase class `c` at offset depth `n`. -/
def E (c n t : Nat) : Bool := e (t + 2 * n + c)

/-- The mismatch. -/
def D (x : Nat → Bool) (c n t : Nat) : Bool := xor (X x n t) (E c n t)

theorem X_step (x : Nat → Bool) (n t : Nat) (hn : 2 ≤ n) :
    X x n (t + 1) = xor (X x n t) (X x (n - 1) t || X x (n - 2) t) := by
  unfold X
  by_cases h8 : n < 8
  · have h1 : n - 1 < 8 := by omega
    have h2 : n - 2 < 8 := by omega
    simp [h8, h1, h2]
  · by_cases h9 : n = 8
    · subst h9; simp [iter, T]
    · by_cases h10 : n = 9
      · subst h10; simp [iter, T]
      · obtain ⟨m, rfl⟩ : ∃ m, n = m + 10 := ⟨n - 10, by omega⟩
        have a1 : m + 10 - 8 = m + 2 := by omega
        have a2 : m + 10 - 1 - 8 = m + 1 := by omega
        have a3 : m + 10 - 2 - 8 = m := by omega
        have b1 : ¬ (m + 10 - 1 < 8) := by omega
        have b2 : ¬ (m + 10 - 2 < 8) := by omega
        simp only [h8, b1, b2, ite_false, a1, a2, a3]
        rfl

theorem E_step (c n t : Nat) (hn : 2 ≤ n) :
    E c n (t + 1) = xor (E c n t) (E c (n - 1) t || E c (n - 2) t) := by
  unfold E
  have h := wave (t + 2 * (n - 2) + c)
  rw [show t + 1 + 2 * n + c = t + 2 * (n - 2) + c + 5 by omega,
    show t + 2 * n + c = t + 2 * (n - 2) + c + 4 by omega,
    show t + 2 * (n - 1) + c = t + 2 * (n - 2) + c + 2 by omega]
  exact h

theorem F_E (c n t : Nat) (hn : 2 ≤ n) (a b : Bool) :
    F ((t + 2 * n + c) % 8) a b =
      xor ((xor (E c (n - 1) t) a) || (xor (E c (n - 2) t) b))
        (E c (n - 1) t || E c (n - 2) t) := by
  unfold E
  rw [show t + 2 * n + c = t + 2 * (n - 2) + c + 4 by omega,
    show t + 2 * (n - 1) + c = t + 2 * (n - 2) + c + 2 by omega]
  exact F_spec _ a b

theorem bool_step (Xn Xa Xb En Ea Eb : Bool) :
    xor (xor Xn (Xa || Xb)) (xor En (Ea || Eb)) =
      xor (xor Xn En) (xor ((xor Ea (xor Xa Ea)) || (xor Eb (xor Xb Eb))) (Ea || Eb)) := by
  cases Xn <;> cases Xa <;> cases Xb <;> cases En <;> cases Ea <;> cases Eb <;> rfl

/-- **The mismatch rule.** `D_n(t+1) = D_n(t) ⊕ F_φ(D_(n-1)(t), D_(n-2)(t))`, `φ = t + 2n + c`. -/
theorem D_step (x : Nat → Bool) (c n t : Nat) (hn : 2 ≤ n) :
    D x c n (t + 1) =
      xor (D x c n t) (F ((t + 2 * n + c) % 8) (D x c (n - 1) t) (D x c (n - 2) t)) := by
  unfold D
  rw [X_step x n t hn, E_step c n t hn, F_E c n t hn]
  exact bool_step _ _ _ _ _ _

theorem D_step' (x : Nat → Bool) (c n t n1 n2 φ : Nat) (hn : 2 ≤ n) (h1 : n1 = n - 1)
    (h2 : n2 = n - 2) (hφ : φ = (t + 2 * n + c) % 8) :
    D x c n (t + 1) = xor (D x c n t) (F φ (D x c n1 t) (D x c n2 t)) := by
  subst h1 h2 hφ; exact D_step x c n t hn

theorem D_low (x : Nat → Bool) (c n t : Nat) (hn : n < 8) : D x c n t = e (t + 2 * n + c) := by
  simp [D, X, E, hn]

theorem D_eight (x : Nat → Bool) (hx : x 0 = true) (c t : Nat) :
    D x c 8 t = ! e (t + 16 + c) := by
  simp [D, X, E, iter_zero, hx]

theorem X_ge (x : Nat → Bool) (n t : Nat) (hn : 8 ≤ n) : X x n t = iter t x (n - 8) := by
  simp [X, show ¬ n < 8 by omega]

theorem xor_false_eq {p q : Bool} (h : xor p q = false) : p = q := by
  cases p <;> cases q <;> simp_all

/-! ### The front -/

/-- `R` is the front at time `t`: the top mismatch. -/
abbrev FrontAt (x : Nat → Bool) (c t R : Nat) : Prop :=
  D x c R t = true ∧ ∀ n, R < n → D x c n t = false

theorem top_exists (f : Nat → Bool) (m : Nat) (hm : f m = true) :
    ∀ d, (∀ n, m + d ≤ n → f n = false) → ∃ R, m ≤ R ∧ f R = true ∧ ∀ n, R < n → f n = false := by
  intro d
  induction d with
  | zero =>
    intro h
    have h' := h m (by omega)
    rw [hm] at h'
    exact absurd h' (by decide)
  | succ d ih =>
    intro h
    cases hfd : f (m + d) with
    | true => exact ⟨m + d, by omega, hfd, fun n hn => h n (by omega)⟩
    | false =>
      apply ih
      intro n hn
      by_cases hnd : n = m + d
      · rw [hnd]; exact hfd
      · exact h n (by omega)

theorem front_ge {x : Nat → Bool} {c t R : Nat} (hF : FrontAt x c t R) {m : Nat}
    (hm : D x c m t = true) : m ≤ R := by
  by_cases h : m ≤ R
  · exact h
  · have h' := hF.2 m (by omega)
    rw [hm] at h'
    exact absurd h' (by decide)

theorem low_table :
    ∀ r, r < 8 → (e (r + 8) || (e (r + 10) || (e (r + 12) || e (r + 14)))) = true := by
  decide

/-- Among the white depths `-4 .. -1` some cell mismatches the wave: the front is at least `-4`. -/
theorem low_one (x : Nat → Bool) (c t : Nat) : ∃ m, 4 ≤ m ∧ m ≤ 7 ∧ D x c m t = true := by
  have h := low_table ((t + c) % 8) (Nat.mod_lt _ (by decide))
  have h4 : D x c 4 t = e ((t + c) % 8 + 8) := by
    rw [D_low x c 4 t (by decide)]; exact e_congr (by omega)
  have h5 : D x c 5 t = e ((t + c) % 8 + 10) := by
    rw [D_low x c 5 t (by decide)]; exact e_congr (by omega)
  have h6 : D x c 6 t = e ((t + c) % 8 + 12) := by
    rw [D_low x c 6 t (by decide)]; exact e_congr (by omega)
  have h7 : D x c 7 t = e ((t + c) % 8 + 14) := by
    rw [D_low x c 7 t (by decide)]; exact e_congr (by omega)
  rw [← h4, ← h5, ← h6, ← h7] at h
  simp only [Bool.or_eq_true] at h
  rcases h with h | h | h | h
  · exact ⟨4, by decide, by decide, h⟩
  · exact ⟨5, by decide, by decide, h⟩
  · exact ⟨6, by decide, by decide, h⟩
  · exact ⟨7, by decide, by decide, h⟩

/-! ### The clean tail -/

/-- The code with everything beyond depth `k + 1` replaced by the reference wave at time `0`. -/
def tail (x : Nat → Bool) (k c : Nat) : Nat → Bool :=
  fun j => if j ≤ k + 1 then x j else e (2 * j + c)

theorem tail_agree (x : Nat → Bool) (k c : Nat) : AgreeBelow (k + 2) x (tail x k c) := by
  intro i hi
  simp [tail, show i ≤ k + 1 by omega]

theorem tail_clean (x : Nat → Bool) (k c : Nat) :
    ∀ n, k + 10 ≤ n → D (tail x k c) c n 0 = false := by
  intro n hn
  have h2 : ¬ (n - 8 ≤ k + 1) := by omega
  rw [D, X_ge _ n 0 (by omega)]
  simp only [iter, tail, h2, ite_false, E]
  rw [e_congr (show (2 * (n - 8) + c) % 8 = (0 + 2 * n + c) % 8 by omega)]
  exact Bool.xor_self _

/-- During an episode on ticks `0 .. L`, the clean tail stays clean: no mismatch at depth `≥ k`. -/
theorem tail_inv (x : Nat → Bool) (c k L : Nat)
    (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false)
    (hp : ∀ u, u ≤ L → D x c (k + 8) u = false ∧ D x c (k + 9) u = false) :
    ∀ u, u ≤ L → ∀ n, k + 8 ≤ n → D x c n u = false := by
  intro u
  induction u with
  | zero =>
    intro hu n hn
    by_cases h8 : n = k + 8
    · rw [h8]; exact (hp 0 hu).1
    · by_cases h9 : n = k + 9
      · rw [h9]; exact (hp 0 hu).2
      · exact h0 n (by omega)
  | succ u ih =>
    intro hu n hn
    by_cases h8 : n = k + 8
    · rw [h8]; exact (hp _ hu).1
    · by_cases h9 : n = k + 9
      · rw [h9]; exact (hp _ hu).2
      · rw [D_step x c n u (by omega), ih (by omega) n (by omega), ih (by omega) (n - 1) (by omega),
          ih (by omega) (n - 2) (by omega), F_zero]
        rfl

theorem front_zero (x : Nat → Bool) (c k : Nat) (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false) :
    ∃ R, 4 ≤ R ∧ FrontAt x c 0 R := by
  obtain ⟨m, hm4, _, hm⟩ := low_one x c 0
  obtain ⟨R, hmR, hR, hR'⟩ :=
    top_exists (fun n => D x c n 0) m hm (k + 10) (fun n hn => h0 n (by omega))
  exact ⟨R, by omega, hR, hR'⟩

/-! ### Lemma A: the front's moves (32 local cases), and the potential -/

/-- Doubled potential weights, shifted: `G = 2 g + 4` with
`g = (-3/2, 0, 3/2, -1, 1/2, -2, -1/2, 1)`. -/
def G (ψ : Nat) : Nat :=
  match ψ with
  | 0 => 1 | 1 => 4 | 2 => 7 | 3 => 2 | 4 => 5 | 5 => 0 | 6 => 3 | _ => 6

/-- The front's move at front phase `ψ` (the phase of the cell above the front) with
`a = D_(R-1)`: `+2` at `ψ ∈ {2, 4, 6, 7}`, `+1` at `ψ = 0`, at `ψ = 3` iff `a = 0` and at `ψ = 5`
iff `a = 1`; otherwise `0` (or a retreat, at `ψ = 1` with `a = b = 1`). -/
def dR (ψ : Nat) (a : Bool) : Nat :=
  if F ((ψ + 2) % 8) false true = true then 2 else if F ψ true a = true then 1 else 0

/-- The front's moves as in the hand proof's table. -/
theorem dR_table (a : Bool) :
    dR 0 a = 1 ∧ dR 1 a = 0 ∧ dR 2 a = 2 ∧ dR 3 a = (if a then 0 else 1) ∧ dR 4 a = 2 ∧
      dR 5 a = (if a then 1 else 0) ∧ dR 6 a = 2 ∧ dR 7 a = 2 := by
  cases a <;> decide

/-- The finite table behind Lemma A, the potential and Lemma B. -/
abbrev TableOK (ψ : Nat) (a b : Bool) : Prop :=
  (¬ (ψ = 1 ∧ a = true ∧ b = true) →
    dR ψ a ≤ 2 ∧
    (dR ψ a = 2 → F ((ψ + 2) % 8) false true = true) ∧
    (dR ψ a = 1 → F ψ true a = true ∧ F ((ψ + 2) % 8) false true = false) ∧
    (dR ψ a = 0 → xor true (F ((ψ + 6) % 8) a b) = true ∧ F ψ true a = false ∧
      F ((ψ + 2) % 8) false true = false) ∧
    2 * dR ψ a + G ((ψ + 1 + 2 * dR ψ a) % 8) = G ψ + 3 ∧
    ((ψ + 1 + 2 * dR ψ a) % 8 = 1 → dR ψ a = 2 ∧ F ψ true a = false)) ∧
  ((ψ = 1 ∧ a = true ∧ b = true) →
    xor true (F ((ψ + 6) % 8) a b) = false ∧ F ψ true a = false ∧
      F ((ψ + 2) % 8) false true = false)

set_option synthInstance.maxSize 4096 in
set_option synthInstance.maxHeartbeats 400000 in
theorem table : ∀ ψ, ψ < 8 → ∀ a b : Bool, TableOK ψ a b := by decide

/-- **Lemma A.** One step of a front `R` with front phase `ψ`, `a = D_(R-1)`, `b = D_(R-2)`. Without
a retreat the new front is `R + dR ψ a`, the doubled potential `2R + G ψ - 3t` is unchanged, and
when the new front phase is `1` the cell below the new front is clean (Lemma B). A retreat (`ψ = 1`,
`a = b = 1`) clears every depth `≥ R`. -/
theorem step (x : Nat → Bool) (c t R ψ : Nat) (a b : Bool) (hR : 4 ≤ R) (hF : FrontAt x c t R)
    (hψ : (t + 2 * R + 2 + c) % 8 = ψ) (ha : D x c (R - 1) t = a) (hb : D x c (R - 2) t = b) :
    (¬ (ψ = 1 ∧ a = true ∧ b = true) →
      FrontAt x c (t + 1) (R + dR ψ a) ∧
      2 * (R + dR ψ a) + G ((t + 1 + 2 * (R + dR ψ a) + 2 + c) % 8) = 2 * R + G ψ + 3 ∧
      ((t + 1 + 2 * (R + dR ψ a) + 2 + c) % 8 = 1 → D x c (R + dR ψ a - 1) (t + 1) = false)) ∧
    ((ψ = 1 ∧ a = true ∧ b = true) → ∀ n, R ≤ n → D x c n (t + 1) = false) := by
  have hψ8 : ψ < 8 := by omega
  have v3 : ∀ n, R + 3 ≤ n → D x c n (t + 1) = false := by
    intro n hn
    rw [D_step x c n t (by omega), hF.2 n (by omega), hF.2 (n - 1) (by omega),
      hF.2 (n - 2) (by omega), F_zero]
    rfl
  have v2 : D x c (R + 2) (t + 1) = F ((ψ + 2) % 8) false true := by
    rw [D_step' x c (R + 2) t (R + 1) R ((ψ + 2) % 8) (by omega) (by omega) (by omega) (by omega),
      hF.2 (R + 2) (by omega), hF.2 (R + 1) (by omega), hF.1, Bool.false_xor]
  have v1 : D x c (R + 1) (t + 1) = F ψ true a := by
    rw [D_step' x c (R + 1) t R (R - 1) ψ (by omega) (by omega) (by omega) (by omega),
      hF.2 (R + 1) (by omega), hF.1, ha, Bool.false_xor]
  have v0 : D x c R (t + 1) = xor true (F ((ψ + 6) % 8) a b) := by
    rw [D_step' x c R t (R - 1) (R - 2) ((ψ + 6) % 8) (by omega) rfl rfl (by omega), hF.1, ha, hb]
  obtain ⟨Tm, Tr⟩ := table ψ hψ8 a b
  have hph : ∀ d, (t + 1 + 2 * (R + d) + 2 + c) % 8 = (ψ + 1 + 2 * d) % 8 := by
    intro d; omega
  refine ⟨fun hnr => ?_, fun hr => ?_⟩
  · obtain ⟨hle, h2, h1, h0, hpot, hph1⟩ := Tm hnr
    refine ⟨⟨?_, ?_⟩, ?_, ?_⟩
    · rcases (by omega : dR ψ a = 0 ∨ dR ψ a = 1 ∨ dR ψ a = 2) with h | h | h
      · rw [h, Nat.add_zero, v0]; exact (h0 h).1
      · rw [h, v1]; exact (h1 h).1
      · rw [h, v2]; exact h2 h
    · intro n hn
      by_cases hn3 : R + 3 ≤ n
      · exact v3 n hn3
      · rcases (by omega : dR ψ a = 0 ∨ dR ψ a = 1 ∨ dR ψ a = 2) with h | h | h
        · rcases (by omega : n = R + 1 ∨ n = R + 2) with rfl | rfl
          · rw [v1]; exact (h0 h).2.1
          · rw [v2]; exact (h0 h).2.2
        · have hn2 : n = R + 2 := by omega
          subst hn2; rw [v2]; exact (h1 h).2
        · omega
    · rw [hph]; omega
    · rw [hph]; intro h1'
      obtain ⟨_, hFa⟩ := hph1 h1'
      rw [show R + dR ψ a - 1 = R + 1 by omega, v1]; exact hFa
  · intro n hn
    obtain ⟨r0, r1, r2⟩ := Tr hr
    by_cases hn3 : R + 3 ≤ n
    · exact v3 n hn3
    · rcases (by omega : n = R ∨ n = R + 1 ∨ n = R + 2) with rfl | rfl | rfl
      · rw [v0]; exact r0
      · rw [v1]; exact r1
      · rw [v2]; exact r2

/-- The front exists at the next time, with the guard of Lemma B: a retreat lands on an even
phase, and the only move onto phase `1` is the `+2` move from phase `4`, which leaves the cell
below the new front clean. -/
theorem front_succ (x : Nat → Bool) (c t R : Nat) (hR : 4 ≤ R) (hF : FrontAt x c t R) :
    ∃ R', 4 ≤ R' ∧ FrontAt x c (t + 1) R' ∧
      ((t + 1 + 2 * R' + 2 + c) % 8 = 1 → D x c (R' - 1) (t + 1) = false) := by
  obtain ⟨Sm, Sr⟩ := step x c t R ((t + 2 * R + 2 + c) % 8) (D x c (R - 1) t) (D x c (R - 2) t)
    hR hF rfl rfl rfl
  by_cases hr : ((t + 2 * R + 2 + c) % 8 = 1 ∧ D x c (R - 1) t = true ∧ D x c (R - 2) t = true)
  · have hcl := Sr hr
    obtain ⟨m, hm4, _, hm⟩ := low_one x c (t + 1)
    obtain ⟨R', hmR, hR', hR''⟩ := top_exists (fun n => D x c n (t + 1)) m hm R
      (fun n hn => hcl n (by omega))
    refine ⟨R', by omega, ⟨hR', hR''⟩, fun h => ?_⟩
    have h1 := hr.1
    exfalso; omega
  · obtain ⟨hF', _, hph⟩ := Sm hr
    exact ⟨_, by omega, hF', hph⟩

/-! ### The potential from time 1 on -/

/-- The invariant from time `1` on: a front, the guard of Lemma B, and the potential floor. -/
abbrev Good (x : Nat → Bool) (c Kc t R : Nat) : Prop :=
  4 ≤ R ∧ FrontAt x c t R ∧ ((t + 2 * R + 2 + c) % 8 = 1 → D x c (R - 1) t = false) ∧
    3 * t + Kc ≤ 2 * R + G ((t + 2 * R + 2 + c) % 8)

/-- No retreat from time `1` on, so the potential never drops. -/
theorem pot_inv (x : Nat → Bool) (c Kc : Nat) (h1 : ∃ R, Good x c Kc 1 R) :
    ∀ u, ∃ R, Good x c Kc (u + 1) R := by
  intro u
  induction u with
  | zero => exact h1
  | succ u ih =>
    obtain ⟨R, hR4, hF, hg, hpot⟩ := ih
    obtain ⟨Sm, _⟩ := step x c (u + 1) R ((u + 1 + 2 * R + 2 + c) % 8) (D x c (R - 1) (u + 1))
      (D x c (R - 2) (u + 1)) hR4 hF rfl rfl rfl
    have hnr : ¬ ((u + 1 + 2 * R + 2 + c) % 8 = 1 ∧ D x c (R - 1) (u + 1) = true ∧
        D x c (R - 2) (u + 1) = true) := by
      rintro ⟨h1, h2, _⟩
      rw [hg h1] at h2
      exact absurd h2 (by decide)
    obtain ⟨hF', hpot', hph'⟩ := Sm hnr
    refine ⟨_, by omega, hF', hph', ?_⟩
    omega

/-! ### Floors at time 1 -/

/-- Lower bounds on the front at time `1` (offset depths; `9` is edge depth `1`). -/
def lb (c : Nat) : Nat :=
  match c with
  | 0 => 6 | 1 => 8 | 2 => 9 | 3 => 8 | 4 => 9 | 5 => 8 | 6 => 8 | _ => 9

/-- The doubled potential floors `F2_c`, shifted by `20`: `-5, -2, 1, -4, -1, -6, -3, 0`. -/
def K (c : Nat) : Nat :=
  match c with
  | 0 => 15 | 1 => 18 | 2 => 21 | 3 => 16 | 4 => 19 | 5 => 14 | 6 => 17 | _ => 20

theorem G_cases (p : Nat) :
    (p % 8 = 0 ∧ G (p % 8) = 1) ∨ (p % 8 = 1 ∧ G (p % 8) = 4) ∨ (p % 8 = 2 ∧ G (p % 8) = 7) ∨
    (p % 8 = 3 ∧ G (p % 8) = 2) ∨ (p % 8 = 4 ∧ G (p % 8) = 5) ∨ (p % 8 = 5 ∧ G (p % 8) = 0) ∨
    (p % 8 = 6 ∧ G (p % 8) = 3) ∨ (p % 8 = 7 ∧ G (p % 8) = 6) := by
  have h : p % 8 < 8 := Nat.mod_lt _ (by decide)
  generalize p % 8 = r at h ⊢
  revert r; decide

theorem c_cases (c : Nat) (hc : c < 8) :
    c = 0 ∨ c = 1 ∨ c = 2 ∨ c = 3 ∨ c = 4 ∨ c = 5 ∨ c = 6 ∨ c = 7 := by omega

/-- The floor: a front at time `1` at or above `lb c` has doubled potential at least `F2_c`. -/
theorem floor_arith (c : Nat) (hc : c < 8) (R : Nat) (hR : lb c ≤ R) :
    3 * 1 + K c ≤ 2 * R + G ((1 + 2 * R + 2 + c) % 8) := by
  rcases G_cases (1 + 2 * R + 2 + c) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] <;>
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp only [lb, K] at hR ⊢ <;> omega

theorem Lw_cases (k : Nat) : ((k % 6 = 0 ∨ k % 6 = 2) ∧ Lw k = 2 * k / 3 + 3) ∨
    (¬ (k % 6 = 0 ∨ k % 6 = 2) ∧ Lw k = 2 * k / 3 + 4) := by
  unfold Lw
  split
  · next h => left; exact ⟨h, by omega⟩
  · next h => right; exact ⟨h, by omega⟩

/-- **Front comparison at the end of the episode.** At time `Lw k` a front carrying the floor
potential is at depth `≥ k`. (The `(4, 6)` periodicity of the potential is absorbed by `omega`.) -/
theorem final_arith (c : Nat) (hc : c < 8) (k : Nat) (R : Nat)
    (h : 3 * Lw k + K c ≤ 2 * R + G ((Lw k + 2 * R + 2 + c) % 8)) : k + 8 ≤ R := by
  have hL := Lw_cases k
  rcases G_cases (Lw k + 2 * R + 2 + c) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] at h <;>
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp only [K] at h <;> omega

/-! ### The witness lane at phase class 7 -/

/-- The witness front (offset depths): `6n + 4, 6n + 4, 6n + 6, 6n + 8` at `t = 4n .. 4n + 3`,
i.e. edge depths `R_w(t) = 6n - 4, 6n - 4, 6n - 2, 6n`. -/
def Rw (t : Nat) : Nat := 6 * (t / 4) + 4 + 2 * (t % 4 - 1)

theorem wit_move (t : Nat) (a : Bool) (ha : (t + 2 * Rw t + 2 + 7) % 8 = 1 → a = false) :
    Rw t + dR ((t + 2 * Rw t + 2 + 7) % 8) a = Rw (t + 1) := by
  have hd : ∀ a : Bool, dR 2 a = 2 ∧ dR 7 a = 2 ∧ dR 4 a = 2 := by decide
  have hd1 : dR 1 false = 0 := by decide
  rcases (by omega : t % 4 = 0 ∨ t % 4 = 1 ∨ t % 4 = 2 ∨ t % 4 = 3) with h | h | h | h
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 1 := by unfold Rw; omega
    rw [hψ, ha hψ, hd1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 2 := by unfold Rw; omega
    rw [hψ, (hd a).1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 7 := by unfold Rw; omega
    rw [hψ, (hd a).2.1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 4 := by unfold Rw; omega
    rw [hψ, (hd a).2.2]; unfold Rw; omega

/-- **The witness front.** At phase class `7`, a row whose mismatch vanishes at every edge depth
`≥ 1` heals at times `1, 2` and then has the forced front `Rw t` (cycle of front phases
`2 → 7 → 4 → 1`, moves `+2, +2, +2, 0`). -/
theorem wit_front (x : Nat → Bool) (hx : x 0 = true) (h9 : ∀ n, 9 ≤ n → D x 7 n 0 = false) :
    ∀ u, FrontAt x 7 (u + 1) (Rw (u + 1)) ∧
      ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8 = 1 → D x 7 (Rw (u + 1) - 1) (u + 1) = false) := by
  intro u
  induction u with
  | zero =>
    have d8 : D x 7 8 0 = true := by rw [D_eight x hx]; decide
    have d7 : D x 7 7 0 = true := by rw [D_low x 7 7 0 (by decide)]; decide
    have q9 : D x 7 9 1 = false := by
      rw [D_step' x 7 9 0 8 7 1 (by decide) rfl rfl (by decide), h9 9 (by decide), d8, d7]; decide
    have q10 : D x 7 10 1 = false := by
      rw [D_step' x 7 10 0 9 8 3 (by decide) rfl rfl (by decide), h9 10 (by decide),
        h9 9 (by decide), d8]; decide
    have qn : ∀ n, 11 ≤ n → D x 7 n 1 = false := by
      intro n hn
      rw [D_step x 7 n 0 (by omega), h9 n (by omega), h9 (n - 1) (by omega), h9 (n - 2) (by omega),
        F_zero]; rfl
    have hR1 : Rw (0 + 1) = 4 := by decide
    rw [hR1]
    refine ⟨⟨?_, ?_⟩, ?_⟩
    · rw [D_low x 7 4 (0 + 1) (by decide)]; decide
    · intro n hn
      by_cases hn11 : 11 ≤ n
      · exact qn n hn11
      · rcases (by omega : n = 5 ∨ n = 6 ∨ n = 7 ∨ n = 8 ∨ n = 9 ∨ n = 10) with
          rfl | rfl | rfl | rfl | rfl | rfl
        · rw [D_low x 7 5 (0 + 1) (by decide)]; decide
        · rw [D_low x 7 6 (0 + 1) (by decide)]; decide
        · rw [D_low x 7 7 (0 + 1) (by decide)]; decide
        · rw [D_eight x hx]; decide
        · exact q9
        · exact q10
    · intro h; exact absurd h (by decide)
  | succ u ih =>
    obtain ⟨hF, hg⟩ := ih
    have hR4 : 4 ≤ Rw (u + 1) := by unfold Rw; omega
    obtain ⟨Sm, _⟩ := step x 7 (u + 1) (Rw (u + 1)) ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8)
      (D x 7 (Rw (u + 1) - 1) (u + 1)) (D x 7 (Rw (u + 1) - 2) (u + 1)) hR4 hF rfl rfl rfl
    have hnr : ¬ ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8 = 1 ∧
        D x 7 (Rw (u + 1) - 1) (u + 1) = true ∧ D x 7 (Rw (u + 1) - 2) (u + 1) = true) := by
      rintro ⟨h1, h2, _⟩
      rw [hg h1] at h2
      exact absurd h2 (by decide)
    obtain ⟨hF', _, hph'⟩ := Sm hnr
    have hmv := wit_move (u + 1) (D x 7 (Rw (u + 1) - 1) (u + 1)) hg
    rw [hmv] at hF' hph'
    exact ⟨hF', hph'⟩

theorem wit_arith1 (k t : Nat) (ht : t < Lw k) : Rw t < k + 8 := by
  have hL := Lw_cases k
  have hk6 : k % 6 = 0 ∨ k % 6 = 1 ∨ k % 6 = 2 ∨ k % 6 = 3 ∨ k % 6 = 4 ∨ k % 6 = 5 := by omega
  have ht4 : t % 4 = 0 ∨ t % 4 = 1 ∨ t % 4 = 2 ∨ t % 4 = 3 := by omega
  unfold Rw
  rcases hk6 with h6 | h6 | h6 | h6 | h6 | h6 <;> rcases ht4 with h4 | h4 | h4 | h4 <;> omega

theorem wit_arith2 (k : Nat) : k + 8 ≤ Rw (Lw k) := by
  have hL := Lw_cases k
  unfold Rw; omega

/-! ### Healing at time 1 (the exclusions at phase classes 2, 4 and the witness at 7) -/

theorem heal_rec (x : Nat → Bool) (c : Nat) (h1 : ∀ n, 9 ≤ n → D x c n 1 = false) :
    ∀ n n1 n2, 9 ≤ n → n1 = n - 1 → n2 = n - 2 →
      D x c n 0 = F ((2 * n + c) % 8) (D x c n1 0) (D x c n2 0) := by
  intro n n1 n2 hn hn1 hn2
  have h := D_step' x c n 0 n1 n2 ((2 * n + c) % 8) (by omega) hn1 hn2 (by omega)
  rw [h1 n hn] at h
  exact xor_false_eq h.symm

theorem pat2_step : ∀ n n1 n2, n1 = n + 1 → n2 = n + 2 →
    F ((2 * n2 + 2) % 8) (n1 % 4 != 0) (n % 4 != 0) = (n2 % 4 != 0) := by
  intro n n1 n2 h1 h2
  subst h1 h2
  rw [show (2 * (n + 2) + 2) % 8 = (2 * (n % 4) + 6) % 8 by omega,
    show (n + 1) % 4 = (n % 4 + 1) % 4 by omega, show (n + 2) % 4 = (n % 4 + 2) % 4 by omega]
  have h : n % 4 < 4 := Nat.mod_lt _ (by decide)
  generalize n % 4 = r at h ⊢
  revert r; decide

theorem pat4_step : ∀ n n1 n2, n1 = n + 1 → n2 = n + 2 →
    F ((2 * n2 + 4) % 8) (n1 % 4 != 3) (n % 4 != 3) = (n2 % 4 != 3) := by
  intro n n1 n2 h1 h2
  subst h1 h2
  rw [show (2 * (n + 2) + 4) % 8 = (2 * (n % 4)) % 8 by omega,
    show (n + 1) % 4 = (n % 4 + 1) % 4 by omega, show (n + 2) % 4 = (n % 4 + 2) % 4 by omega]
  have h : n % 4 < 4 := Nat.mod_lt _ (by decide)
  generalize n % 4 = r at h ⊢
  revert r; decide

/-- At phase class `2`, healing every depth `≥ 1` at time `1` forces the mismatch row
`0, 1, 1, (0, 1, 1, 1)*` at depths `1, 2, ...`. -/
theorem heal2 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 2 n 1 = false) :
    ∀ m, D x 2 (m + 10) 0 = ((m + 10) % 4 != 0) ∧ D x 2 (m + 11) 0 = ((m + 11) % 4 != 0) := by
  have hr := heal_rec x 2 h1
  have d8 : D x 2 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 2 7 0 = true := by rw [D_low x 2 7 0 (by decide)]; decide
  have d9 : D x 2 9 0 = false := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 2 10 0 = true := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have d11 : D x 2 11 0 = true := by rw [hr 11 10 9 (by decide) rfl rfl, d10, d9]; decide
  intro m
  induction m with
  | zero => exact ⟨d10, d11⟩
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    rw [hr (m + 1 + 11) (m + 11) (m + 10) (by omega) (by omega) (by omega), ih.1, ih.2]
    exact pat2_step (m + 10) (m + 11) (m + 1 + 11) (by omega) (by omega)

/-- At phase class `4` the forced row is `(1, 1, 0, 1)*`. -/
theorem heal4 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 4 n 1 = false) :
    ∀ m, D x 4 (m + 10) 0 = ((m + 10) % 4 != 3) ∧ D x 4 (m + 11) 0 = ((m + 11) % 4 != 3) := by
  have hr := heal_rec x 4 h1
  have d8 : D x 4 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 4 7 0 = false := by rw [D_low x 4 7 0 (by decide)]; decide
  have d9 : D x 4 9 0 = true := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 4 10 0 = true := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have d11 : D x 4 11 0 = false := by rw [hr 11 10 9 (by decide) rfl rfl, d10, d9]; decide
  intro m
  induction m with
  | zero => exact ⟨d10, d11⟩
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    rw [hr (m + 1 + 11) (m + 11) (m + 10) (by omega) (by omega) (by omega), ih.1, ih.2]
    exact pat4_step (m + 10) (m + 11) (m + 1 + 11) (by omega) (by omega)

/-- At phase class `7` the forced row is clean: it is the witness's. -/
theorem heal7 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 7 n 1 = false) :
    ∀ n, 9 ≤ n → D x 7 n 0 = false := by
  have hr := heal_rec x 7 h1
  have d8 : D x 7 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 7 7 0 = true := by rw [D_low x 7 7 0 (by decide)]; decide
  have d9 : D x 7 9 0 = false := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 7 10 0 = false := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have hm : ∀ m, D x 7 (m + 9) 0 = false ∧ D x 7 (m + 10) 0 = false := by
    intro m
    induction m with
    | zero => exact ⟨d9, d10⟩
    | succ m ih =>
      refine ⟨ih.2, ?_⟩
      rw [hr (m + 1 + 10) (m + 10) (m + 9) (by omega) (by omega) (by omega), ih.1, ih.2, F_zero]
  intro n hn
  have h := (hm (n - 9)).1
  rwa [show n - 9 + 9 = n by omega] at h

/-- **The floor at time 1.** Either the front at time `1` is at least `lb c`, or the phase class
is `7` and the row is the witness's (clean at every edge depth `≥ 1`). The exclusions at `c = 2, 4`
use that the healing rows there never become clean, while the clean tail does. -/
theorem floor_case (x : Nat → Bool) (hx : x 0 = true) (c k : Nat) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false) (R : Nat) (hF : FrontAt x c 1 R) :
    lb c ≤ R ∨ (c = 7 ∧ ∀ n, 9 ≤ n → D x c n 0 = false) := by
  by_cases h9 : 9 ≤ R
  · left
    have hl : lb c ≤ 9 := by
      rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide
    omega
  · have h1 : ∀ n, 9 ≤ n → D x c n 1 = false := fun n hn => hF.2 n (by omega)
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · left
      have hm : D x 0 6 1 = true := by rw [D_low x 0 6 1 (by decide)]; decide
      exact front_ge hF hm
    · left
      have hm : D x 1 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · exfalso
      have hp := (heal2 x hx h1 (4 * k + 31)).1
      rw [h0 _ (by omega), show (4 * k + 31 + 10) % 4 = 1 by omega] at hp
      exact absurd hp (by decide)
    · left
      have hm : D x 3 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · exfalso
      have hp := (heal4 x hx h1 (4 * k + 31)).1
      rw [h0 _ (by omega), show (4 * k + 31 + 10) % 4 = 1 by omega] at hp
      exact absurd hp (by decide)
    · left
      have hm : D x 5 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · left
      have hm : D x 6 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · right; exact ⟨rfl, heal7 x hx h1⟩

/-! ### The episode bound -/

/-- Steps 2-5 for a clean-tail row: from time `1` on, either the potential keeps the floor
`K c`, or the phase class is `7` and the row is the witness's. -/
theorem dichotomy (z : Nat → Bool) (c k : Nat) (hz : z 0 = true) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D z c n 0 = false) :
    (∀ u, ∃ R, Good z c (K c) (u + 1) R) ∨ (c = 7 ∧ ∀ n, 9 ≤ n → D z c n 0 = false) := by
  obtain ⟨R0, hR0, hF0⟩ := front_zero z c k h0
  obtain ⟨R1, hR1, hF1, hph1⟩ := front_succ z c 0 R0 hR0 hF0
  rcases floor_case z hz c k hc h0 R1 hF1 with hlb | hw
  · exact Or.inl (pot_inv z c (K c) ⟨R1, hR1, hF1, hph1, floor_arith c hc R1 hlb⟩)
  · exact Or.inr hw

/-- The core: no clean-tail row has its pair (offset depths `k + 8, k + 9`, edge depths `k, k + 1`)
free of mismatch on all the ticks `0 .. Lw k`. -/
theorem core (z : Nat → Bool) (c k : Nat) (hz : z 0 = true) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D z c n 0 = false)
    (hp : ∀ u, u ≤ Lw k → D z c (k + 8) u = false ∧ D z c (k + 9) u = false) : False := by
  have hcl := tail_inv z c k (Lw k) h0 hp
  have hL1 : 1 ≤ Lw k := by have := Lw_cases k; omega
  suffices hs : ∃ R, k + 8 ≤ R ∧ D z c R (Lw k) = true by
    obtain ⟨R, hR, hD⟩ := hs
    rw [hcl (Lw k) (Nat.le_refl _) R hR] at hD
    exact absurd hD (by decide)
  rcases dichotomy z c k hz hc h0 with hg | ⟨rfl, hw⟩
  · obtain ⟨R, hgR⟩ := hg (Lw k - 1)
    rw [Nat.sub_add_cancel hL1] at hgR
    exact ⟨R, final_arith c hc k R hgR.2.2.2, hgR.2.1.1⟩
  · obtain ⟨hwf, _⟩ := wit_front z hz hw (Lw k - 1)
    rw [Nat.sub_add_cancel hL1] at hwf
    exact ⟨Rw (Lw k), wit_arith2 k, hwf.1⟩

/-- Onset and phase: an episode tick `s + u` of `x` at phase `(i, q)` is a tick `u` at which the
clean-tail row of `iter s x` has no mismatch at the pair, in phase class
`c = (s + q + 2i + 6k) mod 8` (that is, `q + s + 2i - 2k`). -/
theorem pair_clean (x : Nat → Bool) (k i q s c u : Nat) (hcdef : (s + q + 2 * i + 6 * k) % 8 = c)
    (h1 : iter (s + u) x k = ether i (s + u + q))
    (h2 : iter (s + u) x (k + 1) = ether (i + 1) (s + u + q)) :
    D (tail (iter s x) k c) c (k + 8) u = false ∧ D (tail (iter s x) k c) c (k + 9) u = false := by
  rw [iter_add] at h1 h2
  have ag := iter_agree (tail_agree (iter s x) k c) u
  constructor
  · unfold D
    rw [X_ge _ (k + 8) u (by omega), Nat.add_sub_cancel, ← ag k (by omega), h1, ether_eq]
    unfold E
    rw [e_congr (show (s + u + q + 2 * i) % 8 = (u + 2 * (k + 8) + c) % 8 by omega)]
    exact Bool.xor_self _
  · unfold D
    rw [X_ge _ (k + 9) u (by omega), show k + 9 - 8 = k + 1 by omega, ← ag (k + 1) (by omega), h2,
      ether_eq]
    unfold E
    rw [e_congr (show (s + u + q + 2 * (i + 1)) % 8 = (u + 2 * (k + 9) + c) % 8 by omega)]
    exact Bool.xor_self _

/-- The episode bound at every depth (at `k = 0` it is weaker than the truth, `M(0) = 2`). -/
theorem episode_bound_all (x : Nat → Bool) (hx : x 0 = true) (k i q s : Nat) :
    ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) := by
  intro hep
  have hy0 : iter s x 0 = true := by rw [iter_zero]; exact hx
  obtain ⟨c, hcdef⟩ : ∃ c, (s + q + 2 * i + 6 * k) % 8 = c := ⟨_, rfl⟩
  have hz : tail (iter s x) k c 0 = true := by simp [tail, hy0]
  apply core (tail (iter s x) k c) c k hz (by omega) (tail_clean (iter s x) k c)
  intro u hu
  obtain ⟨h1, h2⟩ := hep (s + u) (by omega) (by omega)
  exact pair_clean x k i q s c u hcdef h1 h2

/-- **The episode bound.** For every black-edge code `x` (finite or not), every depth `k ≥ 1`,
every phase `(i, q)` and every onset `s`, the pair at depths `k, k + 1` is not PR69's ether pair
on the `Lw k + 1` consecutive ticks `s .. s + Lw k`. -/
theorem episode_bound : ∀ (x : Nat → Bool), x 0 = true → ∀ k, 1 ≤ k → ∀ i q s : Nat,
    ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) :=
  fun x hx k _ i q s => episode_bound_all x hx k i q s

/-! ### The witness -/

/-- GC2328's witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/
def wit (j : Nat) : Bool := if j = 0 then true else ether (j + 3) 1

theorem wit_zero : wit 0 = true := rfl

/-- The witness's phase `(i, q, s) = (k + 3, 1, 0)` is in class `7`. -/
theorem wit_class (k : Nat) : (0 + 1 + 2 * (k + 3) + 6 * k) % 8 = 7 := by omega

theorem wit_clean : ∀ n, 9 ≤ n → D wit 7 n 0 = false := by
  intro n hn
  rw [D, X_ge wit n 0 (by omega)]
  simp only [iter, wit, E]
  rw [ite_eq_right (by omega), ether_eq,
    e_congr (show (1 + 2 * (n - 8 + 3)) % 8 = (0 + 2 * n + 7) % 8 by omega)]
  exact Bool.xor_self _

/-- **The witness.** For every `k ≥ 1` the GC2328 witness carries PR69's ether pair at depths
`k, k + 1` (phase `i = k + 3`, `q = 1`) on the ticks `0 .. Lw k - 1`. -/
theorem episode_witness : ∀ k, 1 ≤ k → ∃ x : Nat → Bool, x 0 = true ∧
    ∀ t, t < Lw k →
      iter t x k = ether (k + 3) (t + 1) ∧ iter t x (k + 1) = ether (k + 4) (t + 1) := by
  intro k hk
  refine ⟨wit, wit_zero, ?_⟩
  intro t ht
  have hD : D wit 7 (k + 8) t = false ∧ D wit 7 (k + 9) t = false := by
    cases t with
    | zero => exact ⟨wit_clean _ (by omega), wit_clean _ (by omega)⟩
    | succ u =>
      have hw := (wit_front wit wit_zero wit_clean u).1
      have hlt := wit_arith1 k (u + 1) ht
      exact ⟨hw.2 _ (by omega), hw.2 _ (by omega)⟩
  obtain ⟨h1, h2⟩ := hD
  have e1 := xor_false_eq h1
  have e2 := xor_false_eq h2
  rw [X_ge wit (k + 8) t (by omega), Nat.add_sub_cancel] at e1
  rw [X_ge wit (k + 9) t (by omega), show k + 9 - 8 = k + 1 by omega] at e2
  rw [e1, e2, ether_eq, ether_eq]
  unfold E
  exact ⟨e_congr (by omega), e_congr (by omega)⟩

/-- **The maximum.** For every `k ≥ 1`, `M(k) = Lw k = floor(2k/3) + 4 - [k ≡ 0, 2 (mod 6)]` is
the longest ether-pair episode at depths `k, k + 1` behind a black right edge: an episode of
`Lw k` ticks exists, and none has `Lw k + 1` ticks, over every code, phase and onset. -/
theorem episode_max (k : Nat) (hk : 1 ≤ k) :
    (∃ x : Nat → Bool, x 0 = true ∧ ∃ i q s : Nat, ∀ t, s ≤ t → t < s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) ∧
    (∀ x : Nat → Bool, x 0 = true → ∀ i q s : Nat, ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q))) := by
  refine ⟨?_, fun x hx i q s => episode_bound x hx k hk i q s⟩
  obtain ⟨x, hx, hw⟩ := episode_witness k hk
  exact ⟨x, hx, k + 3, 1, 0, fun t _ ht => hw t (by omega)⟩

/-! ### Uniqueness of the optimal prefix at phase class 7 -/

/-- At time `Lw k - 1` a front carrying the non-witness floor of class `7` is at depth `≥ k`. -/
theorem uniq_arith (k R : Nat)
    (h : 3 * (Lw k - 1) + K 7 ≤ 2 * R + G ((Lw k - 1 + 2 * R + 2 + 7) % 8)) : k + 8 ≤ R := by
  have hL := Lw_cases k
  have hk6 : k % 6 = 0 ∨ k % 6 = 1 ∨ k % 6 = 2 ∨ k % 6 = 3 ∨ k % 6 = 4 ∨ k % 6 = 5 := by omega
  simp only [K] at h
  rcases G_cases (Lw k - 1 + 2 * R + 2 + 7) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] at h <;>
    rcases hk6 with h6 | h6 | h6 | h6 | h6 | h6 <;> omega

/-- At phase class `7`, a clean-tail row whose pair is clean on the ticks `0 .. Lw k - 1` is the
witness's row. -/
theorem core7 (z : Nat → Bool) (k : Nat) (hz : z 0 = true)
    (h0 : ∀ n, k + 10 ≤ n → D z 7 n 0 = false)
    (hp : ∀ u, u ≤ Lw k - 1 → D z 7 (k + 8) u = false ∧ D z 7 (k + 9) u = false) :
    ∀ n, 9 ≤ n → D z 7 n 0 = false := by
  have hcl := tail_inv z 7 k (Lw k - 1) h0 hp
  have hL2 : 2 ≤ Lw k := by have := Lw_cases k; omega
  rcases dichotomy z 7 k hz (by decide) h0 with hg | ⟨_, hw⟩
  · exfalso
    obtain ⟨R, hgR⟩ := hg (Lw k - 2)
    rw [show Lw k - 2 + 1 = Lw k - 1 by omega] at hgR
    have hR := uniq_arith k R hgR.2.2.2
    have hD := hgR.2.1.1
    rw [hcl (Lw k - 1) (Nat.le_refl _) R hR] at hD
    exact absurd hD (by decide)
  · exact hw

/-- **Uniqueness at phase class 7.** If a black-edge code has an episode of `Lw k` ticks at depths
`k, k + 1` with onset `s` and a phase `(i, q)` of the witness's class
(`s + q + 2i + 6k ≡ 7 (mod 8)`), then at time `s` its bits `0 .. k + 1` are the witness's.
(Bits beyond `k + 1` are unconstrained; the statement says nothing about other classes.) -/
theorem witness_unique (x : Nat → Bool) (hx : x 0 = true) (k i q s : Nat)
    (hc : (s + q + 2 * i + 6 * k) % 8 = 7)
    (hep : ∀ t, s ≤ t → t < s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) :
    ∀ j, j ≤ k + 1 → iter s x j = wit j := by
  have hy0 : iter s x 0 = true := by rw [iter_zero]; exact hx
  have hz : tail (iter s x) k 7 0 = true := by simp [tail, hy0]
  have hL2 : 2 ≤ Lw k := by have := Lw_cases k; omega
  have hw := core7 (tail (iter s x) k 7) k hz (tail_clean (iter s x) k 7) (fun u hu => by
    obtain ⟨h1, h2⟩ := hep (s + u) (by omega) (by omega)
    exact pair_clean x k i q s 7 u hc h1 h2)
  intro j hj
  by_cases hj0 : j = 0
  · subst hj0; rw [hy0]; rfl
  · have e1 := xor_false_eq (hw (j + 8) (by omega))
    rw [X_ge _ (j + 8) 0 (by omega), Nat.add_sub_cancel] at e1
    simp only [iter] at e1
    rw [tail_agree (iter s x) k 7 j (by omega), e1]
    unfold wit E
    rw [ite_eq_right hj0, ether_eq]
    exact e_congr (by omega)

/-! ### Controls (kernel evaluation) -/

/-- The bases `M(1..8) = 4, 4, 6, 6, 7, 7, 8, 8` of the round's exhaustive computation. -/
example : Lw 1 = 4 ∧ Lw 2 = 4 ∧ Lw 3 = 6 ∧ Lw 4 = 6 ∧ Lw 5 = 7 ∧ Lw 6 = 7 ∧ Lw 7 = 8 ∧
    Lw 8 = 8 := by decide

/-- The witness front at times `1 .. 4` is at edge depths `-4, -2, 0, 2` (offset `4, 6, 8, 10`). -/
example : Rw 1 = 4 ∧ Rw 2 = 6 ∧ Rw 3 = 8 ∧ Rw 4 = 10 := by decide

/-- The witness carries the pair at depth `6` on the ticks `0 .. 6` ... -/
example : ∀ t, t < 7 → iter t wit 6 = ether 9 (t + 1) ∧ iter t wit 7 = ether 10 (t + 1) := by
  decide

/-- ... and loses it at tick `Lw 6 = 7`; likewise at depth `5`. -/
example : ¬ (iter (Lw 6) wit 6 = ether 9 (Lw 6 + 1) ∧ iter (Lw 6) wit 7 = ether 10 (Lw 6 + 1)) ∧
    ¬ (iter (Lw 5) wit 5 = ether 8 (Lw 5 + 1) ∧ iter (Lw 5) wit 6 = ether 9 (Lw 5 + 1)) := by
  decide

end Ruliology.CellularAutomata.Rule30EtherEpisode

open Ruliology.CellularAutomata.Rule30EtherEpisode in
#print axioms episode_bound
open Ruliology.CellularAutomata.Rule30EtherEpisode in
#print axioms episode_bound_all
open Ruliology.CellularAutomata.Rule30EtherEpisode in
#print axioms episode_witness
open Ruliology.CellularAutomata.Rule30EtherEpisode in
#print axioms episode_max
open Ruliology.CellularAutomata.Rule30EtherEpisode in
#print axioms witness_unique
