module

public import Ruliology.CellularAutomata.Rule30AlternatingTraceBridge
public import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# `Q01` implies mortality: an immortal frontier is a finite row

`Rule30AlternatingTraceBridge.Q01_of_mortality` gives mortality implies `Q01`. This module gives the
converse, so `Q01`, mortality and repeat budgets at every length are one statement.

An immortal frontier has successive frontiers `fr n`, each obtained from the last by a successful
update `Z` with scalar `s n`. Place the bits of `fr n` in a space-time chart at time `τ` and depth
`e + 1`, with `e` the depth inward from the terminal end:

* the high bit of depth `e` of `fr n`, where `τ + e = 2 n`;
* the low bit of depth `e` of `fr n`, where `τ + e + 1 = 2 n`.

The scan recurrences of `Z` are then the Rule 30 recurrence at every cell of depth at least two
(`chart_interior`). At depth one the two terminal symbols of a frontier, `(1, !s)` and `(s, s)`, give
the rule with a white wall from time one on (`chart_wall`). So the chart from time two is the
zero-boundary evolution of a finitely supported start (`zrow_chart`, `finSupp_start`), and column `-1`
is black at every even step, because the terminal high bit of every updated frontier is one
(`inX_start`). That is what `Rule30ZeroBoundary.Q01` forbids.

Proved here, with no finite computation:

* `mortality_of_Q01`: `Q01` implies mortality;
* `mortality_iff_Q01`: mortality is `Q01`;
* `budget_iff_Q01`: a repeat budget at every length is `Q01`.

Nothing here proves `Q01`, mortality or a budget, and Problems 1 to 3 stay open.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30FrontierChart

open Rule30SurvivalBridge

/-! ### One update, at every depth -/

theorem atDepth_of_length_le {w : List Sym} {e : Nat} (h : w.length ≤ e) :
    atDepth w e = (false, false) := by
  unfold atDepth
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none (by simpa using h)]
  rfl

