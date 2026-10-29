import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.NormCast
import Rule30Equivalents.Lagrange
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Algebra.Order.Floor.Ring
import Ruliology.CellularAutomata.Rule30FiniteMaskedJen
import Ruliology.CellularAutomata.Rule30WhiteEnd
import Ruliology.CellularAutomata.Rule30FiniteConfigs

/-!
# An explicit finite horizon for mechanical words, and matching pieces beside a Rule 30 clock

Classical Sturmian repetition theory already gives the qualitative obstruction: every Sturmian word repeats a long
factor early, uniformly over slope and phase. This file formalizes a uniform EXPLICIT finite witness, keeps its loss
under arbitrary finite block maps, and transfers it to matching pieces beside a Rule 30 period-two clock.

* `UniformHorizon.uniform_horizon`: for every irrational slope `α`, every phase `θ` and every `C`, the mechanical word
  `⌊θ+(s+1)α⌋ − ⌊θ+sα⌋` has a repetition of positive lag `q` on `[a, b]` with `b+q ≤ 251*(C+4)` and `b > 2a+q+C`.
* `RecodedHorizon.uniform_horizon_all` and `recoded_horizon`: the same for every real slope, and for every recoding of
  width `w+1` (any block map, any codomain) through `251*(C+4)+250*w`.
* `PhysicalHorizon.piece_bound`, `reset_step`, `first_disagreement`, `disagreement_step`: for a configuration white left
  of `-L` whose column `0` is a clock from time `0`, any stretch `[a, b]` of the visible column `evol x (2s) 1` agreeing
  with a recoded mechanical word has `b − a < 251*(L+2a+4)+250*w`; consecutive reset times satisfy
  `t' ≤ 503t+251L+1004+250w`, and disagreements with one fixed recoded word satisfy `k_0 ≤ 251(L+4)+250w` and
  `k' ≤ 503k+251L+1507+250w`.

The constants are explicit, not claimed sharp. The continued-fraction and repetition background is credited: the
best-approximation step is classical, Bugeaud–Kim (Trans. AMS 371, 2019) and Bugeaud–Laurent (AIF 73, 2023) contain
finite and qualitative repetition estimates, and the width transfer is an elementary block argument. The additional
content is the checked quantitative bound and its physical endpoint accounting. These are conditional statements about
a genuine clock; they do not construct one, and give no density, entropy, realizability or prize conclusion. The arc
components are those of the delivered arc package; the physical repeat bound is its `ArcRule30Bridge.repeat_bound`.
-/

namespace Rule30Submission

/- Component: ArcBreakBounds; proof body retained from the release-checked integration. -/
namespace ArcBreakBounds

theorem nodup_map_of_inj {α β : Type} (f : α → β) : ∀ {l : List α}, l.Nodup →
    (∀ a ∈ l, ∀ b ∈ l, f a = f b → a = b) → (l.map f).Nodup
  | [], _, _ => List.nodup_nil
  | a :: l, hl, hinj => by
    rw [List.nodup_cons] at hl
    rw [List.map_cons, List.nodup_cons]
    refine ⟨?_, nodup_map_of_inj f hl.2 fun x hx y hy =>
      hinj x (by simp [hx]) y (by simp [hy])⟩
    intro hm
    obtain ⟨b, hb, hfb⟩ := List.mem_map.1 hm
    exact hl.1 (hinj a (by simp) b (by simp [hb]) hfb.symm ▸ hb)

/-- Among r+1 labels taking values below r, two agree. -/
theorem label_collision (r : Nat) (label : Nat → Nat) (hlabel : ∀ k, k ≤ r → label k < r) :
    ∃ i j, i < j ∧ j ≤ r ∧ label i = label j := by
  refine Classical.byContradiction fun hne => ?_
  have hinj : ∀ i ∈ List.range (r+1), ∀ j ∈ List.range (r+1), label i = label j → i = j := by
    intro i hi j hj he
    simp only [List.mem_range] at hi hj
    rcases Nat.lt_trichotomy i j with h | h | h
    · exact absurd ⟨i,j,h,by omega,he⟩ hne
    · exact h
    · exact absurd ⟨j,i,h,by omega,he.symm⟩ hne
  have hnd := nodup_map_of_inj label List.nodup_range hinj
  have hlen := hnd.length_le_of_subset (l₂ := List.range r) (by
    intro x hx
    obtain ⟨k,hk,rfl⟩ := List.mem_map.1 hx
    apply List.mem_range.2
    have hklt : k < r+1 := List.mem_range.1 hk
    exact hlabel k (by omega))
  simp only [List.length_map,List.length_range] at hlen
  omega

/-- The transformed recurrence has an exact power-of-two envelope. Index0 is the first break. -/
theorem break_envelope (q C : Nat) (d : Nat → Nat)
    (hfirst : d 0 ≤ q+C+1) (hnext : ∀ k, d (k+1) ≤ 2*d k+q+C+3) :
    ∀ k, d k+(q+C+2)+1 ≤ 2^(k+1)*(q+C+2) := by
  intro k
  induction k with
  | zero => simp only [Nat.zero_add,Nat.pow_one]; omega
  | succ k ih =>
    have hn := hnext k
    have he : 2^(k+1+1)*(q+C+2) = 2*(2^(k+1)*(q+C+2)) := by
      rw [Nat.pow_succ,Nat.mul_assoc,Nat.mul_left_comm]
    rw [show k+1+1 = (k+1)+1 by omega,he]
    omega

/-- Same-label spacing cannot exceed the finite-colour break envelope. -/
theorem spacing_bound (q C r spacing : Nat) (d label : Nat → Nat)
    (hfirst : d 0 ≤ q+C+1) (hnext : ∀ k, d (k+1) ≤ 2*d k+q+C+3)
    (hlabel : ∀ k, k ≤ r → label k < r)
    (hspacing : ∀ i j, i < j → j ≤ r → label i = label j → spacing ≤ d j-d i) :
    spacing < 2^(r+1)*(q+C+2) := by
  obtain ⟨i,j,hij,hjr,he⟩ := label_collision r label hlabel
  have hs := hspacing i j hij hjr he
  have hj := break_envelope q C d hfirst hnext j
  have hp : 2^(j+1) ≤ 2^(r+1) := Nat.pow_le_pow_right (by decide) (by omega)
  have hm := Nat.mul_le_mul_right (q+C+2) hp
  omega

/-- A growing previous denominator pays the fixed break-window margin at the original digit threshold. -/
theorem next_denominator_covers_window (K q C previous digit next : Nat)
    (hdigit : K < digit) (hprevious : K*(C+2) ≤ previous)
    (hnext : next = digit*q+previous) : K*(q+C+2)+q ≤ next := by
  have hd : K+1 ≤ digit := by omega
  have hm := Nat.mul_le_mul_right q hd
  simp only [Nat.add_mul,Nat.one_mul] at hm
  rw [show q+C+2 = q+(C+2) by omega,Nat.mul_add,hnext]
  omega

end ArcBreakBounds

/- Component: ArcBreakSequence; proof body retained from the release-checked integration. -/
namespace ArcBreakSequence

/-- A matching window from a to b must end by 2a+q+C. -/
def RepeatBound (c : Nat → Bool) (q C : Nat) : Prop :=
  ∀ a b, a ≤ b → (∀ s, a ≤ s → s ≤ b → c (s+q) = c s) → b ≤ 2*a+q+C

/-- There is a genuine break in every explicitly bounded forward window. -/
theorem future_break (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) :
    ∃ m, a ≤ m ∧ m ≤ 2*a+q+C+1 ∧ c (m+q) ≠ c m := by
  refine Classical.byContradiction fun hno => ?_
  have heq : ∀ s, a ≤ s → s ≤ 2*a+q+C+1 → c (s+q) = c s := by
    intro s hs ht
    by_cases h : c (s+q) = c s
    · exact h
    · exact False.elim (hno ⟨s,hs,ht,h⟩)
  have h := hr a (2*a+q+C+1) (by omega) heq
  omega

noncomputable def nextBreak (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) : Nat :=
  Classical.choose (future_break c q C hr a)

theorem nextBreak_spec (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) :
    a ≤ nextBreak c q C hr a ∧ nextBreak c q C hr a ≤ 2*a+q+C+1 ∧
      c (nextBreak c q C hr a+q) ≠ c (nextBreak c q C hr a) :=
  Classical.choose_spec (future_break c q C hr a)

noncomputable def sequence (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) : Nat → Nat
  | 0 => nextBreak c q C hr 0
  | k+1 => nextBreak c q C hr (sequence c q C hr k+1)

