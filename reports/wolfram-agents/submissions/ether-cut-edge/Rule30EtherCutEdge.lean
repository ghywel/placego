module

public import Ruliology.CellularAutomata.Rule30FrozenRuler
public import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers

/-!
# Rule 30: the cut ether is off the single cell's edge cycle

`Rule30ZeroBoundaryBarriers` uses the truncations `c7cut N` of the period-4 configuration `c7`
(black exactly at `p ≡ 6 mod 7`) as witnesses of its two-sided barrier. `Rule30FrozenRuler` reads a
finite row from its rightmost black cell: its edge code evolves by the edge map `T`, and a code of
depth `k` with phase `s₀` follows the single cell's code at time `s₀ + t` below bit `k` and differs
from it at bit `k`, for ever (`frozen_ruler`). This module computes where the cut ether sits.

* `cut_code_prefix`, `c7cut_depth`: for every `N`, the edge code of `c7cut N`, read from its
  rightmost black cell `7 N + 6`, begins `1 0 0 0 0 0 0 1 0` (bits `0` and `7` black), and it has
  depth `8` with phase `16`.
* `c7cut_frozen`: so by the frozen ruler, at every time `t` its code agrees with the single cell's
  at time `16 + t` below bit `8` and differs at bit `8`, and the white run behind its edge cell is
  never `8` or longer.
* `c7cut_off_seed`: more: at no time does its code agree below bit `9` with the single cell's code
  at any time. The first nine bits of the single cell's code run through a cycle of `32` values
  (`cycle9`), which `129` misses, and the edge map permutes the odd nine-bit codes, so the
  complement of that cycle is closed too (`off9_closed`). Hence no row of the evolution of
  `c7cut N` is a translate of a row of the single cell (`c7cut_not_seed_row`).
* `seed_no_flush_ether`: no row of the single cell shows, flush with its rightmost black cell,
  thirteen consecutive cells of the ether `c7` at any phase and position: the first thirteen bits
  of its code run through a cycle of `64` values (`cycle13`), none of them a thirteen-cell word of
  `c7`. The bound is sharp: at time `55` the first twelve cells agree with the ether at phase `3`
  (`seed_flush_ether_sharp`).

The computations are on `k`-bit codes, where the edge map is `c xor ((c << 1) or (c << 2))`
modulo `2 ^ k` (`enc_T`). The flush condition matters: without it the statement is false, since
the single cell's row at time `204` has thirteen ether cells at distances `7..19` behind its edge
(`seed_offset_ether_204`).
The single cell's nonfinite past is known (`lhallee/rule30-open`, `SeedPastPeriods`); nothing here
concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30EtherCutEdge

open Rule30Jen Rule30Realization Rule30FrozenRuler
open Rule30ZeroBoundaryBarriers (c7 c7cut c7cut_eq c7cut_hi c7cut_above evol_c7_shift evol_c7_period_mul)

/-! ### The edge map on `k`-bit codes -/

/-- The edge map on the first `k` bits of a code, as a number. -/
def Tm (k c : Nat) : Nat := (c ^^^ ((c <<< 1) ||| (c <<< 2))) % 2 ^ k

/-- `itN f n x`: `n` applications of `f`. -/
def itN (f : Nat → Nat) : Nat → Nat → Nat
  | 0, x => x
  | n + 1, x => f (itN f n x)

/-- The first `k` bits of a code, as a number (bit `i` is `c i`). -/
def enc : Nat → (Nat → Bool) → Nat
  | 0, _ => 0
  | k + 1, c => (if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))

theorem testBit_enc : ∀ k (c : Nat → Bool) i, (enc k c).testBit i = (decide (i < k) && c i)
  | 0, c, i => by simp [enc]
  | k + 1, c, 0 => by
    rw [Nat.testBit_zero]
    simp only [enc]
    by_cases h : c 0 <;> simp [h] <;> omega
  | k + 1, c, i + 1 => by
    rw [Nat.testBit_succ]
    simp only [enc]
    have : ((if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))) / 2 = enc k (fun i => c (i + 1)) := by
      by_cases h : c 0 <;> simp [h] <;> omega
    rw [this, testBit_enc k (fun i => c (i + 1)) i]
    simp

theorem enc_ext {k : Nat} {c d : Nat → Bool} : enc k c = enc k d ↔ AgreeBelow k c d := by
  constructor
  · intro h i hi
    have := congrArg (fun n => n.testBit i) h
    simpa [testBit_enc, hi] using this
  · intro h
    apply Nat.eq_of_testBit_eq
    intro i
    rw [testBit_enc, testBit_enc]
    by_cases hi : i < k
    · simp [hi, h i hi]
    · simp [hi]

