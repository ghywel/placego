import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Three phases at bounded depth: G16 to depth 14, P1024 to depth 8, the 480-phase to depth 10 (Local, L1488–L1489)

L1484's certificate made generic in the depth `k` and the phase `E` (Cloud's top-word tree, CL706; GC2596's soundness and
alignment contract), then applied to three phases of the record, each at every alignment:

* `g16_mfinite`: the 128-cell ring `RING16` (lag 72), depth 14, longest episode at most 22 ticks.
* `p1024_mfinite`: the 1024-cell ring of `phase1024_ring.txt` (lag 21, frame period 1024), depth 8, at most 24 ticks.
* `p480_mfinite`: the 480-phase of `phase480_p32.txt` (frame period 32, `c² = ρ^270`, two literals `z0`, `z1`), depth
  10, at most 24 ticks.
* `no_tail_of_mfinite`: so no black-edge code follows any of them at every depth from some depth `d ≤ k` on.

Generic part: `cone` (bit `j` at tick `t` reads initial bits `j - 2t … j`), `iter_decode` (the edge map on bit words),
`layer E k` and `sound` (the top `wd k t` bits of a code with a `t`-tick episode are a word of `layer E k t`), `rep_bound`
and `episode_congr`. Each phase has its literal(s), `IsPhase` by `decide` on the frame relation, an alignment shift
lemma, and kernel chunks (`decide +kernel`) combined by an index split. Scope: these depths only; nothing on other
depths, the uniform exclusion of these phases, the centre column or the Prize problems.
-/

namespace Ruliology.CellularAutomata.Rule30PhaseTrees

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

/-! ### The edge map on bit words, and the backward cone -/

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

/-! ### Cloud's top-word tree, generic in the depth and the phase -/

/-- Width of the top word after `t` ticks at depth `k`: initial bits `k + 2 - wd k t … k + 1` have been read. -/
def wd (k t : Nat) : Nat := min (2 * t) (k + 1)

/-- The canonical completion of a top word of width `wd k t`: bit 0 black, unread bits white. -/
def compl (k w t : Nat) : Nat := (w <<< (k + 2 - wd k t)) ||| 1

/-- The pair test at tick `t` for a top word of width `wd k (t + 1)`. -/
def test (E : Nat → Nat → Bool) (k t w : Nat) : Bool :=
  (iterW t (compl k w (t + 1))).testBit k == E k t && (iterW t (compl k w (t + 1))).testBit (k + 1) == E (k + 1) t

def layer (E : Nat → Nat → Bool) (k : Nat) : Nat → List Nat
  | 0 => [0]
  | t + 1 => (layer E k t).flatMap fun w =>
      ((List.range (2 ^ (wd k (t + 1) - wd k t))).map fun e => (w <<< (wd k (t + 1) - wd k t)) ||| e).filter
        (test E k t)

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

theorem wd_le (k t : Nat) : wd k t ≤ wd k (t + 1) := by simp only [wd]; omega

/-- **Soundness of the tree**: the top `wd k t` bits of a code with a `t`-tick episode are a word of `layer E k t`. -/
theorem sound (E : Nat → Nat → Bool) (k : Nat) (x : Nat → Bool) (hx : x 0 = true) :
    ∀ t, Episode E k x 0 t → bitsOf x (k + 2 - wd k t) (wd k t) ∈ layer E k t
  | 0, _ => by simp [layer, bitsOf, wd]
  | t + 1, h => by
    have ih := sound E k x hx t (fun s hs => h s (by omega))
    have hd := wd_le k t
    have hlo : k + 2 - wd k (t + 1) + (wd k (t + 1) - wd k t) = k + 2 - wd k t := by simp only [wd]; omega
    have hsplit := bitsOf_split x (k + 2 - wd k (t + 1)) (wd k (t + 1) - wd k t) (wd k t)
    rw [hlo, show wd k t + (wd k (t + 1) - wd k t) = wd k (t + 1) by omega] at hsplit
    have hagree : ∀ m, k - 2 * t ≤ m → m ≤ k + 1 →
        x m = (compl k (bitsOf x (k + 2 - wd k (t + 1)) (wd k (t + 1))) (t + 1)).testBit m := by
      intro m h1 h2
      simp only [compl, Nat.testBit_or, Nat.testBit_shiftLeft, testBit_bitsOf]
      by_cases hm : m = 0
      · subst hm; simp [hx]
      · have hs : k + 2 - wd k (t + 1) ≤ m := by simp only [wd]; omega
        have e : k + 2 - wd k (t + 1) + (m - (k + 2 - wd k (t + 1))) = m := by omega
        have hl : m - (k + 2 - wd k (t + 1)) < wd k (t + 1) := by simp only [wd]; omega
        have h1m : Nat.testBit 1 m = false := by
          rw [show (1 : Nat) = 2 ^ 0 from rfl, Nat.testBit_two_pow]; simp; omega
        simp [hs, e, hl, h1m]
    have htest : test E k t (bitsOf x (k + 2 - wd k (t + 1)) (wd k (t + 1))) = true := by
      have hk := (h t (by omega)).1
      have hk1 := (h t (by omega)).2
      simp only [test, Nat.add_zero] at hk hk1 ⊢
      have ck := congrFun (iter_decode (compl k (bitsOf x (k + 2 - wd k (t + 1)) (wd k (t + 1))) (t + 1)) t) k
      have ck1 :=
        congrFun (iter_decode (compl k (bitsOf x (k + 2 - wd k (t + 1)) (wd k (t + 1))) (t + 1)) t) (k + 1)
      rw [← ck, ← ck1, ← cone x _ t k (fun m h1 h2 => hagree m h1 (by omega)),
        ← cone x _ t (k + 1) (fun m h1 h2 => hagree m (by omega) h2), hk, hk1]
      simp
    simp only [layer, List.mem_flatMap, List.mem_filter, List.mem_map, List.mem_range]
    exact ⟨_, ih, ⟨_, bitsOf_lt x _ _, hsplit.symm⟩, htest⟩