theorem sequence_break (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    c (sequence c q C hr k+q) ≠ c (sequence c q C hr k) := by
  cases k with
  | zero => exact (nextBreak_spec c q C hr 0).2.2
  | succ k => exact (nextBreak_spec c q C hr (sequence c q C hr k+1)).2.2

theorem sequence_increasing (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    sequence c q C hr k < sequence c q C hr (k+1) := by
  change sequence c q C hr k < nextBreak c q C hr (sequence c q C hr k+1)
  have h := (nextBreak_spec c q C hr (sequence c q C hr k+1)).1
  omega

theorem sequence_strict (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C)
    {i j : Nat} (hij : i < j) : sequence c q C hr i < sequence c q C hr j := by
  obtain ⟨n,rfl⟩ := Nat.exists_eq_add_of_le (Nat.succ_le_of_lt hij)
  induction n with
  | zero => simpa using sequence_increasing c q C hr i
  | succ n ih => exact Nat.lt_trans (ih (by omega)) (sequence_increasing c q C hr (i+1+n))

theorem sequence_first (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) :
    sequence c q C hr 0 ≤ q+C+1 := by
  simpa [sequence] using (nextBreak_spec c q C hr 0).2.1

theorem sequence_step_bound (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    sequence c q C hr (k+1) ≤ 2*sequence c q C hr k+q+C+3 := by
  change nextBreak c q C hr (sequence c q C hr k+1) ≤ _
  have h := (nextBreak_spec c q C hr (sequence c q C hr k+1)).2.1
  omega

/-- Every genuine break belongs to one of r labels, with a lower bound on same-label gaps. -/
def LabelSpacing (c : Nat → Bool) (q r spacing : Nat) : Prop :=
  ∃ colour : Nat → Nat,
    (∀ s, c (s+q) ≠ c s → colour s < r) ∧
    (∀ s t, s < t → c (s+q) ≠ c s → c (t+q) ≠ c t →
      colour s = colour t → spacing ≤ t-s)

/-- The physical repeat obstruction and labelled break spacing imply the numerical arc bound. -/
theorem labelled_spacing_bound (c : Nat → Bool) (q C r spacing : Nat)
    (hr : RepeatBound c q C) (hl : LabelSpacing c q r spacing) :
    spacing < 2^(r+1)*(q+C+2) := by
  obtain ⟨colour,hcolour,hgap⟩ := hl
  apply ArcBreakBounds.spacing_bound q C r spacing (sequence c q C hr)
    (fun k => colour (sequence c q C hr k))
    (sequence_first c q C hr) (sequence_step_bound c q C hr)
  · intro k _
    exact hcolour _ (sequence_break c q C hr k)
  · intro i j hij _ he
    exact hgap _ _ (sequence_strict c q C hr hij)
      (sequence_break c q C hr i) (sequence_break c q C hr j) he

end ArcBreakSequence

/- Component: ArcDeterminantDraft; proof body retained from the release-checked integration. -/
namespace ArcDeterminant

/-- The unit determinant of consecutive continuants gives an explicit Bezout identity. -/
theorem bezout_of_unit_determinant (p q previousP previousQ sign : ℤ)
    (hsign : sign*sign = 1) (hdet : p*previousQ-previousP*q = sign) :
    (sign*previousQ)*p+(-sign*previousP)*q = 1 := by
  calc
    (sign*previousQ)*p+(-sign*previousP)*q = sign*(p*previousQ-previousP*q) := by ring
    _ = 1 := by rw [hdet]; exact hsign

/-- A return closer than the error of a reduced approximation must have `(m+q)*error > 1`. -/
theorem spacing_of_bezout (alpha : ℝ) (p q m a u v : ℤ)
    (hq : 0 < q) (hm : 0 < m) (hbezout : u*p+v*q = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hclose : |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p|) :
    1 < ((m : ℝ)+q)*|(q : ℝ)*alpha-p| := by
  by_contra hnot
  have hupper : ((m : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1 := le_of_not_gt hnot
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm
  let D : ℤ := q*a-m*p
  have hDsmall : |(D : ℝ)| < 1 := by
    calc
      |(D : ℝ)| = |(m : ℝ)*((q : ℝ)*alpha-p)-(q : ℝ)*((m : ℝ)*alpha-a)| := by
        dsimp [D]
        push_cast
        congr 1
        ring
      _ ≤ |(m : ℝ)*((q : ℝ)*alpha-p)|+|(q : ℝ)*((m : ℝ)*alpha-a)| := abs_sub _ _
      _ = (m : ℝ)*|(q : ℝ)*alpha-p|+(q : ℝ)*|(m : ℝ)*alpha-a| := by
        rw [abs_mul,abs_mul,abs_of_pos hmR,abs_of_pos hqR]
      _ < ((m : ℝ)+q)*|(q : ℝ)*alpha-p| := by
        have h := mul_lt_mul_of_pos_left hclose hqR
        nlinarith
      _ ≤ 1 := hupper
  have hDint : |D| < 1 := by exact_mod_cast hDsmall
  have hDzero : D = 0 := by
    have h := abs_lt.mp hDint
    omega
  let k : ℤ := u*a+v*m
  have hmk : m = q*k := by
    dsimp [k,D] at *
    linear_combination (-m) * hbezout - u * hDzero
  have hak : a = p*k := by
    dsimp [k,D] at *
    linear_combination (-a) * hbezout + v * hDzero
  have hkpos : 0 < k := by
    by_contra hh
    have hkle : k ≤ 0 := le_of_not_gt hh
    have hprod : q*k ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hq.le hkle
    rw [← hmk] at hprod
    omega
  have hkone : (1 : ℝ) ≤ k := by exact_mod_cast (show 1 ≤ k by omega)
  have herror : |(m : ℝ)*alpha-a| = (k : ℝ)*|(q : ℝ)*alpha-p| := by
    calc
      |(m : ℝ)*alpha-a| = |(k : ℝ)*((q : ℝ)*alpha-p)| := by
        rw [hmk,hak]
        push_cast
        congr 1
        ring
      _ = (k : ℝ)*|(q : ℝ)*alpha-p| := by
        rw [abs_mul,abs_of_pos (by exact_mod_cast hkpos)]
  rw [herror] at hclose
  nlinarith

/-- One-scale contradiction in the form used after finite-colour break counting. -/
theorem no_short_return (alpha : ℝ) (p q m a u v : ℤ) (B : ℝ)
    (hq : 0 < q) (hm : 0 < m) (hbezout : u*p+v*q = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) (hmB : (m : ℝ) < B)
    (hscale : (B+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p| := by
  intro hclose
  have h := spacing_of_bezout alpha p q m a u v hq hm hbezout hepsilon hclose
  have hlt := mul_lt_mul_of_pos_right (add_lt_add_right hmB (q : ℝ)) hepsilon
  linarith

end ArcDeterminant

/- Component: ArcContinuantsDraft; proof body retained from the release-checked integration. -/
namespace ArcDeterminant

/-- The kit's consecutive continuants give the concrete coefficients for `spacing_of_bezout`. -/
theorem continuant_bezout (alpha : ℝ) (n : ℕ) :
    let sign : ℤ := (-1)^(n+1)
    let previousP := Rule30Equivalents.Lagrange.contP (Rule30Equivalents.Lagrange.digit alpha) (n+1)
    let previousQ := Rule30Equivalents.Lagrange.contQ (Rule30Equivalents.Lagrange.digit alpha) (n+1)
    let p := Rule30Equivalents.Lagrange.contP (Rule30Equivalents.Lagrange.digit alpha) (n+2)
    let q := Rule30Equivalents.Lagrange.contQ (Rule30Equivalents.Lagrange.digit alpha) (n+2)
    (sign*previousQ)*p+(-sign*previousP)*q = 1 := by
  dsimp only
  apply bezout_of_unit_determinant
  · rw [← mul_pow]
    norm_num
  · simpa [Nat.add_assoc] using
      Rule30Equivalents.Lagrange.cont_det (Rule30Equivalents.Lagrange.digit alpha) (n+1)

/-- The kit's exact error identity implies the strict next-denominator approximation bound. -/
theorem continuant_error_lt_next {alpha : ℝ} (halpha : Irrational alpha) (n : ℕ) :
    let a := Rule30Equivalents.Lagrange.digit alpha
    0 < |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-Rule30Equivalents.Lagrange.contP a (n+2)| ∧
    |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-Rule30Equivalents.Lagrange.contP a (n+2)| <
      1/(Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) := by
  dsimp only
  let a := Rule30Equivalents.Lagrange.digit alpha
  have ha : ∀ k, 1 ≤ a (k+1) := Rule30Equivalents.Lagrange.one_le_digit halpha
  have hqone : (1 : ℝ) ≤ Rule30Equivalents.Lagrange.contQ a (n+2) := by
    exact_mod_cast Rule30Equivalents.Lagrange.one_le_contQ ha n
  have hnxtone : (1 : ℝ) ≤ Rule30Equivalents.Lagrange.contQ a (n+3) := by
    exact_mod_cast Rule30Equivalents.Lagrange.one_le_contQ ha (n+1)
  have hqpos : (0 : ℝ) < Rule30Equivalents.Lagrange.contQ a (n+2) := by linarith
  have hnxtpos : (0 : ℝ) < Rule30Equivalents.Lagrange.contQ a (n+3) := by linarith
  have htailpos : 0 < (Rule30Equivalents.Lagrange.cq alpha (n+2))⁻¹ := by
    apply inv_pos.2
    have h := Rule30Equivalents.Lagrange.one_lt_cq halpha (n+1)
    linarith
  have hquot : (a (n+1) : ℝ) < Rule30Equivalents.Lagrange.cq alpha (n+1) := by
    have h := Rule30Equivalents.Lagrange.cq_eq_digit_add alpha (n+1)
    change Rule30Equivalents.Lagrange.cq alpha (n+1) =
      (a (n+1) : ℝ)+(Rule30Equivalents.Lagrange.cq alpha (n+2))⁻¹ at h
    linarith
  have hnxt : (Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) =
      (a (n+1) : ℝ)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := by
    rw [show n+3 = (n+1)+2 by omega, Rule30Equivalents.Lagrange.contQ]
    push_cast
    rfl
  have hden : (Rule30Equivalents.Lagrange.contQ a (n+3) : ℝ) <
      Rule30Equivalents.Lagrange.cq alpha (n+1)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := by
    have h := mul_pos (sub_pos.2 hquot) hqpos
    rw [hnxt]
    nlinarith
  have hdenpos : (0 : ℝ) <
      Rule30Equivalents.Lagrange.cq alpha (n+1)*Rule30Equivalents.Lagrange.contQ a (n+2)+
        Rule30Equivalents.Lagrange.contQ a (n+1) := lt_trans hnxtpos hden
  have he := congrArg abs (Rule30Equivalents.Lagrange.error_mul halpha n)
  rw [abs_mul,abs_pow,abs_neg,abs_one,one_pow,abs_of_pos hdenpos] at he
  have hepos : 0 < |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2)| := by
    have hn := abs_nonneg (alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2))
    by_contra hnot
    have hzero := le_antisymm (le_of_not_gt hnot) hn
    change |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
      Rule30Equivalents.Lagrange.contP a (n+2)| * _ = 1 at he
    rw [hzero,zero_mul] at he
    norm_num at he
  refine ⟨hepos, (lt_div_iff₀ hnxtpos).2 ?_⟩
  have hprod := mul_lt_mul_of_pos_left hden hepos
  change |alpha*(Rule30Equivalents.Lagrange.contQ a (n+2) : ℝ)-
    Rule30Equivalents.Lagrange.contP a (n+2)| * _ = 1 at he
  linarith

end ArcDeterminant

/- Component: ArcCoverDraft; proof body retained from the release-checked integration. -/
namespace ArcCover

/-- Two orbit lifts in one half-open interval give a strictly close integer return. -/
theorem same_interval_return (alpha theta epsilon endpoint : ℝ) (s t : Nat) (zs zt : ℤ)
    (hst : s < t)
    (hslo : endpoint ≤ theta+(s : ℝ)*alpha-zs)
    (hshi : theta+(s : ℝ)*alpha-zs < endpoint+epsilon)
    (htlo : endpoint ≤ theta+(t : ℝ)*alpha-zt)
    (hthi : theta+(t : ℝ)*alpha-zt < endpoint+epsilon) :
    |((t-s : Nat) : ℝ)*alpha-((zt-zs : ℤ) : ℝ)| < epsilon := by
  have hd : ((t-s : Nat) : ℝ)*alpha-((zt-zs : ℤ) : ℝ) =
      (theta+(t : ℝ)*alpha-zt)-(theta+(s : ℝ)*alpha-zs) := by
    rw [Nat.cast_sub (Nat.le_of_lt hst)]
    push_cast
    ring
  rw [hd]
  exact abs_lt.2 ⟨by linarith, by linarith⟩

/-- A finite cover labels actual mismatches by half-open intervals and integer orbit lifts. -/
def LiftCover (c : Nat → Bool) (q r : Nat) (alpha theta epsilon : ℝ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ) : Prop :=
  ∀ s, c (s+q) ≠ c s → label s < r ∧
    endpoint (label s) ≤ theta+(s : ℝ)*alpha-lift s ∧
    theta+(s : ℝ)*alpha-lift s < endpoint (label s)+epsilon

/-- RepeatBound and the lifted cover produce a positive short return below the counting envelope. -/
theorem short_return (c : Nat → Bool) (q C r : Nat) (alpha theta epsilon : ℝ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ)
    (hr : ArcBreakSequence.RepeatBound c q C)
    (hc : LiftCover c q r alpha theta epsilon endpoint label lift) :
    ∃ m : Nat, ∃ a : ℤ, 0 < m ∧ m < 2^(r+1)*(q+C+2) ∧
      |(m : ℝ)*alpha-a| < epsilon := by
  let d := ArcBreakSequence.sequence c q C hr
  have hb (k : Nat) : c (d k+q) ≠ c (d k) := ArcBreakSequence.sequence_break c q C hr k
  have hl (k : Nat) (_ : k ≤ r) : label (d k) < r := (hc (d k) (hb k)).1
  obtain ⟨i,j,hij,hjr,he⟩ := ArcBreakBounds.label_collision r (fun k => label (d k)) hl
  have hdlt : d i < d j := ArcBreakSequence.sequence_strict c q C hr hij
  have henv := ArcBreakBounds.break_envelope q C d
    (ArcBreakSequence.sequence_first c q C hr)
    (ArcBreakSequence.sequence_step_bound c q C hr) j
  have hp : 2^(j+1) ≤ 2^(r+1) := Nat.pow_le_pow_right (by decide) (by omega)
  have hm := Nat.mul_le_mul_right (q+C+2) hp
  have hbound : d j-d i < 2^(r+1)*(q+C+2) := by omega
  have hs := hc (d i) (hb i)
  have ht := hc (d j) (hb j)
  rw [← he] at ht
  refine ⟨d j-d i,lift (d j)-lift (d i),by omega,hbound,?_⟩
  exact same_interval_return alpha theta epsilon (endpoint (label (d i)))
    (d i) (d j) (lift (d i)) (lift (d j)) hdlt hs.2.1 hs.2.2 ht.2.1 ht.2.2

/-- Conditional one-scale exclusion, retaining every geometric and approximation premise. -/
theorem no_repeat_of_cover (c : Nat → Bool) (q C r : Nat) (alpha theta : ℝ) (p u v : ℤ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ)
    (hq : 0 < q) (hbezout : u*p+v*(q : ℤ) = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hc : LiftCover c q r alpha theta |(q : ℝ)*alpha-p| endpoint label lift)
    (hscale : (((2^(r+1)*(q+C+2) : Nat) : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ ArcBreakSequence.RepeatBound c q C := by
  intro hr
  obtain ⟨m,a,hm,hmB,hclose⟩ := short_return c q C r alpha theta _ endpoint label lift hr hc
  apply ArcDeterminant.no_short_return alpha p (q : ℤ) (m : ℤ) a u v
    ((2^(r+1)*(q+C+2) : Nat) : ℝ)
    (by exact_mod_cast hq) (by exact_mod_cast hm) hbezout
    (by simpa using hepsilon) (by exact_mod_cast hmB) (by simpa using hscale)
  simpa using hclose

end ArcCover

/- Component: ArcStepCodeDraft; proof body retained from the release-checked integration. -/
namespace ArcStepCode

/-- Right-continuous finite-step constancy, with possible jump locations given modulo integers.
Endpoints may be redundant or repeated; r counts the supplied labels. -/
structure StepCode (r : Nat) where
  value : ℝ → Bool
  endpoint : Nat → ℝ
  periodic : ∀ x : ℝ, ∀ z : ℤ, value (x+z) = value x
  constant_between : ∀ x y : ℝ, x ≤ y →
    (∀ i : Nat, i < r → ∀ z : ℤ, ¬ (x < endpoint i+z ∧ endpoint i+z ≤ y)) → value x = value y

def orbit {r : Nat} (S : StepCode r) (alpha theta : ℝ) (s : Nat) : Bool :=
  S.value (theta+(s : ℝ)*alpha)

/-- A change of colour crosses a possible jump, including its upper endpoint but excluding its lower one. -/
theorem crossing {r : Nat} (S : StepCode r) (x y : ℝ) (hxy : x ≤ y)
    (hne : S.value x ≠ S.value y) :
    ∃ i : Nat, i < r ∧ ∃ z : ℤ, x < S.endpoint i+z ∧ S.endpoint i+z ≤ y := by
  refine Classical.byContradiction fun hno => ?_
  apply hne
  apply S.constant_between x y hxy
  intro i hi z hz
  exact hno ⟨i,hi,z,hz⟩

/-- A genuine orbit mismatch has a label and an integer lift inside one common signed-displacement interval. -/
theorem break_has_lift {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q : Nat) (p : ℤ)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) (s : Nat)
    (hb : orbit S alpha theta (s+q) ≠ orbit S alpha theta s) :
    ∃ i : Nat, i < r ∧ ∃ z : ℤ,
      S.endpoint i-max ((q : ℝ)*alpha-p) 0 ≤ theta+(s : ℝ)*alpha-z ∧
      theta+(s : ℝ)*alpha-z < S.endpoint i-max ((q : ℝ)*alpha-p) 0+|(q : ℝ)*alpha-p| := by
  let x := theta+(s : ℝ)*alpha
  let delta := (q : ℝ)*alpha-p
  have hshift : S.value (x+delta) = S.value (theta+((s+q : Nat) : ℝ)*alpha) := by
    calc
      S.value (x+delta) = S.value ((x+delta)+(p : ℝ)) := (S.periodic (x+delta) p).symm
      _ = S.value (theta+((s+q : Nat) : ℝ)*alpha) := by
        congr 1
        dsimp [x,delta]
        push_cast
        ring
  have hmis : S.value x ≠ S.value (x+delta) := by
    intro h
    apply hb
    change S.value (theta+((s+q : Nat) : ℝ)*alpha) = S.value x
    rw [← hshift]
    exact h.symm
  change 0 < |delta| at hepsilon
  change ∃ i : Nat, i < r ∧ ∃ z : ℤ,
    S.endpoint i-max delta 0 ≤ x-z ∧ x-z < S.endpoint i-max delta 0+|delta|
  by_cases hd : 0 < delta
  · obtain ⟨i,hi,z,hlo,hhi⟩ := crossing S x (x+delta) (by linarith) hmis
    refine ⟨i,hi,z,?_,?_⟩
    · rw [max_eq_left hd.le]
      linarith
    · rw [max_eq_left hd.le,abs_of_pos hd]
      linarith
  · have hdle : delta ≤ 0 := le_of_not_gt hd
    have ha : |delta| = -delta := abs_of_nonpos hdle
    have hdneg : delta < 0 := by rw [ha] at hepsilon; linarith
    obtain ⟨i,hi,z,hlo,hhi⟩ := crossing S (x+delta) x (by linarith) (Ne.symm hmis)
    refine ⟨i,hi,z,?_,?_⟩
    · rw [max_eq_right hdle]
      linarith
    · rw [max_eq_right hdle,ha]
      linarith

/-- Classical labels/lifts are chosen only for genuine breaks; nonbreaks receive unused defaults. -/
theorem lift_cover {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q : Nat) (p : ℤ)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) :
    ∃ label : Nat → Nat, ∃ lift : Nat → ℤ,
      ArcCover.LiftCover (orbit S alpha theta) q r alpha theta |(q : ℝ)*alpha-p|
        (fun i => S.endpoint i-max ((q : ℝ)*alpha-p) 0) label lift := by
  have hw : ∀ s : Nat, ∃ i : Nat, ∃ z : ℤ,
      orbit S alpha theta (s+q) ≠ orbit S alpha theta s →
      i < r ∧ S.endpoint i-max ((q : ℝ)*alpha-p) 0 ≤ theta+(s : ℝ)*alpha-z ∧
        theta+(s : ℝ)*alpha-z < S.endpoint i-max ((q : ℝ)*alpha-p) 0+|(q : ℝ)*alpha-p| := by
    intro s
    by_cases hb : orbit S alpha theta (s+q) ≠ orbit S alpha theta s
    · obtain ⟨i,hi,z,hlo,hhi⟩ := break_has_lift S alpha theta q p hepsilon s hb
      exact ⟨i,z,fun _ => ⟨hi,hlo,hhi⟩⟩
    · exact ⟨0,0,fun h => False.elim (hb h)⟩
  let label : Nat → Nat := fun s => Classical.choose (hw s)
  let lift : Nat → ℤ := fun s => Classical.choose (Classical.choose_spec (hw s))
  refine ⟨label,lift,?_⟩
  intro s hb
  exact (Classical.choose_spec (Classical.choose_spec (hw s))) hb

/-- The one-scale exclusion now needs the explicit finite-step interface, not an assumed mismatch cover. -/
theorem no_repeat_bound {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q C : Nat) (p u v : ℤ)
    (hq : 0 < q) (hbezout : u*p+v*(q : ℤ) = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hscale : (((2^(r+1)*(q+C+2) : Nat) : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ ArcBreakSequence.RepeatBound (orbit S alpha theta) q C := by
  obtain ⟨label,lift,hc⟩ := lift_cover S alpha theta q p hepsilon
  exact ArcCover.no_repeat_of_cover (orbit S alpha theta) q C r alpha theta p u v
    (fun i => S.endpoint i-max ((q : ℝ)*alpha-p) 0) label lift hq hbezout hepsilon hc hscale

end ArcStepCode

/- Component: ArcRotationDraft; proof body retained from the release-checked integration. -/
namespace ArcRotation

open Rule30Equivalents.Lagrange

/-- Natural form of the actual denominator continuant; positivity below requires irrational input. -/
noncomputable def denominator (alpha : ℝ) (n : Nat) : Nat := (contQ (digit alpha) (n+2)).toNat

theorem denominator_cast {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    (denominator alpha n : ℤ) = contQ (digit alpha) (n+2) := by
  exact Int.toNat_of_nonneg (contQ_nonneg (fun k => one_le_digit ha k) (n+2))

theorem denominator_real {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    (denominator alpha n : ℝ) = (contQ (digit alpha) (n+2) : ℝ) := by
  exact_mod_cast denominator_cast ha n

theorem denominator_pos {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    0 < denominator alpha n := by
  have h : (1 : ℤ) ≤ (denominator alpha n : ℤ) := by
    rw [denominator_cast ha n]
    exact one_le_contQ (fun k => one_le_digit ha k) n
  omega

/-- The integer recurrence has no truncation loss when converted to natural denominators/digits. -/
theorem denominator_next {alpha : ℝ} (ha : Irrational alpha) (n : Nat) (hn : 1 ≤ n) :
    denominator alpha (n+1) = (digit alpha (n+1)).toNat*denominator alpha n+denominator alpha (n-1) := by
  have hdnonneg : (0 : ℤ) ≤ digit alpha (n+1) := le_trans (by decide) (one_le_digit ha n)
  have hi : (denominator alpha (n+1) : ℤ) =
      ((digit alpha (n+1)).toNat : ℤ)*(denominator alpha n : ℤ)+(denominator alpha (n-1) : ℤ) := by
    rw [denominator_cast ha (n+1),denominator_cast ha n,denominator_cast ha (n-1),
      Int.toNat_of_nonneg hdnonneg,show n-1+2 = n+1 by omega]
    rfl
  exact_mod_cast hi

/-- A large enough index makes the previous denominator pay any fixed break-window margin. -/
theorem previous_margin {alpha : ℝ} (ha : Irrational alpha) (K C n : Nat)
    (hn : K*(C+2)+2 ≤ n) : K*(C+2) ≤ denominator alpha (n-1) := by
  have hn2 : 2 ≤ n := by omega
  have hg := contQ_ge (fun k => one_le_digit ha k) (n-2)
  rw [show n-2+3 = (n-1)+2 by omega,← denominator_cast ha (n-1)] at hg
  have hb : K*(C+2) ≤ (n-2)+1 := by omega
  have hbInt : ((K*(C+2) : Nat) : ℤ) ≤ ((n-2 : Nat) : ℤ)+1 := by exact_mod_cast hb
  have h := le_trans hbInt hg
  exact_mod_cast h

/-- At the original digit threshold, the next denominator covers the entire counting window plus q. -/
theorem next_covers_window {alpha : ℝ} (ha : Irrational alpha) (K C n : Nat)
    (hn : K*(C+2)+2 ≤ n) (hdigit : (K : ℤ) < digit alpha (n+1)) :
    K*(denominator alpha n+C+2)+denominator alpha n ≤ denominator alpha (n+1) := by
  have hdnonneg : (0 : ℤ) ≤ digit alpha (n+1) := le_trans (by decide) (one_le_digit ha n)
  have hdcast : ((digit alpha (n+1)).toNat : ℤ) = digit alpha (n+1) := Int.toNat_of_nonneg hdnonneg
  have hdNat : K < (digit alpha (n+1)).toNat := by
    have h : (K : ℤ) < ((digit alpha (n+1)).toNat : ℤ) := by rw [hdcast]; exact hdigit
    exact_mod_cast h
  exact ArcBreakBounds.next_denominator_covers_window K (denominator alpha n) C
    (denominator alpha (n-1)) ((digit alpha (n+1)).toNat) (denominator alpha (n+1))
    hdNat (previous_margin ha K C n hn) (denominator_next ha n (by omega))

/-- One sufficiently late large digit supplies every approximation premise of the finite-step exclusion. -/
theorem no_repeat_at_large_digit {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha) (C n : Nat)
    (hn : 2^(r+1)*(C+2)+2 ≤ n) (hdigit : ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) :
    ¬ ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) (denominator alpha n) C := by
  let p : ℤ := contP (digit alpha) (n+2)
  let u : ℤ := (-1)^(n+1)*contQ (digit alpha) (n+1)
  let v : ℤ := -((-1)^(n+1))*contP (digit alpha) (n+1)
  have hbez : u*p+v*(denominator alpha n : ℤ) = 1 := by
    rw [denominator_cast ha n]
    exact ArcDeterminant.continuant_bezout alpha n
  have he := ArcDeterminant.continuant_error_lt_next ha n
  dsimp only at he
  have hepos : 0 < |(denominator alpha n : ℝ)*alpha-p| := by
    rw [denominator_real ha n]
    simpa only [mul_comm] using he.1
  have heupper : |(denominator alpha n : ℝ)*alpha-p| < 1/(denominator alpha (n+1) : ℝ) := by
    rw [denominator_real ha n,denominator_real ha (n+1)]
    simpa only [mul_comm,Nat.add_assoc] using he.2
  have hnpos : (0 : ℝ) < denominator alpha (n+1) := by exact_mod_cast denominator_pos ha (n+1)
  have hprod : |(denominator alpha n : ℝ)*alpha-p| * (denominator alpha (n+1) : ℝ) < 1 :=
    (lt_div_iff₀ hnpos).1 heupper
  have hmargin := next_covers_window ha (2^(r+1)) C n hn hdigit
  have hmarginR : (((2^(r+1)*(denominator alpha n+C+2) : Nat) : ℝ)+(denominator alpha n : ℝ)) ≤
      (denominator alpha (n+1) : ℝ) := by exact_mod_cast hmargin
  have hscale : (((2^(r+1)*(denominator alpha n+C+2) : Nat) : ℝ)+(denominator alpha n : ℝ))*
      |(denominator alpha n : ℝ)*alpha-p| ≤ 1 := by
    have hmul := mul_le_mul_of_nonneg_right hmarginR hepos.le
    nlinarith
  exact ArcStepCode.no_repeat_bound S alpha theta (denominator alpha n) C p u v
    (denominator_pos ha n) hbez hepos hscale

/-- Infinitely late digits above the original threshold contradict every fixed repeat obstruction constant. -/
theorem repeat_bound_fails {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧ ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) (C : Nat) :
    ∃ q : Nat, 0 < q ∧ ¬ ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) q C := by
  obtain ⟨n,hn,hdigit⟩ := hlarge (2^(r+1)*(C+2)+2)
  exact ⟨denominator alpha n,denominator_pos ha n,no_repeat_at_large_digit S alpha theta ha C n hn hdigit⟩

/-- Abstract rotation-code exclusion; the physical Rule30 bridge must still supply the uniform bound. -/
theorem no_uniform_repeat_bound {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧ ((2^(r+1) : Nat) : ℤ) < digit alpha (n+1)) :
    ¬ ∃ C : Nat, ∀ q : Nat, 0 < q → ArcBreakSequence.RepeatBound (ArcStepCode.orbit S alpha theta) q C := by
  rintro ⟨C,hC⟩
  obtain ⟨q,hq,hnot⟩ := repeat_bound_fails S alpha theta ha hlarge C
  exact hnot (hC q hq)

end ArcRotation

/- Component: SharpAdjacentReturn; proof body retained from the release-checked integration. -/
namespace SharpAdjacentReturn

/-- Coordinates in an integer basis of determinant d with d^2=1. -/
theorem basis_coordinates (p q P Q a m d : Int)
    (hdet : p*Q-P*q = d) (hd : d*d = 1) :
    let u := d*(a*Q-P*m)
    let v := d*(p*m-a*q)
    u*p+v*P = a ∧ u*q+v*Q = m := by
  dsimp only
  constructor
  · calc
      d*(a*Q-P*m)*p+d*(p*m-a*q)*P = d*a*(p*Q-P*q) := by ring
      _ = a := by
        rw [hdet]
        calc d*a*d = a*(d*d) := by ring
             _ = a := by rw [hd]; ring
  · calc
      d*(a*Q-P*m)*q+d*(p*m-a*q)*Q = d*m*(p*Q-P*q) := by ring
      _ = m := by
        rw [hdet]
        calc d*m*d = m*(d*d) := by ring
             _ = m := by rw [hd]; ring

/-- Opposite signed errors cannot cancel at a positive coordinate smaller than Q. -/
theorem positive_error_bound (q Q u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hQ : 0 < Q)
    (hm : 0 < u*q+v*Q) (hmQ : u*q+v*Q < Q)
    (hepsilon : 0 < epsilon) (heta : eta < 0) :
    epsilon ≤ |(u : ℝ)*epsilon+(v : ℝ)*eta| := by
  by_cases hu : u ≤ 0
  · have hv : 0 < v := by
      by_contra hnot
      have hvle : v ≤ 0 := le_of_not_gt hnot
      have huq := mul_nonpos_of_nonpos_of_nonneg hu hq.le
      have hvQ := mul_nonpos_of_nonpos_of_nonneg hvle hQ.le
      omega
    have huone : u ≤ -1 := by
      by_contra hnot
      have hu0 : u = 0 := by omega
      have hvone : 1 ≤ v := by omega
      have hb := mul_le_mul_of_nonneg_right hvone hQ.le
      rw [hu0] at hmQ
      nlinarith
    have huR : (u : ℝ) ≤ -1 := by exact_mod_cast huone
    have hvR : (0 : ℝ) ≤ v := by exact_mod_cast hv.le
    have hleft := mul_le_mul_of_nonneg_right huR hepsilon.le
    have hright := mul_nonpos_of_nonneg_of_nonpos hvR heta.le
    have hsum : (u : ℝ)*epsilon+(v : ℝ)*eta ≤ -epsilon := by nlinarith
    rw [abs_of_nonpos (show (u : ℝ)*epsilon+(v : ℝ)*eta ≤ 0 by linarith)]
    linarith
  · have huone : 1 ≤ u := by omega
    have hv : v ≤ 0 := by
      by_contra hnot
      have hvone : 1 ≤ v := by omega
      have huq := mul_nonneg (by omega : 0 ≤ u) hq.le
      have hb := mul_le_mul_of_nonneg_right hvone hQ.le
      nlinarith
    have huR : (1 : ℝ) ≤ u := by exact_mod_cast huone
    have hvR : (v : ℝ) ≤ 0 := by exact_mod_cast hv
    have hleft := mul_le_mul_of_nonneg_right huR hepsilon.le
    have hright := mul_nonneg_of_nonpos_of_nonpos hvR heta.le
    have hsum : epsilon ≤ (u : ℝ)*epsilon+(v : ℝ)*eta := by nlinarith
    exact le_trans hsum (le_abs_self _)

/-- Sharp adjacent-convergent form, with determinant and error signs explicit. -/
theorem sharp_return (alpha : ℝ) (p q P Q a m d : Int)
    (hq : 0 < q) (hQ : 0 < Q) (hm : 0 < m) (hmQ : m < Q)
    (hdet : p*Q-P*q = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0) :
    |(q : ℝ)*alpha-p| ≤ |(m : ℝ)*alpha-a| := by
  let u := d*(a*Q-P*m)
  let v := d*(p*m-a*q)
  obtain ⟨ha,hcoord⟩ := basis_coordinates p q P Q a m d hdet hd
  change u*p+v*P = a at ha
  change u*q+v*Q = m at hcoord
  have hm' : 0 < u*q+v*Q := by rw [hcoord]; exact hm
  have hmQ' : u*q+v*Q < Q := by rw [hcoord]; exact hmQ
  let epsilon := (q : ℝ)*alpha-p
  let eta := (Q : ℝ)*alpha-P
  have herr : (m : ℝ)*alpha-a = (u : ℝ)*epsilon+(v : ℝ)*eta := by
    rw [← hcoord,← ha]
    dsimp [epsilon,eta]
    push_cast
    ring
  change epsilon*eta < 0 at hsigns
  change |epsilon| ≤ |(m : ℝ)*alpha-a|
  rw [herr]
  by_cases hepsilon : 0 < epsilon
  · have heta : eta < 0 := by
      by_contra hnot
      have hp := mul_nonneg hepsilon.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_pos hepsilon]
    exact positive_error_bound q Q u v epsilon eta hq hQ hm' hmQ' hepsilon heta
  · have hepsilonNeg : epsilon < 0 := by
      have hle : epsilon ≤ 0 := le_of_not_gt hepsilon
      by_contra hnot
      have hz : epsilon = 0 := by linarith
      rw [hz,zero_mul] at hsigns
      exact (lt_irrefl 0) hsigns
    have heta : 0 < eta := by
      by_contra hnot
      have hp := mul_nonneg_of_nonpos_of_nonpos hepsilonNeg.le (le_of_not_gt hnot)
      linarith
    have h := positive_error_bound q Q u v (-epsilon) (-eta) hq hQ hm' hmQ'
      (by linarith) (by linarith)
    have heq : (u : ℝ)*(-epsilon)+(v : ℝ)*(-eta) = -((u : ℝ)*epsilon+(v : ℝ)*eta) := by ring
    rw [heq,abs_neg] at h
    rw [abs_of_neg hepsilonNeg]
    exact h

/-- Independent guard control: without opposite errors, the claimed lower bound fails. -/
theorem same_sign_control :
    ((0 : Int)*2-1*1)^2 = 1 ∧
    0 < ((1 : ℝ)*(3/5)-0)*((2 : ℝ)*(3/5)-1) ∧
    |(1 : ℝ)*(3/5)-1| < |(1 : ℝ)*(3/5)-0| := by
  norm_num

/-- Independent endpoint control: m=Q must be excluded, even with opposite errors. -/
theorem endpoint_control :
    ((1 : Int)*3-2*2)^2 = 1 ∧
    ((2 : ℝ)*(5/8)-1)*((3 : ℝ)*(5/8)-2) < 0 ∧
    |(3 : ℝ)*(5/8)-2| < |(2 : ℝ)*(5/8)-1| := by
  norm_num

end SharpAdjacentReturn

/- Component: MechanicalCarry; proof body retained from the release-checked integration. -/
namespace MechanicalCarry

noncomputable def level (alpha theta : ℝ) (s : Nat) : Int :=
  ⌊theta+(s : ℝ)*alpha⌋

noncomputable def mech (alpha theta : ℝ) (s : Nat) : Int :=
  level alpha theta (s+1)-level alpha theta s

noncomputable def carry (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) : Int :=
  level alpha theta (s+q)-level alpha theta s-p

/-- Cancellation, with all Nat-index shifts made explicit. -/
theorem difference_identity (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) :
    mech alpha theta (s+q)-mech alpha theta s =
      carry alpha theta q p (s+1)-carry alpha theta q p s := by
  unfold mech carry
  rw [show s+q+1 = s+1+q by omega]
  omega

/-- An arbitrary integer approximation p leaves the floor of fractional phase plus signed error. -/
theorem carry_as_floor (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat) :
    carry alpha theta q p s =
      ⌊Int.fract (theta+(s : ℝ)*alpha)+((q : ℝ)*alpha-p)⌋ := by
  have hf := Int.floor_add_fract (theta+(s : ℝ)*alpha)
  have e : theta+((s+q : Nat) : ℝ)*alpha =
      ((⌊theta+(s : ℝ)*alpha⌋+p : Int) : ℝ)+
        (Int.fract (theta+(s : ℝ)*alpha)+((q : ℝ)*alpha-p)) := by
    calc
      theta+((s+q : Nat) : ℝ)*alpha = (theta+(s : ℝ)*alpha)+(q : ℝ)*alpha := by
        push_cast
        ring
      _ = _ := by push_cast; linarith
  unfold carry level
  rw [e,Int.floor_intCast_add]
  omega

/-- Positive error gives a left-closed upper carry arc. -/
theorem carry_positive (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : 0 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 1) :
    carry alpha theta q p s =
      if 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha) then 1 else 0 := by
  rw [carry_as_floor]
  by_cases h : 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha)
  · rw [ite_eq_left h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]
  · rw [ite_eq_right h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]

/-- Negative error gives a right-open lower carry arc and carry value -1. -/
theorem carry_negative (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : -1 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 0) :
    carry alpha theta q p s =
      if Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p) then -1 else 0 := by
  rw [carry_as_floor]
  by_cases h : Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p)
  · rw [ite_eq_left h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]
  · rw [ite_eq_right h,Int.floor_eq_iff]
    constructor <;> push_cast <;> linarith [Int.fract_nonneg (theta+(s : ℝ)*alpha),
      Int.fract_lt_one (theta+(s : ℝ)*alpha)]

theorem nonzero_positive (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : 0 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 1) :
    carry alpha theta q p s ≠ 0 ↔
      1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha) := by
  rw [carry_positive alpha theta q p s h0 h1]
  by_cases h : 1-((q : ℝ)*alpha-p) ≤ Int.fract (theta+(s : ℝ)*alpha)
  · rw [ite_eq_left h]
    exact ⟨fun _ => h, fun _ => by decide⟩
  · rw [ite_eq_right h]
    exact ⟨fun hne => absurd rfl hne, fun hh => absurd hh h⟩

theorem nonzero_negative (alpha theta : ℝ) (q : Nat) (p : Int) (s : Nat)
    (h0 : -1 < (q : ℝ)*alpha-p) (h1 : (q : ℝ)*alpha-p < 0) :
    carry alpha theta q p s ≠ 0 ↔
      Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p) := by
  rw [carry_negative alpha theta q p s h0 h1]
  by_cases h : Int.fract (theta+(s : ℝ)*alpha) < -((q : ℝ)*alpha-p)
  · rw [ite_eq_left h]
    exact ⟨fun _ => h, fun _ => by decide⟩
  · rw [ite_eq_right h]
    exact ⟨fun hne => absurd rfl hne, fun hh => absurd hh h⟩

/-- Endpoint controls: the positive arc includes its threshold; the negative arc excludes its threshold. -/
theorem half_open_endpoint_controls :
    carry (1/4) (3/4) 1 0 0 = 1 ∧ carry (3/4) (1/4) 1 1 0 = 0 := by
  norm_num [carry,level]

end MechanicalCarry

/- Component: FiniteHorizonBounds; proof body retained from the release-checked integration. -/
namespace FiniteHorizonBounds

/-- All comparisons used in the obstruction must fit in the supplied prefix. -/
def RepeatBoundThrough {α : Type} (c : Nat → α) (N C : Nat) : Prop :=
  ∀ q a b, 0 < q → a ≤ b → b+q ≤ N →
    (∀ s, a ≤ s → s ≤ b → c (s+q) = c s) → b ≤ 2*a+q+C

/-- The finite counterpart of the delivered global future-break constructor. -/
theorem future_break {α : Type} (c : Nat → α) (N C q a : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hdeadline : 2*a+2*q+C+1 ≤ N) :
    ∃ m, a ≤ m ∧ m ≤ 2*a+q+C+1 ∧ c (m+q) ≠ c m := by
  apply Classical.byContradiction
  intro hno
  have heq : ∀ s, a ≤ s → s ≤ 2*a+q+C+1 → c (s+q) = c s := by
    intro s hs hb
    by_cases h : c (s+q) = c s
    · exact h
    · exact False.elim (hno ⟨s,hs,hb,h⟩)
  have hb := hr q a (2*a+q+C+1) hq (by omega) (by omega) heq
  omega

/-- A zero carry at two consecutive indices makes the compared letters equal. -/
theorem equal_of_zero_carry (c z : Nat → Int) (q s : Nat)
    (hid : c (s+q)-c s = z (s+1)-z s)
    (h0 : z s = 0) (h1 : z (s+1) = 0) : c (s+q) = c s := by
  rw [h0,h1] at hid
  omega

/-- Some nonzero carry must occur by q+C+2, using only the finite prefix. -/
theorem first_carry (c z : Nat → Int) (N C q : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hdeadline : 2*q+C+1 ≤ N) :
    ∃ h, h ≤ q+C+2 ∧ z h ≠ 0 := by
  apply Classical.byContradiction
  intro hno
  have hz : ∀ s, s ≤ q+C+2 → z s = 0 := by
    intro s hs
    by_cases h : z s = 0
    · exact h
    · exact False.elim (hno ⟨s,hs,h⟩)
  have heq : ∀ s, 0 ≤ s → s ≤ q+C+1 → c (s+q) = c s := by
    intro s _ hs
    exact equal_of_zero_carry c z q s (hid s) (hz s (by omega)) (hz (s+1) (by omega))
  have hb := hr q 0 (q+C+1) hq (by omega) (by omega) heq
  omega

/-- A second nonzero carry has a finite deadline after any bounded first one. -/
theorem next_carry (c z : Nat → Int) (N C q h : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hh : h ≤ q+C+2) (hdeadline : 4*q+3*C+8 ≤ N) :
    ∃ k, h < k ∧ k ≤ 2*h+q+C+4 ∧ z k ≠ 0 := by
  apply Classical.byContradiction
  intro hno
  have hz : ∀ s, h < s → s ≤ 2*h+q+C+4 → z s = 0 := by
    intro s hs hb
    by_cases h : z s = 0
    · exact h
    · exact False.elim (hno ⟨s,hs,hb,h⟩)
  have heq : ∀ s, h+1 ≤ s → s ≤ 2*h+q+C+3 → c (s+q) = c s := by
    intro s hs hb
    exact equal_of_zero_carry c z q s (hid s) (hz s (by omega) (by omega))
      (hz (s+1) (by omega) (by omega))
  have hb := hr q (h+1) (2*h+q+C+3) hq (by omega) (by omega) heq
  omega

/-- A separately supplied sharp return gap bounds the next denominator. -/
theorem denominator_growth (c z : Nat → Int) (N C q Q : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hdeadline : 4*q+3*C+8 ≤ N)
    (hgap : ∀ h k, h < k → z h ≠ 0 → z k ≠ 0 → h+Q ≤ k) :
    ∃ h, z h ≠ 0 ∧ h ≤ q+C+2 ∧ Q ≤ h+q+C+4 ∧ Q ≤ 2*q+2*C+6 := by
  obtain ⟨h,hh,hz⟩ := first_carry c z N C q hr hq hid (by omega)
  obtain ⟨k,hk,hku,hzk⟩ := next_carry c z N C q h hr hq hid hh hdeadline
  have hsep := hgap h k hk hz hzk
  exact ⟨h,hz,hh,by omega,by omega⟩

/-- Scope control: a zero-length horizon supplies no global future-break conclusion. -/
theorem zero_horizon_control (C : Nat) :
    RepeatBoundThrough (fun _ : Nat => (0 : Int)) 0 C ∧
    ¬ ∃ m : Nat, (fun _ : Nat => (0 : Int)) (m+1) ≠ (fun _ : Nat => (0 : Int)) m := by
  constructor
  · intro q a b hq hab hN heq
    omega
  · intro ⟨m,hm⟩
    exact hm rfl

end FiniteHorizonBounds

/- Component: CarryReturnSpacing; proof body retained from the release-checked integration. -/
namespace CarryReturnSpacing

/-- Two nonzero carries have fractional phases strictly closer than the carry-arc length. -/
theorem phases_close (alpha theta : ℝ) (q : Nat) (p : Int) (h k : Nat)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (hne : (q : ℝ)*alpha-p ≠ 0)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta q p k ≠ 0) :
    |Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha)| <
      |(q : ℝ)*alpha-p| := by
  by_cases hpos : 0 < (q : ℝ)*alpha-p
  · have ha := (MechanicalCarry.nonzero_positive alpha theta q p h hpos hhi).mp hh
    have hb := (MechanicalCarry.nonzero_positive alpha theta q p k hpos hhi).mp hk
    rw [abs_of_pos hpos,abs_lt]
    constructor <;> linarith [Int.fract_lt_one (theta+(h : ℝ)*alpha),
      Int.fract_lt_one (theta+(k : ℝ)*alpha)]
  · have hneg : (q : ℝ)*alpha-p < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · exact False.elim (hne h)
    have ha := (MechanicalCarry.nonzero_negative alpha theta q p h hlo hneg).mp hh
    have hb := (MechanicalCarry.nonzero_negative alpha theta q p k hlo hneg).mp hk
    rw [abs_of_neg hneg,abs_lt]
    constructor <;> linarith [Int.fract_nonneg (theta+(h : ℝ)*alpha),
      Int.fract_nonneg (theta+(k : ℝ)*alpha)]

/-- The difference of phase floors is an explicit integer return numerator. -/
theorem phase_difference (alpha theta : ℝ) (h k : Nat) (horder : h ≤ k) :
    ((k-h : Nat) : ℝ)*alpha-
        ((MechanicalCarry.level alpha theta k-MechanicalCarry.level alpha theta h : Int) : ℝ) =
      Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha) := by
  unfold MechanicalCarry.level
  rw [Nat.cast_sub horder]
  push_cast
  nlinarith [Int.floor_add_fract (theta+(h : ℝ)*alpha),
    Int.floor_add_fract (theta+(k : ℝ)*alpha)]