theorem enc_T (k : Nat) (c : Nat → Bool) : enc k (T c) = Tm k (enc k c) := by
  apply Nat.eq_of_testBit_eq
  intro i
  unfold Tm
  rw [testBit_enc, Nat.testBit_mod_two_pow, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft,
    Nat.testBit_shiftLeft, testBit_enc, testBit_enc, testBit_enc]
  by_cases hi : i < k
  · simp only [hi, decide_true, Bool.true_and]
    match i, hi with
    | 0, _ => simp [T]
    | 1, _ => simp [T, show 0 < k by omega]
    | j + 2, _ =>
      simp [T, show j + 1 < k by omega, show j < k by omega]
  · simp [hi]

theorem enc_iter (k : Nat) (c : Nat → Bool) : ∀ n, enc k (Rule30FrozenRuler.iter n c) = itN (Tm k) n (enc k c)
  | 0 => rfl
  | n + 1 => by
    show enc k (T (Rule30FrozenRuler.iter n c)) = Tm k (itN (Tm k) n (enc k c))
    rw [enc_T, enc_iter k c n]

theorem enc_one : ∀ k, 1 ≤ k → enc k one = 1
  | 0, h => absurd h (by omega)
  | k + 1, _ => by
    simp only [enc]
    have : enc k (fun i => one (i + 1)) = 0 := by
      have hz : ∀ m (c : Nat → Bool), (∀ i, c i = false) → enc m c = 0 := by
        intro m
        induction m with
        | zero => intro c _; rfl
        | succ m ih => intro c hc; simp only [enc, hc 0]; rw [ih _ (fun i => hc (i + 1))]; rfl
      exact hz k _ (fun i => by simp [one])
    rw [this]
    simp [one]

theorem enc_orbit (k : Nat) (hk : 1 ≤ k) (s : Nat) : enc k (orbit s) = itN (Tm k) s 1 := by
  rw [orbit, enc_iter, enc_one k hk]

/-! ### The single cell's cycles of nine and of thirteen bits -/

/-- The first nine bits of the single cell's code at the times `0 .. 31`. -/
def C9 : List Nat := (List.range 32).map fun s => itN (Tm 9) s 1

/-- The first thirteen bits of the single cell's code at the times `0 .. 63`. -/
def C13 : List Nat := (List.range 64).map fun s => itN (Tm 13) s 1

/-- **The nine-bit cycle**: the first nine bits of the single cell's code return to `1` after `32`
steps, take `32` distinct values before, are closed under the edge map, and never equal `129`. -/
theorem cycle9 : itN (Tm 9) 32 1 = 1 ∧
    (∀ i, i < 32 → ∀ j, j < 32 → itN (Tm 9) i 1 = itN (Tm 9) j 1 → i = j) ∧
    C9.all (fun x => C9.contains (Tm 9 x)) = true ∧ C9.contains 129 = false := by decide +kernel

/-- **The thirteen-bit cycle**: `64` distinct values, closed under the edge map. -/
theorem cycle13 : itN (Tm 13) 64 1 = 1 ∧
    (∀ i, i < 64 → ∀ j, j < 64 → itN (Tm 13) i 1 = itN (Tm 13) j 1 → i = j) ∧
    C13.all (fun x => C13.contains (Tm 13 x)) = true := by decide +kernel

theorem orbit_mem (k : Nat) (C : List Nat) (h1 : C.contains 1 = true)
    (hC : C.all (fun x => C.contains (Tm k x)) = true) : ∀ s, C.contains (itN (Tm k) s 1) = true
  | 0 => h1
  | s + 1 => by
    have hm := orbit_mem k C h1 hC s
    exact List.all_eq_true.1 hC _ (List.contains_iff_mem.1 hm)

theorem orbit9_mem (s : Nat) : C9.contains (enc 9 (orbit s)) = true := by
  rw [enc_orbit 9 (by omega)]
  exact orbit_mem 9 C9 (by decide) cycle9.2.2.1 s

theorem orbit13_mem (s : Nat) : C13.contains (enc 13 (orbit s)) = true := by
  rw [enc_orbit 13 (by omega)]
  exact orbit_mem 13 C13 (by decide) cycle13.2.2 s

/-- **The odd nine-bit codes off the cycle stay off it.** -/
theorem off9_closed : ∀ x, x < 512 → x % 2 = 1 → C9.contains x = false →
    Tm 9 x < 512 ∧ (Tm 9 x) % 2 = 1 ∧ C9.contains (Tm 9 x) = false := by decide +kernel

/-! ### The cut ether -/

theorem code_cut (N k : Nat) : code (c7cut N) (7 * (N : Int) + 6) k =
    (decide (k ≤ 14 * N + 7) && decide (k % 7 = 0)) := by
  unfold code
  rw [c7cut_eq]
  by_cases hk : k ≤ 14 * N + 7
  · rw [ite_eq_left (by omega)]
    unfold c7
    simp only [hk, decide_true, Bool.true_and]
    have : (7 * (N : Int) + 6 - (k : Int) + 1) % 7 = 0 ↔ k % 7 = 0 := by omega
    exact decide_eq_decide.2 this
  · rw [ite_eq_right (by omega)]
    simp [hk]