theorem rep_bound (E : Nat → Nat → Bool) (k M : Nat) (h : layer E k (M + 1) = []) (x : Nat → Bool)
    (hx : x 0 = true) : ¬ Episode E k x 0 (M + 1) := fun hep => by
  have := sound E k x hx (M + 1) hep
  rw [h] at this
  exact List.not_mem_nil this

theorem episode_congr {E E' : Nat → Nat → Bool} {k a : Nat} (h : ∀ j t, E j (t + a) = E' j (t + 0))
    (x : Nat → Bool) (T : Nat) : Episode E k x a T ↔ Episode E' k x 0 T := by
  simp only [Episode, h]

/-- A bounded longest episode at depth `k` excludes every tail from a depth `d ≤ k`, at any alignment. -/
theorem no_tail_of_mfinite {E : Nat → Nat → Bool} {k : Nat} (hE : MFinite E k) (x : Nat → Bool) (d a : Nat)
    (hx : x 0 = true) (hd : d ≤ k) (h : ∀ j, d ≤ j → ∀ t, iter t x j = E j (t + a)) : False := by
  obtain ⟨L, hL⟩ := hE
  exact hL x a hx (fun t _ => ⟨h k hd t, h (k + 1) (by omega) t⟩)

/-! ### G16: the ring `RING16` of `upward_rigid.py` (lag 72 ≡ -56), depth 14 -/

def ring16 : Nat := 0x468b2e4a3c095cc178d9b5d3f6c43ea7

def y16 (n : Nat) : Bool := ring16.testBit (n % 128)

/-- G16 at spatial representative `i`. -/
def g16 (i : Nat) : Nat → Nat → Bool := fun j t => y16 (j + i + 56 * t)

theorem y16_congr {m n : Nat} (h : m % 128 = n % 128) : y16 m = y16 n := by simp only [y16]; rw [h]

theorem y16_step_lt : ∀ n, n < 128 → y16 (n + 58) = xor (y16 (n + 2)) (y16 (n + 1) || y16 n) := by decide

theorem y16_step (n : Nat) : y16 (n + 58) = xor (y16 (n + 2)) (y16 (n + 1) || y16 n) := by
  rw [y16_congr (show (n + 58) % 128 = (n % 128 + 58) % 128 by omega),
    y16_congr (show (n + 2) % 128 = (n % 128 + 2) % 128 by omega),
    y16_congr (show (n + 1) % 128 = (n % 128 + 1) % 128 by omega), y16_congr (show n % 128 = n % 128 % 128 by omega)]
  exact y16_step_lt _ (Nat.mod_lt _ (by decide))

theorem g16_phase (i : Nat) : IsPhase (g16 i) 16 where
  pos := by decide
  step j t := by
    show y16 (j + 2 + i + 56 * (t + 1)) = xor (y16 (j + 2 + i + 56 * t)) (y16 (j + 1 + i + 56 * t) || y16 (j + i + 56 * t))
    rw [show j + 2 + i + 56 * (t + 1) = j + i + 56 * t + 58 by omega, show j + 2 + i + 56 * t = j + i + 56 * t + 2 by omega,
      show j + 1 + i + 56 * t = j + i + 56 * t + 1 by omega]
    exact y16_step _
  period j t := y16_congr (by omega)