/-- Genuine visits to the actual carry arc are separated by at least Q. -/
theorem return_spacing (alpha theta : ℝ) (q Q : Nat) (p P d : Int)
    (hq : 0 < q) (hQ : 0 < Q)
    (hdet : p*(Q : Int)-P*(q : Int) = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (h k : Nat) (hhk : h < k)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta q p k ≠ 0) : h+Q ≤ k := by
  by_contra hnot
  have hm : 0 < k-h := by omega
  have hmQ : k-h < Q := by omega
  have hne : (q : ℝ)*alpha-p ≠ 0 := by
    intro hz
    rw [hz,zero_mul] at hsigns
    exact (lt_irrefl 0) hsigns
  have hclose := phases_close alpha theta q p h k hlo hhi hne hh hk
  let A : Int := MechanicalCarry.level alpha theta k-MechanicalCarry.level alpha theta h
  have hsharp := SharpAdjacentReturn.sharp_return alpha p (q : Int) P (Q : Int) A
    ((k-h : Nat) : Int) d (by exact_mod_cast hq) (by exact_mod_cast hQ)
    (by exact_mod_cast hm) (by exact_mod_cast hmQ) hdet hd (by exact_mod_cast hsigns)
  push_cast at hsharp
  have heq : ((k-h : Nat) : ℝ)*alpha-(A : ℝ) =
      Int.fract (theta+(k : ℝ)*alpha)-Int.fract (theta+(h : ℝ)*alpha) := by
    exact phase_difference alpha theta h k hhk.le
  rw [heq] at hsharp
  exact (not_lt_of_ge hsharp) hclose

