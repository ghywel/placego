import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.NormCast
import Rule30Equivalents.Lagrange
import Ruliology.CellularAutomata.Rule30FiniteMaskedJen
import Mathlib.NumberTheory.Real.Irrational
import Ruliology.CellularAutomata.Rule30Prize

/-!
# Finite-step irrational rotation codes excluded beside a Rule 30 clock

For an initial row with a leftmost black cell at -L and an alternating column0 from time0,
its visible neighbour evol x (2*s) 1 cannot eventually code a finite-step irrational circle
rotation whose continued-fraction digits exceed2^(r+1) arbitrarily late. Here r counts the
supplied endpoint labels; no minimality is assumed. Arbitrary changes at those endpoints
and concrete unions of k half-open intervals are included, the latter with threshold2^(2*k+1).

The proof constructs breaks from the physical window-Jen bound, labels their signed lifted
mismatch intervals, and uses a finite pigeonhole argument plus continuant determinant spacing.
The growing previous denominator pays the fixed margin at the stated digit threshold.

This is the formal delivery of the record's Theorem E-double-prime, with the finite-endpoint
extension already in G131/G132. It does not exclude all irrational rotation codings, prove an
arbitrary physical-clock restart, or solve a prize problem. Classical coding and continued-
fraction ingredients are prior art. See the companion essay for precise scope and provenance.
-/

namespace Rule30Submission

/- Component: ArcBreakBounds; proof body retained from the reviewed integration. -/
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

/- Component: ArcBreakSequence; proof body retained from the reviewed integration. -/
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

/- Component: ArcDeterminantDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcCoverDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcStepCodeDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcTailBounds; proof body retained from the reviewed integration. -/
namespace ArcTailBounds

open ArcBreakSequence