theorem g16_shift (i a : Nat) (j t : Nat) : g16 i j (t + a) = g16 ((i + 56 * a) % 128) j (t + 0) :=
  y16_congr (by omega)

theorem g16_c0 : ∀ r, r < 16 → layer (g16 (16 * 0 + r)) 14 23 = [] := by decide +kernel

theorem g16_c1 : ∀ r, r < 16 → layer (g16 (16 * 1 + r)) 14 23 = [] := by decide +kernel

theorem g16_c2 : ∀ r, r < 16 → layer (g16 (16 * 2 + r)) 14 23 = [] := by decide +kernel

theorem g16_c3 : ∀ r, r < 16 → layer (g16 (16 * 3 + r)) 14 23 = [] := by decide +kernel

theorem g16_c4 : ∀ r, r < 16 → layer (g16 (16 * 4 + r)) 14 23 = [] := by decide +kernel

theorem g16_c5 : ∀ r, r < 16 → layer (g16 (16 * 5 + r)) 14 23 = [] := by decide +kernel

theorem g16_c6 : ∀ r, r < 16 → layer (g16 (16 * 6 + r)) 14 23 = [] := by decide +kernel

theorem g16_c7 : ∀ r, r < 16 → layer (g16 (16 * 7 + r)) 14 23 = [] := by decide +kernel

theorem g16_all (i : Nat) (hi : i < 128) : layer (g16 i) 14 23 = [] := by
  have h : i = 16 * (i / 16) + i % 16 := (Nat.div_add_mod i 16).symm
  have hr : i % 16 < 16 := Nat.mod_lt _ (by decide)
  generalize i / 16 = c at h
  generalize i % 16 = r at h hr
  subst h
  match c, hi with
  | 0, _ => exact g16_c0 r hr
  | 1, _ => exact g16_c1 r hr
  | 2, _ => exact g16_c2 r hr
  | 3, _ => exact g16_c3 r hr
  | 4, _ => exact g16_c4 r hr
  | 5, _ => exact g16_c5 r hr
  | 6, _ => exact g16_c6 r hr
  | 7, _ => exact g16_c7 r hr
  | c + 8, hi => omega

/-- **G16: every alignment's longest episode at depth 14 is at most 22 ticks.** -/
theorem g16_mfinite (i : Nat) : MFinite (g16 i) 14 :=
  ⟨22, fun x a hx hep => rep_bound _ 14 22 (g16_all _ (Nat.mod_lt _ (by decide))) x hx
    ((episode_congr (g16_shift i a) x 23).mp hep)⟩

/-! ### P1024: the ring of `phase1024_ring.txt` (lag 21 ≡ -1003, frame period 1024), depth 8 -/

def ring1024 : Nat := 0xf93d987e174c1347a3e6c361ca6533bddee2110973b9f4e270797c8c743dac6612add3ea91e0afb11a82bb2c6a2eacb68aba4daa3f92b607ea50c0bd9a1a1733334eeee78889c5ddf2d110e9bb98f22758f7c55842d54e69579cf5473856ce4d4b9f97a70743c8c663dadd6129153efb5e082511c7dbb2c122ea3f68b604da5

def y1024 (n : Nat) : Bool := ring1024.testBit (n % 1024)

/-- P1024 at spatial representative `i`. -/
def p1024 (i : Nat) : Nat → Nat → Bool := fun j t => y1024 (j + i + 1003 * t)

theorem y1024_congr {m n : Nat} (h : m % 1024 = n % 1024) : y1024 m = y1024 n := by simp only [y1024]; rw [h]

theorem y1024_step_lt : ∀ n, n < 1024 → y1024 (n + 1005) = xor (y1024 (n + 2)) (y1024 (n + 1) || y1024 n) := by
  decide +kernel

theorem y1024_step (n : Nat) : y1024 (n + 1005) = xor (y1024 (n + 2)) (y1024 (n + 1) || y1024 n) := by
  rw [y1024_congr (show (n + 1005) % 1024 = (n % 1024 + 1005) % 1024 by omega),
    y1024_congr (show (n + 2) % 1024 = (n % 1024 + 2) % 1024 by omega),
    y1024_congr (show (n + 1) % 1024 = (n % 1024 + 1) % 1024 by omega),
    y1024_congr (show n % 1024 = n % 1024 % 1024 by omega)]
  exact y1024_step_lt _ (Nat.mod_lt _ (by decide))