end CarryReturnSpacing

/- Component: ActualContinuants; proof body retained from the release-checked integration. -/
namespace FiniteHorizonContinuants

open Rule30Equivalents.Lagrange

noncomputable def numerator (alpha : ℝ) (n : Nat) : Int :=
  contP (digit alpha) (n+2)

noncomputable def error (alpha : ℝ) (n : Nat) : ℝ :=
  (ArcRotation.denominator alpha n : ℝ)*alpha-numerator alpha n

noncomputable def multiplier (alpha : ℝ) (n : Nat) : ℝ :=
  cq alpha (n+1)*(ArcRotation.denominator alpha n : ℝ)+
    (contQ (digit alpha) (n+1) : ℝ)

/-- The same positive multiplier as the kit's exact error_mul identity. -/
theorem multiplier_pos {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    0 < multiplier alpha n := by
  have hq : (0 : ℝ) < ArcRotation.denominator alpha n := by
    exact_mod_cast ArcRotation.denominator_pos ha n
  have hc : 0 < cq alpha (n+1) := lt_trans (by norm_num) (one_lt_cq ha n)
  have hp : (0 : ℝ) ≤ contQ (digit alpha) (n+1) := by
    exact_mod_cast contQ_nonneg (fun k => one_le_digit ha k) (n+1)
  have hprod := mul_pos hc hq
  unfold multiplier
  linarith

/-- The concrete signed error identity, with the public kit's index shift+2. -/
theorem error_identity {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    error alpha n*multiplier alpha n = (-1 : ℝ)^n := by
  dsimp only [error,multiplier,numerator]
  rw [ArcRotation.denominator_real ha n]
  simpa only [mul_comm] using error_mul ha n

/-- Adjacent errors of the ACTUAL continuants have opposite strict signs. -/
theorem adjacent_errors_opposite {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    error alpha n*error alpha (n+1) < 0 := by
  have h0 := error_identity ha n
  have h1 := error_identity ha (n+1)
  rw [pow_succ] at h1
  have hsquare : ((-1 : ℝ)^n)*((-1 : ℝ)^n) = 1 := by
    rw [← mul_pow]
    norm_num
  have hprod : (error alpha n*error alpha (n+1))*
      (multiplier alpha n*multiplier alpha (n+1)) = -1 := by
    calc
      _ = (error alpha n*multiplier alpha n)*
          (error alpha (n+1)*multiplier alpha (n+1)) := by ring
      _ = ((-1 : ℝ)^n)*(((-1 : ℝ)^n)*(-1)) := by rw [h0,h1]
      _ = -1 := by nlinarith [hsquare]
  have hpositive := mul_pos (multiplier_pos ha n) (multiplier_pos ha (n+1))
  by_contra hnot
  have hnonneg := mul_nonneg (le_of_not_gt hnot) hpositive.le
  linarith

/-- The adjacent integer determinant has square one, in sharp_return's orientation. -/
theorem adjacent_determinant_unit {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    let d := numerator alpha n*(ArcRotation.denominator alpha (n+1) : Int)-
      numerator alpha (n+1)*(ArcRotation.denominator alpha n : Int)
    d*d = 1 := by
  dsimp only
  rw [ArcRotation.denominator_cast ha (n+1),ArcRotation.denominator_cast ha n]
  unfold numerator
  have hdet := cont_det (digit alpha) (n+2)
  have hd : contP (digit alpha) (n+2)*contQ (digit alpha) (n+1+2)-
      contP (digit alpha) (n+1+2)*contQ (digit alpha) (n+2) = -((-1 : Int)^(n+2)) := by
    have heq : n+1+2 = n+2+1 := by omega
    rw [heq]
    linear_combination -hdet
  have hprod := congrArg (fun x : Int => x*x) hd
  rw [neg_mul_neg,← mul_pow] at hprod
  norm_num at hprod
  exact hprod

/-- The next-denominator approximation bound already proved in the arc development implies |error|<1. -/
theorem error_abs_lt_one {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    |error alpha n| < 1 := by
  have he := ArcDeterminant.continuant_error_lt_next ha n
  dsimp only at he
  have hbound : |error alpha n| < 1/(ArcRotation.denominator alpha (n+1) : ℝ) := by
    dsimp only [error,numerator]
    rw [ArcRotation.denominator_real ha n,ArcRotation.denominator_real ha (n+1)]
    simpa only [mul_comm,Nat.add_assoc] using he.2
  have hQ : (1 : ℝ) ≤ ArcRotation.denominator alpha (n+1) := by
    exact_mod_cast (show 1 ≤ ArcRotation.denominator alpha (n+1) from
      ArcRotation.denominator_pos ha (n+1))
  have hQpos : (0 : ℝ) < ArcRotation.denominator alpha (n+1) := by linarith
  have hrecip : 1/(ArcRotation.denominator alpha (n+1) : ℝ) ≤ 1 := by
    apply (div_le_iff₀ hQpos).2
    linarith
  exact lt_of_lt_of_le hbound hrecip

end FiniteHorizonContinuants

/- Component: ActualCarrySpacing; proof body retained from the release-checked integration. -/
namespace FiniteHorizonActualCarry

open FiniteHorizonContinuants

/-- Actual nonzero carry visits at a convergent are separated by its next denominator. -/
theorem return_spacing (alpha theta : ℝ) (ha : Irrational alpha) (n h k : Nat)
    (hhk : h < k)
    (hh : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) k ≠ 0) :
    h+ArcRotation.denominator alpha (n+1) ≤ k := by
  let q := ArcRotation.denominator alpha n
  let Q := ArcRotation.denominator alpha (n+1)
  let p := numerator alpha n
  let P := numerator alpha (n+1)
  let d := p*(Q : Int)-P*(q : Int)
  have hd : d*d = 1 := adjacent_determinant_unit ha n
  have hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0 := adjacent_errors_opposite ha n
  have herror : |(q : ℝ)*alpha-p| < 1 := error_abs_lt_one ha n
  have hrange := abs_lt.mp herror
  exact CarryReturnSpacing.return_spacing alpha theta q Q p P d
    (ArcRotation.denominator_pos ha n) (ArcRotation.denominator_pos ha (n+1))
    rfl hd hsigns hrange.1 hrange.2 h k hhk hh hk

/-- Finite comparison deadlines bound actual adjacent denominators, with a genuine bounded carry witness. -/
theorem denominator_growth (alpha theta : ℝ) (ha : Irrational alpha) (N C n : Nat)
    (hr : FiniteHorizonBounds.RepeatBoundThrough (MechanicalCarry.mech alpha theta) N C)
    (hdeadline : 4*ArcRotation.denominator alpha n+3*C+8 ≤ N) :
    ∃ h, MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) h ≠ 0 ∧
      h ≤ ArcRotation.denominator alpha n+C+2 ∧
      ArcRotation.denominator alpha (n+1) ≤ h+ArcRotation.denominator alpha n+C+4 ∧
      ArcRotation.denominator alpha (n+1) ≤ 2*ArcRotation.denominator alpha n+2*C+6 := by
  apply FiniteHorizonBounds.denominator_growth
    (MechanicalCarry.mech alpha theta)
    (MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha n) (numerator alpha n))
    N C (ArcRotation.denominator alpha n) (ArcRotation.denominator alpha (n+1)) hr
    (ArcRotation.denominator_pos ha n)
    (fun s => MechanicalCarry.difference_identity alpha theta (ArcRotation.denominator alpha n) (numerator alpha n) s)
    hdeadline
  intro h k hhk hh hk
  exact return_spacing alpha theta ha n h k hhk hh hk

end FiniteHorizonActualCarry

/- Component: DenominatorBootstrap; proof body retained from the release-checked integration. -/
namespace DenominatorBootstrap

/-- One application: only the current denominator's deadline must fit in N. -/
def GrowthAt (N C q next : Nat) : Prop :=
  4*q+3*C+8 ≤ N → next ≤ 2*q+2*C+6

/-- Four guarded applications, with the exact conservative budget retained. -/
theorem four_steps (C q0 q1 q2 q3 q4 : Nat)
    (h0 : q0 ≤ 2*C+8)
    (h1 : GrowthAt (251*(C+4)) C q0 q1)
    (h2 : GrowthAt (251*(C+4)) C q1 q2)
    (h3 : GrowthAt (251*(C+4)) C q2 q3)
    (h4 : GrowthAt (251*(C+4)) C q3 q4) :
    q1 ≤ 6*C+22 ∧ q2 ≤ 14*C+50 ∧ q3 ≤ 30*C+106 ∧ q4 ≤ 62*C+218 ∧
    4*q4+3*C+8+124 ≤ 251*(C+4) := by
  have hg1 := h1 (by omega)
  have hb1 : q1 ≤ 6*C+22 := by omega
  have hg2 := h2 (by omega)
  have hb2 : q2 ≤ 14*C+50 := by omega
  have hg3 := h3 (by omega)
  have hb3 : q3 ≤ 30*C+106 := by omega
  have hg4 := h4 (by omega)
  have hb4 : q4 ≤ 62*C+218 := by omega
  exact ⟨hb1,hb2,hb3,hb4,by omega⟩

/-- In particular the final target scale is usable without an additional growth premise. -/
theorem final_deadline (C q0 q1 q2 q3 q4 : Nat)
    (h0 : q0 ≤ 2*C+8)
    (h1 : GrowthAt (251*(C+4)) C q0 q1)
    (h2 : GrowthAt (251*(C+4)) C q1 q2)
    (h3 : GrowthAt (251*(C+4)) C q2 q3)
    (h4 : GrowthAt (251*(C+4)) C q3 q4) :
    4*q4+3*C+8 < 251*(C+4) := by
  have hb := (four_steps C q0 q1 q2 q3 q4 h0 h1 h2 h3 h4).2.2.2.2
  omega

/-- Three bounded visits with the two exact shifts contradict a sufficiently large prior denominator. -/
theorem final_visit_contradiction (C previous q qNext qAfter h0 h1 h2 : Nat)
    (hprevious : 2*C+8 < previous)
    (hrecurrence : qAfter = qNext+q)
    (hlo : previous ≤ h0+C+4)
    (hupper : h2 ≤ qAfter+C+2)
    (hshift1 : h1 = h0+q) (hshift2 : h2 = h1+qNext) : False := by
  omega

end DenominatorBootstrap

/- Component: FiniteHorizonSelection; proof body retained from the release-checked integration. -/
namespace FiniteHorizonSelection

/-- A coefficient at least two would consume more than the allowed denominator growth. -/
theorem coefficient_one (C a q previous next : Nat)
    (ha : 1 ≤ a) (hrec : next = a*q+previous)
    (hgrowth : next ≤ 2*q+2*C+6) (hprevious : 2*C+6 < previous) : a = 1 := by
  apply Classical.byContradiction
  intro hnot
  have ha2 : 2 ≤ a := by omega
  have hprod := Nat.mul_le_mul_right q ha2
  omega

/-- A supplied finite witness above the threshold gives a crossing before it, without a least-index operator. -/
theorem crossing_before (q : Nat → Nat) (T : Nat) (h0 : q 0 ≤ T) (n : Nat) :
    T < q n → ∃ r, r < n ∧ q r ≤ T ∧ T < q (r+1) := by
  induction n with
  | zero => intro hn; omega
  | succ n ih =>
    intro hn
    by_cases h : T < q n
    · obtain ⟨r,hr,hlo,hhi⟩ := ih h
      exact ⟨r,by omega,hlo,hhi⟩
    · exact ⟨n,by omega,(by omega),hn⟩

/-- Only unboundedness and q0=1 are needed to select the initial usable scale. -/
theorem crossing_scale (q : Nat → Nat) (T : Nat) (hT : 1 ≤ T)
    (h0 : q 0 = 1) (hunbounded : ∀ B, ∃ n, B < q n) :
    ∃ r, q r ≤ T ∧ T < q (r+1) := by
  obtain ⟨n,hn⟩ := hunbounded T
  obtain ⟨r,_,hlo,hhi⟩ := crossing_before q T (by omega) n hn
  exact ⟨r,hlo,hhi⟩

/-- Positive recurrence coefficients make all successive denominators nondecreasing. -/
theorem successive_ge (q a : Nat → Nat)
    (h0 : q 0 ≤ q 1) (ha : ∀ n, 1 ≤ a (n+2))
    (hrec : ∀ n, q (n+2) = a (n+2)*q (n+1)+q n) :
    ∀ n, q n ≤ q (n+1) := by
  intro n
  cases n with
  | zero => exact h0
  | succ n =>
    have hprod := Nat.mul_le_mul_right (q (n+1)) (ha n)
    have hr := hrec n
    show q (n+1) ≤ q (n+2)
    omega

end FiniteHorizonSelection

/- Component: ContinuantSequence; proof body retained from the release-checked integration. -/
namespace FiniteHorizonContinuantSequence

open Rule30Equivalents.Lagrange

/-- The first standard denominator is1, independently of the integer part of alpha. -/
theorem denominator_zero (alpha : ℝ) : ArcRotation.denominator alpha 0 = 1 := by
  simp [ArcRotation.denominator,contQ]

/-- Offset indexing avoids truncated subtraction in the actual recurrence. -/
theorem denominator_recurrence {alpha : ℝ} (ha : Irrational alpha) (n : Nat) :
    ArcRotation.denominator alpha (n+2) = (digit alpha (n+2)).toNat*
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
  exact ArcRotation.denominator_next ha (n+1) (by omega)

/-- A concrete witness B+1 suffices; no asymptotic numerical estimate enters. -/
theorem denominator_unbounded {alpha : ℝ} (ha : Irrational alpha) :
    ∀ B : Nat, ∃ n : Nat, B < ArcRotation.denominator alpha n := by
  intro B
  have h := contQ_ge (fun k => one_le_digit ha k) B
  rw [show B+3 = (B+1)+2 by omega,← ArcRotation.denominator_cast ha (B+1)] at h
  have hb : B+1 ≤ ArcRotation.denominator alpha (B+1) := by exact_mod_cast h
  exact ⟨B+1,by omega⟩

/-- Successive denominators may be equal initially, but never decrease. -/
theorem denominator_successive {alpha : ℝ} (ha : Irrational alpha) :
    ∀ n, ArcRotation.denominator alpha n ≤ ArcRotation.denominator alpha (n+1) := by
  apply FiniteHorizonSelection.successive_ge (ArcRotation.denominator alpha)
    (fun n => (digit alpha n).toNat)
  · rw [denominator_zero]
    have h := ArcRotation.denominator_pos ha 1
    omega
  · intro n
    have h : 1 ≤ digit alpha (n+2) := one_le_digit ha (n+1)
    have hnonneg : 0 ≤ digit alpha (n+2) := by omega
    have ht : (1 : Int) ≤ ((digit alpha (n+2)).toNat : Int) := by
      rw [Int.toNat_of_nonneg hnonneg]
      exact h
    exact_mod_cast ht
  · exact denominator_recurrence ha

/-- The exact initial scale used in the four-step finite budget exists for every irrational slope. -/
theorem threshold_crossing {alpha : ℝ} (ha : Irrational alpha) (C : Nat) :
    ∃ r, ArcRotation.denominator alpha r ≤ 2*C+8 ∧
      2*C+8 < ArcRotation.denominator alpha (r+1) := by
  exact FiniteHorizonSelection.crossing_scale (ArcRotation.denominator alpha) (2*C+8)
    (by omega) (denominator_zero alpha) (denominator_unbounded ha)

end FiniteHorizonContinuantSequence

/- Component: OppositeArcStrip; proof body retained from the release-checked integration. -/
namespace OppositeArcStrip

/-- The finite visit bounds themselves give the exact signed spatial strip.
The two recurrences are the coefficient-one conclusions of the caller. -/
theorem visit_difference_bounds (C previous q next after h k : Nat)
    (hnext : next = q+previous) (hafter : after = next+q)
    (hlow : next ≤ h+q+C+4) (hupp : h ≤ q+C+2)
    (klow : after ≤ k+next+C+4) (kupp : k ≤ next+C+2) :
    -(q : Int)-(2*(C : Int)+6) ≤ (h : Int)-(k : Int) ∧
      (h : Int)-(k : Int) ≤ 2*(C : Int)+6 := by
  omega

/-- With negative first error and positive second error, the spatial strip
and the open error strip force the basis coordinates (0,-1). -/
theorem negative_error_coordinates (q Q D u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ u*q+v*Q) (hupp : u*q+v*Q ≤ D)
    (hepsilon : epsilon < 0) (heta : 0 < eta)
    (herrlow : epsilon < (u : ℝ)*epsilon+(v : ℝ)*eta)
    (herrupp : (u : ℝ)*epsilon+(v : ℝ)*eta < 0) :
    u = 0 ∧ v = -1 := by
  have hQ : 0 < Q := lt_of_lt_of_le hq hqQ
  by_cases hu : 0 < u
  · have huone : 1 ≤ u := by omega
    by_cases hv : 0 ≤ v
    · have hleft := mul_le_mul_of_nonneg_right huone hq.le
      have hright := mul_nonneg hv hQ.le
      nlinarith
    · have hvone : v ≤ -1 := by omega
      have huR : (1 : ℝ) ≤ u := by exact_mod_cast huone
      have hvR : (v : ℝ) ≤ -1 := by exact_mod_cast hvone
      have hleft := mul_le_mul_of_nonpos_right huR hepsilon.le
      have hright := mul_le_mul_of_nonneg_right hvR heta.le
      nlinarith
  · by_cases huneg : u < 0
    · have huone : u ≤ -1 := by omega
      by_cases hv : v ≤ -1
      · have hleft := mul_le_mul_of_nonneg_right huone hq.le
        have hright := mul_le_mul_of_nonneg_right hv hQ.le
        nlinarith
      · have hvzero : 0 ≤ v := by omega
        have huR : (u : ℝ) ≤ -1 := by exact_mod_cast huone
        have hvR : (0 : ℝ) ≤ v := by exact_mod_cast hvzero
        have hleft := mul_le_mul_of_nonpos_right huR hepsilon.le
        have hright := mul_nonneg hvR heta.le
        nlinarith
    · have huzero : u = 0 := by omega
      have hvneg : v < 0 := by
        by_contra hnot
        have hvzero : (0 : ℝ) ≤ v := by exact_mod_cast (le_of_not_gt hnot)
        have hright := mul_nonneg hvzero heta.le
        rw [huzero,Int.cast_zero,zero_mul,zero_add] at herrupp
        linarith
      have hvone : v = -1 := by
        by_contra hnot
        have hvtwo : v ≤ -2 := by omega
        have hright := mul_le_mul_of_nonneg_right hvtwo hQ.le
        rw [huzero,zero_mul,zero_add] at hlow
        nlinarith
      exact ⟨huzero,hvone⟩

/-- Orientation-independent version: the return error has the opposite sign
to the second basis error and is strictly smaller than the first error. -/
theorem signed_coordinates (q Q D u v : Int) (epsilon eta : ℝ)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ u*q+v*Q) (hupp : u*q+v*Q ≤ D)
    (hsigns : epsilon*eta < 0)
    (hreturn : ((u : ℝ)*epsilon+(v : ℝ)*eta)*eta < 0)
    (hclose : |(u : ℝ)*epsilon+(v : ℝ)*eta| < |epsilon|) :
    u = 0 ∧ v = -1 := by
  by_cases heta : 0 < eta
  · have hepsilon : epsilon < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) heta.le
      linarith
    have herr : (u : ℝ)*epsilon+(v : ℝ)*eta < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) heta.le
      linarith
    rw [abs_of_neg herr,abs_of_neg hepsilon] at hclose
    exact negative_error_coordinates q Q D u v epsilon eta hq hqQ hD hlow hupp
      hepsilon heta (by linarith) herr
  · have hetaNeg : eta < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt heta) with h | h
      · exact h
      · rw [h,mul_zero] at hsigns
        exact False.elim ((lt_irrefl 0) hsigns)
    have hepsilon : 0 < epsilon := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hetaNeg.le
      linarith
    have herr : 0 < (u : ℝ)*epsilon+(v : ℝ)*eta := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hetaNeg.le
      linarith
    rw [abs_of_pos herr,abs_of_pos hepsilon] at hclose
    have heq : (u : ℝ)*(-epsilon)+(v : ℝ)*(-eta) =
        -((u : ℝ)*epsilon+(v : ℝ)*eta) := by ring
    apply negative_error_coordinates q Q D u v (-epsilon) (-eta) hq hqQ hD hlow hupp
      (by linarith) (by linarith)
    · rw [heq]
      linarith
    · rw [heq]
      linarith

