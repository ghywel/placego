import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# G16 episodes at depth 14 last at most 22 ticks (Local, L1482–L1484; Cloud's CL706 tree, GPT's GC2596 contract)

The phase `g16 i` is the 128-cell ring of `upward_rigid.py` (`RING16`) read in the light-speed frame: depth `j` at time
`t` is ring cell `j + i + 56 t` (mod 128), since the frame rule moves this ring by `72 ≡ -56` cells per tick
(`y_step`). `g16_phase`: it obeys the edge map at every depth `≥ 2`, with period 16 (A5's `IsPhase`).

* `cone`: bit `j` of the edge code at tick `t` depends only on bits `j - 2t … j` of the initial code.
* `layer i t`: Cloud's top-word tree. Layer `t + 1` extends each word of layer `t` downward by
  `wd (t + 1) - wd t` bits (`wd t = min (2t) 15`) and keeps the words whose canonical completion (bit 0 black, unread
  bits white) matches `g16 i` at depths 14 and 15 at tick `t`.
* `sound`: the top `wd t` bits of every black-edge code with a `t`-tick episode at alignment 0 form a word of
  `layer i t`. So `layer i 23 = []` excludes every 23-tick episode (`rep_bound`).
* `episode_shift`: an episode at alignment `a` for `g16 i` is one at alignment 0 for `g16 ((i + 56 a) % 128)`
  (GC2596's 16-fold identification), so the 128 representatives cover every alignment.
* `reps0` … `reps7` (eight kernel computations of 16 representatives each), `all_reps` and `g16_mfinite`:
  `MFinite (g16 i) 14` for every `i`, with `L = 22`.
* `g16_no_tail`: no black-edge code follows `g16 i` at every depth from some depth `d ≤ 14` on, at any alignment.

Scope: depth 14 only; nothing on other depths, on the uniform exclusion of G16, the centre column or the Prize problems.
-/

namespace Ruliology.CellularAutomata.Rule30G16Episode

set_option autoImplicit false

open Rule30FrozenRuler

/-! ### A5's definitions (`Rule30EpisodeBridge`, kit PR 116), restated verbatim -/

/-- A phase: columns obeying the edge map at every depth `≥ 2`, with period `p` in time. -/
structure IsPhase (E : Nat → Nat → Bool) (p : Nat) : Prop where
  pos : 0 < p
  step : ∀ j t, E (j + 2) (t + 1) = xor (E (j + 2) t) (E (j + 1) t || E j t)
  period : ∀ j t, E j (t + p) = E j t

/-- An episode of `T` ticks at depths `k, k + 1`, alignment `a`, onset `0`. -/
def Episode (E : Nat → Nat → Bool) (k : Nat) (x : Nat → Bool) (a T : Nat) : Prop :=
  ∀ t, t < T → iter t x k = E k (t + a) ∧ iter t x (k + 1) = E (k + 1) (t + a)

/-- The longest episode at depth `k` behind a black edge is finite: at most `L` ticks. -/
def MFinite (E : Nat → Nat → Bool) (k : Nat) : Prop :=
  ∃ L, ∀ (x : Nat → Bool) (a : Nat), x 0 = true → ¬ Episode E k x a (L + 1)

/-! ### The phase -/

/-- `RING16` of `upward_rigid.py`: bit `n` is ring cell `n`. -/
def ringNat : Nat := 0x468b2e4a3c095cc178d9b5d3f6c43ea7

def y (n : Nat) : Bool := ringNat.testBit (n % 128)

/-- The phase at spatial representative `i`. -/
def g16 (i : Nat) : Nat → Nat → Bool := fun j t => y (j + i + 56 * t)

theorem y_step_lt : ∀ n, n < 128 → y (n + 58) = xor (y (n + 2)) (y (n + 1) || y n) := by decide

theorem y_step (n : Nat) : y (n + 58) = xor (y (n + 2)) (y (n + 1) || y n) := by
  have h := y_step_lt (n % 128) (Nat.mod_lt _ (by decide))
  have e : ∀ c, (n % 128 + c) % 128 = (n + c) % 128 := fun c => by omega
  simp only [y] at h ⊢
  rw [e 58, e 2, e 1, Nat.mod_mod] at h
  exact h

theorem y_congr {m n : Nat} (h : m % 128 = n % 128) : y m = y n := by
  simp only [y]; rw [h]

theorem g16_phase (i : Nat) : IsPhase (g16 i) 16 where
  pos := by decide
  step j t := by
    show y (j + 2 + i + 56 * (t + 1)) = xor (y (j + 2 + i + 56 * t)) (y (j + 1 + i + 56 * t) || y (j + i + 56 * t))
    have h := y_step (j + i + 56 * t)
    have e1 : j + 2 + i + 56 * (t + 1) = j + i + 56 * t + 58 := by omega
    have e2 : j + 2 + i + 56 * t = j + i + 56 * t + 2 := by omega
    have e3 : j + 1 + i + 56 * t = j + i + 56 * t + 1 := by omega
    rw [e1, e2, e3]; exact h
  period j t := y_congr (by omega)

/-! ### The edge map on bit words -/

def wstep (n : Nat) : Nat := n ^^^ ((n <<< 1) ||| (n <<< 2))

def iterW : Nat → Nat → Nat
  | 0, n => n
  | t + 1, n => wstep (iterW t n)

theorem T_decode (n : Nat) : T (fun j => n.testBit j) = fun j => (wstep n).testBit j := by
  funext j
  match j with
  | 0 => simp [T, wstep]
  | 1 => simp [T, wstep, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]
  | j + 2 => simp [T, wstep, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]

theorem iter_decode (n : Nat) : ∀ t, iter t (fun j => n.testBit j) = fun j => (iterW t n).testBit j
  | 0 => rfl
  | t + 1 => by
    show T (iter t (fun j => n.testBit j)) = fun j => (wstep (iterW t n)).testBit j
    rw [iter_decode n t, T_decode]

/-! ### Locality: the backward cone -/

theorem cone (x x' : Nat → Bool) (t : Nat) :
    ∀ j, (∀ m, j - 2 * t ≤ m → m ≤ j → x m = x' m) → iter t x j = iter t x' j := by
  induction t with
  | zero => intro j h; exact h j (by omega) (Nat.le_refl j)
  | succ t ih =>
    intro j h
    show T (iter t x) j = T (iter t x') j
    match j, h with
    | 0, h => exact ih 0 (fun m h1 h2 => h m (by omega) h2)
    | 1, h =>
      show xor (iter t x 1) (iter t x 0) = xor (iter t x' 1) (iter t x' 0)
      rw [ih 1 (fun m h1 h2 => h m (by omega) h2), ih 0 (fun m h1 h2 => h m (by omega) (by omega))]
    | j + 2, h =>
      show xor (iter t x (j + 2)) (iter t x (j + 1) || iter t x j) =
        xor (iter t x' (j + 2)) (iter t x' (j + 1) || iter t x' j)
      rw [ih (j + 2) (fun m h1 h2 => h m (by omega) h2), ih (j + 1) (fun m h1 h2 => h m (by omega) (by omega)),
        ih j (fun m h1 h2 => h m (by omega) (by omega))]

/-! ### Cloud's top-word tree -/

/-- Width of the top word after `t` ticks: initial bits `16 - wd t … 15` have been read. -/
def wd (t : Nat) : Nat := min (2 * t) 15

/-- The canonical completion of a top word of width `wd t`: bit 0 black, unread bits white. -/
def compl (w t : Nat) : Nat := (w <<< (16 - wd t)) ||| 1

/-- The pair test at tick `t` for a top word of width `wd (t + 1)`. -/
def test (i t w : Nat) : Bool :=
  (iterW t (compl w (t + 1))).testBit 14 == g16 i 14 t && (iterW t (compl w (t + 1))).testBit 15 == g16 i 15 t

def layer (i : Nat) : Nat → List Nat
  | 0 => [0]
  | t + 1 => (layer i t).flatMap fun w =>
      ((List.range (2 ^ (wd (t + 1) - wd t))).map fun e => (w <<< (wd (t + 1) - wd t)) ||| e).filter (test i t)

/-- Bits `lo … lo + d - 1` of a code, as a number. -/
def bitsOf (x : Nat → Bool) (lo : Nat) : Nat → Nat
  | 0 => 0
  | d + 1 => bitsOf x lo d ||| (if x (lo + d) then 2 ^ d else 0)

theorem testBit_bitsOf (x : Nat → Bool) (lo : Nat) :
    ∀ d m, (bitsOf x lo d).testBit m = (decide (m < d) && x (lo + m))
  | 0, m => by simp [bitsOf]
  | d + 1, m => by
    simp only [bitsOf, Nat.testBit_or, testBit_bitsOf x lo d m]
    rcases Nat.lt_trichotomy m d with h | rfl | h
    · cases hx : x (lo + d) <;> simp [h, Nat.lt_succ_of_lt h, show d ≠ m by omega]
    · cases hx : x (lo + m) <;> simp
    · cases hx : x (lo + d) <;>
        simp [show ¬ m < d by omega, show ¬ m < d + 1 by omega, show d ≠ m by omega]

theorem bitsOf_lt (x : Nat → Bool) (lo : Nat) : ∀ d, bitsOf x lo d < 2 ^ d
  | 0 => by simp [bitsOf]
  | d + 1 => by
    simp only [bitsOf]
    apply Nat.or_lt_two_pow
    · exact Nat.lt_of_lt_of_le (bitsOf_lt x lo d) (Nat.pow_le_pow_right (by decide) (by omega))
    · split
      · exact Nat.pow_lt_pow_right (by decide) (by omega)
      · exact Nat.two_pow_pos _

theorem bitsOf_split (x : Nat → Bool) (lo d W : Nat) :
    bitsOf x lo (W + d) = (bitsOf x (lo + d) W <<< d) ||| bitsOf x lo d := by
  apply Nat.eq_of_testBit_eq
  intro m
  simp only [Nat.testBit_or, Nat.testBit_shiftLeft, testBit_bitsOf]
  by_cases h : d ≤ m
  · have e : lo + d + (m - d) = lo + m := by omega
    simp [h, e, show ¬ m < d by omega]
    rw [decide_eq_decide.mpr (show m < W + d ↔ m - d < W by omega)]
  · simp [show m < d by omega, show m < W + d by omega, show ¬ d ≤ m by omega]

theorem wd_le (t : Nat) : wd t ≤ wd (t + 1) := by simp only [wd]; omega

/-- **Soundness of the tree**: the top `wd t` bits of a code with a `t`-tick episode are a word of `layer i t`. -/
theorem sound (i : Nat) (x : Nat → Bool) (hx : x 0 = true) :
    ∀ t, Episode (g16 i) 14 x 0 t → bitsOf x (16 - wd t) (wd t) ∈ layer i t
  | 0, _ => by simp [layer, bitsOf, wd]
  | t + 1, h => by
    have ih := sound i x hx t (fun s hs => h s (by omega))
    have hd := wd_le t
    have hW : wd (t + 1) = wd t + (wd (t + 1) - wd t) := by omega
    have hlo : 16 - wd (t + 1) + (wd (t + 1) - wd t) = 16 - wd t := by simp only [wd]; omega
    have hsplit := bitsOf_split x (16 - wd (t + 1)) (wd (t + 1) - wd t) (wd t)
    rw [hlo, show wd t + (wd (t + 1) - wd t) = wd (t + 1) by omega] at hsplit
    -- the completion agrees with `x` on the cone of depths 14 and 15 at tick `t`
    have hagree : ∀ m, 14 - 2 * t ≤ m → m ≤ 15 →
        x m = (compl (bitsOf x (16 - wd (t + 1)) (wd (t + 1))) (t + 1)).testBit m := by
      intro m h1 h2
      simp only [compl, Nat.testBit_or, Nat.testBit_shiftLeft, testBit_bitsOf]
      by_cases hm : m = 0
      · subst hm; simp [hx, wd]
      · have hs : 16 - wd (t + 1) ≤ m := by simp only [wd]; omega
        have e : 16 - wd (t + 1) + (m - (16 - wd (t + 1))) = m := by omega
        have hl : m - (16 - wd (t + 1)) < wd (t + 1) := by simp only [wd]; omega
        have h1m : Nat.testBit 1 m = false := by
          rw [show (1 : Nat) = 2 ^ 0 from rfl, Nat.testBit_two_pow]; simp; omega
        simp [hs, e, hl, h1m]
    have htest : test i t (bitsOf x (16 - wd (t + 1)) (wd (t + 1))) = true := by
      have h14 := (h t (by omega)).1
      have h15 := (h t (by omega)).2
      simp only [test, Nat.add_zero] at h14 h15 ⊢
      have c14 := congrFun (iter_decode (compl (bitsOf x (16 - wd (t + 1)) (wd (t + 1))) (t + 1)) t) 14
      have c15 := congrFun (iter_decode (compl (bitsOf x (16 - wd (t + 1)) (wd (t + 1))) (t + 1)) t) 15
      rw [← c14, ← c15, ← cone x _ t 14 (fun m h1 h2 => hagree m h1 (by omega)),
        ← cone x _ t 15 (fun m h1 h2 => hagree m (by omega) h2), h14, h15]
      simp
    simp only [layer, List.mem_flatMap, List.mem_filter, List.mem_map, List.mem_range]
    exact ⟨_, ih, ⟨_, bitsOf_lt x _ _, hsplit.symm⟩, htest⟩

theorem rep_bound (i : Nat) (h : layer i 23 = []) (x : Nat → Bool) (hx : x 0 = true) :
    ¬ Episode (g16 i) 14 x 0 23 := fun hep => by
  have := sound i x hx 23 hep
  rw [h] at this
  exact List.not_mem_nil this

/-- GC2596's identification: alignment `a` at representative `i` is alignment 0 at `(i + 56 a) % 128`. -/
theorem episode_shift (i a : Nat) (x : Nat → Bool) (T : Nat) :
    Episode (g16 i) 14 x a T ↔ Episode (g16 ((i + 56 * a) % 128)) 14 x 0 T := by
  have e : ∀ j t, g16 i j (t + a) = g16 ((i + 56 * a) % 128) j (t + 0) := fun j t => y_congr (by omega)
  simp only [Episode, e]

/-! ### The kernel computations -/

set_option profiler true in
/-- Pilot: representative 0. -/
theorem pilot0 : layer 0 23 = [] := by decide +kernel

set_option profiler true in
/-- Pilot: representative 41, the one class with a 22-tick survivor. -/
theorem pilot41 : layer 41 23 = [] := by decide +kernel

/-- Control: representative 41 keeps a word through tick 22, so the bound below is not slack there. -/
theorem control41 : layer 41 22 ≠ [] := by decide +kernel

set_option profiler true in
theorem reps0 : ∀ r, r < 16 → layer (16 * 0 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps1 : ∀ r, r < 16 → layer (16 * 1 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps2 : ∀ r, r < 16 → layer (16 * 2 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps3 : ∀ r, r < 16 → layer (16 * 3 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps4 : ∀ r, r < 16 → layer (16 * 4 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps5 : ∀ r, r < 16 → layer (16 * 5 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps6 : ∀ r, r < 16 → layer (16 * 6 + r) 23 = [] := by decide +kernel

set_option profiler true in
theorem reps7 : ∀ r, r < 16 → layer (16 * 7 + r) 23 = [] := by decide +kernel

/-- All 128 representatives, from the eight chunks. -/
theorem all_reps (i : Nat) (hi : i < 128) : layer i 23 = [] := by
  have h : i = 16 * (i / 16) + i % 16 := (Nat.div_add_mod i 16).symm
  have hr : i % 16 < 16 := Nat.mod_lt _ (by decide)
  generalize i / 16 = q at h
  generalize i % 16 = r at h hr
  subst h
  match q, hi with
  | 0, _ => exact reps0 r hr
  | 1, _ => exact reps1 r hr
  | 2, _ => exact reps2 r hr
  | 3, _ => exact reps3 r hr
  | 4, _ => exact reps4 r hr
  | 5, _ => exact reps5 r hr
  | 6, _ => exact reps6 r hr
  | 7, _ => exact reps7 r hr
  | q + 8, hi => omega

/-- **Every alignment of G16 has longest episode at most 22 ticks at depth 14.** -/
theorem g16_mfinite (i : Nat) : MFinite (g16 i) 14 :=
  ⟨22, fun x a hx hep =>
    rep_bound _ (all_reps _ (Nat.mod_lt _ (by decide))) x hx ((episode_shift i a x 23).mp hep)⟩

/-- **No tail from depth 14 or shallower**: no black-edge code follows `g16 i` at every depth `≥ d`, for any `d ≤ 14`,
at any alignment `a` (GC2596's bounded-depth consequence; no period is assumed). -/
theorem g16_no_tail (i : Nat) (x : Nat → Bool) (d a : Nat) (hx : x 0 = true) (hd : d ≤ 14)
    (h : ∀ j, d ≤ j → ∀ t, iter t x j = g16 i j (t + a)) : False := by
  obtain ⟨L, hL⟩ := g16_mfinite i
  exact hL x a hx (fun t _ => ⟨h 14 hd t, h 15 (by omega) t⟩)

end Ruliology.CellularAutomata.Rule30G16Episode

#print axioms Ruliology.CellularAutomata.Rule30G16Episode.g16_mfinite
#print axioms Ruliology.CellularAutomata.Rule30G16Episode.g16_phase
#print axioms Ruliology.CellularAutomata.Rule30G16Episode.g16_no_tail