/-- Shifting the time origin by N costs only N in the repeat constant. -/
theorem shift_repeat_bound (c : Nat → Bool) (q C N : Nat) (hr : RepeatBound c q C) :
    RepeatBound (fun n => c (n+N)) q (C+N) := by
  intro a b hab hm
  have h := hr (a+N) (b+N) (by omega) (by
    intro s hs ht
    have hNs : N ≤ s := by omega
    obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hNs
    have he := hm k (by omega) (by omega)
    simpa [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using he)
  omega

/-- Finite prefix changes cost at most 2*N; the conclusion concerns the unshifted new trace. -/
theorem eventual_transfer (c d : Nat → Bool) (q C N : Nat) (hr : RepeatBound c q C)
    (he : ∀ s, N ≤ s → c s = d s) : RepeatBound d q (C+2*N) := by
  intro a b hab hm
  by_cases hb : b < N
  · omega
  have hmax : max a N ≤ b := Nat.max_le_of_le_of_le hab (by omega)
  have h := hr (max a N) b hmax (by
    intro s hs ht
    have hNs : N ≤ s := Nat.le_trans (Nat.le_max_right a N) hs
    rw [he (s+q) (by omega), he s hNs]
    exact hm s (Nat.le_trans (Nat.le_max_left a N) hs) ht)
  have hmarg : max a N ≤ a+N := Nat.max_le_of_le_of_le (by omega) (by omega)
  omega

/-- A single new constant works for every positive lag after finite changes. -/
theorem uniform_eventual_transfer (c d : Nat → Bool) (C N : Nat)
    (hr : ∀ q, 0 < q → RepeatBound c q C) (he : ∀ s, N ≤ s → c s = d s) :
    ∀ q, 0 < q → RepeatBound d q (C+2*N) := by
  intro q hq
  exact eventual_transfer c d q C N (hr q hq) he

/-- Finitely many labels, each used at most once in time, have a last-use cutoff.
    This is classical finite existence, not a bound in terms of the label count. -/
theorem finite_single_hits_cutoff (r : Nat) (P : Nat → Nat → Prop)
    (hone : ∀ i, i < r → ∀ s t, P i s → P i t → s = t) :
    ∃ N, ∀ i, i < r → ∀ n, N ≤ n → ¬ P i n := by
  classical
  induction r with
  | zero =>
    refine ⟨0,?_⟩
    intro i hi
    omega
  | succ r ih =>
    obtain ⟨N,hN⟩ := ih (fun i hi s t hs ht => hone i (by omega) s t hs ht)
    by_cases hp : ∃ k, P r k
    · obtain ⟨k,hk⟩ := hp
      refine ⟨max N (k+1),?_⟩
      intro i hi n hn hpin
      by_cases hir : i < r
      · exact hN i hir n (by omega) hpin
      · have hir : i = r := by omega
        subst i
        have he := hone r (by omega) n k hpin hk
        omega
    · refine ⟨N,?_⟩
      intro i hi n hn hpin
      by_cases hir : i < r
      · exact hN i hir n hn hpin
      · have hir : i = r := by omega
        subst i
        exact hp ⟨n,hpin⟩

/-- Changes supported on finitely many single-visit labels eventually disappear. -/
theorem finite_single_hits_eventual (c d : Nat → Bool) (r : Nat) (P : Nat → Nat → Prop)
    (hone : ∀ i, i < r → ∀ s t, P i s → P i t → s = t)
    (hbad : ∀ n, c n ≠ d n → ∃ i, i < r ∧ P i n) :
    ∃ N, ∀ n, N ≤ n → c n = d n := by
  obtain ⟨N,hN⟩ := finite_single_hits_cutoff r P hone
  refine ⟨N,?_⟩
  intro n hn
  by_cases he : c n = d n
  · exact he
  · obtain ⟨i,hi,hpin⟩ := hbad n he
    exact False.elim (hN i hi n hn hpin)

end ArcTailBounds

/- Component: ArcContinuantsDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcRotationDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcRule30BridgeDraft; proof body retained from the reviewed integration. -/
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

/- Component: ArcEndpointDraft; proof body retained from the reviewed integration. -/
namespace ArcEndpoint

def Hit (endpoint : Nat → ℝ) (alpha theta : ℝ) (i n : Nat) : Prop :=
  ∃ z : ℤ, theta+(n : ℝ)*alpha = endpoint i+z

/-- Two visits to one endpoint class would make alpha a ratio of integers. -/
theorem hit_unique {alpha : ℝ} (ha : Irrational alpha) (endpoint : Nat → ℝ) (theta : ℝ)
    (i s t : Nat) (hs : Hit endpoint alpha theta i s) (ht : Hit endpoint alpha theta i t) : s = t := by
  obtain ⟨z,hz⟩ := hs
  obtain ⟨w,hw⟩ := ht
  by_contra hst
  have hstInt : (s : ℤ) ≠ (t : ℤ) := by exact_mod_cast hst
  have hn : (s : ℤ)-(t : ℤ) ≠ 0 := sub_ne_zero.mpr hstInt
  have hden : (((s : ℤ)-(t : ℤ) : ℤ) : ℝ) ≠ 0 := by exact_mod_cast hn
  apply ha.ne_rational (z-w) ((s : ℤ)-(t : ℤ))
  apply (eq_div_iff hden).2
  push_cast
  nlinarith [hz,hw]

/-- Any colouring which differs only at the listed endpoint translates eventually has the same sampled code.
    No periodicity is needed for its exceptional values at different integer translates. -/
theorem eventual_agreement {r : Nat} (S : ArcStepCode.StepCode r) (g : ℝ → Bool) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hoff : ∀ x : ℝ, (∀ i : Nat, i < r → ∀ z : ℤ, x ≠ S.endpoint i+z) → g x = S.value x) :
    ∃ N : Nat, ∀ n : Nat, N ≤ n →
      g (theta+(n : ℝ)*alpha) = ArcStepCode.orbit S alpha theta n := by
  apply ArcTailBounds.finite_single_hits_eventual
    (fun n => g (theta+(n : ℝ)*alpha)) (ArcStepCode.orbit S alpha theta) r
    (Hit S.endpoint alpha theta)
  · intro i _ s t hs ht
    exact hit_unique ha S.endpoint theta i s t hs ht
  · intro n hbad
    apply Classical.byContradiction
    intro hno
    apply hbad
    apply hoff
    intro i hi z hz
    exact hno ⟨i,hi,z,hz⟩

end ArcEndpoint

/- Component: ArcIntervalCodeDraft; proof body retained from the reviewed integration. -/
namespace ArcIntervalCode

def Member (k : Nat) (a b : Nat → ℝ) (x : ℝ) : Prop :=
  ∃ i : Nat, i < k ∧ ∃ z : ℤ, a i+z ≤ x ∧ x < b i+z

noncomputable def value (k : Nat) (a b : Nat → ℝ) (x : ℝ) : Bool := by
  classical
  exact decide (Member k a b x)

def endpoint (a b : Nat → ℝ) (j : Nat) : ℝ :=
  if j % 2 = 0 then a (j/2) else b (j/2)