/-- Adjacent integer data convert the coordinate conclusion to an exact
signed denominator and numerator, with no circle-norm API or offset search. -/
theorem exact_negative_return (alpha : ℝ) (p q P Q a m d D : Int)
    (hq : 0 < q) (hqQ : q ≤ Q) (hD : D < q)
    (hlow : -Q-D ≤ m) (hupp : m ≤ D)
    (hdet : p*Q-P*q = d) (hd : d*d = 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hreturn : ((m : ℝ)*alpha-a)*((Q : ℝ)*alpha-P) < 0)
    (hclose : |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p|) :
    m = -Q ∧ a = -P := by
  let u := d*(a*Q-P*m)
  let v := d*(p*m-a*q)
  obtain ⟨hnum,hden⟩ := SharpAdjacentReturn.basis_coordinates p q P Q a m d hdet hd
  change u*p+v*P = a at hnum
  change u*q+v*Q = m at hden
  have herr : (m : ℝ)*alpha-a =
      (u : ℝ)*((q : ℝ)*alpha-p)+(v : ℝ)*((Q : ℝ)*alpha-P) := by
    rw [← hden,← hnum]
    push_cast
    ring
  have hlo : -Q-D ≤ u*q+v*Q := by rw [hden]; exact hlow
  have hhi : u*q+v*Q ≤ D := by rw [hden]; exact hupp
  rw [herr] at hreturn hclose
  obtain ⟨hu,hv⟩ := signed_coordinates q Q D u v
    ((q : ℝ)*alpha-p) ((Q : ℝ)*alpha-P) hq hqQ hD hlo hhi hsigns hreturn hclose
  constructor
  · rw [← hden,hu,hv]
    ring
  · rw [← hnum,hu,hv]
    ring

