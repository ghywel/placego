module

public import Ruliology.CellularAutomata.Rule30LeftCoincidence
public import Ruliology.CellularAutomata.Rule30FiniteDiagonals

/-!
# One left side: every configuration with a leftmost black cell carries the universal strip below the first even fork

Rowland (*Local nested structure in rule 30*, 2006, §5) conjectured that rule 30 has "really only one left side": from
any row with a leftmost black cell, the eventual period of each left diagonal is independent of the row. He gave the
inductive argument in prose (unless the nearer parent diagonal is eventually white, the child's period is forced by its
two parents; at a white nearer parent with an odd number of blacks per period in the farther parent, the two continuations
are complements) and located the first possible failure at his column 53,209 (wheel 53,208 here), where the nearer parent
is eventually white and the farther parent has an even number of blacks per period. This module proves the induction in
the kit's reset framework, for every configuration with a leftmost black cell, with one common time shift.

Wall frame: `Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`) is the `j`-th left diagonal of the configuration
`x`, whose leftmost black cell is at `lo`. The diagonals obey the reset recurrence `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨
Ld (j + 2) t)` (`Ld_step`), the child `j + 2` driven by the nearer word `j + 1` and the farther word `j`.

A **strip** `C : Nat → Nat → Bool` (wheel, time) is `Admissible` below a cut `J` when `C 0 = C 1 = 1`, each `C (j + 2)` obeys the
recurrence driven by `C j` and `C (j + 1)`, and at each wheel either the nearer word `C (j + 1)` has blacks arbitrarily late
or it is white and the farther word `C j` has odd parity over a common period `L` of the lower strip. The universal strip of
the single black cell, generated from `C 0 = C 1 = 1` by the recurrence alone, is admissible below `J = 53208` (its white
words are wheels 2, 7, 28, 399 with farther weights 1, 1, 3, 3 over the common periods 1, 2, 4, 8; the first even case is
wheel 53,207 with weight 6 over period 16); that is a finite check of the data, outside this module.

* `one_left_side`: for every admissible strip `C` below `J` and every configuration `x` white left of `lo` with `x lo = true`,
  there are a shift `s` and a time `T` with `Ld x lo j t = C j (t + s)` for all `j < J` and `t ≥ T`. The induction: at a nearer
  word with a black, the row's child and the strip's word are two solutions of one recurrence with the same parents, and
  agree from the first black on (`Rule30LeftCoincidence.solutions_agree`); at a white nearer word both integrate the same
  farther word, so their difference is constant, and if it is `1` the odd parity turns it into a shift by `L`
  (`Rule30LeftReset.white_shift`), which leaves the `L`-periodic lower strip unchanged. So one shift aligns the whole strip.
* `same_left_side`: any two configurations with a leftmost black cell have the same left side below `J`, up to a time shift.
* `seed_left_side`: the single black cell's diagonals `D j` are eventually the strip's words: the seed is such a configuration,
  so its own strip is certified by the theorem, with no evolution of the seed.

Nothing here concerns the center column or the Prize problems; beyond the first even fork the strip branches (Rowland's
further columns 58,288 and 72,577), and that is outside the statement. Proposed in the contributors' record by Claude
(Anthropic), after Rowland's argument; the reset lemmas are the kit's and `Rule30LeftCoincidence`'s.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30UniversalLeftSide

set_option autoImplicit false

open Rule30Jen Rule30Realization Rule30Diagonals Rule30LeftReset Rule30LeftCoincidence Rule30FiniteDiagonals

/-- A strip `C` (wheel `j`, time `t`) is admissible below the cut `J`: the base words are black, every word obeys the
reset recurrence driven by the two below it, and no wheel below `J` is an even fork: the nearer word has blacks arbitrarily
late, or it is white and the farther word has odd parity over a common period `L` of the whole lower strip. -/
structure Admissible (C : Nat → Nat → Bool) (J : Nat) : Prop where
  base0 : ∀ t, C 0 t = true
  base1 : ∀ t, C 1 t = true
  step : ∀ j t, j + 2 < J → C (j + 2) (t + 1) = xor (C j t) (C (j + 1) t || C (j + 2) t)
  fork : ∀ j, j + 2 < J →
    (∀ T, ∃ t, T ≤ t ∧ C (j + 1) t = true) ∨
    ((∀ t, C (j + 1) t = false) ∧
      ∃ L, (∀ k, k ≤ j → ∀ t, C k (t + L) = C k t) ∧ ∀ t, par (C j) t L = true)