theorem endpoint_even (a b : Nat → ℝ) (i : Nat) : endpoint a b (2*i) = a i := by
  have hd : (2*i)/2 = i := by omega
  have hm : (2*i)%2 = 0 := by omega
  simp [endpoint,hd,hm]

theorem endpoint_odd (a b : Nat → ℝ) (i : Nat) : endpoint a b (2*i+1) = b i := by
  have hd : (2*i+1)/2 = i := by omega
  have hm : (2*i+1)%2 = 1 := by omega
  simp [endpoint,hd,hm]

/-- Periodicity by reindexing the integer lift, without a circle quotient API. -/
theorem member_shift (k : Nat) (a b : Nat → ℝ) (x : ℝ) (w : ℤ) :
    Member k a b (x+w) ↔ Member k a b x := by
  constructor
  · rintro ⟨i,hi,z,hlo,hhi⟩
    refine ⟨i,hi,z-w,?_,?_⟩ <;> push_cast <;> linarith
  · rintro ⟨i,hi,z,hlo,hhi⟩
    refine ⟨i,hi,z+w,?_,?_⟩ <;> push_cast <;> linarith

theorem value_eq_of_member_iff (k : Nat) (a b : Nat → ℝ) (x y : ℝ)
    (h : Member k a b x ↔ Member k a b y) : value k a b x = value k a b y := by
  classical
  by_cases hx : Member k a b x
  · have hy := h.mp hx
    simp [value,hx,hy]
  · have hy : ¬ Member k a b y := fun hy => hx (h.mpr hy)
    simp [value,hx,hy]

/-- In a jump-free (x,y] window, the same lifted interval witness works in both directions. -/
theorem member_constant (k : Nat) (a b : Nat → ℝ) (x y : ℝ) (hxy : x ≤ y)
    (hnone : ∀ j : Nat, j < 2*k → ∀ z : ℤ, ¬ (x < endpoint a b j+z ∧ endpoint a b j+z ≤ y)) :
    Member k a b x ↔ Member k a b y := by
  constructor
  · rintro ⟨i,hi,z,hlo,hhi⟩
    have hyhi : y < b i+z := by
      by_contra hnot
      apply hnone (2*i+1) (by omega) z
      simpa only [endpoint_odd] using And.intro hhi (le_of_not_gt hnot)
    exact ⟨i,hi,z,le_trans hlo hxy,hyhi⟩
  · rintro ⟨i,hi,z,hlo,hhi⟩
    have hxlo : a i+z ≤ x := by
      by_contra hnot
      apply hnone (2*i) (by omega) z
      simpa only [endpoint_even] using And.intro (lt_of_not_ge hnot) hlo
    exact ⟨i,hi,z,hxlo,lt_of_le_of_lt hxy hhi⟩

/-- A conventional periodic finite union of half-open intervals satisfies the explicit StepCode interface. -/
noncomputable def code (k : Nat) (a b : Nat → ℝ) : ArcStepCode.StepCode (2*k) where
  value := value k a b
  endpoint := endpoint a b
  periodic := by
    intro x w
    apply value_eq_of_member_iff
    exact member_shift k a b x w
  constant_between := by
    intro x y hxy hnone
    apply value_eq_of_member_iff
    exact member_constant k a b x y hxy hnone

end ArcIntervalCode

/- Component: ArcRule30ExclusionDraft; proof body retained from the reviewed integration. -/
namespace ArcRule30Exclusion

/-- A finite-left Rule30 clock cannot have this large-digit finite-step rotation as its visible neighbour. -/
theorem no_visible_rotation {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∀ s : Nat, ArcRule30Bridge.visible x s = ArcStepCode.orbit S alpha theta s) : False := by
  have hf : ArcRule30Bridge.visible x = ArcStepCode.orbit S alpha theta := funext hvisible
  apply ArcRotation.no_uniform_repeat_bound S alpha theta ha hlarge
  refine ⟨L,fun q hq => ?_⟩
  rw [← hf]
  exact ArcRule30Bridge.repeat_bound x L hleft hzero hclock q hq

/-- Finite endpoint exceptions are harmless once eventual agreement has been supplied.
    This does not assume an eventual physical clock: that clock is still normalized from time zero. -/