/-- The width guard cannot be replaced by D<=q in this general interface. -/
theorem width_endpoint_control :
    let alpha : ℝ := 7/10
    let p : Int := 1
    let q : Int := 1
    let P : Int := 1
    let Q : Int := 2
    let D : Int := 1
    let m : Int := -3
    let a : Int := -2
    p*Q-P*q = 1 ∧ 0 < q ∧ q ≤ Q ∧ D = q ∧
      -Q-D ≤ m ∧ m ≤ D ∧
      ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0 ∧
      ((m : ℝ)*alpha-a)*((Q : ℝ)*alpha-P) < 0 ∧
      |(m : ℝ)*alpha-a| < |(q : ℝ)*alpha-p| ∧ m ≠ -Q := by
  norm_num

end OppositeArcStrip

/- Component: OppositeCarryArcs; proof body retained from the release-checked integration. -/
namespace OppositeCarryArcs

/-- Coefficient one makes the two opposite arc lengths add to the preceding error. -/
theorem error_sizes (previous current next : ℝ)
    (hrec : next = current+previous)
    (hprev : previous*current < 0) (hnext : current*next < 0) :
    |current|+|next| = |previous| := by
  by_cases hpos : 0 < current
  · have hp : previous < 0 := by
      by_contra hnot
      have h := mul_nonneg (le_of_not_gt hnot) hpos.le
      linarith
    have hn : next < 0 := by
      by_contra hnot
      have h := mul_nonneg hpos.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_pos hpos,abs_of_neg hn,abs_of_neg hp]
    linarith
  · have hneg : current < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · rw [h,mul_zero] at hprev
        exact False.elim ((lt_irrefl 0) hprev)
    have hp : 0 < previous := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos (le_of_not_gt hnot) hneg.le
      linarith
    have hn : 0 < next := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos hneg.le (le_of_not_gt hnot)
      linarith
    rw [abs_of_neg hneg,abs_of_pos hn,abs_of_pos hp]
    linarith

/-- Signed time differences do not need a preliminary ordering of the visits. -/
theorem phase_difference (alpha theta : ℝ) (h k : Nat) :
    (((h : Int)-(k : Int) : Int) : ℝ)*alpha-
        ((MechanicalCarry.level alpha theta h-MechanicalCarry.level alpha theta k : Int) : ℝ) =
      Int.fract (theta+(h : ℝ)*alpha)-Int.fract (theta+(k : ℝ)*alpha) := by
  unfold MechanicalCarry.level
  push_cast
  nlinarith [Int.floor_add_fract (theta+(h : ℝ)*alpha),
    Int.floor_add_fract (theta+(k : ℝ)*alpha)]

/-- Opposite actual carry visits straddle zero on the circle. Choosing the
integer lift on the other side of that cut retains a strict signed error. -/
theorem error_witness (alpha theta : ℝ) (q Q : Nat) (p P : Int) (h k : Nat)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (Hlo : -1 < (Q : ℝ)*alpha-P) (Hhi : (Q : ℝ)*alpha-P < 1)
    (hsigns : ((q : ℝ)*alpha-p)*((Q : ℝ)*alpha-P) < 0)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta Q P k ≠ 0) :
    ∃ a : Int,
      ((((h : Int)-(k : Int) : Int) : ℝ)*alpha-a)*((q : ℝ)*alpha-p) < 0 ∧
      |(((h : Int)-(k : Int) : Int) : ℝ)*alpha-a| <
        |(q : ℝ)*alpha-p|+|(Q : ℝ)*alpha-P| := by
  let A : Int := MechanicalCarry.level alpha theta h-MechanicalCarry.level alpha theta k
  have heq := phase_difference alpha theta h k
  change (((h : Int)-(k : Int) : Int) : ℝ)*alpha-(A : ℝ) = _ at heq
  push_cast at heq
  by_cases hpos : 0 < (q : ℝ)*alpha-p
  · have Hneg : (Q : ℝ)*alpha-P < 0 := by
      by_contra hnot
      have h := mul_nonneg hpos.le (le_of_not_gt hnot)
      linarith
    have hx := (MechanicalCarry.nonzero_positive alpha theta q p h hpos hhi).mp hh
    have hy := (MechanicalCarry.nonzero_negative alpha theta Q P k Hlo Hneg).mp hk
    have herror : (((h : Int)-(k : Int) : Int) : ℝ)*alpha-((A+1 : Int) : ℝ) < 0 := by
      push_cast
      linarith [Int.fract_lt_one (theta+(h : ℝ)*alpha),
        Int.fract_nonneg (theta+(k : ℝ)*alpha)]
    refine ⟨A+1,mul_neg_of_neg_of_pos herror hpos,?_⟩
    rw [abs_of_neg herror,abs_of_pos hpos,abs_of_neg Hneg]
    push_cast
    linarith
  · have hneg : (q : ℝ)*alpha-p < 0 := by
      rcases lt_or_eq_of_le (le_of_not_gt hpos) with h | h
      · exact h
      · rw [h,zero_mul] at hsigns
        exact False.elim ((lt_irrefl 0) hsigns)
    have Hpos : 0 < (Q : ℝ)*alpha-P := by
      by_contra hnot
      have h := mul_nonneg_of_nonpos_of_nonpos hneg.le (le_of_not_gt hnot)
      linarith
    have hx := (MechanicalCarry.nonzero_negative alpha theta q p h hlo hneg).mp hh
    have hy := (MechanicalCarry.nonzero_positive alpha theta Q P k Hpos Hhi).mp hk
    have herror : 0 < (((h : Int)-(k : Int) : Int) : ℝ)*alpha-((A-1 : Int) : ℝ) := by
      push_cast
      linarith [Int.fract_nonneg (theta+(h : ℝ)*alpha),
        Int.fract_lt_one (theta+(k : ℝ)*alpha)]
    refine ⟨A-1,mul_neg_of_pos_of_neg herror hneg,?_⟩
    rw [abs_of_pos herror,abs_of_neg hneg,abs_of_pos Hpos]
    push_cast
    linarith

/-- The exact selected-visit shift, with actual carries and no first-visit
operator. The caller supplies the coefficient-one error-size identity. -/
theorem visit_shift (alpha theta : ℝ) (previous q next : Nat) (pPrevious p pNext d D : Int)
    (h k : Nat) (hprevious : 0 < previous) (hq : previous ≤ q) (hD : D < previous)
    (hlow : -(q : Int)-D ≤ (h : Int)-(k : Int))
    (hupp : (h : Int)-(k : Int) ≤ D)
    (hdet : pPrevious*(q : Int)-p*(previous : Int) = d) (hd : d*d = 1)
    (hprevsign : ((previous : ℝ)*alpha-pPrevious)*((q : ℝ)*alpha-p) < 0)
    (hnextsign : ((q : ℝ)*alpha-p)*((next : ℝ)*alpha-pNext) < 0)
    (hsize : |(q : ℝ)*alpha-p|+|(next : ℝ)*alpha-pNext| =
      |(previous : ℝ)*alpha-pPrevious|)
    (hlo : -1 < (q : ℝ)*alpha-p) (hhi : (q : ℝ)*alpha-p < 1)
    (Hlo : -1 < (next : ℝ)*alpha-pNext) (Hhi : (next : ℝ)*alpha-pNext < 1)
    (hh : MechanicalCarry.carry alpha theta q p h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta next pNext k ≠ 0) : k = h+q := by
  obtain ⟨a,hsign,hclose⟩ := error_witness alpha theta q next p pNext h k hlo hhi Hlo Hhi
    hnextsign hh hk
  rw [hsize] at hclose
  have hexact := OppositeArcStrip.exact_negative_return alpha pPrevious (previous : Int)
    p (q : Int) a ((h : Int)-(k : Int)) d D (by exact_mod_cast hprevious)
    (by exact_mod_cast hq) hD hlow hupp hdet hd
    (by exact_mod_cast hprevsign) (by exact_mod_cast hsign) (by exact_mod_cast hclose)
  have hshift := hexact.1
  omega

end OppositeCarryArcs

/- Component: ActualOppositeCarry; proof body retained from the release-checked integration. -/
namespace FiniteHorizonActualOpposite

open FiniteHorizonContinuants
open Rule30Equivalents.Lagrange

/-- Numerator recurrence in the same offset convention as the actual denominators. -/
theorem numerator_recurrence (alpha : ℝ) (n : Nat) :
    numerator alpha (n+2) = digit alpha (n+2)*numerator alpha (n+1)+numerator alpha n := by
  rfl

/-- Coefficient one gives an exact signed-error sum, rather than an assumed arc-size relation. -/
theorem error_recurrence {alpha : ℝ} (ha : Irrational alpha) (n : Nat)
    (hone : digit alpha (n+2) = 1) :
    error alpha (n+2) = error alpha (n+1)+error alpha n := by
  have hnum : numerator alpha (n+2) = numerator alpha (n+1)+numerator alpha n := by
    rw [numerator_recurrence,hone]
    ring
  have hden : ArcRotation.denominator alpha (n+2) =
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
    rw [FiniteHorizonContinuantSequence.denominator_recurrence ha n,hone]
    simp
  unfold error
  rw [hnum,hden]
  push_cast
  ring

/-- The opposite carry-arc lengths add to the actual preceding error. -/
theorem error_sizes {alpha : ℝ} (ha : Irrational alpha) (n : Nat)
    (hone : digit alpha (n+2) = 1) :
    |error alpha (n+1)|+|error alpha (n+2)| = |error alpha n| := by
  exact OppositeCarryArcs.error_sizes (error alpha n) (error alpha (n+1))
    (error alpha (n+2)) (error_recurrence ha n hone)
    (adjacent_errors_opposite ha n) (by simpa only [Nat.add_assoc] using adjacent_errors_opposite ha (n+1))

/-- Actual selected carries at successive usable scales differ by the current denominator.
The two finite recurrence conclusions derive both spatial strip bounds. -/
theorem visit_shift (alpha theta : ℝ) (ha : Irrational alpha) (n C h k : Nat)
    (hone : digit alpha (n+2) = 1) (hnextone : digit alpha (n+3) = 1)
    (hlarge : 2*C+6 < ArcRotation.denominator alpha n)
    (hlow : ArcRotation.denominator alpha (n+2) ≤
      h+ArcRotation.denominator alpha (n+1)+C+4)
    (hupp : h ≤ ArcRotation.denominator alpha (n+1)+C+2)
    (klow : ArcRotation.denominator alpha (n+3) ≤
      k+ArcRotation.denominator alpha (n+2)+C+4)
    (kupp : k ≤ ArcRotation.denominator alpha (n+2)+C+2)
    (hh : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha (n+1))
      (numerator alpha (n+1)) h ≠ 0)
    (hk : MechanicalCarry.carry alpha theta (ArcRotation.denominator alpha (n+2))
      (numerator alpha (n+2)) k ≠ 0) :
    k = h+ArcRotation.denominator alpha (n+1) := by
  have hrec : ArcRotation.denominator alpha (n+2) =
      ArcRotation.denominator alpha (n+1)+ArcRotation.denominator alpha n := by
    rw [FiniteHorizonContinuantSequence.denominator_recurrence ha n,hone]
    simp
  have hnextrec : ArcRotation.denominator alpha (n+3) =
      ArcRotation.denominator alpha (n+2)+ArcRotation.denominator alpha (n+1) := by
    have hr := FiniteHorizonContinuantSequence.denominator_recurrence ha (n+1)
    rw [show n+1+2 = n+3 by omega,hnextone] at hr
    simpa only [Int.toNat_one,one_mul] using hr
  obtain ⟨hstriplo,hstriphi⟩ := OppositeArcStrip.visit_difference_bounds C
    (ArcRotation.denominator alpha n) (ArcRotation.denominator alpha (n+1))
    (ArcRotation.denominator alpha (n+2)) (ArcRotation.denominator alpha (n+3))
    h k hrec hnextrec hlow hupp klow kupp
  let d := numerator alpha n*(ArcRotation.denominator alpha (n+1) : Int)-
    numerator alpha (n+1)*(ArcRotation.denominator alpha n : Int)
  have hd : d*d = 1 := adjacent_determinant_unit ha n
  have hc := abs_lt.mp (error_abs_lt_one ha (n+1))
  have hn := abs_lt.mp (error_abs_lt_one ha (n+2))
  apply OppositeCarryArcs.visit_shift alpha theta (ArcRotation.denominator alpha n)
    (ArcRotation.denominator alpha (n+1)) (ArcRotation.denominator alpha (n+2))
    (numerator alpha n) (numerator alpha (n+1)) (numerator alpha (n+2)) d (2*(C : Int)+6)
    h k (ArcRotation.denominator_pos ha n)
    (FiniteHorizonContinuantSequence.denominator_successive ha n)
    (by exact_mod_cast hlarge) hstriplo hstriphi rfl hd
  · simpa only [error] using adjacent_errors_opposite ha n
  · simpa only [error,Nat.add_assoc] using adjacent_errors_opposite ha (n+1)
  · simpa only [error] using error_sizes ha n hone
  · exact hc.1
  · exact hc.2
  · exact hn.1
  · exact hn.2
  · exact hh
  · exact hk

end FiniteHorizonActualOpposite

/- Component: UniformHorizon; proof body retained from the release-checked integration. -/
namespace UniformHorizon

open FiniteHorizonContinuants
open Rule30Equivalents.Lagrange

/-- Coefficient forcing: the growth bound at scale `m+1` and a large denominator at scale `m` give `digit (m+2) = 1`. -/
theorem digit_eq_one {alpha : ℝ} (ha : Irrational alpha) (C m : Nat)
    (hgrowth : ArcRotation.denominator alpha (m+2) ≤ 2*ArcRotation.denominator alpha (m+1)+2*C+6)
    (hprev : 2*C+6 < ArcRotation.denominator alpha m) :
    digit alpha (m+2) = 1 := by
  have hpos : 1 ≤ digit alpha (m+2) := one_le_digit ha (m+1)
  have hnat : (digit alpha (m+2)).toNat = 1 :=
    FiniteHorizonSelection.coefficient_one C (digit alpha (m+2)).toNat
      (ArcRotation.denominator alpha (m+1)) (ArcRotation.denominator alpha m)
      (ArcRotation.denominator alpha (m+2))
      (by omega) (FiniteHorizonContinuantSequence.denominator_recurrence ha m) hgrowth hprev
  omega