/-- The parity of a shifted word is the parity of the word at the shifted time. -/
theorem par_shift (a : Nat → Bool) (s t : Nat) : ∀ L, par (fun u => a (u + s)) t L = par a (t + s) L
  | 0 => rfl
  | L + 1 => by
    simp only [par, par_shift a s t L]
    rw [show t + L + s = t + s + L by omega]

section Config

variable {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true)
include hleft hlo

/-- Wheel `0`, the left edge, is black at every time. -/
theorem Ld_zero_eq : ∀ t, Ld x lo 0 t = true
  | 0 => by
    show evol x 0 (lo - ((0 : Nat) : Int) + ((0 : Nat) : Int)) = true
    rw [show lo - ((0 : Nat) : Int) + ((0 : Nat) : Int) = lo by omega]
    exact hlo
  | t + 1 => by rw [Ld_zero_succ hleft t, Ld_zero_eq t]

/-- Wheel `1` is black from time `1` on. -/
theorem Ld_one_eq (t : Nat) : Ld x lo 1 (t + 1) = true := by
  rw [Ld_one_succ hleft t, Ld_zero_eq hleft hlo t]
  rfl

/-- The induction: the row's wheels `0 … n` are the strip's words at one common shift, from some time on. -/
theorem aligned {C : Nat → Nat → Bool} {J : Nat} (hC : Admissible C J) :
    ∀ n, n < J → ∃ s T, ∀ j, j ≤ n → ∀ t, T ≤ t → Ld x lo j t = C j (t + s)
  | 0, _ => ⟨0, 0, fun j hj t _ => by
      have hj0 : j = 0 := by omega
      subst hj0
      rw [Ld_zero_eq hleft hlo t, hC.base0]⟩
  | 1, _ => ⟨0, 1, fun j hj t ht => by
      rcases Nat.lt_or_ge j 1 with h0 | h1
      · have hj0 : j = 0 := by omega
        subst hj0
        rw [Ld_zero_eq hleft hlo t, hC.base0]
      · have hj1 : j = 1 := by omega
        subst hj1
        obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
        rw [Ld_one_eq hleft hlo u, hC.base1]⟩
  | n + 2, hn => by
    obtain ⟨s, T, ih⟩ := aligned hC (n + 1) (by omega)
    -- the row's child from `T` on, driven by the strip's shifted parents
    have hy : ∀ t, T ≤ t → Ld x lo (n + 2) (t + 1) =
        xor (C n (t + s)) (C (n + 1) (t + s) || Ld x lo (n + 2) t) := by
      intro t ht
      rw [Ld_step (x := x) (lo := lo) n t, ih n (by omega) t ht, ih (n + 1) (by omega) t ht]
    -- the strip's shifted word, at every time
    have hz : ∀ t, C (n + 2) (t + 1 + s) = xor (C n (t + s)) (C (n + 1) (t + s) || C (n + 2) (t + s)) := by
      intro t
      have h := hC.step n (t + s) (by omega)
      rwa [show t + s + 1 = t + 1 + s by omega] at h
    rcases hC.fork n (by omega) with hblack | ⟨hwhite, L, hL, hpar⟩
    · -- a black of the nearer word at or after `T`: both children are forced from there
      obtain ⟨t0, ht0, hb⟩ := hblack (T + s)
      have hy' : ∀ u, Ld x lo (n + 2) (T + (u + 1)) =
          xor (C n (T + u + s)) (C (n + 1) (T + u + s) || Ld x lo (n + 2) (T + u)) := by
        intro u
        rw [show T + (u + 1) = T + u + 1 by omega]
        exact hy (T + u) (by omega)
      have hz' : ∀ u, C (n + 2) (T + (u + 1) + s) =
          xor (C n (T + u + s)) (C (n + 1) (T + u + s) || C (n + 2) (T + u + s)) := by
        intro u
        rw [show T + (u + 1) + s = T + u + 1 + s by omega]
        exact hz (T + u)
      have hs0 : C (n + 1) (T + (t0 - T - s) + s) = true := by
        rw [show T + (t0 - T - s) + s = t0 by omega]
        exact hb
      have agree := solutions_agree (x := fun u => Ld x lo (n + 2) (T + u)) (a := fun u => C n (T + u + s))
        (b := fun u => C (n + 1) (T + u + s)) (x' := fun u => C (n + 2) (T + u + s)) hy' hz' (s0 := t0 - T - s) hs0
      refine ⟨s, t0 + 1, fun j hj t ht => ?_⟩
      rcases Nat.lt_or_ge j (n + 2) with hlt | hge
      · exact ih j (by omega) t (by omega)
      · have hj2 : j = n + 2 := by omega
        subst hj2
        have h : Ld x lo (n + 2) (T + (t - T)) = C (n + 2) (T + (t - T) + s) := agree (t - T) (by omega)
        rw [show T + (t - T) = t by omega] at h
        exact h
    · -- a white nearer word: both children integrate the farther word; the difference is constant
      have hyB : ∀ t, T ≤ t → Ld x lo (n + 2) (t + 1) = xor (C n (t + s)) (Ld x lo (n + 2) t) := by
        intro t ht
        rw [hy t ht, hwhite]
        rfl
      have hzB : ∀ t, C (n + 2) (t + 1 + s) = xor (C n (t + s)) (C (n + 2) (t + s)) := by
        intro t
        rw [hz t, hwhite]
        rfl
      have hdiff : ∀ t, T ≤ t → xor (Ld x lo (n + 2) t) (C (n + 2) (t + s)) =
          xor (Ld x lo (n + 2) T) (C (n + 2) (T + s)) := by
        intro t ht
        induction t with
        | zero =>
          have hT : T = 0 := by omega
          subst hT
          rfl
        | succ t iht =>
          rcases Nat.lt_or_ge t T with hlt | hge
          · have hT : T = t + 1 := by omega
            subst hT
            rfl
          · rw [hyB t hge, hzB t, ← iht hge]
            cases C n (t + s) <;> cases Ld x lo (n + 2) t <;> cases C (n + 2) (t + s) <;> rfl
      by_cases h0 : Ld x lo (n + 2) T = C (n + 2) (T + s)
      · -- the same solution: the shift stays
        refine ⟨s, T, fun j hj t ht => ?_⟩
        rcases Nat.lt_or_ge j (n + 2) with hlt | hge
        · exact ih j (by omega) t ht
        · have hj2 : j = n + 2 := by omega
          subst hj2
          have h1 := hdiff t ht
          rw [h0] at h1
          revert h1
          cases Ld x lo (n + 2) t <;> cases C (n + 2) (t + s) <;> cases C (n + 2) (T + s) <;> decide
      · -- the complement: the odd parity makes it the word shifted by `L`
        have hws := white_shift (x := fun u => C (n + 2) (u + s)) (a := fun u => C n (u + s))
          (b := fun u => C (n + 1) (u + s)) (s := 0) (L := L)
          (fun u => by
            show C (n + 2) (u + 1 + s) = xor (C n (u + s)) (C (n + 1) (u + s) || C (n + 2) (u + s))
            exact hz u)
          (fun u _ => hwhite (u + s))
        have hflip : ∀ t, C (n + 2) (t + L + s) = !C (n + 2) (t + s) := by
          intro t
          have h : C (n + 2) (t + L + s) = xor (C (n + 2) (t + s)) (par (fun u => C n (u + s)) t L) :=
            hws t (Nat.zero_le t)
          rw [par_shift (C n) s t L, hpar (t + s)] at h
          rw [h]
          cases C (n + 2) (t + s) <;> rfl
        have hneg : ∀ t, T ≤ t → Ld x lo (n + 2) t = !C (n + 2) (t + s) := by
          intro t ht
          have h1 := hdiff t ht
          revert h1 h0
          cases Ld x lo (n + 2) T <;> cases C (n + 2) (T + s) <;> cases Ld x lo (n + 2) t <;>
            cases C (n + 2) (t + s) <;> decide
        refine ⟨s + L, T, fun j hj t ht => ?_⟩
        rcases Nat.lt_or_ge j (n + 2) with hlt | hge
        · rcases Nat.lt_or_ge j (n + 1) with hlt' | hge'
          · rw [ih j (by omega) t ht, show t + (s + L) = t + s + L by omega, hL j (by omega) (t + s)]
          · have hj1 : j = n + 1 := by omega
            subst hj1
            rw [ih (n + 1) (by omega) t ht, hwhite, hwhite]
        · have hj2 : j = n + 2 := by omega
          subst hj2
          rw [hneg t ht, show t + (s + L) = t + L + s by omega, hflip t]

/-- **One left side.** For every admissible strip below the cut `J` and every configuration with a leftmost black cell,
one time shift aligns every wheel below `J` with the strip, from some time on. -/
theorem one_left_side {C : Nat → Nat → Bool} {J : Nat} (hC : Admissible C J) :
    ∃ s T, ∀ j, j < J → ∀ t, T ≤ t → Ld x lo j t = C j (t + s) := by
  cases J with
  | zero => exact ⟨0, 0, fun j hj => absurd hj (Nat.not_lt_zero j)⟩
  | succ n =>
    obtain ⟨s, T, h⟩ := aligned hleft hlo hC n (Nat.lt_succ_self n)
    exact ⟨s, T, fun j hj t ht => h j (Nat.lt_succ_iff.mp hj) t ht⟩

end Config

/-- Any two configurations with a leftmost black cell have the same left side below `J`, up to a time shift. -/
theorem same_left_side {C : Nat → Nat → Bool} {J : Nat} (hC : Admissible C J)
    {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true)
    {y : Int → Bool} {lo' : Int} (hleft' : ∀ p, p < lo' → y p = false) (hlo' : y lo' = true) :
    ∃ s s' T, ∀ j, j < J → ∀ t, T ≤ t → Ld x lo j (t + s') = Ld y lo' j (t + s) := by
  obtain ⟨s, T, h⟩ := one_left_side hleft hlo hC
  obtain ⟨s', T', h'⟩ := one_left_side hleft' hlo' hC
  refine ⟨s, s', T + T', fun j hj t ht => ?_⟩
  rw [h j hj (t + s') (by omega), h' j hj (t + s) (by omega), show t + s' + s = t + s + s' by omega]

/-- The single black cell's left diagonals are eventually the strip's words: the seed is one such configuration, so the
theorem certifies its own strip without evolving it. -/
theorem seed_left_side {C : Nat → Nat → Bool} {J : Nat} (hC : Admissible C J) :
    ∃ s T, ∀ j, j < J → ∀ t, T ≤ t → D j t = C j (t + s) := by
  have hleft : ∀ p, p < (0 : Int) → seed p = false := fun p hp => by
    simp only [seed, decide_eq_false_iff_not]
    omega
  have hlo : seed 0 = true := by
    simp [seed]
  obtain ⟨s, T, h⟩ := one_left_side hleft hlo hC
  refine ⟨s, T, fun j hj t ht => ?_⟩
  have e : D j t = Ld seed 0 j t := by
    show cell t ((j : Int) - (t : Int)) = evol seed t ((0 : Int) - (t : Int) + (j : Int))
    rw [evol_seed, show (0 : Int) - (t : Int) + (j : Int) = (j : Int) - (t : Int) by omega]
  rw [e]
  exact h j hj t ht

end Ruliology.CellularAutomata.Rule30UniversalLeftSide