theorem no_eventual_visible_rotation {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∃ N : Nat, ∀ s : Nat, N ≤ s →
      ArcRule30Bridge.visible x s = ArcStepCode.orbit S alpha theta s) : False := by
  obtain ⟨N,hN⟩ := hvisible
  apply ArcRotation.no_uniform_repeat_bound S alpha theta ha hlarge
  refine ⟨L+2*N,?_⟩
  exact ArcTailBounds.uniform_eventual_transfer (ArcRule30Bridge.visible x)
    (ArcStepCode.orbit S alpha theta) L N
    (fun q hq => ArcRule30Bridge.repeat_bound x L hleft hzero hclock q hq) hN

/-- Arbitrary changes at the listed endpoint translates cannot evade the same large-digit exclusion.
    A genuine StepCode is still supplied explicitly; no general interval representation is inferred. -/
theorem no_visible_endpoint_variant {r : Nat} (S : ArcStepCode.StepCode r) (g : ℝ → Bool)
    (alpha theta : ℝ) (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (hoff : ∀ y : ℝ, (∀ i : Nat, i < r → ∀ z : ℤ, y ≠ S.endpoint i+z) → g y = S.value y)
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∀ s : Nat, ArcRule30Bridge.visible x s = g (theta+(s : ℝ)*alpha)) : False := by
  obtain ⟨N,hN⟩ := ArcEndpoint.eventual_agreement S g alpha theta ha hoff
  apply no_eventual_visible_rotation S alpha theta ha hlarge x L hleft hzero hclock
  refine ⟨N,?_⟩
  intro s hs
  rw [hvisible s]
  exact hN s hs

/-- Concrete interval-union entry point. Its threshold uses the supplied 2*k labels, not a claimed minimal
    jump count. Arbitrary endpoint values can instead use no_visible_endpoint_variant with this code. -/
theorem no_visible_interval_union (k : Nat) (a b : Nat → ℝ) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(2*k+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∀ s : Nat, ArcRule30Bridge.visible x s =
      ArcIntervalCode.value k a b (theta+(s : ℝ)*alpha)) : False := by
  apply no_visible_rotation (ArcIntervalCode.code k a b) alpha theta ha hlarge x L hleft hzero hclock
  intro s
  exact hvisible s

end ArcRule30Exclusion

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
#print axioms Rule30Submission.ArcCover.same_interval_return
#print axioms Rule30Submission.ArcCover.short_return
#print axioms Rule30Submission.ArcCover.no_repeat_of_cover
#print axioms Rule30Submission.ArcStepCode.crossing
#print axioms Rule30Submission.ArcStepCode.break_has_lift
#print axioms Rule30Submission.ArcStepCode.lift_cover
#print axioms Rule30Submission.ArcStepCode.no_repeat_bound
#print axioms Rule30Submission.ArcTailBounds.shift_repeat_bound
#print axioms Rule30Submission.ArcTailBounds.eventual_transfer
#print axioms Rule30Submission.ArcTailBounds.uniform_eventual_transfer
#print axioms Rule30Submission.ArcTailBounds.finite_single_hits_cutoff
#print axioms Rule30Submission.ArcTailBounds.finite_single_hits_eventual
#print axioms Rule30Submission.ArcDeterminant.continuant_bezout
#print axioms Rule30Submission.ArcDeterminant.continuant_error_lt_next
#print axioms Rule30Submission.ArcRotation.denominator_next
#print axioms Rule30Submission.ArcRotation.previous_margin
#print axioms Rule30Submission.ArcRotation.next_covers_window
#print axioms Rule30Submission.ArcRotation.no_repeat_at_large_digit
#print axioms Rule30Submission.ArcRotation.repeat_bound_fails
#print axioms Rule30Submission.ArcRotation.no_uniform_repeat_bound
#print axioms Rule30Submission.ArcRule30Bridge.repeat_bound
#print axioms Rule30Submission.ArcEndpoint.hit_unique
#print axioms Rule30Submission.ArcEndpoint.eventual_agreement
#print axioms Rule30Submission.ArcIntervalCode.member_shift
#print axioms Rule30Submission.ArcIntervalCode.member_constant
#print axioms Rule30Submission.ArcIntervalCode.code
#print axioms Rule30Submission.ArcRule30Exclusion.no_visible_rotation
#print axioms Rule30Submission.ArcRule30Exclusion.no_eventual_visible_rotation
#print axioms Rule30Submission.ArcRule30Exclusion.no_visible_endpoint_variant
#print axioms Rule30Submission.ArcRule30Exclusion.no_visible_interval_union

end Rule30Submission