/-- A unit coefficient makes the next denominator the sum of the previous two. -/
theorem recurrence_one {alpha : ℝ} (ha : Irrational alpha) (m : Nat) (hone : digit alpha (m+2) = 1) :
    ArcRotation.denominator alpha (m+2) =
      ArcRotation.denominator alpha (m+1)+ArcRotation.denominator alpha m := by
  rw [FiniteHorizonContinuantSequence.denominator_recurrence ha m, hone]
  simp

/-- **G135, statement 1.** No finite repeat bound with constant `C` survives through `251*(C+4)`. -/
theorem uniform_horizon (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (MechanicalCarry.mech alpha theta) (251*(C+4)) C := by
  intro hr
  -- the initial crossing q_r ≤ T < q_(r+1), T = 2C+8
  obtain ⟨r, hr0, hr1⟩ := FiniteHorizonContinuantSequence.threshold_crossing ha C
  -- every growth step whose input deadline fits
  have hg : ∀ n, DenominatorBootstrap.GrowthAt (251*(C+4)) C (ArcRotation.denominator alpha n)
      (ArcRotation.denominator alpha (n+1)) := by
    intro n hdl
    obtain ⟨_, _, _, _, h⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha (251*(C+4)) C n hr hdl
    exact h
  -- the four-step budget, from q_r ≤ T
  have hb := DenominatorBootstrap.four_steps C (ArcRotation.denominator alpha r)
    (ArcRotation.denominator alpha (r+1)) (ArcRotation.denominator alpha (r+2))
    (ArcRotation.denominator alpha (r+3)) (ArcRotation.denominator alpha (r+4)) hr0
    (hg r) (hg (r+1)) (hg (r+2)) (hg (r+3))
  obtain ⟨_, hb2, hb3, hb4, _⟩ := hb
  -- monotone denominators, restated with canonical indices
  have hm1 : ArcRotation.denominator alpha (r+1) ≤ ArcRotation.denominator alpha (r+2) :=
    FiniteHorizonContinuantSequence.denominator_successive ha (r+1)
  have hm2 : ArcRotation.denominator alpha (r+2) ≤ ArcRotation.denominator alpha (r+3) :=
    FiniteHorizonContinuantSequence.denominator_successive ha (r+2)
  -- three selected visits, at the scales r+2, r+3 and r+4 (the third is the fifth growth call)
  obtain ⟨h2, hz2, hu2, hl2, hgr2⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+2) hr (by omega)
  obtain ⟨h3, hz3, hu3, hl3, hgr3⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+3) hr (by omega)
  obtain ⟨h4, hz4, hu4, hl4, hgr4⟩ := FiniteHorizonActualCarry.denominator_growth alpha theta ha
    (251*(C+4)) C (r+4) hr (by omega)
  have hl2' : ArcRotation.denominator alpha (r+3) ≤ h2+ArcRotation.denominator alpha (r+2)+C+4 := hl2
  have hl3' : ArcRotation.denominator alpha (r+4) ≤ h3+ArcRotation.denominator alpha (r+3)+C+4 := hl3
  have hl4' : ArcRotation.denominator alpha (r+5) ≤ h4+ArcRotation.denominator alpha (r+4)+C+4 := hl4
  have hgr2' : ArcRotation.denominator alpha (r+3) ≤ 2*ArcRotation.denominator alpha (r+2)+2*C+6 := hgr2
  have hgr3' : ArcRotation.denominator alpha (r+4) ≤ 2*ArcRotation.denominator alpha (r+3)+2*C+6 := hgr3
  have hgr4' : ArcRotation.denominator alpha (r+5) ≤ 2*ArcRotation.denominator alpha (r+4)+2*C+6 := hgr4
  -- coefficient forcing at the three scales
  have hd3 : digit alpha (r+3) = 1 := digit_eq_one ha C (r+1) hgr2' (by omega)
  have hd4 : digit alpha (r+4) = 1 := digit_eq_one ha C (r+2) hgr3' (by omega)
  have hd5 : digit alpha (r+5) = 1 := digit_eq_one ha C (r+3) hgr4' (by omega)
  have hrec3 : ArcRotation.denominator alpha (r+3) =
      ArcRotation.denominator alpha (r+2)+ArcRotation.denominator alpha (r+1) := recurrence_one ha (r+1) hd3
  have hrec4 : ArcRotation.denominator alpha (r+4) =
      ArcRotation.denominator alpha (r+3)+ArcRotation.denominator alpha (r+2) := recurrence_one ha (r+2) hd4
  -- the two exact opposite-arc shifts
  have hs1 : h3 = h2+ArcRotation.denominator alpha (r+2) :=
    FiniteHorizonActualOpposite.visit_shift alpha theta ha (r+1) C h2 h3 hd3 hd4 (by omega)
      hl2' hu2 hl3' hu3 hz2 hz3
  have hs2 : h4 = h3+ArcRotation.denominator alpha (r+3) :=
    FiniteHorizonActualOpposite.visit_shift alpha theta ha (r+2) C h3 h4 hd4 hd5 (by omega)
      hl3' hu3 hl4' hu4 hz3 hz4
  -- the final contradiction: q_(r+1) ≤ 2C+6, against q_(r+1) > 2C+8
  exact DenominatorBootstrap.final_visit_contradiction C (ArcRotation.denominator alpha (r+1))
    (ArcRotation.denominator alpha (r+2)) (ArcRotation.denominator alpha (r+3))
    (ArcRotation.denominator alpha (r+4)) h2 h3 h4 hr1 hrec4 (by omega) hu4 hs1 hs2

/-- **G135, statement 1, as an explicit witness** (the GC2133 form). -/
theorem uniform_horizon_witness (alpha theta : ℝ) (ha : Irrational alpha) (C : Nat) :
    ∃ q a b, 0 < q ∧ a ≤ b ∧ b+q ≤ 251*(C+4) ∧
      (∀ s, a ≤ s → s ≤ b → MechanicalCarry.mech alpha theta (s+q) = MechanicalCarry.mech alpha theta s) ∧
      2*a+q+C < b := by
  by_contra hno
  apply uniform_horizon alpha theta ha C
  intro q a b hq hab hN heq
  by_contra hbig
  exact hno ⟨q, a, b, hq, hab, hN, heq, by omega⟩

end UniformHorizon

/- Component: RecodedHorizon; proof body retained from the release-checked integration. -/
namespace RecodedHorizon

open MechanicalCarry

/-- The finite repeat bound sees only the prefix through `N`. -/
theorem repeat_bound_congr {β : Type} (c d : Nat → β) (N C : Nat) (hcd : ∀ s, s ≤ N → c s = d s)
    (h : FiniteHorizonBounds.RepeatBoundThrough c N C) : FiniteHorizonBounds.RepeatBoundThrough d N C := by
  intro q a b hq hab hN heq
  apply h q a b hq hab hN
  intro s hs1 hs2
  rw [hcd (s+q) (by omega), hcd s (by omega)]
  exact heq s hs1 hs2

/-- A positive margin below finitely many positive numbers. -/
theorem finite_margin (f : Nat → ℝ) (hf : ∀ s, 0 < f s) :
    ∀ n, ∃ δ, 0 < δ ∧ ∀ s, s ≤ n → δ ≤ f s
  | 0 => ⟨f 0, hf 0, fun s hs => by
      have hs0 : s = 0 := by omega
      subst hs0
      exact le_refl _⟩
  | n+1 => by
    obtain ⟨δ, hδ, hle⟩ := finite_margin f hf n
    refine ⟨min δ (f (n+1)), lt_min hδ (hf (n+1)), fun s hs => ?_⟩
    by_cases h : s ≤ n
    · exact le_trans (min_le_left _ _) (hle s h)
    · have hsn : s = n+1 := by omega
      subst hsn
      exact min_le_right _ _

/-- Right-continuity of the floor: a small nonnegative push keeps it. -/
theorem floor_stable (x d : ℝ) (h0 : 0 ≤ d) (h1 : d < (⌊x⌋ : ℝ)+1-x) : ⌊x+d⌋ = ⌊x⌋ := by
  rw [Int.floor_eq_iff]
  constructor
  · linarith [Int.floor_le x]
  · linarith

/-- Every finite stretch of floors along a real slope is matched along an irrational slope. -/
theorem exists_irrational_agree (alpha theta : ℝ) (n : Nat) :
    ∃ beta, Irrational beta ∧ ∀ s, s ≤ n → level beta theta s = level alpha theta s := by
  by_cases hα : Irrational alpha
  · exact ⟨alpha, hα, fun _ _ => rfl⟩
  · have hmem : alpha ∈ Set.range ((↑) : ℚ → ℝ) := by
      unfold Irrational at hα
      exact not_not.mp hα
    obtain ⟨r, hr⟩ := hmem
    let f : Nat → ℝ := fun s => (⌊theta+(s : ℝ)*alpha⌋ : ℝ)+1-(theta+(s : ℝ)*alpha)
    have hf : ∀ s, 0 < f s := fun s => by
      have := Int.lt_floor_add_one (theta+(s : ℝ)*alpha)
      show 0 < (⌊theta+(s : ℝ)*alpha⌋ : ℝ)+1-(theta+(s : ℝ)*alpha)
      linarith
    obtain ⟨δ, hδ, hle⟩ := finite_margin f hf n
    have hn : (0 : ℝ) < (n : ℝ)+1 := by positivity
    obtain ⟨ε, hεirr, hε0, hε1⟩ := exists_irrational_btwn (div_pos hδ hn)
    refine ⟨alpha+ε, ?_, fun s hs => ?_⟩
    · rw [← hr, add_comm]
      exact hεirr.add_ratCast r
    · unfold level
      have hsR : (s : ℝ) ≤ (n : ℝ) := by exact_mod_cast hs
      have hpush : (s : ℝ)*ε < f s := by
        have h1 : (s : ℝ)*ε ≤ (n : ℝ)*ε := mul_le_mul_of_nonneg_right hsR hε0.le
        have h2 : ((n : ℝ)+1)*ε < δ := by
          rw [lt_div_iff₀ hn] at hε1
          linarith
        have h3 := hle s hs
        nlinarith
      have hnonneg : (0 : ℝ) ≤ (s : ℝ)*ε := mul_nonneg (Nat.cast_nonneg s) hε0.le
      have hrw : theta+(s : ℝ)*(alpha+ε) = (theta+(s : ℝ)*alpha)+(s : ℝ)*ε := by ring
      rw [hrw]
      exact floor_stable _ _ hnonneg hpush

/-- **Statement 1 for every real slope.** -/
theorem uniform_horizon_all (alpha theta : ℝ) (C : Nat) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (mech alpha theta) (251*(C+4)) C := by
  obtain ⟨beta, hbeta, hagree⟩ := exists_irrational_agree alpha theta (251*(C+4)+1)
  intro hr
  apply UniformHorizon.uniform_horizon beta theta hbeta C
  apply repeat_bound_congr (mech alpha theta) (mech beta theta) _ _ _ hr
  intro s hs
  unfold mech
  rw [hagree (s+1) (by omega), hagree s (by omega)]

/-- A recoding of width `w+1`: each output reads the `w+1` letters starting at `s`. -/
def recode {β : Type} (w : Nat) (F : (Fin (w+1) → Int) → β) (g : Nat → Int) (s : Nat) : β :=
  F (fun i => g (s+i))

/-- **Statement 2 (G136).** Any recoding of width `w+1` violates the bound through `251*(C+4)+250*w`. -/
theorem recoded_horizon {β : Type} (alpha theta : ℝ) (C w : Nat) (F : (Fin (w+1) → Int) → β) :
    ¬ FiniteHorizonBounds.RepeatBoundThrough (recode w F (mech alpha theta)) (251*(C+4)+250*w) C := by
  intro hr
  apply uniform_horizon_all alpha theta (C+w)
  intro q a e hq _hae hN heq
  apply Classical.byContradiction
  intro hbig
  have hc := hr q a (e-w) hq (by omega) (by omega) (fun s hs1 hs2 => by
    unfold recode
    congr 1
    funext i
    have hi := i.isLt
    rw [show s+q+(i : Nat) = s+(i : Nat)+q by omega]
    exact heq (s+(i : Nat)) (by omega) (by omega))
  omega

end RecodedHorizon

/- Component: ArcRule30BridgeDraft; proof body retained from the release-checked integration. -/
namespace ArcRule30Bridge

open Ruliology.CellularAutomata Rule30Realization

/-- The neighbour on the clock's white (even) physical times. -/
def visible (x : Int → Bool) (s : Nat) : Bool := evol x (2*s) 1

/-- The current kit's window reconstruction supplies the uniform constant C=L at every positive lag. -/
theorem repeat_bound (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) (q : Nat) (hq : 0 < q) :
    ArcBreakSequence.RepeatBound (visible x) q L := by
  intro a b hab hmatch
  by_cases hbound : b ≤ 2*a+q+L
  · exact hbound
  · have hbad : 2*a+q+L < b := by omega
    let m := L+2*(a+q)
    have hc : ∀ s : Nat, s ≤ m → evol x (2*a+s) 0 = evol x (2*(a+q)+s) 0 := by
      intro s _
      have hp : (2*a+s) % 2 = (2*(a+q)+s) % 2 := by omega
      rw [hclock,hclock,hp]
    have he : ∀ s : Nat, s < m →
        Rule30FiniteMaskedJen.orCol x 0 (2*a+s) = Rule30FiniteMaskedJen.orCol x 0 (2*(a+q)+s) := by
      intro s hs
      by_cases hseven : s % 2 = 0
      · let k := s/2
        have hsk : 2*k = s := by dsimp [k]; omega
        have haTime : 2*a+s = 2*(a+k) := by omega
        have hbTime : 2*(a+q)+s = 2*((a+k)+q) := by omega
        have hkbound : a+k ≤ b := by
          have hs' : s < L+2*(a+q) := hs
          omega
        have hv := hmatch (a+k) (by omega) hkbound
        have heva : evol x (2*a+s) 0 = false := by
          rw [hclock]
          have hp : (2*a+s) % 2 = 0 := by omega
          simp [hp]
        have hevb : evol x (2*(a+q)+s) 0 = false := by
          rw [hclock]
          have hp : (2*(a+q)+s) % 2 = 0 := by omega
          simp [hp]
        unfold Rule30FiniteMaskedJen.orCol
        rw [heva,hevb]
        change evol x (2*a+s) 1 = evol x (2*(a+q)+s) 1
        rw [haTime,hbTime]
        exact hv.symm
      · have hsodd : s % 2 = 1 := by omega
        have heva : evol x (2*a+s) 0 = true := by
          rw [hclock]
          have hp : (2*a+s) % 2 = 1 := by omega
          simp [hp]
        have hevb : evol x (2*(a+q)+s) 0 = true := by
          rw [hclock]
          have hp : (2*(a+q)+s) % 2 = 1 := by omega
          simp [hp]
        simp only [Rule30FiniteMaskedJen.orCol,heva,hevb,Bool.true_or]
    exact False.elim (Rule30FiniteMaskedJen.window_jen_col hleft hzero
      (t₁ := 2*a) (t₂ := 2*(a+q)) (i := 0) m (by omega) (by dsimp [m]; omega) hc he)

end ArcRule30Bridge

/- Component: PhysicalHorizon; proof body retained from the release-checked integration. -/
namespace PhysicalHorizon

open Ruliology.CellularAutomata Rule30Realization Rule30Jen

/-- Restarting at the even time `2a` shifts the visible companion by `a`. -/
theorem restart_visible (x : Int → Bool) (a s : Nat) :
    ArcRule30Bridge.visible (evol x (2*a)) s = ArcRule30Bridge.visible x (a+s) := by
  unfold ArcRule30Bridge.visible
  rw [Rule30WhiteEnd.evol_add, show 2*a+2*s = 2*(a+s) by omega]