/-- **The cut's code begins `1 0 0 0 0 0 0 1 0`**, for every `N`. -/
theorem cut_code_prefix (N : Nat) : ∀ i, i < 9 →
    code (c7cut N) (7 * (N : Int) + 6) i = decide (i = 0 ∨ i = 7) := by
  intro i hi
  rw [code_cut]
  have : (decide (i ≤ 14 * N + 7) && decide (i % 7 = 0)) = decide (i = 0 ∨ i = 7) := by
    by_cases h0 : i = 0
    · subst h0; simp
    · by_cases h7 : i = 7
      · subst h7; simp
      · have : ¬ (i % 7 = 0) := by omega
        simp [this, h0, h7]
  exact this

theorem enc9_cut (N : Nat) : enc 9 (code (c7cut N) (7 * (N : Int) + 6)) = 129 := by
  have h : enc 9 (fun i => decide (i = 0 ∨ i = 7)) = 129 := by decide +kernel
  rw [← h, enc_ext]
  intro i hi
  exact cut_code_prefix N i hi

/-- **Depth `8`, phase `16`**, for every cut. -/
theorem c7cut_depth (N : Nat) : HasDepth (code (c7cut N) (7 * (N : Int) + 6)) 8 16 := by
  refine ⟨?_, fun s hs => ?_⟩
  · rw [← enc_ext, enc_orbit 8 (by omega)]
    have h8 : enc 8 (code (c7cut N) (7 * (N : Int) + 6)) = 129 := by
      have h : enc 8 (fun i => decide (i = 0 ∨ i = 7)) = 129 := by decide +kernel
      rw [← h, enc_ext]
      intro i hi
      exact cut_code_prefix N i (by omega)
    rw [h8]
    decide +kernel
  · have h := enc_ext.2 (show AgreeBelow 9 (orbit s) (code (c7cut N) (7 * (N : Int) + 6)) from
      fun i hi => hs i (by omega))
    rw [enc9_cut] at h
    have := orbit9_mem s
    rw [h, cycle9.2.2.2] at this
    exact Bool.noConfusion this

/-- **The frozen ruler for the cut ether.** -/
theorem c7cut_frozen (N t : Nat) :
    AgreeBelow 8 (code (cell (16 + t)) ((16 + t : Nat) : Int))
        (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) ∧
      code (cell (16 + t)) ((16 + t : Nat) : Int) 8 ≠ code (evol (c7cut N) t) (7 * (N : Int) + 6 + t) 8 ∧
      ∀ w, 8 ≤ w → ¬ Width (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) w := by
  have h := frozen_ruler (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N)
    (fun p hp => c7cut_above N p hp) 8 16 (by omega) (c7cut_depth N) t
  exact ⟨h.2.2.1, h.2.2.2.1, h.2.2.2.2.2.2⟩

/-- **At no time does the cut's code agree with any of the single cell's codes below bit `9`.** -/
theorem c7cut_off_seed (N t s : Nat) :
    ¬ AgreeBelow 9 (orbit s) (code (evol (c7cut N) t) (7 * (N : Int) + 6 + t)) := by
  intro hs
  have he := (edge_evol (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N) (fun p hp => c7cut_above N p hp) t).2.2
  rw [he, ← enc_ext, enc_iter, enc9_cut] at hs
  have hinv : ∀ n, itN (Tm 9) n 129 < 512 ∧ (itN (Tm 9) n 129) % 2 = 1 ∧
      C9.contains (itN (Tm 9) n 129) = false := by
    intro n
    induction n with
    | zero => exact ⟨by decide, by decide, cycle9.2.2.2⟩
    | succ n ih => exact off9_closed _ ih.1 ih.2.1 ih.2.2
  have hm := orbit9_mem s
  rw [hs, (hinv t).2.2] at hm
  exact Bool.noConfusion hm

theorem seed_edge (s : Nat) : cell s s = true ∧ ∀ p, (s : Int) < p → cell s p = false := by
  have h := edge_evol seed 0 (by simp [seed]) (fun p hp => by simp [seed]; omega) s
  refine ⟨?_, fun p hp => ?_⟩
  · rw [← evol_seed]; simpa using h.1
  · rw [← evol_seed]; exact h.2.1 p (by omega)