theorem p1024_phase (i : Nat) : IsPhase (p1024 i) 1024 where
  pos := by decide
  step j t := by
    show y1024 (j + 2 + i + 1003 * (t + 1)) =
      xor (y1024 (j + 2 + i + 1003 * t)) (y1024 (j + 1 + i + 1003 * t) || y1024 (j + i + 1003 * t))
    rw [show j + 2 + i + 1003 * (t + 1) = j + i + 1003 * t + 1005 by omega,
      show j + 2 + i + 1003 * t = j + i + 1003 * t + 2 by omega, show j + 1 + i + 1003 * t = j + i + 1003 * t + 1 by omega]
    exact y1024_step _
  period j t := y1024_congr (by omega)

theorem p1024_shift (i a : Nat) (j t : Nat) : p1024 i j (t + a) = p1024 ((i + 1003 * a) % 1024) j (t + 0) :=
  y1024_congr (by omega)

theorem p1024_c0 : ∀ r, r < 64 → layer (p1024 (64 * 0 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c1 : ∀ r, r < 64 → layer (p1024 (64 * 1 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c2 : ∀ r, r < 64 → layer (p1024 (64 * 2 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c3 : ∀ r, r < 64 → layer (p1024 (64 * 3 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c4 : ∀ r, r < 64 → layer (p1024 (64 * 4 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c5 : ∀ r, r < 64 → layer (p1024 (64 * 5 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c6 : ∀ r, r < 64 → layer (p1024 (64 * 6 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c7 : ∀ r, r < 64 → layer (p1024 (64 * 7 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c8 : ∀ r, r < 64 → layer (p1024 (64 * 8 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c9 : ∀ r, r < 64 → layer (p1024 (64 * 9 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c10 : ∀ r, r < 64 → layer (p1024 (64 * 10 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c11 : ∀ r, r < 64 → layer (p1024 (64 * 11 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c12 : ∀ r, r < 64 → layer (p1024 (64 * 12 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c13 : ∀ r, r < 64 → layer (p1024 (64 * 13 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c14 : ∀ r, r < 64 → layer (p1024 (64 * 14 + r)) 8 25 = [] := by decide +kernel

theorem p1024_c15 : ∀ r, r < 64 → layer (p1024 (64 * 15 + r)) 8 25 = [] := by decide +kernel

theorem p1024_all (i : Nat) (hi : i < 1024) : layer (p1024 i) 8 25 = [] := by
  have h : i = 64 * (i / 64) + i % 64 := (Nat.div_add_mod i 64).symm
  have hr : i % 64 < 64 := Nat.mod_lt _ (by decide)
  generalize i / 64 = c at h
  generalize i % 64 = r at h hr
  subst h
  match c, hi with
  | 0, _ => exact p1024_c0 r hr
  | 1, _ => exact p1024_c1 r hr
  | 2, _ => exact p1024_c2 r hr
  | 3, _ => exact p1024_c3 r hr
  | 4, _ => exact p1024_c4 r hr
  | 5, _ => exact p1024_c5 r hr
  | 6, _ => exact p1024_c6 r hr
  | 7, _ => exact p1024_c7 r hr
  | 8, _ => exact p1024_c8 r hr
  | 9, _ => exact p1024_c9 r hr
  | 10, _ => exact p1024_c10 r hr
  | 11, _ => exact p1024_c11 r hr
  | 12, _ => exact p1024_c12 r hr
  | 13, _ => exact p1024_c13 r hr
  | 14, _ => exact p1024_c14 r hr
  | 15, _ => exact p1024_c15 r hr
  | c + 16, hi => omega

/-- **P1024: every alignment's longest episode at depth 8 is at most 24 ticks.** -/
theorem p1024_mfinite (i : Nat) : MFinite (p1024 i) 8 :=
  ⟨24, fun x a hx hep => rep_bound _ 8 24 (p1024_all _ (Nat.mod_lt _ (by decide))) x hx
    ((episode_congr (p1024_shift i a) x 25).mp hep)⟩

/-! ### The 480-phase: `z0` = the ring of `phase480_p32.txt`, `z1` = its frame image, `c² = ρ^270` (-270 ≡ 210), depth 10 -/

def ring480a : Nat := 0x9861e9a04f7067dac9855878434051a9ac566ccbb240d95a851645fa61ec99bc017079e98e984fd923ea07957af9dd192e8ea953a236813745eb9250

def ring480b : Nat := 0xe9a61e61f091b8257e9aa989ccc1b65e55ab97745fc32ea59b6bda07a617ee4406918e1eb1e9f02fec1618ea850e236fd1b15ebc6ec987c8da14ffb3

def z0 (n : Nat) : Bool := ring480a.testBit (n % 480)

def z1 (n : Nat) : Bool := ring480b.testBit (n % 480)

def zz : Nat → Nat → Bool
  | 0, n => z0 n
  | _ + 1, n => z1 n

/-- The 480-phase at alignment representative `(r, s)`: frame time `t + s`, even times `z0`, odd times `z1`. -/
def p480 (r s : Nat) : Nat → Nat → Bool := fun j t => zz ((t + s) % 2) (j + r + 210 * ((t + s) / 2))

theorem zz_congr (b : Nat) {m n : Nat} (h : m % 480 = n % 480) : zz b m = zz b n := by
  cases b <;> simp only [zz, z0, z1] <;> rw [h]

theorem z_step0_lt : ∀ n, n < 480 → z1 (n + 2) = xor (z0 (n + 2)) (z0 (n + 1) || z0 n) := by decide +kernel

theorem z_step1_lt : ∀ n, n < 480 → z0 (n + 212) = xor (z1 (n + 2)) (z1 (n + 1) || z1 n) := by decide +kernel

theorem z_step0 (n : Nat) : zz 1 (n + 2) = xor (zz 0 (n + 2)) (zz 0 (n + 1) || zz 0 n) := by
  rw [zz_congr 1 (show (n + 2) % 480 = (n % 480 + 2) % 480 by omega),
    zz_congr 0 (show (n + 2) % 480 = (n % 480 + 2) % 480 by omega),
    zz_congr 0 (show (n + 1) % 480 = (n % 480 + 1) % 480 by omega),
    zz_congr 0 (show n % 480 = n % 480 % 480 by omega)]
  exact z_step0_lt _ (Nat.mod_lt _ (by decide))

theorem z_step1 (n : Nat) : zz 0 (n + 212) = xor (zz 1 (n + 2)) (zz 1 (n + 1) || zz 1 n) := by
  rw [zz_congr 0 (show (n + 212) % 480 = (n % 480 + 212) % 480 by omega),
    zz_congr 1 (show (n + 2) % 480 = (n % 480 + 2) % 480 by omega),
    zz_congr 1 (show (n + 1) % 480 = (n % 480 + 1) % 480 by omega),
    zz_congr 1 (show n % 480 = n % 480 % 480 by omega)]
  exact z_step1_lt _ (Nat.mod_lt _ (by decide))

theorem p480_phase (r s : Nat) : IsPhase (p480 r s) 32 where
  pos := by decide
  step j t := by
    show zz ((t + 1 + s) % 2) (j + 2 + r + 210 * ((t + 1 + s) / 2)) =
      xor (zz ((t + s) % 2) (j + 2 + r + 210 * ((t + s) / 2)))
        (zz ((t + s) % 2) (j + 1 + r + 210 * ((t + s) / 2)) || zz ((t + s) % 2) (j + r + 210 * ((t + s) / 2)))
    rcases Nat.mod_two_eq_zero_or_one (t + s) with h | h
    · rw [show (t + 1 + s) % 2 = 1 by omega, show (t + 1 + s) / 2 = (t + s) / 2 by omega, h,
        show j + 2 + r + 210 * ((t + s) / 2) = j + r + 210 * ((t + s) / 2) + 2 by omega,
        show j + 1 + r + 210 * ((t + s) / 2) = j + r + 210 * ((t + s) / 2) + 1 by omega]
      exact z_step0 _
    · rw [show (t + 1 + s) % 2 = 0 by omega, h,
        show j + 2 + r + 210 * ((t + 1 + s) / 2) = j + r + 210 * ((t + s) / 2) + 212 by omega,
        show j + 2 + r + 210 * ((t + s) / 2) = j + r + 210 * ((t + s) / 2) + 2 by omega,
        show j + 1 + r + 210 * ((t + s) / 2) = j + r + 210 * ((t + s) / 2) + 1 by omega]
      exact z_step1 _
  period j t := by
    show zz ((t + 32 + s) % 2) (j + r + 210 * ((t + 32 + s) / 2)) = zz ((t + s) % 2) (j + r + 210 * ((t + s) / 2))
    rw [show (t + 32 + s) % 2 = (t + s) % 2 by omega]
    exact zz_congr _ (by omega)

theorem p480_shift (r s a : Nat) (j t : Nat) :
    p480 r s j (t + a) = p480 ((r + 210 * ((s + a) / 2)) % 480) ((s + a) % 2) j (t + 0) := by
  show zz ((t + a + s) % 2) (j + r + 210 * ((t + a + s) / 2)) =
    zz ((t + 0 + (s + a) % 2) % 2) (j + (r + 210 * ((s + a) / 2)) % 480 + 210 * ((t + 0 + (s + a) % 2) / 2))
  rw [show (t + 0 + (s + a) % 2) % 2 = (t + a + s) % 2 by omega]
  exact zz_congr _ (by omega)

theorem p480_c0 : ∀ r, r < 32 → layer (p480 (32 * 0 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 0 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c1 : ∀ r, r < 32 → layer (p480 (32 * 1 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 1 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c2 : ∀ r, r < 32 → layer (p480 (32 * 2 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 2 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c3 : ∀ r, r < 32 → layer (p480 (32 * 3 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 3 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c4 : ∀ r, r < 32 → layer (p480 (32 * 4 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 4 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c5 : ∀ r, r < 32 → layer (p480 (32 * 5 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 5 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c6 : ∀ r, r < 32 → layer (p480 (32 * 6 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 6 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c7 : ∀ r, r < 32 → layer (p480 (32 * 7 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 7 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c8 : ∀ r, r < 32 → layer (p480 (32 * 8 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 8 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c9 : ∀ r, r < 32 → layer (p480 (32 * 9 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 9 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c10 : ∀ r, r < 32 → layer (p480 (32 * 10 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 10 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c11 : ∀ r, r < 32 → layer (p480 (32 * 11 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 11 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c12 : ∀ r, r < 32 → layer (p480 (32 * 12 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 12 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c13 : ∀ r, r < 32 → layer (p480 (32 * 13 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 13 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_c14 : ∀ r, r < 32 → layer (p480 (32 * 14 + r) 0) 10 25 = [] ∧ layer (p480 (32 * 14 + r) 1) 10 25 = [] := by
  decide +kernel

theorem p480_all_r (i : Nat) (hi : i < 480) : layer (p480 i 0) 10 25 = [] ∧ layer (p480 i 1) 10 25 = [] := by
  have h : i = 32 * (i / 32) + i % 32 := (Nat.div_add_mod i 32).symm
  have hr : i % 32 < 32 := Nat.mod_lt _ (by decide)
  generalize i / 32 = c at h
  generalize i % 32 = r at h hr
  subst h
  match c, hi with
  | 0, _ => exact p480_c0 r hr
  | 1, _ => exact p480_c1 r hr
  | 2, _ => exact p480_c2 r hr
  | 3, _ => exact p480_c3 r hr
  | 4, _ => exact p480_c4 r hr
  | 5, _ => exact p480_c5 r hr
  | 6, _ => exact p480_c6 r hr
  | 7, _ => exact p480_c7 r hr
  | 8, _ => exact p480_c8 r hr
  | 9, _ => exact p480_c9 r hr
  | 10, _ => exact p480_c10 r hr
  | 11, _ => exact p480_c11 r hr
  | 12, _ => exact p480_c12 r hr
  | 13, _ => exact p480_c13 r hr
  | 14, _ => exact p480_c14 r hr
  | c + 15, hi => omega

theorem p480_all (r s : Nat) (hr : r < 480) (hs : s < 2) : layer (p480 r s) 10 25 = [] := by
  match s, hs with
  | 0, _ => exact (p480_all_r r hr).1
  | 1, _ => exact (p480_all_r r hr).2
  | s + 2, hs => omega

/-- **The 480-phase: every alignment's longest episode at depth 10 is at most 24 ticks.** -/
theorem p480_mfinite (r s : Nat) : MFinite (p480 r s) 10 :=
  ⟨24, fun x a hx hep => rep_bound _ 10 24 (p480_all _ _ (Nat.mod_lt _ (by decide)) (Nat.mod_lt _ (by decide))) x hx
    ((episode_congr (p480_shift r s a) x 25).mp hep)⟩

end Ruliology.CellularAutomata.Rule30PhaseTrees

#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.g16_mfinite
#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.p1024_mfinite
#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.p480_mfinite
#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.p480_phase
#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.p1024_phase
#print axioms Ruliology.CellularAutomata.Rule30PhaseTrees.no_tail_of_mfinite