/-- The two scan recurrences of a successful update, at every depth. `Z_depth` has them inside the
frontier; past it they read the scan's zero memory or white cells. -/
theorem Z_rec {w w2 : List Sym} {s : Bool} (h : Z w = some (w2, s)) (e : Nat) :
    atDepth w2 (e + 2) =
      (xor (atDepth w2 (e + 1)).1 ((atDepth w2 (e + 1)).2 || (atDepth w e).1),
       xor (atDepth w2 (e + 1)).2 ((atDepth w (e + 1)).1 || (atDepth w e).2)) := by
  obtain ⟨hlen, -, -, hin⟩ := Z_depth w w2 s h
  by_cases h1 : e + 1 < w.length
  · exact hin e h1
  by_cases h2 : e + 1 = w.length
  · obtain ⟨hw2, -, -⟩ := Z_spec w w2 s h
    cases w with
    | nil => simp at h2
    | cons x w' =>
      obtain ⟨a, b⟩ := x
      have he : e = w'.length := by simpa using h2
      have hhead : w2 = ((scanStep (false, false, false) (a, b)).1,
          (scanStep (false, false, false) (a, b)).2.1) ::
          ((scan (scanStep (false, false, false) (a, b)) w').1 ++ [(true, !s)]) := by
        rw [hw2, scan_cons]; rfl
      have hl : ((scan (scanStep (false, false, false) (a, b)) w').1 ++
          [((true, !s) : Sym)]).length = e + 1 := by
        simp [scan_length, he]
      rw [atDepth_of_length_le (w := w2) (e := e + 2) (by omega),
        atDepth_of_length_le (w := (a, b) :: w') (e := e + 1) (by simp; omega),
        atDepth_cons_eq' _ _ e he, hhead, atDepth_cons_eq' _ _ (e + 1) hl.symm]
      cases a <;> cases b <;> rfl
  · rw [atDepth_of_length_le (w := w2) (e := e + 2) (by omega),
      atDepth_of_length_le (w := w2) (e := e + 1) (by omega),
      atDepth_of_length_le (w := w) (e := e) (by omega),
      atDepth_of_length_le (w := w) (e := e + 1) (by omega)]
    rfl

/-! ### The chart -/

/-- The bit at time `τ` and depth `e + 1`. -/
def chart (fr : Nat → List Sym) (τ e : Nat) : Bool :=
  if (τ + e) % 2 = 0 then (atDepth (fr ((τ + e) / 2)) e).1
  else (atDepth (fr ((τ + e + 1) / 2)) e).2

theorem chart_hi (fr : Nat → List Sym) {τ e n : Nat} (h : τ + e = 2 * n) :
    chart fr τ e = (atDepth (fr n) e).1 := by
  have h1 : (τ + e) % 2 = 0 := by omega
  have h2 : (τ + e) / 2 = n := by omega
  simp [chart, h1, h2]

theorem chart_lo (fr : Nat → List Sym) {τ e n : Nat} (h : τ + e + 1 = 2 * n) :
    chart fr τ e = (atDepth (fr n) e).2 := by
  have h1 : ¬ (τ + e) % 2 = 0 := by omega
  have h2 : (τ + e + 1) / 2 = n := by omega
  simp [chart, h1, h2]

theorem even_or_odd (x : Nat) : ∃ n, x = 2 * n ∨ x = 2 * n + 1 := ⟨x / 2, by omega⟩

variable {fr : Nat → List Sym} {s : Nat → Bool}

/-- The Rule 30 recurrence at every cell of depth at least two. -/
theorem chart_interior (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (τ e : Nat) :
    chart fr (τ + 1) (e + 1) =
      xor (chart fr τ (e + 2)) (chart fr τ (e + 1) || chart fr τ e) := by
  rcases even_or_odd (τ + e) with ⟨n, hn | hn⟩
  · rw [chart_hi fr (n := n + 1) (by omega), chart_hi fr (n := n + 1) (by omega),
      chart_lo fr (n := n + 1) (by omega), chart_hi fr (n := n) hn, Z_rec (hZ n) e]
    cases (atDepth (fr (n + 1)) (e + 1)).1 <;> cases (atDepth (fr (n + 1)) (e + 1)).2 <;>
      cases (atDepth (fr n) e).1 <;> rfl
  · rw [chart_lo fr (n := n + 2) (by omega), chart_lo fr (n := n + 2) (by omega),
      chart_hi fr (n := n + 1) (by omega), chart_lo fr (n := n + 1) (by omega),
      Z_rec (hZ (n + 1)) e]
    cases (atDepth (fr (n + 2)) (e + 1)).2 <;> cases (atDepth (fr (n + 1)) (e + 1)).1 <;>
      cases (atDepth (fr (n + 1)) e).2 <;> rfl

theorem fr_ne_nil (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    ∀ n, fr n ≠ []
  | 0 => h0
  | n + 1 => by
    intro h
    have hl := (Z_depth _ _ _ (hZ n)).1
    rw [h] at hl
    simp at hl

/-- The rule at depth one, with a white wall, from time one on. -/
theorem chart_wall (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) (τ : Nat)
    (hτ : 1 ≤ τ) :
    chart fr (τ + 1) 0 = xor (chart fr τ 1) (chart fr τ 0 || false) := by
  have hne := fr_ne_nil hZ h0
  rcases even_or_odd τ with ⟨n, hn | hn⟩
  · obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    have t0 := (Z_depth _ _ _ (hZ (m + 1))).2.1
    have t1 := (Z_depth _ _ _ (hZ (m + 1))).2.2.1 (hne (m + 1))
    have b0 := (Z_depth _ _ _ (hZ m)).2.1
    rw [chart_lo fr (n := m + 2) (by omega), chart_lo fr (n := m + 2) (by omega),
      chart_hi fr (n := m + 1) (by omega), t0, t1, b0]
    cases s (m + 1) <;> rfl
  · have t0 := (Z_depth _ _ _ (hZ n)).2.1
    have t1 := (Z_depth _ _ _ (hZ n)).2.2.1 (hne n)
    rw [chart_hi fr (n := n + 1) (by omega), chart_hi fr (n := n + 1) (by omega),
      chart_lo fr (n := n + 1) (by omega), t0, t1]
    cases s n <;> rfl

/-- The row at time two, read at depths from one. -/
def start (fr : Nat → List Sym) (k : Nat) : Bool := chart fr 2 (k - 1)

/-- The chart from time two is the zero-boundary evolution of `start`. -/
theorem zrow_chart (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    ∀ t e, Rule30ZeroBoundary.zrow (start fr) t (e + 1) = chart fr (t + 2) e := by
  intro t
  induction t with
  | zero => intro e; rfl
  | succ t ih =>
    intro e
    cases e with
    | zero =>
      show xor (Rule30ZeroBoundary.zrow (start fr) t 2)
        (Rule30ZeroBoundary.zrow (start fr) t 1 || Rule30ZeroBoundary.zrow (start fr) t 0) = _
      rw [ih 1, ih 0, Rule30ZeroBoundary.zrow_wall, show t + 1 + 2 = (t + 2) + 1 by omega,
        chart_wall hZ h0 (t + 2) (by omega)]
    | succ e =>
      show xor (Rule30ZeroBoundary.zrow (start fr) t (e + 3))
        (Rule30ZeroBoundary.zrow (start fr) t (e + 2) ||
          Rule30ZeroBoundary.zrow (start fr) t (e + 1)) = _
      rw [ih (e + 2), ih (e + 1), ih e, show t + 1 + 2 = (t + 2) + 1 by omega,
        chart_interior hZ (t + 2) e]

theorem inX_start (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    Rule30ZeroBoundary.InX (start fr) := by
  intro k
  rw [zrow_chart hZ h0 (2 * k) 0, chart_hi fr (n := k + 1) (by omega),
    (Z_depth _ _ _ (hZ k)).2.1]

theorem fr_length (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) :
    ∀ n, (fr n).length = (fr 0).length + n
  | 0 => rfl
  | n + 1 => by rw [(Z_depth _ _ _ (hZ n)).1, fr_length hZ n]; omega

theorem finSupp_start (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) :
    Rule30ZeroBoundary.FinSupp (start fr) := by
  refine ⟨2 * (fr 0).length + 6, fun k hk => ?_⟩
  obtain ⟨e, rfl⟩ : ∃ e, k = e + 1 := ⟨k - 1, by omega⟩
  show chart fr 2 e = false
  rcases even_or_odd e with ⟨m, hm | hm⟩
  · rw [chart_hi fr (n := m + 1) (by omega),
      atDepth_of_length_le (by rw [fr_length hZ]; omega)]
  · rw [chart_lo fr (n := m + 2) (by omega),
      atDepth_of_length_le (by rw [fr_length hZ]; omega)]

/-! ### The frontiers of an immortal run -/

/-- The `n`-th frontier of a run. -/
def frontier (w : List Sym) (n : Nat) : List Sym :=
  match run w n with
  | some p => p.1
  | none => []

theorem frontier_of_run {w w' : List Sym} {n : Nat} {t : List Bool}
    (h : run w n = some (w', t)) : frontier w n = w' := by
  unfold frontier
  rw [h]

theorem frontier_step {w : List Sym} (hI : ∀ n, run w n ≠ none) (n : Nat) :
    ∃ c, Z (frontier w n) = some (frontier w (n + 1), c) := by
  cases hr : run w n with
  | none => exact absurd hr (hI n)
  | some p =>
    obtain ⟨w', t⟩ := p
    have hn := hI (n + 1)
    cases hz : Z w' with
    | none =>
      exact absurd (by simp [run, hr, hz]) hn
    | some q =>
      obtain ⟨w'', c⟩ := q
      have hr2 : run w (n + 1) = some (w'', t ++ [c]) := by simp [run, hr, hz]
      exact ⟨c, by rw [frontier_of_run hr, frontier_of_run hr2, hz]⟩

/-! ### The equivalences -/

/-- **`Q01` implies mortality.** An immortal legal frontier would give a finitely supported start
of the zero-boundary left half with column `-1` black at every even step. -/
theorem mortality_of_Q01 (hQ : Rule30ZeroBoundary.Q01) : Rule30SurvivalBridge.Mortality := by
  intro w hw
  refine Classical.byContradiction fun hne => ?_
  have hI : ∀ n, run w n ≠ none := fun n h => hne ⟨n, h⟩
  have hs : ∀ n, Z (frontier w n) =
      some (frontier w (n + 1), Classical.choose (frontier_step hI n)) :=
    fun n => Classical.choose_spec (frontier_step hI n)
  have h0 : frontier w 0 ≠ [] := by
    rw [frontier_of_run (w' := w) (t := []) rfl]
    intro h
    subst h
    exact hw
  exact hQ _ (finSupp_start hs) (inX_start hs h0)

/-- **Mortality is `Q01`.** -/
theorem mortality_iff_Q01 : Rule30SurvivalBridge.Mortality ↔ Rule30ZeroBoundary.Q01 := by
  refine ⟨fun hM => ?_, mortality_of_Q01⟩
  exact Rule30ZeroBoundary.Q01_iff_staged.mpr
    (Rule30AlternatingTraceBridge.Q01_of_mortality
      (Rule30AlternatingTraceBridge.mortality_iff_survival.mpr hM))

/-- **A repeat budget at every length is `Q01`.** -/
theorem budget_iff_Q01 :
    (∀ r : Nat, Rule30SurvivalBridge.BudgetAt r) ↔ Rule30ZeroBoundary.Q01 :=
  Rule30SurvivalBridge.budget_iff_mortality.trans mortality_iff_Q01

end Rule30FrontierChart
end Ruliology.CellularAutomata