/-- An even restart keeps the clock's phase. -/
theorem restart_clock (x : Int → Bool) (a : Nat)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∀ t : Nat, evol (evol x (2*a)) t 0 = decide (t % 2 = 1) := by
  intro t
  rw [Rule30WhiteEnd.evol_add, hclock, show (2*a+t) % 2 = t % 2 by omega]

/-- The white left tail moves left by at most one cell per step. -/
theorem restart_left_zero (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false) :
    ∀ i : Int, i < -((L+2*a : Nat) : Int) → evol x (2*a) i = false := by
  intro i hi
  exact Rule30FiniteConfigs.evol_eq_false_of_lt hzero (2*a) i (by push_cast at hi ⊢; omega)

/-- The clock forces a black cell in `[-(L+2a), -1]` at the restart time: a row white at every cell `≤ 0` would make
column `0` black at the restarted time `2`, against the clock. -/
theorem restart_has_black (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∃ k : Nat, k < L+2*a ∧ evol x (2*a) (-((L+2*a : Nat) : Int)+k) = true := by
  apply Classical.byContradiction
  intro hno
  have hno' : ∀ k : Nat, k < L+2*a → evol x (2*a) (-((L+2*a : Nat) : Int)+k) = false := by
    intro k hk
    have h := fun h' => hno ⟨k, hk, h'⟩
    simpa using h
  have hc := restart_clock x a hclock
  have hy : ∀ i : Int, i ≤ 0 → evol x (2*a) i = false := by
    intro i hi
    by_cases hlow : i < -((L+2*a : Nat) : Int)
    · exact restart_left_zero x L a hzero i hlow
    · by_cases hz : i = 0
      · subst hz
        exact hc 0
      · have hk := hno' (Int.toNat (i+((L+2*a : Nat) : Int))) (by omega)
        rw [show -((L+2*a : Nat) : Int)+((Int.toNat (i+((L+2*a : Nat) : Int)) : Nat) : Int) = i by omega] at hk
        exact hk
  have hm1 : evol x (2*a) (-1) = false := hy (-1) (by norm_num)
  have hm2 : evol x (2*a) (-2) = false := hy (-2) (by norm_num)
  have h00 : evol x (2*a) 0 = false := hy 0 le_rfl
  have he1 : evol (evol x (2*a)) 1 (-1) = false := by
    show rule (evol x (2*a) (-1-1)) (evol x (2*a) (-1)) (evol x (2*a) (-1+1)) = false
    rw [show (-1 : Int)-1 = -2 by norm_num, show (-1 : Int)+1 = 0 by norm_num, hm2, hm1, h00]
    rfl
  have he0 : evol (evol x (2*a)) 1 0 = true := hc 1
  have he2 : evol (evol x (2*a)) 2 0 = true := by
    show rule (evol (evol x (2*a)) 1 (0-1)) (evol (evol x (2*a)) 1 0) (evol (evol x (2*a)) 1 (0+1)) = true
    rw [show (0 : Int)-1 = -1 by norm_num, he1, he0]
    simp [rule]
  have hc2 := hc 2
  rw [he2] at hc2
  exact absurd hc2 (by decide)

/-- The restarted row has a leftmost black cell at some `-L'` with `1 ≤ L' ≤ L+2a`. -/
theorem restart_leftmost (x : Int → Bool) (L a : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1)) :
    ∃ L' : Nat, 1 ≤ L' ∧ L' ≤ L+2*a ∧ evol x (2*a) (-(L' : Int)) = true ∧
      ∀ i : Int, i < -(L' : Int) → evol x (2*a) i = false := by
  classical
  have hex := restart_has_black x L a hzero hclock
  have hk := Nat.find_spec hex
  refine ⟨L+2*a-Nat.find hex, by omega, by omega, ?_, ?_⟩
  · rw [show -(((L+2*a-Nat.find hex : Nat) : Int)) = -((L+2*a : Nat) : Int)+((Nat.find hex : Nat) : Int) by
      have := hk.1
      omega]
    exact hk.2
  · intro i hi
    by_cases hlow : i < -((L+2*a : Nat) : Int)
    · exact restart_left_zero x L a hzero i hlow
    · have hlt : Int.toNat (i+((L+2*a : Nat) : Int)) < Nat.find hex := by omega
      have hm := Nat.find_min hex hlt
      rw [show -((L+2*a : Nat) : Int)+((Int.toNat (i+((L+2*a : Nat) : Int)) : Nat) : Int) = i by omega] at hm
      have hbound : Int.toNat (i+((L+2*a : Nat) : Int)) < L+2*a := by
        have := hk.1
        omega
      have hn := not_and.mp hm hbound
      simpa using hn

/-- **Statement 3, one matching piece.** -/
theorem piece_bound (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (a b : Nat)
    (hmatch : ∀ i, i ≤ b-a → ArcRule30Bridge.visible x (a+i) =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) :
    b-a < 251*(L+2*a+4)+250*w := by
  apply Classical.byContradiction
  intro hbig
  obtain ⟨L', _, hL', hl, hz⟩ := restart_leftmost x L a hzero hclock
  apply RecodedHorizon.recoded_horizon alpha theta (L+2*a) w F
  intro q c d hq hcd hN heq
  have hv : ∀ i, i ≤ 251*(L+2*a+4)+250*w →
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i =
        ArcRule30Bridge.visible (evol x (2*a)) i := by
    intro i hi
    rw [restart_visible, hmatch i (by omega)]
  have hrb := ArcRule30Bridge.repeat_bound (evol x (2*a)) L' hl hz (restart_clock x a hclock) q hq c d hcd
    (fun s hs1 hs2 => by
      rw [← hv (s+q) (by omega), ← hv s (by omega)]
      exact heq s hs1 hs2)
  omega

/-- A mechanical word read from `m` is the mechanical word of the shifted phase. -/
theorem mech_shift (alpha theta : ℝ) (m s : Nat) :
    MechanicalCarry.mech alpha theta (m+s) = MechanicalCarry.mech alpha (theta+(m : ℝ)*alpha) s := by
  unfold MechanicalCarry.mech MechanicalCarry.level
  congr 1 <;> (congr 1; push_cast; ring)

/-- **The reset recursion.** A piece `[t, t'-1]` matching a recoded mechanical word gives the next reset bound. -/
theorem reset_step (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (t t' : Nat)
    (hmatch : ∀ i, i ≤ t'-1-t → ArcRule30Bridge.visible x (t+i) =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) i) :
    t' ≤ 503*t+251*L+1004+250*w := by
  have h := piece_bound x L hzero hclock alpha theta w F t (t'-1) hmatch
  omega

/-- **The first disagreement** against one fixed recoded mechanical word. -/
theorem first_disagreement (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k : Nat)
    (hagree : ∀ s, s < k → ArcRule30Bridge.visible x s =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) :
    k ≤ 251*(L+4)+250*w := by
  by_cases hk : k = 0
  · omega
  · have h := piece_bound x L hzero hclock alpha theta w F 0 (k-1)
      (fun i hi => by rw [Nat.zero_add]; exact hagree i (by omega))
    omega

/-- **The disagreement recursion** against one fixed recoded mechanical word. -/
theorem disagreement_step (x : Int → Bool) (L : Nat)
    (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, evol x t 0 = decide (t % 2 = 1))
    (alpha theta : ℝ) (w : Nat) (F : (Fin (w+1) → Int) → Bool) (k k' : Nat)
    (hagree : ∀ s, k < s → s < k' → ArcRule30Bridge.visible x s =
      RecodedHorizon.recode w F (MechanicalCarry.mech alpha theta) s) :
    k' ≤ 503*k+251*L+1507+250*w := by
  by_cases hkk : k' ≤ k+1
  · omega
  · have h := piece_bound x L hzero hclock alpha (theta+((k+1 : Nat) : ℝ)*alpha) w F (k+1) (k'-1)
      (fun i hi => by
        rw [hagree (k+1+i) (by omega) (by omega)]
        unfold RecodedHorizon.recode
        congr 1
        funext j
        rw [show k+1+i+(j : Nat) = (k+1)+(i+(j : Nat)) by omega, mech_shift])
    omega

end PhysicalHorizon

#print axioms Rule30Submission.ArcBreakBounds.label_collision
#print axioms Rule30Submission.ArcBreakBounds.break_envelope
#print axioms Rule30Submission.ArcBreakBounds.spacing_bound
#print axioms Rule30Submission.ArcBreakBounds.next_denominator_covers_window
#print axioms Rule30Submission.ArcBreakSequence.future_break
#print axioms Rule30Submission.ArcBreakSequence.sequence_break
#print axioms Rule30Submission.ArcBreakSequence.sequence_strict
#print axioms Rule30Submission.ArcBreakSequence.labelled_spacing_bound
#print axioms Rule30Submission.ArcDeterminant.spacing_of_bezout
#print axioms Rule30Submission.ArcDeterminant.no_short_return
#print axioms Rule30Submission.ArcDeterminant.continuant_bezout
#print axioms Rule30Submission.ArcDeterminant.continuant_error_lt_next
#print axioms Rule30Submission.ArcCover.same_interval_return
#print axioms Rule30Submission.ArcCover.short_return
#print axioms Rule30Submission.ArcCover.no_repeat_of_cover
#print axioms Rule30Submission.ArcStepCode.crossing
#print axioms Rule30Submission.ArcStepCode.break_has_lift
#print axioms Rule30Submission.ArcStepCode.lift_cover
#print axioms Rule30Submission.ArcStepCode.no_repeat_bound
#print axioms Rule30Submission.ArcRotation.denominator_next
#print axioms Rule30Submission.ArcRotation.previous_margin
#print axioms Rule30Submission.ArcRotation.next_covers_window
#print axioms Rule30Submission.ArcRotation.no_repeat_at_large_digit
#print axioms Rule30Submission.ArcRotation.repeat_bound_fails
#print axioms Rule30Submission.ArcRotation.no_uniform_repeat_bound
#print axioms Rule30Submission.SharpAdjacentReturn.basis_coordinates
#print axioms Rule30Submission.SharpAdjacentReturn.positive_error_bound
#print axioms Rule30Submission.SharpAdjacentReturn.sharp_return
#print axioms Rule30Submission.SharpAdjacentReturn.same_sign_control
#print axioms Rule30Submission.SharpAdjacentReturn.endpoint_control
#print axioms Rule30Submission.MechanicalCarry.difference_identity
#print axioms Rule30Submission.MechanicalCarry.carry_as_floor
#print axioms Rule30Submission.MechanicalCarry.carry_positive
#print axioms Rule30Submission.MechanicalCarry.carry_negative
#print axioms Rule30Submission.MechanicalCarry.nonzero_positive
#print axioms Rule30Submission.MechanicalCarry.nonzero_negative
#print axioms Rule30Submission.MechanicalCarry.half_open_endpoint_controls
#print axioms Rule30Submission.FiniteHorizonBounds.future_break
#print axioms Rule30Submission.FiniteHorizonBounds.equal_of_zero_carry
#print axioms Rule30Submission.FiniteHorizonBounds.first_carry
#print axioms Rule30Submission.FiniteHorizonBounds.next_carry
#print axioms Rule30Submission.FiniteHorizonBounds.denominator_growth
#print axioms Rule30Submission.FiniteHorizonBounds.zero_horizon_control
#print axioms Rule30Submission.CarryReturnSpacing.phases_close
#print axioms Rule30Submission.CarryReturnSpacing.phase_difference
#print axioms Rule30Submission.CarryReturnSpacing.return_spacing
#print axioms Rule30Submission.FiniteHorizonContinuants.multiplier_pos
#print axioms Rule30Submission.FiniteHorizonContinuants.error_identity
#print axioms Rule30Submission.FiniteHorizonContinuants.adjacent_errors_opposite
#print axioms Rule30Submission.FiniteHorizonContinuants.adjacent_determinant_unit
#print axioms Rule30Submission.FiniteHorizonContinuants.error_abs_lt_one
#print axioms Rule30Submission.FiniteHorizonActualCarry.return_spacing
#print axioms Rule30Submission.FiniteHorizonActualCarry.denominator_growth
#print axioms Rule30Submission.DenominatorBootstrap.four_steps
#print axioms Rule30Submission.DenominatorBootstrap.final_deadline
#print axioms Rule30Submission.DenominatorBootstrap.final_visit_contradiction
#print axioms Rule30Submission.FiniteHorizonSelection.coefficient_one
#print axioms Rule30Submission.FiniteHorizonSelection.crossing_before
#print axioms Rule30Submission.FiniteHorizonSelection.crossing_scale
#print axioms Rule30Submission.FiniteHorizonSelection.successive_ge
#print axioms Rule30Submission.FiniteHorizonContinuantSequence.denominator_zero
#print axioms Rule30Submission.FiniteHorizonContinuantSequence.denominator_recurrence
#print axioms Rule30Submission.FiniteHorizonContinuantSequence.denominator_unbounded
#print axioms Rule30Submission.FiniteHorizonContinuantSequence.denominator_successive
#print axioms Rule30Submission.FiniteHorizonContinuantSequence.threshold_crossing
#print axioms Rule30Submission.OppositeArcStrip.visit_difference_bounds
#print axioms Rule30Submission.OppositeArcStrip.negative_error_coordinates
#print axioms Rule30Submission.OppositeArcStrip.signed_coordinates
#print axioms Rule30Submission.OppositeArcStrip.exact_negative_return
#print axioms Rule30Submission.OppositeArcStrip.width_endpoint_control
#print axioms Rule30Submission.OppositeCarryArcs.error_sizes
#print axioms Rule30Submission.OppositeCarryArcs.phase_difference
#print axioms Rule30Submission.OppositeCarryArcs.error_witness
#print axioms Rule30Submission.OppositeCarryArcs.visit_shift
#print axioms Rule30Submission.FiniteHorizonActualOpposite.numerator_recurrence
#print axioms Rule30Submission.FiniteHorizonActualOpposite.error_recurrence
#print axioms Rule30Submission.FiniteHorizonActualOpposite.error_sizes
#print axioms Rule30Submission.FiniteHorizonActualOpposite.visit_shift
#print axioms Rule30Submission.UniformHorizon.digit_eq_one
#print axioms Rule30Submission.UniformHorizon.recurrence_one
#print axioms Rule30Submission.UniformHorizon.uniform_horizon
#print axioms Rule30Submission.UniformHorizon.uniform_horizon_witness
#print axioms Rule30Submission.RecodedHorizon.repeat_bound_congr
#print axioms Rule30Submission.RecodedHorizon.finite_margin
#print axioms Rule30Submission.RecodedHorizon.floor_stable
#print axioms Rule30Submission.RecodedHorizon.exists_irrational_agree
#print axioms Rule30Submission.RecodedHorizon.uniform_horizon_all
#print axioms Rule30Submission.RecodedHorizon.recoded_horizon
#print axioms Rule30Submission.ArcRule30Bridge.repeat_bound
#print axioms Rule30Submission.PhysicalHorizon.restart_visible
#print axioms Rule30Submission.PhysicalHorizon.restart_clock
#print axioms Rule30Submission.PhysicalHorizon.restart_left_zero
#print axioms Rule30Submission.PhysicalHorizon.restart_has_black
#print axioms Rule30Submission.PhysicalHorizon.restart_leftmost
#print axioms Rule30Submission.PhysicalHorizon.piece_bound
#print axioms Rule30Submission.PhysicalHorizon.mech_shift
#print axioms Rule30Submission.PhysicalHorizon.reset_step
#print axioms Rule30Submission.PhysicalHorizon.first_disagreement
#print axioms Rule30Submission.PhysicalHorizon.disagreement_step

end Rule30Submission