/-- **No row of the evolution of a cut is a translate of a row of the single cell.** -/
theorem c7cut_not_seed_row (N t s : Nat) (d : Int) :
    ¬ ∀ q, evol (c7cut N) t q = cell s (q + d) := by
  intro h
  obtain ⟨h1, h2, -⟩ := edge_evol (c7cut N) (7 * (N : Int) + 6) (c7cut_hi N)
    (fun p hp => c7cut_above N p hp) t
  obtain ⟨s1, s2⟩ := seed_edge s
  have hpos : 7 * (N : Int) + 6 + t + d = s := by
    rcases Int.lt_trichotomy (7 * (N : Int) + 6 + t + d) s with hlt | heq | hgt
    · have h3 := h2 ((s : Int) - d) (by omega)
      rw [h, show (s : Int) - d + d = s by omega, s1] at h3
      exact absurd h3 (by decide)
    · exact heq
    · have h3 := h1
      rw [h, s2 _ hgt] at h3
      exact absurd h3 (by decide)
  apply c7cut_off_seed N t s
  intro i _
  rw [← seed_code]
  unfold code
  rw [h, show 7 * (N : Int) + 6 + t - (i : Int) + d = (s : Int) - i by omega]

/-! ### Flush ether words -/

/-- The first `13` cells of the ether `c7` at phase `a`, read leftward from position `p`. -/
def ew (a : Nat) (p : Int) : Nat := enc 13 (fun j => evol c7 a (p - j))

/-- **No thirteen-cell word of the ether is a code of the single cell.** -/
theorem ether_off_cycle13 : ∀ a, a < 4 → ∀ p : Nat, p < 7 → C13.contains (ew a p) = false := by
  decide +kernel

theorem ew_reduce (a : Nat) (p : Int) : ew a p = ew (a % 4) ((p % 7 : Int).toNat) := by
  unfold ew
  congr 1
  funext j
  have e1 : evol c7 a (p - j) = evol c7 (a % 4) (p - j) := by
    have := evol_c7_period_mul (a % 4) (a / 4) (p - j)
    rw [show a % 4 + 4 * (a / 4) = a by omega] at this
    exact this
  have e2 : evol c7 (a % 4) (p - j) = evol c7 (a % 4) (((p % 7 : Int).toNat : Int) - j) := by
    have := evol_c7_shift (a % 4) (((p % 7 : Int).toNat : Int) - j) (p / 7)
    rw [show ((p % 7 : Int).toNat : Int) - j + 7 * (p / 7) = p - j by
      have := Int.emod_nonneg p (by decide : (7 : Int) ≠ 0); omega] at this
    exact this
  rw [e1, e2]

/-- **No flush ether word on the single cell.** At every time `s`, for every phase `a` and
position `p` of the ether, one of the first thirteen cells behind and including the single cell's
rightmost black cell differs from the ether. -/
theorem seed_no_flush_ether (s a : Nat) (p : Int) :
    ∃ j, j < 13 ∧ code (cell s) s j ≠ evol c7 a (p - j) := by
  refine Classical.byContradiction fun hne => ?_
  have hag : AgreeBelow 13 (orbit s) (fun j => evol c7 a (p - j)) := by
    intro j hj
    rw [← seed_code]
    exact Classical.byContradiction fun h => hne ⟨j, hj, h⟩
  have h := enc_ext.2 hag
  have hm := orbit13_mem s
  rw [h, show enc 13 (fun j => evol c7 a (p - j)) = ew a p from rfl, ew_reduce,
    ether_off_cycle13 (a % 4) (by omega) ((p % 7 : Int).toNat)
      (by have := Int.emod_nonneg p (by decide : (7 : Int) ≠ 0); omega)] at hm
  exact Bool.noConfusion hm

/-- **Sharpness**: at time `55` the first twelve cells of the single cell's code agree with the
ether at phase `3`, position `4`. -/
theorem seed_flush_ether_sharp :
    ∀ j, j < 12 → code (cell 55) ((55 : Nat) : Int) j = evol c7 3 (4 - j) := by
  intro j hj
  have h : itN (Tm 12) 55 1 = enc 12 (fun j => evol c7 3 (4 - j)) := by decide +kernel
  rw [← enc_orbit 12 (by omega), enc_ext] at h
  rw [seed_code]
  exact h j hj

/-- **The flush condition is needed.** At time `204` the thirteen cells at distances `7 .. 19`
behind the single cell's rightmost black cell are the ether at phase `2`, position `1`. -/
theorem seed_offset_ether_204 :
    ∀ j, j < 13 → code (cell 204) ((204 : Nat) : Int) (7 + j) = evol c7 2 (1 - j) := by
  intro j hj
  have h : ∀ j, j < 13 → (itN (Tm 20) 204 1).testBit (7 + j) = evol c7 2 (1 - j) := by
    decide +kernel
  have e := testBit_enc 20 (orbit 204) (7 + j)
  rw [enc_orbit 20 (by omega)] at e
  rw [seed_code, ← h j hj, e]
  simp [show 7 + j < 20 by omega]

end Rule30EtherCutEdge
end Ruliology.CellularAutomata
